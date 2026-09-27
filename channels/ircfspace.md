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
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mu2n15XYQlouKZCDh0kjVQot1OZSBKZQvQOSmghDn0Av-LJmH_5ODzH1yRj8etmgzXX3B9wV2MAGj8IQjV4HmuDDkAX-h7C23ojiq_Hn4sQl2RgaKTzfhDBGIZmxuQqt7-GfwA9fyppPzyvmFKuYbTN5Nqc6i0QbFv7kJwIw2PzRf1TkrTVO95BhzVz12iQTPjjVUY0s9J1-PY9WObBSvhNAdrnHd9AQhVWzJJk3IlVoVfamEJVaiLcrpXyGDlWpACLNxoK0fgYpfvYoo_IcDebZ822nFiL1P2Sbl74knR_5QYLmTe6knsrs4D30bjazCukCkck7ckfHBEHbI7Yoqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DcOL3e98F3qp2UuAE6_jRJJTUr1sOjDxfC9FaZ05LXUId6J59cKyESAlPqF1Ab_t3-bkNEKIXCQjzECNs7vUObrI2UFl-8xuHTQDaqoWdBz2nNdd2c71uGFw2sG_p3eyyvDEdYXRK7eQLKTaKCDjq8oAkvKPhhcoEvXjvabMR4GfdTEm5k3JPJjlRoAmEMzO-eF6Ex3EYHRquKKYLaqgb5mPeMJiA4_StbkkL7zJ56Y8Krccvaba2WSFfZdIYy-2_skOmIa6StiPvdQZ_ZUbCaZTOj7KBZMbYYqLb_NzBZGzmi_E_6TGq5qd4kqzKmD_tFYPZr2jkGIXViY1B_fe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8XTd_dvlDDCZIsKcbGUtd7-MS6XesXb0yv0D0tUyhjWpNmR774YRdmY-HXk9uN-696l1hPIV1N0eFLVHOlcslkF9c89DTm8Ax49KB8F_q1_ooCQxLIrXLaj75-gA_s3YcmxhGEkYABd7TEKb8sOJ650MVn2tN47wVn7ED_Zc0yBWjsAXuomV9XaPd_3_tmnAD1KVF6ulaTwq7d212L6CYxNfGU8rPzTIRm-jO8taH-56PgDjlNnIlQfCabxGO2m_0HvC53lDaW26V6RttBNPkxdZo_TLiev9vBLEgQFEYLre8fwbu51SOwrEP9PYdFNWmewVRRepjMb1ac2qGiHXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhsrSLVVnJ4zaLzLGfS9iE21AFEQodLtzo65J7h8XJaA-ypfOE_t-LlNM6-2esSdhqVsmsIpgswCm_bsRC2yT4K4e24Zi3X01B__UjQ-PCeivApdyjwqR2Xo18PlmvOtz79h5YI4CKpcamBp7Ur684Z-YDPKIvjlqGAHm-AkDb0sVWjgAds7C2Ly0pON0HG_R7aVohl54akp1vgTEPs6VZcvvSiVe3jip4ArEC33h81A1Z7aid2T8mwNxtForJ-7Sx0afcUDrpTXBbdHkTKCZRzeRo9MqkJLItmtbtGAgz5-p_OBpD3sWgaGiOAei0N1IQW7MsbRDUEnXNhjuWnl2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7HlZ7NsW0Wm_BJJFjCqhG4MJ7RuqZjBShFiEKoVDSmcpJMKsQR9EEygPiGDzPsDZbURTcHJN2t0tSg_bnm6o_GQ6WruuSsQnlYDgGBvLtwXPZdqnQTmEWmwzVPKEM38fuKlgLaQrg5WEgeROMx2anE8sf8lTgPi6KxSLRk3BjuhcN5yCO0aHjhwooMBcESXZ1FT7bIJx_2iOB0tVdTBRk0DB8q07fBaGSie88C3243zlR_y0WoX8l0jxWtIsnN8MSa3gOeMOyb4n-vXoZOWXWJp-czBDKpOe6Tb-7TsC802gSnNcLp_vNgUhrPicLnT-uEPB6JTroCCM7zsMmeTAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-TlNWP6eVA7NLoFhmeX6Mm2pOgyghlZK5T19k43LSGNDLNkvlMmxKKccgT4Wd1CHGDt_LgtpFH-NMAOVPkUMKV3AjoQ82e7IOWhJCgVombZXh4cI5N2XGjhoE7NyExHJs8LM5Db2AvDH1uyv1N84Lh-FWUogA-kIdbLU2ajzm2ZwoQl3-85ttAwdRQJdsnNDEg8C6dri_f5oBZkohmR72L2GNjgDhvDvVE2MdE3-jvvCZDsbREJf_E28NOqlJcCuok096hMtqnOraVFXXwv1CUL2kSBm-TUMyUz_JB2sviJBqFybL3ixdCL3QHf5Is0crxiVYvk5BYlbAiT8ujuVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TY4t7Zr7UD-it6KKhIvCIJl3_gpgZiOyE0qstzOWoZ_cn1GerrNtl2x6yctPEUQNl61iN2plJNJvHhypHr8q3H2-klMGmKVWvCAdLFnQoIiCUMH97xxUhASo7rrf_M5_9d3PDGRzs9DPwlwfLSQSGKfjb9YbbB2jW9St9Pa3wsZhQTVF0zgQS_BRr3tK_1wBRWw3hLdkSppBNUVA-Yy2YJP2EnfvOWbV_t0rrSuLhQBt3Zk4H36D3KGdMGfynxiNEBcCP-AX9js9_RGKGyrDZ5OKD3T0qV_av_9Bvt36URTvix179RMtHeDeelvedUKbongAnLP3uRtu_i9H2tbQvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9rVGspomORC0cgj9_LfoTe-1SktwoAhTyn9F6k6_Yp10byYkX5Lx-lztwLxVSZCYee42I4EZwkadvTTNdnBvehdmvxFYv6070gDoEMx5T4UnZKhsUAputYU0v5R1JLvrgcfgO8DvmFpE7irc4L-eMheFlhFeYluzQ9AxtcfSzP_u0PrZ7smfyQHqNW1rBrmrzYbWZKzoofqBsxbewWOOf_K2D5e_staKPwtvq3P678EYUNzqoIqHbMSW2D-ZbmuXOAyzakmhGeewjYOMulFYd_eHxUg8qNunNEDs351Xsf8mFk1-qon40lEV9pGHNOyHaAzRfGM35adezvojSH6qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWJ5G29KDzXK6i24s4DhbU7NQD0LaZRQ9JkRUehXy01lp5jCFotg-mFwAS7YML4kaUEeKtJZDHU_X2hcx1mMU7IYKm0gFkYalDc-X9jLHTKx_VrC8ijIjK_Ip0VYnqWWBxbky2pwYwfmmbpq83hJjl6ib73v9s-TuT9KX7p7TX5xHNqH46LD0asuqCfpDBepvFqCowpazEVVNSOQeZ0W6JAkH_Or8toDjiHO8yncMiLQXoR7mLWctxGT2yTKgpnKc4oA4Koqtu9PH9LE0sS_0VKG1kBUqhEu63xy-QF4xzhjs5hwnMrOAIMaLT_Xu7KrNFyJAnevhqxrzp9923r1cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XasoieOnFHZrHCagOiP_Uy5ZHlZbrBRvvX3HDas2Jk_bC9pRl56NvJwFYrmTJwaN5yLb-rr0OFyekToNMbolTvUzWC0vMRIIVJIY6bI0L877nlyzqh7KvSV0gJzLtItivy8MdzH9J8fNO5gP2cGvNfwszsiwsQmvPNVcp_puGSqfnYL29dBQEBdzjXzTmwe1fr_IEcYR-Tuczq3slZk4xY4z35QsWUrs6XTIdeGyNNRNUGQQxLM9-LIiZ2ZFPbCnCrnMp72kSJZt65CCHqEZKd7rz0uKUi54Wen6dQF_RnFIcQ5NwCPEcFuRywgeM5UmlZo0NeSKRULFNwWYlWoQxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLY9l6-36KX64Sog_YEB_aBZTcEF4hMmZQtQkJd4cNg7eIYoxlnSgp_sixI9hQVCheZ_yG2t9_ZGB07ZGjXSv2cE21x-LJRGC13Rmb5FNQ049TySgMIVWWFgvvOfRZk-Ydl1Y0cmyNiGe_nBGKjMse-n7sMw06ygYaypR504UsDpaQgPQIOlQ0x9QM6h5HsgKp6c4qxeum346mwOulbuZCwKbtytuCYR_Ap--98DQhx9sBKar54QGJKCtUv1qNz51myk8mmmkS-N2UPcBkyVcVz-6H2JO3GvNv2LJ4LHZQOG8HGcM3TNb0kHu8JrG17ZqS9_sqZkC1Oo6IvsIBMbOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ao62xRDyotEnbHVRTPNCynN0f1WAMxXjr-Q7WBJKul6QEFggfjv8n5bcAOoEQSG5_XZEC8lyLp6VUHTElwnLaGjjNJDfb48x-hwgXnqI509gaDOoIapLOm94pNTx2AkSN9C7IeyF7uRDzwSaGw_G7wFffQUXI7TEhSgurWJTmF72OmHVl_RQSvfGpcEuoPqLKNDvUNj677_EH-S3ReoJXIM9f-yklPTa9_kjuISUBM2s3_yTlKmdWFCBaCOhPzptX4Z6pkRmRHs72AMgIsQHfxLo1Vrf6ZnatO4AmgHhDjiW9UGyBce98leM1MYRP0847YLAZMvMfm88JqRvO7Qixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ao62xRDyotEnbHVRTPNCynN0f1WAMxXjr-Q7WBJKul6QEFggfjv8n5bcAOoEQSG5_XZEC8lyLp6VUHTElwnLaGjjNJDfb48x-hwgXnqI509gaDOoIapLOm94pNTx2AkSN9C7IeyF7uRDzwSaGw_G7wFffQUXI7TEhSgurWJTmF72OmHVl_RQSvfGpcEuoPqLKNDvUNj677_EH-S3ReoJXIM9f-yklPTa9_kjuISUBM2s3_yTlKmdWFCBaCOhPzptX4Z6pkRmRHs72AMgIsQHfxLo1Vrf6ZnatO4AmgHhDjiW9UGyBce98leM1MYRP0847YLAZMvMfm88JqRvO7Qixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cA-dHqkuTazY6ZSJyh0zD7zdsdAm8mVW-teNffMBfe1EZo9wz9nf7hDCE0o1X5RILTLG-OBNnE5oPboL0fTbivQXsNvVOJ1_pwMBXzcpAeSl1nSfUX5XF_kVFsjsZggYkVMSDplB4ohtfGYcDUDGKId0yUS4kWMatHmWkIcANkNqfsTPKFSqYJAnxFluvBrR6mK83sQ9gve3qfqr-ztZMkXSyeEtOqZaPgcJW1QoA06e4iYmz6CNb9o_ov0QB5z9V4SpaO_HbzeJFR_bra8-caIeg3WAmhUj_1whT10X_KGFffb7a7lEYuphdpn_8jgJzW4mhCGCUxC_m_s-UAXpCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hV1hcHMDU5DDMYfay8Dg-fRXGRyRFajfntfEtPBCV88YItnpr5hD4L0NFcb-x0yji6Vtkihdud1pG0IXiDlrQE-tVMiJMMDLokShkSS7akZhlK-YmLHpbFGn5sD_3ZHHhvONI-7DWpfESxLDXFvongddbvDkfCnRidWHDTrYHIwu8eu2dMP24CJL_9xPCJrANrhto1BV3heS-Scw0H87p2NEuuQwH-4SGPeoQI1nD6crMZ9EJMjBWW6yvaO-LZFDEdEzB3c8xKnsib7pMBBy9MuWAQ5PFci_zqdAroVrf04LWDZ13e86Bk0n3aoe7yDP2Wu8BR_V0ioUOqursZpjRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6tlOEufsmt-9yaOhTKK4W3kJzaRicKOdeZ6ZB_sbPyHHAU6Kf1BMR7HnUMnHFXRGoSrnZ91nWJeaoTjqKh7Ai2qjJz5Snyyb82skSA9UYHIaAgoNl2nzmPhxsKM6c5ZJJtDwWn1ZAZ9rtJJ1JluJ_kn1vHE6cH4JrTMnIbrw3oyzkj6-gbIc3nBM2NRD_OSCeP0S1OONXDKNFR9nPRUq8s_OrrwCDhXEd-Kus81lgylCCRVcbKF162OIVd8QhfkL3F2TrQNtBs6wkVV6SfcA_oFK2RYwk4YQanSG3rfJvbl4UVd0m9HX1MJZ0YwMYmcSUi-qdMBoYx-Ej6FwnQYlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYb5eXJ46bji_e8o51oqhDyQIx0JkuNVkfvaOGq33Yi6JAkFxzEHFH7eVxerKPfD40Gjl0DmfR1NaeOtg2tE1DbMH66inFJiM0RAgnseee2uxtjaq3Hx7NpvnF1aHfdhlCJ1aL3FrscMIn_Sf1u3iTG24C8P03Ww8aS4SyrTM6eH2VnDEqdUrWcVieKQG1WGGRjBFZ4btLQXAnNKT0jcr2W787wpzIJiv9JbcZ0ak31eC5g212C4WCAQ1KGdr62P5LtIb4p0FOXpNXy0deGyZqxbZvJLrNFYTkvjtmb0YE5lOuPDmPLtHNi_VAY45iXQrFCNb_c2_qvXF5jWcxwunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S6tjLK4hvByuJkt1_4gmq8xFU80xxIewKFRXcCNgc-COUlW3dPlC7fgVkeQ0eUcR3Jydzf6MpUN6eO0iUrEeLPLyoPR0KBmmnba0m_dW6GWiARemyKoSb3su0oPNVUQrMQ_5YFpZ2ceahP69W7_DQkzFsmsXSsfjqS-sFU8kSYnmfSSkQSDsnljkkIvcOAunIbIWovNsPX_c_VOqOGlul5uN9ExNM_Trd3Ds5dUbe68NXtZWz1fB4iSBooADXtNJgdfarInoVnfsEoO7M7dA2SOcsk2YGgRVK4qvyaXO0jP-RIltJ9c7LMgMV4eRkK1Tp6dfy2jCBaT3BF8JV4LA3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CCGYSweNT5btcE7-bVkbbzoY73bmWuglNemEaVnRQlr127fX2md2pRLxkX2Uzmbh7jasrC1LNm-jCWhOu8wpn49RtfYmSU4cGcqgUKlgO5Gh1A-5cdfoSGLQjSY27lCr18alKMawODBx0xWPjcWtV9Y8TwGh7agvUlBnNeiKKqGeLHJcedRvqLuLvho8ProT3LA8yGShO8W7NW7aITtMlV1mfsFZjjBjuQp7rYseccPpMmkoH9zWqHm1SaFcb2VQc9X-nnpbCLkyvjGA9b4y5tNskOrBq5NGFlWWKlhSXtJpP2Ldo9L1qVe1BMKTqXBQ6zoZPgq_TuG65QcNUpSScA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDj8gnBVgE39xgTIEX40Pjrs3Uf5CxcevsbCwL3UCQ82qIho20kmktpee7X7C0ShbWMvz1o44DHmlMstlGvMyODe6FfIrKj9v2GiB5SEByHVA1-Qc_uHuWG_ByVKKmpPrARX2ydirVT_nK9BnMWMef_HXDGQ9YNwdUlCnk6qrmAwxbE6Ew9_LhuXyKVrwRcZjeo16XV71LGimGthJTMitP5BBFbFEuOuReD-8QhsGuLcgvLf_xPu2qmqEHZGjElBkYVa58ktZeiG6qX2_X_mpL0WcpO-iJ-sR39xDfDkufxU4TDTqMPMCyF1a_E1qDhYlFkpmDtZUWycFGfk99iZnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E9oIV2fFs-TJPqV7VTNxI_6Mdz3Vbf8prDLQvsXrNNst_jXNK3YJiDu_2DjJ9eaALWlYVfpk5FCVfVmV24YucvsseFcqbDH98CWOtkCUG_ZOKjXk0VcLgINHgnMn6L62oYSFkShBih0vr_5Y04zLD2s9q5fLi8lgqMEzx-jt37DcXMcEW_CPNmX1ryTGdSX4UWX9sebn43ECTCnfigpd1ZDPWRIZa7cgdmpclFrP2fOZEbxUNksjfJmFywn6YgPQ9tsHJ5oh8vjNazdHfFeeKbOV7ZLLjnCyYvTdOzd6eBmxXX2K9Dn5BXYjZgciYpqN-5f1n8HvkePHSGxCOpu__w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mUHvAr_cL77dLIIhrMoC4K3ar5B_DDw7CIl-VOPBKWnR0bJBnzFR8ncXLsrT5shDJI_vIX6nn4FHo6j7YjxEZaI406QzjHMBu-9WWN5EEaIXTiH3OKgEzm4o7UuDm30MB4z8mJe9-oitkrYHWDT5qaWHqgZcMC4ix2gCUh5MWmT6fdxqZ2WYhS5pyqIWOFrLvAFk0f40JOceciVvjG8xMQus64OWcW2Kc6SwKEUVZ0zM_YzR_-zmjmD_7slzCYkY-6HRui7iFwJfzqUInd6bcv-VajAGOu9Cs3-E9LIWz8Z7WABDLUMEpwNG5vKzPEd_IHWWGtmmfBGsy_ZsCh8BVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZ12S6qVVaKzx_uwgE7HVa_WRhLt_eahdZk55H4iBl1ypY55nKVrVrV2UDECHEvBC6_QVqjZ_dV5rzs0aGCj4nFFkc2pjkcjJS2qD6FGL8pFcga4T0XjwaCeJeuS_OPmP91EauRRuNkNMMhMXqzUJdV3SPJhXdy0Ik-l5sxFOErv4x8FeXWYfuEpH4I0L8wayYl4D4Pu5QxF97quJokOE-0ahngYRh68FBZ7TJWi8zAr1Ll27oXTVaaP_DzQllgN4u8wDbEDB_ygAHDElXatou4zSOo7S_h7jEOtDjvt00VVHrWozsWJ5LIkx8-QzfbCD9pp2krd-d-VWJfkJddp5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oz_XdsXQ1yB-9vL1h9qG_QYgTVTyZCXj9VduB46ypctI53oakUilyt9VB0mGXPUAKQ-iGDtSb0ZPKFh3DPApxBnz7pbPGRgL8kWEaoZ-7qr2N9UEc3P0xaFDQiOkeGrN-KW0q_g5As1kGO1C8g637ALsB0wWPFnd2YkH9Os0I0x_cy4WpYvFxKMi5NpgBIATZqY4vZ3q0K8alqbTndlCxWf1BuaRBMRvEDKzd0xwcBO1VcG5QqO81gX6ICz_QWs8OLFpb6PyWY9LlZFnaWyfj-2B8fkCmb4n6w5h0FTWiKff0ucXsYBbaPdUm4SmbT3pAT3t-7u8DlpSzXveu0qPwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mq--iVClIc5ywlVMT7MqI0cB2XbGfMuiT8x1lSj78MhQZV0ZX3zxITcANoWsvX0ozI8uYArnsH2vtUGC8ZI88tTt0vb74JZHTK5S9PUJxiVNB-rbMOj4aH2nCXwc-OuDLg5W9MOia9sRi9txzBuO-53UJtmhXALa1FYYsbhuRZPU-41mGcTg873VohdzHPQAVfpKwFAOXHBtRyVN0gqE0v4O8PiDLuBiQZiRe7T7EFDfKULeyHdoqxJddsMy6XLHnew5U4uL8d-_BULQAAOcVmPuPGftpgf2QxNSFpHu7Okq1BDoJF30-afRGK-ovLL6tqDbeEPAEUvbViR9ix0eRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uBFM94INqnOrgTdHaUlVfprZe7n-D9BnB8g8GnKzb-SzpWSsKGnUdYbGchKImHr8a3hQOHXWZgEsvTOG_97N1JrgktKpiZo9ZXhjimwXjzdIr7sknwYgROScF1asjZMOv7hnRP7JqEo8ZSEzX1z5vPANikPxAV1030Wh2elS57lWTfii5CNc_MH22WnnsuIUAd6OoJvARmQ65sCl3axCpys6c9m2PCMZlAD9E13-KXlOVkmH7OV_cDOuGTM5LVg6IX2XJEBnlHAisc1MA_AQ0-ng-b21vHRskX11xaIg-5lrtxe-F8AwtS1PQqLgwOinkoB2HkpGWtE97bW8NUizDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Saf0GhICvG55C1iYIHriOj1_O47sdMlo7xvmCo8r_0mznr9cFcR-yZGANdSUqLKy8_8-4MIHoh3uD13RJa_Mg1xpHQC0G1r31kSyS49eb-5EbWNv9wk_opWm7mGfYrrfYW0T0dRJNRO8-a80TlX9sB9_H2P6Rgs3aYIUElDBR9PtgwOsHYDsjQ8ogYoIhD4bd3Se149hACkJReKnHhD85bNCBRG5Y5HUhG9_DhQSNw4gLZbFbp5w_O_Mt9kFWzpgUm3ziH9LOVZUegzX8PZC8z-AnozjsLWO_GngtRFVnSjCJ2Nb3TlaI5gLS7o46j5ihKn8QtO5rK2r9v1l9W0MTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oC3F4Tmjh9Kfw4qO_6zT-VwwQYPIyCmoOb-EARR_fjtEGBDYWZeOCGNiRQfIrGqVmFcezB27AMUtBv5-OQCbmY8EyoDPwJi6yWJRT3M6EhZTlqxcVdCaF52MgT0t9jB1ptTsJwBaXShJ2ciM0PvGGe6ihEUrBfpraAeUIyfmtnGkdcL7fQveIK5BhIN4a3F20Q13_WPVBIxTlRXJfBviosjcmjL8P29aKhjcVeSowACdOwNgRwtQ47vVkDmpfTOnPhqP0d9HVpecYkqcGsH5xKEFhbaIXYlhfTApnYjboAJUUJIdkOcJYIROCi6g4aVgt4x-0Ro4xhYYaw-uIZVZ0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCOFRraaWYEZxl_myRoOkyq0_EMdOwYwRQkT-UlIyLZLvh0-Jyao6ck_EbHvQ_hxl-I7NbyPP2t-7D34uHGz23Gy7UCpxjik3FkG8BHD2mF68bdNdVsRLKA_e-CZtiELEsYeI4sgS08r-fNfD40xGn8Jmv92tjARiswqWq16oiSW_SsujH1jrM4d_FsZB9jOsAacRYPijViQwvaCVI5kpffsmyundgyxqXpjq8iP4wf2cshFXuyn7YQDywzJ6lzWA7raraMqCc4wSjUaAKulHRmPotBgZZO7Ko26RuDevC8npuTcaPUraRNGyFf9HMPMgOslMkw6pXKBF-WDjaDSGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJMMjjDLTw7pEFSN5CaFK3OinVYdGnGGGSXrOX09e5v74kG5odlBK6rcdPbZ2CXLYMcOiIR1dtgZQE32oaVA4lDyXn-GSmJe37gS34dSI6-3N8ch7tLWYgP0YnEXXNDmu9YvpdihBZhHynazI8Zf6T601NTez5G2dSriITdNzY3w9WoQcSgTkD7mjkRh6orzjbyqkeQlxIsDMYPVSygnJoUDGjiLILcYbJlGOPnDm198pLSsKOJmlzI8RAksDiePHaE78zde_n3gizMHyzL1nxN5vUFl4oxaRD6tNAsRtQ_ifRATdJ3nSEW7Ea546aNvqWM1JOs02Iq4-suGBiMOiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FVkFG9UKPELw2EyJ9L2_KwwiF1riooFgbkks6iGP0WQo5aMGuNY-GPNyr7ywZPyl26V-CdEGOh0988fQ29YrxdDfKi8vt50p7UYg0AOHuwyo19adKDG_Vrhj7Blc9NB7_59BAmWuB0ATHC-g4RRF03i0KO4vZUU2L0_IW1EXNdgadeRYtsbhxCFyqbL9RfM1w3A56wN2vbjO2by5XGJMa5mRRsmi_HYT0On5QoQEHuNLwUV5tQ3jzusjFI-KbV_fEsQ1JMHFtfU_1KGosaseD3zq1xLwJ7Wnio7PM0KUqUifdBrbkYAq3KbvvELvxmBt5ad5Cwk36CLkBmuXriEKww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WbzITNbjHwhh5rFVr5hTylRI2bRb7N3Tu1V0kkOGcjvK4wYmTTEB9J98tGAak51iFp4HJo634N-BYbHrdLQAj0UYoVOUTf7dXvMj4OXmM13seCJx77t0bK3TgI-TBFJz4JGfQTgGJROny_x5Kbs9cm7gfADj-47yF07bEEy6kFqhevQMlTrh1XCFjlzypsUgqiMLMF2nB_aXNqrh6422U_x-H4q1zWZOERWWeteD1zqmfuUicEoA0IiMlZfmQujK8k5qRZ0M_R4BmxaZD5buNajeRWaaFq9sfCBzTlUX4iedGQ26Y3Tsxbna43tC4hChEOg9U6SJP3jua_-kFdfOLQ.jpg" alt="photo" loading="lazy"/></div>
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
