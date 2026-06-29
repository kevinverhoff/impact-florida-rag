"""
Survey statistics helper for spreadsheet files.

Loads an .xlsx/.xls/.csv file from disk and returns descriptive statistics
for Likert/categorical columns and numeric columns only.

Used by the survey_stats tool in tools.py — never imported at module level
so pandas/openpyxl are only required when the tool is actually called.

Column classification:
  - Metadata cols  : Respondent ID, Collector ID, timestamps — skipped
  - Likert/category: <= MAX_CATEGORIES unique non-null values — value counts + %
  - Numeric        : purely numeric columns — mean, median, min, max
  - Open-ended     : high-cardinality text — skipped (quantitative only)
"""

from __future__ import annotations

from pathlib import Path

import difflib
import pandas as pd

MAX_CATEGORIES = 10  # columns with <= this many unique values → categorical
MIN_RESPONSES  = 2   # skip columns with fewer non-null responses than this

# Column fragments that identify metadata / admin columns to skip
_SKIP_FRAGMENTS = [
    "respondent id", "collector id", "start date", "end date",
    "ip address", "email address", "first name", "last name",
    "unnamed:",
]


def _is_skip(col: str) -> bool:
    low = col.lower()
    return any(frag in low for frag in _SKIP_FRAGMENTS)


def _load(path: Path) -> pd.DataFrame:
    """
    Load spreadsheet and normalise to a clean respondent-per-row DataFrame.

    Handles three export formats:
      - Standard     : row 0 = headers, rows 1+ = respondents
      - SurveyMonkey : row 0 = headers, row 1 = sub-headers, rows 2+ = respondents
      - Qualtrics    : row 0 = short labels, row 1 = full question text,
                       row 2 = JSON ImportId metadata, rows 3+ = respondents
    """
    ext = path.suffix.lower()
    raw = pd.read_csv(path, header=None, dtype=str) if ext == ".csv" \
        else pd.read_excel(path, header=None, dtype=str)

    if len(raw) < 2:
        return raw

    # --- Qualtrics detection ---
    # Row 2 contains JSON ImportId objects
    row2 = raw.iloc[2].fillna("").astype(str)
    if row2.str.contains(r'\{"ImportId"', regex=True).sum() >= 3:
        # Use row 1 (full question text) as column headers; data starts at row 3
        df = raw.iloc[3:].copy()
        df.columns = raw.iloc[1].fillna("").astype(str).tolist()
        return df.reset_index(drop=True)

    # --- SurveyMonkey detection ---
    # Row 0 = parent question text (or admin label)
    # Row 1 = sub-question text OR marker values ("Response", "Open-Ended Response", etc.)
    # Rows 2+ = respondents
    #
    # Strategy: build composite column headers by joining row 0 + row 1 where both
    # are meaningful. This preserves the specific sub-question text that carries
    # the keywords staff actually search for (e.g. "logistics", "facilitated").

    _skip_vals = {"response", "open-ended response", "other (please specify)", "nan", ""}

    row0 = raw.iloc[0].fillna("").astype(str).str.strip()
    row1 = raw.iloc[1].fillna("").astype(str).str.strip()

    headers = []
    prev_parent = ""
    for r0, r1 in zip(row0, row1):
        r0_clean = r0 if r0.lower() not in _skip_vals else ""
        r1_clean = r1 if r1.lower() not in _skip_vals else ""

        # Track the last non-empty parent so NaN-continued cols inherit it
        if r0_clean:
            prev_parent = r0_clean

        if r0_clean and r1_clean and r0_clean != r1_clean:
            # Sub-question: "Please rate... > Today was a good use of my time."
            headers.append(f"{r0_clean} > {r1_clean}")
        elif r1_clean:
            headers.append(r1_clean)
        elif r0_clean:
            headers.append(r0_clean)
        else:
            # Both empty — inherit parent if available (continuation column)
            headers.append(prev_parent or f"col_{len(headers)}")

    df = raw.iloc[2:].copy()
    df.columns = headers
    return df.reset_index(drop=True)


def _col_stats(series: pd.Series) -> dict:
    """Return stats dict for a single column."""
    _sub_header_vals = {"response", "open-ended response", "other (please specify)"}
    clean = series.dropna().astype(str).str.strip()
    clean = clean[clean != ""]
    clean = clean[~clean.str.lower().isin(_sub_header_vals)]

    if len(clean) < MIN_RESPONSES:
        return {}

    # Try numeric first
    numeric = pd.to_numeric(clean, errors="coerce")
    if numeric.notna().sum() / len(clean) >= 0.8:
        return {
            "type":     "numeric",
            "n":        int(numeric.notna().sum()),
            "mean":     round(float(numeric.mean()), 2),
            "median":   round(float(numeric.median()), 2),
            "min":      round(float(numeric.min()), 2),
            "max":      round(float(numeric.max()), 2),
        }

    unique_vals = clean.nunique()

    if unique_vals <= MAX_CATEGORIES:
        counts = clean.value_counts()
        total  = counts.sum()
        dist   = {
            val: {"n": int(n), "pct": round(100 * n / total, 1)}
            for val, n in counts.items()
        }
        return {
            "type":         "categorical",
            "n":            int(total),
            "distribution": dist,
        }

    # Open-ended (high-cardinality text) — skip, quantitative only
    return {}



def _find_group_col(df: pd.DataFrame, group_by: str) -> str | None:
    """Return the first column whose header contains group_by (case-insensitive)."""
    frag = group_by.lower()
    for col in df.columns:
        if frag in col.lower() and not _is_skip(col):
            return col
    return None


def _infer_grouping_cols(df: pd.DataFrame, n: int = 3) -> list[str]:
    """
    Return candidate grouping columns — low-cardinality non-admin cols
    among the first `n` non-skipped columns (district, role, school, etc.).
    """
    candidates = []
    checked = 0
    for col in df.columns:
        if _is_skip(col):
            continue
        checked += 1
        if checked > n:
            break
        clean = df[col].dropna().astype(str).str.strip()
        clean = clean[clean != ""]
        # Exclude Likert-scale columns by checking for agreement/frequency terms
        vals_lower = set(clean.str.lower().unique())
        likert_terms = {"agree", "strongly agree", "slightly agree", "disagree",
                        "strongly disagree", "slightly disagree", "neutral",
                        "always", "often", "sometimes", "rarely", "never",
                        "yes", "no", "true", "false"}
        if vals_lower & likert_terms:
            continue
        if 1 < clean.nunique() <= MAX_CATEGORIES:
            candidates.append(col)
    return candidates


def _render_stats(stats: dict, indent: str = "  ") -> list[str]:
    """Render a stats dict to lines with optional indent prefix."""
    lines = []
    if stats["type"] == "categorical":
        lines.append(f"{indent}n={stats['n']} responses")
        for val, info in stats["distribution"].items():
            lines.append(f"{indent}- {val}: {info['n']} ({info['pct']}%)")
    elif stats["type"] == "numeric":
        lines.append(
            f"{indent}n={stats['n']}  mean={stats['mean']}  "
            f"median={stats['median']}  range={stats['min']}–{stats['max']}"
        )
    elif stats["type"] == "open_ended":
        lines.append(f"{indent}n={stats['n']} open-ended responses. Sample:")
        for s in stats["samples"]:
            lines.append(f'{indent}> "{s}"')
    return lines


def _match_question_cols(
    df: "pd.DataFrame",
    frag: str,
    group_col: "str | None",
) -> tuple:
    """Return (matched_cols, was_fuzzy) with three-pass matching.

    Pass 1 — exact substring (original behaviour, no change in precision).
    Pass 2 — word-prefix overlap: every fragment word must be a prefix of, or
             prefixed by, some word in the column header.  Catches verb-form
             differences (discussed -> discuss, identifies -> identify, etc.).
    Pass 3 — difflib sliding-window ratio >= 0.72 on the fragment-length
             window of words with the best score.
    """
    candidates = [
        col for col in df.columns
        if not _is_skip(col) and col != group_col
    ]

    # Pass 1: exact substring
    exact = [col for col in candidates if frag in col.lower()]
    if exact:
        return exact, False

    # Pass 2: word-prefix overlap
    frag_words = frag.split()
    def _word_prefix(col: str) -> bool:
        col_words = col.lower().split()
        for fw in frag_words:
            if not any(cw.startswith(fw) or fw.startswith(cw) for cw in col_words):
                return False
        return True

    prefix_matches = [col for col in candidates if _word_prefix(col)]
    if prefix_matches:
        return prefix_matches, True

    # Pass 3: difflib sliding-window ratio
    nfw = len(frag_words)
    def _best_ratio(col: str) -> float:
        col_words = col.lower().split()
        best = difflib.SequenceMatcher(None, frag, col.lower()).ratio()
        for i in range(max(1, len(col_words) - nfw + 1)):
            window = " ".join(col_words[i : i + nfw])
            r = difflib.SequenceMatcher(None, frag, window).ratio()
            if r > best:
                best = r
        return best

    THRESHOLD = 0.72
    scored = [(col, _best_ratio(col)) for col in candidates]
    scored = [(col, r) for col, r in scored if r >= THRESHOLD]
    scored.sort(key=lambda x: -x[1])
    if scored:
        return [col for col, _ in scored], True

    return [], False


def survey_stats_for_file(
    path: Path,
    question_fragment: str | None = None,
    group_by: str | None = None,
    display_name: str | None = None,
) -> str:
    """
    Return a formatted stats summary for a survey spreadsheet.

    question_fragment: filter to columns whose header contains this string.
    group_by: fragment matching a grouping column (e.g. "district", "role",
              "school"). When provided, stats are broken out per group value.
              Pass "?" to list available grouping columns without computing stats.
    """
    if not path.exists():
        return f"File not found: {path}"

    try:
        df = _load(path)
    except Exception as exc:
        return f"Could not load file: {exc}"

    if df.empty:
        return "File is empty."

    # Resolve grouping column
    group_col: str | None = None
    if group_by:
        if group_by.strip() == "?":
            candidates = _infer_grouping_cols(df)
            if not candidates:
                return "No suitable grouping columns found (low-cardinality non-admin columns)."
            return "Available grouping columns:\n" + "\n".join(f"  - {c}" for c in candidates)
        group_col = _find_group_col(df, group_by)
        if group_col is None:
            candidates = _infer_grouping_cols(df)
            suggestion = f" Try one of: {', '.join(candidates)}" if candidates else ""
            return f"No column matching '{group_by}' found.{suggestion}"

    n_respondents = len(df)
    label = display_name or path.name

    frag = question_fragment.lower().strip() if question_fragment else None

    # Collect question columns to analyse
    fuzzy_used = False
    if frag is None:
        question_cols = [
            col for col in df.columns
            if not _is_skip(col) and col != group_col
        ]
    else:
        question_cols, fuzzy_used = _match_question_cols(df, frag, group_col)

    if not question_cols:
        if frag:
            # Offer the closest column as a hint
            all_cols = [c for c in df.columns if not _is_skip(c) and c != group_col]
            close = difflib.get_close_matches(frag, [c.lower() for c in all_cols], n=3, cutoff=0.4)
            hint = (
                f"  Closest column headers: {', '.join(repr(c) for c in close)}"
                if close else ""
            )
            return f"No columns matching '{question_fragment}' found in {path.name}.{hint}"
        return "No scoreable columns found."

    header = f"**{label}** — {n_respondents} respondents\n"
    if group_col:
        header += f"Grouped by: {group_col}\n"
    if fuzzy_used:
        lines = [f"*(fuzzy match for '{question_fragment}')*\n", header]
    else:
        lines = [header]

    if group_col is None:
        # --- Ungrouped ---
        matched = 0

        for col in question_cols:
            stats = _col_stats(df[col])
            if not stats or stats["type"] == "open_ended":
                continue
            matched += 1
            lines.append(f"**Q: {col}**")
            lines.extend(_render_stats(stats))
            lines.append("")

        if matched == 0:
            return "No scoreable columns found."

    else:
        # --- Grouped ---
        groups = (
            df[group_col].fillna("").astype(str).str.strip()
            .replace("", "Unknown")
        )
        group_values = [v for v in groups.unique() if v and v != "Unknown"]
        group_values = sorted(group_values)
        if "Unknown" in groups.values:
            group_values.append("Unknown")

        matched = 0
        for col in question_cols:
            # Only show columns with meaningful stats in at least one group
            overall = _col_stats(df[col])
            if not overall:
                continue
            # Skip open-ended when grouped — not meaningful to split samples
            if overall["type"] == "open_ended":
                continue
            matched += 1
            lines.append(f"**Q: {col}**")

            for gval in group_values:
                mask  = groups == gval
                stats = _col_stats(df.loc[mask, col])
                if not stats:
                    continue
                lines.append(f"  **{gval}** (n={stats['n']})")
                lines.extend(_render_stats(stats, indent="    "))

            lines.append("")

        if matched == 0:
            return f"No scoreable columns found when grouped by '{group_col}'."

    return "\n".join(lines)
