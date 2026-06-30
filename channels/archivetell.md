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
<img src="https://cdn4.telesco.pe/file/MQV8QfIv5h66PivvoKpqYQjDY6GLVOW-7vzZtw1jJbhNO-vRydOzyBWbcvoc5hgYMg6La90Ma7JEEraJIP-Cr8dZPxojHIhNoECT_drB5RyR8JtB_g9o8iQkUJN4QYZmyMsECSX-MyRxz6mpPJMRa7M15JV7yTbGpuWMmHmloH4EQfJJT3-qfI6fhrBSeXtgik14VILTlOb5csdoNw9mxqHBAR7-RrtgXSVPEulO-YacPsBvNa4Vj73a7p4LpmQ-AxFpkqXdq_Zm0WtRNrtYsB_nxNhx4EpjfjXqV56snKNg4L2y_H1i6KgmaI3bjWE9FBpwPz_JK-ozEs3QGyplXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 00:42:18</div>
<hr>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 558 · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 576 · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCRMEPCe97cu-6kPC2yAY4YqnTShPfR5ltIPTXibfkmXF5-xsKcp1gQMk_qv9r7_bGaMVddlTcsU0SBViEAiECA51pAL45QBwHB1wkM3mYz9v9HyyN--e0gN4p46z0mUp2vB4_1SGMglfk2oUHCqWx3HvMYAtj86-nHWH8pMhmY1S98GvdwEpZv-kVDzgebBAGKsYvU9j9XMEFXLYP1ol7UxbWe_0eU8by-rH_d4F99UW6wmQFxzmdvPjk566OnD4RM_rBkra59jtB8WwEd46uPf-0bJ5tUVMKyBcFx1xhc4drqP70UH2O8iFJ-NkC4ARqSsvYt_KIGkEV6_Rn0c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 578 · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 575 · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 572 · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
۴. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 523 · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdPy3O8C63Fgy7IczySvGLxPfMp8G4DyExkFCQe3CY9Mp4wtR8l3_JjC3T48fU-FuxOjevfjiPA6XG9s38w98YJG0qdgb2Pfs-Md-OzDqABHYktcldJ2UcEIj_5RXQZMOw2KgtwrpgX8L0EL1Q5Oky1iQ1Zhj6DYV4UU-IeaA9wZs29tVnr-XMGJ_ve5_xlKdqexJqh66h9C8yn-YHX--O23A5MaDnrxBFb4myLlQDEUV_AWHqjdCLFjTBiSgV7m4HEC9gDVfYDuELMEnfIL6o90k60YXaf4HnjrLdfdHBDcA7WYQeBNhUMJWkWF4Srbu2Nd59ZpthkPDysO7fBwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0liE6J2wFVU8Qa4sL2WvvwBKkhq7kcSIfSfmAgTdpCLdvMWOGVKkmju5_OUm_GH0ttVzdfr_TsrKhDBA64fquK5KujdhMqz8LVLz5l9hD0tSvpRvVtzRYsfsLn9LfIGcgevWAx2a-nPGwP-uxEZfht23vCgVa-odvlDR_mYneX59XKtU4eJQRwYXbiy6OoJpbKiE0CO79-SMPed42-fdxLGj1qtS7Yh9s1T4oPHeCshgwauqnWCh4_KJLMmIltMYecEhfPSp3FD1Tu4sUh_vliYK2gtaNgD5_RqE1dF7-Vr0TSkGhq4TPwHS_9FnEG9N9VhhvvwgOTPR01DE71drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxgVswh3Kmeex-hTaEYnb4bFwQPMUhrONvMN66x6UQ9upZxwgwnA0FTUKq6HiCelSJ-Uc0oBzLe5LuvD9K9jNPwM6XJVT4tbDh4owzJt7P0kD8h2VNcd5Q1Uwo9KOkTWyxpHt8Y9jHLULcb2BLiL78q3e_56otL42erZdL4LwP1iIuRiJnxjm8Dg8INYPYXJHabsa8o0PWLgtfO3PpWOjbXSetn2qRdzNBIJ9QA4Mf5WrkhmjleNjwi5gt_1eTxrGNQ2bKiOl1fxzOX2z-0opZJ0StMXRachyvm0Dq2rkIodyX6RoMkJij3_ZsHWp0e5GzersDBSTf4a2o5z6B6fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fuoEdYQp0DVqDBMqe3vsQRovPjLdpQFO11QXh9FQcRfN_9mWDq9IVMRZrjEdoMmlekAzPPgbwh17Ap4G-D2mksNyOQaTWniaFnKfUs1EWRyr60BorlisHXTnJwUvcnzMU4iVJthrZDaAevH577Gps8AKBm_pVJjdkTzlKlGqieAys3jgouP7EaT6nsir-MwE1gdRFq_0ULFt-vh7hn05ngE6V15xG4kXmujxAoXe-u7XR3908C5zgWpHG67cKH0DQ4pA8gjZhr0wsjbGqxDYIWHUemeiu0rUtex1Wbe63OmtW91iSGPvq1nOUPRrP4St_3nbgEJcgsQ21QIrmv680g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=hQ98wNWekNxAdZB8wzo3Mnja7JETLkL4amAZi3uE6wIl09zRaA6zYvG2yo5_VqGzzS5IsERCyZtuEbMEPqG1S4nkBgGzKcXRDXb9f_ku4uOWHoUJuIjiNF5_AjJq5WIlZ_OpokBSjQmmRMDIefYhCjfmQewrEweV5vAfqsmsq1mmwphDDQp3YuBEjoDFOQ0GPlit55K0iSt4VKH_hlM2qGAy1XqPaTKPIWnd4fei9Xs4iDR8BuIo14niPZFV6hSOO5wCztCDSjIGdINlNOfbnGErJcBzgvRJAmpzglnf5Z3czvBG9JEIVXBVR5B2uK44KP40wB59oVGDL1QXlji7-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=hQ98wNWekNxAdZB8wzo3Mnja7JETLkL4amAZi3uE6wIl09zRaA6zYvG2yo5_VqGzzS5IsERCyZtuEbMEPqG1S4nkBgGzKcXRDXb9f_ku4uOWHoUJuIjiNF5_AjJq5WIlZ_OpokBSjQmmRMDIefYhCjfmQewrEweV5vAfqsmsq1mmwphDDQp3YuBEjoDFOQ0GPlit55K0iSt4VKH_hlM2qGAy1XqPaTKPIWnd4fei9Xs4iDR8BuIo14niPZFV6hSOO5wCztCDSjIGdINlNOfbnGErJcBzgvRJAmpzglnf5Z3czvBG9JEIVXBVR5B2uK44KP40wB59oVGDL1QXlji7-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieCqFDQDCeZ-1dgrP7C22t12JvrTkfZca0ZunW06lCSPNgxKQJaGxEe4XhkBNW_ibh3D4D_U-EfLjuwFMdSbh1R0wDOqfTdG1u1P1gCorPpAeX7sb89s63kqnbMsvSsh0Pfi71p5FXCcXSgshct8XXSo68oPEJXvpAh5mnn0zOVNlwNDe4EKGR10qitToJkYcXQdbc41moM_crECUT09SvlaNVzp9DnwN4RYcxMHHAjiAfjc7obIrkZDyT5nP8_cj9zyTfsR3jOnm2ITAyjVUzqi8Aya2iNP-ESEOY2tez_XrcGgGDE4s5n3yj0PePyBQ7QO6I4qKqX9UkTK_d2BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=jzUzgtYAZ2qkAQxMspq4RZlNwpU17CnwOEFczjh5Evz16wy9m2rMoVJKRZ7-aPO_QsSqwF3ydZL6LAr2uFNjljpAEXTw8gYRS1WE1RUVre6QF_OQ3tX1SRbij8mNtQrlX6VUsgxExepCwTaM_kjM_jZ18El2-eg9vuLGfavZl_rIXO7oPFkNOb5LBhZFb9kQN9Tri4GrbbgxEfseuzvftJKx8sWZ76Scaypyrck9OOoHTXsaSdHRECUp3pyiy-Low23l6jTpg1M1rvvLtyfqn3kQ9GaozRm_gRKpxVKVT0tHyTnNMG8ZRPR5HWcK96s3cS6czhMxgM7kWAYttsUryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=jzUzgtYAZ2qkAQxMspq4RZlNwpU17CnwOEFczjh5Evz16wy9m2rMoVJKRZ7-aPO_QsSqwF3ydZL6LAr2uFNjljpAEXTw8gYRS1WE1RUVre6QF_OQ3tX1SRbij8mNtQrlX6VUsgxExepCwTaM_kjM_jZ18El2-eg9vuLGfavZl_rIXO7oPFkNOb5LBhZFb9kQN9Tri4GrbbgxEfseuzvftJKx8sWZ76Scaypyrck9OOoHTXsaSdHRECUp3pyiy-Low23l6jTpg1M1rvvLtyfqn3kQ9GaozRm_gRKpxVKVT0tHyTnNMG8ZRPR5HWcK96s3cS6czhMxgM7kWAYttsUryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKsJNDhQZ5el2Bnv34B7B5xYrpNlkzqR5ZoLgQVEuvurSkC32d9Yg-JyElzkjeDXLCYXjR6bxLO2WFfOtxBpQAHrbh_YZLKkQM0PSZshh2mA4ZuHnxyy8OH9J5fYtR3Ge2FY6qKDxhUR_lXsfuh53Zs1Q-ypSzOTDopuSWLNwQIM5-exHNp6xK1nf3fVPHMTNukKdrVEZHmjtPR407mzUEg5RCveH9kqC5kKDRxsskx0qcakW5CIeVzF615JHkd0HyZIHepYgy6_uTppEXVDZmXxBUtsq0EfSgSxf89B19O4w-pV7aQeZw0Toj1klzDfCjl19-R8ttPBSQSYQwTkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqhZJkZ84plUJROz7NkQ26vZs4VLpGX0Yb3fIuNtH-7-mccxp_vWEX0zBO9IZjLuF6zMJp2ZKhJaZp47rz0hE7yhb2kOJsS4UHvf8OFpi0A-6Z5YQAluqLbqVrv9f2rhyruyOvGMwcEGaX8dww1hQXng7o1scyyQHCrk7u5v1ya3jg1Wnmm6gMsUTmnmUGUw0rBTGvVJLWhl8LfNQLQe8CaRgSPhCAAASZov02EPcFSvyTtDUZCKpqHpVfg_iHaJMwi2Jb7WtaaInFzNC83e8njuwWrJLOCevZRov7_OyDePrSl0f2xRXbKsR4GqJ5xnnQp3CArkwd0T1jnP9rCjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b2TSyixxHrfzK6M2ffLCCBq8v-8Krt2UzLUAa-7RG7qPR7fv-L0rbzBI_3oOUCssICRqr3qMS1FjUtACbuES4OLOA78UpKONMEv0M5-FY5GYwrkN6MzF-5dBx7YmaqeKkgE5wHBYSZpP-TLv-vljNWGL06kF4XwrHAHxNREiDAEt5fQ0KdihD9NMkBxE69E-tM8aKTNFQrpvfxGqqKY4_V5VDcuer9lXlnWwoRDzwBa7tDIXcAQm5LjNNBftUNBuT--seN7CLSGFveoYAG5_vwm10uvvzIX3AziLlgJW21JhtkhQuvn5dh3FTe_Uv3gnNZJKbT4gb9SKD1GoSwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVBM_fNt3NnpPvHNWZ5_Bd4E4TayMbqKmOIGyb7KzOYh7I2DxvLQKb2mhLhoCA9uzSh1G_1wySnkfNYDEk5lgTI7lnKFNtrg_h4q2l0pHqKjhx4TGT7ufibB-svsuwu9MP9BCGbegZYppnT_9sXs3CImuIQt99leCKOgKhhoEUjW04Fs6KrvBCQaZ3pTf4eE8T0t8SHTAd2BkkUJbfSoKmigotN1yBQ5Yotir3-lJYnU1mNkk8r-vP2yWhYAASjA8atf23J9sPW-uKgAJoOgK2or7WS7RXIyL2HA3kgZDF41Ph5KSqZZI2KrlNIjT1PLu-U7sXXBAQFTDl8RjYdvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWwCtTz_BVjwwC1yXvHsGkBkYb5HJE0wS1fDmQLK2yW2MVXGzDIxamLQ2oFHBhoPHIeCiV8IFswGLjtwsqDZPt5G-Fs3x9u_GC0HGWIJxhoJh5SUciKK0xBQ8975dafUykNlGAIO5iQ_la6gDIwQ-Vs_YnQlLNnjHCBdfpVJPCftu8fZRDkHSOyY_vR-avC4X7KekpE6SC8DtEXpbbpVGRDVoszrzEp3JMvNkJkPNBV5x5RkjKs0lU3LYLYQIX7Lwl8MeLsOd2rKZmOE1GGzF2NhxAM6rX5kd7N9Hbxu307JDrUEeH83r1VPSMer6GL8Cp2T7yR8wv15CCIYP4VVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIT0mQo1L3r-ChZ70jOFTs0P-odlCb1IwB2iK0R7h7LgLNkfdkjtKQy8YakOX3Eitl3x3dc-l12A2qNwrfvSiBhT-sfPAC6lEPlfD3mGnvWUtMBaOJ3worwuIZqBgohavO59GaBAXxKu-hea6bgEQ17EPMQLRzYOSlXKcMHaNZ5mEo2zT7MfdSmZhhIAxHe2-_aBIbNF7EJo1FlOnw8yLE-KvNOjvOFRRWlma0uNum2JsZ1TOu6bkBJxzjeYHQMlzh39f4bpNn97F24klzfqOTPckfM8gCxUvABAeooazc9gTxBHQ6ayViUN1Zl4jTbMfN19WKKcNOUmxlV8ebssjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McTmd6--gk3OSkQlxf-HDnZ8BZohJKguK7xa8x5jdD_BEWogMeycdtcMvRuf45JoiOQHpvAUGnJhqsfa689iFKg-OADxKegEIMGMOUSafSHyKawHTezu0AImwDHXBfHf_0N-210zkZbDF6SKDBS3PsemDxBSMwJfxukb1mVJn9GgGtX_C8L92DAXzUB9ZkHp-VpDA5x2jyaWRd2TaMVnB3wtz77a-GbOtNloHxW24DG2TPwigxlDn_k_L63gmLxxwNLkJa_hOeoJEGUaw8ftCTcHz9-5rqy98QADp4W12z1KxyTo1D74zNFTIbOe0K4c5FdGr7lLt680lBJhXKuhqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckZZCQ-xfj1ebFre94PPkvWpSEbgbFGR3PiYc5TNKNPGhCwGa6DgqWXcVfI-UGdxBXGHmo3JeR6PODADedK7pI1E4WB-lMvkv9aQ9P8GFNwF6KGG0hxx_d5pksf1MYB1UPvRIQSIgZJGpWDquv2JdNCH3vuU_cWt4QkwV6Fb1QZFGFhgW_pOgnGbv6vGUJwPFOGNYrGbvu_b0qRM7JW9cV5LulLF849j-mEOnuXVJn8bqCFUefCg41KPbAc2zx5sXOhVIoZf2HlLnSFweSsRenlJgb9mByx-2bgg6aYXEWB1m7pGsp8spBLRo8LfkxDP-YwOpV99RI1oywJz77vFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=Qx0NJCqc_oQWENorO3RAsUS9q_nfUSonuWK7zXEmtiroUoHcKlkNDEGfC-Yfiej7b4eTllDKQb-3fZhMF01w9Bwz2YJdHY4IzaoKnDWCYlQX7wDsfIcmln7QboHcpRNIVT9F3DoMlMTc9mG54Ov0QGoML-036uui5Og8u6MPxu3FDT2ngcex0C-x4RP8MXNL7FzUUDpzkfkgecAj07tsFrklGLGI7ytOdezSanoVDiaCK_NawuiMM2HdpKZvKmLWZT1v1UC2I5QpudBffUKdVyhhQWRyf7D3YUQg6EbbN9wzWRj-E0-z6sU0DosBjX6ReP_Jxlip3YLTIl_J4AJ1LbLqwgZz4Voav_YOApFExKZcJXKtdejLwPwvNu8dY_F5-xUnp8q8wGwUGTd9ZtmU_XWSb3UeG-i6vxkRvDu2KG6Wh2A4I-ON4SHuzQh9A889GukiR3uSHUia4EPLYC8AE31BBhsOFXKY3dcTKkCir3fTj10EPbqKyZfcJpthrfbW4o6aGuuYm_jUx_d6XJyXzGIq8bl-M3jCS0xVDdJHGhR3awXmMJXY98LDvi70WnuB0EjBt0i7CTmghvgL7H4ATDGZFn5iUu3-YyBhpspDC8Whxi82L3pznfxlz6mpJNSidnFsJqERo3evvWG9j0tTIRyYYLDTKLCWZ6QYKgTg85w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=Qx0NJCqc_oQWENorO3RAsUS9q_nfUSonuWK7zXEmtiroUoHcKlkNDEGfC-Yfiej7b4eTllDKQb-3fZhMF01w9Bwz2YJdHY4IzaoKnDWCYlQX7wDsfIcmln7QboHcpRNIVT9F3DoMlMTc9mG54Ov0QGoML-036uui5Og8u6MPxu3FDT2ngcex0C-x4RP8MXNL7FzUUDpzkfkgecAj07tsFrklGLGI7ytOdezSanoVDiaCK_NawuiMM2HdpKZvKmLWZT1v1UC2I5QpudBffUKdVyhhQWRyf7D3YUQg6EbbN9wzWRj-E0-z6sU0DosBjX6ReP_Jxlip3YLTIl_J4AJ1LbLqwgZz4Voav_YOApFExKZcJXKtdejLwPwvNu8dY_F5-xUnp8q8wGwUGTd9ZtmU_XWSb3UeG-i6vxkRvDu2KG6Wh2A4I-ON4SHuzQh9A889GukiR3uSHUia4EPLYC8AE31BBhsOFXKY3dcTKkCir3fTj10EPbqKyZfcJpthrfbW4o6aGuuYm_jUx_d6XJyXzGIq8bl-M3jCS0xVDdJHGhR3awXmMJXY98LDvi70WnuB0EjBt0i7CTmghvgL7H4ATDGZFn5iUu3-YyBhpspDC8Whxi82L3pznfxlz6mpJNSidnFsJqERo3evvWG9j0tTIRyYYLDTKLCWZ6QYKgTg85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmwiptUFhoBdE96jTg_V7sySi-JDGmQEgbXG7EtjRpZG6ryQajfD5BkcTIoeNyJFURza8yGsyel-JAsNGumnSY0bf1PESZ6IloK6uCholbUF1-a4_3d1qzHs9tTA7sMhhnh-Mut7wPdQ80WVi6SswhSwuNyRPSUYaUWox5ExmW39b1nEaphUAn4stFNjE4pvFKDQV3Ig0MXpXBFmHrARIRJqQwIzi0pLYqECZHh88_PgJK19l5Lx_qqxHBcn9kYaF4QMuPBmhlwUxPQ4-RA-hiA2H39V7WbHluxN5aBX12pPzCMrGCD7d7_J9GWEa3Nk2sdcXtz4wPVVjk7y5Cmoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puPN3hOGgKGOjKOpcGY-CFCHay1aRyGoTH3U9O7yDMbnRzi-Am4LwOSs4fq7V9ofu5fbKr64IFClzgrdAJH_pmxvRH8APyGE_yNZVeVpWQwQPTDh5ypbSNNbahRve9PM_am8nBsExGZNiVV-v39fEXZVHfFapUO1akCZOoIS4v-26e_A56U_oFkJvPMCw_kDGElg3UhCl4Mo1sW8AJWOSrw8wuDwc_jer5d_PIS4GuacAl3rHtje9ev6mze9NnE0CKNKnOkZ87wzVx8Xw62DwG10ZEyrCIQfEatH3B70iSq8rKMgqy22XojhWvOC5l3ZuTlS-4jNkPS9lRc0dXScdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVxQN7KtWz8_SIwLxPN-h7xVGj3RMDfOLMP_DzDnZYElffZ5qwSMvtds7tm8X1Y-AkPXe9F5YeR7qthg69gl1mvxDag7emt7PscqVXYihveGv9Kh62xR3GVTJ0HQFzyDLDKnzFIMb42rkdXRZoXJH1VHP-peXvbSwc8fQJiFCwLA2BuumLCgmCH8eg1Nz06RRaO1uvb2FA_ylD20ZNxv8qff_2tBpfdwyqTmmOap5wqLIS7LfUnJ6LDsq11deT1bKVziwiy84mWl2NcFuCsLMwJkBvtaofrw0QnVy6tEsAoSL26unJ7s7Nm2to8JUUripNoZ9koYGcud1_8Wfok4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrAjG-CtmC1WvoB02tGpqwH84IPvKHdmpNR3GfBkJ9QpuPm1iPqHLG8kCQOywvHOSrIb8hL5DQPTo8NCJ7kA2RgS6VnEGFxbFza6SH2cBDN__BLxQvWqn54IW0HF8HHHuTHFsgOqotH0NVNpjASuydcTWNFo3pfH3J24p5UggGQsYazyCyBdR0sl2vnXgv-OT-cCnoRNHkhNb5aJ3cyjjlkb3IABOCCHnxnPAy18rx6kHBLBqEq0XkGtLD3H_Yl6Ea6kDmsq3Zj15myMTzDjrwxVgywDTpCoXHB1g-ybkOmUYY2sL5xg24VQfIoWaUxX11HOdYSmEVTW4zp8M-X2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Lqos1xfYjuEC4D_VCP5yMrUZj-upMcClphnctvtadcCJQnH6pzfiOx6dR2ADH_0vTD2PIVLxIkE6JMIVCAUMwlkzLD7OJCksmtkHf0eWXeCNZYfgQXlgkSGE4olXbZmz4j0F3Lxm73UjrugLpl41ado0a3PzDNGf1bBJZQDcRy4_fxjKhZY-ZnkpQWrd8d5QzsG8ZQD2fm5Y6xOh1LAkQJewewyTmM3k8inZnRVwN0f59KW186smNqPlu2jZT_fvSFQ-jbO06sK2ihbUAxycFKnfFJJy7lwaWOJ3N1YCNf1Pvb9hQA0q2QVI-zdd5lI0hn-gHKmHOa-n-cvLLIAUQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=Lqos1xfYjuEC4D_VCP5yMrUZj-upMcClphnctvtadcCJQnH6pzfiOx6dR2ADH_0vTD2PIVLxIkE6JMIVCAUMwlkzLD7OJCksmtkHf0eWXeCNZYfgQXlgkSGE4olXbZmz4j0F3Lxm73UjrugLpl41ado0a3PzDNGf1bBJZQDcRy4_fxjKhZY-ZnkpQWrd8d5QzsG8ZQD2fm5Y6xOh1LAkQJewewyTmM3k8inZnRVwN0f59KW186smNqPlu2jZT_fvSFQ-jbO06sK2ihbUAxycFKnfFJJy7lwaWOJ3N1YCNf1Pvb9hQA0q2QVI-zdd5lI0hn-gHKmHOa-n-cvLLIAUQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=NARVRuwMF-gBOzPr8uD83zeQ3uU_fGe-3GE6e70h3SgVshrNzAZ-UpC37GpiwG3u0zlyNjZCG8xeTNuEx_7gbTI0-mm4WRGNO6jIGm-uMwWvbRPfl-eYFwW69fc1QgFTto0BQQWycwG2qeOxAB9YJGYMPO82zUBnzOQLMK-gBC6kHsyvHLBzMAY_t5BznLwYu9dWvV65-9GvvyE4yT32qhQFm7Ikscijd7PdW7Q1dtoN4TQnKFbz0AUmyCGwYxgJn16DOpyGAm1jnUOKZZB1kC5j3IafhdmuxP86SVymX5xCY1FUWvgi7AgMMM_mFgfsbZtsmbj21PdiC54Gr3l5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=NARVRuwMF-gBOzPr8uD83zeQ3uU_fGe-3GE6e70h3SgVshrNzAZ-UpC37GpiwG3u0zlyNjZCG8xeTNuEx_7gbTI0-mm4WRGNO6jIGm-uMwWvbRPfl-eYFwW69fc1QgFTto0BQQWycwG2qeOxAB9YJGYMPO82zUBnzOQLMK-gBC6kHsyvHLBzMAY_t5BznLwYu9dWvV65-9GvvyE4yT32qhQFm7Ikscijd7PdW7Q1dtoN4TQnKFbz0AUmyCGwYxgJn16DOpyGAm1jnUOKZZB1kC5j3IafhdmuxP86SVymX5xCY1FUWvgi7AgMMM_mFgfsbZtsmbj21PdiC54Gr3l5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXG7NO7RESPiKSc4yqTmOI9fb40BO8E4HbCB4O0OkM0OYXyaADX6QyKqUYgIskOROMjCdEihcssOuvpLYBsc9zfmz2xQGBWRLXr92yONlKoYjufBoeX-vm_AxogajPTW5IAyL_XtMAvuJ4PHyqD6EkLhLy0pHnea2bFRYADoNQNieMDkimtJk7o8_yqQpxQ0oq1Ef82h9ws08H1CTbtPsBfsbInPxaQySOMIh1NdyLigYad3xhjN239fxa2AZ2M2cNhwdnuPNmQKxAIAqeTjpd9BvIN1MZAJsyhpOIYqm36mJ8G35bK7boBw49C_br4ccr2fvFAps4NOdscGmER3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkK-t5oKsYE-JxQjsqQZCBLP9mcc62abr5p4fKsCULOMhxpP9VgceDt7duM92zECHIsdiQ5avGgcgrnhVoZMrAhe-9fgnnjV9ROA8wH4OcpcvlhOwfkaj6Cv77-8m_lQgbuhvYXM8rqPFu3fwibLS5_m0HbnNBXSdx8XfA39563igfucODHCvB2VPT_6ZAfvOQ10hQnv9pABb0DID8lSGhfrIfWbwbz99Zd3WII2oAXyZrjg7n_U9i3kovwfagfm8nTJMgDDRxNxOKQB-cYMGjIh6fZt-rBxAjOa66v0M7NN-14ZOSUUtg3HE7Z1uIb3D6NJmVessVfE6wHEtFVRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo25-ZQkxCXJKy8kTBrW7H5Nn5goAUEo0sBJK86KAwC6JEjn-827BKJHMHe_ldEnguspQaZga3PwSTmQvlMyUwRt58vNXmkVVMFqr8MZGszkCNBg-8ug9hNYiSh2I5LQgI1GW2zQTIa9khYnFYGqjAQBV8rEfgrPF4AuyFDF-7088yfH2wr1iocxn8mNpKnYFi7RJy6cAeeDG4heNhkfIMhUaYVlVlYQAIvE-2IooXoZocPd36SSpSh9EwcLLi7u0i1T9ARs_DVFqZoHNACLCorDbC0Yh_O1a6fgzZKKVWyCk9Kw01GFL6AqyZRNYfN0I8kuxkr98eMvvgKdKrzg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luMmowyXJj9MVKy8rDVhw8rle3dbsEK2bU4JyEAPjqngSPHqkbEpMrhihV2fLDvv4N2ttdYleHU-dXGU6lSG6c4Ie0Ywo8qHjjVfk8f39QwS8bidgxiNiRqFVriNPFL9YaqONHxYpOcizl_0dGhnYkLpcjcG9FlBM7pSUtqMhgdWFRQIHuRh5PqYcDn85uezHCBuRTEkZD6A3bWsuHkmampjKHG2XykwAvFc5o2CafyI1dSx51uyzw6PJKLjkjJTQzTY_PC1KxFR4XJS7Mc8jJBOrwoKPjAmImPTvkq9Lm8kPZTdPjKtuln6SQ5O9njBnM55ydLMvMpTitA18lK7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBlHyuN21uAaETfVMOoTTU4wntnKH0ZBTnvpVuGMX6VYZ-nwjUKWkbbosiN23vDkfABpAm4dpCGCRCZbIysKpUedz4eHOnJ8IM_ICR1UdFV-YAxpLodZqLY3TCKfciKsNIWsOyIg55YcproZkg027adgJGIa0zEbkBrY-N2ozzlkdtNMNHqefnHyqMoC-y0y3KxqyXERPF7xAxeWuAh9P_1AJ-UTJfe2RvGMgiUSzn3ioz5Y4UE-RQo_yJnUUt_2_sshRJ7tykO07iPSRop8d0a90c5HCOhWN-dchj33B84KtUuBD0Af-SEsWK9AKd9byhlsWLxD7Tours8I9Mimpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6_hjcYC1bYQAqAkoAEGyuYYbLByUKLV_F95PiC4Metfi-kBVpeha-ljDEtIc05cIcyZxfKhidiTxEBSDG_z-9JVKCd2C8kj_4PhNuvAYDCFSHRtocRE9KhTtUJV09W5H9vRjBAQFrXMkOiIdWeS5iivLCiLxcPNkUb6UWXEsdx7ds0QFpZBv5PCMkXLkXVbC-xunc0QY6BPBcqJCJuwsR_N88U4oDXzDemGLMl2pvvSVwUHtbH4ZaEr6mB0J-T5ZD-7LJTD93TS6HY6fvpnyaDwkjKTmdy6rqgQ3DCdMeltV91s1YolAPuIo6Ryt3nSsyVpTagPyiZ2W9j2NUijtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9fQhbMma18_x8444Tp95i_8DvI6U750Ni0gGtdbT6EgPAjJnuW6vDFV7qxllEyGGYNDmgSP0rWUFv7DstiHA95CrF884H7MPuU9esV0inVcXMOapVVd7G8FKvZzbR-yRDNE9QM7jyoaAAGDWMYD2PbLj813ap-uWG3He51U10QXgRVHzzMECRyCBU69Rc55AtYRV0QJ9Ev_ZeFkfRJeedDou1c5SIdTyBwI5qFiJfEhE1C9dW1aRUBjXcG_ISV1OZ7Ziq3S5S077BbckvhorisT0Nx6Wp0b1dWEi_dqglGMYO4FZD3hQw388EwiQB2hrJns6nhUr24feaYvLvj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=FJIc63MWKhXjZ89OV3Hha1-KUzc6GvvnttYYwp3doquksALlvmLa8gp_CvhzSHwk6xnXD1zgeU_exRDYTraax7yqqW_K43XuqTonk25wj4edlJW1kk5KZQUgbadciFEAVrRjPbtOkOJJHRV0RMJeRVuZgSyXhuyuh1smVQzYjiuvJHwxjOLvKesfau_v-qKrRBMn96ahsb4bFBokB1cDMqgL96usRrpaT9xPvg3qFJO_Nmvxha-9Dw0tCllK9kFq4YCXRNtjOCdoF4_WSR94TtT0t0VaWiBUHZFZkNsteq3kBtOlElLRobony1Xf2LND7Ufxpfd4-zNRtV_sXNuEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=FJIc63MWKhXjZ89OV3Hha1-KUzc6GvvnttYYwp3doquksALlvmLa8gp_CvhzSHwk6xnXD1zgeU_exRDYTraax7yqqW_K43XuqTonk25wj4edlJW1kk5KZQUgbadciFEAVrRjPbtOkOJJHRV0RMJeRVuZgSyXhuyuh1smVQzYjiuvJHwxjOLvKesfau_v-qKrRBMn96ahsb4bFBokB1cDMqgL96usRrpaT9xPvg3qFJO_Nmvxha-9Dw0tCllK9kFq4YCXRNtjOCdoF4_WSR94TtT0t0VaWiBUHZFZkNsteq3kBtOlElLRobony1Xf2LND7Ufxpfd4-zNRtV_sXNuEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_DgSprKhikHJYBWjCV2ISWHgT6-2WPHxvuJf5FAKlMa0X2Ec6n4kBdkjzx3WIVoEQAVWyXErmO9JflMwl8qr7ak_PBmaYb62n9ugc_oDdbzxbfU_TzS-Ky1TRo3NYD40-jZ8qcUlLYZNaTL-owrI7C24uTQBz_Q8G3HOJCvWUg-k8Lifqj4ycbiaqyNm325BmSHjfMAJT__Qov-e491lhAEdsa7v8T590vR9uNxojixmt1pYhXXFGGpd9gMROEhobif6cqMnHCi22fEmKWxD2u_0hsPfmDcoGXVnujQRlfkdWcEnpQdM1vr0AHXLvGvUR_YfuJAOxftGK3GAWKAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKpFRAssUpIkcbj27AQ_c__bpBaGuS7ocUc5J0WFlVWC0BwID0piQIG_DhWSU8XN1TrXbDPCFyDQvSc18F7EjTDI1Aq0pCDfQJ4aDpk65IVIENzGrNn0k2500K3B6tj70IF1XvCXynhQfmrJbh5nPCWJ23n44AB8uJDG3kGWmt_lFyeOLP1Lkl9vZefxnnq7owe2r1ERPJAVb6ykzR9T0O0g4SCOabqdMQU3so48xyOT93SqwoY_w0-Vj8TZgi-QgHa0jPoSiZWJ_JC176NXCse9folMPxDQsdpsOx6Vo85Nf0uXL6Jj_893qSoUZZtyfypjgs8JpAddpHW6V3IgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmgvPAjQLYkT_EVo0IZC6_V1w_2jTdRNrOLTYQfSaagMbUQsYzVbquduxxTkY-Nwb8EIry0r_SVkbFizkGW20R-hWhtuXENrKDS1bbxFx512tYzCIXFMa3nP5znG6DtAbtPRszNZ2VcWddyLlxwnSoX3mBj3fkYtVO4rDii618C2izjkJ4mKQVRPlpQf6Vq8L-ui9hwUvrVwPOv73_EZB5BIWykeWX7rNH88ZIpzVSJ58azfy7goiwdaj4XlAPFuP1LEEDA9legE8Gr8H-qlEQiVTHJHsoX8WIiAHK7GeY1BB_zmQMqbURD0cRaoxzq-mJfGDYyOeqhJzvkUBdTfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6EGo7zXRtVSpjdhTaxtvjvpaC13xYr9YUV7uL5AHvDJNQOvtl77W9q5mDSXKEEI9hIeivebuMgk6qBpBuArN_zd70JjNEiWcZT9fkejkcH-arSaaw-4K7NRAINh8lfUKY2NFhL2gU40vuBQm7dopq7jVBpJK8AKASchzJaJGvp4UTE8ugLlpo_n5I27x9pFzarpyJ2NwaMxYrgr3zKk7OuJyiYZN7Xvelfm3zncQUclHUwvmAwpsYsNtfOSsQAkiF7221IGnpJTorj1g-E4QxNQCoqLeipDYqq709nDrNst4LB0unCtjVBUv-b3Shvnmqg4tWN67KO24rBloOERag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPZO6ZZUzoFyXyYBuhR_Ru40vsuYaa3JexVCxdS2xo01LE50NwK6vnF97vnbHojrGypj_QHL4zJYIyqKm1ebtHmc34yzVfyE40G-NfSiClxmtWfR5pf04xjuZ74acEyV0SyfbOfJ8QP8bzwuJuZCjrFBh3_nXnDdwJljjAPMIBfbWTvo3Etn62CA087_U-vllIEtPRvu-FdM6_7luB3BLIGUCzMk_4h8X9QY_FeCzbCNSpfE-fJUVRpEELL9QSYQnfcDj6nLSjehz83e08dMB00__txE9l7WesjCIG89F2oOT7kzbvcxGxbXb4f7mIlSN6V8yel99FyOn3SzXq3xYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIQV2il8L_Zc0b7TF8Kw1D8UQuCpccUmnvHoXh7qrKA3_tNuSqFOt3m9BBeTRuYVGi3MS6EEYjxysM62pIiEV11pP43B7wMecsZP69FmWfy-wExma_WNX1CN9veJVHaV2SyWeuf_i5jPwFm39LNuMmKqrN7G9s4A9LOj4ctlRXCUmF94V8M-uHPGazMBwOi7gsx1ZNS5HUhdSuuAHniMGhqjrtLA4cYBuARMx65vm6kdiRpSBI0645l-pLz33IxMB-PaaUglUC_FtimJmluTvxc8L5Rfb3P_rIaKf6Bd5DOvW2_yRzuWLCMQ-oiJP6KDWAFdVak9_gr-uPleLDP3fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJKmsEiG2ArM8nT_3PVS0kiXcad34zTPEOdT_OK1GVmvnIlD4YpDeVGzXCD54M2g7uX-F-2ZhxmvbKgiWu_lHEmofiA0KIqKYc21_r7nr_GU6C1fpBeKUr41xkgGHVzXOG5GpfDIdTdENFASo7ygzKUKZez2ikE03qbheX-rqU4xfbH0QAwmD7nTqmBevw41mya1pdELn3sYStDjad2W6JISzuYp8rZhmPBTsKsrsITe2ueaSunuc0byo1ckZDdoMRhuXsVS1H_JtxGy2M33r8GK4DOF3NKWpv_5QlDz06ZjXeoUm4ZB3UlBF1MQ6ewkwqbiGcRFSuwWMi15cZxRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=YfiLLQlEZa20L4NvSq0OXlTw0UcHdPTlZNFrNkyxWU3dWfhTnJNTc6B_cgcsNXioTcor5aAqFJbhkjRMmIVpl8nzn0YET8YNAt3f8aYyjf37G6wZRq6AW5ctqHUHTHTmSz202fVbz-ralPsDgDAyHYzq0uFptYDlJAi0IZamWd5Nx6mng2KxU_4CbPeHLNWNOTj30lY-wx1aweia8-Okmn7Uvx2wfzpkFvulQaGWtibcrnDjhNcF5a2nJ3mlhGjxGp5uvIEBavytrw038zbUBhl22gjvnqOHt2xq4-u_5GoyR6myRTQWJY7s5EFXX9VWKC5y5JYVKPVwldq1cC1Ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=YfiLLQlEZa20L4NvSq0OXlTw0UcHdPTlZNFrNkyxWU3dWfhTnJNTc6B_cgcsNXioTcor5aAqFJbhkjRMmIVpl8nzn0YET8YNAt3f8aYyjf37G6wZRq6AW5ctqHUHTHTmSz202fVbz-ralPsDgDAyHYzq0uFptYDlJAi0IZamWd5Nx6mng2KxU_4CbPeHLNWNOTj30lY-wx1aweia8-Okmn7Uvx2wfzpkFvulQaGWtibcrnDjhNcF5a2nJ3mlhGjxGp5uvIEBavytrw038zbUBhl22gjvnqOHt2xq4-u_5GoyR6myRTQWJY7s5EFXX9VWKC5y5JYVKPVwldq1cC1Ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFjtwFMu2u710udCJMalmcwIe6l2gdMqef3vxnZXw3lcGGutlIsHce5Pv0yaCqy2dJ_vEg0P1CtPU9s5Q-e78cqhBttwSxARZ3ba_1CWQ8TFhXXCCFtTXz6njSi7PDs7yDPDHAH0Tql2ob_21EAnJaGGxObW6KhnwmibSvhzLSQQ-dMQrgAQs-43VxBdB3TbMAIL9KEqDwcwXO6uam38GonfLKjW6jrIxHiSaa7jgGjH9w6myo8xkJANYXCF1bzdiy6umzv0E10IkctyTdnK3SEAjOcLAZCmed19sU0grukItBBnHk-xvdhl-MfvUl0odpwjJM3O8nF85LVaWqnLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snLcdcU43NPMP0KePdRT2gzYL6sutgyrfuXAofx0Ry9BG-xtPVqXpAZgNt-koyCCPpfziSBf4c1HZ40GEIUC52f0DeHlxm05PomwjlkJ04DZKMGVAPjVdFW0odyagkW5V05IfsmFHS4Tt7qQIPQeAjV0N6SIF8VWpx36euMZZv_Biq9--gPs_CN6sB5GCi-oNHDPyXj4cSbD0lO6oLpqztvU21OY3OL3Hcs5xWZs2Toi7L5bThZLshO0cvez6g5plbxSBaAzha0yyVSRmXF3OtmCk202IFPLRbfaLBcCaNicTr6bW5ymhui5F-akQfXbtV0mQ86qlshSrPR4q4tO0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqV0jCg29jHx8t__eEnlUUd1wjWeYHKsgCkTf83J_hS1dDSJT0PDxt506SmlgVtr4s3JFlZNNz1iuVNGFtNSsORvZbxSv8-iUuO40KpdsT93eoLKxZmsoIprzp0kmMtnbVLhvGsZEx6CHJ3pr_HVIErV230ZrBDk9u3AB9EnmsjVQLaOfwFsyZzfaesIXuq3g27iPb_WVwECiPPrjlWVETRlsPzB_aR1JA4Iiw_2PtGFggStWiamqU1ir1s2a6Du11LhCYZItptuB1XG7vVlsLbqYPCENGb0zIbfoJO_UJGTMEu1y6Ewq5vxCgV6T5J-9pmG28zqEenWbDfEFraxoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/piTbOeX802QmQOqsnS1kZaR8eE1E6cUOUNNR07A3kIRLjE4kcyO7f4WY0CNPiZvYX0vJNRna9mIu2SHTXajdmbcdrP7lZIQZFPY_HgI816_c52aEuvOXWLl1kKjNoIuoOSg6pI0xJ5zEuR8IsmVtjLjmWZo7zQBbBJFyC99HBjf65rY6XnVAEyQ1rSC3u0ZhDIoEy0LcWI45FlZph-HNTtB_g1dNQdLma40_pSuaGtnmrL7t5Y0Hgz3P04CUDrf8PzIODNpgv4XB9oNMfTdwgv3xKQRd0xmvrHGds3tqML6PU5bYeS91wNLQSZC476C-JtbVf8Y2ZTWiKTpFD9F1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmsft28Um3OIFWMA6_2XE2F1jVUoRnceZPERmiUmiE3JxAkKIlTxToWhovh5sZV4S602_HV8CgTcoddtELOw1mxlC5iedC84esoKLOjcqascttp4A5-KxaladZm2ZFfu4PLGCBlSLokomOfTscok-R5Kik6cWKXfU8OO1bJlR4218BwCkRnnHe8JV0Vqj5BavBbVJ2R76TaU-sQ0P6TOpHhQX5NZzRKs0y2XdFJYrKeVAP5C2DT4TJPAkvJGhIt_LEhjyDTFhWYWousowAzz8wLwEljGlcyI7cxR0F6fZjRTMaS0j-NaWqkLJRzhDfzJo02oZny_L3mXyJh0s-pw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t94Nhf5ozYVkXI0wQZQhJweW8heJt8wK5Pd6TefLRcw5rxkPkbvxlUxcYV6-VMmSw96wG4y7_xTWGiBzXbI2dOHiFtNmaW0mui_Dd0UVgmQ2IE4DNgelIQVuasi_vCoqNTLMxyDbxzhzdwlpI8SZncEAZ9doGLxR4IOaWkqG25pkhUH7mDVGlHyTm6aBqOwCuEpuhSxvp0iHl1tfTwvs6EiylycIOKlcOejwFzpJOhDJXssWF-kliFfXZqfPPBPCEIFP6BUSHy7PrN_cnJcRHmEZM9ihR21YWFPgDvlYlc8pP8A3e94PZjvTL1RYJ4_KomVEqxsY8EjpMbb3CBmbNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=pwc3d85UHlDpONAbc-9VDmW29IUpYGU2UfXf0nL6vn87zJliYnxOsoHqE0P7sXbexJpj9qsCS6hwtzbqUA2oq9HXGo1dH4lSELFOJUlH5ecAxTVHkCRPwfQS9vUvL2uipXJ3ib12YYf7kr7ONbC-JZlQhnn8qK3m9NL5i_ew2Cgv8uOHOc8d1DOjWIkHdhZh9KnKT1nUOGCG_hehseYm90RUPFik4YtmAzGprGMgDF7UCwirUu2FN0rzCpuUtM9EYg0g0jiNtr1hZuCeycNRH2q2YO_v9KLBbJJo_-lb9q6PXe9zbVGvP1C04i2yeIlKZyALmYRCkxy9mOF4nu4PsqPnSPs8EMHVOX5xHcyPwCzndPEPADx9L8r5ckfY22Awr9eq50d6QU2igoFKjbH_-IPrGVSlEkz1qtXccaRv7h6W8BxtcYITbbpWv-rcldfXtFweEcpNFT4T6JytYvZVTvXUOZHR7JcVRVhDpW9ju04tjIMKzNY53FA7Gxw6iFldVduMMxMrZMznkfiQb-JdlAhPXfqv5VkjhyLv5iyOh93dfW79MX-AfNEnhUpQqn55JgP8z1oKXNVXLSxZf1Dcr0NehP9Meo6YY1WLf0DoQVwGZZKHF6hIplKNDZ9vxNZiwuojqlI2d57sDjW170Av_PvG8FimYELbMEgvlw46nEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=pwc3d85UHlDpONAbc-9VDmW29IUpYGU2UfXf0nL6vn87zJliYnxOsoHqE0P7sXbexJpj9qsCS6hwtzbqUA2oq9HXGo1dH4lSELFOJUlH5ecAxTVHkCRPwfQS9vUvL2uipXJ3ib12YYf7kr7ONbC-JZlQhnn8qK3m9NL5i_ew2Cgv8uOHOc8d1DOjWIkHdhZh9KnKT1nUOGCG_hehseYm90RUPFik4YtmAzGprGMgDF7UCwirUu2FN0rzCpuUtM9EYg0g0jiNtr1hZuCeycNRH2q2YO_v9KLBbJJo_-lb9q6PXe9zbVGvP1C04i2yeIlKZyALmYRCkxy9mOF4nu4PsqPnSPs8EMHVOX5xHcyPwCzndPEPADx9L8r5ckfY22Awr9eq50d6QU2igoFKjbH_-IPrGVSlEkz1qtXccaRv7h6W8BxtcYITbbpWv-rcldfXtFweEcpNFT4T6JytYvZVTvXUOZHR7JcVRVhDpW9ju04tjIMKzNY53FA7Gxw6iFldVduMMxMrZMznkfiQb-JdlAhPXfqv5VkjhyLv5iyOh93dfW79MX-AfNEnhUpQqn55JgP8z1oKXNVXLSxZf1Dcr0NehP9Meo6YY1WLf0DoQVwGZZKHF6hIplKNDZ9vxNZiwuojqlI2d57sDjW170Av_PvG8FimYELbMEgvlw46nEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=drqhuNzzGj2cphrXGf7L5PMFL4ceH409fUU485E_NZb9SzT5VkZbnE0OJVcl1Eu0nOVC_MLjRb2D981eDGtuaOAk72VdVHbx95WTktmkygEi_iszgsWzcDJMC5dNMh2Zx_tu3mPCA737I_D-hTSnW8J0vCxsxQK3JO_buh6tPzYFnj3lUsklPT-JK1HkevqH6DMMsfg5WE48JjZJ13IDTdldP44SW3redUfn4JOtkA52qLjOrWI6FTKWgF_cDZ3OY39mb-vGlg6uB2P_82_ZKPtkRGwVNCG9q-NYh8C7EkIbC_CuoAH9jLtxOtQ3VqH2qbjMWEf1FroK2SPhXFCXqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=drqhuNzzGj2cphrXGf7L5PMFL4ceH409fUU485E_NZb9SzT5VkZbnE0OJVcl1Eu0nOVC_MLjRb2D981eDGtuaOAk72VdVHbx95WTktmkygEi_iszgsWzcDJMC5dNMh2Zx_tu3mPCA737I_D-hTSnW8J0vCxsxQK3JO_buh6tPzYFnj3lUsklPT-JK1HkevqH6DMMsfg5WE48JjZJ13IDTdldP44SW3redUfn4JOtkA52qLjOrWI6FTKWgF_cDZ3OY39mb-vGlg6uB2P_82_ZKPtkRGwVNCG9q-NYh8C7EkIbC_CuoAH9jLtxOtQ3VqH2qbjMWEf1FroK2SPhXFCXqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoeAdgUrKlc8KA6W1qosB6_hS7ruCkk0Qi5IFTBvx0SIRMl_JVOR0F0GjmIUbq6cRujsjL6FLuC27LbaXaRfXIE6TT-tDu7uqlScxLEiJelf4xLrRjPn3flunG2fLr4TbeSH1DklFTxF6xTKYbR0HOGP7qYdsx683_fX4Ej283KImXLwUWADTq7UkAaa4i2x0JWGKta5cidinDiFgs1OeBrxmhL2XpjJs2MDefsYJr9Qqcxvi3NMUH2jUbsudfMLXKXX2oweN7X9VDLSwAM777w3T9OhBN5fKZPsT1jtpUvWfD_IDWscnWdDl3xF2i7OiGbmNN4qT6i_6eWwdXOc5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=SQRhDkTVrfGZ6vuePlnM9s8T4Mwdeqn8AhVspvr0CCm5y8DLp7B6HWB-p7Acsp9GrOv3UMp_ibmJFGnwC_6YC0SfU5XYgl9o4gNcWS2HqgkOd63X9v2bxAgrJw-Rzj-1ns39cMDgTnXDtbnEZ5AGN22faWKJNmghimMszSnD2g_6S3i-bOP8_jzeuNPlXVMdvjrfO70qRPxKeqs2tndL3rcAmUCPJDLsquY72gYDx3fTFUexMaXTWiZ9RueerT2oWzFQJzSXP9BxvUVi2YUesa9Bx0--vTVDEL5aUY4xN98F9aBwe90C40rO4XpghbxxXyTf6N2MgxgyB1H_LfsTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=SQRhDkTVrfGZ6vuePlnM9s8T4Mwdeqn8AhVspvr0CCm5y8DLp7B6HWB-p7Acsp9GrOv3UMp_ibmJFGnwC_6YC0SfU5XYgl9o4gNcWS2HqgkOd63X9v2bxAgrJw-Rzj-1ns39cMDgTnXDtbnEZ5AGN22faWKJNmghimMszSnD2g_6S3i-bOP8_jzeuNPlXVMdvjrfO70qRPxKeqs2tndL3rcAmUCPJDLsquY72gYDx3fTFUexMaXTWiZ9RueerT2oWzFQJzSXP9BxvUVi2YUesa9Bx0--vTVDEL5aUY4xN98F9aBwe90C40rO4XpghbxxXyTf6N2MgxgyB1H_LfsTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=EYYCvOcOBX9YeWYqX5uS2iWUvwX4LxdWE8C5c_BSJC2XDXkLFyUCKjtEZhZ9pPg-IeDh8lr24bbxKzwwhRILM1cMHq4nAUgNhuZATIMgiJNsLAVn1Dqo0niffklMkbkak9i6LKqiywPJT_8aQD9PONNVsk4Ib5Ecm0muOF2qIPBwPt4PLiGQqFdeK5pKvM-Q2oJ7E2A2A6Xn0Bg7gzY_QbP9I2jQqJEn2ufK4_Z-NReIAK7Rm5sZt56usES8eUS0O-Qww4k_UUug4V-AJGwD-jMQs1rCUyWm1IZ2RWjF43cV-hpPz0n4s2nSrOIJF4Pm7sjVOYnnrfd5CZFkrmUGfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=EYYCvOcOBX9YeWYqX5uS2iWUvwX4LxdWE8C5c_BSJC2XDXkLFyUCKjtEZhZ9pPg-IeDh8lr24bbxKzwwhRILM1cMHq4nAUgNhuZATIMgiJNsLAVn1Dqo0niffklMkbkak9i6LKqiywPJT_8aQD9PONNVsk4Ib5Ecm0muOF2qIPBwPt4PLiGQqFdeK5pKvM-Q2oJ7E2A2A6Xn0Bg7gzY_QbP9I2jQqJEn2ufK4_Z-NReIAK7Rm5sZt56usES8eUS0O-Qww4k_UUug4V-AJGwD-jMQs1rCUyWm1IZ2RWjF43cV-hpPz0n4s2nSrOIJF4Pm7sjVOYnnrfd5CZFkrmUGfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJsQR6wBY8dyS50WU7zt-l8FSkFj65BPPMArOXzni6lB42KVO82_c6JJLF7RYBEcZFMMq44jdiw59M3Emw-kU8BW0x4CLVYusMAyjutg4ob2PPskxcpUGFwYDLZXQrhLJdi8eNMEDIluYJTpqxHEg87CFMZXsUVzXUsBe4k6__-jCtB9sTQfRtP1LxT4K66w7_PDH6JPxxiRFuw__K8r0TOzUYJiox00a5lgCJ5VkCl8NQJ6j1zTml4u3lfEmGZinjv9aDLhUWngT3VOdMzIAKBDjo9UqwuVzjJDU-N5xsIX9wpAYihUGVsFfU0YWXBpaY-DVNdowT4NeDeCn83Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbS43o1Ko8zfwyk3pzADE6A1gnu5iFdSaOZY1Ru2lH8koXRagLJRQxk8-ulUzUK-4HCbH28DrViKdNAXH0P-QY3_PDCUnGdWQxBHMcv146_pIzR6kzyyAzOXV4fRKZEubEqLa_WfHWCIO9uALAbp9fbXS7xeOa5-GOUAicFwmedvJGMq6p3ql4QAkACJP_hZGtOAOgUQw4MriDGUvb4fr8XWzqgI1tZLa_LZKnSY5OwOX6dWPJe_xFiSFGKlnDSBrfrilzhJUGvOnsBrhNZNdQ0fuguuwDKnII9zFaXUXjcjnhXn6XADO26ZehnY5sdVJzW5zMQoBySQ1ihss5dH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDef_lStV4zO3nJK2FWOwmmBV1syINiq_e2z0C5K6E2J3jUY0z_FtIzzV5fEpC50TUdNliwfOYLLj_N_-zMcplXHiZUQrqAfLcP8myfgiQe0KHA2nLDizW4JtNyR02esIBXx4_Rc4PjeqRV6oIDFQvo9gMi1a8iAE0MK66dP9tTU2FrKBYcJiL9CR0Dg5vHUzzkg6KKWMma2R8evpQrf6Yf2uN0nHWmBAU_2t9O6WG8OodRvBYKmk6-Qe0aMOO4vRWQ47cr2EX1sLlVqcCv9xnodrPWiZSXJb82-UKV8wpHDT6AL_hewkOabUw1EJokyb2L0ODITZDdEu4ltnGmqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=Q9kzojV2uTxcCcl_n4tMeaP5Aa1c7mg2HpuP-G4LHkZPtF9qw-3ztn4_x0RvlBTeetFJmveVVVDTZbRfzpNpR4D-h8qe2CBLG6D1QCKdv3HA9bLuvOSG6_Hbay8dVjqnOgy9e3ggDO7q-thtqKsn1HsjjnnqEx0t7Ow8gS8t3-sKe4k0oZccZsrej1Hjfp6dMSvslPNUOe0tFeVpqplWlfgbLQyHL4BI138jkmnhS1b1ldENYFdEuT57jchJpPxgotB6GTj42qh5cQ54DbjJgptrN6h92eh2f-v0ecQhnUuOAfknH9UvuNerx0Ib4q1h_bZ0vI-NuY-EkTH9OUjwEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=Q9kzojV2uTxcCcl_n4tMeaP5Aa1c7mg2HpuP-G4LHkZPtF9qw-3ztn4_x0RvlBTeetFJmveVVVDTZbRfzpNpR4D-h8qe2CBLG6D1QCKdv3HA9bLuvOSG6_Hbay8dVjqnOgy9e3ggDO7q-thtqKsn1HsjjnnqEx0t7Ow8gS8t3-sKe4k0oZccZsrej1Hjfp6dMSvslPNUOe0tFeVpqplWlfgbLQyHL4BI138jkmnhS1b1ldENYFdEuT57jchJpPxgotB6GTj42qh5cQ54DbjJgptrN6h92eh2f-v0ecQhnUuOAfknH9UvuNerx0Ib4q1h_bZ0vI-NuY-EkTH9OUjwEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QNVQz2fGBKlLC3USMcn4vmi493SkSLFsfkpsbu1pYMs332Gu56aCPkOoFvrArmkQhmfq3XiCTWMkHkH6zFKQzeY39WWzlcX_xA9t99X-vVEYXEIrNI4ZSIwZVIGFDK5bArub-1MNOBGiZyVy14sxPfebmv0otpUx16v1JHjJlJoJhqVEqHkMR14VRC98O2uONcFU5hpJx_xpdnInz_bYYzD9FgtzZjXt68YZLny1WA1lxF4JX-LA24W4yYFhAdI4-Ok6oS-Psti8qiRoJWTTiXLubg1tbk5Y_eE49qbqnHu2uwo1t2b5PoHLKy15wdQ-O3RDdVTeKqVK7nb3k6-rMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QNVQz2fGBKlLC3USMcn4vmi493SkSLFsfkpsbu1pYMs332Gu56aCPkOoFvrArmkQhmfq3XiCTWMkHkH6zFKQzeY39WWzlcX_xA9t99X-vVEYXEIrNI4ZSIwZVIGFDK5bArub-1MNOBGiZyVy14sxPfebmv0otpUx16v1JHjJlJoJhqVEqHkMR14VRC98O2uONcFU5hpJx_xpdnInz_bYYzD9FgtzZjXt68YZLny1WA1lxF4JX-LA24W4yYFhAdI4-Ok6oS-Psti8qiRoJWTTiXLubg1tbk5Y_eE49qbqnHu2uwo1t2b5PoHLKy15wdQ-O3RDdVTeKqVK7nb3k6-rMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQZoyRdAJE3xkKkxWD74ZFryD6ZCm1A6bPz_KZAkEivmYGB_tSHUhBUG7cu40oVZdv0UlB5mlx4u5DaeD1I1yX9d6wg3TCVsy74z4ikTuzT91s_4ArVJZ2c_AP6rPHFxcbpG5V381EhuZGaqlVzv2P1heDwy0g6FoRKFOa2yfJBSYc-oIBeAGik3EjiFm1wkPWXmP4tIuVyNAvhLj9cgbAHWFFSu_QYRHdh3Phz5PewtYfSRG_zP8IcrcRmpzs8RGvJbO7TOVXFNQDRktbQ7JMg8di2dIBMOfZmsGpHW0ydy7pOFc0Gwd0F0sNgwNv6i5TVS4ARMQhEaZP28kNsDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPBFDCHupaP86Y8HVB4zOc-JRrxicoji6mMUPsKrCaWPVoyeszaW1VxgL2o-Zbmg0ExmU1vgXO3dwe8a2XZ6N9cT1ytWYRQg_VNHfir_m3hR8J02vNl1S-cljb-aUVlz6Jk0yk1DZEyPAbT0KTY3CKZHFX0tudKMqOwAPiepHXZcviPnhQ9a40M9fykWO2UTJi-CQoUpqKZ-UybZ8jWW0Kcr0AJ-_RYHNRiEGf8oACM2VPqDB15984JCZzkjhvcabDd8CNAyyQZLBF8FhWvZQ5wSwPrvqZlik0RtSpN0quw9lhzN3_ekf7MBl4KZJpYyIjaiQgOtLgqmMN0zuDT1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6QSECEjCmtxeV9ZjMykcrIEDDEfdh4D12EIxDd99mKEA9lHEUxLG3UJhPv8Sw0ThgPjguLyggpY2A0jND79hRvBP3XWhlKNnccYJ_DxjdBqqrCs5Kp_ZiAUzonI8_bpBwD_qCfx8OvDyYrf71JdorMDkfyBzdEvDWEa1ielWWnXTMcOCtGRaS40KxfB7f7HCSqK_OGaBMcD__GBRBeo1ufj8hltAVRbNb9kg9gBhtrn7vwb-PFaphF85CUD38BfO6WbGKD-qudQ3FJ0dEaQsYNZYBLbFX9dA7vaunfAYiRb5pIuOS47VNlEniRUHlEWz18l3BwtSZ_uacxln3ic5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbcZjXzfeBetzIlcuyCDGR7m7GLwmJZdLHKhsiJsE1uSiaPYYlL9pTLMQF0eJ2UqysAWUboucXxtShvtHTFS09ll1koMOmR2C2oqfJBbZ_EId3RcpTIWXWH7TYLaFXxyRtl8K32XgQSt4JLRgjolNkbQUcNii9jhYT_QLlssjmFHQmMJm8cKOF89v0HhK8a5ceaSCPM6z87dKu7zx8sVYpKKwekuAgxk9lio0Z1t3L-sbtRy01VJje6TpHrM0iQ-NdrOCSyd9YfFANGoMwznrg_UvEJFa0AdO3qVIjFfV2qGOxAOpxcrirB5iXC74BmUsYR9sYmPAhobYjogR_2_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n917EZ7__UlkL_R8gty5Y1x4GhFuxXnWHPuN2ltknxTM244q6Yol8nE8skO003f7F3f9BDXPG40GIuua4HlhyMld2GOXrRO4mGlOg-aSsdw4Y3pRfVJOEPAcuaakzn14zrlFma6g7kfWqOiIiEuy2_xl3n0HMbMe-AFFLRPxxUVFURSEIZORkPVxz0Pp4WXgJFxr7E713x1smTvWfvlxx7CT0w2CEA0bJ6wvur2c3VUfCUgJdipV26eB0IDHY6uctWP77SBKFILbQzkmyQWZ4-9kPTtVMKLr1DYG4zFadjO0je4GPNAs2peRz2OjyiSbsnuT70A7esaLyQHjiH8SZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or9r1yZkZU3_FA98IsvQZtM6zXYvDA8lqnXzVyF5pfKgwuugKgg9N645CtzCZPSrpj1BbmbRbhYGpaM1O-GJNLG2QPAuUKQzs-6eEqwgJ4hA85XgYqkSW47dUc5SxI6OmeLH3jxx-pwXZg3z79K-J5yOVSHE8OluhjNind9GLirbi20KK9G-O2wuRLOv_3QZiLp6nGWICBpcOJmkjREJmbeYySy9-hoG21k5qIMBbmDg3l2CCr45HTEmh77_Izw8GVaFgq9wIdTLuRQD1vFDDrSrWPSYt4K1vtyzDxUa649wKsqVtXyJ6flkvvsxoyZUFBTJZwWAS6VSzhTyU7BPzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2MSxTtGl7GddirtZO4sEqN7aiB76udvgP2dfsA5bwZLCuXaD4vYpXQ-7BkZvHQ3d4TNlYSxulT0qDtx_gpF3SgN0WvIRw-EtKLaNXtA6TDZNypKgjFqOJp7h6TfbI_l4DQsLe67W_FPAvcaC2plTBmS7XLLdGpb2dzeFE8AqElK-0P0Nfd4PmANx1WWXXQSHOFzzvFZ9TjhzDvT8BwFoAtsH5d2JXA9Y8jVz8hyDkTMVaLzEKQ5Xdpw4EUpqQGOtGO8Dnx7CrANT-jwMZm5FvvJD3wXMxF64tpKg2T76GUda85Cq_XuMhRFxgG8Ux48w7xeTIAtptWZ_J5szSxGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
