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
<img src="https://cdn4.telesco.pe/file/FHUMUlyYWDYH8otrlqh6BmT0UsBbThU3HeWZgdja3u2wW0ieLKsBMe09YreHLbPj2q7zY7HA1jcsXoWhZMiH-LyKZa9ewIixmrMox1xfF4NVSMLnaZ3zJLYC1Hd1na3HxBEXUcKZd_3M29sJ1XRxvBS0WzkvjQHOYdARnWH4gBPKWjGTFBN_OVjiPySs8GsYtTT2-fUT12LyFlB3CZ2Brk7O_XSk8bHa2tPW4r6h5BehSwWkDYGfydMA1NcmFKm9DCmqHCrLQPPK44e4yOk7Cy43SCKBPLo81GEVJUpsh-SwqYMzFOddabW4wJAfC6GggtwefvjwK2pQ0HqkcJxGDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxFfW0kQudAIZzdRxQD0fukaaZN-ceG94X0UWpOuz1xKx4LX0k6EQ86spDBaPYiSf2NMBoVFoAY30lN6u34k8OoueHYF8f-O271iCEj8EtPWyEPAiqD1JuPxXWpKJzpXpSwjUd97g-Dw0sMEX-QAmuQF3qgwiwTzsAX8d8LxtU8G7wCmoCBDrGY5kGyTinbej2J9Pp1r7l5K5Db_T2ZbN9hl61LpRq3VhDEyA0Infcz-hHcya8jHe-vFoL9gWJ7pwhFnLVBV8rAW1kWKa4w3eXQL8nYTcJjRJ6_Ehf-8bHutFWH88S4ZXL2A7wHjw5kW2-Sm_3pwa4KyTdY_ELFKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 264 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 496 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 631 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKYTzXbRGMCTQzvHaBMRoBTpEmgHiwjb31zwoXM0hhTF1RXdLSm2IClMjQtFzi1BqymaxuP4_4jjgPVGug1MGrGSbKXTFlU7gDUh1qHhb5x35FCuXP-g3uU3se828IcZ3_5LVkRfk6a-HW5oCX96-3U6HIK8F_Sl95b92kRgDhaRygVG3QEGJC6ULtNr2HfyVvqYgcTpsj-Q8Izk-iHABk99CP9Hi75m6fVQMZMiuIccc8GdJ2u8D-iDeq4VITHqYmK24gm_8MRxsBrM7RxFGgqM8LwK5jcCHki0tbWVUikJtRz9fOISpZqFGyqmgZmFtNdWlxaSrfO1fXm2ZTRj-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbYWxU-dYYduAU1CWfctVg6A1PxxkBVAswa1ZAoj5vp-5SRgaLO9j9Rhx9_CvNUEuoU8Ft5Xcxwb22eGAIdBPlX3j3LdjPvbHv6XoRYmJsT_26iMsyHbAnpFw_0qDj9PKLbiwjDrblGHCOJmQBftj8FrV5ncfxmeTvFp7J3BlG-i9mXjab6hl1rNauLYsbVkFzHJEzqSwBlQ2QXldhH68EzcxaaTV44V5gg94kAmHk3MhjdgNz70LXqWYwJH5xlfpQdk-y2ty-1wjuCsuNU9J-xYJ3nOv3tMh7-H92-2ubIn5BxmFENINVlMUyFtr5u-qtjOoTn8yYsdPUBjvInTuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GShWlGiZCxNE32FxJRrsIeL4fKKN2YN3I7VIxCrvDy9KXFHmyALQAFfjkCu6wKXdP5ZHMeFXCzucVIpYaeESlJvY_A8G7xk44mGb2-Ti9GWDHcOM1pTT4kmGgVv2msU4ha3EeHrzHOTsGBu46JtdRda9uRe1ZFADTO_nJRJB3CNTfM8RKzGwLnWmlIpg769Qu3kv6rKawu-LpFsWG8EBPfH--XTAeTeJ1XMdz8EyfzD90Ip6licMcoOg-vGWjT5o5cVD7aYTtxvDfzqzJsOXOT0R8ZBaOqZFXgRPUSLn5Kgu2V9r1F2G8F34v-pWyVQI8uI9WRo8sPdx4Nr2CdqFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyKJJcPu8-vhtGsGvRSU29-Gk1SNptMTyZ0CvTitMNvUGwlvw1DQrMAWHDnJ-A3VLF32x4EGVWXuIQBFnh57OqgNJABA2X_ycAKx4zjfuAZRg6H6r13EBbGQ4hllynhwklVtp-EuYlktqH2gYeNkoF0Gqo1_o8MqTFvE1aap7DINwcZ0Ge6b8aIiYe2FnE32DvAm9gLXZPlw6vgqCgLg64izhqPpQbfHIhwk9MfFP503UCND0hHdygyroo2b4-LshF8c2t_iKTO2RgHwEG6IPc2YKe4AmWpYHFctwB2xEUO1NxIZz5LsHM25bgnXAlsiQRlGbdeYsLoso3H7OgPRAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux0JUN9sPegcTT75sezjJoNaW2GX_71qsdavxpQ64YaBsXPqmFTOFvwzDrXqjUuNRRNNkrJXNrSLalSZA6skFmfqcRTs2HoFbluQBLlYJbyA6J5c1YJRxfYunGrv6BwkdEcJqBIRjPFk7ZyI_w7sQU97CDn9nViA1T_wbRPb5z2hRAwVC4ufQHMVLHV3P0h4qERu5g8Srpt7FIXjgJSZ-W4isAuLNuNXfdYd_1unftULqNckoPwP1kF29uuKB1-OQFo1DHLyelywkPtLiwHxEeQ6wujkvFFwonqIPfbgBHp2b0JuXPKeC1o7d5R0ov71LfRMMkJqSYqhDThmU56hRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu0kMMMTUR9OcJQ64uUNw93DNwOzor0CFpc4qQYVdHtZnoUHDM8qtWfcyICbvSIN5KdDRjLVLkSFldoNy0XDQqc-sQ9D-gWUAxp_APrcFvTuZ8bHxYIEahYf8tdILrT3AhsqoSd0ycll1ZkhnhDaRFRj6MJloGEMdUmpD_76vIiiRnNvZ8mzyksZZd0ZpkYHd5Z2z6Xyln2zq9ZgoiZt94SxyrE4z_HIblXfQk9XHsVtcZiq4WJasqYgkt-byf4URlrAx8AhpKOJy3bzluJDRbAzCbqB1ObM1jYjTVdx68PCQcaKUaccf6mpPc2Dj7q3_qrYun-MrzcfVxzBzd41gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBjW7An6kHoJbjYQjSK-nH8S4TxSskIUpOWoxUjPEdjY8vbqNJR8beSNhSSQrPDm35LpAfyj6b-D12ephCCYN91rALqA7N7TLC3_BgNBEMwlYHspfDx_uqPjxS7kaWywaHN2QmP6OP7DavX05Pb3RbdVwlqBOzdGRIKSZmH5ZOB0IlYc7qQfJT89mmliSfYwdDB1TwBGVc34cxVF-2ktSIipWZY799XL7yn2UGAz7KxiRYfUoWDCr_zlWB-JLvay6lchyC7iiWJZLMPky1LX9bqPYnbtCgOEqIu3UXHsU6qYiZuEVp3xXFlgLeQDSkgjd4K0t6NWMFfjOxDyMR18eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyij2hlUZAc0NOO9i1fuYlwEbEqRrF_A1oMtqfXswRrTuXX3hGv593alstiaZ07hbHO4bBdljrhvTt2p5yTLs6zz1n8CeirviD0ZLUqY_JTASM2i3kk0VegCk2WT0jrjYgPDesnZc8JbvC6yFsc4KHpDYGUy3yxGj901o8GEqQ05h2VmU0MwKbdCeliz7XN9E3w20f99-MtKJHkjyFbFuuzJJDdHt7_UI0gSiqsnt23IjUMXrRPuj7byvy4gF_13VU4mBE-tT37oo0V2A83GQlrzogISIooGXUcAhpB_Ul0CocEw_uyRb52ngd-abZ8L6UzC7JGThuIPWdkQtktOpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okHFjEzUbX46ykFExk3O4POIUfHworxqLHP39KN0Fo0OLNS2ggH1u0HbQ-1MBqhOtZzWI4qcESKaZa5sF-tMpGah1frCPQtPC-EZcdM-NA1zERYuMIfpNRup3B9VFTmTICaOwFzO-AYDdZW66wm2HMdbaafeWYoNS6wf_A80-jasyCsrJKoUgkZq3l9T542WlgZHBTPWpcgP4PF3WmGIn_bUjlQOIqdMnGh81yFuA1WlkTq7pHvRjP_hl2-ZorYylwOgv892s7coRFozFQ-fNxYqsnFsxbb-9xY_FEog3d0Kt1yGSqQJ8aswqhjIbbHIeHTlbtLRjoLKX26Sou9YZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NueZLfnNOsQ0LskY1AVMU4KhvADWcqIufvPCMGyD-osRpB1_dsofv3p1x_w5eQ0WgQHRG9ql1QuVuX0Kzyl5CyWcHZg5Zih1oAKrub5MBIMxTx5YqZ1OBhpuV2CCiFVx_6OL3HH2Mj1QfGn1k2D6Ea50K0pqIT6Ze21u7LzBl72U_SE_5JPJ_VKfFi1RUlVpHq7l6waICI_0b_NdqHIJ86IPb4jCs3fCU3wZWe8zGxtURck8imutlER_CdsRY9VgX5lXhxy-6wOEEVktxkhAf304DmZpiF3UZkMerm2QPBX_rBqCgO699bXu0h1pzrAGyyooHHJgujHu_aiv4mu7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlwFgDf31Knaa01FSK4AH12MQ9aacVKi8xcJKzufM9TZNx6XyByWIwxNaXCCMHvWRvKXgXiowKQTXiGDntttTmO79iYZEsLYWTIzPyAwu33nrnPLmDblChM6fS9WLAfFIJG05d9RbsMtuncs5iUU-6difEqwn32lONyB0atofJYDN2uAi3WrQLidkas1TjoQ6hRMSDp6hzeriddBdl0M61grvgA_rNAj0zCpq9VyosmfiEVoJfpSjFSIeeAJYpgpVYOqiMU015-14plo8glIvOYaHpjpx66Or468jb1_e7Zcmr4Wm-WBfBKyMWmwf6a6Nz24UoTCGmGYrDTk0ZeSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZxnz-_MGkw-GTDkYRrYqXgvehWnfhWnBajSPBgHso4LVA3xERlh3jZRhxWde1ERbKMwo9VGF3hotnF9asxx5NbV7Qcu2qa4JYp06DG_8DWvIQ6k1Rqe-K6qluFkmMybaHcEr344G7EgHyVkTabXrrnlT8-dOBDYm_0umSf4fLZs2Qt-SAtiLTHBhJ_vDWll-LRA1OPOKyXfMXwVopXofMXMJiN0RS6UY4amoNup4bROWlXrum3hSZACvRkEUtE_5RK8cQ_gF9MoE5OjBGIoMK7KuV9kYtadKavpsswIWqpvS88OTxDGo8iznawH3sePL4jg3cizUL9FhNaJ4-Datg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjPUaDmHwjr8BF6dB2Jv6hiAaEBvCet8XYiS8eFrRQpCGPKS4y9k1jZvu9PmkTd6PwZaZJKLwH4KKLqeaQyy74XcZJRslMMgLlHYspyYEsjhvbg3VoT9TTOzmnd_St52aINb53dh2eUuFUHHoVxEynMshaKH1QNq6z8WJko8W_098tUhURU9V80UNNEhuxFArDPBkETbfkI8QzJb2ocfOvLm95dLX_dNmAIajAS89TSiuPURTQVE8y38XuSRLjOVZeC0zAFT72Kf_P0vICqvkpdr3jAzJwcDaHSwgKLVL5UYgD58N43knYw9pJ4ypjIfhzGvUzz5e0K7pvLaGDJbBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tDeoORL-is3TYt4HNZ9tPbXlScUfpkrnZaPjsXgMsBR2Xc7aor7fha-oY0HRkujkZmp8d936QVobLV_4m_WVrvbZwhLbWjJMnAshWSX-_sqDVPYpWVjJyPN49KWT6yL1t0-a--yc_ApnrfGsiFw0BEWorUjiyLESGbu-fv-9Kpu-GgmUgSd1HvOpRSzsH5V95kTnWB2nWi7It01nRDfCL_zYmpESbiaaO9tyVKQuiCAoayxqj6PYkVRj-Vo6PmhFosfN--7cEeo18n0mjpp2Kj9IAIca0KeqNBVuCb-0dvzqxTytYWTDVVBvyBkytqE1rl1LUWkeZ2l0tjocjHmIRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tDeoORL-is3TYt4HNZ9tPbXlScUfpkrnZaPjsXgMsBR2Xc7aor7fha-oY0HRkujkZmp8d936QVobLV_4m_WVrvbZwhLbWjJMnAshWSX-_sqDVPYpWVjJyPN49KWT6yL1t0-a--yc_ApnrfGsiFw0BEWorUjiyLESGbu-fv-9Kpu-GgmUgSd1HvOpRSzsH5V95kTnWB2nWi7It01nRDfCL_zYmpESbiaaO9tyVKQuiCAoayxqj6PYkVRj-Vo6PmhFosfN--7cEeo18n0mjpp2Kj9IAIca0KeqNBVuCb-0dvzqxTytYWTDVVBvyBkytqE1rl1LUWkeZ2l0tjocjHmIRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBqn7Lcwti-oqfTTK1AehGbaRRZ8qC0hnaM3PfuXi9jDwVhP3rNqAMivLR6V7rkwvPNgzBbCXFCiGJaLWPnz3R0kQL18yvFge29IyPwFmXwy7qVNmDm4_qyWOCF6NDLJY76XGHyg0BpzUJI-w0PGBwLhRBxiHdtg9fK1QZ1yAycjCm_22JxURATUj7fKrVgEEiduJ7e-fdeUYg8-OKUBiHV7wipILV4M2kAuDKj8foeBvnmpvbtwF_RwRamviZEIJKknjZlS5Kb3d6GM_sWxVB7nW2aSJCP7uoeS03OvWB1VMM2ev2h45AsJLzBMzyPqg7q6-3b_4EmBbZummQZaPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYlTm9KxSZxb5fG_HrUhZcK-OCUmeV55op5PQ1LdbOO-HUWEmmTGS7A54T-ra7xeQo1h_qPykKj3ME2rJsJYMF-iILhahSE-6mFUnBGgoxkGpDSyCa0NcKLiTsqncbCcvVe-W1q3X3OwBYz_Zbd5p4vepi6wCMws4McBDgUXW-W8au38-KL_ruuLq3dY2ThMDX-O-QgIvK0Xwx1q8uG4_BxcAKUqPZKJ1nD0gBchwlZzsGzZXyXaMmjHeUbwyMPbmTi98ohsJfsxP3rauRwrd22p0t9Y-Z-EPHU8l32Un0vS9vFdm_fSADqMr-auUtddRYqGH9LCw3rWZpbxdWmfUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC3QJ5Z0bzND60B0qrARN5-R63C56zFQV-srzZI1hZpPUc6ohJtqPLrwUIL2qwK4SEbBPgEBRlpX5SaS8nNiC2vkyoRrLlysQ2tOh2JH66vw0Jp71k65DUoC1EXzR-G-7vUYVdbLyrIrA1XHhXUK1ILMQmiwiq6GaXl66Y5RuPqxGYyEjW80bfDu8pDXAfsO_YgmRwT3qwXehXWBluFykfyQ1tThz_oBOrfidSjQaKt-PqTGeIMN111oS86-7Zu8GhPNv2xO5MbWvT0cE74z9RUsa_nXwt7PVD9YLBfSrx-E6GZQ50FlsGfoHpoYRO_DQ-rm6P2NPX2kANTna976-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVpPR2Mkz1BNZEQuakktxLmNqWntzXyXCRTLZGagV5R1fQUoJPoGwDorYrUxr5atxPNLBkah-fasooKd4HONdAYhwI9Eg_ZGWKCND3BeP1LopO-o465xTLCqeIVGGNrsW5Zx1bbBvMSQgrzGWFvNzLq9Ph8OoFJwFqCRtfDx7Legneer7dxWrHVwgW7N2CiizrzVQCmMSR8RL-tBRwaWGErnOrVB_4NRX1rMdD2ZDZxc4faVvZkidWiX_0crVgbtUqq0OMhTIWq-4WBqTCLJZgVdvX_fOFu3tNuZl2KIapWj3BcDBW6OhrxSP-VG4pkob-4L8GbVto7ciAcHB1Mh3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjqVOyzWoEcFFcth_m0dpFyST8sXnms8LLebAR0t7zJJcwQ3YFDxgVTHP6giJCXImMonL9IAOWD-CwV23ljehEHxy5OEU9esvSe6PkOYaue1WKe-Aptbl-l9-lXhLZ53CvS8MnZ1cXRfiWN8r_FFvSPHqQoChuNjhoJTBYFSVYltmRAO5mtSZ78DDxgiyZ0uc3Z6wU8z7XK3uGXAK6YUBV7YjFj7erggJa9P6cTxkbXrkg0SN0ikcbEskj9cn8O_C2ANZo6pJVPimFB43PoQLrti9BkchEvU6Tct8W4sX-3D_vchD4fppUvENZoa-0rbdzLgUmMkGnFBX-ejD8C3qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCzXlxiCUdMT24DwMSrZ0_Bb2YjV04r24vd1j17hPBoOFXBPHnxa0q2g1jTi9u_OLwHE6weRXDlzHCexgSW6-2bWqrHkNOc87pkbrkGuwWc9qIAVqWx_FV138bDAymuAF5UR13L5xnfvw_N7ZxH_Yrudy3OgRmcmR_FbQYehS5ZrpCIXk1R7LcWAx33zeJHXaPMkIj90VAIQ4YapI9TPvFp4N-9iLt5mH5V5hgI52fPWVsqelD4sqik_BO6w1JbbUZUr9JBic8ZZXfw6_NI4FkmnL4VAqsVJQHtCYLeYq5l-DKW9yI_RhaFfYtsKiEpeA2C1LPnNBM-8Vw2m13pU0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ri8b-kOSTWNcjpWD1qZEaJC1VySQhjIneVkQBCA7J13YqKQaNGGjNGytfwognYINq-BK5pZIDM0TvTsxaLOYEdxIVipZCkYD84ZtJ6N9gsPCwlFG_bJR9lNiYZcEapklsarrki_ZE7xZjS5u5wNAZTzNegha4aPCDnyhI34KtxapayZl9-npwYg-0lv0m1FGrIyoNxAUod8dB95ikwJj-vIyiSUvOsr3QJ-kpa2U4jv2BnKmWRbWDCgtT4Dr4Ovh4Ptn9e-GN42LPoGNTF9-aodWRHxu8KGDIkQz6h_1Qa51waBM9ipe6mCWEQKiJe41JOrFmUbExZgLHSuqyDX2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB3CgH6FlpQTIt1ruyEogdPkB4sVTs9VKZjzjFvMqjrWvnszI94aZfcao_y1w3gFT7wa3zk-_gYFtNc6krbSBVcTR8cnRusfgi9CuadS_rc8a_SoBMt7f2N3LhE0CfCeAmVapwz_e3hRfoKyK0SxYjLVLyjy36URzegEcmA1281k1FLliIUW8kmJuIOSaDkYUfvj4F9oYarzZOTdcjcCxCEk5yD-wIz4NPBPi_U3IpTy11sWt0S74a49VI1TY4-uJ8KT0rGcTb0dYHG7go4bq0o27KeNDY-CrFrlEo8T630aW1ENnI-jzadJKPIqmraf1WKrK-Ket7EubCwy0IJVRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNhJKQyNflExyU9qk3gTMUuOGA7OamFsu5p-dw7F0mU0Rqw6B4_rbNR5U74hBhFjaDzWl9Pe0EZ47vKW7QYP7QzoH99-jXMxYgowA_FW1x0qAa-hNJQTN4xiozlAFtphV3f7koHfoakjqtxiZrlGxR7KvyYen--b4kkao7GSQZPaBa6QB1-6cdBwfVH-W_dy5vxM6-Uk_7oXvfSB07FmAa_7i0c1YiOMKrW_qI0uGqOvXi5UyZSZHKuf6x1ZSUx7Lk2RemQ8SMqLSYZmTIHy4uiwKr92IWJf1lC2NzYRwN_Zh246m9PxFfaISj9asXZHWFlaxrUc7D2DQ-mZvOnGlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q49iVHE2BsnZr9Wy9Xq5Fm0eDBy8zBLMKME-mupVnDlLPjVomt9kp4Mge-NfKrOC4nTfwR-MhlG5DCny_1UVIBO_VGFJwdO7StGxxlRA9gy90_Z28naByLW4CVkIp_PrQi5P3kK4H9Ln5jbydtUWMW7gwSWr1cRVwLQ10pHaomT7Rw4za-XLeCT5FuFALCF16KI2R64NggGTzJfRZDrrhje9ph_DKd-7rPrBFTuJQD5vYi6lZNwpK5j1-VN3aUuwj4hGpvjC00qybzYBcTl3K8d6LvR7qWG2oMO6MB_fxKdZGzB_h4DZZlzxw4ghijotzYLqEJPto8RCS2cw6MM7_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUl0BfOC7D9FWBRVv3cDsXQkYbs-hbxFePmLJOVYVeUgeyOWylxUMYz_2I5b8c215EdKbWowhnmSPoKvYJkd_8qXlYMiRERiOuceUo13I0Ox-usSqs0EBvFCj5sLtbBGGbYUJH5v92DkDLTQZsfQRN0dYImOVwRJGCkJEnuVzNzif9EsItiMBd2js66elSYCYEAIJLZoBVEWkzun00o5DYw1vthdKHQGX54dwcG3WTwBOUsvmIEzWI147-tJwdJX76I4jC6rkcrErmtlV0YwOSFkKYNNCk8fyqPAAQrcQnpUv5lY9IM85QBf499kx8tHh_6Hw5AkI569fftBdtqp1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-IhSC1eUpXSfi8wHyhjG6tIXkZt2LUIJHdb1e6sRmKPYPW16qRwmZhZntXif9y8UcLnz0pVe86nhZnoaxRtq-eGTPrGKGN767TUvj8Dr3MiMwP8ww_tR6H8JsUPa_vKG1QCNOqdR2iLgLzuhH_0bEad1-16NFIzfEpjE02TODCC2dD3hXjELCYM_mU7IcU4IEe89vVi5eNmG7PLfvttlCVYeDcszj3rw2u_BRcGsyNQ_a4t1x6Vf1pzNZmmC3m0hwe81x9Nn06-YaQbJajYhswd_lOGh3ksTjxE2niXSBoTlFpCMyUgjFjQpYxoGYJscoYDwOqiGvil1HZLUqDvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf2fb4SKMBKvR4P-7kZxtaTRgPZq4rzX2PiXnMi8c6rvG13nb2xdbo2r-5XaZnjvh0ww_ZCeWcJjtn44prJTRhWI1h1WcsZ_gfO6M9SKEVJroA8bmCQQ_p1ZmGFtoeohUzyTgHt5xwKshGzV48G128uzyzORqwhzfbFcdluN-Q4UDVaXaVxzfm2df5dF8spWXU_Q6UpkrTezdt2IYjQTyBPchZk3SSe8YHLgT3eHAIb-e3HSAVB0E87SjbwQyuP_F-ZXukyp4-QYiprQ6ybJzxYRhtALPHRL7KWzwQg7UORiiVCpU3FjZYdN1N2G01m3n7yTZL27-aG3rLxv3OODXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9BVxMtrclXF2R59L7aG8yo61Cf7F16UZTf8wfXi9dGBdpZFN22y-oMa0h2-1bnGcX3V9kDU6RwPIUeY5OBTgtU0Tz0L5_MHZoUw00dnc-UaqIoNHsNC14oIIIS7uVdo8MgP0aEAwUZaXcwABrYZ-zombf6YLvxWA3ynRpUm_8qxT0_Rn-_vmydjouGcAKCH5UXuMprcagkNdL4o6fhd6NS3QhtRdUfW1_wx9U4FaJIrtBeMrDpopCinqb5-yuXTUEuaBoQf0RGLLi4MlW6UYXBQCGGu8Cs-mQhOSkm0gHvLbpdAjA2UpI5nd6IaHq92-L9O8353sCRffz5BL_pRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOKRZQ2qe6uot5ZH5jBordHKJzdb_sqoKXtTdWxiHWExeXq48z0xPmFrYfN6w4YnqScWzCE2SPhUTNWqepyx6PlIGb31buZRvy2LhwrKx8M76VDxFRFt8VzkKSllFqM6O5wsw58FnHpq50i6FybcNmeWNYoXPzOPjxnTaZ7nwPhJidUXoteCLgmC3dA5czAsSEL7qsFTh4_mahI8vc7xMYxc2NZveVAb-GESu1MTIybpicYOWj0MvVAE3mEvxrQRELXc5yn8Y-hguvM0TqTnN6bZG-ojkLAiGmyt0gwHcNUbe-1io_neF926J60njoe99ii9MuE1Q87yJ7j5sF7AEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlLVLm5xPs65i8lZdZtkl7aEk1FQFf3Pq9Uu6oE93YGX3vvDOFHEudUu-I2yzv002sCewTjJ-0_STaMqWIKn2Wmy6YEjb0ecE1C21pBEmscX7rnyijy2vwRNkdKLyd_EsGUAgOyBrW_IV16hL1S66uJh-9J8xxj6fdwwRo-G057b20PQerDpQC6NC7i9i8TxvfEYUM2TN-quilxMsaAGeI4lOxRz8Z_j3SeIxv3CwxJpMLbABmgxYcMFhw-YZygjqtd0S_DtgarqMUGGgJEiFgpeCcmkwB9ayZBL8UYaVvgrS20RU2ZSLLQe97bhxPeBzp-JsWecOqfD6kBLWHN9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVOFmLU6-Kdi_rqBU-mkOI9axNaaVYXhYvPKLHWG_QRZrATtMko_lVUbqjfcDogKMH0DhdpTSb7daWgdachP1M2qyUwbtjqT4CWu2KVjnTRr3rBNCKFLzyXbml6qCQjKiuuR83ISeOi-LopyrprEOmPioMbNaTw-Mxmw4UC3ysZJNrFk_AqiFclQAeTdoGeBT62qJS5jYLf-Z61KPwBiZyTgyiYV10PlUjIiU_WNKFTnhJjv967Z-MvzcsL_A5v-zVrA2olWJBXWrhe5v22nfSGHKq3U2acGmcoq20NaSHGpUwMNmZXOCpn5Hx0_NIPy-LWWIb2rcq-5IqlsI6sfyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt-6HojYwk0Na1kFASutqutjX8znV9VgAdMKMeZHrxp1j-NlFoQdCq9jphb9m_0v9roAh_rCYaj8XaNWA2s_xGqZmdVny5wJNHTKIQoiOUbjuKokvLZG5miRg-aQEz4Tk6vF4ogko7ykE_mE69zyQiu-kzdll3EKRS1rJTTGwDR6SyvGBF2OA938-EfI5wrrKWmdXrLB_UvU2wlD_2WW76j8vZCiV0QW97WYpT3JZwqoHgMry3rDTSnzUqAZmc0wiMYne45dDaTTc9Hjoyp3QKSU5BM41_AsGWUoLVhUJnXxOxxkjFii-o1ygckb2lY7Cd_Dn0U72VzSRNP8kGozEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saHVjFPkBeyln2OOo861GRb-YI1-0sjgqX1l3gILi3jiwnhQTU3CCmF41QBc3epc93uqv_XOQYDKEIHvLG68oPFBh2DeQaNId-2d1xIjD-51l_K77sRranRvfAewA1N3FNd-51giLRoR1c1ctiGep0RENrLkRdxuP6K-idRF789xn1FD1W05GUrjKcKQZtPdpDmotpX8hEoiPpZNDvU-EYgz8PmOfZFygzj2B4kco7P0dIESqoQbtcx1Jf8I_R8REl0xirzeCmNvXZimU3V0wKFD8xRMj4ETlmi-nHvwrFKIRPvkYwd_YJI0HoTghRNFgjGKigh6qsugl8yb1hnVxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIRWrFZdwnFAMpgGU2JD6dCRCJAgxJJgxI-5YZzZ8F7Fcv64CvVCSWmn2QqWKLDVnGaaBxEVbuw5QFIeK47cwD5SwbRMTrkCeN0W3bXAM_jyF2hpO68LhVzosOQSfA15eTYBq5a3UnLFsW1IbvjpfnaL2nkORaZAsoFg10DXAptrBdYoXSxF-a4RHivFNO7tbUV1xVFag8F1kqLpfKSlv7a5cudq4b-SmlcOGs6oN52QDaTtiI0a6ugYJev93YBeikh0Pnh1TUNeMu9yxDgNCW68ycus1_FbeIX-JfLH7549HcV3MPOUTpNSVyvAwu7ecmtVxxTELJ3KM06xI9PfZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl_AXNodVWCRoAEquyAYSHV_xrhbCtq9Aswh0md4aQD6KykAhQhm-UDJPuh-2E1CHfgb9cncWrznRSVBjjA6x7p8YkqX_Dep5K0n9KbFECNOBZNtr-xJhi4lIuaVG_fFsqGbF8gyFTdLa3aUDAdUctAt0ke7ogGRK-GP8YwdA8vNwIb1iu8NkZSLxobNgFv1sfewgiPq2O35puj1x4GaPvDsGR0cDsq4J1hFY3Pzl79yik22yp1YoWi9CZmvHEgeZ1MU7L6MG1pykb9HAaWYyDXejs9ZTylsNWITAzbNHCycWfh3CnidgwleImsDYii8iuIjkkNme4z6ccbeVtJW7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7QnORL_e1_j1YUUaqaY1eOtDm2WbLF4Xtylag9fDuRBi4WA8fRphGA_5_fIwAXCGqrbZfTgB0PDdqC2DwFFviGN2ut31W1Cuo31i_WvNWiSX7fB-lFF9YoB3lbvDjhsHyrnSMaqiazgqbhXTDvddwk6CATGDFEMv3OKrzW7vct6eBreIuV3CXQIgsqhMDHh92jItPioOtLLRpiAc7onVp9mfYv1-HZPtPdAWyP1vizjzwKjDMyGw3YYPW6dFe90lB2va7BXYcI7hn8wsD_sOqpPGP9o0eZz7WSEpaz-iIn8a-VlFstVUdP8MpyaUcew0-khUAGm4aX9OKTohjyFtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZDJlws3FJYuO4w73_Nbk-ltTtihWctPiI4Oi3p-BksKlipaPaZU3oBtqXdqGnCrEigtnHDwYV6qKMl4Zn1amsqHaksa2c3mgCSg1Gxf1tz2BGrxn4OcjBLpL5eNmgX47HwF0wcKSz3fHHZrDti7a4rawlUVLGgzKFC19Rcbe6FD5deRxWZS1chuVKypY7DMNJLD-pLpuI3WRpAhT-dle2lfcL44WeYuwY2Gs7rKn4eCK3Y7QEewNwGlBojxiwqDBhL6UW59xIpAPXCowX6mqOBGf8ERKxmov3DxIeFAnbvICzm9xo0mt_ykFRo65i8AM7_FJe0mTa6K036fVY5YSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0xrBiH8MtVfNNzSolVyWcOcUorwcEAtRcwN0zmxv0Ki3xTaWVtqIkFi9Pno_059FbMy1o4MZYVT-62vPLegEzudSuQEZPgimRFwxMox60qwgqUbBBt2knxeU738NZAreFX50_mSmnZ4JhQTIef18kSTQ7by0PvM5xluXJxR-A53_PHoj7wIZRqaEmFj4hJ_M9cOBCabXAHJVbvaoeoc7KX7tgpANhRcdeivoDBEMbU-LKgya7p3GhUO9uOveXX-7Ttog2xGwsTf0sO22meie7jIIXm2V-92JbhftaYqdFWGoBQKRReI_pplOJ_ApXrRQzShy6jy7HrpmpG7rv01iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4jlwWe3w6G0c7HD_Y8WENmPuNXVdMfvjGOVsrDij8Iye5m6Y2LW8LFWKboaQa7bR5UzQK8z5rAHz6R0YCiezLTQGlRA_Uh7kuPorvi3mzXJhpDiBlsPDYbi_KZ0ShrSEGFWvqfWFwl4hqZnjGhsw222AcOc4Jc7CDMeUhUJpFd0CrSCDMf7q3UvQgrmq3bxsA_WrAIQyju_18CnqeCeQGpJom1QZgnGjvyET3AXWFrup56Gz6M8LwJ0PKBLR2gEIBnmGnx_AoBCgYDjwNboCkx2dNu2apsbxYvgb0mDQEJNalDjtM6oTbd9suqh0QesLjPEAjaNjKmI8hKlmM7vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5S_ct6gHdeRe4mDJL-0_IPXluW0bTuMPIbPzqYDVbfFucVIzF4DaF276OxuUZNzcVa2bCCRnT2qzmP_XWy_HAnxNzvv1QFiva5R988l4ZAtHh2uLmFHzvglchrPPW14-BIftwyDq4als1l7kGgx0mQXYmGRqBrFlc8RQAMuFiX_5B4Ltd0v7tVmxDU9kv_O4aL4KN2O-9_TO3KdgeTL8YQWdJsrjp-ODAuKAegpBLrgW1lVNQ8nLoqzQQ9w-qjvz0BGZrDw0Zn3S2Zh9hRXyfAxA8mgowignUMjU1lBm-v1_GeLOcaXCxlNMe2SgYRNAosCauHo1i2y_Hjee7sl9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX4NW4JkiHYtd2uwbBFyT0QPz-8dA7W10LBUrQC2FL055ZU_17ViThyTShvwUC4AOhNx94ozxvYJO5CLCLuGmfgiu5fNp9qL9S-7Tyx-bo2Nq30-PiAsB-3_YvlP8sXDB_CkDUMrWoZo8tKZd3YeaA1bdwl6GMlu4q4qCQBIY9UDrWQiRR6pETLE1lkAQqM4FJT-VumkaGZrEhdKBcPyM2MagHZ0ywx4igFA-6fAr63iZaOOrEcyzu0dVHKFDRY8l9yCl0BNMS9BdvfRM0crgQGn181efpw5Zae_Z6y1p4k8ZPiM42narmLHWUoVJBMU6pUPj-Obzp9YZdNi_pLQoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQvkZGZhfPYAjFngppTcESCzBcpo2NwbCSEmohX322ur3qTkRLOliYE8TNr3L5FiYiDX1O958yqklgWafeLvAehQJLsk_61vdJP1EkS5FcoMIPPa5y5P6gi_fVe0mOk5mtE-XhHmLvOi86FXVlkKb8hXIZpQ_1O73yv43jkQcEcJ9kGwGNqr3EQ1qy4p5POq60vfAVmgIw6BFAtKTT-oKGm-gnTY1hH168LRJGg3o1Ab9FTLjxRdeS-40xVXwLngPlPX5-nWsztFI_N5pGanz0j31mvFiRqK5W9UAIUCE-Sb30vZ2UdlFAY3F0D5A2ruEnoanhAnFnWyy21VnWFCIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcnNZCmonlTr52VoR7UHUoc7CNZ1ZtH8Miy0c3zpO1oPvG84GsZQAJNMsnub1dr8KPTyW2S4MCc309uLADwC0Gn9chKpf_6dpRS-4RerS4fCt-rHmI5zfZwDLK9CkexURVEZr4IVLVde3m8jr50uUlV-bXVVabiJtyfAygZYLIlpxsuRSnw8VK2fQvgqB0f11US7Tr_w3Rj9oy0pOQwh0KDoUQTGKPf2abv6PkviCwnZfeoOGSlQbvtOnXrQadSg63vDxUmCzIFlGeldmRCMcTmgAlJ-Qc72tMtUQ3LlYKvyND8vbV1xFWLHLht1ttRUyaGxgPdImoWdZercbJzYjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9gqWemhShegWdSxGdER6CD8RPU-picxPIh4AmPbrbHm5aiPv_rcMC_yrND6UZLNfIdZsiiQKEaby_Rm5TSxbYHAgVhG8fXitpNfCPU6WhAPDWqxOSDxHf9EDRYR5kS9YvYBGLWtavkF1E3iKTOYT5ptjUORadLG3NIVxkyxmRdWlxCHxG95U0RtGzbgHzcdbLxSe_g75_836HzVb8jyz1P_XBq6R996ygsKJOljv9a4nzoU1V-DvjJrsnwgAXFSxvWBmurpxSr9C4V4OTkAt1de0wIYrVrO01FjSwIQ9WKto1WQ09UdvyLCxFBTdx2wRqlQuBU1Hf7aF3CzKcX5Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZxjE6Z1R50q3HMMpxGaAgFsNnIoNuEkTSvD75hpXjYb1vEKwapIWXBrQny2EWut1ttRwApDy5rtq1XIqgynQbdVklhRHflCca4QXaO8tUZoRogcSre4X6_wbFx_BkjtXdCYk_yoQ9uH-CD-N7xP9rv3nj2Rbx8V4DHavEBOm7N3C4WpWDOKlOdsbAaQMwlrJBAjNaRMB3gLIygDadia4aBHR9-NCQE7-2y87-iZBPAAq_whuYe7T9lH0sVtW_2ZdLyvDO3Wt2_UV2Uxj9iobT5eAuA_WTUv7ABONV2vw3kE9oizNGJ-DOZT6iM4uo2Mlxdvr8gTNAK2YZocviR4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvsYRAU0ret6O64k7W191dJTFS0sWI-aSRSIHlbVKdJdECtbhoI_7E3fYTt1rLIjc5OCLQq_DVRMSPJoxyiN2gQXHY1wpgEBZPQcE00s6BZAw9BGXbws6EwBdMM1otmujUDaEa0XcEKbyw9F95NaZvm4xX0foLwNZQ5quCUyEGMSpypVpDT3st4QaZkEsvea6_ytTn4kOXQJJimMoVU9fBWhL_reMNIKiWbaSJ5UMO8J6_qA7rKEdzCFlak4T2EOCFDh2YoJ80l5DflLRkg5w0_PuDTgazsl611Zi1V7TbaMGmvjsvYYJpa2vV2i0Ur2ScB2yZjO-k7pGPgI-s8M8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUkiWLVOTZ3VhxBUvt7Z0AsDskmm0N2YgqUEiM1n0u6RUaLGh8UQKrAw8iRCLfumrdsVl34AXZMc5V5lMaWDi1XW9Q7aniF3s5SHIllVlqCVLZ1IKeA26j6yV6OrnLYNgUgIgj29Rif0ojT-3wWbUFo9HrWi4SJxv_ITCMgytCu3_wlqk6dFVkwHpL96-F8pwEXEsPWosvbNoyiwby6gUwpWEMBuOYvc5aOT76Gur7dty1pReKto5gvgsvIVeJIXFCnqgDWzJ_Wv-OqDIJLgthLDrYU_6yFx55XEfgVvndePWkQb6VVnLF153q7Shia3kHaJOTn713X5iRhSG8g1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbqhnaHgS4nof3kPbDFd7qHW4LHUE3YwYHtRagU3i3MOCGrv9jUO9hdWtUNV0C2Mjh27ZSppsVCLAaDKSSRHOVnXSm7tdrkMLZZapbd1mdj4AThVPahKMg0NyFhNmaIea82VXKFAlPQ6FZiilZvGtbtPCijKC4cR9EmVOBfKlA7zFm27-yobgGDtQasSdICBxi5KaDDZRtfm_v41VX3cCuklSOXbvkU3b-fH1wC-h-kHvKHmpWDbenVFCHkNCnJhifZhjOnmoih9zsyPzJSmsJhilpSE11eeCJmotCzFSGOudTs03wTlIeynvR8IGQXTRdTLnjDsvMgUg5AgWDlieA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX5BAEH1c9uFrWc153QhJIrJL1nA8xMuSRZyN8bGRqaEXIKcHA8f5op7fRVHc0mFKF60ruBfmrYblGrWDAoWHqUtjPzrwEqdh6Zf6RSBP49xl0dZbqdzR8aiekKaQ-EA9zVVlQGBw05PEFsOeTOmiWYqUXgllPiLn2HtgaqYtKPfA9Tyd6YkKQIVaLAVeBTAefyjFTzxcOhltiishVOhSetmrHl_Wktz28ezvx29-196YCVG5Ub5-u0fDdjwszvb_2R4DxOjZBIDYtI8VYRK2jx2VTfgfqKqNuoWHXV-TcLjVJUcsa_2G5_woQu8i7KjYtvENGlirbAiPkPuwF9izA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXnTau0eJErPCYUns54lyiFIRFw-8qGpnKA_yrPwilWD67vhtGuywlUtsb-PABecc8SYB_IicB0bOgNUxLp3QnToaaSkJPWss4ipBhbeMkdsiUsh6nSXfH59X9txqWQI6QtUe7TvPEgp464Q5tQweCtt7Mom_Zhz6ield1woduVGvRyAdqpSOxI5TiDhY1BEAjCPi7xLz4TXVY5PIsQa11JVrmkhReD5yU3ukIxUL980Dl5yOLx2nngR5yfZX0RZ43F5gFdBzJaJ_ZgUdUUL7KFITwagVmzlho2VIiUBSqvLqanGAwPm3oIctSDSeNLVH8cG0eu7HgPHvfmVN_Q4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7qY0BB_xCgwwAXXZ6uTIgvaBHQ2qM79vSrLOBkhErN7KFQz6ZLqNCBBya5WtYFN1AFX8PJND_1Cu-twZgjHVsjDSJT8N28jm0NykLDsL1fAV9SJE9LV2QhRoM-vk9KlmY2vZ9Cjm0DS5GkCEjikQi4M0sjIYwTi5Z5Lr9bxLVIY3TDx1tscqsJRsERrWOwBFTg3hFe_0t_z3wk3m2ifn1_mI0xmTY8ZXS95Q5PyK76guW8Z2CuP4DzE59UFend_3Wtkt_d2GKFoMjVModAW795ydQqWScu4PYl17FhV1wRMnGRGWEaM-2o2sE8w8O4wP7-iuvCVzfki7CiCQCcycg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1yXpnhWCF7mIQDuacFdGC_c6h2VujhvoG0J21q82pPd2vJF3Av3KHZIXMMPtQlVDlBa7YYEM7i7OsehIZ1x4DScRGgTJRPWXI_TL4Oig3lL6kQuQCHKuya-ESueb8oltsmL3_8FA6JgKtEjl4Btyu6KcRp3ciW7OUHw-il4HhIBls3CdoxHsQAnojEDSExgiFQ0Fcr1qO6_G8e71Cj9YeQc0xd0-IM4vjRwupJte_KxpiBZIcg_rxe8hUboj-CFxL0UnOfVby9ZN3AZYN0P_f1-IyWDB7AXtmCH8WlBvZ1ryuu48EBuKWH6LjrZn7YcVCbnmoKz72HiFojb8h5eeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKYOkT09GctLPlgk_paE0qJU6Yay2n1QSeRpYVjzV2lyCNzz9nH6tfeJZsnyk9eWtL8zE9hseY3Tp7cOPN7MKlBGYgrOZRHLBUdGd_-ETSAZy0qcovtThdhmMweF9FHxVUePMZ3pg4_3v7BL7tGAeF2n2-Afk2D2jnLFrh42bthqpEiCzPHavMTYeY4y8rAyXzcF4WgFpvxiOfkrkhmXiTC8nNBlBklj4SzFCVJ7Qg692o-zPZAfd95K7lVO2qKkwKY4Q2Tr2J0DqT2QAY42fVMOn2eXzGlmrbNUjNRYB6ISiMBwhLTdhqOT5E--PVua2a4rbV8v_pDOR-L9eY1AIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiXjtZy3jotvcQVsblXx9vxPVSqkBcT1_ZPWeboJJNvraMoE8tphpI5rUXdDmeqqJhgC07vEiIg2CVJUuHRFP6GPC5tNfmDodSll5i39RNkMfOdKWsGPXsmOexrPjONnl9KAFFL5AabNhzD11B05VCg8YSmLKfCYZrGNB9KM6oxvw08gTjynCv5wLirSqgvuaXHbOMzMb6abtVPIBei7Y0qWBYKXolXDeB9Z-ZhNwf2jXX0tpt19AnXBfiKNqKw-0KMaGjvlViHpz6U4R6j9yp6hbVIH8fbG8Lg_mDF6bDkUA0EWZMtp1e50tvGGq7yIBriaf8oFnI-N0_Po7CwR8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvmzwNOfOiyJmgyzAPPdoSNbwWd6LcKd7rdficFSuILQbKaWjhW8PElR9_23ToHTmztKKZvNc0PLH9Zz9FtvlIfR-ITcMGIN83VHy84Tbwg47MNRtaljbbp0AfKu8rns4V3JGyZ0XONepF-tvM9Ahtk_9HEzDZH_7EnoLT8zPriRhSyVJUosdcCf-EWTKrkfVwMsFZmwStr8edLm8CUDo3JYqIIDklIk3MG81ycvt5Mp_wsRrJUp1X41Fc_AKBmxKZkeryB05x5uGYqbDErYd-sY3iiJFeMZfChThPEV6nJYbqIVEHtJmTb0hFfrbwkgG4o5vXFwlAfEhLRNQDVT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDo72VdHZcszNiqEDkHHdUbTcv1nqVZYveyRa5S3Y4RahBF6VF25IwOnCQQyaklkWwFrdarmuk5qvMq27HlMVJuQNlJKWLZeb2k2GwnGAVhRhqBgREUuDkDIpB34O63idYkB4jID3Y8kBoJVCtPc4cZGr3S5u7P8LACWM6iVCxAXT_ZHwWiD-FVuf6b6wfipXxOPPycNn8vR8owwL3ky8wpRLwu0qJZcqjN5Zk3whG-7107ojrkp3eFMiwTpJL23KCc9-6sngVUmzeXSEqGEIymiw0KBEUBR9h5WZv3ZsPaq1fD4weSD8EFRs9qM5pfPH-dAaHMHQ7lk3K2yRxTGVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnuy7nGN8rGIEXE2KUDS8Z9BJY9GxlLhT4BI5IP3KD99MyKFIpQOm0w6jOSMuk-2HFt0A_TAOEpyM9Vc7lRzNk5U1tZ2--oV4UX1EQAG6Pt3axJSah381thLQQMLRly20EEFe-2nSYS_54ayRHgXA1-XuZO5qAtJ7mSiihmee4B5J8Vca39pCiPufGiJoiiZdo2TOINxyxZAKoE8lyr-Tojv1cA1xHb9e6kqsnVmE1tcvGXYHuUTIYE9qOXQF6HqQ73x4VGWB1B-XCp3BOyawAUw0cawHjX65CSIq7_VPdGIRG5M3jubT59iZtd7BDlIDY8CXjRJsRzg365KU1w_bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLQKvUOIK3Q3M4IcnpoBJ3TzayBu1IqSjNcvn7Npg2aRr4FmY_THz1l4qWAgDBVG4ulqQUwFn8QdpCpeEGk4MPWlz9rWURMmJzBdZpNS34rHSUvb6Jdkv6gSFIi0YDRT5u7HT81yCiIJTBPadwB2Db4ez_EpM7JkXo6_gT7sRnIqcjCgkK0rvmCwsoE7c4h5zTMrnDCPZVQ9Dn7nDGvzzUiscYgmo5xyETVmBRKlvLFxA_CcpRjPXZVTbtyNhR7muYDPV7g8kJ5DhVqLDPAc-XcYcN6JooIdRDVSHJGbclGMMcb4qDqo1-_qyJMRXDJu3FSGFbxBjgN6c_dkOLeeqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzBnEyOYtiBDwxlTR6qKZAj2LIruGdaTqYN-WQDauOf8OPbqBSFSTvvRPCSPRn_bnaz7bZU9Ml9aq8tOJBpCaeCjqdbqy7Xln7DNkg6LyaBzCyQD6R3-Q6CBVZwP2_RArf_5dG3Aq0sBWTGB1KYIr77RFoOPZt4A-vDvhhGG_8Vpxb8epD3iCerJa2B8c-2wlQ4gvpbKSVpxEJV0ftesscO1T7y4AllIoZlUeJqd0veZUU0HHVGPo4cSrjc-J7ucgHy7OrOjAvk98iKaJP5fqGTbejSXRSlG5YSFn3lt7Bz0O68EIsqnMorq_ehN7QryZaDX6fqffvQAd2ecnsjYlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyQCfDmKvZ8E_ZhAHHyD139D7FFIYHu2QXkCa3aSQsn7vjqxwxA4dRucie2OQtQhkcGRn5E6zGnvCUCWzg-vMQZY3ECJnm37urIwga-qUIyU0xjxd7mDUYiDwNjP8eqcC9G9ssNQBOynBZEUCnQAU6vG-SZk763qIAuhVWeJxf_aLQ3v75Vcahd6Zd_FRkAP_f9fxQW60xKIQngLYm9bqFjNxSWdwB0GgKCUAj5riVH3WdNhVpn0rVBAZS_a1kM7a2IAufx2LPz8aEkIIipwjeNaD7aP8GebCUw0EW0W6V2RWtDE6pfZ5p5M33y7J10jmPylAn8nrcikTcmL89rUA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aNO14HCVKBCzAJyw4uSvYweqHBsi27jpfjwOfkVhTReoto55TJ-ndrBXvTJ8q6sk45df_Y4K-88tlHeK-nPMo_GeJyx-ambGkDZOXRfHzQjIHuIgXPTcq0K4sV_nLuD-EWCXy6br4JKioU--b0yRxS-U51hTKqfWvV83vPl-WTRujfkFYumeMUSwUrxzNmuFL6xnWiwxZOQhcW_HQ3Vr18DervTtbSdhKDMmUnA9VxNJYwoghVoSkpVtTTiYRLAcD-4sjmOZ8mhEwTLwvOgoEEZXwKhaV_kynnG9oOL6ZnITw19XV_4l-nE3F0mm7dAzu8kspk6P4qx1agnMwVu8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aNO14HCVKBCzAJyw4uSvYweqHBsi27jpfjwOfkVhTReoto55TJ-ndrBXvTJ8q6sk45df_Y4K-88tlHeK-nPMo_GeJyx-ambGkDZOXRfHzQjIHuIgXPTcq0K4sV_nLuD-EWCXy6br4JKioU--b0yRxS-U51hTKqfWvV83vPl-WTRujfkFYumeMUSwUrxzNmuFL6xnWiwxZOQhcW_HQ3Vr18DervTtbSdhKDMmUnA9VxNJYwoghVoSkpVtTTiYRLAcD-4sjmOZ8mhEwTLwvOgoEEZXwKhaV_kynnG9oOL6ZnITw19XV_4l-nE3F0mm7dAzu8kspk6P4qx1agnMwVu8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1kO7fqgjhiQtEWp1JqK38zDNpV5b7g2IXpH8YjHCGFTztAOThkOZMfibAXwnuF--toKIbNg0ggP0f_J90_6RUM9e38U_5r7MNib9o-R-1vDp6YFq6cV4ha3Hrl2LBZmrXp5lgUD5k4DEcRfnVOtaU83uNZFgx5WxY8IOmW9rztiPRwe368vCPk45PUi6VpsgUOXPVw-Dic4kTvnIUzTs_JKkg-c1HeNnolwTM9A5HlU0Fk_3jQ9mJZeNPfG1fIId_TUAXyF6yh3tD-813lzDDqi4ExsyRbD3S8uHC6m-Ln2U222kECboThPs-GJXOGCWXtvxgipGozLF_ETqYc_Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pajLx19NWJ3pXp-TndRGxUeqFiQR1J2mcn3z45kF5HFCgMdAVgCcwjjKo-Rl9IhVVCV51_acYebmzVXC6EHYSBr7Cksq2z39sx13VzAPsoAPf08KJCyEDeOkyfBAoG0D-uBOI1vjL8PolwCUU6bJwBDgdNqgNKClrZCZqf6tIkOu-_GVAd1KZ0WT2qe5LfKZyCJsTcSPffxzH_1WfdnOwsann24Blu5gi7b-Mo_Z8A8Kv9d7QFc1oKebFSeKdeBd15gD7PS2aoT_zZxLmPIy7LB8DcldTUc8rP9tgiVGvVYHVMHTVT0q289zRZ0XUz5rMqi5Sjq9AmbczZ65D9ptcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBHZmnpQjY6SnjNSHk2KjavTg4-prMObhd3TuIX3zRI1HRdL1BDPUUh_u7edWqpr4kUrEoJkW1WHyoLGUEU5PXJVVHFYlJZeIIwEj0_cGJtggArBqDOaMsLT0O6BRRFV10kWWMtBIQGKh3CR6OsckEtWJD6ej0O3IRwrOo8AoAtbI4kD8XKo2lF74FIUb3w9wNpwEaF4-2SjKdx-cN1WyX5zaLHtxt91g3xbkJ9vAm06IZbC1yuAgPbJnVPNxvcp8z48qpFW0g1Yjc1JgkpcEEtCZA9KYdyqo_vqsZGXzvDCQRPLu02IhvfXBsNiHmkYniCAPVQKXmjN65VlKMLGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yc0mSZJWg9MWWDkjmFlm0CU2RbK3IEWuTM_7VPlA6_DvEO80vcdKrP0qsBWdHSr4eJh4m0E5WiEGLfR8p9kk2wgRD4zgthmJpRN_q8G5JNzY5uusTjuaNpf8wmEnkh4ccYJU-RjQr4Lon_C7oxIQMPG0p4Opn7q-48bCFwWgtMjAe51MGKqWH49ZOJfNN_0n1APd_y6xYLebN7xtbBeOvPmjH7tfAk7qW8Q4ghLo-lUV844EhnAhsr5t_cRyfBVUk3hx9gJrYrgOm84j-RdDeLCtjG3vD1X4AIaZGftfXZuqvBYzdx-zKW6ML32X4Tn87mrrGd7ySxhiebYd8jV4HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5-a3H3kyKQYwun6a79T85gNyekMTN8EU2Zs3XIhWdzWvecMvn6A1SKXL8cs5n6w9y52-phrMd3T62X_k99x-z_q6mR7iFi6D2lxm0tMuUCxavvJ0aji49DjX3KI0My1VLYtkAXzper3NmyqLMCJLkyOzE9ONxwvd5AN5dAEO_eATODtdzOytLRM82OmZwqc1qbcW1j1QeRFtTVZw1SpYttR0UGi3qbw64P6IWt4FmWkD1B5jKcGNHowCGvcW9a0gxBB3zGIU7GIcDwozR9hBz3t7W-Ats1SFrrg0RDBcTE8SSWDGS1ScsJK3wNY5J7lIIC6qEoWMxrelHdAoIVA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haLjPQk2QiSxt7Jzh9wsQHU2e_mcz6nboVXHYD5WFA8VBytsTW50wXfYs24jcyIo2KFJtYaWjfsxP4uIKwp7vRwMpoB01SpW4sTWFQ_jAmyRxgV5YCaGHp7X8Sxq5SSs6HA5QMH8OXKIGXetqugIL8xZoeUKasraM5vHVKboYZ8cPB4a1yA06eqxYhqsKWyZ4WO9yX1DqAjQgLQC1SGD6k_i_T9-6iMjwqT_wPmo1w8KLlKi8Qk_86ZfPaa5OfwY4cYySjI1IepbEB3Wu8Tj2Uzz2EYEJ4UFJmVGgdcr1SlLk6DDmG8ErtceB3KhJBxbOAEDvIsLMsUGDMeYj65Ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oprkhbyODu3DPBbj_R4K6aew7g3lyZYs9uN41ggIZgR7Dq7wBWsMDZWAvF0tA2Ww_ykzVHc-o3b5OPH3ZW36HKha-pwZuoW7UKMfxV52XvSEYKTNqy-O8YM5DGHe2kO8HYaRoMlQh_ul1R7QRlfPL-XtDKIYOkSEYCuD4Upxh_ZDZsI2p_YqJ0zk6aCSxTCDIlJ_vGSIZO8oqKQ-fSgjkVzKRhKLKVlCrafxY4fNRN_OyPwwuIPSsdZBGnZcUHFDxFxpqGWFeX2FrNplTLVvuVykgyTYkR9bInIDbg_tRABFz2-t7r6dr1ezjObFgZMASog14QsXrepahKjy1uXFuA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=u7OQmQiu71G6BGxSzkbaaRfAMNaIseDHh3oGM-FAilvB5Fp8V405KCDcGZ4tnagSvk-fpRsYSppH84LdNFIcvCkiXp6L0V-W5uE6dBjRySpktk9Lfz6_pH5_KOJDzvs28kg9C9T7Ll3lk30vWmd76k6khPqGJbCi7KPP3ycQSjYKN8cScOGwNwG1SWinrcljIyeMUDtpOwPG44A36LxPqzgNldN_pSkHNG5PnGIepmtGDxvrgu1fYhtL3Y1vhbi7GfSzsrFI9_Wurk1Ex93z3ACJHM-Zsf8f2PCSf1AOLRCRXZGGfGZ5iuk_WvIy3T67z8JHr8XoEA9hcAWkVrd-RSAohV0pzIlorBN_LtxzZnE5YzRJXHNwacyD6DZhd0_NHt8C7nwWtxIiXY2MD0ndAsP3_iR-ZTlVWZ4Bl7Af3RUWb0m84x07_qm6WeuwrxNTr0yHXgteSOYxsjMXSl4Rqf96yk_ycssVIAnII0rTORL6oRyDxZeCZpQMOJxI_pxRjsakhdNoOjoPWOk6Q_GJFSCo9K37UDHcutlUfN7UIaPHpWTUpvVm-XK_PbeBE1_AXdebvmANBBdeaT2_iG_17OidZWwZAWwMdLNpSzcs2wHPpE3YI75BpiCGiTHOzKkxZw6VucQL-2zc1dHfhhFXbfSwM0EgJCb5QPr3Lj3wZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=u7OQmQiu71G6BGxSzkbaaRfAMNaIseDHh3oGM-FAilvB5Fp8V405KCDcGZ4tnagSvk-fpRsYSppH84LdNFIcvCkiXp6L0V-W5uE6dBjRySpktk9Lfz6_pH5_KOJDzvs28kg9C9T7Ll3lk30vWmd76k6khPqGJbCi7KPP3ycQSjYKN8cScOGwNwG1SWinrcljIyeMUDtpOwPG44A36LxPqzgNldN_pSkHNG5PnGIepmtGDxvrgu1fYhtL3Y1vhbi7GfSzsrFI9_Wurk1Ex93z3ACJHM-Zsf8f2PCSf1AOLRCRXZGGfGZ5iuk_WvIy3T67z8JHr8XoEA9hcAWkVrd-RSAohV0pzIlorBN_LtxzZnE5YzRJXHNwacyD6DZhd0_NHt8C7nwWtxIiXY2MD0ndAsP3_iR-ZTlVWZ4Bl7Af3RUWb0m84x07_qm6WeuwrxNTr0yHXgteSOYxsjMXSl4Rqf96yk_ycssVIAnII0rTORL6oRyDxZeCZpQMOJxI_pxRjsakhdNoOjoPWOk6Q_GJFSCo9K37UDHcutlUfN7UIaPHpWTUpvVm-XK_PbeBE1_AXdebvmANBBdeaT2_iG_17OidZWwZAWwMdLNpSzcs2wHPpE3YI75BpiCGiTHOzKkxZw6VucQL-2zc1dHfhhFXbfSwM0EgJCb5QPr3Lj3wZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTmyUlo3U2k57Gj08v5GQVIOQnY9JvgybGXCb-J4DRxa5EGCoBShBtYKuuta7_DuYv1m7FXrCmrag6GeWqTq5Wyi3rdrZb70cYEXI60yv1_acsAG60Wmk6hFhEUDKef9PC0A0gvPYznS-SUGR9ppDy_thgeLnoBX1MZwYicKh2Ni6f7VHSW-xZgXySawExrP-5KIM-SAaeiMK1PK-XodXGtQQlGoGaS6ZWm1ONjUg9JTjB2QvNTtoTRH5nyWa4skEmiFlAHkXi1dl5l8ikn4A7DcReIHPIwaqzLSaL561zq99gxKJBGe6D_BeatIEvTlWpK_laBxjyE4pCn3bQAmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kocaUrmoF0NdYlQyroDOnAGntMqWrw0otwujNJV6Ub_k5qYiQ_YneiJfb8GN9bix0DFeW6HsdWso1v3FLK_TSUWoErx7UB_hOzSA4MxCUZQ0Rt1eUUgraPXAmlQ9--2FDtPVOCa3FQ8knJ7dSb4q0g8VKpBDo50VYZJQpHqOIyiXQs9qBzkzWEqZETolcPD8pPdT6QEbFLYXVt3vWUBGC-GJWxmTlwvBBNpwC_R3HPE2KwITiMKvui-ZnKtnp8m_Om2QzrZuNR3JVTlY7AYMdJcSj0GLFfR-Zykoz-OZwtIydNQcFjQkoGTLtrAcY49SSL96IZl59rCam9XHBdqWTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PM6XnOAvmxSQRkNe3YX7hxs_mA-Ksl65s6BRaiGe8udy4dxipOrs_hOYyHxfSinD0tPvGdr7N3qyjwQDwrv-pVVbZC5jlrKzbSBLfshnuqGc7wkjZMMtaUX0BLNOyjVRUmPcuG_V2XyEdftjf6bNUVLUVs-_5nljC1iDwEdx4z9jhLRnmBXDNbYvOge9xA9m09ENXiVXNjIJhAWkkMj04G9WBoELyg18LCmSluWg_Cs5HQeS67SCxYGXVTV_-uoNB46Vh-SkJEOMVglGEP3Ji7pxWFlqsxiP47zW0I2KbtAppuMXsf2xqjjmS2eUh2H7kEEh1kvE96TGjo8wL8LLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTJFvlmQqrLj5-g_Y6LCs-LBmpH8Pw2BLWK1vVMijASxPnyq1YiInD_TZ46g8zmwr-jMslhlv7qskh4xoK9psLvr2i9PthBMhIC6sslTDhiPe2DaYeKp0I0RmsKJ2O3-oTP3ZFbVNtRIwrds7zW2XQrDBB7a4UnptDxFIXbW8PmoMXIqKc_8nMcLbF-aKoU38P0-wReZeyQOLTbh2fXjXuquPE2jTKcnroNEwZj3Rqp4DWvivQ44_5xhnD_m9nTFWi1PQ4DNpiscaf-aXltUo5uC1JXgzmprfkdVAEu-_NpEB56Qu8_aJxhqHOThDC62T8NXWqYgnZ1G2HoL5ea3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtGtdn-AEF586zdbW5vogqTCM4YFNuw-nL_DbjRL1eoa4NqKtUW_E0Qw86OgTPoZ7AiqXAJ-5dn8VnceMlEOkpS77KbQPXzERNuwBkZue5s2H8tf1GFyZAJy8Xe7PirJbmqT9hzgFddImcoTbIGlP370-1i3ducKI12l5xwOEZNHfUlxt0EzInq3OE_Is5VWq2KzeV_Y3vmvFMF2QwfP9ayj715JLnI7na-Kn4qtHaUZOe0BQOnCiX-kVBREeKMLpIEqlUPjTkHk7Y6KedSMhdaYmj8WuyamaV9PLXnwLWz905i82ZXOMUkMU48KUiwb95Omj0OA_6S9ZwHjvSH5dQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QeEDUvDIaihAO0OFbVuV8URjboitikylo7LFzHNIar39UzZfIbWaJK8Xpn23eB9BjDevmP7QZPgd_sBsKGpvGuEdqI47GyKXddHi_BpZy-CyotAsFeYMCiI-greIJNR8nfAUcZrfzI-uooBfxZeZhgB-ea0nQjyaYS_2ySdJpNLdMY0FSqcjbet4wl0Vw_NkeI1pjoplgRqIqlw7LZycOWLsJOYTafz26YzfofbLuDgyPbpm6B6-D3Nu-Cgi5YMi9oo7pig_tTPjt98seyDHs1YIeF97Qll7WY-docoy9RUmm1kXJfJNptAEntNHS_E5uNfvaXO5DDq3OoPD-II7aY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QeEDUvDIaihAO0OFbVuV8URjboitikylo7LFzHNIar39UzZfIbWaJK8Xpn23eB9BjDevmP7QZPgd_sBsKGpvGuEdqI47GyKXddHi_BpZy-CyotAsFeYMCiI-greIJNR8nfAUcZrfzI-uooBfxZeZhgB-ea0nQjyaYS_2ySdJpNLdMY0FSqcjbet4wl0Vw_NkeI1pjoplgRqIqlw7LZycOWLsJOYTafz26YzfofbLuDgyPbpm6B6-D3Nu-Cgi5YMi9oo7pig_tTPjt98seyDHs1YIeF97Qll7WY-docoy9RUmm1kXJfJNptAEntNHS_E5uNfvaXO5DDq3OoPD-II7aY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm-lzwl7lCN44LLdQiPL9gf1xC3QGT5ehtZFAY7sB7JZE2idv9Sf2V7hbG6aJesc3LUi0y99lZ_mhr8d-6qPLjg0mzt8lCMcz2XudgBOtoad9DELAgBYSuoTpZTQPVOuzkg52bjoD8by6IjbNPDeo293JfTj9xSJOGIeymGHjsQSc8M1AGuix7-tiAM6H1NatX4FSQnc6yEOF12adkVNTZAOFU5pDfqKB-zbUff_GvXf7pxeQhzOLSiMZyIQWfXQKuYhsBEdwN8dj5ABIdFfbvt-A3zidu5RMEbSyXWDKlp18uabY5q8-uU3hMBmsss-caNeltXZUrS7DgmT_zyflw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4vKuRWV72r1OAoW3k9m7kWi1wTse8SbU27CIE0z8jMnfCSA4DMuV77tk4PM3M9-b0-sWzJO5WQWX-D7aeuAGRPpkqx70dTm2KY6zQB1_84YAoklTmA9BP6DUJ2ZnI5fA8oPCzh2DfHupEOEpROyRhYA35q7ecmalve2D6yA97QJEW-qM7t6n4xoQ-rPCac-oPljLS85zg5FvmHp2IM7Z1by1ECJSJ-N7gFU9IWCtHcOD5oGX0m-mybiOzVEctf8pwU5BKZviXTpyDNnM7iU5LSSeM9GlUD5gq8Ka8-0-BevYQR4lqjfNAtUF-Y9LWIh1bw0ugpXNk9uUPodmz7tjA.jpg" alt="photo" loading="lazy"/></div>
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
