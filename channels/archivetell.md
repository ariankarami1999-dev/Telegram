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
<p>@archivetell • 👥 9.67K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✨
ویندوزتو سریع‌تر کن با Sparkle
🧹
یه ابزار رایگان و اوپن‌سورس برای بهینه‌سازی ویندوز
• پاک‌سازی و سبک کردن ویندوز (debloat)
• بهینه‌سازی سیستم با یه کلیک
• مدیریت DNS
• نصب برنامه‌ها با Winget / Chocolatey
• حذف فایل‌های اضافی و junk
• بکاپ و ریستور تنظیمات سیستم
🚀
همه‌چی تو یه داشبورد ساده و مدرن
🔗
GitHub
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🧠
AI OS
سیستم عامل هوش مصنوعی لینوکس
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
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjHlVjn-sw8cxTOxR171VV55Fcs6MKIgThmxh68tmht4JfVZcW94YrX-VdncHHREn2Np5K5DvsJrAAu5pJp5OIrRMES_yYpR1dHW3XRVdiSPYLV6r2Sn3R0yeGlZrk6485qz6LmG72sguZTl4nnpN0lLOQAwQWZ_OUpTpDTaYcWOySrlNAAg-OlbdUK6tLKzMEA0swWkuu8zrLv0BrAxB8nKsaR3lU3m2oKgNLdDC7u6eSgSpM-sIRPlpR5kBRZc5ishUBRmU9Dih3-3-qMekm9oNnZFZ7TMQambX5xjezGtgGAEAI1caLmFt4oeLfuDVkPchQISbpyrvpRm5xzLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgyHvL4IROK6BSQRsoBW3aDV6YwzXlQ8SWvjp07jgDwNTs4RYDrzqGqdl3_iSnqoQ_KIBGsO3a0MljKjy4SR0-PDJEZuSmNZktkSBQDG0Y1DLCClNjkjpEmsyrr6FggPqmZFtytRtjxIs6RbheM0M5C2eosRGL4siDzfBe6pUfyshD9I3jAJYHsjCxCbRoY6_MrQfgkw_k0jjCguCmkYQWZz3B1YNKxJasa4W4mSHKzhyh3nhdA4Uoy46svfUsaBG55PXIshom_QGh-gkFKQw7OcQ1E0FDjGKChvTVThEUy_yn7QH3eQjW-DbJuBD5ChDy8mAKJDGUVPMbLe5xM5Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJqdNmscV5ZOlPEiYoEkW2LNLk7YmIn2eRyeJK_qgxV2x3myiJV_vmtZAtbELnllNMB-EsJqlAx7A9-4wLKu3-eepmU0rbTeYzSUwYbUnDCdd4-zFC0K_BaZ_JtHGNwvBZvg41JDehx9kj0z4RnkRXoprQaQ0B0Fqc_1WN1xK630HXCgrCWPfCwYKHxxWIekU76V6T0tXrecqQ5KOdbzQY1nNg5rxEoUD5pl_A8yVwwJ2-41ie-sGF5pc1rTohT0gOjwhWOLJ4iSxlRwQnQQYn3TI11Gnk8twpZ5FM3pyzNMQeZhet2XRHLcpyoMgd8PRg8GdFFj58h1GqpnFQYyPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID2lZdZ8YV10nD-9D5YjrPzz4KC6kBCfali89U8oTolfIxeqPp8t3zkiYUrS5vAfvvnkQPVFXPjh0LSme9oWvg-94IUFEZnurdbneR2LK0BC8lmLl3xQzbDsezrg8eHmccmv-WC7Qhap_Wb43ZMdLIByd4icQGDvKSUUaK8b6bFj0GB1RXj5mT9fmtuNmCpw8K1ApMnPUnQBJACV6ecJ6v-DpLUp49Pv322IBVQt6_r4x7RdB_CGm6jW7LYw9VU5uDUc_jXLe_ZKlVRPjPHQUG2YTfC4HXGvSFsva-mEd-hS2zM36Qufzd9P2r-cVHVjRcfqW7DKnZdIf5bPh7750Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLkG52wuDdmuIdzxvJErRCyHNMboOKtrKfZkTEI4xvgQa4qtSpNGbbV6RfpGMFFhbFdrFlAIaQ7z5pflrrErL20CysU-GUAb-RMPYj9M5urdC0n8_UHbwQimoZItMax115n5ehKPLHV-Ot-WPAuR72EJ2u1PVjcvX_KEmMXFExXFbJCF1LTgFf8C2DIJEgzJ3pb2os0wjf_NQfjcmj1sFTYxNuJMoFGiW0xHZgd2LpHyghXrKG75jMC4npsbdP-2VTLqc5Q2Bi4TfYb11CL-0qI6RvWRMb9HY5uaYI0vjcx-wV22vOHbNYTcT131NGM5uSiznESUaeewqN-lwhSxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prMQdVsdFPdnEuRW5hOgSuhhqkCD--qvTtKqBPwBWQZEz-Hfuy_5aaYDiD5QYtCL6lDYxhNIJJfqnPpx1k0PP_1I2HjWuO_lcbUT3Qi-uD5fxdbUO8xFVX90-RiMNqlDFPsbGuTarfP8jjWxh_ANgbyU8MVPCzDjL_OSWSAUGkHE_ihhCWqdnVJPJobaCHkd6i6xyZvqSh0_B3Vz-wJBF9DmgVPB9P_3AYH54QVrOi-BNEIVj9SLozlC2Tz0z03nH2kPWMy04GkXgGrnoeP1dyKLOdx6HyojPZ3efizNjODRVP6uxeIvtiPlhGk46HfuI6INesQmkuE5qES5rBIfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0m9VR09KHDIR3dwpEBjDFsu5SsRLDorI-LQLkhldy0Jq9LXKKMz4i7uDmV4kQY9ebXEMZYJGAOd4BnIIrk7F7Ab2mPx1kGlzFEM6jBpPr_qUftuEtN9VxP3rKog7ct_hhg0ce4tpCg7_rvxzMrsQCZkLJwR4Tp8lksY-hk5VXmY2AQPojHz2ZruxkT_GSva1Lrw1p570QbN9zzoDG_dS_COju0ie6YZd1fr8kB31sKed9ZT3usW37aZdiVaqPG7T_5S3uJFI_-74BD49e1UTYiljeC8-8MN5sWRrOQU_jFbfuzAD1NOfwlPn6fDVyyR61nAiwKRRjss4lPNbNHOtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWjCeR6IVDsznVhHCF1c1MJZvdoWHATpfKmISvovDg-SYPWj94ZNf6MMUr329V6Glkoey6QE-DgNOxpAepIZy6wta6qM2oTkIcCK1uogMoksOI8qCZ6LoTXukwUGAdQ122TzhmXkIBBJTtjzSTAoHwoLvox8YeAamZIgaHcjRDeKmF-9E8Lt-jlYKlc-IF8wrUXo_n4zA_ww_KRbEEdnsOXD1NaHqBIu-Zlu40to6doGQ2QLc3_1L9CV8L7LG-3TGgPLM7hGl_8yqqqG1zGsi5S0d3kvf4HUFFPJ-BQ8u8yxeA78IzXBCUJzZ6zyU_TTXKGCBJCj1rrY_-Iu3TEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlfOHRTBSEdVSMnRJw7p6RYeNeuJWMYaGtTB0MQUQcm-T-3UFp0qRmhCRsUPIl2sFtx9A7VWrxqIinDXmDoylnQWYC3gOeLV7b_9GeVA5t6R5HlJY6EKGr3NjPdDCH7aEnn0wkmeH0VzRh-YwCv6TaNuAmFOpOgzgBJ8LiSiqjpzzHmLnVYYvqViv3VC-FWtGNmAk5ujeMuV7ICMQALsO1-3pujdpBSWcxPREi_D-l2dxHngM18xQVIQv9H4a28IH1jb8etKDJe5aZcY7_AbMqXqFi7JvodJBvjZuTUAvcIcB6RRc3fw1vXcn-70vLsM-JjEbdoWCldC9i8ZP1LxKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psDR9MqesOfJyO52Dbilnqnr_jUbf0gB3r_Havu4weqKphFSflJ99zCeiN2O1LAbL9_gwkIC85Vuk-xt4ijZz2nOQas2JOigQc7CVRF7f0g_VqqNhgKqdnzx_RhtPOZ13eh3L-qUmrYWfc9dViXkr4ao5EO3nXHII8DbJgpt5VYGYpv2YxNtUNkk-Ge449I713oq-yOr_zBAnzyUftK72x183uaTgX-rUmF00l3LHhT5ROdvtRjgnidzSgrW4W-eFPPJt8O5IhVPRSyre2XahXV2BnY3LSttMjXSXX6XhYsj7wAJQ2mBE6pqgvitvgvyN_joPNYTVbiSKChnVwS3bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=qKaOD5kXGoUjTfRTGrCAnLcPgRgnEw4YVtLQ13i9Zq6g6VIgYd-_M7bEIBoRLqtqM3nwG1nfF8pWQEzl88X3UaRL-Yv5aZ-wht4OJqXzCoRDdX4Wk7NKBvnwXcDFbuzckxZwz9DQ0MTK4O6c7gyDekOfYk37kfe1AzQQMM6mF2xeJL__VwK_nhGHkns7zz3wGBO5wJccs-qLL1yy3bup6imh0bn7uzmR7hMCbeuEcY6jOGFCO5qyE2z88nGFgk6NUV9RmuZusGEHwM0mIQl3tCQVo3SC1NCGuXgZ6MSKI_Oc4_L_dh8RJZ3uCXR0ZNzZ8ULt84W4HPe9C90brGLhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=qKaOD5kXGoUjTfRTGrCAnLcPgRgnEw4YVtLQ13i9Zq6g6VIgYd-_M7bEIBoRLqtqM3nwG1nfF8pWQEzl88X3UaRL-Yv5aZ-wht4OJqXzCoRDdX4Wk7NKBvnwXcDFbuzckxZwz9DQ0MTK4O6c7gyDekOfYk37kfe1AzQQMM6mF2xeJL__VwK_nhGHkns7zz3wGBO5wJccs-qLL1yy3bup6imh0bn7uzmR7hMCbeuEcY6jOGFCO5qyE2z88nGFgk6NUV9RmuZusGEHwM0mIQl3tCQVo3SC1NCGuXgZ6MSKI_Oc4_L_dh8RJZ3uCXR0ZNzZ8ULt84W4HPe9C90brGLhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVUpGa8yG_hWXCipHencAxChbFE7ZlphUmY5UFQfOjcz0BSz_pxV-NQAp0O5kETph3rsit24Kr0G3wrNzvnjfH6mxnjBhotUNoL-km5JAfzcj5V6SJXygMEoFUpDsCX6JLiGAchQQN1za-yvKcdnVDud1umFmcckV5sNcIbLwNZyK2CNSz5qc5oaIB6dy3eW_0pXYhev5EBavzKzdn8i7rGZ7fY0iHCh63mXBnthG0X-MXqXf4hYyw7CyZVRiPMLeywgWq1UPnM4nQ6V98Ewx4WVZs6QGEF0DkxAND-3vu0w2S96WswVfeIql_xR9CVhQ4tuR9R67EKl0c2WeKb1gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHK32ACUtVBVocgSq6ULRbeM7_jiLgju74UBbIYdeYafXhq57we516TWNbsZWAfYgtInv5hs91OTyYY6anlmJHj3-EqFnCVjxp00Sr0Yqh5bs2C3RFl_QJQsvHIn3Am9NaU6t8Y6u4B9JvrUeKH8mzsbsclY6SCHnwB_nwym_kqTfz9lN-Zk38OlDO8Thrs1ZcHwXFoM6VCrDnMUwXx0NCa2mqJvyihRV-cGizza3-CialRoy87_FjxSpAai68bKKwh9MyEhI5NuLo-QSi7jgArR9lXKiuXcnSP7SrVHAALF1nXiMtqDujEj_xd73AAnn7WE6ucC0SyDrH9UnFy7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=PQOIF96F0dSNEMXwjRiFWKOnPA5KDXd6_9ycVOmFVg6bEqO1hEShC-a8NZFrEZIiP-qfBHoF2PdnXukrySeUT3fibHNWjnEiiCgpUQqXXOsT8N0btX8tcoxT56ZAumtLkObP5LYY30_BIspcUl6fgly9LQ33jolD-BEHx-Ok3HBcE14k5mYJ4pSSYgQTc-p0JWarvyA6gHa5fGPOGA_Ur3IEcwcJe_dgaYHJhqBK_UDkLAba-e6wiTctdFeA7rxcVWl1A4FdYLqY7uHtibYuCtmcQBA11wLikaX3iHhPmcKAefdCGsR5TlzvFWFkC9CRTrf01m7jNDNe7eSm4KVPpBbQ9EkaKvgo22X5ODh9phL62Bq6rqMSFus3zb88xuS1Ol2Tkhd2cy7m86lCFPrq8f1kw3NW3ye5ArFbaY42djecsGK13dLrKd44BPrFGemJLC83gb3Pf81cIhzpnrDjbbUFi1g5CUsRJ0dsvfb89ISh4_UwRPT3dO6DluO7Qr51HMZ5tfxCe2cBecMCq50kx8t10kCRRS-eop4UhdmlP4J-z0EyXGnvdIDnVL-DOMYDdmZalxV3vOw8P06j1xkCEOz_2FAnWJu6OgUW9mRX1It5rtxXrotSDrdOmT12MMNiOKYCEKa4AqrOqNYC_i63FrcplcPmUp2PoZNPfNVYKSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=PQOIF96F0dSNEMXwjRiFWKOnPA5KDXd6_9ycVOmFVg6bEqO1hEShC-a8NZFrEZIiP-qfBHoF2PdnXukrySeUT3fibHNWjnEiiCgpUQqXXOsT8N0btX8tcoxT56ZAumtLkObP5LYY30_BIspcUl6fgly9LQ33jolD-BEHx-Ok3HBcE14k5mYJ4pSSYgQTc-p0JWarvyA6gHa5fGPOGA_Ur3IEcwcJe_dgaYHJhqBK_UDkLAba-e6wiTctdFeA7rxcVWl1A4FdYLqY7uHtibYuCtmcQBA11wLikaX3iHhPmcKAefdCGsR5TlzvFWFkC9CRTrf01m7jNDNe7eSm4KVPpBbQ9EkaKvgo22X5ODh9phL62Bq6rqMSFus3zb88xuS1Ol2Tkhd2cy7m86lCFPrq8f1kw3NW3ye5ArFbaY42djecsGK13dLrKd44BPrFGemJLC83gb3Pf81cIhzpnrDjbbUFi1g5CUsRJ0dsvfb89ISh4_UwRPT3dO6DluO7Qr51HMZ5tfxCe2cBecMCq50kx8t10kCRRS-eop4UhdmlP4J-z0EyXGnvdIDnVL-DOMYDdmZalxV3vOw8P06j1xkCEOz_2FAnWJu6OgUW9mRX1It5rtxXrotSDrdOmT12MMNiOKYCEKa4AqrOqNYC_i63FrcplcPmUp2PoZNPfNVYKSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=BDk0ajvyCmSEZYWXIGMtvkeg32pY-BQAuXgIbRBsG4pPVrFmHFUzBG_bin96huz1cEdQxf7-a_khs67LxZ3HKRiQOUY2cW84VCXcTDl1SS_QHwo1IOtWecHFU7uU9AKRMru3Hp1TsySTFWbVIP8NOvjvHS9edOr-Bw5Q_GgdnMZLwPuBBQAbkNftxoyt1CesQ-QKGDxYxcxF9QoUfpvKQrt0f3R7QqhYuyGr1pNHMce7LLeLmRRNHitixGTTp2tpv5uh9qxt3LyCivC8I1iWJ06D6HinuPBnZ96QPJB6nyLiS73JOyVvuoWKrbH_l-0Oze6Hl8qcl2FX4Xy069qIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=BDk0ajvyCmSEZYWXIGMtvkeg32pY-BQAuXgIbRBsG4pPVrFmHFUzBG_bin96huz1cEdQxf7-a_khs67LxZ3HKRiQOUY2cW84VCXcTDl1SS_QHwo1IOtWecHFU7uU9AKRMru3Hp1TsySTFWbVIP8NOvjvHS9edOr-Bw5Q_GgdnMZLwPuBBQAbkNftxoyt1CesQ-QKGDxYxcxF9QoUfpvKQrt0f3R7QqhYuyGr1pNHMce7LLeLmRRNHitixGTTp2tpv5uh9qxt3LyCivC8I1iWJ06D6HinuPBnZ96QPJB6nyLiS73JOyVvuoWKrbH_l-0Oze6Hl8qcl2FX4Xy069qIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjLKBPkYktLb2tDHXCcylSsgKupGebOjmjh9I9YN9KSzh7AjcvWPMnJV_YWQsOEUuZ4Y5PDQHwdMyObO06ezZxaFLIUKdhvOjGAzLjsgTQKvA9iXkw_FPf9FM-ZjNOTvLuwq8tuW0FeWC66cnC09qVYoywW4C3DCKQFMmXLnXNP6GCDwMUqFP8Kx6PJMrQ3VIbM5bTqdtG8CLdfrBI9-I8ObzYev5deRY0sblu6Sll1mBpnXa2wp3w3STwsQ6nyJAquX7Oe4Eh1tNlvQQt1O0udvQ6KBXzlFihMiP0NYv0jJwJ1P3WHG_kUZJu5U20_-OlVGrCk78D589k3Y5Ve94Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtiX5MCpvlsDEaxVW_IYEThoSzJudOcl8DXvPIqui12tkWwk5ulzvarHsjkHpNR91RbEdrBTeJk9omoq3Wi11Qs6izUmr6BIP3shJST3AoN6zTjoX1DSN-pZMuF6EScf10zZx0EQMqZfN0Th_QZIWUNpIKMavaKqY3HcLivPMNEeYgKUv0mgrugy9gxe49435IDIeJYzGw5f_XedXB5y_GlrzRtX_6y0_sQCXzAPCztO7ceXvsJj5I4_AB74OHdi3y9280WKWYYrIT2FTMPBLXaxs-6ZOanncXqrYvjxK3k7d6SfVQ7OmYAjMRda0Uzsqz2GYdCG4kUOkTBPd5YqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URGDzX8Xqtvl6hDAvww_a2IU3TRSYRzR9cODpvD84pxXlfmq99Np_ex8iRL-qqA9AP40JWYEfg1CNTmi9Uzydr0q153zZPyxGRr-OaFXbekkxe1GHnMTVeLhukduA1WgpYMmk5zh9829rBcHt9omJs7t62ZXqQwg32J0zfSH4nT-VrUqK5roGygmPHm377fEkojL7-sFumHMTcoZhit55KHE6g5mszF-gwANqe0XSoZam0AFHruj5HKP7PZIbknNXmZbvGXOoirxtpMh35lbqYvLKLSjRvXiMybw2vCzSjdqAelX_nYzJUyBWSMH6k6mu5WCDO1eWRN7BUJpPM_oeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0FpXPlRsKmo7-CgBnr5_eg-2zbQM0O5aTtYBIjhF7TwNJNkuY8b4VK2wRONNvbJ9dUtGoFqJgaX3JEk1RlXlYSgrQs82fX7XM0kQBnmd2lrXZqU9_BVnBkP034IF8EkZH-AeD6XnJjdWhMkZEsSAC5v64yO8JTP5RpKVRCmDrRwyzVXbDFhIMC6D9oUs_zGL7yiqARAeDb8Q5ybcxV6VNRwA_IOVhBEQ7oNOv1OlbN7WIk2d-4ARHpJG6vgAyTM-pb5CbEITIPuzJgUYZ9fuoPZlvpvUAHeX72lZJIsKw4TyqRyvJPUm448HvHKzQaHRYJOlVFkDtJYceakKdzCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4TyAYcWmbnzhiUKe4CzEw3zkTd2wDTYwKUNluC4Ym8gv45ugbgdzqkCgOohSOZ0-fJUbYki7uLxFgFkbKjw_UBaTpUFwEL1WKo_ELVktj9HBEuicwPcPVvVrqDrd4xvaQ_obD89lGqTaTFxDWIxYrw4aApa_eGzKIVdsI7JnGpCBoRK9ckT5hfsAxIvT1mwbvNUKmjWBI-hT2SK_eaxCm1R0gUtpxv7I3mbwlE1BoI4E8TMnfE1DTb0ryAh4remRIvwfP1CsXCDowR8-M6L0uryWbOtUkJxb7wdCZ90RDAsKgQSoiNtGoG1vTp4nXLGxQIVHwRZBvGA2gL205xtlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usABUfZ13Ubf9tMLdmYbDKqqFw8QWO8fRCUwqGNFqcxqs4uRuNxNNwhq4V5thEYt0-jROA8LPjE1vr_R1UtweUn8JHZbFopGW1Orm8oJEeHQ4Suaz3P0dZrBvilpANSbpwi4b2vVMVWXG8b8tMlGwm9DzQzzhvW5bklZCr3UcfPCGVttC2qgTcGARqq3wpw-1QXZolvNPjXF8NpJGDzTeH9C3sMCIfVW8xhpy8zB6atS7hdMeI18RTKO8ChB5F0fVh5TcG3s1LYMuhNHWD5iRiQISojsgQt-FAiQF4z5TTGCzD4lT3DFQnyESzD15c4sd0itN9ztBr4j-4H_7kPw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNnQtXpXs8hsXmmVP2i-1-Wc0qNFNJK_ZfUiJNVAtEgYwpD02HmHPehq_tOZJ8ZDWsqpQd3eyk4L5Z40CLil-ZssPdmyS4d2VoTD1gJB1eNqor3juKvOeDTxsEVGdB9I4xLPlc7f686JtwdSXOuanI9CgKIdBRDmd4CUC9FLbsyCX8qDfd73Qlg_opwrxJDASubIGx0YJQKo9LtIYQbEK5OLeUpzc6SF1wARt8DizUkwvQ7ugCvBuGpX2q6C2oC8VUADBwQhFr3yTR2QtyO7M_eEfgP0OgpfEZ9hc8HYzdqaQwKGivXJm4V4Ux_37YX6dMP_4QOfb7wYV5b_cjWGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyo0Qmmg2dX6NSwB-gX4WU-xVeDwszAd1C4C4gPRheRc98myygoscWVN72096Dv37hLWtJ-XIHrV0dKuS8zTwchaqGzCnlFcB6VERNJnpWqE_rNX73oMnsmqBI72c3gPNlS3_FhD3tPPSSn4W-lhcIDwtNmCR8qcvG10pV_zf6X48OFbLEqRRRwN_IlFN1xLSFjAh7fC-uWiDjBCEH71mYkjdo3YkXRSlQMy4XtfVBXEDYU6jTzqupDEjPBD6dSvYloVXwujyZ2cJ30xftTl0ERISYf_4sLZ4yTf7bFd5vF17Z-UrHfdmEgvNw5xhi68v3tuaMWHOqUK7CXnxxJ8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTvBuwaxKd3lY2JC2ObOYX_qczdwbbbKx8KNIFfehoI0dlPxCNWKVG7r4wVux_Lb8DeJtcxCvjlexWMAPZnBnWcF6IT5zpa6nmbXy7Ego6M-IoSCOZlFVzwSv1-FDKxDsBChEaKksV5GI3HKtmtc0vcfJj2UktHsmAECuX1xPOBK_I1PhZVvp9lPxRqMarjcWdh6Aj229R9Br91YAXyFew0gAB6wUxIRs51RMAElutwshwhLzFKgFwPnft8V1fw1h05yZ2lidxxqjlcTFu1nTr4B5aYMUN_Hbs4VM-JLuCjUL6ff7xKnD9_7gHnXBZmLfHzmL2QaS-WBBv2nppstLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmTbeynUQAr9pTaoMOHE69360qpAWGADMFjG_-XUgbTZOyxgzODXu1R-ePQnBiEal5AwH-hVkmbvXfMC5CGV0BzjPX_ICSG3fALYKzV3thinEgTyzLL0F8QzVkBP5tK5ENep_h1JNO1dMlxegjSW5cGH2jf_bvwMDpyh8cwVljt5E3mdF0gERAOGPERslvN1Kxq2lhkoNWfN4di0lS3cbIxm_9uUM-HrWuBJhl7PEi0MuH9eFRMpSYKhUpe34JAZ9Hda3x_ekTYZZHzRIFGPakr93_yd-BYyn_14WJMTK9DaFmLgoscJnAFH4ChJsSzHrFY0ZCAyogKYHiKS2WwjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxWBk3DYs1oPoWw14aiWdRmjqz8NoIcf5M7rFqR7WWJ0IAnG6nuGZUNZ1OM5ItOjREhTXVC_DZU5E5iwHyeZDGfL5vB2r_0V4DGw7gYLO4c2xiIzOXCDTL8zjjzLVqBF1r4FIIOAMlwWdmjRjV66Vli0mD_pvRvWDOOZnrQbYQ4_x0mksqR5FyEaqcoplqgv4mC9ndApoxEPRnw1Aeg6XD7SawxYut-UvdcZs06jna3nZvLAwqRSTAp3TNhWXupGt0Gw3vy1zfYeFs6Z4Pkm3mkTeIG1yeCHjs5VbM7iKdVzmWhvrn--nb8Dh-N3sKXLJtyB6IYzED1-iebG2gNjvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpnTunS6fUO84aHXSRAOcEDjCwydb4Z3cupGFZ-UeK9HKmiCsKloWW_JLpq2Ie0UebQqjbmopr0u-exy-Gsa77L02uMk0_uf3Ljn9xi5QtEt50AUos4WckFGFC4w1WXYw86WSax-LBOh1xOPsiwMTTyczr81lLOcuoSlAFa2zD4wMVH_sq5HttxH3-qVmkWi5V77ToKvv32M2bwpTzpnKQ1JBqSAvw40VrKzV0ZlmPSqAU-pu_8FIRndQXY6mEoN4xhhK8B7ZozjGy2YL1g-HgHcnlT68IJbYhIMTDEunVALComkiWTt7EVBS-hCGOwFU8QzbOEk3q65_tOZcSqw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=MtV_itQZAg4xXWcTaqF_Pu_Ids1BTKBhTJl3T0kiKDz2P-KeUsszyv002nGjDegokwI3GzMmbrtYMDoEQec1iaKznhcI0EvG_d9e1VSgJ8sy3leBav1gOO2P3BOZZ4-dtlC6j2Mxs9Mhgva8Ra9qb6PQdR7WU27gfaMgqVmb6s_a2KeAfyekxbb7WiRZiOHbM2Q25ak9GKzBaBYOzEzhhV6kydLtDs_O_rZFePYcJh2uE3bSbH3K4Fmp39_3tyWyShMdEf5EkZGzUm5lNGjTM2Sxnh4bzuanJxlQTtneebFUUUwrOWCrmn1985ruOG8G2Oel2vNDmn11a_w4e0q9TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=MtV_itQZAg4xXWcTaqF_Pu_Ids1BTKBhTJl3T0kiKDz2P-KeUsszyv002nGjDegokwI3GzMmbrtYMDoEQec1iaKznhcI0EvG_d9e1VSgJ8sy3leBav1gOO2P3BOZZ4-dtlC6j2Mxs9Mhgva8Ra9qb6PQdR7WU27gfaMgqVmb6s_a2KeAfyekxbb7WiRZiOHbM2Q25ak9GKzBaBYOzEzhhV6kydLtDs_O_rZFePYcJh2uE3bSbH3K4Fmp39_3tyWyShMdEf5EkZGzUm5lNGjTM2Sxnh4bzuanJxlQTtneebFUUUwrOWCrmn1985ruOG8G2Oel2vNDmn11a_w4e0q9TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryh_GF8hKBt9-pfN7MBiiAy3xe9oMTSaCKp8ol9gdvkdh-Ot_nrQgvWfjZdwzmJ7OqjjL2acr0if67sLN4w8hHZal-3yxXK-knpZe2jOCtXBfZtNBX575VGqxVdFdsl93j9K-Z3LednHLFE2QDH_IlYecLMzfJny6E-4UPLOqnvQR6RlO9OYd3GrVUnJuASJ2Dtai5uOwxCuDeADD_B8jdpFAdM4KcPmBh7luuoyA5Ie-1JTIroUoWpVoTZdGJaKe2hAmixL5eyoqebhf7oRoHF9WEeFars4VF07uwOiwWwHR2pDtWkN7KszBH3EOsH4AKz1fMy825A15a4Gd1kKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxsNmNCoP0IOgCuZfpzv9-ctmWjJKiOaPHf3JfhJGrOUeR4rBZRgCnTA3GY6HLYxikCP-76AFehJf90MqTu0BmMc4BLKgZ3-8xgsNSBhYR8383q_fegOMGeTv7K-CwvGq8z2Af7J9GnYoTdAJ4nNKL1ZZKlZ1pb2x4mXmWE5C9lpK5OkIxHG9YJtC_h5j_BIfcLaZzYQpe3j95MV_YMwbcx9BawNxGMnmSCPD1rCyn0xdQ5ZXXzDKqs2467E0VrE4_Z0OPObdki8LqYUXhoFWEmSOW-iBxfQaZaVUOmliWOaD0DSBV8bf_ibCJQohM6l5sMpyCIvEbWOJxuBALKBiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBY6aobFJkduZYRtOAIwtKa02e8CZmmAZv8ZupYO-TdBOyEDr4VTiLe_sV3M72sZ2RqMFHzygSoApXrtneZBt_Tfk4xgcwzmfwWDdZKoVL04_qKcmCz93uzGh-QNXp2QbslIO0_rSUOvvYwcRe3f19NoFsft9tZduhQEXHU2C1IG9mlBBoCPwWmzKRPjaP5wanAnip6F7_-bxmAVSyFadA4IsOB2I58379fz7_FnEMIHMsB2PXk1aMaPHem23dQJqACAmfC3m8xnZACB2PZIWh40UaThw5KIC9-mIdOFOnn_IJUS7Ty_eoM6M4NdmxETvjqhj279OrtGv_LPZdFExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3jh6DbYxjqhpHccVZoVl_jp6XZUCIhFTyeBMEWK97BVElDRMSBCKJ0XI6-A9AMOQ1TosMOxYN10fgVz7u7FoFaG0b1wLLjdmRIznhzHQtXayCWbGDVA1OMIdpruN9sR8eP_upH7vx4Ko4kACP7IoYnjTj8PmDwlSMEDnTw_6m9F9kyudTh7lOmuaYKcdposp-GkkM5cUHOr7ULQ83duvghV8XDQ9UHdO9R66TJ4P7ckCgB1IJn23PmNYTqlFZvBLFJXuCRr-mCA636Img8AG66Le2TME4qI5KNDjiAOrqIOH0KMXwnlcLAcbIt-0Nr9FHh4d0k_g27U_pi9oZ2Cnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=rOqN1R3SFPwi588F8ooy5HVAdQzdjIVmeXxFiSzsex1y51H8oT9yI2B_7C5SViSbrdsKrm5UfmgIlBfFaP1xDaVTqnFXFUYfabvyEVGLXGnphDJpjcLnVBgD-CBcKiMX6Jymmg0QWxQ6g1BBCnO81XiAdMbYKUNeNwxRJRQotZDkD3L8pzCzRTOai08JeBPJS0R1F6zLzN8CSssGEDcTVX8AzsEvD1C9CjeBTBIbkG0wgSx9AWk1w3w8YpTZV8s_l0o0Dk50IR7KYMMpbxjMY_ZM8El3a8H7Vf7rm8yoGU1w7AaXuUNb38OJ9lNxizoLPzVHo6VoHlPjIdP1BBuadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=rOqN1R3SFPwi588F8ooy5HVAdQzdjIVmeXxFiSzsex1y51H8oT9yI2B_7C5SViSbrdsKrm5UfmgIlBfFaP1xDaVTqnFXFUYfabvyEVGLXGnphDJpjcLnVBgD-CBcKiMX6Jymmg0QWxQ6g1BBCnO81XiAdMbYKUNeNwxRJRQotZDkD3L8pzCzRTOai08JeBPJS0R1F6zLzN8CSssGEDcTVX8AzsEvD1C9CjeBTBIbkG0wgSx9AWk1w3w8YpTZV8s_l0o0Dk50IR7KYMMpbxjMY_ZM8El3a8H7Vf7rm8yoGU1w7AaXuUNb38OJ9lNxizoLPzVHo6VoHlPjIdP1BBuadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRVvtzEcYjbJYBya82FrHFPj05CE_5qzBw98vIhWsEHFgjY-ZZ4uXZJkX-giTR_B44KDYfmbgMtkpocfUBq3dxkUP0RNBKIbv_AFRanOnSntsLuLbkLi6J1DlazpKwdpaKqA09JIlce0xuDnJVM_mn1JWrANY1wiSESx2WPiNeiTLxKG72WOzVygS0vFP4zKcy_gr7fCTHbiDeNqaicRqNrKJ76ZeZ2iCI7PWYoWtftQP0kBoyZJ2WotA7sltvh0g-5mR7-Nol8ul-S39XWPxQpecyjGylknPO4RPXR8j0CJARpvzKsz3UORi-0CpVHomVTwSsZVy06s5PTTuEauwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOwf5heABpV5_GXHI1_VLkZyVhriuKXdRhcw2ShMM04G_xHmRwaO9VFEBO5xuZQyiD4E_uOjA1fgJ7VLpzggFmG81B-n-jtyEa2r2w-6rc6c3ap5GCdUjzrGpAtR2nL0QCjCIyeC5fQPbtvFrIGAWV24shoFw4kPI3zeIlMnAdjFgPp0wq9UqcNx3QIKKA9o-7-fUAD-jxsWGR0E3Lwa525j_hiSuBd_mroV6E4P7VIOjwza80YMXR2ZzT0Lm3q3f4t9OffJ8cFPPkm7NZsy7IY9DOTMu-67OAjtTFvLKBnvteLMLyLdK5C_vyCknFHTiy3bcwytMtxIOfxG0kQHsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up6Kmo1Lj_dCbVphGr-Pt0d1mdAR-6WzwYTmuy_6UMAfGJdTqFhi9iuZM5XCCWy754zG2yOwg4vT-zCdEznyJTVUcX2wnYzcThlg0eO0FdYn2pVVt02gniIokpc8RaSQyW_JrjouWek24Fu8zH7NM-nxu2Xj7kSOKJpmmFgAujn83pjTAFu7t4LakTGH3kVsPvVvUoCsd4lPmffpXkcTOMWBc4pm0sEJc2x8J8ECKHVLPLXP8EV-_jAbv3R8DzCpo15F07KwUSLNlnW06chWhPxKVms1nBIurceXnk6etYffq3Uc_KhsIyAdqD5BEUb_2VEXWUGmKkWcCUizN-f0kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-bM8MEILyjWaizu7Z_E0kJms4fOQnPQLsB0DaArXJMFrJAFN-KWa_3C_8ugAWx8xpf0Xjehu0CbZvu8WdVTiY5PFeNKgOsX1eBxJF53dwRnb7Pu-I2auwQPW8x1vAqlPSmYsWbrTRQKhNgLchVLpE9_LlhVEkjTFnrbXvXwockj1ClhbDDy8RzGPZ14jRWbioNEN7WFBlRENemygqierhJ9Ph2AutSSby9oRjmai6lzqGR-M3rrKCBUM6K8OMwbfF_Wb2LQTmO7KVefTZ3_5cll1xY3djnUznK0fPrMEtDmpLQrkhfN_HQKRt2zLQ0f5UN-zZ3CYEDZy_mj2vY7_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=vlS-ve9rH-6ceFUEV0upaUHO4DhagkBHT1-tOSQ_jS4r1yUmPnshIdX1P2yHQkT_Wi6D8yvZdsVK5K9FtvBcT-etJAxR4N4HPl1g8FZgY2WCWU7Orq-2mCY6_-kTAOg2A6TNNIyPmY_bgHJRhwZb8T1JXcEy2B660BYitopl3AH5OB6vrdgJyIuKHXGQQSsgwS-ph9kXu60cktjzITC_O-3yYZ3-CISDdZGPAB_Oaw_pfl4sbcGuCX0ZXfseMcWBLhqKbVtPYvnLBu8BGwbkOXpkNx18h_OZPMDVvhSnHBXk7L5SQmqcY0qeWiUhayxL2uh3h2hgzsqKabkOXsdf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=vlS-ve9rH-6ceFUEV0upaUHO4DhagkBHT1-tOSQ_jS4r1yUmPnshIdX1P2yHQkT_Wi6D8yvZdsVK5K9FtvBcT-etJAxR4N4HPl1g8FZgY2WCWU7Orq-2mCY6_-kTAOg2A6TNNIyPmY_bgHJRhwZb8T1JXcEy2B660BYitopl3AH5OB6vrdgJyIuKHXGQQSsgwS-ph9kXu60cktjzITC_O-3yYZ3-CISDdZGPAB_Oaw_pfl4sbcGuCX0ZXfseMcWBLhqKbVtPYvnLBu8BGwbkOXpkNx18h_OZPMDVvhSnHBXk7L5SQmqcY0qeWiUhayxL2uh3h2hgzsqKabkOXsdf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwz5t55xAnl5gTdly87pjitduWYpv6RLKPA27PFvu_LnBMPdxqiPUg15YVnKOXNMbmu_-uWNjPvVB-QQa6HNFKpmHP4cPq0CoVyTxePHmpc-FgzNNrMszjEmtwEYfCA1FMSHFmYBTS88poTPZ0cggb-FWUD6dG_27UYOqKp7cCoeIPXcW4rkW91qek0A0L5TtCmTsUCu1fRmJ1Hv18E_Ay2_zk8RxbPbsDMDSiy3HgCG3piwlD795LHmCADv9Gf9QbGeYgd5FUhT0PwD3uT6MDKMsuuVqSAf1WgcerCTP7L0db_dpl-NdE02tEmuxPmR2qcozGmNMgP-9Kh1_Xyc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWLtgbfMjy2_VBIYYFiRFD3cflOI5aKN1ZFqaD68_4z9FNhjdU4M64j5ue-maMbpeK-H6nkxalti8icQxZU3MvCe-qRdZi-ydCKzP-KbSS79mF0Tyo1Qzfu3h8a1svJISMhXVDoqPHE0TkzM10dcWWbU8E9whvvUymh_t8gjwS39wBXBzjXI4MjAnJEmBZX9SEc6ZIxHDU_SLBqwOnThbmIk41dkf6Kb1eQzm4v2B6-jrgSN0CwEMAsqTKkxjmbSWA_H0imkeQg1PopT3GppEgGY3haGbS7ARKceNzuACvfaRBCgFaC9seu0q6bwQts1ooQCXGhnA6FpQuSHW_IhGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQn1xH1niYbpiezqYrQuXH84v01QkSffmRAjgcddZ8GHspP2UuZlrUxbbNaO7whBEw4W6QKFfel0DMUweT9Tu_sX86KEL3EmAube5Mxky2b1CzUX3XygZwTQKhc-b0mqz4F1pVoTz3bKRTssWhiejyKr84bWoI22_jD4Hx10Q_P7PHRz9NkoyjAPsMarL50_oDToli4c69JA7RlucQcooqkLQEdyrs9ew7qqr8ZARioDeId4q0FO7u6VAkMWhxf9VKJbrVHz4We4ET4WEbLiA2QUhZxA-bCXQaljB5RoB5-J0vSrjbzA3NkfaMuneWY-9RfreEAuKuhygG3w_aiGFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwYdF-OJ44qKjjqjHkn2f17TtAZZLBgJJ6sCU6Lh8bKanMPMeh0XIr9UwlQVvWY1Qn5yEHDqOx0qIsuAl7Gkg8MuX5b2INDN1dc9fICk7ucQQJwS1j9Yn9UjKxnRatT09O2-3F0H-qnCMzzAyXwqWvW5LKzVR4sb3YDbt8RsbOFuMIT0n3yReDPRP3j_59UsC4DmNfmn8Suk_nQ7KeOURhtr5wM3R6PeCVD8jEnj1AdjvETvzzq78H4mPUeSHOdbSl62F-YEyvdxemgQp39UI947XUp8Al6pOi2rggmZ9Fu0u8-SrkPRP1KmiwZRBG0Mp0rHkEEugFGjtA-CIwXUwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AigbqTQkj49hHSmDku2ynDzjbn3hzgYbd6iFGahC1q2TLVe9LI2gq-CtwmwLvcQiOSZuFQjnaciyARZT2bqqkFklrvGv79SHBcDxXeKs1CnU1FY1wSbP4zYQAGVdHoxkB4qfZeCB33vQ2i6GNsY4L0Hu9nIJaJT5OELGd1q2ccV95_blDXZtOo3Wn3Ubx-IOX7uQLc7sTuq7h8LivxjDHupdddRrrWVbWplB4Iq4CWieRirHIjnXSwufWyQHsNAaUlQpSTwSxlgE1wsHWyA1BGmzo3PBh00_x5AWUXZWJ3kf23M3RjpHJqpENbFkZXEyROcrwDXS3hIie4tKN2DRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul5vnxCxrLvK7Y8PPCGOwgrtaF8KYB-2k7tr9j76dWjlHb_qTOZo7q2Rv93QCmWX3dZoSX4EJ-0HDtfqgZwzx7sE7en81s6LRQCvFWw_Je_8CEXLu9iT2zcAHgvQZV0e5znYyYqL26sSvV2xDKIt8rgHbpvRF7mc5Nj3Mg1c53ZPMyoivtf4zUL_g7OC4PXRredX3Gii9HzYgoh4mLZN1I1xOw1ZaS8GkCoK_w6wxFh6gBQELsoaj3awkJjkThE1cEdN5qxi8rTv21Y0GVKVYM7lHX1YfJ9tkWhs6by5rDcqo3FDT_PabcsqySGsoe42iK33p-HwWHRH2bL5YkjKYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=jEk-ADRHfuOBDVE98MJW56RPEwGOg_soRXo8zXoZR068Pl5sTNE2OZeRdGemVTpiFvGBqjyZcUjFQBrBfPTS3NMT_jNfowUutQe9C6J-FR9tk-PjEg6whKZgN-_NGjo19N6tcEI4eLcEssMGyn9pJpbHwmck0yVG8eTEhOmgb092nO2ozeBOEYk8pCkpQNSiPGiT0LczFZma_gXsUExH1B4tyeywsDIdxopAvl56cS2vKpJxbOVGm6iH6aBXPEdCqHVpvno8bxJA_JX2kGaYuPMnP9NuBNLBhbckaVe1356_d2OXdrOShPoteZd8eoTZ8Pvo25pXlbAThLmWBlcYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=jEk-ADRHfuOBDVE98MJW56RPEwGOg_soRXo8zXoZR068Pl5sTNE2OZeRdGemVTpiFvGBqjyZcUjFQBrBfPTS3NMT_jNfowUutQe9C6J-FR9tk-PjEg6whKZgN-_NGjo19N6tcEI4eLcEssMGyn9pJpbHwmck0yVG8eTEhOmgb092nO2ozeBOEYk8pCkpQNSiPGiT0LczFZma_gXsUExH1B4tyeywsDIdxopAvl56cS2vKpJxbOVGm6iH6aBXPEdCqHVpvno8bxJA_JX2kGaYuPMnP9NuBNLBhbckaVe1356_d2OXdrOShPoteZd8eoTZ8Pvo25pXlbAThLmWBlcYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMaXXvlliwkhoyktPo8U89B7v6GpjYdIeYc7e99c04FT6V8z1CABUdCLI-GrYsWgeLSltgVGkKdWcIAC0MEdNI7vDz9SQAAUX-5HCBswA6bLa2kkzfoeGCuFaegAJKcnknx3y9XtSPkZkXCRGA7BXVVSETwfsPjjUN8_mvdBBoGobhYaa2Bdj696-vLgLrzGetl--k136BKhtk3OJZTj5wk-gvAvGvV-U1XdOSUm3SY2cqj5NMy3QQb0nrUpPTwoqzlsizl_dBCJGruEgN9jo9dmHeIcrKEA084fRwzuJ-5j68sILCwCdhAm0t0uyCThiZPWS-XMWWXL5OuoZqwlJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7UV_hqbf9Z5Xa2nNynHIvgYChJoiMVfi4-q3YbWlJ-W-fwj4rMKYbDuydI1UJEpYY7ZejqzAkEEnMVlUNAnVEEF4eQX5Karysei2O1diZMJAYxt3g_Wh-LW6S_l69rtMvKFEYhI-y0Hd7k6pJ6T-xpiVO7ni7b4gRS_RoJPNidAV83ek4EX9gn9ERs1IDmKKVFQG0QmhK-ijnOrOXUBpbGJQytKRcVaNaa01SS6kPpDBBEx05QzPw65XgBcPJ3pRdImXI9PGzBhnvCfQtaS0lX-soIib6uog36YS3TFrH155l4apL87DBfqVY0W-9jJHNIXFu79GWPKzzDhZfuuNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
