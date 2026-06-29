# Doc Type Audit

Working document for reviewing and finalizing the `doc_type` metadata taxonomy.
Built through a document-by-document review with Nick Lennon (Impact Florida).

## Theory of Action Lens

Every doc_type assignment should be interpretable through Impact Florida's three pillars:

1. **Advance Educator Practice** — documents capturing teacher/leader learning, reflection, and growth within cadres
2. **Serve as a Strategic Connector** — documents from convenings, networks, and cross-district exchanges
3. **Influence Systems** — documents related to policy, funder reporting, district systems, and strategic planning

---

## Audit Structure (per type)

Each entry records:
- **Working definition** — one sentence
- **Theory of action pillar(s)** — which pillar(s) this type primarily serves
- **Logic** — what signals (folder name, filename keywords) put a document here
- **Documents reviewed** — with Drive links and verdict (✓ correct / ✗ wrong / ~ edge case)
- **Re-assignments** — documents that belong elsewhere
- **Final definition** — agreed after review
- **Status** — `in review` / `agreed` / `pending implementation`

---

## Agreed Taxonomy Changes (running log)

| Change | Decision |
|--------|----------|
| `event_survey` → `survey_reflection` | Collapsed — same document type regardless of when administered |
| `baseline_data` → `district_data` | Collapsed — same type of data, collected at entry |
| `virtual_call` → `convening` | Collapsed — same purpose, different modality |
| `gcit_reflection` + `performance_report` → `performance_progress_reporting` | Collapsed — both are structured external reporting |
| `progress_summary` → `cadre_progress_summary` | Renamed — more specific, covers synthesized narrative summaries of cadre progress |
| `site_visit` + convening huddle notes → `field_notes` | Collapsed — raw granular notes from direct engagement, any session type |
| Convening feedback surveys → `survey_reflection` | Re-assigned — these are survey responses, not convening artifacts |
| `podcast_reflection` → `participant_reflection` | Renamed — these are facilitated practitioner reflections, not program feedback; broader than SWS |
| `program_feedback` | New type — participants explicitly evaluating the program (exit surveys, convening feedback, EOY satisfaction) |
| `field_notes` → `program_engagement_notes` | Renamed — avoids confusion with `field_influence`; clearer that these are internal notes from direct program engagement |
| `field_influence` | New type — external publications and advocacy materials aimed at influencing the broader education field |
| `program_delivery` | Renamed from `programming` — materials delivered to participants (decks, agendas, handouts) |
| `program_overview` | New type — program framework, orientation, and description documents |
| `program_planning` | Forward-looking design docs — session agendas, convening plans, curriculum outlines |
| `program_logistics` | New type — operational/admin tracking files: rosters, participant databases, year trackers, email lists, completion logs |
| `program_progress_summary` | Renamed from `cadre_progress_summary` / `progress_summary` — broader than cadre |
| `intake_survey` | Confirmed — includes both district readiness intake forms (Focus K-3) and teacher cadre application/intake responses (SWS) |
| `survey_reflection` → retired | Dissolved into `participant_reflection` (practice reflections) and `program_feedback` (session exit tickets). Format does not determine type. |
| `evaluation_report` | Retained — first-class filter for external evaluator research. Tightened definition: third-party authored only. |
| `impact_report` | New type — polished IF-authored program results: annual reports, impact briefs, results decks. |
| `program_data` | New type — processed quantitative program outcome data, including external evaluator data visualizations. |
| `survey_reflection` → retired | Dissolved into `participant_reflection` (practice reflections in survey form) and `program_feedback` (session/convening exit tickets). Format does not determine type. |

---

## New Metadata Field: `primary_voice`

To be added as a document-level metadata field, derivable primarily from `doc_type` via lookup table. Captures whose perspective/voice is the primary content of the document. More granular voice tagging will happen at the chunk level in the RAG pipeline.

**Values:**
- `teacher` — document primarily reflects teacher perspectives, reflections, or responses
- `student` — document primarily reflects student perspectives or data
- `family` — document primarily reflects family/caregiver perspectives
- `district_leader` — document primarily reflects district staff or leadership perspectives
- `impact_florida_staff` — document is authored by and reflects Impact Florida staff observations
- `external_evaluator` — document produced by an independent external evaluator (e.g. WestEd)
- `mixed` — document meaningfully contains multiple voices

**Derivation logic (lookup from doc_type):**

| doc_type | primary_voice |
|---|---|
| `perts_elevate` | student |
| `podcast_reflection` | teacher |
| `intake_survey` | teacher |
| `eoy_survey` | teacher |
| `survey_reflection` | teacher |
| `network_survey` | mixed |
| `focus_group` | mixed (tagged per document based on who was in the group) |
| `field_notes` | impact_florida_staff |
| `evaluation_report` | external_evaluator |
| `district_artifact` | district_leader |
| `district_data` | impact_florida_staff / district_leader |
| `cadre_progress_summary` | impact_florida_staff |
| `performance_progress_reporting` | impact_florida_staff |
| `grant` | impact_florida_staff |
| `policy` | impact_florida_staff |
| `planning` | impact_florida_staff |
| `programming` | impact_florida_staff |
| `listening_session` | mixed |
| `convening` | mixed |
| `readiness_data` | district_leader |

---

## Doc Types Under Review

---

### `district_data`
**Working definition:** Administrative, assessment, and workforce data from or about districts — retention, attrition, student achievement, FLDOE datasets. Includes baseline data collected at program entry.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keywords: `district data`, `district strengths`, `fldoe`, `survey data and decks`, `baseline data`, `tw baseline`; filename patterns: district name + data/retention/attrition
**Status:** `agreed`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| 1–6 | FLDOE datasets and requests | various | ✓ | State/district administrative data |
| 7 | Focus K-3_Teacher and Leader Perceptions and Use of AI_2026 | [link](https://drive.google.com/file/d/16tWwuKzirxVxRBXci4qzT-VLSl5V_c9E/view?usp=drivesdk) | ✗ | Synthesized insight report from survey → `cadre_progress_summary` |
| 8 | Focus K-3_Teacher and Leader Perspectives on Instructional Materials_2026 | [link](https://drive.google.com/file/d/12aHDlccctJsk6Ud36o3UWrgLdB_VnIJL/view?usp=drivesdk) | ✗ | Synthesized insight report from survey → `cadre_progress_summary` |
| 9–16 | District-specific data reports (Fall 2025, Spring 2026) | various | ✓ | Assessment and achievement data by district |
| 17 | Focus K-3_Cadre-Wide Data Presentation_Fall 2025 | [link](https://docs.google.com/presentation/d/1C1FN8r09HoyJhBd2ltLIJjXAfcaCvUHXkrliwneHSfo/edit?usp=drivesdk) | ✓ | Cadre-wide data deck |
| 18 | Focus K-3_Implementation Pattern Summary_June 2026 | [link](https://drive.google.com/file/d/1JBu3gEmUx7llZu4NsXJZf6RMGl8PdsQ5/view?usp=drivesdk) | ✗ | Monthly insight summary → `cadre_progress_summary` |
| 19 | Focus K-3_Wave 2 Focus Groups Report_June 2026 | [link](https://drive.google.com/file/d/1xkL-fWsDeHQBEJNQamUQxYIBVFLULwot/view?usp=drivesdk) | ✗ | Focus group summary report → `focus_group` |
| 20 | Focus K-3_Wave 1 Focus Groups Report_October 2025 | [link](https://drive.google.com/file/d/181JOWTZTJlZb1ED_5aa-DCHlxgK25HQR/view?usp=drivesdk) | ✗ | Focus group summary report → `focus_group` |
| 21 | Focus K-3_Cadre-Wide Student and Family Empathy Interview Report_Fall 2025 | [link](https://drive.google.com/file/d/1Wbi-avRRlNCU76JucY_ZdH5uVnUv6YC5/view?usp=drivesdk) | ✗ | Student & family interview summary → `focus_group`, `primary_voice: student/family` |
| 22 | Focus K-3_Cross-Site K-3 Math Educator Listening Sessions Report_Fall 2025 | [link](https://drive.google.com/file/d/1b3iUqyMCix3Y48QBCm8JyX79G1D80btN/view?usp=drivesdk) | ✗ | Teacher listening session summary → `focus_group`, `primary_voice: teacher` |
| 23 | District Story_Osceola | [link](https://drive.google.com/file/d/1srnGoExGhpHtIotY4f7iSQeOc7Djp5wo/view?usp=drivesdk) | ✗ | District narrative brief → `district_artifact` |
| 24 | District Story_Hillsborough | [link](https://drive.google.com/file/d/1vWeF8qNSmrsWGxUaZ6QV1rJN_VkRbWPZ/view?usp=drivesdk) | ✗ | District narrative brief → `district_artifact` |
| 25 | District Story_Highlands | [link](https://drive.google.com/file/d/1EBcKkzi2GK3pfHsS81UJ58TKRX5MR4PH/view?usp=drivesdk) | ✗ | District narrative brief → `district_artifact` |
| 26 | District Story_Palm Beach | [link](https://drive.google.com/file/d/1KWDhPswnDKBXpbd3dU2HRL4VEE-00N7n/view?usp=drivesdk) | ✗ | District narrative brief → `district_artifact` |
| 27 | 5 Conditions Measure_April 2026 | [link](https://docs.google.com/spreadsheets/d/1ExZhaYyXhXc5tLMClrw0gLLXyLbDP5N9/edit?usp=drivesdk) | ✓ | Assessment data |
| 28 | Focus K-3_Network Survey - Spring 2026 | [link](https://docs.google.com/spreadsheets/d/1IFV7vXS5WrcX7X9DEFdNqVgJTYr-G207duJhnW0xHAM/edit?usp=drivesdk) | ✗ | Raw survey data → `network_survey` |
| 29 | Focus K-3_Teacher Survey - Spring 2026 | [link](https://docs.google.com/spreadsheets/d/10cuSp6BCKPaQk8A-HSkvZ-qQaKAkAqX43wIrZIEUKcc/edit?usp=drivesdk) | ✗ | Raw survey data → `survey_reflection` |
| 30 | Impact Florida Network Survey - June and September 2025 | [link](https://docs.google.com/spreadsheets/d/1zzp3cdqQY8_x6hI0gK96hMHlrfsqGGjw0rwSweU5oNo/edit?usp=drivesdk) | ✗ | Raw survey data → `network_survey` |
| 31 | Impact FL Teacher Survey - Fall 2025 | [link](https://docs.google.com/spreadsheets/d/1slSiS6G0tvg86FGS6-iEQVU1pYtH-X-OdBwZPNPyW1c/edit?usp=drivesdk) | ✗ | Raw survey data → `survey_reflection` |
| 32 | Impact Florida Network Survey CSV | [link](https://drive.google.com/file/d/1VSspJ4gv7_j7tNS_0m65HYnJ1Jy9oIAH/view?usp=drivesdk) | ✗ | Raw survey data (duplicate CSV) → `network_survey` |
| 33–35 | 5 Conditions, walkthrough, student work review data | various | ✓ | Observational and assessment data |
| 36–40 | Math achievement scatter plot data by district | various | ✓ | Student achievement data |
| 41, 47, 49, 52 | District Strengths Assessments | various | ✓ | District-level assessment data |
| 42 | Focus K-3 Cadre_April 2026 Summary | [link](https://drive.google.com/file/d/1q7UgVjKFz38r8YV9VVOF2kVIobbZexG1/view?usp=drivesdk) | ✗ | Monthly cadre summary → `cadre_progress_summary` |
| 43 | Impact Florida Focus Cadre Teacher Survey CSV | [link](https://drive.google.com/file/d/1pgRxezzjj2He4dhInKt0-rpEISvvAMzC/view?usp=drivesdk) | ✗ | Raw survey data → `survey_reflection` |
| 44 | Impact Florida Focus Cadre Network Survey CSV | [link](https://drive.google.com/file/d/1PXw5d-1oB02N5rS2pSEukMW7Ttu_ZO19/view?usp=drivesdk) | ✗ | Raw survey data → `network_survey` |
| 45–46, 48, 51 | Overall Student Growth by district | various | ✓ | Student achievement data |
| 50 | Impact FL Teacher Survey Fall 2025 CSV | [link](https://drive.google.com/file/d/1mO0dniYISWFwnOnHeSD9acZmHMmS96Re/view?usp=drivesdk) | ✗ | Raw survey data (duplicate CSV) → `survey_reflection` |

**Re-assignments from `district_data`:**
- → `cadre_progress_summary`: 7, 8, 18, 42
- → `focus_group`: 19, 20, 21, 22
- → `district_artifact`: 23, 24, 25, 26
- → `network_survey`: 28, 30, 32, 44
- → `survey_reflection`: 29, 31, 43, 50

**Final definition:** Raw and processed administrative, assessment, and workforce data from districts or state sources (FLDOE). Quantitative in nature. Does not include synthesized reports, summaries, or survey response files — those belong in `cadre_progress_summary`, `focus_group`, `survey_reflection`, or `network_survey` respectively.

---

### `programming`
**Working definition:** Slide decks, agendas, and facilitation materials used to run cadre sessions, convenings, and events.
**Theory of action pillar:** Advance Educator Practice / Strategic Connector
**Logic:** Folder keyword: `!_programming`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `participant_reflection` (was `podcast_reflection`)
**Working definition:** De-identified transcripts of facilitated small-group conversations where practitioners reflect on their own practice — not evaluating the program, but exploring their teaching, their students, and their growth.
**Theory of action pillar:** Advance Educator Practice
**primary_voice:** teacher
**data_form:** raw
**Logic:** Folder keywords: `podcast`, `what counts`
**Status:** `agreed`

| # | Files | Verdict | Notes |
|---|-------|---------|-------|
| 1–27 | All `YYMMDD_F#.docx` transcripts | ✓ | All SWS, all facilitated teacher reflection discussions. Correctly tagged. |

---

### `intake_survey`
**Working definition:** Applications, pre-surveys, and district intake forms capturing baseline participant or district information at program entry.
**Theory of action pillar:** Advance Educator Practice
**Logic:** Folder keywords: `intake`, `application`, `pre-survey`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `site_visit`
**Working definition:** (Pending — likely merging into `field_notes`) Field notes and observational summaries from in-person site visits to districts or schools.
**Theory of action pillar:** Advance Educator Practice / Influence Systems
**Logic:** Folder keyword: `site visit`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `convening`
**Working definition:** (Pending — most documents re-assigned; remainder TBD) Structured multi-district or cadre-wide gatherings for shared learning.
**Theory of action pillar:** Strategic Connector
**Logic:** Folder keyword: `convening`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `survey_reflection`
**Working definition:** Teacher reflection form data, open-ended survey responses, and feedback surveys from within-program cycles or events.
**Theory of action pillar:** Advance Educator Practice
**Logic:** Folder keywords: `survey reflection`, `survey data`, `convening feedback`; absorbs `event_survey`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `perts_elevate`
**Working definition:** Student survey data from the PERTS Elevate tool measuring learning conditions in math classrooms.
**Theory of action pillar:** Advance Educator Practice
**Logic:** Folder keyword: `perts`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `grant`
**Working definition:** Grant documents, award notifications, and narratives submitted to or received from funders.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keyword: `grant`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `evaluation_report`
**Working definition:** Independent evaluation reports, feasibility and usability studies, and data decks — typically produced by external evaluators (e.g. WestEd).
**Theory of action pillar:** Advance Educator Practice / Influence Systems
**Logic:** Folder keywords: `evaluation report`, `data slides`, `wested`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `district_artifact`
**Working definition:** Decks, plans, and reports produced *by* districts (not by Impact Florida) documenting their own workforce or instructional work.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keyword: `district artifact`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `cadre_progress_summary`
**Working definition:** Synthesized narrative summaries of cadre progress — themes, insights, and learnings — for internal strategic use or executive audiences. Formerly `progress_summary`.
**Theory of action pillar:** Advance Educator Practice / Strategic Connector
**Logic:** Folder keywords: `progress summar`, `cadre summar`, `monthly progress`; call notes that summarize program progress
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `field_notes`
**Working definition:** Granular internal notes capturing raw observations from direct engagement — site visits, convenings, listening sessions, or calls. Written in the moment or immediately after.
**Theory of action pillar:** Advance Educator Practice / Strategic Connector
**Logic:** Folder keywords: `site visit`, `listening session`, `huddle tool`, `meeting notes`, `call notes`, `field notes`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `performance_progress_reporting`
**Working definition:** Structured reports on program performance and progress submitted to external funders or oversight bodies. Formerly `gcit_reflection` and `performance_report`.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keywords: `gcit`, `mid-year reflection`, `annual performance`, `performance report`, `gates`, `results tracker`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `policy`
**Working definition:** Policy briefs, legislative trackers, lobbying notes, and field notes from the policy and advocacy workstream.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keywords: `policy`, `hqim planning`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `planning`
**Working definition:** Internal planning documents, concept papers, implementation plans, and frameworks under development.
**Theory of action pillar:** Advance Educator Practice / Influence Systems
**Logic:** Folder keywords: `planning document`, `concept and district`, `spark planning`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `readiness_data`
**Working definition:** District readiness and needs assessment responses capturing baseline context at program entry — distinct from individual participant intake surveys.
**Theory of action pillar:** Influence Systems
**Logic:** Folder keyword: `readiness data`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `eoy_survey`
**Working definition:** End-of-year survey data and summary reports capturing participant outcomes at program close.
**Theory of action pillar:** Advance Educator Practice
**Logic:** Folder keywords: `eoy survey`, `end of year`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

### `network_survey`
**Working definition:** Survey data from the broader Impact Florida network — cross-program, not tied to a single cadre or district.
**Theory of action pillar:** Strategic Connector
**Logic:** Folder keyword: `network survey`
**Status:** `in review`

| # | File | Drive Link | Verdict | Notes |
|---|------|------------|---------|-------|
| | | | | |

---

## Nulls to Assign

25 documents currently have no `doc_type`. To be assigned after the main audit is complete.

| # | File | Program | Proposed | Verdict |
|---|------|---------|----------|---------|
| 1 | Impact Florida_2026 ISEA Hackweek Guide | Background | `planning` | |
| 2 | EIR Mid-Phase Q2 Performance Report_2025 | EIR/GBL | `performance_progress_reporting` | |
| 3 | TW_Outcomes Survey Context_2025 | Teacher Workforce | `district_data` | |
| 4 | TW_Cross-District Data Slide Deck_2025 | Teacher Workforce | `district_data` | |
| 5 | Network Survey_TW Questions Only_Data Report_2025 | Teacher Workforce | `network_survey` | |
| 6 | TW Update to Gates_May 2025 | Teacher Workforce | `performance_progress_reporting` | |
| 7 | TW Ongoing Funder Check-In Notes | Teacher Workforce | `cadre_progress_summary` | |
| 8 | TW_Outcomes Survey Responses_2025 - De-id | Teacher Workforce | `survey_reflection` | |
| 9 | Polk County_24.25 School Retention Data | Teacher Workforce | `district_data` | |
| 10 | EIR Running Biweekly Call Notes | EIR/GBL | `field_notes` | |
| 11 | EIR Mid-Phase Annual Performance Report 1_2024 | EIR/GBL | `performance_progress_reporting` | |
| 12 | EIR Registry of Efficacy and Effectiveness | EIR/GBL | `evaluation_report` | |
| 13 | Legends of Learning Usability Study | EIR/GBL | `evaluation_report` | |
| 14 | EIR Results Tracker | Multiple Programs | `performance_progress_reporting` | |
| 15 | Gates Results Tracker | Multiple Programs | `performance_progress_reporting` | |
| 16 | Legends of Learning Feasibility Study Report | EIR/GBL | `evaluation_report` | |
| 17 | Feasibility Study Executive Summary | EIR/GBL | `evaluation_report` | |
| 18 | Weekly SPARK Meeting Notes | SPARK | `field_notes` | |
| 19 | SWS_Historical Account of Cadre | SWS | `cadre_progress_summary` | |
| 20 | SWS_Monthly Funder Check-In Call Notes | SWS | `cadre_progress_summary` | |
| 21 | Focus K-3 Monthly Progress Summaries | Focus K-3 | `cadre_progress_summary` | |
| 22 | UW Sponsor Agreement | Background | `grant` | |
| 23 | Impact Florida Sponsor Application ISEA | Background | `grant` | |
| 24 | Focus K-3 Cadre Summaries | Focus K-3 | `cadre_progress_summary` | |
| 25 | Cohort B Data Slides Fall 2025 | Teacher Workforce | `district_data` | |

---

### `intake_survey`
**Working definition:** Application and intake forms — teacher cadre applications (SWS) and district readiness intake forms (Focus K-3). Captures baseline context, qualifications, and intent at program entry.
**Theory of action pillar:** Advance Educator Practice (teacher applications); Influence Systems (district readiness)
**Logic:** Folder keywords: `applications, intake forms, pre-surveys`, `district intake surveys`; filename patterns: `application`, `intake survey`, `pre-survey`
**Status:** `agreed`

**Re-assignments from this type:**
| # | File | Old type | New type | Reason |
|---|------|----------|----------|--------|
| 2 | SWS Year 5 Tracker_Completion & Coaching Log_25-26 | intake_survey | program_logistics | Operational tracker, not intake data |
| 9 | SWS_Master Participant Database | intake_survey | program_logistics | Master roster/database |
| 10 | 24-25 Coaching Call Log, Coaching Feedback, Survey 1 Reflection | intake_survey | program_engagement_notes | Coaching log — internal staff notes from direct program engagement |
| 11 | 24-25 NEW SWS Application Acceptance | intake_survey | program_logistics | Acceptance tracking sheet |
| 12 | 23-24 SWS Y3 Alumni Information | intake_survey | program_logistics | Alumni roster |
| 15 | 22-23 Elevate OFFICIAL Teacher Cadre | intake_survey | program_logistics | Cadre roster |
| 17 | EMAILS of 25-26 SWS Year 5 Tracker | intake_survey | program_logistics | Contact/tracker sheet |
| 19 | 23-24 Year 3 Tracker | intake_survey | program_logistics | Year tracker |

**Confirmed as intake_survey (20 docs):**
1, 3–8, 13–14, 16, 18, 20 (SWS application/intake responses), 21–24 (Focus K-3 district intake surveys)

**Final definition:** Application and intake survey responses from teachers entering cadre programs, and district readiness intake forms completed at program onboarding.
**primary_voice:** teacher (SWS applications); district_leader (Focus K-3 district forms)
**data_form:** raw

---

### `site_visit`
**Working definition (old):** Notes and data from in-person site visits to districts or schools.
**Status:** `agreed` — type dissolved, all docs re-assigned

**Re-assignments:**

| # | File | New type | Reason |
|---|------|----------|--------|
| 1 | Polk Site Visit Notes_July 2025 | `program_engagement_notes` | Raw staff notes from site visit |
| 2 | Osceola Site Visit Notes_June 2025 | `program_engagement_notes` | Raw staff notes from site visit |
| 3 | Osceola Site Visit Notes (Internal)_June 2025 | `program_engagement_notes` | Raw internal staff notes |
| 4 | Lee Site Visit Notes_July 2025 | `program_engagement_notes` | Raw staff notes from site visit |
| 5 | MMC Cross-District Learning Walk Synthesis | `program_progress_summary` | Synthesized cross-district summary |
| 6 | MMC Hillsborough Learning Walk Summary and Debrief | `program_progress_summary` | Synthesized summary/debrief |
| 7 | MMC Lake Learning Walk Summary and Debrief | `program_progress_summary` | Synthesized summary/debrief |
| 8 | MMC Brevard Learning Walk Summary and Debrief | `program_progress_summary` | Synthesized summary/debrief |
| 9 | MMC Volusia Learning Walk Summary and Debrief | `program_progress_summary` | Synthesized summary/debrief |
| 10 | Site Visits 1 and 2 Survey_Aug-Oct 2025 | `survey_reflection` (hold) | Raw teacher survey responses — may collapse with `program_feedback` |
| 11 | Site Visit 5 Survey_Feb-Mar 2026 | `survey_reflection` (hold) | Raw teacher survey responses |
| 12 | Reflection on Year 1_Additions to SV 5 Data | `survey_reflection` (hold) | Raw teacher survey responses |
| 13 | Site Visit 5 Meeting Notes | `program_engagement_notes` | Raw staff meeting notes |
| 14 | Site Visit 4 Survey_January 2026 | `survey_reflection` (hold) | Raw teacher survey responses |
| 15 | Site Visit 4 Meeting Notes | `program_engagement_notes` | Raw staff meeting notes |
| 16 | Site Visit 3 Survey_November 2025 | `survey_reflection` (hold) | Raw teacher survey responses |
| 17 | Site Visit 3 Meeting Notes | `program_engagement_notes` | Raw staff meeting notes |
| 18 | Hillsborough Kickoff Survey_September 2025 | `survey_reflection` (hold) | Raw teacher survey responses |
| 19 | Focus K-3 Cadre Summary_March 2026 | `program_progress_summary` | Synthesized cadre summary |
| 20 | Focus K-3 Cadre_November 2025 Summary | `program_progress_summary` | Synthesized cadre summary |
| 21 | Site Visit 3 Survey (duplicate) | `survey_reflection` (hold) | Raw teacher survey responses |
| 22 | Site Visit 1 Meeting Notes | `program_engagement_notes` | Raw staff meeting notes |
| 23 | Focus K-3 Cadre Summary_September 2025 | `program_progress_summary` | Synthesized cadre summary |

**Flag:** `survey_reflection` (hold) docs 10–12, 14, 16, 18, 21 — revisit when auditing `survey_reflection` to assess whether `program_feedback` and `survey_reflection` should collapse.

---

### `convening`
**Working definition (old):** Documents from or about convenings — both planning and feedback artifacts.
**Status:** `agreed` — type dissolved, all docs re-assigned

**Re-assignments:**

| # | File | New type | Reason |
|---|------|----------|--------|
| 1–6 | TW Convening Feedback Survey Responses (various dates) | `survey_reflection` (hold) | Raw participant feedback surveys — revisit when auditing `survey_reflection` |
| 7–12 | Focus K-3 Convening surveys (Day 1/2, Slido) | `survey_reflection` (hold) | Raw participant feedback surveys |
| 13 | Convening Team Huddle Tool_December 2025 | `program_engagement_notes` | Internal staff notes from running the convening |
| 14 | Convening Team Huddle Tool_February 2026 | `program_engagement_notes` | Internal staff notes from running the convening |
| 15 | Focus K-3 Cadre Summaries_October 2025 | `program_progress_summary` | Synthesized cadre summary |
| 16–18 | Convening 1 Survey zip files (Doug Clements, K12 Lift, Overall) | `survey_reflection` (hold) | Raw participant survey data |

**Flag:** All survey docs (1–12, 16–18) held as `survey_reflection` — same boundary question as site_visit surveys. Decide `program_feedback` vs. `survey_reflection` collapse when auditing `survey_reflection`.

---

### `survey_reflection`
**Working definition (old):** Survey-format reflections from participants or session feedback.
**Status:** `agreed` — type retired, all docs re-assigned. Format (survey vs. audio) does not determine type; content does.

**Re-assignments:**

| # | File | New type | Reason |
|---|------|----------|--------|
| 1 | SWS June 2026 Day 1 Exit Ticket | `program_feedback` | Evaluating a convening session |
| 2 | SWS June 2026 Day 2 Exit Ticket | `program_feedback` | Evaluating a convening session |
| 3 | SWS June 2025 Day 2 Exit Ticket | `program_feedback` | Evaluating a convening session |
| 4 | SWS June 2025 Day 1 Exit Ticket | `program_feedback` | Evaluating a convening session |
| 5–12 | SWS Cycle A–E and Survey 1–4 Reflection Forms | `participant_reflection` | Teachers reflecting on their own practice — same content as podcast reflections, different format |
| 13 | 23-24 Survey 2 Reflections.docx | `participant_reflection` | Narrative practitioner reflections |
| 14 | 23-24 Survey 3 Data and Reflections.docx | `participant_reflection` | Narrative practitioner reflections |
| 15 | 23-24 Survey 1 Reflections.docx | `participant_reflection` | Narrative practitioner reflections |

**Cascading re-assignments (held from prior audits):**
- All convening feedback surveys (convening audit, docs 1–12, 16–18) → `program_feedback`
- All site visit survey spreadsheets (site_visit audit, docs 10–12, 14, 16, 18, 21) → `program_feedback`

**Taxonomy change logged:** `survey_reflection` retired. Add to agreed changes log.

---

### `perts_elevate`
**Working definition:** Raw student survey data exports and codebooks from the PERTS Elevate platform, disaggregated by teacher.
**Theory of action pillar:** Advance Educator Practice
**primary_voice:** student
**data_form:** raw
**Status:** `agreed` — type definition confirmed. All 15 current docs appear to be in Google Drive trash and will be excluded from corpus on next pipeline re-run. Type retained in taxonomy for future use.

**Note:** `get_docs.py` was updated this session to add `q="trashed = false"` to the Drive API query — trashed files will no longer be ingested.

---

### `grant`
**Working definition:** Grant applications, narratives, and award notifications submitted to or received from funders.
**Theory of action pillar:** Influence Systems
**primary_voice:** impact_florida_staff
**data_form:** summarized
**Status:** `agreed` — all 10 confirmed. Note: several grants exist as both .docx and .pdf — format duplicates, not a metadata issue.

---

### `evaluation_report`
**Working definition:** Formal third-party research or evaluation reports — external evaluator authored, about a specific tool, intervention, or program.
**Theory of action pillar:** Influence Systems / Advance Educator Practice
**primary_voice:** external_evaluator
**data_form:** summarized
**Status:** `agreed` — type retained. Distinct from `impact_report` (IF-authored) and `program_data` (quantitative data outputs). First-class RAG filter for external evidence.

**Re-assignments from this audit (originally tagged evaluation_report):**

| # | File | New type | Reason |
|---|------|----------|--------|
| 1 | SWS Impact Brief | `impact_report` | IF-authored, not external evaluation |
| 2 | SWS 2024-25 Data Slides | `impact_report` | IF-authored program results |
| 3 | SWS PERTS Graphs From WestEd_2023-24 | `program_data` | External evaluator data visualization, not narrative report |
| 4 | SWS PERTS Grade-Level Visualizations from WestEd | `program_data` | External evaluator data visualization |
| 5 | SWS Year 3 Report_2023-24 | `impact_report` | Annual IF program report |
| 6 | SWS Impact Report_2024-25 | `impact_report` | Annual IF program report |
| 7 | SWS Year 2 Report_2022-23 | `impact_report` | Annual IF program report |
| 8 | SWS Evaluation Report_2022 | `impact_report` | Annual IF program report |
| 9 | Solving with Students Results Slides | `impact_report` | IF-authored program results |
| 10 | 23-24 WestEd PERTS Teacher-Level Visualizations | `program_data` | External evaluator data visualization |

**Confirmed as evaluation_report (previously null):**
- EIR/GBL Registry of Efficacy and Effectiveness Studies — Evaluation Plan
- Legends of Learning Usability Study — Key Findings Deck
- Legends of Learning Feasibility Study Report_July 2025
- Feasibility Study Executive Summary_June 2025

**New types added this audit:**
- `impact_report` — polished comprehensive program results: annual reports, impact briefs, results decks. IF-authored. (`primary_voice: impact_florida_staff`, `data_form: summarized`)
- `program_data` — processed quantitative data about program outcomes, including external evaluator data deliverables. (`data_form: summarized`, `primary_voice` varies)

---

### `district_artifact`
**Working definition:** Documents produced by districts themselves — strategic plans, retention/recruitment plans, data reports, and presentations authored by district staff.
**Theory of action pillar:** Influence Systems
**primary_voice:** district_leader
**data_form:** summarized
**Status:** `agreed` — all 8 confirmed. All Teacher Workforce, all from `3_District Artifacts` folder.

---

### `field_influence` (was `policy`)
**Working definition:** Documents related to understanding and influencing the broader education policy and practice field — external-facing policy briefs, internal policy tracking, legislative notes, landscape scans, and advocacy materials.
**Theory of action pillar:** Influence Systems
**primary_voice:** impact_florida_staff
**data_form:** raw (trackers/notes) or summarized (briefs/reports)
**Status:** `agreed` — renamed from `policy`. Broader than external publications; includes internal tracking and thinking that is part of the field influence work.

| # | File | Verdict | Notes |
|---|------|---------|-------|
| 1 | Florida Policy News Tracker_2024 | ✓ `field_influence` | Internal tracking of policy landscape |
| 2 | Policy Lead_Conceptual Notes from the Field | ✓ `field_influence` | Internal conceptual notes on field influence |
| 3 | Optimizing Florida's Textbook Adoption Timeline Policy Impact | ✓ `field_influence` | External-facing policy impact doc |
| 4 | Legislative Session 2025 — Lobbyist Call Notes | ✓ `field_influence` | Internal notes on field influence activity |
| 5 | Mayernick Session Updates 2025 | ✓ `field_influence` | Legislative session updates |
| 6 | NAT HQIM Landscape Scan Framework | ✓ `field_influence` | Framework for understanding the field |
| 7 | HQIM Policy Impact_Hillsborough County | ✓ `field_influence` | External-facing policy impact doc |
| 8 | Practice-to-Policy Lab One Pager | ✗ → `program_overview` | One-pager describing a program initiative, not field influence work |

---

### `program_planning` (was `planning`)
**Working definition:** Forward-looking design and operational documents — implementation plans, onboarding processes, support frameworks, readiness assessments, kickoff decks.
**Theory of action pillar:** Advance Educator Practice / Serve as a Strategic Connector
**primary_voice:** impact_florida_staff
**data_form:** summarized
**Status:** `agreed` — renamed from `planning`. All 7 docs are SPARK.

| # | File | Verdict | Notes |
|---|------|---------|-------|
| 1 | SPARK Kickoff Deck_2026 | ✓ `program_planning` | Forward-looking kickoff design |
| 2 | SPARK District Overview Doc | ✗ → `program_overview` | Describes the program, not a planning doc |
| 3 | SPARK Program Concept (January 2026) | ✗ → `program_overview` | Program concept/description |
| 4 | SPARK District Support Framework | ✓ `program_planning` | Operational framework doc |
| 5 | SPARK District Readiness & Needs Assessment | ✓ `program_planning` | Planning tool for district onboarding |
| 6 | SPARK District Onboarding Process | ✓ `program_planning` | Operational process doc |
| 7 | SPARK Implementation Plan | ✓ `program_planning` | Forward-looking implementation design |

---

### `eoy_survey`
**Status:** `agreed` — type retired. All docs re-assigned to `program_feedback`. EOY surveys are program feedback regardless of timing; the `academic_year` and `season` fields carry the timing signal.

| # | File | New type |
|---|------|----------|
| 1 | SWS Final EOY Survey_2025-26 | `program_feedback` |
| 2 | SWS Post-Survey Data Question 7_2022 | `program_feedback` |
| 3 | SWS Post-Survey Year 1 Instrument_2022 | `program_feedback` |
| 4 | SWS Post-Survey Data by Question_2022 | `program_feedback` |
| 5 | SWS Final Post-Survey_2022-23 | `program_feedback` |
| 6 | SWS Final EOY Survey_2024-25 | `program_feedback` |

---

### `network_survey`
**Status:** `agreed` — type retired. All 3 docs re-assigned to `program_feedback`. Network surveys are program feedback from MMC cadre participants.

| # | File | New type |
|---|------|----------|
| 1 | MMC Network Survey Data_March 2026 | `program_feedback` |
| 2 | MMC Network Survey Data_October 2025 | `program_feedback` |
| 3 | MMC Cadre Network Survey_Spring 2026 | `program_feedback` |

---

### `readiness_data`
**Status:** `agreed` — type retired. Both docs re-assigned; type not meaningfully distinct from existing types.

| # | File | New type | Reason |
|---|------|----------|--------|
| 1 | SPARK District Readiness and Needs Assessment_6.16.26 | `intake_survey` | District completing an onboarding/entry form |
| 2 | Needs/Readiness Assessment Breakout Room Notes | `program_engagement_notes` | Internal staff notes from the assessment session |

---

### `focus_group`
**Status:** `agreed` — type retired. All docs re-assigned to `program_feedback`.

| # | File | New type |
|---|------|----------|
| 1 | SWS District Leader Focus Group Summary - RR | `program_feedback` |

**Cascading re-assignments (from district_data audit):**
- Focus K-3 Wave 1/2 Focus Groups Reports → `program_feedback`
- Focus K-3 Student and Family Empathy Interview Report → `program_feedback`
- Focus K-3 Cross-Site K-3 Math Educator Listening Sessions Report → `program_feedback`

---

### `listening_session`
**Status:** `agreed` — type retired without individual doc review. All 9 docs → `program_feedback`. Listening sessions are a data collection method capturing participant voice; content is program feedback.
