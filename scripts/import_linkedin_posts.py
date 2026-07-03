#!/usr/bin/env python3
"""
Normalize manually collected LinkedIn posts into JSONL and Markdown.

This intentionally expects manual input instead of logging into LinkedIn or
scraping a member profile. LinkedIn member-post API access requires restricted
permissions, and logged-in scraping is brittle.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_INPUT = Path("research/linkedin-posts/gael-breton/manual-posts-template.md")
DEFAULT_JSONL = Path("research/linkedin-posts/gael-breton/posts.jsonl")
DEFAULT_MARKDOWN = Path("research/linkedin-posts/gael-breton/latest-posts.md")
DEFAULT_PROFILE = "https://www.linkedin.com/in/gael-breton/"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_manual_posts(raw: str) -> list[dict[str, str]]:
    posts: list[dict[str, str]] = []
    for block in re.split(r"(?m)^---\s*$", raw):
        block = block.strip()
        if not block or block.startswith("#") or block.startswith("<!--"):
            continue

        metadata: dict[str, str] = {}
        body_lines: list[str] = []
        in_text = False

        for line in block.splitlines():
            if in_text:
                body_lines.append(line)
                continue

            if line.lower().startswith("text:"):
                rest = line.split(":", 1)[1].strip()
                if rest:
                    body_lines.append(rest)
                in_text = True
                continue

            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip().lower()] = value.strip()

        text = "\n".join(body_lines).strip()
        url = metadata.get("url", "")
        if not text and not url:
            continue
        if not url and text.lower().startswith("paste "):
            continue

        posts.append(
            {
                "author": metadata.get("author", "Gael Breton"),
                "profile": metadata.get("profile", DEFAULT_PROFILE),
                "url": url,
                "date": metadata.get("date", ""),
                "engagement": metadata.get("engagement", ""),
                "collected_at": metadata.get("collected_at", utc_now()),
                "text": text,
                "notes": metadata.get("notes", ""),
            }
        )
    return posts


def write_jsonl(path: Path, posts: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for post in posts:
            handle.write(json.dumps(post, ensure_ascii=False) + "\n")


def write_markdown(path: Path, posts: list[dict[str, str]], profile: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Gael Breton - Latest LinkedIn Posts",
        "",
        f"- Profile: {profile}",
        f"- Generated: {utc_now()}",
        f"- Posts collected: {len(posts)}",
        "",
    ]

    for index, post in enumerate(posts, start=1):
        label_date = post["date"] or "date unknown"
        lines.extend(
            [
                f"## Post {index} - {label_date}",
                "",
                f"- URL: {post['url'] or 'not captured'}",
                f"- Engagement: {post['engagement'] or 'not captured'}",
                f"- Collected at: {post['collected_at']}",
                "",
                "### Text",
                "",
                post["text"] or "_No text captured._",
                "",
            ]
        )
        if post.get("notes"):
            lines.extend(["### Notes", "", post["notes"], ""])

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import manually collected LinkedIn posts.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--profile", default=DEFAULT_PROFILE)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"Input file not found: {args.input}")
        return 2

    posts = parse_manual_posts(args.input.read_text(encoding="utf-8"))
    write_jsonl(args.jsonl, posts)
    write_markdown(args.markdown, posts, args.profile)
    print(f"Imported {len(posts)} LinkedIn post(s).")
    print(f"JSONL: {args.jsonl}")
    print(f"Markdown: {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
