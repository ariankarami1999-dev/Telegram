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
<img src="https://cdn4.telesco.pe/file/BSao45F0BMJ29sK_hD1E8f8kicSAKpqlvgrT6-VASBGzoZsx59tyrT31D3vnYUFXvdyT75NaDLWlWUXT2DVL0QQyzUHDNe_wQRk1UHU_zfUUjni4Vtquffw3oPNAxCLEmgfi24FwE2EyPZvLDwplJyg0_K3LuOY7qKK-BXD4495Ct_LbCvmQjK8BwOZF9ctt3dk9B4uYpefHj3UX00TW6OVHwmindZuECD7-CQiv7jSR-Asd8RZIjdYFM5JE3hLxNo0S8zrEjBMEStGJoNLx8D4PztxMoop9beFTFXHPky994EM1TcP12Ms5RGpNp0MmbiNZaVqVRwSxV1X1GqSITQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-3088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU5zi-BcTJzmGiWWpWxWa5mJpkH43l4FpvU-m_oqyZvNmDeSCbnBGJPyYjDYSNQIWBjGAtI672mMuU4GEImqGr9Mu-vwRsjOhsarKH9UObsyoHquEvklMcOxanKof3JQUAWUclvLM9tnj4_cJgb0-zJ1OuUaAgbNKx-xu449kZYWFOd9Lw5VydgiPB7sm-QpvAwuhbUBmysCljZ5h7rLuS4_lahwavC4ZiEpERcK76fZP6A7JLwxL0F3-lDfAMToimhgOjCB5qXXW9MkaO2zlwDFdSv_zixrXhN3mStrU7fvXzIQDbH-MyQAiWfx3jRyDj4IQsyKl-G_X8O6aaQKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک حقوقدان: حکمرانی فضای مجازی نباید به رفع فیلتر چند پلتفرم محدود شود
حامد نیکونهاد، حقوقدان و استاد دانشگاه، در یک میزگرد تخصصی با انتقاد از شکل‌گیری نهادهای موازی در مدیریت اینترنت اعلام کرد تمرکز صِرف روی بازگشایی چند اپلیکیشن، پرداختن به ویترین ماجراست و اصل مطالبات مردم و امنیت سایبری را نادیده می‌گیرد.
🔹
نیکونهاد تأکید کرد مطالبه عمومی صرفاً حضور یا عدم حضور یک پلتفرم خاص نیست؛ مردم امنیت حساب‌های بانکی، پایداری زیرساخت‌ها در برابر حملات سایبری و پاسخ‌گویی شفاف مسئولان در رخدادهای امنیتی را می‌خواهند.
🔸
انتقاد از موازی‌کاری با شورای عالی:
وی تأسیس «ستاد ویژه ساماندهی و راهبری فضای مجازی» را مصداق دور زدن نهادهای بالادستی و شانه خالی کردن از مسئولیت قانونی دانست و ساختار کلان حکمرانی را نیازمند انسجام و پاسخ‌گویی خواند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/iaghapour/3088" target="_blank">📅 17:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSimbaServer | سیمبا سرور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpu6_4XbVhnkjqxUwzV8Ru85gp02UC2CeXiJ1GWsoyxPcS3J0xVCRfE6ju_dPaVJRrtYEzkNFKhPP0aE7ylp1589VFGuP_tEwRq8Kll0aKXsKUGY2F5H57W3WQ9D0XNV89Eu_8NS6sR_0_pCxE1EXX-r4WumSRwYEXBLtB-rzViS74MygZn81rojMwd-dRrMFPxElxSDd1rM-PqHXJlfe96yyCvEk-1FLTf-Xifb3xrVCRUB41O2xex0kkdQA13rPcQbhRkGQ3DMKF4c_F1cwzobl0O42PX4duPTHzhb1LMwwlfAMWSj-CpXH48IW940Y1YiIi-2dEqQuTCAsgv2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
سرور مجازی ایران | سیمبا سرور
🖥
شروع قیمت سرورها از
۶۰۰ هزار تومان
🎁
۲۰٪ تخفیف روی سرورهای مجازی
با کد
SIMBA20
📦
هر ترابایت ترافیک:
۶۹۰ هزار تومان
⬆️
آپلود رایگان
♾
ترافیک بدون تاریخ انقضا
🌐
IPv6 روی تمام سرورها
✅
بدون مالیات
🛒
سفارش:
SimbaServer.ir
💬
پشتیبانی:
SimbaServerAdmin@</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/iaghapour/3087" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgrU4TunZr_0o1hSz4Nrp_eFGONC3uUF0XgLKzW56CW09Fh8kTKOLy0sf0uyzihqhdiRr0rk_XdvFYaqXqJo4olYcjcoSrfwMlqHWZ9Qt-GtqarVd5Dbi-yA-pY8qMm9XHwCe6TdFMbDXj8E8335vjajLkwVIioPKQlrxUb443N94oqUC0U8qBKHBQpS68n7UknjPV1YelnrF-8zLz2S7ZlDPfQmR0iLAeckitrnXrH9Dh3cSAbSfGlj310js0f52Y-xTq6FhRBF_FwoCxV8_B3mcl3XrK5nbCrYuUx_H6IPaY9QBujw3IzaRQDz-SW5rtBenMRFrLagNgBdHBLmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تانل بین سرور ایران و خارج با پنل پیشرفته GRE
🔹
تو این ویدیو یک پنل گرافیکی و فوق‌العاده حرفه‌ای رو معرفی می‌کنیم که تمام مراحل پیچیده تانلینگ رو براتون ساده کرده. با استفاده از این اسکریپت می‌تونید به راحتی تانل GRE رو با قابلیت‌های عالی مثل پورت فورواردینگ پیشرفته، لود بالانسینگ و اتصال سریع با کد جفت‌‌سازی راه‌اندازی کنید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#gre
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/iaghapour/3086" target="_blank">📅 17:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZUiqPWcP6FpHiH0XtSs1NGWYmROQ4i7-PaG2YINnuWZ1RlXRP95neOpaQYHa3jPvLOLRK59TD0SZwvnHXuxh7lWeVc8pHDWJVyUL2fS1DEDr7DMMxSqjwyQo0OJiRGgKa0fPBTJZB9up_6Z_O1cXR95glP8OQX0ZwhgRyfs1TRKI08U724dHMmEFXgXekRywLW-DH4nn70tilw5-20bOvq4DaTqOWkI2cvaZo8RzKXNmWscb4C7y-0LaoyrkRynH60m5NMrAcm6fDorrE_hdL0z8clSz52iMNyvWPAyZ0UDWawl3PZGqxgzcEngP7MDmrHpg15Svsp7FqI0y1DEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی افزونه Xray for Chrome؛ مدیریت هوشمند پروکسی‌ها مستقیماً در مرورگر!
این ابزار از دو بخش «افزونه کروم» و «برنامه همراه روی سیستم» تشکیل شده، به شما این امکان را می‌دهد که کانکشن‌های Xray خود را به سادگی و فقط برای مرورگر کروم مدیریت کنید.
🔹
پروکسی اختصاصی کروم:
ترافیک فقط و فقط از مرورگر کروم عبور می‌کند و تنظیمات پروکسی کل سیستم‌عامل (ویندوز یا مک) دست‌نخورده باقی می‌ماند.
⚡️
سازگاری با VLESS, VMess, Shadowsocks و Trojan.
🔗
امکان افزودن دستی لینک‌ها (یک یا چند لینک) و همچنین پشتیبانی کامل از لینک‌های اشتراک (Subscription) با قابلیت به‌‌روزرسانی خودکار.
⏱️
تست واقعی Latency سرورها از طریق HTTPS بدون اینکه نیاز باشد به آن‌ها متصل شوید یا اتصال فعلی‌تان قطع شود.
🛡
جلوگیری از نشت اطلاعات (IP Leak) با مسدود کردن اتصالات WebRTC غیرپروکسی‌شده.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
📌
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/iaghapour/3085" target="_blank">📅 16:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPD-fqpI7EzxBovizpOZZ3zIjU72qPGLeTAxMdcKFboMlbxBhvtVvTUVr6GZQcLMA6EQsvkQLvOFE2QX5t0Q7b8n-6vU2lO9aw0g8OS38Et4e0GwJtc18qLfcFd1ROCr0SPlRcQ4y1iRb2FTPjCZDQeQz9rUe46MNObd_aqyiEEGfl7e43LlSh6x8mwe2djMvwNa_1q-n7VwOPqvzzIqdfKaZ5vU0O3-K-ox1AeatCquzp6ckIHrWm35CBVnIHirWq5d60_HpEv5oRuzfkw1hHStL8K6GZX_srfR34K8DsvYHCjmydzs1SWnlDB2N84E0vf-V1Rl_NhzEnyqKwCDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ پنل W-UI به نسخه ۲.۶.۰ منتشر شد!
این به‌‌روزرسانی با تمرکز بر سیستم نمایندگی (Reseller)، مدیریت دسته‌ای کاربران و ارتقای امنیت منتشر شده است:
🔹
سیستم پیشرفته نمایندگی (Reseller):
امکان تعریف لاگین اختصاصی برای هر نماینده با محدودیت ترافیک، زمان و سقف تعداد کاربر؛ با قابلیت زمان‌بندی میلادی/شمسی، دسته‌بندی در گروه‌های مجزا و اعمال تغییرات گروهی.
🔹
عملیات گروهی روی کاربران:
افزایش یا کسر حجم و زمان کاربران به‌صورت دسته‌جمعی (با پیش‌نمایش قبل از اعمال)، بازنشانی گروهی کلیدها و لینک ساب، و امکان حضور یک کاربر در چند گروه مختلف.
🔹
بکاپ خودکار به تلگرام:
زمان‌بندی ارسال خودکار فایل پشتیبان به بات تلگرام (روزانه، هفتگی یا کران‌جاب) با جزئیات کامل سرور و حجم.
🔹
ارتقای امنیت و پایداری:
بازیابی خودکار قوانین فایروال در صورت ریست، محافظت Rate-limit روی تغییر رمز و 2FA، رفع کامل تداخل با داکر و دیتابیس، آپدیت مستقیم درون‌پنل با یک کلیک و فونت فارسی وزیرمتن.
🔗
لینک دانلود و گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/iaghapour/3084" target="_blank">📅 15:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/iaghapour/3083" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTmcewjKq-kBdR-4L-ndM4m0XNgjdn-doH14bihMDmTxmOn_pUMf0Akr0cGyd81jOa-gxYkmBZyD-VLGoFhzCnjfk_UixNWc_9rk1G8oy2kXeX01yZEUif7lixp9bMnMrSPy5mXz56bjpXwpRoZ1XoofzXm8emZ_bYcWMKkDD7G1AMkvaF7SSv7EaUGsSjw8w9Fft8kp330ISXDXkhO4YkJgaJCjT53e97Dq7BMu5A8McLkmGWn8Faio8gGpe9-kjss644Z8e-jla54u_Py5mjBsaNEoGzm9HZPyAyBWBQ-Bqfxgmaz2WE6-nSwO88U6Wub6MOLZ8Preb0mT_6JMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWCxmG1vL0T6MKxxT0GYVnFlShX_nVCwidCmBZjcsbTXUr9OZZ739Ab-SGEJB7OpcBNfTDxyQRPKlVI8f62L80jf3uEYYu5IRVHnpb6HIaqXWtGP4yn2kJG2I1uXAKVlILhC9vvuF7jbPhWBBMUOS1QlmWpB3BTE-eWNjAjxzpODKfO9-Z-iF1Awhe9HQzc8StY2GlEUi5q1T2Zs4r8Do89Ax6TfuV-ZJsR8LLF-l2H-OpcjrFYR96jzMCub25nHOEfJHBsZOSALdZlNedZJHdCqzGJ7RWPS0FMWYSfH9fOQ-raufEq47dhUT9_R6-zWXB4Pv4a4XiiNfpjCDDT9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Row-Template؛ قالب‌های شیک، امن برای صفحات سابسکریپشن
اگر از پنل‌های
3X-UI
،
PasarGuard
یا
Rebecca
استفاده می‌کنید، با پروژه
Row-Template
می‌توانید صفحه سابسکریپشن پیش‌فرض پنل را به یک لندینگ مدرن و کاملاً اختصاصی تبدیل کنید.
🔹
۱۷ قالب متنوع در قالب تک‌فایل:
هر قالب یک فایل HTML مستقل و بدون نیاز به منابع خارجی است (اسکریپت‌ها، فونت‌ها و کد QR درون خود صفحه پردازش می‌شوند).
🔸
امنیت و حریم خصوصی بالا:
بدون ارسال هیچ‌گونه ریکوئست به سرورهای شخص ثالث؛ تولید QR کد و اطلاعات مستقیماً روی مرورگر کاربر انجام می‌شود.
🔹
کاملاً وایت‌لیبل (White-Label):
امکان قرار دادن لوگو، نام برند و لینک پشتیبانی اختصاصی شما بدون نامی از تمپلیت.
🔹
امکانات کاربردی برای مشترکین:
نمایش مصرف ترافیک و تاریخ انقضا، دکمه اتصال با یک لمس به کلاینت‌ها (v2rayNG، Happ، Streisand، Clash Verge، v2rayN و...)، تفکیک سرورها بر اساس پرچم کشور و پشتیبانی از ۵ زبان از جمله فارسی (RTL).
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/iaghapour/3080" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEiNCYq_yJIzhZV9uCcDZXpQ7AGY_GKvXJFdrNrloZgaclOrV18KhTd0NxLPusydgJP7VxDbElTahe6r6Dnb9OY04LzxfoDlel3ptJh6PlwYYNZ_h7xFd8IZ4bV5yVXok1WRD5Dgq6PytxTiNu3DPNHI6j1hGoFsnYg5l7mrID7UetRwsv3hd3Oz-N_-NoyUfp4wjU3Qj49b2aGsSTqplfkLxwufmbOLeBoe_PTk7emK8PWAJDHzOiK3TRKESIqWz1ipcMOYySwMGMqnDAvAtTW8UZEy3u8_WMwyjHAc0wWCqtnOBp5Ve0WYVh__pGI3vRTma1XhKZQ_dBANEiK6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aESy4Qt4Ve40hmbWTgdya2EuRU96ISSK2xNfCrBsxy5qeqcLFs_NVJG-5MrCv8vu8Z8tzqVRNd7Dsv2o9jZW0nOH7sPhEpU70eQ1aEKJKjaeDlF6khIXZQrozz5hKvFK7FVOYJZWRRtYBTDHDilDK3zj5nu5mOjTbMlhLvDcCR4E0zTKjfo9QDvpFsc_LecJHYK1q2gbNOMX0I-yLXhxoVzgJ7Ruh0DSBR-LLDAVyUoaymtVVizUQGI3js72dDr3CV-MSSPmY9e6Q1Q34A7qbfaWI-3zofdNI1EjDK72z6znsv9V_cfakibkAjcCwXkqQI-mtZF53zrP-jgBnNkSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه ۱۳ هیدیفای منیجر (Hiddify Manager v13) منتشر شد!
بزرگ‌ترین آپدیت هیدیفای با پنل مدیریت متمرکز و کنترل کامل روی جزئیات کانفیگ‌ها در دسترس قرار گرفت:
🔹
مدیریت Multi-Node پایدار:
فعالیت خودکار و مستقل نودها حتی در زمان قطع ارتباط با پنل اصلی و سینک پس از اتصال مجدد.
🔸
تفکیک آپلود و دانلود (Split XHTTP):
امکان تنظیم مسیرهای مجزا (مثلاً آپلود از تانل ایران و دانلود از Reality یا Cloudflare).
🔹
موتور جدید با هسته Xray و sing-box:
پشتیبانی از ۲۱۸ حالت پیش‌فرض و پروتکل‌های جدید مثل AnyTLS، Snell و SOCKS.
🔸
تونل‌های DNS یکپارچه:
ادغام پروتکل‌های MasterDnsVPN، Slipstream و VayDNS.
🔹
بهینه‌سازی عمیق:
۵۰٪ کاهش مصرف رم، شتاب‌دهی TLS، روتینگ بر اساس دامنه و تجمیع کل داده‌ها در مسیر
/opt/hiddify-manager/data
.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/iaghapour/3077" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd3bwiTsczP6HOmEIW8WAk9MB_dKomi7cSjYjiv1xZm1XVSbU-phyRcP7gNoYfeL4hmKLTEI2wDJygk76laljnwjH-8id6qIyn0CxY0hwTP5iiZHDIGWUhR7CXBJ9jLoVx1Jh2M-UGzT3V6NiDPLCfDQ0t_PbCBXD8LIxFrrkDC-jeiokt7lIswNIhI-qzCUSESc8lXo-yOtk8AXjH2yZ9HY4fSwpgE83CtcMNicxE0Je-3xVGQu-VwOrczgIlm46GdjG8Tsdyf_9OYSX754eQJujJS2UIjBwVZ4KskrM39HePx2L4HQ44BfH4sMTHMsXEQh7x5n7HssmxbynxBV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg9pB0BQSzCnZs9VUHeCGJZof9I_bT3c45V_eKA6WcrQItrC1d95H-KLBEmtPbxoSdXUhxUi6_1LGpPs3h9HoCl6TXBBkoPCQ0K45wDW7PX5U55xbAyuPMLVpLyu9hkCnJOsK3Gk6QId6N9dRVrqPEGQFp3RwD35rSDal1bMFiJsFqVEwdezEvn9KrhGpKKZ6Akg27vWriLoKD8BOWVx_Hoxu6_gDVH2QCyk2auPhkQjBI4Yob4Nfx0LrO73OVg27I92PGlFV6MF_PsbOco1M7mZcSBFpnFGegpDcrCS3rQUr0L8T5W1__Xek6vPxZCqf8gGTfiGpOTogTvRqjbaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AISpB5WHLaJqqexGj4__lX0pRZ-gwB380iduo2AqrVtdYl8MYMuzrckdOl9VQzJUXiy-IPTPDGFXoY_-4O9ZY1EArv0oCvqLdMqn4e9gqkSI2MO6GzVTrhLbDDXpvhD96UF8eyo-esTdI2dRL4mT2Ljmsq12LtjXYcfloIwZCtX3BVXfg6CKvmmgEKPwILHhL6niF9HhezHsEGx6vEIBoHzyc4bXuFrl1gKiVjxvJ1ZR-fPdsFW-k2NFp9QuVcgzSuLKjXYCatpvFYjMQjD16dYQS4nIr-YAHF91Ct6poEEKE-DJsCvdi9Is5z-BElcFARTV2zhraG5su8He9MmNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6QCM2xHLyQBQnQaNFSRXaOOxmEAIczyLnQOL71WTWdU9od0S48_85m03uxzKLEvDjFRbTVzv0Z5Qfys4BLLMBN1h_toM7dLCdQ2Os5V3Ya_BHtKukX5hoamufpYgnX8GtCKpfrWo_fy2lz7Quww5ey5fFiktOsyOfFUjGCshkilT5PkBXS4Sraxs4DfArFgGtfES2Qhmdq-650f-ukZNgOTYpj0JalY8WU46gIjbqyqoDVUpNz-Ke6U4MDJlX9KQXWl-Yu4xJ6BFigRkCnai9rpZTl5pyiG1TDfyHpOYJKM3qHNsWygr8F1H9VJmRhkLL4K2128_92gr6OJ6wqlpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBcHDkqeEoKiiiAyMm8CLvPsdOsrRg09NMYDSaf2XGyNLwfSYSmKtaJR0P1l2qUeBtllFr8-hHdml0inIMie7FkzVdJvfI8FZEz1dw7rLC1zjhUalkqiwASybgUKDVY7aqvvA62mZ1JRfvopyr0XwuzJrCz-4WgmrCmdOs7yxUadn9kbd-gOE84XY9kZfCiFK9li9F4b4Hfjb_UgPfM2Y2yHRmsVkxzOSAoVKspYdXpQU9RUTfwY1f16lA3Z5JGJzd-G53p6KqFb9tot1qh6hUUw68tBLvrAMn4F8jif6WUvVIonRGSZ5CFxWbEmI-qBRIw13CBA3LOs4VCbp5ojyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون کامپیوتر فیلترشکن بساز! (مدیریت سرور با گوشی - اندروید و آیفون)
🔹
خیلی از شما درخواست کرده بودید که آموزش کار با سرور مجازی رو برای کسانی که کامپیوتر یا لپ‌تاپ ندارن بسازم. تو این ویدیو قراره یاد بگیریم چطوری فقط با استفاده از گوشی موبایل (چه اندروید و چه آیفون) به سرورمون متصل بشیم و صفر تا صد کارها رو انجام بدیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#گوشی
#سرور
#اندروید
#آیفون
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3067" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=Orv02JkQgV1spZW7YC3ohDpXQ-SZTTgWPC-VYudf7o3ip7JNtaQrayX6VhnGOYuPu7V7RVlSU-0uWANBP3VpP7Bdg6CldDyiXlZ7O9eRf6Fks2UK8nbOjB1j0prkYr1u_gVAo0BmmdUtFiQpZOhrCh8vlFQeN8JtAZz7n89wllBdgEsKI3XXVnWsuzVzqbxy5uU_IpuEEXHpI5pk9ZOUOw7C6RjOPijj_fORjF0YPPK5erKfaq7wdAdJwy-xFB22lrSUGI0wcmOGG1MGfm1Zyx3nvRWJaewSfa-2uZna_ZKbenXooo5bJFjiT_8rmGCcokhoJejyjdrsuxzk5s6w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=Orv02JkQgV1spZW7YC3ohDpXQ-SZTTgWPC-VYudf7o3ip7JNtaQrayX6VhnGOYuPu7V7RVlSU-0uWANBP3VpP7Bdg6CldDyiXlZ7O9eRf6Fks2UK8nbOjB1j0prkYr1u_gVAo0BmmdUtFiQpZOhrCh8vlFQeN8JtAZz7n89wllBdgEsKI3XXVnWsuzVzqbxy5uU_IpuEEXHpI5pk9ZOUOw7C6RjOPijj_fORjF0YPPK5erKfaq7wdAdJwy-xFB22lrSUGI0wcmOGG1MGfm1Zyx3nvRWJaewSfa-2uZna_ZKbenXooo5bJFjiT_8rmGCcokhoJejyjdrsuxzk5s6w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzv1lzIzrEIfa4TViIUnVkYtvc2uRLeFvRR8cflSjXHZaWJ0VPMX3NV9wACnEGPRjLHK0yU0lss0Qw-7utyH37SfGDD-ZknRKAGxKIfXJoBdx2Z7JIMvYvW18bm57zzNOmumMvvYbp83MIiV_R2MyatPqf5VQidr6fUsytgrzNaKMsHMqkyGV2S0OZay85UwpQdLi7MRrUk6NnBFmKyvcMGzyfdn5vTIOsFZWMtuNr-lWsQh4VbSU4Gm8hq35soupNiI2iOZPbp235-mPLWFyNYkDsV1KtLGiKXqNSL5Moan8AtFFE9oan39GigK4GrRZKpqvuz7kZIENGYg7Y0m2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی VMTun؛ تانل کامل ترافیک ویندوز از طریق v2rayN و Xray
یک ابزار کم‌حجم برای ویندوز که پروکسی لوکال v2rayN/Xray را درست مانند WireGuard یا OpenVPN به تانل واقعی در سطح کل سیستم تبدیل می‌کند تا تمام نرم‌افزارها (حتی اپ‌های استور مایکروسافت و UWP) بدون نشت از آن رد شوند.
🔹
تانلینگ سراسری با Wintun و sing-box:
هدایت خودکار تمام ترافیک ویندوز از طریق مسیر پیش‌فرض و فیلترهای WFP به پورت ۱۰۸۰۸ v2rayN بدون نیاز به تنظیم پروکسی در برنامه‌ها.
🔸
جلوگیری از نشت اطلاعات:
بررسی و رفع نشت DNS، بستن نشت روت‌های IPv6، و مقایسه تایم‌زون و ریجن سیستم با سرور خروجی.
🔹
قابلیت Pro Connect:
فعال‌سازی هم‌زمان کیل‌سوئیچ فایروال ویندوز، بستن موقت IPv6 کارت‌های شبکه و بلاک کردن QUIC جهت رفع اختلال.
🔹
پایداری و بازگردانی خودکار:
برگشت امن تمامی تنظیمات شبکه پس از دیسکانکت یا کراش احتمالی (همراه با اسکریپت
Repair-Network.cmd
).
🔗
گیت‌هاب پروژه
🔻
این پروژه متن‌باز است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده سورس‌کدها را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3065" target="_blank">📅 15:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgWrsLyNh9AOH_bS-0MkPzVfCp794PcOVb4mYQSURV1cStkZojgFJsapMZgTCDLVxOkEcrXDrPa3u030USJmdcYd5HoflDcrDZjC_X1SQqAIbGhN_4WVvfN-vWH6iQL7QNSEqsZAoLkkiqI0hyzUTE71NYMsGnNieMK5b34olu_Etuaf6aedZQTA3rptplDK6KLM3rtolqDtLFyMt-6xkXcrfo5OipgKXJLByFzDCuSN_xsXUPL2Wf6bzeJmTkhPy2EXmlQmvCYtssIWE_J_Hr4coIuz-Fdm7JRrGo5L1C8fxrGM_5VQYrjfv5hLkRIHnrJ6rzDqJo4moRjWgr19Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2k26lAKI2Wnj4f6kw30CiFTTipMEVI9IaV9Pkbp539LACXBKE5zMieT0qtLVM7OiZcOpdCIdUUhp5rlVvZRvS-arSgvbQ--s1Ly3jExFpUOJZBUM03eynzYasbyuzGuUdUZHbdWg-gdsmYCC_LwRhwgEp8DD_dXsFAtrd1HwixVC384SeMnKTBSEULKh8mk0foZk-FZ1EF-WIWD3rOdkjbLVmzcVVtdYyHmS6BRCO_z2aUwVk2C3GHkmecMzIcZ95NGerd7KGp_McJ_8x9vlPULAI9eo0aX2dh4Tv-jFMM5M_yYoQobd5BFGCjBIB-5o1Dhot6koqXxhsV4fbfXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت نقشه راه جامع دسترسی به اینترنت آزاد
🔹
خیلی از دوستان جدیدی که به جمع ما اضافه میشن، همیشه می‌پرسن:
"از کجا باید شروع کنم؟"
و پیدا کردن آموزش مناسب بین ده‌ها ویدیوی یوتیوب کار سختیه.
ما حدود ۲ سال پیش یک صفحه اختصاصی برای حل این مشکل ساختیم، اما امروز این صفحه
یک آپدیت اساسی
دریافت کرد! هم ظاهر سایت کاملاً مدرن و مخصوص موبایل طراحی شده و هم تمام لینک‌ها و آموزش‌های جدید بهش اضافه شدن.
🎯
ویژگی‌های این صفحه:
🔸
دسته‌بندی ۶ گانه:
(از نقطه شروع تا ترفندها و تانل‌ها)
🔹
سطح‌بندی شده:
(مبتدی، متوسط، پیشرفته)
🔸
توضیحات کوتاه:
(توضیح اینکه هر آموزش به چه دردی می‌خوره)
💡
کاربران جدید:
این صفحه بهترین نقطه شروع شماست؛ از بخش اول شروع کنید و قدم به قدم پیش برید.
💡
کاربران قدیمی:
حتماً یه سر به صفحه بزنید، آموزش‌های تخصصی و ابزارهای جدیدی اضافه شده که احتمالاً ندیدید!
🔗
لینک صفحه راهنمای قدم به قدم
🔗
سورس کدهای صفحه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/iaghapour/3062" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKF7cf6oXEQDaag6LRyJICCps0iU1bfSIdOeHgH6fYUFaLd2YdTlsyqx-DFXwVkO9wHiAKq0jeB0TZftSXFaeEihWcseY5AWqfGjxIIxRZiJyezrklKyhd75UJEtBpqZlQkYydU68L1zovW-FKvmWvBYb6o-HA9FnPtVyA0fnyE32yIGFr6_XVGbQmmxMWNTnKZc1RwCSlPuQc_-kTq6-vvvhgWn59bs6sCuQ6IEo-Pt1kpmYNsuuDZpES3T9NGetRGoY8MLptrE99NZkXvh_Gv0czqGwWbvdDj-x3QJ4M9QyBVW7_pyp0CVH5OUhH3g_VrLcipMag0U3fQZUQpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
بروزرسانی مهم: لیست جامع آموزش‌ها و ابزارها آپدیت شد!
اگر اخیراً به کانال اضافه شدید یا احساس می‌کنید حجم مطالب بالاست و سردرگم شدید، این پیام مخصوص شماست.
لیست راهنمای کانال با اضافه شدن آموزش‌های جدید و متدهای کاربردی به‌روز شد. این فهرست یک مسیر دسته‌بندی‌شده از تمام ابزارها، ترفندها و آموزش‌های تخصصی است.
🧭
پیشنهاد ویژه به افراد مبتدی و اعضای تازه‌وارد:
حتماً با
«بخش اول»
آغاز کنید تا قبل از هر اقدام فنی، مفاهیم پایه و نقشه راه را یاد بگیرید.
📌
لیست کامل در بالای کانال پین شده است؛
پیشنهاد می‌کنیم آن را ذخیره کنید تا در مواقع اختلال اینترنت همیشه در دسترستان باشد.
🔗
برای مشاهده لیست اینجا کلیک کنید
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3060" target="_blank">📅 14:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3058">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgGlXDy2yVAiX8tGHNXvLwoZwLM_Ck4ZgwhLf3x3jBrm1oRjuczenoYEqYl4lTp93VhyRQKRlR3Zsbh1-l_x20FL8Ld_nVboW0Z730hzzFusUM56e4ZwUqR_NanEtiBGOxB5jQphcEBVh6sHy_wzGpabVfjYGXgf-R0nGBsvP1QNUYsLYbdWbM8xzIeq4fiZNcnppIC63Nf4nl3KCJy9_24dIV9Xd2tt9H-FcalAtMHRUXC-PNYqKS6-eYYZvpv3GzPfgewNBIpHx8RlXXgoeM57WnicYVmEjrdin_hVfEnKbWPGspvD0Txt0wCficc5xkk2dowxvOb641v7D8WRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
رفقا یه نکته خیلی مهم درباره کامنت‌های یوتیوب، مخصوصاً وقتایی که قرعه‌کشی یا چالشی داریم:
🔹
خیلی وقتا پیش میاد که شما کامنت می‌ذارید، ولی یوتیوب اصلاً اون رو توی بخش عمومی نشون نمیده و مستقیم می‌فرستدش تو قسمت «بررسی دستی» (Held for review). حالا علتش چیه؟
۱.
کامنت گذاشتن در ثانیه‌های اول:
تا ویدیو پلی میشه سریع کامنت نذارید. یوتیوب به این حرکت شک می‌کنه و فکر می‌کنه ربات هستید. بذارید حداقل دو سه دقیقه از ویدیو بگذره و بعد نظرتون رو بنویسید.
۲.
کامنت‌های بی‌محتوا و تک‌کلمه‌ای:
متن‌هایی که شبیه اسپم هستن سریع فیلتر میشن. مثلاً طرف فقط نوشته «کامنت» یا یه ایموجی خالی و چند تا حرف بی‌معنی فرستاده. سعی کنید یه جمله معنادار یا نظرتون درباره ویدیو رو بنویسید.
راستش منم سیستمم طوری نیست که مدام بخش تایید دستی رو چک کنم و خیلی وقتا یادم میره؛ همین باعث میشه پیام‌هاتون یا خیلی دیر تایید بشه یا اصلاً به قرعه‌کشی نرسه. پس حتماً این دو تا مورد رو رعایت کنید. دم همه‌تون گرم!
👌🏻</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/3058" target="_blank">📅 20:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2lfcjKzZqR6uQCsMqakcXx6zwHj4_TY_vGT_DEO_Jy9uREepnCQGTySB4Uc-Lg2wSQLBmIASxC05BhJBXjX2V3h57vFLuIIDbt8lCYc1frv5odesVTYhrcj9cD-FHYWok0ZS0Qe05UXej2KhA39MzXaOosWipdf5R6QTbrD0Vbk9vYuW2dbisQB2wEf-TjfOPdbUtR5BV5_d__OnY55aOMarNkTXM-xl_3Tu2-s8KEorq1YqLcpfVophADo7WguhFrT-KMh9g0V46FWs34KpMGqQ5YsrHBwWMcugUBlSHK0xvi5XRz5bdDSEt468ZwmiXEFVPIdgp1HfUPQciP64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuzfhFmT66-1nNIaxHl_xKVYQzDiSZNMrg44voYXY5s-CTKwrshGsEHKs-or8WMVRQib6FcckpZ_EVe_qmoNBTpgboai7X0DtzKBxZi39lfWE17WCnR7EevXsBrGMkbgu6jZmolFfYBeir0wBURbng2OEoC9kq8Sj-NvumC3XtC2f9gf-uxKQkemvJ-j4Kdeh5yWi9YvnQaIOhnq5ysycyZu3gt2NjT-gGeTwZNkuvMcfCPaaABUs4QH4gzZl6TUqZVkTXLsiMs-1oqiCJ5WIM227vratXXbtPB3_jeRTn3eOynD2eagj1puR6GElda3RnqfaeAD5wp1akyOVi3ePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-e9DSGw41HGMgrA47En6ODllvPecq40Y9UamCA3lP17-jHGsK7mBIDVqFvcUXEptT-ueHoOXe2km__C3qNfDEVLq2621ZTlfkHAaOPTE8njBSKUeoZh-nrJqT1sRZIAtkptAozo7NlbWk8HivXTFF-96cWQdXcvItCn8Fr-UWgrIUivFmf79yl0wUHtUyPuw68u-82O_cctsAZewKwrE1bbkqdsiQ0Q5IoKbQx7-A0DVIpGlEGAPLLPPEnl6FPJlMejJL2Fc52Kujlr7HhP8_96dVv-1TVwT9fOUlrezPNrxIuz3E9C-HVoTTOycgFuyih91LoHVvNw1m9gewHYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی جعبه‌ابزار کاربردی مدیران سرور و دواپس
یک ابزار تحت وب و رایگان که تمام کانفیگ‌های کاربردی لینوکس را به‌صورت بهینه و استاندارد تولید می‌کند:
🔹
ستاپ اولیه سرور:
تولید اسکریپت شل برای امن‌سازی SSH، فعال‌سازی BBRv1/v3، فایروال، Fail2ban و نصب داکر.
🔸
تیونینگ TCP/IP و کرنل:
تنظیم بهینه
sysctl.conf
متناسب با رم و پهنای باند سرور، کاهش پکت‌لاس و بافربلوت.
🔹
کانفیگ Nginx:
ساخت پروکسی معکوس با TLS 1.3، پروتکل HTTP/3، سوکت و هدرهای امنیتی.
🔹
فایروال و روتینگ:
ساب‌نت ماشین، پورت فورواردینگ (NAT)، رفع تداخل داکر و خروجی مستقیم برای iptables و nftables.
🌐
آدرس وب‌سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/3052" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcLe5_YHY_DxrB3ibNrun_KDj7_ma7c9JTVXl6TRF4oXofI0sFvmuNNdnrEANU_jHNyX2DoRzp9dcl9nGmImtbWyB18WkFxMxsHHL1Y19RykWWcwtl7Fh13Mbk6TMnkVtYXAVMVnzOUBaSFVuabk-em__cxa5rWipdgpWoPI4VDEdwWCslWNr3jopKewQlQjbDSXT82KlvXMUCDUYYzC1b4FUdWeTOTJ1kwfXv8TT6OEF3f3HWymeG6z5puGfwHmXRHLRYNZewOT7WuIv7Y_DVbL-Rlp9A7VvQpyQwiv8xV0kcKvDibuQiJtjL4lha06lfRFQAF4dzFZ9ltB_9Thkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTP_vVAUwWOrjyptIqQOouYr_9uVF1CuUajZujrto9fPaYwBMcWXJYTWMAEbgSVDHI8akIhspdmahIzGWpQZRcDgcWmp2IO2wxQFAsU4nbgUftvcx8cUlWjTyfiuqim1RnEuwoVmoeSZ0YxzL41CrCMk92ZkyFpSeWEmu4W_OU5sR7PYTXtmgyy7TlBRFuoW1YycJhex2DISt5yuV8nx1EYmIn647Iiqhm7_AWIda1U62sDY40VSQebEXw0xn9i560teaVelNzjb2ak0-R7agImnCBaC2Yzq9Ybh9Uj7FSDBg82GLmOOkej44DKvIx7WVOrwVhBkzAnKUSUWlceHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB43cPvOqHCrwMECJEEqGknAzb3cg2iLOeo_fl80yNsKzCvZwlXWa5fyjsaZ4zv2Q0LwxPS_f4K-LcHq53B0_ILDfE045cEVyl172yCwMRIMOzM8FVKbDKXynMY9rm5qDBdCp-4naeFoajcPcKSolKzU_--InA-AcS8N2sCKbU9RAAWwdvXYHbGz2hHWvbDyqNySPmr-bLqKwLIbT5o9hpgpzP1ZZerkAN8EIDM3O782nvm91LWbJwNnklc45yjgcdTcwR09UbUnG4EZPpRIdD_NoR1o-fohRVWGO-MaW5RpoFCYAuE-iUYJ_-CJDCoZU56UB2oSb7tCwBnQpXPCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=CXPtL6Mqnjv8fqgEyTcnoiuYeMVAxCTFn73Cu42b_p5410TSUFtUZLlxgWV4V1zbiGwYntJMvJiLrLdmC5_04QhVgPx9fhSNDGrePseaLRGpUH1w0Fe3qRNew4iN1NyidL4TJTYyxQ8Lc8cRi0pVdtHBsTps3kjc75FuxokayzHd3ZbLjVDn5d32Abqjw4foiUx6kSeMbR9dkKLjohHdEjqikTlMy8j6-1QSeBVzMRbZ_66x8OCOCiPWt6MHSG8vhqByxH-NdOvIs8CnTi14m1mXlRvhIOMI-DtFA6gCwRYUY5k0CXoQVWUjxjuFWPnYNxLO9hYllQsje_X8-CIS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=CXPtL6Mqnjv8fqgEyTcnoiuYeMVAxCTFn73Cu42b_p5410TSUFtUZLlxgWV4V1zbiGwYntJMvJiLrLdmC5_04QhVgPx9fhSNDGrePseaLRGpUH1w0Fe3qRNew4iN1NyidL4TJTYyxQ8Lc8cRi0pVdtHBsTps3kjc75FuxokayzHd3ZbLjVDn5d32Abqjw4foiUx6kSeMbR9dkKLjohHdEjqikTlMy8j6-1QSeBVzMRbZ_66x8OCOCiPWt6MHSG8vhqByxH-NdOvIs8CnTi14m1mXlRvhIOMI-DtFA6gCwRYUY5k0CXoQVWUjxjuFWPnYNxLO9hYllQsje_X8-CIS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK6s4j7_Qn3p4DVtEzYHsnpZLHgvgslnpeOBiUhuoE8rAX3H9n-g9O1qFnfM29z9OWmcjgzA0VgUsSK2bgTtFAupCFkApxFVazT2yqPd0i9GIkEnVeGX20aYxXHprwNA36n9gpbLnLCdeyfSTherOQGuH1Vm9ugs_De497JVK12_cZsf1h15IaekY1DMdGL9Io3Ud5ylerlgrbpJTeB9t9y6AlqyUmOlLkqBcQIQJlMOJIa2NhUrdq_JoixWltr7gwyNQWRf78nk-pRTeWljkovZJi2D1b5aGAYHot1tQwiqwIiI_l9WeXQdZkVQKI3yDoh67k81pVEWraNB_EMQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoVZi9puS_u_Ub2SvgKxQr4CNDEOORa15FXmT3Q3c7OyzkK3O9qN0p6G3sysAwAq410MXkpLaw0lZLzihm0lkVSWtvFDE2qWRz5yrVyhDEfUcUkWAkZDEo5O3b7gjcvTXv1L0jemZtk4JYRVIBZENOjYR5EYz7j3NVSFZ3oVritSG4vUzEDDEuFQL65CJI-s0GeDK-GK9axRahLOgxKwy1ZUmry7W09yazB7tGx7f5p2r-I_D1LF8peelxn8OBrnOLM3EmC8aw8OzKeSeOdwNA0pZgMnIx2PCQ7nBLpXROwGApa2hwJuGzuq3FY7fGXYgstr1n_oi9p_d2EOZL26QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d98rhJ9qxU6g7ZO7M9d_VTAmE72GHHMBqO4v2PTMZNGGQsUWcRMIxsquIFNJ6P-F4BJdb1kBLx90k1SsRd6voWtcmTldax5cYLXPHw88-nrkfG6JgGcRiOyojM8znKybfyliWPyvBaFibbVFzm-xgk79ANs1CtwvgjykFRHl5Vj4xRIAeOd6wOmsCl3yFypOKSElHojhrEKN6UpmpYjr_NUJrJIQq8P7ucclA7o_NyegPmrkaSaetAhSt3HtYeS_JH2eQb5il-xkAUVrypUGsv5hcUzcTreQR2Kz-OUKKsafbriYVBzeqTsCbOZPaXeIEfgf_h9CmnTbrN1UnATHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t46E_sQSuRWiccvgUNzcOMh_IH-EF4Jqq_qi_KK5vpl90J6-ZB4iV0rZL8jSwS-TNiCkz3E4g-Z8jjtpzDlZBSUZrN-2GXYnFt_yHIUWAZMt35ACaKbkirz_SVZKnRl4YpnB2oOOqwETpgbt4ogQ69FZeMwGLySCq55S4zRCKeb5V4YlDG-AjSouMIgiJmHnloeAb66jJ3NEnqGIq8lmf5e9Nwvp5ghSHQ35nRTJJEib4rKzyv0Pc7rbVVm5Wpz6UfKrLHESGE1BdzigKqIrVDHw6bh3hf0B1hr3TWmTIM3VUOaAwAVRbRFDJ7l1qzb4brLobp9xZg7hzONdNzK2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB9KHl6KdrYRCfjdu0GoORah8r_Gk3wUMq5W45OeBEY9Z8z5wYwosewnb5Kk_aTBiuQWYByyth6Okdim7wOYRvmoXAVUMnQQ9XRggJa6EIeGn_PQepMJDCYXVF4DEMlicbeRbRpr_m6wh-WXy7_AhiZedQn-vs55KlgPCYyM-qKpUcPifQ2ffFdUwILNj3tZvYX097m2YpbEP-iDnr8Sc19BqCa6E7MXStq0Xf8BTBnayJx0hmDZvFuLaXQt3ep3OokM8xK66zlZ3JRzChu2MrlIPU5OgeBv_pUwTNq-5chd7hxGiQEZ3wGkt97Uajw1R_9nB1bNN-2_Ea0fXUei5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coLe0u-8tdAX6xSAhaRLk_WPt5qZm4zLKST5agWqx3TCILKQr2bBV4J5R9byx4pAaTTdlTb2WZZeZQWLyqOa1wIlP8bjGQL4t6dPcdr-UM8nYOkNEpHoyKcjmygxDBQHI5mkRIGV6USNvR-tROEaqkjs8BTiHNjbekMRRz0xAIYs7pvM1r7gAE9Q79NKHwl_3-BUMRCS381tJJ627pReT0y_wxLm1dYjrvFQi82uB-8YJ6h8mb0bMWb29fQ7MLAPfUaYnG36Lzsj-zSM-btznalHl8gelVmCd-cpVjosw8sx4SIcaaYCb8mxUbNNzvskK2foBkV5m6Hz9qRKb1BMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDfoW4OgUuyd1GM228s9LqxS4BUnCGRsYcyHFSJJ256R5LjyjGzn0GwXZTQAyD-BFrtih_7S3gi-_jk1X8L8nux6Q7nKnq6RaPxcyEf5wTCZ8LouJ-9nEBoyNNqvQ9R3827XtpKQwzxnjL1Gw0J8rQPOkTxtRiWaQSw-AHJncVx537JSByrSjkMbPsrte02lFVyK5gkA701F46PvMZUhSx5XpvPmgp2xRMajIGSzeUkZEbDiG4Giw0Z-TfWvsepJAk7EqnA4iyEKDKqWgKRKB-1XkFR05W2HmklY2DjYuNWWIwzSJM41OVpkYCO_FmQM1ViPxcUW4oK0vmJ7xbomIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1iQAPGnQp-TZFj-cBqccbhVYfBZvUajHTI67aFmdV-m843bIH4dS_W3x_NkT8JaRf6VrlJmMnGQP7l9PkX3Ym-CUUhR8n0KiIRPUJAv5xs7muCrkzXep7lelXnN__v00HuFXnkdrXKWmiK_kt_ob2mGjiyCL1oSFbUpkTzL97rfJ4gtKFiy3OrKFQwekQZ458oqb2wSGNS_plVVcZCD8eCQC4uQB1VQYVlip7OMgmC7mrIbG8rRG4CUT-RKGY73UmJ88zPoMU8NoWL3oc3nV1nkrWRoupjeLjJaBE7Jk3EWbhdpvO3va-iXZgOpT0fgY9VxB-zZxcCavGNDRXbFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwL6yxgCZJWVkGrw8bT1frTSTxdhqs9RrWEceuQmmDTwTwYW5Dy-QRxWgkSz33SAkEXQsFVcIiXs7A2rErnbcTHycqPUK9NPp107NR6ig2EZMVDgIdMUBY6LZa9eb60IFWQljxnWP1w2_wKE3szzAIzzJmLKuGUvVF5QHq2UgOAe4fPjYHTwA15TwxPh3aR2OMoNGWIUGD8O6dAwJly0m-kejCBX6m4MuNJBOtS6VEBY9hSJfMqcCuU2-Y4WtKsMzLcwaH1KICXw6ITi_-nrQ21FoeebjsImCfTWnCeWNMdgz_rKxgqim8FS8gRT3q9ElY-JIuLjgRctFJGZ602hJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQOPbmRbE7lMU6bW8gACjPjTsa20K__jVHE5BkQP2ilgYmVEWAwLLXfUCnEEQgYIS1YqMQm1fV0I2TDNagOkhgvGF-paoFzxPWIWOp5J_wG7wauOolEylufkuiNKZ_o4wiOS3IWQN_giFKazGBlkcBYFC6B1nV9RAUwqAEI9oEWQKogU9CygFNg9M81oIfvka6MjtwFStmtoUEOptnBW8SsZVZLkb_ROiTt3nkQKrW4V7xohJ8-_z6FDWysk-EQs-nXRFYdYh7GkqXLG77PTWuaUmZhxLw6FXYYi2JHATq3hvI7A7k7grPt3qrqw7Ww_3SNnmEMUhcD-E1byPlqFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=ROdM4Uwq4LBl5ZNjvddM6KBva5rmXaSRYOy2EaUc_CUQaxgvM1d88RpYpz2tEeOTOhpAlsBsIM0h63QIPsZUyyCH8jS1hj5FxI7EW0qCmqJSeXlb3yZzTPq3TBgdL-J6rqlgedE57ie4esYJRhFTvyDVpF0P4YnTlwfD2tsbTDeofltxooaU4cHrTwLVNy0pA0AVoYD8g8t_-MzRoQUWiQTZq6BxqNDTlxoDEnwgbEnQK7xqucK0NmmbUczFFweeNim7CXYPqPllCcVkq6bvkEl9I7SCphv59RkAE0U3DwSF47bANB6si3BclDiGQNg_rxq7v8A_rEuCz8gaUmWlUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=ROdM4Uwq4LBl5ZNjvddM6KBva5rmXaSRYOy2EaUc_CUQaxgvM1d88RpYpz2tEeOTOhpAlsBsIM0h63QIPsZUyyCH8jS1hj5FxI7EW0qCmqJSeXlb3yZzTPq3TBgdL-J6rqlgedE57ie4esYJRhFTvyDVpF0P4YnTlwfD2tsbTDeofltxooaU4cHrTwLVNy0pA0AVoYD8g8t_-MzRoQUWiQTZq6BxqNDTlxoDEnwgbEnQK7xqucK0NmmbUczFFweeNim7CXYPqPllCcVkq6bvkEl9I7SCphv59RkAE0U3DwSF47bANB6si3BclDiGQNg_rxq7v8A_rEuCz8gaUmWlUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTVU3zP9UZkWLvIHc0jQhrSmpRivH08qc8N6q5EToqthWhCvmVLoZCp46ENWQZh-gWVNPAYX_WBKDHdEFYKuuyNS0XUL0BDo--5PoMaWbRS-WiBM8TNoMxrNqsgrK_uefpxnzNZ_XUZ6AzGBLDvCBUkJmcdKDeXPSAhFDlBU7slIhXwllPpn8Y-N2uU5mTuyvv6_NCOs3sLNmeApFFu6Mv6sYjfEmaCILl7JjkXPdsmTGXIzEHkbcW3zE63SLCyyWYubAQzne7kUKl3GWDFrDSTRikiDcwL908_ie2gu05fz8RzpVW-zhve4_Iq5VFkG471Z5mdKHL8ArhOcDzgb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNqpYcqt6jqFqyBZfYMRzIHnRpjpdQkTQzK36ne_YILrHzPr5wfMBOVlpIbuE2aAJJv8e5HEY5BQBO93Pao3DHT-HQRw7FwvpQJOZ2Q9HLHRgipiVMBVgqGnVUJG6HbXlzM-_t-vLnih8G8oiroc_rOzoC-xk5655bXvAvEbyRd1OcnzWhCNiNvXWUOiSVGWXVI8N4BV2s8aBvRTk07KdkrVQ-k-iNuNwM0QP2t6V617FJDu3IKs5Y23x34yMoYSaWAU6xBPkAJn1NQN2l3YFfWYqC-i-cA-J-Rp4jH7OG1mXZqrA1PQXiUYqNo7BKEtQDr9VSu4myYC7X2lPmGQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4IN5H5oOK2mvdSHY1VQl0ScRR_J8aWjPkKKk-0SsIV39c6td2rnvg3zT2BiqkCCJi9tLaM8xRDS-fl3YOviOgAiR4mcTKgRJOEnEFhw_SYcSQoVVs_3AsILZ9vN-AWCI_ptNmytoiTJRg4jz8u7hc3jtNWDJzJDtukqIeceJDzN40sFq4ywntcPMaLRCCqenwS7iFbA2zp5zNrzI2IaeB8ryQXJzcrTh0FrmK9P6wLpQzVGGUioU5vt7RVEg4S2itnLd2rn-pO4LZweNPCtnyad0z_3H9qgSl45wXx4S1JwpRRaWWfVgItv_09ie9HMF7g2IaPUo_2D11FbjuviHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlbISBdJUikaMt5n5dSV0p92rkxGe0r2JeIm590LPBMR4Zu2W6iwDP0y-7vK4KgWj8TmuFy7xnTt8o1Q2pPcgKvIF6fLhoKXLjW9sfB2dniqdsZKHP3uwgInAvQBNXILAX1v4jK49YjNRD0LDHENRm6TLmg9Bdqsf0PXfIqc-6IP33yCFuBg8vmx5K9TwxGhfv-h7-QYGE8OH2gQ0HZTG8MFhbXb_XMylFGxOMayQfMg0sPBIxt2WGD-Iha3nEbmkipcpdHrkRzgjzR3_m64sSmunhKMkiOEZaBJQjUw2AN40MIPuqOjicWOFyv-KYaP49rXN-uHV4yBlh-BmaFC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZmmoxrU0HXc69E82Cqn9d2ZlnBZwo4aAL1gbivpP3Vo5aBdPCCvT_DBYYTuYQBfiyCP5HksLUyugGNSwwCVvwYV5sW2BT-axQfJGHbrJjxC5pNC0HgD54rkpScbl_DheRBBcFM6-esaQgl2IWki09OZUcCNYPmbyxuxo6lFYc5ffPjTN1MhHwL69A2rqhNEzJZc0Bg0_P42qAHERKFAAyeDJ_EJ2EhgkVlDj1JDNB5_SvzPlgrQSOMJV_pME9HIH-YiuK6PzkqkhXI0ZGZ2R4F72ldEn05EGPWpzmppk9ysBQKYcHeJsp_0hZCxO8d7CjvQqZQaSoQJIgfwIAE4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ4ecvqb2wcYAQGXkASsJ360iXJnxAq-K2QZqcxRkyLoCjInUgBMxox2Ew3VuGRXXtAxKgLl2x1I7GJOPhqSQhRi5cTnflxTXHUy3m9sUbMRYxt3fmRTiup-3ex7r5bGi_o6SOq0qzW0yZ5R8CK8bxta5W-kzbJiS31-tY5Fl6rwyItf386dJFBJ5Q0_58ssjL-3IxcS1A-AiqNZ47BjXkD7IkTljzd69e__gJyP-Ldqz06DAZ1cncJaaYLlcfrzM58gCKD6ZShBnaIavIs9BifPUh0xVKSazy3HLo0m9nAdZeN5aozV1jm0OTwRaI9gQNIumsV6SQ0Kp6GgV1i7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Udh2Lr9mucAqRhUpnDTptYhevnhpd0t75aym3Jite0YlY2or70IrVpQ7ne1yB3pgIvPd39p_Kvct_EF7SSBx1wB3dZ9XXNMBE7OaFGq5yNb3tqlUbpjDBdyqdxyQzQtzJ98PxFX0KiJ2BKjb7-Ed1GICUBG-B28FEVO0CKqA94850Lmu-Z8M7ApvxsIjtj4arPvwi86dC9D8Ix5J7hryqqv3KBzl0bvUO7B3xGkwvEZaeNlse9yyxmd3JXglXtCEf1gK9slpqt_UwvRYA8J35N6Di8_yZv43e-GMM1s--LvO-pdJM0yO7WZ-1Xj-T711x4cNVLFcepAjokWD2s41KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=Udh2Lr9mucAqRhUpnDTptYhevnhpd0t75aym3Jite0YlY2or70IrVpQ7ne1yB3pgIvPd39p_Kvct_EF7SSBx1wB3dZ9XXNMBE7OaFGq5yNb3tqlUbpjDBdyqdxyQzQtzJ98PxFX0KiJ2BKjb7-Ed1GICUBG-B28FEVO0CKqA94850Lmu-Z8M7ApvxsIjtj4arPvwi86dC9D8Ix5J7hryqqv3KBzl0bvUO7B3xGkwvEZaeNlse9yyxmd3JXglXtCEf1gK9slpqt_UwvRYA8J35N6Di8_yZv43e-GMM1s--LvO-pdJM0yO7WZ-1Xj-T711x4cNVLFcepAjokWD2s41KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0JGwj4W30ThjRwXenZExzl0U6sq1g5sAmhp9mwLQnkd2KzQScQb_N5oOh7mtPNymxPThTeTWBH4fyBzW0m73aO0N-8IlMqeaD_DJGoUTzo6a8caE03JG3E8tL4Zq3vRVLNql2Y1Hd6zP0h4EyH_YUuEdb6G3k7aZYv5w0lsNiqJ6LMfEQQs2BXELNVgWiY7QPl7LQAKoWpdo2mhMM7ZDZX3hfx7ISe4l5q7BeoxRK_Q_W8ctLJbd_RWdV3TQhAnjPEbPLeFaeHHqxO2UeaAijmx0RLjJECjfRTS4qVkSITUn2r4l-qHTS0Nr9fGoX0zTFC7c3dJ9BrC1V5HGYtg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhYWgZ9NtQ0Nk4j9XIzp7zYGOWgu7Q2DxygsREAkEBFvuDabjcqFLGH7J3L-JNAVkBL5r8EFcUbtnuLqgLeWN6ge0dafSKPidd4k_PdyM7t_4QjxMaxkf6GZHDvTBR5jItNmf1s64ahqdJh9vfT-nvH-WUsuYBAdgjMl518yyqvx4kJ4oYk3toeVkQzrkFqPRwl6vpGOu6s69ZTXc7dM5stqixIrYaKWAlqb4ct-4jp5JJPvGwvPJdROgSJ7moOWt4knllI0o0rtspS5Y4RExiSoEBjsZxIgaiGi5eUWa9ViPWv7fKI-UFQWYY5eOfYnMq1o6yz_n7xytAHIUD2w2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3pGGjEFkhiFrT0SEIUMqmgZGskGBCamDKS_jqtGYdV--xWEzLW5EEKbE55DJwOqNUxC6QefSO3M2rLqwdJGK9vG7PhadPaUEWIoFrGiZsxO0LUWLHEp_PGmvBeZ7CRICJGN58eongw6xtJ8uZqp06SQ3-6quSelThKFjGxfZspmPhOMJmAiAp15EKksCaTOVy1MCNP4kvR0RuyQxEfVM7qR5oE4nV5MU_7QhC8IXBGwmVBVw2Cqgm--ffl3SqwUAu9RaTYvnQ7sfG3BCj9IqliBlZCNSvZwddBtnBLJ6XA5jt2juUIOg_8iE-_aiRn-rN7btvy2NOzCqi476caIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3eOwACtUI4eMPy_Drgw7HFLloqRnmpqKUZWg2wJCbJ4GxycOnBa_35hf3-syXN7kdfnIvE4hWc057-r8DvZB971rp4R9CAa95rZtffcPZ5RHM-uWMXLUr01123qcy7sdZH5ehI24jdd39ooF5UjuqDvDFX2roOn2PrG2hcUNcmRwMpdG3YIMz5reusEmxEmXF25kgCDTktUTUB5AZNexbgZ_LAZXq8vFK7CA8gsRuh2j_HTaXaQeKqFhlTE0I-rb3mpQkCFbX77IaAWzRp2OwSCdxoNwOCLnRmcKptusPZBmlV64_dpI-Z5Kpe8i0G29cgUhI80Ah4IbUjgz2-8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vytz0K9iXFUqpGUHUfzGLZFHEzg5Zb24LrzUCqNnYO08lVjc269C2bHBU1g3lP8d_b39OUm5_EphQvy7hloVSZINuS6822hcTp-XI0tIw2Zne6OwX3EXQm4XSgsI75kfgIhMcJqznGbLzcSCArqcOtXCX5zpG470VjtA7NWGnIW-kBaY7N2cSElOC4K-DZqfNaToR4tOK-78VYXyWIIyApH3L1RUW7XQhcU-FP4DjAritcx5GAn8xAfgUiqF0uJhwR7HNQSoG6TbB3py4LjS-w8VzkHzq4kj6Q5opTVAm2fZFKgCl1wOG7A323n4a55ht9FAZ-96j8xmLY1ETEpzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3ysGhWTkuUDTcaMbt5i3YBozltYsAwHK7aSAW-DrF7eZsXqfhd54vTKefK_EHofavv0aGyk4jzCRVsTivpaWfP3Oz2JtzQBWiwWj4X_OKnR8-oLLM2Ryr5ulgSpsqmt1EfhNrH9BObw4P6zBeqTb_R3M3B9HV-KPYt84NCasm452TTWWyBcBSXvrtkIYkcVPdOAJpWw11sIP8XOfh4px3V7TpnDTLVvFCu03n-pmzpeIH_ufVY4mcAInRN_mL7CPTILKWWDoUs6pqa_EdFZE3LgMuxb7LVur7hBlg1tU6srEmBVe8Y7ewIHtLGoV-Z9JTxXhDBNLlKo4-ZwSGAXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmWO8UhFF7mDfIM88_hGHP5Daf2VFop5JUdxgWYMYlQW9-xKcoY1IGbw5Frw1LggSkNBnVkyaQTKLyYoi_6b-D9BsSouuHvBsVNLG017RHsQjbMK8YfUgJDhIxphdtEdwo7QPd2R7xWUH2-kC6TGmJe0jA_vxLvCumE7dlQh4nZ-dZCsaRazRcDiU9E6yw_sAHJY31qbxHZr-iDuGUGPAEMxn0QcVZ0PHGxyHJg1XGnBPDZio-V3cgO-yhDoyHj_cDusvPTJThlVyLuHiAfMZmf4UHGc2bT7TE9nQHsgnB2vGNn-dLpQ_4gqYUqndSEblXiFYblO1sd6sOjhs2591g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mhn1A2omDpbJ1DJLCUOu966diIaEHdHm5PC8z-6sSfMzKrN7q73f0mCvLS1cSVj-3f6CYPRB2Cq32684CTNxnAv75tLl1jCVAZcZ3a5xrCJQJF21lkZcj80MEkXnDfMbgBDgYURz4Yfi8KZBonkf4hOvLAzcMqg14DurESXG2PHHCunrN2iDKe9WT4nxdgpRBtPD8ZY-A0XQ_9BWPKqGJY_SRt6tislGW4o7e3_BB1goi3PMMchEn0zqHA_TohiqxSR1Rt_e40xBMwlo7-fvrGZRtdx_Ts0ueOev1wktYiC8wPEphbCTiHYDS19B6pcwDviYrup2A3LChHlOtM2UVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=mhn1A2omDpbJ1DJLCUOu966diIaEHdHm5PC8z-6sSfMzKrN7q73f0mCvLS1cSVj-3f6CYPRB2Cq32684CTNxnAv75tLl1jCVAZcZ3a5xrCJQJF21lkZcj80MEkXnDfMbgBDgYURz4Yfi8KZBonkf4hOvLAzcMqg14DurESXG2PHHCunrN2iDKe9WT4nxdgpRBtPD8ZY-A0XQ_9BWPKqGJY_SRt6tislGW4o7e3_BB1goi3PMMchEn0zqHA_TohiqxSR1Rt_e40xBMwlo7-fvrGZRtdx_Ts0ueOev1wktYiC8wPEphbCTiHYDS19B6pcwDviYrup2A3LChHlOtM2UVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mddkvhqUp9DBm7u1d9jt5DIf9TepotSaM5qVRubqDCHnNqO6e7LMOqiHFs9augtvV-dyGWZgyIKqv4j-KNxIaLL-6gUJLwAc6LOqQk7Xcx6KMrVWNsWXbH93Nonw9EbHPpF3Md_lkSgPOlicWeMYmMfTFsd8JOfngA6TJNp-eaJSrdBx6VguTE6vD7aFVhZ_mnBDqH2G3NJ7LKN3HiRE77nuVsBCq6PrW2EbKU8ip7mWw1xdR0LgDC4eq5v0fD1ZmmYGQlhKXFNi01W8cVvxnz1kT0BZOkamUjznckR1kSaiKwCDv8TfRiRtHbEkPcNtSQ9M1GdcS74SqHnYHhXq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=biXoI97rDzU91XiNSKq3JFwmJOZ3TFrMVlHiRdRavnzqtTOUa4VeaNnZHINeSG4KJGHI3QZVkAV_BQ0XpFA0rB__VlUqtfTagSvOIQzp7zXjffzAHpOGf8tmpltOwISEG4gdwhcLRc3k3yk7GEc0OSVJjGDPRoC40VoOic9NS0puwBIAYmhgANgjQF7MoyysHCyVE95YUediQXmvbOHqP8319TvNcQnTTjzrb2sl2n7wXDZGK1ogIa0av07WqA-nb8MlDxKXhOL8oTSflwLLd8bThSsIMfhY4d4VZkO_rq6w178GsEhHafFJm8_KTEgEx86swUzBjJZDf3nF5YIJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=biXoI97rDzU91XiNSKq3JFwmJOZ3TFrMVlHiRdRavnzqtTOUa4VeaNnZHINeSG4KJGHI3QZVkAV_BQ0XpFA0rB__VlUqtfTagSvOIQzp7zXjffzAHpOGf8tmpltOwISEG4gdwhcLRc3k3yk7GEc0OSVJjGDPRoC40VoOic9NS0puwBIAYmhgANgjQF7MoyysHCyVE95YUediQXmvbOHqP8319TvNcQnTTjzrb2sl2n7wXDZGK1ogIa0av07WqA-nb8MlDxKXhOL8oTSflwLLd8bThSsIMfhY4d4VZkO_rq6w178GsEhHafFJm8_KTEgEx86swUzBjJZDf3nF5YIJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQYNgQesi91CG5YKqPiCvMwFrCdxHCsMMpGXCpg4ZUF5EyYwPxaQLEc7chRQFv4m41aLDTMMXwXSMAUKagZer_rjARHLiG1o7kV1E6XKfK7COgI5xWLySR_0t_in5MJ-Q0DD_Oxf7zhVu_D-KldiTkamP2QasfpoIY4NO_GYCm3xN7J0CxuCKZDPXIvV0o-STE09Gs_2LRMFMecgxlPzgI4bF1LRE-CdZA32iyoh7zCqmHvgYxAwVxmLYoq2Lv2jZq9inklARpxGartttb1xfCeiBdkZlNVG4dFEmOEHkV3OdIFz6hZu4TvGvzEhum_mcaXkeI-5R2qxXzT5im04ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOSFv5MVZgLXTAJO1UQmEgSRtCbvM8T5ONt7QiPWd26xcqBqfz6KmgZJI3EEun2ZDyPF-s7QT35IamXmh_w0HR5d6LqSWK2-vWRdqR2t1wp99RE2snj8RM0Ec9F-DaD_S6TL-FYmEKq_JhtXNpnRd78BhykS_KUHlavoAqvu5U5UI5Wze_PsdGJ1s3y7u0sUonMHqIULQ0eBpwHBXR47Zypd14wGD2XyCbzjUBxoLrf5Fr54q3nIQGjgGGB0oPYe7OZcU9nFfCG5cYgMr-7eLHynoDt0r3tswMcrCXohXtiA0NJ6gzsCnZFv9Gm_I7i5eRiadGeRMY7P1uYif13FXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBYnTHfkY94kFSAW0vlXfA__9opb6zXYoMWJc_uMciWYP7s_olb-8OYOHrP1xhw6S0Y23x9l6gBKlR32UVspJmCERemFvWVfX_u9lEuED6mYbjcX7SOz8u0w-UGgCdDUsMs2ZYqhmS8DewZyFGQHN-IUWNtEzkl221xLVHNaNyEJ9qDOmsUVeJ958-oqswUziyrtqiJHsUJZlASYZBjqgAlDhx_eQGC8PBbwOAv-Wrk5SBN8SrzZoT9brpiEUzFQg0iZkS7QUAVztxnejR0gXBLesjYRBVxhHkBkpvCs0SNMqxj9uh3vL0kZfevepQDHdrIgMkyxlRm9NvfSTpceKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVFHOppb2J1eX_GcbFFJvfYTKV2o9f3kU0KzUFGGERpTy-e7lfq5XV6l8Ms9iUnVtz_fWRqFL0q6QRDhphIWWhfQIIRfgOfHmPCBndMNt2ObWtJt9FZFZeMk4OJmnaCZ3qJV9KoxWTHTUhn6Pu6Czte-Ohhnb6A3h96ZshdzfjgFwQzDO4jnyLx0tEpxiO_0M5Vo6a3hL93DxsEzIvMklgVP1COyegZyJUsph4348xIyNr7_Lb3fJ6fBD6U4y0vLIQ0Sxr7-H13fx6unqD33-bTN06bUFP6eTwgucddhdt862XjV22Lyp0jg0g5wBZh6UpIgUT1nS7L5u8Ktr86q0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0LIISjq5AAtybvW4YaJUTJ63Yeo2Htz1_z6X8xh3qcDVYEHBrXUeMgvBmdqC6ZAN7XZCOtLopSjfWmBr_Cp7Qk14LrooUhLxeiHXgrWYiBEcEATMqQOukvX_gNvkOyBo2nuzZRI_juxTMBDaXyMvhfO32P2xPtiNkVuCPliLNLIImSRGcedWW7XdoCwB3kxZozps6EMw-2V2AYXOqvayLR9Xb6s7KfrWNOJA24VOdCxmWYlh46P-mH4K-gkcmERg6TM6dbCr3BAZu3xXDUziBWAY9IEbfmsyZUoHCnbDWgu-Gdv3q4CruKBlzgxZf_yUoPEVvUKV97EoueDDqdRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn_DQlEoDjHE53uS_bSDRn3qcWb6YGdAogVSO74U7TVe8JzDdOUtSjnipMCIF1icQsVxaX6C_J1a9vsIyKQkB-VcZY2g7NSYPt3gPMK9_qGMCwX4HJ38ZBjZYsOiXcIr0nnuPs6cGI3ylwYagWq_SGQaQvRK4D5Ghi9xPwgPgltcnnzQuMrCU252qegpUI4-_QmD206feOoLWqv6VrBHLv0Yh2x9ZQwCznsa902XXGUGxkAonWVf4CXFsQ0y4tn_KF38dk5-tyJP3qGKXMbgvmmwYCrjyJx5_jWeSmXnAasU2ZfM_dBfSsFAnf-vm61zeJH96joCd53NN5_thgKctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3Gv0ZOi-cnBLtmb1ilnDV-ocC5XIcznlDCTvLnuZzkbC-a74Sokx9SXmmVOAVh4DTDWpiG4TCd1G1zPF8rPEY_2M8SjrgZHNkQsPZG8mt2exJSkQ8uns771xTIkcrWn5diG4wDhxfJmqMg121alMYrkP4yxnmufAqh2sF0-FR11gJaiQnwPOlP4O7aqu8t1tmIY1AF1DsI-8w65jBoVTcFtRNSVsIYebeOl7PT1EI4KD82oYw0tVlcTIOw4781gWOgqL3-BD6o3MP5YJXenvXFtK6HzjGm49wyrseM3vSPA5dmuoPii8ufOlmgS5iRT-FMHPrm2-nYrgVMD6_qI9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4-NdQ0TrW2x2Ci7suUV7n5aAyKOCsWQaDCWxFh0NH47bWVyX9HX93bGSgtRlBIJavhMZZsTssbcthe4_GAi57S7cmvw8zJ9a6GQqlD3oBVLJMWPM227Xn8wZm4-XE_Mt9weqbL2IU0jMnCffm_rFLwL82ptQ3REUNq519MI6MF3tebJEdu-Bc6Vb3s1-YOImHErtP0ShevZEDEdSHVMzObuDiRSVMCuHrNwLvOo4lc43dald3tW6cN5lYBCaV3X4MaxsdA8h2AV8ffHk7X5A_WlcWpml8MmmbTtQ8a11YKURZpYc70MKmxIp6UlrAbnz26oI2upe-MqaV9ewLhMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=KFgmXuONfAV69WOJHk67qEDS2e-AZxmHr-qP61hK22VvTcHmr5g3YemJZHAsRFft4MlUup3VzDomjtdWEvmdzrNzxT61DTvQxe36ovppo0FjgWMmGysDONWvp0Mgpnqs0XbBSVFIm78LrIoePeJlJOaR9hSuYSzWzO31QQlel1xIsM-M1h6_PKRnTnMNysXnRovz1eqELJtJtt8TkjYKAr7gBaqFYhPbcgeAouYyvefOqrGedoL2P5IH2Mse-qEbyjHRlNNqvcv5OJWQxxe7UkC2lG2TdnRNo9ZQz4AXLLfpba1D1DQEkvg62G73P_tkm7CxZE9687CagCZNuV5olQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=KFgmXuONfAV69WOJHk67qEDS2e-AZxmHr-qP61hK22VvTcHmr5g3YemJZHAsRFft4MlUup3VzDomjtdWEvmdzrNzxT61DTvQxe36ovppo0FjgWMmGysDONWvp0Mgpnqs0XbBSVFIm78LrIoePeJlJOaR9hSuYSzWzO31QQlel1xIsM-M1h6_PKRnTnMNysXnRovz1eqELJtJtt8TkjYKAr7gBaqFYhPbcgeAouYyvefOqrGedoL2P5IH2Mse-qEbyjHRlNNqvcv5OJWQxxe7UkC2lG2TdnRNo9ZQz4AXLLfpba1D1DQEkvg62G73P_tkm7CxZE9687CagCZNuV5olQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km2abPv8e9Cx331wh_YMl9haHv9u4wCpyHWLDcqh3cyT4ApEF4U4irwa2ylXqWVkBoY62E8bb_qHkHvqr5rj-7p0_SmJstMf2onso1LLsNd_oGy59_p18NCMdpRC5Zc_uPdnNTsudIm4ePV2Ui_KUjEfJt9fiBWig9sjUS1hU_EZLDWsWcF85FFa3S032TwP3zKuPUcFX9fHd2wOEx09GbsxZnD1D6az597B_p2rwkjAYWHrqFZH-Z5W_-zh3dTO7JRhmQwPrEw9cJt7gefq7iME-GiNg6feS_OgfdaQCofnH9Cj9EOo1B5TZX-TK_t7GMpyQGU97Y4Bi7_ecruk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_JWxap4nusNI39kG7852jznUNbe_HostiVBeEfVNeUXsG2nFnIj_XsbBi_ZbXqDF0ThDC9eDT41FKgi3edIHLZG0xvu9I7cuvEUYuQT5OLk7y5OBWoLgyZPTihFrPqKeApf9CCIbI4y9eLx0I1mrAW9EYSAaoaxvNp7fKq2IY_w2Tvmt6JghUN8nNhmX0aLVTB3mOEh-XzrBF2j6rqxAyhaMOtJXgIkWwFHSCLRP6v16mXOEL9Mk0mWwPN6R-vyAAK2o2hJLRCjTrLq9cC7ikio_4SjyAP85mbNOBBT7UFiHO0_YPg7jemXNHLI3mm6xdeISe6S-xEUA07F2VeI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFZZBuEdMJjWvfNyIAWR5H3owWsisYzA5dgrM9jlwVGFElGUCH4zz4qf-014VQsydA4VVsmMN_hDuWCrlwqyDaddb0rapbdaOUwAHahXt4fYoYBbtmtEbqSr5K7rgkIKmDV6g-aUKyGM7izEsZrSpbu1LH_T3q2Lj6Z4bhfWu-7SpFrgOprw6M32RbDexoFlCojYjxUWPfwsr2rIRz_MkT_rBeSgsa1xLIu7EY6pPDGN3pI-YNEOExJ0MwF_GCt4Ieg2HniriMMHz9i6k-_DoMly9IXhSTGspnQtqfAguGWrjnzqNYX7g2zFdgsej1W5ax0iF4uiwW-n6EeLGn3aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIIKGE9HPW7JGizeDp9V_D9uBCFW84ut8z_JImTAPZ6c5XUebsy2cvDcpmyV2NdongLT-N7kRYIgltGHZKjVoXXDfKdjjK29g5CNBPiUyLkpv7nfO8BeDYoEVJ2YJOXhUtVVlZkWPAqJTOh5ttXiw1p8e_BrETg0DfUBcXkhDu-Svy0fQXabCZTNe0F3jSUaFpI6NUUEotvtI5lW25VT9KsYUfML3Mf1A2ltrQQzuTLR_EjZJEfGjQJLp8Lr381pkcy0FFaWJoFuenqynCwOr-vsU8bizNMgffq3ci-esjNY0jHYGzAx_FV6dAiWib010tIYCWg5zm5s-T4vker2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=Hiz1LARaNdqFX6dywFB9MrNbwIvOSTxpH5LUvmAayBZoGWs6cFicTbxUWlfgQVMEjhE3BiI6r-MrGiV4pDh2Q0H6wVhMf9MpjGosKo6nCzwCGuINfKewx2A7aeFZuxo5BWtqJON-HkQsas_hLWxFUi1Q3sQRzOcxhYLEczG5tsWAliIJBezZ8oHLqmwgXJkj1xBM2reLKIS6x95pJMFHeMIjCfDz3TwrzX5HAISyH_xF6pFB5eSYDlZhyPkYAdkp58W1unRMqJrvgYYJMtk5sA0HLfv4EMzkjGgzI1zW7UU55nwkkmYJmjSqLrtbq-tKvcVCO060u0OiqpvfWEmqdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=Hiz1LARaNdqFX6dywFB9MrNbwIvOSTxpH5LUvmAayBZoGWs6cFicTbxUWlfgQVMEjhE3BiI6r-MrGiV4pDh2Q0H6wVhMf9MpjGosKo6nCzwCGuINfKewx2A7aeFZuxo5BWtqJON-HkQsas_hLWxFUi1Q3sQRzOcxhYLEczG5tsWAliIJBezZ8oHLqmwgXJkj1xBM2reLKIS6x95pJMFHeMIjCfDz3TwrzX5HAISyH_xF6pFB5eSYDlZhyPkYAdkp58W1unRMqJrvgYYJMtk5sA0HLfv4EMzkjGgzI1zW7UU55nwkkmYJmjSqLrtbq-tKvcVCO060u0OiqpvfWEmqdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOZwwoNT1PPz8BFajh05hwgqUMHnTseNoKTd8iuNPd48YUOyMyFmWKLaBl62xHVqs384ZoOS12XxwZlMPYjzK2PFtr8Co-H3gIQW1fJ2Kj0q32gJ1letOoPsvrXynrDXQNXr1hwMhPUvQLjAjhY61c4car7-oNtdBYLc-JrQg_Gp8F-AmiGE8oVPF4BjLkaOhWYtdIxS-Tlt1c162_Vew8gr-8gQqzYkvj6wJX38FcuJtOv_wCu3t76NqRG4U2ZJQxi4nJ7ZmJziupaL3QbBCxUUZ82Ry-3U40DQFsqUT3kG3v0ZYNbImT20n5fZkwZZeKBXY3UIuVHfuid0UUE6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1ktFkC_Ua7G4YeVDM3Mbxa1KJJ1Uwi0sDycU6_findJvFNbT_be5OVlI_OdrniDWQRV8idmqD3wQuq6EsSOVTRJ1qmQqFpBuVbeRZO_J_qI2hQPXQV7RFKblnJIla0UCIdsKUzWgtrU8zu5LHeVobqpyQ0EkvhMxevPVVlL6hgpwNKGNw8n2P8BIHCYXD1vxjBPG2lH86Lh7wr-2yA7xqDLvMmfVY2JZqPV8QHus1wAS-KFDswDLqLYC9kpI47lHoQfH8Hdgd3LXYfJT3leDIT-F7uaxW_IxaNmLl7sE76wvR6770J0rgIxRRtXVOmezEyZ0sR87_CpamV0-qmE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzqclJ7L4z-EAgCA49jmJkVDNTY_PZWl2gq1jEWTlOUJyMY_J2kup3hC3X7YtHO4ECaijV80RwAEtE4m6RnMkbt3nDGvxtRyfuB1RklzdpIng2yGHDqLvqCZ6MgKiMvgAkFgTEg9DOANxh0mpv-QIyFjMpbqlVjxgsSA5kUjkst1DSHm1GHUy6I68H3tO7pS0ZbCCqIj5PVOpbUsifNRlbpXa8FxbQzlkwN55mr6y4-XdP6wVL0CtcG17zGoU7bAngQ5adPMhUfjUVbHaWQS232uQElQ57CpbprxnRhcS9yKA8V82RKjXGTQ-BmbEpr4HkL11kbtOjZB1pjRRjE6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBK3OMT0kZSOPaOe1k9GRxE18mS5bjxA-I7m4f9-3bgZ6HxZ0jDI_U6M95_IJoSWEFwQ1cEwUrUIj7E-jZIlDEI4nDAzqvxwGJqfEul90mwJ4dzBoKiFIVoAUkWZCokuBjHK1piURvIqgTLotiuLonsSAEyCt2dWbvfjakOCyAB4c76EjXzRqK0OHwL6y5mXNublcdJn7oMxL_0cs-mGaViImjm8VbTya5LXHUc69lLBQQ1GrV0jZ0vjGgR7LC2PtsdbSdUY8qaIfQETuiJsp6c3N2-OoXP2cnzW6qB7exY-i9xdxAo5NxRGZRQbXUyW229TC9zQMqzm-ixdu8FS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUfGWsukvRA7knMyDqqq9MCFdKpyzIpnY9AAPmnUUSCLopVFWv-Yli17UqRD867y2OLcCDdB3FTLa1tDvu3Rb68ElDQvJK03C-_N_ZmklQ7vjgYBpJhzkTlbu-y5unWBYAbgUPT7vFQGgTQysyhKSLNUtgCE9AdZBiPpsyRYMl_kJRwh0ZbUHZNi8UaONU2u-sUgfOsWyLQmlUwiuWZNL71-Ths2bUt8sTpdR3IuGPFkdwXTlkdfKcZS03l9jx-T2mY8UitaF1UlVl3j3L4wE9ln1ijjWK6LdaJuAeplRgJd1MRppZhQQJXo_Dwy1FrW8YA3EVY_h8TW5-1KJnrX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg7R02YT04XGyhtoVtDP2kNWSL_SH0T0t5nGCDTFBxkfno3iuC8tkGz48PLoAycA8TI9UrSpsR-wDFGkEiNPGOOi8af6vGl5Qyc6vQumqmragIQ311T_FI8PvU4ZlER0cOFoI8sfBABrEvhcROA0xtENd1KrbaXLJCL6iPT22iWitvKd2qDkB-3Fq_m0xOqP23eeayzjIa9nkj4y-aienbTiq9wmN3DbOx25EFrgk9kjk6rQPUOb5_9YBvqfW-RQ0pA7_J3WcA-yhebY7Zv023cDbCwNlZvQglnToy5RH4spHHQUTPaMlQmwIk-UoktVDe_UCfbDVpDD6FVcjQVWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=TEzU72GvPqaIhfKBXYjDLhAf2HyxMM5wEqtC1R-3YQW2uyNh0I2JIINYvPCJCT00uoeCZ1i_95PvJ4WJGfMs9ySH1y54xAjGvd_NJXL-y6yRYiy2Etc0v4mCrjEb-D0VZldD4BdGCWJ6uoTIm2UKyl1Vog2UDhPYQUMNRxnpekaRSZL3R_-eWJT68aQH0YfDon-OrOG_mHA1LLSOeXImyRSPLlr4C0J5cGzIo9yJXEqvN_ZppTvznsfOFK9L7YIXwoTA9J9yA6xgRHLVPL2zIiJO7G6Q7e2r1mnO9jQSkYGbdX-aybPfoSt8FlhLtM9qFMk_lf8E-E6JNfJtAI7LMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=TEzU72GvPqaIhfKBXYjDLhAf2HyxMM5wEqtC1R-3YQW2uyNh0I2JIINYvPCJCT00uoeCZ1i_95PvJ4WJGfMs9ySH1y54xAjGvd_NJXL-y6yRYiy2Etc0v4mCrjEb-D0VZldD4BdGCWJ6uoTIm2UKyl1Vog2UDhPYQUMNRxnpekaRSZL3R_-eWJT68aQH0YfDon-OrOG_mHA1LLSOeXImyRSPLlr4C0J5cGzIo9yJXEqvN_ZppTvznsfOFK9L7YIXwoTA9J9yA6xgRHLVPL2zIiJO7G6Q7e2r1mnO9jQSkYGbdX-aybPfoSt8FlhLtM9qFMk_lf8E-E6JNfJtAI7LMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8lgEiSCBeAwdZlKp9tEw1CURXBw0FMn8mlM8-RKFQUfwUEMt-N4zkOihQ41Ev7wxYQTkpaULzT4habgNo49OqtHyDt9nwge3tZABiKnegn3bRtf1llmpTYug8W1qoj0ZKwZFEtBHV_uk6LI3gu75TgeBqm-jYDKNUl8zARQGP6jB8iUZe0dgE5hqCvMP1UMJ78BxGds0l709jm2MfqQ2eAPqOKufpo7cArzi9_orKLWbZYZLLI_FGNZuMhjgT-1xRxMOov5uBHXKPqJRUCQ0vlGggMxFA9z78JVI2u59ZT3JzUVjF8tNvvwsNg6BIK49J1xDwjt4JVqBz18iel92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JblScDdYYxuTAsCMAuyXPY_M-uhJCwB9MP6kEAaVsTcIpBzEW5pYSKz_nykAor6E4KSyCh9Z_C5VcjeYwqH6_YG_aLA28JGvWmXv2yjewrjewLutSfDr2RklbeGvuoplun_obQFkVZx20oA4get9ALZewwNHJbU1-eLMnl4WVhAQnzek5gFWCZrN0WdSvPJ9OCulWMkTaxgXexviKNCiqqQGpRjZMbWPfpe3IoJOvkiBgurVSSzFxNqcCqHJ2L-CR3X4Zo1HHP5o7_b5jjTLT6qSwtLaU71QWJM09Gcft-DDG1xz99LqwhQ5J6dS6iRSUvJPrLK_IJqIyspOERgTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzKN4ccPi3QNq-qp4x89tRKX03LuLvEoTAPU_I_6ZjjCBdycf_YhXaiUsG9hF5ZORPzZAyroOKbUHWUk0DSiUI1hm2F7fRigfWxblWy-jbAZpRw3OXd2ToEW4CS3ygAz3l9VAsHrztUfY9Q_Xmgja7C2huH9p-EGBaneIEDKs1h64R5J4SmxQiZlaqaK7fwArF_88U3ExWLuja8In5jHuvpJUXdVl6O6Of57iYkOJ0xQngKCSnEkIgoZucAS9Y5UBhL1VZM0AawOZln0qBdaTvNRunRLudNL3bHudDCMgLokhczfuRxsQKZx_FQclD_8CG8mzCeIRADEUHYoHTyWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYBF2Vm2E7Qsvdyafaq46OXwsM_KrkR8bInQr8dXlLOjL-jsm2zkrQruo0A13V1zzXs5-yyvJcknHzR-JoDqWH6tkP7zLhOlB240xG6soE_OKt7jlzS-BD4KQKehT12WSSbgHMxWctEAQvQE8iV66TedjXq2XpoaGByoyZbegF5tcHRutkdSfL1pqcExxfzVJP7VJnMNb9C4qAm9i18tRIV_1UG8zp3sGC0HhgbJ6n6Kr2NdZ67D-47WJ9ixbBpcU9BkXJaifu895ShTEj6MVE42Kn5iMMFU4m6y9Id_7ns1_HyRTfGe0wz13POkN0H08VZFiTtIgvY4Db732sLrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9-a68WfqLc-Ya7OSYEJAzCSGpOvdj8bvrAnfJnrJclCm_xluY8-_L1XERP-YqOgxVXp2emTvZP_jTffsj8YbXABJDj3_yc9NlV1KoPe2FcjkM0KJMG5QDGzzZBLcbGE2L16Kb56obnZWC9vK6ejBqDo0tP-4b9IQwiUrY7_xhP7SuKLO-z1cmOZDvp3FRWD8jW9KhIshX0Jfv7GC2knebzqV4hhZHhCi3IrHC88-LOSeo-fJTrv-aMBOCORZlu_sAsL2TKxOVvaZYUKKI5Ba1miA5PieoF4AbrnOMY1wLoINMn5BN7-WE_flwmyl0cUJcLXDqhI-zoIAdAEAd6hSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHTz2fnN6SvlK0oStulvLbFmqfnwbAjzVjORU1pTlscWL2_Tpr_cAr_JKB38osF1VNoReIROi1YQjeZN4Ab0l81elovWVmM38X6LJic_yu5-662gHsJjKRrhndblHxh7H8tv1FpbD2TMTZqD6FoD810qo-6R5B_FQpTcBvHx4IdzHlhrRzPRwX37Wqfxx-gJt4d-NHjIAQfbV0L9lgtd80caZ1e_RLAUyrg6ewkc8aZEN97gTzCDO5vyz-KsFL8OlzmcTqJRXdZMHEpeIZd3gvsP_JljnRvFpuXlwOS_uTFT9I0H353ehp8zMAvecj4R1mynKJP4NaT3smQU_A_Rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdzG81m-tgHtD_UsQbwOYlGn8yBpwjFSHvhXnSyrZGL_u5tmh4mvlr_V0JJihyetSqbcAqBgu17G25qpYjw2bxXNn9Bn59O_1HYui0a3Dd9dhkRtYf-j3TbSkvwL0SVXWH4Qspf0yLuBD5fGZwnRiId8icGStaok1Z3_Le8K5Oqr7wn5j6jWphn8GvmkDCZu9RVh-Mdjr9upTv7zVlJpm6Bsa_EfAYKxEmUyPOyd2jsO4GiJnZ9MirEm5OnNbbOEoJZ_q4XQgwzJUMmjP5oTMb-V4GMfKTJbNYOBV_Gthol29L0XGUQs5GUTcUnat7Y9RPP_2aNXWCXQ-9wQccqiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF86ptlz2ioAfuOYl8cEOElJus9pnfQBdvlG9jzjPXHvqqmn2oDUQswVFw5rYc6WsQ_GK45CAfmtiN93jvByFiRLIpolbiUDoUoDQXmt5ibFNSPQ5OcNa6J9w89Da7N0f2u5nfuMtvyRWafnHQ0ETfDETiI-0R4J3bXF2BvgqpvjeZ8pPCP8ydKYpgUEuKQtUKuR6hVpygDhi7HapZn6gYKhh1K0P-vnFg07wJv7XYHhiptriHUI9R7BuLiLzkUqdbGMIhqHRBEzUwn_A_isg4p0uWPf2hmd_KOv4ElaQpWZoVxizozF9cFqRsL2g0zcMenh4Nq69kBPuXOMkzpoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
