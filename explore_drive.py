"""
Explore a Google Shared Drive via service account credentials.

Outputs:
  - Folder tree with per-folder file counts
  - File type summary (count by MIME type)
  - Total file count

Requires:
  .env:       SHARED_DRIVE_ID=<your shared drive id>
  secrets/:   A single service account JSON key file
"""

import os
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

MIME_LABELS = {
    "application/vnd.google-apps.folder": "Google Folder",
    "application/vnd.google-apps.document": "Google Doc",
    "application/vnd.google-apps.spreadsheet": "Google Sheet",
    "application/vnd.google-apps.presentation": "Google Slides",
    "application/vnd.google-apps.form": "Google Form",
    "application/pdf": "PDF",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "Word (.docx)",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "Excel (.xlsx)",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "PowerPoint (.pptx)",
    "application/msword": "Word (.doc)",
    "application/vnd.ms-excel": "Excel (.xls)",
    "application/vnd.ms-powerpoint": "PowerPoint (.ppt)",
    "text/plain": "Plain Text",
    "text/csv": "CSV",
    "image/jpeg": "JPEG Image",
    "image/png": "PNG Image",
    "image/gif": "GIF Image",
    "video/mp4": "MP4 Video",
    "audio/mpeg": "MP3 Audio",
    "application/zip": "ZIP Archive",
}


def find_key_file() -> str:
    secrets_dir = Path(__file__).parent / "secrets"
    matches = list(secrets_dir.glob("*.json"))
    if not matches:
        raise FileNotFoundError(f"No JSON key file found in {secrets_dir}")
    if len(matches) > 1:
        print(f"Warning: multiple JSON files in secrets/, using {matches[0].name}")
    return str(matches[0])


def build_drive_service():
    key_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_KEY") or find_key_file()
    creds = service_account.Credentials.from_service_account_file(key_path, scopes=SCOPES)
    return build("drive", "v3", credentials=creds)


def list_all_files(service, drive_id: str) -> list[dict]:
    """Fetch every file and folder in the shared drive across all pages."""
    items = []
    page_token = None
    while True:
        resp = service.files().list(
            corpora="drive",
            driveId=drive_id,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            fields="nextPageToken, files(id, name, mimeType, parents)",
            pageSize=1000,
            pageToken=page_token,
        ).execute()
        items.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return items


def build_tree(items: list[dict], drive_id: str):
    id_to_item = {item["id"]: item for item in items}
    children: dict[str, list[str]] = defaultdict(list)
    for item in items:
        parents = item.get("parents", [])
        parent = parents[0] if parents else drive_id
        children[parent].append(item["id"])
    return id_to_item, children


def count_files_under(node_id: str, id_to_item: dict, children: dict) -> int:
    """Recursively count non-folder descendants."""
    total = 0
    for child_id in children.get(node_id, []):
        child = id_to_item.get(child_id)
        if child is None:
            continue
        if child["mimeType"] == "application/vnd.google-apps.folder":
            total += count_files_under(child_id, id_to_item, children)
        else:
            total += 1
    return total


def print_tree(node_id, id_to_item, children, label=None, indent=0, folder_counts=None):
    if label is None:
        item = id_to_item.get(node_id, {})
        label = item.get("name", node_id)

    file_count = count_files_under(node_id, id_to_item, children)
    subfolder_count = sum(
        1
        for cid in children.get(node_id, [])
        if id_to_item.get(cid, {}).get("mimeType") == "application/vnd.google-apps.folder"
    )

    prefix = "  " * indent
    line = f"{prefix}[D] {label}  ({file_count} file{'s' if file_count != 1 else ''})"
    if subfolder_count:
        line += f", {subfolder_count} subfolder{'s' if subfolder_count != 1 else ''}"
    print(line)

    if folder_counts is not None and indent > 0:
        folder_counts.append((label, file_count))

    sorted_children = sorted(
        children.get(node_id, []),
        key=lambda cid: id_to_item.get(cid, {}).get("name", "")
    )
    for child_id in sorted_children:
        child = id_to_item.get(child_id)
        if child and child["mimeType"] == "application/vnd.google-apps.folder":
            print_tree(child_id, id_to_item, children, indent=indent + 1, folder_counts=folder_counts)


def main():
    drive_id = os.getenv("SHARED_DRIVE_ID")
    if not drive_id:
        raise EnvironmentError("SHARED_DRIVE_ID is not set in .env")

    print("Authenticating with Google Drive API...")
    service = build_drive_service()

    print("Fetching all files (this may take a moment)...\n")
    items = list_all_files(service, drive_id)

    folders = [i for i in items if i["mimeType"] == "application/vnd.google-apps.folder"]
    files   = [i for i in items if i["mimeType"] != "application/vnd.google-apps.folder"]

    id_to_item, children = build_tree(items, drive_id)

    # Folder tree
    print("=" * 60)
    print("FOLDER STRUCTURE")
    print("=" * 60)
    folder_counts: list[tuple[str, int]] = []
    print_tree(drive_id, id_to_item, children, label="Shared Drive (root)", folder_counts=folder_counts)

    # Folders ranked by file count
    print("\n" + "=" * 60)
    print("FOLDERS BY FILE COUNT")
    print("=" * 60)
    for name, count in sorted(folder_counts, key=lambda x: -x[1]):
        print(f"  {name:<45} {count:>5} file{'s' if count != 1 else ''}")

    # File type breakdown
    type_counts: dict[str, int] = defaultdict(int)
    for f in files:
        type_counts[f["mimeType"]] += 1

    print("\n" + "=" * 60)
    print("FILE TYPES")
    print("=" * 60)
    for mime, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        label = MIME_LABELS.get(mime, mime)
        print(f"  {label:<45} {count:>5}")

    # Totals
    print("\n" + "=" * 60)
    print("TOTALS")
    print("=" * 60)
    print(f"  Total files:    {len(files):>5}")
    print(f"  Total folders:  {len(folders):>5}")
    print(f"  Distinct types: {len(type_counts):>5}")
    print("=" * 60)


if __name__ == "__main__":
    main()
