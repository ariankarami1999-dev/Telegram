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
<img src="https://cdn4.telesco.pe/file/u2rXeEghL_mkH1EaANBtBOc8CW-pSKVcD6hf_b6bjyNAgsNRfSWFc_3jqg_mTPyT-Vgx5tfxg7mNgRWN0FYLD5KMIZ7HO_NqtTGhIPa7dyyyhYDAK1R0l-X0wWCiu-YBxtUjR8fUhesxlZfxDU-Nj986gBlQDIJ8PYjaa4xVHCciRRZGwbZdqFBeieCkCJKv18xktfO3p5p7QZmR6_sJlIN8U7SDxM_Mz0l2A9qQHsGu_RZOAU30Ue3cu4EeimV78HRUT_U2MnAwThTlTY6Om5RNkjHOhNhG9PxqtSgKmPy7MiareIxyE3Uyx7cWuHGdNvEfrpVjoNRDt3Os7CU3eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.68K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 08:52:21</div>
<hr>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sadra.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">همین الان ساختم
نامحدوده
تست بکنید به احتمال زیاد وصل باشه برای بعضی مناطق
@ArchiveTell</div>
<div class="tg-footer">👁️ 695 · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌐
ابزار متن‌باز
CF-IP-Scanner
برای پیدا کردن سریع‌ترین IPهای Cloudflare منتشر شد.
این پروژه با اسکن رنج‌های Cloudflare، بهترین IPها را بر اساس پینگ و پایداری اتصال پیدا می‌کند تا در ابزارهایی مثل
Xray، V2Ray، VLESS و Trojan
استفاده شوند.
⚡️
قابلیت‌ها:
🔹
اسکن خودکار IPهای Cloudflare
🔹
نمایش پینگ و نرخ موفقیت اتصال
🔹
مرتب‌سازی نتایج بر اساس سرعت
🔹
خروجی گرفتن از لیست IPها
🔹
اجرای کامل روی ویندوز بدون نیاز به نصب وابستگی اضافی
📈
اگر با افت سرعت یا ناپایداری اتصال مواجه هستید، این ابزار می‌تواند برای پیدا کردن IPهای بهتر مفید باشد.
🔗
Github
#Cloudflare
#Xray
#V2Ray
#OpenSource
#Network
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
همراه اول بسته نامحدود شبانه که لیمیت سرعت از ۶۰ گیگ به بعد داشت رو حذف کرده
✔️
بسته های حجمی شبانه آورده
🌐
100GB
💳
49,000T
🌐
200GB
💳
69,000T
🌐
300GB:
💳
99,000T
👍
خوبیش اینه لیمیت سرعت نداره
💵
کد دستوری خرید :
💎
*1000*252#
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤖
ابزاری جالب برای اتصال دستیارهای هوش مصنوعی به شبکه‌های اجتماعی و سایت‌های محتوایی!
با این پروژه می‌توانید به مدل‌هایی مثل
Claude Code، Codex و OpenClaw
اجازه دهید در سایت‌هایی مانند YouTube، Bilibili، Xiaohongshu و LinkedIn جستجو و اطلاعات جمع‌آوری کنند.
✨
کاربردها:
🔹
بررسی نظرات کاربران درباره محصولات
🔹
جستجوی فرصت‌های شغلی در LinkedIn
🔹
جمع‌آوری و تحلیل محتوای شبکه‌های اجتماعی
🔹
تحقیق و بررسی بازار با کمک AI
⚡️
گزینه‌ای کاربردی برای توسعه‌دهندگان، پژوهشگران و کاربران حرفه‌ای هوش مصنوعی.
🔗
Github
#AI
#ClaudeCode
#Codex
#LinkedIn
#YouTube
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGbhIJFaPnE6CIHVxnTfaKQdEAyJxPXZAYv1M_2HX-RF3QGOVCujFHgozVczsq4Maut7mJyP1Oxt61g6Ge2qerxuKKTd25tOrUKV05i48Oq0iZ475RW_Svf16DmiV7XQvkqAmHna3ausCQzWnN6MqseK6yt03Iba_0qblU7it-QlEDVINlygJw_1uiH6gq3oLgNlL8FNf71o5sQn0CSFnwy1BNofAtwdZ8ZBM2Leg5ClyLfhCh9OgjcfvZRwwU7Z8CZVxRevTdBbjPViy2pGd_aDq_BlGtBh-1Ddc7EhIzQEBpoFr3tei3lZ6QuQTljBtjOnnU2mCo9jHf5oO4IeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdwMJb6GTRdtZX-uUvpefGxMzdF14c6OmURTBF_NScsN1xkih8Fe9Gi9kpZAD-nkaDaOwrm7RmLRfGDzJchaEpA3vW3oQkgEJ2D52B40G0x8kC8NoZNvV970EhctlMe4DxncZJMIlY1Eg-_DylXQWYEph7WM0W1yPHubrCOAOljyX5z_7YzpqWbTTPEHH58itGcA7Wtn7TWT1SoegQTey7ayWzm5FO_OKu0i5Z3L4_My7I6xJNRVZDlrkmChkirHwYFQeCxKnPYzi3oeMVIt50cPyf3vh9hEVuf02076GU0bpX6uhl1ExWgvD0hAkc-Gt6_rxPJm65L3whTSKtzr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KI1LX1WL3EDcNYUX-y9Wkcbi1R53MQXhqd5KfwkAqJj99WvOY5wN17qW3ksT2yav37JSYV7_F_hLbA-mpfVPWerH-icTnGogp05s3hyVmG-obGMm8T-685N2EL9mC6LUg7nzt7yYFS_2TuUyNYpZureBi64NOkObexj_oQ0JG_Gqua3PauPRCZwzEA5rHqblSFEeQtW-bgDteSyo3JbyYA8DGEWPqK-SN1gCsJwC2hugZfhix6kIEW2yuaVWiYBesSsP3p98pIvsW-KOHzXby6OP4p0a1nQUsXh9h1sX1hqH6Zec-AZ535jMk4eBhYDSmHr7GF1BhXmamRajZHqVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLqgxgHiqRkZUp3PTSe6Ux2lu4iXmCimszOpEGpmIXVB3P5nLOdIo6YPqjdCnuwk72vhEGzn_vUlf55vf0fFPn3yB_ZT0G9DhGcafHarAcOY-4KtQdOgcu4WNHzFSENGGy2EY-Qi7tGltDscRaKx0S7XyC-Oao7U2sZGrS-2IpnDFxrMQzBghAHwGNlsXjb9_Bnr-67XfrDJzs0Qe9LTdGnGijU40P9ZsWBEHFA8t6o0BD0U53vpupn20WC2Gr9npgMlUiaGg9eenapqlI8ybGJ2OI2iUr3f41D6ObhtTzvPWCn23fIP04wxn1v5LmCR9deG1S5pK1DBPU5ljh5BfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=rXJ6f8gfaGFH-Sojul8wYhNeWit-Kxlrp4lz_rqzB5YAMZEtXGtsAoCkl-b8cNhCTCXLER6y-EqKg3kBrphFRSmYv6zq8kvUHHwbLlXsOjlQsKyVW09kaLJkT1txaxkUG2LyXpZGkqf5BrQD0ekHK859Z6qt4NSp3IetKhxyWxErH-oejIVInFDGSIL8Y-8BgmnnT5mUZU_Osp_VR2rl0n2QwQLGGFQfDp8EPtyMipnNXM4n3R5aPhN1yrrWhtjCFDs1exk3IYA0B_13_km5qkQ2hMsDj_7jX43UNarsVqV9Qnx_cfbFUOZgfa5jp64wZdInqjpOelYs46aBULdDpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=rXJ6f8gfaGFH-Sojul8wYhNeWit-Kxlrp4lz_rqzB5YAMZEtXGtsAoCkl-b8cNhCTCXLER6y-EqKg3kBrphFRSmYv6zq8kvUHHwbLlXsOjlQsKyVW09kaLJkT1txaxkUG2LyXpZGkqf5BrQD0ekHK859Z6qt4NSp3IetKhxyWxErH-oejIVInFDGSIL8Y-8BgmnnT5mUZU_Osp_VR2rl0n2QwQLGGFQfDp8EPtyMipnNXM4n3R5aPhN1yrrWhtjCFDs1exk3IYA0B_13_km5qkQ2hMsDj_7jX43UNarsVqV9Qnx_cfbFUOZgfa5jp64wZdInqjpOelYs46aBULdDpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
Fable 5
اکنون به صورت رایگان روی کامپیوتر شما در دسترس است.
توسعه‌دهندگان نسخه ویژه Gemma 4 Composer 2.5 را منتشر کردند که با داده‌های استدلال دقیق آموزش دیده است.
🔹
تمرکز اصلی بر کدنویسی، تحلیل و درخواست‌های پیچیده است.
🔹
کاملاً به صورت محلی و بدون نیاز به اشتراک یا API کار می‌کند.
🔹
در قالب GGUF برای Ollama، LM Studio، llama.cpp و سایر ابزارهای محبوب در دسترس است.
دانلود این شاهکار
#Fable
#Ai
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNByDiSLOTGwgRzOf0Ts63txFRwuD8N8ihcYRZ4qSqF_ANlOB2EpM2nuhKSp7bCk5_V3FL0IaqIJfxPO2_n8r1cvTZexrAbi-z-e2WqsvTS5J_vqvh4XfNb4tsHCAEkE4bfYYn-m96EvwB2CYm57BHYaGGKwAEYcu8EyM0aAkrMcK6DIdhryailMyUmf-tCvEZsK1POzu_suPg3eFrVDVRl6i4eb94FOWg-SzxNL8QeMLNKQ9JsHgXqIGiWiYjS31Fv7W3nS9TScLnUz4xk5S_AbaDp35nCKaHQOwVCDzpnyt6Qd54ZEthxHO5swjHcVtE5b6n-hSeffBaUkilrTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=tsPUNF-5Lbu4aL97XpzFd1DppvmDPKLLmGrQ0xpB27ysPCMEW943SQPPXKKs1IPAwpqvgfnBoWQVJl2zDJjHI5rUbbawXaCpmUggFmuL2eLyt16WWi3vMUTI8gCq6nyvoBLDK0nCKvT7F7UCslnI6j0I_N_JF_WMCFmoHoclgwzrsNVGl683Cl51eX1g_GbJqTOjWxp7b-0aChJkktizxSMm18yCfV8gF-A17DNavmgrFtrrshDG3p9y89YaHrxStZm6DapRkvF42XaEtUwzipasmK4lIRTH6zAQIsZq9WjhjoryfcHFQgsUeiKGkOzm0JHl5WSUEUo82v3LXoVMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=tsPUNF-5Lbu4aL97XpzFd1DppvmDPKLLmGrQ0xpB27ysPCMEW943SQPPXKKs1IPAwpqvgfnBoWQVJl2zDJjHI5rUbbawXaCpmUggFmuL2eLyt16WWi3vMUTI8gCq6nyvoBLDK0nCKvT7F7UCslnI6j0I_N_JF_WMCFmoHoclgwzrsNVGl683Cl51eX1g_GbJqTOjWxp7b-0aChJkktizxSMm18yCfV8gF-A17DNavmgrFtrrshDG3p9y89YaHrxStZm6DapRkvF42XaEtUwzipasmK4lIRTH6zAQIsZq9WjhjoryfcHFQgsUeiKGkOzm0JHl5WSUEUo82v3LXoVMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_8BvziaZaO3LbXm4gEazz8XKzDHdva7vn6MMtAFvLtqXKV4Wc_ADT68HlWzGbv7hY2uFHwuFV-uyAwNludQsaBA-l887qPv-yYwXbZ1DutKDzK1No7ZIw5wjbpU742PESAGJ43ueLbFJ_VXFYSIASVgukwGhYHZ4ipBzvxErUKIUQ7ysRU9Hm1Aod6giej-Emr7Bfs8J9E5zmWD8Uqvpx4J1CfpY3U1ODvcC5cw6abc8i8_infYeJ0KR--x-3yT4xfAeh8Hhi02x9N4exwte7M4RyK0z7nVtmf1ulvv1BZ6RMRndkJ0EoeO2y6LCsX4mtVF1CPN7SDZPvtpU99ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hdG-I35_sK27cCYlIeL09JGXZgrg_RrSEY2A2YihJb13Kf_FoOSpWQ6yc57Cz3O9PcVFSiigGJDmabHsS5oCW-LXsPwI5KGdy-m94QGpd_zPzPYuVl1TyjBO8QLodk9EqUWQRa0z7k7Um6a9--2DSZ5-N6dQ5RQ6TjuXlspBDJz2j9VhCVL-KWTd1qDxsimFZvnRN8DDM8nIWTDW-uK2W9ovTRBPm8uYk4i4J3jAU5xbd3n87IBiguRsEfEFuphB3jDzH4Ec9rweqF6IyU8Mm4PBvlqt8LyFKmUGeyezBuolMbkYEoguSTGVE1HzQEZwnpchT3jVly-WOvd-YVo7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2tW8-lsctRQFkQGRZJ7Sv_U0spt3uawjiOr2EPB5kYkoAG_T_8O7d8Q8fIBVNDm6JiuTu08FgLxqkt_ROmfssMwz8c1bHl-Zfy_ntjx5lMJFawsBTA5JLe8_tejFIlR9nTt5RTRAyz86GxJJR67wJcJ9l2OvHCpVJoRV7lVBTAZ2z7fqfai44oBm2i2IQkkzuOUoQxZwL2Y-0sMMC6JCyJ23ZNBSDgFwkYAEVB527AszIzhHD_rcyj48bLh_GdsZ5MRFHOmB1eogG6HdNABJ0rM6xgjz46cdXhPuQynKUwsAbgWtsEK_oFk_rTKENQZ7f-Qau3G0r81BBL3NVmf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcHKROgP86DBsh0uZJTCj58Drmk8TySJkKhvWDW9SqXYLKZnXXI8Sa3w5VzK1ezsbj9KxfZE4aP7Rzs4WIMMuEp8NQyMf96hg7zTUMafjl9aVUpkC0TohibWYGZd9Dfobhgw7ivWtpjjp1pHuvdWMI91_LGSM1_bykYVa_eQfjVZgiKh6dx71fBRrolIrXVsU1cohlaDWxXzo_b7MtMSwN_jCJp432ah0YTA7c1eocb1ed8-bVSzzlRtGpfmvMDkTdkomtKtoqX4z0YDoGU9QliHhXh1gD5h_tcf7suK3azhaAHvkmSO62Cfr2HBgBIVYYDHWLnvjbtTABSFTBJJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWfVPapZ4rpbfEgKhmiZrSEkPVFwPMuXrHONEtMlHMuZqtTTId2Rrf5Bfg8DW5l1b62bar3iD5Puf12hGZm4GKt5MvxNemU7mpr4PQz18n2CWEroMdosadX9eGiUokvcdVZK_mDLaFHdmGlUA83iazbCv5p_gaCBy-cUIGSfU6KFRdrA_MSWY9l7z-yR2iMj4XhTWJ8BApCSccfT7FCo9zSX4-n-ApnvugKL4RImkt5ofsFSCxMm_s_r3L62V0eLLMb1UceTPFzlHMlAEkD4eFUkoTNb8om3HljVRospyio52Wg0BQjtRiBLeAH4HHbHQZsyewDGirdGi3QWDX4YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-czdINQPaEWd15fd6YGbwMaZqoMCLiEue4fTPnoTxGyU4Mi3X56cMpb6iLifFPVQsTYhi26m0kgmzLq4lpGgnZ9UZLsdGbfk4VWGjIX8GwisvuxePj2DXR-bvDKlNCXTND06-2XGY2KvZp0W5DLcfZD3pK4SSzd9-YizjoRTfBiLowbSN-cNDAYTJL-JqVwccVv03VLmHpHUsNHgbx6nLsxNA3kzNqHNm4mmPC3WvlKZDKoVstVSd7wjGnz8aQ7FUsyY9iKhBsYuqaJdwaQFTWbVRpP0be13uBcKFylkbwOF-s8lyqAdLdkosmoJo3Swm0Vt_4dayr6DybeNtWFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTwUXMFmx0zusU5pPUHvHorEKZFxGs54LUbDvRI94DqLnG9U3Rs558w9obTuoEhZgdQ-46snQBMFbBA2KAHdryAZ2QIkzZ7ieI7-FSS0ROfEhpNlOE0L87_UZw_oTu7CB_CMXXYg6FLvtblCmNcjyY_HMfGPvyhxiBb3sXzsaly2OyGm-SNEXpODLNoQIRnxKCd8DCmUVKXijvC65WwfUTZr0dyonvElYIMGMQ4PNeJySKIjyK4usYp8XC8UQObR3eemWAmg-MadkwMBXS-F30VWEoi89KNrRE6HS44FhyODWiVVUYB8C3tk635urwyBuJqN3zEru4xjnvAWFe0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_hjzu99hzd2blzu2dJA4zJg5F_GBRu9wc3QqXmD-mMI2gkP_Bwa0v_izZyEObC0vgWqR8YzwxS4EqIbEv-bMbBmUaIIzTscmHJxa-PKX4T524j191sYo0Bz5NqhwwiayMCD0o38UIPG56jOIWJCShp843bZO8kr23ba1Q1GihRk7jFmR6puvyyv5Nat9J8Tb9byiywmVDK7CL1FKoH6dXsInZ1S5exOtwNRMabMBqwJBcydG4hg_UV3k5VnNQEpVCJg7l45pjMvQ-G3V21dyuX_XL1ilw4k8WtzCc1o3zHLjBTffwewc4fVMuBWcRhhTUIQ94mBAYzLO8-ZDEVrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHWj-iecldTIeUYYFcXMeqd4IFTekVxkN37TJNnSiLQ1HJN1_Xdaro84P41FoPmlXpn68mhKNGnCgeRRTWOTzI5YfSIxSahmXYioPh5UFgWBUkUjEAppokpQ0HuEFz9xsN30NyW_k7pSxmOSWclp4HsbbzTxaGNCyepg_DeJY_weBQYZ1p-qFkrt4TICxDirnHOJ9XLcrxIpr7KPxwVlYGSq2KMHz7ZQFfcbOzkdbZQiqPPtFacf0CYs5IGJuM3rDC8491u53rxpUlzExV_pyvEfZ6MbZdtDXp4vQUSyH-AXTNZppoak-l2aHpLkCxK_fQFF5NTzzNSdoPHR66xXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7wlTxEyJnzgVBFDgL2osFtOw6Zn5EO_NWVsDc6vzIoJFBcS880iJNMzINOKvwXXnLdpouP4QUERl9ptIBspmEzAR7TIbA9Nx-YaBkFqqey8sYJFU1utvEXWotvDqdpnJgX0-npLQOwtyZzmcba6vZIQ946GRrXvU3JptlZUEM0ZVXC6CmcWwIc4oVOPd5lDl-jMgsY7ob0lxgByqW6Oe_ewX0YVWRBtFtQYQThGzzXu2HX1z_vvBwpaaOSCzPHl3PBS5D35hY4S8G1v2bvFTXGNwV8X5Z5zsyoom1spHxUizd13RpDzaRzYYZjU5vaF3G7PmnVWGSrTdqY9MbqdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ8lcqao3XlYAV61zxBMmArpvec3UpM6vuUAeGk3gHLGSewjwsQs4XB7eL1G4fAEG-LLqkfKFpUnvZYr3NA0NppPHSmecMawDJYUHJD4meokESiI5_o5QTbCknnCUFE_vadNBM50vDOujeJAqq-RPPK4X7avMAH5J0k_6vP4FURfZJiJjXXIJNTz45-fcgUIdGnHVWrxi_PmBvRGGx1unkU6EsgX1MDimbt6ZMFHAiWigYWn_-dcxm-QFN9Q0bs3Os0ajdZK5R1JFV6f2OKySlF0VHLXzI5r3jIiuFvUuun8t6JuPe7G2SpIglUec8VxyJDg1dEYZ4AX1Z6TtJxO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=BdtRBv6okMNUUB7E9sugW_YyBPhmOeW4P86ICoD1L9mu_SS956uttRpoGt_F0Sf4e71P0ublaKQyTdw_Hta-5kUZO7lSYNHPiMfQ39iArxLPNqW4NsMxeDmZcNvdxUfSgzXG-5tiQ33q6S0kuF6eZRrxXO-cEVPI09nDKNUi8KvE9LCMz4MpWULk2c-hUQukFgSdgarJomE9UuZIHp_GnxrDCR1dTj8jVKPOKqTC7NxhXg-gVE5LK2lLeoP_nNDJlgF7iQcWh53sShVRghdD7hTT35mfngc-6rnQUkzqtfvjVa3O7BS2ZvMfXtMk6TikbBtri5GEhPz6JM9KCenU_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=BdtRBv6okMNUUB7E9sugW_YyBPhmOeW4P86ICoD1L9mu_SS956uttRpoGt_F0Sf4e71P0ublaKQyTdw_Hta-5kUZO7lSYNHPiMfQ39iArxLPNqW4NsMxeDmZcNvdxUfSgzXG-5tiQ33q6S0kuF6eZRrxXO-cEVPI09nDKNUi8KvE9LCMz4MpWULk2c-hUQukFgSdgarJomE9UuZIHp_GnxrDCR1dTj8jVKPOKqTC7NxhXg-gVE5LK2lLeoP_nNDJlgF7iQcWh53sShVRghdD7hTT35mfngc-6rnQUkzqtfvjVa3O7BS2ZvMfXtMk6TikbBtri5GEhPz6JM9KCenU_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isyuEzOMgh77I_G2JQCX4XQLo3bk11lhiscVkxpbLJy1k1WAqODJ3iFjFvMsmx5rBa-_84J_qSOy3DWu5j_DMPYSTBJK74D6CIEoo_Hl4mZZFmeATIATcAXHpYpiyNN-FhRSstJtHI6CvQZureyKnaiKBpDjqQ1KNcE0nXUrPAfcCspiXY3YhLlvGIcP1xtrsPQpHH0_qQwCSobn0KYKdLVjXTZL1AKbfeiTBEfjcT_n7tVBzO9jN0a3xVn4GB_riQyIz0Yh31uEbMqXuOlPR_3mq9-QIsYD6xE4oXx9_7CSpmbkEOIipPqmXVVKa0u2TfJm8q7F_1h15Tvx9pdmOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXslAdWBjSsFYxgI4BJPX1fAd9q8R82O-v5dG5D8iO8MbiqcU6c376tay6P1a9jnGLyt6c0gILA6xyWzOXxbi8iY1cPkUf6lIGzw2YkuYeS-5KfhT0gWdEQOa2gqdf56HBpEaZvxmXk-LU3bKsZ3D0ZZQ8boP7I1yK89JK0zFQPUb8aqlz9GRQ0HH_bOfgCYyCAlVve1k1tO3-AzFWPkxDo5DbhHAF1wU6pgzObal_gJVYZFoyWM7aGA3Iu-X-acs_XC107EeUhMWlSAL99Daozmtr0TkzQojOGN3nej7VKcSCGf1bCjtgtjSy_487nhaueDpX2-YDi2FgvuZpkYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nsWjUdApvHU-uTERkX3b95NO3zI8Nj7e2oxX0VGQft5UbI_c5qp8H5mOaYzxKIQSwoVgxl6CqybYndi5t5OMEM4XpC3-n9mvUXLIcEXaUpLom9Omi2wU83bCqIeEPdmNp3ZDkdxlbiEPP0WIzstpfOMuQ5p1j8lXxKlCRanpx3MdwOMREUUFhKJWvAzpBd7QAmQZwa626owPFic2KzL-JPyAR361xuENBO1juiOpV8N6cgNfXg3arXlHPm7oZvgVa015rPJ4RQ9WgBT0xcIVoV0Mdg80K8RIU0jR6AK62kO77d7Yci0XLtLcRcxzFh1glyQCw1y4PqHR-aZi3czaI5olAS6aiS6DxF52wI2909wkiM5vrsQxiYVPEaFgATGXGCjyEQr2GFhv3kA6idJy22colhvPE7X3ol1BxWxR9hzP093idpaDyRpH9FbCxEmFL7oPup3FRqyQ9zINCjhylXBMZutRfvKoXScC9V33jnn3oNUaeQnINH4CqZXwLWNTCNYHxUkROoogrXtBoHO-ZcTxnJxBsJi-BTcLw8HyuPp3Oc4hQvfevYRXluPoP3zx3MvpFHA_HpL7Ao1-NvwcOYZkXRCo6iHVSV_o1Niw02eyWqJJg3aMgHAIdTnGeBoIr3MeFX_YMi4WdivifB7zrG6sDgTugoxxwjsXTiB11EY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nsWjUdApvHU-uTERkX3b95NO3zI8Nj7e2oxX0VGQft5UbI_c5qp8H5mOaYzxKIQSwoVgxl6CqybYndi5t5OMEM4XpC3-n9mvUXLIcEXaUpLom9Omi2wU83bCqIeEPdmNp3ZDkdxlbiEPP0WIzstpfOMuQ5p1j8lXxKlCRanpx3MdwOMREUUFhKJWvAzpBd7QAmQZwa626owPFic2KzL-JPyAR361xuENBO1juiOpV8N6cgNfXg3arXlHPm7oZvgVa015rPJ4RQ9WgBT0xcIVoV0Mdg80K8RIU0jR6AK62kO77d7Yci0XLtLcRcxzFh1glyQCw1y4PqHR-aZi3czaI5olAS6aiS6DxF52wI2909wkiM5vrsQxiYVPEaFgATGXGCjyEQr2GFhv3kA6idJy22colhvPE7X3ol1BxWxR9hzP093idpaDyRpH9FbCxEmFL7oPup3FRqyQ9zINCjhylXBMZutRfvKoXScC9V33jnn3oNUaeQnINH4CqZXwLWNTCNYHxUkROoogrXtBoHO-ZcTxnJxBsJi-BTcLw8HyuPp3Oc4hQvfevYRXluPoP3zx3MvpFHA_HpL7Ao1-NvwcOYZkXRCo6iHVSV_o1Niw02eyWqJJg3aMgHAIdTnGeBoIr3MeFX_YMi4WdivifB7zrG6sDgTugoxxwjsXTiB11EY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=LPmjtw2S8dM0j_6EPKFtcPgb4WmGyrlHHnZO7BH93X8op_8Ib84YdvOjtRX1EbkxYZtlJwfOXO9lxvGpdq0pVbNYBPLXF0xMcw5YgkK2AgMfO7zwGiOv8cKyug8fjfAuP6h5WLRJsagQYT1D6i6bGvjf4RoV7Pf_PCams_ov6yefWOGznwye4Ajiah1ec56aRHdEolsFrPscCOqVyngeE35YLfhxELBZAetFcmO8LlQTeDxRpMXnJoNtDj1UZX4zpWW53QZ7NBuEmddegrsmq1Ek-nIRYboxcKKgX68LVq39ibH1cP3iQLescGYahgTn9GopBFE4lSQXuYqyjvtb_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=LPmjtw2S8dM0j_6EPKFtcPgb4WmGyrlHHnZO7BH93X8op_8Ib84YdvOjtRX1EbkxYZtlJwfOXO9lxvGpdq0pVbNYBPLXF0xMcw5YgkK2AgMfO7zwGiOv8cKyug8fjfAuP6h5WLRJsagQYT1D6i6bGvjf4RoV7Pf_PCams_ov6yefWOGznwye4Ajiah1ec56aRHdEolsFrPscCOqVyngeE35YLfhxELBZAetFcmO8LlQTeDxRpMXnJoNtDj1UZX4zpWW53QZ7NBuEmddegrsmq1Ek-nIRYboxcKKgX68LVq39ibH1cP3iQLescGYahgTn9GopBFE4lSQXuYqyjvtb_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPmru04ZcI9o2ZzX3iqhz1lsSHeX_SGx0IZRaUWQ9HGdQAP3stoNFubJmqpoOZTDsY3PyQ_EMWWK5aefY8GzXh-5z3TnyP7fGeaifWfEs7bEougeriKsoGNjXehBfExnqvPVq3otVZouVZCZkcLdrIsJWGI-vAuKqZ5hYUUduVfJchdEjukd06WS9jOYALkaazXTRMbelAK8Y0h65Lnx4llL_fV0rU5Oua1ctr61BnO5Ek9zfy9EQWr1USpUSDQM4oDL0W74k_CuaTMQ-0ST2WwOQgGLG6bdujSUCJzYtw81O7E1_hfltdB_VzNA82g8YBrY9scp1q7bN-AUF-jfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeAH_0s5PQTpoUUXMkBtEXOdc92TW1XbUmr5rgneaC9wQRNEhfAKeZIFy7KCsGseDvbD6uQBbw7odxW7koaDxtMl1K6e7yFBKHOHIi1XUWr3MrlSr4C_5tw_FA1uCSc64aZOVEOMo0HEhltITbSPQFU1LzG75pcfPLgQwsZKFELd7Y1EAtGy5Q3ycXer3iwFy8pros-hAczeWbFSFWXwO1C_kf2yWtHAsBUlhh9amvjGAD5tWK1t2UGr6yZrTNBZCXXT55HCqjiPEn7xmJ_lmkhXpnn3MVww8eaavAqEuqYVWoA8Dhtu9V0aOIdLkhgqOAtxnE2chs3AUZnswXKxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXTtXKrmNvDvgJp_QjE01_auUICiOZ45AQ47OoNjMDUXgonulwWT_kzkJ8izpBh8XmMVZwQaLct6b6ckGvQmbmZD32AJQhfQP2FG96fEiL1Hjr7PdtfXLv2POtKFbzKs3EISTrEoUgfhnrEZOxtDCKJ_yOdTasV1WTjv64QGxbKFeI_1rpjmnSRhhLrFt0-Bt4I1X9R0bF1LmVSYolgEbXzqcAds2C4LeRd5cVr2BRGMRxMw35swT3KbPuiPmTucDZsjDJWt5ll6qr3lq4emlkgfZxvy8ywDlkXmlLtHQ3uslqWBjcc2CQvrTaWccaTL4byS7xsfnH4B8A3DclUPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVYmLsDiVqInQCwYvgSFHp34vRpWt7-Mzgi-dX96f7qz6pJ4Ojq0rPUIuVHLpE5P3FKyWGk9-CLV50eDmyEZf_gyrKzFbJKoQfL-N8tfNgpRVwmqF_Ju7pSmcjmFpVLpie38jwStQDEQZN8tM69kAlKFt6X3laW3Gu5g19hu9np08Y54B3M4Fe18mU-DjJ7fxYvVy6P9zM09esHolh0sJUriY6mGMYxfxoG0e3m7-VPJWyGwmaNRLG97Q025eoX-QpLFoWKKkJYbnaIGTBZ-VCnwQ9NpMDuiVpfPWkisrz69-fjWAYvTzm4ocMH_Vg0aA7YdIu2Lxy3DgPXKsYSQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hysYYL5lhAdQPLhKXFaKW4Dj9CL19ess3ztmJxEmSo0daBTr60y-K_4tNM2I3NeVUgfouA_amLCckbrAuMJ68VbMTkGRtKOQvMX2QyyOcvWbNPHCJiD77WEnnbc3KHDZood_tj9rpB0hoqYnG1jDzE5WTueJV4Hi_2X2umqj7BNty6QVmedWomeVp56n8FIw_smTioIMJQVFRZKbixBpvBMhdquFmQoIwzsStbsUhmi930xnVBhL2kDVTKOkyHpohP69px3QSN5cyrLCmaw6wcJicF9jixMkJJ2-jWKqF0d2gUVaw7FB1u2xl_FbKRreyCipqUW_zUVwwuruuowGFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7CRXGqusyXlmH_urnf34M6G6rXuB_5H3q3vCG-Scl_XJoXOihq1R6t2M26V9C0oueHgoHU7-hMDJsvNxrRchs27J7tbSdm0yF1TXRJdKjwKJ1VQ9K2wOFLhYXiKFGnGoCxrXVbfyaA79vhqhDXNcwMCNZx-JpR-hi3UZ2tXDaOtypUR18Eo6ECbu80EYuqQS6wfjo3S29zpNERc8D32N32fP9KW2qqOfTst0gUqpnGPuR-EeZGxZKmrP2HdqNhDRdluu1vcsuA9QsuHxVzNa_dEuMPTlGCTW2qFrAY83UA076ZAhkmi44ZTDQvCnA-AUPZyLkwKNQKgqlSl19X0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBeAs8ZJmJRr7Vc2KbfrAz_ali5m6eREZAx6EHBk1ZFG6h-4trFdEyKDj8AGziy_aX7ErcRPZHRvk_CZsh8Fwn_vmEkTthb0w2_DPSghdsrC61a-GLNnEWsQUoAd3UxskexOp0vSL6RXUOrmg75Ku1uIYmkURRco_2qaj4UYpajCHnUUTgrGnCytNJAhBefBwsl7tWfBKOIQr19ntacNpVW7J8gwKluqfVytwY8pYyUl-easvgcJt5YOCbocRxRf8uEnyni7qORk1pgl5rXBc0y0RFB4nZi42P4l-HXsFHd-u3zhWKr23pqMr3pVOaWkY_ljJiU06WOYwiY6JUznIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeRg5VXaDZ-W1sDYRDWHLW6aFrK9As14P5gRHqcBBc24tUozBZvE-eOUbD3ydLuDvW3wG3CbSZ7mbVnwSe3RUUSp1PF28iicTsqQLB-r8xtLF8k7MYpSwZ-oh6Mw8skZjxC8YOH4_xalUZINooTP4wD-nHlfC6BwtMCD-i5eV8P4qN3w03OCFtuVAMJeiOpgjzDuSzOtC03ZCW-4jHKzw5WEBbmVubKisivUvGc4OR_rCqopSuctb-qoZzDuO52_3KPGQTivzcWLqIrNbF-g09lGv-3D-sxJILHXbx5qsNrElMmkjb2b9wq6fxxvo5lOAIsZAnumwZFPIctOXNPqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHQ3xVgtnrrrMxgz-DxOPJXIrzoVn9bC6IX3fTontQ6yi5KNoNYGeUyOo53MxfZVrU6QqcypTrHR1d17s6FuZc5zIkNBSRT7tLniqinstkTx9joDscyuY8c8sJDxKPzxE-ScwAWHHrUDzIj_ZS5K0_46q48Es8_UBi4-O8Kg0XHzIrWXMxgk1dHAxj1-oczZUEIXCKbj_HIrPPJcymP0uM_K-OPsEY2BYPMhCR5VkqdO8WXARJm5SajidAL3HhnMqvaK-5AUeU_PRRPg_NZt49YSfemEtaaq99lZGim4RdNc34AEulPZcIKS9oYFkJatDXz4Y796iy9NB_3kBFs5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6XTs4bd7FfJ0Ipxf2Kp5bY_Me4sVAn1pCGTQ2FfOsav6GTNHPMtfAzz8-bWyc7GDNvmPUvyIS8Lps3Dgh8A6hoSzQYXpVnQndEOH2_tHHrjQ47_nd0LOza3MI-q8Bi6AA6owgxlIuWEEe-je1cVa6mF2o6OtweOIdFZREeJ3mp3uXhf5mkRMF9WAnSiF6gLUfjuRedUTPeQN9ykoKWCMqS8UOYIar3LiSxZgpk90Dv72re-3IES8GPavYHaFi8q04sj5WgXkdXesSCKxW3Edz2XMKJuYl5rGUpSVukhf5KFj2KllQ-RWBxlAT56RF7HmB4q8gySp3M9P6UugUBhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umpqubcqxvtdOMHSlv8ADDW6LnX4SWe2rKze-Z3vxNSdp7uQz--c9cdXKl5kTO9jB8MIwpiQjkFPCpovV9yhsnYJOnCF1cQy1SX9HZ10bHnfcldc1ik9WCAI3zjcM4RugKJyahrt3dvFRq8ZekB8WBDLaspD0_-y4MA-y5oshFe-TDw6kQy9SLcZJth4GnwmCasGy3qxR_Ub1V7a7XLCDA-a81sndCqBsXa4N2oLnfaviBmsva-xqczvbV78kRY0UZ-ga90CIXUigmgQNRmqcsE1A0osHoWbWKoFmapV0CdD448Tpv-7CauFch7VgHrJsmiSPP6Vu561O-M0Qge6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAAqqIqCazli9TqEwBhMK49xiEU2eP4r5_Bu9aHB1rwIja8Ufiz05pAObVMow0WTeFCEIABA-UA414yT6EbxAXUcic-e17UIPNbE1Och0wxD-ps68L2ip-8JNhPIi285kQUo9PeJTnGmtto7vnM5ygHE1Tlp4TyF9cJbcgsU0NFvEMiphymD0-9k3SkY906sAsg-c6EgLmvZjuWLD3thlK7RK37mIZkKgexo5bjlEWwVJEJH_A77I4hUJkWveWY0t80i6e1TA6MOjSNuT3bPYQT9HMZjN-kyi_inaxW2jnlbRXa2GkngrD6OHop0mvlhcAxX30x-uywJrWLdAgET_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=fzn3pceRejE_guaQUt8S59GfJWcdiRcaTPv98nVFWE6AaHGIIGthg1H9r-6EKkokdhchocD6j6zKSHA8RDqqTyjD3IxcWAw3U_s8IY6Tz4k4OPZ54TqTCz_SOZUB51MKsnuUyw9EvSC6Ka7x7wbpXbG5656oOSktk-F7ED7qIEe_hvTjQJvdDkB0RVpW7GAZhsBFJAdgVjFIkp8tOVp8eagsSuoTSs3cUmRI3bhC25h09-z3SgDdyd1Ro8_pTumTjcaOnwSTaUhwc_PiHkYuTJMTgEwKE6Y-vltd0HtR6J9Q9vYVMCnE5orcwx1LrlFE3onNy6MGt_dueRtAy2LHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=fzn3pceRejE_guaQUt8S59GfJWcdiRcaTPv98nVFWE6AaHGIIGthg1H9r-6EKkokdhchocD6j6zKSHA8RDqqTyjD3IxcWAw3U_s8IY6Tz4k4OPZ54TqTCz_SOZUB51MKsnuUyw9EvSC6Ka7x7wbpXbG5656oOSktk-F7ED7qIEe_hvTjQJvdDkB0RVpW7GAZhsBFJAdgVjFIkp8tOVp8eagsSuoTSs3cUmRI3bhC25h09-z3SgDdyd1Ro8_pTumTjcaOnwSTaUhwc_PiHkYuTJMTgEwKE6Y-vltd0HtR6J9Q9vYVMCnE5orcwx1LrlFE3onNy6MGt_dueRtAy2LHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLOB_O6riQVTnxXK3ISJLzFCuh40y1jkkYNP3wWutrP0QjDZtx2hQpFvMUeRpxHdFnKOi2-YGAiX5HY2iNgpNMkAw62xI8KrBd93nB8meUwotcYyMld0EoP7hwgMv2ZQeOrtl6F_rLfY1wFQSkWKbBKV9TM8roLfVmBg84Qur2jFyj1-LgobtUG3_c4mOgKZ_Vwsp9MIWo26b854-Izze5Sm7MOyoAz8K7wSzNZd4e3m7Zq78KdDIeJmUJqeCEIIedE-TYjGhcemoVOT3ckXcSeEzEfdhzE-rBr94kLiLF_jmsuQ1yzBv-rrOGTWp0MJbAJMGie270SNWuev_AnS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoITd6ssvV-j7iFBReC-Dx7z8JSHa-Cqplqf659iUQfL6p6DdqLTnyc6RELyH4Ev78hOYmMJvjvxmiZgPAP--ZBIT3ewTSxTUcSbOgbZ53czrv0srSq3pJsGLcMyz9shaRA2J7oe-CpxWtx6zOtKw_D2f0GCjHCI8R_WZsLxlUo6-0pS_6YUAiNJ1dmIhAEj2DmJ33RdnM6o1KYQ96_bb_xIGfJvCXRip716nEOIK6riBu8EH1oRmWHZKE8PcgBblmJPX6YAsJxVl3CSMNZ74NnJZ7JhxKVhqHalUa6fixwurdmETkIbL1zIqdjcy84uj4S23Z7AOoxFIxDa0F3ZjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlSjcTe1_FQ8Ve3gCdL2FjMtOF1DzVFRWN82Y7CFuE4Y-Z1wlXYChGN0IzPFYElvanGER2fi_pKfjwP-wdBwosvF4cWh9dZKEO2k4FZxLfX5hU5DmqdkHKwmOg4vMf0Vv62Nr0GjaCdXjIqVw8bH8d6AfdFuqumaB2NTNdtfmEED6SJoowQDKjLwpO53Ijs18IT-P2hELuyIhbR5HlvCWLkw_zN2ElR48BOWuLmALZKmPMvOZoANHF0T3lYuH5JjW5DjM_JxKz-RWuYH9l3h4NEZoFzFabvktKhVj3D2EVnoORRLw_UnTNsHWAtx7SPQTY90rlWb8MVB_olcCS73fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgdyO4YePUx2scwrZ29Ju_tFGEf1PPBOvpk2l0_w2oDVj-wC1MnldPfNO2Afp4xwh128-ROajz4F75QDUTkMgrmfQouaf5iC1GrjpOh72Ds0xjvkDdbywbChGwWJpnCRdY50PQHak48vO4-AU6hfajeOz_G_UKWXqi9V-vCRmOUvNI3FnFXbbzlINbTOjflaukAxlT-nQJuktphjdXDbbo93SN4M2_jpnBb1-InMZy8JgAKSnMuxYgH-Um2G-zRDaal9QBricXTpvYUKkSkR1cke5iKukaBbbzViWk1Bra-fZGUcSxUsw9L01yvlGFdMEEhP-ZnRx0fxxfHnhP_Pzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=LdOWG6DHd_19KDJ_u-dWdxSyek-6F3ElvNix5b3x2TWDYb8W2KAUx2JiZ92j5WmoUjx2QlQUUlN6dfTYDKSTn5jpmVPTvfMbZ775gzTD9fGEaKCCyE5iUQ4nmT1pkHBXq3CZnxaQx65DKq46ZDODKqL3XaqCJYPKf7KxTW6mvgiGHl5k2blIY5UAmuLj7rWelUZvO7XD40u_Ms3vuNepRYZq9syObXVbnoD9lVYYfCr9Ag2RiWqW8226e5hPjbIZ86aP6atCnymrG38EeziQnT2zgWLjUL5-eIqehtpFvWKTcaiDTZrBZF4rNPFNhsCHV09fR-DWAXvdX0K5MplUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=LdOWG6DHd_19KDJ_u-dWdxSyek-6F3ElvNix5b3x2TWDYb8W2KAUx2JiZ92j5WmoUjx2QlQUUlN6dfTYDKSTn5jpmVPTvfMbZ775gzTD9fGEaKCCyE5iUQ4nmT1pkHBXq3CZnxaQx65DKq46ZDODKqL3XaqCJYPKf7KxTW6mvgiGHl5k2blIY5UAmuLj7rWelUZvO7XD40u_Ms3vuNepRYZq9syObXVbnoD9lVYYfCr9Ag2RiWqW8226e5hPjbIZ86aP6atCnymrG38EeziQnT2zgWLjUL5-eIqehtpFvWKTcaiDTZrBZF4rNPFNhsCHV09fR-DWAXvdX0K5MplUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKlMIKTmiZmpVRsTgWLg-ZlAGh0nRHHd_RfDYGDVAFe3hqk5L2FVtZtl5EKa-P42F5RbomRGo7iYlceOjcRFDiQUjNhMLgM_tL_sgVLuaRi3Er4N2joUH6VIo2tkzOMJfyTLi14lhJMrrmscNPP-kTuH-13vejh_3AKaQx0YAYoo2YP1LYqUNVsxkjvNrpbxTtOoI-vQuY15uGi6lQwXSkdUDIHVi2uCPU4w_AzIdDfySaGCPTXAcw-pp5cL7tsain6Tszp15h73kvScJ-SjjwWjPEhio2QIppodv36TJ-DeLhxlV2msIzFDlSoZcJicpcRmoHInezF5BsAT_6nLJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPmbVQLPnGZFhVWOGLetDNwcdSDtREkLSMbSlOdf9Pj8hyA2px5wIxcu-b1f-3drMPu2l4RIDo7QLt2ydXDnoysjG5ccpjR1LQ65E4rFXx43P1uCsUD1NEup3KCu3L_YREMsUQTGLWMNybQ5yAfFzjrgeVw9tlqA-PzZbakFGGbn8kG3p0PJnbySPiJinZU7mMpdiXWe8jx4KtVyXpfclnTzBH_Qn3jH0n7460oU6S8CVIRZ2iBsL_-v28Q3e5rR__HTNt5YoVQ4gJkkT4WzRpRI0cpF3daiocgZi0UXQCAYUnNeskXSJvh5kZt4Y54YxEKN5yFXQkQkU8pSbV1Vsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8jyMxdu8_x3hxIMnKL7KMi6BC8uemAf0rqoKO2wmqw5PgzTl-gK1S6Zd78AL6pHY3G53lnaQB5OLxgBvpk5cE3Abg6_SCWFRBThc_LJ6oIXm0OePKjZIMXh6IU0g2vZG_VqBFtF3S2oOo1LiUT7JTHL913Cz5rtm9fca7MY4sj-bFjPf6UbFweIWVd9VsvLjyzGdEjLmSXcTR-L5BwUa5FSytSCQ-YCBKTvT9WpQHQTd3zzUzmPwKfFY9iWKZJFiBMInA0pPkd3eP2Yd5ogac5Ov1kNoTeKQjr9hLuZE8xfEggc-HP1riduGK5qG_cv4ItgYwgX9Q05sjB6ERuAZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwNCxE_bHu5o1_K80JyVs_45fLpW1wO5_gP4a9XO7Qgjbeevs63tBB7RnYTpB86S5vB2lXRZAcu_jT0RPLKWXwkGJzjhh4qh8QIGBXgGYR7ZYuZy3n3IdWOHy1SxvFiDhYD-YPsmLBELV9xr9XYgdvl8ZZNG8QaUe-9Y850gE5wS8gTfuhwKJewuWGKBhiL8WV5VUAsPmJrHoR9eV2X5Zr1wqQtcedMvLpRiFcmsPDcj2-xmmHBQgXGwGNkhNEuAt286Jw9w3l9Kcgik67eX-B6Q3gwmXiTRcBjQuFy1VW7n9OLlkY2LakIynY6p88pmiOASdcxzUUnC-p2ltnDl1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=aTQ8tRIEQX88pGR8KAwpcNL9FEisO76Jm38dxzVn3aWYxU2VD8YwqfkVAuRkVUiBdlFQMPJfxi90FcFiI7FJeT-MzehfehDgrU8egYQ8enpYLVQaKDpn9mDSrBfQu4f6qK5Wrh0N6LEd6dM0O_jx01KmKOWkUhS2yiNWF6MeNc6755kYHVlyHVSMr2um3kMF7ATNjI02vRv_084riZx9ZcT0wUgFFLsBOwjkMJivobEKmpYOI2d-UEMgA_Uyoo2t473KwQnX9cLg8f7wcmuK5S48vQwd1XQkBpWFc6Mr7VhWNDxD-QJz5Zn7gRAt1MPsV8SK2c0aU12eanLQM-Dfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=aTQ8tRIEQX88pGR8KAwpcNL9FEisO76Jm38dxzVn3aWYxU2VD8YwqfkVAuRkVUiBdlFQMPJfxi90FcFiI7FJeT-MzehfehDgrU8egYQ8enpYLVQaKDpn9mDSrBfQu4f6qK5Wrh0N6LEd6dM0O_jx01KmKOWkUhS2yiNWF6MeNc6755kYHVlyHVSMr2um3kMF7ATNjI02vRv_084riZx9ZcT0wUgFFLsBOwjkMJivobEKmpYOI2d-UEMgA_Uyoo2t473KwQnX9cLg8f7wcmuK5S48vQwd1XQkBpWFc6Mr7VhWNDxD-QJz5Zn7gRAt1MPsV8SK2c0aU12eanLQM-Dfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7MKEK3gS-X3RKXIdLu2ERLXEPxbuSMeFlmO-kZRV4_siIXzLX2FlJTQAeY-SLLUy1wlxJbAFXI8fqrDMHuY-ZB4pStV7PpTgX3qKecl_CTC9q6HpExDFz9orEt66yp6rrGEYpfFc_Ezcvedq1V3bTrwkaGumC5JOtiJSsPDiwZ6_j6zGmE3h4CYqNAIvE7AOQOgqTpdY-zv7VBscYF28FkXlDmmkMyS1zupEQbsm-v3xEFNjN541hq-_DcH4YSSw7ry4bjDzwkmn4ytA86p1eh9lKu6G1xckeGIZAOvJPFgWvbaOy1ksOSNZhTFwSWtBMNx1ytcTb5sinx11UyAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG8HKpoc6mNr3jBVBAeKcxbvQx7yZB13viGbGveJID5XwU0yWL1gAmq3KeimjEFJul0x2Ty9yxLceODoQby7ZSGnQj48HtuV-eRCI8W2SsvBo3ENNn9VzXXM5cmjB58YGUtquFl6ZTH0VdGQF4_pI2pbo1b-TtAtRCVL-wgL3JeffJoNJhloqx7xd5Jh9OwYlQOY-3TUFzeSOChrYQor9GGQ-ZEj_EcFQXR4wMxg5y0KRrt5deQqD5Jlz4a24DV9LpebmUxPW_yRg1apps0qCoZkVvw-a2g-MfgGzLh3A5drS-f8m1WS6lCV0B9QSoogVUcKUot4fyDTM7uJJg356w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUTsu2K2YyGJvem3TjuYhTjow3pzZiZFJx7iDCOpidzDPc0dHzmuSWS9KFhhoCMIsCuiWn3q0CjHLcpI8b29zIWoDQjLHi7fjm16KnImkwAp0L_xT_Vs9gvOBtlaxSxFAhLjuzmp5qwysJekR3R94Dc05mx3UxvaJ9CVoh5nUfv2L-XnfZBVbjF5GEjligT2rHD8Spk4nN4UzNOICqg0vyVP0POY7oWK0hv6Jxf1uCpG2q37aOdzUMi-JQmghVGK-UJQIQTpZqO1yPVujVwaBLcaZdtE0VRIGwBDSwIbBHtuQ2cClQWfunQXA8RhwiSDxAGV81b3CHYWjXe8INoMGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZYONImOpCDk8N5rvHFqLxN4CTg1eKI3HumFo03WF1wekQHslZIqvfxn6_S9FQ6wL4EH9saIQ1NAdvpN3jt8S-UD0OsB4RGQWRqyvl-G211n6pKKHS_cKLEbIok20WseCqOKxAJCAkzyhKCotX2I4agqSL4Xq0zQ675XVWziU5y4ymkPZHC3RuuTexUQJqqN-JkOzLxhugRk0hIJ_pbtXgqz1VfF9_5Q_tm1rDSutr2v5UIJteByW7kgbxBDHZe0Shb4DwYCYhj5dwwDBMUc1RZ48uQ3l5sZpdPgTta6v8w5rejBMKFK6QlCN6KyO6xta_UGf6B7kSOO2Wlvq20cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HE3O3C7FvqCX267cV1apVpEd6lXgDNgdbiqvya7pSda0H04uUcJZ1cxromLB7uVsPQ1Wn1bgSez9_pj6Z8dr4rr7eL44UqKQ-lbRXKtTMg2HKzs0eWkBmlKKMC9OoLaWAt3mfLSwf-meObmdGjUgKIS-FUKvXawx7HflunL3AJ5U3MVZYEQoZkCWAcms_5J6GHwiDca7CltC4XUkUKFPd-Cf9R6E4CkoqNULVzV3VHOrMCeHUpNOI_nEXMsiMQzmKGmQn1m5TOP8QGDbO1xX1OLYiBqNUAjpsrng9DJDg44PZqj0LjkDvmGjEhkJ-bsXgTrnnq73D-210mtQlq5TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgKrA67nACrhdVcqsWepsr0KQLie_59MnNA-gXe_Jgr2MmH1ygvnuFMVu4j22QUj2wSMJxL9Ei3bLbfxHteaonBznsH9c9aafFhhceskJJiPE6_Eqm8aIsLXhCLQHIwkDzXWQ3PpGAwW0B6wEA3Dlkq9oj94U87oIsJw7vNm3b9nrgQgc3mVR-qschW0A56eGX4NiJCS_ZBFkjBoTH0WF-TrCoen8M82Go8o1rsmXhXpBAa5fjIF1zuyo_0TyBtJMYJ2pSaQjFvmmv6FGXueQHuDs5x6Iko_q9XYCXnNCRMW1Dwkgw7uiUr5R65s-7upbRS9b61-eal5UpQI3h9gLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=oX0qpuwIgnYU3-eb9Bhun9xNrzHUs9RTq-zcqouEZD56QrgpP6bABcUzL4dWPeYlKWixhitATYDZliW4kEgrVH-OajZvbpVMoNySFHvRwxTXp47cFQWBYzt4aF7iQiD1mNUD30Hr3Nfz-MOjUZg3uuDmVMGIrF6oGLlPBkqGRVCY3tbmKeQdS4Tc5_D3nAVq_EHrekfSYPezwIPwYdpLh5vpk8NaAGFZFYd5f6khHw-W0pa6jsOk_gjH-1zd7ibGb3keya4rSx0h4whFOZjgnFjN2hKpVuw6Qk4VovvJSeRsTqZ3au9zloSU0FHkI8tdvd23lnb6UGnCDY9oHH9zAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=oX0qpuwIgnYU3-eb9Bhun9xNrzHUs9RTq-zcqouEZD56QrgpP6bABcUzL4dWPeYlKWixhitATYDZliW4kEgrVH-OajZvbpVMoNySFHvRwxTXp47cFQWBYzt4aF7iQiD1mNUD30Hr3Nfz-MOjUZg3uuDmVMGIrF6oGLlPBkqGRVCY3tbmKeQdS4Tc5_D3nAVq_EHrekfSYPezwIPwYdpLh5vpk8NaAGFZFYd5f6khHw-W0pa6jsOk_gjH-1zd7ibGb3keya4rSx0h4whFOZjgnFjN2hKpVuw6Qk4VovvJSeRsTqZ3au9zloSU0FHkI8tdvd23lnb6UGnCDY9oHH9zAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1Px0RC5c1JIjyJtJ_jnsievLo4uocsZpHDSF442p6vHtAJWr5tR377hJ0vfVMLKYAJi87UCqyR96Xv30YLX65N1dPO9vU0dJ7X_OD5YRKChNzwceOYsjpeRX-Ywp7tXmxAokJBgTjcuT7YJ5lyp-ZjwrdfskPgmioc7CHDLIUl7lrrswJvPZ30r5dFSfCi0Hq6EkY7Z8Su3igQxCF2O6NjB55zbdVesIEwALkK64GHfddUKx0WxHFnYfVVc73cdXkvvBdpSsHfa6I4EOAPL6bhNBWMcmysvrHaWHOtsnKMhtJAn7HhFZSGwN_O-pPrQ9fD4pgNv1b0US8591cQjIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzAqTQKV1quWntbQQxoCj6foAi7s7ihYCRAJdDP6afgvwskno1qvixnWgRdluegdcewWmEz8HEXWDImzdJympcGu70B-mT1Jeb9HMY_XUQrIT9S6xplcow4aArlsCKZ3MGgOCaDqq919bFbKyHxYD2cSe7cA6waVBXG47KfXNNsPcMv6Y2X_vDOKPyV9QuaoQY407INVJNdMkXLezeiaiIUxaAcUWnH5wwtnZb7adDymH77M1SvpnmQimQeaUCNwmvc1-WGU_cES_X1swNdnHn1_Lk2hOcO6IlJVKF-w5rNUxXOSMQ6ZD4_2A4XlXfbjtmPvKwLNluC5JDfl3s3nig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz2Dpma9AetaX3S3supQGUCgqmEYeh7c2S1DyQEdLl4DOeHCw0V-WxaWNHgrLZ4jnyNhhvNfwBpJso5tkfba-uFf5mRzf6gbXmHr6HckO9H4MZrQfW9Q1DppXWrZzQb4FxMmYhbIgiY6i5rXB7egPnXpcdKhMfXcmxeXJA1IhQTVCgjuUOeRdPhP4YyHqEiGrctj8JBnmJyQvX0qKO1pSqQNLJFAfEl_fTxuIe33eo_Y45zGO38DkpbjQVqTPvtRC0AuvICk-q9wsFfqJsBZnMLLpegFXL0Tk0jI96sLWvJ90o6Ru9kJ0AcGfv49XhXdXTtipTHp0ejEeQaaw8HsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ6rxWBOatxaj0a41bq9WgB19TxAtAjxxbtiJS3oTzUk0zIDJ5nB_AL_gmMgzlMNdxTkcrW8Rpo8f4jxfxD_DlTzktIHHb8XKQYf05Ro-cs5ddMbIvW-Ne_ZcmzqRX-OpnWt5OriiemFjopppcuPfHmu58RXxyUciJwjGhurKZykhj63dZJt4CdTfq1vdBYaeh7Pi523dT69h4ej66BMOn3xYahHlosKPKHMBRjxWvbclGFLEO4c52oyik3RnfzrcVJDhJ253MnkV4Yrp5pjuYgNeExM2iH2IJRDvC-sbZtyOb24Y1G8RQic2ThKm75xiuhX5eflghhtIlVkPcy5Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Yx1nE88pmXjz88yzo9jc3wfr8DVzS4sZpin-lIQD6okPLS6TJ6p-s00o3h9n9RqPRoKGohxhR5prP7XORcinV3UsMOa6Hi8PDjVmKcVpZZ9kTVjL62SY7zRe8P9U2jjHCzF8XcPEdjsoBLmUCaoCXqfRMdeHIo96M3D_g17LcBagQ5zit7YFq6Sj4Ho3gvCKdwU8UlC1QEpTakJgpRxjO6odS1yiYMHfwSRUMPKhHEiEcmWZVVIa2gMADqNNVCqEgdkbUen3GHhL6Vh__GD99VPu1u6CTt_MT_1yg0TkVE7A-38LpwlqsJhRFfTEr8ND3-0f0Tft_35Yiae4tfVAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Yx1nE88pmXjz88yzo9jc3wfr8DVzS4sZpin-lIQD6okPLS6TJ6p-s00o3h9n9RqPRoKGohxhR5prP7XORcinV3UsMOa6Hi8PDjVmKcVpZZ9kTVjL62SY7zRe8P9U2jjHCzF8XcPEdjsoBLmUCaoCXqfRMdeHIo96M3D_g17LcBagQ5zit7YFq6Sj4Ho3gvCKdwU8UlC1QEpTakJgpRxjO6odS1yiYMHfwSRUMPKhHEiEcmWZVVIa2gMADqNNVCqEgdkbUen3GHhL6Vh__GD99VPu1u6CTt_MT_1yg0TkVE7A-38LpwlqsJhRFfTEr8ND3-0f0Tft_35Yiae4tfVAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIqcT4DHMdp4is8sNaye6HglgX-DoTiHIpHah3C7Zv7jhZ0IfU9zj5wxJGJo2hdBYYOmuNqZnwzeYhxqmxVowMGush7CYIt174eq8rxfBFheDbnLHQ5JlFnSL3iScrz_QQzGZB89nr1715aV3PaKgZowCtWqrjrFMFzBBIyG6vCoJYPM1TtGrRHb_WaRaFb5Bt__pk65vWo4qzZaZk-xDPCruyMnJ_uMf4SJqbYvlazQTdlz8oqrdON6ucmSKloUIq-37sWcwMGsRhl1nmAKDheVht98xZ_BobhlixSkNjCFk5qd7lfqewiEfJbCDfto7nc0JrVgnqI8Ft9zxf5I-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t95tTP28l7-k_Ju8x0vGRKO-AYQPVSZ-IfyG0IZh9zw7QbPTzsGLryaRLlZqFEtoRT00lq5BjKHQ9AZ5L9l7hH7t_plV3HR4B84jV5artKhqZ41I3kvhzreOTgIqeUVcszUCAX_AffI0oAthKLi9QGE522mzGubTrv8vNIkA-RpN7GHPrKGa3cjccuFSQYHwZvIWTVtoUFDzDy6Oqv9prjnp6sliVwQWKJhKg7xqO1NxDQ3Izyq4p-20-ngSKCBwflzGsiwCZZP8dHyiK8k5s_yBmoptlyfJojnwJ7rLvUNEs9io8gainOrcSdJSPLwxWlVQMhf6x5cgDmlLh4LzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8NeCbebvHtJEdjLDW_YUeLFAOSwD7zDYaA5J5IFWlzwAfAbWc5cGCImFJrzpDGM28R8moccWEDQHMShlLB5SRJgs5kdnxJi4OBimN9eoY3zqlMTzFyP1O4Wl5b8mooZEMY7Oa7XN6lweYDhaeL-BzZh6yvhTxR25JKUXAyOd56zCSfHyBgL_pJFXV7lOHmfwW6vn6YkBvwOvy_jEAYI2mrtD4DSMkKmGZFCuSIxhpbJjuA-_97Pw3EhXYjBc5rsP6Qne6nZMRgF9BmWY_f2EopcU6oKZWJr0X3v2Ish5rv2JojTxJMINTzWdjQdtJzGlXUuNiEyPe2dEocv4ONWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-UBWnUgeer84iX8qryfqmQuO1SEBoXaoqfLWjvnGFC8prUtZotBkbDE9KHQ7q_6NRfpHezM7_yQ0Q-DiE6lqOw3PTxQWGmgxAvVQBbrmu7zGtuJOmYsxBFQAdv12b0tjrUhXNuUg_NvSKJXeXjCvJgCp8szFVF2OnHxmRont93nm0RVrWa-lanM6s8Hi-z2HaFzaKlRipLmn6ZIQdMED89FfzE-yZmRaQnj0buYRa5VtWqv7__xcooytaoq32H2oSGG90AWNI6ZsbBvzfTsQaaM2PP6r1CUfcveZKz9S-pEzq2gRocxDcFbWht4CeDC5q5TFmhKa1VyJ5tw3jf8jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=dLnUQjC2XBc-_8jsAgdB5zeecC9aLwVL-njQTisx4tw_KZ-11Ph2ywa6Pw2POHHa7-Dj4rUaCf5iuD8X0AwhBK_bOqIoA5BHEU5hEey9ck02kf1eCSfBEsf8q87nl7wYahxBwY-7xQsr7Z6Oui6rB_PzzUOimsj8m-gjJB6yjX-OK3SFSaCZPrBPkNV_f8hwrEFCLgsilo9GbOeBBO5V86BlNCRNFyiyo361r_olhcDiHJU23eWWfV2cJFFSzpMOxI9iPYdVI01J5ZZWK9cV7bY5w0hJS7oyqoBZQZdkpRZIW_OJFPWaX1gOyi_F76ZZhUQ6KxSjViBXJO9_xfaLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=dLnUQjC2XBc-_8jsAgdB5zeecC9aLwVL-njQTisx4tw_KZ-11Ph2ywa6Pw2POHHa7-Dj4rUaCf5iuD8X0AwhBK_bOqIoA5BHEU5hEey9ck02kf1eCSfBEsf8q87nl7wYahxBwY-7xQsr7Z6Oui6rB_PzzUOimsj8m-gjJB6yjX-OK3SFSaCZPrBPkNV_f8hwrEFCLgsilo9GbOeBBO5V86BlNCRNFyiyo361r_olhcDiHJU23eWWfV2cJFFSzpMOxI9iPYdVI01J5ZZWK9cV7bY5w0hJS7oyqoBZQZdkpRZIW_OJFPWaX1gOyi_F76ZZhUQ6KxSjViBXJO9_xfaLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
