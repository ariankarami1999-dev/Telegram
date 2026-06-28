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
<img src="https://cdn4.telesco.pe/file/gtFqI5YO2RXYSd5RJsTvuDpKQwGzVP1QXS8MCF67go86CPGAy_mIJQgF8Pfhuyq3jAiHkkiFaOtC2sOO_yD7GYjZt6wsOXJPqKn5REM2eoxJhh7b_VcOdyvoi9O1h0C_TG_vcwdpeAnHHD5gMIzZ9PJwRNKyyi3oGq1Kb6pkkDtJApBFTRyoe95rETEIQjxW9onGWASx2mOA0bdU0-rWRlgmco_-2ee0QHtUXcAqhNxfeowpTiKL3IiHTKwzL7guDy3Ic6aeOB2mjRZJBImJ9PblAuCZnUjFdZNDnb3J3pE525J_jmkJm8pizi1wF5jquINs1q5eMJwGM2lUTKdnag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIv5DL88PlGOdsFyf6sLihpwCV9EGms5l_fTzPz1DQ_-uZgsqvbdz4X-dEIrqgGDjgP303ZP9FEn5aGtAY0CgOIgzgJGcI1qgISqEzVftXRFfMJV-gDEZ7sW_1Et2a4MWPy8Qb-NbHJDZkgyJw-0NybRV7cWaHTy2SnUjIJ2uuh2TXIBEQv_5GDkVTYx5gU0SdpnYBsYk2dchAAKpDb42u4OdFQ2Q6Ih4GrRuXEEr7TvORegzM6cAJN6Ykx3qpueaPmFImqUIQtvXYePcFmmmm687MfGjI4znwwfySVYPnK_RR-VWcOOYohJkjwPOp5Ww4u37im0wTmDOqJed1H9-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 201 · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=UuccrSQJopJ4BLtY1lVJUnC-0boJoDZOdCWvVtTYoLrNK3T5Aoifpk2cCS2cRJrxQ_LcYUubA-om78KPMwZteoBC5zhOCDe20QnYcUPMYuz4F1N_ZkF6qedZZEJoO8JWQqprFHPcRDCNmvRus7-7t88ZMdrJ1E0pkYLo-i2xUvhGBlCnctw1ae0vnZBRR27pjEmtVBdB2kS_8h0ZjpmCyh3b-f_s7rfjrTezuFKCKwLsJm0Xo9UalS6Z989deYifzAxYfLdXBDTo1qH7y1u3K0GyrVzwHwvwT3N3HM4aGMkpMH9KScks4D10MOhs_vEZEfs2M58SYCFhrN06uY7sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=UuccrSQJopJ4BLtY1lVJUnC-0boJoDZOdCWvVtTYoLrNK3T5Aoifpk2cCS2cRJrxQ_LcYUubA-om78KPMwZteoBC5zhOCDe20QnYcUPMYuz4F1N_ZkF6qedZZEJoO8JWQqprFHPcRDCNmvRus7-7t88ZMdrJ1E0pkYLo-i2xUvhGBlCnctw1ae0vnZBRR27pjEmtVBdB2kS_8h0ZjpmCyh3b-f_s7rfjrTezuFKCKwLsJm0Xo9UalS6Z989deYifzAxYfLdXBDTo1qH7y1u3K0GyrVzwHwvwT3N3HM4aGMkpMH9KScks4D10MOhs_vEZEfs2M58SYCFhrN06uY7sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 898 · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrlqEimApmEYJ6iLCDNnv0YayyHUio0T-CMs1XMmFcsuiXKJQNGhpw_v308YK6nNyKU63-r1Jv0ma3l89391_ZdAickiAlRxd0UN11_IQTd7edUR0uq2a7tYNgWC1R-0RpNG4MJLuTGo2O5YHpY7W4_btcp7rujuffR-K9vNWXS8AMyCpVe-rxBuJ4qq6SC5DuLYUFtNp5ppzhbU2SiG0yWTin5Kd9pzzMWEoBUdVidYUrZGrmagd7Fd3uYBg6En_qiUaWLtJZR4pTD-D9TsahXXX60BrqDEMPn-EV09giIlCoHhnw6NGBAJN2DU6PLx7uYEW9oDfm7u0gSUbeiWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQU5qKeBbh7R_VS8stSIC7JUkgA--4rs4epVtHJvRccE_4dvpotoS-jYm1gzRiDJabCFBjcuRRKhnreCOYnofBEQrySZIZZHkI2V-mMrllcBwAkINSt3VZt8zrPKMPtJFgGjpWFObtPyY5ZkvDoN6bJLScMR-0Oc18KFre_3C0CN2mfSXqqVIdCDneZKLKuSYRw9CeRwwMCLvQyvCfA6TJeggwup6dMHJcQl3w2jNABMTFp-vvwa7kHVIV1tRvxa_7j_1Qqgxq4EKxrPYAyz3Mh1nejyb4hrx2IpAsaBYSlpdnU5EuqU_MuOIP_tS5AnG6NVNbBBoivx8Oc3bo7d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYSXGMEQbGaysQGNnozBAcZvJZseVZRa5XU9c-Tu3x5Y-OlTDRAUW6G8-KSgpVIdzFY2wWL1l697i1U1jT46yptvH2xOheK6xGkQ4u230UXzuYzc5yTyE1-xhTASQsBdNcp7hh-RKWdNwgwdg8GygxTGMHyP6vE60N2Gh8YoYK7UOmyB8eZM5S2VmnLRe9rUiXtCFRlhmyuTODIEUtEubEAyot_Ai5owuh9XywuaqZuWs3qoylO3G0_EMa-x4zFOuUB4R3h_2GxR8Vii-a3CS-W7Ox1AiI095A9G0WiCkPmRPG229lMOJF4rlyVMt3K1QIYWg2-fJLJ9qizFEY5Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOdGPjz42iVhbwQPYzqvXMiIY2gSTWnIcBkfdSsyOi4wGQDE6CZoIIez2hrxwiZN7mOc5wJ8WFC7FU0RnQ3NSS3q8kLRMbVmwq8kiFshTHvFwivNp7M_5w0N1WgHgQDZfxamFeUhS_Yl0Yt9dsWxOcBskz6rQ36soI8phweOLlMmNR-m4pe7FuQI4HMVP0FUCNBGiSxO6VSYhYRM1t4KDFfyRL6TElixLXsUna1Yb-i0xI4RFI_AxgPFNVYR0yI3JEjcTmiCfWcu6NVy28yAODXGpjxT_dpzCWlIUYUAupcGB7gcPTQqWjomXYZgN3TZvM-Pa5f35-oFr_WK-s4tJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOMwfAE4597sMThyO6NvDEwosUYXGCccPTm8AUBZ6NpvP6FWpD_vR8PTUX9Hm2NahZJEVlEyZtMRnlL7sglUC2wDArmWp24kkG1KMSx5WslggSyo6nHCdPediXyUgrNcnfEZ09HiGD-7Jyw74R4lqONUkLA64iYInIvmROhR19atKIxDhWRMR5QN7Dz58rYtHsdOC_C1pYSL6PFRQFZxT3wLtUDUmMUZMzzApO0wkBmKBN904lpNEYFzvhHs4E2GeFrF1bzVd3EJe_XiWMius_TJTdexlHiroK1F8RUEV2suEgzFw_UgHYwsSPJYvISHjXQ87Glo7ATE2d3wMYlwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d36VdOtWHzoGPQueAjNqu29Jnq2sr-PX8ra4BC90hMzT8zBYxR6JUwRt-e07SMRk94AhOpO0GDo1DdZawt46YQu8FMm5OgHALViMLEx75g7xMH6MddhFTTFtOt49UKWmtVD6DDagiTPm7ChhjdxgzsC2Nu3N2ZVPk_H8GMj0clUMC7akHHHj8aH7e9JrgOWsnbuVAhTTwy6YR9tTHF80m-VowzetGlkqT6iBaL-CH_PMYY-uG0sKafr0oUfNfqCV9cmEk7wQRT8lc8nW4zr-oNeDZNRZ7myPz-OlNNkLL6cJtVcVJv3Mwcf6ROcuD0MY-09fu1a-DMnnsZBHma8YRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arGzJEee1HyuvVXHp89IwlOE83RVV1DVL4uq1oPQAm1-LrIBmg914BYK_F1zy-kkJ06sJURK1iO3aArwUoFE5tXtQxmNrG8Qu-upLKYmuTKnz3m3DiGccPfyaFqGmhAhVN3IKmKS9nepOPXxHReCavHxcDrJiAiRcv33XajYOL6M_z-mFApB_5OUPnGAjPv6VZCgAJJePazqltRj_l_H35FTNEn3iYj_GLGx7T06zb0LEc4FdAbQrYXZX1R84NAM3sXw1dT3UflgOL83fKcd5rOU1mAVWXcMDmefWbRXBQCBl-VR4lRi_kp5LaBxdv-t7TgkJq5wnnIKthVX8UYhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=TQvWln2RVlhujgQUu_nEkwXbYzWDduMpWVZfvy5v7llGvFX5yqYt8U8K9qOnGcQtjV0wXED0v3aVgdmoxtoUb6HiIISHRmFzRx8FJFdNAJE3bc7x3KOH0Xs72kphM3uPIQZTGYicXHIHAidHFC-DsmJt9IOFaPZWvFsXPDy3lh5hkiiA7-lwhinpiMfiNm-sBQv-iGqbqse46HuW4XOBfNtoPdHNOXNqzhSdqo1Gn0-LJjhJRSGERN6J8yzwF1FR4ihDMP2S8ndakG9nibcF1xezB0jDdFvbnFMM2FEZ46y5QvQYnpkpcDrMoHWoSc2PRliKxftpDczY8xU87PsGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=TQvWln2RVlhujgQUu_nEkwXbYzWDduMpWVZfvy5v7llGvFX5yqYt8U8K9qOnGcQtjV0wXED0v3aVgdmoxtoUb6HiIISHRmFzRx8FJFdNAJE3bc7x3KOH0Xs72kphM3uPIQZTGYicXHIHAidHFC-DsmJt9IOFaPZWvFsXPDy3lh5hkiiA7-lwhinpiMfiNm-sBQv-iGqbqse46HuW4XOBfNtoPdHNOXNqzhSdqo1Gn0-LJjhJRSGERN6J8yzwF1FR4ihDMP2S8ndakG9nibcF1xezB0jDdFvbnFMM2FEZ46y5QvQYnpkpcDrMoHWoSc2PRliKxftpDczY8xU87PsGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8xyn0IJofpZ7wJWB31veR9qwJcccUDJ6sqrBA4bWxL4HaSdA580sii9BncxUIcP3V7HgsoK9fFdQtFJC7gkybc0r0KBR7wG5hQdTHMLwsc19dPvvU14Brk2YBz7-cUE1jKdH9aSEZsZ7M10jnEfnSTBLp38hbzpZOSkfqAh1k1HEO-mEyEjj52xVx4UBNJ5fF1TtG8X0H6oTi0QTnnhufXSy_r_P1Y8E7c70Ty-szBK5-QwcS39h4z5nY-AGyHMTNNnbIn_TW37ikk7lXmbIwyC0h0PSFyK-MJrXs2n4MkOSbf7MWaDzdxAxxFpqa2Jh_TqzMvjsfmqavb0HcfKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIIvgZ8uSsMXJ2hWWum5qYywyXBnd0t5i-ruBDqhP0XBvl7CfM4gtrW3CyRIamP4gPwlF96L_0kk29li_u-Of7-oETa9es5ogg9YmLtmr02PnRS492TpWA7P4OcK5sLNJaqQuqAN82xpIWUsniDpilkfNd-dNuYAFMsOeuxjLY5y6Z-_cXbgv3oxP0UxAg6-1ZHSNUgHsWLqj0RCjCpXutEEPWPWBTC7PYMuPVGySHP2grYGMxDOuqM34kNL1NhW0XstNOMzyymAAlen_5SXx8YcovZk9KdLlcwnzx4r1JUxA_LsHiJQwqSqFoJQgBAX0-Tou4BlhEks6oNhzb3LSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f31Q_RBwv_KQuweF33KpiDew-KMrVefOk_pE2Fo97VxWCscVmoIo-RrafvmKruqA7jAmA-grkHfYBEaYwRtpgkw0RRF_qoAzjW2kmT32x0Q4Rb0OX5oJAhRaHMQ-Hvg7eeXLCosUc_Y0QztlwXjl-XeSDpb4EQtG0_UEiWsGMHTRMsVvMIq8VwBhjDy11ezW8ZLpFEkyA2oDd8BL5GZcJGdi6XMAIc8tkNf0-nJsdgYc28KOKaMSSvCbdSGomzIgxLw80abQJNFHp-FXtOdJ_77MiXAoPjEf5bXXlso2A8k4gwtiASnOq9QnhWoMen0a1JDroAJKUbczZnzlfygXvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXw1WEQNPA7REAfK0dN1AiIVdM0eUPJO4J0LyeD5C9UXRAGyYKNZHmgMmYIVrbKU_j3uTLTr_5JnRuW6fzLStjSW94UwRQ7FglbWcJaqBYLLH0mPLSrRUkK1uar2vM_rsrgSDKSX_1jI4LRA7rAten4CGV8L6Rmf71Dko1lPfclIPUGidbmVpIHE6i60h5PfOg6Mt5wdlujAZTYRI9YYf2JH0qjamcHkz_xGPkAKTb2LBVjZ5rTCKULp9XdCBDODKvedBuECjAHvp5GiGojbKkHokonU4Bmy_BPV1MUY8ltSMqVpbtBp7OHwdCCOxoZ3P6p09ipgrxGn18VqFo1-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFXtkTvvK4s_B6wgaVn2foEdghIWZ0g55Bmgf5ox_On-7-p0laqtDXO-elx5D6rXstTRN5ukiRCr3IXAdAuVryTS2cfxGR-uDnuxVa6BH1XtxDtbOd-JBeAUvYgi65Yh1vIyIFTTMzqrkmgDtwKckduCRkBC7-LCcNA33iSq4d_T0mb3RWIi8YenOxFKDo9WLIwlbUiMyvXhkN9Z7cUfLWwcKmsiZjSAi4FbjhehEpOIcs_kD1aqLiT39yumBHthinPqjr9PPV61izdpfRW6iRwCaYyoNUEaLWUKeiQNB1L5YU5pB0WFHu4vHX71_S6yunlp_HppwoXmuzskicTbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni6ocx_syR6ir4J1HZXghiE3rBrKW-NWjPqnBJNd755rwNmjZjDUEg5V1SRbivC3ojfKRHB3oPGv-C4LjNxqGtb0vkhnMJA1WOOxOjECLTCD1nvMlTiuO0mwZHpOzxHapWAHZkPnx55UPP-ccZYr12nbleldbTekQAXg9AGsMbBy33lL7xBiEi6VmJg5VqaxGDq27yggSdoJ4_3wFX-e4-7WnphKXuqLvicsbF4n3DZ16WfSdAlL2nG2qARzE2A5_3q6LyHqKjMQOYk4ZxxpoMozey_3qGltEYXw5jyhFoUYBLxDvnR7c-DL8YWONz-zKqQ6fVewZZI0Qcfx2QGZ6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Y5qY9M3-xi9zp-hTFoZt2uDhJ3l3uM-uEAPLoquu2SO0wcarlex_2S2gm1jt1gx7zzX4HSGfoeHLDrU5EErOBYZXKAAVtvYcFd7qma1g_AK-BSFdywWxCNrEwx7nCeqP0uZffXrlUE8ORWz7PMIjMMjjdCYEuhFnFbUJQ7z8w7dWzmETkJ2hPsFlQrQrsOACs7H9nWnlQZbK_waN8hPbMbNAKSl1FLYVfVlOkHlsKFhlKxjQ5CZ5cKifPE8iDpiv_9TBxZk3vG9swg3ZmL9nXTY6NwKj1fIV4DyH4o50XNLm5nYJI6MNK0pDizZtFXnjZfWBWKT_Pf70qMXeWFxdtjXGfOPh1XfIm2Qqo5R1izPtMxeOj8F92-8FHrUPd2DjdCOLv9mDn-F5HTjL6bRXxQsAWJGuThV2PgXqwyF_077mzaKYlSsPEY9YHC-qREUH0Uh_LPeBq-6RrMQxmfgN6Oag15dGUDWYMWiPExp0vO1PMIXVlaJuV7bHTsJYam1Jt7VNqUmIXgZOSo6KtEXyJ2MfEKK__sZoeQ72un-65w7CH9G7UPA2BJJ6U-RKIdWf9z4FlLjqr6uKulTVsBYzt1JR4RMxelQmnloLuIzhRGPezJlS7L90xod7A5RtW8F7_IDnDIK42ttihcn47Hhp7G-vryPTv3IjiQyAa3G2h9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Y5qY9M3-xi9zp-hTFoZt2uDhJ3l3uM-uEAPLoquu2SO0wcarlex_2S2gm1jt1gx7zzX4HSGfoeHLDrU5EErOBYZXKAAVtvYcFd7qma1g_AK-BSFdywWxCNrEwx7nCeqP0uZffXrlUE8ORWz7PMIjMMjjdCYEuhFnFbUJQ7z8w7dWzmETkJ2hPsFlQrQrsOACs7H9nWnlQZbK_waN8hPbMbNAKSl1FLYVfVlOkHlsKFhlKxjQ5CZ5cKifPE8iDpiv_9TBxZk3vG9swg3ZmL9nXTY6NwKj1fIV4DyH4o50XNLm5nYJI6MNK0pDizZtFXnjZfWBWKT_Pf70qMXeWFxdtjXGfOPh1XfIm2Qqo5R1izPtMxeOj8F92-8FHrUPd2DjdCOLv9mDn-F5HTjL6bRXxQsAWJGuThV2PgXqwyF_077mzaKYlSsPEY9YHC-qREUH0Uh_LPeBq-6RrMQxmfgN6Oag15dGUDWYMWiPExp0vO1PMIXVlaJuV7bHTsJYam1Jt7VNqUmIXgZOSo6KtEXyJ2MfEKK__sZoeQ72un-65w7CH9G7UPA2BJJ6U-RKIdWf9z4FlLjqr6uKulTVsBYzt1JR4RMxelQmnloLuIzhRGPezJlS7L90xod7A5RtW8F7_IDnDIK42ttihcn47Hhp7G-vryPTv3IjiQyAa3G2h9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=RLYGoNZpiTs2nVsNsmqO9YBugiu0XnoLj28Y1GukCdETfJz8u456sKYSEx0UxDXnUCJxzgUoxeMo7mJ_09BODxeE1TLqIQaHJTql08O0qhnOXQMZXk1yGk_zo-vWF8Zul_poUabtCzWg0E7iscA3SdtPoJYLKd3-qfUxzy16QXFwTZasUUZiFMgeKVeUSifC5pbVbRpF5qAudvsU5zW7aZ17EIN9yP9bMxxfWZjFGUXJwLqUQd1mBT8RWM8ARm-9gReCTS3TzZSWwULLhOHIatA8QRALIwowNhQixEru7Im9tKMyHI9UNdnCql7ouj4f7I3wzL1Vy-ef0jdhUr4HZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=RLYGoNZpiTs2nVsNsmqO9YBugiu0XnoLj28Y1GukCdETfJz8u456sKYSEx0UxDXnUCJxzgUoxeMo7mJ_09BODxeE1TLqIQaHJTql08O0qhnOXQMZXk1yGk_zo-vWF8Zul_poUabtCzWg0E7iscA3SdtPoJYLKd3-qfUxzy16QXFwTZasUUZiFMgeKVeUSifC5pbVbRpF5qAudvsU5zW7aZ17EIN9yP9bMxxfWZjFGUXJwLqUQd1mBT8RWM8ARm-9gReCTS3TzZSWwULLhOHIatA8QRALIwowNhQixEru7Im9tKMyHI9UNdnCql7ouj4f7I3wzL1Vy-ef0jdhUr4HZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayTrrqW3jCZTf2Za72GQeYVeAWVoxQEZ9CBSM6tHFUr7Fls9JD-Y30iGJ03SgNhmSJ5yiT4s_SPATfSVB8-XHepcYDHwOU8oHpq3mx_4nOvugcz-_VmhJfyG31nRo6WkWwA0fNkG0HlIhBfWmdiZFbJBUBOKnKTyih9IZ_527pQqLQ9K07G5V-g5_nON7zZwWKBJFgFP9Yrd0WacfUDi2uHH7ou6u3zKOzr3JQKLTqHTmynNLSfnCknhVqZnWgKpSUhmCU02G8ZielMqQbiTILvlCjBExqfKtVKU4YLTU4yPKlwcLsF5hqucAgB8KFseedN9D-KQxHG6SmBsv283iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=ohE2glg2m5si0bUG1rdpOO1aKpgzYtr_7PytJgBf6r7mu5F_2Tu2de0xo1PGnHvI1AJifRdXxvQ4EOjVG_lKmSV4dlJkqvT9rBllGB2sSUSBhvJ3tIxmzP0d3Fo3c-Wp0zmMAMWVh6t456W6flSaxrcUAzKu9zDE2y5uVASU7SxmTdsAegi_WlJfkLsvGMTrnPaP1sIdiMOGeSMsUH2nyGSH3RBI54PoRmwJlWT-Bm52nZ6x61MNGbYQIEHnXcBdLZ8ZvAi6xZfkIObnMGbjTQ7V8XJsxB44QKfhEIAnlhGMcSUAitoHRcH7RWj-1NKSxegzAXEBrV3n093oVvoEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=ohE2glg2m5si0bUG1rdpOO1aKpgzYtr_7PytJgBf6r7mu5F_2Tu2de0xo1PGnHvI1AJifRdXxvQ4EOjVG_lKmSV4dlJkqvT9rBllGB2sSUSBhvJ3tIxmzP0d3Fo3c-Wp0zmMAMWVh6t456W6flSaxrcUAzKu9zDE2y5uVASU7SxmTdsAegi_WlJfkLsvGMTrnPaP1sIdiMOGeSMsUH2nyGSH3RBI54PoRmwJlWT-Bm52nZ6x61MNGbYQIEHnXcBdLZ8ZvAi6xZfkIObnMGbjTQ7V8XJsxB44QKfhEIAnlhGMcSUAitoHRcH7RWj-1NKSxegzAXEBrV3n093oVvoEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=sy6LBLoNNqb5QXtGToHPLRKMoOY9OGNbcAXAF0GmehciqxGEnDU5d2168sPyJMquTfa0qBOckqX5tl0bYaSMYK2oskCYzGeSnxnKXndp429kLrdFuC6fCjXFgqD1b6v4cw71ebmP9d6BldDJCgMEG_n4hDQGrktFOUl-7KJJU0nfZppaNwu8-pcrlMuUx-IfG-H9XZ4xyXaRn2FxWWkB-kYNwwj8cpYrESAz9LlpzXE4rNEDC02OTX5_hdadaV65Q3Kk7P_eKpDFOsvukPVaETkINWcoQRKX-lrs7wJOCmwXxMr74tNlLK71GRC0sxKY9jw6BNneU_-1oAWq8DQmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=sy6LBLoNNqb5QXtGToHPLRKMoOY9OGNbcAXAF0GmehciqxGEnDU5d2168sPyJMquTfa0qBOckqX5tl0bYaSMYK2oskCYzGeSnxnKXndp429kLrdFuC6fCjXFgqD1b6v4cw71ebmP9d6BldDJCgMEG_n4hDQGrktFOUl-7KJJU0nfZppaNwu8-pcrlMuUx-IfG-H9XZ4xyXaRn2FxWWkB-kYNwwj8cpYrESAz9LlpzXE4rNEDC02OTX5_hdadaV65Q3Kk7P_eKpDFOsvukPVaETkINWcoQRKX-lrs7wJOCmwXxMr74tNlLK71GRC0sxKY9jw6BNneU_-1oAWq8DQmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg8_SmY0QVqwx_WXhs_s-O-ZrrQj0DsuqlI10MwpSQLTK5Riz04X-ie9cO0Rvocq-Gtm0IWdsu8DDYZh2omCyrc8aL_tRg-wnV8Xw_Vds5FFEafNqLyzGeVaVnELvKj1RaehGmOdYbwX0TkC73V8hhf_2rd8ZN3w6oY7pbkQ5j7D3J9M90g1WVeBIqHMFQr-nbKG50vPhQo-cwcjdtYhZO-eBjmMukDqi4R42D35zKBbzNZGtTMxYvbv2Ome6JvXZsEnZZxuukTkgyB1OhhPOUo6aiZKh4uUcoHzs1CcpFJqAJNcObac4j5iV1wKP3DiJCgKrHEwdPAqqMNSpmuzJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpT4AdwIKbWc805fenXli95k1qoh-jHOn2r6k6XJ3scJEba1Ya2RPuk51Aee7caJULPOoNofSAUAqsQz0X4w4SwgXawP1vf5leV3YCjZdCcCSvgvellMYyCNcmsPQn_3IxbXJHL9xHAbwjU_iybqHRRYo_BSeCjGLqNxIpDqB1ThMW8SoiNSnbiLv3pa6GwZ_aNx9nbzuqIQONuWYkCfxd0O0kJB0ze3GkNf_4t2dJdbDraGI3p7YOiN9pXTu-zClwXO8nFuzc9tolbDavdJvAoNgPvQo8GYlwgk354RAU1AEfLJtYYnobyjznOJzmP9H45Q7WC3fRAT2IojpGAulg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-B_0Ozu5kpJ8ZOnW1zf60FlQdeDKYp914r8jU0g16OslXlbWecVF7C7tvXJf2n-StEoZNW1urE7AdfTf2MfSuGaIfqFRb58UDX-RLLzzRziXAQ7e8gzi-0OuV1n5xvvAFwAvoTGBu2fQ6cZU1CXgwLqiFS4Rp_n4iUk1SHklQEt3Jaq0lkRdvSx4Yn3MMvgd7kw2nfy7LUSqTIjBAF_S2gq8hnN_0TvCwQl0BOej3GsOsDHA5I-3YU__NFXRYy8zNzgt1-FfKAetAMVzQT_FnNPAqBmrtb6YVQE2bm8WSKllaizw0nBhDqsk0T4GDLwOH7fcenuckoje8Yn3xxZuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=M6zwTV2ldfqGAQQVH1atTRCx-c-2rdc1UgQAFi4GzQ_OBIm1qN0fGJeJvdVjas6cazBVpaLMp-NQ3a5EPpqXmf4e4oibPX9qVjzkeP2zW6HWkjGldnQ7iJv0BJHPdiFaONQZd9jAWzQFlgqXBSQ0bf8DVICP3BNBSAUdfbtwFZrTd0bTx6frmFrXM9suGVv7W5xTwB_OQzatLjGrlsL6dLDFIM3p5PS_KymCJRjtAfQqlpsxHxtPA4xtOdetCSdR3TTeE8pEktyETqDaeXuQkN4BCGWcHC94UCAMddd6aRhotm_elxqiVbyi0w3gaMpyRSFO-J9Xtk_5NbgEvoTm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=M6zwTV2ldfqGAQQVH1atTRCx-c-2rdc1UgQAFi4GzQ_OBIm1qN0fGJeJvdVjas6cazBVpaLMp-NQ3a5EPpqXmf4e4oibPX9qVjzkeP2zW6HWkjGldnQ7iJv0BJHPdiFaONQZd9jAWzQFlgqXBSQ0bf8DVICP3BNBSAUdfbtwFZrTd0bTx6frmFrXM9suGVv7W5xTwB_OQzatLjGrlsL6dLDFIM3p5PS_KymCJRjtAfQqlpsxHxtPA4xtOdetCSdR3TTeE8pEktyETqDaeXuQkN4BCGWcHC94UCAMddd6aRhotm_elxqiVbyi0w3gaMpyRSFO-J9Xtk_5NbgEvoTm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=qaFPgFaGETsVOK_TEEHn7MNtJinCT8JOL8_f0SdYDjI79eXvbWBCalRORNq2UPx_0FgwL-hQSz1SBS7MlZONoQ1ncvVvuUEMf8sKfib5fsBnPPQPA3hCnp6f7b_qkiDlnaNKFjt6VxMBW7TJd4SSo8hP6NPH9-oEfT-90bRuGf7rrj7JpWvUu-8sMuUTVGXTrCMVFgCOKdESImP84GVAPWd4hv9TudmsC9CkShSMaQ7N-B7HuldxEx2e8aUQjnTjgVhMAyaQPEW3ZEPb2ArA1aYwgm-WzGsB3zFeU8IEsvvFdCvST_5aUoP2KD11YSlA7YxBctvUZvAFKFdno-ToDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=qaFPgFaGETsVOK_TEEHn7MNtJinCT8JOL8_f0SdYDjI79eXvbWBCalRORNq2UPx_0FgwL-hQSz1SBS7MlZONoQ1ncvVvuUEMf8sKfib5fsBnPPQPA3hCnp6f7b_qkiDlnaNKFjt6VxMBW7TJd4SSo8hP6NPH9-oEfT-90bRuGf7rrj7JpWvUu-8sMuUTVGXTrCMVFgCOKdESImP84GVAPWd4hv9TudmsC9CkShSMaQ7N-B7HuldxEx2e8aUQjnTjgVhMAyaQPEW3ZEPb2ArA1aYwgm-WzGsB3zFeU8IEsvvFdCvST_5aUoP2KD11YSlA7YxBctvUZvAFKFdno-ToDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqPybJOxGTRhqdzzlnYBVQyTuVTWXBXM9JvcaOXIIK4bYkCA9s7eiZcQaj6ywQ5ElA-sFvmYumcsfYh6q9tEzyCa02gmKg3VfMyPSODD8skKJyx1nCUbznlRVGbEYXODiyJz3c6n34LczOrIwSKRd8AUehZIY5GbJ2sc3JxDEJO4gD5dRPYP013y3GGNCeUyxHkl_0ye9HoJMhUW7xBqKjjJhzosb_luNe8wA6WTiV_LYdEEqRuZSm3EiJ_t-e1yIIWq112DnXlwRtYwxgn8pHImsKWm2dWBXzwd12Ov4QlHEbgTwzibPdlhXMsaEKKbZbmp81-yQa0jbb-nUYOYaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoRVypmycEYtB71BI_ecJcrsyQuyhTsxPPR3FRC0HwuyTkd0ywDvg1bJe3cxSNx3bi1gkLlL16_3_IUHI9AXbWG_Kq4nD53EkfHxDETOm3yE1fctIRhITrp2v9Af2jT1qx-iHD-JqxAduyttZ30SiwtjU63nqXruPUixBGsxM3dirL92S8a-YkjKB9IXWQUblqz_q6zS1Ng7XWF_3lki4UcPC6VRjmW4nUD50FWl8K6F57HKLfXfsbBsKhYUclDOjIbhveVId87YN4GIudRUvU2FtgxipdsrrQLtqKqXY8SQ1vyh35EAKKkEp5Yd6wrR9TqB08F6EFuJ953M1lhAJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CatWx-1iY3eHXu7uKEyGkU0CTUtAdtpB5usYLyelLVaO41EhNSZmvGvW1jWhZrwwNiwtHnwVs8KOxiFsCOv1vPBGdmSgdSWzospSZ8F1wySonpka_qUxU99ahMBKDldUWGCi1Qe1mGAy64sGdFFKlxZNFm4_Dk83qtehF7xoamKkA8_OXAS9E07f-oLU4_orkQWIObnDLYrspxHE8Uqyo7s5P6CIqKfvH98285mwND9oh4Q7fcrv0DUa7LaQoqHet3QFo3fuaBSFNcvDDQl1fKAR_HO9a2euiSW84ioMLkt2vnqw4jIUO5VXyJkczeI94pkoTN8ODjtIjiJ9B_XZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKm7BOYQqbtMMed34mBM_HngMh0V0xTgoYGQHVDRxYuINPE0WAzQNo8_DoS91f5_JPuQiesIX4GoM4-BUwV-4-Zy8DQXynrkZRAfJQSY5MR3zfYjIYsAgoYccvkCY9HjejjQpHJ6pKRgDBCqS98WUxlutiharCVO-JLy_jG97JkCMRNOpIk91-44hLCjnH6Hxw4kWT0QsdMopXXaJkXfkjbZxN0SZcWqMDEmJNFATGcckS9RU1rryhvKUjdp11uh2g109hl5PXxtwN6ySQ7RUGiMwrYHigzmeOtNnMV2aLj5MyWeB9NND9R5a5dwyCEmZl5Y9wxqYaZacPUbvdy08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy2ivQt_XJMzONXLyNrvjQ35XYOOAcwUn7Cs0llgzBgWI5edxgSs3wlIvl3NfL2333rc3363a_f_pYgtj-1JTnzEukOGgc8W5c3M-7vvFRxiEupD20LxJW0Jjt3WQSdYq7XZN-LbwzRESiMM6vIrHKyIuo2jSFI9VYFvxqYbVFnUbaRV5GClcZhRi0sezC03-53oBSkqhm7PDzUzAmRFKhk0QTntxTYA_WIuQEGtCyVjFzUFnKNm3NcQjCeBz8mfkqaQ8YlUdrNWQ_WjWFPRs6RuJaUZwE1231eXTaUpaSSZRPy8m9h5lOvibjdJVzEnLrYp2Z2HH7K43r1YpO4_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mx2-l0xUob6773sWBYCKJ7pRQ4ddOhOW0uhO1tOyBFH0mAeGWICJADkcTeg1wjcYDLfVMYQpBPesZLam_rJGGsZhC_XnwUrHhJhztsuIPPQQtxeLG6mWfFeqzSXjfsqmOK5RaFUiq6Qwi6cVEt5C2oOVmLSoj1dcf00aCmH6F7xlp9wILN6en4ZBfjuTQ8Z9tL8bBkug1oC0d41MEhMODIqYDKlhBTpxhicl1bASOjKz0L3AK5evsJA8ZAqwZI2sOK3xil-QT3iT-Zf8X7GzrfWmmFROcWd4g55NMAGbFRF8UYKkpyxq2YJWoffXs-0IBU-GMVX-UOTgwCQrFAAlsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIQoq4kow2g-HSHZ6wfAIa9LCMasLE41dPAaV9h171_e2BQKPE3weFXGF4v87XYxaO0DF_4fm300sYQ6hMWr1Gi4Sf7vbi2PUw566w4R_6ccoH89D5GLmAvSQvoB60HXDUCAiXh7OnQa-DXXikSN2VMw7zQG17QVt_7PcOgjUbKZBMm60vaiVIVpL8OJFN54Pu69xh1X-Bsd89L8Q4GE6WXqXEF9FL9W8n_7VBb6NlLibk0E-MIY68Vqq6yZYfYn9LCQ3id80fHd3MXZmyqzkhZJdWweLfYFYS5EEKHuvvuaP0zmW75njRs1D_UHGBB-MjMZ3_315_0getkSxWPSLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGgP70rrWHy_FBL-eOimmqKVDQkjHAxzvlhsYoh2J00BAbyzWDSNB4Whp0W6WHeQAnRKpXPouV_jfmOBdEijSBXcu4d2ahkRMiNR41vVUocAYjpAsvdYzyUyNmT4fH0pKYCJxAruiiB85mvYH-eL-fwylGHWaWP1twI_G0Dvb_g9voOwBx_TLNqhSAJVFsaRpascHcxrJSsQvYHmz5cjU5QDi1SBDtm44kn0ZQrgZEN2II8p0CLzdt-DQPfYZFUeUatkQzKKnJR6Ekd5US8GAGrrcGXIygjoLmCJGpbpgvDDG1_6K0XYt1X7Gq_lX8YHXRUynOX8n9firlDBuPA5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5_OBHvxdl3WOFBlpohY7ZqYHiskqHRyFmlP1Andsl-l4zMgO26NHBw93V8hFNu0IcuKomeCh9yRxRtB3aP8I3z5x3swh7sl82CNPFbA5N2rc0uobGV2rJPfRXczTrsdg2qNeF-bd2xALw0c1gofEaBbB15UG8yXP5f20rgCw9-ZrKriQaHh0djNiU0PIL9fR2nusMYSJBLyyCOdzZ5fyi6LoXzLMm4lxTADATCcXtirD7Tm1qAFCIxl2xyhwt4mMek0_PaNjTuN_YGuJUygITWrleEBoatpPVbzRIL2b2BSd2vgI1JnbeRxGAuL4UfIcbsGrL3YBeQfOBdntoX52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9-VdBxk5wFaoowinJpthkXqLr5T863wiFimcsRzN1gHrMJKqaEP5cml4BHOeTxhCnCRmbhkC08YesqUoqqrXrCwEPFaxGP_2S3NqJ1FfJN68hLkkGZlv15FHBvdnDeUDO7ulKQ0wToyeJfAS9lAV6m1paxm3AI7pAMWK2f6Txr_6OXeadGgcqyp4bPBiIAfBJUBjbsH7UDNGq8LSoTvpxdSWW_pwdSAj_IUjAf2DBEE0X8xoT1xRuHQfKhgqrv207feEYEVwDwdJkMk84aYfmQaQgrx3hdUy8NN_VH0aiBpPRqwPSan3TKZ8Bzh1BYf7Gv0DLm-VrrJRCyuFr05ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJFfWqncmtXCJBLWkzAvEI2vB4bB42me9QJ9_TKzPTvGgeD99pwAG9Bfpu4RxBCSdERiHefoHK9M7v-20WzK3X76gjBWxNWgijPOtc1Z3PbSuA6gz82FMPfx8U13LCoTvrL3fS2-PZS5qZ3MLO3yIRaZUJhblByKiVGDxrZbZmbA9j0YkNLgxuLijeFzPCa47DLPCOplliUwhetJQzacAkqjTsJqY5GHAfoe65WwIHn6SPMiL-tFL0lm9815PjCsCoYh59l16UmA5LRWk3N5MAmIDtvVzinqKXO5e7a7lZQmvj5QAGwnSLVbyPJFjTYBkF3GIczJQAbVcaVYKxMy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDMgyCR8Pt6F3YLlyozFSWAOOez9zd13zwjQgSNVd3Lcjdk6bL7sKFOlNsEpVQVMUMbj6MNEgMVg_trUURxu6qqp8zIwW7tE1QWmxK6bfDLqNME_jBQ7w4-tmag9ytbjqg4S5hDVRD20285hxGfynkwDBWRFpebxwwH2U7DrubpWlFknmHql3zbwGsHn2hB684FabsMZALvWTrapjqCKiEoOHiUmX9qKazQCXiTvteqM_-ZlTj7cZWHAjY2hOeQ4EmDTL3ON-5j58mkHXf2fq17ePWr9gjo4jNBaOe0EnNA1khYn80kaPLzHm8WPNQlRUVv09z07BmAHpFLeMTlHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9DZbPb51cRv9-mCDMlCrZfLyQHQCqQgHS9tfPuIxs4zzwxib4adknqLt0HBjYRSNdQGLvlb5EpPuQVQhCqvS15vf8fBCU1Wymsa5Vavd6gfEoYQNmmR0VyrthnUxNYvkRgARCrqwSqCgC5oCTskYTU9KRVhSVsV5KQGXSxl3quMYrJ5qyq8EqCGAi_5K4PQcdAem-Yas1VXmf_9ejkeMHuIj4lOJBlQwKiyE58sR7eFohk2vmk2PdJEtnlHMtWNcWDQ9fgkXoVNp8Z-DxtDSLCQoQhHGJCvuLVoGtHetrOBaq7heeAOc6HC05aisaib-woigp-aMkqjiivFzugBjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6biiMX_LS6RYlgjbSi9ZJqGPvETj7ru3gWLkVuUF3ZN8yw0LlEAu4Gmql5v1H3nBZY9DKqmCIF9Fe6n4vmnyDfgf8xlqGlyRrTd61VD-C3I9wVXiiM0_po9IKgOycSrn7jk-OmNmu3hIJzSBw8X12TCAnEB7eerZ3m9isZdyi5laEMYpQ3Rpta2_-TdUH8T9nbgOVpzjzPl_vmlnuPAuZYzAmts-mON7Z8Zm8gZh7GMUt8Pgyfe8YAFGeJihJlQHUIusk1ROpSN2vXMsAftV57_57xPg8hrHvuNHuTluoWlPOoUmrzKkeNDKImERD5OSfEHiIF3hOz-VmOXvcJ8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=GtpqNaNoZHPndAiZFd3Uykq80avsuD4l-9CQfgpccuEmD7NIpMrHIvlS4pWK0Md718pRwLlKpeXZft61qGKskt5kjf5jMcZSgOzOl7tnVr3UJ8oYizYF882FcTIt9MdBouyRXClveIY4kroYoaz3JOzt6Ea0AQ_0t6NfI4hHFr5IRzFIxqx1Tnz23ojwzG-KzPhJFEXA-a8DSDWoXj6VV6BaL46ZfuaUWpAbWU7zCMMr1msvvUF7S1KrJZndC_-LJMUy9bKKC6W_XMLp3pNerNxuS3a6sXWgxEW72NNce1PkGq9djqtOzCRoNMVx7-Y3wdE7vwqg-Vo6vkL7gklxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=GtpqNaNoZHPndAiZFd3Uykq80avsuD4l-9CQfgpccuEmD7NIpMrHIvlS4pWK0Md718pRwLlKpeXZft61qGKskt5kjf5jMcZSgOzOl7tnVr3UJ8oYizYF882FcTIt9MdBouyRXClveIY4kroYoaz3JOzt6Ea0AQ_0t6NfI4hHFr5IRzFIxqx1Tnz23ojwzG-KzPhJFEXA-a8DSDWoXj6VV6BaL46ZfuaUWpAbWU7zCMMr1msvvUF7S1KrJZndC_-LJMUy9bKKC6W_XMLp3pNerNxuS3a6sXWgxEW72NNce1PkGq9djqtOzCRoNMVx7-Y3wdE7vwqg-Vo6vkL7gklxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3WPgH6Z0ShRXcaSwBIvjUYA6SVRL_fChJgqmbKqOkYS01sBMFamNyeZNRjWHePv0q90lphnlHG43uTvqfUnJYF71fZ-dKqRof6eirHUXjv_IxMzI3gdDcXybKtWQ4fNlYBgsfUUltA2DlPLMjOwf_02sNO9iECApTbVPKwfkM7o084wk_s-h45EgiVXgf3yEDPMAbEvKyFXmV9BtDd0IWRYQSim9nVujolQ7kow0oPX71s5svFygTjHHY_n4Z5Kcu2aetv54-dZ7I2EiNMJKfWJ0QiYZ5ZRJ0y-YYzsdIvUR3bAv3H9BymchemTFfrNbJEneXXh0-yGii-EZYkEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4nWm-ZzIAKnpNrdPJpZa5BaeEKR1LMYgqukb_x3kzL8qFO3fbchkZXKvHfS-gDT-g0lJGxQY7g5O844hOwj7VR-cCDjy0W6MucmhFHEFsHRbRN59_F-YKJvgApebhl2_lu2kNarwJ67B8ewSF6MRq5NJpZsmSTk0cN3gXxxAhEVXGw2fG4UKrjPJ7zrsRtDOe-cet0PsQckQxW67h5-E2UIXK9itYSIu-iN11-ZkxjrMq6eXtzcO7jtSaAvKxyqwhEXD8szbWC48iv1y9bgsmQyDeY5sl5tXbdqaL6CZg1IueNy_TDGh_lxYJHfmEZpoOGZxPX57MNqJ3Dy9sttCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ2hSOxff_5S-2p2Bnuc5gg0d3AsHh1w-XvTMSDkDaxxDkFFW-e_CWpUYyxFSqjEJEdrvSWUz-BCAXxfz2w-DQoLmO03UCEpR3dnRFHWSGx4bXltgHfNB2o7MkV3MPbG6UbRKnTM9C2XbFUFJ4P8B08kuQF8IVz5JkRDP-Ujo01S7hQgfgeB8WpQzUzXDHNCow7V4Znicw_imw7zK4zYpY5d-NMqjiAAVvapL1z5BXM4GZMicciGRbuLcYu6omSeZlcIdiRIhNEYqLfoWknn92YyjuJg1dH-dY1MUoK-KZC2O24DUGxe-6myQT3tn8VOdzFmjgY59ay2eRfL8lyHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEAMwBcOKGt08D9TRtDhL76U3lL2l1BUGV9YNnTq6iVasSFK0ESjR5EwHgYKIS6ZNXPszIn67sgkNb6PeXqV0u6xV-mKjLFP-hE0iO80jMBkcLmeTyb2BGIzPWpxYuE55fQFEfeGnEIhG_J5F2Wlmi31D2Wl6WcYEIlnokSA4gmqc1x1Q2tJlheG8CdF9s7E5htRacB9pGb1tjoA14MjrUx-S5n1JSVzcZH1QOJtyk5pdZRqhHHYotz9bBLyJMlJc8wCOqYUIZnMPVORa8hD_POB-Ej_eWNgPHuGG3hB8tJps_FAlzRN26fsKjthHYoSSmhCP_AtQX5UBeknw70meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=iBLZkd2vKOZooUSAvl-0-I5dtaZnQz6ZSKN2N5OHKoR7brW38FQNSCl1ALptF1R62mM7VQDQEdM48dzyo4CbNhP7WOVgc-ETCfrfvIhqZQ-gYKCJt4tjPvrvqKjkmmczvE5pmtjdcftTHossukU2tTvoQhPkyTLe_57cuK-ovtuO_0K95TK2EtoOyF08kE5gAi6J1o8y1Q0fSMcyAFYjdYNPDyYzXo8PN7uBAnmK7SdPh3drNbkpISFUnRCso6CF5Bvj24HoLO-O9mwilfnDAe4B1JUTqRr8HHARwBibIyuRbS4IzA9vyjVNwjyGxqt-I7DhjD3fFYv-au0XGXdZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=iBLZkd2vKOZooUSAvl-0-I5dtaZnQz6ZSKN2N5OHKoR7brW38FQNSCl1ALptF1R62mM7VQDQEdM48dzyo4CbNhP7WOVgc-ETCfrfvIhqZQ-gYKCJt4tjPvrvqKjkmmczvE5pmtjdcftTHossukU2tTvoQhPkyTLe_57cuK-ovtuO_0K95TK2EtoOyF08kE5gAi6J1o8y1Q0fSMcyAFYjdYNPDyYzXo8PN7uBAnmK7SdPh3drNbkpISFUnRCso6CF5Bvj24HoLO-O9mwilfnDAe4B1JUTqRr8HHARwBibIyuRbS4IzA9vyjVNwjyGxqt-I7DhjD3fFYv-au0XGXdZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=FteIpF_pvDa1kEycrzY3pcpr_6iHeDxqQJqPpqOFnsSYXh0xKaaX-pIGWl6cZKy-zrNOynm8jQfqItHWSE5KFWUlnF8KD2fgNZSRW7aPrwSkhtUdoLJxkx6ifC1AzK_HOEreP_tQDigQJyTPGofhkaTs7lb7l3142kR9wwXOHrRGOUv3qVAvtn6rCnCjPT0C1iZqEmlWUG2ydE3b2jYaT77imPnI1uiQ1FjQfgIpCj-HMI35Gxr2hE758kk8o9DMhT2ye5j7ek9CvTVfLxovzzj-sFKTw1_FGhPxDekTD2ASk0Jk4pq4mrADXuss9TPAou1XTN9sAKmGK9mFe1pZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=FteIpF_pvDa1kEycrzY3pcpr_6iHeDxqQJqPpqOFnsSYXh0xKaaX-pIGWl6cZKy-zrNOynm8jQfqItHWSE5KFWUlnF8KD2fgNZSRW7aPrwSkhtUdoLJxkx6ifC1AzK_HOEreP_tQDigQJyTPGofhkaTs7lb7l3142kR9wwXOHrRGOUv3qVAvtn6rCnCjPT0C1iZqEmlWUG2ydE3b2jYaT77imPnI1uiQ1FjQfgIpCj-HMI35Gxr2hE758kk8o9DMhT2ye5j7ek9CvTVfLxovzzj-sFKTw1_FGhPxDekTD2ASk0Jk4pq4mrADXuss9TPAou1XTN9sAKmGK9mFe1pZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdCfH1sq-fkGxt7wnFRpYrDKtrOa7J7xYOyjVR7hMWhspwgNduByr9WUpoj5922APV-PcBeC7m400JnWTUDpcv_NLFvkMn5PMgAL5q7iOFx7p6GBkgyE63etsqN56xJHTNVh702JKkG9sUtH9YypoP1GTD3V2DvIXzDfe9er2gvH8betPvjKCtyt0x34jTeeQ6ZmWLQnXsuFRP4a_pLa1REDkOX-Ui-YHLUeEUUBTQmRJUJ5m_8srMR9n5ZWvAC4tra1kuWwDZWg3ZrBMrdQOP-BWwvsy7TeLf0HFI9bjNKQINLcC4OxjpWcSq2kAoj8OL-psVPgmTfPtqj8AEyTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=IiFjic6ArHM9-v4ft_FbrIUBumNfkWkQ91m7mNfTJKDeaHBcJdc87pyOP-PGuapoQvtOBsqG-0vJGQ8UOgWGz-YkBpXhRTI16vnRLFKJzb3UpIIPApLz8ZQ2B3foMWqQPWCzMtVbuQ-saqJPOqsS9ABJPBwuHl2H3Jy3k1x3MBCwDe0rRw6uHTIJ3Lq7p5UzZCvNhjlTrgcEzCKy6vidSwKs97tshD8CVs5FzI1YuWL3CPwY_K3BgtvHL8E5g3lb5To0sH5YQkS7B94DrkYwhncGAL8Lldq5GMvY4QSdfcqbETUyO1L85G3Iq74743lZW432sEnHUXQhCstk_a6xjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=IiFjic6ArHM9-v4ft_FbrIUBumNfkWkQ91m7mNfTJKDeaHBcJdc87pyOP-PGuapoQvtOBsqG-0vJGQ8UOgWGz-YkBpXhRTI16vnRLFKJzb3UpIIPApLz8ZQ2B3foMWqQPWCzMtVbuQ-saqJPOqsS9ABJPBwuHl2H3Jy3k1x3MBCwDe0rRw6uHTIJ3Lq7p5UzZCvNhjlTrgcEzCKy6vidSwKs97tshD8CVs5FzI1YuWL3CPwY_K3BgtvHL8E5g3lb5To0sH5YQkS7B94DrkYwhncGAL8Lldq5GMvY4QSdfcqbETUyO1L85G3Iq74743lZW432sEnHUXQhCstk_a6xjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCGZN7FvpdW4LLFwcHTzvKNYg9_bx1rP9ZU0fDe4kLbaBhdpkYtvwgITqt3XKPBp60D6Z5bo-VT3pdCWH6DsnjkPYX62KNbu5wGrLSQGUhJcfSfDErzO5LB9UJaWDQzw7dcl64HnI8fCnNQSqfszz4JsQ1u0LcNDlBUDe_9efkTdJxlEZGC01LxUo4hkHyzQxuVQc_KcB2lKOZ_mwHcm_0i0ODkoM0lV_26BI1BGLdJTSEvOcRNLFRdXZsc2-Y5SftVeAUCD0gj5-JeIVXi54RORMvTvmrKRyk_fOGW2TQiNGlZTqQwnS0cfM1Oayqa4e04h4z3kMzx_pts2x-QXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB5rfM6xAVHVgqN0Cl8YDlXcozOGYdApO-kAkEVNCmRm-sgEN3a1dVd9zUHsUYP08uktdP4y9W5s-U28zIhJKS5UL_LPLhVoKTXS-4UGzd5EqXQMkcFab7eCg-Zb0FXFeDmNdGmGKQkUp-6S3QpZ-aE9Zx-ZhdZ9JQMNUBLGbBbSurODa2uzWOhf-1XX_DABM4mS-K66V92ffouMmTXR9RbDZxJghvbH_Q7tcezEMtaXb034_ngjRyoNwHxUe8SOTMk9NDdYn4l5-apLbEEHKxEpYUVETMcXVYA9UpLc8Kz31yUIWPyUT3R1sxSBHF_hG0I6cCvr8DvFOczGCGMJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVfb8n7ZO4-LKh23gOkYjaGyRGGgpV-suX4C60bgTL9_QRAcpCdGdD4qPslHs-sI0YUUvDznGVPiOj9AAebvhDZRqLbks-YXTC8SXt-OKUgLfXSGd3UW0-i6tQYjucEB-7NXmANkgouL3_1qIW750uT56rGvCVv-SaCpNYlaL_Z7QWoRqFVn0AhEiHPbsMmft5eksqoZ1VBzS6zb9CsQMROEf8NCKo2edwrRb8UJhk-Yii4L3LMfs7jMVUyRvavPp9kmxz1v0BeWfz1iExpD7hWdV46Y0GnvBsMoLH86gy9ZQjpULrfn--gs4MUlRm5pb5DtK2BBYE8HJNxoTbfntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMEnRWfIcbIC0c3QFR_Mh4ntN_M44FOOuM84oJjQBGJOGJUt6za2W_l37wV5bSZnV33qsNmgzwtVy2ik2AaJIkh7ZHsQtiZPikNpOq9yIQOEQ_rhDhhrfmyKwrkhcmp2-3TER3x1woaz1hd8yBUxJkOtBtzHIlBC9pU-FRGJZDXox0Rv6dEazU1-8emRQmO0F3rR3h3gWTP0zLdvB2mLUJBUIjcMFa3Mnor9yroEgifRnePNCFrA2YbCnvl-y8HXrouPkEiUa2pQnm8zZPNK2dH7Xi8-bChhkYkGoimKMI8cxkF41jGhXQ06pkjRvdu8s8TJbkG3lG5PnK5dzTVDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=kCIXWeI2TXbUgoExbiNqIHki1vpUntHj3yOQPagf-DoL3PtlDNBcm3fVqOe9ha8O4b-MypmvHjcFYOQjFMkH7-bMH-abiTf6cAlUq0tg-P-Fsfg3zwML6Zi8wJzaK-OGoLDJrzOlWAyWdDXFXaBHUPMKpFImy8bSxD3oidT6_dV1IikeJXE82EoFock0te-1c9MjafhMM98FqLxZYa_9xeGYciQ35fAtq2DoU6i3qOUEAM7AF_2vAVrgndFhx2OhJIYQvV00_skZ5lOsQTwmFQNGubKybHIo2L9lDfcZf-_UXnJX_-R6pFXO4gk060r9n1Ulz0Xipp93KFJ34PXkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=kCIXWeI2TXbUgoExbiNqIHki1vpUntHj3yOQPagf-DoL3PtlDNBcm3fVqOe9ha8O4b-MypmvHjcFYOQjFMkH7-bMH-abiTf6cAlUq0tg-P-Fsfg3zwML6Zi8wJzaK-OGoLDJrzOlWAyWdDXFXaBHUPMKpFImy8bSxD3oidT6_dV1IikeJXE82EoFock0te-1c9MjafhMM98FqLxZYa_9xeGYciQ35fAtq2DoU6i3qOUEAM7AF_2vAVrgndFhx2OhJIYQvV00_skZ5lOsQTwmFQNGubKybHIo2L9lDfcZf-_UXnJX_-R6pFXO4gk060r9n1Ulz0Xipp93KFJ34PXkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnbQ0Md-PmMibUUsQNkdPuGQii6E4CZYY_1crv3mwOd7Xv_k2r7Uvgk9Gf4qJfIVxmoqAmhOhb43hc9P1ut7dJZjvbC_VXGDz3ZJdoyxJO7BZERjB-fUIIkVnL1x4vBhh0Zr3eWflxAcEt-xLOrFQ3Nucnf9myrPQnHwq3i8n8tmcNaz6AMpUWbgWn15LwqoC2Xye16C_dO-Tv9DN4hyyKvtXHG7ud2akPr6jbQh5WQ2QCNYCqSu1TWYu_Dcov10N6xkxKhgZtg7uHr1aKm9i99W5NrQbOLJJqWqP5h_jTxZ3XaZsfOIXDFOcciWzCwVRfpxcAYgWLwTcD00goGyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z67ekUAJbjFSFBkbW26zC3YSKSXLAyGDPYpweJ70IzRbK_EfGWxKxDVVbKGJvwE03ruivbpW4r9Vj8dtXhUXUuUxCC8gTvK4ta6aJV7jJ-SMbml77s0Tyo3ycJFNced0WMDiL5CClOBD6Z5NesA8tBuy69GZby8PCT0p4p_TCBQAcpSRw9JDR2YppBfNpfZAz4DsoS5ICNy_lseS1IF0OEADTKWfsr5XYI9SspqnulMndY-a8B7xtBvvzIfviOTgzBo8m5ursCVqVZa13NeX2caQbLhxfndP4VKdJ4WIcq1X6H2DryoP0M5POhRkXrXp6EOl7sXM6DLAJbWVR7NbKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTAQaFy_EdtKeT22_RLLfrFv9ypolXsRLL043lN96vm0RqP_VA-GIG31UEGWWGyXXEjcSDvNvaQc4ZNWsRGBv3dg25gvRvchPUz6ZY_8-05oYb1-C-zHTm_PIDbqvZGt7kbsThrpZxjDlYxFvqbaTCLVK-WfC-XpN-IYncqKLsq3PF6XngsNFJD49_XQctkTfItf7U_YxhYPxFlC2i08TcA8imodNHGeStR7E-aYJmPZU986tCrs-CtnoHYgqeetq09IrWgKO1Aam9x5uKZBkQsE4hgMpJhrd1RT7KIgiw6mIHzBXuq9qgU--LUWD3A8bpsnJrgLZFJo_IRoHzD0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYx11QH8RTVc_moQ8yT_iJPc0uFboBMuEJoHwYCWT9KYJdEEFrP99sfWbNxmCH4oKlUX46R2U1c_-kZ8UF31I0RzFEm2GaUmehzCyX9ZrP2ccQasyElHKuCe6IprkGX5pNU2baCFzDEh5kwrVcu7BJWIIGcdY6JdC6KLo_QLTQl5F3UVA2KI_1FhPAsuOxn_3yPSjqPuyQSh4ibUpI-GTImjbINMAQc4mNRGr2hfgneUNH1OVe6GwgO2cKPE2RAGpwoiiInN74aSObQTmgiD77CdDRU0IjjxsjEBEgVt0aHTRx-LfLNu5sp-DThjrwuJiNugfQiNmbJ0qrTn35Kp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFPB90xdxspffYAzvxTJFYl7YexTG4Ysfy8b9QAhKkaH39pQDi8CvWeIos8PG0IbIqRik9t9tsnr0i5cd5QaBYfFirY3iZhHNEcoV9IUuMpVQZXpjN9fR_sX3n5ZmlelAY9G6nZE5Ih_pWcEWExaWmQ5NLKpWgc96giExoUhha9Y_5_zrGEiXI5Mn-sF8TKOEqDIIwiyroweq-BtfaOkpCU5CzdUdvI6sjeo3vWCwjR0sbLBkdIQxAfgSCsgiEjR-LjNbjbxiByffEi3e54eDPTCT0GO5V9JAaH4qzggMdyBxbSBjdy8ccOP9bwOEZc0oKm78IHGQun6PlDCCFindA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgcgoXNhGKBD52rjLZKxbOdF2ta0rEdPoUP9azDYDbKEcMTRhFcj7kD578CfxG1q55VczDVZDxJrWdZtTvKCcUMqFS6RRUnV4VSNxXzcpuhCRcCEQ96TNTqD8S0wnZ5Iz2Mbcluke3pVC_SELLk3ddwDgP0fakgv3os5-I7NaZO3jwuU5dkZe68XrM6LRt-dTktDhtYmIWLycNdUOG6HSuGFmZhQ6VispJ6HLNnCob9XLtgd4B-Iw3a9Qkm19Ls68lNGkpcJhuU44ges58MCRT94o5iP2qSoflxfmE4TCkRxmF7GNB3zn2YHC7rFa42Az89gzBxBhVyz-kllcWIgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK2gQY1ZTRya96wUJiFg_VlgiMkZQPMKAL7mCDXlvys7aLMTy2Asw1D15wCMtVqSdPO4Sc6lzoiUHzEPyyCmqvdCihcaf81h0C4nBDG8bsYQDvmD9hdfBN0pEomsJGDYUF2HMH_rINwj60l6qH3EDFDFaknmSbromaXiBF7i9gxNpU1vmBwpza5AG0GC8f8RCceEl_awl4kTdR_ABn3fUF1Vko8U85rorLxdXcbAWvaI5cBE0FsozFnwV_L_ngi7OpDPMNhNRDxVWkzyrVVBFh-_W0NZE8CUMX2eyXG5OM1K7UBqm607_agoi3c1QvPWHQywFsUreqq85xb3jE50MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=EZp4XIu3S6mLsqdNRGYwAB_dd1MYJjwTVQyq-zUAEnZZ8ExVfZnH2QPLwo5rr8Rn00YBaZdTCMUFNXijTVl85bXflvGJIxOzFrprEPrI1x4I4nfCPGBP_o6Nv1KiPBs_0VLN9OlbSkhxWSefTLf8G4vwl0sec4XOtf4s1Fil1OCLq3q66g63_Nhc-RTbpkqCqE3PKCDhUCifwtVdb6kiyc4axhSSWgTacpKwzuPPeRK6dg05CLDI51Ouz5GUzirIlPD1rswZw-o2gcBfgqzH13mbwdbqLb_Fe_SUDLeNsh7YX2thTlt8T9NGcTBFgn5oN60Nef3RLkp4iblk0pUw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=EZp4XIu3S6mLsqdNRGYwAB_dd1MYJjwTVQyq-zUAEnZZ8ExVfZnH2QPLwo5rr8Rn00YBaZdTCMUFNXijTVl85bXflvGJIxOzFrprEPrI1x4I4nfCPGBP_o6Nv1KiPBs_0VLN9OlbSkhxWSefTLf8G4vwl0sec4XOtf4s1Fil1OCLq3q66g63_Nhc-RTbpkqCqE3PKCDhUCifwtVdb6kiyc4axhSSWgTacpKwzuPPeRK6dg05CLDI51Ouz5GUzirIlPD1rswZw-o2gcBfgqzH13mbwdbqLb_Fe_SUDLeNsh7YX2thTlt8T9NGcTBFgn5oN60Nef3RLkp4iblk0pUw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTeaZuf1yNMeYMMVUvrOS5CQt4QwQGG1K2X7z2Rg602y8bCeyy7ylWI_zGyNDg6XSxhZzcWznC-njcG-bvUfwoSoDDNORN7KkaCmqcZ4HaxlMC-Od7L2XBqXupSJ48JJJvGZkL--9EeERsMDZm66P17yOlVKyqQqkGD81Iy2tr0thmMW3dwZadB4Xg0qFfc5ZeJnPEgl7_mxgh-pX9pOOwRFwmA0uZx2Z4xph6PrbQFih1artStXUjaecviUDyXHnzJ2Kmy9X4UQaXDxkY47J6aw4oXABZEA17bjYlZjN7xvNEnP60BLessTVapw97TISCQebyizUJvqeZa6oU9-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF1M6aYAOk6zY7BTc0jwYyxOHd9upCE3XLMfxAiKYhfkdtJLgvjYYYx11bS_o_TaIhlbp8M9rqJCzZqUrHVePqadSh09-kMnZ2Ic_1CVBjzBBjr4-hyGKsKjyCGvM9-YxbbUepbTeivaIAUZJDvWgCFtOjxFgKRbYTM_aEa8Hfcv8MPyMSF-w5WlPEfDcP2LuQQHiuuoj2hDMAZ6w64gypNYc1J0lyxvchKxJq54Lp2FptQTxeZ6yc_wRIE6wbtTkMCYQ_1Lyn1OlkST8bVnWfEPzt96Ek3cMKSc3yFZeEQJnFScul_TkyAMt6aScVL1oFDsRaTK3Ut4un4jvp0eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJDbHI4t3RgZMavIYaifTaVkscCgOPk0TyddlE-fdYUS0Ndekda2z6FXjJtrnf5uGW_aB4Ntkm6MYwoxcDmfmje2Q0YmOtqFaOK1RyKspFRTmAbsMvzqe3vRo94n2ATxGqi7LLyZLZjOmGHcJ1eSnJlNWPW-VS-gKoWz4dpBUrlXfdToQWnKTS0RLDviaWv4OE9BnebFGtPBFvNHyUVoww9wGXQhjr70lTQdJZjqjSiD6bJevkAxIXiT53eVuWoIZRAF-7daTUgbljukKtg4kkB5w0MQD1VOF8s1r3SdFXZd6230xPdTByQeb7PgSr7zdSI2KsFuBT21C2jVUJbymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTEcPbgC_9KyKdQYN3Y6vI6z4qq3sMwjGr7X3XHMh84bu8QOgt-gKTl2T8W1aRcvhWqsZGRkoORthsDbaleAEFIv0OZBMNPng8YXDngnfwBRPqspmohnrkzq8c6nDdFNWpX08Ibqg9v45uPDYKuAzTvbf6e_7OYsfjrhM2cZcnv0k0H2By8Zw0QMqFV6JrXftL5U58HDyzpj-DQcBGSaCp-7_jqLgnkQPZJi7qEZDgl-fbT0yelxvJxynkuPrjDSC28lhmckInTgq7TaFgWZHC8U2p_Vv9wAdCSCH92xOSP6N6JDl1zS2MmtuE9Mt97KZoyoIhKvryslI7ZeuhmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
