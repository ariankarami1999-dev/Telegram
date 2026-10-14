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
<img src="https://cdn1.telesco.pe/file/DAecZ6-pxT0-WQ7bE4802oYMFauBXTuXPPCt1YMcrLkhNmhfZA7fwfiAnDO2zmfnr6XEg6uQumew6uQwy1xT4CqpuwuOeI8eQSe8mOcLFoQP1Goc7ZJao_V4gJK_s6Ax-QokQ9QnXeu21Nxf2WKLLLavzAjGIhxB86jp7iGyOTdcApkr5-IKOeN1TyVY5N3PqyXwaGJraFs0R2weDszaNodPbZ7ryPBuzMuQ7gjs73a756X_9zbuKQz3qTSX-_E1tmxWw3_qHAHbhXjk58p4LfdwECv-nKYcVdEsFDN8Zv94kXKy1Nc96HywPPsYLuypw6k2SSbYAr-cORoj0X3qIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">برای ایران هم گویا نامحدوده حجمش و رایگان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5579" target="_blank">📅 13:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P09JIJPfX4yyLy3uh5YpwpWnYRPPM7zxvum91M881f81GcAecyex8Q14A9eMwP_CoGlSiE0Tw9-sGhVjupRW4GDubynEhwjPxAbjuMMw3uLJ6Y7U2cLxi90OCOIhSZ7FXPX6vmme4o9GJyha5HtAyesMjtw3rbJxKbmwk9OtV6p3NvFQnXa96AuM83qB225hoLNGwwqmuAQbJXc8CEa9VLcBvHODX8FaE7qjfgk1V5qKMGPRi6p-wetffASKLjG0ONKVQL_r4YshfcmKcZ9_xqNfL_5JWkhCij1dsdv4IWI9avm9PU-rmOsY5FIU6EsRdHv3W59XFMs_zZZrt1xKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FK2KPj_yZ4AVQjl8UPntpDjJWUCcpeJBvVcJjvhTgZnJl1Lnkrxy8U-rP9Kl3xzD81Fs8JdkKQVwsQQ9WGDBmWNZnbz8FaVSxpwdmLyKfboszm_FVYamA3L9L5CO_E-jKIrud5lqwRJ_vWYuSvTwRVmgVSW3HNBzat23MCpSvPHigW-YCFRVPgBdXqDdidBdtAzou-8LdwlIIskM8TZFgkH2DEKE9UGvJuEKp0HVIyPLAR6NNRbiC7GwgM-4VwrbontueBCO2EvW8MlNtjh7SWzp9ug3qq2MynIqHfV28uNLsn7bu4w7FxLbATTbz697Cf84Yic5n8C3lWMrXoDcbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب ورژن آخر فیلترشکن Lantern(نسخه Pre-Release بتا از گیتهاب) رو نصب کردم و با همراه اول و ایرانسل و شاتل کاملا اوکی بوده. بار اول پنج ثانیه، دفعات بعدی فقط یه ثانیه طول میکشه که وصل بشه و توی شرایط الانِ اینترنت، عملکردش رو عالی کردن. یه تست بکنید ببینید برای شما چطوره:
https://github.com/getlantern/lantern</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5577" target="_blank">📅 13:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Qa_b8ALAAAuBV5F49tmxw2S-L-cWBumbf0fUOraCB3C45cLqiyg__z6nuUWt9CMZgO8Y54ZW_bujWjfuKN-yhDiKoek88AwLpiQUnnJ076VdWwtKk5HKBLnaLaFXYG-o8ISXJ0yhfqRcqh3MKWXsAmqBgCXbEIGEYS8Mi3WpTEWXqgPaUUxjuDAwQM-VeI2ZmeLrMJlktSrDWGx3FZICYYAWwtS64HY-FFtH2O6ZzlXBvFqVfAaa-JrAuAtRwAedZzJ_Du2KVPBInp3PQPg_kaeX3hz1bA77_3zNs4qYFSJXHznRS6hO16wD4lZ5Fk47SyJ2pEOu4S7K_Jyn6Jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
آموزش ساخت یک تیم از ربات های هوش مصنوعی  Hermes Bots
✨
با فیچر جدید Hermes به اسم Bot، شما میتونید ربات های هوش مصنوعی با اخلاق و رفتار های مشخص بسازید. بعد از اون‌میتونید اونها رو توی یک تیم قرار بدید تا باهم شروع به همکاری باهم بکنن.
👀
درست همونطوری که یک شرکت و یا تیم واقعی کار میکنه.
توی این ویدیو یک تیم کوچیک تولید محتوی درست میکنیم و نحوه استفاده و نصب Bot هارو یک نگاهی میندازیم.
⏯️
تماشا در یوتیوب
پدی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5576" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی و فکر میکنم با ویدئوی بعدی یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5575" target="_blank">📅 20:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا Mpay رفته زیر maintenance. حسابای منم قطعه فعلا که گفتن اوکی میشه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5574" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tAXHTkhI5v0TjgmKgdWD5HJYE7_G7yGJpWc0BEOSSal2nkF32oWzu1y6k8snHPgp5IT8anwHEsV3yTGku2kPyyVYVzg2QF4iOoSHnrtBN_2FVgtFND0qvpJypZxnE-0TsvXZWeJr3qNgLsPeoMUVFSBZLk9OU0CcIcgF_X1wc7CGkAxLbFlsrWBahg18ElmlQRE6RgzUKTnHTkPgaJlyBxX0F5ttJxUjc3WSWCwzKOt2NgVAO3ORjP-H37FhF0iIf0-lQ6bgLdECMQpt0VKz5JH3iIXC-mJmO2iJc3dSLkbmx3tp-dzf6jPgJ9s_p9pkewsT82ukvz41WD28wO-G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Wonder بی سر و صدا معرفی شد:
• $4 input
• $20 output
• $0.20 cached
قوی‌تر از Fable 5.1 و GPT 6 Astra، و هم قیمت Opus 5.5 اما اندکی ضعیف‌تر
(نیومدن Sonnet 5.5 توی بنچمارکشون یعنی احساس خطر کردن
😂
)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5573" target="_blank">📅 11:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flUdsrIq95vQL4JS3utrSb_f6druVMymXtE9gvl9xuT90dTkouvgstgE79MJ7iKHzTL3Y5Y_pIcSqOTgl4C80Bn-5WkJeEcBjCU84BCAYTAyG34krp7WRto1ijFwzlk5j4iivcDX67-89QzfsJ0AsvsjjxKKpHs88dFXOee93miJM3ivuSgvxmhnpR2_6HH0JV1ZZf25gX7NI0_ZwU59TfgvLjnhmHg9ABVz4yoMsJbC8jx7T1YCivx0PTXs9xNmEmswBPjH_d4hP2E1ZnWgKiq0HxSNZSAUqDeIE7_-7Z6uc3uqFFuWHWFcAATbhg5xQxazpaabzh_jcX97aGFNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنپ؛ مدل تصمیم‌گیر که ۱۰۰هزار توکن رو زیر یه ثانیه می‌بلعه!
استارتاپ Subquadratic مدل SubQ Snap رو منتشر کرد: کانتکست ۳۸۴هزار توکنی مولتی‌مودال (۱۲ برابر رقیبش Jev)، پردازش ۱۰۰هزار توکن و برگردوندن تصمیم زیر یک ثانیه، با قیمت ۵ سنت به ازای هر میلیون توکن ورودی و خروجی رایگان.
توی بنچمارک Decision Index امتیاز ۶۱٫۷ گرفته مقابل ۵۷٫۹ جِو که طبیعیه. ۱۰هزار کاربر اول ۱۰۰ میلیون توکن رایگان می‌گیرن:
subq.ai
در واقع پنج دلار میده. مثل اوایل jev
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5572" target="_blank">📅 08:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی  اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی): هرمس ایجنت رو در نظر بگیرید. اما: سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5571" target="_blank">📅 07:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKwTxux6-u9_0Bf48TxQG4y_ClvT8aetAZhkGmqkC2In4Z4dZNAyxtQ8h22VpEDDKBu7OwziKLQnXo-KMgwe6aFM0rOgy3_3m9tKkEvu5MCbR4wpIS7p3YZ8806tSvWmhSG8iT1Fu1LK3RKiG1G7S7P8lO3h_LvQ2trZ-4dONIbf2YnM_nyW5FaYZEyWCgkmOcewrcL5jbulVWwxEjd5n5L3aVpjLT4jJji4qhC3AGBlJLgipVkxtujgQGLaBegE6-9M12lB8J308ubVcY2Vd8dlZIHtFhGarez7mPJwOHfPsQgIa0uNGTwwp_W5-sGdt-LbZOArKbeW3tc7ba2k3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش راه‌اندازی Muse؛ ایجنتی برای روزمرگی
اول بهتون بگم که Muse چیه از دیدگاه خودم(یه آدم با استفاده معمولی):
هرمس ایجنت رو در نظر بگیرید. اما:
سریعتر، راحتتر، بدون ارور، بدون ارور، بدون ارور، و بدون نیاز به ست کردن  API Key، یه سرور رایگان که این ایجنت داره روش اجرا میشه؛ با راحتیِ وصل کردن هر پلتفرمی بهش که فکرشو بکنید.
صرفا... با سطح کنترل کمتر توی مسائلی مثل محیط اجرا یا خود API. که شاید نیاز معدود افرادی باشه توی این کانال
حدودا یک هفته‌ست که دارم با این ایجنت کار می‌کنم و واقعا عالیه!
مدل پشتش Muse Spark 1.3 هست.
ایمیل‌هام رو جواب میده، واسه‌ام برنامه‌ریزی می‌کنه، چیزایی که می‌خوام رو توی Google Sheets ام وارد میکنه، جزوه‌های دانشگاه و Rustام رو خلاصه برداری میکنه و قسط‌هام رو یادآوری می‌کنه(
😂
).
یهویی مثل هرمس "سکوت" نمیکنه که وقتی بهش گفتم خب چی شد و چرا یادآوری نکردی بهم، بگه "اوه شرمنده داداش! اون لحظه api key یا سرورم قطع بود(دفعات زیادی این اتفاق افتاده توی چیزای مختلف اما هنوز، هرمس عالیه. برای کارهای مختلف. خوب بودن Muse دلیل نمیشه هرمس بد باشه)"
شما نمی‌تونید روی Muse، پنل VPN و DNS و... نصب کنید. لااقل من که نتونستم و اصلا آیپی عمومی نداره و فقط دسترسی HTTPS میده. 9Router و... هم نتونستم طبیعتا. هرچند به نظر یه کم Tricky میاد و باید باهاش کار کرد هنوز شاید قانع شد
😂
در مورد 8 گیگ رم و 2 هسته CPU هم بگم که این منابع اشتراکیه و متا هم سر گنج قارون ننشسته.
سرعتش هم یه وقتایی میاد پایین اما خوبیش اینه که شما با هیچ اروری سر و کله نمی‌زنید! و یه دوری بزنید و برگردید همه چیز اوکی شده.
و میتونه براتون تصویر و ویدئو هم درست کنه(ویدئوی فریم به فریم کوتاه و..)
که متن فارسی هم داخلش خوب میفته.
آموزش راه‌اندازی:
*نکته: اگر که هر چیزی شنیدید(ریجن ایمیل و تایم ساختن اکانت و آیپی تمیز و...) اشتباهه. میوز فقط و فقط به آیپی حساسه. و تنها آیپی‌ای که باهاش تونستم وارد شم، آیپی آمریکای گوگل بود(که صد درصد یعنی با آمازون هم میشه)
1- با این روش یه VM آمازون بسازید با لوکیشن آمریکا(200 دلار کردیت رایگان):
https://t.me/MatinSenPaii/5130
یا با این روش یه VM گوگل بسازید با لوکیشن آمریکا(300 دلار کردیت رایگان اما 10 دلار اولیه باید بدید):
https://t.me/MatinSenPaii/5149
که گوگل خوبیش اینه که سرور Always free میده و منم از همون استفاده میکنم. یعنی مهلت اعتبارش هم تموم بشه، اوکیه.
2- پنل سنایی یا پاسارگارد و هر پنل دیگه‌ای رو روش نصب کنید(توی آمازون نیازه پورت‌ها رو Allow کنید از توی پنل مدیریت سرور روی سایت(به Grok بگید راهنمایی میکنه))
3- یه کانفیگ Vless معمولی Raw بسازید(مهم نیست که مستقیم کار نکنه. گوگل که اصلا امکان نداره مستقیم کار کنه)
4- اپلیکیشن PattN و PattNG رو نصب کنید(یا هر کلاینت V2ray که از قابلیت Chain proxy پشتیبانی کنه)
5- یه کانفیگ که واستون کار می‌کنه رو اد کنید، کانفیگی که از سرورهای گوگل یا آمازون ساختید رو هم اد کنید، و بعدش این دوتا رو با همدیگه Proxy Chain کنید. و VPN رو متصل کنید و پینگ بگیرید.
6- بعدش وارد اپلیکیشن Muse روی گوشی موبایلتون بشید و با یه ایمیل که تا به حال روی سرویس‌های متا ثبتش نکردید، وارد بشید و ثبت نام کنید. به همین راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5570" target="_blank">📅 18:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e5nnDVvu-ajQjd8a_zkkcZV8iHK56qEmBresS7Z2HRz3-J2msjOk6G74YmCUN3rarohw4aHJZ0zs3NtSCajDvyo2C7SnMLbDEMYrGyYA_93MfhmrPRoXyrdNb5Obnqa1q67pffDj-BHa54GugGpNtp0pOISIdeP8Jqv-hHiujqlk6dE89C45Iy360rN_iMMCb9GYKfDABYOrlbMKTSJ85ttLvjvQ7nn9IAWua_JEABsJdgJuJZ1m5v36PVwEy-AhRAM64brGfyOtaOsBKEDeDUMjGv3x8I3Tlq2f3i8MuxbkfZEoUtRJjHfW1a-k4Sd-OxAUAhOsCVH-r3ITPgoOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول نوشتن آموزش ورود به Muse هستم
فوق‌العادست این ایجنت. عملا برای کارهای روزمره، کمتر از هرمس استفاده می‌کنم به جز کرون‌جاب هایی که از قبل داشتم چون Muse همه چیز رو Unified و سرراست داره، و توکنی که میده توی چت برای مدل هم خیلی خیلی زیاده و کامل تمام تصمیمات و کارهام رو یادشه. به زودی از مزایاش بیشتر میگم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5569" target="_blank">📅 15:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeFXZWPMC60-32CM3FNCngp2tSxp3uXdnzRKHcgs5s9e2zoAAmG-42mcwnwN7yRVvqGBQa6r3oKScw1pKUPqSgD8Ur4zbNhWx7qlZIuDIFEljaX59uZ18UnLD6IpUVXwrXW_qAsdG3koVMFibVYcqNcBb7viCvr-vTrqxlSyN0BeWtvWnbh_AXlofDDh_1bt3g5w94gvJbs657bCZXhbrK7AjtuHx6TsBpmjzDLKurOvyyJWaIZ1qeHC_d8WTPkvwW6SoB4V2zJmktYnRWxqdCf6BwZqhS8kcR5Gp1TQgR1WfW9dGFeMH54P5o8Q27dSHjp0O-ccfDY7w5ljte37fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوری؛ جایگزین اوپن‌سورس Canva
پروژه Doory
https://doory.art/
به تازگی روی گیت‌هاب منتشر شده و خودش رو جایگزین اوپن‌سورس Canva معرفی می‌کنه؛ یه ادیتور طراحی تحت وب که می‌تونید خودتون ران کنید و یا توسعه‌ش بدید
🔗
لینک ریپو
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5568" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPWQpduSmxs23RXuhgS7T5RqKckfasJDMsM8SSeHNlLsoveJ3z9HXolJHx-FcjPS2RzITDNJgmrR-yHK7ETlVqKZ9PtlGE2xiTFFvssKzckufe75YmxVj5xHxRz844Xo2U67sX8OyHP3VfMfa2ekSmMt1oUP_wTKXykynRwXmei8ZB_oqKTGRviGjVR2isUFftSfd96noPlTm3wRdkJIArK1qNQAS6tfgHSsKctHsxY0N1F0-hMgqLiszsDznzZpBnKbknWA2JWDvFWfc2XiRsBqASTsxtU2CpR05gG4RGx-RsQSsavWri4n9vcBLclNj-_gkHqOCHwIvBoj_xgg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل زبانی‌ای که خودش کانتکستش رو مدیریت می‌کنه
محقق‌های متا، MIT و دانشگاه واشنگتن روشی به اسم CLM معرفی کردن؛ به‌جای خلاصه‌سازی و فشرده‌سازی دستی، خود مدل تصمیم می‌گیره کانتکستش رو چطور ویرایش، نگه داره یا دور بریزه. می‌گن هم عملکرد بهتر شده هم هزینه محاسباتی کمتر
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5567" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5566" target="_blank">📅 10:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این ویدئو هم ادعا شده که با کد خالص نوشته شده. توسط
مدل نامعلوم Claude</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5565" target="_blank">📅 10:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5064aac929.mp4?token=dJoJv3d4CatTXvX9YntRBr2dF_ED_V5nrBEI74z52p8qAprZIzqPA2oDmwKMaw11EWkAnpiOi6dUGszbvTklCEItNeb79KSNUMNkP4rFCjkY3G8rpJpcK85hPjvMuAMZzl71i_WAgKUDzMi4Cb97Cfu1xjnU0P1wrg0fD3wX2Ep0sHjhjhZIDsHUQsTAoOVJUlVx3cSjcZHjrFRNfNYnECX7uXOx0QqA8Rq1r7j4AXqce4wUdVAVf7d8zRoMh40x--mR9UmV-W77zhNwFal5QH3vTYXK2HBxwzva10T9PcnPDKUljEFomOT23YwOV0sPrTe6EuQGVa1H1JqNQYijlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5064aac929.mp4?token=dJoJv3d4CatTXvX9YntRBr2dF_ED_V5nrBEI74z52p8qAprZIzqPA2oDmwKMaw11EWkAnpiOi6dUGszbvTklCEItNeb79KSNUMNkP4rFCjkY3G8rpJpcK85hPjvMuAMZzl71i_WAgKUDzMi4Cb97Cfu1xjnU0P1wrg0fD3wX2Ep0sHjhjhZIDsHUQsTAoOVJUlVx3cSjcZHjrFRNfNYnECX7uXOx0QqA8Rq1r7j4AXqce4wUdVAVf7d8zRoMh40x--mR9UmV-W77zhNwFal5QH3vTYXK2HBxwzva10T9PcnPDKUljEFomOT23YwOV0sPrTe6EuQGVa1H1JqNQYijlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل جدید Claude قراره خفن باشه(اگر لیک‌ها و شایعات درست باشن).
مخصوصا توی ساخت ویدئو با js خالص.
اکانت توییتر chetaslua شایعه کرده که روی Claude code به مدل جدید Claude Next که فعلا در دست تست هست، دسترسی پیدا کرده و هی داره باهاش چیزمیز میسازه(مدل Image/Video generation نیست)
و میگن احتمال زیاد، Fable 5.5 باشه
(R.I.P Gemini 4 Argon. we all forgot about you brother. hope google come back with Gemini 5 Xenon next time
😂
)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5564" target="_blank">📅 07:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2wMRybXmQ8OdSIU4SLoWiaaqEdjABVTdMeRta3rm5QQxLat6zwMB0Vr0bI6CQuOvpRZWU10M7GDsCYn-6CsAd7NqPtvDzGv2JaZ02vsKGr2nq_0RLStQxMzpCED653rfrcWPbDxS_1cKvPII3q1RoPOsguN8BZuaY3l3_3nUZRCBIGXR1NTliWpyTVTRLQWzwXUaB4VCDMoKXkeEX8baWoghaTyCOCRtJiF_-PDQ6ijQ1ic662XbDSmmpYpMDCSJ7xrP8c7cknsBU_fo07W3tn0igMNVGCNuZof_8wcpA9tnViranbc3Y0ZpmQuUN9MpcUhSxoI_FfpWXk4SWH4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله ClickFix با طعم Claude؛ تبلیغات گوگل آلوده شد
هکرها دارن از ریدایرکت‌های واقعی نتایج جست‌وجوی بینگ به‌عنوان لینک کلیک توی تبلیغات گوگل سوءاستفاده می‌کنن تا کاربرها رو به نصب‌کننده‌های جعلی Claude بکشونن که حمله ClickFix تحویل می‌ده. ترفندش اینه که لینک تبلیغ ظاهرا معتبره ولی به صفحه مخرب می‌رسه و با انجام دادن پروسه‌هاش، دستگاهتون آلوده می‌شه. کلاد رو فقط از سایت رسمیش دانلود کنید.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5563" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدل‌های زبانی بایتی؛ بدون نیاز به توکنایزر
یه مقاله‌ی تازه ادعا می‌کنه ترنسفورمرهای معمولی می‌تونن مستقیم روی بایت خام کار کنن و با بزرگ‌تر شدن پارامترها حتی از مدل‌های ساب‌وُردی بهتر بشن. باور رایج این بود که دنباله‌های بایتی چون ۴ برابر طولانی‌ترن(در مقابل بیت)، ناکارآمدن؛ نویسنده‌ها‌ی مقاله می‌گن این طول اضافه با مقیاس جبران می‌شه و انتزاع‌های زبانی خودشون درون مدل شکل می‌گیرن(که به نظرم اینجا باتل‌نک قضیه‌ست و باید به شدت بره زیر تست). به نظرم مقاله‌ی جالبیه. وقت کردید بخونیدش
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5562" target="_blank">📅 21:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTzkcYlU7zu8yVYsJK5k_J6LuEQaF1zzm6AcdM7ILRANoZatwg8uUTEWBuUCBLbwewMN4eGZDlvMI9sttwEPCa4S4919MpaOEfHVEnK-Mvkh9oYrcKCYUchrwJ9xS9prvBdM7uGECtHU-z2vFuWfSiqlw_vA6LwXErkzSgrXLbyRAHrmPa4kv0o35U6RmUh5NJr4q36aEhyzwjFaXOQwLvXstYaUXGOAVtQV0lcfFyGhHHZ32X81xHmVZp1Z-nx3aYN91v2x9KSInaJrwyGr48gqJdT72_S8GFxKfXJziLGUv_fvZaMis1CD7H0b4KtQjgMd2dhAwvQlX7MoKs3ysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل اوپن‌ویت پرپلکسی از Jev جلو زد
یه ارزیابی مستقل روی ۶۶۹ کیس پزشکی می‌گه مدل pplx-decider-v1.1-27b پرپلکسی تعداد ۶۴۳ جواب درست گرفته در برابر ۶۲۸ تای Jev، با ۴۲٪ هزینه کمتر برای هر تصمیم(که فوق‌العادست. موندم مدل مایکروسافت چند میگیره
😂
). قیمتش ۰.۰۲ دلار به‌ازای هر میلیون توکن ورودیه، و خروجی رایگانه، کانتکست ۲۵۰ هزارتایی داره و روی OpenRouter در دسترسه همین الان. صدر جدول Decision Index هاگینگ فیس هم مال خودش شده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5561" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekmJmLBMzVC_YHANJQGurLQQRRKYNZCpMGXXBi5jQQkDKhDRhfNCT3OtdKY_5nR5cZ7dBH4p2JqYgZCIrWh2np55T2YzTgedMA0ErUcu9ZSQFeAEYGVV7BqJYtRXhYbSBZIx-cFENxIR8UST44HuF5cYD4jIvF0AoBbLHNM9J-K0f2oGA7OWomC9FnLtpmrIcSBDV_YE7GaLVjxcIPwk--7NIpNCqumC9gpJsiOwVzd56IVVwp3tSs6yEBMvh2hDD_8q7RsMQKq1bGkxTOr8So9bLobx5OB8QWptv40vYfgCKEFRLlqbDC9T3k2GyUeeS7rft7-RUPu8EKL8vZQnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت Decision-1؛ مدلی که فقط تصمیم می‌گیره(نسخه تنظیم بازار Jev)
مایکروسافت یه مدل تصمیم‌گیری (decision-scoring) معرفی کرده برای کارهایی مثل روتینگ، دسته‌بندی، اولویت‌بندی و کنترل ورک‌فلو؛ یعنی به‌جای تولید متن، مستقیم خروجی ساخت‌یافته می‌ده که نرم‌افزار بتونه باهاش کار کنه. ادعاشون: بالاترین دقت بین ۳۶ بنچمارک با نزدیک ۱۵۰ هزار سؤال، و سرعت ۴.۵ برابر نزدیک‌ترین رقیب و ۳۵ برابر GPT-6 Sol(چرا باید با Sol مقایسه‌اش کنن؟
👍
). توی Foundry اومده و به‌زودی روی OpenRouter هم میاد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5560" target="_blank">📅 20:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کارزاری ایرانی با ChatGPT مقاله‌ای جعلی در رسانه‌های واقعی آمریکا به جا گذاشت
گزارش واشنگتن‌پست می‌گه یه کارزار منتسب به ایران با کمک ChatGPT مقاله‌های تولیدشده با AI رو تو رسانه‌های واقعی آمریکا جا کرده. و این نشون میده عملیات نفوذ رسانه‌ای با AI چقدر ارزون و تر تمیز شده.
اینجا هم به دلایل مشخص نمی‌تونم بازش کنم جزئیات قضیه رو
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5559" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb_Cu0_e0V91OSrInep6DePwSTI2No1YHEhrSbu0dgyS9UT1rwG-P_mPUFvzNSJ4_ouH8lJ7Lf-B4OQh3tjDEQSpxwSTefzpC2AZICc_B-FS1EhMRfNkHxtrN_-gF8ufb2y-vMW8xTxYxRKF2I0qGl2mrz-qfIUcHmstGWio4TW537ILo4X7zhKlUi2bgY3rCsDh2dvQRL_32gM0dYUCMjUyVbtKJAZ5L92mhRgrprvo3qJC_M6J6t8wgKeJhLwxd5phyWhA_EcbqEnbH6Cr-lZDy8X-Hri_lZVUrGJbU2gdbnTOa00MFvipLFMRv_4wgIUiY79uS9ZVqvCPoOqC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌ای که یه زمانی فورک Redis بود و الان انگار وارد رقابت جد شده: ValKey
پروژه‌ی Valkey که دو سال پیش به‌عنوان فورک Redis شروع شد حالا ۱۲ تا Maintainer اصلی و ۹ عضو کمیته از شرکت‌های مختلف داره؛ تروپوت بهتر، کلاستر قوی‌تر و برنامه برای رپلیکیشن Synchronous و ذخیره‌سازی چندسطحی. تمرکز روی امنیت و اتومیشن هم جدیه و داره از کاربرد «صرفا کش» ردیسی، فاصله می‌گیره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5558" target="_blank">📅 18:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOO6s1NaVPC2NmcgUJEGX57FezmGEWSUGQdKLUv87HJmLHuZYdB4V2bKf4XZWzeRzzB4pnfL9vfCSPYFl1-5mP1pQucGHkQKNPtRpb_IIhCxjI0_h4GVJ9gMnSDe56lMS6qvZfP5sMrZ0tcMlhPtwN2xsU725KEObpvsvmcVuC-_ne8qD--VSvz-Kb-F9lonpfMBm8Ysohd_n99xbTba-iixZVugG9bbioGsvO9YuTMleFa_OIyd8d7JJumP9_Ma_Z26GEcotVUteOtq677cJjDcAyZl-ytgW9NlO0uiHV2kiLTysgltSHa2t-V721PGSsy7szuiodlV4nFz_ERg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من و ایده‌های استارتاپی خفنم که قرار بود باهاشون پول در بیارم توی ایران:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5557" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تیکه گمشده‌ی ارور هندلینگ توی Rust
یه رایت‌آپ خوب که می‌گه درد Rust انتخاب بین تایپ دقیق پر از بایلرپولیت مبهمه؛ راه‌حلش کتابخونه eros با «مجموعه خطا» هست: به‌جای تعریف enum تازه، می‌نویسیم (io::Error, ParseIntError) و کامپایلر چک می‌کنه خطای اضافه propagate نشه. با widen هم ترکیب می‌شن و کانتکست می‌گیرن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5556" target="_blank">📅 15:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ec0VBaA2XY0qRkNc3px5Rx6G8zOtNH4upzuBeV8_L5rb87hFGqeVpGTV4XmrjDOtIGgFJOJEIZETCV3nk-AnwqUdu79Tfo60CySJDavRR-eAXhefkNT0GHwm66LatUwISQ0CMw1_3h8Rd2Mqe-TDp4arkUBtcLUtOhRFKkN5FB0krV1iviVsH7KMFIUGsN6kRxouJchObXM2v1DPDZPVwEMpieb4Cd_gP7zDvB8g01jxRNixIIXOAfPGBif7Qohae-Lx5yzrfLCva6hJOhGqb9eCPYebcRT6ydBlk2JdCLvV0a46wDOIyG21SLq_VeJnxCJS_7LBLwj3Z5yqLkmsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدلی که وجود نداشت، پس خودت با ML Intern بسازش
یاوراج شارما تعریف می‌کنه دنبال نسخه کوچیک بازنویسی شده‌ی Qwen-Image 2.1 بوده (نسخه رسمی ۹ میلیارد پارامتری که ۲۰ گیگ رم می‌خواد) و با ایجنت ML Intern یه نسخه ۰.۸ میلیاردی ساخته که روی CPU اجرا می‌شه؛ خروجی معتبر ۹۹.۷٪ و کل هزینه محاسبات ۱۶ دلار. تو چند روز شش مدل دیگه هم همین‌جوری ساخته و هر هفت پرامپت رو تو گیت‌هاب گذاشته.
به نظرم جالبه ببینیم برای GLM 5.3 Flash چیکارا میشه کرد
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5555" target="_blank">📅 13:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/der89swyz5vjmnWNqF5_Z5WjEbSVtY-1hLpeVjpHk4sy1o4GP1D7KZtFft52L_hk2kKUzYizoU4UYB2ThzStmm06Mi-NRWNF7kzqilAHCa5ZPM3a6E7QmyAyUR1uDo_O4DnrW-q0BgvkZX5Wq8KgVdhBmyIXeMbaOZCgeO0RsPRKXprPs04wtHYXjZYVs1QHWVoADVYoHmWhJS6bbuo-XnMn7sdIczMGANBpt8nsAU3_w9D8zRuILvPN7xUW6OvyHloT3OIAI-UsiCQofxdz0RdfWrHwEC8_oTOTt2pC38s2gqKs0mTRIcf9GukfkCwoqP5VKBWLAqA9QGSbwoIDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داده‌های زیستی آماده برای AI
ابتکار Virtual Biology شبکه‌ی Biohub گسترش پیدا کرده؛ تعهد جهانی ۱.۸ میلیارد دلاری برای تولید داده‌ی زیستی باز و آماده AI تا بشه مدل‌های پیش‌بینی‌کننده زیست‌شناسی ساخت. اگر کسی از شما بچه‌ها توی حوزه‌ی پزشکی یا بیوتکنولوژی کار می‌کنه، دیتاست‌های Open این پروژه ارزش دنبال کردن داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5554" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله به بانک‌های کره جنوبی با کمک Claude
یه هکر ۲۶ ساله‌ی چینی مظنون به سرقت داده‌های بانکی کره جنوبیه و شواهد نشون می‌ده از Claude برای پیدا کردن کانال‌های تلگرامی فروش اطلاعات سرقت‌شده استفاده کرده. یه نمونه‌ی تازه از سوءاستفاده از ایجنت‌های AI برای جرایم سایبری که زنگ خطر رو برای دولت‌ها به صدا درمیاره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5553" target="_blank">📅 10:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مدل تصمیم‌گیر خودتون رو بسازید
یه آموزش عملی و تعاملی توضیح می‌ده مدل‌های تصمیم (System One مثل Jev) چطور به‌جای تولید توکن‌به‌توکن، با یه پاس و ماسک کردن وکب فقط از بین گزینه‌های ثابت مثل A تا E انتخاب می‌کنن و احتمال کالیبره‌شده برمی‌گردونن. نویسنده با Qwen3-1.7B و transformers نشون می‌ده چطور همین رفتار رو خودتون شبیه‌سازی کنید. به نظرم خیلی بامزست و ارزش مطالعه داره این مقاله:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5552" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DcN4Z6nG9YBRG1KgxaRa24L-QgnKcfoB7YG1twsl_RYW-XLy4ROWUCkNpZRap8z4Pcw_ylWuUCTQ4JETaOEHYN6CeNqzWdpjZoa7xMcIvw3kdTcyjp-wXgl6XDA7IoY5o5j2faxaMt1X39O7UxYjWWSTHn2eSB-h2mc95MKDZsCw5hpyV1GUSw96GYPLzxRZA7ZPxI6ZLA5AtKkTNS-BRhxWosoWn2iG5nB_tR9lVQUecaqQLrFONZjwD3yhXz20vKLTLDnH1NvzoNK-2p0-GdD4dO5ewDKMxctPNTqfF30yXTGgep2khmY6VY4A-UOZWrUpJAOzztGQ5kyzROTnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفیس اوپن‌سورس با Rust؛ کدنویسی با Claude
استارتاپ ArtCraft نسخه‌های مشابه Word و Excel و PowerPoint رو به لاین‌آپ اوپن‌سورسش اضافه کرده؛ یه جور بازنویسی آفیس مایکروسافت با Rust که بخش زیادی از کدنویسیش رو Claude انجام داده. هنوز برای پروداکشن آماده نیست(که نکته‌ی مهمیه و توی اون اپ‌های جایگزین فوتوشاپ هم دیدیم که به نظرم به زودی آماده‌ی پروداکشن میشن).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5551" target="_blank">📅 08:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">طی امروز سعی میکنم اخبار سه روز اخیر رو پوشش بدم واستون</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5550" target="_blank">📅 08:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سلام
من از غیبت برگشتم
👍</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5549" target="_blank">📅 08:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!  آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست،…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5548" target="_blank">📅 13:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هفت نرم‌افزار Adobe، رایگان و متن‌باز!
آرت‌کرفت نسخه‌ی رایگان فتوشاپ، ایلاستریتور، پریمیر، افترافکت و چند ابزار دیگه رو از صفر ساخته. همه‌چی آفلاین روی سیستم خودت اجرا می‌شه، با سرور MCP که ایجنت‌های هوش مصنوعی هم می‌تونن باهاش کار کنن.
⚠️
هنوز نسخه‌ی اولیه‌ست، ولی ارزش امتحان کردن رو داره.
🔗
getartcraft.com/apps
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/5547" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W7e9ex6-Gp9volCwgfjcgVti4PNKWSydJT6i5mNtZ66JONRLYvFw4kpfyFBcZcoDQt0Nb-6v-FxdKwbBelsSuU4cPQmbF9bbnHbI-oSS8DpdyGy707FQbpc4bji5YLfI8btCB_HzzMbbUHdTbUELVza8CyrmJXx-b6Jb5dDZPDqOVJMmSbYcHLgQSxQwUXypLlJHU8Cf-d254VupM9aWwm5aySa_x1nZgyDaBPfg5u4aSzHwY1i0l31UOagnx038FQXLesoupBZKX51ja_iBHXmmn8m-L3wy6EOqIzHOM-dSoOSfCMgY9ZLRm9LxHG2Ayknciojw21QDx1AbHiISmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
ببینید چی برگشته:)) Haiku 5.5
خفن‌تر از GPT 6 Luna</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5546" target="_blank">📅 09:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یادم رفته بود بگم. من از اینجا گرفتم. تا الان مشکلی نداشت اکانتا.  توی رباتش بخش هوش مصنوعی، دوباره هوش مصنوعی یه کم دسته‌بندیاش درب و داغانه
👍
اما کار میکنه @OrcaSubBot</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5545" target="_blank">📅 08:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADeoC_czPNDwh-Q9zoXBdCYfldoqci3V7dC63a2SpZj4MrFMhP4ebxiLcIYTbrLC9ezsiPxvSX6VVZNiCQb-WGQwuw2bwnSbdOkg0kguYxqC3ccQ6hT3bLZqqhjcIgPtsJZ0TU4f4XdczJl8MTpBYD7c6iTEVtLE1Gpuk0xlDvfAzCq1nhmJlm9MTu6aaRZBJaRUJYmaiRNFuSqQATFwXaTFoobeUij-gSnM9NujGdr2RWhHnJcx7EmOMqaCiF2-wtSu0M3gdlTFQ8DtCZwAKIj0vmZ_JHDAcGIY7BrbUB1vyrwUfmKZftDpPxBV82B7Zmwzp2kPDzLHrvcRRY2xWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابط بصری جدید ChatGPT
گویا اوپن‌ای‌آی داره یه رابط جدید برای ChatGPT میده که جواب‌ها رو خیلی بصری‌تر و تعاملی می‌کنه؛ یعنی به‌جای متن خشک، ویژوال تعاملی می‌بینیم و برای کسایی که هر روز با ChatGPT کار می‌کنن(مثل خودم برای چت روزمره یا سؤالهایی که حین یادگیری Rust می‌پرسم) تجربه‌شون حسابی قراره بهتر بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5544" target="_blank">📅 08:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5543" target="_blank">📅 22:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5542" target="_blank">📅 22:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-7Wz4gpTjy7WrYw84YqqD5VPtUq0wSk1AHsxy8Hj_ztX0wzBvs2c5b0fsVlkoZJhAkmtUcBCc4fTddQBeAYsl7i3D5C05meC1mst8P-EQVcBC_ZSTcFCtc2Q74Ek3zAZAC5n7pvIwn9D5H-nc9LkuLvKaU4ut_lTvFCeUSn_Jr00WP4S1wtTfCBWm83dj51QVnqcGkMy4-4fOvx3PiH2OgoIRPciqd2FqQ-QLl1QUkLuWKYGcju9SQbkaz9k3JEyB7YvhzvDguLGCDQt5g_lNPhNLPrw828F2i8YZlGz2y2PuBHVgTEGgr4vLGpIK6q1d00XSJHgXFMcLTqSxetIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5541" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوست دارم چیزای واقعی بسازم توی ویدئوها. محصولات واقعی
و فکر میکنم با ویدئوی بعدی
یه قدم بهش نزدیک تر میشیم</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5540" target="_blank">📅 15:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم گفتم به یکی از بچه‌ها دوتا اکانت بهم بده توی پنج دقیقه بهم داد:) اصلا باورم نمیشه و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد هرچند خب استفاده‌ی دیگه‌ای داره کلا.  اگر که اوکی بودش و نپرید و اینها،…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5539" target="_blank">📅 15:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5538" target="_blank">📅 15:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Math lovers, check this out:
https://github.com/openai/math</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5537" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!  تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5536" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135826faf3.mp4?token=NvH-ekUPRSDA9RrZJ01lQyyJfgpn-4t7vm767mgZ88BF-J2ZxCpy27arhTAwIp_P0peqe0SYvlE6UDyNHReeYgXbp9X-xPa5hZFCTEVD_cEGVN3lxMyJudUxRThoOCIm84E8_EUggx-SZuFNjEKHbA1fNtDIkONanPLZGHEbcxTQb5hn9NUZrmG6hs2uT9m7Ujw8hMW2ublbqKIWYBx9WUEmQlsbUAr7V7x1g35y44zHd4MG7gi8VYrzKIxYOtKYkaQg9lTGEz3_e2eyjSIuWZwE8FZbpq7m1cuJJzsjHG0eIwiJUAQG1rCVO7tgUD-nm0gqV91igl9CqeFP-NU_zD8OeQ2hUFxDTERbMBgsUbIHjSBfQwJNJbtKk3nAU-zNUUDVnw79kLOWhv6M6UAmfIsHu7VVeYQidgWrgp2oNA28ctHuLBiMdqplM5AKbHyZNkm3NXKnySnmJLvXuvZePhxGs7X3gnS-DD_QOBkB8804DfZYuvq6syTXGQevQYpGGhB7zg8M9q3yI6jfhNcyv162Wrw6e3vBwVLgtkry9W_6rwRmCPXNHaHuKC9P1Zl6ZVtGmJ7NBffn6804tn8biRq8F9Utc_M17ILEPwCv2fJ3r8gYCD7gmnz8NPJd9elcS1hLI3tXilR01B3kd2PP1EszWpf_Cs-wdzq4TGSBtNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135826faf3.mp4?token=NvH-ekUPRSDA9RrZJ01lQyyJfgpn-4t7vm767mgZ88BF-J2ZxCpy27arhTAwIp_P0peqe0SYvlE6UDyNHReeYgXbp9X-xPa5hZFCTEVD_cEGVN3lxMyJudUxRThoOCIm84E8_EUggx-SZuFNjEKHbA1fNtDIkONanPLZGHEbcxTQb5hn9NUZrmG6hs2uT9m7Ujw8hMW2ublbqKIWYBx9WUEmQlsbUAr7V7x1g35y44zHd4MG7gi8VYrzKIxYOtKYkaQg9lTGEz3_e2eyjSIuWZwE8FZbpq7m1cuJJzsjHG0eIwiJUAQG1rCVO7tgUD-nm0gqV91igl9CqeFP-NU_zD8OeQ2hUFxDTERbMBgsUbIHjSBfQwJNJbtKk3nAU-zNUUDVnw79kLOWhv6M6UAmfIsHu7VVeYQidgWrgp2oNA28ctHuLBiMdqplM5AKbHyZNkm3NXKnySnmJLvXuvZePhxGs7X3gnS-DD_QOBkB8804DfZYuvq6syTXGQevQYpGGhB7zg8M9q3yI6jfhNcyv162Wrw6e3vBwVLgtkry9W_6rwRmCPXNHaHuKC9P1Zl6ZVtGmJ7NBffn6804tn8biRq8F9Utc_M17ILEPwCv2fJ3r8gYCD7gmnz8NPJd9elcS1hLI3tXilR01B3kd2PP1EszWpf_Cs-wdzq4TGSBtNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه skill واسه claude و بقیه اجینت‌ها نوشتم که اون حس اسلایدشو رو از ویدیو حذف میکنه و با استفاده از ۸ تا تکنیک مختلف که برای فارسی بهینه شده، موشن دیزاین‌های جذاب میسازه!
تکنیک‌ها رو از حدود ۳۰ تا توییت motion design درآوردم و بعد با کتابخونه harfbuzz واسه فارسی بهینه‌اش کردم و نتیجه این ۸ تا skill شده که اُپن سورسه و می‌تونید برای ساخت ویدیو استفاده کنید :)
https://github.com/atmirrr/persian-motion-director
✍️
AmirAnonn</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5535" target="_blank">📅 11:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کم کم دارم فکر می‌کنم یه نسخه از خودم کلون کنم بذارم هرمس جام کار کنه
🍿</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5534" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4It01Rv5altxfzGzazNzqn1izvUfILIuYKqn8lgFqbblsBiT2_mcAJdfE0yXAMANPZ_4lDg_nFHSkLcM5mgtv33-jp3uItym-I-ZWdtpY1mKcw8L1vVqfT9yE3_3g6kijtmdSGh_39IKyVbeo1t9kKqmeezdyFyqpIIPgtcXKS_abeTJouQt27myVqTMc_bzSq6IAiEptvzco0m9DSqxh2sdzxHF9Oi-wcTrwFxaCGZs7-4hz_WhGh06b2l4kYg0nouU43mtjHw5jOvdDLvRMegk2oQeLaZGIIql-Tlug4T4kMbGoeatDAp7KU8XZ6sTIQ8L8FAEf7925Q7rn07nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن OpenChamber؛ یه اپ موبایل جمع‌وجور برای مدیریت سشن opencode
نویسنده این پست توی ردیت گفته بود اولش فکر می‌کرده پست‌های OpenChamber فیکه، بعد از تست کردنش می‌گه در عمل، به طرز عجیبی خوبه؛ جایگزین opencode نیست و همچنان opencode رو روی سرورش ران می‌کنه، فقط با OpenChamber از روی گوشی به‌صورت نیتیو به همون سرور وصل می‌شه و تسک می‌ده. برای کسی که opencode رو ریموت اجرا می‌کنه و نیاز به اپ موبایل داره، تجربه‌ی تر و تمیزی داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5533" target="_blank">📅 23:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBjJfSsbwQPIXKGDbILiORmKUaUXYt4Mdz-9DF5eB_QZ5W-xzregfZR3E4LAhTvG4eRTltdhjH4r2rTs_y3YpQYCipyZ9c7n6qKdiySNdwY_XIEXgGkswHqcmg_9if0jkGKhEkYFDvemUR-tiXdoOekx1HIVgFgfAfJH7sV4OlrX3W1x2rBxREttbPXkHFvs1OPzdAnttikk4vXHc8npAYygTu7Yj6zzZKjgPH0QjiMEUAlL-MYM67EbbukgL688Ybt36s8hcZRBAx_DkjB7bCPiVWob6NOHgo28JnvwZkVugQtC_11VpbD_6S3xihf9Uj_J01cLLUSq_fC8pBv7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل نانو بنانا 2.1 اومد روی Google flow من، و افتضاحه. اینجا با GPT 2.5 مقایسه‌اش کردم:
https://x.com/MatinSenPai/status/2107527090019131503</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5532" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینم کانال تلگرام یزدانه پرسیده بودید توی چت فراموش کردم بگم:
https://t.me/antimatter0x1</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5531" target="_blank">📅 18:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzKlNOfYKVBOR2hkEvN7TdTChQJKrxSXm3M9CN8K4VG6XS0RO0W1jP_57_cP-dqIFXuW3Dko3wo1z9D5HoQzb9AzwWZClQ71OplQ_3QY1N3XKn7AeyGMDG3Ds42R-Tn_W5AqpBAB_qQqVSXnztKCKM77_K2gvFm7CNXKxX7ykCCgQXqu-M_92lFkVaStJ-lxcP9s06MR3YXJeMaZ_MPZiIcnnwU67IbIk9n_ybLFvXDXtm7SE64O3SMZ9L6FbIFUfZ0pkVkyeIMkLlAY6Xzhlot8QCBPpyYUNTen6dW-l4LNgsZxfiBYmEczVp4ErJDRWzDT07b5f0hvjBF2XRJT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو تموم شدش
می‌تونید از اینجا ویدئوی ضبط شده‌اش رو ببینید:
https://www.youtube.com/live/nbOls9zPckM?si=xnkhmSfdlmhENs_2
توی لایو توضیح دادم که همین overlay رو هم کلاد توی 15 دقیقه زد قبل از لایو
😂</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5530" target="_blank">📅 18:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">لایو انتخاب رشته و دانشگاه بریم یا نریم برای برنامه نویس شدن؟
🥸
https://www.youtube.com/live/nbOls9zPckM?si=dnW0hyhkqq7wyJ4-</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5529" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان) با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید: https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5528" target="_blank">📅 13:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfS_FmO-5WldmX23nERWfwJDKSj4NylaeQQ_XGzWnpWXjwWAXxffD_Q-zuLQZWgVcYkbJSTSGkCZ-F0D96xG8zowEx7N42aX-sfdJEC_5b3w_ShPykKBQp74C2r0Rroxhf_kksTa3rsb72vwSTX3cyx3XigJm2qCavlYh1vvcT44cy9OJyIbCx_rfhbT1F1S_JVvga5xfkvhY-_KQ_znfUQ2tClMUYsOx1LvwiJUefmHPk9w23fKtAOnzCdUSKzYEWhfrPZ8NSvO3QuiDu8vlr15lplskfLM0aw7ReidZ1SPLE9b0-1oGcbRXL0RReV-JTxIDFoTjVrOjXpPrBhW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانو بنانا 2.1 توی Google Flow در دسترسه(رایگان)
با این پروژه می‌تونید کانفیگ مناسب وارد شدن به Flow رو پیدا کنید:
https://github.com/MatinSenPai/Gemini-Config-Checker/</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5527" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Matin SenPai
pinned «
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:  1. CDN/WORKER with ECH  برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال 188.114.97.6 استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5526" target="_blank">📅 13:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkTTRHS2sIB1S4hjT06Hgo4GxZ_lwkjXjGjafzdjiLuEg37rrILC_Ld_7WY7M5aOU6OkZjwKmJcyIA-0HmGQjh-LBZXNl-kzCEx6l0KxueuzTYNAwGDImTa4iBuFmlEmh1h1yGAJuoWCHjbfNpzC9-Tf4VGbLEDgq5Klf4ZHattZJAqOnnZoaxJcz4Iel8SjTFA_9dB6q6eU3UICC4UHn1e0M3LY63Wm_gM2AoI0PLzB4_GRZsqkF8IQa78yMxePjTyiROwL_p32VIneHORbagg1vXcDqd0PJrRT5TsW2NjZyx894bFMzhkh3HGtvr0QM9l9XSbsct-jXX10HRWxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتای کشور به قدری اوپن سورسه که الان سایت زدن کد ملی و اسممون رو با شغلمون میفروشن که مخاطب مارکتینگ بقیه شیم :)))
✍️
davodm</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/5525" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw6R-2kyb1Rvc7iWbf9xD4ccYNwT1YMHPcGrEfS95CJ_osI5KWwaitfaPOVVVv72mPCGXjOzpKJ5b2D4nCpcgD5rNOUa_rWFKwJge1Wxz8zWtPrEw_YhtNhVIji7XaNFI_T4qKECVU57GxuY3fdp-7WfYk3FeW_3fwZGYCBZ3hj0MI-I66_BWhDLRE2yDw4BhlOXzmV7JcV8UGzPQN0n87WzDVfq9beGjOIXY0X3jCKHN6qlqEblKpYxslWJb-kZcvVR-ZqzuPBhhttyJf_AKuGJFwyvb_Nkr3lR2inN56tlOugHNKwKvNGaI89RbI7J270YHgDjGGK9QOHlhAz9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnjxWnIv9UYfhEFg_We3bK1V0voGC1Zdgk-o5ybiCmm1-xkETs5ui-rWc6Nd7YrhYKuW1jUNqzIpCEDU5C76FAvwiRikO0JAarT4nECGX53mcVnvNFrx3wLn3YOBA1xQXo51RWr_4RQJ9qZdzoWeTzrZw2pP_eS6lDFkm4jDObe7MMc5JcL83PoJ7TMIRBpQQ7Z5XVCHKBTJ1zq9Du_QzhyCjyuAOZxaqA5VLegdS-sNXiCSIyX1hgxg0AlNITmLC1H3lkBvigzF9PA5ygU66J7omlZTUjxqc5ixbqxcfPM4WP8kIAV6cgMsYQQICZ__CcOW5lvLRoKxjsh7q_eR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwpGBfq9nRRL9q0WX8d89YM6dxszRZ32uxWq4GaHdu2vIXAptQ5e_A2EtJKQqyAaCJaBV__KAwNiG9RChyJpFSoUbA2a3eAzPG-Wis6zdMB-BCUrU-Q04diJ_yp3mMvlHWRO1fpI_8EppGdUelvp_19EbCv84lnwZbZPi3VBi7enbl637xtIoPgfi5klW5xxuB-t9zLbiSjtFS6wBfz2j9ifymsL-9RhFTnXAwk71Qit1-E3dvAiDdl_5mrsYilBqaAFs2QC1hS9A19vHYRWXI3HGfMdO51uSUDP2yTMY1Bc-XPHm01ErvzDgGf1Rd2TlbmoQWS2dAstYqVU_pdNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WaA8YkKE-YEYa-GkGgB7E6TMaUXQ6ffkLqRTD1JNiJHR2pd0PYxMsqVjae5xAGB6yLkmQqCfqzGpjCqf0PPiWaxBIzi6YyOa8X_F7hNY-W5gC-EusJEJQQNbGoMNvsLJeIVLoelpkjRSDVGv1lKvUdlxjtcA9Q3dhkf0Hr6GCWWNu1bvMCWDzuOBdEU8nOgQ1NTFEgZrum9SofTqDShbgAFJy-gItV38a0roZwTv69AgbQHl4fwZ3_IA4eh3_7ZiQdG0Hi8RWBh50d6Yea75uuvt2-v5wAHzhzjMDtUAb6zOmH9liSux1PDBk0Tif8kpD2esyLOz_I3_SSMAuxF9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICq0VwfYbQH5j60r8y2gYWoOJ_Uk0CbZJeCu9jPKugZemo_mezLIwaJqckyJSbNSFw8joDjXofRCHU7Fp--3AXPCw3R0d3NJpl96qqe67fdY5ZyWlziq81_pgXrnv4WR8vIcy8HNqUmx7jAggGk4ZyA5fY2eUl_-1bxKweLc10HWO45HY1w1VAW79qzZwc-xgfanO6Fw6fBVM7cGrUppeef9HTetFr3Dm3q5MPM3nsWJTBgAd0po2yPEQ_Cg9kDDkgNSa2j7UDiEGJ9ZiCwDKKfi5d6ITIt210jrfLEbzOdYUnfTQpUoMMtLZ3q0V9STX_BcijA5X2ew-fjnw6fpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvzDSRsqEHy8xiV6jxjQHkQ5Q2ZsLO40wYAOqv1XUad_QgdCIpDcuK6aGm_E0o3BJ9ZuOqic5SRtK6Ag3TlK9lcb9vpnbkOq44cLDuPq6JFzB3z8nKqLEwRo2bv8LaWdep7-hLG9xQb5r52dQpA1mK32TICIXVqN_1Jo5bX7ZFh5wDamiRDpcMOz7rq-eMhBfSa6p18saQyljZsWTGZl13lqttNP3Ywkz2DXbjHbqiq7ws--WOWx8q2bINOrtzHvptKqR0jwILNfg7jU4HqW083JnFuvjjHzzmbsgd1VJAkqoSyYhSOXf96r-rBpoZFXiLEYbjTYvuC6ZmBu7k4a5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OIX1YPEFXsWRkRi2Rs8F3TxGyZNXC2gFyXrBp3PeI92ay7wvQYZ3hMVTA0l0vKRecxHeWv6eAD9Q9b1tpmstaiOz4XnvDWYBEDbULQmEASMHvy3RaVEGMqA8IMI0_zIwMdhKc96pmNLlgNIJ6IuXMUSNXGPrhw5QCTB_m1Xl_PoeUzncSCbyu3jp_xSQ1StD4wMDTiT_mhVerrKzockAVfiuCvNbxLXCJy8V3ObIlNZgSRbv4eA15SP1y4isj8wlx4gwV6CtmoLA88rwx0725yYbszfFqqajziw82dczgm2NI1KHg2sVFERsKBAuqrbrUQ_z-m_GmCtVk9_83nyAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdeaYscobvTiNvV5PGOIGxgnZzHSNyVKw59NXgtTL-1OvB8P4Rx0fu11cg6wFkkIyojuLjibmapfYT5M_RHDPIQE-8mfeml0L9BstaWIvSFI8IL4Di_KpfzNH6DTPfthEUa_M6DF6WPUDshvOlb25cXYIWTi4gfNPglU2M4dCZ9uqo7ouwWBgnE0sT0Ef6yYIe-e9s3K5_hMPkyODnUKY_aUT0ZZ7Bib1gOx6FhSKGT9sY9eFQnDKyVgZqMNBe_8Z5J4YQLNswwjz_PQf06gVmVOIlVtjVWQsUVcjXb3VXvRw-MhRWKTS6B8W10Pq3u8sHyjLby-D9TlbTnNxaQV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pue5sV-vqedPEdpRTeu2668wi-RUvlN4j_UlI-1UgG7_thkCSkv6bm3o5E5Tsr1JCsHDBdNGGQy4DJWrXvgdr-vLUngoU-xlkUylC3tv2TVg4GSjbPMGF0fdF_PIAYq40tFa-HCuDVLIgEEqyHeC0tNGEFTdxWHYC98cCr6-zc9P35_JjCv9MaopzlWsN6mQXM7XR5tvrC94SzZsKoOOC2_a2InwoRU-XRmR3o13zK_HUMT7YTPsaqhiFB8VF2SQOc2JF0EOdiKIhr9PNSOugAthFw9WThVAI7sHoLAa3w46ih-kKd6b5CEnbwta_VkxXAQY5nshrvfORaF0kN1caw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bK2oQmBCmRn3d00yqCfBARL6I7FcEK-ev-Zc1kj7hce3Uus--O4bjBAMI8lscOJkAT9EXpNiaaDkyklqg8hgpH-wQ4NxXze6qKr1ZxeQbH9bVp2ot__2v5WucWMuFAJrcGcor-D2nleB_xAB4HpyflaxTZ_Rd1icCZZ9hamjalCld5MQUDJiLBV6gTLik-itMDtRlFa-Bb0_VDnLZEKRefak4sDq-xJdgkRNf19Wiw1yIJhpwKFe28iQX6Y3IhWPj_ZGZn0Fd5XUHfzrdYrdNqN7OPIg4ErqZQms5HokOFYTKq4ht-x8YuY1mtHsnaxP_z3Exp3G0dEosLI2Dtn2lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNzUNCzCahGP3LU128bgbPyj_6BHz-Lbxg6Gv119T5sRGSLp_Ly5TzCIausBSTNDxW83ghXT8NzpBCjWsP9EMelCJPOKmFV1IBb1b1lxZ7G_kluiSEHoJCf_3JV0XvldIOZEP4QzBY9aVZ4NurP13-Dku8PS7fkOk78z34NTUi7QSMIuwuKZ9g1fxEL5GrO3cIlcq98EmH9AsYBfGKIIfTAHWUyfcjgr6VSVDqV8IfPlDpczogK8d9rzuOIdNiGP4DBLVGSJHAzNzepoSKWTFtdKw5X3hGJMRyRIi4wlW2tDIC5ro-CFi1U9avV26Q97h6OfAZKrNYrn3F9PomHwbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gc8Ov6yaR0FyRpX3e2UxdyZeL0Fh3Fao1lkRpyzHeM5zZ0PZEhJaEVaLNaR1l1lzuK71BwShKn7p-DBewe8OYb967p76v7uUyRKxC8N3TyLeRwV-OcEhZUYcZgJn7pKBvJ8c7KWLDMLdf6FCxBn3NpNGo54rnR9R99UFDlQdBfBDC7-kSElc5wi_T4XrjeWwjOVTdgBuRdNT67iwZ4VRTNpexEtSayft_9Q39Yweeh_2ULEVC63t8bii5iKL2qPhMP53ojm5tK8WsS5yU2suHEwR7l9RxOwfNFU5zuhbg7HzmjjqWjUx5NCcwhPbT9MQ1YehjZryLf2PouVCqXhj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCCdIIabcgoaKt6SklBSYju5sAYIL-JV9MMmO3Awr7EYGFjjLTSUYhHXQ5foYaOLfREJZ4ZwsMN9YLo7qMuqHFQQWpwGIauk7Q81sit0ePSHbf6caTJK4LK4jk9UTcVn4t3Pw8iLWlx9dHz3yPwWI-V2iJDS6kl_k99Tp2qDZhVO3CThK7APOo82yFvRFxrgVLEM6zwBTEub0tGGvYSC6udKIqf1VjEVOpgp5LCKP9CojFvFPJpo71nLs46FVFM8hR3l5HdpdE-34AgPX4vW7sndzSRmQUbiAopAZL3uaPXp7i2A33a3eumksV7duQyRVU9j8SbolsQRNytSa_pXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=ibFJNG7ZdZKtHIHB8DB_k-d5Z74qZNyYHHRPW8zeHPede_pzppOTEZB5fopggCUUQWvPAouxv9ucWnO8You-Ex62RQZZFGf0verhy0gzn-4ig6YcFnweBOOzxk5RyqgXLUVTP3N3uHQmxJLMRy82V6tCDCG8S3UlS3c2PFpeH4KTkX7INHr0w_7hg2IzejuVA1HdZ4JAht_FkYCoGFmB_RTCsGz5crBwn-pU2IppQjHgPuSZfxs-2Ighu6JB5RB1j0wczj_dEA0xl_KYs7zye7xxGbko7qIDuq6SWwSpFJrvbaZ-65BIUcqYhfVnWBprPzX1fAo_J-Cn-OqF1tXD4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=ibFJNG7ZdZKtHIHB8DB_k-d5Z74qZNyYHHRPW8zeHPede_pzppOTEZB5fopggCUUQWvPAouxv9ucWnO8You-Ex62RQZZFGf0verhy0gzn-4ig6YcFnweBOOzxk5RyqgXLUVTP3N3uHQmxJLMRy82V6tCDCG8S3UlS3c2PFpeH4KTkX7INHr0w_7hg2IzejuVA1HdZ4JAht_FkYCoGFmB_RTCsGz5crBwn-pU2IppQjHgPuSZfxs-2Ighu6JB5RB1j0wczj_dEA0xl_KYs7zye7xxGbko7qIDuq6SWwSpFJrvbaZ-65BIUcqYhfVnWBprPzX1fAo_J-Cn-OqF1tXD4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LSVYdpXGv1uCsFuz0ixvEKWE8KPtBvknrvDCiXcKW1pQTraj9AquIhRnCHDuYpxt4fIH5frDRVXYYXmAsvV-jdkJ-1gem6e09rSLhr1wS4vTdVFY1An3p-Xp9Tnonw2Ot2VculOBbCqe1brhuiucWJr4eT16HmHz-0PM0MS5i4csJYk7t7YdjzNxL_hE4hgqaWWYYIOJdcAacWuLShI3MkLc1hP6BhEN3YhcgKVtLYcLQnbPhf29LuzsMDLqUTIiqCVI9-dKE9YgF6RXTukC3I86ttpZ73uptUkAVN3cafJV2Oo2acScCAudDaRkSPoDITSaqvNMJ-riOyU8EQxpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rv6lmiVefcn13PJLoZDyRx9f2Os0vEOVSude58UT2LKqE8ZwCcwP636M1zeuC8SYuclHSIejobN0_3fKrl-UXHRgwWE4iSF8kb_-4R3hq8F5P91qRqf1TELUZH4OSVVrzeQ4_V8DEBgrKzyy4ZZTLGPyKwa9OjVmfplib3QdBryrO9f07JvViXKqq7tyU4hXd7oS8dpznoLUSL9Gob2iHT51hT8XvYhGSEGhTEJ6CCl4kIVHnUXLk_eU-SN7895baSkMNppeyB23Ipm3rYHmKrQZ6PZ3Ib6HQbNjLA4QaIInORGWvSi_-H7m3FAc1ybMukbeG_N7L4QLk-auohdSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pq2zo5d1UKpFUnicOWpR9wWafV9h7yoPnSEodE-OyhIBc4g2R3SOdJC3LbJSoiumMl7-doFdhiODfk32SRzkClSam3d1pIwbgSg2jSKkr5G3sksJKnpT55JSDRyhwZm2HZOQVrtgpY0FuYMIpyjOW7S0TUsb2uTUxrR3jHu2a2BP7LvnFNIAgMmbfZVVbwUdR0vghi-cgLVXeWUckY8vL2CjitjBO7J1JVbDhIWoDMu-XZroIZImxlmvJ7EiOH-91auPjTx6kuabSOOB5Trp9HbPIggM0M6FQXEfEH4ti7loHKp54o-NkkVIk10zjpWQm5fULInyLuyoZVhFASi85A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHRf681wqKa3S5VVB0p2dLJowb_7RzAu96Mb1VvoQJGaN3l8P2cItyAgHAtKthLc0bKZK4c9DnuVlfJJUcaQJJcDMVxjYcOu8MeFYDXasX2ZGiK0QWLHwQaQ5q9SmlFuzBTOkiX2k1SdMfMt5708EkpCGYZ7TtSMT552Gha-GVj30b_H48nWT4zyTsFRy8Aq7kb35aBRHirpjURggRqbpJYnmkwf6EqCcUmpJcv7RT3QKcqzmYAHvSN6H4fQAkfVBf-oIJfHzuqcwprRlvj5XZUnmmkorp2aIOBSoESnwac3q-VpEBcwKiXoUpG9LwBjmJc-IPOGIUsosXD2qI3JzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1Q6PPtTkl5tsIXG4fnX5APrAHwkJqmWopWmgeVpZqDFZxnM228QK4GH0xwHThTSDBSD69AquAZjJpoRaYbz_66yl1URI06U1egqeJlokyxI3uRyGGV4kV0irT2NbaMYIkzrd7A2-bZravUdAgPlyQTAFoikRRW5iOoWQAEqAmooT2nOGGO2_6kvlYuuKjm5zvr14Zvtnd9l2G1B159T9GrM0Kql7gLOxoii1GMldjGgJJ9x1yV8oPW7igjxPcKHpSyH3fqoCAjHTBlCwxHZCtQ9VN6g-sc1Mv8p6tCFtetfjfTmJAtWxLpBUwzgdxMUp8EZExLKX0VQU_BIBPSMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVv1egZNi8unfG5Ub91Tu18BaTvT6ZhNioCq2kk8BOvKPqQlsJapocD-ZX3-RqM0NDOalXbnTu0Dcei3lE74vbvysF5P3cTws-KyQpzMlIpEBA2lHHH_FORHZl8Leu86mVU2iEZ5GX2net3MggegXOgym8AFoboS3WVjMIRFDSaqPpbCR6RdB7-_5WNGa5VdPpnpeTSoXGQbT3c6X9QNQcShKZ2ISpS3u2WNQ-MEVKRctP4li6J_sLDuQKBVa55aDW3nt5fIb3DJzAFssmt6brC7J8YSrPDTNXUdbz3YX5hWSgHpoxvy2o9SIlxE7Ef6c_EH4SXhL-Urv43TukyRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZrzzlzthc74T1YEm1dC1T3c6_R8G7q8_9XnMocIaNlxzj9pBiYE0kywO4frA0Ss_GLWTEBGmYNDSyzU7TiqcV6bUVB4r82BAa9A7G6ZRFVUWZfJisLaWp2wUMOpqWPjDvSIUWbiUHADRuu19u3ptSu8b5jKTww7UWiYAWuD8DYuooPWl3Fz7RLeTTI5tW-vl9p-qOV-f_gAUhWISDbjfm5DKrVRnF8AE2ex8w47P1qPBMyWkoTZY9W82rFO40M_C3HMWnRq6NE_hsXJHbZ9eynKtXg8Xs9giZHjqN1SJb7yIFhp9mqKDbDjOThvIsVd4Bf9K41I4_t58LlI407gaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHi9D8bvWsmHbe8qLp9qOT4lAQyPWYmrkVizLBVhFLTPSDw3ZfkVjqWJH3pdS0nhieHp_Te3G8ikNjNCSLu5peOYh-nOpZB51wwKZaI7u056BbDPD8RtBc80_zaBrl_vI5-GaEhM77DNEf_VXS45z1S1zfUG7ysF-lOCrZiJSY6uQuBUxOj-3PBtInpRkMyKVlDjmCtvcD5QyuJb8DWJnaB_obfprrjWmDR2VPuW7huNuaydspht9LEz78dqjqEzg3lBESf2A2R3F7XiLa4Dk8fcbuZiKHbx0DzklqPf-XIo8E59cOM4GmiYUIGVcrHekYrFni5MPR8QniAIWXBHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WHJkVE0lRdLcaVoeTlYNDUa5omIl3s96YleMlQ8nJFiK1Ma2A6E4Ts9uehQvi12alFd2AStRWv_T9UdAIn0RhwomoaKJ3Zyj8s1XTMUENnbFsoCP0A4RvJHo67e7GVnIfMA3q2zNzqsH5jKAe-QZIwmNb_-4vSMV3nsz8ndmWIcyxZtd6zc2hyaN7ac61bQtBGWPY2KQ9_8BeWZNkNX2hWgX-kwJwizCqTZNLyil4ZlVhHjaQIjLi9PDHvvo3xEN3w-3cy_6hF37SxomZGfOTUN_ZLAPOZyBpfaz8nXe2DM_gTc1EdLkSCGplMDcKREEy5s2o7BSfm1ryvB9_86dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZaUYB-GWdyrkavNfAdDWCD3VQuCXMh8uQdZL1trzEwxOPrDnX9lAl0U1w2ucfauYgG0jL2zgr0TCNVMg3g5sTKHUpdo-MngWmGPglsIi-0rZRM6Z5MGe-uPLM-81msMnkUqc3G8XoK_9zrJKLg4bRqUqmspRPBUHI093YHlQlcJUk3ow6H5j_QRRErXsuGx0B6rTvzRisq1OELj4uWSnY8LX3DdlXueXEIO_6jk2149B9qSvsNz-R1hWQ2Ql3Oqbcyp6UPG-t0t_X99a_XvJhCAVHXnEOmk1sFf9-yIWHMTtN5Mq4Gle4eyZrmnPR0iZnnCWeTNk_6qv3xa7YyWVGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hX3U9Pt2Vw24-ogackFuYex4XZIr3SqZKsztnJxbyEURJn71suvUvrOCJBiBKXec45iANVY-Qs67pls6YSv7_3gyONGgffMQby4YsOYAY-TBJPWdoLMjx2ScYr0HUmkg2wVgKPdYYJLEU2w3mX1FjA0K23Ydsfl4Dsenc6amE79ojeODnpQFHrwxB17wTZSjfXBFfan-nDaLKFfv-CMekH7jXriQ4mkhUya4cGtWTrwsSh7MM1rU3-SyaAA5Fq7l_5QmvYYV3pqVkzzT8aePgWX6OMqGrdZPB4JuC6jkW29nlHdhjDpafczFe0Q37Gqf1ttqOPeUS7LSx_kP9kcF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teFYeoBIpi5Gz_TB6oKZex3Z2h3XVZrGwd0Dx1Zfe305PGj5akdW1wp9rrfeR1qUZOLt0O2CvW1QafPnlW3o2GNePPckTSmt6q198uvhj0wAdOWFJOfJOrkh2lTQtZf9BuxN6v1BA8cIOrU9ekw7w3PF5wd0jH2lVMOjTmLbr3yOSgPI0YcMSdojJ1wN_dZrSFuTaB_HA84q2UNO44d3wiDqJaVq2bP_96XJDGHnvht2P2hAl7KgB5S767F9E_IQznvb7jivDNgcCAhI2XMouxo3Olyvg0OaZVPbApa0J6HYP-SwHsMPEJ47TzqkgasLw_fSgb-NsTG6gRQI0ZQnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
