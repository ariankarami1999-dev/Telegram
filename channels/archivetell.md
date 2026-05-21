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
<img src="https://cdn4.telesco.pe/file/OqWjyKPy-umur0jbA_gWIt_8uiMq5RGxy9qzb_PZSP4BqJGmPLhLWDhIRiZb9qUbvbz9CB9JuKL_Z3gcoXSnRSof801k3WKKW3dybbfH5HGqXYwdn-MFdKtk8ZI8CG6a0tC-9RMTSA00uZE5MmNH4bm9IJPH15ybaqZj45_Ngq2iglf5jRQL3QUxPKuBz5zLSUn9QBuYFUxqBT7x0Qr2iDWmDCXuBfL9x6YL8XazjYcB0imVPG-Cjuq-K74xEtVYmeSDx9kxgeRARYRxW3BtqwXGUnX-WhofCp8sTXgmckE0nurMvNkf1nWXXTkjXW0bOBqpoCOuCjzmkcutDNHKMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.81K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 00:16:57</div>
<hr>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبشکن Beshkan</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PsiphonAndroid-GA-469b.apk</div>
  <div class="tg-doc-extra">24.6 MB</div>
</div>
<a href="https://t.me/archivetell/5257" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود نسخه بروزرسانی شده و جدید
سایفون
ویژه اندروید
👍
✍
Beshkan</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/archivetell/5257" target="_blank">📅 23:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
معرفی پروژه Zyrln: عبور از سد فیلترینگ با ترافیک ابری گوگل (آپدیت 1.6.0)  ---  رفقا امشب قصد داریم ابزاری رو معرفی کنیم که با استفاده از دو تکنیک متفاوت، فیلترینگ رو به طور کامل دور می‌زنه و ترافیک شما رو پشت سرورهای گوگل مخفی می‌کنه.  برخلاف فیلترشکن‌های…</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/archivetell/5256" target="_blank">📅 23:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
معرفی پروژه Zyrln: عبور از سد فیلترینگ با ترافیک ابری گوگل (آپدیت 1.6.0)
---
رفقا امشب قصد داریم ابزاری رو معرفی کنیم که با استفاده از دو تکنیک متفاوت، فیلترینگ رو به طور کامل دور می‌زنه و ترافیک شما رو پشت سرورهای گوگل مخفی می‌کنه.
برخلاف فیلترشکن‌های معمولی، Zyrln نیازی به سرورهایی نداره که مرتباً فیلتر بشن. این ابزار دو حالت کاربری داره:
1️⃣
حالت اول: دسترسی سریع به سرویس‌های گوگل (بدون نیاز به هیچ سروری!)
اگر فقط می‌خواید تحریم یا فیلترِ سرویس‌هایی مثل Gmail، Google Drive، Maps، Firebase یا Google Docs رو دور بزنید، نیازی به هیچ سروری ندارید.
Zyrln با تکنیک «قطعه‌قطعه کردن دست‌دهی TLS» (TLS Fragmentation)، کاری می‌کنه که سیستم فیلترینگ (DPI) نتونه آدرس سایت رو بخونه و در نتیجه بدون نیاز به رله یا کانفیگ، سایت‌های گوگل براتون با بالاترین سرعت باز می‌شن.
2️⃣
حالت دوم: دسترسی به همه‌چیز (اینستاگرام، یوتیوب، تلگرام و...)
برای باز کردن کل اینترنت، ترافیک شما وارد اسکریپت‌های رایگان گوگل (Google Apps Script) میشه. سیستم فیلترینگ فقط می‌بینه که شما در حال تبادل دیتا با خودِ گوگل هستید. سپس گوگل ترافیک رو به یک «گره خروجی» (Cloudflare Worker رایگان یا VPS خودتون) می‌فرسته و سایت واقعی رو براتون لود می‌کنه.
✨
تغییرات کلیدی در آپدیت جدید v1.6.0:
🔸
مسیریابی هوشمند (ایران مستقیم):
حالا سایت‌های ایرانی (دامنه‌های .ir) به طور خودکار بدون نیاز به رله باز می‌شن تا سهمیه گوگل اسکریپتِ شما هدر نره.
🔸
بهبود در آپلودهای سنگین:
پایداری در آپلود فایل‌های حجیم به طرز چشمگیری بهتر شده.
🔸
سیستم Failover هوشمند:
اگر چند لینک Apps Script به برنامه بدید، کلاینت فقط از یکی استفاده می‌کنه و درخواست‌ها رو تکراری نمی‌فرسته، اما به محض از کار افتادنش، سریعاً سوییچ می‌کنه روی اسکریپت بعدی.
🔸
رفع باگ‌ها در نسخه اندروید:
مشکل کرش کردن در زمان جابجایی بین حالت‌های Direct و Proxy برطرف شده و رابط کاربری بسیار روان‌تر عمل می‌کنه.
🛠
شروع به کار و راه‌اندازی (مرحله‌به‌مرحله):
راهنمای کاملاً فارسی و روان برای راه‌اندازی دسکتاپ و اندروید در صفحه گیت‌هاب پروژه قرار داده شده.
📥
لینک دانلود مستقیم نسخه‌های دسکتاپ و اندروید:
🔗
https://github.com/ajavadinezhad/zyrln/releases/tag/v1.6.0
آموزش و توضیحات فارسی پروژه:
🔗
https://github.com/ajavadinezhad/zyrln/blob/main/README_FA.md
📌
#معرفی_ابزار
#گوگل_رله
#نت_ملی
#فیلترشکن
#اندروید
#ویندوز
#Zyrln
#Bypass
#Cloudflare
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/archivetell/5255" target="_blank">📅 23:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🗂
فهرست جامع ابزارها و متدهای اتصال (آرشیو و دسترسی سریع)
---
رفقا سلام!
✋
برای اینکه بتونید خیلی راحت روشِ مناسب خودتون رو پیدا کنید، تمام ابزارها و متدهایی که تا الان تو کانال معرفی کردیم رو بر اساس نوع کاربردشون دسته‌بندی و هشتگ‌گذاری کردیم.
کافیه روی هشتگ اختصاصیِ هر ابزار کلیک کنید تا به پست آموزش و دانلودش هدایت بشید:
☁️
بخش اول: متدهای مبتنی بر گوگل و دامین‌فرانتینگ (کلاد)
این روش‌ها ترافیک شما رو پشت سرورهای ابری (مثل گوگل، ورسل و نتلیفای) مخفی می‌کنن.
🔸
MHRV (نسخه اختصاصی پایتون):
اتصال از طریق رله گوگل با مسیریابی هوشمند، پنل مدیریت ترافیک و فایل اجرایی تک‌فایل (exe). ➔
#MHRV
#Python
🔸
mhrv-rs:
نسخه فوق‌سریع و بهینه‌شده‌ی رله گوگل با زبان Rust (پشتیبانی از مک، لینوکس، ویندوز و اندروید). ➔
#mhrv_rs
#Rust
🔸
NovaProxy:
پروکسی حرفه‌ای دسکتاپ با ترکیب Google Apps Script و Cloudflare Worker. ➔
#نوا_پروکسی
#NovaProxy
🔸
XHTTP-Installer:
اسکریپت ساخت تونل VLESS روی CDNهای Vercel و Netlify (مخصوص سرور). ➔
#XHTTP
#ورسل
#نتلیفای
🎭
بخش دوم: متد SNI Spoofing (تزریق دامنه فیک)
این متدها با ارسال یک پکت فیک به سیستم فیلترینگ، مسیر رو برای دیتای اصلی شما باز می‌کنن.
🔸
Cloak:
کلاینت گرافیکی، ساده و بی‌نظیر برای مدیریت SNI Spoofing روی مک و ویندوز. ➔
#Cloak
🔸
FakeSNI:
ابزار تخصصی و حرفه‌ای تزریق SNI فیک نوشته شده با زبان Go (مخصوص لینوکس). ➔
#FakeSNI
🔸
دامنه مستقیم hCaptcha:
اخبار و کانفیگ‌های مربوط به استفاده از hCaptcha برای اسنیفینگ. ➔
#hCaptcha
#SNI_Spoofing
🔍
بخش سوم: اسکنرها و ابزارهای جستجوی آی‌پی (IP Scanners)
برای پیدا کردن آی‌پی‌های تمیز جهت استفاده در متدهای بالا و برنامه‌های مختلف.
🔸
CDN IP Scanner (تحت وب):
اسکنر بی‌نظیر مرورگر بدون نیاز به نصب هیچ برنامه‌ای. ➔
#اسکنر
#CDN
🔸
Network Checker:
اپلیکیشن اندرویدی همه‌کاره با قابلیت اسکن آکامای و ساخت کانفیگ. ➔
#نتورک_چکر
#Network_Checker
📡
بخش چهارم: دسترسی‌های آفلاین و مبتنی بر فید
ابزارهایی برای مواقع قطعی شدید و خواندن محتوا بدون نیاز به اتصال مستقیم.
🔸
چشم عقاب (Eagle Eye):
دریافت اخبار و کانفیگ فیلترشکن از طریق اسکن بارکدِ شبکه‌های ماهواره‌ای. ➔
#چشم_عقاب
#ماهواره
🔸
TheFeed:
فیدخوان آفلاینِ پرسرعت با قابلیت Query Sharing (برای iOS، اندروید، ویندوز، مک و لینوکس). ➔
#TheFeed
🔸
EzyTel (نسخه بهینه‌شده):
اسکریپت خواندن آفلاین کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت. ➔
#ایزی_تل
#EzyTel
📱
بخش پنجم: کلاینت‌های اتصال (Clients)
برنامه‌های پایه‌ای برای وارد کردن کانفیگ‌ها.
🔸
v2rayNG:
آپدیت‌ها و معرفی قابلیت‌های جدیدِ محبوب‌ترین کلاینت اندروید (نسخه‌های 2.1.7 و 2.1.8). ➔
#v2rayNG
#آپدیت
---
💡
نکته:
برای دسترسی به آموزش هر بخش، روی هشتگ‌های آبی‌رنگِ روبروی آن کلیک کنید.
📌
#فهرست
#دسترسی_سریع
#آموزش
#فیلترشکن
#نت_ملی
#آرشیو
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/archivetell/5254" target="_blank">📅 23:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb86e0d73.mp4?token=jtgeBwarUaOxqO3suV-_OBGf__SxYMbiicVVoyBMm18I3eX7YDtmqjriVppHjROdRQbHwsw1XUGVjWoctA2TFgciR0fv4TeUfRixvk1TgoVI2d7-b-ZnX9EWSQVoaQwBPCTh5wchHlzUgZ8Xq-MI0GYyKfE94KJMCHYaJOvtWqcO5wc8PT61t2_f7stLltTD7HpT8X0o6E_ci_pD6hHZdXUtuz9LK6P6nGjdVwVgkolL6UcOesaHa8hEKc1t5JQnmsvwrclANOFinsZW71jlY4xehRufrd67sRNj3WHAct8lTY9LiPY1dJkW2t-XgPrXWlmb_lGeoC7shCyDNlU82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb86e0d73.mp4?token=jtgeBwarUaOxqO3suV-_OBGf__SxYMbiicVVoyBMm18I3eX7YDtmqjriVppHjROdRQbHwsw1XUGVjWoctA2TFgciR0fv4TeUfRixvk1TgoVI2d7-b-ZnX9EWSQVoaQwBPCTh5wchHlzUgZ8Xq-MI0GYyKfE94KJMCHYaJOvtWqcO5wc8PT61t2_f7stLltTD7HpT8X0o6E_ci_pD6hHZdXUtuz9LK6P6nGjdVwVgkolL6UcOesaHa8hEKc1t5JQnmsvwrclANOFinsZW71jlY4xehRufrd67sRNj3WHAct8lTY9LiPY1dJkW2t-XgPrXWlmb_lGeoC7shCyDNlU82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت ممبر به این نحو
😐
😂
🎁
کد تخفیف تمدید شد عزیزان:
archivetell
@ArchiveTellbot
---
حجم سفارش بالاست صبوری کنین</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5253" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عصر بخیر دوستان   تصمیم گرفتیم برای ۲۵ نفر اولی که دنبال اتصال پایدار هستن تخفیف ۱۰ درصدی در نظر بگیریم
❤️
تضمینی
✅
پایدار
✅
1GB: 200,000
➡️
1GB: 180,000  2GB: 400,000
➡️
2GB: 360,000  3GB: 600,000
➡️
3GB: 540,000  4GB: 800,000
➡️
4GB: 720,000  5GB: 1,000…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5252" target="_blank">📅 18:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتمام کد تخفیف
❤️
🙏
مبارکه دوستانی که خریدن</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5251" target="_blank">📅 17:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">عصر بخیر دوستان
تصمیم گرفتیم برای ۲۵ نفر اولی که دنبال اتصال پایدار هستن تخفیف ۱۰ درصدی در نظر بگیریم
❤️
تضمینی
✅
پایدار
✅
1GB: 200,000
➡️
1GB: 180,000
2GB: 400,000
➡️
2GB: 360,000
3GB: 600,000
➡️
3GB: 540,000
4GB: 800,000
➡️
4GB: 720,000
5GB: 1,000,000
➡️
5GB: 900,000
این کد
فقط تا ۳۰ دقیقه
اعتبار دارد.
🎁
کد تخفیف:
archivetelloff
🛒
ورود به ربات جهت تهیه کانفیگ پایدار
⚡
:
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5250" target="_blank">📅 17:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عصر بالا باشین
😁
تخفیف داریم تایم محدود
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5249" target="_blank">📅 15:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Samantel@ArchiveTell.txt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/archivetell/5248" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی سامانتل شیر و خورشید</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5248" target="_blank">📅 15:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Se7enPro_Setup.exe</div>
  <div class="tg-doc-extra">76.7 MB</div>
</div>
<a href="https://t.me/archivetell/5247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⬇️
لینک دانلود داخلی
⬇️
لینک گیت هاب</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5247" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔰
اتصال به اینترنت بین الملل با نسخه کاستوم شده سایفون (اختصاصی)
💢
قابلیت های برنامه:
◾️
اضافه شدن قابلیت Beast Mode
◾️
اضافه شدن پروتکل CDN Fronting
◾️
اضافه شدن قابلیت تانل کردن کل سیستم
◾️
اسکنر IP داخلی برنامه + لیست رنج های مورد نیاز
◾️
پشتیبانی از پروکسی های Socks 5/4 در بخش Upstream
◾️
امکان تغییر پورت پروکسی ها (به صورت پیشفرض رندوم هستن)
⬇️
لینک های دانلود:
●
لینک دانلود داخلی برنامه Se7enPro
●
لینک دانلود داخلی آموزش استفاده از برنامه
●
لینک گیت هاب پروژه
⚠️
اتصال اولیه به خاطر لود سرور ها کمی طول میکشه. برای اتصال با پروتکل CDN Fronting ریجن رو روی Auto بزارید و تغییر ندید که به سرور مناسب متصل بشه. هر آیپی که در برنامه شیر و خورشید اندروید براتون متصل میشه روی این نسخه ویندوزی هم اوکی هست.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5246" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دیسلایک میزنه
واقعاکه</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5245" target="_blank">📅 14:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واقعا حیف این‌چنل نیست زیر 10 کاست؟</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5244" target="_blank">📅 14:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5243" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">mhrv with panel.zip</div>
  <div class="tg-doc-extra">68.5 KB</div>
</div>
<a href="https://t.me/archivetell/5242" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5242" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAuLDYIV2dXDY9Z789TWT2a6JPn1Xaz65A1xBonMkv4hfl8VAczdJ6pGy7CSNM0jLhvD0-tlvjonVXpfsclnfDIQao4PxIJF_93tD-FxfmK6zciL4xZTkefhdzTQTE_luzkqbHCKPZudSuM5t1aa4GhmUAII-lZHDzlHZSDIIoBPAWfWeK9HWtChiK0LpXr7lkQm1u6jhKI9UzdmuZsZ24Xta8xvEKiphA78ose-e0_rW7Tf91Ubu4j2BPSOzvxfJ6VL-828mcScsoPFPr-MiR4X1umIBgdFHGGuhWrQ0VVXozV-LlOu-US22eSYTsvnqjR8l_tg9RY4ze8ngmBZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
توضیحات تکمیلی درباره عملکرد این نسخه توسعه‌یافته: https://t.me/archivetell/5242  برای دوستانی که پرسیده بودن این نسخه دقیقاً چه فرقی کرده و چرا سرعتش بالاتره، تغییرات رو به زبان ساده اینجا باز می‌کنیم:  ۱. سیستم مسیریابی هوشمند (جلوگیری از هدر رفتن سهمیه):…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5241" target="_blank">📅 14:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💡
توضیحات تکمیلی درباره عملکرد این نسخه توسعه‌یافته:
https://t.me/archivetell/5242
برای دوستانی که پرسیده بودن این نسخه دقیقاً چه فرقی کرده و چرا سرعتش بالاتره، تغییرات رو به زبان ساده اینجا باز می‌کنیم:
۱. سیستم مسیریابی هوشمند (جلوگیری از هدر رفتن سهمیه):
در حالت عادی، ابزار MHRV تمام ترافیک شما (حتی سایت‌هایی که فیلتر نیستند) رو می‌فرسته سمت اسکریپتِ گوگل. این کار هم سرعت رو کم می‌کنه و هم سهمیه ۲۰ هزارتایی روزانه شما رو هدر میده.
اما در این نسخه توسعه‌یافته، یک سیستم هوشمند پیاده‌سازی شده؛ به این شکل که اگر سایت‌هایی مثل خود اسکریپت‌های گوگل، گوگل درایو، گیت‌هاب و ورسل روی اینترنتِ فعلی شما باز (وایت‌لیست) باشن، برنامه اصلاً اون‌ها رو سمت رله نمی‌فرسته و مستقیماً بازشون می‌کنه. نتیجه؟ سرعت به شدت بالا میره و سهمیه شما سیو می‌شه!
۲. پنل کنترل ترافیک:
یک داشبورد مدیریت ترافیک به برنامه اضافه شده. با این پنل می‌تونید دقیقاً ببینید چقدر دیتا داره رد و بدل می‌شه و کنترل کامل‌تری روی مصرف اینترنتتون داشته باشید (مثلاً می‌تونید ترافیک‌های سنگین و پس‌زمینه رو مدیریت کنید).
۳. افزایش سازگاری با سایت‌ها:
کدهای مربوط به ارسال درخواست‌ها بهینه‌سازی شدن تا سایت‌های سنگین و وب‌اپلیکیشن‌ها (مثل تلگرام وب یا سایت‌های هوش مصنوعی) خیلی روان‌تر، با خطای کمتر و سازگاری بیشتر باز بشن.
این نسخه با کلی بی‌خوابی و تست‌های مداوم بهینه‌سازی شده تا پایدارترین تجربه رو روی نت ملی داشته باشید. حتماً تستش کنید!
✌️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5240" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5239" target="_blank">📅 11:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صداهای ElevenLabs نامحدود و رایگان
صداهای زیاد دیگه‌ای مثل مایکروسافت ، هوش مصنوعی گوگل و موارد دیگه هم داره
https://teamsp.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5238" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPrAUZiZsGFu4oUENd4ns1_4rE7JyfCM0NlVrFFXg2oOGiLkrw_5glLALgjJNDNEQmalc-VAPTxCGZlnF-IFERkV7q_n6WPrQQ5sAitOkhEWOVu58Q7MKr09LFrniD-0pLF-mZZFZmeq4vs81ZYuzSyO2Bbhh1BWwBmCNJlrXij1GnfVngIIILJDB6qy-UYxuD-QZsO-ef9NLshD80BaP5S6b7dfDjNNZK45LITfjed7oLc8aONZfgei0khtdlTXYfDDVSk36QM6NbL7MDqH97D5Wa9-eKllNaTjmYSqlhHXIS7iMPE2mBT4f4Ap8JDrnSJo1Z6ERGtTnGlYuMTaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت هوشمندانه ‌تر کردن متن بدون اینکه شبیه به متن تولید شده توسط هوش مصنوعی به نظر برسد
Rewrite the text below so it sounds clearer, sharper, and more p
Improve the structure, remove weak wording, and make the message more confident without changing the original meaning.
Text: [paste here]
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5237" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خواندن پست‌ها و نظرات Threads در تلگرام
@threadsreaderbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5236" target="_blank">📅 08:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دانلود مدل های هوش مصنوعی از سرور ایران
Bitgraph.ir/iran-ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5235" target="_blank">📅 08:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جدا الان وقتشه کانفرینگ تنظیم بازار بیاد قیمتا بشکنه
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5234" target="_blank">📅 01:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📘
معرفی پروژه GateRelay
یک reverse relay سبک و حرفه‌ای با Go است که هدف اصلی آن تانل کردن لینک ساب پنل با یک http proxy است و نمی‌خواهید حتی یک درخواست غیرمجاز از proxy عبور کند.
با GateRelay می‌توانید یک دامنه داخلی/قابل‌دسترسی مثل:
https://example1.com/sub/...
را به یک upstream خارجی مثل:
https://example2.com/sub/...
وصل کنید؛ اما فقط بعد از اینکه درخواست از نظر دامنه، مسیر و متد کاملاً تأیید شد.
ویژگی‌ها:
• نوشته‌شده با Go
• پشتیبانی از authenticated HTTP proxy
• جلوگیری از open proxy شدن
• فیلتر سختگیرانه قبل از مصرف proxy
📱
GitHub:
https://github.com/YrustPd/GateRelay
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5232" target="_blank">📅 22:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=p9syS11hJ4fBGMd2n0IaprQhLLAR_o3kad7M1-l6HrbyY4ZkT6wNpHedURcBhw6Hv--69JEt-du_R7CwijiCq6V3wenAs-EnPT5jfvocYiMfyxaZIISCVgw-nTGmYhmY8wVVr9G8-dUh7Q0_0fStRcgs7AmHeNiSglWVYOmg69614Z3E-tVM0C_Yn0wNNwLrw5z1KwZADevIfBTiZwyW6-5nqWFZcRGOcbmMYUdDXXgJJwwmxl1yNW2R3TEkTNluRzpaogl5Wz7CMUcNTHG7eNbOhT_5HVoVH4Bk6NPfW6BDcDW5GPsKGWaNmId9kWMN7P4mfx7e7RSt9KetbmiFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=p9syS11hJ4fBGMd2n0IaprQhLLAR_o3kad7M1-l6HrbyY4ZkT6wNpHedURcBhw6Hv--69JEt-du_R7CwijiCq6V3wenAs-EnPT5jfvocYiMfyxaZIISCVgw-nTGmYhmY8wVVr9G8-dUh7Q0_0fStRcgs7AmHeNiSglWVYOmg69614Z3E-tVM0C_Yn0wNNwLrw5z1KwZADevIfBTiZwyW6-5nqWFZcRGOcbmMYUdDXXgJJwwmxl1yNW2R3TEkTNluRzpaogl5Wz7CMUcNTHG7eNbOhT_5HVoVH4Bk6NPfW6BDcDW5GPsKGWaNmId9kWMN7P4mfx7e7RSt9KetbmiFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5231" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5230" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش بازی های انلاین با پینگ خوب برروی ویندوز با استفاده از روش SNI Spoofing
موارد مورد نیاز:
اتصال به Sni Spoofing
v2rayng
نرم افزار Windscribe که از قبل توش اکانت داشتید حتی اکانت فری و از قبل بهش لاگین کردید .(الان نمیشه بهش لاگین کرد اگه کسی روشی داره بگه بهمون )
شروع:
فرض بر این میگیریم شما با sni وصل هستید به اینترنت ازاد
روی v2ray پروکسی رو بذارید روی Clear system proxy و اصلا نباید حالت TUN روشن باشه .
حالا باید توی تنظمیات وایندسکرایب این تنظیمات رو اعمال کنید :
1-در بخش CONECTION روی split tunneling بزنید و بذارید روی Exclusive و در بخش app همون صفحه روی دکمه + بزنید و برنامه SNI SPOOFING رو پیدا کنید و اضافه ش کنید و مطمین بشید تیکش سبز باشه .
2-برگردید به بخش CONECTION و در قسمت Proxy setting و در بخش پروکسی تغییرش بدید به HTTP و ادرس و پورت زیر رو بذارید
127.0.0.1
10808
3-دوباره برگردید به بخش connection و Firewall رو بذارید روی حالت Manual
4- بخش conncetion Mode رو بذارید روی حالت manual و پروتوکل TCP و پورت 443
دقت کنید فقط پروتوکل TCP رو میتونید با این روش بهش وصل بشید و پینگ خوبی بهتون میده اگه اینترنت نرمالی داشته باشید .
سرور هم میتونید از المان فرانکفورت یا فرانسه جاردین استفاده کنید.
با این روش اینترنت شما مستقیم از وایندسکرایب گرفته میشه که هم اینترنت تمیزی بهتون میده که همه سایت ها و اپلیکیشن ها باز میشن هم پینگ خوبی بهتون میده.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5229" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">sni spoofing
وصله
امنه ، راحت استفاده کنید ، به حرف اونا که میگن مشکل داره و ... گوش نکنید ، واسه سود خودشون اینارو میگن</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5227" target="_blank">📅 21:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده
لینک داخلی v2ray ویندوز
https://seup.shop/f/zp9bi</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/archivetell/5226" target="_blank">📅 21:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5224" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">IP,SNI
185.141.106.238
,
a77.net.akamai.net
185.88.178.196
,
a184.net.akamai.net
185.141.106.238
,
ak.net.akamaized.net
185.50.37.52
,
a77.net.akamai.net
185.141.106.238
,
ds-aksb.akamaized.net
185.50.37.52
,
a104.net.akamai.net
185.88.178.196
,
ds-aksb.akamaized.net
185.141.106.238
,
a104.net.akamai.net
185.88.178.196
,
a77.net.akamai.net
185.50.37.52
,
a184.net.akamai.net
185.137.25.214
,
a248.e.akamai.net
185.88.178.196
,
a104.net.akamai.net
185.141.106.238
,
a184.net.akamai.net
185.88.178.196
,
a248.e.akamai.net
164.138.17.122
,
a184.net.akamai.net
185.88.178.196
,
ak.net.akamaized.net
185.50.37.52
,
ds-aksb.akamaized.net
185.137.25.214
,
a184.net.akamai.net
185.137.25.214
,
a104.net.akamai.net
185.141.106.238
,
a248.e.akamai.net
185.50.37.52
,
ak.net.akamaized.net
185.50.37.52
,
a248.e.akamai.net
185.137.25.214
,
ds-aksb.akamaized.net
185.137.25.214
,
a77.net.akamai.net
185.208.174.167
,
a77.net.akamai.net
185.208.174.167
,
a184.net.akamai.net
185.208.174.167
,
a248.e.akamai.net
185.137.25.214
,
ak.net.akamaized.net
185.208.174.167
,
a104.net.akamai.net
185.208.174.167
,
ak.net.akamaized.net
185.208.174.167
,
ds-aksb.akamaized.net
37.191.95.70
,
a248.e.akamai.net
37.191.95.70
,
ak.net.akamaized.net
37.191.95.70
,
a184.net.akamai.net
37.191.95.70
,
ds-aksb.akamaized.net
37.191.95.70
,
a104.net.akamai.net
37.191.95.70
,
a77.net.akamai.net
برای شیر خورشید
تست شده رو نت ایرانسل
Sni
a248.e.akamai.net
a77.net.akamai.net
a104.net.akamai.net
a184.net.akamai.net
ds-aksb.akamaized.net
ak.net.akamaized.net
Ip
185.88.178.196
185.50.37.52
185.141.106.238
185.137.25.214
164.138.17.122
185.208.175.228
185.208.174.167
5.160.13.85
5.160.13.85
37.191.95.70</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5223" target="_blank">📅 20:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برای شیر و خورشید
IP,SNI
185.141.106.238
,
aparat.com
37.191.95.70
,
snapp.ir
78.39.234.140
,
snapp.ir
81.91.145.2
,
snapp.ir
185.141.106.238
,
telewebion.com
81.91.145.2
,
digikala.com
78.39.234.140
,
varzesh3.com
81.12.72.218
,
varzesh3.com
185.141.106.238
,
digikala.com
37.191.95.70
,
aparat.com
37.191.95.70
,
bmi.ir
185.137.25.214
,
aparat.com
37.191.95.70
,
digikala.com
80.191.243.226
,
aparat.com
80.191.243.226
,
bmi.ir
80.191.243.226
,
snapp.ir
185.137.25.214
,
telewebion.com
78.39.234.140
,
digikala.com
80.191.243.226
,
digikala.com
37.191.95.70
,
telewebion.com
78.39.234.140
,
bmi.ir
81.91.145.2
,
bmi.ir
109.72.197.1
,
varzesh3.com
109.72.197.1
,
telewebion.com
109.72.197.1
,
bmi.ir
185.137.25.214
,
varzesh3.com
109.72.197.1
,
aparat.com
185.141.106.238
,
varzesh3.com
81.91.145.2
,
telewebion.com
78.39.234.140
,
aparat.com
81.12.72.218
,
aparat.com
185.141.106.238
,
bmi.ir
109.72.197.1
,
snapp.ir
78.39.234.140
,
telewebion.com
81.91.145.2
,
aparat.com
5.160.128.142
,
telewebion.com
81.91.145.2
,
varzesh3.com
80.191.243.226
,
telewebion.com
81.12.72.218
,
telewebion.com
185.141.106.238
,
snapp.ir
81.12.72.218
,
digikala.com
5.160.128.142
,
bmi.ir
5.160.128.142
,
varzesh3.com
5.160.128.142
,
snapp.ir
5.160.128.142
,
aparat.com
185.137.25.214
,
snapp.ir
80.191.243.226
,
varzesh3.com
185.137.25.214
,
digikala.com
5.160.128.142
,
digikala.com
185.137.25.214
,
bmi.ir
81.12.72.218
,
snapp.ir
109.72.197.1
,
digikala.com
81.12.72.218
,
bmi.ir
37.191.95.70
,
varzesh3.com
iP
31.214.169.244
185.109.61.27
46.32.31.30
37.255.133.30
37.191.76.110
80.191.243.226
185.141.106.238
81.12.72.218
37.191.95.70
63.141.252.203
142.54.178.211
5.160.13.85
178.252.128.66
94.130.13.19
2.23.168.254
2.23.168.144
78.39.234.140
109.72.197.1
185.137.25.214
2.23.168.7
78.157.41.60
2.23.168.96
185.208.175.228
81.91.145.2
2.23.168.47
185.255.91.60
2.23.170.80
2.23.168.213
2.23.168.174
65.109.34.234
5.160.128.142
SNi
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5222" target="_blank">📅 20:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5221" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTylfGfTESimBdpx_eXtN3MeRGpXApjt55ztpRrMH0eTdBFqSYpS5Ic5PjFO7Bt7RprsBg_ipn7yyiYO5Ac0f2UvyX8F_vffWcwcjv1ya1yltok4cWTWTQoaqYw7D61CXnyVdMusbZpX9gd69wXAdNy6sjoEhsnrev3i6APIxHD5HNOjqaBK9CJmxWA5RxNxxhWPkH7o8boZ6Ww4wqyMLOg68_LKJNLdu3Kcz9A-dA6QMAFvy8JRz-x99h6HfAYAtlHAbpoa0kpAUozOu5GmO4y7BosMAGGI-_iuFiN6diN_ybD3yPUQXsyoqFQZP15rcQhs0CSx56omSAYztQJxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjAxWH9cE36zRyJMZiRxGWTSYwBsQiiLAixOBznrDE5V0-0Fmq1wczToUm6LABY3N3jjAszyfVBkeAe6e3pk3cjMKQWZvM24mUxP3kDAvSXSq2uVipwUicFp6Ggb33ynD2YVZS4X3vcHUmCfw9oMSq1TIs_ifYXMTc_eF2gWjn2PDUAPin7dRk7Tb6htbTrHZ3J1Tx6of1m-eKsZKmwgZ0wiSufxdvqSc9kSg2z3MjJuaDhwxTnlUuCuXd5SLPvp2cbUrM73pESTTl_vD60jS3IBnvthjvRA3F7wJMWdkEcVvqKWNLMZ5UMxMdaVmH5aZDIj-pyPsIGblbWam3mlzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرامپت تبدیل تصویر معمولی به تصویری که انگار در یک کتاب کودکانه قدیمی اروپای شرقی دهه ۸۰ پیدا شده است
Turn this photo into a strange vintage Soviet children's book illustration with grotesque humorous cartoon energy. Use thin shaky black ink lines, awkward anatomy, elongated limbs, uncomfortable facial expressions, chaotic movement, weird proportions, sparse composition, and intentionally clumsy drawing style. Make the characters look slightly absurd, nervous, and ridiculous rather than cute. Use pale faded watercolor washes, dirty paper texture, uneven coloring, washed-out muted colors, lots of empty space, careless sketchy linework, and rough old-print illustration texture. Keep the background minimal and random, with small strange details and loose doodles. The mood should feel weird, humorous, slightly unsettling, and authentically like an old Eastern European children's book illustration from the 1980s. Do NOT make it polished, aesthetic, modern, cute, detailed, or realistic.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5219" target="_blank">📅 18:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات های کاهش حجم فیلم رایگان
@AdaptiveVideoBot
@Compreseebot
@mediaEasyBot
@wecompress_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5218" target="_blank">📅 17:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
آپدیت حیاتی و بسیار مهم فیلترشکن محبوب mhrv-rs (نسخه v1.9.33) منتشر شد!
---
رفقا سلام!
✋
ابزار
mhrv-rs
(نسخه‌ی سریع و سبک فیلترشکن رله‌ی گوگل به زبان Rust) رو که یادتونه؟ همون متد خفنی که ترافیک شما رو پشت دامنه‌ی اصلی گوگل مخفی می‌کرد و کاملاً هم رایگان بود.
حالا یه آپدیت جدید براش اومده که دست روی بزرگترین باگِ این متد، یعنی
«هدر رفتن سهمیه روزانه جیمیل در زمان بیکاری»
گذاشته و اون رو کاملاً برطرف کرده!
🎯
تمرکز اصلی این آپدیت: جلوگیری از مصرف بی‌رویه‌ی سهمیه گوگل (Google Quota)
توی نسخه‌های قبلی، حتی وقتی در حال وب‌گردی نبودید و سیستم شما کاملاً بیکار (Idle) بود، کلاینت مدام درخواست‌های خالی (Empty Polls) به اکانت جیمیل‌تون می‌فرستاد تا اتصال رو زنده نگه داره. این کار باعث می‌شد سهمیه رایگانِ ۲۰ هزارتایی روزانه‌ی شما خیلی سریع و بیهوده تموم بشه.
⚡️
تغییرات و بهینه‌سازی‌های فنی نسخه v1.9.33:
🔸
سیستم هوشمند Keepalive Backoff:
در حالت Full Tunnel، وقتی اتصال شما کاملاً بیکار بشه، برنامه با یک مکانیزم هوشمند و سخت‌گیرانه‌تر، فرستادن پینگ‌های متوالی رو متوقف می‌کنه تا سهمیه‌تون الکی نسوزه.
🔸
کاهش چشمگیر لودِ سرور:
با این کار، بارِ ترافیکیِ درخواست‌ها روی «گوگل اپس اسکریپت» و
tunnel-node
در زمان‌های سکوتِ شبکه به شدت کاهش پیدا می‌کنه.
🔸
پشتیبانی از ناوگان‌های ترکیبی (Mixed Fleets):
اگر چند دیپلوی مختلفِ جیمیل داشته باشید و حداقل یکی از اونا قابلیت Long-poll سالم رو داشته باشه، کلاینت هوشمندانه ارتباط رو به صورت Round-robin حفظ می‌کنه تا دیتای برگشتی از سمت سرور قفل نشه و اتصالتون همیشه پایدار بمونه.
---
📥
لینک‌های دانلود مستقیم آخرین نسخه (v1.9.33):
📱
نسخه اندروید (Universal):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-android-universal-v1.9.33.apk
💻
نسخه ویندوز (Windows 64-bit):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-windows-amd64.zip
🌐
صفحه گیت‌هاب پروژه (جهت دسترسی به نسخه‌های مک، لینوکس و کدهای جدید):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
📌
#آپدیت
#گوگل_رله
#نت_ملی
#رایگان
#mhrv_rs
#Rust
#Google
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5217" target="_blank">📅 17:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGtaCnlnff8Jc3ktt11iFVQhiwM1kjidAR4mTzywIWPTHULUXjMLq9AeRoDqQVR0hA0cEuRnfaNGZvDL-QlUsXtgvu3b9IYtnErnGcwISYgJWFrIaD9_Jukbd29E_oQCJefG0T3IUYvvOPZ9NIbtw2gWz3h-ultcDn25vvxI2bmkYM4cBwOLCF9ZGpjIOT4a6fAK58slqz6Py5uEC1-RRuKFrLqUIl6etDHE5WoRj1E1SUUxpc3UjtKOXyudgiW3LpjEMEho9m6sr4qm69Af64wZcv5Wi3KCiV2aAfq0E1EjXB_qPfnTpazHnqsmsKNNvKtraQP-mUy6t3YgsXwKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpIdQZZ7il8T2qoijvb962GAZAshVzxy9hG3HaVpNUvTdfZqODrdjQGU9l1t1K-CVst7uqdzomgRo_C3WacRYRQRHvchTydPUS173TVf7rgeSrF_Ib-RBYbU4nUuFREwZTIKWew1lah4JkWCUh9QgoKOcGD3VAp33xo94KQnDhBucvreEGB548lJIpB2Rt8OMI-bqu10NeolyZ_G4QuZtTpFzoKwsz6U6NRzQjz3v1m3EDhsHvP0m35mgV1egQ1YoQ8ezGwi2JJxOz6CAJxdhj3ofbjUDhyCmwyrMocvoFZ0t4mZOcRKQCoL85iGGH06CRugAcx_Sz-Clb85m9AoZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!  ---  رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5215" target="_blank">📅 17:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ezytel-v2_modified-r1@ArchiveTell.zip</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/archivetell/5214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت متد ezytel
باز کردن محتوای تلگرام با استفاده از گوگل ترنسلیت(یچیزی تو مایه های telemirror)
یکی از ممبرای عزیز ، ایزی تل رو ویرایش کرده و باگ هاشو برطرف کرده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5214" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!
---
رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند کانال، اسکریپت
EzyTel
رو کاملاً بهینه‌سازی کرده و یک نسخه‌ی Modified بدون باگ و همه‌کاره ازش داده بیرون.
✨
تغییرات و بهبودهای کلیدی در نسخه modified_r1:
🔸
تغییرات ظاهری و UI جدید:
• اضافه شدن دارک مود اختصاصی با رنگ‌بندی شیکِ Telegram Web.
• شیشه‌ای و شفاف شدن هِدِر کانال‌ها همراه با حذف آواتار و اسم فرستنده برای تمیزتر شدن ظاهر پست‌ها.
• امکان فول‌اسکرین، زوم و جابه‌جایی (Pan) روان با کلیک روی تصاویر کانال.
• رفع مشکل کامل هم‌ترازی (RTL) در متن‌های ترکیبی فارسی و انگلیسی.
• نمایش ارورها به‌صورت Toastهای نرم و محو شونده بجای پاپ‌آپ‌های (Alert) رو اعصاب!
🔸
امکانات کاربردی اضافه شده:
• قابلیت اضافه یا حذف کردن کانال‌ها مستقیماً از داخل محیط خود برنامه (دیگه نیازی به ادیت دستی فایل
channels.txt
نیست!).
• مرتب‌سازی خودکار و هوشمند لیست کانال‌ها بر اساس جدیدترین پیام ارسال شده.
• باز شدن کامل باکس Quoteها برای نمایش متون طولانی و امکان کپی شدن متن داخل کوت با کلیک روی آن.
• اضافه شدن دکمه اختصاصی COPY برای کپی کردن کل متن یک پست با یک کلیک.
🔸
ارتقای فنی و سیستم ضد بلاک (Anti-Block):
• حذف کامل دیتای اضافه و آشغال‌های گوگل ترنسلیت از لینک‌ها و باز شدن آن‌ها در تب جدید.
• استفاده پیش‌فرض ابزار از سیستم سورس
curl
روی پروتکل پرسرعت HTTP/2.
• اضافه شدن دامنه‌های بیشتر از سرورهای گوگل و تزریق Headerها و User-Agentهای کاملاً تصادفی برای دور زدن لیمیت‌ها.
---
⚠️
چطور باگ Rate Limit (خطای Something went wrong) گوگل رو دور بزنیم؟
گوگل روی حجم درخواست‌های پشت‌سرهم حساسه. برای اینکه لیمیت نشید:
1️⃣
خیلی سریع و رگباری روی کانال‌ها کلیک نکنید.
2️⃣
از لیست‌های بیش از حد سنگین و شلوغ استفاده نکنید.
✔️
راهکار رفع لیمیت:
اگر خطای Something went wrong گرفتید، کافیه ۲ الی ۳ دقیقه صبر کنید، یا اینکه یک‌بار حالت هواپیمای گوشی رو روشن/خاموش کنید (یا نت رو بین 4G و 3G سوییچ کنید) تا آی‌پیتون عوض بشه. (این ترفند روی آی‌پی ثابت وای‌فای خانگی جواب نمیده).
❌
محدودیت‌های دائمی:
عدم دانلود فایل‌ها و ویدیوها، کیفیت پایین تصویر و عدم نمایش ایموجی‌های پرمیوم تلگرام به دلیل محدودیت‌های خودِ ساختار گوگل ترنسلیت هستن و کاریش نمیشه کرد. این متد تا زمانی که گوگل در ایران باز باشه، تضمینی کار می‌کنه!
---
🛠️
راهنمای راه‌اندازی قدم‌به‌قدم روی ویندوز و اندروید:
💻
اجرا در ویندوز:
۱. برنامه معروف XAMPP رو دانلود و نصب کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
(محل نصب زامپ) کپی کنید.
۳. برنامه XAMPP Control Panel رو باز کنید و سرویس
Apache
رو استارت (Start) کنید.
۴. مرورگر رو باز کنید و آدرس
localhost/ezytel
یا
127.0.0.1/ezytel
رو بزنید. (اگر نیومد، پورت درج شده جلوی آپاچی رو ته آدرس بذارید، مثل
localhost:80/ezytel
).
🤖
اجرا در اندروید:
۱. برنامه KSWeb رو از استورها نصب و اجرا کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
که در حافظه داخلی گوشیتون ساخته شده کپی کنید.
۳. در برنامه KSWeb به تب APACHE و PHP برید و گزینه‌ی
Enable Server
رو روشن کنید.
۴. مرورگر گوشی رو باز کنید و آدرس
localhost:8000/ezytel
یا
127.0.0.1:8000/ezytel
رو وارد کنید. (ترجیحاً از آپاچی استفاده کنید نه Lighttpd).
📌
#آموزش
#ایزی_تل
#تلگرام_آفلاین
#نت_ملی
#گوگل_ترنسلیت
#EzyTel
#Bypass
#Telemirror
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5213" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
معرفی Cloak: مدیریت حرفه‌ای و ساده‌ی SNI Spoofing روی دسکتاپ!
---
رفقا سلام!
✋
خیلی‌هاتون درگیرِ تنظیماتِ پیچیده‌ی «اسنیفینگ» (SNI Spoofing) توی محیط ترمینال و کنسول بودید. امروز یه ابزار فوق‌العاده به اسم
Cloak
رو معرفی می‌کنیم که کار رو براتون گرافیکی و به‌شدت راحت کرده!
✨
چرا Cloak خاصه؟
این ابزار یه کلاینتِ دسکتاپ (مخصوص مک و ویندوز) هست که خودش همه کارهای پشت‌پرده مثل تزریق SNI فیک (Fake SNI) و مدیریت کانفیگ‌ها رو انجام میده. دیگه نیازی نیست درگیر دستورات پیچیده‌ی ترمینال بشید.
🛠
قابلیت‌های کلیدی:
🔸
مدیریت یکپارچه: وارد کردن فایل‌های کانفیگ V2Ray، Trojan و... با درگ اند دراپ (Drag & Drop).
🔸
تست پینگ و سلامت: تست هم‌زمانِ همه‌ی کانفیگ‌ها و انتخاب سریع‌ترین سرور.
🔸
سیستم پروکسی هوشمند: اشتراک‌گذاری کانکشن با دستگاه‌های دیگه توی شبکه (LAN) تنها با یک کلیک!
🔸
پایداری بالا: مدیریتِ عالیِ Tunnel ها و پایداریِ کانکشن.
💻
آموزش راه‌اندازی سریع:
1️⃣
برنامه رو از لینک گیت‌هاب دانلود و نصب کنید.
2️⃣
در بخش Settings، دکمه «Restore Default» رو بزنید تا کانفیگ اولیه (که شامل آی‌پی‌های تمیزِ پیش‌فرض هست) بارگذاری بشه و بعد Save کنید.
3️⃣
به بخش Profiles برید، روی دکمه Add بزنید و کانفیگ‌های V2Ray/Trojan که دارید رو وارد کنید.
4️⃣
بعد از اضافه شدن، روی کانفیگ کلیک کنید و دکمه Ping رو بزنید. اگر پینگ داد، یعنی کانفیگ سالمه.
5️⃣
دکمه Connect رو بزنید تا پروکسی فعال بشه. (برای اشتراک‌گذاری با گوشی، دکمه LAN رو توی تنظیمات فعال کنید و آی‌پی و پورتی که میده رو توی گوشی وارد کنید).
📥
دانلود برنامه (ویندوز و مک):
صفحه رسمی پروژه در گیت‌هاب:
🔗
https://github.com/PechenyeRU/FakeSNI
⚠️
نکته مهم: این ابزارها برای دور زدن محدودیت‌هاست، همیشه امنیت و رعایت حریم خصوصی رو در اولویت قرار بدید.
📌
#معرفی_ابزار
#Cloak
#SNI_Spoofing
#نت_ملی
#فیلترشکن
#ویندوز
#مک
#v2ray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5212" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتلیفای بای بای</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5210" target="_blank">📅 14:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم دور زدن فیلترینگ با روش SNI Spoofing
روی سرور ایران (ترکیب با پنل 3x-ui)
در این آموزش قصد داریم با استفاده از یک ابزار بسیار سبک و قدرتمند (نوشته شده به زبان Rust)، سیستم SNI Spoofing را روی سرور ایران راه‌اندازی کنیم. این ابزار به ما کمک می‌کند با جعل نام دامنه (مثلاً استفاده از یک سایت تمیز مثل hcaptcha)، سیستم فیلترینگ (DPI) را فریب دهیم و ترافیک را با موفقیت به سرور خارج متصل کنیم.
###
🛠
مرحله اول: دانلود و انتقال ابزار به سرور ایران
ابتدا باید فایل اجرایی پروژه را روی سرور ایران خود قرار دهیم. برای این کار دو روش دارید:
روش اول (پیشنهادی - مستقیم از طریق ترمینال):
وارد ترمینال (SSH) سرور ایران شوید و دستور زیر را وارد کنید تا فایل مستقیماً از گیت‌هاب دانلود شود:
wget https://github.com/therealaleph/sni-spoofing-rust/releases/latest/download/sni-spoof-rs-linux-amd64
روش دوم (از طریق SFTP):
فایل sni-spoof-rs-linux-amd64 را از گیت‌هاب پروژه دانلود کرده و با نرم‌افزارهایی مثل WinSCP یا FileZilla، آن را در دایرکتوری روت (/root/) سرور ایران آپلود کنید.
###
⚙️
مرحله دوم: ساخت فایل کانفیگ (JSON)
حالا باید به برنامه بگوییم که روی چه پورتی گوش دهد و ترافیک را به کجا بفرستد.
۱. در ترمینال سرور، دستور زیر را بزنید تا یک فایل جدید باز شود:
sudo nano config.json
۲. کدهای زیر را دقیقاً در محیط باز شده کپی (Paste) کنید:
{
"graceful_shutdown_sec": 0,
"listeners": [
{
"listen": "127.0.0.1:40443",
"connect": "104.19.229.21:443",
"fake_sni": "hcaptcha.com"
}
]
}
💡
توضیح مقادیر مهم:
*
listen:
آدرس و پورتی است که برنامه روی سرور ایران منتظر دریافت ترافیک می‌ماند (اینجا روی لوکال‌هاست و پورت 40443 تنظیم شده).
*
connect:
آی‌پی سرور مقصد شماست. در این مثال از آی‌پی تمیز کلودفلر (
104.19.229.21
) با پورت 443 استفاده شده است.
*
fake_sni:
دامنه‌ای است که می‌خواهیم فیلترینگ را با آن فریب دهیم (در اینجا
hcaptcha.com
).
۳.
نحوه ذخیره فایل:
کلیدهای Ctrl + X را روی کیبورد بزنید. سپس حرف Y را تایپ کنید و در نهایت Enter بزنید تا فایل ذخیره شود.
###
🏃‍♂️
مرحله سوم: دسترسی دادن و اجرای دائمی برنامه
۱. ابتدا باید به فایلی که دانلود کردیم، اجازه اجرا (Execute) بدهیم:
sudo chmod +x sni-spoof-rs-linux-amd64
۲.
اجرای برنامه در پس‌زمینه:
اگر برنامه را عادی اجرا کنید، با بستن ترمینال برنامه متوقف می‌شود. برای اینکه برنامه همیشه روشن بماند، از ابزار Screen یا Tmux استفاده می‌کنیم. دستور زیر را بزنید تا یک سشن جدید باز شود:
screen -S spoofer
۳. حالا برنامه را با فایل کانفیگ اجرا کنید:
sudo ./sni-spoof-rs-linux-amd64 config.json
*(اگر اروری نداد، یعنی برنامه با موفقیت در حال کار است. حالا کلیدهای Ctrl + A و سپس D را بزنید تا برنامه در پس‌زمینه سرور در حال اجرا باقی بماند).*
###
🔗
مرحله چهارم: اتصال کانفیگ به پنل 3x-ui
حالا که Spoofer در پس‌زمینه سرور ایران کار می‌کند، باید پنل 3x-ui را طوری تنظیم کنیم که ترافیک کاربران را به این برنامه تحویل دهد.
۱. تنظیم اینباند (Inbound - ورودی):
وارد پنل 3x-ui سرور ایران شوید. یک کانفیگ ورودی (مثلاً VLESS یا Trojan) با پورت دلخواه بسازید و به کاربر بدهید. (این قسمت دقیقاً مثل ساخت کانفیگ‌های عادی شماست و تغییری ندارد).
۲. تنظیم اوتباند (Outbound - خروجی) - بخش اصلی:
حالا باید ترافیک را از ایران به خارج بفرستیم.
* در پنل 3x-ui به بخش
Outbounds
(یا Xray Config / Routing بسته به نسخه پنل) بروید.
* یک Outbound جدید ایجاد کنید.
* تنظیمات این Outbound باید
دقیقاً مشابه کانفیگ سرور خارج شما
باشد (همان کانفیگی که در نرم‌افزارهایی مثل v2rayN روی ویندوز وارد می‌کنید؛ با همان UUID، نوع شبکه، TLS و...).
*
تغییر کلیدی:
فقط دو فیلد زیر را تغییر دهید:
*
Address (آدرس):
را روی
127.0.0.1
تنظیم کنید.
*
Port (پورت):
را روی 40443 بگذارید.
۳. تنظیم مسیریابی (Routing):
در بخش تنظیمات Routing پنل، یک قانون (Rule) جدید اضافه کنید و بگویید هر ترافیکی که از Inbound (کانفیگ کاربر) وارد شد، به این Outbound (که ساختید) هدایت شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5208" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">https://seup.shop/f/nn3o5 از حالت فشرده خارج میکنید میرید توی فولدرش بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام  trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationl…</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5207" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
برگ‌ریزون‌ترین آپدیت جمینای؛ کلونِ دیجیتالیِ خودت رو بساز!
🚨
بچه‌ها، قضیه آواتار جدید جمنای (Gemini) خیلی دیوانه‌کننده‌تر از اون چیزیه که فکرشو می‌کردیم!
🤯
این بار گوگل رسماً مرزهای هوش مصنوعی رو جا به جا کرده. تو این آپدیت جدید، جمنای قابلیتی آورده که می‌تونید
دقیقاً با چهره و صدای خودتون
ویدیو تولید کنید!
🎬
🎙️
یعنی چی؟ یعنی کافیه عکس و صدای خودتون رو بهش بدید، تا یه آواتار فوق‌العاده طبیعی و واقعی ازتون بسازه. این آواتار می‌تونه هر متنی رو با لحن، صدا و میمیک صورت خودِ شما بخونه و یه ویدیوی کامل و بی‌نقص تحویلتون بده!
🔥
دیگه برای تولید محتوا حتی نیاز نیست جلوی دوربین بشینید؛ خودِ مجازی‌تون با بالاترین کیفیت همه کارا رو انجام میده! سرعت پیشرفت هوش مصنوعی هم به شدت جذابه، هم یه نمه ترسناک شده...
😨
فکر می‌کنید این تکنولوژی چقدر قراره کار یوتیوبرها و تولیدکننده‌های محتوا رو عوض کنه؟ شما حاضرین آواتار خودتون رو بسازین؟
🤔
👇
#Gemini
#هوش_مصنوعی
#آواتار
#تولید_محتوا
#تکنولوژی
#آپدیت_جدید
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5206" target="_blank">📅 12:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eup2GGaxki60bi-8Af2qUNuCqdoTbTjVLpBit3_HeXM2bhqpt3tbzDdBG6zjdoimF8svyoc_wyNT9bgkSeK7zIcbm9ndNhHCSHDKPxdDk2s62XewpJ8uBRagHAIQTJwN72cjWdI_YA-ugbmKPK9ilhkuAtAXr-Hhj6lUwcGiAq1pTY0u8cY7XkS90k77SVX1XaKKuwpJm5UYyJoR3f9dDDiFRO5j2KCQ3ZxnYiPlGB-z4u1Tz63R-b3SB5XdiphrjIG_Vw80pF1wnoorbp3BDGkEN80lAPLc9veqI0yGIjugza12TSHIoA8KZkk3M523Ea0rYvIjcyFECdWsiw2u_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای ۳.۵ اومد
پر قدرت تر از همیشه
+بنچمارک هاش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5204" target="_blank">📅 11:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فقط باید داخل سرور اینو بزنید
ping
104.19.229.21
اگه پینگ بده میشه</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5203" target="_blank">📅 10:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">راه اندازی sni spoofing رو سرور ایران
کانفیگی که با این متد وصل هستید رو اوتباند کنید تو پنل و کانفیگ بسازید..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5202" target="_blank">📅 10:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpb2to15uLHCCAFat81vO9rL293bxZcGlCpXO7UGThzuSxiOL6HwsdXefstIg5zD_poRM8BDWCS0Z1zHFGUcfLuLdUafNKSsOITM-NmBmQ6OpndUyUDNZaLjj-MXN09LxtcUIeeG3NThMLjwuVsYw4WfiGNLHdXHyli3TwDVdzDl7lklxPlANAugEn0kYqafkg0BQJavsbzXExn2MvXHeDM_uzNhyHLiANjF7yAuGm03Bm7xlMgeThvd7QN8WaBMcNY1rj7_bmNHFUjOWw1DGHRPp-3SIStC8Ub_I3-wtkrGqpBm1R5lrKfGLDehZ0fCQmFsz3xlRmvxfZwBNWWGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Google I/O 2026
جمنای، جستجو، عینک‌های هوشمند
جدیدترین رویداد گوگل موجی از نوآوری‌های هیجان‌انگیز را به همراه داشته است!
🌟
از معرفی جمنای، تا به‌روزرسانی‌های پیشگامانه در جستجو که وعده نتایجی شخصی‌تر و کارآمدتر را می‌دهد، گوگل مرزها را بیش از همیشه گسترش می‌دهد. علاوه بر این، عینک‌های هوشمند گوگل بازگشته‌اند، اکنون با قابلیت‌های پیشرفته واقعیت افزوده و طراحی باریک‌تر، با هدف ادغام بی‌نقص دنیای مجازی با واقعیتی که روزانه در آن حرکت می‌کنیم.
🌐
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5201" target="_blank">📅 09:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqk_lzP9Ls6MNFKaDSfXnwAds-sQatFmEVhaGecqMWyJWLDe-lJQX_GfNeDiUq0QyLFsfrPCqU-iNu-1P3_GwUYVQGwCGWNs2s53U7sO2SmqyN2wZNcOH5WzzXXt4hyfGok4VgjbBWoc_4cplUIBlKlObIv2RTwjJgV5AxGwGOnomfgP4QO2A_CPlLxF_5-N_eHWN0Kuut-iUUUS-xMZgDps1bEwzwP5MvGjULo1h0QPVjwV-kPtde5NGpk4xuzqz9vBVq2ZXjJDSZYi0YuQJiofQ2mf-bhtZ1LWe_ndb2JHzQlyIJMmlrya9PNy64EPUxP78Nr9a1uDOp354Tc30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه Gemini 3.5 Flash منتشر شد
این نسخه به‌طور قابل توجهی قوی‌تر از Gemini 3.1 Pro است.
مهم‌ترین نکته این است که گوگل به مشکلات مربوط به عامل‌پذیری (agentness) به طور جدی پرداخته و به ویژه مدل را در این زمینه بهبود داده است. به عنوان مثال، نشان دادند که چگونه Gemini 3.5 Flash در ۱۲ ساعت یک سیستم عامل کوچک نوشت که می‌تواند Doom را اجرا کند. مدل Pro نیز وجود دارد و وعده داده شده که ماه آینده عرضه شود، قیمت‌های آن احتمالاً بسیار بالا خواهد بود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5200" target="_blank">📅 08:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e945b36d4.mp4?token=O182d73SXPgf74tWKphHBpI1BPtbpgHAQljPtnDNDjceNf8Zwvl6sTRH_WVRiLu5jQBD4xY1EaYIuUHJhZtwD7H0TCtjdccB-DT4sdE7rlXw__VD4YV9Ct0PiSl1aEGJL_AvjEVro14ctPhrlASkzEupoPeXZMo3gxcxTkPV2qThmF4z6Frox5VbKSU9sn3cyGwRcujVqVVbPZpOubg2DRNwmC4gOWAw5L_43GSqlJrMFZNtAM087fMp6sfBuPz7mJDuzkBbNnxG8eYmMXTFFGv1YI6zUiD29-7V96jj-pdh6B40cGz0cIykYXmAUrB2hk1-KcctfFw8bEQ6fM9WAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e945b36d4.mp4?token=O182d73SXPgf74tWKphHBpI1BPtbpgHAQljPtnDNDjceNf8Zwvl6sTRH_WVRiLu5jQBD4xY1EaYIuUHJhZtwD7H0TCtjdccB-DT4sdE7rlXw__VD4YV9Ct0PiSl1aEGJL_AvjEVro14ctPhrlASkzEupoPeXZMo3gxcxTkPV2qThmF4z6Frox5VbKSU9sn3cyGwRcujVqVVbPZpOubg2DRNwmC4gOWAw5L_43GSqlJrMFZNtAM087fMp6sfBuPz7mJDuzkBbNnxG8eYmMXTFFGv1YI6zUiD29-7V96jj-pdh6B40cGz0cIykYXmAUrB2hk1-KcctfFw8bEQ6fM9WAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آپدیت جدید تلگرام ربات‌ها میتونن با همدیگه ارتباط برقرار کنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5199" target="_blank">📅 08:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده
لینک داخلی v2ray ویندوز
https://seup.shop/f/zp9bi</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/archivetell/5198" target="_blank">📅 08:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">marzban_http_proxy_install_guide.md</div>
  <div class="tg-doc-extra">6.6 KB</div>
</div>
<a href="https://t.me/archivetell/5197" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤔
راهنمای نصب Marzban روی سرور خام با HTTP Proxy.
در این فایل، مراحل نصب مرزبان روی سروری که دسترسی مستقیم به اینترنت بین‌الملل ندارد توضیح داده شده است.
قبل از اجرا، حتماً اطلاعات Proxy خودتان را جایگزین کنید و بعد از نصب، مرحله پاکسازی را انجام دهید.
‼️
﻿
توی این روش حد اقل به ۴۰۰ مگابایت پروکسی نیاز دارید.
💯
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5197" target="_blank">📅 01:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
آپدیت فوری v2rayNG (نسخه v2.1.8) منتشر شد!
---
هنوز چند روزی از انتشار نسخه ۲.۱.۷ نگذشته بود که تیم توسعه‌دهنده نسخه
v2.1.8
رو برای رفع باگ‌های جزئی و بهبود عملکرد منتشر کرد.
✨
تغییرات مهم در نسخه v2.1.8:
🔸
پشتیبانی از SOCKS4/5: حالا می‌تونید لینک‌های اشتراک SOCKS4 و SOCKS5 رو هم مستقیماً وارد برنامه کنید.
🔸
بهبود نوتیفیکیشن سرعت: نمایش سرعت در نوار اعلان‌ها (Notification) حالا با ثبات و دقت بیشتری انجام می‌شه و از سیاست‌های جدیدِ نمایشِ وضعیت (مثل لیست گروه‌ها) هم پشتیبانی می‌کنه.
🔸
رفع باگ‌ها: مشکلات جزئی نسخه قبل برطرف شده تا پایداریِ اتصال بالاتر بره.
📥
لینک‌های دانلود مستقیم (نسخه 2.1.8):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_arm64-v8a.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_armeabi-v7a.apk
📱
نسخه Universal (اگر پردازنده گوشیتون رو نمی‌دونید):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_universal.apk
📌
#آپدیت
#معرفی_ابزار
#اندروید
#فیلترشکن
#نت_ملی
#v2rayNG
#Xray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5196" target="_blank">📅 00:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b104e89c3c.mp4?token=ribPJnIukSm0yf44MKxHalhUmPMuZ_8HKudnkICmVuKWamjCHYXEtQ-Lo--_yJv9fdD95xfmTpht6rmO6zyiXjmg2w4O-fyjhGsAhfMCfJp9_2imKMVWHH3zf5f9F2oxFMDCVKkmQAEk965gMGjp11PAebI3lzbrXscwjyUVUuFES43hoZuONZKmHoclYBzOeausJDLpRoyxvjcz2Jc3fuPiQQhjeWZE5LZfaWCldgPB_0JfltuGD2g25DWG-jAy15Xnu4wOui-WbGzIUNJYt1hMoS8zd4Mka3wrkBBV5XR4IFsurz2VBJsvxQRmooRezY21C84ezop8knago7VcRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b104e89c3c.mp4?token=ribPJnIukSm0yf44MKxHalhUmPMuZ_8HKudnkICmVuKWamjCHYXEtQ-Lo--_yJv9fdD95xfmTpht6rmO6zyiXjmg2w4O-fyjhGsAhfMCfJp9_2imKMVWHH3zf5f9F2oxFMDCVKkmQAEk965gMGjp11PAebI3lzbrXscwjyUVUuFES43hoZuONZKmHoclYBzOeausJDLpRoyxvjcz2Jc3fuPiQQhjeWZE5LZfaWCldgPB_0JfltuGD2g25DWG-jAy15Xnu4wOui-WbGzIUNJYt1hMoS8zd4Mka3wrkBBV5XR4IFsurz2VBJsvxQRmooRezY21C84ezop8knago7VcRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Sni spoof  ip : 104.19.229.21  sni : www.hcaptcha.com</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5195" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاینترنت آزاد</strong></div>
<div class="tg-text">Sni spoof
ip :
104.19.229.21
sni :
www.hcaptcha.com</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5194" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">لیست SNI ها برای اینکه روی یه دامین همه نریزن.
three-cust.hcaptcha.com, stats.hcaptcha.com, www.hcaptcha.com,u.hcaptcha.com.
tg.hcaptcha.com, primary.haptcha.com, pat-internal.hcaptcha.com, jobs.hcaptcha.com,
hmt-lucid-neumann.hcaptcha.com, dashboard.hcaptcha.com, cached-queries.hcaptcha.com,
billing.hcaptcha.com, assets.hcaptcha.com, api.hcaptcha.com, analytics-beta.hcaptcha.com,
accounts.hcaptcha.com, a.hcaptcha.com, 47dilm9.mqwaa.dns.army, rel-I.top,
www-canary.hcaptcha.com,tractionrec.hcaptcha.com,tp.hcaptcha.com,
three-cust-imgs.hcaptcha.com, temple-gates.hcaptcha.com, styler.hcaptcha.com,
past-issuer.hcaptcha.com, _ health-check.hcaptcha.com, exchange.hcaptcha.com, email.hcaptcha.com,
abeling-masters.hcaptcha.com, pre.hcaptcha.com, fantasia-assets.hcaptcha.com,
proxy.hcaptcha.com, loader.hcaptcha.com, i2.hcaptcha.com, hmt-pensive-torvalds.hcaptcha.com
chunker.hcaptcha.com, analytics.hcaptcha.com, hcaptcha.com, newassets.hcaptcha.com,
charlie.hcaptcha.com, js.hcaptcha.com, imgs3.hcaptcha.com, challenge-tasks.hcaptcha.com,
serverless.hcaptcha.com, imgs2.hcaptcha.com, imgs.hcaptcha.com, factored-cognition.hcaptcha.com,
hiding.men, cf-3.payun.men,_mit.hcaptcha.com, risk-prod-srv.hcaptcha.com,
pst-sample.ncaptcha.com, sentry.ncaptcha.com, nmt-eloquent-mclaren.hcaptcha.com,
hmt-elegant-rosalind.hcaptcha.com, demo.hcaptcha.com</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5193" target="_blank">📅 22:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دانلود همه کلاینت ها با لینک داخلی
http://Files.en-javadian.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5192" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لینک داخلی Happ ویندوز
دانلود</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5190" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMashaya</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pztblkf5ty6n-oq4mQ5xMNXBv8NEer2QXha7ZXDmVjTLg7tdN14xuCTJ9q9LmbbdVfIxAunBFS-3WG44foSOZYcS5a8vfq1_iEiP6WUPRiyoajlEke0_2iszGTHUXoEzsVAeGdEveuAd_CYJKqo1hqzDNNLOsgyVZsIraGrSAK-VPYoSkJo7hcQKuirKXAlD8yZmndxEY1dXi8L4p_3nnnuhENLVepIG8QS8Kqh8Hlz-5dDsDPCF70vGAfKpIB0_sWGuPA_3ShXgAmWXLRtJueiyz3rLUvuILRxf_OXxw1oGK8KfW6DBlxZyuk6gDXMLhLzX4_b8tTxf2_KEvHrDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rg54VtRg6GAG6CwpfJYkNq3yuDwfBSSyCUNmS6wLMFSdD6sSrmuSO3qxGhmv5hh7xCwLCXN4S1Qlq7_u18VaWXAhuNsgEszjuNCCTP-TbiFkawBVD7rEn5Qpl0yZu2QCzxotMEibWQi9GnrC-lIaTwIo7mjaC3BzZGXsJS3-hiKXJp0ps5LLiVP5vj5h1MEc6hUnY_nYTdEXWdBePwAzMnEUCIa2tiTrEC43Hg40D343C3fpZhaqBEq60-E2RZGHRT_Uznowj4iydJF3cwTtWzmkuVtvjTnxWN9tWAusz1eUKl7p1bxH1BPTVkTwfIz1AcczTm3-HIyTvRLWitssbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5XkQw4p1MDP3_zkBzVZiq2EANfh3DKm1ILZmqzY9kd-51E1bojcitRJDoi3spy4ZFR2PNzB-qGBVnN_tP7Y1_UYPrOoTv1NIpS2FREWbWb0Loe3MDRENUA5B2mNu1ZUcfmiDEV3inQvWvnv2_PSSCkXkd0BLXOIC6xyYqR9J2Hy0MIof04qn3WOKysl3vlSb9_Qhs6wDoVSQosHqzFr4iOcJTbaceEbPmGl82TrjER5Onx00z0xLpa9PMxjSxSKzWBW-1LSByHjrFyhOB6Mcv6BCI4aXgz05UkilLb8Vhov10jjpUsNTGFltB8gdfG5TrC5O67GeISGPBD5uqTPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3lq6M6heUwuBKbdZAlwjGfdxghSBpMGkaKfwO8jZG1uAP9tuwQUpWxqvAGd-YlC0cx2qyAx9W64oBX4wtXQ8N10sz_njgpE-j94LJAA_yejYpWUZ8fJWBf1z67z2TTlFCgNQwVleqDrVqGGRgkQJC7ht65FwwjGkjcXQn78nvZD_sJGqsW5qi19CWMkAHnr0vq2vtMI_AhXV9S7JExpUyFwU90JL-P1Sex4-MfNU8IswC2TGZzzRHhQ-V9uVwwegIbZTLWtyka0cavdQ5MfJU9sZVMMZH5qi1PJ72HK3RGwDogoEI5xtklsgTVASibr54fAN8q3EsWwZcHEOkekzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMDQnd3HiwEYOON_BscbOEZOsTT0m3dFBn5zoTVTq-oIDvdmCzLovUsw9Q936fj0BowJEseBkSlZu3M567mm-j8-pUMnXSg_PMXzfwP3DY1BZBt3ePSEukhrR6ytFWQ1rnYFAVFO-E4BIeryUQ7zAPdPuuHAM_bgBNSZGSdaxRRYDTxtzJ1k_nWepKRWlZ71OeG93pf_YZvsxS-FJcrRAoph2pbn0UTriTqPLw-SZcyJx2_D0fwkkUyrNi_ayEnJ-XLn4uc_lmXQhmeheQ0hvt_XhHZ5Sb8ciVqYgWHQeUhPhMhTRvY0ca05oxBUtGo-uI97bEOaxgyGsdAiBdZ54w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من تونستم با sni ، گوشیمو به کامپیوتر وصل کنم (اصلا نمیتونستم با ویتوری وصل شم)
برای کمک کسایی که میخوان نت کامپیوترو به گوشی بدن
من از اینترنت ایرانسل استفاده کردم
برنامه ی happ به جای کلاینت v2ray توی کامپیوتر استفاده میکنم . هم توی ویندوز و هم توی گوشی بهش نیاز داریم
دقیقا مثل ویتوری ، کانفینگارو توی قسمت سرور ها اد می کنیم ، بعد از اینکه sni رو فعال می کنیم و پینگ میگیریم که ببینیم کدوم فعالن به بخش سیتینگ اپ هپ میریم
(عکس اول) اگه اسکرول کنید تا اخر میبینید یه گزینا نوشته allow connection from lan
اونو فعال می کنید
ای پی و پورت هاتونو که دقیق نوشته چیا هست
(عکس دوم) فقط باید دقت کنید توی قسمت ویدندزو فایروالتون حتما برنامه ی هم رو تعریف کرده باشید
مسیرش هم کنترل پلن ، سیستم و سکیورتی   ویندوز دیفندر فایروال و الود اپز
اول چینج سیتینگ رو می زنید بعد الو انادر اپ
و هپ رو اضافه می کنید
حتما حواستون باشه که دوتا تیکارو بزنید
(عکس سوم و چهارم) بعد اون میاید توی برنامه ی هپ گوشیتون
رو اون مثبت بالا سمت راست می زنید
منوال manual input
بعدش socks
(عکس پنجم) بعد یه صفحه براتون درست میکنه
اسم رو هرچی میخواید می زنید
اینجا نوشته server address
این سرور ادرس رو دقیقا همون ای پی ای که توی هپتون ، توی ویندوز براتون زده رو مینویسید
و port رو هم ، ببینید عددی که هپتون توی ویندوز نوشته جلوی SOCKSS proxy port چی هست . همونو می نویسید
و در اخر وصل می شید
✨</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5185" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤ</strong></div>
<div class="tg-text">هر ایرانی اندازه دو ترم راه اتصال به اینترنت رو تو این هشتاد روز پاس کردن</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5184" target="_blank">📅 21:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein</strong></div>
<div class="tg-text">چقد سختش میکنید اول سیستمو متصل کنید بعدش برید تو cmd تایپ کنید ipconfig بعدش برید ipv4 رو کپی کنید  بعدش همون کانفیگی که رو لپ تاپ متصلید رو داخل v2rayng یا v2box کپی کنید گزینه ویرایش بزنید به جای 127.0.0.1 اون ipv4 رو پیست کنید تمام</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5183" target="_blank">📅 21:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein</strong></div>
<div class="tg-text">چقد سختش میکنید اول سیستمو متصل کنید بعدش برید تو cmd تایپ کنید ipconfig بعدش برید ipv4 رو کپی کنید
بعدش همون کانفیگی که رو لپ تاپ متصلید رو داخل v2rayng یا v2box کپی کنید گزینه ویرایش بزنید به جای
127.0.0.1
اون ipv4 رو پیست کنید تمام</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5182" target="_blank">📅 21:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش اشتراک‌گذاری اینترنت آزاد (V2ray/SNI-Spoofing) از لپ‌تاپ به گوشی
اگ
ر روی لپ‌تاپ خود با ابزارهایی مثل SNI-Spoofer یا V2ray به اینترنت آزاد وصل هستید با این روش می‌توانید همان اینترنت بدون فیلتر را به گوشی خودتان برگردانید:
مرحله ۱: فعال کردن LAN در لپ‌تاپ
در برنامه v2rayN روی لپ‌تاپ، از پایین صفحه تیک گزینه
Allow connections from LAN
را بزنید. پورت SOCKS نوشته شده در پایین صفحه (معمولاً 10808 یا 10809) را به خاطر بسپارید.
مرحله ۲: پیدا کردن آی‌پی لپ‌تاپ
۱. در ویندوز برنامه
CMD
را باز کنید.
۲. عبارت ipconfig را تایپ کرده و اینتر بزنید.
۳. عدد روبروی
IPv4 Address
را یادداشت کنید.
مرحله ۳: باز کردن پورت در فایروال ویندوز
برای اینکه ویندوز جلوی اتصال گوشی را نگیرد:
۱. برنامه
PowerShell
را جستجو کنید، روی آن راست‌کلیک کرده و
Run as Administrator
را بزنید.
۲. دستور زیر را کپی و پیست کرده و اینتر بزنید (اگر پورت V2ray شما در مرحله اول چیز دیگری بود، عدد 10808 را در این کد تغییر دهید):
New-NetFirewallRule -DisplayName "V2Ray LAN" -Direction Inbound -LocalPort 10808 -Protocol TCP -Action Allow
مرحله ۴: اتصال در گوشی
۱. در گوشی خود برنامه
v2rayNG
را باز کنید.
۲. روی علامت
+
(بالا سمت راست) بزنید و
Type SOCKS
(یا Add a Socks profile) را انتخاب کنید.
۳. در قسمت
Address
: آی‌پی لپ‌تاپ (که در مرحله ۲ پیدا کردید) را وارد کنید.
۴. در قسمت
Port
: پورت لپ‌تاپ (مثلاً 10808) را وارد کنید.
۵. کانفیگ را ذخیره کنید و دکمه اتصال را بزنید.
@ArchiveTell
@NET_SPOOF</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5181" target="_blank">📅 21:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3040ff2528.mp4?token=TCVu8a53CtrG5QEuWIFNHC0QfWSqr_j5aZlxlFzUxSirO1ddQi90SW3AAFDGu9JEQJwtyv1FJmAZ6yYL5Ub_GVjdvWw5CoFZF6yEyx_F_QZacLL5y0nCHLatzjwYA8wixEpQJt-v_o_9irMnXbAS0PNOaU2LQLV6jgo8-kktgNq2a9m2w0_UlyG9JQ2Fbx7_gUA6sdr5UWETH6xkCKe9VrviLaeSFm2TYhcehSbt6--E5J46Nc3_zTFOY30GyY8aW-DOVqpvAaSD2r00OYUGFcpaSRQxaPVh600jPty2lRVqVZhbPfeIL4frP7h-0a3uIGyffNhzW1cro_RyZqJEFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3040ff2528.mp4?token=TCVu8a53CtrG5QEuWIFNHC0QfWSqr_j5aZlxlFzUxSirO1ddQi90SW3AAFDGu9JEQJwtyv1FJmAZ6yYL5Ub_GVjdvWw5CoFZF6yEyx_F_QZacLL5y0nCHLatzjwYA8wixEpQJt-v_o_9irMnXbAS0PNOaU2LQLV6jgo8-kktgNq2a9m2w0_UlyG9JQ2Fbx7_gUA6sdr5UWETH6xkCKe9VrviLaeSFm2TYhcehSbt6--E5J46Nc3_zTFOY30GyY8aW-DOVqpvAaSD2r00OYUGFcpaSRQxaPVh600jPty2lRVqVZhbPfeIL4frP7h-0a3uIGyffNhzW1cro_RyZqJEFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">HashemVasel_2.0.0_x64_en-US.msi</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5180" target="_blank">📅 20:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HashemVasel_2.0.0_x64_en-US.msi</div>
  <div class="tg-doc-extra">86.5 MB</div>
</div>
<a href="https://t.me/archivetell/5179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید HashemVasel به‌صورت کامل بازسازی شده و حالا با رابط کاربری جدید، عملکرد پایدارتر و مدیریت اتصال دقیق‌تر ارائه می‌شود. در این نسخه قابلیت SNI Spoof اضافه شده تا اتصال‌ها بهتر و حرفه‌ای‌تر مدیریت شوند، وضعیت Core و اتصال واقعی شفاف‌تر نمایش داده می‌شود، کنترل سرویس‌ها و System Proxy بهبود پیدا کرده و بخش‌های داشبورد، تنظیمات، لاگ‌ها و صفحه درباره برنامه ساده‌تر و کاربردی‌تر شده‌اند. همچنین مشکلات نسخه‌های قبلی در اجرای سرویس‌ها، تشخیص وضعیت اتصال، بسته‌بندی برنامه و راه‌اندازی Core برطرف شده تا تجربه استفاده روان‌تر، مطمئن‌تر و قابل‌فهم‌تری داشته باشید.
- شب نسخه کامل شده رو میدم، امیدوار باشیم وصل بمونه.
لینک دانلود داخلی:
https://guardts.ir/f/058a7e797803</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5179" target="_blank">📅 20:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3zcJCCoBAE5NSME0a8OfZaQvuG2PwAJN6LhgOZbOe6mHzSc-b6n3KKqJfe1VADVuKa91T7XoEhn0zqukeQBA-DAkenHR-AyWqxiAntIhv6J9ihB7kK8I59yGsbHAPUj0nK6pUFb4xctIwLu_SfPvjbdyG2yGx1-3uzctF0mkO30X5OQg7AbgSfPEZXZnpx9cVlOjXfFJ65rI3b5MohHJjZqsN_TUalEZAzFKd0c-H67fi2e0jpoLwDmdBlFsxMemoj4Ex1u2dFn92QQl6UvSOY9D2RNw-S5xNGLkF53_W_xb50M96e7pGZG76vCpSXGDhufMeurAjPbuhJ4lPyMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfEnT4Wbku-g8cbtLuh1o5sYSiFYY6YAUKoRMCzQAl89hYNY6cxbw8v-dAc8WIhz5RUWnwIZjuur9mgog6sCTz8acsH2xYb7u2ZZ0tpztfp0Dg3MBpTib6fLwmpRw1B9PTLvY5PQ5KelbnpDhSdmauXdHXPV3HEKO2ZHfJYCJZcyhBnom9kHkHM5NGqOIsVQ4yzEbAVngrzqfN356Nh3rU6QTT_cKUXsq6mBTPC6ik_Kl_9um8eP7Ij2SmJO8_nPDaQNvzXdvs84J21-dZOc0-PHgCRnBoNiHROtzfUw0tN8JdZhz3cXEcgmuL_Y7-s2p3xr7HxPVrGx6stliZhv-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیفیت کانفیگای چنل
موجودی محدود
تضمینی ، سرعت بالا و پایدار
قیمت عالی
@ArchiveTellbot
آموزش خرید</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5177" target="_blank">📅 19:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚀
معرفی ابزار NexaTunnel: مدیریت هوشمند و مانیتورینگ کانفیگ‌ها در iOS
---
رفقا سلام!
✋
برای کسایی که توی آیفون/آیپد دنبال یک کلاینت تمیز، مدرن و حرفه‌ای برای مدیریت پروفایل‌های تونل (Tunnel) هستن، اپلیکیشن جدید
NexaTunnel
گزینه بسیار خوبیه.
این برنامه در واقع یک «داشبورد مانیتورینگ و مدیریت» هست که بهتون اجازه میده به‌راحتی کانفیگ‌های مختلف رو وارد و بین اون‌ها سوئیچ کنید.
✨
ویژگی‌های کلیدی NexaTunnel:
🔸
مدیریت حرفه‌ای کانفیگ‌ها: امکان وارد کردن (Import)، خروجی گرفتن (Export)، کپی کردن و سوییچ سریع بین چندین پروفایل.
🔸
مانیتورینگ زنده (Live Traffic): نمایش آنی سرعت آپلود/دانلود، پینگ لحظه‌ای، آی‌پی عمومی و وضعیت سلامت تونل.
🔸
تست هوشمند DNS: قابلیت تست و انتخاب بهترین ریزالور (DNS) برای شبکه فعلی شما.
🔸
امنیت و حریم خصوصی: تمام کانفیگ‌ها روی خودِ گوشی باقی می‌مونن و مقادیر حساس در لاگ‌ها ماسک می‌شن.
🔸
رابط کاربری مدرن: پشتیبانی از دارک‌مود/لایت‌مود و طراحی بسیار مینیمال و کاربرپسند.
⚠️
نکته مهم:
نکسا‌تونل خودش سرور یا سرویس VPN داخلی نداره! این برنامه فقط یک «کلاینت» هست و شما باید فایل کانفیگِ سازگار (که از قبل دارید) رو داخلش وارد کنید تا بتونید متصل بشید.
📥
لینک دانلود از اپ‌استور (مخصوص آیفون و آیپد):
🔗
https://apps.apple.com/us/app/nexatunnel/id6766783641
📌
#معرفی_ابزار
#آیفون
#آی_او_اس
#نت_ملی
#تونل
#NexaTunnel
#iOS
#VPN_Client
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5176" target="_blank">📅 18:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سلام چن روزه نبودم
میگن نتفلای شاشبند میکنه راسته؟</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5175" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">thefeed-android-v0.19.0-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5174" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.19.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/archivetell/5173" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید TheFeed (v0.19.0)
این نسخه چندتا تغییر داشته که انتظار میره سرعت برنامه بیشتر بشه
🔸
برنامه تلاش میکنه تا کوئری هایی که میفرسته سمت ریزالور ها رو جوری بسازه که شکل کوئری بقیه کاربرها که در همون لحظه دارن از برنامه استفاده میکنن بشه!، اینجوری اگر چند نفر هم زمان با یک کانفیگ‌ و ریزالور مشترک درحال گرفتن یک کانال یکسان باشن، سرعت چند برابر میشه، چون ریزالور یکبار دیتا رو از سرور میگیره و با سرعت زیاد به دست همه کاربر ها میرسونه! ،هنوز نمیدونم در عمل چقدر ممکنه این شرایط پیش بیاد که چند نفر با یک ریزالور یکسان یک کانال یکسان رو بگیرن! و البته اگر‌ بخواید میتونید این قابلیت رو از تنظیمات غیرفعال کنید
🔸
توی این نسخه جدید برنامه سعی میکنه بلاک های متادیتا رو بصورت هم زمان بگیره تا عملیات گرفتن پست های کانال ها سریع تر شروع بشه (اون مکس اولیه که قبل از شروع گرفتن پیام های کانال ها میبینید سریع تر میشه)
🔸
ظاهر تنظیمات بهتر شده و تنظیمات دسته بندی شده (یک سری از تنظیماتی که قبلا توی کانفیگ بود هم به این بخش منتقل شده، مثل تعداد هم زمانی کوئری ها و ...)
🔸
قابلیت فول اسکرین کردن ویدیو ها
🔸
نشون دادن هش فایل ها توی گیتلب
🦠
رفع باگ دکمه ریست امتیاز ریزالور ها
🦠
رفع مشکل تغییر سایز فونت در iOS ( نسخه جدید واسه iOS هنوز رلیز نشده و فعلا نمیتونید آپدیت کنید!)
📯
من نسخه اندروید arm8a رو توی این کانال میزارم و اگر نسخه های دیگه رو میخواید باید از گیتلب و یا کانال زیر دانلود کنید (ویندوز، مک، لینوکس، بی‌اس‌دی، اندروید arm7a و حتی ترموکس):
📦
@thefeedfile
🔗
https://gitlab.com/sartoopjj/thefeed
🔐
SHA256:
d2b10e3d16d3d07662c7010aa28495a2936e3a281b92c459b6d93efcaf95fb59
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ هایی دفید:
@thefeedconfig</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5173" target="_blank">📅 14:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
ورژن آخر اپلیکیشن محبوب v2rayNG (نسخه 2.1.7)
---
یکی از بهترین و پرکاربردترین کلاینت‌های اندروید برای دور زدن فیلترینگ، یعنی v2rayNG، یه آپدیت جدید و پر از امکانات خفن داده بیرون که پیشنهاد می‌کنم حتماً نصبش کنید.
⚡️
مهم‌ترین تغییرات نسخه جدید (v2.1.7):
🔸
قابلیت Chain Proxy (پروکسی زنجیره‌ای): بالاخره این قابلیت جذاب اضافه شد تا بتونید ترافیک رو از چند سرور مختلف عبور بدید.
🔸
سیستم روتینگ پیشرفته برای پروسه‌ها: حالا می‌تونید (تو اندروید ۱۰ به بالا و با روشن بودن TUN) مشخص کنید که دقیقاً کدوم اپلیکیشن‌ها (از طریق نام پکیجشون) از VPN رد بشن یا نشن!
🔸
رمزگذاری روی SOCKS: اضافه شدن پشتیبانی از یوزرنیم و پسورد برای لوکال ساکس.
🔸
میانبرهای سریع (Shortcuts): اضافه شدن شورت‌کات به آیکون برنامه برای روشن/خاموش کردن سریعِ اتصال.
🔸
تنظیمات جدید برای IPv6 و SOCKS5 (مثل بستن UDP).
🔸
و البته آپدیت هسته Xray به آخرین نسخه (v26.5.9).
📥
دانلود مستقیم (از گیت‌هاب سازنده):
با توجه به نوع پردازنده گوشیتون یکی از فایل‌های زیر رو دانلود کنید (برای اکثر گوشی‌های جدید، نسخه اول یعنی
arm64-v8a
مناسبه):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_arm64-v8a.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_armeabi-v7a.apk
📱
نسخه Universal (اگر نمی‌دونید پردازنده گوشیتون چیه، این نسخه روی همه نصب می‌شه - حجمش کمی بیشتره):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_universal.apk
📌
#آپدیت
#معرفی_ابزار
#اندروید
#فیلترشکن
#نت_ملی
#v2rayNG
#Xray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5172" target="_blank">📅 14:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اشتراک گذاری متد اسپوف از سیستم رو گوشی
تو سیستم ipv4 رو پیدا کن بزا جای آدرس کانفگیت بعدش کلیک راست کن روی کانفیگی که توی سیستم وصلی گزینه share بزن یه بارکد بهت میده با گوشی v2box یا بقیه کلاینت ها وصل شو</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5171" target="_blank">📅 14:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5170" target="_blank">📅 13:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای مک از ازین ریپو هم میتونید استفاده کنید
https://github.com/selfishblackberry177/sni-spoof/releases/
1. فایل دانلودی رو با config.json داخل یه دایرکتوری بگذارید
2. داخل ترمینال cd بزنید و دایرکتوری رو بیارید
3. sudo ./sni-spoof-darwin-arm64 config.json</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5169" target="_blank">📅 13:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🍷
ورژن Python برای SNI Spoofing:
https://github.com/patterniha/SNI-Spoofing
ورژن Rust برای SNI Spoofing:
https://github.com/therealaleph/sni-spoofing-rust
ورژن Go برای SNI Spoofing:
https://github.com/aleskxyz/SNI-Spoofing-Go
ورژن اپ مک برای Sni spoofing:
https://github.com/g3ntrix/Cloak
👑
@ArchiveTell
💎
@xsfilterrnet</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5168" target="_blank">📅 13:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
معرفی ابزار FakeSNI: دور زدن فیلترینگ با تزریق SNI فیک (مخصوص لینوکس)
---
رفقا سلام!
✋
در پیرو پست قبلی که درباره مستقیم شدن دامنه hCaptcha و روش SNI Spoofing صحبت کردیم، حالا وقتشه یه ابزار عالی برای پیاده‌سازی این متد روی سیستم‌عامل لینوکس معرفی کنیم.
پروژه
FakeSNI
یه نسخه بازنویسی‌شده، سریع و بسیار تمیز از پروژه معروف
patterniha
هست که با زبان Go نوشته شده.
🔥
این ابزار چطور فیلترینگ رو دور می‌زنه؟
این برنامه روی لینوکس یه پروکسی TCP می‌سازه. دقیقاً بعد از اینکه دست‌دادنِ اولیه (TCP Handshake) با سرور انجام شد، این ابزار یه بسته حاوی
ClientHello
با یک SNI فیک (همون دامنه‌ای که فیلتر نیست مثل
hcaptcha.com
) رو به بیرون تزریق می‌کنه.
چون شماره توالی (Sequence Number) این بسته عمداً دستکاری شده، سرورِ مقصد اون رو دور می‌ندازه؛ اما سیستم فیلترینگ (DPI) وسط راه گولِ همون بسته رو می‌خوره، فکر می‌کنه سایت مجازی رو باز کردید و مسیر رو برای دیتای اصلیِ شما باز می‌ذاره!
🤯
🛠
پیش‌نیازها برای اجرای ابزار:
🔸
سیستم‌عامل لینوکس (Ubuntu, Debian و غیره)
🔸
داشتن دسترسی روت (Root)
🔸
فعال بودن
iptables
روی سیستم (که معمولاً روی همه لینوکس‌ها هست).
💻
نحوه استفاده خیلی ساده:
۱. سورس برنامه رو از گیت‌هاب دانلود یا بیلد کنید.
۲. یه فایل به اسم
config.json
بسازید و دقیقاً مثل پست قبلی، تنظیمات آی‌پی و SNI فیک رو توش قرار بدید.
۳. ابزار رو با دسترسی روت و دستور زیر اجرا کنید:
sudo ./fakesni -config config.json
(نکته: این ابزار خودش به صورت خودکار رول‌های iptables رو تنظیم و بعد از بسته شدن پاک می‌کنه).
🔗
لینک سورس کد و توضیحات کامل در گیت‌هاب سازنده:
🌐
https://github.com/PechenyeRU/FakeSNI
📌
#معرفی_ابزار
#لینوکس
#فیلترینگ
#اسنیف
#FakeSNI
#SNI_Spoofing
#DPI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5167" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تعدادی کانفیگ واسه متد sni
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#1
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#2
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#3
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#4
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#5
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#7</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5166" target="_blank">📅 08:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5165" target="_blank">📅 08:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب hcaptcha رو مستقیم کردند، اگه: https://www.hcaptcha.com/cdn-cgi/trace  ایپی خودتونو داد یعنی رو نت شمام مستقیم کردن. {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/archivetell/5164" target="_blank">📅 02:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این لینکو بدون وی پی ان باز کنید اگه باز میشه اسپوف هم وصل میشه
https://www.hcaptcha.com/cdn-cgi/trace</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5163" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing.zip</div>
  <div class="tg-doc-extra">131.4 KB</div>
</div>
<a href="https://t.me/archivetell/5162" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">spoof
mac os</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5162" target="_blank">📅 02:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم اسکریپت XHTTP-Installer (تونل نتلیفای و ورسل)
🤯
---  با محدودیت‌های شدید اخیر، اتصال مستقیم به سرورهای خارج خیلی سریع باعث فیلتر شدن آی‌پی می‌شه. اما با اسکریپت فوق‌العاده‌ و ایرانیِ XHTTP-Installer، ترافیک سرور شما پشت سرویس‌های…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/archivetell/5161" target="_blank">📅 01:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
معرفی NovaProxy: عبور از فیلترینگ با ترکیب Google و Cloudflare
🤯
---
یه پروژه دسکتاپیِ به‌شدت خفن و مهندسی‌شده به اسم NovaProxy اومده که با استفاده از تکنیک Domain Fronting، ترافیک اینترنت شما رو دور از چشم فیلترینگ جابه‌جا می‌کنه.
🔥
این ابزار دقیقاً چیکار می‌کنه؟
وقتی NovaProxy رو روشن می‌کنید، سیستم فیلترینگ فقط می‌بینه که شما در حال تبادل دیتا با
www.google.com
هستید! اما در واقع، ترافیک شما از طریق سرورهای گوگل به یه اسکریپت (Apps Script) فرستاده می‌شه، از اونجا می‌ره تو کلادفلر ورکر (Worker)، و بعدش سایتِ فیلترشده‌ای که می‌خواید رو براتون باز می‌کنه.
این روش برای وب‌گردی عالیه و سایت‌هایی مثل تلگرام وب یا یوتیوب رو خیلی روون باز می‌کنه (البته تلگرامِ خود ویندوز فعلاً با این روش کار نمی‌کنه و این ابزار مخصوص مرورگرهاست).
🛠
آموزش راه‌اندازی (مرحله‌به‌مرحله):
1️⃣
مرحله اول: ساخت Cloudflare Worker
۱. برید تو سایت کلادفلر و بخش Workers & Pages. یه ورکر جدید (Hello World) بسازید.
۲. کد فایل
worker.js
(موجود در پوشه server گیت‌هاب) رو تو ورکری که ساختید پیست کنید.
۳. در کدها، خطی که نوشته
WORKER_URL
رو پیدا کنید و آدرس ورکری که خودتون ساختید رو به جاش بذارید و Deploy کنید.
2️⃣
مرحله دوم: ساخت Google Apps Script
۱. برید تو سایت
script.google.com
و روی New project کلیک کنید.
۲. کد فایل
Code.gs
رو اونجا پیست کنید.
۳. دو متغیر
AUTH_KEY
(یه رمز دلخواه قوی براش بذارید) و
WORKER_URL
(آدرس همون ورکر کلادفلری که تو مرحله قبل ساختید) رو تو کد جایگزین کنید.
۴. از بالا Deploy ➔ New deployment رو بزنید. نوعش رو روی Web app و دسترسی رو روی Anyone بذارید و دیپلوی کنید تا یه Deployment ID (شبیه AKfy...) بهتون بده.
3️⃣
مرحله سوم: راه‌اندازی نرم‌افزار NovaProxy
۱. برنامه
novaproxy.exe
رو دانلود و نصب کنید. تو همون مرحله اول یه پاپ‌آپ میاد که باید گواهی (Certificate) رو تایید و نصب کنید.
۲. تو تنظیمات، کشور رو روی Iran بذارید.
۳. برید تو بخش پروکسی و اون ۳ تا مقداری که ساختید (Auth Key، Script ID و Worker URL) رو وارد و ذخیره کنید.
۴. تو صفحه داشبورد، اول پروکسی و پروکسی سیستم رو روشن کنید، بعد کلید GSA رو فعال کنید تا وب‌گردی آزاد براتون استارت بخوره!
📥
دانلود برنامه و کدهای مورد نیاز:
کدهای مراحل اول و دوم، و همچنین فایل نصبی خود برنامه رو می‌تونید مستقیماً از صفحه رسمی گیت‌هابِ پروژه بردارید:
🔗
https://github.com/IRNova/Nova-Proxy-App
📌
#معرفی_ابزار
#نوا_پروکسی
#گوگل
#کلادفلر
#دامین_فرانتینگ
#نت_ملی
#NovaProxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/archivetell/5160" target="_blank">📅 00:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">config.json</div>
  <div class="tg-doc-extra">150 B</div>
</div>
<a href="https://t.me/archivetell/5159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5159" target="_blank">📅 00:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing_by_patterniha_v1.zip</div>
  <div class="tg-doc-extra">9.8 MB</div>
</div>
<a href="https://t.me/archivetell/5158" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل برنامه رو ران از ادمین کنید و در v2ray وصل بشید به این
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&fp=chrome&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#ArchiveTel</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/archivetell/5158" target="_blank">📅 00:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-text">خب hcaptcha رو مستقیم کردند، اگه:
https://www.hcaptcha.com/cdn-cgi/trace
ایپی خودتونو داد یعنی رو نت شمام مستقیم کردن.
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
///
104.19.229.21
,
104.19.230.21
///
ولی sni-spoofing رو یه سری از نت ها کامل وصله، یکسری کنده و یکسری قطعه احتمالا بلایی سرش آوردن یا صرفا ip رو کند کردن. در حال بررسی هستم ...
///
خود سایتشم بسیار کند بالا میاد فعلا حالت عادیشم بسیار کند هستش.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5157" target="_blank">📅 00:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718e643c7.mp4?token=EMFxerORbgi6dLovThYf7WtvnEIzg68-mbP2dAftyQsSUD4oagDdCAQ9T3aMxY05-UImvKIR-ModD4hGD6QsKCKBC-INv8TTqZ_RZHhzs-s6remhswRRyojwHGk88fjyi745BDJCHoqxsZlQYJOyl90R4RuWPbDvPW61aNGcHhy5cgKlE0mE4KwUeyovozHhRNgy1eNaOfbxhUUf6phFVxzgwJMcJRAcWCloEdp9OiSSe---0xBWXm6JmpyZQd0Zp2StdLlD-xddtVclXckrRZhdw6TexYQ09aDm9H3y2HSJU7L6QgRjdqUWkMGFxkLZEga9dyZUFNVVNWtQ-UoAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718e643c7.mp4?token=EMFxerORbgi6dLovThYf7WtvnEIzg68-mbP2dAftyQsSUD4oagDdCAQ9T3aMxY05-UImvKIR-ModD4hGD6QsKCKBC-INv8TTqZ_RZHhzs-s6remhswRRyojwHGk88fjyi745BDJCHoqxsZlQYJOyl90R4RuWPbDvPW61aNGcHhy5cgKlE0mE4KwUeyovozHhRNgy1eNaOfbxhUUf6phFVxzgwJMcJRAcWCloEdp9OiSSe---0xBWXm6JmpyZQd0Zp2StdLlD-xddtVclXckrRZhdw6TexYQ09aDm9H3y2HSJU7L6QgRjdqUWkMGFxkLZEga9dyZUFNVVNWtQ-UoAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم اسکریپت XHTTP-Installer (تونل نتلیفای و ورسل)
🤯
---
با محدودیت‌های شدید اخیر، اتصال مستقیم به سرورهای خارج خیلی سریع باعث فیلتر شدن آی‌پی می‌شه. اما با اسکریپت فوق‌العاده‌ و ایرانیِ XHTTP-Installer، ترافیک سرور شما پشت سرویس‌های قدرتمندی مثل Netlify یا Vercel مخفی می‌شه!
🔥
با بررسی دقیق آموزش‌های ویدیویی این پروژه، راهنمای صفر تا صد اون رو براتون آماده کردیم:
🛠
مرحله ۱: تنظیمات دامنه (Cloudflare)
۱. وارد اکانت کلادفلر بشید و به بخش DNS برید.
۲. یه رکورد جدید از نوع A بسازید. در بخش Name یه اسم دلخواه (مثلاً test) بدید و در بخش IPv4، آی‌پی سرور مجازیتون رو وارد کنید.
۳.
⚠️
به‌شدت مهم: تیک پروکسی (ابر نارنجی) رو حتماً خاموش کنید تا خاکستری (DNS Only) بشه و Save رو بزنید. (یکی دو دقیقه صبر کنید تا ست بشه).
💻
مرحله ۲: اجرای اسکریپت در سرور
۱. به سرور لینوکسی خودتون SSH بزنید.
۲. کد زیر رو کپی و اجرا کنید:
bash <(curl -fsSL https://raw.githubusercontent.com/avacocloud/XHTTP-Installer/main/install.sh)
۳. اسکریپت می‌پرسه رو حالت screen اجرا بشه؟ (کلید n رو بزنید).
۴. حالا می‌پرسه رو کدوم پلتفرم می‌خواید دیپلوی کنید؟ عدد 1 (ورسل) یا 2 (نتلیفای) رو انتخاب کنید.
⚙️
مرحله ۳: پاسخ به سوالات اسکریپت
اسکریپت چندتا سوال می‌پرسه که باید این‌طوری جواب بدید:
🔸
دامین: همون ساب‌دامنه‌ای که تو کلادفلر ساختید رو کامل وارد کنید (مثلاً
test.yoursite.com
).
🔸
ایمیل: یه ایمیل معتبر وارد کنید.
🔸
پورت و مسیر (Path): دست نزنید و فقط Enter بزنید تا همون پیش‌فرض بمونه.
🔸
توکن (Token): توکنی که از پنل Vercel یا Netlify گرفتید رو اینجا Paste کنید.
🔸
اسم پروژه: Enter بزنید تا خودش رندوم بسازه. (برای ورسل ممکنه تنظیمات پرفورمنس هم بیاد که باز همون Enter رو بزنید).
در نهایت y بزنید و صبر کنید تا عملیات ساخت و تست کانفیگ تموم بشه و لینک vless رو بهتون بده.
📱
مرحله ۴: اتصال در کلاینت (ترفندهای طلایی)
🟢
برای کاربران ورسل (Vercel):
لینک رو تو کلاینت (مثل v2rayNG) وارد کنید. برای اینکه پینگ بده، فیلد Address (یا همون آی‌پی) رو پاک کنید و یکی از این دو آی‌پی وایت‌لیست و بدون فیلتر رو جاش بذارید:
198.169.2.1
198.169.2.65
🔵
برای کاربران نتلیفای (Netlify):
اگر کانفیگ خام پینگ نداد، برید تو ربات تلگرامی
@verceltoken_bot
، از بخش Config Builder گزینه Netlify و سپس Mix mode رو انتخاب کنید. کانفیگتون رو بهش بدید تا یه فایل متنی حاوی ده‌ها ترکیب SNI و IP بهتون بده. همه‌رو تو کلاینت تست پینگ بگیرید و هرکدوم وصل شد از همون استفاده کنید!
📥
ویدیوها و سورس کد اصلی:
▶️
ویدیو آموزش نتلیفای:
https://youtu.be/B-As6aZSiMA
▶️
ویدیو آموزش ورسل:
https://youtu.be/yz2gLxTeWGE
💻
سورس کد در گیت‌هاب:
https://github.com/avacocloud/XHTTP-Installer
(طراحی اسکریپت توسط
@avaco_cloud
و آموزش ویدیویی از AmirS
🤍
)
📌
#آموزش
#اسکریپت
#نتلیفای
#ورسل
#نت_ملی
#XHTTP
#Vercel
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5156" target="_blank">📅 00:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">vless://557ad0d8-5a72-48e4-9408-10c04f1c7347@198.169.2.1:443?encryption=none&security=tls&sni=relay-arb3pb5l.vercel.app&fp=chrome&alpn=h2%2Chttp%2F1.1&insecure=0&allowInsecure=0&type=xhttp&host=relay-arb3pb5l.vercel.app&path=%2Fapi&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D#%40IR_NETLIFY-XHTTP-vercel
vless://557ad0d8-5a72-48e4-9408-10c04f1c7347@198.169.2.65:443?encryption=none&security=tls&sni=relay-arb3pb5l.vercel.app&fp=chrome&alpn=h2%2Chttp%2F1.1&insecure=0&allowInsecure=0&type=xhttp&host=relay-arb3pb5l.vercel.app&path=%2Fapi&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D#%40IR_NETLIFY-XHTTP-vercel</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5155" target="_blank">📅 00:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">😂
ورسل وصل شد</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5153" target="_blank">📅 00:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ربات Music Tool بهترین ربات برای مدیریت آسان فایل‌های موسیقی شماست!
🎵
✨
@MusicToolBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5152" target="_blank">📅 23:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
آپدیت جدید جعبه‌ابزار Network Checker منتشر شد (نسخه v0.6.0)
---
اپلیکیشن همه‌کاره و فوق‌العاده‌ی Network Checker که قبلاً تو کانال معرفیش کرده بودیم، یه آپدیت داغ و به‌شدت کاربردی داده بیرون.
⚡️
تغییرات مهم این نسخه (v0.6.0):
🔸
اضافه شدن اسکنر اختصاصی آکامای: دیگه نیازی به اسکریپت یا برنامه‌های جانبی نیست؛ اسکنر آی‌پی آکامای (Akamai IP Scanner) مستقیماً به خود برنامه اضافه شده!
🔸
کانفیگ‌ساز Netlify: یه قابلیت جدید و خفن (Netlify Config Generator) برای ساخت کانفیگ به برنامه اضافه شده.
🔸
بهبود اسکنر دامنه (Domain Scanner): لیست دامنه‌های پیش‌فرض برای اسکن، آپدیت و بهینه‌سازی شدن تا خروجی‌های کاربردی‌تری بهتون بدن.
📥
لینک‌های دانلود مستقیم برای اندروید (نسخه 0.6.0):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-arm64-v8a-release.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-armeabi-v7a-release.apk
📱
نسخه Universal (اگر نمی‌دونید پردازنده گوشیتون چیه، این نسخه روی همه نصب می‌شه):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-release.apk
(برای دانلود نسخه‌های آپدیت‌شده‌ی ویندوز و لینوکس می‌تونید به صفحه گیت‌هاب پروژه مراجعه کنید).
📌
#آپدیت
#معرفی_ابزار
#اسکنر
#نتورک_چکر
#آکامای
#نت_ملی
#Network_Checker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5151" target="_blank">📅 22:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5150" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/te0t4k_QRCpNDd2YaVw4qk1Km2sei7JU2-gOaE-qYriKZ88T388kJ42tXXFOFjUobT3hbB9eZhj8cQLYP_odS1CoYLTV_Cv-6RWMLN85OIpyYPoYF36A3MRTjnv3oXtmCgrI5I21n2MJSndb5Wy50-rxdXIAVC7uFY_02exw6nTQk2Fa2Hk3nqh3kI8xV72rEN38O6SM_bsWVmrnzH7vRjH94hBXYmA_NG4VBoUi5-9o_AkiEsrRC5XLlNu1qt6QlFaOJfElf_w1FcPNjkMOzaFXvU5SK1s5ea1Q3y4xX5vIJ0FBrhjYHatvVKnH9a8IBYBrS2eu8cnj0Ni5IXQndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2p3V2h9AtWCmD27tu6pjMTGKQ7sLV27Ot8hiclGsGxWN0JLJwcaBXlcTkVDmXsFGK83kWXjbZ1IzRdCbMOvZ3kFfnIzkJ13j3uYdJ01vAFnTGPKzhLuznpTsV7_ONcwcj7C6teZDs076z_8ShblO_AiQC3HZcZBbUCLYWTiEYHbSxRJ8bqHOVMixfLtHeC9V55qg2QRQoa_McITCQPcUSjP6NxarQqeKp8thtxBa_h_jRg_U1j35MhzxN5JTBfhRSvpc3gmBDHuvjLkCC_D2_DcoB1GScTlB_klxkaDgNRQRIFt8WWJHe4Isen-jyCEJM7AGWI9dU2W3ONMlDjZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4OTIaNgB1VMWdk0FHgHVKdv10NkOv6BEH2JZv0b7LFDdSW9E-UTO9yxjHwVIEHtvBLQ4ELAIQqixJ_ketFJn-e6_MHx3z5hbEVoxwyphcX2EAFNkQI9le4gvl39IsmOahNVB07xMfjazm0p8LrsleYjUTAontTp2biEqQ4S1Ce9jfFkyGro7VFhHWltTZIWeBJwoPm_AcqVJ6LDp2VbBL-PUK_DBePN5ERf4Dy91kmsE5BwySqlNxheq1EvL12s5BF2QGPQMIxISGHW4AB209msgZbOeAZh2ocmt0QRwZ1J_HXGOZ7GmMuD4KyLse0xZd3PCXLpATdXpI84bNEiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPz8NgNM0lKvKRfQyfxKYRS6D1wkW9sw_smJaGl1GvqLZ7C-wZspXnSjxnKwnH85FoHn8tzeXRTyEP4vmAZfzlvVF8qx_8bUXRJ0h6s_0Xe0S9N85HnYyCYXhsp5W27w3bM726Edxf2vwg6ptCB-REJLWABUCt_y4wcF5Zms2Yu4al1B_BLXYPEfxiLdwZg6vLZ8CbZISgoZCxIjaRj4k5fIM-1PqJfP-A0kU1-ttjL7uWdJXJQVaorLx8oOy428PO9eN6Dze0yx-wkvDLHARyzznK8leWs8WdYbvMbaf89uLdnkEZZWU6aw62wDEZzri970s_Efuydhtp140Cv8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKpRtySsTs5mMBZHEiLA3MCLvga7v4AiIrvIxVBIpKrBo9Js_cDY0p9uxqrQzd4kBdTR9f9EMrPPmoSAQevJxotgdJUByi-3XGgEvoCDzglm_tN9RaPmS3gG1SRfKmZHk0K0tZQrY9IUc1-FDdrUwWF_FYRJ6xsGD7EkUPVeeo5p9_hNXaruPQzUPdSug-Kbp_9JvXFg1-2Lzy1cxWxxLlMFArx1cZgRmVEr8ATsmwQU8YNSASM3Gu-Rx3BWI_QuSPgne2t9zykOPBaAI0jWHxkKOcODtfZT0OHP2LFYp_9u84Xjnp6R5ZAIKJrTWVcTF46tRUnEpYQY6_L_Z-er7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5tFBtKoYQRm0fv4JLOBJKqpMkvOv6OoRAEeVagNkp94LyEsF1plNcGdtWHGxi9L-F9nNVBUpwZQTFG5Yy_9yXYM-0XCRxyfUTkkRxjOkB1hNSFNh6Kh0DuKn2vlvqlx8_sfx_g5A-a7Jwxds_byjeYUsjZ6MygkfPyc8b_aZu5yZrDJa7_NFGtCEa_1IM3ioQ-sdSg_wftRPow6qk3MHVvnUaAPGuwGRL7m_fEbRxiNOy4XMqmx_gXWMN0iSOXOIc7SIOc3H3I0MAo0mQMBVUFFQ9qC6y32wl94bPDo-lY6kFA8-4koXWLGZdc2HrKawqPfdDK1caZIWGXnlwLXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCYqdHnVp_KnhLAHCBsb_KAfCO3J0t_4BdgWpvNAkfPmWvWd2yYHGq3GxQW947gaYmEfkVBK_K0HiAcTTkzzIfyEZWnjn-IEO6Xvr03mQxrO_aRcJJs0jw-6_nfkwAPqAOwi2glQQ40mgvQdV30RNYYPFCDv49ZhrRGKsZZOo3Rkf_Lp3zq1nNVb044FIHr9AQsYLlkqt-PMG3-rG3kjWv2KVOYtA0yUd2pw-3TP1h1EMIVcNNt1Om-NtJuV9xdEcCeOrAZBAQsRFFtJ5A7QlFuYV15TsfPKGcl-Vq54Vq5WQyWcY6a1zeKtK-lj526OZpv8UcCK_mulXbwvEjR5Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
آموزش تصویری خرید اشتراک ArchiveTell با سواپ‌ولت
1️⃣
-
ثبت‌نام و شارژ (زیر ۲ دقیقه):
وارد (
@SwapWalletBot
) شوید، به بخش
Wallet
بروید و با شماره موبایل و کدملی احراز هویت کنید. سپس حساب ریالی را شارژ کرده و ارز
🪙
تون (TON)
یا
🪙
ترون (TRX) بخرید
(توصیه ما TON است چون انتقالش کارمزد ندارد).
2️⃣
-
ثبت سفارش:
در ربات ما روی «
🔐
خرید اشتراک» بزنید و حجم دلخواهتان را انتخاب کنید.
3️⃣
-
پرداخت فاکتور (یکی از دو روش زیر):
🪙
روش TON  (بدون کارمزد):
مبلغ را از سواپ‌ولت به آدرس زیر انتقال دهید و حتماً رسید را به
☎️
پشتیبانی
بفرستید تا سرویس فعال شود:
👇
(برای کپی کلیک کنید)
UQBS9c1YqBaOI1oTcXo0n_khM6XxaJDInwHpr0u63JhgBrh-
🪙
روش TRX (تایید خودکار):
مبلغ دقیق ترون را به آدرسی که داخل فاکتور ربات نوشته شده واریز کنید تا سرویس کاملاً خودکار و بدون نیاز به رسید فعال شود.
✔️
در آخر، وارد بخش «
🛍
سرویس‌های من
» شوید و لینک اتصال خود را به راحتی دریافت کنید!
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5143" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار
قیمت عالی
@ArchiveTellbot
آموزش ساده خرید تو پست بعدی..</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5142" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
معرفی اپلیکیشن TheFeed برای کاربران iOS (آیفون/آیپد)
---
رفقای آیفون‌دار
می‌دونیم که پیدا کردن ابزارهای دور زدن فیلترینگ برای iOS همیشه سخت‌تر از اندرویده. امروز یه کلاینت جدید و جذاب به اسم TheFeed رو بهتون معرفی می‌کنیم که فعلاً تو مرحله تست (بتا) قرار داره و می‌تونید از طریق TestFlight اپل روی گوشیتون نصبش کنید.
🛠
آموزش نصب و راه‌اندازی (فقط در ۳ قدم):
1️⃣
قدم اول (نصب پیش‌نیاز): ابتدا باید برنامه رسمی TestFlight رو از App Store سرچ و روی گوشیتون نصب کنید (این برنامه مال خود اپله و برای نصب نسخه‌های آزمایشیِ برنامه‌ها استفاده می‌شه).
2️⃣
قدم دوم (نصب اپلیکیشن): روی لینک دعوتِ زیر کلیک کنید تا صفحه TheFeed تو برنامه تست‌فلایت براتون باز بشه. بعد روی دکمه Accept و سپس Install بزنید تا برنامه نصب بشه.
3️⃣
قدم سوم (دریافت کانفیگ): بعد از نصب، برنامه خالیه و برای اتصال نیاز به کانفیگ دارید. سازنده‌های این پروژه یه کانال تلگرامی مجزا زدن که کانفیگ‌های مخصوص TheFeed رو اونجا قرار می‌دن. کافیه کانفیگ‌ها رو از اونجا کپی و تو برنامه وارد کنید.
📥
لینک‌های مورد نیاز:
🔗
لینک دعوت و نصب TheFeed (از طریق TestFlight):
🌐
https://testflight.apple.com/join/J6bfxDdZ
⚙️
کانال دریافت کانفیگ‌های مخصوص برنامه:
🆔
@thefeedconfig
📢
کانال اصلی پروژه (برای پیگیری اخبار و آپدیت‌ها):
🆔
@networkti
📌
#معرفی_ابزار
#آیفون
#آی_او_اس
#نت_ملی
#فیلترشکن
#TheFeed
#iOS
#TestFlight
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5141" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آپلودر بدون نیاز به ثبت نام
https://guardts.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5140" target="_blank">📅 13:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5139" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCheshm E Oghab - چشم عقاب</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CheshmehOghab-Android.apk</div>
  <div class="tg-doc-extra">26.1 MB</div>
</div>
<a href="https://t.me/archivetell/5138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود مستقیم اپلیکیشن چشم عقاب
یا از طریق:
-
گوگل درایو
-
گیت‌هاب
-
گوگل پلی
میتونید این آدرس‌هارو با دوستان خود به اشتراک بگذارید از اونجایی که برخی از سرویس‌ها رو بعضی از آی‌اس‌پی ها باز هستند.
@CheshmehOghabApp</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5138" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
معرفی اپلیکیشن «چشم عقاب» (Eagle Eye): دریافت اخبار و کانفیگ VPN، کاملاً آفلاین و از طریق ماهواره!
📡
---  امروز با یه شاهکارِ تکنولوژی و انقلابی اومدیم که دقیقاً برای روزهای قطعیِ مطلق اینترنت (نت ملی) طراحی شده.   وقتی اینترنت کاملاً قطع می‌شه، اپلیکیشن…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5137" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
