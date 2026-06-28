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
<img src="https://cdn4.telesco.pe/file/GwvI7TEWlEkM6nlV-G_9yu2Xt8E23CWrv77QZseqyT6t2entm9VmIgENXIZQ4UeKQbS19kUomMynBSrFLDrhPkvabU2FY8RTQLH81RrfEpkMvSExP1b7VWfS8Gnro8X7IGgBQ3vCI661ARtTrgWFJSbkynfRh9CZMHnqW2Azv9EVRuwZUrUqRDSeq1MNDc4YWAcBGoeVJV3CUyMcoGu_MzDTA0gwvP7U9RM-s47k7hVxBMBa9DG8fge3S3_jn6aJLh73rDIDu74fqOQKFPPYo6QO6Bf_GGkn_wtn8kf2fFPPkLrjyea8byh8iA-23B9-buGFvGs0uuQhJowqJNhLaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxFfW0kQudAIZzdRxQD0fukaaZN-ceG94X0UWpOuz1xKx4LX0k6EQ86spDBaPYiSf2NMBoVFoAY30lN6u34k8OoueHYF8f-O271iCEj8EtPWyEPAiqD1JuPxXWpKJzpXpSwjUd97g-Dw0sMEX-QAmuQF3qgwiwTzsAX8d8LxtU8G7wCmoCBDrGY5kGyTinbej2J9Pp1r7l5K5Db_T2ZbN9hl61LpRq3VhDEyA0Infcz-hHcya8jHe-vFoL9gWJ7pwhFnLVBV8rAW1kWKa4w3eXQL8nYTcJjRJ6_Ehf-8bHutFWH88S4ZXL2A7wHjw5kW2-Sm_3pwa4KyTdY_ELFKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 267 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 497 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 632 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=IDNaHCLgPNDPHwoO65Bq_dN_UIwwUQdqmlrPbDVDaQwPCCYs_8AwL0yKPWwskNIQPmwpw4CqNL83_3IsbdeGBElt24BBOeW3V5OWrdFM7SYg29JdTnYrys_wTdyQQoGkh7kNkQ8Xj28UC4uFWO_7MwHYSWwbZ_BK0UIlYMLWF4vasNdMFmM2TWHln6wDYSPLYELUX-hOBSYBvx_H-EuC88Vl3Jmoeh0aX2R3_reByTCRy6So0tc9PaZZEJd4fcPJ-jzrFJQH2-Pp1bkNDK5Z7QjwvMh_aZUA4jcoBwljILTK40Ouf15sedfn7nwuts99WBajcXVAFws8PBetbkZQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=IDNaHCLgPNDPHwoO65Bq_dN_UIwwUQdqmlrPbDVDaQwPCCYs_8AwL0yKPWwskNIQPmwpw4CqNL83_3IsbdeGBElt24BBOeW3V5OWrdFM7SYg29JdTnYrys_wTdyQQoGkh7kNkQ8Xj28UC4uFWO_7MwHYSWwbZ_BK0UIlYMLWF4vasNdMFmM2TWHln6wDYSPLYELUX-hOBSYBvx_H-EuC88Vl3Jmoeh0aX2R3_reByTCRy6So0tc9PaZZEJd4fcPJ-jzrFJQH2-Pp1bkNDK5Z7QjwvMh_aZUA4jcoBwljILTK40Ouf15sedfn7nwuts99WBajcXVAFws8PBetbkZQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUICz7w6Ws_yGwUNNEl0YpX9Xgv5Sw64wV_5ngOGHt_wS4MAuFNkDE3eBMk7Y2UFTMs27kY-XSoMQku0AkOBozGN9YkCTljtq6j_JGQLEF7UuMcU5RIITk-ppabgto4x_po07I-1yjxood_NQYllLHSK1imEujqRcZde7gKRlteZ75inJLr1C-YCaYijRfudicq2zrRt_vGNs0kOxOtOkwIxzwixaoTP9Ha8d-ZU3kzo6bpX5Z4dvu51EGeb0oRilggGFFlHNah3GBYpCS3pwy_9Qs5C7TClIpJzxGTRtWatpG3CFNipYqmtgXiji71a6yR5Z40KgA48TuHmkgkTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eub8tYlOPvTyMIWs90ch0B5is_coUEQg5Z2Gs_EqBz6kCyNYj5T2yhJSwDfpO2ypIWDfc3uCFmsPuCecxq0RqvGUV7Yp7xR9bq06hCcs3hv2_NX8h_pZA4IcK-6R_LUDx08Y16U3XYLtDRP67ELt7WUgqh-bO0jAGkX9u-jJy8kMOgD0ibV2wdh2Kiu9Gxv000ozn7n5pZRZ0277q3ClJ4fMdchvmB2WO5bFVIo91mgXcQh7xA4EJnY1TreZ6wyokYjaYeBYENdmoM6xiq4sU-xfZKBIfOd2pV-l7oy4ogwBW7R3BYHLEpC_Jm9CuMolsqth7Htux0YdRJPpCsivgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0RMjOAdxwL-BR8hMXMvoDxS1x-irAFqKUycceWcwFzbDlQkjzobl4pomFg5uxsuyjDFViIFwNvVTobr23sUOVcMgLaToZeXZ_YC6SM6BgyZOCOUpOOTXua_jCcdjGqouBw5HTT6QjHuB_JMlQejfPevNAKqi-hFMUfX42yEL92TGXWirVlFo4zaBn77Q65v3AfYkTqd84qDA_jKdn4kg0qcp7RqldF1M1o-MMds5Sx2aNB4oBP7eEOv57pWwaoX56PSJjHWV29QrqJi47dkmmH_fRwhg8ShDxHD_WFsElJUsk0VB7GegxaZ1PR9SYlBocZvvvbiebiSzmtoGc3qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNwbh7gLUWVGxn5HJFfuA9bp8gUEgSj1_1JR0fpsRNOzXuBcH6-p2T25NM97rPmznmCnC3KeuiTx6ksVhEF_YAAy54deFVZya3YHcsw0k0_1ljE-IMkFCZa_iPw1bqjrWI8OK03tgw0LP2byrSbxqDTyzJu4gO2ifXGvTdlF8lHQ9cG_61k7upe8FpZ1VzZYmKn3p-0L52htcwAzHfhMcDO0e2iXdWqMitfGKT4F1ANI47klF_pncgVA0uTyYMnD84iFm7thu38BOyKMBp6H-uAXexad40H7BK7DvymimXvoBPHLlai1fw73QWSbB9pVsvPoNiLwFAFGGIJ4hk-GYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qboub9IZpFWKs7OMPRgL7Dd0_zzl-TvGzZH-S-8DRblUP9xBQlggITzpvn-9BUUcZCyyjPFENXVA2f3WlLjAbNw3_vAzQLTjkHjnnHpCrab6OqJ2omHLPWcykq33ZuKyMcT0eyXymOGs8AXzoeP6YtOTJgI9M3aTfVsTRsrAOIY272cW_gKNURueDvaIJFLDrMy10Hw7I70o8Y9rUHCSU2BfKYx0eBKyO4B0oYOiKsuiu88KcI5FjpvkCWvuREzkt8y27uQApNhYfjaKsxa2apDI5RwfpL1kapUcJpZtb_WKR5g0yFf_9u8TGFTuRTYCj7rkdD_GWS4t4qTz4FOjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNa5UNqaMoe50dMd8eTBDuhzkbRr50lfkRgLdB575SVY2DVtSGXFyMC0PFl80tqq311v-vZ3NVUlLCxT5Ynt49Asfx0YK_8_h3gVWE82qDIzPrblCYFOfczwE4WXupBIs5cJHC3FNyPsFrNCYGtSonSXYMCumfet6a8MCDtJelMZ_2y2ZYktCpjGiM2tUlPQ9E1GVWjhKJ2w6puz_meQRqCEXWTmGGTD8pZLhvGCY_7pbadCCfAA_Z6Uh1dLWKZYeXU4-ruhbkR5lrT-4kx95XlbgOfms70zwHBuNnNATsLHmCbT8nToX90M97iayXv3xenKlHev6OcEAHoWJ-VsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWEgE65l4WbPd2PzWNCKRTgkKzBVXj6Tx065DFBFBGJbV08Bvc4lvXYx5kaPSGvPHV4Uco93AWkkIbVLBPu6FLzW4TcY3ro_HJntMvsjLXJEMuID3_dekfjL3UYuGjGBNZ_Uu06AfjIJrBr-K0j3N7kQlhpAM9Vq1R0YhQwfG_xkeWdcV6kB18XTIeS2aixH4sSKnejOsOcqeyiUrC3wxuVngD4lkDbbsZjy8twPbQSXfvuUwUR8dZ3mOffzeCtePYvZmtRUWCk19cJyt7b4SInHP2tx897z5Hfzx2szULQRSLSHlWbOOSWy31j7v4Cvd9j0yLkEeSAPH-LOp6pppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqNXP9vQPL3qOPVcf9_sJvdyWWwBvnollhf9rjuQckUcaqJZDW0ixgBXpXicXFDb7dg21t9wLeTLXw0moWxdyPcSf_6fX1HXpEq0wleiirgyw-PyVvt6tazdVIOu5Cd64f3AKDSzfsfcOBmSGP-yTkwlS_FiQSGgLPEmwl8MqT6Q3KU5QfKeuA2vo6HOpQ9lzajxyiOjDWO3mogyMPTmMIlLOIDVPQRFPZYuX2DnjpVExHUPyrb_EkER1746_LtgeITCifE7KMUUPuxf_R7O3h3SqVhB498XvI8MxCrwmPa2cJ2Zb3V04ulD4h1AVA2qEnB22ZDpQQRiq95p_uZKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el08rSb6U-qjK9-LFUMZ6FaGmiTxZ2i0to3RIiEHd4wg3IZoKe1m9FcaNO-96EJ0OP-Eu-vrjDaX48K15QJ0u5NoUKYO0EDo2FxwBv3wai7nmLTNe7YIR9E2igWWR26i_auxijJVtiHBN-Dr7ed-WaLp78y2OJGoN9YHrMyQ9uF7ek9nNaPN2Hcn2G9SRYxSlDvKil7s5gtP6Z__bkgAeqJ-JXDLBlvH6AxjwAzT_kh-EbW9SbqWEveCVSeEWNS2NOKXZPkfqp65J-1IjTltg98oxirVvJAZoNfoewo7gGH931tvV7ShJkKMe6MlasnqEYlqDzufhAPInLddm0MJrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg0ihozPGLALS52N4Pqgfi1TDmNRJjgEk2hsFIAFKXEjLmsMFJJ7tewFOuaBNe9z7SwEfDUJcRf1Nkp_cXr57nwlgqlTR9zrT6d4k-_h-oK5SerykhnPwmccCzCXkumq-aWSKxoB33-bu6fCLnUCTDZyZc92Yw9qyVY5747g2jsVgthOxMljwgsYLZ1DWjBW8uxsXveioTIEfYSWhJ9oGVJWNwXbdJfCFwzJxChNjlYeipTjmLIdziLMplNe0d8LBowtHQ5mzTFDB3jtUchM9aL7nzydokozQe_uQjnOJzVN0LbSdr6KgKfIBRGVq0EWHX8sLOQMPUgpSeny9Ii4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3F4-rR7NAFp2abDLVNmQVJLsCwq9Ce_1sqK2JNZOHCySRWkCWroPYrj2y44TV47BpyBfoPunPPkCvNCaEs3Sr7Yf4YGSZgAyy-1GTJICAYV4s3VFzu7qIbwh7pO41vt88O8z9_Fmzo8LZb7miq3ex-ZgTtaXLF6D8vmIhdrg8vk-Dt_IAfROBT6NkOtPtrFq4l2iBrXAk5Xk93CQEG62Tdi6r6LjbbOdjaGy9pYTso6YrzLzfWVLySodN_Rz_HsErFU-2B-F5243ChEhHUmNCP4cbEDB67dbnqOIEcv2SqAZ8ENJ-64BoVZ75S_w77xW6vWk5m5haNk45JLdA7-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI6Bk5jfHhyIabeMlLTwnuAdSXAs1zoUo9M7sXcN1gQCPALCF4S-1txPQKD4vh09zWZu1BII9P8tCUAkx6qxKhLM9RJaHqo_z2crGfb_o4u6sxW-C1pp-D_kFcii7h3tHN1OWy19xgvt6ZnAjbDg2dgXA56l1kcIKbN_V0fXAek6uLGK5aygeP0KHeZdR6OBJqulZQB5ZskYR8rnT08_VrGK6iA0m4BvgBm68Vs4abqpRl85tiT91Gs3B_CHjQVciR0Hknba0rWaOGUZrjJ5aB0tBjK_g-hNRHRpg4l_JE1hw-OuILu7gZRdM3jU3eEMigQJOh9piWQUxULCcqb6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7aC3vXtcJ7upCp-vyrnxKBljjKOORoUPJWkYILTZ7FdyT6GczzjMYPko5WnxPBXSeESzM9DZjX8Jlkn8Xh9uK4hcQsscRQXUuzB-nempCAntue0tdIE1XwGe73Ivs6Dpun-PUaCJXpxcle6p-jPJTPED_nuyZurevvv9dYpjorKEVw0lNgcDe60kQRqfYGYWz_qJ411DLcQrA5qner0lOE1x95kXdor_95FVN_iT1rcLXp4XlGCAeSu7b7DuMohgoEKeqZpo6KX6f8zrME_YnNQPOdtIaiJa8zBIuzznYf89XF8glvWRY2b-gZUDCS1z2qqPl3PVIYVz2D0sT6a6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2q9nX3U93XZojknOmrcQLQsYlWAaLCdNY-SsiAIZk4yV7hLfDQS6oL-C62DNBkIiyrPRorXWAInoYmh8bTcKnqcsHMV_jB06Qwo6p2aTCtC2K9aiGjv4MKTEsZ-MEYP0FhaMTOylZ4xkGhdR4EqBc40clsb1pbKNOWdE4ki9le8bGJYwpWRNMpI18YDXQzszV_1QpFTUPlNbe8XjwVnKAcnSfHdierleJwNttDdsU3veBPJCxf3nTNq5zZpjB0pDd00R01einIom91V902eGMt9CuAvQvMmYln_aztUtgDdeYkKhljYNWFra5yQvKw0n7rdZvueH3aG2NL1E9NfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZWynYM3_kN0EPC2YIMl2Y1rXieet_MDwjthC-STjIshls0JXrLis6_HoNkdYUDmzgj4B5rsVXd-nqIaIAPZ2PJUaeva84D9kQ-X-K640IZf1U5VxnxnKpiBPe-heLWE02_Yqztje4kmP5gPefoeoGQ9lsOHO7o3TsPKiT6HbzqhV54KlYUoeUJPIZ41o2TqsdCSwuQDyDMMlhHuM5QZaATVXW3-ay8AsGVj19XME3azvhWa-cqT66qHhK-Mpz1OtZvpkpBaGs9QgVsLC786NP9gwSlJrnXrtWTE-vcsSJQImhxY97bM_s2rjrpfJ9ACvV4M_eKcDhAnogqe_tKATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pgc2R-HQ6KbFlPkc6ieeMnRYcJazpCIGX6uZ9RQ0WG18_-StNAOmVcgtmRv_lhdk3wrW-8ysPRC7sxCA77uTLa3OqC-KNKY1UfolO_E1yYIWYLP6ScokdzQcKOVWXdUYFn6j69eoKYcVSfJwHiyPBqqs0vKH6wShakxmQuF2Ct3EmX9jxeVH3oYWq88TtxO6WW8oAWpXwReQYSsTdKSu-54WEQ6fJr1tTOskB3mEp4jn1YO0ph_Bxja1Qw3TcgK42Vwf8grc37150RZSV9UWn8K6lmYX5mIN7Uo24vQ0ijizwjaodpH9agBlZFUJXCbjOn0i4ZPl6SG_w_51jwy7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRtiguJUlrKpBpAqKjrq_OLtsMi_mOI2RFA4hhogLpXlXx7RwcX4XdCANxQGuffybRiBVK3lN_NFPtKy4yC2KY3_dJ05CEIi0Yzp2GN0KnaoC2zU5cY-PWhE0Y43JE4WWeXEbDRTfFOB4SCWBSPO6ZqDfLVTjLrnheKrzOnlbezQzeeXMSDJfv7i17I6U0VNx5H49SKDK8YrD-GWekMl0Uxv79hyt-ZtBqFgh479q8jyktZ4Mn3XvD6Yw4kFZehNK3gpPrwR5VPkdcIsPjIuZ8bLO4izKO6Ke1INvnH5EfXoZ0QDJZpQfLeARMHnbEIvPFtLvqPwf6blY07lmKcyAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SixusVS7s7BdIHGxM1W1-N_pjOQZPhMxfsVPxBD4yCjwupj-HONQfxL3uIn6QliHrVTWUXPKVfm9DtG9xnnqzTuB0ii2rBS3uuj7MNAQyHuljsCwAxY4_8szEYYbSjV9HgQo0uZpGkoKdbfrDbH1Itr26OlazfeFAN7T4YtQbRBcpFLexVr81W53rr6cWyBnWA9DSDHv_DcLhMmJ9YdhkZnFJnhw1lpaCe3NvxXdJcHLhVKLLECP8HBjhUcF7OLXQIIeKj_3yTBkYvXo5TWO0u_8uS0HYMKjKjdCDhyeYu8Oi-nOWkr-HGomkUiZn9_VnzllQ_kzZNENs5-3_Z_UHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=YIi9wqFKlMYuQW2YW5SICA32nSpJCpvzUzuqzcnhDBBwpu6XAQi-62zivRB8j2ofvDWOAHazGuNgBkAG2uamRJnskjd5i5uSyOFuxNBoFaJ4_oHW3kyglEelBiZ9xLHy8m1x7XIymUGgAt4Io6z7_mVBKX3SLFZwFEcvbYSi5eS4M0z_4ORnkLXPx-96veHX0zEgdz5RGjQPIvdCEU1jVqqwkWVx-3MH6OFr7A73eBojhrVgqO7dPdJYUhlPUYqMAmStQ-NEQTY2cYDxThtfn3YwVLz-uF5nFAa0yd6miZ60t_rYN8AYXoy77EzSsbcKwDljhl7wa9pmJl9efiJzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=YIi9wqFKlMYuQW2YW5SICA32nSpJCpvzUzuqzcnhDBBwpu6XAQi-62zivRB8j2ofvDWOAHazGuNgBkAG2uamRJnskjd5i5uSyOFuxNBoFaJ4_oHW3kyglEelBiZ9xLHy8m1x7XIymUGgAt4Io6z7_mVBKX3SLFZwFEcvbYSi5eS4M0z_4ORnkLXPx-96veHX0zEgdz5RGjQPIvdCEU1jVqqwkWVx-3MH6OFr7A73eBojhrVgqO7dPdJYUhlPUYqMAmStQ-NEQTY2cYDxThtfn3YwVLz-uF5nFAa0yd6miZ60t_rYN8AYXoy77EzSsbcKwDljhl7wa9pmJl9efiJzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGlLFCawA1m8n3MqtDFpFje4J8YKaDBjLnYiTslf-vKt7n6BZo7-F74AVfeSJN7NI9zHdkthifkdzjQvx0N1GJRICD5xY5EM64owLVHe9ng7Wr6GRMzhsnnzkeCOeuGS-6VDqLmtr9Q4CS-Q3y0QuZKIGpYEg3y5lNx3CR43M2uIVk2-9pO2y4GMN8AiYq4Ndzca7YvfjKAGX0ZprfBVFWLWe4DjVew2U5tTyAHRRB4ePYg34WJ7EuUI7wztw1pWxHVxT98jcWlibv9wOaQgFwUVRNt5tbegr-ON6saJ-NmEJheU3b3aYYI-BPAEu8iKGd7xiE2GzllGXg5kuh8t7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdSouJ-RJtCNdvy3ZyfXEF9ltWrmj6sFOfGJAMACf2jdFDDTDk4dmcykiOBsNkh99KbEjpeXeQlMZyY3LYqHqip77KgGu-E6-P1j7mIpDR62qQ_2mXIM7JyYWNnrwn5-_lq6M8bphaG3g2J5fUsu7G7NtQfaLj17Lxopz7COnXx44-GiVKKdqd4MWMfD8FqZywrWgTq-QMBNNCEruaC_vgw-y2tHkCqG5egPVkSJfTVkOkdj0ZGzKs-aQjGQh0qwqoFytoPq9C0osFVmKFqQhBdmUEBmUS6JjI-fe-hidkwPrD0sFCjSWJTHoT4Bzlih0H9ExZ2qdHr-2pSVcyQ-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3jZdU2c74rI5GO1uDRjl_dZ0hI93mrpRZI9iOtV_lmPszVwqMGJ8DNmMfwM5SEW9Xs8OTsppFgDCVC4awGS0HgtAAQuAdipEPssicjFkQtVgRN8z4RSSJEsEGorJTGnZDWrdULJdfemHtMFb7wXJPJECEJYC6REnjzpzVqdjLz6ojTXzA5mvHvDWBEduKekMBeT4Xx1XTNyJ5w_pRrzNOZ5SDDkTFuZJnNXdcn23SJUZiTkTtv2xK5jFfvgk6OmwFkEH58T6Kek_GJsmOSfE6qh9knlDXdRzWSFUOtS8JdkTriwN5zihnWKAn1Mt6tGnAxU-zaSlH2YBImYDgzV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jf_z6NqUjouDF1wPIIUWy9DYklVVA60bHrEdE21Rg69D0C3BUpzLs5ccyMRDCuHzB_5L1w9p2CJPGyBUWXCUggIiIPkLZSnZnK2vF_V4-EKGGeR7eH2m4W8aCothom2Jud32snVltklOMmULwn0PUif8SC3omhoRFrgGOjMyhRHQ_dXZSQJrbbmjC4_WSOCzRQyn95PCJrYNTQUOgoHkBTvl0gkT3c58uQcYpANmg8AxfJ0uLVgAt6Y34EQ4UL9x3sFkl5fITS_4oFsYyAhprmupJoBjnYppUDXdyuQDkJgDaSCSiEOOrDtp3__TKGMQuMXyTKpO_UMXBmUPDR5eKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9aNvoOGA5aqLosJVrrPrOwMs13V8zl_mlZ_JoRF6IxvENfSYb4ygpMlNmKRqZGI-2squIUFraGZvxQTG6XjPYFyb-oxch7kNBaFwBc6QcV5ZYp2CPsy5_yCTRVUrm3iMrmqBZlwSMSiNp2FsDImn0SCxyd5m25zS9NYIdURZF3CkxvA6r4QXo2s8LGRAXqKyASLRt2b_JGw7grLgaNPzjt6ReeDbWnGvLRB1nCFOxU2imM6NfrNwheFd9CsGWGCOJiiACZrs83IxTNxAXSm2b-gQCb1PJFoUWnUsTLXHk9-_MbFO90dwckQTqkCifdiwP1W_epTtc1D-fvqvszDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBX_NR6fDazI8C3PfxtS1FeM8622O7NVEFj6cOYqTqu64WlrfxzuioYjFHFFbvOJmgcnM4HTAHdyQuV7Lq9FWZb3KajfGuvlVpyuRzbgUXXYq0zXMXEDGUzPeCnKjlfpziL-xUPvEXPLnA_TogDNr2iNO5CEbd8lgWSEi__THgKsDh5TwxGYhxew_jQxg5WE9emR11yqK16fl1IoCPtoJhypTYjgPfgKu99_KcnLW2o6nWD6Hhb-bLj2pBA8cXwZHUbRRMGwTiK3B8XjLR0lsBMRlZ9X1bZcH-0F97CxCDy6ujgV0OXxbPFoJxHC2Oh9qGUH4XkVZe8yysqDtP1x7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itvFFR5jZsPOhGDYu0tlqcpJ-VEIApurRs5TAaQVlCJbZN-z2dSQ3o93rIP8yoN_2QW1jN-VbInmw5MMg3viskAHG8ioCOXpErP0aAwpfdqA2hH0xt9tdVYSytUee4HkLdkOSl2Tq3XWofqz2aWeilmr_SN7oGC6vWMkVZ-0lwyEkaMybLYHm-82BwxClhXTOiT39dbP6xyTiRTh34oeJmQ6zabBBon399fJSl2J_k9NvRALu8CcJn9VaeQMpJaGpvVYSAFJWXPE2xvupB94b3EgCVkEmkz268OfT8sw2v0b3pvWTsiDOeWgDdeGX4SulF2FBIg1jXlM-zADJk83Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9Dkccqw6yQxm5Wmv4Fbcy3fSxi7LnkujpqYRuM6rn-jEOy4lCnGixpzV0Rp9N31OoyZzUbQ9m3XszsXVjB2ghHWypk7f7f7nL60PZx3sGSMaBz_jn7WTompJwZMbhfmrYm8eTGFnZTZNjA_IpdBuhAV9qofKYI1rjXpvhbML01XkUzGJ-A59yyy9vXub07zx3SHlEJPdeErUwHciOUhYFJOLmfbSO0Oj4WwhUOFptO2qJrbxLa4unZMw_U_oN274Gh3XjsFCJYoWaBDsq23KxMedSoAukRBGjstSzLYGo_7Qr9ffx5mBP-l_GnuwPcQ1B7TJvlu0H9Y5Aw2zfIbjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCr8jN2qREeSrXMcmJrhBAtpz65T6_htuPI45c2_brVeyTEDuCi4kEjDVufMzk1OA2bLlDJxE7ypAd1hs_6IcPQD3vofFl0nr93hYxfCw2NXAZb87XebAuxP8Ye05V0coIpCi1PsC4Y9IZPoLYRfAB57JOf66ahOHA8Ap080qXq7nVuhof_RYXWGG4gdMne7yWG5EoJ3H--Xvt9ylouLVnJaWX6Yh580KGbwNlhfTJcSZl50plgc311-QXpHfYylndJJb9L2I_Cc6RE8R8TClo1VbcfKaYRewSpNgbWg_AkxS0ohfssY-3zYgv41tgH7gzNhsZUDXkD-y1aP5n0xqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUzGtPqDWbkonVM-bST5Buw2si-Z72ScHQUmRlQeQ8ul57WU7lvl26D6TF1cJ3aFafZGOi_QGdayJXQcGx4sn5BbK0KcduJTGVKzAfXxrY6CrrU8NlF5KKEuLO8InsnYwOdMgivAjfAe5HffNfxcjkEZESzW08q6GhXGo6PrQ-1RQqsCO6F7LdT50zsng3HV1gRKoxXHNKsxlO5fDKchZJWVg115Ayy4Z1r2baMBW3tAAEm2gRuTpED2hTX2DVeeT8obvj3NntZrV6zXlDY4qsIkwNc1BbrFsFaJHQ4_vuK3fBQBRyeSHTwU07mWSJ9dvZdtQUO50_auxXa4ppZo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf1nxqQm2YlBKHPU8d8skMuw-r_O4jnAd6eotfQc1kFpPCGD85JZzCOVB9cSMBwVO_SHvZva4vQ4OQK6sZJv8z2RI3SUjFnpSrJpZbkI-2so4QscTkRE6FWLkLpr-MbSj52hXvmpMBCDorcdcG3OMCkNhy1YrVzIA3zkR7fUPrXgmKSfcfITls6_QROqZnDTVZ3L5k2yEeSxyeAaFNtRiFIQiydx3jqICfa2OMJlzp4-gp8x_HKclu0aR9tJUm5ABwlELBWrrd2c7kSEPReEUDYAoRl4xKKEyp9lIhaVqDivcsXZMZlRMWLgHWMCQUhCqBLZkl7qp6QmjKBqJvLAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il03b_MiBrxc2f3xkF0yiCMXU3zPMixCsh-5W9htllJXLt609LlWVX5fE7Zv2JyFWSQMJeIXQXzmaRwnRqYhpMawOtCj-JYCIpi35OlM6iXd_mkwZdJY1Ko1Nbk_07DYNmOkPvpW201PGG4dJqXTeEord3MzrqYHwhA6T16pIJ0_yjoo9LPbKqLJ6FlrhfgsD730ojNq3Gs6LlMC3uyDrA-fYNROOmMUmKcu8mNKUpuPVEuHqGWJQK0S5x5pV0qRT92gVnw-Iv10mq8-DNQm1KrQDt0Sh4WuTJq8kzYB72Tzb59JeHzMIHu4A7pVvvf1tsk2gZJgXBD3knyauhYV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzDPF7ZGVe6JBHryENsTq7M3uSdvYS3zmB-9zczMDLQOMnVavL2v7KH9Y-HgfzjEJZbtUeMkfq3Nv3XiGsgorNnel8zAm9Dzg-pIWqGtZM-onHsKghWzSzMgKl1yQqMsSj2IGEcER9vGpF8pfjo9AKE6xYNSmIsGcOy334VW68_uOmXYwTjT4Z8JsjhnMrdRP4M0J_ssLBdQCu3wEYRMyq_KXOszluNE4NqHuiQR_Sr4am6RfPkda5ziDVt3SZpRJ7BEkbvx0zZ1YhDhIFYFy9B_VKzuw8jKKfzWqZSl87ItiOhtfkc87gIZS7BU9XNFOtk-4OaxIKaBLSaTuCmM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJFQReb8yn2GqXyP5yGYME3tCS95Sf14FqlKq6RVBj8hce4U_IduO1xAuGCx4qfBxeDMPOHr-LMqDAQNkYvF5rRrgxZfHtRNAN6MVNgxRjmfIEciRHO7tMX2Ug9RRniCo1djc1cgD3We9_q1FCXmr0EbKAQnBciLdUg1k4Z7IMItS4Rsaq-zZ1uOoquOIA05XC5_WXNMvLqyCybwOo4ND5Pv6rqee33utWh2MlZf8kkvnPJHZMgz-9WdshLwlHTmeAzyomLcM4BzaBVj2WZJ2P5EYnJvDJsLP8L5xXO99LayF8FmKYEpa6HozWuJP4iBkrIbTL8nMLANJGz7-2QEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWFlJqtrQ0UttmNwhTqAMiot7ZOJLOVjVwnYk4UJWEE-_XWr_wIJ-ZNwsKW-A6nFwV94X9Fl9DRw-EsLqmpbsGdcMhH5S2BK81-NLUBwWGspdFfgqOJIrrUUQKF4B4aKC9hbU0eVop928_geUVyVJfqqItZDLnNmIWUGyS03nox7rgaQYKTzbr_jEMqmWPVz-w54N3GpvQRT9Ap4O-T6lzzqca3WMB2HC53L8XJT3tNW4FVMUJknyOHRMrBO_QRVU3u33sv2W4rmshGIZ5mw3KeGed0ZWvF4TR1ub77cnKXNLHoQVzzW_zVkN0ssUwL1XFyaf6Hd7kxYDM_T-eqnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DniVKxbZOrqD17Ef_LxLqFPq_7oMVr2USPm3TiVg1AWUaL3NreLB5WUpedbBf0UzbcJGMPWSjsrv-iuo1twwK0axyFdYbM-a_A0PwIByFSOye0fBU6srS8BHGWFdGYqfSkJc5H_sH2mRkeo4R1GiIn9P47PXvmwE7IIz4pVMmVYjiDPB7XHDNCtFtkdnNfzYEdNMwsIbWcrWyum5dTZTiX3coq5zRy5wzIWXv--2ucqCh5QNqnU17dvbrXVH4ML_unkLk6WF1sL62bXNrd305TRbXX1li0b85Bn3dWRVDu_MXgoTeuqLJUjdcO7uFhT7zQu1hr-WMMdiU_ZMPK9Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kngPT3PajpGDse-CvTR6GvzrLDfLi79FKqv4DH-7XobSN-H09wydlCJosra6rM9qOc6TerBiIyVF6XQbq5vDDoU3sIpnqRSaCiF1S8wg9_pUKries6iRdL30E6cJza-fSXpfPdVocjVfWYPmuKhFLAa8KUxP2Ke6uVFAWO_bo4acEafZYyKnibE12tqddTdxhXXGO7Ql3qTFLeF0M7VwCBQZHoFQBxclezOY4GNsEOkpEJcDHhLu8e99mT30p7tdns0AFgMafxnfotBhT_cZ4IqTFbWPiRD_nZ6yvxOcH1wDJr9Ms7PPz-ogF4WU6UR0rrobtjhA_1nrhCwjRlNRSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc-N0SwI2zYLzURjHC0jKMzUVOCJulwpEP67aHlVwXdDYhR6bH6ppFOio5qGiDfnBHytAFD1bHlIfTjC8-Ax_4j8SbV4kRF_60D9lCwYJ4iir8rsWhsloygQUiKGNEsC72oSGb4sOF4vqHT66ZAzSAVw8kUy9Er62oVyTeIS8t-zyn0ErR41uObSNOEGLwJGj2qeACVIHvJdUGlTfxaPQvWFjo8Xk9QiNSb4G5Y4pXAwV8SS6Iz52iqWtsPgEkH6tzIrqCsoj6DOHwhIIBklKZa22ZPIIse_0_q89pbGZfV5ksyA5IXQ4apH_5MVNyItPeZAkU8mFnvsOuKKQKDMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 580 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYyJf6FA_nG5a0FVCczyt60pd2ykcwcSyrgRN-F0FygZ-0Q6cFWox2KxCIST2lJz2wR4YQQkh6d59YQ4RamF9vsWfg3gO8C6kvfWfc4UM3zabvVV6t-t7E6WkOst7UefalabeUDHc5tUGq0wcJlgn25ClHEvtd7ct3KqSy-enOUINzycGgu2duo6pRHtpF1quDNfSJYGxXQ7GEejhqa_SRImdX7rROfESbZkuHLlgC8vOHKwYwZwmoW1FSL5Az0JqHQzOU_mMMzMX-rJakkDKV2xLd4xp_UcpW81Jy4pz2aSoRh2aQ-LfWbS_u9AJzw84EBICEwl7ftL2HXeEPygFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbLOUKaBTeBDwAY211ZUNnMe8W9qVdvuKfJV4bgxY3RQgfT6ijtISspJUTghRrwph1pp8ST-Gq59Cn8kXKGJeASF5iw8vTonvg5VdQWDgHXFL2lXI68wudqhjCTmYQ1zjn3xKAH6vN_j2WQl9sfE2y1_31CD2VdEarw9ACJ98KRkuban-TH5ZCSuFV6GQVfw9xNEXAz-6RpRMbwItGOUtLNCgA70fUS3jwfp0KDjCibRaUSpta812fVKZXhD-YQxX1L-LKuSwFeW_cfBpxlhTznH4jHmrIkxzEJsM4hwSJSaJaNCHfp-fm3LqGX34AVVFrqY2i3WSeqKtxDSWwfOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pASLj6S7yJV_ryrej9xkvzmT04rTDghODGOGmFiqM9EubXQbdOK7JHYvHGoMoyN3NO5gH-c24_jwZf_VrVi-gwaZa0pivxpEn-GeVbWKly2dnGsxbG8Z7xyC-GWIeDud9bekrbk7QacLZgTtN-ow_59oUkggDN74Oi-pymKDBsFcBfQO_OKF-6knCh5CcsqyX75xCiAAJN7KbIaJ2f2XgCk1E7KPL7_VquFW25QtczfjMTbMuw3rH2NV0TlY56_NRZ8c6iqMGVHabvkITGr1SmRAXmRc5skEw658SFq706ePFl81F7Y_SFHfos3jIY9u9cRD2h2NbTTqm-RfYJyBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi_rw6fX3FLOlEkMZuIGOwO1SZNTIV5fXlxlhy7KBfris1I6DKmbPeDeG26OJAQaj8jolNaoySAaItgdZ1xT-Ax7FvlPxdAnbVTwWQzm9x9h7cBp1iXigYpNDfs-FN-9Js19z2hYIiEKLHSltgnOkh_6NOoJfIZOnHM6n9qadf4rTV1y1OwVKqOPDFFuUlDWTeTj2kF0ohxfBXnEsGGzFSaGJfAqdZZ6Zq2ZSYG_1B5uyx_7ucZnAoZxoiyahRtNthlOlt1GzGZBAaVvYqxWGNlhZ_SYW2Rxcj07MCurQ75CeZrPWGyScG4O61RBURbAaoPHsQq48DkDbGchP2K70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2R-p3eT1DhJVya5Og08PY-s2EVpsstPEMd96eWJTTVKQ9jOOiD01W4uFXXVC7YHmAHxpfi_xut-arGJP5CQuqlvxYw2799SYWrDDruxmwuJCxFJQPxMN_stzgrPYCuGnIZhEafaP6Ecpo-y-8GaAoqPUAKDARFRHHUQta2_hnLssWuEyonr0YUuAJ_a6P6xHydXN5HrGxBH_PmY4OhWIkbOINZopjlkK4udCoXIogaWq99fZdVI-8L1wGgj-_DxqBiyoSAJ1fdcXrihg5h4gpI4zIMTmuzpCeaaC9nYwKy_btYYUUbaXmm6lzp-JS4WJP1D9qnFyrVXTkmGMjI3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udy1hOREeIvMQmgoeTnqUX3o_9Bxvi76SvSwjk6US1ndUwjUoWxSkSDdob2UgN-l6puMtXigVdrxww2Hmcx77Tthx016-q1mjoi8CXLU2FrExKElXft7vOmCHHEfZglE9n6pz_NJ-qFFohfhg3ExSV9G5P3qqwOfm1pUw0WKPmlskAWnOhB3cLg6ZchcGTNlYIE0rkq3r_y5YXLn5EkIxbpFnOBXSwfkUEdZrbOToAVaL7af_R91TxEU1iHZ_kEe2o1-Brv9Xw7lCDF0FSRhYE4pOeYtX8gR5vNtCvjO4siolCVT9nqj7VFo0GbL8qUCmPu5hZkFWgaBnL9M7KTdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idPaM_rbk2BX9yc5rZ1Ecvzt55e7Ex-tjLHgGwwV1kS3dkHvB5tQcgvnDuPWZdFatjYNMFd5FkeA8-0X4xIzPvYvzgCNO6U_iGX1LlLG9vRWDc-Vtj5n92HfNm3r5Tfl_K9FGwWiUmsN28j5_iFg3m0-ePZCJ1zOR8GGW-mB77OOsuqW_Iw2nwTIP-MJHdQ7WAn6W2LTcwpeWsa3cnquhNFjvGCFpeM6dxofwwt_4uhgu_67nwhSuObMbMs-8qhvWB1ov4qKffQGEavIbS_SH12WSiA5t8OauioSC07Hut9t10A8oqCY5yczynIGdWG2QOS2eMEaf7X3S7TubWyCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQ9j2Woaim9WTvzr3SnBB3rLRAgy_yTIZOhsgKEOOvJxEqE8Xu56mFTWuLGZmGS6_tkVdToAxYEjevt41ld8C3uA4OXvgp8Ie6b-mCTjKsdDQ_Ly2FGrrC_JwshTQkSwB1lBlSS3m6GoAbGICO63H_Qg1u35slj_-6O324WTQEll52mwxow90QPB7mmSg-Z4cSq2SAtk7gsGcQ2yCuQBB4kVJhv0PZ9Yr9g5Ln4eLb9wdwloXgYE75trgr-smcwaPeM4HylVAgu2fzQRVCVa0KZtvzEJVGoh9RUOzprk5iPCPs0TcYVZ9Qlw-zZdCA4NfN25EnuxGZtlbSGYl-MmNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dcz_92FEblGzo0xAGxGdRO7rjxO1P7VPrbGv8FQv3nId88sVVK4TUoZz-5R0Yc_OIiXI6RD1GNnWDaIDRLaHfV9zSbuFIT4YLExh3d3LxWbZ_JyH7VBBymqLuOjgicmEfYEiZVj3KHoTz1Fwra_UnXUguyXOr9Eu3bFvCPy0xDVWHadzKiwyXIg7I1olXZN3kHWVcilmIuh7uVsMqDcb3EC_EEZwzmhox-X6RR-9XQExE8z-kPKBWCgkReuwoqX77-m-pOGvdZJHkg0Qh4vAIBluMyUL9_rA5r8upmfZyvLj_PiR73yJeYCxRZeU_9toIa0V2yOtOXd2QrAlF9Knvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9cBI1daufmzXJ6aKe2ilYsP_XnUh5EPEHTD8XD632iBo30LRCHdbGgjSJapqNObXQVsSEyA0wcfZc2eRAOrFLCMzpvl-qVksamryFNkI80tSTFTXBVCb_IJie7rOvR-VwaY9-mNPY4Au1lWShzGhN8l2zPAWy571Lfml6Zn2lABlwR42FLzd8vUvL8ZEJeP5G0TfZjcaUNV3nozygsznZZ9NGCqRies4BNAEC-fMpL54Zj4auj65Isyk-ptz2lPj9byuOHo5lviaHaItke21YxXVFrz9tGuCRLv9J6qwbkwwxGQfDFl_5gl9PkJbJ4fiTck3i8zw2YOWtkGSYCGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONVyqF3tMIieIbpSXQsVuj9Qlk21xvYdER5rVeyBML9GDcAQ-ATZsldDcGP-03t37IbgWPiV6ThYEKRKdCZcbK4TP_g6XYtP52rawK3PUu6yo9y20Hlw1nQHZOkUUMMA47BNqMjXEvHsWnABZqoIEwEYNxlYclyZlo_CWWJJO0I8pbLI5CbFKq2_TBdni9qbVjBBY_iDa_uafkLFoT5eWw4jUVEFCXMwTluKzuZMtQixrVqxsCZ41CIIj7gagZ-dW_J6VhInvRsg7vdE8v3IwigazWqzuw448PWsc7IFq3VQFOmlaOu5mVytT8SCYevdjBNoWnHxuygZ6o1XAXCVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGCL3SYDzRbY8X3Qzzf-boL2kidKMgv0dcmrds9z23TdRZ9c6zYuloc4mq5lZWnvXmYTckqIPYS1bqub-685HMjaexJrQvaC8Id0jjovheXTTNChKIGvw2TA4x1SLnM5RAf3GOcg8i2PjlfRabeEU_BsFFSBDq_q0LRo2J9G8tUKzMLB3Wt7yfyb1TvlbECXldtGoa4sRAJ_4yU2YaPtYM3dkR5NXoSlEMAa2PUVp6YKEQoGx4TBpNU5FhHui7KBD3lj007bs7tbo9wolJRqu6QlGhTHmqLkebFpqiMTuvzmHEyatRujapVoCqa6z7jZHzSAVhFajp3864aXLN0l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb0agU4qielzlemEYYbPks5bXaXSpYpi3S0sEQdwoZOEpKGqf0qbsvI3xkAM9jE9TDDFSd81JckZB2cXT8pP_ZXGzQ6SsJV8KcrTBhJoqbKDtz4JWs8rA-UnzHDUZu4yjnuHTeK4be46DAHFBuPCldM0yXqkMzCI00pBZaKgRd4hMIUHfbt8MjsZvx4MZRmOaEj7oj_bp6WuZDkLP_knZkCmmQTyqH8xXOuMNs3yh51j7xGD9NE3gZRH0v0eF1OLPTeNqyi-_1W2CJgkMn7bBj7niTjEX0DjOH6zdWZPqY-m6JANvOY0pKone74SYzMm8U6bLMi05GwECJAuiZPxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLgSCXWZ5efTIp7frXhInJTi6C5cwK3R0SVI7BagLXwHGYlQc4x9r-7N7xTybcsQ6kAH1SUuzbxMOPngHGqc74b2nCzMdkQTed6PPevcYTjqeTvbx1jl6xzFBHP0PdNgc-xr3xERurbu_9TjkmyluvztLR_sXLaFJkHzD3XspGfgr4CzZ4GND329hX_JA5VKN8byJ1-CZszmHBG0m4ZRjYvTqgRM5NRn50_t7O7LbwZ3pSumbdYEK2NN_oYq26d4QcA9aj0cj8cyXt94jJT793XyASjHUrf7abIgrMDvs_XhzKbGcsC0MrcoaJXQWWKhtmhEkFmuIFJvnIhue3STxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqUzdbg9_U0u8Q3Pt6JFWG15s83K8H1FqGy1eX3gLQn43ivj3BPX5jyHDaFdEWNJgxC81yZrvhxBlMRq1MWgIGC--38UKcOY42CKreudS0bCDsuv5IKbxQwjha4wfVKqRXu0mXNhn9e9Y8G3E7sj55kbUrotd9hY-7EIBwDiuYXzrYFyDfyDZ5JcSbvq1Ej-HeCBqGMU1Z-_BuEVZBcFFDOw8edfwD5IhOYH8_LrVF6cgxPLF8lqVyqBiimi54QNQeM9751zoIxQWwbfVcx_WwaGkuEzC6w59tvzPMl9pwIXDlWdISyEYok0ht5K8Tbm__5qkgtjM9ERucP0cEp2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhdlpsG4J1Jjg48ialPdKlGL72u5vLgR6SHdhMtmHWRGEF0iG0tjhk05vwmw7s4wC_nDFettlvq6sti5oAC_SapJ9Sn4e-qk40fjGyAmIs3F2P_jcl_T27GPifuC55oFVz4L2PNtqKoFZZ1VcO9KlslUefBdt_xV7pQbDOEbv4tf7TpbBxKHaxDPiErHQqOvZK4fmcNDDkFJKjVDlQllop9KPq3SabC6R6OKlovQ63e4fxI_K3cFz2-bAc6myhM3TwxHV48_AerfMIAFmWdhvfmWp7cjG-ugv12LyOvQxKWUmWIENfQC6Urg1uO1Qv4zsWOanCfNZwB3LOOO7Z0SFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkCvCZodMAw3WcR_5mL0OSOQv66Fgq_nLsihcJ3AgReXieSY_yQxw9PXsEjPPdkmJbrXEXrkaiYBA3HPtjjzUGYoUKefX2DHizQ_ldCT-_y-mHoLqEapmvGNU8lyyIYaKcRBX5HCyu1t8vpjZCUYM5fX6RLT20rV6wjz3RXDZDuRLRh0vI94BbODsPKCZ58fOXf8Pn-ueON4pZOuLfIRKPytLnKYtMBTVcUrbg9z9wc8ZEty1MsuLUyKD2xTtiuuZUlkSUn-Yi53ZWe8ZK1h5Kr0wXLo2oyAIQd0rAQyKcYk5FCoZLWUfsVrpQj4RJqp7i5E8L6zUzTW1mq4izRrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zc96_7Nn6xdhAmofgbV_BHgMKcFFbKTYvDc51HlXfXsAc3UTMGVvqPTe1lq9iaEi4PUKPcDDPKXIFb9Aj7duo2lpBMi2zfsDUi8Sz3jqu95BceFclBgNQW_VyCfqAaysjSkYNNOArGW32-X2CRDTED-UqBsM4JmFPDAUGhNCAZiq5QmPWCIGKx9Iz2erC9AlB67_aU0jq_rxcJjAjIG4zZlgQiYTPUWVA_ZzCAiarAtJC1XM8zrhj_DES6MHtqvEsYZ2e5IazbL7edXnlSFud0alpuEQvwx1iprTlpVwdynEdP_QyzxGopVoH1hTGUrHXMjQo0IcMrpVJNMF0pmqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqA1J7Ulg3DosGKOBMoBX2ZpqngbfRQAp8JjKkKyvvKvXXVyOFq7sLuFOUYbc6ryHK1BQHfzkdVtJ8JN2cSXBeyHw3KW661MISdLj1pAdLgQnXc9ShPZ51TW5HwCjyV_g0KfG7XgskmuyyCcqfevYdADihQtHKeBxyZqlAJTb6Q7D_5OywoO6StpxF-l-t8Rnusza9mlmpf3noQ1MjHQ7zt8mjLMLKdpoB3hYlU3iCjgLc8iL6GzPeYW1h2Hwok-ColEB9wUgfrhiFVTrBEV6_5onnLZOorBbLbYdX_eEJGKiMKOupZq5meOp08yE5KpvHBHLyDFOHI9YSo-XT3F5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxbOw5HtDL8J_XJZWZOH1UHZ6BIlvN9Ahmkwt9uDY4gOKG5RJgyODtNM2WUIVS38FXfhlG-GFOS6kIfImvv7eNaFJwv09qCUG6W0ZvD7yzAE0ZdNtjVc46gmx-kN1zYMIrONq4tDVvMK8zTuIJ6NE-gh9sJ11Ro1TaxNXf_mqhhjq5skNVWv0IJKOxfEjXeh0uQvwZz02Di8cPCW-F493x66LhHLO09Ib1Kc-llpDLtQToBOwvt5socRcu8Ve4svSEgQynRez4e8REhfcxm-oSUVC1J8jsC0Qljq0I3OngzfXe5-mC7nb-r7lJ3NCczclb6WTwpr_NdOD64QDeeqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CteY_J7wL1CDISrYfZRZdx7ARIWUba2-DA8ce_39bv8p11pUFOfeeLfCGvAT7ZwzhOiC4tlF7wiA99gW2yLalXk1vInGylGI_B5miYfnTPqNjt9Prv2fcOaKyJ1QFpPrXlocJq3TZt6oPN2LsAO-QVR1wyrXCbgYo_bgXhZDsJfBrLrdlxLx652NRNebCKZCjbskvY2Gfq2F2WHHnQ_d_3ZblJyQ8Wxa9ENCf8JDqKU5ix-VWopLeeVqL2xCpYxp0ncEAYu0VLzTQyHSJe62QIYR7wMX3GcMnu6izLT8bpEyPLrZ-rAaIbpFCgee0Uhlfz2PviWTE8FU57V77HihAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClKF-S9ZVQCRvji_73ue_wtmZFQDiei_CCMsGCjM32whhe-jjps71mp6csjZHZ3p5s_ERsdu7sPMreVznOW9Gw75suypPS8NzTup8UfgiXs9GD19b5hFrbgZNtbmeQJiwISG4yKwMQ4iGtER-baxBRnKytbT_BAg9zfzjhGwnOnuiZ8FMTAzn3TeP7mZtwwPIx96u-JKGstI8YIShapCQv5tPEifEoRKcAYpGd7B0VTZ73p1cZUT2IdQUYOAg9Swzp1QvOR5dbNfchJQ_RGfmWaeXyUWQGT5ParcPCPRY7a9bDSr4VB6LydWl0tACoR23oyvKrwg5bp6ol-0WOoTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxTL6RUvrpV_bcPMKsaPnVJ7KQTACAb7eGsHd0rnzsHnivrqFlTpzFPZbu7uTMxcd2uezwORA_LRP_TZ0Bt8tIWtWOMXDfVfBqJxnKwly_bPTHj-ncGR7p340uxXB94ShSKUXZCfQyjB3wIJn4r2eMXyK1sHQtta3av80CQgq2zbXMXuKXyOYRdlycelGu8kgny0a8Uu3vwQ7x-gzkWDuwVei_02TCuVSKFuYc1OsyRSYN1sTNpQaFepAgWmK-n8Myn9etIRF9WaRtp_FzM8IlVh_e_QNDc-Nb0W3M-v1rRp_eAxsuvbfdIp8P7R5BdVThQaP3hMMAHrH_ms0_zaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFMTT-DwgZChqej1XaO6hzpza8GlK4tohfSeBB6ICh2kkKh1w3wULgqXQtlQdkzfg6uG3a7gCEd3mKggwThuJGxsPyPBn91QdTC6az5le9Tp1uBhFiNL4ljdXBf2hMJ7WHt4lqyAmKGjG51D1Rq25JErUQnfUWyb8Ddb5q5dEEtmx6NrvlaPVF_S1IQu01pYSggJiOW3YeSJpHErqyIpCy5POK0KafYbz4qVnopngIa-ooLpP6O_zcptxxtbsE4KYb5Lm98W9sMmtlRRryfrhL2hyy1qJ8cGIorZHXQGq66symw3u7epAAie-wMCJ9IENQ5snRDqHmX--VWZ_3s49g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjFlsaQ99AxW7loddXCC1idoDfecqSKQyjqzvYR3damYNk-6z2qiGjeyKXDhGiSWmKd7uYDVE7MxSd5IUU8D8GxYBBbOnPdN7jGpWwh4vMg69U9LIJUm_ThKnVR98jTGzho24WU4YYaguYredb4w66HGPmTU76whuL_uGIu9d-k4L6c1lhvshKff7nfe3Usjs2feiMNiYvFaER1cle2eVvcW_nEab8WrKKbSbko6nu8pltDtPtAOc_1qPDPp88rBAXMi7Vm7LcjBh2aGa1jJnZFtK63RZffbAo1s864zVZMOVo0WM6nJjz_qxioK5o-_nsaPMxMEYN4IaTDpSwKmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQspDStaSKhoQhRN5VGa6eAswvkTNsk5iQutl17aO96sutjoqYTVxVqx2Bo34tO-vmxlRtFXHPINIte8obvR7EvAmyFCCB2BvQgxv3Eoqg7nN6FOHngSA4q_tviYapLzxLZwUDXv82oAmkMSiC83rR3xJCYODcrGnQGuFSGKrsZr3ACSbxB2TLMSyAhagqJ2xxR6euIsDxWfGXaFkErfeeMFd6NeWUQf78UwpQeAJHycxpsW7Yk2d9Moxlly5ictzbERnxh2JydXMcXr2aQ6O4cRTsberFPcI_xdeK0l8jkQWhcBklQ1rBUjHw0aCtgYmZoj3RyfeD8XOApMIYYgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGDjRS3kVhwqqbZv6Dg-AtA2FwrurSk8qpA1Uqfaj2lxPb0us3-jgifpf_7OIVn3zL9QlPKPtHzKlXyoobvtuibP74kd0gkhU00T1UoaUB2ibZ7hAcWbyiqI8YrCJN23Ml9mCJpfnunp0Vw_idLWDwhWDLK6ICG346i2Jfu6qLb_a7jAuQpwVk2ss36ZMwHPJIIUB0YIayMXUtWzah46arxXSUtR57JlekNQaTp_JbXRKwzd2FWkKIfFUCcnBBx1BUfm_xgLibwbqVSvsFBoLwCVt0xWj3UVsBxcGsoCN53Umt9qjk8hGa2TwdW6bNVVez92ihDpEisDsDOvn1lgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLv3_NbrKIiBv_qTniR6RrmIgG-VrW8kMq_7QlRBLcoQEWlrsOHxNsWgVygY4SB-ypItUF4S42AxmpmrdEe3OEZlRheceS3oDP5gMHAqP1am5WNb7evagiRRajOAkQ3AxJc4UjAOZzgKRKkFayLx8yvQGeZMWCdQLGwEM1wiYJ8eWyWpXVbIpNquXO0Us2xZ1cOvQRrIGHwvEmD6C62s3_b6JUTiRf6DWDGPXZDJ3wjEh5FPL_sC3CI4AiUy4ifF0eISzFWzxLKPfd_jxy7c4wv9rzTUbzhIey7UjFfcpJN7aGQ5VW7DZdNnu0PjLTEG_567ekI4Ix0juJ79_ChIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=VNCh8saOtErFUHkh6zHxhin-iA9BV3Emb2qy1V-RhdOx73fveHpyQ0hi2aLcm-b_V6BxkUqvAdQix2Os80vRy8E2Y2hokOrYcJo3D7qiemVw9DNInbjHBN2FMfoKezs3iWnTJETbPxN3PSvSCNF25p6ht1Kdq_qoCHC7etJW1GyE6dNr3oxaYigTEQV-4gXoOMhR2oYQxQn3uCANt7Lp-RsZxxa6zja7LH9zXkJNOkswbxqGTxR6Sxue3iTYdAbnWzfAzC95lUYfhkxYBQKpy9QBmV-fFXw8bNX1Sc9GhJhqyd598yEBCCkMAoyrkJyzgqZJ4fdZ5m1-H9Rw5puiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=VNCh8saOtErFUHkh6zHxhin-iA9BV3Emb2qy1V-RhdOx73fveHpyQ0hi2aLcm-b_V6BxkUqvAdQix2Os80vRy8E2Y2hokOrYcJo3D7qiemVw9DNInbjHBN2FMfoKezs3iWnTJETbPxN3PSvSCNF25p6ht1Kdq_qoCHC7etJW1GyE6dNr3oxaYigTEQV-4gXoOMhR2oYQxQn3uCANt7Lp-RsZxxa6zja7LH9zXkJNOkswbxqGTxR6Sxue3iTYdAbnWzfAzC95lUYfhkxYBQKpy9QBmV-fFXw8bNX1Sc9GhJhqyd598yEBCCkMAoyrkJyzgqZJ4fdZ5m1-H9Rw5puiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLXi4NwCezRoIfdVMk_Fm9-YHyQJHFFX-2JUx6mexuXsO4jGQWwx-SP2tUTNUsjM9x_urh8qBSXVAk1b5x8fG7bikX0yUP4lP1fSXbhxeqFB4FZXzpzT8NPx4RMeh8qdeBNCDtqitpplXz2IM0dE4Kgiyh4PhfSCOalltj39r7cgKOdYaiVU8SUIXaDOW3gVcGz3SrGvTFj9oJ9OFuORPz01WYDSgnCjDcJRiSW7_HKTzFWXLeBnK0ujlsBvaC63C7pKXzVRblCfDS2Kwc7ZMPtarvBgayubYP6d0Q8SVLjlS9NKA8crOSWi9kxDTYmPVth6_SiZCP6wn1UCTtB9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQp87KOuycTQF_XSyWYMGLEExgNjYixn5_zFPge31tVu5YUtU7RaJ0boaCC1p5eqdj0kFGCruU12pq3agEDOXOuOK8NhfX0_H2eQ7c5hq5w9QWu-vXeYtbP1qczig6lSFaMzWZ6AFnNHM_nsdxtbDap0RZiPLeNHkdjglRNRFjPDLMJykUZx06pEWY7dw38dDVIMRl1_E-XxqMPW382Bz9OV784sT6sDMsWskPq1IHVCmiWvwIwAyqiCk7vV9KSYk-Gjb_wFyA77BuX7iEKawPf4zyyb-YSSwr67h0FwXjSGXFBkMA7m3luTaE9FWF63Payi0umTj1QGt2qszOLC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlQ5q5uWhNB2tw9dr1Cjht2otRkSaS8He5L5OyLOBOYKyzPrfvX-mNTorGUg_0RlHCq5stinomwAi3F60ncD9NhbplkMyxx7VmITtbUdfujg8CN2VReXc3in-p1SiolFL6ujIg7PJyzezxmxb55FMYTmmMz9Hm0uxkLzxUgIweIg4G8kUs8SZlrGbvW8V-MA9z4AXh_vhzuzvpBC9SwjsRtruN6F7MWhxJa0ucVWWvJIns8-quFfkW-4H-HByNJXiffqxUFOG3NoeBLjM2Jl791b2nxxIk4B5lpTsg-TFFfIsLRub9ROoVaG33-d87MoeNzeXNQcjQdWf-P9L2bYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVr9211jrhzMPNSAM2VDRPrszBY3VN-UybyxB5zcoKahNruv-brZQY6eNen3HIhUF6ytxr5rD0FuAsErVtKMsVfC89slKWvFiwoIg8x3CJvtv_dVA2ADrQ6798gfRTBZXnE5ZyVuFq9Wu2EFvtzDVyBGdOkgCf08hvqK-U6r6QFS9sgoTS2g3sQepz7foRqGbC0pyIBXbj12gvstxr8phO7DlOPP_IOBL2rhxTStnCEuQnNAmAgyuCmymmZhLVM9VVObnOPRZ5KOLEGVW02Dc6F0d6BCLFO05z9upbj13OxIw1jRyVbz8Lqq3GQlRCjAAGCZOdMyl9FYMHsH3KFOTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inxYcvqSFq0WOH7O7YKTzUIuooXbp4iGug9ApqkcKnQIFG28K0mCGlptQNUZgWeexmBy54DUi4K0mipH0wEY1mpzPjK5DmA2bO2zsOwrSJz2aawfUEAWUNA4OOpv-9DWnnECRt_sqlVEAJ0Bjdujs2M7vUAOde1X0nb1H2iV8oHffRI7x39BfIjBWpeZQtRg0FjClom1R-rVLf4F_BEvPTM-hffu_A1mD5HYCFIGNIlEKV6WmbBYsODPvg66GvOivVLKgfTyxWblDBSRGAYNCseimeeNJ9-es41Qur8NPRUwZNX6kFSQcQaRwOrGjH08mvWvrWGmNZ_EKSg5Cg_Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTmoedksoKNcPwsZ-O5E-3DDo4BctBIarODfbYXq7Nho4VZIxY6XmLFRgOO_oLSLx9oKkFgKLmrbzUX9ICJmJE6-BVR2Z2mvo9bF2cKclVddBHMU9vIACPtBE2V0JAlfmYrk7XVL_wwtvUErbeAo7wOg4ztjlw1xgJf_3ky7XHAU5i5ZR1D46j7Xc7F4MLGxu2Gv_hLKSoszFGb37t-UsDSC0-yWBPAz_BtWm_9ug93ljpUo88eo3PrKzpyZqPlbzufJCHxmwV6pGNNqMSmbvBstZgjFreDCZR9l-H2mieXZZRSkvshhA5ovVq0ey-WFYS2v-XyBJmZ2ifSmyvRhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeZ3EAsASqRXoHVOBJ6wBCQ2T1AJczUc9cEWPmAvalcp7PxGRUdc-D8F43hHU8VQ67OqotjdefNKLqKpkM72Isi_QqYCBalV0NACqF2y1JfISBJDBWXSpuLV8d--Vp9CUMLJ9knWwua9-dEUKYip3gABtLO6180sD-U3U3sZnLEBJpv4L6BudUO8Mc-TvGNjgY5BgWBXl7UAfIXiv_O8hCaTEMu5zHtjfjaMCuju4lsU5mBSSOMxkoscbqks8O3MQAf-3WnspA1wEBQbt_L6gZn-HeT2VxEP6ud3Ez_G-TjBO6TyX0mmurchRN5Ds1vrgLOiJ9MV4abTbDGIsamN-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rpEPGO-GV4V3U8ml6PsyNfaoMSAyijlhUZZ8v-HKGlNB2WDWasl2btLKv1zmFcVGhwMS6xDPc4KWj0FeKAK6B8-qBfWEuhKpXsY402PTn57iVQBHfsC3GMvqXXEnMHbxqB1EIa0vRPClxdS3tnQ9gryApVxp7YH1NqzsoVr5h65e7Ai4onBnrLDGAb9XDCqgCJqVX7xRCtEqEjoT7lKeh44hx-V_HJry84dU8yDYYtb6B3mz--sJbXk3ybsCZ-TtOfjAKyzUDTZ9hJniV8VjBbtYfMr7uDbYZQmSWZq-Jamx5oZE8QnOCGxiF4-dDb0fzXX5qN4q2lULn7YkLhbfJqdjJQP2JMzZ8GJnOwT7YGDZALvUrFUcXVKsMp4MHlxuAXyphCEztTmnZCeKGfqPXkljh7Aw97AJ2205VjCTIR4y4PNNeXioMiO210MBaZtx0MTpbLcB6ybOmnZgyt5z_Ekl_082EWRCUOiU_oD15ZxCtyDa2M6IV5Scg6eXY6_v0V3HsV70DDM9d9V4RXoa0qv-RexbyePMNU22DPyMpS-lwuRjxdsEjHcZERBo4XsxP9Z8qSyQmPcR98LUCfToGqKrE9GcooefRoRnvSVnPI2ifZBstJWBcv4o7gSa8MfkFY0dYYxSS0ktEM4LJs-d_keVsPuDIYbI0z-I49L6G2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rpEPGO-GV4V3U8ml6PsyNfaoMSAyijlhUZZ8v-HKGlNB2WDWasl2btLKv1zmFcVGhwMS6xDPc4KWj0FeKAK6B8-qBfWEuhKpXsY402PTn57iVQBHfsC3GMvqXXEnMHbxqB1EIa0vRPClxdS3tnQ9gryApVxp7YH1NqzsoVr5h65e7Ai4onBnrLDGAb9XDCqgCJqVX7xRCtEqEjoT7lKeh44hx-V_HJry84dU8yDYYtb6B3mz--sJbXk3ybsCZ-TtOfjAKyzUDTZ9hJniV8VjBbtYfMr7uDbYZQmSWZq-Jamx5oZE8QnOCGxiF4-dDb0fzXX5qN4q2lULn7YkLhbfJqdjJQP2JMzZ8GJnOwT7YGDZALvUrFUcXVKsMp4MHlxuAXyphCEztTmnZCeKGfqPXkljh7Aw97AJ2205VjCTIR4y4PNNeXioMiO210MBaZtx0MTpbLcB6ybOmnZgyt5z_Ekl_082EWRCUOiU_oD15ZxCtyDa2M6IV5Scg6eXY6_v0V3HsV70DDM9d9V4RXoa0qv-RexbyePMNU22DPyMpS-lwuRjxdsEjHcZERBo4XsxP9Z8qSyQmPcR98LUCfToGqKrE9GcooefRoRnvSVnPI2ifZBstJWBcv4o7gSa8MfkFY0dYYxSS0ktEM4LJs-d_keVsPuDIYbI0z-I49L6G2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMuuS99yzakJrFshcvQwVMOPZCKSeja1_f2ZjmNhnk81GLFcbTrc5dQDXQVRvAvdimWhnDt5Tf6QthXQep5tvry8yWodDADfcYDlnJmeNl4GsDQgkXieB-Fyrux7HLklRI5IeTnxxXuSia_s7rf7gcxHTyaVuR7Acqfd90xOpb1VVMqUMPuIfHZoZh2oH82HsliviAtkxrlTQWeKmyV7VWEFI4EptCe_jckAjr1BgeQOf8GnskQeCLXc3TpjRQufMIIhwUPoKVFTZkoN2YOoDOPkRDcA_s3KpLgGgXFIhNzncEiuCAr9x1Z9jH0yFUAZmdbpGrQgeb1BG5cpQzjsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r44rTpUGbOS03VUcLEvA2yyqhMUOwInmm-ohB2SJSGtL8aO1jDietrnMcHMP8iO57_FmCjEmOOOGdPCEObslEKG2-o9IDa8wXr4Pu8hWqr7b0O2Ufe9mKb0n7Di_ijGEk_zIc0y4Wbj6sDmLfeWSmi7-nh5fmfuoHPSAvjg78Fnk8zn49mgn_rdSRimn9d1KGOxwuFK61BD6MLeI_jxsUBJNWYANHfW9FYsZQH8Yj-UYJ26XmjfQ9gKPQMWC8i6uPX0LpQ_rO9PJdjDHImpgHDFFeJY3DprhjErfo4GR-ftjiGlQEr4NknXAWMqo6Ymr6ZlIh8TeoxFlT4Lh_v-Kqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXtcs8S370ZWacnME845HwnqztbrZkBVCAQecYgW5d0vdSUSD1_mDXpbDt7-4zrHiJ3JUSNB7nruFmxqKiEpEqhGN_Kvp9lL8Efpqr6Ym3yMty0WEeubrXva66qq_lbe6JswTxQtCHyo2kunPHzR1Sqsb6H_6hfN5u925RDZEfBTlDwwxf0uUk9Q3kHphzljgsVTUdy26Z6_f5h64Zcp4IKCGlUjNPEf8mXwiWEoYPNsyh3aJh0oLj3vfjb_GqICXXDiDo-iwXx368xgdOekR1KN--rc8vV4-xqy-ZMvtnLsE2lXTwDJKka-J8Z_tgLKV7sZebplPyUNoX--BDZB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgZ8eTOFJskIVsktvGsr0i2xIo-bFBBoWI0jjJsoi6VE-v8HPP772h51_v6-zd8PVTJs_u8NRESau1WDfDJibdFL19hZ5SzsSmKoIAApORU2B_ASzE7e1k3P88KeOB6_ptonB7OP2twjaAmzSnPwDm0SM0G0TKmyz1_sYs_Ork35eWtbBIgRezZMXzHuvb4-aYndYba-fuW3RX5rlpq3KX6R6YvjBnplqYLfIldoC3qARXnR66S068-f5U2HfbHE0XGvKGZjlFKoMot1gxuBdk9QMzNgCr84EbuAAu1hY4ImsoO-rhCWUo-giOyvJeJdx-jzkyMHRbmts1VIovzUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrn7ewRFMVTxkGks01wgL-0UjRXqwOYJRaL2otonIqCN1a8DDxRbvYc6rnBvQdMzu1dq-W2FvLYfWtYHWrOAsnk1G9NpUSmoQcR-VibLZxIQqYjU3Vy-5gxIHz6KgRF-psC1nwBO1qXO7fZOg3T_6Z4ABsV1LKFYdmC6fBCIK2k0PdkLOli9AAus07VpK5QO2ipPul_N0pi0vuE4sJsW1hed-l_vHkHGSwQ6LJXIukhWnSHEKO6V8VhVfnI_J_OCVfpq2fFok8wW_DuI9v0fSIqJ97uJUkokPxUSF5sK-aE8qq5t6HXfxn71T5Mwf_hEHD27jZU-oHgxo77TmBPaGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Q9CAIOY-J2u6jpxYhtgDTWK7OpzjwuTGjfHYKXFNlp0igh3_gRqLKK9BKceXqa5OS2xsBT11NSwFNKbT4ZLudRLxBJ7oyEHCZ3tMiFUnDI7Qr3Alb6749nBADRh1En2IGveajG8iUS1AFLouA23msQ07dvg9Qv0vkNb8qgofUorIRkvESTTfMpOr_Tsov8gjJw3MH81Q_Iu8iErOf1vKM_YWbClrC3s_d-zg5HD_aQUFW7QnJNbt6EkII64O5HyXYdSN9cE5dbnUkOT7T6vjOoZE8pDT87B3qpBv9z95x44sDrfgLgKOvIox92mctrc15EOTGVreoErGegqSfPAhuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Q9CAIOY-J2u6jpxYhtgDTWK7OpzjwuTGjfHYKXFNlp0igh3_gRqLKK9BKceXqa5OS2xsBT11NSwFNKbT4ZLudRLxBJ7oyEHCZ3tMiFUnDI7Qr3Alb6749nBADRh1En2IGveajG8iUS1AFLouA23msQ07dvg9Qv0vkNb8qgofUorIRkvESTTfMpOr_Tsov8gjJw3MH81Q_Iu8iErOf1vKM_YWbClrC3s_d-zg5HD_aQUFW7QnJNbt6EkII64O5HyXYdSN9cE5dbnUkOT7T6vjOoZE8pDT87B3qpBv9z95x44sDrfgLgKOvIox92mctrc15EOTGVreoErGegqSfPAhuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWmkLA2qLjlP524VEHjiLRe7urK-91QfD3lxGUAK7EW6uTSC3x05b7NINcFMO87wqxC7dgGxcPvc2ipjNbFD9vt5elAp4WEOSK18o_lpbCUtMMysY_-D2bagsV-DUO1yemzVPNswOvo_U_MoQp0-Nkw-wijw2NcnT6WYY8tP9xnY58V-XKQeN4S6uWGuJqX8H2mHk8EAuL3D0xhPUdV7HS2Wag4arCELUwo5SgeSCE7kzyTeej9pqHCbAcYXVxFCdgdw9uwfFE9bCFmCAbfUKcWacENoG4PoxidYwRthIaDlcOFu3CTf6z1aSsRsopeLNz5OsnkCe3vkRbtuZRmBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5Dd7mu6EL_GwEd2TdRcu4-C2DwK_aozLJW_UkrjAKeVBTXmvXNNf3CiK1N1_VWSpjmF4vJJRAtUdyStiYBzZriGuvAvqeLzUlANjEHHolnjdoxeeuhZWte6Piwy1QCS4cXfb-h0LJzX7bDJvvetoo7hSGIc7Uz9wcfBQPHTrHZFTQNgP89Y9Zw3ioRTgn8CVCkp1zInKjnTrPrn_To4smM43qC5Beg3ugD-Ny50B4Re7dWss60dwfY9C3YccshvJSYxJSNWEn4uxWAZTTwMNGjKeVKiIwahtz207nVdgLAYXuVaUMSsULAyhzqsQrn-IZfabcWn2DkipSvMwtw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
