#!/usr/bin/env python3
import argparse
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def parse_message(el) -> Dict[str, Any]:
    msg = {}
    msg_id = el.get("data-post", "")
    msg["id"] = msg_id

    date_el = el.select_one(".tgme_widget_message_date time")
    if date_el:
        raw = date_el.get("datetime", "")
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            msg["date"] = dt.strftime("%H:%M · %d %b %Y")
        except:
            msg["date"] = raw
    else:
        msg["date"] = ""

    views_el = el.select_one(".tgme_widget_message_views")
    msg["views"] = views_el.get_text(strip=True) if views_el else ""

    text_el = el.select_one(".tgme_widget_message_text")
    msg["text"] = text_el.get_text(separator="\n", strip=True) if text_el else ""

    photo_el = el.select_one(".tgme_widget_message_photo_wrap")
    msg["photo"] = ""
    if photo_el:
        style = photo_el.get("style", "")
        m = re.search(r"url\('(.+?)'\)", style)
        if m:
            msg["photo"] = m.group(1)

    album_photos = el.select(".tgme_widget_message_photo_wrap")
    msg["album"] = []
    for ph in album_photos:
        style = ph.get("style", "")
        m = re.search(r"url\('(.+?)'\)", style)
        if m:
            msg["album"].append(m.group(1))

    video_el = el.select_one("video")
    msg["video"] = video_el.get("src", "") if video_el else ""

    doc_el = el.select_one(".tgme_widget_message_document")
    if doc_el:
        title_el = doc_el.select_one(".tgme_widget_message_document_title")
        extra_el = doc_el.select_one(".tgme_widget_message_document_extra")
        msg["doc_title"] = title_el.get_text(strip=True) if title_el else ""
        msg["doc_extra"] = extra_el.get_text(strip=True) if extra_el else ""
    else:
        msg["doc_title"] = msg["doc_extra"] = ""

    fwd_el = el.select_one(".tgme_widget_message_forwarded_from")
    msg["forwarded_from"] = fwd_el.get_text(strip=True) if fwd_el else ""

    poll_el = el.select_one(".tgme_widget_message_poll")
    if poll_el:
        q = poll_el.select_one(".tgme_widget_message_poll_question")
        opts = poll_el.select(".tgme_widget_message_poll_option_text")
        msg["poll_question"] = q.get_text(strip=True) if q else ""
        msg["poll_options"] = [o.get_text(strip=True) for o in opts]
    else:
        msg["poll_question"] = ""
        msg["poll_options"] = []

    url_el = el.select_one(".tgme_widget_message_date")
    msg["url"] = url_el.get("href", "") if url_el else ""

    return msg

def fetch_channel(channel: str, limit: int):
    messages = []
    channel_info = {"name": channel, "title": "", "description": "", "avatar": "", "members": ""}
    base_url = f"https://t.me/s/{channel}"
    before = None

    print(f"[+] Fetching @{channel} (limit {limit})")

    while len(messages) < limit:
        url = base_url if before is None else f"{base_url}?before={before}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"[!] Error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")

        if before is None:
            try:
                title_el = soup.select_one(".tgme_channel_info_header_title")
                if title_el:
                    channel_info["title"] = title_el.get_text(strip=True)
                desc_el = soup.select_one(".tgme_channel_info_description")
                if desc_el:
                    channel_info["description"] = desc_el.get_text(strip=True)
                avatar_el = soup.select_one(".tgme_page_photo_image img, .tgme_channel_info_header_image img")
                if avatar_el:
                    channel_info["avatar"] = avatar_el.get("src", "")
                members_el = soup.select_one(".tgme_channel_info_counter .counter_value")
                if members_el:
                    channel_info["members"] = members_el.get_text(strip=True)
                print(f"    → {channel_info['title']} ({channel_info['members']} members)")
            except Exception as e:
                print(f"    [!] Could not parse channel info: {e}")

        bubbles = soup.select(".tgme_widget_message_wrap")
        if not bubbles:
            break

        page_msgs = []
        for b in bubbles:
            inner = b.select_one(".tgme_widget_message")
            if inner:
                page_msgs.append(parse_message(inner))

        if not page_msgs:
            break

        messages = page_msgs + messages
        ids = [int(m["id"].split("/")[-1]) for m in page_msgs if m["id"]]
        if not ids:
            break
        before = min(ids)

        if len(messages) >= limit:
            break

        time.sleep(0.8)

    messages = messages[-limit:]
    print(f"    ✓ fetched {len(messages)} messages")
    return messages, channel_info

def render_markdown(messages: List[Dict], channel_info: Dict, channel: str, fetch_time: str) -> str:
    """Generate GitHub-flavored Markdown that looks like a modern chat."""
    lines = []
    title = channel_info.get("title") or f"@{channel}"
    members = channel_info.get("members", "")
    desc = channel_info.get("description", "")
    avatar = channel_info.get("avatar", "")

    # Header
    if avatar:
        lines.append(f'<img src="{avatar}" width="70" style="border-radius:50%"/> <br/>\n')
    lines.append(f"# 📡 {title}\n")
    lines.append(f"**@{channel}**  ·  👥 {members} عضو  \n")
    if desc:
        lines.append(f"> {desc}  \n")
    lines.append(f"🕐 آخرین بروزرسانی: `{fetch_time}`  \n")
    lines.append(f"[![باز کردن در تلگرام](https://img.shields.io/badge/باز_کردن_در_تلگرام-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/{channel})  \n")
    lines.append("---\n")

    for m in messages:
        # Forwarded
        if m.get("forwarded_from"):
            lines.append(f"> ↪ **فوروارد از:** {m['forwarded_from']}  \n")

        # Album (multiple photos)
        if len(m.get("album", [])) > 1:
            for idx, ph in enumerate(m["album"]):
                lines.append(f"![photo {idx+1}]({ph})  \n")
        elif m.get("photo"):
            lines.append(f"![photo]({m['photo']})  \n")

        # Video link (since videos can't be embedded in GitHub MD)
        if m.get("video"):
            lines.append(f"🎬 **[دانلود ویدیو]({m['video']})**  \n")

        # Document
        if m.get("doc_title"):
            lines.append(f"📄 **{m['doc_title']}** `{m['doc_extra']}`  \n")

        # Poll
        if m.get("poll_question"):
            lines.append(f"📊 **{m['poll_question']}**  \n")
            for opt in m.get("poll_options", []):
                lines.append(f"- {opt}  \n")
            lines.append("\n")

        # Text (escape markdown characters)
        if m.get("text"):
            text = m["text"].replace("\\", "\\\\").replace("`", "\\`")
            lines.append(f"{text}  \n")

        # Footer (views + date link)
        footer_parts = []
        if m.get("views"):
            footer_parts.append(f"👁 {m['views']}")
        if m.get("date") and m.get("url"):
            footer_parts.append(f"[{m['date']}]({m['url']})")
        elif m.get("date"):
            footer_parts.append(m["date"])

        if footer_parts:
            lines.append(f"<sub>{' · '.join(footer_parts)}</sub>\n")

        lines.append("---\n")

    return "\n".join(lines)

def update_channels_list(new_channel: str):
    """Append channel to channels.txt if not already there."""
    list_file = Path("channels.txt")
    if not list_file.exists():
        list_file.write_text("")
    current = set(line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip())
    if new_channel not in current:
        with list_file.open("a", encoding="utf-8") as f:
            f.write(f"{new_channel}\n")
        print(f"[+] Added {new_channel} to channels list")
    else:
        print(f"[*] {new_channel} already in channels list")

def build_index_markdown():
    """Generate channels/README.md listing all channels."""
    channels_dir = Path("channels")
    channels_dir.mkdir(exist_ok=True)
    list_file = Path("channels.txt")
    if not list_file.exists():
        return
    channels = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not channels:
        return

    lines = ["# 📡 لیست کانال‌های آینه شده", "", "| کانال | آخرین بروزرسانی |", "|-------|----------------|"]
    for ch in channels:
        md_file = channels_dir / f"{ch}.md"
        if md_file.exists():
            # try to extract last update time from the file
            content = md_file.read_text(encoding="utf-8")
            match = re.search(r'🕐 آخرین بروزرسانی: `(.*?)`', content)
            last_update = match.group(1) if match else "نامشخص"
            lines.append(f"| [@{ch}](./{ch}.md) | {last_update} |")
        else:
            lines.append(f"| @{ch} | ❌ هنوز گرفته نشده |")
    lines.append("\n---\n✨ این لیست هر ۲ ساعت خودکار بروز می‌شود.")
    (channels_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("[✓] Index page (channels/README.md) updated")

def main():
    manual_channel = os.getenv("INPUT_CHANNEL", "").strip()
    manual_count = os.getenv("INPUT_COUNT", "100").strip()

    if manual_channel:
        channels_list = [manual_channel]
        update_channels_list(manual_channel)
        msg_limit = max(10, min(int(manual_count), 200))
    else:
        list_file = Path("channels.txt")
        if not list_file.exists():
            print("[!] No channels.txt found, nothing to do")
            sys.exit(0)
        channels_list = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not channels_list:
            print("[!] channels.txt is empty")
            sys.exit(0)
        msg_limit = 100   # default for scheduled runs

    fetch_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    for ch in channels_list:
        print("\n" + "="*50)
        try:
            messages, info = fetch_channel(ch, msg_limit)
            if not messages:
                print(f"[!] No messages for @{ch}, skipping")
                continue
            md_content = render_markdown(messages, info, ch, fetch_time)
            out_file = Path(f"channels/{ch}.md")
            out_file.write_text(md_content, encoding="utf-8")
            print(f"[✓] Saved {out_file}")
        except Exception as e:
            print(f"[!] Failed to process @{ch}: {e}")

    build_index_markdown()
    print("\n[✅] All done. Markdown files are ready to be viewed on GitHub.")

if __name__ == "__main__":
    main()
