#!/usr/bin/env python3
"""
Fetch YouTube transcripts for research.

Default target:
  https://www.youtube.com/@AuthorityHackerPodcast

Two collection modes are supported:
  - supadata: uses SUPADATA_API_KEY and Supadata endpoints.
  - free: uses youtube-transcript-api for transcripts and YouTube RSS/page
    parsing for video discovery.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPADATA_BASE_URL = "https://api.supadata.ai/v1"
DEFAULT_CHANNEL = "@AuthorityHackerPodcast"
DEFAULT_CHANNEL_URL = "https://www.youtube.com/@AuthorityHackerPodcast"
DEFAULT_OUTPUT_DIR = Path("research/youtube-transcripts/gael_breton")


@dataclass
class VideoSeed:
    video_id: str
    title: str = ""
    upload_date: str = ""

    @property
    def url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.video_id}"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(value: str, fallback: str = "untitled") -> str:
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value.strip().lower())
    value = value.strip(".-_")
    return value[:90] or fallback


def read_video_ids(path: Path) -> list[str]:
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        ids.append(extract_video_id(line))
    return ids


def extract_video_id(value: str) -> str:
    value = value.strip()
    if re.fullmatch(r"[-_A-Za-z0-9]{11}", value):
        return value

    parsed = urllib.parse.urlparse(value)
    query = urllib.parse.parse_qs(parsed.query)
    if "v" in query and query["v"]:
        return query["v"][0]

    patterns = [
        r"youtu\.be/([-_A-Za-z0-9]{11})",
        r"/shorts/([-_A-Za-z0-9]{11})",
        r"/embed/([-_A-Za-z0-9]{11})",
        r"/live/([-_A-Za-z0-9]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return match.group(1)

    raise ValueError(f"Could not extract a YouTube video ID from: {value}")


def http_json(
    method: str,
    url: str,
    *,
    api_key: str | None = None,
    body: dict[str, Any] | None = None,
    timeout: int = 90,
) -> tuple[int, dict[str, Any], dict[str, str]]:
    data = None
    headers = {"Accept": "application/json"}
    if api_key:
        headers["x-api-key"] = api_key
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            payload = json.loads(raw) if raw else {}
            return response.status, payload, dict(response.headers)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            payload = {"error": raw}
        message = payload.get("message") or payload.get("error") or raw
        raise RuntimeError(f"HTTP {exc.code} for {url}: {message}") from exc


def build_url(path: str, params: dict[str, Any] | None = None) -> str:
    url = SUPADATA_BASE_URL + path
    if params:
        clean = {key: value for key, value in params.items() if value is not None}
        url += "?" + urllib.parse.urlencode(clean)
    return url


def supadata_channel_videos(
    api_key: str,
    channel: str,
    limit: int,
    video_type: str,
) -> list[VideoSeed]:
    url = build_url(
        "/youtube/channel/videos",
        {"id": channel, "limit": limit, "type": video_type},
    )
    _, payload, _ = http_json("GET", url, api_key=api_key)

    ordered_ids: list[str] = []
    if video_type in ("all", "video"):
        ordered_ids.extend(payload.get("videoIds", []))
    if video_type in ("all", "short"):
        ordered_ids.extend(payload.get("shortIds", []))
    if video_type in ("all", "live"):
        ordered_ids.extend(payload.get("liveIds", []))

    deduped = list(dict.fromkeys(ordered_ids))[:limit]
    return [VideoSeed(video_id=video_id) for video_id in deduped]


def poll_supadata_transcript_job(
    api_key: str,
    job_id: str,
    *,
    timeout_seconds: int,
    poll_seconds: float,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        url = build_url(f"/transcript/{urllib.parse.quote(job_id)}")
        _, payload, _ = http_json("GET", url, api_key=api_key, timeout=60)
        status = payload.get("status")
        if status == "completed":
            if "result" in payload and isinstance(payload["result"], dict):
                return payload["result"]
            return payload
        if status == "failed":
            raise RuntimeError(f"Supadata transcript job failed: {payload}")
        time.sleep(poll_seconds)
    raise TimeoutError(f"Timed out waiting for Supadata transcript job {job_id}")


def fetch_supadata_transcript(
    api_key: str,
    seed: VideoSeed,
    *,
    lang: str,
    mode: str,
    text: bool,
    timeout_seconds: int,
) -> dict[str, Any]:
    url = build_url(
        "/transcript",
        {
            "url": seed.url,
            "lang": lang,
            "text": str(text).lower(),
            "mode": mode,
        },
    )
    status, payload, headers = http_json("GET", url, api_key=api_key, timeout=timeout_seconds)
    if status == 202 or payload.get("jobId"):
        payload = poll_supadata_transcript_job(
            api_key,
            payload["jobId"],
            timeout_seconds=timeout_seconds,
            poll_seconds=1,
        )
    payload["_http_status"] = status
    payload["_billable_requests"] = headers.get("x-billable-requests")
    return payload


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
        raw = fetch_text(oembed_url, timeout=20)
        payload = json.loads(raw)
        metadata["title"] = html.unescape(str(payload.get("title", ""))).strip()
    except Exception:
        pass

    try:
        page = fetch_text(f"https://www.youtube.com/watch?v={video_id}", timeout=30)
        match = re.search(
            r'"(?:uploadDate|publishDate)":"([^"]+)"',
            page,
        )
        if match:
            metadata["upload_date"] = html.unescape(match.group(1)).strip()
    except Exception:
        pass

    return metadata


def enrich_video_seeds(seeds: list[VideoSeed]) -> None:
    for seed in seeds:
        if seed.title and seed.upload_date:
            continue
        metadata = fetch_youtube_video_metadata(seed.video_id)
        seed.title = seed.title or metadata["title"]
        seed.upload_date = seed.upload_date or metadata["upload_date"]


def resolve_youtube_channel_id(channel_url: str) -> str:
    html = fetch_text(channel_url)
    patterns = [
        r'"channelId":"(UC[-_A-Za-z0-9]+)"',
        r'"externalId":"(UC[-_A-Za-z0-9]+)"',
        r'<meta itemprop="channelId" content="(UC[-_A-Za-z0-9]+)"',
        r'"browseId":"(UC[-_A-Za-z0-9]+)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, html)
        if match:
            return match.group(1)
    raise RuntimeError(
        "Could not resolve a channel ID from the channel URL. "
        "Pass --channel-id with a UC... channel ID or use --source supadata."
    )


def rss_channel_videos(channel_id: str, limit: int) -> list[VideoSeed]:
    rss_url = "https://www.youtube.com/feeds/videos.xml?" + urllib.parse.urlencode(
        {"channel_id": channel_id}
    )
    xml_text = fetch_text(rss_url)
    root = ET.fromstring(xml_text)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
    }
    seeds: list[VideoSeed] = []
    for entry in root.findall("atom:entry", ns)[:limit]:
        video_id = entry.findtext("yt:videoId", default="", namespaces=ns).strip()
        title = entry.findtext("atom:title", default="", namespaces=ns).strip()
        upload_date = entry.findtext("atom:published", default="", namespaces=ns).strip()
        if video_id:
            seeds.append(VideoSeed(video_id=video_id, title=title, upload_date=upload_date))
    return seeds


def extract_json_object_after_marker(text: str, marker: str) -> dict[str, Any]:
    marker_index = text.find(marker)
    if marker_index == -1:
        raise ValueError(f"Marker not found: {marker}")

    start = text.find("{", marker_index)
    if start == -1:
        raise ValueError(f"JSON object not found after marker: {marker}")

    depth = 0
    in_string = False
    escape = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : index + 1])

    raise ValueError(f"JSON object did not close after marker: {marker}")


def add_query_param(url: str, key: str, value: str) -> str:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    query[key] = [value]
    return urllib.parse.urlunparse(
        parsed._replace(query=urllib.parse.urlencode(query, doseq=True))
    )


def choose_caption_track(caption_tracks: list[dict[str, Any]], lang: str) -> dict[str, Any]:
    if not caption_tracks:
        raise RuntimeError("No caption tracks are available for this video.")

    normalized = lang.lower()
    for track in caption_tracks:
        language_code = str(track.get("languageCode", "")).lower()
        if language_code == normalized:
            return track
    for track in caption_tracks:
        language_code = str(track.get("languageCode", "")).lower()
        if language_code.startswith(normalized):
            return track
    for track in caption_tracks:
        language_code = str(track.get("languageCode", "")).lower()
        if language_code.startswith(normalized.split("-")[0]):
            return track
    return caption_tracks[0]


def fetch_timedtext_transcript(seed: VideoSeed, *, lang: str) -> dict[str, Any]:
    page = fetch_text(seed.url, timeout=45)
    player_response = extract_json_object_after_marker(page, "ytInitialPlayerResponse")
    tracklist = (
        player_response.get("captions", {})
        .get("playerCaptionsTracklistRenderer", {})
        .get("captionTracks", [])
    )
    track = choose_caption_track(tracklist, lang)
    base_url = track.get("baseUrl")
    if not base_url:
        raise RuntimeError("Caption track did not include a baseUrl.")

    transcript_url = add_query_param(html.unescape(base_url), "fmt", "json3")
    transcript_json = json.loads(fetch_text(transcript_url, timeout=45))
    content: list[dict[str, Any]] = []
    for event in transcript_json.get("events", []):
        segs = event.get("segs") or []
        text_value = "".join(str(seg.get("utf8", "")) for seg in segs).strip()
        if not text_value:
            continue
        content.append(
            {
                "text": html.unescape(text_value),
                "offset": int(event.get("tStartMs", 0)),
                "duration": int(event.get("dDurationMs", 0)),
                "lang": track.get("languageCode", lang),
            }
        )

    if not content:
        raise RuntimeError("Caption track was found, but no transcript text was returned.")

    return {
        "content": content,
        "lang": track.get("languageCode", lang),
        "availableLangs": [
            str(item.get("languageCode", "")) for item in tracklist if item.get("languageCode")
        ],
    }


def fetch_free_transcript(seed: VideoSeed, *, lang: str) -> dict[str, Any]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return fetch_timedtext_transcript(seed, lang=lang)

    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(seed.video_id, languages=[lang])
        snippets = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
        return {
            "content": [
                {
                    "text": item.get("text", ""),
                    "offset": int(float(item.get("start", 0)) * 1000),
                    "duration": int(float(item.get("duration", 0)) * 1000),
                    "lang": getattr(fetched, "language_code", lang),
                }
                for item in snippets
            ],
            "lang": getattr(fetched, "language_code", lang),
            "availableLangs": [getattr(fetched, "language_code", lang)],
        }
    except AttributeError:
        raw = YouTubeTranscriptApi.get_transcript(seed.video_id, languages=[lang])
        return {
            "content": [
                {
                    "text": item.get("text", ""),
                    "offset": int(float(item.get("start", 0)) * 1000),
                    "duration": int(float(item.get("duration", 0)) * 1000),
                    "lang": lang,
                }
                for item in raw
            ],
            "lang": lang,
            "availableLangs": [lang],
        }
    except Exception:
        return fetch_timedtext_transcript(seed, lang=lang)


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


def write_outputs(
    output_dir: Path,
    seed: VideoSeed,
    payload: dict[str, Any],
    *,
    source: str,
    status: str,
    error: str = "",
) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    title_slug = slugify(seed.title, fallback=seed.video_id)
    video_dir = output_dir / f"{seed.video_id}-{title_slug}"
    video_dir.mkdir(parents=True, exist_ok=True)
    json_path = video_dir / "transcript.json"
    md_path = video_dir / "transcript.md"

    record = {
        "video_id": seed.video_id,
        "url": seed.url,
        "title": seed.title,
        "upload_date": seed.upload_date,
        "source": source,
        "status": status,
        "error": error,
        "fetched_at": utc_now(),
        "transcript": payload,
    }
    json_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# {seed.title or seed.video_id}",
        "",
        f"- YouTube: {seed.url}",
        f"- Video ID: {seed.video_id}",
        f"- Upload date: {seed.upload_date or 'unknown'}",
        f"- Transcript source: {source}",
        f"- Status: {status}",
        f"- Language: {payload.get('lang', 'unknown')}",
        f"- Fetched at: {record['fetched_at']}",
    ]
    billable = payload.get("_billable_requests")
    if billable:
        lines.append(f"- Supadata billable requests: {billable}")
    if error:
        lines.extend(["", f"Error: {error}"])
    lines.extend(["", "## Transcript", ""])

    content = payload.get("content")
    if isinstance(content, list):
        for item in content:
            timestamp = format_timestamp(item.get("offset"))
            text_value = str(item.get("text", "")).strip()
            if text_value:
                lines.append(f"[{timestamp}] {text_value}")
    else:
        lines.append(transcript_to_text(content))

    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {"json_path": str(json_path), "markdown_path": str(md_path)}


def write_index(output_dir: Path, rows: list[dict[str, str]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / "index.csv"
    fieldnames = [
        "video_id",
        "title",
        "url",
        "upload_date",
        "source",
        "status",
        "lang",
        "json_path",
        "markdown_path",
        "error",
    ]
    with index_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_video_seeds(args: argparse.Namespace, api_key: str | None) -> list[VideoSeed]:
    ids: list[str] = []
    for value in args.video_id:
        ids.append(extract_video_id(value))
    if args.video_ids_file:
        ids.extend(read_video_ids(args.video_ids_file))
    if ids:
        return [VideoSeed(video_id=video_id) for video_id in list(dict.fromkeys(ids))[: args.limit]]

    if args.source == "supadata":
        if not api_key:
            raise RuntimeError("Set SUPADATA_API_KEY or pass --api-key for Supadata mode.")
        return supadata_channel_videos(api_key, args.channel, args.limit, args.video_type)

    channel_id = args.channel_id or resolve_youtube_channel_id(args.channel_url)
    return rss_channel_videos(channel_id, args.limit)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts for research.")
    parser.add_argument("--source", choices=["supadata", "free"], default="supadata")
    parser.add_argument("--api-key", default=os.getenv("SUPADATA_API_KEY"))
    parser.add_argument("--channel", default=DEFAULT_CHANNEL, help="Supadata channel handle, URL, or ID.")
    parser.add_argument("--channel-url", default=DEFAULT_CHANNEL_URL, help="Free mode channel URL.")
    parser.add_argument("--channel-id", help="Free mode UC... channel ID for YouTube RSS.")
    parser.add_argument("--video-id", action="append", default=[], help="Video ID or URL. Repeatable.")
    parser.add_argument("--video-ids-file", type=Path, help="Text file with one video ID or URL per line.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--lang", default="en")
    parser.add_argument("--mode", choices=["native", "auto", "generate"], default="native")
    parser.add_argument("--video-type", choices=["video", "short", "live", "all"], default="video")
    parser.add_argument("--plain-text", action="store_true", help="Ask Supadata for plain text content.")
    parser.add_argument(
        "--no-enrich-metadata",
        action="store_true",
        help="Skip public YouTube title/date metadata enrichment.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--timeout-seconds", type=int, default=180)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    rows: list[dict[str, str]] = []

    if args.source == "supadata" and not args.api_key:
        print("Set SUPADATA_API_KEY or pass --api-key for Supadata mode.", file=sys.stderr)
        return 2

    try:
        seeds = build_video_seeds(args, args.api_key)
    except Exception as exc:
        print(f"Could not build video list: {exc}", file=sys.stderr)
        return 2

    if not seeds:
        print("No videos found.", file=sys.stderr)
        return 1

    if not args.no_enrich_metadata:
        enrich_video_seeds(seeds)

    print(f"Found {len(seeds)} video(s). Writing to {args.output_dir}")

    for index, seed in enumerate(seeds, start=1):
        print(f"[{index}/{len(seeds)}] {seed.video_id} {seed.title}".strip())
        status = "ok"
        error = ""
        payload: dict[str, Any]
        try:
            if args.source == "supadata":
                payload = fetch_supadata_transcript(
                    args.api_key,
                    seed,
                    lang=args.lang,
                    mode=args.mode,
                    text=args.plain_text,
                    timeout_seconds=args.timeout_seconds,
                )
            else:
                payload = fetch_free_transcript(seed, lang=args.lang)
        except Exception as exc:
            status = "error"
            error = str(exc)
            payload = {"content": "", "lang": args.lang, "availableLangs": []}

        paths = write_outputs(
            args.output_dir,
            seed,
            payload,
            source=args.source,
            status=status,
            error=error,
        )
        rows.append(
            {
                "video_id": seed.video_id,
                "title": seed.title,
                "url": seed.url,
                "upload_date": seed.upload_date,
                "source": args.source,
                "status": status,
                "lang": str(payload.get("lang", "")),
                "json_path": paths["json_path"],
                "markdown_path": paths["markdown_path"],
                "error": error,
            }
        )

    write_index(args.output_dir, rows)
    print(f"Done. Index: {args.output_dir / 'index.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
