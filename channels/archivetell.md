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
<img src="https://cdn4.telesco.pe/file/hxGTR6gecU4w7fW4D2v93s3rQ7zn-fNhTJqiDUJSXGZNoRFtSJ0MHK-UXQd00YZzDi5IWGK6kS3vvJGzbrwVsRxgYYrWn_ZuC3pc5AsGoKCRjfM0_SperiC3hQmRNQ88Aolv7tcJOWvcyboi4UXhrJP353bX-1aEYi6Ew5qHqS56l5B-25gPRpiy7uwEa_JEWNTTczzfdosOnSkgyGm0ZUNL1Sp74zLIF99ziKy-Zu07v_6Ep1fZGF1f00cIx7gGYxAcMSFR_HBoKvDzOwvfvMkMPhd-dzHL-aMs4HLIwsR0Kth1z65q4gdN7QP6pcENgNUUURXKEWUfYktIkadACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.68K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
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
<div class="tg-footer">👁️ 192 · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 576 · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 990 · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzIEF5uxmVT6w6jmnnusFbQ3oxDWoU13ypadYGBZe3iioKppjOtqOIGaYrcjemHoYVX0gHaGe2xitKTC0qUbGOPiNnALfG0tM-l07JiboyxTA0WmouNZlr292plyAD7trJRvhcdnC7IanmepzOeHDbmCvyVBrdbHcu48DWBaytmpmWPEPt7wRtxA2jT4u_hJwhCpiDuDR1kcR26HNs3oQ3GC6N8fxxL_Bh7c6MVNVBdrK9wnIW31MPCAWBPpNax9IsakPJVprJGBjH_dwUPohsemJXegps7JWzSGA_U3HE-87Kc_E6m-SwpPrYSi52P8_st5oNMvJjfAtwZ0GidRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcHWcevdaK2MZUUm1I7sdGakQzkGeGevjcIUdVYuR26hqUFHsesmSUtQunCa2LvchhwMw0-88uoSr4LzqdXcvdHkxKfjgOP4Bb590G39MwfbaNMhHLTZqK5Nsfnm3UdWNoYRmtpZt6rvEj9kPETGFk18Ti74PeXXFJN3F8NfAS4bDcRkmqF-F0ZvB0gcQ0nrdpnmT1Pw4rovkQuiU0vaDPZQ1tE60IaVkZEH1vKIujxHpvlmPTjK6RuWCfo4CCF45icGdoi0XCL14d9zuxKiOR6Aj5zsB9C-SEw0FHt6B2fwj97GTw2Y7yNJuHrSq2WiFFq1fDKr0O24ZDLYNmxasw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1eVwwl8Z_pnQ_Z9qsNiGE4yyNNFRiG7NgHUEeHUEmA3UkrcamnaunBv-NtEoYo9N-5gfTTw0pjk6W5HBKvaSIfn7xzj6LWXIQ9M2SL9Xc6_r__euSEsjCSaGjc0bv4tktqgf2hy4sq2nsANQUhR8dxt2l4idQM0RVcd14XePkUpwyiSaJX5dv-xTHCvWmfYERciZzBHV3dE7ScWs_CMr_2MrUFNw-Ea72LKnuRrjQz3AOnFBeZ-PfGHNPKXN4XcsNZvejGa-APrJbG6b9QTW9IAGKGlZeIAbP300TEBQJyf7WdXT4tZQwN9XEr9yuZE7UExdr1H3GleKEP35d06sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbVoxGd6Q2XvspGSVQ3uw7XtHVD7Ee8qFocEehAEaz9FbqTkiV-Ipn09ZSNJ6zjGzAUA2TQu2gsofap3aM1qTiagQJiLlN94lxTTKsG86g1vbr8hZ_LEgBmYA1ZIzdMSrn6LqlDS7rK9nL8x2EmrIFp_torC7Yu9aDaKIAdgDVuXBx2Qy5lJAWpyvPhnO261FkeMaVzYrjKpG69FoaJtmtR3psuSUEV8F3Ygr1h8zn3ZFsHIfHMaXL-H9_PGHXz0j7c10ieoSZhvjwaT1_YbMAfRRgPIZYTerabm-wZz-9zqkSsavoq6xrwYjfuAcvJCXHE8EMEMq0X3Bp3zFPCe3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z92FuYTpaG4ztaKhSCgO1wfYzb2sDaqQUHSOJJnbqjk_EaPCj0OuIlRw15gnlEBd9pLajpb9ghNQJ_qZ0hmSGPV5edcxZU9uJ4bRQelK3pUfUhhmV8FPjDtlyHZ-CYx7-VjgcmU-a9lztGygEa9wQXz6rQXyVSx2c7KR2c8WD5xsRA_4Zzr0hHT_ZaSTK49fVh_HHQJwVppRIMosERh1X-K2ufGjhVXhIfn5ucWC7lWiNwmpU-B6AvQtB3pUADVdr8HyttL4QP-MarjoJqio4kMQMNNVkzCrtSPAt9j77pGGVBTEBMg8ZwBvsTaKSJ27bIFwmTUxR2E3m8QdwOtgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjAhZ45wFsAiTjv8GHjbbcrZf1wF6fD0UlbWFzl8ONvVhTFWQcxDGT2tPBvrYhze-2dRMufKFFx-Pk1kmwLI-iv1GxGWg48ksS8PMMt8KehP8n6dzNQvqmzKTw598-YaP19_ybUbu6yLhOwjlI7CAfg_auD2u1YFiE56rhlireBa39jEn0HUKdVVMWMe-YFr3kjW-8sEIdmbWJt75pcfyTQ6P4hZPqXTte6p9M4qRkV2yeWSwFEFoOAm4HufVHUPrKymLIQP5zTOSDDL3WsKKnS8_rFpGWoyXiAFMZqqny20K7NCSg2bR5R-Oy5kutpX_f1zadgvHrHvrH5arVSBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIG6SQS5fz1j567Yphjgkiyjtv99A8aySpvnWPsRHDtuYdRlmk7EPBkdHeQ7WCoXtz3EK5JkHV5ecjw_9G2rTYI3f8MNxpFxrLkbVwbUxXkpTc48aPu_Jv0O3vuJ29dBxpAzCWRBsIiu3Kn3f-bbcqyG4pPQ7NQQwFwMOcYzaZe8JCL9PMAb71Mtt7JyX5ziKsBl6G8-A5YaZNOPSSijmO-uR83XS9oGe2IzjWDEfYw3ECQOxKFjDXuBQrSz5XflNJ-LVEb-CRStDG1ItE7Zwc_7NFQznOO95uXk7Sei4bptqztrTB7kSPvRJkrJdjZt2KxZsXGDA2XfvHfuJMkb8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLHHC0i5gFQSWV0AeLITUlMkGtXMI4J2bWNH1NNFJdA9Q24f5JEdjb76bllKoNC55lKgnPXA998Kg3hXPrVkd7n12K46HywDbLkpNs40qKEHIwnnBoqj_NnGWzbUylqiFH4CJ0TTslgrsY4mn3wKHA1W2XG33oRQ_nKSscp8ehvTfAX9_y7DKrdTR2ZDK5R6NUu0AZvq_-DBw5vjIci8PmjqnxFsU4LHL4QUMBp2cFW0ZT_3sxUiXyKykiCX8UAUPc57YHtrNMmp_sOv8mlE4HFdg_WWgk9bwQZEVIW4QupOEMplP286oUexwJTCDixOKRnpn7j1yZfFeoEbcoMmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhkCrS69nrm9jpTKWP20I_h0P1zlvT_dCttJa8TzlcTm0o6uDWkNUoTHPZCTITEqUQNrj8zrIXl1xWphcrnvJe4XgJ1KuERuZWZdve1qHSukg2mO-zhVvfnczm5NE0NzOEIue4hup4BsEwYdwW_ytSyUkHcR6KPZARd0aTMUJwtQcANVlVGpAdRNgwOsefFPWFhpfx_2qPPbh3LH9Jw_G8zBrLVpU2uURalvrQyC8FhieaM6gDIYRCr9bPKeFWuUhvnL_X1crk6JP8ZRfXL025HS-I1qz9X8bbKOA4litGOo0bszdUE7EURRvU-HAwCzp3GkrksVU6uoS_ImhyasCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFfD-U2wBHhNIZKPUxiCNe9ij78HBNHfm46AF1nFcZEtgYhVt-Md1Ch8OfOzLuCqBz2DcnYX-TORCWudzC79ALpXgvZDRc2MG3tGObdO5nKdt1s3fLExy4j1bxtYhKzRW-PBEci6gNjfRSFEzOuvmkLkgcg2CF9ak17KNY-v6H2Bc8wZL_u3i_hYYNfYJDq3cW6Xv_0CiUw6w2DYfA7df4J9xXOTzuKQGiYBga74M9yz9QfIeRi6iFusQJS2lAwuWiijbjPrB7AqPu_RRowK3LxxnyW32dc5izzDMNopByNTE1MwXppwVejV51YIXntN5mlZM8sAQ_7VUXgKfTF0w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=tehuMHxUivx_rvHQJfQRdwGHEQbUa8KqmyNt7Q_-R9Cb1-DV2rPBSDdM38ac1wNUCJWZxaCs0XAZzzEFy595uO4k8abRg2PJaF8JFVJ92M91daCa35mJFMfgnWmRG9jJSO3QLxUDSrVRkYw4yQfOne2NjmR7J5m_mA2LFDsSmRWNZK88Geo9PN_AljCoGWGJ_ogak3YXW0G6QGg1bs7QOpgjxXJLuUcuJpFxxToDyhzIVJqNRM2TvrsmgbF9I1lpl9gUhh7Ub7fnultCtdxmFmDRIS4pQTlcbCqldeDwqFJD0DL9nInHnaHw8z-A34hk3no9xEWxpSx7OvCJbLYkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=tehuMHxUivx_rvHQJfQRdwGHEQbUa8KqmyNt7Q_-R9Cb1-DV2rPBSDdM38ac1wNUCJWZxaCs0XAZzzEFy595uO4k8abRg2PJaF8JFVJ92M91daCa35mJFMfgnWmRG9jJSO3QLxUDSrVRkYw4yQfOne2NjmR7J5m_mA2LFDsSmRWNZK88Geo9PN_AljCoGWGJ_ogak3YXW0G6QGg1bs7QOpgjxXJLuUcuJpFxxToDyhzIVJqNRM2TvrsmgbF9I1lpl9gUhh7Ub7fnultCtdxmFmDRIS4pQTlcbCqldeDwqFJD0DL9nInHnaHw8z-A34hk3no9xEWxpSx7OvCJbLYkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWrsOrRBQM0h83BSzj5xxC79bUS5iJHPALpyF5wQ2TRY95W_H7GAfHGKEd05lE5G1rPQxjdoD6ZG9xTBCajC4tOzmF0iop8_FcjskAESVz6pGGUvXNIaeaRn8V6TQODwCpVGfZLkVD2jRDofW6z3R5yvA79OYheyx-ebvCfYz7k9Y4d10DJshLmdxSD2Pw-4SqMfw77SvWrKP4JKk9QwZwrRfpTwI0F90-OwqSYX5K5GLtxzIrHrda8_sniD6xbvl2vpf93Ax5EYjJADU_yi84lY-0Cw9whfqYvoYUZYIIS_xbB48bc_8eYn_HVfc20NqIB2QiddW5CzLiVzNlTmYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa-HJlXQ82K6tvbQRVgCj6_MViJfKa4GycDB0DV_edU6leLTideFoPQCNpisPlWVMGH_MhoTCcjbOpAFE_BDogsjRAhwiFq_gD21PrkMDTH_UacmJwekUc2a87VGUlQPm4MneLSZ79RGofu2mRzH4fwbUVGJpxUzWw8IG-ou6XkjaPAM5NqEc17TP4O2G0N7xLs7Cnu03x3izkrfvJ1yONnsdE7wj4X2vINxajazK0CrFCFu5LvrezZ97LuyDDFq_Z6xE41NOIxRPaO_KYKAgomtXUBhUqBltn44i4aYEXb1Pp0ZeDiEmqJYvQoRNj2ME9mgbHCHB93giA3YIk3y_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=BweCIjl2zGHOrXGFmOiw0YtszfSXCdrvaptFSRoGb602OKGopv2faGVR4GC7aRSQlmm0wjlimSMHZDLBiAcL5A-dWbx313lhsdg1EvZg-n7OGVLsWU1Q03AnD1GxjO_6KsPpwhi_m3n2XlPpqzMZROjq4RUpUh6ggq4W4siIi6BgGaoFZ9FPwR1miaMRYOMgHRags8ZMTUy24xEG2_MlWyMIWqZYGB8gOz16NBkwKG--4TVm15dY0EQ2ceLqVNV0hsdsRKYvLeOS7cSuTlbav2XPoHwGTfN6wLtx-FmCGD22dv0bHO3Aef3-kzwBxhK1Sw3OKsWQqcT0CRmtwDX0daICjZ_u3Z3eiS8_PL5kN1JKuioms5OdfGDnQk8h5X5gpELJAeQUchyq7JKHDUA86udP1mz2jojjfRI7usON4yzzO9cXcb9JNiBgxXzbhLsmsezTXDKjfTFWQrJFfkpk9OmPLOu5nh-NetqOvV65QNyIVNS3kJx7-CU0E3kpkWHf2vjetDCQnvX7eG--Ch1f0nTQnt9fZ1QW02DsEx5GzcM7BNRg2TXIazEeT_L2GsQzmrqAFBd4-6rNs0-XEItCx8oPUdBfCkIMIEhCU2jb8J7AXMGe87Dy1vDpUcsdBCTL_Au2Wuf5psDjvX7uSSLT4Z1vCV6ELzKhl79OAWW1HAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=BweCIjl2zGHOrXGFmOiw0YtszfSXCdrvaptFSRoGb602OKGopv2faGVR4GC7aRSQlmm0wjlimSMHZDLBiAcL5A-dWbx313lhsdg1EvZg-n7OGVLsWU1Q03AnD1GxjO_6KsPpwhi_m3n2XlPpqzMZROjq4RUpUh6ggq4W4siIi6BgGaoFZ9FPwR1miaMRYOMgHRags8ZMTUy24xEG2_MlWyMIWqZYGB8gOz16NBkwKG--4TVm15dY0EQ2ceLqVNV0hsdsRKYvLeOS7cSuTlbav2XPoHwGTfN6wLtx-FmCGD22dv0bHO3Aef3-kzwBxhK1Sw3OKsWQqcT0CRmtwDX0daICjZ_u3Z3eiS8_PL5kN1JKuioms5OdfGDnQk8h5X5gpELJAeQUchyq7JKHDUA86udP1mz2jojjfRI7usON4yzzO9cXcb9JNiBgxXzbhLsmsezTXDKjfTFWQrJFfkpk9OmPLOu5nh-NetqOvV65QNyIVNS3kJx7-CU0E3kpkWHf2vjetDCQnvX7eG--Ch1f0nTQnt9fZ1QW02DsEx5GzcM7BNRg2TXIazEeT_L2GsQzmrqAFBd4-6rNs0-XEItCx8oPUdBfCkIMIEhCU2jb8J7AXMGe87Dy1vDpUcsdBCTL_Au2Wuf5psDjvX7uSSLT4Z1vCV6ELzKhl79OAWW1HAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=lJ9uSfsXSxliebi4J68HEV3y2SJ_hcoFwCrSXgcSjCPY47hGqvSF4cUbsLcHlt4Qrm3G-DKOpCAOmRuguL4fguKx3D8uhvGR3Pb_6jVt5xruvWIKphgOlW_5N22RRAwF2kvCG7-yz-jO3b2JLekLX0tYlbYSpu36c2BcJn9f1TvzmAukgCCymkolRqZ-lRkTs1TUHfg7i0rErtCycJJ909z0RnuQwA7KkeDjBFE5fLU4drQsfDzAWO-D7YKSnpoi4QP72S5mLakCX2qdvUQVkdmhcx-f4hQ1KGkB4G347ON42qF4G1WNo-DOXN-RRKlgAKkgT7WaneEffiVtlsIKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=lJ9uSfsXSxliebi4J68HEV3y2SJ_hcoFwCrSXgcSjCPY47hGqvSF4cUbsLcHlt4Qrm3G-DKOpCAOmRuguL4fguKx3D8uhvGR3Pb_6jVt5xruvWIKphgOlW_5N22RRAwF2kvCG7-yz-jO3b2JLekLX0tYlbYSpu36c2BcJn9f1TvzmAukgCCymkolRqZ-lRkTs1TUHfg7i0rErtCycJJ909z0RnuQwA7KkeDjBFE5fLU4drQsfDzAWO-D7YKSnpoi4QP72S5mLakCX2qdvUQVkdmhcx-f4hQ1KGkB4G347ON42qF4G1WNo-DOXN-RRKlgAKkgT7WaneEffiVtlsIKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWW9kDQjS98GpVkszsCGrkA6xTI-J9U0QWGg68RDfuaZC0ybl6GKBVwU8ok4Su9e9dHL4T6Y5-TvLDclwU8Geby6BTxV9VZbPqbWmo9Be0eLNmR3ison34SAqHTYNyu3BayPX83xkTFYG49X6dM5ou74Gibfcx20snP7XKqGd-hS_W4NrMFWxSj_Imh5UxMzgL4JSX-DOu_FW3OAqZ4L1ubhfEMua_5WnavyDlNfstay6_lxk7KKb5YyqiuvZ7irh76NxtWIBp72rkaa-wZxtUONeJ84FSYy6yIv9moEg_7Q6i1xs-P2y8vCYy4k0-zzLHiyhnqpg63oy4I_3VU0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZWhAMUUZaqGg06lKH4eO9PRlcjsqHsfn7NcOJ2CiRXSkwsw3_76WYlbGvZVylJCON-iGarYzWgDLZkxlwMJH0xuODUzP0NGdbjSj6csDouyNJAih0x8ALfobTpIkNsN8luxLYaq_JJD-yAys8fKjqg7FK0L5jpxeK6i_kt1XRYFd5Fw9_W0ksTJgH364SGqdFw8Pf6vgPA9Ri7wELQzJqtD4sOvDImVe7K-EHid8RAs74xTOxl2Bk8Nar06RSVm8BIYJJb3NNSlX5a94lYG2oUb7RHMj02aojpU6e5zSvhDygjYizsIr0BPYxfkz_Q1Lgb82WJ8Iu2PB9WISB3ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLvcGVYHCnXSCjXgjiOl5Rqb__sp9ePmRZF4xHoAn5qyRMEBZ-oOfEp--Ki5HX4bGl1klkyWTvvy4LwN_dllv1HFXhb3nzZoCdsPvbp9yg72hpb5X-FUM8P5aTcujHNIJNy1bCjgZPhzABOC63lASrXbtVa40Jjf8rg9xOEMFhNImx5M019hS9CmG3oRa_A4-j_Fpq3s8LkdZih1oxy5Ns0MXozvhkQv97SwJCAJ26OUm4FArGG6ml64oht2PQmPl_UCrIRpBDIVw2EY1GWl190larKQO18eEiGpTW6NbBFSIMZGcbH89ku1-JVMBY5UfaJ9_abD2pgoq7N5T75--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMqa4QWCnEiASaroCWz2OFjtr6AbvaGx3uM94jzd0yDbSW9xEP-w_HKPYV9ipev8wMFOoOBemnLyvFnbIWtOrUtON4-j-Yr5PM3dhCk1yf4IuN8_yCSv_6uTkIyQrKmQGKpIxCv9imaXi1xr_TZE-RyEIrF69dRzZV8M8JA4aJDhFxI3R5w3GByizPi20H_Kpo_JcKHIY0i5OKgDzz5SZtSyT6Kf1s0PD1yylQwR3Tb5WjJWUFcbFtrN3-DVost8hbSB1djBtf3NMqHfE_aArsBh91I8kvFibxGCzfBukPZfk5LGqBvfylwntQyAXv080gzRJeo75YmNMmGGQN9Rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgwIiA_s2MLfm8HPS5k1RfG8RfoDzQcmzxE4pMkaQFIj4-BmOZdqHUB2U13PW0cko3MdE52_5w-xWRGJFI1-egXDzuc55hHTC_yyNdmnTDNKJvgUdS_OoGz_m1nwNxjK7_qLsj17p-ng2L_4SeeZif52BbFCBo8K0FshcB3J2MiH9ywGSWziyvanzRSrAy0JpNg-ABAXagrrenjiPj6TttHu7FcM4Jz9LGTC6tMEAbbrttBtLDNlKKGUYdzrh-M-VSIIcePnyPfzOD2R-XT5CV72P7d-JHE74gO3YRgfUrcuIxpC4rczybrDfxa5MAiUMrYEfBlgZ_MGEUZikBsJpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr42zrFJEhmCWw36-1zaxxSSyvlPOHF1ZVwn9ogK2rd89PiVm28DSpA9A9d-X9CsZcUlv1UOYIe2D4Fmz1X-L69xcCRPxpbJR49R-XRC-oW-ddr9-RQ3jvhk9Jicl_KeWfE3KlAExImeMqKDreCHjL_ejVlHKK1GzEE4uHV40h3GiNezjyoSPmB_ybJEzt9GLCYSPKM8ieRuB37E2zEPKMpAFtnCU9DEzWeEMhTO3LhQzpvBHNU5NHsPhkyyZqDqmPJIU1I0575y4jq9O9ZhuSEDYw4jWCYGWDp6-5JvR2WDZdfB_FXN6HIo3g3EueGKDaxHRwlFRvc6tob45_Qg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyAe3vuPwcxdfkmBrFJCdbTkz5rMuONxUQvP__O0boPJKf1WoRjcMzTEX8w9o-VMgzkh83HnL4MYOcra1cmQH4tbHxSL7sUHzOeaOHsJE3V7csnPIqZc3Q6UGl1OZ01ZIEQVO1tsBE9Wn_RSKl-F4KIemHzxNbFjLtSx-nurPxl9A7FVDxnmFWEsDZazWK-Oeji97kEI5kBS1cNtywZYmgEkZ3uf7E4DUmNdNW5ZlJLKt6ByGGeAo4tyP7RYe_juxRzdorDnkgWND2foVnarBzz-tjUOBoEV3uFnI2wCkleAiIX4tgqTg5KOdBDTkO7VxsXtzkKcO5Ru0cpWkJAnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8GCGG1vtes5YP9Rn-r-8SLxw7nPIj6tuSmy8EkAZdKEjvCEDdyZNwqXfJf0IAgLKDJsBWRxK6xZUh7i3fT4j56o0B_xsnlfHNnCNE27cYjX_3V9RXl9iaEAul9IVmF1rVgqruYNAjc1itmcIKykuH9G9W_PZhuJmrZB0RT-LhrAX31fzyC94PB4jOCJLYltSO6F3_aGCjAeCA1X0Gj2lQNDxD-ZaPf1QRb04J_bk-rTdiyZb5TIzYbAJKsfrqW61CRZ1i_B9R6meOxB4v7w07UBB7lqsgSX9BzJsiWg1ZQ3g3Fhh-nclwT0txUd2BFyPAGxDuPltY2gPQNGh0A4Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnb3upx4tPw95jeSXk_sR_2M2a03iRWVsx1AlKHeH9oXXhghmTc7_P2V0fZDbAQGybUzbG69osdlzzFA2JyCVi3aoo20D7-BUGOk-kmiF-CcIbYeF-Oa9GPZVjZLOi6DahMJusYGpOg5zyq8DpuOU3KIJjVFIua2Nsr7_xwrbrhx5Vhap7VF048gSh3VIIbO1FOkOkOcl923B1w3a4QnuSlnJVGZTRn5sunpihP2QaApQ8TTuZ-wqNn7o7cq-raTRtaFDLna4alqWQzXK_7aaD40In7SVUcRm5KbxlDGgITXoDrDC2HZGBIkl1Anqon1hJ007BlIy175HGKP4kr2KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znj3AskLtuzpErdfPSwtHD8phIe3NheBTBgBdCP-6vPcXTNCdBlLaYxX9uyP2t6IDgDSYXw1rVuAP7saQaFNcEjb3axzKUkoyKlvhxhjvGUgPRAojvHnNlfWwR2OUg16CiY9yl-kRBNpESSJ1TMKoPY-4jDDHa1kJMcfVPLPDtRoR8rD2_WNEx21XBTarPTJ0MfTGbePXRHXEtmlqiEuZaxSvSVut1U7I2HL-wGpEezSOBwSR57IFCkm-68p3zw6Cl-8tGHw0gBZLi5mxatvmEqJYKHayNbko9zSHrs1DrlrmCAagbx7aXEqNM-jGvVl3cze3QbfSxFDvDbSANbFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq3wx0BVN1Ya1ACym_J1A2vfKQuWrt-oOu9Qey9ujkQVaETu_zbkjVd1hV7uKhykFFkQ2F2BEsmA8EHaq6IxpJPIUiIX1sO4kRtxmgMPljivEpdfSPyPCKQASO7CQW76Ly5lqwyGmP-1S-yrz3FQeohP5kLyL0-z84Q2PGO3drBgOVNHmGVeX_8mB_6eHeYjRa5PC6LdnTys1bzLxB-lii47-MuUHUDCzqs4UhR8zHVud3y9B8D2hKFOYlofPA6JqglK0M9A-4i-qWEw1MLKF8ptKDd-Xbbqe2-MnWZPXfilQfG_3t6HFFtvnx0Ye9yz7mKaYYR_Yut3UZtPFTeHAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCB7wfhOY3xrdg3Rr_XrTk4AXoXxG3eC0rNwVizOvBNZWztsHrg_OYqF96Wa9Xdi297BiFPBMGoRRKUoKm3eN9_pAVXxr_nykzRX5sr3dkzf3FYHryz-pBMZLStSSXT-le3WWoZkwwHk_vdYt1aKjICHTwc-rDXNsrwYaHAfmmoChoHMgB_KsrsBwcp5X5DMGr18PxL2T8isz71FIcpdRZDrWhWuBDnrHXVgnJLp0HkQuLys7-jT7-BvA2yXsYMd4l-KhaF4QFWaSIdz64035BsHiHETkYm9txTpAHrR8VovvkSXcsf8yq08QU34qLMjZxERUOpOxwookpSXtqtWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=H5Rpa_vVLigm375kHfp6bTwGRiBNOzwuuC_GiLLW5aGBU_2Sul3piSJLHJznY3eQPxEEwfbXVy8Z7NolyH9f8IAf4KSsbPynJeR5tb_UKsAdOmEv-KgvouQnb-lpeVIsrQNDO2-yuSHvM8D6y4nuJ19C-alTrK9cEaNxI5509Tq4ALiHcn2vDOiJbtF4JcTh-Zu84O8nVj2qM9NrVqE66gfAbChatp2k6_X8f0JVazXHV-h6ACls9Y0fanFBJ4nRJxcWtMN9EB-ppOBbzkaah5CL3CS_LZ1LwM9fFtywF1R4spYWAUV4SSUHiVajxOHU_leeA48_YdN-wM-ufKz6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=H5Rpa_vVLigm375kHfp6bTwGRiBNOzwuuC_GiLLW5aGBU_2Sul3piSJLHJznY3eQPxEEwfbXVy8Z7NolyH9f8IAf4KSsbPynJeR5tb_UKsAdOmEv-KgvouQnb-lpeVIsrQNDO2-yuSHvM8D6y4nuJ19C-alTrK9cEaNxI5509Tq4ALiHcn2vDOiJbtF4JcTh-Zu84O8nVj2qM9NrVqE66gfAbChatp2k6_X8f0JVazXHV-h6ACls9Y0fanFBJ4nRJxcWtMN9EB-ppOBbzkaah5CL3CS_LZ1LwM9fFtywF1R4spYWAUV4SSUHiVajxOHU_leeA48_YdN-wM-ufKz6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbzSII6yJmCau4weFU4YypUj7XvnoeVHQkRQCShjc47RlmPTXFlfsPY9W0SEn14DZHy2md9EzMPFPfWWr64mgScDU1MbspCR6raHK_5C-pSd9_tPAmfwLGO0OsFwyIgOtHtZvKUG8W2xgTtdl7Uv_fbxVyTiqh4pKDW9JUO7Rh7kg43ZtXWqLuAqSPzWsxuTg3N_v0_A3NfIjPWOx5G_gbecL0NKUoSCPMrJeF7rBYNlSL2Sb30UWBzdNrzzXokmIz3eYYK-BGxV25OAAm8NVRlSkf5PD0--S-roXmgFQF6fDVZIZ2kDwvQmyAQ1ALbNo4dFHKnuvi1UQA7kcSsWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCvhWXPxWyJ8kjF5Kw-vD-D5P-k5wMNA4vpovAEvsx6AM68v94-YRPR7UODj5_AKIQMutj4nRNttoNq-QCcsTT5cSnL2WQ1foUfxBYqNvX9RMDQjbcjd0Hf1eRMSJsQCCDLnU_ZOwjdm4VovKgmFuos3lqhb9c8ewvwEwaDIfLSOXTVAkez2qzGHcDDpsqGhVnPIal_RwsF50u0UzIchGsltH_j36N7l7npr5Uy9w4xaQTPPdW23cU0P_wzQpwjQ7f-ttibom8D6DryqOyUYCbv4sSzNQcb3s5yqxF1aEBvllaNb5PL3sySvuGClRNtfxQRrsz_UNJzG1XviHujQRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNA3c8TEV9c2augh4gqHG3gv_-aJM7UIWMvZ83ozLok6KV6GcYGR7GFRwg15orata2M0Jv20bDZMpAlLFjlAnv8QqZXtekjM4336yNb51V6ZZipG_19OxZUrlPY2wTrRS9Enk8IN4qZOCzB4_0CKHtHic7t0XTrkCddsa9QZuOzQbxiiEj2oTUOTire32jsiwF6uB0iaTBPuGhBSQZwhRsKR9dgTffXaURvNKguRpPsjqa23iO89tgofIpPJ2qO4DmFWFlMlq9AQLcwdgI2knh9PMVRwV-1x1o8hxTIw856aKQXKZCzlDPxQZiRgYieo2MWSBKvOUbq2uBxVeiHJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaTEmGI-bf8NZCu_Kj7sfXZXUsq20CBzMjic_ip8PLy0BmsOPS9eFU6AqeqcSV1nnUEBUUBRac_qNwqxtBPeBb9MDqt-a8PqmUuSu-JSu0FyradrMQVdbJTEKID-UtBIR9Dq4zMBckQB51DIH85DLScXZEM367UzJsOg8qkOuDUwi3dYFMfSdgqehVKUqhyUeXDgXY8HB7-2SVD3NRdKqDsKbmwxR8F1ZeixIuuYn7AQuGNfm19M9D7xiFWicwVJej_FGRxLNMLzlaY-8Wc-m-NoLpezjsDK8vPQseXS9odS2AqHBeRnjOt_zJa74a0dmf2CgFTUBKJD_Q2hsfitaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=Jh6w0LwKe94vlc3tMewy-dsHKBT-ZtNeYSFf6iyr4M3D7v1AUnomg4aPNMAcVnS63QbCYRfy83qJ0_dh3OtrKUgZqvXECUnad52UU5QyZP4ZjItoHpRQwDdSrHIURNHIV9AdP-egX2n0wNYuu7UDpvvZx3DX1vR0wgJfymMzif6vsj6T8OZJ6GrbZbbDxH_GJiP3q983vcSFWo1DSwyFTlkdL5AdWPRaAYTBUZND8l02deaNx9ZlMcNZOxoVrg-FI7Rk9FTBFGCxeY2sOQ2RBK3DkBEWYUHMDh6tsFjZXm8KmRpo7xTO8sJ-dmFi7_xcXgakIKboihIrgvMQV6cYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=Jh6w0LwKe94vlc3tMewy-dsHKBT-ZtNeYSFf6iyr4M3D7v1AUnomg4aPNMAcVnS63QbCYRfy83qJ0_dh3OtrKUgZqvXECUnad52UU5QyZP4ZjItoHpRQwDdSrHIURNHIV9AdP-egX2n0wNYuu7UDpvvZx3DX1vR0wgJfymMzif6vsj6T8OZJ6GrbZbbDxH_GJiP3q983vcSFWo1DSwyFTlkdL5AdWPRaAYTBUZND8l02deaNx9ZlMcNZOxoVrg-FI7Rk9FTBFGCxeY2sOQ2RBK3DkBEWYUHMDh6tsFjZXm8KmRpo7xTO8sJ-dmFi7_xcXgakIKboihIrgvMQV6cYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPp5HCgDjBkzyf9U1As-XNc3ZvIMjh7WXyH_gk6I3AiBqoUcBk3iBng6_nvRP1W7s1StPbqz3S8ImaStrT-ABUymPigKDUIKL7qMMX07WL_BqfaXXvVZ6XRpi-oMlku1G2PhIg4SZv1nr6EkCW9JmaUWs6ypdzs2HgqCMwkbKgQ1GlnyyckLl4X3Ylz9PEfvSNPSvkYHq8mlmPVn-DvWhV_MOlbGnyBBbRcKaq9LDzX7yGBZtvvpWb-4APLd5Ii2ruidmyKSWjCuuUeUNZxChAMPyQ-zCKWPRDLLcbQiDIZsi3SvP_vTNPTOJYl6_rwiPyCZsOufgI0pJkFd-Q3MRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZoTw3n-aDYS-WTreRhEeigPxgB64r_eyojY8wPWixGHw9vkpWWxS81yZscs_1e7K72Ms35PBc3hToozQIDNS_QqrYeqEkBNr8c-uvhhmIqhJB3d_Sc4e7DXnpFORnE__L8JCXC0ADtSDPJl65qiQ_Fe_I0xi0OatXlAhgTS5oesOX4YVmov97Qk9oihcTfhNeq42uG3P8KjTKIia_UNZ7GxOUCvBO-AgQp4iLotsbnGfBebb1YMQY0F6G318JVcSgc4TlP0UKvp1k43NsXAgjRLlAa5lkfo3ZNXjAGAwJ9YepzUEAdnaiIsq9iJjg4tu8tUBWB2zms6oOrdBlSKbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rElCDZ6VVHNOXfTP5noCZITwu6EOqKqBVsOer6nTp_mrq6kbk_a3qUihgb_w1e5UUCIC_b5F_-Zlc67ebzlVBComLs3QPihkIdQqMiA0W3A2D-mXr24CWvFkTWtqd-6_CTBx1UUnga-iCUjVMRMVl0ov-LLow9EZa99-eBqo2_PVo0M9uFZpsTX06G4LgQDyiPJ-1gJWbtU7LxEtmfCuUXJ7LgtBJgkFELqGXkEbNvTzeWQgIfaKA8O1H1TAu6-ev2sU9xTPK3WzURoXko_epy1OPAqcMLd6BT7xmbSbe2gxzqBL_MVhbaYsELmV9pB4TZ9B839CbGfVGh0nQljr2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCGgpJGyvK3RgzsZX6k9UTYqIuWgHb6D5CueHf18saukSN-0jSpeD2eoqwFq5ehc30nKE-Df14afdkoX1UJOEyTgxyUWoe91uMVdoCPjLJOeZGHOL6pSAb_NRnAMOE8eXXWA5mj4PVdPJcytsKQiFohluU1HIQs5SbG1H73Uyr6P4nUa4YJCLqIED7D6tif446yJHCHnKJSJXLGxiBDRtXqN4sV8Gl5SC_nI-B8oGIky5krbD1OwMMJerKZghOu8dbtLmtbdxOY1V1K7ccFMt3VLpvD4UcdAlKjnwZ8lvYrfSKt-KLk77BNZQ0nCtBirA5oABtnDf5XFufmxyS-ipg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=SvaqSLYyb_4f_VA6os8cGcdyRC20gLDdB_UZHglpx6toGcnZtkc8eZq-15wSLElXnrUEh5ebZmgO0BSGE_7RJdaE7V2UbiAqldlxTqphnWr71UbHtSFNUW1cnxCdHurFsz2obwhsaQSg3cJ7CJusjPekTHEXUmowzV7fUKCKMcINdty24GaS7IOJtdUJthoHwW8XWmjMzMvfKoQBhJRgdzm-UWXJPARNcefRDDHK_GhyZTgxj4ziWDoqKmsvDM5qRe6yXiwrgS89Wcn6rLcoqWvwaErqalyMu0cxQ71bJjih-Z-t2WWvjIrwtegbPOGco1M92K3cDUoBguiVuvwhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=SvaqSLYyb_4f_VA6os8cGcdyRC20gLDdB_UZHglpx6toGcnZtkc8eZq-15wSLElXnrUEh5ebZmgO0BSGE_7RJdaE7V2UbiAqldlxTqphnWr71UbHtSFNUW1cnxCdHurFsz2obwhsaQSg3cJ7CJusjPekTHEXUmowzV7fUKCKMcINdty24GaS7IOJtdUJthoHwW8XWmjMzMvfKoQBhJRgdzm-UWXJPARNcefRDDHK_GhyZTgxj4ziWDoqKmsvDM5qRe6yXiwrgS89Wcn6rLcoqWvwaErqalyMu0cxQ71bJjih-Z-t2WWvjIrwtegbPOGco1M92K3cDUoBguiVuvwhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGDYb0XNTbJhpQKikmXL2s0paIaXVvz_EkJ9Wb1aRfriM5Sc-4RE0vjbxV9LiU5oiB03rFSXK8Af14kl_-hFwOdwVsFt2x7XVlXGh9nTyOaxoDLYxxt3PVS3xyZRwZwsoI01PVQjXhmR8Rvyl6AfZ9MCFOMtPiIgZ8jZIhjVxyCFzi_ZKVzm9vq9zoKVBpmUyQ4s3FQXIYFBiGng4TCLdEZRH97FSGEeVoXUYnFZrAMJ2V9aW0HGuCy1nbeFRAZxnmAroL_YoEwtJvy4h5hjSt22LdvW6zsxf9TYo8TT3Ql0sb42FuZjISm__YzhAmb_twVgYHuIIeL0L8wW0L5F4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Acsstkpgtc0-oMedff0ztCdtNq4rkJ2jzC2JgZ9hXIq-p9zn-f9ZVixcBCUdvfJ01Jo4FB-r1MRNbh_aZAoF7I6RgZ63e8qZqv7oqT3cB-qP9PPiChdB0Yz-_t06OxJURWEkQOaoFyP5h7fMyR2urvRla3T7ESdZAQfNrNv_0aaoV3bMq_6HCovFQFpXB1Ek6Cy5GSkhJd-7CYN6B_V3SBQDVMAIHsMJL1amKUZ-4-sCgXKNGpgM7NGktKzsqf8HF6sPcnZveWKWzVhYyik0eZ4eTnbZbZf3lQHXM5B-jXoW90Jb8WYWQ_XYIWnN7hFjlM_Ghl1kz-qcztZFoVscNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o60AmXDL1AbcZ6v2zytxShyPkkPMhXE0wuK6kOnAaCDmwi7QkqpZj4ncsVklo9B1ps_SwYdp2eOGVwKToGwTQ1eD-XzFsNmnPFKb6XsdR02a3CnkfQifmGvJ9UlXgwo--ORdmxXOAqudVKnuGRkpIZxQIsBc2Yq2BxPn5wzExiVrS9jmE9ftB2VpEN6tUFoMvY40UagcFpd34WBF2cgmTgw1zH_uNk7--FaRzOR4UG47Foyktqqo-DAGdanOw01fFFaujTgXGZ-lB8CRVoepNva0M8UQk_T3VKBX2k2Spsz_xLYD3rqitO8hFmb1o6LZcpALSAE9TvsuqEL2rhmAPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxCyxRAvkxBWrMjJOlO4DRKkC1G_ayn-O9M9Th9QRZJBejv6mfJf0HxHQNPtoUo6K2DjYpUxuZysXZOwrukKoHWt6kdB9Qt6HwD75IS-NgRjSuvrq3opD9MejOjsrv41kvYXYLhX9D4JEOqCGv70DnUzPW812UCeJzWmE6gmi9nWebnQO11KlLjyXbx2EiWOk_FgZ2RbP3cAl8AWoxnNdzC5y4HC2wJmiNLpxkTD5QfdRVFf3PraL-pKts4eUHPbVGHUgh7lBf5CtaFER8kDGA_BAWkmdzswsSBImERy4q13fKnJg7Ljhjk8CyhicAEnEga8ENvdXf4MYHkZYjrq7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFqs2d8jTM_eWiya9_Zv9W5wAKqWZTWYasG2shyNmkpSsYrBO9RDRp-KY9zz8bVoYz1EvgOuqn4ftfztjXhDvOCzeu7kJ-OXle-U7XloOHTJl8XALAQzbSEAKnchIKsyy0JUPV7wKOKF561h4QFjBCRMToUNMeRlug6W6IZ3hDc-WJtGMB6FN8zNRPm2PeiHS-eTp1N98Xuu6dorpv_Bkia94umxBmvNwrxkIJAOLkiXOqoMr8vvYY-t5m8uHriGXuCxX_AxYOcr7TDZrB2tRsuoWtLAtpn3wwnqU-oeIA87ZkEJhqulX-FiGSfyoPUWxW4nUr7o8dcoXqPILCWqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-jM9qxHHcEchl58NAyuUEYqLK0YShd4krKgxcllIuoA5R7T-9ykTzTOlTzCRsntpmpGHDtbEPO42PAM0SjRJmdsgsfe-DafRQiCR3OHR6tjpq0-qMJqTwwLd6bxr75D5_O3x3DcWv5rmucnPLFWRVQ3QMJn3vl6Xq1caFQs-ny3XVW-xObiAlidrARaiwlqSZ0fUs0fyY8KX0bK1tzgJvV2K4Qp_A-0VQY-7wvvvCwqPDgf7TIjey5M3_3kjj1JwT5C9dvv97Na6h6TGgzD-0a-EWaypiw-x4mueFA58URkPKo_biSv5l4Cmm1EDuPN7T7OGjMNyoS1g2eXIBE1Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=lxonc1XD_e0SUErMqF80ID7Chv8TzOTkzMu0zZjECijL3iXHAHbcJCalDX1u01CyJ-O_ILzQ5w9VQTVLrXwiNQ7Rd14YG08krY2wzYxfjIX9LazK0rrOKI6n34cNf99vvb161vR19JWIrN_-kGvDSg5aNjAi3n52p00ShR48zNJLMIus0Ztt-OVaGIBbOdN-vrGHeI5wsC_dn1vqChQgxjV0bTuIuBQaaIlcCzjQz8Xvqt7Acq3tHm3b0ErSNycZXeBKIXjobSswkgqystdVsVSGusfxGayt-thQ_nGAAxhClBZhSbjDzkkmVIbC5fYJ6N9ypRZnwUxscqaNwLu4PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=lxonc1XD_e0SUErMqF80ID7Chv8TzOTkzMu0zZjECijL3iXHAHbcJCalDX1u01CyJ-O_ILzQ5w9VQTVLrXwiNQ7Rd14YG08krY2wzYxfjIX9LazK0rrOKI6n34cNf99vvb161vR19JWIrN_-kGvDSg5aNjAi3n52p00ShR48zNJLMIus0Ztt-OVaGIBbOdN-vrGHeI5wsC_dn1vqChQgxjV0bTuIuBQaaIlcCzjQz8Xvqt7Acq3tHm3b0ErSNycZXeBKIXjobSswkgqystdVsVSGusfxGayt-thQ_nGAAxhClBZhSbjDzkkmVIbC5fYJ6N9ypRZnwUxscqaNwLu4PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egC41mhi9cjvZYIffxuaoXwXTyeBVie2YRYqLfBytHzPypXduwG6JO_8sa_qYmaod1CH5JnPmhqcNAhqe9Du6U8ZkYoBGa26fzPIxeD7Fe3LF47RM7lZ2XAleU9-8b_JyGY7M-QVl6Stpr0HPGVoYN-I5QDcpSqbZxi5_0G8Z4E8kKCDoCgRfJYjMrRnRtC0czGmzrjpRIoXwG5vTrHqPzfmj3lGDPKYuZZv0g9HRyqzBbQLpLCkYJsO0IdgMdqL-bj93WHayfImz-TscQ-HK71eioHZdBmRuV8vBKlGx8XHGJgO-xm5_Zbafaze87-ZeggFCcshIrDWU6puv54pdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImtUGhFeeGyYJDdUb4nC6clfAR8VW16L8PTXGgJOSDMJ4AYlBvx09td4H01woY5xRjOjDo8_B_dApf_WdnMYKPgKmviWZ1Z2XPDgEHOdoZeRDPPjDovRgsHYJZ_ibN5SnnBZGgLWo17I4v4_ZymHnkDHviFaMCeJNii7mrwM48PN26D6MhVKd2Rn11oz_PgskfU-3IhupjHe4JaG0rl0uqSV9zaY8ALmECq--iwn74f6xUXZgPWJrAMaN-TE-echrHYqdSA99IHwJSiSvs4Y9w5QkzegRVedY4_PIgA2uaSolbYa5hV-ny0SI4hvs5vNvbU2oPFYXE0qSw4ZwAvoTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr1K-wC9fvb0EcFRdnPV4cJMq2RSTVbvP33bgpG40MjizWmPQ27DIm4BoDiXvkMRs9Q--AOHVVpxvTW3nmiLXEyRCeeLPMkrj-6s6VBnBt21vRlz3RfxoYh3_j575gCMjl6TZguK7oODZepXVVCeNnPAVzMWlIhMpne0iWjGdmmW-D9IzSjziKASib28vPpxEv99NIN5RnPAv5B4N3icJtg9jBoP_-_MkGD9lkmn5BcGYAfMkKqSEwhNPsBPrJQF-WRE-i_8qt4F2kkTR4gv_36klwcm3YwxMk_AaMMTXyh_CdIeoJrW7dKHAH3CwObGspxEq5jD3Y5rGLtkfnu20g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrQCBq_E42snvTIMYOw3hIIGbmDc9pmI6podCXHtz4xUJcfuHF3uEfdU8xqKi5v6NT39TrgNlXDRRJuuv1xYbcGIs8FyxHtUG2Iyryxrtd7x2Zt50CgWVZhPQL609dSzWPuUqAC_ezDQA54wZ8keJr1piuJLNMGKxzXOZCxfsuIcBTf4Lavk-bQfXPUzA4rTcleXcDctMDIDhbeQ5qcDA6pZBbl4PHihtZx85dlqjQV-VSwN7JvE6Ngqm2_7hiQHf4ujozeXdzHrfpvyp0a_jJIh-RQg8B9BLOjsX7yESWCYnP4r0_ypSw-oOWLI7nqcv5TFyqbPZRTO-5b8iCSE-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=mZFhgg53SK3BY4y1SNu3dDjZO6x4GVL0NqGWpiweQMJG31cea7TmzCyWgxYW1Z7i7mchzXK0Rzg1M0w5xGy2n8KvAok1emDYuW1YaSiSupA5uH6vPGYMmmXAuq90gX3lPuMaVwFTExwEXs5hIV1EzVp-E9mygOq_HLXobfYxyzyl7TFu1-BvUM0UKG7Is8jXbVgwRkg8nOnrs_MR2u9QhsQvUAoi0w-UR7sHjtDcZ2ecioFmP7SKWT7-qpAZalYCwrxl7IDFuWICaeemcFr3MYNVTbqFMyDavn44swYMvCDwyuUygOwfUQKZHunI4Dgyx1xbA47cvzvhALOeMNTSaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=mZFhgg53SK3BY4y1SNu3dDjZO6x4GVL0NqGWpiweQMJG31cea7TmzCyWgxYW1Z7i7mchzXK0Rzg1M0w5xGy2n8KvAok1emDYuW1YaSiSupA5uH6vPGYMmmXAuq90gX3lPuMaVwFTExwEXs5hIV1EzVp-E9mygOq_HLXobfYxyzyl7TFu1-BvUM0UKG7Is8jXbVgwRkg8nOnrs_MR2u9QhsQvUAoi0w-UR7sHjtDcZ2ecioFmP7SKWT7-qpAZalYCwrxl7IDFuWICaeemcFr3MYNVTbqFMyDavn44swYMvCDwyuUygOwfUQKZHunI4Dgyx1xbA47cvzvhALOeMNTSaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5G4kjp_t1pOx5zpexZl6vJFRg4o7El4i_z6-iZDpcvk9moG_Fdfp2gRP7DwTzP5-N-Qf4-DOHookUpxIr21O6zawyeqVoYcU-bQB303wfZjaYO7_KqhXHfaldHncYn8IPZhJN2fHlzGersnz6NAxzcXCp5qkn0X99vV_6abw6gcAMHjGtTtfunIPsg6xsoXHzHT8EjGyQsNhOqwYQECrQTIaJVn8z-iuTA0QpTtS8hp8ibFr7kBZboMru13hvBKZ333D8uuYC9_vMfUHyqxMscV3yw8HxHmUK9WK9ywXwJmMExwRzloVmtcri2uXPd1tNzwAFGnWumNKyQxbq6btQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMdgRz0zdKnlYWqt1CdgEwLLQRvHSt0q3J3by-Ey1HINMms2z9HPIo_MehofkO_SOeuXj8xynbt0ztEAV57Uo_tw15fJnkmSTbYzQSxBuuEnduwDUEJyEEpwHcI1894bEoBovxqTNcsm_RhshtHqO61wxS75114sH-QeYuVgk0JSyq1NT7WwMr_QFL2kmc-tJLci_RDTuSF95_EsWSMP2hWAzBWpkihZ-O7tfPht-YzYwYbkd1hjpFi3pEL0Z_aIAuX6EnliU1GXNCVg_fdPFTQaetFBuhh3jox1V8UndQqNQY9FFoaV6vFQM7SSOg52cH6shQP_8_7pTDcgKC1a6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJftJTTjnGZ-eBJnntfi6rmZc0j3cAAVWETWMrptMtT8njOIGpI3afKMA8d3FscqWNndbaROJpgAf8627JYc1c1NrE7XHeV41K0Qp9MeSK7yCDIDMsooWvQjvbWzXbEcXxhG84AUr79_C2HvRtRWjKgZ6t4kDwSXRpcnV7vVVJ1QOQcrBI-jOLXo_SoHDc9QeMYGoBUSO8_9VsQapwpgY0ZLG5TR_RtiVQ3k-xNc4tqOwCiuhsPKDPRosivMC_nfdNe7EwP2Kwh3oUV1BRESUE0HdlDWQUIDtyitgWQoZt31enNtuXMdadfu3iLB2VWoXuJOKH1UE-U5v8BaZDYXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6mOuC6A_Zn2LnEXAfvc0tn9SBMAkDOHWYeVWV6lWJB4DO9HbdojkeBi96kkomRjctAdfRlBaX4rU_UwUE7hTWP8WiM7MGzrqlFuP3H4bANdXXUnAtlMAlqXC7AxVih4Ekbj6gAZTkb8MxHDt5hZbfM7gS2c6gn6akjy72AfaIVWH86qzd1orcLWpAiz50H9ytmRh2AjAdgWlLvUQSHAFvVMQJPzzl2A7HcLDC_VXpafOCSknFM2ASNGnAnDOCpiuUSN5w_KbfdKK8JmmNVmViwBtbRSSVsY7JYE0cL4IRJ6m2A9BOS4O7B7Im2jqzWwR_V7iQ92bLyuPcVdRhfJNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=CftYoABHhmRH86eVVBM97x99t22P4_mdu-2oOhOcw51H1kdlQro3KybyOjTzFTbYfCro6OWE6ttjPh_qlIwR69KeT0rl8aLFiOze9Z-J8GcRRXlQQFm0-kmSWfMrIJDDmaLvjPCMrjFEH4NrqiJqEK_IUVNMiZIoKSuoZ9FkWmRlSJUkXLrWAawXj8oeYxqF5AW1nDFRYCVVekKWTvmUF_H2IaH0Lb0oxWU3PuyPM9NtkrCMYW1Q6koopXlYtiIN6ChF19mZoOeJ27mj_acpdsfGO6WRiHgEtFEmt3Tr3LB0RQVnSjg1UuXwrrOirJmArOogDyjR5beINZU2aXiKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=CftYoABHhmRH86eVVBM97x99t22P4_mdu-2oOhOcw51H1kdlQro3KybyOjTzFTbYfCro6OWE6ttjPh_qlIwR69KeT0rl8aLFiOze9Z-J8GcRRXlQQFm0-kmSWfMrIJDDmaLvjPCMrjFEH4NrqiJqEK_IUVNMiZIoKSuoZ9FkWmRlSJUkXLrWAawXj8oeYxqF5AW1nDFRYCVVekKWTvmUF_H2IaH0Lb0oxWU3PuyPM9NtkrCMYW1Q6koopXlYtiIN6ChF19mZoOeJ27mj_acpdsfGO6WRiHgEtFEmt3Tr3LB0RQVnSjg1UuXwrrOirJmArOogDyjR5beINZU2aXiKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
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
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=m6EmN-fZ8uZljT6Cf_2XhwKQgr3kJ0QAuDQdJOohJMHRynU3val1Dzga8KY1TxQSKXNu9VorErfuk6zAa_eFEx164g6fFKikxpEGBzAgOv2VUcSaC-2NOoNyskYFXsTqF9RCN9SSAKiDaupTmi2sm9Pou_w9HbnkDasRc-OD1OJ3u0CPIMpkFBuvy9aeDVBag-rtsSkUlvH9FPPDzLe0hAQIwZ5ClZl0LAZwcmPoGZhnRyInnnBTDwnw6-3NA3d3RwGt6fczO9dIiIunK1SSzaqFpKiP-4lLjkmkQWMkyNhL-9AUljhi9CxXbx4XHHeskcB-1WUfMidSlc0vLxhw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=m6EmN-fZ8uZljT6Cf_2XhwKQgr3kJ0QAuDQdJOohJMHRynU3val1Dzga8KY1TxQSKXNu9VorErfuk6zAa_eFEx164g6fFKikxpEGBzAgOv2VUcSaC-2NOoNyskYFXsTqF9RCN9SSAKiDaupTmi2sm9Pou_w9HbnkDasRc-OD1OJ3u0CPIMpkFBuvy9aeDVBag-rtsSkUlvH9FPPDzLe0hAQIwZ5ClZl0LAZwcmPoGZhnRyInnnBTDwnw6-3NA3d3RwGt6fczO9dIiIunK1SSzaqFpKiP-4lLjkmkQWMkyNhL-9AUljhi9CxXbx4XHHeskcB-1WUfMidSlc0vLxhw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
