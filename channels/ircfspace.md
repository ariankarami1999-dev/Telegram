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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tet8pef9wMqzz46oWLdvtXEFYDU8G7IZx8KBupnArVndJ16_kKk4GDp3ERwpAxSC8mnRyjJpowHlQUtyI9oUwnAqre_nIy4bdPbCbMw9Qwb-YKiSDK0E8eJKcjXBYQncIRW5h7jqlGJxiEQYwPMcrTwqnHEj55A61Cs4YyKLzvu0kSswz4qy1VPj5jz4RtkTffC2bHv0RPM6eIG1rUJy6VawPzdnow2M4h-CE2NvB6Ohlz50rDMi8xjO1jWG4lie622TlKbRS4pLRFgWjcBKU5O6eWY7rPmtRE1XzzBuanNeIoVg5NDnWV5jEJRaB4M4lwbDwPtzNiuVnEd5jenr2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9XSBZHHRfuJFkDskmhPeM2lrDqNet2dwJGtcq_8UM0yZ0kBNbMj0tK7YJ2qKd8YmvlHR0PJ5qTCfL7DxK2G6VhPs1uKwlXJgxH9qtCQAtsmabUUiAQ_N8Lgd1ljsWSOYkrvppyR0r0rtd1DHNw_C9ax9oemOf0VbSnmjVezQFB4oidEolU1A8cO2EDMzsDA5KNBYIHMaUAi6fGLUk8gWdVDKmUtJ_2JsY0Au9B03WnJsJbetJm__5fTu5oOscAWu8HFDu-SvD18Y3tHdYv6kND8C2Qc41Efaa7g5PAhPNOgtLNFYdE91gN9Wi1P-vA0Vgl_LmdDegd-mhU2tD-uPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1YsQtc6cKmwSLkJI8ygTRdxf5G2o0zA22WWRxZfQ1hEzS51Bo00Cs-EG8ax7BOIGOQKEzS44LBGdwCrxBPsmo4BmtxdAZ46U7Y1ypIfVFWwq_06W68qdeYzPpAjqgzJXISKZgMYIh7jg-F1ZvPklH8GHa0CLo7YCOYFyK4kSBe-iAE2YmuqSOcKjTBSkS5rq6VS8Qu2ACfR2VaNX5O2lg0BVP9PIbUeo1XxxAh2zW8AXl47PzjVKoAeM3sgYtqNmi9Y4s0W-EkDOj57_JIJLcslimFUmh9GX5xDY9h4Lecc4uUs1tMf1q3ZjTCTmTNHj192Og-tBdR-gere7afjRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUCZXXHYQ7Ga6xMfgclh3WqV8NXdVCAmobc8cQ-3v1aju8Ij5adswtVUhH5p5r38nkTOPgaaHfqBSgRVVX6pB0F99sgE13quWFoo6SuHmnDcDQoyQHKtmRHspOl2pzoaSJuNtOyfz3mf20xKwbV6nR8YFEaZq8qNo5fIpi1wVkn-VAJ8ObZwCW8mCmbBDCyNHrChTwoVg0n2dbMcrIXNE-os2EMlOIMvJSHRRYwQjtOPPY9opa08gr9qW48Wl6VMT2aKYOH-M_KAVTrMt2n2mIWX2mHzxG1f-eQ8sLh3ezQIJTupQG0YqjZkSBuqOcBi09BufgYHD_UbRWNqINUBqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AaaOQmsgFqthOSqp6zoI_hfttTRHVwzPusa9gFRTCm1w9zrRmAFkDvAonM-lBAKbJ77ZlFqynMPju04PggYVCZxEJA2Gi27GaGveeqNUFn47v7IZQ6rnnV-hNkvopt2C2zyNlxfSC6Vkmh6zH_sNQHeKd9Z_-6zlByAqkPyM4U7lUmaZyKZ_B_H_fbALTTYkZ07Ibya0ouBNuihYee6Q7Sx09qukyrmiaLhFrZcR4hDxHme1E65G0mjsl9_W6QgE6pepyfpUqqlccqN2mJcgmU1ffKXF0_V820WmJLLoNLab1-hU1RIaTVpgumhkKrqh7cexzg9LuTd-jLpEczgvjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hr64G_NZS-QkJhaAAxJ5xEb04n5AzJhNE2CNoa_2FmmQQWjQ36qRImi1qnNlcg3sxRn9yYO0WJ_d9corgfEDom1_VfSO6mHTIVFhXvDXGSpIuYLlk2UVFlPI13RxVLLQwimVFpSERP8NiBAM8U5U5N0R4cpSz8CVrWThif__uiT8BLl5aTCwRA7xa0cCiLe4TWK6iB7IxoVWrJFyitXtZp_iPo-qSwu30cYCN3opSAuA-99b0HU1iIPBOk-iwuCBuLxvTfGV_btSdcertq1nRiblYFwZ6cwLJpRFDBa7ATM8kxp7kSRJCcseJ3ncRH9fQJhpzV2LtVTOyMETyvnDbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dKZtQZPXR5SKsVz4n8MX9SPq0pG2TssCuO9YektCz_psnFQnkkob8FqvT2G6CYsQDQgtTKL0vwP7fKWXP4gs0bQbzLvdXYP2X93VuEkzafhMxM98G86q1VwDpMf1pQjXMbzw923TKJNgdrnqxc9PtF0SAHLFDOxTe1th_LsrlEb0z47SZ-ur6U5ht3Ygt_NUHOP3nxMaRecDi0ASTAgfXXR4lrqIgBdXvvhATMUtnmvemDwpzCYgzajuBbIpR-WHryN7lymkGjCJiHRvrkXfkLH6tT4cm0s0Wbhp7j460obreLzw-pfJh4VceMLQn26CA_R9CKg5ghs66KWxKGnZlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbELqrTAB7n-rshjrWtguv1x6Q6kBWMH8BZxBUDnk6fOT5xGMv0qNf4kwtNVKWDdERL7a7iwekQ2Ba-9qoZjBjI2VMpDWy1X6gJfqInCxW8J8AY5mfoF-m76ZBxujkgHMihaCpMVovT-dLFkSsoh9XNVasRMmsN52pr5G8XrskAi8JzoSY2F5ruPK-l2K5a-EWJE7ityWaRJ2AEz-pcTsxS65xxYm_s9z42CDinKvgxnlV1sgGUIGU-Xan0sTh1QJg9pVfbcrX6r9E3kA79qxWjmNvkIiT5WlYM0UP8pHy9lSv2zXfm4WxDfOkMt5K4zh7f_VuHoSuvjND0SozWtsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWcOGzX5eVEr0QIJuxsWKP12z3eC91J-Esbf4n142V51OiAPrEdbAmdAJT9kkIELXjdPN1enOiiu0qQJxmQSJwguTe5VwErt-6bjyvr3Y3A-QUT86gl1B4M53SZWnbak7-QCSCktV0P5FcCQNzu9fzs0lkBTyt0Nf-jYMmc-hnI_pfmnufZBLYEdIdwrf_9Xn9CvEuwaVrylKWAmXWH6GC93DB5bN2ej7vt1uyIDmU_7ufjwGbxBhQ8sJmFuBhEOWSjUpkXTVPPnbJ9bozhRLQ5hrcReOCnBzrVZ2fuJxXrXVZPM_oABdBXv87CCw5kjjEGLs1fLOo6EmYSJ67D3mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFXe0uYo1N7KB_SMBJQRvSr2iMRvthRY44KfbR_fly1IdlAhyiL2mkD5sJ3h1wdCnr3jXxkowyAHZXiyJBygKljmbk2QpV0nrxE_Rl3xONreNtnHMEK0YJzvhJFSmbrLSTM2g_3QLRBiErZTbclIY-d3t71dZXkbOLUS6Pk_O2V3qbQ0jrvtLz2umgYWYt6drGKHCdt3RTe5njHu7Pu4SZdaf8E7QC2IRIr8ewp7vcebkeaN39USBnzXNf0vA2EIMXaKSBjSlxSiaUX6VbyQfOFY3vhP3slXEOYSljvH7XxiaInD49tkVSmWJTYiLucz3e79QdcztFDRwC8FP6vA0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rf7f9CgtNCBtjs6S4clEYPow_1-U_IjFjc0PFJRt6xUcte_71Fcuu1qqOMi2oGJkmXZDAsIVZ-4cBSvCOtOVE3O8tdS-jXLiauYezCt7bXyBTJANZMqMiE5fgMfWyP2GmIiLLYRssFB0jFReEElJ4wIyFVVHo_AQQJoA2gXS1AyOUzier_ClCmo3JNWWn5yD1792jh2OSlLbZBGFNz-LWxgr1znu9yIqyhvDOhfq0_DR9EWVjoOMUGDSvOMKUm_sFJT-jXGnQQctuKh6IuczJ80eMg1CdFdza0QKPG-OEhnI0xLiOcTdImgVexh2hAuStCaTA30OgpLhRZt73TBgmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5qcJBOpCMw9qht67Ryp2CCgrzMCSIgPLCt20aorkTg7kfa030eNOD-WnHd6RpjEC4gvYRgMNCicVagyjNS61aMi9U-PvrACwuJQvKtFHz9Gao5G0uk8VIPL3wVBjxdRjAKooAU_n-WGfA-gMAutkMDODVgo6Z6shIw5J_U4OjtrKpwep6vE4qrwr42jOx6ZblZZuBEsi3Z9O-73ZPMyp0PaDZzbSeNwmtCWcOvmHp6cs34cXCnRAOdWfh4Ku0cPaccMKRfj6oBdUeONgtj1jGBG-2rm5_ee26w0CgdBtE2Upse3IeGdvSpC__VHOVAGP7EBmsRA6ckpNqLv6T1oYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRgEr7xtcUH0HZrHrp72OL5bOrnN3NWa5upxQ0HVzoraqFgWgsvDnovX0h7D4C41vmHHTUxCWOjUjyBivCuIbjbHP7E_jCfwQj00xskFya5M29siEY99t78J28IlTWPA8GqKdQGB_M5FKHKIoCE4nSuF_ggMVsXcvQf5uH3ouLLiX2sHV8vHUu9GpVXmeDPyo_5ggmCgOK8fr1bimZyuf0tZXVPgWwwHAjKE753bw1G0akUUA7Qr2deLiS1YBSMsAsLSTXCz49tBUO08RlCYmk-TSjCOpjpvagHpBdVT5yEXUKcUjMKFoPtyyIKMOambM4SKn2q9KA1h0ezXp2xsuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zkf4nz8SEZOmIerOOD98hoop9OF00Gt3DsrOwdi2xIX-mts8xcxuEEEwWQOASacBbObfzp6c16gEbiKAek0U_3uiyCOtklRvwHH2MQhn03C36pkF1XJ2tCAhDgOVYKLL9uqkiSC6KgTE8Oanh_UigRFdrXhah8WBDOFAcRo6v8DiXB9y05Gf6Wy4cJDphZfjDbeoZnYIilAwDg2bhIbXXi4gbBmu4HxBAhWf9GgUkGCJ-LxKcwIJs0t2ZvPFLDjpXwb9OL_EqyAGEED-zRZ759ed1iaBtqFcvjlnIA5oLgnxmwyR_HuC7KL1w21xTuowkBcb10LDVtXDlB-yrLJE7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WFDyM2Z15r5flcf-JKWKRdwcJ7p0JGoOJJnv7287765GJrHF8_VTTweGMgiQ2jRoUB8nwEsAzMA9oXvnMi9cBs1Bt2iU6HRbWeCZN_pncaBtPMDdflwazl1INbibc3xLSLvw8fdXFoNoey-ebIkT4OGKrDmZx3nXjM9tFQ91miGLMhY4GcLdvBoWtCzojTalNSwYIhhYhUlwRWeaWxRnUvahqBgEr7rGw4UG6yPph8V95E3Eph16WGgP10J8Wt6L5ErZjtBEWzGDY1V1kv3jRiUdUsXVHltXJh2zJqeVCjUhcrDeyG38VW9IQjqKczWEDWwvaebCxD4URrhUqS0bSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiGStqodFzNhOLxrb2UqXc4k9d1---KV-giGKSrcvSVhuqlW6eUXgFq74rParQjVKPXqDvQQlANQEzJzWH6hg6S12MvjajVDtVYIBaJJuETpz4OwWym3JNKmhGl0VRTFkhuFY-zIS7gSjB-XGPDf8fiNZSzpyUQG0gV-WXLDv2xi-iUU73Fn0DbdVmIEWa0D9PG7k_sU4Mxh_OgamowplNoBwZ16vQvA0QgcFj7DJUqqDLYx4fJCYvRXnlic7773_ZpCYqGQ2EzY0OMkaKiKhVeybEt-eiJii0W8zjRNKJTwTTa6c9WDDZpm_NnZOSACcvPzIPNVkuR5ujxO04hWYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gi_mA25OfcPTyOB2BjyaMOy1rXQ3fzYbGptida6cxKPEgbwU1AA4oOwHMGeXDMZYzPFpjvlgWLfMf5X3Z1wWMgBOY1YysZmFNfKHMjeIpFnnKcHWM9d1ILCXC4qEVbbm_IzX3Y1Pc8te5A-xs4l3yAuZgEfkePf1_gaVXPOHMsPP8CjCYYDgMnTvwpGlCicIkbNwJIVYkuIZUObp0jb3SuMPWVUH5G_jGkOYmLoG7ITSaIlVuSi6v2Q0Sqw5eoKFaIg2lfIPLQfdPnkcYrx_ezSQScm2_-3HxJbFOyPEg08PoOCZakAkjES3CqPfGFqICnnMy0JBBpgtA7aoqpzHVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=VcqpXNT8K525IowGT2ZKhc4GbNcTaLEJLlTi1Nhd5C1WzoUeSyggU2dAFZDW0TQikJcs_dgTBtAoCAA4MBsoH3K_aTKJIF8bilanDYx0YAa0R8FOm7DYmsKrZARoxaXfPydru5Zq7W266pXj-I1n5On5Nwv2kjY7KOhMbHP0RBFJC62MY5-Zc0pBev7ZR7ngSrlqjtvQSaoxQG6DN3gkk6aMfWDyZ_nUWTtdWCjUWRa74jIxlT6WOC7JK7-qAudJezjRUGLWQSCi5nZf7QCeD6uRDV__zsigdbQD7lfvsRVvKC8EHL4RU0XQjgpkVEha70dJgoheLza1lixHOnpmNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=VcqpXNT8K525IowGT2ZKhc4GbNcTaLEJLlTi1Nhd5C1WzoUeSyggU2dAFZDW0TQikJcs_dgTBtAoCAA4MBsoH3K_aTKJIF8bilanDYx0YAa0R8FOm7DYmsKrZARoxaXfPydru5Zq7W266pXj-I1n5On5Nwv2kjY7KOhMbHP0RBFJC62MY5-Zc0pBev7ZR7ngSrlqjtvQSaoxQG6DN3gkk6aMfWDyZ_nUWTtdWCjUWRa74jIxlT6WOC7JK7-qAudJezjRUGLWQSCi5nZf7QCeD6uRDV__zsigdbQD7lfvsRVvKC8EHL4RU0XQjgpkVEha70dJgoheLza1lixHOnpmNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ozg-40lVE8ylcLC7x-uY1FDPH-AnJykwpYS2tsK7HXropl6I8MQPEEPFuFpQp0wXzsG7w8REMmB8RDYeDATTQ219elKTmKjLeYxrVVGOW9g4jM_-Hmr5cIg8qMEQwXy-v2kZ2rX-UAhAlgjkHgB-I6LMlZZfzYs_12lUewjE_nE8lbK9KVvKyzNU6Ay6lWNKgS8fcONHd26DV6WKPHCKOPWE16l95Rz1eOigIUCwCgLvqEl7R6ZqsSFSWyG-hJ7plNJX7Z8vHM1h3nE_pF1WGk7B5UL2guSLJXR2ViqM-njEYVrfZ-ugI5Mdh0wYxP13dveUoYgWFFHYsoMlj8TFUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/inigbJJQkWASuib2Rc4vcKYFlu9fNUpggJEd1Ugwj1BFGyUFAKdsOoJVULI6kiHAHbBVOByE1sRTWXlUR4iQSenVMVtiztJhLJoFcu6b9VA84OiPuNKnsViiJDhk5f6dkqXKtd8o0czORQQhOWAx4ubo_8UWcaVAKNIrk4561CfEXySKZlJsjQbA51JtNq0r6MBBkLT2bBBb1QagSYAhNsonheezbfpIGrbf6CKH8zLo6muzz1MvvPI_K6rdf4-4SgCHUEbmBIIxp69OK8zWhdJUEmc0qfSNHYe8ZGYtS4wzDupEWv39BMuhubRJJyJyrUWJ9ycaCgxaJvg_IXGvyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PXRJ_Bd3d0OiUBMU2Cr62HaGjo2RgBjJPVWJMalRv2I1Clz7AYJ5_uwuzNLB2uZ8J9i0W4sLtz2NdCtAY_FW9SDv1RTAlPif7wkNtFDYMA9LgVZDxh-WnCtdnQgCLXeCiX-L1E-_RbEy9Du1Xc8oQ4IZUSAnjeBbqgVc4Fr4UOnPjc2FQXh6octUfTGefm7FPSR7_ZRzsc93vRkh0CADTDVs32XJqC5ZJsF8Bddl0XjKKWSWAh-O5G3aQdkmufXcSkPcWHF20SfG6tSJGaSdYFqIvDTFvc6XhiwH8N9AqGiu9nIP8N0-FPIqtRVtqHL_CmFn7Zaa7O19dGv7D0gHuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NMetrI_gNz6GQh2QAq5ZS7k74Dq7LUVCFgFu02U8R_nhKFUjoDH6btDTS4b9oSJnI_Kv8Gkf0VhVS4F94wr0pFgSKVAwCshP2LGtudnQonYOSm2jQElm498dAINqCsMbaApDGCaJyMgP9qclQ-LJt7pw7dz7tAdCKWqyO5eXpnT6NNvkwADUns4VkR9P6h7bxw55npQUmDMppNMvIwT3iO5iPuDJW5Vvnuxyh9pbLFdHbdNeIye5oSWNx8LtwO_qSLT8UCJm67KnG4tRGfqQ9J7YyIDeMYnrhuG4DTOiNLlKKEFZ5fKBUc-buMgNl-ooiDjhoeUDAYTS6Ip6yM9rwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UBn3f1uY3ctYMpxpCd8EmnauZtb1TmcMl6ASi3bP10dYmGeUc7sDeDoimJWNYMOQHsjCbsBLKGLeao1fDseZB9ZL-mCPwl9FN8FFSfyJdixafobeSiCbSTYy6SEJ-DuEkyvTDXqEg1yzQnwyk8EO_LOWIyPj3ainZA1uzgBzM42q4tqrAgLCjKj_LbEJGkYGd7DpkrixTALNnczjseDL5IgS_uHDPISgpPsdLYCJrwYCMAR_LABRF7SIKRyAPm8eCV2XZfnKy1VdQbyIudAweI8w1EjAiX596LK--NkQacg9M92S6vZih5pSoFvFNbn0unG-v5aRvYBsrK287lNLRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nh1hdClTCnlCl3LuRtnBm4BNI-QDvDNhJp4gMi5PUJC7vSkKRQtuJzsp8MC-VfHfjDb4HANjefoi_c9r4aM61bNZqaDxIkyiXpOcmKdThCxxAa-QvIeNx3brHM-U3dlKJ1JST6Z37HfEm8lCuFTQU7rDGcinCepSu73rEWJzF8xCb2JPqdOmoqxiYI9E545HxSHZieYnSKacLEk5oxhtbpWumCT6-wQO8lATPCh9NOdL2ZenW61Cbz2aZxWUfAEHryI21bFHqpIwz_KZVZDPJPLrPOtraBuxkuoNIaI3b17Bb1iaC9L4WZ7EWFPaQh8A-x4PpSrTirM4Ke5pI6Z_oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lwjy1ULmBB7x3DZwgu2z4zq6oeAI-RAA4ArA0op84HQb0AMwMUNzoThjZ5s3NnxnqQy90taMqEXXWybrxcRJmB3kUJ7N_NnowOmZhcJrvF8kOZgTGMqWuvoGhXZOIr-lUj6FEdbsH3X7zPmLzTFvuS4LtgwqqZbfn844i6qT6KXePQpV9QFfZ290ik6lqW2yqb7BVUZF_3x2o3rX_htURxzT9lkbhorAzDno7vmqMZMa3hsoq-dAPDwXPlIWLS3I9rmQ1Zae1YCrt_VybnbNRqSsR12kUHlo0ZrU_SRiWdsgCR3nAsyh8E2cB3nL4xqXrPFUGrUjzQhu_yjbiaRbfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkJba5H_Lewctt8MWhkHaoeCwqL5WUM8KzCvgwF3W2Me8Qqb6R84hCZxQM2M8zp2-IEjyIBtv8OjDzTqSjXxmOnDNZchRG0SMN0v-HGX7m4l1YOiXvR64BBaMET0tRRGCJUS2vxjcj2dBGG1QDSK-Hht5CAy3nLRSEdrADqPQL9b932iIKoM8AVyhoHM11z5YWL9f4719cKjKw6_FBh3sF-Vs2t9TFTJwrbqh5wvtaMCnXCWKZoOFF_TIpd0ef4Gw8CRxPtdzBByqnEitsfslRipQdRLxX_638Im7PHQ4lG2BIAKrygcL80tANfOhCdAcNpDyg6uwY2S9hsbeagDHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZNPDASzgO_oj76R75UInoDfhhg7NH0aL-1g1oS1OiNrLkwi-7RqiAv2J51JEx3kqKSagT6t3jEPINQXznsHuCN8jF8evhCZ1sQoI5okabu_EOR9k5MXMO2IeyVSLz5ZQsDU0GQEcbZsL01jGUQi_O85rpM6XWiJEud9oF6zqqbvY4irXiHAn8eLM_4q2Le_TJcE5_XjVgv-Zpz0S8lNlawtCX4CrnCpg79IcgnFKMWcJWBIFZech1UrNkzH6gE9ug9gsywlcvnjul7DGFexQlmclNehPP6gmwT2YmEuwSlDLvuvMVjoxhKcsM4qvpMF--i_nBIYgO70-IgZI1hFzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nIjoiEQoT-nzDje0qEJ1nnaemrEpCGmebjzmvh936VggxDfsG34CxG6lvmNrwQJwD0iuXzWyeGJU12CVxQwmbo8I2FwwTGkijNamrohTYOiZP6wcWat5CaChkku7N-MfcSB7ru_GZj9POzkSNes0lMf6tmjhCtDaHrJ68N_z_zt4MpDgy1B2IDQjNGDglGdY3PGZ7i4xF9pjsWuASfz38tF3KVg8l116upT9X0ZJveBuPRdgw2QDltXMNu52YxxkdTKghQZuoauKYqZwtstW51M8BOYEUXUAF6qWd8M6wRzNBOqdaFvquuWz_yDHeUFWeQbo6-PMGX1jAkcGepcoTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUQqsqAqr26TYaT_FAO1ZYxB7bdBtO-ZYc0O9-M12jsom4-v0xMxNlhWhE-taZDSwVcpi5rW7std4EgrwCHCkuSz1FAq7SjtoP_QwUkqFaoggt2vVs591KdXRkiiYdl1FrmjLSTfHv8es_ivMXpRCWctbzR8A5aFfon-09dIamQtcf4DkMOwv7SNsUCo92Myiouv4xq2afj8qIHQGWLiffvazo9zyYvttuMSDUxIZD3EVE_nOnf3vBe4lEJBNdxwPzlOFb6tNoSgLgQrzxeBlVPol0BKo746-56jz8nEuuRscKeLMMSJEwwknhrxv5ozRxomsHE_zUNxE0G7nDALMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Erxn8CiI5KUBhje1OegsT8ZSRA9RRoLpjRqmboewsFiKiMBQQJMAuA_tUJupLjpTs8lXYY3mud2kEFS-QtHRKYqWHIQ0CUaKk-r8ypip35I_3HRAIBmha3O86gYC4ORCfk-xt-dAIL4X6Gmu2o4SlQYylZ8BaisjW5byG-LUD6fJ6f_lnEchpaA_Jb1McgiAnabTET1YislWFHTIsYvOc4CD3YSO1aN3qEoxPwD6z404lRWyGY3Q5h1SPnZWN_DG_iCQbTAYakN6Y1MOBGhvh57zoPDMLVGq_0G2gdKMHgOPSyj35LIT7Nu6wBeu9kFis64cLGymLsS9lcIct6b4DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsGdpEBjRHvpdCaLPT1SLJoI242sTUgi_w7npjkgnoQFEL94QPlujd2CtJ8WGmDX3JV29iamNdyGT6RdzNs4BKOXZrn9NuR9YQFRudNDRPPt4beMeH1ua-CeFXieQnmZ-sjCMxWM8XhE1xc6BR1MFSVszCSe4ddfWgEJYSsbGUHMwWeofgfU6knNJoTc20pec3XAwOaMKnbED3iV5RCYmpcw53EscjAZNLMYbgNDvYM1456992lem-MIXzbP1wYcFhWzqfvFbcCKNkXrfw_W8k20_HhgP6dqr1Nz-xnfF-uwdF2NmA5-kwpW00XPkKNs3Uqj7_iLiKZX_kcWvydhAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mkvD-LJoVIfetoHupl6JzLR8lq926VfLcrQFlgHjVLh5T1pKzJt-ldLck0WTt-IsM-QLDFfFJP4Mm-KXiN7dNuBcT9qHg9Kow0ep6chnNZoDYCHd9_WFQ6L5QSWGIpug_bslpRDlcicrgvIzMgKi--w-82L_N6n6geH1ERtHFWE0AR3V7GREIi0sHgcLyuOyPfUvfj5V7fRdaIRy9my5IVBO1r7C2wVNVXV9IgA7tQA3SK7d2DnV7QcAnYFqnVv8KlKUxuiJclFggbvORoMmJun5z6CJ0_n7Y1qbTZdoM3IcmoafQAkFGJIArU5RCB9LIU6s006hS6y5j_6NvXy9kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_f9b0B62YOGWmMjvfDSj0uxBHSQYJo9lh0OhVtDengsbhv2rQq_IVvnDezTiDNXN2o-AfXoM3Q8vXVVhZ99gdv9rchcNYPub2EKMQYgXRYOcfFzfUMUz6cxGO7AuPVH6ViToAPYCwTxaW_CAvFgHemSEHJrix2gqge1CBIPRIa9-_S3iwa-oIylmy1b5qbn-fmqBALGBNDU-1iM-Y-pTo3x8SCwkyH-vcnYIKIrKNcYj33Hk0u0ACz1_wdwLytgxXvvFoK_i5PDHsr3I1nEPp2OfHtJAg125GdlbfDPhmUlNjhnMWIkDPgxuFmkIK44FIZKTI86u2LkKTKPWxEGGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qp549CEvpGNKcz_yX_YW0xT-_waezHWGgjBqe9I1G2kZUqUWf8iCdIFgkyoQvt4OjWFusKlyAyxC2mKdvO0OPUHYc5DOFIsFZfubfRR2c43ZTHob4jJa4a9mWxGHoL4L4TEU7GxSORtC-xU3nwwBNtlPZMgV8xXoG33RNJnI5rT0pQFdKSuNuKkCev9p23xFxo4muHYbwInxOvdL6fyENG_R05fr6AX8jCObJSZjqteYdqf86QwkzKoOPzjXcJPeubBaxUicLvPuuOJTm93PoHFKABqDWggPcWMJ8ZkfLrN5NiwdzMcAJWLJrXfiYEt0e7jRwbYZ1afnRXLeRTVX2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d6jlbENX89bIvC3aNq9FYuxuIHMwPHAddOCfqPaH_lJj6WJEJBbLfc0ygmGHrR4MMb96SiFmkWuf68r_Nye_hx3bL6O9z7U7-2_7gfBu86QABMCnM_67PJD85yqwq2PAhiMMkKL4u4xv5Nwkz6Bx9k4oBRiUWwhfOcoKHA6Qr4viDTfeB1K3xGoPEc7sb-aPzxMf3g7ZCIIlneN3G8NQjueX5LD-bHgfxeJWWXXl422VJB-GaH3ubYk5-u4c_wzTjlT7wExmW2_PIVSyBcz7tA_Tkx3MP32QfqSJdRXcjKRJqhGZBCdPBRCAPEv1W4vxSle_tdAKcVKKILQcnHOHeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NuhDw_J8QKuXAmmjZRkwPx99MQKus-HYCgkp3q-c2YJcFv_gD2k_qC_ueFLM2Z8i4h1ayc3T_UjXGlY50C3ZZ0ymoSEUyXx0RCOxR3B9kcqJXuNPxaxCaQ5WUikkgtLQXeRUUjtq4eYa2JQiQFJ58yzJVHauAR2OdQ5lyxYQMYmnSjMHXhaVS38EA48bj_4kIKHG8p3WokS4as0Je4GTD_oXloP7tvROeyWRhEYu8K4uPG_bzhBJWUGpvBtmk0mWzOrboJl12O34NwHrobsIVjpmR1LdDFtdRy8y7ncPa4l1IMHL6s7RA83spXT-zNxV6XKFBeVFJrXL5RIm3LZ1aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xo94VGWrT9UE0kHlc5416Js1hE7mA8pJgJf-kT7diYJ5X0AsxYQez1GlpnwchtykD-kIJERMI6_TTb6rXJyZpS8oSo081QiQ51FVcFra7Xmwg0pQeuTxIxlqA5h6DgNfCuseaIBwq10X1qUJnnRvTY6I8YMqtzgbtkFDAefySXeGAuV5tB3u5g0DHyZ9x0OOy4hjPm63cSFS6GLwjTmnogxcojortaMx8h_b4cqMHFNZaV18OomIlrMv8r6SiSKO5VzIVVpH5Ntpi5qnJ2Ozapmm08gGTJg7e6nr-3-25NXsO4yAH2lxKusTREqk2UUxI93_1cAzku-PikKax-4HBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kc4PvIs7NFsuNDQzkkzTyguQunjHc0KnmfdtmQVaRxgIXSSzKwxMwUgRPHryDCiC14YBd3soKEzZSu07B3RY1EpTvlvqv4vbRvLbsdRhb5Cx92X-v3VQ-PoA4hHC0_UPS5nl7fc9oMTxlwXLhHnxLpxFkvzMel57eHi0qlrcY-NpZFZdkJ4GowYBsPMDyzeC0zgUg9gSxebZYEzPq5JRlsmX08QVrjccBBFyzlZ1fjeKDBHMQzSU5oaqMS2w4wVj2fLvp1sXefDkB9lQcvQGogKu3zMOX4ZlP7ZZhC-JYU7RDtHxxujJl6Mr6DYI5yQ9UhwAgl4EnWhp1kXI9OArTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EPkx26Mz3kNkHTKN1GnlVlHnXAmzdkUgf3qFIx75nhGSgfjQnFAz3PkjDLxKj1T1alrpFoYfdV4Dl2rnrvKwy-X0aSPPonTQhuwnb7dCKKVNG3wIRNxa6MFuuB3Bx2M3mFkYsjcfTDQMJJb_xd-1sm0Jrhhh5w-8ukNPikCLzWdNBpFWMVjYHcrRX7wGiXpY9n5KyvaguoQhwrZ7uozJG2MLo-hH-iMh89rzUx8jGbOhR_Y3JcMajZ2gNcVv2Pq7rp3IEB9beEHUjaV-Zmay8_pbUkVovD3SV8nuXgelBPaWUxlkjCiED7JEG3GYYJ1oqZVzxFlr1FrJ7e9mBUXOqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtZlQnAf9flGO72QT-BSftHY55EV9asUlBx-G-j29DkgqIJRDrYcsMQ4YioqFepvLXHvAzUOXLBJtrd7KjIK8jFePOJh2HpZkwK_tUlofFmlH-cqif-vVVU9bWTSQ-XZJc6zn_Twv64aapWxA9iuQ4GfWzo8WrbspOO4yogRLMfrjFBdUrqUjJvOzEgNuiegWQi7qwh1bv_pgWaki0Y7gXDlAWLihKPoKDn2DzM-KoiF2DGJFx0xyA8wrH7oK_gODEEZ5czWAffNHrS_O19bSTlobxn8kM7u7JHuvJnMho64d3-cth_LrV50HjzzkMmJylaOqVTY2cqyOwrvjaqepw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nc9xCRLpJA2vAHR6si-SnRwVLGT1ioah45J50Vg3OfCTbPyobZDUcBIu3KaNtk6uZQMA3i64sA1FiJMhv3JQ8AlTiEfoowBucW7pEQLhPO_POuFDS7Ko2u8GUeSNBES8evNKUPQhhi7LmtpU0_23LORk-2w9ks0mlNvhHHpOzMxbMe8HFCZuAxB5H_mjMgupv1iAvuU1NsFIhqPa5sinkzkmTz36Fl2Yy3B22gnjCvqM9w0E6DpZU-TRzqfd7waPWTyLudTZ00dhTLebN7xl1bDNNWmXfAE7jpJ6cPqYv4QBU_JP_fok9Q2L2VGjkkdwNsZioJMoe0rUlPdLF8DevA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N94sd-gq06532t58ttofzDe9TYSIMw3YI43Dk2xonTOLJSVnY3e4_Sc7p0ek2AsbUiJzLBhCSwL_nR0mNS_ZnxaKADaYpntWbSkc45RSFQPrB27vKhlhuKa6Y-Qbzds7-7fEJvxvatRpdWje7kd-Dj9P0feLP3zWTzQVX271THHQ1XoJX9KGDyITiciNq9EHvrAkhjy4q_a3WHZd5AWNciNGZLF1hxEG6BIVIAs3s6GfeUzuVUorAi6OwwsR_B04o1Vw5r-ZnYaNwrvnp8F5870eQFLI5Yul-aBtKYbIAe0XqyNUImQUfqBOvEvrj7a_ti9nzc4AKtUYCqxV4M4FIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cd8eQLoq-x1etRvgKx8H45MgL7GbgIsgQO1Rtw87L776yDsIO02ZPmLHZpTHkqUVAnxE85xCbBYu8Y_gq0wOuCW-degELC7wFbabLS_zE6Xxy1HS43s158O4tbDWuB2CVh2bv1DG3-mV7LYJcHR6lCezmoS0_ML3WCWvY6s-Lmggbuu1-uMecOuVlWs0rdBW2kyqul6OYK_wzBn97XsgTxnYDYHTmik3SB8MTsgmqK60jmKn1fOPHE7WG27KNzQaejTXyHMKOnsCSa7AHVpWjQcuWLUPJiC0oypvKJgVd9uOr6m5wnYJExab5rhRGdiATUxjPx83vGCB9LLTcQDH8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t9ISTX-NAGPonIvyG-eRCXo-olJsFJvea9GY0_oEns3LW-LZ8Urvfln__4Av89c_vv66Ea-QZsOpUHql_YofLyOgnJpD-oIhGtgJ-4CzhX6Mt__1ivx7CRfNPnUL9wbqYTls-6igyvxdyHOkFg31au6AgGA4WMo36dQB3AhQhEC_i2H3OICjM7WG1jmuFJQfNRa2fzqNskZ0ggm7uwsJhufMS--tBs1mNn9wmWfij3_Csc1Y57Osf8HONCBGru5l-M2t0U5RI3iL9VHJmsd7P4hcXM5s00tPYvmA1nGgoyPBbeUMmsMGtDnvarsJZsWUfFJAsAEt3WJy1ou832g-hA.jpg" alt="photo" loading="lazy"/></div>
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
