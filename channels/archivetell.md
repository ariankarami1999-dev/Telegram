<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/g2KPvoJEb-pbzXPAtaYx1EHnXJraooqUVCQSIoT8dS0KFly5_Yu0HThFd1FklMz_udiXm56n3er5B4ZYsZ1Fn05p70wV5FW15EUnU34XVmcpPXSxAchkI9_vSiMGiVR4DFFHBMSrZblJewZca-iLoQkz2iTR6DB4nUj2dy8wXQLPqjTY8oUUYVE7UHXjh0jqiUQizo0vTOUEGphy7biNZt_mEhlzJcwypb1qx2mPfs05H5nfZ5M0IzWgn_GmPEXbfrZl1lsyXk33-qFqCEgvs0Cnh2a4_gfAflWlmIJaK9HlzdkopT7PggJJ-pN5WYaQ39OF7OyGOe_RxgYmFMehRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 01:26:55</div>
<hr>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svRKp6frvHnNqB2ilfb9eQGOFKHxMlFnTTNQ0PNeRc2mOOMjM1WQYnxh2z3cQgS9pzIqmCY63hzi32Z2ZEpV71XhDIe1ivJd9PA9qza_lyJ06rQ2cBca9OT9cEK3UXcYa7rd8mI2_AsIbzAc-Zpsde5HmovYXDkwqORIBsCJNBxqI6YbFTbC7Ea1TRGXX2FORuWEWXzazuw_J_Fo24ViCzKTaVoHWdw4GcaolbHwS6BG1TmZaeMVpwcnmppR5T-WKkEmQnSKisVpYlpV9OaPn0EvCgUSwORHHzx4dIZyztwH_1kpV1yrR5SU25tHMB0qvkIN-sQkdb3JPLg9P5xKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🪐
اضافه شدن GPT 5.5
🔸️
قابلیت تحلیل عکس را دارد
🔹️
در گروه ها و پیوی فعال است
🔗
اضافه شدن قابلیت های جدید
🔸️
تحلیل عکس برای تمامی مدل ها فعال شد
🔸️
سرچ در وب برای تمامی مدل ها فعال شد
🔹️
در گروه و ها و پیوی فعال هستند
🔹️
وقتی با مدلی چت میکنید به صورت پیشفرض فعال است
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 467 · <a href="https://t.me/archivetell/6363" target="_blank">📅 00:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=Pb0AQU7qtWX2BcUPsW2X6ZCBmzdcRHlwiFxUB4kpJbgy_XIgpdfofWEf0c3g5dBUifRSKhcWIRJP9wNTmooQCYW9KaphkqGvGs2FkUO6s6kNb2NfcMNS6XDqsugpXA6lO7EimW0hq8phGwfBNDobRiL1WmeMMjmHN8UTIIvY4-vUhhvZl4dTwzeg8THEglgLYmXIE5rxoYLKYRLEyn7dkAedXQbjRCMGjiFkDOfA5nysKU6JacLkLdYpVPkHskm1IQ3xY8nOoqMgHZIQxN4O24WghiMd49NgoY1YNgmpDdZIk6YWtpIU4IhBe2tINq2H_qGHfz0fKT2bNYx9QeYiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=Pb0AQU7qtWX2BcUPsW2X6ZCBmzdcRHlwiFxUB4kpJbgy_XIgpdfofWEf0c3g5dBUifRSKhcWIRJP9wNTmooQCYW9KaphkqGvGs2FkUO6s6kNb2NfcMNS6XDqsugpXA6lO7EimW0hq8phGwfBNDobRiL1WmeMMjmHN8UTIIvY4-vUhhvZl4dTwzeg8THEglgLYmXIE5rxoYLKYRLEyn7dkAedXQbjRCMGjiFkDOfA5nysKU6JacLkLdYpVPkHskm1IQ3xY8nOoqMgHZIQxN4O24WghiMd49NgoY1YNgmpDdZIk6YWtpIU4IhBe2tINq2H_qGHfz0fKT2bNYx9QeYiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbxxY76iggMGez159gzTo-ZezAJFQFfOk2iXpBsOmuuWkuE2bzo_8HIbTWfbwkHnLjL3oKXPBF8yeLtJTBN6d0iWTxZWAaCqu5OdWsPhoPsxxh33z-wrtgr7nVXCX1kIVIet7RovgEJXCg0_sdYn3WReNOrWgfFN81AxVpyChZAzCu95lQnNsEjODMvqOGTs4bSodChQDgSClxTWbgqA5sJ07g4UC8iHLOjpaWTUyuGxwvnRsQBtdIzbhdGhoKfXruRlIyv-0u7yKtGN3jIWy0ZpyrPJe1I5XIC-XYQYjVcRq7hme5lCD9M3l3AGXCaRB8jvUTKBgpVLw80AF_eKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR5fud7uFOW1cQckANpKGgTuaMGXJY9GKzoY4zjnr8V39IfOP6JrtpULFEvuXaEi5j0PPkeESov7XIFRSkL9aP_DnD7EZ9GK_yfzvAHvSGF1d1QwFqZd1dBK0CI9zz0-G-lwuXWJ-ATx51jixFJd_4J98yrgwZk8GP9lQg_Ej3qWNspE3aKGJjcpCuXQicKST3HPw-9XDDsx9AdfzmgiC1-P8ydb3DKJAqwhSDzR1G7AFTppyu8ehBuEIsKKX7mXd9EwlaUO_OX4_t2r3X3V_yV2RWXMhMqmYNaMHO1ydOGsyCC4cHRpt04nX13FLDg0ZWDZigz0KliGrHf73vmG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=vTTaTDmgQQY0OTHXWusCr4P6qQRJ3rDcyAmGrqQN2DAp3UPj5VVn8-g_cv135yF5b-ljisRHMgD4nYulNtSIRzA7yfAF3bPoKWmJXs1Uvqnxtid8Tsn2orroJoh7T2Z69DhYAieJNB558GDHzCcHN_Sg_YsWxbHjk-RPt7tx-eb12C5h8wnNXYM5c_fNrcW5V2nWNJpjpijFCycR4R567rqqlrSHPDJo64DSTq2e6cvs1Ouc4JxyHCdnvH9rUuWRzgWKeEih0PmdZgLcWKxBB8_oDi5PbuKigac25Oa8XIavmIuX2yf5m4FOV6do4stZYV9VyfuhMau3vdWA7ceFXhn5d_L3GaBA7Pq3OO5D2zrmNZ5oRxOyI3Z-z3-30R4vL10SosyNI1QLEhRvZvN14Jqrjj2rcVLwmyTdJ1c8NYcjTKstDnHnU-eUygL_PQQOSscRdEkHITnPP2QIwnbGK2keuAJox2fVJdX_GtKXP9TcHKOCBMRlJUZfwMN3DkWcVbFMZ53QRQj0qhsndSu7A1wXT-Gy-83jO7P8oH-6JnKGpDUSiH6OXgWw2c2DvFQ8KjUaXxD2hgbN2AoCoNGpzKBfgRPQE2tkCEEWs_rBeHg5qbU4afqrIXOj9OQ9uJ5IyoZmrDxV1VcNK9_MF-oEEmHniZWXynqJisNyjhJFRy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=vTTaTDmgQQY0OTHXWusCr4P6qQRJ3rDcyAmGrqQN2DAp3UPj5VVn8-g_cv135yF5b-ljisRHMgD4nYulNtSIRzA7yfAF3bPoKWmJXs1Uvqnxtid8Tsn2orroJoh7T2Z69DhYAieJNB558GDHzCcHN_Sg_YsWxbHjk-RPt7tx-eb12C5h8wnNXYM5c_fNrcW5V2nWNJpjpijFCycR4R567rqqlrSHPDJo64DSTq2e6cvs1Ouc4JxyHCdnvH9rUuWRzgWKeEih0PmdZgLcWKxBB8_oDi5PbuKigac25Oa8XIavmIuX2yf5m4FOV6do4stZYV9VyfuhMau3vdWA7ceFXhn5d_L3GaBA7Pq3OO5D2zrmNZ5oRxOyI3Z-z3-30R4vL10SosyNI1QLEhRvZvN14Jqrjj2rcVLwmyTdJ1c8NYcjTKstDnHnU-eUygL_PQQOSscRdEkHITnPP2QIwnbGK2keuAJox2fVJdX_GtKXP9TcHKOCBMRlJUZfwMN3DkWcVbFMZ53QRQj0qhsndSu7A1wXT-Gy-83jO7P8oH-6JnKGpDUSiH6OXgWw2c2DvFQ8KjUaXxD2hgbN2AoCoNGpzKBfgRPQE2tkCEEWs_rBeHg5qbU4afqrIXOj9OQ9uJ5IyoZmrDxV1VcNK9_MF-oEEmHniZWXynqJisNyjhJFRy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DulBwb702fkGrkdEippizyO7hmSyc-c7fxa-6jxLOOr9Qd5W-ObM2hDPZBnfcWlvut1DwtdFOCjsByZBzQRDsy_I_KPgSp_UoshzKgPu75HOAOrKJPJC6BWEkhzeTPs22dJ0031f0UYBvnafl8FhyFmvpmYkc3KhK7kYss65oOkJ8fAC5qBiHdP0ERcxoifqAYOHjRxiIkXZZmh_0co8B8YMwmYs_BNXJIo4vVE0jl-tGwYdRXl4L2sAXPx7VPDK9LLEHlzUKHSRKnSL2bSNNW2x6bnE-E2E9T7m_EN3BSaf_0m7G6XRD9qmQ9Pdy00kMDGY_TLXOY73pVJPXTGgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=DulBwb702fkGrkdEippizyO7hmSyc-c7fxa-6jxLOOr9Qd5W-ObM2hDPZBnfcWlvut1DwtdFOCjsByZBzQRDsy_I_KPgSp_UoshzKgPu75HOAOrKJPJC6BWEkhzeTPs22dJ0031f0UYBvnafl8FhyFmvpmYkc3KhK7kYss65oOkJ8fAC5qBiHdP0ERcxoifqAYOHjRxiIkXZZmh_0co8B8YMwmYs_BNXJIo4vVE0jl-tGwYdRXl4L2sAXPx7VPDK9LLEHlzUKHSRKnSL2bSNNW2x6bnE-E2E9T7m_EN3BSaf_0m7G6XRD9qmQ9Pdy00kMDGY_TLXOY73pVJPXTGgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM9ip4UFAkNUUHFHM9LRi231zAKOVd8Xes_LMjV089AMRgTcSYkBH7Ok-LXAcxoaTT-F07kYMFN8VAtGXPCeYqVpXCMmPQMlxdlx4rjJFxOUUpqJmOJ5BVxZ7RhfHQPIVlpAp2CI0Z_HJPBJjTdgqKed9Y6bdJiAT6er_P07D6MndcmgYxmEq4NhaggpTP0LzPEtxCuySTABqa3vlgZehU6YaamdAnxFRHZzyyARJjKNflijJ-thg0J4Abu9ZAiyKScei3rpCQV6b2Jj1LjoNmRGtsa5He2z4tX5xSHwMOK8MyMYxF06UzfTG2m8-WuzXR4P1NVPHgoCB5Z9PReVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7lXvoSW8cS8BKbOZd5JC5MQxKyi2PuvADyO8JPB9lZbB8kfDCX1haYNd3iy7-rLkt4pYH-gHiV9ZTsWLiy4AnnPjNI1Nn8lukI8E4sYX8ZDolTZtN9vBHezShBkvNnPxvnxBFW2lKt_v19MYdhpg_1WTI6ZBs3A4eHRcED10el8AHsfxd3ldvSmBTrULIQdMrFQZ62-Fl0dYBa04W0psiycgDMvIfAcebBFr6H23CZN2UZuFEXRPSbXMLAX-SO1_5-vFTW8xcbExb_4jsKstxb6s7QEcjxZD1PHndfPtvlIiMm3UcsTe-wO3s1PwlyB5V6__3H-hA99vzj-QiEJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJP4tA9cR6CQ-2FJvr8wqZc5zET-g5xpW1NkK6ecT7alyGFdqMR4BjxkVlJZy-8p4TiWRqoYSu4GXRwJMhEdWqz7FQyAQJlmLVkm4CUXk4OKHdIHkkOf1Rwv-s_ueUCz_5dyXufurDV5q-FNme-jPdPhRECGLbQPwXeIc3EwHuK8Q86gv8ym8PFwwis81ECG7xqlO5q34tIrvLY3Z-UweEY5n57wO6Bo0P-Wj3E7PRYe3p8LErdU28BRQLGWbyonwB-LdaE0EYc_iacHYtAoBNyXv39XRaIrU0Wy6vgYHkzmAmsa9PPEkNrfJVNuafZkkONpMdBFD9r8ebS4hvNUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lnd4rPPxY5ERlBR-Jvl_6EDy5ZsehppJeNYX9wRZA9K5-KPR73D1_7SVHELShT9BBF42Iu30QM5aqEZyPfUqpXYQlAyOicDyB_oX_DZhOEiY_oW8MDTqEprtQn4S2mqQRWXHvFTjfVKKVdJJTNeEhFJ2EQASgZs9CaUMH7jYHVbY65Bn6JM1S8jgCDIxPMDFTKuzL3T0l2pQnPFCqaiU0G6I2zKe5hlsX3OnNMP0OcvE_yakvBF3y82d3umxSpA7c0lvtQwCtaR2xy5W0Mqnu_-3aHchfgjfnCnIxLwkGvGPz5St7GGQU3pQTAiy6lq7avXhErzQ2JGIq5jlZXgQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkAhOH7T_UnzPEDafG8CHgTcMBYOEPgRDSQJbrs9ogeWP8CvDk1ZyaIYzA-f7chbxRud0M6cSe1x0BrDrkphJmKhD74O6zSZviwWicByxY9JyfXwAQvpA4DEoP5WTl8i20SnX2ciXWr19XysCD1y_k9PoGjzVC9WfalwpuRegDVWWX0RuP37sNvxO0jlJmB61nkI1qbCPRY0kvNgBapdh0tzR8m98GuPKngJB6NJooDZjesn_jqVsVmfa66M-C_YD5UjT96hOUlGLWHuABR4PVBw8bzTh-slkDpDIYKS1w4qX66mFm3uUbLN7htzfH-u2gLgB-eKieM9X0EqOaXlOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsyeEhDP5Mypm90HV3nEzOPUXy7blTfEMTn1W2ZR_7_UJ__Je0IgLuHzuMcy4r8Y3h6gwliB2MBrGrOLZJOtU-RseZvogs5SkekjWFZYjij16df_B3BFWSDL0lX-EBt76N8irQesndaMi5z2EYlKGwnR8fFm6vfUI1wAh38uo71kM8uct5frnBKVn81r0K5VevXE5MqB6rSOmZTvNuMqT6X5ioGMqvIpe_zznslgAQt3Xq9KF88PRV5FUcgKl4QVMhkVVUw1FRQlIPgw7fr39xY_J2yW6Us4jhFbgNqtBVV2Dv_7QlUDYsLQ0k_G_RFINNwVFkwrqVT07Dwqb0Cqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkpXFTXOkjE3cDqz8ThXS8MwqciqfIiTOVw_AovUR3Bnl7MzwNzwRK4Iy_iajibhHpI76lVROPAV3rXhSwqsMf8K1wdzXn0xoZngI-aUCYG8k64-2j-xBFBj7jKQJOUOYpvXUmMRDPenDr1tZsVCuXUMlNBz2QutIJv90iAT_c4Y9cNjlXwiTmVeUdaj6uClNLA9URa_1es_MbjP2ffA8UHmkBHTVN9yDkkJl6GzXHn5xa05xBOQqKY-Dlm-w1Wg2PMvsQkqP80VsRJYwBcrnI9ea_SLev25PNXmO58jBYSFmbX7RsLdOe9H7ean8KADJvMBpNIVcUSmSqNycLJYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMAtD47eDWpbzRla0PBqWDt1jAdrQ84F9rKait00B4luFQVM_ZEM9S7xGv6nrodvhWFrl-c-3CwCa8EyFvR_IESHuR5HDj-vpOtFoS_7tfQK2GL9GNlZMhTXjoGDtUG1FM4ITrqgTPNwD55m3imdesoZGeMGbzUoSOmc3HWHQZ4b7GOQPUtB4CAsS7v5DF0xYm4K6NalEFYvnA9JhFKrQi6WldQWtHqocWOy45a30ZSlYTqQ_O0_4YfIbvb2rdQ3DByx_jOIVCayCpLyG_Mtu2y5Y-MqLEe3UNLw6G9BXiYHrygFJ36fh4Qp9PEIbcgGylszm5-C3H6kRiIDeJd3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUb19QXkgpiOExts7XVbsbsWEdyvKoCQ0I-R9aoJ11I04VxlxicruCpBWh6kyCw7YUrqOwiBxYxzEB2fTR-vXM8XYtwKF3kymccnpa4gMS3P9Maju5yOU0LrF8KMGapd32GbcKhWOAmrW50vXHVDLSyL0w-a8C0i2R1rN4HssIfQTaBwUpANZbgG3oBUIB0MBYBq1Wb5Rslj3s17lNIdMjg0VAMD8JzpVPqD7p1ipWo4yL2U2j55J7fCW_5EPwAqUG7ejpaBV8Dg-dCcG7O4hS5Ney0FNYP35R4rcUnskZ8XhXvOlCtYN4FGjq679jyS6R3IYLlnOTizRtPxqjGtsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLL4d3f0nMjal3d0xRZuig8Fijz9HkeDvhuPE2NoP9_g6QhOrwcB_7FBliX2feqgSUIanFAdKWMR_gd3LdDiEKiRv6YqbBLG6WVjzltDC2x7r1CLcrbGs2k3Yg5IJdl1vqbkN8fY80we21QKcY6BJ2hJf9RZLsnYEpuDPyx5wCUkS1ZbFtsfCNM3dF4xbQzYXOgT-p6Dqmbfw-28GoH_pLN5kg1j1vBT1jd9906KCPNj_KP8v3vB1MjvEJtS0YD5kAeG9pA5_1LCSEkxN846VGUjU-D131wH-7LcNSGWhTjdOJx6mYxr8efVLUVFAFqzyuPdYbwTA6xLqdXkh4BBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R58z0JvvTCE6oYRLHOIR7SxwXHAU6K-hbVAR713z3qEhxRwefR3W1wGbMwg5Amrjov3g-ZF1s-fbsGFce3fG1OGidn8H7pusac-3qrGZOyMe6tk86nQ8Qdoy7KoDPKfK_toivXWNcmBPoT1py8ZZrVRfcpFj-cWazC9mi9c4m33dP1GdTTyfYLAbAt-U2eKuAMjbG0VN9v-AkBG10xHaOEMAxL8D4-kNXpnoMeXVZG7UbWyAaC_RQ2jtptt4K0G-aA-Z9Kj8CZQCZjjp80yl1MZSceXL6TEVfMLS3BijXwf8tLm_-iE8t31ka1BsttbnzqQf5qabK_l_Lc2vt6taLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7BvlPjs3SfR_eddoSfovWTDOvu24Bj1ttK2F9C4OV_REI7rKm6qaEu6WqS3ZP3zIbtLqDtANevwCrshPEdOCPpd2uOs5F-ccCHsoepHwPQFUKXsqhvTktDTf8DYCacM8Hwy7F4P5IYbI8llKz6PLlbLUOuJ10DF1kAIYplDlHrNAHbAsPVaUwiKHJcA7jpQSqq2FI5e6Z37zEGCqnQ4wC2_xevRJCs2iwtoLyBPm4r8URCMk6WeDmuHuTyXz1wiAC4kX_oqkLApZfG_wdZSvGsoHC-7_DR-1B3lNL8DDFVShzd2xXJj0RNVHjWy0DlTLmCBmBAId_W-Ubbj-1R0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=GFl81itXMxIxF81dw5KSDXh06w7oK-yWW4dzBwnR8N87Efh4ralTi2q0N50A77_rmy2rkrOosaW0q6LbzFzkgbrKzj6jDOinPdIW5XRhLL27jCtklgj6Vuzdrbpmv4SHaObOMWd6XEi_R68-pqZz_EnlsdEioyxB4V9NeBZmFeDoUu2yTlrTOxyd8opp7vgzpr8MBp0y5R7Jz00h5ibXDHhQaCnFNEcONwv0F1kDXrfSwpiNWXU9VttUo7jbAb2miBG-EQ1FR0h4zLtlZl0rxojS3rpRL47kYVuw-ynlXVzKR1uahq75BdheZA_RCMJoyokvUMJr6ForsDPer7WH0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=GFl81itXMxIxF81dw5KSDXh06w7oK-yWW4dzBwnR8N87Efh4ralTi2q0N50A77_rmy2rkrOosaW0q6LbzFzkgbrKzj6jDOinPdIW5XRhLL27jCtklgj6Vuzdrbpmv4SHaObOMWd6XEi_R68-pqZz_EnlsdEioyxB4V9NeBZmFeDoUu2yTlrTOxyd8opp7vgzpr8MBp0y5R7Jz00h5ibXDHhQaCnFNEcONwv0F1kDXrfSwpiNWXU9VttUo7jbAb2miBG-EQ1FR0h4zLtlZl0rxojS3rpRL47kYVuw-ynlXVzKR1uahq75BdheZA_RCMJoyokvUMJr6ForsDPer7WH0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BywgF60VrKpsBjD2zOOaFxZ769NK7pSjqP0ffMJr56PIvV8hoOpkt1-f0J58lbRUneCyYFFAmv79EYt1WfnvjfQkE5KUrxKy6cSPNFSbhObZuPQ548CWKx4rlnyn0hcWk9BimQDEIaPhrfAMh7y0VIjFK9lb6-iU2lwknz-F3mMHuvR3VDlhUvCks1Ry0V_rQjTZzwwopLSC6dPVjvzWPCNw4m88v_IiAWMi_cI5CalELN2rnoTa-Ban4HJu-hhDt5uBihP-wqHIviHs-UbzLzHm6zwQq_uqKffE31DQuOG5IYmsugFO_CCOe3gp4BvESqB9RwDHaZqqE3OB5j6wDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ0_YGugdoT_WUFGgsowQh_HW3Gn6HzoDh1O4zT30Rk99uOe83dIOlHfJjaApkmUe8fZ6DvzTjCtMC8Eit5KLwsVPIovSnGqP8Ot49kYlzbgxdOhWxbxqIIi5hDBFHHqzcAzwE-6BGN5WP1-OhC96TVbW7qMZXGki2kXsxy4U4N-M7k992d9Kxkf14V4aEMo2GqzuBV-ajMcgSgABdOgrfnYfH_SVjJ6msJRfE4LUA-KyEAapH4apebkDvK8qOSK1VBT26JVGC0EujQvyb7W2Oj_5vWytxIoxMgWAanX1Ububqos-1StgO7pzRplZn501YuWFjFs4RVLtVSSaqHLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
-
لینک سایت در مرحله اول
-
لینک سایت در مرحله دوم
#GPT5
#AI
#API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4yX5OO7Y_Zi4M3gddLOgPFjKE3EEhcKCsoLgbiHiavuTuLhIhvbD92nFMSgmA5o7ufNAIiL0rYPfMt_cvwP8XzP8m1LvyPBsAz9JJt-DkwcH2vWDpxwLFO2OoR2JwAN_jJAKvorSO7M3pLolli_sMpIflC0lHZ2zxJKwyDNI6SEycCS9Es0AC7kjRyOwFHi9jf4-KnST6w6o7Qf-BCuPNHx5ihaiXoeNn9dIHAniD_Gr6lBnUmvQu2xYUjASffPpVEyf9kL7KHrA_krtRtH7LrKBf5oRSNye1xurdQzxFG4xVof0tvYFJKnh7o_5a7LyiswlMwXMoKH1jSZf3O2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPEjBtPuExHOuFAdE9GTA1lBec9_u3qV8HX2hLS2rB0kZiwiQ6fiSAEvmk8idNxUe0FuFgsdWNNUKh8OBkWk-C_eC0HVh7UQr6na2dLA60q0OeRmykSOv69Dsd2jy0zXEipZTdN1uLNuCvKCC65QGvsHmirYu_w3z41UGeMw1nv1bTdrTxYwtBhU4HINqL7rX2No5hQnBESRUq1ee-5Lhqm8qA1BrJcU8uUkw8E3CgJR3j3Jc2yaKjszse0L04oiQ6wFcDvbz6yblFQMu8NkZeN_Oky1C-MBq2UG3eB-onlY33EUW1vXhMvE3l7k0gQqMzev2KVd6idLrVGnUSLzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت بازسازی عکس‌های قدیمی بدون از دست دادن حس نوستالژیک
📸
Repair physical damage on this vintage photo: remove scratches, creases, stains, and tears. Restore faded colors, rebuild missing details naturally, and keep the original grain, lighting, softness, and period aesthetic. Do not modernize the photo, oversharpen it, change faces, or make it look AI-generated.
#ChatGPT
#Prompts
#AI
#PhotoEditing
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=n5jfveMnR636XuA-MCZWvLi7X8lejzUQf8DmUHcwzRfKRztcfpMV1meaJnpZHABMQgphJVF-bYDfq5_aexELhEkZIdBbIfo6fWmNLY6j9CoDm9xf3ZeP7hQ4Fug0cpSCAVQDu4UK_B5WipSB_PYj8u-FFTqBX3rrJW0WE9RpsXOQYsdGuP3C-X44TLrYD_h7YHzy8cgIl4pVIoE1ZqoFrsNUyxtnYnU0tIrEXkp8PiuUxeRVurumLqRZzLLYlsrJJBLTtTnR4WDKvUC6HfJrLVUscEtI4IuLKqn9qo6NVdAMrDIGT8nm0sd-uzY8T1Jxl9styw0m2nr7dy3mSQWGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=n5jfveMnR636XuA-MCZWvLi7X8lejzUQf8DmUHcwzRfKRztcfpMV1meaJnpZHABMQgphJVF-bYDfq5_aexELhEkZIdBbIfo6fWmNLY6j9CoDm9xf3ZeP7hQ4Fug0cpSCAVQDu4UK_B5WipSB_PYj8u-FFTqBX3rrJW0WE9RpsXOQYsdGuP3C-X44TLrYD_h7YHzy8cgIl4pVIoE1ZqoFrsNUyxtnYnU0tIrEXkp8PiuUxeRVurumLqRZzLLYlsrJJBLTtTnR4WDKvUC6HfJrLVUscEtI4IuLKqn9qo6NVdAMrDIGT8nm0sd-uzY8T1Jxl9styw0m2nr7dy3mSQWGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPjrkSyX5Pxu4G9dpzelTc3RWiFhk20WMPF7gwirFw1x1PLDPPjWb6_3vVUnymt574_IRTBbapK-I_9_C-saFNjSz26k3cvvIB5Lrdhvl-vqHB4I6f1Yx3IagnQ6m6IzUHfNItsa2wtIXROkG1oYZvRyWT7HodYBf5G2jO9sFgyxPW1OaufMc1QdvA3pd7i23eCyMo8X1qmt4OaWkqAa1MTxeWSblISqaQXUYyOTNToKdCY0go05Z67WradtS75oGsRnvvQvMx1Tn95uyiPk3Im6Cqs54lf7zUUS5xOBhbk2eIRhz02NdzuuLBewSPlXhqUp5uq751XA7vgPgflMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF1ptVw6SDw48BU2XlL7GWfsG7Ku2E3km4i7F6WPqu8DtRW4BAAKIayqIOH-Cp4GxZE7uT0y74DLvWlYAwgOjEBXg3dQH-1q7v231MHXrfmrC5xr2eC4Fk7Kdl8w5XegspAbXdckYRYd5MkT1Eflal18MfdMkmUx2ppJLh9bPXFA0qlrY4u9BiO_tJ8DPEnBoYnoNcjD0dm9O0teUkwcgCDEjToD64Qg_DuUKk1YtyUd3uEzB7uUsLLp04I6ZfbADjngpekdvEERMjndLcMRzE3f1xY3JqMH3fdBENKgJbLMM2ChsvMfvM0HMkyuwfjEgBKrwxjMQYy9d-LdRTOf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRKEIiXrN8gK59iPP0F-u7xeywMi3JI_g1i8CXsnCbCio1nyL6yuBjr5jwey1b_7Hr_L5W5TfFrqHM95W8Mn5i31XBKqKMZdjLSO6gFs9OPoewxgYawHnbFgdWdMWlwjtdqdZoi_j3lmQHnXdHa3609VGCd1k1NiXfpemQI_kIoCEwNaDzej1JKQoMBivqWS2RRfBVDCJOPviXzO759STvmbdw9KmPZ-VkgghBCRQT69ucv5OA8-YIdw5Eg1O2FfL9axpQpixsNbeyjWJUI5VpKcE3GZ4zxhxf_3_vIrmeA_fAhVVjRTXOGzwF9NhrhqG9_HAg_Ux-g78ouEAbx7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNKQorQUkmEhLYyq8IPbGnDcu0YpZ8pD2rqQ3rBk8RVoJQRWDHQvHKMjKyKWPQ2fQnQBx6XI9KosaGdY4fT6TvfHMDRexT_Zll6oUb-hAGpJAufUxgogqF4HbBTc9L3qXLKEwhBuaOajMZC_YI2Igw9OltEGvpqPqGpdKjShzPXrXCpPHWykflRYjxOJHghjLg7sZ6Acr7p8M3w1Rcn7Ofe0R3yPnR7GlJhUxa_KpSfM-yEYjtSnyr4tXN4-ci1D5Zpqxy5bLxYAFTpxtKdeA18qR8OHY3woZjiHbXn67kb9bdmEWi3iOfEtTuOnMzHZjHPYohQQBFAWR6muLTyzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=D0sD7qG5kCzH6Mu9LIdpADJ-tp60iwi5BTAc9TOJuHdEXRzk5MC8rKCDlga1jwBhHYLAlLfrJCT6Vck0iaFNnYZ3OoVoB--TudbygVCeYNj7UomcjUj2yAkBa8gPLg-_Y3sv4QXt57cBOWXT4cqUASuOSOIY-i-tQA0-c3lntFsxEIsaZAOF6qEz8af0Tci6vEmpB0lFC5XNBAG71lnodqnCCBhzHjRVZgFOfDwzYIALQiVA-tMgSA8TQaYwoNZT3JZ_PjDtDRlGrGMBXDWL4EhrE_bRrkl6HRwJKp0swn-MbJHlNED4kZZA6zJPq0jMp5E0PzuW03LLxutfi8nMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=D0sD7qG5kCzH6Mu9LIdpADJ-tp60iwi5BTAc9TOJuHdEXRzk5MC8rKCDlga1jwBhHYLAlLfrJCT6Vck0iaFNnYZ3OoVoB--TudbygVCeYNj7UomcjUj2yAkBa8gPLg-_Y3sv4QXt57cBOWXT4cqUASuOSOIY-i-tQA0-c3lntFsxEIsaZAOF6qEz8af0Tci6vEmpB0lFC5XNBAG71lnodqnCCBhzHjRVZgFOfDwzYIALQiVA-tMgSA8TQaYwoNZT3JZ_PjDtDRlGrGMBXDWL4EhrE_bRrkl6HRwJKp0swn-MbJHlNED4kZZA6zJPq0jMp5E0PzuW03LLxutfi8nMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENmK9TIqHdVVXUrqoYQUP7sOvmny1Dm9Kn2ehiQ591RMHPiK9eUDzCT3f-GyctXPiVMyi-J0Zlg56OFcsj5Wj-0n9X-Vg61UBF9iamROxmBRIZUBDjYHU0WSAWSB8iJ6e520bsBQ7A-GJ7ptSN6ZHaP7nd2n9KJYL1JbW7FhRqggkCk_JQXZVHfkRv3r7eB8MVdAMoJIWqBqR73QkCp3KB3FFb_oLWe718Y6LqL4w_nptkVGOB3UYBieqzAR67wdGBEFi_Kwti6hcN0EuVFwN3EcLUVWkMLPnFlbsDEXdkZd0j3Zumc4v7F6Qfj_SBq6FYdNkjWCdujSsdgR6QPFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOCIMjLWlPVFKdjPHK9I8WD2l3708BzVhju7jjof_mim5psX6hW6C8dD61EZbTFQvIEFwfkS1SVu7IrvLvLUD0-0WF8kqdUFMcFjYQPBCRWVPumyjDSVe5ICCXW7TWp6Xn7vCpr_i3af9pDeBFiNjNeViDxIxbAglMgU9CnY_FkRXiunjva7QrJWXgEe26pNrZshMoTyFGKnmLe401z05rO7Mpz5MZKxtoTZ7O0N1IIoiVqhMOxN3uV4sjS-OvOcHW95yaHK640FLM-KOyd7TlRPTW-3k1Cc_hrsc2wgjlcFUFtZPeVdz9NHsuEtt6GWa7KxtDXq8pjZmsw-8o4aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ue8dKaglsDaThYoaiv6QFBu_cYZM3QQlBxgmjFh-AGIjS-N4SmOFtqU22r4u7YvSfXg6NDegFd1IhPCGmk7DhlfJILtyEND8zSD-ucKk5eM4Jn-mSzCryC4dZT21ynwVRMPJzCsFf77jwyEcG3xnUZgMEckFkmHPyr8f4Bnf9iSd3kdWQ1OBFlsMf9CotxHa5M7-BCuKl7W7aPGSA19G70a_HbThUawAJQldoo0z9P0gZKEt2chIc67NBlEt6qxZihfjusXFgKeja-i5tfgnB9sBf8YmkaKghGG48u4lRajk15BoalDE6WldQKV2HOrJ9JWWtHTZr_fZ422cinn3bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxnJjV7YsqXhoH3V2zdO8pC3C1oLrDx3H1B-9FziJl7epQ6df2hsuA_LQRnfh4avgmBVW-tpVBWkXMgk2N-GGYyD7zWgnkO_gWctFqnmy7ZdfvprCqWIXEW8Eieqvr-aAIe5OY13qGOxs2OtrXjh3SHm8nwfHAi7zIwm88quCqRm7PLb8XPLm6wdd6VZxnCsfjj5LdEOQBBWmj3tjtFDp735bA_nf5rBW7HLD4lKJe-hj1UzT0tXgcwP9_771pSl2XzeqwpKEbIhlL7TS-4q_u5LbdMs-t1GLdTKvTXODBOeHYY02gvhPpUPUTGzS8w9GOicJejWt1u3mPt-7jZnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcK9_RAKKovB4kjJk1UhZjlq-ANvQg60UN4y-cDqbVN_VhylhAoYe6Z6RqvHIc01uWP-pq4RxCeQ41RdFZR2K9yox313fRlkr1kU0s3D85FBnSbOhu9iFTb0gvpo1IciBuE6tJGMuqGWH81i1ABfKgDEijjFnRiM9s5tHVkeXj3IBTA800sSXNNFmoUQPZWX5_eMaSzRnB3ZQuQjzCcztUoDZtgzmd3TvtFyrE8JjZD5OWWyDi8Vy-KFIe2p1wPscCQdy2hI9P-QcO6XnAldwIwMRru5Iqdw0gXs1ih3CmADQ_gRtqShiB0ibueL0TQ3JwCDRvT5yHNCaBpgwE1GEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aK9SyFeBlKGu9GL2cCvdL-gnvz3iNKDuFKlwW7aJibHQX7AJS8zh7AOYLXjJSAOsydgFrnlEwO4-8YTK-4_cLxNbfEORhKNiNS37EbNl3seWT4PPjZXP4_arJLd8KpgB96rpuCRHt6V9xDpuQ6Z9ULpUhiVXv_J_g9H6Fetd2_v8TPex2_hn5B9GgZQ2fQO3PZBInmZojijfEDcHuNmB00l37wPfXRqIPspmU_GZhmoF9wVEHrd9Yr8Ai8SLPh72JqzaULoZ0A1dm9KbTn0fI0Khx8aPfdSlyq9FSA-w_3ppxqV3qtXd7MldOUyssrVf2t0H82N41KVhVoMBrEjF1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=pWjrPvOq0fex9Hk4XLepPhFdt_27KCQn6_2HpcsZcjDq_6AGpNRHUwsvmorDVWkLFK-H0Yxm-WMmmwC_NJTSPRWZHl5RHwRoPi0IrIniFbnw_uuIxdqfCRIp1HNg0nhzEsQ5YUMmMdBDqgngNgcINmwj8BaOYZYfY5yq89J9j_2jh6hbWZsCphYZuyIkzp8gWiATvyl0L2PidHLGHdyC9-WGgQik_v6uJppnj5BY6LA1Q9Y_sv6viVdMtOZwdRdEk3x4JTmaOqU-dGHQ8k27ivZTZQ-KfC9rmAzX3iqs_dNE2MU0EsghrEuDNXUanSUTa07i_JzK_5kwBJiLOYO3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=pWjrPvOq0fex9Hk4XLepPhFdt_27KCQn6_2HpcsZcjDq_6AGpNRHUwsvmorDVWkLFK-H0Yxm-WMmmwC_NJTSPRWZHl5RHwRoPi0IrIniFbnw_uuIxdqfCRIp1HNg0nhzEsQ5YUMmMdBDqgngNgcINmwj8BaOYZYfY5yq89J9j_2jh6hbWZsCphYZuyIkzp8gWiATvyl0L2PidHLGHdyC9-WGgQik_v6uJppnj5BY6LA1Q9Y_sv6viVdMtOZwdRdEk3x4JTmaOqU-dGHQ8k27ivZTZQ-KfC9rmAzX3iqs_dNE2MU0EsghrEuDNXUanSUTa07i_JzK_5kwBJiLOYO3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ3w9BUh-UBDXaqfLx7edsYAcEU_-GGPrKWyCTcrNFLZBvqHC8NOtS3P6OnE9j0kawBtLgUGTc1dtNvRnKNv2t6Srw4BOU3zJK6bAWQCbEqC-dEq-MwQlxciIGHJjYxt5QANrdbnXnjdrdBZisppsyP6yW3KqIF88AYkhWSYh8DFu6vUpiqiVsxis7KY0zihb1n9w8PsSXmFlsfT9SCk5HlfHNsRIi_mHbVkwn2_W4JT0h9gW8znCF45YgSY3jaikfSXHBLVSc158iPh0d94XsEEJ4xOfSvzgpD0ktrfQccSGkqEFDVRLANCAXYA7SoaTkYFa-mH4696iwOTr_w9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDM1qHFpDPCkKom8Nqdpq76Ue-7I-7oe9I_ETE6eNibXeXUBynKvPIWzXW7yhkz-FhYfdCS4CahQlDhWVUzR3ucNvc_zsVgLZk_TyCr-kDzjRU_0A5AvIfiSywgWeXRFQ7xSOJX2JmwCAdKEgIafbtqCv2gI4qYCmQBlFsYKPm_snNX0LnJfmF4qR9PitWMhYr9P1txziMdKe5wQdi_KHOBkMrLxvze8NpzwmwmOzBxjw12sbSPqrRrE6ZeZ7rueYAeWO3kRBwHEP93Jxwxaol2nqYM1fQZfnCA8N4y1AbN3mjnoWlOJ0fLO5Mv6vzww37D0LR74EJ5IWzcGhVt3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmqyM9tUXxh6vCXtINYY9CL9pHB3yYlsshRn4Oc99ye9Ty-9oNenBGu1rtCFnPzcCA_4mN0pSo-deYoS2s8mgjQ-iTIQgYR_OaOXBNrOZQiUwSqO_ZQwydoUgyfjaCSuzwPWSWHO_WyeFC0TEtqAvDabT7ATY5-t7IVMtpmtzl9eHeyXGqY2ZW7jP3nNnR-F0yRUMW0MoImyElxfeL7-oAx8n6PmvUb8GrANnZ0kM-Peno-EYDEl3xl5l0unckPJeZL5wKzW_lXY-9Z4e6kpVH1YOumxpETOtVC5egqYS5DvmfwFCou93FuME-sFobKWTgMHWSs3sxG8D7Tqb7S8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1v-K11Y9gO5dKBOsu_fk64UBtk7Sj19vRNdWrCVDzOYZfO0IytaS0frztHtvCyw_oZ_2g76ZGL35rZNosr0yRjnRx-XQ4Kqbyeu3bJi9SSPvyFRqj-jiJwQgapw2hW-U65VgNUxt0bccBtKOT9xRzbRCcwprCtNet2EW1miVcvMyUFiCePHrNg6WA71l651ctXZ_hWqdNtn9PvEnE6crHZUNrE0x5BLo2C7ylHyyKdj9-JwTIgBzIErs-xKWWbs46Ojn7uWbuGpHS0dPNZZ-0prsj3fNyPslNFMJMiXSNakufgoAg8qCsZqGFBVlv8ozmXEqMNh2qv9mf-3BM91LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=r_hPjzWW9KjrvcPRjDI321DfnAxaQOOYCsG4pXLJfwm0m8audq83K8YK-8k7_eGguQY11DS9G0p4CIyj3bLyrMFgCZ7clFsuCE3S5lm2wJI2gpTNA76FAiDWUqeRewBgyCbIDHYRMNq-OXf_DCI6tjJxjqxiQzwCUaV1Ap3nBuUt9p9TpciD5ksTfYGy0nQ2IMBYYgBN9tZ4KziwjDpw4yjMd2bRNvUiqD8kUISFK0tB98u1PNXqL-l3I0_ko_sh6IxzCoj4uNwTMEabDMhL3tvC57HdrlMScblfuRBIl8oGFbmxGhEcUQBXqSoWz5cV23cBmfZP76iymxXfWd-Z5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=r_hPjzWW9KjrvcPRjDI321DfnAxaQOOYCsG4pXLJfwm0m8audq83K8YK-8k7_eGguQY11DS9G0p4CIyj3bLyrMFgCZ7clFsuCE3S5lm2wJI2gpTNA76FAiDWUqeRewBgyCbIDHYRMNq-OXf_DCI6tjJxjqxiQzwCUaV1Ap3nBuUt9p9TpciD5ksTfYGy0nQ2IMBYYgBN9tZ4KziwjDpw4yjMd2bRNvUiqD8kUISFK0tB98u1PNXqL-l3I0_ko_sh6IxzCoj4uNwTMEabDMhL3tvC57HdrlMScblfuRBIl8oGFbmxGhEcUQBXqSoWz5cV23cBmfZP76iymxXfWd-Z5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKMYR0RnQU_AJeZUmydZxDBMI9eXdttcbmtiPgwWPMQPY4pOOLziSEsGLPX_mI58P9a7HDWtPLDjaeHPUDuTEgR55zg3joBefI_r7GRB5QDRcKJPJLzf22ndYbpnOi2TfUkwggH5BVNKmEFqQij5MFylDqGmveB-GRh8hOmHzYVGVTtQG6lbgKPFGQdKFBrDnR-f5ULyDp1HKQq8LgOCjBbnpI4fLD1ME8cn21W_J6E6NAoGMx3awTCZCIAmlCNzAr9EsVwoMRwhSEQ2bumAidPHuRs-jiM_r_rQluCYNI9NfnIVct-fxQ-icVq5OSKQhc13WZlUTZKUqLXQRuX7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyWYfQNbY0z_Po0K-HBUiGU2QbQpF_gCjQmU_7IFZD9p9vVncWMkqMIeWQ04EWlHamL0B3XrS7ZWCZrSnx8cjIVYwjqDAP72k0XzFeTNBVZkdkStmn4thkoMIChi3h0KFKJ3IuVOvq8AHBThEdMvl_jreayIkU7ZT_HY4dvJZLIjcHhn0KNY0sXUJEv78gxkWs2jyFySLfYJ4zRYOEL2iPkBXMEmMkx22T-pl08B9KimlpHy-m5rFfprVorzQA__HhTBlVfvGiMOFFbCQYiIAia4DobNxvFSBat_KzTFp0qNHUNM1LUP-Urlaek938xfzvVqdvL_36P0Ks0n6Wv9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEOdVAw6OeJ6kE8kTt43bvlvMkAVHIbGLZHHCCloYkHPaj0gD4Wqry-zrlr0fAthB3bb6y2xdbQSqm_LPRu8KV8kFBwRPAM6earsiDNisIiZlmNvQUrewGvQm7ynxJPn94BTtx00U3x3WSuP-8dfHcmjOM0fgN561JcQSdFUp1iaR2C9kXaaes3i3qDXOHOYZ58WRpcWemqkUluLCMaBb-58LckulvkJ4AplFMOef7-eyH0U3q5GbU_6M-gxsDqPiodgR7xl4qKajCmz-l-TirUHhgB5uLRxv-rhM-dTB0noCWWWooZti-m7uXvss90dvuQwrm3-yCtgXMEg5oLCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9DEf0kKTjQf4-RMhKibiSOONaQAbUJ-eKLmbYK6Y18zwbt0LLDyovf7xcYjDfL6VcXdvWpPgNoi544VLIJbXhID7G6YIfUG_22hwWUN0jVmcXPM2BjKn7QBfI1Bw9A7e6TACJsfGoBTWk12L-GhEHXN8zwmn_MKxM0rx_FjNSgPoTibklfvkfa7I4zvxrnsNPhAHoFc60fMKBpD9aclwTNdmJK4P1DFjlgGUOZQAeXmXR9_gHjcKGkH4r9CrH0Mmg4UXPBJywXS_O6T_bAanWWRe0t33IzUGa6UMoM-B8YONVhI-A5DET83JHioq_kT5f93A9BSgseA6Y4Ph-X1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=q-Cjv8fjioDtYYJCZSeMwDxdrDMGSHMzYZLoqkl_8-GzoXcXnecl8quSfoPvr8ByYPjv7VEd_s98781fJr07w-Ci9s9pGW-QdTY4qOw2ZBTC6swdAu-XBTXlYmeYq96-WlOMgwecdJfy0Db83lErFRhSZplJ5Qu_7YApbPH-NVvkaLEtRyBKdnPpveSmctzk4ZhVPCUPH0gVOjdPkEc8wG9y9_dltHJLNCj8uSBlSAjX5ZUrUQAd7i2LH6_nOjh5vKw8sYMr25i_B_2mCJ718yGVAuWct4LH-x0_H1BHD_OoTPWVTAixi5N8qBzplbGNWSuFU3GcQqpNQAAYWYzg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=q-Cjv8fjioDtYYJCZSeMwDxdrDMGSHMzYZLoqkl_8-GzoXcXnecl8quSfoPvr8ByYPjv7VEd_s98781fJr07w-Ci9s9pGW-QdTY4qOw2ZBTC6swdAu-XBTXlYmeYq96-WlOMgwecdJfy0Db83lErFRhSZplJ5Qu_7YApbPH-NVvkaLEtRyBKdnPpveSmctzk4ZhVPCUPH0gVOjdPkEc8wG9y9_dltHJLNCj8uSBlSAjX5ZUrUQAd7i2LH6_nOjh5vKw8sYMr25i_B_2mCJ718yGVAuWct4LH-x0_H1BHD_OoTPWVTAixi5N8qBzplbGNWSuFU3GcQqpNQAAYWYzg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=r38-62BC1_Jp-eARDIQ6KoeNsmQg7uRwvq5pWdapE9SC3q42Q0BLfJy9Y6mqqTCu9tUGVTQHgH04tiCcO_GQE5mRy7TTFqf0MfIvCuCy7w5IjoFwQsB-zdfWE_r3QuBGjYbmpraH3YURv-TFDmrEZrQjktuELzxK2jOjAqyOLwD-GziGZE0sR7qjopLQ9lHmI7iRZGE2HXpQFc_zEMyaLlSYkQB9lKqAImmXH9BkeAe3fdNzAXOM6XAnpkF4uoCgA8cTK6M9wjMZOSn4Z6PSuJ-6mrchRfG9ToBzQvueDJrr0RW7Qtl52IimYTPXo3dr-Du-T6k8Yu0Y1dF5WlcuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=r38-62BC1_Jp-eARDIQ6KoeNsmQg7uRwvq5pWdapE9SC3q42Q0BLfJy9Y6mqqTCu9tUGVTQHgH04tiCcO_GQE5mRy7TTFqf0MfIvCuCy7w5IjoFwQsB-zdfWE_r3QuBGjYbmpraH3YURv-TFDmrEZrQjktuELzxK2jOjAqyOLwD-GziGZE0sR7qjopLQ9lHmI7iRZGE2HXpQFc_zEMyaLlSYkQB9lKqAImmXH9BkeAe3fdNzAXOM6XAnpkF4uoCgA8cTK6M9wjMZOSn4Z6PSuJ-6mrchRfG9ToBzQvueDJrr0RW7Qtl52IimYTPXo3dr-Du-T6k8Yu0Y1dF5WlcuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdFY-E250XpxWieNfd-G6E9jfCD2chXAn54Wl471C9QmImcMvzS7vIT0hgsdDQrT46Kjoc88Ao3VlUFZL6fYx4yS3j6WoziODzeJ_hnb2WxtWEMqy_v5OHnv_7Hirf9S5BSMEtokhzhyt89BBUwLKVF8QaOUyKymHXnvKfLf1rWgkpY_vH5LKr6sIeIoID3UWftbbGrCxQ_rMEo5XyIdHxETfqrqjoapesP2NOfhRNLYTsL_jswK1avjvQPWkJyAIlFRMy-C0nHHi0jgyAbtiObPbTH76RDG62Kz3m7QYy5M78NS-_zgpaaNBR1p0N_llPSlIab-7omTmuVC6Mosxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IEGjCtzNT5tj2BGOITbT3R8kJPpaKs61yJBDSkI1MdvlWni9HdqyhyP5farJLE6CsJdJyrgzKjsXFOubpvt3Pp0HhXLZjpeZHSoH099pK_wf1PJeBpEvvvMM-HyCWvdzlhF8vqP5KjNKHYp1Vi05ML_Cp52oTvHH30a9IWLoyve__SuRiyVHBkDK803INj2oHc2dn6gt-eJJMc8KzMoZk64CizMsLJOGzF7OIzcwzPiFd1fUhk5T7htAclFvrUkpclY3k_EpnFaMygSTcbw_MFmDZN9Azj_6-vTMAG6Kan0ZKNZ4CfwpU3Td5QnDI8-GVfWMLTFUw3mCkyfotuo9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=IEGjCtzNT5tj2BGOITbT3R8kJPpaKs61yJBDSkI1MdvlWni9HdqyhyP5farJLE6CsJdJyrgzKjsXFOubpvt3Pp0HhXLZjpeZHSoH099pK_wf1PJeBpEvvvMM-HyCWvdzlhF8vqP5KjNKHYp1Vi05ML_Cp52oTvHH30a9IWLoyve__SuRiyVHBkDK803INj2oHc2dn6gt-eJJMc8KzMoZk64CizMsLJOGzF7OIzcwzPiFd1fUhk5T7htAclFvrUkpclY3k_EpnFaMygSTcbw_MFmDZN9Azj_6-vTMAG6Kan0ZKNZ4CfwpU3Td5QnDI8-GVfWMLTFUw3mCkyfotuo9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3ku1t2oU26QG88rCV6Nkf292RTI2YsC5CRiSXZU6rEgh3RJJcuIMNxrmIJq_HR4dAQjDl-VJASXyCPCM5qduYX4Je6Id_gJbjSB-uajNKYsrAtb2gYvvYzmc1T2BANrnIhShJC31khpyJQTtZaFyeY1vZ4mC719SXCuJMJ1Ln2XszeL4IupM12JVSa5RcZP9YXJ_4r-NeSuqs92xzmbhxDfqlROVxf4d8Z0AV0jL2ReW8derXMoVk39eiSIRjYerFxpCeAGfQkjPdNuRWeLkPEIxUP_6Cl0IGVD3zGle19jeSf7jO1NW97uLc5JdU07bgbbd0qwjznAURq_vBH5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zpn2D9aQ0tTBBxVbBSiAkTyHOsJchXdbeOKfFggi_rq4aVIYJWBvRtAffnMwgEF-1oqQOxo1SYhovSkFnyZPC7tIKNeY4Gjb7AQQkLZ_w4nQzQ9hc5usmKK1dAYwra7qTab-mmpYO_XMN41Hm6pliVSKq3wg-dDAVMd0rH79OJZsgNHKzt9G6lhf19OBGgcRfYZC2LE7Mm6nDCb7sXkup5CRcZJj32lIvFZqoPF9xHzdULDI10JePYcnUDVGIRPFZQAov5df-Z4HAaG9wX6XSlzV83Y_AKlwkdR7Tjgzglfzz9aDRAedg7KmstLTehkBzRRdJXvgQ5nYYMma4FIf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=bMBtnidB4sPdUnMC5jYT41rH9yASbT-kqTtkl-KbwbvVtukrbw9IX7QRJWj3SnqpHrZfyGsgeGDpvM-kFbe6CqvT0_0aSwWU1DrAmwwujp1JyyfQUZ6JULRnqRVbnEoq--yEyAHdJBxlnOAwMNMAYqPhHdWOVhVs2KyS9eRI8rmlKTfOEp5y8DKjmcDFYPGcqCIEZsldYQcH-jsrMp6SPKhaH69YcBkJmY2i1hqX9oIWaFoa913s4uo16wiu3jHjvGkuGqzVfZkRBkMWaXbBs07sBybK7IveraQ4qFrv3V6Nm_LBGBmHYFLf6CFzJPOkh9uYndy_HJ6y9whvhc_ASg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=bMBtnidB4sPdUnMC5jYT41rH9yASbT-kqTtkl-KbwbvVtukrbw9IX7QRJWj3SnqpHrZfyGsgeGDpvM-kFbe6CqvT0_0aSwWU1DrAmwwujp1JyyfQUZ6JULRnqRVbnEoq--yEyAHdJBxlnOAwMNMAYqPhHdWOVhVs2KyS9eRI8rmlKTfOEp5y8DKjmcDFYPGcqCIEZsldYQcH-jsrMp6SPKhaH69YcBkJmY2i1hqX9oIWaFoa913s4uo16wiu3jHjvGkuGqzVfZkRBkMWaXbBs07sBybK7IveraQ4qFrv3V6Nm_LBGBmHYFLf6CFzJPOkh9uYndy_HJ6y9whvhc_ASg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=J_UUBPK0hg6jqMcA0mx1QeCIfkaSOYcduvEkcMhohgllZ3dHGKBU5IIMXgqwbxZyJNsW5OuqnodDF0GLToCiuKpd8Lv2-aa8pDijlrXc1Xn8JA4wRO8870ogX4v7MKTCADXEm2yCN8wzmuzNBT8gYlhf-GC98Jc57Rtl7U13UnC99ldizms92xtSDO2-vQlb6HRrgnsLKI6Tew4UsuorKMpLan-HMQt7oy3E6W6XOWetVHuLqJaYE6VfrXfMEholYjHvy6wpNuT2ZlSYhZDxxc_EFMdMkDFF_lCtjKLP2Go7GtbkMXJaURvaPyVZZhndlZAaN72kBNZ2PvZu-q9sKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=J_UUBPK0hg6jqMcA0mx1QeCIfkaSOYcduvEkcMhohgllZ3dHGKBU5IIMXgqwbxZyJNsW5OuqnodDF0GLToCiuKpd8Lv2-aa8pDijlrXc1Xn8JA4wRO8870ogX4v7MKTCADXEm2yCN8wzmuzNBT8gYlhf-GC98Jc57Rtl7U13UnC99ldizms92xtSDO2-vQlb6HRrgnsLKI6Tew4UsuorKMpLan-HMQt7oy3E6W6XOWetVHuLqJaYE6VfrXfMEholYjHvy6wpNuT2ZlSYhZDxxc_EFMdMkDFF_lCtjKLP2Go7GtbkMXJaURvaPyVZZhndlZAaN72kBNZ2PvZu-q9sKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=tqB_yEl7VCbC5SJ_1jFhmjswabomMczOI7tefr2vYaKnZITnmULfI2nStKnYz_hoSy3xsLqw97qz46cWWLhTJQz69Vp5TrLmQz1MRE9bV5T4zg5zV6jkxE515VU-TQtVZyFq1S6quaSi3ekTGl_dPOjn7Ng811YG3Sfutm_WzMbjn7NVflQ2OFCwWseKcsy6Oiof290-0ubLJSROzQOEiJKvMVyEhrEneQ6gsg-nKZgBtymmue-6z9WF7z2Xcfztnzxgt-TuHUT0e4wtrLHgliy7yZCAdkNTdLjcbD_FDFMLfMtzmaMBznCc_wXjFtvEOH1HHRHPViHSxN5xoOX7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=tqB_yEl7VCbC5SJ_1jFhmjswabomMczOI7tefr2vYaKnZITnmULfI2nStKnYz_hoSy3xsLqw97qz46cWWLhTJQz69Vp5TrLmQz1MRE9bV5T4zg5zV6jkxE515VU-TQtVZyFq1S6quaSi3ekTGl_dPOjn7Ng811YG3Sfutm_WzMbjn7NVflQ2OFCwWseKcsy6Oiof290-0ubLJSROzQOEiJKvMVyEhrEneQ6gsg-nKZgBtymmue-6z9WF7z2Xcfztnzxgt-TuHUT0e4wtrLHgliy7yZCAdkNTdLjcbD_FDFMLfMtzmaMBznCc_wXjFtvEOH1HHRHPViHSxN5xoOX7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur-ug5y-XO6jGh9jh27MYhKosS5XwudzqiSZG7PpQeQezF_PYGjqU8uPFtrCWU4e6Kbhsq_hgvB9UgIzpAoLCrELWzzWSNfszMJuK8cSMxvxSOpACGho-e8RjMtnyhkZwyILfy9TVuVpIVlWJgIxMf_zJp1Z6T7UqKcTDjOuzz1jh3AT-5LLLAA47CKTpdJhiB-MQ0ZdRQuDlMs2GURmovhydiskYTZ-67ceekLFAvyEg-mnpsP-5bvfmeUmpMQ_b02gk3CVfpUhk2J09eUeu4fgu_pG1FspJgY86Ku0GuV8bXsutfZNlau_9Kp689lZNQsSWI-FefsX5iIkACl5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZtviodgU5TKrKm9YZlfX-UImH5jLh0vbiz53BWlJTf1on6vb5ccYQmw5uA9JMf3KfR0avq2U2hteltUrW10kUEBH6NygKg5kjWLDiN2a9w-BYMJVsttoex9oaJiBDQuv6mdDK6C2ecBHBa1pdaBJJ6JcX-o8p_O0afm-L3-sIMlnpyEiQnIaww2pTQ13pE8h6pjoXggGDSYFmoxpx2MGYW47Mm2Gqux8UkvSYOaU-0w6pqqBTNjJjw9gFaS5kPgUX1H0hEB-lt9twxdoL0pnosf4OSpEUlFZI7TDGh1glhDpxsz9yWDw1_0V_B0JcwYXgpj7_R-B9P3hidnu7Orqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=UHQkNc6MO3ToJQ7UIYcmNYK85k_r5H4eDsMIbMwkP86YZ0VdQW2tqaqMHU-yMwpKzWtp1G1bVs3c9DfyrlHu0HR51S8_6uPoPn8LB8nt7009tzy8oS6q7qtC2HqWCDZWm97yc6ploIBYn60pErcmNk57iyGEF24lvqE80KbcQn-7sq7_87nqsqbdClbu8EXze4lL3mJD3Gm6iTzyX7fEjwes5VgQ7ZZ7rGl_To8ltx216wBIQzXmR_vxecBvacEz6wFE46jKd6iK7Eco2pNpyP6OhpEYySSMewvd7j8okfO1iCuVeObXtY6_ndtspG578J-e44hwU2TDmwXOjM_91SB2rO948aRfjgtosm_HUnvdhC_rWjFBNQSyfOUqUD99MnpcbGoUmdZWF1wsNAVnMw3mwJ3GDPTANweLPcWhfkhmz5KPLgt4NLF-_3j4lEgMOn7YiDXrTzwdVBTEoIJndqXvuLmNk8o-LW16upu7NpoXxpQmIojtrazJaa__UA7E3YSK069ea-3yP51ZSdN6pFnIteaS_MwujyeckqYB50h16RuAk3nnoCHrf_RfIKZPNiGKXmM6w3d3FL-pwTkHFMNxl_olIDYc5cb3-omUwYgV-XcT9-dB6VbOYqiML0JqPlzmPGI-uN9P7ruVchsB7_6Uv4WVEcA_-QPcFsn84iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=UHQkNc6MO3ToJQ7UIYcmNYK85k_r5H4eDsMIbMwkP86YZ0VdQW2tqaqMHU-yMwpKzWtp1G1bVs3c9DfyrlHu0HR51S8_6uPoPn8LB8nt7009tzy8oS6q7qtC2HqWCDZWm97yc6ploIBYn60pErcmNk57iyGEF24lvqE80KbcQn-7sq7_87nqsqbdClbu8EXze4lL3mJD3Gm6iTzyX7fEjwes5VgQ7ZZ7rGl_To8ltx216wBIQzXmR_vxecBvacEz6wFE46jKd6iK7Eco2pNpyP6OhpEYySSMewvd7j8okfO1iCuVeObXtY6_ndtspG578J-e44hwU2TDmwXOjM_91SB2rO948aRfjgtosm_HUnvdhC_rWjFBNQSyfOUqUD99MnpcbGoUmdZWF1wsNAVnMw3mwJ3GDPTANweLPcWhfkhmz5KPLgt4NLF-_3j4lEgMOn7YiDXrTzwdVBTEoIJndqXvuLmNk8o-LW16upu7NpoXxpQmIojtrazJaa__UA7E3YSK069ea-3yP51ZSdN6pFnIteaS_MwujyeckqYB50h16RuAk3nnoCHrf_RfIKZPNiGKXmM6w3d3FL-pwTkHFMNxl_olIDYc5cb3-omUwYgV-XcT9-dB6VbOYqiML0JqPlzmPGI-uN9P7ruVchsB7_6Uv4WVEcA_-QPcFsn84iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IerZpVqzH4IDd7PLxggyrx07Z2EfXY05AH8mO-jA4KNjbgRYkzrZabfv0_MsqQrM73J1aubFEjK2-haKpL_4j-lOrrRYEpH78FvsGaX3dU7V-xoho_YQ-51Nra-pO8DiDnUPgf4JEeg9oVMWnwSudE5jZPQW9W_F1orp90v5p_KvGxh2ZewdCSwMxtn7ymjyUoa8NmMOSKlffb9um3nI0WYYGeEZj7ykt5FPMNr-ogDmAyPZmUCYNtlkaZAs2IG4H8TtECUGn_EmBMlmdmU4viN-Iss2kTFF54NC2QtT3cDyiHere4h30v2g8b6B9fHzeqdjRqJOObkdLWodxJ2_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=EWMmjeHCpjM1h_tk02U2b0Xfv4Xx1ngg05c8I8k6ceLJ9paHybm3vooG3UglnqJezSaaXAMqc9K_EX174wmWC2HXF2LWgagXN7eCdHURCzqeKhDG3chhTlhlKZv2q6Nah6oyxQhsP3-b47rhE_ZJLiWoK1ZvozI4NRJCGJGyX_I2Ewe16auA92tY7mZNtSMRrskp4mf4ThuWiHkz8xPTUae8MuDjXbHOvTts2e9SMJkK6DbbPDfZLaDZiJO3QUD6J14AdFbHD0rHQ2tczVFQLqSI9hOORvtOlv0tLckI2hpiGmBe5LCmWX4viYF1kvn8Bu8xqC4qXVMiNNWUR2233lt9Mw3Uk-Yf8BbTWHcVOnm3VHw4d5JTdfsFPTNsLtfUwE5uGaR-cCL0FvzfA51yBxbVUw4Fanf30bcfvuNPTA5-p7YSLTySNvzToiw2I6mHRrwI_rUK2ldjpspNbq7OTq3rg1miMPG8uJjWR5IAQN2xHyDcdoL83YcEcIRUF2tLz0BFayLGT49IMxtCRW7PDtF_EQZ0nfTI7MYj5bamcADIyrsg37AtwAtwVEGHzXw368P4O7uB_Km9ZxPcOqNVgqLZg3zlkRCoATDFnqERVlIyFz1oQAIbak1J2XBMklJ71bGKBy4fgTdrCkNhCn4UJLBTOqdhPyYR_saKJSPMrm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=EWMmjeHCpjM1h_tk02U2b0Xfv4Xx1ngg05c8I8k6ceLJ9paHybm3vooG3UglnqJezSaaXAMqc9K_EX174wmWC2HXF2LWgagXN7eCdHURCzqeKhDG3chhTlhlKZv2q6Nah6oyxQhsP3-b47rhE_ZJLiWoK1ZvozI4NRJCGJGyX_I2Ewe16auA92tY7mZNtSMRrskp4mf4ThuWiHkz8xPTUae8MuDjXbHOvTts2e9SMJkK6DbbPDfZLaDZiJO3QUD6J14AdFbHD0rHQ2tczVFQLqSI9hOORvtOlv0tLckI2hpiGmBe5LCmWX4viYF1kvn8Bu8xqC4qXVMiNNWUR2233lt9Mw3Uk-Yf8BbTWHcVOnm3VHw4d5JTdfsFPTNsLtfUwE5uGaR-cCL0FvzfA51yBxbVUw4Fanf30bcfvuNPTA5-p7YSLTySNvzToiw2I6mHRrwI_rUK2ldjpspNbq7OTq3rg1miMPG8uJjWR5IAQN2xHyDcdoL83YcEcIRUF2tLz0BFayLGT49IMxtCRW7PDtF_EQZ0nfTI7MYj5bamcADIyrsg37AtwAtwVEGHzXw368P4O7uB_Km9ZxPcOqNVgqLZg3zlkRCoATDFnqERVlIyFz1oQAIbak1J2XBMklJ71bGKBy4fgTdrCkNhCn4UJLBTOqdhPyYR_saKJSPMrm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJQupqdJHUP0_FDK5URg7vlZM5AOQc87KJPv5sfCBc7TlxXGKJuS-z0ExBdhgjiPl1zvGnEqJhp4LErrNgNGV9u_L8Bf_x_BxS_wPkpeb2FbraI-AQQf62_4PCBhIWCAu_QPMvodt6AJ6yq-ZSA1QkUrmZrFrm9rS9fTsrhNVjxKHggCus_f9PI3knP8IQ1sGc6gtDordNSzAC-_qQQb49L5bJd4lEEqz39XARygFSgsuuAMvuEZ8l-fhsddt9k5U4xBIbvClT6VMpyjFFbh8ryd13RduHUcE397GKxiv5RxyY2MsV00IaGyaaO52qdZKx6SO4TuVy-WvYSDhb6kqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Izgy86ffRHd6QAtbcVJjOv4YAMaldh8_zcWa73sCfErznAubj2d35gYc3yUPPrOiM8P4dDFbF44JUMO4JALFDl8V0pll2D1msD4NdLT1o87iXaKbdC4RnEpMTaGamGuTaXuiBhlbIk_tCe8NXMT1puqiLEiH3QrT7epjh5KooSJEjskE7OT-Ny6Vty-wyR1UcB4tIC1fRK087fMxz9U3vblOIKpHu5nEqLrdz8vqWeNLCo9_YJ-F4qEA9lkOakl0imDPdcA5QAQuVGKrX4Fn7KekQeLSuj4HL9617cpHWag0KUMRXSgdgDlWRoI8ixWVN_PyOiGEOmjbPZxfQAWBaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdJjcZX9VMrChrNU-YTZUdWZH-na8CICdzTrrI8iCzGbSyt8vuV5SdlqLwAHJGKGdY7W6x85grgqrC4rRRC-VqaGWTwyASmMu_jPy6gYI7M8XKJR-SyNlYi11oFmvO9IuzBGrYgM1ZmLPazG94qP_Ma_uq0yl9M7VxKTd8xx5ncH7YvfPsowKadarye5tjAAwxZH5qgjf1kd5N9QdBYWt2xdA37A30Qm-Hnb6lx9qYefK1-iIcOOOz04fTm1W20071J26v5zKe0Hqy1Yey75HeBce0Ab7siFy4_MrttsIS_2bFyxKHKNvFhsWSMUnr01HD5vkImDWqPG5ak_LbMisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBTqotW9jGA1o_08WqYz1_5bpalXGnWZusR_I2Gp-QpcaMOfxvbME44Dpsd38p-Xn5G2hgmS1PXzbNldmR1dmpp_rLWDzbDvssxV5dnS2bv2_QQzL8NxlCyqGsw5ROo5h9YVhgAvshaGgLjcfSQ-Nr0oWudl7F-9uKAOopfL-Z1w3OPFqEun9UtSZcKPSC4OSuIzXNpD9gDo3z1FcfTwiq4Kx_HYus6xieykHExNOJQUvDP66nfLUwA2Q5O0RrGGiPj3Ixh7JqfrlPlUd5W6jnb12miWrpE56uFp5gdsOc4gvxzPdiQJHE4gfWmp5Dug7f7n79xf4tGYaHWbvP6iWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncppJaHXg572elgY0wFWHjTI9_6nSrRDamvo2VmTTLB5Akq1uqh55Yy6j1PDP6Uw3CMpE9rjtb8dHClpoYOwf6wHfnt0tvjUYYB_F9-Gy6RzWHL-cUqsPTeLAlGfD67ZuCeRq0YxFon743dQecU5s4BuZy__shp1b4pCIgkSiNqBcP9NM2_sG8RdF63dhEc-orTzA7FMMZdKf2GXZfFmPU07fLSfLCR4ybok3jAk7bG9bNyr58cMvReoAgQCSoHZfQmhA6W0lpAI4XzJDVZNmFLHqziTBlWLH4GvH0TcHB8jortekoWd6gEBvZ7lg3SUPj24ZseRUnElfphOjCVghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=parB_eb6Vtbx0Zq07FQ8oAGcObpLYm8Z26vhwAXr2cU_Mv0ySLoHIxjrxdmgVIPFN7WjW0mP6iYjFr-oCFNjPKVUnQ0nyDw5LMOJNf1w_zz9h54_kM2mx_AXZ2qgTYx6e7jPNBWiftOp14B68SpOWo2BiDYu12QPfHpQk_Txndr96AgbQCl7E9H3JTjtwUm92qm8XwKhVLhbgGt-pqQQ8IO6VVi-9xtvW8QSM-POpEMMZ_4HpTyxxAsBwqyzH0VzOOUy5I4ODuJQBUPqh10whlGCAxZw6CyM2169TrE1uMV70urJkZ86T0NysYib8HtJ5e6cq4DFSl5GfVNCagaBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=parB_eb6Vtbx0Zq07FQ8oAGcObpLYm8Z26vhwAXr2cU_Mv0ySLoHIxjrxdmgVIPFN7WjW0mP6iYjFr-oCFNjPKVUnQ0nyDw5LMOJNf1w_zz9h54_kM2mx_AXZ2qgTYx6e7jPNBWiftOp14B68SpOWo2BiDYu12QPfHpQk_Txndr96AgbQCl7E9H3JTjtwUm92qm8XwKhVLhbgGt-pqQQ8IO6VVi-9xtvW8QSM-POpEMMZ_4HpTyxxAsBwqyzH0VzOOUy5I4ODuJQBUPqh10whlGCAxZw6CyM2169TrE1uMV70urJkZ86T0NysYib8HtJ5e6cq4DFSl5GfVNCagaBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lav89T_4d5MmpKZAw4uXSPmR2uFEI7p1FCUY6cyi-7Sp0CUTe4IqCKiRMp_CwaAVnGFef3AScZSXJiU6euhNIls1TeN7HGE6Cx0eU4-xaqmEZtKX97BZGdzZOtCfo6LKT5eEwqhlGFJlRbR14E27yw9IB8KyL5Ah0XxiLyLrbGwdjpyKiKyH-rNj59Pm-ZNmaQwwaJjsBbRKeqDpwncgIhEfG5LnasHTmCUo6u2RIau3d60c00lE2yqxA18Zfi6LGq6xnhHoo2B1opXM9AR5nNO1pCAxT82V2MBT5VGw7A-bKAldjUL7Q76VcCmDfpF5TN-4i2YZkJVdxCgSFe-_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVeXNxlxP7vTSF_blXYQSDT_JqU260L7MzTIx4xpAGyqHWakAU4Dm0ANOo1vwogIv0gXdCs2Y4zngAQ8i6mw54Zxjl-ged9uGcouGiXxUVxqJzKNU8Rn477OpQpuJG3NRmVBBBQOSPAkSp66AcX-xCv1rPQChSIOqA9eWz3UdOIn01wrwEL45NDIjaNuTnS3RdpPGKxRfrlBvYb0VjxtoHgJJK_TLB7RD90_SfLqheuCMuopFx57pxypt6gLijcp1WAASgiTaKAzDdB4GGO3P2o-0so9Z_q7SO7RFKW7MJtnqkulIg72tqms11bz0CspfaEmjN9mWUAYqNO5aWwYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
