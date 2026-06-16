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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 952 · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzIEF5uxmVT6w6jmnnusFbQ3oxDWoU13ypadYGBZe3iioKppjOtqOIGaYrcjemHoYVX0gHaGe2xitKTC0qUbGOPiNnALfG0tM-l07JiboyxTA0WmouNZlr292plyAD7trJRvhcdnC7IanmepzOeHDbmCvyVBrdbHcu48DWBaytmpmWPEPt7wRtxA2jT4u_hJwhCpiDuDR1kcR26HNs3oQ3GC6N8fxxL_Bh7c6MVNVBdrK9wnIW31MPCAWBPpNax9IsakPJVprJGBjH_dwUPohsemJXegps7JWzSGA_U3HE-87Kc_E6m-SwpPrYSi52P8_st5oNMvJjfAtwZ0GidRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEN73MCNmvPRVl-ygIzmj6IV3YcxDEbNEZbmiwbO8KuLEQn50Hp5Wq7XGw4EET7OME6IYLrCHj81BTRH9oKvBawGfLSsa38az91MczFUWjrlZBfk1TPk3mNEIBLsDfWsQC9HJIeLe8CS0FIx-jYwpighfLGFfpN9ig-ne8GJN2ROfgue_VuqtZlSfSz3VEzFHiPM6LlWNnrkEczyQT7yvmmJS0HF9ioA_Ntx8HZF-94Ya9RGIhfd8Np24_4yzgU542901W9NexS1-JvPMQlG8gKoU8KCahyMQKUuFC89gQSKQI7I1gw_BwGtANL4Pw-lsdHQausLKFotitxcnom6PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1rqylehkP803MsdbmYawgrJ049nIN2575T8UD23K2a9qNXnW-VXeiPr0kuTakWXXrpZfAngsdf4dKiUaDUNZkTP6jJob7riVnZ8csPs60gYT14tx9v4P2TSAHK7HbvgcQvRC9k99nYVQA3HDQRFSCEmouyYVSI1m4a1DWXT4uWWRfDfpaEQZ7viu90RAhoLduXGMP3drLE526wPWe7icE7BYW5J0nfsmZ8DKOUE9bNpVJRvi08R9cjbWWH11wk-EHF38Hp52xualIPDf_llmpJohPU0ZWNc3ncms5ItHc_a8FRDu3l18cLAPt8_3Z5WnHgoGsSGB-5oqTESZC6i_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5MyFijy-7RU40LosI9y6iwe9KdctUIPAorYyRYg_cHTdGBdOUlUKpTW9-iBbg2aqc3_LoFglS-JAWS-RCja6C9y3-ZueuLSyMXZp6W5JQP4Arq4j7wuaGJOHhwiYMkIrp4zThypZT6ZzjaAT4dktTWLohyOyAceg7lkPZbMK33KtHNIZSiA_na4Ysobtc9iXODZ6uudGofCqjDYoG4ytBtfBoun4C7UriwPs4QHjt1rVqXL00E31qs2hmpR2aUZzIVd7wW_IE_cx55h2yU52ZfDsuQuVtDWn2yks3cSU8quUkeFkYZ6HK8CDwDwJTSgafgq31J6YH_X5OeYp8ZiPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2kU4PIXvz-1r2J1CeHag1rTAS_XQaFAqPA1IKDGLUcxCXr1-eAs3S4Xj76NiZ5QgWQA_YiTcDL7LQQfzIL54m34Gu9fxOKexpRsnnXIrG1LSPtsB_iiBTNo7lH6xZJkHZLcv1EDltgjIPRSCQBiCwumNyTAKnI6MShvSTJHYI64Cgz7AdggGVPPJ7LhwYf0LFvi4E74w5HGbS51d3-2v-d0Bz1sIoEkzWWRFtLGaf1bIjzZvz3Jy7JFV3fmIqvTigIpyHAvXvCBJmZOFGpgzT4WfGbtaAoddi0SBdAeu8syuH3sJqzTFB6xmd5IZ-6l8JVZ5laxS7G5_mC4t-0PVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG0hl9lec5sDpx5xtFdM86u6suKUbF--eAtFpalVdke1Our5xttOWnKie_SZPzLKzTIzCjUzH0fQFD-J3WwknBuRo0Yqf6Igq1fPbd_YnkQXV9_03rJJtYBoOvJCXyQJMCPpjktJyXDHIbqvIBi_dm_9X9hHx3kQi-WMSzDnhmXjlluoiHVIPOyVezx-b5OU6-ditg6T0EFDCHU4dywGUT4J2oS64sXYsOx9Oki3BAd8pZ1alLaY6GQ-muzVo1mRZiQXD-Uu4ZC72r5q0d7D8MCea6RQx9pRRru8LFKkny_JkJn8RZOmBIA5G_dNE_EsdZlE7eSsY-hq8SDmtkiWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kON8rvkI53WsLUDbYh85AvNTlUKE1O1lsV8GNHvjwy6CSEA266pBFdvu7fwXe_PJcYt0K4v_ccE1qufwLlyIEzDSgOra8Ux36tDtTcPw6yJkDd2EOSAkrfKTQzEtO1MDDUISPc3uWY1jj4jlaNF3wfhOXYtvoC-W4RC8lFUL3ttS3PmApW954iRtJSxbTRsAMmEF9i0qCJ8bwlhH34t8HeATA2eBHwY4UXJurpw3Kfn1LuenDo0YKJ0c_XNdePv6YmGK7Va7B8tWncjoyETjolIEgjQvT8nTRME5A876CJQLJo4kvEvU5vky0yooUK4DHl30WBk6ELVbka3vJoaUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0nn68Vn4_VvFopyskL8KuwzcZGNbCQ9kJpX2UidQIzpdaKiIHhFBDYDskaR6R8HeOOHdUQaNW_aiP1As8UbVbjk8UaHqZJShnRhPkeXdS11U_yfHJdpg0TpfiuDuHZ7H1cDDA8fSiTqHsbkCdU0hsvITSVFq35j3yWTGWlqWPOr9tmsVbL0fH-fLG4wPR4EEoCDZQNJua0nQB2B9w1zBCTfzjkT5CuQD00991VkRmIm1KrPXJyIOk6dKKvx854sBranDzzquKURpD8DzROEkOu_FARvAjDU8gBQqNWm-QgKwgfcdiL-q-UdEj26OB4IOKBY0moWrUOTYe86Vs2w1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL5a_Wt1Mek-8eGAHqoJkfQ5kJe_BMhbdgd42ByHPZ4QzLbGw5giRAGutnIOw9QDZExPam5E6LTA5OAm54WA7WAMuY8YHtFyZe-hUo2RIyxeeFQtD1a4hFFueJP1YfLj6KLUNwjO68dQvmdd5aHfYVyO54ci5ohOtyTTSfqf3Jx85rnkava2rKnZBtbE15iw_WC0vtpa8ypyi0husfEbFdXGqvSDRMPz54aCXJsCSygsdKVrNsPrP47yvEzgJ9eoyPNjNhOL_gvHN_AJNBzY6JtGKUEKjzWj4BHshXIR3my8uOyO2OjOI9uOnblwTZI1-Si6GsSVTKF56nrE469yWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAFYuEbCI6TYQBBImf2l8tZWHo2Kwn3n74fu_t1Ha5vxKt2KSYAPeI8ubFTIFMCu3Tfb9gAGJPqUB7nFYfG4rIspUWHt6IIwGrSvyKyKcEFaczyDqtqeu06UiCZeNYxdgjwtRseqLf9qjd_JK8_ZozpMObi-H-3_uPfPgYQPDjWOdktrNjnQG01NNwHml0_T-OwUK_1EndP64NGRQtUTPL_yKPD4mhZuIjZn-hGpVzoKBiQISaFvkjxlBzIa-Lo10Y6wefnyDZ8-CoubWwLrArINCyfh3K5tBscVsMadxIlLGJurHwVjDaNMjvSkRz-AEpC50hUKqtXs9Aza_vp1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGjMrmIx0q3FkCxqqeDBTPcWhYXu1VaeRCVbcAguyXJdnioP8_v8HvhBQj5Epuc9SAcfYYxiNZZcdlq-H7UnGm7FQoXaWmgReNsqrRonM0EsHExAHh0qiZ3J_gteILj4EUur11a_En89ricGCjBVp3_wnNMzODtNE--PTxA8S1BIdvcJmLv-J3trxYHM2h8P9Tm4C-LRj6GHgYhSG47JDePYqsZcm2UAc8I8HKmmzynq5prwNcn4PNlBZLIz-JHQPyD7Q5mmMSSg3v2ymP7O5z2IExJh5DbIiqK53YJhmH6Nu5_IOpBpQ15xEjv-abSDZrJ9salbjpKO8sxvNWIJwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1z94mNxCoVZM9TFh8MfBsoHcTl5aM88ds8hv_W5gz7178xXoxW3ovAWX-B3niMG8rEhGR454kL1LPD2HKdeoduC6xRQDeJHCnEUvYtXDD02Qr5kH1FFHTCvYyaBjhTuL3h6QfYokYgqNIhS0Y3GAL5sJqQ5DAEeCvRGRYq_8G-GmUfgj01JijsmoGI1jOL0gjOEUKPaB1McHNsYdsXV4sj3Luxu-WUNNPFALs--Tu0dQZWJ4WpSB-PULlI90s7OVYG9rVm1BkbHfWqi1PI1uOYh3Ij9e2CDhzVlFzSOYa3BQ18pca-Vl5UbB0goGvxA6RBmIFsnaRC2Vzgl-SZ9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=RZErMEFBmOFcvIxGTwzXnnIPTsAtpavTZ4UiiVu1Eq5gygWFC5fXqP3m5QFXCqx3ruzmNd_OTeTRJHOPXgoIqtWY8S5W8xvthZ5ZDRJQ8a02YiACPF96ZYclq6JskMKxZJmwwGkg8m4x0xoKqHwQY7CndEreTA9Fy0IQNns_1xesGIpHPW0FAM7Ix5w1iTu9F_rCdml6hF9DGWPUNHK7zIydV91XMROVjOqOzqqUK2949tvtRVS2mh1ptmHxmrp1WcVTf4qG_9ZeMKH7sUgl7HIwYaSWMPLPCHpr_bXSa5UmuH8TXkkzr5A7lqD6YKihUgjh7xPj9nnz35gB7RLVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=RZErMEFBmOFcvIxGTwzXnnIPTsAtpavTZ4UiiVu1Eq5gygWFC5fXqP3m5QFXCqx3ruzmNd_OTeTRJHOPXgoIqtWY8S5W8xvthZ5ZDRJQ8a02YiACPF96ZYclq6JskMKxZJmwwGkg8m4x0xoKqHwQY7CndEreTA9Fy0IQNns_1xesGIpHPW0FAM7Ix5w1iTu9F_rCdml6hF9DGWPUNHK7zIydV91XMROVjOqOzqqUK2949tvtRVS2mh1ptmHxmrp1WcVTf4qG_9ZeMKH7sUgl7HIwYaSWMPLPCHpr_bXSa5UmuH8TXkkzr5A7lqD6YKihUgjh7xPj9nnz35gB7RLVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKcl4QY4O7gTxsCFrUmg1X7FuSYq2jeulee36NMoOTEnYQmlgOJVDUeaxTbXfhynd-XAa_6R4gzALjXoQGVGSOx-4ynLBcsvqpzKIDBqTaZSt2V0j9abD_WOQ2BcZHHUytBoAon451ZFCI-Q85dqaikwOZEDh5tfQ46rUztQud0WEqnAQdEn9_IX6r0iks9Aku0xoSiawixzxVu8aqAtCRYDpZeYEtEVdhWTSAkUXlAMz0Nb7aEs39l3PwFO_DRAJVHDhhbmVE3p_6f6YTsKwZf05Y0P3Lu8KljtqimvlcQBNNKLqXnh_kvKDzF_HqpVFWC7mxnwcaSYA0F3ItIWlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1M_eXDrAn9cwFOi8m4zg7wHMrGMK7JsuHdLJiIEb2W2PfmjmZAaI0qOCdYtsiitbUW6J_K48Zz7JXUddA2KCj8rgb0aSAnPDkPtcL2lYgbtggLrov3F958Tpb3GvNs7fBfUIEdXjZUA3xtBpnDLQaVBCpsrMDEoTd7NX-ozaUa-jLCLvRw9Uzvf5QrY9j-m5QjySqi73wi7yuiEwgRpaDJmOdwkSCfB5NWDN7wzBlN7vilTdfoEUVF63frzVuhq62HfvQnhh2djxvPqCK0az9kyAUmiE4YnSkyD-ymXm7Muww6VQzm3V9E3Hq1E2h611-wKADlaN0d3Fwo5jFZq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=rPfOI4UwB9QW_HlNBNjlmzKPk4VNJRlvRpvdsllDT8d7RaOeZKh02DzvixlykjqIMCxCDUjUf_XmOk2ZrVJHgdMrNf2TE3UbOY1ECIZ4-0FHCAZ4rQ0KtRpf-l9mZx-JNoOzoz-zhQKax8XtT_0HGrRTW-uSY2eCWQx-jft8PuKg_K93G0Dogxpw4My8JWr_M-qvvSoD2rROF_a4CJehhsLuRiawtvz72z1o9ASr7o6-Zx8Qz1To2Bges-_KRM6jTLBF3-TjUm6-Nl2tHAbL0nW-pqj-ZkVCz5qA4TVT23qu61euxgKNHWm3nOSUV8dMYyfCu6jlvaQv2n36ihrSrW_0cGeOdF2pvOfDdp80ChLShEdU270IZsIUZFyKs-xY1V3nApaIdAvHQWSZtenyjbFMx5odiPyeGSt0KS-SU4G5ZMAbJQRYmHKutZpQvj9IqfwKxOXTfXnsOz8JgrFN2HdZ9s1HXRn96t5TundcD61EivMciUN67zxGYRhweNfjNkQ7WLHhLVjdMky6mrvT78b8mpBA7GAEbecsySESkXBqYxGJOAJNrU4uIjY-FkUjbjT2HrmKiOzLuB_WXbFt91-W1LKcLeepB2G2fYqVXPX-F1GLi2eHvkmLuqOo30jRFTR_OyvQOJdsDu1XM8JaPhac6PSBRaSBC8__G72Fyfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=rPfOI4UwB9QW_HlNBNjlmzKPk4VNJRlvRpvdsllDT8d7RaOeZKh02DzvixlykjqIMCxCDUjUf_XmOk2ZrVJHgdMrNf2TE3UbOY1ECIZ4-0FHCAZ4rQ0KtRpf-l9mZx-JNoOzoz-zhQKax8XtT_0HGrRTW-uSY2eCWQx-jft8PuKg_K93G0Dogxpw4My8JWr_M-qvvSoD2rROF_a4CJehhsLuRiawtvz72z1o9ASr7o6-Zx8Qz1To2Bges-_KRM6jTLBF3-TjUm6-Nl2tHAbL0nW-pqj-ZkVCz5qA4TVT23qu61euxgKNHWm3nOSUV8dMYyfCu6jlvaQv2n36ihrSrW_0cGeOdF2pvOfDdp80ChLShEdU270IZsIUZFyKs-xY1V3nApaIdAvHQWSZtenyjbFMx5odiPyeGSt0KS-SU4G5ZMAbJQRYmHKutZpQvj9IqfwKxOXTfXnsOz8JgrFN2HdZ9s1HXRn96t5TundcD61EivMciUN67zxGYRhweNfjNkQ7WLHhLVjdMky6mrvT78b8mpBA7GAEbecsySESkXBqYxGJOAJNrU4uIjY-FkUjbjT2HrmKiOzLuB_WXbFt91-W1LKcLeepB2G2fYqVXPX-F1GLi2eHvkmLuqOo30jRFTR_OyvQOJdsDu1XM8JaPhac6PSBRaSBC8__G72Fyfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=VkbeNLTXU4kVUfHx7VPtHYKUkd0xCWZskAB4273dms0mNCKZq5uKOp-RyOjBgFF1m_Q1QRmm4Ik6_1ni3K576RF4_i14PvLYP_oHaTvW9z26gO8EE8ddksgqv-_VowD0n0wNRj4RNzQnSF-sJep-Ma3ViK_c93ksGS0GhWE9UthPRolhxueIz2MwXq6xeWzCD7AspMibqkaDLegU59-h4UU6VW3wqpJjy3P7lJI7343fKxnXMR327FWGJOZg2UIV4k65YzFKZ3zfphT5bJA-IEVh1-g4YlMMjgMJpFThWtB1vEg3Ekfby_lRUkGBazKYR6bhRt4Kv3RifBPfpjSW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=VkbeNLTXU4kVUfHx7VPtHYKUkd0xCWZskAB4273dms0mNCKZq5uKOp-RyOjBgFF1m_Q1QRmm4Ik6_1ni3K576RF4_i14PvLYP_oHaTvW9z26gO8EE8ddksgqv-_VowD0n0wNRj4RNzQnSF-sJep-Ma3ViK_c93ksGS0GhWE9UthPRolhxueIz2MwXq6xeWzCD7AspMibqkaDLegU59-h4UU6VW3wqpJjy3P7lJI7343fKxnXMR327FWGJOZg2UIV4k65YzFKZ3zfphT5bJA-IEVh1-g4YlMMjgMJpFThWtB1vEg3Ekfby_lRUkGBazKYR6bhRt4Kv3RifBPfpjSW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqzDlGqytdJHNbcuPxO3tlYWx9EOZsW4VNi54XPQ8Ro5IPREOn57IZVuVZrt0Qj_e7wsd_RMK7ZqeK2Bd_yMQdH6M6JGKTy5m4E7EnJkpqvW7gWR4ffDBC4lJLIF1Fo_LHJTVr7Q1FVprC4k0h8ccLG5Ble1mZ0N0wnRv8LwWsUcCC0f0s2oP2Ae8mlBoLK1IDYYK3P0BuogQUQ6clIKp5yn8LTZdXJGzP_wOe9a9D-3aUIFHOojF-WXGg08DW_i_3MpDy3V1onUDXytbWB_W6Zut2M2G9NvBLUGyotGBfjRzXv_s1WEeV4MOY691M-Ny2oGE83QiotgoOiifF5Nxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSHDJ3Lp39LhrFei0MpSIwnmUc02PXOFIyF7m6RFf_0VCzW2KeyGoyA3Ezbj-IJUxD9593I6COKDlo6QvXHk7E_8nx6hCBeyHdGrahqSpoDb_WBg0h0QimdDAhggsC_khH_Y75x4POybomeO27SaAUUdtfzK7qsPZNp0IGhrbvt1lFspbtTxM7BHbDHNZQmfS13pKPUlYUbRNjvuY1-XZVhuBHHyr-UPqVtuxD5t1Y7Gnp738t8ay3-gK13TfvmgKwS20smxBs2pcNycqDxP9knuv6qAJk2K2_vPGzQkHKSZ9jx-IqY6K9xe7bRvHDMX1EnKJcgrMZX5ymrxvs9TJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVAbggkKNChI7UQqgNrLc1QaukLonEuf-xtxGNK2KI66fvZMGfQYRyPzHs4qzsKHFHXc-pUHWSDmxOvFW72n3br-jFWcKB2fMPIrh8GDMK7no-2WYZoXisa6ENnBTB7QJwa6gwEl6DwQ7ct3X2klcrYNQwmOygxniBWgqXcJ3WDLfDDrMaqc7-AFilVem0sNuURvGC3Fy3qisYW01OuDphKV5_16FCVIdJZjNf8TrKXR1cu7_auGpHhSgBomOneZSB74ht1xVVU7ELzhmgKZKJmx22FYBmbJf4H0Q3F1X8f0TEEfUi-pkbw3IH0n7p5fV2cciiYciIG4CxC3sxJ-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2lKHGk8r6RWuE8Buw0aFpzp9c6n3nrqluxaBwjX-Ga1ROXADpWQzefhd3kBRNVWdKV_yn9njf6IPCgepqqxwseLqGD46jqGleeAqgGtd5-UUvYj6UIUIKO0KVihDhdQqQy0veiabPNZ6Wu-fpDJntuyYjvEAquz2QXdzWf3aJy2iLcLFrbPJWV3XMuDXoUscBQbd06TwQn89ktVFL_fKIziErEODWD4S2RqOumlbMKaDzFf0HY9uAS-0zERsqzU0sxnUsfPcESYDoYkj6jYNABhbwMOIPJjalsnGN1Jngtqz3Ucb0ilpsSFQYSUQxzDcsyLVy7ODZapyOLB_2PniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgoXDRf9Dtfno27qXWmxG8blX5MvynrF48uQMCTkuAfz3kPsMJ7rmmc6ExrYjWy0fM8B67QEpEEop6fn1HhbAEvWnw5KpgXKUsoCUHUjnlRV9IQuCBym6gZAA8pvjaaJG5ewVBdpztUhs4hcfXia5wYiRhM81uwbwaQPFlWBHCW_xBRpXy0VtBgt1vWK6YgxDkGzpapxUCdouBVS0_pDTzQ_LqneuqYJByldsw3pgQOxpwOHitC4VTgT_ZwENc5wtDFfbBuu12loy0uA_VAeZkBQJYO0MeI9fBFQxzYHXIaNoRRtMXvXTpfQVrpoN_DOsA8h0z0IQW0D7BCa7_ertA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIrXqElLRaYtl5BIi9JqbQvg1LNgHoF_w0uH_4GDxNatUJ2KiuFlwJ3CmxJkz0HzW6GFrJAZ0MV28zFrRpyFhlcdGUsosO-ijBRAUzhzbF-g_IBNaI7ztWuHrUTeOfYLv9msXi3cDO_ZrmGmOyLTOcW5BDNS6qFSGxHojyGvm0zjCfLdD2LQovCFz9ctMrd3ZUV7vRoNcr6DWnRcHLu6gJcAMY-KUcg_-j8W7j0neuiQKA-1cADkx2dEjoik9bKKWsSuTP4U6TIuXx_DiSCDXnc8SuAPucEIjkjrDY4hWVF1kusUUxPkf0AqN5vbhTCvojWczlCAEBxbI3g3DGssjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-Eb1DXPEoQfOvtsTUdrSLaJsv1uKOesA1GtPBMGALE57mhwz3gRp7yYUprgMzCQaky5xflsNlmL26-R46eJL50BBjOQbpA--M4ghJe-_VQIJ3eI8QCsb9P4KGz6JndenvczIjpx2SqextiEhXXtSaTJuWXaNPp8eIXFk9Mi1bpojycczPf1f9nx0flZc7nP8D3t2KJbj91ppZY6XTf8vhoBXBPE0iyLDURtZZL9OkgrdMKmLsgijxfvi6llYJ6JIeqBQLTAmkWBSZEoeCMUSLDK65EbRcywtjVdNeBU6b3qy_zT_524eFs7Mw3xytsXqr8sHIoul6ZA2ANKxR27bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiC0_IoBCR-3Q4PYJhDz1VrFrsYuJyt9V03FfvFTVvSdyAh1YCtiJF6yW-9vGBGuc646b0PSv-EE6DRf-RPdurTYThsIuC6M9ju1MeFYzMuTkwF6GFK3S6rNV55EeK3LjoV9asYWCEQJEVgbR2Vi3_MGlPCdJ6KPk3z6vIjApshyioY7zD9-EGpn1xWC_p-Oxx_JcApcj_t3wI8KY7VSaZi7cDFpdcq6SCBroXJGkxPPhcpqVatxjeG5KYaCA_A9fg_tdWngi9fWMkLAgu3P8O4zS2Qnioba2LPUloa-QPBlv_65j4kTddwedRduD1P8tDbxjF6j8ncxi48eagYcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJOz2tc5FZB-eo48pDRLlvBNQKrziUoBuvX4QRsTSNe6Rk5T_83iEfxDv4Y5OQCJyFSHvlKsqI2zlOoFzhorP-lTh59ryeP55yZ8EszqFCPGrObzbqIjKgeYZienVxEXxRCT1K2GKf-kfgUnK15GmIwRIdGxG9jFKVcKd-n3z-TTdcoLHCHQWsGyPxiXGVv5ABSaurWwQgTZiLzSdG1vZu9ZWBeir1Nfrugue-yM8M9J7pPLXPPSvh9zskhwFKnCuwY5y2NTWWbC24oK_D1k77EBLg63PSLMn90hhasbVwAuJIWESsXJwingCSvXm2OTqo1ooYDQ-TIkCRDdiEZ1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9OGa5MGvSVFsHL6OAvBBKFXLmgLooBsIW-00DL5UlDW7fnornIE7hV6h43VJZxWcHUpwQ-6puz3eD1L-gd30SFFH27T5pSYsflM8wqoazGT3qYwHJLxlPQuyQK5CxbJyVh2mBCX7STH1bh5yfrjYOSToX7KTQhaP5iNun5LXY1i7BnsJ1lSfWaJOsBo8vB823uTQWPsgN1QlUH6cs1tTLJAFXZvbzKpu7eVLOe8oG9Ozed6Rxx9Ef1b-bFGyW_2_huB_l78kSVzNC6r7IB2XYSgHkT2W0TKnFhc-zzWEm6akoJdi2W4Lo9Sq99jEOjdGvXwdWc6FB4KfLmeEKpI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE5bGq00_ZbYz3wDwtSJJ9utrjAw4T2MIcpNblyIsc7LejFh3ZR2tnfReC3vpe_fDmHQEe6p_kjSlpwUWmmoYfV50NMj9kzGrlmI1CPqShM6I7ImC95AlO7NJfbz8hG6M_KBXyVbA8sn2LCXSaKcVw8ra13xClUt98Razz4G9VlHUwmGkuxJXtG9flpyWrbvkkaulyvU1hmKtXcQz27SGwUyoIm44JpTpW0SEqMAVkfdfYCMVLCVbKcMQhihOxsSbFWkMwjGjK_bNH8P8wnnYZ-zFFXaDnsZRC5bfjAVF4kG7Yor_7-z6wy0iRAgfIDjxJewum3FuEB5iXI-2Ahpiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mebMtpUgP1ZtKx7Sy6jGnyrUWqIcZH3SEPlPgLeDqLeoP87hipTUwQFF4naA-GzMNYH7O70CVu-HZ9JT3YEiQXKsn8hAsCGS6ONCHHwMYr9XHc8vlACXbUKg99gYosAO4aYrskzZrrXrumaW4MwvkpvRqx0HSsuBWhPs2l7tqfMLHC1ftwc723Jn3fUhlPcHYy4qSifarvOmvkKRQVXduUPX_8IPC-5LoFs5ogXrxCGfI_0YhNzTTZ3NoqBmjwwW7VLbdSbae5yW7ryWIPnOuCccnJBFLY73mQxc5I4pBkwaBHDlTG3Doi5vlvtRFwWjmM9Md8h8zQpSEt7ZQ4auGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=nAWpQpFwa6-A9LBNychaDHn9k8koS49dk0IoWS7vWEavQEZBmDP97soGocT4Kc4DccujwIWSpprZeklR8ymMnEJ9a055pPVRr5Yfx-R3W8ZNTlpqzS50vOEVv0Br4DQiKphhKwmRrcFqiguLxtiMNKCNzMP7YzWWgo0imwNEDoOHRoThqq9EOD8tPMzbtzqadGzw1drqcnYYigId-Bw25l4ijdRRkF9LlhKKI74tcF4gDtXJMCTMzkB_cRJ-IfHL8Lxi4S6SYdKjOCpdkG2OuiQATTrwWZP1HLYlq86Utv5NrPao9DExjaAkRXUcfTxCrJkhslEnhwwzLj9-voxUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=nAWpQpFwa6-A9LBNychaDHn9k8koS49dk0IoWS7vWEavQEZBmDP97soGocT4Kc4DccujwIWSpprZeklR8ymMnEJ9a055pPVRr5Yfx-R3W8ZNTlpqzS50vOEVv0Br4DQiKphhKwmRrcFqiguLxtiMNKCNzMP7YzWWgo0imwNEDoOHRoThqq9EOD8tPMzbtzqadGzw1drqcnYYigId-Bw25l4ijdRRkF9LlhKKI74tcF4gDtXJMCTMzkB_cRJ-IfHL8Lxi4S6SYdKjOCpdkG2OuiQATTrwWZP1HLYlq86Utv5NrPao9DExjaAkRXUcfTxCrJkhslEnhwwzLj9-voxUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd5MeBUHS2yTijevtGOTonpNNmz6IArcAa2ZPcRsP36oaDsIjtzE9eL95VqEkQZJCAIHMuhChWNoBGaM4K93yAuxPBeWX5351O6VNteDYZO6OJpyW83FCaIarpY3aXJ19bOKjPK14Zc7I3yjrzlLu3fDQgQVCGW5unCEMRXAxS51g-F3pqmwVFPwytqEnwjNGv7i4LN0HtIsT8y04c3rcMwHqYStfHCYGjaFY0vbag_cNwnyABZRHHFUYHYqMKw6jO4l9WYWQpJm1S6NA-MtP-okLHDE6dIWUHb9ulQxBYY4ZfzrMd5e2xWnBRhMgtesef_Zx5N1ClfEoyrVqkF8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-FmmbFlVIeQzmm07n1XdIVL1AzDemBSaVddIWXr_nkHEoaWH7aLDwQQnGLOldoyx9g6hbZTtl2aQFID37J9_c6u9WX7jtyBsr_rbnBqVS9ZWf6-mKsVi0YnqNH6e3t9CfTGd2fhXZzPwDStLPnNVURFJAfQG8zumX0shStfM1rSvdlK5AiotjXcpHA3ewcvXL4OXiSuqTwr0vfRHetHTIZRbbjtZh2J-3MirXzQD8zbn5ewHYb2c2R5aQ4z82SqcOINMp2wqqtC0cPGng4nqOkpV1ZiXgkIuOtZZ_6dWDKRu2H0CGJt-LXzr9yPs8ceDtWJ3ZDmveOTAmrruVOFqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJbeMG05u1z91y1iGC7OYCmeX2Ta2ut1NYx8gUaUYWG3z4haw4OYZIqAbaj6xkChy28alL4QHAFxGA5thdPqMng5RthTtmHCEGxYYFfV2FmuDWR_gYvBG1Kbj5JJJhMF9_ZfaM8Tw6M3FYC4dff2DYMhlV8YXx6N_ACoHDj5Mdinlh4IzuNMuawQLqe0XFo7hYfoORPtHCB0KEaX_JvXkjtaxaYPPb60vJuzW7bDk1-_D2ay2sTw8c1ZQLlxDZueFKIFp4mvLb9VZeppkscjpTFezAxiLx7yx6B5mFfmm9IimKKxuw7dWKJgal1f7-2QZdiPDtGryzckIwM_haljgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L68Rq0AQvWTnOBxGRxYPCRsZu5F2G_4-eJytMcOOBJVy2K2DtTL-hz6be7oHVVfFqlemSFzkeLb__nL9_HqLQ9fmKZXrEX4OLiYT2iCUjwVD0a7B8ffRGVKs8Q9cijNrqNuFO6MzWVtI1DQ3axiKgp6sVmmbeJC3MJ5rRW17HgRnDH642KyL0181kXORlnD2Edm1Xe5ug3LFqB9Bl4H8hDleCCzk11RuyEUCqt0Egk3CIizDrJEXEoaUIftLLk18T7beYOqtvsTvJZ9xSPhQ31O7lfFC9WPzmgCoeyYdACLrOyKiT2JhuHu16X6BK0TZLAFgbknKtaw6HrUAvWm9ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=pz5CKloBbTRWJolVRY9ezIeP5F-ZyYohXownHhMGUz0JmGfL9TwnFjbrrOz0WZDLI0wp0gWU8MxruSHUUzshfhjgmN9NSBKT_g9icVmqlJBV1Cyc1O7SwFPEBvXEUThwYdK_7cyekFYX9f_HctP9mIWClOYXwzSMi0RRdHCdQFWpKqQT43aUGm1s1ZUogJJ1lDvlDctVT2ZDJjUe7eOQMNHesiGPrXusI5BWsVYfgbjdL6XVwFXL78CoiwBpJ4iGY_MIPf-WnzLTWbXC8yTxS5QbPO5Ttw_yZ3Z8ru0_S5A1sbhkhm47rJ_PJULUFV3WKZ8iLA2MVFjzcSRbDO2Oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=pz5CKloBbTRWJolVRY9ezIeP5F-ZyYohXownHhMGUz0JmGfL9TwnFjbrrOz0WZDLI0wp0gWU8MxruSHUUzshfhjgmN9NSBKT_g9icVmqlJBV1Cyc1O7SwFPEBvXEUThwYdK_7cyekFYX9f_HctP9mIWClOYXwzSMi0RRdHCdQFWpKqQT43aUGm1s1ZUogJJ1lDvlDctVT2ZDJjUe7eOQMNHesiGPrXusI5BWsVYfgbjdL6XVwFXL78CoiwBpJ4iGY_MIPf-WnzLTWbXC8yTxS5QbPO5Ttw_yZ3Z8ru0_S5A1sbhkhm47rJ_PJULUFV3WKZ8iLA2MVFjzcSRbDO2Oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRAT3uWe5UnIz9JX5HHGz0AkTj55_34uZWLxFAcGIv8A-6q6zz0IF4-X6O86Ktd46xTzCenBI4AVHT3xAB_HmEfjW2eGmnScUya9bY-s67RUbIsN0n50TnnbhfYmAQurBawX7QBFhheCh5_hlkYsjO3pCjoDZzGcy_I5tcgMxrJazatLpguqBtycn4Ah4o9-f5jDpftN2WzpbCrQHJRed0KgFqMh99BvMhaKBkDr3Mx1XHvXl-idlt1shRl4MVoJxo4sp26W55Ts_1ZX1ETgwWB8kvlQBIS2Bwp5tbwdL7FFYOuFpJO3bOoEoFvsKIkOLMguKDAxBibUg4O4NGudiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2PEZlFeLiDZsqPe7rRlGXrgjpdFA-twYQ_lYrRn3mVcu8GlKjZOdcSGNuK8iRhh2LV23SfG_3RLErsSs6NbEqprgYwX3WIHYwBG4V1gD2QcFzXxny9W6PEPnP2KqID97GtX-xx4WxVHT0Au4IsFzmxU2tXxlv7FHS4dOrdM4NHQ5TETBeI_VR6_w6xxup5fNKvXWEkT0_0ZmYkNdRTAERM5-ez9tj6kttiK1_KtJBCX6mY8qSb2JF6B_13xNY18LG6gFrUtqhPdk94-jtbI_rQYvL-mdD7qqp-WG9HYNXVNOlCC8nNtpYlOv9SqJ_EDF9rIE0rEaKkgRQk11ZCcuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en7WZjyaBPptW8i6XXwWndDn_RMoFwAIB1TudfhsYWK3WSkeMKOR0r03EdyAZj5kkbqqvTuE2bTEBx-rhSPDc8SBjWt-a1-4VWoHLf3v0dFQFln67rjKCt-rGP0cW6Orou5vowxnjnuznCJFu1plIMJbEGUQJM2Klz3XYvtjZw1nMqv9LozZd4mieAZH7SEF8CTxy95dCW8HI1mOCJz0q9WfjiEWGgAuq7EBTAy_u427gBx77d8ZjPIaaOkp1mZczOOfA46vYUcrgLHcUFiA_cMzFcpA5K6O6o3CiT4CdODSTxzsUnEYpnSXdSBzPVxgCfNsGcK0Z8WX8hgEMdVR5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2cRwVoFvFgTzj5bK4iPF9DEnp0AdHbhfqG9LQOYEwBsn4PE6wDIGw8EVmZmEgz8Ipawe-sXIaDYltY0R29FJ-UwJJLmpPbBbHvKVzbeYT-KXUkTG731EnDlyPoKrhMAG4f4AvVrPmF5Tcpp_m10XdN67QYfzFtHxPa-ht6qLiwBwW5Lt3bgGlY-91SVV0obPIGCPiSH6ww9cZPqoBsPQo5woFpn6gnq3P6_mlEWyv9Y7gt6ervWhHlFwWQ_mIh-qh8XsaeTUjxZ07IVlM28OLb1Eua7gPXiw8gH5KZjDJFRCUI1xpXDo4MM_NrEsUwHByvsvjmapsz1x6HM1jdyKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=GRbJf9zaMU170JXpr62lOnEzKrJT09as5zcvF2-u8fbCcFPNivKJzFFuqR7p2eXWnWQCcPsrYekI3p5q8A8gPunReEBpOg4sf_3fBNPq9fb5zxiGlIKeK38sFoepDh5Li6MFEA-jET61whbLWOyibvo2HhVaDMrNru-91z5evayW2FNUPsWk93w9_K3bbbGKDdMlpQVHXyDa9yn6yxN_v2qoL4h1__PYPus0o82mMTt0D_VRBo84HDFBbvSwiCesYgyp9NGJkyS1K-7_Qcz4lE6BtgaGi2JGHv42d6BVMdxwgSeMO1ue1lGqRRRH6D6nSjl1Efi-6ZhZuDiSUxk-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=GRbJf9zaMU170JXpr62lOnEzKrJT09as5zcvF2-u8fbCcFPNivKJzFFuqR7p2eXWnWQCcPsrYekI3p5q8A8gPunReEBpOg4sf_3fBNPq9fb5zxiGlIKeK38sFoepDh5Li6MFEA-jET61whbLWOyibvo2HhVaDMrNru-91z5evayW2FNUPsWk93w9_K3bbbGKDdMlpQVHXyDa9yn6yxN_v2qoL4h1__PYPus0o82mMTt0D_VRBo84HDFBbvSwiCesYgyp9NGJkyS1K-7_Qcz4lE6BtgaGi2JGHv42d6BVMdxwgSeMO1ue1lGqRRRH6D6nSjl1Efi-6ZhZuDiSUxk-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abRgnG041dnFJu7k4QIydfxWx0b9MCp5UpUim0fJHJpsjtkj8fHskXPGurSsKo4us7SoAUgsXO7sn8aNOzNSiPmMBpoGnA1Uaa6NsP76LrTgSE0-ttijntkJtSkv835oK9VsimtPNIoY120KhN0aEShnQrvFpfMSi852FJ_xz35Gck20H312VhXk4air79cDO6U_DVRpLfDTEG5AC70BthG09vJVnEjoiCoTcjmMtRJJ2rCttxcke-HLJuAHXfkF08Jw9XpLrUnjDt82vqWMf87CYN4oPCdrrY1radp7Q9jl6-t_xIF3MFIRhIY1CeAqsY6-VmVLziTEpvg9Iegj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0vH9Xtt4tgHHpD_e2rYd2AyvZsYTHErWl4IkOPohyQp6QOGtEvwqhlK25KJiY8ar8NJw-gy2nRuXBGcB9-AUimwPSuUmZdaK8pBGXneKFSI_cqah7_BYfzshRrk1AGmX-Y_rgrDj3py_XagnBshJYVMKDVZ1Be1sxCfQ-bDi-kM956shK1FHjAek2RUqwPsjNMzQPC1TXWxu27xvBAO0x74sA5t-M-gikxqrh33v3rkNxlFyobuWseLMr0EccoZfZy3WpngB8cT2RyWkw-7Ymb0hoklrwJeaKgIh-QigxlJApsM_q98wzki9JxJyV4oGJNaXZyulkFJulZr-kBLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkLSq9DG3qs_rNWfUWkB3wD3ja68m3E4G5jxmJI6I5ttEKuCziMDd0NaDZDeLk0kMntxxOAn97jDCcmpYT9QvnYVih7U4u4Om5YtRNYMxfFJze8N1KtW4QHcF_seXO3aGjFzgvMAbaC3engzb67b0eB0qwxGtNnci9vSzBNNukllnVG-zF_WF1uhFaFohG9Wd-eweFhTcKLh006vVcRhc-NAGu_Dj71Dzzq_iNPPiGzeUGCMulD6AN0_ulzfjdAzYx6cQPBAPmpa3cF0CbTlsErTt3vTrh8vcZuE8JDyekV28ST0zJyulkOWtw9kvvf55vPYUs_beHQ6sd8ZtkC5Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW2BwptJtRmy9Tqatz0Sp0JA76yZ0ybDkpZqNZYyyAmrPVtTy2vY81fobmBFJJNED9wFaekwElt0F6NXizKjjvILZZhi_R9bJdLnN6sM6rlZ9nWVvw2TBjbO4fdTE9wNPyQ1VJICUnIEjbCx4JJvir9JUu5qJK1Fntk4Uia44ITcMqmOUtS5NsHsHCbzwf1iZtoC9M8L7DhAbujvuURiBJ_nYV7eWLQc2vyNlBgheYoJNVInlxCK5HTrAa-_L2Zdz0HymLiRcnbDp_9G7Uf8ebFTRcqHyVRKw4AcyY_zEjgoWCfMh7tvuuVleZvCLXXAwLuBbPyIbEIuEayilFyd8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4VoGndHmYsFDZ3sIRuklO30YAKHTW-hGzgMP5bgvoTw6ViT9neXgvEwwlpYxJId8yBHB1mHuV4DrZ1p0FdF1TDRxeUvsgFl-qieL6Sp-Hwos8EgpSMb5VXDFmAgzJtLDeWvt7NcJlfxtLywRiHxXgCiD4grdpLMi2Hv9iJN4AyW0yVLLHchXUVs_N9aLJdY1et20DWpX3TBC2ux2sxRDRBKj7jcLG-chjXH3D0thGOJ7JN-4D6IUFd8DKn5kHSnCnzrHySe3SgGyd89jWB2slEYi9ZrnFDY_LiqlgVCrBm97_D_83lDO08-5aOoOWJiV_Q-iAtt8uYhRE9QRHx0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8SHaq-SpY2iJh3maTa30iKzdpNvj2VsGmU6hSRLV0BEWkVSASSLHZaVd0zB-2T3skVoU6KyAeLDf9RCuQDm1ofF97gF1XaK_fyTAvE7nrLIp30n-PAIfhXNpOALxQgy7UahaXIruz53F-ut4jxneNh8BndfIJLFdUUxaIt0snczPMixgHFOEyFz6hmwy1BZKugBxDENZlAtWJsMpsnR5DlTGZ5kCM8ts1D13VZ0y7_KwXr24_eFZc_jrY8Vlz8d3vY8hpD3KkheLy4QUSmvq2nfVK3C_XSQMGbKCYMOQKsUZiaGVqp1aZVyysNogpkaiCj000lFD47PYnUhFxZEtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Ru65XU8_u5yut1rGbNuhb1z_L6i0eMEC4nphMkdRKVD7OTid3EKWOKbnZmAuR9dhRwhtMEwTdwqIpjtavtKwJTeMXQgRz16ZJQD2SLnj78kYfgFyiTxyFwW6NAqIsleOanEmrK9LWOTpVjgcGsQBR05nsfyUtXMqaD8RHxDn73xj_ag2HRAKLc-P4VUkCyU4r7C-xzgo05cu3HFfOWtArvXr7gB5-6OVSJIBieaRQjoOmI-P-43mMMEIXncK1pRJ1rfUsKAnVDSr9g4bKP8XFiel9So2JAsAkbCwQnRqltrQUaI_D7KVH1-e-ir0d4lUPNThkDLkxLzyYwSlB5fJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Ru65XU8_u5yut1rGbNuhb1z_L6i0eMEC4nphMkdRKVD7OTid3EKWOKbnZmAuR9dhRwhtMEwTdwqIpjtavtKwJTeMXQgRz16ZJQD2SLnj78kYfgFyiTxyFwW6NAqIsleOanEmrK9LWOTpVjgcGsQBR05nsfyUtXMqaD8RHxDn73xj_ag2HRAKLc-P4VUkCyU4r7C-xzgo05cu3HFfOWtArvXr7gB5-6OVSJIBieaRQjoOmI-P-43mMMEIXncK1pRJ1rfUsKAnVDSr9g4bKP8XFiel9So2JAsAkbCwQnRqltrQUaI_D7KVH1-e-ir0d4lUPNThkDLkxLzyYwSlB5fJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlpZxd7zjqIR5VRZBBzCzv1JPyk9hoaRkFiPdX0J1WRyQRHrPjvXYOF9Yjz9DDtEJmS-kXFDynQ1TMZb5ivoo2wpUAyA7ePnc-X75gv3aIk3ormARopfp4Hyl8t-uCZSfO6O9ROk4ATx3Xxpp7bAIeZbkKVnOH_MKbhuXRrWNBJ4kypyAbr3ry60QHANfVx81O7ql7ATsLBM0MlgKWLGuwMrvk3Z4vCWHIsRWFQ19SGmEqn23uifHxMpPSajdyEUd4Hrjse2HdFTPyzCYmB4ntXYeLM0S5ODQJoCuPXzvX_MYks1SdLW4DfrEmyiKlf29dghb4t67BHQ7HqyKM2PCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1_NXx58EaBGi78o8Slzm2hW0O7aq-yuSaG1_dkm41KGiFgT0_w1rja_GFXxVuQzPHBCHZN5OR8Fi8msUnQFXFl1IfJXjN6jBE3iK9YgFjDNyONuPaPBhD99pvIBKnY1RVI3KsxO34GenWc6TimOC1ZkW7DDKjWLSNoDT2XXah4suYAsquA_cbeCObbLhBsieie1ocdMIn153xSIBH2aspZaB6iLs0ne4R38SYeF-Vq9J1GeXQ9NlI53LRKQu6H0aB8h6kvPC3b0ueMVhhiXTMmbl_tNOwiuZ1mvc-b4W_sj6qE3ZUIvYD6zW__iom7qLKtkmQOBM2lgnyQEO2XTMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwoflm_PexUHerjtXZkWLboZ9d0hceHVoxqH0LXdGx8moQdsJZCg44n4-wFxJAnbdJ8jMjycduqgETKcveQDs9TIfTJ82aP37LVZF4VrgjQ_wWfEBIFJO07iIUlYVi0LEXKk9wjP_o2qK_98p3bADBuD8-FCGtlA-JVNgqoOo4y8QjU0749S5YEEy6HN7UZ3pIfSmVRuA41vZjwm41HkdONFcIbHxTFKxfjTzVAZc-B2LwSDJ-Q8gh84pSZrWhy4aO9Mmfo0I-b0dnmC6VZnVYbIhl0erWe6K8SNrlRM3GAgLtYbfv3LRm-uyzZg-zY620NFWD6z-K54nJurh4kYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9cGeu8_KsH0slJ1l9xNTS05_KV0QtZFU0Z5gCTWfksY146WZw00pTCZmQSoaSILYeVLb_ni9YeuPJbbcueC7fBleHEKRjQIC7EIQ6Zvv3y3JZZiXGKCaDLawKuY_ODFsky1yo7r8jievKcPaVRCRRF1eTLK80tV0DO4VuD3xKHa-Z6BNgVf9giE95miwJKJaPxl5FaYot772Vt8jJezPan1DXw4Wa-Er67scmrhvi7NrVtr43rt1SsQJJtYqlbUwFg6OGBcwFkJ6cqscNb5h40LlaBVxH1368foReZdwGEPl3mxBGBqBmoMhJmpX6fqlllHowRmpbzn8giNuJ1-Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=EE8FDIm_GchK9bbHkuesy6aPtEGqvKJpSshvauTDOYfcMzSPRP0iLxn67Veezh15LcDaasNym8eApVLmet2iuwlOgn4oW_3ykkEp8eNRtBgnhCwqy5VKYEfR6-xkL84tOOIJkWZI-GmUavB19JqfUPSaMmC67VKOMdlqPAD2zd7P9Xenv8bUPjf7DjPUQRvHQa5NhmksIxodbC3ylsu4_fK0I-VdiwEcxTndzQUxLc3i_lpV-GkEokPOfZwqAoDNnc6GX5rfBFq-zk7d0M7SB8amksacCbZabh896tjs7aTZE9CobAgm5lPM_twke6Arux9TL3-MPf8cwwUWvyFVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=EE8FDIm_GchK9bbHkuesy6aPtEGqvKJpSshvauTDOYfcMzSPRP0iLxn67Veezh15LcDaasNym8eApVLmet2iuwlOgn4oW_3ykkEp8eNRtBgnhCwqy5VKYEfR6-xkL84tOOIJkWZI-GmUavB19JqfUPSaMmC67VKOMdlqPAD2zd7P9Xenv8bUPjf7DjPUQRvHQa5NhmksIxodbC3ylsu4_fK0I-VdiwEcxTndzQUxLc3i_lpV-GkEokPOfZwqAoDNnc6GX5rfBFq-zk7d0M7SB8amksacCbZabh896tjs7aTZE9CobAgm5lPM_twke6Arux9TL3-MPf8cwwUWvyFVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK0svEcXKZEz0ZJcyG49y6iKqXYSHkKnEVhUJq3ua3gj0OZbkmcbZ2ILmSSKR7KZw-bucxlMQNpY0jcVXyqL4XKLOdQ5B2qh9jeYxZ2CnT7P6fYRfuyudDUBswB9mqMmYLvfyMHMSqdxtYymCt-O6-UNRXavk-bFD5DVRBkd4iNvMt3AQtMGXDn9BnKVNUTXkb7pz8NLSdzlPRibwE2AR-52e_XMcQw25phdQLVElm69hEuzBSn40ouw0-r0UJG6CHFWaA4j-wGlEx4sW-cf-Dcx2qTS5ry_KffBfeaf_sXLCBreOjiLX-926OsYwpffhVSl7umb8hbJp29evwJJMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKdGA1sfQKdbNk5sF4fFpYG8hzHiBgbmXBxGv-Hyl43lvHLA6LMhN9_ac8EzNkF4C-AvCc9xAXWZCHsYLjkn1sw1FvjXYTP8C-cwdCCjB0hEvS1Nm2IwDFfZeFXF6L-XH5LIwWpgyNtuJcHsyudUqJWeszwnai_KjcQf389PGjtafhvTxs9a_eLYKwyKoI0TgaS-oA64OdHHk0ioP_lpq5CRm-jEbFyrbWC8GHD5ERwpsNjSCjN-nNOPAbmw6CI2jY-4wG_7ElkGyYqmZ52srcVdhmjOik4WOIWOl05BdG8wPYqwmgWjd1bgj0VnuD36QUO9QrB1g_49xbjVsT_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCeV5EnN3JA0gb2JTEaRjb7a4GbP2gDme6iKWhGaVNWnvg_9_Gk6K9kXAByVGYsxtiHIeNcSmG4IfxCQwEq9_b38SvLmTo4Z_VLggHvG_W16oj6RMgPYwIX5mkuM3VnfTnZ6wpChHa5CEL7d4_Gl7lC6iYlJoae_CBsuhtIjhLPSLU3SFSfkOsB7LK8KxrNvqoOjnd1DyJTunTKsmiMmBWedVsaZi3gaZZo9xucQK5q4qhYk5Z7KFc-q7De7e6IvMmC_SNrgMSdD8vkIUNuLro0YZ-dgBaQPDnGjCUP1I1oYxzj_1TL4nxDWp7-bDjuKKJlZzQ7kR5yaQeFpAw9JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT9DrJWqMxlWFJiAWQd2tN0PPg39RlAmxAFhSzpco3ezFZEQUYO1Y1ozTW-6zlzs851Ngb8gwQ-pEM9Yt1fUiOvN8hf3okwzWRXXfHeoGw9-tShYzHwPQ6rfkQxtsa64PJBavKlWKZdRgeZWBeqfD9Z5jY0xvgR7GWKjkmmJ9GSmhPQVXz4O4hHtVYuvM9zOLkSCRINTJ9OEvV8bx3Z93bz9NYmXQ7yYFGcWxzB7tbBR12i3PJLUU-gckfH-hSiOmyHR590pHjJ5xHJRxf5g2BOrONHFK-sSzrlDucM6dUkIhBHtjrjN4g5_cmo2yfp6Pyut8QOE4-oqEv1kXx_1ZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=Ed9o-jnFI92Yeur9fauxs12nL4hnLCZfH_C_zC6nk4N-49jr6BVb4txnShp4iDop0lVJ_xvNG8HlGDwvwlzCA08byne2wmkqyjpY8t1MW89r6qq7fMmpJa1oK2OxcmpclWi-zaP6IXlEM8Y5M-htpLj9TOtnWYV82BTf7Bv6px6WUwc15OSiVYXeYDfLvJFWJNSJGoUdMN0soUd7qaIBBJmlL4pGAfOdNyEyVX3jq4dZMjQ76P9lYDnFZWg8eQrY3QVRN-1yGlig7KwtpkP74iNBCp_dDBG3R9gO7BercLqu846BpOx5xLXnf2GMn1Qq8HdHpuReVjVzUrWKtXaiag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=Ed9o-jnFI92Yeur9fauxs12nL4hnLCZfH_C_zC6nk4N-49jr6BVb4txnShp4iDop0lVJ_xvNG8HlGDwvwlzCA08byne2wmkqyjpY8t1MW89r6qq7fMmpJa1oK2OxcmpclWi-zaP6IXlEM8Y5M-htpLj9TOtnWYV82BTf7Bv6px6WUwc15OSiVYXeYDfLvJFWJNSJGoUdMN0soUd7qaIBBJmlL4pGAfOdNyEyVX3jq4dZMjQ76P9lYDnFZWg8eQrY3QVRN-1yGlig7KwtpkP74iNBCp_dDBG3R9gO7BercLqu846BpOx5xLXnf2GMn1Qq8HdHpuReVjVzUrWKtXaiag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=aCdHyEhdXc8jaHnOLG8jqjsai44WSfcGiBaWD5hG2yN9T3Lmr156WlpaVMu_jG9MgqTc27zxyoN8ryJP0kDrIH7496sz-8SfiZFyTDusSaQEJHDkAuTGocDmiAPrDUV4irWRiS7bJjZhuM9nIkuLgszVhb4DnxR2cpjhjRgAoyyI8bOGgvl7tctSdrl32ZuFnitw10z6Ku-Fp42WTtxVkzNMQUP6X725JLWMbiXvFV2rVWquAKsg2JEQw2iDHSExK-JB1Zv6GZMtmul8IWIoLysjbYF-W14XPT_CvJrpg4Ciq0jYEsEULrDVUptg8nbLj7Z0hNUaX4MOEh39ZS8LKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=aCdHyEhdXc8jaHnOLG8jqjsai44WSfcGiBaWD5hG2yN9T3Lmr156WlpaVMu_jG9MgqTc27zxyoN8ryJP0kDrIH7496sz-8SfiZFyTDusSaQEJHDkAuTGocDmiAPrDUV4irWRiS7bJjZhuM9nIkuLgszVhb4DnxR2cpjhjRgAoyyI8bOGgvl7tctSdrl32ZuFnitw10z6Ku-Fp42WTtxVkzNMQUP6X725JLWMbiXvFV2rVWquAKsg2JEQw2iDHSExK-JB1Zv6GZMtmul8IWIoLysjbYF-W14XPT_CvJrpg4Ciq0jYEsEULrDVUptg8nbLj7Z0hNUaX4MOEh39ZS8LKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
