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
<img src="https://cdn1.telesco.pe/file/l9HdLNhiv71Wx1fNenbngBDLZsSm4mQKvG33kFih_n9_pG4-y0YBw7aqmcm28q6zA1CO_vYsxFZ213RFx6cPEKkwFi7cqXASEEFpK9rGyWnddVysKMyjVLwP8Raytfz0rRxKny9Apr0fg_O7OUpNhxe0AysyoAhxTywX6RA0LRKo0TeUcgD5xbqI-YXntuV9iMzgWNj7HvYVBoT7k2Pnsie72OV2BeEWjohKUKoEh6hO_vv4gx-aABglTRKJfzlAXa2sp1dGCEZmPm6QOb7IV-1PawrgfZERJSn-S-qG3yd8Fss-9TMPj_XF7w-vkase0xQTp229ZA3nKh8bDToe3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARcaQdrX2qvQdH62S7Z9TdGhJ2arByKwAuT_6eDhAD0Z51c_YGNmMxIN3yANbJz3BXjc5OWOzbyk7VUv8Wctj8YAplaRgaAAHZAtK-jIJ1LmDKYQtgfwCkvhBwlC34xZ645IX7H5Syi2lMGKqoX2YjwPD7EyUQhsE7OWIh68dZ1Q3i5rr57plL9aHRUH3glEtS4rh50GUJcUPUD-qmp85dtdgHS8u6B5ppCaj--JDVRzyxRXRK-H9dqob4Ih2I-QSk3bxjN0Yd5lnynggiG0bm06t7Ebrrcky4N4hYMLG2MBGOcRbw2VxL4GpoJe6cLSpG9XfabVoE3lqJwz4nkMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXww_-tg9oU3PzVXZd4uXcpjaeSKofXZdO3xUPp0GxkwPzaEvKCbM0y_rxH9-A5BTb7PhdX5FHZHZvZbsOWHhDV_tYnbtfCOHZTpWooJeLZqZICQPZGqB3R1KicRZoOYx-94S3GIz5FTNvfWY7YQh6Q9Wxl_uu2CmaF-pI-Gd6MAlu71jGsIbCUTvk7jQ9lk5ZOQAM1jGL-uheYdGjZ8lpCAPqPlq4awtngnFt-YhzGmE7vfY1-s5CIW9qkHlONDnDubU8McWzDEBrzn-rt3NxyQj1QK3zQhgHwGLmMCA4sqtMql8H3eyc0DVBvvpERrtsoESbfGhBUYyYvpKBqgsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAe0ZP6DpPHisCzRLKXchinj-nsa9usg_FlHIsodBBJ4bvUj4ZevN8e7CKu8V5f_9C-jMyZmUQjYPbiqRBJA9XPjP4vkrRe2i624NYERFB0CbANNuCvzuQcyplw6R4XvYNbfPJx69OqR-ooxJLTgSeqKEoNFwZe6OKW6u90qF969mXMRJHouTbDFFrSTgd7lDaHKeMyl_oCA5yjm5qRG2g_EoiIb-93DuaxjsQGvTuysNW_aHqbu0fC-qHWv7TTbfNwX274CpDj_CCYxaefkLbapHtvzCk-9b7H6uNQvgD4tToU8l2m-356F40Rkz1ulz9M9sfu-_VTViynH7UoKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeMgrHQU5VcR7fHmvvHfYD5aaxCkO4mfXIeC4N7RArrDsW-GDDp525YugxCXTyZphoRZy63H8pNXLo2UlDzYh0GacXARHzUuIFz49VGXQQhbjism14nhx4oD0MLzEUY97g4usWrv5vN0Uyb63WOpam5rt3GjbZNsspIiqMZUF3JPAvfL_CVvzj1OcNPI_JwnGPkxcLwLLLKLIHX2Wv1XcLsvud2Ybf2qXiDCDsUsla9sWctQuIuDx6WlASdELoD8EQnPAa1ZM5pJEY-9lwK3uIwvthtPe5pW5VU7mNO1XUvvna12A01qeOMQsn7zbotwVTBJqD2mhWdcEhtWsb7XDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cr3lYq3DBPfZGBnWN0PoiAsW5TguhF0X5sUz9vsZqzBK-sDVzYJy82S4KlmxYSRgzuQtxGHhE1Kw5TroobQuB8iB8_tI4sWm8nrSJVlSF2nOb0FL7MCzAZGQd0fgmaFn4dWkUoOeq1oQWqhA2XlJ7668wX2MhhIDMjlJnnPS6kse6VkxZw-892sQTCWr0jhY4-beth6xn79AS_VtCi5yxPiJ06LE-hmCrxuwXrXzViokIgX7lT2MKqDcnK5DnAvCcDVmKxN8HPMUY4_RI6vlg8D5UR2sCnrf4A1z6bOtrBZnD8W8BgD0GdR4jU3I8s_cw6yKVbldj11GJcN-dO2ygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJ52q_gmkTQMvJZTdr6mLUldWMVEMHeVsFtVM7Vnzfdf8mCOJNgzaFp84lvUEjFFoElyKIqUyVpp6HXBhhfTWELX-_7aY_rMqhzNP_wFaLqwoG6Lan8ANP_AVfGeYRWtryNfetkihvDYMAzl-BLovk31-MH6HU5sZdTuig80icqEShCuRHrLjGIypGbZNY6eaVQtE__MxxoNMpjAjqnb-ZrFHO4dq_ZHaYfNwhwpRw3sQ0ngdO6CPYBNewbJKKlYsyVu-gyxfhs1TksIKuGTYCxPXyO3lVdY0DEhoj5M5Nq9qhB2IhiEvR-efMZxYnAVu7gG1phcXAxQP1oETLSLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ea-STuS-B6PEf7rEgIGAt3igEa8Cqx1PicEm2FbawzrpLvOrxfiNbB4e6Ws21ud1O1uH3K4EwEWdrSG4U2zN4sR2oQL_HTqB1tC6wKoh07_0Q1X4w5xzRs9vTF6vn4VGJwsqnjrF-9sJ6cSLeJd1a0g510rFK5F5TuT2T2HdaFTpaGJixJMpJ9iCu8-v_AFFLw_J7crXEKMjoeg-HYdSb8VfZ0ttMRmxUD_Ck_aZjLcZlbeBsFw1tUS3XS8dS6sR5WUUUGNvws-mdCUbH3IcB8be8BdA49ZT2ox9VJSTvzMgaIJKw6AOXLfq5y5OkGchmvmgl623ptsMa2lJdfUBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j-1vyH2ltZJlXgbJCN_Gw3dNhQKXfqCqalcyW2wMODkLu8IkGI93F_UA2lesKwNrg00IY5ENSVHkRIVf15SnRMoRfVYzGcKDpWPPsSAeqvdD2RgFtLWFW7hCuWGR2RI885iC7g3Q37hSDmUVFchFVRAr0gspIjF1peqO9Ag1MQX25ZrOSEzebKOomwNv1xs1vQrqpURCSTJ_tmWygvgH1hoYfag9nm17W0U7J0gkY0uRp_66JuiBZ7-7YeFd1OJ8JDVwU0EenJn2kdKZk7HqIChsYyH9pAbyCefckf6BOhuoMSU-8ZSCJikQZNpNOF-hQaZfl4bq30Y01c4m58NoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kbS_nJMp9_WafQ_az2F0wgdIPTnog9iDr1IrmNNOYNFa47v0DfcU61BiA1v8AY-ou5ioP_0SoRRzA9x8H4VyGWdLnwajurQjhRZzdmLjkBvKPLIifuwbOnPKOT-C-sMiZkZTGPrXGyaZvSkZ8qYsTLXe3YGdqaS5OcnR8VnahRV-Q-pZWKxJSIRgibeGmuStYTT9Rr9dcdh4-yCC5eegFORXg2_TBI2JOxBvGvfVFFICUwlI25KuO4_IS0nhqp02x-aoKzPZJtRn7O00tZ-Nb64eZ4uRWbPg8xVW6zeP4oeV_9a22wfPVyhpmmHY_NDWCB-El9RKKwElweZ0yvRnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g9rJn6JbH58V2oGs99bUf3QBWO9HKpj1DpuqtO9KBNyZJXwrrNsCJh8SfBhzfeX5OpuNFywTHkwAXRtX5iZTE9cGPWkv17m6ypAxPWEKLg1zYOCC9EAR6L4L_UlVJX5M_27x6SrsqIxfl-tQ4KyVa-QHl_nHPknTznp7OyqWS-unia1gzeSTu4tBgsuo9ZDWTjQbCsqC6LzZGIph_aGgqVccOuPZ_dAJwb8nyd4zc_hxtQRSQAgbxDwt5T3z4FpZstzcaQvGfsXyhn69sfTNiTaaYh6MzjTo40A7YMuZAyh7lNlhJqDKnQte-DRn5dW-zNGS4dlTjGR9sA0dPyl4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/McukJHLsyYLTIvQe4kqvhKMVlAjqR5KXsYRnOQr2tEnSy2I-RS3fuwTaG4cyeYARH0sLA3RHsmFsyPEB9d53MeB2vIv1Ja_UudxV6POAozIuBlRWn6JoALL_6MJZs61QHHDarc41NReu0VA-JgzdnQGJBkF28HLEkArtZXhyb_scQCSqN7iqTzyKcw6uIj_iuqHB8YNb0-POy2ede1r4h9Sr70cGRhupv-e78IcNkzej-pnzyXF5GW_lFjTyUXp_kyMM5yonOhPAioBG3lHorLxb5ddDsFZfc5yKOM_fpJ27fWa-vkxW_koAczb7BzrkU-gBSmhDbGjzCoG2SAN2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBaKOtgNe1lvSBbAftHVrSwEWYmNxf4KFqwlMJ6zy_4kZvugMtAAy4Lzo6A0N0lVlNTQmoL6j1PRjaV7tc6xaMHwaLcdcPpUxMiZieFBzYTfcWmQS6tojesJe6N64E3AvS1uOVQzs9bG4GTIlVTulaWON9FjoGTE_bZylu8RHcsNQojvVLbeVdnZeqyOBKdwdFmU_oOxzeQ68j9d7_vVyZfIIn2JjZOD0I_sRUETGjGLPDMEFG4TGgXGaSGy-S68g1FKiXQyM-MGb0-QOLNFF-jSrNWz0ostCi7DxmnDE-hQZB4KqKcK2XzGVv4Z1UfUdn7ji8fifyxVnljXfvOugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkUK6wxr-2wvTtSBvcfn1pPS7AjJTH-nd9wtjqdc-7QkUwv_S81k5DQvm6shIvyvOZgnbdycMi6pof4UWpYXiWiH5TkvmbAv5vq0k3c3HIqBPPsjnSi4qzZB_Bwz1-LJJQqgT584bWTIYszxdZ9T-Br7DHdieN8lwsEqDaROsIlKaX15ZcWYioiNEpUgMebqvj4bK2ELpc1LH_VAj311-Wqa7Mo8F0WEMkhhyuwTtiUomhan2C7oA-MJr69r7J7bPyX_g1x6D0eOUFAmQLL9YQPcIH-jU9N5SsMO12KoT5Ww-zU2QhHpedGEYqlcVtrfoqSo9SvuD0R1T_k9HwDJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_LLW2HMtVd_TKq3tBTJw8_OIDf7X3JX45wfNMbpGThDHTQ41I4UTI2ZaAHszlxMbU22w3n7DqJTh_1VT0KSdim9wOqrIvZ582NRD2hPMSOCdOjN8tipabgAGtW2P_XGe3TflLhuOZbHl5X5QyHoAaQuvbPuCukr9szhS89QWL8NhrxIM8kCFHPI_U9zDllLYRTo_EoqJi2xklx582eZ1C0CdFKXiyg__kwZKzVxUtoKWDbdRl792POWjtRXQ_QBlLg51hxwOc7DdI3PPrf84iW-cDsj2NGmmJBeHhNZfKHx1LM38qFx2CCO54F4N92Ws1WAjUYRoM6whnlYTErs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSvqRHYqy4JS7L4uY9Mn3ADct0R-InxLDs7TzkEavBl1Fg2Wn8sYOYg2ikpGZw6H-_BSzkJxxeGS1vjPf2XcJA096o3V0bOfMRJ2yfgsQNOxRFPswBTIkLJKBFmL1lRLINRWtsWsobCKwNskQCm0-C8bJAyv1sijSiE8W1W5RcrFfLeQrTRpEzYVroobxwB2UvK9iCBmwnuS6aKdlS-Vr_rhYrS35YUjWziUAqXUBUXo1AfU4OUTLuH5cBRrsPPfoMpbax6vxvTaZ65SLqm03z4DaUlIlOtTarvcgeszlVl5k1FBed2O4p0fOEW5RBU8zH6JuNXn9By0M4YnXYq5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e28PBsBVuaAzMuPuJxcHn2LDz25eZc4o6yKMgRRF5wzO2zRkpbRXiyFkPceZj__uM_m7GbdBHmRXRLe1wmz5Xr_nHiaOfHfHnUMBekIcJE5VbTtKRryaubjxWF5FZB51hICvBBFfwxdMUVS17sGB2LxSzLoNLebuE0ME2nlJslR4v7t-qzukZ8RKw1_Szge46BoP_zmSUabJqlpixjKhW3zQ3xPcZKi08la3BxVRkjDVrTwMX1Cs6w1qQ35dsNWjqfqQYlgdpbKgx9n1pIbRxUEtkvgon7_zqXJ47OpDeO7CkBpFg5VzcLltpDduxpdg0YXbQ-sa__-TG0ddfZuEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmkTnWqUJt3jbRngHPs4cvULrbBnnuaZup7Q6faIH4_gxvZ__6nDrh5qf2iq36UUyJydJUjvxZ-E52FVA7B85SNeyLceRJHJ2SRV_p5AioFQMGGDdqlzy_OuIga6pV56nqYEDhSSCaytD-PYts7G3keKA5_kA0CzvGumZewmWCOYSGzuKynZmT84VCBzn6J2wk5Hi0x5S5jjh8i6BPI7kwJDRtIyssLzVS6RS2WJUpNhk2zZng4LQIDl4ooyVc486O7JltmHhggOiazK9d4uaTMY1zk-rLtBA_trzqlgckg_mUHyzo0d4JJymWBFvb_dA6xJit3z_tXsr903fJTaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vu_ictvMbhChoXgbjStwVp4mDUbu-swXHUO8Sgn5JDKO1NqQvx7ySjBvyW-7KEAKoxGgtKhiHo_54X4u3xsO6lLdqADHDRMnF2McFQoFrt7ehWQVrHkjw84rjkQWLtAsXCVKaiiEvNO-HjEiYTyc7u2Owk48UL9bop3fjZl2CzDZqr0r7YK-NVdh5CwCtw11uBIQa5BHu_i7KkOMFXrVqAKAeROl5stwfjgO02hhN72mgz34mgcM61GWFSP5wLXZV5c0zz9oNkjC1o1My2GyeOvXS0t59inHv4KRORy-JwAueyMJTlnbeOzx0P5hNFsk4UE-myZlrupnA1dDrJALPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tksJqFpngWV4cHUbDqerQjecbXFp4Vs6bYoZZCtMyQ6r8_H6hpbGvZPUsLuH4prN0A9IjQpc6hhVi9g3ECDIk4l2jZyM7Wee96SQjNl8v_x9KegS4D2s7SPYW1pr3z4uXbmzlo5x3Ou-pBFdgag6U6AWbmusyboAMsPpOdFybAhPZOk64jBv814czTNT485fPiQ7ASsvWH-kU1ql6ojRrkIiaT8oEx7q_-FaxLDod4GIrFRozyGRHTPBUbrQlxe_Glx3nEG3l_7kVVRMke1yFaQuuLhnlaZ3hmuk1m_lxbkLboapby0BmZVB7a04LGqYeu7TBu8PWFtUmf97zPgmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCkTTBUK-JkLleSav6EzuVVYu9Wh-CuI7wgOMoHinTmen4Q1Or-TSdFI03wHf2H-HZo2ceCDvqv3ediA4iUhYO9Yg3NqNPNxb5YX9erkyZ1joJAwXfFvOEKHC1wFCjm-2DNsijmjZDg_LIqDoK5gMPRWHNAKkWCqd7NdfNyIcV5hymjDl9mNZDVfe_ozhogAGQEsLn033yV4LPSjGQ6XT_Hk8NjVCIa_VR2o4Qyj2bN6CM0JrwTIjQz_rW95ZsKdZUp2HQBAOCd_vD6_9AAocPy3Lg-kf4KIYjZ_87Hka6KhskTuY3eK_sA04DTGMJLNOAZ9wJvbbg8YFGewdvCasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lb4s1oWGJyE8lEoDr1dt8WyjT430D0FkQqzZJqYknzvvfr-GZTFgIF0utUbn8NNMz5CrD__6nfPjq-yP4tEj2436OYgaBTePS25jHlFr7JCj01YpqxhXL9K8D3AE9I2WnwfTeZDXtBiXQ4Jv04wmoKQ6OsKdi7R2ILTduqzt8cJ3D2lsyhhf6Gro849RVP2rQFBJv5cNS7ds8s85Wh6dx8r8bq7DBM171QBUxrK5Crrb4VzD7elgCrDtut8BytbyjREQc0Um8v3_BmT-WzUfEIHMhOx3XvJdmf1-4Z1ykYz1ITu84ogmQXbXmi7YpVfTzQ0YGwezVZm-WiHLbg1X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hCrtoCMMKUiylWhAq-bgXnTgNFTxLZkY5eAZhpBaAGbNlouHYWOAgFNwp-tM_78EkGObHqJgZNyF6OVhYQWfs8cm6FBGEwowH_1tXpqZf7s46ILE8d_cF1LB3df9uj1wZ61ja34sdDuVSfix8-APxXmed8jKzj3RfnavubhPO6KkX-J9uuSma6WF1qEySBSM0Z2xFxk6KZDz03_afl8qwMURUXtH29nf26mjOX64ShkPi10mlml0N1lB5dhIvgSgez-RwuHsJsV3-Q-UyblvQDAGQgjVCkwBudb2ETMCiMZofBtRPqjrmGuNvuwKcXjdN6seBy6mSQsaZmnfivio-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GL5ZERQAuGpTInaSeXKVsRNfXSL78-IFx1hHRlRviVoG21ck068mkvD9KdUihFtURiLmsdB3KNVmBu3kYASPZhEL-w8u-JuDzmhjUUL23btMcfWe-AZbF1U0AUJOa4hCQG9gNiAPc9T-LPsBE1g_fa4Wh_5s3pYWWroUfZPVegqC9zq-jSvNVpnbta-uMfXKC-IVpIoEfqwlhhgk9dnV7EH8zYSpdcjnGdWA_VVBeZNWDpRfy8-Ml81wRDk-YowFd_7gjV5nedv3uek-X3o22ElYSGkFq5LYjSNUbOAzyRGYIie1bQdSAN9HR-EI7W89hoaNRblpmaUzu99IohK__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EF6CSjE4vGd9Euo0Z-_9wRM8OELWYhZLgg1M51omCnzukhc5B6u-Ru7Rz_PJiLuNZHkv5WcKWcjv2Ac5pDTRQsLdwqbRWw3STkvnOzlFvswBEwOdar24bEr1IuWDY6Jx8TwG8tnynY9hy9QHCnG0Ny3r5P7hcPnMUHzZSjvTKqruJoR-vcyK1cEI3zbJjRclD6D-NAj8oIb_Fuod_X8c1Srt5X4b6D4Z-OhpnU4dcirlsoHqh_tSqoqkeWCPMdh28idW61pt3qsV5VB8WQyFtS8mJ1A1kh_KduqaBbwPLmaUkrrP8f8MPrkdnwSljXzdGVQwMFv_3bi5LNv0X4M4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Um6LExZx7OVMFr1hct3jWCz4vbGlAzQZYCgJ4cuuG2m_gYemNJ0qO_DevRfBwul5STMgVExzq1F9jl4gW3Km5neWvKVOoEKgbqKLtpzx7GywppOv6yoAA-XPqvBsR2TSwi3SSnilUpWDrCkbvDMHBTYAKnyj1Jhv0QBMXHXmU0xRdGXyPDwk9KRwzGGOy3YiSpaysrEHL6fG8cjm01blMS2IiX4y9fLCrCt8TSF2Wn0I3INpqar_O5nr6fqJUE5QW23ZoyG7T15rlwfDaANfJONdRN1AISaehOpCLoplDm49sUklT86b9U9EDM9MS3nGoZcoPUytNBPCEjSYFuc4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RprfUctRIOvUmLkvG4AhIJqJhJFKqHdCEe_EOcXPXnvwDsP-AxBZXyYYa9SJPTifdSrw7T5VKBElOO4ZNHnWcwzfI6VRWHOiqbiyCunbDncJnd0E8b77YE9pOug6__c0wgfOUrLVACkkxUbkNev263UyrtK-5fNRQ38lX-m4_wQ3m_x17tAn8-FEnCxv3CR_BNSr4DrDPHmZnIFueeg4q3LDDoB3CoqJDuGR1YpdYXBvDeKj0QKqoW7B1LUy9I9F7AHyvZhysSHRgkFEHAVFF6B--fGqWnsMGFCbVlaXYEMccmLQXTEOGXY8jxbefLdKKDHsGmM4U6Ot--jukcBs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XsgFih1XS6g9I2k5owhiwjnGAfLZN5pRuT8yfP-1y7WTXMzbd6DGpsG3ETT4oQfrS8_KYelE4be8b6_3Ei2n4_AGf3bkEeXPEIXrrLZOSCPcNlOmfRQj9LHh-KpflRiRmWlXiYo28WeQC08bavGRodGh0IKvGSQF_rDoFM3tyv4D8uqa5okT0FuNQ0YuC_LkNCPhO1_pOBhhJlDmdGI7mCgrugd7dTFeO566ZNA2-a2JZCUyiA_-uLrgPd1RN0TC5CQ4H-YcIb-4XKQL9yLKtjSsf77GpPmKLgQqGpdq7KTqKGSG2_ldXmzZpCHoHHJYLkIUUj72qbXwZ9QsblWomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OvqH69FYfH3mO8yjlXXxNqoZtGl2Puim5lTd4PcKsUjx7CYkU6cpwImQbvxfMI4YHuMbDOAhnSoPL7y9tkuvJqm-KUJ5vEq29lHptue8COVC6Q6qLH-7k40fu0HFm5Yd9YR79DrPzyXR-jdrWSM_wODqOJZmQDZaA9EmVy1j1LRVkN_79rxKFxqmOh4WsD7EpC1DR3koJdsDUwlddnxyFZZEl5gn0AvWjtro9rhOWhw8frk5uuU-XhYYBGVRl78dyKkvZJ6p_CDkuY4kxDPLWOcGkXrx8dr-b1MGGzb_qjPa1xh3BfbRLsGcYXPBLUcqRLZZSblDCOi_H8s5xO5zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XUxFxF5-H49jm6DrdUJW4lm1yAu7ED4wGAPw6AoVVGhVf-lP3d3jEQZpyO6tGBF6J2xEsA0FvGIHO5xGEuwgE66XmLB_AgUigwnB1bD6bv7YsRqKclYWXgqIAvFgUWNEulKubQlYmOSCFZyWzlMROlXvEiXx6T7KC-HsftpkkhVzWeXpDRWkRhh_LHxSDLeabZ5_jnpPho1fVRLqdhnyttfp7TZQ2DLt4c-Rkl8-2r39xeDYeULH4ISthJLGwawGqjZChBons5Zm0DzIsjpc103F3SzO6UaaRAC8I4PhMp98kRiLlbvmOMSKYKkHDMMAq8kDh-zDG2N6stac2cg7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ajod_KPfX3KPh7yjv0z4fmUcMkESZyAoMratOAbImBDE9Y6sv8a0PIkakgnnStDpXO3s8sdKKRnvcyFj5gELAH-6kGxsR41wFU6ATsJl1YgdT-_TfQKGGNWEIVXBzmxRCdms7qvgxkyRj0sDdotXcIIv4ylL13wC6tS8a483eOjUlk6S8ibCWX_ObOa8c0tsFC3e5te_IIcQ7G2aMsSU0CdJYkrEeLQU7YHbj8RhD9xCY-GWYSP1IhfAK9s9HpbX-lIq5_mh1eTH2yMYTcUWLcAkpdgq5NeuLhrsJ603yaU2mNbKKzYK8IzGrqlRk96BRuQr5GslHjGd7pqGV3lBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tmNUQbqLb75B3U68BI_AgyCz4Ix7fX-CigmhNJ2lNNA3d82kkpaxOLXPQ855aTk2w8sGvX2WYsbCcaQb6pSMmekrhVWRnSmRdNM-i-bc52jTs0M8nt1zP0wuOhp1AQ4pUIovZsT5E3r0ixWjwyEbMwZ4_yYzABkk9OMYhdN3nrq3spBbPsp9rnm_YZRRsLjNfLL4XiDipDS4Op-ZtkEl0zhcS8faky7QerfixsfcMeO1JNhsKD-KFzrNmiZYRV-QTKCY5GhWu1JrVqeCwiAYgllA24iu8yGxrKK6dDEJj5-2f1jWbIkNeoqRhjFF16uv-YjWkITjuiFsbfXdtpHkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRHtic70vpHlf2Gg4-SBEEhMDiHdRPR6q7wj7hbYAyTsJ5KCcA5EfJEGIzZbUfCIZUcnxyuxoodvCLlX2pD2OEO5vvFLet30KCaf_Xk2QybMa4PcAa5AeO0jKf0_0O8XByQiYocOrh4jpPpi2R3k7B45Mzm0iUQxnRnm0fNayZXJzQQRBRDIi4Y5Dh699kMg3j8SIWQ8kec5zUJiBSXUWMIF_-96Lw0QhnRCLgsk0hKyQB_rslO__oZ2ARIFTGZUhfi-BYo0kOTlizTy-WS1TxaujpHFZj1FONfXG3aXPxmAat2gOPE-AvbfwwUUHUTTGt0okWV8yfGmhpLCiuMlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZbJ9mJtavG442dmpMieCK31iLxJypr0oNgnPU8UWG0RSXpcqFIVwfDBmgiuZsk_L_qi7LsjdsajxN2ykDYkOdOIMMwrchB955eWDDt7DqumU-Vsv542bbNo8QkQUQG8GdqTNa25KoJJnogJiYf_sd6O1ieqmxeUwPCbwKow-1szzpCPzFniO3VGk3Lcy5VKJT-zt624b91-Q8ssaMiJHcFSZy4KgWhbUYIpBUEjIW2f9vtax0xnA2rYAgULjmh2IDLTiRhno6zbh5ky0hoAjdIp-CyRqHLvoW64lOSfx0la5Ro6iDSekQYbcjGHISQ1AfM-jo0HKLnCT3izNJz7ioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nBYq4NKzrTDArmnp5JTyyrWuzRbtkHSoCk8tF5n6CkX7R69NTkNv8_4jJ4W-cpmFLLYAWag-2LQdqSuuWuBaPWcgiMEpwdf0kVksieMKAA_FhO3a357RbowHdbu5LwQYu9cp5VcqlFMH-ig2qdt306ZL-gCxmkFv3wIv_ggrYGnep9dREwwpHkJ-q28tfJ-tc1ez7evbyWEF9X8oV5H4X2f8v_e6K-gCngqFbihNML6pMgKOCWXXV3qPsMVW0UDOraw3BnMHT8ksx-9V2Ot2VK-qvOn1K8mHWOZjZssqbBifofl-ieAClBJXSnW-Wtzy9QIzNevYvJesjGnogkalCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j850Vo3QjOn1BsnlIo-eJ0zvB4Jbs8a3IYFM7h9D5uY9fpPyMz8jaTPK_eRYY9oxS06lKwSIFd6Q_Dvnok5sPEKKieV60UKt1nbAbsAhlv6WCAMx8iEHFAyq6y3muivZi8jPG48f0NuWrI9NN2rbfvhs9iQ647uT3mu7WMIaQgbV_DPwIvKG7YpIu_ji3m1ymFdmorHCEmhF0Av3S__aJDbnImimovKJR6GHiaGmv3rrvVTFOXcBHx9rDI-xBZ2V70fngygtqjvjHYLqqogCYJlUqW5JLfs-35yEbd_-VnnfaQfpY7rz18iI3U6Ic_7u6JkuSFA5oSM36KQJDqmsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4FltZIU5zq2pxZbJ7RdAGrFmaJAl3ztfnzDCSpeQDtrbkRhKxRvzgVO654jtT91wLgoQ06OWmWwymic-GtSf1hisazMuG6GapWWO-YfOBZME2p5QaqbqPHc4benPm_xDWB3XDZfKccPCtTHu5nIsr0VMVlRRubVcWgGkHK709dlC5lAi9DhoEzppqrWfidPwYR9ka6Ix77Cqwr6CTCI1mF2Xk9-OEcQezT4lSXsFwA4T4eRW6STswiPgeX3n2L-8LoXT34_XcBvXmXGuNdkdFeY_WLpg0WbSjjOZtCagLyEIxZr7AsxxfcZP-2ncaF6Mrwug96SW3Ki9IjMzgpQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Suxh1IGN4AqjaO7O6OFr1u42ED03qAuDJD4K7Y7VEwomiElTVIVQnWyaQINGKArRHiJQsBJ5yHNfrdpbZ_hfF6G6ALF7V2zkH66nM0kiurPSm6r5FtttuScqDZX2CipLYscWaF7uqYBDUktyW3aGQEBY_1oeF7tqUXo3j8a8dHSu05Z-a5RQvCEe8nr5MX4gKjM_EnG8FNtraFGvBUS9VM6X2LVpNCoR6Ify4OK8fS2Cwxoggvp7DuRGJ947ngeFL7W7w_DfBzJUOeptAVLefX38SOnDJU_OSVMg47bbZQEeuOhL40WgLuaSpnhYpHhOB0FS1raFRWHvsx8aDsKmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsh9mJpV2wWsnJ-VHF2BhkbP3MwWpsLOJWgC_MTcm_ZZHxPANt6a1oGVNKrKrQIdXtQxuHuc6qDVSvcAe4CJcVR7CaIq2Ez2jarhtNVCqrwTIgYLxpag5RjkEuuYNu0CQquRwbnnX1x0UM4PeeHUAPf9SPyDJgWVdSVZ5xOdsVlm5Om1PfBnaYTC6F4kFjpQi0Mc46AvnoyQIZSuf-WLQjLIJO2gN5LdZJHWK0TVDrV4WhbmEoybFZutHOFhCn_f_46H7W--i2x8xnosoBEfuSayrALxNkWdiGe994N1CzqsmmWib-AVaGZ4P5o_w8Sor2c1iob9qmGjfhYpZixsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvB0k6aK0tDOBmR4kETBeqKkr3wkEfAsUdIOMVcs_PogFEYV1jtGPB6wOEUaQbY0FYIzvfwa6EPR_FWhcdastphyLYT-kNQiD6g634eifYws1AkUQOPGQdgIJIcXedCt61xbC0TGSYkscQtLxz-Uh9DZWscWlKyaUh70gnwHjQ1hrC0krpLwhgA_ANLwn1uyfg9rouubaUDi5-VZ8WjbXaf3WU6zAeUPnIuA7q_psGgOEVhq52zBqcPLV1hMGz6HJUwUAdzBhtXmoE52mKJuWnY4CVlvuyH_GesGioS0SQwoVq7izaqYx5VdSxDS-yNXS8MqH7t71RneMp5jGU6pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skd5AYXkSNSS6HM4d0cxwmFXUOLm4_NudIjRIztkkQuUxM3qh672Grd_F7cBpegV1kmYuuLSJ29NaaSX5ALYxZb7a5s4_9sEt5SfVo4BOc-OTBbtVltWsP5xzN8z9lc97KIPtf4uWzMmq0M-JrrJGlnQoaURE-WXVgmxsDW32WGo5CZ-mLTHtkVNS95PeQO7aHxHZQfx6OulWqspzIxcr9KRvZqLkWAHtgiMvntmBF_o-QMakS0hdyiOGyrQeGvKB7c_n4Ik2lHjqw6UFBzwV5cwFYECaGHuj5xH-UXk6cQC-ZsLht-SGWyPlZeSXfl-4DhJT6w2TLxHKp_NL-lFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TAIOXrVy3hPACqKsP053TOE8RiLUNLaBQUcM86shdU95D-DxaaoRLA2-XatHbymqC_y5zfYvw8ohIbTJ4C7Bsue1SJCQ1eJeeZMnOu_OentCrIKQsIVD6Yirj6me2S4-1wfFas9ZJwQ6JAE0rcqaex4IfgZaBXN0kEbDzGLpC8Q-dBQkprarWw8bDw55SosvV2A7C6VREhZL5RBqkKBynTV7mcBYqXN1Q9-Yh74J_eZOiBza7n_jp-cOewP-H4T7dWFob6-KiSp4dhZvAoyVRjKnzEjQg7iHvmSW2XiYlboYP4j1tpZdcYRwHPs5ihehFYBT9F48EqIoUJhEAJNVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl0fNUrSj6KEyWoAR8-HAv4ukawHADrl_IIsDVb_psUh4lT-UlGnf5SScGOoTCOED4l2E50p9oTxj1OlzRbjsI8Vb9PjCjimqjCdCPhiQ8De42V2etzfCZ1KMMNVPnTAS7RbCvDpS1jyu48FjShAsQPhzSXUkKa2OrmgfOJHVVQUNn0guORdwEtzQ65QlwhTiD1WEApoKzZRpqjW25nvfiIhiIyHEWJ4hv6woM9Zvg05676r1gJzjc6z1X5xRhp8W38cYUHdfAW65gw24QYNtrd7kDusuRS0GDI-pjEkpGXl1JbxfYJwq1LL4K5Mjqhwk_dBnDb23gxRbWx08dn8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQ-REAOPFHct9eWFqYWDnqX5Ggx7wM5vQLDZ2eZTVht_TKcEJps6n4ShRt7o2SHfLvvrgykPPgvADfkqRNQPYZHiQtV1BQANsJvJNtK5yWbI7eeRkd-X79Tqe-qiWJk9bWrBFmNrBgEh4EGVGFQbklVKijy8tRWBpKSf70P1msjRPwUoGvFScGFcsBBqHuD7Ql3rOKXE8ibyUMeQ_1ngQ-HQhw52PdSum0espOHD-_O_RYRIrzhT_Dmoh_UDtv5OB9Cr51mWvYiinuLt7XmrRqCm6b_oqC1c1-mnofvYJWNGBZDxTw5isL9HcYDniz6oU5rRQ9_VW81hlde6ujk-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BVgOIp5po70qNvBhrkvJsWzIb1rmR5LnELMt-ooQNEHAhVMuJ3zP49OThtzJYlnkE0iR1GjXrVoJV-y6hRmwSw3qftM6s0Rcdm_fu3UxEHOGaGavHn6ehB36jYacaZZgLC9WIoLujuky6i8TicdWmaE6OCZ3_HxY9nQcLIjMKiEMHVb18I4pOW25Pug9cE-0ldi8Idus8QijR3-YJOzBw82R4hn0_z6nRnNOFHCeqZWOekXFCcbT5XqDkEXmXdSPbkkvlrfSs0fE2pmypv5wW5YgLAQXnYkMKuciCeg3fJzNK506C8FlxCViqDWRriCeb__g5T1Y3iWOzPY2ORsOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGOCar8D9Lf5PVTb3O5_kNJO7rFCnODLNKDsv2ubXPAoC9EVqa8GMT6Y1-tT2G-ERa7T0WK3leoEMCq5U397Vfu0lUU0SktRQDE7T7W0b1xz6DmhtD_BwtIkksY9nh6LBNsCOvie2wfCEzZjFDTPLtcNgO7QUWtcVHHhoFb_ZYv5CUBhHmyiuMdFIuSgVux1Uzl_OsIH4JlNB0AoPa5w18aSFpNLI0YHkJXQ2suJHLkMH6y1Plj_bYF4PZ8k_B7UhLIfg3pbL1TcxjrPwS9TBwro0PcihVA54MyLwap8ye60fCqE6DIjtqcQVAi8ospK-Ma9WpulwFYYyriQ3JYlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TdJ7Ez8P6gezOS6h1xcHDQh7D41As1D2bfuspDpwMqK6r5DfieJZ_WzgRnPliJNtAbnYXup1kNaMTXC5sIk5W0Knc1iGrLw3uYaKZNSHrMUSxZ12Anvw6ugrnrMiStN-xwc16GdYqzacAP-uqIG7tnXzA3QWES4BVZ8GmIIfwyKaIeuyA7-mbeihjxPReOF-Wh_xNp2R8hvObX1OBSBnQdPp_SVWm5Va2taKdfJg94t0zVWXX7cSvD39lXlFxCn_u-5cJTxSo_jQQKsBQjck1QP8r3mRgaxnl5_pemmT_uryVIKXayRgmeo6ndg_omX648uzHyiWeX10UbIwaUrJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tIPk2b3tH5Rcf2e3bIegi6kBSVX5HijHAhZByOoDIfuA7vDqZsY72NJctaX2T62zpSi_Q1vTXxCBu0NQbyfxhBALIIkjQ_FuE4xXUZJEdpYwANZWa5f5YgaFAOWrkxZIcoJTwT0K3y_bZt8dpENaXB-RSOxsO8rf1ZnBplNIzX4k8qn-yConzfHx7eWvVNk-31SdhLeb89PmzbQFzFj9zSLOhR3iNzFeeZY-cHTask_KvGZ8gEysTDVI3u1T9I-tDQy9Gx31CUDlgh_QDiF6WS5oMDQGEKd42REGyOYwiYAmnOIxX7lDJZjQxfJxsXEwoXy9Bafuw-i_FPcbCUK7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-sjJPDlKnjMhsQvi9II8s_4PvwUa6UFuttVmAoxutxH8Vxttw_WRP9rChFaP5CJ0W_XE7pjf3sz3lTuC7tkDNUEOdyoMkrNEtN6B9fY55604ZR_kPyXsw8DVhOs9zGLeQWE6KqPizyfElzskXpIaY_O3zd-eeIQmny9zmUl3z0RAvNmJQ5SW7w7BVL_-S3mU1oU1m8rpIju0WwcwTiLAaAstQ0NsjiBplMpWyHMCeMQEgmcf6BW5rPh6wCvVzWglgYdLCmUgmqUHCD5CwSgOe9seglHvu76913UyNpy7FBjqyc5LWgj1r-nAAcHXZERNM0ooEurs9cE-3E3qgn_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E-jvmqHLHaCfTvWxffV_dgUH4Dfoub9DCRD0ZBDaRRuTi8-iKWmUl7Ry8TZzORMEeulBUsnaTin-t9JrUjVwi6vCfNexcYgN6eQJyVNyZfnQUfII6YX-4Ajf-tz35Sn0IIKbu6FPfdeq2ecY9KCvJwSIqwF3AbFjQMYFJj2XVVdcu7yofKreDp95LXQ2Eh2U3lzJWO6vpnkytw8TN2jMuTeNMEHQs87alif8CgZgoH9A2D4L3ijrOY4Pffw3dgtQrLN8s5ZQ1SwN45zd42zN70m5dSThmFFxXJnx8Pw2idfqw5LLNZaRvmd9u3DGL4OkeCl-qT9zUzI93A5tBdQjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NCQwF_D3uK55_IkpHfI8fG1XDdweNwKOpqnFdfk-SUYI8lqvSldwmb3cDj-ZK_V4CLS12HshEP9K4Q7E_1prDBh0NrB_8hFbR4CpwLabnmpctSpmSBBwV2dBbGiuDu84GK8r8aMSqHRZUYlJEzXxdnLbkeF7DY0Gb9mW6AEwnQhhsYhgmIGC64jsIl3aYWkztkEoKE8KKjvT5GjybfQ6s4CiBjDt6-V4ymQJ15sazq0gR702vqAqyAW-9ItA6PLljh4Mo2tHH9dYNlJRYeEX-TqXYEt9u_kfEJQD04QvNx9uC7nRtL6eT4dmHQXmnhi5M7Op5xSPDZIhNm08VBXbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/txBHqUMAyGxn2QxJD1n4g43SXnmaf5RB0pUZQ-MigUzKGs2XGFLkfS0VBdVgq0aYF_mL4bjP7aEgmdfAZEI2g3Axffpo9L7UoBkz0zvBj5U1ljzU-wDdNuQY5cvmtPY9I5nCMDN5fBgR1-MPC7UI89h-Gyx2SbSbQGbaYLxDfARbOe1xkUvLwu2S9ZeJBYOSno5QFTsWfUpB6mA-oRfqlTFBhgmEHJ7PLG5oBXYvBnPhT5SqbLvCqto3HovNWnoKFNJGoGJQDHTFi3nMbEh04IHq3j7bvpQ-Z43cRYZ8IcFhVZNkJ6CGFi194YD0Cy9ubmn7G8LjQZhJf2Zzp28K0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=hXyZlrFH4MTozdGDhvT-ttGlyEftZS9EuJGQftnNA5AA-Lbf0HOp_TaiZPkpKOoqTLMjyUt8EUQufR2pamcnH0nsMZXGNN3iweD2g3n85ybfL2V7wp3qMYuKuNVO63qP_55dYvMERU0Iw73S11gwELpDiBTl4WsDT4KSfKPDpAlwGsJiREq-stUfguaYkKtayKYvT9oYfGYJ3swPgr8Q2X5rO2yQ5Y6oApfhA1gYU6s3yLofSiX9dUAg2ecmnSvFHlDkTXflHhgrt052PoO8LhuWNZ0Q_r5-4FW4mPOpkSJZFgItF9JTNIRIbHPqvCof1AMMlMcp-xWmheIZ2iyfIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=hXyZlrFH4MTozdGDhvT-ttGlyEftZS9EuJGQftnNA5AA-Lbf0HOp_TaiZPkpKOoqTLMjyUt8EUQufR2pamcnH0nsMZXGNN3iweD2g3n85ybfL2V7wp3qMYuKuNVO63qP_55dYvMERU0Iw73S11gwELpDiBTl4WsDT4KSfKPDpAlwGsJiREq-stUfguaYkKtayKYvT9oYfGYJ3swPgr8Q2X5rO2yQ5Y6oApfhA1gYU6s3yLofSiX9dUAg2ecmnSvFHlDkTXflHhgrt052PoO8LhuWNZ0Q_r5-4FW4mPOpkSJZFgItF9JTNIRIbHPqvCof1AMMlMcp-xWmheIZ2iyfIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJkeKYph11GMaKBYlM3fph25drEYNDXrtbtnbJye-01uDCSYlIQxkWglJMAENeX6qrP2HWQpcdvNYpc2gr5LxLur3XlK3MB4xty5Etn2pFAQU7yHRlY-s8dP8lsi2r3M7m_xNPfoekqjRFSFys39cTuEyBzzjogJPPKaoyHhYSKCLC9XevbswawJJWTg1x6AyLsBYYSrojBoSFX2JH8HDxV_hsh72pa7Cg2yjxkpm0lMe9gEa2Pb8cverQxG3eikd26phbW2e--G3IL7rjD_0mmnVnohDDf10Y6Kxlj1X52TRGYQoWBVoI2aCwjSBLDsmxEN258W-WiVy-5tdDsBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOPU6h9NsH3Li5t27AIPuyK4w7PyGaxP8kN1hN6SmE3v6dKJsMPxK8Bmv1lZQMwe8fkpqI23kdKpt_Qf0N9QI0q3Y_12x_Hp71wbzaeRd9TroThUPq_EK3nWvYpBgGrfe4UxdJ4-w3CLGHT72cnZb3rQGuoF7NsEy0tSz7OsgKppuyq6i67uLy5Y876YyjhlAxKIKoTOFwY7TFOsxqa4WTHrc8WGT0jTir9-1_10bzbusLPzRPCIZhRoBUAvTF1iRuWcq2Jss61mJY-6XyArWST8m-xJiPMPIxm9b62wrPNRSX-7hOS59vpf2CX9DzgBRd4rEAKfuC2Ui8K3Af9XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mjyK5J-kvFXCtlZksHX3QiS8L4rgFOYTpA73wd5w_85ii4HGqL-0c1SSgHSWmxupGG63JvhCI79FgNqGKqtCkcUtYS6uKhbVQQ-Xi91zCqPPEu8TjKDXUOOOeuP791nyEQPT2w-eJXuTJfTSmrED9cu4sE8XOrZZExAhsybrR9t0reEPABSBqYZbegYV0Wc58RPd-wwhHE3zgUXmXNS6UMy58CIjHBB0dybTiWEIvXuBVSnhXUscseSRcwYMD_PFndLheDkvL9IeFEyBi47gwl9ZcoaXet8xGimILeP2zrbuyNlRmGi0koKqNsdemkMP2H90tdL6xqo9O_YdOjGKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7cofm17hw16YmPHS7eJVsebif-Ujsigv0Te_Uc71HSPOYiGhAtCuoBQVnyRc-jIZKzddOqRMWrKkux1MSJcPxbPi75YrxMroVFQZF8B3kdbliSanElsbftJ9PHoSmBkX9Z0l5c-eEEb__NCMyoXGn0dS-ZRmR6xxyLprj1ZJEjRMOCedpZssSsBgA5YRqGPKEt0tg6DH86qziN2lWpQzFyo3sVXJ667ygf4CMY2sZJ8Hg-iITTVZorzYtBR6rOLhAushzKtTn8O-W8HDsU7jrHZuRG8wUXAtlHxqQCCqYg44gFfBhVG1f_WK1llEu0vF8I1MYB_vCACB-_6c_3xPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oVhPDFhtvUIBTX8o8L5G5z5mlZShtPbyD-nHgQimYF62qFe9302eVwSCdEyDjkZ6jx2VxdFSMbR8-IaggSo7Rb1vocY3Bz7W8ruF0Tn57T1KBXBfURBA-hsINFZa9WBcn8O0LAPQGH2xMKCB3AZV5v7LbVhRnEe_KXVsatNJ6fNasciKFlhOmqPnkItUkK_6uT5YG6iJekuOcE7cEFixXefAQNd4H9FCSJbvFcM5SnneOhIbnH1biTRbKytildDR7OCxKJIy7knmTSHRwuaZaUcRzyqL7iyTwLm7nIY1uvhniGs7Bx0aRZ0qDVts5NS6BbG0t7tzK9wJjWn2Xpr4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAleYgyh9hoRY2oOQ3es_-_ozh0LlzibF4j4cz_3vdumiffvy-21KP-YgfoqjbIbhk8UpHD1zjySS1XfhquG3d15PQgsOFqk5g0MF0xbNiaTAWtLZR46RkOEYvsjHELzCVluZq9y5MkkU2_wbVzKmIwEy-sxU0ltz0h2SoEoGcZuZ2NG7p81X52xn9U_YWDAtTIfaPmOkw_o47CyaOnY4hdK6otFMd3HFZX8UjA8pQZxqZX7MaSGZpZy22ZdrHvgvaSO70oQ9bgQjPb1A9xlx6kpVYHyGSci33b1jH9XvEcRfBmKHthHwRaeUHvBjvVfN7uPyQ9jyuNuG-Tp62UYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxLjI1SaXaejW7oTemgr0RgDtHgkhWeskljCOTPxxtfcISphS9vkmPhx4oELdfjEBCNc4thv4H5fsDx5_HC9_PZoWDv42KlcCmV2Egz8STazHBMswbVA5kSI0OkdXOi1yIryqPsOwQjRaI4XHec17m7k2y2ivPDhYMeY4uHQxO3yVTyfGSFrfoUFxa2obaVXGjHuEPXCNG_s7F3eft0dTLET9y-qNXe-pqbToMve1dd2NsN6d502-wp6BGIsROLcqBbJgjNO-r7lAO9O8ZtvmvvTDVsM40R7qmbI-JI9zaTQ3TirZW6oggOAlSbt9hcUO6KMY1gzamRnnBM_zU6xOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uBtZmd8TfYgzrL_gTl5evZCVAc0cN68IPJPSDB8u_oM_2biCD8nUXHxG8ARz8kKiIQeABuKR0m_IvkOsgFmnEBiLbZ9qUOxCKk84OTrk7feVv5JlQVZOqA3wfNXhrCL96UtEuk_80hzGV7jFjCQdkakr9dRwivSlfXfWarxlvnGQVFI29yvt9vq71kLJPKD0cy9x7M9J_-6N6fIn9K7PWUhke1Cr2L7WO6FxyCG7_ZJ1W87UxByR6mXQ4ILgYv9xrX2RQa5M04MOO6JJT0KdJlJN3LeAOQofMWX3ktsk7-C4tDjNwAvZbrPN2oVvluyV8yXTWBahXcCETcoNolG3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvlWCyL7EyDqCKTBdrv0e6Vxt3UXjyT1TscwN-y_ObmMEkLcP5KZaoD5U78b0iZSxJUjtdh0lMIvi3VMLoF1GreMF10bJszdJF-hF6r3IvVLlesYB9RsnM1FeTHDSAKZCd8mds9Ojqa6XYvhqZ_NNMzxdPwNCi2N3E_7hUSOZWgKiEXekCHXVUgQJnMyf7nYXxMIQB3UZTsmX68yPZSd7ws3fWEupScsTDiYPe6F1CFUMNTELDkGyfDma2Bp2UYyQyrpq8Txd4P8xAYtdR3nhEwfnLd7l1KsvkvFjVcUAdLB4N0WXw5pwdJ0rye04FLZfPsvBWfVQ3l89mNVm47RNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJOkyxb0jgZXW4sP_AznP35ToI_3nwBkC9p0hkOfer_C9t-tNbTe80wK8t2e2VTZk9JkGMiBw7mom8wTgE777Lxdi5EFJsGRIZfEk4GWYcyVuAak2hAHjLVUNUybotefTbc8Kdp4y-TobSh10b-wM8Qmg6va6U1SGQUoEuxMcj_jygOVGKI0RskKYWIExT1Z1XNmtCUARpSeoNTcXkO66CwpHAaP2hKV1OqJ1RNTxWK6DHlGgcDWFhD1qgVUkTWm_Sh2GbiAyV_Lh-29x0t_RFIQXiJCuGqXFPSm9XBSGiUMe1WkrzCNrUVphdeJBqztjgrbWjHHyOK1ydhVw4PMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vYYQUZ4A078jgEn8GDBUnH8eS_5oJRYS1XxqCIINuQ7R1mVYfoU6YzFrlBl_P7FT81I-MAr9joCVvz1YjRpf9KdCI4RIIMuAMOJBnQaSuRVaQwUpLNhS4xmsnwYbEUZDg1TItTsVopcKesLKXce1xrzk8r1Y5_k8LUeNGiEhnEQ1zcuQXC6DuoQ6_ZPl_Ko4skoXlQ8u8ZCZmGTRDUOdfFbWf1CKWthncPVj8ctTpyoSlCV7EvdxXxCJkkaeeQpGI_ZDH1WUCmxvBcZVLKhZhi4CvpQLpLwbkZwq3l9oSpn2AM2kRvVgubNj2jcVNUMCcf-JtqGL28TRDs_3PPhcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJ5qAaWXnU4y_kO5Ba5wpeVA4yl2sjl2xY2ghmjKr8qsQ270Y511_LCYpJzO8Gz4M52EY3cxRSjbMPL_deTl334wdOzCQ2ltuxYCXfSlRHnIC8WB4V_j_IGXOPWM_pfRlx4BiKi4Z6k1-4Sne4ZFoZDjrDiTky_1NbAKEm9mwIHpM0Dgwzd5o4j5fIAJ4ZRaUS7yQHarhX3zcYA4URzexXecdhSrsF-Jn5__w-bEXDHQgmZ8JgzHCEi-R-pN9BMbkFDcUfE1IZ0mrS4WpYNu6c_Q19T9oLvXZHxJK-mVvUp85CJB-FUo3-b4icKW5ZXvIDCccUuhkhX9V5jWIdvzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ilt6DkeiqBO5vmd046N-BNaN-plly-AQGdHXAM-I947Yv2tOVRmzyfP1kAkb1v3HFOdw3DXFZFYgT9vd3g2nU_s1TPIMQj-LtozgVzorFpvY8iTImN8hXpYGHDJCkG5io1GP6O9TfkDWtTC0Zjsrb4-XKPt7COJl62n5eM-OEPccUCdbAeOkb9Z3IuZdJboJ1pbKU002VkMGx3Q4kUn2_aOosdCWhboZub5OGDNCnta3Ko6Or-WlGxn22ZbgJFCLYImReZ1e23ixnJ8WUfqeNGhHilVjwjsOc4noJCGb4x7BoXJ619RkzrlhMH4RYVNZQii1dyaK8TNhOI4AiEQojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZHBmU2kMhNd9FoNyrRJUDw7MmSfPSsIfTQ7w1NyzBc-EOxnkUQrPH-YE7yQCRtV2YQfXyFijJB-j6SpjyKmuXt5rbf4wcSDMgClic-eA2mP4hyQfAbGEsp_gx9xiH9RDPU9iWF4WiOQBtsvB0eAvcT-fdijRfxcRphZLYgznwbE9TWXLJgEMCPMVhcZkNRTlhLd27ZIs3ucld9i4C0Oz4LIF6a-P24_yw8OTYxQT0iF71xhJmz1w6TKP2bDftoUkQO3mV87-PMYxkOuYoNVDdr6OKxt9G_YtKvu5MjimUZ5X4sS7PvRwgUKjoiqTarWOCNxi2oFHkD5V6kSkPVI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dBfJQsepZZMw_GBW1e-iliWhpyBvoXX6SZxvN3swATKP_cOb9ZuykdQVwX1TaCVVe_THMlFgqoOgLK4mDQGI_1auV4mLwHPcMzRop3POka3NsNCSqwJJzJAxc5RYCSePD-b3LKKCgndw9-lhzsu_D-3cSSYyoKeV63jdceIaugBtd84-p-Ka-zCDrcejHp__wg53nzQjHoBBxZ8hN22CLfGfkHtGeg2eBHn0IIi9G19F2zm3g9G6gLf5jJp_jTssF6OYdvonPICxlEGR5q__qkPxNUP-gLmVXLbJKl_vcdTASr6tbrRVc3TDMuNrTT7UkH5MVVHlBnB-I2gv077dOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZ6r07GlUBMI33o1Kq0yj8B8W42nUj2SxFadrs2HySEOTpu9CoLJSulFZTEGkvD_bg483RXeBLoXr4vuHZQZL720BW5TdFDCH5E9sN2LsaaBUAfikIsTyqkZ9FOeBX74ff3gDKPD98ai8mLap2ZqbwstOqTsjBqTRxyaIH5GP164-W5Q-32cFB5EeZ344Ngu0DzgkiN3KxiDIz4Xi5eePq7G1Dm22hbrJrnz0Oc0_v8vBvFtJT__uOZkB1fdtehYRei5Al5dq6Lw5T0ld8oTscMtf0OPHGwJLBS3iUbxM-57bWIQ-LmwyYcteCcC6ewP4oCvN9ZTZo4Bluaiwlu7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cj-QEZikajTlTio8sxuyZVVEkOkBLE9XXhXvSpPAMaGF7Cx_PhXYeWpMGmyfFaiC4OguYFIY60htWX4_0MaHPpegZ69r2W3E4plnGJBmIjsi1DmaQUdgPQij3opmLUTR7Ze05C9VLgSqD5eshERJ6KTNqKakEAJTHFEeL-pGZDbTP28W5lm-bvbzvIA0KtugYhSJ6MKweGwKP0jOB8GDbNQhncxBVulHcrYKnA81OYhS5w6FkjKsQ-q2EZZA7S-8VPD_CKuIZNaS0CLto9pJtN30Y3wvhWrzclTDQH5MrzrIWyIEyREYN7UnLz18jhl6BlNpdAkYsy-7TqHdui6SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UUUTWCVPTVSutFMbSMKrVHbN2WEoWKu3QaHOq9RlFWs4sSw-fmfZCv_GGgjlEZO1ddIw8C1J0VjL9lDjD2iruZ2R68ASH_tVZNle-UkITK_zuYM9w6lkZcd7xF_s3FDFxZvMok8toqa4D6tofb2hDoEs6L5mFNXyyW7VNNJ5eNDBAy-7XI3-hXVBLvUUKVXDIdZTRKIHhWRzSK4gIyDfu_euCI4M__b8oRvvt14dZ1mtTUwAaO9mQPL8ZNeHvoK3kZm672Z_oQ6YYvbAECy54OZUR1YAOhClpA5wZFlkPDpUrBsHZxjZP14jjyER-NT3wZJ-K4g6-t0LqqspChCETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cfg9f2Qhz9mbcx8sJ5tRCXN7KE3ZKxbwbC-XEziF-2SbxQZpuf3DZ8XV6T7UfXuFt4bLq4G27S3sb043nMcqD6_5JfR8S_BPHNF6i0DEndObWx1EtgAXxl8dfMc3UsNFfZT0fogPFoIFJNZEKkYujFPpwwPhGDW8Gpa6Bwh4GWFVfQ6LTmVXXWCsvpGFbieE7SV_GbwsYg8AdXP8Ru4BdaNJf3KoS5zfIEYMT_oOIyy3u2sWNBFZ7AWmd0XypnK_CI894zHfQUTkNSedbaw9OXkSPdXO7FR5th1ZJ7Ay7PniMn9eTrd3Ps1SbLvUZxaBWgGIP7Y_2i8IrhzcOcRDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cm6RskD42qwxXybVEbAWJx6nopz7RbVeokAFadGhYmAXP996BML0oQvaEgLuQG9OkvEHnTf50CQHtmNCzOrIlCihrIznXsaX9INEQ6UJreB2yIt4uPktEf10Yttv0fwP_zNdlhnJu-WmX3NzJzGd6o6TiuCKT2w3LpXcB8dv97qoDuiZKCEOYqvu7DoAlXsKI3aN6PRMWZ-Mm4__D-QdSejgFh1gcZEsWHnRBqdXk1cpp6xuLynhzTQnSnFyQsTEBk7fa5-tccmbv4g7HN7rwRhG4Ql_3KCLJUXRwc9Kr37wqzLMZD65uIWLtNmfL6l71LD9-Ii9tzU9X-5NYkcdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pcr6RACegXJkCB-vbAGxFng6DwTr4yWvnzhYqLiGIvoT66sTq7qclEUtiVEnZQ_-acBaGcgeC1wgO5sjFQDwkLBH6wcGvspwO4ODSkgSVZ-gaZ0caP_aSA-iG0Eq3xD1XKTjAzxtImKI1X7TaGzA10q47djs6M3P8GWeh4cGm28A9qReESa4NaDcrlg3QgmZOKe9O0aTM1jauVcEIIROvl5gdFXlX2er8Vutx4HXqUHtCqXtcUMZymlZ3cwZ15SZsH_GCoqAmJOskDY9Dr_X9Ct88wrM-47340vH2XHTXuKEvF4JHH7Zb7NAfpRkrDi1y_eMiUL3BM8twIYTPgjfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WivUvyHgw-EhGoa1djD5xs3YxOu2iGxD9KmTwWzytHjwQJBtnpi_Xj3XEUFAwut0ogFBG3rf01bGvUGoDXoDqU1j14pOo-xNlkk0quGysKlmxTvkH9o9MldtoBcdWWs0_8dXus5N-ko-gGyJlF8Ywkkp61IJOoK542SA1a9f8hPUeVECJ27VElWzrwflcqhKkB6TRI_KrqNPIq5bzNAdeZKRLsAcHaEY6wFCsBxKF7UMHrgsOzPdivd6g3V-hz51sRZvDR-Ov_DyMFzck4B0zc0-uKlCZeZHvvV7jAFFTJe5Ln4aZ-7FzzJivQwmzaRWDDKKSUKQfqAVEiiq6DE-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oQiQFgYk1Eb3NeyAKWJQotvS81L0YcABNhqaFLYhClHwsI8To7jkMd1iNt1bWtqk3SVBhgPcY00sEyZ28rxKalVHgFfBHBxMedBdvDLE4YfkC0Js2IBBh82QxujVYb2nZVfbBgWLW5OThbEAQvPMxthuIfwZcFDUbHB1gHDKmdfqbnSenIdRwi-i4A3ZlolCcVOIcmJMblYV0kPJcG5dFtGDo0A8MnQSfcT9EAYz2sMYyYH1kDMEDBb72n3fAx9h6Zujmph0l7cQVkkRxWIfPGnbm6fWVcMRjG5vo2n61lJsfLogMBwN1HRp0W22omcmkVjFk6_WCfAQDV_o7a17kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2bpBmfhmXVqAn7KFS5xf-hlORaq2wDl213gqDUBb9fUeyXwyaQu0zuBics9AJAc74shYKLiVPblMDoTznj0J8fpD2qamrLsLIdyV5EvDPb1j4axm3uszhhgNVe9atUuPlqhKP6YInd36htOrtSWVQM--cZLrXjjPsRFj2yJ3ui5NYeHJ7O9GOuvsaicENrwqO_3ozp5cqeVuB7tvHwt6gse_-QMUnu8nI_41kTe4gKX_emhHiBRt-WyxJOzcuPUfvtxL7nuwhpnOhXuxZjnt5vEQKr8dOKt6uElsO5MVgDSuNuT4YPnEIUXGrs2nv-LSZtjDfsp6hekj9tl7ewgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0H5keRb9C315xXNIprAmA6aeD_4ks0n5LHK_F38sf6-0klM4KmtKm1iH4GwpbnQxC4u3v6tFK3ocX8vONnySisrZCTHV_KhnHRpZTbARNyioy4uWqZQLt55jjA-cNLzmlS1wbiF1Ap5sAAuZL0OJhStZBSlGOuvnkhcYGN73FFLKGHn0U03lB-6isxfOkxE_rLoiHJFGc-cDgC6YSXZBDu3D3zNy0m5gEuKltAowCPeUovnwil_oDVM7DyDwZiAsuFxCtFhDB97N5erxhY03fG0nkW0Vc0X7_KZIKny70GGX1g841IEkR_aSSPy8Adj3vPXPjRaKFJlMWlOpbOaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjjZ41N0iLz5OEVG9Z1GVuH37R-waZOa6Jw3W3XymJSv6Yp3mmVVb63Gu3HW3gRAkeREbBdLJzo9RvzRKdIdoywjLRtEkvKxELP7Y8kpktwKntH54BwUWLovdtYjI8gQ4luAncnMD8M7xI2cyP8YBa5q_h_5EG-1eE8-ek04P6ViODFda5pWeeomZ7m3X0PKq1NoqQWF4O15EHLAJ0uq6x6_RHlX0pmufswrEsZBsZA-T6KyobQmBZitoz6kvJunc-4_cKi-o8cuM0R3t8q5ZomnzTVpm4bpCgomw_9gNbLDjCHbr04z7MTrR23fSFaBUpyWmD7ZBsgp7Mws_mpthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
