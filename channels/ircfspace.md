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
<img src="https://cdn1.telesco.pe/file/S0BRBHAnbxchSuuxsuqbEmdjof5Y06TKSZVuLxWju89N7G30k8FLJJTzYckfHs9g7DT0Gp5ehMt4EMyCGDlldu_HOvt5tREpUTvKG0iZ2j0zxW4Dx2LCxsAxFoiezFf9DInhoscsi_R0a61f1OYBnCBHaicNXZa_9gquH0BCcsvo0u567JTJ8k_Mdb40ndNlbC7jHZE6JTDWjnw89cDr2cG5Vf1wQKx7bgJyu2Rn_6V1M4JthOUR0h-PDqlTSIS-3pvJFF3budvagBxhSW5cms-yvaphB1s74-OGlUGeF0oAT96NCdFEWmSMCMjfpRhuf7BtOPYCbFkUQKQgPwiBCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qMp7Wisk-Fdw3wNosi7UEhvIYxAJDhvwF7PB_KL_NZqfZAGO5wvCMw69Jqj6c3P2vSWaqYsY0FB0K6ZOAG0CYARjtYylwZFMPdwKF7cjrSIyWjOc_J3vt8Nr0tb0bIBNVIFRP_cy4qOntSOxT2fVa-8zQZnRjudrytQVrpNSRKDHITIcAovVV1FiyeXLY4WrVUEz7pzhSFLvjncZmYI56XtDejn67BhIotWWWJq_XSDksmNysx8qRLFf8dkU36Fj2J1oCIfipVS_PHvnWdB0ajRNb35ovBzeVHsR2NUbxxdBsxbqFK2JpPPA5kKBWE1I0L9gDcI7EwdnkHxX7NvPpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQQsqBm7t7szcPdO9neocSqz3VmTkb_VFHl-f6QS2dc7QF4EAWHxIjS0PcLkgdmNhLfXy24Vxs7P6hUZj3_04bQfl1jzgqOgPqdxkcltRVzzzB4htz0DruoidgxycLJj81g4kbq10tJ8sN3JQboTcuQYsV5vROGlz_wNwDCs3nRXfl1A1dfRKjnEl1AyIwONAH1PpGhSvTkDBTMnBy_Brc2P9SmcGuOSkjJcFUcII-zS5ETqKM01LNe3XXPw_x8whfup7F2KQFiD0zizOwLK_YKRzgAmfPeA1z1Ch5hz0rMCzyH4a2BEvzCQYO7naoyOhIhWtb9-1KF6OtJiKbTl9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qT7aB6htNYZQDn-ULQ8ZiwZBYgSc5RRDeHrzxGKOD5uCqNnfJBEpM8gfwAloj0qt_jjcq7ZLctVAjVsX0AZD3UpIlMPRiXiwsvZgdpVJeqk-Sr87PIpqs5n1TJQ1I3uTls1epALwPqYbzg0tPmW2ngWHfhz3KbKMliOB1vBU90iDeU375CfTItEDN2N8_LYalWEx1qqaHgKsmbq0cbx0aWdXBWvuKImXct8qQo6wdO8K0plSf-z56OPtM0Al_qhZFF_BaOjS_sRGW7upXQ8kx9pipzbGWWpVEDAqvWouDopyq_UgIYYRWoeUdeVXQ7MnWO292v3uPxGa-JrTKCiZsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HvVxGKAq07QpD1ldpaaXc6Afb902doFUBab_kcNAqySwr4IwfwZrxC0ffySviQD2D3rtuA23I_CTy6l4rpvcNwFq6VnEi4xl2AEoxYnzmsEemglbxvf4NHZAocz4KmHhpBJPEeuMtvlDv5VE_5ZkMRIK9YF1eHso1o5XVbY_nQmYhpuSiBg-t9G5ywTqtSGWR0maCRUbccB4OXwWHS3v4tEeJHW4yxuYYgMVYjGpaqSaEU6XFYG6ivibMU25fnfZbd7Cdm7_GKS4FQ7ySIxbYkoMfDCPkWMf3-Jfk1MlchI1fjBEK7ByKp_0IOIwl2lDWw7Qkehg7IwnQmwW-C8AGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YlHw00aC8mZiqPGsFCtqatRrNb1J2mifj-E7jsou7fTy6hpXcfw_-qJTFoNOmeT-SMYifHf25iBh5t41FUMHoEuAYFub8Q3KiDde_tbNAbnvYtzh_qvHiQhI-c7qeM7b4ocHYjKEPFaI8tx4O4L-RHO3fDN_2ToT1pvBMg13vUdrTJLlpYLMMkABG7KojZq1o5mFSi1cVbFgqX3UqJn3tYlX8_kOvAUURJqmmrLKDjMlFdFIMRJhPuBve83AvvXJgOIF-FLairlG-Hjx9XgVswxZi7pPxwAbf7qNgHoj_HXgmgpkZrxgdkm-9rxX4PqTRkYoWa_olnRJwN2t-iq4PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kq-5XqrtuXKUc4iF4EhQ1VIffuM80QRJwb94wsCB_Dh1glFknCCGwd4TAksOuuijYY0QX9_MMzkJ9L3ug83G6HtAmRZztzG9wH7scIqBAqZnfjqtugQymnbBGe2TWEp4Rw5UoRqLMlhsqA4WoKyS7RZk7WcbLiAQhNzLvQ5EhL-Bj_xDONn1g1-MInf8rAjahjPkz7cToIBux0WOOsj5HerpSmvzrsoFSw9fiGSWP-YrddIygUjO-JXd6PsLf3JFCkUdM8koG70DcCL7pUVJ86g4O0Uf4MvC2gJZktF5xWCAw2wipn_nO3_25PUs3oHWdaWu5ahGEGlOdqjS4p9T3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EvCo9KAJ4mVNn6cnmqDtXchhNb5dY0rG5-79weusdtUO5B7RmDjF49flJ26bwAuh401KTtFtF_y8ITYPoe5UKxAaD2HlAh3J32VSGMg3dO1gNAf3lYuRVQKTG1_Ybbu7A6nYilVXH1Ta0RUxYLK4rqOqMB5GfzU4JMuwtKxe3JDP8kMVH60Xx_OYxF5rxNxfT9wu39SGN3cf8dLhHEARG7J7e1pr5wWjI3daMK-7eINhOORd5H31gYQRPEXyTJsCB9XJp7K0JAfCJodnEUFtfbzMEu_0gOWptvFW6rI8eUH5A9Mr3TDRRllho1gSMsKWfNAxlZPrUOchl2k9gLHeDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWWz5QidSeGcMsdMEIAj75mHHrlv-Y9Qm9uCjOxAeo33bVkYAD03sQXMH7pBo8h-hRA0fzQqPM78zB1Iv5ecqo7jM4_CwsOwifh7mJW6jhyclidbJfW97DGZlev9gIyL-zLUOYyzZc1bxcvp6rlZd5ACGUrXHhCS4Pc8kDTzCjEpskbnJTmQVZgV1mELqaJ5VosdR-38p4hG-datU0PWdtHIl4WRVphyve_4reOGRuHW9qeK0s3bMGut3pksU1fPEY_U4C76wS6v8YYBgeNeArfdgZIrxYDv4McKG-TAIJhe4kHKkJKeWvHl5QiF5g3KWx-eND96rAEhCulIvFHBfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A03XbN1ld80gvuWjPBbsMmrQR_MoxY5MTP_-XdDpBqLwSyWgrbbQ1MRhgIQOccQagxRevhENw4piBilCJHNgmJeNLoZhRQavxezDs3TLtdBawbxl4Yahzou0Xz4Zfo5bfafeFbQU3F0jdcs39H4Aor8WMCHl8xxjAaMXajQOQnykia609o_CxyQFyRMsPTTMytNzpo8SjC-paF4q4DyguQtSSj01HqTufA2-v6h3kOBlpkNv67GbXnHMA1T6sULxmrfcPO8QcvCJuQXm2TrZbmrCUWIkUxhv8sWc_biJlOrWKK--ZxajE1CJy156xIdfvEg_M6Dzz9X7yp_3AoH3yA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cqzr0_QJ5xvoim73tP1ccYOVtsS2KDin8Ki1vg5DqdTw7v7BoBazKjSkaMKca6gi5LlxH5ShOhyDLSpSKmaHZEQZaxL3_tkWNhExQj10HkUmUP7muW9iZrrTATE_GL_1WjeNTY0WrJTOVcD5Yvbz9qlhNbRrEcrJI8kkKK4u4utGbNuupEvGVhgmW0mMcqIqNFECtSIU-DNs5uRLhMviDVXbYugBDDopKDNfiU9DvXewKDrelB-g6-pTSI-_rtoiecybtE75F2sUHpCFD2x9QIAR91f0051rQz-1-JXl_BVkjpBQotiSmNYirbUnypmetRNrr40us2Od2XWfTpTedA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XwwuZvZJ_CD1HTzA2-IbmSNHME6cHz5qWW95NZwo8sYetUK7v0KsdifrUQexmLBvk87AIX8vVLtIeQnUA3qC5CvI-WytPPO0eiLXx8G5KmxIQwkMpVPsuBKdRtoJPCZw-6KXXK60uuj8HjAPnCZ2-N4fSqlbexfifsVm1QShecLnNjgkxcxov1IFNdch_pifZSatFXLrbLP_ELtP_MFQUrQYw--wnK9tBJ9QtV66807UujrJDKtJB0P8TeWh-n5Elfu6Av5ZiPkakjU-ViHf-MiUD6yUQ1jOKhXBUBcFFZhAFqNuMR-OLFtRrFWlDfHH6d2s659p2zKkgku0Wy32ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibu8amfy9c5Z3buq6pqMFccRmSsY5VD0Hsd7Wat1GHvQNS5gqf_Sle0RcZPHlnER9RZGkpok51xuk4XUQsCaHInGV3RJP9qIcO-UL-uWUmZg-VnFLPXMUIpg5SW-H6n4w5EuoX9X-AKt7jD4nGzevY9PEVKwmAlqpAbRS_eGDXlot0ZyHEic1yQG-gr8HHAloGgqAr5nkX97NV5uunp3j7ZTenoFVN18rgId9dQ1qx2dlLYUGQGHZGfUh5c0iGX0Pt0LNefsfDTYfecaBP86d9hYHWvh4wHKElaBPrsPxiixiKrI41GKEMErxetnmERQLaDEOfZa33OtIL1q-QJlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AR6T7oWTvYeBJ_MVPfVvCWz1xEm2uDKnFNws_baQxDQ6cvv2S8s4deraXgqnlxsME0OtfIxUTwsEl0g8qWhTQA0yOJLZOumcFKAV2QT3nBzkW45DHGb5hC34Shgxu4Rw1YTT8t_SlFohVXK85JnJ5xbo54yMKeAjFRNpisH5uvR9PiX-_3eSOnstsLtTxBjA-E1SeL9httZJevC140rMnw21NY8vWGYp3sJ0bi0nxAPNZTOen0hMKAMa6sh3MG4coQJFMh28iBt7gMerUyllys2L2PS1yk_ZI50oJ9proA34k4f35TmzGPbDJV807Sie09-Y5Vm0HYhEKtaKWQ2MlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3HI2Ujk_EMbbxTKYpbUhFcCT8Uu9Y063ttRBr7ee_J4l3V57tBQRlv5ENjldwdVkN6C_QndDzVn4ifQcvPlhQ91OkRQOcZXwmL5YaTYcCqRJ5c5J8JB7rstv5M6DyF6FczmBKHNTkBjkvzQyd9h0QkdLCKTjvRaP_pBt5fstJmqZJRJhg5l9x2yfxgI3JHxTxpCqqhq_WywnEi-SNRADvV7mXZbY8yn6cli3gznDiwPl-RGtcbKrbwHe6M63Cka2ptRR_0y95AmkJ5y3UJEcW4BAi9FXk_RlceFVMDaY09VJJkj7r2vqGQif5zKBDR7iFMtboordVR5wDn64t9tHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MQv3bb-CfTI6NUsz0CjOwTcBLS50hLQx06ZGF9DtCcDcGPACxAj3Z6OKble_7_9z2zZQvHLVpLnaXhDepcc_A876Rc4MNQyLS4V8YuuMS_fK059sMDqA4lCtnd8wuMs48OnoDROJgX7S1J--YjdvDKuRS3QkeG-GOhDyKylpLOFBWLVI1XxxrICpbqRwl-3gyc3TdjMfEPzVHCNAVuXObZPnspwCkKBw4tFDApxB4t5oGvntbP1zQwHfgcoKSSpvGsTg-XXAi57Rv7zeByVpK41Bcp5HeMGTi-IRRksTG4GjVc14u9fFMfWIoPs7KPyPag8L3SOOPFFMuZMphM6Gxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dqfra8WngFwJXsCJkqjQ7Urq0NE5Y_-bjaXEI9BS6gpqu_g7agNliXR181dPnXougZs0kmv-VyDVSeY93HFINj1GoswJ6DivIfGWHABYHAlKIcb28SVUJ1CivbOxGqUF38f_ZF14F8qAM0YMVMAnE19RM8N4qK_FdHpqf9D0sGBkOKRPO8ibSN-PQ53lFf9RtVvoZbHACndQmuzRhKL2KpUutHHoDaL2ypqZyiLLfehf9c0xFmWvhzIoQY4GUTu-PXmXBqYBT48H-R13aCIwdVuxSesQ7O9swggXmGFJ5QUzQaSsZnw4xFjoeXWHfdtF3EiV0p44MVaW8CJUVUxaXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/POIFotxolNqWbHRh3afPI1O48BfPfCx0Bq5i62Zst3nmfOTAMwNIjRYdJJPBT1ryx09wYfc6n-23Fy_dDVg2igw0HqRkCOaC-ohlAaLlh5RGs-5EhjP4Vk8v3hSKGD8mJpvPqFXe-zE21hNjgSIAtFYnYexzeub7ECB1bjTEB_XMBcM1fh2fyrTHcGrTkDnW0GwKPJ2IAt3SGxuPx8HtB0iqe_PR7dnNcVPh_TH8E77TTYoScfKZHMK16rHfLmgJNvnIE0qpClOeFtSHgxzE4_2KTBBT0QPhmvCc2bfMTtZfAAeEwabBoMM5FRyXSO8nqkAJqFUrgpWetIs4HQnHRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODR8GxWyxG7r_RFCH1P0jFnb_SJtS69C13Veqhx7rdpz_lkHdmIVV6udkGp-uqJpQhYi5dDokxhCP242YI7ckmnpnNrJi7hq3Z549ILP24_Gcb8BxEoGXxrXtrCR9Vr_qBzwGFxZ1hkTSkiltVXsUPFE1Ltzl2o-Yd267pfn7fJ6TLIPaqSm25z0ch1CnzZpcw5fbaTERRL-eILX62-Hppq9O76QbWQQLJRpDqFkVLTcRZ2i6gKs0-tDgE28FV_t_VxNW3k8dYDdBUrhXivNaBpocv14xj_N_UBxZ-qTak18OzOkp-j98HxUKpcnrR32S8LlWg7H3ttXyp2dpDejug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8l_KzoAaZJr3F1Cfarv8C4fIfSBU3IbzGF1IpE0uhM5vMSQmrfod3o6ngvukuksNBRdV2lFqYqdVDm_tK9yQ8s_Z_RtAWvIGcTdCIlQPeX1Q6hpEjGJo7uNcbqhElAN431O0-UbRpbLMzhi3VPKUeCV6B0ovXDoYsuPhE7cu3yktHosQHvEAbtDstWAUzgANKqTtogJIr5Uts9V3KOFYbNUmObZW-5QDFxoVuZAC5p0kwBMpsj2MElFh-Gavy8ZK0K2rHvQDzkwCgbXIpJGIjFeI5gBH87BviM8DTzDz_7PARzJCKvZcuVcxJFVCkkfHshcwQr0f--bK_14HHWaqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oFB3UQBhTtAWPJcKrpyqVR0-p7frtNOaqDbMcXzSgBZRAM9BAZQOAFZAG7TICrV9dG6E_1q01EbrOmeWxwWFbG4eZdz29a98GltVFb4o9Uknqqk_96Y8xEks07lu-5hCV1YpVHUbtQmGeWJsWuJVVbuHNi-edcJEopd6Qwey1D4Yqe8sVDfySL2aClo30F_KNWZ3LiA5ViJShmSwn6OJtQGhSZkt3sGsVB3iar4EL6dCCzzoMRANr78O8lHRL6UcpdUnX5OJCfXpYxvA4YXQVj3ivVFvKKx-Ev14hEuFNRQImycdY1OrgjYV9LXRgl602MWCi2HfMrVEG6adKIXgLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivZowCDkkzag1X0hRvl-Eg5uaSnWdyVkdqg0oM_ZAS4vgtSTpbvcwMQqEdA7BLG7ddUxI0iLpnjB7VHAfPmkyHqLy5FpsyTwhRqt9HAQ-qvmauCH78i84-RNTNTvfP8VAaAo7bAyab4az6DLuws9zsuCp2TDZhUdMI41T-JjccNyw7i0sd0K161RJX56SCP6xwxRac5fzD8gBrAi5T9zY4rtZb3fFKpcwpXUId5pMES1o4Trpm_OiPVAVSavxP2WGDbm_f7UN1aEXPVSonPOzSvdZrCz4iKL72_s1o0mAieJGLnkh6bLGBCijfwNgaFXfVgzNn1UGmQEX0LcmNmMxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f1o0JRaGY_mvsEueoArakWgJSmIsGEaFly_3Aa9im-tpqXrmtanHCq42MXjSn4KMVm61KzlJCcbzFLsI9dRNHcCcAK1uEdnB4PNUMgELKKNg5MiEt8nDyTf91EMWtK6pPsQVbW_H0rA5Gpp0feFAPu6Y7W6sNm-r9aojUpBmEHfz6D1N2jjNfsOMg8KGZvjibnDntzgRleoNlEVGWTKZ55aGp3LFUZ5zxw6SkcWRATfMOCl0P1OoE9S_Q2x8CqQW9SDkfjrs1rKN37elibr5j9IG65-r2CGHJAukPj2grzbb4eVV5iHrtJHLnE0rrvG4vN0vJId3jdhU6WPAhurDJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKeNTtdBKMa1Y0OX2lyNpxiTfK1UGzwAJao3IEYaw80iszp7sw3CLUyHYhgS9VtewtuvI4M7HZ0EfNEh0j8qcpsUcdr9gd3GPx5IqWxCoyVZZhr2kqjSE5oRiNffpF1QFkMOBf7n41HOni1ctZ8Z9k_2sOdvrtZ9JsklbgnuXXljxM9hD4sINo8gi6pnndJnT3_XHpu3qKmPZkGyyj7629w5Vml4kP_jbznNWNDXCA2m03bR8WMhX_z809o0RkzQHJGTCIVc3EMKqFuBVLsa_t3o9rvufmi0v-IaA9kFgnBnU-Tp-jw14tdj-HA1xMAt9i2xLU47XnrkiTj17Q_nWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgeCvQDXUqV4t7nwnSUD5t9ZmmxEKB8giE_k_ozICehLyUI5xrYaHdekgLW_ldOfAtXRKQnAndLIT6QFIfDlGXPreJtG3R4DQx7bqsVkn799MEmH3besYHKSAxmagPaEf0wMHt3ra0nV5HAb6deMbvTKLGbmktR5LgkiZH7L5YAJbPOEuDZkVpY4xvmk7fuvuFcpVEOxhR5BL_GlOlCGQr0gP8y-wn_MMzk535gBjvAJ_j79JO0lf0ez08XtftY_hJPYxBugqfCId3CmmskTESvZuVEOcrCO6iZVLp_TpCHh3b62_dgFiv8m84e2G9Msqa2O-ybq1wkkMnCQSkoHwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfpADtxMLmyInUbHc1r2j7Q-hyCBQC-UbCXNBWlsANej4pxiYwPrXO1MpUcIwR_DDFwvcu8P1UjGUrI0U0xsCRjlgPbbRQrSpqq8WyWBkaRqBJjOwRaSb-JsTrpapZhg-JZPLlGcTypgYtjNYE4GyveCQMujrQGsfA0L_lcwQa9waHmOkty_uZAILuAZLAcTvvLpU58SKAdeUgNm0yozpKJk8nEdxardr1EmIodulolsT2U7fk1QYImcnZrec4uv_JPCmEaH9czXJtkSVHM_bsrVHg09MCeSNvDIXk8fefi8N1dg_TfxBoz-eIngpXPVe2scgbNLGhyraHdp9k5U9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhsseIKcC1KTqaON2CJX8cUtwrC6PvBaE2z0HXnsi44GKk0IuQ1synkjLoJ9y3psfk7m3gJTPG0cuzhORxhY0kbjGf6D3fRXe9v1JSlbKjcC9v_UylM7ltjXa5xD5_Ch4ypFEHG29I8IZOwBF-VeD_320MaopPDbggO8pvTTbOoiEWwxEukXxWSbBBpITNHojDvL3gciH2DZ3tvsHj_eAwmHGKXv-eD79P4Xn5VJb9Q4-o6yxb1VqmUHdSo1cYkknjt1v4cT9YgMcxVG2ISPy6rLN4Zyi77oTQDTyoPpwevhwPqatNMTDMyHO4-Qe31I897NJWCrqusGd21J77Xaqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOJiiS4gKu8YHlSPkBqRt2gP1P1NrTtvsl7EGRWxq-K5Uzwe_w4u96D59OuHjXhXc4CvC_zm_MnAl5vrG3S5JcjtlK2abT3AnzvPlXPB4nQLQojVGInHumu1Zmvpgm1cCZzuSXCQanEQu77koox7K5q_wrtg7mpaRtS3mpjEARjLZ7yLHgHF7ig4LT3K1Si04tI7wQAox23nnPp6tb8vwQg-mP0cRli8orqDCFgvFfJMI672Pgj5fdw-W4WpzuvaolvRgTf2CetJcfDXXK8VOwPyr2WZhBiWbSJuJ-KtBzvIaJei-V1ZdHHDlmwrEUrXNFVKWwQjO6uH7juMp47A0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tw-9BB8ZSG3Y4N6mOD_zfHaulvQOAa285irQTpgUM38ax8sTe5cCdWgdx-s2YvYzLRwosoMS-YB9FALqUv0UaoaIUAoSl1oMEUHXA-nszws3y8WCHyn5NF3MNPilJmVM0SyS7yZGNcAjhfaaJUulWO7dpBZzQUPXWJBUqGaPJa3ObNo0kyhZA1YmbcRZZn5sxcR8QBpu4NsBVX7-VXtPd9qa8HWyl_DOGz4sB5Iay3jY2FBLZlJVm64_lVC-Sk4K1uBbIwnMJy3Bqiy_7-ekL6yyvmzp7yDqFBdtGlQFvILPqwEp0M6curAdJpNuCQknPKdSFIVvGVohOx_M8QIFBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fE4fe06o4g9ZZDS8jEdTJkM9Y1C28IizqFQAdn6sIrPQI-Eo1qoIrVcN4y20MoVmkGwqVYzPu-G28sC8EV2RHOci0F_vxXv_onB-1Q1dhStwmfsWjUsJ4PVUe2euzJeuwSlV-NlUnha4RINK05ONsBy7yMDgzQEuMUr9ifYKTV-drUqUeUqbBM5e3WKx_takcvCZGkaVSfhMJLDS8B19TqM90DJyFDnKHACvFn83KSBLHCtbhjDJbn7tLwWsZcFoGQ8AO7Lj1Er3ESbIlyy8YAlRETkYXr7KkeHK7JIOjZbmBnt47vm1ia3kbQUUPzXmdmS1UcYRR3yGW7_KTCfJuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-yInGeLBsul1UGhfVxbZuxdeo2jd4WHqr3e8icmjC6JHkyfzweGjdMC5P6RP5AzWC6hvOMPZFvAT6zjouoDrDwu0cC78mMAS1aZf1JCOp4kxd0HQJYKKQY5VsrCryxGe41Q0VYiEtNinHDzohOUZvmRHrSsTZ1d96N7G2Lit2jX0axXIXCCMlRcOFCN779vosok1AyoeIUS2BEBvPXbNNWXihwowhbh-9FuhEXVRZdlCl2yLmKhS5zp_P3GtNyYJxfICFQU2EWeZmimywxTb0-Rdnqv45BrpDb1on3kpMppyUaIJETVyAN6LJzvNPj1AhVijJ26uOrte1hYfj0pmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-GXRaCaIcbV9tHDQQMssSznJ2hI2uafYewJpqNRmXI-1INwX7er69BaItuhm8-78b9BSapuOWwlNwcO1AXLr6DfDxT6kjJRGloP31t0YfF0zptw0nqhpMumC1eX_MIBBJ4BGUHjXmQ69IY0uAqSdtPwtDVwx-pFFaa2XdhtFhCjeuCzHlwvB5h0mUcYmBbViBc8hxjbucdI_qtqabXd7nj4q2GCF-Adal3PztJFJq22Q50XnGvmZeQuk_DgyLi0FbDrnQq5qWz6iUMtBo9fjNH9DtqtLnvkWOt9T7wPsPxu8U08crIe6l4RgLaTtg08n8cmrr-sjBPqOt3lgIcDfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TjdibWMj5zGs7CfB7BYZOeGU15yxqVEoHtM_2Tk3aqNKiAZkp1MmxQOrDP2ZfAZMg_wau6GIWFDGdGqVgfbpPCzH_mUngt4Q_hmre4GgSZCAngHDCd8H_2D3e02g9179IyzktiZIQItkZSyxrUvDSwulux_s5bN7m2z5dvbki_G_8GiVJr5UoaiCNqxRNNoqMGByPmsObEXSpecANnM_IlFCcrrgVVuu6PrmZckk8rIsE0sN88LMXb_gJDuJl0ipfL1udHQ7_UKH6xf60YNNhOB4XIP82Q93nNM5GpdKyFSE2_dx7cS4FOcaPu76XEs3LJLcqn-12BtSBaqgSFM0cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4J80CPAz8VVOZsgR8UIuDjNq1TfdRdGKBZuUdoAUT8gvFw1aF-HWHXErCkPyGAoMK26o9BBx_x6YWlyCwNXi4LMkT_OSGSROcZOKkLzJTMDOkQ_CB_v13tBEpTWRx9hGrvc6Jd4GmJOrm6KJ1EqA0TJmkFF4BD_ZQ8hkMYvd5jMdXXQ68-UFPsAYpPfJlR-8MrNr8PCBSEDnAWEIRvVGbLFlynzqA-Z1Wvj63DwcegpXniQwxlW7JkEI0nyxi99sR08a-CLD-XYQu8igNMzV_jmkA9yLlmUrVksfESJ-u88HKua_eKxILJh8I8wcCeBOq9hvPrPjH83ugelM2Xl4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WuYmaaDXhxUmLx7mj0NhRHmDhtqpE_9RTqxbt5FFJvYsehkEEhKqP9FxWDSRMyqs9cod20qQ3nYdW4YOay2l-sADjFXyArW-2T_6gvjF5LteRJaEdjHeL37geHZfgD8bkayFrOWXJEJWjBIje4mKcXc-Lw-EFZ8oZmHcurYxkUtV2GNb5IJNmlBSB0TeGikHi3mQaFynTm3kWe9i4RwwX0g1ZhBVkb6byjDQGzstSCSmBUQppytsDCMm9kjq72pyvwQfHLlqq_I8WFfmObjsvVFJzYTr0B92pzxMIQZAvBQE57t-sj0isJ__o6vmvSrQKCQc2G1TcPA3FjolI5t2cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8E8bW6tK9HZzPHjNmZVaffsXsBbzoOfAq518_35ND9_SPjOiA23jgNTp7QYPt_wb_RwjPuxhHDXdNoDAzs8IRXVK7HLJgjqx0-2CO0RdaizUwhBPxMA7M-gwZVOyWJ-svEe40KxRoqcq2mmbFHa-JqiktwYSTNYfHX1bexWLjULEdvPANCpDz7ws35rMRKYKqfRa9VXPQrnBo2AC4Cn8qs58Qp1MMI7nji-IueP2FTM2JUCuswxNGEEB1PS6q7P0KcyXgAKrL6BTxeRD5E-KWtCNmDceBUYgQmRQA-a8zIKzwdyr0RxoZx-Ruk-pbehgkFSdHtU5GXkmdXUYQdNnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eYSUFFE2aOeTSKGvlLA4gB3BvZJZOIbKTzitYlnH-Ud1C8uBhsdGcuMxZ41rLt2AI91av-I87xuRFb2O0-gvKQHXvxF4_DEZnSGaFVZG0tljpWY38KD9Y-lvEldxZpGJzIgB78qK7BkQ73M9AHZdUYGmWGIdrddL2tCJDx6TQ7-IEbo2FKx1i_-SMurLGVSXA0Q3bmFOMlxE74kk8DPuO7Nmd2g3vIXPQ5AijeF92V9wle3u1BohyrBM6tLfqWzFlRYZ__iUEo4dF4dymfS9DgJ_J9Nzkg_nzp_t9uyN-31OwfHVzHmtibVscbbtqJF2lr3J7kgfPA-y2t4uduQkLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QY_9G5n0zpUyvV_Pt1rrxVBjGmjIn1V5Wx36Hq78FXKawThSTWdd25Yr9lbtq0qx_jlBRQ2K0g4FmQid053blPxOfewpNqGMO3S47Au3OWGP_UDkCBPvWL-5lH1_A_jG4paBKxeTRNhnIRHK6hMZmVhJViow-xGNILBnbUvSzIRW0Rh7oMOjn5a851Y1LMHKAVwKaLwrHH31Jn-r4ugekahCLWqBbizSGCp7moJ884SvFOr1QVPDvNTRTFX1plBYGsm3shfIJZIfkc9HO5aYT_yTYZ2MVIFV6ZKStenYd9xnzrU9afopqFra2Bb373OXNeXAqHuh52rKYPa0Wwz7KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kyeln2otPum5aKNlVkGc3c4hZEiKn-WV2BCxcud17qK3mGwG__xHTevZxJNwaDKXjaOk5xrRIS3hsCukg7e07jaSCS7jCdtZSCuoVvUuxQwQUNoSufPXneS63a-bqeYcaq_EcdSniuSqYwWLzmfiWU58EjU0gmzT6n_Edd4eK39gdPShwsyGIjQhb_UJqOee5k0wsos5RQ_BTxYST__tYYzspNZfhoeY9EuwRUqaQ_SBxstGnGIjbjb9XglHnrZhD72u_BQsgQkd0ElVgx4eE5NmI9gMhoNmXbzvUNmhgfFuF0brJiz5KBUSjrh7TyNaJE_ZXSnghrz8YcGBMPaNhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F0yLmVXunWyLyS4fQ5NXW5d0YOoeCjiNagrUTSSS9fbUjBtORMyzahXuipOolt7O13UTLpsO6AlHhKKrOuCYSXR_OvKI_z0AEyylofZd-uMyCLUtH-pit0LzsGI7w7mMaqb_0Quj3EyCL9EVr0Jo9ZNb9xOW5eCixzyZwOGJNGUGwnURfgQevHRJpVMi-amugzdtxzJXp9K5-kn86rt30yzYVXXzhZ68BVUUI_W0xMw7d3lw2gPyE795sHgzdzVBZOxgM3bb-c0ANpdg9vwklBcAh_pgqgjtFrjf6DZG5HENgug725JTm_mwVy360RmsVfESxxKl5udPs75AHWmR8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=uyjhT8nWYpGBdxz2tPsjX3ve_vak7I-K66Gs8PvX0EfxeRKA_tJW_4gUJF7mkrXdx1LGTezr8OzWWhhK-WJFuA8LRrKwofKOBEkwnPvQ_Dfw3lM-Vt0owNHcJUUuZmp4LcWK5fnt_uht2NJdzhXQacE3Qj3Ru0DT2QYr1PDcuCqgm7N1XLDmJtdoyex_7WGyt3o1FSQtwqPSU1n1a4mogzwINiG5bDmUr_FOH30oxVabiYQlUHppE2MSgJYR0yiben7Xe5_jo2HIbQS3VCl9AYS5p3JHs2rn1F-TV5newU1wt5lDn5ReMPwADqLATbABkOnkMQ_X6xHuQTrqtLJfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=uyjhT8nWYpGBdxz2tPsjX3ve_vak7I-K66Gs8PvX0EfxeRKA_tJW_4gUJF7mkrXdx1LGTezr8OzWWhhK-WJFuA8LRrKwofKOBEkwnPvQ_Dfw3lM-Vt0owNHcJUUuZmp4LcWK5fnt_uht2NJdzhXQacE3Qj3Ru0DT2QYr1PDcuCqgm7N1XLDmJtdoyex_7WGyt3o1FSQtwqPSU1n1a4mogzwINiG5bDmUr_FOH30oxVabiYQlUHppE2MSgJYR0yiben7Xe5_jo2HIbQS3VCl9AYS5p3JHs2rn1F-TV5newU1wt5lDn5ReMPwADqLATbABkOnkMQ_X6xHuQTrqtLJfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-LbxTQ5yLsq0NRUhBMr5GA8WbRFwOIuOPLLi6AHCnP27AIeHXCzb3MS0dlSQShGdd36YmrM5lz4ccin110kMrXpyoDwiipPp8Gvw1GT4OqZBoPQefWJhqeFiqeY4nLNSv7brTKHNA_gg6NBT1Hzr_vUbPoYte_K_hktQ8NHO7w8g43e8S2mNn7Xmv4FHXyQiQH7gKooVcwrhA613trVpvDFK71rUQ2uORddVyr32Ytwwzjw420ePyJqFCCUHhiapmlTrSo_AAmUFtIHgSVYiFbbSPLPOF1uKL9sw4Q8Ik8r-sK1SGWaoxn_NSOReefN3Pt5zu7Ny-ZJy8q1-nvXkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9uu0hs6KBc2xE8tbEdTTXcKp48tUGDHg1xs5geU2p7FjTguUywv5onJpcFuHDxq0gc016EWTx6M58UsNa3TYzawzXDwOUBAJhUIRe2ndzYfjfEsoNOiK585erdnKjK3XoBj7H-7mEFCuzktI313WD7AZdkG09vrf3ItCbIVUuZEZNHt_dm5eralokAQzVqbhMqYJDbMQESa5NUUwd0UKIHVlf8JYH-THEBNs9QM5KEz74fzCsPzkiP-NiRth5pWfUca1dfLmk3rGQxWBh918T_lNhtOjO88xaYSbsBFkdcRYDYFImFqbKPFRus9Lq78caX6QaUcUCfSCpBQhmepxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkdiSeuuJkFaWT8L20TQjffePhrpy40s2GfShvsH0EOie6ciPc0bBpETdPeL1-DaoG-aZqVlLAUJbgegQQvd80vDw0QFx4TxdGjF9WmJCYVDlvrcS0l3eD_JVBIQon6cSA17BsnNfF6EQEI3gCn6LIr-2nFPlEseIIQ3fsYi3CVMIXt6DVGWgCroDdC8-etxJmE4MD0d_NVjMo1If3z-DT3FVd9EXsZNjkeYh4Mq3CbVwKCqeFSHv_k4N4RxgejmVv9RKGcn0UVaBokxKYtOP3ttLtFrNey27ZVNViDsRtc9pbJI1TzbDiv9ELVig7CQTSoQ1tHPzgt-Tqd8CL9AOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nq8jDoL4ExURq54wZcIJt7Y6bqbkevj5ZrC-uKcEfgrhnR21xYGi2mclBqyCt_gGeDrqvMvcc3oXdJUevYDCS-9sVPHxZtmUBnXMzUZnrKlCC62hsyzQd2IJEuE-97q3XsaRonCtanOOkyYsELz7L5s7uOezhQj0FRDj6CIoWUJyU7MufdbD1yt_I0RwvgLiBsAiPBRKnCG6zWhhbAK8brlwcg11_su6xJd87PLKYNJ-UXgNqblNVC0gZjmhpYR7mo7CjJ3pRlI9UZd_kkKMh5ntlOXZWWT3zkos7XBqj9hs8mxnlC3GV60IHMbfuTL_f8q2f895ddqYyLkj5h3HSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYjD-zYCtzTBQ8g8YpBBCkTfkJ3n_JEZuOH70n2iqBVaxzfMn5AXvFHij-hqAcTOXwX6LvPoABeYrRJ1V0uyb26aOdQOl6gL-T_lr91yL0QoqKCV-tAczACSaCybkkHPfBg3pJd5zo8kXBi1Q-mpPKtvcf84VoMg2feBeHykEpuD_wikkvWIe2AJ2oADN01feKpaVRfIlriD4yf3fMBHiaTKPP5easQ_ysyWuxKNx9iDgccFy346iXVfAXx9ZEuViu9Q2eJK1dBdnCnno5NTcKlb4brT3SRjkIwoBxUT0r6__-6_a4pMWN0kmZA406VcHyN3AYdIUrE-A5H7DPxZUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIcpAA--yvLqCCceJHXANFUQ4T0byJWms90ztsaXOj2BLECH_g3Ls5yG7n5ozRRKqOWyraA-e0ZPYFle0B7cHvbcT0EAbaVoe03iwi34tRhDDjplsmUPzyy89yQzBvM1XRbKnYgEEOsPnBqURiIWiLbkk0gWPk47ayJBqv477ApU4355k5r0a3Rdd-JyyvRLRCTJ665yJs9USVq42jUgJ6BJfJbg3U8VNVpDJDUacnrxk9_AUPNXCaKlwjH-fLcaZVjYqO786utpsda0BCNBJh4HbfoNy0XIMqOWqtz16qGqW_wYiRKz4h6aqcQNRiOZS_XBWaQiISQbmuSX9vO7iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUjXwCfCcfzk9Q1VskUOyZBob8JxNi2gnsmYhPtro-4SeXUIXgecrbVJ9kqXQvV6yA5ulFpKEJYH8hN7K47sodGzm-TmrnRQGlz8Wvs4GFpTA_W2AetuQf_IjxqibhoNh-bhKV18Q_KKoFAV_84fG2GhWlu17ZLJWk6LkqsePEshIqPCWh30eUvjXE9oUbndv_5bLnPLQH6EH7epgr2DBnqTku_YLWDUCHHrBpx2ErV1BJkG3GFaRRCQ6C-AsYBFZh-5l3VgdeLottAxvKNm3dcAN2zvR7HJeOWOc2upPzNe_sV6TIVhxIvNpr_g15bZA_i0hGqvVD49noaXN-y9_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BuGRM2URMf-CO2zzgHb3z6OG0Q137TN8gi3uGhuwUSiQHQ3VeZdxwiOwG7O3YImibk9sf086P74SSomq_KPeZ1s_5NiE_RJi48hMY0ar1PsRLbVicN7cWOB1lsxtk0Z6E7XM2xOyKzQ5EFHi9sZiAZOQCzstaSY4BKz9oMjQHbaCyJL_imrhkMb4QAKMJLoCITIyIf37mr9LZn_hVjeziFL7g_73Q9f96AynE4Me0NuQCkuxpTHDjJ4K7po175NpLkYDe_oDUYsjOMmO3r-HsLP1mCTpnSKX0_sbTvg-Zcq8yyWAqTF9gvWBSbuhz1M9LRhg9YmAq_mg7VpUzXt_ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YANnzzbVzHY2DIpcfVyb8-zgSg38zRDpl8-I6X6v5KTv8wSYt-AKNW2oz7mhF9OT8EL4c8PMhKncpKRC6z2vIrvFPqWVxGV9FdOZUzJRZQhTxoG9WlUc71Pnd3HyTrFjJFYcDhXqCCRm5Ch7NrF34-Lq9HFPrLnF-mO10txae8QS80NBBXPkm1ZnsNJM_bdPVXHyMaH20gTX6NBlgMsAI_jfIR95fGPWPdW_K3svqBX2cPekj4Qa-i-zzXIhrDRylzxaix7mjNh4ZS3agU6OgDfzjXwUJae2uW7SDaxsI5nKeZnhq1EceELq9Ldcp9nZJYpAYNpGGAul9pjSX0Mnqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HEyVWO4WtFHXQ8TxoMUFzqHsMG8bEtcALdRvJ4Yfx4Qg45lfKuaul8vbT4gfSSljsQmVWwb-O3DaQF0ZvsoByEomkSfCtyxBC16oZyPru4BYKozGOC-L4UtPg2fBhHhfSvRduUDi-q0su5rmXiPDkqqDv2WpKc5pAZC6sxA1pch8OOfTRAamjrHHQWU2w2KbkXyEh1ZgMslLPTMUojhkw3ENaEAGHkaXg8kXPvFNAgT8Kl_ykQiYReUyFrCP-X2vBDvi5WjJF3hO_bAs5QEDFOqbhg-fxJZ1iDwVeG2XCV-XK0S05B3C85bMW2GOBoXth0DpKvMDUDyoAdJ2KVAsng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRjgiUDAZPE_KwYcAm86gEKEefE45zY5KADkPq0k3wt6K6ThjL8xhlwOnbLR6dGxh5bqdfIMuDMZUMkfr-JbRhVscMM1-RTAMz-qIQy65iH_bDXM-Bx7B0c-bjDuMDfvldAZqfKZWmE3aMoXaG1Hz6sCOUOXCxMELsMOICDNpfkBzpve0X3_z5Rc0BWZtpdHMBnlF2m64KyAdaTdQe_JYHLln6JWUfEHXKrSjZ4bX23OlTgdgGDuUmK7hztybluIr8y9Ypsc7nYlAuKyKsONMqY6qERFURzZrBs4RTtWxV41ZKpW-Tr82Xqot_huf-Xn7zm1wXqYULHgOdrbpa3o8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agVhTegtSjFq5kzDqYozacp12gdae64WV9RGWoZDpMr-IyexvpwuK1vEAb1Ud0Sf3n77Qv-nrpzB3f_PR2jFr82VYyP4WZCY_3KJ08pwzzEhLZZ0yWCQDHO0wUhDN7vyuaZhVFzAAQSzY_J0P_aZP9K2DmWdGa5Y9ujvUPJ9eq5qJ3O5PWO2Zqc-PR50TkY0HK9__MqpeuQpyf9mqWsNCKRCSr1-991Y5eSjrEMnexEosMMZxnIbx4WghMX4md9gdebmdYXRva2hMMGwz2odEHfusoCJLFEiaaeVGuj9_gG98C33Ey8lVPkQKzVcn4G51SAQSGrCcqa4z1Z6cVYwgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDTrja07oNla9v956maEfFQbPGn2F7E4gbJqTKH9BBckbrJPIXRlhgKifFgozzTK3smAHCloqKg98KWi2rkCY6MGGLTNFD30jNmu_zlJaehF_iy-Ru9gtTiUnOvO0Xq0fV9_z-LuactnfQQK2r5EGCevnGSJAFAIQlM3Gq0tJuUQtdglAdJ2dFynGiGUb5PC4eXnTIDWzfMuk6OokmL0J8n94To1n8hKxBgJ4L6gtzrxyFP9z6M_Ryg8ghLCbA-hwPboa5xmqi5hitSe2lZCdqH9qfh27uEkQOb8qEYYa-D6A6Ir2hU7tRy27V5VumAPInjjeYB7M-GxoTBzcdkQ8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4j6KMG8akbB9Knbyjs820ESpXTe1EkRv7HO6byn-yUXV2ke_XUOFxa1Gtlt1LN1u2ukThWf3tO6rM0a0icGOQottihJSC-PsZV41a1i78lAjCaFO4WhaeTUxpviVvUl_FapdmcNVTlNCheuVVdGhJUQA1j_P1ji75LEAyN5MQOR8WBKug6ZM3uW_hvC1HZE_JQVHPldf7lzmBKv2EK0VNk4BQZ4sM7DeiLRE6Xkd7tLfK5hxtioodqNlbYJG0VQc8P0Fm59On_LJujD46OwRYv-AkUMZ-Pal47KcJewFBwMkoZ75d58LXKVYRH966rqbFwI0TnaMndwCRqPmLNCwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kK0QHFL0R-CIhWarTzKQrJAg7GFvwMIqV5d1XjY4Lvz8igu0Z4cntxsltPv-mZAclRA58de65tuUwFbVIJNulF7tG71ziJg2oIQX00_eZQ_6Ow6vglI1161GqoUKmk4f2FG_A6k48PadsDrTZCUiXqlMbOdqAg_Lv4d9SwGGD3IMW8UGrrJ2hthsWasjE2jgKrS9oR9Qb2BznOBemgIxdqUYtTPeVGxBErfefHJ7N3iGy9AoqfdVI0Ttw68jwJkCub2DrhC3uwvvtyJg5KsnJ_2NczD6aZCHe1NjEwu0HFy7_dmFWqkrGXgei37lI4hQIshSOoxbhTIpvMAKFc1e6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHPr9IIaaAU197LyXJtzxiFQmMJoxAXG5z89KBJWcE-O9wp2geay4W6kUpGaC_EchFf7rxnPoLzuI6lx0T05wVqGLRE_OzpaqhI43U5CS_-z3Aet7CtJLZtupfb6HBWsuyFMM2EahOSFOvznpsRGhCe6eUDR9GgK2c1YKRT8BOynqGLY32mAcImJsrR6Bd3NSXMsnrsRrYI1yraRtq8B4fyuWoZWeMMViGNiNsMlkJZqTqPtlPYpgHjXulEjXGM5eJXiDe1udNiIFMoi0YHSE0WEtPP2J0imEiqTNmdNChJTE-3JIu6nCJEZ7tjpRmpYwBsDCN8phN5VavzkHyG9HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDtU5X3MOwhHRkUX1Vr7IfxcxIXQS4xkjlyfVEufDGYNPAuOFajcpgzP2USwAE3VzMesSstdp2wVOIrAjsTH5dYQSNJINvY_V38WGHhYat3KlLBXD-NxAzH_i85LZ-j29aF6lHB7F36x3jGBji9HKkXs1MmG2ku2pwgCzTf16h5Qynj8pgDbZeF0qwBSwJHyi9eSrc_DK9LpSeIHe3mabRd1f_4XjOlwdZ59qjprbqkqsuRnt5-viwokz2ePW1K3uSyZ8FhJbcBQV3OxEhZNjQ4p-XWakgP1UsTZrV_TmZtacpdAHk0qz8Gnwexixhg7Del8A0BtbK3vefF8nGkXMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SbZbbvLdVG1wTsxmcFVOy2KOPmx5UO_KFNc62Lxh_o166b47JlaXorTRCP0ZiJkMrV1oEV8bPgJyFBvHWIaRv59Vh7SGtMJD68MD0E8U3jmDRPM_XU7BCHVGDvfOCZ88sS4Cjh0iIM1ym_aSj4K_i6-9N_fEexTsdhDFFQCm4FNjBrE5IObJBnK236jCH-H5v_FN5ehKcVsN3VetBvRa6j54mJCNK4T0rfWd_7KhVY3x9If3Pzs18oD_5-69eHKeT1-6Ot2VUA9NWl85emAKe1jJJ6weWDb7WOQ5na0-NYdsqe6GApCzRjeCdnq-_Qu5kd7LWcX_dEkHKvX1EuILjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6Axf2nrg63SM652csf5Vo9x5cVOQw17A6ago3lYFluPtR8Hh5pPaM4gh83OxsVSVASxNPG8zoCDMoIIFJNOOT9i9sWLVqAS7r6GvzJx5HUVJQYfQ8o8NpIS0AK9TWhJKCCf6dhSBoHyZEG9F3hZI_1jBI9QtAuRdcm_LCHu2h8ri8cG-u8HP3AR5tjFivARPI4jQmNq3R2JHnqNeRwm8qU9bCKWj2r_VOmXRZJuxhBZy1rWzYEuBDaKU68Fy-ATlEIb4oRAvPfEnDoJikDj7-McZUZLSBfFCr04rgGeh9Vr-s8ECLlnj_qhC3nYR7w9LXgct24W6dsBEmTHBNY4DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EC35z0wBmev4MXOSdRQG9Jwq8P0IRtpRtW_zAhvMxcWot1vi3IavCrni0ti4RDYyhQ8DLSsyjvmukC0zALDfxntHlAkC9yTa5dzrZVVTur4FAKwC8HRJtt0TjG7U7z1lGnTCp597uLRcXJJ85Nava0zP3PLxbxigCC_J8sL-NKqvdnFg2mv_s-4lXq9re_BlMljTC9qpADCFhgzulbQSMHht_E6KoqRIOjx9oDBTMe-myoYxC--5MNcsxCKUUErKP369KooeZCnq0ITxuBIV6CkPgK-MkeEQ3NPdX0I7Rcs7h-J-ZOKJzeZvMJMFMFfMV0V7jTYyEqFFeI3dO9IBVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwl-2CfKpYElcXf_iXPwbAb_hBybQpjYVED3IiLFIq9pFIlRomO9nBJEmVE9IHutQknj3M-QreWlilrguztVoxatvy67heHrOZLVxwemp4t2TsMCdtXkgl-tsOOWYiVK-m89EmjNWbqKb0OlA5JYsRsSvwco4DeVEucw8IZahFKZmJnSYUDI8QCaSCPfiuf9JggWzc73_zPdm_Ne9qBe-hw6QZigXL1iVTauHhx2VjpQVOgCRu_iSSrIRHTzTfPkAQqKC3bANFHKu1fqTMjydFzuUtR_fPkTaZV2RoUV8KF9O70hZ1ONno0Vxb0wAqz72oVYGBi7QwatQKiCaZEWlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n4K5oaKbSw--gZMtAMMOasNwLAL6Pdxw_dsrIgzyghKUhliLG0Iov9C-NhZim_QbWvJ7KNvk6CeyPgYZDilcZYSJcRYM-qJAnQBkuGIxKqd0xySnmeXMgb-DGymvu1obunEeNVMzWiR5_herjR8fYFKnJ85NsH4c1IJmTEzxfTYKARMd3DTuoNsxqMbhppwZFuTqGR7DFms6AI14OK8dneE1bj2q7jMXvAPqUs3FQtqIkr2w2WMQArFzaAvENyBYjwVqr4-D5ed-7b2K_wQ6PdY7ULXDBEolBTcV3s60_mfp0U0BHdhyecz_x-aGSM8Dz4KFqNrx1P_TZ3MkIbvc5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7gs9xvK_x9PKV0okv6QOQKuIYygWO3v9-wh9imTdQXyXZwl1Xrm78NbpeqssnM5u6vRPRGSorNxrWwtVhqgKfsKCBWLDeo_SpPudDWlKq0ypmJpNYaJYKwD7FhoNSPCbnK41UjYu5Kw3EQWwtlCXoIrv0rkAV8bnUu0luqiP2kE5k-7t66aLhDzoGsZhqtJ2YJ0oT709x0A6-PsFJyui4ePq_mQ2HfdSjpsry-wJ9MF-dWbomQD7rzer8ugi1g2nIjy8b1X0mBtP5cdK1x1py6XVq6ZbJ9LRDRkS6fKPjHtV5NGtSheY0i2YdKjT79HaDeVBw9mTyQzL3pmLr9sLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BpitAa5M_5TgqupLBAaRye7xqPd8IhGGQmA6smz0bgWp-SCNBlu1N5vz99i8xeFLMqiua-bvB4tCG5FTN2un1SczlAe5FHNLxlWWyPkp_nQsmQ-J5l4tquLHoYRN7lfxGFkODIS0QujoKSVen2-2QhyjdnZjFlXEjxCMBircEBhlh99M_73Ff-3DFyWVerpo2TQhZLJUILdGPN0sceJHYkZfQynmGIw8uMIengzTkOIwD5SEwuS1kqCUEyIBmWAQmLEqx-eF8djgldYoX47tsBnr7jFjKAFMYGWmxhqSFjFk96vKkIQuu0MHnVONUGakB7V3z9z4QcmQWL8aZy9-gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYrfy4jO9yed8Qi4_fbvoZWKLuy5OgfeMXOkj1mMvmLH7Dg1b6-pScJPImkfR6VPYkR1UqP_K2Rl9Q7bHeazaGdSwGFCokEcWlfAzA1o48LPCei9fDKJrPg_bjduI7hMLE0f0pF6iI208Y8B719vg7kbyQSoABIh5ltYbFBMhrhYp7NCWBhN-HEb-m_dH1j7dnjeoALLf1by-CI97Vx23CtoPAHoxmqUF2H6Ndvfy1EuOYGEuUXnziGv2gkCs8YvkShJP-IbZp9bjCCJ-CZ1cKHmD7rlmps26PXghvs0bi1vRRnxpsWzW1LEqpcSxhGyYQNMOxBk2Dl-4LKOHBY80Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DvqxjLtQwSDC1Rkl3mEGYtEHBB9k8ivHsDEEf-VQ9QcUHK9RaxP72uoaCLCqjUG0UcK_2iFGXKtDf2CYX-B7o167vFx9zMNgf_VgV5BVx4wCk91TsEdni1W3f4DUohVoFopiR8LxeU-TAQENxnxEPtQuhsOZoVL66u0wJKW8aJzP_tVvbOmFpvuyi8iKt6S5Z5IHhbk98p8sQcscN2sZLLoIwGvxloSJTNwqGYln19q8J96tKsBdubeydru4GnYzSkc_VZsuKAOpFERc81XybU5caTt2r77HefV-pxBxSlKdNCRzCjAuNVxKM5aAlFgqPWSmbUQX845ny7Qvn2UXqA.jpg" alt="photo" loading="lazy"/></div>
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
