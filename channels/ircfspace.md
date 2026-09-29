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
<img src="https://cdn1.telesco.pe/file/rK93BuGdAQl7sr9HtdkXn4xLiLwztAcdhoHu2dzZwDbfFg6KMUvBwTFoALDZfV3hh0f-HJC_fRyWLIT1b-vuHNsLUT_HuUuJNLeeSEfZOdjU278lpCvyu3lXqY2t-xSzwdG3H_mnjPozd0CNqeRe-4ZRS73XTtFTo0WsMg-Crk_niBedKb03nPH6fnbUEkzWDrlruXZNscQPVQBD_vEkVSEndjOzelGkyBzh0IUqN8UU1cT_UWKdObuCnsmF1gPgj4eQoZoSSzMwGIDW6aHdsxLbBOexD5Kna911g9u7KhpJy4OELXXqyCVNkuOtduLypTUu-XvIKVaSYM1y4xaLsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufFj6zBtZ4wa0JOLl2h_Gigyb9unrOZAJyXuxBp3FyiwgX1UXZYERPcucXRL59ElumKLk2JVw9gxxcfAWm1YbYRjnlnu-EPExNv8-wyTzzglbnL2js9fGjoz5a36JPHsAD9-mgSK9y--OZuYukBIMFMCTwfRt-R8uRTM-WMXvZ_I1MiBuJ4h56dOAWO5NWel2Y15HtNjUbSmrqfayP4YUWWHnQWQdEHobGH2QTw40S96ZBvEzYf7k0mLDcQ-xIdtCG_7lae5ARRRSDZIkpqd0ZM0YJ2_yJVfuNeH2vBA0CzCLgIUx5zrWhqtGZMYg5YOBwRoZqzo6643GCNo9K541w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPjkDYaVxUDaonCEoLmD7376nXs2s6Dzu7has3LyvXqUuO6PQBENsLiLNCS9JZhDDPugWm986mpmf-DIrkBcyGpQeVwjgcNKkAVzqQCuJvcQdYeCXKXAT6an3NcwQzKN_3NmDtw1f194xzhYJwgoch4QWnj-1-tmEa6sejXPWLxFzUI7z0fEBoPkmt6qh7c1fqtEgDXOssk-hwNOd8gzCK3784A7ph3iwMOJdyInQ2xZhw_tDIFNM7Pg7E3kWyJzZm3edAKibbYKG4lku16JR2_UFth3vMiHW5I-vfNPgfLR5bErAPDaw2rWidwZrGYrq4g_igLvHtRK_BlUzVdP6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XseX5lWU-qFik_bLp_Qka4AJ5zyWYnTCVC5SNinzGcOqfJV3twjAkc9UvOd-qkJaDURnCVXYhxsqPsfpA0-dZbgRNO2rJvcuvPk6Xs1Y4sWmzLD2xNPt723zmVHuxOQfwGYD4kTYGHl9OTj1PjlwNsPJ8fdmTz2nu3VT9ZzYeraav1JxRNrW-b4bbYA7Fq_KBAVaL0DhknrtoWUwznH_hdgpuqa-jHXQLM5y3aFftKHfwgmKmaz_jZRrU9JGC1Wyd5O7ocnNINZ3YZ0aC-zq9YsSQ5xc_9ova_dfKnLM871TVe3CgkSeEbrKXGiS1IqN4NrgE1Df4eI6C7DFif2qDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TO48BKtLzNvtKPra2pLKSuGtS3pIWBf-3LyGnMm7en8lUGhOCLQFiEt7GbYkJ3cNBXLhy1oK6nE12QNqLZxdr4wS8sBsvWjmKA7jxsCmNYs9qsXRSs73EAlXN_dJlT8zVQwY5DdinEzdrX7T21oXiNu5wGoOpd_l2dTZtPSObPgxV8vch1YLgBvHj_oSXfpgI5Ba2LAFrzzOEEOaO5tnOzv6qqMTxXVw5LDTkHhzj4lnU6g5TM6QrtlrsU-vcn6f5WDl_DiFaYFWNAhRCgVmuGaPOpJLWR_t34Xyz-rrqYyOxKXuXNhVrz7wggpP_nu-GULf29Q5jvHkgbAYee5YnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Je3gfBo-NCIAeh_hKz4fcuJ8oIaXyCXibbXlZIk4VKF3FDBD7dhogX_JpfTWCRptMaoMf8n-scPDhVdYInTRxoJB3Lxsa-Shw_U_J3K6IFE2nrGpuHaMCnwkeyxLofEYNNiCu3UZcopz0GzIbjvllrx8H8vbefzsdghELX6t6N4Ksm5J1YWkEyxkACltKkgrTzvge8u4L20NKQ94w4D8i3OfZIXLGMjOcZexcmGdui4lor84RNorkdbptBDQh50GZ2_zhFKzs1eZgat9tEDBRjEolhd27pL4GyvEeRBJjVg76-1RllVqvSPWLBAjWaaAHuVjSBhvvxKJxYVjBOtYwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6fqiWdJpTWSyFG_gzaBZnBdygPiUYuz-uIOAJMc2TQVfF5s33G2McD4ex5Taf53FCcw2OJshptWKLi5ve5Fnkp1ZZNHZTiu71SeV6ckV27qH4yPY98Z1lgIxNvSqy2-4SSxM3EIlO0ugI4DujLRnCFKsF8X6DjQHF5_GEHRNT1s8X2Ildzhuxw1e566LrwElqqHZbISOGkaIOEfzY7s_hYSP5kqADhzfY71Gm18ZG5YgG5dJhUfGy_HDuGfA_tFDnf-dGbQrIY19-prAcSvxm91RciduVdggrY5kFva2W4r2_mcRDSLSd4dqa1pKDvJcniHh9a8W-g3l6kydv5vOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fBLINYPjNwnvQY3WPc_e1s4Y_IW7bLor4RanO30wxnhx0EwnerzuVoEAk1ntc5wdPTCTUjDx-qqgfQzZb0AYPnoqkcMdVAVVE8OiBOcOCm0-QglUeVEuuRGl8tvbDjGuT4OoKPfhtP4ddJCzErQt050di8k1VjW7VGMkcfaY837dMLiGwB0pJVKG9dHvq4qupEH56a_X754GludPL_UlMUoWe0xfmDxphVlQSFS_b8x4Pi83hAIwU5F6Mawxjx5Ilx5OkD2XrnDUXxvDWEdUnFpRpn_34bwL7RqWfuqKCNc3-BH70SCLAAnvE4vsVv5TDtV0NB3s4gFNVSkcF7oc-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZP7gjztQNJXqgPZIKZYzhyn4MHuqwmG0pmODXphLavdpkUrBm2PomQxGvNldAq5AsFnBxz9Cqr0DtWg6sVKLr_pv78n95QvZOh9B7EWKQuEokVgzANvSFF542FnzOkWdyRx2Gp5OIBwgI5-mex4UJnXWSw0blbF4z7B29SPW5OZzP8ougVnW0riJ6g07qt0Sk8hAQYYXUwMybp_n6uoeCPua-k5T8PbBMXr439gFvxWtAVLmUCbZW1PS-fctg12cQBYj25ax9sg_i5PVK9t1BM1TjnG7_452l24WEEt4YYIbIZOwvZGnoSD1M0SOey_tg50F-1k8ryCLolbmJiJlIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HMBjZBQR5yY1sny_ndPHvdJjKtxrYb7LuZT8QrAvCkXaUk5wt_y933MwYYmfweA8yDz0D6Ea8zln_IUA4TFa4jda13iU5xpvsBjiyjMeBh8edFOKJ1Yl6PPH6YnK3QWjunQc7LQVI13fWUiLSWyJJkREK6JjvmwVmFChqInSlotzaDszJBaPCDL6H4z9MJyX4pXN_G2aHhVrts4rMvsZ1q3xQ29gvj7A0mmkCZtr0KLt-6kCRDAVMw3LjvDlUDxsIr2205pq1dPod64_L95J3z_Tv8PW0w6jbZRFWIFBCo9xKTpR1Tf1csECIPE4Np3kXb-zrODBs45JgcaF3bKJkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvOBUJ2_CiHQp-69H0ShFDhZVtsXT8RRG-X8QoSxJFpOMsRCLdvetdpDkyUXoj1_cBEiqddFRh-MSpDanmeDoMD15o1M6WbRUnOU89qiwwTNKtp1ie78af2WMV-NEMTz2EV895ByGP13I-lxXpaQ7sDQkMy0eAwkzhq0CgmcOSGw9W21x_dxCOJB7ZvtmlXz2KB6XttqEmWMblxNGJiFbumXaosRXjdZUTXMwTbYrMynKUKhuDh3YQ3d5Wmmh8akg9r4_-Kf5Bf93D6VBMebIzUcfU8JMq4307pp_dnwETN0Q9m62JWyVU0QDw0P69WgPPhPMj2LeTLySL97lqGjwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5fJIYdF3-dJfZQLot3SMAroPhbH5ozKCbu7GygFbzeKI88wbtI9ssxbUzh_0BDMLK2oO_pIgQFT1PrbxtWtwQrZQmru0A695406hxzSqMIQ8_EOl2kgc-8CxM7lqrH1L7zE6B-ro1h0WmrysOYyqTParsrxC9jVp0swGwlvhmXphpuyxL36QN-OZOjSu21TN7-rROTJjcpkr6TOTR2ht5UrmXxpr_bE9wH6w8WjaphZ5iw035GcWJNykdng0Gv116uOcT5IfA_av_z9iZAjCRElaKLpBuTKjcjcvmjEr0337zsvu4gQHXWoneArOzUWCIMQPbrmoVsuQeuuu8gB3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sldazMkQcS9bTJvvaF6LePpMzemlhFVpo19AfFRFnkHUhMCVyqKyMiCN-uK6otMUYpaybJj9YmNyFL9K82WcKiyB_46a4HJKhn6-x9VLUXuLdxp13Zq18FDQeZoHMEOpde9K5DXRaEa1QruaIrhF0MLc9DcSMhLUu9naSu_Mz_l1JxbwnLGCNY5DRLrrSNe6lntHpjsA1lRZFL-hp4HdUt1x38Dxng6fW5-r_hhzXwECcVFUM2S0sK1_ge5dZedvLWTqOF4SjUU167MrQHLrB-ZcxVwJ-ob_hI7n19B7PwVA_3XqKK8zsJHEwpxQ0P8s_P-Vpc1BqzHJkzdlUrhJHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ieMM9mXlbj_ISKTr7k86Z-UUqVn2dCjVdHR0P_0agrUqPUpHw8w2b9UKqzhtL_WSi8vUwmV6J1EiPwGzBQ8zvAJAtiiuFxNRdq-qyr-kWPYuLyxmluigrHTm8xHW1UYy6W4_t8W_X8wNeNr5THSP_Kc5nzgxx3dAP8kZHidaa7LN3y8na5zc01Jha8oK1OaKMU8DEdyz4ctHtXARsgFdcluWjl7ElIPJV3cl6fdcWRnEyrEyuWw17RhRHsWtuuJwQjehCXU7Y97V08XrrYHo8gKtmrxDbkniXD_AIolgdnRAaPmILSgwhmzyBpjevU_S-S-BXWTGsX2iFIbvUtJA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TaJx5e66SusYPX4OmDyST0E-Ifp0iQJd5urTRlVqkHu336ZxhIZ_XEVWXKckhAghXvWCc7DteSsY-4wvVKT55ljE8lx7hdLAsqos1b0qjt8VIm5QbEarOrBexCmRdaj7OJ2a30l01nXPoniMAuovkOYrOXaSUjESpbfGaoSkYmX0OvUNbwQLg5jG-Ronp0wyzcLC025Vzuij1c9iABJFoTOVJ6CiLYN5Glre_CMJS0xuEzd0zwND_CHRybydvAeJsOVmxJjQeDTbJ6nFq6weyBgCXNj-6gAs5qrWJ5G3kockZGgJRoTMjVJhFGZfsr7crlkzBrko38eO3y71V4Jdjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uklBrFtW4xDkYMjpNf9ur0WlTHzqRRGrZ5bbfGWSZ_YttPyc3JjaG3x-EvBWTGYP5V0oGS3FZPayv-53V_PV7fYdER9qvM_PsOsB09Et3oyoT0FggpVwum0s9w2RY6WpWMKQ12oaQaN2PoemR7Zow4ZUsT0z8wOrsAC9yd2n__KpeFXcE9HH7qmt2Kc-5bGjXA6la3Kue7dPB02WyU_cs5YpHf7n5F8AAhaFP8Byt5JUwfwJWLZ8zuGHa-RTVS7OTKBhmfQEgVN0dTKeUTR2uP8ubYPTQdXyu3zkLWtNblWyB2ush06c2WZsC5Py6gi7idoi2IPZbOhttJ07jWcBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mP_UdIKp5JU4aEOLogb3ExIRYEtZyYDeY49r2Rg_k9GGqprvqHTtdXupJv4l9lLHSEDifS3855URfrH6HcDlAj08-e7vEM9YASFhgU9fKxbtQcSeGm0bpc7RM0GTEmk5m3mIKg2hMwUWQkfuXW9VHhL-pjsDpO7khpY5217beh88EbmVDCfMM9C2Dd_tO5My7Zd6LqtxY7bhv2gnq4ErMSon01Eq1aFagiDxdnKd2OTklBh2vvoqLMR5uGHCfZDsO3kCIFFazsW5S-wQXrTFEQpnzb3kR7Cc_7-SpdkXFoefZpC_ECox947-iKVTS-gOY8k92Bf04EfSFU0IyPY9vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8wcoYS6bwvF0gb-mch2eSAdQGfOdJfUgu6m91gbyS7ImerEpJnuWSfxK4YbDj4AHqkGaRVOAa760xVDtCeOY_lxlPbSM_4ImsFu_hPhzlk7nUolxCr7h88ABnu0YLcf47ppYNilfznHz9BBFMDyXBfzL2KdvuD0BXoxgHXl-WDvi5mo61Fi5ff8z2BXZPAaI6bUK2IJJP3406LfdSAUl-3cVQplVGVkfEAM1ZJYJD91enBgeS6DN1eFA3UxXGlmiMObIr9SvCrOFAFPUPXc1SGjdZTpkXqxdSlljMNET9peecGz8QVNS3q9OhwMBX9JOvzKdBozgAppQXkCqBSwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_DihSOMrPPJ4ZYH4aSNjI1swzGAMhy_0ni7qcQU3ULJQTUwG_VXZZih8Ihct-gGEh6FpWbOGqe3YD0HLjCNw5XzX73f1mClKfLZAr-ZAqXA-jLKCqgYIhdcCwOZOerkuboE8G0U1NdDrIPSp4mKNCHNbQXXDnwX_q-uBOK740jilgYYCLnanxOx2uSThXldFWRAvwWfwi8KM7dmntI4obu43Bcmqfgj4QMrleImPZwqv5cTtN4skr3rFWsOvaTE3mibGkbmxd_uAnfPVr3kb7LN7qO38Hb_hkmozBAWTbcB4iqPL972ffTKHiQUIhbKkdVtiPtTm_GKPXo0hh0bIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FMb8GUyiDZTGpVbDvfF4zMXLEiB4AXjcHjobv78T1wBlUhMyAscf4-Er9jZozFqs7vCCvHLy9sp9GxARj5C_LciFYvAgHr7MAcSNy5QRJLcjOEmy7tcBf9531fuwtcmERIZeTPzal7QD4vJKudh_ewkDAoQNFeBTULprSGI8SfyZDKYYAqzqxlalaO0JXuHqV-KOYPKND5H6uAzD3tqtAY5AKNQF8fr-8daXaAkX0wIodAfNociDwTOqgUYi8f_x8kd606-yYyd0TKdsYiKHSlcsZ7M0qc6gfpTgvHOFBtWBLdR4ybauoL42ub0ykXCYsQUi7vdrwsBU61mdE-9llQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8sKcQ7jblVM2mbmVHhSJmZ9F2YaPlBFQzNk6Y0jpbCz0nF3OWDV3unLa_Bmwil2KySQBGmLa94OdFNj6APjG-u4D8TKpwe3JXHLscDjYEzkvsttN8w50tvKNtBlDRPB2IebgaMpOecxNFE6dmUdJ8o-K582zMyd2RXDjdQ3UM0rDlwy8ccA4onW0lmb7PB6mmQw_vlcofrpvIt_6rz7XCSWmcRsF_ORrWfDKkDenHPoDsmc1xQtm18eORhqdxF1mmu4F84XTm3TjV4YR1guls3JoHw4bXFwSKRj4Pdiwdos47nmFfvt2VOa_IFbxbBCYqr_MLDeV4C7Yk5PhXaKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jWQBjlicdpUCJD0mZg-FM35BCZ6FlpDg5C6SOo_sv6ODG6UOQYBBjfUjO_rn1QyWY1vGyECrCo8NopX84dLAqgeyyYqrk1USAR-Snh2GhPfrCBVgU_C9U8Uw-6lRyyt_h_ekHX0_7Ip-e9I2XteJu1wZ7epFDIq9OPFqNUbhiV97IitBXFKALuMF2HbtJ08IQN-Z3nwXHGr0QmvZg4zyktFxezWJPy5JEEUNzI7tt34ytRjHbbjngyAwNapl6klTGs9ZfU18VKRM_y3eu2ylIEVlwuOybzn8he2OzFtEjJyHIOQXl22nIG3-Mc2hwYmXYFPKlNU8fbDqU55d1V4Sgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mb7nD9siSboVdDz0FBP-Vhn3Ui2mzxqDPVgWY1ibimGeg8OAk8-3a9HvKROaZOYyqjIObPJwQVlVWKHxFkgmZJWjHuaj0tHimA9YNBxvezNZiM86bY-IjM4mOHr-TO6SyKwAmpOK6GR0Q-XPFGW8xnDtErA_4VXFtyilcI49I67LSBnNuPlDSpih0avlKRoTkxwfeqbSsafYbWlGF4-AyRGbtgtJw8sQa3iyj_lxbCJGmXJZvB8KVrGMpEe8BcPCiUahEqPCCORMxdKqFmv19Zxw27mFS9JF7ZU1z3-tB7B8eTxbW1GA3Ibpbx7N9DLnFMyDc8hD_VRIiDJMZUXW5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/byuvCVqbj1CkAI5FM8GniQMjvm-9MHMWRsYG2eItBZkzz6u6yUPSTKtA4zwIbc2W9R-iaKmywxAAwBq0r0ez3lljbt70ds11LnlP3x0aLDiCp73dqBj6On6asMdUm8usyD4fmH2BXFTo842FDK-qJ448YnGWbEMk4YZqfTolHaLZahfMiGU5bqa6df7Rxwv17XM_gW87fUoqRtl0-CjMHKxhX8WvDTQ2EclyjeAIIK_fI4ap2NDhlJniALMdTWQQyO5sS_0rbRBhiJYCk644c8BE_b4WoPDyG60G-K3sQyKROFKIG6LJbHS3c4Kzobkl9WLDLRONBziJgtbPbssSRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDboCEVpT3ozP1xOuTiE8D-e8eD4HYhZzUGfiUa6n3pshoHMSDhHd9YX5t-gYvXTsn8Uuh0a6Xx1qQwhZZMlrrDWLaGbdjftse0cQpenRBweaTtPbYoRDGaCt1_rLSDGJ3VZWNqLtlw9c88ataN8vScnAAVMDpigXYKgWV8jOzYVou_U7KG0lRlrfkyqfnme7fioe0n1nOwiO7MAhS1ZGDaqPfeJxWiNR8GOw1mihr9top7_aReCDOPhuddUIrjm8BM7mhYVX6vCtoLbbGJQ5Vj45LRwdHfLuQ8Nc5jH5KN3HXCEE12w1HZSqIgg-7Y0GIcbyXXdL8Y8qxv1vBeXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2Y0EMtG6khFIJM2hn4Jg5XZqyG_Hh4JyBl0Uxwtx42Ly50kn13dchE1Yufr6jFz_PA9pDQdDDBuTWYhDHxmRcifDOS-0Gf6Jw5fcLS3DVefBn8tdWhuMpB98U4noCgySVD_B_HMECVr83p2WAIDTTB9adzv1nJ3P8dSwaX6QGRWq1TF0hsJOwgVBXfK351T-BLShdo4G9klywQVCwdLGwXAE1UMzaWEqSQqggh3p9RSkBZslWL16fg0Uboodw_udLQB4mt_OR3qRJHa_xA1fweh8nov4WQ-_zT7QdEaAQJsAdLjRKz2AtpQltbVesC2L2UiG4BKgNyKNa-wIyVSJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tuste6SbT_Vc6eZ3WwsJLvGpXkSKbJdj2r4SJCcJwqGA78hojvzPpPX-jdPhIQVEFkQJ3Ji0VD7tEEOoryDw4us1VBw5DePnTew41hR8p2Y8YHcUDhmZMnK0OLoBSSzIGOi9zIMVb9brP-E7MFDodDUtqxzmLFIXLKUp65G7sqwuobVLE6bSE90sShpL4cB2R8nUyc9Ji2fW239B4rNNwI4uOkmgmKvzaqOnSkSr2Klu35nj45TJZu8cx9o_QI8JSIuy7jGHc2CuC7_b53fZMvQIbUT4BfSgdJRprmWVXTtFUX9PIb9XEZttPuTgdPFr2EiyxidrUzm19Twq7yfQcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qI94PuBTyxmMHgaRyQwhuNAr4YkbVHuwPNp2l6AhnZ_bHHMtUDvWGQp1yKbczBN9R2pUopviL3RZHYiFYy-iJKCjYOKwAQI9btIDxqZBn2YAxp5VZMntyZrEVLPVNy0TZyYNDQwybjXy66bPjal5f7B_lFQvmdfaM44LR8WBNqUiWpU2Q-hpbI5nQAx8WmFLop9x8V8Wt_W_MOVMX1FxrJXufsW3Uwbl4cWJm4vnQC4ODh_rOFpz9wpzwLjpF8W9D8TUqGcxFkEQe_ISMv4J7P6H0naGmU8MP_IIxdfhJzQ8aQx1IqyuU0H5hoaoVJAlOTjGV62KZv4NWFnxTmzr6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uo-lWYoyL83VbTdQ9qsUAP2XumkhHt1u_H0b92AkTsuVLEH9z7myaQpGFKoz01n90BJfX5wFpOHz5pcokOnhNjOWEFncXR2ppEpp4wHQD4XN6XP4ix0pJBk2oJ8jtRe4Tvo5iumQSsCExA4xzx3zQBiNU1HBUrYhk9jYwQAhi42aIsl9WZjPHT4agZWEkTq8hRbL32tqy9DXFV7uWCh3wtRPc-MrS7xudR6yr6mT7Gd63W6FFbSfn0xuS84lGVnaaOd6tOm6w-OYll0TlfqaOG2WePo1lUa3K9VzXtPk_5rn6-lQ7yR5u-DGuDYP01rQjEU87Rn77JTAV43jN4Alkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jO07hMyXlyaqtbQRprNK9CsaZIMbkMD3LUw4IRJLtGRo6x-pIKM6ARQcsKjGAKGIQVahnXEYILyfDN5tz7QtgpMGJuns-K_LGjbl89ya6dTw4LwEkhPl2M_cuG9LuUNsjb_6iDIwZO_chl3XYqIT_4LxdtDSSmF_r0fQrf7atkXdQIaTFYBXdEjDScNfilnx9PjC0Oi_IzVAsm03OxkLP0OG01FH92oBkkgu5L0zsgcz8gZLpPWtjyQv2YCILWv4fX96A4M5Ua4ZmhnYjtVBuLwCjq0tn5ppi1f7zBXuChxGro0Seh0TtkmIbMbq6bsZa3QsrgRvFmqbqrEFKyewMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuknaSsoDWnek6EySTw_cWH7fUcvc89dt1qcnVptUc_nxiDTzi5LG-T425kHJe5akjSqE4LdIIoiEXOG3W_6ygEXcuEDsDZyWdLsn7BRJGLvq9ym8-t-jOeq0oK00LaqjFqPDL-jCmMl_EY2oowrI1dTSoNRxrb4Xt70_UtziiEEpu61HhlMZPNz7H6Ssn-2M_BFUs0XbB0oitDVFbTcuLRXNLl41myfLj8GHCLafu357EYRvcGmc6i4_94Y4iB0lEarW46Q91rnX8iZeOCmwe_4-XWrfdAaZ-UQL5sL8VWpZfjVoqYLW5C8R1zz_nJlhEC3ZhIKmkBa7jp7cywZDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lih_Brr6r4KS8vsNkumvHVlqS7c5IOAAPD_MgNzPRdqS-dOOX_X2vR3S31Tzzncld4vKMDPM4GLdPwpCjBLAfOHkhs8eQgsZriQ8pgC-0S4tb-sObPtjxchoKIChPDbN6UIDegjF5INqmiXjxGyE1QdsTYJyi0SDWPlYgk7wIs0_u4gL3qPHBFJU-pVLcQNXbc1O4YJ5CNQF-wNeB7XMnlKvQ6EiI_2frv6uCO9cfJOuOdzbsGfN5UGzcIONhqP5g5bxcv5-wF5srMSPPnODwjF7OAwNcvmBZ1kugukaMJSvv0TbonNBXaSo9T9PvEUKaOHb4KkDokqiSnXIc-NW0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kit1VpqWuGtDTaecZTUG24pi0wxeAjJALCR2jI2IAb2h33WITzDCvYPnerNMBZfrDybyZ_q7EYlQAkwEcc8pF-e8eFOayPGAf1_tYCdiWbxbXsQ4iA7TjxRiIQbR2uN305yIOq2Y5ZMsTaLq5M4ekyOxPOitPhccmlTg49w6KBRrur3ucMKSMl8Py1nlP4tI5ss-vUX1g7-w6Qp8gW8EOfNnekjsoMdIK-hclnZbgzGqwVZBXPeoDKXfO7C4MAwygyjmS6nJumTL4BddxXZ4L9KJ_jIge2G0PKRcFLvZd493EiSbJ7bw_GLq8I-F50uD8JiPemDeYM0L6VdhnRVDnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tgWfDtFkyem9d18XWz_sW3ihtc-bgzktSZ_fzUy6C408IdhYsVqiSiHlJmbXCbOLV-L8V7uZ93GGa4_0GpF2ief2HDLCteAqQ73fOdt1cODK38tfyKzwUJXIHhIlbUJ5n-iECnStMHUIuQuNljq-gL9PgoKue7VFpRiclIKdCVpEXTq18XxDC4eycZ1G1_EBX5hXob7sHS2-uWKgQ94wSmGJ1guMGlRJrbd9we15nCybAKfWjq-uAc1EvseZzEocl8xjMJeC6enCfQEPRYK9jETIvlfuXKco_cB11CNOwpKWL0iXfOp7Eu5Qfel3zigNfEOiadOCNSoFZVVpetM2oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aGDzU9yMfy9a4YoQxAkIOvU6JrIqFzWwll0BJvWzipzrcBkKufIzVKiEtQ8ZmMn0k_X8HxXJ68vGw2sdo5puTAbn2QX3l5nnh9Yl6NqV8Wl_Z8Q91ZQo1T4LmaquwczXvjCYLmqLFwTmOMILjckQKLpxNRpvS7Os-L9xg-NYSjgNHo5zYSS0NSkvZqVgBB8xx8j7zYT6JKMoVosvnWTw9NsQRdkNY-pBz0MSf1Ti95-4AKYlVtum74Dj8ePsHAhvxbRyWjypa7eKiAqQFK-gXA3oLhVYOk_H7gDGhUTsqwXmVNQbZrCevp903-bBECry3Bgnj1OXMngjcnGbQXZKZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXB13VAFDQz8BzsS48xtJOg0juJp5htzkSbOWTEe97SISzEOdpDt_uVFJ5R6mTTSoJBTcdm6pwFkYCk2MXbEU8VacW9enjtCvU3QM-gCbub284hP1qfBAUWeFjv7nIzRygXAZfD0JAtX9t0pZQb-zPXVD93INjLTXWjIgBb6zXHxs9pzaeIT4dJgUmMqvfE-XzP958k5LoWtYKVGovEHa3c5F6BusKwObYv1fg3RaGxopGRm0tD35mnEILQXvTxKyo981nAEiu6LJQ1y4RdFSU1Apf58X-JxukVq_qgrxYYlTRf6o4XlgzhdXB8rT-Mvkvr35PNo5DVIRjQLp0XW5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tmt1WSYC1klgCod48aBcOxdoZPOHungcqiWNFiuc-UYUTIEMc83EJeZP4RaRl-C2V0CJKFHfr3mBRvjFsR9K-S1mkNnstk4PsK7MT6jh4AxISzKUnqV5G5tYzahCHEji9qglPdx52eD83wynCXi2yUl5Y9TpLv9WAfiEA7Ms4tZKRuMuM-xc57Mk1XE_0gc0jE0iuDypgHX6IqqEiDPi7xj2MrhNsi9eNaQz41Pm7kFjVJQFkTRuHMwd-HS1jpDtMss7cPSarSYNvkD8bobjTR1-aUSjgnPzHGCIWlBQ8oenXbSIdlE9A0t2Fsma2r-dS2MCpramdYaR9CdjCP9iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZILEtSrdqh5H6XqRORugzFVUKtUjhFKIjv6Yy-IvlLuy8aeOZWLob9yvdESmZE_ZRpp-UmHzn-95jrx93XbeCUsWYx_po3zTOFKKLWbwzrcdAsR_uITSwcdumEtj4OwrigMDOlenbuwJk9Bxnbpfneqsg9FBdnPwsXt891HRRMjckK8YdeUnjcYRkT5PX-3RaNlRcQLulGD7JENgCXvGNpd0GcI3zXHR5tFoT5v12r_GR_VPFrUn0pHqp-8RF5bZWOU8xf3ms5UEElBk7fXMBNBrK4Z3T7fcRRZTgGV3_6TuezFVxHoeRqbug3tAvu2kDQqtX7gzy94gXftZHHvwQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYb1eLLqas3s3SgsSbnk-3yNkCytdKxfbmON66Ga03fvByaQed0ul3pTnQc9_nO8S_EYfDTA_n7fluJyj-dSiIQJwaXu81jaqMGm3ot4ewR9cEdqDKn448_SWIu00LVOnidTLT3PTrQVjJdw3D7PXdTF37hmJXRAxuDFRh7WPS-Skf7ohvPBZ2ZQFAsJcgasfMxihAneeMnS7Efg1BZmHpAZgnZfUte4LwvgAQZ9bIc782nt1nZoGiHe69C1it1tLr_EoWtaXqlLAs2lagUyfRSOCvGP3NV5aLmAWY8GVlVqMtwJ9jAye4l3otw3MZjdDVKzujQqM20V0l7LFZekUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WuWLDYFj_hGnUwxXwxRbFN0TzTFdvbcmkQy39iTE4JB6jQqxGgIBb2IekQSsESmZQwzQRkf31X-2EYTpp9NZoHspDS94dDWLxsVCJxtqBIgrSWJmMeJgMNhfz0aT-AIvvNQxJ1Nfk_TDSQd71rNfXVusPNGdj2h13KRn6FDvnbZSGTxTWokraajQyF4qnHHbemrUVpi59PsceR149I7fPrnm1ftqUt6U01ApjExecr1xEFz6DX4uL20b5G9lMAIKE6vS8fKn-HPCkU2Umv1hm83aohIPa2xWg7RQGciC-u8MiG8uSr2aXjspGASx-4UzD86Rf7m8uAGunVZg-imtcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4BMp1o-XrT2xZOM6svl3oKZFlC_FmZ1RgrcrkBon8BWH_mqSknc1ogvncLXkqrhr2ce1RIx4GVNt8d8E6Ggr9qxNR0pw-OWTUpawmgjMgZs3Vh_p0_xd3b_Dems-QVigsFDYTiPi3SedJMWKQVruEeKRTDzg-UpEqqG_Za49s6DzGVnkyFi0y2NMwo3U9ZF6ZW7PuNvVSFyA7f9hzQpXHONhe9D8UPw7XDc3ZHUrPQJqffsgdskrhOR6kki8Qk8nto6lHj_w88_SfrnV-Ff7LkbYhcVDNlMxdUA6v1nsV1MgmFfBrPhtcKhWvTHwYCR1-TwScnhUT2e1VvOZjfHzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sETnE2CDanrpXUDAT2HD7oE20wH1EjLfrosDmom8jFCdETNzRJuPLWYl3vzo0UfGPm_o2eAwjepW-cSeQFM0mNxlAzrsgiOuIcPmSVQkxHmVsznnuA6tyZLpdcIpbpiBoc29NeprqxxZUWr_GPAvQHIBwTHADWH6cDRtlSJ2V7YsNRP5LYRtDokySfGvAMpjW_qjH4eFrWyRaLzo1KZ-cWxpbWCRpTVjBkDvrKxlqDnv-bfYnwWYNuZWn8kHvsEEoO1J4pejl2h9QrCw6tkcl47G3965s9an1zUAkylDPitovqWulcznq76NfFqxxlex7A7UUeXgl8zI7aFyoK7H-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfzY9qHt4ht3ULqiNREZaxKi3TpKN6s8r0xNvkRoF-B3mfPvsu8ko4Je1HafbPKkO-MK2V9jHwcNnLdsFYMKcOYGpMrFWpFNMiNAznTiEzHIO5XsELVKvPwJkJvlxFjkF1-BUrx8ZzKG_j1tMyotJb58b8oe53sh-aUJCgTz9NczKcsbqU_iv1yAoUZX0Q_41IiHi5l4SmVXruBEeVBzsPdxXG0oDRzq8j2datkHTzf8nGqD9iXj6EPWwa_wmAQVx1kde9PFdArKIIvNb2B9sYPx_1fA0iZl8nsFBwQYvrHBEububowIPk2Xak8GB3APO34ayOOUngLocY1JiAkg1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NMgi6cTooGIXnsuCx4Hhg3mSgqakEiHvwqu_HtxxGjLsop7dKIBzpH-HMhaLkrF8MuwqqxuS7-GSmLgAWn4fpT6l3E1W856-c6YoFx3TnT_FULws3qo4wkzzoCQus3gN3hncYjgzkiN39NRTm0l_FpUlZHuCQdjENAVoUC9AF0bK8ph7_WNRHUSYRMEQ6ZSisVvs2_5zMx1Jjgu-51Xw60GIMIGtYnoaphGBHX6HX17ygWbyskzkgOCK1CHXw9M63iR1lHXH4dwavepMeakDBJmsn1gMDoKRbD9C1D0lz9FKPByhE3pLORLPR-59Htmx8zUjUAge58NTg3q7VidRGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RNaNR9tc-sVPJ1WFDgFRkcbGZMu61DTMBB9hc_sdPLvRc0oaSJhe-4o_Qg5GgeB33ZFp5dWCBA_2SpJwcQRZ6-XfwNGvbNb1OUs4AHRNIRytXOmiAN6JdzydhUg6o11bCoEo2j90kphkOXFNwWrj2O5UhbeQL5qbDL0w4Qb_foa53z-2Y9B_JaiOqIfZlngd2cF5qHSBNQWn4qpOmMu_JEzFMYbVZMtFQmcGlViY_le6UHdYD625WrG0H-CysHDaQZOxPDsoMWV5hXUREvZ77v5ARTfQ5Y-qnxrmW18GJA93nmQhGKkoTRFLAQaUBOVt5uc7KsGppQOKM2gHzVNvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6rVHv0jqjbwu-XgPRI8gNfLPeQZxVrx6OhGv3_iJterW1cNEsTAj7NZ1L_L-TTKT7xB-sIcBnu1DmiGRGKWL1saAc6-4RlOl7PBu5Jz31xV_rgGIU3qyjAsTeGEIsE5FW5Wq9QFfSCSFPV6jiF4rEJQ00U-6Ei1Yi4OseVETZuD5LCCah_-Ya1MgeEjbqbG6SbmyWads3ciYqSqNVduwTk5PjfvTrnkkZ2bX3MCj3ytu25QMP9NkjZCWj20Flps5D1ZWKRk8KKxPVinRVVtWLLMQ7sQ5hfLVmeUAuw7ONF9oeZr8Zp3RTZcJmz4wIzXMTPYxDu08Fmrjjub95TzFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtDkI7_XbT0Mf5EWkScl13K-ZzWX_KZ73o2663n4ugvh6nvOzImsEWy6sn2PUPtDI2UhYGbr7QYSIvJdwEcV1fX3jQdWALvl0mkNBAfmwXpLtrSou4jBq3XBhZuODImEkI0vywfLjKXGJBZGMvMlISVEgMGzeqWlAJZr7F4hk5919nD7jnAP5b45yEo7KytUh92d1uoWk9hcJ_kAc016iCPX_BVPNl4W82ewiwCzcltm_HVA_X03rhfOk3sF8SGl0gmw1-Z1wK9GIasSo3q-0ROBnzqOfojIQzmtpBbF4qCeON4Z7vDpJhDcL1TiOA2a3RJMwr3vpTQFF-S7UGQb1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVrPaAW07zT-NvD8XJyKpfV2u17f_E6RyU1LJpw9JtHRbmRPrcvHJBldeLZ6_DQ8FJpmHVhZ0B3BJ2ar-AF6AIGZSFEF3b5LtOCYpUFow0mooDXvLrMGoGxZgJzet1WYG2YLQ3krGUm5t-zkJ1kOurGzE6J4kH5UeVfOiEcdiGRPrr3jKTdhQjqCeBwRLNMSds5snJD70RcZo_bqRhmz6WDh6hNO073JBlnfjkIx7I2I6V7R2FxJLijQn1HjO424WhQurWtDXzJEfIzjw6O0XRl0BuengqMYRoBTfOYzq1_Fhv2i99EkMJUc3hPZC5EfX-zglQtBNXQfUjHB79mNdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SUn_Tp7qSweJRHTNGVIxIQofpUCzU3xRBdDou3QGqriYFZD_4mrDeSm4FM1SFuSBhWdvQGHbPFGnwbUscUZNKR2_AB7z4yL0WJg4TpsFYVQ-j3zDTCjo8SCi4xHLKGCo2755lh2xRSWlJC5hiXJLVRMH2RlXehoay6SwetfkhwXxgszzxrxvSXftFcts9eMaLrrm29YUXLta5Yyhxc1hdIVzu03yoVe2SDw7uD0Xm1DEUP0qYsd1wx8t5kWrBbVfiTMJiD7UQd9VSympKVUWO9FLQpZVBs3YncQOv_M8aQNT3WWAykhocbe3156dYDgsSGTmAyz-i2zUS6iJIxyM5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKg49Jmz592txSVFH1T3X6ThSuq--jRAxTNAyKtU_ZYGa1aHt_hCxPvCU3-pPHCyEOIqyPDOFEQ1kAApsuM8lmSXH29vQzx4w8soz24idjnnqdjuMWE7yZy2hZeZ_2wuBXIxZZfcDpZA8rCOl-c7mJRTYCuLCXVZT9QCmW3m6Vc9PNLSYG9RCn5OFE0tQD61wA0cJu5CSU6Xi0PcxTQ4Ff3ULsnwzbwaQV2Kds5ch7RDKSCa23_AAecFtsyHn54Hlr8fvSRMNmEsZ-bA6t3DfH1bezL59Xl8G1-mWt3lPAvXC3r5vtC4CZ1FJsHFKK8JIThaN1vhR5i1xa_c7W_GCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mM2fIFM0hVA7SHDvrcgkK8d2CXAw-TbCZDTSI-WCA4yv6fn7MALcHQ4NRw14Wg2QP-wxwZYMOBXLs6hkJ6PETW6IH1fENBeUT9gwNSpuesluX6QkuF7HjQvvw0D2irFq1m-0U65Y9WqgAPMURniouDbUY0B0DEmPmGyIlwGDcALshiRBYk4YSIQGkYgbeozdORpKVmjQ46lU8feXvrOa_NjRZOrtdmzCpiZY7L5-HbkLjzJ6XADZDmtDBWEAzGwztf9O5zdVvCgn5zlvFEzhW9eoUR3RXFZ_AY2XZGPdGrOzau53EOKLijDV7t-2Sp3GVxHKjRivw2c4nxS3ezlFoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gm0Ojlr0_WZTKGCQ-ICGFajfJbXcJajIVNFl1mvr8ZW__qhpA_lH_jB_aqmTgV17xzrYaihlrYSs72Aa_613E-CWby8K8YxzLPiMyRjLkkr9vYViK8JKLNF-zzvw7Oy_kuzbi9nHuIfEZwDTRYIj2SyRG9UBzusChSnzQzp-zICwaEkWk4lC0VnSoYKJkNznwAY-ZVpn9bZUh9N_j-_gP-c0oFHHfziLzvYeSeaR0-HjQvfb8iHP3JJgVTTTfjIi1s2GnIVtiWfBe6yB5e4Li0mEXccyupdE1hddaFVpq6AtFykycpcZYsYYMY9q3smEKf3_lESBxgDwfKMPlNJH0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ssaCsbJR1bWAT3r7s2KnWP6gEeZS4KDByzSwYZVZSZ9LliT1X24mJHx5c8bZKg86xhR8RF3oEaQcXrQ4KGB864YnSwR0QYYRmbKJnhxrtPuHtfryh5z_qwFBaCyoFRdHMuanbgPDaD834mL5fDOVFS_Ybk0anqLJ-wrWXdnKPYTSRDePry1nc5R1ChKsIEqU4-ITv4PC7-qoP8w1_0qCDO5xmuQnbXU4_DPY1odhAxIasO-VfeixL1T90O3VfT0BEn5jNjmLLUcBPFbvgjNBr_EzAo8ZqIuQ2y8nj6xhT7tiZ09lr6a3m3HGM__o0wcHMVY1SthzAGRM4FkJqanVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ssaCsbJR1bWAT3r7s2KnWP6gEeZS4KDByzSwYZVZSZ9LliT1X24mJHx5c8bZKg86xhR8RF3oEaQcXrQ4KGB864YnSwR0QYYRmbKJnhxrtPuHtfryh5z_qwFBaCyoFRdHMuanbgPDaD834mL5fDOVFS_Ybk0anqLJ-wrWXdnKPYTSRDePry1nc5R1ChKsIEqU4-ITv4PC7-qoP8w1_0qCDO5xmuQnbXU4_DPY1odhAxIasO-VfeixL1T90O3VfT0BEn5jNjmLLUcBPFbvgjNBr_EzAo8ZqIuQ2y8nj6xhT7tiZ09lr6a3m3HGM__o0wcHMVY1SthzAGRM4FkJqanVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5DzzT3Iw9S4d_JeQl57qLXZFTKM5QypkITDYSP1ghuGiGcebH10VJ_Yh281HhEJJ1o-_Ja8Hkf3xVmLV5eScUx038B7bkXRGZPk0kp6wNWCrvQizH9znXyNPlecjGyuVzRPqp8LuKCbWimjaH9jr7WVMhkPsMo0HaJ10Y9a1opmR1wdEHpVrvxC0YdoKKzdiN5ZwwP_8XabNpX9xp0fni2owiH95_00CeqSMygamP7dMMb9cnSto_gxkAIIvhsICceYc0DQj-H5mlW1jB0GjJfGplSz6ARtEplmCLfducVsJkn-DTI2vodqtu6RuL_nmUKGVib3HwVb0Pcsy2ba2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILhAu8m92Pt0vlqNEhAHUD_OGZmwRsuEGAblGO48M4t63Bh9122b-6kVGLgoap7-DztYwpWYAYc7S-GHosqpyrEjGJ1CVPV33ryLJ1fsS7l3e2M1XmAmH5U9_9J9HAkRSurF__lzuRkx9WwXjVOWXtc1EnP7aLG0_x4kpwcday8U4Y-OwwIsyf2__dhKHooSQC6y5orJ826cdrDk79_QTVtbLNaBRAKR_OsMJzM6KOtawfuUsVmMSd36PLG8ZBHyN3jvfF9QnetPZrZxLcjlsoDdQ1b-lbmWQXZd4nhx8ea8fv1DgF-MABU1R5ipRabU2EdJ88y0qIvMrlVOMNfQyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhJ5uVYYTD2bIs2p0jb4laQWlSSrFMn4tVHk_WDZV7Nrqcu-Nsvh8jsrO7PRwBJuRNv-tUb6ZUJ8g_G4kSQ2MVExtfduWbzeEq-bpb_U6jyi_fz-Y6uOIxdmXi1PAm0p2whKO0e4w0N2eGfsXRJRpvzkY2GPgaf_v4jW1nZ5GOerdKKiRQ4Chgq49jMJRtqHvCMGTJk6T40MN3wmwaA3roYcwaE8Ln8vFnJn95_jnNyn30tERVXalm25gfILk5IEd8DhV7ukWXGK1yAQPeEEmfsM-GrmotC29PuqEJ9UyAnfuk55aTtxkXDEjacUhO3yvvQhwMBwvjf_AdzG2X4nPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iEFAfZJAl9Uek-wvSRMc-A4YjmBRuA5T9pZp9uKO3lA-az6hgZjruQRR9ZgpBMSvU2G_NrwgM0Yx459o4Q8CYVCpxPYonrfftmEAWTg8R0ckw2JoX2xnGl9geLWdkSMQgwc_1Shlt7waleQxn5MJrfvqDrV1juDubyh_O28w6LlQYOMzyMHnZ00XfaD4upf5tLrrV5XPTlBE1bl8yNsBKynhFt_870pZCQq7bvpsQZWPvWpv6-CFzIJYZK7VU6kjS0BrGzL_vmTdk9ey6SRWdbI7QZuH2rOE7EYgmphVWMYhMHVYmpN-7JGGVC4kynpodKLQ7-WqgooTDeZm4g3frQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iI2aHeCv860ymQZd2DNPPovRLAGQzz9YQe5hXZ1bY_0J_CoCwuzim4sM5nxTKUwjCsNQBF0oJ3OPfl9S9JfHwY0SQZelFAubB_5NDderGxIfN2Wh8LPCbiD8lLdMhcSmxelM1P4Un_qThefrXzyZmHIOgDjhUE2KSCt-4Gycnbp6oKFSUbxRJiWFsJDqZTZ6WokP4GDEe4DTnEcV3ina1QbBw_rD94RtP8KEvJQjkir03Bjht_bfVlTyB8kWd2pE-e9FHxyvVhQzzvnWYKnos-eEhC0XMjuwG6Y2_fR7uIM98En0YLkw6W3qLO8x6zKhQbGy_bbzpEmx6L-mZXKoSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-H6j5aJXAdzgUqaqZ42fOO30Cf5tsVs2ZnZUxwN2RVZ5ZHUxvfmnasNR3LRsZxwOc083OPU7l4Q24IhTocJwcVbr3m88oDOUhdrElnUHHt4C5cQvoC_Wyqo-Xm4TAWHA23jCZiwOqDxSUzU0QhC_799J1oSY_9P7UXVvnciSDzhF6EZrmw-0Tme5f9mSrifhTgHTO3B5iqNM6IazMWgkLTTZH1DxIDCk11py_jGuv_8C8d_VSnJhUSRlUkF_69DdoDbXi8Oj5Iu9xwxNA6bYwBXCdI_NyKHxRrYWhXQJDe_KGi24oYDTdSxuDgvTWcU1uZIM-5IIo4K-2REN1QTQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPef_KTMdiC9sY7dC2CGzVBeroLPjG0DnRjw-Uik_VAsshiPMaCXcofC0-c0dqxHyd_juUOcJRI6wporC3WtYNiqxN3FarChbNjgHpZphniMt_sYJnSh3W5vaet_UTXyO96UN1rjIyqbn87dQ-rZTJOVq1NYtqpa5L0uLDTrGkAhrwSNB6IMSXBv0OvVko8yWg1ZO0NQtN5t1O53_qIcCkFD3u8t03FJBYS12kM2TwuENUywoUq0SGap9DoaBcZyKKcuMuWIqwx6IvON44tEdo7rs0Blfg0ds0psL5-9POXieYn_p2W7wi_WPQfIuYn-wRJG4v94QQxJs8IEXEO2-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pPK3z811jgorPrLXshrRJ_d-B8MWlT2XTUUlCpumrQdiPHb23xcn-JZpJzdSFZSAWr2BYyoLUdNvcGqeW0QEsxHS78rKD427iv3hRkodiH6DZk1iSOZ-aJWwIO_emhoAp3eQp7k32j4T2croBvjwIo_OPyWeHuc0E6sP4I-1zldJh9ENARe6bM6dDZWmkQX3ZAclRfs5A10FJG4b7uMcOLInbNTQGSKGjrlW08xUasoAHLWBHo69d0WyenOzjieT5_5RLyvk2RPOwbx9dT4CmGoFKypbVsWC1N62gLALEqv_zS3iBZxahXJAgXjbezHzL7wfqz8tjzr5SeQvIcHhfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y27e0bbkGhygsV0ao7gjDZ-StEiqKy302ZI68t97Zs_SjbJ3DyYgIgsLROyJiL-88kbw-BrSI_Eydsw9gSXJggL-ULVkHGe2QopG5hFLEPic1np3GWnC90NcFfRh1FMMBWd7e2guFM8a-nbBTL0vY9BRC60rIi1zNa22ck7lFbKvtQ7O4VXkbdD2tflmxDVBkgrrd04AyjqDVOSeLuhNH-FPqY65gnAaonsvS8kbctCa1fbj16Rcy7_40uf5z2jFLlrfijSWnp4tFTKodDCylAPoWrw0zQ7yF0r2OWqskOeVsme_oY00wog-ETrdZr4Ibn7WMI6cHqdtdg8BjnGPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nssbYY8KcRlCXKH7wy7VAxTF4jf2fQLnQK4Aziw5K8BQ9kotd1wA2mQKPS94InERnWttFmN-zw3aTEay2XrgC2cgZvchO1ajhYdXoWcBlIlvvFMLaL6ZRN83u7v2hIp5QC6II1R3a3B9VzsVPNX5tmo0UCuCvfL8v8xVOjtMO1yXqAYF3e5O9CjBevWLK33RORBzG6wdyR1meUbr4AqGx7ta1CQ7rbnhFPkASxvvX70rAhFM3FKfjcey0j9GqNJIdAI8jkhT9xQGk-XvCtMQIJL2whl9f2r4mnM1qQFhqmAwoWzyhNmbcmLNPs8lp2pr4heoW61jt8Ct0SNZuJTr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbW_WsV2ibkNMX64HQNoHVHdv2-X1zKyfsGR-e_OClK24vdEF30vmFQvfrrbHGzacLmWJzVWS_yypp9qOsOBmiFe01t6uYdZ_rf_nzJ1XyQVRisceOCwREgwwuhgXV1PRg76yxTjCOzjIkpBqgnYnMvNJ5rUpEnxfhYpWbuPx-WDPFm_heaI0iE29ZfCk6ZKSmupyUPOG9DYWQ6LVypVE2LwgZ01Y6OxIxgll8aAsTlQ-zXPtmKF03k4d34sM5E4-fRoxe05YgSXWdeiUL2E-L_5f0GmShcJhoP1BHA9m9OR-w36XvZLQdqHtvK3hKaOVa28nUdPc086-OBJvIm3Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQZ0TJYlvfURUk3dgRXwoH5jaqw8eYxhExbLLBi8iWiK8TfhALjXJTT6dBsTih7nOfwYfH5h_Qscl0Fg5ocZgIvB2kj5Xr7-ZO877VNDiod9VJbsR415mItwTvs5mFg1r4PPc5lXnSyJbv7IvjYrqxFfywvlZvrsHq29263bRl4t2x809r9kXyZP6Mp35H3oX1SXQ4IaNDIh-PiAa1f5CrUSCCkf9zqkhmBDMFDp7VaiUk-00mbr8BpsGuL0AXpiLBoouSFlmHgnp0BrdUta7ABB99UOsR9lBHUjRL8BCrrbGAiXO5gOuiPj_Tac3BFsKnSH0XQnTMbsfDEn2PMCUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjQQsNyQVJe5YI6RO3DrgSLRBddZyxHh4iGkeFng0QlWD5uLyqLXgvpRuGktyjbxVRnBUdVdvmS-q25kQnE_yUKoWR8UudFqVP9Hoj8BUkgAUdtdUB2VYiMKcjd4fscxhQb4oKK63TamOHdo6RUx5s2Ilv4QgzMZBiUNU9z9azwaadoBPhTGHPWNWr7ExaBfgScFJ_53GjsXucFlELwKsD1_MUnZ1d3SGM8OEppUfvlE6lQDLFdPv6HSopSSCzhcoEwtYynEwqmZc9T84sxu9p6LVZV-QuOuWGVkU8vL0qdMmWMoCKFyx1b8R8-kEWDFQuPKcjj1egIvo83BUV45Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHxfRwyEdT5SP9-IpojpX4BMR1EPjCGUbqfrnma_6zFfzzF3hBy8MKlD-UOJnS5lICSTHFmhzaW79f58CMznNgC3PyWGKErU0adkyydlh-yw7PI-kCm0QDFRDc58sLd6TcOoCAsw_7ugFCd63e-pLVxdESHbvncBPtv2UaDU0T335ubBSZBG5kxF3As3ZI5AoJC1jAYR3ix6yGG_RTQaKkRUsD3rjNJeV8htgnQU1S7ZOOVqrJggCjY6Kkps68gq1kxMtkaUJXkBbcHPRff6qPJI-hmhazaSRCHxyfnN2jq68TP1cvHcFSCN1nX_bptxc5Jeo4u-oot8k3FurwMZLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kBhJaL-o8-1jkgtp4f0Ke0-Wgh4uoh8pS3NSpHzaMjC9yuQjy53t244f4b4L4DkHs3smCReDF9h34YMXO3VF8XR02HMJxe09nNAJ9AHNcG2C626A0nZBGTd0VMBOlbUwE8OdOe0Hevi3i5bE87REmyCjoy7xBrTa4Fb95IVxFMUza1H_IpFg_JjrQemKeYhSwwo0GV3NHTzpXEtlnEDXUHr0LPwdhWKWl94v_5ktjjLBc4Ph_GB53f8cCX3C5Q5e9qRDk8ZLcbBXg2Dt7_tcTUfbSeUxWEpGEzfhtHOQvYx7oaHyqHtUwA4JwTJlnDcH5nhCiKpEQtRqCeyzmRzy0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ceqOPTNnswvFtbTRKgJfb406WveIZLeFAq8b8IsISLz6SzyIKgi2amW5fU_dLsSp-IPt8pf330IicWQy2D92EzQaFh7bCQ_nKw8_5rHxDWYGIu__dssIjciuPLq4MpXgLbJHKeUEHSBwIXkwsuYHwe8Cy1j1AEGwEqduuI0BS3deAZcigLmEWJMNyg-1ujaDVkKKv8oTpee5TcJ8eUJD95tX4DaWWrRV-uxg-ihGDbU-weQ_jnefFCSfpHtBAWgYmboAdQhQPkX7N3KWAbtwqtQyxBfBHH4fGoGEEf-P6hl0XIRi04HDr3CU9uIzy3jjAN5xdx7lNvLXsEgl0Iotmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jv4dYW1yTX8lP0Mqq9zvDqCYgnHLaJKPHi2iqqaZ_2ksB05IHbC-12CLFsFzt2R2WGE6WNTHfgRzBMV_hfvPX3EQyxRW-PDDZq-FDWYZ6C2B2GVNqjrDQ05RKkXWL1gxdioJq9O_KQMNth7zwxOFzuDTQEkAyD7oDe0DEIgMrjzv_4l416S-5P9t79VlviLlebbHtMIAop29hJc_tfxkVkDfm8LChpkvBgA1-aC5AR10pTGt3On_WZ1N28cysIDLhhdwBx90WsIstUm6I9ZQmx-UwvTKPhCEnqff-SqYdEu0eqSn3VS28xR4g2Y6vqBskc5EfVimPhc0W5jcDh2fqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxTuUTyEMjbAOZHMPHz9KhuIESaG82_zW3MGV6ucOP3gcy7xI3CnykyIhXPxoa3PZ-hKoZzXd0vbtRHaxVxlNqZ31b-uEbbEOvG4dqKuZfeNsD-05hDY9oVcqE_H01MW1yiTNKcNEGOXdBFqzctcDaTajnkLhV4cR8Bf1TCf59Ch-IihBX_Z5Xm6XmQntDOft8791Q92dqmzHaz4VqALRLcg5KtucHrl0SGJ-BkthxB0q212DufL3_BbCvWkx_1CKBe3-z_O9vT3v4PVgeiBT6ixJq85ufI_4mhEwj0KB6R73xSskjvKL5hbNt8W_3pPXrqeI10w6TwNDYEsywkOww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W3NeCNQVtKL0BViX9d1a_K38cfyTOnG2q0QOD6cJbRPZUhqW7REQjar9M7MEo7rU4PpVHHT14N0T2xLMLAer3iANMlCCr43KsFGuqCodG2UU7REq_xIYLwTqhKJpOQf2IBf9DXroqcICao7qX9V8rnFrH2hxUFSNkSTdRdMNu6p7-homDntsJHmfAyuq-5fq5PVTnAzQ8mbg2Ehcy-T_VhuEN6Y2lLLvzhNi25DACct_Z6apRV10WmnHa8gG67jfFDVCN0hhmln3-KuAyT6VSfxAzlSg_cEg8NYDDk9Zte_DLOPaymDSrZnDciKY0SZfvdMoRCCLUprS2AIwGq71vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D50mnlpMYYNBZTuoUbJi6x2JjhtPwuw28Nfr1flCCe6l41Hk1omEsE24NfD00h382yyM_R4RAuAoiu5ZzEdliHMalSBH1myQPd_2it5V2EQ1tCKc0hHMxwx9pS-FZc49pCSguvgbJ-8UIV3QaHqz05Agc0Yk4bCeYYJtY_hyIPOdc8Nuzd9WmZaXFcKCy0rC78ImWOWh8YFYS7GR4__oq6vmwWCZFKfbAXqxD1uilRpD7MJR0v_zqpMOY8dwuP4AHtWl0DTlz_352CNGAJdPvjATvYDrBzSQp0vTEeKWqRjGR10BL60xKglGJlw6Uu0213vfOEPBEL0upHUMdt-Osw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WtQHGg5qT4KzH1zE7SYCnsFsClA_hSt3G7kAVTVdpUXOFLUCAbPylJDB3OhtxbR-UP2iLyQ_njJ0_NiDNvmr06CwM-AzupZh6Pl9Ej-cV3jfJhQzSvrRTB8PaX_y8Cd-64PDrnbOIVZmKH4lNjxo6uE98HPDQB-Uqgiv-DjtyfSiY7dR2zFYRZg4-wYF-SVwysOHDvL94C-rKIU8zJyesOFVGaY5bR7lBAFuMI8MHJPGt3KQ1wnKC-OCY6SAlIXFqfe75VVHY_FZQORl-47v2N6HmAt9Mnu_sOvIN0zcWZiAeLMzMN-dni7kN5l-We7HTJABek_a0NwpJ3zTyjAzrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzxXFdWT-y8t2plAYTZ8sTDelbEKYrcDxmIxuGZAkMNeUJ3U4EDI8A6XDXal-3c_qX-1JFJYcRxJjB2_GR-8tp3gPQlMZl3AivqdQRQN1ZjbgEwIT18vGFwq4PmKN9yYqI8E_4BXyH998uTpSmUFxkQPmadHmtX1c9PTeukrqx-YfqZh82u4JaB3-AKF_Ou9xAMkZ6tdDJ9t4my7LQQzxwfdoRyt8dB3LWC8sV-85ddLQtb61__Hz5oQ_cLfNInfRt17pCLb59uYbfR769S4e0clAtuAlM2jIYqwzYZbhVugwlNjFivRjdYLX4CKYBBmMpKLsDgy-5m2AzfkDpKxmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rh4TgQaiiYR6GhXxVcQr6V-qY2GMGdg7FoFk1mByEs-BsfDFWKCQ7PDGbKtIkDuE5rO3IVdP-PUKpF74Xeukr752FKtk9_k5S6gysUPutTzvG2ZoaikauJJVBX_jorWCiP40vZEreWRGx05wtooEf4qwP6shO85hSQGgjpZmcYzfOozNqko_KD4tp-ppaNQdL7leVahEfKqES4DqTxnR-IL-uo528W8MJ7IP2imDw9-27bJpAibVvXSj4d4CTXULLqNnJXNxp430qxjJd5FsKZgt6DFeJ_5Aj7oi0lfd7s9_VZ2TBnf9FmojFEYNDc7fGn5B58NzM_G0cjlbXoBJ-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVX3cgtNa5WNPz3pdwnXzMantsF2nyB8bEhklaGjf_xA6ps9soNZq64a0EfCRaRYvSqspOL2FS4PachHLX9Q2bzrquqiWVI8npLwrVfbBJy9PriVsDfAFZZJsACW5tO13rufCQhspkSSUTZtmoTelEdppK2SVyZiFZP_KYAdiHY6vRdCcAUyw3apgkd_Oy7e87Ou_br6QABuR2FQM4lJvSRFb8i0vcvagwuE5LBoEgBXR82XoTZoT_QiHNo-QFKBmTIcLWcnFhWAWiLCM_KUMYEggUMqVjqh0nrNI25SKWiP4c8-HWv_KkXED67N6UcbpU6xcfqIEBO6JesDqgzMMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s72htSIhpFaxag1Erewvfmj7dadOPW1w-e7KRWt3QBLYKTu_dNmQC2JRtVoy8a_uytnJj5ODKZM4kcvosJTqQ_QV7UMLMKQN3nY8e1gNFrb06XRxDAkIihPpEKtMs2Z7INHZxALM30TLsyWRKHJqIgqAIj2AsG0S1tE_cU8mcfpIvJrkXysyHT4LQr4d79vW1XVw3q2uw0i6s4oc8TC14Eh1mgAKmG6MMxKQM7wgAf2IiKYYAU_4S1kTdY2kq4r6tNFbZfEz_fbedSn3put4GQ7geIXalJak7VbArrYBcp6awNayM02WVU8btxDaV7mM7g15w4feDxgnNFZndpANFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npqvFqyOdQLf_eX6tZwzF_YqqmGaA3Yp2wskW6uKEn7C4mxUhB3puitYMWAfXn1urbVVS2q5ZIowK-mjHEMdpqtGDOenlSVWGTdwXi-8P-mMckhbBnhn-4ILvac5Ui1zZNvE2j86q8ywsiULKWEZjH1PrnUNnSIl88EaL-aV_f3jTsCOka_cSRxKC0BMorcWqYahP5tvpuLJ4-d8UBDPyCqZ3hOX2aJ7Z71dgMxhEVnK4RgFsHxoABv3TYtEvqctDvP2BLhogVMqOFG1QfrDjmygifl3MS9PFz5icJDW9g1TFEGDeR8yMs43vTRZjNOfFGOwXBVNZ2wYCgqfGOE0ZQ.jpg" alt="photo" loading="lazy"/></div>
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
