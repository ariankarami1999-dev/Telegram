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
<img src="https://cdn4.telesco.pe/file/p-CxBes0wKK2Jzx-I5r0S20Hk95Rlegb35BQxiJV3sNwdPHLishZazaqBnQ_UMFcP55mOBq1SNvh-QVvENj_Ti5R3NM8I_xbtf9O4y050RahPmCtySIk9aszuF-nZ7JwgJ3u_QMTXkI9lmDe_5p6GJSSIwkdyM4JRCyOgvuCisdmAZqCS4XdO20iNDdjrbBbfKDNvuNYNtGvTuvHw3a0cbnCvXUbnkOl7MTAbUya2e3xfXquR-LwSUeA9TzaoujViuULAiTTQPzkerxI1pcaS0vTIVVc3OsT2-HoOf-2bbQHMYCGyN4LVlUd6KjqO3srbCArLS1WCWUoMOF0Bor7CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 6.32K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 14:59:35</div>
<hr>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e40uOADEzJz21ro9xSydr_B6J5EERZSs8Yi776TqlHDePtRqDiJ1-GJbhKRBgmlloCMN82ibYdjsMv9nHOKn-0rPEfEKtLh-w3K8D_bpoVUQhIlcrxBo4h7f95VceKUoXPlNBDR5O3NIaIrwM9FdaUpQyZnYvsid4XG_TUv2d_At2nGuV7fmwcJMCkJg57B_cGuMWS4DeGvuUOyihw5seNZtcjOMGCJat-YHyvLqUVbgXLWxq0nS2OvNooeC0ydkIJWodpwrjFEkf_PkAQpJ_xa3glvEU1q6zyaVGEbW-fkuI6X6PSdl1JB0LkNo2HQLaLT3YvHWFjxVgYdCnoCWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
اضافه شدن سرور های جدید ( اهدایی عزیزان
❤️
)
🔺
بهینه شدن لیست BEST
⚡️
اضافه شدن sni های جدید
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 517 · <a href="https://t.me/archivetell/4777" target="_blank">📅 14:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ربات فشرده‌سازی فایل‌های PDF
📖
📚
@PDF_Compress_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/archivetell/4776" target="_blank">📅 13:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtokNcTkOsCMYtAiAeFqc_Zs_87kCWdT0H2oKFl24XCaJqYWg-rToJ-pA2ZZPHXbWRtm3Wd8VjlMNvag44OzbmQmEf_kN3RQYJKlnRdNxFonz1Ce3EHploJ9iAssZotATDZKgcDCgb2jM_0y-cMiunEL0D0Rtxg0SQZpck7lG4HWpjDBJniNtyjQnf4ctpxb7dmnaFA9NvYpyUSM-6KVLn1k3oHHH4AL1OZ5omAC_FxOZCdG2wmw9LYFrqyIoYnLvixgZ_t3OMwj1dnC0L1fgPokgqmJdTJcSfLTZcBcaxwIuOZfrUbBObAj64VC4WIbVu13z2YPFXqBbnkgSV45Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
MattDownloader
نسخه اول منتشر شد
❤️
می‌خوای ویدیو از یوتیوب (یا هر لینک دانلودی دیگه رو) بدون VPN بگیری؟ با MattDownloader این امکان میسر میشه:
GitHub Actions روی فورک خودت فایل را از اینترنت دانلود میکنه و آماده‌اش میکنه؛ تو فقط با اپ از همون گیت‌هاب بدون اینکه روی گوشی VPN لازم داشته باشی، فایل نهایی رو می‌گیری و ذخیره می‌کنی. یعنی گوشی بیشتر با گیت‌هاب حرف میزنه، نه مستقیم با سایتی که برات مسدود یا ناپایدار است.
چطور کار میکنه؟ لینک را به اپ می‌دهی (مثلاً لینک ویدیوی یوتیوب که به لینک مستقیم تبدیلش کردی)، ورک‌فلو روی ریپوی تو اجرا میشه، بعد اپ فایل آماده را از مسیر jobs میخونه و روی دستگاه دانلود میکنه.
🎬
مناسب برای ویدیوهای یوتیوب و لینک‌های سنگین
⚡
ست‌آپ یک‌بار با توکن و آدرس فورک
📥
دانلود نهایی از گیت‌هاب
🖼️
امکان ذخیره در گالری برای ویدیو/عکس
راهنما و APK اینجاست:
https://github.com/matthewnet/MattDownloader
آخرین نسخه برای نصب:
https://github.com/matthewnet/MattDownloader/releases/latest
تجربه‌تون را بفرستید
💙
برای دریافت نسخه‌های بعدی:
@mattspoof</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/4774" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت) خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟ ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها،…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/4773" target="_blank">📅 12:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdrg76bSa_fbCaeNAJ0l8pQDO-H4z9lnA3OUoX1wPq32L_a6zdJb6nEZDWyhXZ61GaNf0xNEw_J7-d1knBNVPX2cl86nHjhgBX_OmdPevhzOGeb99kAAkBA9fg-gDNtJSa78waxd_WgqalX_OlwavNqEI9irufUqMIRm3jvItqaB6TohJxiNiyKSfF2BLa5_iQZAwFyVTD-fP9UJErVQs2iWLosaHctw82yS21yumk5bqyLm8kfv2F45HCOirRqqPFpEDmOp0U-AMQWiU42i5HMWvDCazXijPq75JqzmFydRg5N2XU25zCiH6ZDo83TGrULrpr1AGtimeEi3UBYahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت درحال احراز کردن IP سرور های ایران هستش. اینطوری صاحب هر IP برای حکومت کاملا مشخص میشه.
قبل از این، دیتاسنتر ها احراز رو خودشون انجام میدادن اما برای اکانتی که میسازید نه IP سرور. اگه حکومت هر دستوری بابت پیگیری IP خاصی میداد، باید از فیلتر ISP عبور میکرد که میشد با روش هایی دورش زد یا گردن نگرفتش
اما الان خود حکومت دیگه میدونه کدوم IP برای چه شخصی هستش...
@ArchiveTell
Source</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/archivetell/4772" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ربات تبدیل صدا به متن رایگان
@sedatextbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/4771" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
آموزش صفر تا صد راه‌اندازی تونل ریورس (Reverse Tunnel) در 3x-ui
---
رفقا سلام!
✋
امروز یه آموزش پایه‌ای اما به‌شدت کاربردی داریم برای راه‌اندازی تونل Reverse بین دو پنل 3x-ui (سرور ایران و خارج).
ممکنه بسته به شرایط سرورتون نیاز به یه سری تغییرات ریز داشته باشید، اما ساختار اصلی و تضمینی همینه!
مرحله ۱: ساخت Inbound روی سرور ایران
🇮🇷
1️⃣
وارد پنل 3x-ui سرور ایران بشید و به بخش Inbounds برید.
2️⃣
دو تا کانفیگ باید بسازید:
🔸
کانفیگ اول (برای Tunnel):
• Protocol: VLESS (یا پروتکل دلخواه)
• Transport: WebSocket
• Path: /tunnel
• Remark: tunnel
• Port: حتماً یکی از پورت‌های پشتیبانی‌شده توسط CDN (مثلاً 8080 یا 2082)
🔸
کانفیگ دوم (برای User):
• Protocol: VLESS
• Transport: WebSocket
• Path: /user
• Remark: user
• Port: یکی از پورت‌های CDN (مثلاً 8080)
⚠️
نکته به‌شدت مهم: حتماً از پورت‌هایی استفاده کنید که CDN (مثل ابرآروان یا کلودفلر) اجازه می‌ده؛ مثل: 80, 443, 8080, 2052, 2082, 2086, 2095.
مرحله ۲: تنظیم Reverse روی سرور ایران
🇮🇷
1️⃣
برید به بخش Xray Config و بعد تب Reverse.
2️⃣
یه Reverse جدید بسازید (بخش Portal):
• Tag: portal
• Domain: یه اسم دلخواه (دقت کنید که روی سرور خارج هم باید دقیقاً همین باشه).
3️⃣
حالا Mapping رو انجام بدید: کانفیگ tunnel رو وصل کنید به user (یعنی Tunnel ➔ User) و ذخیره کنید.
مرحله ۳: انتقال کانفیگ به سرور خارج
🌍
1️⃣
از کانفیگ tunnel (که تو ایران ساختید) خروجی (Export) بگیرید.
2️⃣
وارد پنل سرور خارج بشید و برید به بخش Outbounds.
3️⃣
یه Outbound جدید بسازید و لینک ایران رو اونجا Paste کنید.
(دقت کنید که دامنه‌تون باید پشت CDN باشه و به آی‌پی سرور ایران اشاره کنه).
مرحله ۴: تنظیم Reverse روی سرور خارج
🌍
1️⃣
تو پنل خارج برید به بخش Reverse.
2️⃣
یه Bridge بسازید:
• Tag: bridge
• Domain: دقیقاً همون دامین/اسمی که تو سرور ایران گذاشتید.
• Interconnection: همون Outboundی که تو مرحله قبل ساختید.
• Internet: روی direct یا freedom تنظیم کنید.
3️⃣
سیو کنید و تمام!
✅
نتیجه چی می‌شه؟
سرور خارج به ایران متصل می‌شه ➔ تونل ریورس برقرار می‌شه ➔ کاربر به سرور ایران وصل می‌شه و اینترنت آزاد رو از سرور خارج دریافت می‌کنه!
💡
نکات طلایی و عیب‌یابی:
🔹
مسیرها (Path): پث‌ها (مثل tunnel/ و user/) باید مو به مو یکی باشن. یه اسلش (/) اضافه یا کم، کل کار رو خراب می‌کنه.
🔹
نقش CDN: بدون CDN این روش یا کار نمی‌کنه یا شدیداً ناپایداره. حتماً پشت CDN باشید و تیک WebSocket رو هم تو تنظیمات CDN روشن کنید.
🔹
نیاز به TLS یا Nginx: استفاده از Nginx الزامی نیست ولی برای تمیزیِ کار، روت کردن پث‌ها و استفاده از پورت 443 خیلی جوابه. TLS هم بستگی به شبکه داره، بعضی جاها فقط با 443 جواب می‌ده.
🔹
مشکل وصل شدن بدون اینترنت: اگه وصل شدید، چند کیلوبایت سند و ریسیو داشتید ولی اینترنت نبود، شک نکنید مشکل از ایناست: اشتباه بودن Path، مشکل تو هدرهای Upgrade/Connection، مپ نشدن درست Reverse یا گیر دادنِ CDN.
📌
#آموزش
#تونل
#ریورس
#Reverse_Tunnel
#سنایی
#3x_ui
#vless
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/4770" target="_blank">📅 11:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سایت ارسال کانفیگ
http://m.ulni.ir
https://sphost.theazizi.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/4769" target="_blank">📅 09:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آپلودر های فعال
https://up.zaringo.sbs/
https://rozup.ir/
https://uploadgirl.ir/
https://seup.shop/
http://uplod.ir
https://up.20script.ir
https://punkpaste.ir
https://my.files.ir
https://toolschi.com/tools/upload-center
http://nixfile.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/4768" target="_blank">📅 09:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ربات کاهش حجم ویدئو رایگان
@mediaEasyBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/4767" target="_blank">📅 09:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاش زودتر آیفون ۱۸ بیاد که آیفون ۱۷ ارزون‌ تر بشه بتونیم تن ماهی بخریم.
@archivetell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/4765" target="_blank">📅 00:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/4764" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.1.0
(نسخه ی رسمی)
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.2
📱
Telegram
(رسمی)
12.7.2
📱
Telegram
(Windows)
12.7.2
📱
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.03.17
5️⃣
Mhrv Rs
v1.9.14
📶
Npv
123
📶
V2box
5.3.4
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
Masterdns
1.0.9
📶
Open vpn
3.71
📱
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/4763" target="_blank">📅 23:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkvDbyoHSdv-atBXFIpSw8_NrwVui9qRHqEc27Zc1Pz4QrFAhv1Q36GuAXp3-x-pFTZcZzl3Z7KuncDj5ihbYecgZ0z-YjSnhkW4hEpQzdlL-1fkQC5ztQ6xYJVOZQwnhcfOKl5f5RaOGKiKYMcWJv4l1nIW-KX_dMz3XSB2GeeCwmhr6G7O_zjVAmqiygxKbWykMABiGYvO2xjDdgpoa2-cQ4r0Js-E7M6rT2nsN_o_uFDkCQG7QmYZR-_ifnIWJnetZUk1s5GRLmQqB-h-eeIL1jYrB2_lHuXYmOBSbFU7kooP37HrZU6aSenmr0KOSanRpWKXh-4jq5sHd2vQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
بومی‌سازی هوش مصنوعی برای توسعه‌دهندگان.
ترجمه YAML، JSON، TXT و محتوای چندزبانه با حفظ ساختار، جایگزین‌ها، متغیرها و قالب‌بندی.
@LocalynBot
⭐
کد منبع گیت هاب
https://github.com/LocalynAI/LocalynAI
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/4761" target="_blank">📅 22:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">YT_dL.ipynb</div>
  <div class="tg-doc-extra">22.5 KB</div>
</div>
<a href="https://t.me/archivetell/4760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/4760" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
دانلودر حرفه‌ای و پرسرعت یوتیوب مستقیم به گوگل درایو! (بدون مصرف حجم اینترنت)
خسته شدید از سایت‌های پر از تبلیغ، قطعی‌های مکرر و محدودیت سرعت برای دانلود از یوتیوب؟
ما یک اسکریپت اختصاصی و هوشمند برای محیط Google Colab آماده کردیم که به شما اجازه میده ویدیوها، فایل‌های صوتی و حتی پلی‌لیست‌های کامل یوتیوب رو با بالاترین کیفیت ممکن (تا 4K) دانلود کنید.
💡
هدف و مزیت اصلی این اسکریپت چیست؟
تمام فرآیند دانلود توسط سرورهای قدرتمند گوگل انجام میشه. این یعنی شما می‌تونید ویدیوهای چند گیگابایتی رو در چند ثانیه دانلود کنید، بدون اینکه حتی یک مگابایت از حجم اینترنت گوشی یا سیستم شما کم بشه!
🛠
چطور از این ابزار استفاده کنیم؟ (بدون نیاز به کدنویسی)
استفاده از این اسکریپت به شدت ساده است و دارای یک رابط کاربری (فرم گرافیکی) است:
1️⃣
اسکریپت را در گوگل کولب باز کنید (فقط به یک اکانت جیمیل نیاز دارید).
2️⃣
در فرمی که می‌بینید، لینک یوتیوب رو پیست کنید.
3️⃣
کیفیت ویدیو (مثلا 1080p) یا فرمت صوتی (مثلا MP3) رو از منوی کشویی انتخاب کنید.
4️⃣
دکمه اجرا (Play
▶️
) رو بزنید و تمام! اسکریپت به صورت خودکار ابزارهای لازم رو نصب کرده و دانلود رو شروع می‌کنه.
📁
فایل‌های دانلود شده کجا ذخیره میشن؟
در تنظیمات فرم، گزینه‌ای برای اتصال به گوگل درایو وجود داره. اسکریپت به صورت خودکار به درایو شما متصل میشه و فایل‌ها رو در پوشه‌ای به نام YouTube_Downloads (یا هر اسمی که خودتون در فرم بنویسید) ذخیره می‌کنه. بعد از اتمام کار، کافیه برنامه Google Drive رو باز کنید تا فایلتون رو اونجا ببینید!
🔗
لینک ورود به اسکریپت:
[لینک گوگل کولب خود را اینجا قرار دهید]
👇
اگر سوالی در مورد نحوه استفاده داشتید توی کامنت‌ها بپرسید.
Developer : Samad.R
@ArchiveTell
‌
#یوتیوب
#دانلودر
#گوگل_کولب
#ترفند_آموزشی
#ابزار_کاربردی
#دانلود_از_یوتیوب</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/4759" target="_blank">📅 21:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=pIg19eCAxJTuZ8TYrnHDAIUhGOX2qb5clZ2lAspHCzmC-Yxd_EfGVu996tADzO4veNBZpDGj2HZ6jkeQZKoWlTIh-BgUWYoHqv1khZ6RZBtk_nKcTUpJrwYKvsFBrw6e04KNogVSqomF8Rwolcj-dv-Jx2kb9hxhTYI9NJcjSXjRMWey7R3DpvrWlqGpA-eNxBq4hMyGTn9wsFczt0ebNMbgjIgAKFh4jqhwFIuunw3EAiNzjLqwASCVMWjeyzlGaPSPLL33vzh61_Cn2_-yPlrDFK1_3pQL-Zd-X2aT2NHR5GZpu6DUno4-Vuj4apkf8vM7Nt_5AD00x0C319OgfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7bc1a6d.mp4?token=pIg19eCAxJTuZ8TYrnHDAIUhGOX2qb5clZ2lAspHCzmC-Yxd_EfGVu996tADzO4veNBZpDGj2HZ6jkeQZKoWlTIh-BgUWYoHqv1khZ6RZBtk_nKcTUpJrwYKvsFBrw6e04KNogVSqomF8Rwolcj-dv-Jx2kb9hxhTYI9NJcjSXjRMWey7R3DpvrWlqGpA-eNxBq4hMyGTn9wsFczt0ebNMbgjIgAKFh4jqhwFIuunw3EAiNzjLqwASCVMWjeyzlGaPSPLL33vzh61_Cn2_-yPlrDFK1_3pQL-Zd-X2aT2NHR5GZpu6DUno4-Vuj4apkf8vM7Nt_5AD00x0C319OgfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
گوگل در حال آزمایش Gemini Omni
✅
قابلیت تولید ویدئو – جایگزینی مدل‌های Veo با یک خط تولید یکپارچه.
✅
همزمان خروجی صدا و تصویر – ترکیب چندرسانه‌ای پیشرفته.
✅
معرفی رسمی – انتظار می‌رود در Google I/O هفته آینده به‌صورت کامل اعلام شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/4756" target="_blank">📅 19:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram-X-0.28.3.1785-arm64-v8a.apk</div>
  <div class="tg-doc-extra">56.6 MB</div>
</div>
<a href="https://t.me/archivetell/4755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram x
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/4755" target="_blank">📅 18:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ_2eM6EI11rJknomkE6y4E-sJ7ZsZozkyqtPT4S-hui48ZnR2XtNt0xauO2PAw0OC3JbydnD9XXbdV4r3KYqC8_wzwivSf_JfQlGn5_tsxWcSdfNUtaU5bXf-CToTz-YZDK6C_BuUmpbiwTgX5MFoL7MOoW3E2y3H4AEA9bxBFILdkHIORRLJ-lkW8cxP4FMecKxDXtfwu_mmrzVCAhHWcfaBtwdiakJCc9X43QzDZz4_8zP4y1HdNcCC2qY_fRKwsNk-O3En-4unw1x0HFJRGBVYvZna6l_ferklAeIGo8m0cgh7UpX7JJwfo4oo_2M8DNPOyRuIAuG61RkfuY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ویژگی‌های کلیدی در آپدیت جدید
🛰
امکان اسکن با DNS شکن
(نسخه آزمایشی، ممکنه کار نکنه)
⚙️
کنترل دستی پردازش‌ها (Thread Control):
قابلیت تنظیم تعداد تردها توسط کاربر برای جلوگیری از کرش کردن (خطای Signal 9) در ترموکس اندروید.
💻
نمایش زنده در ترمینال:
نمایش آنی کانفیگ‌های متصل در صفحه ترمینال، علاوه بر ذخیره در فایل.
🛡
عبور از فیلترینگ هوشمند (DPI):
تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
🌐
دیتابیس داخلی غنی:
شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4754" target="_blank">📅 18:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تا ۱۰ روز دیگه جنگ میشه..</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4753" target="_blank">📅 17:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4752" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی Telegram 12.7.2
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4752" target="_blank">📅 17:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یکم زمانبره. لیست ایپی ها و sni ها افزایش پیدا کرده و تستش هم دقیق هستش. برا همین طول میکشه. ببرین تو کلاینت Exclave یا V2ray همشون پینگ میده.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4751" target="_blank">📅 16:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlkIrjBjwsrvx8ZYeKkWKbq1wBYlmaXrtUkA3qaxQNDi52xjN9dxg2oBPtY3mYsg8Bgmrs3QNXw-s84YEWpoD3d_d1Reh-KR8AypslO5Ln2HsMxmkx6P1EH_neY9HyyCiXhRL1iDUdpveikUh51fl1L3nLZYPjYduHd6dYnOlLPeFylokzslXCLyEFcha8bXOYwBmL384W7Rh_U_Fumev4QV7Yx6Bu9JbPCjndWXdH0aAo6sRknT8t3h_KdhU0rXGgEAa_hoRfs30NGPDCvqtQuDr9hDuT1eAhnLXjCibkPsmriCByvGV-IZJazUsASJ1UBrkFKbwCNDEBMzldS-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ابزار NETLIFY-SCANNER (نسخه V1 Pro)
🔆
اسکنر IP و SNI های نتلیفای  ---  رفقا سلام.
✋
اگر با کانفیگ‌های نتلیفای کار کرده باشید، می‌دونید که خیلی وقت‌ها پینگ دارن ولی عملاً وصل نمی‌شن (پینگ فیک). این اسکنر پایتونی رو برای حل همین مشکل آماده کردیم.  تفاوت اصلی…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4750" target="_blank">📅 15:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad--AjRoBWd_-4JZAWCx00ppekfX6OStYollTcmSYLWR6-DKYodAmNafS6NksL_m9OSrOpb1pa5NoRZyAv2im8_Df3XOKXU_QFHKnTjQ_7iYtSem62mqAvrR0mkumGM1MedsAbVfFFz91Ze3uJoHRTKVhh23N9T3ihZpR1uig_6Qw_8E9NpwxkJjHl-N1NWvMV8hkHULLw6J8cRshLXlfEZ6iWQUJm94z3jNNsqZKpBB1EXXlonXw3fkbHj5bM-9GDhXn0PqzYNiEooSmXz1nBfnsKj-spr3lX7aODk4QfJzZWWAVtwzqokxiZNpJkwlLMFZ5x620B7a3AYRbkqRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/4749" target="_blank">📅 15:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9PtY_d0kgQhO0GrLcW7XFDz1FJReSz82oke2iTQyr8BxVhm75OLk6F0yOMaA4swCy9hw1NAsKCRmrsxk7IJscvPLDWB8oozKNsgll5aG1iT46XNW4WMkT8UoCtiFsZDatCuHHPP_W8C28yfQKTsQRTHzm8ACHXrPyERlQMM5yOQNTzUKIWORa2vI3b8FrPORKjedwvzJimlp6veeLM2FKyAuGwAo98y54ENYmFVjxsHWBXQ3P7dhkOWeIKiyiz7CqIa4CKF0upY2Dk1XJY_1EWcVFh-PG1_KSJhGAn_sLW1ULUmFXL8nSAp4YzZYztYSiXSk6Y7nfry1dzHQPFYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
سایت و برنامه کانفیگ ساز آپدیت شدند
📌
فایل برنامه
📌
لینک سایت
🌐
قابلیت انتخاب چند سرور
🔺
اضافه شدن شمارنده تعداد کانفیگ های ساخته شده
⚡️
اضافه شدن بررسی کننده لینک نتلیفای
●  کانفیگ ساز جدید فقط روی
نسخه 1.0.3 پروژه
کار میکنه
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/4748" target="_blank">📅 13:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/4746" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">install_3x_ui.sh</div>
  <div class="tg-doc-extra">22 KB</div>
</div>
<a href="https://t.me/archivetell/4745" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اسکریپت نصب آفلاین پنل ثنایی هست.
برای افرادی که اعتقاد به بکدور دارن و به میرور ها اعتماد ندارن.
فقط کافیه که توی بخش Releases یک نسخه انتخاب کنید و متناسب با CPU سرور یک نسخه دانلود کنید. و انتقال بدید به سرور.
در نهایت این bash اسکریپت رو اجرا کنید.
bash install_3x_ui.sh
به شکل اوتوماتیک بدون ssl نصب می شه.
فقط بعد نصب با دستور x-ui پورت و یوزر پسورد تغییر بدید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4745" target="_blank">📅 11:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kln566gttOTIYw8a3rbVTyNCbW3VzH_24q6NXtOrZNYicUQdFlpnkg0NHQg-AgjhPUKsyKGpDYOcqIufnsKPDlBAeqQrI1TD6Bdzgx6WVGPvybguH2L0dj6YLY2nbppaIStk-AViloourNtZHpF64KhEZQr6xxWMZlNg-HtEWrxC0DmK1QK1_7EkI_gGfHDmeO60w6Re_Bg0e_RQnFVg4dQUwMIx6uzAhr9PeIHg9-ecSDw7YazwSvC_dwyDIl4IdoZ48C5hFWSsmZsTZqqXCp0XZ0mgLOYov6WB-mysaf2Jx_lu9VOeYv966xi6OX2Q2QrYR73rNDEG4Kp9gXYirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ ابزار هوش مصنوعی که ارزش ذخیره در گنجینه شما را دارند
💎
1.
Claude.ai
— حل مسائل
2.
PicWish.com
— حذف پس‌زمینه‌ها
3.
Perplexity.ai
— تحقیق درباره هر موضوعی
4.
Suno.ai
— ساخت موسیقی
5.
Canva.com
— طراحی گرافیک
6.
ElevenLabs.io
— کپی صدای افراد
7.
Grammarly.com
— اصلاح نوشتار
8.
Luma.ai
— ساخت ویدیو
9.
RecCloud.com
— خلاصه‌سازی یوتیوب
10.
Runway.ml
— ویرایش ویدیو
11.
Descript.com
— ویرایش پادکست
12.
Syllaby.io
— ویدیوهای بدون چهره
13.
Skysnail.io
— تصاویر کوچک ویروسی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4743" target="_blank">📅 10:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
نسخه کاملا آفلاین 3X-UI (ورژن ۳)
فقط این چند دستور رو به ترتیب اجرا کن
-  دانلود فایل نصب با نت ملی
wget https://boto3.s3.ir-thr-at1.arvanstorage.ir/3x-ui-3.0.tar.gz
-  استخراج فایل‌ها
tar -xzvf 3x-ui-3.0.tar.gz
- دادن دسترسی اجرا
chmod +x install.sh
- نصب یا آپدیت پنل
./install.sh
📌
نکته:
این نسخه کاملاً آفلاین نصب میشه و نیازی به GitHub یا دانلود فایل اضافه نداره.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/4742" target="_blank">📅 10:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سایتی جایی که دامنه رایگان (هرچی) بده بفرستید</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/4741" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجموعه‌ای از برنامه‌های کار راه بنداز آزمایشی!
سلف‌هاست شده، به رایگان، برای همه.
https://hxlab.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4740" target="_blank">📅 08:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6LnfVwnrWWTU0nAFMvPtoOsLN2q75oqyfxUlA9NxM0HE3iyMAHuxLQFxpNHuXjy7SezTFF5DBefr4vqsu6xrxxtck0sDHTJHN5VuTsTWmxKjyDnP9sV7pXBYdD6pgFlq0gUpK5KVsSbkxbHedfgFQIn6-2sdTRaUw30DOQkw-OM9vG8g7wJjvoUtaxsVN52Ikqg2T6GZ2g3Ir9vlsutR2b8h1bdfFyh0Uh-AAWKPj0oE9mgcdaj2HHMgppRiL4Yq1LYVsRdPHf5G4GMtNqAla0HUWDcuuzdJ3ffvjDRhSfPuBUS6nDdyMXYixSNaeKC4WSvv00LbnnZP6Oup7DYjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔆
اسکنر IP و SNI های نتلیفای
📌
github.com/IR-NETLIFY/NETLIFY-SCANNER
🔺
مواردی که ok میشن بدون نیاز به شکن وصل میشن براتون
🔸
دی ان اس شکن رو کامل حذف کنید از سیستم
🔹
یک بار مودم یا نت رو خاموش روشن کنید تا آیپیتون عوض شه
🔸
بدون هیچ DNS و فیلترشکنی اسکنر رو ران کنید
🔺
می تونید کد رو روی سرور ایرانتون ران کنید اگه چیزی پیدا کرد تونل نتلیفای بزنید به خارجتون وصل شید (
یه کانفیگم بدید دایرکت
)
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/4739" target="_blank">📅 02:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ultra_downloader_pro.html</div>
  <div class="tg-doc-extra">34.5 KB</div>
</div>
<a href="https://t.me/archivetell/4736" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Untitled 1.mkv</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4736" target="_blank">📅 02:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فکر کن عراقی که سنگشو به سینه میزنی تلگرامش رفع فیلتره
افغانستانی که مسخرشون میکنیم برای اومدن به ایران 5g اوکی کردن
سوریه ای که میگیم آدم برای دشمنشم نخواد پرداخت با مسترکارت اوکی کرده
اونوقت ایرانی خوشحال میشه که گیگی ۱۸۰ رو خریده ۱۳۰....</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/4734" target="_blank">📅 23:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میگم شمام دیگه خسته شدید؟
😕
@archivetell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4733" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu__zxxNDc8UPdQr-uSf5Hh1vv_XTiOg89Fq8vvyEK5wbWCmALEaucrL_dQdwNeF1mrU2yruAIiU3BWEc1QTRFSfASGsiVSbi7AQcTND69V5XKIRw2AOTxIeEvvyfywwRgI0NsLP93xcRC92PKlVkMIJLi8V-MwvuIdxd7TnT9QeVld6O7s537A6Eb8F_tpIzrMxaRyFo1d6fRc5grpiwR6xmH40YzYdKlBvCimVbuwrpRJL8tP658ufP8oYeQhN8n9aD7wHjNTGB9hLvrHXwC3yKjf3T_903vF_E4iCR05eHNDHBW3F-GGJyV1ezWyAY8V7CBTko58arlOU22Z83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/coyPPDsdzjaVOif-p1ueoOYZDz8tn3cM6KI-CSRXKUBvUzWHLTnaOqcjl10rMj00ikW_2mbnHd8iILCvtcwW8ICtGfy-B1SZxGsqxIUHWnv_-gWA2Qlxxguld1gfnRQYxECIa_sAd3JQNKLDnojUhXWzuj2SYrrNYe2Xn-DMQf9UDmVnrmrZImbd3TBkQvzPtDinhkPkF8EFlRglVezthOAj8_ZfCQhtN_Wgn8Td8qykpHnObxhDKxoIEGMO73zgaZWedctjp0qHP9W5V5FiLozA7aEYRt21joUsr6TTF973uGp2IUwpnZMAl3uj0thseVbFAN8KKbfzt2mYGEbr8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4731" target="_blank">📅 22:29 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">client_resolvers.txt</div>
  <div class="tg-doc-extra">9.7 KB</div>
</div>
<a href="https://t.me/archivetell/4730" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns  قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب…</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4730" target="_blank">📅 22:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⛈
کانفیگ اختصاصی StormDns
قطع شده
1️⃣
در قسمت Profiles ، گزینه import رو بزنید و کانفیگ رو اد کنید
2️⃣
در تب connect بخش Resolvers ریزالور هارو اد کنید و کانکت رو بزنید(1 تا 10 دقیقه زمان میبره وصل شه)
⭐️
لینک دانلود برنامه مورد نیاز
📱
لینک ریزالور ها
⭐
مناسب برای
🌐
وب‌گردی،
📱
تلگرام،
📱
هوش مصنوعی و ...
(بدرد اینستاگرام، یوتیوب، دانلود فایل‌های حجیم و کارهایی که نیاز به پینگ پایین دارن نمیخوره)
✔️
اگر برای خودتون و دوستاتون  نیاز به سرور کامل دارید، سرورهای StormDNS به همراه پنل مدیریت در اختیارتون قرار میگیره. کاملاً مستقل و شخصی
برای خرید سرور شخصی پیام بدین:
🚀
@Mo3inh</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4729" target="_blank">📅 22:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جایگزین گوگل میت
https://meet.theazizi.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/4728" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ربات سرچ عکس در Google , Bing , Yandex و TinEye
@ImageEyeBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/4727" target="_blank">📅 21:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فشرده‌ساز رایگان ویدیو و صدا برای کاهش مصرف اینترنت
📉
📶
@Compreseebot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4726" target="_blank">📅 21:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV-EpgarybCn1Vpxf3cz8Z_nEVzbPJe8H16BCxDmQk16kAfMJfROmMt1rOWzuVF0tyWBLMmnnwcUMv9eoQYJ30oRmlqEzeF3Y5-irdrYaqvHaLUdOsMNzP7SzEvvy-2l5bNda7_itKdesQsixhPdak1ppQJsNUJSvo2gInFvfJq9zl9PX9mX-BBl19_uCGzVXsIEvcrpfXwPQNFc81h_0kQ2CxTna5xzlnpAl2CBTz5L5Gy46aQN2uo9v3Q66RtEMQqRQEZIPvvs7FVwIl_OYR4tYoUs0KKzSRIbzE0bxPQpDanEfMK1lIoHG9PFHtftFXh0nhgAl9IpCVChN5teSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامپیوتر شخصی
عامل هوش مصنوعی مستقل از Perplexity برای macOS - تعامل با فایل‌ها، برنامه‌ها و اینترنت.
https://www.perplexity.ai/personal-computer
• کار با فایل‌های محلی و برنامه‌های بومی مک
• ادغام با ابزارهای وب از طریق مرورگر Perplexity Comet
• استفاده از بیش از ۴۰۰ اتصال‌دهنده برای هماهنگی ابزارها و فایل‌ها
• در نظر گرفتن زمینه شخصی کاربر
• پردازش داده‌ها در سرورهای Perplexity
• اجرای وظایف به صورت از راه دور با آیفون
• مقایسه فایل‌ها از برنامه‌های مختلف، انتقال یادداشت‌ها
دسترسی از طریق اشتراک Pro یا Max، در Mac App Store موجود نیست — از سایت Perplexity دانلود می‌شود. کلاینت قدیمی به زودی منسوخ خواهد شد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4725" target="_blank">📅 20:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVf1Oyhz84IyTk1YhKeF1Jw94mRmcQAQKQ8h8shwexS1Rigje8-JGjXKxgQFOQK3dKf2klOg9golPlR9j6juDWPDTTVriZNc-mOJx6hhGQlal6-a8LCm2qFpFvcc2uGXA8v5URfpJFE-UHMrZ6nitxNWLvquT53jrqvTAzscyPuJS2TgRfiOZQkTtL1zqnnqjpdG6tL7igelfx3Fuuf8E20_UNlU16AZT9WElMg8bNxTv9GP3xhPStICpqGn9-h_v34SNTiQIUpGcwznSk-QeYHNBKcMEpy88M6MuHus0hNADyX8cKhp1OKaGy85P6Hta-qsHLBklRoT83b2zvJJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین گل خیلی دیر پاک کردی پیامتو
😂
چون پاک کردی گذاشتم وگرنه مهم نبود واسم</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4724" target="_blank">📅 18:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
دانلود مستقیم فایل‌های فیلتر شده با سرعت نور (بدون نیاز به VPN!)
---
رفقا سلام!
✋
خسته شدید از اینکه برای یه دانلود ساده از سایت‌های فیلتر شده باید فیلترشکن روشن کنید و سرعتتون نصف بشه؟
امروز یه ابزار پایتونی به‌شدت خفن و خلاقانه براتون پیدا کردیم که دقیقاً برای دور زدن «نت ملی» و فیلترینگ شدید ساخته شده!
🔥
این ابزار چطور کار می‌کنه؟
شما لینک دانلود رو به برنامه می‌دید؛ برنامه به جای اینکه با اینترنت شما دانلود رو شروع کنه، به سرورهای قدرتمند گیت‌هاب دستور می‌ده فایل رو تو خارج از کشور دانلود کنن و بریزن تو اکانت گیت‌هاب شما!
بعدش شما فایل رو مستقیماً از سرورهای گیت‌هاب (که تو ایران فیلتر نیست) با سرعتِ نت داخلی و بدون نیاز به فیلترشکن دانلود می‌کنید!
🤯
🛠
آموزش
راه‌اندازی قدم‌به‌قدم:
1️⃣
ساخت کپی (Fork):
اول وارد لینک پروژه (در پایین پست) بشید و دکمه Fork رو بزنید تا یه کپی ازش تو اکانت گیت‌هاب خودتون ساخته بشه.
2️⃣
گرفتن توکن گیت‌هاب:
تو اکانت گیت‌هابتون برید به مسیر زیر:
Settings ➔ Developer settings ➔ Personal access tokens (classic)
یه توکن جدید بسازید و حتماً تیک دسترسی repo (تیک اول) رو بزنید. توکنی که بهتون می‌ده رو کپی کنید (فقط یک‌بار نشون داده می‌شه).
3️⃣
تنظیمات برنامه:
پروژه‌ای که فورک کردید رو دانلود کنید (یا با git clone یا دانلود فایل زیپ). فایل
main.py
رو با یه ادیتور (مثل نوت‌پد) باز کنید و این ۳ تا خط رو توش پیدا کنید و تغییر بدید:
🔸
REPO_OWNER
= آیدی گیت‌هاب خودتون رو بنویسید.
🔸
GITHUB_TOKEN
= اون توکنی که تو مرحله قبل گرفتید رو اینجا پیست کنید.
🔸
REPO_NAME
= به جای کلمه random، اسم ریپازیتوری خودتون (یعنی
downloader
) رو بنویسید.
فایل رو سیو کنید.
📥
چطور باهاش دانلود کنیم؟
1. اول فایل
req.bat
رو اجرا کنید تا پیش‌نیازها (کتابخونه‌های پایتون) نصب بشن.
2. حالا فایل
run.bat
رو اجرا کنید.
3. لینک دانلودتون رو بهش بدید و اینتر بزنید! برنامه به صورت خودکار فایل رو دانلود می‌کنه، اگه حجمش زیاد باشه پارت‌بندی می‌کنه و در نهایت روی سیستم شما ذخیره می‌کنه.
⚠️
چند تا نکته خیلی مهم:
🔹
ضد فیلترینگ هوشمند: اگر دیدید وسط دانلود سرعت کم شد یا دانلود چند ثانیه متوقف شد، برنامه خراب نیست! این یه ترفند هوشمندانه تو کدهای برنامه‌ست تا سیستم فیلترینگ (DPI) متوجه ترافیک سنگین نشه و سرعتتون رو محدود نکنه.
🔹
یوتیوب: این برنامه لینک مستقیم می‌خواد. برای یوتیوب باید اول لینک رو بدید به ربات‌های تبدیل فایل به لینک (مثل
@file_link_irbot
) و بعد لینک مستقیمش رو بدید به این ابزار.
🔹
امنیت: توکنی که ساختید دسترسی بالایی داره، پس فایل
main.py
رو به هیچ‌کس ندید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/soheilditf5-svg/downloader
📌
#آموزش
#دانلودر
#گیت_هاب
#بدون_فیلتر
#نت_ملی
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4722" target="_blank">📅 16:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فیلم و سریال بدون سانسور
https://www.sorkhcloud.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/4721" target="_blank">📅 14:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">g2ray generator v3.html</div>
  <div class="tg-doc-extra">70.2 KB</div>
</div>
<a href="https://t.me/archivetell/4720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚙️
g2ray Setup Generator v3.1
یه ابزار رایگان برای ساخت پروکسی شخصی با GitHub Codespaces
بدون سرور، بدون هزینه، بدون پیکربندی دستی فقط چند کلیک — پروکسی آماده‌ست
✅
─────────────────
چی داره؟
🔑
هر بار UUID کاملاً رندوم می‌سازه
📁
۶ فایل آماده برای آپلود در GitHub
📖
آموزش تصویری قدم به قدم برای مبتدیان
🔋
سیستم Keepalive برای جلوگیری از خاموشی خودکار
🔍
راهنمای تست اتصال قبل از وصل شدن
─────────────────
پروتکل:
VLESS + xHTTP + TLS روی Xray-core
بستر:
GitHub Codespaces رایگان — ماهی ۶۰ ساعت واقعی
─────────────────
⚠️
برای هر اکانت GitHub فقط یه Codespace بسازید</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/4720" target="_blank">📅 12:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ربات یوتیوب به لینک داخلی
@downloaddockbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/4719" target="_blank">📅 11:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رونیو ابزار توسعه دهندگان وب
https://ronio.ir/fa/
اگر توسعه دهنده وب هستید و به ابزار های خاصی برای طراحی نیاز دارید میتوانید از رونیو استفاده کنید که شامل طیف وسعی از ابزار های آنلاین می باشد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4718" target="_blank">📅 09:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mefRSZMJ9tltFZt0LHApvZwmV5cnYzxC6Q4HdCKya_Arl9MQswZpUTrkTwHXcLn7O8eJtx4demTkm9AP6g-ZaTf7aGVhwc6fne1gDt37bLOrsdhHN_awFReDGa8ZuTww8_KiKZaO9-_vENiMbyMGCTxUnmcgVM8iTl-N_zCdlJ48sk0327_qVcVMdwIOi4izx0_hoAK3BwFm1sBTAU0yH_l48SNIlViG9ChceWktecewmBui3nO8wHDB7H8B_JJBbHcUvoc8Zxjhqnur0WlMtp3VPtd6MYv9NZyG7jS8BIuQrxGTwarfjkQ5bqsB6-SSqeF7XrdLZHdmRolqiLRe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنظیم NTP سرور داخلی برای تنظیم خودکار ساعت و تاریخ
با تنظیم کردن این دو NTP میتوانید در ویندوز و تمامی دستگاه ها و مودم ها و روتر ها قابلیت بروزرسانی خودکار ساعت را بصورت خودکار انجام دهید همچنین اگر میکروتیک استفاده میکنید هم میتوانید از این دو سرور داخلی استفاده کنید.
194.146.239.1
194.225.150.25
ntp.day.ir
ntp.time.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4717" target="_blank">📅 09:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4716">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ربات ادیت موزیک
@musiceditor_tgbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4716" target="_blank">📅 08:59 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMarwinVPN🌓</strong></div>
<div class="tg-text">چندین سرور رایگان با متد Netlify بدون نیاز به شکن
🌐
لینک ساب زیر رو کپی کنین:
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
توی برنامه های زیر میتونین بزنین، پینگ بگیرین و استفاده کنین. قطع شد به یه سرور دیگه متصل بشین
• V2rayNG
• MahsaNG
• V2Box
• Happ
• Hiddify
• Streisand
....
منبع:
IR_NETLIFY
🧡
اگه خودتون هم با همین متد کانفیگ درست کردین میتونین به کانالشون اهدا کنین تا توی لینک قرار بگیره و ساب مدت بیشتری زنده بمونه
❤️
🛜
@MarwinVPN</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4715" target="_blank">📅 07:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگر کلاس دانشگاه شما در بستر adobe connect برگزار می شود برای دانلود فایل کلاس، آخر آدرس کلاس این متن را اضافه کنید و به جای filename در آن یک اسم انگلیسی دلخواه برای فایل را بنویسید:
output/
filename.zip?download=zip
مثال: اگر آدرس کلاس مجازی شما مانند زیر است:
https://vc4.uni.ir/s14042-23027551-1/?proto=true
آن را به شکل زیر تغییر بدهید:
https://vc4.uni.ir/s14042-23027551-1/output/filename.zip?download=zip
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/4714" target="_blank">📅 02:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il0NP_sZTRDupmhCXOssZ0qnrH9rDt_lYYy4k3JF-oW3Ivf1WYZ_u_whVBs3tKzSIz53NSqfDkQRfJvU1pgk00wOu0QHdJ-6g73PitSzLunEuIfhH1okZpZyKu57io3cRYhj-bQ2TMUZZXQq4x0Ktkhan2YnM91AKA7DlOafxRcoyFLJSOz8krPNoE4GER3lLt2NrTgqOBXkrb2h3UooD7wPIR2xvPxpsFiKYzubbGw37JBoSGDdqSCOkGMbd-3B2vvdiy1zjCQbfkYKpobkEcyPLNAbh7HlBcvp9sxm-qGQ9He-zDOGZJjkWx1x6KKhii0vCugauA1K_QfX5W1J0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
Canva AI – دستیار همه‌کاره برای محتوای تصویری
✅
بهترین برای: تولید، ویرایش و خودکارسازی پست‌های شبکه‌های اجتماعی، ارائه‌ها و مواد بازاریابی
- نیازی به مهارت حرفه‌ای طراحی نیست
- ایجاد طرح‌های سفارشی با چند کلیک
- بهینه‌سازی هوشمند رنگ، فونت و ترکیب‌بندی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/4713" target="_blank">📅 02:00 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4712" target="_blank">📅 01:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ربات دستیار هوش مصنوعی میرا
@mira
🔺
تو شرایطی که اینترنت برای خیلی‌ها محدود شده و اکثر کاربران ایرانی فقط به تلگرام دسترسی دارن، وجود چنین ابزاری واقعا کاربردیه و می‌تونه کمک بزرگی باشه.
🔺
می‌تونید Mira رو به گروه‌ یا کانال‌تون اضافه کنید، ازش سوال بپرسید، باهاش چت کنید یا حتی بخشی از مدیریت کانال‌تون رو بهش بسپارید.
🔺
امکانات نسخه رایگانش هم واقعا قابل توجهه، از جمله:
• پشتیبانی کامل از زبان فارسی
• چت بدون محدودیت
• تبدیل ویس به متن و متن به صدا
• جستجو در وب و پیدا کردن اطلاعات
• تحلیل عکس و لینک و توضیح محتوای اون‌ها
و کلی قابلیت دیگه که رایگان در اختیارتونه.
🔺
در نسخه پولی هم امکانات پیشرفته‌تری مثل:
• ساخت و ادیت عکس
• تولید موسیقی و ویدیو
• کدینگ ، کانکت به گیتهاب و...
• اتصال به جیمیل ، گوگل درایو ، گوگل داک و...
در دسترسه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/4711" target="_blank">📅 01:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4jyHugmYPx21hw2yn-1dkA5yARP1XsZm2pnafq96JLhw_4FXu7Ap1xnQDTiJi8K8aHc87REtNnNIljhemXko_3r8AaE2_dS7bkBI2giddgDvixbFcvTeadrcAzjm8Oafy5BaGcWb93ZL33NwdvtV1FIfacMnSglKkVhW_LdrU5g1JXi3puY-Im8OBP49t6mVFr3uKy8z2BIVAmJWmX-wLJwGBehOUm5ggJD6O1HMAb_JmNcv-wjivWMfWw5NE7yiA1FqyLQh0uewRswYDSa27jvkXwhyN9QL4ONWd3XZXq2mTiaWXdQLcAXNJ2m9ucOPt9Ne2tbck4id4flpaw-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IR NETLIFY V10.2 • BACHELOR EDITION
⚡️
تغییرات اصلی نسبت به نسخه‌های قبلی: ۳ تب کامل و حرفه‌ای:
⚡️
Generator — با پشتیبانی از چندین دامنه نتلیفای (داینامیک)
🔄
Replacer — جایگزینی دامنه با قابلیت توزیع خودکار بین چند دامنه
🔧
Tools — ابزارهای پیشرفته (Rename…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4710" target="_blank">📅 00:31 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOw21y6faUu4ScfoWT5o9QlOOltY8kekMIlNbKF_NxL9zdgoilgB5Xqo71rcToOK_3axYLIr3BoEgl5hn59Gz3sAjE1uQVs7oVcC-TjZDhXUcK8RNI5Na1i2o0o11bZpz2tJ6a3plD7viRv1ApIE6AVLJX21tPTIa_bN0-xCU3_RCWEaz8lM8fcH4aOIFM1FDXrem_NzlvBnp1rXq4YR7A8fGGkhKM__E12wy--wMt0UEDnT0IMxZYMvclhQAwlhc3HLohgBqYriF6XadDPz66ZPIwUOp1Tl0eV8k0WmUI_wexZ_8JtUxVQcOZm3-hYlzF5935fMUaq9mfgAJYb-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره
😁
🖤
طراحی سیاه و سفید مینیمال و حرفه‌ای
🌐
دسته‌بندی هوشمند SNI (۹ دسته + دکمه ALL): Helm Ecosystem Core Kubernetes Kubernetes SIGs (.sigs.k8s.io) Service Mesh & Networking Storage GitOps & Delivery Security & PKI Platform & Orchestration
⚡️
دو حالت:…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4709" target="_blank">📅 00:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmY84ADwEt8TDXfjlvhFPhvEw-cJ3hop3HjD8VaLTsxrfQB_SN_la-0cGL8U86KRkoeXiYhZYH6PZ-Xo_SdpodWLK_GQm5HnviH_oig7VfjFMBudaCiitA8-ozfvDhwa1iVbMP6-ozZ42HcR5rTLiMrHSe6vDOQOQAoUgHZYt0ycOmUU0EMqPrZCRLIn5OIrX9zWlJ7fISoqFYvsm42Nak4dCS9mgwqejrb-BlVMzwrh1carWv_boJ2WxxnaOoXpVlani-tCiX0JPuuEKHhy4GSZCFowia541RNdu2MxpVjlWUYH14PQUJ5Kw6fYlutqDKurUPANcmHB3nw3xlF1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه جدید لینک ساب اختصاصی کانال
⚙️
به صورت خودکار با لینک پروژه های اهدایی شما آپدیت میشه
⭕️
با شکن
وصله اگه کانفیگ ها قطع شدن دایرکت بگید
🔺
اضافه کنید به برنامتون یا اینکه بازش کنید کانفیگ ها رو کپی کنید
🔹
برای ساب جدید بهتره که از
هیدیفای
یا V2ray استفاده کنید روی بقیه نرم افزار ها بعید میدونم کار کنه
🔥
ساب جدید
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🚀
ساب قبلی
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt
🤝
روزی یدونه لینک پروژه (با اعلام نسخه) اهدا کنید دایرکت، کمک کنید این ساب تا ابد وصل بمونه
🤝
❤️
برای اینکه راحت تر پیدا کنم
#اهدایی
بزنید
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/4708" target="_blank">📅 23:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">@Bitchlorz
دا این جی تو ری چرا استوپ میشه خودکار هر نیم ساعت یکبار
دلیلش یه سیستم محافظتی تو خود گیت‌هاب به اسم
«Idle Timeout» (خاموشی خودکار)
هست.
قضیه اینه که گیت‌هاب برای اینکه اون ۶۰ ساعت تایم رایگان ماهانه‌ت الکی هدر نره، حواسش بهت هست. اگه ببینه نیم ساعت گذشته و تو محیط Codespace هیچ کلیکی نکردی، تایپ نکردی یا اصلاً تب رو بستی، پیش خودش میگه: «خب حتماً کارش تموم شده یا یادش رفته ببنده!» پس برای جلوگیری از مصرف شدن حجمت، سرور رو خودکار متوقف (Stop) می‌کنه.
🛠
چطوری این مشکل رو دور بزنیم؟
🔹
راه اول (ترفند Auto Refresh):
تب مرورگرِ Codespace رو باز بذار و یه افزونه
Auto Refresh
رو مرورگرت نصب کن. تنظیمش کن هر ۱۰ یا ۱۵ دقیقه صفحه رو یه رفرش ریز بکنه. اینطوری گیت‌هاب گول می‌خوره و فکر می‌کنه هنوز پشت سیستمی و داری کار می‌کنی، در نتیجه پروکسی قطع نمی‌شه.
🔹
راه دوم (تغییر تنظیمات گیت‌هاب):
وارد تنظیمات گیت‌هابت بشو و برو به مسیر:
Settings ➔ Codespaces
اونجا یه بخش هست به اسم
Default idle timeout
. می‌تونی عددش رو از ۳۰ دقیقه تغییر بدی و مثلاً بذاری روی ۲۴۰ دقیقه (۴ ساعت).
⚠️
(فقط حواست باشه با این کار، اگه یادت بره سرور رو دستی خاموش کنی، کل تایم رایگان ماهانه‌ت تو دو سه روز دود می‌شه و می‌ره هوا!)</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/4707" target="_blank">📅 22:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFjy3r8aiR2hc-HnW-d3LGT7jBlh6XVVTCkOPJ4dSTZ9XW-6EMl0EFTww42xOM6UOXrF_PeEceArAy48qZWQyrN6RQyxTfwy3__WYrFECNBl6SFin6dvCcKGVIcleSK0iizT5aKMYLhfF55rkj64c_ohTNqGCGZ7gDeum9Uc4IqS4fzvJVwxiAsNCZaTh3EUAQOGQE_-V2_ESqT05htNsMVUnbtH0LC78gIYaLCW--A0K5IXRnJTePIVbtmwIk5IfmpwpWJey1CnXDIjP9q4qSVIAekI65okbw9FxzRaMDGSdXSsZ2kFasBRDH32dxHPOvtPymvSLuW0KOOS5Qkg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83de2fa668.mp4?token=km3Csd0u8GYmPesGN_swKXQrUq0CfGEPPe1PP-sPa3nSWzuTWzUAHxctukrfrNyUwZsjyQ8kCmXaC5NNY6YnxAW2VOlGa8GynndBn4aa9a299OLhTmeqDVFxpSH5Ooqhx17kxj2Pezg-rzIhFrJQ-jXSKJ0YlZWfykM0BAQLyXbC5JOCp_oi8CyehS_iFKCCMNTiRSJt6uqotm9O_myFwfqpDBIMrOYDb2XMNv0ZsbyUqCBaTmRhFspzIZyglLOzfge4_qU2f4CQQ4wyvRMzoUrFYZyGGzmt7U5faN-djnMLj4j6bNdfh2xyNHjPF4roIE3LME65mLgWjvgRoKV-KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83de2fa668.mp4?token=km3Csd0u8GYmPesGN_swKXQrUq0CfGEPPe1PP-sPa3nSWzuTWzUAHxctukrfrNyUwZsjyQ8kCmXaC5NNY6YnxAW2VOlGa8GynndBn4aa9a299OLhTmeqDVFxpSH5Ooqhx17kxj2Pezg-rzIhFrJQ-jXSKJ0YlZWfykM0BAQLyXbC5JOCp_oi8CyehS_iFKCCMNTiRSJt6uqotm9O_myFwfqpDBIMrOYDb2XMNv0ZsbyUqCBaTmRhFspzIZyglLOzfge4_qU2f4CQQ4wyvRMzoUrFYZyGGzmt7U5faN-djnMLj4j6bNdfh2xyNHjPF4roIE3LME65mLgWjvgRoKV-KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔆
آموزش 0 تا 100 نتلیفای
💠
netlify.com
🔰
دانلود فایل پروژه
⚠️
نکات مهم متود
⚠️
🔺
با یک فیلترشکن پایدار برید که مشکل اپلود پیدا نکنید
🔺
دقت کنید پس از اپلود باید همه تیک ها سبز بشن و دو فایل باقی بمونه مثل تصویر
❤️
با تشکر از عزیزی که ویدئو ریکورد کرد
❤️
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/4705" target="_blank">📅 22:10 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آپدیت شد V10  جنریتور https://johncarterjourney-rgb.github.io/netlify-config-generator  گیتهاب https://github.com/johncarterjourney-rgb/netlify-config-generator
🔧
سرور کاملاً دلخواه — UUID تصادفی + مسیر دلخواه + فینگرپرینت (Chrome/Firefox/Safari/Random)
📊
…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4702" target="_blank">📅 21:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
رونمایی از IR NETLIFY V9 • BACHELOR EDITION!  ---  رفقا سلام!
✋
بعد از مدت‌ها تلاش و توسعه، نسخه V9 ابزار معروف IR Netlify Config Generator رو با طراحی کاملاً جدید، اختصاصی و با تجربه کاربری Premium براتون آماده کردیم.   این ابزار یه دستیار همه‌چیزتموم و…</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/4701" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
ابزار همه‌کاره Meli-Action: دانلود از یوتیوب، تلگرام و وب مستقیم تو گیت‌هاب!
---
رفقا سلام!
✋
با این وضعیت فیلترینگ شدید، امروز یه پروژه اوپن‌سورس و به‌شدت کاربردی به اسم Meli-Action رو براتون آوردیم که حسابی بین کاربرا ترکونده (بیشتر از ۷۹۰ بار فورک شده!).
کارش چیه؟ دقیقاً مثل پروژه‌های قبلی که معرفی کردیم، از سرورهای قدرتمند و بدون فیلتر گیت‌هاب (که تو ایران بازه) به عنوان یه دانلودر واسطه استفاده می‌کنه؛ اما با امکانات خیلی خیلی بیشتر!
✨
ویژگی‌های بی‌نظیر این ابزار:
🔸
دانلود لینک مستقیم: هر فایلی رو دانلود می‌کنه. اگه حجمش بالای ۹۹ مگابایت باشه، خودش هوشمندانه با WinRAR به پارت‌های ۹۵ مگابایتی تقسیمش می‌کنه تا محدودیت گیت‌هاب رو دور بزنه!
🔸
دانلود از یوتیوب: دانلود ویدیوها با کیفیت دلخواه شما.
🔸
دانلود از تلگرام: دریافت مستقیم فایل‌ها از کانال‌های عمومی تلگرام.
🔸
گوگل پلی: دانلود مستقیم فایل نصبی (APK) برنامه‌ها.
🔸
آرشیو صفحات وب: می‌تونه کل یه سایت فیلتر شده رو به صورت فایل آفلاین (MHTML) براتون ذخیره و زیپ کنه.
🛠
آموزش راه‌اندازی (فقط یک‌بار):
1️⃣
وارد لینک ریپازیتوری بشید (پایین پست) و دکمه Fork رو بزنید تا یه کپی تو اکانتتون ساخته بشه.
2️⃣
تو ریپازیتوری خودتون، برید به تب Settings و از منوی سمت چپ مسیر Actions ➔ General رو انتخاب کنید.
3️⃣
تو بخش Actions permissions، گزینه Allow all actions and reusable workflows رو انتخاب و Save کنید.
📥
چطور باهاش دانلود کنیم؟
خیلی ساده‌ست! برید تو تب Actions، از منوی سمت چپ نوع دانلودی که می‌خواید رو انتخاب کنید (مثلاً دانلود از یوتیوب یا فایل مستقیم). بعد سمت راست روی Run workflow کلیک کنید، لینکتون رو بهش بدید و تمام!
گیت‌هاب فایل رو دانلود می‌کنه و تو ریپازیتوری خودتون قرار می‌ده تا با بالاترین سرعت و بدون فیلترشکن دانلودش کنید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/Kurdeus/Meli-Action
📌
#گیت_هاب
#دانلودر
#یوتیوب
#تلگرام
#بدون_فیلتر
#Meli_Action
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/archivetell/4700" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4699" target="_blank">📅 17:10 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4698" target="_blank">📅 16:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرادار وضعیت اینترنت</strong></div>
<div class="tg-text">🔴
هم اکنون اختلال در زیرساخت اینترنت کشور
طبق گزارش‌های کاربران، هم‌اکنون کاهش پهنای باند و اختلال گسترده‌ای در زیرساخت اینترنت کشور رخ داده و برخی سرویس‌دهنده‌ها با قطعی یا از دسترس خارج شدن مواجه شده‌اند.
بر اساس این گزارش‌ها، سرورهای شاتل، مبین‌نت، ایرانسل و رسپینا دچار اختلال شده‌اند و همزمان بسیاری از سرویس‌ها، هاست‌ها و خدمات داخلی نیز با اختلال و کندی شدید مواجه شده‌اند.
همچنین گزارش‌ها حاکی از آن است که برخی VPNها نیز دچار اختلال شدند و یا اتصال آن‌ها به‌طور کامل قطع شده است.
📡
@IRRadar</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/4697" target="_blank">📅 16:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4694">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اکثرا وی پی ان فروشای قوی به همراه تانل هاشون یکی دوساعتیه برگشتن روبیکا
😂
🌟</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4694" target="_blank">📅 16:25 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به زودی چنل IR Github از مرزاد
🙈
🗿
🔥</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/4692" target="_blank">📅 16:12 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🛑
آموزش متوقف کردن (Stop) گیت‌هاب Codespace  ---  رفقا همون‌طور که گفتیم، برای اینکه تایم رایگان ماهیانه‌تون تو گیت‌هاب الکی هدر نره، حتماً بعد از اینکه کارتون با پروکسی تموم شد، سرورش رو خاموش کنید. چطوری؟ خیلی ساده:
🖥
روش اول (سریع‌ترین راه - از داشبورد):…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4691" target="_blank">📅 16:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAliReza</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Vless.txt</div>
  <div class="tg-doc-extra">121 B</div>
</div>
<a href="https://t.me/archivetell/4690" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقادیری که داخل فایل txt هست
UUID - ADRESS - xxx.app.github.dev
رو با مقادیری که داخل ترمینال گیت هاب داده بهتون جایگزاری کانفیگ خام بکنید وصل میشید</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4690" target="_blank">📅 15:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4689" target="_blank">📅 15:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/4688" target="_blank">📅 15:50 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm9Feis372HapnLhrgb8rXVzzYjGHf8lSrYF2d4G-L31nmFFA2O_ahhpgdCIYZTKxwUp3nvV17u7XqmZaY_QPzZvKWAJLLLxG2_00iFVXzEN9NTjSJyiTBo972a-kC107V05GBKJf4J6bP19CfNP-gBMLlhwJziKRpjUb1gfaacAGnqSrKg60IZjWMYqb2kBO_Jj6yST65eLI1MgFVZnLcrRrAekOqD4Xvj5LUgTEZar4KEYZ7xe9A1r5KJ31rTIN9Dd7EP35JJmYPDm5Ct7mLPiDOx0kqZcrji3O7Q4VRdyDAQ3Nm7m2Am5YyyJY13BuvJxx-mjqNCdq7w-SvEzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)  ---  رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).   این ابزار بهتون اجازه می‌ده از سرورهای ابری و…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4687" target="_blank">📅 15:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پرتاب شدن اسپوفیا
😂
🤦‍♂️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4684" target="_blank">📅 15:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
پروکسی VLESS اختصاصی و رایگان با سرورهای GitHub! (پروژه G2Ray)
---
رفقا سلام!
✋
امروز یه ترفند و ابزار خیلی جالب براتون داریم به اسم G2Ray (نسخه توسعه‌یافته توسط ادریس رنجبر، فورک شده از پروژه اصلی جادی).
این ابزار بهتون اجازه می‌ده از سرورهای ابری و رایگانِ خودِ گیت‌هاب (Codespaces) استفاده کنید و تو چند دقیقه یه پروکسی VLESS پرسرعت برای خودتون بسازید!
⚠️
هشدار بسیار مهم (قبل از شروع):
از اونجایی که این کار ممکنه سیستم‌های امنیتی گیت‌هاب رو حساس کنه، حتماً حتماً از یک اکانت فرعی و دومِ گیت‌هاب استفاده کنید تا اکانت اصلی‌تون به هیچ وجه مسدود یا محدود نشه!
🛠
آموزش راه‌اندازی قدم‌به‌قدم:
1️⃣
با اکانت فرعی گیت‌هابتون وارد لینک پروژه (در پایین پست) بشید و اون رو Fork کنید تا یه کپی تو اکانتتون ساخته بشه.
2️⃣
تو ریپازیتوری خودتون، روی دکمه سبز رنگ Code کلیک کنید، برید تو تب Codespaces و روی Create codespace on main کلیک کنید.
3️⃣
حدود ۲ تا ۵ دقیقه صبر کنید تا محیط ابری بالا بیاد و ابزارها به صورت خودکار نصب بشن.
4️⃣
وقتی پروسه تموم شد، یه لینک کانفیگ VLESS مستقیماً داخل همون صفحه (ترمینال) بهتون نمایش داده می‌شه.
5️⃣
لینک رو کپی کنید و تو برنامه‌هایی مثل V2rayNG، NekoBox یا Clash وارد کنید و وصل بشید!
✌️
⏳
نکته مهم درباره محدودیت گیت‌هاب:
گیت‌هاب ماهیانه ۱۲۰ ساعت مصرف رایگان میده (که اگه Codespace شما ۲ هسته‌ای باشه می‌شه ۶۰ ساعت در ماه). پس یادتون نره هر وقت کارتون تموم شد، حتماً Codespace رو Stop کنید تا زمان‌هاتون الکی نسوزه و هر وقت نیاز داشتید دوباره روشنش کنید.
🔗
لینک صفحه اصلی پروژه در گیت‌هاب:
https://github.com/edrisranjbar/g2ray
📌
#پروکسی
#تونل
#گیت_هاب
#رایگان
#VLESS
#Codespace
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/4683" target="_blank">📅 14:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ربات جستجوی معکوس تصویر با موتورهای جست و جوی مختلف مانند SauceNAO، گوگل، یاندکس و ..
@reverse_image_search_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/4682" target="_blank">📅 14:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ربات انتقال فایل از تلگرام به روبیکا
@FileToRubot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4681" target="_blank">📅 14:11 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تلگرام از صبح با سامانتل بدون فیلتره
سامانتل ادعای استقلال کرده
😁</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/4680" target="_blank">📅 12:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmAvmCmceZ2QkoISgMTb-hGC8dpoLcmLY1tSmtEWhLvZCknR-Fc_chh7LxDpvfMM_80zdx1FUFyK3u0r4AgkkGmFkuSKF8JGk5kCxHpHfmNNwpUwwvpU-lpG2El_vDB1z2FzEABBhqy82sXMRIGxjkEqWGHlQ567sKffFreSFZh-8YJLBH1c_U9kYl9DYbdGNZz_nVVzX5NyoVKQdeh1jG2f_Iw2OVK09zJGCOYtoKov1drD7lqUI-edWiF8fTt7pJD1Bohm8LJHb54k5Q4zi0ljG9mci6eFfdvq66xjtY4yaphy_xXeKNNalKp1qDirTrxdVqok2kEGY58vFfuCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار فوری و به شدت مهم!
🚨
دوستانی که برای تونل زدن به نت بین‌الملل از سرویس «شکن» استفاده می‌کردن، فعلاً به هیچ‌وجه سمتش نرید!
🛑
شکن همون‌طور که تو تصویر می‌بینید، صراحتاً اعلام کرده حساب‌هایی که این کار رو می‌کنن مسدود می‌شن و فاجعه‌تر اینکه، اطلاعات شما رو مستقیم تحویل مراجع امنیتی میده!
⚠️
برای مدتی اصلاً از این سرویس استفاده نکنید؛ خطر لو رفتن اطلاعات و دردسرهای قانونی به شدت بالاست!
❌
این پست رو حتماً برای بقیه هم بفرستید تا کسی گیر نیفته.
📢
@archivetell</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/archivetell/4679" target="_blank">📅 12:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">resolvers.txt</div>
  <div class="tg-doc-extra">11.7 KB</div>
</div>
<a href="https://t.me/archivetell/4678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐️
ریزالور مناسب StormDns , MaterDns
☑️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4678" target="_blank">📅 12:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">استریم داخلی
https://meet.theazizi.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4677" target="_blank">📅 11:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.6_universal.apk</div>
  <div class="tg-doc-extra">61.8 MB</div>
</div>
<a href="https://t.me/archivetell/4676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4676" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">vless reverse .mp4</div>
  <div class="tg-doc-extra">52.5 MB</div>
</div>
<a href="https://t.me/archivetell/4675" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک داخلی آموزش reverse</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4675" target="_blank">📅 11:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🧩
راه‌اندازی Reverse با پنل سنایی (3x-ui)
1. نصب پنل روی کانتینر
ابتدا روی کانتینر اروان، ایمیج زیر را نصب کنید:
ghcr.io/mhsanaei/3x-ui:v2.8.10
سپس یک ساب‌دامین (زیر دامنه) از خود اروان به کانتینر متصل کنید.
2. باز کردن پورت‌ها
بعد از بالا آمدن کانتینر:
- پورت 80
- پورت 2086
را باز کنید.
3. ساخت Inboundها
🔹
اینباند اول (Reverse)
- پورت: 80
- نام: reverse
- پروتکل: WebSocket (WS)
- Host: ساب‌دامین اروان
🔹
اینباند دوم (خروجی کاربر)
- پورت: 2086
- برای مشتری یا استفاده شخصی
4. تنظیم Reverse در پنل ایران
- Type: portal
- Interconnection: اینباند پورت 80
- Inbound: اینباند پورت 2086
5. تنظیم در پنل خارج
- کانفیگ پورت 80 را به عنوان Outbound اضافه کنید
در بخش Reverse:
- Type: bridge
- Interconnection: Outbound پورت 80
- Outbound: direct
سپس پنل را Restart کنید.
6. استفاده نهایی
از یوزر ساخته‌شده روی پورت 2086 استفاده کنید.
پروتکل مهم نیست (مثلاً VLESS TCP تست شده و اوکی است).</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/4674" target="_blank">📅 10:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(Ahmadreza)</strong></div>
<div class="tg-text">دانلود از گیت هاب
گزینه آپلود از طریق url رو بزنید
Github downloader
http://uplod.ir</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/archivetell/4673" target="_blank">📅 09:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecda9aeba4.mp4?token=rlJUqgWgh9fBB9b1YxgquAtbKD0sI2bkrYKyU0lYS0d7QWI4tjqdzEr0gg21cjhx57qHrk-tJPNtnAW84VG_ahyep6YumM88a9Pplli5hmf7FVf2FRFvW7ab-ZZFz6i7rNKDUxGanSWtxFDo99cc_zQ2Ag6ctTbaOWFCyAR2xg73tAfkB9PFrAOxn2vDgw6NGf-G-D3AvECNk-5uk7MCHQFz21HHL3aVKvAI4aXeP4oZSnrg-us7fjLyztqV3WWKesQQzljdgVrO2RTHlTVdrVIS7G_sl06Es7VoQmgXS__8r3k6n-FgEvHTER3CKHfPDzKmP21oDvid6b3E9kiAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecda9aeba4.mp4?token=rlJUqgWgh9fBB9b1YxgquAtbKD0sI2bkrYKyU0lYS0d7QWI4tjqdzEr0gg21cjhx57qHrk-tJPNtnAW84VG_ahyep6YumM88a9Pplli5hmf7FVf2FRFvW7ab-ZZFz6i7rNKDUxGanSWtxFDo99cc_zQ2Ag6ctTbaOWFCyAR2xg73tAfkB9PFrAOxn2vDgw6NGf-G-D3AvECNk-5uk7MCHQFz21HHL3aVKvAI4aXeP4oZSnrg-us7fjLyztqV3WWKesQQzljdgVrO2RTHlTVdrVIS7G_sl06Es7VoQmgXS__8r3k6n-FgEvHTER3CKHfPDzKmP21oDvid6b3E9kiAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4672" target="_blank">📅 03:16 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ورسل دیگه R.I.P</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4671" target="_blank">📅 03:16 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0jgn7iPHkiqmk_8RGoWPWf8BNhZlTZr0PWjg2QWHcVSXqa3RI1fbbY0lz1ojrP7EYtufUE2iW7PJjolSAeZzimTaAG_6tCFLJZBKUSbUyHUDf6hLiBQGPGGfuwKDqZwf-yzURy1Yd1lPoKwp6zWEJVK9-nL-lPGQuA94sZZRV-ZFDd1g3ohSg2MPaqhLGR2t-5LFuZyYS-Z6W7DXS_3nMKb9yIxAB44MBJRS21sYLqn2ItURZOPQQrwLRfCOl0EQMUH4CwhFGWddEJLOnKExxMga-eDCHW0w7oSP-CefKvbuf433oQ6lE_Kg4SrZmAMxLXULpYv83sQo_9icKYlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لینک ساب اختصاصی کانال
⚙️
به صورت خودکار با لینک پروژه های اهدایی شما آپدیت میشه
⭕️
با شکن
وصله اگه کانفیگ ها قطع شدن دایرکت بگید
🔺
اضافه کنید به برنامتون یا اینکه بازش کنید کانفیگ ها رو کپی کنید
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB.txt
🤝
روزی یدونه لینک پروژه اهدا کنید دایرکت، کمک کنید این ساب تا ابد وصل بمونه
🤝
❤️
برای اینکه راحت تر پیدا کنم
#اهدایی
بزنید
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/archivetell/4670" target="_blank">📅 02:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya(h.r)</strong></div>
<div class="tg-text">tg://socks?server=STARLINK8.vayzro.ir&port=42528&user=%40Porteqal3&pass=Portiqal</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/4668" target="_blank">📅 02:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">@silnce_0_o @demon_0_0 @mwhamdreza @overhz  @heybaat پیوی منتظرتونم
🌟</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/4667" target="_blank">📅 02:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">@silnce_0_o @demon_0_0 @mwhamdreza @overhz  @heybaat پیوی منتظرتونم
🌟</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/4666" target="_blank">📅 02:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4665">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHbXHDgR-fuLQPWFo3nrf_iyVEFBXlR8ISZZsiiDTQLSDkuTzOQSjcSXNvVy6Z6xpQ956a_iJp7hy8Udfu2SxRYjSBRCVg65btf4-kRTYo_I2YywDnQwdmdpfS8pqaNhxRwU2fhZcoxWIkZq9hcM8KaKQRiLuy0kzlXVUxh5xqaXVziTT4DwA55GgCsl0XFTIXUobPJbDmYG2zMVR1R6Q1f-Xmhd7djAy0Hr1qECGvl7hmXTlQa1pXLsuCpSGcnAPMJEFrR0OJi_uQsqoQKj_oRWjmdEIb1m1zZ2wDejCrdtQDTwD-uNjdc2fo8ripH5R9ho4SRkJ7nS8i7i5tXmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه کشی وی پی ان به سه نفر تا پایان امشب  کاری که باید بکنید چیه؟ آیدی خودتونو زیر این پیام کامنت کنید تا ۲:۳۵, وقت انجام دادن دارید  سریع باشید
🌟</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/4665" target="_blank">📅 02:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قرعه کشی وی پی ان به سه نفر تا پایان امشب  کاری که باید بکنید چیه؟ آیدی خودتونو زیر این پیام کامنت کنید تا ۲:۳۵, وقت انجام دادن دارید  سریع باشید
🌟</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/4664" target="_blank">📅 02:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4663">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قرعه کشی وی پی ان به سه نفر تا پایان امشب
کاری که باید بکنید چیه؟
آیدی خودتونو زیر این پیام کامنت کنید تا ۲:۳۵, وقت انجام دادن دارید
سریع باشید
🌟</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/4663" target="_blank">📅 02:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4660">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">میرور ایرانی جدید توسط میهن وب هاست راه اندازی شد ، میتونید استفاده کنید.
High-speed local mirror for Linux distributions and packages
‌
https://mirror.mihanwebhost.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4660" target="_blank">📅 22:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دولت ایالات متحده رسماً اسناد مربوط به یوفو را منتشر کرد
https://www.war.gov/UFO/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/4659" target="_blank">📅 22:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4S8QtkbBzp61GR2l_1Zw4MADXwNys-RMRm7X_mLlvFcngUkK6xxWn_DYr-u5sYaRfNwATvx0bHLnFJ0LrRVSFBX2Z5KQDN4aopFqv7GEXuwbHY0Rw_m5eXNJsOm7OLoLHI-WTCp2SbEYgZhaU51xZ1wJB1Oho6rD6AyV5IkZK4oHQ8Hb5XTQ_vXVM84R3y0u99kED2ato1vlInsII7v1Y1kseHRwu0E1sVNaw1vD5pfjKmqVgy6sI_m_baZ7BWDMfTRSclDa9bIuxmtE4PSgc5yk2JjXiIxWcIEvdsJrnn6ilD7GaDPiAHhztzAKtgEMPOVuJ50n4f9mrpxTrdTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میو</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4658" target="_blank">📅 18:38 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دانلود آخرین نسخه مایکروسافت آفیس رسمی از سایت مایکروسافت:
https://officecdn.microsoft.com/db/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/media/en-us/O365ProPlusRetail.img
@archivetell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/4657" target="_blank">📅 18:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آپلودر
https://up.zaringo.sbs/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/4656" target="_blank">📅 18:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d632d4ba.mp4?token=QozgtRAzkpA4gpEZ_DEKMKkf5WwFNM0nhrEgYACXWcY52etO91BGFinbyjP8anK_FwZKs7thLIgq7h8NTyE7O0fmaqaby5XBiMQdu1mmCtf2C49zvSfSSepBWXpUhlw-Joxeiaujt2MwEB0y0pf9gafTmEuMSouPzf0pFFZEpFQZigI0_rB_d1WFa4QwU5hVIjGKOk-52T98rKqzIR7jsDoAoSBh1dpCvsuNhfTJxGSyZr8laDZsigjq10ZQm6skxAnL0yETnQ2C1EEYh7L24nM76WPLwDAD_D7k9g7Yelg57iWjaX8Dea_kadCdmIU5NWTQb00Yo6vfh4jOe27QyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d632d4ba.mp4?token=QozgtRAzkpA4gpEZ_DEKMKkf5WwFNM0nhrEgYACXWcY52etO91BGFinbyjP8anK_FwZKs7thLIgq7h8NTyE7O0fmaqaby5XBiMQdu1mmCtf2C49zvSfSSepBWXpUhlw-Joxeiaujt2MwEB0y0pf9gafTmEuMSouPzf0pFFZEpFQZigI0_rB_d1WFa4QwU5hVIjGKOk-52T98rKqzIR7jsDoAoSBh1dpCvsuNhfTJxGSyZr8laDZsigjq10ZQm6skxAnL0yETnQ2C1EEYh7L24nM76WPLwDAD_D7k9g7Yelg57iWjaX8Dea_kadCdmIU5NWTQb00Yo6vfh4jOe27QyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DraftedAI: مولد هوش مصنوعی نقشه‌های معماری.
راه‌حل جالبی برای تولید جامع نقشه‌های ساختمان از طرح دوبعدی به پروژه سه‌بعدی با تصویرسازی.
فقط مانده که این مهارت را به یک عامل اضافه کنند و می‌توانند Unitree را در این مینی‌دفاتر در مراکز خرید برای برنامه‌ریزی تعمیرات مستقر کنند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/4655" target="_blank">📅 18:00 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
