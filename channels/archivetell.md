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
<img src="https://cdn4.telesco.pe/file/nJTTFCN8ckXNykJo565mzrvWbKe712LHN2oR8yg5llFQgVH8cYYx2kKg4Sue28rMKIPVQ-VVxx8KqY4tMpZ1hOpcq_oQBR9Rwfr6SHF-uiOVHxIOw00xyVDOsU13AtVYl-4bq1ZkrMAn80TXWFCzS3feSbmWk9W_zEBLOWiknrgQ_16NnLP7bQloOxfaiNl8iwifZzZ702Al_H4UjG-UzMRoamdwMAc9yHOv8On-jAphs_8G4JzSXHNpvwJrvVTXiAWRbgRJCVKhQEX-hWtQCzw7lQ8YJNOkP4evTcPJR1gfylwfqhGujD2i0LLaEDNN1yZG81clzeFYWiWBFO-DRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.76K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 22:11:35</div>
<hr>

<div class="tg-post" id="msg-5803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کلود اوپوس ۴.۷ فوق‌العاده قدرتمند هم همین حالا روی این پلتفرم در دسترس است
😁
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/archivetell/5803" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">می‌خواهید اپلیکیشن خودتان را بسازید اما ذره‌ای از کدنویسی نمی‌دانید؟ بودجه‌ی زیادی برای استخدام یک تیم توسعه‌دهنده ندارید؟ همین الان باید این وب‌سایت فوق‌العاده را ببینید.
Anything.com
یک سازنده‌ی اپلیکیشن هوش مصنوعی سطح بالا است که به شما امکان می‌دهد ایده‌هایتان را فقط با چت کردن به زبان انگلیسی ساده به نرم‌افزاری کاملاً کاربردی تبدیل کنید. به معنای واقعی کلمه لازم نیست حتی یک خط کد بنویسید!
این چیزی است که این هوش مصنوعی را کاملاً شگفت‌انگیز می‌کند:
• ساخت برای هر دستگاهی: وب‌سایت‌ها، اپلیکیشن‌های اندروید یا iOS خیره‌کننده‌ای ایجاد کنید و آنها را مستقیماً با یک کلیک در اپ استور منتشر کنید.
• همه چیز داخلی: به طور خودکار موارد پیچیده را برای شما مدیریت می‌کند. احراز هویت کاربر (گوگل، ایمیل)، پایگاه‌های داده‌ی کامل و حتی ادغام پرداخت Stripe فوراً راه‌اندازی می‌شوند!
• اشکالات خودش را برطرف می‌کند: با خطا مواجه می‌شوید؟ هر هوش مصنوعی به طور خودکار اشکالات را تشخیص می‌دهد و کد را به تنهایی برطرف می‌کند تا اپلیکیشن شما روان اجرا شود.
• طراحی انسانی سطح حرفه‌ای: ظاهر هوش مصنوعی ارزان و عمومی را به شما نمی‌دهد. این برنامه طرح‌های رابط کاربری زیبا و در سطح انسانی ایجاد می‌کند که باعث درخشش برنامه شما می‌شود.
• ابزارهای هوشمند هوش مصنوعی: می‌تواند در وب به دنبال اسناد API بگردد و حتی یک مولد تصویر هوش مصنوعی یکپارچه دارد تا درجا برای برنامه شما دارایی‌های گرافیکی ایجاد کند.
و بهترین بخش؟ آنها همین حالا 20،000 اعتبار رایگان برای راه‌اندازی فروشگاه Play خود ارائه می‌دهند!
از این لینک برای دریافت مستقیم 20 هزار اعتبار رایگان خود استفاده کنید:
https://go.anything.com/cp-anythingplaystorelaunch
اگر اولین بار است که ثبت نام می‌کنید، از این لینک دعوت ویژه برای دریافت اعتبارهای بیشتر استفاده کنید:
https://www.anything.com/invite/bzxtuvp4
@ArchiveTell</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/archivetell/5802" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خفن ترین ربات پینترست در تلگرام
@PinterestAllBot
🔥
دانلود فوری ویدیوها و تصاویر پینترست
🔍
جستجوی مستقیم پینترست در تلگرام
👤
بررسی هر پروفایل پینترست
⚡
استفاده از جستجوی درون خطی در هر چت
👥
همچنین در گروه‌ها کار می‌کند
@ArchiveTell</div>
<div class="tg-footer">👁️ 584 · <a href="https://t.me/archivetell/5801" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای گل کانال
😎
vless://d02f9d1f-7e41-4e0b-8d11-439e0f719e74@95.182.85.120:80?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=ata.photodrop.ir&mode=auto&path=%2FMySecurePath123456789&security=none&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/archivetell/5800" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اقایون گویا یه روش اومده که میتونید
Sni spoofing
روی گوشی بدون روت اجرا کنید
+آموزش رو بزارم.....؟
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/5799" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اقایون کانفیگ sni کی داره
دارم یه چیو تست میکنم.....?
@Sina_1090</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/5798" target="_blank">📅 20:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروکسی ایرانسل ، سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.51&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5797" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پروکسی مخابرات و ایرانسل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5796" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=mEbRY_ePV9VoigZ3Yp_kg2pbgp_j8-L3scXpRIOWR518hruQoT5hhN5BUQ-wEUjQwAxkuYOwkr2v7sbklWZgmo_l43WcQaTUbpksjgLD6yA3Aox3M0LUtxVG7GzJc8ypot8QswoxV7CbCtI3Xz5iInjwU0jng96LeVQGqbQepdxFXE8XsP-ih9mvSgoPlqdoD5kzwR7V1Ho4usMf9EZ9oG34h-Cfroa_L4woF7qH3KdYzmkXTOkHT4z6q1u02Up6dNrnIuLDwpVgljx_pdAGBbVFMqlS__1T9Wt3w9m_SGnk-VN1K5cr0nTiQfm7bQqfvYk9-qVFcF6gCrgzwUikEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=mEbRY_ePV9VoigZ3Yp_kg2pbgp_j8-L3scXpRIOWR518hruQoT5hhN5BUQ-wEUjQwAxkuYOwkr2v7sbklWZgmo_l43WcQaTUbpksjgLD6yA3Aox3M0LUtxVG7GzJc8ypot8QswoxV7CbCtI3Xz5iInjwU0jng96LeVQGqbQepdxFXE8XsP-ih9mvSgoPlqdoD5kzwR7V1Ho4usMf9EZ9oG34h-Cfroa_L4woF7qH3KdYzmkXTOkHT4z6q1u02Up6dNrnIuLDwpVgljx_pdAGBbVFMqlS__1T9Wt3w9m_SGnk-VN1K5cr0nTiQfm7bQqfvYk9-qVFcF6gCrgzwUikEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دوبله ویدیو با حفظ احساسات واقعی صدا!
📌
شرکت ElevenLabs نسخه جدید Dubbing Studio را معرفی کرده که می‌تواند ویدیوها را به بیش از ۹۰ زبان دوبله کند؛ آن هم بدون اینکه حس و لحن گوینده اصلی از بین برود.
⚡
پشتیبانی از بیش از ۹۰ زبان
🎭
حفظ احساسات، لحن و سبک صحبت
👥
تشخیص چندین گوینده در یک ویدیو
🎵
جداسازی خودکار موسیقی پس‌زمینه
🎬
هماهنگی دوبله با زمان‌بندی ویدیو
💡
اگر گوینده بخندد، هیجان‌زده شود یا آرام صحبت کند، هوش مصنوعی تلاش می‌کند همان حس را در زبان مقصد نیز بازسازی کند.
🎥
ابزار بسیار جذابی برای تولیدکنندگان محتوا، یوتیوبرها، مدرس‌ها و کسانی که مخاطب بین‌المللی دارند.
🌐
elevenlabs.io/dubbing-studio
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5794" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برنامه‌ریزی هوش مصنوعی برای هفته کاری ایده‌آل
reclaim.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/5793" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=I8ilb0ttGLZ9hEuHGSM155jDw8CNb-cONV_cM0Uyq4YWfklp6URv_SGJ1oU7S9O79KfHMHMj-RnzuOSqUOxVx8JlSnOBky7ZPa-Kpb7PGui_KBLN3Qee5B9SHm89gZZCptnjuBhRjRDmq4eCI3iKebeSb918pC55SMqHMJNexYdUDyZO8OkMkw5esDHBAYnNIErvz7fh0JHPOqlScFPLFNVQGibhopojDlSXaiK-V70nUyb-JhhJ-mU2e-xqKKJO8Pju5M-tVjImyGdVyXnaS4OSZD9tSsZFQwIxe5k6OSMgawuFCUPla6JmJl21zxv_O_ZGWHupWITRz59nM4_8Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=I8ilb0ttGLZ9hEuHGSM155jDw8CNb-cONV_cM0Uyq4YWfklp6URv_SGJ1oU7S9O79KfHMHMj-RnzuOSqUOxVx8JlSnOBky7ZPa-Kpb7PGui_KBLN3Qee5B9SHm89gZZCptnjuBhRjRDmq4eCI3iKebeSb918pC55SMqHMJNexYdUDyZO8OkMkw5esDHBAYnNIErvz7fh0JHPOqlScFPLFNVQGibhopojDlSXaiK-V70nUyb-JhhJ-mU2e-xqKKJO8Pju5M-tVjImyGdVyXnaS4OSZD9tSsZFQwIxe5k6OSMgawuFCUPla6JmJl21zxv_O_ZGWHupWITRz59nM4_8Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📄
یک ابزار رایگان و متن‌باز برای ویرایش PDF!
📌
پروژه Every PDF به شما اجازه می‌دهد فایل‌های PDF را بدون نیاز به اشتراک‌های گران‌قیمت و نرم‌افزارهای سنگین ویرایش کنید.
✏️
ویرایش مستقیم متن PDF
🖼
افزودن تصویر، لوگو و واترمارک
📑
ادغام چند فایل PDF
✂️
تقسیم فایل‌های حجیم به چند بخش
💻
پشتیبانی از ویندوز و macOS
💡
اگر فقط برای چند تغییر ساده مجبور به استفاده از ابزارهای پولی می‌شوید، این پروژه متن‌باز می‌تواند جایگزین خوبی باشد.
📥
لینک پروژه:
github.com/DDULDDUCK/every-pdf
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/5792" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuHx3WlccOVkzAVhpvsnm49nMdYc00rVlt6EcDFj9jnkW_orHFjpe2Lzw7vVJiXP-_eap3dSu9pNle3InApAafCYWNK8miQpsDZjrVg908wz8i9IIjZ6WtOkWjPmAzXEiQ5Gf84WWQ1x3c6LWH701TiU_4QETTbb8L-N5F71k7_OStdyoaxmHEbuYQL88hEfC-7PMwRtDmQeIFt2BuO0MLLaTKay-JuN-_ZxTs0Gjcz_BlJ6y6ATwXX3Y2PRI1eWttyccbXaW59pv2PG79Vsv4DxmGTKahLR0KwMlklEh369FPEbPESetvGKimv5wLbS7nNkG8og1MvCPo-wdoelmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💧
دستگاهی که آب دریا را شیرین می‌کند و همزمان لیتیوم استخراج می‌کند!
📌
پژوهشگران آمریکایی فناوری جدیدی برای نمک‌زدایی آب دریا توسعه داده‌اند که بدون نیاز به برق و تنها با استفاده از نور خورشید کار می‌کند.
⚡
بدون مصرف برق
☀️
متکی به انرژی خورشیدی
🧼
قابلیت خودتمیزشوندگی
🌊
تبدیل آب شور به آب شیرین
🔋
امکان استخراج لیتیوم از نمک‌های باقی‌مانده
💡
نکته جالب اینجاست که نسخه پیشرفته‌تر این فناوری می‌تواند لیتیوم را به‌صورت انتخابی از مواد باقی‌مانده پس از نمک‌زدایی جدا کند؛ عنصری که نقش مهمی در تولید باتری‌های مدرن دارد.
🔬
اگر این فناوری به تولید انبوه برسد، می‌تواند هم به بحران کم‌آبی و هم به تأمین مواد اولیه باتری‌ها کمک کند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5791" target="_blank">📅 17:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروکسی
https://t.me/proxy?server=r33.proxytg.space&port=8443&secret=eec38451cb166b3ed3a1bbf1d4e7e382817233332e70726f787974672e7370616365&&
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/5790" target="_blank">📅 17:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI0MTA1MjgzZi1iMDM2LTQwNDMtYTE2NS0xM2MyYjA1MTY0MDgiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwMl9zNDk3ODM2LTIwNC44ME1C8J+TiiIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJub25lIiwidHlwZSI6Im5vbmUiLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiJkNWZhZjU3OS04YmMyLTRlZmUtOWFlYi05YTRhOWFiM2VlYWYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwM19hXzIyNjYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI4NDJmYmM5NC1kNzMwLTQyNTAtODYyNi05MzQ1M2NjMWE1NmYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgyODYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5789" target="_blank">📅 17:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">vmess://eyJhZGQiOiJhbnRlbi5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoidDIuYWxpc2VjdmljZS5pciIsImlkIjoiMmJiODVkNzQtNGE0NC00NWY2LTg3NzUtMDc3M2I0NjZjNjRlIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsInBvcnQiOiIyMDk1IiwicHMiOiJOZXctNzk1Xy0xMC4wMEdCIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5788" target="_blank">📅 17:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWj5S1tWGXIjsMp8Hvh9D8Era1qe3JPJY2s9-_Yj3-1XAXngUMwLP73h_8OCqooSzs4NAzBQ3BW7y7vZ0CYjXMB4yuKrQBbeZsSfwcty1HqoSrTZE71FFvnf0CHgzrzOgMS1EDVsifqPzTVYIK5YC36d9I3laVSCdlPrSkvPzhVIbx6eSxkCVsWaXuIJLr243BWGgUiq3ERuMZXNZoQM-aB3bqXJf9xOXiU77DWil4u_KRfslNSqIoxnGO9OW3ewPnZ72W5oPdlLp6AHt9JKEtnKIyxAgRRdu5vjpRDyXZgvVAvyF-jBasl91enF6cDw0mItH5hzivZvvQG0zTGznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxghGp3O3n_ekmEpUJEIO6N46bDNKjqrb4MuHnbvogR68kbNdlNl1drz4D008iJ-7Ln6UZOARS5Aw7spLDVrQUE0S1RtrBvInIx0EwmRuRn0702qnraKIwvY4KlCsHRDrwva6XRWm-1zGUR4XelIqRfQEWBTIe6E35uTvHu-TKkS-i6Grr2cYeMJAx_aPYm7npFP9q6g0d12W_clI5MdARhTAWxZGMzglKrbNdBPzJTLKF8ic3wlxny1aHhkxFvCP1p6ACxO1X8yBGRdQNwPujX7YTb33jVf5JmTTPXlrZrZKnaEp5onRdKk6jH9j0zgutvXflZVVef4b9H1ot3_sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نسخه جدید MidONe Scanner منتشر شد!
اگر دنبال IP تمیز CDN، کلودفلر یا DNSهای سریع هستید، این اپ اندرویدی می‌تواند کارتان را راحت‌تر کند.
✅
اسکن حرفه‌ای CDN و Cloudflare
✅
پیدا کردن IPهای سالم از روی رنج
✅
تست و رتبه‌بندی DNSها
✅
تشخیص IPهای ناپایدار و محدودشده
✅
ذخیره و کپی نتایج با یک لمس
برخلاف خیلی از اسکنرها، فقط پینگ نمی‌گیرد؛ اتصال واقعی را تست می‌کند تا نتیجه به چیزی که در عمل تجربه می‌کنید نزدیک‌تر باشد.
⚡
📥
دانلود:
github.com/mwhammadrezss/midonescanner-android
توسعه دهنده
@mwhamadreza
یکی از ممبرای عزیز کانال
❤️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5786" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRELTqFce2-0MNUl8b6fIotJSS8dvDfDGYzBKJjR3sZ09GtbQJe3CtAq2taXW7LeGfoHCWit8RHtbwSmxnaj1B88RmzO2FWfjErHbYJNp5xUONQ2kE0KsxzcizO58-A2Ke9hX76oCLl49uQ-KpGFbW2r21buYZb5q00c_sID_7Kg783fSO6tIfV1rB4MHBmygixW2y3gw1eoPHkDmdaoDIP6Wl9mVHMc-lN04Q_tYXOsZRzdxIaqU2FMHXlE4_YzgZb-hvivpOdEMtJqGDUrKi-sZUUscImfe1GiKVJPYUNnSTVJfqqbwItEvhw2oGcqIuflylWjYF6sqGLLjpicWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
انتقال فایل بین گوشی، ویندوز، مک و لینوکس بدون نصب هیچ برنامه‌ای!
توسعه‌دهندگان LocalSend نسخه تحت‌وب این سرویس را منتشر کردند و حالا فقط با مرورگر می‌توانید فایل جابه‌جا کنید.
🚀
✅
بدون ثبت‌نام
✅
بدون نصب برنامه
✅
بدون محدودیت حجم فایل
✅
سازگار با همه سیستم‌عامل‌ها
کافیست هر دو دستگاه به یک Wi-Fi وصل باشند، سایت را باز کنید و انتقال را شروع کنید.
🌐
web.localsend.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5782" target="_blank">📅 15:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1uj4uPWxeDbXXP9THsfP1v8SEnCY-DqJmdEtzxKPNs6M41uHhcWMEciHwaTJXyN764ysrJPcWKhPoHQJvI3lav_3yFifKAOWuJO89orNfA8XtM-C7YerqHzsPFZX3J1LSiNtRXOgM0tqbc9ugBKX6CeeuOvH-REJe20p4sV2DcXucKjOf-WQB12VdRbZSuCTPD7vRi-RH9buDYxH3_oSeSg4-hjKbGutfBqUnOTL_SeC0JdAPnLiV5SHEv9uMHgwYRjJ_4L5mKjtwO_d3xAMd0orzGQJlE5NkJuty_ukFzSvSh4aNsXboGKUXY6JQXBtK_i0qm2Lts74Tv60D8ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell @ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5781" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/5779" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ نامحدود ۱ ساعته اهدایی یکی از ممبرای عزیز
😁
❤️
vless://614ad5da-e5cc-479d-bc90-3db549ca96e4@84.75.220.223:33434?encryption=none&fp=chrome&pbk=CBLftLCz0w2EX8H3sQ4ahU_lc9_aWJZO_8OHJEWGjDo&security=reality&sid=0af57b636837&sni=www.yahoo.com&type=tcp#ArchiveTell%201
vless://afce710f-2261-403e-ada6-459dbcb44b64@84.75.220.223:80?encryption=none&fp=chrome&pbk=XnjRQWaZ2QGrIJBGPuYOePg2wLl_ZM_gkCyJ2aKxylQ&security=reality&sid=7797159c&sni=www.yahoo.com&type=tcp#ArchiveTell%202
vless://3d1dbf5c-6f7d-47ee-9138-e217e0a77265@84.75.220.223:41034?encryption=none&mode=auto&path=%2F&security=none&type=xhttp#ArchiveTell%203
vless://5c5cb739-1112-4eea-bad1-282db5c24512@84.75.220.223:443?encryption=none&fp=chrome&pbk=g_oiiXO-P1L5MgEzE9qx7Vt0x-Z1-vI5QjXmscfh6Uw&security=reality&sid=27fd6d7ea3&sni=www.samsung.com&type=tcp#ArchiveTell%204
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5778" target="_blank">📅 13:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8boXwZ1TvLQF8GbaXsqlmjNLurH85h8wtHJuPCSCBGZXMK0TyCZxi5a-4zIuHrPxhfxSj3R0oD3tUPU1G_a0wXihdH2x10YRHRoIgoN3ocOE4-Ow4MJQ9bQs7w76sSJIyJTPqmNSdWFPkqDKOksdOhnKEG2e7yVj2D2exqumP7i4AxROPqPGy3OjhMbOb2O9QeoDIoIItG9crSLcVKC_X8uZfBZ8RUWMeyaI2e5p-aZOCpjGFw5k-SXF-mKXd9Qs0mWsem2GI7dma8KSB-3RpCOvMBBRt7tLn0ymaGk2uFJNkCUZHheXb_uQoWgt3FPittddRRidognWwZGd-Lpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5777" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4 و HTTP
📋
پروفایل‌های آماده و قابل ذخیره
📶
نمایش پینگ اتصال
🔒
کاملاً لوکال و متن‌باز
💡
مناسب برای زمانی که می‌خواهید فقط مرورگر از فیلترشکن استفاده کند و برنامه‌های دیگر مثل بازی‌ها یا نرم‌افزارهای بانکی بدون پراکسی کار کنند.
📥
آموزش نصب سریع:
فایل
.zip
رو از بخش Releases گیت‌هاب دانلود و اکسترکت کنید. بعد توی کروم برید به آدرس
chrome://extensions/
، حالت Developer Mode (بالا سمت راست) رو روشن کنید و روی
Load unpacked
بزنید و همون پوشه‌ای که اکسترکت کردید رو انتخاب کنید. تمام!
🔗
لینک دانلود و سورس‌کد در گیت‌هاب:
🐙
https://github.com/johncarterjourney-rgb/advanced-proxy-manager
👨‍💻
Dev:
@Bachedev
#Proxy
#Extension
#Chrome
#V2rayN
#OpenSource
➖
➖
➖
➖
➖
📢
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5776" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il3OFGkIRxYW-hXWPxAnBdCT74ftVrgpIX6UsyQfYd0AvRrWhJNSiv7dH3gljlXpaZsTYxrkGFv_eK4C3F3fR28IOngE1bqgs-xSRx32PWCiGuei_rMHuVgN7LRT0hY2JVztv0BqTlkH6SSFgctIrI5UpWBC7STo4dsqhi_YYMII0Dw8w0DunCbuDVFaOTL8QmfKKv3YN37Cg-HkETpNglLwxYO0uSvmbO-nqwrb3ezxC_4NEFzTnjxZCTZ3GYEREsSNhml8J1QLNvzrBbc5-9iMAHHAPgceKubZ2huacWhievqYdaP1jREh6Q60bgtWnb8U7UG_nlcZzT3VFGwrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی کردن سبک هر وب‌سایتی
👀
⚡
ابزاری که هر رابط کاربری را به یک فایل آماده برای استفاده در گردش‌های کاری هوش مصنوعی تبدیل می‌کند
🕤
کافیست لینک یک وب‌سایت را وارد کنید تا این سرویس به طور خودکار رنگ‌ها، فونت‌ها، فاصله‌ها و ساختار رابط کاربری آن را اسکن کند.
🕤
این سرویس از صفحه اسکرین‌شات می‌گیرد و همه چیز را در یک فایل مرتب به همراه جزئیات طراحی گردآوری می‌کند.
🕤
نتیجه؟ یک پایه آماده برای تولید تصاویر مشابه با استفاده از هوش مصنوعی.
🕤
تنها کاری که باقی مانده این است که فایل را به یک مدل هوش مصنوعی بدهید و آن سبک را در پروژه خود اعمال کنید.
🕤
این ابزار رایگان، متن‌باز و به صورت محلی اجرا می‌شود.
https://www.designmd.supply/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5775" target="_blank">📅 12:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5774" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">trojan://humanity@188.114.97.6:443?path=%2Fassignment&security=tls&alpn=http%2F1.1&insecure=1&host=www.calmloud.com&type=ws&allowInsecure=1&sni=www.calmloud.com#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5773" target="_blank">📅 12:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV5g5KZ3ifSHQrZ8XBBFPagHhm_VS_QB_qvcUasAm-VNh3lGPz6nCGgn8M8TRaLg00u-6WwC1Hj3bUvD-Lz_uyH2pjvCS58dnLke8fsHnznMDT42WpERz6Pl2uQ5_B_URUslAMII22SaWQ0lHImws3BYCPmN0ri5pcQUsFBkQ0erMb0KFY_0KHIRDBc5OFAzaJam-TO9Q7JMGqAAIeVzZTqQzugT3mTQmd305iPr-F1crXvEQfjlDD_eSCmF4A0mLbb3ABqr1Ox5oNpCgOsERFS0llsYCrN3-8HWqD_MZM_TgLP26I9Dgn6ZiKZYAotgd5LaSf76UYOLwTnOgiJb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ابزار جدید برای پیدا کردن IPهای سالم کلودفلر!
📌
پروژه CrimsonCF یک وب‌اپ متن‌باز برای اسکن رنج‌های Cloudflare است که به‌جای تست HTTPS، مستقیماً اتصال TCP را بررسی می‌کند و IPهای سالم را با سرعت بالا پیدا می‌کند.
⚡
اسکن سریع و موازی
📋
خروجی آماده برای Xray،…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5772" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
ابزار جدید برای پیدا کردن IPهای سالم کلودفلر!
📌
پروژه CrimsonCF یک وب‌اپ متن‌باز برای اسکن رنج‌های Cloudflare است که به‌جای تست HTTPS، مستقیماً اتصال TCP را بررسی می‌کند و IPهای سالم را با سرعت بالا پیدا می‌کند.
⚡
اسکن سریع و موازی
📋
خروجی آماده برای Xray، sing-box و Clash
🗂
ذخیره تاریخچه اسکن‌ها
🌐
ثبت سریع‌ترین IPها روی DNS کلودفلر
💡
اگر برای کانفیگ‌هایتان مدام دنبال IPهای سالم Cloudflare هستید، این پروژه می‌تواند حسابی به کارتان بیاید.
📥
لینک پروژه:
github.com/amir0zx/CrimsonCF
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5771" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5770">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۱ ترا کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://2d0b825d-cbe0-46b7-98e9-e955b99e71c9@cz.helper-internet.com:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=W-zf_ncm9sYALF5EqvUsxqTkYGdAw-tQczT2SqwVMGE&security=reality&sid=ff776ff77be48b88&sni=cz.helper-internet.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5770" target="_blank">📅 11:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5769">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ربات های سرچ تلگرام
@MotherSearchBot
@en_SearchBot
@SearcheeBot
@argo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5769" target="_blank">📅 09:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤖
افزونه‌ای که کاربران Claude باید بشناسند!
📌
افزونه Tally میزان استفاده و محدودیت‌های Claude را به‌صورت لحظه‌ای نمایش می‌دهد و قبل از رسیدن به سقف پیام‌ها، وضعیت حسابتان را نشان می‌دهد.
⚡
نمایش تعداد پیام‌های باقی‌مانده
⏳
نمایش زمان بازنشانی محدودیت‌ها
📊
نمایش میزان مصرف جلسه و هفتگی
🔄
انتقال گفتگو به ChatGPT، Gemini و Grok با یک کلیک
💡
جالب‌ترین قابلیتش اینجاست که اگر وسط کار به محدودیت Claude بخورید، می‌توانید کل چت، فایل‌ها و کدهای تولیدشده را بدون کپی‌پیست دستی به یک هوش مصنوعی دیگر منتقل کنید.
🎁
نسخه رایگان روزانه ۲ انتقال را در اختیارتان قرار می‌دهد.
📥
لینک افزونه:
chromewebstore.google.com/detail/tally-claude-token-counter/baicaaiepddopbodaccgfffdimceidbp
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5768" target="_blank">📅 09:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6e5-pPw6TCcNLF7uTev7bGmiL0FAyptzt-qVjZSmEsQtHFSxJlK_FfasveCy_tsIUh4EfSAq9zeZAiyJ-24Lnqf363ycclbdJOs79H1pkMpZxCFmxiUbEaZYED-b9X8pQLpAvQF3Rpl-LEV023hJbRqpOeAnPHr_ImijK49FlfSa1bPCB61y262cxkbzvC2nlbBS4eqVzn8mdHiqNQAxXWw2ckmgGwv0r3febJuVLNPFbg9-18xYh8tfFFoM0OT3R7Boh3IXK0XOI3CXiefUEwQoX3ZypB0XX6ruRXjogP9zn0Pg9P8XjV876QwlKkrcJ516jMEkQkOWw-9DC8R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق العاده</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5767" target="_blank">📅 08:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانفیگ نامحدود اهدایی یکی از ممبرای عزیز
❤️
vless://42adc67e-49cb-4c62-b6ec-1b26c33980e3@140.248.190.1:443?allowInsecure=1&alpn=h2&encryption=none&host=shahrvand.ir&mode=packet-up&path=%2F%3Fed%3D2560&security=tls&sni=speedtest.net&type=xhttp#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF%20%D8%A2%D8%B1%D8%B4%DB%8C%D9%88%D8%AA%D9%84
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5766" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی یکی از ممبرای گل
🤍
vless://9146fb59-a4fe-4bb8-9a25-9eb5fc31f45a@a.harmonycodesign.shop:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=TAJxu6wnkIMcHn5KhnND8RiNJr6-q8zIQAwWzQdSqXo&security=reality&sid=8eb76dd83c&sni=www.yahoo.com&spx=%2FiQkeLHgmqtVGmzs&type=tcp#test%202-100.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5765" target="_blank">📅 07:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m78VQXV-Iwoa7InqCSQUPSVFfZJ_L-Z2WQ3f2PyP6ruCV6caNZM5q-pZYIbcNGGhIQqASgVUgnxxou9iCT3SMhzDZM4bf1iCC1TarzT8ifAawLxvYljimGFdOo-l9U042NEIX-lHisIudX3g-LBvOlujh3BATOjo3xn9hA67HXHJFauX-KeN8BVA5pPaEzh5-9qnRflNppNe1LPU1X_UlABWS5vdiKo0QmFnk8AUeDenuqixmt4SzPC7WrjeZOinVYqIhay6kd8Z1wPfl6UkKUsZAO-id1UkICbEzuIxguCoiD0nkV6rZCS4ElYm3NrjeMjSRLOefjF94FcX_BvJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت
گوگل
شما به صورت پیش فرض روی
3 ماه
قرار گرفته تا اگر بعد از
ماه سوم اکتیو نشدین
از
دسترس
خارج بشه
🤩
توسط لینک هایی که پایین این پست در دسترستون قرار میگیره میتونین اکانت های جیمیل خودتون رو روی
18 ماه
تنطیم کنید
👍
➡️
https://myaccount.google.com/inactive
➡️
https://myaccount.google.com/inactive/inactivityperiod
💻
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5764" target="_blank">📅 02:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetelll.npvt</div>
  <div class="tg-doc-extra">6.9 KB</div>
</div>
<a href="https://t.me/archivetell/5763" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5763" target="_blank">📅 02:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5762" target="_blank">📅 02:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
ساب هیدیفای ، اد کنید
https://panel-01.sidin.com.de/NvBmpAnVK6fqJOC4hmd7eiSaJyLs/64d5ede0-8ffb-4636-9565-bf95515a479c/#اهدایی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5761" target="_blank">📅 02:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5760" target="_blank">📅 02:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromOpenSourcePulse</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIZ_89E8BI_WjyOogsq7gwRGDseMJKwe6wUGwvrl9nu7JhlL1v55lRFeHM7bijvvUsgt9enIU0ELjY4HjXSNqvJH3xOQcyG2t5DC_mQi66Oga1yVsvzBwa2QvlNgkgZUfOD-XWZ9z1mRHCHtfgFCakKBpc2w7bzd8RLOChiiMk85rpYSuAaMewxFFrob2MNURDSmpiw4LZQtoPlNmIQxPEf2vuf0930FsASYHmhy0qUJ3Se49eLGYLjCVEIAQ5D8UeSYsnrryYkeenVMvRt-fcnOFuVTYLTF2ptpf2Qisli5eDN57t5NOBM_Dtl2ZfVHswkelT4n2cG3Zo7DrtcRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
New Release Alert!
📦
MITM-DomainFronting
🏷
Category:
Community Suggested
🔖
Version:
MITM-DomainFronting v22
📅
Released: 2026-05-30 21:21 UTC
📊
Assets: 0 files
📝
What's New:
Add DOH; Add meta (facebook, instagram, whatsapp, ...); Unrestricted youtube
🔗
View on GitHub
📥
Download Release</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5759" target="_blank">📅 02:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💣
بمب جدید اینترنت آزاد: دسترسی به یوتیوب و اینستاگرام «بدون نیاز به سرور و ورکر!»
رفقای آرشیوتل سلام!
🌹
امروز می‌خواهیم یک متد کاملاً انقلابی و تازه نفس (آپدیت شده در ۱۰ خرداد ۱۴۰۵) را به شما معرفی کنیم که معادلات فیلترینگ را به هم ریخته است. پروژه‌ای به نام
MITM-DomainFronting
(توسط توسعه‌دهنده ایرانی patterniha) که حالا مستقیماً به هسته Xray اضافه شده است.
این متد چه کار می‌کند؟
با این روش، شما برای باز کردن سرویس‌های مسدود شده (یوتیوب، اینستاگرام، واتس‌اپ، فیسبوک، ردیت و سایت‌های پشت دیتاسنتر Fastly)
هیچ نیازی به خرید سرور مجازی (VPS) یا ساخت ورکر کلودفلر ندارید!
این متد با جعل هویت سرور (MITM) و استفاده از یک SNI جعلی، اینترنت شما را مستقیماً و به صورت لوکال به این پلتفرم‌ها وصل می‌کند.
---
⚠️
یک هشدار امنیتی به شدت مهم (قبل از شروع):
این روش نیاز به ساخت یک گواهی امنیتی (Certificate) شخصی دارد.
تحت هیچ شرایطی
فایل‌های Certificate دیگران را روی گوشی یا سیستم خود نصب نکنید و فایل‌های خودتان را هم به کسی ندهید. این فایل‌ها کلید امنیت دستگاه شما هستند!
---
🛠
آموزش راه‌اندازی (خلاصه و مفید)
۱. ساخت گواهی امنیتی (Certificate):
*
در ویندوز:
فایل
certificate_generator.bat
را از گیت‌هاب پروژه دانلود کرده و در پوشه
bin
نرم‌افزار v2rayN اجرا کنید تا دو فایل
mycert.crt
و
mycert.key
ساخته شود.
*
در اندروید:
به سایت‌های سازنده SSL رایگان (مثل regery) بروید و یک گواهی خودامضا (Self-signed) بسازید و نام آن‌ها را به
mycert.crt
و
mycert.key
تغییر دهید.
۲. معرفی گواهی به دستگاه (Trusted Root):
* شما باید فایل
.crt
را در ویندوز (از طریق کلیک راست و Install Certificate) یا در اندروید (از طریق تنظیمات Security و بخش Install CA Certificate) به عنوان یک گواهی «مورد اعتماد» نصب کنید تا دستگاه اجازه تغییر مسیر ترافیک را بدهد.
۳. اجرای کانفیگ جادویی:
* فایل
MITM-DomainFronting.json
را از گیت‌هاب دانلود کنید.
*
در ویندوز:
در برنامه v2rayN یک Custom Configuration بسازید و این فایل را وارد کنید (Core Type را حتماً روی Xray بگذارید و Socks Port خالی باشد).
*
در اندروید:
فایل‌های گواهی را در بخش Asset Files برنامه v2rayNG وارد کنید و سپس فایل json کانفیگ را Import کنید. (گزینه Enable Hev TUN باید روشن باشد).
---
📌
چند نکته طلایی:
۱. این متد در گوشی‌های اندرویدی (که روت نیستند)
فقط روی مرورگرها
(مثل کروم) کار می‌کند. یعنی برای استفاده از یوتیوب یا اینستاگرام باید از طریق مرورگر گوشی وارد آن‌ها شوید، نه اپلیکیشن اصلی.
۲. در فایرفاکس باید تنظیمات
Use third party CA certificates
را به صورت دستی در بخش Secret Settings فعال کنید.
📥
لینک دانلود فایل‌های مورد نیاز از گیت‌هاب اصلی پروژه:
[لینک گیت‌هاب MITM-DomainFronting](
https://github.com/patterniha/MITM-DomainFronting
)
🔥
این پست را برای تمام کسانی که توان خرید سرور ندارند یا از قطعی‌ها خسته شده‌اند فوروارد کنید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5758" target="_blank">📅 02:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
اتفاقات عجیبی در Bitwarden در حال رخ دادن است!
📌
برخی کاربران متوجه تغییرات قابل‌توجهی در پیام‌های تبلیغاتی و مدیریتی Bitwarden شده‌اند؛ از حذف عبارت «Always Free» گرفته تا تغییر در ارزش‌های اعلام‌شده شرکت و جابه‌جایی در تیم مدیریت.
💡
این موضوع باعث شده بخشی از جامعه متن‌باز درباره آینده Bitwarden و حفظ رویکرد شفاف آن ابراز نگرانی کنند.
🔐
اگر به دنبال کنترل بیشتر روی اطلاعات خود هستید، بد نیست نگاهی به Vaultwarden بیندازید؛ یک پیاده‌سازی متن‌باز و سبک که روی سرور شخصی اجرا می‌شود و با اپلیکیشن‌ها و افزونه‌های Bitwarden سازگار است.
✅
میزبانی روی سرور شخصی
✅
سازگار با کلاینت‌های Bitwarden
✅
متن‌باز و قابل بررسی
✅
امکانات پیشرفته بدون نیاز به اشتراک رسمی Bitwarden
⚠️
فعلاً هیچ تغییری در امنیت Bitwarden گزارش نشده، اما برای بسیاری از کاربران حریم خصوصی، این تحولات ارزش دنبال کردن را دارد.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5757" target="_blank">📅 01:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">30 گیگ کانفیگ
🇺🇸
vless://02b0ce21-e1b0-456a-b26a-746948db90b2@104.167.199.250:21886?encryption=none&fp=chrome&pbk=lCJf5rHYWjlRoBt04knpHb3PJKX6lpmdnq1Uk8le6WY&security=reality&sid=6812cc8489&sni=www.yahoo.com&spx=%2FtVArRVlBAtoiJnE&type=tcp#30%20%DA%AF%DB%8C%DA%AF-30.00GB%F0%9F%93%8A
@archivetelll</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5756" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">50 گیگ کانفیگ مولتی .....
👾
💀
vless://61ff07a8-9f1d-4bac-a9a2-37249ad3a5b4@104.167.199.250:21886?encryption=none&fp=chrome&pbk=lCJf5rHYWjlRoBt04knpHb3PJKX6lpmdnq1Uk8le6WY&security=reality&sid=0febf6&sni=www.yahoo.com&spx=%2FAbfBgvqwqJDzQOU&type=tcp#10%DA%AF%DB%8C%DA%AF-10.00GB%F0%9F%93%8A
vless://1b16b6f8-b8dd-43d7-84f9-8eb8a7e15504@sina.35o.ir:25645?type=tcp&encryption=none&security=reality&pbk=GnAQ0pqW4HGqMuOY7crTmcQ56FuABKPP9YaiJzOS3X8&fp=chrome&sni=www.yahoo.com&sid=d6372f1a0a&spx=%2F#..
vless://cb61a314-9e39-45b5-bf3b-264912e7553b@panel.96s.ir:8080?type=ws&encryption=none&path=%2F&host=&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1#%DA%A9%D9%84%D9%88%D8%AF-%F0%9F%91%BE
@archivetelll</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5755" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
مولتی هست ، همشو اد کنید
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:35503?encryption=none&fp=chrome&pbk=kg3m6BZFVDfMlVFmB_mGcdt8DSep31F80p5HFcftbhU&security=reality&sid=25d3055f&sni=www.yahoo.com&type=tcp#-50.00GB%F0%9F%93%8A
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:34409?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&mode=auto&path=%2F&security=none&type=xhttp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:51796?encryption=none&fp=chrome&pbk=j8GasBT0TZtEb8wnWUqydRpfhJ8hYENOGSTMPOCkZgY&security=reality&sid=04f58eb4&sni=www.samsung.com&type=tcp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:80?encryption=none&fp=chrome&pbk=MSuNU70q36Ubt3AsmqUNYq4xreSxZOzGkIHsUt8SVig&security=reality&sid=5c20c9b00ee2be&sni=www.yahoo.com&type=tcp#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:37424?encryption=none&path=%2F&security=none&type=ws#50%20GB
vless://633ca2b1-2452-4b38-94f2-269d2a486ee9@104.167.196.143:443?encryption=none&fp=chrome&pbk=jPF_6gmAt1CFrD4DSoe8vl3SeEYjYpEaU7nt8JYsWUM&security=reality&sid=2a5fc7667f&sni=www.samsung.com&type=tcp#50%20GB
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5754" target="_blank">📅 20:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">​
🚀
آفر ویژه و اقتصادی سرور مجازی (VPS) از شرکت آمریکایی RackNerd
​اگر برای تونل های DNS، بالا آوردن پروژه mhr، ساختن تانل یا کانفیگ‌های شخصی عبور از محدودیت اینترنت دنبال یک سرور خارجی باکیفیت و از همه مهم‌تر «ارزان» می‌گردید، این تخفیف‌های سالانه رکنرد رو از دست ندید.
​
🔹
پلن ۱ گیگابایت رم: فقط ۲۱.۹۹ دلار «برای یک سال کامل» (یعنی ماهی کمتر از ۲ دلار!)
🔹
پلن ۲ گیگابایت رم: فقط ۳۵.۹۹ دلار برای یک سال
⚡️
سرعت پورت 1Gbps و پهنای باند فوق‌العاده بالا (۳ تا ۵ ترابایت)
🇺🇸
آی‌پی آمریکا
🎛
دسترسی کامل روت (Full Root Access) و مجازی‌سازی KVM
​این آفرها توی بخش عادی سایت به سختی پیدا میشن و برای مدت محدودی فعالن. از طریق لینک زیر می‌تونید مستقیماً وارد صفحه آفر ویژه بشید و پلن مورد نظرتون رو با همین قیمت ثبت کنید:
​
👇
ورود به صفحه آفر ویژه و خرید:
🔗
https://my.racknerd.com/aff.php?aff=20075
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5752" target="_blank">📅 20:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206RmpHM0lQYm55KzBaWVU0L3AxdlVMUDg0R2NLcEdvWnBXS0FheTE2VmhJdz0%3D@51.254.128.106:2083#%D9%81%D8%B1%D8%A7%D9%86%D8%B3%D9%87
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5750" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5747">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۱۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://599fc8a8-a939-405f-a755-922381ffa3ba@172.234.105.250:56845?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5747" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5746">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoYFVqSHPXGP1FoHl0Pa2zdfM9V3j197fSZyi-mD5epMBMU0AfyHGaneF-MOSNQqNxu2x4gHAX10LBGTurt8waF2TneVQeslr3Y6o6gkbSHgPWTmIVxavD2l_sstNucwzQwlXQbQjFr_3dx-DRzg3myx9Hk7beeVwNR6MzyFfG99dBGN6x2F93SfloO8OsiEDer-EvQ8IG79B19b-5yYSJ_Ckv2WlmO3_jM6KLFg4VD_ZGO5pg__UinHrCCGiOL477gQWoMulpUmsl46czjsrM1kgKlKhoXkAhcP7_Q3d9jM7lHbdRKSSgieF-eXT_3lC3GKKuPYkV97BYJfhp2jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس ProtonVPN اعلام کرده که با شروع اتصال اینترنت کاربران ایرانی، بسیاری از کاربران شروع به ساخت اکانت در این سرویس کردن و تعداد اکانتهای ساخت شده در ProtonVPN توسط کاربران ایرانی، 25 هزار درصد رشد نسبت به حالت عادی رو شاهد بوده
🤔
✈️
@Archivetell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5746" target="_blank">📅 19:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">10 گیگ کانفیگ سرور هلند....
🇳🇱
vless://60eab5f4-e085-49b6-9d1b-2e9122dcb6ee@panel.96s.ir:32373?type=xhttp&encryption=none&path=%2Fmarg&host=panel.96s.ir&mode=auto&x_padding_bytes=100-1000&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=panel.96s.ir#10%DA%AF%DB%8C%DA%AF
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5745" target="_blank">📅 18:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eV_ORvBCi9nrbQCX4sgLQYdm60HwR3AL4hujAHV3qrG2lJ4e254V8NXMiAqOdDHCey6Lx16FXJ7NxTAvYYB8mPVTogYB1zWz6xJ8eR0qnyb4n5t_IcDpfNuFGdILmL_vqgdutav5gz9nmp9VpNvNaF0-s2LdkB6vgk0pZtdlcHJzphcbpthE74cEbRqyyz4IJGwKYab5Hpc5OgWAQ0jrTagrsUPO-_pyhsIYCQzOm62zKbCZjN4a7t7nYNC-9nENBeQFTbRROzhLIDTL8H8IjNtHu6KsdAns3EEcXuHGyluSAuHqlhA_K_DnrsxlHpzJaBe0Kf8k71rxOemyhsqCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSguDbZtKa6G6zjpYgqzmF84-jbE-WQT_bXlqdOop6bP9Ur2EvXmxTuN3pw1Jsi4CjBkAD35V5O3L50uzJAOPSfGFRVOVpP1P7igFq4UVVE4IoHQh0-ZyjE7JE9xaT5t7bt0Ly5yQtEHV98AUSiObLSVL3RnHO0L2A51HgRVJzmkXFKet2kkyAcikSiSJhO0rkwmwclSWvOct27n9OqxSIua8terVk72L99Y4jWmGVI39nofaLKAOmlqHi5DGQClIvBW4HxyQ6hkoo7AZOMI4ioiugXRhfFY0PLwVceI-gOzxqJzzUCphsUOKqnWqrU3PZU2fTV5RLqBUxOeW31ZtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9846908dae.mp4?token=lEYJIrfT0-AZOz_IICzyoTQip8hHsNTemkQEMTaLTDCeSNb8sdrtOCBLWaMRZANY8QTXNcdNJqtzKAkiyXjbOhjLV5xeaG-W64zfXGd9huSeJhHg_ExG0IkG5ySNdqIWvVSSRn2ClE1v2d6TxgMEF6hulZ3WKKNquU0hhxP0KFHSqbOdnpMx5m7zgl8RaH9BIF3J8CjtOTGHgee5h1kSBamj6NjJlqBJaqC8-sBbPdB1gWsczeFowIRPGOcXmyIxB64PsAeqFIfH-aV-sZCpWind_kTMX4Hqag8QvTnhfcwwKfzeDGhbBdT3Q9oaIb8XEZPHaVNWn5ncnRPlzLwrJrQ3cx30F3j6A2bNrQel970dfrzFnmjzuUa1OjOy47zDQzha1U6h5s22dfhNlQFw5uoq5tHm0MTZd7iq6Raes8LDWs1eEKKkByTlfszOZlTDH1pE_tnK5Hyk7-ZXxkAvyCHI6lua7Dhh9yCzob0ZrIVOUMT14RYzzuP_M82bTFNkeCG-0kPBNCK1gXJsj4FHiFZ0b89d_fMZX0sB9v7ppAven3t_tTa9O3rCJvDCorRY8fJ4Prkrea_b3Q4561x5yUXrQlX9Bvukhh6SWZqkKmspyAVTuwzfhSZKSR-tW9QujPIRxof5-WySEdw_D7BJg7hyhZj3VVA_F6Ptz4v5DG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9846908dae.mp4?token=lEYJIrfT0-AZOz_IICzyoTQip8hHsNTemkQEMTaLTDCeSNb8sdrtOCBLWaMRZANY8QTXNcdNJqtzKAkiyXjbOhjLV5xeaG-W64zfXGd9huSeJhHg_ExG0IkG5ySNdqIWvVSSRn2ClE1v2d6TxgMEF6hulZ3WKKNquU0hhxP0KFHSqbOdnpMx5m7zgl8RaH9BIF3J8CjtOTGHgee5h1kSBamj6NjJlqBJaqC8-sBbPdB1gWsczeFowIRPGOcXmyIxB64PsAeqFIfH-aV-sZCpWind_kTMX4Hqag8QvTnhfcwwKfzeDGhbBdT3Q9oaIb8XEZPHaVNWn5ncnRPlzLwrJrQ3cx30F3j6A2bNrQel970dfrzFnmjzuUa1OjOy47zDQzha1U6h5s22dfhNlQFw5uoq5tHm0MTZd7iq6Raes8LDWs1eEKKkByTlfszOZlTDH1pE_tnK5Hyk7-ZXxkAvyCHI6lua7Dhh9yCzob0ZrIVOUMT14RYzzuP_M82bTFNkeCG-0kPBNCK1gXJsj4FHiFZ0b89d_fMZX0sB9v7ppAven3t_tTa9O3rCJvDCorRY8fJ4Prkrea_b3Q4561x5yUXrQlX9Bvukhh6SWZqkKmspyAVTuwzfhSZKSR-tW9QujPIRxof5-WySEdw_D7BJg7hyhZj3VVA_F6Ptz4v5DG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
اگر با Claude Code کار می‌کنید، این پروژه را از دست ندهید!
📌
Claude Flow یک مجموعه متن‌باز از ابزارها، عامل‌ها و افزونه‌هاست که برای توسعه نرم‌افزار با Claude Code طراحی شده است.
⚡
بیش از ۱۰۰ Agent و Skill آماده
🧠
فریمورک SuperClaude برای مدیریت پروژه‌ها
🔌
افزونه‌ها و دستورات کاربردی
📋
مدیریت پروژه به کمک Agentهای هوش مصنوعی
💻
ابزارهای CLI برای کنترل و هماهنگی Agentها
💡
اگر از Claude Code برای برنامه‌نویسی استفاده می‌کنید، این مجموعه می‌تواند بخش زیادی از کارهای تکراری و زمان‌بر را خودکار کند.
📥
لینک پروژه:
github.com/ruvnet/claude-flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/archivetell/5742" target="_blank">📅 18:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان، تانل تست کردین؟
سرعتش میگن خوب نیس
خوبه؟</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5741" target="_blank">📅 18:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBg-fwy4QVkqdUSEfPHFa5SIyTnkDDY6dDHROPDjZIT-F4kPGCyM0NZIGa0en-aQQNLaP7Tm-Sv-UdYbi15vJpo3j1pDxwMRIhgmFBuKC0_u992JWOoyeROo1zUmNPh6JSSrqf6J2tbrlNLurunEVnKNmp7sgF-AL9uqClnclsS5cvchDpFKn4blcITz-DnOqz8iSe9gYt9TKty4egEoCdREshTHp3PADmbCyg4RreBMaFODrzvqEz9SAVyO42E0V0N4OFMFEXKTBvYivX4tFuYKwbzsKo6B7BFD_Mn1kYOqd0SrLPCVEZ1g66Mgk3iuVZlp5-PMiKAPij4o4yzj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Burner Emails
پنهان کردن ایمیل واقعی خود —  آدرس‌های یکبار مصرف را در عرض چند ثانیه مستقیماً در کروم تولید می‌کند.
https://burnermail.io/
🕤
هنگام ثبت‌نام از ایمیل موقت به جای ایمیل شخصی استفاده می‌کنیم.
🕤
تمام ایمیل‌ها به‌طور خودکار به ایمیل اصلی شما ارسال می‌شوند.
🕤
آدرس واقعی مخفی می‌ماند — سایت‌ها و سرویس‌ها آن را نخواهند دید.
🕤
از اسپم خسته شده‌اید — آدرس موقت را با یک کلیک غیرفعال کنید.
🕤
به عنوان یک پراکسی ایمیل کامل برای حفظ حریم خصوصی و محافظت در برابر هرزنامه کار می‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5740" target="_blank">📅 18:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5739" target="_blank">📅 17:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-WwZxI7PUrtKVpkF5Fl1oNaf-ESG6q5Vyl09Tjpjj3Ja3fw56Wgd-zAoi98KM-YYTZvPQ9MF4wDrHUs41xKhjVIMpjJEtcWh2Q_WBUkIdu-wwZ9P5ew9VrHyMaESD1S8mH1xXavGeP0KBFR54b9WtrnUk8wzpg6LlPHxCYLtYzpNENT34CFxeBdoBd8ZfL4JQfDQo9H5XA83Of3eLt_P0qFr6clJz9r6xIF5eJlYI_XsCR9S_k-s4HQy0rf93DIpltXmvWNRW-Um1d4BoZd62DILNmoFFq4KWNGdcruzdBJJ2WIMFvQAGblgI7a7De9kRyC5MwvdTgAdY5oNnEWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر تو متود Sni spoofing درست براتون پینگ نمیگیره و براتون
➖
میزنه از قسمت :‌
Settings
➡️
Options Settings
➡️
V2rayn Settings
➡️
Speed Ping Test Url
رو روی Apple ست کنید
✅
❤
@Archivetell</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5738" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش جامع نصب و شخصی‌سازی پنل سنایی (3x-ui) از طریق منوی مدیریت ترمینال
🎛
کالبدشکافی پنل سنایی (3x-ui)؛ نقشه راهنمای کامل
🚀
آموزش ساخت امن‌ترین کانفیگ‌های VLESS Reality
⚡️
آموزش راه‌اندازی متد XHTTP؛ راهکارِ نهایی برای عبور از سخت‌ترین محدودیت‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5737" target="_blank">📅 17:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
آموزش ساخت امن‌ترین کانفیگ‌های VLESS REALITY (پروتکل غیرقابل فیلتر!)  ---  رفقا سلام!
✋
خیلی‌هاتون پرسیدید این کانفیگ‌های قدرتمندی که براتون می‌ذاریم دقیقاً چطوری ساخته میشن؟  امروز می‌خوایم قدم‌به‌قدم بهتون یاد بدیم چطور روی پنل سنایی (3x-ui) دقیقاً همین…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5736" target="_blank">📅 17:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">100 گیگ
بزار استفاده کنن
https://104.253.74.234/nNjCm8vkRvU47XqYLC/6c9ad098-0b86-4192-bcda-96239e9f2691/sub/?asn=MCI#F4</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5735" target="_blank">📅 17:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">output-addresses (11).txt</div>
  <div class="tg-doc-extra">18.4 KB</div>
</div>
<a href="https://t.me/archivetell/5734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۶۰ تا کانفیگ پشت کلودفلر
۲۰۰ گیگ اهدایی یکی از ممبرای عزیز
❤️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5734" target="_blank">📅 16:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://fcab8482-21d1-4c9d-a95a-9814a59eca27@snapp.ir:2086?encryption=none&host=dfssfddsfdfdfffddfdfjdfjdjfdfd.parscon.ir&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5733" target="_blank">📅 16:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎛
کالبدشکافی پنل سنایی (3x-ui)؛ نقشه راهنمای کامل برای بچه‌های آرشیوتل!  رفقای آرشیوتل سلام!
🌹
اگر به تازگی یه سرور خام گرفتید و پنل معروفِ سنایی (3x-ui) رو روش نصب کردید، احتمالاً همون اول با دیدن اون همه تب و منو یه مقدار گیج شدید. امروز اصلاً کاری به آموزش…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5732" target="_blank">📅 15:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
انتشار آپدیت بزرگ و جذاب پنل 3x-ui (نسخه v3.2.0)  ---  آپدیت جدید و پر از امکاناتِ پنل مدیریت سرور محبوب 3x-ui (نسخه سنایی) منتشر شد. این نسخه (v3.2.0) یکی از بزرگترین آپدیت‌های این پروژه است که تمرکز ویژه‌ای روی مدیریت گروهی کاربران، بهبود رابط کاربری و…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5731" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سایت خرید دامنه ارزون
👇
:
معرفی کنید دوستان
😂</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5730" target="_blank">📅 13:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">RIP
⚰
Reality?</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5729" target="_blank">📅 13:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvw8bI0WrRkgcjaf4Rr4SlLGYNkw2DEK7tP9NXXqnd7wISBK7dCgw-zaKLTq_ZX2Ik26eyBIuZE_fgNaNNtMPFZZCqlS_QyS7iIX05flh1ultwh9-GjQhGBJ5sMLwPyW_Dul-6rshcR6ARm8WDJqQp-B33bNNFCWY2j9BcnJ9QZGim4FC7sfvUMrlu8RVW_e8k-har3ymjSCsCFw7asXo6wdPP8BXUzUIC1ef3IMhbanRKJ6wSPc9KRX2KLvRhNeTG_nA4gcTZvB1hPVs8MFfbb8-esqqLWmyeXVL9maI30s_5VAin8fZ3kQ70OnpqghiYqDcyzKTGCTSj9IHKzEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15 گیگ   vless://38a80d5e-0d9f-4bd6-b6ec-836fd07c8223@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=be530c2769a1&sni=www.yahoo.com&spx=%2F9BvunqVqfGOOoPS&type=tcp#MOHRAZ-beeu61q6k5-15.00GB%F0%9F%93%8A…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5728" target="_blank">📅 12:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">15 گیگ
vless://38a80d5e-0d9f-4bd6-b6ec-836fd07c8223@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=be530c2769a1&sni=www.yahoo.com&spx=%2F9BvunqVqfGOOoPS&type=tcp#MOHRAZ-beeu61q6k5-15.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/5727" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5720" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رفقا سلام!
✋
امروز یک ابزار فوق‌العاده کاربردی با رابط کاربری ترمینال (TUI) به نام
SenPai Scanner
(آپدیت جدید v0.4.0) را معرفی می‌کنیم. این برنامه ابزاری است برای پیدا کردن IPهای Cloudflare که واقعاً با کانفیگ VLESS یا Trojan شما کار می‌کنند. این اسکنر مخصوصاً برای شبکه‌هایی طراحی شده که در آن‌ها پینگ غیرقابل پیش‌بینی است و اتصالات به طور ناگهانی قطع می‌شوند.
🔥
ویژگی‌های اصلی و تغییرات نسخه 0.4.0:
*
روند اسکن دو مرحله‌ای (Two Phases):
*
فاز ۱:
بررسی اتصالات اولیه با استفاده از تنظیمات استخراج شده از لینک کانفیگ شما شامل SNI، Host، Path و پورت. برای کانفیگ‌های WebSocket، زنده ماندن اتصال از طریق DPI نیز بررسی می‌شود.
*
فاز ۲:
اعتبارسنجی نهایی با اجرای یک هسته Xray داخلی انجام می‌شود. در این فاز سرعت دانلود واقعی (Mbps) و میزان تاخیر (TTFB) اندازه‌گیری می‌شود.
*
پشتیبانی از پورت‌های متنوع:
امکان انتخاب چند پورت مختلف (شامل پورت خود کانفیگ، 443, 8443, 2053, 2083, 2087, 2096) برای تست وجود دارد.
*
منبع آی‌پی‌ها:
می‌توانید از رنج آی‌پی‌های تصادفی Cloudflare استفاده کنید و یا لیست سفارشی خود را از طریق فایل
ips.txt
به برنامه بدهید.
*
خروجی‌گرفتن سریع:
پس از پایان فاز ۲، با فشردن کلید
c
، ترکیب IP و پورت‌های سالم (Working Endpoints) در کلیپ‌بورد کپی شده و مستقیماً در فایل
ips.txt
ذخیره می‌شوند.
*
تمرکز روی یک هدف:
در این آپدیت، منوهای اضافی حذف شده‌اند و برنامه مستقیماً روی گزینه
Find Working IPs
برای تست کانفیگ‌های شما تمرکز دارد.
💻
نحوه استفاده:
* پس از اجرای برنامه، با کلیدهای جهت‌نما در منوی اصلی گزینه
Find Working IPs
را انتخاب کنید.
* لینک کانفیگ
vless://
یا
trojan://
خود را Paste کنید.
* تعداد آی‌پی‌ها برای تست (Count)، تعداد Workerها (به‌طور پیش‌فرض 50 که برای شبکه‌های محدودشده امن است) و مقدار Timeout را تنظیم کرده و با فشردن Enter اسکن را شروع کنید.
📥
دانلود و نصب:
* این ابزار به صورت فایل‌های کامپایل‌شده (Pre-built binary) برای سیستم‌عامل‌های ویندوز (x86_64)، لینوکس (ARM64 و x86_64) و مک (Intel و Apple Silicon) در دسترس است.
* برای دریافت، کافی است به صفحه Releases پروژه در گیت‌هاب (MatinSenPai/SenPaiScanner) مراجعه کنید.
* همچنین برای نصب سریع در لینوکس و مک می‌توانید از این اسکریپت استفاده کنید:
curl -fsSL [https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh](https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh) | bash
.
📌
#معرفی_ابزار
#اسکنر
#کلادفلر
#ویندوز
#لینوکس
#مک
#SenPaiScanner
#Cloudflare
#VLESS
#Trojan
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5719" target="_blank">📅 10:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان ببینید این کانفیگ واستون پینگ میده....
vless://c3e49c34-1177-42d1-8c7a-1b1fb2e269fe@45.130.125.76:443?path=%2Fproxyip%3D109.61.110.202&security=tls&encryption=none&insecure=0&host=javad-3yb.pages.dev&fp=chrome&type=ws&allowInsecure=0&sni=javad-3yb.pages.dev#CF%E5%AE%98%E6%96%B9%E4%BC%98%E9%80%8913
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5718" target="_blank">📅 10:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">vless://df1ad808-d628-4bdc-90ce-8f6465392207@91.107.243.68:80?path=%2F&security=none&encryption=none&host=play.google.com&type=ws#sadra-%20hetzner-500.00GB%F0%9F%93%8A
با ایرانسل آورد با ایرانسل تست کنید
500gb</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5717" target="_blank">📅 10:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هوش مصنوعی برای دانشجوها
1.
perplexity.ai
➜ دستیار تحقیق
2.
hissab.io
➜ محاسبه هر چیزی
3.
otter.ai
➜ خودکارسازی یادداشت‌های سخنرانی
4.
stepwisemath.ai
➜ معلم ریاضی
5.
scholarcy.com
➜ خلاصه‌کننده مقاله
6.
caktus.ai
➜ ابزار مطالعه
7.
bookai.chat
➜ چت با کتاب‌ها
8.
chatdoc.com
➜ چت با اسناد
9.
textero.ai
➜ تولیدکننده مقاله
10.
jenni.ai
➜ نوشتن مقالات تحقیقاتی
11.
tome.app
➜ تولیدکننده ارائه
12.
plaito.ai
➜ معلم خصوصی
13.
heyscience.ai
➜ دستیار تحقیقات علمی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5716" target="_blank">📅 08:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://99a7d8e7-f588-4d1f-a2c5-30cc94626c21@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=de50a62ae9c03b&sni=www.yahoo.com&type=tcp#MOHRAZ-y28qfr8zv1-20.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5715" target="_blank">📅 08:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu69qhVKqz8oQuyKiFAvTcgl9OX6cTqmM3WXY6TIaAbrxkfP3-J0JtiqFQCeg5kFOMyibQWxFCIKFiyuV6zkcsMle0PUV40dYwp9718NpdtjYExK4Q_AD-pUxnxwDpCk_vBOqliEJVdvEwXFLRNelcvJ7GkRBvifjCXCzw50wpiYh8OLdnBl_ojvSu5ItLIRTq1KwEbh6vqRCEb7_aKa0fr-lBJ6SE02zh31-Zd_TBao8Y4zrZrtlDvKzt_amjFxnSggQw9sbaIXU3VWe2gNq6glL-eNgjWpV5m2092xHS5kI8tWXgsJN0t4rZ9a4w66HT2me1iOCrK6gYZ7lNJDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SNI-Spofing----Plan B
coming soon
🔜
گویا پترنیها رو یک متود جدید کار می‌کنه که به راحتی میتونید فیلترینگ رو دور بزنید ..
اگه منتشر شد
آموزش رو واستون میزاریم...
❤️
@archivetell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5714" target="_blank">📅 04:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عه
رکب خوردی مشتی.....
🫵
😂
به جاش براتون آی‌پی تمیز کلود آوردم...
45.130.125.160
@archivetell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5713" target="_blank">📅 04:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانفیگ های
🇺🇸
🇳🇱
vless://4c5ec35b-d2aa-49be-a596-77c956aa40e9@31.57.63.70:12530?security=reality&encryption=none&pbk=odlIn9uuty8SSCafs7Dpka-jRTTUpiuJUuotikQU1i8&headerType=&fp=chrome&spx=%2FqlF7U3tRy88uURE&type=tcp&sni=www.yahoo.com&sid=dc6ed267aee4#5%DA%AF%DB%8C%DA%AF-5.00GB%F0%9F%93%8A
@archivetell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5711" target="_blank">📅 02:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy1s8K9Yy6YhHOBlPPUPaxcGO3H4lNiwd0OuFaHzP0-2HUDtXMqenJhrmVJL80wa-YA0CXtDPWMdENzKIadjMKNHYkSa6jjEkvmVaWDyiQao6pEtgMvbNpEHLhnCNNmcGXsjuDviM0ux-P6jvZoJ7L1rua9_Od1PT97CUwBf5fazVRK6TQlFZ6FqF5VTmZeAUcfmPMAt7GMnpF2brwG3uHmIzmKw3zLQjWwUTb6xSPz-pEoyUnUZf4pY802Kkl7kHjcfLYoh_GFgC8pMSpTK_wYqOVu3RiG6pPDVtNP2lkihblXKFEaJGv9ldWdubWhDlyBJWEKMUOPST0r0bcp_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5709" target="_blank">📅 02:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
آموزش اتصال پایدار سایفون با دامنه‌های فستلی (Fastly)
---
رفقا
خبر خوب اینه که در حال حاضر روی شبکه فستلی (Fastly) خیلی از سایت‌ها باز شدن و می‌تونید از همین فرصت طلایی برای اتصال پایدار سایفون استفاده کنید!
این روش روی اپلیکیشن‌های
شیر و خورشید (ShiroKhorshid)
و
مهسا ان‌جی (MahsaNG)
در اندروید، و کلاینت
Se7en Pro
در ویندوز (یا کانفیگ‌های MitM+Psiphon) به خوبی جواب میده.
*(طبق تست‌های انجام شده، MahsaNG تو این متد اتصال بهتر و سریع‌تری نسبت به شیر و خورشید داره).*
###
🛠
آموزش تنظیمات:
۱. ابتدا یکی از دامنه‌های سفید زیر که پشت فستلی هستند رو انتخاب کنید (به عنوان SNI):
🔸
github.githubassets.com
🔸
docs.github.com
🔸
www.fastly.com
🔸
pypi.org
🔸
repo.almalinux.org
۲. حالا باید از دامنه‌ای که انتخاب کردید پینگ (Ping) بگیرید تا آی‌پی (IP) اون رو به دست بیارید.
⚠️
نکته بسیار مهم:
آی‌پی و SNI باید حتماً با هم مچ باشن! یعنی هر SNI که از لیست بالا انتخاب کردید، باید دقیقاً آی‌پیِ همون دامنه رو تو برنامه وارد کنید.
۳. تنظیمات برنامه رو دقیقاً روی این حالت‌ها قرار بدید:
🔹
Mode:
psiphon only
🔹
Protocol:
cdn_fronting
🔹
IP & SNI:
(آی‌پی و دامنه‌ای که در مراحل قبل پیدا کردید رو وارد کنید).
💡
وضعیت سرعت و پایداری:
به دلیل محدودیت‌های خود سایفون و تعداد بالای کاربران، سرعت این روش در حد متوسط (پخش یوتیوب با کیفیت 480p) هست؛ اما نقطه قوتش اینه که
کاملاً پایدار و بدون قطعی
کار می‌کنه و برای زمان‌های اختلال شدید، یه نجات‌دهنده عالیه.
📌
#فستلی
#Fastly
#سایفون
#مهسا_ان_جی
#MahsaNG
#شیر_و_خورشید
#Se7enPro
#CDN_Fronting
#آموزش
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5708" target="_blank">📅 01:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5707">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">5 گیگ کانفیگ اهدایی از سرور آمریکا..
🇺🇸
vless://9a93ccb9-c010-417d-afec-b62ed1246ca7@31.57.63.70:12530?encryption=none&fp=chrome&pbk=odlIn9uuty8SSCafs7Dpka-jRTTUpiuJUuotikQU1i8&security=reality&sid=9a1fb502&sni=www.yahoo.com&spx=%2FoCtZeR0TiaFYTed&type=tcp#5%DA%AF%DB%8C%DA%AF-4.95GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5707" target="_blank">📅 01:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:
* پشتیبانی همزمان از پروتکل‌های VLESS، Trojan و xhttp.
* پنل گرافیکی قدرتمند: مدیریت کانفیگ‌ها تحت وب با دیتابیس KV (اعمال تغییرات در لحظه بدون نیاز به دیپلوی مجدد).
* Sub-converter داخلی: تولید کانفیگ کلاینت‌ها (Clash, Sing-box, V2rayNG و...) بدون نیاز به سرویس خارجی.
* پشتیبانی از ECH: دور زدن محدودیت‌های پیشرفته.
* تست پینگ داخلی: تست و انتخاب خودکار بهترین آی‌پی‌ها.
* پشتیبانی از رابط کاربری فارسی.
🛠
پیش‌نیازها:
یک اکانت کلادفلر + ساخت یک UUID معتبر از سایت
https://www.uuidgenerator.net
(این UUID رمز ورود شما به پنل خواهد بود).
💻
نصب روی Cloudflare Workers:
1. ساخت KV: در کلادفلر، از Storage ➔ KV یک Namespace جدید بسازید.
2. ایجاد Worker: در Workers & Pages یک ورکر جدید بسازید، کدهای قبلی را پاک و سورس CFnew را از گیت‌هاب پیست کنید (Deploy بزنید).
3. تنظیم متغیرها: در Settings ➔ Variables، متغیری با نام U (حرف بزرگ) بسازید و مقدارش را UUID خود قرار دهید.
4. اتصال KV: در Settings ➔ KV Bindings، دیتابیسی که ساختید را با نام C (حرف بزرگ) متصل (Bind) کنید.
5. تاریخ سازگاری: در Settings ➔ Runtime، گزینه Compatibility Date را روی 2026-01-20 تنظیم و ذخیره کنید.
6. اتصال دامنه: در Triggers ➔ Custom Domains، دامنه خود را متصل کنید.
🌐
نصب روی Cloudflare Pages:
1. آپلود فایل‌ها: در Workers & Pages یک Pages ایجاد کنید. با گزینه Direct Upload، فایل Zip پروژه را آپلود کنید.
2. تنظیمات: مشابه روش قبل، در Settings متغیر U (برای UUID) را ساخته و KV Bindings را با نام C متصل کنید.
3. تاریخ سازگاری: در Settings ➔ Runtime، تاریخ را روی 2026-01-20 تنظیم کنید.
4. دیپلوی مجدد (حیاتی): چون متغیرها فوراً اعمال نمیشن، به تب Deployments رفته، Create deployment را بزنید و همان فایل Zip را دوباره آپلود کنید تا پروژه از نو ساخته شود.
🔓
نحوه دسترسی به پنل مدیریت:
مرورگر را باز کرده و آدرس دامنه خود را به همراه UUID وارد کنید (مثال:
yourdomain.com/UUID
). در این پنل گرافیکی و فارسی، می‌توانید لینک‌های اتصال (Subs) بگیرید، ECH را مدیریت کنید و آی‌پی‌های تمیز وارد کنید.
🔄
نحوه آپدیت برای نسخه‌های بعدی:
* اگر از Worker استفاده می‌کنید: کدهای جدید را کپی، جایگزین کدهای قبلی کرده و Deploy کنید.
* اگر از Pages استفاده می‌کنید: در تب Deployments فایل Zip جدید را آپلود کنید (بدون نیاز به تنظیم مجدد).
📥
سورس کد و دانلود زیپ:
https://github.com/byJoey/cfnew
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5704" target="_blank">📅 01:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">20 گیگ کانفیگ لوکیشن آمریکا...
🇺🇸
vless://d08a3998-d155-4541-9d46-85014b182ee8@45.39.230.25:42391?encryption=none&fp=chrome&pbk=vWLA2Hvig6fUErrisZvXBRs9ioeqegs_xmGkZf1uZ04&security=reality&sid=1608&sni=www.yahoo.com&spx=%2Fa91vwk8Tl6f5E3g&type=tcp#20%DA%AF%DB%8C%DA%AF-20.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5703" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://acd15093-fc20-418e-aeb6-e500d0509255@snapp.ir:8443?alpn=h2%2Chttp%2F1.1&encryption=none&host=shop.nex1shield.shop&path=%2F&security=tls&sni=shop.nex1shield.shop&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5702" target="_blank">📅 23:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEkKPV-EEW4xdhrD4G2enz5mgqKS0g84YQW1sTIHUfbiOgw5P6xDjtNxu56w0M9Sx8ET-mxIbYrPvLRqO9kiMg7PXNf0jSQ10MIwPIEUIMgOyT6WyNfuQriQRBZ_08v6gb39rOTPwxqcw0vMCHbBcr-q1suNdAAr7i-GWbNdPtmJPPVXy_SWAPac6G-pG9k7FrxR6Vxa9etDmTNmv8k6yKVyjaawcdyq7uYmSY52xNKal45a5H6STzQxEBkiFFru3FxWsnv_T9nC70OMxlu41EYWpHjayLoNLMMnnRHAyWa19A3s8-9P5rI2B3Igug6V3hkPnJZR3PZ2crfDo0kDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SolveCaptcha
توسعه‌دهندگان راهی برای خودکار سازی عبور از کپچا پیدا کردند
چه چیزهایی پشتیبانی می‌شود:
🕤
reCAPTCHA v2/v3
🕤
Cloudflare Turnstile
🕤
FunCaptcha (Arkose Labs)
🕤
GeeTest و GeeTest v4
🕤
Amazon WAF و KeyCaptcha
🕤
Grid، Rotate، Canvas، ClickCaptcha
🕤
کپچاهای متنی، گرافیکی و صوتی معمولی
https://github.com/solvercaptcha/solvecaptcha-python
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5701" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">output-addresses (11).txt</div>
  <div class="tg-doc-extra">18.4 KB</div>
</div>
<a href="https://t.me/archivetell/5700" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۶۰ تا کانفیگ پشت کلودفلر
اهدایی یکی از ممبرای عزیز
❤️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5700" target="_blank">📅 21:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://2fd687a6-7b5f-491e-a7ff-a885da5504b1@se.sanaz.online:20609?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=2KojHs3QuIDI9X3HpOwIvEIhMy-54DLblBADeCuzlkU&security=reality&sid=0fe6d3442590&sni=www.yahoo.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5699" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دریافت هوش مصنوعی Anything — ۲۰ هزار اعتبار رایگان
🚀
دسترسی به برترین مدل‌های هوش مصنوعی در یک پلتفرم:
*
GPT-5.5
*
Claude Opus 4.7
*
Gemini 3.1 Pro
*
Kimi K2.6
نحوه دریافت:
* اینجا ثبت‌نام کنید:
Anything.com
* برای فعال‌سازی اعتبار رایگان خود از لینک زیر استفاده کنید
* دریافت از اینجا :
https://www.anything.com/signup?utmsource=promo&utmmedium=free-credit&utmcampaign=anythingplaystorelaunch&dubid=znvE3L0a0X3pl4Jz&promo=anythingplaystorelaunch
لذت ببرید
🎉
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5697" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۲۵ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
❤️
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1REpYUnBtaTNpeXF4UTc5UGZLdjNC@195.93.253.240:14130#The%20Netherlands
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5694" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استفاده از Claude Opus 4.8 به صورت رایگان
👀
یک پلتفرم به نام Genspark AI به شما اجازه می‌دهد به بیش از ۱۵ مدل برتر هوش مصنوعی در یکجا دسترسی داشته باشید، از جمله
Claude Opus 4.8
GPT-5.5
Gemini 3.1 Pro
Grok 4
ثبت‌نام کنید، نیازی به کارت اعتباری نیست، روزانه ۱۰۰ اعتبار دریافت می‌کنید که هر ۲۴ ساعت تازه می‌شود.
فقط Claude Opus 4.8 در Anthropic ماهانه ۱۰۰ دلار هزینه دارد. اینجا آن را به همراه ۱۴ مدل دیگر رایگان دریافت می‌کنید.
واقعاً یکی از بهترین مجموعه‌های رایگان هوش مصنوعی موجود در حال حاضر است.
🔗
https://genspark.ai
@ArchiveTell
#AITools
#FreeAI</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5693" target="_blank">📅 18:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
❤️
vless://b0785d2e-33cc-48b2-91d6-e1ed431fd849@panel.homan554.ir:45868?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=nyX6hzFp1vfyL5oPYp7Zpgn5jR5kZ_lTUN-wyx-YBG8&security=reality&sid=72&sni=github.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5692" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به به حلوا و شیرینی
☕
🧁
ss://cmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg@146.70.61.37:8080#ArchiveTell%20%F0%9F%87%AC%F0%9F%87%A7</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5691" target="_blank">📅 18:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📌
فهرست جامع و راهنمای جستجوی مطالب کانال (آرشیو ابزارها و آموزش‌ها)
📱
۱. کلاینت‌ها، اپلیکیشن‌ها و ابزارهای اتصال
جدیدترین نسخه‌های برنامه‌های اتصال به همراه ابزارهای اختصاصی دور زدن نت ملی:
*
شیر و خورشید (ShiroKhorshid) / Se7enPro:
کلاینت‌های اختصاصی سایفون (اندروید و ویندوز) با قابلیت CDN Fronting. ➔
#شیر_و_خورشید
#Se7enPro
#سایفون
*
خانواده V2ray:
کلاینت‌های محبوب v2rayNG (نسخه‌های 2.1.7 و 2.1.8) برای اندروید و V2rayN برای ویندوز. ➔
#v2rayNG
#v2rayN
#v2ray
*
مهسا ان‌جی (MahsaNG):
نسخه v16 با قابلیت اتصال مستقل سایفون و دامین فرانتینگ. ➔
#MahsaNG
#مهسا_ان_جی
*
متد رله گوگل (mhrv-rs / MasterHttpRelayVPN):
کلاینت اتصال از طریق رله گوگل با زبان Rust و پایتون. ➔
#mhrv_rs
#MHRV
#رله_گوگل
*
اسکیرک (Skirk):
ابزار فوق‌العاده تونل کردن ترافیک از طریق Google Drive. ➔
#Skirk
#اسکیرک
#گوگل_درایو
*
زیرلن (Zyrln):
عبور از فیلترینگ با ترافیک ابری گوگل و کلادفلر ورکر. ➔
#Zyrln
#زیرلن
*
نوا پروکسی (NovaProxy):
پروکسی دسکتاپ با ترکیب Google Apps Script و Cloudflare. ➔
#نوا_پروکسی
#NovaProxy
*
بله وی‌پی‌ان (BaleVPN) و Whitelist Bypass:
تونل کردن اینترنت از طریق تماس صوتی/تصویری پیام‌رسان بله. ➔
#BaleVPN
#Whitelist_Bypass
#بله_میت
*
چشم عقاب (Eagle Eye):
دریافت آفلاین کانفیگ از طریق فرکانس شبکه‌های ماهواره‌ای. ➔
#چشم_عقاب
#Eagle_Eye
#آفلاین
*
کلاینت‌های iOS (آیفون):
برنامه‌های NexaTunnel و TheFeed (نسخه TestFlight). ➔
#NexaTunnel
#TheFeed
#آیفون
#iOS
*
سایر کلاینت‌ها و ابزارها:
NekoBox، V2box، Slipnet، MasterDns، OpenVPN، Happ، TunnelForge، HashemVasel و ابزار کلاینت لینوکسی XuiFactor. ➔ (اسم برنامه را سرچ کنید) یا
#کلاینت
#ابزار
🛠
۲. آموزش‌های طلایی و متدهای عبور از فیلترینگ
آموزش‌های قدم‌به‌قدم برای راه‌اندازی متدهای جدید:
*
متد SNI Spoofing:
آموزش دور زدن فیلترینگ با تزریق دامنه فیک (مثل hCaptcha) برای ویندوز (RM SNI Spoofer / Cloak)، لینوکس (FakeSNI)، و اندروید به همراه آموزش راه‌اندازی روی سرور ایران با پنل 3x-ui. ➔
#SNI_Spoofing
#FakeSNI
#اسپوف
#Cloak
*
آموزش‌های نتلیفای (Netlify) و ورسل (Vercel):
دیپلوی کانفیگ XHTTP، تغییر دامنه نتلیفای با کلادفلر ورکر برای رفع مسدودی، و اسکریپت XHTTP-Installer. ➔
#نتلیفای
#Netlify
#ورسل
#Vercel
#XHTTP
*
ترکیب سایفون و MitM:
آموزش متد Patterniha با گرفتن سرتیفیکیت (SSL) برای دور زدن DPI. ➔
#سایفون
#MitM
#سرتیفیکیت
*
اشتراک‌گذاری اینترنت آزاد (Hotspot/LAN):
آموزش انتقال اینترنت بدون فیلتر سیستم (V2ray یا SNI Spoof) به گوشی موبایل یا برعکس با برنامه‌های PdaNet+ و تنظیمات LAN/Proxy. ➔
#هات_اسپات
#LAN
#اشتراک_نت
#PdaNet
*
گیمینگ و پینگ پایین:
آموزش اتصال ویندسکرایب (Windscribe) روی SNI Spoofing برای کاهش پینگ در بازی‌ها. ➔
#گیمینگ
#پینگ
#Windscribe
#وینداسکرایب
*
لینوکس و ترمینال:
آموزش تونل کردن ترافیک ترمینال لینوکس با ابزار Proxychains4. ➔
#لینوکس
#Proxychains4
🔍
۳. اسکنرها و ابزارهای پیدا کردن آی‌پی (IP/SNI Scanners)
ابزارهای اختصاصی برای پیدا کردن آی‌پی‌های تمیز آکامای (Akamai) و فستلی (Fastly):
*
نتورک چکر (Network Checker):
اپلیکیشن همه‌کاره اندروید (v0.6.0) مجهز به اسکنر آکامای و کانفیگ‌ساز نتلیفای. ➔
#نتورک_چکر
#Network_Checker
*
اسکنرهای تحت وب و ویندوز:
CDN IP Finder (نسخه مرورگر)، AniScanner (داشبورد گرافیکی وب)، SNI-Radar و ابزارهای اسکن Akamai با PowerShell و Python. ➔
#اسکنر
#CDN_IP_Finder
#AniScanner
#اسکنر_آی_پی
*
لیست آی‌پی‌های آماده:
برای دسترسی به لیست‌های پینگ‌گرفته شده اپراتورها (ایرانسل، همراه اول، مخابرات، رایتل و سامانتل). ➔
#آی_پی_تمیز
#آکامای
#لیست_آی_پی
🤖
۴. ابزارها، اسکریپت‌ها و پروژه‌های خاص
ترفندها و ابزارهای کاربردی برای کارهای روزمره:
*
دانلودرها و ربات‌ها:
PlayDL (دانلود مستقیم از گوگل‌پلی)، MattDownloader (دانلودر با GitHub Actions) و ربات‌های هوش مصنوعی (Gemini, Claude, ChatGPT). ➔
#دانلودر
#PlayDL
#هوش_مصنوعی
#ربات
*
ایزی‌تل (EzyTel / Telemirror):
خواندن محتوای تلگرام به صورت آفلاین از طریق زیرساخت Google Translate. ➔
#ایزی_تل
#EzyTel
#تلگرام_آفلاین
*
سایر ترفندها:
ساخت شورت‌کات در Termux، مسدودساز آپدیت ویندوز (Windows Update Blocker)، ابزار Netlify obfuscator و مدیریت پروژه در VSCode. ➔
#ترموکس
#ترفند
#ویندوز</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5688" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
معرفی olcNG: فیلترشکن سریع، ساده و بهینه‌شده برای اندروید
---
رفقا سلام!
✋
امروز می‌خوایم یک اپلیکیشن بسیار جذاب و کاربردی به اسم
olcNG
رو بهتون معرفی کنیم. این برنامه در واقع یک نسخه (Fork) اوپن‌سورس و بهینه‌شده از اپلیکیشن محبوب
v2rayNG
هست که توسط تیم OpenLibreCommunity توسعه داده شده.
اگر از شلوغی و پیچیدگی‌های v2rayNG خسته شدید و دنبال یک جایگزین سریع‌تر، ساده‌تر و البته امن می‌گردید، olcNG دقیقاً همون چیزیه که بهش نیاز دارید!
###
✨
چرا olcNG رو پیشنهاد می‌کنیم؟
🔸
هسته (Core) فوق‌العاده قوی:
این اپلیکیشن برای مدیریت ترافیک و پردازش کانفیگ‌ها، از Xray-core و ماژول‌های قدرتمند
AndroidLibXrayLite
و
hev-socks5-tunnel
استفاده می‌کنه که باعث کاهش پینگ و افزایش چشمگیر سرعت اتصال میشه.
🔸
پشتیبانی کامل از تمامی پروتکل‌ها:
هر کانفیگی که در v2rayNG استفاده می‌کنید (مثل VLESS ،VMess ،Trojan و ShadowSocks)، بدون هیچ مشکلی در این برنامه قابل اجراست.
🔸
رابط کاربری (UI) بهینه‌شده:
برخلاف نسخه‌های اصلی که ممکنه برای کاربران عادی گیج‌کننده باشن، olcNG با یک طراحی بسیار ساده، سبک و کاربرپسند ارائه شده.
🔸
منبع باز و کاملاً رایگان (Open-Source):
این اپلیکیشن تحت لیسانس GPL-3.0 در گیت‌هاب منتشر شده که یعنی هیچ کد مخرب یا جاسوسی‌ای در اون وجود نداره و امنیتش تضمین شده است.
---
###
💻
دانلود و نصب:
نسخه جدید این اپلیکیشن (v4.2.1) به تازگی منتشر شده و با اندرویدهای جدید کاملاً سازگاری داره. برای دانلود مستقیم نسخه رسمی، می‌تونید از لینک گیت‌هاب پروژه استفاده کنید:
🔗
لینک دانلود مستقیم از گیت‌هاب:
🌐
https://github.com/openlibrecommunity/olcng/releases/tag/v4.2.1
*(در صفحه باز شده، روی فایلِ با پسوند
.apk
کلیک کنید تا دانلود شروع شود).*
🔗
سایت رسمی پروژه:
zarazaex.xyz
📌
#معرفی_اپلیکیشن
#اندروید
#فیلترشکن
#olcNG
#v2rayNG
#Xray
#VLESS
#Bypass
#Vpn
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5687" target="_blank">📅 16:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
این سایت یه معدن طلایِ هوش مصنوعیه: از ساخت حرفه‌ای‌ترین پرامپت‌ها تا ویرایش عکس و ساخت موزیک رایگان!
---
اگر از ChatGPT یا Claude استفاده می‌کنید اما خروجی‌های دقیقی نمی‌گیرید، یا دنبال ابزارهای رایگان برای تولید محتوا هستید، سایت
The Prompt Index
همون چیزیه که بهش نیاز دارید. این سایت فقط یک پرامپت‌ساز نیست، بلکه یک "جعبه‌ابزارِ دیوانه‌کننده" است که امکانات پولی ده‌ها سایت مختلف رو یکجا و رایگان جمع کرده!
کافیه یک
اکانت کاملاً
رایگان
(0$)
بسازید تا به این گنجینه دسترسی پیدا کنید:
📝
۱. ماشین جادویی پرامپت‌سازی (Prompt Generator)
با این ابزار، کیفیت جواب‌هایی که از هوش مصنوعی می‌گیرید ۱۰ برابر بهتر میشه!
🔸
دارای ۲۲۸ فریم‌ورک استاندارد در ۲۵ دسته‌بندی مختلف (از برنامه‌نویسی تا حل مسئله).
🔸
حالت مبتدی (Wizard):
فقط با جواب دادن به ۴ سوال ساده، حرفه‌ای‌ترین دستور رو براتون می‌نویسه.
🔸
حالت حرفه‌ای (Expert):
امکان ترکیب قالب‌ها برای کارهای فوق‌تخصصی.
🎁
۲. سوئیت ابزارهای رایگان (AI Toolbox)
🎵
موزیک و صدا:
ساخت ۲ ترک موسیقی در روز، ۵۰ دقیقه تغییر صدای هوش مصنوعی در ماه و ساخت ۱۰ افکت صوتی روزانه!
🖼
ویرایش تصویر حرفه‌ای:
افزایش کیفیت عکس (Upscaler)، حذف پس‌زمینه و واترمارک، ترمیم و گسترش ابعاد عکس (هر کدوم ۱ تا ۲ بار رایگان در روز).
📚
کتاب‌ساز و نویسندگی:
ابزار PromptBook برای ساخت یک کتاب کامل به همراه عکس جلد در ماه، ابزار Humanizer (انسانی‌سازی متن برای دور زدن ربات‌ها) و استخراج متن از PDF.
💡
نتیجه‌گیری:
پیدا کردن سایتی که مجموعه‌ای از بهترین ابزارهای موسیقی، تصویر، متن و پرامپت‌نویسی رو یکجا و رایگان در اختیارتون بذاره واقعاً غنیمته. حتماً سیوش کنید که به کارتون میاد!
🔗
لینک ورود و استفاده از ابزارها:
🌐
https://www.thepromptindex.com/
📌
#هوش_مصنوعی
#پرامپت
#ابزار_کاربردی
#تولید_محتوا
#ویرایش_عکس
#ساخت_موزیک
#کتاب_ساز
#AI
#رایگان
#پرامپت_نویسی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5686" target="_blank">📅 14:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
آموزش ساخت امن‌ترین کانفیگ‌های VLESS REALITY (پروتکل غیرقابل فیلتر!)
---
رفقا سلام!
✋
خیلی‌هاتون پرسیدید این کانفیگ‌های قدرتمندی که براتون می‌ذاریم دقیقاً چطوری ساخته میشن؟
امروز می‌خوایم قدم‌به‌قدم بهتون یاد بدیم چطور روی پنل
سنایی (3x-ui)
دقیقاً همین کانفیگ‌های فوق‌امنیتی رو برای خودتون بسازید!
🛠
مراحل ساخت کانفیگ:
۱. تنظیمات پایه (Basic Settings):
بعد از ورود به پنل، یه Inbound جدید بسازید:
🔸
پروتکل (Protocol):
روی
vless
قرار بدید.
🔸
پورت (Port):
ترجیحاً
443
(یا پورت‌های آزاد سرورتون) باشه.
۲. تنظیمات شبکه (Network):
🔹
بخش
Network:
روی
tcp
باشه.
🔹
تیک
Reality
رو حتماً روشن کنید تا تنظیماتش باز بشه.
۳. تنظیمات استتار (Reality Settings) - مهم‌ترین بخش:
حالا باید ترافیکمون رو پشت یک سایت معروف مخفی کنیم:
🔸
در کادر
dest:
آدرس یک سایتِ بدون فیلتر رو با پورت ۴۴۳ بنویسید (مثلاً
www.microsoft.com:443
).
🔸
در کادر
serverNames:
همون سایت رو بدون پورت وارد کنید (مثلاً
www.microsoft.com
).
🔸
روی دکمه
Generate
کلیک کنید تا کلیدهای رمزنگاری (Private Key) و کدهای کوتاه (ShortIds) به صورت خودکار براتون ساخته بشن.
۴. ساخت کاربر و فعال‌سازی Vision:
حالا برید پایینِ صفحه تو بخش Clients و روی
+ Add
کلیک کنید:
🔹
ایمیل (ID):
یه اسم دلخواه برای کانفیگ بذارید.
🔹
⚠️
نکته طلایی:
در قسمت
Flow
، حتماً گزینه
xtls-rprx-vision
رو انتخاب کنید (این همون جادوییه که باعث دور زدن سیستم فیلترینگ و کاهش چشمگیر پینگ میشه).
✅
ذخیره و استفاده:
دکمه Save رو بزنید! تمام شد!
حالا روی آیکون QR Code کلیک کنید و لینک کانفیگتون رو کپی کنید. اگر به لینک دقت کنید، می‌بینید که دقیقاً همون ساختار حرفه‌ایِ Vless Reality رو داره. کانفیگ رو تو v2rayNG یا NekoBox کپی کنید و از اینترنت آزاد لذت ببرید!
✌️
📌
#آموزش
#فیلترشکن
#سرور
#پنل_سنایی
#VLESS
#Reality
#Vision
#کانفیگ
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/archivetell/5685" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
معرفی پنل PasarGuard: نسل جدید و قدرتمند مدیریت پروکسی و ضدسانسور
---
امروز قصد دارم یک پنل مدیریت سرورِ بسیار مدرن، جامع و قدرتمند به اسم
PasarGuard
رو بهتون معرفی کنم. این پنل با زبان‌های Python و React.js نوشته شده و با ترکیب Xray-core و WireGuard، یک رابط کاربری بی‌نظیر برای مدیریت صدها اکانت به صورت همزمان به شما میده.
اگر دنبال یک پنل حرفه‌ای با امکانات توزیع‌شده (Multi-Node) هستید، پاسارگارد یکی از بهترین انتخاب‌هاست!
✨
مهم‌ترین ویژگی‌های پنل PasarGuard:
🔸
پشتیبانی کامل از مدرن‌ترین پروتکل‌ها:
پشتیبانی از Vmess ،VLESS ،Trojan ،Shadowsocks ،WireGuard و Hysteria2 به همراه قابلیت‌های TLS و REALITY.
🔸
مدیریت پیشرفته کاربران:
امکان استفاده از یک کاربر برای چندین پروتکل، پشتیبانی از چند کاربر روی یک اینباند، و تعریف فال‌بک (Fallbacks).
🔸
محدودیت‌های هوشمند:
قابلیت تنظیم محدودیت حجم و زمان، و همچنین
محدودیت‌های دوره‌ای
(ریست شدن حجم به صورت روزانه، هفتگی و...).
🔸
سابسکریپشن استاندارد:
تولید لینک سابِ کاملاً سازگار با کلاینت‌های V2ray ،Clash و ClashMeta به همراه تولید خودکار QR Code.
🔸
امکانات جانبی قدرتمند:
دارای ربات تلگرامی اختصاصی، محیط خط فرمان (CLI)، دیتابیس‌های متنوع، API کامل و مانیتورینگ دقیق ترافیک.
---
💻
آموزش نصب سریع (روی لینوکس):
توسعه‌دهندگان، استفاده از دیتابیس
TimescaleDB
رو برای این پنل پیشنهاد دادن. کافیه به سرور متصل بشید و دستور زیر رو کپی و اجرا کنید:
curl -fsSL [https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh](https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh) -o /tmp/pg.sh \\
&& sudo bash /tmp/pg.sh install --database timescaledb
پس از پایان نصب، برای ساخت نام کاربری و رمز عبورِ مدیر (Admin)، دستور زیر رو وارد کنید (به جای
<username>
نام دلخواهتون رو بنویسید):
pasarguard cli admins --create <username>
🌐
نحوه ورود به پنل:
پنل روی پورت
8000
اجرا میشه و برای ورود به آدرس
https://YOUR_DOMAIN:8000/dashboard
نیاز دارید. *(نکته مهم: برای امنیت بیشتر، پنل پاسارگارد الزاماً به سرتیفیکیت SSL و اتصال HTTPS نیاز دارد).*
🔗
لینک گیت‌هاب پروژه برای اطلاعات بیشتر:
🌐
https://github.com/PasarGuard/panel
📌
#معرفی_ابزار
#پنل
#PasarGuard
#پاسارگارد
#فیلترشکن
#سرور
#Xray
#VLESS
#Hysteria2
#Wireguard
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/archivetell/5684" target="_blank">📅 03:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
انتشار آپدیت بزرگ و جذاب پنل 3x-ui (نسخه v3.2.0)
---
آپدیت جدید و پر از امکاناتِ پنل مدیریت سرور محبوب
3x-ui
(نسخه سنایی) منتشر شد. این نسخه (v3.2.0) یکی از بزرگترین آپدیت‌های این پروژه است که تمرکز ویژه‌ای روی مدیریت گروهی کاربران، بهبود رابط کاربری و ارتقای پروتکل‌های دور زدن فیلترینگ داشته.
###
✨
مهم‌ترین تغییرات و قابلیت‌های جدید:
🔸
مدیریت حرفه‌ای گروه‌ها:
اضافه شدن صفحه اختصاصی برای گروه‌بندی کلاینت‌ها (Client Groups) و امکان خروجی گرفتن لینک سابسکریپشن مجزا برای هر گروه.
🔸
پشتیبانی از XHTTP پیشرفته:
اضافه شدن تنظیمات حرفه‌ای XHTTP و پروکسی‌های خارجی TLS (قابلیت بسیار مهم برای شرایط فعلی فیلترینگ).
🔸
عملیات گروهی کلاینت‌ها (Bulk Actions):
امکان اضافه، حذف، انتقال و تخصیص گروه به کلاینت‌ها به صورت دسته‌جمعی.
🔸
فیلترهای پیشرفته:
اضافه شدن دراور (Drawer) فیلتر جدید برای پیدا کردن سریع کلاینت‌ها بر اساس حجم مصرفی، تاریخ انقضا، پروتکل و وضعیت اتصال.
🔸
امنیت و بهینه‌سازی دیتابیس:
اختصاص Role رندوم برای دیتابیس PostgreSQL جهت امنیت بیشتر و بهینه‌سازی استخر اتصالات (Pool Tuning) برای جلوگیری از افت منابع سرور.
🔸
ارتقای پروتکل‌ها:
اضافه شدن قابلیت Salamander auto-seed برای پروتکل Hysteria و قرار گرفتن فیلد Testseed برای VLESS Vision.
🔸
بهبود رابط کاربری:
بازنویسی و مدرن‌سازی کامل فرانت‌اند پنل با TypeScript و اضافه شدن داکیومنت‌های API به داخل خود پنل.
###
🛠
مهم‌ترین باگ‌های برطرف‌شده:
🔹
حل مشکل قرار نگرفتن SNI در لینک‌های اشتراک‌گذاری REALITY.
🔹
حفظ انکودینگ صحیحِ اطلاعات کاربران در لینک‌های Trojan، ShadowSocks و Hysteria.
🔹
رفع مشکل تداخل External-proxy با SNI در اتصال‌های TLS.
---
💻
نحوه آپدیت:
برای آپدیت به این نسخه، کافیه به سرورتون SSH بزنید، دستور
x-ui
رو در ترمینال وارد کنید و از منوی باز شده، گزینه آپدیت به آخرین نسخه رو انتخاب کنید.
🔗
مشاهده لیست کامل تغییرات در گیت‌هاب:
🌐
https://github.com/MHSanaei/3x-ui/releases/tag/v3.2.0
📌
#آپدیت
#پنل
#سنایی
#فیلترشکن
#سرور
#Xray
#VLESS
#XHTTP
#Hysteria
#مدیریت_سرور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5683" target="_blank">📅 03:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)  ---  رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5682" target="_blank">📅 02:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)
---
رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو روی یک سرور مجازی (اوبونتو 22.04 یا 24.04) آموزش می‌دیم:
۱. آپدیت سرور و نصب پیش‌نیازها
ابتدا به سرور خود متصل شده و دستورات زیر را کپی و اجرا کنید:
sudo apt update && sudo apt upgrade -y
sudo apt install curl wget ufw fail2ban -y
۲. نصب Hysteria 2
با اجرای دستور زیر، پروتکل به صورت خودکار نصب می‌شود:
Bash
bash <(curl -fsSL [https://get.hy2.sh/](https://get.hy2.sh/))
۳. تنظیم کانفیگ سرور
دستور زیر را بزنید تا فایل تنظیمات باز شود:
Bash
nano /etc/hysteria/config.yaml
سپس کدهای زیر را کپی کرده و داخل آن قرار دهید:
(نکته: در بخش password، حتماً یک رمز قوی برای خودتان بنویسید)
YAML
listen: :443
auth:
type: password
password: "Your_Strong_Password_Here"
masquerade:
type: proxy
proxy:
mode: remote
addr: [https://www.apple.com](https://www.apple.com)
quic:
initStreamReceiveWindow: 8388608
maxStreamReceiveWindow: 16777216
initConnReceiveWindow: 8388608
maxConnReceiveWindow: 16777216
maxIdleTimeout: 30s
activeConnIdleTimeout: 30s
disablePathMTUDiscovery: false
bandwidth:
up: 100 Mbps
down: 100 Mbps
udpForwarding: true
برای ذخیره فایل، کلیدهای
Ctrl+X
سپس
Y
و در نهایت
Enter
را بزنید.
۴. باز کردن پورت‌ها در فایروال
برای عملکرد صحیح، باید پورت ۴۴۳ از نوع UDP را باز کنید:
Bash
sudo ufw allow 443/udp
sudo ufw enable
۵. راه‌اندازی و اجرای نهایی
Bash
sudo systemctl daemon-reload
sudo systemctl enable hysteria
sudo systemctl restart hysteria
📱
تنظیمات برای اتصال در گوشی یا ویندوز:
در برنامه‌هایی مثل NekoBox ،v2rayNG یا Exclave یک پروفایل جدید از نوع
Hysteria 2
بسازید و اطلاعات زیر را وارد کنید:
🔸
Server:
آی‌پی سرور شما
🔸
Port:
443
🔸
Password:
رمزی که در فایل کانفیگ تعیین کردید
🔸
SNI / Masquerade:
www.apple.com
🔸
Skip Cert Verify (Insecure):
True
(حتماً فعال شود)
✅
تمام! حالا یک کانکشن به شدت پایدار و پرسرعت دارید. اگر در مراحل نصب سوالی داشتید، توی کامنت‌ها بپرسید.
👇
📌
#آموزش
#سرور
#فیلترشکن
#Hysteria2
#Hy2
#اوبونتو
#V2ray
#تونل
#VPS
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5681" target="_blank">📅 02:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">https://t.me/boost/archivetell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5680" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚠️
خدمت دوستان باید چند نکته مهم رو بگم:
هیچ تاثیری روی پروتکل های tcp , udp ,ikev2, wstunnel رو هر حالتی از سانسورشیب بزارید از کانفیگ A تا حتی H و I باشه هیچ تاثیری در وصل شدن سریعتر شما اصلا نداره! فقط این حالت برای وایرگارد قابل استفاده هست دقت کنید
نکته بعدی این هستش که شما حالت server routing رو هم حالت اتوماتیک بزارید چه حالت regular و حتی alternative هیچ تاثیری باز هم تو اتصال شما نداره فقط و فقط حالت اتوماتیک بزارید
مورد اخر گزینه large tls هم روشن بزارید چون به اتصال بهتر شما کمک میکنه وقتی خاموش باشه سخت تر وصل میشید در کل این ۳ مورد رو دوستمون دقت نکردن و نیاز بود این مورد حتما رو بگم که سرگردان تغییر کانفیگ های A,b,c نشید
❤️
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5679" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://80fbb3e8-d705-4eca-a519-fd82fd6d319a@46.38.137.141:38554?type=tcp&encryption=none&security=none#%40IR_SI%20%2F%20100GB%20UAE%F0%9F%87%A6%F0%9F%87%AA-nubknlau-tpbvyzw1
http://46.38.137.141:2096/sub/eyovzx7b813yvs6g
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5678" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانفیگ های اهدایی یکی از ممبرای عزیز
❤️
حجم ۲۰۰ گیگ
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@sv2.vaslimgroup.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-asli-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@snapp.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%92%9Asnapp%F0%9F%92%9A-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@tapsi.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%A9%B7tapsi%F0%9F%A9%B7-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@anten.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%94%B1anten%F0%9F%94%B1-200.00GB%F0%9F%93%8A
هر ۷ تا رو اد کنید ، بعضی مناطق بعضی هاشون کار میده
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5677" target="_blank">📅 21:27 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
