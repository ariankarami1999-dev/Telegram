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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltn4OWJZNVlDCMP03buI4RK01sSOper2KZY4zxLBCIP-PpxVGlKMqDsoszc10XYSesqjqzY_H-dy7-NNiWja6XVQJ8o9V4NoOWQON_f0QXMlLhlcVvpWMTeGDueSyxBs5nO45jIuDEjRWjjOtCt45oEdQPrO8mkj1vG-ioStbVRLYxL9FRkGnvt04s1FFJ6z2n1TQ9xwElMjUZ-5XOmuLzA7iVA6RSpI5R7XAErU6YODzVw_nmuKDrIy00pHrc-fXtKzSvNs657xAWry7f7RpBnodbnbGP9XYBe47jx0SqsEk9TE-FwpJFln54OvK_gS-R9XtgZ50TClNTZ4WwIACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 251 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 487 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=d_4tvs6oNRaCRQOkBVjzVeJW84y12Nkdf0uuDC0vbEUCzizpkDBNMpg8QWR8FtsysI5JKv4vEgSymhN9j_Ip35KaDdtRp3WT3MUvBqigTrBkWyysG9t9YMouxzaunzzGhw9AhkEmul-6crHYayWmcKTh2v9PpCcXhAQHJDRQ9yhEnqXM28hvPEbxbDY4hRs2sWRhMErR7Cn5DptmJGq91-ch3yUKJ066be0-XGQLyFFOAlOe6TUpgHuZIMZdkxe9i-2Xir4cEUaPkhFWKglQq5Ex4uy5gJaAmsA4MvjFraLPSdmHGaoBMzvOpBa2Mq260yc7RbOWgZ9_wkW_l6AYaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=d_4tvs6oNRaCRQOkBVjzVeJW84y12Nkdf0uuDC0vbEUCzizpkDBNMpg8QWR8FtsysI5JKv4vEgSymhN9j_Ip35KaDdtRp3WT3MUvBqigTrBkWyysG9t9YMouxzaunzzGhw9AhkEmul-6crHYayWmcKTh2v9PpCcXhAQHJDRQ9yhEnqXM28hvPEbxbDY4hRs2sWRhMErR7Cn5DptmJGq91-ch3yUKJ066be0-XGQLyFFOAlOe6TUpgHuZIMZdkxe9i-2Xir4cEUaPkhFWKglQq5Ex4uy5gJaAmsA4MvjFraLPSdmHGaoBMzvOpBa2Mq260yc7RbOWgZ9_wkW_l6AYaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCSVjIhPiiCudv7R17Oqk41fk38gEjw7R3mrs_E85fQgUDPvxOa8AaqaDMvesgXVHtmxtTsLOjoqhtzhy9TfOXgWxl_9CA12mZhxYOQrsPKbzF2oU1tinxVmH9e_qwAncHybOUpbVrJsa1lM0RepV2fY20ox1DBsduYXF1iWL72CNewA6oK0eqrfSNbBlZK02NNywpvNcbnGRxNAb0U_YNn3RfdccFLao4JiPWV2jMGOVjUG3iYFeRRUAnqn8YtziDjcDbCTc4LAzesQRLrpv9kZo8UdpXPdh3_srpnz-XHzA-fUfUoncJzoegXeTUA-DhxZf9p_7DQXW7iRGjZWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcbWbS0R1EXdaYFtkdxTUliAbr8L2OL1lG23Keh0ljLaNmbAE4adDGdKbjgdhR2TzlCJgspsBF72y0LckrAEEKP7EOT0ckiqXauwHLir23V8quDtwDF0hmkZAhk_2o3QypUspBZeqJJlGNgrlbXPkiryoqRR8Z0DxKfFjvmmhHFg_OF7Tb1XUF2FL9mYX3sa3THtnNw0UQ9uDS06RdILlkSJ6Hi4p9-OZdTDkYlHaI2w4zsd6hoQf4J_U05dLILvme6ibm81Ei834TTFVKtM_P47KXF1T5eCU7Otlk5BepcZn1xUvv6f3JXqqGh9g45I7tYCEZLs9_45JbhC0uvYFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7hEt3pcgBT46NR54xHHL-w_71PySVm0VI-keHx4JQWUsztXIB958C4Ls-WCj3XK-eOSRSIuFjTzvg6N_mfjR8DQWoy6HteYVINXYVZ9IHIMCCsqLUFayokjnikA3wZ4SEtTMzR7wdfMvcaGPfGI7YfElyvK6eF6oqhmwlAm7XFXjzIfG1uz3Wk0t_zARohBAl7G8W1vA2jkX9LhgOIXKDqTX_--iotUP-YlEr1ia1kienTdSe-IpXhUUzJaMOhS9qbbBT3NNCToHgGhh-D5kf4LLSuo-NLkoXV6AI7SB_2YGkWt8aowAMq4_lvcUn0tPx29q3wXh98VZRbje6C6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMphydj_2VwnFx51A-DIz-q8mfEApN0As1vW68u-0DRmliuGqbfB5OUcDXiC3SbQ0wpnaGLM2P-gwPjCu_Ngpm33_E-0F-2FutDJagnfCTWw72XdVThpO6ydnjUCZYFS3ecw98tg_VA3PE7i5rnS5RumJ_sZdbcVkuZkYvnjXIIL1QYtY33CPGKLVbKBeghUCaVgDXbfd_sKF3eGqKXkIC9rXpA6sD0Mg9tV3iMEzqPf4oGnrJOMCB-Q8vbzwSe-0pBgRvLBiWSGbP9c8UJ9b46XB-z05via_2u6K6CTuYHc5-KJnI5mib-pb0TYVEKszUXVc6iC86S_rasy_BQS0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy73iK6LAiSbFhy4sWhpFFekYsDJXmVF4t9CQw-6I6SPLeP_guZdTXnfn9R1H4xiGPiYLrr78rly9UJ_gGC29C5itT4KzNRZNcKXSXovJWANfGnKM_3fuvJKkZ5_waQH8nVJg5TBcyEWBZhibsiv1yFLStY0k_sqvGeKZ3Yhs_hn6V3lQ6yDu6Ss2UFqErPGHkR6s03TP73BUpvt_BbjTGhiDDpiZ9CZrQ3mvBLD5zgLpwHC6qswmqnWRHBAGmppO8SQ9_4ZAe7qsdkpYd-J573mm724vIkS-KMG5gbZgcKpmvPUrbZywLusfuaEd_YVCtIhZb-G45OEMRvHMgURNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcY_GCLcRtXu0U5xYEPF9SCyaQ7WOOsTeJSj2hISBz-wESB34hFuhfKMB-2jHIHTx0otenetMe0qOoGFMzUi77Ne0ltnAxdVe7bBk1oFxyipyV_gY8gz_ZSl4rUmET_xlnG9O1ua37hlqb0983ET0tVIeBvfNMaVyM0lg08WYUL1PvepIgOUKiw4eU--8ghBQmKGT5DnD6E5RZz5fyFTP-Grwp45PoFih3CPOZfqb7QTJmWlmLfKzqerEZRFqjWBIibB5dtxSiowtbyq9DBOn-8QUP0jqRF5Zl4zsdiyj6XchFHtAbACvpdx5C0ba28h8v8zJPEjyfmA0zlxNUcSMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LS6shhlLm9osXRGDcbq_hZY_ny6DmVq3dTGwmd7RcqL7iI3uAX-QVWNwvzVY1mamXdsjDAR_NRLVyywD_DYWQuG7ySHFvqAdWyT8k0TakX6OE-_wkcqqUX0Tdy5nfaP7N81LHs_Wnct7Yxrr0vZIG42cDd5QH4u89Xn9sC7qw_y26Kvf5ajD669mGAGQUvXMfYCi34jlyK6FBHx14MldnrhQyMXzqpt2095xuw-0-n2kzmDI9hlYEobfQvWaf_s5jNgpMNuyrf06uPlp37enQrC8ZFCfysDBRQtH-JUFo2TOSQ4GjLvAZhLCxhTjcIDNvIHmazkU3cghPO1vO8i6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZyUn7nkLD1Ht-jfCJ1_tEJjLgHy76vpOCQTqQJL-o6F0igitdKV2rm38VpvRuux474w3K-dkVU3ojKix_xlmRyPBuJhvWcpHY6OFTbUu8tKQM1qVXbEB88ge1s-nt10jMwTuTa5j0kQAuPYMv5us13qTf8gZEbYAI-G9fcqwcUgPvYi1L1hKrvxp_rtoK2FX6x7Cv9yUuI78Zh31_WtKrGVZrxdyARy8MQpLymUnO2VivgWAjWNZN4JOrcVor4Fita9IzRVKhlSCUV_ie8uszU0h2C6PkUAxrO3o7Qu8Z_FQT1mnvT7iuayA0UPgSwI122EsclcryLB9ZmCmTsX9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO6qY48y6vY5fWNk9co-lReqrfr6rlnvRL0LGYSQZXdTi9iDxaN6FZftbYpdvsqiyjXUQs9Ph-BL0_j7u2apuH9YizCODgHBU5adEfLv2halWKqguN8Z7daF0vl7cWJnwzXhHd1k3b9G9DANqBdXpV8SOYK1IVtU4oN60IAaiijddayKEAMc1kUcKLO1iMF0Qmn4jCgETbMNkt6qsuukyqHsSrWSoLrXh4IsUNg260MQEJH8iDt3nwZPMMWM_EnQnJ7q9SpLg1csEm7CxxQ3O6Dxl5aC1lE3zNVlt7xr683fD3PoyYSyUuIBrMYTi9K_eMyIG68Btp8t0R4AC1pZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 952 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuSW1tmSG1L8C2Z6fkwf9Ufwh5Uv4rAuF7PKtCIIJlAcrDue819yQaQwP84H8MK89EpdGsCGhHza9N_V4FtZcpyLf0pv8zU--c9QeU5cMrOTwHCgp-F0cq4LsY3fUrxNUiNNbo5XtDtiRjOXNk5kFUYrqaStabLDlh0nBUSm-klFRhk_5dDdi0drPNMXeEZYL0jJ2gnwJ4Va65MUQpBIMoEzWdv9Tpqu5kIOCgmhyHzrneWB08jZPOq3FBtlKQ4tWa-v3SuKbNFmTAaz740qHC1HdxeHmtzkVUUIV5xxeGMLnEswS-Vupvcnr9HhGAjAAZGs0GucnYWrWfIYRCzobw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdrpLogvsnPwu4HZJ50iTgDXmOT5xzlGpyy3JZN20Glfx-6t4r_u4NpHjBD3TGZPoWjFSu37oCwKb-4WAXaP7YQTP0NItbJMclLGeK2cvH9HIZ3LUde6tPzGaAc-Igbf3XZPR74gZqE_WZnpd_AUio5Bbq6SKR5B_fUcDVSDU3UvjwWu_JAPpYSQIvqt3FYMno9SiauS5IyXbzWAhwPtguhMRlRFRx2trDSp9hhlBaejQC6qktmhKB-b3ievTpZ_joODIIDcFh5uoHfqdwIUvLnRD98I7zc70ro7lCC8bUkTy96Low7jsxtB2JeTnVm0FmvD0ACQx92HtvpO6ZmWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLR96xX2-R8w6yJOdndZJ7Xra2w2RUw_F0qwae1c9mAxduT70O7S46ax3wvV_1pd6TEBK0K5345AXDmI6u63L2unbmJAVaGzaEdrNyFNh-4WpFpUo2UtaLyYeaW9Dqk-c00FwNMYlJslHmcJLTj4dt80vphpvoKIGuUwNWH2u24WQl5CowxE9OdPNtTHHUC77Q1DbhItCJbeNEDg9L7KefV-yjgayo-q6TOOZqD7qBnAx_TDc-jAO78GKOztSE6bKEjoVdR6-kkdOtZ_mbKHa3PWjmWFn0dvVgTxwut204RQIKsAH23zE7QCKpZ56DXIw79SGwLTStDVkq6YBYsDmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyOh6LM1fURdJmkPhM1JSiTIMd1j5yyItf3p1FbyftVyS428AcigvM5470GnjRHEj1OPmVFBhv2QE1SHwJxaNUZvs_0xVpZY-Z1NIKbiP8LLPcKjoAyfFoEA40laqPeR-30BAAsOYApLhFJNgtGKUYzyJ0_QjWFvzXw5GQ3OL_HMSV0UJOpeaY7yz_c9W5aQ7BcFpVDQwRV-fmrE6uH5Fn5quYJI4TvnblFPvNZxR9umNiMMmiXQUn4LS05LS6UmxeQogmYq3expi0jIf10qTy19E1PGtVCwHBd7a0nt_ahhJux0gTNPIsDNOD6KwCDIRiP8QAHts9cyvH3XHaT0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2rpxAWlNMRH8evgEDC1NXZStNarhwhkfCt2rKEI2DDfMQmGBup-HANISHma-Qk__JipoPkB2RyVxzgeJbjhSY3YHYdgj0_k0kkE3aH18twr97pVTTrHc0qgI54Gb3Q9piwhB7i16hYLDUdTO-SYhCYOXe6UEr0kDfVV8rTnARBwDQonI6gnLrfgsHSlg4EEFdKPt0JZ03BW8jgLrgi0bacflI_LN2avqEe-4n-I-hyv6vHd0iGkZY3kibadlR9eEuak77wgM9r_HIkQe1YTe7CHHkJpd81nzETH1tY-gilG4qVr4sxO9JDPZZn3zAzp6IcajjWBOEaxuObmz5yAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuLIRazk1tb-prYjkuX5ZF3YpzCj4dR5YN0jozVOXKrAz3gKy0S5Fv-3Z9zq1a5ZKOftw2HWRv8hX3HBAjCaQZn6Bsvkkx1vG7_c4AmsP3PRERoB1pKUHEPIt6Vywcuygw7GTQjtUwHCHXO2IuI-rdfdxFyVrAbz1bsNzQ0I_cE5t40wnyC5_MK1czlp7Ni9ioQ9PNc7j0agzKUdfnkT_RXXjux_CHW2EwGmVZXhzmAjTp-UzVi-l9RMFEocYpevDuy8R6-GQIyzHn4xUnxYEVjjKc6t5KkWCx2DzNBprqK6C233An7H03Q01OI5hrUO-ZzLVFPY-y25zYgTLdC5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I62U_SI3WHWD8f26BcDUUzs8TiNbm0ip0Tr4hcXRcKW8mG11xZqXus7VqstrhWA9LLPFUDaq9mhsqT6XE-qI-y9tr4BICRO0hhtyqXE0gZzIxcXPOIpPcL5hq-w1aqsWOcISD4Zw2E3O9WWoPqVy_WUMcJQEYIP-d7PSWRvjhFxJjAMO7QBqKtEru3WngAp6-v_vNZPcjHrBu9nHY41nJ3TjFzKfzbujf9tvEv5oNkl4z-CBOYJq-C-MY4YNqCHAA2Sby_DijxIqrqmDEqzYXN9EqU-Q_mTqAGssAhoiMpKISOgIEIk8CDqNr_scYUse1Eul8KaM8lKmdnH-ZblL7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_OIJXFLqbTDUG-NazkliN-rM87Qw8OVFB9xULX4AfEbfPaa_Akk3nrvmpyDRVhkAay1TANTWiJiMNA5Z9AqixwIKkNJgB6pZDkMn8IevT-R3kD9LPLeWWxArZ437gT_IFTxB3fPmMwVhY_8r32LU1nUkWlheHcRsLgDnC0kE1PIf31JWER9n91mN7-hvH_scgoR2NG4eTUZfL65fux5h6Ci2WT6Ue9JmA_hCp-7S-jGK3USHqZ7x-2TFmAM-SWbGU41ZZkohVigZnF7mlQZBlqBWas5KxuRso6_okuvJcec8uRzFLHqymeYth7d2Xg-3ebPIQhYqGGBkAD9vXZMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=l67Z0bmqO2JqCrv7AT5_TO5Cl4qdOC6Mz-X03EFpQDFOveMBai5kf0xBfKrWk-mpC3YPtL6EM1iLm3IvF4Ga8K3sFZkn3-HkAc9hcfs7HKCOCGQ5C7XcU4otWUpz43EyrHy5YDbCCeY5kqEW3OzEAJdQkNaWWXxiJLeM9-A7XSZSpfpnPSB9TyUokp1htvRIYSNoWZ8c2hXKH-g8nQyYZjXxPkchL_xUY0RAumcO20envyar8FRkQUmuVJ_gg_1Px11qH36GKEt73XeQNQGintd_zI40B1suakyRSsr63r1nKVEYAh7GXNdx3bI0764B07haiYxS-tZPGCMs9QSo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=l67Z0bmqO2JqCrv7AT5_TO5Cl4qdOC6Mz-X03EFpQDFOveMBai5kf0xBfKrWk-mpC3YPtL6EM1iLm3IvF4Ga8K3sFZkn3-HkAc9hcfs7HKCOCGQ5C7XcU4otWUpz43EyrHy5YDbCCeY5kqEW3OzEAJdQkNaWWXxiJLeM9-A7XSZSpfpnPSB9TyUokp1htvRIYSNoWZ8c2hXKH-g8nQyYZjXxPkchL_xUY0RAumcO20envyar8FRkQUmuVJ_gg_1Px11qH36GKEt73XeQNQGintd_zI40B1suakyRSsr63r1nKVEYAh7GXNdx3bI0764B07haiYxS-tZPGCMs9QSo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U29Fg1184iCb9qlhtI1NA8xcw8mxLcPlZfq_J4JjDS00tRcF54NqJHnuCX-6kGxW_oDiVTvZnEIirzLyo2BMueV-_wmMkIrM43jdR4bQZRS76U0e2KQNNPOBBF9j28yarAvGyIFB7TNk8LYTsfgdpiVO1TII_rF2jUcePkl6agEuEM2PV5NbTiNo5Xbd7mF_45J5V4_BOw1G4AaA5gbixFl9VPyleu3GTE-x0vXlJwFA7cSKvqsmYQujEDbl3_BCpeGDt-v8d13uWIVwim6fTpfG1CP7RQSzcl-vfWjkQUWTL2QLqxCmBwAA9qIZ_PfMArUeRzrf4v2ei1Gu2G8zhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9KspocTCS68okrf373QD6wLuYvkHC6tOy1CrQu2Ws06f5tUe-2zuE6htbSlOX1VVUvhodMsBGTNwSYYqvKst8yA4-ULpqs1uPjghgGV9GwEOsv4GrrFdX0cp4_PAafDQ_iBYTgCDN7zRFk3xQW0__neTlJDBKeZBFXHZX82qbRELDhqJJhElDmMTPt73E3xBVTGfoK9qUdtv2veSg99cNY8dFoQy6fRgRWwwm9zmD1TInxQ7jE_DmgwUdbj_8tw3OXW0bT4dwnfgO_K6VeIEJCorARjjGFbcKLWlXz7UfgJejlYoV4iCbUeMGNbpjSCqgMsEdb_hkuDdFXSfSCqiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1fRdE29VDUImhddAKnBKNS_XpuDILfFMCh8QPg9bJq1RyQ4g8K8xuQ2xjjMc-MhD3hTyI57XLOiAYQ0HJeC1vU8LiBhUDi471mtiiEFmA-JDR3_CfcsJAiKGeRgQ7UHHWGKAqIRmwqhm9jAstTq1nyFkZvJPmMhPOm9PtgtqjZ8ZmfUqhenPLUjmNzDKJI9jzCMBUxY2qdXUxdqf9hx0UGh4nJNx-5YR6NC5PCHLHytZ4EMXBFKuJ6xAjIvKy8UQy5hNt3uento6fSinpi9ZThANAT3P935U2fG_5-2j-7cgeuC7Sk5TPZb2tGqWKbUUJxubmFE9V-pw8qHQiEXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUta1pWdHESRAdWk9gWZVFQVOVGOYs7nB9wHEPONJdXutN1jQbw1q2rYfpdQvxKsgPcTtrphvH2-3S8STx38gTFX1dXSrXymCp-rOBAxt0TtoVI9kJVXjoKe1Lc0hTQb9yxCUtjC5P0rG6Gj2lhTFt5bjsO00VT7fB9dgmSvlZ4QjXixhOE3lK-MrJ5t6eSaF2WjbBrIrULshEdZkiDzLssntkZZLl1e4hBzHNZj3y9OUOG2yvbRfRum2wHHLySIYlZTNzBUEFeE3rbrjLTBeUskPE5NQdqGIiS4zNyQRivelKBPCbBd5pJ34Uqb2LDuL4fPbG2__BRmbd0-xLZboQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc9iuwjXYWZc9whu-gEv0dcP1bkC6aQSFaT24qLbVsFchkzx02_xq7TID-IeQIJ6NZfOpacqfPa7mZmWaBmQzPU-C4jxri_Lcz1gRintQI7L2p_FtAF50It7O8mjqX_v8v_r2x4eJSjRUJoDQqrUUBWYS37L8XfsBSK11kX4XfcwrI5M3zu0Vp-KDf9XiFMoZBhNj4_GnRT71vs3pm7arD8tR0wV63ok8glAXdunDnxhL1wduO0P9ev1BboBdbZTAy0InrKUqWUzrFygBjNbyMs1CZIuwwf7_J6u-yhISUKcxCpLsv7R_VND_cWKTQEvYlNLGKZD600fCoVv4dBFkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLfdYZrpOY-xsPb7OJ0TnDks1RUz1M8-gwIgF-EhzXUShdrclpNGJqlKel7jRt8odiKnAAHj5SiHHHx-0Ez18sxIiU_-wsr8tX58rbviHTLInPQBlN87B0CLLJrSYzFqWZ31JDHElid_tOqaUZq417JRLcOP6fWk0xC08wE2mIxmu1OOCV9k8vLpZnfFUqZI9se0AHl9n8Df2SLv5GaYPcKYWc1hmBFk9CHaM3AY-8BmvioRVDw4q5_7PUkTy--3eXlktN4tf4atPMep2mGS47y-LJnPWMTcOxmpnbmZmo4PRC6RROqnaTHNmPFn-RXH7Bh7SykxpXKm1dWvomAkPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMqHYK4TZf6eiklhukDT_I0MqCz7fPFh2JvPGqN_LJnGt39bnNOt-6mM3XbEF6yLSKS8myUe7xnzvC-SDgQN-wsSryJeLJ32bbYOHt4fW30uy_VH9po1yP-QB2qeLneZd3iZ7VMQC78OOs6QCDGoTqaquJgGJHEbNxpRztcMgV_YBRCchCSAtFu4pSdzugwKxQH3MMKY-Ad54jTvHzIfoQkWLWCszLnb5m4K0P0dEaTuY5-4NITHrb7yc45wQhpfVkI10b9oh7GzfFmdenwt-kbwm4ow0OPyCURLTBmlpYJbTKhfNe9Y6f_z3EUlDmxC_9s1lWpu-UW-bHDoheouug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWM8NFDl_bLtuvlC0xd0fBY8yf5d-gk137NiMlKUNxhfTpbTk8vTG-ToEGaxmRcHIbrztb2DkJLGW3UPK6QsjkWk-yVm9pbEpWrdmfGPHHUX2Cqy_t1Rl2_nPfZuOr7XznezsCDqzdDFhc5T83Lr-7IVtE3UHSZY2WPvdkIgzQuYlEB9xbQcKo8IKYDS_-ceIZubRfDwpUqSAfx0j6k-_TQ_Z7A7W5oiFx8Jyhe7cHz5BtG7L7SEULp2UsfXO-Nh_Z-WS_yIOwVARiepxsDNBgQoeI5DKm92ATCqp6EPRRsEnBden5GugpC4tq7lCffpW5Sx0Gs9I8BOBE1qhZO3Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPvbthyLWzu0YJ7hI0C76JhEtE674BPLBRhQPrCCjKwYa_1ONrIRWL8hYFsIToSTW38iRlT3rdRf6ze8a9TRGEDP30XI3SUv6u2aLxHYjM-AsJ0-4W0y7y_zJ5-lW5y5sx1vtRXnpY0qvKRnTT7wgfiKfTbLa8vBTw2FUNZlZZseWgYXZsWK-LtiZRaecpSQZcPjUw7yymZiOvY3LDKO66QrxKhe8dF_IjYTTs81t3M1FkOpxWaf72hzmrPrG2Uvw_bqR46NtJQObdWdUDVXYlnalwmAqgRdnk6fxXck3SMW6NdtXmDegeL0IujymjrjmF0YAlT5DVUz4rB-_I610Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3qQqSmlY4-ztNLpE2eKzuQIUFsBb4gtbZQyeIMc2cfhwa_wixgPdASAb2bDTJ-GERhaTSpmEeeFITtnbflKFFalW1c90eAn_LCtazrLUNt7CVEJY04AanE6iSrbHgtG2PIVDiqJLru81q0fvz3bnhl8vNJTV4WN_IdNebDvSk3GBykgI4jFvkIspjjtHflCfIXxj2UTdiM7Sr1-0jsqh31bE3OwHIm-It3CCptTUXDKQH3327Z-G1mYMhyuLWd2hOX3EBIE9C_7lEW1p1nyA7gN6trcvaX0xe5q3lH3sI_y4EHlb7naqcSSQuAslzCGOoCcFVfTw63oKkGI_vtYXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRFzij_3-95agtR1wcQ4tSXAIkGAIeqsKQBcswzL7Wk3s3iuF01GgIst8zMQsmwAYcgbcKmlxF1u29KFeYGKsjxEDgai2ePuxd2gwI019C-Rtbdxegiq_CXwOd0_jFQlVr8O8APnsF5I1CmsN4faIAE6ozcKlz7g6FMtTcfWP05QqqWdY-_2kuVVf6yNZe1iqbwjkbFfLwXjnxlLL4fXIIsJtQh_qRT5IJJVxRVqYcrtfpzhAP5Q2jDUUkQXTI6uwr7V5O-tcKyAzVbTjVGNMsSir_mDqQ8vKQ_DR0cDyRt29y9dsRwx4dG6UAcGxkAa28leAtp33Dti0_JTLxc5aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6gSk1L6_FqDAUo_I7HtrT5eEBCGyR8_M-TMCatxqJNFFxFWmgWr6NsXa28y8i1b5oMFv-Jyy8Na1HbMqzpULNSvHvIEGf5EXX9ZOKK2BR2ajczXhPfNi1abXCJg374_HZY7j8_yqS7V9GfV-92EWz6lOpfdND1dUnxaVURZmSk1BfnDFUPlfkLvIF6cwQ2fpRclbxCaedBU0fkIZeCigZ3EACnAKyg_tNIv5gq0iEiSbgeFDtsGNCjariU2oxoKU3DAwcPebbRAwRi9kNH8atyqNG8luDAAzlYiLPB2L1ymSPFDV04_PAWkFZP6HN2MrX-UlRcOFCWlLAcFaVKwpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byctCLfOFno0qTc-ogiPMlhhWJVMLNw3ccCB6tTT0efAtxEVaRdbxtq1lJb0sVHXy4b-Ko1_EBWCCsNEV6-heJvMcticOCzRnPRequ74POsw24ntPDhiAGKOJgx1skmvTdPIPBs7Xgwt5GZWp97QVm1SvX8lr0A3H1UatYVXgntsB4Lp7mx1RuL6YBWQA-8ZWo-18fH8hHlt7pTkNywu3GqPK1MsyHElmTQCGfF3I5F5ubBPbWUn3B9lw0E39ReHxIxH1o_K2wEG9i5cln06Ld0la4rRbLeyLx0Khnul4HqRS6teOWEYCAWMDe8hzZyBeNoFeAEV4OiZ18sNautKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8TwFlRr3wLy-ZFYwx4c7lQ64KbvNAUVgU2dgoH7uOWqym9ZWKHz7-G0i2jP014BpTQFN1yWtkiUYOTo4OzhPYI2rQjEkR_89eTssYWgHuVyqRkblkfvAYWQfOwDG13Xihtyf6g7j49VkSAPbCR6cXQzA0oHAZmPgxbbZwsw2Gr_ucnN8Ch3Nm7RFHS0rPUYwpZBAcvK8aVctwm7d0Xct1JKGsHWcvh7qVAHRj2CnWFW-BhyLsj5_37w5rE1qoMcr9S7e9rY5by7x9oa5srIIIyPXeLDfx1A7raK7-U-Iv2TDo2JZYVUem0srn8LpDSmgowHHcZBRKaV2EXhyZtjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7ph2-y4P9UY_gNCUrp6wncyM4FSwDGT87NmGaZLhJwrWleQCvPemDYinxx_w0W5_YaKrtSkDBbQnV3YXmA7Rfx1tsblo_V9OdUiyVrYg8A2davTpy1Qxb6gidplW_VeKO_Bdfzt9HgubZ_YfYYJSDUKQQy0mZyRC7gqA0CVsKLMRSrlV7jE-Xja3tjiV-Tcf5pxyEiHsEi6Zjm4z9ZmQnt12s1drY_SUyr5Af5l1rEMTZRa0m6voiD_6xoePPMfnd6QAgcAcS053-w8IA5li-2eR7qbTkXIOjlbL1rRE-2b430t1e31RfqHRe919tnltyIFKNTcHghbS5R-iUfG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-pORJ7S8Nn4OSXC_VU6b-GhJ0hf2z4bbFAzGJBEfQH-kZVV-sFnYoAdK_Hb3EFYa0BeaiCRBjCUVzGR0T9AnGeJ2MP3kWM4GgoGFY4C4GRTFHpugVf8LX9oROLPTL3VYWHkaGi9zqlZ3cm9MZMotuoFgZfc78N9wCchvMXBb3oA61Jj9U3LDzrJ8TXUBE9BeKnNugBA9W5QCZE4t6CM--bH1OPsChvng4wPEVWX5Sf96u7W3QvpgozgB7iFFRjdCrN-SWDeL8vosfpEW2FJ87722Rl6nqXL054GOHX4uzfFyvc2v7vhka6TlZHRbSygA-6rn5-zzor96fitHcnfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oj_2yy2wzVxC3VOHyH_GQu-Lmti8ncYcIdmqfq_C72g2Li2iaImDx5CSOGYwKF4SoHktY1uWlab-WCJbQf-SmKULllcAKU7HK9pgFfiZUwHCKJFqdkNkS4K5RZf66y3OtuQZZ0ykQDs13jCmEpCunbKDrAEPwUak91rCQUh3j1x2N_Z98ETTLozz36ABvbDfReJD_diBz9NpOdz0YkmBkDydK8t2LJ6bFA5J8yIH0e5CX3tckpbD4wNt5rDQa26_qvkKlUpJKE2arxDIpWE9Z0ExMA6qoL9IQwThCTGZM0yb8KYeAzCnr6gHu2muFaJWNzcqAavNbLcbVcMP84RaZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI3bg1RqL9EkyrZ9ibB-mAilAQKhJqFK9zPQsF9eq_PFBbyPoGGAhoFX8eErmp5ulQnxOCiJ3JhenePXa8XlVT2fq376mXFSf_MqxwrpxlV2CLlNMW8gsacZJjkXkJ2-T2QWBBpfnBH3R7-w1ni6c9prJBS8Nc_GC-OS8LwtDYSoPnX62XGQuTVfedkcpgM8_TpzBbudQ7eTerPb8Vb0H6nASL_yJLth3p7kpQ1AOLpdKEWgyk-uTanfeT3xflWm9A3u10OcX74l-JYQLWok5w00Gl4BS3MqeiqR52QQVK6S_HdNhQ_UGOCBoc3CJmOzBUGNs-4ImxlaHXWH42BcQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igXF4qlBuhk_b_GHXx4CbjgFGaWg2pkR5xSxVtmfBLzZqogEF4Zv-Jgvypub1sHB6s_jhucJUnk9DeABe6U-nFFJIKb7mxWAv1phuItDmsJHLt1xwFFnMYEekNfODQGWLmrykVtLbr54u8q4LrGX9VS9KIMBeK1H_rsWqTVAaQ1tHoaBr8mmrpTmJ5dG3Mw79bjgutRZWbHwyzQvhZya3ITxuBsPSh23NpdX1eySuxuHI9_i3pZ3vfGzULOGdRGIJtWpQs5sofZazmK3hx2V2ut153XuBTiFSMvvLPkAKdhI6f0RPG1fDBbNMXb1XtAjUpBe9yvRpFVyZHcnOSEdtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COVM736VTtSJP0kO2ZHtN8o-lg3UK_7ME9O_0tVnLpFMMjmw5CiP9zUV9Q18p5jW3Pwg6gKvFh-S68rtb3DiW1i-BJoH74mOqVz0wlCbe7NvBRrqi9cnwPqkDk-TV0m60DYewh9FYsCaVBN-BiDKRNxX1CGCCApARWolsvBcICna6QGrmTXCL_vMCnCIPlGrrzspX7QkuI_yxVhHeyT3ltBg3UWnAdmhGc6oSROh4gJufJbUbr6WoLi203idNxl6MPmSXhLxEqZWOmi2Ej9m7IxXH9CkoZ76PtMO5WoSPChta6dG16nc2OqhMhZiYc7X75aeU1KNvj3JSQ0G527efw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOk-jOjzLG3l-hIQKRbBmpgNEediyY0oDta6fxUEA_lNdB5AYmuASoBBbmYUxZt4n8vEbX7WmsVETjTycESmFspEosd7xV65el-TPaLC0KhnbApPO4ETjABSQaQE0Uky5IuHjaCANllt1_DKLHIXLYM-PLMb_xFjcjnLDwfcjfDsR6UcRg_GsQvDgd5xmNpoGld3UAMH6yERt_rPQ4aqapa90NpT7VIwcXpME9pUljAfL7MowpB7R0YSQvSax0fVecytM1DTRRHt3P-j-h1A-Qpu_QFz5j3KSVkgrruwREygz0z93w-1vMv8R9fIGUzK2AWy5vyJCoBqdZXm0OGusA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdQcx2NTd9_dTxknkn7ipdUoEKqeYGZ-3zSKqOkdg2GaSJvGtjXEAWo9YimpRzcj2mXl15cXok7p8ivfsxuv8r6WEv1sywpyxKh9P0q-g3kXIc-OyJMUsbFiicmO1F3sCR86CETCyT0kFgCwu1CFKBO3acEZkPjlPAv9NonfVhUg-1wt0FCd4MllnA1hvwTtH5G3QH0vkY8DVpcj5S7H5Pmj8APk5kV3rcxAP98drGLyRipdtev3LHFMawZoo7ZhJQFnv6LAMVGLBKnl909vQL58IGS5KwcKF6ncm8RYSMw5XcZ-WFaiBatCsVvPf8UD0bVRFHrspVthmyeibxRvXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRHyLW8kyS5EGaOGyPmOPXV6PSPfXf1PuILdHN39r-4RCzsLCTErV1jYXqPRl7fS2YF91-fd2TYiEPV75jpAoj61M1WoZ1z7zIxVwTNe1hu3-iYiR5_T4Tk-tdb3YpXsXZmJQXMcVRNdlBwCCElpq_2sTLtu6hrx2e4TTUn4F3_jh_QCQtG6RerCtbIDhgid-Ys4kCY5kccV8MzxTjj0EFdpWYEMtflUgHVtL3bSTTbAoysF9Ah6Nanx1zSdYPnHG7obeIqHYUiv8ifz1vpTULtcrXym4wEKxnNPrcNR5Sas-XAlkH_oRxfajkC9Lq-ibTor861Wxg8-aLC1kip0zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcYLSIR_t5LltR4fMEuakpk3UNMYDdSQ-owlAqAStB0Gt0D9c-K7eOVaQRUQicQ3v8zTc3dlGSZfY28mbB91edz4dDOtSmdnwLN-horhpT283nbo2NAX_8DXH7te4sKFK5iFqi-6AAzkRZXwEJ4yygs1mmoGCVTsE-Tkw0nnKaUmbVMVAxsJN1gvy3Poknhhc1IAJWBPwj7sujJXgNDO9q8B1sWAHAvbmBYqY3etnERFqIoLKlFq902B9hxjIt-9CiZsBJ0NffpDRiF4BvH8JEtKrw_xJazcARM4cg93H0-9vpCAFx-ZKiasZkolp5YmnRAv-YMS4Gh94sA4SF9EDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfpX3uk1YqkT9_d6c7W8K39lbvzp-xn-WPhRqewiucWFOvHRT2_0V8uDAh3Mact3Jo4AtTVq7R5Ri7XVJugK1J_x_QaPTQGVhuhqNhJNlnspwLqtdO_AQqr--6GdsIHZQLaN5sX2IrDwQhvfoCCTX3UFITRFF1cU20xgFtsodKAzbXwnOeC423BYaXnFxlz7PDF9az9oF3eLEFcguH86IMyyzUeiLJp-vis9Fd1s2tx8cXSH7Ke7KPigybY0rDJ0OW3QCFtEkX7JjwtCR_RD1UTwbVPpu-Ypdds3JjA7v1f6dskAJgbJ9CpQr72MIWZe2Z-fCJxnRgeVUNOnAtKIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sg7MxWhdExCkjZOcgnlyvKxXGiij4yYYss32HUtFj8t5J_1ijjUh9B-CTDHvwPPa1og9GUW4R_k75_RdA5jFEnM2yhF-x9ESMregUFq5fT6dv033Zvpsn3FJgpx2qd11SdbpLs_tUObi9y3l_TgaWCcWPc8rSFlXUlsUVVndsYQXG4FByNhrb2kPiRlfIYAYrGbNcrxf80ziDIByUiMbGwhA2L8mvY3hQp1dMUovnDM3YKlI1h6BW3Zd_UOfOKSwr0lYUR-4ZUNmCyBk7LIK3BixMUTBdB400-FfxENEh0RCVWkZH-ITJU9cmT-6W-pDFuqh-TImmn5Nd-DhgfLoOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8QxXhRlKe80s0g11auhinr7V6XGYM8apzZMe2UByOlToxNMo_rSjTukJlcQATrX0g2eUACncLXybwYsOF7CaQGLwUVX02353C2RgqV-qno7YbhpPbHK7Was7btlwZHthQ4kFdtKWj0jcFplxc_wb5GnWOJUu6a1fnxosHa68q4pLlG9L0aPzYqQKvM8LYl6LfjrbkjEGS4Z9sZ8k1rfXHqawqiwUzYiYNir6EjOZtte-S4IB5jNshcUMRmCUDclFh-YyNlIlpmug7RI3pftiVGSzmDo9xHLl2zP_te_ama3eqNEA4q2awcXMbIcDy-c38tzDlzfkqzZq5VI1cFYvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1W8HfEv1W7xnqSiZ7NLs3FdWY7beCGLQX4EfRcs_g2Mzd0rHQBeQPnsE739Is9C9GRJB22p7sQYIK0pIHMUtIPSGn9PlADOvLK8kNfshrribXSykhF_0_9SFfm7d3Uqolxv3FONJYNAzmI4CzymiqoBgvUIoGgPJn8myKjRUlTNRKf9RVrFfUAECBxjL5tIvDO-e04bcDOtC8Zif3zAcANXZlj7kbQiAUTsC4BFqNVB7kmSxoWzCPN55zj0glWnoVZRPvy39vKfdXeuYatFQSjwBJYvenbGkBuVTQtztN3-lLiJhvS22r1tSOFHjU_5uUuvGtfaqwO5JFNq4fYULg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV_ygxqdBDOYoWjJoZlB-IQNlhiKP3Kbqy6MljAQYXUCZGcGTvK8WdIjz1u9LY_egFSg0I4XAhT6V17-uRyetcCiUomYXN2lrZ1BVyOe_Z00U786q6zKBJR6Jqj9F7xva8cxCyZHFuXZJubRe4cpDQjvDk4SB4L12E5MJXaOPdfvelbHSz2bIVOUGSBTf4lawBcXqNN1r6lMAKVKpIDVrGJTHV9QU14lr61oxSWau3yI7BkTo1ss_BQFW4FLeLvS6aWh1U5h7-lHodbMnMDw4z8cb00aXPusP18-AUTisvtDPCPgvjAVGBA3ikLNM2j0mi_mmW_Ra-O6svEjuZg6Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwm8GUy5jf-qj76POgrxOWfXbUE3DaFCKBGJreb6EDpPUt9a4fWzzYdzceCx2YJSQ_asqYjXiOobaHzmz9aHnB3L5RIJq3k0F0PfLbIaJcLpt30NS9iE3zEPNKCahVamiDDVOd7pUnPo6R03sVMe4EvX7gvpf3a8QxgOOUrToOpGy_qrMlwEmyDHqVj8kIgPIT2vAt41zI9wWOVCrARbhCkqPe7XRhp0hY9U4tOW6ZjQdCSgqxgzShLPM_75ozMMk4YT0ICevJ2FNExrivOyg_xeAM-lrueCLjImr-URuFVCzeNoULFfS0YeCQc1MhAaL66nGq50hEFZZbstGw4zPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXaasswWQW7Pmtg0IhJY-bhANxVVqy9qBNQgdHXtFXrui9IkzW2DkZhnRmTwzwUrHHxU96VbRy-dg34cxU650xqPa2vAQzsw3mBGPWjtF4sjByNdOlY17_LT7hnfzm_ZIO4oDhtT8dNkhn245YmxIQgC6vIGfrlBEy6JJJYCqFb1pqF0fdivAVD7AO-ILhkJF0wbhx2yC64xnvt9ePM45oy6OnzZW9LMH7svQMW0koJ3OvH_PoBb8ePBI4W0WH9bD0sjoCBjm1YrFpF-zFpO2DdqClncP8x3hDzSsY8ZjmV0cJoBSzA-fkQMYkT3sh6btQ_hivbasBRetDvN7V7hAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhgwEcIAPK4OSHZqTPoChDu3Gh7k78GgLxuNW3ooMonnKMgBoUIi8E2XTqHV2jOoQzDMT7eO2JPeaVi4Gk39iGvz_QUY3sJBrioFFuyvHQnbIkMUiM5tUgW0RtstdwHLxfX-98vuuzLB1rpOFlufwyYfHb3y8bkiAj0oTPYHViOWlh54R8X4jbhFqgxrdqN06UYbSh4hbMHwhxAXddaR1s0_yAEcak-G9vneqhRi3kRItpzFk0FxPMfd9xWrdLpvmVu6LTdE_n2jKZ6tHMXT8kQHC-9CSpRV2XqvGV4zN4zTdKdBd58hqkVPB2l-tVi7V55cgjaswsoudlnguQIbLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOcZILq6g3a48qB2cTVBQnTGqWHSYThYEyptLo7oK8SvpbDt2hK8iNE2Ud0QJ0z5wFqZVZG0levp1M3c6Il3DbUqZE7A-4iq54tsR9eozniu0TOhncsWP8TJ8K0A8WqqLwbRaaNm9_qxbU3bp4BbiiByOE8yKP-wUfG92V7hSxlt4HRUHFCYSHzlrcIzabdfOxQQkM2zckeKxjDybzjmZHaatzF9HiYqEaM8zC4R94ASs2sGB1ed2Hyfd726wnCNyn4ayQTyb8G59Xxnkc6SLpV_MbpwXd8Da1sYb_2QMFC5ldT3tNL0_bAqOQQMekuXdq0tOb90DXkSnjWJBTA7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zl3RW-DMjCgxDiQcQ-KnjVs6aJqkqEve-hFhwqZrW59Nv6G9exIOSxquG7qsdC65PlOaxeiKs4OI2riJEAHFNCBl8ZH8LPmXpWCouLKI1LhKL8xui59bL169K3r5QnGXsjqznaazf89T-XNLE0Kw39k96JWnOcVy-tgYURjXrmclqPYDQs8bCIaBjSGaZVO7lHUY0cgenEN_ZnWWN2w9UUIH9sUvrEdewofepJ6hQvFJKpWayhKpmPEFJOoo-eylFm-MXaelOzdirzD8uHXzlKvGWzesmy10nBsAE-ZiRWyjpCq2gUwI1si56FIdmAiocjjhM-uU8qiO_Gr2LzHp0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZSM9ThhLsy-mp6G49iy5UsX4ItCHqFsUFIwBObOHztP52pxPMQYDiTc1h7uev-G93juyzTgadlxma_cGA7aiKjzQ4bqqDiKbUBqjCh6u5hwnf71beRuOBYsLLe4SsrkNNd5TBmT7BOgth3VSYhlx-4pZqZ822BTje1IzMKaMfZVkGNU4eg34aK9Yvw7pssOjHOMpcpXCqBioO0MDFLG_GQLSGpOlte2J1PvCJAuGhscYd-RRaMOFOIZBFpe6WnpPN1OnL_nmoIFjXFXk74AGcE4kfA8ily0WR1sGLf4tVmZmWwUR_gjh85sNUFAaQykGWqJRbRL88Fo9i7J1RVfaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udIBc6R6sunjc5n2WqEf8Qp-vWRmdNjf8M6br2DQ5Png5bKmNbJDjW2E3P11y-1KtQ8DaZBmkoajeoqVgEX5tescpBb2ZLuSWfCjZ9FcJ_MMxkt1zzScY0wLAoBc8uRiowrUIGWTVXCTJ_y_AxLkpw58WQiiYgPCVqp3mwlHNqCryrqry3eYBtn9XJOU6oWUo7S7k-wfm-DseEuuYzl9fXA9WKK03g8rSBsTYCkNxjyp-MLWTXSTNvRJ1drOgKa376cc7jYZ4YC5r46kTa57nPSlGSWhsN2rJCGMwTy4PAebNy9Y8MqNmZPe4JO9ZMqEprXSG52xJ9eo6ZyOXpLnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGbnErkJvAZPH0jUUEaKzZevy-O4584LYF4ZkfhIEGAvPgRRSBb7BWygWnTMEBtdxfRbrctLFFl8tGnQN-_WzaOU9YEdSx_U1aysWH5xxsocChrUrpKeiUgTnybDcNsRyMYOgz19pjBtYrt4nBkxZ7YKBbT1PlJxBXEKqNE0fAnLsffvMjh0YM7iQJlp4ScsqDwSfmyLOU3IAqUqoHDtUTo5-fGhd8vBBdtIbydqWrQr3rG0qBe-gObzC0e312IH_6wq1FtW8O_carE6JgsN4cndaMLmknKnQCBdreSGYkSWkgztvuSkIvVrBu1mLB-d6qGUMmvkw4L3_Z3MMy597w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miP9a1bk9f_LHjAKgxiZpmc5Eks5-8eyVK5xrnLzbCCW0KFq0yPE1nDotj9tCa2T8QYdk11uY-i_79X6AYwMdboaI6CcfEfrUo4PheHYzHltoNOqT2umOQERID7i9MLCYUYNCWeQReXyGeZoJQ4m6PE56h767PtnnVnzFwyYZFSX7Jh2bzFabvd116glo8mvtI1ehuUYPMKNOcYJOb2jnCwZtKO5k2oYKIp7gixb1bI8TnzRgtA8A4zyb8godeJf2oS8oiMop8HXf8TWpEjtF4tPn1dTazdsXX24oIl97X-7x3ZxwTksAYwowjCoOM36dPqymTycHa4KJAEvFV4q2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvGJjaHnLP9h9ryyFg5vsqstgCjQO9xN1_l0kmBojjns0MlzoPLqugUf7qgsgk3Y-q8MhmEP01JnbPJ913foZwhl_kPrwBzfhpU9_WxwXxugcgsSEC_LPFtvwnDehlo1L7nO8NS4THt9T4Ih3V1yQQE5qTKcamq5PHznOiAGFSVref1HBfUJKbsLOfL1lPuwsm49BjvUHCwveetpM4dUaK1zto9liGlaIAFefg3f0X1EnjFoQiSKcBjRtMRysdDwbFbQFhQipbHUx7DZ1Og4M9Cj9UND8r8qzHZCDqRJwb3XZ87Ex5IMpAjvfy583SmtOCXFKCaSKTFc65Z62cBqsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8EzBoEGbsbMjIBYvDtiA9ua_1tpe-5zRJqT9a0Jb79NwqfH2tpOjJh5EG-GBnQ51Z6oe7xMBf3RYGqca29XHQ4mjpWv88kSLFUsnrShRhIJHIyFTa5mdw5iNretI--s38X674198FDXdiogvaZuectY392XvrEiGtG9PbfXSBcrWOxmLvZIR8kU3tXSzoq0bMa5dXzfkLtga9EkkSra6C1AxXsRLbVNFVOakyexMZjqlS3f5S1J6AEoWVDZ4h02QVKKv6WEx7a4rLBXgCVhfXIfI4Vna4VNT4QackJyT_0ZILXqCDaKdsV8J5l3Fr94dH83rUcWVd_Ban8o_PBCsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku_mYTnm0PkvTvauX9NytMBnQafFFmrKdXjb_NKINxGifZbKZn4UA7hRMur8CIi4uFwEAC75hWC3ggNyULYbW5dBBHtySnAzZdWlHupgPXq3VVNuN9D3QAE4iy_u5rNGpYhTsDKBm-kMbQNMSb4ZjjlXCzIRN7PkD4-opRF0WnfxSGEolj8VXDXgn59nBYQrAqQC8vinaHaxNRKKnMcz58Wv5FozKwJ84C4j5OlBBZ1xZ3H6fM06OW9Jz8-7tpDLOVj99jrRQjn549_jiBkdWWuxOHhyUha0U2rL5TuJ2D69T9fwQbVwWmeqTZIC749tGl17htYuaSuOjBZRJwN70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPMnEl2nSJXLvHkDus4qiM8Yiyj-8-zcCfdEvGXRAocJXZ6FXO0SwmnstXb41gAldMq7wMI74SrEx148e3d0_ba8DB9oVuHTsafsfHrGUFnZtGVhVQOqYRidIeZTD6yWtKHogLO3Rrs6dpDdcgVUqQlHpfR731UI_bqZ2TCHIqKwx7-VSvVqoReIrLyTKzCPUMtGJsk03tQvWo3cN6yffSukXhkZZIDmtohSnZN8GcOoxysOTLswApS0ghhWd6HOtU9zlbGO2XqAqgMh7hq4HhT6FMFsoBXBRYtwmXJRpXkz4pXQKG_sFGmoy2FMhZuYMq1mtZakj9qbZvAqo-Mgpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoRZrKdJqEW_dy-IkTIxRsAEZQ4Yca09LAWA3Z5WgtsFbqVbr_hBtypuMgW4FNdFG2gg_3j6J0CO2Z4sE9BFb2H4A2biX0ekncaeJf3oJha8Gfi-t8K8uXCyy9km6514kW0Dx11Kf8jNg3dYeojyECQEsBENhh8IrlzZb-WBBKYkJ7QxjarGA9vCcCPAgkXLNH57leAuJbW8ukX_mFtaZ54PvirqggPYJCSh_g5pzzOOrI3uuxtEcCIjXZGvQk1B8walXj5zVN-YQtnDXIv7s5ktV749qUxfoXuYc3RFbi8gXNSvjdjgyNhn6hBQMZQ97Qcn81fK1yhRf-g87VVj-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oct45GvdOXqTKDp9KUvrybO8_AsoN6A9GCUYjcsHPz4LiNp_s1CD5zdx-ExQzh8k1N-FqIj_O4QPTsrWELu_vk9FGow7EYnWE07OhVz6nLGUZf1LhoT_-gPQsoMk4H1d5MVGhuXzZoArtmADZY9yDeSlbRQlPNFR1Voc2Ut9azxHIFH9jJcg-amIZEJTau41kPWXwoKJGGlPF_xTgUtvWaDtwC5y40R7Zs051pS_3psjQAnakV95D7nX72X8NnaXwY3ocfs-Gq_ekCYzvhRPmqqjwUylOUbFJfjQPZIbIOqN-YYt2yKTDUvMbfUSBbuCwufkToVyduEFVjGEuNziMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCIa1BBtbFLUYOxg-IuEqB9R98WospsziaPdWKHg7VqCl8kURKI9ic7C8xV_AsGjIMIXagGs67RaAndfXy-uAYtfbT7hgyDrJbR_AARN3kuzyErqUJQSwbFIhrAF0wVtM396wH7sLz22jfBTVpL-ZH1NPUxdoSS4nTzziCwrU53mVonhnxUpxFIIWQBmUIF3jlnGf_r__fJeqEHmX5Lf6I9BHJIimqUvy6fOgpywAmIeeXC0zzaBgli9RN1jUCmFPRoTw5Udo32FS23cDwEE_vLCCXMdV-jr1Vi16gjQpjTtnCjKc_ipxQUIVBiE7OBtEbz1RcaqIQ0xh9TfXWGz1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je0eB1SgA43xCAhVrApaZBX5ro_YbYUuwN9DQmYy3-QE05dGcocTBOU3uMPXX8Wre71bJexPm8fTQ5NGswq2M51zTmxzOi5DbRHFhx_bOZ_R1TKaxZ1RIzTHugvUAJHXePQyDJfXAu26OUZDminpQB4IH6AfuIflouvjjNGQXu4WeMeW0EMlO3qlkwihNnS96pEjgpa6cu_iNhvrho_HUIHLWj25r4DCVo7-oRSuuYSWbaa-LbDjKf2e6hz1ZHNCbx5K3SCuarTlD_RU1EQHhOG1tCYTEZOlnQgGvnpGvPz1ygcHOQvdZ-mQnT0qIYAWeKBOT_FiXhp7ZZ8GrxZffA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=MNk865NTYF8OZA4GlpkppEe3MMUgsV4aM7eUqnc5eqFeJJ6z_sVBLz7NZRdjWcd_7OfLe1g5KxqkD7fIvC2oxgfUM2BKMSn-577wdeHw0iIJa0a0r_W6bvq7OA4mJ8aoaB5LThymB4FgzxiLEtSkVaHc_ev8KP7-AfGm0DI-4gqGlQ371p_mG3RQfzHaWYDo8A8SDKmgFB0YvaF1U2S-UwMGa6RDFGKCKKL7lslL87bsiVdhMg0epvetvM9bROodGOLKNKVvMYFLR4S52fYqjrOufLuBL8bSQIeMpYnlKoxoP9vRyr84J0T9O1dF4xs-laSqfLgkImyHyXX81Ds1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=MNk865NTYF8OZA4GlpkppEe3MMUgsV4aM7eUqnc5eqFeJJ6z_sVBLz7NZRdjWcd_7OfLe1g5KxqkD7fIvC2oxgfUM2BKMSn-577wdeHw0iIJa0a0r_W6bvq7OA4mJ8aoaB5LThymB4FgzxiLEtSkVaHc_ev8KP7-AfGm0DI-4gqGlQ371p_mG3RQfzHaWYDo8A8SDKmgFB0YvaF1U2S-UwMGa6RDFGKCKKL7lslL87bsiVdhMg0epvetvM9bROodGOLKNKVvMYFLR4S52fYqjrOufLuBL8bSQIeMpYnlKoxoP9vRyr84J0T9O1dF4xs-laSqfLgkImyHyXX81Ds1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jqno4xuwjPzVaWWozHe8fHYp8IP0p7A3c04hu2PW2ES2C5DzW7Eu_x0JecrivkHVesoOoT7CZmf5U1DqEvbFlMSUa1q6ekpS5tTt_pHeEZ8YEqz7EynkVA2-OrbUa01uexsf1BtU5m0NO_MJlIQQcUYpfohoDiNWRDYQF4Wk8snSYG7s0vkVDpVs7WUxO6Hggcg-Zv59U2-zIp4EH4UASU8bOxthV13I_IzD88H9qKR3GpqU0PW3JB8NZk8eWCXjJd8iR51RXcYF04ePc8TwR8w-CQJvagCDz9zPGOUUCAPQvXHsIwVK4R1I2AWVqwyIVJ324pZDd5-7ABvMqG0Jlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R95mTqehteJYqRpEl1l_tqa-w9LQXozC0c_gHowOndfgDImN0_uSu1lHqJl0h_atCFRBV-EQlxyYwY4eItJArSPtnBCEVoNZ-w2tr6qlLe_5q17b8-lItZoGNdTtkmZu2-xpNR8KI5mZU4mNIt5ZAQSXMtNBjlClayInNGTYM0wbm1o9KCE3XkbLCQg_VtOx2tCORHowg4ZanNkQInUBYatZVdIPTULJImcvcIE1L1ah_d-pdy5LDBm960xzq1l5xvWso9YDcznhnxH2WNvuK9vH5p5xGX2g_xN_o0HyZ3OtfQTO0yIxTrwbhrVQOt5iimUwi-lZwlm-WN3LAM5DSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVw9uWmlNBfegc9p-S1XIQPoyhlxTe69zUCwX-GnHlSqi4KsSKdgSSg_oqJA1-Kxq0_N6ZXkqqw4RRy9YyPgwf-RyKIop_azwaVfs1Ztm5RwS3xSAakNtxir7mhC5cqux9EurOcVgooaC8TO6x4UJ1sqjis4ErfnQJ12aLCI3b0yroA4mihNmiePr9QpVpahNcpF29x3-QN2E0-TyYkTQNFwIQgLA0TDAd3JYBamlDtTBgDEKEZOQEq6nfAR-UFnloMpz_nfzDHeApv6IKV6bLDczanc6leCH2Y7F8EeOPQnqhYxaJ1KxOStGKpy9JKvFh4hPf8QzbwMzNwjxxxSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rExlJuUn7GWltcYAy-NFsjZXbLxH0sv96nPoGCmbffJ1kecyNYcIeY3-CVqP3AaTCI6jeUeqeAi0c-8_Pd7ERuIs8EZN0nWMhvlC0nFbnjF_4FW3j_JspuKLShTf5ztWBKKwushrksGeKc87pzwyBtio_g-mOUlQ-Q6E6x3tcbzLI3mvuULVToCkvmYdx8cPkQCRp08mTHvOA61JYbYH6zJFn9PWMrLLGzYbOtjmJGPedCHZ0ytvA45ABO7s4GmCgylpUq1lbfXEaXl2v1vYxvUOkOI8rgIlSjKNpydjUynyhprk0Cds7R5R56ENNv0WTeOFwuIvZ9e6HppjbtkfLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pev898OASuElE_nz-s8mN6qHefbyqxv3Md31cKWFqkDGFa-16XabdAv9YxS08MGM9ild91Q0flHBR77vDa48s1OnKu5m0TrNL0NSnESY65F0WdOBEYRhdNcx1AQsVExFVVbBiXtq4l2xyxHngfozDNP2ariFKxYJIKFhTVgvHT9hrvuIFV0WlWWKQG8-cp_UumMlLwbbWShPRzmTzUOKh1_6d8bazZ840K88DRURH15SBmsoxKt8OaYwF69gzIQ-NxgRI75ki7CRJ08pNNTgfIHxqq9ezRKf_-4bBoXYJTHFCr2vTnxZ_09L4hhQpi6zmtrK_enhp4PL0XeM7JjfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjd4UKXcS41YbksD6J72nh2ZV0FdVy_I9mCPbMgBf7X2qyICvwNH-B0VlriuC5haWOSkflp81eGijkFcAsTVnQ6jA8qFXA9BNii5Xm3b1ssQqqjcFnbtxQ24qBGmQbvSAlIBERWzGkEEh9LKEGa0wn8Ej3iDzndnShLIn46FA6sDplPcJEjFXy991enKBwWLdt0JpKmrAO5lywfzstsBuZXgqQFcmzeatsL5GD3BQ2-Jr-Er6uMoSeDExcQN2w2vIufDwaYVQJt0vVGSHLcdw47U__vj8xOPHt6iTYlVqHiYkS5E_rppcz2AL3Na5PDSIVi1O3AyyBPLNXWo9KNHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIC3d8_4NsSSTyyS__zGbvAHvkaWOYO9GpKLTXANv6CkL6JicJih7xaoHgL_wmb6He4ooDXR7FtwetZcnS2D9pGEQgkL_VaJ3NJqRpLDAprOJ0Hh18kvuxm8eJjkkBxzL0fgfiRZPPBXmPWKVLl86NgsgtJLnzCqUIk4QQxO3gGILHhHrBia1KtemZr8HyoI11liqOiGwEZtuVh1lDHJyGPQsMhpRsVPDO-wd68Ci1yILSDQ9tnwD9FEadef5iNK9EkMWBaeTForEjV9eX7rj-UfAjQdK1RxCdk2JJDdHzAxsi666TApUgJ5E8I97tJjIzEia6ciW9-89NmI2-hgFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=aibmolZLx9kQ5pQob0rJpOVy61ql4cUhR8T8XCDOoNNxOjJhsuZ-FJJBzsfgD2jg3S6RYRmvx3IDjP5qY1xf4VnchZMGIOYkV09Z1HRbVXAv-987y6mho32cfnaBylo_ec3-lBTimTBBzyKs5FSsFr8Od1g5u_3ckSsfWbAFZj1xpuwdq8EidUiV5sR5d1So0Rw38uYJC9SdrxonDStrWP9u-XLpHmOrH0SlWLK8rWAN78SHkcJEE8RQKtx1V92M6971iRwGCQ5VC_uzOkw3sC05WSOZthKTljokCcEWCQb1-3xI_dgvWZzNpod8sYBTcA_IzKgC5TIpVUj08cL0x1AqK3r0ybxYFh6QRDdgIRIGEOkhvy7XLN5os0strTbpkgfYcdXguhqNpMyH90Kzs1NFPFnXGfAxAgA0BzWT6IyGOGlPVBpzE6K71m6cQlnUDXx_vIWOPkDM8rRSgHVh6y7qCipwUdvgqdZigbwvkM2P52EmLNFUkrc-Mt-unSOGxm1kdKg-qI6LXWUKiQf4Cvk4Ai9c2N0pCdXRlJWmnFq7702i3IoSE-il4Xgb2Ok_0kHx9mnLLhZS61hOyUnRahUKILGofDUBhDBgFuAk6ruwKt7KvfjF1ryq903Xrtef2r8GQoMYRdIyjdDSgDO1DMrhyWTwoV045yzVuE_zIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=aibmolZLx9kQ5pQob0rJpOVy61ql4cUhR8T8XCDOoNNxOjJhsuZ-FJJBzsfgD2jg3S6RYRmvx3IDjP5qY1xf4VnchZMGIOYkV09Z1HRbVXAv-987y6mho32cfnaBylo_ec3-lBTimTBBzyKs5FSsFr8Od1g5u_3ckSsfWbAFZj1xpuwdq8EidUiV5sR5d1So0Rw38uYJC9SdrxonDStrWP9u-XLpHmOrH0SlWLK8rWAN78SHkcJEE8RQKtx1V92M6971iRwGCQ5VC_uzOkw3sC05WSOZthKTljokCcEWCQb1-3xI_dgvWZzNpod8sYBTcA_IzKgC5TIpVUj08cL0x1AqK3r0ybxYFh6QRDdgIRIGEOkhvy7XLN5os0strTbpkgfYcdXguhqNpMyH90Kzs1NFPFnXGfAxAgA0BzWT6IyGOGlPVBpzE6K71m6cQlnUDXx_vIWOPkDM8rRSgHVh6y7qCipwUdvgqdZigbwvkM2P52EmLNFUkrc-Mt-unSOGxm1kdKg-qI6LXWUKiQf4Cvk4Ai9c2N0pCdXRlJWmnFq7702i3IoSE-il4Xgb2Ok_0kHx9mnLLhZS61hOyUnRahUKILGofDUBhDBgFuAk6ruwKt7KvfjF1ryq903Xrtef2r8GQoMYRdIyjdDSgDO1DMrhyWTwoV045yzVuE_zIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPgIAq9ZUWPjZfXeL4ycXl8HgShUzw7opRjesThAw_8p2K2wR-98kFcZqVKMfXJZ0CgeaTlIz5ReIuBkBzSZFiy3Tuc2ybYSyL5j6x25p-rfs4y6yBpgnR2V_Wul65GpKqveua_t-D_flGTEoCjgYsthO6Prvu4fz89efjlJSC9yY7sQZygLOluxWt-5iYyqbVHytWSgEtgzQqoME1pmV_-lCOaSZcccF0HOwrjqmq7cfgan6pZexv0TqaqA2q4oR9_NvQqQ3Oh9tmIWrja94XIziBe4eSpiktmusrNk_w67g9XVxsME5CPZKQS8N85qHZrZbfWW249-Z8trV-eJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGDzJRvrfnuv9miwC8Dyd85eFjL3WnW5_mQM9qQ2Bt_sHHYhu1uxGcZhUQqFdERSQmKueVyEfXMI8oYnTQht_c2aZwIdPTcNU8yBOrweoxI_5V2HeqEWS6JPftEh1ebzkOY5HYMYr0NM3hD4q1qCpVjIrybx9FwP0Krjr4GeRyhqBMq9Lir_0LB_Lkpi6v8i7aRrH53eTm6DQY2xKHc-nSAJ-nyPp9ROh8UoJfbd6e3zeVP9_z0Ae6J6NpzFDKBRoJBBuUlfIzp2MEUr0iHvxFEYxUleFZk8LwYBQPUmlEUDqm787rOfvHLmJcJA4xUZaVrm49cMf5X7MJBm3-lLtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P42r2yY1BoHlCYft606xVzZedojzEVthfonuzuUEfDoPeDd1V9K1o4-IbrY1vmO70EV_ltNSaEM6VBtNLKyt8EcHbbOX88Clnw2hcf8d0_ejalOvuxpDUql0HeMH0TILvRm398lc8uxd74Cm74XRZORnQBct5I953XqA3YFtE9Ih_I1Y0Ckt4gle_f19R1fTrlHMiM2U3xjhU94KPD74dmVilJd8puI2dj2CKs8aZtKjHfuFgwc5x7W6hZEJaSt9bEIxtmQfYP7j1_uVcyOwER-sIv_poULz2fOXmPefe9Ne6acFCQD277rKvqnhmYDfsw7yYhVm-HgPvO15v7LkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oroFORe4IWKmCNBHqAE0RHuBVf0OKoUxEFt-kQNg-1MGS4h13MnRE_Z7rdG-7h5DeIkUUhgiJxWitBr_i7ycAR9fKs7zwaufSapAe1p0D3X5be6x-cLcBDX9rZN8gJHNlA-JI9lQ1slfsPFmuoVZZvjhbiINOgY3Vu0jMLsU1C_Rei7EBCCrISd4aXg4TWf2CWR-wf-bmWoV10jCKNhpmL3QzHGVNLjK_2Ec05fZqa5yddajsp037plV2bWVDe3QzA430jTpNi7KEIpEO7LrPIMLbTwW3qK9KKX6OtfijyMd29WQNJHch89Av_dqE2URcGVHaZiZrpsI4ahqBYItnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHoNLoFc23q3T1sSNATH2_NjDT-3GXzroDOxZnFegnX-49SUrjTfipPo4p1ifw8L8K2kXxYatvvA-r_wulLCYLQQEDaJzfjHnHECwQhu4G4Hm3fDquSHhTNKUF8cM5eLBp-jPwbBhwT2hESoqCIqQpjoL1120GeDeoxpcLfhPOZSnzzcP9UGMir8KUNEQII29kn5_sLn5rAYIbA9tUYdvUlu4hZoTBCuz9oZURjpOfiM41WdTugWZpsLnHRRbSPXTUfXJR3N9ohKInv9n_qB5ltZEpB46fUjVuF2RJD90kuOaOsSuC-RnZ-nAUehDIR6wE8tRr1MdjHXb5tcHan4uQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUarP_WxP26bUm3pfeKWXXx0l-GeARLqaypQJdau6r7l7BUmwHOoPsfNlUyhJoLZRZ0KZj2m9_w8a4pyWoiA_3d6bXXVM8mvnPZ1rKcNmQeSl0oZB2i5jqIw4dbrLFhskNP-LkUrF1NvFIvfDKNaso9Ooo9rAIHyc1yOmf6yPO2yPAosZZQ1Zcs_4KgI07zbaR3DSn-nifzJWQXroehyEA8uo7zbAr9hYp1uZSlHEuFPb3P87TdZERZEV6_b2Nm7wXHz6wxjx_j2i3rV-Adz1n9o6Mkg2UDT56xUkIQfET4h9LKLSsE1clzmnSSMFsnNXLCV6GOGlkA1lraO5F0GJSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUarP_WxP26bUm3pfeKWXXx0l-GeARLqaypQJdau6r7l7BUmwHOoPsfNlUyhJoLZRZ0KZj2m9_w8a4pyWoiA_3d6bXXVM8mvnPZ1rKcNmQeSl0oZB2i5jqIw4dbrLFhskNP-LkUrF1NvFIvfDKNaso9Ooo9rAIHyc1yOmf6yPO2yPAosZZQ1Zcs_4KgI07zbaR3DSn-nifzJWQXroehyEA8uo7zbAr9hYp1uZSlHEuFPb3P87TdZERZEV6_b2Nm7wXHz6wxjx_j2i3rV-Adz1n9o6Mkg2UDT56xUkIQfET4h9LKLSsE1clzmnSSMFsnNXLCV6GOGlkA1lraO5F0GJSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPATplI3D5fAObBHXW8J0e112wBw3kKOXoJFNms9ljqNhJHmFoJaveSZvKAyackcMcUOD1PV00_YZdvFn1OlXz5vYNV0gVZzgjUA2OPL5FmXu2u9wHSril0KLasevS5ZiYoSpusik7x54vCQF7RMUy36-GvnWrjBl3YjwE7MS6H62FK5fKxYd7US0afrr1seKLNpaeQ-aEOkaSbsejVMgV8r_d_IArSmK5JmCRNLiBdOSMp9MiwL-lVHMzV5ksk_sZqBZu5fbUdYfS3Ku6f9oHgg4gul3lL39ID-cUS5UL9fyspq0CK2xcTIGGoVWwIPobJYf2OungSLkv3MVXS-LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHEik-ihmPyDEcRIGUOm9s0zPCsQS_t_-ZdabWhME3t3W3-FMa9B_8BneFmA9QH_8VJSFHQtAD4lEHpWGhxj-Lcooiw12B4mrSxZlSeBaScoFVTBAm1OzvOHdgKqkatfP-_NIc8qfW3bjY6liTDgeRn8ERRpceH-dOrWlLsEgge-j6-SwYP0YjYo68Uukk71AnlCrL9L_SuRu0-nYeaJ_J252GGN1cxIaJXUMCtGF8t01LmPoRBUvQ3BqJBc3e1Z4T88eKsfCjVCq4rC9I1gEjfzDXaGNlwmmLDIQS6P_hMO8GN6RvWNLEkRCldL7kBzCiN7BKGFEPCvLqAc4gBfTw.jpg" alt="photo" loading="lazy"/></div>
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
