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
<p>@archivetell • 👥 9.66K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DJBXirxaJmnjHvuUZ9uBb_TPmZn34LO-XZDtGTJmtNGdjL0wRkxtH4tWZFSMFeOwEGxTtUr0zat7iIONI2DpqWWcP-VI-rIcNh6Z2_g4JWH5ASqf6iQ_8pQXun30nd6iVrhf6crgPChLGmfj5J0ysqrQ6E1cWqWyA2lYvBJF7wnUHT22KEitYSzYO_ei-Frv2xmoNy7VI_7VOcFmhVuJsNwGL5ZXEmWxgfRTgYo6jwlbHrjWQZ39Zr0iB4HveHhnk-1jq1K3-O-D76KBrx1L45TSM-cJmy73hm-2eJ5oi6KVY-rg2W8xTpSO-lRr1kOfAfqIqUzgoRL1GdhRhcedvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba7a0dd75.mp4?token=DJBXirxaJmnjHvuUZ9uBb_TPmZn34LO-XZDtGTJmtNGdjL0wRkxtH4tWZFSMFeOwEGxTtUr0zat7iIONI2DpqWWcP-VI-rIcNh6Z2_g4JWH5ASqf6iQ_8pQXun30nd6iVrhf6crgPChLGmfj5J0ysqrQ6E1cWqWyA2lYvBJF7wnUHT22KEitYSzYO_ei-Frv2xmoNy7VI_7VOcFmhVuJsNwGL5ZXEmWxgfRTgYo6jwlbHrjWQZ39Zr0iB4HveHhnk-1jq1K3-O-D76KBrx1L45TSM-cJmy73hm-2eJ5oi6KVY-rg2W8xTpSO-lRr1kOfAfqIqUzgoRL1GdhRhcedvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
Open Design
یه نسخه اوپن‌سورس از Claude Designه که واقعاً به درد می‌خوره
😮‍💨
باهاش می‌تونی از روی یه پرامپت، سایت، دک، تصویر یا حتی موشن بسازی و بعد همون‌جا توی محیط امن ویرایشش کنی.
✨
چیزای مهمش:
• 150 تا design system آماده
• 260+ پلاگین
• پشتیبانی از Claude، Codex، Gemini، Copilot و بقیه
• خروجی HTML / PDF / PPTX / MP4
• همه‌چی لوکال و بدون قفل شدن به یه سرویس خاص
خلاصه اینکه: یه ابزار جدی برای طراحی با AI، نه فقط یه چت‌بات دیگه
👀
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 342 · <a href="https://t.me/archivetell/6434" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">با سلام درود رفقا میخوام یه ربات open vpn بیارم
دنبال پنل درست حسابیشم
اگه کسی پنلی داشت که بشه حجم و کاربر و ایناشو مشخص کرد ممنون میشم داخل کامنت همین پیام یا پیوی بگه ممنونم ازتون
@ArchiveTell</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/archivetell/6433" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6432" target="_blank">📅 22:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6431" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/6430" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6429">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/6429" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QP3DA36JOVPHclYGQIARYYL-_iSgoHwufRshZNt1Ettqww5GiGh-lpgF3l3z1MQIw1aneS5lR29CZHewbykzS_LQJ_LrXKDuQOY65TiDS-sLijlv67qzV-MoMhhNZtjJ3JAj93bLRUZY_Eek0h1GHMv1SlY8_wehXUVSTJ3V9wv3R2iADZafI_xQnf0wR39B3mZ-5RrF0V93Pxx6v50qOz425wLMMbp8MMho6cn-_of4EHy_zMWmC4Ofvt-LGwQTvlQhknAgmGAfZ8r0a59qM3heqoSSfn77DlvLPxTxyMhx5IY3XBGNheRvPUf1f2dWMMQzpxCwArbFacUezQaHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBSHiKYWrw7L2xCSlyPAc6dDTdQrpxSHW6YfsJf2SBXSQ3AV-E81xz9TZysYuRdjRBr0L3fUN_hFg2bYaoqwzjSR8jU0hXNwGAxWzsvPPbLyZU3A938soCq520DDUMJ8aOwvcji5DfVFdpY1nq3X5kGidVnwSoVEj8rtchnChRpDKsKIVAZcLmtzC3JKRcoKVDnTNZjqNFc8KVOB1rTzA1ndJrLlGqk7o-UgNesOYItWzNearVRq5Jr32BFUB58zcMUDrz3V1el7QZRkBj-bQpvCHjQ2jaGYraV-wLHfAoN57YWGX0rNJSC9bcwPTbFXBEmzw_H2D7pUorCeD8m7yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao7MvVsAgnu1gmlzCk3_Pc0mS52vKTf46t8-Aal101ujdtDL6nMW4B_dVbqXQbdfI-BecaZVWtofQWVNTRytFyOxFOdoFq20_bilIBXOoZnQ68N-ui3UckzftuH6bTivDYump-Tm8oiUoIKeTOG8BQFFlY4X_gLixgYKNiWGZEFADOnwcFusJah8W-W9OKqHCf4NbLUl6wjefgcJtRlbQHMacsqAWwCIkJrXEExA42ZRNGebzqCrTzlKX7FHv7Uyb8ll49Ij8HNZij3KQNvOoL0iZxZuyBLExdTephqITQK1w7kc-KLH1xuJxtAVhZjyWpxrgUH2BY28JWjgxmqZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQ5Riph3MIsLyOzZCWgioev0h_kkhwFqiCbda9eeuFjIycLWNshEZIpPK7IlcartRx_qvxeySmoFCRo_2l_iRkD94TdHZOpVTAJos4ji4P_Gkz1WQ9h1x4hDIXPV5Q1nGtS-MCDIhPsUis126-v2qK_aksCow9gC_dI1_DImKQpXoDRgMn_zUjDPa522a4UD5IBR_o9CHENSgqclRzEUdtGJzpj_yKJxkBql7SD20WQ3Tp12NrWVrlLYhzBnCc86GiKY4WuFesOnCP-BykCt42yZ_LnDefP9S93n-dxxfsB50Vv6yAFzmubPkzDh6oRAkqN2lZsK6xrpYqRZ219Wbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxX-MnmQB639zQoqtAzG8s9A8j3vjNkfhd6AojuPh3GDjYJ01rF-nXo9tgJ-zDNTpUYs--iQD0cDIqac2UWiaU8a_eKraSGQMM3G4FU6IG99jAGBvIjAqJTL49W-BT9HmoJqmaZMya6lMX3IjWo6K6cgq44BvTF0S8UuHew1xOXZi1HvKCe4vTTtxN4gmg_BD6IxxDdYdEjCyLkMKCPKY38aQxTtmD8VoSxlZMTrqOkyqljaN3H6Cm3MvtHXymeNLiPCwCwkoVmAxrd6si9Io1R9sss4xuaUcOYD3b2xOpCcovLuIeyZl3k8O9jdgotT6J0Awhie_gJEDhKP0fd7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRxymGKyL2y8hWXPU-rcfMDA0WCwLvYizHZ4nkzz_bJoRueKGfGNkNRjTTnVK1jvP4GZV00-mpuvZUL5wG1hcYDj4WnzHPT-VNJtFrtJBEMgGQeL8d4kkUpJ4J85UJXR-sMFm0OxmmqEgweIILp6PCHdS9u9LhtywZTtA_FrweGjPOEpmWWbJn80wIxq4PKib8bUvXW8dvWBW4WhMfB0ipxLKwwkrmwRtx0chS0oBEc7IukG4LjffA_tvzAcFDbwh8g6NZdNNBlMRhJbfUqVKJQqzqjzShvTAH4BoJZGFUT6k9Jv5EGeVKuKku2U1fxfwFiuBHNs9SRtg2ijQ52D6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت تصویر به‌علاوه کتابخانه عظیم پرامپت‌ها.
- طراحی‌ها، تصاویر، نقاشی‌ها و راهنمایی‌هایی را که توسط هوش مصنوعی و هنرمندان و طراحان برجسته جامعه ایجاد شده‌اند، مطالعه کنید.
http://Arthub.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjHlVjn-sw8cxTOxR171VV55Fcs6MKIgThmxh68tmht4JfVZcW94YrX-VdncHHREn2Np5K5DvsJrAAu5pJp5OIrRMES_yYpR1dHW3XRVdiSPYLV6r2Sn3R0yeGlZrk6485qz6LmG72sguZTl4nnpN0lLOQAwQWZ_OUpTpDTaYcWOySrlNAAg-OlbdUK6tLKzMEA0swWkuu8zrLv0BrAxB8nKsaR3lU3m2oKgNLdDC7u6eSgSpM-sIRPlpR5kBRZc5ishUBRmU9Dih3-3-qMekm9oNnZFZ7TMQambX5xjezGtgGAEAI1caLmFt4oeLfuDVkPchQISbpyrvpRm5xzLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4yhk1q1I-o9UOE5V5IV5H6qTRHf5kXSHRxcVeia1DddsF99-eUQdxpyxHBBhk17gyYSUtEwZOpHY0v4Jsq4EEpa9gnCulNQkk6fl1bGGOtlcm1dDDZ78GMlaZb8qRsX0GtUwGwy3oDqUtLFDpL80ZfCMu7bvtma10_d806hAs6TvkaN_whsbTKjI41kRgmyYo5Lp3YrMOWrLWGbZHz6cfoaYFQ3Q-9WLJDt2gfLZ8keDyGGqljMzKmGLutafEZw-edxgIWIorz4DOl3qhTeKRTwv3MWptMTPT9QnQVzoJ4oBOG7VGFe3xf_59v6aUM5zMcnzFaSvnTSJrrxkFrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tupNDSDBUmfXWZm3gkzcfHnLxoe6rszlHCjWwth7rnRoY_tFWz1eGZNVzlIXwYEFKn8o57JhfEEgBshKvqeMDr6BvuJCvP3kR7d7E1DnGtZjdDsfvhmTS2uYRKVFnLxl7wYVjilxbKuh_MA9Q2cZwJc3QCTi4LSZ6ggIgUfg-dEOvLprNSLwm_dWXHK2MWgIXJ2yvW1TayjgvKu8i3UKR7we0na1x0icu7MTnzlbcFSch-0zqdEkL2S80V_NTuVsfQNkLWLdFvtI_fgU9MuKABmtnf2_Y-YQF1XV9zZg17zaJkt6L1VleAemvOA8zoG9BXTixUoewRgc0x9jxuisog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DazQiDRUsAWYSbe0Ch0Gb1sNCl0T4m5ZOwuyqQN52GqpwWhvBgO1bvz43SwrPMXhxH1GATY8QnPUcAZpMnX-nkxY06MaMOENw7JLBW9xT4KfYvOqcSRL_0zEOpyEk9AA8wPK99VY-rX5qkh7j_99b_bhtlJO3eEY2FZ8C2l1A79Qn1C6HKx4G9eOLCJVqf33xWpyBopFPXeYRaW6m5YmumapxVSrQsMS8LFJZA2oJzJdeiaDOIkro80Stqq9gyBRD2jLll8Y-TCRfEYjRlMdIuUfN3yQXG_7nyc1jWzxjuw8XRHPsSgpVwOgTlxan-nrXOHTWHDl-LtRGsDXk5aiig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYTKI7zM1UNTDopaT1ZqmpgDNTmeBMehCc3bPKidvH6ovklOXlnmP8ZWa4Ztm5fbR7rb_TQlIx7IgEe0Z35AFChb1cXuScRSRlyCsHoDQNmsQf1NqjoxslcX-PnmwzqY-GThfNCb-83Yn9MLz6Y4Csm08GJTLKrhUujau0Hf6l0T0mV7Nuu1bhRnYVt8H5iARi1Tw6ldSY0-FLerVymrDoG_rwMIVaB-Y1A-FX7Cje_q3bGz8In7iWizcwRXIpaJ1smQLJetxKvUYl-MOBnxCvtIZtlzMKMeOSm_f8uEBO3lHGdCEdhtEwwl53RLbden3S885opuSzpPhBQdwpxO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZa2rdm80Dh2o27hxAMPfnbeQAy152PkqpxJiwRvpaUSArWcKQBZsTv4dCzTIcWACI2BF_IzWWWuI3_aZEmwSaGVatby97Q8GjsdBQutRyKIM7aXNsXtb-IZ0I5-8-JXwXK8EoMmyiEXzr_Rvc3RBOmc24O08DVOjjPBWwnIaNXSZySv1dzfiugxT9a4mwS8ik9iXkz2kBRg5GKYTnQNENPUro4OGRMMR3TGI1t2o5t4Y89wK57CpZtpoqDSrLYOssPXktrTqTo_MvKkDMl8lvuJhstRYAxBlhY9ERMwnF0RyL8fHsKAzwU8OU7eL2crBpy-xq4XMGXyGIvmHWj-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO-KbK5PGJh6UE7LqDu6QB09MB2xIS18ANQwimohsl4cWdmGa0Sk7ZgbVc-DwT3QtTIWJfE30XEbL1NNsfh_IbZM6ExPoHJqTk-YNhIUPSzxL5b8k6MCjsB3cHjIgSGMC_8nM_x-uXMYJhr39dKczHwG_jattM4P__USvwYe4p7f5gX8mxPsspYHDerkP2ynLSu4fmdn8pnbFPOfa1-SLZbvgsbaOSxmxUQfyL9FM45Mf4Jk_8B0wp3rbSoHY0uxyLqU2s_TJIGaaYs2-hzk-kdFs7G9UxyEPfbft4LPfAu6h964D05ICRnkLES6QtGXbV0v8WIY_o4W91DUThBy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDgn6OJT9ms8DL3Qyf06bRrjnUKX2DKZjBzHvnoTHjRqbVaxltCrCDOcNYoXaPyWUGoVEiQ4T94pHzReHCPNOuf8k3sSW3NjFanuQiejHH_KE8Uioo11XQZG896XTfaI-LiK9KK1XB399AVqitiZkko8EzdNi0_-O_am1PCL_ziZappMpTAB6mXFzMzEbw2DcmY0ny7vCFMRdgKJ9zg9fnDUEA1EyREq5_4rewDcm9A9oV4G-2UiDG7g0Qyut66-ODEsmCTvxLIXEffloH-PyeD2XQODX-e9FmB1E9Pwbh_YAEf8h0zOqykDLbMtoM2XOHUA5j45b-4buAslf_fVmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unBOngz6l-IVDfz0pFMSQygsSmoUsqD1ZIUKx1nq6AI87Or4n_inwe1_KKuxFQ5MoqJLC1d-l4iJSbznTzHBAtNT9Hmyk7jSND5fRma7nR400bp0P7RvpDEc1WyhhzT6IGOI1T369Z3cV4Uf7ZY2gw8kD_ZvuGVbSjpbsOtR0LngqcsrwcMb1q-jzjNwliOztVFx3KSUjkgY4A-2p-HMOHEX0kmpSo4hMkTylESrme0suJHmFtTSTpylB5d8pQaH83s8_TgWbAhY9AUWVJfKA_7GeCsvH-yglzHpTUpntDF3rHL2tPkMYi8LyCb0UH6Bgr-H7iji0h6R_HbXcpEeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWsp-D-592Qs8wSGasIes0jPYC5Ui4IM5fFD4liRT5gkLVhNgEvS_58Y3T_CqnJIs_rs8Qr4iT83bswz0Kf3F8fumOR7A_akh-Jp2zwHVvug_owtYJ2FUWVAhdrco0GEtsrslyMob7N9VzrmoGW46H-6ihNGFPmHtBJp7NuW6bDmnEYAGuBg5Ewq8zJg2QORcUgUpvMrG80cJAegskgviXTW3eRW8tP7FttMvZHObkL_2k9Qdy8gH8ZUAHvDC9wTAeXWdfes6z72jLpuky2bBxWYFZpI1KSmsYs8I6rMDYSHk7G8aGp06iOF-Hxs9PPKa2MZQQLYpJaeoHePj7KR3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2dZIigG6mwoxC58z48AqaMgGGeHtL_KhwI58kP6h-38g2RK2m7HacsoGTK8Qd3LqQXNKILy8-o85UHBlbZZlE2FPbIi_WhahNnnXFOyUCXlOT6g14U58qP0oNXALDvITULpNDFK3B8oSbeyLqx6PUBhgWOdo8msT81ZYNSjBhx-uh5fm_n465GNQmLUtyaY6czTnCr0fsHePh0V59KGkthVHfp3GNL0iZ0EwSarULvo3iU1pJxLpu0AzmPaUip4caQ3WzXs7gSYKAhUTk8YJN5vmLAFJ8T9coBZnJs9JhMnDorcgMvaI3ApicGmu1XMt3HF8L4qtIdSAdi-aAKzbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=C1h7yz0_xbLOW90KL5GYbqnq2g89IZTqXEJLYapxuvYnuloFMmi6gFl1G0UyyIk1wGLVaV_7pqD5BBk4g5koKGDVmqm3eg5f63io9MZIOyCUTPMsj0mVJ8iipHBLWcnX62CFCNKPwQpllL7Od45y8Ku13tcbhjswnUKVFJ5I9s0KjHpZd1yR7w4pTAJsri7U1AlpZop4G921BWsM4vGmhdKlfSfM7UNLvPM84ZS_bhz0FyLucbV5NIJzwIiFfPgkX1LtEKFg22SH6ygHwk0yEJ0uELrs1bFYnykB07L46WVtaxvNHQvtDPMSoOlk_8IliUsj-tGvyrAJdbkIEugfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=C1h7yz0_xbLOW90KL5GYbqnq2g89IZTqXEJLYapxuvYnuloFMmi6gFl1G0UyyIk1wGLVaV_7pqD5BBk4g5koKGDVmqm3eg5f63io9MZIOyCUTPMsj0mVJ8iipHBLWcnX62CFCNKPwQpllL7Od45y8Ku13tcbhjswnUKVFJ5I9s0KjHpZd1yR7w4pTAJsri7U1AlpZop4G921BWsM4vGmhdKlfSfM7UNLvPM84ZS_bhz0FyLucbV5NIJzwIiFfPgkX1LtEKFg22SH6ygHwk0yEJ0uELrs1bFYnykB07L46WVtaxvNHQvtDPMSoOlk_8IliUsj-tGvyrAJdbkIEugfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av54H_6wZUagrd4MW6ecvbIZqN-gmuiSrrUIo0e4mcZ5OgziQay7jOKSMhoDBbzoXOZlAVaqhtHcnDhVa3MSJP763lzz29qo7jSVYHOvALGvkONuFrltfuvXCBYS4aQIpy2XQkPLbhYgQPOv6MpIrd8osD6we3eei7EdRTwl0OcrjN34FxBvs1uUF7Z_jyBkWsmDxMpwLhTUMaUON9lYthgp-Mr-w1X1dD7-9sqi3727-t5lVHfsaKGBSMHw9e9bo2Mh8avKF8WB6-qFn21b1MZSpk5cX_KZ2fb62Zg4Fg9upNZ2rg1gPgLCScClxLTlXcwJxe7MvkumUNXj22THrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFCDeE7cQHE_WGxv14Y4-a8rMzXq5bLuzCCclkk2bG6moL89Os53IxTvz5dOjpoKcw0T5gQNbtWNxoDxnC4pvxCzBbygO5D1sK7wP3KBJeP6wlWVsz1mjKQXWCfPdRUWT2_TruXHzAICdWQ0xaWbS19Wm5eYnddCU1StmRBq7RFinT-MuGSpXTqs7yg1Go31Nxou2980HxaKqzi9OzZFx9peh8M-lIaekBHm9DnrFXukkyAeI47UTmLrQ2lIihdE7Rx1oNdiEVurG5QiyaRb8OdiwmHxf3JVcfoPtMCCNB9VwbYu_i9C_bh5lsqd8iC1b0iS1Eg-rqjEbws5EmeniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=YZ-pOC5Bed1si5_TkuoMZgDYt-mx6A_R_C36bvG-FFiN7mkqn1ID0swr4S0_zdmN5rZQbiYs9o7YnC3a_O8C4K5U1_-mOFDyNjzXkYji2FkAY65GkDxJuceSOxMmCJzVE27fbbU2XWBiaCMFYtohkQuXC1tJuBHomYVcv3I2jCpAOkWpGWv8aVJ8b1SROSF7zcusMN5cSpkFgyk3rJLFHa0BYxfylstLmOwgy0e7aNdWbGCfEB4jWCsnUOenW4Q7nvrFuGtXFTh0R-oF-UDRVYEis1kelmYTEPqVNfMt-ZLPqJJOXKz_cGA9o6C0coMiq3OyJHLJzICZm4GRZ6HaxRW6CCBhIAvnJmsjZia_wiwiSLS8oxU2aG_iVMIHyLlXi8cufQLhUtwwRGF0YzbfxicbQYqQfPWcYQzBmHb9y__TFHA8oZPdQPyn3BlGhp5whwAqoAEf-Vh8iq0juF137BSm08tzv35wLfDcpUMCpvIhZyH4d_RXWy-kjm7N5JK6AQ7GCIEFa3zxS4chkndV57pokgZ9_5LPjxX_gDU8SGjfGQqhm83LOS12iU_h-8jdxfJ-21xg2HEyMMBtPMP1M3g1LryVGrM4SkDf1aHcdOuUu-oqaOXaSLArvKHDRp0paL-lHNC338_mZH0gcNgdHcnMep5lMnS7ghC7U4yWNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=YZ-pOC5Bed1si5_TkuoMZgDYt-mx6A_R_C36bvG-FFiN7mkqn1ID0swr4S0_zdmN5rZQbiYs9o7YnC3a_O8C4K5U1_-mOFDyNjzXkYji2FkAY65GkDxJuceSOxMmCJzVE27fbbU2XWBiaCMFYtohkQuXC1tJuBHomYVcv3I2jCpAOkWpGWv8aVJ8b1SROSF7zcusMN5cSpkFgyk3rJLFHa0BYxfylstLmOwgy0e7aNdWbGCfEB4jWCsnUOenW4Q7nvrFuGtXFTh0R-oF-UDRVYEis1kelmYTEPqVNfMt-ZLPqJJOXKz_cGA9o6C0coMiq3OyJHLJzICZm4GRZ6HaxRW6CCBhIAvnJmsjZia_wiwiSLS8oxU2aG_iVMIHyLlXi8cufQLhUtwwRGF0YzbfxicbQYqQfPWcYQzBmHb9y__TFHA8oZPdQPyn3BlGhp5whwAqoAEf-Vh8iq0juF137BSm08tzv35wLfDcpUMCpvIhZyH4d_RXWy-kjm7N5JK6AQ7GCIEFa3zxS4chkndV57pokgZ9_5LPjxX_gDU8SGjfGQqhm83LOS12iU_h-8jdxfJ-21xg2HEyMMBtPMP1M3g1LryVGrM4SkDf1aHcdOuUu-oqaOXaSLArvKHDRp0paL-lHNC338_mZH0gcNgdHcnMep5lMnS7ghC7U4yWNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=MXFAg-MhTVpdMDQPdmULRNbzj2nSjaXU0JT3-RSrduqnvcXpY6nfJWnlBKU36aXI8lVrA2W-Qk1N_4REJ5W00TtHjqzvBa3rh98iN8dk75diDlTUzG4oKkGVCdGJVRUYAO8woJA50VeIc3l0HlXUUzoMCEnQPsiIuUnuVWBjoVDFqqkKrS0RiE_ZWcuegpqOLeDb3UXPRcObYA6JBGKwrFQPNRrsalSfV9BMnZUzg_GsIyXEtiZDNlaGXAFxxxhJzYbAtH6u7JQAjSbvXv5dSS_WS5_v7AgIz30MZK3MN1VOLsrMb-oXxQhzHJaF9-VlSuzPoMpARnjmdzaSvyyvqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=MXFAg-MhTVpdMDQPdmULRNbzj2nSjaXU0JT3-RSrduqnvcXpY6nfJWnlBKU36aXI8lVrA2W-Qk1N_4REJ5W00TtHjqzvBa3rh98iN8dk75diDlTUzG4oKkGVCdGJVRUYAO8woJA50VeIc3l0HlXUUzoMCEnQPsiIuUnuVWBjoVDFqqkKrS0RiE_ZWcuegpqOLeDb3UXPRcObYA6JBGKwrFQPNRrsalSfV9BMnZUzg_GsIyXEtiZDNlaGXAFxxxhJzYbAtH6u7JQAjSbvXv5dSS_WS5_v7AgIz30MZK3MN1VOLsrMb-oXxQhzHJaF9-VlSuzPoMpARnjmdzaSvyyvqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkOBIV_96UOxkl7HmrgbxJAaBK2HOC4xVKEmPVczkmbljCJnxVLhwWevDmYtL8ZCti0IPGw3Qjpf9osWTPyp8TTyUQD0ZNUPvXWBw1_POTnMoovUNiPisLS4R8-TiRtpTZIVx7x1IRl1DS9QMpyNUBo34xvNwvhewpLirrxaxHvbWKj4TyNP7MRSgvPgVwJYfHNAQpGesePWVb5P-cawSLQE9C2Mu3Sj8TVmrKWmziniJKnXmwJTZFRUglr3Q6MFQpXL-6TUBE40eUq2kv081-Qe5rpBpGhv1pNwy-005LBouVaTN9ZtwoGuU5pb6m1dT4d_cdVG4P1mTvI0JQL2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiaZJ2Y9JWLx-f4oZ1UlGdTXukX7fGrh8nSX42hPTnPdfiluhx4MBLLF60H2QBhQgkPAzLjY22KqpC-jLYkJpWRqrqeNUb1ObVo261XAVDlQ-N0PHWh6YGWe-Af8WijdPq0LIo0QlSAbSZyA57p-JZbngCv-2bq4pUSIl3YHNqO1qsPpLw1eq7bRWvktTiNKp659YvSkEMjRGzmgsmpUCalCFY0UP1KGw6nZp-koOMhniR-Qr-2PMU9NQAC8swXFEjR5-B9TYcsdQ2CQTHhf9luabXyUpZsshG0AVuBrIe0kPSq8wzaFiPYzfiwul5DNqHlgDjYs1bzAgrOHIB9qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAtme4GE0pBE-ShdYFbFURBTYwXrAeRr04WacL0N_sQX1lB2iLzayZFP0Ob4wzhXJi-vii_SLZlVIFlzRElJTZVD3ABuVaBMvgmxv4u3jBjfjzCABIcM5XI2jObReCitkhU8H8gwsXHHxYrKp_Nh6859Y4nWH1xysoue39HlUwFDjp7GtuWz69snJAgfRCtbrhxQp6Wd7coCwelzdYcRxEMsZrE9KZLryymf3Cl4OgOViCkMwhjL9h4kj-Wj8uOmUzS_8oqh2D16_AzyqN5k9dFfIFmXBV8VpiUFQkEvuWdZ-sHZXTRH4L6uSppT2k4sHe-r34fwwxLFuCTGe0FipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al9c2b8QqIdS1XUzUhPzZPLvM3gw2x7dEeFlj-t_k8O8_-Z6sEz1rbgXI8eXKyCXtZq6Pr2dMvRjChkEZdBgZJOfD-WO7aQfFUQwLZqZ4D4bzVt-0-GtX27TCTlpVplL6nAdwI3tMtaO2_WQEIyRklEJGBvLmke2nep1WPjP6-wpGnyZCsDG5DAdD96xOTfpJtIz3EG5ag4qazNM95jLsDUig6YWKUyA0GK7YRGwM44YnPXNpoZuZJvnviwYdt5VwFQW6QC9PMD63J8VtiqWlqq8WE7irej6bGcCTcx2IkRPU4vKvcmUrHA3hnl9TBaw1gbNE-3YnmG6DqGCsTQvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUsSyWEqwZs3P7LjvYItY5ynZj4MHbTKiZ_TnyObSkoKgcdchbO9iSpp8JorAIEheiLTlALStLzaO3MyOkQFEAQV_VifJ834FftabHeX740u8Oa5EXcZkw0cEoJsAbtsecsJ4Wm9uTBIUZjijle2JsuaqgIUE6TL83FKKv42HRk5mxWflwT8aHFJF-UVKDwbOc8acTV2mpgrwKHKh4OAP1U6eVdLbIhVFZcFPmAJah-NjQlLrBLC755vqN4nGMEd0iiUfuKGU4wyHJYlQZNFTX_snkaSm17Vimv4Jxq3iP9u5SyLTJRZzGyr-VchtNtFjH5fmseKFNkxIt-zs1fJJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFE0fWeBJqyl0XMWQEPcbKxN_5fV2np7EYLzNqTHMp55K1hEuzy79tKWSpeR1GslD_bKwxLkk--FTxKyLwikV2UECQkehlzQ9TZgk6C2H3DYY_oAuPxj28cIPlPfa6HqGaY5hzRICbcZFkkvwM_JbdzOOHlrcIEpoOPaSI2XqdgASuuD5BEKOwqrS4pKRZBKAdBVtD8fMJcLrLKEk9T37FRBWPwlOtiXP4av1fLoMG7W8B8Zo4FEjIu1aE0BMFHLxA65Vbey-kxASsGz-9iBAGWFOjp0veA6fThj9xfC-Tkid4_pWUyg77nquanT5Sfyq23uFzBIwcIpxQcLkqK4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF7AY5e9NEilh-gjYcN8iKAj5HLPpptpjeympBQs3-6Czak7g4fGstRiOHwVoCulYA71wJnQXH7da4HsLFPdMvdvsONr52_f4s-GyN_Sl3dS8F1rvclZ6GiCbAWWPp-umhua6vnPiRlVBfFfhvMsPbvJiVPvsiyx8uPwn5QjwyYgbrN2BB60LhNN4Bm6mnKlrvkyR83ANEt6F9Dpqif9Z7r7qzaWqGb9wvVRCdrB3T2B4AB3VUflYOCG6OtM3QPPQJsXZ3H5mt96_MRfdu7dvy6r70YUr5Xv3S5vJPHchGoFFwAZ8vtiGE1kjKPy56SX7yDQyZ92kdDe2mKgLb0Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pILrZBoCkAnOR7tB_VtRDcE6u13Vx4CMLaDzdDs-KpxE7GL4d7TcQLDCYN63bM1pfKrI3kkpd08GIhX_6uHug7MKfyLghX2PUu6XOybpmn_ID0jjvaivQZSgoH1hQFYdOBOdFUGSb7Y7SHV8Ppr__4jqYSnV8MjnVLiQ2leoxYTjpDR4IiH3dATs0TvcPuToYux_5YOCRM_qP2Li66frZhYD0oPp8yWN2Q7jJKWjvKRXTMznnifhCkwovinvb44tWkmVJkASDNN7oPMPfs09KaiIP0EjlZCQWkSK4VTCZbcA2E66yuU0wyXcXsZkjzgVFeiSmOHiSa7DCphMurCVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaW8keWWs0cfHw8vJbo3KIQskx_RZ4u2aeZ41C2SfnX9-NRbpa45TWN5uXa36r8wUygcJ5x5KJQAaWuyhgNBmBIysEDdZkQpRwBRyqcn9L1uEQdv-dp2zRSL-6zvPSZf0oB-TgyGRvR4vdRQuOeRPEd_z0tRi14olBtMBWS7BWC6tA1nrQ6xI3rwZUpfE4mI3mt9pMt7PAAZ28NITq02licIHQ6sWHr6Qf64Bv4B1uZdgW3NF_WcqyG3ZjCd_hb7BLqfoZJa3W9f5rXKx8-MvRpue_4Jub21TATxN1ndrIZCCIRc2Ut8tHcSEXEfauzARTaN00jlQeuNPcBTyOPBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKLOZOzKRhP0wMy2roGpd7OcaLxoQmYJeq5xbw5Y0etvF2A2gRZPRQi3zUwHGUdh57HASl43opdSPfc_MSo92KstuT-2kXMpgVOewnOPtvSv8mZ7fBbLkVs1rBOABkyOMalmPQVxHHrjOtpfbfPHzxpOGLQR2Cd-A_WVUT9YvsWdBtnhm40WwVRNMGoeCqpJ1urDXWwOA3TFhtbabksIwqTnlZ2czr8KeUCP0Fw0gNJA-yauIqWEVti7FVevQduKd8WJkd3TkOiuD_uyzSLX-BZGvkVAUsMy0-yZQpkyO_5zi3Y8QcCv_g_P3ED2eEi37mv6G_jOwBbylp-5EcpXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAvPO6Fqbx80b_oY2B4ijSYTuMUgP1breMSA2JCdv-yc2ImHK74VKuLf96U5tFGCDsG9PXlzgPUudfrpzbTNn37vJCAc2Tmp7iCPmXVpcQAenpdI4Ki8j5mFIyaUFsyioeqHaVXIbr-3CxVHd0N0FBC4n6fi8FIEzyFkvFpOagHgpnLlrdMFYWRAo30Gxfmoak9trtcDt-vABZ1BCmxHNKSt9RM_FtNCnzy8iEPJLPXhg1uUpCaQ9HUJ5_qGKBzUGrrryvimVZEkmKV_6fPpMbOR4suzT4s4BsDmHKLDpRk6LSI0vA0FUAGmWvv0pBkUT9BWZQiyBWmmB9xSHhRLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Hwl5WiT2QFnl2fpMWy2gi3KJk1fxtKjsXyMW0h8T72OV4VV7iQdczyuYqn1BuLszskXMcd_vk4Shku6kbIhacVVcKqtcEMYteVm5Deoavcl_5mza1p72mAQr5TAg4o8IAkqdxMpNHngjPH8a1lpfxUPoY0qladBlSC108ng-BHrAJxLQSgYyNJ5PRQHvpANr4Gu2KMS2aPiLtQCnoLYvP7uZosfHVFw6Ilvms2bKlRCKI2GZLneLna1pW_4Hh81Fa6q7EWLdpxYTVewQDWaZOmK9bSXKU2aWBO-ADuNjzjGzPKuNQ0orHdXbxVZFX9Ko9cBiwXtBvFBkBAZrX8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=o2ZiWwJLLz91DAcUTT81-3n9R3Grs4XpqfNvKHGe067I4czJkkmCkUlf6QMSHst5N8Y-z0rMI_EwR3KWdOdHTII-WLFGzitNpXKoPNU0IgBo4cLiT3JXbjrqcSLm7TjsOe_wF8XU3LgOA17g4Sfi7da_lWZxIH44qgUbX8d33s0gYAoVUl9-ruLzLFuZbmRfZ82Eo6HIO-OmZyATdG7-zPHhTzktuZUmQCzdIGJeRtdNXjSH5bn-3ZSs8LI0HPL8tKb_Q8fm8o669Ehc50vqpZh-OG-ls2wWEKeC5FXBJxUPKIQfJ6w1TVsOEtTJS9mh-fWXX4AhA0PaFiTLXmlZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=o2ZiWwJLLz91DAcUTT81-3n9R3Grs4XpqfNvKHGe067I4czJkkmCkUlf6QMSHst5N8Y-z0rMI_EwR3KWdOdHTII-WLFGzitNpXKoPNU0IgBo4cLiT3JXbjrqcSLm7TjsOe_wF8XU3LgOA17g4Sfi7da_lWZxIH44qgUbX8d33s0gYAoVUl9-ruLzLFuZbmRfZ82Eo6HIO-OmZyATdG7-zPHhTzktuZUmQCzdIGJeRtdNXjSH5bn-3ZSs8LI0HPL8tKb_Q8fm8o669Ehc50vqpZh-OG-ls2wWEKeC5FXBJxUPKIQfJ6w1TVsOEtTJS9mh-fWXX4AhA0PaFiTLXmlZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_CToqQhHCIgtwjsZORHFg2rb0kVRSKO9mSrjBBcLxCaAg96sa32p2DcE9rlTFyCTx7LDnXuruiwfjwhrm587SRFFv6HFrZmueYsGittjMJMg0e_XdaGIV_VPnVAC74WP97C2_0Pplq-UgOn9-nLWv_rswmDLr_Tyt6V4CKM8UOxuN-A9-hOnNHSjs1f3ylb6nxbdDdKY44XKr47X4CXr2VmYpvd7bLA-KjyZLnohghcavoCPhQFqf2IQm3mUJDb5ai1h_wsZ__kCJSxdAaGwBVLs50YXVEl3_8mvvnEZQPRhHnDd7jn837KAs82BrW9QQt7YGbJLCam1hvfZ7SY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWCiNj1FiaxN4VCrI-vtF7VPwtD45X4iVnYkeiFz7oABJ2NcbIVojl-poBQWuXgJAmmTkypMHy0SS0j4E1LunGUUmQEgR9yfylMVzOMmV0ShNcQhymqVe9rxXVhqyhaTRyRK4PbLC0XkLKgAOaJXil3KHPwZDXfRs6pVro6P9_PIbsWz1DBNIfSLGKfGJaGCheu00aCSFZUKg57er0KP8wOn4v_9zSgk2VKa1dPeDz8wzz5-ZMX5nQqNl06sjijZ7opIq85I433pduJ3hoJ25dyzzj07Qr0gqapgP8Tw63LXE4Epni4dS485qv9_fDahE3R8qvS9v4V4flhIRQPp8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ_6oEw7OW8-I0_TnsvuoYq1ZGVFKd2-RRqLC7mInQKpHs3sD6MAvk_2UDbHEwzlORNKbtm00y_7WZqUUkFzvRxVcw8QOiRmIaiNd0aEVWT2wu-VOZz1uMu2yn3ses0y99Z9n6oOi2wD_Wb225EBOuf-l0-lz2G1Th_tpfKvFih4RdfqRa6WayapiWVGod0WUpU_FDMkMlmtvIvF5YZDwUkToWk65zZVk5UfCDIzK399DgEt1wW6uOKvaKB_2cwGD1LMlFo6YDJRzLp4LW_OXa_fqw8WKxmtbIvyXH4gYJmul31xtJ34h1iXdbFsCOI2Fjz6DKqQHFgB2w3lfd30UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_beTrsO5kt5XyS0rzZtLZ0xCxcixD1RFNF8q5NPIzWXFTjQw7vs3rrStgW__lFxDjVwFJ-YiTq2Wwld3QglmVJfeainBUdWiym7tPiNg1qlvh8pWsdNKJZatnaS7FrEfGDB8bq12bOuqRqhrfPzS27jzXrGtAh-_NX_T4EQBywqa1CvJKcYQVa64r55AciR4HqMfx4CzLIFIt0qtXEQMigD1TMuZ_tw-tkoy9I-AR3FPaQtJ0J_XWVo8S667a-VuvjmYa0BCPncP9YtcxV-iUkEYjC3BHWIuZZ-kZwDM8-AfneaK3rSIcacTY4C5h2vqdE5rdfenLIlybcV_8FVjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=JhWAST6Tlu3ye_6rBTzxw6nLTzM-UIfo_3K6VP1QW1DJKCNn5FTCdelwqxlSOQHQ2fM3g6VuHTVhmjsIjcX_CkXqEh-LRRrN1DKOEuVcoPRBo-iHRF9CES95LdP-lVAdWsTrG1cJ3oyjbYC0KYCNk6oi61NopGO4bD8YXa2Q76VeIg-P3ClS5te22v913vW5M_yRSx_ty9YAPf6qMY2usUq354b_CGpQDgFSgRVqM2w63aKiJU2X5yJqB7i1ZwctLklk7Jji5U4jS0mvucttB8h7ph_Y9phGzsKbC93bw6mKPXtfmcfkLUceunNJ_qvfBjb3h5mT4aSWK_tWBLlctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=JhWAST6Tlu3ye_6rBTzxw6nLTzM-UIfo_3K6VP1QW1DJKCNn5FTCdelwqxlSOQHQ2fM3g6VuHTVhmjsIjcX_CkXqEh-LRRrN1DKOEuVcoPRBo-iHRF9CES95LdP-lVAdWsTrG1cJ3oyjbYC0KYCNk6oi61NopGO4bD8YXa2Q76VeIg-P3ClS5te22v913vW5M_yRSx_ty9YAPf6qMY2usUq354b_CGpQDgFSgRVqM2w63aKiJU2X5yJqB7i1ZwctLklk7Jji5U4jS0mvucttB8h7ph_Y9phGzsKbC93bw6mKPXtfmcfkLUceunNJ_qvfBjb3h5mT4aSWK_tWBLlctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcxJU0jleOBFzZDMoMhCCQS7d6XfWYjhZpoI8THi7F3uPVksXIDzLR54VAflPJPHv66Qh6pxf9utvdSwE3XmmU9mOur0LNMBfnQDApoFi6XGao7RzAdfjOVRSUFjKBt7sEj0IWkPCds2Nx019VY8LYDUPHLngplmrSfP_2hh1hHmppo_gmytXia8MaBaCdlMOC6BbviZP7HkvF276VP4qfuvmmMpGSEF0oX1fEvGMhlFutQ8IUtpiRa9KH8Y7B6tXx0j61Ff8YUM116C2R16bimotgAMxmDOGGMxsjRPuqL3Thsn4-IT-6ckQy540uNUWDSyF5pPYuWFrc1GUX9wAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_V3_OObTMNso2XJxPMe2_obQ6er3eKYkC1LchwvXuDFYvcAUwaNPqtSmIyWFEh3pgL3IlT13jeSxtjYW004p1AeyI6r-ITUSemoartV26oyS9LMxj-enCWXgAew5I0-CgAN0H0AQlotw_VzbBQhSjeS6WdqXsKw0QxGBvt5PZfBu_dzrQu42fEo9aQTNuIby92DwVQojQbYsJDGP6pOa501OkDFJB2z-6SAX2GB4z_0aIMG2B4Uako0HDrr3Bc0NE48qZQfEZq_xBUbDmbnbrTl8uZ6Ej4LfXP6hIwr5FYz7IUFxT0fd-N6k_NnwIvDaWmeWKqFWIGJWtaOk9woAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHWcCbKZYYTp_UlDn4cTjofrBzFx51wvMf937u01MeavdRM3Tis2GiYx9r9eWeIKJd1-W2wofQMwBwxkpLECpEKGTCSThyqJph9xviSHK3okmpInk2qc-LA7W6bfREuw_UUxKEHU81YDHmonUFUkH8bUw_D24jDcGODsFpykxxefXXoSBJgerVyTDbSq2pj7KdQYole8fsnN69fK_vKhgu_MSKQR40Jf3YIOhursadIAaKS0RfxfvE3scUCprcWyLWo7huRak7V_haxayN22dmHbO1xwd6BPAbHDOf8Jiun6nFucOqrq7W-4CC4zvhFkq_FCCH4__egQroj1Cxk_Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=oqf23y-pc8NzrtTuoF-QqyvTalMYJha11l6SQlIlIhP2vnYFv76H-GNotGd0ewyR4vIb_J6m0ZXeVwNVpa2pw5-59WyLXmSTlmnz91-9ys37FBcX53tzg4KmAzh5iVxdqlZkVv2K1D5IHm_BOlEd1WeF4qXE7gkteBSQgfCn6paetyOJ9we1kotAVzs8VhN3zp2njQoHNbZO8dXxoFMiJhbHh0V6nRYm6GQDUoW_-MoeQeLxzCzm_3KWFHejI4ZNMPiXPlVC70T4NWfWXaryP58xSORC2mFj-kiCDW3wjNqGrs6rCzcHM02cyDOEzvsJGv9PBvbL123jOJQAYiFJgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=oqf23y-pc8NzrtTuoF-QqyvTalMYJha11l6SQlIlIhP2vnYFv76H-GNotGd0ewyR4vIb_J6m0ZXeVwNVpa2pw5-59WyLXmSTlmnz91-9ys37FBcX53tzg4KmAzh5iVxdqlZkVv2K1D5IHm_BOlEd1WeF4qXE7gkteBSQgfCn6paetyOJ9we1kotAVzs8VhN3zp2njQoHNbZO8dXxoFMiJhbHh0V6nRYm6GQDUoW_-MoeQeLxzCzm_3KWFHejI4ZNMPiXPlVC70T4NWfWXaryP58xSORC2mFj-kiCDW3wjNqGrs6rCzcHM02cyDOEzvsJGv9PBvbL123jOJQAYiFJgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFbk5TZDRNWftXqsMuCm8_gVBoODOP_jgiKR0DtHDq3FSy7_d26DoIg5tz9_tjABEvcef43_S9gKRNye-DEvtpYZhb3L_U9FTTDPemOkn3_BbBHbprPmdr1fF5a0syud_SYTTMs1BmoSnvpOu9K8PEwTi62oPyeOAwpc_3Nw-Us8yHA2nsh1DYI-1LeVE_OJQhBY-IqPQP6AZuq5pdM2LT9kxJROAFgJrmBpp6ZOl3lX78t-Rhg7xNqIVNfgGTakdlWi5G3GZt629qH8HwOlGus7S_AzURjIDaaWDSZDW7fUH74PXPRq5lO0iAOhFHrgVU9SrUMw4_4qyNEoIvgPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4PBNGljdj-NYcesdUYn3zvpE8aeyGAM2Hu2QwGBnBQ6EaEooxJq-HNK3cHOlw7N8oLkcm7zZpv3IZ889FaeRnmoPH94acwRmpCcmPPumnUvX08CR5ut1YksBRhi5AlI1x50JI9yFHWq6dqJTIy2tg3sRGgQ7Nlb28fVg0Dcja6zUGKPIyHwKQQF4X-GGx1xAkHqO7VKLH-ohiOss4UNLL3EKIzPIMPo9JDUf2_3ISLMKwedSqZZqViWUTdBzF6TKyVRrIuOQNCy9E8AIBdKvwk4TzjKEqJg5YYthCounCgp_lqugaYy9rs7HPVadRuarHglxMlPEnCktnCmzTEOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwmg8LvQj7AWyzjBDBWTAl84JMV-haYIXsbAzJrIF0weQGHo7PQJYD17-QpOVNijiPRNs23zXT6YX1mf_bhHBuSnVkavrY-PC-if5Rag4qy1E1D_d1xR9v8dGG7jk0oN96yb5fo3PRjH53qiHRtv1i_ZpG7Ld4PyonRaS_UccoxcJhD3I_1BPuxJ2cbtKhztv4ltKe1B11pCmQBz5CHK6gqA44S_aAHmqmw1h4KNtcnnGaE0N5ryRxEqDhjYOx3lG0PCiMZ9G96lF8nk5YkwvbD3M9F-AU76HgXGYEVSqVJycadg8fqu7PNqIPz2fkzABSuQE_RX8mXhwrKl3uV5fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnpKgdH9o-qyj6Pvv1zzyyVaC4xkYZ6QxPtjjMETaEZzIFEfvTbZA7ylvmctLJGSKOzZ4Dkh4kxQI24rOKTjIGn2s6wKo1EIPJM-dyvlorIqcN7BvqppLKs_Z0XXcsYUeCgrdKHv55Cvc_o89_dSdoNL0Zimob7A4OVSuoWKEGYYpL0Sr6mzH_uTPf8y7kz8p1hqQUHvXVUtEG87M33dfVxTy4c7aiCS76--z8ePyGof09m_Zo7Gwn_sTKi_tUdGyTmYBjLCPjcyoHZKWGAqDMoylmX7QX7Fz40PgTHcTZxDnztB4KiX4Aq_uddeK9DBdHzut6E65N21rGRhLTFhJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux6uFvPkQW0q-NSQ90nLGS2_jpe-mFTDYQbzq93ZQ5ITZoj7KBO_aPpWOorNejqSGK9XotzOMEHPRjUbI8B4u-iskZfBbVwrBbhYYnZ_5bs2zzAEN5hLDHs7g8uFtj7nt2bASLLmksUs4zB3CmLQunhHNEG9_9FTaI0WTpyKpQFVOTo1lSYOGe6eitEAGo6-sOjvdtVGGNzak1xe5SWt4HPYJKrLTMx7pjK0BzWOK1CZ6BB0aHD6XqkmFOTIyy-BxkR0XTxJWLygnStxA5XUBBN_aonds85V3kz7GlKPOIO-SsKJz6Ra2jhMK6dEPR7HdXwyp6LqRkn8iiudwLcH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZnHy5SX6Z0piDwetBqnRJK-gC_Km3a4_5q-J45nULKEDIw4GWI9QodyWYCQS4uHXABxgROka22IAWvr5Pg1ixz46KMQaSOqnG0DFzVN3F5R-oJ21HymDhE9J0w9BrW7A55TBiidS7taAoTUvcSxerQUooj3xlKBsmSLGwCn6MEPimNSyHNRUqysdslyuqpk-OQkzwm2agsxnlGcYDbE3ibxMQ3bEV-YM22VPZXELiJYsL6nz6e5ut6G_rEUVairlDAw_L2rI5fzSVaEqXWXHucETiSUlV6KG7Pl3iIEMV70IqkDGs5xb_coRLEq8McOLtS9pYmGIHlr8vkeSHkLEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=fgTbA9WTMpDi3b7FFjUzTIl_ekTsuAHMG0cAg6Nxrrpvc8tIjq_4LKdggKzgHYYic00NBQi0TRVCCsoVVEjgXx_pn5-7XnXMdTGUw6g6PrCUTA2acqAHKSmeirEzRoAWAA2NsJmZN-Xm-vfEJXymZbkieIRKRQmJiIvzMhj8H2waB3IjgH9H3ofEozUW0wCUUd7ToAGAvqcYnqVA6kWZJ_55V7IHny6YnrXuRWniUMdtPWL7weO0V8-SemBbqJIlelGipMvMjbigK_aJQaQ9z-e-Zg5X_8P8qMFHrLJtYoC-88NAs9Po69Ys0uATSTPNcfySDnOTKNlYcqbsZPWMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=fgTbA9WTMpDi3b7FFjUzTIl_ekTsuAHMG0cAg6Nxrrpvc8tIjq_4LKdggKzgHYYic00NBQi0TRVCCsoVVEjgXx_pn5-7XnXMdTGUw6g6PrCUTA2acqAHKSmeirEzRoAWAA2NsJmZN-Xm-vfEJXymZbkieIRKRQmJiIvzMhj8H2waB3IjgH9H3ofEozUW0wCUUd7ToAGAvqcYnqVA6kWZJ_55V7IHny6YnrXuRWniUMdtPWL7weO0V8-SemBbqJIlelGipMvMjbigK_aJQaQ9z-e-Zg5X_8P8qMFHrLJtYoC-88NAs9Po69Ys0uATSTPNcfySDnOTKNlYcqbsZPWMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwJzI3sAu2JVwItyO7zquBpLLZ1VWJUcObYo3xQF5U82nVn0eNwKdmlS1QwbjByUyDOVO6z6L1tNopiZS0bL0fAyclA753EJljz1L97xe1lilcZeDiiv7Evi-OKyt8bibFiVEFLfUJ-Tp41d-QIN6QknNhHho84p4Tq1sUjHd8FVcjkJJxa551wQq94FfMkUPFCkZFFIdsdvHpLrzgqjAqcMgULO8R5cggj8I3_Y5mHXtk3ooS62ZNeMSKv3o2RGKNzWlZi87YbXF8nriKQkDO80-MeTzoUrJhFPCozUf7EOgpZfGhNwIi58hSHqC8uG0ODeVfZdRW_-LHv_sAvl7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
