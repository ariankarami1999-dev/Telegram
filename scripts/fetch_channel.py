#!/usr/bin/env python3
import os
import re
import sys
import time
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def parse_message(el) -> Dict[str, Any]:
    msg = {}
    msg_id = el.get("data-post", "")
    msg["id"] = msg_id   # format: "channel/12345"
    # extract numeric id
    msg["id_num"] = int(msg_id.split("/")[-1]) if msg_id else 0

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

def fetch_channel(channel: str, limit: int, after_id: Optional[int] = None):
    """
    Fetch messages from a Telegram channel.
    If after_id is given, fetch only messages newer than that ID (incremental update).
    Otherwise fetch up to 'limit' most recent messages.
    """
    messages = []
    channel_info = {"name": channel, "title": "", "description": "", "avatar": "", "members": ""}
    base_url = f"https://t.me/s/{channel}"
    before = None

    print(f"[+] Fetching @{channel} (limit={limit}, after_id={after_id})")

    # For incremental update: we collect messages until we hit the after_id
    # We'll fetch pages until we have no more new messages or reach limit
    fetched_new = 0
    stop = False

    while not stop and fetched_new < limit:
        url = base_url if before is None else f"{base_url}?before={before}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"[!] Error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")

        if before is None:
            # Parse channel info only once
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
                msg = parse_message(inner)
                # If we have after_id and this message's id_num <= after_id, stop
                if after_id is not None and msg["id_num"] <= after_id:
                    stop = True
                    break
                page_msgs.append(msg)

        if not page_msgs:
            break

        # New messages come in chronological order from oldest to newest on each page?
        # Actually Telegram's 'before' pagination gives older messages first.
        # To get newest first, we need to reverse.
        # But we'll collect and later sort.
        page_msgs.reverse()  # now newest first
        messages = page_msgs + messages
        fetched_new += len(page_msgs)

        # Get the oldest message ID on this page to use as 'before' for next page
        ids = [m["id_num"] for m in page_msgs if m["id_num"]]
        if not ids:
            break
        before = min(ids) - 1  # go older

        time.sleep(0.8)

    # Limit to requested count (for initial fetch) or keep all new ones
    if after_id is None:
        messages = messages[-limit:]
    else:
        # For incremental, we already stopped when we hit old messages
        # Ensure we don't exceed limit (but limit is small like 20)
        messages = messages[:limit]

    print(f"    ✓ fetched {len(messages)} new messages")
    return messages, channel_info

def get_latest_message_id_from_md(md_file: Path) -> Optional[int]:
    """Extract the highest message ID from existing Markdown file."""
    if not md_file.exists():
        return None
    content = md_file.read_text(encoding="utf-8")
    # Look for <!-- msg_id: 12345 --> comments
    matches = re.findall(r'<!-- msg_id: (\d+) -->', content)
    if matches:
        return max(int(x) for x in matches)
    return None

def render_markdown(messages: List[Dict], channel_info: Dict, channel: str, fetch_time: str) -> str:
    """Generate GitHub Markdown with theme toggle and hidden IDs."""
    title = channel_info.get("title") or f"@{channel}"
    members = channel_info.get("members", "")
    desc = channel_info.get("description", "")
    avatar = channel_info.get("avatar", "")

    # CSS for dark/light (works on GitHub)
    theme_style = """
<style>
  .tg-mirror {
    --bg: #0d1117;
    --text: #c9d1d9;
    --border: #30363d;
    --accent: #58a6ff;
  }
  @media (prefers-color-scheme: light) {
    .tg-mirror {
      --bg: #ffffff;
      --text: #24292f;
      --border: #d0d7de;
      --accent: #0969da;
    }
  }
  .tg-mirror {
    background: var(--bg);
    color: var(--text);
    padding: 16px;
    border-radius: 16px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Vazirmatn', sans-serif;
  }
  .tg-header {
    text-align: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 16px;
    margin-bottom: 16px;
  }
  .tg-avatar {
    border-radius: 50%;
    width: 64px;
    border: 2px solid var(--accent);
  }
  .tg-message {
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px;
    margin: 12px 0;
    background: var(--bg);
  }
  .tg-footer {
    font-size: 0.8em;
    color: #8b949e;
    margin-top: 8px;
  }
  img {
    max-width: 100%;
    border-radius: 8px;
  }
</style>
<div class="tg-mirror">
<div class="tg-header">
"""
    if avatar:
        theme_style += f'<img src="{avatar}" class="tg-avatar"/><br/>'
    theme_style += f"""
<h1>📡 {title}</h1>
<p><strong>@{channel}</strong> · 👥 {members} عضو</p>
<p><em>{desc}</em></p>
<p>🕐 آخرین بروزرسانی: <code>{fetch_time}</code></p>
<p><a href="https://t.me/{channel}" target="_blank"><img src="https://img.shields.io/badge/باز_کردن_در_تلگرام-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/></a></p>
</div>
<hr/>
"""

    for m in messages:
        theme_style += '<div class="tg-message">'
        # Hidden ID for incremental update
        theme_style += f'<!-- msg_id: {m["id_num"]} -->'
        if m.get("forwarded_from"):
            theme_style += f'<blockquote>↪ فوروارد از: <strong>{m["forwarded_from"]}</strong></blockquote>'
        if len(m.get("album", [])) > 1:
            for idx, ph in enumerate(m["album"]):
                theme_style += f'<p><img src="{ph}" alt="photo {idx+1}"/></p>'
        elif m.get("photo"):
            theme_style += f'<p><img src="{m["photo"]}" alt="photo"/></p>'
        if m.get("video"):
            theme_style += f'<p>🎬 <a href="{m["video"]}" target="_blank">دانلود ویدیو</a></p>'
        if m.get("doc_title"):
            theme_style += f'<p>📄 <strong>{m["doc_title"]}</strong> <code>{m["doc_extra"]}</code></p>'
        if m.get("poll_question"):
            theme_style += f'<p>📊 <strong>{m["poll_question"]}</strong><br/><ul>'
            for opt in m["poll_options"]:
                theme_style += f'<li>{opt}</li>'
            theme_style += '</ul></p>'
        if m.get("text"):
            text = m["text"].replace("\\", "\\\\").replace("`", "\\`")
            theme_style += f'<p>{text}</p>'
        footer_parts = []
        if m.get("views"):
            footer_parts.append(f'👁 {m["views"]}')
        if m.get("date") and m.get("url"):
            footer_parts.append(f'<a href="{m["url"]}" target="_blank">{m["date"]}</a>')
        elif m.get("date"):
            footer_parts.append(m["date"])
        if footer_parts:
            theme_style += f'<div class="tg-footer">{" · ".join(footer_parts)}</div>'
        theme_style += '</div>'

    theme_style += '</div>'
    return theme_style

def update_channels_list(new_channel: str):
    list_file = Path("channels.txt")
    if not list_file.exists():
        list_file.write_text("")
    current = set(line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip())
    if new_channel not in current:
        with list_file.open("a", encoding="utf-8") as f:
            f.write(f"{new_channel}\n")
        print(f"[+] Added {new_channel} to channels list")

def build_index_markdown():
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
            content = md_file.read_text(encoding="utf-8")
            match = re.search(r'🕐 آخرین بروزرسانی: `(.*?)`', content)
            last_update = match.group(1) if match else "نامشخص"
            lines.append(f"| [@{ch}](./{ch}.md) | {last_update} |")
        else:
            lines.append(f"| @{ch} | ❌ هنوز گرفته نشده |")
    lines.append("\n---\n✨ این لیست هر ۲ ساعت خودکار بروز می‌شود. برای بروزرسانی دستی همه کانال‌ها، فیلد channel را خالی بگذارید.")
    (channels_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("[✓] Index page (channels/README.md) updated")

def main():
    manual_channel = os.getenv("INPUT_CHANNEL", "").strip()
    manual_count = os.getenv("INPUT_COUNT", "100").strip()

    # Determine list of channels to process
    if manual_channel:
        channels_list = [manual_channel]
        update_channels_list(manual_channel)
        # For manually added channel, fetch up to 100 messages initially
        limit = max(10, min(int(manual_count), 200))
        incremental = False
    else:
        # Scheduled run or bulk update (channel field empty)
        list_file = Path("channels.txt")
        if not list_file.exists():
            print("[!] No channels.txt found")
            sys.exit(0)
        channels_list = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not channels_list:
            print("[!] channels.txt is empty")
            sys.exit(0)
        # For bulk updates, only fetch 20 newest messages per channel
        limit = 20
        incremental = True

    fetch_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    for ch in channels_list:
        print("\n" + "="*50)
        try:
            md_file = Path(f"channels/{ch}.md")
            after_id = None
            if incremental and md_file.exists():
                after_id = get_latest_message_id_from_md(md_file)
                print(f"[*] Existing channel, last ID: {after_id}")
            else:
                print(f"[*] New channel or full fetch requested")

            messages, info = fetch_channel(ch, limit, after_id=after_id)
            if not messages:
                print(f"[!] No new messages for @{ch}")
                # Still update the file to refresh timestamp? Optional: keep old content.
                continue

            # Merge with existing content if incremental?
            # For simplicity, we regenerate entire file with new messages + old ones?
            # But incremental should only add new messages. However since we only keep last 20, we can just replace.
            # But if user wants to keep history, that's different. Based on request, they only want latest 20.
            # So we just overwrite with the new messages (which are the most recent up to limit=20).
            # But what if there are more than 20 new messages? We limit to 20.
            # Good.
            md_content = render_markdown(messages, info, ch, fetch_time)
            md_file.write_text(md_content, encoding="utf-8")
            print(f"[✓] Saved {md_file} with {len(messages)} messages")
        except Exception as e:
            print(f"[!] Failed to process @{ch}: {e}")

    build_index_markdown()
    print("\n[✅] All done.")

if __name__ == "__main__":
    main()
