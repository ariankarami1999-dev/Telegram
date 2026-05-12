#!/usr/bin/env python3
import os
import re
import sys
import time
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional

import requests
import jdatetime
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

TEHRAN_OFFSET = timedelta(hours=3, minutes=30)
DEFAULT_LIMIT = 100

def utc_to_tehran(dt_utc: datetime) -> datetime:
    return dt_utc + TEHRAN_OFFSET

def to_jalali_str(dt_utc: datetime) -> str:
    dt_tehran = utc_to_tehran(dt_utc)
    jd = jdatetime.datetime.fromgregorian(datetime=dt_tehran)
    return jd.strftime("%H:%M · %d %B %Y")

def parse_message(el) -> Dict[str, Any]:
    msg = {}
    msg_id = el.get("data-post", "")
    msg["id"] = msg_id
    msg["id_num"] = int(msg_id.split("/")[-1]) if msg_id else 0

    date_el = el.select_one(".tgme_widget_message_date time")
    if date_el:
        raw = date_el.get("datetime", "")
        try:
            dt_utc = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            msg["date"] = to_jalali_str(dt_utc)
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

def fetch_channel_full(channel: str, limit: int) -> tuple[List[Dict], Dict]:
    messages = []
    channel_info = {"name": channel, "title": "", "description": "", "avatar": "", "members": ""}
    base_url = f"https://t.me/s/{channel}"
    before = None

    print(f"[+] Fetching @{channel} (full fetch, limit={limit})")

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
            print("    [!] No messages found on page")
            break

        page_msgs = []
        for b in bubbles:
            inner = b.select_one(".tgme_widget_message")
            if inner:
                page_msgs.append(parse_message(inner))

        if not page_msgs:
            break

        page_msgs.reverse()
        messages.extend(page_msgs)

        ids = [m["id_num"] for m in page_msgs if m["id_num"]]
        if not ids:
            break
        before = min(ids)
        print(f"    → Next before: {before}")

        time.sleep(0.8)

    if len(messages) > limit:
        messages = messages[:limit]
    print(f"    ✓ fetched {len(messages)} messages")
    return messages, channel_info

def render_markdown(messages: List[Dict], channel_info: Dict, channel: str, fetch_time_str: str) -> str:
    """
    تولید مارک‌داون خواناتر با استایل بهتر اما بدون خروج از فرمت .md
    """
    title = channel_info.get("title") or f"@{channel}"
    members = channel_info.get("members", "")
    desc = channel_info.get("description", "")
    avatar = channel_info.get("avatar", "")

    # هدر با استایل CSS یکپارچه (درون خود مارک‌داون)
    output = f'''<div dir="rtl" align="right">

<style>
.tg-channel-box {{
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {{
  .tg-channel-box {{
    background: #1a1a2e;
    color: #eee;
  }}
  .tg-post {{
    background: #16213e;
    border-color: #0f3460;
  }}
  .tg-post-header {{
    background: #0f3460;
  }}
  .tg-footer {{
    color: #aaa;
  }}
  .tg-text a {{
    color: #7eb6ff;
  }}
}}

/* کارت پست */
.tg-post {{
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}}
.tg-post:hover {{
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}}
.tg-post-header {{
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}}

/* نقل قول / فوروارد */
.tg-forward {{
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}}

/* متن */
.tg-text {{
  font-size: 16px;
  margin: 14px 0;
}}
.tg-text a {{
  color: #2563eb;
  text-decoration: none;
}}
.tg-text a:hover {{
  text-decoration: underline;
}}

/* تصاویر */
.tg-photo {{
  margin: 12px 0;
  text-align: center;
}}
.tg-photo img {{
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}}

/* آلبوم */
.tg-album {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}}
.tg-album-item {{
  overflow: hidden;
  border-radius: 12px;
}}
.tg-album-item img {{
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}}
.tg-album-item img:hover {{
  transform: scale(1.02);
}}

/* ویدیو */
.tg-video {{
  margin: 12px 0;
}}
.tg-video video {{
  width: 100%;
  border-radius: 16px;
  background: black;
}}
.tg-dl-btn {{
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}}
.tg-dl-btn:hover {{
  background: #2563eb;
}}

/* فایل */
.tg-doc {{
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}}
.tg-doc-icon {{
  font-size: 32px;
}}
.tg-doc-info {{
  flex: 1;
}}
.tg-doc-title {{
  font-weight: 600;
}}
.tg-doc-extra {{
  font-size: 12px;
  color: #6b7280;
}}
.tg-doc-link {{
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}}

/* نظرسنجی */
.tg-poll {{
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}}
.tg-poll h4 {{
  margin: 0 0 10px 0;
  color: #854d0e;
}}
.tg-poll ul {{
  margin: 0;
  padding-right: 20px;
}}
.tg-poll li {{
  margin: 6px 0;
  color: #a16207;
}}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {{
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}}
.tg-footer a {{
  color: #6b7280;
  text-decoration: none;
}}
.tg-footer a:hover {{
  color: #3b82f6;
}}

/* هدر کانال */
.tg-channel-header {{
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}}
.tg-avatar {{
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}}
.tg-channel-header h1 {{
  margin: 8px 0 4px;
  font-size: 24px;
}}
.tg-channel-header p {{
  margin: 4px 0;
  opacity: 0.9;
}}
.tg-channel-desc {{
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}}
.tg-last-update {{
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}}
.tg-telegram-btn {{
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}}
.tg-telegram-btn:hover {{
  background: #0b5e8a;
}}
@media (prefers-color-scheme: dark) {{
  .tg-channel-desc {{
    background: #1f2937;
    color: #d1d5db;
  }}
  .tg-post {{
    background: #1e1e2f;
    border-color: #2d2d44;
  }}
  .tg-post-header {{
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }}
  .tg-doc {{
    background: #252535;
    border-color: #3a3a52;
  }}
  .tg-forward {{
    background: #1f2a3a;
    color: #90cdf4;
  }}
}}
</style>

<div class="tg-channel-box">

'''

    # هدر کانال
    output += '<div class="tg-channel-header">\n'
    if avatar:
        output += f'<img src="{avatar}" class="tg-avatar" alt="avatar"/>\n'
    output += f'<h1>📡 {title}</h1>\n'
    output += f'<p>@{channel} • 👥 {members} عضو</p>\n'
    output += f'<a href="https://t.me/{channel}" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>\n'
    output += '</div>\n'

    if desc:
        output += f'<div class="tg-channel-desc">📝 {desc}</div>\n'

    output += f'<div class="tg-last-update">🕐 آخرین بروزرسانی: {fetch_time_str}</div>\n'
    output += '<hr>\n\n'

    # پست‌ها
    for idx, m in enumerate(messages):
        output += f'<div class="tg-post" id="msg-{m["id_num"]}">\n'
        
        # هدر پست (شماره و ...)
        output += f'<div class="tg-post-header">📌 پیام #{len(messages) - idx}</div>\n'

        # فوروارد
        if m.get("forwarded_from"):
            output += f'<div class="tg-forward">↪️ فوروارد از: <strong>{m["forwarded_from"]}</strong></div>\n'

        # آلبوم (چند عکس)
        if len(m.get("album", [])) > 1:
            output += '<div class="tg-album">\n'
            for ph in m["album"]:
                output += f'<div class="tg-album-item"><img src="{ph}" alt="photo" loading="lazy"/></div>\n'
            output += '</div>\n'
        elif m.get("photo"):
            output += f'<div class="tg-photo"><img src="{m["photo"]}" alt="photo" loading="lazy"/></div>\n'

        # ویدیو
        if m.get("video"):
            output += f'''<div class="tg-video">
<video controls preload="metadata">
  <source src="{m["video"]}" type="video/mp4">
</video>
<br>
<a href="{m["video"]}" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>\n'''

        # فایل
        if m.get("doc_title"):
            output += f'''<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">{m["doc_title"]}</div>
  <div class="tg-doc-extra">{m["doc_extra"]}</div>
</div>
<a href="{m["url"]}" class="tg-doc-link" target="_blank">دانلود</a>
</div>\n'''

        # نظرسنجی
        if m.get("poll_question"):
            output += f'<div class="tg-poll">\n'
            output += f'<h4>📊 {m["poll_question"]}</h4>\n'
            output += '<ul>\n'
            for opt in m["poll_options"]:
                output += f'<li>✓ {opt}</li>\n'
            output += '</ul>\n</div>\n'

        # متن پیام
        if m.get("text"):
            text = m["text"].replace("\\", "\\\\").replace("`", "\\`")
            output += f'<div class="tg-text">{text}</div>\n'

        # فوتر (بازدید و تاریخ)
        footer_parts = []
        if m.get("views"):
            footer_parts.append(f'👁️ {m["views"]}')
        if m.get("date") and m.get("url"):
            footer_parts.append(f'<a href="{m["url"]}" target="_blank">📅 {m["date"]}</a>')
        elif m.get("date"):
            footer_parts.append(f'📅 {m["date"]}')
        
        if footer_parts:
            output += f'<div class="tg-footer">{" · ".join(footer_parts)}</div>\n'

        output += '</div>\n\n'

    output += '<hr>\n<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>\n'
    output += '</div>\n</div>\n'
    
    return output

def update_channels_list(new_channel: str):
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

def build_index_markdown(channels_dir: Path, active_channels: set, fetch_time_str: str):
    if not active_channels:
        return
    lines = [
        "# 📡 لیست کانال‌های آینه شده",
        "",
        "| کانال | آخرین بروزرسانی |",
        "|-------|----------------|"
    ]
    for ch in sorted(active_channels):
        md_file = channels_dir / f"{ch}.md"
        if md_file.exists():
            lines.append(f"| [@{ch}](./{ch}.md) | {fetch_time_str} |")
        else:
            lines.append(f"| @{ch} | ❌ هنوز گرفته نشده |")
    lines.append("\n---\n✨ این لیست هر ۲ ساعت خودکار بروز می‌شود.")
    (channels_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("[✓] Index page (channels/README.md) updated")

def main():
    manual_channel = os.getenv("INPUT_CHANNEL", "").strip()
    manual_count = os.getenv("INPUT_COUNT", "").strip()

    now_utc = datetime.utcnow()
    now_tehran = utc_to_tehran(now_utc)
    jnow = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    fetch_time_str = jnow.strftime("%Y-%m-%d %H:%M:%S")

    channels_dir = Path("channels")
    channels_dir.mkdir(exist_ok=True)

    if manual_channel and manual_count:
        print("[*] Mode: Add new channel with specific count")
        limit = max(10, min(int(manual_count), 200))
        update_channels_list(manual_channel)
        messages, info = fetch_channel_full(manual_channel, limit)
        if messages:
            md_content = render_markdown(messages, info, manual_channel, fetch_time_str)
            (channels_dir / f"{manual_channel}.md").write_text(md_content, encoding="utf-8")
            print(f"[✓] Saved {manual_channel}.md with {len(messages)} messages")
        list_file = Path("channels.txt")
        active = set()
        if list_file.exists():
            active = set(line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip())
        build_index_markdown(channels_dir, active, fetch_time_str)
        print("[✅] Done")
        return

    print("[*] Mode: Full refresh of all channels (cleaning channels folder)")

    if channels_dir.exists():
        for item in channels_dir.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
        print("[✓] Cleaned channels directory")

    list_file = Path("channels.txt")
    if not list_file.exists():
        print("[!] No channels.txt found. Nothing to do.")
        sys.exit(0)
    channels = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not channels:
        print("[!] channels.txt is empty.")
        sys.exit(0)

    for ch in channels:
        print("\n" + "="*50)
        try:
            messages, info = fetch_channel_full(ch, DEFAULT_LIMIT)
            if not messages:
                print(f"[!] No messages fetched for @{ch}")
                continue
            md_content = render_markdown(messages, info, ch, fetch_time_str)
            (channels_dir / f"{ch}.md").write_text(md_content, encoding="utf-8")
            print(f"[✓] Saved {ch}.md with {len(messages)} messages")
        except Exception as e:
            print(f"[!] Failed to process @{ch}: {e}")

    active = set(channels)
    build_index_markdown(channels_dir, active, fetch_time_str)
    print("\n[✅] All done. Full refresh completed.")

if __name__ == "__main__":
    main()
