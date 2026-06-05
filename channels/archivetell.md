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
<img src="https://cdn4.telesco.pe/file/KTuBCZObiK8Y9ObVw5_9uUUKvNfrCEHlzdAYm9i74wDHngWsAaNNIOwJRwpWC8DY7mfpIrCqHrDBhZRMaEdA68-QqATdLzIfAS4rweE07KLbf3kgbqb5RpB2DLpsfVkTIc_JjoN7iwoo-7YZ2GJIN1n6CwXBA7JVKJ7KbV9gkuWCndG8tSoA0pCePjhRk0Ds2hpOYZHlnVeH7vBZVsa6UWqvYUW9by53d69WEyrBbwdjfkQq4OKMBaNKgVjGThDi3rwi9g5SF_5F9bGOQBvOEeqm5vmpA6JJfpu3kAlcxuuaEl44seo6q2ZLyK3UzZHqYo1kpYArkXGrvjslApEwNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.21K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
معرفی اپلیکیشن AzadiTunnel برای کاربران iOS (آیفون و آیپد)
خبر خوب برای کاربران اپل! اپلیکیشن
AzadiTunnel
منتشر شد.
این برنامه تمامی قابلیت‌های کلاینت محبوب «شیر و خورشید» اندروید را به آیفون می‌آورد و دقیقاً از همان هسته قدرتمند سایفون (شیر و خورشید) استفاده می‌کند.
🔹
ویژگی‌ها و امکانات:
✨
اتصال امن و سریع تنها با یک کلیک
📊
نمایش لحظه‌ای وضعیت اتصال، سرعت و ترافیک مصرفی
🛠
دارای بخش عیب‌یابی (Diagnostics) و تنظیمات پیشرفته انتقال (Transport)
🛡
کاملاً متن‌باز (Open-Source)، امن و مبتنی بر حریم خصوصی رابط کاربری بسیار ساده و تمیز
⚙️
آموزش و نکات استفاده:
تنظیمات این اپلیکیشن مشابه نسخه اندروید است. در حال حاضر بهترین تنظیماتی که خوب جواب می‌دهد، استفاده از پروتکل
CDN Fronting
است.
همچنین اگر IP و SNI خاصی در کانال‌ها پیدا کردید، می‌توانید به صورت دستی وارد کنید.
اگر کادرها را خالی بگذارید
، خود برنامه شروع به اسکن می‌کند (ممکن است در اتصال اول کمی طول بکشد، پس صبور باشید!).
📌
پیش‌نیاز:
قابل نصب روی iOS 15 به بالا
📥
لینک دانلود مستقیم از اپ استور:
🔗
🔍
(همچنین می‌توانید کلمه
AzadiTunnel
را در اپ‌استور سرچ کنید)
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 451 · <a href="https://t.me/archivetell/6056" target="_blank">📅 22:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
800
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 36 / 800
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/archivetell/6055" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1ZwzlUiHdEvfd7m5JFprCtubLyJbtQAO83eAy31FmFfDEHyMd_Zln5gc7crt1RRGplrnSKBg_B2Zu-KPHQgnLH2ykKm6__z2N100JIxx0WOHJ_Qnl8YzQtocF8ojrTfEDRdATEzAU-UwzhXGSSogNJWiueXc5Ulf8QzVBZvfGqrfPQhudWLcSTUFNimK5dg09kXS0SiSZb41rcnOmhgioUhYgyJIZU4qMcDh2VPRjjGblhtfGm4TYsqeLaklQniGJy83fMN5HPOn0NHrTY9vYCa24OyMiwCYL9ce3vw9iEYBTqbaapg4180Ua6yYjDP3mD8CkbUtnrLs0gR2V1dzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرشیو تل؛ مرجع محتوای ناب و کاربردی
🔥
گلچینی از بهترین مطالب که نباید از دست بدهید
❤️‍🔥
به همراه پخش کانفیگ رایگان
🎁
عضویت در کانال:
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6054" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiYNbzAlJP7SgwVKBrZ0-L88am7ltO-oI5BADoSBewCHp3S-Oy-lihoeUa4iomSzdatE5BEUIDZWTk-fGmEcpI1aGY3mMB4ZGylUMC1R9UzPDHBM3aR47dR4WUeXWjHIVRns-8mtTWq-yAdzI3079ktnrw5danIVYoZQRoot9LNEq7kfIGhs-9kny92SaA5NUO6YILMgH3eXWr26I_B7VbStiQqGg6z-vlvBSk2juUYX5wtXNcC0iMkmwxZhACBRRtwzo0UFjGV561d1d5uWTCQRBwoRdYl6w457TiBxexKzaHDEhDWoRO_7_2d49kvwCJy-fLRw5m_K9zr7gcKLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید ویدئوی هوش مصنوعی از متن یا تصویر با کیفیت 1080p با Seedance 2.0
با ثبت نام 10 تا credit میده
https://seedance2aivideo.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/archivetell/6052" target="_blank">📅 17:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6051" target="_blank">📅 16:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6050" target="_blank">📅 16:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sorrow of Sophia</div>
  <div class="tg-doc-extra">Draconian</div>
</div>
<a href="https://t.me/archivetell/6049" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6049" target="_blank">📅 15:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGA3eUNI8YaS9bQw3wIAmrNf0IB0lpY1VkdcNBP2o0fMaUbasSiO2WZQJLcWbkykYGUDYzOLrBcYG9F6fBc8r-Gglsgq5APcf2TwW1jB8ICf1VBmIwufqXS4Pi_4CZMi3XD5D8gpwD-ElNWEvziYmqetmaJXTDhODHM-JQjTbIYDGjoOyqEFkvplqiyrsQFB4BWCD0Xf9T6QJmKspE7_3q9ysKY1_1Qp9SDI1Clnqp5mkyksoZ8q-NZ-MIzz5bqvO6Gk8CubX3u-eadc0wWNWTNLaWVIlJQBzxI9txuPq9ZdPfrVLn5bewv-zsmb4rTAg1ugvPhYFtgPTiisJpU9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه 1.3 قابلیت QR Code به پنل برنامه و صفحه وب اضافه شد تا اتصال دستگاه‌ها به FileShare ساده‌تر شود. حالا کاربر می‌تواند بدون تایپ کردن آدرس IP، فقط QR Code را با گوشی اسکن کند و سریع وارد صفحه اشتراک‌گذاری شود.  هدف اصلی FileShare انتقال آسان فایل و پیام…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6048" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7pL6dKce0pbcDhwpEv5jIc9wbq0DcNI-LmwnZK7HZxeT1KRIY-9S0aRYdGkT-Ol8ZThy8--hK9QZNQ-YsbNhmwgJQdcumdn2aRa09kYbbx4_P-RsFoFUUDhfPddBm_JianVjB321UFTpx-_weSzmwghDbM5nVfZx87-txcyR47qNotCTaGhb4uoOxpuGjRct1ckv-4sthzTl5Z417-HN_3xuxmDoMoq2Qh65ld4X_sljv1wtugIOBqwMWoA-wvA1HqGfGXworAV74xsE4nJ_u2VIQuFJMQL-DT__3q-o6VMhWG9-2MKPyyzk1yQaiaf6Lvd9lwdHVlrsu4vyP_vRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">FileShare.exe</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6047" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/6046" target="_blank">📅 15:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همه اپراتور ها وصل
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 100 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: پایان یافته - تکمیل ظرفیت</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6045" target="_blank">📅 15:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6044" target="_blank">📅 15:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
کمپین جدید
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 58 / 100
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6043" target="_blank">📅 13:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
همراه اول Happ
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 169 / 600
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6042" target="_blank">📅 13:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6041" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/archivetell/6040" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOxfo90rlYov2gHYD5x0KI7PcRzyeff-vVZ0s1a94E3NipAHOEQDf90_t4u_EtGErsXDRYJXC7DYyOOgFtUpWTwwZbDH285Rlwqf5mbCRhB3xXOpXknG7igIhGGgflTZTfABaFKlzaJHcV2OuENLdTWV8teEqbLt-jESHhSUJJL7Qal0lrInLyTYNjFUlokhZ51QMOUlDpEff672yTTrqCH6q3VAYesEC7XMH2NOvoB0HqT6buAEveJNCDx5pieKDKTjsFVV0UPysPiOGYkGOBFTClGZx_J2YLxbX-GqcuEahp8TK3YZ-9s2DmYk2ul-d646_DNmEXHkz6tzT5U63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان پس‌زمینه تصاویر با هوش مصنوعی
پشتیبانی از فرمت‌های مختلف، پردازش در مرورگر به صورت محلی، حفاظت ۱۰۰٪ از حریم خصوصی.
https://quickbgcut.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/6039" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6038" target="_blank">📅 13:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
اهدایی
❤️
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 280 / 352
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6037" target="_blank">📅 03:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6033" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6031" target="_blank">📅 01:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6030" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6029" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6028" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چنل های رسمی مهم:
🟡
چنل شیر و خورشید
🟢
چنل MahsaNG
🟣
چنل TheFeed
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6027" target="_blank">📅 00:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNJeW60jJKjxWJFxe3Y3iGFUOF25onZJ5xt2fqvzbYvqTF6Y01uvvB8MCbLEyi9yl7s0Wy9e3afNILEdAHpwYTecgF1LBxjh-Jj5IA7wn3pl25smIv8t8S5IaRLIjRn13xDnRo4CJ_PW7DN-StHCcpBgNa5x9qOLlzcWLrqSkd_oPlthOHXZUcrzR2nI8OWlXuVESXQhuW4VrnF-e49azl0yfFlcBKdUC-YLHqh97LIyQOD2APFD-hko2ZswJVWtqq7jsXFesiDQ6lFVHPeBA6sL0rBK0qqwTS77ndYACdm5ab0gG6kw_0F-5uMtAo2M-vlRfMgNhTcdJxR1zC2h1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال کلاینت شیر و خورشید را دنبال کنید و به اشتراک بگذارید!
https://t.me/ShirokhorshidOfficial
دیروز متوجه شدم چندین کانال تلگرام که خیلی هم سابسکرایب شده بودند خودشون رو کانالی برای آپدیت های این برنامه معرفی کردند. دقت کنید که فایل نصب برنامه رو از کجا دریافت میکنید. فایل های دستکاری شده و ناامن در بعضی از این کانال‌های جعلی دیده شده. تا جایی که امکانش هست فایل نصب برنامه رو فقط یا از گیتهاب برنامه یا از همینجا (تنها کانال رسمی در تلگرام) دریافت کنید.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6026" target="_blank">📅 22:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6025" target="_blank">📅 21:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6024" target="_blank">📅 20:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/6023" target="_blank">📅 20:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6022" target="_blank">📅 19:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعضی کانفیگا تو ویتوری ویندوز وصل میشه ولی رو اندروید با همون نت وصل نمیشه
راه حل
😁
از کلاینت exclave تو اندروید استفاده کنید
😎
لینک دانلود از گیت هاب ؛
https://github.com/ExclaveNetwork/Exclave/releases/tag/0.17.41
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6019" target="_blank">📅 19:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzknUDhiw1VudfeQu5P4nW2q81YU2rMwrT3qVVNgi6zRkAlQG_nspS35vTR_voj8EPXhZwyJLT-k-kotLW7fKWhS-l9dPwhSxmpNX-HrQzH-x8UomGc5MVGJ0ZqydqySvlmkOba9Vcl1tFIi8FqYTd5QzMc2qgkVSrlxlSe3M0PRo33KHFUZ5ts7lVugsa_xdu9Nx5fOOsyZURkvie5ikvf7uDazPrMbabpELTt4H38rTw1ghdsjJ1HLVzvvN7PURz1somvD6ol5I97lhTiQe8VncwsTjJxKbtzBCFMnc3m1c6aGi_MQh8uuHXnM7F80kkppCcpJyCVH6h91-eWNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgbKCKiSsV_kxFQ_LBhiA9WBthpgv7GwX4_Esop_l-gr-nqt47SdKUOTpZc1CiXcHiwf4pwXBRynHVd1U_UEMSMaJmvJtTxy_teENgQiGCU67jccg3pV3swh7DYX4v9wUFt_t8vekNXXFJD5yZOlns25JVhmzgNnMWa_sWB_CzAwcCmWEoHYaPRgLQTxR7iMcOJB8QKqvYsRp94DzIhrUvx5Fd-3jR_mQYPigkaGXsaiVWlWfOPSp3DzlIXfebwzFYHSGwe7iQ5ZFZ6AR64XbwimO-tBj-DRTpwrCFkQHiDd5zf6BGTVx7d-Hk8j6bn0jaAEOBWDkaxGviORI1ps-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vs2SGfyj1Y_g_CcRehPsvQ3ttSaFn-54ohwxXXSVuLA2rgzyjHW6TsIJgrZwBqSz6-nbRrvRUNcfZxvMe2YboUcnOh2eojV82O9VJAkvqha0YnLv8yiLCQHEN__TFMBgWrDy7hxfF3sBx_QlZFMRBdCMCWjb1H_XAji03JE5ksTi6nzAs3edHJzRkT9gfnhycza3tMmXjDSSToH4Y6f0fp0kv5DUia5sWVyx43BIW0v5QRcJd2JcvFxMPZAK_6uPlmamf5me_p7mdoTBDlHzK6lCj-4MJAIWat0HQbdZCkW9UKw8gbRetvQHlvoKY1KkUmSjuzYvFdO1mP8cMKPjWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNFl5XrgBiJec2zsg77QNeBB4CBN2GaYZBjH2oViavDADGfbdBUTYh_ZABNSBeSaX5KDDA8qDrclM823TilNlJgsrpw5HaVpdspapA-0uS9y6I7ZO2vqRFoYMR5hMUax5l6KkEOh8XRVo-idF6CUr_eQ2x80kGr5VpDancNONuwihuvSTPT6IPWsJcoNXlkz3r1XyUxbFeCdtkMdD9-_8D3zVWHKZusmvs0IkwToD_kx8ffDS2k_Y7ODS28YagwU6yy8l09TUSRz3GOsIoo5AqutvZ4oVJvcxEfFsejKDbxNPClhbvP234Z_eYkRJxWg5xlNyKXlKjiW3--j-cdC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrMBBjOtqtaS5V2u6pszRyaaCUnK1ipl9V3JDJcP1Y_m7I7JaTwDrGnPCrTPOpBk6CVKeI_ZECTX29SOA2yC7cq6GDeSPGO0RiH5TP-mNQxePliWgDFmNhYsP_I8MSp6JMqjhIIvWySVGpp_36zoAR8zQOrfHgQydjMtXIuxgFFodxk-JarTrnErJMumKlYBQYxqBItTnDFrV8p8QBusQ95GqBLc4ZT0vodw6rsEvPWA144Td70DdoAUsh3umzSxFmAJ6M2ix2UAKUNwqcyYUd39cpRULCRWk8xyoQ-nJstF9zwDt_XScuuQGQtW8sojV7SmWE3_v4LTRtFP29jdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZQ-kTVibk7feBuOM6oUeImTgj1SjJbzlqPq_gU9mf-Gb9G8MJS3mL7m9m8WeEn7Q8FTSy_qk4vFzjegEup_ebhSvyha4mLwCbU35-HlVC0FsyGrWCn8TTiLy5y9z_O8SBhDZHQ8icxXvsr7dyGLzinNxDES8ZtM-s9rEtlpNcDoNV75xygGgiaNBjhFy_UH0O8uBp5MNtUl3Hd4HAHGDFZLDD-Aju7SWWVC5nRK3rrfu6p-LwFhD5BhFrPw_0Y_HrWqnmBCieY9kgtP527da7M5MMj6RT4B4w5Kd3rM_Sn1BD7dPGsYwQyfryka_c0cp-JBYhxSyzh_YfniJzHijw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=KKZNDvb8woRhJg0EuHc8LmEg_X4vdsPKdkes6ThSK2npCrfpOPlAMAMzEexVLMtpX526tQoYXCkwNjh758m5f5UOOfbhZpA4BxMrbZpM2qBNQ0nQrCxX8I0yy97yduLZd_OkC4gpvAzo-TFyKB57zw2sYbJhJNXxb57JbWpuOldqkpWG4OyPCM8s5tukefTwed5VUP5NoErlIMV9jKmrM123rjo3-nLkCoBvNvvY8I3St_oOiOR2Gw2lc1Lj1oT6hINWjrZzZ-A1Pb1pI6T0CjxSlQl1DCWynluizh711wg9Nzo03mH2dsIfadOl1DyXfQo-_3dA2mcvvFMrCZar7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=KKZNDvb8woRhJg0EuHc8LmEg_X4vdsPKdkes6ThSK2npCrfpOPlAMAMzEexVLMtpX526tQoYXCkwNjh758m5f5UOOfbhZpA4BxMrbZpM2qBNQ0nQrCxX8I0yy97yduLZd_OkC4gpvAzo-TFyKB57zw2sYbJhJNXxb57JbWpuOldqkpWG4OyPCM8s5tukefTwed5VUP5NoErlIMV9jKmrM123rjo3-nLkCoBvNvvY8I3St_oOiOR2Gw2lc1Lj1oT6hINWjrZzZ-A1Pb1pI6T0CjxSlQl1DCWynluizh711wg9Nzo03mH2dsIfadOl1DyXfQo-_3dA2mcvvFMrCZar7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQfNHoX1nwUklRA2kdMv3nJVyI1t8nIxbnr6TXJ7o2FpgqFJ8-ef8gAEAUD0r2ftef96kNxkPpu_406T6-bKLFa4YWh8mw5wN-UfcqmJNI5m35Nkqm4sdg_l8AziMmu8VdEhwVzc3JRLoAg4u4SegyhA0zFN0965g8fS5_XDMzVwL0omWVtye4xlM4GUtYdBgcYtT4I64f65lTPpuMokiaibGFM2TTpN7TKSzw6bcOJF-tkUk4_M009bQJnT2h8W_TYM945ERAqeLuW-5Z1LcunGG5obNUHv29tkgFKMRWI7FcK8afCfdf6rmpvVXEIDFY1K3KmJvRxqoC0VfQPZDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riMFiXFIYLP4HOklun2at3pivi1d1OzFHBSPsJk1G-qvf1HFRJ7nIIM3uKj91b69s0RA5oI4-LKlrZXpd3nwXQFK5yId9r3HqVF6qXDYAu8AIsXkEtNmrJOWGv1d1fXDkbQUdRcwco2bRwiLwfI622APeUGj-ys3kwPjT08GHTUrkg_rM38kwyi7IPUSYyQNs9u4cuaQ9jFXqPp6RcSXbbOUb9PoJOJacR7iDFZJjN11o_QAh2hQ7mFa0KU7yrqu8kWrHrgdAYt8no2iThR1llMhPMbRvKJw6WKYmah9dr3m3hFhoFreqgKrPNkPo1eqcr5WxFGq2pvGtu_szR5hgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=hvMJjbVoA_tfvFkYRSZO6ZLVKKqDH0EZzwx05Q_197mlfZABuZwyv5nOEG5VIOpCSzCOmwC9Tf8fOQGHSnsnDepK4cy2iPnfP6Hv0irkBwq1Ie5vBzZXDU6uka9C8GUqKOjFJoCXUSK1vUWjDbP0Mk7mEHdF0v08Vc4n3B6229u0Do_vpjJ2rcvrC6ltWnPZVFI8bEeA4ulXqYiEgsQbsOXJhoos7n34riGGPK-Sp6mCgSg_89-QozdHs6wydO_qippWxD3Nmf9k3rbNFlkIcCE20PXBUGHvV5U1vSOXrEyRQBERQKZvMuVwk57oJSiDHjTSdvO61cYHz2av31wE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=hvMJjbVoA_tfvFkYRSZO6ZLVKKqDH0EZzwx05Q_197mlfZABuZwyv5nOEG5VIOpCSzCOmwC9Tf8fOQGHSnsnDepK4cy2iPnfP6Hv0irkBwq1Ie5vBzZXDU6uka9C8GUqKOjFJoCXUSK1vUWjDbP0Mk7mEHdF0v08Vc4n3B6229u0Do_vpjJ2rcvrC6ltWnPZVFI8bEeA4ulXqYiEgsQbsOXJhoos7n34riGGPK-Sp6mCgSg_89-QozdHs6wydO_qippWxD3Nmf9k3rbNFlkIcCE20PXBUGHvV5U1vSOXrEyRQBERQKZvMuVwk57oJSiDHjTSdvO61cYHz2av31wE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMHEecwVscwhF6NyQMZnG4BW9gpUwdSjEB-qIuNGnd3rttH6__JxTwleRhr4nWdBk5ql4m24AGyDpjT0XRai71tuXeFwRQtQuzaHWPRM9XL-p6lIADIDOfWYsLEhTmFmM3-Vpuo1gpaKQcSSvskbEEL_iduTuMZ_zceqogftaDYpnjxLChUPYZAm2m94K5jZVDufpxn7AxhI1JgQxe2uTFVE4mBBXDWwjk0v9KHjZRa4ntBCj2d1WsxIVP11qE77zc-acrAimEk55yDPEVT8O5nynlYNGY6hEjGkc0LSc_VsT_t9JNPPzu0MfKKdxcXlbQ_WAAIwAv69ioEJg1Ikew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=LjF2gQ46cue2uIXe1LFIMaFFvMahF-cZ41mDOcaDbMcsSqfsWIPSzONuzK-JFndBOlMVhMuAzDn6cHpSmsN2ioLwDHD5ws5CywkE7Tn4U6QMdRErvCquFptT_VwAI3-M781a9UZz7kJ-GACpEYRQaWmyrhd5EBFtqavNOTEElZrxUFr8-QUxXp07jxSchYwPmc4fmcqHsjJheh0cXVtjsfqQ9-W4fw9lM4FAXIACT6O7y7wnPqlh__9F9sJa08vQ5ak8Tb4e1p4o5giSxTqoqleleegBciRuCAOaUXkaYEGYKrCI-5KKO3RBcFskULi3ykIpyly6mrUTJ9xjrmVuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=LjF2gQ46cue2uIXe1LFIMaFFvMahF-cZ41mDOcaDbMcsSqfsWIPSzONuzK-JFndBOlMVhMuAzDn6cHpSmsN2ioLwDHD5ws5CywkE7Tn4U6QMdRErvCquFptT_VwAI3-M781a9UZz7kJ-GACpEYRQaWmyrhd5EBFtqavNOTEElZrxUFr8-QUxXp07jxSchYwPmc4fmcqHsjJheh0cXVtjsfqQ9-W4fw9lM4FAXIACT6O7y7wnPqlh__9F9sJa08vQ5ak8Tb4e1p4o5giSxTqoqleleegBciRuCAOaUXkaYEGYKrCI-5KKO3RBcFskULi3ykIpyly6mrUTJ9xjrmVuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOUxs8FtPa1amtgP-X5b47O92kpPYs5RMu4l4-ftLpoHyOrhyLh7KaWrH394smkH3_aFVFRG95fQ8U28qb12XkyUJq0u5k3waclT8yyOQDpENbNAwUjmx99JH9DRv5098ubcv0c3ihnWWtJXtDOWxQa1MuSdyzZES5JVR5N_yk5b1DRjopCYCe5iwLZPZ_Gv_TjNMdQwtSa61SMQi5t2eVONgy8HPKHXc47z_lYkHnzoSIj01Pg89DAdwEAmncdsatFUWtkClQlD3T8shsyDtg3gq6kxEka3CDSSiO-hjgRQpbCp2v8nX8ro6EJJR0Ecb37U_-3Dzye7SE8YdlH3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5967" target="_blank">📅 19:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5966" target="_blank">📅 18:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.  کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/5965" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.
کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5964" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">vless://c2b6a323-19ec-4e4f-a95c-8b0e99aa7660@109.120.138.95:443?security=none&encryption=none&headerType=none&type=tcp#%40archivetell
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTRjYjU3NS0xNWJkLTQ2NjQtYjk0ZC0yZTZhNmI0Y2NkYTg%3D@109.120.138.95:28655#%40archivetell
عشقا تست بزنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5961" target="_blank">📅 18:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb7RlTKyJfVVP_t10uwLZyPXjkgiS2TIsJ0K1xG9W2ok5prCccIezVhle7BqgtkQrnHPClWu8JG6IZQJ4P6u3WTShFSdbuiOQ7thPw2I8jzQhLrhFuYeuLC_ORTuligGct-6gyK_cazLTG8iUJWcFjfX90LYsFnlOMYge3Mo0CfLiHrWOd9bBGHGbAuP8Pbnrnk5qf3Qez0jh5Z6CRF7NPwBGFK9qnIuFZgKyPRkU52749P97dDew7RwifWwrzAVPfvAaQeILz-7JKu8Tg-lFAdjPSYE9ergbWzQX6fXL57amircdLvvtmlv0qu5y0ZA5TBuoCrdNzCEyZG1IZEEsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5960" target="_blank">📅 17:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-70M6eZ065mPupk4ezC4-guyW2o51p8AdNorLuU9XJg5MHliPyWCDQtrq4WpvZbWZ10gBBsF7iagobaRFoYDmA5ZJmAmGm-xYwPWZXJbchnJMtGq-x1qz4x9aPnrunmV_oWWTXPVewRN-SxlcsCuLwpKCPENAjO3CgAvTSjJEU1uwh-rH143GxKJXZwaQhpoX-uKWfBUWjx8agGz64ZqFifAjV7lM0NgSCaqbVyq8OZM6-B39sn3qqire_RJuKkr_Am0qistry8oBMx4d7rG5JItdkRWPDb7uYXFqlzEajhrGxCxlTdLdzqUie-7zTzwusRQVKIZcGsx7QYiHjcGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaC44Q-S0V63FS4lCUzkZeF2ve2pN5p9T02TuVD3B1Nzp7Dbu0DdW5NzyDqvfo2ePn0-0XJZAgXEnH9oLVuJ6x1QU_ScYO8qp-dlrGyhsWI3dibiIO6HKvYNpqpj9xxeG7RTCLIubutSW0O7RUg76bZVxrL_VwwS34LRxicJfiRemepR7GX5LMyZ-fvjx9CaEASlyff_wpFEkCa0yJ3AbaG3rrGU44k60HiN496BzvoShf-N9II_1XRKQWM_ihdZWzWSdWH0MA34_7-2Q0QKJLV1k2HGbQ2VvB90idKevlREIVs_qu0da2PkLDYxe13kPYOgan53lJXB67BZ0iQKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=Jh0LoJ1nWbwxqwPHGUA-c1D03iR6ag3JFUNyNhp1TOgSEDi6tw2VQ7eTdn3y70USwc6MdJz0h1l0Y63UiwFqvPtJj7FqsJHZaOjQRgvG4Aw1CMbSCjDnI1kCVQW3uSBw7k_ZRb-HXezGHdVJCz0iPqfm8CMuEjLTDNO49YDGgXZjwid2gOkWvPBbGNMwI3IJm02Ii6bSjr-8QyMiv-joxY32sX4NXqANfYeI4HtZpqhexsh1d6DdbTmZ9zUHiHI7zos0mynfVAGpQG74LHYD5AmfPP-NHA4IYwe2NGXtY7qN0MMc934XSJs0f6UWePxquzB2s_4IWOAZ3be76b8cqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=Jh0LoJ1nWbwxqwPHGUA-c1D03iR6ag3JFUNyNhp1TOgSEDi6tw2VQ7eTdn3y70USwc6MdJz0h1l0Y63UiwFqvPtJj7FqsJHZaOjQRgvG4Aw1CMbSCjDnI1kCVQW3uSBw7k_ZRb-HXezGHdVJCz0iPqfm8CMuEjLTDNO49YDGgXZjwid2gOkWvPBbGNMwI3IJm02Ii6bSjr-8QyMiv-joxY32sX4NXqANfYeI4HtZpqhexsh1d6DdbTmZ9zUHiHI7zos0mynfVAGpQG74LHYD5AmfPP-NHA4IYwe2NGXtY7qN0MMc934XSJs0f6UWePxquzB2s_4IWOAZ3be76b8cqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=aO93jm2fzQAKhSSheDUd_jFnTqLQW_4IQOeoBAcPjkjm2eKiyHvYiQyc_WzgWE6QRspE7aYhbE4b6Z1nmc0UNTeyfwR_53HkXrGL2fZ9Ol-mY314ZwbHhru253sLoPvKB5WBlB3EYwK1mF2TuFNG7VmElbUMNG5sSjGXLvkOJ8UPsO6r3bvjE_7LSPKkxJ3P-6dNWkIzzOfS7-jfCofqVkhfq4JxAawWnja5_zr2q_6KmWFapjkUaER8eu-8OInf8WuaBQd-9mbgenjKndCBufcVWU0Dc4_8Ywbk-TcIQpYhq8U9oGqeYP73WVKmpY98D108SJQM5UdzJAAwOhermg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=aO93jm2fzQAKhSSheDUd_jFnTqLQW_4IQOeoBAcPjkjm2eKiyHvYiQyc_WzgWE6QRspE7aYhbE4b6Z1nmc0UNTeyfwR_53HkXrGL2fZ9Ol-mY314ZwbHhru253sLoPvKB5WBlB3EYwK1mF2TuFNG7VmElbUMNG5sSjGXLvkOJ8UPsO6r3bvjE_7LSPKkxJ3P-6dNWkIzzOfS7-jfCofqVkhfq4JxAawWnja5_zr2q_6KmWFapjkUaER8eu-8OInf8WuaBQd-9mbgenjKndCBufcVWU0Dc4_8Ywbk-TcIQpYhq8U9oGqeYP73WVKmpY98D108SJQM5UdzJAAwOhermg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ArchiveTel
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کردمش یه ترا
تا جا داره بزنین</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV61as8-4SF2BlNKJFvgAyw-2p82F6rSareGj55uGL2lB_LzNMD2AqHnucr1zH-pySyWUgjsXtaa5JVTvztyU-EvNtgV85jhqCCgQJpXaTsG-K6TfO2gkL6VhwIbKkmX_1utIwa872N_MRRqhAIgBxgVFun034YsWxwi6FDQo6jJw5GMMOMD2xwC0QGtvv-mG9SyNxE7RERuNe90O4ZQkZ16H7bYoOXCeCXW_uzZM5bPX-s_SA48dH4Lj8Umf99bsIPBs3us9n3OgEPOZyvhmAzI028gSyaxsW-zZ8WfN9DGGhpTaag5RqvU2Mp7QpA7ZH8q5QRW2uScyCJ_AJ6NVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4OGAuyIopwtoClPolYQiS7jKipWTFnintnmKvsJPVdCN-ateyFwN6OaATfHBrwhZHtWBR6_WRmorhgOVt8CEf31uuUfk2cEJB5ps0ZMEHtGCtfFxG3zIN5kg-s2ruo5TjcocZ1bUaKtSz3PkPn3oiA62wJFuci66E8b-RI2wYuluT0LA6OytxXN9eI6bjRhHUv9BDfkxwME-qHzaVmRjRG2l3uAzN55-atWXrNn7kRpy6G_V3aaVgz1NUjoPR8fxR2v7LCRbvuJvhrcSXqevjNPzl_vPJJCiqJQUVRy0EST49gA2_GlAAQrUgORQp5ErQVuv3pnzcvuHlDheM9HkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rod0ZpBRd4BzcstLxv9knja5KiDI4CvAc2XMEs-1VOwwt2NifRD7fk6Oy0VWIQEgbyA9QEElqgw1taE6r4vIY53dXLuUDYPTervY5y3sdRJt_2iLpBSbkUcKj-FeQ8W8iYXs4_wkPyh5SZS1OtJBbqpZ-1uXjTCMtGpt-gxmzAPTuT-QNahQ6OB6tekBmXB77krBD9BY9McbkFQxVfmEnceDi6gB1_XeHV_RcefvcEIqQQy7sjYAhjMvHuJ7ZOJzrosaXLIVOOMElTUBB6-qYfxLxr_81mg-p6GAanvS4CFHZTDlfn6eQlqo2md1uQJZzIrIEfRG4w2IbZYXzjgqPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">GoFly VPN
سامانتل و آپتل
✅
(اول با vpn برید سرورها بیان بالا )
https://play.google.com/store/apps/details?id=com.ambrose.overwall
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5944" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5943" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N94GRX0V78Tf_ydP_LVuMHGilrwlJ3d3A46Md_TjWViTu_pmMix-FhiDVADokMwjpnwuvEUs-qq1LGUHXuNhzeQQJYO6W9TeW61aSDJsbwbg3sgTk65ULNUb0UYCm9l8i1WVO36ve94Q0dCZBy0T4oYv32miO_b0lqaVBHjf3aN7LG9bHcVwv35EuM13EdEeX1s2_4yMLfY6RCh6AKgjSUgADHiaZWq1ylXaAXJhuyvVSGh_zqt62tiSkonCsy_CHgItUZAW0NJ_k3-SHDLA6NjuKT6hZ8i5LFFPpyckwHUoKw7TjJeaDkgD0c9DIfd5E9rZk73jPfVdi8SRUIg8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cybear vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.bear.vpn.super.fast.unlimited.connect
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5942" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTysdUKws1bcf0HZLfVIghIp4m0mgwLwtpknFmowCKcQGq2DbqGI130hDCQIhlfZP5vgunpzHdMq6ZvqDf-JeI_Ii7fY9dCpKEN5VqxusdScoFHc7TzJdIRS8UKBYYWLVsQFmkFQyOQsRZtcJ6enHTmcfbpdDp64pdLWHdogtgJtnQ9egxHyPzBV5_xYIEMyuUcuadBZ-sgYqDxPFzyQQd5OKVSjgT8-AtRW7eQqMmsh2eeiMoE1VlzfJLRewVd2yHRJqOuVpjhawoPpM1as5Ph3P44vgp04e9iqSMQSsK04gWzMmCwrno-KN6gXA8O_EPsdUhvyGNBncszFRkJR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Soren vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.provpn.soren
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5941" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpD92SIj6BzOjVVs9rdCtEdA37Tsf-_c5Dx51V4N_0KjwtoG_015pRPb2RegDJ02Vcwe0ePmCcrznQtFrQtm4-w8i6TEoRSbgw7Zf-c_sy0cyg2ahgFea9NWQABp9BpKchyis-gDpXt69OAGy3554uptunk74-VwCDQnohM3sxNv_Mj34fy7WPT1Y6aVlRmb0Bu0Rqx7r9p9CBJkcFK9Drltfqp-vbc4TE0zy6PUT3BG6Qq0xmuRT_xTSPBTIaknHTqbzsSAboic7qdE9AMFjDm2SR3bTziOOrmO9_1i8e2Dl9G_Bw4ffhgYQyJaUu16C6erZdS-loLg65K5aNSvBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5940" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://hjfisher.github.io/SNISPF-HJ-Configurator/
انتشار configurator مخصوص SNISPF-HJ
تمامی تنظیمات رو می تونید اعمال کنید بدون هیچ سختی و خروجی بگیرید و استفاده کنید توی برنامه
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5939" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5938" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5937" target="_blank">📅 08:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=MSCs_38i7WxrT0vkbeuoFY1V3h1m6PJPxeJsLGHbWzq7vZqOnXRRazE56LL2rRs3ycR1uFgRYkVvczOdxRWAlMfTWd-BNkemHoi5-k08eTZgbCy0SmGP_p4nuPR89DfrxBojigOU6meQdDmXsQ7My4995EcNXUpr9nJmqvILzVXsbJebUfj2sHuHP2BOeC1Ssv7BpmAPezalprCITJQrUKfy_gA3ubwC-ndtGHpiaCa3bjamUUTW-oKN7Qo_0kJGEbAOlU1asI1khf6C_g5tjVmGTPw5wMLcijEyiGtctGEugbqmCYFf_5DGm5-PNTGdKLcweXs86_fSjmyYBusr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=omZz6ZJdSnD_YYhfKBqmni0bezWgktGNNUsfaOYwKdAXdPbzqgR_hnD7IM_xQJ5iIg1mSU3vuHgZshsy7WAV8TyEREVWDnGCQiGt64Fby2AKoeMZ6iBGGGnrWxgkojpFjkXvv8WhgQq4OLkois-Z4u0M-w0ragQtpd7qye1ds_pb4wPWrgMeuuzj2YVTGSTI9DhUqZ7oEHvQOOrzYO9WYEs1i798eH18AAdtJrj5AJXABRx_IOM4ME72ztj2075P_DAeXhkLnU88owufJtN4A8dkgke3yKUpd2clbSJDJjtggA1uPqC-B_P6AeiY2ToDK2uRK7SEa7kCIbwOw3J-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=kP9OHvXGB4UXusmngWE3yVGszkptwqoIMJHttRJN-Xk7kWa_O5LGTxHsbOQXYINe83gS7--JqiSm8Fw2vosahxRMQtblWd9rIVPTAr8tk4c1848rskn-JGbRpmxcuUExxSchKLiM7EoBKFX8pL-4xELvk-sgLxKxiSPSqGRoKT_RyjNAnmZI_PJsTa-5zIQ7-dKZGA6Tp2IhjkLSewCtVMupZSnXx92kz74jUeSfMOWfKc5gzCyf0B2eKnkxuVoj6RwqlaRtHAfng4uPqZ8FabN-yC8GZcHHql_jf-bwJyBsWvostHXG12SS_CYYyaeoZgpAxWFZDYP6Bmtqqj7Www" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
