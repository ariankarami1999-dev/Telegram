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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 06:39:04</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBWtcBEejYbID7LWuwujy66CLs6bDU10Dz3n4u6HOT8D0LOB0mXaGGN-XRFe0f3fhuu2XHUZde5ympgJccWKr93SSREyyC21PINHrveJmmbJTAxgKDQeNUDk4D5MZioUjNucHlijxz_Aj_sl2r_j7PdoQvnAx4ia86z9PA1xPjPM8Ln5hLp5IEnczTIKD6_BeW2hN_F-wnboRTGDNRyYhiVy9ue51TTSrkLrpz-QvLm-GG_lE9SONTYtkf1B_ux2lvq3-dAeDiLNh6XrgckQ6oJDfg8Gp4urNooWvk_Jv6HPZEq2XSA_p8kwcopqMvEAsgQPAG84ZSHmtlSkxP7WZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1NBNQZrvlWfzc0_zehcS3WmeUTr2NawRZXsbbvoGZQNM_sYYBsFQoDDHo3R44c8xaFhVzopC-TMd8kOpyhnFkUKtaR6O6g-ZAOBGOPZJPvmfAHYcHGYFsGJsCttYBmBKkZrThhxeLkZt_XTgpCG13NJtqR2TepF_7N-maxGyYWTp2lhzOox1dxPNy1SW5VvlByFC6IqbghYRdNrVPVmm8jxinSWngcS4HWgkJTDYhq0SpO54Jq01xOhcHYsYMB_O09JL_tZdVFWH7u_ZCzYpvr1TDSm7wVnTf5DKLOz2D2JFvKtGsWZWgS4QPSjxGfP3yig1BUqmei-fbgkOjanEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ak7O9wEBwJNGH-6E_Hosl7QEZX8oykCVO3liT1dFR7d1ad0W5C8bTJbsAZm-Gg04yqevIgBaeKOvxx4gCIRU4lBDUJUykzyRisMB13RLBfZe83AkK7ybr24xkD2Dvv0I_fASq4i9tLKOx7AlxWwZWpwFvTw3OyYm2LetBmgH1QMvTJNj_T7uQrC-SDQZGYKzXesSbnpzmT5Wj6Sa9P6R-QHF5sObBveCxaV7AsDTLbG4376ebYcQCCSK4S9eNeYq89b6xeOCYgfesyg-XB1GRol4lNrGWRKyKjGEPIJ7iZuv4iDpjE5zt0Vu8KxamrHuyicFAUKrOuHPns46IPH25g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRxzz2A4jfeNFfPsoUfO8X6ZIIYLck6uiH1fAlAG7UyUleKLi7leoNyXQQ6CRQRIPyz-_YMJD-YI9qgEZL9g2vER9l6UCGLUgHy9tKHC6mQg65cizJHkNHmjyHxUOeAd1N3LnVA154Y3DBYK9HjW2KGB3d8pFHJ0oHr69iqYSqjVCNNpWZz2bxZQnA0j5whJ14TOptw6lzJt6cExt5DTvUjMAwVkWF9VTnP_Qvf0LFEHJXRm4DT2CnxckfrsVKegv41TiCqCc_plL3QCQbc3ysd3v9QzIB3uJJRRsKK8ixTqs-oRBUUTAY7ojKryDzJVPclzMyLLN0zb5ooQp7d7rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKvamzCKjpCfD8oaOKBpvBDMwhvI2Gyxj5hPBf77MidoWATzS0aPK-XtNTmoqMm8CQIH82ZNZN_AQbbP3K60wgQE9p5xUG82l7culnjo2vQfNdFFyw3tEy3-dch4z9Y73MEJfV9bqv3Ugd-Yj3MGJXuHbiPPE77JFgVuROmvY0Z8KKfRG-rhLUWH8lvQ4LVdxprT4fEK3vaeai9Jo7m6We_nDISg4odO1rljVE79rFFSqP7n2T79j5iGGhLtGGfDYonwwN14n0hYFuZWLLrEPCFLrTovcr7jqjhw-VhBFKCbAg07tCG3HohNFmK0M78bq8Q2JT0mXenI4DWvBiiykQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9cUT33SyyzH7x2030bw-_iQdIG7274YlpJS9LeDo8OboFPazkT-intmucFQj2AbcJGzciVKtaeBiCNs9zED73KILz-vBVuHk_zJqWkw8LHI6dY-Co8AVJai4jmsV8QwvPNg7yE5QEP1y6PTJ89ZLxAFOb6wFBRCYDrwPhKAKADbrP1iEOCgn1hBXjm9tcCa8L8eYrIR_0A2AxF9t_D0NfWmlGOqOF0e_lng0hYWz2U1ZmU2gCFGvJxv71P9dF1rO1HMQZ_IvFYk_E9A3szlbeqLj7bTVgxkj6BMq4RxQNh9QQLU_bkY-Zrt7kkJdUkEf6x-8thAVLHbChCCYYOKwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJEOeXBA6gWluShV2Yt-yxvW3q0nhK3-DvkQ9ELNx-8B6AS3y-l5tKOvcZysczZbTNDcflDHSCFapmbyQ9PShDM89TdGAxyf8qXZGDikBTaxSbPmxMoHIui_7USUxXT1ilsLGh4jn0nXKPsaBvIOhJ4SYNf3uS1gX7mGYL2twdaShmS6XUKTVFD7zvRz0icrzXqDXo_7D6_tEBioXIATLJb_rgq39Grddem9diR1xkSHympnbl-sLsWuciCPws2BUgDamxHou8ip92qfWU8iRrTeE57k8oo1uu51BDMzQrYPC0N6BZlLUbh32LKB6aL0cxDf3iyYVg0Mw-TSnY-ljA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnsbovS_LMrfrwM05EEVbpkCx5psv7_4EoBQ5dZVNBaPKY0CpgkcSu9Dl1trkLHio4QjlMUGQz57Xy04dKDx3rVltcqEcP_619eiMH64sUh3ojReHz4j3O8uK6G54V4DGHGATCVmCufIVp7LRgnlLl5iFVzlkNCKtxb-63sLEAVhHglbAzeH4hhoc6i2qcaOIlwZ-7phmaD3ED_uATaa-XbSO1DtsVY1UgGQ2fJQA7jjCFGqFW505f-XIySC47Pxzw5n40CItQ5fOsUfiLPMFtdyXQ2YveIXIxxWr7RmIr4apU6wJrrXnzEHQw1jibAbAxVNcbP2yR78-RCBGJHprA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8XJqB_T8pEKxSLdMlPsQe1LJAMaJNQGmu8OJHtAsa1LdX0p1VTPjiOD6Y5jheOp1c_SZaUfmur8fgjaoeQlsszw_Wq_5BFc7kIAExFZ-6ty1V-mZpo1VQ8Bfj5Wie08gWQ8tNvo0ULy7jZjoaZMBNRf5iIu_kabBnr0r3fkNmihd67tvYDte3eelsmVCqIKEYc9TB20qTZMxD2pVpbI3qHbAotObcxxAkY84opgTVbWD5h7Iw5tz_kQNf921AEtJrIWYuqARImp7rWxHHkU8fnDfhcHRBlrNassmVROpqrdTD0UBwq53RUhMdgV0MkaijziCa_Uvb1q9EEgXUxFEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVbGNJyYAHdjojwerGK3m9qFkXvqynFNmNHVS86sGxJkHxcq9iJjSswD5QlNY8KxddTVvwb2sR0RHp23ajLi_2SLaht7Ud9hWMVOMD_wN74kJjNL8MRY3_NVkhBMYRj9l7F0LCujv1Ny7VzxWQQxuEjd88dJ1tt6DTknq9qx5io-IEnZO8C0EgEeWyg11naZNnfN6yOEGvPcrrmzaVCVT-rlLrsq6ijunJwP2PATo-PaFcLgjh1kJbnGRIC1EqqS95IfmPrVG0pFe0tSJi3zUbtaYqfK2nUbZfcEKKDyrOWjFL2CnKR_k2F5q7oMhdYyO105oUFS7NdaTJBPIdZz7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejHsABukoZ6q7kcE2xc1G99mVAi5PXHSOh_iQuXo6VeozO20NrJSW7-1BIQVb4L7KvTw_oHvc7qdNmlDHdABMZEyn_odgQZvOK1l7d_Fm3BCS2NExRQcdkmGGfLHp8vAXYDpB1d5rFmg-lCiS3LaQVXJmKuqDDR4KD0Xk31DP4N3i9IFvjy-bU6iwjXADDa6j1E4Qxx-yKEuvLZ2h8r_KmnrCrjNstQ6A7EWK0wnYvSRCwr-eKrzSLTsr15HdEg3pohg8hIeNecEf-JARfgoWmVapY9rJaeL4UDo08FHNCeJsfhgOLYQWDVnBwnahks1SHBZQkUa8SDJ877VORutEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHcDVuvg5uDyB2ryaNwoFv57tysca08fxEICQgx958lZIvw8QQzOh5O-Anzvga_ge5G5j9XVRxjJCVhWBnWTqs0TpCCfBj5sqrwGRFleXkbDCwj69qIhOm5oPhAkHQ2QmSt76hXygeijq1f4CQ1SPP1inU8zPuKKEbJia9U4zBwaK_Y2mBduzAPJmuV1K8vfrnlYaZYq5w7qUG7TUEMhqGPrOW3_WczrSrtYH9WJbvretlbqX9SdQEs-DR41FDTABAoB_tFS0CHwoWkvFFGt9bv9jLoH_MKk7rJmmG9GtRCd61IlOX2XgM_DrjQFlsOfXoJPaGLFMtkaquV4lTQKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R3KGakiJrpA8uicmd5lGcCLfqB5ZS_7D69TD-R20H9v6RopjjtVKDa4r2KQlBEzSztJDbODvF35KV-Z913Ff5kBBd-snHD2SpAq7YNBI240XTPYmSRC02c5VMH24icq7d_IKE8IWVLJzccOtfjMYsyv-c8hED9EUeSnh3kyRjZvFzS9h55630d-XwFKY67L89qk-6RZcMW3ysQf0H9gVFIzTm8sXhf2OD4ubFGGc2YLArZ3gbDEL5rXuxStq7x3-SPy75Aln0wE7bcLNSkn_XGvzhCTvitI8XDqkMTbXDnNqfejtAip03qSu-LZKaqwmCswy_Yy2pZaTh8qsIPkNdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LmUEHFuW6441Fjq1PswWPfzSJV2HGstlWgFggKpDeK_BiU6DtSWEqK2T4saYriiFcWxcoayYeWQaTWkHhEVKpbV5tUBGO2eOccPu80uutm7ZUwULOslahHX8jLZPcxxQoCPTiuOtwleGiL4TTZ_bOv2GeDh_OrqLi7swmCNrHXjA1ZfLOlBecueHIoIkoGsrG_7m7P8xAFansBJIUJkf0-189vzAQHbvrE1ACV8FPbaomLPaRa488tByMQwUIfe_vwtIjFjEyVatgp_tjIBsbz9OdBR3nrKHubSMjD47vld3dS4R097l7XMwxZyf_2nUal0KRFlYinnFwCurXm1L1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dk7aiRC1V46gq0jUxh_Cw7ZE0AT2wAdzuo7RgrI4QEf10SaoVExKLXuTY7N-YQbwh7pL8DZ2x6_-o1oDJiVMwx8XJMW6L8CRlKn9M5WnajeIYSE9a4SVQCVJrn7UZcE--bVVqMR6j6mnabldFwuGzp5Hf74D0Fd8mb2P9aS-tCLyoGt5GzXlclXcc6Nr_pFJANY-5cW1IZYMRI9P2b7fFR4OJswbuJqF1zpcrwBQmzCTbs9inbE8uf0v-IW5P0jvQ2K8aXviJIOB5Soe1ybJGagVnoyAwhiMrazhAcBa2ldrCkdYrPpgBmxJmdZpBxIw-RC4iaH1ghSxA-VqZykJ3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r7gRj599DdSzv_fobQn0vH-4W_QBKDt-fKxHoUtT_52m9OyGjro-cZLSQvY7UUIUw6jCQLxwvL-6oX6vettBYvXR2symqf6WEn6yVEpafGvTsrsT7FuUu8iGeC-FAZhKiP39jF5CIqocyxrqEOAqpnFuqQJ9uKaMx_2qvHhxZczZBNMOPnygA4Hfbeqrdv4KoViu_j9T6tv6yov3daMwpt5NjjUI4lTxLLt7YfTTCQSwqBa1aJAcloDtXUf4STvqY--0wxsPGrnh2aZmR9xTmsbI3VTF2FBxnkBnK-ar7m26r7pZg1Xr0GZgfG2QdkvBzTQk-l3Y39ajDF4VCvaG1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPzNVSF0J5zA6FS2f5wb4eaexiVYq_ixlQIK9iG1mCBwh_162al6kF4OWYMKPjdJJSR3DdNKrpMhUlhTflwoGdxJYL13YadCAayhyHAMwa4mLV3k5WNl1TEyMNNv6RTDbmi4sW9wcWO76BVGYeTHNRSJYNgwN_Buai_jlxZb60-ajzoSK0DCLoI5QHzEQn_5pMnD1hmMTQMaWdLfkbvqok8MaB4cDCgUZPxDJuVzvwyChAoArFvjtfXkybaGfjNVL7ZmfekMVWXIKUFfaH6d6qVI_iCRGSn-1r-xX22qhEDKMXMbfAy4wb7jZAgWvNUTlIZLii67rq1ibP6_wflg9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4JagaJ1jvLJI_55gECeXL7kEVIlTZ3Uqi-yvqiv8fi2cv_ajmxnGS2cyQTffK87Zr8jcq_5to5wNx4DDdAesW4wNwhJhfH1sNovTKlErEZkoS8Fnd2k3nWz5kq7XqNtOVVigsCCCVliiwKWh6oWBcD3dlh8JqlwlRGE02xvDkjFRpoug9nS67Mn-Q2jCUL2drcg1r-HidIBZ1ca2_oGVwPxxERJSJHT8vhn2lDUa1bus6C-6QbKn3Ieo5VJU34wAIjLIKHZrcpfAxSBNIiCoRxH9ADQzOIm753-UBKpOTbd6UFQDh8TXotM8gJPxVupxhkGMXZD-Uq2wq9dDv83qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueZXtg1Eb5V6WYL1l4xtTsXepovdojSm06q-TH7uWYiVxIfT4A-IDI8Lj6c1EbBkauwgRMN3DZgsrCVVyfNJiNsSQk7rC6pqqnTGSO5uf7icI4xvcupx6hg1XImZno2ltnl6f7S_fZgSsKBzSWXwwlnUnmZBRNt0aZF0qtuncFs6y5Rz5GasTtFrDOxE7KEa7LAZ0lsk3ib9C0pLdUPHfBTS1schS2zs_5ve7tji_woowq7U_vM0AqhXHVLSYnHRC6AYTTsBlqj3ggMCWwFk2rOtDBX4pLzqA4PgaaffbWHQEcjf5sflnkMKLjmXlekvDxwAyUJIh3Lmaf6XcAfkWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f4DRO-J5nLIIWA8bVW9aq4K7ftzuY0I1X0xbG3yVF_phr4dCYwKNqPeD0D1hz6Q2v71vXGS0CoypfINyUu3EnJN9kVltCSun42dg2QfzA2XsNT3cdyz4FLlOBhddQ9Zf4lfn21CxQYvngUHp7aczyithOjMdCcRXrGUu9YefIwFzBHboMuQF332HbsqbH36-2odUuJZ0zPIBVOWNE7jJuf19L5DvqIvhIeMwWDeMGSnXD4HXiIr9cNXwITRYz-7dVsM8VBzYN5Ml2ByK6R9WjQikrvea6QNaee2zw81jhyHlP8Dn6DB1kEKdtjQiwzpKuthfhEUvatEh2r57BxirYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y8I_5YE7dzPddMQnWV4e-1RDxgvNkmiGf8tvEBart072mSkgoRf_TJq0kxmxOX3cNMstchfgmiJoCRkjC9-HP52jAujRjeMReDtG5yjZ70KTFBll_UX6E6415C3VBB_GNWPbc4M0YBEhM9gfxanwO0AHtoatwWbJYbA3dkr6jR9USUr72F03kL0nS_KLtRn8q1fqbTSbXLULFg-MlnBWgqDHu0owU9rB3UzX3MW7VbbB1MztxM_Pj0t7byr59U2dGXPssLcVPDng35PkxIK7Rhx5iGBhcCGZdqJQLi_XXzUYBLQAlzKGTd2UYH-p8RFlVVUFMzcPyFGQl0vc_XhI1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhlM2nosaS7qq8ejijDMMu-2Uwt8eH8VtaWt9NIO8GpKOf93h7p9FqLUz7Ff7BzAhlgtjIFXhdaVI_UIPTdpO8MY5VXJDhO_O3ri6bQbQSibXBD49vv1GFmWbCos6GRHUwcZ-W8mcip185PEYq4igJRqNu_F2ghei-8Us5Yl6jkV8vDnEY4dFpQxLmqaBYJhrD9D8f-H68GugnPqBC_3dUYDz1tA9DWwzpESb6zqq9v_3521qmyxFXsMc7Os6VIVW3XAFGt9AGCH_x_6Z1lJ8T8FVvTaNeNsr8URUA6mqz98FfrR5co6ALvzQo-XticNTm1zRzFVy5xcjBYbIbNe3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHVmNmXtERGtDPy4s4cysy0iUxWGJP6ZSkZt3eWBam82algEFciNUOTukjZVwsvbxchQiieQ8XIiR3wZPf5hJa_o0y8zj5zQNusBiTpwUzo-kd_OK2ZUXCgX7GANMy26Ujr4mKqTA53XlKugSNcucEuzrZ27EvDz5xvoULvL8aGxnn29nN9Ik14ZH_fA2z4ru33v_Q0ioxrPDvuCWfJw3y8qLgvlaZRgbJ5GdqdasrGqQZInnGITsSpeIx4r7e3kpv2CCL2swfPptMva_BDQZ5HPFiiJ27Tp0CvrxodZFhZCiUzVPJsQG3PcSxmiAXTqNb_4cvohwKudhTcqN0ZVkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEQUEoBgM12h0SPa2gF112YIt2BHQGzmBV10SLtUu4i74TdnLGyrdRcHYKzue4VJoyFEvNppQvrXGQWlc_4yAqXmMr5I9YuTy61RJl4yAiP_tdiaaPTSx5Njv2wFT_Vt5kilSOIZSjP4IitaKCml6A-y-Dh1kBQK1j2Uq71_nrZeuyDu2V-CauCpo7lChkGb79wCRrgSQMerBS9TBXAJd9tRmCtChXl16yPiBuWzFobi6yHye7yHhsUHaR5UNLo9B-hwWgam0qLPm3IPsdXPn2It--uhtgRJ_LHGA2twJQH98YEeAzLiwttvgG_bdGZVicNUwt_ZstP5GLe0Ex99AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k2hieHNvGGzfkLWTCqnyU7F03UD9-0ND0Vu6DuLMQinqtZlJJSQRQajPdtgS0Iadr8kuxpD4IShGcPJGKiC-3wEJWfhgsKjH8_EahJqPzFHS31QkrMlnZ8PO8N4vzrCapRnUGcFJ7NquHdlXj9Na2gg1fSTNPLtWGvgSPTMCh9xVyZKeiAqhl1omnnsa-knZwqA7dUcurXT0lVawPk8wNjvqyxIdRkwSgzNfaf4RMIbLCc3JRnUfkdyVHPQ3E14DFgpD8QJOLORL4viQdPkVpfuapYXw1w4J7zcKXZP8_boKs5HXp5Oz0tm5dZs0kE63uNdKIEZ3S75CBkmW6C24dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQz1w6liqxVhEN9nRIyp70W1yX7Kxa3qAub_3UF-mW6DD-gZ-VSDPs-XnVD_x8qYjfiJ6kivVp6xZ_xBUMttLT8dVsbPT5GYyvP7NGyIhVinO-MdET1CJYGbmftWff2y0L8hX0ORFLnOxlUcbViKdApRPhBiv8ykjziQJgC6eNagKyuSFifdf224O7J5F9FzVCDCZCgXDcQ-M-oLUoOUzP1GJSm6ySEwk_XZSSJXe48DBdwtnAosEyv_ESvAScUrj_bRFssWDp0-MRoA5A3qRxQc03T2Ibelpt8zkDo-9rCX7H68CsCMQ1XO2Up85f9pKmfL9aW9fo802uzZWEiDCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LF_JB7awXVWM2OoxJRWA7XiQFtQ3D9gqj9qwSoyK04OIEpNfjFAgRyv0VVcw-IG1jiox0cFMqJ4JH_4xKNa2RbPo-JsTgTktFWGoVAEgXdn_wHIiCP_yb8yKY4Ig6Zn_mR_zZEik-zfKJ5Ej7W15n0ZluLp10NKRIXVxRtVMWSgIUTp6sWLRHDFRZO_GjPrfG0y6LxSqosx0uINEMe4NfHim_7QIPNISYVaOiC-mr_8Im9UeXeewykGChHfOUmNSNfSUhPwUMCiD75SocDZ9NIuSMAqErAR8B5G1pObs8d_bzJ6rXAK7dMtOMpb7bimG3YyNzw0LwMfyGaBma5gIMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=kZ1j6ZOoz1y5IgQBYKgTAeGWLTKcvHfAyJj6rk-ftntObmBuURdhlXlFdfynXNWO8pQLyzbnR4bGFbounnGfxwl2Tbeo_OHXJrk9ftSEY7Jr-aexG-R1-9dcopjKkOMoUDGlmJLADduOgJWPf0-M95ON-u9C3Za3NhicLxGp35IFvOGdVNU2t4FmvIFS8i5mllQZN5wilJQc_oL8pqPinoD225qZA8Sa-hUgT0TkrWba9LpUGj7KAUZD3Sm5vmyKuOLfwfVd8yt1LD-JasdYmCluIv1wZemqPVcn9-5qD2q9Y0970zp9YHXcpMwhP0H-Q9irJTjTFgmK9vhcN8Q7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=kZ1j6ZOoz1y5IgQBYKgTAeGWLTKcvHfAyJj6rk-ftntObmBuURdhlXlFdfynXNWO8pQLyzbnR4bGFbounnGfxwl2Tbeo_OHXJrk9ftSEY7Jr-aexG-R1-9dcopjKkOMoUDGlmJLADduOgJWPf0-M95ON-u9C3Za3NhicLxGp35IFvOGdVNU2t4FmvIFS8i5mllQZN5wilJQc_oL8pqPinoD225qZA8Sa-hUgT0TkrWba9LpUGj7KAUZD3Sm5vmyKuOLfwfVd8yt1LD-JasdYmCluIv1wZemqPVcn9-5qD2q9Y0970zp9YHXcpMwhP0H-Q9irJTjTFgmK9vhcN8Q7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNHOI03KGnrx1mw7fS1nTwYaeMkvOmPn5vTVybBRHOBHtojZkLhjI6sZRZSm0FpdAL9J0XtR74Fj3LWnF1iGCMytaRF9hhHlyxMe0uA-4X45ceedGgbHO8By5Vv4Xfej6VcWjvZH8C8g4t8T71EGsPUgQ_iwluL-2KDFVRMDHGMsVo9sEz9j1NLTbQZbrmA1roezQkBqj7xb5VezsvEZkSuVyw7weCZWB4ao3ZH5CYXDjVdMuHYJ_nUhBWfI_ncBqDD5dOW0Nc4L9ZPGIladvJ2TkkUDNWXb-o-72Wf-BxBoOyiyPqVDOy6oQ8O3C26MWdq5DW9j9hxVBgW7mMQLJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G1t2OwmmvhGQqKRBLX_khOjFqxP03DH2Yxz03f1b3RT4GrqXYabueamJxZhsAk5S-7BQbuyPywr46eeAqJ63xY1Rj2CtkoNFmXIsp_AjcEpSvNg4N6ORQLJNS2yjLWp0OxuPUOOgqPcr4LIueGYiKYi8XQLSSsxpVayKHsZfAnAc6JAecYGKtyTWx7-AYuaM5YZI2twRpqcK31gYGKI_kJFZJRPB8ue9np56Q6UmRdBWf3G4WEdS1RhDMvBqz3di3T-blo796t0AGZKoIOHnZr3nUdiRLszt-uQEXoQflvUT5GolKSbecitK3Y7BjTuvLeFJ5DSSXYEbnAPmQ2gQWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pp1kDuA15-26XA1ntSWbSP0CtLBtzQQgLivS0GSz0wz2VwLxNa6WEDIG6PmfvISxI-NW4-bn2ygwH8ak1YsM9oUZrMap6DX2j9Gy9V67jc-KLWQQf7MaBLV635_4qFwzd5npfyUEZbMcVb0RdT5WTSJ2WZuJLKg8sLl8fFOLudmKK2ymBy9OyMMTf-ODEXkiyj4JgSaZo0ebaJb8_TCwp9TaqfXePBYXzfnu7jtN4Q8Bb5nOst_tA-WPQkEEU2vKt_bTOpkSvdh8Av-tryO806ycJiIQNAYt2iU9o1FlbneXKLGmnScFqVPUwVAzuDvMPDnko1e14Qjo5u4E28Yl4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KuolamXPRbJOM8g2ek6-iJJqfIFwF4J2LM0achp3Ugfv8zN8TmTrJxBEfF9w1eonRTY9Ui89CLstMbYUjHTEK26KtFBJ1LGby0D841vBgy7_HjAcBMbEuUxtXFMepSrylxA67xLtRNQjfbzaAG_HqHtVmtQv2CgZB_zFPVp34TBke8UYgxqi22WX36z7URIrnMb7Dx6xqGDQy7gYVKoIv6F10_yFr0Lj0crIMmoe3rcOGFUPcj4FOY10AQtdES4flnCU5CLKi2AH5rjVGruoNloZe-krmwqXLoKAs63_U6IoFwuKUEEfVHE1W1Zf7glF68Wf6Rxq1biGN0ab8o5bhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nSRVsggrTSDKeGu_UdFA-_ozA0D0jb4xWKuZOhjF0y3x5BNe-xWaoj-MyZPTNB5wvaZJDqLv8vNRpAGv08JTZMQ8A4vup2yV06fKx14fKlU2AcW_8Y5kPx774wyKqJS8vUDHdkVAqOv8IrOaCvew1aPKmSLsumrogjkZFqLwtLqknpJgKuKnScFSMGMvaqcAszxaI5ybRtBZowe5R2TcL3a9W8zwOSsgwuxg0SD3K81XbsdNmg0Wf2PgISDhhljJa8NqOB49vnBTpaxFCmZq7KyUoalDGuBBOm02HZgkAnID0bFgoGcwUgMR1zAjRbnq0lTKFleQ9psAO61M3FTrJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFJHrYTx1h8FBRbXwc0HAblS7IDRYuA0DHzYWsyj1BDbIRagvC1f5aQIRhJ0pQE8Weu5eaSlws-IStLAOOHBkGkaVPeTvu5rP03jsxNttivoxV4t5elrk-kFaMCByTesBHwmE2oNec_xhrrMGxgjTOqAMiJ7pI6RL7hVfkLnyxIkAWkYKOiPx27ebYN_uUSIEdleQyaxj8v11v3sgHTQlRO8uO-ySNBXqG1l2uI96h1iyI6jTZyLXdHo8udY_kLfs6iBPH8ZVTiR9MlBfD49DlRa6RhkrlDVRWWxrQcGmvirGll1JPONOJ3jvR2r8rHbvqCHjSiZDKChaSer5iQsAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwCI8PJO4S_FgeT5xUWrWiwNs0tea7RGFV6jppTYQcDK3nJrJAyYoqq-J0himx_l0LdKb8ZXkIyzlerJv18gwLICWSRpqDN_-48V5d2cBRL9QQDXVl35GS_1LF8YqaFIEemhoZLbzY_pz0zFsTN-Ugpnj_SAmTPhBbA9ZQRQD-Mj0VsZ1sNo3-SL_wb0Olf8zecG8VoLQhIn_-FQT1ha53wdqJMbUqWIOX1KtQkRBbn96Vt-t39wBAywhJVVzNutssexZar8wUl6eEyujmQoWMCu0LEJFCb8jkkFYxtKZIwMacYUcDSXg3YpukpxeJRNnig25m_0_1NWxnYV9V0lXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_FaD4wgifQrFjYuXCdKls_YqJhG6bfGuxAudpuno8w_BZVQasETRGS_XpJhzSh0po89P88P4CI276lmW7WgxWCZ2W0u9-x7ItOYOrqPKcBVGJ0_yA1eC9Vz5GiNIb13gO3OILstcKoTYRkEKkMAiCJKzsrhiBt38X24tqIp0RKuKjeZg521_1SqXt9fZeEzS1GP2-A_8B3XCHosoNmZ_PnktAkjMeKJTiV1DHZ2YyC15RlqcFmzY19K8Xt9iTExKle4wlJHK5kw8NbKpCaNOUYgWkaqUr2gn3SsvwHvLsVoisQ-MAB53RSwjV-DFHkVgG58yXUP9I5ibW0vw6krnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sX_KVSRDFrZro7fJMj51Lh_x_ODZHnDZZlpD_MgmxgqWT1W_SV1gwK0EA01XR3oHkAfpiWfxtAfhjQ2HsjrsD6XMYQ6u6Eg2rUje6dpUXsTRE2bJB8ivET8q5KAGKxbUILpyzGrTABH4ZpzTbf6dh2TEtpEne0u-uU5t5Nnxb1QFH7izQQdinzNW61Th9wsxwPd6MNJIJkmrvv5AbnYrf6C36cLcj6YgEbhywSYcIoTxHT1Ctzz_pbAvOoWcnvd49Dy74xzFfDPNM4xoQ2GNMiCxaYPjLfqscFEzReBoBsTZih9H9iVsiOEDoADkxA0yI3lXPw9LQ50Caiti-JHUJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LrVXyEXn9_uqetSh-mOG0xxqWwn6DHQBuoVJtRp9Mn_49zIGsvLiVbOV8lB8n4RPji0IB-LAkgMjT3igtzWghILPKfKCwKkVvYDozmTgnabrIIJFYg_Xz1R6Eoqthe1-E2z7M35gnhgF8Nz5rzirbDI4TYZfDU4AnlO8ytGNuL8yXwc2pPUJXuhA9T7Hfi0YbhTXapCSYbOl7NepIYiQjZsuMRbREktGkSPDujxdF7cEGySFpI-HNH0V-lFDy4HhGskTZMJX1WJwjtZv6_fT_JoQfTbC8ENtHtm-LMWXXJhB8kqvKyE3rYM0TiEMNmMj9FFs2O72Mbdd0Vb0hbvunw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZ5kdIu-2NXLemRntIm2q-amVN1gpN8YFSLi9M_I334Uh7dNIDnUntcrKJ52-5mEQXT6mwnqh0x3ZovscScD79i-fBkHwOqil4rJ2QB6tn0MAddXtJzBhaj98Q0h-XIBE3bdU6u49qSNLnJInDdHqh07MA7wP1LzSt-ECPLsEJevywam4bZNhe41WnuvOgxQv1k_YaiX6AsnfcM7JIIgbravbFZqt77Dw2tA_LgFqC98FUxyXxhLoYVzfgmuAFuEVkun4JmbIrlASNa49dR8fr6Mkdau_DjaofRVzIDc7gX2k-stGwSWCvHCIOBDi5MA4GyPeqZ0WR7gmc3sGflvsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZyr4vt7hDr-ZppCGgisXQdnqZ6PcpjLdA9aJyjk1anzAWKUygqwMISaN62ezbbH8fvlAZjfzxIIGAlpEEBTSFRCQrF1A36ZCHmR4f6oCdEdQNeX4NXOG_D0ygKQ6yefTppEMaUz0GVYuF3J-e6P6iXFFIHR6jXPq33p6QHf_Kgbpjj1skRErMSmNP_aS2fOseOltuqNGLXJdjtjAzYwy8Q_MNcahGT4J58GIhg9-W8HsPmm8yqat67jzub0DGkIezgzkuORgnLrOplgIMHwrEeR1d6tcUA123R2Jg55tkOc7xJhUx4S2XWuTexP7c2Hlhl1R0G1O_w32laeZSLy4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lb6iAgeb2oSBZi9jS8n5UveCJML7JAT1lKjgs34qY5opRLXwvxCY9hvx-OhSQHC5zlZnhVep4M-Zd_Byb2Ol8855z15LMlopJs9xK4MYf081vU12CVnrgkadtAH2HAaY_6DUHNmrygU1YdK6rYl-UoxnmR8Z0hp_NqTP1f2VVJEc3C2Tf1NrLeuYu_4sM53UdWisL4youhWoi4UGN8xioFdc_SRHWpGw8TePbwdIkQuDuYjO3dzoOTk_ykOYLTgBf73KBPq_YMCSo7A_1910dy2XH-zHL_rSk5oiADupjHA2qYAQpzSpS8YqpaE1Gzh42W9PzJTvfAt4b9Cw9ZwzWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vo49Av1CD2LMy2AfLUd-UpjdDg8-OyUeaJsQ41bIUMisSsBFoCQ_P510SdMy_rvHImCsrH4dFwAeAibJWWr3NmGESGekCcmUBtwzmKowfCYfqHgHGdwWSvSeu1bJGkZAX0sxOdiJiX_1A1CotePItjCHY8vJFr63lUe_nneJMJ45kh1ATTQumXhWwCMIYdLz0R8weltNDhxHmBfFBLpFRO5fL0HKaIiuEa69I4RJnEdRFYEW57K5R4n83uCIWNbMzXBOCviNEzPSsw3LMvhvTjKlxcpjsBAUv1mn1QgrbPKqB5VIJmX5TZ-NR3ZlhsIWAM4_HFb6eu99JsXCayBe7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jb361tt2st_chSJB7ocfvOnq_SYOKECqTwqQywl27Vri5qvihekK4rfnF4CKMGvlZBVMnVNunBRIFUxKkDVh2ZcfO8wAMSctWzvCXDbH4b91UOlp8yR8xBAioe5KBfB3xKDPzUY4A1t58kjyzu4xkVNo0xe0x5vROH8EXlzY4Dj-EGuDdL_u9MvKaVYyup38ET6ou7pvxOZf-qUGu-2SsMR2X-vjunpaWVbuFmle2Oj9fEzwzbz-9r1MtwioZtVdc5P4AzHn3m0wLNfbHCFBFPRKCP97XKIEBYMAKBjEIdbbI_YiWnTNcv7xqC8LF3ehni7By-O0oVyd-dB7CEjIcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6BfBYhgum1qbdKLwSAsGSs8BhRVsB_HxkuJNId63MNlS4d2uHUs8UGZwvUAW8icPeasHWmLVKASS-k0W59KUCgzfOAQvBITpa2NuQ03O8AEG5xeU-gzp7jYP_wCKsNWhdHHLLTSDll09xMa_g0iPwPAMPix4dJN2wXPP5HIqQhV92AxKDwBh2L5zG_OXPuMgDRXMZhzcUx4QaRpAYdpqgR3LI50BY8HnEUKPSFMW86cILcfyHc7Apim9C98e5u7LZ4dfptZD7Rp_MklujayGTzlkVb-Cr_bwpITxGXk_IzdOYF5-sIcijbL7PrUIUw6YyDtiYnxjPzbLqs9EP8mTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Onyp0aBI8BHyCrTFk3Hz-h4mzsk0O_x2S1xc38v4DCVXlJ9BKSciTnZjthvnZ0gsSVwEhsz58nljrI9eY1Wwtok4dq1c05WcDjKuQU-rHBGJJAsfbq7V384cvYEO3cUQ94d8pp4710eVp1qXQ_8TfdfBdqv5Ik-kIXywgbMVsv2uqZNFQKEZDR7QzQTkAvygqVmdibw7k4-qArbI7h9RJACdupsUe0Bb9f42qv_-n4Ioc4PcyHx1r5YawKIGw_ttv-cyj-ZNk0sxnipIkQvTc_6CMK5Qd0dGaQB96uysHMgx1r3u06-RgeQtdUJpXt7OXE6CjFOjXKeSNc_en3ZoTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7xHtWHYWKN2SMF9l0b-SunaCnnqlocxyvuJnaHAMlWj0g8X3Uz-lQXkBFJT0qO6d0FDMks4auzszEPyBaOkQs1qPuQPF8T-V0mXEYFp93oy6L9XE9UPELxWYRQcvCONh5sRVOZHo8xucO0R0v8YWwvFucgSimjRNIhbRAdx0fmzxB3WxvoVV61h6XKP9h7cvAbZhaz15_0OARkdWPfPe3o8-Nm9XDrI5vT8ytfB9IiwGFY3Xi6GjWvrYpxPF0b4enLtF7T6ipeKeEMOyjxJLKq2y6ue_6zughQ1kIIGKgm3ONPjQBAA0zXQjKrTiWDp0M71aY-JKDovPb2UO_FmKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XCIinqPtAwFKZ4r98cEVnBEaLB_vb9OjJeCQmNJvscErDY1UycNAsxNntd13Rj8Q8x14hHxLYs521hiwgfAuPfkTec_022vT-l5A_O0GyXiIh14xwPD_oOX3EjROv25HbCM1YJ1q4h6VIKKUGGtmIAhU3DM73PszvzRV4UTDcygfp8-URqPJkkqf8Gw4MMllVAgg5tcw83Y1lTUAdELrO84ExQHFq48qBY7ZdttDC-RoTkYbLLr2SBzFwS9GhyExor5xidNGqFR1u-EFHeW08bEI8Z78F_r2JJouzRiS2MmHybpkWhRoozR_P1UnnIW60NpyIbyTfiT4VBh4tjBJLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgp1Ac1Zkm_PcRpVIIyucfc8X2ZScTuyvISJk16b2s3kwcDitrYeWWnEvoYzXH5FrulIOQ7re89IHBfRa9fTBZ09hevZ4sy1K3zhMsTPXCa3qC08ax3BKBtA0rGzRU0YpLwMTEG3npsuCQLtqQ4Wwz3f1MTicvkNfSDWQbULxFsdB9JZAb--SBdKa7YMwLGlGAj3m7Xj-FhIITsg0YauF_wyR3uWyJzZ9R9YScPmg9M8eBdzBiRwe0jxIA7fQS_z-Zk01BaYOxFUveTPz7i8JElLGJCtFh9pocKDrFJxELki9rTcW6LhEF-IJWPfJGmbMbDbcpBt5yh-aaiyX9nTlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YU3EUg18S7Z1MQUgJY1hT-7ScOcjKKgqved_qhpLnCO1bFflGJrDYut9dJTdstHRKN5Cw9Ee0COF23-QVezhMCpGmxnBcSodvPY8WgOVeUc3vafF4aEGRDZInLiAwFp9EaQdu_rq99DUmdQ3_EPM4MjMD1O3umXIDA0zSkpdJ1UUgfAR1gKxAYWv-J-vqZhqz7bpdQz1QVwuCcZkxD9B0k4ASN-Bg0DDrfL8joeToyKvkdT5VgUSRDQmp7AcfSsTHSRJo2jz99aKeXMoBG4vUFHPUowiS-IqeKEBoqsP6gn1q3-pH_l0-x47mhw45B3uOAPLxI1nzCqsEd3k1iLywg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/feRlw0xRFM4ky4AgoGrMlSiyrGjkCrYkCfElYMfP3gVS67b5zg-e9MjvureSk4IEbMBDPeBFJzYJI5N6fdNfPhw0OUCwAHVutqxPN2PGcOEuFaLP4Ha7nTD7N7FzihqYy4Uqb2Y5kXxmwgTyo159xIJGzVVyLd_Eb6o7gIOyj953EzV-HY5mPdbfFLxSkBq8m1kfS1hlauphW-8LdxeFgrZgHgIo5wHCIXrtiJlSCtIfMYdvobSl80It7sd_g-QLrikKqNs-p0TnbcrJiHxa5VojfiID5YMZ_VD-5WN7T0fXlEwq1Kks0msH0YdaxUYL6Wju73_2bw73CDmqCS47WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hhF1eSMrBSb-ChesamAfE1wIqzFi1oN0_osb_pgfqlveynIwRCyNnrOCImH_M-vBn3jYvjzi6Zs0BBsDnylnBwvE17kdMcV0BQEEzFBpFa917MSAN20_mtdNhIOq_3jF1A7tJRHsi0bsYUGbjXvejvx8tcKzy8YqZ-zRva61a1dWMNN5ZLFgrP5HNcQGQiW0-gDKuInkcQgMXgqL0peZZyjXIpGPBhcc0Qn9V6QfrboHGGSaBDAlDwrdzTRUV0IRBRSujmkj-NOnxUV2_b0ofgy6JcD-B2LBhH7t3e2RMiGdR5hSwsTU9idjcrCewt8hDHOa_bkfYwFh01S8u7qzRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFZUVSm6z1tLSdwhsQ3Ox3UXJxcCGVkv3c4jUGWXDuN2JHBtLroZWyUrQ3cQ_p6nRPBXdl4iihCuIq1C2fbS9tYoPaHEAdWbChRN43xSYU65US9rE0F-6ayN8u_HQdF8GDavbffaw5sTrQr8xYC1D2t3JW84foO3oEiewJ15lGCCfX99uirasmMp8zholRWdMhyk0WpDEFkLE-P6F-Np3C59vl67Ytjem8__Hab2db0pwfYlROXxf98EWzxa55oaAWkqs2DyI-vqy5Rj8jNN0dhl--A7mH8iZs7Q7MIW1IW4Y1XQk38ad8HK2Y3p_8GHFXImF0CTKNXigJSWW5U-dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PzSdgzWn1NXEJHu-4Zh3WoggRANKAcLF8v0TPbRn-MzHD69C9gvbYuSeRWEbb3K0A0DQ4mkyhR0HmeSfLbb7yxkr7p4H77n9cq6hkz9lqkzDL8MfKqVqrkFvr2HRYOy22VcQTLXfagkunU-OsqpkMvpt3A2ngO-BbpqYB2WQ8QlOQITgobg8K6PX5gWXiKhtpwKFLq5dsU3200DS17lmp7t8Ccrr1VonANfBj6NLC6ECgVJYyLUlqr2o5j7BptNrmyMBh6N8PjyXY5zrk_vKAX9wxK3Y7augjg1ZQokslaLnlhPliqeNBzMPEiMius-LxWmAQ0ZXqvx-jZLKu-dB1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ijr3GSbrGGkQH4MleXyzN_0ullF51bvKawisDzwe45FrM_d9mlFvG8YU8hNKezhmUK6c0xO-TIszp1g0-ih8GUbkduyrJvGWio_bVfE5GGWpaWQfEK5ZqXd-rR3cel7x90II5nN2P_O79b__QpPnz5Jw8bf9lVccClYmXG-zrTL85Xjz_xpQ4rCyTwb90iI9kY8v3ExF8qDpzj_I0D_B-4WQ0tfYxQhikhQIj6ieBmnsWid264QCeqeGqJNVeXTgJ6fvDlh5kKyx7eQHtMAqTAoU7aw0vmmoHoOlwbnlo8qJvPVkkbM0lxAM4fqHtEPb2MAKaVtPInl04zj9oW96jg.jpg" alt="photo" loading="lazy"/></div>
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
