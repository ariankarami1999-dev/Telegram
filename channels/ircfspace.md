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
<img src="https://cdn1.telesco.pe/file/pBJJUNOdlMEYCDwGeX9__B01-ofHF6K1HouiMZQZ-nXgcsba4Y3TkW9nme6l19y_VfJ6SdY8ISDF96GXxVyEZeWSP_D7nfR5awCVaso8iZ-QxmXm6ibOZG0dyaOIu8xPSSwwyecfnJpBEXldUsTsiefRZR_DhI4Uu0TT5hS2BhBIx2sm6oqkLHDLJxh8zvwi4xNsRWa_-wbYnkFVX1mb6s0xTZ_bc-VZ3JyOH04iVNRuCiwqlS5sgNQ7Sj1cBjhTHhA7F7TtmFZQM-76ffl6Rt--ooeaJj9EQL5UwAMrZ_rmNbivYjqj39nspRD4epSowGqeZGFbYadTS6iGoWYxCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxdRrVdLnWRhxcaham-ERjuAkG5tespsYNYkp1F2q203eRUdcjdolxP0f26qLx-cwFeivYm9zSGRXR34_RmUy8TS3xcIm98h0CNEf2F52u9O39ogQQH_XWQCclyvy3wJK6X7GQa4f_gWjsHbD8Nce9UbCvR8PPhowHOUdsI4q_KT_Zue3MYuLR4aGzfImdc9TeNFUcLd8RFZ4lmRPdyQsn39aqBepFAEWib30FG6qhaDCs7z9Ap5q31Mavsg59o-Vyy7xrKlV95fdXfZ2rQ5DjXzNEbOUUxdzAORP2wl9fdwyq6WyOp03xHYfQ2RC9cEr4qLwQ3dY4gdLlLoM78OUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mc4lD51Kox-qpIwPkZKrw_dJ1vNu03ue7kN5e4LI8vPqeoRUfxGEQvxCVzlkvLR9t-QD7p_Cue3l-ZpPVbnzKZ43AbXbHVaj1Yfu7IrDit_ICNiJmCRLOTORlGnM3IfB84Vn3dYNh0OJudBNJfyrU7FuCwia3sWoa5gdV1pD_F3CmVz4crWfhCK0Td_gr40QQTqKosPWWnuUnDMZzPvFXqJMZkZbmwr5PYjDuYeiIdW3yy9NQs4bQi3drn_3a5dHw7xnfWQzZEY3E1fkrbElqqdhITEDj7A1DKe4UqZWcYfkF1y4vgPrmZZcfuJulfRtaQaNEpv_ndOmgwrLbNXzgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scGd06nI_l1FadfXDXtmkaBt4i9cnD2CNnoHH8kIoqJG98oz-XacDaqs992SdJF66id6Ct6jnoJeU4S8NiaX4Qy_YkwgR61YO6AF79BToA_sq7A76QpfPnwg20S3cwzHE9xxwPkd3y6rztoB1zt5SUU7MDHrUYlR1Tm0L_2d-Jowza5IGYZ0Qe9z6IHfgGp9ObRhyQG0iG9Jb0qNfINZNbAXEa3DAkYv6fTHE7X6oY_uKIfmSOnL48LqT3CbJluNoCafWPYgGbqeRd9r10veL0HR-6K1FjjZabxQXakcgQAozILAtJPjicUBPRjZnt9gV-lqekMwFnOyri6WnCgkOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QykhAKyw2Y91lHMCjg21qyfbcYyn9tz9KPP3mMXV8cCQfUVr-EwneUCsHTd-WxOjW1HRk1ALn8vnLaeBwjjvuKc79th5yKdEGHZMk3iecpzqRk319yblhUvlLP51_jpAFa4w9ls0AudaUjnU1-s-fMsX3EcnPW5aSxgHeaulfdPdPrEuzh07AZtoh5f5RLFdXlbC4RVDnwC_iJ8-djwABF3vlX7UG6mnVjOM-kZiHSCZzoxwRLZCln8jYOjus1CHturbkDqpjx6G5Z1mXWnY5oNARUH72zsi26URDMBYbOS5_AA5iw-Bx7SuSavAN644FUrT_HeUVJJ5bnEkouVuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FU8I31u8GfEXyVMg0Liw-WsFORXwzpiRilebgsygJ1rdrH87VA4OtdYj6eZ7ICUEPXYHZm3ZuUcBsQQCR7eHgirz75zy6ghP9fg71yL9aHZz8NVVJSfjGCcwDpUPygEQAPT4kB6VV3pcAAHjRHYvwphnLy0oCbC13ZZ2a_Dpbep4bM40x4g_8khZJIk4o72jIn1r_LqZXtAyPe3jjdDx7IEt3-1wSWMnkqi-dmqYwAQfoy1i1A2gg2o7LVm9i9dIRnBwHc6GTfpytvdWuxXg1rCZ4P6NIqVyZlG4_wzaZLR9eaZhIHu_ci-BhU94fQobHZ7tyU6-qkxY0Xr_nRgfYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBOvyD924gwCS2QAEVQP-_bQdyqL7rBM7WNTvQY-zJWgG3mGmbBa59PJFACikmyaQnrtmFrxWDRxYtCyZlGGacLCuD4Z1dwqoCzmHeJmX2TnU_2verxkxFcxEPpIsRY9fpdNwTEnZl8Iwtsw1z7sk24VxqRtZgH40RqNMGTEA0j2I_XcJu78vBZkBKG3X1rdG6-YKL6wUHIGUxtz0JNwHAhhiZOKmezF-EKsHbAHPmkPzqNiO1mjns9ZDHhk1EK2n2vCCGJOWqqA0r9rgZxSfZO6tYGqe_Jd7YrLFPRjYz3sCalqEDdvDyDgShWrNtlRpifMb4q_h-c-JjiiCZMnpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IA8JNGFd4MhCYTi6_kcI7gz6RPQmmE-WZLg9v6lzCLlobjwdob8FOBBBQy6KyvPTJdIrIBDhQnhHSETlai9AWbN4qInLzHUVsk3n2pjHtYlJxDf__BxZVMyM9_tL0icY12fD-9LIy2hpG_q63ZglzcSew2TXvOwWs5cXEO9kE-4Lokui8umGChIAYt7-iKHk9Nb0D_a-jCsEfLAL_hfFMrgu1MDjnvdli-QQ_tsVkmqRRTKkQtis7hiOBrkuWTsmsZ0SymwBiBtEuvDOOYh4pfhvqstthEm6mK2NjqcgjLSYZG3f693CgXBF99h28LOHccM37y0Dn2duDaNljKkjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBz4iLRiLSHxft9lDR7S5O5hn7GIfPOPGmHBcJy8rDfCsahwfvcpfulFzF92MOZ_j2OOK0WbK3AGiWP-Tkab1ICubJNrn0WuFD3GNNxS4kcxrGjjN-iWAnNBHqc_gol2bkCJqOpZseAsg9Mhst6nEYnfWnTnizxQzkIt6SjPRtbPKSJwjHT5I6muN_-YxyqsWikyvN5GaRCz5xbtUB8wEf9kq2PmyHC-QQYv7ojp-j90SaumGQ840rvRoTYbrN8C7xzG5mS55eJ8hufcrdz1QwAt9S4J-qPr7OMJbmIB8H2pyKfBLXFXR6KaNXB_0pBZ81VmqVF6C3p1cVb1ZOdSCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JeEkNjM0PnyYMbDhN00jiXOqim5RZBUGzOqE2NKV93YOfr21FTQVfJwqr-A9RazOXvRWB2umDrcAKBkgbYPyG4Jc1Rt_oxjjEeMqHNxnVxd3Zng1s4Z5oyZyrcNDlhNGiKQrN8CrLcjzzh7F2IKFsxlIj5Nx_qD-7zqgJgSm3XvhIXhSvtwnSsllnBltlmOLnAkXy6MRVnDpBky3GORXQgootao6EsEReoBB3Z5Ib7h_NnHoG6SMM3egke-z7We4K8R8Muh7f_qShpKMyKk5bom4PFBXiNPs8lZ2Ped_pSJLI6Q2Q_DW-qsURIwMRCev24PEIChpVkRPMaJ_wCXNkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHFJ9fzyPWxnvSdqvdDH3vPypixUdb4WUX63bTAwGHxB6gg2cxg4drshzrIE-80bqZMiHvvhXtonxTwIimh_h1mf__Le0ZQAHkdt4TLL5O6hIeokt_tLu97B6Wz2K6b3YjBrpKyj4cCiV9MXkW_4FQ4Cy9S0JMeBKRT4GxGpDmuOIOYSwQSUmPi0fqoX7nJEupURA3FZL7sfvtq71xMEHYQ0NKGxv6H5nc1tHgGCELmyKgvcyj3jj4fMtf6B1-fsehofAcLUelCmTNN5Up1h4oS3rjxBcPnaU2AjnykUtk6Vt4sBsZ1chLLRdUA_aGlN2Wcn3oFgQY_bsxuu85JbsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ENK0lYFKc_P-LymNhj_gVs72hv94gfzWmYE_I8tw_98Dp685bLnxd9GderviAaLzSQzsFX-6q8Nx9gUt2MuAQsRaWlMLzy3WBopWwfu5b3IPU77HIa5t8xtR7Ltl1u0OTGgsOhjrEZzwDShVOtw7I_N2vcmuFI5l-LyyKKXBXfXSmIM8yth7cJW5lx0uEpHyL1RWx7zR1XViHaBjsimTflPxTfjPOxcrQdxub0kPOTncspmCL12qxGAcjWbivb61WQB4KwbXraMhdoUW7hmOQXKQ4cCdk24vPBXCgPdKyfTR8GyiEvdVBz13F3Y4_ydsZFPCxdjirpfzO5B5zr67nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwyUuH9wYLJqlbMh6fwjVq4mPFDwmWujlFgW8NjeWUeESnkuj36yyG49w_REIIj-PMOKe8sipEITWCKEaYrzGczcAMIT4JH9TvdRc5zQK51q2Sz89-cCbD__NW-8RcBM54DYzURbWv6xZqIzmBNQvpE5mxhoKp1bM2j8jb8lL25wP_Xpdc-UKqYMdYXrvUO1tHb6wlOBO5xlNriKfGITdteAhZpHX58pr95yTAXVaKSK_AM5gx_4O1HQdQda4WT88P9k_m-0Ydy5GVvCrl2gjyrtsWiQjtKkwjZC4udCG5VzIu0Rx_s99WBtEpewCYsnWW2cD2G24MtJWNUF2yjywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/teU5VsbrvRY-YhrQvFxwZMdAWJeuYLcKFL39TkEAYUMP4EynoSffc60tSmCfWVJfytvi2t4OG42CKHgCKLLFT2ieboXu90ufRCS1Sku9JjrNlVIC5BYimmSWOiNft-WJPF4lGULNqAxPQqO_WNwBogR2WzHfabXN1R04t3x8fuYiC_ZRJygks01eEmeC_xbx1PaPg5nXES5CAH5gsiS9Z_Tx8ZOe23lGdMjS1RtFM2ekJNJbs3DR_oXxc1_oJ6OzXESbXwpsyjOJkBmMsk_cX61JCRovJE_oZZ-db7wpmLFJuiiiMCxdwvzeV09Oq2v04FRbdWu2Aak5ZsV3PUZWmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CfzoYteUFyujA1w-85ij7R-LyqivGxhAa9uvw8Sr_BVWeeBnqQPp91vzqa2W2OEpOn20DI6wG8Lr4rCbIgBNjstYmMj1V-JL2DFznxKDVpGmXAzTRgNR0SpP9vJ-BcouBzaCSRMo1CBCCK9YVCYg3hsvKEMPdOy6uZ9yVe9yrGKCLuNd0k9K9BORyRWSRCl2nZzYXnzZjgCBj6RM83fXBfhSZSPoGfSd2G85YacMeQAJia_CL2GeUHakEqDlyvcD3jfP_dfIHmyjbFQ9S8s-OXk52NJFUBl9ufpyWjh5I6zawjLGFLoiomRUGF-3PS5xmpqNr3WnuP5yHOoouJO-YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=uWMVLGFil2i_UVl9w4Ky-6yczsnd4m7wwMAo7LPWcs-ex7ouZgOBrYfz74oOyr_MYXlTEYqmui44xLK_F1KhkddhdqQEwLivnxhMbo4Ff-20knfcRIQPJtKoIx-q0uUfS_KrSTimiEoAwoC6mjdZvpNhfXmOdj7tCKe7en-PXJX5fM-L4HE8tzfzenf0NW5MJ-xfhQusZGrXcJO_zEwovLsfRwJ3HjWQbnwseQ6D_4j1_V33ZkOeTFQk_yslfrWaJ5PeOCfGmIDYK8FNIPGd8rpoaVW8K9JlmQqxhTfWZunUeZLNmS1Om_u0n9xyOyH11S76mai0Zodr8kH97vO_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=uWMVLGFil2i_UVl9w4Ky-6yczsnd4m7wwMAo7LPWcs-ex7ouZgOBrYfz74oOyr_MYXlTEYqmui44xLK_F1KhkddhdqQEwLivnxhMbo4Ff-20knfcRIQPJtKoIx-q0uUfS_KrSTimiEoAwoC6mjdZvpNhfXmOdj7tCKe7en-PXJX5fM-L4HE8tzfzenf0NW5MJ-xfhQusZGrXcJO_zEwovLsfRwJ3HjWQbnwseQ6D_4j1_V33ZkOeTFQk_yslfrWaJ5PeOCfGmIDYK8FNIPGd8rpoaVW8K9JlmQqxhTfWZunUeZLNmS1Om_u0n9xyOyH11S76mai0Zodr8kH97vO_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJRzUWrqsKzNCQfEFmnhLyYCBqe3uuIymHmmAtDJziJsV8VUC-PUAYpjSS8K60hH_y0-XB0SHlTZPoFSOywuvf_9ohDWKH4L9oY_N3vlFFHeDUoB1hx2BFlLZ0HMDditgTqHo8abXCY9ZjpIRMZ5YggY0Xn3UR8UZTiAwrsdmTmVQmcCag2IAnC-j-CNCoGq2uu4HgNXzRI-SlM0mwM0m4JTl5VBLNSGGBO1tw_iHE5osTb0naard1-t4DlGJUFY-HN7DfQu_DQeq0JYvowfn-3Su0Uub5dT988gK0Jyl5mkXtHpYJD-o5g7a-0RFdL5mZqBhfc5ib3ZcchxV6tKog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uhweo8CWbXu9h145XvWqPE8CBB3Lu1H4ywFe8Tjh_RX4reF4W2eFeW5nhIeIqSIX0DoOaMqHg1BCLranKyP3PaAutG8cljrLe7Y1pYIino34-zVzhI3Yacsv5rC31hDFceT_UtirePrFAkBBKnXcWk5UTkxCqchmLE4vlQF6pGaTo0oAyOn5GZBzSJeSVGpeI90awbrrOOSU1upqacmohpH_1uGu9aUHWja7eiBnFvl39DXi_qy6MAL2hzmByLo5BJAvjgvQksMyXb1nda8ovc_Eh35XEO7kcNbyALIyGoDfL-DN9rpZTrsEhYawWssKE_yavsOPvLyRwl388C1Kqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOujnYw0bRHOjU3opAGMdC95cqKmDDYifqxKL0-_B_xuU-_1bn4AZ3wmFWzWiNMHqCASmFG88AgMoNLivfQ6qcgaKGyvWTGQMxahR5ILkUfqiMM1EVXmLLDT-9hSz3jOBvqu5xpLL7q4Wpr0xg_b60IhSll9RnSdfdiVVroTTmJubpCSqhDVMzl5vVJ3uZxVifNbq1_e5zdaz-d_55V1ek2BSBPzKiepnqb2IpVj1yvZcUaSz524IefKQODv7rlnE2SHCV9cb6m1y8HYGrdRMUB330I3RjRXJcFeeT-tauyiobwH3_avi7CGOnnGVzHiLdJMeTqyYTmUvMJ-Zt9ZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhHtVkXTjyPKhDCx8HO7GvqzQL9KJ596HHEw3jSNVlk5l9m0y2kLQ0D84hp768t1CXlsg3I5w_QopDSuss1lHY4YVVKgLOmv4aSGS8E6BVtnZouWNaepaX2LK3pUUYoundgs-BpRNBchtBPtXYSJKyA-M5cGfJEllj3L7Zl8EMO5rAD4ZA2JQjNfDCcIkNgSjS5Bkl0_egqSlx7d6weXljjJWUSJvYLJG4A2-7KTbD-ySwrzcmqiiMuPdvbdhiYOY9N4fv9-PFZG3jm881JFqdErYv4cD_8DYc3ho0xqNrUbxYFAbHfjU9vSvk58q2AoVvwq9osgP7ySPYqnxJikUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nm7zkUoapbODj9w1WoO4VlsZ2I6HfqjENRNXhtUygnICN2RdDVTO-wWUXy__6v5xqhZzeo_DD4j89sd3I6Ij5woxgElzIVlqg3VfZAEX_kPaW4bodQG4CKF7Aby2CBO40wpWBXyTUVaSGjz-FV8Px39L1gtXvDKKkNxd02ZoTsIOQRuvKfueJeiW-1_BjJmX7ZioenYjJ8br8iwGSU-hKNayFQ8KmRCnGO170f7cqBl0bMFj9vVju8kEEQ2DJaG1XiqND1UBEUcIdhkO9boDnbubT6si6K7pmqyLXGx1on6ofmRJE6uWf9SJ1IdNC4gelq7vCKAI96DSui51UAt_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5fXSKBxhD-uRuq6IiSgv8AvYK5X__cioDicxvWAJGYg9Jrqu6dbOp8A0iMF3AgI4rEP1bxWdZ_Cb-ZVnE7JKFUFFM4njrwL54DLhNJfaUFdb41Vce4QKVrv2ntRfKGl1k5mtXy9cHVZrBi963Jbl_gbWJ8iKBHbBUHEAWC_DRe9cJ4G9zJ0QdrkLEFUiz6XaTK4vsPu84Af6DUGNO53CIL9J0IZJqAgkxsdF4clxhfAVYAmTvKEbRoGKqUjQLFW8UWT0ufmD5ysEgMqGUf46oWNYLxdmUgvHnoEkre47VzTuwhtMRer1cbQlkQ10BEwmQB3WoNIoqv6dtJhhT01gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INgdyKWCTFu5a8QWFlgUHdyagKMQdr34PR5eFGDpDgeTPEp0m-Vly8elvybf4WO4wfTZOkeUwqZKKjGc8PYNgbyFPwPuevPJUh-q95m9t0CgvbymUeHjJivAB1Ot-RJdb3CX3zer6iVFuwUqramhKeUIf4zRx6b4d5AO8Jw06mFwn-z25dJ0N22OBTYreZSWaL2Zy2cyiWMpF2DEzQjsgni8bU-MAE9xKvW78jQg1CJcv2w5YZpSlXhjzcekZVru_o_aR9zAwuxvAgQL9Sbcf-oWyIzRdWhtKOlJyRhHy1J-MEQSxni0Hf8xFvlNBBX5NlCsgeBKKlPmAJ9mWRjfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUoHGS9T-ErrFpRiw_WpnoD3uYQABCFadQFWMRa2cVM33G551zXuCWXbrBmbkWZVwEXtNGe-4qV13BGB4W2XgFmTAhOfYuEeYSsABi4dGsygjJfyFYfh1OOgJFKCUhrDSyvPGi-VjGr7d6Q1H_nOsx22yR7KUWdg_YoLx4_0I9wGxkr_zNXBZnuKe2IKTXwcLhf6uRA_xcLlmGp52C9TFGjvKzFdt2IA-aVW6DzL05ufHKaKLBLIblBHE6EHKIPYQL7vHZyJl6fRNMf_SaXh0jYCeXGNOLKNM0EJyzlMIBdI9R0xHUQBRmMbNXNstCjv28jrnSpdJyXMC6Uuc3f5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vOrbWlvnzovkEGm6AxrVEJo7F3UHB8lURZSlS6CLrUP-EU6GMW9N54sO3NyjqrbZB5d1wQ1towMhCcWHazQ63MXrl5HksuJrY8hAh2C1gNtNWvwwOx5A8EkMdCSmo3K-9tY5LQdL5Ba_QfAaL3-eyTADtc1SRMnV6i6BiruRo3Y3VG1fd4wRl7NXYRx7WOBOiUAMQzKiTVLLY8bTR82udWCuhgv0zXaMKnJ8ZMJZveAMPvOsfx73uUyrbd42YdvBxkK_cD5R40C3yzo3BdLXWhlS9A_jl7p7ploIbtpbDYA6ze-mORZ7e9uovBm2aiYSKrQsmsgJXn-nFenUELpHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4d4H7HF4xMKO5F3sC020gZmTIg6S8mX1x7rJJ6KgAFPJ-wbIWYA8i3cWsi4yf8qlvtMWkTYwr-EZBFz864798Kw1dEjIs2fryWFZL7d3kJ8ixflxwwWa9FEHg3lJcB6N7U9HDWbFzJHvA38ISHKC7hcqGFAMc6MYlyujO4MKnh90sbh-IduQqp8V-iPE41X7LA1kaAKpLXry1aqWsQoSKEhUHwYpd5t0AeVhmAPSX9RN17eTq-9-BlPgmMeyCti1uCfFYsumc1vPv35TVV_aSYzu6aXH0eMhDfBRJrHf55o_aM4JgfFJ6ARW8wBeMg9yvzyJ1ZDgyamw0EA8UQRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uSPJv_LzZPoUFO2PYhLJpnbbdXzicHjPDiZnoWSRurLP56QhuJNXHWeBCx9cj7-wlVdhj4fwaVbtUX3vw-k_Qnmzm5EArulS-eq2YRhOUEpbvjh7OGKQ62kLSeR-2sGeZs2VoaT5UI3TimNuyPgxALd2bOpz41X-_kTKLSonOfeCN3rcGZ8ojINiliayNNyabiD_9SHL0XVlANlb8s_Dja1alfM1XnwIdzWWU1lFeKxYp4QLkyWQIUUswLD_Vr3W3e_IFj0p5X7frdDfe9sTCumQCnUDeZrZMS_wQC9k1O1DFh-huDIoKSkLPBXEVhEau918msQgiSfGhp1jU-Tj2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5A6HL_knuKd0nR5WbfoUVXpGga7Q6Pd6BfBD1NNZDrmR6ditvyQoG8gZG7Lgx9WaDgTfN_m5Zq_Os10DmMkryTr-JGmiJF4t4ExxZjV9N8uZ3gYI0tMolIXpjeN5C_vnMT78W-drvu75IdT-19UgeNmgqjfXArPXawVSdbrBIAUgg9AYuXcZ6H50p5phk_xza7JXcJUuMzyZECwD9fy9eAJghXKp_CnUnwzLPx9FPoXcRH8ae08PNEBzHlF3m8eIW4-g-d4EVCAQ6b3HfrOm5BcnTLIsocZWbak3RV2hYU-GMmy03xscEICdi-1CdUzfTqqZU6lUjz-sBSjy62k-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ksdbOiRh9CtpNYeuexs5PQh9xjqtt0O3GrpkKVslfgo2MKF2_48GWO57hMmvRMhWuTq8pqxNfOIjorj8YRB4dlqUvZnTkpIUNHSail2xY6A7vVApxufqjenGx5K3ZeW6gLhj1gwpAOuLkiXTjLfwR6WedOXM6VjDeqNhIJhKFE9W-lXyHIMnPWUzhu_ZzWvqEGe2DAJ7esekVyH6YvbI4tXZ8Ke2PGMKPMTCsg_8hN9QNMemKuolfJTxISO3k2PEaxlY3CwrVHqLLWqnWEj03ROuwj_1R0pG6FkGR4QH3_nWayN7yEKP7nWc6YtozqLi9SyiJv0b1ZfgqaMOLlb2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llvbCMSzRwQhfT6ZkR8UcHgGEu4LMcmiw6m9od8JV2L0umU1k8MCPsxZK2YqMTs5ToqL9xkNHtYLoFJ6hxg-CdB_6U0v8r0n-l9J_0tMfxcrYffxEaRH8LGopuL0GJC6I6ZWc7J94FdHXAITr8SEc8cOGUhcrfWSQs4kjrHJLHJwzwSCWsu7CtaXvT5bF6xwQgk1mzaMcoJU3_REujOgyfR1J2_AF3y7IuPQ2L_T3cQsrQSVE06n4rZSK53CBmdNC5303TJFoJEkQsUDkmT1l2tAGtKt_-fo4nf6nyb3ZlXoGd-GMSI-rlClUcSoNFRN353OhevFW6zKIK783fs-0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KClxlhJpgRDLYn1G50uith8xciRIWgyqWJK6YRKhJLAirRJyhbhdG1X5tW7A5Nq8cEjKjp4CU3LUMXrJ4ImfuSVkg9OpAgujEfepEpmyM3iEnOF3oTWZkQZgOgTJRp0rGuFsPiajq7-k_Z0NSZWotPRdcM9FYPfwFj_kQYWEE3AnLcTVTVxEgU6ZXfJ5V2SDev0sktQ4kDu0rh9l3yJR5rfOw2KMutnRIX4EjChT3Fj40wGATB6IJ4s8ijXE4Z5BXTS-IHbIyDJ8yxX47hvjMno3OBh8I3wth_tdWbSfQx4hqtkf_alfbosO41YU7gEd2CNGFDG410UMqYKE78UG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGw-58NGtP7lA9nnSobGWu4Wa15Ej59Yvuo2Q-HVw81baC5f9UeqC1lcsVztPuhBW7sFx12M-4AZSjHvZUWY1XBg-w01VxsAL9gmw3eztOA0rWFVegLHwUeLkVTTUnZMHjQ8g5DwVUkr3a3yr1wfaocW5tacHFIi0dF40l9zwQJuOsYU8cB7UDOvZYACq9V6LesEHhwi9DQpVRzL56etBnCnBXST8OuqQxJdcq0NJFWbTZbtFBg4gFEGx6Pl6hq_lchhUSaxR-cwP5dTJq-fdvKIEgRvVDZoSgHrIPJvYidDoVEQyY3FUZ1ZU6ophnbRt8wMiCtPfd8N15h-GA543w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGhXVM9KXICs4Yr7txvlq45mOFjqpwEMXY-URKIFtaqwhIPv82dt5P6V1KMaTkumQM81S6co1--iEZCPVNFLgkKpMWAULzDXXznLwUVqd6MQrgGYj0RgwiXNDrRK6y0NCvGJX54IE8h9-cq30FPti2PW085vQxkd0WNFW5cmWAprc5ofv4l5aiEf7ONXy_LkFPaGHWj-Nbd9msWgUNvBUMk7D6ZuHDCMyr4loA4wxWJnSY8pI39Iwqcq51cFn43H1R3LWJtneOBZ8Y0e84TK4TMYfqzf9TMeE-49tpG2c87AKizhphaeJ23jWpbBitUvatGEZiXM3qHSrRqyjigZAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C3AUohr0r-uOLlUhcMO-KM-FeF98ZsMAz1AjEW3F1aV4bUOA1dyE9vpDObvF72r4kB1BK5QLI_zryp3ERyNDmwSGXh8qWxXDawZyHtzhMwepgRuD9f_vTr8oHC1ZAhpnXA64DYy1swhigVUZFl1mF6ELUpxzEaii7Hvle8LHuhV1YFyLPIkc8ny9UboyzrPFxDu-GpAHjCYEFzXoMIshT9kgy9v84-E3Ti3QvIBQ-1WZ-SGwOY61RicmoCDVWHQGJ5bpY6fG2J3JjOBdnu2FUlV-a13ce0XykHUPipGl-8PR7UX7TaIiBNpt9O7PLClTMQAekcqv1p_zivGo6pyy2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJAUDeNi_8FM_BS0MzvNnftrJGaIOdo4c9eVLwlEnx31vCiRwbKlLY1yt2nAGBhRZEPDoMVJs3afKvT33204iS3VfzLd6PQaYPONavNU9rIQ9HAlGheV00leLaIKDV_nFllgTaiAqNXk4luFdqe6qHF-wJMBNasPmWAJJ63z1LoYAo-Otxq6BRbHZjtR92RnNJIb66D-F9gNFT4yFL1hX20twnD5p0gfi7oSI_sWalU69hqtzHjpaX3DtjADXVQxwp1UF0qMnaPzFwVBHIhoWNUYBxQ3lVDzURKu_xexQkuvHxgwbxFlnyQl448WkrXDtWLUjH0IHbEsYmwUYpoDUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpExdE5uV66fVH0ysqjaNVFmUOlQ2o0oawcmFARmF-LthT0JAjOvdA3KrVACChOot3NEz43QqSVNxF1m_vvuZuIdqdeOqt1F0r5nE9Qrxg489spfnrenhrE9kksxM53GNJNdCVCp-nLSbFQfnA51ZvSuq7-C-J_dEpNw_cJUN9lJ95ZKvg_-MRBR4h24mJeu98yw2geuqSwtS8vwQ0b2kngVCYy90MGZfuI7AxDZCGs8VxyuZ5vPcPvEfuA35C6jw4ydzMw5LoZMQJoctpmtfiGM7UMUdyazp8-kJ9gJw-vxPpdBufSmrgbfYB55YbhSL6pCmZkDWhdgcVKNky8zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R-fuA5Lx7iRnXpMUswvX7XtmfKvyWq6sKlY2LwuzOJtaIlHQLotl7AsFYHd7VGwnIbVUp0BxdBmVYuc9BiKTScRB0BmjGnG92xBmNcW3EZUoRZ1NRWdKLcypwBkBqzzH2JsLnLdrP4wYI-Jgjxu47R9Xn7L--ZGBnMuDmxnZ9P724QFqFMLdLMK-rQktI2lb_WuV3eO0TDZ8Zx9RJ0i0T_zqkQ4n-m6G2vzF5k2JzTNZM8ygpFT1PhkXxZ9oerkX4gVZi3AAit8yh8FcQ4t-fVATkZqjh_Ay6rmsVTiKtwXlutkFxDCYxlVHNFUziUSPn_7RJMFP4toyYa2Cxl3TAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TuCQ0udsWh07dFPuKYiD93ex01gw2j3xi7zENZNtssNrvI2pYgWHsbPE7yLTP6pYdJjWRkYpLrqnT7c7pFrHRUQ1fDWJVNykC0D3nYhJZtK55jp8QT40_pHImmYtWP7XglqsaQ6Q-ojBqHiffVywuJuIG054O-9dFaRBpBi7g9WthB0WCqxSE7u4-uEzzrFDFjkzsMWapSk0Sz1JD_sDDMdOlLzYX3ZYI7FIwsSbWEuusHOVTvgZ6hgZn45ys9RqAcf8gXe-FCkoLPCMhuVhKrGo79Rbxdaw6hOjsm_Us2dhEJ6Ib2ETai3GitIwj0MX1mR8gL_cyWQdI8y1AwHC7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYb_rZttLU2TNkTVcbOj487lk95uP-Oh0GiUCUP2bourwEH4bJ-6vo0jPY32TkVdRM9z0FAuvuBK21mdqQpToEs9P2Gw-2wd6SXoCvw9GGoxLIphoKeSAKxLL4_FRjj3jfgAKkVX_ggHD7r1KQkV4mHFP0aU3WCy3-zl_C-BvK_9SDuXW6VEHTMBeWL5YRq8FiWuBGzSCLTDlRk_iTPHHQB1Pe_dN_yIOdEqnb0oqb9LNGXXoOZVJ2ng-E10MygXRQFcfGdSLQF3AHLBwMjQUwp7QAyA7-41mRpoUl7R4pXlHjtjjIK6intmpQkLhVmev-BXdNkljrZ0SvldsvlxxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWEdTW4hJGGteDoYVgG_Tarsl-cyiNfDadQLju_G0u9wY1GtwSyl9eofHpaFUOWvjonho_rr6_qcKJ7NiMhT5LeC-xTszEbLuQg-LB5UNVR7RhL7VVFdQnYd-Jr_34YnjySBF2NI-8jP7w6fP72tj10P67_n3MSVtGnizgCMF5e6GnpCwVgYlWv-evFfCi6V82jLdu6B6yeY5E_ucZRIHaeEeiREF4dubKeIHHO75JzJMj5bOaC2pWV6zpXqglPp1tj0I_uXyS_NYLTQHklzeQYq3vhgRr0leHWRHm54oTBBMrpkWXvWK0eoMBFsH4jsBD_95jHMBjVLyLh-Cj-U4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FhPfvt5_UyR58r_vUkNk_MjcOVh9M1R7pagJ-3uo1XG4Sv35Rpe0QNJILkarugX_SKU3qVAWt6Bgqd8d9aqEcRJm7S0U5dasJ_kPcUkbgosXd5Punty2sfFapdEBCvsuPQnWcKnErQV4H65oekbQJMwKBPWvwZXP2EprYGOmI2bjhPbNLb19Smzary1YhfFwrdRVL0QiXoHsIfH07Xt0z_ayzzWcPo9elTgMpbVaIoY2vYChfBbjFc6MKE_dOxrZw5HPZEuvJsgGK151jhbggwaaVIPgVWguFFaegbd2gB0EFRXCuMPkNXKJo7vuNA8zLy9hZEbrhw5kTdcod0ZxRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcXSHS4bHnWkjIcbr9zxZQcXIvt3sJnX_oPWoEZrBw1ksLuFX7CJvSAgAtEtG1ZEZL1aZHaXyeGSiP6COih0EkOjyr_nn5cIaBwQ5BgEF7aOeMdapgKzAgHTDmFqNfx9aWOHFMad3IewvU5b3QxgOXBhwxtDiuY9lcbDHhercRDt865lw3h1fOqhXtW28EcfNTbHBLAykknMtnfcKYiAX73gRoTTkfm9FgvsJ09n8NjHHsADJ32TPmAD8R8O6o9oQRoKJNC0L5VSY4_Tnj2aw2qAvnwYdjJ_zoSTVxGI7i9jB9Boka_UNSrUuEUEueYodzNyBg2rMeePal2T1PNVKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P_tJS5qgxZL79YcxkhTnJECmVlI5A8u_N1cecWUwkuqr5q9pzHn0YdOxkNuGtcZrIl0t0kn-8LU9MZjdm_QRN1eFApuCqzfo1Vx1y_YLQZ5LXwfBeRE5HxArcCrEYH-zTne2LcKKomNQKM_d95RMeLJF37reglQ-pv9xEXfkHkh_EH0wbkbMfvo_IFGy7e73XbsPqOX9TE6lQlSfaxl49Cf5e_8xt24Kj4iCR6KQLuqwaXLypT9FTwT9JwJ8CcyuTDZE_KTfTcn7__SK6g-6STXwvN0cmNNoklQSrWWKV7Hnkdn-4XBxQn4g5vhEueCMSKXCWaJqpEyVKFCW54RBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twJMvkprE9_VjjWW95UeFYAANyIIYAZar55qxBZpY5aFdkZ64d3h-WhQ50FMTw0qKM5GdQhfM_MgnNAWBQcIkDUzM6df-MZ9qpwH3Y7ii4AaCJXpk6NTCAgWXwT_0HKcVvsn_PxyFyb5LxbdNUQ1Sg8D3khQ5MW0vOAwq8pjj2A58R36D1Ad6biGR1CN1B1eyQ3-IX683-1AlFqdNRNJ20GJtd3bhNSUnNlj5trzFzqEQNhCO7huAnLF9-q0Hu7jr0juh3ybR_731LaohMC_vKai-RkL9jmww3DTZy81Vuo6vM2LUWOTsU2jhksGHa5FkRR4vcQPIrOs8jDyDL04ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-xZHeHVJtgwRYJb0SH3QQ-jsIAjO8fsv5F2FDi0ON8dzatCoDH5hvgl09njjscQRyGDcTLxYCuFrqCQDL8PK-3SHW7lPtu3MpK6TPLyLBQsbsxZiA15DFjjManHWCSXPTLwSjreN6EPyh9TNz6kT1lJEUlC4SNBUrxVnc-iWPWsAhs81nOlzntMlAPu7qCQEbbqikXnEmL08NIrjGoBQXtKFqa_qQlB995w2sYUqOO8BGKu4T9gfAr0x2lw-Qr5wqVNvUmDKyQoFy6T4Y8b2If_pDCi-KCb5Gstb8V9n8DSTuIicHnVafOkxkSwBpb200N4n3f8fe-3z_jcz72TXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJvgdzbz_D5y7ht04Ycz-sy7H74qJ49aG9h3A5WsHScXIlO4B69bW-G11wBNuPgX5JqeS-yLQU1HOT3VanN5dh2z3EC4UBCCm6wKfHMU3VnJJ9lDg-nB5CW-VsioQnGWQJTeWSMK4yS173YQHw0Nj9kW6bG3IVICkD8o8Ln9eQZOoWRCi6iAKjgmhV4SXDwf1Xed4V56j0iA6bxvP8X9KaBTWICGcWz7vbZP7KFn6-msVqM8oZIpfH-RMzfzNF3hVBFMysl_kbQ6DBI4KOKOZXY9mbYrblGAzZgkyx9eSGZCqZ4llLdh4DPUvCStDx-ORwEUNkYl7iVLqcJNggweVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OyxuHgxCHrBoA4sEtga7L9zIK08IOx5UciAe-EZw9rpUQQ8xRsqy2mpQCn0F_NP1gK7Iz85lusE8zA4Q7ou3ZsnWhVRMCp0y6_0UIFiGAHaF0FFHOHsCt_rRXYd2vJ4U5JNGejj25BLSNn0PO5AzuWRg-nTcxW1FwGAx6UPTljF6dh-t8JmpIVKHGmr-VudJdGKr5Xr4eyH8kzVwIYi27oeErfPVZe7yp8ec0HTmkJ1VzJ7CkAgeW6BQbHBfPzhsN4wVzL_6Si6wfAwn6I8fHFqyKN0T-RJVyDBU-7VBw_VTGtC99ia5staoyMzRNu818x1Vd8Qwu4sctx_0tMWcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfTMbiIshd205ZDs2o-2DEyifhjnWB3VykCUFFRhehhaqwMbUVGnGXZP71lwMKH3yfswRTLW5ZH3Wo55mez5s3Du5ZfARMzcat5fmhvoYPhSJAkUVDPDvug-8v2g_EpzCq_1qjo7KKdUYWxjwN6tv3TKCLKKUoqGUQfAZ6ql3krAQYTtSXWnlld8LiQ72loQrOFWjepV7JpU6JM5_Bh4_7muNBemHUrOXBxQJS2BfNm4OV5lIDZy88z-pANMzQHUKTTJ7C-zSDyOj2jJpOsk5QIvY2SSG5XtZ6UbqLf4tOxt8-RSVIwLw0-TiO2ICTwTTtzTLMjEgHRU3LRQbdJmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NrKteb0kQsExa_PGsNfm720jAN9uMVg4UQZ0ul7dJRgkKSSq4lBOtbduLw15m1ReqAHEgKLRNQMtdZqrdpw13Lwl6aLddpWvECIv_pV1Sts-T_5KwI2yNC1IRVtXQaPBvJkokzIrI3LQFRUwFkDW1ZYlszrupYcJwfDaEVfd-2HwLGXYKb1yheOF58VMegSNI2ST-SrGDgCJk04eyJ3tLwCXg2zWJs1QeE_c7Ec_xHCMm2iw9KhD4kYvYiFszqs9evI_sHN3-4_JvBK28WsVEgntnqCrAkLMKWfWXE3vd38bqBYS_9DDE38dBRG5IuBOIl88D58IfoM0o_g10fJMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJ96oxqMdidMeZ1tW5aVar111dISKBMqdJBfYlZKbkpOcbTPhtk-exqj0-NDVHLjCttvBjhwBu99eWW1qfS_nQo-6r510wBUKatEXFsG8ygh--pZrxwpSvf1iDLpAGWG3JLt-nq_Li2YuJElOvUrQ1ynWZ5wRgwTbAeJw-l91IAX5OY4NHIjl-AZ4KJs-5tAu5c6RE9FeMHyW3al85GiGOjTZgdqdy7urSBQ37KOnbNR23MLLK0UPHIY5DL92dmZXYHRu6fUAVI9ns0nPD5urQZ978XZKuuKK96rK6huesFU9nUzpbiTxYoAT3MQddaRCYvHk_XdNYjy-Sy3iyye4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U06ZU0AhoW13hFLBx0ZPLoP-ApQEdDIjp_teMNr6lLD3MdWhW-GkO1nesznqcFCUZWnFnhMTTfchtW3PXAt3fURJUt1elFUEO7ZbOtEAyhoFjlz7VFm6MGhsYnjuxUZvObEfta_zL4H__DBoJUnmyczBaCgeIHn59vApPGVwBkh34Em1tNi9VL7D7ImZJNBzy8Z-n-VDjaioABAxQf7LDJ1QS7YBnwgfPs7AT7ksmxuGleptEp0gPcJq7XiEl1U4jCPTkuvqM3Q-2d-F5tB4hRLapzsVQnRybJcXOXP0Rytl2Vdy3Y2_B2qjZVoryX7xAWgdzgkya5CB52cA2o84Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BiIz_BbDsPa-aCBib2M3Ck0HL3IlIN4ojlUHhA1utq_tghxvVfYrGTvKJeRiIN91ljxuikO9f6G1Vn7reu7HZsUostPafeAIQFBi4CZ6UmwvXC3FPsNA475evAAd4ia-NCMQQcI7i8fCILWNCNtA94tZ541ntfSSV1lPySIi_v6q-SmoK1tKA--tcbggh0ZtnVaOUkE8nXl9iJLoLEhz_d5ENjvud1xePYnOCoXmO2kWY9wdOJ5zd5W3Q7fcxKJQdhEicCeuzXjUN-mAFBp6DoV4ybMVNk-uZwRFUN5-rHOvOkrwoDWdLrobZWaP7xiZ8anxLlg65QEfj3T7hit8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfHMrVswdoFhftQFI4WmAEf2z56ScA3myrtGNwJ__zkoNqDQwCooRDQQ-Vgul47y8AcVWZB274fD9aBBjNiqWVHtiYW0MFKgBDI41dhpZcz2IYgUTpMyazqwvdE1BA9_49hCz87rAlGUjIQ0ivajJxDJc4FZLdGJMcJoAXAITDFK9ysbQavNGMscb4qx4IHjpgHiRmFRTNrl7LjH6MXWy8WnsMaY_pcFDNzta187a-GtPfaHJd5AQcRFmh4hkAUwLFNLyhY4yXqr8KGPFVXIdGg32b_qDCUZSFamMgLn533HrpAzMwQd71HQ7SKM1HQ1kvaSuswki0R4m6Hj-zEWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWcW-abm8QnEyAcKxQp96lYxK5MyxL4RBXK5w1Sftf0nIjKYiKXUhSJdAjDG0Bi8ZYVB8LHQ4RozVj1JKSBDw19-4JVuu9uOw54e1JP6d3Uh-hraXs2WQewTOj5FINxId3P-Fy7c4hF3ZtED95UnB7ZTb4-81QB0pyXA4XrYV_xZfhpm0MwwliW1mKK0EZuHMYG0bWNe3kYgkQ9EWD4XRJdBMGOAClRq-L9PYWuWQ8VLLaPR8mIsnnsuyaG40rygXNJw-XeXKd4CA8u57HnuG0Y556CILfBfltKWSBD6tZFz4lxya-hP0UftlYLnnnu_k1AiqONOd-MW0EJoFIz7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjC9GTU3gJeNBXyXwQfntWfy8IOZja_aibk-ONqT05i2BQOuC-j95Fp9lcORpKIj7YLBXQ85ZKmXpNk-noNGbEgPW2hpQUUHjhRJ1_xmtXDOeeH9p3rEGeUEh5q4wpwqEgb1aU0Cp9lIKyWNlNaKU26sxVLg0z47GZS6yLaO8gZaNE0le4fpQrh5zz59o5QOML6z3l3tnVYsoXkFe_PKgTZyHqrMiKK0T71Hv_TvLM7ENFxp3-1ieaXxbrYIF029cFEhyKlgS2pxcZ6N7UvyMkVGx2yoZ3wsGy52uhC8DbR7qiOtzF4qXYSuYZBE5MD3hY8qnooE_mENMXKiLR8yvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S7KQ2eDlAXpKQ6RN8h0unSE4_PKv1CSyNK9dwSMITHPaYtCuLoxvp6itkuA5AApJhxpN97EDbY-eNpId-Osa_lrdBn79ZxZRYdT_befy8KCbMALapMbZIHtQK63SzVRJCuDpuUh4N9u7sxDFNszhI71t-Qs5JUTpM0ROBrPDNNyrSdbo777xWNfVRKnZpL-lys5K5vNQZE42SQw7gMwUOc0Tl4L5vgmWTQFn7cTgzmMa7UIUMHoix_LlYMwU8vaYYNzjfuW52dWnvIdok29qc5u953UeFwjD7HfRfuWNDfraocUF7R8pGzjBHt8ZNZ-VQ7ce76PQ12fKjF32nnr4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pS9RGKRdtU8aTssQtK6p_3XFUt1HXXxJh5hy_9ttTcZm4Z0gz4OL6r3yMkXzmBbq4-o87zuxxemcQANdRAnnQzzrwYTxo9jw5vnpgYpRWLBUINMxfL_hwSYd_TTOXuCocvI34CI0rMzufVNWhR7NWhV0WaL54wHnDmR-DrXYuRnoKiH7ZTWhmw4LGbvRgIxa3I62WxcVgVL2IUWx2f0Z24IM-HBImH3onR_GX5T0hJ_3bTV0J8gz8uM3uj2gyEJZYCZb4AHUiFIwvkhBfxBJYzutbIYTTept8DXcaFTI5olnpzEaW-PQAKHp5tJ1z17Kwv6X4FBe9hH023kKc3t3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sSofY28A840639IKFva8_nxFgrjeJ-rTReN25UqBHTZUlMkApAuZa5N1O2sKvBqCuWFs6JFXybglvz5XYaDvJoIPKVJ-4z-K0FlrbX5krcS5P3kPbXXuX-OzPQRvzHex3gUIVoYXMmL9On8NJA3izezrQ471LokfTt8RuYuEP77iO2XVcGhXTC5tgnKRxXflOaZxoMo48SYaR80N_ZQMuLQiUNYJkvO8l2oYqoKKfVYX-f1aHB068tDVKIRG7goC6ImIgTC1La0c4aQNNBekOCO1mCrlt7AMzo3jdgAPXtJXQsQeBYfP_sWMMHRPtM45YBW0Y72KSeK886e8ZqMp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXGCszLcOTgw7IqIZbc6r2VH0e9ihvPt_PD7dmrXtg1hrv5z-D7GnsiDq4EpKcH-u187_MYfM0pHTO9bZd2QGKQetKU_dQF1MDQYZcqGIOtxKlI6rhP7LXD01fdjABmD1EDaQSCnkFOwj6AjgiVl_nH-U2pFi4kWh7F5vN1uPtQu7bLvgkB3Dwa8Yf_gkJ6QhMNTOg-US3eO4Qc9k_7iQR6IUfwSHbLto6GN6Uh0lQ9f37-vye881KJkzPC5-JcIvzVz06d1DQ1397tPlAVyNSbtR6YUqaauGzPhhnXlNIS2zLwbYA_LGKMP_LmkCyAxZ5JNw-RUy-kzE3onuBvoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PO0Ql6hT2eTAtklkTbWgundd62m4sKXzhGy2pdt20kwRNRkiuqDjxKR11rXplVNsa3E35gYEQ4O8HAbSVYB0ZLxvdxLR2-301yWu6Dr7OqmORkQcUl5jNrXx7Sb8VYR2VP1nb4ii3vxGEWr1shM1cj2dMUmzO2XUF22hgbg1p7Lpt3ksq_L7q42FcPiMFmNp-tIwMcS_KFPpT4I975pYWA9FEh6kawYBJ5GVr4TH1iWELabhi8VvVCwxpg6wtB-dC6hXQOvjUG3Kf-DjBZZeU3pd-O0oIlMP2xUrLLVjUADb73Q7OF5Q0ISEamD0IRgE9WlCP7IsncLjuqIbPjzBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5h-SHnQsIDxHJjDA882SgLRt82NNjRBqgOputi2L6Sk3SvMb-EN_sqQA4VnHL8BQlozUNEaG21E6uN0Stt-m-oU4fUxD9MLy6GBlQos1rEXpR-8JFPcnzA4jujrGqmgHWD_IGsFQVndObhfWGpXmkCgo0lT-a5CnSgLCeCgPchu51t3z91tOfQmbraZN9MyVIowApgnPyGeW5xUJD_JOHok4gGj_Rhp1R2jJ9jvuPV493GRC-pPdweZOuptk0fJSsa2WY0qD1bTsUnbf-JuJfTMwHnFUjp1hZDsQYmJDwdp7ikKGTDH6hVJdB3u3UB-y4N1YmTIIeEHZzB43OHqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fBR1id2J0nM218zgwKK9NR5mq8IhkXUXGE0TeT2eaRlqLzc1iR75dGXwpdRRmrToIicUguTwsTGX0X9ltK830SoCuoD99UgyNZsyqLHlr1yaXxJOZsvYDorWODxBKL4sct2zVEiSj8soXmUdWQyyskMe8v-MeQf491up5pdBfTfgQMsSg4EFkcgvsbm4ubzw1JUkENI7QbK8qyHG1l1j6Kl3bEofEoCMxZE9sDJ9XxiHvm-UKBNVisD1m0Jb_IV_6F7QhPeBMhV4OqOF3-fEanUjwNp5ku0jOj703akDDahqkt-0TQLSeYrCV_dbDBtpsY48tHbVf18eCbUrzwyhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AZr25kj8kRH2Ak2hl2yCTTCKjpeCjcZa8vPXu58VPQAQali6Gr-ZWyMMHEpnWQ1nsWxZskdeYw0jLMQeKzeKlkS5V3y_qfAWjJXSzmG9koO_jW15Z9lL8QPotQ6kgTJV9K4kebvbR_37j8z0avy6KMdaUjrjlCf1qZ1qQjSboEi9XqWbBO99sGennD5VIj24Obj_vgWXwAre2BGJeLzXBae_hEG0t24YBhsHXq6XxQYp_oKn2w7n0warRDN4KR9BZiGaVe7ymUkJPNkPpzNrFtS70h3zS6hLBlzssyRf5KMo9Jw7UmsfOVD0PqJrdQKreH4ordk9FOT2FJSYKAdhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0vzdDOtB5Ru6abU3vk2tZI8G-8h961rZjSKv_cBmGykiMvj3yi6S915VmWPRt_PnnKumdKKE1XYnxuAibINGGbmR52-ijAYNkTBjvo0i5TDyA71TfVUPvtitRPcGCSEICe3otrbEClk9RADkfeQfCn-XK1ftUCIDnvbFXp4o5WkCWXmDdeJCExH3CUcqlnc-4F7WQhlG78So1CXFAt35cROyZx97fPTflKZ9tKRLlWEPsOZpfvJIWcmIlh9IN4m8jvzYlQeiBRb2rhVgvVaSbIJX_fp9GqTqbEbiigko9CWDXBM6KYte9LOyiebJy8CucVw5U4ObnP8yYIYelt41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFLS73suTVOETjwZsDiv3Ng-4BlFc66OpxQeL3Zj7KxwT7d2FSO8LmMMz8xSN1PYGWmqakpyPjoPukRG2eo9J-G1jt7Z6Dk6lvOcAh-3ef_DhnFut-eKUJGG9RgeExSKX5FZ80Z-psDH73ZN6ov6nhTT9WYNSpipjFQCgK6zC22BuERD1O12V5Vi3PikxD-P0L8jr3YMv6PD1L4L3GUELcvtiKP1mSLrzhCoiEaIz60gYd2nMexACLFpEyl3FJZTgG7KtismPkK5XOoaPqA-U432OaaRHr9DEvhOAEgysbMyc1O2b-ffsrsv8Q7tIpvrYBPpDH47qUa70QXoU_IskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkJV20qzjTeJZGkBxPp-qOWS6Ff6u5TZmm7ru1FVP9Ebt0T3Mqb9Qc15an-6isXQjxs0niBKUL0tkfUDxLg5Z6OgfHgpZxG1VVqdVkDgJ_2qywEICt2aN6Jhbw4-xaivlVlBrw9r1km5TjKoOl7zKhJ-zOFWyWXYB_btroWigi13BGDnCeIIm1mMYh6YSjdsyT8DkaEoEBBDgQtlfN2dmfXB7g6aJtY7Lj9xrSvmgwXP7j-KSxlF8iJ6KlkbjiCZi-TS3UqlcGpDnPgm3t6Hzr0xZcJx1uC8xoTWO8MczGoKEhceK0hb7aWDohR1zsftcdSwciNURlgNnV_vRzx3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3GVfhwZ54IMmszP2aFYG33Wu2Ho8dYxV9X5BiFpw_TZNHa5PZGf11517B5U715mpydV2MKZTQznVpPm_ohNVIcNMSbAO9fqdvdbVdVCGr2isWlcQef-nEUsgnS3iiVjEhlylBLFSbybodLl5C4tnQ5pIfqbSJqaelyQy4ExxdtzWrnzrTFbhUNmBlaUcMLH7-bHOPq0y9FV5UCQbqcvHHqISHB70TB_5dX9LQS46jrowKLxlISlnAGaEW81om7VBMHTyKdIXjG1zue2oENBK0y6AeDQordJg4gLouZLqtJ3oimSX0JfQSnGk-4m6h3PhVY9w_1YrAHmMM751iw_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tDeHnBw1qlkHLUzUB7KH4O8QhsEyFwxvthcFFyVdUUdivqydpqgHmDHHv-5JAWV-Q8u62R-0z8WHua3t6-wxV8fpeVpFjKq6QvXsIhmKKHM66G3BOIh0y2GWZ95r73l0IzUoRn6QfkrsGsip-aGiB2IS7yf_6i7PxVl8W2fKxcXY5YbAXRXylVHNXvVdVlmE0hIYeA9olL7oFbPWghz2uMNgBZlOyViQQbS7MCYVLyteJybWfjyNw3N_NqWXDRdprsQJ0L2jv5LfOpr_FAknUAn6AtexZsS_hcj-rjS9sK591xKhsryRiFEN5UtSWzGBjM0fukxlXbqhdEeHgCObJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gpuTTBo87Di5BM18_c5A3Cun9QAlecW0XxZvVhh3SNVwc5fsFtSnz6CJIXAGFKuFkEZv83MP8yNpb4lIUJsOEcEMKbZLVryIA7fPrE4II6Yc33va_AXqppXqzhQErNFnoMAqy7SKPdmuVT8pBIfMz7V-Lj153DU08kq0qmedhsWDi22yDCPE2ibXUbwkhJUlWU0vg_Ma1z9-E_b9c0VmigexSh0Xzmcu55giXvIv4Uw9ggqffbTfu0YKbPBrF5B-JnlkcwEfgtnaqddFGQYDof79ozzbxtUUdjzTKNS65Pdtsp9EwQ0T_hC0SJrMLUcsr_Mg2-nRaChRYYfddUwgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RE6fVLd-naSFR_RO4_pXP18HJNqcNUbA9NLZcGYV_nWvPMhovi86eXXCVr7Q0lgJcUac_Xv_vnob8fgrj7hn48-pCvamth6_BiAewrvH9gNwFXV8y6wRcEwXdZg6IhYnBMPKSgmO33ULufvQzO-Q8zJt5cfpiiFQYW9Qiihl4c-5Fhvr2aDuSSJWkmbmOFoKGlnmOl5tq37hdi95GsKWcTjN0FCyNWsxFAMNNo4qlNv0Xy_BTGrb-5NTNhXVuWafMH14E53s8EsRNUyZr-9UIAr2ZqKqj7BtPjDbUTr-Pr7eaYlNrIe3lUZhjnfh9JdURSIp2XKwo-GIP8s6YOQ_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fuMg5Tb0jio5bVIhEksAP0ckJDK82bdZL-mjtRTjGqmHyPWaK0boJBiGcvv4tEURssyvWKqaTMqYJ3wvc7rPZHX8HfmX6c0b93WWHjflM968r2-YN217GAg5xtwNbBD0eJOuK8MFf-WDfJhhjsnIxVdTiXb9jBhkiAEiCTlR09CghOmav82DmKDqwX-p5tWA6V4E7pIgJzrBvApzU5KvcdM0heTFQYC1A6SK_JZknMKCjm-Vhj8HuEWN-Dj7ditAydjcTt6BpeXBlpnPBecSYNjdCN9mbZtI4zMxFjk5uhzreZJ234YezFgZpcXUdl0aFz6R0-LVr7kxza6g-SET7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EfIR1K4_RV51qKU_LbSqtt6JfKBIdQNNFywhoHmy5xeSlvDmDm0Ex7usodia5ceL43MWPeD09iZd77HJ-tejjhFoy0ZdnJREIK_bbjKiZUDFmzwW3hImBg0K0rRV0wtN1w3LGj42CYS143IwhF2Bqh6OqJQFj353MHxWGTYp3PwuvD6C0EzuWfJBWtOZPCzBcaFIEpuuvRpbtpyUApYZtDWM-d9AcRb8jTSg5mujZt2IXYlXynMFha0MTa23TgQOyfKGf0uSW1ljEJy3Q3QDhAxKiUj1yHPtdnBDVpqbmS_DqNg5gZ2gKEotiNhgFK_Fp6zqKZxKqoZs1GJ3KZnwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/is_luea9h8nK9qEtxLknd0tx-9FEK6asGR2qxhoc_duJLPAi3LM5AE1jUuEXtF04VK6IqNrot4hfw0YeZRB1-F7mOGJZXde8HIMhiNlUMYd-5YlI2XM_qVl3wP65tN034E2t8W3zvgJdlFQYdBHG0-jjXoXPk1HGA7iEjzXLPbTg51ftBSRH_RBGL3bBxZGKNb5qKHZ-FXspTnQM9CVfO0zpP5GPQSVAMT56QZGKMp3nrn8B2XZOsBE9d7wRfSj0Bo4yw_BtsdelTzm0i9jIy0jRaKUjv0HMq13bzzb2upeLoeQ7vYmKqkaKyNiSEOCs1Qdp_HHjqCf31LaTxFlgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TdNpbPIgoNz5BJGeaJ5e9QXykjaBYW-IUN0D_GBbgBTBR_ZjJLGci7S643DlyEq-1TUlQD3WtesXc5CO_7JnkTcnBF3ezg1RiI0lLJLEpSwWqZtA28br2FYMU47ifwCiArFL5t2BtAw4t7GBGpmOypShn41wX3_3O42Jat5mqUCtkZi0Il_MidhWRtvR6Yw3lK4onarm1LDjh3xH6-avxie5tTXTMdrc4BZGZSFdZ6kDhtfrEKOkUKoYyHGszYjjcNZZrfXSDQ0gueY3MQ4IlUtLpAPhqzFWJjHNDh0XUZnCiOG57WEP8IUbky4u1bztHZcarbrdKP_LtpR4s-MhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
