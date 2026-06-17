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
<img src="https://cdn4.telesco.pe/file/pn0vruaEyfIA68a2ZBP9wnGvQOM0epBM1Tzq9oEmCuH84wQY8E2ecqg4g0NddHtiSLW8H_Z_FxUtutkZCwziGAY7l5sJIen_pCyTL5y8ilVevi0pCQqdjV2e6C-xHETrx3I6zRG5-aYZqfV1ozSUvNoPIweG2Fn8Ax4zFc-dmAJv2HLsr006VPrCfT1wprVl3884yzle_f2qt5_y5KXCVAy5jBEVCeVyoAOGkBGpB2KJ0RTvEAYIiKa8rR_-qFBrRTmSKJXK_tXe0qSk_lAGpwBlW3gvpkzYOlW9n6gYoKst8pSY5SQ4tWSxkvC0zcOk6oAmeCPmqh-GwyMWjuofiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.68K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🧠
AI OS جدید روی لینوکس
👇
یه سیستم‌عامل ساختن که بهش میگی چی کار کنه، خودش واقعاً انجام میده
🤖
🔒
HAL (امنیت):
• کار ساده → خودکار
• کار حساس → تایید می‌خواد
• سیستم → بدون اجازه دست نمی‌زنه
📁
دیتاها لوکال می‌مونه + حتی آفلاین هم کار می‌کنه
خلاصه
👇
دیگه چت‌بات نیست… یه OS هست که کار می‌کنه
🔥
🔗
Github
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 461 · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚡️
Gemini
داره می‌ره سمت ساخت ویدیو با چهره خودت!
یعنی یه عکس از خودت می‌دی و بعدش می‌تونه ویدیوهایی بسازه که انگار خودت داخلش هستی.
فعلاً این قابلیت دست یه سری تسترهاست، ولی اگه عمومی بشه، تولید ویدیو با AI یه سطح جدید می‌ره
🚀
#AI
#Gemini
#Tech
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTONbeFL16j2UpzbPgk5xz_cEHoWcGzA6PYiiYrk7ZPLlp0NG-Bu425NZa9m41c7BrPSvkjhXVMPjJYW80AW7pmUQf5mBN1_7XPkAbs-qt9YHgKkzzQkkPfIBjIerrbdQVHlMmNFWgtwfQCd1Hiahvu-BB7ms9mALR3_nDXxRLjvGsbFM_AOdrDPg5u1spuN38FlYxVOrLde57HfADTdNlwgGS3M_uekkgYdTnbdygL3QFGOPfvyQdr5U3QzTPx4Kip6RcR1ptO1rW4iJVBlT8pitUqA4XkNmBSa6-qNLOOORX_Kg645b84NrPmB1dLAsCXHzQWFxye1XHlwWI5LoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
اجرای macOS روی کامپیوتر معمولی بدون راهنماهای پیچیده و تنظیمات دستی — علاقه‌مندان اسکریپتی ساخته‌اند که نصب سیستم را خودکار می‌کند.
🔹
نسخه‌های macOS از High Sierra تا Sequoia را پشتیبانی می‌کند.
🔹
روی پردازنده‌های Intel و AMD کار می‌کند.
🔹
به‌صورت خودکار ماشین مجازی را ایجاد و تنظیم می‌کند.
🔹
کمک می‌کند محیطی برای Xcode، Logic Pro، Final Cut Pro و نرم‌افزارهای دیگر اپل به سرعت راه‌اندازی شود.
🔹
به‌طور منظم به‌روزرسانی و پشتیبانی می‌شود.
▶️
دستور نصب:
/bin/bash -c "$(curl -fsSL https://install.osx-proxmox.com)"
GitHub
#OpenSource
#macOS
#Proxmox
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌐
DigitalPlat FreeDomain
راهی برای گرفتن دامنه رایگان
این
پروژه به شما اجازه می‌دهد بدون هزینه، برای سایت یا پروژه‌تان دامنه بگیرید و سریع راه‌اندازی کنید.
✨
🔹
دامنه‌های رایگان فعلی:
• .DPDNS.ORG
• .US.KG
• .QZZ.IO
• .XX.KG
• .QD.JE
📊
طبق اعلام پروژه، تا الان بیش از ۵۰۰ هزار دامنه ثبت شده و مدیریت همه‌چیز از طریق داشبورد آنلاین انجام می‌شود.
🔗
ثبت دامنه و راهنما
#Domain
#FreeDomain
#Web
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">ایپی 188.114.97.6، تنها ip واقعا تمیز کلودفلرِ ایرانسل دوباره باز شده، بقیه ip ها رو alpn-1.1 (وبسوکت) محدودیت شدید آپلود دارند، در نتیجه پنل های bpb و ... رو اونها قابل استفاده نیست و فقط XHTTP رو سایر ip ها قابل استفاده است.
///
ولی علاوه بر
188.114.97.6
که مستقیم بدون نیاز به چیزی وصل میشه، رو بعضی ip ها مثل
104.17.121.43
نیز فرگمنت باعث میشه که محدودیت آپلود برداشته بشه و اون ip قابل استفاده باشه، تنظیمات زیادی برای فرگمنت کار میکنه به طور مثال در حال حاضر میتونید از:
"ip": "104.17.121.43",
///
"packets": "tlshello",
"length": "1",
"interval": "0"
استفاده کنید.
///
تمام مطالب بالا راجع به ایرانسل (و بعضی نت های دیگر در برخی مناطق) میباشد، و رو بیشتر نت های دیگر محدودیتی وجود ندارد و اکثر ip های کلودفلر به طور مستقیم قابل استفاده اند.</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsnxRz2AX0gBVCho2pAy_RsLCCMpMDVSDUK3197RJPjCvNrCj7Ubq9WOWdh1r1RXDDMda2E826zlHf2_2ZU3nSJe8JM_hsAw7K0FKL8k21L3qVsw94YB1pGw1FCmW4BAOtFWHE_3Xt8Dfkqh40DhRVJAUL3OxfAosybjliPPRgj9tWDKKM7mw8vixHwOmTChlvElts_A9ZdHskjJHilvhKqGSaMjKvgmt0Kpl20d6-l_Pt0U_nJoqwzM2trKz_i6iPhurNzqcG2tKm_nX0OIB3QRAZE3izvIPiKr3G2qfMEHVJ1N1GuMw9ejsrnqIVy2y2DS4HC01i8Wko1ABt9miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
برنامه Sandboxie؛ اجرای امن برنامه‌ها در محیط ایزوله ویندوز
اگر می‌خواهید نرم‌افزارهای ناشناس، فایل‌های مشکوک یا مرورگر خود را بدون دسترسی مستقیم به سیستم اصلی اجرا کنید، Sandboxie یکی از قدیمی‌ترین و قدرتمندترین ابزارهای Sandbox برای ویندوز است.
✨
امکانات مهم:
🔹
اجرای برنامه‌ها در محیط کاملاً ایزوله
🔹
جلوگیری از تغییر دائمی فایل‌ها و رجیستری ویندوز
🔹
ساخت تعداد نامحدود Sandbox
🔹
فایروال اختصاصی برای هر Sandbox
🔹
محدودسازی دسترسی به اینترنت، کلیپ‌بورد و فایل‌های سیستم
🔹
محافظت در برابر اسکرین‌شات و نشت اطلاعات
🔹
پشتیبانی از مرور امن وب و تست فایل‌های ناشناس
🔹
متن‌باز و رایگان
برنامه Sandboxie از سال ۲۰۰۴ توسعه داده می‌شود و امروزه به‌عنوان یکی از محبوب‌ترین ابزارهای امنیتی ویندوز برای تحلیل فایل‌ها، تست نرم‌افزارها و افزایش حریم خصوصی شناخته می‌شود.
🔗
Github
#Windows
#CyberSecurity
#Sandboxie
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNnhWDsEMi1q4xgBES8k4s6Zt73JUI4HG8L44QWL6m7wKm9qtW30oyPT0c2tmM64EAi_Qu-9paWZKGn8kxvoV8HcxQu18C_ZGRN3RZkOTs6CeJJplBwppGT-cMWSVGNnkR4z6wrNGp0KH8-M4NTP9DtPyan2CEsQnpOCNj4O5JJ-5srmRxOk2MR2byInMvUWIAp_apj0xZdbmj1ZLHQrMpZpuCKDb34XeErd-cq1KC7YNsXUGtXb4129J2J61J8UvbgulB-KESjwA876HPc2C3SOe86ATqvXup3wCb76F9PQYsUTp4115lIdgBF9lcU9EdmIGmGNle7QUqwIb9xDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏬
دانلود ویدیو، موسیقی و پلی‌لیست‌ها بدون تبلیغات، اشتراک‌ها و مبدل‌های آنلاین مشکوک
یک رابط کاربری مناسب برای ابزار افسانه‌ای yt-dlp پیدا کردیم
🔥
قابلیت‌ها:
🔹
دانلود ویدیو از بیش از ۱۰۰۰ پلتفرم محبوب.
🔹
پشتیبانی از کیفیت تا 8K و صدای بدون افت کیفیت.
🔹
قابلیت دانلود کل پلی‌لیست‌ها، کانال‌ها و زیرنویس‌ها.
🔹
امکان قرار دادن ده‌ها فایل در صف دانلود.
🔹
به‌صورت خودکار مرتب‌سازی و تغییر نام دانلودها بر اساس قالب‌ها.
🔹
اجرای محلی روی کامپیوتر شما.
🔹
پشتیبانی از ویندوز، لینوکس و مک‌اواس.
GitHub
#OpenSource
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuTwgBaAoA2Xxq6MoeTnpIwOy2LzeJJsBxmPYGfajDlb8jHn1kSi0ieDQkQ9Wm7Lwx5E5n6dhFwV7UbISESpSBwi3MPanlyFcvYVMjFbigdgfu07JzIi_zDbBYupcojhWcknhmRw0grDy2fw7r8ZxV7N3BUh0mLnZF5KMCT3e7b-Jh46qZxMZZINeWh-hJyn2CS_08UBBM4QBNKRY06XFuIsFhOsvQYPZbISq0RfnuZJ5QlaFUAn0LKw-0Qec_3dbdasZj4LsZffyce1Frt2_OMzFpmmqYlPDOH8WfxkzJtHgDL30ms_dHQhRqzYhjUZ9Fmo3Kk1WE5u3fSmGHDD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت api رایگان- GPT5.5
لینک 10 دلاری
ثبت نام بدون لینک، اعتبار نمیده و با صفر شروع میشه
وریفای کردن هم با تلگرام انجام بدین که تایید بشه براتون
با شماره مجازی نمیشه(چین)
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/johrmn2e53lrUSZ4zE-P3wmdwl_5vV7p116vCJerY3O9Bd1neeJQ4O_uvCZK28ttK5k6ps44rvxAiKRe8qlI3JQ4O39POC7P77h6-6LTNPB_W14ScbJA1rvXuPdJb2eB_4qMjQ9qyYKfn1MJPcjoVAejCC1WaoNHJLJg_J5CWZSvaD6QN9D_msRqnyyIoO2ZdD9maIBseKwJQPHyd1Vrvw9_Viu0egQSqJpwjV_tCmN8rbLNiU49SuHHavs40U3J6zHeH2-e0077jEJ_1a3CDLSI2crsSVQI-_OTb--5RwV9OHGpBr08NPJQr_O9hV3XcwhVqW6cdemv0ets8O1CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل Cursor در حال توسعه یک مدل جدید با 1.5 تریلیون پارامتر است!
⚡️
نکات مهم:
🔹
از صفر آموزش داده شده و نسخه ارتقایافته مدل‌های قبلی نیست.
🔹
گفته می‌شود برای آموزش آن از حدود 100 هزار کارت گرافیک H100 استفاده شده.
🔹
علاوه بر کدنویسی، از Agentهای هوش مصنوعی برای مستندسازی و مدیریت تسک‌ها پشتیبانی می‌کند.
📅
طبق گزارش‌ها، این مدل طی چند هفته آینده معرفی خواهد شد.
#Cursor
#AI
#Coding
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk2AJPwTGxEQJDYcH8uqXkEU3wpG8Vi95YjOaS-GBhFKJK3G4bIzLlrZnGvCfvM5I1dnfDKGQinQmJyo6uoeg5JMkr9jhuC3qA0at1pFzeC7EhREehIjd4J6xMSLctwo5R8bJpEAUSjlqzwN-_-W0ncWcVOUVSdCv5MhaD2m8az8msOcskyrahcJAPwVSJkTjNJKW2hznra_1AToBdgyWjZjti3UxOsVnYeaCvaXIDSlozqs44K6iKRiLODPsh8PBTOGg_jnIcgPDLvsvkvtF-ZL5YPrVJUDLNOCz4WYODPC0JdX_lVzQGDJAtoQRisGbnvjNUkUXZlJckeCV4RULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbN9la-UGIgtVCrncQMWT9-qsege14MbXXiwqUqRPTxhcHVycczaey0RPSB1tiifrcF2nqoqg3GpQ9sdDr_nHZSJudqnydpk6_XX3tFHh6tXqVWE2_aNLhQdXcb3NdHz5SlqxbIA394H93u_tgwsJoyc2pJvqAA-lMQrKRL_mgV1vnuUI837cHqcp4s7EsugRMqbRcEU9vmVEvYph30WFw1obd4FLDUyuo8M6yr-xDXyr_Arlia458nPEuMUgenXbZeSAjNujEkX5QnmdcDeQb-RGsmitfj1KA6OxpFHgVkjwvT4K2rA_rILFuEDAYO6_S4fNcbZNWA1IYJoqz2WYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGzGvZ1RLTS8s1_dg2U5_EL48UyQbpMXg759sgSx_L3Fa2CfBBSDKvWEH5cOtsy4hx66cGWJh3M1ipWmi09-qHGa4daoVw6eI1PiwT8ZLjXEkpwZSd2oUCGkecqEtqiZqFjWKkGLMP1NfflcuAxZ2yEEryjReiFsp_XFN7rTgWiIRi5Baw2cgyUFf4EI4Pyr7f8KBOkKVwkKEpSv9d0L6FN7_RVGxyR22EDLZdfwtEb0QrJeyUMyMnw0jn4z9zffGNh54Fxn9SCxypEx-lz0uMyjHer_GXKfGu1mR2WrIYzK3tSi3EQ4zbd7JL9-3FJ-hDdmXrpgs28IG34iz6w4oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل جدید GLM 5.2 از چین معرفی شد  توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWruPxt-lGjBk4JyRIJ1wAxDatq77i6SQZdB44K-cb4_NY3Bof6XqhTVmCFQDO2Rq8XfaQxeUJ2zykMcx8yNNZ4D9CqvHzFa-gVbGzqfUoMLHOHXw69_3cukkYrA0ddYy8_rk-EAj-1K_61DvxrqtF-TJWUX_fPiquqQ2FVqaXQsr4wUjSeZ6aCsXFj7i9vkVIwvJXplOA3fZL-N_jBSuiEvkNcx3wgIwEdsdsmr07huoxp1S7IXGSI5mX6Zhse7Ruc-VAZKScJQO2Ea4xla9w3ZBsSWrNF83LZ6phCuuU0HLzeygkd4v_ijDeFY4ZAmzOmo-4ZASi8wc21DJsxxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIsVeBL9ZU9_YvyFNQ8kF0humc0gPegb1Dfc5V0z06GfSefGMA-xCFKYY0SLHk9rv__yezHArjQifgJMVY_wVJGJtE-_3xXy5MjzfiVAaubLHySHZuwPPxyqqALPS3_W9dr6C4O7_1EAmVYFoOaedsr8K8a8LOiv8SDnL_frzrMah0XtgV0xJ_d5BL-BYfKbHjgHlqaVv0c2qUeF6E4GsubC53CJYcYIB6CMcSCHFoTnk4cWnfqYMxNGAJy86kuk45HIU72B7gCf7Ay8MdvK9qk5jJ2Mux-qZhiNL379Nkj1DwZQifuhqIBl8ttutldHPO_MU8UbXNP9QluOwdcOFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رقیب رایگان Suno پیدا شد
🔥
StableDAW
یک استودیوی هوش مصنوعی برای ساخت موسیقی روی کامپیوتر شماست
✨
قابلیت‌ها:
•
🔹
تولید موسیقی بدون نیاز به اشتراک
•
⚡
ساخت ترک با پرامپت متنی یا ملودی خوانده‌شده
•
🛠️
ویرایش دستی ترک‌ها با رابطی شبیه FL Studio
•
🎹
پشتیبانی از MIDI، سازها و استخراج نت‌ها
•
💻
اجرای محلی روی کامپیوتر با سرعت بالا
🔗
لینک
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao7MvVsAgnu1gmlzCk3_Pc0mS52vKTf46t8-Aal101ujdtDL6nMW4B_dVbqXQbdfI-BecaZVWtofQWVNTRytFyOxFOdoFq20_bilIBXOoZnQ68N-ui3UckzftuH6bTivDYump-Tm8oiUoIKeTOG8BQFFlY4X_gLixgYKNiWGZEFADOnwcFusJah8W-W9OKqHCf4NbLUl6wjefgcJtRlbQHMacsqAWwCIkJrXEExA42ZRNGebzqCrTzlKX7FHv7Uyb8ll49Ij8HNZij3KQNvOoL0iZxZuyBLExdTephqITQK1w7kc-KLH1xuJxtAVhZjyWpxrgUH2BY28JWjgxmqZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lw3_qm8n9tvPhhOHyzaEQU4EIZvM6NsBNosr6ITtkMOXHKmshcyRgwXWYZ2LRramH_hGR9UoCflQTJR4s3hi8ShGNuJJBtXo4EFHaluvwRMoPnymaryKmJcMUXZO09A79BhKl6VNfDFp_WZDPShtRtBIX_toBxpTADUu3qCjMn0YjdmWsvwFKwkKzJt_g-rbdkr7Pah722fHISZkII0TGy859D7UO2x3QKJGxnRL4VW2JmsRNOgGgHZjX0Ol0nehf0_d6QbLkEHgXcUE-xiXPt2TxZFzfG841x_7OBtf6q_hoqs8nEXcefKdPPin558l70rRWjHNWfaRqugb4atrug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npjCiXTmErzWr8f90tQNYfedPvmKsIX-ntmN9E2xxAMsye2OBVqvwAlNZkQd4kcGeEFrKKKtegN2yrYCOLdlVlfaHqF8EoZhp5Uek85yNzILR7r_vQzBjS1BULPwZaULOe8o2cieriV9Yh94YTjhSQeDaI0cdnQqkDsWPHSj5aPNcWf3COMtfO9MeygYqkBjQX0Q64ql1aX-4NUaLmxEMSfNeSom5nF7ivpWXfJNQ6jqa13PhfPO5fO-GJbP3wu3jtWUePVLs1dXLq0CJbf3Q3st6y2G_nTlBUFgi34FVIOSMPks0FC18u6IjJSXALHAnPHAveS6xOnh6ut6wLYRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRxymGKyL2y8hWXPU-rcfMDA0WCwLvYizHZ4nkzz_bJoRueKGfGNkNRjTTnVK1jvP4GZV00-mpuvZUL5wG1hcYDj4WnzHPT-VNJtFrtJBEMgGQeL8d4kkUpJ4J85UJXR-sMFm0OxmmqEgweIILp6PCHdS9u9LhtywZTtA_FrweGjPOEpmWWbJn80wIxq4PKib8bUvXW8dvWBW4WhMfB0ipxLKwwkrmwRtx0chS0oBEc7IukG4LjffA_tvzAcFDbwh8g6NZdNNBlMRhJbfUqVKJQqzqjzShvTAH4BoJZGFUT6k9Jv5EGeVKuKku2U1fxfwFiuBHNs9SRtg2ijQ52D6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=hGFD8P5bGQJsVTQ1x-XrlpljzDk2q8oqt22QVa5OxUu2IEAxZnY_UTOw3kexwKWL0WeC8m9_i-rLT9o0nbThMjuJ2ED444OHXSHZZ1MDqFY4pVlioILOci09eOl4EZk48lrSRS5wmqaBQoeXi3DEmy8eRmHA64lEJzR26nxDrMjD86B6krEJcHzoX1-CDjcQhD8hyt3Po7CX3ccN80km-w-CFb16V4EoZmjbRe8sC_MkJ1jVZu6YaAhq2vumhtemV_GaOi8woDM7Dmox6_xdcGsfx4gbQAgBc0_nMMtrcfQofrwVTdyC6pgPbm2sBR3zuTxEXpro73UqvS1Bar5vvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=hGFD8P5bGQJsVTQ1x-XrlpljzDk2q8oqt22QVa5OxUu2IEAxZnY_UTOw3kexwKWL0WeC8m9_i-rLT9o0nbThMjuJ2ED444OHXSHZZ1MDqFY4pVlioILOci09eOl4EZk48lrSRS5wmqaBQoeXi3DEmy8eRmHA64lEJzR26nxDrMjD86B6krEJcHzoX1-CDjcQhD8hyt3Po7CX3ccN80km-w-CFb16V4EoZmjbRe8sC_MkJ1jVZu6YaAhq2vumhtemV_GaOi8woDM7Dmox6_xdcGsfx4gbQAgBc0_nMMtrcfQofrwVTdyC6pgPbm2sBR3zuTxEXpro73UqvS1Bar5vvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjHlVjn-sw8cxTOxR171VV55Fcs6MKIgThmxh68tmht4JfVZcW94YrX-VdncHHREn2Np5K5DvsJrAAu5pJp5OIrRMES_yYpR1dHW3XRVdiSPYLV6r2Sn3R0yeGlZrk6485qz6LmG72sguZTl4nnpN0lLOQAwQWZ_OUpTpDTaYcWOySrlNAAg-OlbdUK6tLKzMEA0swWkuu8zrLv0BrAxB8nKsaR3lU3m2oKgNLdDC7u6eSgSpM-sIRPlpR5kBRZc5ishUBRmU9Dih3-3-qMekm9oNnZFZ7TMQambX5xjezGtgGAEAI1caLmFt4oeLfuDVkPchQISbpyrvpRm5xzLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a8vKMo1E2DwA6rdoVa52dV5Ac8LL5R3bDSAsEk6bnO8nxtIsnK5nRgUPsPFNhexInh1FxYMNkfFZfVvDrqXUOhF2DU8byqmDKWhgEk3UeAniqMZbG_rCReGje8oVGDq9WNGgsvahvo4MvoTvCCxoTsQLqk9jKAMAmI9T2pZOpuRVpYH2OCiGBZB4L1SrCqfBpr-iQGtXLRVZWYeWGB5kYXrUo9VaH49TUlo_MpSnoDoCaPH6TDHKT-pwDytOsRYtaJ1mk8KTUj5t01xWN-nNNptFfJVcyzmbUMOiYxkN9U-Z4fCyEQCm5JsOrAUeaqh4p_o3J9iRkivgvLsaGveYwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=a8vKMo1E2DwA6rdoVa52dV5Ac8LL5R3bDSAsEk6bnO8nxtIsnK5nRgUPsPFNhexInh1FxYMNkfFZfVvDrqXUOhF2DU8byqmDKWhgEk3UeAniqMZbG_rCReGje8oVGDq9WNGgsvahvo4MvoTvCCxoTsQLqk9jKAMAmI9T2pZOpuRVpYH2OCiGBZB4L1SrCqfBpr-iQGtXLRVZWYeWGB5kYXrUo9VaH49TUlo_MpSnoDoCaPH6TDHKT-pwDytOsRYtaJ1mk8KTUj5t01xWN-nNNptFfJVcyzmbUMOiYxkN9U-Z4fCyEQCm5JsOrAUeaqh4p_o3J9iRkivgvLsaGveYwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n58hIbHkDH0e858c8pdMtDweH8bUhSBXykLXXF3wL0ZmJogJGMR88idCAFYOxsQ9ucxkuIS3JpgkdU4belHJEQKRGX0ufQswK6_9TpIyLpw3HI81cuKJnddmKn9qHsW4RTGhweiPp3wE-3i0mhXmVgqjq6pOMKTY-1HB5iAE1jsHUr05XYQHMIhA_NRQbm56KMBWHOyvMvx24a_-i-i82zf-y9aTuiS0NCPSYAL8hTfNQ38uBt7f4Q7TRfaUmSmnZbtt5A2-sJz_moSVsQImnF6iwnRkieEFWaFEkHibxZSB60m7DQ2OdfWOElFmvAXaa5F9U-8lBKhqd9bC3oiJaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xfld0hlOEcwg4TrLQ1pg8urJzRfVS-L7OEjB28xzhcFmPrMik1QBgg-_76So7us-4rg8uipqLAdq_O3Xs-xc8OzEErL5ZUn5lGs27kDJasG-neGkT0aAOI5Tw_NKYV1t5mO9E6JosjJn9yhN-GlpnAwa0CCjFu0vXRCUsVCCQ-Mlf_QRF0dkoEfllgAY3w9JX9BNsJ4--8dxTlhOTY5UCTcPvn1E3RCIfbK2H9BWHi7HnZ4QOawWM8-27of41XPmnrbazJGFQyN1rYeDn_52tYfqigX74U9vvs48EeX2Q3cBtntqiI6DJm_V0zIFKpnY78emFqLU2Osjr_6ODijIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egz6Xb-uq5N7YoFgkxYfpryJvuwWeiOm_OL_S9dMoKMvkUXbxMjzi1FiAT-U766IBE7_Zd8Tqga-b0X_U5Vt6QdCLo1PVVa24QR7eGcO3FchoI3-7Pcp9-Dvq7fUS-eR5DwAKTfAeiMqWl3IPkYjcevX-tJhMgCPfxfzhXTRsZgNTGs00l_aFZxiJu3Pf_csIT6Htz36jIGZTSZa9iCSNtSafFzVnWu7__ym_ztgSL0e1F1UadZp-99QXJsfWgxl1OEtLb8LRvSkSs8uYi64OREFhPw2TthtE40Bx0KJwAJX0O_BpsacViv6vrZpxiwzcxbO6LaWnElH894Rfnx_2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL_NaohTSvEkDJaM2Ui9-AiUWyCglazag24lIn8OkZbgLX4-6JjdlSgYGZR0AahlW3ohwXqji8DD4_GyakHHqNbMcRTTOwBif11FNvijzDTl-V0JsG_mZRTKgbO_QmXlQMZAiACLiUcYqcPFssIP6QwV7DgMS_vSWM7kEIGn-79HDMXMAMpMzLuC9YOg3f9AtA63KKTwpU1ouLIb8no08Pu-SAQfFhULY_Oou7xiegghrnbDxOz3URFt7mxdwuKlwUgVlAKjmEyzJWStCZR0F1FAB2QiKC37Br_4C5_SxIlgvTJeJBSYZn2ffoySIrB-2OQC0xMmljS70yRBBvmJtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK9N5egviENSvo3Ys_FFvGjywgPeUV0zELw2MSYdn9HkBHrM6o9F7iO_fiaeUoGczbihXsIuSdjkXcWlxD1q78BRhmFKMAWgEFYRvYkKUL4ODUVOLeVWukPzYFMJ1Zj996r0fHhVbNSLaCpho-FTWioRqlouOeSEkhG79PLnxr9FP1GAADMeUgyn2Fr65AD7G803Ex2C65NExlw_BdxzR76491nb8wnKJVa5KGU2rBcfyikulaylEr8_6xPIjYbSXdDx_BaatCrk4h8dt1eSUlKNsyTqdWr3cXOkaGUP0AOWsHndHxMGmWZgot9TSeXl-EwuJ6Vv6Pu8_EHc-ylP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvxEBxpxtfV4hf6xADcuLEarN8wjOHITFzywRONnfmKGeOGGmtgjSKzaGR4ms_atrHFbP9mnj8e12u3XOAtyICjkDU5jeEMnzhS2Ezc9qedVgW_cEscTvH6Yeu-ULjabpklrDVbWf1jVa20jz367tK0Mx_VtvL1tnRTjyesmv74YrILYzvgxit7snns_EDu2KTX86GjEZuVKYd1LC0b6mSvOA76WRo-ASEQEGjClXWbI2Q_u_dFZem4jBeMKRZXgy2iWI0kEYT3ycUDr7NEGEB5F8WF1-Sam82xSs82OVE_Hn4s-pASzE-_L1UnODB0DhL8ssW3XTMyuvEHCOXpqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGa9RdX1uZOk-Cs0d4zHe9oRqTnebfdTZgg0LNJKomRdw-up1h5w545Ejdh_pueDAhNsQR4_Cj5pL1W3BEm3ILb-hHHaAHCeNqn3kGdHbcF3m4nqeap2GhOhECbJ4w3ahEn3ub4MABTbNn_831Cd_2eWkwyHtCBG5ReCjLUWNQ_V0UTTs-qkfyOMKsgJ3m32FnWRI1t8MuJrfIr39thLqvXI-4ZRoQ2yhHKb4PiCh2BlCR4htm23SqPqL5neUlq27b2ve3JRXRlyRu8LGkopTzRIjmBUZy-wDLBPxOjkzp3Q-uCaMrHZ6zLw8E3nCkVsG-t4rPtDM1TvnHnHag6w8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwWq8oRi1IIXArOYR4qG1Ito-z5MNOZNx-dPZPsN-bAogLkqpnyIJWp6mq63jHe1JLTUGKZzn-qUNrM_jLnq1Kg5ObmicTyEnI9azSiQo29aRfCbvayNBhHPR4IEhHDd8IJ1WJrc7_7_5K0ADTp-YWfpxKJo9I9ElXHgQqFTxzjpYI7R5w0YOg1iVSKfpIUtPV0XLAz4vPhG9_t4uvItJRbrkrEln3SE09s4NFWBvrsFSvtH7U5h7tYKoN8ygcS-ENLE69p7Y_dVHCB8NQh3WsDLh6NjcUaSC_hzumUiG54aq2ta542IARqs1HaiPGkUDFl8PC2p2rURJOGooXfurg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j97ZNDgRM13nW-3q-e0mJVeQOYKnq819SAWaf1_KFWERxMakbNEGA6OoZfqIKDu61DYPFdrOxh-OqoEPvCkhS7toSILoDpzBE8XZ9JWzZ_Zt1n2p5alBI623ngfmCU9vATLjBjMQP-o0RvY7OpIvUx2XOfxr9KN5NTIZACyaH1vkbC81aHZOBYsVW92rHLSS4pKlXGV1p0ZsJFXfUoofHhHGbyQ_AL8BJ9vO-9TOLzBfbTu0eLMiu5PU4wsxQoKlvcrMGxmDhhgqWtMvs4RgJC_deax8kIKL8D3Mqry-j_AfwDHf_cijJMI-w4WHdpU6XDOlKB4z_eY8mXmpYVQljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk3tji6Mfawrdsz0N_qWBz2J_SnD0vr0uCCGqcFa_en2mzKzJ5fVlYwTMVvFB168WrSY2kSVZamnnp5a21G7VeywaZ3wqy0OVQIlpHgk9V2DwZczmuA5AXv5ktT8c5JwJvfodtBVTTPERqviUzbNpcH1rWFSaO4EVRydMiNi1cdtrihBnPeFrIdH6PE_nIgpcRWBThtK9Dsji5p0yUxmVBvG3lTWAtLU-dVKFL5ZFqkZ1SPhgUuvcz2e9azVvBKmTu3vMwtXW71WVtX4h8GiR5lJRP13TaRTzVk0sn6bd4Kbm04Bewe1Ba4X80jUfQCswGROcIdApdgZodiLSGpS7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT-JjdRoykBylhis7qa4P6T2OK-D5JOwd3IfCSBnhKKeKyW72eZlbY7SPXcO7QsHK5AsSiG6mrKTvZmFlLmtu2GvC1tNeZVgjy8DxGlF7686EgqdikIbvc0FAoxq9X5HSp06NoiU1ukotNwBIMLFwAK-HR_TSXUF-c3Iwfg5LYHusKi0lWy7hiyGdz1YwzpCDznI04dpRg5diSF7O9su37h1O7xiDPLqMGI2qBaqnWDQtNcyeaEwFPeQqdR1FSELYwHvWJckIOILpDImJrcBK_if-ndYtrpXFyNQybo3ZevNsXgJfg_EKLkacshuiwe_ULFgXDrdsjw4AoeWNzClfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=fXymXVXrcXp9SVfgS5V4mhbPyI2a9k_20iSnacS9c_4fdxDjYYa_B7I1QF8RtRt8VWFpOwG8HFCQVJ8mgv9l9tCuo6GChB62l1JmbIZlRlxc4rX3nFDZ1TaCS6NOsS24hEluhiFdulVk01irYauGGJzami2EHRQU8Kmu1T9DlsrftrTuomzPq_bmimsR0J6ycSdYGoum7hZdQneBDJ2vWl1zorN1UBIUv3BUNZBls9VSVbGJlEv4UoaxsJOHC2-IxhSoeZ5TfHwFnICZllX3EOU29LHuxuLioeC_OrVB-5fAlxpg7Of7TXMxKkhQWqqQ-mGUKBtZjmLKaboj8UsJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=fXymXVXrcXp9SVfgS5V4mhbPyI2a9k_20iSnacS9c_4fdxDjYYa_B7I1QF8RtRt8VWFpOwG8HFCQVJ8mgv9l9tCuo6GChB62l1JmbIZlRlxc4rX3nFDZ1TaCS6NOsS24hEluhiFdulVk01irYauGGJzami2EHRQU8Kmu1T9DlsrftrTuomzPq_bmimsR0J6ycSdYGoum7hZdQneBDJ2vWl1zorN1UBIUv3BUNZBls9VSVbGJlEv4UoaxsJOHC2-IxhSoeZ5TfHwFnICZllX3EOU29LHuxuLioeC_OrVB-5fAlxpg7Of7TXMxKkhQWqqQ-mGUKBtZjmLKaboj8UsJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cifqL6RMtTklFa34iNnwnPPzzzCs83wyxYfCFo5GroXSsIp86rO2XF2xOdxsruenVYmMTrDetXueqtEMkktILDagDLRerHhMSh-g5poiBoPeJ43T-5tjCF_zrrzqtYvRUAmF_mYgVetcwMYE4kj4PidLes7_2rZS9uS5VMU_Ps1WWWmnAnpZnet0LSgQNGwLdW8FqN4Rj3d4VsViEY8QWdfSRJMsXs9i5U8ZWrCWgGXoVQG5ZYJpxddWFhnwR206R7dIDhKyFzQSh5kZ3aS5a3SOmUbXKxfaCSyUvdOFRGVGbd9zejipB1kj7JffBz-PBCFXOzLc_UbmxIgAlhLQWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrpwMyt6axuLvEp_PPNG0l1LydTywpYEZi8HQMUQTblBIDPisWF6zLegzY2aUg9ivwgMQl6ElZz1Tg69EKIOpQXSo8QOc4lZpJfn6G10T0V15DMFfwZwyTChU6al7RopNZdiXdxQfISKeWT1A0ByxWW4EaHM9mJMastwD4mH19-EuKKl8bWiBvI4aGK0ieoBa8vWh3IkUWHgMmvL4Xw48OcXCbNV_wzc2vPrbBsYqoF5QbRwKBJO7qgK-CdSrDEBzregJ8Zqc94oqI07mJKvEdgRXrwNrQ8lNfUib_lfoEFGc_mM2qNT3_VRX3TBwXrHzwhY_GR8_1X8KMFSrQzU9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=uTTWStv0MEhAn3cmOt-uIr9vEPtN6901-nQBxG30L0g7G88BfT2N2BM6QXR5L5C6t535n8GBK9X44YtT6k0yVfWBYmw_YpSa-Ysng94PzG3mvZjRWvpctAWIojCdy-nZbRkHMy_tBAgc-JJWE_mHNhDV7nYX42iTsTzAlx_q9fH7vC5EHYGwgNIpHBLB0RU-Fh9Irz83MC4nlDXRztggrV7Nb-29mVCAeu81mA_g8Ezjkwl0XvSOvBmUlNy_ta4UmaDFK51k3CCSFf3BbgjHEt_Xg3oCizFp_F1gxW33QZxxzspehDmkIlJ1_fuBqDut9XhmHDQMLIoxvsHeiMQrH7b28YXudYjaXUSB53T9HFNSZk_65YOGnjxPd3wMx71hapiYqo7N1pGJZ-BI0DKUazptM0h6HwN6CkjeFAOB6mimXoxNsAH_-lOm9DtUfwvL99z5yNzVWuuofNL1YOZG8cg_5gZq3qa3nsj9CuXtunkjlSK3PP3kmfm9NqC7wTUwqDAcVzicICQDOYkiMTh78xQVtUHWYMIrTXwT6ZY6tVwNuPS2yrUKW4hIoSu8_SWSbpvn4g3VuDDF8gfkn13KOCa0jGLopxdhYzD-N8X4BSkn5L-dnETO2-Z9o59M6qky2lnD8lpCzm3QsJWrKBFdzY2JaTcRW4z5VTtVW9kb-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=uTTWStv0MEhAn3cmOt-uIr9vEPtN6901-nQBxG30L0g7G88BfT2N2BM6QXR5L5C6t535n8GBK9X44YtT6k0yVfWBYmw_YpSa-Ysng94PzG3mvZjRWvpctAWIojCdy-nZbRkHMy_tBAgc-JJWE_mHNhDV7nYX42iTsTzAlx_q9fH7vC5EHYGwgNIpHBLB0RU-Fh9Irz83MC4nlDXRztggrV7Nb-29mVCAeu81mA_g8Ezjkwl0XvSOvBmUlNy_ta4UmaDFK51k3CCSFf3BbgjHEt_Xg3oCizFp_F1gxW33QZxxzspehDmkIlJ1_fuBqDut9XhmHDQMLIoxvsHeiMQrH7b28YXudYjaXUSB53T9HFNSZk_65YOGnjxPd3wMx71hapiYqo7N1pGJZ-BI0DKUazptM0h6HwN6CkjeFAOB6mimXoxNsAH_-lOm9DtUfwvL99z5yNzVWuuofNL1YOZG8cg_5gZq3qa3nsj9CuXtunkjlSK3PP3kmfm9NqC7wTUwqDAcVzicICQDOYkiMTh78xQVtUHWYMIrTXwT6ZY6tVwNuPS2yrUKW4hIoSu8_SWSbpvn4g3VuDDF8gfkn13KOCa0jGLopxdhYzD-N8X4BSkn5L-dnETO2-Z9o59M6qky2lnD8lpCzm3QsJWrKBFdzY2JaTcRW4z5VTtVW9kb-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=XFQ6svt2F077Ys3hM4TVH6kkQyTdYR5GGYeHb-893UIhoogD9R2-OZySaB2GW-4QnaDBuHhlpWc14DOuDi3ie-kwrXM8C1llQ1M3jm2sbvNxO2oR9d_6TcOJYCCPiK2yqpNkUJPfJxkOjFT93TJ6lLjp8WudSkSXDgG6EqOGs-kth3naw3Gm4oDeZGV2mHzYwq3utT4IuXFimJS212wSc3BM3MwBhr7C00JJ8WgSYqY-qQ7m7rdsjYLTxjS2DFkz3dwF8J9cT4D9GQJExp7CC6hxnnpOVVFF6FJOI8NZmET-35OoVCiaUkSk2Q0FeIHN5XNkkGisOhsIBvlgJI7DUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=XFQ6svt2F077Ys3hM4TVH6kkQyTdYR5GGYeHb-893UIhoogD9R2-OZySaB2GW-4QnaDBuHhlpWc14DOuDi3ie-kwrXM8C1llQ1M3jm2sbvNxO2oR9d_6TcOJYCCPiK2yqpNkUJPfJxkOjFT93TJ6lLjp8WudSkSXDgG6EqOGs-kth3naw3Gm4oDeZGV2mHzYwq3utT4IuXFimJS212wSc3BM3MwBhr7C00JJ8WgSYqY-qQ7m7rdsjYLTxjS2DFkz3dwF8J9cT4D9GQJExp7CC6hxnnpOVVFF6FJOI8NZmET-35OoVCiaUkSk2Q0FeIHN5XNkkGisOhsIBvlgJI7DUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKaR4z-t6BJGe_g-m1i9cFiEyMgM4p6ugA7u7RWeEM2qXKbb-WTcV3BgpftViQ8kOYcx1HoPMjAySiTiLXOI84wTnAV76USRFzBx2p_GyegySDKuVm3qSIDzj7tl_EcoQtvB-1Ac5uEB343JI_QO-hcmdka-8J3xq8RdtSysr8gRPHO_H2nyfPKS4yup7nofw2WzmKtgthmyodEa3BdvwXJTfkXJbjNG08jDKbBisioiukM8FIMjzCWbJej-1FNx3pjtwwPzPtkepdzgMr7uPo8oWH_Okx5i8PzwtRPaGzQl942dP1FXiq12fonoCOuy59IT93tFYl52hxlPpqLaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3m9z32fMCaez64JIma-6Jzd709BeH5P8sqCKZGgY4-1W5b6mfTRafRIY3WWMpkcM0Gb7SntHzXDReqSSD_QUGcDQz_PNcW8_lINP6FMrrER0O3KiDCcMAmWXO3GReeJwr9DBn8aMzUFCxQEqs8hSmgr5ibiofqa0P7YT8Yx_bdofEIxAybL-KowtltKrcPZZaBo-pnF6-KD4RZNAP6oh4GWpLSyoaDP6FosG5aOEZZGD2xL-NTFVR8n9Rf338yX_tNPpoQtmMHzzMcv8YHEB1fGu4eq1qI6HDZS69r8myJKIOfKkkPFt_epHGpllQ9UD8O_BnS3hC6AHt8dLe57Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtwUnsR3VqIf_O2MMFgtdEkjplpdXDKNLWVDwxc3tKgvH8-_gI3F2uIXyZ-KleYzPQGgBx3a8wr437Va-_0qVqJMqwfzXER2f8l8UA6_fU9WhY2BB_6h_xSGTGHS1kyaFQyKsviGQ2sWX8OL7dluyQ-GjM8gwqzEbJx8syqzU5ruXHi4Wq6ps30yYmaW0A8jya7R8biXp6p4m2HQYyOu4qP3FeWyH4xfr41IFmNP1bV7qvC_45EpCd1oN4CtlbZBilK8ZQeJz6BfZENWDkDNvaX-64s4hta6RBYp93j_UQ-8LWuSBo_ugYjPDi0EeALjlCezzfrGKGhqfUcHDSgZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O66lHThnXw_ocsg-6kwF66YScsnkUOFvBiHKTJ3AXVY_hYj5tDNFnUdMjFgWOIdcGuNu4bIHmPR_L26Zi8LMIgQxtiN1lDHHx6C2h9ECS0EtQT-Iag6TANJNpMjQV5dxy7SgNNcIAaFwZDtbMYlW4-t-OWVVhWBec-0tPC29I4zDNLmTGyrY2ZCmb00AVZ1nrC6ramKHQgIh4ntWs7asg3OHF0vm8trJq-m2C3VwCDvL0yEIKG7UpvwjSJ-ptleNnyfNcJ-9SJBrWUqhMJXOF7ksaNALQiWIIerdQtW4oiPIlvVtMSegdenTwjqAZH1_ov77VFt-iHfDp5HG_dzjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/in3qun6wXEJik_aBe7mTJG_eeZDJGLpvT_1vx133zIUotjIkbZOqUmZc7cU9giCQ1wCnqSqRP1U4ZaJbnYK0BfMzW5HQkDpHSZ7Goo-BGynoxWfUPQbsXEFcS2g1CyIsQyzlCI8xP7O853rrZCBK3Uy5dIpDBTMylym6DFLXogpPHP1ndjjsV1OKIvTe6LEocXj6UY9BcE5t7LFdWuySm3BHHGhC7rjIXrsnfr9OKH09P7Ljxm45qmpK-MFbzvcVxwV0eeJDLR0VTBljYzcgSNVOVLvWbtZ22qaXfXZKL4e53vfOvL3-ck8Xy66wwSFUEcv2rwOKkEC1gMP9KB_21A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGvuDIMxxPShtjgwQDlPO_B2nE6477evEANjq0dj49ZyaYeCR6MkyYZ7Im665V1g-Eu723yDF5s-WNux5uVe2BapCN5vsTFIzcrEjRJKR0G4eTCbpThbq19deBt2jnHQj0phE59011aBBkmEMtLj7O1XxXEa0GofP-PHXjWHEzGLo4q8qjkGNSGyvAE1tVGa_Znkf6FuTHRF0WQEKUH-SMCpHcc_H6UZPB1eTVjiL7W9fb-6BtLgDK2BpzcHzPcrNdSwzIkvdV64O7Zojoyh6808nfMlzBzClB0bPgJkBpAy0vUtEPFjAPSQqjTLIa6BKN0yKOZ632LqcoVe0W1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRh20meWVKXpUd4ansXWqJrh_1vf61Sru1OxyNMLWQLSpUx52Y1PZbv7uXASSWMF3ci1hNkAlsdvEK3xffmdLAKj7xgiYln3m87E6nPlGLwfgJ4GhqWCe3U-lGEr5wr5-gDKc6BT-PrseyhOXNLKJOarFs9ob-zHmgfx7lhuG56NdhcVcNlxi24px9WHuZ1E2txkztpf-dyHXV4Z19Gv-2te-7Q0rcBKcD-CsXPhiv7fTNCyczXf-cXq0ymSktvyp2Ri-IvbzpQE_jC64CDbiuwtx6J1TI4eS7hIG9qWyfrawUHCJHrgB2dqQQCM-fuiHRzeRdRfk84GJmepjnXSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHQdxTFthw6fj18ggYiZpTmKChuwktz5Gq4oO2A_3YtYxkslUkjc7SG2qYPS_7ukD9ROrPEjEGj-2EcIyp79Z0pycY1WJb6dpNh1qarBUSZ4NZfaeup0ekDih3j2sPHY9D38hMr8ZkKKZQjWw-lz7qQR0439eyXKLE6-0SvCYPVZmdMDk8dPpWQHkRND-hnn782bMU6-itM0TzW3Jk4H4z0UEyh3U-uZrRWpiG00Jnb6DY9uZJfklg0RQ-kx2tny7tcaDtzMocHQrWqE4NYz2T0JpJebOiAM8O_HPeSkbx-i9lvPJ-3JJ669AO50Jl57pMauMwhvmN8A4Fg7NKbiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSpaVdWHbgSqhbm9PzTPl3ahhDYwBulL41O-YIoFkgxN9bbD6Xc3BRvdQ5mjFhMT1ef3UOiewoR5GmgWZfF7IxDCUwKUn-cQ9oblyTxP148GTgg5YQZ8cdD5T-a9vTJBkpkhxLFBs71LeEsCkxL0y3659YbhMxnjQjCVfnJhzg2FRJEwo0khnsMEanwc5bboCE0OGsWYODqhyKEelRJNqJIJfE4NeHLZOfsgkAHylXMetH8UebB8dmVKcZWtcPblDHri2tLErWHwFX7M3aTf8pxqeUzJ8fgJW4z9zg11nr9YSYOCiOoIYPlg10OlkPKLUQtzyi_u2t34jDEMcTdATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwpyZVRniFrMBs2YVcksv8x7Q82NH0xZoI1z0GVL_agBYbEvWQl-FXiGj1BeHcXWL0CAUNPke1ZkIVwhkumNfxOJuPLVEocI9Tu8JRh5PwmevGGWNVqI3qAoP_QNrSxCbKI41wBKWmpuesa0jYmXwyqdD4zBTJbjFUepd2kbe5jcuYsDmJgqyiKxtrtFmNy4b6S8sUzG16X7UUQJozZO1Hs7FGxjTraFKnKYXubTLpa33jVoadrkkfCjjncenDP5EeQbGdeIjpOtMdaFPojUdiRA6FFZOJJELJbLTBJaBLXU2ZGc7Nm_tz_Eg1QyZGFI4ReyBZMN80oT3O-hXhAgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehWyV2PoLby2qByoNZXbZEi5cejVrE42v4NFok0IZselmqS3i4Z-a_RaCQ8KVO6wE0uxoc-ReDcVFtWJW3eAqco_XY7wZsJRKC6c6zRZGfnWgvIpTow0gYTZtpF4pRkO1lHcK3z0znCAylt-3dRHkrcb7xcWcdUrGjaB4UBD420VDef2hDyiwsH9BidqZNOIimJLz-3K7JEK40N3bjTrQ0gUJ3XiGrbiPsN9IbChNROmHnpcrx018FmJnENxioSAeE7x-DWVJEiReCThD644_W9z1NiDtSpf9OySNUGB_fbDGRK6wInWsqZk-IAI6oPyY27oKSSz7Hqop2IBnA5wEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_5cseMgwD73q8yFqVO2NlGi78hOI2kZePbUgMcCl4F1m-qRO0KoB83m7b4C-W01Mb4mDJg7d0EJ2fmSYMEWBbQpccK9D1X9VSBYfBJX2xP0HifdCskg68Tgge87MADkR90HoMq5eJs8A_4_rSTEKYu3F6GqQXbfAx43BNEomx6QfHu0Q3HdWfkA3d4BIAoW-Nj9yxEsZvssJrPlvuo2lT7KKAOAcsrDLEUBghsX7wtM92weTUXX7uvaBluXj50KDFmbWd2JQ6vZMHXBY1GLCh_pRiHvdQZEZLCWDCZlHrHcDH8KwbkDTHx8fXhD4AKmTYgORLyVuJsumNbOULii6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=SNbcWP7jsFBgVjjiq7ZajBuwKmxGJNMdz6oY22w6G5L48JzJZAWqkCnd-uDTnjjGTcER1i591PktNG_VTXOHq3wBY9D5CIQNM3l_LF4sJBRfS8W0P__wJUkm2tzI4DIVAS9L7gWUSLOxtvgaAwOg87wPzg_eeFetWgDl0vMV6SaOljL6ZjIGBlSW6FDeAMQdGvNjK9fuK7rCsCWujNdFTFjkand18UgkJeuE07M8tfp0fm3MFun5L51a4H9ZZHmHxyH4Itknyw1d_XsRUQfeIrsw1IPPnVmE0QM4otJu3Yp60MNCfep_ZBhN15bwDEsPRe-BTYyTjRmXgkOsjuxFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=SNbcWP7jsFBgVjjiq7ZajBuwKmxGJNMdz6oY22w6G5L48JzJZAWqkCnd-uDTnjjGTcER1i591PktNG_VTXOHq3wBY9D5CIQNM3l_LF4sJBRfS8W0P__wJUkm2tzI4DIVAS9L7gWUSLOxtvgaAwOg87wPzg_eeFetWgDl0vMV6SaOljL6ZjIGBlSW6FDeAMQdGvNjK9fuK7rCsCWujNdFTFjkand18UgkJeuE07M8tfp0fm3MFun5L51a4H9ZZHmHxyH4Itknyw1d_XsRUQfeIrsw1IPPnVmE0QM4otJu3Yp60MNCfep_ZBhN15bwDEsPRe-BTYyTjRmXgkOsjuxFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E590rBZjJlP05uxdiJtJR6_FYewyiLdNlWxH_6L25iqTqvqVDM4E1-POLcYfMDF_GsIWKs0RP5enBEL70YsRYk7mJQnrZ7E8mq0IBXJ5xPVhU5DJD25PfMm_tsk9D8xt6ehc5LEmfmCM_d9KMbqCWX7AIhGSUBrIXm3T7NfcSUfOxmhHbR1d8odeQQG5UMzPBNDgpeltoInoYWfTozDLFNtQAtfHdzGVTMPn3hbKyZZ_VxYibs-opxeImxIcvQDti11rsUJSm-ezlNq6IA8mBEUyI1mLmzCtRLhAN4S6EZIY6iJO7ZbLAw9PT0G5JCR-a4SjhH3akqfckIsijn7-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ1hjzruNLYe8FNVWWdIICZitMYBV-vSy0mTHmLv0YF9Oh7Mt0W9jExuG0hDx22Rx9bOPtU50_u6p_0hf1ESAs7KiyVSFOapzLE0HixMkBEtPU7IyeAC0LckUIOESpATSbUxODDIigtXJ8dA6v3uiNDMlysRQcWjGSLvNiuADzLP2etR1W3RpZYyqIYbeIJOt5R9mLR1vtSrhsWv_pb4eqAe--5Q5gnDHfkneQrncUrraJyGfZQoyPQVIOYzYf4US3fNWzVUbNmzC5Z5IMbWrvkwL05rtr6xulJWMjoWtULnzwU8euw2uyxXN7iIPRUeKD2cQCj-SCkv9Mb-CO45xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oanVcdU2ycFyOZ4D0OA-Pg1E-au3OrPR3StBb576DCzvWGc4DtIWa7tC65k2csbkZ2D9mPX1wY79XtSsY5k84vvBsqt-48PB449NC7MEWIyEG-kPUTUmrMI993h8HTIksv3x3wG99RcKWZsy8wRt4iH0jU263Da2gszvM5ttRV81xSL7NZv4AIueULmPGUh3O5g4W-GbyAEzyxjy9Ua9WZ5ynBR1euJRmeLZ1IWh8Fp5XGtIeVk7NztN5VUxdt0RJnFSuvSSvKiYuWLudUtNWfTb3cKfvt8z_TzyUq885HMO2C4304hfRmgVpbF2_9cMfqWKblRzjWSgFm4MQ6PBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtBZybLATLpxMZSBE62NKCLgSOvNWbSpTfiXlxSt-hr2nFBVEimm4n5hzbGKS0nzVa5ywtwf3E0_zucDv1mhgj9WjyS7os1_5jKJipenIppBi_hlzY4a3vLnmI6y6NjXttwAGs1J2IPwhwVAJgagfykyL9CN_M__u1p-YxMZYptv1j2B56yScBHbsJVc-2cfh_-Cuxd6pQE0nmyTkUytgVkKDkAr4t1ZML0aajwrQRGJwNLB9-XzddfHaJLp8DzNYvCYm3F80dP2GFAHVbpXamFePdtr0HPHKcNVNXIgTUej3ZLD_R2k6Z_VVxi3xpBMo3VXaQoSrrY5rlhWDLz7PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=O2EtzZNNXlW_SUhLlArj-19h7xPU5Am-EhCovAv8Znm8AYvmRG0e8WfRGeWQNllHj-zDjH2IHKCgJzSkxBtfXw-mMDUQukojSZGM3Eux34ot8PHd_gyxCTiz5GQ-dQ_joTTO1a_eKeSwTEOzzXLnokr8tAcctagYwBRWfc88kQdJIwXGZ7ODWczS4oe3x6GFiri2WMD2MpZyJj8QlhA0IROuF7QmX9ZWW01tcpE1UHwU6bUX7prVq9MSW-pgNXX0SDQy0wiR_2ITmP8_w8UVySksJcyEAuxlbb1gH51931A-Kvu1_A9tZOL117qkb21Mm3GrvrJ5NyrlvuuPTwxz8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=O2EtzZNNXlW_SUhLlArj-19h7xPU5Am-EhCovAv8Znm8AYvmRG0e8WfRGeWQNllHj-zDjH2IHKCgJzSkxBtfXw-mMDUQukojSZGM3Eux34ot8PHd_gyxCTiz5GQ-dQ_joTTO1a_eKeSwTEOzzXLnokr8tAcctagYwBRWfc88kQdJIwXGZ7ODWczS4oe3x6GFiri2WMD2MpZyJj8QlhA0IROuF7QmX9ZWW01tcpE1UHwU6bUX7prVq9MSW-pgNXX0SDQy0wiR_2ITmP8_w8UVySksJcyEAuxlbb1gH51931A-Kvu1_A9tZOL117qkb21Mm3GrvrJ5NyrlvuuPTwxz8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUVWHTRywBpuwd6GWoyOVQxSSZN8g21vjhpbcsKfRPXfN47eQ2V-Uuk0awot2qyd6R89E7dLw-pYgjHdUsRrrZhzx1-8rU6UzEilGnAsqDmntGAAZouzuSKtosLGT4gr5E9ihZML06asvFWFFLAx9Ky82e4kjFI58axaddJIOosddGoZY1AtAJgmZZFbYzJR7onOApT4UIJc54szcqhHBZ1WdZMqxcVg9jDKhxUvijlFD1zjQujOiMMzvUvAGu8eS3_GSRhFF8dBKbVWIukAAn0I0OPWk2zQLyyqWbTPyvD5dmp7psy1z1nvC9PGh6aPWz1sSxBdYfjOfjc8rBmMig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSFUfNIf8pHkTs6VNKpBphVouWdUJGXuCYCdSi-qowrMbkxC4tfA-t2eITW0ztuwkMjkjeo26Kf6uQvgytRq3L35UbBzv7lqGcGYuRRadF7R5JJg0lxHcFIo2X0EaUXNtD7GeR05V_T3ao1IE0aEuzRQSwHOsl4dSpGbtglyLPkzZBveDPkpED_lVZDDYWHYSNpfAfb4uGMShs7YO1nH4CMtMAvrphm5NoSAVdwmsoi7xTj4ffysK82d-TR1SYcRRmvlMl5Jeoysc3YRQr5DOY102QbEcjPTECNLG13kzXPTlvsB8dkLqwwfo7h61_WHhHeEQuul7wA21czwWFmxLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyMhf0oWPinQEEYwYIk7hBbRJu01T6nJtcLynhbVWXxDNRionZ_r11yveFDHMCQHlSNCNqQTntYLz9zWzTowRl58lKz_tfQ16383Yk-Pnn3ZnsC_2bpfS_dz36Il98jTz9J78GR8NVVuSUdqW6bF2CAqWtTSqH9m1cZtheHTrFFtGTgN2z_QUk9h3nxVdayaQS6k2skoUDV_1OPSk21KAVsEH-uGdtc7Nvf6eYdqn-hyZvhjz_BVPykSq6JFa4w_JLUIGB0GJMnAFmKsbHoowEWBB5ODakJkfiO_bO20BH_LVL_6kKgm5W_srbL8mmOMznLKu5QbRsvTgm-0N0nzPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=BDIm21mjIcs-6RWZACi55QgqNtnTthfyoCbarDXxess9gdg3rNygZYTg5lCmqWlUc-o3M5NFi6596N6cPKiwRQZ_StXe8ttl93nX9AJrocA9UlQ1AmRqhP-evXV9j02O4xRFXf-eC7ufUSKDx0dlUibh0_Kc3clzERlWuwh5wHtDq-SM7UT8DFCLCAgA0zu3pXijKa_ozRIFegb8ZzlVBvXWepRsKY5PR7b25hSnbRDsBZNlZ91bhHU0IsJxOC-oZuTUodFQYvwPuHuOLh2eli8q635jxaMJEH_R8BFoXpkbif75p0QuadgkZykZlF32cI5I03zxDgt2BdOdsFbvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=BDIm21mjIcs-6RWZACi55QgqNtnTthfyoCbarDXxess9gdg3rNygZYTg5lCmqWlUc-o3M5NFi6596N6cPKiwRQZ_StXe8ttl93nX9AJrocA9UlQ1AmRqhP-evXV9j02O4xRFXf-eC7ufUSKDx0dlUibh0_Kc3clzERlWuwh5wHtDq-SM7UT8DFCLCAgA0zu3pXijKa_ozRIFegb8ZzlVBvXWepRsKY5PR7b25hSnbRDsBZNlZ91bhHU0IsJxOC-oZuTUodFQYvwPuHuOLh2eli8q635jxaMJEH_R8BFoXpkbif75p0QuadgkZykZlF32cI5I03zxDgt2BdOdsFbvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRoKvpCvQw1m2d-VZ-zjDbLVAjr0hWhU4b8J0V1uDVuPJqPTZq8WBjT0ZoSPdbGVpNjqmVR-dPkFGSAnfxSe1X_NkkZPNzeWa7cXc_EV95E--x3qGB4SVKkuWjj0maiXf4IAqfAM5lG6xVloOtIfM5tqfb8qGjGLM9VAyoAx32Nf0jAday_p9rVqWSBRBW0JVZTAuY_Tb7j_pgKMwDSeKTh35wB9-W3qGpS7W6fB4MNWNcinIFpfuAMc9SkD2sUszvtC1mKXWJiaKP4bPuISEqIcL0nBOmbCgCeqZFWI2LEsco6xn2zeJ0pBwsLCItZ9p0EbwIzsOlt3UPdALF5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2vdj7t4h5BghNXGT0apGJP01LJQwmGRdr9-U-dOJnnQtA3DjyRjr05bV4RHBKWgjHbQp4aB8uEdb3xnl0lzdkjG04X1o86fQJ_x5Ed0Op3t6FxyESOG-1dJXF1PFWuEkLtCgKSw077ial21WsXnhWd0mB-U4wZugB0WdF-WzHdujY-9b9YdFAddr-WRjOZRATft3EYpVkJ7jpP1OkIqUB6WzP5UZX603DjbdVokajP7njpGKdCtmqNi3xF0AM7zYCfcr2m46A-ld-sVEJUO65Ed7evdKJZkroDZuhbu6B7NlB5yhVHwNJE2gPqtZJpdatebuyIKhUFBrjAUdR5EEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkgHBtuQUY-Hqimj0FT-DcpUeluGMZYuK3YziMhqzWUeuRIsh0zMdeAxigpqEGwpEDSU5ktufsK0oryGjrUB1Hjz9jybVG2ZYWiIfFRx1VcJ-G_nqDMdZGYcYAnXtoizL9DRa3A_I1PiM1XvPOVFurVtUmpNUuDV4VbdwaLRric62Gr5vrcQoAIYHLoaXKGkaMzI6Qt0g8h0WncYvUvs-cuoSmrbuK5rKkI80Wc_tayF59rJbgmJnNX5HWdj7eWe_ylMGhqj8nIXKS3WPWY8uLoTCGVccl6f8LnetkqTfAq1tOEJxtgCPJprEo9IhVYm8FVGMgAgMzkmsDLbjkXiGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v79EVi8yi4ByMnWTQo63xiqT6apIA-5rhs70rPPLEzd7Pf5IK0luay5DdheGPWnSJeERgFNKPD7UpV40GWhOmFan2qJ6DtE4LfQ0fCvTml4KwHaoZAjjKxPi0q1wvcVEk_6HxoyCAbn0mIJx4Vk7APHDaZBDJucFzvbB5eVXbQgoUA_sm4srRzF9cyKm5GOvWNaljg3VSNXXsmPszeQu36DSzhifP0xyDwMIkz0nCKY2GpPjPDjSgB2toIMCV6fObtqt4-hgD1UT4cEpQhB22h7pISaaimsGr5KdVeCthZ11fhNE7kDmT0ef_v8JXrjDY8sg2LPcu6efArC2cURZeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GePPOV6fHLb52wvLLjaJe3nb1Vm1WnJmjJBf5c5x9DJG3iPSFEGNhosxPbsfskFs1cjMFh3j1Zxs67Sultq74jcZnhw6cgq1EIbyBmLZNcfE-XKUuTbw6dd8xl5KNfXgqsc8BPbKLR558mjVCp-ITuDl4mOf2i5GWb9rRSiJalDUbdsQ_KFvF5qM0ZjmR66fjuNIm988QQcoCou2kVt2WNnh99P33OMC2TMx9LEhcZsXmLXvZQz5iNqccL5p70hnnwN8JAc-5OrQhTolzuHvQqULnr8pTFuuWUjiVQCmF11dY_y5AdrbtUJb13A__IYsLszgI1tV-BuBWY418bit5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGKGMgJ4mzbXh6VkxFsq4h07cAQ3lzlURfMK6_TA06jqOq7LLBbjLabXYgLgBCxG4IBy3bWXxuYlKl2EUwe6TOlbyuN5uZqMg3GEL7ngK3jxjFg0KGHGkpqYLWx-N24ribAQ_nlXpW0kuFG6cNI07tKupa45eJX1ZActeQIQV_SWZ3XF0rwY6wg6eEJQgRDTUA_03vy_ONrCGw3nMrkosKUDD2vOvJMYi2wPaaWhp3nNK2CZQ4xiWdPaI5eKjRUvt5Joe-RrOgu8g6hkDhPzAvnj8axcY7GNcjZXvn_geyM3e3XmD4d-p1_yaNkJQ1PDP9yjt-TiBWo0bnqZ12fWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=cUeYGYx48C0CfIabI62MzEP9IbKKSY1aEi-2HMntLTds-clusayXuOZ9OSK0UlxMN52kVI2DX59EQ9AidQItMWO_iHO8mDdsgCYBqBs47zSdvdeN0OtfkrwgEbfFaaJzHBF85K7N7ILLe0_fwnP4lDRYyp19UWIE3RJAuaMbOLb0qkmGXcC3yICAbFQdHWbIhdxJOxsLh3tSSCrchQRCWhX4IPUY1ukn-AhSDrKJqvCugt7UM0aKMgb-mCmPL_ZQydPYlHkjoXWU9VMPnVYiQ_ZODNjn84hqFtMA9MotM4EMKa4RfO5Cu32Ee_cLx255Z42ZbqgqAZSq2HAfSyLjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=cUeYGYx48C0CfIabI62MzEP9IbKKSY1aEi-2HMntLTds-clusayXuOZ9OSK0UlxMN52kVI2DX59EQ9AidQItMWO_iHO8mDdsgCYBqBs47zSdvdeN0OtfkrwgEbfFaaJzHBF85K7N7ILLe0_fwnP4lDRYyp19UWIE3RJAuaMbOLb0qkmGXcC3yICAbFQdHWbIhdxJOxsLh3tSSCrchQRCWhX4IPUY1ukn-AhSDrKJqvCugt7UM0aKMgb-mCmPL_ZQydPYlHkjoXWU9VMPnVYiQ_ZODNjn84hqFtMA9MotM4EMKa4RfO5Cu32Ee_cLx255Z42ZbqgqAZSq2HAfSyLjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBQm5SJvSVEX8X58jnCkiW1l-jxzusUAWE7p0ibeowUJRrxb_Quq_WnSoGMRwfcu8rXh6PkaQpIDK-au-aEFfqRuvtQ0Eg2zhtRD1fcDgCAn2Reyob_hanpYmCqybciEMfb1L66LHhPRgVMEBqrlkmJq781hLf_9V_t5MT5PzAzbuNb15NI7EmsgOEq-embo5N2ghN_b5IhsmUhzYNk6fXRxwb4qtRGhHdCQoPpggCy5pkwdLBzfBnv5SLEZhxxAdbVbxXLxKGtLIRMTfNGaGvd_FBP0KG1uFqVAYr_Ds7-o1T98iNYaVF3dx8lE-k7lQkIj0e-3m-Bug4lcyWsugA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWyyet9WXbSQFyR1xOIFFlVUNzsmRQPzznEO0xW-mvkswIjReUvwthLH6wy1A8xbBvXNS-c9CisbNJUx7PbFsud7gho12pBdD3BKmLms6EBgtfcfp3GSwuL0_p9W_duhw3iVsJAEa4pRU36e_fKlR8ffL1VFTxsxaVqFw2RExvheQ1jehB2ta0wUzUG-2obA74sMSIzhhpLktx4lduhUsZGVlD3wSCLC0Ur_sWmQIKBKIyfohkkWU3bSVwACq9JDUiKwi8YAdXSYLFR94b1IB1J-YlyHkxAc6TrgY0t47xcCsFkThEQvkog6z46xtOLKo7ouejcpjHXxLsgaft_4yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
