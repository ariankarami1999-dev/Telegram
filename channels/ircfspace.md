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
<img src="https://cdn1.telesco.pe/file/heOoY3_McBTL0amQCrm4SV0jPgq0kQ7GxhNBeSJJKkaqqSBw9ekfiy9PFyFuQeAwAJK_EEW8BJYuu18GCL7cLznA5ZEIA9K8IyymRUtZQC0SnD8RVlPRE3oKJoiurw6o8ngsKtsLgy92ObgRcRgkmHAF6IwT5DPSbZcLuvvAm76Tq8IlPinCLFAjGQQdbsTU-v80gDsA5U_KlDARxs_Wfs1I-wYST_mg1oouBy7Y1b1GUTl6KR-QDbG-k7bBaGo-yojAiOuIAQW797y3v51iSefwIe30m0KDpikNoM3pK7ap25nmLABdLYIIro77pPXcjHTgocdYWZi7stZinyrk_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csZVdT2aFgwls_Vxg6Ua-7H0sn-j0qOOnZI86slf9XUu8pSF5E8IjkBNsfE2QJhTZeEEQa7fGV3cXWZ3q1w01CCWHOwfXHZZ--J-Qs1K8ZSfJB7R983KoF4662kh31Y3nQacMUv8in0TBJtIQ82znJFkG8ADJRsxhULgXEd_lo8L9vVEFemvFHKqqtivslmycnJc9Yt5pTA4yceh9jf6EkwbY6W5y1Xd-fB4DDNr75AeZbJwJ-LE6FlperSOzp7-2RQDqcsmlz777wmUFX07Mf-adun53QVM6RxZ_hhiG2ybDIUVCRTRLnZa7FHfxHCr38mCabsNMTjHjsAtJmiKOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXU8hy-wJfufIQwTwEtS_7LOFMzIH-5MgWCSFAQdqHaALc7ReN_o3e65Lwde326WgilcVvyWJFiW_4dKbo9rwKhUPlQcMTH7awzqLQSwwnecBKcgfjiZKuykNe7QpgzG-hqfSXseKPfzY1wV6Li6oftZVPBHxyJ62-4K4Wyd9WyizIN8T-WODiV7yvvlF2c550HYjoBB0CdBHNDvfDpEAhPZsSM7GhfNykq16hu8yD5EOFl8CZnUeIqcB6twE7QQ1evslCIwshECfirAgMsDg9bi-3_tI8_W4Sf6Qz3EFrkMWsPAERY5EIR-bO76dUxULKCEwzRR9MrS7ThuSt3AUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OaTJhbnGfO9XvXCK0MR9Bh8EdaAAewJSu78L9k0agCT8Bxo759vTHq_ui1dM6xhfHoqSpoWofT6GtJ-yYcLr-0L6VyOKkiKzxSIYWWtB79w0PmbGKjbN1I3rxRPVX2wO7BOaV14jBJAGVr0iroyLSzTnyXq_WbeCfVFvmaMGA-cZicMraI9MXZ_HU_wjZsdU3H9Vz1UWcgheegEHRMJIfP1N5WF0-znXh7roT2zCHbWMC928BhWcbHSVN3SOJAx_o-f8zx7UMPHjKSKcVa2JQZRr7bGnPSB0m7QCl3kIXuX4IrV7obEYV1jHlBEUlee9DUrUGKLjotaPUCghRU8yXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NkApnw0Ww05dSFI48JtquTXhdlyqy7l2zmtFWEj-qWszXYhGZdaZy3EIlm_s1VQJd_aH3JwxO6hw-VIQ6KSkXQN2fWsK0vdcCstPbQwOpZAiGDkw3OaC6n8RYZBOyU-Kipilu_1nFsZsJLDcksu909yvdcabKEfQ86B0VdTMK50hVTQTCF0pVCbZA2FUkCTuoiyW9NgYYSzGTaRC8UJnreV_6SZh6PG9LCLu6nH_txSOFMBluAmPUayYaBLpI5Z2gIPsjs8fAO11t1pDlMdwk_psGpBKGdV0A0OZlcLhuRfkeg_eCBH5OZ2aBsmgxHBMtUU7fVxF5VE6ZsRKzhXAfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-HZeGqjMefql4DYRu7nDdb2YDkAz36czlT9Q3dWSIWjxIG6dFXcuegHRRE-3KCtkn9-no-l8kp1Tl6JXi1rTjfVe14qmfeFjAUxyILldpTiATgo5EKMtmK3Xmg3bnG2JLw5aRxgrstkQsdUQReME3wNxEZtg6ebJbqeP0gWh1gqAkFY-ihWZO-_BAc-0DmBJyPIrHR80IrT1Clt1xomLFh8gOHlmSJS5EHKk49aOYz89g_f1IMWojNk1RhFdgN6eH-ode84RGZgNHXWzFqPrGu5TndFPfsiW97EG_dUiz5Bbhk_UuGYzP4NzLLF-9YIyBDuYWmH6Jw73zcbuIBVjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8oKqryQqXdb0APeK1HJEMOi6kiqXPynZs6UsCQvk0jniwI28BMk4_EQko4ItvM40PLEFqTJDGBKw1G94jl_Po51afuyCYRJEvrz2tqdmBwniU5g4oSz5I5gcEg4E7MZbrLu7KQIuq3kayRGwzNfgQ4FVOV5yE0MQ6B9B3lxPwdKQtr5SlSW3u0yx0U4NotwNrX5NpC3fGvtzH1lmtCEncxJ8J4eGaWGoOUV2C5DczpXKSOYjNdovI6NS6yNDEK6u14IQ8gPEFglV5rfoucgX1T5QWIQ5l_bWzJQGd5uSCZ2I0pn9v1JBaSqbWMT2KJtfgjSyqsUiQmZxBN_Wd7V2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuBXOjs_X4r24dCUgofapmal7o4Sk4S6VJZQ37pxPXPJmirXEx9it9hcS2I38WWwMJXLw4rr5uFmVYHuF_YPR7iXOoIguhHmsckoM0gZ-13igJ_ibegpPGa46-TYnpLCQ_lnkB5vFKd98j7nkQOHJy9OiWE0h2f7yH6Rh5fHB6Ed-K9N5D0TNZF5Y9DLR2HfmXJ2GYp8cHS7f-EBslcm5rimAOWO2V1YRwTMQ_Npb9VWNtmWKqtD_DzyNR7CVNnPN3R-gd399rMu56827Ckr3exBECJ1K582uML_STNB6DzWntsRDfqzOpML-MtX6203GcqMYfc7JATAivghLRMFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0O20h62CQH_lXqvh0mbuwcJDEbGsIspn2QlZaRobBzeB_WOlDjrwBXFvnp7jMNYQm3xG1aNQ4g4rt1JuoHmfe7wDghgWPij6KXAKQ9rLkcRFR2tD9z0nZw6KbsNSHtw7r5N524aW-SzgByiMqfjnEn9MnkypgyLbO4nzr7_5rl30CP94anOT1Q5TO5OLqXfUfX5vGk1AUCYvAswP1__WopjImlOJTyEFaM7BpItW8e-egDnr1Q-7Z9M5_h6bzUT7J3PYGf0w5UjeZUoPO8LfH6fQxxEqLVgKPbqgbsphLiswEhuQg1VcMG5S-NeDBSlh2EmNuDlzHGSTD9Ii2DtwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhsMnoqNfs47EPDJYxSYrhlVJM_EfwaGPPtCHti8Rp83fvvc-sV8DP9KI8t9ygNd05MAOKkyLasoFqunnAcx-EGQFKZqwaWqKagRX0uMPzQyFErMPG4B0JHWY4Mtd7sANaAHk4KqaoH3x9bZLcFx6nMRw0gUHGiv1AflQEQPN4TzaSlvTR16P6sLgbsYL3I8a-TumuLnI2MX_PR_xCWBv-R0cvl0zwVKW0g_coYQYxDo9au_DadF34vL10twc6VD4TgJt_kYZe_Afg0V9DVWJ9NxKpn7BXLEFpEbUWTU_JyzhHs7kKE9OJdd_OY7dEVGyzTZSpbQDqDeYiuezxuWZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWPHsLISvu27F-tDi2kGKrH30bNuj76u7ndyBemTuMX8AcKPsLzgjNwG4BXDg7w2-Z1IoeGMFOwQHOT56CZVg0byrjKrZyeigL8MVNM_dRcwcbeUu5Gu_GLCZbmzrXCeac8DewZWwWZSerEobfTaSXD95S-FvKJoCmn7au0GnQ5M3HxOTTaZFiZ-3ck6yzu0MEZnqSDH0BU42O4Fn3yxZe7b0zQZA__bBuiqk8UAN8t7JzGnPVNglHKHNhTNrazywMB9mNNHZhcYrQ-ZIj0Z0KFZkqgfQjO9A4C6yqJL1YbsiOLUe1JyxdSGCG8gq5llWUeJgbRX0g36HlSwON62Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WagnVPyLZX3s6I0waFigqYYnWEcZiKRjS2aDLWyvcji98jO8voYHUi-akjldQAxul0qX_vEODDjfEk2StLg119c_RaCZvkuEfuKdByZpRwvOlyPBcV_HlBf8OQLdjIbeDnmBB1MVF_UCfPMykTXvhQNULVCUejX1jqo-7imBKHVW589pfIb6k67lT_zuUUfY_vIF8odWEiHmz6CZ7BT_gYSidIsM36TP44-vjE2mnu1dxXywwf8NzPK-57QJ7aRyV0_QP0KCRe9tHq31sBxBQKo1hU2val3zsJakWUJ-F6-u_PUCmMRdXur_hO5O_-LYul3wQsxdGl5dvwz4CDtw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c07TBlKjbThju__E7p-j6TOYytuT1lydaOAM4XYuOU_fY4W76Bnro10YerNFK-KAZIVHG_5sYuHy7eGTh9wPUMHe04_HIKCZRGMCmvTYLoVeX_Duy25wuySJ7aG4tPZn-vYXHcofbR9CjXLiM3JXhQX1j5GEmT1JskEi2WDAqmJEYwyo6BNhrgRXtzgQqs2gTrB5miPAx6dRs9lBKrT-PgWDhkFLx3-8R5fcWd8sb0CEJngVjifiXMlbKP1hHHuBzV2RGbKe5_seD4KI9Lw3-fHV_aHATSkSx3tIzootm6u9GIGHdsycig8WdrvGqk0MZVcqam_q_8ImsU2qeK7i1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBrZYp38hOWxien6A_htm8DrXblRjUohlxN2rMDTqTJx9EFo1nJkm0D0rGKWR94wHCGYFLKCWgDw1ohjqjk67baKPhReFVyXjvpJObai1jyiLVE95R1CtwRGaMOzNSEGFnEQWzmIu9PwbtLeVIyOOmBBp39LjCU8AGxtrGgHIAHXLvhwmZzYh5BBWSe2O4_o08at2mMfvYjzPCLJQ9yneXXj32SAECxQKNC8veGGblaiC_zxkt8f1JUlB-VX5H1MYoyANv5DKyejqDWlL2UabeDW533TH-KgJ6CjrysXtGVzRsX5O1Za59fptaDabpIH2wZg2dnybSwrPmRbOk8c9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ai_P3AIYVpzJPDbs-PAvZHSgZYk-M2VZqIrx-klkODumnDf2AaCHTDjvTb8B2CZlPGltjV_BoQcqhjsv-6Z8ZPvxFtUZB6feDcPl8BqiTc7KXJ7c5m_olYtSlNwoxWsrKKA7IGRRyG-Cinx6iU55xBDN0kXgCHjl-ZSp0kOCm7zzttehk1sOEB7KLmNIhtJ0y50wGZxNPjFs0rpwgstb6VA7eK4KEGQd-w7mpfgxQj0bHtvJBORErIDNBBmv2lYI8yQSqEdt5JosGutzE7WiyE1gAe2W7IfPlDLtQRzAxoQk3ceuApJ-l0wOS3jve_-Z8P4-9VaABr8y-xd27aILNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b8nIxQWvkXHwYQ016mmTZlqUZBHSuPLzWDG7xteq--LJsxG6A_RqIgxuShBSJvPcECL9suytuIlrgGl1XA9a8M1xmtEjUHoK1RdvjSS_Pzi30wp2pkfANuPuabd7EwpLj_KnUrtNsjAnZSWhJj-TphROV-_wLXJEFh-3uyq2-M_JpCYwjQiLOcINvv2s1ePUt91JPNTj0kYT4mL5l2BZxbzhNpyBaupKqcb5bWKfl80v4FLmGx95p86AfSE3bcOWbjn3R_yqz9EFebKk1-Mukqulhxwjny8nMAAyALo0SMk9gvXi8HBjODwo1kika-YS3lFr6CooVfsMm8vq8eoY5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eo2CBbetEjrjoC59VRsmNVqy-ggbSzERAeOzXT5NYZpp43oHzh3qAeF9NJ6Tncae6V0_gwkXrLPD6tjIGJVQYAKjOHDcmLblMtc1oo6HX7VFlV9XaWTO35ClKxi3-ZlIe2d5JtG7C4CEiyT9HOupmUoK-Q2XAOJHUYY_uUTJuXbHIkQomQ-RH99dcFq2YBWtaS0f9zgwhJMCDz0A3RkjtYsSv_pFqXUz0K13GVvSfZEjRM8_n2KOfZw-fgaIr_GZAeXio5sn-wJg0MxE--hrfNxlcy1QpJl3Dq85D5SouQYDBs96lYD60Cc-aXIbgUnEhhEgm2WGR8n2QZnUHMjbuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ij036FQ21RgNjLfJwRjF8r_nrau7Ps6jaSy-p3zzOcbNrSCjfTi8jldscBlVhZTSpHkY5G3pY-TO35VN6lkPqiq8GKtTC3nv92hgwc9Er6aNAXzdLqj9Qdri6XhZB1nd-lECv5eN0_YQhktawIfJ4Di5rwyG-y4X49tMsTuPsruV93pLbdlHGvBeZn_8e4xLPHKvpWvEVENpnSqXwWUboieFi6wRheSteDk9FqgeOmC6yfj3lFV6I3faFjdwYqlSTdTjx7dchZgPkLCi3fzqqyxTyhMLmQ-UXceB1x4wMZviU4XZh-N8hsiFpXEewR0sxay6BA6ht79R6ASbkDtDrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jV7B8bUd7NO5hs_SdA-vCmjhE5RKxf0WXUxNFWuyp3NNN45BRgTF9tR0uGmg-JkTSVHdtUcSVToRMP6AKSs6yH1DAb8rEj6S-bmdcB8FJ57YT2otWsPnkRgDQwBTkV-0tUtPDDtUja8C6YFbZ8DQ6jxZ77Xni1JxUIdhQvK2cPAE9F9FCVQdfEHRs-Fe_VOYcFg4qbiu-iWj8op8N19CQ9a3Huris3hrjXbVzCBD7hEqW5iW_WkpRLqjjxdgpY-Vn2qh5apzQAZjsrcllVo2-yBWYgZfVRlyFviBjY5Y5Le8oOOlEECYU1rEvdwoILtoOlIBgt-hYUqUz-UxvGn8rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdE1p8FlfAqp6nKw8NgrkUvcqWTP-XNIEy_4SG_Dw3_cv5gOu9kidoacyQwC4ea1y19eko5NhIbZPbxIKikOYNlpuDBE0zfnoWq070vuDxZ-Dez9rMy4NjRfhv6fJwmxMc9GnxDS51b4bjn24B0_H9eEmT_bxt2AO6395vNT8xTWkv4MrKHsA7nbF3eJBIX1Rt7jAEP59iJTn8KdSHMQ0hpoEdyyeGIkDHiQeXfVWv5ibfeOhmCXP-_dYox8oh-b7rxh2fnXA1k8gsM2yiAHkYqbTezH4PGeDNz9HYfUjl7ZPSYdbDTiyKePTuwwsbaSSsjtCf4cgu46Be_Dcc1T7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgsG_70WBrf7g97mTpThDGAVlftxjk1QD0UmHd4SMZCfwHxDgDuGZMfyjITjxCXOjWjvS7lhH4NV0sryueRhpUnxNVKc0s0LCYMFKddrGTS95PkbRTfjJ9Kz5LmK9zJc52LIC1FJivLDm11fmBNshNIDnNqupFvbdPIO8zC56yTseAJR1MAOKtlOhyjimngQq1XpYYBXGNcSv6YncLOrQX0MKq9qHyTOvfmixtpBwYylFvEpB2Whu2FWrt7_XoiDLd4Nqn36nli-lBrQfF952-KnS8RaiWAfFgm52J6cEnjOC7lGsfnoCxhAdNwSZBlegeMsnl7KcAnGCRJqXBh4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5NDbCFvbH4886WznrhwZIwmMXw-EYoeAcdPCTqCEfBvH4ODKUoQWsBuhkYivy95Fo2JD_IlA4A_-zobIBSh5roUPf01dAHJplvjmE6DnMCBNh-pyK6Xjuw7TE7G1IjvQomvwi_z4oc70UKWlfIDybCpNm2xNUzNZS-X_Cfx2NA_Cf4PrM1OBTzeWZWmDmuGhMO0bXAHo9HbFpIohl35gBWMmHgiVe20o3xxT8SnaUdw4wM6mqOU9FV43vzuBuIJotasRCSNP72ERmT-GTdyhuvr6KsH0GjpDABq1nebKiUBxiUpWOnhGEiIeU8hJ3OCPiBfR17zE0cC6sLbtwXb6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRnWwVeOO5bKshiwsSTyFvu0OSV3TqeGSD4xIfEUtpYSviCPf6STrkY1R9DnTSBkTXUoFDmsYyjGKOPHeYp94HJXCsZQ-id0kOsMYCBldxB-tA9mubDBYZCDKKgMtewY7I8HHmjg-TjlbpNbu5SwF29axKb2_50ItQVQYIGMPyRiBIdsegM5R-vRGzarSSGhZl4GuXJR-iyXOgBNnD6OXFf9OYl-Kki9qRtoIPusi3qLZp2LHdz0X6wuH2Bf-0z6KCK65D9Alq1J46iuNf4r2gUzuf_M13DawD60Y_auwoRwSnBKiTaltZnZ1Ne1Lcq1KUDoUHzh2ZhxLa75azWuvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/efsqK_Eo2S-pc68eA50H85KcktcbDsTzKVCST4qeyoiUe8fachINt3uuJX--Nsui29poeewQFsNGDa64fgq7kw-snJdmgrNKMDLi1LBUuji5_upJkXu526o8I_xb4kC1TtFT9dHRuSYEzOks7BktQBHJq3R_KB8wixv6voCyT3rx_BS7_RIx90gi5yfl-M9nAwzIVVRmZoTMOUFxrjZ4i2ed7hDR5ttJnI25zJC4AUrD6-orqs7XqiDRmyFu7jB-rJUffbfCbdWwPs1Jn_0zGkGCWIOraTF6k910UFpNB4FKVOOgmoU0pdrPIWHDDOUrnZQkjVnxoGH2RwBizItTOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iegdmaeGKmekxeo0g_ZiIfwJJib8U1oC2sje6zpcWYXuVmoVLYWebY41G9BAvItTghhk5ntHZB2N5zH10JGQSL7m-YIQZz6vw9uwzvBSpWL4dLEY5k4JDH-V1ykjJFEFHJB24uvcqnme1uFj6ckezaiP303i2G-xaCxnFSWQ-gr0hmcCbHtPB16Um6TnPZSRarot-nd-8cfIMmLW20ldS9pxkkwpuwCoReB2PcYunvyvzlWcy2DzUM2rhXbtdSyZ8ODLQxpkVcHbQWdNbuheu6NxAutLb1Sy5oryn8niplVMmSbeq9QjDMj1rVXI0L7JJdr9R-k7FPHlfbfacZbIsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSMm-QsQrdWnwr8RAA4Ub_HNMGnCUzi0U16dqPBoA5n4xdaFEYyLTowJrwGXmvmMSwfvV9ht0AalHJVaTDPGLTWkmdti-Khd2zIkaXnWAbRdmH0HuUlH_-7hNByczyDg9ZnnXAt3xKGOfM7ZyITy8pETUvDbuSIwopOs9nSdDNd2zaRz1Id6k4e6tZyH_hgBAWisgGl5B7lLjr2L63KBzUzfBE4oqMyNpLFxvH2IgxoxR2Rl7uBkDczGqIBzNCambLbPE9h8RsMondq4HPUFyu9k5q2_6AGaI2tXJyJsnID4_zOZ2eNpprfV7vTQKUjzrPyHzSVcn_1xJDPq0cl3sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mUmKt0YmBpuE934mylW8_8Eub0cen0VdxS9y7gwJyp2ZzmJPUrCNOEjLW9TWU0rOHazRGw5tqN1UkcrLwEtJ5JSloKXsgAHN3tMZiMgAd1XslDnXeCAhKLSmRgpydCt01dSWu0I2FNV962_NT8bxS-Frk0xr4JnLexVDON9IhT6hMP0coVSX-xXPHKpL5UDtyV97DqD7ViyhrHZwbhpd6_MQkfWJEuxztx7d_IPMZSc6vRvo2z0F-w3LGjg7WDPGzUdUbP178WAG43jhR5ilE_cERuakWdyUB52uvLTP-z54cycXqOH51XUXN7URVvJqbEfgHB0FB4tI6YpXdNq3Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJn9qr7l84HNekz9aUfC16CWp5g6D2ksWVC1kCSzuEz20CIW2M_Mk55MfbC7diQ2Oa8szpgabHi9dnE_1pDcNXGIJsBndlDW14qbinq2-jvqE1CcP-pRO6rXvAf4A3SmHMKqPGBHEA2wVURDHnA5LFsPx6CjvFevcsvw9Tl7CIivkKSJH77Z97UBjgGcTzIIjUPsogGi6hTPHhe3bw7wXq04_Z0pBrVnKQJeHlohRa5EKGwwU6j2zYwi6X9s_GfKFiF2rD52l3vVsiVEjeg0XkfC5c12rfFLa138UW0n4yMux8_9NNSPfK-IYqvAUcyY_ns8Q9Dr-6PLmzn6706FKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4nwBBhtkjgKeNJjXXaRCgHH2hBD5DOojsInDeDeDRUMfHN7gr5lBMKSyQ0Mn_osnAp8nNR86ZDsb8r3etTd2YPAL2UAVnkVLgdkkkofw8_swdqvaoc_27K0_PgWdeXQKw7C_jW-BAXtfF6HtYE8uzar9y07z2pgQyD8w0FTWdpnElWwBg_yBPZF4odj3RNZ-IsRl53HILsdp6Iv2MH5PLcZgz7Me6WyIND7g3Cu6blae7lSLUaRyV8U9avqEeznR8hE_6-v7uo3OLIDwXz9UCOMoGdJl_Ei_HSwSzVyZcakVlgvYacTy0Tc8__8R5S0p65Xpbxo3cOTkcrXhNAuwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDMqp-sA0WTqoO3tBnG7fwWbfosBg-h-Nkv3zg0psxJEdDBueQffKTBWRWx7B1FThkNJTSV4VZixZwDNC41VHfnxMQ9KKfM1Mb3nupyGRt-Joq1OtdG8BFnPNV8cvk1kqY3bKyLQ5l5EHWcAkVIxFyKCHOsCpaafuRdkb0oXlzOeYwyf3PZ6fvRtEMm4sFKxi6Ja3sqOo6Nv8iiZvhlI-Ip14NGIYBZ_z_L16tNkJ-i2FA5cfclCH9ImMheNpK9MZXmAOVvAYRXn7QyjJRz3ms1RxSGfd7Y2HmzCvwTaBcDqN0f2ggi6eGoS2WVur4BSCd9utDEBvOMq7paFtMUlmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRPtDRBRfZ8tRDu2GZC3fdk-6FnUhSkPnF1rvR0E36kq6JUeRuQkRmEyM19dAWw2P-Dv0ldNQTG9N9kRLSHalLnkxs7kxBMzOr5hB6p5e1NkxxBWxlqORpX65pHLkEpDPezYHvMMzan7B8Ky2eAy4x9pJiQp8jthiuE3cG2P7GGhRp2WUZ9BMRVjA7c77Tkc2Q5utDB_nn5JSG9OuQTqiRrqm8d62WPq_yLyxA-RDTDdTTUhKP4Xm6bNP_a5LkXnzU8azGNMhi_e_n6M8O5VsOzyvyrLz2X7Ua4PMRCDvDwPtdwqIHOWTa5HxzDYDX4CvVkPGUId62uH5SwpFA3giw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KDVBMeiER8f_rJ7rOx308edDV989xmIiPf31h6FibFMOG8we3CgivyN7PSayacJd53JHqZ4Vy2Bk_Xf37CBBSbP52B2BQLSjUMEXRme7yphb696FYrlky-2JvMBSIlCtHAreXVz7UNVuhACoutk2vmw8fnoaR_R5G9SWJ7h3OcIQ-hCkjms-leVEFIpZf8sEVHNWkIjrAs9_allH-FJChAP7xT76eGcSIVOkSslPJX_gyyN8Dj9BDrP7EpY2voAN15qUZU0R72o-4wBoIS2wRtwP1LDZxmQflyg3rKinVoLfRCx17N9xShdTzZMdllaq4mGHb22RoJ8JujehrwZbaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IskbFOgSMf6oq20y__DmhsuQUFz3nelwmMNTSi7Cnlj_VuV0s2PMoBkAyq5S8aDn8jhteT7xxtiPkCL_jISOQFlWPrYMWuiGs9wOckMi9tEm33P_46KDJ28bAG8KZd52ArLRxE5TZx7vIxGRvJLKJMHBgsrXsb7tYWZjRgmNDOwbHyXodoFrfRZm66AWmgj-CCgJj1-LsKz4TyMB6kOdCV_KV-vJUivNipArbN_m_ng3N0x2koAbPh8_Se86wuZh7vdVURXxd6B4KxLrLl3N5KqReMiSqkOUtjvvt3TB26eAzHsqrvozhf0UvymzUZl2NqvHMdka0EJyP0UG7-fdwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMy8FOR-NuxihvCA3PWK3aynPEegpy14bwiZipiP01Glrv5_lSG1AxAbFMRBGM-durU4EME_k1xs41TWkizCVQOZb1P2rYzShBY4NGsB2gGcbKtvcGD8OP63qd_KFbZtg75HNvkb_Zs_Ik0UkXa3j_X1EV9SekrrDpJJOr8iHSLt-q9-GCaoQsarzdK-SnGs1B0MStjXDnK9_1Cv91uKN3F71TMXkc8zoregq-mwg-neupGl3ZCc6ANCJdcy6NrNTsOtjHaLMO3I9kVXACrPzW1W4hg_U6Mk6y1eDyyJHZLJgi7GdczFLrRaID17Zo2A4MylaSxyLp1twjiHlnZ4OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qiJk810FAHmkiZZUvP-GN6tk-2D8zPhxyqVWcJeD4_H72d6-1MK9_5sdyBZiGFKPibN5lzoAuAt-aawIupi0KndhdxB3cDXJo4agCZujk9cgW39KsG4GEe7SwFDHPDL3JqlSO1-7SUD7NBfx_5X0jAQ-mBmcGRc3Qh8RZ60P5OFL-wF8oR8i7WTKor3wa2qGpiTFSgZlsMP0gQS2xg0nuivSlE6U7yz1OPhjz9cQ8fa92ibz-x39opZ5pg4b_vD6l8dX_KJMi9qvc6gKo1xNXMcGP22RhjMZDKv3DGzBZf6LVjCyUYhCHpZwS49VrnVRUcL7jS1lLKt2evedN8rObA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DNybtsqMZk9eHShGSohR5DqTHomSgjeYoD_kDMbqb0AjK5p4lnLeUWSoekKmz2YiIIipf8HbtMujQNQ9raQGuRtsUty7avnadFlVtAPwfpOkdblXAie67VV9R-oHRy752bTA6MIIcm-qwjurjwc6i8sUy8-XFRpreE83ihdW0ClEZSPABvMNGFG2NCZp62MUj4j-qSIuwlehLQEy-49ywHPep2uI8Js-TKFL9-N27S0ExHkq2JnonDVZky1LnDq-GLkoMnFrHpO7npmSwWWkzGgqyVPNsXSF2o6IV9EBbx0hGGJTqERLPFu2pMw9aoJkwz-Kd9uiV_5HTZ_JuQOzXA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=QdVp9yIGoZ69wh9e-LCH2c9BSRgwGqrM8_CV0VaV1dmd27ZBAOr4OSyL2VOy4JAOvoSPtWzOpNzy5-OihpPoRcOoSOHqOmHn35ZONBg-u5QcEOnXj1B-yanlWMg7wFYBvrvISAffT6YuKTjTbh4Rl4W1CFHwOEzVQ1w8FLEjruSZBwB3b-zOldcUM-kieGVJDbBx7HsZel1CA91T72NAxHBRaYZGK52FgjjRr9QNqJIM-Og3ghuaPaXf_z-X5SghwVGcJWv7SlK8rHyQ78fcj8zTvarsnp863RWOsJtuCtjlPXzVdnnc-lDhVXvSf592L5pGa2Qq35otAUJ4JFaxag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=QdVp9yIGoZ69wh9e-LCH2c9BSRgwGqrM8_CV0VaV1dmd27ZBAOr4OSyL2VOy4JAOvoSPtWzOpNzy5-OihpPoRcOoSOHqOmHn35ZONBg-u5QcEOnXj1B-yanlWMg7wFYBvrvISAffT6YuKTjTbh4Rl4W1CFHwOEzVQ1w8FLEjruSZBwB3b-zOldcUM-kieGVJDbBx7HsZel1CA91T72NAxHBRaYZGK52FgjjRr9QNqJIM-Og3ghuaPaXf_z-X5SghwVGcJWv7SlK8rHyQ78fcj8zTvarsnp863RWOsJtuCtjlPXzVdnnc-lDhVXvSf592L5pGa2Qq35otAUJ4JFaxag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCaestKbX-kPtDWqpESy5EKoO3xco1hJBNlklmsvgJbNrIY8nlSF4Pt9JLGi_ccPhZMTjHvGuxdicEXxNoeGjOoZBTE2ljmY039hOJcBBrbQlLcVWuMlhB2QobsuU6-9qddcICnjGQZI-GrOnzeiieB0m_XMkZ2mp48v5k5bExsh6dN9kQoocuGvsDmK5hPUywWKPZ2PPE497kzdA_e76C4E5wG5LTRRyxTQZYlfg-T0yKvbdPcRJ6TFUeS-x0Xw-9eGsZ5OZtmM8WTIeFSgLcgIC5Cg2qIiBmtTpHnEq0KarGtdT6O9ZY0JXxHhh6FUeI8ApMXTq7Y9gzbSInckaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCaIJdNUSoRJ7K8splwjB5n2Q2SmCc1ElTZGkb6jJivCMe371OFKIxQ2r3GaavC3_LRXFJGKtJG3ozHzs5fIAPe5kuTMTq-BIZD9-q7sOpBrc_EvVP9-69avg6llJbpAjtHwt_ziTr0EFY5gz2R8tb32nBZ30uE_XOTdgOoH7EfnFinhmuEJ8Eq9DTl2fRXGYcK29prN7PNS78JrLfKUd16I6hYQDB8nh23cUm74gij_fSv_b9-VLSpzCE2KaH94Ub3Ih9SBilIxsLp6yMt8BXvXJyReDjIFlbk8UunalCW09U3KlIlIPBhzRd8u9sLHp0vrqyittu1ze7fDMTZZDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jMBLvDlRoxwY5bPSWsFyU7zi6jTFCCCqapNq_3WKPNFYmwCwfQzqQbaigjxdgBp3EdB6w5GTG9Lj0FKY2COsr8iyu6vj7nVSA-ym9bLe1DUu3U055PZLPF392PjMWX1Qu2N4P_iazivzmOtvV5a_psqHzKTlrpuzq544c4CqBKLpLGNsIkA2UpuYmW7G9YVTg64DKhB-fDwS_5IuhDni5AS7G_MHHjDq-QMQH5i8f9o5FqjfNf4M7758VMzLnqNVlfET9tNb7194MGyiQOmFZqnwYKsQfs5UmfcFwVhOkqUwATrfhnKpmBZo39AxLlA4gmEVQylJMB8KeV6GD0WdSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IxGJArcUhUwfBgCXgauLWtlx4q8-cdeDqizq7oUMWU_JnhQY02D9JfVNk6SgnqKa8AJhKdBF30YkWTu0tiDD1MemFW9UvACeESUceVngzTe2nIItJgVlNyEswIDpwqunhHkyqsBHkktoa2sxpLNQy_io0uFacsN7revEPsvILhegpqDpDy22DdvmI2TwbKD4beDAD425TQto6jKXD8MXS1YqkHi-C-N7MXjnRCQr727nrIFvRr4BkG1cpG9kPa-cRuf5-uiPwfu8qJwIsaQvO7N36-ujTz4fe27LVOCviVPYbkgztiayADHZL49BpyInVdpJWbRhfR9EPhPxqFVjNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9NKWGlY-L5bYqIY4RTIhSR9zTKjgRcsp2X_GhNQkuqbziM0SqYdNbaxJKyT4qivWfMs2WdyPPkNVO5RNhVHl_meI9t5GHjmlkoLCf2yhcb4XOAqpkf5BArmBpITNUf61JIbhPf_1tOXMfN4mZIDR-_hTjyfmT80FESOD0-wkE-UfSiuxpZKx0p6rjV4Rwcuanvinqx70Z87VOhhdElQ-eHFTv2yA0UqCNQW5SxDnBpoGIFVS8EBk-lrZ9ljfc8i9-yvi5t1Ip3LZsA1ClOXtN-srkJkDN5KHZVyaFAqv-wUA_kLJt44p6HHS_bpqSisJX0xnEOmxScPlBu1HSeCSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_s7POj616U4hrccACxwCHl15fjHju6FVVEdjCLa2Spw7Ywdflxk7YaxbTyKpA8hc5a6YNtp-DMyBxzTHCF6wPNdfvG5jPZhxFYcm2zWpxmCX-QOAY0pbFk6RGafSGx7hwd3ie81evQTi4y6WPa1Oq8Zbz2jARTj1IP-jljCihsHe-A1s4tzPo1cKh7yXjzGk5rZHgXvJg13r15BY1eSTmhyIEi8KbDuKVbMduPh2jBsyZ0W79fadKSWQnoykRUSei0DaDnUCRsVrRBLbBbetIPGn7VhTHAIxXNux8gJOEEyAsQcjQByoZYJK7JIT1CNh3sdtAY7uCjU5rsCktJBHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTCwcAcft4ESCbkfH_bm5nT_M_DJ46qXaGK7thIf8Nz3TnfsSPlM30vd8JuCMuYIr84AK3skNv-fOg8W0qDe8mKub08Qypxh1S0CVFMd72sklUuGQihsXCURsxB_O-JTY_Jw2CmwtapwBZP51U1twiJU1mX-gjpFr1HzPsj1G7hu42Y0TPf5jvULdkoEAITJcIWcI6yAKozc6t7ae0892Q6jt8HvQ2SpFy6foiQgk7enWBv9T4s-kpxYTMuTF8h4lcvybS0rQUGzR4PQgRavYxeyNRLmiHFwDFyQx7ll1XM7LwaqgrMQhbfztZfdyVgRFJj14v4qoBSDFcVdQ5EHuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bh3_Eju6w7n7IzSc5aPddqp1wSMD_HXGXEgELWcQ3K5kHg06z2i2AJ2jl878-rRFgjMcGuhdM2u_i4JHt9BD4_wFVNV43L1n-SHXcFPJe7Zg5UHR2PymqC5-PfHZ6Z7bi8bFVF3aabHTIRh9eFmXyAoA5jnsyRH-zhfMltaU7kLvkk7fKOMpdaRILoB-OvRvEn6ICelgzdxlKIXLvewbQVBeGWDGq4NCiyvyG6JlxcUIc3SVl7r_g2tbJPTeQwvCJN2WoQQYyslQIaZafCp54eRLtPqUAwOaB1-Bc09s5Nfg-iPnADMPUoW04rqKwZNQY7ydGV5DwWCe49GZ62q6XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z1fqgG05yNoQSz2RErK4to-lZ3cSkr_6SnYaSa4RWU5bkoqGp9BV7u1YcaVpJjsKC2zWNC0xQuDo-e3faV5dNG46uZCfxwoOC0tp2k0Qq6U7qhWqVGh0sCsYUD3pt7zfcWVe_xX98Rv0auQ5EPAMRHcjHAQERdu7G9zZk80lRSEEZC7JWClj2g1RngXziobi3m9sRCvJB3KMSfHRfg-63urChKqNeoisdAhw3Mv3EuDulkYQLzO0n5zpxYELQAENqetU2QswNlV6k_z2g049f-65WOX_t5UVdpgX5oexbvZpGmVTvbJjUugoDUhnFbEuURnUmYJM0AG4-sBoFnAd6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxZkUEamkKkSH0j6Kl3VB1q4euZXCYY_yXJ8VqaS0JbPKanqOsLM3_41_vMuL82IL0R_rjQpxc3TatxYY8lMWkImYDGEkEgh3779Y_Ne2Fj9BHuazdqzCIjpVeteNAfP88cpy3sg6yWL_Zqr-d1pY8ssSGWz1kLfLk0qOJbLZkJlmARi9SNsxp3-FrOKXVM3PZNrFkjyTnSZ3LZx7Owl1VikLV68IDKZK8kjeoJJ0OMSpX30yerircRYb_cJgL_HpTZ78oTZ5aoW8Ya55eSSBLu9h3V-ApvSJNFBU5BmVMOmQ8_qW2jw7Y9l9QYO55gQpsUyda0xxeXpCEbZBd6tig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-6PDYA_awqWcvkmjH7M5ko96WlQfFqCVc95I6OophNTMim3SS2-2bZ5oBoSGZr3EWZ4y1pFeA0ulIuQqxaK-jOLiW0YFHqeXabWNnyU5eT6PlM_U0R9oQlMQ07ocdBjsKdyiYuE0g5lB5jSP7immnRpxDfvXx0Ags1VtFxWcXz61DRQYsLZM4rqc-RBju71Zffn_j45ArSE-hmcBnDAS6gAF0BDI11u4-i4oe1ubNCKkUaWVRwNNbJadMqRBtDqZCoVL7UJGVqXAT2G1JdDdozz0bXsvgDWmzi1gngg1_Jpu3sFHohk-r32DWM7nwnD7ljVJAjs5qju82OW6-RJaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VRrkYT71AJzDIG4ZQUPL8dhZb0qgzRWFHuXzgvl9f7y7wVFzeU6qHxd_9HhmVpb_oZn9jDk7UCYa50apy6TAsxonwDwR0ITmH6i8LekKGolry2sSjkOxYF_m0CyRTP6AA86_khtZTOvSgm_gMPEklRX_VnUBv9d6GdrzYTaUwhQG3U3s_a3GIdw5dAVSsZtcSkVDK80JCVxX_GkLVf47kddc3gB-1ujC5ZB57BF-kLtianhTmYJT8ZXoAXrM-fPNi18SnJMUh4zQHGKcfnWicQSmJcM5_wvJ3Otx9n00MTdRxIeBtJZJCAxWRk7PUNo3b7S4n6n1mSpZRjUZz65Vvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EsqG_mdumuXzIlcRHGOZCDvpM7sR7h505KswJy09U_0ZViDMDse9o3JMy3gjocvyoUQzmUlvuzio9oDFiXfs717Ic-86M4Mx7G0BT-pKI-reBmqCVmkarlFzCOEPvNo6kkG65C-OjQZbGVAnmU01mi8-pnDiTQrY2urfjs0aWhiNcfyLGZ7QQNW7182eWegmXdJMthXl-hsRBzGlqNuDorVagBAWzGiCVEnnUJ1ayotEdoJI_aNMGP8oxIKqeQh_UANz_qGzhMgk4_PEtxUxMWSpXzQUFUUEYUY84pNezrfo8JU_isTWPXRve7-WX5duZepmsc_pKm7EfZf298s_jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAdZQ1Bd48T4_mBWm_5tVkfeh0pXf-hL2nZtRazbkaLY-E0Nk_0vkb5hILLQxpx19Drrb63nMp_Z69wGb4E_qxxqkS2d3nGqefvjPpbUXSTVIxiZNe1b3Tsoz4iYcCS6ix_fh0c7Ei1eOCefcC1Y-Sz_weUHPk5vUL4P1gm3dWiFp8_bg76Al2PR6zx_POlnrmz6gsrbpD_vLrCWuz-sLjwpG9JdGRQhUGSRqK-68FexUOcqEZRaCpPbJEbXpk5dsefXxABoJ2F31a1nWdALdWIsD9kjZq58iNsf9VyVBq0h3_qpa5RypQH-B1cYwsbeKIQdfdmST9MA25380gwGgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYyGdIesAIG5TnAmT0yOkJlbQ4RLKiNAaOThom4UR_547woy-sRHNi7TBFyzpL8NzDy4dEmwuVWbHn_aWgvNse5rbhMxgnNnbDzaJWR4GS70HsMUUHuFHeu4rjZLof_2kogzb0s0u9aouZs54a7_l9NjDUCpcyUoVuWT2V4scZtDlmP2DdL5e6pW_39frsV1SJqjIuMh49FXzXpvZ_njnU6vJfXv463foRyrvsuDLvlJNoWM7VDHSvzg3SxnVtoswyAz8AKXpVKV2LMNkyVtI1xKIE4EMNwun5xftNihLh88BaiNvvImaunHUT_W7Um0ok-nNReysJdip3BBZJ2Ckw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bXmDJeqa5z-IWkcUA3okSNNtUaqeWxF1aDnU_VYoTcS57wjemdoxFUqAM5ZJC0N_fwS1pERfUqGeE_4gw808dpcKm0YymNWSkWED6Ia7DSV6fOlilP_hRSzz1NMU0_oq3UgEQgVd31LAEurIWZluGWRuJJEXRY8ilCIZ_ZkfrKOs3D7XMtDBwyzr6PsPGogqEgFk7HjZ7T-ZhQ74HqK_O57j9xy_-A2xsi90NsrVtt9ysOvXkC-MiuNI3C-_Fi1wvTBFMDvHjioCvMr_mgx0QrUhOmdaGtN-g-83pEx2JNL4QMNqIUHEK0ZtT_kah6OCOjuHa0jm6gGFaKnZZlmrvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipyIJHZX8cK6z4j96ZQ5QhyeVW9MTzDXsCy4qlRbkHLhzYNrLIn8vbA19temnQOYJNFs2dN9FhiuTkKOKaPmORU6DmpU6m9f6Q7WPxuqMjZYnJfQgGeJ9N4Kjahq4e0JbvZQCC6XKJQ8e66WWp-a2KKQZbzWsmPEVsPhqYAGmpwJdp8Z4tqlRgJQsKAnuhy5zAwmpNpA3bYJzE_muwvVm0bEM2WFV6xNvJZdrHbDqznSbnXjNrY0iEuE1YajqRpR33vqnRlcIGytGALSyMop_owe7cUN2poJuKRFU4FqKR8-RqpPnxZ-h5MUC_jApxKgnqyTc_TSH-6A1-h5ZbAN8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TH-9EzdWjYq50l4DjVOGLAO-AJbzTVkd-xIJ3WcpnrnmLOMANtuJRvfilPfH1T6Ktx-Wn_8aGiLck3oxxD8OIA-YjlNaZBtDzlWCtgT6ymtZkAmnyU5EQKpPYw-ytlUGjbFz86u9peV_DjKO8XYUI7ByPPmkQRBrKksinf3Ot_1-Zj4mjkZoebwY-QwXlOJR_TQuSfpmze89Xe3PPsYGcXjHt1x3M4ECmOhWeB4BErAh9yqGa5gXozMP3opkhRZbk8Aw5cASzsn6MmEcfpeiD1Gt1_r9gnQ69UccT2BCO8-EfN-9y818b8o_NWIsTwhpGRPOJYfkAwpC27ClJe4Z5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTGdVd8NItqr4l2ZOcgVllYqzsJv9IvgYT4DSRvtpmxZo6QOC7E72br9sUVM6dKpcpzAri3rQiy40XpnAeJnVtWi42187DiTo9DnEdEsKlByrv8SteMJbsxSPYlFJY7b-422xKv5KbOl-MLtUFYW0PYKXgAIZ3dqnM1dAWYxiif8YLoK1XULIeNw8EE9OEM5oX82cTqybA-aTpzoRnfo1craqSIqjqzKWhm6k45O4lE1z_FHr9MpXtg0uV6w_ovRu6_Da3UFED6I61mefnTGotjYZj-SrKv-lIVKi55JLafjeh2eQGE2XIVycf30s5eVLC2LTJj5GC1GW-pDGVDFKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPSs81t_u419aCNB1d0QOGi88jjUaYivdwxfsvALE_PpmexhQcjoGzoFgEd-7e7947DNrAjrMsAwdTqH9Aaf_r0o5E359sNREqnEYMlwTZo8WeOrcKaUxmuFmRMI7xNysqfjFrcpQqlsJCyEXtdJl5M0ZLx2oFKhlvSB4JiL06xrNgUavzJiEkIeDRlN6M6dk86lvOsLBcZlce57Qu7PM7OWLfHiYD9X1Vx5dyZ8QASOybJqjmsqq--U9PaMYKxM2fRagldWztvI0-z8vmGCDkA1cvUoj4TK_mDRkZzO38YtXfwEqlwfZhqpKyIMc5hzZmInlFmAKi0rI2P5R78EsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WPgKcCQxrgL1zLfN08kp9KOpXoxLOo5inuhrVLqTgfmARt3u5wLsXvevufjm2Dx5Jh7XofSfPWOQ4vHGVJClBOlf4AregV4bpLz7d5x2e3SsiPq7YH-rxfKii1bivAECJ-fK39jJKJauidb28tDX-Lflofm1s7Z_NFsqoT5QTyvFhYwRJySVlR8EJRy2VfKHB_iILMljnrTbrPlDkYvFWVkUPiOybobw8GDrtX2tW1uey9aszia4N2RvsknpbYwwLd9XWcNvX0pkZ30pyIuxiv2XwlKfGot5VDEMAeaMr8U7pqgTcG-eHpL0zRGlkhVt7pueVtN-LJ0gkTA4Llznig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtl8iOclKa5UQA8LW7qo08oH8TMINWC6013JCMqxVpnejEN-7XvQbZWjaiAVHuRtjkTVvDFfrpVMXiIfFXI9CpqAF3y97JhDbl7VDTH9zxVD17rwzcV8SZEcD1BpOUkPmB1z3NmExSeOWx9Dj8zr1f_KvddySV1SDesj1NhPp8Dps0tEFHJ-1ezNDMJcAFaedsIr7eedG8Q-bJwfBQZO9spLlkhSUqCPpKLN-biCtFqIXR-17WQTLJHGEOCjRGEA9tVCU96zdHnfcEUsaJ0yFgWJLDYMFF8bWPhU7lkqhBulsm2msdhnxukHY94m-wWzvDTLOL5_YaByJsHDXV5IPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-jCczwsE8fxHfCKkCX9AfAVjlU89me8Ci6XOiNUer5bhffhzwMzUOByzTK0v4Cq54HVgxblB9-HES5_R_3g_qAMsoRLZjlb5pTf4YQyzNKXj5LxlQQQPJZTMHZVj5DPc6Q4Tdygiz0Q0ud4fku2-4MqawB2fwVSaY-G4ZWaL0jvV98B3eL0HJ4gnXVK9E3oLOh3vrddMwKuMPzfLdZOUlAX6IiyfwEoOpsnOFjxcvgfUY-hpMd83qvYL-jMbef3KIr3WpHs-x8qAFBAAmbO3gLwEb58ht4IrFoQ2OEE8ezuynvsF7O_RfnwnugJgY1gPFF525hDOwwVdcj8fcW3pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooOM3iPcIUUIdfrZeGuDyQkD4bfBhrq13jK6eK4ib7p_wOOEKKlk2onlxWh7z9oFH53xHHmP07ttqs4Qw2ywv505hp1I9JxNWVl4pVUeYP1oqCkdpM2jIZ6ExVdaXmqgvyrbKxPxnElPoXQXUr3y8kn7D-p8E3FYYKdNh0cDe2eHuPRbSuGzPR8kFU432nAwZ_MA4U-yYJuQPMp7aNEvsFry2Q9CjsRCAIC9BeBffMvGlAqRLigH_YaqSaxSymev6HjATZY54UdCymELTH9lf1TVVRy1dOlJnaFR8ataWbIIWrha0hYHxkWlhOUIx7jhavgO1SJZuy-gU-sVcqs8FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2NQtO5Yod5IUckq3pWT97ooX5CrFw5U0nQTELBI9pndbDth9FZZ_o8lxEArLTEMSy_dG_3ytujkQDkOOHOrnH1wLm7pfkEfAHkTekvryyuSOAYfh0c2b6voclpSfX3IRhs_-SYnzP1mnr6mcFfCpqNjkk_duI7a8W-6GXiHIFieTE6J7_0EOaTCYLqM2Cxo4EW7PfveKfnJOWXnrBGofVhH_HCytxwaEGGfPgNb1g2st1368u9k8WPbvFXTLJeSz-mbCTciFV_z85ARvfCrcXhN8ppLVN3ZR4kcgvVKpFNknE1a3ZKOEy7qCEAxCaTgHFEz2ukjF4TQe4ZJt2S3pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZftM2LUqVAGltXK8bC9cTF4myrckFeF3UorinmiAlfqAMqeOGKoxsgpnEHAF6zWMRBds4nQf9JFyizQkihCKmpAsW8zDhs-REvtFX6-HSjOu5tasHcyr_14Ogzpoi2L_gbzvUVeJPYRy3k1q7tHT4lmkGIMLatflOyW98Qqf_5MFrRHyx7cBnjvpDVDQL9BO7z-2Stp7VnmOetU5TrTw8Xx5nvuVX4rw19y7rAYxwFAqYm_ofJ3iZMv6k28U3OV3qjxKxV0KDXtxjP1oThBAgbmN6A-87rSNtu-bJG-ckOrj7j-MTuEeZ2DBQjk87x9CDPodzPmSubs1mopo8Xs0-g.jpg" alt="photo" loading="lazy"/></div>
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
