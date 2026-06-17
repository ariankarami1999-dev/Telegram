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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 03:51:59</div>
<hr>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNByDiSLOTGwgRzOf0Ts63txFRwuD8N8ihcYRZ4qSqF_ANlOB2EpM2nuhKSp7bCk5_V3FL0IaqIJfxPO2_n8r1cvTZexrAbi-z-e2WqsvTS5J_vqvh4XfNb4tsHCAEkE4bfYYn-m96EvwB2CYm57BHYaGGKwAEYcu8EyM0aAkrMcK6DIdhryailMyUmf-tCvEZsK1POzu_suPg3eFrVDVRl6i4eb94FOWg-SzxNL8QeMLNKQ9JsHgXqIGiWiYjS31Fv7W3nS9TScLnUz4xk5S_AbaDp35nCKaHQOwVCDzpnyt6Qd54ZEthxHO5swjHcVtE5b6n-hSeffBaUkilrTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWfVPapZ4rpbfEgKhmiZrSEkPVFwPMuXrHONEtMlHMuZqtTTId2Rrf5Bfg8DW5l1b62bar3iD5Puf12hGZm4GKt5MvxNemU7mpr4PQz18n2CWEroMdosadX9eGiUokvcdVZK_mDLaFHdmGlUA83iazbCv5p_gaCBy-cUIGSfU6KFRdrA_MSWY9l7z-yR2iMj4XhTWJ8BApCSccfT7FCo9zSX4-n-ApnvugKL4RImkt5ofsFSCxMm_s_r3L62V0eLLMb1UceTPFzlHMlAEkD4eFUkoTNb8om3HljVRospyio52Wg0BQjtRiBLeAH4HHbHQZsyewDGirdGi3QWDX4YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpTwUXMFmx0zusU5pPUHvHorEKZFxGs54LUbDvRI94DqLnG9U3Rs558w9obTuoEhZgdQ-46snQBMFbBA2KAHdryAZ2QIkzZ7ieI7-FSS0ROfEhpNlOE0L87_UZw_oTu7CB_CMXXYg6FLvtblCmNcjyY_HMfGPvyhxiBb3sXzsaly2OyGm-SNEXpODLNoQIRnxKCd8DCmUVKXijvC65WwfUTZr0dyonvElYIMGMQ4PNeJySKIjyK4usYp8XC8UQObR3eemWAmg-MadkwMBXS-F30VWEoi89KNrRE6HS44FhyODWiVVUYB8C3tk635urwyBuJqN3zEru4xjnvAWFe0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8f1kXrcz9YK3eOfYswdeC2Q3qra4qeYKLxBjk85qrgTduU5IUf6oplmCFVGpY8vrFPUGFB-lceoqxwitUlyNHcAzTVDF1rkboZP-z7It_a0w87zImELVQoeW1FEoqrU6AB-i6ZUWmY5h0zJH0_q4AsZDDvwoPOUC6jXHmugfSlISsf0FNeGeb15kg3PECNtRhZQHuhQcex1o45Vvpky1PFiBiWd4x4wliN9pcUQgdlHUg18oZN2p0XmjevycYcagLd0Pi_JgOD9PsDHtcohSnSbOaTP-VGW1vyzxsYf7_wqiUD5X_oit4FnPmDmpUO0mIax0Xr_GrHvBedeN42c7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBroecgPjx0zMQ8FC5hHsh271nZzOM9OgBhxeGNrWVGURcoVJ1554IdE1dj-1HAd4PQ_yLAQUXUn1I-vEebZPGxaY-CUkeDEl9k5CKnhd5vK8-fZ-zBIMPE53rUnHVQDJIsr6QDPGZc3nrO6jY71mLR7OGBmhObUfQkDChJjUcnO9w0UHumBs0Y2-sTPKhcwYuK_sHCU4BWIIIT3Ks6iU2L2PLV3lmuTrkb-yf9Z3qG7pZBimBE4qGkpvMcC9l4HzyNFJ6j2aWKilgvTnDfPzqp8VhCwPwDaxSq3W5MsAlfpwmbVV0JHd6LSQRpsNj-AqGkzh5piM_TqDzWzbrA8Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=tlo1UWL_L0yO6QfDSg918QOR_Azq5Tg7RWiq2PeW-wz5Q7JKFNosgiIccob1Ssr-LpROpc7ER-1o7LKdomk4ahdacXTNHYFl-FuVxxR5oJJCTU8EgAxfQkSVys6Z8P1oXAoaIupxFWDQBNUWTFb_orckWD_Pg7M3QA-fcx5bttMrFPOwt5W2OrKiFy6xJHmtoM5GM3t024T5dEqAWF3H1tLx5V2ObtWtNejDOkOwOXfZOUPvExX16jvpAAvwMsmLCIhr66NC6sTwslNfxAYwyuTnG30nUQxwjjui72HFyoE3O3XsyjJPAF1ge5scK1zQiX5Z_88zwlKt2XsGfYXMrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=tlo1UWL_L0yO6QfDSg918QOR_Azq5Tg7RWiq2PeW-wz5Q7JKFNosgiIccob1Ssr-LpROpc7ER-1o7LKdomk4ahdacXTNHYFl-FuVxxR5oJJCTU8EgAxfQkSVys6Z8P1oXAoaIupxFWDQBNUWTFb_orckWD_Pg7M3QA-fcx5bttMrFPOwt5W2OrKiFy6xJHmtoM5GM3t024T5dEqAWF3H1tLx5V2ObtWtNejDOkOwOXfZOUPvExX16jvpAAvwMsmLCIhr66NC6sTwslNfxAYwyuTnG30nUQxwjjui72HFyoE3O3XsyjJPAF1ge5scK1zQiX5Z_88zwlKt2XsGfYXMrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXslAdWBjSsFYxgI4BJPX1fAd9q8R82O-v5dG5D8iO8MbiqcU6c376tay6P1a9jnGLyt6c0gILA6xyWzOXxbi8iY1cPkUf6lIGzw2YkuYeS-5KfhT0gWdEQOa2gqdf56HBpEaZvxmXk-LU3bKsZ3D0ZZQ8boP7I1yK89JK0zFQPUb8aqlz9GRQ0HH_bOfgCYyCAlVve1k1tO3-AzFWPkxDo5DbhHAF1wU6pgzObal_gJVYZFoyWM7aGA3Iu-X-acs_XC107EeUhMWlSAL99Daozmtr0TkzQojOGN3nej7VKcSCGf1bCjtgtjSy_487nhaueDpX2-YDi2FgvuZpkYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=AcElZuHFKjEBerr57eboofeICXMTb88iCv1rpqhrwcZEaA5wE3S3gMDt7NL700LqQd-s8n02hlYLwCSnVfNufU2_9Mo8p83MUD6GwXXjjTfhR_W0VkZ1g7A1WDB0vcR1VazZaOy_0MzOSkDtXk7V11WXMepGRGjcNB_9uIPx9hUB14vruinPrAVsKR6eucpVmYWmFEJOZLAXm72Tr3_joSd5CreXSREBCxz0xb8j9SA15cx-Vhge6-GJuHfMDF6HK-pGAVPX1_55ZeiutS9a25FrCCY_d46b_wJMyJ9sFmlx91r8OaUyFnbdFQ--j50Ux_FQD62lZ7tvBRFfGs-7QV9aFFhtzWqwTsteLRRWD8BnGWYVV2I6Zby8dLWmHbki1P40ByuOZKp-gYSIFVE9PWiTtCP43HSo7j95CtjyYhcp81xPr7Q6Pz8Oc1nDbCKeJYpBfCvRpTR2o5CCjcEWKjA0OMX6V3ZRv_Hd-9tB5YgTcq6qQs0SS_gOBktET8VZLXYQIlRwpIZ2Vj2EAAxkpZkntZn3c4YFiOfTTH47r81ioSOGszWVy8hfh_D7Wu08uFHO_M0Th5v6csnrvliu9cTTebEBaUUeUJi26ZAF_WnvXm4R6QqEJihZi0DD_-4cVz4A49zJueEIl_of1Q4liaDRXPVWuYJLVbHUSIhLxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=AcElZuHFKjEBerr57eboofeICXMTb88iCv1rpqhrwcZEaA5wE3S3gMDt7NL700LqQd-s8n02hlYLwCSnVfNufU2_9Mo8p83MUD6GwXXjjTfhR_W0VkZ1g7A1WDB0vcR1VazZaOy_0MzOSkDtXk7V11WXMepGRGjcNB_9uIPx9hUB14vruinPrAVsKR6eucpVmYWmFEJOZLAXm72Tr3_joSd5CreXSREBCxz0xb8j9SA15cx-Vhge6-GJuHfMDF6HK-pGAVPX1_55ZeiutS9a25FrCCY_d46b_wJMyJ9sFmlx91r8OaUyFnbdFQ--j50Ux_FQD62lZ7tvBRFfGs-7QV9aFFhtzWqwTsteLRRWD8BnGWYVV2I6Zby8dLWmHbki1P40ByuOZKp-gYSIFVE9PWiTtCP43HSo7j95CtjyYhcp81xPr7Q6Pz8Oc1nDbCKeJYpBfCvRpTR2o5CCjcEWKjA0OMX6V3ZRv_Hd-9tB5YgTcq6qQs0SS_gOBktET8VZLXYQIlRwpIZ2Vj2EAAxkpZkntZn3c4YFiOfTTH47r81ioSOGszWVy8hfh_D7Wu08uFHO_M0Th5v6csnrvliu9cTTebEBaUUeUJi26ZAF_WnvXm4R6QqEJihZi0DD_-4cVz4A49zJueEIl_of1Q4liaDRXPVWuYJLVbHUSIhLxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqqZgRI46jRnFHqVzMxzUY7Xd3EPYoIJYIvnI298i63hE3BmhWYCntn2yspn8Yn7w0fIIYVgXpLd_u4qBSCONc4SHZlF8N7Oy7CV9dfOigWRC09sEVmIfS0YWQsfsIvfolXN0nSt-U2gbjM6OEKLJoJNPbA-1T08zGwRPWJBlBrPts0LODG_6Msx-pZ3etL4c5PNrvhPdP9iZ8x-WZFvxBxE2kwilonlj8GD2xAjl-AzYNJxjhCVY5d1W2NI0UyuQbgJewg2qia53cBITIRlxTC159NmIJvhSzMCL-BVSPAPM7L8mzE1GoqA5T2ObWOL3vSsveibFiieIH_zCPwW5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlJcmVowKnIshvMO24szjFEzI5GPwIBAdxjv_ShE_vbugKbgY_zXy8g3tzg-MtsWZZkLDfm5_O86Sva5NgZiTlzhZNWRKXJi058LwWL8dJspMe3taEEvjwpkbc169EZPfMfxXQ6leQwWsMEl60QtqROhFIo4hBx9qVkVyhz9l_xat_AgegjWQkdQBB40XAMg4ZOZKGhpCihJ7T1SuQ5ZKhcKN3Ovaw7rq-JzzpN3ZDZQ1aXDiKpoJzDfH3oluhUvMQCeb5f1bQPmJxsL44xHq5fsRHek4B1enVNmfFo8XIS65UtKOBGx95cS6gIx6CxwL9wmU0vtYZvlrjoSQB4f4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umSVz7Yl7XQotK5SL5oCHn2JnS2aYeU1rwfLVMxpQyaD9j7_pr8qxTiYDNvKuIRP9gsjJbK9I6LC2Uw4K7uxB29SBdVGls_3mRO9Lvqsgl8sXS15Rfgk9PK3ckAwYJvmIV6qqVCbZdYmYjX3XfVVf6cwz13-KWxR2fHB42OVWr0G2q8Tf-3aW_-kEV6eAcSJ3O66TFmatswTo5WExDSrgGONNCQpuw8I7fvn4DNdb-5j_j-EYFABzVuaYsNkGUdcQ7kr4oJj0PdWRinh1-RRbTih9jB6EfhgEgR0p9ekGZj2KzZrxNt-PRNFH-L-DRcnpDf8wZZuojZ9JWNlFYoLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj8-9R1nT6_yPaO8BZTt_ayQdxj_NvhdABy6sdxLje9JRMCqfkKyCBzgo3SkTrnSqbhaQ2Tjljs9obTq3gbpqIfIUJ3WGhRIbpy0EOa_-JAoD0i2dPXczSCa3hDmHINqU-DgCWJfgQRFrZCElIf3UbeHOr-0aJiCuy-HMXobirxX_HH5VcVsAB56ErR6zExACJJqnOS-7U9rwJiE4QgbYMBHHjT-XKgUUSbohBHHZRMw6IfyoQNVG9NDIWhaRi9MH5gI6U-usTkCkVFfpEfHZAv3Go4PbjlI8ItHyxX2_p67zPcimTdEl3BXelRyiBj7l9R048ZBqFbskHnIh7RclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XG0vxUrv4ZACuw4UO85ogAPu4HRXVJa2Cpp3bTXsz_inQ-j-Wu4VcvY8VeidNTpF_QVPqcUyeGv5z2wTTGqRWgVtOanhdz8XFtowdSdHYyoe9Yyg-biGpJXRx_xOB3UoKkDNB54BSu46Z_g59tRLDVhZFvAesSbLIxMXbHeDUeNQ4WlUfB3qAIoScRYIpUx2_MSPZlaXo4Xk0-bda0mAjWj-WZF8Q0lrLqpOwDq3x2r86eHul-7iR1dEu5mxxubwfZtYTA-o5pJxEZ_a_dJQ08dLWe6M_lrYE84MrZgiGIxenKVnJfKPm6WfaOyT7Ly8ee_Umzp8nBl-qrDiLx676w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3gcPbWJy2CiDvc9_ffgftW0G07h9NiTkePTxIo9VbQH--yXjGvO5A5tzG0ceshHslNJcgobzB3MaqbnepfphVXxmLLqcLH1SeAx7E0lx_axoYG7gXaOV_hgDn8qs-5nCkRbuiMwvfWVofjQJmRSiiDNlewD4hI54To93WBCIxaX6ulmu1KGsG9iV4SwBZyEOUf32rP6iR7mPO2X5RruAVIt_6-LYGTbUHvFR6qNLtZuPbmsWRzjYyhcG3d9erbHurbon3LuWkraZihd95oqPx4pNGUx6_-asPGIoCqmmqeTKIFesLcMd9vKW5SdRrbpRrq1ffglG4Xgwq252OC5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdtbhS0a8_uiebeBFsR9OLNKcK9PIZEoG8Oqzc_hNvw6ApNqoIIRiBVa2h3w6o6koMZQOPuO6xdLPKYWis3zE8n-PXmfNOwnfGIiCbiORPaQr7iBMV9NoVi3I2fhSljJFl2ty0ArFKuK_p9KmuG2G1zfqDLqVgjtf9cSubUdxbci4CqQD8NT0G6vq13otUR8f6enuOOmGlfYy3iIKGIsP6AVgz2VZ9rzljhlz-SimecayORrew5VUapNcEonDPdFWX8yLuL4LdmwE52ey-g2M0rMO1fxTOY3mrppgMTTbfv5Q9QMgq1Ar8spZnIJvxQcP7ucC2GwN_YDhRc6wJsF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjPEHRK8_va_fFd5iGgpFcONraBw6bSBkkcwSVFFzsM5e8TXyLvZK2WwTnuIVkIuHzsr94LAOR7c__cpjPhMqOYhLGnXE9GS9NBMfokzsVvR7rAepnNtY9ryc2_A9EpsAhMUwyKSsSSKU0Mi1jiqZMa9CakEypwuw2eVClUuuh4Inh5WiWk_6D9A70Ui4uynx8V4heb_S9n99osofWKdSlkg7E6iPxoBqW8GUCAgP4qPKpvCEy4TMo0k0WNA2wfv6bhVCsDjwyn89mar9CPvpDYSFC9uWYa13uyYzbstrNzzk-15aCq_JZgYuH9dMALQADKcwBWjpJQugTUh72PCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgA_F1Xgj1_-6_ifBo-GSYhRno4TVoGY6FQXirIJP-smT0G1weTM4dOeEuU5S0w-PfCeM5ZLyT2ZqOv_kd2xw7rsfarddN4BPfCeRkFe_A1y0KvcBo18g0dGAmlsib7gDIFQn9DqjofFhJYEG1DUdOq7YCeBlsruzYJV_AH23QnibbywOA4BNeocTJ0_r_ZtkWgZ6m9R3aQIk4BnY6J-i-AycxNOQfiRvkjn0xHPnF3Zf1Md66RPoTYlbHEkDn86FxW9lv6lGGZFy9XRm-8JMS5kNWEksFnyLGsSWca0_Zbu9JP22551rMTNhqJsv46S-huF2jTwwVAaIdeK-7ucXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3-7HKQyhlH2KE7kFUVwDK933vBFIuuHrWEIJoN8IARWbpcPnKgCaN3nl0p30gMg4Uq0G1hDA_pq6K75ag4q9QCsR3k-rccwrUut7v3klCwbMFuObK7dseu3hJij-tGjxJ0otpCorOMy9y00PEbeIN84ZADJ86mWjp9sAbdHLgB5qAlPa9sZSzqIj7IVT_rpMn-Og0UfBpYe1Nj7n_EH5U65oIQ3XA74obsXy0-2UyXT2qtF6J6uKvHBazhk4xlHzHTNgnbkf3ZKHFSkI-trxcOicDy1DDQ1ehnkMhCS69HKDEinH4xX-opcIk0jKfQwGv6L52sJsumQbJXsV00YRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtWQb_OUaZDFINLg954qVigWrh_5skorzI09bFWK76Ylmx0u79uIwVwo16fndpNjgkxu-MhomxcLF7gvUsrAiAVAkXsoccl7a-LP146oES1_q0HH-szTC-OIgMNBeJYRRd1P8w8yo5fnZYXiTBJOWvuEp9gDH108jl3Cz00Cy5nP1s53c_U45Dx1RoBmRPSYWSARx9w1L9SUFwtaQQotNcOfT8OYJpUAqpFVO9FgiTAQy9iZZfVi42dt-edYK1RjZziOFKOtfAHQTU8Oj0j0JJzIvGbCUIx1CnpsrKcYpWKva08e7SU6o0ilfK5j7PhW7Bnw-uAWRICc9GAoJeUNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP-OrDhFN94J2Jj3Bq6Qt0xIM35s1iLGDH5g41RnHcC9zZJbAXSyTSt0NYqkgBhf1jv5r80KE-BqtZr9rdWJ8LHCXuDaE6gmIMtMclpSf4Oq5mtNKf_1RqmdH5dZU5wOFQG62E2WUU1_xWQU17uzvh3NRsScwigQTdv7o1YRBFttOUPoa4astGeh-cG2EXb2ejrsla9eA4SljOC0K8YdaVwLXwQcFUAfXniI8uohbCsgenQrJumRL8V0UcdWKcsu-EpV-mMiRv8fEIChhvksQcb_PI4t4CCnTTRtMfhb_78vsEvCFjlNcr1GMu6MwSMQTt7pJbrtRJVmYsXnuQrkQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=P68bzFjZrdTGyW_UNASPQKSoyr51t31_6900WvKTz_UxFVPYSOTJh-zuCsoXcU3xEsTUh-bNgyXIbMextWvcXuauhCnXuGe-CYrb0QUaqXJgi4yx6pVAE7tle-oGLJh6UYAIXtRUPMXiAd6jj7Uj3zIYQJFYXJ6Iqyw8x9faWSiodHr-PJQem2fo2jE_Tc125MB9t8AFL8gXgpjhgOtiODfx-5KXZV0lifidOPgNj5Nfe_gbhKql61uBoyFYOyDHXO4ken2ehVs1JcUmJXS2lzS5KQB6Mf5K2i5LSuowKELgRBwnCRwovNufMf0QyZjz2y_LTVV3uZCXC1QSeJPLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=P68bzFjZrdTGyW_UNASPQKSoyr51t31_6900WvKTz_UxFVPYSOTJh-zuCsoXcU3xEsTUh-bNgyXIbMextWvcXuauhCnXuGe-CYrb0QUaqXJgi4yx6pVAE7tle-oGLJh6UYAIXtRUPMXiAd6jj7Uj3zIYQJFYXJ6Iqyw8x9faWSiodHr-PJQem2fo2jE_Tc125MB9t8AFL8gXgpjhgOtiODfx-5KXZV0lifidOPgNj5Nfe_gbhKql61uBoyFYOyDHXO4ken2ehVs1JcUmJXS2lzS5KQB6Mf5K2i5LSuowKELgRBwnCRwovNufMf0QyZjz2y_LTVV3uZCXC1QSeJPLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1O5NYncJZsKHikLReDAJhYRtWHoBDmK0uAsbVpllVvpQTtZ71Jvmg-i4i5nYWA91K3UOoqFmuZqycorhry-Z9cgiyOtA4veJESJ2mAnC0iwekvM_hVPbyeCNs09pCY_QGQJBYies_7tjE_uHnEhVn8MxnRZ8J-zmaSSH50Sh3PLGnVVE7SfexWWwbH9WUpvrovK6qumCi9_OEU_PFbUAyQ4rziHDuCIyt4XVMf-w2WGZPaOb7czW-cim-EKnnp9D6uBtEyixgML07WAJi5BvfBKXaYjhFwsyGSE3kRlyj1RkAlcagn8RIO_a9aX7CcLhcL3YIu4k2yvfR3I-q3sDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3y21RUCGnQAGTlUm-5J7_9w9MK-pYH0GzAWCDI0R3slaQgle2Wu8wEQERmTlPhK4PPLprPqaJvuTm143460tTEFENs_YtP1X3uhXUwP6goNqOorrlwxUdMvAFluh7TuXaakqcoT_oF4dc3KJg-QTm7CcuqGGryG8FVvs19BIlfVa0lrSR4kSlH-5PvfTQhQyH8fCGuJE-Pa5ihVDqWha9-C5qUpQ40jZkXBdI_c8pO1RiuyFcHoDj_LphA9juaypmondj0TgXMRzncSQtECLRXg16Wwjw51rpeoOD7pp0biXCPf-YdDIqj_6AjW0phpIOtg2PbKn2WUBO8kNisn0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdjbahv3uWxC_4ya1WKRqHUQ6Mg9aDARHNIwMYVI6KnYmIPCQHgTX8Q1KONeqCF5rZs1LU5GE5RMnfOFnKoaOeiVKbXRJg4r3Ykaf4AvtmsVPtII_Qaw73c1kl4DpIscjSafhQUGbk2dKqKlHe0-twsNJ_9xs71N2krXvENAZUAascHrtxjRnl9zJQWQxxJqvt4D_Ead2DjOhSlb7shtypnwOyJ2pevAuUCvj0MJECfB4F75OCRRlVmMsQ1SLdiGWv_CbPOV45bOk8-QXLx757cVwypoAnQ_0UNn_jbboevZzO0jtohNLCEQsOnHfV3MBXP3KvIaa-8AQiuKQr8q2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhoksXySEZ_2qASCv2HHkecNrI8dJhUBHNB9NBYvsWVN2gghcyF44rU9M9S6qfdOxqM84NnXHFPHvoGgGL6V_zcQh1vLSZ_FQZNeeui67Xb15GoTSi5yOLQvVJQHQg7OUXNkUiVwce4eCMWbphSJf3_k76Gg2BeCtD-CFXH99lDt_UXVXnGqW71n8b591aMMkILdOn7ZreKgQ9nzdzr3LRxq_vKLn1UO4nTMKuh8UP2LQk335Fed2B5pUtYZwnl4NTdwdg0nQXNrih1kK30Q3rtT2MKSzZ8qv5XO-J7cjPJEVYZyrQNvJJGC9tnWkQYNP0sN5a9njJBZ_eLDv1lU1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=nxkzKt5C-h61RCHpWPUZwwDLf7WFrmaUse8Hig1j8MgjFvc1iFdMnFmAHKbFsrTOQ4FiFTYxFVUZxf284JM6Njz47AhZb17RQ2VA4224YVDzKqpC7in_d3-WQDMDhahd0mgMYGSdv7rAhMmUyUHuZ3rLNT64CToB26PDpWbNa8O5Dz3V-ATBpMzGg-aPp3Tl0T7mjd6PSO92Hu9suWxcgsQWvWMjlgVA_BxHf3c6umAMdL3NI09dfxdpqPPJy5aRIEmVtOhBuOTU1rXJYfFftpB7WrUWfLZBv8m8jb-RRgCQ6r-BC4bGVnlZZjFIyDDl413oBpmka9TGVXb6h1SUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=nxkzKt5C-h61RCHpWPUZwwDLf7WFrmaUse8Hig1j8MgjFvc1iFdMnFmAHKbFsrTOQ4FiFTYxFVUZxf284JM6Njz47AhZb17RQ2VA4224YVDzKqpC7in_d3-WQDMDhahd0mgMYGSdv7rAhMmUyUHuZ3rLNT64CToB26PDpWbNa8O5Dz3V-ATBpMzGg-aPp3Tl0T7mjd6PSO92Hu9suWxcgsQWvWMjlgVA_BxHf3c6umAMdL3NI09dfxdpqPPJy5aRIEmVtOhBuOTU1rXJYfFftpB7WrUWfLZBv8m8jb-RRgCQ6r-BC4bGVnlZZjFIyDDl413oBpmka9TGVXb6h1SUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC2bsVSnJoyMz2vquOc8lriJCbOv-0NjS03YAfnoEJnIYvoLq3RgbPFtyhwuYenI_TH1M9RJS1mhvRHwA8PKaXdR_jhYpzJkMEV-C9pW7VYJCal3CgwvEvrR5xAm7f-XDjPM8sEYpcZlSN88FFQ66YIywT_sLi20Jum1HFfd8PM09dQFA7NFeeCfSx_8TvLBo9PU762AEm9BZx-0iwtc27OzthOdQ5xhTL1-dIpJkwfTPBDSKN5ccwrEzWdV4KXMhFdRREQqOxH8mcScdIXgio5aZ3kpRKXQPI0SXjUuKmfjplnXo09cQwg1iRakeYIusVrGyqjaVULCMhClgPkRCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-p_XdocXY5lyksbhsMbkNhOMndizTgArD1-ZStD6MxM8okv5DHtJnRthHhU4UeKRDNcMK-4lyle5jBVznpbNOBTeJkzL5AuZ5gq57QHhNajYy-tblbjb_auc84sPAPLS7EE4mIcOnSRxL2EQksSE77upwWKS2NMCsgeuKKaY-3fBSCNCcxw-qO-Jsrd4650l1_SejtB3aFaQv-syCUOgnjytOrWxzhSKiREE22q_SIHEbstwbb6sFUrw3Zr1qqQAt3kLZw27Qnl0vcMREahLE5bvs2mxLlwykgEjFzL7eqrRHgABTYpcFQjfvqpzjfHwFpJR6Vm5IJtllJirOisxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoznp2IkKv1AEDiJoQ9Gq43oQA3GiPZrC9TQSEuKGWfgUGjEG9yt3w-3c-uf6bgDN_BJsOGmHhfC5UMRBCx428iOxSvT8eBdzNWFA3Iz1AwkJF2n1_he8NUS5mN9oi2utZp6jGourHno_tFCpjE9bb0cabfst4lzkBfW_UMgDgEeraBXxR2jzIHGYIUQg39D_65ogfj7MgbpO91FPL7AK7WCwyXa2iHtBT5nL48ozYajdmqbs2S-6Lgop62VDFbeN5ngwD3iuemDfLJ1Zqa_RoZdagoTL4e9gig60UGzahWiFR2Rc4LeAGm4wCU8r_U9KTGxGpyFWK527mz-OnaGKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=YTWF3WKBoLLy5bs0aiEQmyKStKuT98X4Gyaf0pSZuXD8Uceo8fGupiGTGb4tz6aRMLMyBGEAgJm7c6Hxj2V-MNQDMDXsQQQchNBLFVx-BB3gjXMKkrc0wjP0mLYbmBvEGJD4PD2aNhOnwb_yUr8Gj81STKqsfq45XuBsRFvitg49NzXq7QujxCnIUuWSouTeS3lBZZzDcyJGbvaiCvna5YwQ_rQuV0D5FF0B60gWi2tSpPgx2ET7n4FhM91EtvJOZnm_AodSgz0RWCDLdd6g5dCNnwCMyrEmafI6QJo26eNlkyInaDiJbx7GJ3zX0-mGTQLG7FswlSzK468ItDlc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=YTWF3WKBoLLy5bs0aiEQmyKStKuT98X4Gyaf0pSZuXD8Uceo8fGupiGTGb4tz6aRMLMyBGEAgJm7c6Hxj2V-MNQDMDXsQQQchNBLFVx-BB3gjXMKkrc0wjP0mLYbmBvEGJD4PD2aNhOnwb_yUr8Gj81STKqsfq45XuBsRFvitg49NzXq7QujxCnIUuWSouTeS3lBZZzDcyJGbvaiCvna5YwQ_rQuV0D5FF0B60gWi2tSpPgx2ET7n4FhM91EtvJOZnm_AodSgz0RWCDLdd6g5dCNnwCMyrEmafI6QJo26eNlkyInaDiJbx7GJ3zX0-mGTQLG7FswlSzK468ItDlc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYWMH7DX7-McJ3nDvZa3cPyD3vaGcABUCmA2_PL2vhQpELRcT2jFl3Cji3a-94G-SRzO3t_4M7OQW4J-2bss6yNfwxXh1jSeMQ9Ce4l9YXc2VyPybFqy6Dhh6NEi9FQgSi847GZiNHN4aRScwzcieuBSlVAfRH-qpxFqa1Z1Cu_hC1L-1enGHz5X3gDhyjg5JMNnuL3kX2G2si0miwyFBx0AJMET0i6Sl8lvenXddzaQyzXcROxbPpbG6hQDVln72lda5GiFT0PklibO3TJkmPQGSbsBywZ1lk5AJOQaAsQweYFaOSQ8AyXq_fPqhi0L86s81W9NukJw1NdKFyHyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-woU0g9rHNY4vFKjrVLaVDQ8vAuOhvam_M3CoMvwhcPn9zhbAaY9nqp5c4KK8R1xE2MUDIJQtppI2JPEB4NxOEQAHUx7CcSSLPJUKzORjxxSy2e3u-CqveEZ4nVY7vPuhgfJNKeFR7vM958vBulVTuDSCsydrW050nvhzkTpBH16TGl5gezj7xrM_jqwgKnlLZ10GBjfQY4v6l1bMPZVr4R1IqLSGBoy0E294HFhqfpE3JQwPH1inMjtTXKVl3YwvAzRfpZB-mGsOs8SnIDI30-VeqsSkv1W8SzvHZGn8UGzkxMsVh-mZuw-vnVfnHvaQfBlrXrmrueKsXVb8Xdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhWf1szF-2FqqmAkzHq8WeRh2A9cTOOxt5nWFWNDyNW-NGh60xj1tb2C-1o7AbXQEsu3DtZSvyutc3FqabP_9gHQ9uGHnAT4gt-JAEic6nFCxtmzcpaU6sZ4OnmsgYdC2VMv-GFnLkKbGHaeJ2_wrGVo_sgPB-Jwao1PBSOKQltlyT_K35H1LMUqSCe60-T7dte_kwSD0XlXthiu2mBz1-uLTIjH80tEABfDnNgHuOeH0lWITn6LznIBHeSX15VltPonzsoi645FNx3bITjA97eSSCLUXP61k7m452V3akFSDmGNoY13C1gUQA9d_oU-mLnzNQ_ZS0mUrp6DEBc4cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd0QifuUroglwfTs3gJb4pOwxgEH40dwzX97mKvZgcVdskKbBlgJOi5Hs8D5o4v6SoeMjI9KomIiW8jWShNPn-n76k6mC8JcWZli3vSMXPTA1mHPCnwTrnCRrD_2bn5g3cFb5KZaWXIA0dMCOFIyvxlGRnFRxS8Xge206P0pdIYM1Tu9H8OQDoNHR8x_sBw9pzDcOeV4JwIMDdwJC2NZd4HfrNb7A5facVhgdAW8jQL8XLIdGp3qNuP8fhMriHzm6J3BzpAd5knu3hw6LqtHE5ZcqMHtx3bijvzylQSbE-fu0uJWyPZIH1FasLEJTGd56J-OeXxYSP9KtUOIlxr8ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7WayAFX8KOp5YcOIZM8y_3GX8FIe8GO18svxYESnXZCqm_b0lllRT5KJLeEFKdRfHXMYol2IV5eWHLcKMU0FdfqmiMgHk10BIw-RI8XkXdgbo9vM_Iy_cJqIZEwCUyFlxx2ELkH0BzxiOTvUildjMCmR_XnKJx-ITGNItKPbgeoY42-WVAVzRRJ8-lgU_ZeVQ9i4ktqX0klm6FZshWf7NLs4649tEKCC8lyHqA2Hy132t1kk8OJz03JXLQnmHNP1qjbblSsYtSBLJMsmKiT97la86feKORCcALfc1PNxtcpB7HWAJhtMJaLcHof_W_cQIs719Tyeuu6s3Hcrf0NcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev9rdBfqX9BK5ULSlPYNE_qw-8mktk86odXy3T9J5wJDUJKlmn1wsMuaRzliaLM3SwkAY2tCZPz6vcpdLqd2aeJ-6vq-UzeT6HjSupAQTk3C0qtNtlaM8ecaHVqpdbo3ryRQFi0itquuqUNS4chojbM2hC9k7BAsBK2GYNdB5vJ3m-QreNl3T60pq_pwSBLhh3dbNk0oXRlW2zRaHC-y4q5jAvfRK74dddRe8tnbkQYTXvIk491Ssggk912fx40rHfMCCG_doVSOPFQGm0ssyHdJtbkO96wXn5pJbedIg5S_Wi4D7GiUuMKDoqKG_0hkovi0eVEw7N9lfJwZTJVBRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Usri35qD3oYV7BxTTShWJnuad8YrunHn4GroHhVf60--j2oSOXPRRkmlufsbi6pZEDuEO5zhOcvhsGwatjQ-IvVLHS0aW6q2Vwku87N03XBf6Ep_aWrb5YrtvYzsWWCErvEa63RXKY5bWB_bwi7Bzj6cle_IiEN4Wg7gF2S33-2arBHQ4uCCetxp2jTX28NhOla3njDM2W6MXFTa0FI7_lmidQyq-MVzKlAaNAyOeIfu15ORRyl-zxzBv1emAqBvrpM78jyi1qAhACBpXtrznnahb-XH7MCH8-wlTViWgT635RgSmOv2WbnFeEOJXhGjs9b7Ffz91uXE2rWy9u5zfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Usri35qD3oYV7BxTTShWJnuad8YrunHn4GroHhVf60--j2oSOXPRRkmlufsbi6pZEDuEO5zhOcvhsGwatjQ-IvVLHS0aW6q2Vwku87N03XBf6Ep_aWrb5YrtvYzsWWCErvEa63RXKY5bWB_bwi7Bzj6cle_IiEN4Wg7gF2S33-2arBHQ4uCCetxp2jTX28NhOla3njDM2W6MXFTa0FI7_lmidQyq-MVzKlAaNAyOeIfu15ORRyl-zxzBv1emAqBvrpM78jyi1qAhACBpXtrznnahb-XH7MCH8-wlTViWgT635RgSmOv2WbnFeEOJXhGjs9b7Ffz91uXE2rWy9u5zfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkIRfosN65Ep-WXqOHE98fCJ5tYUaU_2Eu0svjtBRGhqQtYW8b9kSlZtaeXKprvv-J_nuzMdG9cGzKPoXzTFsPLZUjm6Oi9NlPe4UhiXHse_qjq7G4CCe1Jss17WSdWHILf0gu67FfBIOIPpEN8oJwk5snvtPtzml9MPQjpSlzIfl0Ml7G1sdMguBQMzQFatTnJ_OwJDHZbz9R-zUnFMM24FwoCl3PPT65uyeHYs62AKg8IP-UhyLR4oLy7z1ihMtoRsup-yPnBIwDRSyOAX4kMqkNvokxXr-SAiMM9M5c8HMajecodPnx7vwnZoP75Bq9fzTyNrK3-77RAWcne-tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szHFeFYRzp8I29JDxfTQHndN7gJfOtebdcDY2wkbrjeJTZbX3Pn1G-5Fwt4EhGhRK50vkPxK3736JTEhDEXLxWxGwugfcNromfIulHCHuc_GYf8akRMyJt4g6zx4YQYkPLxSdOna0y0W-c_sVU7-XDa2_5yzY2TSC1PErkAJcSNEzQU5CvP7ZDQEZHabssLVcquNbw2rORiCWhyPAN7y4YQ-R5z2y5pU4YhrKGMrOCDix3aO3BsZ9WEyjLVwFdBgyNPB4a65NC6o_vP0abiDTx6p48xRB1bxS58rarqW8SVNldwTnwAnI9WOTOEXiygz-r2MEMp5WSjN8dUFMpwv9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5rOBzVwXH0Bm0R4Lvsg_p53dUJgj5AfVBxDOUI3YOWwYe5kIa21RaeeLSVx7gizDkfsj7_FXph3CpHBQbGm_Kx1rgdh6nspuv-tyPNE_yzU2HKxLFLCrTUd4-Tbya5qi-Keq1236vgJb1y8nwBo1Sgdr8YIAYB5Bkgtl90uQMf40n8uAQ6eQ83qnw8xrrzaZKSuxIZXOSpADDPN5kMXSQwCZKHkLuR_RP04w-fDXfljmttPVFCjiu1Cu7yq0l6EdDkK-CxjznYiiWisSxXfS82ELmZIsc_NOm4aJN9Pw1pHITFBt2shCwN0qyM6vHwD6T2GGqxxmg_AKX1mRjg6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2O7QN5qfvzIWGZ0REZynsfs-r_E1vs9RZn_X8Vkv5uRaQpV7UchiU2OXwxfM5St5OBmMMIxmFZ-wE2B1vWMDke_ClRL25LXJLnbiNdGFk76qPaq8VkxtBifQ9pHwc_iaZo03zY6RtCkN16EkIk8JQFvUiFf0eF7815F7dhvY1Ujq6Ffqo69rKqO9PMXIl1RxCfMGAlHNaa-7A8RxCJM78H4_wXFC8i5M4uqHaArilyLZhIvF4bgBlIfbWfsMmImOC-JpFaJs8Cj8bwCT8cLnsCSsLsqaHK5JRdGT-ebEic7yZNczmDXgGflN8Ohhn6jCVDtwFk7ad6ddq5aPfm8qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=M5pM-Gaj7NDO1I0Lk9asXbjhoKd2ER1ALjademOunEjjqqgtvSZ4PDXncTwTx-3f27x13wS-E0LRQBjXNUyoAx5FIHmEpL1X3WHUpu5XVKXmZJK7kBVSMq0pL6oKciehpjU7tprtmOIcG7Mar4dTS0pHemtbYKdxq2-UZg6V5p7PH34foe1exOnLW6e2TvGFOx7zT6W0eq3dot-0aqBHTDEb8W7_p6s6hl9V4SexmrfYvSm4LwmMA8vqhQmYkVjF8vWtYFlXqEE-6miGi3cYhn4p-pACWUII5bK1azluOGw-n57Pw9ZIyS8DFWaJTTVTZz0A5ld8eyilSN0le8mPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=M5pM-Gaj7NDO1I0Lk9asXbjhoKd2ER1ALjademOunEjjqqgtvSZ4PDXncTwTx-3f27x13wS-E0LRQBjXNUyoAx5FIHmEpL1X3WHUpu5XVKXmZJK7kBVSMq0pL6oKciehpjU7tprtmOIcG7Mar4dTS0pHemtbYKdxq2-UZg6V5p7PH34foe1exOnLW6e2TvGFOx7zT6W0eq3dot-0aqBHTDEb8W7_p6s6hl9V4SexmrfYvSm4LwmMA8vqhQmYkVjF8vWtYFlXqEE-6miGi3cYhn4p-pACWUII5bK1azluOGw-n57Pw9ZIyS8DFWaJTTVTZz0A5ld8eyilSN0le8mPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpejC89nvIJ35tA1c6n60OpPEVMckN_beLJaE5FjnMDCG_bdulmoKeYdv0HQ-HijfZmTOrqVww5lnZM4bEH761oiJrzdg98JnbVh8dyBEVPI09fs4hSiSuyOhmCsXfiV-Ezd8x02XUNjEDGA--njMgphs91NSt7uDHrL_UUGUIeH9K8ozsFObBQRBU77GM1TUJNnZp1X35k66rfJyXzW4Fq4_dbwOEOZLS2hFv_7nExjm7tWNnif_7GmN5Hq12Dqm9P55rt5nY0AMT4isz-Wveeg5Bii_6IZdlJm-s_aZsMoe0NsQ3xXiAmSDjG-mteut5R0fPJ_3hp8H0WOD0rTvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oR4L2K7cyByPXaeYSf9LaMW2Hxpu41BfeogJ6acvKe23E6vZmcptrbRPtcJP3rrQr5hYRDYGu6Bws1_7zG4PuuIaPVG9CCOkRATdqyYGwvHkZFdy2wqFTUn4gd_2QQNwqRciV7GyvTuFsNNgWPY3P1JdfZJ5MDNrcdOwMPNWeuShDSOWF_w45sQ1GTsklQkMprOZED5bECqdxV7_4zqRUj7a77PuQeRuVSN5a8q4scviE4KgRc4EbSu1V__dG6r_ke86x2PnVRY1XggC6QCC0ptkHWfg6_CiWlBONJ7VaVjMV7H6Ii1DDqqY-D3TmJ9KxBDJazuJEUnqkumRAycPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keqBuuSgw3LTlqy3i4d4TNp8TRRM-jWE6L033cpTNjLLLsCOZm3C7MlpSUkG559CT8F09T6PCZOO1C9nW9sJYl0cUXcNUAuq8FZ50OQkrgYt5JGqGnTwaUPoGOX9Cl3gsz2pfdCnDASSHDyUQbIcuHoPBRa2WrAymoKQeYP1oc3NewDIAbUiu0CQlByGTKXGPogkFRmPVb-xlF0g8f8Nl4XyjkJ1DbEdRCaZB_7UDQAdeCTznMYMkdFSi9K3mt4OJHWpc-yAb_Fg1Z6PPsrCmijz6fP-EmrTIoPscpGzEd5smEQkzqyRgpT4VfBWBnhdtKcYN-qOs12niXj_Vl1bPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWzUYUYF_G7PNbFnNqUM3zl8SQKkQ2N5QBrC4WiWRo29cz-ViFTf_a5CM_y68ORO-bsL-nPSeqlDIogC-hG4JU4zF9Yyxeawc4_AOdX3yyNIszMMsp1j6c9bin3MejTsuS5QAgwdOh7CF4jgZi8TQHT39tO4Z9kzd60K2HC0YiBNrtrOV4N1MA9XO3K92n6-mxBRWYFZhWjQ2RhWNBEVeKRy0SL5f-4szcBfjalUqETVLtpgEEpXGfAR5gzie2XSiwwzBiAgg3KQY9xsE1lxt2uMP4jTJpXywg0qc2gT9a7ukUnpYIaALVvTJgVXAHioZBh7lfBK-Xf2rOyfh7nXvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=vWo6RqrEryPW8mtf19jM44krFYzIPO7pqU03xDymV-mzxOKDbi_uelsWc7oilNe8wAvnj-gOHaLyHIW_hbYVwnRfCJCL_oxz9-9z3Y4zUtGgQzc92ri_xCJ377-z7HmG5mj3c3OUOiT7tj-9iARWdlm92oPvTkwg7Ww7zFf29Oe5qMBXguUM5A1DqrLyAiO_TgGdTVvJFoBo7OOT5GTy__LgU3hyt7Q2Yy6erbZTxnpj3W7N3cRuFecGe9Kbe9pI_JWhOwr0eLz1z6tBwpjHnGxWKa0524c_RLsFJXrhLtQM6GB_9VZkzYgtsjK7PV-fzTdjGMSIxtECXe3Tkh3c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=vWo6RqrEryPW8mtf19jM44krFYzIPO7pqU03xDymV-mzxOKDbi_uelsWc7oilNe8wAvnj-gOHaLyHIW_hbYVwnRfCJCL_oxz9-9z3Y4zUtGgQzc92ri_xCJ377-z7HmG5mj3c3OUOiT7tj-9iARWdlm92oPvTkwg7Ww7zFf29Oe5qMBXguUM5A1DqrLyAiO_TgGdTVvJFoBo7OOT5GTy__LgU3hyt7Q2Yy6erbZTxnpj3W7N3cRuFecGe9Kbe9pI_JWhOwr0eLz1z6tBwpjHnGxWKa0524c_RLsFJXrhLtQM6GB_9VZkzYgtsjK7PV-fzTdjGMSIxtECXe3Tkh3c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
