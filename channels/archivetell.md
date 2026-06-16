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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzIEF5uxmVT6w6jmnnusFbQ3oxDWoU13ypadYGBZe3iioKppjOtqOIGaYrcjemHoYVX0gHaGe2xitKTC0qUbGOPiNnALfG0tM-l07JiboyxTA0WmouNZlr292plyAD7trJRvhcdnC7IanmepzOeHDbmCvyVBrdbHcu48DWBaytmpmWPEPt7wRtxA2jT4u_hJwhCpiDuDR1kcR26HNs3oQ3GC6N8fxxL_Bh7c6MVNVBdrK9wnIW31MPCAWBPpNax9IsakPJVprJGBjH_dwUPohsemJXegps7JWzSGA_U3HE-87Kc_E6m-SwpPrYSi52P8_st5oNMvJjfAtwZ0GidRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=EiyH2ogH-b_1maQ9J7gMO55jBxyhp4nNOcfK03YmreMdDHyCaOVr03VhPY3yNMYdHZINAempno4Wg7DfFmOOPMiRMgy5vjp26R_N7qJWlWb0YBSU2cUDvt4jk4PClVfVSt6lsNPLr_Gl4-UaiXJHn6yRlxQHXVyB_KGbfq7Mvngd88QM7szPLSBqNDw8fYup_uFCbYsiyIHarziRNHnsM3Gt6RI0dwRv8UAbN1NwcohhtZCJhKyBVjChMJ7r6StweRzF60aq90YWT06-jARvPCJn1pYxmY8hjxY93b_hnJ_uvkhtePzmeztUi1g9IYwBLnRdcFJAwKN5ubs5okdSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=EiyH2ogH-b_1maQ9J7gMO55jBxyhp4nNOcfK03YmreMdDHyCaOVr03VhPY3yNMYdHZINAempno4Wg7DfFmOOPMiRMgy5vjp26R_N7qJWlWb0YBSU2cUDvt4jk4PClVfVSt6lsNPLr_Gl4-UaiXJHn6yRlxQHXVyB_KGbfq7Mvngd88QM7szPLSBqNDw8fYup_uFCbYsiyIHarziRNHnsM3Gt6RI0dwRv8UAbN1NwcohhtZCJhKyBVjChMJ7r6StweRzF60aq90YWT06-jARvPCJn1pYxmY8hjxY93b_hnJ_uvkhtePzmeztUi1g9IYwBLnRdcFJAwKN5ubs5okdSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMEoGtApO1AMQ26oDl5QiUgWNIpTcGUx-y1mfPcByolJeYLcLupHhtLuvD-hoV-2NENk1661LCDcqLR8JwKfqbBWj48nLeHsb0NNW7_xn5sIrVkx8w0WfMO2xBXry6BaZ9q7y_82Y7jJPpz_alSV1WBb61dBhj1VRJes6_RwxwTMa0y3Q7n5UqsvNyJjMmYnln5nJISiu_l2US-eNsMC9JHrKNg6gvLVRYLrqMGozN2ad4xjMP7GEvpMu1xVRs0B_gxdzH0X_goDA7fOlFE4XwAt4peG91Ugux2gnnXVbMBfWJ3CuOK-3BCqRyCvJTr4OiQARcEGuSqD2vYwPmy9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXCYYDaMk8QKW2AX5jaSPypQqur_8TUy7zovNHHlsnzPfkCWmdSEQxqNcJV09fEQmp9Z8STgJNkWscivfvRJPl4v9ITCMurRw6WZooaje15vD-OdWLAgQUG1e3lxx8wPVjDH89BPSh3GVqOAE_5Mh2ZIkgnqCCdEFezetza6kSjw75WSd1ZwwuZtgMcG9Xm7fVeB_zEs2uNke8YbqOAIBVE6kDPvhg4VEbmGjw20dyjhzp0pAvQ6TUxQjlvWj_Veu_JWMyUtO_mEwA4uaQeQU9t0gRlPnKw-fpwzzfuLh3hCGvLTi3TY8fWU0H-W0UhMdbksMVpFff2C4QbJeTB7ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyzRNEX2Suno6XKiIc8BX_j9nr8tKfH9JZGYxaznPozzD-lvl8x1vEI7RpNES3CM0dDl9an5MwvB3dZNVmN6JW1hYTG0XGQPSmAtto_5vUMO3AHdB0uVGbWeFpxNK_LysUve6wBJ2e-xh4-AEIZXUxOqlQCWaYBbavvlaDkJ4mseAm0ejAWWlTFmdQ3fZ03_HboEQeZL9WGEujW9kapVOmAZ0ZaY1yShItcb89S4XStDSIoI1_Hjmigj_6QEAWdYXIM1DZsTxQs5Dhumj5enb8YmLJxAz2n-b8dPm54fhQLqhV4h8WORiTBxuC76aomuKzsxtTgDwusUrV9cekPuEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugqr7duwDcYEK5TbvDYhsbwTz-N3Pb8Qyn-kWzR5cKm9f9FvrlxJNIkrFhymcZbVqzTvTheK8qpBXfoRVoiJbyA1EMeM9adUgQHTiAa1Fz0pZxo7uxl1qjI2ETO9JOQIg_IM6Jvhxw_UrL-KNmm3r1BecrGS6vC1YDPn3YvD0ii6kYNevGDhaRojpqtOE-QP9Vl-rJbrspVrefIouYGc58b6uX6rvXWSqftoFT0GaYVBf5U3kZQkeL_y2kPwpdjXZdADQdtLzOuseQYPPskgwOTlH8tzq2Hn0iUklNpv-DO-GDpwA3UM3CRWmfPpIuc0i8SJ4kSZbzKXXivcsb_IZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOK4Sjh00ApQ754cVl8iOuntwwBdCKtj_XNCR7O8DuOSp0XX1c0yrgHlynw9nCRpjnvVHerrX1EVIXmuPN1UvrpuQNq7naQfo8qs1iIXc_kvCmg-xrc3zxZcNKUJX-vJPFZwZlwMDXgDnEA4bLUizYOqEcT-DGDo5pQ-ON1YqlSbEjxtrkvNbyXHn5PrqT5KyDpVM5m_5prUwZQKPZ_ILqI7Fe2_to2GbFIAY-yGQ3MlAOAmH283VQMXQkv6op_C3VQ_ey_ae3dOpLQSnJ1U2rV202gxYRx1Fp351r2boCelLqO5Rjerc3hTznRUOuQ6Tr0_OpAZUV8JayAWajpSWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCuYDiN-ujsWvRnsnDTj8L_wP4wV0CujPKbgLlWKJD34nGKnbeTagCiFP8mmlTcPUGsKl5dWNzJqGMBsVZ3L9kk_lc50wF18qUb95DvTFpl9JQiBUUheVjwP9OI2m7t_mhV0lnIrFeA0zZmrGfZ4xoxbziDIEt074TZY32JmwFWIZ96LkY5ioUznV2Tox6s005WEAqO83JUjwzMoRa-bVbHY0uZs3zJdYblEo9M8uEEE3OF3t1QUZ57On0LPsSBIit7AVWJ_vDWy1oHKO6hezLXoNUSQNGzOL9Tp8LNpKLIthgTkdWoou2pcgGAVbGgVq4EWeFZLFvQN9zn-kSWJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIbJ30m9yjpcNHhcsUV0j084Ctng5RGW_AIPBq0je5d8vFTuISDUvpPb6ACzI8RrT3r2lLelJYZ6FmWrhoq_VHxWkeM4RS-O8yDIjNUOpJYbHSzpaSTaXDCs-zXXnUMCfpe24XVD9pEzCpsUQmQ_aFaEaZINEHCImzF005FtN7pTzJ97KulES3JLqWlBOpS-81g-lDLge7rMb8ifcP9nXV9w7awc9iehTDhk1eVBv3LcGIv4ZpzRTqeXofMLOVMOrPNPYiEYvciFi6LRfURJCDflJDxnApnd4ZJTTbSB7_co-ZYFX8yXawg_IjhWgSm6DcZqZk-c-tpChvXXNekoag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOpT0KPM8AdUBHLAMXKwI8RmhNbI0R8CHeUjYvU3gT9-_ydojwDVrYp7F4P9mMHgh_8lgMGtmb-GB0h4IfZZNavUOhvKh935HZDqCxCuBPS7X43Quladkq9mrP6Lf-fjvBMibXvfah-p1h-YfJ3LHXwuPNMynDlv8sZVV0tmDowa5pvo4c-rWJPX2inYrceOgK8_fCpmg4E8EqG2SRIVwM5qBzEuVkEVhvy-YfXQnFDSiG18D_Rfz4-qfLgqujEe_5u3Z2Sj1bgPRO-EoPnADIvEjw0-BU_jpqAApbYLS0GneRxm8Wa5t_bUQS82gbyZYCE7YNdGNVEKwuQ9fL6Arw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgjyBTaJiqtn-KYUXBfTTtZGtKFUCDxb24MAlGiz48xjq1os0ILwDp-VkK5ZjOqR0MF9YhhmuMNUVRS0geQGoahGxMJdh_8H5LV_xM-ahZRyoh2VJ900El-P9svQgUL9oeLtO4fFTje3xC-uRNXnUvK8j-Nn_tCr7PKVPWBMkM_c-Nf_yDt_b4vJl33SkvjJsY2OSypTf1ZoEEOhikSGDvTS9_99oRhPx9QIi7F7iBLKOLZWHUl7l2tgsvlWaTvT1CXy-I84QCBHEArfxeA8I3PU7EP7HZDy2PnR7r6DXs10fup8NnCPwiRcxsNrPZ8rFwGYZ1kscTKURQP-Xo6QYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1yLH-Tbfpo_pq-KrdyF0ZVsK4eGJKMN9lHEo8iybBr2CkzdaeDfcaimfAVpcvZj2bFtirqVmbL4_IPuay3eb5jqK5tV-10b7KAR0j7IMx1BGmzY6RCWOoEX686C3tQ5nRfFUG5rTAR2zbu54f8dJC0TlH-d0aYOquwDpwN7EK5y9sU2qncfgT4zf29EpyidKNSy673FouXxnXYMbspQ2YEAjgvtfoB8BX5r7mbiTYZoohjT_jKFym3wRsDTJcVE46qGNwNrRqei8ZHxXJzfODoXROR1lQiZR7EtHkMz7Kqchuog-irfMmF_a2K79Xhv3RH_9ALTmx4dhg9Va9gTkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=W8R-ltKIZ0EW4NrKT-BvEWDKBPdRIgApG2uoDvJQ7BM8djvj_mDCYu_bpzzb-5MI_Nnz-ld5KEARrVnKEhftqfQqfq85NuOqHk5sM-h2QQW2bO-W8HiWG_U-03vrsZKk05KQVejntJrDY4GXG44IcwYOkPSruKTA28R3nQmq691Tyk8mHTaL1xvTKiQoQQv6neIaYOcb3q9fAvQV8kkhjfr87Jt2-OIOlS4SmtkaFtp9Qjrm4TVVPY5d4Ir909No7UpQ-jI2VUtmqdpwwebhGpq57Sif8KZHiHWEd2eO492VxWIGkWu3N2wiGunxdZNGLAPPG8Jbv4ua7EoerFKw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=W8R-ltKIZ0EW4NrKT-BvEWDKBPdRIgApG2uoDvJQ7BM8djvj_mDCYu_bpzzb-5MI_Nnz-ld5KEARrVnKEhftqfQqfq85NuOqHk5sM-h2QQW2bO-W8HiWG_U-03vrsZKk05KQVejntJrDY4GXG44IcwYOkPSruKTA28R3nQmq691Tyk8mHTaL1xvTKiQoQQv6neIaYOcb3q9fAvQV8kkhjfr87Jt2-OIOlS4SmtkaFtp9Qjrm4TVVPY5d4Ir909No7UpQ-jI2VUtmqdpwwebhGpq57Sif8KZHiHWEd2eO492VxWIGkWu3N2wiGunxdZNGLAPPG8Jbv4ua7EoerFKw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSHby9KUSff-kn2GSqeVBXkIBMC7wm1ZMLFMVBB1ANgDU953SGhX8tWoSxa-LRyYHK6Gh2cIh7g_Z1-BlvtCmTbAkRS_D1D6ie1l78E6-N0aXRz6hH0J7Qpp36DdbXCvjwsns_86rLdyQfaFl1xdcsTc4n1538Tamo-tiwNT5ZmAYgRtctKJKaTpG9tzmeTyTI8vDy-NfXm9D_3B6LVyggHCqVbQcCGd748EQnRmLQDpzHyp-nxGlYtQlZnisDssi-GTY5Xe6W3i0WptET1hxT8Iz7m4oF_97wjsuMtKouufyK-D-Zlc_d7tmxUcUjp6KE9RNlwjqXFSmSkN69_G6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6GGdnxbLvjlwla6UxblLFcAiL2rXGE1jiXQ9JkirOES2MV1etCfGH0X8WBpgOXac7JXzBu5wwFXCV5MhcFRHRGhizSOTNS43XMqAgXYYd6LS5dIWTY78dJKJTJxa5Ky9iqp7ueEi2LFEqOuvqq8HilMqUxWXMbuMCp68-K4xqJa9rVCzmAgeJVUHkJIBNoJ1Ep9jVCB1sQ61Il9NlOHt_JfmvszMOKAtUqq32kHJvHoxc7U6LfdQpXi02CLuj94dUhyFyVnpI8I6qnZ6-v7pELSP577-Dou2hy7U42FVH67cobSE6O08-5I-I22h9wd3EmKsLnuFRsDLsxyEbVC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=GGK6YC6lBSikG1eIR6YIbBf-NZDCh3BVBBafRIDPsQeCvsjzyHp1Dq0w5NR475mmVUSFWTApgJQbGG4WnE4DeqFWl0I6AlNWQNVefz3oWlPE8_2DZMsxMlrstmYi1FFMiYOZDWOuTDlGwMGsaazK5pDeViUHLsGjCBqdzxs02-8LcFY8mYZGB-chqqjIE4sBW-Kyk26886q8aVj5CjTCGBr3l6lxMPB5T8i-cqTqeasgbRbpLWHMr7Gv83iaGFkHeRIrD2wWUw1xbKLnJk3eI7s4QXM--Xa_C3GFuWQMq_4KI5jH4arpwydYSEOkJc773cf7bKco94fp0iUa9X0CBokC-VjmeYibq1Lgc_PuYA-NVJQkmflv49HPZN106E72P37TyYTUFgf7TnPqq_P8jYUWEVatL6Q2DdpWHs6GdgcN12DzDT9tvGmA_19vGT-d-ZIZujwDzwmRyKdTPNLABAvpmosXm_2U8yxZurPEKBK4ofr5a8yc0Jpwb24xUXCpTlkMOpO3qw9XWnr4j27T6V5DjTlVdo7ymXgBdtIt4niGlXM3M7YivTwSyHd6wEZVYaErLFXnfg3_XCMqVP9Gv492ICS4ppKfUw-w2jOFLQOE3R2lfZ9ACuw-LZr2cA4ebt9s8HJGDgGuBv8-tFQmNgyQdtpAeYtxmaDuEg0yZfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=GGK6YC6lBSikG1eIR6YIbBf-NZDCh3BVBBafRIDPsQeCvsjzyHp1Dq0w5NR475mmVUSFWTApgJQbGG4WnE4DeqFWl0I6AlNWQNVefz3oWlPE8_2DZMsxMlrstmYi1FFMiYOZDWOuTDlGwMGsaazK5pDeViUHLsGjCBqdzxs02-8LcFY8mYZGB-chqqjIE4sBW-Kyk26886q8aVj5CjTCGBr3l6lxMPB5T8i-cqTqeasgbRbpLWHMr7Gv83iaGFkHeRIrD2wWUw1xbKLnJk3eI7s4QXM--Xa_C3GFuWQMq_4KI5jH4arpwydYSEOkJc773cf7bKco94fp0iUa9X0CBokC-VjmeYibq1Lgc_PuYA-NVJQkmflv49HPZN106E72P37TyYTUFgf7TnPqq_P8jYUWEVatL6Q2DdpWHs6GdgcN12DzDT9tvGmA_19vGT-d-ZIZujwDzwmRyKdTPNLABAvpmosXm_2U8yxZurPEKBK4ofr5a8yc0Jpwb24xUXCpTlkMOpO3qw9XWnr4j27T6V5DjTlVdo7ymXgBdtIt4niGlXM3M7YivTwSyHd6wEZVYaErLFXnfg3_XCMqVP9Gv492ICS4ppKfUw-w2jOFLQOE3R2lfZ9ACuw-LZr2cA4ebt9s8HJGDgGuBv8-tFQmNgyQdtpAeYtxmaDuEg0yZfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=mN7nYuPeU82PuP0IzBolTJWCxkfcmXVtWczWtGAT04n8QO16UDnYGPNMQdMswmGe0bX-_2JjjVxdwa6do8bRYiZXmD-Gd_qVUc0_JybMxZIix_n4dSHhw4nXxzOp7eM2pYTRweEYYweo1_sNKf7GCaHvml76lyiKsN_EUHnHJQbUVwzyUIZ4SU9MNuC3gZC7GzlxWj4zxRjiZiQ-1UnXp7w2wqqFlQ0ynS0fWJqv8iHDJ9QkPGxJKyFYaQ2Z9UHQSq-axUV-vRL7Jv-xQbpE4ACX4HbXxrNDMxuEogPR4kw5wTPs9xEFLnDhNPWlKHL28s2YNtUFMFywPmUI1x7W-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=mN7nYuPeU82PuP0IzBolTJWCxkfcmXVtWczWtGAT04n8QO16UDnYGPNMQdMswmGe0bX-_2JjjVxdwa6do8bRYiZXmD-Gd_qVUc0_JybMxZIix_n4dSHhw4nXxzOp7eM2pYTRweEYYweo1_sNKf7GCaHvml76lyiKsN_EUHnHJQbUVwzyUIZ4SU9MNuC3gZC7GzlxWj4zxRjiZiQ-1UnXp7w2wqqFlQ0ynS0fWJqv8iHDJ9QkPGxJKyFYaQ2Z9UHQSq-axUV-vRL7Jv-xQbpE4ACX4HbXxrNDMxuEogPR4kw5wTPs9xEFLnDhNPWlKHL28s2YNtUFMFywPmUI1x7W-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAl2vZhPMEIlxdW0bXSYz_DgGpG-zEXtqtx6zNbOynsD-fFVl6fnvwOefBXNagUIhJdc3mU-djx3vpXvGPGu5CYXEHcbSx9VTU0KGomPPfasYxfRlfOKMobyFaHu4sC9dboLiHnugdA9eOIvqYwy-bL3MplBmDKsnHlzvVjgOVAVKcAnb23-yzXUXtv9hZdfY1EuqkHn8u-7U0CLvm12f0tiIX8qVwZm7qR_5a4cjoL2JtLMrxfA8SijZ86V35fvEaeqsV7fiOpjIOpE2QjpfE5IroCqjQtYlBJzsgvREqZiLjRq0XEkx_PhTTZHX1tFPC0ove1FFxqeN_UcvJEbwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VusWosZnulyHaHFOmX5CkZCl-7G5kqN_IQmGJo7T_RVyB-MHT96ykaMra57ixSESQvkVHQ4aambPVyZqqyHuf1wm4mrmhzs_EwiKErPUyw_ULuC3uH9HAX2Px5PoWF-jDHlSBJIMi-aXWYEqhfjDHfLv1GdF_zNCi-gzfa0gkjDjCRtQ0AyjL-ZkbIwG7KiiJy5XWVZVtbsrJS-Er28Qba-vz_L68r68EO8_tgyaEC4MfWC_sbXM8cstCytBysrNki-vPiu7rAJOigh4PzrduZJk7BunXNSXNNUXTsCz7nQdjhBLp9Gdv6JeHZcNkEwonISVWeobraKGg3ZN3j-qvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgX_zxUa0YfRVzmmAuCABvE8Ioa8BitKpoivShUZ3ORqcMqmW0ptE68JMm1cZw2Byh2tjiI3So_fcqKQn1zfdatHK6yiQyKlpAIz9gHrtGGdCMHWnEr5XopK4XfSHHGt0eY5U4CmLXSZ5dWhp73VUD4FJIp7s_LKhpj__8i84vaLBq4Mu2PNgD8BPRVKss9vPdHrp1lRk8mqg9cVYEgu4sEozKJ-Fpq0wO5vck7U8e7HZXQ9wN8rC1U0b-25D8iux22I1heqO4oLBG5z2rKayz9nH4PdsFi5YLgbt6ukBTNkm5kpvTgJxnju9Q1815fqEX28wnc6ZuG-G8-aCFvkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIA8kVgu8p3cWU_v1psi6moHmTvaW5Eq4NHQ2pTr9rFfBlrtjNbEQUI557a-Zmlg49pwSh89apmib7YDi8Tm-PdaUyliVfFt8c-2pzt7ORU7hui1iW_N-aV9q0zXlZR8Z1qDzeou9wmtm5Ng7PoDsakbhBBJ-Pj6CcJN2-BeFuPWl5LI-L5qEvMU7a20ra6bgF6SKRH_cGh8ULIpFKXE7dQP37v36KQfzYijuhz0SyxlHqUuJ6xJDBvcnYYCbK91MS7yj4l5ytFo5OA7630yZizU0JSU6haSsYSocp7Qw7NZ8sN7Lv4UbMQ8SwA4kDGCMbQo0lPnN_B96Y1P2IxB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8XzC6UnAORcid1VzsrxoBKTWmqH3_FfBsU8Nk3pQOa0rj1q-6WdFQZ2uh8snUIyeI36L4-iEavHOe9-33lWXfH70IDjze12vewiXNZx6GDGsCC0ifAMnRHaLjCaj6x24ydST80a7wTBRUaHb4JrEAVBZ6E8evluEy0PqRgOr5ngTDueCdkkeBEA3mTFITM43TkOgmOYgTa8ptb3IY_m2do-yoTAfJ6sIgwcr_BuP1hXnDgE3reNWt-7sUyYbWeXc6AMS2Bgm7yvBls7v9yOf9D2YUMkldf2i996jBk_AA0ExEXbXE6698ShH9FBOtnTlAx0poZufmVl33t2i6ZxHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8kZIzMxGdIz6xcmL1L-DdJuAbS58tpEcxOXfIMRDV2FScmo7i022JHyC-OXgTw2LQR00myTM0N2DBWxl6XIPIJippygs8_yCHq4tJwSkn35W27Pry_g-32m-Kvs3DAaXceiGUjGJQ_XUByFrPiuJYMa3fGxgqdgfXelDX6C6tENAyw0kQbzS4yPWdC1D16goQT_cyKHhWCiz7QfolyO-Mv6px307MmXQiHy8tzE3Q-j_u5wDV-NUuipiJUJij9BoXHGMc7Ipq1Zn3L3lKPgp_2NEo-rtHztC158UZqL7hjc-vi_oo2PBHaIilRK9JNFktYhW3KAGUN4oYwbKPmgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYCsgwPsZTYaoluVl7wvZDI01FWYcxkq6jPMM6g6YD6waRPYTWibzPD3-mNtIInGcqXZ47ZZNeGmSKnuvDPUC2BcP4jDYijnMbe5hgfonyvZqxacb_VaySHowSpUXmzAEcI1irTAw1Jd2KcJGAfVHqmxKn6h25oLT7kqD9fB0ljrdGbrIz5-gtKlsvbVX5Yqrl683Z7-DiJMWfbFfrBbOv4-G6Eo0zmh8CaM8dA2PK7WawWRIRE-6Gg77Qnyqs04tucTQOUYSr6Zdc5ZkrXh1sUyY9ickZ8n-9FcQF3F8xhvxOBTklOgjMy_iF4bQgEmgUD6p_jeft_M2ip1omaAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqKEHk2XzkxYqAHG55d2MyvpeRzM93AM_WnSCSDrfvq91ViXgkeqLns67enV4yp27oyfbRDYFds08B7eByfoh_UbJTE3eMzQUSOfpsAMtjDwDp1VJylDxKmgzU8ccggYAde4AlrWUzFUmR_W96jougpZiII28sp9i1F39y-Dx6sawpEajjMJMq6t3ZAFK6q-P4V0O0hLW2VB4lYXR2VT9goUCexawwQYBZ1p2SdTViBz49tBEXlubElbHHWVkkl_2mBTYR1CUIRvL2ng3rrT2ofr_HIQeBmq_9wF7sbEHDAszrude8fCtZK1GTiKZFdnOzlB2mUDaqMF6nI8JdzKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov6j9O98DDizbCYCWuEnFoFbzcd_ZSqNzT2cLxZlYz_jxV9Z4u7AXEcOOIQz-pCwH6lyCaP3729l7CmVV3CdOy__1fahLgXw7onVXbjDDRdqrL98Se3twqet_xf5JIxpthUd6UG4RPeintKiWjkkcEASMBZ5QmcFzBL1qvg5_2LnCa75RVRtEniHOmZVQAP2VEO2K0iH-W7z26r-UjyctwlU8RGY4Wm0VtfWfYYaQAGr0P3ur_LPEMoKits9mEThP7aOGADOmvpRqpEbt9Qy0k7BiZDA53qVZIc-fUFfNKHt5Q54CCXW-CQaNQlEzQAhVOm24k8Fs4pLsDNjU949Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwoDBHLHKF0ZKPHewEF6I1iWgPJHXq1XLx3Hm3xTnjKqna8ZOEeaWi0FeUxyjj4bR7auLPTQpMkSvnU3W79w4XZHxAl1lVReANpJXisTXBZ3_w7FCauInJuaLIWSfeL6n146NEYdROjJRne890d9quiUqurX_fTdLA_dPSpju8LysjtiIhrkJbW_M3_pMTPMD9MebuYd96jkAYTyIzWmqb1PaIkl0upvlAJIbvj8LLiEMUKbhFbHCTjCIlDi9YQhskWL8awN9fLomPgoPKDA7lffWQjGW8uf54GuNWBi7zXQ0fSYrK7R_OfXPjz4OM8pmc8DyPiQTvx7zhZ01ebIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3DLD5QlEDKk6YtAnqeDnXGaVgLM3eLiTdHRbQRa_wSazgxLVV70qinsAb8_3-YAVtkFd_JPUFJ8464R-_d-L2ui0aBkSIHX2s-Q6DJr13MVGlm4eoYVAOd74HcvQrYInWrpu19tYWlOF5Fk9pc97KpdhfKcSCkXVHiVyq3pGoY3TOMP6atbWNRCVlYjnLMsPI_Uq7w4Rh3xeozB3eXHEfMK2FPLMdkvECMTtCJxfsfmg4mnXHzfgG7B5oe8DXbUqjj88fWxSMb_jWNu1NuO0EfGEJM9UCfKwyr373gzzSSX01_uAU8-xf0dXnu_M5Th1XVUpD0b_Q1MdKHEPbgMPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOEXpAwau0Zqsu5tPZUgBo67lWD_0YvuHUpk_ElBHNHcn3hpKZcn6ycoDVgBFy0gRl-oAZ0ZrCV06ME63hg-dvlb3WjTDf3DQUGrEax_MHXeflcICrMupvOsU4fd_QmxIVgv7wkpD1uARbHJf5KAjaL566iv2UO_2xFvVpp1t9HL9YiXiXc2wi1xONTRUmebgI8X1raZRZzbeJpxlnNoxnCCZNtmE1LuoAoZnbD_0IhtM6ypg4qJo64NC9JLAGSr-ohiVDkXDJt9Iz8wI96JRZDzvfIkLI3AiJGJWgbeY4DSajGZZgXQ9AitRFI2K-eOCqNVww5XK0PKYpKEKczr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=XxfKKrGEklpZMtU2A9BfNQNi54FftjBirXhXYO3qr7TsWdyHZzw3Ngy8cumVE95eorgd_GOpKX5cmsI5ZX_2JexbbhxWhF3gxF9LDD7N1cm43FBxwb4lntYSB2SkATQzp1Nl6UP-RTh_bE2Xzx0bVTYjBv1guepTc8ZqE2Y-m-0DyRuFYecvqCwViZBVSzqP1lxkTS68uzYiXlTAhmR6qYA_AcJpjAqxmZzZS63qh5CqtLjP4KDbWuf7KyRdxMeue8bKa43XBDVjrwED3f4n9VlMWoss_lLoV5PzX7GPUm6gYpXCWXUVS8ULTzgubP8agIDQLx_1391v7WPNyJ85Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=XxfKKrGEklpZMtU2A9BfNQNi54FftjBirXhXYO3qr7TsWdyHZzw3Ngy8cumVE95eorgd_GOpKX5cmsI5ZX_2JexbbhxWhF3gxF9LDD7N1cm43FBxwb4lntYSB2SkATQzp1Nl6UP-RTh_bE2Xzx0bVTYjBv1guepTc8ZqE2Y-m-0DyRuFYecvqCwViZBVSzqP1lxkTS68uzYiXlTAhmR6qYA_AcJpjAqxmZzZS63qh5CqtLjP4KDbWuf7KyRdxMeue8bKa43XBDVjrwED3f4n9VlMWoss_lLoV5PzX7GPUm6gYpXCWXUVS8ULTzgubP8agIDQLx_1391v7WPNyJ85Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg8reWJkdV4QfAEIH6CvJDExppXVqQulyyIhPUVxCspF00dH7si7RJDx-IGXcoJMftenTRIi1AjuIvPb8iaLzJXdxJ1tT86Ucowub8ArzWC2cQKeba9rOMNY9nFKgCVzv709ls28qErWHmoxtDFTGQjSQlkP1vlQF--wDKA3I9mK9E3TTQJFRL3ShMKPEx8HtvFponIqDGdWcqfxG7tBCDhldziqWsHAfATFPutImiDdr92Lwg1daAI6SYfD3k_aWjfCQggyRlAHXR503461zEUg_-5AVFkoas0KKZCC5AoFYLCZRwvrCQt3fVeQubbuWmhsKiRPyZeFe3OSWfMAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpdRwQSApw_ahvFVgmuXBRwWV9j60hGmFxuFh9-mqk2g1s5KyqbpihblvKZQmUrMr0XrQn7hnS5cL6LVMHUMlDSruzbGn-78yBJFVQcVXXkjyZirUfoHAAG0sFRtYGDbvyH2euqJug_ETLBV45YQr1h-o1rCFA5jFEoszGKIsCrgKn0KWjPtG358exhghAjzFMxF6PMV70n8AZR06Jc5xEtvAW0aRvZYxs0mzFfj5L--PnyE1iCVc0z6qxkeAVS_w9Fz_Kxzrj3K3b3Yo_egoaY-Tw_GSi8d2HS_5B5YKMx5RJUuTO0uTkDOhSuzSnojotBXCpukuOMVDJJx8GBLpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4tKKeOXqYRFx98ukzqJ3T3nuw85tqRw89h4ajWRkbh0d3OKyViMNZzsryz9CqboJ3SnACCGo4N7QmaTWPBVdGIUs7KVcl56rRvIlPx3io7v-Q00eJHR6FLfwFT9xL50XkIV3WLxEDvx1HI4Okylm_HB6-nbcoPgRGNOBjypcVAYPdYe-pem28SyOseEC-RDi9_Od1DsY9LtsMu1FIvEDAHC0vf7awvtrEf9vi7sYU3fdjBxGuf0-j-sPAq1GotVTjTvpb-nyx8fei7lcwTZrml9OTp3ejKE2pLjBDpPNuLwKZ4QHlhnfBmKbVdPOoTNvVoi67rdYT6gX0EMptjIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJWkcawWgxf3ZI3sx0UkKUsPphyuZDvxyGDAKUAufCvrbyOaluq4Lu1yorAMocHN_VfYh0czTbb5fHEy8ls6qFWdTC-eeUce3SyWXvrbonwdFBpaLbRd0cBGlnsgCZ7Xyg4z9SlLqmp4XP5aubPn2sgCK1KnBt9snTnUKyMJFZO_qJE2mMfPpo3jc3apErZI80HFFGGgyD9-U_JEDsls6EyTqt92Xh49PW1XHzThgWvxNf3-Bxs0Pl2UmYxAIk991RRwAlwPeymD_w5GW0bPyc8u32AGzX1c2UnBT4MK9AJBPhg-3QTBkqk7uw26fPf6Ne08rMDBGgqZIWw80gpDeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=nkmO78Xollns5ynsk6RmgnV0PvsPmfeGvOehQ9ggkw81uFCY1GDfgPm9FuHQzW40pxxg7I9SP63MRS1_sN96-xxNeR--lmGo39eZ4C6yKi6lU1jXBZxI4i8edVEfTLCRtsYGJT6HCw2PjvL0SQ-AOdau4TmkfAjtcY45dyJb0SAS2gMKCitAWUpIHX-ou0bzvGCUvkBjoHOyW73HqOPD2IDS8XpYg9Eashxtn0tT9Y0WNTpU1QTsuZkviGxX8mKsCqvD979uMtc8srHSMVruaJyH1gByKSDtw7rV9-Kn6pmbGBkfN8zVkNcUoEGiH75k81bfawXZwDZNtOug0jDLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=nkmO78Xollns5ynsk6RmgnV0PvsPmfeGvOehQ9ggkw81uFCY1GDfgPm9FuHQzW40pxxg7I9SP63MRS1_sN96-xxNeR--lmGo39eZ4C6yKi6lU1jXBZxI4i8edVEfTLCRtsYGJT6HCw2PjvL0SQ-AOdau4TmkfAjtcY45dyJb0SAS2gMKCitAWUpIHX-ou0bzvGCUvkBjoHOyW73HqOPD2IDS8XpYg9Eashxtn0tT9Y0WNTpU1QTsuZkviGxX8mKsCqvD979uMtc8srHSMVruaJyH1gByKSDtw7rV9-Kn6pmbGBkfN8zVkNcUoEGiH75k81bfawXZwDZNtOug0jDLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwzMo49LWH_uelguiCmH7RlBouzRNuVOw47G0cfdL-fd48kr0suYueJkdUH0izzC6swoUUkvvsuqc8iPOVQBNWUvUXwrSS_4gdiGW-N6lZ3LWXnJm4Y5MDXFPj20UHAbQik_oZkPs4C3ZFfQePByphZYosetwnPv18GaBK4W42yGt7FWKPv-5uQJKKB3jOt6_pUvtQJvFQAPCFOA2EUktwFs8DyKM9nbUtaPern9zX3C_zWF3cVnmRllcOrqijDasE4DX4L0aE7Tju6voZzFVkI8xP-Y_4itJ-WQBRZ_z32FPeO-sVEclpGEocCDcG464wZnHkNIvWBVGJMjpbnu_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxyMu_96n4yPHzqe-kDqf3L6oobOjV1PiURuXXS3dRzqaUeluCZcyt95uY3GvpxkN_Vs8DNHYV-lznbvKl5gyyeUEpoWetms0BUkHB_-rGnGFaXCvWJmnElfioZx7O518dg2jLoQhszzPf8lGBi5tqLHNYO38ozHE_ZYJ8DU3DP4iUuWkMxYTtgW_TvbIQ-vQIOCAYdTm24tjXroj3Jmh37tzHG9pNLmlZw0g2qKoMRlUJKcxfWNKs8igEEK7Dzi7DMMHjec4YpjgB0g1OSwQq80yoLDEmuB5wWZaHu01Q1kPdjxQfHhtRQApcNmDzXEg62gA0c2x0TPiRHb6bIrfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwtvAEQgOGL_h7jMKMQzzKAmQfwAYWcS5LFbHA3aRKeeROBZGEI_gZPZ8EpR9K_9bW0kGpTdVY4XkRJPfRoMYD4lMZrpm317BzrOvDMoxOgs6wIkg1q8ZOyjNhQ7Uo0k37NEAg9bctw0aPfbvW4fg37tPaGlz5sJmWm-yKdZdLpZvcPwronWPu7VpJx4IOix4yQvM9cJ7cnr6clU5JHelbcDwtrxZzR4rrCVDFqSFEI7GYoNeUwezgEYFKW5IGBZIgxDpNlYEXMSLvWOmdI41guk9ng0boIBFhyxSzFJ4s7fwgfTv7HWSdQkPLmbNS2qTwlElE0JjIrNZ1NBiUPeHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXsG6rGoLXvQDafyeShwfMup7Ue1LWI67ZvDmnvUbZvVEjffPJT-BKBZYiJLlovXSjvF7uKyvyJWaXu5vJKlglzG1aEb4BjN2ZgPnTf0D0jzwmcCOvP43NFbWK1WZFdiUUQjReMYyNGxSkOU0Sh2vC3Xiirpx_Lnye489-nVpFbiF1NCOVfqT6YsQOCKQGmaZaSKE1f24XwnERTh8Sovv3jKNGohBxkh5CtdIAGm3B1nQr1b46VcawwVcHDMB1TvA7rtEu2zzEVDDJSSyTXZuVwuwGpfcqts4jU_4gCF54oaKG1LT6waD_G4fgplm0ZRkPTFhZGfvPbJJxbsLqu1-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=vtyMmKe8dGryaSTjMLIbtAkBvRtKNWFn6GfAHS__AOtxl-YPlkRX01NrwPAekkBJkFmUmHQbp_QaawMOzQfIFinWLkh-ynUw93koVIqa_WgVMGhVXsku-5Rlsx5YELnMA7NtGOGAFRXDYPaEl8-MCsfRE6aWAY_daEJHj-da2On4I_QNsf41g1fUmgUd2aEZIgoDAdEa-Qd4up7k4tLEoPph78UTpk5iDwTB7xjo8parg2oSVKLUMeI2WP1izz-m0Maqsx9oKLj1gOTSfQeZ2HFxHxq4Hzwv8DxxVDlpHU89f8-kF7HrTVoHmuOKBc0ripoa_6Q57H2Enm9DkHvo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=vtyMmKe8dGryaSTjMLIbtAkBvRtKNWFn6GfAHS__AOtxl-YPlkRX01NrwPAekkBJkFmUmHQbp_QaawMOzQfIFinWLkh-ynUw93koVIqa_WgVMGhVXsku-5Rlsx5YELnMA7NtGOGAFRXDYPaEl8-MCsfRE6aWAY_daEJHj-da2On4I_QNsf41g1fUmgUd2aEZIgoDAdEa-Qd4up7k4tLEoPph78UTpk5iDwTB7xjo8parg2oSVKLUMeI2WP1izz-m0Maqsx9oKLj1gOTSfQeZ2HFxHxq4Hzwv8DxxVDlpHU89f8-kF7HrTVoHmuOKBc0ripoa_6Q57H2Enm9DkHvo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQHa8BPz9axF1kGB7NEQWFOljZr41b-HCHUHSheo_UJxPcv1Bh9eQJp1FehgrMD1HgpUSAO0sZId0E1xWz1Lb57NsD7mHPPGv4xM_7xPLPbaP7FGXaFJGIlWxKrDhQ-CLyvdvm0k4t6qDSx9bWbMo-wkLJb4PhUXlupgZzbHPQMoTTe4beKlvhr9rVv1FKf1hwUSunYajVemHZFdfpKK9ExM62t2LmXQHtU0_Y9hJyGZOL4nDIHd46f0SsjklcWxL9c0DAw3QnBKnubbJtXS4qnTbyAtUyp_wVEcFPdKAsabdb5bvwmWGr08d8a0jBUkzWHP9CvmaSwm8S90iQKVcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTn5sHEQdgvlZWHbXScsQp7ZOf6WcBjnVwKs3X6JNRjRCyGQEyou_tHpFYcGI9JRSONtedKigYhs84J5UoQN_T0Qpw7ODzz_3JdAZE9_f7KgXrrJmKLZWDgq5tcVtF5V-BjRaYBABjIbz8xvnEAv2PYC0Iwrs2rkPEvQGhvoKF8NraGHeAsfLRG6JuAm8A4uVlpzsYH23M2DF3T6ahN6ytlJ9YfroAIcNwWugmY1TUrSo37ohTVczqyHOGuf78Uibaf1FSJAhAAHfaRJSv-AKnH2GF3FebTyqXOivkmPk_NLD2yR15xRKc4r52ir-sAv0z4TV4z9MJvjWJzpeyiMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_POwYt4wOJdtgyohAkVPkvWtXGz4D3je1V3Mig57H0yR9yiGQR4IqOg3pV_ujYfZPkNs1KYU43b5ehGBdaxfJ4lL8BCt-KqQqPoGCwmSp-DuHkUO516XScJnTS6lqREgCDJPVMJTjOySuq-w5itrcOR5fdAIdu8ko8lVwITHFCVdKOgbl9JXXHZgu6Sqqm2PAvREWJ8Kyk4FXSzvLKZFpqqyzROqpnt4raUfAauAX6lQ5iUG7LDoVm-av3w6Q6UuJ_f_IzrkD82bnkRakymm2zmpsOPWdbaTetBzUfW47pj2YeNg9NV0-LdQ2E9ZbFXcQhruhhlPL2rga-Cz7vKmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBelAuwNFDS-kbAJtJY6zTcYRrYn9WgWUrvuFDAIjzVdizgRXFujiBkPQM3ZJhRvSuyMG4fN9sn3zZQQ0PfgPx5AQKEPt_5_PY1zzfTgZLdbSV0864J2p_YrnItpEIFLErDRicHQ5n-n0Qy-JOvziMOBju6iYwl6GBQirBAGLqJ1GKnIcRJUrG0APyRH1nODO7CbnWP3yvpCfhFhXQ29wvSf-IQe6Ykn5t-MSOTB3PNI5thMoPXJI2UFpnUsXK_v5JhFmQHlNKhe5hpOr2hTICz-8TXyEL6zYoxlXeTbXb8gy0O3EOrRm_q2f06RxY1NVyCHwjwlcWQg6U4i8ee_Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpqW5Alc8vYRLYzik7MB9jfSrULiQRlEEUqHd5T0X7VKhaGKwcGUtSCRUJZDV4qLDBKDXeiQAVUTKhmE5Jn-F3OWX_8jDDTKPqclN0ZkuQ5xS2uH669Wb4oHSBIYjv0FCnjPJE3IU58RTBuhbIumhx3klKGRke1Z0umx1MZqHVuhDYcv8MgYtC35jXjSe6YQErOsIFfK1cMWdh0fxCJ_PqgTiGcRMm1Q8noFeCMWVplmOB8efRpf9bOwVRBzk3zcK9elr7MhR-d7W2AxtsAQiVpAgBioaiUP8R0M5K1wnm1LLgdalS7Ncx2WKjF9yUvo7Ovizai5w6MoZNnuDQLosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdqQ6dE4uTO0SugkK316vEcw4WT4GOZtsaA4SHJ0CvPdndu00eR0kU-bU8uL9h1ReJE96Y3mspU4C0r_ylKWLM01DRvPgK3tN29x5O6jO_7e2AWje0cPjAoLM3jNHusHo8CzOwvXRf-EZ0A9qxGInz-h4Zqi0jPZcSpfXGJrKow8PO38eeLpfOp2pnoShk0pVVavX2_nlBblMZE94UrQT-Czafd-e880rOr8eEZu7SwMt3BzNA2nOK78QiAU0YB6v6zKxDqJ-nfQ3joQv8dMUekFwxP7LZ35JKDYwoGE0MCLblgAF7BZ98U4cVET9hdk_N15rsiNJ2t0SzwWL70FwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=tz2L161JsCRup5ymo6cTEUKIYmVUbXyLdcR4s9rKg8DcIU4tPTeoQ-v_QRoAh2-soKZ9acaFcbxF8OlbKERmN9HcIJOtK1SnzO4RmxK6M2iOmsjukgORa1AixqJRou3l85lxQvNxuHGfqjo8A2UQDckZSmN5OiyXzPFIUZ9RZoeT7WjzcefRUnQrTl5ctT5fGG_xhRCg3UTGg4UmHX59yYiwnG9aAWpdeVi_wLe1rA2yRwUf6h3K_ZqsDDuKeRpjLUuzvnuG0qgP09s_-rH1OELmiNXeGbBPM16wnpEhIn32xdV5IOK2QaRGqqRkjXMrdJ4pmagqU2CQTxbgXeOuGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=tz2L161JsCRup5ymo6cTEUKIYmVUbXyLdcR4s9rKg8DcIU4tPTeoQ-v_QRoAh2-soKZ9acaFcbxF8OlbKERmN9HcIJOtK1SnzO4RmxK6M2iOmsjukgORa1AixqJRou3l85lxQvNxuHGfqjo8A2UQDckZSmN5OiyXzPFIUZ9RZoeT7WjzcefRUnQrTl5ctT5fGG_xhRCg3UTGg4UmHX59yYiwnG9aAWpdeVi_wLe1rA2yRwUf6h3K_ZqsDDuKeRpjLUuzvnuG0qgP09s_-rH1OELmiNXeGbBPM16wnpEhIn32xdV5IOK2QaRGqqRkjXMrdJ4pmagqU2CQTxbgXeOuGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtNWGFXrJcdR5H9_CtH7M0ZWPUZPqluzdkCGyK2nBVFv05hlnLSkFb570tabTuJprBFewI6FB9wFh4OzV5cboHUF3Fw1s_Z04KOnUwt1w1VJQIb_mELYr3LKpBY_q4K9avlouyTx5paMQqmetfbBMJB7w6Ib8-Zzlvp5molC3mcqYKdj33AXPqSi812m3miSlSInbd4OFJ-ftRvkGKyCp1MPuyYWIe9cBBuB44bL-bGRnLBGXy5aYjR59ZSWFIiJ0DEd8jMO5d0dkVxjce2Fke2EPfFWHig8LVszYBmyzk_RRdh7WtB_70eiHVK3Oq-Bsfx1kwzRcpOPZvNxdMFqpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ0OEf9bH0GLG72VPxB13Bf8Gy_UwgF9GfWOe8p-nE0zayDzEtP6Rqw8MnWI23Jx6eILQMeDE1QtX0MUbNQAqKLjtRz2Byqg4ji_VSsmm3v1_Ztpb_DTBj7JitB3uOJbsbXHaWThyshwfKKaM2GHfDU5a55BUuEvdggAkwAF21W4g2oh6EWESOLz20ezqHtTrB-2p4d-vAtyHX9QfKCteg2ErZV21BVLe5aza4lEVSIfDmb5qF0156F-hhz9PPivpRAOjlBGVOnYxG_ddbCJ8Ux645_R7FOPvSIyzQYoXppO8nZRlsCHmuqIcnIZtsQFq7QqMMP8YuFiOKMLB8pFPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJFDiU1iMBRCGj5n_3LiTNVlRaEYVvz6DZ083P2uk_2DN5o2IUlGeKnF7pEcVW2qkE35zfvfwCHfCZXAFozKNqiC-M5pXiBbjMP3sAIbR3XZsc_TKM5-xciaXsxI9L_HlkLAE8txj4VFTsulMjNPLd4aAjqwEibBJsQQ_Xeu8PrhmfCZJqchVT4oHojEKzKQ51soId-yAjEFNeqsiVMDUlmdSaHBgWtSsf2h5xSWkX9M00xSqZoooStkPJtsUjKcmnhit89Qh9xa3J4avxW4Zqp1K4Vsh9u59MbKAT5MO4bRAoBTT5v-c2CD84D1SCunvvg7DAzp1ALS04LgkJ9bvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvurAAmLaiIQr3PNaGuV4GTZ1lTieOGD3rAeEwX5t7vd5quZJwfUzDFODvg0dignkxbUz44ZE4yuCgoof-aNwwspnju-k2Q3OICXIcz3ZdqxuDtGvXCd51IiBf870nySg4n4QxpvVTcvUgtL_2dZw5X94UA4kT2PUJcvUofXBlds_fH8jrf75p7X3Yh8WIpwczuWCdV-cSNK3ktmLN5W5VRrfPhciocg4NA3KRJQClHMbzUwVNjAu1V0wOHWOEs_OJozDLyJl9x1HFTHAIJzjlkU0TUqbjDBx4aSxOrkSGaWrA0Y_AHGLw-fU5kVY1lgLBMmeSFymZmNvrJuA3p2nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=t1V5HAhz_cQMpPrKx8BXJKtb0FBy8dTCHuu2z58kywjzKUdpHd_ZO8PDtb-lb1aNLxQ-LBQFy9z3HMvBa1w7AM0uEbTY0UH3ocMm3QEYJSQJZFZQcen6v2EStJoKgqQYv_AlA02JIYAB4Idkp6dDovNC7r_bvANjhUoTxZoBRPJrfkYJrckB3qztY_97AKGhTKJ84u5Xw2JuqxUSRwtyx8xRoikH-XTQ4ZTxBXd_gYtUGs6OBTK5UgEvVhknIM7VKXDOoVWJM_MnH3f7oRoZRpDhDo1fEc9MbXemrSvCJybeV6D2arwbwJwplMg9ODLDFIm22qH_N0rfMTUCAS6Bgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=t1V5HAhz_cQMpPrKx8BXJKtb0FBy8dTCHuu2z58kywjzKUdpHd_ZO8PDtb-lb1aNLxQ-LBQFy9z3HMvBa1w7AM0uEbTY0UH3ocMm3QEYJSQJZFZQcen6v2EStJoKgqQYv_AlA02JIYAB4Idkp6dDovNC7r_bvANjhUoTxZoBRPJrfkYJrckB3qztY_97AKGhTKJ84u5Xw2JuqxUSRwtyx8xRoikH-XTQ4ZTxBXd_gYtUGs6OBTK5UgEvVhknIM7VKXDOoVWJM_MnH3f7oRoZRpDhDo1fEc9MbXemrSvCJybeV6D2arwbwJwplMg9ODLDFIm22qH_N0rfMTUCAS6Bgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVdUVB37eyAkaypff9DsiOLlhV4QUqpKKE_BsudjC-PAzBMZ-m1cX6Dk0kwcCtuzkgvMmy8pyNCgTuUDlhvC4RD0gfjBwiUZfe8zAf9s8DAQKhn4Co8yQ44Y1MgD-Ea7gPxkMWMxLiUbcpuF9onYV2DMO3V2IWmpWMtZQEJIhanrAfCFRnzwxiGWO2TXo_v5ASHdeDXW8YzsZ8aFoQ6LpKT1KNFWyBMEiBWMGi5P1zZin992VrTCfN5NBQFyzaTmvmJIcJP5OkMTCMg20uVJNtmBpS9MjE-LwtnoemX2AEBtdbR5zxdnkdHZT9LbzLYxl_Ydxkg5U7bVQoaMtiOuGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2rEGOxMY8-Zu3jJQpdIE2dYHUSQJsd7_VnQWxn5p6FZWGUj0mxsf7vYGDh4qrsG5oMW-veLuG5jVfHaJcK4-Dd5RYaM4oeAL56IYaHcxwZXt_Sjnb8B6PZyK-XXUmaxrgkyy0jrSJMZ0oKcHkn9BAfFntH9HxOmtJQlUno5x2qbbcJMkwlfwZZN5_BoX5Y1-_t9JVyyl8ciO_j91vxeFkL_KWP7687Uqm5AYwjw4xT7aK_ACnqC7D-FLRBJtYh-1c8F_pognv4S6mqW07uyJGoafxzkQfxvEr0r3gfnX0SV-rNrFfwj7VuuIKPLC9SXZlQbhVBZqKpPCkYObvLeDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQzCCxA6irJYm2GZEAE-NXvdBrhNYjQ4A6SBuLgDJHWgSgGDEGXxlSFv2ZscG8gtTSVIwuB0hk_wT2DKxzIGzLHXTI2PThV7BSZO8H_AlqMfYLaZReqv9jjwkm5_ysGESIUyH36Hwztps3kHAL29bW32fGQtJwRRkewIH7VanEkLsAASVKfYrZBLKz4c8jSUm8Yd19uDlmqdkLK-DtnoxWkg_-Jbc9jYz8QNk8Hx-a37fP9LpB6yiyoeKC9k2ediU5zD3YcMARIHBoMteihjN0cOhDjTXL0CmaLCyrLFwNstNHMMJI49Mr393g-l-0ZQW-cMk0fRMApClosC1tykew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGb2w3DFUvh76oERlqudNr36xxFnTShWfKMedzq2Fk-p0v8Hh7eM2LhhFuVi5YZEkGlYEzzbq9ZxN6tnmxjo2BYuHF7NisiErbY1LA9rj6zXKFfYj8qHL4CMlRfJevSOHFwrkfmkceFwdVT65P1RVyBh3WATi4stukItnERmzDBXDYYOjBg5JwrmLYDIG82_GBng0OxeIaeNhy2IJaqsMtyUOobcctSkz7nGUHATIBwjZpcDnLtMjmCIMox8AxBUqVNoLxAnR7-2AgVKNiFwN3y09jfq1vQXLBFerDZk2vskhjCOdaZ_WHz3RvvWjV6-gqhVcLV60EyZbZPFwDBWWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=Z1ou1C_PfeXNN3sE__mAnyHnzXlTFq6cAaVwMBj0zYg3nHtxzpAgaYt33_oETeZaF8JkFpGqqNHY7CDYDDOn1MRqEGz9PlkPtbnsNwMJbBwBo0bCJODNPefROcEwOIzrhfeGK8UfLyp79AEWm4kYvvjP5Mh6J2ZrqY1OoaxBA3bRZN1Ohx524MxpLp-SKmu72z819XHj01X9ZuQ4y1LILvPLy2GFKH9yWV98Cwa89Rap-Vp9bAqEQaIWj4SbqMtWKWfUrrT37W0bSuCpO2ZBvd-dm60-LwkQMwDf3qeRQPwIDzazUXqBdEASlX5qklcUdAcrJ2EfCKIY9WTvMSgwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=Z1ou1C_PfeXNN3sE__mAnyHnzXlTFq6cAaVwMBj0zYg3nHtxzpAgaYt33_oETeZaF8JkFpGqqNHY7CDYDDOn1MRqEGz9PlkPtbnsNwMJbBwBo0bCJODNPefROcEwOIzrhfeGK8UfLyp79AEWm4kYvvjP5Mh6J2ZrqY1OoaxBA3bRZN1Ohx524MxpLp-SKmu72z819XHj01X9ZuQ4y1LILvPLy2GFKH9yWV98Cwa89Rap-Vp9bAqEQaIWj4SbqMtWKWfUrrT37W0bSuCpO2ZBvd-dm60-LwkQMwDf3qeRQPwIDzazUXqBdEASlX5qklcUdAcrJ2EfCKIY9WTvMSgwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
