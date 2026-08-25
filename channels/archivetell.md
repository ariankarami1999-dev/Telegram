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
<img src="https://cdn4.telesco.pe/file/IzRktD5naH0hgOBgnY6MoujBk7oTaDze-Qwa-kERKHyqqammV1QwYY1OMSo7j47OpEUFcQhiNwv-CroaQm_HCU8BUTGbM47-jLeJzZsJB5bPJDcGAU3c9BhZStKYgil25breGzknJJZ1HKRlOmuvBU8zyaUvECjN-byHaf_-ySL_ldfF3yWTVu-J16sKEaXvEHFkPQ3ARuVrrpgHKTUBh2CJRBxRYxgyKhRstAyWAs_zR8qF7o5chXD9tJdrI020WIeGJ_DoEhsf9g8x2x-GZY0D5Y45AxEjbHK21w3AqJHhXqVsJb-xmhxtI7bFlXubaPzRwgbrVc9AIWPABfCDsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 23:48:21</div>
<hr>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihGEoBGAaTkXcg1fI6CDmYxFsjuO8m3OktZ9f6SYmW5zNllk-LhDi4FP4crv7cHuAkPGJTPM7WXsnGwrMtF7nw4G-IixkYfKxMn1HyJOl7RuzREwUBTc8QEkxtzcoeN8YtcA3XV8kZhOsgg68HDS8Dg92aP4mGsJaU8oVegcEuwiLZfeRi_hsYyMSeT6Co2sMHspvkEg7f-KMFEg2b6J8aSzHAZim7irlapOzBL6lCIbHL-LW4ptFIZ3pTukt2gmfj6tX24b_K4HFQLjz4u6YMXKP0DXIGCURr6rkLHM2ktCnpbkF74-05dEZOwlsfTPh3VbtezqueJPN-kJ2GCyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoGHhX3q6sjg_MJH8Gum-Dk0EuEAPJthJEd3Fr52h344kBCvFNgQ9fuOMZjkKOeV5V2P0JXHwF1mLaEHFL1V6P_76NlnFm2y9ZiE1H4wzLtg_wom_Y4d-ilSkk2sC9XIzE-rCWu5cgDSHGcUAqeae14Oc_TynGn_KSUP90NyuUeVY9_1_IuBD_VwlkFGmN7lMlHj3jpzjdlAa4saIWbzaHrdpuUD8KJqM76Oz3To4QmBvNtfo9ii0y5CJP4P5RfFZxOwrRgMNEGnI9AOUfGKcIN1Kz2hrpde2DzvvmKf9IvyUBuBAdd3aAw47BDNAF97wuQoCR3Csy-JFRcY_uXppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVFLjnvFD1gt98cuIJBvMn9qHWnVkaupwxcUO0b6nYMh4gByKTXUWKBZUSf8drtgrvipgtz0oORpDDEiSSVhPxvmlPkKjfaPLu58w8RozOwSzU6r7kpbadFcH6-bEQdnGhyPirVJbAlkGr4BBQLr578ognkmiFG7zuDaYBTvVs46BrWf0PaBxu9hIhaZaponJ71MxSePDJfHCyxb0YqhUp0PofTEKQFC1pq1kSGjTYNpgJwcLonR_oTBwHLjZMhL_iTK6LKoLhhjwmESNLjGaS_OV-ftODDtBZMlLhXQ8DQxmOCNSfRmEIpDCRDnDCn2MTjAuIM5XzkOEud0HJ_Wtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anJJjqgnMeqcIAgM9L0T19XbyT_iSX_HfSWSf0tL76ekDrNT23xBXlOr2mqQ2d7sfr_dQEtPiTwzkhRdQy6_GgZ6ZgoiKjKadzSmbP2cE3L3XGjtzl-rPad8SB4qXYgRlWjhcY-xTO9vJ3gVwQLJE7yXVxNkDPjrdeVRrLljjFlOraOViCZSn2KmXDLg9WHdHNMzgY3glDUEEcEdUcjnSB9pKoY35TjLHjEG1f2aOh-Fi2S-mhoCxtzRw9blJbE4Lf3m_dMmXxgXHcVN0rzIV6GFqLETvdwbWQB3k4nrtVJ32qAJgoPu6FeV1OTQvXAPbPQ_Tct4GRumSws6bR4XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WczFN9BVLoXtmDbWqG-jXf_FYPMDnE5MX870Hgdw1s41Jkh8vvZ9RbvVNkjQ6pu5MkW0pblhLlc0E30_p5sNqOZa22pL2wS99yBgaJA226PY0vRn_j46_GzWsXbiJVBihp8X60rvzx-Q5XjfQt28lbhsra8fOZYsbWu3M8GLogpTpmPvXAJfDP8oYHSYy-bXcfIZATS2jeOFXtwjXDOqj3KOrlGYkJrYSjy5h5X0R3QXCzpBGWUx4kTKZdW0LIDkHri059teqn0Rll3XbQlv1reZbwpC-rOw4B_8ZSB5jtKhMRkPUXWADo-g_dog0FoT2s7Y5i8sO_trwLA6bocu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=uYVQqlZdJIJ-NFTin5uyvBicaOCIE13sSJcbootvbQKvqiCYa1PLbHAr9cDLRcHGblPutAD5ujakwjQdB_Cgqx8mF5h1msOThkE0rnrOpfCke0LYYv4F0BAM0IBZ1Kzg4F-neycfesNj1PDWDH4b2jY1IiVfrz9sBTQIpUWraoFIikTQF5em-nBpCoSz0BdjngW7TCddnl2oG0_n3k3Yx-yEgZo4v-tJwKNnFr65Offum-Alhsju3gysuoKO9VPpG6FY5N9Jwe2nE5a53i2mq8ldTWSr4NWesEYIpxSHvWMv9NqJ6xjTiaS1QsuCIUxWZdVN0k816mBgNky-0IeQdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=uYVQqlZdJIJ-NFTin5uyvBicaOCIE13sSJcbootvbQKvqiCYa1PLbHAr9cDLRcHGblPutAD5ujakwjQdB_Cgqx8mF5h1msOThkE0rnrOpfCke0LYYv4F0BAM0IBZ1Kzg4F-neycfesNj1PDWDH4b2jY1IiVfrz9sBTQIpUWraoFIikTQF5em-nBpCoSz0BdjngW7TCddnl2oG0_n3k3Yx-yEgZo4v-tJwKNnFr65Offum-Alhsju3gysuoKO9VPpG6FY5N9Jwe2nE5a53i2mq8ldTWSr4NWesEYIpxSHvWMv9NqJ6xjTiaS1QsuCIUxWZdVN0k816mBgNky-0IeQdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=C_WXYAT_e7mANTqIT8jNwbc_g1r-B7WbdKNI_v9pkXi_3nMjrnC-t-Uj5WgyfDFMwmAJdYOMpqt6HzvyBLRj2lWR1_g-Xp2ciktyHxfhJzhH5ooCfDWe1t9aBqD9cvTDcQyh_4rpspOOfaVy5lHM5bbvnJAMTk0_n_wfDA-gbUDBvtoMx7aTD2OXfTFdMsFkDTt1yLcfFWLCZQGBEpc5hLih1qmwlTgyWHgN56wXXaZkHKJusgWZYufVlTH5EWOM5dBNb_gVsT2wTcSKuK5ONPQX3RmIn9LU5SKe_1s0uUVN4DFQp5PU6XSUm_pu4me-zvVf-qUZ9ez7wHHhVAKFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=C_WXYAT_e7mANTqIT8jNwbc_g1r-B7WbdKNI_v9pkXi_3nMjrnC-t-Uj5WgyfDFMwmAJdYOMpqt6HzvyBLRj2lWR1_g-Xp2ciktyHxfhJzhH5ooCfDWe1t9aBqD9cvTDcQyh_4rpspOOfaVy5lHM5bbvnJAMTk0_n_wfDA-gbUDBvtoMx7aTD2OXfTFdMsFkDTt1yLcfFWLCZQGBEpc5hLih1qmwlTgyWHgN56wXXaZkHKJusgWZYufVlTH5EWOM5dBNb_gVsT2wTcSKuK5ONPQX3RmIn9LU5SKe_1s0uUVN4DFQp5PU6XSUm_pu4me-zvVf-qUZ9ez7wHHhVAKFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaMfE0SfNj0cogqg2tJzilYnbc_9Jz8IWPB0cxhHu_-7xzWFOHpQbwIE_rD1eVD_tVuFuoiPsoHiQUHhAAr10cA_UkibCy-5ERheM3tuSVzFGbhsoWEKqGADQwPeTT4H6u7SGRfQXXzmEfCHYlx0KU3aqGofqB5DLyh_u7GS7dgAouQIt8E7iWCW06pB2SahpMGSqF7Ampl3KmLt389DxcXdh75pRrBEI0AeI4PAiYOTSR1BakfM63gBF-DUf608FZGnS6BdSm6I5fNCleGsC5G693-RThc3dQvYL5V0U25XdS3sb5QyBxYKlytBSr-DxDDLy9U7S50zDDQpCe81vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ5Q83lOXGbOOhzzc2NJRnhlqgTw7zD5LT0FkjWfEuRyymV-FMNF_jlzVXGN3lJCNdumIvGkgeQJhGcomXDxqnbQl3h9OYw51GHGTeOFj4XMletFA_y-FkFfifJS1Uw0T3xrEntP6YKPWW-rwEJKjzZE9T23ygzdWe6nN04LTMvOG1cRKwVlNNjMgkyT0YWj0RzaRN7Ml_2ty0Dio3EwJLx9RTfC44O-CrNVpgfIlPho7Fv0Yl7AdYT9MgoMMabOi3aqstsvf0IEGZ19U6gXu0oCFfzKwbULpgRCvED-R6AiRiRs5XMGPcd1nb9XNUXz7mf1dPOkzrPkpFOdBnkl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spEi1WE_WzxXYJuwxBJOtOwk1jPZJs16RDrT1AwCarC5VPf156sv5HAXyTPyhEimziUA3EKcRPfrehCoeWtv2_qygShRSwB4Cbpu8MAc9nxZ7Per4Urg5ibFpIufzLhx8Cq5mYowQMe7NobA8U1CdCRUp4mbhWy1RFB06N7lepMt5VI1aUf_h_RbXYg_kbTSnmNdJ_tMVKP4Dxs6-Jkglhb-fdXk-Pyv1xCO8xMrIZOxaGTrL8jQHe-FCwi0exZdJ2e8soZWy0wJ2ttb6F-BUzIvw4z7YHGX1moFKCPg5ZjU20HWn7f25GC70q_0Arcnc1sSQq0KJGVXXGhF0OXs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=APGLFY8_ShXVAu1q8Lsr2iVpuxQOcJRmgB1NeYIS8SnHYpwec9vy8UXDmcNfwfxTB5uiBtat11fiaOkU0BXn5jskE2GVuu_MC7F-2A0cM70wOpwPqJzWy2RT3n6ohLMtayv2nK9jjMUGTKNNMaHiisDZpY1ACbdEct92tAT8NDyf7jaQ19DdI09JY_xcHLtXFKsZBTtAGPlCehs-RYvv9I-SGzmvkLV3ziii8MP4MKe5i2Q7n-BIlHqnS5f6nMQkGE7PfEjTxiPOkNuj3z5C8a7byAdWt_BDMwtPDo957R2A9BgGqaMtRDaM8qjpR2ZDdlTziMddZPxoWDr8kz-K_2NWb0TQNGVcsgNwGdF99-N4QqmI22W7OCngYWvdfZjpdT2oi1a3b18ctbrZv_70xKFSRBJoix8OnIFHo0OsgKg0FRYXz8pBE_QS6mXKL5gJQdO8ex19Sv35kezPplozGre6xVFxq45KXLn3hFx78avH5e4oqH5T75yJqLWntj14uGKWSn-qzeMFkJxIKEMgfYHmanqxdGK9laH3PgSeT_6XGtrc6FrNIQdUWmxzchNaNYdwln8veR2_lvzJ9whG73P6TGwN1Yk3-Bpf-QCWVqKYj6ZXgDu3xQwbL8hAIee8pjRLRkkdyNbk_-jzpnbDuRF3lhuO3KegEpH8vSO_4ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=APGLFY8_ShXVAu1q8Lsr2iVpuxQOcJRmgB1NeYIS8SnHYpwec9vy8UXDmcNfwfxTB5uiBtat11fiaOkU0BXn5jskE2GVuu_MC7F-2A0cM70wOpwPqJzWy2RT3n6ohLMtayv2nK9jjMUGTKNNMaHiisDZpY1ACbdEct92tAT8NDyf7jaQ19DdI09JY_xcHLtXFKsZBTtAGPlCehs-RYvv9I-SGzmvkLV3ziii8MP4MKe5i2Q7n-BIlHqnS5f6nMQkGE7PfEjTxiPOkNuj3z5C8a7byAdWt_BDMwtPDo957R2A9BgGqaMtRDaM8qjpR2ZDdlTziMddZPxoWDr8kz-K_2NWb0TQNGVcsgNwGdF99-N4QqmI22W7OCngYWvdfZjpdT2oi1a3b18ctbrZv_70xKFSRBJoix8OnIFHo0OsgKg0FRYXz8pBE_QS6mXKL5gJQdO8ex19Sv35kezPplozGre6xVFxq45KXLn3hFx78avH5e4oqH5T75yJqLWntj14uGKWSn-qzeMFkJxIKEMgfYHmanqxdGK9laH3PgSeT_6XGtrc6FrNIQdUWmxzchNaNYdwln8veR2_lvzJ9whG73P6TGwN1Yk3-Bpf-QCWVqKYj6ZXgDu3xQwbL8hAIee8pjRLRkkdyNbk_-jzpnbDuRF3lhuO3KegEpH8vSO_4ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8nJDbfc-kkgs1jGEF0hyTquTZBLrAITYiZVOv9ctnV0Pk_loYNt3zFbOMQcHBsl93Q_2w26iIYdlL93b7_CJegj3stCyVTf5km_ZihGHwadyYuPgz3uQHAqU2VJzCcKFExJeSkzIe9fd61PkLlLxr7-DkHvtZVK3gy5q5TKWy4IhQHYQyGKrLDC3rt2gG2dPLT5KNury7H17-T4HW9XplsAlonkpXFhae3gboSPIP9eFTG2vMxjw1JDcvRzHRcnN7bOp4qeDD7ChNi0JWWDdl-vxLrSRC8rbbMaoCslSUL7d5JBS7ph2ZfH7F83DFecjnwe2_N6Km2wVbfDXUrHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2YsFsXoM0Mi_rVtAekx1oJff9Ft9IloYNVPgbDbJ5ibuCC_-bfGBf-W5ivztjjbFwrcCHvRujGCjlwKuLimF3nAvglG1LYnSEchLOtNprbvfNok_Eybx6AKFJzPVxHISWMQSjg62HE5QKCx7cjSoUmJsL2p7ZGXdYzMwoDcjxyXYxW6aMkuFFm5kuXqQeK8nvODHpR-yy7rlYJVknivGqrK-hJiwNhSQ7amSqMseGipNaTkqJve6cvA-pMReZkRYAOnzOTHmtutl_fNYq03Z5DI0wZpRCSJc8RZ0q_GnXiGmV00Z1JG9E48IEy52RBYRz0jZUtERiUa9WJsKnL0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugzmQFT3UzC9sagevB5kqZm40t9ZMB-Pdv-yCchrf-O8UP1m200gOegHulaJtFwLXk4BTbVApj0R-CRZRBSVezBnVC8g05ND-y3ma07khCjx06-yHKxBzA7DCptPwtjGqgYDoue4ttbTyDA3sfN8TWBBGg37KC_n_y9SHUlKVRlZO9qzeMfYgvWlGsGBuwOpc1PsATjqcx0l8ulIxeh2KgUyNIagI9fxv4zOC6Wul7OrnzMBcR5uP5T4a9SJ0PMhkNblPLNfnzvCwG-snJ5-too6RJ6m07EUI681axi5xnaylRmMF0jXKgwV7CEBptkIZ2Oil6ESGxgBFIUriTYkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlcz_atjImF3NgHUs2KQeQHSojIkfWrxlmmI20XLFiij9NQGoonMAIVaWs9ox9PcdZ0hYunm0eULh-QCIzLGzioOngMCnYMU5KJxyLi5L-c1DnHdbzvtXHEKwhe9uCLiKUJYSZBFwAKOKG1wxJvTKlY4Fkyq6d9FOlipod4nRuXifVleTut9BwKwZje9hpkqbes_En_Ntp1kGZT3x1U4P7_8T-71in52a2-ev0iNNy0ZbVd2b6W38v1zSMIJGMLDkm5iR8pA81BG3cOFm3Iy1Ndu2YxPLx2zDdMHlO6PmaT4K7531RvgTBajc4Ngva0i085bu4tRzOKsC6-wdGZFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBlITk7x0r6EJCbvrCDPmy47oQA8kgUrHO-te2VZFgvO-ITEMTr16elHBsTJEDQxHV_mSZNNz0YNLx4h9EZYpfByxtJpmfg3n_WFzicHfrpj5tT4ahw5NwTsdbRgJWFxHZFP4VZKLctMvIGdgg8C0M4sQER_hPK810Bhazewt3JkvpX07WZ-4fhhnGcJuZrRrxPxxASjtsPt2u_F_2bCKiq3Eeyxva54NUxsuKaD7mtZgJa8fnfNyU9d_qN1OwicaOFGUyUxjFmNldP-7tCwmL68169se_LEgt522zJQ4ci-PsAVCthAOgB1PP5ajEux3TJbiEY3UodTExL8TPOLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlH955hPpEeyoN5lOGJRwPIUiSzNDHXEeRQ-6w8lbA3hLOSdu7eYiuYqjKiBWA3B2eYqm3TPnbGVSUXfvQq9jq08TtkWGrbqrOmHPsXIdUR7EMy2oxG9y2_60pFcKpj15nF5TBrjp2dG7KyzpZOO1xnVKcyNJJH9iHgyLClIroIJC_iwqU4R--ajKwKyY95_LGlpx6oPWb2JMjEbvC-i-EYHT2RwX10QgxFMPaueesw1IaPjNzl_PiZAcwlrdv62SegwXXsWy5w_uYeKYMbak_6wEjKEVXmPY0r_KPBAtC0twCk3FrqgDLWFpGKTEhu_WyBxIf-yJyeFxvJZZ2XJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ho79LdmC3tkLQk7-ix2BkfOhFotOK9HrHDrs1xjGzD5osI52A7tZypn_aN4B7H1CHFM2HZjQ3iESPPdnWMVJvDXo_00xNWMfRjVykVRo5_Kl7JZPTKN5RoKe6rmp7VKsrF7GkGGuhwoIQShJyD7mGiQw7T9P7B_Dz-MejeQAPGVZIcR2uAF6NDyet7_73ukpOt6bYrkdpnidbHzskKnZNCyn2yPdzjXhkyOhhSPy22-1TOSXbh7Chslm7BEWXVPpHbOqlnz53w9prsxhPTPxq0yaBLdtDPuUiBlE79CA4Q0SE9Bnsqql4PyLrqnyyzbOM9IKSWtED5NbwvpJP50s8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ho79LdmC3tkLQk7-ix2BkfOhFotOK9HrHDrs1xjGzD5osI52A7tZypn_aN4B7H1CHFM2HZjQ3iESPPdnWMVJvDXo_00xNWMfRjVykVRo5_Kl7JZPTKN5RoKe6rmp7VKsrF7GkGGuhwoIQShJyD7mGiQw7T9P7B_Dz-MejeQAPGVZIcR2uAF6NDyet7_73ukpOt6bYrkdpnidbHzskKnZNCyn2yPdzjXhkyOhhSPy22-1TOSXbh7Chslm7BEWXVPpHbOqlnz53w9prsxhPTPxq0yaBLdtDPuUiBlE79CA4Q0SE9Bnsqql4PyLrqnyyzbOM9IKSWtED5NbwvpJP50s8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqCRxoiJMCB35EUJcYOkvXS0TX1-jc4YPzqiWx8r2GLroeerL9yaSA9kskvHpHz-kjjODxmp0nj7d1sDPGrUWhCoYWbugxnuPD5XKRMlgqkYtePtFfiWqGFreX-gJqVfkc5ri1gqNOcIBOmkqdbp5F9q0LVzDHNIvZa7HQVFRs-TDDGYlKEg0-sOSwxtYUYQAthWCBpOCIiu-PscVkb8YFFBBraTpuhpGF8cG7e6Vu41jM54GDkc56L2pNzuxowmfxtAT93xF1QHRtOwgMsh7sUcF5UXNZZEVGbvdN57TgHcCYl5BUEHtbeL1UbiYneeZQciJn-qKGneqqG_C6HpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afm07quJ4LZl4--s4VYV7cnpiEpHZo6e4O4kpBdUTUu13e_OTYumhOw-3aLqDn_9QW81hNdg1AnvejaKv6GXgM-pBrlP2fKF2iO6DSPRK-OpR6hXEjjiyRDo3uXSFj7kVxmR3Ax8zk_g_RvKDMKxY_mhRvPlZzreD2gpy85YvHfVJcidItAgnwVBGltcHmSzMNo2XebdhLLEm4E2lP-k1Fwrvy0dMCAUiHmWkGtV5-6sw0OZB70neAQKSe8T0fChynxZYEIPTjv_G42MUpnUGRe4uZpc8uJM5QUkxF0lZRq_fPew6flIMqE-3NUtzzElPdSIJ4FyPD4BKYnqcFAGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRzl2p-WSGDNek3TMmNr7vBT7mu57SB_3goavs1gkjm_eob7fi-4oKZPa8cjRQd3q-stcxW0foLwj9I3ZXv2BRQEaA8MQp5NXnearK6SVa6pjbLtQpsMbEp1t6a-Ce4CqR9g9zVIfw1Db6-wnrAoJHVv3u_PJ5Mm8Alil_nlFGHfTRcWk9oC_PchUNiqTEryQd2GXmDDCNRWJnPzIT0wWzGgAlfFxfVL3KpLr2cCiuoYCK7mzQ1stkcev_VYbpzSQh-_LFt-BHFU1nnlQ5we2rSKO0bNiTPN3OGpU-715IcqaLkNGZUXugZYtyZ8IDlgOp6KWA2_6b0kAttXVej12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpUjreS0ZvzIDFoZCRlrM6GZ9hI2-eUJ4ZJZeVlEBGABPSPMf6ZQFe30Kba3Q1a8F3lNOa0KcPC9pDjAFERw0K3_jIr3qWnpRtne3JZlboSEON8F7PyJIZGPRrD4_7lc_5enIN5ZPOikJAoJf63ztNW108vPBBU19QXLJH2I8SndBPk6jl68w-4O2yKUwBg1K1j_WTxOR9d4WvTQIdXEOpY5iqIESb7_FbE41wFklzGIc41IdeHURRZ21bMVAaoc2wAlrpUTz0nFhqT5eTQ3JXm_U4iur4VF01rMcNc_i8OHWb_1mSWLsNereq48QQ6tZi8qauWZEYYAoJfmgQW6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDmdQ0zsyKDfKO5x1a-PkaT5IowmpNIPX08wnMNgzFQ9WnUZCGwIc8fNjm-xacm3VGndTErqA_61az_OSF8ADqjIgLoCc-LBedzk_dM4IUxaE6UORgYzrrbMhjmlmpKrcIABtzGm09cWSYxGnHcnU04cm-XKPuAZAVFq7QAFVmgrwT87GmWeGHBIfRsYCxN01fgchD1U0GeBPTUrTsdpjkYGVkMft8dOB1jXzPYEskC8Ggp_8UD0qIMwIydqL3JzsZfE9_H0zStc-KAsTg79QTg5DK3E9zm0_WF_-LztNZ91DkrIk3To5usVmAOft1OgB7U8FkUHqkA2CtqC_VdbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP4DUJM1SzlP8ezlBgtiR-6SqhX_wJQlJ6BOhO_qKZp3I_yxNUowUW1WT4tSEwootZUFlgFHwWCleBH1RYiTvFCVxcW19eCC98sDEy72QATV24uX30QSuQTu7e936CSh-GY1ryRO-cnPunF2Wy9rR_FpboqkvEX7ei_MsDL3oai7qzPqH4jiY9817gICGFlrMLSge738W__ffxzymwuRVB4SLWoZArHdNRsVf7frUhle9SaYJXu7y9k5vNfvPAJvnV30F0KZyq9czil4WsxCGQZWkmdhVwx4ijtB0cGIqBtN9BwVpxFEk5amv0oNHdd0k3RTo-ieSSpVMV3ukIlg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDStl5Gr00r0R0tNTHr2fT4P_X6etgq9aBeBAuhUG-qJ-cQsVWya2Rl5GB8RlDsUbRiJdvxNL3FsIECR673nxkycKpWGG_7bTI-SgurYQkVEhB24HRmG1xjjVBvqmQQQREj6LYqiaGeKhML4Yx-vr01m24MxIdisJ5C1p2nBrikpHyggFCIIi2IAPvYlzLpL_SZoWOaYe44sIJqV2plRYoEJPiHjyuaGoA4evB7GWzpsPJKCNfZ_7dhg5V_2fNVd7lF0aW0MwOQYs3NDgsRCz6OL4QgCH5kur7WVCPy5vpJVKsQW6OMsI9puu528bgOFgIreBeHWfAhD3Ox-_7R1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb4BEG0JXQukqrmmOJMIsZir2f0UHFvfgdZOfvFS1vtkP8ntcsPeSEkeVrNFeb0a4b7bwZOzYPEJMogwfjXqUOSg0OPi1RYhCjjRYq6PLivCedBxqMjLL-Q7XmtWDKPb38PN6hi_tQ-JxMxZC5eKfZlqCCPDgvrjjo_IQw4IYpdQI6a8ZS8bxN_PR4DHOTvbNUWuWSXVRD8cT-XLVdT5VZA7rlke-EGbn1e2nB7RJvnvLyoU02eTfG8Ww3HqyVPMj7tA6OdwYs0rCzqIwnY4JdwNvHpJhX-qCTBPMOrEhWRtHYcXI0K-XcYDAi7y_BEOIhuAE5E1XcDmugdvxoBHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebjCf0PMSbxwDv0ApUNwynasVPDKN1PdQyMqpaJ86QQU9RiENJh4T1hhLwfG63UEZkhyE4l7lAPDQJRbHPYBHuAN98BuokLPgJLosgY8LFm13Yw3-_hHjNJeTnpeaYQHZFutIWgsGa2tw_F00MKmJiFzFmq3QfokqkJTQwvxPz53pBI6pDcmqa3Y9JrrXzlxtElg_5zVFjwR8Z01PspR8vK759_9WXfza1Mppnd6ZsDcLTU9Bf_2uxl0P9dagNZm5Zl4-ra_Tad2alLCN1bebFP34OHEV9p6YHScSaHjyyVWs9p1wHMuZIbHJm8xxSgNih_fj2x2e33W2zWx3EIw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=arNfWA8g5H_z170CjLmvJysDQsDNJj-0rkxUolo5G3XEuIuLFmYexQSOz2MFiYIn_WCZCxQkrXWdcHTs4nEOKKsfT-YYhJE1rcr3rIFH3k8dNpNe7gdWWTQzxmbPNXewG00qwE55gxDt2y2PIn7VCEgHI9HqwHtaIWXIJ1bcD0cG2ZqSN2VLxXMBKGUv5wQNcbU6_6Q40PKuQdRl3oT8O5R34mpIjfY8o0gGfQ6kfsDEa3nYZ-rrcNp1BmcYDpZHPFDU46qiw0G1EXHreK3pyHy82L1cXjw2Z8IvfN0fXuuRBKtEcWFGGOR0NA-KyAxn_PRoOeXaTO25TPAHRcfBR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=arNfWA8g5H_z170CjLmvJysDQsDNJj-0rkxUolo5G3XEuIuLFmYexQSOz2MFiYIn_WCZCxQkrXWdcHTs4nEOKKsfT-YYhJE1rcr3rIFH3k8dNpNe7gdWWTQzxmbPNXewG00qwE55gxDt2y2PIn7VCEgHI9HqwHtaIWXIJ1bcD0cG2ZqSN2VLxXMBKGUv5wQNcbU6_6Q40PKuQdRl3oT8O5R34mpIjfY8o0gGfQ6kfsDEa3nYZ-rrcNp1BmcYDpZHPFDU46qiw0G1EXHreK3pyHy82L1cXjw2Z8IvfN0fXuuRBKtEcWFGGOR0NA-KyAxn_PRoOeXaTO25TPAHRcfBR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voD4vhcqTJmxazcFRPyw_8cZUHhe7V3BuZM8xM1vDUdEn1IA08OPyalX1lapheNwVMubgeny2MuFxQKL2rmv_ehyaI4ESC2hLVDZEhKu3ObEN5DBGOBuTYdDv-BtTvHa7jyREhVD5J5HcCJmBcMyN9wNUK_3z81AhhToPC112-pOHsIp6RIP1gonXVCN5OS_vJHZwOesYYkOqw483l_mAeyP2L6MtZRBtXnOLQuSSseYB2CLn-V3EuoN7E2YUZe5Z9MJQkrpHcSQn6pNocYHnF-X7YO9fXZKTmVNegDQ7uNsqfMKAdwG6mT48w3yNagLaE4sq61na-TfsnY3kSJ-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDRe0KnU2H9XXcRCxzRsRHPvOoLHcJ7FbeEpo4JjQXzatw9qyLEXfu3_CF2EFfhIgul8RZE0zTJ1csosuH-JH_zJQ_wFXHHmcHhIhlyRGM-At0S-ySqrPqFcZLwsHkYKU1uJMsJdMUQuOsCTC_hEeLp_LwDfreerYxGyWGs7eSykVHDKZ7g87dOzzvqXeTxCuD4rizfa0dkZco1vEfbSPCD0zT8ZZXDlaLOrNqd9y9dyLfk2t_AMO2XcKUt0h1vp8hxqUrDExtbBqPT_SX0gqhKw7Tni03C8lP8-1jwG5iHgYAIiB6h9sGQi_M1CXbHutha1G_g3uNoeou4KldPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDSuPTVl7Q3LeLRHWUcsFHyEivuv8LIuby9A0DB_IoJDJLwSxtBhmwbFpWypmtlz3DH7Xy8G_ebLqsTOtcAmN-JmUj6Dc_wTpJj6ESTO5NKhYzb8sLWbC4l2AGxHG1_lmL9YgLzhDZyPHZ4SpoiK3CcuaW4xbXVYVyrDRRyDZAVtjjI-8zIflzfcLTuyD9wG1EC3KsnJZFABwb-lBcUWDPmFqcE4-fBpgffVtk6sUeDt2cPOAZJa2AtWcP_fmQdhl1JIqG7NpZztPf6YEdjvaZYCF7ZJdejrKRagmwXgvjMuKDz_7iICLBNNsUdOeHLpVomLz3m66YucdX1i0uu4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc0aMSmEZBRXWjN5Ka8DtoE1zE7OzHyjJdmqN1ode6GIWT9SGJm4Sp1v4zn4eBQLb8voXgehnQ8wqYegrufvVX6hjHQHz5I7P_dE2JgflIafALehU98O2S4cVtT31xQ46y7cO-RBT8BUD-eAhdqZAKbARlgBq41y6oEpAc3Ah2jh-NNEmHaOkdkk6H1xkLhNUb9lOHOUsPrPYtOZRS8a2-C0cSTpu0Zst_Qg1omeE-yC-7DEzwOK29ahXrIlk_6KxymlCZWh5tGe6_cr1dMOE07mRMPQzlbRjHhPpM16xLzV8G8fGQvhTj2fMU-8y80XmwSUcVeG9fAdD03zh3G4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=YvU7jIePNJBcj0RJ7J5YmrDBZNvJraiODPncyYUUU-894W74zIiAaogrdC-UJ0MuGChOBi0-dtwFp80QydyHIMb6rK9XkTEaelGKweqIFQeLjiPFGprEQk8dqOJjRDbPFPcmdwUN5npXLwIK9dMrQaJtH-9cFZIt6dzRK9jD9oXgNTtdAx-p3nflYqhG8q-jJP2rtkiI9GSNjH4RNH6g77_59rP0iZvxCm02Hpi6Xq6Nqim-LBQZeGiAfQkht4W3yISc9HLmoL_mO2-r4s702Q2o94UWzP9z8Fj5ijRNDlSvGGeOmh7jX6bn4hImqtLwvkLxVxSKDsNq6QhsFVsVFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=YvU7jIePNJBcj0RJ7J5YmrDBZNvJraiODPncyYUUU-894W74zIiAaogrdC-UJ0MuGChOBi0-dtwFp80QydyHIMb6rK9XkTEaelGKweqIFQeLjiPFGprEQk8dqOJjRDbPFPcmdwUN5npXLwIK9dMrQaJtH-9cFZIt6dzRK9jD9oXgNTtdAx-p3nflYqhG8q-jJP2rtkiI9GSNjH4RNH6g77_59rP0iZvxCm02Hpi6Xq6Nqim-LBQZeGiAfQkht4W3yISc9HLmoL_mO2-r4s702Q2o94UWzP9z8Fj5ijRNDlSvGGeOmh7jX6bn4hImqtLwvkLxVxSKDsNq6QhsFVsVFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ0qtwo9FR4VI7sk--S3-0btTq8gX3Bi1eQLBWLUpgtmQD43cfZ4TpMQlOMLfOc0-XMB6lH-gAaompFR5Wo9fqBj9ztLj3E5Dy-r0N_4dp3BUFr_pRJuh37Fv_YgJHLlEg8GbHrxFy0WoZR02Kjc6naSImR5Go0j86R_OnLF-3IWe5-oSiRMSBtdXy6Sz7gcO9C8YLPRBrfPXS3N2i-_wcut1nYxPzvu_U7a0N9mqE_w5F1sRquONGdhO36sj6yVWxg-bPX91EMjyeb8jEIIiImH2XZ5A4QBLmXwUkScIJyZeTbEbFNC8SJgZZLSvydX0Qu4h57d7tvIJH_HTF6lbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=Q0TTZ9svMi1NxxdoiEdki3-Oc6IXg6nA8y0HCkh6a_ElHlo3sO35HTldKZTf0sAFhelc7IiEre9PXxlUwKjgWk506WTMhZX18xwbqH3bhkeXB_HFNA9PQ7MdMrKq-JYyQD9S5mwneFh2Lb-ffR-ARSSk_Uu2n_YpILciFneFHaEdPeBDsQpX24SFzJs8jjVhVsOhBhDVw3ZmFIRdk0bje0ybY-LysC5FqyQ6rhZ2e-TLM5_IYQQx9BW1MEdo0-8OnTVTsnPJE1yVEXZQc9ypT7wSny1wd_nVPc2p8WbHoUcGaCHK2h9Nkw6Il19OFg_d9OWU-tPib07WH6_Z1CcazQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=Q0TTZ9svMi1NxxdoiEdki3-Oc6IXg6nA8y0HCkh6a_ElHlo3sO35HTldKZTf0sAFhelc7IiEre9PXxlUwKjgWk506WTMhZX18xwbqH3bhkeXB_HFNA9PQ7MdMrKq-JYyQD9S5mwneFh2Lb-ffR-ARSSk_Uu2n_YpILciFneFHaEdPeBDsQpX24SFzJs8jjVhVsOhBhDVw3ZmFIRdk0bje0ybY-LysC5FqyQ6rhZ2e-TLM5_IYQQx9BW1MEdo0-8OnTVTsnPJE1yVEXZQc9ypT7wSny1wd_nVPc2p8WbHoUcGaCHK2h9Nkw6Il19OFg_d9OWU-tPib07WH6_Z1CcazQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr0HXErp0ImWi1QhK5FaXKskz9qGtBkNmblpGiJ0dWxlBpx8fCCMguylE_uHh8rbsTmkwuBhI3DrTxdLKX-NPPdFCylH0gNsHjmiWuF8Wvcq5t14pQmtU82FblBN4qq7Z-9WgXNoMsXKHb-wOcbIWBYd6fDu54nzTVOU8i4_QNQctUbzpZOciECDeLIa_mys43KOJaKi_1dERLLvT1Y0gYzZJvrn9l3OghH7NNcGxg85xhcw0yjWv2__mnFy3kNTW3ihEX3S5Zk4eiGFE4FMMScHus7jpIOTsdNC6bW-yIvw6K1UogigH7yXuyIOFMnu3AASMzQKwCmQPL7BU7i-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFz35GiFm0cPuogAPWTybjwDn5fITwAQfTcYbO1wzkcBBpvMSL7A4w0j-k53cQufApMCZ3Tkg6UB1Q7QLXmaWmocb8tHi_y6rwYpg8Ul-1ig71VCwhDFSoOiR8ks_sNPlWCZZhXuwiXDjc6uRS-_ee-RZ0Dk3IHcQphYDNdu7LcGqLgCP6RfQKL6Q-AlAMU_3kqlmQiQ8CvLeBrz7tPIloD96fiEJGuw6aqlxzDydVzlhVqG_MnyXDquZfNXCU-GBe1pb8mXwkjlKhk6DrL0IeSKM87MaNeN_cVIZOr0Z3zGaChhT1zMb6rYE7FCM5lQlgr9QByD-yhQfBHJUeU5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=SP4OwcoAwLPyg5TrNFkOhlUsciut5Rb8nt2hM9hV2jXDfTcHI1-DLQScQXLPDymqKt5FLAPAMaCH3nvFb8VIK-eCNOgDJ35tslTK2DHInn33iKgNC02OyqLp1kP0plkVeUCO-QkunnRyvwlSzN8M0EzmLo-REvJRuZPWB8glnbshqZ2cuMNQbVmVOaBs2fOur4zDO95NEgafoX0WEgwQA6-l519XPKsGNaliwXU7dLRT_1WSmBFiVRkYdEjeKiNrZ5MQHK7JHyKwTwCh6zSsPXvDvOk63d0aDnmLIkU-8aee5DS81TuAMU_fYKDFIQ_dJ51ACPErPpKVEQagNfT0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=SP4OwcoAwLPyg5TrNFkOhlUsciut5Rb8nt2hM9hV2jXDfTcHI1-DLQScQXLPDymqKt5FLAPAMaCH3nvFb8VIK-eCNOgDJ35tslTK2DHInn33iKgNC02OyqLp1kP0plkVeUCO-QkunnRyvwlSzN8M0EzmLo-REvJRuZPWB8glnbshqZ2cuMNQbVmVOaBs2fOur4zDO95NEgafoX0WEgwQA6-l519XPKsGNaliwXU7dLRT_1WSmBFiVRkYdEjeKiNrZ5MQHK7JHyKwTwCh6zSsPXvDvOk63d0aDnmLIkU-8aee5DS81TuAMU_fYKDFIQ_dJ51ACPErPpKVEQagNfT0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hxvi-A35laNLiQ5C-_zinhlqdmQpjLgYjtgSxg67oq9DYF8K5gAprhcwzqHzesAHjpIl1e7Bhpadmlkn3l5FtoirDypRs0Rb17CbKWvibOcLm2m6yRITFAx0p5lDXEJaVXrhlFRABXZlB1T82ZCrCLtFJa0ta2t0s_j1pfMPp5G3fHEOkNeBolmPzGiziF6n4bDRvv-tISl5hF4CZDCHgjAQ67Al553B6UBLaKNdO6nkXHLy_1NWTMtWCOKaNyaH79Q6bsAb-iR5BawoUEFJ_7Fco4Kb_HqxSBehAeZQJWBKuLZJP82N8Fj6PaAvcmKdpcJdJ5UtcT96Ktp28ImHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxlLb2jHqV3T8Z_mX4DGK7julS3PpLGgwLp2V8j2N2NByzp3d1n9efm1nT5np6aXa0swTjZSyq4bWziz5iJSrGX-XoQON6GDOT7ddVdh891PKFrXWFFYTNdANsovMf-C1gJYOY4Lqx--SwxtRah0SWbdpxB5CXlPAGnzcRfAkLcPmh4rxv1KIn1x2u0t9WUNserldd0srsEuC-md9PCRU04iyCTRUz1TdpSWo9qGHVzPor3fA2znUbJAC5YFdLZ9I5aB5Gx30jiW00FuyS8MMd7GwJGLHjHfxbpYkoLNUBpjFAGrj1e8zVzNO0uGziy3H6dD4hg_rYxbMY85vJ_WQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=MG81nOiRp99n6OzVQh1mH-Ea90bXjFxYBE5VkQqWykO76VlCY2v2gctyRbWzYUD_vkN3sPaE8qvY1C5dQTU2W2ooYFl7KVQtJycK4zMKE-9Ze6sOHIDa6aoi3Gzhi-0Zx0VDCm8DVeBZjhsgIVNUMtKwIVyNX3_f0ZA0CBHp8D2Xy019_mxJsurHDBYFNkxrXPx0etCWhh2uP-gLmMo4QmCngDBhwiTLjx8_-EVj5YCmw1H_lWxuDwDgH4v61vmp9p-IqG98qERkBDuSN9B_2Gdby3Yym64I51DTUcJPc0NsFqziKd_km-7kUd1G806lnt9q3BhF4TVOcJ6OdyZPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=MG81nOiRp99n6OzVQh1mH-Ea90bXjFxYBE5VkQqWykO76VlCY2v2gctyRbWzYUD_vkN3sPaE8qvY1C5dQTU2W2ooYFl7KVQtJycK4zMKE-9Ze6sOHIDa6aoi3Gzhi-0Zx0VDCm8DVeBZjhsgIVNUMtKwIVyNX3_f0ZA0CBHp8D2Xy019_mxJsurHDBYFNkxrXPx0etCWhh2uP-gLmMo4QmCngDBhwiTLjx8_-EVj5YCmw1H_lWxuDwDgH4v61vmp9p-IqG98qERkBDuSN9B_2Gdby3Yym64I51DTUcJPc0NsFqziKd_km-7kUd1G806lnt9q3BhF4TVOcJ6OdyZPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECVWnJN5dWXbUYbJkGdJJMF-Xs6x0W5f3SixysTZMY7jf3M-iWvfPJNaOiPb53Ngi1gFVO9xWZrSER4s3GR69GlT2byLlFvWSgZJdF4ruQcrMQ0jaUv9HVIboBzOm7wT3zmFkt9B9zt3tTKAm_IZOJ3jdhjj3m10J4BRbpVOD4DrqA_zJPIUUbS1BfEjkzhoIbrBzEZZVQA_kAh6I9OxKhEAoK6W8VTCph3qcMd6n9psr2zZmH1pvPrgP1b3XntGY6dtYvHN6YEUP1nUKS7rwtZ34e0SDNB-R3vg0pab8mDL_9rzqpUCcDeHLaX0rPkBGU8PptJS9vbCcHTZElwUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5_CpMecf2ITl1gyzKY9FxPeXmb-MJlLwugRLfpV2OsspcgnoZFFcN5jFJLo6WKYkiTN47UjtLbNhDQrmeE96yGtVJ59iUnHFEe6fCb0ROBGPUDbAYF7xEAlrt3G1i7ZVIZ_qo98PrvumAUOu6p1qqHOLEv9QNfms_ZVRgz_ANef37zyf8jK-0egLGPnFbR_LS7-iVKkxtgf3QLThmGwY_Pb17Pj7funSxjH2rUuASyaK2DNMTkCyr-A797-6ZStpopI8V11nC5fsAWnZhtYrgsrmE2H3DcEnn737CdAoLKQaDBQZgFw4kwSiXp0E1ygoq5FisW91DWLGdHpg8Sw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7AOxXnSEJ-Lknjz7LWeqlGF1PhL0y-u9g_cfus3QUhIW9ICFKSfn4h0ualfjM2w_L6QD_d4vnorU0txmSYXIsVF_eGTu0g9ZRaQQ__0-6_Xgc6-6QtkIk4ZivfGIGBbz_F9cLJ64siSLURDdWW4Xzg6PWkr2XiypE7ZNDg6cFFaCzuWyqGLAemkvTz5xUcuidKtbIGeRDVg7L7Li20-f4ruVYjedZ6QDrl_2ibQzTJ0xAuA3Rjw32L9aulDJSa2iMpwRtN602j-BYGndFjPiqJz43WDxFaJqBkFp6cbIEccTYzXWvMHlWskKc7EfIViqJhFGj974W22f08qPw_zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKnnFD1PClsWd-WMB6G7528L3fHSJ9BxTXyiu_UyohXuXCr0b6nozqFVMj0vYXPeUzeL6YnieFLc7XUqCDrV6-A23PNxb5iqp-aN7P1X_UmpwSf3bWTgQ4cMVdr3O5m863MbQzCD3qtZbU3tUz0bjLuIZ7jJscUMoMGZF4v48sbY_dkCTomDJKfKTjQRUuk4UHQn7xTOmrHvFZYxvo8W-nKvnw3AOyZN_9SQ5YUC0K8vfkZaPmI5jeO7MKm5gDhCEVT8dGKM0JMWXRHvnu-ebo1Jwz799VrJyVkA6jKf984TbrOCkSqnUKqsR__AMo2rAU6llLmEYHSfMCA3B1It_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA3SBV72sW0q-BJDaGFnb-wgMFMFNJjRAg2wr6_GY-5IpFYxbbjj2xP2ofXvTs5UtZUKvSQnwxtUk6CDCfxQYo0q03BnsmqYXVdZIoMHlz_AZmc8fZN0jxpKz4Bwf49c-UEGoZWuIsZDe3MACNOFL8II1audNc9OClNg5iDK0TPsWn4SGGvF4gPAPj8tYHhGF06FOxGCQmYgms0GvFatZRJ2Z0B1vo7twfGFXe6J3jUC2nMEt7MOVwukiViIJBYycfMkB0BHNOccRE_DM-64VBODJAKRPbBYUyyin3qWoKh6jAa-92duxqXLKVTg3x8aUtuzJcY6Zd4wfNyJiIpjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW-WwFsvaxcQizuhL_Cggq_bJzLbXYQA-tagxt3WpLPk_ZLcRq4LJYDxZ51Vnu1j_8oS4jBalA-Q1mLmYi3rduz1OxBldlxMgF9L60bzYTYSf2DORPOaOdAl7gqGqWV-XoNwUB9EOUEihXkz6A1Q38jB2vzN2Y-IimtD_69t_H3bhkV5jwSZLVxYwa5nXc0VsL8wwI9X1IwBJ597k7knd5EA40MS4XIY_ZUeeEdEgDHJIHdhhtdb_hObGcTsFYoRjz25T7NA0jISvMb_tGhrFuZncbSxJuUP4TEiTbfKLNsiAL01fKLgfxsrg85uEvVSc9rCzfGOvG0OhnprRlAG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdca5efbLv_BXtzciNdzUro1Uh9M69OT87Y0j4b625_3O3MqPPKoaMDNv7tIBOhTezvo7M4eSLdsa4trDrwzIvUL_joGli0dZtF2ZerWjEXtMADjM7n3ylniPhOWCrI8YRFdRws3CTKd74w1_kwLUAoWg9L0d-U9Yq6tq_2E1TMZud_RRzwre2pPSXr2NIxYacdcHdSCi9enPECMSK84qhWTBTG5tuPlgpGeJ_lhwSov-977kCeKHb6PG17n1ICTqxzKlh0lq89GP_B5OvyO6jGVEfwzGto59obC5tE0X9jg2_dp-Xo12wZOnyNQ6WjOUJUF4gGyPUmViGr177xG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue4rOMvTJ1j3PRmPb0z1WWaeLW6mzsjdInUfIjUhuORg144JsdpCWa5jd_X7GXXaEtUBiYLHr_WdwwqIViOinUP-n_wQ-ziCjC_HL9BxQOmCR5_ixf96mtYtsaFuczw98pWt77LdcUjWiKWnpZk0ZHM_87q_j2jxCwGmaJDxYYBM_TOK3CnjuEabG5i9vDerkXjXTZ2EVcnvsyMeq5h4kKSwESUZn3GdTZxFsTUMgG-1yKP4JErVkX2LOfaGTVXu_BBwYpkT9m3gcZhkc0VhFozhjLaRSQJI0FsKYnNj1a-veL-Xj_vpO-GpokNFhkPCe-qHcQUJ789M6l8MQHod1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdBD1EDuOOMAc_CiUfYg5_C0W-oyN2ZRso2LnLnoijgbcdiMJiY0HqYsHg0g7_9WW4f1srTtTrcm7nbx92WXzBf4TFwonR-VXq3LIEWADQiBjbYEaITF79AWvNxyqkZmF8tITePF2XbIvKJsHXx4LJZ_HOLCMmQ57lISqHGz1yDWLtJjse22QJXpajJ_pPkaWOQ8Dll4Qv5haPJfBkDpykphPpTs12epSDKxu76x1H13APq-uBNwisqmndgGHEkKSdNZdw5SU4Emntigey7bjMCf0gKdT2Wmt3bFnFfK6sZ3DnoAMvS0wsN8cE3HFSDyjss7oKpI0JpXzFMS3JSurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYsZZmlEgFqDTmfVkOjItJ5Pf6U_KrptEAYiPhAAMThM8zkFLCfd2f6dGiVRjBxkhiWxtsDDpBgz_NSQI30K4jr9sVBvlsb6lpotZp47te8ZkrYolmIhIf6jJCzyfWfSH0_sMwGJAiWwKhyu-OYcF4yEiGd15mwUEAWKR0rSSpabINmO3nQNyF3wdwF51i90AmHMrki5Vh-r5079fRHbnqzoU1QqGTQI1JmddWG4ENVMWiIEQJZkW9jzsp736eefopccesxx-WHi3JnuqIKSTJeCTJk9sbpF8lfImKxxuXKlM6c7XJg8Dvbe98p2CBabqq35LmFOq-VS4t3GDXdUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSmk-qel5401JY6g-5XfjTDvKc0Oshyrq0aRpkkItBkiFfA3yVfkI51EEJBGX7QwkxfgZdAJ3IQ-rJAYugJR-tflG9dH0hElHb0cWzRU6Snw1yK_DX7Gils6deN3cAvWdX-Vmy9G8QnPfkKfkjVvY8sSVSB_pYH3IAjvg0ugRKeKU1xaeF32usI8060WL5DwNlGlDdVxCAYMPSiv8c_34-0DeD40ZbZX0BWbKiDINE5c6MBG0HR1joceOzJBice7jCqNFiQtXwtb2CfzoQwrD6uH_ylkwqN33Yc5BFj3Lrss-Z3HIWi0C9Fjq46YKFi8Oj5A0E7beFXVsZTVQ6OhAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdzNcGzWBvcbHe9OdYwbRRsN3tA7CLsXcqhzGJZRGiXMQ0xVBXF5OqmLD3m6QmVVKz2GiW9iRdsFvwamQz9S2zSsxHRIX4uu333XfoDDrjjdBnvOfR9D3Qia0aD8QPXT8uqhi24Bj_1e3RVlyunzGGuWLfPfDecFJ8gkvItEFkgxAqN4fiiI9LbtTYaT7YxQ7ZOi1y0_LrUojqjBfhJkCpjrhPSZbOWYt3TOcSNHKmZpw_YywNDhayg34xd3Aoajw3oDseI98k-d6kogZ5DDmKeDvo67mxsVaikr0n6-C3gqg8BE0RXu9Jy4p2YPeTuArjxxsL9Uz0o6EUdeOJzQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDUa2-e7YUQlOSn2rxcg4F2CTavpJEJ2Oznp9Ukq0LYWAX5dZ11Cym4BaYV3S4_IppQ3xTMbjGTYd92fy2jPe9bGfSr2YBfVBeXu0LaPZhRwJbYX_RYvC_ja94jY2zkqDtyO5BZkZ4-fl5puCiYWrPR_shdg9Ve0kwmit7oPRll7hBAqhUSg5yUEsMCPqLan25RCbza-a9gTb2dpefJVWa-5Hwvzw7gF92n93wOdYvykp6P7ei-rarEZCiLYC7D8UtPOXo4xbvSbwoM_IvmWP3mTJKkhekckrwhDKZR27oAASpTJTyeezLhgduG0D7LUI7p9-ES3PjXc6qqiD7wtCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po3VusECsHS8wCp7kbdgdU-s-EEiK5W3LaCPpU3uv9o1M9HiPlJLpOAHr7_0gxiSKG-hkKsD4139vfWnA0CIlCUTH3OAZBcQkcMzniBxnth3duTpQThhh8fSn8zdu6RbC11V7rAfKuCYCMmnE9iUFMdSwCWGtAeiadrycQ5rpoMFmJRq8HIBrVEoOtWOWc8vrZSvUtpP2CVBFhyqmhh2AlOR9BD4Jfr6GEuRlM3KGDajVjJuknpelU7ud6Ofbma2JJFzp_f3zY38ESfp05p1WMSSS8TGq-k4zHdwrNviYF7Z3AcZ2O9m549Mn7fSXEqeAHY1x3kvlTs_UQwH-E_fQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNf0VjUx4BnxZleS3SvhwIm4QTlitW2mweLDxtz7rgd9fZXTX_rQUQHUNjOWgWWBwot-n4Qj_SPJNe3W7il3vSImKLMypLNkU9h9uhDQHP2V7mUwOtIkvVFYhYJiJX5SVVx5TZcJbyVB1fCMQSqCPOdh-w3eUFZFl4aX9TfigqaSgxSO1HqbKOruYRplVPS8VZsp0AHErsgqvmJlGjeABd5JbEQU5U9HZu2Cxb_xKuG2TMX_RWoWdbHWpyG8QJbECUFjFSfC261RJpLwS-_I38oywWYQOWAeRHD1eL01BPB0fv9GOoiVRNeoEZojLeW4kNQEbKDxDJSL1ZMr4AVVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq24-_JM1akthzDfzDJEmOHt1bzNCdJCikhANHlcuus4veMOJxXkoMxa-BDBKHSAuWuRKQS06E2rRL4woVYBp9JYV9ntQsYP8uIdvdS6De7k6tSo0kl8EFeX4dGrbiJwxRxgtX_EwPJrqhuzunNXiAXMBCB74sN-ywtZhoC4jULWEr1ES20YlJ5yRtAHZ6-TPHONtn6bSCWpdVyz7mVD9xFyE5kpsHvW-9jt81peOYx4FYziAMOVdQJdD7UoTxxuxPHAlu2JX45YSHX_W9AxXWBUYL19-5c78PjEW1g4ysN7j7oZW60lD-SzeuvHrctjH7ETsh9dtyq0xaLkU-JtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_ZE96R1xLie_24Uqye2vuH0LxFi5pFiTJX3RLxVlQYaQKxWHfKZLm0jjYWoorVIfYK-Wp3grhK5NUnbSZQ4-_848Z0pbsjvWa614cP_5WnlI_xJcEhf7PuPq6X0y2qsrOupnH59z_82AkdXZwwFpjNZZKJB7-H8GVK5AmV-W4dxKe_6qxoYElHI0yj6rBOEWF4vfwnXr0a3_NLIU5lBfNYApmwQSheWvKKF9hssGf6qcLyH2wVP5etxV3zvxZjjP7auxaFhoKnPaOot1zBsEZw4Bfd1LzCaYeX40neTnKumh98T7Fo_pqP_0UxEIpM_Pu6U7ysQEHw3d-_xsGfVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7458" target="_blank">📅 11:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjr4Rfmg6kWvBCpHAC7WM0MOOHtpDT6FaZLtChuMoxeyo0hco_YAAAYoMsUYiAXtlks2PCgaDZMtx8YkuDqRz9IpNWMqgP-o2RYttGUUCkMet2vN-DKLVTbggN_hk2nOoVWymWyAN3spXU52ylbeFhD5ref-5kc3sBHF6Sg8Gd6ftfoOo1MrGFJZ1clXIgCKmREgG8lVBGfff7yjkOC9AozeiPUzU7QW2dTpMGdckYpOJoKOMp7KMA2IdoQKLsXzAtezMoGaiAjVPykelqwYrezi_GbJpN3EIZC2edZT6in3Q843YYRNDfmNpWiO0nC-VC8AnpHMPCB0VT68UpJrUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
✨
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدیمی لازم نیست )
داشته باشید و از طریق این
لینک
وارد شید
✔
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
40 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7457" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdAr65b94gMeyVHmgipFmhb3B_hzaFlr5kcn9RtSoRAKCWzuEYYYyDlW4jGUecA682QuHTL6XwAX7xVnVPnbcGoFSlEJUwFxWQPy3_tt0GCIaciW2cJsAOPn3cn9muoGSjy9nVWzI9mUbaO5K5VKXLYmRRayaJ1ySVbjpbLsHH1Luf5YzlBLPD-3T5f-eqIT3BTvA-OsXv8hf0AFlXaD8-k3sEWq4hFrbJ5rrtdE5ExM-YDc5WB2FOn6ubpWmZGwlvA7ce_OG9OQYpxCUZNrnlauGkOlEhA6ZuzllfepnFUfNesm8-iHf7JqKXwf7DccOPsygVLI0K4oM3WRhZcJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع بزرگ یافتن سایت های API رایگان
💥
🆓
💵
با پوینت های این سایت میتونید کلید های API خریداری کنید و یا کلید API خودتون رو به فروش بزارید ، همچنین میتونید Redeem Code برای انواع سایت ها خریداری کنید و کریدیت دریافت کنید
🔍
همچنین این سایت منبع بزرگی برای یافتن سایت های API رایگان هست
🎁
موقع ورود مقداری پوینت دریافت میکنید همچنين هر روز میتونید از بخش Daily check-in ده تا پوینت دریافت کنید
⚠️
🚨
نکته:
حتما با فیلترشکن وارد شید
🔗
لینک ثبت نام
🔗
بخش خرید و فروش کلید
🔗
بخش خرید Redeem Code
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7455" target="_blank">📅 22:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPIl_60cAb61j7QMp0B6NffA3zb2MFSwoMXoxHc5h0sBMYHf1eL69dIu9HfhtJB91R-rQ_s_OTZhZ9KznTd9r-lBwDY7wrJk4E6HQaC9uUIzts1-YTVRzCzvL4TWpNDpDxb18Q7UOfG2lPoG07k2kiNLgUpJknoyXv8teg15KwUfoTn4JAHwhPFLYN78fYIYjqRQuF2CTIxX3tD-yBazl-8teTy-9lo3WrriFGunbYCMKtOTaliPE2e4NndDKmzoVg_LUlBPVN428DlUttYhgjhF3Wi994YtSwVFPjotxQQ8iVgVwZ6zjaU-UKQPmT4B6HM1UCQu0r5UlXnIa-Wsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش منصوعی قدرتمند
🚀
🆓
Opus 4.8 | GPT 5.6 sol
✅
وارد
این سایت
بشید و ثبت نام کنید
سپس به
این بخش
برید روی Upgrade کلیک کنید و پلن Enterprise رو انتخاب کنید و روی Start Trial بزنید تمام حالا به
این بخش
برید و در صفحه چت یه چیزی بنویسید و Let's Go رو بزنید
✅
پیشنهاد میشه که اپیکیشن Postman IDE رو دانلود کنید
‼️
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7454" target="_blank">📅 20:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usreVxCLOs22B9nC-Yszl4CguRBRx0C_U7kBp5e6biNfKbBwb8cN8KXL81NT1sHfW31kOK_DbzIC0ITceeQWXT6too1pvY9_s4nv_BxDKYyv8dVQo3eNwIt1yX8laLA25SskZIKODxhduVV08roHV7hR7RyA_InwGre92TBkY-FMhnxVAaqovCOCvSa-n2CTM3O6rhIbXO6X1xhToVngIBS_q01Vr3RHQ9cT-mi1CgPKCZuA1A1MSGvnrUEyIjWW5rAdedUeA9sxV62Me3luvoS_LgF7JZAc_cMFCywbvfBvEfjxNhLkueevB51_tIv2Ge6QBztro3X9B4a19YD0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 میلیون کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
dxai-sk-5feecf996d141afae9e16f8bc072d49a692312d7452a4043fd055c37aba2c8a9
🔺
Base URL:
https://airdropdxns.my.id/v1
🔺
Model ID:
grok-4.5
|
qwen3.8-max
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/ArchiveTell/7453" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جزوه ساز پرومکس
❤️‍🔥
از این بعد لازم نیس سر کلاس چیزی بنویسی، فق کافیه فایل صوتی کلاسو بدی اینجا و  با کیفیت ترین جزوه ممکن رو تحویل بگیری!
📝
https://github.com/faithsaly5-stack/Study-Note-Maker
تست کنین نظرتونو بگین
❤️
⚡️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/ArchiveTell/7452" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان دورانِ عذاب‌آور جزوه‌نویسی دستی!
✍️
یه متد خفن طراحی کردم که می‌تونه ساعت‌ها ویس و فایل صوتی رو به یه جزوه‌ی تمیز، مرتب و آماده‌ی خوندن (Study Note) تبدیل کنه.
✍️
فرض کن ۲۰ تا فایل صوتی داری (مثلاً ۱۲ ساعت ویسِ کلاس یا ویدیوی یوتیوب) که نه وقت می‌کنی همه‌شو گوش بدی، نه می‌تونی کلمه‌به‌کلمه بنویسی. با این روش،
بدون اینکه حتی یک نکته از قلم بیفته
، کل اون ۱۲ ساعت تبدیل میشه به یه جزوه‌ی شسته‌رفته!
🤩
فرقی نمی‌کنه دانشجو باشی و درگیر حجم سنگین درس‌های ارشد، یا دانش‌آموزی که وقت سرخاروندن نداره؛ این ترفند کلاً سیستم درس خوندنت رو عوض می‌کنه. کافیه صدای استاد رو سر کلاس ضبط کنی، بقیه‌ش با این متد!
🎙
دارم یکم دیگه روش کار می‌کنم که حسابی کامل بشه. اگه پایه‌اید و می‌خواید امشب تو کانال بذارمش، پست رو لایک کنید تا انرژی بگیرم.
☺️
✈️
ArchiveTell | S</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/ArchiveTell/7450" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTfiDNW82w8RiUmnFpImvBQeHO1XoQRXULNcU3JTSyubXWonNFEE_ovPBkJ4dIn5fAb7N9zLlnEtPBYIK_nboMEjXMXW267vzIXDVsCZIAS1NkSbsoAWMMwAjwh-py5k-uQWGc5_quoeaSCcQyDs46_jaPWniJK5K_LYu2g2aIpKJLaheUiIu4calIL7sUz1Gkx5K5I486qH-2SWUzcnnmZWY2boeW7I6GsuU7ZjCB4knT3D2SU_au62iTvS-Y8LE_-KVhwlTHx0itkb5Lxj-WoDTF1BLoAW0sF3Gtk1K_sh35tmbc3CuS1UiVP4wqT7cBDSNgMyQuI8GV-TQOIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://tabitoken.com/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
20 دلار
و شخص دریافت کننده
120 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/ArchiveTell/7449" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIP3ZM7avwAtXoA1-uuG8FWmaM3R1-zkiT02JH3eoYyDQ3DSGrCKIzCt39wdTuvJgnup5zt_bYJpSFNL9LY5L0KH4kShnVD0ppE687rsYHun33IQDdj8xJlEFmZTvfXFQ8FNupiTHdWypbVsFvYoKY5c15HeS-DTaLkOPMdmVh0Rn0D2dz4pmd5cSAK-DWoyPBv0iWRH0-QH9ucVE1RKzrLoFUsZ34WOX_gqFBCGfoyBCC7NRzz8wRwLDfS316x7-5a3_9Zr58aJu-GZO5hQwb5t45MNgTJYEqVRwdOZmv-XPobDRbs6gYvlZIGQjD6inOnevoJmj90JbSDbNZKzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20
دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
GPT 5.6 sol | Mimo 2.5 pro | GLM 5.2 | Gemini 3.5 flash | Deepseek V4 Falsh | MiniMax M3
✅
برای فعال‌سازی فقط کافیه یک Gmail یا outlook داشته باشید و از طریق این
لینک
وارد شید
✅
Base url:
https://fapi.leileihog.top/v1
قابل استفاده در
Vega Agent
✅
🎁
با هر رفرال شما
10 دلار
و شخص دریافت کننده
20 دلار
دریافت می‌کند!
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/ArchiveTell/7448" target="_blank">📅 18:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjmyJ5v545RZOuE_6rJwkdc_YML0gZjbGRH6vQ5zn11GTGYtmdvgz1qwQ2sU0swFJNyzIMbAcaZ_elzqIAezvTO-tpWDMXW3dvgsaPs7Ea811mzUtQfMu0MEq5MivkaMP50uyLclOi3itSinlb44uYy3rJrKjh2R2zXwjPsEygbTChj4vaXFTwShLXtvBlUb-yVVypwrevE8T1YjaM3Ish01NlK4djFxcQeqUDdt7Tsj-iB1QexBbLX8xSTVyRkDcmWY7Q-XBzv1VDU1-EPK1qifkW-xMmtVNBpcFEhd5QE1zHyzuluYnWRsuQaGoFRy9WvyaStvri7XTSuEjF4ZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10 هزار کریدیت برای دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
GPT 5.6 sol | Opus 4.8 | Deepseek V4 Flash | Kimi k3 | GLM 5.2 | Sonnet 5 | Grok 4.3 | MiniMax M3 | Gpt image 2 | Seedance 2.0 fast
✅
قابل استفاده در
Vega Agent
✅
Base URL:
https://www.getunikey.ai/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API
| VeGaS</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/ArchiveTell/7447" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB73rAmSIhG2ixT_D6la4d5fZ-O_jtWVgll1Dmq2DSq3y27UEG-JFNhCPeT7_DkiUrCIMDmlOuCbCAoLyG4KnagVeeURJVOYjSFEn-t8hFaLZben82VnwZGgtEqUswjhdvuQefXXGITvchlV0Jn9tUkjzJqx5tsc36eOhX9qw-V7Iypq_wUFEeo2eIHSiFQVcyPoM9LS-wnB3Ip4sGFsh37Th-CpqRKyL2R54AYwVSajm7unYpEzskUBvOrOevQCnkNrTi2C0bkqvtfOjjDt6C4q8to5VHfpQDbPDxDnJvBXCjTWSZJgqkA4nWZmavcfc3mCmwJl6rh-Jq74yBvGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان نامحدود به برترین مدل ها برای چت کردن
⚡️
🆓
با این سایت میتونید به 35 مدل هوش مصنوعی به صورت رایگان دسترسی پیدا کنید از جمله :
🚀
GPT 5.6 Terra pro | Grok 4.5 | Deepseek 4 pro | MiniMax M3 | Gemini 3.6
✅
🚨
توجه برخی مدل ها مانند GPT 5.6 از کریدیت شما کم میکنند ، این سایت هر ماه 3057 کریدیت به شما میدهد
💵
😎
🔗
لینک ثبت نام
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/ArchiveTell/7446" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💥
🍌
نانو بنانا پرو نابود شد!
کمپانی xAI مدل Imagine Image 2.0 را معرفی کرد که با قابلیت‌های خیره‌کننده، اینترنت را منفجر کرده است:
🚀
🎯
پیروی دقیق از پرامپت بدون افت کیفیت
✂️
ویرایش دقیق و حذف پس‌زمینه پیچیده با حفظ شفافیت
🔗
پشتیبانی از ۵ رفرنس به صورت همزمان
✍️
رندر بی‌نقص متن روی تصاویر
📈
آپدیت و اسکیل عالی تصاویر
این مدل قدرتمند هم‌اکنون در Grok در دسترس است!
🔥
✅
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/ArchiveTell/7445" target="_blank">📅 20:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=a4smUFUspa2U0vLLjBhjM4Fq0Nr5giZpd2Mx__I1pAD3oATf9P5x8M9pfoXtjZ_DvgH2RgNjgIacxQpZ7qMEjcF5PP7j0U2Wkk2gttXRIJ04i42Se3Ujy_Xjxb_4ce_qf9oqpqgNO61oaJLmgVq0PycA6mrkY5aMH67_SsvPJXx9_EGqDIC6EfEf4o6mMVR4LGPJ0BblaHS4aLbM6sGYvkRUs_vswTdvke6RThA0Gf2Pkrlg9c4AlCVjH_tRfQxuvHdp69-vom8FMTuQqSFqRPa0h3uVeVmmq0l3qd034BzCIaUNKo7c1GD25Ny69Y-ymp-6DtdUcbV8h0dP1wMgDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4fa5df7.mp4?token=a4smUFUspa2U0vLLjBhjM4Fq0Nr5giZpd2Mx__I1pAD3oATf9P5x8M9pfoXtjZ_DvgH2RgNjgIacxQpZ7qMEjcF5PP7j0U2Wkk2gttXRIJ04i42Se3Ujy_Xjxb_4ce_qf9oqpqgNO61oaJLmgVq0PycA6mrkY5aMH67_SsvPJXx9_EGqDIC6EfEf4o6mMVR4LGPJ0BblaHS4aLbM6sGYvkRUs_vswTdvke6RThA0Gf2Pkrlg9c4AlCVjH_tRfQxuvHdp69-vom8FMTuQqSFqRPa0h3uVeVmmq0l3qd034BzCIaUNKo7c1GD25Ny69Y-ymp-6DtdUcbV8h0dP1wMgDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهندسی معکوس پروژه‌های گیت‌هاب با GitReverse
◀
☁️
بچه‌ها اگه یه پروژه خفن تو گیت‌هاب دیدید و خواستید دقیقاً همون رو با هوش مصنوعی (مثل Cursor یا Claude) از صفر کدنویسی کنید،
gitreverse
خوراکتونه!
🔺
چیکار می‌کنه؟
لینک پروژه رو بهش می‌دید، اونم کل فایل‌ها و ساختارش رو آنالیز می‌کنه و یه «پرامپت» جامع بهتون می‌ده. حالا کافیه این پرامپت رو به AI بدید تا کل پروژه رو براتون دوباره خلق کنه!
🔺
ویژگی‌ها:
پشتیبانی از مدل‌های مثل Grok-3، Gemini-2.5-Pro و GPT-5.4.
🐱
دانلود سورس‌کد از گیت‌هاب
🌐
سایت رسمی (نسخه آماده استفاده)
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7444" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
