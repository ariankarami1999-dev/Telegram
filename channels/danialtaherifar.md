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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 02:25:41</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5kloEkNE3Aqp_GkHC0CF3nULWslK3YXfEB7NxUBmZYFK1_c3_8lv17Gsox_Rj-2R0p9QBgcyqogVIStB6NaLL0aWn-_ofcvpWEVsv6J8hse_3x5A3gqRo1O3ZaAIfzrJfrxebHvnrPXuT2bulG2GwcKrSSfV10X26oLfY9GPkKBIvYGgebrcRx-iALsg457VNe1wL-NFygUcI0BycLVpwd9kdQMkRcTc7C1RCn9KR6WUEBSFIogXCmMyFxjPTuR68cQL8Wa7Pr7xsqOjTJK3ZRVfteOJnW9GxdT5TyPe16GhBV1_raaiAizYZBOMy6mkWt8-8Kp80Qw6yWtK_ABVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 270 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 499 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 634 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 660 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by7mfVH3Mq62DbX5UkwuhhYA6nTUqLNW9oqLvzguB7OX2TnH2CJq2PlZK4s2XdJ63P8hrHg8xG2Hyz9sOPU_hwJyaWBw9VVBd2L1Ih9vIa4JRW-Z3geHw-7lFQPsaQ0sB5pleaNx6TzcUjVyse2PvtmEVPk1V7QobjGo7NPPjRhDfYM56usx8TdN-SWMh6raFGauRvhj5gBmEEBcWbldifKKN-0PjKTEG4cxAgYHylpn-REaSK8c8kLosXNy7pKsxTi5WzDT4QN3_O-DgGFhuGLYvkzvfLpyCW0CbR__B4hETSl7G3AslG14hXLIrrQpn2iBRuaLLWS2CRtcG8nfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0s5ynJonfxgtV_PRGf_Hz9Ftr9ndRibxYfFmt6gjVlYuS-NrxY0boTtsrLwXaytkqOqQ65s1SqjdnFI4aGchjtoI5siOL9jV1ctHhab_URtih2qdiS1bYioOBXLVPQA3uKBcuQSinZszRRfoeiToJC4GFxy0AB7sengYXH1wtl5teJHDqUdn4ekgAV9yp77sb2lGpTIiLWku0WWW7nGZ4-IKtEZkQkyuArhTxGn3bXCIb1ajIvHx_jsn3PNtroN4o72zpopTZFPqW_a4I7yPtu9bHZMADxkajyADGjv4pEXdUVoeYRdurW5Z8qK5lxJS1MUCShF3hy7aXO14eOvlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnIaKkkFgvaqCnT1q8je8W9Sw6puFoS2DLCEgMtEf40sEPeT7b3MOY8e00aPSCC2blYLPLhYLxEm7oY4_uaggW9IOjwagN_ApSfKZoz0C89m4WdKpTFncOdcoJNRrk55-ZReJwftOZlwIPHILSgyL661R9_uXjGTgJn1o4PyvsGqxTqdJXG1C2POKAxVpioqUG18HUcPwe0bjg0DdU1w3CxXeQFv7k8UNdW4dBze2XiU0JCCha1l9lOtCgeYaNLgdv_MqDW4C6NKzW_-vVQjfgN5wyzS5TXHc11od0PvXM7QeQy-FJ18mEh8hV-n1rKN72lpYce5a_7VRo2o4Wl-mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noRtGk2Chz7Vr5qHHGF2IFIP-hjfba3fFbIL5jHe7PCZ6YDrw_UOK2WsnxjhEfzaXCIwhWp6o9f4hnFrQ-LfqCab-vmPHkf0lUR4Sk9oR25N7dgzijdqnKes0O3jlQcOkIKTfV328xjsiqj9abiWySOnSinnZUweXKfuBzpD_PChMmMapfynXrM44GfVlLvFwBYxPQCtPvxsVGtNSgtV9aJwJ-1gnOwKmT1V7stW7ZauypLud9UUqdI53BxN-7JC8Qvqm-1vNs2kZkU2YXCBgoXJJWblMEN6icR7SSyRdFxOC38uyhenNnq0wfKxkLZ31iGkSrLDDe0RS2pifQSZzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYJoWBb0NVmfd103HhNBt_Q5hIphey94CZuDeuEupdbTSicFFLelv0a7KgOi6tl-i5kfSXCJS79TQb4HWp90QEZeVSl16gAgHnpYtU8VotDRKuqE8NdZAqkfuszwjcO87WPVKShL4M2cj6c50jCoIMjTb3GxaPcBPLyA-qGzkjVMKonzyZLPh5rfKRelKpLmZWBMbRErVvpdtDrKVq7M42_8pJpxlIDj50X-_snfPo0qSUvPwxSljR9HJb8xv7IVRfaCHfCKGB3qDPgIJaOlHLt1ogwXYP8ffVJNNBA1a6KVyztps9vgpr_D2-YjbMhaDpqCBTgjfn5DxDrSIK2fjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGTkokXlyAtZkYXeQ1j_v5MdWGFBwQoE_NBp2UpdSxMxVF4SmGODSTzRFPt7SmwA_shFL_rA8DW7slnI9kyCEXskRC1XlhnncyIrbQSM7VXZM8SNmGU4zNkQQJUEkUMAERTz7PgMq7QrfWbh7QC3h01bshUAiOd65HVQo18BU_iTs-SakwBv1XrYsmKnWIeAB_mh-gAz7jiH7tQC3owCBNK9aXcaIXu8cMs54tqAWy_wArpwhcvZUVKDaFOwELGaRdKacdbJCJubM_cGqHpSyO3WsY7J7ldFxNQIMczeue2079FodN7hp9qcUzLzZ9wmqbq_5K25MqDDECu08ISxnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIQzkvTaC6ze6-BwjK-quAS-JnONjOePGwS5aYpfSCgeB9sUlKpgHeQ8VK6_iNB8HLv9TE2-am3FC8Ik42CprkTQSMLvDzFyxgDoKekN56hqvsVGZxEnBA1TBhHrEcnlTwkUP8hclBxkycSFZ3nH0f9UE2t4Eb-tqF-7zdYG_umLHYQNdaHACHLUS1fQReDNAAgY8dw6gvOwH1bEQs5qKPQYJfmplGnDXlsTnKjNj3Uf3FusCk0ndpFf_1nkt8Bi-hYOfkldihDY0pFbEsLF8FjCJzm66kE4bosYDFUQJzixzfVot-j2pZ-VK6XZPXKr6vd3ngpCB80f0udb_gJPUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0OqK-QwWwV7udbl3PgGX1i7fZNV7wsth7vJOo8EwsQiy2pK9LFtqRUdqfSDW7mWA2N07BgpOcWee46r9zIyNW-zfjAhMUI86vyPu4YjkrBj85aVKmr23x2qaRPMm56NKcQGd3hYLOIIENl9rjhH58NrX-ROTxi_9LY-cWurUv5eJ8-ZP70rRerogcQjs2X0qdDxm9zTVRdkWBu_ZFEf6OcyJekyHwpkhOkQ6u0SNGsUDd-44ThAZ7iD60onfWU6A-VYD_zzrbEfMvxE_hISxH-w2dWKbv0MW2MtdlT9OEwSyQrfMU5PItxWCqDgRVBi68wCQqIWlMGiV4xbBas2Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRb3ER_3L5WOfVbp2fTFuCKQhRIQHy814oQOiPUgoKsl9amkpMtI47i7wANgiM487h3QgP-EuG4li-tZG5dXT0gMYUzxJRhygKqgDYvg4aaxeul0GFKl5HP0QpOnGmmYa_ZJiZc8TxJ3YvM3RkvWfL9Y6JsJGHiX3f0FyM0kcHJaqgZzM-hzWZ4Wz7HUJoJXHuKfqyTQgFVLSgzR9u82thnnM8HdB4nTyO1GWrvB4lp1kkn4c-AOo89H5XBRqRiLYwsXD6rYMl_t8AP_UV554Y1-sP95GWpq1IguLajIQfK6ygYxXT0-oHYmQkewwaXFd66YuwSE5J6z3jDRRPYqcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEYwG2eO1U1ereKvnD3qqVbl2tyGKEYIbIZg5uzrTJsCXWm-aTe9xDj5HTKG1V4KBG8MRqSpYfsomNBYi2xBL6hwCjG57AhbmpF16sSZDFZ9U3ltxQhbv54P09-OExQzoaOzMRKJ8aRheXh0yla3H_ixcyidROnpFqXUl4UJYWBqckKOPBEW8JFGKd8K9u_6UdnXLawndnV3F_Hz8hYwObjUT3cWrKEngXXkkNboHEJ4gLpoXUQck0SuhpJ5Ff9qk4qx5uKbwXFIOJL9EVVlD7Y604JJ2EUgFcwKFqIK9l-NLKtMarOQVqar40qOaQYTdg1H9ErxhOgYx2ln5YXuLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJFOVfVkgw_NHBLKei0-_3HX9cJnL-2O6C_rZ1K8-9sFRXbTPn8ZQdEdKRM_jz9iHjfBajaHhAEQO-s_1SNCPqXzyIoowktcyBwsYmPzuxlUNV_v3_ljuKxvE6qaczseL9OgpCTOZEH8cfCgk1FNWLbgYf85iF4aEDge_cIE9P5MZMFUxtShlKwFymAIq4P-tm04EV4ZD4q23yLhTWboWVlxhxQ7oLStb-j6HzdyWFoqCgC508Ab5e9I_yb2iH9L8FmTJp1JeVgoLc7A5T4CHzaWn7xtnLS9g7XSfjeCDi7qQH_h2YJVtlZTNTfW7H-EVtIA6j1AnS7cF2-YHpccxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJebe6HhpFdKPowdU4ownHpEpsGYwmVfn1JaYmTrHGVCCjlMCbvEjV3zby0dsxRFrjJ96gPN5ISE2PPbkFbuB7nfzx0N1wEfVkbDvA868PrUMlY-lzyZvAkHdDVm_8UL4ZhSI1rEyxPvYat85R53Jwl48eVLzES3GCme5srKDdEluJhxaxIJEt-Y8e5oXv5lTyvwm0MOH497gbnq9Dnp8cbFnCpPiG9C4AqJbb52Us7M01-5oUpxEsRMh4z4HkM8nxPzATdL6aDDOPuvaoDjGhhkbNmeqTdbheXZYnFg6rCUjqYO0kvQrVEi-PUkQe1RAX95Mj1FlV0bQSA2YS5qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_US5z6tBgj31P5Pwj7AR2cFgE-_ZeXrApjIwfzusg_9ngNsslNRL801iD73oRFm6RzQy_SzLniA50fmMlLgc8I5iCDUfmgvQRNh4fdgTqVkqYHn9UHwipMDIwu7EGeGFvliHQrlnjzdV-dI2vXpbgIIiFrbSGBt19wDQgL8oDKLpskwPwYZCcU_iBPPyJalpL4KTAVCcPbIQlEpjeS16YtQ_ciz4jFlcZE5BIK7VWKQja9D0d5Jptovfh5LN9RXTVILDFnIxN2qKOAo0ciC3aM69FJdZtoT1Ty6-fs3yvG9d9SircCQEx0Lr55GvFdlWw1B_h0m6G2GzNGHY5wLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHAbxrGJti_He65VRqblxnxsxUyFMNppHBaeVWDFpFAK1_9f-ELT_W3tek5-EE36QqR13oe_jn0tJOPLqHZrFNI46mL4g44Wl1Q0EcS3mCxoxuW8y_ocvE5JlC5MHCVlO4g-r3xN6qxHjqKfIljVZOfzqIZDIWw38xoDwLbPGYa380o2f81rofVffWkgM57ylWfHyccHAWBeujHQMBnhf_SEXY9a-I_EY5bJew_ua89pFg5YI9O2AqLIoKmPukWcXLn0NapIYwEfY3TGRGZeJTTzuR1c_qujLumyHEbGAorrdPRz4aYo4q9FhFZ2DfzyMOoJ6cLBr1og4psbShjH_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_6E0P7Ot5-9VcBd2fDt5w4aMsoYQjR5oO41SEp_WBWgT4R_ZEEwxm1KFgBLir_6QZDk6D867o0zM-Y_x9UrQHZJ3TcjEdQt3KhpGdsedRVgVjrIDGlY0aaZqJ93L4UNUHDtNQ8-ZhiEwvPl5pi6Hp079BZp2WWP-ZambqjlOTWD31t_tE83-qYdsv5TbD-8HC-9hCbCOCYEEpY_lrY9d_Cggf9o0ryq6WBq50gzpHyQtLTCxyMqhd0ZnLiuUBHrZX1DuFeCycHMk1QrmcPImO9ET85ntEDGX5_OLQ8hOoh2IqmLY2j_7EBxLT3rgc-Cs1CRW-o1U7VJuExpTSPtog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=AuvztVnPIiI3Zx1rJuBpsiDH3MNUVDM8yWbG4-hl6_OjjCLD58moOCxFQldO-dSmt4LGaKm_Yhqp8YMiJeMOzd3gyThWcoGbhRyDVThENzgrEd9rusaHnVAM75RSGT9OAQok_MRSSUAK-wxw9HixPnlu2HwQt-_413WmNeuZ6-IpQLNImpEnl_pl7oCp7KuaGFn-UK4Z6fB2ieMW9Z6S8WSLEPRT_c4WUb7E2gAvvhK3o-_bs6Os-lFj-Ak410lpHeF94tSbdozLA1hDq0JqBNjb_l3KjabtsWTsAoq3sag9PLeuDWOS3yQIkW5LcmZXqWbvyTEZNY3jhLqXlVkz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=AuvztVnPIiI3Zx1rJuBpsiDH3MNUVDM8yWbG4-hl6_OjjCLD58moOCxFQldO-dSmt4LGaKm_Yhqp8YMiJeMOzd3gyThWcoGbhRyDVThENzgrEd9rusaHnVAM75RSGT9OAQok_MRSSUAK-wxw9HixPnlu2HwQt-_413WmNeuZ6-IpQLNImpEnl_pl7oCp7KuaGFn-UK4Z6fB2ieMW9Z6S8WSLEPRT_c4WUb7E2gAvvhK3o-_bs6Os-lFj-Ak410lpHeF94tSbdozLA1hDq0JqBNjb_l3KjabtsWTsAoq3sag9PLeuDWOS3yQIkW5LcmZXqWbvyTEZNY3jhLqXlVkz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEO2fF18Eb-NinwE83SnQoVJnz5fWRzDvD5lq551RUFpAHfJZwXSqPI02rZvCq2eoSoWaxsYREvuh_s6UWtTYp2NmaGkJXqtXFGKGmF7cFsofOeVejAbICBUdgFOAxAttUiJcsJkijq2h4UHgrChxGhT1Gn8X2gvroK0120Wwcyu9eW5pG3pvso3Jh7HiGpItY7gRzbCcj-Y-Ad0eNFdUmvikCjjXHK-IhkMKXLCMnmAbH863ghWGk6_TIVzSubHYs76noxGPHIe9X8xax219HyYcOFLJL4SCeA3e4X63PMHRMWfG6H1mjuiRv3t0h3ySy55hb5GJ-vYJa2kE_bSSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NreLsJPBbOs1Y3IdbCkw7nw3z9cMnRRMOwxRbhdDrmmj44B3D9ng4De9WyrACTmtwsUGJNpf8XJEIgQuP3es3BhI0H_y9GlESiNztJAE6wgFcZPncIwHxKNtQPGfb8k1p7QBo2BJ4MKEbqPu2Uyp6MseZxcQVq3Sdp53Sd_DHPdP73YiUa9ymLStmnCSmUb5Az0Q5_sdrm9AX-De6YkFAtstys5JF4NAP1JkizQ_wQtlbzrrv3XddKZcZTPV97zauPG3UpztcOAJkddCZiK9zRiFEg1OVP79yV3gEHKzTCxnVRKyxTVyxZKFjfz4tvwBHuXKX2oyS4N2TvDA8ulTCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5S0maMAuQcqTVzXmb7ur0O6sBY701oG8bDRm5ak8-iVFhfj6VI3f-ODk2Dab0feVkIkfo7G4rcBgyT-kEhhcV32bInn4IRw2-8EG_8vHP0HSMUipXZptrKB3WvFNuC6xTpHwZLD5-q3kOA0ScUWL6rUx94AOZZ_KIIzfmnGJh39mW2Uzid2hc4Ct5iY6mWZCSxCTeulSAQmzInMpv1rX6PiZ-mWlDFC69aVMHnI_yDsRif-LbkxSRtwu_KxTz0U6IYJgtiQ-b_sgiwbLW3I541OlVJFqm0AtoMEJwmO9gE1aS2g3-TqPvVxbSAOHaakIINYnVkMuyQ1F7SEmf0jgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqynqf5VY0fe6VKzI4Y3b2K53PHQemQXAF6qKNI-hGCbsFPRpkZfFIMbJi8vFiS2LD_BG-B8eSOYbBlm7uk7IDR4EtrryEVjTMYdlRFW28ljKFJ-1ek-BnLKX_nvOjSInwQxtubVcQi5hm7x3fcnQfwNXz8QOBfBgLroSoF_oUsv56TSr_tA6XaeO4Y8gGxdObMeIFfQMbOljU_gWm9H-NghjEoT_BmGuTOBFuRrSFW-AMUWLAYGFOvDz1rD5QJbIoOH_GAmQFEN7W0djIAdie9_hXaSA3RghMdr7kgNpQQJz9ix7_Dco3tjyCl-l_cOTYnnals5W5P3POLd7nprRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF_V58THZQY6QMmi7-08mgVsaEojuztI12FSPNlQh2rC2xK8wRxYFOz_Ms8CpzO4mKXok-8iCCR99Hl2J7rBnQzpwTtH920WGEpNsX_-ihSJAaLHbqB5ifIy8EJWRtqt42f8qHikw9OQS23VgmSgyll_3DE5aHuGwkRvbWFJNxfrjd8bKp4SFuEb3JIFCzpSQQsx8mwZjrNNUTRoWRwu21MDxEIX1QwZlG_jD3QyjyE39SacVKuQCPWpTTTnXlro5vMO9IMX0bhiIapLx9kJaiWJ-XdctyYIVAXC0BNKzB96dRcwGlI4fexyMYtdMSdOhQFxWqGFKb30oUTMgH2z3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdk3JtDkBibhFGRtgWpH9lLWlu2H4itOFjHaOZKNScfhnpXCB3WJWyfvhqJldZNDqh_nrkZU-OPLXP3AdZPN2waFXwF4qbqLSKjf1WnyW69zll3vfNc9lTHgVbe0HL57QLUatdAhbpfpNshHKfGjOHC2p9e2GVI4JI-RwWS-3rmNivue2xURRvdaheKCRc4Zj2zfYH0OLtUvcrkkMxQEfJBhywTYj8LmK0ZbGf5lgX1LEPzM_gq_HbMRUZTeJc7QVVAG8ZXmQ27mEc1YoJHSBPDzUlLdjfrZvE5mmCljbsYWc1K2sDqsCJx-YV5aoZq49lLKd3u9cNZPaIYZbVN5pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcn7TNM8VWGCoClmUJNWm6VjfBhHFFxOaFsLcgivRRQNeX5df-c0CZ8XNe8UwO2RCWsGSdchAvQia6A5CSpHT4uPjIQRIwZV1V3KlMEzMLkUFCk1_byVEmccnpUyff0WjTbsDKpVUmX57eeETbrYnpkrOxSXe4K9KiFZO_dXrr8YhwC8QPNXWWhBYgCX---uVLPQnbKQD_G9TTGx20a_XNNdKzMPHbaRsDiZ5qYfzPMDfdScZVZg-dFy5B3i_roxiR7eAzX4BSqWRNwwWJ0ipapIJAkz_DHP0fSfmlvYV1ZXiIhKi_Jy35wkwB3t6IkG97eO1y_5MtGJqXqYl_3EFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLjLEMO7uQKITu-Eg_Tk4ykDi-s3giY1ow3dQVJrdorrsYGQEvV1tTDrv0oj32_3czfRkdMO04R_t2ZckNBL5s4zga4ZHLrUtr-RsTnhZUFfqCwnh3adMyHsPDoeh9BOP485_zv_pYHs2Wm5R5P3zz7EPDGEXhC9fPF3Wf6Sj1ES43SazWtWTpepcT56uvZ5pcxVILTFXdSJ_saBmdOsJkyvQNk23gcPxX7eQ902LeNivR4QeqFfM-gr_5PrIwNmCLDZ6xW-3lJr6USx6_yaEQlihPO7dsVybL8BfpVFlex1lctzH6EazlEFE0JEcVbE-p1UM07z1OVwl0ehn8FLUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is7GOwf4AwX5qB2I_234yDEToATv16NepkqQpDZzD5Gx8i2eSaf8Qt4ivk5D6UJgSZBO0cdPk34Dq91DQ85l51LkPpp7T-vL66uNKRbiBbyzZ3GCUkCvUxFa2z8of-rlo0g7xj9tDeZkcC4XMKXY_buYtUYEiDABGVIV0HmmowZIAzwuYMmr_O3hBGQvC_HUEybmIbM-EwxPL0mUrZ-YxnJ9aB3IukDAnDU_3Fr1lcrKKm5-GE8-6cqrFSDBagEmkKkrb_j6N8wb7jxmPBWIyH77VKpdeoDbR_KIM3VTN28mHOgZN7pikZZzvdb3q-gVbCWEAMF8u0cysgmqqgrACw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKcshgQhNRKE3syPuf3Q3x7ik6c3fJ7hHnHhH822rKuYgFJ1FkyAz96Zd3xFQYt15Vaihi_OnUgW_ronCrmDFcELrrdh5KhGfLGcY8HekZxyQsii8RX2EEep5GvAuIlGvUQDFfZcVqBFOcd9sLMfDTOGiEzy35D5W280F5voASj1O0t0kZ1SBVtRXyVTlJ8y54h2FIuWRNvK_CZsWwAWYn7blImJ_gS9yxjX2llwB7-gu3souEMw6kEYD9-4WzK222OhKE-kfNc8KPxjMw89XpV2Rw1cKg109Mv-zMr--DPC6NeddP_YjS7SAl8V7KvnEMKho5nI79ebBWvzdOOpAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_gJWBuhNVAcm14L8dHpkPVeiWTkilA2GcDbkhoq7NDEq61qf2V9FypJzSsQNkjOQuQLhwXDa_P4kLDC3ZoKXZx48PwNu5HOP605cEm0vjrEFZCKoEub1WcxbDO1ucfIEBoVRGQWSPbTy7PjGrZXPJJBNtw2p0vFXDYVj19X_GklZ6lIPPGQRGBCbcl4WEZVqcQB7HaZzU7rfOC6YqN-4cUjbjyhkez-FXGNcn8tDkOt_Ya7_Ny-DNbpgWlqrsW_VC4JQiII2J7ZsnljFkv3y1lE42CMu2vsm1mg4Vc7I1HeLP7-cWMNGIJ6Dqiwtd23v6dW4JaTIXLZIvgjmRYZ_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg9Z0b4OFOJKp3YwUkl5Nxfu4Mb9pSvOIgCktMyOLvbKa6giMIM-hIQ2nWwzKJ5oad8Nrt3VzdJKkXW3d13n_qBKq8BRdza9ohmImwVFhiUIKJhkVSi77bT5YEKa2y-3OFTCwXDnXDM16u5GNPZ8FI2Xaql58SW4TAh6nEGtqPUIGxWxDLdNvJiEF-xPYnja-3o-m4NfErVw6BIfijQJSMTpUSGJqR5H3AkbVeiLI-xy9sACSMViSk3XkZJSMRnShzrOrgSxrQVDhCfpILN3sowNZdZsQmzhMkzG-eDyMrcVwPiSHzfoIlx0-rjb5cue93zQSgz4m1FGF5gdrBv9pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPdq77od4IUzTIYOzGLH6BvSyE4Dl7TnJGcoqfwgWvmYBjv4sK4WZxsJO3y0xCde5La_v0QB26FeNYAonNchffk70VfF9r6rDr2uWufK8Ld4Jwf4jhsfOZwEAwb5haXJw4o0fKlFTt5QTvgBRBKeEYJZYkn_rUDIek97tJJBFzUA0yA_OQTZ6DcTZ0Ctb4wtLB3TM0RANeoeCGr693BoG9DCFMb0-sjTxmxbdvBLMR8uaT5BmoQfnu6mBax7lQVzg8rThRArVcvU0NBT1p9dsP66lBfdblO221JaPOyRW9j_76MKhE5fpX06rzZeNnfaKmrZlxIHMkEC7kMLvptRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOWI_Y2F8ffFQVC9woITyozgHLhSbsI0kbPkzwHXuGbXUbqtlxHPXDh2hZeQhTng3SNkWM7NkelCWA1NOmoQ8Ygj9wCGJaf04jwm-y5qL9ZH0zFcSQTJe5QYW6gBG9lSi46fUz9MVAn5_Rlnpb12WE9GHQBNfAb7YrSIxMVSk8pXwvdDcEpy7KmSx-p36MDMJz_IAQU9jEcwZ0liOP0Leudgc-xKzM0wbDknlMTt2ewSHMxzKo6OeFcwudzKO5UdCKQZF02C995YuwCaBs7i6D7O_qZqqzba0lDmI0xs7KiddYQY1IuIs0PfQFvggAK11nFim7KG0q2e9sLtMo4JfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqROc7Kqv33FcxtwkP_hep1Z-nGNkgIHEkWVFYMiCJ3Oqh01-QZJL3rGpHqcoFv1R9VKzdxLj4RiQL5uY1BufT61XNGmZMGdz5fOjvM0gAvjEUHGEGpgfqgvA_FZLmnqJQPw7NrMoQxxWjqjA8vAU6Fn78TUsZSaZ3P3QEpoMiMcSYnmlVtT9pdlXz42gkG9glrrxRY4j_bPh987d9_5aEiZyna0DT5glg4Mn3X3ngpAlJhO--cuy79HzWjRHFDkVV_VePeeiRsaD2QDAg2oVyUS3IgsSHmTn0YFD7rrDMVed0J6EtmDol3TZz9AQkUl3-lXvwF1oNJC3ZFrmNA7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khqnTRHEtGYvjuw1GJjsdXkuqueKbCTNFizYqRJ6T_Mmi7vWLOnOib8l54G-IFMwaAfk-g4ppNFL0ExCwC7-7kJS41wzNCS-Y42DziLG5Hv29giwbBMT-rWRUTkXaCB_boEB8dKyO5bP0G8h9zpjyjxSKF5BBkYq-HPmrs3B_hTimzfPBafU4nzjspbKJJS_0rph3niCb51zzlKH9mKEVvqyzgY9TuxuXZHoVZutku3Ul3UHy1GmB8sBgWMPAPQ3g9m1oliIPy2FEtn-aGjXkIETT9GS2OgeV9ynd4_FWDaJfvIrXUulf6BlWrCJepRKKvchMypb8_hakasrw-5d_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3_x0QYxTYRpxQW70hs21WkYoumJGLvMSPZUVlmWfR3Ls98WZawcBWHESFM8UGNj1-biKqVM4P1VmNLzEHlxdvKYChiZh76hcdJsMVJ-grat599-net1Iz5rYZJpg9tewEgZl5PvDs3czPmE9KFlo5cSJuoyBVDWTjEmNcmW42oqWKg7L5tu9Xv7tSRWcWjfG7mI_QQwkkXD9R4N0V1aLv6pX9QzrbBxbde_NtdqlnxEYcIUKc0sRifIBeTvEvpFGpFWIOysMjzEzZ40vrxDP_Z5B5wgrAHcirOKF48Mvs-Kn-Mq9kRog4Wj3vdt48EZ2l4KPNR60RQXx3HNdMFimg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzRb07QbLwYWXN64ELSt3Vf8RgLIUOdn3veSpyuPSmk-hz_7q9TM-lVwV4tjJuIqqdEWjpm84hq-jhmikXjBMHdaDEfqJ-hZsyQCgXdyOiKz22hMgF7OlfS1HVeurFjzv6-sKFOHXcxPihiF09QzzIBg7mMbtPrt1WELnpd6Frs3xmqZROrUYDnPiyljwunyF9FCqYhVQEvltKGeopl5KpooWQLOVVh6oSTgyp_RQm9XjnripmaXeRMAxEv0e06CDLCNw1HjAf239rmxMlBbOs7TUfY43gfKN0h5MiWi7ceN1iTvcPOxnUbIomVyYsS_ci3Q56UR2ZHEHAawqCdqEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J66C4FErNffw_N7uAdXDMdFgLGgAryeAmW_YXtg8-jlZJydwlhhduL0GF6FntTZh1zlXTHqxzv8W0o46oO5z988f_Jq4UpL3NoxEZWFJxnnYWwBkPxVv5DaofIvl_dYRC901-fh0ey0L922J5k8B5CUFxHKZghVaUthiDUP2g7ZLJYU1LHIQLqLkq3pqOdfZeKLqArUiIAXn5miTMRozX5reVaCtdJmvuywoZu2xv0XSISd41uU609vuCb3QSGYQSinVp9DzlLb15UfycUMkxi75b_Sw2GH08w51coXxypEdcYFxvaMwn3cBiO1IztwMSfmTvRSD6Sbt0_g5itcviQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRqqm6NizqL480zkisJCR-4n8QxkaBJCGludme5oihmHTkLY0spHEtaaadkjGc7fwT58n7NpVU_JeswbDKKfsDFOQ9IneZVBKOMy_JuOnkgySsKz8R1tD2hnwV_npWI2h473mLcbXe0sHMA2TYxF4PS8JR7LwYuTj-ll2_DfZnldTOBbJDoJXxW1O2XZ6hnZmZw35I5Dtvyz_NDr0ghc5hXT4NYbvG9OiwmV-9e56CzAiddGUtcOomvHAH84WiN0HbMnrkiojPJAMBCP-J2hkTcrReK6QM3oT0xAjqj8GJOdVUBPeQfr6iMX7Gd8WgwBsqWCKL2ck8IEUhhpoZixKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxauVD8y2TL50-PG1u0vQF87nfI-K1VuSFoXKmVk7xwvEQPgS2j46NTRPfllYDWcwP5C4rW13ssJbfXl9rmYXbiu2C6x5KK8hMyrXOdHmSzsAw9moHvmwYRyRvc3mI6JPGSkmmYmL2zbEPlG5xO6UAdTjqXPhxR186o-4Y5Wnv7a2QS1WzofoqYHaR2GCMUpPDXunYrCLhRiqgTHytMGCGpEPpovpCQdU_6Pb9vJHS7iS3NrENwPJjvsXmaGOwEGvdu3_hlVPxcV8AsXhjZa8Z8awy7oHgl5M9Qbp8tbIpN3adrBoHdvoALUWyzwEzo00m8BeMnH_eYbQC5MVB2AYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXV8MLTdgkYMyLdnENEBYyA0R_pvzQ5lpv-5lQZukYjEieVlEAhAUat0fxwNjLVfo_ZpSwFOigEkttFqyd4fUPOp5yDuWTNOhZ75YxFyYvHyC7SGe07nt1ZxMT2hSeZYrNPmjPqH2PFZKaDgt37q7xkJmox-45Z_r8ZwDJlhRDHKzH995Zs7yCUWwi20J60OA0H0LadsmK9wVrU6EKjGb0Z-SUer5qxoyZJjfLQcVYidpQs7uAjNgqlJ3VmTyaf8DtV255Su2yy4si7wNiqh-7ZSyg95BehlOUak601CLIDgGnmysTmP1dETcQKVAEyJznSV73_pHKah2rwrTZmqJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpHKozrx1uVdMWUe5XNbb94BdrhcEAye4CBsN28D_giyQMx5PkVvnC5wjVx2pTmFD6jjTO3malkPMs_9XZacdEn6J5x4q7nyNPDhRoLaOTKEQCwVLcj029nuzgAYtkAgvqyZLHnczW_exYMGQY9lxLqRRr84-DFTtNJM-xQ01DmpIlOcpi6WiooTzBDMInuZwN_LwvU0HxyJlRwe_9rdmRA0nhm6NQOoHoEGbeFp7emVKCMP_MVJ83E5jlK99hE3ibjkdrkchMBmU1yx2RyGXyF5IPTSrvLrI51N9IACyWJE-AdPtnaEjWoJGR_n2uf4b9vYveQhQKQOmAOAy-ydkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY5usM2Mh0aei1iodaIWepL1GkFjku2qn9twSnb_vZz8Q-eq8rKcp2nmwwJPWifJAXMU8R0uygOIYu9NOwK5RN8q_B8yVT-l0h54SDVcK7BoqbaZS4nFbUVj_Tt04gtIzCQUsHfsTGaFNiKGsvTO_ZmzfZGQx1GKB1o2CR-9eGA24l7lGvA-O-hupkutgzVQ96XlCbV2bDqosminSy7QjiKY_WIQxh0ynx7xwF6BSe7oTPdkIFjfhf_DDxuzCQkig8QFx1_ps75E2P19Hn4HhxHGcgxU4AF_xKyLurWhscupdB7kXNf1k-MmPLfTFEzqDBYkWpup9s4LxryXtMGnXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAMyyAPwl2E01qnYavMfR9xobGmStdOSh7n7TSkzSJRioU7J7A1XtCB0ciT_0HA0jZL2ZvOKIE4L_UTpQ7UWEVU6L700SV6eFDuVvKk7heZGJZrJcLT8we9t5E-cSE82tHrg2mr9uKLD15cTxHxggj9Lc5SGYVnulm4r-tTUOPqPEgcU5-N2HRLUHX4ZDYpSuVIKtAiFcxNL24z-iFGr0EnRI9Zsk9P9TsRy3sT_HCCj6TkmtRuNDIAZmzQYaeKbpzkZ8V8JQU4YpcxIFBi1d6A226rpsrFI9asGiY6RuPveESdP4bk9ob1dKjLXFHPPmDpJm8xy0aUAqCYELl5DUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgSfJvj5RfuP9HdJlV72L2FAt3xP_0R-p86SnRaaYo-9MnL2dGOyDHxdo7q_03_nk6k_d2AOSMzlCYD0X-xFBVAJubdzkpz8jFM1EdSutZ1NlnlEG1rZrSp9kxLHj2i8DxfMXtzACmmTH5ljpC7274EOV5TM9bqjIWXqNhtot6XRqZM0bMIPe3wQWP2xELABpdDjsXVk4hfE4SqJZFNXtU6TjkcigH9g8vrk9vUi7exvtgOwef6QL5KckOm-Q0piScSpr6uXNpZxGnT0kfzLmbV7AvNh8Wsb4BOK_7JXZHoRKK1jjQ4vUxO1pNn-R_-bhRf7F8UTiwG8T2AtkeC91Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDhB4yWYr_Gc9CFGAkoipgzJxcrn6W_5t47eniJSP_z-8mIlDw8JGTVDi9sHQ56mMafxzGVpQChFGW2WFq43WK6yG41yDsGu4bfvMzCR8CdKi2FhR_6jMSYhLROrhJkHhdlk_zT4rDa51LmFVPZzJ31PqKd-QmTmOyWuxvx0HPyiYQfCPe8srjh-fhCBNg91wAQlM3PmF8FJS98g_PiC-jrlB6kSFuoAOgHWlu1Gl3CwN3M64HmOSo6DqlCemV6GvI1vSdwfd_I9DBIElb1lhS21TjY6lRJwUrffWX51jttauhCfH-tg_PPSdN-BxMbM5ONy67_SmsaFMwhtR6ZcAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO-iZqAVST6q_98q9jM0mtMprYP5PGtLVBPTKwmn9xPzh0wLCm0Ch2sHD6RYgO47v1zJmm5nDpxtDmq5h7IcmUfOI7FzUL4HRqTGykpJpoKz02cEME2om6jQQfyQCI2GlUjBVWTvcNqivW9yVa0vn56V_wL1y2kYMWgqEDNit5dT6fcqGdCsMXJYwWCRMkE4Pt200VIinA7I9iZZ_4Pc6wgubOEJGHRh9NRO5yPKbEGEj-Pe8TX4KOaMySJduxNoOmR1S5VbXFRu1rEK43a4ci1wbIAE6TxXBFwFXa13XH8o4OUFF_MBeqvihF_SH1fwfpNPBG6ncjxkObZa4QMBnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WehXP27ds1PgzSbZ_RrYfORWl9g1AyOHuFi1158XmSxvnvgZWzdGDObCZ01-xs33b50ZW_nfKstc442yGX5yiekIKlh18Pa3TtNJalPlrBOmL1mqAMTcHx_gMxdhCAIeLl8klPgg0So6DHIQUT1N-K7-bZLwUb2MUJhhji2eRjFy52ZIcig7Le4eBsn5KpemzWy6634LD7Y4up56-abQQ9bGr9KhUT4wUOujGGLKOotfjxbZ7VudOUKrlZgUKmwLaMTHnp6CvBJ8rqMuB7RjrpZ2Nueb_fxO6hMYZVNNsVHCX2P3rq9fR8HNFTqU4KL5EXXsXjawNaKsQrL6wpkmWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnR5o_JiDXLamuEJCxMJhhpoitczQ2mFm3osZCiojdB9l1G4XATu3JkYr8k-lR8OY7-fIX1VnSf8nqLz0VN2EL1iFw4rMspjN1jJtN9tq0dU5Zb6KGc-8RtV7SVYCjNRl59LMCVvb54FQXFbxqJgHDRQwm7Q5Ho8IQhy8XViRR4CVCuecMlhR_UZYQeJMuDHB4ub_un50vgkgUeL4XUMB9BayN61IYdf31DpIr65fGPo2Zn40uHb4XblaHMf0DUYhxh8CWP6b7Weo2vksAFW6cAnFa3yApmj9J0cST2-3biT4RSzwqSsbCNHYW8tEg-vDfKqho8fDwig3gnO4a1cmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcUQQQkD7o128czE3nSzw0u64pQwPcXPUrIaoW4S11KHJItAGRaoo6N9i4dEIBZl0cOtIawfGfyjhAjo9z0UUOGnHQg4Uzl91Wt2vHIVShXj1wFMkficUk8JsvmzxnB8gjZIrwgLwSHGlXVz3aJTyE6RUNN13Kt_E_3TVThfQAu2i7B5jKdkIrNpv8Vrb7ujdcj0HE93clOklrRBeZ-ciKt7lTksRDT7XXYOka8ZtgyFW3Z6c6kSayZXYpfDrPEcNgbzdh9j8mpdsAxSc3nHF64d95xeoCNwzTGDj4k2sqqogtZAaRc_c7f6qNZ1Fpjn9PxA-Ue9p5jsMKdhRDzmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccYjVvWPB9XXp7FjZixrNDFNfW8snu64FGWH5xy3kzAygU4rE7UCa43QOWgCygvJoPdGFu06jWuJA4FkfwIEAc_9jloyD43dK7mzu1qkXuGRCjbGFfuu_flymQDxrrHUkmYwOBbGQln3WK3QR86iRT16WA-B2ICUBW2tRpIaKMhQeg7T8gRPwWiYQ7dpO6D1kJ_iFmZch1bksM1Pxwu_T-q9tyfify_5ZPmlaMY1cRySZuF-g_ZOHQLw_xmm9EC-db2ykrC_2-vbtdVSR7jwfr-qBRiq7KwpYoW_QaoTNbb4H9KVToFXoNYoZMRbXSWQ0e0fV6ghBGXC2McxdnuToQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfgtq_v7tNyDAu5LHOzADQ3uVCuG3HWAW4kbRBULOhAq6mzOfRmsOOO0zyiSSFiuBM5SuE8FPHPKJfU3l_t5T0Px_jLr8GJ-M0hYSatMLuolT2iNSgTz6EJIJNIHgnHsupjqdtNmLJADe8OQdd1GDp3rNtJWoeSjmHsXg7fbF9diWBEieKeekhEanlwT7dJjlYNfoESFvwfmNiaceArLEkQjLBQ_oNsimVx86WRAfKoP8X0uHfXrRsBvrFnqRBWBu4xI9MiisEFYUal9ipD-6td4wXD58m25Om5yd259FuugnYYXNDeLai_HvKgn4MztFPCC63ei5ghYylOBbGfyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6sUTR4AeDHy--fimZwcb7RzGf_yR5GV7Y8v_uNeqitZHXqKRHQvc5JAJSl7zLVsuu3x4c4o5whoHUtH3akZWGdSABO2DC2ZhEQMg45Cd9jazE5XROSK7lCzXmKUHcdl9cvRNW81qUE9BI2EXHbEqBY6noLa8AV0SezOZr8b7vPCbRNMNOWt9LwWcy1IOEfEa31YUiuZ60MUj5QQMzKmOBgR0J7sbG3p7PUZAH1L5yodmcUP8f9m4XT6gPy2xLDGgkv5iCWLbBfhbPPJ--UnJJDwd0EvznPIvMyV5cusBSK-9BSaDHoWQ9DJnzzwVkjIQrPJxUQ1hiduYdodyKxHzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUJIK_4AI23ZA-GQDa6M_den0qwJ7rNjghFBpLwEUTl-ubC5wq17EGXlaSoJg6IxEQRIFD_eySTTUQhihM03s_CADzZkZnEhvTnX01qUKWBv5sv531814LyhGRBK-T6404qs2rMdLHy3UmO5IY1FV6y1LiOpPpPIWjZ044PJbitQYmZMR2ujBGAUiapIBXvmmUubVF_zCazE0spxmi86MZxGIwfq5HobGnHuLVcl3TiCYYMkktJtGcMTaMoT7a7w0zOBU7cD8A3hFRSqGnFzFImsWyYvWf0C61AfbZUa0CfrF2M11TUNO4z3fP8iwfSwu8KHcQdcwnFbTXmwVsQ4sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNWJ4QhMofwsMZD1fkzp6Bwky_4EEEK81muZ-5iJmedrphzHkf-42rcI2jo4xKmBc8_W3gOrvJp6KL2fxWLJLfmltnil2bPFhGZu3ojamoGYYrNZWF4oveirXXD9NQxwnxeRnEsQ1yPAaSprWSWxfrrFTa9aUmWtBniA_xpL1iszdqy47hN66AwosMR1CEhNMKJfDM2op5i-q5zRoTsJ_9wpirr9nVUtrGfdPgAPMTAbPisxQi96hncyNskevCYth99Dz6ZssF5m47ppXr36Hv_WFXTccNP9QzOFjnUjxeQhwELMuhWTX4ZvS0YGqpkXYr8KKNiF21b4QeHZ96DcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvCAUGSywE5opPRjjkD4WxjWdvm0KXqC0rapbOg0U_CA0xjOcL7UJmyBZXXswIf65os6e5fNaNvb-9VDgAt9FKhMDhnzFxyMp0r4gXaJKH0E0Yf_NwmYfQb-HD8VLU_USwUMrv0htwN5lJlqW47UD-lEhjcasAmqPl1dBWVa6ctH8I1S0uqn0JMx8ikTcZ8stcPxME7lWV66oNa1fiPLOnPoPUMV-bJimRbIVtbKT7nRPWoKFAvExoSi6LfmTkAR5Q5kjY6TnkPPwOUA6ZK0Rt5fxAgqnlGvyc7PgX8UtJPrVPO_Mq4_1TUtkXJFtQK_gU6xdOUbjaFR3AlXN0EESA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRxbqO_7xs3n0i1jdJbvihfhz6wNV4CEer1ZgZP1rwViI_L0ifuqK-IfbLTI1XJiYXWzzw7-HyuAt-i5qbHSIWeGc05Uz0xyof7IyOAnPVssVV_ugeUGQZiEJERj6jeo9wR0-w5g8hngDelDaiwDbz6r68ofzTfBinQ5QqY5yxuwvLnXB9epxddidApQ2I4HDTuVZnfDASqL5fzuBXNeZ6mvlzdrqbf1LeJu3LuyhG1W6zThIP0aW4BCcuE2ccpr0WjkrMHJUVNdfbR0uZJI7XICAHYIjPVFSTNDs9rMIwduxxqbYHsUk5DhDUDsbocT0JiX3KgOxmlKISXRWi6SPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUFBKaRJMQ2obHEJvSEattC2ZkfmWTBeCTCEJghzDPWzrQjGITl6R2BGjN3QldRmSo6-rIUpkKeFti-qtsFUGkHfXGh9S6blPYHSjpfTfFlLRCCY_yfQBAjwefcjzDN2dWL5K3aU3u1nwwM8QOBGcy1ODbK1Un17zYXEpHKwLfit7xZcllitIIBrquacxn51_oyGsRtpAxMWA_-w1BNu9LkRaynptuR4NyC5NSI8M3XwGMOoF7kVR7VDLeXFI5ZCgRVQgYKd4Ctp0eVcE2eHpDXtH1B7lzSU_T30rJexf-UuIeYHJw74rfJ7foVEsp_ujxmNNSrFnH61_2FkAhss9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWUsGroOLi26CQ1IvlI8RsLCHylncuq0-DnvpdprhZuABsssODT77cqa1jtycITeJmexWKkj9Dj-RGy7Lm_uYTfYcGVNtZllc-5W4uhgVmoC-QseJHam7iA213KbBStNFH2DaZdYm5XkumpKpdAMceTL6eqeHVHwyUc5gjE3GuRMKpYiICk929j2ztigYrRVwwyj6fR-9v4mReyM9plvey-2oOo-mTDKFXe0FmV5g0dv9TlCTmiDAj30C3O0Kt99jLvkQxibBJaOmvmlvLBJPOBwZBEwn7M6BewjdHaCimI6XNloSC9grZknqzpoqhl1jzeN_xUpwrOFj02TTDouvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P95h_es0yEyXDCCOAZ31303JjeAXNHiGB0alhbfFKE3gDvoLzun61f60znHLKNs72FtaDIi8MT2F7WOy-R2O7bV48JHZTnI5ggjct98FCSted1_lIVIR0WqkFkikjbgARUjH1nyQXxIsYKC7piA5r8yzIb_zkZ3LIKTVU6OffbeoD3vLXVzvj2RaujSTM2PHB7Qktlu2yezEoSvl70BNKLvByB4qVYG3coIpeUhiEcVpvX10k47dY1YYwuJPFqCXenE43Pqreml2HbYycYggXSQEhoRNcJZaLC-hUOrW_jrSDLf4lxic9M-u-K9yveGU6PO-z0kJtFBDgUYDUJhUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmJb4wRP8_xUrjxafozdB2HNwfT8uW50bXUPqhX_YpXswF5SWl68roTY2oSJJEc_VhzcV80tlc2Ik1XeKMQ4cfDVX5ES6YRjJQugzraQ_wDu30A0-NT0gJQDLcoo9EefDdQl_dOOXNf-NkVDVqLm58WWi3q3kXLeGijkK7lntEz-GzLNJiaQ3GeNbD-iQaFSiyypIFa9TqUVChRrJJpglPSOumeVzztTQmyBUYxR2dWyhWcGV3coIC2pQXGqm9Us915sX8G-A8iGbqAFzd0KDPvpxdsXzfJD2ClHZVEAlwyrRTkEWCm3-4lO3B-8j-rpk8XgqaQ1_iaXvavRp6itWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWo6ylgteFLcueK-BZLdLVEQNLr_i-syPcvlpEeNEkkEyqiApEES8PmmWN9XH-G1bh4sDYOMq1XAeCPH29dqYZ6uerdPiaPxoywsSNwfwOq1AmSItKARLagKO-Rlnet2H4dkd-qwt64wE96pvVYfG1XhRz4es8XNBK7gdxuNz9FhfdNyBI9OLugNP52cQMCbRVJA265rdAvbQ4qTBBaAUsdCQ8nmS7-kdkcv4hqSZtLL41u48Royq9G0drHhn1xUZbV3FQ-7n5dHGMpajE6EEXcu7fXj-m2spyUESetOGNoi3lIq1uAMcLnoRM664UIRcweCgPjFmMgad7gG3AKnVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW0UMLvxZhuyz7r_hAKK2NC16rMPtaz-MHM1lm2mqz99M3ig3CFc8OPIBaD8S80bKkEdnRqltO5PepqhM5KbY7Rc95O390MyOW3HaDnCvdYVqrfuiflvW7rRVHbPM0kD4jfjQrPlt6YS9hCCtMMSrbKAXxShmPc-a_ELLNAXYQaeAKVlUkHC9uFoisirD4B3FzOnfZk-1GfAOFXwV5tFpeAj-TNowcvEe_b-VanFi7EmXXpy3LgMLBmlNTJTq-t12CL0sxF8dXt25tqdpEsIu_hui5QRGk4Q3dR1vbGfMRzm2aRhnejHqH3VOqUqDEQJmZKd2L9isxO-2jnAKdSqpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwxZFRg0RYI_shhifX0aCZNQ-oD07xDOhQLVxiLtaRb3nFJsqXNq7pYaJCHqVjbIa0cIw_18UyZJNB-PQ4VIHiRFdJcoJf4uh_1OcfRHbeLDB2fhv8IjyJe31ytwdVT5GheWVyI70vjANTo7vBtjMgQwa-brPYD5N2De9vSVo5NoTICXjfVEICOR6QZbHI7ZpxO2hzswDkmQEOQjAhP3fDE-V8wMUmm9XqraPKK0DTp7G_hfczCLsCcOq3bC0UAWn1P8loqtEaqVuqaPaS3J5HeTLNs_skISuM88kzAOsn2A6kdgR5YM6MDWkfG-hetcYb4vhoyfOyQys85zoo1mTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYMWwsTbVG-pCF5jdHOCWKOlQMQF1jGcnp8vRYQbbgAZU5xP3otRVMuGi14DVH5WNBnefiAXafT880MImv1szAeAMHWqBCU11KzxfeOL7UU-SsVaG4NPC-Q4QD9Yjm3yObrmRdHDVkAGiOyCLwp6KmjYYLhtW6c_uhblCRvFwgUSNylucXOUWTbEMttdee7CZ8OR2uAmwjXhaQlQBnzThcR3JyzZmLiSg_xbXFHI4-COWz-j_KBkA5NTRiCaPpZEoDtBug-QH0i-TMLz6tjcRFHAj2YzQZCQB2Pg1n4MRrk8x3y75gTqbIpqjzeRFk3NvjyDG3z6e6WldBsTAJ3EUg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=eWqum8Ed7v1eUWfEQeUSZpuhj7kEFsCOlZ1QL-eXj9w801Da0j8pD-tOl7s_l-8Od2paD-fk7IRsFiO-24kR_Opg4rYEUxEFRX8IlQ6surcDGycTtpwygXeicT_YP6U5SWZHzN8RWozw6MtHRCKTjQ0ucGMbyFDhA7Co8fLBwf0UDcRY5zgoalh9gHJ6XAZDegYr2j3CmLkWj7CiJN9qnIlNGbmrPe4lH-lD_Hm3xQ7dJX5dVxh32yOa-aDqfYecfznZHK-VyzS2s9N2cpTvAMtqEsPHfjVT1XBFcW6ggPD_WE8U523HlOaoHONxniO0ROGtYuVNgzit-NB2A7dehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=eWqum8Ed7v1eUWfEQeUSZpuhj7kEFsCOlZ1QL-eXj9w801Da0j8pD-tOl7s_l-8Od2paD-fk7IRsFiO-24kR_Opg4rYEUxEFRX8IlQ6surcDGycTtpwygXeicT_YP6U5SWZHzN8RWozw6MtHRCKTjQ0ucGMbyFDhA7Co8fLBwf0UDcRY5zgoalh9gHJ6XAZDegYr2j3CmLkWj7CiJN9qnIlNGbmrPe4lH-lD_Hm3xQ7dJX5dVxh32yOa-aDqfYecfznZHK-VyzS2s9N2cpTvAMtqEsPHfjVT1XBFcW6ggPD_WE8U523HlOaoHONxniO0ROGtYuVNgzit-NB2A7dehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvfm0EzxGbC9GO2CApXh0sxqvvChY1IdfIwHrWWa0vxKMkkjslCVVLPuFaNEpgFvvT-OfTy3TuW1J4EPs2NtFFJy6X_RoXGo-CKBSCwJyY6l7wecDup7_pjFJ5h8tnJ0KiK-c_UmaygXq79LIFC3Qa5xNcke70s33O465G2X9Wpp9qwQ_fJ3fqeMVkyDRhsbHRgLfbctTUhlcktOykufCFbIDw5gLjCRmrmzEH-lxNUoijDvybzTUJbdXgrUJghX3CA-cA0Oe9SVV2TJhDZgQf6P2yo5w5zQa46-LR9nv8YHoJEooKsUNMh_ZmSiV6bDdZMIeKCeTYpERVAmvN0VOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8p9ET-b4oIM8Ak-w9KItTkjZP2paZVatgGBaQ8DAdBar4NnyHDdydnuB6Ln-NriHTntvCRBnoXqhr0M3A7Ew1xrLoRZwBuuvv_aVADwnBny-duK9KMt7vemM5qlu_5iNxIYN3NCbT94hYm4ctDDa6gHtWhYKccav7AX7a0ZV80GcxyEGGEKzz6VyOfEmk3aw3aX4-GFFAXs9XYoLFN46W3A_r3JxvUAvnS_gz1jjf57nWqYU2FXU4dRgRnrvrjNAz5Hp2T_a2FwWl4A66t9fAOLNmJYrDDlfnLNzaLClk0dYXfmUpnKSgwfqr3Ju2jNpu4rZacNgp81263zTsiNDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gS-Y_m6W7L7AFf9xuIJlNDEcrdvs-KNCb7CRxRnygeS7Al7pABBbArEAGVw-JXo061Crk36Uddgc64uoyFQnq1Z4dvBhAjuq2iaCdWZ-fy3kgUGh7liBHFJAiatEcLpFDDKIXkdtRAifHXuoMdB8dBcjGnO72sVGRYtvBDRR_I_CDAUn3Kd2vtEfda1AQbIAE0mLSPQ4gJU_oXN6LYKpPG9JCvk5Kh700QzkVTf1YSrxeuxKVlOhVRlbWut7tXcOOZ3SJNBXnrrDa6z7adCKyMTIZiFAcJ3nmlQ8jHHEYxgT04huZT6aAs-1E_wXb5moIZHdYPyiT9OKeRlFvhcHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mq-ewULNBFK4Ch2n087D2-I8pRtR88fPszZ01vlFJz4DlKTh2IJ5G59pfoYae-mhGDt19oNx38l96tW3rQ1UbN25aBGxNML7k5zeX_WndCPFx73TteSGjci2o5U2MUMz6ODk6PJuvOnjmkc5HTAOJzxK6O5tZ1oJNjMSySkmt9da8kg9et2pY83NNVkLB9EOYKsF6j9IPzpB2A3BkZ8fkm5xw5zTzbA4xoQTCfiQ5eDacq6wFU2cC9W-APobg-J_MAbZ-qH-sfKBytq2sLcjCy_IZWJrSgtmoAcnGBVq0AyJz1rQRUHFNgmmaWoFwbdfFb6chUfaTcWa8nofFop1-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O81oWIYiQ9XWnoQuRw8fO0N1uT-pND0oirUQvFNLeEI93rQ5d1R7mxj4JYp2ZWElGIF9vJBedbyIWJXT8wlo32kalkJ5xp32oK-lem5BUGw9bgTmsvBfbWZrlp8M1kRe8N6tBVnbZHE88MIhs3kCg3sH48reGU7VUBTfoSDEmMq9nsJ1pXkzek0F4EUTMHFyWeNK-TVRC4my1O4TbERjsrAW0wo18tDoPZ7ljHvYb5pL00IwMeyrGetByS40tTZoeGZjfStNm12Jb3P53uzVCvqjFUmqtRyk5fLucuj5_OC3pL15HVR-DA_oCKWjMzFlD7jJPVyUzS7tEmjkHHUg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIMyOoeTnmwQAsdHDtKSjf-g3dFEddc7nbrgZSjIQirlMSeXO7gpn51Qhs1FgpMSclGrTHP-H_EFhMdAbPiPY7wQsbcmu_AqiB6lBQmgiAw4bzdUkMvp8vqJ7ycetAU6vodEqFCiK9zIA9fEU9hWoFa9rOhtWCeGswYtz_sYWSIySE6pzKNqe17sqQOc3Cf92Kakna7uz_j2-Eanv98JRfe5S9mkUEV1JZcGBrV8f1lW2a5nq2D4z9VxyPeqAHXs2HGyFmPs638E5XZtQrnPfetyd8IdHiK6tLlb3FqVw2TH5pCnE-5qSdbZiY4rnZZdAKqPoQ91ij3macbG4XHzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiITIl_OniwORnD9ZhHYQm5eBBbkrexRnoHlVN-97pWdz1oczsSScxoO2FtmaSxzyYKMPgp5w7O6gO150IYO_NxN6WEzFr9pAYWa6WJTzrJyDwWOg6NW-J1w1SUPXLGy-21V0V2sGkiQHq0AifkP97g2Xts8DJWLBUZtQlcYYKYH2tacH9cRrm1_3VLWpGyiTIF4LbT9nDRpQZVS_VAiOtl2wpCpPZkqzbH39hL7MKQ4IsEJxk8DeqVwNPTSCyVVZIoky7u7yUTjm9HpxkB9tOq7f9Di_5zsQhFgvf8geXjwkL7WiHKPGeVo2Szwn36SQ6CZ3nxsyQJd8icq55WECQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=HXj5Ish2SCCl6_TIbciwsTFMG3lCWgR8QajScMBFMbbkLUBj5K01rZ0xsGV32ZjiUJIBbEZzT2TaT4gjncJEAdHM8Nc3qK3cJsJOWkMfhKC-NLA-SKco1_wVhNWDJxK1MwQNTl4PCJa2xsxH9LuPGJZxubsS7xy6SW4mgD0UiI7xoMtC6ggihtwdalq3E5vaPnVdWd4DGF0uUA3ZvN7Q5TFp7avwTVs9JLfN0lgjnlsT-tRkhtEOWZJ0HOaywHIsjGVFtiYuoLFbFqrrsBErxTNSgW-eoUWUH2Z3LErdwDUtc4Jy54FfqiuxoBsnixA7RP7tnyC7SIiiR4eAROGBF24Z-ajv8SAEbH-34n_VtmXwDlxkbLKw4gxE57lwBGST44wTBKkd3a5kxwlDgIKmkIxSi29Q5wg6sJ-JqXRWAnl6Cw7R-qMnVzasbO_D_VbC7jUYt3GepxOamA6GrYExTtM1fvFNGmdpDQIPW00oGvK5osX4vJj4_AbAph1H5scPqcjpo5KR7LLXdiRdWy3epNY3bXOYb-ny6B-eFxZxw7nx-IXmLgQYm5mUtSAyukkn1Py4_0TlZuC-WBYk2_gI5XRFdPlfaUn5LC0bNOnzWl354YwaA_1R0ZaTc72PeNrYSSUBbawPw2-WqJOwxehf65DCKQ5-PsA11Nf8P7pg0R4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=HXj5Ish2SCCl6_TIbciwsTFMG3lCWgR8QajScMBFMbbkLUBj5K01rZ0xsGV32ZjiUJIBbEZzT2TaT4gjncJEAdHM8Nc3qK3cJsJOWkMfhKC-NLA-SKco1_wVhNWDJxK1MwQNTl4PCJa2xsxH9LuPGJZxubsS7xy6SW4mgD0UiI7xoMtC6ggihtwdalq3E5vaPnVdWd4DGF0uUA3ZvN7Q5TFp7avwTVs9JLfN0lgjnlsT-tRkhtEOWZJ0HOaywHIsjGVFtiYuoLFbFqrrsBErxTNSgW-eoUWUH2Z3LErdwDUtc4Jy54FfqiuxoBsnixA7RP7tnyC7SIiiR4eAROGBF24Z-ajv8SAEbH-34n_VtmXwDlxkbLKw4gxE57lwBGST44wTBKkd3a5kxwlDgIKmkIxSi29Q5wg6sJ-JqXRWAnl6Cw7R-qMnVzasbO_D_VbC7jUYt3GepxOamA6GrYExTtM1fvFNGmdpDQIPW00oGvK5osX4vJj4_AbAph1H5scPqcjpo5KR7LLXdiRdWy3epNY3bXOYb-ny6B-eFxZxw7nx-IXmLgQYm5mUtSAyukkn1Py4_0TlZuC-WBYk2_gI5XRFdPlfaUn5LC0bNOnzWl354YwaA_1R0ZaTc72PeNrYSSUBbawPw2-WqJOwxehf65DCKQ5-PsA11Nf8P7pg0R4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcwmTzoOzvj-Xlx7vM2GPZ5dAiReeND463jVESF3aZKbw9re0C21bUhfZtKqBFMpM-O__nxOPsLhq72WGeqQOeej2fiAA0Jy5UbY_WiVvmBot9KYYiUg-oEBYPK566S1H9guaJU4kYn4CdaT2Gqxa24DaE9Sk-Cog93b9UaEvYIiqWHipsqxf1YzuCzpjZ56ac6FMuWr7ngxzvwMr6Kgna20wU2lYlLnA8WjFoJYTTNwPFhCxB0UpjeXDGTSufXRK7Fsa_YQQfaAK20RX0fcPEBZ5ho8YxjOx9Wp339FES7RGP4WtnO5Mj5mHa7eD61--CISj4G4uysRBSv0bMMCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apZBVGB0KEKWFivZ7JoEBpib8_iNZcRt3a78Fqm_SsdQvIK1cXNKiR7DTsAeUjrBB-Rjle_70XElniuxddwBn5OT2C-_H7UPjti9Mm4ro7lqIgVt68iWPOcZvK6DVlAUsIpzwCBnAW6UKn6Zu4Fk-vAJV9flmWPssv04ZgrfaI1lqu0OdSVhF__yGQbdAvrmHlGXuF7es0M50oy0DyjzaTcuX23TiFexRrUJbzVWV-mlzNhf_Rsa3OUJTN51BzQcJx6QBqEMtDmYjlOaBrOWje0oO7DjJplcQ-2O3EWpI6iopWTRQNA6BereNXklE8Am3Dr-TRaNRYQWFoiOyDlQDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_tDvKU-DcMbMFa1teeBK0f7DzNhTVd_SI1O1wvWKBfHKX951SvwuIWzdfl15NZ57PkpdI3_lI2uFWCH1MPZSuuEbHiPYp24uafmVIvYliBoAS0wdIF_xWtZRqvOl1zxxRUVXpkMiHIS4aQWof74kCp7tTNegQ1pFSCGcYTl8Xt9wpyv1RkfPjrRXcXAQ9_d_b85rZmZaMj3qbl1Rh0GMV63miMXvCyFddOfDewDMeutxLO11jniqKcqsx8ukkSvz3Hr4vktX3w2sKQ4IPh8q0VIr5PDaUtfb8D9CUBu1wu2PSCP_Y-XMl4yavXs9YVsdtRypC2Coe2qShlnqewmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYoJD6uM0zSvW4Z5XWHqanvAE4BlltvFIvmxXY1LH-_gQt5l8bNxJmry50ScEx-96yM2nqKStd1KqdljHJfJqWbkaJUMkgZsR0y4lxaqdKpYxtZ-mQ4kLQ-mHC2o26IGUY533q734hE4W9YNXMy8nhN1HkyAUmqfRpqzTLoxKa1AeSjijVKfbzlYW0w58S5U89K2EfVY02gVpOOolYIOdSSq_g2SlKsXy7YAnV6yU_nGfxXsmt7m_R7Z30o_AULpT8wouj0HQdkbrEfh6bCRfG6PULuVVTi0USm18bUgwHen35TeE2QqmGoBeTOQrDe7lwqG6H2SG_KzDWhpSMgvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bklh44bzmUWLCmDD6YcV3BoZBay8anQc64DFyzxVhaKa3rJVPGwO3ZGNuLW1rMw-0zifsp6BrGprAjft6_0PVw-78eDhFvw4dBe_Nl2fB9Lz5ST6pdchzNrSFElWk4rs02wRM_-IKyamKrW_5N_0peiH6NDfjSby4gtmvF7bYKi7uhJeiXqF518PODONH2_h5CYQmqSdPIbtH9myD-sBmQc4XM5HWOcGQrgIpEYGd6G7_nuJjCPLYFpePaHKu6hRF1-brY3IMXetCldyIpkctFZ9DHkHY1b5dm0-3Daa69IxsKQUOg699o-kc7t2ZSvh0P0ZFQn9HEI3FTI0BC8bvA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RSTIiGh2_PbAGyMUckiNiu0kGVThfZMSrXaXo1BZi3PZ0UbfBlQQtBVM9H85kst744C5ohwZn4Xcw5OPlDTcUs04fPN6UOGAcmKZCmMFMBt0qKqYMuQW8fT0L5JBbPr36HjMMY8obmArUO7dQu6SIsNaU_me66SSBblseZHk7tPjIwhJfmt2HfTxT2mEbUGrdagPlCKMoEFqT73OlRnmDBLDbZ3a7NilUNMhZ1C4LNGFP4X0VBGik58UTux7EZIqQFDFYJNmyILLQ7Y5GVFUnBodQW-AMMedmAgmZVj374GP14JCqU8itCd2G5NVOrX9Kpjtszu8qHGdJSDRq9ZSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RSTIiGh2_PbAGyMUckiNiu0kGVThfZMSrXaXo1BZi3PZ0UbfBlQQtBVM9H85kst744C5ohwZn4Xcw5OPlDTcUs04fPN6UOGAcmKZCmMFMBt0qKqYMuQW8fT0L5JBbPr36HjMMY8obmArUO7dQu6SIsNaU_me66SSBblseZHk7tPjIwhJfmt2HfTxT2mEbUGrdagPlCKMoEFqT73OlRnmDBLDbZ3a7NilUNMhZ1C4LNGFP4X0VBGik58UTux7EZIqQFDFYJNmyILLQ7Y5GVFUnBodQW-AMMedmAgmZVj374GP14JCqU8itCd2G5NVOrX9Kpjtszu8qHGdJSDRq9ZSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfwe8V0IIP5mUyAI4Qz4Cqz4bFailiMptc9_3kNVX-f-IjwEFiFO2M0-F2v_AX-bCTzO2znvn6WJS1ggz4jdughFXLkUQG91NajKBOHzH8dtAeIN6mp0Hf9asj_S74DYu7rh6DM4D-ulZZqejv0I_b17OZ9Co0JAlhSfJh-LUVEu5vtAGs0C-Y1ZJjfHNtLXcYSGqJuOL_cUbzcyQOP1MICDdHT3f-qvUBUGz7AHGX1AwFl33CEVOZRkRykUsKb9HfMhuW-1KZOgSF5y9z1kZETFyDCeGBqzEE1yNYbdrOqmNB_nKNOSU_Uwr6uFur7pvLbuOmmFS24KGW5Ai5U-xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u90RcznKwS1PFcf0YmXkDFDiiVkendDTMsl-onM2OOH5NeyeSIMNiJU3RqWqVItzBOUfT-UNClZO6m9DfXvzxdPreR3TimrFzGGY2yxkuPau9p9lUlZazoNrJY_WTEehlEqvLjfF08rpBkfRTAcpqY-D9Dh8SAdEVw490MWAjQ2mV2ZJD-upnj1UmVTNOFAhTnM6cRi20Sl6u4NtdpgzmZWQ7B8UIDBUaEOxykdtaUJQWnAXzjaOZsScs5_M1O-m0U1rjT9jsvyraqox_V_d-IDyj1No9Y3wqJiVb6BymygciHrcNmgi8y9Z16_phGmKvZmk-dFq5HnKHfLM7Gldbg.jpg" alt="photo" loading="lazy"/></div>
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
