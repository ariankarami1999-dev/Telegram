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
<img src="https://cdn4.telesco.pe/file/t8omcVpZiqBNxLhDmlZkctYo98Zb0TsmiYb4uHXGKNJqyEUL6UQrR83fKM8wwRyvJ9oHUJdf9c2zmgKeP1WCkRE-g_ORiU3elJjB5izGlufunRMHn48VjAniw8erLpu6Ifk8hS28vE3cMOVAryHIFbyG91g3-Dj8ePEv3H8QkwSMaI3x1iSjEoRgxT2KLe6sbnphN8u5CyrV0QnkLS_KAK5GBxYwD5_27QthSUWJhxdaHw79-XzV1bMBstCEqIPV1d11uLfdZZfVOw7oHX0NjtTC0MQxGCkjXpTWXcpCAR557sk_LMPzMpCIJBD_crIRzauH8qENfcffXKvDXWzWQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.11K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 6 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 87 · <a href="https://t.me/archivetell/6045" target="_blank">📅 15:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎬
دانلودر یوتیوب در تلگرام
دیگه نیازی به سایت‌های دانلود و تبلیغات آزاردهنده نیست!
😎
فقط لینک ویدیوی یوتیوب رو برای ربات بفرستید تا:
✨
ویدیو را مستقیم در تلگرام استریم کنید
🎵
فایل صوتی را با کیفیت اصلی دریافت کنید
📥
ویدیو را دانلود کنید
🗜
ویدیوهای حجیم را به‌صورت هوشمند فشرده کنید
❤️
بدون عضویت اجباری در چنلی
⚡️
سریع، ساده و کاملاً داخل تلگرام
🤖
Bot:
@youtubedownload12bot
👨‍💻
Dev:
@Bachedev
#Telegram
#YouTube
#Bot
#Downloader
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 407 · <a href="https://t.me/archivetell/6044" target="_blank">📅 15:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
کمپین جدید
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 41 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/archivetell/6043" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همراه اول Happ
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 139 / 600
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/archivetell/6042" target="_blank">📅 13:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkc-IurdpMgxevFnA3g7i7K81plfL1pHm-Blaht5O4wfkUTitZt3PtzZmBevkt4F-tWyMuznikZQrMUaH3JKzxRvzJi3FCk3Jy5fLYOcBvpsnBlRw0QxYeyYvH50nbvnkgUVF6_CsvYbqU-rPaAV6piEkXiegjZMGkL_Q3FztoeCYzSUZwdJv5UW3QizVtHz0iJFskRi3NIZFP9tckX9AfoyBlzW7nmN7OTqlQviy1Dm_0xAJfTCsNt0PvSppYnpLe4fEHa5Yhl-0WZ8qWrrEzqFu1egoBWPOnKPmJtBElrS--sJmx-tgUR0hKyvciGHv9ZNNQUC7CzW615PfBoRgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ابزاری که مصرف توکن‌ها را بدون از دست دادن زمینه به طور قابل توجهی کاهش می‌دهد.
به جای اینکه فایل‌های عظیم، لاگ‌ها و تاریخچه چت‌ها را به مدل بدهیم، Headroom ابتدا آن‌ها را بهینه‌سازی می‌کند و سپس برای پردازش ارسال می‌کند.
این چه فایده‌ای دارد:
🕤
قبل از پردازش زمینه را فشرده می‌کند و مصرف توکن‌ها را ۶۰ تا ۹۵ درصد کاهش می‌دهد.
🕤
در صورت نیاز امکان بازیابی فوری داده‌های اصلی بدون از دست دادن جزئیات را فراهم می‌کند.
🕤
کمک می‌کند تا با پروژه‌های بزرگ و جلسات طولانی کار کنیم.
🕤
از Claude Code، Codex و Cursor پشتیبانی می‌کند.
https://github.com/chopratejas/headroom
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6041" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=Y0PqWndgWieRjrDEDLlumG9zvEEy2VLVBsI7r1Snzp4Vy7xXwpYL7OtLriUnccGw_9-E8E-M4JH65m3ve-OqAOXCrNZUTG8LN3QP2oK27Vy5agidcy5x42K8hJCS8b6decajXfOGsA-cbhj9EbwqH0wcW02xrqgJ8tICGYGIcAErSmW1WZzVeUNSdH1Zqj3x3W_ViNbB36XpibKMrWbmZt6p-gIay1oi7wkok38j5pxopZhcWwxOP5yvQEDrBR7-rEAB7uTaPQYrdmbizVYbBhNz6hOiV6tSB95LjtrxVPFlJ6eGw6BxiXGX8G6SM0nOQ_TAUmDZhFZBUfLpiE2Bgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7b603d8f.mp4?token=Y0PqWndgWieRjrDEDLlumG9zvEEy2VLVBsI7r1Snzp4Vy7xXwpYL7OtLriUnccGw_9-E8E-M4JH65m3ve-OqAOXCrNZUTG8LN3QP2oK27Vy5agidcy5x42K8hJCS8b6decajXfOGsA-cbhj9EbwqH0wcW02xrqgJ8tICGYGIcAErSmW1WZzVeUNSdH1Zqj3x3W_ViNbB36XpibKMrWbmZt6p-gIay1oi7wkok38j5pxopZhcWwxOP5yvQEDrBR7-rEAB7uTaPQYrdmbizVYbBhNz6hOiV6tSB95LjtrxVPFlJ6eGw6BxiXGX8G6SM0nOQ_TAUmDZhFZBUfLpiE2Bgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗂
ارسال فایل‌ها به هر کجا و به هر کسی — ابزاری که همه چیز را فوراً ارسال می‌کند.
می‌توانید سرویس‌های ابری را فراموش کنید:
🕤
پشتیبانی از هر نوع داده‌ای: اسناد، عکس، ویدئو، موسیقی، آرشیوها و پوشه‌های کامل.
🕤
نامحدود مطلق: هیچ محدودیتی در اندازه وجود ندارد، حتی ده‌ها ترابایت.
🕤
انتقال مستقیماً بین دستگاه‌ها انجام می‌شود، بدون سرورهای واسطه.
🕤
رمزگذاری در سمت فرستنده انجام می‌شود.
🕤
رایگان و بدون نیاز به ثبت‌نام اجباری.
https://github.com/tonyantony300/alt-sendme
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6040" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOxfo90rlYov2gHYD5x0KI7PcRzyeff-vVZ0s1a94E3NipAHOEQDf90_t4u_EtGErsXDRYJXC7DYyOOgFtUpWTwwZbDH285Rlwqf5mbCRhB3xXOpXknG7igIhGGgflTZTfABaFKlzaJHcV2OuENLdTWV8teEqbLt-jESHhSUJJL7Qal0lrInLyTYNjFUlokhZ51QMOUlDpEff672yTTrqCH6q3VAYesEC7XMH2NOvoB0HqT6buAEveJNCDx5pieKDKTjsFVV0UPysPiOGYkGOBFTClGZx_J2YLxbX-GqcuEahp8TK3YZ-9s2DmYk2ul-d646_DNmEXHkz6tzT5U63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان پس‌زمینه تصاویر با هوش مصنوعی
پشتیبانی از فرمت‌های مختلف، پردازش در مرورگر به صورت محلی، حفاظت ۱۰۰٪ از حریم خصوصی.
https://quickbgcut.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/archivetell/6039" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo_IyLqoTCerKtCOC8NjgNZ0J6C-zuf7XoOXs4QyeFQs2mHlIhQwv4dNijNd9ZZTfXr1uVpKNVXOgrSmwlPO0MPGN5thVQmS0vR-oOuLw80bmgo8v05Om7En8oMzmIm-0ZVQxNAIn1cGkpSfbAKy4lccmkkyZdPggo93SUTmQw2LDh3cyrZunSjvAgcMuIyo-2je0EOEz39SAs6VhEeMjF1ShucGnTYwbVqzZ6OluBWlWIx4iYFJskQyW9_AfENs4gP-zvKS0DyqN4Jf-YFteobwAGISnPCptPXRQFiht6YAwcrD3eRTjr1Rq07-c3pxwQkSC3gQn-OspSANsnBcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
untracked — کوچک‌تر کردن خروجی پروژه با یک دستور
اگر پروژه Node.js دارید و می‌خواهید حجم Docker Image، Vercel Deploy یا Bundle نهایی را کاهش دهید، این ابزار به‌صورت خودکار فایل‌های غیرضروری را شناسایی و از خروجی حذف می‌کند.
✨
قابلیت‌ها:
•
🧹
حذف خودکار README، LICENSE، CHANGELOG و مستندات
•
🗺️
حذف Source Mapها و فایل‌های توسعه
•
🧪
حذف فایل‌های تست و نمونه‌ها
•
🐳
ساخت خودکار .dockerignore
• ▲ پشتیبانی از .vercelignore
•
🚀
سازگار با Docker، Vercel، Heroku و Yarn
⚡
استفاده:
npx untracked
یا برای ساخت فایل Docker Ignore:
npx untracked > .dockerignore
🎯
مناسب برای توسعه‌دهندگانی که می‌خواهند حجم نهایی پروژه و زمان Deploy را تا حد ممکن کاهش دهند.
🔗
GitHub:
https://github.com/Kikobeats/untracked
#GitHub
#NodeJS
#Docker
#Vercel
#DevOps
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/archivetell/6038" target="_blank">📅 13:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 271 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E62AK6-OTpyHrVviRdxp4oYRQHYCZI0Qawd_eZ8I0ZJXhsHvEXh1IBiPm9tWDSS7KbxzeUDHhW-HTaH7sGBhsE1O_8sxtUtuTEU5jvD-ItBfvzFbtYJRClKMGLRWToL-HokPlsk24UTxlxxDp2ltR39s1mfvmSE2WZj0OEYMtgpKuR3KaqV4WbFSICuaGvstBkHXmo2Bk0BZdaxEm9wN6F8dyrUVQBLmWEjsP4UCIEvh3YAEQPVYwl4C94G2d_5rv_fZwA-mA9k1hu_uH5UeyXOit3sZL1he9j2y6E5HJMnMoa66a6ZsEtle5a-hXeAUtr942WfRQ6bj0UdbY4vj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100 گیگابایت-تایم نامحدود
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 149 / 200
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/فایل
⏰
مدت اعتبار: بر اساس تنظیمات دستی/فایل
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
UAC SNI Spoofer Android
ابزار متن‌باز اندرویدی برای اجرای کانفیگ‌های VLESS و Trojan همراه با Xray داخلی و قابلیت SNI Spoofing.
✨
امکانات:
•
🌐
اسکن خودکار SNI از لیست دامنه‌ها
•
⚡
انتخاب بهترین کانفیگ بر اساس پینگ و اتصال
•
🔒
پشتیبانی از VLESS و Trojan
•
📱
آپشن Split Tunneling برای انتخاب اپلیکیشن‌های عبوری از تونل
•
🌙
حالت تاریک و روشن
•
📊
نمایش لاگ زنده Xray، VPN و خطاها
•
🛡️
مدیریت VPN محلی با tun2socks
🧑‍💻
پروژه کاملاً متن‌باز بوده و با Java توسعه داده شده است.
🔗
GitHub:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android
#Android
#VPN
#Xray
#VLESS
#Trojan
#OpenSource
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤖
Private Link Bot | اشتراک‌گذاری فایل با لینک خصوصی در تلگرام
دنبال راهی هستی که فایل‌هات رو سریع با بقیه به اشتراک بذاری؟ این ربات بعد از ارسال فایل، یک لینک اختصاصی برای دانلود می‌سازه.
🔗
✨
امکانات:
•
📁
تبدیل فایل به لینک دانلود
•
⏰
تعیین زمان انقضای لینک
•
👥
محدود کردن تعداد دانلود
•
🔐
رمزگذاری روی لینک‌ها
•
⚙️
ذخیره تنظیمات پیش‌فرض
📌
مناسب برای اشتراک‌گذاری موقت فایل‌ها، اما توجه داشته باشید که فایل‌ها از طریق خود تلگرام و ربات مدیریت می‌شوند و لینک دانلود مستقیم خارجی (Direct Link) ارائه نمی‌شود.
🛠
دستورات:
•
/settings
— تنظیمات پیش‌فرض
•
/help
— راهنما
🤖
ربات:
@Private_URL_Robot
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WLYqsNMsZ_tNF7L35VFz7-QejfmEWsCJmfHv_npPcWcp2-6WksHGNdlpzTPE-c_9Q05NSwTPIhiUkbBzFUaLDfvaYsFd2N0qm-TTSOwv0ZIa5vZ26flO6YQ_KN7HLkafte-eMPxHp0ybu4LWhqa7s9Tn10efqUb-Rh2CP-fyXyZJM_0PRgXCU9iX2RFxPBPgNu-fsioeFl6GIgvuXy-J24wZP5_xuw-4o4RGx9GhmrXfvJW1XhRg8a3SE-U42naItuRqmP5T1Du8L3DPs60Il4URsIaa6fscTouGQqAlIwa2zF4nv2_djoa7XwadQQzjJFhHGZni_xjrIebB1hc8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/6025" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: 50
🧭
شرط دریافت: کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 49 / 49
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 49 / 49
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/ساب
⏰
مدت اعتبار: بر اساس تنظیمات دستی/ساب
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6023" target="_blank">📅 20:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzknUDhiw1VudfeQu5P4nW2q81YU2rMwrT3qVVNgi6zRkAlQG_nspS35vTR_voj8EPXhZwyJLT-k-kotLW7fKWhS-l9dPwhSxmpNX-HrQzH-x8UomGc5MVGJ0ZqydqySvlmkOba9Vcl1tFIi8FqYTd5QzMc2qgkVSrlxlSe3M0PRo33KHFUZ5ts7lVugsa_xdu9Nx5fOOsyZURkvie5ikvf7uDazPrMbabpELTt4H38rTw1ghdsjJ1HLVzvvN7PURz1somvD6ol5I97lhTiQe8VncwsTjJxKbtzBCFMnc3m1c6aGi_MQh8uuHXnM7F80kkppCcpJyCVH6h91-eWNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hS6impCdPAFtE2CNyPSOTfXR2HSdbJPSq3_KQNGB8LK2WFlMGOoI6t0xEmyqAdLPUkL78IZTkRmAfqSdgNOGWOKp6OQ2LmMQisEycjp4IxOvGzpLa6jtSeAzy5Ia4saoZSyuxS5DjgwMDwa3KGJQ1D6UEcP8frcHbbqaq0D5AsZXwm72KERo3shdbrRWkrlaarnwoYfF3DGm6WBfFLkG4ZJaG-IaHLJ4jTXBC-Sp7ZcGikq6tcWaXi8eqxUkrhS-lR44X7XBdimJ-3w7ipN5t7NO8UtySqALZF4dHCiHABPSACQvRE7A5Og8KbGDGESWEOmvvBnopLJT5zxfVQNNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDIYBbG0paoufC_9DuOQ18sv2MgozSMUsYR7DEZJXSbZezeRVeBo3kbHKm5-FKjEbTgz8Uj9EKwBwX38JR43gfaChgYGkFwhkl-FPwByStP2ITARMRuJm9EZMhWv4MrfGY3G2yTIMqU9gnor-2KEO7BcPEYL82a9D6c_bqjo13IA6rUlajPxn9WrQ_45oY13rS3wLdQbzYJn79GmBnMxDk-CTNRvbq0zaO4BTsUGuncK8LDBLg7HxtA_vDEi5WZlBGjDy2urXcApzaaGJl0Br8wEMRQ5ijF2NORDJXvH7dhTtaiHMv5QI7W2Vnk3eNMUHr8uy2-PM_gXGscudY_76g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
ابزار V2RayEz — ابزار متن‌باز عبور از فیلترینگ مبتنی بر DPI
ابزار V2RayEz یک پنل وب محلی و تک‌فایلی است که مجموعه‌ای از ابزارهای شبکه را در یک رابط کاربری مدرن ارائه می‌کند. کافی است فایل اجرایی را اجرا کنید تا داشبورد مدیریتی در مرورگر باز شود.
✨
امکانات کلیدی:
• پشتیبانی از Xray و Sing-box
• تونل SNI با قابلیت‌های ضد DPI
• دامین-فرانتینگ سمت کلاینت
• کتابخانه مدیریت کانفیگ‌های V2Ray
• اسکنرهای CDN، SNI و IP
• پشتیبانی از Psiphon و Cloudflare Worker
• رابط کاربری فارسی و انگلیسی
• بدون نصب‌کننده و بدون تله‌متری
🔧
فناوری‌ها:
• توسعه‌یافته با Go
• پنل وب داخلی
• قابل اجرا روی Windows، Linux و macOS
• متن‌باز تحت مجوز MIT
گیت هابش:
https://github.com/macan-dev/EasySNI
آموزشش تو یوتیوب:
https://www.youtube.com/watch?v=Y3tVfMqgys4&t=28s
#OpenSource
#GoLang
#V2Ray
#Xray
#SingBox
#Networking
#GitHub
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان
دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:
1. وارد سایت
cursor.com/students
شوید.
2. با ایمیل دانشگاهی (.edu) ثبت‌نام کنید.
3. فرایند تأیید دانشجویی را تکمیل کنید.
4. اشتراک Cursor Pro برای شما فعال می‌شود.
⚠️
داشتن ایمیل دانشگاهی (.edu) الزامی است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وایرگارد...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNFl5XrgBiJec2zsg77QNeBB4CBN2GaYZBjH2oViavDADGfbdBUTYh_ZABNSBeSaX5KDDA8qDrclM823TilNlJgsrpw5HaVpdspapA-0uS9y6I7ZO2vqRFoYMR5hMUax5l6KkEOh8XRVo-idF6CUr_eQ2x80kGr5VpDancNONuwihuvSTPT6IPWsJcoNXlkz3r1XyUxbFeCdtkMdD9-_8D3zVWHKZusmvs0IkwToD_kx8ffDS2k_Y7ODS28YagwU6yy8l09TUSRz3GOsIoo5AqutvZ4oVJvcxEfFsejKDbxNPClhbvP234Z_eYkRJxWg5xlNyKXlKjiW3--j-cdC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrMBBjOtqtaS5V2u6pszRyaaCUnK1ipl9V3JDJcP1Y_m7I7JaTwDrGnPCrTPOpBk6CVKeI_ZECTX29SOA2yC7cq6GDeSPGO0RiH5TP-mNQxePliWgDFmNhYsP_I8MSp6JMqjhIIvWySVGpp_36zoAR8zQOrfHgQydjMtXIuxgFFodxk-JarTrnErJMumKlYBQYxqBItTnDFrV8p8QBusQ95GqBLc4ZT0vodw6rsEvPWA144Td70DdoAUsh3umzSxFmAJ6M2ix2UAKUNwqcyYUd39cpRULCRWk8xyoQ-nJstF9zwDt_XScuuQGQtW8sojV7SmWE3_v4LTRtFP29jdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZQ-kTVibk7feBuOM6oUeImTgj1SjJbzlqPq_gU9mf-Gb9G8MJS3mL7m9m8WeEn7Q8FTSy_qk4vFzjegEup_ebhSvyha4mLwCbU35-HlVC0FsyGrWCn8TTiLy5y9z_O8SBhDZHQ8icxXvsr7dyGLzinNxDES8ZtM-s9rEtlpNcDoNV75xygGgiaNBjhFy_UH0O8uBp5MNtUl3Hd4HAHGDFZLDD-Aju7SWWVC5nRK3rrfu6p-LwFhD5BhFrPw_0Y_HrWqnmBCieY9kgtP527da7M5MMj6RT4B4w5Kd3rM_Sn1BD7dPGsYwQyfryka_c0cp-JBYhxSyzh_YfniJzHijw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک استارتاپ به تازگی ابزاری برای تصویرسازی با هوش مصنوعی ساخته است که در جهان رتبه دوم را کسب کرده است - بالاتر از گوگل و Midjourney.
👀
🎨
نام آن Reve 2.0 است و همین حالا منتشر شده.
آنچه این ابزار را واقعاً متفاوت می‌کند، نحوه عملکرد آن در پشت صحنه است. هر تصویر به صورت کد نمایش داده می‌شود - به این معنی که هر عنصر به طور کامل قابل ویرایش، قابل دسترسی و تحت کنترل شماست.
بهترین دقت متن روی تصویر در میان تمام ابزارهای هوش مصنوعی فعلی.
رایگان با محدودیت های روزانه
این ابزار در رتبه دوم جدول رده‌بندی Image Arena قرار گرفته و از Nano Banana 2 گوگل پیشی گرفته است -
🔗
https://reve.art
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetell.npvt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/archivetell/5986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پخشش با شما
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=ZZOv9qZAsywqCU9gY4ApJ5855WYrb-i_gYjN1FZ64q5q-Ge8SWTfC9gduGj39IxLOcvt5_Kc-Wn0kmEAwu0XnjkcyzL3VH_t3alqv5c_pmoit063_-i6KzuTYSKLSShqot4WpU1_d7ryYxYBQGOIsxxqPrn0ua_WAaJrxK905vlb59Bsiv20Ky-offi1IhPF7f_o2-dHxxyLhnkOjD3muNC478YIFbNVZfbZ6qTTqWEJcqV09HNPLDVPRHv6Pgo88_CXBucnSso_Xzx1ZKXO-1Y8GKcTb4fIVDRT1cbTqz5wlERSuMMjyKwbent4itqgP7j9BEQSYytukcVU0HdqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=ZZOv9qZAsywqCU9gY4ApJ5855WYrb-i_gYjN1FZ64q5q-Ge8SWTfC9gduGj39IxLOcvt5_Kc-Wn0kmEAwu0XnjkcyzL3VH_t3alqv5c_pmoit063_-i6KzuTYSKLSShqot4WpU1_d7ryYxYBQGOIsxxqPrn0ua_WAaJrxK905vlb59Bsiv20Ky-offi1IhPF7f_o2-dHxxyLhnkOjD3muNC478YIFbNVZfbZ6qTTqWEJcqV09HNPLDVPRHv6Pgo88_CXBucnSso_Xzx1ZKXO-1Y8GKcTb4fIVDRT1cbTqz5wlERSuMMjyKwbent4itqgP7j9BEQSYytukcVU0HdqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
اجرای مستقیم بازی‌های کلاسیک و نوستالژیک در مرورگر
اگر به بازی‌های قدیمی کنسول‌هایی مثل سگا، پلی‌استیشن ۱، گیم‌بوی و NES علاقه دارید، وب‌سایت
gam.onl
یک آرشیو کامل و کاربردی برای شماست.
مزیت اصلی این سرویس این است که برای اجرای بازی‌ها نیازی به دانلود فایل، نصب شبیه‌ساز (Emulator) یا درگیری با تنظیمات پیچیده ندارید؛ همه‌چیز مستقیماً روی مرورگر شما پردازش و اجرا می‌شود.
📌
ویژگی‌های این وب‌سایت:
*
بدون نیاز به نصب:
اجرای سریع بازی‌ها در خود مرورگر.
*
آرشیو جامع:
پشتیبانی از کنسول‌های نوستالژیک و پرطرفدار قدیمی.
*
سازگاری بالا:
قابل اجرا روی مرورگرهای موبایل، تبلت و دسکتاپ.
*
کاربری ساده:
فقط کافیست وارد سایت شوید، کنسول مورد نظر را انتخاب کرده و بازی را شروع کنید.
🌐
لینک سایت:
https://gam.onl
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu3VtdRwhaQKCp3_AYRHo7dqKQqy-ppHHJUII_KCP2wxj2mKv4bT4yhPWewR_rvley4FJRyighf1Q0QbbpKuxyKnGPPrHg521Nbk3tgccToC-AxF-PhxWS_MzVMDJX5yt0OlHUVm0WoneUFOEY3XIkVeLh-GewEHwz6ROaTXLnzT9zWUjQvpF2eHRRMQVj-lvWlpwdGve4SDti0b_7auCs3yHh7SDd3B7xqst2kHnmfwvPaZBou4waCPeH_BNwTUB2ENtIcC8PjaooqgArVSeK9AeZpeQJn8fLOu9c7jcZ-jCDPBJMSKNu5h-SLFwS_xnpSX8ZZpLjy7GlsPPRopMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
در حالی که اکثر افراد به صورت دستی گیت‌هاب را زیر نظر دارند، Trendshift به طور خودکار پروژه‌هایی را که همین حالا در حال محبوب شدن هستند، شناسایی می‌کند.
1️⃣
رتبه‌بندی مخازن ترند در بازه‌های روزانه، هفتگی و ماهانه.
2️⃣
جریان انتشارها از توسعه‌دهندگان و سازندگان پروژه‌ها.
3️⃣
جستجوی هوشمند بر اساس حوزه‌های فناوری و دسته‌بندی‌ها.
4️⃣
فهرست‌های جداگانه بهترین عوامل هوش مصنوعی، دستیارهای کد و سایر راه‌حل‌های محبوب.
یک روش عالی برای دست داشتن بر نبض گیت‌هاب و از دست ندادن نسخه‌های واقعاً جالب.
https://trendshift.io/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">معرفی ابزار AutoWorker؛ راه‌اندازی خودکار پروکسی روی کلادفلر
سلام دوستان
🌹
همان‌طور که می‌دانید، پیکربندی پروکسی‌های مبتنی بر کلادفلر ورکر (مانند پروژه‌های خانواده Nova) معمولاً نیازمند طی کردن مراحل مختلفی به صورت دستی است؛ مراحلی مثل ساخت فضاهای KV، جایگذاری کدها، پیدا کردن Proxy IP سالم و تنظیم پنل.
ابزار
AutoWorker
توسعه داده شده تا تمام این فرآیندها را ساده و کاملاً خودکار (Automated) کند.
📌
قابلیت‌های اصلی AutoWorker:
*
بدون نیاز به پیش‌نیاز:
برای اجرای این ابزار نیازی به نصب Node.js، پایتون یا محیط‌های برنامه‌نویسی ندارید.
*
روند کاملاً خودکار:
از ساخت ورکر تا اعمال تنظیمات پنل و دریافت آی‌پی تمیز، بدون نیاز به دخالت کاربر انجام می‌شود.
*
حفظ امنیت اکانت:
این ابزار پسورد شما را دریافت نمی‌کند، بلکه از طریق پروتکل OAuth 2.0 یک توکن دسترسی موقت برای اعمال تغییرات می‌گیرد.
*
پشتیبانی از پلتفرم‌ها:
فایل اجرایی مستقل برای ویندوز، لینوکس و مک در دسترس است.
🛠
نحوه استفاده:
۱. فایل برنامه را متناسب با سیستم‌عامل خود از گیت‌هاب دانلود کنید.
۲.
نکته بسیار مهم:
پیش از اجرای برنامه،
فیلترشکن خود را کاملاً خاموش کنید.
روشن بودن فیلترشکن در روند اسکن و دریافت Proxy IP اختلال ایجاد می‌کند.
۳. برنامه را اجرا کنید. مرورگر شما باز می‌شود تا ورود به اکانت کلادفلر را تایید کنید.
۴. پس از تایید، به ترمینال (محیط برنامه) برگردید و منتظر بمانید تا مراحل تکمیل شود. در نهایت، اطلاعات ورود به پنل و
لینک سابسکریپشن (Sub)
برای استفاده در کلاینت (مثل v2rayNG) به شما نمایش داده می‌شود.
📥
لینک دانلود فایل‌های اجرایی از گیت‌هاب رسمی پروژه:
[لینک صفحه Releases در گیت‌هاب AutoWorker]
https://github.com/marketnoobtrader/autoworker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN-Z1SRaS5671cIoFkx-vUx7ryhb1M18r73t6TEw6X6lFHxmDWmt2khCchx-sJQUVb6gL1T6jX9hb3sKrdU_F7QqBd7U5fVDznWiwgUYYztK3zjzynUrTiroBxntRODel3TCKsCo3gbgNW5IYqOacUggI3YTSksDiOOvDAFawc6jGFeXRm-It8pn-Rfv2We9CUnbrhu8LU0SznXFe-o0zIIG-7J7TgeczDwLqOXztptecdKyKQ3PSR37dMgX9EoU7KILDWnluJoG9P4UfgkV-SToYBuGD-s-2Pg2D5DXAm0rX02uTp2qg0hNkyC3fjPxgvWf7i1t53MgFX5OLKOTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
متن‌های هوش مصنوعی را کمتر کلیشه‌ای و طبیعی‌تر می‌کنیم — اپلیکیشن AI-Text-Humanizer نوشته‌های شبکه عصبی را به سبکی زنده‌تر و خواناتر تبدیل می‌کند.
🕤
افزودن انتقال‌ها و ارتباطات بین افکار، با حفظ معنا و ساختار.
🕤
جایگزینی کلمات ساده با کلمات تخصصی‌تر.
🕤
کمک به دور زدن شناسایی‌کننده‌ها و بررسی‌های هوش مصنوعی.
🕤
نصب با چند دستور ساده — بدون نیاز به برنامه‌ها و اشتراک‌های اضافی.
https://github.com/DadaNanjesha/AI-Text-Humanizer-App
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=Z-hIRRFfwKEKm325SNbvAzpwc0i6zRetsH5Ue6snjWAMT1yWldgIK29XywKtOC0c8tQwxWQ5QHcqxjJfSN2oCRStqtFqnczb7HicEuZhgeFk4soKwGlaMvAqcSUqI3MsfT_e5pF3uUPf3mV4ck1gTDtRmO31FTTSF7Tq2dY91mmaUgrBwIcC8pfsj74TBi0r2nIW9u49gRFcf1lkqaIOkSsPqqVl4kZBL7Q7Y5y2EmjorHNB8ctdDqFpUOgrtSktTRn76sV4O_eHH7xmpTOUWN6Lgr3lN6nN1XHN3FO5T5fcdTJSgdd6jzKk4pXuY9Gr-XDSa454qfxvzfeQSATdmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=Z-hIRRFfwKEKm325SNbvAzpwc0i6zRetsH5Ue6snjWAMT1yWldgIK29XywKtOC0c8tQwxWQ5QHcqxjJfSN2oCRStqtFqnczb7HicEuZhgeFk4soKwGlaMvAqcSUqI3MsfT_e5pF3uUPf3mV4ck1gTDtRmO31FTTSF7Tq2dY91mmaUgrBwIcC8pfsj74TBi0r2nIW9u49gRFcf1lkqaIOkSsPqqVl4kZBL7Q7Y5y2EmjorHNB8ctdDqFpUOgrtSktTRn76sV4O_eHH7xmpTOUWN6Lgr3lN6nN1XHN3FO5T5fcdTJSgdd6jzKk4pXuY9Gr-XDSa454qfxvzfeQSATdmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY4Yx9o_yNjkduBiMu_chTwJPE5tjhzTuJCA8Q3bt5F7dYCYkgLY82JWBYb5YnioB22xqJV_yHys9-U14J0tC7k6PIfRYf_LQ0HFq1zddOWJWWxmWJw9VcNcAXDmMn-Ozs1FrFC-Gpl4U1G5j_dZtdkfVKjir1gggrYgVfajbHEVEFex74Qfs2dU2I7B7sgpSygKuW2mxGCENAYT75TCNTwv2AiTN7-RjmQ96XZTzhe6uclC4oMEGEulKW1M2mLDm-QwonkCc3RPj24EokOQOE4lQZpywomaoZ7i6L-yHE5G_woLw0nqzWE1M3qPttWrJ8c16PgDZs8uw0XWQFZP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎬
🔥
ساخت ویدیو با هوش مصنوعی Seedance 2.0 رایگان شد!
مدل جدید Seedance 2.0 که توسط ByteDance توسعه داده شده، حالا از طریق Dreamina در دسترس قرار گرفته و امکانات جالبی برای تولید ویدیو ارائه می‌دهد.
🤖
✨
🚀
قابلیت‌ها:
🎥
تبدیل متن، عکس و ویدیو به کلیپ‌های 1080p
🖼
پشتیبانی همزمان از چندین تصویر، ویدیو و فایل صوتی
🎭
حفظ چهره و شخصیت در تمام صحنه‌ها
🎙
پشتیبانی از صدا، دوبله و لیپ‌سینک
🎬
انتقال استایل و افکت‌های سینمایی به ویدیوهای جدید
📱
مناسب برای ساخت محتوا، تبلیغات، انیمیشن و شبکه‌های اجتماعی
💡
فقط کافیست متن یا تصاویر مرجع را وارد کنید تا AI بقیه کار را انجام دهد.
🌐
لینک:
https://dreamina.capcut.com
@ArchiveTell
🍷
Bachelor</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=jRPgvwSzshiRDNpJCQWWfPU9bGjKbhFaogMI2s4Kid2P80u1YkLCQ4pAaGiHCrByN3Z3M7TbsSy7q4QwoKbSqhItQnHXyafOb-g7e4YQmVJBqcbIil1kxbCW8MaEhjBnQNhTctUhSFWu_tgjwHGv3NAzI8IUtQcjJoBP3AyyHxNf_XNeLNTDvl0SwAnr8KdasIJCy2FklmeX8jZBQmnFeI1qMYpnLYKfQu_aopzIWcRJJC9mMo-DPSoqG6qjqWmqPWHPUO9bY2y9OGnKi_bVMvuF4zNMYqSOwis_1BGcA1pXUW5F-DhpGlm3wMJa0rxePOlgA1R0YRL9wWe2FCSAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=jRPgvwSzshiRDNpJCQWWfPU9bGjKbhFaogMI2s4Kid2P80u1YkLCQ4pAaGiHCrByN3Z3M7TbsSy7q4QwoKbSqhItQnHXyafOb-g7e4YQmVJBqcbIil1kxbCW8MaEhjBnQNhTctUhSFWu_tgjwHGv3NAzI8IUtQcjJoBP3AyyHxNf_XNeLNTDvl0SwAnr8KdasIJCy2FklmeX8jZBQmnFeI1qMYpnLYKfQu_aopzIWcRJJC9mMo-DPSoqG6qjqWmqPWHPUO9bY2y9OGnKi_bVMvuF4zNMYqSOwis_1BGcA1pXUW5F-DhpGlm3wMJa0rxePOlgA1R0YRL9wWe2FCSAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔎
افزونه SwitchSearch — جابه‌جایی بین موتورهای جستجو با یک کلیک
اگر از محدود شدن به یک موتور جستجو خسته شده‌اید، SwitchSearch یک افزونه متن‌باز مرورگر است که امکان جستجوی سریع در چندین موتور مختلف را فراهم می‌کند.
✨
امکانات:
• پشتیبانی از Google، Brave، DuckDuckGo، Perplexity، ChatGPT، Wiby، Marginalia و Yandex
• امکان افزودن موتورهای جستجوی دلخواه
• جستجوی معکوس تصویر با Google و Yandex از طریق منوی راست‌کلیک
• باز کردن نتایج در تب جدید یا چند موتور به‌صورت هم‌زمان
• کاملاً متن‌باز و قابل شخصی‌سازی
🎯
مناسب برای:
• پژوهشگران و دانشجویان
• کاربران علاقه‌مند به حریم خصوصی
• افرادی که می‌خواهند از «حباب اطلاعاتی» موتورهای جستجو خارج شوند
• جستجو در منابع کمتر شناخته‌شده وب
https://github.com/thedmdim/switchsearch
#OpenSource
#SearchEngine
#BrowserExtension
#Privacy
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEEtnvVPKwsa7QnvoupTMrUEp0XP-3a9bXG1bCIfhBeyS_zVDbWADGGf90lNaywee6YU71L2WZo653pc61wMQ2FFlNkruoNYJHXYiofPlj7vwLAweP0q7yhhsGRart04mHlglVAt5N1xFlVZH8VDO2h-A67Yugf1GaLCD8VjH5-xLkBJWv1CSvxyOdTbF-8E-EtC04MnMJOU-HtjmkVCN4nl8WfdxeUyRJDSzjNIBvWjUtouykP9zuFIpPhg__rAvq1Amrn6edGShWQyER56F388eZJSHVemcTNqnZ-lUZLDvArcGmYcSC4_nJVIIxM5NiQCmjDcrDMg2S24WxVdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5967" target="_blank">📅 19:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5966" target="_blank">📅 18:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.  کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5965" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.
کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5964" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">vless://c2b6a323-19ec-4e4f-a95c-8b0e99aa7660@109.120.138.95:443?security=none&encryption=none&headerType=none&type=tcp#%40archivetell
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTRjYjU3NS0xNWJkLTQ2NjQtYjk0ZC0yZTZhNmI0Y2NkYTg%3D@109.120.138.95:28655#%40archivetell
عشقا تست بزنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5961" target="_blank">📅 18:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD_75rOM9B7VjDMops6sfYj-ivRSlFeQpZoV3XTxVLCzKF9TzSfy3h4RTb4dz5gAhI0635H_vc27SZSgM2iEaq5uByix4hF5VnKr2D_7_Tq-rZjkCElTRaY9Zi5WeaMBHZ-HnyWZgTsTCbKny6vR8-xCFjUlLe08ImxqZn1O4dLvCDkadat4TulYnk_uVpkbxDE3uhoyNYXU5Aoq1RWc48s8IjwfomcHlrWcjyvMNthx_iBoecQKxparkJpwmtpu6kUCCZjVcKM07ixcfTxHBvHhQFIXKo93jVVJCzfZ7O74wCTjHhhykVDfV9IhBG1E4vY_lTLiIHmxWoCnHiDOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اجرای شبکه‌های عصبی عظیم روی سخت‌افزار قدیمی — کتابخانه AirLLM اجازه می‌دهد مدل‌های سنگین حتی روی کارت‌های گرافیک با ۴ گیگابایت حافظه اجرا شوند.
🕤
به جای فشرده‌سازی ساده فایل‌ها، پارامترهای مدل را بهینه می‌کند و به طور چشمگیری نیازهای سخت‌افزاری را کاهش می‌دهد.
🕤
می‌تواند حتی در جایی که کارت گرافیک قدرتمندی وجود ندارد کار کند.
🕤
از بارگذاری مدل‌ها مستقیماً از Hugging Face پشتیبانی می‌کند.
🕤
سازگار با LLMهای محبوب: مدل‌های OCR، تولیدکننده‌های تصویر و سایر ابزارهای هوش مصنوعی.
https://github.com/lyogavin/airllm
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5960" target="_blank">📅 17:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0krO3OWaqzCQxUZENLnohAN1PbUmWcnU2Si0tzt60ZOd4_If3dUt_hiqWMWFV-nEBBuUln2BRy-gaGaAm5FyUELTQLGdIJf9veJwBijunGdciX-t-_YQWBhswjU7g_dPgK2ab9OHPMItrsyrruUNCExh0Emx3rIRg0UxOw-f_SojMet6l_eykOEt469fQAjPanxqPZ3BVy-sBb5n9_SZrr6xtTeF-YZ3rNcqkd0s9c4OY1kYE4jMmB9K2WhBOlSHqiL6Bm-M_GEOAFqUtzlsJCOIqmtVhTubOgq5lm208ZxzLQxj0phARbnx9DOay_dI8FkK2FojcntDPH_d6oNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujBhP8nZ6O8AXn2uB1GHxTVykBewpxIl9jCPbl_G-S5iLx0hQvOzsXRq1lGPF4QJ6RZei3bXDE-PqsXZk_XvElh5jd6-B0WBraAtqP9r_qnk_f4fs1Hmgr35l6Oqr0HH-TL4BZrc1M_g_yP6HECekS3V9HIb9uEUCS-0Fc4BXZ5Brfd-FL-7ad8DAWoKnI8V9LkYkYq0dsEcoW5j_VYcWiULYeBg9MjRLKKAsKpnhTHxOP-nnxOcQA5R0ykX4mIaspVXNH80RMs_GtGBXQsVKpBQa2gKeAzpqCMvy7gLiuB2Emg9GH1npQamRETIbF90urcBgHRVzRxBvNzt8Kjtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
WakeUpBroo — ساعت زنگ‌دار که شما را مجبور به بیدار شدن می‌کند
برنامه‌ای منتشر شده است بدون دکمه‌های «تعویق» و «خاموش کردن». برای قطع صدا باید کدی را از سایت وارد کنید — تا زمانی که به کامپیوتر برسید، خواب کاملاً از بین می‌رود.
چگونه کار می‌کند:
🔹
هیچ مصالحه‌ای وجود ندارد — فقط بلند می‌شوید و به سمت کامپیوتر می‌روید
🔹
کد برای قطع صدا در سایت تولید می‌شود — گوشی هوشمند کمکی نمی‌کند.
عالی برای کسانی که همیشه ساعت زنگ‌دار را عقب می‌اندازند.
لینک:
https://www.wakeupbroo.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=qQVy9Rzk4tH3swZ4cGqaY6pFdpwel3h4GtxWz-agDVBJHpVB03dv2dv83b8xy5haBikb0Pesjl1CFNcaYpHj_H0j5FK52AMXyXBgP_9jCekiygmfiZ9jC_sTqw799zNtn9s2BeHkIGJVJscEP0Xa8QWQrsWcT601vVHlF04NcNRWdfFHa76WoHaVFfTh_QvvGHleIWExd4-qu3EnzBqqOGPqdnggo-sZKmrmcvoaBBu6s_yKeXJeslFMQWIS8VsRIe5oDmbjbTKI11mHwAeeXQhuw4Y1rtbKr7qo0uQUc33WWtSOnt_Vm1tkprcg1CjYWjwAsugr8-wEDpo3L0F-Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=qQVy9Rzk4tH3swZ4cGqaY6pFdpwel3h4GtxWz-agDVBJHpVB03dv2dv83b8xy5haBikb0Pesjl1CFNcaYpHj_H0j5FK52AMXyXBgP_9jCekiygmfiZ9jC_sTqw799zNtn9s2BeHkIGJVJscEP0Xa8QWQrsWcT601vVHlF04NcNRWdfFHa76WoHaVFfTh_QvvGHleIWExd4-qu3EnzBqqOGPqdnggo-sZKmrmcvoaBBu6s_yKeXJeslFMQWIS8VsRIe5oDmbjbTKI11mHwAeeXQhuw4Y1rtbKr7qo0uQUc33WWtSOnt_Vm1tkprcg1CjYWjwAsugr8-wEDpo3L0F-Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کردمش یه ترا
تا جا داره بزنین</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCd-fg0CKvdxzlnTAXEkMJXNFQvvIHemtFQ29pD3GOjXhu6P1kwdHtaX3ZDUjgWG8EVoo9nd4qWN7U3Q0B7GU572EAFTscphwaoaO_JvotoJwcj_QjinB9SkbUrsdkrRvxI6nUCQRhlkuCgcZyacQfjfBQ6jhedY-2ZFC3_XQ7l0UA3WLWxNAj6FzPZKHVBu4gooV5wGp1FQc-WUhur_jHjzb8LYmWUB_yCVo4UzHrPO6WT71yVNSzVfd9u3_bYEwcsMWFK9JGBisEStj5HSpSdOFdcktA8zQY1-ZwWbw2erBb6SSNAoau-tUR7UNAf6VRMK52bCohqPIQrrbun5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪗
می‌توانید اسپاتیفای را فراموش کنید — پلیر موبایل رایگان Metrolist را پیدا کرده‌ایم که دسترسی به موسیقی را بدون اشتراک و بدون تبلیغات فراهم می‌کند.
Metrolist چه کارهایی انجام می‌دهد:
🕤
موسیقی و کلیپ‌ را با کیفیت خوب پخش می‌کند.
🕤
موسیقی و لیست‌های پخش را برای گوش دادن بدون اینترنت ذخیره می‌کند.
🕤
بدون نیاز به احراز هویت اجباری کار می‌کند.
🕤
متن آهنگ‌ها را مستقیماً داخل برنامه ترجمه می‌کند.
🕤
امکان گوش دادن به موسیقی همراه با دوستان را فراهم می‌کند.
https://metrolist.cc/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vErkWN_my1CNJD0mruLJYo8lHEBKLgcO1nnXdYcvtB3usQ3dIePIFjFYHqRBfC1V2bk7mTlbteMyDJLjDlR8hkc7UjEVd93IPNqHmsgUb6J36TNZDcgcdV-Mv87YeNVGBOM7j5MDv3W1FraAsC7IK_1HNALk97XcTFAw9tmzoRiYDQcVrvsPOEq1Zn11z-1M6fgWhE7_GpinL0H-eevloAQemG_bYYUlgOb8ta8IEwGJSXq0tyuEJPirscQ8c3_u1ComVUnKAKNmer1HU0PdTUwrt3-AwmgPan1WtufZpLo6lmXHf083D2Hn3nKTOkaHM6hlfdybGTx_dXEnH6Hi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rod0ZpBRd4BzcstLxv9knja5KiDI4CvAc2XMEs-1VOwwt2NifRD7fk6Oy0VWIQEgbyA9QEElqgw1taE6r4vIY53dXLuUDYPTervY5y3sdRJt_2iLpBSbkUcKj-FeQ8W8iYXs4_wkPyh5SZS1OtJBbqpZ-1uXjTCMtGpt-gxmzAPTuT-QNahQ6OB6tekBmXB77krBD9BY9McbkFQxVfmEnceDi6gB1_XeHV_RcefvcEIqQQy7sjYAhjMvHuJ7ZOJzrosaXLIVOOMElTUBB6-qYfxLxr_81mg-p6GAanvS4CFHZTDlfn6eQlqo2md1uQJZzIrIEfRG4w2IbZYXzjgqPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">GoFly VPN
سامانتل و آپتل
✅
(اول با vpn برید سرورها بیان بالا )
https://play.google.com/store/apps/details?id=com.ambrose.overwall
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5944" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5943" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N94GRX0V78Tf_ydP_LVuMHGilrwlJ3d3A46Md_TjWViTu_pmMix-FhiDVADokMwjpnwuvEUs-qq1LGUHXuNhzeQQJYO6W9TeW61aSDJsbwbg3sgTk65ULNUb0UYCm9l8i1WVO36ve94Q0dCZBy0T4oYv32miO_b0lqaVBHjf3aN7LG9bHcVwv35EuM13EdEeX1s2_4yMLfY6RCh6AKgjSUgADHiaZWq1ylXaAXJhuyvVSGh_zqt62tiSkonCsy_CHgItUZAW0NJ_k3-SHDLA6NjuKT6hZ8i5LFFPpyckwHUoKw7TjJeaDkgD0c9DIfd5E9rZk73jPfVdi8SRUIg8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cybear vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.bear.vpn.super.fast.unlimited.connect
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5942" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTysdUKws1bcf0HZLfVIghIp4m0mgwLwtpknFmowCKcQGq2DbqGI130hDCQIhlfZP5vgunpzHdMq6ZvqDf-JeI_Ii7fY9dCpKEN5VqxusdScoFHc7TzJdIRS8UKBYYWLVsQFmkFQyOQsRZtcJ6enHTmcfbpdDp64pdLWHdogtgJtnQ9egxHyPzBV5_xYIEMyuUcuadBZ-sgYqDxPFzyQQd5OKVSjgT8-AtRW7eQqMmsh2eeiMoE1VlzfJLRewVd2yHRJqOuVpjhawoPpM1as5Ph3P44vgp04e9iqSMQSsK04gWzMmCwrno-KN6gXA8O_EPsdUhvyGNBncszFRkJR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Soren vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.provpn.soren
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5941" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubSh-mSTlOStjnGdVXIFqlY9KOFHIecfS_kw9ETlV4nS_ikED3aIvjrjxhZ5Di47gQ4Gc5dFm3jb5Ma-DCmYcnSePJA59pRer8NeYuldAtppspoxPL7o6BioetD7ubPK03IKKYTkpY9xJ0QlYLQv2V5Z0HpATs6i6vMk0rlvo9Wcr2T6xnmssSxZ5Q2tObSn_1zxF70p5onjdg01Dl8gOTWkcmLgHAR1nVnXYvXyG2oqdUZlodOlMUtABnBaWLWR2gEcHW5z8KA7U3ePw9olEpkRZBgTyPa3YdDSMuV6CzU4knl4Vq1fCfszTY0Z3uyTredRWr1CQb0VRd9GVdgTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥷
۱۳۸۷ تجزیه‌گر OSINT جمع‌آوری شده‌اند - یک کتابخانه جهانی برای تشخیص نشت، تجزیه و تحلیل شبکه و دستکاری داده‌ها.
🕤
شبکه‌های اجتماعی ، تلگرام و فراداده‌ ها.
🕤
جستجوی داخلی ابزارها.
🕤
به‌روزرسانی‌های مداوم.
🕤
دسترسی رایگان.
OSINT Tools
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5940" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">https://hjfisher.github.io/SNISPF-HJ-Configurator/
انتشار configurator مخصوص SNISPF-HJ
تمامی تنظیمات رو می تونید اعمال کنید بدون هیچ سختی و خروجی بگیرید و استفاده کنید توی برنامه
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5939" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🛡
معرفی SNISPF-HJ — نسخه پیشرفته‌تر SNISPF
🔗
لینک پروژه:
https://github.com/hjfisher/SNISPF-HJ
━━━━━━━━━━━━━━━━━━━━
⚡️
چه چیزی اضافه شده؟
━━━━━━━━━━━━━━━━━━━━
✅
پشتیبانی از چندین IP و چندین SNI به‌صورت همزمان
در نسخه اصلی فقط یه IP و یه SNI ثابت می‌شد تعریف کرد. اینجا می‌تونید لیست کامل بدید تا ابزار خودش بهترین ترکیب رو پیدا کنه.
✅
Health Check خودکار
هر ۳۰ ثانیه تمام ترکیب‌های (IP, SNI) تست می‌شن و اگه یه مسیر ضعیف یا مرده شد، اتوماتیک جایگزین می‌شه — بدون قطعی.
✅
انتخاب هوشمند مسیر (Weighted-Random)
به جای انتخاب تصادفی، ترکیب‌هایی که packet loss کمتری دارن شانس بیشتری برای انتخاب دارن.
✅
Graceful Rotation
وقتی یه مسیر ضعیف می‌شه، کانکشن‌های فعال قطع نمی‌شن — اول کارشون تموم می‌شه، بعد مسیر عوض می‌شه.
✅
همه قابلیت‌های نسخه اصلی حفظ شده
Fragment، Fake SNI، Combined، TTL Trick و Domain Checker همه دست‌نخورده‌ان.
━━━━━━━━━━━━━━━━━━━━
💻
نصب روی ویندوز
━━━━━━━━━━━━━━━━━━━━
۱. Python 3.8 یا بالاتر نصب کنید:
https://python.org/downloads
(تیک «Add Python to PATH» رو حتماً بزنید)
۲. در CMD یا PowerShell:
pip install git+https://github.com/hjfisher/SNISPF-HJ.git
۳. اجرا با کانفیگ پیش‌فرض:
snispf-hj --config config.json
یا برای دانلود کامل سورس:
git clone
https://github.com/hjfisher/SNISPF-HJ.git
cd SNISPF-HJ
pip install .
snispf-hj --info
━━━━━━━━━━━━━━━━━━━━
📌
نکته
بعد از اجرا، آدرس
127.0.0.1:40443
رو به عنوان پروکسی در v2ray، Xray یا هر کلاینت دیگه‌ای تنظیم کنید.
⭐️
اگه مفید بود، به پروژه ستاره بدید!
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5938" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5937" target="_blank">📅 08:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">100 گیگ مولتی لوکیشن
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=c4cb37f029af5828#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@crope.top:443?security=reality&encryption=none&pbk=Xgq8hNKvlfsBVHeJtXwjytbB5Fv2Tnu7vXJdZOgS8ig&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=crope.top&sid=b5af336756f77990#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@birch.gouher.one:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&host=stream.greenfield.lol&fp=random&type=xhttp&sni=birch.gouher.one&sid=28e92c6d545c9c26#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@meadow.pinevalley.top:443?security=reality&encryption=none&pbk=JfUgtIVRM26EKkksroAENXLWNJp9n28mSG-z-8CDAHc&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=meadow.pinevalley.top&sid=e86995a2ccab9364#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@rouze.click:443?mode=gun&security=reality&encryption=none&authority=rouze.click&pbk=PqunTCzbpHjmqH97ZpXHL0RBMyHaFzjJAO8i3uHr-XE&fp=chrome&type=grpc&serviceName=grpc&sni=rouze.click&sid=7fcb3d98608f93b6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@berry.riverpath.live:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&fp=qq&type=xhttp&sni=berry.riverpath.live&sid=bdf09e70262b409c#%F0%9F%87%A7%F0%9F%87%AABelgium
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@road.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=road.oakvalley.digital&sid=54aafe829679e92f#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@stone.quietgrove.forum:443?mode=gun&security=reality&encryption=none&authority=stone.quietgrove.forum&pbk=MchbHn3bpJaqAX-oqnNXYiXrbUTN0n-K203T8YGr8D4&fp=chrome&type=grpc&serviceName=grpc&sni=stone.quietgrove.forum&sid=0ae20b3e5e2c0bc2#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@flame.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=flame.quietgarden.live&sid=06d7e21ecb57367a#%F0%9F%87%A9%F0%9F%87%AAGermany
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@ember.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=ember.quietgarden.live&sid=fd488ee90cc0b9eb#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@valley.syrniki-iz-samokata.live:443?mode=gun&security=reality&encryption=none&pbk=euMfJzUx3qAGiaXwcvAXqXiqglBQKPOqxkTdSqwnqEw&fp=qq&type=grpc&serviceName=grpc&sni=valley.syrniki-iz-samokata.live&sid=c6046d150f597d04#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@field.wildgarden.digital:443?mode=gun&security=reality&encryption=none&pbk=dtxZ0lFLHE0IGfg45g2t1t7WwHWHuDW4xbfww3zKhDQ&fp=random&type=grpc&serviceName=grpc-bridge&sni=field.wildgarden.digital&sid=bbbbe9607d343bb6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@bridge.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=bridge.oakvalley.digital&sid=5278abf8d6d75483#%F0%9F%87%B9%F0%9F%87%B7Turkey
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@eveningwalk.sunnyside.city:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=eveningwalk.sunnyside.city&sid=54aafe829679e92f#%F0%9F%87%BA%F0%9F%87%B8USA</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5926" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@areal1.greewebservices.ir:2425?encryption=none&fp=chrome&pbk=xQnXh5EfPDhcEBB7rRiLca33GYrMEeUa35domLL_yA8&security=reality&sid=9b60d3&sni=yahoo.com&type=tcp#@ArchiveTell%20%F0%9F%87%A9%F0%9F%87%AA
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5921" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کدام مدل‌های هوش مصنوعی روی دستگاه شما قابل اجرا هستند؟
یک ابزار آنلاین که به کاربران کمک می‌کند بر اساس مدل GPU به سرعت بررسی کنند کدام مدل‌های هوش مصنوعی را می‌توانند به صورت محلی اجرا کنند.
https://www.canirun.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5920" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۲۰ گیگ
⚡️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5919" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVxn_T24B67Hyxq11CH22k0UAtlfTzpaU_J1r8KiiNe46TN8WETVQqoQG7PKbodI3khmuM-Q0k46U51J7cVnCFEfs2jv1yDNYkbTbsDi9t2icdzZKb6T3P4keDPjdGInmt-sMz4rhOVxi2l4T8diaPPxJi3UbO7xfR2_jtn6VjmM1X-pjx-XcXz58_FUCapdNL1QheRzxJyqUjQt_aovkU_wP_-06f_2NRDhEtGHka3N2QSB306aTJB0KUBWccw9c9t29XmjHoT_F4jBMRKYj6QUcDaZcF07R_RXFqxeGBmHrrYoD73sPFkFZTWGtbduXKcv-VY4Dz8_B00b3o2Xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚒️
۱۳۰ ابزار که جایگزین تمام نرم‌افزارهای اداری می‌شوند: آفیس، ورد و پاورپوینت. همه چیز مستقیماً در مرورگر کار می‌کند، بدون نیاز به نصب و محدودیت.
در مجموعه:
🕤
ویرایشگرهای تصاویر.
🕤
ابزارهایی برای PDF، ZIP، CSV، Excel و فرمت‌های دیگر.
🕤
تبدیل فایل‌ها بین ده‌ها پسوند.
🕤
فشرده‌سازی تصاویر.
🕤
فرمت‌بندی و پردازش کد.
🕤
کار با صدا و فایل‌های صوتی.
🕤
ضبط صفحه نمایش.
🕤
ابزارهای متنی.
🕤
برنامه‌ها و چت‌های هوش مصنوعی.
🕤
ابزارهای ریاضی، فنی و داده‌ای.
https://github.com/aghyad97/browserytools#-features
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5917" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">VideoNote: ابزار یادداشت‌برداری و قالب‌بندی محتوای ویدئویی
یک ابزار یادداشت‌برداری ویدئویی کاملاً محلی که می‌تواند محتوای ویدئو را خلاصه کرده و یادداشت‌ها را قالب‌بندی کند.
https://github.com/xiaokeaijqx/VideoNote
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5915" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8GiVfMCO2_DLwn9wUl54ZSU4u-cvN6Y0C4HaHsYeBTa2FPGmKJLarR7P67KJBJteHV395PI4jXPzqxHU-YjEhYFA70FzCuo-SEShbUA0GBxiKhnTxxwGaN8fN6e0isQ_NvV_MCsqcBsJ-q7rMySI2MQNw8BByYh01vUoBcGVeujgLy2Z4qbR6IQ6wlWD4_dcijkf1LlJ1yeHu7fpsnZcaQpDhDzCmV5r1rfBM7VMKkSwGmvAY-zZgMmMpQNb4UQE-zqARDolaGKQ7Qk1qwZwgL0r61K5dwlnNuAfzFzJ5ik4LxeNSQGaz0pqk_9x6y6GaB8EQ11Kh-XNVY5lfFCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WU4n9bGBakVZk4Q67xfVj0VTEICUoirC2rh0iQIknD5VLIb7jMB8Zl-95IRI5vo8X2-h-N8GbGkOEPfLgPDLWGHMcs6bbAnY9SWicg-puTPNYHoU_GWacdb_n76nyMbFM7l_x0xOiW6xB-NthcFtpCNyBqmsaX5pryzjILVNlByzspG7sKMmFfkGgMeKg2yU42hlHeRK4t8gdxTghGRY9oTAGcXNXeK425bcZXYGhsODvH_msgLw1SU8OqXS9P4vqGskRVRc4jg5hmTniZMh99_mj7oVIFVYdVwo_NFY1p5-iY1I555NTgHvLiqBjOaEAAasoSz0jvSXII2OvZTGDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت عکس و ویدئو رایگان
https://www.mindvideo.ai/creative-studio/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5913" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://t.me/proxy?server=47.86.102.135&port=443&secret=dd887aa96cd9b760d42f62217afdcc6bc5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5912" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFRxqNpC-ffbcG27yNvGiap73Chb1IMCv9vI5ZJHtrkXrjHIYvdt65SQRVbimGiOVf-ypair_5jJ-jCpRBEfy6N2sDdj4NNNHgYBZXG7Hn_BoAlKSdPNclUfzlbJoiFk3gFgTljiNPncgtXNP5Im3e8d8DbFEUwLeQcfpvXZ2D3JnD_-IV4sc7g7XshnKX_HpNGJoQdrbPwE8wXsV5byfDrg7I3xDU7eNd78r5Ux0Fan9OKOi8d9h1lXoBLAktJ_1EewPtf9BWlmwaE-XXf-NbnN0a_h7BCw5_dLeuQSWnAaZE5Z5XZCF_NdN1q3e0JkPi_2Q9_tLop8LM9A1giLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ویندوز 11 را تا حداکثر توان ارتقا می‌دهیم
1️⃣
بهترین نسخه‌های ویندوز 11.
🕤
Flibustier 25H2
ایده‌آل برای استفاده روزمره.
🕤
Revision Group 25H2
حداکثر FPS ، مناسب گیم.
🕤
Ghost Spectre 25H2
فوق‌العاده سبک که حداکثر بهره را از سخت‌افزار می‌گیرد.
2️⃣
حذف زباله‌ها و قابلیت‌های اضافی.
🕤
Remove Windows AI
حذف هوش مصنوعی که منابع را مصرف می‌کند.
🕤
Win11 Debloat
حذف برنامه‌های پیش‌فرض.
🕤
Ultimate Tweaker
بیشتر از ۲۰۰ تغییر در یک ابزار کوچک.
🕤
Open Hardware Monitor
کنترل کامل بر سخت‌افزار
3️⃣
نرم‌افزاری که بدون آن ویندوز 11 دردسر است
🕤
WizTree
— بالاخره می‌بینیم فضای دیسک کجا می‌رود.
🕤
Revo Uninstaller
— برنامه‌ها را بدون باقی‌ماندن رد حذف می‌کند.
🕤
TaskExplorer
— مدیر وظیفه با قدرت بیشتر.
🕤
Explorer++
— مرورگری که واقعاً راحت است.
4️⃣
ظاهر و راحتی استفاده
🕤
Windhawk
—
مدهایی برای بازی ها
🕤
Jax Core
— پک‌های بصری و ویجت‌ها.
🕤
Seelen UI
— سفارشی‌سازی عمیق  رابط کاربری.
🕤
Cursor Mania
— هزاران نشانگر موس برای هر سلیقه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5911" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال: @ArchiveTell https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5910" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال:
@ArchiveTell
https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5909" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
