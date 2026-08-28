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
<img src="https://cdn4.telesco.pe/file/Dq17OcqFmiU5UrAyG2iSQi257CmqPGiJqSoO3ByiYqzj3I6QOH0zcsaFBQqPNSuF8f1CgBsG7Bf9X9D02HMvGMFPCe-McFws4zpR3lGQnEdEMbqcps_ek3jjgU8_wUz0vi3kGJUYEbdjsh5dK9JmFT5N6GS8aJbMr0JmumpwHPw-HsMqAJ260zr7BmHjqmVVwBnYL76t8zkkIyJlzPuXnFIRunBP-uYtut4seB2O1xv0Xkyv5Er1AbpHW3AWSC-szIL0tRWWCuEsjfwEvr4yIj_p3i139_nzUxxTiAtNVlorPchLTjjbkJEObHjOXVEyHA8rj0G6DPVkM8P8NfcE5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfj9Ot5dU7_yx6suYbWCGRIlf2xHquNcmQ4rKMVyxTpEEU-CQkFj-nF3fsrLok06LFqdHb1ADoxrc_gQ2LIRXPrXlt7b7MPU_uoF-CMPifSuvKTDmCCoaEptBcRqz4uDzp7dPxEloBsk20UL2SXtu7OrxwB9PUlzAre1Vum76iRT_wdQgn9eQTQ3sIz4dAcTIIVKaFngzrKV3iWRzxZqIQeurcjGLTeQ-sUZ5qESxIhjftB1NsbkxIFN6_aAgB48PlxmFvpJ978alO2FnL5Z4KmHxNIUt2lLu5czvBk_s1bSIar0EzsHMsb_n0lOmtWN2KIYZjp0hxoEQMxGS1PvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=IEV5gnTZs9ibCv_JW7bQb7cq85PjFJaEEnF6Tzsirfb9bXnC_3F3soRJxD7xQ3nDF5XtJYQ8kSIuwYLAtpLOJwVRpRYf0kOkm6Wd9zDqbLSfIhETj0zCeMRlMty1oAtefljWpaapduPtSjb4AzxjiFSeyQJU2atm2ZIJTrPMmeHM8ifbP_JfPrNpF2uGtvKHHZjPvVea1k5jcRXk-U-7bjBiLey6dODR2ANYze7hFiOC1fnJTO8uawEWfCIoA8y-FqZ3hZrjEdGay2AlnZ6vMPcp2fw79kbmXtwQAped1EWpphM6hO3JK3bWXrYmlkdd-bAQoc0dmVcfkBFin2R-4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=IEV5gnTZs9ibCv_JW7bQb7cq85PjFJaEEnF6Tzsirfb9bXnC_3F3soRJxD7xQ3nDF5XtJYQ8kSIuwYLAtpLOJwVRpRYf0kOkm6Wd9zDqbLSfIhETj0zCeMRlMty1oAtefljWpaapduPtSjb4AzxjiFSeyQJU2atm2ZIJTrPMmeHM8ifbP_JfPrNpF2uGtvKHHZjPvVea1k5jcRXk-U-7bjBiLey6dODR2ANYze7hFiOC1fnJTO8uawEWfCIoA8y-FqZ3hZrjEdGay2AlnZ6vMPcp2fw79kbmXtwQAped1EWpphM6hO3JK3bWXrYmlkdd-bAQoc0dmVcfkBFin2R-4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTq09AwWnQKwhlfxaG0YwJSP6wzt25DWLWXi-pRNaYTOQwRYNMUduJZi5NNTEjRA7QAVP0bJOqCrAKcZdUQe8KrUZLDp3RhaxNFfVXhxIErGG1mH_EGjQ-H5mBuO_DCUMrKkKkVDqhGT_cWIBRqCmbGn2zd8e14153mHaLx1Nu_iP0pRJyx8pWfkUb9Ah2uY7MCbBMXIdWVnKnv_hf33k3wypyB0yuD_4iJLiiNg4J11gSKL0DEJGRmf5h-wIp7TnHhiycSiOClmA-AH9zRLyyahYbPa_dg7SI9sBdB4basjZXT-Fx4y-kA1imzEtuNn3P1Lf6b6sVOFMiz6AgbNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=fVf-wfo5c_YxfjxIrttjrF47r4oxvmm6HEqhP88w7D-pgpq1GLdGErD_NpTmjswZ0FQ-7PptK-hczrrd0yYRMWOzCmfQc_1lOAJ2MsU2f3p6RV-XvVg56ddFkZN2988AiTYrR7JJI4oO1BaehhWPXrXUDPFFOCJiFde18PAFm4nnv2bZooNoCS6RTwc7rsJyfom8IV9uyMVUzMmDXcl6dJt7v9Rr4fz_SfaR3-QFV7hzi_0Lb26_oRGIPIrqALT5Zzy0J0USURLxeEDimWUxX1lxo8MklffAcq4xaNWcA4iFeI6SMRL9NxwcVgCzxnPzEJsVbf7dbomv7YCvDuHJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=fVf-wfo5c_YxfjxIrttjrF47r4oxvmm6HEqhP88w7D-pgpq1GLdGErD_NpTmjswZ0FQ-7PptK-hczrrd0yYRMWOzCmfQc_1lOAJ2MsU2f3p6RV-XvVg56ddFkZN2988AiTYrR7JJI4oO1BaehhWPXrXUDPFFOCJiFde18PAFm4nnv2bZooNoCS6RTwc7rsJyfom8IV9uyMVUzMmDXcl6dJt7v9Rr4fz_SfaR3-QFV7hzi_0Lb26_oRGIPIrqALT5Zzy0J0USURLxeEDimWUxX1lxo8MklffAcq4xaNWcA4iFeI6SMRL9NxwcVgCzxnPzEJsVbf7dbomv7YCvDuHJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8txP3NabPG8i_a0gTDWW2N1f5IKAfLgsIw8JF5SqlOxdBCsso1Vp6A8TlHEh7vTn009ua8F17AXBCAs-8XHAlb30u58LvrrAwRyxhULgsK9pb7GYLlb-LDderiuY_VJcbSHPrpiOW0mwrW4SKQoguDfEyCmZwdN4HSzjNyVgdrV-gV0iz352dxz16J9YcGITp0LX9O-tPkoKmxnC_6Ezmvwpz-xgy-43dnbAeVFyl_Alay_xeAWjPzz5rvjbezN2O-jqPvGOiq-uSOVp6tWLmCabStZTbUNVee1jw4BsoY1g3AvQTQWKdxYXRDgBDPG5MJGwziPTbS0kB7KhN_WWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjkR9FhwnKk5tmbWA5H0GEj3IZIUUkMqPcTSB6lZYT3F3UMdjZmBEuT_-H-NV85GMGF0IWNu3GR1cm3GgzCIHnwJYOzHJk3spePq4fl4MIdbDUdKL1vSNBZDLPgPleXV5CvspBbUSardbCjbpQV67XKWrHADPVdMPgQ2BytAm7b484Yhp5T-AYE9mn8qx1lnhKZ_xXQM0TI4Ai7eWhw1lNhGZxQoVjIxvI-Q-mzHbICwqJVkEx8WQjRW6tTXZSQXDWKykiCshtOs2e_asfRA1RF1AiXADq9bn-9fGEUWqRG732cMTgI7cow2m9wCQ2tbgD1s6yltVV_IDT0KpRrujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XV4nn8_PT99rHmG9iYJzjk300jaUDbgOdM52yFUYgsWQLSIDVR2xj46Ji46Q0ML1_2FqxgIjZc2hLBWc3O2wqqc8lW9jzKZXYc4XfTKm4ETaFxpafAfT3TAlYjRf4JFNmGXXDMGaEXYiwTGbu6P_feZptYFwcO6m76dgHEF1zyB-pf9sDMgfv502_8_wYVcaCmnAMvwS7OCu8PWUQlITdo-1Knz6bgqKt4SSIeSzDfiaHWPbwmXc_AAX_TmWsysa-crcZvnJxpx5cj9UFW3s93LxEmmf6lburmsKdLXOeYVRijbVEBt8LoqJea5xgrfKQ-J2FfPnhAMLapVRalumEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N01_ySSJqWq4lCm3r3rPqnaBFSKyBZGe5wkq_VJuoRH6PSyW2iH6LPlEqH7HDF36gRUghnrQhPtrcN0voRP1pDE5MmdrR51huzDh1I-QuhQs7fc0IUuBIucr1XMg_UMSRWRmJi8M6q7BshBsH1wEmgj0qc5qGgSfPCu_1g1iR72wzaMJ-VqWrtg1PjATzI1GdlHhAul7atT8u5PSo1Ii68E-i4IQmZVSno774sLPH7yKFmDmdvIambQAJkMYH2Bq7Yr9aMOzrU3N1kDAJNzjsLIT1xVw6Hl3SaRkE3WRicHWD20G6ea-57CwkA3Xf-hS6kdP5T-CvKnYI3lSYggKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuQgzgHMcma3qEyH26YChtheIncVvUm_beBz3sSadnVVUTPrel_BEVR1ExvCH1Zw63g_HQmu8nOsudNOvz4GlHwL4pIfHYtrMqluowXlKE58CJhonx3_cV2Bw5UgPq0oc6sy5aKXpO00VGV81COLzviIeiQ3mg5N1LFDRmv7YzXnadoF6_T2Nowa4JLcqXRPmP4yYqxfsl39FmIvbikQB3ZIfws3DQtR3xUEZXYXvdwOo-4wBrTsLbXrkiScUz0Ia-WVGqt3c7GZxfgNi2uJsMMTLsD9orAmhJ_kOS_v3Porefe05ylsSkquCI_DIY-ao3zzuJlAjsRbIxpYIpUgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qht8_V6ZpQES9WkQ0elz03tXNeuP8bw4c__KGUtIhIvmMF6-xCrHzgtIhxoFsgdAZXaldaVfzZxlSGiubGZZcnzR_Pc8YW6yGwod2uh6frNd1-BQfbEM0CGYNC4bYzs8LjXPCng7ClXycjYD0x7qfjj2WdLoZMx-KjH56kg-A4M-SIr7BN6eMPTB8z_nSNaPkVi9a5QIza_yUgamcEahQW7p0qtcomJqoNfWzVGp19MYUOayWn_DG9NLzGsKzQw30a5IeyjF1tmXPfgLTJJOqlzq1IxV5DX4mB4AwzG_Dp5zFqpkEIyUhktvhjuM7RmS3Sg-r4Qms8WOhu4Q7TdTHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFTgGhhS2hic8UNWu0umCmA95D0aHkOq2WvkodhZ9ymmOtA1Hv6NF2J6eCWPrFSioFHuGzOVvfyqOMXFdwI0lurAfnNZrF30ivfpw4Kydipmo98YxJ4iCudIIPszUMbvoP6-9QSfc_J5IplZ2qUevmZm_-nl_bvQvLO3VZEAkNAhYEbyK9VjNanYMzuzBec5VFb5CreE0eEENOHVVRd_MpF0v6cZUoGyKTYGTha8_AiPo_mt2UHpY3-6F562e7cRM5TkdeyrhSGCVC8OAnNjv8Tjaq7hmnIrNhg6ZpQB1QTcCdWiDelK8-lfeALeYooVFyu4xGYJ_flM2Zrg1AGLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxjoZmvyhzCKvM27vxnLQieExPuCH5VU-sRk6FDQl374xYMj-uZh8tU2LH1pI5w4-v2nTWseTFkhfs93i74qllfN976GFahGiSeK48EK2GQPjKTlhRcMXqn3uVfh2IDFhHFTiShnripA1Rr7_mPp2WTE0UrlwxP3T67zvTUQaGseSl4tWcdz9ItzfitScB8s9EI_7zHqSyipoSOK-Y2sCPfIBViwDFJDLq5Tg67ilItRo4JAgRbedhWsAHXDBynz6JUKmV2TVYPSsOtYwcbLMyAq9F9bOJUiLUkRxCDaGHAz_b9fseURUFY3R4PneVjS4xXnWumTJq30vVzyHLx9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6p9XsWIhyWNEVGsBWDgwJiUkzomhgkImHLhUMO0sJeNZK8Sg-BgKkm9fwiUZRQOat2tQItf2XUy4VFA8nXD9y9lkMXY2FjMb8cYC8SK37lOspR7_UkEy5klOaQD2OmjAwLuIGo_RyApIomjDLAHsn1nCQgx1IOglu7W0ZINiGFQFm-kdPW2xG6q2RKDjdDjZ_dayOJtyrtNyDIJpXXvJgBieypu2k_dd2VdNzAT4vd6il6YSxI6MvdTOau-fydFv57jwoVOBjqciLecW8NvHtSKJ6Xc5EilfHzGEA0cEakIHDSgo_IPpUjsVoyXKjJOT0nulSh5CwjTDcudfp5LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dStuYRTxuDXO9Uiww_PbzTXx03jSqHmojQPxdK3nC8nd8rvhpEZmyoD0YsjHmu_P10Rn8sqHtld_75Yauo9jVcirsNNAh9CONehP2mtMWZFgRnvcUwVVHDxjfGzR829hMtrIvpTSGhVyAWDQKMoAzCrbbMgC9sOZpOnLa4Fx8AijQh3aG0CcadXw1M2bON5uHpbuXL5a4_6eyB0-1cJQBnQiKV7R6qXCPDNzGgBdwmDRYaTBdjqUO9Ljyj7oSzHkFgyG1Dg3F23CBfzFg0Evnnu2Ii4djFgM5Tm98QCAWsWT3gL6MRWulNYHIwfRxJ3_II6JeIqN9QkXmWMxvPgoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrmoTKAOIRLlHGe2joQTchfHTOlnd-9ovJUUpe851oW1ZRnDkbYi4s5dwFxlWYaLzsV-Bh93vVP9K1pXT-7LyCjEG_z5NTE0A8p9RGPq1hO0a1BNSxCeHsFx5vt9nnUMgkAqhubSHUG0KlTnfKoMPCzGAbGrqiCDexR7Un_0QqlT8D_VJV302htMjTgoWT-jVtKP6igdSOllBB4AfcLxqjnBtQo3wL7WPoW_-vTRds3SyhvQ8aGMLX60I_IBHoFqswmMsIr8Br7tHLzD5wXp2NaCG5u5DHM2i4tApBqsVvabsx8OlARmnh5oi59sAVcRbuEyc4PNFukXcZmN8HREGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfZt8ApoTsQxOc9JPkIjdDo1Mz0SFPFehOkzfYWSR65o42D-ZlJ1sG6d7zzgkj7cFnExnipVVajGALcNx8SF8feJQxhaDR01YhZGPuVCt2jVoBfklLTX15e9ERd05Jh_RoTvc0GOAoc1V7N7rxrPsuVUzir5r0x-kTlnp8PU81wmgRcZnzrm_FhFife4QD-bHagBqBfAwIGPQ-vZBpPCWlz1iGOhxOtQkEnkQ_pNHkcwOMzhUNxSol96gFQNatBnI_oInXCQeyZqM0Ug8c_3ESW7aoykorhRMkLOeWK5KJlRo9tmUzxPx5O8KZSzor92wohYODFSMtVUROKMpJsrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L19KkF5gxL946PciyoNDJKObrBGc_oSKUoa6ulh-nMaS0UN3qr4f82teKK07ek0GXOlvg57uLn0Hl7HZwlJxtvqiYgwKGbS8pJwGgAEEuNpFITb9Cs9iSTwju8-CjS9D6vFydeBZBD7RLxtKoMtFGMXUGB0iIYpFrd5LvnEb9Ra2h7efUzrgwc_I6fe5oueeIxT1F8LnC-dqCAgmC4b5jtGii7LaF_b4nX-7OGGYx8Vz8NSWTiu_tMiEEtN3OC6RCeAoVsGd2hw1hHPRoID4UTwOEmrkp1TZjRauQTJ5VR4NzfCjXwCHhkn2AvxoRzyEIMn-hy_ukhUj-GpDfk2kBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=YbLO2kWkFdMUlApf6y_b-nwMkqhWt3xzWMwmBNCxnDjCSFlQuJs7jZ4J4vdFKfCI0NwHYRuyHBoJiY72puCOFbUQZLUpQUiHHlMQ7dpCR9OMvckN2uNlS_IlcYjw7T05ryl4WYjZpZBoAfSpbe7iuKLPu7i3LV4flu2j7NKV83qnnbc_12Gnog6zvXx1HPrPkXiBaVvQUF_ViotP3k_2yU1H5awxjzPy6gSzB-MwOc7czUzN_DlaF_NmVzo_d2ksG0VkSh6eTtzXmr8cQrGXqVlWt26EOj0Zn_3paiG3kYLlWxA2yu58DMj42Vrs29RDMpjcQZIMfU9WkL50SxnSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=YbLO2kWkFdMUlApf6y_b-nwMkqhWt3xzWMwmBNCxnDjCSFlQuJs7jZ4J4vdFKfCI0NwHYRuyHBoJiY72puCOFbUQZLUpQUiHHlMQ7dpCR9OMvckN2uNlS_IlcYjw7T05ryl4WYjZpZBoAfSpbe7iuKLPu7i3LV4flu2j7NKV83qnnbc_12Gnog6zvXx1HPrPkXiBaVvQUF_ViotP3k_2yU1H5awxjzPy6gSzB-MwOc7czUzN_DlaF_NmVzo_d2ksG0VkSh6eTtzXmr8cQrGXqVlWt26EOj0Zn_3paiG3kYLlWxA2yu58DMj42Vrs29RDMpjcQZIMfU9WkL50SxnSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=G1XTIYP0OZGBcHy3CUJwa6VV0tgxonjDKnBRdzozvubtCxpfC0zdXeNaPNlXuRQe0dAdgiFKl3zsf1-gPwZJvSbpRCfCeA8fvxlmsVbHVQ_iAIWZ53OsURVAMH2uY5ZcqrL-spPhrqHNM0sGVsJ0hW8YDUuGDl4c5RGYgx0UsRwrycoEOo3isk91r-6ihdgb-Cva-dI_Mhh-DIRKqkM038iv3LR4dUGq3k67fevGVYJINBPksdvuNkJDWiog1bA81wcdUgBP0R0zEnvwxXahS5AbO7jf8fKA8uLF0Y9w6lOb1RZEA1iuFfaKbgB9DluSZQjpi115zcMfCekEMp3pdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=G1XTIYP0OZGBcHy3CUJwa6VV0tgxonjDKnBRdzozvubtCxpfC0zdXeNaPNlXuRQe0dAdgiFKl3zsf1-gPwZJvSbpRCfCeA8fvxlmsVbHVQ_iAIWZ53OsURVAMH2uY5ZcqrL-spPhrqHNM0sGVsJ0hW8YDUuGDl4c5RGYgx0UsRwrycoEOo3isk91r-6ihdgb-Cva-dI_Mhh-DIRKqkM038iv3LR4dUGq3k67fevGVYJINBPksdvuNkJDWiog1bA81wcdUgBP0R0zEnvwxXahS5AbO7jf8fKA8uLF0Y9w6lOb1RZEA1iuFfaKbgB9DluSZQjpi115zcMfCekEMp3pdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdSGAVc_h_mmxj7mBaECzeJuMS52lJTUM0wXznX_MPLLY0N9KbaHIw-6NWDkO0kk0IHZudRqBfUkj6Nhq9j3oVtKsN4BXX-EGEF8Lul9QyzzHuXzrFgd6a0-iHjeA7d1ThjyGYhcSaGwUGRhgAU5WneYVRVEBtrxFmtEAZqfHiiBQuvrWcH7ffAg8E8nqVLm0tSLGaB8Gu48BcCtAoMqAU49_DRevSWzIrjKk8mYzWlQjLjRVPo13sdhDJEnIv1sbWTnwQgVhWhukHXwg9yo3j7JBWKIdbRcYkmcn18pJfgCUW1VorW0xHHECa9k9aJ_co0uwPz0PqKjgx7dQi51hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXhDNcz2TJgAD-GQC6QhetAh_a0azuQEFs1mL-XVgeutjQEaaU1qpB_9z0EDCuNHb_mX07VkwvF23icaoIN00pAQISgBOYgjxDQYMv9f2AoidKpu9olx3uylrDZ5KOyMEINp89deYcKWerN27O7tOgkuOHIkoLWgKGLAMvUiMoP5rRyjboUMtsfsAUQKdkUfYKFXpb0uWNQ-vb0yNNrW1g8u_aaL1quNeyrXPmZzCG8P92gcpC0sx83mE0gbt_wthVqJ9zbmRVajpYGPzem40nl_XotkyKkZ7c3zdiUonwU1fK4o8U9Hqcln5wIv2eoWcKu1vX3qs9NPbaFDgGgl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTdZoo0PUDMZMnqjCMzgSBoI1MvOzE21EiVtcgfEhTsTPg3m8t7ax0lQiE2X7MhRoXS-Y8lNv5dLzkDWutfD473hltlvBqfgfDOsoa2DrT79purGjJPJoKHfbyX3CIxt4-xYKgnBcoQ75gtNK7fSk7HhYHVyHaBg3MsenXVNC2wlI_FUlrMqgL69WXsBsn0B4cSe8tS9LA4wi7FpilBKpAoAr-tLgLBHDRfjWUvjznKdJcn01E6-y6osC8I4PHrlGnnc-_2N-TR_LvFC56d7vQtxOwHT0WrzA4XFAx9P3QOSw5o6okll9W_Za5rfrBmjNp1soAwCzuoiTfAx8NmrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=OXjZLuSEqBjcZ9F0p7eerCEo0pT1TqG4jrfyxS-W5BFba9FL_oNkkr4OAuj8Ii45vD9_cDBCBF9ZhWz1DyA9YtUt_X4y9qFMiGHi4eNcV86u9EVFmvGHOzqavBPRCBXia9Vp3QWxulYxUgxAB6xLiirC8rEKcnDj7rdAUckv6JSSOMwEM7NCJRgE90fqE01aAkFQrIkCtIQN2xTrjJdH3blSdcL6nio74OBkwc2t_JGKQ9Bh-bYlgKPmcYLwsNH6829OZzoIVLir_3ZUi2bEKvUw2nwprwNTwrAqzhs3HaSj9LsqBhVKNAkAEZtZaBs8wZfwiI2DxTxtFc9qztCvjGywKhIBVFAKzVlSxNmq2V2Sp4XwHyNW2wap9Qdi9r0aCly3jkEf8Malq5cv409J5F6TTEZ9zLROcj93C7g2SelDIu4FFBjnv5oKcl4pZ6JtuDsgkx3HM-gs2sEcOzQmMLyJ-XbcV0i4PbFJnfCuttXUKA8Hw02e9P3audsACfGLoqupbNeeE48bd782CZy4Qtz3AHNbgE5QTmfO1cLjRGn70c-s46Km0_OJ09lrBVLb2csK7AUx2N6G9EP5f4SkVq2HQhLDsgKcdwi4AloLzQNTV_Rn_-Fi6CBrSmdVEPVQUdGN-w2r9ho7GUibW0i7XSkjTUii5RTFLHT3PqmgBfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=OXjZLuSEqBjcZ9F0p7eerCEo0pT1TqG4jrfyxS-W5BFba9FL_oNkkr4OAuj8Ii45vD9_cDBCBF9ZhWz1DyA9YtUt_X4y9qFMiGHi4eNcV86u9EVFmvGHOzqavBPRCBXia9Vp3QWxulYxUgxAB6xLiirC8rEKcnDj7rdAUckv6JSSOMwEM7NCJRgE90fqE01aAkFQrIkCtIQN2xTrjJdH3blSdcL6nio74OBkwc2t_JGKQ9Bh-bYlgKPmcYLwsNH6829OZzoIVLir_3ZUi2bEKvUw2nwprwNTwrAqzhs3HaSj9LsqBhVKNAkAEZtZaBs8wZfwiI2DxTxtFc9qztCvjGywKhIBVFAKzVlSxNmq2V2Sp4XwHyNW2wap9Qdi9r0aCly3jkEf8Malq5cv409J5F6TTEZ9zLROcj93C7g2SelDIu4FFBjnv5oKcl4pZ6JtuDsgkx3HM-gs2sEcOzQmMLyJ-XbcV0i4PbFJnfCuttXUKA8Hw02e9P3audsACfGLoqupbNeeE48bd782CZy4Qtz3AHNbgE5QTmfO1cLjRGn70c-s46Km0_OJ09lrBVLb2csK7AUx2N6G9EP5f4SkVq2HQhLDsgKcdwi4AloLzQNTV_Rn_-Fi6CBrSmdVEPVQUdGN-w2r9ho7GUibW0i7XSkjTUii5RTFLHT3PqmgBfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLyPY3iLIZ-WA1N4TT83ru_i_2f36-hyxAlgkcVztag3ih8uxHA0D7vHrs4swoHPwLEi50ZlNJPgVEIq8cSuLKbXMnoigqjZOKH2uMSNHjo7Gl8VxS2YlcrVQXXK-W1v1qA3FtapPVoKf8v4_FhpC5KzmL9bEjijJgm5cyzTNAPxAPmmBEYFS0rN6FGw08GmuXy1jLC9uszD8Yq0P4GJDT1t_iIp1qWtD9dglzEzQr6RfjRMaZK6OpR5DR6UQkrPRpRIUNFXOOZ2OcfowlQQPBughrtnz67sIc_9MGUSQOfWUJ64vqmzEQEKNHECzPpIeBwociD625lJxerk262feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhWUq9AntiHQFKZ70zef0ZcKbD93tGVKJq0c7gCvuSQzhz08G1u3bPdmeltOwCFLty-DmW8iu9VIwIcQtG8alA-LBK3bASfpt0xyjqo9TKjZChe9ESb9s92kCm3XA8JJTRg_Epbc2FkLELzyHTisugcvyeBLYJKDTfm9-GRPdlzKmIVw80W0r1hlC1QjuzP7pNdL8n6SG6qmn3Kvpk43iCUpxDLPBse8dqPGTQng_7F6SiqOMKSuoVmFHAEopB77Vp-fW3v1w1Kvyfag9gfei6ec79DVNVGSZRem9P2MJW4yxCXQrARoUz6-dyl6K6Qnc_uPgBmF3s799oyh5vyllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wZ1hY2h5XxNndOuvg62symu1heEC11dUmQrDUkT-tN95VUS_0HF4sDJV6tLoz76GwGceIlr8WdcaYu24qpNZBH6PrTWFtpuNCreJ4xmWKMDBrm3hFm1ESE2msA6E_4wWyBsSYN7_WFBFTZB7UzRzREWKo352rP5zOPZLgEORje-OwxWPF8-3T-_6PaC0jmA0AlfrHvw79s7-W7pKGciyhVuaoJzzAi9Fh7Zx3nMba3hjXGAhdnHjXffEUtI7VyrR_tQzOLcyWxinVqXzdJob1aq0EOMm3M9xrFgH0ivyY_J61Elb0Z6s41yYYkXKKivE_x3Ao7zMtHUBMk6I8WUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_pMyB_6pcuVq10hkvbLf9iliZKraCttTCXBS83ey49zdQRm08iy7z-7pVQOqwe7lbTXBxc48wupiGvMakpmrzEEuB7dFtyRMiZdgV97SkCukz0A3cOcOqgPpQgj1zTV7UZv8q0zWEqBhsgyDj1eD3cA0w5TEJVAFmLqEbPrZmaGdOMZ2ay2NbBdYRHwtDSj5E3Wkt7NPWhpFxoLwl7Yv9Fs6JuQ1jzQzSR26Gn5u9xL9e9Ey8Ez5Km-FrAtU-ZgQIlXwJC6rlOS4XAQrcYcPB_N7J4tn3UuiPMDd0AYsxbtjZBDHpbSpql8hsr63zDG-wSD5RkAINW1baJoV9aEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr8EVbxIsowlXzpZF40QVTueWsgjNcr9NuWXYrBcM1HyZ3vDq3P-sC3Zuzcgo3xzgOhjEtPWwCTSQWUdyQuucE3XsXZTm_c4rp15aEK_5kKJRr1QEpEcgY_h3j075D0zRcK_28D6an-0ZSbpkwUPmE3sOuqGZ4rJGrJSGZ1w0IWcoSYRFXGB-vSNd4EKCMTSbW-fnT4dndkT-NQrjk7_KiEHwDxcKWy5DQtQU26rUyMN7uBxRWTfsz_DqfsR2LPuW4gJqjJcyKWme6oxS1gioltkFPw-pZPOJMkyBQBtq15LT_J-1JTCci_COMT63GQkdVv2EqdkzpSWxzoa8mOihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVLUTIAFx2Dh1a7miGYxhbKEp-MBCXRrARxlbRRTYkE4f0woPO6_kGoY7o2vRTdj9U_eqojGHi_w_Ue6pDWuXii0VCpbz-qNKu6rUslkGUfFhIq2CN95sdC8KTDycbXjetUhuvvwAe_NqhBddpEIXaP_G1zdV7UJIeTdH_PQO3rPQ_T9rKPutswD3rwpi4v7QEgwdNqw4cplZHRqpxndBoUjfyZcphvr-D6s11Hcdc64nkuIDAhi8F1IwwjsMj6fyVLV0iiU7izY1mSU24Cmg6pRxIqRRsYAVvgHFRIl6Yv9JDn1tqTlS6R63_aDrjjFITVj525nHSF4g08mraFruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ldF3kQKo4p_R6aQuzmioW0SfSMxpTyYCZydiuCbV9MS41Ue-44aAwx37KhRnPimV5pwOiaWPqYXvK47-5ffVRku5pTitAWZxcHRFYe595XuUiiYDaQGc3CZ_eSD063U-7RQPEgqdCXDXvxgVypBPOkqmJQ_S_3fbH9jC0vgHEivJSaNLEv6SovKmNDpjrGAz9aFuu2yBgKtAviQkJrie59v0Vj8r9J7eXlu9OZx3ajENvzNx3WSGH7JSA2dDLxFsBFtyOL9L2XYygeDVFFE2XYSqR5pOCtyrSrWHz8zpBW5uN3hgnA3Ruar9XYGPajkc5nB8pritBPr1vM38gi7bRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=ldF3kQKo4p_R6aQuzmioW0SfSMxpTyYCZydiuCbV9MS41Ue-44aAwx37KhRnPimV5pwOiaWPqYXvK47-5ffVRku5pTitAWZxcHRFYe595XuUiiYDaQGc3CZ_eSD063U-7RQPEgqdCXDXvxgVypBPOkqmJQ_S_3fbH9jC0vgHEivJSaNLEv6SovKmNDpjrGAz9aFuu2yBgKtAviQkJrie59v0Vj8r9J7eXlu9OZx3ajENvzNx3WSGH7JSA2dDLxFsBFtyOL9L2XYygeDVFFE2XYSqR5pOCtyrSrWHz8zpBW5uN3hgnA3Ruar9XYGPajkc5nB8pritBPr1vM38gi7bRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPqmVJgsQ_HkzeaIKhpXF25_sxcPdkga9z9sb9-x0uVDUWpJeDAN7HUmtFs2u7vcrjl2CkUJehUEpBxXdS1iC7FCbalIWfdQ41Q_IHWT5zbE1zl0xN_kYsd_QiiIhQ6jFVz9ufiul2k5jkZ_J3okBZMZljWvn9sAeAblVctCDk3LtNPexs6W3qa0sJbDzuCHD1vXZhyyDUWwpu9LFL5vUVphV2OALcBUNXIb4jOXjm-HuCftVia1UGDQexDwBVWPlf63_dlns7nP9OIZtX9MCD893LguFQ2xUsUe-UcpuUC-cvsYEVOE5ChboiD706w3NdcdIBB1RTqsigYaZvetjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbbwaRSpQfKL2KUdWMhbgLMAI__W1O1mWdkKqiTku_k48cWqS-ds2wCVh28GfSZ2ASxItJhGjH8s8sfX3JymdRQm4HWHLVfqaDSK0HDzySIcP1ICZ6JGpry3kijrb9CHFU6pCXmUdnRuQ6M-bLHtNXS0xR1sGlXW4RHC0-x1cGb386gWUI9gDqDmL_XP5cnLcuBnRrHJdl_-7fps6l6s70HbpzJ1-2eEgn2jE6W7VwBVCSPOrPr1wh7Pq0FpEnf1NLhdJ-zCx-K8KcP_SA_o-rezsonDeICnZVa9U4tcjFKraSEXzpzt9nHcGkFB695V4PuGC8x-Zxh7atJhgioHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlR1dR73KnlD2wW8_RPSgnaY7e1EyxCDJ2CHt0SuJcEPa-N6qhthjjZdLXuuVxlejq2CxkoIEmLJfRBi6Kv9Wqesq1_5Xc-tL09MOu-P12Ps4jGIdzrSUCma7raBlgpG4qfJIozH-L_nbOefGrJeZzLMz6FzL5LXprVjRlM9_L41ZNvM7geMLEeYT3XcaY6k5Le331RzFPZXAdw67wXMlsayZj6wkOlqOFESG-FVQ33m5Eg-AbjNkVaXEgPxlf82FYLrCvM8RafcDpaJKAxy43kFNeE7Vus3mcQ--f7-YfjtkeZQITUhTDNZhv9eqylXvLy9GYqG81C885P5N7Eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k59iMhyr_2qjdbgVnYUCuCbBHggyfpoSeOckJape-yNHh0Kor1GlTFcjpUs7GZ7zAPiTe_cYlI4OlXk2Gc5R9VIFdwG3Rty9HhXNrU_KdQaSLNhWabfCA_uwlESx8gwdHYtJoz1GT456gKDG9YLGJUJJWOpShwvbk412grdT9v6cdHPiEECfqIwrx2vjs3dHGhSPRskFhRrN-ThE07Mmjqj2qM2j68OCsw2GKxdtXdeOy4rLeMd8t2KUQmB1gXWN-MltQZJV-gjRsPA6nSzTcNdeie78iRvEL844gK8TlwoW1MCbFBUfXSSayWtUzYdEGCyIrQ8v3Dl4UiQaD1xhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 میلیون توکن برای دسترسی به API هوش منصوعی زیر
💥
🆓
Deepseek V4 Flash 0731 | Kimi k2.6 | MiniMax M2.7
✅
📌
Base URL :
https://hskyauefqcgbvgvxkluj.supabase.co/functions/v1/gonka
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7525" target="_blank">📅 20:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔒
بهترین ایمیل‌های امن و خصوصی
اگه دنبال یه سرویس ایمیل هستی که حریم خصوصیت رو جدی بگیره، رمزنگاری کنه و داده کمتری ازت جمع کنه، این‌ها بهترین گزینه‌ها هستن
🛡
🇨🇭
Proton Mail
— معروف‌ترین ایمیل رمزنگاری‌شده، با پشتیبانی کامل E2E
🇩🇪
Tuta Mail
— تمرکز کامل روی حریم خصوصی، رمزنگاری در هسته سرویس
🇧🇪
Mailfence
— پشتیبانی از OpenPGP، مناسب کاربرای حرفه‌ای
🇺🇸
Riseup
— سرویس غیرانتفاعی با تمرکز بر حریم خصوصی
🇳🇱
StartMail
— قابلیت ایمیل مستعار (alias) برای حفظ گمنامی
🇩🇪
Posteo
— بدون تبلیغات، حداقل جمع‌آوری داده
🇸🇪
CounterMail
— امنیت بالا، پشتیبانی کامل از OpenPGP
🇨🇦
Hushmail
— مناسب استفاده شخصی و حرفه‌ای، رمزنگاری‌شده
🇩🇪
mailbox
— سرویس قدیمی و معتبر آلمانی با PGP
🇨🇭
Librem Mail
— از تیم Purism، تمرکز بر حفاظت داده
⚠️
نکته مهم:
داشتن رمزنگاری همیشه به این معنی نیست که ایمیلت کاملاً end-to-end رمز شده — یعنی گاهی خودِ سرویس‌دهنده هم می‌تونه محتوای ایمیلت رو بخونه، هیچ ایمیلی هم امنیت 100% تضمین نمی‌کنه؛ این چیز به عوامل زیادی بستگی داره: تو کدوم کشور سرور داره، چطور داده‌هات رو ذخیره می‌کنه، و حتی خودت چقدر رعایت می‌کنی
❗️
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7524" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSjelVKRjoMw6FZv8oo_CxqJmAMfDao1SVZn1Cl3-1w-Dp9TgwB51To6Xze_ulu40MqzC2J9TCgoxhSP7iHpGaHI2qnj6uhZIgVsWCN7s5CpV1ReQkGizufk6ul-OkTsthzuzbTfbgQamjYZcwvar7iG15wjW1SySSdcSvs2Oz7rZhS85sA2eQrEiLZdvIcrKLkIV4HWeyWGEz4l8KhozAJ7cabkNqvpFizRhWdHVt8clTlgyMOBpyWJAozrirpMnub_WB12wIPRLjghJ3ClD0CQrMhAhjX6E6uWabcADm-u3qG6vK_FrbUYxk94GxurwxxO9fNWeyhNC6MRtPzDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">60 دلار کریدیت رایگان برای استفاده از API بهترین مدل های جهان
💥
🆓
این سایت 50 دلار + 10 دلار هدیه رفرال و هر روز 5 دلار بهتون میده تا بتونید از بهترین مدل ها استفاده کنید
✅
Opus 5 | Fable 5 | GLM 5.3 | Kimi K3 | Qwen 3.8 max | Grok 4.5 | Deepseek V4 Flash
✅
✨
مراحل دریافت:
1️⃣
ابتدا در
این سرور دیسکورد
جوین بشید
2️⃣
حالا در
این سایت
با اکانت گیتهاب ثبت نام کنید
3️⃣
حالا سایت رو به اکانت دیسکورد خود متصل کنید
تمام حالا برید
از این بخش
کلید بگیرید و استفاده کنید ، همچنین به بخش پروفایل برید و 5 دلار امروز رو دریافت کنید
🎉
📌
Base URL :
https://tokengate-cqt9ivzs.manus.space/v1
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7523" target="_blank">📅 16:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دو سایت عالی برای گرفتن دامنه رایگان یک‌ساله
🎁
با این دو سایت می‌تونید کاملاً رایگان دامنه بگیرید، فقط کافیه مراحل زیر رو دنبال کنید
👇
━━━━━━━━━━━━━━━━━━━━
سایت اول (ساده و سریع)
✅
🔺
دامنه‌های قابل دریافت:
de5.net
–
cc.cd
–
bot.cd
–
bbroot.com
–
ddns.ge
–
l.cd
–
ccwu.cc
📝
مراحل:
1.
وارد لینک ثبت‌نام بشید
2. یک اکانت بسازید
3. تا ۳ دامنه رایگان می‌تونید دریافت کنید
🎉
━━━━━━━━━━━━━━━━━━━━
سایت دوم (کمی زمان‌بر )
⚙️
🔺
دامنه‌های قابل دریافت:
indevs.in
–
sryze.cc
–
ryzedns.org
–
nx.kg
–
ryzn.pro
📝
مراحل به ترتیب:
1️⃣
وارد سایت بشید
و با اکانت گیت‌هاب (GitHub) لاگین کنید
⚠️
نکته مهم:
اکانت گیت‌هاب شما باید حداقل ۱ ماه از تاریخ ساختش گذشته باشه
2️⃣
بعد از ورود، یک کد QR نمایش داده میشه
اپ Google Authenticator رو باز کنید و این QR رو اسکن کنید
3️⃣
کدی که اپ بهتون میده رو داخل سایت وارد کنید
4️⃣
به این بخش برید
و روی گزینه Repo Star بزنید و برید به ریپازیتوری گیت‌هاب اونها
⭐️
بدید
5️⃣
در آخر روی گزینه Verify کلیک کنید
🎉
تبریک! حالا می‌تونید از هر ۵ دامنه، یکی رو انتخاب و دریافت کنید (در مجموع ۵ دامنه رایگان)
━━━━━━━━━━━━━━━━━━━━
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7522" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه متد تبدیل pdf به متن میخام بزارم که بتونین بدون محدودیت فایل های ۲۰۰ صفحه ای رو به راحتی به متن تبدیل کنین و استفاده کنین.
دارم کارای اداریشو انجام میدم تموم شد می‌فرستم.
میخام همه تایپیستا رو بیکار کنم
😂</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7521" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM6b_lYZOrvobp5M3PGMZE3iBvzUfCq2rIFoU2fJ8ieiZpyuxOvXJg_5II8sR1aMsAdKU18sJf6qXGI2JbjDMaQYAl7fmpevHPHrNGe-wXXfIPLXU__6PL4ARfA0bHv-zLcrCzQHi_EDZslx6d3lSxKGzL12cAPZpo5cUEDwcp91ZZ5P9_bU2JcKlsw0h7KyZdIoOAkM09xNHYfxkvTrV_RKIJR8Exq16KV-wo7UIJue9V0brgmluN8HDKHGL__fQiXpo8RmIRIlGo2qPoTMKIA685DoG48aEdJG1X9rSUQxh9MoJn6HZrHxg708HpM16_tBHLFMntoKeaBfrKnXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن رایگان هر روز تو xkiro
🔥
مدل‌های
Qwen
،
DeepSeek
و
Grok
4.6
رو بدون نیاز به کارت بانکی امتحان کن
😤
برو
x
kiro.com
،
ثبت‌نام
کن، پلن
رایگان
رو انتخاب کن و کلید
API
بساز
🔻
هم می‌تونی مستقیم از
API
استفاده کنی، هم بعد از ثبت‌نام با اکانت
تلگرامت
احراز هویت
کنی و 5
دلار
اعتبار هدیه بگیری
🎁
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7519" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF0Ewj2MbIEzvuJ6z8M-mJB_BAZAbuiFCQkjm7X-vHJbEXrPTBFOSxJYC855MfnYc6U2LGJQPIw_xhNwJRMc1NUGUlhl56rzHQ7vmYL7PRArEbewaG5Oag9YoLUltY75IUkyYanT-NkArUD3B6ylaV81EuQPqQOFzL638jo6HfRIfl8lRLJ30q-UEnWpMdetYjEFQjtySXH12PneIygylhx1P7Re8sqkz0dOODkrE19jcc8EfZIw8k0mQ54WoT08pU8g-3QUatNYaZIchI1T9Oq-BDASI_VIusQPOk56hpP73caekGzns40nWc2pFn8JZ9HlAMgD5zaG2RSodjMakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی
💥
🆓
Kimi K3 | Qwen 3.8 max |  Gemini 3.7 flash | Sonnet 5 | GPT 5.6 Terra | Deepseek V4 Pro 0813 | Deepseek V4 Flash 0713 | Gemini 3 pro image
✅
با این سایت میتونید به کلی مدل قدیمی و جدید دسترسی پیدا کنید این سایت هر روز به شما 100k کریدیت میده
✅
📌
Base URL:
https://api.anyapi.ai/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7518" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدل قدرتمند
Qwen 3.8
با ۲۷ میلیارد پارامتر الان رایگان روی پلتفرم آزمایشی هتزنر در دسترسه
☑️
اگه اکانت
هتزنر
دارید، فقط
API
رو بردارید و به هر ابزاری که با
OpenAI
سازگاره وصل کنید دیگه لازم نیست پول بدید
🆓
مستندات کامل اینجاست
➡️
experiments.hetzner.com/docs/inference
اگه کسی بلده چطور راحت‌تر اکانت بسازه یا ترفندی داره، لطفاً اینجا بگه تا همه بتونن استفاده کنن
🤝
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7517" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSmfjsgjKnOSXEt_KX6dvFa1AuDouHaeXsEywHG_kSftOyZ_CldizjHB5xIU_ZAVhMTF7rRid0Xe-t0pMEmT0GhAFB1DdCnq-FOYuEaWWIKdyUWLOYHyur77BWPGlDgjxcmGn6mZ3IEoIyLcdHT1Wp-lF18Q9qfthCIE0D5jKuvS84wZhSLZIfbTWgfP3BYi0lnIe6F9o7LtyBqQDyYocYAwQo7nF96HMp5paWLXgUKrit834uZNW54yL5nVSmDnvjOxTVugDR_LBht72vN7DqAgW6QMWkv9v_YqudFnbJxaeYoUbHkPaSuBDOXTGZhrj9JkgS-vT5JYCAebUDoEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب روی پروتکل IKEv2 رو اکثر اوپراتورا با سرعت خوب وصله
🛜
✅
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7514" target="_blank">📅 13:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5O9QoArUOYmNa-o1UMA3k_cNEJ6Wb9o88A80Qx5QkiIj9I_Kt9uetzyqQa3MO3iUd7zmjYFtCkeFjrTjz0r6dXVu8rncEpSaSS1gbGeIUM7uU4aaGKRFl1LXVcxtsTR7C6dWKfRTIbIcU_a-l9j3zo34hctQImXwC4JyD3ZIawUeFYXAs9o7t-I2RanVFnC3OKsZqIMkg9vWunxyIgvSbkLzO9veKdMJNRQUhOCwA3eX5hYpdr-OnSJqV8ZShMhat9otSZWou-Ml7W4A_iY-MiDGjUN437swUIL4aMtlCuJvBBwMTOoIUXR5NHd_3HVoO2PMTpGEwOEdmt0BA8xUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت دامنه رایگان مادام‌العمر
💥
🆓
با این سایت یک ساب دامنه روی دامنه‌ی
kdns.fr
رو به صورت دائمی و رایگان دریافت میکنید همچنين میتونید اون رو به کلودفلر اضافه کنید
✅
✨
مراحل دریافت:
1️⃣
وارد
این سایت
بشید و ثبت نام کنید
2️⃣
به بخش
My Domains
برید
3️⃣
روی Order a domain بزنید و دامنه خودتون رو بگیرید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7513" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7097199502.mp4?token=Tw9MgMWJP9cw0tv2hyDrthfsg12NrlVOpYpGNcKt6kBsBQqUPERKTbfAAtf5rWAoVJO_soLDxHCe_kJf1shwvkLXxTj815qfdfUp0ON9ZujpNb_mWhf8ku5cmauBo8ZdV6yS5GURjiFxlT6mK1jCZLXQb_RS6_yDxNWJpKpsM23LcXxJx9QHNMv64ctRZuq7XfN988bKRdEJa6Jl-hIOyGezNfy3SOnz-OzkU8F8ylSUwwKej-YHn-QTnvy3yP3WPClSl9yU4vVYfuaJiuL1mPQxLF_qak2BufJ6YX3_8s-m7FQ1P2iKXK1tgPA4-K233TlAwynBs6VZ35YaZkhNOClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7097199502.mp4?token=Tw9MgMWJP9cw0tv2hyDrthfsg12NrlVOpYpGNcKt6kBsBQqUPERKTbfAAtf5rWAoVJO_soLDxHCe_kJf1shwvkLXxTj815qfdfUp0ON9ZujpNb_mWhf8ku5cmauBo8ZdV6yS5GURjiFxlT6mK1jCZLXQb_RS6_yDxNWJpKpsM23LcXxJx9QHNMv64ctRZuq7XfN988bKRdEJa6Jl-hIOyGezNfy3SOnz-OzkU8F8ylSUwwKej-YHn-QTnvy3yP3WPClSl9yU4vVYfuaJiuL1mPQxLF_qak2BufJ6YX3_8s-m7FQ1P2iKXK1tgPA4-K233TlAwynBs6VZ35YaZkhNOClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
📱
وایب‌کدینگ حالا رو گوشیته!
ابزار HAPI اومده که به‌جای جایگزین کردن ایجنت‌های کدنویسی، همون‌هایی که روی سیستمت داری رو مستقیم از موبایل کنترل می‌کنی
🔥
سازگار با Claude Code، Codex، Cursor Agent، Grok Build، OpenCode و چندتای دیگه
✅
🎙
کنترل با دستور صوتی، بدون نیاز به تایپ
📂
دسترسی به ترمینال، چک فایل‌ها و اعمال تغییرات — همه از گوشی
💻
سشنی که روی کامپیوتر شروع کردی رو بدون قطعی و از صفر شروع کردن، رو موبایل ادامه بده
🔔
تایید هر درخواست هوش مصنوعی فقط با یه تپ، حتی وقتی پشت سیستم نیستی
🤖
حتی از تلگرام هم قابل کنترله
نکته‌ی جالب: HAPI کاملاً local-first و متن‌بازه (AGPL-3.0) — یعنی داده‌هات روی سیستم خودت می‌مونه و به سرور خارجی آپلود نمیشه.
✨
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7512" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الان سه تا مدل قوی رو می‌تونید کاملاً رایگان تست کنید
🆓
برید سایت زیر ثبت نام کنید و به راحتی از مدل های زیر استفاده کنید
✅
✔️
مدل‌ها:
•
z-ai/glm-5.3-free
• dots-studio/dots3-note-prev
• deepseek/deepseek-v4-flash-free
🧾
Link
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7511" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تلگرام برای دریافت پسوند دامنه .gram درخواست داده است
🉐
اگر این درخواست از سوی ICANN تأیید شود، بیش از یک میلیارد کاربر تلگرام می‌توانند دامنه سطح دوم اختصاصی خود را داشته باشند
💎
مثلاً
@durov
می‌تواند durov.gram و
@monk
می‌تواند monk.gram را ثبت کند
☑️
علاوه بر این، کاربران فقط با نوشتن یک
پرامپت ساده،
وب‌سایت‌های تعاملی خود را مستقیماً روی زیرساخت تلگرام راه‌اندازی خواهند کرد
🤯
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7509" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sV6UrF497FrCcEnX-YXU86kKUH319W24BRmUGy5kBU2Bg2B9WgsY5-R-tQwBrtWvw-4yXBNmEJU2_irj6UavYon59PAAWf0tJXbi3cf24oP25NU2dINK_6XeuFxXXjpCUsfrqucC0w7NqYCdU-PhI9gzg5uWMVYPksSWYp7CmhxaWbwC9oczaTMBesUZfDOo8mO3xdlJbpC3dkNAgL2XKCKEBa300-N0ezED42ypIN-WsnAfCeo04rDZZJwbhw4zpd6WYzGqDOk2OXDTSbOOzr6FV9oSoGl7oUa2Kgq2DQPQJJMEsZYGpZqPgBSUdal5uP9LVXT8N34ge6WUYYuArA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود کد ابزار قدرتمند طراحی گرفت
🎨
تیم Anthropic به عامل هوشمند خود قابلیت جدیدی برای طراحی رابط کاربری وب‌سایت‌ها و اپلیکیشن‌های موبایل داده است. کافی‌ست دستور /design را وارد کنید و تغییرات موردنظرتان را توضیح دهید.
🔥
سیستم به‌صورت خودکار کدبیس موجود را می‌خواند، خودش را با سبک طراحی فعلی تطبیق می‌دهد و پیش‌نویس‌های متعددی را در قالب طرح (artboard) تولید می‌کند که می‌توانید به‌صورت آرتیفکت به‌اشتراک بگذارید  (The Decoder) . کافی‌ست طرح موردعلاقه‌تان را انتخاب و ویرایش کنید، سپس آن را وارد فاز کدنویسی کنید.
✨
این ویژگی هم‌اکنون به‌صورت پیش‌نمایش اولیه در دسترس است  (The Decoder) ؛ برای امتحان کردنش کافی‌ست دستور claude update را اجرا کنید.
✅
🔗
لینک دیدن جزئیات
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7508" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تست کردن مدل‌های هوش مصنوعی
🚀
حتماً براتون این سوال پیش اومده که مدل هوش مصنوعی‌ای که از یک سایت دریافت می‌کنید، چقدر به مدل واقعی نزدیکه؟
🧐
آیا واقعاً همون مدلی رو که ادعا می‌شه دریافت می‌کنید، یا یک نسخه‌ی ضعیف‌تر و متفاوت؟
👀
✨
توی این پست، ۲ سایت معتبر رو بهتون معرفی می‌کنیم که باهاشون می‌تونید مدل رو تست کنید و خودتون نتیجه رو بسنجید
🔗
لینک سایت اول
🔗
لینک سایت دوم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7506" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOpkQwChelrphtFlCI-SBu4AGX1vhSmTgJTVsnT36NTFRvgckcm5oXbAKpkwICYKF8-yqXmTE1J2U_43IG3VzOnoV1m-f6B__ZUIP2XHof_CZJA5PIMgLL3sEWlGw9oakUxTxDJS_7PDObbpS3YD9w55E6aa-SgTvyplQ2_q6vPspgJthz-vPsM-1bTE3rJH5zuTGpliDnOMgHJLj77EDFL7jSp2CkOfoPC2dkw4-lHokdnyYwf1W0krGjjGTUHFh1zWcpiqkNwInuVQVBgNhMLQznW90FbBWtXxVeVDGZWPNhI9DaaBieYrSlQcg4xJWOk0jNL4t1pH4fulYnbONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL :
https://api.b.ai/v1
📌
Model ID :
deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7505" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ejQw9268x53xWxH2yA_sCmM3vjfzfNg8NDAoP0BGlQG28Ap8MSNvXpdTa1KGm204ubWME45pg6KOwv9awmcxcS_RIfIIO_GGkIkYBr47HyFJHfSS0-PV0jnS2e-UbFvTX7ANexw9HwJSgtXYXTYLeb-mq0E7zLeK3isJF7BlVT8_YIMZkeVkoR9t0Y7Yb8aYzSGtCna7wzCirfEUlpgl4Zr4FgZ8D09_GRyS2Y7YdJmrT5BYT79khdipRa2RmrbQpUu40cU5kvY_hIP9nm1jZ0qLVo4xaiD3Sg0M27cIeD_0qrpWw2ViqdfsaKQmIxfQNCyUKsDdeeEKxT2WHeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.2 الان روی OpenRouter رایگانه
💥
🆓
هوش مصنوعی GLM 5.2 یک مدل Reasoning قدرتمند برای برنامه‌نویسی، AI Agent ها و اتوماسیون پیچیده‌ست. نسخه رایگانش در اینجا با 128k Context عرضه شده و از طریق مرورگر یا API سازگار با OpenAI در دسترسه.
✅
❗️
از مدل z-ai/glm-5.2:free استفاده کنید — بدون پسوند :free نسخه پولی اجرا می‌شه.
⚠️
محدودیت اکانت رایگان حدود ۵۰ درخواست در روزه
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7504" target="_blank">📅 13:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
3 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-IXNxrDiaLV2vNxU73TC0Y4zSW1uPrXj0a24SxG8LbD4TYkfp
🔺
Base URL:
https://tabitoken.com/v1
🔺
Model ID: claude-opus-5
ری اکشن فراموش نشه
❤️
توی کامنتای پست چندتا کلید دیگه هم گذاشتم واستون
✅
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7503" target="_blank">📅 11:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEo5zOZ2eJSthy2D_mygjDYlKbSE4poc-20vHjEwX6VPebBvVm6dJpb4WaCzhRV_unF8I0FbylW4JBYjBrMP0WOiGOtXVzj5MFENlblv1ThH3cOSObI2kNSHaEYAlbYJRY3h7DaGm7UGVN5wW_unDm7jCg2g7WIXfguiSXz0mLwwKMuYRGlhcB2pse9C4eApa4Oj1TDnYH0pOK823C9Q2KJCzLbmGq_qTP3NXq1YNUWZlyTsGpb8gAyoJvnUqNuIZckh8gNViZ9yHNVdxNtuJ4k_KJq_KMl29LU3WKb-5I_Y2Z_q9yPU82GfocOQfx5Qsx_6nInJN73Jfr9rIdyLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 و Qwen 3.8 max به صورت رایگان
💥
🆓
این دو مدل در این سایت به مدت محدود به صورت کاملا رایگان و فقط از طریق API در دسترس هستن
✅
📌
Base URL :
https://api.tokenrouter.com/v1
📌
Model ID :
deepseek/deepseek-v4-pro-0813-free
|
qwen/qwen3.8-max-free
⭕️
محدودیت ایی در میزان استفاده وجود نداره اما به دلیل شلوغی بسیار زیاد سایت مدل ها کند هستن،  پس باید در تایم خلوت استفاده کرد
🔗
لینک دسترسی
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7502" target="_blank">📅 10:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190976507.mp4?token=e4xbnuY0MAZx3UVozOXb-6pSyQhot_lcOQDhCkiK3fybfOsdI5U8BFsfGiltHrgllFtpbEWAVfxYbxr9bS9v1pIEa6dprjf85CBbJqzthZIL8_AOFdFNjhYwa1FhTB9xMJfi5VSsTmwJ-rt3K5PzChoNsetj06erf35yoHUhV9NvfM30N6K3k-wdLKW3zVPnTCZbsH2w7ulR-QZKGYzFFcDb_LnpPpqW1M7Gpb3FzKE8WXZFsSpedjS6ol_vgbBy5inAzj1KQ-4XqCdMRtTd_NsFNWjdiAO5xMY-0Sff4tw2QeuYUTekRERTO6_Lj7mK9Erb221GA3DT2_Im64YxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190976507.mp4?token=e4xbnuY0MAZx3UVozOXb-6pSyQhot_lcOQDhCkiK3fybfOsdI5U8BFsfGiltHrgllFtpbEWAVfxYbxr9bS9v1pIEa6dprjf85CBbJqzthZIL8_AOFdFNjhYwa1FhTB9xMJfi5VSsTmwJ-rt3K5PzChoNsetj06erf35yoHUhV9NvfM30N6K3k-wdLKW3zVPnTCZbsH2w7ulR-QZKGYzFFcDb_LnpPpqW1M7Gpb3FzKE8WXZFsSpedjS6ol_vgbBy5inAzj1KQ-4XqCdMRtTd_NsFNWjdiAO5xMY-0Sff4tw2QeuYUTekRERTO6_Lj7mK9Erb221GA3DT2_Im64YxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎧
این اپ کنترل موزیک رو مستقیم به تسک‌بار ویندوز میاره
ما FluentFlyout رو پیدا کردیم — اپلیکیشن رایگان و متن‌بازی که پنل کنترل موزیک رو دقیقاً روی Taskbar ویندوز ۱۱ نصب می‌کنه. کاور آلبوم، Play/Pause، Seek، تعویض ترک، Repeat و Shuffle، همه یک کلیک اونورترن.
🎶
با Spotify کامل کار می‌کنه
💻
با Windows Media Player کامل کار می‌کنه
🖥
با مرورگرهای Chromium و Firefox هم کار می‌کنه (بدون Shuffle/Repeat)
🎬
با VLC هم کار می‌کنه (ممکنه Plugin لازم داشته باشه)
⌨️
با هر پلیری که از SMTC ویندوز پشتیبانی کنه سازگاره
سبک، حدود ۵۰ تا ۲۰۰ مگابایت RAM مصرف می‌کنه و عملاً مصرف CPU نداره.
✅
🔗
لینک سایت برای دسترسی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7500" target="_blank">📅 23:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn8c_8UZF6A8oj2LKn9KcfMvKI_fR7WpFVMgWwjI49WwnzKsrMp5VtfQkLw_JwAFaFgk68NYE8E_1y7_KNmTsJQiGVHKqc8WHr-NnCRWZg8YeKCXMStTP8-HGgb3zFMfwFbFxmwbEKlvFbv_zukxlQcYCUtClokvVD-KUZloFV72oxAq2V0Ly7aUVuBR8X13JPt4rFUJIeam9F_-YYIqPwf5JvhJCiZxAlAQKKL6SiH5ZmyZL--nwLmjIhsiYsizVjnEXZUwvb8nBvwFTqf2o1GYhPQ-1rZuRL70UxYuQPUDnK4QIXKLFqAAPgj62dgFdBfDxfLuSqZPWD-jCrtZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
این ابزار خط‌فرمان، یوتیوب رو مستقیم توی ترمینال میاره
ما ytsurf رو پیدا کردیم — یک CLI رایگان و متن‌باز که ویدیوهای یوتیوب رو تمیز و بدون حواس‌پرتی مستقیم توی Terminal پخش می‌کنه.
✅
👥
قابلیت تماشای مشترک با Syncplay
🎶
پخش و دانلود فقط صدا (Audio-only)
📥
دانلود ویدیو یا صوت با یک دستور
📌
انتخاب تعاملی Format و Quality هنگام پخش یا دانلود
📃
تاریخچه پخش با امکان تماشای سریع مجدد
📂
تنظیم مسیر دلخواه برای دانلودها
🔄
بررسی خودکار آپدیت برای نصب‌های Manual
📺
پشتیبانی از Subscription کانال و Feed شخصی‌سازی‌شده
⚙️
نیاز به چند Dependency داره: yt-dlp، mpv، fzf، jq، curl، ffmpeg، chafa. روی Arch (AUR)، Homebrew و NixOS هم قابل نصبه.
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7499" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=qB7CYh_NDGcLRAytC_YCEpcMcxPGn4Sr8TIe3DKOInkYaIUYxt-gpM7CIdTPe6Dykef5i0164lM3FEEcozxg12fqePC3J9QBGoruFV4E2PYdrJu9aYmWwND2nKL4QE61ALv6sJg2QpK45BsPs2_Bmassig__SlU1Vv4mDZ07tUMBKlfJxKsuZsIjo9WczxaNHvmfwS3PWpfRWKfoOUYtqv0mgdgf9Hk_7GkTnj_esjD4IFK8qhHEGp9O9fCH5fz6mY8F7kOgBjmg4qN36Lg54Dk175GjZfDUtv2rqlXWRCDYDYvnraIuTwsSFWJzJB7MU8V2fTm_azPL8pcfS7SxnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9e219aac.mp4?token=qB7CYh_NDGcLRAytC_YCEpcMcxPGn4Sr8TIe3DKOInkYaIUYxt-gpM7CIdTPe6Dykef5i0164lM3FEEcozxg12fqePC3J9QBGoruFV4E2PYdrJu9aYmWwND2nKL4QE61ALv6sJg2QpK45BsPs2_Bmassig__SlU1Vv4mDZ07tUMBKlfJxKsuZsIjo9WczxaNHvmfwS3PWpfRWKfoOUYtqv0mgdgf9Hk_7GkTnj_esjD4IFK8qhHEGp9O9fCH5fz6mY8F7kOgBjmg4qN36Lg54Dk175GjZfDUtv2rqlXWRCDYDYvnraIuTwsSFWJzJB7MU8V2fTm_azPL8pcfS7SxnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پرامپت هر ریپازیتوری رو به یک نقشه سه‌بعدی تعاملی تبدیل می‌کنه
🚀
بده به Claude تا یک شمای ایزومتریک از پروژ با Dependency ها، مسیر داده‌ها، و توضیحات کامل بگیری
💥
📐
معماری رو مثل یک شهر سه‌بعدی روی Grid می‌سازه
🏢
هر بخش از Infrastructure = یک ساختمان با شکل متفاوت
↔
مسیر Control و Data رو دقیق دنبال می‌کنه
📄
به فایل‌های واقعی Reference می‌ده
✍️
پرامپت:
Analyze [لینک ریپو] at latest main. Create an isometric system map with legend and explainer panel. Show infrastructure as varied 3D buildings on a grid, with dependencies and payloads tracing real control/data paths. Cite files.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7498" target="_blank">📅 22:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxQR0bOcduQ_lAo8SUDd1LNTP3b2eE3_r17q5iNoDxlDKRyN3k0Y0kUAKSLIGDWGDmNh82yvzuihUen2Eg2l3fv0gdhq1fVN_WJ5BsiDJ8onRlFi7aZKVscR8WAuYZuXh0KPMVrlmYIV73S3HZiIrSZ9BvpylpPm4Rg407CxCTNCAs7XvVO-gX-aHRE5cPKwTOsFt3eE5lxSvAkIOqCHI-gs8ytRr6NfDa5PKnvXvQ65bIU0EqUdRuY_qBZLdJVPCtYNfDPLyf9EZjiN5V0cjgMfcifcfp6KcbhrqeBx3AA_W2g3tm4DITZwOpr8_YMH7cPH9AV85NtlPNglYCxWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧹
این ابزار متن‌باز، ردپای AI رو از فایل‌های شما پاک می‌کنه
ما watermarks-remover رو پیدا کردیم — یک Agent Skill به‌همراه یک سرویس رایگان که Watermark و اطلاعات پنهان تولیدشده توسط مدل‌های AI رو از فایل‌های مختلف حذف می‌کنه.
✅
📄
ده‌ها فرمت رو پوشش می‌ده:
PNG، JPEG، SVG، PDF، DOCX، ODT، HTML، Markdown
🔡
کاراکترهای مخفی Unicode و ردپای متنی AI رو پاک می‌کنه
🖼
متادیتای C2PA/EXIF/XMP رو از فایل‌ها می‌زداید
⚙️
کاملاً متن‌باز و رایگان، با پشتیبانی از Claude، Gemini/SynthID، OpenAI و مدل‌های Open-Source
🔗
لینک پروژه گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7497" target="_blank">📅 19:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsPcPDJ7E7e5YC4rPBc2IoVpx0XpTNiukCsxnoOv8MfbHio2uLJgvb0_ceRbMgaKqw3l5kfQEuDIqurz3P-0_j2NDPwyQQYQO2fsqxL3SS-6ZjCHYufc8afhkd4CWj3wxRCZvTZ0WlW9UdV3Ted3AacC6UNUHdirtrrAsKKAD5zWRVE7o45x7ITeWFTRC98Xe4bt2IA3uXXi4MwIJQxJhReyAIsOx_TERgPpUw282u6rXhCR_L1g01K8rM8e6SbYXc4ZpV1WKdbqo5pI3KpNeY1fLN1o2AetfBd8j6qvnwnsGpljAt407uFo6sTmiI3TJkk0ON9LReasxxj7Tjui2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Grok 4.6 | Kimi k3 | Qwen 3.8 Max | Deepseek V4 Flash | GPT image 2 | Seedance 2.5
✅
این سایت بهتون 5 دلار به مدت 7 روز میده تا بتونید از این مدل ها استفاده کنید
💵
یکی از بزرگترین فرق های این سایت اینه که مصرف مدل ها به شدت پایینه و کریدیت خیلی کمی رو کم میکنه
✅
📌
Base URL :
https://heyroute.ai/v1
🔗
لینک ثبت‌نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7496" target="_blank">📅 17:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=IUv9sQvtFrEx_TYNqHfmaOAdb6MsfLn1CnhnoQpIN-NxeqNyQuU5iWSJtzeEnCtX2LGsZcmTgdIWOngriYB2EQoXqXcz4iTBzyfSOLhPuo3qosfErNA4uUNLNnqG9gGlBK4E4KgIhqCEVaLeuBeJTRq0ykaUAu-aR5_rYnfTX4KesIGth1eX2tRfx7IoJ2TtBrcH6hT_6EVcLVJKPubv2mI8EqUJVq7ptoVJ1tTOae2JKS0iOzDMCHSJ6E6xhYyilyrrJw3YGH4vI88uuU8Xn1yzdVbCPj4fxmy1fKfrQ7VTCo3QsA3qEyDOglhn5rQW0uueLTDaXHOAd1gXnIUgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a25507f84.mp4?token=IUv9sQvtFrEx_TYNqHfmaOAdb6MsfLn1CnhnoQpIN-NxeqNyQuU5iWSJtzeEnCtX2LGsZcmTgdIWOngriYB2EQoXqXcz4iTBzyfSOLhPuo3qosfErNA4uUNLNnqG9gGlBK4E4KgIhqCEVaLeuBeJTRq0ykaUAu-aR5_rYnfTX4KesIGth1eX2tRfx7IoJ2TtBrcH6hT_6EVcLVJKPubv2mI8EqUJVq7ptoVJ1tTOae2JKS0iOzDMCHSJ6E6xhYyilyrrJw3YGH4vI88uuU8Xn1yzdVbCPj4fxmy1fKfrQ7VTCo3QsA3qEyDOglhn5rQW0uueLTDaXHOAd1gXnIUgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرامپت، کل معماری پروژه‌ت رو نقشه‌برداری می‌کنه
🚀
پرامپت رو بده به Claude، بذار کل Repository رو بخونه، دو تا خروجی حرفه‌ای تحویل بگیر:
⚡
کل کدبیس رو تحلیل می‌کنه
🔗
ارتباط بین فایل‌ها و کامپوننت‌ها رو کشف می‌کنه
🗺
معماری رو به‌صورت دیاگرام تعاملی می‌سازه
🧭
مسیر کامل هر Flow رو ترسیم می‌کنه
💬
برای هر Component یک Tooltip توضیحی می‌سازه
📤
خروجی:
🖥
فایل HTML مستقل
دیاگرام تعاملی با Node و Connection، پنل Flow کنار صفحه، کلیک روی هر Flow → Highlight مسیر کامل، طراحی تمیز و Responsive
🧬
فایل JSON برای AI Agent ها
ساختار: { nodes, edges, flows: [{ steps }] }
مخصوص Agent هایی که باید معماری پروژه رو بفهمن
✍️
پرامپت:
Analyze my entire code repository thoroughly.
Generate TWO ready-to-use deliverables:
1. A single self-contained HTML file containing:
• An interactive architecture diagram (nodes + connections)
• A flow panel on the right
• When a flow is clicked, highlight the complete path
• Tooltips for each component
• A clean, professional, and responsive design
2. A JSON with the structure:
"{nodes, edges, flows: [{steps}]}"
The JSON should be specifically designed for AI agents to understand and navigate the project architecture.
✈️
@ArchiveTell
|
#PROMPT</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7495" target="_blank">📅 15:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWPCPc6mLccdm-b6CSTqpg3NMHJkcOWJ3Gfzd8Jvse4fl5NkC7EZEM4nKkZWRP6tt7M8L5cgkq1BwzGHCDXMGtihnkl2KPH3T5WVPXJelZR1denHutI3EnQ6WofDCAZvXL_zHrKG9vGH4YL8n6Ouqt-aS4Ir4VjGauRTMFo-9iCa15zfQkG4XPBWjHuTaN6iRXz9c8NYGWCsQe6V61meptr6l7AbwIlclmdWgip8sQzB4odkLdzNOOPvGNEJZsYwsvYGWqEys_hkgywODDx2-AvZ5ankB_dgovRz_iyPwsDqDketGNAjAKOjAC99CfIychKTn-iH_txvxidKRimjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی رو به یک ایجنت هوش مصنوعی تبدیل کنید!
🚀
دیپ‌سیک با معرفی DeepSeek Harness یک محیط جدید برای ساخت و اجرای AI Agent ها راه‌اندازی کرده؛ پروژه‌ای که خیلی سریع مورد توجه جامعه اوپن‌سورس قرار گرفته.
🔥
💡
ایده اصلی Harness چیه؟
تقریباً هر چیزی می‌تونه به‌عنوان یک Plugin وارد سیستم بشه؛ از مدل‌های هوش مصنوعی و Sessionها گرفته تا Skillها، Sandboxها، چرخه‌های اجرای Agent و حتی رابط کاربری.
⚙️
معماری Harness بر پایه‌ی Cordis طراحی شده و این امکان رو می‌ده که کامپوننت‌های مختلف حتی در زمان اجرای Agent هم تغییر کنن.
💥
چیزی که Harness رو جذاب کرده اینه که محدود به یک مدل یا ساختار خاص نیست؛ می‌تونید اجزای مختلف رو با هم ترکیب کنید و Agent موردنیازتون رو بسازید.
🧩
حتی جامعه‌ی توسعه‌دهندگان هم دست به کار شده و هزاران Skill آماده برای Harness ساخته شده که می‌تونید ازشون استفاده کنید.
📌
خلاصه اینکه DeepSeek داره یک رویکرد متفاوت برای ساخت AI Agentهای ماژولار و قابل توسعه ارائه می‌ده؛ چیزی که می‌تونه برای دنیای کدنویسی و Agentها خیلی مهم باشه.
🔗
لینک گیتهاب پروژه
🔗
لینک سایت پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7494" target="_blank">📅 13:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptTRpsafhKO8GSMtZPPPhcAnS55-Mv9E2mmyW-7acLX2yGALibMJ1kVwsx184Au-OzGYE0HHIi4pIZ2I9aoY10LKrYC4zeqI5njm6TwnNohd8PIlMzWfRnryS_xFunZiuEEYVVYe8M6ORI9YhdGiBdOo0QlYqUt7Agqh0yw6KyNxwFAaxv2gsGGVUVp8zXmpZKQshsQ9F69vfBpWQuANeEzRMBHy2_12IFv6m2iMFSm9OmedHdx8XsNy60vCuq8S1uGqI28WE8mct4MKL0yN97CMK2Zb3mtjzKOrSe1Oj3AkVMdsLxD47WwCUWXGcrelckYjJfmhHfzDfF_MtUqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست طلایی سرویس‌های رایگان برای برنامه‌نویس‌ها
🖥
سایت
free-for.dev
یه لیست
کامل و مرتب
از سرویس‌های
ابری
و
ابزارهایی‌ست
که پلن
رایگان
واقعی دارن (
نه فقط تریال چندروزه
)
🆓
از
دامنه
و
هاست رایگان
گرفته تا
دیتابیس
،
CI/CD
،
مانیتورینگ
،
ایمیل
،
ذخیره‌سازی
و
خیلی چیزای
دیگه
🔸
اگه دنبال
ابزار رایگان
برای
پروژه شخصی
یا
استارتاپت
می‌گردی، حتماً یه سر بهش بزن
💻
⭐️
Link
⭐️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7493" target="_blank">📅 12:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09dd417185.mp4?token=EsdSxO6KEEw4cildeCsuqjxi5MddLqC8zqIRP4UBQc0zDl0DMvkTosQ02hHuLL8eM0z59z2l-xQzOzdgG2E9UbQjbAkSUuX4c_5_4TGSiK32W3UqU8LsbYpxr3V07kG_v9FhidS2T9yzUK-bt4pva3gsLCWiJHkWq0imtErByqNDyjMEqOdDaHWyYKRONQuWPkGY-WHNhrBiae6UOrpOC7Nbg6SAERd8_ngbt0cIDQMPGbHVNGm7dqV64Z9OMlj2YHrBq98fOokFof4qN7sNjGBmhORcym_dQfaj-RqLOuoo9uT5chvQ1dS2hFhHTPUU7Np6Dh7HU2V4K5zawZAdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09dd417185.mp4?token=EsdSxO6KEEw4cildeCsuqjxi5MddLqC8zqIRP4UBQc0zDl0DMvkTosQ02hHuLL8eM0z59z2l-xQzOzdgG2E9UbQjbAkSUuX4c_5_4TGSiK32W3UqU8LsbYpxr3V07kG_v9FhidS2T9yzUK-bt4pva3gsLCWiJHkWq0imtErByqNDyjMEqOdDaHWyYKRONQuWPkGY-WHNhrBiae6UOrpOC7Nbg6SAERd8_ngbt0cIDQMPGbHVNGm7dqV64Z9OMlj2YHrBq98fOokFof4qN7sNjGBmhORcym_dQfaj-RqLOuoo9uT5chvQ1dS2hFhHTPUU7Np6Dh7HU2V4K5zawZAdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
♊️
گوگل هر ریپازیتوری رو به مستندات تعاملی تبدیل می‌کنه
گوگل ابزار جدیدی به نام CodeWiki معرفی کرده که با بررسی خودکار کدبیس، در چند دقیقه یک مستندات کامل و قابل‌فهم از پروژه می‌سازه.
🚀
🔺
ساخت خودکار دیاگرام و نقشه پروژه
🔺
توضیح بخش‌های مختلف کد و نحوه عملکردشون
🔺
تولید راهنما و آموزش مرحله‌به‌مرحله
🔺
تحلیل معماری و ارتباط بین وابستگی‌ها
🔺
ساخت یک چت‌بات آشنا با کل ریپازیتوری برای پاسخ به سوالات مربوط به کد
یعنی به‌جای ساعت‌ها گشتن بین فایل‌ها و کدها، می‌تونی پروژه رو خیلی سریع‌تر درک کنی.
👀
📌
این ابزار رو از دست نده!
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7492" target="_blank">📅 12:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by--KKYzrMtxcq0IlvJhcpTaYy8LvBVs9SuRniJoJ-o_R-OaNngOIre09XxsvbOl9N3lguvkU7FX7J96X90j7kVTlb4Z8z7Rvl0eMsh31yT8h2ZiuthNOQmp-AcluENvSelhbU4qS7j_kZdln2Dzw9cU4DGP2JDvtFYWCIYaza5hZKd77oLcL2pZY-nciYI0tpmgRgulC75jeMRgcDb4nu6LNYmqnrYaBhrFU-Y4-SW3DaXZrC57mxCljHgHbL1WyhG4WSNRrV-IgxbtSaYWrMlc3RNZaoDp8vbsNvrFuz6ypERnMAyjCI5xCYJt0XXnWJcDkgm3Bph-P0nwKE6bmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TorrentSearch
♻️
اپلیکیشن متن‌باز اندروید برای جستجوی همزمان تورنت از چندین منبع
📱
با
TorrentSearch
می‌تونی
خیلی سریع
از کلی
سایت
و
پرووایدر
مختلف جستجو کنی، نتایج رو فیلتر و مرتب کنی و مستقیم مگنت لینک یا فایل تورنت رو بگیری
⏬
امکانات اصلی
💭
جستجوی همزمان از چندین
پرووایدر
(قابل روشن/خاموش کردن جداگانه)
🎁
فیلتر بر اساس
دسته‌بندی
(فیلم، سریال، انیمه، بازی، کتاب و ...)
📁
نمایش تدریجی
نتایج
+
مرتب‌سازی
بر اساس سیدر، سایز، تاریخ و ...
🪣
جزئیات کامل هر
تورنت
+ صفحه جزئیات داخل خود
اپ
ℹ️
ذخیره
بوک‌مارک
+ خروجی/ورودی گرفتن
🔖
حالت
Safe Mode
برای مخفی کردن محتوای
NSFW
🔞
پشتیبانی از
Jackett
/
Prowlarr
(
Torznab
)
🦾
طراحی مدرن
Material 3
و
دارک مود
🎨
⬇️
دانلود از گیت‌هاب یا F-Droid / IzzyOnDroid
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7491" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡
پرامپت‌نویسی تغییر کرده؛ این ترفندهای قدیمی رو دور بریزید
بزرگ‌ترین دلیل جواب‌های پرت و توهمات هوش مصنوعی فقط یک چیزه:
وقتی جزئیات بهش ندید، جاهای خالی رو با حدس و گمان پر می‌کنه.
❌
ترفندهایی که دیگه منسوخ شدن:
•
نقش‌دادن‌های کلیشه‌ای:
نوشتن جملاتی مثل «تو یک متخصص ارشد با ۲۰ سال سابقه‌ای...» تاثیری در دقت نداره. مدل به فکت و داده نیاز داره، نه عنوان شغلی تخیلی.
•
تکیه به
Temperature = 0
:
صفر کردن دما جلوی اشتباه رو نمی‌گیره؛ فقط باعث می‌شه مدل خطایش رو با لحنی کاملاً جدی و بدون تغییر تکرار کنه.
•
پرامپت‌های ۳ صفحه‌ای برای تسک‌های عادی:
طومار نوشتن برای کارهای ساده، تمرکز مدل رو به‌هم می‌ریزه و احتمال نادیده گرفتن دستور اصلی رو بالا می‌بره.
✅
فرمول ۴ مرحله‌ای برای گرفتن بهترین خروجی:
۱. هدف دقیق (نه کلی‌گویی)
❌
نگو:
«این قرارداد رو بررسی کن.»
✅
بگو:
«این پیش‌نویس رو بخون و فقط بندهایی که بار مالی اضافه برای خریدار ایجاد می‌کنن رو پیدا کن.»
۲. بافتار و مخاطب (Context)
«مخاطب فردی بدون دانش حقوقیه؛ توضیحات رو کاملاً روان، ساده و بدون اصطلاحات پیچیده بنویس.»
۳. بستن راه حدس و توهم (خیلی مهم)
«اگر پاسخ یا عددی توی متن نیست، به هیچ وجه حدس نزن و صراحتاً بنویس: "اطلاعات در متن موجود نیست".»
۴. قالب مشخص برای خروجی
«پاسخ نهایی رو فقط در قالب یک جدول ۳ ستونه بده: [شماره بند | ریسک موجود | متن پیشنهادی جایگزین].»
💡
اصل ماجرا:
هوش مصنوعی ذهن‌خوان نیست. هرچقدر دامنه حدس‌زدن مدل رو محدودتر کنید، خروجی دقیق‌تر و کاربردی‌تری تحویل می‌گیرید.
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7490" target="_blank">📅 21:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWPJlIF91FA2lZ-HAeQGOORe5I1c4IJZQMEZhFxGSKVA9TGdZlcqZJF6cVSiDUf0on1NggCx7waVZddvFXlj3c99ECUy_s_gnOSo-_sweerbsXDsRqiF2OLm9LHIh-SJ9qLcmUGx95vKznhy_Jhapnuq8jv_eIVpMPfM31SxKEJLKR0aTnEk2UF1sOfD1T6ljtlNWeB4dnYpPtKVh0bUdNE-DyRrNY6XmapZyAelb13BcdYWZ9mhYhV28BylOMX8ZgV7WppyNOXlYqO57bzfwzySZpyy1wO7EqwdvjneD-bWByh764yWXv6Cp26LFYLoEeUUQ4JJlb4WlS6RPbcQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به برترین مدل های هوش منصوعی به صورت کاملا رایگان
💥
🆓
Sonnet 5 | GPT 5.6 Terra | Agnes 2.5 | Mimo 2.5 | Gpt image 2 | Nano banana 2
✅
📌
Base URL :
https://ai.furry.vg/v1
حتما در بخش انتخاب گروه ، گروه Free رو انتخاب کنید
‼️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7488" target="_blank">📅 19:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syFVLyosItZwy3ZSbKT654girK7k_8H_ZIIa4PllAs1_UZygphgFqLUl1EdXFJgYRn_q84fGMGBZiPEaZPd2ikVI-xvkT0UrH-ijREqPZdgVRPouf7S3G3kyEXnEzm2mZXMfR1XXnIFF9EyKcOBrkHvscdkGIwktZVmGW1VuhBuOBx0DwjrpN1zAHqAqDEiE1Qgx0cF4ExRkNWnUp-OfeU6UDitIpptnIKbrnXpzyhYGIsSu2q4FvOMHUQMGEHe6jsvOY9XprfF-UhR0mgukr2PMHL_NR9vpojmvVLCm02DvPBWqGuPZHC5m_B0t1cPBqcfJwSmxi5uHeNmDmSXDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل Qwen 3.8
💥
🆓
با سایت Runinfra تا 48 ساعت آینده میتونید به API مدل Qwen 3.8 دسترسی رایگان داشته باشید
✅
📌
Base URL :
https://api.runinfra.ai/v1
📌
Model ID :
qwen3-8-27b
به دلیل شلوغی سایت ممکن است پاسخ مدل کند باشد
‼️
🔗
لینک دریافت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7487" target="_blank">📅 17:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahbZGP3iVw9Exzlpqa1fpQFhniO94fAFY2q-q4CMNxAqmhCg1XfsOUXq2bnTTCnk06SCIGdVrGXBHtC1IuI33ODWksbKTXNaWkV39PczGP_2eWtiYRqh73I62QK05eCH-J6BZt50t3g4i3AEmPjcGCpQV60h1XZ6JWF8eK2Sy7VdKCvs2DlRqDpOrCxtwynmhPkBGwa-w64J-jqgIInocbo92nIKNyPM2g3zpMZJOpVI3DndBR-IwMWjLQ1CgMh4mYTYKy9Wmp1eT0X694Ck_mW2AvIBD4GQdbB3eraeWic342avipoh0QKP7HUhqpbaAnULgm0kDnQX43FMX_2Z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی محبوب
💥
🆓
Qwen 3.8 max | Deepseek V4 Flash | Deepseek V4 Pro
✅
📌
Base URL :
https://api.orcarouter.ai/v1
🔗
لینک ثبت نام
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7485" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mErHFm0eXUDFRJsCaPLej7gbGSN4QjuVjsI8DW-ynaRNHsiqW-OORezwraCfjjmsOgtStqC_Id_8Ygcsasp3S8cp7HAWj82ZcByMhwI-A-TKGL_R6ZxcMMxazAAYFlTGDxQpVBXG4HUCqdTn04i403C4AakOpgBUtou-snDlnkWq_fj5VcuSealSw631tmdiuGk5pGNZSzPdMUJUQ_08NZjr427sKmAcawiR1bhZOAgohWxoGmL1WLjD4LkKS8ogOrgBEiv4uXxEpcoxEYpOHhH_wBTaLn59UAeY1TPbnlG3LdVaDtkEyYkNKTMEn4wdK_xFUypdGWS5QYfng15Tgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت
z.ai
بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7484" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هدیه ویژه برای شما
🎁
100 هزار دلار کریدیت رایگان در این کلید قرار داره ، شما میتونید همین الان کلید رو در هرجایی دوست دارید استفاده کنید
💵
🆓
🔺
Api keys:
sk-bY9B0parF18s5v1wasRyzRZsVLzICaSVfZNVEMrqG2Rlt7dH
🔺
Base URL:
https://ai.venlacy.com/v1
🔺
Model ID:
glm-5.2
به دلیل شلوغی ممکن است پاسخ ها کمی کند باشه
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7483" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYeCQjQqcN85wKKw61UGRtOY02HP0-L8UkqUE50pbMzPAp8QG3zS2FBcLF6PmmzccpG3_UOKrnjwxmPPLMKnLB0SiIvT6S_cpCmOwRJfPp0OWDAnme0Bw9n1H83oftyQcBfhV0ynfiUPgm_Y90yVY-lQjXiZ7AMHU9wl6VFtU7KbmatAEYii5CN0kZ7Gaq-wQrEC81JzGFmjIP_Lv9uFVuUNfliMi_Yy9-fB6LouXgQzkdWLtPeNjjOGewpSHX5LjpYAWW2G74KmPqABagC6Qnx_qokZFSrw5xbc8A58bdAyLkfTMcd2LC9_Ro77IjPDcILg-mNuvmEigLL7Hw9SwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 رونمایی شد
🚀
نسخه جدید GLM با نتایج بسیار قدرتمند در بنچمارک‌ها عرضه شده و در چندین بخش از رقبا جلو زده است.
🔥
در مقایسه با مدل‌هایی مثل Kimi K3، DeepSeek V4 Pro، Qwen 3.8 Max، Opus 4.8 و GPT-5.6 Sol، GLM-5.3 در بخش‌های زیادی عملکرد بسیار رقابتی و حتی برتری دارد.
⚡️
🔗
دیدن اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/ArchiveTell/7482" target="_blank">📅 23:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfrnF5f-tNgiAFqMkx3S5ZWxyCpe2eRJ2SCASWjFfWi7dr29RMYYMu1JrSIsMPLduKV5DP_FIvUwbv7Jwwhm3EsHvHYbEydGwVY6K2A24UMBGxwCj-fOtSY0wlaTltkRKudm_ZzMzXyzg1jaKlCnBu2IASiMhasMpiKRWVWkg4-czbiAUNUyZJrJCVbdC2JXhC4lZ15CSzwp45yyiD6qsXuCWgyqi02swPrjEEjagVEQspXaioM4oWfux7GR25crr8xNzVfzP_pL3al8ZbJPmjaGXXneLEhBP2H8nmZgqZzOCEv2WjPGuJDdXh84WEbIdnWp322MxoMsafYEPLmfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفاده رایگان از جدیدترین مدل کدنویسی متـا: Muse-spark-1.2
💥
🆓
طبق بنچمارک‌ها، عملکرد این مدل دست‌کم از Grok 4.5 (High) و GLM 5.2 (Max) چیزی کم نداره و بازدهی فوق‌العاده‌ای توی کدنویسی ثبت کرده!
💯
⏰
زمان‌بندی استفاده رایگان: امروز از ساعت 12:30 تا 20:30 به…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/ArchiveTell/7481" target="_blank">📅 15:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7480" target="_blank">📅 14:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2VPqA8LRHhK39Sl68OFLEuWBYhfTnWB9W0RyzgDq2Wu0e59xd8jVfkkmt8LReSoB1Wj9BbcuNSnx0UMD3qBeRTcKhysvbLADO2WtTrOaJiyq-bGHiKOKqa7NoGEaBybfKc7rnc0cwkmpFFadcdPxnu8aQtW0fKiQsmJAjgOHtlMWE2NhNsSTlTXGYwwSJrvZVkcJOrhwnaRHPAanJzAZIJzaUXOcXfS27zMpZRJ97Uj2HOsVAGbF0ek3_uXhKq3pELPR5Fx05riVoDoraJDMYaWSotcrxEAcMLUlrrJdezAXcNOKzEWrhJzioJmzCgqm1YYTYTIe3rBnubwJksaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ تست رایگان مدل ‌Seedance 2.5
⁩
💥
🆓
‏اگر دوست داری ویدیوهای سینماییِ ۱۰ ثانیه‌ای با کیفیت ‌480p⁩ بسازی، پلتفرم ‌JXP⁩ این امکان رو به صورت یک‌بار مصرف برای هر حساب کاربری گذاشته.
🎬
✨
‏مراحل ساخت:
‏‌
1️⃣
وارد سایت
jxp.com
شو و ثبت‌نام کن.
‏‌
2️⃣
به این
بخش
برو
.
‏‌
3️⃣
متن یا تصویر دلخواهت رو وارد کن.
‏‌
4️⃣
دکمهٔ Generate Video رو بزن.
‏برای این تست اصلاً نیازی به کارت بانکی نداری و کاملاً رایگانه.
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/ArchiveTell/7479" target="_blank">📅 13:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پرامپت تولید شعر بی نقص پارسی!
از پرامپت زیر استفاده کنین تا ai براتون شعر هایی در حد شعر های حافظ و سعدی بسرایه:
تو یک استاد مسلّم عروض و ادبیات فارسی هستی. در سرودن شعر، اولویت مطلق با صحتِ
دقیق وزن عروضی است. پیش از نوشتن هر بیت، آن را در ذهن تقطیع کن تا مطمئن شوی
واژه‌ها (حتی کلمات غیرفارسی) دقیقاً و ریاضی‌وار در جایگاه درستِ وزنی
نشسته‌اند. خروجی نهایی نباید حتی یک مورد سکته، لکنت یا ایراد وزنی داشته باشد و
باید کاملاً روان و موسیقایی باشد. حالا یک شعر شاهکار کوتاه و روان درباره مناظره یک قناری و دایناسور بنویس
.
﻿
تست کنین، به همراه مدل ai استفاده شده شعرهاتونو کامنت کنین، بهترین شعرو که لایک بیشتری بگیره بش جایزه میدیم
🎉
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7478" target="_blank">📅 22:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Gemini 3.7 is out now
😍
از اینجا میتونین رایگان تست کنین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7477" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chrRRMowxNZqj2et52mQtnOM1o1W7moFl5LWQu71g1ZlnFdxgbAd1KFg8e3RzLDNoDoQYchFMouuzywGD4Re0IIv1eFSvo44wxJPu07CioBd9PTYty6CjNgLMU6QDCOrcisu2Uc1bNRX81e-QBlJb30J8EPMyfl0V1_ZuIvNrlwq5SHpCMPbFNw0_Fk80XckPUI6GffkMy1zbBq8TX3FD6rHJswCGm-AGqu28_i5sefAMURf87ELGv_l1OXZLGKkiMl2eJgK4xcrDL_MxtxygvZUHE6t0uxJYDG3IXNGs6Ol0V69eHK5lIJujChZKfwp5l2EBviBRWyxC5UCdSSD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
CiteSeerX گنج رایگان مقاله‌ها
یک موتور جست‌وجوی تخصصی برای مقالات کامپیوتر و علوم اطلاعات که فقط به جست‌وجو محدود نمی‌شه.
👀
🔺
میلیون‌ها مقاله + جست‌وجوی متن کامل
🔺
پیدا کردن منابع و مقالات مرتبط از طریق شبکه استنادها
🔺
اطلاعات نویسندگان و تحلیل تأثیرگذاری
🔺
کاملاً رایگان، بدون ثبت‌نام و با دانلود مستقیم PDF
🎯
برای پیدا کردن سریع منابع علمی خیلی کاربردیه.
🔗
ورود به CiteSeerX
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/ArchiveTell/7476" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">20 دلار برای دسترسی به مدل‌های هوش مصنوعی GPT مانند
:
💥
🆓
GPT 5.6 Sol | GPT 5.6 Luna | GPT image 2
✅
وارد سایت شده و ثبت نام کنید سپس یک کادر میاد برای جوین شدن در چنل و غیره ، کافیه فقط روی دکمه ها کلیک کنید و پس از ورود به صفحه بک بزنید صفحه قبل ، سپس روی Claim کلیک کن
✅
Base url:
https://apimaster.ai/v1
قابل استفاده در
Vega Agent
✅
🔗
لینک ثبت‌نام در سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7475" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">120 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
✅
برای فعال‌سازی فقط کافیه یک اکانت گیتهاب داشته باشید و از طریق این لینک وارد شید
✅
Base url: https://tabitoken.com/v1  قابل استفاده در Vega Agent
✅
🎁
با هر رفرال شما 20 دلار و…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7474" target="_blank">📅 17:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtUzMggZY96Zwytx88NQ1tzzXJtOdc3iP_A0LW0F4NHEsStzqpD3ZHH0RpInqH_Ch4r8NcYeJukgILJJhxEAV06jLuKlmIO7zEQaACwB8FhNcwvNdUmaEeHrmib78uriO_gESk_UZqoTqvdEvz8uqo53IOvwUExaoomdYysLAexOxGckS0UgcOvOqi9xkrllreaXqKwYHoYGEjvyE0YYFFKb0LKOL29jVqm4ECDbaTte_foYvOxsYVUSoyM67YsBu8kpy_0t3pA6NI41oCO73Xz6U-OmyasRaRVuRUDakaq7eTU243XgoVlc752WnPvc4OsUDrjPxlM7gAgxI57tHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4 Pro 0813 وارد رقابت شد
💥
مدل جدید DeepSeek با قدرتی در سطح Kimi K3، GLM 5.2، GPT 5.6 Sol و Fable 5 معرفی شد.
🚀
🔺
سه سطح Thinking: کم، زیاد و حداکثری
🔺
عملکرد بهتر در تحلیل و برنامه‌نویسی
🔺
اجرای خودکار وظایف و ساخت گزارش
🔺
پشتیبانی Native از OpenAI Responses API
🔺
اتصال یک‌کلیکی به Codex
🔗
تستش کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7473" target="_blank">📅 17:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnVchaUEFxHCzehnZ92wYMkZwr11wwD_6Y6dz0894jykXJfFJrE7_8U6B-XGuYtFtxO3b70gKz5qn_9EnILyH9ON5_9iJkMRr_IQFkEI_K3Uev3pMWNn4NZ2TqhR4KHNVxp4mXRAAwO_o8FaHi8n3cFVE8QhAUxR-7aZpHIXjZpj7G2TV-k9F29wFukuqwMVGvigR7nsIA5WVQnjqXjzXIQKLzK7NcizcZwnr_kDrCjqb_RlM1MIEh6P0QeLy5O3a2nRY-9Sg8xPt6cYGFj1_GdPBCl6G4J6CsMt1Z-u0Hi4OZRhJS8JjYfHOi4KTB2TsFdeNZGXQfGXlyoWLAwd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های هوش مصنوعی محبوب
💥
🆓
با این سایت
روزانه
300 کریدیت رایگان دریافت کنید و از مدل های هوش منصوعی زیر برای کدنویسی بهرمند بشید
✅
Sonnet 5 | GPT 5.6 Terra | GPT 5.6 Luna |Gemini 3.6 flash | Gemini 3.1 pro | Haiku 4.5
✅
🔗
لینک ثبت‌نام
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/ArchiveTell/7472" target="_blank">📅 15:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGXNiVG1-uwAZuMGEZGvqAPAqF1K3gNhKMU_ZuhCTofTxvnnwEe_EpLz-PfaMFgSyXIHM_kasLQyG_IsCJWU5_gEZEja7rACxfCL1hy4guXKBeVHgqgE0uSEuXoVvtgtR2TIW9RBaM2zX64QdU5fVjLDXSoFc5rvceSzudP8ndtqs5ctATUDW9ehoAX7uQ73wRUI4JYEUK-PRcLk3zRnB2qvRViFAPZsfy8VPGcYhAsGtSbAaKxmdq20cVqfeK4-a1496mm8ZD4PMRrL7M17Gtb4_lJivJlWq0_kvCdjDxvaH7Wzp9MXFM4iMMtVUQPpyETwqqZrUhANRCfu2cfi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کریپتو‌مارک مخفی Claude حذف شد!
🥸
هوش مصنوعی Claude روی متن‌های تولیدی خودش یک نشان نامرئی می‌ذاره؛ چیزی که با چشم دیده نمی‌شه، اما در الگوی انتخاب کلمات پنهانه و می‌تونه برای تشخیص متن Claude استفاده بشه.
🧑‍💻
حالا چند کدنویس ابزاری ساختن که این الگوهای مخفی رو در متن تغییر می‌ده.
📥
فقط متن رو وارد می‌کنی و نسخه‌ی جدیدش رو تحویل می‌گیری.
🔗
استفاده از ابزار
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7471" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSB07mu4134b80N2WbgmxbnJFgOq1Mb1DstlcwtCRp4AP_2KXVCl-HEnmyel-3igzxl_P_N_bWL5TqaCFosoMQ-BHEwvDNIA_ZoA60KjwY9_nlSzsYwK2Uy3qaw9TZU5lggG6k0UJNDIuQ3umf1NTbfyasXLmlv5t5pS8nuvJzg42GT6h426rLF47wVO03f5rCqVb9lfhhwkfcc-b06NBUehmBx67nsbB0BvvhnNdPGErZC1lel9l9O72SQ0Pt3Lf1BtNcEiVdHzkRYGL28JvxX3Q0cWvRdyGmcruBNnUK2M0cG6TB-86rL4qONNek3jyNwKWHp6g7MSdoLcNZi0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد  قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود ۱.۵ تریلیون پارامتر داره و قراره در آموزش SFT و RL پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:  چند هفته بعد، Grok 4.7 با حدود ۲.۱ تریلیون…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7470" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://t.me/ArchiveTell/7053</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7469" target="_blank">📅 17:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STYvdYXjX3lxgVtZmKNmUJY_0lkZUbEYdxl6lX5xvJSPob0-52qOZBpFv_K7O4cJxrcOj8ZFBJd3hyDV-vS2I9m8DsX-N6AdL87N2a79v44BUD1DhyCBZry2Xw8gIk1S5IczXx6nz8C3NjypUH-ab5Mz8rgE1PvKwnzoZZuSFX716lWJPIbvRJvM9pE46NcRULQKSB3JjA4JGNhgq2ivlXCmtVujl8q4ubmWjgAogHXcTTujaUh3gm2ZZKioerb6nJinSsGTcNWRWvLdk-MgymTFpnNRyafZhRx713dSh1GflssReScREt_DQAopQ1iVnN90PWIs7MptcC218G3j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
Grok 4.6 همین هفته میاد
قرار بود ۷ آگوست منتشر بشه، اما انتشارش عقب افتاد
😅
🧠
طبق گفته ایلان ماسک، Grok 4.6 حدود
۱.۵ تریلیون پارامتر
داره و قراره در آموزش
SFT و RL
پیشرفت چشمگیری داشته باشه.
🔥
اما بخش جذاب‌تر:
چند هفته بعد،
Grok 4.7
با حدود
۲.۱ تریلیون پارامتر
میاد؛ قوی‌تر و بهینه‌تر، ولی کمی کندتر.
✨
👀
باید دید xAI این بار چه چیزی رو رو می‌کنه!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ArchiveTell/7467" target="_blank">📅 15:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎙
LivDub | ترجمه و دوبله زنده با هوش مصنوعی
با
LivDub
می‌تونی ویدیوهای خارجی رو
هم‌زمان ترجمه و دوبله
کنی؛ بدون اینکه مدام به زیرنویس نگاه کنی
🤯
✨
قابلیت‌ها:
🔺
ترجمه و دوبله لحظه‌ای ویدیوها
🔺
استفاده از
Gemini Live
برای ترجمه صوتی
🔺
پشتیبانی از
۷۸+ زبان
🔺
مناسب یوتیوب، دوره‌ها، مصاحبه و لایو
🔺
پشتیبانی از مرورگرهای Chromium روی اندروید
⚙️
روش استفاده:
مرورگر سازگار رو نصب کن → افزونه LivDub رو نصب کن → Gemini API Key رو وارد کن → ویدیوی خارجی رو پخش کن
🎧
🖥
مرورگرهای پیشنهادی اندروید:
Cromite • Helium • Ultimatum • Quetta • Yandex
🔗
افزونه کروم
🔗
سایت LivDub
🔗
گرفتن کلید جمنای
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7465" target="_blank">📅 13:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUHYsfIyUrUb5iX3C8OlghNdGqoi-FQGChqmhtAb3NzSAvL0sGDwJDDfkIpuoOQdFyBAe8wfFRDwgMiaWPpGcxtCFl9wc-s2738q9yAjCpEnsHN2OzP3ilVTNfcVGdeoIs2Wj8b3bm2UnKfXJs2QgmlG2CV56vqtQWQ4-BZrQWrEAoo51Cw7oZVX_oKeYeHidCaE8Oea1gNf-UZgXIIBbpQqu1e_Ok6g9kFyvLkfA4Bs_D0saX34pxA3OJibozxZJDIU-Yqnb-vcQYdZzhsjhyCMk-P6iJUWgSskrM2sDSdKEDYogytnxBwuo7dwxUy7Kc3PDEWudcyU-GecGMT8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
FLUX 3 Video رایگان شد
؛Black Forest Labs برای مدت محدود، FLUX 3 Video رو توی Playground خودش رایگان کرده
🔥
⏰
فرصت استفاده رایگان تا دوشنبه ۱۷ آگوست، ساعت 10:30 به وقت تهران
قراره در ادامه قابلیت‌هایی مثل 4K، ادیت ویدیو و استفاده از تصویر/ویدیو به‌عنوان رفرنس هم اضافه بشه.
⚡️
✨
🔗
لینک استفاده
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7464" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آیپی تمیز
✨
188.212.97.3
94.182.177.92
185.50.39.15
103.25.85.84
176.120.17.44
45.146.240.17
45.146.240.70
77.237.246.20
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7463" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJZC2Zn1KT6pCC7BbOE_mdVLpC-J7Z9c38kODvUdXx4hvkpPwJ-rDD2OkCsdGl5pUzDEdZXd2l9WX2HQ9HHMfOJI1ZquI_TCczgFUj4V-ZCxMLCjp_aqrAhF60V0Q2vlnm5SsWxkaC-OHyNPhJsGpf_Mmwy4_KmKVgzFNGs5ZAYVDJ2qFwjImVJ8J5ub65y2XAev5tbVFlUumXK_MwUQ1rB1Ye1t6KueGWJFuZHywX8RBw_LY5KfTE9Xz7s8vKrpoC-wahZ23w5wBfPjhagFv7FGFdf7d7kSVdqSfFclJ28QvuBNWKp5TU688E2M0m0lHE7-zqICaeH3HDXlFH5-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از 1000 پرامپت کاربردی برای هوش مصنوعی!
🚀
یه سایت که مجموعه‌ای از بهترین پرامپت‌ها رو یکجا جمع کرده؛ از درس و برنامه‌نویسی گرفته تا طراحی و Excel
⚡️
✨
یه جور جعبه‌ابزار کامل برای کار با هوش مصنوعی
🧰
🔥
🔗
لینک سایت
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/ArchiveTell/7460" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK5SAubNCnIt7YIAq368rNovTXnng8keuYU5ldNeDEkJ3-UQYOyMmat-_VaiiaJWVnhzsBV-r9Vgv-g583xntgfAg9HqCSDzrSv9_LgSFJtUrJ_PO0aeYKRif_Yafam7dUzS1orqV4sB8GPdiftU4GjK5RFI4sZykXxXo_qthDjdL16sL565TikomXZBUTrVN1RCpjyzOX4rbOVz-ahVKcshWeeiKv5yygN3Tvvq2j69nijUBoHr_AwreNlcFK4AGjr31UxsbghaGLt3a0vL7K-6IG29CVL0iX2pUiXVNeIrJRu6j504-r9ue07sRIrE8rkxXoSPG9A7XNBF2gxxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤔
گوگل قید Gemini 3.5 Pro رو زد؟
گزارش‌ها می‌گن گوگل عرضه‌ی
Gemini 3.5 Pro
رو متوقف کرده تا مستقیماً روی
Gemini 4.0
تمرکز کنه.
🚀
گفته می‌شه مشکلات عملکردی و سخت‌گیری‌های امنیتی در مرحله‌ی تست، دلیل این تصمیم بوده.
🛡
حالا رقابت جدی‌تر می‌شه؛
Gemini 4.0
می‌تونه از ChatGPT و Claude جلو بزنه؟
🤔
🔥
✈️
@ArchiveTell
| VeGaS</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/ArchiveTell/7459" target="_blank">📅 13:01 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
