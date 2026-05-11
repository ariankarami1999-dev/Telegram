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

# ------------------------------------------------------------
#  Message parsing (same logic, but returns dict)
# ------------------------------------------------------------
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
            msg["timestamp"] = dt.timestamp()
        except:
            msg["date"] = raw
            msg["timestamp"] = 0
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


def render_messages_html(messages: List[Dict]) -> str:
    """Convert list of messages to HTML (Telegram‑like bubbles)"""
    lines = []
    for m in messages:
        bubble_parts = []

        # forward badge
        if m.get("forwarded_from"):
            bubble_parts.append(f'<div class="msg-forward">↪ فوروارد از {m["forwarded_from"]}</div>')

        # album
        if len(m.get("album", [])) > 1:
            album_html = '<div class="msg-album">'
            for idx, ph in enumerate(m["album"]):
                album_html += f'''
                <div class="album-item">
                    <img src="{ph}" loading="lazy" alt="photo {idx+1}">
                    <a href="{ph}" class="dl-badge" download>⬇</a>
                </div>
                '''
            album_html += '</div>'
            bubble_parts.append(album_html)
        elif m.get("photo"):
            bubble_parts.append(f'''
            <div class="msg-photo">
                <img src="{m["photo"]}" loading="lazy">
                <a href="{m["photo"]}" class="dl-overlay" download>📥 دانلود</a>
            </div>
            ''')

        # video
        if m.get("video"):
            bubble_parts.append(f'''
            <div class="msg-video">
                <video controls preload="metadata" poster="{m.get('photo', '')}">
                    <source src="{m['video']}">
                </video>
                <a href="{m['video']}" class="dl-btn" download>📥 دانلود ویدیو</a>
            </div>
            ''')

        # document
        if m.get("doc_title"):
            bubble_parts.append(f'''
            <div class="msg-doc">
                <div class="doc-icon">📄</div>
                <div class="doc-info">
                    <div class="doc-title">{m["doc_title"]}</div>
                    <div class="doc-extra">{m["doc_extra"]}</div>
                </div>
                <a href="#" class="doc-dl" download>⬇</a>
            </div>
            ''')

        # poll
        if m.get("poll_question"):
            opts = "".join(f'<li class="poll-opt">{opt}</li>' for opt in m["poll_options"])
            bubble_parts.append(f'''
            <div class="msg-poll">
                <div class="poll-question">📊 {m["poll_question"]}</div>
                <ul class="poll-opts">{opts}</ul>
            </div>
            ''')

        # text (with linkify)
        if m.get("text"):
            text = m["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            # simple URL detection
            text = re.sub(r'(https?://[^\s]+)', r'<a href="\1" target="_blank">\1</a>', text)
            bubble_parts.append(f'<div class="msg-text">{text}</div>')

        # footer (views + date)
        footer = []
        if m.get("views"):
            footer.append(f'<span class="msg-views">👁 {m["views"]}</span>')
        if m.get("date") and m.get("url"):
            footer.append(f'<a href="{m["url"]}" class="msg-date" target="_blank">{m["date"]}</a>')
        if footer:
            bubble_parts.append(f'<div class="msg-footer">{" · ".join(footer)}</div>')

        bubble_html = f'<div class="msg-wrap"><div class="msg-bubble">{"".join(bubble_parts)}</div></div>'
        lines.append(bubble_html)

    return "\n".join(lines)


def generate_html(channel: str, channel_info: Dict, messages: List[Dict], fetch_time: str) -> str:
    """Fill template.html with real data"""
    template_path = Path("scripts/template.html")
    if not template_path.exists():
        # fallback minimal template
        return f"<html><body><h1>@{channel}</h1><p>Template missing</p></body></html>"

    template = template_path.read_text(encoding="utf-8")

    avatar_html = ""
    if channel_info.get("avatar"):
        avatar_html = f'<img src="{channel_info["avatar"]}" class="ch-avatar" alt="avatar">'
    else:
        avatar_html = f'<div class="ch-avatar-placeholder">{channel_info["title"][0] if channel_info["title"] else "@"}</div>'

    desc_html = ""
    if channel_info.get("description"):
        desc_html = f'<div class="ch-desc">{channel_info["description"]}</div>'

    messages_html = render_messages_html(messages)

    html = template.replace("{{AVATAR_HTML}}", avatar_html) \
                   .replace("{{CHANNEL_TITLE}}", channel_info["title"] or f"@{channel}") \
                   .replace("{{CHANNEL_NAME}}", channel) \
                   .replace("{{CHANNEL_MEMBERS}}", channel_info.get("members", "?")) \
                   .replace("{{DESC_HTML}}", desc_html) \
                   .replace("{{MESSAGES}}", messages_html) \
                   .replace("{{MSG_COUNT}}", str(len(messages))) \
                   .replace("{{FETCH_TIME}}", fetch_time)

    return html


def update_channels_list(new_channel: str):
    """Append channel to channels.txt if not already there"""
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


def build_index_page():
    """Generate index.html listing all channels"""
    channels_dir = Path("channels")
    channels_dir.mkdir(exist_ok=True)
    list_file = Path("channels.txt")
    if not list_file.exists():
        return
    channels = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not channels:
        return

    index_items = []
    for ch in channels:
        html_path = channels_dir / f"{ch}.html"
        if html_path.exists():
            # extract title from the html itself quickly (simple regex)
            content = html_path.read_text(encoding="utf-8")
            title_match = re.search(r'<div class="ch-title">(.*?)</div>', content)
            title = title_match.group(1) if title_match else f"@{ch}"
            index_items.append(f'<li><a href="{ch}.html">{title}</a> <span>@{ch}</span></li>')
        else:
            index_items.append(f'<li>@{ch} (not yet fetched)</li>')
    index_html = f'''<!DOCTYPE html>
<html lang="fa" dir="auto">
<head><meta charset="UTF-8"><title>لیست کانال‌ها</title>
<style>body{{background:#0e1621;color:#e8edf2;font-family:Vazirmatn,sans-serif;padding:2rem;}}
a{{color:#64b5f6;}} ul{{list-style:none;padding:0;}} li{{margin:1rem 0;}}</style>
</head>
<body><h1>📡 لیست کانال‌های mirror</h1><ul>{"".join(index_items)}</ul></body></html>'''
    (channels_dir / "index.html").write_text(index_html, encoding="utf-8")
    print("[✓] Index page updated")


def main():
    # Determine channels to fetch
    channels_list = []
    manual_channel = os.getenv("INPUT_CHANNEL", "").strip()
    manual_count = os.getenv("INPUT_COUNT", "100").strip()

    if manual_channel:
        # manual run: only this channel, and update channels.txt
        channels_list = [manual_channel]
        update_channels_list(manual_channel)
        msg_limit = max(10, min(int(manual_count), 200))
    else:
        # scheduled run: read from channels.txt
        list_file = Path("channels.txt")
        if not list_file.exists():
            print("[!] No channels.txt found, nothing to do")
            sys.exit(0)
        channels_list = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not channels_list:
            print("[!] channels.txt is empty")
            sys.exit(0)
        msg_limit = 100   # default limit for scheduled updates

    fetch_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    for ch in channels_list:
        print("\n" + "="*50)
        try:
            messages, info = fetch_channel(ch, msg_limit)
            if not messages:
                print(f"[!] No messages for @{ch}, skipping")
                continue
            html_content = generate_html(ch, info, messages, fetch_time)
            out_file = Path(f"channels/{ch}.html")
            out_file.write_text(html_content, encoding="utf-8")
            print(f"[✓] Saved {out_file}")
        except Exception as e:
            print(f"[!] Failed to process @{ch}: {e}")

    build_index_page()
    print("\n[✅] All done.")


if __name__ == "__main__":
    main()
