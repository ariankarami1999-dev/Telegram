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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #100</div>
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
⚡
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠️
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
لینک:
https://github.com/meel-hd/lofi-engine
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 135 · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 326 · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 631 · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 885 · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 785 · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7lXvoSW8cS8BKbOZd5JC5MQxKyi2PuvADyO8JPB9lZbB8kfDCX1haYNd3iy7-rLkt4pYH-gHiV9ZTsWLiy4AnnPjNI1Nn8lukI8E4sYX8ZDolTZtN9vBHezShBkvNnPxvnxBFW2lKt_v19MYdhpg_1WTI6ZBs3A4eHRcED10el8AHsfxd3ldvSmBTrULIQdMrFQZ62-Fl0dYBa04W0psiycgDMvIfAcebBFr6H23CZN2UZuFEXRPSbXMLAX-SO1_5-vFTW8xcbExb_4jsKstxb6s7QEcjxZD1PHndfPtvlIiMm3UcsTe-wO3s1PwlyB5V6__3H-hA99vzj-QiEJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 726 · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsyeEhDP5Mypm90HV3nEzOPUXy7blTfEMTn1W2ZR_7_UJ__Je0IgLuHzuMcy4r8Y3h6gwliB2MBrGrOLZJOtU-RseZvogs5SkekjWFZYjij16df_B3BFWSDL0lX-EBt76N8irQesndaMi5z2EYlKGwnR8fFm6vfUI1wAh38uo71kM8uct5frnBKVn81r0K5VevXE5MqB6rSOmZTvNuMqT6X5ioGMqvIpe_zznslgAQt3Xq9KF88PRV5FUcgKl4QVMhkVVUw1FRQlIPgw7fr39xY_J2yW6Us4jhFbgNqtBVV2Dv_7QlUDYsLQ0k_G_RFINNwVFkwrqVT07Dwqb0Cqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIqZP1sQXtnS95smLdkuuJQyCyTQjMki_jmbVN7bM3SicYnWrA2diBRfVJKA36QmzWM19QBkq2JyROe-cJzenMOJS9sxpmZCbd54B5uZ1fJXPDpDQG2D2YCgvkxDDfqCfNj4lmSkrLdkDtfaWyA4b0BYS0iSauOoexf7mwURQT9FBbXrxVcjjuh7mv-8ypwRq9msOHA0wb-qWCVeNA_Nt9jxs2uKrBa3Kq67-BJDmHYC43y9E0DKPkK2Yteg3ZV7YFxsJiQYKjfQlch5gLMf_HwORk5fiGDhry5zb_gRBZTLlS1GrqcxQ88jncyc0pUTKanJD7dRmAPJmzEghcn8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMAtD47eDWpbzRla0PBqWDt1jAdrQ84F9rKait00B4luFQVM_ZEM9S7xGv6nrodvhWFrl-c-3CwCa8EyFvR_IESHuR5HDj-vpOtFoS_7tfQK2GL9GNlZMhTXjoGDtUG1FM4ITrqgTPNwD55m3imdesoZGeMGbzUoSOmc3HWHQZ4b7GOQPUtB4CAsS7v5DF0xYm4K6NalEFYvnA9JhFKrQi6WldQWtHqocWOy45a30ZSlYTqQ_O0_4YfIbvb2rdQ3DByx_jOIVCayCpLyG_Mtu2y5Y-MqLEe3UNLw6G9BXiYHrygFJ36fh4Qp9PEIbcgGylszm5-C3H6kRiIDeJd3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXWCGw0GHEQmYjNuZPoyhcbOmQ-Il-3puvm_WPhNDgczj8-ey_i3GslwEI-frujXESrjabh-E8BiHrU7ZYQhg31U83vO9_flsDYrwQTlTcmUtlvPPTKTyeJ-0hamwXxTyk0JekMW4J6Jwb108OFSu0lIsTKTryQnDoK_MwUoq4EvlIvBjI2VXskXPCSxrK8iPZl87tMazug_BZecloHVf2d5wxblg8xIjtyxnw2ae-fXwycMphX7twLVJ82SpmbkrV4n_a4QxRInA0epRpoRaXrzsut69O3j92vSp-J2iNcaio5MizNIrtehfNSl5Zb0nTDCTzbYGJyTbZ11yldosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlAsmxQYiIDv544KMCOuq_RAeQeSoV-A4i58z3Tz74pskHKcHMvbeyAeB6Q6KzmHH5BOhRLP3tf1ni-s2MG9ofOr3K4C4APa80Susc458_jJsNr7PrU_WSF2cX5YRh84WS6YEci9UUEoXf-RgI83WpNGP8yiV8g95SrxPp3wR9nz2A6do7SD8osyjViXYTm9UTzoaemIMnj3PH6qfErsGA5fFtb1bh-fCTeXhnbgmnSUSZ4q00RWRWE67zRBsdJu_NU9zKHxmendVBuixOmpdTAaRwd4sKOTlc2TcdopBGc0RGgixRCu5iR65dgYNWYV4zDhT2izlzLa8kzkGOhnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5j7TPGVQlkdR0sWXWL11dU-YvWSPuwZ4D1Lvi-WXqFZyyyUoF-CZE-ApW5FHVJTVBzmgKJ7K7tGlG4AJt7FBa6uH5oCWB-WVn6H58O7GZj_LQiE6S2dp0Vk18AkslRbFK_rJa_GA_T2I9DNOtxgtKYQR3FrjGoyYF4VO6XwVaPxzBDs_Q3Kcv4gOVUW-H_fAEAWb_IN52vjbrNdoHPXje5u5DIQf1H9GI7bPUYBuh_rFSkOfwBFv1S7Bwz9Br8fYV7SlAAhMtNOx_o9-fnoEQ4upYWVJtpBNR3NlSZqUz5ljlJ6EbC_ESJTZ-UqcgYmsza1dw2N87hcuhVJQXDReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLmD4Pu4N_br3IJ-Tl1umJXYDHqpqzhTnqvuIyPjxJcVhPexSK2YZdbLsELuNfkoMfb98umpQjWC8dryhqLlAu3Pnvf7LLJ2OzxB9FSbXkxGcGd3_z37lPokCEB42ObnaCIYXLOVpTt0DaV7OoKGQjOO_o_1kFxTk1JM9pPixE54GgSr1xGB8Tc_I_AiD1MJ62KuzNRoPMcvIbPLKkv8OMa6IYTHw-pApr2LTNyaPkqalT6V6C_caYmv0KmXHJXQPic13rPFX_Gr_z5WpKxLuuKUanu23CgqL0yt29JwgLLjLzcDoMVbsi7At_X8XSJ1h504NXm3kDjqFNQPqV9CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=GKlOVM2nNt6mK2ad4YV988lcVFgJXeMlBLa_Q4njyLVsgQfk16v_16Dh7oMzBXquvxPjGcvkQpko4VyJjpoCRYGpGDjG_GhQm14JPR1gJvTLB98TarEMkccvLL-yDOR878UrdgeyGDxvcYxF_ND-XqfzX5lBwCLT4qOlXzsPRJVvSwBsf5YtANXl89ObrAUE4TwVRKex9_QCk9MGJPeCszXqMhydNV3x0_XRdhcKbKpLPBos7w9487X3rNna0_j6dD4-8me3-TN-w-S8d-mch2-hlW35S0nyLlU71UysrEVUG_8hPY9RvMyVI-84R7ainqb1nVohEeUx1arDhG8hQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=GKlOVM2nNt6mK2ad4YV988lcVFgJXeMlBLa_Q4njyLVsgQfk16v_16Dh7oMzBXquvxPjGcvkQpko4VyJjpoCRYGpGDjG_GhQm14JPR1gJvTLB98TarEMkccvLL-yDOR878UrdgeyGDxvcYxF_ND-XqfzX5lBwCLT4qOlXzsPRJVvSwBsf5YtANXl89ObrAUE4TwVRKex9_QCk9MGJPeCszXqMhydNV3x0_XRdhcKbKpLPBos7w9487X3rNna0_j6dD4-8me3-TN-w-S8d-mch2-hlW35S0nyLlU71UysrEVUG_8hPY9RvMyVI-84R7ainqb1nVohEeUx1arDhG8hQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BywgF60VrKpsBjD2zOOaFxZ769NK7pSjqP0ffMJr56PIvV8hoOpkt1-f0J58lbRUneCyYFFAmv79EYt1WfnvjfQkE5KUrxKy6cSPNFSbhObZuPQ548CWKx4rlnyn0hcWk9BimQDEIaPhrfAMh7y0VIjFK9lb6-iU2lwknz-F3mMHuvR3VDlhUvCks1Ry0V_rQjTZzwwopLSC6dPVjvzWPCNw4m88v_IiAWMi_cI5CalELN2rnoTa-Ban4HJu-hhDt5uBihP-wqHIviHs-UbzLzHm6zwQq_uqKffE31DQuOG5IYmsugFO_CCOe3gp4BvESqB9RwDHaZqqE3OB5j6wDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI93cwGkcqpj17GqBjxyClWPeXcx0HrZdMPN5ZbtYQAeMS9XubGLSB3Leiiq4D3e75pYVPnsW4Ao2RkftmqH2myob0JVqXrUze8DYUfl3JarPKrDv-aGD_QKhbzxPEAuec-vRs4FPJW-VYUWCIN9RcMmrWW2N-uG2V-bYiCx8_3Qg2OktqFAxVpWzxaOD6OgBWmXmfMdvnRjmzoxFh-USPk8HBwX4TFrDuZ7eUnSZVxIiVhzp9B1DB07utknvqMr_J_icu6DOAEBUpFPqVmqzJzME2qeYTsa5nFlX3G6d5in9_8mIk3Cg1Crort-t-xjpXXiVjgXsrE9VP0biNP4ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uToYv30o_3oUX7iXzevMzWcOesW4z9e_tEeHQQmkK0wxANu9Rwx6Ed_K-0sywvNg1qA3dpNXw7FhGJlV4driB7qHZGKPF5i_fcgL2Cmkd1OjM2NTi_MYk66RsLOl5xwF1MOGrSwN-pgsINRZQPit48YJtMdwdWXyDcWa-4rf1wTS67llCOycMPmxMJ5XvylqW_U3qYO_D7ha-7pHqAUVtXqziGfbHuc2ZEsvtnX7qzxc_NlEtynbYSeazYDKa7D9D_gp8fEsx-VulHWUVZldxN5sNXXBFOm_oFhfkL4wFfEnfljGVBh_17JfzBnShtQm3ofJFOxuxAgKM8SCBgp22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1t8Tnv2gozF1J6PCxobcqXamtBUFZACu6OqDUJToz7USPJsRzWojJS53z8Lehc7JnVOmFLM3O8B-K0VZqEFgcUYNF6muyBU7mCk90io3Kl0oiaFLHSqzM-7L_tyJ0rk3hgQnmWvlUsUXCF_kP22MHyn4sSXNHaDuKi1O7hXPwxB-BtMqsbgZmqsVWyE1fle-jSQ6obEU6YjADOaoEXx3V2pcjcaRoIxaEYW0Ou5JYd5lCFnSB5lE_dBv8cLnEdl-zWdnaTxXfC6M6rJr26ClST9_mxOYKupbLADil2UfK1uE2Af8zZI06xzvgSnOzibCKmGWLi2HFl0tQW7AZuKBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=UV4QG1YilrR1YQOZ5Q7roL4wre3F7QxYBz5m6vsGJE2dUyH6tqoBxhgjuwkdMIaSeN55IPcLfEjmbbmpVS35IWG2CTUzk7Yv_-eMkBb6bET5Fou8nQeDGbtgN5S4jwIAEr-1IiOX7HKgEWu3qBYG8NbJZ1fcspwvKBxIe-OF5dR4iHcFwvI8LPTd0bpHNgcAEYELt6fcmSHPlEVfnln-o3-4Rw0Y4fJ58EjMP8x91gONIhdEWpDzPIGSlP82RCzwJ8Tl-uBuuBoFkkjlcP0g5RJqj4joHH3pavFuw1-wnnSBDCWsdkdLRhdZUdu4KsYy5M5QngM8emVB78zRUADnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=UV4QG1YilrR1YQOZ5Q7roL4wre3F7QxYBz5m6vsGJE2dUyH6tqoBxhgjuwkdMIaSeN55IPcLfEjmbbmpVS35IWG2CTUzk7Yv_-eMkBb6bET5Fou8nQeDGbtgN5S4jwIAEr-1IiOX7HKgEWu3qBYG8NbJZ1fcspwvKBxIe-OF5dR4iHcFwvI8LPTd0bpHNgcAEYELt6fcmSHPlEVfnln-o3-4Rw0Y4fJ58EjMP8x91gONIhdEWpDzPIGSlP82RCzwJ8Tl-uBuuBoFkkjlcP0g5RJqj4joHH3pavFuw1-wnnSBDCWsdkdLRhdZUdu4KsYy5M5QngM8emVB78zRUADnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvyE4V-9U-pej37Mlw8TSEFHCThJzwP_ACh9XKECq8fnxcB6WlNang_cEJhk01WHVb9zrZlBEXSTYxVfAK9DMGFhUo-Lhruj44a4X_WqAFs0OPB8a8omgHFkUCIt6m9aC2ocFcRY6vsQcGXWAEkGmS4RovtfL_RlOrCdj5rL8Y4C9ALgz7OJICKBEZ2RajaN0o-hEI-2s6db6-n-1kt4wOTbfcSvONaWzddrN2KQpQ7RNV31OxUcfX-bzrspsF82AxNr7r3Yc2OVYVQzWgK-dB0ZH17XQR3DDsI2kAe5hMoSLP3h5QMyY2pFm0TQQxLSb6QqaKZp9CPsFhBjlRRZ1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VViJqYZT1rXL3HMxHUMTBmV4dKC7uQkxtnYmLIJcc4gsl1M6nfAFuDifIU3dAupf_pQeL_VmoV5uXzr11XeAb67XForeZlfBveAC4ftDImxjNKfizY17OPjTbzAuKy_OUpIKiGDYHrOSSSgbrOKgrd7bebokyBoTe_9hSIrPaPTIQ0GYjQvjOmxeRWzemIMxkxWQQVokkslkjhJR7LPbnBAI6TLJcxgs8afqBpwqo8N_EXNkB4-SXXXDciIS11RO0JqnQ-n0BenL8nM48i3TPC0cAy08k3oXWI84Lz1jY2Iu_YhWzNMVlBvyPKj2jWkqKwkDLbE09ivXjS1j5CAyYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=ow0ZsJVZli428TYeYjedyy6hO0hMbHzvde6HrMsi4633f3idS4BuW8gCuqZAZ9GfXIKjz4bhvWBYdDrJT1cdBJYI49bh6AUTSfjT6flkXxhXYSIfkFePXEOdwVFMXYJnZaGjbgFF8D5hh3NfozCn0Hi2zUOHmcsXPkqcny6Qr4wP-6-UG9TgyoMZBcptnnaj90IJ_-Zy9ybFNhLl2FatvSUvpQNe1Zf7osk1O6292wm8ouGo3PKfX7NLsSCERYAqSoth6BYek4En3qETGIQGUAjc_hrsp1hWWhcXwVSFH5lGfuR-VJAkfSJRNzUCWMK6EZfOH73E1WPpElKZ-rUijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=ow0ZsJVZli428TYeYjedyy6hO0hMbHzvde6HrMsi4633f3idS4BuW8gCuqZAZ9GfXIKjz4bhvWBYdDrJT1cdBJYI49bh6AUTSfjT6flkXxhXYSIfkFePXEOdwVFMXYJnZaGjbgFF8D5hh3NfozCn0Hi2zUOHmcsXPkqcny6Qr4wP-6-UG9TgyoMZBcptnnaj90IJ_-Zy9ybFNhLl2FatvSUvpQNe1Zf7osk1O6292wm8ouGo3PKfX7NLsSCERYAqSoth6BYek4En3qETGIQGUAjc_hrsp1hWWhcXwVSFH5lGfuR-VJAkfSJRNzUCWMK6EZfOH73E1WPpElKZ-rUijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAERJjyvs6bz9g2i7DnSeohE_shh-6ezHQgnZDyiG3f40wz59P8hQOmjzfx6ltkH9217iobUin6wqkgKnSJVVhlJyrampFQmmVMr8zOOz1Zli8232k0RUeqrxYoPDUw3W4la3JTZClWK0WmBmsY3-NKNTVAH7f1n7VtX0pl_QnjWMxEkc6gae2m8qpd1fKX6xEQBenMUBXEkRkRqN-3yTWkvJJ_e0g5ibgoItF7pClY31BhWO66j5ZxY3VN0sejMUs6vYC79nH3TJ93JHIKPZJQqyG8159u1wRgdaofX_gGWiy2rNjLE-ea1IQKGb3Wcb6Z_joF9TTtXtKzGJN04-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKSQ3Hw0TAOfsd2y0AbO-c5iI0XiXXaZQCh9wnvfR_t9Q7SdNTDK8COHkuKuiuM9tzxkvCKmmGXk_UHnfpg_AZSm2vYFedUq5PSvskPitUYc1J57-ohkay4YfOSUyu_gct18jWbMQjpY_zZBOQ5C1SoRw8_m-9Qm9I24RjaTgxTZxcHYeNnq4byzEXVhd1dLuO-oa5WmrTtMqogDMFkhuZsCIfi0FiWP69sAqTwghhD0C8uN58j0pg2Z-ozdBV2kA0DdNnst9us9joLm0MRhOQyjKYWz2LC_pul-jK6TO23ikDmK0llD4azb5azKWaAMTtK9icPpWel33JI4h9Q3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzbu2iEyZCwZrwDkN6pBiqF1Jk1yHmL32tJbrqUlyS4omNPortSu0_ObwAO4x00RTc9tnjsaF3UVj_5mWRpF1MZJ1tOCctFDpXOd6AQvzz4btwHITOBfU3MZi1GclsTaY5Jf74kbvLD8NxxZb7jDKtZS1cy94inP8XQOc2scjWpKiJrbDiC6GLO6kLbOYhsw2pFP8M_XcuhZo2h0Ttxn5zlb44i3uSWRP_IFvoKI8YAkEmeVxjFqM_qRlzicA-tD1nOEQOdn-iRQZqAm5UOf1o1mFni1Y2mgoiYzHwG4iKEh0EGrDfmJaMYUGcWjMi4EV-C_Na4WTFemRCpbB4YR7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEUiHz8Fd6jdUG_ZzhlLcGViZcXCDpWnjWoPYboRRnsRQFhiuyj1f01wPE6WH5jfW73JwhXa1Zc89gkSepVFGgu4RwnxzaudqVEn6fvvtpdINspSLkUkDgA80oy31s8ZiaY03yLT5cKB2QZH9kFjbLqJSxLTe_JlNMtwBYwT5b-IRe7YMNV8OrkJJ8GswQXdsm53KE9GNb1zsTn8mJTevFOD32o5qMzja0YFvStemAKXSyz4vQy_iSmX5EHgxs5y9Op5E1uHTY-Z98BnHKWWNidnXzNjqCPrfu5fROGsuTsMtysdoV64F8vuuDflpeMdrUlQAO1YSC-bbJMBSJfbTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASeRs4i3_o6FTb0uzKRz-CKZd3zNMEFSiduGvtDophXZKTU84BtNXvu13ez0wJ5KR4-b62nIiBEdCssI3a1--HKMP5L5Dm9kEoehm1_6U3S-uiODxHJUwvEUx2c1-F1f4-x2bhzbre5N4f_LCED2kZPeXcYxeUDRkJw6clCwBHnr4Bh5g9ZSbK-ZVCCNcJ09kG8G99fW0nCqogZ-pHAM5ZqQObc9FqJUf43VRrHvff-eDb64-_Q4h5q67c-q5Nmv8cvzFJGHRywU31EmgmyA4yUiI03RuS5Wio7pFyaV8XxhMxJzEefr--8uvssI4SOzA0d1RbEnTCYChSpG-NZfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPrA31vPqEekZI0ekKP9ID2npuZf-Y41U7g_DaWnehHrUWxQLsBmLpvKkj22XJALT1_DaSfhknzMkdZOXjHWkbEJxuw2XQsi0Iah2EFzsbIq5WUo-TUnv6gaM4jFJ9wvC-CqidJsYOrAX3Zk17X3kuQYe0_6WQld-PzjxvvMUwgggDcMYwML-lOxslJsPsoOjWaEsToiu30cHu1n2q9W8liPu8npNBKFAJiaHBJ-r24lxai-7wkjtmZRNcEpPaCF5AW93YQCDYi0o1686PFLgpZqUmHTqbETVpf9fjlyVX11jfFfjKuBWNy2xiHJ53atIXYI5NAoAylqUscoXi2VdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=AlRpNOTW54y1boS7bZczGishjhZ22QaruOn1VhErrdbGxnHa1G0qp3n3LEDHtzcDEtdyRuwNpsu37XJ5EZ-A-mP6pujxB6ysUw6njwmHM-GUZbxc-bZMjB4Zxlo1c_3-yCryUjkjEouDPw2IkrUYE6IOrGSBSdBZWFrO5SOb54XuG3QsDGZenAXx343PKFom_DBvjTJTOrPVRGzztcV-Skn61kO077RaZbW_hWjhPT8LvlJ8T2uHvwj4Ed3K56DMQkJss1OVpJB7_Pyjel6yakYmFVVc3Bke2b_XOEZW4oci0sMavYF9lGTkRzBemky6VgWfK96N5lYYpx8n01SHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=AlRpNOTW54y1boS7bZczGishjhZ22QaruOn1VhErrdbGxnHa1G0qp3n3LEDHtzcDEtdyRuwNpsu37XJ5EZ-A-mP6pujxB6ysUw6njwmHM-GUZbxc-bZMjB4Zxlo1c_3-yCryUjkjEouDPw2IkrUYE6IOrGSBSdBZWFrO5SOb54XuG3QsDGZenAXx343PKFom_DBvjTJTOrPVRGzztcV-Skn61kO077RaZbW_hWjhPT8LvlJ8T2uHvwj4Ed3K56DMQkJss1OVpJB7_Pyjel6yakYmFVVc3Bke2b_XOEZW4oci0sMavYF9lGTkRzBemky6VgWfK96N5lYYpx8n01SHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUG0H1Llswf_1pQTdzLu3iBvPA4RH4oSHfgQU1G2KgDR04ed42kGvtJu9YC1HEvqy0k7GSlR5AksVcVmae0Z93T86vSHL0TpT7__9NmaRFVO6g3rkjIZPDi8sPZltVfwJ8H3nQoZFr18aERV-L47IoTTacXRuLzAAYxi5nmM8vo0j4rBnz0o7pgbVw3E1VNwTi4jgOaOyUO7Gc7u0skqLJJfwvmbCMYMbDVg4ISybCHRDvKGNMMe_hJ1UN_yV73DnB8pUUlIQJXIfA1giRns8wjB-IWro0yx6M7u_F5OsquniOMyARJS9S35Y9Y8oLydGR8-97ikYC1FvTo-ss35xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTSt_iG0emYYYYmkOB22LdQ_3vAxbVi97wn9xmPz5LR2ksQOtTghNf3Wt5_5QNdT81SoDFXFo6Q1262C-d_ChwjeJy8jUBcpIuJnOEKkzgUbCPxvniO65jfYODbH-B2Xu0AaY-7fNn8EW8Q_SycSkHS__EBFyNzD2DIeojNozsWFwkK4OKymy0mVL5Rjs2aMzbR4plHjt30qqwiXQWNkv26r6zoJVjodHyZtkRPxf8fLqa6KrtE8XvsayiUv-doxwI6a11hGNdwWGJAxZq4s3WE2Tq7v55ZjjjXev4dHL_xjp96D0Bu7bNOEamdB-11bqvYVGZYz_5_sRajSUSFzYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX2zQiniIGd3OLLRGf4z24ESCCB4fSRHeaajmySc2hyWCwf57JgftxOTfDTki6PbMvQKcQFn7l6hWU1nk6Oz_C9dS-5Eum-OP7vGkIxy3dzfCDISCr1OpPFDXOit7SFqJDfGICvmhn0ZRu-QxO8dkrTbDg9iEk7PJ7yS1ool5xQkp8bWIaPP92w-gtMKJtOan7eSXPNfQCjjJMkzY7z_uL3JalamEiP_SKeywWkOn5tSkDJDUiIfYaHsDNHxcRzf5VJRbdcqqcTgf7xT9S_IwYiBbp8PhGrC4yK1a9kWUA_51OviDcskHHoE-HXLhLm5Y8wrSWyqeS0XFHDyAcSG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDFILG-c2_nmr2O1wYtF8gGIAGk3oitkRKSp4jTpKiF4P29geDiIld-dxjR9s6c_iM6ZHpcrScwmWvR4Nhv-IUnq7ZB8byxwAv7XtNha3lAei7J843EQAcvairQOXQIkfd_nq2dmvYYbWZbKpzD-IOBEq7xvHWC_F6aoXEYSm2JoUBaaWmN8EB-LJpnXU07Ij8VYltbaY9fk2xwaf0cv5BiWUttrVgIyjFLMAGUO0BpGW20EeKz264Ct2WJ4qrC7nPIEWwNlHBvF9sq8WA5nCtsss1zO3Dt0TCLEJVUhb_K5NuwGiIuZs15oe8Ma9nnUgP_UXiigewgy0L4G3Sz-tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=u79nFa9hz6GCELU2T62WZakI2z9x2uOfiXxEG24iq_dbmdjOLpUzXWJHX7e2qKa6Q_PQJp4v3R98A3a0t3Zzq0mq14etRdW7mZmw-CkjCQ_fxKx2UVFLSeExNPkPbjLs6ddCjv2TeJZ1ixjL6b1wcXl6U1Sy4z73UyrJZn-LRWa8ryWiJS0Tqt4b-m_daWiRW3XKI8FcaSNXdfe8fEAEkPl6eullfN4YgTG-dH-jRxKGJmNAqnrF085-BnPjRLfXqBntlbyv5E-8XChlU2dwUUNn4OIh0qRDyTTNzpTRwnq1pGlZxavTeCQhWeAFM0OANYgOYQ4JX7ml5qN3vCtn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=u79nFa9hz6GCELU2T62WZakI2z9x2uOfiXxEG24iq_dbmdjOLpUzXWJHX7e2qKa6Q_PQJp4v3R98A3a0t3Zzq0mq14etRdW7mZmw-CkjCQ_fxKx2UVFLSeExNPkPbjLs6ddCjv2TeJZ1ixjL6b1wcXl6U1Sy4z73UyrJZn-LRWa8ryWiJS0Tqt4b-m_daWiRW3XKI8FcaSNXdfe8fEAEkPl6eullfN4YgTG-dH-jRxKGJmNAqnrF085-BnPjRLfXqBntlbyv5E-8XChlU2dwUUNn4OIh0qRDyTTNzpTRwnq1pGlZxavTeCQhWeAFM0OANYgOYQ4JX7ml5qN3vCtn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZrgeadre7F396tOFjMOQoPRgj-mvXEwe47pySLWiiAEDs-7At3dDxFee2NYRLxOcNtRjJLlX-p43-SCezpNIgCrK3aCyIdoNfuimqi6isR0bwT15eqB1m9SrZ9CJw1IrvLfzO1o68flfMvOCpDTc2zSGyQF5l-oaSVNrf7knmwgMB8Cv5Bm2dp5QIBjgk5A8GLX1qDQ5apcbMMFbVZstZlQnsAMiKNZcE324nVDbSiCTbV1axssdIMtUcoiEMLHoxJdY9mmcws0Ya6BprqwFKUIa4a0VrZqv3hTyO7-hhjEA7ZJiFs_wQzsY15DDN40Vh7Cmp3W-7a3LZ3R23Ew-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3cRYNYl82eNERGwYJXnefwQ8hNtFWKseZ-x57qwjpINYYXA_nqF_l-47lv7s8TdmlZrNxiGQLTCdjGNL9roCbR-b_q-oU_uNJp_KI-HmE7oPj31mC8uESX_MoU_E4ixas1gEty84gzz2pLrWJX7HL-rxYiSSWDS3MUpHyS3QcZVAj9cMMMVuLZfcIY6dxba2MbGvdXtlmoMb7bMW0m6Vg94VNRvlXzEz8bL7cbncKIlC65Lgf7iowA28vmsbZf-14bFeYyNE0cZrNM1iPvYFEKOvo60ziQH1a1fA5IBga895B_5JSQ8fjkx298tcP8K_nY-H12YVU-RKt7t_8VYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_h0XkcUWwPizqTMNhS6CJTCReBjF_KIVQT8g2lnH3V2baBpsJHb0kmpw9LNHQEg0NyKdwZ5uuDCn3rFezeCNzu3Pf9N3JBkcYVGI1AapubuKHMaPbiO5kLImveQRFw_NEj0AuhAT2hdyoUjNex9KEeM9oRNdn1z-wK2HPI-EANdj-fMNxRJe5_e1pr2cYYZjiEijhAhgid8tE7nTRqmtUlWTL-Aa-YFyBg-Spc4qRMhvsGi2UvtlH4lulCJN87iilNs7Qy2_06Dsf0xnU9BNRnOX3qN7H9r6mi5N18ToZX4Rktk4t-2OuYB3nUSSaWWfsNi2saNepjHqpPAMLfTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsWg3unAKaqkmFf9B7HUJ_a8-qvK8Je4--M9mW7EAZYRcFnzhKIoavI8Ki7g50hyDKs8aXmTUuP-lytybVO4u9smbCgct4i1hZ-WAZ8cXsvWXDctIfn2EQIcNuI8E1-dmm56zva7kTwpKwKV3IRvrv9zdOFeKO3D-J9L5dnLQ_DEy_mLBHKQ3JU5v5QsmhosorcbW67tXohWl84FTzjTvAWMm-8bkl_XgZQGK2gckWU26F2O69ASjGeh4J2fH9zMIBHuFZ0nLS58htJHzsJmfmE8xYWucBY3H1Yxt0fudaneRA_JaGr-59M5Hpc0edpMg37xschtY0knwRVLlpo8Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=avbx7KvCEQRL07njxAd2PaU76VjdV6lT5kZgtbRdsTbPb54V-qSvL3zvMgNkmOcBs9ZioRPr_SDkYz6yfQzbcxW-blos0mgt7u3-yX9YGfWx9N4K1pBjapPdkVjZimByhCJvGBAqeT3YMRVcruvFSYAlHexl-3ufUMJIIQbNsFhwBWNhYTMzXDsrL9BxjS97bIyY8BLdhobQlDcOktxgm50TND9A2wAkCy505pciOkx7FQtTkxrSEJf3rV4FvOprMXkGCIK121y907y06NaDF_Zn6GipnhIyZAksVcF7XJOi1p47OKOsHRBRG6Qiuj2JTmuPoZz8821rXzIsMQS6Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=avbx7KvCEQRL07njxAd2PaU76VjdV6lT5kZgtbRdsTbPb54V-qSvL3zvMgNkmOcBs9ZioRPr_SDkYz6yfQzbcxW-blos0mgt7u3-yX9YGfWx9N4K1pBjapPdkVjZimByhCJvGBAqeT3YMRVcruvFSYAlHexl-3ufUMJIIQbNsFhwBWNhYTMzXDsrL9BxjS97bIyY8BLdhobQlDcOktxgm50TND9A2wAkCy505pciOkx7FQtTkxrSEJf3rV4FvOprMXkGCIK121y907y06NaDF_Zn6GipnhIyZAksVcF7XJOi1p47OKOsHRBRG6Qiuj2JTmuPoZz8821rXzIsMQS6Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=G1_6h-030IHUv9f7WyClVJzMVxuxIQQqPmk-M50JVjRz2MJs2uRwt1pVaajDvlXkBlTUwRK_S2GX0X2_P5gAyAZFRFvIkmDbIyE3zYDq_sdDWm13F7OyTgiO_9IRkOclX4uyXKW1hdLpz4pmyRSdKNRv-lSAWf56Q0OJCH8jgeeCIZaZ0OUlWvXv2IqNROYgiCjebA8bAq11lBvIHeFI7o6Vynv_ZFZoQ9fN4Zo5a_eXrRKHHQGF8xTiHcMRlv09SKGTSYbdod94ohIVEMzpDn1YwiBLVZo_2bvFO6eLP9ExkIxIYGQ5s_XcrbbwPvgV0VgF60oD8CTQqlePEUITKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=G1_6h-030IHUv9f7WyClVJzMVxuxIQQqPmk-M50JVjRz2MJs2uRwt1pVaajDvlXkBlTUwRK_S2GX0X2_P5gAyAZFRFvIkmDbIyE3zYDq_sdDWm13F7OyTgiO_9IRkOclX4uyXKW1hdLpz4pmyRSdKNRv-lSAWf56Q0OJCH8jgeeCIZaZ0OUlWvXv2IqNROYgiCjebA8bAq11lBvIHeFI7o6Vynv_ZFZoQ9fN4Zo5a_eXrRKHHQGF8xTiHcMRlv09SKGTSYbdod94ohIVEMzpDn1YwiBLVZo_2bvFO6eLP9ExkIxIYGQ5s_XcrbbwPvgV0VgF60oD8CTQqlePEUITKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEC3jswxtLIX7YI7W55rvKHIyN78qj2nRN71ugQf5hZnmfvfgFNBHGsi2lJR6vSkdTl-cGsZNb9am0Zk6ZF6TWr0ykUaUF5aNzqj9mO39GSVePR2xODnEw3pt_97rjBin15j_2R3lVSUlhiZK4ERcQW76h3XPhxzsIhTC7m4LsZnWMRApiyNV4jDWgkT7FK8agRaL-VwrfMHDCz3psx4yiVXqR3ZuuvKHUcOo-jBQUs6tpCU3QgUefD8pLvgXxans_hGWfY2C9vTPDxzZLUnQt_MKKy-p30w-zyQ0XfzUStEu_WP3xTcoslxGz7zDgfydeJLVyhDNauls4EI3i5Muw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=AzdRkQAxL6_Wa-9SAfClP0AUJhtgPB7G0RbVOFFmRtJO0QWd5YsZj-CmHvUWJ71J0T3srpBivUc341N9t3WTWbJuCnhsl8WYqA2OmNAF6UOe-V-KCxOrgU9syKt8z_QGqQbuQoTZ-k0uxNM7SywLonfr-gAV6V15CziD6oidPSx-WGCbGNXND3gNum3K4nnACsb6LhMn9m9RcvUjU573-z8dPTWDP8VtmW9_rgHyVZWfDVHLpSEm_03AmKphZ5JYqKBJzPQ3C3GQ9VUd4xip_z7gRpz8URTiQM_Eep7wHpWSGDgNlkRAQAk3MsNcXvj4Xt8qCwiUo9tmor5yEatxwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=AzdRkQAxL6_Wa-9SAfClP0AUJhtgPB7G0RbVOFFmRtJO0QWd5YsZj-CmHvUWJ71J0T3srpBivUc341N9t3WTWbJuCnhsl8WYqA2OmNAF6UOe-V-KCxOrgU9syKt8z_QGqQbuQoTZ-k0uxNM7SywLonfr-gAV6V15CziD6oidPSx-WGCbGNXND3gNum3K4nnACsb6LhMn9m9RcvUjU573-z8dPTWDP8VtmW9_rgHyVZWfDVHLpSEm_03AmKphZ5JYqKBJzPQ3C3GQ9VUd4xip_z7gRpz8URTiQM_Eep7wHpWSGDgNlkRAQAk3MsNcXvj4Xt8qCwiUo9tmor5yEatxwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E472zmSaEbH1nFgjO0Qul95RaLlJwU_y5AgiZk-fi7qWMqjY-olVd-DWZWWFKlvsGJDOG3YFH42jEXFjkJKvU9mqEWKObFhixgSnx9h4aToVbHap9nFevdiXNGztIpdylB8ecGqvsEx-C0G9Z9zYE3cjwlQmV-eY_KUUErH8M2cWlxweaX4ECePGDV6yZlBludpFUpklqy6m7H5s0bGM3sFJzT5tVjfbfLy3TD-GHP7-E3H0ehF8A6JZfL7oaVC4IO0ZkAOVTdikUSI9TaBkuJAcDlVYG8wKkyCV_ObIY-QGpG9Kfp-V90227C9YiUztE2hfjDEuAjn6YGkBNOfjJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqNLd2gpr1H_IadHn9rNHiu-iivFQjPjhRCs-7oY1_On1JxTLIiHABO89sg5htVrJaFn95S7W5XyhPIqjjO34FcoQUPVvUkjBgensV-LNqoM_FbwramL9X14e5M3ayHiGXBvdqrJNBN1OXu3bzCvfMU4sybb2MbMBFYl1XOePmgl3rn-zmvh-c34T8K4bc6fNqLQEjyZj37Ntd_qusvRhi0MuoI6Q-hVfxM2ucGOZ7rkUupAJsLxBwDF8rU4P3VE-mgrtMQ2XIVg22f-Ql3GTE-kJvrRQ3jEsN0YT1ZjUL1aHBjZr2eSuT0HMbF1Tnlelf53MhQ1a5LtEDObsL9c3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=jsY3e8whdjQPp9JEYGKnkM1eGSQz4ofZDGlwzIjZ-Z08oaefEGvT5iqMIggwjxSQ8LNtx3ztinMeTySemKfHBdRibaZsXS3Cls17fa3nETDV7XGuPG-GCAo9QVz1cUtS28b0LC1KziQjbocbR3GvKAirpc9E2jeFDSrsd0SIkXLuEdurUMk32Rf2deEkKjxOwHiHrpNYCdu7Wa4c_3Apz5Kng94AkDZlGxxZTrqS7p4ZDkQsDpvAMHtJ0qVI8N3bbIVVEguhnSJ707yOTRoDnjS38tCYjKqG75xkVuRex24zXeqapj9W8hqEXCOMoMGfMuWhcDeK6uheFT7PbnmQ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=jsY3e8whdjQPp9JEYGKnkM1eGSQz4ofZDGlwzIjZ-Z08oaefEGvT5iqMIggwjxSQ8LNtx3ztinMeTySemKfHBdRibaZsXS3Cls17fa3nETDV7XGuPG-GCAo9QVz1cUtS28b0LC1KziQjbocbR3GvKAirpc9E2jeFDSrsd0SIkXLuEdurUMk32Rf2deEkKjxOwHiHrpNYCdu7Wa4c_3Apz5Kng94AkDZlGxxZTrqS7p4ZDkQsDpvAMHtJ0qVI8N3bbIVVEguhnSJ707yOTRoDnjS38tCYjKqG75xkVuRex24zXeqapj9W8hqEXCOMoMGfMuWhcDeK6uheFT7PbnmQ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=rw846t-ACVxUwLG4EcxFMPPr7061bW8df83qnfZzCP06syjwVMQRenMBgZ3QuSac7uGpBsTUu-y0ZagUcwGQXokJ6SkSKCHgKnDKLBwEaECvKbIZachiPoQS_5ZknV1J03muJZuD8Fxq7We3Jl_JolWOfnG5UOsg3FPRV4R9AODYehUE1Ql4kYaYlqr3pdHnvDKxygB-R24TyW4tsKvPzmSnlFQKbvYrVv-zhbr_WmPMdf9hU5c5NQGTKEx64v-ZGdLVCtVBaTegmkarxrcbfTXDTEKk4Bn0T-U3RFwC3PrggoqXwBH2ndbTHO0EhlLxoIREKMYWBneAbYpBpHtT0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=rw846t-ACVxUwLG4EcxFMPPr7061bW8df83qnfZzCP06syjwVMQRenMBgZ3QuSac7uGpBsTUu-y0ZagUcwGQXokJ6SkSKCHgKnDKLBwEaECvKbIZachiPoQS_5ZknV1J03muJZuD8Fxq7We3Jl_JolWOfnG5UOsg3FPRV4R9AODYehUE1Ql4kYaYlqr3pdHnvDKxygB-R24TyW4tsKvPzmSnlFQKbvYrVv-zhbr_WmPMdf9hU5c5NQGTKEx64v-ZGdLVCtVBaTegmkarxrcbfTXDTEKk4Bn0T-U3RFwC3PrggoqXwBH2ndbTHO0EhlLxoIREKMYWBneAbYpBpHtT0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=TconNUNzipH5Q9dRXSUZ8t-dhflR5n8M1u6cntvSAqjJW_mdyBGGuk9HFSoWonJyaMfwWuK295MdWNcTSNAECvH8xT9UF5qTFs7MQZ4ujlrDLTIgIcntX0wP1dx_7eTHsYWmW4X9uO2P--japr2FrXb4KptPTu6ELVZenhW99lRIwzAMsH743zuRPfFnoC4tGNOlB8VycJ6o0Woaiow045tRwcLWvutZ89kyh9OoU1xCnRwFMNXW4Aq1d-vN-NTiIL_LTbbgUJS9RNJjkROHqAjF3oUzXtnJetOyP8vi2a3s1HMHFV7CmqRDQVUzZn3fNovi9F2_NnkYa3STc_XvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=TconNUNzipH5Q9dRXSUZ8t-dhflR5n8M1u6cntvSAqjJW_mdyBGGuk9HFSoWonJyaMfwWuK295MdWNcTSNAECvH8xT9UF5qTFs7MQZ4ujlrDLTIgIcntX0wP1dx_7eTHsYWmW4X9uO2P--japr2FrXb4KptPTu6ELVZenhW99lRIwzAMsH743zuRPfFnoC4tGNOlB8VycJ6o0Woaiow045tRwcLWvutZ89kyh9OoU1xCnRwFMNXW4Aq1d-vN-NTiIL_LTbbgUJS9RNJjkROHqAjF3oUzXtnJetOyP8vi2a3s1HMHFV7CmqRDQVUzZn3fNovi9F2_NnkYa3STc_XvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3g9JZqabM4Jj_3K0vxdndvIpuy58oeMAEj1yLs9xuXNs1-DSzBjuWTTqrO9d_K8gcGJPjacHN4LXKtwwCWxTxTRmM6Rvrr6UbBuFshMrNA74v3tc5_qN8Xf3umkIwqrg0_GqcL8OfrGphVZAEbGQdw0bu5WHrTdHqWjiK1vLkwHU9zJioqRyBhlpYIvKFaSk9jW6bDiUSeGyNi--GltZQ5WHjw6MLsGRMPjs2pdggTgG9xM7JtbUjEPf6VROZqphESj7SMyuuTnhhAoy6vimQdPAF6v8FlaZyp6MGf0EDInZJX_aLtkvaYQuMB3O5XtUA3caiBCmzwoN31uIFQ6mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8GRYCBUXc9x0ZFc-TL03_2RVpbJR2C6WanQms46W9wTik178vUcNvuAbmuObmwKSZPVGU04lGRUbEegZGIBNSV0C4ePVJTy2doP5luD4SGndeUoofprcKTkHe-lWqvb1S78LG5uW6yA1RI_T4dKiFsQ6iAEf7Eea9ty7Oasg1HOF85IzFhuHHl_Ps6-PP3pKEOyXBo6FxO59YIujeXePEoc0PWsMr0_Amcb9XqbWJ0-GaEr9Ht-CTN_lPhumn1LJvVwMx5oGF_0a8wavZ4GhU-K_iQE2IAxhEGt-j564kdYyy6uw1b4sDj8H9CjV1kN2WQoSliRT2LVqA9n2Z36Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=N1m8fBKn5iwvvuJ9fuLuQF86oLkYpCvZ4n62mnj1EsIo-i29crgYZxrTBEtPHptwCFqAHelV6-LRwtSa7ca-hlIXYwArSeDOJlO8P94kl8zC2CpzG6wI0VCHlEVW5LXgB6jxZeeqLPKkF0L1x4jT4J39oFOU7hVXy5e30v6N1ESp87r4NT3GzIJaD5NzDcDtiYTSTNVqrJOkwt7454_4SsLsVcp09mOiO_vQVPr4KPy_sna1KEBh2LQKccYVpKTewdt5lsh2u7N3hw9Zj5SvsCxtHb3gt7B90V3dbgtve1M-fQFxz_63YtlbL_ff8chxZoZhFOeQuhKWaRt6EKMXg5qEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=N1m8fBKn5iwvvuJ9fuLuQF86oLkYpCvZ4n62mnj1EsIo-i29crgYZxrTBEtPHptwCFqAHelV6-LRwtSa7ca-hlIXYwArSeDOJlO8P94kl8zC2CpzG6wI0VCHlEVW5LXgB6jxZeeqLPKkF0L1x4jT4J39oFOU7hVXy5e30v6N1ESp87r4NT3GzIJaD5NzDcDtiYTSTNVqrJOkwt7454_4SsLsVcp09mOiO_vQVPr4KPy_sna1KEBh2LQKccYVpKTewdt5lsh2u7N3hw9Zj5SvsCxtHb3gt7B90V3dbgtve1M-fQFxz_63YtlbL_ff8chxZoZhFOeQuhKWaRt6EKMXg5qEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpFty68tp9Ve1S2aQUq51Den3JozgvJAjg_LE9yc36uVMJUu4fzTw8Nm7JF7iGXGhLp6xf5EAhrX_XvX7bMIKjAsqzC1_aHBeAZaS-yNK9L2e_ccJr9Ri4I5BRToQUYyAI9xNzrArORlfgGi5OJqBPeFJWu1XIMWa__r8uoJYP395H0bNKk4hyidBI6xEhAxjUD-OtNvTa5oYgbcBdnz1pFYp6nolRprhpj3bZcIbqiffHR7w3Gsr7OT_TFjr_cfO3k12ZcUhwhtITTRgOvfq45zMGpI2CygajgzfKtLPzJl1qDR06AQ5IalLpZjifh5Cw8lg3KHqeJbWtoT-YcvOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vuc2jhMsku0n-oMWeBTkQ7h58RYDCQtUyRwiO6DRZLpwBFXZdjMsiSzeB7i00LAIVnD7HfDM4SSbEDdDLJi1Q8DOhdTKHmCE4U-0hLeUJRoO5mA40OxfEVXi6vtEpc6nkNM9_CwoqpZFTc40Vfl3FcE3rhMQWdyIRd_JRQZkQvJAJ-mAiP2441F91FtR5yVEgdQlyuIixKKxDQIvdr6fHTd9Atf7fBoiApgq0CgfjtpamI8TdyYdMOO3nazYcwnwyPpGMjQTYRuJb1aQUWMcXAWf3QANgM5jWmrRr1iWv5Bc-r96UI-pIb80z9fiX6qAaY2wBeDSmyUv3Y42ts-xlr1F7gvBEGhFq5gMKFDROimxZgYjX-FkO5dTzyDSd2XyXgEx5nHm8Ndk8xkp4wMe39LxMEQ_aUpxYpaVm7c5znpHGpVdlRAML-wm5LlMkp5K0jdr9R2xAw9puT8dWS6CZlOLoI5lK6e1GEO63xsXUqM4lOV4WUDSF73bdyw7YERbQoLjnrxFaTqobOtRszfG-8pnB0G7wqmLw6LGBnV4pF4AYByRCxq4NW97rW_xvKSEHE9R0Wwm4XRatTGbGCFcpDh6qCoewgHpB2DxwUCQiDQOeokuUHPUedqBvkCKX4epwYzh4CFWXNKRZT85H2gTLwkNeEf__kSTQHtXTcFnGa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=vuc2jhMsku0n-oMWeBTkQ7h58RYDCQtUyRwiO6DRZLpwBFXZdjMsiSzeB7i00LAIVnD7HfDM4SSbEDdDLJi1Q8DOhdTKHmCE4U-0hLeUJRoO5mA40OxfEVXi6vtEpc6nkNM9_CwoqpZFTc40Vfl3FcE3rhMQWdyIRd_JRQZkQvJAJ-mAiP2441F91FtR5yVEgdQlyuIixKKxDQIvdr6fHTd9Atf7fBoiApgq0CgfjtpamI8TdyYdMOO3nazYcwnwyPpGMjQTYRuJb1aQUWMcXAWf3QANgM5jWmrRr1iWv5Bc-r96UI-pIb80z9fiX6qAaY2wBeDSmyUv3Y42ts-xlr1F7gvBEGhFq5gMKFDROimxZgYjX-FkO5dTzyDSd2XyXgEx5nHm8Ndk8xkp4wMe39LxMEQ_aUpxYpaVm7c5znpHGpVdlRAML-wm5LlMkp5K0jdr9R2xAw9puT8dWS6CZlOLoI5lK6e1GEO63xsXUqM4lOV4WUDSF73bdyw7YERbQoLjnrxFaTqobOtRszfG-8pnB0G7wqmLw6LGBnV4pF4AYByRCxq4NW97rW_xvKSEHE9R0Wwm4XRatTGbGCFcpDh6qCoewgHpB2DxwUCQiDQOeokuUHPUedqBvkCKX4epwYzh4CFWXNKRZT85H2gTLwkNeEf__kSTQHtXTcFnGa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeSQNLoTaAwTxhOKE_xyWCAJEsZI3KPrE3eM9qjWhteOOIfjyveSeIhF_GpNa4HGYuncvMT9XuPAFya3u9cbK4KxPmLOQUjS2mTFJ58PxnatlQIAx25iRqWgLWiOuQ0m8sEwvPwilPizek2pwtf9QBlsUFwZTzAIuq3f5JcixIYKx2NaaxVeNPoBxNY7Ht-Cl8q0XCCkt6csgOTAMOURlD_VzGbNaz9Mvm2gTTNE85-LcINc99YSRUwmHL-uqwtklGhi6GQVabxHTlil7e8B3NcXvQYt5KmEn2crbvlbaucK6XVgQLh0X0mpkTawj3thBTOJ-yoS0-KGD4I2wMSvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SoRfRQWdAsgPzC-TYKykOj5OP1mM7MDendLojQEdO45ezPMxW6xQRo1rpcxFcA4PN-4_BD11NwGnutPCxxHtT7-Z9feLnJGHUyb3As2qKWPu9msojPxBMoZ_uxKZ7E7vns_2Wld7lkbw1k-ivrho7sXJyZydXx9S6W0xcTFCsouTM-jLC6n_OEan26twls0iNpz4_9GSL1QSkLLdLYLZt5UhmnVaFZllOk5s1MfFHQ6m1vUa_L0EUITCGkFx8Ms43HGVMI0VIon73Q8wS4vi5ehzf7Rw1MGmdCPGOGFBy5iHRHKVbl2-JyvQRR6_EmZKNiCeT7wY8MhnjfRcl4Svuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnMSY0W-ZaUGvyKdxjpGIJBFw4xtAnc72IV6oDCHIh6WqUgRgaLXnvO417Mw-8KdkN9m7xvTE8r1nW0SoLQAriKSnd-8JLfg_iIHQbvB7cXFjELYTxr8dLmbwOSwuTaKM8bLz6REmvO_coeAXZE-lwtpybYPP0lj9eYPLkt9_jFWo103RgWw9xU-k2eT3gxNWqws88Pt50yMym9Ejds9Cze-73c8q97kQjaXmXqV6gzsgdkZVv_6a9AZGjniz2opeY00SjZuimErG6BBBsOXkJf9ZFWTdaOhqWgejbI43XwfB7sHhbJzszvyidjMU4xEOKOG-LcI7JiEiLS578teBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHkfd5Dd0WQr8Jpqmoswvzx6LvN1uTltYpIoacxUwQ8ks4eULl7YExvxjFeh8upnx3JIzPUOG_LE_-etK0vHzdRsGt7l5WSB-cgYX15Au-cn9Brd03K3AqmwVTzr5DsjdlkZ5IDEbMPbUhPnVvTGmdc6y-S-jRwF2VfF9rFXVCf4fTX-qB4bD5Ac1UT8RX3U7OF36IUF6O3rSzXvjZkqgv57J6zPuj7tC6Yo0WQB-CCv7GvueNlHsPa-gOmS_iE-lL7G7pXIvdhGJvZ4jgC9eSBImX-GB0ZLf-3g36KHO7p7F0PQpzE9hH0v34zVGSYN7tZxJ6Z0zQ-gRHx6lWF0Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhroiZMj-lrcvZabAb2WJ0bCFjUBhRv2qBEcrhvnm001TSNzAzkAMyTGjpjp9sGyqowL5ZzIR_w0PA7Oi_ZF4THYgSlWTjwJk8tCDxpqTfrAhA2KAgMSN7kiLHtUFKsxQWchGbdYIcAP4O9fXEwTk6qZUQPPKIxgMGekqOfDdAvo8MvnWs4QccJ_5VmZ7CmHOLiVzCkDhGXuytywwuJCFuKjhfvTT06rYwu0LsV3ODAdX6IGJcwncHMq9tPwgrXANsLGtcL83fd-uf5KSMSl4m3CQAZKMcNU422exveiAARGv42iTZJ574dO9jrIxILBQneQKJs9wmCjPR6s4-uc7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=obsLCxKfUdcc-EQAwH9yaX0BEqZKyx9ISbqVpYz3XI_EgfgFRyEMcwcm1WaKGCYKU7w7pw8Bqklwqd_r2APyFZM-7lscGYExj32vC2_Pv8mPFvXgX-HRNsijuP-o7FOPBby43pB8pdvtEfa4WMR8t1juEBe6jL-AR45jek4uJFEYsE630FJ0hG8x_qKNYUIIkZjFIw0Ler50oMhVdNFXrAcKx9q7lyLi8RpcBMFg3wmIy291pQME-snfwj0JgWVd_b6cnEAsNPbJAX_FMLSL0v5BY3X_M7pof2_ncwxa51FXOWVehtiazz1I9-LWaWOVorXlBQIi-OMDKwNhUyPktw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=obsLCxKfUdcc-EQAwH9yaX0BEqZKyx9ISbqVpYz3XI_EgfgFRyEMcwcm1WaKGCYKU7w7pw8Bqklwqd_r2APyFZM-7lscGYExj32vC2_Pv8mPFvXgX-HRNsijuP-o7FOPBby43pB8pdvtEfa4WMR8t1juEBe6jL-AR45jek4uJFEYsE630FJ0hG8x_qKNYUIIkZjFIw0Ler50oMhVdNFXrAcKx9q7lyLi8RpcBMFg3wmIy291pQME-snfwj0JgWVd_b6cnEAsNPbJAX_FMLSL0v5BY3X_M7pof2_ncwxa51FXOWVehtiazz1I9-LWaWOVorXlBQIi-OMDKwNhUyPktw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcTGozfnJ2WKg-ciXc_bUyi9f45emt3NjsQ6JEnEuh_dWREZjkQopUTqDI7aQKLzK4aqCt4L4TKC7SD2hVdXw4eNh-R_eeFHEOMLfo6QpOSmxFLiYzHSPclzORmDm2JSDdMRVLQEYNtOiB4pod1KAUvwua5xdT8t8x1APuagmJKjo9e3TSX6Az8pujXY2-1_47HBis4_UIOwK7c8-Ty8a22VmwO4kuV9PadHE5wsXYUcXu2OeFwId2OFe94HYRMXg30JnPPGddyC1Y6tiMQUat2EodhSgOaOpHIjPDovP_8IyJdHej3ZPtyeQUTQEOvUKnljNtNJW1vvmV7HsNpRKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKcwt7vDNhWgicBDFixTqERqthwdRnPIIuauQBH98f2k_tP-yC-IpWlfzyZ0HRYuMVLjwTLGW7Gu6PXAcs6XrUkQ1ply9l2gLHblHH_p28vUeWfqQrFlTYE8WKzWo1giW_fFsMenOqbdsz8btoad7McOkV40htyS4i_IcZKyLeOaoez_PItG6f0y_GGhdf3GtDFfgaGXixjZ9m1AOWh1Cs3amGB4K_9cszvYlkWhNZklhYRqjRPEyvEtaYKwue_KKa76vgtpZ3owaq5dQozOX19F0djLcwCLwqPMN6Gmv2UM5bFNK93hZDcREaxFUBze-B6NBnrDGiDb7Y9i8KCuSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQWwKS_QL5E3zsBQTvHboprxM1FUbb-A3s1A1Pq9X2iCYynXIXJo-8-gYTPH_E5xHfC5fSsKr-A5vayyrbj4b_X9yHntBHjsi3oblYezWWsDkq-w3I6a9Mb3JyhfXf2oE31hEQE1Z17IXsW_phSZ-A9MV8IEJcngymAwLjKJOmYLUWz8uQLKuHqbh98J1pvtcrE6yy2cDJ3a7iM896F_POKS7wne1zIXQMZecOfZu1BLWlaIK-wyC9FeIr8qbCjU2xB8DQoyTsPJwLq9BavQSQB1wmsjq6J8v91S801-FBpbHIAFgLikdG1B36NSvPa0by6QosnmfvhRJV2tf6m5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
