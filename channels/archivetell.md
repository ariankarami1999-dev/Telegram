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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 37 · <a href="https://t.me/archivetell/6427" target="_blank">📅 13:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 371 · <a href="https://t.me/archivetell/6425" target="_blank">📅 13:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 719 · <a href="https://t.me/archivetell/6424" target="_blank">📅 12:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 955 · <a href="https://t.me/archivetell/6423" target="_blank">📅 11:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 986 · <a href="https://t.me/archivetell/6422" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 955 · <a href="https://t.me/archivetell/6419" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6416" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Heybaat.ovpn</div>
  <div class="tg-doc-extra">8.1 KB</div>
</div>
<a href="https://t.me/archivetell/6415" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">sadra.ovpn</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6415" target="_blank">📅 04:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6414" target="_blank">📅 04:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6413">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6413" target="_blank">📅 18:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6411" target="_blank">📅 18:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6410" target="_blank">📅 11:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6406" target="_blank">📅 11:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186940244.mp4?token=ZeoKXL5yBuvD34kQV0zkGf7qn3SoIb8ESlQT1QJFrfv3ucP36zKyTe4K5RRNiX_itf94kyA5h6aL1D5xTiSnMCd5z0Zem8wxg-ST_5eRlvpvlf6UaqkeQ7BB2UUTjJ-bfRNPUgU4FTUCPPybnXH41JQIuh0TWYjBT2Rj5bYAusQzwp0jXg97tvEx3FQKf8Hmdzo7atZDrZttCein5BUH-3379O9EcFZLnXX8LJw1fIOhzQ-iuHsQ87ulyk4Jilw7HQjHNvftcWIlLsOYUuIqxb39ruiBoUZspkc92EEp-XnX74mJ4MFqn-ugPPn44DJDbatN65uEIOYvqPGuRugIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186940244.mp4?token=ZeoKXL5yBuvD34kQV0zkGf7qn3SoIb8ESlQT1QJFrfv3ucP36zKyTe4K5RRNiX_itf94kyA5h6aL1D5xTiSnMCd5z0Zem8wxg-ST_5eRlvpvlf6UaqkeQ7BB2UUTjJ-bfRNPUgU4FTUCPPybnXH41JQIuh0TWYjBT2Rj5bYAusQzwp0jXg97tvEx3FQKf8Hmdzo7atZDrZttCein5BUH-3379O9EcFZLnXX8LJw1fIOhzQ-iuHsQ87ulyk4Jilw7HQjHNvftcWIlLsOYUuIqxb39ruiBoUZspkc92EEp-XnX74mJ4MFqn-ugPPn44DJDbatN65uEIOYvqPGuRugIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6405" target="_blank">📅 09:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVVSU0AwKUaLavqdlsMIyAgxvkb8-hBjciPlkAlMFGz5VPjgN8ilQvUOMqs9SwPoLhnX-IZplsDXnTbW5_CAzT0gdKh1vqZKpdbt2WvZwxasz8u_EWI46jg0qlroszuBygYaAjKP8Bd8nXuGuTeweQRNftXSZvf8aBTOKgQkLe3e3mj5088Y56dg4YvOxYbQXqt1IpjB6wzAd33gn00zI5k4WJOtf6hm4pK1z9KKUV5nFhEQ06NV_xAWOMcQDmpz9EzsQCfHeN5AYJ8XQSMUw0TXH-9nSKRkLALOe7il7DOeuFQIZB06F0BLGK3sBLj2NG0c9nbAt0-pzWQnYjDJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=ElYveDlnTgQ68-R-WtHHVzL-3yR5PrZSH1hqN78DJYtSDeiztDLRAHGVO1ebwq7e8gncBUMyHHUHaFWWJDFv6e80E-Rpi7JtWPde1UEucsasRnuRwvSD_LzZbzOlhGdN0RJv5EwayH30QHbKCDqpZsQWPfliGKITX-tlU8Z1knqIl2eDIEiJ9lLj61KYqhRi7wTBaBXG95RpWMOU5okD_BmU30-kNvSeFYDpVTrWeJee-ZU-vgliaJI4YMlClD75AorV58A5nV2AZBMcZRv4BFYnXoN9f65dlkK9tsJ0pHrBwlRaiDlWsK79OXh7rf__x0lqhTYRurOf_fkuY3kNug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=ElYveDlnTgQ68-R-WtHHVzL-3yR5PrZSH1hqN78DJYtSDeiztDLRAHGVO1ebwq7e8gncBUMyHHUHaFWWJDFv6e80E-Rpi7JtWPde1UEucsasRnuRwvSD_LzZbzOlhGdN0RJv5EwayH30QHbKCDqpZsQWPfliGKITX-tlU8Z1knqIl2eDIEiJ9lLj61KYqhRi7wTBaBXG95RpWMOU5okD_BmU30-kNvSeFYDpVTrWeJee-ZU-vgliaJI4YMlClD75AorV58A5nV2AZBMcZRv4BFYnXoN9f65dlkK9tsJ0pHrBwlRaiDlWsK79OXh7rf__x0lqhTYRurOf_fkuY3kNug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liNLzIMS4r51GohforYIfhl0vh0Ep0Sz967mCZVv-bkcptWVLNTDrJu-14ERTxPOBm-G_of3lR-dEoQRGPHE_JRSHvCOZ2weVDyvfx0GDRkpzPDDZTisIYkNULgSoVTPCyUUv6_PqCUBHJ64X4MdcgSpgP9QsElLrjDKaaV28YTZA0ALlg3yy05loKDHqK6oXvJDxTKajq3JWfNpfJ9NPZuRnAaG_O_oSSnPQRo_fMEX8WRJt_ter5jlF0BK-o6sDS96X974GjBvdDR04gTgiFQ84uoxm8uBkFeAgg9xL7Zrhrs3gu7_jGDmAOfapss58R7sdvLsQjsSuaBKOYe76Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhsG_33O1BOdko3gMrj6Qbw81NdUY_eCbFI4BMVrhb5hqB5Vcjeo8ODtcmxsCixHFy9lSN-bBs-kWtnnHJ2rCZ8nP5Mcj3qkHeCEv8iSc4ZPomwrBSVtFenpePzxRGyAWDmICmW8xIRVlXHigxCeC92ONORf9vkiwORVUd-AwBP-ojh0UHabGQg-nnZyCS58kUG8aadcZmH7IJjIyLXPFGKOHTyYk2gvGgrdZ3XCd8-i0c0bS87ztmfNbnw_GnF0oXVsoEkudSL-O9kMH5yhccDQgc8SUhKniRdlYlnnqEcasSv4rl4hkmzf_uj46STSwDpecLiI43Xz0qjMWCPnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgiN8Ye4lX5GTmQLG2h8WvZbzAMmucA_6ZyiCF5veNyjgcqRIC17kgjANTnMlEszfhGQeyswfpBDILsqFgePnVTHq83xkRVwPvfdQUi9ssl7hbIIxhYe_j1LNEaCdMER5lH5wvPzL1M2Nyf3TOB3UG74Rsh8f3z_ktn5KAt2jbrWqgJLY58Lz9u-z_hB1Ks8slHsn5TuIxcjaujqWXwayRyNSj4YJU-UVZFD2rB7arHBbL_WMXzBK0oBxDM93lRUcf08QfG7ruye82qvugtfhwzfvOR1iadww-z6gd6S2yozNdb5dQxwffNiFvuSORroHaDG5w3kVbg5B-FaATORLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfeIsBs4_r_yBwEnYBlYtaSWhu4fTo1MeU-oPVX4ZapK48YVnrAyzjGIV4JVkjHl64kn9xutpynfE9zOWlMb4YPz9eM7b1VUelf6rTLJSzuqlrh9HF1hgRFUL8YWHHVvRHO8JTJbfMHGpeVD9C-JhFgxVKfzBxmB2U1JJWDPp7VOFmq46nce0Ne-rRJ_cUxj0UYqElNCKYc6c9_jveP2y8rNywAIidN81OIX2EyDrD0zTB_9pnLj6aCr-zoN3iJzwSKOPlVNpDcyo3X-aeUayte1FqMdO3pmx-ok_kVyidLxoZepD_4ATpmWvWicVw2GpuwL9Tx3dKtBQ69aKjXfqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3xqke_WIO8NTbj1a7CnLAF8hWNaFmltEC0Gvc4W9Hx9hG1DulWItBIBEXNKwgSuZA1V6uwb1FlzqevBO6jbICm9fQhIOEbCHFoZ04fMTF5vbKGsOXq_epIXBPkbqv2dMAC7m8Iwt3uycTczsGrtWqO3unLbwvmrirhW-D0I8eyPtYTUM1SBmdCGWiUVh0wLDfwEiIeblOGNDNAU3wJopE5oVW-AWr29V2gOGv6db_fP4SHsUjCy_K3KTF76DkbqhpKFvIFPJyrkLVhq2kQfMfb0qhGKzWhczz6n4_iHG4eryyrs4s2Vjyi4RlnHL4claADRpgGnTl8RPHbYf-nQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk-a0nyIPueCuvdMcHXPL9Wba-2RV1ADX1G5uPOqKjRiidIUVQSQFmki3qITnWHAqaBlzjS3C2yi9Gtqj1CCDGgi6YemZh_OdUaSrCTRbOC_RlfQzHDLl-92KTZ_GoRNwVCYe-kKtTYBuprLRHEQuigr8Q3Y8WHrQaPdTRipoKedWu5slhyJyB9Z02Z8D3HG6yBJMfF0MxvVJj8ljuGt5dcpdJLVIwET0jbsqRP4iWolucHDljN5fx0xrWVYYQpBicnop6D3k9fjTAeq3yXJreyprj8seUipJAaz-7QvyROi-3GOz4kJAZfW0ym5N0IfewtsnkkU94mR5cqdsd86Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld9cY8_alZopH6JX2MK0EaTksZgHoTDCu1UfwX_SXGAxWsp8m1P6EEc0QD9VStS0XDxbIf_CnWMcqW4tqoHY_SNY8VPR7n8KIOy6c5-1uS2UCVXT5QeSTEhFAZ8iPnQRdoZhc9eT_ijIgWs_VciS_kTnjcX9-qfyd5Z5b8j0RMK7KzB9fH_Ozmk7OdXS-0Ustq_fa1KQ7zNrfIeDoNE9GhS5bsX-p7vIBcjCnBbXnCha_RXXqNBxQC1y6OkQioZFa9HKOtYRVVt30ZFXCBquCCqYwx9oM734hsACL41Qvtd_aFtrw0-HPfSGnwARhdEjXK35WwkatIR58es0cX0ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHI9rxZdSJ1i00onzsc9ERj_dAB-TnskqdViuR8IrKlFkgQE5K0uAONaBhwqU-EiTS1CN_gMqaadohZOsu6rZ7BWbpZQXYVaKoqzH2EauqKDYMiFWokTkM7CTLgarw2UvuoHSQFWrmHNhLc20bs0J2zBDYeGOVJRm163hRX3BamwXHkZJAx-w6nGlopgGgrwsGhyUfFiDMnA7gMUdZnHsN81hsSUV_6qSIpk4wAqdGVJhlO6fdSGvA3E962UqEX7WVj4E-001TuXEZm6WsjfPr0n_H2Ojpglv1dyp0bI-nhXiHcqphWYQBjYgxZ6HU2-ex7Oqnki3t7OcI4QvUHY5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL0_X2yF7VHHpBMGMlCd3Q9blVY0sQoMswmDHr7pTwS4t0wlAR2eiXFxrLIreTJuHWW5Ga3Gu5779PCvroqlyT3pwW18dCaABRMOKgn2dHbaN2rRzx1-91DYhQijMkRziTR4s57OYCl4EOxL6L5lLlvJ6A5VAjJGmAd4U7Ysf-mLw6MjtrJOCmdvrNqCs4D8hUm1yjJOK1HexdvTckpk1vRovzt4o8tUQealTTW9dl7wL3azlTFFKxVAC2K1KQp9Cv4lSkRhRroKgbP-9U2XIsfNHZzIHIx4LD2-5mVroasq0ZOTyhTHT5EcQB8DF-Wfyo4lEtbS-eLw6YI_EAISzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAYetR-ZPg_jXyahVjdxPQ580GhFoqlv-pPtsde1_0e1YlCfiXzf77Gu8lwgMcMX7hNMcxjyjxQyn3qoArqq7X1Fo9xM-cesN2h27RPNCpkTmqj2UJsaKzvfCvV5i3kLcIUOhYEnPrTR3YLwvf0MBJkeJscXvDRPxTvP2FgdU_f1rLbbDIbKuN-scfhkQEtq_cnsK4mvlf4276SRuHwtnvgetNf4JLCKts5W8-m4CT1cLcLorvewsHGff7x-PNkBiUkDxCDt2k-4HAUo9mYJx7_j351l3cFXAXfVMZ2x0w6V9r8f2tjZVtq6dUdv9bnU6C5pBfbJn9PYTpPn2-_beA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9wXtAx-luPQDJsYvCsT_PKzSY3YLGjyqXkzMOKrR5qumOibKo3-zDcTj_avHKyrwd0zphfI_j5YTRUdiOVieCvaw3ntQTXABgOqfLRCDjNNdTC7x5O3D9s4S2fxFhHV7QWOrkvhwqZDknsryK83aEF5tK__f5M1qZRlcgmgCpRzMuFFjSmdk78mzAn-Bi1tO0uT3MiuMERu2zWC-b2fc6C7RI0WQwTyihiWen0Tk9ilbZwdDCYStl92F-wTL1Mmu1CQ7IYkhQACOW3_FXU3UoB-Z5XI6S1ETyKU-QkJRvF_T-lNiHxyAIGiuP8Vy9OHEZnMGc1Qt6w0xhr8mI-AfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=rBKAcrCTb0hyDRnybIUmfzvvzPhEJV2m0IYce8FwWuLa9fC4NQAY8rMVp_bodaiI3IyAo6BagKX-jZZ0WUHcmRpHRjNfYbpFSbAUVTr__Q-ho6uizCSSKCN_AMarO2vzbB6uExnQ8Zo1YRSZObg7NqXkcOFDqRS9fVAxBJFi8sWgiD9Cv02ttSevhHW2gYWo9rJMAGCtD3yjs04uiCoYPnBn3E7K5czo5ssojcXSh9bjE37ZouchmMOokfrhLX1P0zOVHz7Dmxms1rK0MUlTIlag9EJWBznBHVHRHQ6_IUVot9Ur9F_LmEqBMWDNkGsSrzAUcPMNOjcbKrJi0lWXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=rBKAcrCTb0hyDRnybIUmfzvvzPhEJV2m0IYce8FwWuLa9fC4NQAY8rMVp_bodaiI3IyAo6BagKX-jZZ0WUHcmRpHRjNfYbpFSbAUVTr__Q-ho6uizCSSKCN_AMarO2vzbB6uExnQ8Zo1YRSZObg7NqXkcOFDqRS9fVAxBJFi8sWgiD9Cv02ttSevhHW2gYWo9rJMAGCtD3yjs04uiCoYPnBn3E7K5czo5ssojcXSh9bjE37ZouchmMOokfrhLX1P0zOVHz7Dmxms1rK0MUlTIlag9EJWBznBHVHRHQ6_IUVot9Ur9F_LmEqBMWDNkGsSrzAUcPMNOjcbKrJi0lWXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azy9idK5xm5J3M2Rr7xB4gKqwYiTAUHBuFeOBQKt5yGMSYpD9qBDFwYXpJCP1nB7dz6gNotcGi8vmqqi9FfpMP5c5QCqY4AfXLPcfCFnYvR5m4IGuSVkstdkChuZHtiAKnvrKPfYVTmzncVwbELoe7369KmApP-jiim0unfEEAMTVW0j2daIwvoaPEsvtLnWwnsiofgDtw12ka4iSJnyXLwBxxRy1hsokvFBKYzMDfybHnNBjx30EEj6nVvoqf8XHhxCQL73R8KxmsvwJcBK13lpttPRn75LAPo1eAHM-w7p1Kcto5TwWxru6AG55hFSmvBQRQOOiV7djMjNeJgGKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP7YrrBOE2DV-prTVqkzx6wVCDfsGBB_HGOcP_NwSNbWq1mcJLl_0G4XyZLu5dYNFAIiYoleXkkbdZ8wKj6Nff-GD68LFHwB7sF2KShaHxroLoLHA4_6EDkdpjhwqU-43vAjiJ4mID6w1exOfDzVcJmEFNouuNu9FuSnAcKZPI6XWqWGGEbKzXoEjYT0uLLefBC62Ge7j5zfXPLRV2rinuuusAGIO1BiDrxUS9jSnbbwCgUrw6m4DhxMwlUjIpiVJ0YTXZbeGULqieo7EvKbIDgbuHE7kRnGW43r8buepCRgqIWxfooPsYHjZpDFW30LLYosS9bnh2iqEgEZhzM_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=WhxQ1JyMH3LkYKrXO4VhBIem4ezJLfURIP4wW6hjLTmeEeAEIaOeo4yimR3ba8agI5O4Hdu-inAD-3zZFKCTrH5NAVzc89oqtSNdrxQjExEK045IS1p_8KOFDBK5A61pBIciU8gDzkwOKpnhdH9qDpRI7Sy4SQI49qlH74lXjmbPaeiS2Df73xCqSQqDXfARqzCRJ61cxf4_hR6GO6Xkl4_6xnVZhr7CYCbbv2yLGZFWRi1BRovpFfPFS4qS6yPuk3UAMjhZpKdeQPao975tzBeXJXhq7K5hntSdgNDA9l6nU3c1mFNBAiioGF73QJRDSMiEp0RZU8IXKoJTw_jBhnFgxQwmatsjfnFBjjPyCtoVJdaeG0PMtanS_LkBVZKg7ruPxVVxRCoEuidAzIc80olcVj8P0gLNIfS-8oFFQ7vDozXNZq_LQdqjCUyKguqHZ-qvgK3-c5pPkfZojHcQi2aAkFRONTvUXNABaFM1bAw2NUS3L3SY3kyl2kejQacXC1h9AygLSMijIV2qOGwui3OLovu7p6FW8gSSWcgK9UODR-7x07-VWQUMGTVQIyuqriJJH6-NoM78u6txaaQMmENQXUCsVNVMP0MhYHN19ltiG83taQWoN_6A_Tken6JrQ7oFcA0tBOvrOpoChqn2fnxDFUSVkBX7xKQVXvZFvDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=WhxQ1JyMH3LkYKrXO4VhBIem4ezJLfURIP4wW6hjLTmeEeAEIaOeo4yimR3ba8agI5O4Hdu-inAD-3zZFKCTrH5NAVzc89oqtSNdrxQjExEK045IS1p_8KOFDBK5A61pBIciU8gDzkwOKpnhdH9qDpRI7Sy4SQI49qlH74lXjmbPaeiS2Df73xCqSQqDXfARqzCRJ61cxf4_hR6GO6Xkl4_6xnVZhr7CYCbbv2yLGZFWRi1BRovpFfPFS4qS6yPuk3UAMjhZpKdeQPao975tzBeXJXhq7K5hntSdgNDA9l6nU3c1mFNBAiioGF73QJRDSMiEp0RZU8IXKoJTw_jBhnFgxQwmatsjfnFBjjPyCtoVJdaeG0PMtanS_LkBVZKg7ruPxVVxRCoEuidAzIc80olcVj8P0gLNIfS-8oFFQ7vDozXNZq_LQdqjCUyKguqHZ-qvgK3-c5pPkfZojHcQi2aAkFRONTvUXNABaFM1bAw2NUS3L3SY3kyl2kejQacXC1h9AygLSMijIV2qOGwui3OLovu7p6FW8gSSWcgK9UODR-7x07-VWQUMGTVQIyuqriJJH6-NoM78u6txaaQMmENQXUCsVNVMP0MhYHN19ltiG83taQWoN_6A_Tken6JrQ7oFcA0tBOvrOpoChqn2fnxDFUSVkBX7xKQVXvZFvDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=CTdrLDIQOT2HvX4pPSYBaVmPxxBgTpGeD7RBlMf9f060DN4-bqraDrlsFnjWfd5ctHUloHmAdQqgAS-MO8pedmrqm7AESZuTAkXYNAcK0Osn0AbwYusMG3IEdRqAe022lQ5UkwFizQnmcqPoJbWE84vv7vZlb_j8HxctyM73Ye1rSrw_ehL1IOYPSQHW1xNwG3Mwt4EehZIUr2p7ymAjngtgz7uAvC8KOp9QxR17GyYV4Tbb_LI4JF1giZTCwhvgzsiQuPEfUHYFkMGnW2sg0OVo4uiuUVSeCQQOTF6JhH4f9d8hOWnz2uFMHA1GRi8bR_So032ojUS0RE_tnpuZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=CTdrLDIQOT2HvX4pPSYBaVmPxxBgTpGeD7RBlMf9f060DN4-bqraDrlsFnjWfd5ctHUloHmAdQqgAS-MO8pedmrqm7AESZuTAkXYNAcK0Osn0AbwYusMG3IEdRqAe022lQ5UkwFizQnmcqPoJbWE84vv7vZlb_j8HxctyM73Ye1rSrw_ehL1IOYPSQHW1xNwG3Mwt4EehZIUr2p7ymAjngtgz7uAvC8KOp9QxR17GyYV4Tbb_LI4JF1giZTCwhvgzsiQuPEfUHYFkMGnW2sg0OVo4uiuUVSeCQQOTF6JhH4f9d8hOWnz2uFMHA1GRi8bR_So032ojUS0RE_tnpuZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvV1Mxb2o5OeGvw0_824VGybi3pZQ0h1Y_LcSdOitlvjhiNM2aYqN0o5lQHC1CLqk9UtesNs38HgmHwgWxQo7_HnTljWy1G_65uNdVFWH5gmsUjFz4_gcbLlZC4d3bkN7NMquc5AdJGVyA2VJMVJLFDQvYdQpcoOFhB-mT0pMn88x51r35sVdcjo8noLJAqAGRdGUz5pdN6wy-w3nFntDwR4PXXGIIsdq6r_ozsXj5ci62lClJCyw2Q6JED84EYZ5kwHNPHrwGqVCC2T2kfU-zEeS3Te8wIP4BCInIKzrEoDZenMaCJfV8W04aTa_9Bc22nL2N_Wgv_jz9kN7fVheQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNexXq6w_1kJTreepn0vcPX9ytnBi7oGCFuV8p-YKPO5Ukn6GfEtcbLTxbCF1g6YUDzp52CSzNzqlD0H63oTRchkU4pFS-1s0zph2gYY7p__RnGJMfqlZkfElSR8Xzjc6gb0DheESmYLXm5GPXqaMKUbs0t41wuysuH5OAw7863q4Eq8CSJ4T5uq5bgbrwoPV-AiZ7jGP-732XlMB2XwgVoLDPu-ZsC-F89dsI_TqEsC6VGKQomZkwljRJf7E8JDzNj7ljsNiaZJunQofjTX24BaDbOAXkbNhW_G_sA0K1BJLpXJSLty0o0zJJGWek1V4DQ4u7yBmfR591zqzEp5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjW6BX6nr0TlP0n6_UYtFq-uHHnJ2a7yle4LQhYB_IZVCEW_sOZf_q_w9BRH0ClFthW6UnIuUqsXn88wfeFUJjLc4jD9iqELzGPmqgVAV_iNboN4Zk2JA-Zli5j2zXh0dgycvJOKf3UdISbfoSfq__IcGjaR6OzpY9rn1Agh3KgulFRpFm9V0rv_g9plTmjajbEZ1AZWvaHYDzLHestE9waOUJNE4h-nQA7G4PO6P8SvpBQ1fhGskMtUm4HIEq19LtvnLpPq3ZLJsjX_oqu0n293_tK1NJ09xFb-a9MMvCto4CBHZR9Ge5Ys_49YHELZUOhdfsG_gnO5TuNxIzEOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXU3n41AW1vCRTm3PVkrRJlj_dZvqD2uuGoByq9n_4FRq7hZt__Pi5kKEH1REx71tF0wk10oJ7sdC8UBSEqQZmlmdEciia1NkgtZ83EbrW5cx8NPCj5yDp76RnEVxppnBcXNZO-y4Fk1sB9Ea1Ebqbfl9aWRiqTC8kLaJK7-xeP1uFenMt7QxFw_VykYMqLa9rfLmsWMLVMOjoP6eFkhiAii8BW88FPK3odZzK9UkWP_k3KIOt4ZyjHA92pBXYGCXfl1oMAk_-Rx0FyLsSoAsb4c652r3oxWGcONYzgoTWj9nAuk6br7hDCDs8Sfd9OfYu0WYOWAHywM5GLWJW4N5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddkzCh1GNsr7XCSaKKTv75hFHzPU-KMI1BYkWlFzZuVXuItqQ2cyKRlX5UdvHkPPyczFoZPHR8kYxuuBiMAicNMlSZaOspTF9xxtEpwMupam90UHIufM2sC3rA1nQazh0tpshgws30wJJBsXsgNg6pZgZXJIzSD5x7hrO5MDsSwiMcR7Jzh2FBG63UY7k1tT18CkB_BWGjnRlTYC-KplNzmCyqE4iGDkmtlM8o5OaGK59F1WicJOyRMr-8r85ipMlpd8JPGwg8reQiX31iY_Ldmowg-XSKKo8BRuouNJmwKjkcAk1S1tp3tFB2-bvo-ph_KeEK8_f1UeknHJkqBF4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G61j43slNSr4NMhOwAgwCy0ykXyoiyyzax9aUo3ZSxyoQNi2qKRbHuilzejK7ibq3HnH1ksACL3sHjzh3OF1IzPzSxyawrk_cvnA_px8609tp8hog6FK7pI1j9LRypNAFyqeZvEmJ8KqkwrFmxZXBj0vXkJnSo-1wlYF_jbOK5x-_DlLsO1rCtRnMCuJf_9Aw4tjlcZOI19VqAlbTALZ4XAqbdryVkbtc9clWkE1Mn2uhbbzPV4UFl7kADyTKs9f8oWbpoHsY79opR120jv_nQPB63uUeZHVgDDq-nxhRYRbTooqrAV1HuPU5PRIagS9QKhjOlGOE1Akstu4N7iJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImVIWShnDCl6kti0_7QNQwljPT1FSoasqHvrp8ffcBK720LrIzITR6Sf40Y2ZZmUtZj_ZBcKy1uzLKdQqDjRQzj9NfN-WkaLyMyMQmcXnAd7TpAKEOQi21l8fvxslXgQ3_x0Lj8bAH3sG4L3gI_No3W2k7NPV5K5T8nuKq-slpBmv_sThq7BdGvvvIyQlc1cwNsbW8YtBS9mASnlzQQylxRnarAfulbri-vN8dlp6x8BkbA446fTuUsWKkLJ4EFET0iST9F5uEed8Tzp-Wuw7GUe11rxiGPbcCAp2qUS4858GpAcVQRcT2MoTSUW7BuBSU2yqQ0zaMX1k6BlOJDXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQC-Cmd61j-v1-tnqUARolYOPlGTAuANkiBorDfmxhybFBycJPMt6xD1YyA5VPFfb6emZSwZkNgP_cHcPExeVAJPZin9ftmMtuu4vxauPRSwgzM5UuA7a9K_xJiKNsT8CWXQhpFaURvZlM5uR9EF3lfsC4AHzMGYvLSgdZYP4nWeRglMTp6Ft0m13ZyKxAWRdShRx5j7AsIBuwzZimtTkiHEf0sILx413R5oHwYXRvdxghSDKElD7gYZW4yb-VxfSgAw2VpwW6W_hmFzzWyvEncMq60WcaxGLbnHzT4mTO6eXSzv7PngHnNixJlnm0Hx_JVzqqgAN_sIg0YyU5O8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v24WTYzvuGWeAIoGlUc7Dl9hraTijDIUc3QZU3vMB4_s2dQ53K9WTaC6bTJqK7JX_aw5I554OL2xsAWJBkJ1FvbhOLmCg0zHgyBkOZAbC2WK9G1eM8YnhamQrvPdUwu_teFCs5eFVQPx2M3dA1l0XNNC3KS8xq1I153o-UO3XAfBW50HqJKFzQ5I4bJThdA94HnpMzncFhNtOB1gnkOqbYXiWx36pO21Mxjh9QDe8Rqj8qcYPS9HB_Me3xnQfY4Oe2ERplDm-w0tN-_EicbGxqvP5tln9Hsb9zcWRfbZGboja2RH-RDHclEbDg4HA_SjLo_ta78KAnO-iJf8PZWzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzBkF_DQCImDuT70jSiyxwwbvNCDWyo8RbBce-jPFlnsxk3oQKdhjkv0Fu8estjMU-AtU-rLi4bbZciy2jYuEHwKRcIUSh8RUQ9IiBL0edPjSSTA_9JeUAOz1rjKX7DmazyFYrFd0v_KkVf2eCOjekRAKEu3SQ385DJT62oSfIBTzwWfgXpdUo_t61VyQ10XFrEFSfsXXYyT0blnI_fvUadwzss7-yF9Bxt7ozzWs0GfJVqJHGZt4KSpI00XWhBqA8Z20FT7dP3bmjYOIIPJ6l6vMifLHr5qiKnH3QmtjLiI_Q6kpJ7Ao_zWbjtgf7NaEFd371Ov09moU4Y7rcCQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyqfHcti_HXA3OX3XxPiUpFz21hzNImqKJbnu_wuy0BpR70DbrPHKXJaE-AFa7dCDUyo0Z6PK2luDvuoZkRTYI9TuKWiHIwQe5hLt9kCVvW3u2PKS8T_m7hJ1b7ER9On_QjHCmKll25UxuJM68A7jxAOJ1mVek8b8qEiOa4kPrV0XLqyJYDQbnoA3QXD36rmh9Z-YVIEAloQHeAghN6AEB1VongnE4MhNqHa0AtfKRX9V_gdAB_F65Ki0HM1dAwtwlUPZOA1tdmP9vHscB9dgdM3Y0VJu-nyK1f6foHjl5DmVdXjt44iw35W82ditVbQwVqhpRDfDBzP49SL35tBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8wgUylc05fSg01548jj0K7VidDWNQPZMKrDX0T7pihadBAAS3_RJP8HbP9M7AXAs_iSocJjopElc-F_EUO01GKz3sSc6qXEzobrQ9734huI-rdtioyB_jOr0nTzZVvVLp-Vns05SwI3Y42L939QcjUCiGUsmrp1CxLOk9alUf_uE_B7OxMj7tOBqc7XBQkpK_VvV9KOETcyrgZ4AMOqMGXFBnDKvkJ0icdpWdt3TZ7ayoNasfqLu0sfeEz6otVxMPrNZtcbtPibfwLC0nZtRbLuM9SFmKlBMq3fWg-euvjfsK9MKUAG4y-SIC90U9p766hrNuP4HKI655qFLnXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=lkwEb6-nG0Kf58jmM0gdNh0CikzLW7J2M7fOf7Rf2WqYSzqEQ1zSfFfdQ5QZH6ZAwZNafunaUGDd4_sTKFRNZdUU5ZKYGUwCnj-0iMeOLPt_e2hQi3pKXAlgRaLdbQFMZoNe8-hVT2HS8ADziMFt5c_EjxsIdQX79YqbOC5T-QOyETaWH0lF_2LY7ajZMTQk3xjfCg3BH9w7KIWYwo5RSKphFAu0X_W4COc1-eqO6bbZByJIJWnWW0X0WmcTByUQ2Gw7x3hT2GvrM_Bwmtx2eshoq6hGrtY8UShQ-wybJJa7ucaTaUNuBCd0g9daYCTRpftjmfLXiigGF0QXpAQhJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=lkwEb6-nG0Kf58jmM0gdNh0CikzLW7J2M7fOf7Rf2WqYSzqEQ1zSfFfdQ5QZH6ZAwZNafunaUGDd4_sTKFRNZdUU5ZKYGUwCnj-0iMeOLPt_e2hQi3pKXAlgRaLdbQFMZoNe8-hVT2HS8ADziMFt5c_EjxsIdQX79YqbOC5T-QOyETaWH0lF_2LY7ajZMTQk3xjfCg3BH9w7KIWYwo5RSKphFAu0X_W4COc1-eqO6bbZByJIJWnWW0X0WmcTByUQ2Gw7x3hT2GvrM_Bwmtx2eshoq6hGrtY8UShQ-wybJJa7ucaTaUNuBCd0g9daYCTRpftjmfLXiigGF0QXpAQhJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC-iHRtd0WtiXAwH-iT7WlzpMelGzAejXnmPYwcXF7s0lEG5LzjOX5m6Zo3aKDEuCYb8E6VSriJMHFMPFYAqgWTdTXCVW_XIHZmT35CUI2OgDFgtL1A5DbfEgKgpNIJWsHXLdB-pzbODhP7E8aA2WJ_X-eSxCPjT8aOBWMSHvhAIxZ9kXXexW49ZMhEqhI_R_dVS1e_tnkHcaxnxCgwW8LvVOfwB_qhMk27m9_xyt6fLJLJQ4uN1sqbnaMH8F0uAZJIulOQ42QM5NiV8DBpt6EdYjbIAhv2809AVPBwD5ONvvJOBPdxCen6TB0jDjzBZtmCGEm7v2oAdFiDjv-3-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKJoASLrjo8mWgK902U896zbhX_jbqqGK6CEejcvutufkG8WphB9a_HHNvQDF4ypfMRak4hFZotVavQgJMNp6u1hI5HTvpe_PTWGFodKthCyrVVwwU2PEz9cpJAaBtf-Juhube2MYqDBBFJDPBX0-4wUeENRRK58pgnnE7HoAoIYklpEJS4CTYGBNa2bcPT2852Q38AiviHOoj_NbahRX5QDsZcA6aG6cutohUt6fgf80aooe0OMIdZoFRm0dvyFSMSJnLRvIz_Pl6ZTm76u3XnOHuzZktPeeEHhstRLALXTjBdpAvfak1KifBGx7JdWRvPCTau1oTK-TfEa7USpGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxT4wQy89FEaYXXnxHXl6VuQ8MQ2L2nVA6Kz_TqZolyEiFUpaBoKGLXyZPDXnH3vi9UxACY-xoHGjvTaFV99XJaYnieFvFIVr6kCiTzdK4g2106czrgNyFfFZ8Sm15dlyH8gpSVFCZuF184Wb-e03VBIbPMmsw139828XikS6ThtqBvS0AWEppY20NlqBhFf_FEEz8Lr3igpsSa-9ODiL0Bi-WtHBEC6WaKWzFKWNxiWlf1f9ywKDoJwy4kNsPjO49Om4_IEKKsizcKteYmDekxIsapdyTDpktQCGDluyQ3DSaBCTRx9Jy1TbIRebyOp4AkZrSbkqdK9yUeRRmWsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLEOFDOELWKF8sDk6Z3og-o7wY3dE6JnNElXf5-QwJ8Z787-M2jd5dnkM6vLqJDSiyjpDZiHO9qgUGu7A-68pYQposT8x5tS5BYpo7jaJKeaa4h4zMU72TuJ9FERQBacr7XWhXptsfKHnlvsR-grD-XgN5OlPAlGp7KqUxYJG6C_UO2nn7eqgfF-i-Xyn3-MgMoRZS_55uWsO-ZpCzEbmr0XeZfVCTDyKBkISgvL2IA3dnS0V9Uo8fe5hhlUTxv7XQ8CnpFcdpBOIu-wd6cAiDhfD3Qhm7ACjY3pQ9DP0XDe6k8VspTCiFzKI_fDq9LFzw3qvex3PaR0FE4TDQn-6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=kQN16Fh53CI6_RkCj6Lvp09PM4QxXFThC-4V0uopOS93kKEMXPECLL4N_SKwKG8VmZvhtKQ-srbdcdw-a687MvOP__VAuj8utR2OrKxxvC8QvpMAHTNUtkerXG9ssOC4HE6Y9d8Hy8aS7blaxW65du0wIB2uD4cShslUmS0_iiusW-fhgFAiJN5STKJYN_uxCOK4lhPUaPyQlVGoqkoj5xp5XB53dl_ajF2BAtea4Kl24U3s0SWpSWqzxGonCDXoRRPk39M0ZzOAk6McBkM7Tu5Lfc2I03Hb2PEhjnWIDDmpT66zFgR7PRovnUwcMLcjp1444nCnrE2o4tcyqUmppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=kQN16Fh53CI6_RkCj6Lvp09PM4QxXFThC-4V0uopOS93kKEMXPECLL4N_SKwKG8VmZvhtKQ-srbdcdw-a687MvOP__VAuj8utR2OrKxxvC8QvpMAHTNUtkerXG9ssOC4HE6Y9d8Hy8aS7blaxW65du0wIB2uD4cShslUmS0_iiusW-fhgFAiJN5STKJYN_uxCOK4lhPUaPyQlVGoqkoj5xp5XB53dl_ajF2BAtea4Kl24U3s0SWpSWqzxGonCDXoRRPk39M0ZzOAk6McBkM7Tu5Lfc2I03Hb2PEhjnWIDDmpT66zFgR7PRovnUwcMLcjp1444nCnrE2o4tcyqUmppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ManwtXLGeBWetUL1fWZyeZNBQ5tYsz3qDXiSf0lMOKtjh42L_nP1EDGLbjV97uHwUO0avZohwRZ7cUs7cdFNll8ZQjojiVXCguCQphy9l3lWtNequmiUthTlWd__R8fsokXuSRnIajoFe1LFwoJgLz-lJmHXVsqlZmrCDNHYr2_qkmszycxz150Nt8354rlv2tf4ZQidSOjmT-0lIgQ3Fbo9hLrrZ3wN8C5LovathjR3N61SpgdTkPxFOJDSjuhdETeFqZLJxJGZGP9pqxecFcptaS0A-sA3cYU9J9oikbKE6CWpg_UA0-iAOLgasg8m_u9XJznDcvlgS9AX_vC8uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IutzyDFHY8ZxPpagbhbFZEIkVoPhXDzNAezbF_5XlNyJ7eeoxBCp30khNuOXTa4-E0XND7Ncgq18i902N4OZrj_jx6KJCGfkQcFi4ta3CPVJp_rof23u7jDlOuCkpfy4bU_1TNpc6M5rH_FPYslNKh5r1Y-pQHYe-DmpJ5JdKiMDqgLEVLe2ZuRHNVmz22LIu-d1jocrF2tqjq5QvyKPHpovdPESeYO4tT1OJAq27Jk-3YYIVq3YNmEEORyUbrnZQWLbLtsth8JQPIr4X0PRfZQGv0lE-2vLpPa2SFb4Vh_SNK2crFHPMnhVdk6Tbb67Ha2p688EKBi4_6MZZNR55g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw_2AXTR36c3CBHZv700fE26UrDtScpNiKpG-IMOR4Pt2ClrezF6Sd1j41c_9UIaRDnFnYlvJUaiZHUMUXMKSNPNU71Z9_ykdzn5nJt6Y0_wG5ZoX8WcKVUR91OWSG26pPRvySQuhMTQwPrssV83dFkqj7TlQRwSMoQUqKm1yREjVhFfscCNTBSAMa8lL8yfkUY9oYj0J-m_LMe38xMm3TLMNN9OvljvmaH80_5wv8vqsA3AIv3E_gECwY4xqiDctsarXaPDCE6A0nB9xQq8bzs1cLv6NFziotuqYdRhIoeoRHUB-YTgsGl0VEPGl6sSHhON3MOYyhNKS-y4mpHtag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=iJRINJloqfZsApf8RZ_uUQSSYEEhbMUYmNzKpo4ky7Vop7oVs6JkL6Ttc2NYs6nipYsKuCsUbCux8DdwJQpZYRhuAvVF0SeuOqn2qiTW-IlDTbOtqXvW6rACJin4b93vzO--hBRZkSchyJ9yeZ0RT0nzNCFNmK_KVTTwR-rGvDmaU3tXdMNhM2Zyv1YwVguC6bI1nI8KSmN6XdISC0KSTbGKgy_k7j61qgJRbXZpzf_Hs3d9yBATVH41LMcFt4lh7dpfdporReCxofWkwoT1Wp341uXImhJEZq2LRiHqlM55nuT5MLukbrcA0XTZ_jAwvhiowoO0fqPI2GuklYFPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=iJRINJloqfZsApf8RZ_uUQSSYEEhbMUYmNzKpo4ky7Vop7oVs6JkL6Ttc2NYs6nipYsKuCsUbCux8DdwJQpZYRhuAvVF0SeuOqn2qiTW-IlDTbOtqXvW6rACJin4b93vzO--hBRZkSchyJ9yeZ0RT0nzNCFNmK_KVTTwR-rGvDmaU3tXdMNhM2Zyv1YwVguC6bI1nI8KSmN6XdISC0KSTbGKgy_k7j61qgJRbXZpzf_Hs3d9yBATVH41LMcFt4lh7dpfdporReCxofWkwoT1Wp341uXImhJEZq2LRiHqlM55nuT5MLukbrcA0XTZ_jAwvhiowoO0fqPI2GuklYFPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkSRbcsnw-cQpwZYK6eZJgSGi_tQIOlqsFJd3lmZ-PKnKAwCEFMsPs77E1dKht46dA0xBKxj1xrzpZnwM6bAZko6rinmTbdE7ZTX7Ukl9LXxb2WkviImFnqX9RkAhByOXSVQyEwPFJV4ePqX1kAe5p63fct1O7RdpXEEpUCaOawdcgKFc_6JoHkd46E8Hx_Cr7hlNSe1DKDk9dsaBSAR-SjErLZb11bYLX2Y73DsnnpVxkV_YL17VMgbSBItf2RZ9A41nrayyYrBp6Q-j0nAtZ6H7F6T8YxMRulVQD2wjk8rG7OpB9hq_onBqdUjA4OTA2YxlRoaIb8DrtpZwDY7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C56Qmb2Z2j5iY26ezXrppJ4j9XIZqEIXnYV3i9ZwZIyxxBDpYhiVTBi-1xKO7bAW8fJi6ebwQfytCX6DFKbLlZX8plcjd8U3QQVrrWwny5QMm3zJlXMaVjKaR-SbT9cdIW5vX8CIZSDaW8NX6v7np33U_XowHSaeDRdzfp226v8RA8lSHfJ1afvi6ui2y8L5b7klJi9YQNGDl5T1SrjNDYgx0GfN3s4lyR0-WenrLJOTk-oko5WtCalPe373IJPW5PIlhfRdcwKQ-qx8f2s8i-NhRkI92nOrpj_pMNQzs4rFa8Ax2QFiXwamWzbTBx3ai56GOd0X-Xr8WCWPhplJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRhCsHl7YZBJ9QH4Rx4lp29h-R0Hi-ojB18eJu_-r_SRUssTE7g1G-ck3KUz1N9DTSv-xfervLc4YrNq09GycgX8GyZZQFKZV0gW7HuVh7g5FE9qnEQyje19PqpST9liyR8FxTtBPveqD4ssMPv-C9_xZN7gdHGlOWWocdbD5z6knMuDMWU4KAEZnPL2DZbR3tXjVpEXeJ6J8lEb2COWRf1OaWAJD0zwLFbAUliRM44aCrwx8_57jtkCDHRnLUnW5HyT52J4THlTzaFfin3rNq0_rIWu5JxtXr9nGPZ-PwUEyen3BmstTpwRRdJ22mrB2GVQJFI7WPlcjOAaspvi4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPJJsF7ZFdahjTUHuvRSzYebhPhVW1oLhm7kWV4xEffMMlNpB2oUDEJXmFwtW5i3S6nqUjFBMYNlnDlfJzSWW7tF9Wog4J55QZz8tct8xOG5XfLqiK_T4OnRAtbs5Q2chsCRaAnBUVdSNAsyhDvVlPB_4BjMIpEoZulBxHvsUfpj6VIcxhGxJ8K4IjT48uqzR9lAo_Duvt9zPKWNnJuix9oTwnkxOFkVE-pMyICf5BZPHD6t_CPuqufa6-ztQmeFxbmDwzIMYU3uaJf9fSzmVZWj0sr9TqEIg9aZFnjrpLp2rt9URTWhGeDdKFQQe85mLqMJr0remECgRN0UQsQfOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFnFgtx5nFXIjhZvQnFqWx_tBIFaJVGuijNmXgPn7VrlzcO15HNhrIwLkyyILpSVicIaYKMdvU36AYAjL1hOW9h9ckZGbrJwEKvsymeeBc9ous8hnwtJ4vc7LEHoRVt4yOjn2CyMCWVlYA9iAFiYjUnsvFWSZJMs581sgUbddEjw9VImbpacPNMLwS2rECv6MR90OWG9rDoDegGehqPADWLqoF-coYCDawqFcAfjblooVhoVwQEzmCDcQK4gZt7Wkov9VhTKqSy7LYYPx8t11MYj0P5XUHu--aH1tA9O-ng0H3nOM3KBcZ4SP9X5wMQjEH7jaIeV7XMlniLhsObAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awa7u3B9UAYaMN7sY71WE0EJqub1X3vgCJsxxkshqF296Z9iBAdzf-8MeI6DqwHjEDT6oTTKi8uGOZHTEAxcoK8jF_4xAmFY436OWqrVoiHdHloFDhEU5h2q5Wm-CkGxrJ1a_P_yx9I6Rx7dbECUZ1Z1m_1kYhCoeGyrSfmz5eS4VS9t0Yyk_EvbelijVNEc4wCXGgwvcFGKETUillDafo7Nt9ES2xypbY5tJHe3V3S2khbFDMIk_9qWyZw3NAXBcLj-2huBMGTLWdrSIoP9QOoauiGYtq6n8-G4mtf4_9St-YKHKXXE9GlzpA2D7vDEjeyvPkzkEjayYFN1kcCYXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Jj9FhwnygeUqskOjCdof-0Of7ulA_NJDmstNwlYhpMwTPjiw2nho5RkrGMd09b57g3aCMURM51UaBOxm8pCWr4CrJIrgo8bKS_m5aI9UX0cEz6AI-Km5hcABUL1zrQiQIqMf10c41NDXetPRMAiT6PVGWMpQg63E8L3FwN08QNdYotZxMuOSsLRFf78kxvR_Ce3X-D9lA1yL9EWpgZlJsRTGl7XGsfsy_VcZHBHzkHE60CWMSVFS6VieHmWOzhiEQqXZfnkWGdoja5piHwKp0uuiY8u3pVq5LQ_XO-cH2p3MARGx4sAYRkj8L0ZbOcLw_CsE8FxPZcu4EbfKR6jrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=Jj9FhwnygeUqskOjCdof-0Of7ulA_NJDmstNwlYhpMwTPjiw2nho5RkrGMd09b57g3aCMURM51UaBOxm8pCWr4CrJIrgo8bKS_m5aI9UX0cEz6AI-Km5hcABUL1zrQiQIqMf10c41NDXetPRMAiT6PVGWMpQg63E8L3FwN08QNdYotZxMuOSsLRFf78kxvR_Ce3X-D9lA1yL9EWpgZlJsRTGl7XGsfsy_VcZHBHzkHE60CWMSVFS6VieHmWOzhiEQqXZfnkWGdoja5piHwKp0uuiY8u3pVq5LQ_XO-cH2p3MARGx4sAYRkj8L0ZbOcLw_CsE8FxPZcu4EbfKR6jrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srgKP6w3wAK2nmwEAnHqDRVFwzkTOdOdlCxezTr5YwqBaecH4PxsxqMu0s7Sv1imhdkPZeFRWac0z_M9YPAmCLAFZACcu4Z9gYmTT1bW56L8kKOEhBJ22IAsJUzijbndVC7VZ-1PQCa7wUd2-LrAUbFmNvXA7cfM7RkbBSXTVwfsbwrW2a3vJwPaMeuZODHCkPjxwZkaerw69VfhBqVcaf_DEPPBSKaSAFtNpNzLzCES2e8HVhVCVEZu5zb_hQqCJNzm3NZTnjxb3WybxMZlgikTCQMrd57_7EOroQ3KdBJpjpCAPl33MjICseZkbR1QMDQsYFPsfCxS6N7EJH4HVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8PmKbF_fVdMf-XssoJnm7q2ZL7eUDwk4YbovboC_M1oRp8W2iSv4Q3o-b9_A65lZDc-zrxWspjiKJ6X0yWpn8mU1m-my5fO7ccwoFYtgdjzpZieBkLcn9Q2sNB4oVUVvAdg9XoFXOtUd6biZqDxft9tEt-GuKIz03GIVMDs9mhhg377Yuz-qjXCOwouEBlW4YZ47hlwkKHJeq-af8plgOyd05OieQXtsB9qKiscr5WPan2kHB7UdRyswd80lliSIZavgC0FhZ3PeBwIp6G1Ja0gsto-Scfyi3UMlc_bczQgR1mk8VdYv-1ZB2DvbbL7HNqWnr2eV2h9lAqS8UCfFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxB6x_MxoA3QDrA9fwjG9bUSGJt0eE_25byLZtP6oNei_2gWS_UzrRsanon3GC0KNT7IU5bee4VMkqRoCbvxLX2Smr_eeL3yfDcQdESxix6J5wk3LWbUebs6gs8Kh8w_X5c1pZV5zC7p1TucUcsteMDUVEI3soUTRJnRjngzz8qIDMEAfHv12pKj9KXM1fR6UsLO9QmAlnbiUTKWhG-bHj1FxY6Xf1sRg6h6WK6e_JoZb7t27J1KagKbi0tFvMSZECB28eV43e3R0Z5_VlDuNkEplMdC5YoE_b1OyJn6hOImnhMVTxZeEMbLAAEnII5ImhliJzcCUjxnCxcayoYu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRTVJZDt8J057of2HSz6ymwOWGJweSfZLprhiDweJ8OamV4wJ7lgu22HRu-rcvlvOPrVuGUV9ON4s9uJ_RpCcQ4g49xx5lojxKasuitga6fb-5PMXVHMe3IRvWHO5R4O4ieRsroRswwxH2TluLFN08Hl8ZUUBgMNoL54q0EsIOffzzfREaMLy18JL6HKLVPiKyAFn8INsBjZKO6J9LEhQHo9leujpBeTtVCz3J3nKpctDMTFmicoNRtBJp36pqmldtV6HejHkqeZr-pJqkDKuSJeD6srHfBstCG9OsNwAFPar-hFTtChBWyl_g0ncwFOSdN4DTxRfRKdVfQF1W_IFA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
