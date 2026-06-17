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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 705 · <a href="https://t.me/archivetell/6428" target="_blank">📅 15:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 753 · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=E1bw8RTDkZ2ht5c-tmJOirWLaiDx6Ncwp-0yi7C3HTIx8xoLwhq1mnvx4Ap3bOFDBtZOQ3QL37BS5xsrSU7-0YoLgN6outQQ3hZC-o9wifDEsjdm36edOUAldsSiSXtK-8HM0HCgLWgLGhnJcBkf8A5V7gZr0K9Jp7ccGl_UlbNbDxg4sled9-vjEa0NHbcI6eLj5C8_q5eIqO7_V_tHmbIy5FTOjQyEljSlAx9q9ewW19Gy4JirBCRbIrcnDsagffK0Pvp7sNNGnxmGWmoaOf7__6LnLPAQ2zdSd3S5S8LWIdqiCGxuHHXfqWaJQM1WBGqo25ZSaDLUijm_ZLV77g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=E1bw8RTDkZ2ht5c-tmJOirWLaiDx6Ncwp-0yi7C3HTIx8xoLwhq1mnvx4Ap3bOFDBtZOQ3QL37BS5xsrSU7-0YoLgN6outQQ3hZC-o9wifDEsjdm36edOUAldsSiSXtK-8HM0HCgLWgLGhnJcBkf8A5V7gZr0K9Jp7ccGl_UlbNbDxg4sled9-vjEa0NHbcI6eLj5C8_q5eIqO7_V_tHmbIy5FTOjQyEljSlAx9q9ewW19Gy4JirBCRbIrcnDsagffK0Pvp7sNNGnxmGWmoaOf7__6LnLPAQ2zdSd3S5S8LWIdqiCGxuHHXfqWaJQM1WBGqo25ZSaDLUijm_ZLV77g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFufqLQSWLQ_dakJYagyqzh3urz-Gf7gKhRyddShmpMUVbpABO0BOoO7qnOjFcH_877-4gm7H68QJgG-XTGDXj4aVvTlEsIHabqkqiMxoEGA_bWzB2pTjFhvTJbSUWvv1v4YfNdvFh6OOZUdZppCXGd75SNvLc74v-QMGX0BQID0bIXYlIvsQFrD9z4unLXHyQhma8NcG1qf6gELcN_7MFix1DswznaVBjeUAERiWhkZTyM3OifqarWNk5B9tocR56EpDLSHAkK9ASlgMv3a-gjY0I7-scSsf0lFknIbXMtbLEmWAqW9tPrnf0RqcObO5p--I1fjJTYdeH_M7pmFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=KF6O4H5bceFJrW5qMpAexLY1EPYTsPo2_uwIwZrH24-lolrE1fzk7Nc4qKEfj1sdSh9-wJRyOTkHirGvPVEk1NNskHVXcbjtVg9npGtfU-cV5exiJi9jAjm3qIrGA0ti1uTgQMaSfS2l6LbkvR7Uc7dIWhcujSM38bkqkJIIlhpq-JpX1APcRLgWdxuYJTiLJqGzNF6E2eKcz6qDJ4RJmtULsPxw-MCO6nDuw4HwOa7qvpd-S3G2CPOLXEDqWGH21r9AIgLR5jMSDhUVgrOKStBXOPE__yqGiJrgYW_1SAzpkV4oZu1CLlezY4zuGcjofczCBZFFhtYW_r8t34vSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=KF6O4H5bceFJrW5qMpAexLY1EPYTsPo2_uwIwZrH24-lolrE1fzk7Nc4qKEfj1sdSh9-wJRyOTkHirGvPVEk1NNskHVXcbjtVg9npGtfU-cV5exiJi9jAjm3qIrGA0ti1uTgQMaSfS2l6LbkvR7Uc7dIWhcujSM38bkqkJIIlhpq-JpX1APcRLgWdxuYJTiLJqGzNF6E2eKcz6qDJ4RJmtULsPxw-MCO6nDuw4HwOa7qvpd-S3G2CPOLXEDqWGH21r9AIgLR5jMSDhUVgrOKStBXOPE__yqGiJrgYW_1SAzpkV4oZu1CLlezY4zuGcjofczCBZFFhtYW_r8t34vSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYlpdb2fjwZ44WAqF92dkfuUgUfaEqFXP8hGAz7sooaTRmnGaxrWlsIIqY5Zx6fS3L4hZcXbJ8_6mw6xx7xq1suZvAkYxW4Z015adePyV9Xf6YMIr08qMLEtKBLKkBme78BvccBqdjKAlI3g70amK0_kfnqe2hBggwC37Xsk57is3neQg4x7fdXkrAtT7J7SESc4NJo55udHAWarxzQfbwmxQswPBCwyjw_e50eg-ZgguztC6H1KzMpgy_gk27Srw1KHfhd-xS8yBRbBNp3DTbcPf-UXHM9KWHI9E0Dx9ufeLrB9Iptvbg8Jdw5jSzCKwTepIpa2ZXhvt9ZwwlTWCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qKLRaYr0G_eRKyoVo26374FajY4S5u23xlmSRwaaKuUzo9KYoRs48Ut6AY5VI6T5d-ROFnrlK87DPoGiqwyx7sgeCQmh3Rv2g6a-Lrwq8sd_NOnm8bIu8952JwOdh9i-cFP800SI3fFF9bbmgWka2yezSaneD1xdObvHD7L3DZlBcYGI6h3PdiVD2R_Fr98AhqJKb3Fdm1aGOWlI4v_BFKF2HrkyI533BHcPHq0mr9wyEojfjSkw3y3rj4QRwE0lfNUQlzwmHjIR4C5eMoDxjd4DRdtiqQsrkGYU4Ce6aNEOt20XwGNwJ8PrWnosGbMWTta9EvllsRFkDlGOQl3q0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvjJbramveOEAURSv0Co6h62Ny6vErM2555CSA_nhXow8pZrYtjSTOFwxdxGotQTH7OEOsSuf449y2qcPdydLiYfxNXs1-h3PoCysDXWAJG7k3BZu9or7DgCO3fZzrv6P5ij15_ZSg6K_6dAjga1nixLlGYVqRu7kGTmjZd98Jq6JY7P7f51bMDxgX2kPjFLaWlFa8yPQlz7t_BDYgfSgfwRFaYoXjE_eHDaR9zBavBV8idOUKiADuKnM6XIDHcV8CGPRmsFEe9yBWYcWR65Da78ZOXfBNzlcpWQ4Ro_-IcjlI4--2QQHgYJoBbgggo7mCfCJRxeX9cA6ngHhAt9FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM0cisYMonxEfkVVTRYCa0lMjo1FsPvgyQ9kyTcCS8KBjME51HLGafNznAvZRvUPwt6l81X7RAZZm4QSgvKCAoCrS3tsUOBQrZUvSxyvm52-RYx8OJ7szGX_FP2vOG7Aq5V3BGH_ppucMfWyu87wsgIhuZTsNPjOJVuvZZQryk3NbKnZtdigvgHjX04aFmVXXNG2Q5x75ZVcuHj1eboCE9ttvd4soyANYyhLn0iyWl5aK_lTjVi8iigiV6CfkXpdehCq1khibMxT4xg3eREkU5bauRhYU0xUffiBbKXAMoy1n810ZjUMsvS7678MIGBYSPtkDm-Qkgwb5oTQXilc2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8o7tYnJPu5iU_rW8GChfT4m8usBX27boNzmB1_IiPo5YQ8IuwSWnDffxwaDmyYD0T5K0b_squi4ymX6WLlYzgPaULgyu2HG_mtjRXUifT6augAwm6NUqVKKc362RqknA4Oxs4QWdnOUBygYjEALaCW9hb7WGIeVRMwOyzrG-Tu_xko8zoX2joGl3ATWK-29OXOZRyf2ar8o61HkFDhHvB0PSHQ6wwyxAVDGDt7sbslFBU4GJxLZDe0H032lYMT1i69ojiOZIlfOXgyAndoD7GVdrKB1A2ZkiEsgEwzwFm8s6kk9cRPuR9PzpUk62P262M2pBq7fVnxAqkP3wJAeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEbw5F5nv6unvyT3v-rPfcAlaWSPE3-31udcc88_2CHg_Q8O1Gp8fjqKtt283nSXheGbCq6_SjpiExiq-OX35WL5boLN0hINU8ONOWV73w-Ku2prVFuqP3HIxO0Nh8Dzl6cEi5oaQ8CZOYG0r8ffn226V0vMPqwSJStu_VR1hoaPsjRphmfjfqqRD6I5LgzEge221dTPrIyIe1E0tjSr467M-R2q0j0ZAVotGMzVQ7EI_GjwIWNuTbU4x5LR08Hxhqi3p8x422WWAgm-WC_ra4AsJpepq4JWeL97cNZ6rLvsDQ4388q2USLmykf_swcFpb9vjB2MmLFiyCtlG-sBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXH51nymPhIWzmVKGKrm9zD9Z3jGcAXCT0E_tGcab57LRMZwr2pSfGAufx21UkaxWEXB8irMbdEXRfQ4OYe5RzP72uTnlHpAF0qRtMDxQVlmgJo_vsL_YK6LPCT655LhvARD52Ne9kYRW9Wo0WIV4VDrrw5PN3D48tSsgbPPrAnegeinqxHxK5oPF2MA1wv1MG2EbtsbCyj0TDaIX_6kjch6F4UkV8hc1vqRW650sLvDQwoDLzSIF9bJrzPRqeH9QJI-Wzg9X0H6wX4m1pMD1GjXeZPQ1gvugQkiM9u4i2HQ90wQ8ZVR35ETuYOEDOgFKjCv1_b6ywmC05WfgKb0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJV6i08Hvj3sqGG9Tz9xgjli-b1wkCYIrxRgkiOvY5ubbe7eYDwXF_vnBdyeub1Kjoto7XcaRhWaY8pzGihVhKcGziHOP9qqza6sHT7I2CoFHwZMIyz349SGlrNmL4oKekGkygHzoyehE9qduBtFYfdOQ4cApzBDC3VLdHW0gMcSMTZFnrQdVapDQQB1W45RWKluUV1La6BevQ10Fn3A_9TkQ4LrJVY2BT7hvyCFt1zupdOHT8oIstE0uYICFmQRhT5kS1V2upNPr4U2F_pX2J2-7RVWh_e_jfg_6BH8E3KINZR34qaub-m92U8PDGu1YJKMkFfeyvFIHFPoZoLQUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmyWs67obTdrV64VpddikVibJ0sckcJPYzAqLjipXlrbRgtNrAC-9hjZlx1wwNduUQqzg0iMyWM0TVCK2v0OhlwiQrtJdm-wHxNAMmaLD3yy0SfUJYHNilBfPL5rHwo0j-I_GhX8xjPTYaHkYmcBryHkRvZkUdXZdBKZ9R_cvQK4cgBXRftA3h0kI4KmP3Gwu1cXDjFfO6jIQl8b3S6NgtB9SZigm7SeAdjCo2ANxsyLZH20hSoomB1ScrDw3AwbV2uZ0rlyQvj-LoZw6uUzlgTtTyjWjqjtaiOh6EiVk1mCZW9ITtJSMbIL9_qQevU3reBhilHhb4JPvOGLB0M-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY3PId6vwn6RLX6VkFv4ScjJ0_YfavkBj4o-CHkdArdAevf8FqlbSn1DNf8XgJt0PDPBJy_8JaKAOHseCwx9HWM7TtuKawWxuf_zAEiXMkyVUPE4GnoSObSmMKXUohVVIwVmwg5yBEqf0QPr1JW_8zbQSKPl06M7vTKC7brpUKcTCyEDQtvUZ-T1Sxr3Rd2P1SQVEI74rxmGUAbE6R4JeSmrnDiRoXL3GEXp0Rf4k_VM_4im0EMIY5I1zfZVERyxMSP44aruU9bCzam79REtIn-CXJ_x2zwdns2mabkDWCAZTqIU27XyY_1COTBZsjZnwXU4Ou88e3huHVfVoEx6mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK0DtZmH2Fufj3lneTA0XyHvGQmboHHeGvldP1bPoXfV8NtPkEbOYfb_GZJlbSHZpbv3DIavxzyrix4Mxse6Y0k_j7y-jQqUWw3b2eeAuxbilk7zs9GEFaiAxavlBZhDfVcGFan4BFbk5JJpFnm_Z-6s41xPtOFGX4tHeEtDuymvKedLaCy3v3uRi_w7ZABDjOv0g6SOOWvMxA27dWG7g-gpDVDllMjV8MT74rNuakvQCIWxsoBeA-KF5Umx6mxOX74Lvv0MVZGzutmYuCWPoNjINsi-nbGet77tPJdp3edcbItRZKjYT1iDpJTin8QoyGw9avypcqLU2Dk0-zi5Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=aPBrS6WoWCHo-_AS6WZsZUlgkOLRnODY-82fPkLfpl-S8W2sdzaj8cmhtrgaduOP1dXlamkszyZnCZLCMUv4RT_0m613ZWt9oM2jAlaR6c4EDXQY74DiaV5v_OZovoEbDKwZ2V9rQx4eWTgfG-m2aTeHRwP9Rd30BlELYF5ihHdh44Zj7bOgDY-TJY896un6nV-Q-J_cg1uE-CekyIaqgFoOz1UuV-OSU_x37CK-2ZrKuUKq88RTwZUtgaJWLrIwT0uUMrZYN1flNtA3fz1gcPNVKVstlSzeFK1PqriPQsKXREOP5id7Oo5v46kYL0g_TE9-lSHrE-ngZP3tbgFIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=aPBrS6WoWCHo-_AS6WZsZUlgkOLRnODY-82fPkLfpl-S8W2sdzaj8cmhtrgaduOP1dXlamkszyZnCZLCMUv4RT_0m613ZWt9oM2jAlaR6c4EDXQY74DiaV5v_OZovoEbDKwZ2V9rQx4eWTgfG-m2aTeHRwP9Rd30BlELYF5ihHdh44Zj7bOgDY-TJY896un6nV-Q-J_cg1uE-CekyIaqgFoOz1UuV-OSU_x37CK-2ZrKuUKq88RTwZUtgaJWLrIwT0uUMrZYN1flNtA3fz1gcPNVKVstlSzeFK1PqriPQsKXREOP5id7Oo5v46kYL0g_TE9-lSHrE-ngZP3tbgFIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQWnpZPXereXpgLyxTH7dSd2Ae53gOUYFyQ8UsZshF2psWFRYZQbbnmPfcRSwQX-KEsqA_O8-r_b9sE36F5-YiJeu0KCsLT4atl6MU1fxBzWaOw2LFLczOBGi_EYaiZj2WxNKqggp7xktSMFJURqjUQe2dhVMsmUcTGT_KdfJOfC7o4dChtC8SSsXvsf1NhTKO7j7MtmXoc9tWCT1RxPHXUQyTuu03PzHSNknJQdmC8KImTpvIkjjkxpzB94GlM9l1zqU0_h5A0gE_Slq9l-bY7ge-Grqmfd5OF78Kob5CjgwqJC5zZ1PFNids1aMtKVvCPAAGJ-uDDShUY5YZUOZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI0bQc5M9WKqoaqQ8FSY7nOka3OCGVUyAxqFiOdR9v5K5-tcyvLV4t03H1USJS1WZ2_ZPSnIERATgbPq6VNoeX4dYFw-TIcoBppXolawxlfmC39Zb1-6R1SSW6vAYDO2eJvJYgcLuPQhxmv0WQCUesXgNggzNxZXrPIbvxsVOevQBo7zXlsk6pBogu5CRFGaLGf6xc6qI6SDv1KmOzFQbIBm6F8lUKQ5msb4OgRaRaRh8EzkHp24lfoSrHsIPwmP5Fxh8KMSnAwIJpO5OiyqupvcwZ1MSZ7h3p8ySQtvgkigLMCt9IY6KiU0SSwB0jnavte7xB-KYozsJwNhAaoaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=PoDyVVSgAlsjxPvqMIe-b4DUhtgqxr1pBBXkRBVxZQ9GWrFSGWbZCAf5Y4xZacMkWhZLLq0AR6hVu7i7NO3YYWq6rnvtJkphp4kNR6UMdszgB-1WwT-1Tnt1yL8NP6867ZDiSPhV4yqfh9gOAab_idLFIGwo67rJfOf1zuRwyGeo1v1iB3e1RcLFImph9AJjPbtRtOynLxRBPvR4OrIvoJOmzeObmeV5PEFqjEy6kAGXs7oqQCmlRpTF1JEPmzl7Aav-FW4jHv2vN9exo_hf67Bfu-6MwZQnAFkmeIC8wfiTPHq0Wc4RiApAh6QS7Ie8vkEuXccgWcEyVA6LPnHCKBU3DHQl_wy_57FNXy1ClJV8CjqTzap4NAuGxx982PhHPLYHnvF2FhO1CSf_U8Mz2LqiN8Dzi7ZnlQ-NMMavBa2HJCNIjcXV4kKir1ISeKQQwNe_ZecyX4BX6lA_BLMV17MrRCE3_a2qyXHpcEM0J4MjpawJmrVdwRpLLSDaUEHzmR8jamvZj28J6J-zx94lXsCu_hKxvZAXa55QHuOzaZlodcaz3N0CRb3mTODqf0WjUO-X6noG0lVJ366zWC4dv7AlykruEkvVcHRFzLGNdGxbwNz3Xh9ZG5BrXVbSINbc6eJBwyQHbEXf5OkyCioZ1JXLpdN3lvYRXz3irJqp6D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=PoDyVVSgAlsjxPvqMIe-b4DUhtgqxr1pBBXkRBVxZQ9GWrFSGWbZCAf5Y4xZacMkWhZLLq0AR6hVu7i7NO3YYWq6rnvtJkphp4kNR6UMdszgB-1WwT-1Tnt1yL8NP6867ZDiSPhV4yqfh9gOAab_idLFIGwo67rJfOf1zuRwyGeo1v1iB3e1RcLFImph9AJjPbtRtOynLxRBPvR4OrIvoJOmzeObmeV5PEFqjEy6kAGXs7oqQCmlRpTF1JEPmzl7Aav-FW4jHv2vN9exo_hf67Bfu-6MwZQnAFkmeIC8wfiTPHq0Wc4RiApAh6QS7Ie8vkEuXccgWcEyVA6LPnHCKBU3DHQl_wy_57FNXy1ClJV8CjqTzap4NAuGxx982PhHPLYHnvF2FhO1CSf_U8Mz2LqiN8Dzi7ZnlQ-NMMavBa2HJCNIjcXV4kKir1ISeKQQwNe_ZecyX4BX6lA_BLMV17MrRCE3_a2qyXHpcEM0J4MjpawJmrVdwRpLLSDaUEHzmR8jamvZj28J6J-zx94lXsCu_hKxvZAXa55QHuOzaZlodcaz3N0CRb3mTODqf0WjUO-X6noG0lVJ366zWC4dv7AlykruEkvVcHRFzLGNdGxbwNz3Xh9ZG5BrXVbSINbc6eJBwyQHbEXf5OkyCioZ1JXLpdN3lvYRXz3irJqp6D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=izHs9nWBwGk9Or5BzOD9fYWS8NCutuJrVNRKQQmPCZBNg47ZuWqBQk0bV6ay1dzhTztlbHx3OIDLbZQj4SnoXs32rnakeQaGp2XZe4tRI7d1rdYjEm26fPSmulXzjC5o1R1EdZl8aP4S6msY6N_eWjRi9g65kaZgHDkX7EluKCuxGU-r932DEbZ0FyrBXo69SKvivQ2xvaKAyuBoJIiadbOYPx_kw4rCVgoIj_OoUSe_y1bPC-dCv-5bcsyUV5ls0pKTEwGVrfR5_Y4LRe7gpb2IErbD_IM9K43s7J1Q2uSqQIUrSQ5JGKA92NDRFND4e90nYMTTsx4Bj-jqlKiExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=izHs9nWBwGk9Or5BzOD9fYWS8NCutuJrVNRKQQmPCZBNg47ZuWqBQk0bV6ay1dzhTztlbHx3OIDLbZQj4SnoXs32rnakeQaGp2XZe4tRI7d1rdYjEm26fPSmulXzjC5o1R1EdZl8aP4S6msY6N_eWjRi9g65kaZgHDkX7EluKCuxGU-r932DEbZ0FyrBXo69SKvivQ2xvaKAyuBoJIiadbOYPx_kw4rCVgoIj_OoUSe_y1bPC-dCv-5bcsyUV5ls0pKTEwGVrfR5_Y4LRe7gpb2IErbD_IM9K43s7J1Q2uSqQIUrSQ5JGKA92NDRFND4e90nYMTTsx4Bj-jqlKiExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUIwxyKaAMBXFGmSdz6sw5FdiExwzpkGhui1G150LJl4IsVI5D5XuPgoMzi4GeHuQap5_0jgb08BWrnZcOI_oEmGPDslkfDMIwZP5oMf9u-9UzXOikQd25zIR6bkN3jJmDjznPuvVRSZ9_Fy4yxB-CZ8M2oM8uoE035hTFDfuwr3dOFWnMwVzb8SKrC5E9juwJEyHOrmCJq1joMKoywDyQbrwBKjUeZmha0vJ55Fwu0CczhcYbi-Fh5_BS4EgxEw-nPnWWNj42WvhMhoQ_VHDOqauErEIdtT1KXNhSuEz1DXt3mbPyjGmkGqv-KrIdo8lz6MSzNoeehR5nKdUv-3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx5xeapuMpxKN5YRoeNgSxF00WZTsc7MAXgDH5Fz3qTukqVHaU1fCNX-EnXNGuNOFf0L23sTjdx9kJrGS80gnutjbkFpVinqhVmYxQza0xJmipvHGWCsMX1WeUGkaGInHem8KyrzwVhPuusP05k52gA6qwLnk8K3BBZpokQzDIRf4T_Oohxehu-5JFxcoVhkEia6vqlA-Er2F7dpJw9A7Q2U9R7o8rlVZUm2y4CDqd7ccKkz3eG2_I_sO8cBw82WeHXXGSqdQxdkagdMFfTg79KYRDeJ4OhsjrMvRFZ6MLakvL_zLG-ooYuxju3U64FZG-SsPmURYD3CQMVaink_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FugpfsXqvoC0r74slyDniZnAupdF3wVFF8DCwwCUoSWUlF5TIuB-TUngTkhJ5f7sSdQ76AF_eaBoqmjqPwUO_kCyvWW_b_3JUYfKpHLlqQHGZ5Coy0uc422apcaMVZ5ACSgllJv6e1QEnWOVeOLq_GQ0je3YKzaJDsDDhTelXQ2eurFdFouddGlGvosW2O_t2L6B7KOk8lUdVWqRK_iqv1-6QBsdDujQaStW83fTlATyETUE7BPW434k3Si5BQWdavQ4HD9j1UPDNr3azzPTk-GVzfvAtzfI5pI03C4xZXmMEmBFujcmHC-ywqIk-OIyDnjCTSxb7SoiTsecaipwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uqax8R41Zx5NAF7t5-gHwFI51JfXSnR_xoEbaD5leU3vHIiixmC9UsDnxw20_01C16oQfo9LdJJTQk2IsNP1LYBY5EJ483TCs__7BlLP-DNnlXAsrfDUBXO_UFVHQ5kA-8TS3pPgedSzlOcVbroYC5lWKE_oBXXEPRLGr4pSN8MgZtTz5xn62MMpr26gF5jo5feltXAFZTvQERYofjazkmZInitM0rMF06FeRMMvidgfAeiMk5zej_2viQxQ_Nipy116bMg7PjErkw5W0ei-EYK9DQbfAtr9EJfnopMQV-lUOa961sU7pH5MdPRT7GS0E7XDwDAvds8fLkfkKJyVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFaS1BEUaLT5vgSAbxyJ2vuWbTwEkAQdnsROO71xaPNaM9ui9rAse26NUitHzFJPWalUTcdBP-gPt8Ki6hpTe_fxqiOyQhgzKVUeWwrowGeQOhEyrUH1rU6sJHzcDcYYE8guCn7kh43GdZXd1enTmMXafohQRVAso7lqYu3H5lQ0rBGrZQlQyyIll-EgGM2dEKeYzFRIORVcyZZ54M3kGmgWShGBZEYtr1XI1qdL5D45k0w-qQwRAdDQReutpOxKouPSqVxSdUnML7GelcwIn5Nq_OTEZm4lHChjuXCuTDYd57H9o7UWAtwEMD9NIu1HdJ4N5933t31LtYuU6Xo3UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQZ5_4SPTP06DM-lOMe9UkAZGrbwH7d47jvG7v1dhEeQL5nWr_Hvwb_RAssCXJrVxig4in_ChMoEDsP0LEYmuYPNg_f1cECHV7OdxQrEN6-Qnf7Ur-vdaaXZ7xlUCGyFikur5zQL3P_roRc9trG-1e5c2GTsbJ7uMUTuXffEXQMVNw6FRzkDM2Uxezfohvb0HDi_mrnmiz1hcZlJ8LbiufQ-XDDrbcr6Y9iR27mqc9rdr6-H4DnFa62nxmDXsE5gJKlAlgMQtwVJf3HDoUaTDj_veVdjeumtJ6-kJe5E4rxldL0mosrhKYPA1t1ibTYbNWjitjDL2sm5Gh79nCJ0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgmKWStTETkzyAyrfsuFj9HQrxWOG0OgopdwkFIP1eDKA6GUKFBW8_ayfxBW0ClYLjTaJfBE4M1v4tOzoFgcj1Gnw3IE4Yy0O9rKf4VsuK7EBqGkAV50v3OxeV6-vLsFTLHEikf93C3kUB4tQXuO8YCK_HsLNL4dAfa8LfR7dVtIi-q4qxECO-k75aMQyHdmaoW9dMhXwGhMqugK-MN9rASIArWWtQa24dw7S4-Z4CptsNE_q4AP0mMEfi7aya8ksgNcCAMoiKjRuFCffPTqN_YwpY5_DBi9Zd6lwAKMCu_N0cOcuHXpsD-oujXjdNX5oZRBUEcZHva_FdrptMCQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrEb4vPE91z8NqTpYRSCbwAeT5r32ldV_ccDGvsPi4NoJ4yfjrmRXoO2Pperq7ASRyF0oPHIpTD3eUgeFevr8jZZy6VLDkofz78Pxno9TMW30Jc1bIgUR41Y4JT7OrGQGRVPw6bMdhYVz9nnr8FVgAyZYqOcp0XC0dMVJg2R5b-0kFJn1Jus3u9pHWnGTjzUAW7xnxNHHYEvAqB7JU2NbM2CQuD-tAuh7F_CTlie8Oa6hVvZVb4gU66TUvsB8o-gpfW5VGoKimByD_E29Qul5QKe636lCOcXagtPeox9KuuIhbHiai3HcrD5eUSt58Ayrg1gkN7xD-jrYQcM_Tfm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKiyiI1IsA3l4yjR5QUTpYQI4cf8B4l29NXPGUble8yjEUQmEikKEDh5As7Ke32WF_dVfjEQBKd3jqsRcmL_e9cY1HlrGXxYZrASn21MqO01R_AeF4TuG7sM4fvlFvyYcirckUB1GZIjjM9oT2wXDZMhUEiUGq2HbV8NRZfMSuc3l0VH6wOfh_C-ARR15KtAf_vsTXPwT9bNZNfro-5NEz1fdRIwEKtTPb66wHCfP-VInnFDPLMSCnVRydqv0eE0rO0vtJ2yx1k4OmtcsmEPARMFFIieyHaUTOWpXUcKwkGp_WAUHuysL5dwYaaIse7hv9T32jegeXfhg2P82KitfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMasa4LkXJX1JalzyEq7sonX4RA8JJF_wVce_3HiHS5XToPz6_qZMYRYxMgmsG06Xstbb5dbss0qqtYbu_ipjx0lRP7ydpvxLlCRZZ2BP9iW_ygrEr4xJgRmm9Am5D33EazjJwEjXWeVT8PvYruH4XeN8NLm5L5arCNRc7X6uR3W1PimTSW80wMDMjRptM9So9r8dq5Coo9bETX-IXJnCHicZk00peObijuKmyFNJlh8mdppn-3ok6TQX9ufNzuTKb_kc5JvEJIzBD9t3SR1p_f7FPc-qNO2GIaddp4gxdPL8XeVuRR9YjozeZYxZ5AJt-oqbHJ8bEBAfkdCqvnjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IChgX7FSUJlkrRjgvRac3zcdEuHfXxuniRsSR3p5CWwlSwq9ubZ-hdb_QuIL-oOKyY0zoTsQvhJqKHKwDPzBdTtZBEB0t-ewxFiEdec_KFCX4IYeeVtlnc8zt4BVCyxvTht_AjnwX9AqgbK3XIDoyyZW8xfVZ0KV_STMCVoS_bCAvmXYAJtt7E8O4udSlWuqHe39EOElHeBnkimU5vn_0JyeuB4EaGNdmOuaYvPsSdmgGOUl1z_XLcSpx579JF9Y_PpJrFukyqmA0u0sV8MSxqLt028ULed56jq3lVvcZ_kKvtOyVUbeWWpPKBwsR7nKrYmN6KZ2pzO7gCcAjoTlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyY2eWu_orB6ozk16nmPOTUDTkzFFnfE-fZx5uDUXuJ8B79avRuBMcGvkIzRzkwJF3bR13Nm9f1ocOqZUqs3CHnZsTgusP4o1bOC6JdG0Z13BVYXRbLiSQiO52X_lVaGsmG7-gsnEcxSVFC7zw89xReDgHNHq2JfGT0gHYX3djvxUxBya7oagrtG994ZW4CbeGvmiZ4mOlvzcBoMXACEZNVSICu6r9Cy7yymA1nky3Gx8OC4_8gMbagCR9nfPUwhNG_AvHkrRW6zCBtfGgrtO-bbxetRN0mhXZr_s1E-WdIFZeKHHWot5BgxpBERZDTblqLIi1P3Czs5x__Sdx96iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Qn79PKB14iKQ8gxSTdMMH3cjjpDVxgV0zLocYsghxRAz5KU90y4saFvPac1PnBd2mUyq4t0oGJbAx2JnrlDOZdQWLXLJnYGskbAU23mA4eDCmtW2wudI6OHsVg44oz3rg5nygpIAFxnwNnu_slUoVG-MRScP0hnwuqfxWmO5Nrm9YM21auawYfMOz3XU-aEyy1aQmFLj9xK8PYpwOrj5GP3F1ETny4KUNUiEuNX6dwE-nYzkSIbVBCkJobxXPzOJMf5hzMKzU87XDeiUYu58VLYWGRufOD5GgaBLufIuTmUwmI8HKkqb9-nD0BGNcZnBLTdvpFGyi0ZHgIPaFhfxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=Qn79PKB14iKQ8gxSTdMMH3cjjpDVxgV0zLocYsghxRAz5KU90y4saFvPac1PnBd2mUyq4t0oGJbAx2JnrlDOZdQWLXLJnYGskbAU23mA4eDCmtW2wudI6OHsVg44oz3rg5nygpIAFxnwNnu_slUoVG-MRScP0hnwuqfxWmO5Nrm9YM21auawYfMOz3XU-aEyy1aQmFLj9xK8PYpwOrj5GP3F1ETny4KUNUiEuNX6dwE-nYzkSIbVBCkJobxXPzOJMf5hzMKzU87XDeiUYu58VLYWGRufOD5GgaBLufIuTmUwmI8HKkqb9-nD0BGNcZnBLTdvpFGyi0ZHgIPaFhfxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxK4y_FUQrk9nPwn-PQh7OfngvjaOxFibkvOMq7ntlegDWHSAqVJdFuVOx11Yhndr4SifxAQGYTUu09HcLXH0nlgDxsM3IPZ4S3IZ2hDBOuDcCQulSa6Ihj3oE6U1xF52BYAv49JC416n9KhCZlRcKon9x6DQ-VAsYos0OpYXnBoAT2FsOCtcnmeaG3C-dSYyQ9oS3w3w9XZF7ouAnoP6gHLnsDszvx3pZ7ikm8AfekAZVLbfjDA4Eij8AwJmul9rC65zDIgYRCO5l2hE53yL2simpH7ZW5QQddVxcb4MaCkhSF1KoohNNDnflQ7VYfgCwvG1sO_J8C4Byco0QsPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbDEuE8BG4QxuZ310jj6r4N_o8ipHZ4oD4ICCXtX8rUC2GEmuPjH6FUzgwh4-5r738ni9srBQFn7-BFpd62c86bOvo7ucxAWbiZGaYox49xJEbJv-hAjfbcBChlxiMra9UJR-p_to3qranSL2ATMlF07VUZwh5mstihW9IFDLXXMG459j-jHyFcGDCf_orFIfFcsbMlht4DHtgoJsNqdtCclmaKGkNLGL3yRm9Dw27nahPXVZ_JCj_LToxt8P8LsyZnNK7ThhDI8ribweXV1aN31pH0Q5PDgx2YdJWA5dwXAlwLTg4h7zCaGzDA6DLNG1fZ0dah6s3IZxwbPU0g7aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qplUXjF9h1NLZR-iUD5ISHCGZPImEJYbZr1kEBSxUTbx_nOuGvi-8i6ylp3WbwOkR9zx2TLrGGeZqyOo4kQQQaJALdmZRMXP631anlCkrFH5I8UJ0geVBd95DgcQzGCRt83wU3NmvrsDiu9ni9E6sjKLMYsy9X7vpq46p9kcNrCT3m7fkXmRPA_hdbRYyKRTmfRysc5yQVoQAiBTy5AwgOzy1EqOWWPqB9Efyy9_GrMqHGOIN6iikNawuijj5ontbn_FN1P0sp1Zq9e94fxQlVTktyntA6ZO__pHzezc-py3QKO8QQtbqMB7_VPOayUcboxSb5QhXdbvhiQnMXF7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN1TUnzvskrrKtfGF4IrUG_rur6WFs1y2CevhnaTqNbo2mBKjVGUuuZ95MraUySQgd0Gl8rp00tw2D9zqsfUHrChP8_mlgs07Plsq98ANGl3JslQwOUVhbYq4pRW8ShIlkIS2Jp7lzM97N8e-AgvEmfTggHH01ITYRTWexAhHlh_j6CskFydfGSi0Og4gAsDh2n7QIlxNul4ExvlfPy_nrTsLXuaj-K0xTRIuN3_U94PgJoyuIxisLwsSjfOq69fyrAYbh8LlCIohqVYyiqmH51pmy9JsDuxXjmIpxrA0PabcO1g_VkRuRcleYJTpiav23n_O7J3hR5907DG95q9Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=YIMYhNpynemR8T19DLoiW8pa1Ytj41EVeRWsc3WQ62lBaarK0LM_ckC6HX22fCXMSkkJ80RKoLR8cZRsMFwpDTEFHafN8Kf_zJUDaS0uy1h2ejujEoT4CyrLj5e7Uj4qieU98a0aIGG2zw_R3Kaw_o6Iqsjn_F9-ElsSEWwo4sKel1zUlhx7zs1O2xu_DPuXEzksaxkgHbs4aht2Ko5Lp382RVpErJ8-j1BwNKYLfdVIwWwtyiLK_aHSz7X5qakkokorfjO4O0k7ar-F_zcDQ62Ml5SBxSI_VEkb8FhQcAj1d26drO9FKDHZLd2KWXXa8-t9ZQUHvBH0Iv7uFs_Llg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=YIMYhNpynemR8T19DLoiW8pa1Ytj41EVeRWsc3WQ62lBaarK0LM_ckC6HX22fCXMSkkJ80RKoLR8cZRsMFwpDTEFHafN8Kf_zJUDaS0uy1h2ejujEoT4CyrLj5e7Uj4qieU98a0aIGG2zw_R3Kaw_o6Iqsjn_F9-ElsSEWwo4sKel1zUlhx7zs1O2xu_DPuXEzksaxkgHbs4aht2Ko5Lp382RVpErJ8-j1BwNKYLfdVIwWwtyiLK_aHSz7X5qakkokorfjO4O0k7ar-F_zcDQ62Ml5SBxSI_VEkb8FhQcAj1d26drO9FKDHZLd2KWXXa8-t9ZQUHvBH0Iv7uFs_Llg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXhlGcjKjVXHgjSAMvIf4Gnynzk-BEKRi9moBRO6IskXQUksjqSgpY5kX-ouXX8NGUbt_bOvkmqKR0dTdCYgNYfYcgJdqStiZp2_pmgykN_OpwlIrJYoKfKO4Y7wg8nhLalBkY8N6mAindBp_X39doJx7GvsRUndwataZe12_JlEF0GnOTUqUjixBd8OKZ_jQB5lu52EKfuAPxNylvejw0z8zzg7Vp5zygGTAESy9dqDZ1mg1QltERvdbAs0UFe62p3mBSiTMAA7-tZqu4IqC6E5j-GZOZehK1RxWvyGxl8v1ze__TT-Q2448vQgx4BmhLMaUqIqKSNsQkQxDf3s9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa3cCVXygKVHE6b2y3r1ErOumKWeQDvLxvmIjtB_qFX1YOOZKMXdAFi-szcKV_xwdHTYYrieoD6KKnDoe81GU-UKYu9sVA8UWc7jGyGoXy-23tESPVElvG0YAlQlVAVzb_N7UZT7z3xloo9R7D-vK2pQDR7YQNExmay6sAuYeJqDobzoVGfLk7f2Ox9FvrODL9m8kyVhv_SNs-TZguKxSRJz5VsCc4p8euWvFjHeCckhbtGgbwfChcQCbBvZJKn8NPZrLVZ9kx57LEyritMKEeQQOczzYlhwN8-5ijSXbmYExXJHc6bT6ULSIeEjTPoyHljas50up2ikSC_MJzx91Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZbO95lak2zWFULe0g7gfRYPabmvHzoJIyc1y_ESrwrzXEuiNu4-SiUjFj50z4C8BuNWLZLDOMP824hma9Zc824Dp2UMpegLXTwZIl3QQv8Lv5lov0lJ1XR-IgFCHqPDxm8pCf0RV47Rvud_SX298EJpTomIDmIij6LWmLG3biEsz2XlTFI4rupp957tFQjxAdXiiAmuh2pH6nUT_ws1yJe29NrFLBE07ffgT-g_PBuQ8smq_mIWT5FhbFqvS8PYQ0ua29pCcDpfRDa9uI7_1LD4H6s7jzwj_vBY0PttvCg09ZmuREkXz-Hh9tcuu5JCYab3XsxHTZedyCSN5EA4Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=SQYMGdHlvq5WeyZDoZ4HZ8-hCYXpSGa4cUqJ1Ol09CvdEExmDQaM4uDGSgQZkx0X1-JWBde1xyHWE8LmmoOL_qIyMvvA5wdWVmgLAySmuc1WTE_sbA3y_vucepM03HIF5Y9jocEbhFLpzcZLjNPBGPxKEAecRro2yZtnFnek6RZhFafy9-6PLgLdxnYJRbBk47qObEOzfvQTNWdR3X8ZYlFiERiLKS1q00yprAAFJD6WXEKXQWMpa82Tcblgyi3fntQOkj27CEPSaC_tYbsxrQDcfBWvv9WRx7G7ufC0N1BfONG8iWj7HPszep38--jCZd8kQgRrVxrHvD-MaySJag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=SQYMGdHlvq5WeyZDoZ4HZ8-hCYXpSGa4cUqJ1Ol09CvdEExmDQaM4uDGSgQZkx0X1-JWBde1xyHWE8LmmoOL_qIyMvvA5wdWVmgLAySmuc1WTE_sbA3y_vucepM03HIF5Y9jocEbhFLpzcZLjNPBGPxKEAecRro2yZtnFnek6RZhFafy9-6PLgLdxnYJRbBk47qObEOzfvQTNWdR3X8ZYlFiERiLKS1q00yprAAFJD6WXEKXQWMpa82Tcblgyi3fntQOkj27CEPSaC_tYbsxrQDcfBWvv9WRx7G7ufC0N1BfONG8iWj7HPszep38--jCZd8kQgRrVxrHvD-MaySJag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re1oBTFjwsvdXPdl_m0-g9IfQc0GUvVGUm_nGjSDDii8oQ6sguKgSJw4bJAfLO6qkfHGqzXVx0nDjOD7IiBI0VD8uD6alS3vrfWG5x2pl2LvKPv8DKUw6V8TK_iKc1yi1CwzG7KvcNNoPk9e6FNW4AReHckQp0-H1cA3a4GkWPbJmA7KLCv5PCm1ecIUca3gscUmY9eUlHX4cw0B9-Oi1jCiSzZeBJmMuBIWHx6bPvHgDrQ_9-IdR9cc9gluaUHuE-0jjQxpv9b_z1W_P0Ugr2amzp3Ks_W9tFUlgApfzQ3-Bfh_AUMtNfJZgR_Qd4PKS1IsvrW0S-gl8FHQ32qMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8Cf12WYosjJ391L0Qtvpx4dGPJTqpB1In1K60eAq2BBU6Ty2KV40g4QhP16dkbfPO7rudQ2fFHuhwbg8_2nu2JRXwtg4zNsaD84e3HtAQ-IK2s5Y5wkLtsVWOAEaUywwLs7i5KNX5xKqLePEqPuAMXKXn6Sk198WZMn_WWif1fgnuLbz_ukKsba4rTYbwPJTB9E-YoJltO9I2WLTj8bgY9eRMQN-sG01PLA7yVANdvnTcDNrSH5zmSm-bykRX_zv_xmDTYC2oW99FFNu-GOx8YV1VTPE3lzG9p-AE6KrSLkhsgn4ksNmMYhpZPiU9ugk5_pkZcacSIfMp5rekCUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaNQ3TZHmKiSORUM9MUWahwXFS_O_N1ehI-zJSuJI9MhQ8nI7va7tawmzenW-UgVNaTk07w2tiB242XX7BMoy7yHuPZ2fHfmKI82_4JanN0_l-mbizHZAYoYILRFi_Fu8rLLEzbtX9Jb7uDxUSjkc_q_GxFex_0k7L3m6ByWh-8n3r3D_nxeR2kWBte6IrAJNXN9t7rNnplPVXKcx86fI9ulNQoFOghCStkm2SvG3qG3C13sHLgJGIakWws1GRAQQ4Y1_N-8tGczz1VJZi9LIocsS8FsYjOMBFqsRJNDhkgd_u8WPJhRyLka7RNxbCZBoyVRBtkMtxODR-JguRihTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlGUH_GP_tY1YT6mv0sBBhK9Gybicj2S86UIAzYPC_pZhmjtNJU9FE5F44Z5RBStI2PLpZk73YUR650Hm6NhiaS9G1EiZ2w1heA8DluekM8HtsHew49Y9spwhccJrI_7Yyo_GP41_riXJGF3GHYWk8-prD99TiaIpNblkQKH7wCwkc_xaqzCgnSOPq2EMD26BOWZPlEeecgptro_4A7YuFxm7bqCEhV98hDYO2Vi7pLr7YRL7wAel-WLpFuN3fcFgkyVOkWKf71HQcvxQ6NhXnhpUZJQ16iJpOo6yTUPCt9gy9SLTUcnsbeojLm3HwflV5qEpGF-8Oolse-chxtXbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWGgS7nsBycj74eyIBdOSps6Bp8JR39Pgfh0JWLInjisNdXUYwqn0zefvVAxpxCk7D_le7wBOYIxTnL_0rfBtqQ9HpvHRnuvgmFSSgD2CncVKKRlfHpjkkn-j8qDMxV3ErX1RjR566WAm--eT0GdL6dvMw641L6INW_V4u_kzwDQaJpRhBOtQrJkxpfi0TAXwEZwIy2x8EI9t7Uf_Ab2Uywzze6YuNFwmVTU4HYTTW9WTniMs_n328OG5WfCP_B_CVHByf0qpHvoVz9uFPOex8Vo9BEGuL3eCSHDbl9oLNW7pQjTbxGAzdffhpRBhIV-yzq1rQ3Bm-PskDI1Oh6NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAva_go5xRyKigjPaV8VrJsdinbu8x2ZugulzE7OrxvKyLWxtFE3b224VthiCv-UvuoEDcIVreqqbrm0is03ds1-gWLhhi2WHWM_AmU8onrw53OWEFFRnFu2TvMMc2w5Mw5kQhlbg1nsaU-too4GaX_P83eau3dC3Qfn03_rZIYSkY8ClEmGbh7VFfgnzz9unQu1JexNVbQbF16afzY3RuxhAqaexn2F584uO3oIUTEM8BHHoScgXkTn1FaBUR93DlSQwLfdO521f3ZCJ2fS5ggblfzrrWF8z4DpJ1TOtkrP5Au7sQd-GzcXqPWRxcgDklT5yyVvWkfwKIQj5Ix2WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=KAuq_blT8CGqwqUULL5wfvfmPGVY0_Gx6QNn6xKXcC1DdU0zn0uKNH6AsUAGun4Q4EeA1HTdnIrDzasvvJvvKV89v4YmAvpO7xLXcVSa11OGPR-FjWKlPr0hyiKdlOXtwZKPWMnJt-ErvvuMz7f0WHKLBWWmxKFZ53T_lmIwFKhHbXAOiZY7Q9VoHjCr-2khmScdCIvbLrlglW05rRQ6Xgmvfq-6YeBxdFufC0qFsBnYD0kR5efVKD-Fkgd7EHFm6Cmq4pZ2jgFa2vtAKLIqVTZ4hura4pjPQolqtbz8QpQjRM4xtbMNK8ZAwfsJhjZoLOGgfz2G-G_jU__Ujee-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=KAuq_blT8CGqwqUULL5wfvfmPGVY0_Gx6QNn6xKXcC1DdU0zn0uKNH6AsUAGun4Q4EeA1HTdnIrDzasvvJvvKV89v4YmAvpO7xLXcVSa11OGPR-FjWKlPr0hyiKdlOXtwZKPWMnJt-ErvvuMz7f0WHKLBWWmxKFZ53T_lmIwFKhHbXAOiZY7Q9VoHjCr-2khmScdCIvbLrlglW05rRQ6Xgmvfq-6YeBxdFufC0qFsBnYD0kR5efVKD-Fkgd7EHFm6Cmq4pZ2jgFa2vtAKLIqVTZ4hura4pjPQolqtbz8QpQjRM4xtbMNK8ZAwfsJhjZoLOGgfz2G-G_jU__Ujee-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu57v9bP07AaEvCl5KqholUsfLigT3i-Own0Nik-6Aak6SPbC9pGGOLpyVtv34QwBqTF0t1ZsHDNivnWgFJKK21CvwXMjJnRuHAHkk9W_lohb1EGaSDMoJIbLInqOtkXNLTGCXTYazFYzVpRqQXOyFE3zLlK60bWJRd4IEmmDo1gnJsWhLs-BHpyI85PeqyaVHtYA0T7E4jtlF_XauobIkcIX75z_daHL4_9MXKd420D6hwPRmIikX3M_41GL2zrEo5T_aH3E8IIMUFhF86GaIpb69iWOLw8j8EtVwhGZEBA0ePkgf0fVrCVYHpgUBcYVWBjKuyFp-2rZlL50P_lGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoTgoGGN-7_DuJMsENikN1xHe58E-2x0s_5WqK0Ijnmcn3kLknblaKv18sbrQ2nhILu2HWPTKcbTD9oh84qZEM-6g9bp6C1caaMfFkVEe3kk69L1W4fgnHZjhuyV61kMR5-2aCwtBhDxadt9x2ZYSSf34wlmneVNFkDOJAPkuVoWCaoQ3iHy8FByo2l6V6ZNlG21t0uow_h8NXg41_HqN2_SBpMASWVvNbEm-jK3-zGcFGhlTIKK2vMr0C0sV_jfWEu40CaLZMtABlax0FC3lNHZKXoYz1lN1B_Z9ChsAuoz4__Od56wtFvs7Z6vtJO9u-B-Aje24SepXN0zqEceXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-V_maG5vAk3jlBDdpdvvKg-3gKDqiWasy5O6G63RX8pQsrXV8LW5e5_rPBjH2X-d4bJyoZUN31ESx4N-dU40IVdpUoFBbbkfU7Ois5PXejKcAAnxIxMyo0Ri6Q1nHINe32hu-tqM6GGHBmvs9-Frj2V0-3_zw1vo78mwEihRmgio6HVV0ofl6i12Ot5r_TUI_ubonWiauOSMYkex4rOT5oZODtXgsa9gtxOJfsxlDUVVI1s9BOTWXJKX7VsTCfBY2vOR1c8-oSQGX1H68zUH7MZPn5elMPnkR-_Izow-cHIaf023p3eWyCQyP6Q1hsMRHgvk4I2iR85yJtccj4JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
