#!/usr/bin/env python3
import os
import re
import sys
import time
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

def utc_to_tehran(dt_utc: datetime) -> datetime:
    """تبدیل UTC به وقت تهران (ساده و بدون نیاز به pytz)"""
    return dt_utc + TEHRAN_OFFSET

def to_jalali_str(dt_utc: datetime) -> str:
    """تبدیل تاریخ میلادی UTC به شمسی با ساعت تهران"""
    dt_tehran = utc_to_tehran(dt_utc)
    jd = jdatetime.datetime.fromgregorian(datetime=dt_tehran)
    return jd.strftime("%H:%M · %d %B %Y")  # مثال: ۱۴:۳۰ · ۲۲ اردیبهشت ۱۴۰۴

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

def fetch_channel(channel: str, limit: Optional[int] = None, after_id: Optional[int] = None):
    """
    دریافت پیام‌ها از کانال تلگرام.
    اگر after_id داده شود، تمام پیام‌های جدیدتر از آن را می‌گیرد (بدون محدودیت عددی).
    اگر limit داده شود (و after_id=None)، حداکثر limit پیام آخر را می‌گیرد.
    """
    messages = []
    channel_info = {"name": channel, "title": "", "description": "", "avatar": "", "members": ""}
    base_url = f"https://t.me/s/{channel}"
    before = None

    print(f"[+] Fetching @{channel} (after_id={after_id}, limit={limit})")

    fetched_new = 0
    stop = False

    while not stop:
        url = base_url if before is None else f"{base_url}?before={before}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"[!] Error: {e}")
            break

        soup = BeautifulSoup(resp.text, "lxml")

        if before is None:
            # فقط یک بار اطلاعات کانال را بگیر
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
                # اگر after_id داریم و به پیام قدیمی رسیدیم، توقف
                if after_id is not None and msg["id_num"] <= after_id:
                    stop = True
                    break
                page_msgs.append(msg)

        if not page_msgs:
            break

        # صفحه جدیدترین پیام‌ها را اول بیاور (برعکس ترتیب)
        page_msgs.reverse()
        messages = page_msgs + messages
        fetched_new += len(page_msgs)

        # اگر limit تعریف شده و به آن رسیدیم، توقف (فقط برای حالت full fetch)
        if limit is not None and after_id is None and len(messages) >= limit:
            messages = messages[-limit:]
            break

        # گرفتن قدیمی‌ترین ID این صفحه برای pagination
        ids = [m["id_num"] for m in page_msgs if m["id_num"]]
        if not ids:
            break
        before = min(ids) - 1

        time.sleep(0.8)

    # اگر after_id داشتیم و هیچ پیام جدیدی نبود، messages خالی می‌شود
    if after_id is not None:
        # بدون محدودیت عددی، فقط همان‌هایی که جدیدتر بودن
        pass
    elif limit is not None:
        messages = messages[-limit:]

    print(f"    ✓ fetched {len(messages)} messages")
    return messages, channel_info

def get_latest_message_id_from_md(md_file: Path) -> Optional[int]:
    """استخراج آخرین msg_id از فایل مارک‌داون موجود"""
    if not md_file.exists():
        return None
    content = md_file.read_text(encoding="utf-8")
    matches = re.findall(r'<!-- msg_id: (\d+) -->', content)
    if matches:
        return max(int(x) for x in matches)
    return None

def render_markdown(messages: List[Dict], channel_info: Dict, channel: str, fetch_time_str: str) -> str:
    """تولید محتوای مارک‌داون با CSS توکار"""
    title = channel_info.get("title") or f"@{channel}"
    members = channel_info.get("members", "")
    desc = channel_info.get("description", "")
    avatar = channel_info.get("avatar", "")

    style_block = """<style>
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
"""
    output = style_block + '\n'
    output += '<div class="tg-mirror">\n'
    output += '<div class="tg-header">\n'
    if avatar:
        output += f'<img src="{avatar}" class="tg-avatar"/><br/>\n'
    output += f'<h1>📡 {title}</h1>\n'
    output += f'<p><strong>@{channel}</strong> · 👥 {members} عضو</p>\n'
    if desc:
        output += f'<p><em>{desc}</em></p>\n'
    output += f'<p>🕐 آخرین بروزرسانی: <code>{fetch_time_str}</code></p>\n'
    output += f'<p><a href="https://t.me/{channel}" target="_blank"><img src="https://img.shields.io/badge/باز_کردن_در_تلگرام-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/></a></p>\n'
    output += '</div>\n<hr/>\n'

    for m in messages:
        output += '<div class="tg-message">\n'
        output += f'<!-- msg_id: {m["id_num"]} -->\n'
        if m.get("forwarded_from"):
            output += f'<blockquote>↪ فوروارد از: <strong>{m["forwarded_from"]}</strong></blockquote>\n'
        if len(m.get("album", [])) > 1:
            for idx, ph in enumerate(m["album"]):
                output += f'<p><img src="{ph}" alt="photo {idx+1}"/></p>\n'
        elif m.get("photo"):
            output += f'<p><img src="{m["photo"]}" alt="photo"/></p>\n'
        if m.get("video"):
            output += f'<p>🎬 <a href="{m["video"]}" target="_blank">دانلود ویدیو</a></p>\n'
        if m.get("doc_title"):
            output += f'<p>📄 <strong>{m["doc_title"]}</strong> <code>{m["doc_extra"]}</code></p>\n'
        if m.get("poll_question"):
            output += f'<p>📊 <strong>{m["poll_question"]}</strong></p><ul>\n'
            for opt in m["poll_options"]:
                output += f'<li>{opt}</li>\n'
            output += '</ul>\n'
        if m.get("text"):
            text = m["text"].replace("\\", "\\\\").replace("`", "\\`")
            output += f'<p>{text}</p>\n'
        footer_parts = []
        if m.get("views"):
            footer_parts.append(f'👁 {m["views"]}')
        if m.get("date") and m.get("url"):
            footer_parts.append(f'<a href="{m["url"]}" target="_blank">{m["date"]}</a>')
        elif m.get("date"):
            footer_parts.append(m["date"])
        if footer_parts:
            output += f'<div class="tg-footer">{" · ".join(footer_parts)}</div>\n'
        output += '</div>\n'

    output += '</div>\n'
    return output

def update_channels_list(new_channel: str):
    """اضافه کردن کانال به channels.txt (در صورت نبود)"""
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

def cleanup_orphan_md_files(active_channels: set):
    """حذف فایل‌های .md داخل channels که کانال مربوطه در لیست فعال نیست"""
    channels_dir = Path("channels")
    if not channels_dir.exists():
        return
    for md_file in channels_dir.glob("*.md"):
        if md_file.name == "README.md":
            continue
        channel_name = md_file.stem  # بدون پسوند
        if channel_name not in active_channels:
            md_file.unlink()
            print(f"[✓] Removed orphan file: {md_file}")

def build_index_markdown(active_channels: set):
    """بازسازی فهرست channels/README.md"""
    channels_dir = Path("channels")
    channels_dir.mkdir(exist_ok=True)
    if not active_channels:
        return

    lines = ["# 📡 لیست کانال‌های آینه شده", "", "| کانال | آخرین بروزرسانی |", "|-------|----------------|"]
    for ch in sorted(active_channels):
        md_file = channels_dir / f"{ch}.md"
        if md_file.exists():
            content = md_file.read_text(encoding="utf-8")
            match = re.search(r'🕐 آخرین بروزرسانی: `(.*?)`', content)
            if match:
                last_update = match.group(1)
            else:
                # fallback به زمان تغییر فایل
                mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
                try:
                    jmtime = jdatetime.datetime.fromgregorian(datetime=mtime)
                    last_update = jmtime.strftime("%Y-%m-%d %H:%M")
                except:
                    last_update = mtime.strftime("%Y-%m-%d %H:%M")
            lines.append(f"| [@{ch}](./{ch}.md) | {last_update} |")
        else:
            lines.append(f"| @{ch} | ❌ هنوز گرفته نشده |")
    lines.append("\n---\n✨ این لیست هر ۲ ساعت خودکار بروز می‌شود. برای بروزرسانی دستی همه کانال‌ها، فیلد channel را خالی بگذارید.")
    (channels_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print("[✓] Index page (channels/README.md) updated")

def main():
    manual_channel = os.getenv("INPUT_CHANNEL", "").strip()
    manual_count = os.getenv("INPUT_COUNT", "").strip()

    # تعیین حالت اجرا
    if manual_channel:
        # اجرای دستی برای یک کانال مشخص
        channels_to_process = [manual_channel]
        # اگر تعداد مشخص شده، از آن استفاده کن (full fetch)، در غیر این صورت incremental
        if manual_count:
            limit = max(10, min(int(manual_count), 200))
            incremental = False
            print(f"[*] Manual full fetch for @{manual_channel} (limit={limit})")
        else:
            limit = None   # بدون محدودیت، فقط جدیدها
            incremental = True
            print(f"[*] Manual incremental update for @{manual_channel}")
        # اضافه کردن به لیست کانال‌ها (اگر تکراری نباشد)
        update_channels_list(manual_channel)
    else:
        # اجرای خودکار یا دستی همه کانال‌ها (بدون ورود کانال)
        list_file = Path("channels.txt")
        if not list_file.exists():
            print("[!] No channels.txt found")
            sys.exit(0)
        channels_to_process = [line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        if not channels_to_process:
            print("[!] channels.txt is empty")
            sys.exit(0)
        limit = None   # بدون محدودیت عددی، همه پیام‌های جدید را بگیر
        incremental = True
        print("[*] Bulk incremental update for all channels")

    # زمان بروزرسانی به شمسی و تهران
    now_utc = datetime.utcnow()
    now_tehran = utc_to_tehran(now_utc)
    jnow = jdatetime.datetime.fromgregorian(datetime=now_tehran)
    fetch_time_str = jnow.strftime("%Y-%m-%d %H:%M:%S")

    # پردازش هر کانال
    for ch in channels_to_process:
        print("\n" + "="*50)
        try:
            md_file = Path(f"channels/{ch}.md")
            after_id = None
            if incremental and md_file.exists():
                after_id = get_latest_message_id_from_md(md_file)
                print(f"[*] Existing channel, fetching messages newer than ID {after_id}")
            else:
                print(f"[*] New channel or full fetch")

            messages, info = fetch_channel(ch, limit=limit, after_id=after_id)
            if not messages:
                print(f"[!] No new messages for @{ch}. Skipping update.")
                continue

            md_content = render_markdown(messages, info, ch, fetch_time_str)
            md_file.write_text(md_content, encoding="utf-8")
            print(f"[✓] Saved {md_file} with {len(messages)} messages")
        except Exception as e:
            print(f"[!] Failed to process @{ch}: {e}")

    # پس از اتمام، لیست فعال کانال‌ها را از channels.txt بگیریم (که ممکن است در همین اجرا اضافه شده باشد)
    list_file = Path("channels.txt")
    active_channels = set()
    if list_file.exists():
        active_channels = set(line.strip() for line in list_file.read_text(encoding="utf-8").splitlines() if line.strip())

    # پاک کردن فایل‌های زائد
    cleanup_orphan_md_files(active_channels)

    # بازسازی فهرست
    build_index_markdown(active_channels)

    print("\n[✅] All done.")

if __name__ == "__main__":
    main()
