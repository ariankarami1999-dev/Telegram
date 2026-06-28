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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 19:15:55</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxFfW0kQudAIZzdRxQD0fukaaZN-ceG94X0UWpOuz1xKx4LX0k6EQ86spDBaPYiSf2NMBoVFoAY30lN6u34k8OoueHYF8f-O271iCEj8EtPWyEPAiqD1JuPxXWpKJzpXpSwjUd97g-Dw0sMEX-QAmuQF3qgwiwTzsAX8d8LxtU8G7wCmoCBDrGY5kGyTinbej2J9Pp1r7l5K5Db_T2ZbN9hl61LpRq3VhDEyA0Infcz-hHcya8jHe-vFoL9gWJ7pwhFnLVBV8rAW1kWKa4w3eXQL8nYTcJjRJ6_Ehf-8bHutFWH88S4ZXL2A7wHjw5kW2-Sm_3pwa4KyTdY_ELFKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 268 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddo8y-F2NGk_2UZ_7zZyHf2z7OS5d9ubcYsUQUEX70Sr0s562rm9XgmqI9v_yoaepbJpkRr6xfr61sGTKEi4oXWA-vu6YK5diHHyCyhuBFZVo44vUDbiB-Pc8TTN9AOznma-5U2E--PVJWHJ1jUEudfl6HAZul9kVMyaQzVpa3mtZk1g_EM5jjXyGYFYkSj3vXwwZf4AGLgxp7W9h-KzozQMoNpQewpHivWuKTyW2fGgMQ1YzG8YOCb5OsWE50iBxNjtwIzA1L3SAtpPq1Zey1jjqF9XM5R2cWssoLVQzYx39NFURVJC_ppevbURkY7EmymFQMXZ98og_z1zn6ZinA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3f1pMqjxjDaXL0L8mVJUfG0EaR9byvslHbTz56GNtrTEAve9VbT5f-syCJ-dhBkX0VNmMPTO4VKqRBaN2sj7eC8Usuy22yqJYq5EjkxEeBsAOMEkVOhprJel-3uELlJ1DUJerUZfyHCowKp9zubVlQJeEKNbjMsEW9Oz6WaG9pw0OwhXmQ3-fhXaSBn4rjv3L5XPlmXkuGG0kvgEdViqNljiWZ7nlHWTtZfGOA8_qWBQnDg6bjxwcTLZSNx8tAZmKQZZRfnPFHTCjBNkv768blhKvZaUCIHte4l69zlZoCqutZbEl1ZVO3FPqLIn4rD0RDef0z0RcVLoWDQCikhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4dr7KEqngiBZL5vpZSoq-UoL9d5606gzFAh26ZG5PiKbTY_YTe8kskC8rMefyC0TwF12IBgLvRKbD_Btc1tBMGEv6GqSTYyCTOtuMqgDB47UaWaK_m2ix81DJQ4wcs4vkYGtzCTJ0apWHzMzpHVDNqeyiL-F3zBF-7ReeivDvNTmv5o09v5mxOzICVN645Th2hLh91knCPP1XxuvNiGWvKnAXC5XsEvA9wWof23AYQgGgExBCULFOJd8xVxZXOIQOg4P27SU6IAHhcmCEY3nSXxYebq_XPBBOeJKtisEyDP-ZwsCJSvQYfal9ebkgfbe00SXN-5MSFGEb4J_Gd2Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xoz9OOvZY3tEkUjSuNuP3hSWhMdPhQ9P7QPmpfzcs6yA_XwWz-Zd7CW_0eReXaWsUFR8aGo-4A87fxaC83Nk2L-yVttw7qLNTduif3wBUh2weHNGpNu4eiaXYOXvh_Mu55j3bXyD4Apza6atT26j3w8I923WXvNS1ldGbyFCimsOjHeFqGNkqe2fQLIqwrc9Heo3RhGBC9hhhDgdPpfLmJxh6Rx0bQ1c-gd3J8IidlxZhGdmN3SG0EBNo7P9rSdGQJYKJxVbyTxQMZ-qeqmfAXxAn6Ov999A7HknqvUkmUAtnCTPV6DFylpuFdpY1f-RLP7ChDuKozbLUQSRF0R67g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNjfOQROm6TY9ydLNJe87NHb15CNLWWsm1S1bz_H7NVGchRsUYgLjXpY_NNiECW4M3SAO7djIpPM8XyBM0oHipJAqcx3FgRJmElxxorpPoPH9NpfqihAr4bpWEbRXppaLOF_t5KE8MIxqNFB0BYozjsexW9bFdJrfBbjqPS7ER642-byoOliru-i4vj3O43KC0WHDPnJMx9r3AptxGf5KK_uVQ5RV9r1XvLNirf8XtKaYsfuxaRPzFDFXMRg2G9PuDno4zsJbBTFEgUmkhCBQupoWD9MdxskenArEYpPv7c_BgWhpsoMxi0sHv--w9nqL9jot_hdDLHP4H2YRWygtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JliWrWj8cfvkjD1GQyMP0uDB5Kaxj0LcXd0ALS_QiXZ7SQvP5-xlbo3A3roxG9N4Xm6EP2stev_AOEdenxKhQLquEkafxe58TKu8XB9IGy6cuBvj9ELjCls9siuKxeLBiORojTrhDUb6kmVGxBw89Xwim2jqSdrfwIXyntNZLZTkhBMWwM_jvzpfvxnzHkV6Ev7Zoq4DZx5J62LqAS_tIbK0SdheK3jFkb0oZ3OIrkn3Eeat0GRpaPoSioimB6PddYLrKvBaQwfhsJ_1mpH9g1_FESoSNADMPjHGfGjR8G_Wc3Jm_OdKaP1QUj-tHJz7wws1huhXx7d1GTx4P5Fq5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASlVMseVnQo-t3om5zgDhli_1lrAUVTvc_MdPHwC-K5IEjQDreXX6NW6B0V97aVv3RnxXaDeXvLP4b8HU2ePHsuK0R_sLhAh0IVO2Nulq4xaryrewm7gCS6ncPiQq08lLx5js9WwUPPWOlWBzAej0FjwOD2NBHMBg1uGn552E3h0pD7vOvXTOVADtfadKrkf6XQtyFfBTe0VuOvtWNquWhXwA5VkoBzGCFuMtghrrijaVBM7PBcNHyCA3xvt_xVqH9xGwOQxP6nFOOduXUpZu-jcLVJlwAZo8geKmCKDN6TgXBtirZKPJxjUKy4ir-6yFORVDa7UUKwtd0TM57IBKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmD_7DmMaV05sK3ca-aKFoh-Kzo_c2292jgH0hv6XhMCp6v22_-g3_BfXPTh6udFVqnTH321ZQ73d0VXoHQReRowGPYXjo7fSHqjMrITWseI8SW5dCMj-TUWUNVOh_eDLCzpUHXHSyggmxlUCIUqytqP3QkrYLFxkBgW6X9Kwsk6ErCU4SFOzHJZ7rCOcm4zelOU4Sx20scBpZzNf0NNBjWV5h4_YWgD4lsgrDcd58ufI8fmrLwxjBJvYk0GRZziMQre3mh0SX5WNgdzITtMUFbkjYpy0qPyzCYB4M20DMFG882mvZqIZdflG_QQEfgbd2Be_Q_GkoNBZ3AiWdO3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYRX7EBNpZ5s-_YgAuwAi3E2TSALQDsvleEM8JWYGURXUrQtkPaKbh2_WxGBF4wliO3GFi1XKUmMhxCPG82FOx4zoHUbwfR4jJK_n2U05FaP8MPL9wwYf2HA3HizmYI7ySaQy4FMK7qkTPLNQI7Zyqe0WkiAeppEYc5nYBkfa1WqaCwUIoluXcU-xNUfn1kWqHeCwVwcGuHzs8Z46OYIKDvJkI8SoQoRAeM5rMLQ1ea2fNmKJGZ7sMWcuZsoC8ofPd9Jn4aqlvodIPLSwOzh5BxKttyLZ2NNtaiO3bH44fWxwHwe9yZsU8vQ-mz5slVmvOOivkZlgwyRAlIb5ks74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LefM5sIrmuOJWKe2USnCRuMclowz1zvGXG7U0L8LyU5SF_enk9oqFWGVBlWhmjm75nyzDON8U-YL45rr7eg_jCXG5VPDI4sRRZQ9lCreS2pPQEYg2470qrqe0R1uu6URH2aqWbPR_AmxefHwQ40x7oF0cYuwFC3H2UtEefb0vc7gL1_p2sFjCrCdT948VjIpCyn-upKOtvMtS7lIgZXrwWd0adjN9hh5tz2jLdZftp6nnFN0GP90nCACgGJcrpglG1hbsXoMBvPZYS4E4WVqwn2U4o6UqmZnJfnCTN6ugMN78N0nDtBGbOfPVg96V0mYCHdk1_cevwr1mbDDE_Is2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUpz3z6_6oYcjkEOwO6hsJMD-c3nkaePN2tTTUiYChQZPAzl30LMMdnOeUGVBK0PT3KEN1q9Qb0AuLq5uabxV0xSkpz6O-YqiVvYvR51GIOu3pvZXX4O8Z2pZDL8yNokKC2ejnfo7ivoSXCvrMWFTgecjxan04qG9S2N__MVpgod6dIuwDR7GSlGMD3XdVkbWZQs6va6VORFyl675ffnzQAPH5pJpnGljtu-VRGVaGmWUGZMDGr-9sViK5hBbAgp0m9ND4uGPWvn8mxyxOe5bJfYnNaHsn9MUzGCylItIKiH56oXJI7WcNT61hFkR4Ie6Z1q2i0UUTNmP8D-gnsfWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwQ2Hj9tyI7HLuwE-waS0ovyUJaYkYT4kLcvRQ1dsTDmg5Isjmer4YQNsRvg1JSR7Y8ZHk9bI2WqAtf2QqKl7yXx394qQ-09CdjAKXznLt-TQ9FscwgzayLcxdZbHGDKzCo6mIRK2jZER3IfxBTl59wxtWwpU89cpazc0Ba_T23wehpaffBnB3GcwkjgXmDGk-N8tpePzfDDz2wsR9YDwhLpnuQBGkvW8W4xkupAc5LBrMHhm5LA1IkM18z_2TkQD6TaRD4ahujf6QPKhJC0ip5mcgzrN_0PZ1ArnhgkJZJSBEmTwDu3gfxK6jPCmXzaPEhWEPi5pAydNkdu6RVPog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=FQq0raem59fezVyXUs4bqRtNGs7gGWag58jkp8Wdt94gh6AUWqg3FEv0o8u_zbX8Ry2wbyWTxt69428jM87YfXso0LmpRbd3XYrwoWjCIPBjJiD9rBSSQzKDgT7qWaALHymHKqAP6WuF1hD5n9mbze0iCuUeQgO3tdUxjb0402CopT3cQBKMVD7R5ZLttQsZC7EckO3iYFt8NtfvbzrbFnJteg5SVHOJeJSOAldZhGaptq9BbGzL_UjJdFN_H3QyDsw-KXzd2IxdPQq6UeQGpoQMD7BqsNkyLzDDnIObEhTv81gRGta5nidpmKs8ATLP0FagPvKFr4hCFFl7ZX3vcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=FQq0raem59fezVyXUs4bqRtNGs7gGWag58jkp8Wdt94gh6AUWqg3FEv0o8u_zbX8Ry2wbyWTxt69428jM87YfXso0LmpRbd3XYrwoWjCIPBjJiD9rBSSQzKDgT7qWaALHymHKqAP6WuF1hD5n9mbze0iCuUeQgO3tdUxjb0402CopT3cQBKMVD7R5ZLttQsZC7EckO3iYFt8NtfvbzrbFnJteg5SVHOJeJSOAldZhGaptq9BbGzL_UjJdFN_H3QyDsw-KXzd2IxdPQq6UeQGpoQMD7BqsNkyLzDDnIObEhTv81gRGta5nidpmKs8ATLP0FagPvKFr4hCFFl7ZX3vcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbroobrJdPzj_OgEFrDbZZjBxO78fvb1Fgqbbp5oUdzZe5-TdpPtMRoHCd79a9rCXnG2RzMAWkBgHW2r_7Yl2s_7EtxNaNj-1nasVBh-ZESXRrq3e_yj_vp4apdBXgzvsEDTmHjCdEz1QEFo71vmasC5S0VMCf9PuxtIfCK75o5nzG7526Lj8JPWXOyPcnPhGStNbxn9v850ny5qomEDF79L--hWj35BfntLFysyfuXSP5nkQvsIwapHKyxjoOur7Xt8xBNytKFlBBWzrZMCRWJcZE8GqMk6UB7icGwBZmyKl6mec1390s5duvpK9rETF4f-CGPdbFqasCbx-aw2oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR2VctvAyU-Zmr3todEMOq_7EGE9X_wAE5oev9pd6LhfpeOxP_rmLqQ-K-v6JjqqImCh1mfPWEy1D0cEAW6rjKZEvO4Gs_ZD-stNrpTPpJZ-aKWW2hKt4luJVAg896Vbzelj71L3K1venXBbAcWyxKd_DJwYk6ug_1U7k0t3fM04bxze8cgsSD2NDoLQUbdO0EPW06AXyuMlwQICBdI8vOP-59op3iSwda8mgZGZFyqZR3CzMSVr8FqlSkLZLpfsJlAmgvSTxgu65RBXUuQo4c_umEl0V7Q-LsBPm7ymsKdN417LPf5hn-rHU-uvNBixbBp5QIJ6uTjMg0S6GqhfgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/du0rpcSH_N34XNDNPKic66kvjQ-X95F5u9JD14sbVk7TdtUcZB2NdDBiSYzyUiEOPQwPvqfCAmG79KSP8VK-zwj2OfOmZQI16cNRrGeecf3lFWuLa_q8vrRyJUd7AYSy13U7BardDOd3vWhiD6ycu0yAMD7UvcMHNMCx_3Hg_Dr6S-vJOAliNSy9kdaFDUiSVjdBcWqrVueiwod4DpR-kFDPGzWuUJ0f7FTqjnIA1xQqvHXJhSaSESK2o_Lw_8b33GxYqjeTrWSjWX1_6RKrwyhwkaYvY8pkA9VOtGP71GFxqJ7RfdHdAvgNsdV6Mv6X-_Ly-canYOE5BnJ5Gc5u6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgFchrdNm_v9dhhTffI_jLJsok_eFhqgDsix78UF113pojYSJC9dtBiKoqyg7xGyJKQJqExbo3tEWqFeuEw4fvovJ6x9ybNsOAL0-uUCxIES94W6y4GNW96TukLgSvMJujHUHK8TtClEHjBTWFAx2RRY3uNFbxBBbIuo78vQ2KnJktHVy5oU26-LO6X2Gf4BLjF7zZbtRMrJ1whZsrgquktCl9aJoAKv1Ex4cZZKA9tYWPdBSjWO7kh4aThB7AcnCN9pYnREodd4_FOKWoKQkcMs0DzpBrJ6E19gD923UdNsRA33ziWFkQ5ZgHSWBWciOhg6MQm4KxIUG8tZwuIWjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7OzA1XXUYzlAucwmAEsfYWcM4pMoxsPfFRZnAk5LR9Z-gsBfS3bu8CwFV3cG82hhf4BvHh4otnzOl_2_KdnOEaYp7i58fHxgb_aGWXwhI4o9Ozzu2ngjGGZmI7SWYERXuWKAa4k9gtiRoTB_e-7V5npruXXhm8KHMWKOSZ_mqjLey15bM_JqLHP6_Vj_I9n26yTe-164IJPs6hdl1-L-S9fM4LIEcWnuCwLvUONGBpNPTTjkWrhHnhClupX4-XwMCTzCC0LuFqVlKZajJVD8pJmbldtfTTBFYN-exaoEeM2rndi8Lk7HwvHDnqNisQSZx_PezFOAkMGbaPHPSXU6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJyP6RnNNEgcmEzJp6Kw2QlzvkkbAhcgGYwRVYroi1tM4WTrev8z6oOx4ty5u-WnFmoUa7VgoU9DF5f9Arq5WMBOShbnHXgaZ9eJG0WouNbWNiYUDtnLJAJsh2Q2Xui-CTSIQplBSXY7tX_VVlL3MqXnAWb2qu61yciC4_0lOhuGzu74BkjNk1VchJr_5eUcrl0lVpq-hAGFaoUcYuspGlNvEviXU1BunRGHC5SSJWRkFfdPkAUIHgo6Wx-_BqB4mjIIgwH4hpn9ZPWobLpFL-idhl8vFFKz-tICtjOW4bNcITbgZncgWAQ6orPFGfaGI68t9HkZ_d_0iCLdX3WeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJ_TeXe7sQVv6rtmaSmZ_1HrCAsGfMsUEoGBGB0TlLqztqpIdX7gZSaLLtSNcapHxuMGoo30cQQpXSlvu3EYGoQPQY38JjuNWCRPchSEt_Qdvl49EI_MC4FoP_y9veOS72_7ptBiUChuHRSPEINwNmiKa5FopPfUlK85YJJzOz3Ehsq19ZHBqkNaDVqGYKGK7OA8y0t9jLh144FI6cBz1Pk78H32rC9vsBvB_Ss2Fv7zfPDvhFuzngjg5TRD3BoTO8w2xYcxzx8uaNJp2TDMNOs5uOUjp0JsvM7bhi4sou_rnrzm-mK0O7yO8C_illGimCVGu-IM2fywVY5Z2AZDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbJ3ez71FH8WXMBYcnxtHpIEXtBaVqqAqbInxnnQGXJaMbkzxgChAkq7hQky92hI0T-UinVLSUX1k0pf0pIS2Akvz3bgUeOB5lRzccBGzYEJJF45-PVf8JNJwalrB1cUBf-diH1zOjpXKmZPgTmqi6m4XwECkI1DsDnPQ7CiAY9JCrrFOw1VY1vAqx3CaMsEBh0fTpL9U02ZL4uzwmXPpjkOsM5BQS-I7H9Wx79us_xDRsmPM13R0CIppz5S24IlSKL29ylHgefIZ-rR1IWR1KBXFEUnBCIF6zMM_ICFu0shKz143b8JFsc8vhaWQy0PTSrIzF2clFQgNFSFOHOhhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkkaImbIZFGy-5FO-5dYYDoJwNgbGj59ruS2mMvYFFkJ7mOLy7e8RsmgzDwmhEx2If-WkR3jsra2oIunRCwhBPfusojg-LuJ3QW25r86HRBXATzI6AoBLwpvr61wkYzgemntR1lZUJZVMXlzieNekH2uyrHtmjse013QSGWAOJ5emiC6eCGzmd-FRzDUa_tjQ2qJY_sygikiddjI9hkFwNSGk3279Tr9plBiftyfh2m2GRy05Wjn1i0jR5HvEcB6oSiFMIyC8IPfEIyK94pbnewr7dABSt-Gcmt_xQzKMYaYxSOZqUBdpU1e86LFXyCBoUTL99-Dh4KvOc3CFXk92g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-1pZaNpWZt6xNJRbW1ij3ofh59b_mYKCCDhAkgsMG2iDE-0_DKpPTgXw9s4sZ_LSbt75kJSnh2uv_2NK95YyFmXkx10yk7Rcuu0n5yU_owZJfKvI9zdCpbrv8Vyw1oZGITAKUwq0u_HUP8IlX2dwYMlxmjjj6SOyLc6rimoTeDbOuyPRXbxbrUoPAJ7LXA1DufAS2_SMpxmeNwHXuh8Qm_mcooQuS998mrmt5iT8N9iEj2AcqFUZFaJIaNPQ9RDkTqjvrOWA3aGVaSasgBpC48Y79xh-I-WJiP3J_-ypt_IZm0TY2kNDDKUScaZ25TbimBGPJPYNvOcflUdz3e_QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS9P6n5jtOuesLKQ-VaXmL73RjOYQlHC0lQrzKByu5FgQqFXxCkIckOmYEGH0-LKI-Y27RvDed7ihpEAn79IUW6ZVMjyQe4ZdwtBpoilZOlgB1aMdy6kOKsvHYjIS_D5H58wl3TD_gdJPW2S2-el5mPLfTLvau1e44WQ-lurvBB-N4fIj22hSa2Jet92WbT0METw_PFhpO00WIZngz3nz0gik-Gg3Qa648ABbyKJr6TkzKl3HrzsHbVlvbKz5gdO-16QIWXoOV1IapxX0gLVPDJuVX8WZ7vDb97dl1GuSKSZ6EAmd0KM3d0B8xbRQpLDKooesYUT1LaANSuvcBnP1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC8ichm11wcyRGiMXmT4aw00FuElGmJe9qot7hTSWXBvAVzJ7fLHz4ou4dZhPgIBt3rv4Tkr7FJvX8YFb2p0mC1H9QcWYeMtPvqibyySq8Xi2DYKaJQtbWEG7s7eZ148nX02wHr0lbe0up-EHfAyLAJ9qEx9NXlOflK57upPURw6s5iNhpRROC4Jcxd2e_NgNJwQIXtjWOQebGi4jnYOF5tiidjZVRXNsMBETFNjhxYbRX4eAFIFzbPqcmwjIAa448taK20VjRLXU8p2fHq3ywwT6xX-2FOLJH37M70SHH1fA8Ykgja5qHIUFKn9kx31E5GJrHlWxEkNqaAAsBq4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PN0QrM2fasSjWZCA06gElwAd9Gup6f9dr1vJ-oUIYiXLJxDFEh8rN1XU55lGA6qVVc6T-_wv-u21WKwHn510bPWEKkXgFk5KIG1l8Lca61ydyX30FvQ0ol-ShDv1NwJYvDZdl8MJ7pl8AZ92qNfQ4ljuspyxSkEI230k9c0zwv8spHdNASxfiaBM59VPP4adzPSTwoUKPTLyd8rVNP0a7wrgTcMmdpJ3IaDJElKJC5Gu41KIaoUWrq81tcIzcfe-wBJ3cyi3OHs1YIJqnr293NCVfQ89Ha2v-_JNkZJzv9N44LtfXpldHB5pmIj7MxjlYhU70J3737UTBtdtoJYxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWFlJqtrQ0UttmNwhTqAMiot7ZOJLOVjVwnYk4UJWEE-_XWr_wIJ-ZNwsKW-A6nFwV94X9Fl9DRw-EsLqmpbsGdcMhH5S2BK81-NLUBwWGspdFfgqOJIrrUUQKF4B4aKC9hbU0eVop928_geUVyVJfqqItZDLnNmIWUGyS03nox7rgaQYKTzbr_jEMqmWPVz-w54N3GpvQRT9Ap4O-T6lzzqca3WMB2HC53L8XJT3tNW4FVMUJknyOHRMrBO_QRVU3u33sv2W4rmshGIZ5mw3KeGed0ZWvF4TR1ub77cnKXNLHoQVzzW_zVkN0ssUwL1XFyaf6Hd7kxYDM_T-eqnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOEQ_YwsegbwdCJcRFXAjmMEm_De6wQhZqAp49cYmboHXgRGTH7JcvYd1Ib0FjSL0heLk7pKQjrMdcREpPLrFttEBWB9KUn_8az7TuLCR9GAN4XyqJyrCo2iE0bL-Y7gz8lAW42J4v7z1RSUp3jwqv9sI8m1ZApHxPxD3MpTRknjHTElcYPgpDM0SCc-ElzDQxZ5u7MLq_2Qe_rjU8AMQZ4fRIokD6mhtvqzapVe4YSO3ddz1w3eto5B521tjgc-dAuGG5Vf7ffkcMPm_591s_raNR-Ze8Wdq9r0HZDDuzvzl9JnV8GcH8boO7g5lPJltKqsVX66rwMGBd6sow0BFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUgJZ9SLoxWlSvamj5uYspkb7Vd1CzViQSTsfSyJKVazLJTSqAEvgXifkiScte1BgYlhrSvN4IYJuCyyhVeH6K3tYIFRzvzmpAB5azwZl-TmLuF7foEtG-m6hk2Xi7IHWEXez9ow4_0Iv52B0UwxZiRubjCubt8IezykGe7Iet2hOYg9msDFCQlZxd3PkpoJ-OB6B1iNWTd-0eD2pcFEmXDnjVNswcOutLXTfg1Ec-Sj9JxkicwDd9V1BBhVKjOx7kdvU6GF3CHTFD4j6RqURK09y9GT3LT4oCmsTpfruy1G8QujhroN3c7Z2OFbvxmk9s0FClFUlWApimvLih2e4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFVzNtTLGhfnaUntJYbjaCARAToOnJJBZwWwezxGBMUTdS25KoNTeYzPtvKFk2XAimQXs-MpwIrNgp6j-NLIUSn5F8uHeldliXp0k-L-wBIheSZYpBaeOIIE6S4h4W9mDjMj2gdv66KXfB7fRHJmZtFQbV0XFLxXPSo2T0fJOhdYOS2-IOVuIzcsdOxOSxqnWKL0DztHmqxbjUQmZMNtIDDJDWtvUddAZIiWbhA9SEUY-hNPe43OY9Fcz03WRnYbxew1vZi-UyHO9CUi_Elj9IetymzkjkMc0D8RQM4b8YrgEs2ZDG6MDmXPHrzyDk0i5l5Wf53nj2uGHtNPMv8VbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmIdNuh-icZecCrr67v6asUliSLTN3NQgkPdGGiKb7L9OW4fgETzd40r46EoIwZghJ5SXWTyZ99kye-3SJe9edlGHQvzloCIp5iuusxUqyOiGPqrjiYVYYCs3IbItDvbCn9SO5B3LPWt1UnqcyJNh2fKIAHsgchB_yqZOP_lGRZfzgykUxLPzaJP2nEyOUf4RThdv43vAgg0vD-x3yAX-nlPAi0y96lLod112g9RVV3iOJZnG7MZnu0mbYFi7VNfrGC1-osXLHqimiMRNzNwUIW4m9VaqFTRU3SDdbXEkLZ1z87HhcMcb4fnWnerT8Ne6CCvxUeygowFGw2j3Un7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTjJ1Z98Or62QtKBQCRjyRJLH0wClW-nchwX_HJXgnaDgA-DOgtIRvaQ3Dh-Wkk9lo6TGS3dQIYLDAAP9ulaAIf3Au0BTPMjobRbLIurbAahX1OZbpE5rrk2xwgmJIZiAovRV7OMJrbzQWZ3ofP6c_jUUNDReuVGHEXQJcc0q0RivQPf3uSo2fdnyIAcR8t4npF2oO4oO1lU-rxO06CRWgRteA6dSYLNp16q_U8uzbmIq0vYynqW22NqK_QtxCDyIoKUAWzqhKrCi2bfn7YOXKVX82YrAWCozh6w4B47qpsN6NyrwPgwi-Wr_IRcW10wJsWzgBi1osCrpS97YsUinw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua9RoST14XTvjAIzrRHysbpmyWzPIZh2Y-V_gUDpC9Bun65vV0cD3BshKvuX3JrzrRN4mNF-NYR1jgVoG2SRZ3QkHy2Tp5BbOkIHoBR-MrPIQQW5VtpV2Whr_oszyeCzCioSEEsJmjB5dMcPkocdkZBAFX86EO90a6Dpn0akCdWMRGBKHdmtP2GDIFaiJMx92o8AiX8I1ONGHragIW3_Q1arWfVtzqF0WJ3hRcuz7lBVcPCmNiFE_cKiCbrz67Ar-zUPBD9NjMCs7cq183-TeSLkDNQf2RnyepO-ii0wXBygTLs3WcJYDWkLOqOeEmHNqyfjsZdKR9ED9bziMNK5RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Dumh2RdVu9QbteiKVbDmZUY2c6Yt_nM7p8Ehq2iMnne5OACU7JVA0Z66U1Dr0dC-gkTCDnImO2efT6ObyA_goV8UtlNsvBkVU_zh2A0xg0678yU4Zrw1iyclMcEgvtymGSLuTwzblhHCwqMgctT5laSjdtmQG_wzKv1siyG9rYOVwHI2ywKLEI7fLO4Au1Fi81deZLR1sZQNm0fng6zEIp5MtgTYIa3RDF8svHJWY_MApBJ6f433OIallhbXWLbbQOoe9nw5qJU-l06FB40EWD4ucwcVjB5l6X4y2lzfEVzY2Ns7PY6PZSmC3POI8j7wtBB2D-cS1aILyd6-oqeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9Z5DC2KQSPj5Rprfqu2TeXdGUUdJaToNxFXg_nqpklV47nRaplUm0OjuvEHS7AYI4CbkXpYRxrN3zOmsZ7HffGbu_Yq0dQkctQlxSe6ds8bz54KmIQ25ntui0NY5uCImQzuD3ZEAHvmtVoj0IL5IZmDdJOGs6lCHvhMKFug_0wSOmrBjKbqR_jEacuijD-B8J-2IJ-9_qXSYUcyHQzcAYtwj71xk7n8HPK2iGmhtonr98_3uxCzrBT9ojv-Xp1RhqscBNdOt4798ZLbSvFYxZdPMn2_Tbu0OwXBxTB7Bjpjfb9bMnvhRJtzQKxZnlMWGaXUfW90LSZqHd_amYSwFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge4yYSeVKslEStMBDB5liwxtb2H7d3MHh7Dh8wsfxW04lJ1qJW0CngVaUGJ_j9akrpcFySjBZxgiyrmgx3mvu1fWA_i9z9q-IETjVQYDIE6We1rk_j89p2HfDJDzgv2GRv2lUAmHSlUbZv6JGXb3rmCBvCWe6-RdofHwjSTYbmrYyol6jaiHkzH0wQWiA0loJ0aTFCIYa-t0Fay1f_t9J7OFjole2uFUBTDeyuP1NCNoIPVyiwECF2HFBCq68MXdpkQE_SHPTLj-DLxJPJTq1dKCBLZ9L7TZJRPU1puxcfaGTdsisrlszWNNntyMjjBnW6wOiI23YuWprxf_Xr9_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jx8Mr_uAG0NXh2GpUDdo6SDUWi9e_OWItbhgxswV9ITN4V19m57pyUk5kI9dMa7c1K3eYf4RBUBWhem0YfGVg4LUHkSljDFbAO5W1EB36bcmPiQDDEVfbYrLA-YB8Dh5Lyr-op0gY1YdRpVvxHebySn7FwSHWtlzm9GNNfOgaqwW7SLC-YlgnJiZLsjkPATQXHwwzUFgvXb6xCZjIoBO0gx7682zZEFaa2o-23EXsDHF_ATK7oyLnCeUGlcoG-GymbL2VunBTA7F-YKW25QWd_Iof-PNoja3R4IfkWaRryikqfyhs-dBRS2CO8RRoCTpfG3s4Bf0NBm0EuYp2tbohQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR2x9PcgbeRqoVTNi4APkkd5HaZNxOCCI_TY20vVCWwUlYUxL8l7ohdR5609MqCypJyhU_7HWZHIG7v4UtA3i97xzec0Tt3KVBY13sNbbdLR1QiOgcyITY4yZDcsc_ulfsAtShaN14O5ne1ybX-rvIELgpNLQJVCk492KgQzfEwU0wAZPOeKSWS3_sotvAw91loYy2BlCI6K-ryMDGkkmGR5r9Q18FMT8jSpuZSlms6EVvnf2zlJarFvFyqTHRi7eDXSiXtmtQxIRl-vcx3P7eWpkSa4bzoPNlGS4p_nN8AiSQjF1ViIuG5rpxZoB-kh_oqJ79LOK5_z44hLT2YCfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_Xk2s9GRzjLggK50IWU3GBaaeISGfIPqc7b9VtLw7SCPOxYZri5CO9Q0ayLRz8Dx94Ret9y0tkSIdj7t1cwyH8Ak2a8iHiDoaRXxQdP7z4osYkcmcaAK6bNN-EFxcKx2npRFXOs_9dXNTxKyDNiXjC6mfyYCkhHddTkzYjIGO8OpdnZtKPIJylW8DfLhiSb3U31vibOoU9ZnSWdvJYLDmhMOCOb39CvM0JfVJNKIOHZbf10Gy3mKGDj9x-dJwGYPidA3tTvnUCrFbJ3Iv_vcS-DeUYxpWpJcDd52t6Rk8N4-9UCDLIIMxtNmoJSDtaYsz6KFKITYFcz_M7O5z6RiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqgwR8pU2x8YcNbBsJXpKAMSGwVV41-LlIuOMrJnli6EAUfnqwlMSNs8pRxnVLbNrTA-vetxXJeXw3MEG_uEFWHLNb-1Uw338Zs3TAO7EJJ5jVblhjRT7fZ4t_oHkpk7LV60x1Vi6OrlphVuwwSlzbZyI3xUu2vLhMm9gWSciLkysDx0kY1thr4MT7TPFWgmRwEu1mzTlhF6tUVMsK924wc4wWLwmHkXA5qC8h9O2ncwZiFjXX65KOrafFsHrvRvHc7PeuSyza1bOmlJ4xYrdvZWYBo5Saiq8QPD70Uv1eqwtoMC9G3P7wlcbUn9AVlnW25Ki9V-lQDNO1MGJrKSSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW7tM2q-opC-7ak2SGdJxoattXCUnSVxmowfPmQd6eychBZ0ttCL-VtnYAdnU8IHfJCtwvCvHHjpUBChbarA9zTUIyjBIEEsaHxrlsdWoVqkfYE5mgZQX75wU6AW4JPdyj65WRhECjUhH_dDUTYB1ROwc3Sg1E4gsAPg9dVjws1NydlFufL-BdLdbUAqv9GesYt3OJvi1QISjxpFNmH2jEMPsLGkJeSzT_5fOPlRTwYbt3mKi8u83lSqpvvAlx0Y-jqNrcDrnw5MV3KQmH2MAjT-8tGQACZIVNKJFaHZePRiCNOSNtAERWnmsUdY2mZs-sxCWVgMLkKiWiTCWKekfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Z2tMBZ9WvRvb6_sIkTLGJI3j985AcHC_IlzdQk11UnAQZDvUsuufBbNAFH9VfE9h0sWwQ0Pmpyfj5kQ5_T3Zp_4EmdwcPtdLkX_0B_fc3fm_tY-lpBQKE1kw2o1tEe2MoAjwqTZ9lCutkVsYagiSqXLb-FNfVEREMkvcLjUOZxtXcf2ar-sZbL0mKqMCdEOg0X8XiXOHXI_HFrxxjiRTefgk64ndpy3cAr9FH5qUyuI2vNO_enr_mup3W9qtgvzDRmRRZliNY9T1Tzu2EdXnkFfECumHEXeatjJON-JzetgXy_sCq-Pit-ZnmoKJD8xtMFK_CfJEN8jY_wmTqPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVUU1YQ3lZnagReOTkafv0SlI9sz_lGleyOdbTlIrP4Un7GoucfNRi8jE2NsqpAngrSNS9skkDnLY5rqNsYp-Xyb2kyyYoA1Sr3dFK1f_uoYfqflqevDw-3-SzYWXnBvxc1pFC4Nge2kM5wQToNYGQm77KilkwVo24IYA5Z8S_mwZd0_rWdDotH8dxBgAY3twMm-xmc55m820jcPC7C33f4kowp2KCf2OalgY2Oh1H0OVvg1RgNeUhHqgVh2OEMryvgWzmizHDTHl7z8bFB-kTDl0qJZxmeZ4dMRCoijRjmJA8xOJ5pNG3yLa2SkmTbwo1S3wOCFtwVhPtoYoQumIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDQRcR7-9Tan1WOqM1ZiahRusuwxJ4GypRUupS4rqCnjPVcL3fOXILTh2m3DoyPDzpwGg4rnjKHNkE8Y5LpgsvZ4J6gdFSOve1Cr-jIxyY-fGb2UoW6OS_WJSzhDO5GosiVxBSJqSHAICOhLKO6rtIUpygY1PR2OyZsa55y2ZHM9MShHjXV0EixPw9Dz-FksQ2IwHlnyFoQkRWTnFHsOIfqYlGntj7GOg2nISLyJWems7wo31g5XY_JFLn-SFTj6hCqrUqWGl_DwrBIhmvUPjMpomhDd0FKbiz-6KDxag_23egz8uLh7A8gP6jiilLXvw4C8eyLU5rH2rgDde5V5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVXHmgKogvrG3CDJsCag_v3Vq31WM8M-vXNoDqn32AU5ugVaOUqm65sr1JFAKQuI8GwKy2EXNO2hJiKLOi8ll-rY9nZ0tGLWhOh-r3Zzp7BCJmNMIcc466TRFLIayf24Es6z3njWw9rH3AxSN3cKpQnzrc3PHP8X7yU7aGQgwaH50pe6murR2dSNPSsunc094QSVPKWNeAbQv1Qir88oX-u3TAzC0LAkarco5Bs9ZEPwneuClbEH6lHfpZLg9g58Dj5J-HEJVADRwH6XtqupF203ZlsLYjh_jy8k5YLsgb9s2UVXarxh3Ijs8qdSV511actcViN6195s8WFuRONOfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcJVQKBkM_SPQfs-FvbRKkL53ikhv1mhf9fFiOG3PjIMEV6KdBYvvt5UStMOVusNniOnwW53XI0ts0qNr70-WcKWsY12hZRHq4KilnIpAK-Vl1es7SZv7l8By8r2DDlIJwaibImwCNpOWfbehVuwEx4MG6q95MyhUM2bVLoKDoIjUINeQlJE-sZFfAQOu85TFi1ajMV3IhZUVPhXjCaO6u1SlsZdmoiRs2918IrR1bchnDAcuSMKQNDoLy4jIBx8Wx5PcrprF191R37_OlWBjfV5pE6rlHmwvim9pMONOYRQLANXkmIeXpJvNJNR709iF38VS-I-ArKOT8SoUoeHTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMUtaYC3j3TQ9heFV03LW3iJhBIXQPOgaV80m9Zipd2Kpjo4iUkb2eXjba0gVxXoyRVI3NaXAfQT7LOepW-KtAcc12dzjirOo23dUSg6_tD8XFpjMaiN-gjw2QFcon7d_vjiB3ONVCA9n4rUmkmVnBx5wsNH7H7-AoZk3KJBfoSrP4Mk0AAWMlwj2J2NQIzjqdKrqKKm7jS0qkQqHxMkUBuGe3L2WdkIFpMEgHNKoEPnVA8mOktOTxFLbnLSBaVhN_HpQmE3I0r8refKmncNMlwroRnvIA5ago-ilkzlKy04COAJang2H2R6iR6NULi-uE9iPVzsTmixk1lsunOwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf7dO7p9la9MeHYTwmxnRWt8zL-hddN35ezAcnCkytyfZZ93kOnGwKd-4D0ltyKONgaTgJ_VyutOybzb_YDDiUwuA_TwBa5KqYPt5xTlxIJw7MWMBoiHtLbS1V2hOXEMbJayHW29pzEbGO8h8klVppueImsfOHyXUOCCIhAuZ6HrUQ20qb9DBbtZQ1iDI6K7GHCAdfcbjhfaEKHezfuO1bqK-mPjHWjBZk4usFLNwdv2Uaua3bucxgyKNekN57QWsTPRWp6t_RfwPcqnbUWt8S7DiFyptNCkPO8WORmESOZ8nuHEfUqZcD40z7EiLG6JDxQ6qp6QLxdDPXuxNMSsLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpQ7oM6cn0jbl1y8xdyarYZG_K38yYCfjpsYRWhmj_Mvfr5wkoR_KV-pcCt3b5KAkIkOCwItembhwaLZVR5wL0V3PvFvr-4eDs9uuHe9PWkHZ5-eteOZHnvldtb1IeLl0y8u2z03sl-zpdiFaaKYwKW51KRHnEgV4qrGXk3XBqw0wWlpMWbFsSqV7YGq8OvTPyQbi_HzBFLq2qXa7A8OjqJq808xxreIwbjXm9Qp3uBbP17o8cUdwgE29wXW8rFJFv-5csa_n4fikDpkvoPikEBEGmAHUh-3X1mMB5N-JS7-XiVDWkiSA0YAaQxdcXr5J_i9VCclcO8WbKRchl3StA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP4DdIZRECz1lQqvSzz6RaE7TbEzaTV8Xfy6k6TUz-u0IpfLT7aGkwXbAnr9LvYn551j7vWVk4GM2ZRbBQnAUuiWD-HLkDJAHunx_QoDQjfcNouD43Xt3Lr7I4c4j-LjSTvqu_ivsrbziDNI-WVRKD40zLv_A6pKRymI40RzJb-KOiwFDlKMxEbJ5A2xfQSzYfiXs75NN4V91Ciu-WMv3Wz-MrZY8E5qA21kNkTdtqc4PFboP7l7fV7LQLvbqI5K5fFCYONwTrqZdmvugTfiA3ABkaUlEglcS2FJVQuosLjor9EYuKpy-LIN3wOPXJUOHlSdQdH9wmP6cPdMxJxrcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfIex0lYNO3xMZ2eaFnn10XhAUUFIRMnj6lzWZTC9YJIZi5rh2HmqsuSGVLJ-dxMPrI_hUouCToHhnki2pIufGs6ZUexiGNwF1H-kVI7dBr3a8jJk6X_nE7e9xvhhOzdM776tWOuAz_y0mHl_HpCLdbZcMcXPXKZXDFoOgF1bWm2Z5gYMfU875Ud_c7dQ_CipjUs5fBZ77-IHzSJxZGqwhCL6Jjp_6X_h9QQtVQOr-gzUC3__-OoW7EBU7uLUW1tMVKT9y7sjelGBBoMRQ6X3etE5Y5J--8en6d5C-THwb02c7pRndF65TS6vUedYZUgExYv1D0afxIQM67ab55RSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mshXPZ11GA62VyQrgLnm22DR_7yfL_ZbuGGc9rNe5Vp4dYCh5xScv0BmtoMHHPSccHTbWggnRm-MIiJN1l1cSBTMjibXaTZuV2_3Wak2qQhAJsw2YD01Wox1YfIYg4LK6khmciGaOX2cTvf-A6Pd4IFJtRb-RYKWU-2JMYv5MyrkTkJmCGVhCwHVHQoC5OHUd7AU4G4uapF2rqxbpug7kJW9FHKuExBbD90KAvnUWxOlrRukUeb8ZIFyUpB_CGsZfe3TV9009H8erJY9RYxI3yDy84th4NRd5_q92nMy1g7kL_6kNLeUU3WeInC4fz2SB1F1X2YzvnlTIQQeENDE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyBi03yAPn6nGkdhyNDMR5zWLc3z7wGhLT2GcJ09I-pVH4xTFG_Kx2Jx0l8DyVbtcaxrF7Xb0SbBfH3d7cgFfcIuCbIlqWZpZZDCIkOFbhSajH5i2upQ6p1kvbiG6L_gwXQeluRUJ1kqbFsirlUhottMTqMRH4r5Ybw34JJqzb1xF3Z3dbECD1_wKyitExGfO6Z-tJfQMvuTaL-HVlxDhHbZkVlZOSEl_I_N0WS8KjeBncgrM9_rxRCwFwP64-JKJUEbhgzvr9QTsz_snWjuiaADIF0kSH107rwLnTf7As9hdZY4r7IgtVgdFmPXq2sQpGC--q3oZUHIfwEHYXvF3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFstbOvh77IcR6VJZn9jQnucjLnYgd4ync3VtN4gplyKyD1IBmLBBW3cpVzdMAmOzbu3NnuybxN3b1x8JoQ1izQnbbyb9ORhs6YITL2tuLX_SEEjMd1Aa-mSkmlhkqfmSR2LZWETqVxrY-3Nv4MSQN1XE38EaR1YGdkqcB3y_PNYpTRA-3bCNsURVzlA98th7agbuwKsQ6Y7iqyTrXZErg8-ILsbrMXyY9DVBQH5X8AAng0vXi835J269oEN_NKFeQhdJ6614oLdNUcWp4l01dEOwRLoHRCLOeWrE0wGbTAbKfP94Zg_Z7SX_r9LA0y0MK0qOT1KkPcgdE2EwTqW9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a36LmTv3XnhpcodduTL1lsIaOPd4rzGZZxBeT3xpEdcSFEmrgGez16dHyLty9bsJVY1MKYS9juQlq3P318U9KlkizSWkDUkidjB_lC-otQA2I5uN_bAE1wlRmd7Yqg-JtjbUTgKGa8dmzWzfzxzo2900Yh1jNjNut53mDKVNOoyNyhm6YlGLvWta-ESs3Qu6oQ78krPoLkYVr5KVmaYjkofknGN5UrbQuqgvuJztPwtWisPTN38kvs3lfGFGSvNyG-o8G-z8367m8fo8Tph7yatkqv5rd95Wil6lLM7DR86u8IQtyXRRJ9sEY442GfcZGPRPttQtNuvqGndyLqJ4kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jy3-ktMSRTRfMTMUXWIBwOWqjhdoj7VwQ3UxljfJnKORaMuOpCgGatQXY5CQnvA0jMQZPCR9zsAkAP6cjvI1-h7VaxDZVtUem3_RMEDZWJhMgk0agSBqF68Ia_BYTlLcOpHxBddoDtpZn_nF_JlGCSqxFMtUEao2N8e_-6Xuhqrg-fkkK6AvGeyIsWKVhnIC2lSsjrDjVC2HGOYHTKQRvZJBbSa7aZUc59RiDOWC91gAAb0cMpGFmqsl6xYBtr_JkIvWybMmfApvlgeMdW72r0cwFZNU5qjhXprNEcsp3OqQGL0nqLFUwixjuaWkeD6xtsgdMOALjzm8Ms76Z9YjCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-zdhg99t6GjkR3P0UkpcZ57iFeP1VxX13phBCbdc9vXDqwyyoLaN3G3V1wLk0i3lXDKBi6y0YRnA8TqHy0V9Ick6YGuasmK1fnO0DAmF4oFd7wPmVi-Y5dQp8trVRgACWTashAjqHfTCcpC0As1aNQJsnTN25oxK1jmiI6Qity6gFk0QSd7AHOj3IvgLm-Q5NealQqztSdfLjbYKMJd2wXcpCRcpZNx88Y-WZqG8oUojDtE4YKC-x_5-UR5u1-OSzAAm9DxofysBkb2dd6pTLDyHDrQLIKOJtbZiuVr6rzrfsvVA-KYKe3iIukOAkXLcC-0XF3T-ADQ7UkB1w-U0g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=At4Q2OKehvLM34ihoByFSbE_bIEkU0U6uMj6A2rH4xx-BDzAYmdMyImgU4AniJk0YOtOIAS66YSZSVPmQ9oUUDPG-Z734q4aLXSjpYx8PrX8uAJK_SXUXWYaOSOFxvO7D-W6Im9z7kgHwnr02ONSZ_MTqbYOFwPyPmKZxiTRTnN4UJUF0mItOfnik3tG0rUr5oLR-eblLLsG0xt6HXaESwvUMzjXA4D7ED3dJJKKimZbFmwXKvFhTrzNZXwSuMw_dt_iE_WAZEm50ET0LngCqKdaK3GbqG7eWPcO8xLY-NJYSHEcsBGOWDa2jYLAtMy3_agE_lVksIDlSz3AfgXsqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=At4Q2OKehvLM34ihoByFSbE_bIEkU0U6uMj6A2rH4xx-BDzAYmdMyImgU4AniJk0YOtOIAS66YSZSVPmQ9oUUDPG-Z734q4aLXSjpYx8PrX8uAJK_SXUXWYaOSOFxvO7D-W6Im9z7kgHwnr02ONSZ_MTqbYOFwPyPmKZxiTRTnN4UJUF0mItOfnik3tG0rUr5oLR-eblLLsG0xt6HXaESwvUMzjXA4D7ED3dJJKKimZbFmwXKvFhTrzNZXwSuMw_dt_iE_WAZEm50ET0LngCqKdaK3GbqG7eWPcO8xLY-NJYSHEcsBGOWDa2jYLAtMy3_agE_lVksIDlSz3AfgXsqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfsbFM1FV9UQSNgZL7VWU-Kcfc5avBxkGjmUs7bwm4RQlomADF_d2qnJOu11MJhxMhvuizgpc1p3HKr3V-D6ldp0qI0rIKNGNMhyOZFnyMKdOl5FmSHn512xxblO7S-LRgT3SL4rfwWSbUj39-NwSozQNdoPGWWJbirCVk6GapMIV4hE7pTU9IdWbTmeYuBspExSdMctQ3kbIhJ35lyrHBcRxqPPVWuUivVEOZ01r6SKktkoa6BkoSYSDOTEXD9fLmI4fBlflvDdL1rkkSijpSe22p5OgCiR6w_gHwa-ba2KgAH4cZN87xherRmKCtFksub7-TFWX0TJhXxP9lfLrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6vrsNKXwXxEmTs8o77rUeWzC0bKqEzhD2LVg_wvbC66NzgQ2OFviyb5uZpt2X_xapaPqMlAbcfLGZABrfHnr4ldAQdGh-_gwLsgWARkyESuWLP5yIt5t3F6JbScK5MmEIpbigpsFN1T20o3N8EvW7gjxVJhoEeRVSezHzZ8xAMhrbA9mocIwGt9zA6BHmFKp0fHxGlgNUhyzKG7K6Nm87RjRZI3emjL16CkK_JAn1g3iXpF5gdyJcZo6YamlYwkWWPvNPsE6-3UkzWfDGin48GGPw3ClD6PscXKDdojG_6gQC3phSuRPndEGMLs0HgLLxE76khyzP6IXmes5LVmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THzsNQpu2-2eGe3PTuDa1HBcScjTVFtw8Cu7g40KYsB_RVF5Xm-un5kESBUCWEttRkLT_SJRE6DHPSkOQ6v6eOSKiLplEVSTXQDkqC1sHC5A0q99YFlKPHO5PCFX6llM0M93T1WtR7ntOD3LiKndmmZWz805t4zQJefQMV4g9_A3sNqyhy-pDGpLmPexhDDE5lRNTc8kT_S1-v50IBwcXyDh4dWHT_zlSy4tvLIr9_MfBp-5jNrmxtYUm_4xeaid5ngZJrM0pPh3BT2ZzEXzNkl0swN4-v6jHTh4m-_IjdxbZAa7cspbjzZ9zfiJ4bm0iGM6EWqujeqsul4dVRLMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJEMKdK5DvpfvLeA6Nfn-EdiXOnmrZ4vaGabrLxEGucCIm4A0KVulftvaPmg9NAhXa3Ub_w9oZtjp4yfg2LKGOY1MI0EFvwsXy6jdm9u8BMcByaXU5SwSU5EgKYNhQCkSUvJTqO2iNoOk8TauMsje1eYbX2JKYVKQAmyXYRmTvkoS-JSOguoIMqzYH8cW3RZ3zLaRHuT_oKMAzaIjrIjEVGxlDghAIj1vuiwJIonzDptlp0JQMrpFwYew9G3u0esJ3OOMNRAuusgH-2aScbOajy77MAmSd1X2gDvs9CMwBxlUkI5l3bBfO05w7MVhQue7HHzNirDgU1fj007LPSBhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg1_dJKvxtF5xVWQ68dSZsgkUIXBPKw3Q6hMEfXLrnjj6odKABWhsoh0rJ7pqIs6wsgxtIfKKOc-Q7Iohr_mD-6OVicFilko9Hc0xsw9rq4Ntvd4TCT0sKuNLR7gQTYLVyIcEcDCcreU1-z5a4MRAG_qyrC9TTVBQEoXmneQxKGD5oPZGsnOf4t1kSKEFi-Og22M-9S8lwCzAmg5j6-3ImfDyJD0Ia8JCx3D_TL_VlQmbg93y3M7OhDgd5vKyOVHhQOQfBQXKM_dseTYYXeG8_ootjhmYxG2m0IumxxeWFKE3YnsZA2jXQowBVQRHCQE1i6FPZ-GuCUbyDhxEu13MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtzgEcl1z32dXvZjRMEi2v367hKRI8oB3WQ1-rxHLUGKCKlimb74ATHla05bzdOYuUTI71tYO3mm5J47Bk1Aeq7XTHGKz5Dt0sbJ4FUoWKM6CsmvQc7rdG982sWbt2XeLAfA9r65b4uErrB3KmGbQzLgiW632rnuaw4vr8KCijKfI-_EbbL4uPM7ZeZNu3J6TS3Izc5IPpaFDsRMG74ivbhN8-IyUHt3FYX12ieBzW0bGeGOMJWRhUWXMT1HxWWQ04o7FgnKiG7Krkkyb267_hCwganctWS_1yqCvA6nQLzA-ECmxYEPgXmD1wfGHOy0o7rLVT4h78qRonqCA6zZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNJbrbW5Je4LpIGIhSlhSQth4yqJuJVSwkGEgWi4v0BW4snzJwAOGJijYks5QvrtMt6SMyAiurBNK5fC9HV7ewgApnj4h_HGcgvykDxRm4MzMZr2hBD1HiWC__IuMcQmp2VA98oC0mbJDtZTIwdwre1kTbVtMjBj1ukKg2IUASXGWdr1_GpgIb1RajwChLArjFhYSIgZ-h5en6ioA-bz7S0yMzfB3mjXmD26A7Oyk-UJ5GJHtkPDLcUKkW6VoIz0gnWMemeAbbGc3s4mjhNiLHao8mCovb9GOk7QNKQYnE0t1shOvZWe3HhvWhj-6NrxD_lAxjycft2HUwFG_Z1tcg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=UBZ67vHRm5ADQnb3QlXiwxdW2fnTCwM1DP5j2YXpmJYPxBrgM-zbO1zZgAnGsNaur0yKPc-VaRXEcfLliejbDJvuAVebVKVKZUzXg3v1o21-u1pbxbmwDUl8fX8BctLD_uOxza_5N3X5VNBz-Ly5v-mU95Ovq_Ew2SpwV7oTFklsEjedA_Q8l56z8Dkjk51vbk73OjUVWLZYTl7LF-Fwp6K-pL8LMo7wjDMVEekdw3nvBhpMHrQ0hht5R6yd3vCjThY70D90_WhJVUoKdONHxeWiJ5WAIp77qwLwi2q8hwN_OCTH6SyfXU-tGrEb3pbKancKXxRauO1ehE_23I52l5lasTAo_NRb_EbGtaV4V7J1POa1xOf_J7lOdLOxgvk4dA7AViLYV-5adzA-oTfXvZfX2cfz-HDNIKAmTBFVg7eMnGQms8JjA8nfablrvhCb4X9a2douGROY7tH_3ZlA0pOb4PN08i2yNiI3VYCAKeLOPRfRiZvXMz6GcfVehlp_fYgZXmRipb6ApA2_hr2_ptaFFvTcatPI_68w__mVEDsvewewN_vyKEVsugn2x42Z7zscOIIMbMr5CDzefjVTH-Q3wGQkaf2EDbefvvI1Pp-AIpJt4LSvKoCpiDn-bnPxB3RhZ0kpQpIZa9eHAn0ceH_ZWO14SCEtiZfLBiBbrKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=UBZ67vHRm5ADQnb3QlXiwxdW2fnTCwM1DP5j2YXpmJYPxBrgM-zbO1zZgAnGsNaur0yKPc-VaRXEcfLliejbDJvuAVebVKVKZUzXg3v1o21-u1pbxbmwDUl8fX8BctLD_uOxza_5N3X5VNBz-Ly5v-mU95Ovq_Ew2SpwV7oTFklsEjedA_Q8l56z8Dkjk51vbk73OjUVWLZYTl7LF-Fwp6K-pL8LMo7wjDMVEekdw3nvBhpMHrQ0hht5R6yd3vCjThY70D90_WhJVUoKdONHxeWiJ5WAIp77qwLwi2q8hwN_OCTH6SyfXU-tGrEb3pbKancKXxRauO1ehE_23I52l5lasTAo_NRb_EbGtaV4V7J1POa1xOf_J7lOdLOxgvk4dA7AViLYV-5adzA-oTfXvZfX2cfz-HDNIKAmTBFVg7eMnGQms8JjA8nfablrvhCb4X9a2douGROY7tH_3ZlA0pOb4PN08i2yNiI3VYCAKeLOPRfRiZvXMz6GcfVehlp_fYgZXmRipb6ApA2_hr2_ptaFFvTcatPI_68w__mVEDsvewewN_vyKEVsugn2x42Z7zscOIIMbMr5CDzefjVTH-Q3wGQkaf2EDbefvvI1Pp-AIpJt4LSvKoCpiDn-bnPxB3RhZ0kpQpIZa9eHAn0ceH_ZWO14SCEtiZfLBiBbrKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIfhDzRZXzwfpvGRkkM9o-i1rY48IBtfQge8MPMLNAQVH9pjMcpNmGLL4mMScDGM_PDRtgUnJYgcbvn0FuIPvmvVwygGl8BY9qnS0PAeimXp6Q6n9riLkFBIu5yLsdehmx8PmlWXf5gGIhPgs9MzGlK91qU82QFMscNrkRb2AE7Fw4qljB9795e6Tase6Wz4f3qZk3SmKajCXG5so2aSxMntshyPZ_-vlIuqq7PVCQpPUmLz5E73Yl076ikUq-vHMP1Nfzjikjl_ye0PNsSIEinjw5ZvdcKKf6fOlXVp47jMy45wsXxsZWsEH-mDUE8PeiNcSUZmdq3Ud-0JmBhKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EN3YJ9vQ4rl3ltJvGi4f9FDKUZne6uRRiRghtf5dFVl5gmG9pOQF3oGOwWOsm2p34JPz3K2H69ILqho1QRsOr7ORMGoaygUUXyvv58Xrtq8wp341dRwOOQKyKU1nb0BEeejPjd0tvYFEP1SXbd2CTfd2_QKjtXsjpHFdy8ZrlsZnYQ4h2MvU7mYGAlgj_LYR6bWHRvUKuf8XZASGtGXEpL--DihFNH8MKHnVMtccnv2GMmruWxBItOmOPU33sMTizjBsiBR9YEG2Xcd2fs-1VltsUSvU3WeeSli5cV43z5XiDlUtSEBcy64p5U_tJY3X-KG3NxOeZvbuLWolkJICvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfL1_VGcIuu0PH_Ir0eukkwRE_htvH1BZ9fbmVI4Zk_MEthno81hGliQs5uWFzSpzevYcVt_T_SYc3bT_N5KPjENlOk_9AkoArjJ5imER3Kr8pIeN3pXTodM46rFzBBQqzTMB7hKGgwRKKr-LwBxiAnkDdaH-YrkULcmldUNeeqO-WaOC5CJxE_jC41Ac0rXKHLr_BqVzclWOEZJ6H5Vfibbp2LaBfAJ_rED1oid4biDNHXNKx2ReyHm6QyfA3IsOi5jkI6hKwxfD5NFnDTsJgMiU5d4B-WVShOxK3-gcoe2ROJeGrpwh3Rldd1IELsbTRotP9MYfEbNTWrZzAVKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1zUmm3wK3GnPAiMLKmrhSux1UlsSIui2SvrBY7H7o5kzDMurMgbvN8j2TulstG5ifD1j_OnmX5e9OsGSbYVq2sw_NpJi5PIv4VYyluw5uRkh63yAFigpMJX8HBww7tAeoaJ4hv_2nqQPfiOBtEYyyBWgy5BGl815FvqWcnGzzGrbrHIC0CEukU5D1GK5eW-acUDi5OqLxbJltTSfxHPUgfpyJ9BtJcu1EAFgvpaEQcjZVwD5YSyC6SZmRQkh2AqXefx6V3rxQKzcbrWDZzw0BLZqGpYLUvST-GentwYAGZLOu32T5BGEnB2Js45JsZ848WUJdO_kU0duVFdfxvX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLfbbgkENafrYYvWmJBL3iINMd3MR1PdOTTb7qK2y0xsJf1q-0WAEtf8Ppw8Rkj8ZTsGjwZvl2cFrq80Fm7m1fdAC17kJ_4U0UQCWLXej7vsZrP-NlG5odb_mqJY5k8N4FpKEIv41fP0B6W3K-WdpgxbD417-y80dBhBA3RA4LucE7HI7ACQyPnH7ZjdYU3usC8lPIhJtCC3ZxJK9ZFQzIlGIQfz5bDWbk63JayZB1SjLX3cufnj10J37V5XOUSMi84EOvwB5GRpHyKQUD0T-L_pHOYZAgG3YuOlL5a_y_CNocrmMJ0ZP_kJg_6GpyHCHxzsjVFJnIbQTCfjNMp4KA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TZNTT25zJ_CqJXOHo3PZSaOicLoG6ueXGSf7Ne1YQAOIbUb4pY705cJ1e-JTd-2pbdcym9cB9Bp3KAS5qDVsAA9siK9LYALYdL6y8I3G3EmiO9M_Jy9JCptPWzsWjJBae6Gy2QuPiW5zHBBgQHhfZmCeJaJ-KfbNaCaQgHf5BRqe6V945tIT4GsB1ImgNxzgcREhrwIYivCsrjHNUeQrl81sEAeK7a2j8OPTMJkH68XAHoFPaO6xpXVqiaLR3gpd0EuWportpbnTjYHHWqM9np4x4SH4fzbjfowE6LCvHUs1odr1gTrdcjpfzEfoqdiRIFIuXgKYHjJ_zPKu14F9Ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TZNTT25zJ_CqJXOHo3PZSaOicLoG6ueXGSf7Ne1YQAOIbUb4pY705cJ1e-JTd-2pbdcym9cB9Bp3KAS5qDVsAA9siK9LYALYdL6y8I3G3EmiO9M_Jy9JCptPWzsWjJBae6Gy2QuPiW5zHBBgQHhfZmCeJaJ-KfbNaCaQgHf5BRqe6V945tIT4GsB1ImgNxzgcREhrwIYivCsrjHNUeQrl81sEAeK7a2j8OPTMJkH68XAHoFPaO6xpXVqiaLR3gpd0EuWportpbnTjYHHWqM9np4x4SH4fzbjfowE6LCvHUs1odr1gTrdcjpfzEfoqdiRIFIuXgKYHjJ_zPKu14F9Ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK4602HnpyFcj1hgsBKX3r4Ki4lkbSaowsi75RpTJYX_1s2co8ANt1_4Jl1hNz6t7GW7NKDUCltxsHR1TXo2hu-St7fgYfKOtrXa6R1DYKOwS9kGc3hLJY9buVN44BT67kPZk2_z1kivETi61L3uz_KrzadslUNw4HtIINo9ay4hMW5UP24vFphnmY7GhFAjIl_fXje5m-Btz9CpZCSPe2VhziE_S8fCguNSRiAa_ysXOMxcQsFqnmiBeIdWMq23kMkOmRoWWCihUHUbDL1cZWSisLs05TwmDvtG7-ZDrjnBluMrQJgZw8WJqx7FCOYXS-yU3yRPZ5ZP3r7LYYUYEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8T1VBnHemoLnIMR2oVnrNZ1lana0rMMHWreHgGtCmEXMn6y3GpOipcMVKikpukjjY_pINYdBIJd-BZKqWeLvIEM7znOh7TOfB_Z2YwenC2dAejr9Lkz6vir5VqmxS-NpdFgdEwfplm8nxb6zeHZBucr6G8Q0uwslqee_rbuvoAZTCvAUGWzntrK2t41_PsnSRVaYR-ukzgrhpDQiuP5peDWUUi8wCm6urg8nARbjdpJjD8piY6EUIol3poETEdommVtE_eJw34nJup6-I9r_tjroaLtczV25qWE-aj_9Rye_hIhf2V3HI1GCTcFkWfUQwSMs7Q-qfbq7XRanEdwUg.jpg" alt="photo" loading="lazy"/></div>
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
