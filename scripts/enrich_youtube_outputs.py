#!/usr/bin/env python3
"""
Enrich existing YouTube transcript outputs with public YouTube metadata.

This updates generated JSON, Markdown, and index.csv files without refetching
transcripts or using Supadata credits.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_DIR = Path("research/youtube-transcripts/gael_breton")


def fetch_text(url: str, *, timeout: int = 45) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
        )
    }
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_youtube_video_metadata(video_id: str) -> dict[str, str]:
    metadata = {"title": "", "upload_date": ""}
    oembed_url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": f"https://www.youtube.com/watch?v={video_id}", "format": "json"}
    )

    try:
        payload = json.loads(fetch_text(oembed_url, timeout=20))
        metadata["title"] = html.unescape(str(payload.get("title", ""))).strip()
    except Exception:
        pass

    try:
        page = fetch_text(f"https://www.youtube.com/watch?v={video_id}", timeout=30)
        match = re.search(r'"(?:uploadDate|publishDate)":"([^"]+)"', page)
        if match:
            metadata["upload_date"] = html.unescape(match.group(1)).strip()
    except Exception:
        pass

    return metadata


def transcript_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        return "\n".join(item.get("text", "").strip() for item in content if item.get("text"))
    return ""


def format_timestamp(offset_ms: int | float | None) -> str:
    total_seconds = int((offset_ms or 0) / 1000)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def render_markdown(record: dict[str, Any]) -> str:
    transcript = record.get("transcript", {})
    lines = [
        f"# {record.get('title') or record.get('video_id')}",
        "",
        f"- YouTube: {record.get('url')}",
        f"- Video ID: {record.get('video_id')}",
        f"- Upload date: {record.get('upload_date') or 'unknown'}",
        f"- Transcript source: {record.get('source')}",
        f"- Status: {record.get('status')}",
        f"- Language: {transcript.get('lang', 'unknown')}",
        f"- Fetched at: {record.get('fetched_at')}",
    ]
    billable = transcript.get("_billable_requests")
    if billable:
        lines.append(f"- Supadata billable requests: {billable}")
    if record.get("error"):
        lines.extend(["", f"Error: {record['error']}"])
    lines.extend(["", "## Transcript", ""])

    content = transcript.get("content")
    if isinstance(content, list):
        for item in content:
            timestamp = format_timestamp(item.get("offset"))
            text_value = str(item.get("text", "")).strip()
            if text_value:
                lines.append(f"[{timestamp}] {text_value}")
    else:
        lines.append(transcript_to_text(content))

    return "\n".join(lines).rstrip() + "\n"


def enrich_output_dir(output_dir: Path) -> list[dict[str, str]]:
    index_path = output_dir / "index.csv"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing index: {index_path}")

    rows = list(csv.DictReader(index_path.open(encoding="utf-8-sig")))
    metadata_cache: dict[str, dict[str, str]] = {}

    for row in rows:
        video_id = row["video_id"]
        metadata = metadata_cache.setdefault(video_id, fetch_youtube_video_metadata(video_id))
        title = row.get("title") or metadata["title"]
        upload_date = row.get("upload_date") or metadata["upload_date"]

        row["title"] = title
        row["upload_date"] = upload_date

        json_path = Path(row["json_path"])
        markdown_path = Path(row["markdown_path"])
        if json_path.exists():
            record = json.loads(json_path.read_text(encoding="utf-8"))
            record["title"] = title
            record["upload_date"] = upload_date
            json_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
            if markdown_path.exists():
                markdown_path.write_text(render_markdown(record), encoding="utf-8")

    with index_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Enrich existing YouTube transcript outputs.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    rows = enrich_output_dir(args.output_dir)
    enriched = sum(1 for row in rows if row.get("title") or row.get("upload_date"))
    print(f"Enriched {enriched} row(s).")
    print(f"Index: {args.output_dir / 'index.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
