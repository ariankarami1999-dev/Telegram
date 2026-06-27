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
<img src="https://cdn4.telesco.pe/file/F6D5w0p8YVXFONO-yejC9IBYMeE1Li-GgxIIZJ_z4Cc0ukYrqpOOD_IMaEw1KZsRcydU6i7oRTvAuVgGCuS-vbxI2c_hzguvodZIDrP8BUrab2M1W3z1SeC8aNNKdkCugMQ_DxHSacSgf0RM_TnwVBE9HhS1GkIpPd_ovSH0Kup9rt2VuYSNPsDlV3ZWisnK09bGRQhZLxtwEGNjGQBSaxqem_f5xugnqKKLZJ9u5YB4jvbfyIDxl1nwTU7eh160I6q2mr0YNStj9qkaydaP3ioe8KRmy-QHW8LR-TgDXf2Lx_G0JhV_XbPmBdLTTneQqJ_YM2B6YexhsQCiMxraOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltn4OWJZNVlDCMP03buI4RK01sSOper2KZY4zxLBCIP-PpxVGlKMqDsoszc10XYSesqjqzY_H-dy7-NNiWja6XVQJ8o9V4NoOWQON_f0QXMlLhlcVvpWMTeGDueSyxBs5nO45jIuDEjRWjjOtCt45oEdQPrO8mkj1vG-ioStbVRLYxL9FRkGnvt04s1FFJ6z2n1TQ9xwElMjUZ-5XOmuLzA7iVA6RSpI5R7XAErU6YODzVw_nmuKDrIy00pHrc-fXtKzSvNs657xAWry7f7RpBnodbnbGP9XYBe47jx0SqsEk9TE-FwpJFln54OvK_gS-R9XtgZ50TClNTZ4WwIACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 246 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 481 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCSVjIhPiiCudv7R17Oqk41fk38gEjw7R3mrs_E85fQgUDPvxOa8AaqaDMvesgXVHtmxtTsLOjoqhtzhy9TfOXgWxl_9CA12mZhxYOQrsPKbzF2oU1tinxVmH9e_qwAncHybOUpbVrJsa1lM0RepV2fY20ox1DBsduYXF1iWL72CNewA6oK0eqrfSNbBlZK02NNywpvNcbnGRxNAb0U_YNn3RfdccFLao4JiPWV2jMGOVjUG3iYFeRRUAnqn8YtziDjcDbCTc4LAzesQRLrpv9kZo8UdpXPdh3_srpnz-XHzA-fUfUoncJzoegXeTUA-DhxZf9p_7DQXW7iRGjZWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 956 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnSLO4nPiiH_HM84SLLlwd8wHxtkAzznlnSj3hJJDQrdJfpBLZliUfjFQVBINHgJ3FLCfjKTtbdxaMcvN0u5AlIcP4BbRbUcAPicsyROgdjDeUWCDGnhWCftCZp9IpsRngF5fDZ5BWVd3B5Ojx_Mjdxm1bTUoyAB0U4zQBtNsFWKGobxo5aVX4epPnKGFa-mVVrAsnAQ87JR5JSC4ETvn4Vfb-H7PAqFO6tzJAQuX_j3FjvD0ty9pSiJxrP_Jb7A8h4r8NtcAX-7RwpTFICJ27vfYDBAK4cvzjZe9gciwjxL72f9dU0ivKibZispfr92p4su_wkPplwiKk0e_Jzs1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlWjg4E7EybQk9w2Be2WNQtBUI3SvmlFRn3zgl1Gs5wc4JW7xCvSg6kNYJikOLunwam3TAkOZlyY6xaVRt47bi87ZPbSoJQGF8O-cEjGGN2tsuhBd9KOBsfeWcVgUzShIe980Y4jAEoyFLIJDzG8pwkVM2nsrsXLDOgkJRUQjwpUjVpse_6hN4PKdW1TZ6fFGQzbdh9cxufqoO8FXqSdf3sn5BCUnnopen5wITJu1xi4XSzn60gU6Dv5e46n5Ggt9F2PzGQC-JLoJKy4SxDf_5UuldCydbX3hiQgRwFn_B6q-_7mfPvGMswFzo8p2QLhnNKqoW4Gl0vb9f-bxnAtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGXpNnfHZAcXPoBME6h6u5yfeJi87JvXMJnvcRmRO7EBUKDhQwnSlBGaPAdouaMzZBrEYoEEfIol42W4C2BDIhPcV3kqQET__oa5tfFqoYvYqChI-PtiQzJbG9g7Dxhjc6IFjlte6Cx2u80kjwqJGNDNVOIpJzRog6lRYXEJ1rhUQnYa1JiBt3_m6wEHggerLjkPl3atvHyBVX9pedPpQpJyCltcsC3FPD1etjHWX4cXqIFibA_sazYpLt7ZKAqupsWAHav7n9hYVLRvB-QkwoM7Jy8u5qmkmg8D4iFQp7S8eTuYprYxh7YU8NNvWDRtL_zfOFJZSGIpiCcESbUIWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI2KRI9JeJs0rzev-gIq1PZhp6ZKTYRlpu5mb8XJBVosNHO9y_nCv78OKejWZhRLGY13b85IxImmH9UdEVX88kn2mYBls43m88d-6mhShdWRHENgI_F6uU40u9N9Xqdmr9vgPBOjkj5rU6rHYFG1SiAQg1qDRQ1lPYRoMgWLMPyaiJDnNdvWrBgOrxMN8N1CMP16uGXJs24hk086-gO6fydAhKCcqaqg9BdWblrLw-zTf2ZKHBK7d91IZ5-HSNXgu4TAtxYnLKij_RHGjlnq26IdMW92kZYmCzWhO-ShBTcUTyxtus9FkT00Pv1FCSp6BfonO-kgWKdcbqU6WjQqYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-lxsGJlTSxDWTn76DXNmPh2aiVLJ1PKzmenFqBCHHjMtqWpdl1Q1SxvjmpzwdLmqYDP-P8bAM1pLFGGeDFTUqhgI3kTsVTh9EwPePbEiDKxb5FBsKQTCn40kX-Y_HvVyfw8azi7OeucKlIWvwIeo3HLeVIRmUow9nTgeCu_lkZ6YM0Ptf8MM17AZFCDoj4nrSk3FnHsMKzdi0eStdg9waUwqut_oJZPhm7tsKRwAlRXuwl9pPX0n3WWWDffVCAlZvqO_MGp4a4962CU0zasjQgi5jZnsZZrRxGZwlj1wvlaV4E0bp-OlBnU_3217ttx_cUXvbAIL7RnlLjl8tlChw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrFLknNSJ67htZQAeOnCn-K9V65NQTkvruqQ_w4NODGpo6VrkYJgCTQkYhj2k1InecJ07iYnxLiO0y5kbTUV1QD91e5uhmb3U3z_8a-kYiXytA6fTLzA4mGJVwxWwTIKYvlg1RZKWBzyHhjAJHNprnKzoPp1Px9d0gDECkWXGxo-gAFCNZVRndc8OkYrMz5Ty9CMuLICtwE2tuAZM04jbqPH_dE3ooQvr5ceMwyg0Qhof0QDkUg7aQ5RgTQoUJh1sfj1V7K6GdtuhPqQDcvcQcOSR05p6pj8o-4puKnw_pPhYieKtIWClwaV-PwF5lHuMeyHQ0TP-kjI8Vi3Bd8vyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkN9X9-ZU0sHM3zyUVRORqqp6KES85lnhGE8be1crkyHt9RZNySNxQZH-DkiC3XXsneTMBT-GJ3w7Gq6tl9ytUdSFFZhjObLeQ4baRaD_GyCIHmRLQMEVNCgHBJ7G8btm8K-x3xsXwtY2VmeVPXBPFO7ufoXYWTAKYDv2ujh8sL3ZJPWJSrQgNk21--keAZYUJKDI3zH5LqTttPjCCKDuuzNsLbBzT6HBFJ4eMZFUhGw36hfeyZB-RCRDTx_njps5MBp-Nv_D95y7HBfqg4StWUSPD6NfT1KLwBDo9ZWWELXF4nffRVSB_UWB9Bd1OpGwZI0A8_iQxjqmJJ-lRvxmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j37DwvAvsIeK2zQHhz_Gt-SXxq__Ub5z2hsiEvnzXYdEXLEg_swj-PrdbOHvQeE6bD0onFnMW2anWlk-TuzLnC7TidY6_axSL1mJm-j0sMUceVh1NXdY1qsMCJQnIgpeXKR7gWypxQAD1SXvLiz8q8qOqGI2vZlLdWdFSMmP19_Tt_Nmh08CcmGkkUm3yC5qJwkMsDzy4hGZpsTzqWINoO03pzwSIJo-mBCboTiFhTyksG8nsWTwAXJPLCekPGhJNtzEJ8kZnwoikgl-jPCRBW0Vio3qunghJv-GO9mL-vCrwxLQ9vmwHlkGNDKk9ycTmNIiEFg1NMpWlBaC-QkXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgbUwZwsjf7Psja3Ar_rP1o7SIdkOxpw9vZfFK6tDjT0pnehmuUXz_CXeKJtrzN78ULIpcVDHRjwSY-Cr80wM4_RYeRRwQ0NYSgs-78NmTAA_06nG-bjJaBqr0gdKbg0g7VoVoYJe9ZQ7P2bOmcy6_FNR3m7iTIAJAE1DbprH3wY5SOoCD-_MuDK59ExepxvpSLLlrHU9TORS3L6gd5h3aFiH5wTOJZWGq1AA1fFNRLWgWMTnW1OlSMfsEabrInbk6Q7oxWEKwZk-tvyv4wsUWz1JRLwhC70SpgRuRNTIbCANfU5FukIAnA_Vygy9gG1tTGbf6iCUxrtW-pcB4GztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMliQQcBNVPsxHOq05j8111RFXQDe5wELTarnS8q1oYerlALz4WyHs5Y9J2p2RMIWotqL7wpzDhEwmB5_ur88cdGDErTU8ris8XwmznI_4WWmGHcxi25swD10y5_ka59dOtW-supAF-X7LGSRvJSkxcnPopVaDUagH4B-EFG3EPFdSQgEaC6IjV7dstqi4bs8LdIKFi2LM-HBwlpmR7FePAS84uDPslxtYQ35-y-YzLLOHr7-RT53FVhKueMVxgLpQ3Gb7cIM_OSHbuCz8R5xmRAgRpohXA7aR352SlVDl3EStEEo4oZ73sBsdhVuPY0qPVR6baaRcpCpLWb7gWmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJ-4n8baf_SBT3sFXFbArpr5GkV7uFekiOKzxAIS4aq26RzBV_XPGTTSGtxrUR8krRPfCn3CUTR5mfEZwhPfYw1NoKqvUFa_ptD476DDchn4orCFsUe4yhpHlPyePdJnfA6ofb283Xj-7ex-aP-Velt1PBw0h9-OIivRRFkamrtdCsOfvEh8tXoGDDMNlrhjENehD3L6EWqCbT09ylgTcrcR4awFkxWLoM8rvz_hBpf9k8aiDTd7cm0VIHzKz1dw4k7QB5aERirgi-H6fzaq1BFJT967YwEtznjb2-e6jdxmDZ3W0nSZuQK1NTQPwA9L7GbrupjtSh_AkIRVsdRC_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTmnC8wFV9TWQCjrTZuU9i84Vk9qDC7UKbZBTpYyowCStPdJFDtgUVqskyj_GzTlfGypdvihSUX8L8QMeZYYl0oAJe6j8huBq9cHdySqd7ghAu329G1Oz_ddCrzgDnUE0jjC4VZ5KbQ7YIlOEYJpHItkjh7cr1-_igi9bh2RU68HqX_6kNsloNyPzwnmn8hxFaPgjU59DgvRQDJ9mHskXRX97XiVnUVllWKW9Sf8RfgwN6ANQz7q9g4vbVmRwSNbnSBTaNZjtUB5xp_5kyCZxMsIPxAhdy2Fj5lquNSBS3Oo7nE0GuZnrIGcMxSz_mBTdeKW8umb-hO61FKKKDNiYg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=IdTD5EnhUmZb1O307ri4ecFhMzscb4rqZrn5cJfqMSVhTX0pMBQsdHuFpv8OocrPrFYpudxMLgMSU1VIBP6sEC0Q36NyLtV1GFRqyXDErg13FwKaaxEtjR5dcHLo0_833zCqQKYBDpgfjao82HLpNDQhcXfLNOlJTdwyEr8in9l5Ja_kLQkSf_yCBKjlfTg0AVQyOoajUcT_gGp9L-UvFkwE2uktUNvnIxKruHrlJY8QSPDSUtbXFQwsZTEK67I2QIp9WmKqeuKckDIv4bzeKesxW9qgLd0EpcDAH344QPHxIM8pzAJYjCWqaneJKRAr2iyIZKHITLhVcHM32AYozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=IdTD5EnhUmZb1O307ri4ecFhMzscb4rqZrn5cJfqMSVhTX0pMBQsdHuFpv8OocrPrFYpudxMLgMSU1VIBP6sEC0Q36NyLtV1GFRqyXDErg13FwKaaxEtjR5dcHLo0_833zCqQKYBDpgfjao82HLpNDQhcXfLNOlJTdwyEr8in9l5Ja_kLQkSf_yCBKjlfTg0AVQyOoajUcT_gGp9L-UvFkwE2uktUNvnIxKruHrlJY8QSPDSUtbXFQwsZTEK67I2QIp9WmKqeuKckDIv4bzeKesxW9qgLd0EpcDAH344QPHxIM8pzAJYjCWqaneJKRAr2iyIZKHITLhVcHM32AYozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izqGyCmgyey_c4KY-V2kIehi0GBl71PbTsE5sQjcAB-IIrWf9R7ZZqtwhq03v_Olqgai7sqN3KfrZmRb6HTYSmxmOMkH3h-8OGJM5_hZJDI57skAZGXfcGrCvDT7u2yrVIwdp2Yrk8PBBk3zpaMkEVJ6dJ9WDwX_MiPm1-z9Vzg2xvySqkF6jwtEyha6EpwHhCeKg7yqAvKSeSSzKVPhYZfwfDPTsVO10gMXQm4__DQrKxELFV5HHT7tzwNDzC7Gf6iqY_Q3e2uIcWdXTJCWHQbis5PPNTk9XajhTsZZWcVoaSV8fnxl1_FqvwAaX5hJUtGPk6p0SWCdM7IUlWM0WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4QxWJp6vDII2-6HTeqNFAj1GgrURZpnhGaWxstV8qOUD187Rx1gLsq4iqlrq3Ll_YHvdsXydsSJ6-Zf5BQvpmtPz7Ld_nfmN9y2XjftFiaQolYU1qYsY8TtboOMI-yS3BXMIBo5sfQY8Mbs8jqbthcPRwggC_RRFK3VUqz60briMH4Uc82ve26SjBV_pmii8QvS7Z5tw9xu7KnkAMMnJtT00aSfFL1YTZ7e40o21NyM2aAjIjlZopIPeE2lsdkjRD6MISHSW1IKYtBpczztLF8r-6I_1_0WzIzWffLulSeksm4T4fTr9rhED4Vn3DWnBf7Ti-zgQPGxeWHAhmniDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XajX6CMrgP8ZctqDW0dW0AiKG-qDzO1tbMIsFl7hnIedgR4dUdUD5UK8ga5VHX2zL_LUW33BIeQ86dj-9Zrfl4OC6Lz7LLHHBaSm1f2EhK-nadLybUlVonDq6tEx50ZsnKZvjvK91X-eXsVBM124h2dv1Cjyvccgml0OQAHsvCUKDtJ-tDXMa_lKzIGEVfnJi5imfD_d_VKUO3gAasRJcFV8yVzCgr8EUKsHShOj4ao-iy39t-hX3nBGB1-j3Z3M1E9PI0SP4LIHVTH6MvFI3RgA36lUUCyRgmcmpIblodhCniDNMAItFCnhYP-03f3i-KCfpSHJPMUYw77wFnBHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSv-TRLKri8-cTQ94uaVLdcJDkrqwhfvso5KXAOZSwag8bvgDPW7IA5JpOCEJ_WwqW8o2LTBgRqcAbeUWeqTcZ_w_TOqiCfEDJOB1drtr9-mZFRrsQKVjP8RTkcFG6g0wYuLZm_SDcCbqkji1TYjfsERBf8GcqC5VjYoGofO1MOcVmr5doVx1_GR3WwObpgm5SczN1Q2O3DVJI8-QmwOjJKraPOyXRPSE-nd1-2XWnqkZkFm-c9DVTSdOYnCfrrVOG6swFVjgUQvgkDTW0durIpayTNBHdtb0bwA3KZw2SFjJTrUmIQlJCfh_qhW6dtmPWPLL9pTSU7x5Pq7ADx5hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrJh0h1s4NdGfLgvwRGsSPnZwx44oFTbNG-UjFzsz-8YRvgHByNhh5okxrOLspuENgNF6fdlDi05ho1OIFtrrJn37CvAKGCUJWz21R26huKsZyqmTfcMf1AAn-Wc-TfUCviyczpshMIx64yGzbX_5p40bznbTo-bdNm3WuhaalyacSQewEumFo4Mb5Rj4TcOpyz0E8dlrN94XMCw14QBDo4lqBL_pXRe5lSEnw88SRjxsuaIdCz3IjpPGkIS_MefiJAfUCHLmmbVYrP57LWPqKsedcxzYbp7gy_f4OPTcQr2WthN-yLEpu-GLa2pWU_G4D3v1OCdTe-YmZ3KbUQl-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ2kXHM9OvwBQQy5DR76nXcCnn8JEOJ0VJAcK-UDEOJMqSONUVZc06J56owialow8nJOO6pnddRS9pToTFqlnD3lTNSDFJLRhmXCiMRV5lGB7cS6ueBYVK5qF3jjoPE7CoUJNt_9X9DSpffRxmFe_ql4l2wkug0qukiNIYPwHMZAmm8cwh1keLbc0JrqxkVSyxZAI3ei1bpNdQY6W1n_Gk0glDAn0E3v96nAyRVFd-t8eHXRxYuGLc3jXn5sztAP18RyepGkGDG6yrLRh7Y_BcpO8Wvbo-P6Y3SmheWdZhO8EKGTuay90sCqTnl08DA2plrN_qdBhtWifoTzZzPayA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZlmYNq9LUoi26vGfS4tiGDEEv_QRfHPBLTq-m0aFZWEmWSyzq3WiI_8G5DIzLHmeGF8qr5ryktm26U8ocQ7KmXxNrO7eTSNXpUvNHbRWXrXE4l7oTRwHR43--97LT2MI1EOm4gjL8y6a55Ia4zzvX4PrtDUu6OAhBFElWa64INR77z9OKnNzyZ6RkuzG1HOlZJP_Zl97Hj0hZdzH-cRV6makKXq_rYAXbTLbpazl-IPOSef18KgjnJWPY7Wgy2ARV2OwfuTKYjmF3HQ6hKUFgCD38qaOKVcvSm1sHt6f4wqR0ZpQDhfoKcPlnvapoFyo9IAdW-0PFcwCqPy2smeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdzUioLhLIjoM58_vWdhjHaUq9yAI_X2RuJGbkZ9qSMQptjvaPObrIR-SDyoa0VlsiOISPPdeVuNvsatBgnEI_Yr6RHxYYdy1LAVtZzjEdtRMepY4wmwvGPFv-lIRmP8_-1LelTtUTaP1EGqRAGL2BnDWkZh7JRI3BZ2NJ8XSor6IAP4IWr-ZK6h4ljQgLQF3XNoHU27Rv0x2-OhypyzA9jUqeDCuX6r12x7d_PcmaRjicxsg4HJgW0RPDqDi0tmysX_Q5e4f_jju20U4JVF4MsHAZvRwPuCxiLA-PsBMPIF9qpyBFh6IeMa54qJjoV020apO2LsHPspyZN37ppkOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdhG8YoomUcF1Yvd8CELi4rVlKbZ7SS2R0KuTFokX2P1hU--adjeILnayzBGheMncg8VPmvu_BRj4x10hvTsLMbv0yPOIznjzvXMnhYvdcx1y0jCILIfgkk-t5SGQIsn9FpULeiXP5kcVxjeRttJ4nE6G2EhE4iXdLFVaMg46V8NuOZ0ohWsOVUDlN9u022sRpthSPUazhSxKmha5E8-kYD3R5KaB71hwmEtyRRaNJnNEc74vgxAlqYxbVCHO1tVjh2a-0hQOOnG8KO1YpIPv87qiEFI1ptz0JZMf8vdE92vpjvQXsBiJ5r_kMZP5GfqFX6C6ZQAvu6kky29acU1gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiuXi5mYyR4XVMY48s-PRGh11RTGOD1jVfgKlaQSLPF8idLokALhAi2c7CP_78c4YURQlYMTsnXg2GM1bu8YjjUdiYvslnE-wYElItz0qT-RInAbWtiQCFDm6TYeIvQRcc_Wd-htzbtgbql9fxW5IVJtrUf_Br8ZD1WlVE2WJV20kv9z2ErZ629DkJlUHeAz88m9FZMm74c9kYwMNslIeiPINmyziYqiiIWSpg7vBMf9S-WGhmloPjHBMnZQSHNREVxRnr8hwvt4jOi0r73p0ZguOa-J0W95YUZWll-Sl3G_pYZqlAYO7Wgt6b4YqcRaveWlElmQCYghIfh0KXxVCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1tOUCKIUnwTfeeC5uisq23wKyHeKuzbzYRXIn85SFDWztt7NuaK3BydyXayc9uNypA-23vh4Fxg-R-L8p-P34kd5z93iNE0yNb3T8DzYFTw6SFgOudXngWzvuADKH7BlNq25VSbF9t7VECq71YOhCG6Ouaad8LIXHiHfZwjkWl-R8pxgWDG8VP2vuW4VDyqpYQUyDNpz5cDPXTejXnKaFdu5dNx02wyJJc2OnAFxieM1Ks8zAQsJrUNZZb1g9EQ6ug9G6_6eUIi7xjGCvgHPggVOSbLvz4_l248FSEY5rXMvIT7NwLgmBDSR8zR3Z_zTiDilC3FoFp4H5WYaV_xEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoGBlOUANEEN4AUGOvoCk9XaoZ3fu_80UlAF3BoIPIqDwELg9GE4yOgUNpL7trfwSlSEBGH3raMQ8Yd4S7igEzzFaihJwrOnPJKUbDqoeoWjKYX2uUCKX1-spRCLROx8KGTO_6zdBzwTEAqtc_y-jKCGFw0Zuonl1Pr4BbF3rS_yN4T9Jw8d2LxUXv2rF8YmcaYdip9SU8tqIbBl_In5Fht-sxekiEhtanwrXSGWTcxntTj6CdgpmzqDBpb1Tj0XNJKATsKg90-gNNHSWtuzYu2ANhSce74sX8_HlZ6GtAdgUFaKvA6DH2BMfRdFuhFv135pd8OF2Sp8Kl4l7ymwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 695 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUm6qYHakNcb3Rpdu0vFpMv-1co_VYLqaCG7MDU0eqRH-3c4BJqwvLhHSzd7MsInDQEa-FCIUHWxPhnsY-Wd97J2wwVJa3wv0EX3bRSbo-KNNJAL5nrH8MDbmvujMUC4TmmiaO6GAdwzcZAAAhAqXoETx7Mt2YwlmjJTKd93Yx9dbyzsHlm6QR5RiATyI5jq3MuvZEVJaXC4kUY761PNrnfABGtjQ4rxBz_G3ClDxHcS-24Vwt94mLzHMkA9sqsQ_Lvl5_Cs-mhC8rGK7rdbQRSxwvKNB84mlq3lU_LhVMH8jB2R6HGY0G5zd4FlRaXTt79NaI53VGTgogigMihIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLELPSxM5NrickaDIYMnjtiqsppuqxrL4FeQSkPLm5412ICsw7mqfEOIR9B6tO1O3wiWjpRDT9w29gyTNXNfWgMHF6dLtq5CXfmibOipVK5P4YSYyGSl906XMfqHdrj1bw9N375o9YEPmhUHALFscmMKkYVtJ11XAW1Vou4SuINn1i_QGJttfHdw2Om-gC8yHzdCEGNVDiWfEWD0XJ6y0H4jGU-zWZKW9eq_eoN_5KI1LvZn0OpasgcL4RLCk5h8WxoJ0vQZIFn2OgHxupanTSYmNdM5HfzbjTWq2mBlDBR4jKqmAHmVo57nSAznLR_C1esAxYeZKevcwCSjyGRQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWiP2PmlKXtd_JlL9Gd8pcMRGbv9CG1MuiPdDHL0ywOVe24LS9LjpVt9LYe56y-wwt32W3a9OeYlanNmknhn95qetlCLO1aDdTM6WYYnS59Q9gPggjd-cDjcH7zkeGs0rTQfuaL-_QNymrQ-oe4Y7V_L6GHwcBKrFs396_T4MWgTHm0__R8EPxFc1aaEj2iTbEDaIhDWY9MtvdUwORtqakXEodR6ftu3OFz9qZTjvUSr5_s7jtvuoND87U5TTqwh2vqkTsMcfJPwdpl9SDfM4gTpJd6S0-3ke6Av_LHGEPRCpwFZaZ24xdSCfeK5HG_cbUmcPECD-wMOgW8-mZhxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aK5oSh6hkKwW6jaxShRKW035Xz984_wWJxAzbH70hiOyYUMadezWCLcf6FF-KSF6ClS6AfFqL4n4CgCq0HpSCslK_xQ-6WFPMQrce0sOcdLJst2xPjyNfu-dhWAzLfYhc5kNkbNNd0V85XMvqHHG2kF0pkLbUe-3cFOC7T-mGhqm6PLg7gGM63zHJ2cM14VATHh7rESW7awGhyTVR8sHCGRd9uvrsjIia-Q6MJzH242n-HYJ-kznUD-rOByvmFKHSQhsy9oLGfMIr_ySqz3bUtVCG6t5K0-72LdkDKoJpv_jOHAFuZEVhhhEz3SqYfVEh-jDaLf-ZETHTUi-sTnUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgDiz7Xn9LaJkODrhPTcIX3kxCMYh9YEaDBeKqvBBlHFVFWqCYZ-0GaOszCxoAfD82ywH15o5v5CfAZy1mWMDkFnAf9WR4ami2qm-wfuI6v1E0B-_86H4z3uKRVvANg1c4JK47FwqvDAtG3KLSbU9gY5mripkqVKBnvr4l-0Sll6C2Qth-xFSevo32lejK0zXxZYZr8kzecszORUP9bz-3io7UWkIDEmr5305KLImaIfr2Wp_Ik9o5bwBFMlTX-3gaOYVSTyeryuBqWTfy_UiLSVLhi8bwywQEUFwVe-s0s2i-qdi2FupNV4hhaDS-kSSXo4Ma77qkPRhUI1bhRIaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTOpoo7cOUhzIuK4WCVAbqW0dZIOEU6BafbQLmnadjdsLyd8QN1zNly2tJRaaw0js2ZNV_zOYBzahjmjvW2yt179y9dA6DqvMg9CvfP0OCNG4C29mS8kZniUXxSkk4Q4t4vuNlSXc4uWdiv60RYO8gGfvLUnqAE8fMOVnXKr-z_2OmYzLwap6B2QoLgODyHb9y3nPxvKHALBX-EZ9HUtrtoH69M4GmJ6SXCA8w0VrEzpVraDS_D-UzAz9HWb3mwP_WAutmuDBA805b68Jq5oR6Fl-NRtSuzOjmOCfiUfrU5nalrFSrc0gLb7u_VJtkV2TrnG61J_EJJFo9BP94X_qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kegw3IiB4lJ6VjFhb9GaCInliVnK276TysO49l1rqHZyn8D7-npRul2GhIGU9yc_iVV51jieBsWmI6terrhR6fXFHGsuGaR5M9PYR6WNnSDsSiVylpvnBwDSHdHWllycFRnSbGiZaHhmXiXi_ua5idB87yb6yo5Spjp3kIT_C1LO4MngcwhvM9fa7F24zzM6B0r2ng8A5B-9yjQaieMYSFnY_eu0oseB-WyDOhMtg-neE8JXSOutbewF5-NLZXC4yRmTjLxtgXMf-FTcf76529qcSGOxz6CoyaIbQGGQ9x5IPgGi02oPesUKMauakzarb7_DrJE8b7g3yHGJanA9TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9dt_LiKMmOEhsWXa5Rx-aS-dolPK1Scnl5EnuYcx7AFgq0YXYU2gErcjTynaAqdp_DmNT7ERQ07BjNHu8BL7awFn1fa_erMmxceD8vyyrTVfpy8iDrJ0R2OWE2LjquJKLJXo-HdgdgYr4zjYx_AxS0BfkOGs7OC_QxXSJ5-j_Fzg23lr3Ct869jX7xgIqwMkG0TtsuyYhQuF9okyXiCjyYVjRVgC86_ivdZh55ftgopwhNMHaA86g8u3qfRe6vOT0C5TKf5l5gOQ1BqENfE3-kdP2RckNEXjGarJka8BXUyg0BWTc562wcyfE62pWznCnSznbvzvvQT-lZ023sAvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SckDY01yeHELB2l0SymK8in5EICynt2aE9fvZDyQ-kLsbO67ybaDsGnPAi5VUIxjvqHSiqfQxMGCPQdhBt5CUn5ghj6UnmVd0EktSb-jjTGn2HixvkQB-jAPuLLHX209n6F3EqkGOn1SlKtEr21xVgqjCO7q7RccCD74248Pzz4pKkkaZNxkaHu4Jd7FHFvwm5fEHi8nxRVcRf1ORXrMT1VBbcfPRhX__W1oDxOtjb-O5m7GaM_6b__nSpR6Zqft-KVlgl6UmyfdF6tYwM-8W6izTRUtGbGEeKp8OiyAQsgQTS-DATtZ0NiHWKWFpIpXtnc2k7Q41XnONZK05YapyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgM2IJbgBbKbQEbX-9m8AHmgF7nzF68ChUfO6Rjm8chouxkCKIRLR1nv1EDS-6Ihg35LSldHUbogLDw-E3pKfcXKeYPj7M3dPkM-vTsPhDGUAtpsvT8Ulpud7U5j6jnn3o9INonc_qtojBQYweOGLMvbx6dnSfrJzwYOJDPzJ11QTOv57LuE_vM03ANrCvx002NUxizpEgTXa7Ccc2yZYtciZ9s0utA6Dbqo1VBnj-iqAgsKcmhySlNrfTkB8phncNzyI5oaie--d96m0Y3Yh01vnu_q_p2nef6ja6aAtSeYecyONB6pKmDZc5KuGSUhARCw7tP5ZPa3IjSiFvaqhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLGhtK9bFxkusEHtNjjzsSV-ZabOS5WrFtCvdXAh4rkBZAnjYW_TDPNRxsN2xJsUbXQUBfydJ2mH5qwB6Eu-Jcg5t49AwrPLjbSflA6c7nPhJeLPjogn8WO0UybHpmasicz5OJtiDbyxMWdCDzmiSFrpzSwCUGToUnEktNXwnawh4GVFQgDiN0t76YA54jEYDUV54cV2cgdbY8B_jGo0oUTnC49qIb8qKdXCllv4D-DFbjjK-8p8GU1KaoX7wB0I1DMfjmY4QlLcI13-zNtR_0ahXqkFPJL5ZvsTVlcN0p6mnCsWjC1UpV750nUWeZ6__lQMxj6w2GKnH4ywiXATGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGbvS3rZM-b6uzkmkwIbQNoCkovHEAiagncsvZwvqhvjNxmU90N2jNjrckT-fa0PO96M8O12inAezlGicZd7HM_IHXhebXqPyI9XXUP1YdUVUobacQhJI0TKQMFqVKH41WOCvSbKnhFE1qq58KsaU2ZaKzRpQJmUXeAv5YyXsfdO8gqaeHTZ61FLS0ha3wr4nq7ghq9yJvNdQROxJplRbDwyKYTmA-6-BSNPNbj3Rz6H4VbSNrwD7IiUn8zfKrZpUyoM4VokMxqvILKLE4-BiV-F8fkfa2aTFMDBtdjcOXE8s7qT1d-DRE-_RDXkwi6qMdQwPNKcMGQsreYc7mqdYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1-Co9XoNXMxYPIDg8dvB7O9Iu3rjANZyqxhpZ7arWxxesA9dBi5h_2UIZNzt4IvIpi5MC8s2knLJMh2opFkt4DeutfiAIL3ffI_oEEC5K89gwMHnRzDjPS7gYuJhGxKFYihmhuagjQnx2-7hMM-nFZP7u3e_Dqu6QdyDekwiQGNBw9E9ml-JchNEFPeQ1e0CjFebHQRoqDdfX45hvTA5QKnGzNEYiy4bHzdOr5UMgCrOVDBtY3-lIBQU0eZcdq752NQGN8lSwtMiMWVU4I_pep0fbiFdaAc08uzY8A96_tUIc4BZXzzvaaGfmropwxwkYBvwMjvF_PIyKqTdXpLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIlPNVjqqIzS2ia-DnOSR9Coh-I_jBCcz22fW0U3XS9F2lizLv97DQCqiuC2H3QTsul0cyCQMes2Zqxt37EEsmNv-oJb8AJKLqmjwdws42hQIjJpT5PRd7HINyO1H7xnTQgoSgr1d9JxpzcWg9dYt-aGprzx-QzjdfIiK-C7nSyIWR7XpADenPPPIYlCN6s03eS0YtuH2uO3ZR4qwX33Z51737aJ-Pappw0SC8A1HO-qQJ8yWrz58mnnia18ikLWYJRKm4WY_nbeu2QeKCNwGSc4MgYR89lfO2z5e2CIjfDCfw5jXicHDcnS06SfuD3xj_zv0KMqdWD9cQp1ZlikCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDvDMYWRRlBhzIgnT7N22Zu40eD7Xd9wDTXNQgaL6tVAsqoSHSOKzc80PGpQ7K46SvwbjG0sb58LIrJX8kqYTpWJVQeWD_DMNIYj4H88fsyG8H5U6ATd9WBzC4G5TjfWfTAks1QXOrUoMrEbd_lw9Jv3E0E6CW8xL-03rD4rHGHgkDXEavBXktAd0KThHMr_0Cbmh4ppEHiExDdJ4q86tCSn2DRA-SaOxv2QWHcDToK-JA0WyiIMHnJ8zfX_aGcnZANUkzgUKzfiV4lnUmUY5hZrMOqguZuJZpSnOHvYs672AXvmcrMO6Ft2k2cneWI60v20qsJS5AUYNn5JH4IxmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPokm7hXeEiOa4sHawxCIePKFcHRn7js-AJSPloy9nk0j5OA_Etct1SvC4wtf77Y6EKosBPNofxcSSilzPeQvUW55pv7aifeaVSRQ0vwfhMqSb6zNtg9l2Patnm4Qk3arTGTmD94RYOe15IKXnptO3WznWOHIrqsb3qEBS5zPkk50wmUt6IrYVou7TnXfw05wA8uY65r4rE2VY193AoaR8_diEBUuISvMHLXDX496RftcwWt5HSieKP0Bt4908uFiIK1I5Zz15sUC0suHRqOaLN9uIvq0wcBd8nZ8AO_XN0Gfl4tH7NDv-v_PIjWJZwPAuUfwgLQmHb2w79abErANQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L82qDFGg-4ypw1sI0cY6Lhva1NJRXHwu6YgtxHTzgcltAmgqfXZ8rCofAqbr5-bbM99I-vKARMhYETs2ArsKNhD8yKST6d02r2V21s6nd_l19i0VaTl1Aiftla5Ms31mTfjPCSEnfwxxIjJSem8Jl7JSeujNY4lEgXEtfq3L0c267-2kY2uI5bdeladKhOyNkgoW0mt8MeY0VLdob0XMPdKkTT0sXbyqIGQ-oAQsw7Atqx3ldkwIUz2OkTqsfpk_afR5-fu5-3xFm4bYyceWQoLCBJ3OFfnwF49pVt6_PYE7XmjS5Cgee9EgKwMf8Pt-cfhyugFHX76-A1H4hfZ6RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4Lr7h2W-fXpji53lMfmiXMpXtvFPoYdgQuipBV48BjVK4bz6mWTQfeGnDCPYXAMYyMlkn_q3WUxEhtUCMeRUA1LcN-KEbXu2MRGWZTTFfMKuyFLCotRvOZFXDQa-vGXk5QZyQzrYjcSL1-UKX7OTV6sv9S1jMRMqVSPlVx9WGMwjp1-tB040J1IlKtTF0ozYvBzf8NWZbaYoA87jifaMQeVqEiSN_8ZrWn4PZ1ioa3-gVOHFa6KoHU27KmaBIwyMD839zXhiymyKbGyk9VY0DsXCNgMEEss1isj6PAw0SZvQxzTjfjT3ygnCbdH1zi6bxSC7zrx9NcbSXp7mxnX6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuwP7UkdJurRSdin1BGlII1w-3IH5OyuNbxeKGy2X_mrzRNXy_Gc7wtDklnrA-IgS2HxScXAAWxFVXVITRF9P3QvODGscFwkR9sbXWiX1F1vlw5oziBmXWkhWlNknau2vTCpD04N-rLUuyVWQQSB6_Mopclqlh4fJ6y2KesoK1aPSTflOn7q2OcmxAe_D_wFwiGg1UhYgs6L3i-P1GseUfR6glu6jXCnQKcan246z4--dfq8IJRzMzkeYjav0cKwNaLNnR33hR0Pdlk2Q_g1B4pQdejL1_Gef--nFIvGipQfbwz8pV2w-mZqwMrQ4hQfO6kDeUYdjnW_uppAqvYVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgJuuClWBzL_RkS-2CCIWhh58QUqSQkHRb5lRxM9odIV5dT0Y1P4KTACuW6Lx8u2A7yOXSyPuJmABBHCNJzrKq_KfP7DL1fiuHS7eTYSP6xUh46Sxc8M4Do1ecM4VeGdtG9Lo16fVgut-rnPL7ckxm2mZaebIBILzmT1iViqkqu-ZG6l9nGF4xLkg3hrgCBwWVblmIWxpCyoa_i1hMENyLJGXfAkYaAty93OGGzZxfLopL-QI4NKxoz-0dHQraD2-w1uGwB8vX-t-eahnA_KR70r8TBTRMV2zfqXWj-6qj9M2q-_7bwK5SkL0JcU0AAXnf0Eo3eXD858N6HDu9WN5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlzTTcxfU4nV4tNaHaxpNFEnBeKxa1uZfxkoR8M1B9kw0EMrq7YrK8Bp0ldQKbiA2TiK-MLX7VznJ6seYBhah1m7I7qoi4p5Ac1vg266p080XclEbT_tctMpmVnl0aabe8lNgExg5UDRGxnWyxLd6S34FMX_eQGf9ujafgdLrADEN_OTuW7S572kp-tRUk1yCI33QzVLt0akFhaEm_z1tYKXIhlGO4TuY_MF1BmpjWKc_tDFkYtmcU8fkzBERxH0y7AfEJjGIi_Pd4MGoB31Xh_MB0IXblOce2s_uRP_PhPZvsZ0VL9-Jkayu11iaqePGfOIK4F0QJk1EyohQ4lhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XRaxXzi7EnM4esRf-fzwIy9sn41Nrg3GAQSBec-aMtXE5e-1pVWgxllTt8EwKSYp9vqb7VrEJF5gLUflFxkBozt42RxbOmbF43TO3Bem9Cuk0x8FSMokmgeFU1Lm9cBntqeqOopzU24vqlDeWCOzmYcW10F4b_u0Sx53Wo9X6ufT1JcP8G6HewPXfho_ygeiegGjXYLDR9eWrpUuIk1CGcvfJKX4X0KAiF3PoTcQAWaw3wLzSizRBI0fee9xXJ2cUYw48Qx_girzGWMaozsQq-bzuxueZUX0nR4SbZVAuuU3XuqUXg2wDnnu5vAslzf1SPrewWkJ-1PEOGuJFeBbWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-K0_FasmbOUwwwCj93F_vzMPxp6Qosu9PcmSgFQLOAOMhE7rpxkAfk60SQSX1I8wqaPj4wI38a1RYmmO1c9eU9QcnI9ZAovij_-EW8YesXolZaCsb4wP4CM1EgQF-DNeq0Pfi_ZYQZAp41zTf2Mtcognq6IKdFgUERa5dE7a4C2LfJvXzNMQNXW67fMGjlIEUib4ot06cQ_JnXP91QzDrh7KMLZ3nEZ_aAzoeGkAmfGENI-WVhBvh3MJY0_0y_aTFiX4i32bM1nbTZE0kH8cmmAQm_CW34X0vokaWwd-Hi9OSj2HdyWZAbtkHAH9HU2yOpkLpVBFet6VRWsUQEJaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr1_2gN7kFMpT3dhu1088eOCgF1Acixn8QLPK--PXhG-8Kd9uXxERbgOEle_14_l8lS1zLvvTCTjgS2sYE3_HjMZqn1gZqrdOxQqF3X87834bldsgv4pRdRWfss7s-rSbpEG36ZeMlgqky-OQv6qlXADWP41raEdxJ8VjGIuUBbBanP3_WUQzDJj2vep3_pGYq7RUa4lSlm_Hthzta9yO7OUXngabkh0yU-QJHRnGaqjgC_YA4ukBqrc55uO85iqu1z7oan523_VE8lGWCEhrTqE9NAhPkK_2-ry1cRNBmBxo-qiT_mldlQXmI_PzrS-CD6aVoi1ZnWDeiWpJ5JByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyMZQHnMakTpkF0nd6jJ6_enN3--BmBx7ykv54j7pmXv6S93mFWldpEeDHBIl23-6l7c2Cge1cILfFUcDwSIu14DcyUQDefnoWb6bNEPzc0uukEwdmmw0G0FGV8ovaIv3xN_nDvY1Ub54X-_OJ4Jl7vgP9fhWHmINcuqgjho70pqf6a--ZjUigmuGy7w2fqzZAOyDjgno8vp4FVlbqfy7uP2F2oBQLgGTSd-lt_iuaflQ8-iEPCTv5taCUoNyr_y5AVjpNoPllwYhOGbBGkPz7JeZOct-a2X6SvETt1w1ByGtp3Ul8GDiZrgBhnlccwfa4Fqn6u0pPadJGetDjQY1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptPwFnCQFkhn0ZGG6xtSAUrMXnPdwaFkr4Mct5L9IXqZO2qqYWDEC0Jzf9UEPEK0gojxcBANQi1V3UFwwjwx10FCkyW7-GvER05jzlCS9uX-L5k-mqVyC6vrXKLd9l-sCg79Bk6z7CPILFlajZGsbF9KXMgoEG3qwfK9b8pARhu3xI-FbMaoIqWUpZYnx5fTKbOEwQnmAhZMEZnu5BDR7IJ-GjzDlSjlmyiQ8Hj_WCAT8zeLR9f05P9rlXXJzmt9VJItanewICSVS4EvFTT4bgebXSX4FX3c4MQzDWaaIuPLZuAfaaCHnrA-FLAFwKk5b11Muaad9bNiVSrNLa4H-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUcEmlb1o2rGS-eRzPBF1Hpl4TJkef1Z6y9H-iyC_sFq6ygEBlFgOz4eduFy49wjWZxVmtMnLAdhgwsCzI8ytovaaQrqd_8yLoKG4C7hd7Ue8jv7-9R0ilE6xTRPLLaPXsRS4Hv6MfUN_0WBphahIdvlXmU2D6-kHYOu9Cfdy2fz_RAl0R8GIdEp_RnfN2HbXsGt8ycCj-rK-4wV3LMjs9dtoLzjLHhf8tdkRXsVVO-fcgkEtAsBAdx8K2M3wh4IAsfH_oEqRUGH9_gPfmIRSXtVxA9R-ExjlH06J38ksTyGdSOBDW2yt7Z_scUZzhG2yAL05tK2YDPeX6RboJLw4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubC5336voFspCr9DcAO9lAB5EVkfqloUaczTGbWbxWJrERCMU_MKcpC1h5fBRiMP0Tf5UWSlPYYR8avoaR06F98rOXKj8pbf3B5aCfcwQgbGH_uoLArIALXr1HQQS9vfEsi-b9wlGHCTgGuWzvnrzjFTdZrkL3VGQtHE9bSw0VlrvicWl1SNs_Vd4VYpZbbzOBiIvxwF1LjB_fW21TS3KEAUD_Ni_9wm2CTqBKbuI6Sbnlse9W8VP-SwUJLt3gZ9B5D9RfPdq-LrvQSn8UJfQV_g-HiOOR6TSt3XyCra23i9UWPv6R2g-XfTPrT7BD8MI0vO1YBbGxoIp69Na0ocSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxbUkYIZjQfYYHbonMuM-67OBDWOktTw697TlpcWFsHm2V8S5CS5t04i0QoXnTuQYdno31fcyKRhmc3MIxa79JX5m53rAVAzYtKGlEXAjIU0KNd9O3B5C4Z296tVftTlN_7tgc1Zx8nqKvvG7Zbhgg0gnh0aL1Fgv-_lRH0ZE7SIyvnc7IXPUP0zBUtqw_R6aPoQiIgNrrmx1AGxrnaHv5ETYtKCvM5Gma8nQnRIH0U43PuhU4igN5SaHj5iB6Q0qvif02R_fax_R4F8gIdyh0_g__llPpoVYXsugyPPCb5GjhuQsSpVmOpy5EfpjmKoZoSrb6gd1wHZFRZyI9JyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLRmAZaqlZMnFoZmqyfDH_ZuV15JLiczHvVGY7rt-loZIfhUMbIN4SENVboeqh5GfkBqe3CwPKgG_1sxC-B_aQp6ibm1DkJw1VRn0jTO_R3AywigqPa_skXqCd1NRghMnf4EYM-M8y9gGcgkyO09He9N2kEoMe8Cuvd5lf_1Bh11NAPQ9GtbafAQ3rzMZnDKV7n-Jgtnu2NI013owI45DWOj1HZkRXhT6STNb0jZf6Q701kZh50AqYhWJcgk4dYxISm4JYDzWjMlfaIf3h8fZxiHG3lIMAC91cq0YaI7i9RE525d7Dteu625lLQvWGGgcehKzP2OiUeGvUqm8tqcEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0fUX754sysWb1wmB-C3cJqmBhd_DoWaSEO-DWryCXjiWZHReh5qPCrCeRi6Y2fnC4iAt2FeEV__Lg9joZlbCfNk0bcJGLokXsnLNE3AsTRkrpkjg26wqJXlAam-v0BuIaZWtV75I7yfkllOJQxpfHI8f59IAWzFuqkSugWwrwrk_VTmvwqXuwyiNAYcO29pstdHeLh8ELc4sQFq8_Cg4xOJTFREApbVPfrtF6Ts91U5BS9IHI6tO73nItOYBp81WVAZNzdyA3ZZyjpgioXmYeiUdoUfSwYkOBR6B5snCY0Bk3zKLT2jym5VWwv52LqrPIA4LZn4KQ5G4PUUbH5W_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1zhqepBc26nIC-esBowYnh-7FLIcXrODWimbyyKbRY-d9FWRi_eotHx_4_4ouYLWvqPSTuWdjmuMJCfw1Ro72DAanm4lY0nDCutFcBFemJCeeBnjoYJnUgROdi-EiK-924syHSEy3kk_7R7bIV1QhjwuufH3MuuaKtDSeuimCzI-kNeODSMDVdlLgmWLWlngIigbZKMdbLBnpApPqsLabNibIOcCUw0CFKVzNYEtuUK8spifRLnO1Qq6gRVmDs1IYj4hwNqfhhcknHqFJyIY8rvb0F5C51MvOY2J4QtPFVeyCJK_BnfxI-dQEicswDKCHdg4lZ3zx4yTnC1U03bMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdN31DCykakIFfSFbJMjhkeU9e8AT-Hfqi7I9YZiTzzztJ22YajJORZVv9DGOD0XpFR_BmNSO-Fbbh1rksUqMK1fo4_jVUKGjAGPlVah3PBJvrUIi0hMaWIAP6hSHolJfFF3ibh9mgu8Slk-hykEl7JUG-G49WYTb6CT9srH9uw6p5znFYcSIGagWKk7x25SZvPGy1tKwN3_xcGKUpiB2n35eJA73zRothUoQHA8NwYoWCevRANV2I_gWgzx1VAU1RH7I9Q-sFIczl5GM6WBXOho3-CssXEzvyFv9fEP5tifLUD8ltaNpX1GxblNjFWnIAf2qW7LzQmVgnLM1kUnlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEHFBOUTHVW2gp0CYsdrOTAn5ZHwPtWKZTHchYmvyOSk3kI6QwzAsB3uaFLniq90HZXeyeT5i72wLECKciQtsObNXkH2sTV6Iol_0JqWNWHOn3W9Pwte8XFfqoRJHRDuxRZY78UuackTQYLBGV7Q_AXwlsiF_4OFl9ZKeg5V7hTI4UxLMy9AnL2teFlVJlJfKBBtvGd8mLGFPXhOSGExniHNOzMFPh4vTSUpCNY6CVQNTOIK_sSFkz7_cgDtBxh1OFw_HnTsdBvKQ74ZwM7QiRPWpvfIFWnwMzLKwzgGEyfrENoiIwh-L5W5Lbumm2EsdNz8sbW3TNUDI2wjy61oPg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Iu5GvsPl8NalRzMvH3JJYiICtt8luVMXigaMKPse9xT5cZYFEc9zn-J6FW6llPpz19eq2kHlvhmSzDW4akamikCDFzEN3M_8ZfHwIxAaSUxKUCUrBhUbPLwmPbq0H3EGgLBDeReWGOaXUvxDTEveow5qUt22OA3lD1FBYqnVrzWri42t7ruEajs4zw3jW54TgvvIC-tnJQ_HxAAo2TFTGT5jQbnVa_LUsMjE3tmnbzHD8MB_g81Z3mgmCGFfowo7B0Q0_JjlVY2m8f3LeytnPGF-3gih05t_Ewa2yCotH6y5e671SYgJsrmOJciEYx3tU3rYSolY6lGfVsNEXeGEGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Iu5GvsPl8NalRzMvH3JJYiICtt8luVMXigaMKPse9xT5cZYFEc9zn-J6FW6llPpz19eq2kHlvhmSzDW4akamikCDFzEN3M_8ZfHwIxAaSUxKUCUrBhUbPLwmPbq0H3EGgLBDeReWGOaXUvxDTEveow5qUt22OA3lD1FBYqnVrzWri42t7ruEajs4zw3jW54TgvvIC-tnJQ_HxAAo2TFTGT5jQbnVa_LUsMjE3tmnbzHD8MB_g81Z3mgmCGFfowo7B0Q0_JjlVY2m8f3LeytnPGF-3gih05t_Ewa2yCotH6y5e671SYgJsrmOJciEYx3tU3rYSolY6lGfVsNEXeGEGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFGNlMOgSwD421WbTdm6E3ZWzNTKlbZd9Qp4odak9BY3mDWMLP-TSHO07_AQj4pe3fGigJGRLjsZXtQCcm4FowwIEgSwq4koq9clA6Vk5iBngmDi6vTBsWsBO_8qElKa8ucDs5e5IdINfnUmDDhBfVvA2XOkITLDZfvXXXNo83e5qxmr0te1M5bEF_9RuwXZi7-nxY5TaiYdrlyorr1syaExbS3lNDr0jOpWzshB-a0D-54MSrhDdQlvcS2beVwjaIo3aD_0ZhHyj_9nB3dFgqca9YtPEUrgrL7aIupYl9t62b9DrZ3_sknhTpPbzw1jYSjyvFUWhSqqnuyq6hPBbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu4M4ZYVD2BqukX32Rjpy7QZ7xoZDeXPc8zWEZZbBhG_ZPjvaoist31PSiaZ_3kMKsKxQRjRDl_b8HCKh38pbgui1-MtgT7wUtUjUxzYyLX2pSxqohbVwEQj7MkuDkiGs5MOQ8buC-475XROIjnRLN282YUMDH1niYnQODUyzyUBBQZjFAKSTnRyPnDIUdP-ZBeiDyzGbvHOTRN_bFV0WOb3dkL3mG7XfKIZuicDuFleYB3uiTupTNP9nKphbt1q4pWtkdGrUMGf0ryWalJ6GhG5mG6GAfoPmDe_hEdenKXWWxrbKb5i57ju-mhp-pDMPnwwCcVI_N_WZ6H7IDS8wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXgcpfcUC_OlVGWK5o3s3VAZQ2DMY1Gi-M5u-RM5rtLJeAvcoQG3D3dDztciH_YbE2YFeKFA779NTwcsRhWz5sWm-ftY8D0HS3nNUqcW_V4OiW0ReQeb8woqU_ctaIy0u9D1Mw2V0IpkgqxZrpIdlrSQehYmZMWpWHtMfciYspG8j0-mbH0d8uQYxXFmUwg3oM1veJJnmxbiZUTS0viGnYkxVmzHqvNC4xHArKi5m1MbIx1WeLL0wUoDgpCUt2-IDM1WPcUL2x4JNFJoU3yfiEzcnrLZeck6QY9ADXlIc2ze77LJaSdu2gta-ZTJsmyzpG_uMHEVYRw7IXC2jT9Ggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCzlkOmLlvXcT22aYSrJO0Jvzj1L8o1rhoD7Rc4oL-yiZDsgidTU5s6BQLhd2bcsDpnUHMHfpc4MeBo-tlZeAj87dT_ueamUE7Fsk3BzJKzXAfrn5FECxirrNSSmHa5EC5OO1VR9yEWQ52IyxV-c3xDY6mmonipVLo7wFAiSgbrZxGjsnAFevzZcxbGd3oLGkKJjWJNRQBvqNzvqD4gl_OLJyb81pu8MufAEcZzEHqU-6Y5X7b7izRWntNrGak7IJrimsybF1nRX0GYGY-JucvmvE45SybVLE_hh1V6u5HYSjOzB6VQqiuucTjvamPGbCoLbaitspIMQU7zwCjCWgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQjFA2ujrRSvtraiKNZwd1xCG7FM9vxi0yNhXBuLhktSLvgsD2_ZiwNSkZB0owlcK-I91XGrvnGF9nUDn12tvqjf0ZYuJ2Tr_25kIXEXhBxzk72pDmdyXvDgcxghoCxW1PNM9r-PmSyPjg5pRJR2ZyH3XrtQSMRDR0YiL7Tf9_5W82PMF-wbxt0OfSn7T8Wp44sfeASv37N_AjkDpDaIWERkEI-JwPOtl2HWbChNgeII4EHQYwZVEtTxiocz10eVhHl9QnqCooXMPi2yzdFSeobjDCltgm54T45Mv-VwxeTgdpB4FnuWnraX2FUe4jhLYtj52yy0crmND4EDBaEiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S01ZwEWIFFV4pmpAijgiHXK4emE5HDG3XyfKSzs3G3HkDNcG0Q1-s6EMERpA17KPUfbRq2x3xwOF7S3xcFLPMGJwsq-ZKdCPklpRYdOyXUTnEstEzffOu3SxqRwPhLwUZHEVA4DM5hG9fyfuXrK07oKeOy8QS4HRDwoD7Bt2mkuOPzOF4zIeywDvcIQMfGwQLXwcrbS5DBLYT3NzWwL2NE9Zlvj_1CpPz34WKUz2U2DnBtOr0fWZxAgmn5FbHF-FBD-raa008iHXDfFxd1PCe88mZ9jlkSOxU9Rr5bCNKBnSp8KkzAVEKdkvS9qC025k_bOEBr0VMTRtqrfioeInAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtiDX5tEwLNw8lJgFUWAavuWk7kwYoaOZfUIlZpJujTcy0WqxvZdFG-X8WhtI2OLoq7XfOazghLJC3j4GK8lDivGkDc5MIDECt6fM9guu4_8wnVeFfKzfD8q3kEOREGl-uXlJuqptnLuKR-hG3K7UcngcGN-bSYFPu-zQSdC6N4Qs5zQNUJKS0xMXtCBDtny97xa-v9Wq8q9mL8g9ZutYzKOAIHy4GfjauhEF2uClPCF8tn0Tp2Yvs-_4biBQ23-ALUx74XTGzRT7o-9-sqmIKyRwX1oVRMgwtYX8HvEQPNS6otgkF76JPtncguBtOiCmKcqv8LNZreVWc-5hR0taQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qXLtlueR6_NDPYoSaTxgBBVFW9amLwg7Z_2EnhRxlpc4_23cvD9PSF86FVF1bOHKctO_x27xwxzl4cmKTyptSHXUy3XbuM9hWtXsSnWXv5Ghwh9Jjzd15lC8ZH9KX_gRtKCduN2OhsBKNvFjxAxjiFDCvHG5bMsbj4RiZsEpqqRltwCOvxPPQcPcnvd_FtjOljCAqvb-h3AGvFf86w17xk1LnPEvxAdBX2BBaIXO2uaTqArhyhfa-qGOI_jFVmWFtXW4jPkg9SA2Ekh9HuZxfDiPFZ_-WAM8lVZRVaZzYCnHQxGoli6gE2q8ZgKcaLpE-QP_UNRbhUEG_bG_iHtgGZF4r3pMLCIBrDiNnOedXd9Y_hKOV1h2B4xyFI-yUAO-SAFPdcMfCeo7uRXSvuYpU-OFO8fQJ5yF0A_-O2SJpneCKEak1p2snzws_dnXR5ehOZTmm2Mt-27TNI9UoSa9slADfpPIT6fUu-Vjaf_xB7JNmXcTmQVrH5tq1GatMnKMPi8ZNryHw7dwbQIEKOmHftVslKrnovN0FieHpQg45HGn5J1SMKJKhPljT2WK5R9JDelwr4Ee6N2ll2S1mIYWpdu_imjmLc2VYnljUdHisjXAxGfycFr-mwVK503AIHsMrNxyTfKmS3udAX0q41RBlzfsFAazLPzyIlkjuzcChKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=qXLtlueR6_NDPYoSaTxgBBVFW9amLwg7Z_2EnhRxlpc4_23cvD9PSF86FVF1bOHKctO_x27xwxzl4cmKTyptSHXUy3XbuM9hWtXsSnWXv5Ghwh9Jjzd15lC8ZH9KX_gRtKCduN2OhsBKNvFjxAxjiFDCvHG5bMsbj4RiZsEpqqRltwCOvxPPQcPcnvd_FtjOljCAqvb-h3AGvFf86w17xk1LnPEvxAdBX2BBaIXO2uaTqArhyhfa-qGOI_jFVmWFtXW4jPkg9SA2Ekh9HuZxfDiPFZ_-WAM8lVZRVaZzYCnHQxGoli6gE2q8ZgKcaLpE-QP_UNRbhUEG_bG_iHtgGZF4r3pMLCIBrDiNnOedXd9Y_hKOV1h2B4xyFI-yUAO-SAFPdcMfCeo7uRXSvuYpU-OFO8fQJ5yF0A_-O2SJpneCKEak1p2snzws_dnXR5ehOZTmm2Mt-27TNI9UoSa9slADfpPIT6fUu-Vjaf_xB7JNmXcTmQVrH5tq1GatMnKMPi8ZNryHw7dwbQIEKOmHftVslKrnovN0FieHpQg45HGn5J1SMKJKhPljT2WK5R9JDelwr4Ee6N2ll2S1mIYWpdu_imjmLc2VYnljUdHisjXAxGfycFr-mwVK503AIHsMrNxyTfKmS3udAX0q41RBlzfsFAazLPzyIlkjuzcChKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daZdEWI5YwscH2XYceyuxdHOfQ6y8do92BWBaOxwcNPcOWBqeqSFzOtfInOH5MIXPQRuePDgX1bnh-zc6KQ4uyRPvTiUqkoxOR_i8ykFXNEBtkz3c_2PV7S-lplrStgvzVSs_uHkJIjxyv9MP0IUGm6VsepQK80eiVC4bN4nFGuoW1hMPJ6Nl9ADym6SpmC-mb-v5wcTOuxSZl471yQhJ40KDXxsD5xPGnpDv0QxXj_zfNpT-nskh0i0xNnYu-xVv2vyV9wybPVVc9OtGF-c-JfEm_bZYE66rLLipiWMurzjxhXG2RKOZg1wpmNe_5YUEXXDsraeoe5j0c2T8jj13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arrQWWVRM-8covumferW2zCxBsEJRwx8FOg7EbDmGEk15ECdpuL0AizIo48U8UzaakcDoVpE3E1o65TO2lE02N8O51fBTVpRT03LXQgS39s_qpCZ9WfdAGJCYtP3a-fC-k5vk5RYVxugzGL5HcCpHJo7COv58BNnHt-XumTlHFelxXoI0I5MJP-VFdWM7GW1l3DFWQJh7BgR4vxhVfiTFe4FgKdfRKt_n_Fef2gEAFe3A-ZksIq_EGGf-t9q6cSxFw82jR8oTVdgdpraFM3_6eA6ndhibIWmRHw9v3ehyQn3lvdtTdvdWi9L0P_jz_uD_2j0AawlpYmQeC1mD219MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsvT854BB7C6P0soD8gBkBh-0aIPssWOJUcKwrmLmB05uOWFArfzDPifrzQbnbKeHw0N5NLSNL5NMk-faF9NvjLEDOXdEZCbybIpxOXgg1VwbgH7ylGYvE0IkVfMFHKwzjOeq8KhAjH-IX2krVBdhJFsOex_i8QuR3pdO4Bo3R89QMklf0VapIAmIgS4hwP_K2CkHXLdSpXbe0pB71rzxK1EIVRpLpfCVC7Lexf7iGIau2ZTRQHU427rQCsmA3O-nTVchVSr6pGe7D1Nvje-7Vgxz1qwrfEeW-0j8REJr7roKQxZYE91WYwACeaNjcni4OMTl-5416Xpzc4jtT5Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpUtuWbsMgYhmEINKS5YssZkaDNg_99ukPJEpAjnbKEWCJM6ru3YlZoFr76UqNeUgGF5SZbRmcCSfhRBBR1JAY788YVlFUxe7VzmrpcE3GnpRUp2SIOQXhzRX3PUsWKuqw2NQP1EceYFezvaxpQVidcsb89yrGjtpftftIyBbBjAg-95iP0PeMsWFXT9Xr51AWyyA6iLoIqxOJVyrNVO3ALNHoVzLsAOYL0qAMlhitdQ6ODOnj74PhREhEOaBDC1X_lAN-JOylUegjdk9DeIbvJFQlYxK8r3aT26KfVVgt78yd1RM-9FI8TakHZH_kRbvHM92wyqgwiMouDW5Y75bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8cWS86FsIkcaZhzezhnSI5xCtNEFPu2rXsBHnsJhzs__UJRgNX5eotwCaSkJy5tL4nuqa316WCxWmGWqcmml7Mr_vAo2-Z1AgxEaeWLBMUtOFCHuzBbhEw1xZwG4oO2vMpCDAjeKLcmdl_8aCFyvpDr9l9DjYWrRnReIFT49Trt3PFYlRtDZxmZZk0zhZkqRbFaBg93L6KutWahf_kzKkqBbv-vHqvU5zqbrawK-jvFjSr6yWfD2AA6a5uHhvPOg8enBe1ZWrRlJ7QR36Sx8agQMhBHZhfZEgLYeJjpKgwggOAvwE-35bdcYofDeHdoyyC8tC13GY7n_UUiWSMwDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RSMlKvl_afeo-hMaxgtzOX0-egdDyaod2CZQ1NYumAVqNWX33IOm_F2H_i0YSQltAVb5hOjf_wn8qDvIuZvN82mmBZkZrgau7tfBtphFG2bsfXHlciLz0s7uNUFvWrOK6eAU24V1Ks3uUCmltnbW1EkVKx0FcWeny0-lQr4_cBPqFTXhhrBs3lwLLwQge1aw7YpAPW8W6PNN7H3dMFBMRbYBdBcDZCZIw77xDAt7oeXMFYjYFqOfZwv2j0pOXoXGCgjYkGYa5PVNWI1gE6mXOwJozaic8nGjZdgTlLBzc1G8dh25JoSxn1TW9DXLkzxGzsV7i4ut1mgWOtkSXKj45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RSMlKvl_afeo-hMaxgtzOX0-egdDyaod2CZQ1NYumAVqNWX33IOm_F2H_i0YSQltAVb5hOjf_wn8qDvIuZvN82mmBZkZrgau7tfBtphFG2bsfXHlciLz0s7uNUFvWrOK6eAU24V1Ks3uUCmltnbW1EkVKx0FcWeny0-lQr4_cBPqFTXhhrBs3lwLLwQge1aw7YpAPW8W6PNN7H3dMFBMRbYBdBcDZCZIw77xDAt7oeXMFYjYFqOfZwv2j0pOXoXGCgjYkGYa5PVNWI1gE6mXOwJozaic8nGjZdgTlLBzc1G8dh25JoSxn1TW9DXLkzxGzsV7i4ut1mgWOtkSXKj45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwiKl1srWecZKs03KINek7oEl4eaJD1bJP0dhZx0eE3h1VNOgtMadTqhvXnZ0f-dMjOT6dW7iAbqpZYNnprupK3aAIYnTZi_rCBK0wt62cJb6TRO4GZF2Kjfuc8hvuCLw39uoqG0y_fneJXtbvtGqK5dsp39-S3kYarETxvwq4pTdTBZHPv0FcXFj-Km1806b5NMEGoj07grhj5LeznQTPRGQ_C_Rd1Z6zKXZrtuT5efURk5WB2Z_wIBaH_MYNVIbCgZgT68MZ2EONT-9nthzUQPMfNb-c77YXhDSBs5byvq2XPv8Zs-OcTOjPD8jkZVWoTihYsdqkLvqfOBfPSUww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV_5e7ucrytPwTo1XoxCkq6QvGBQYJ1EhJgCTbeSLMn1rMUAVE1y0Y3Tlsc83Qkt9G9THWDP2oh7Emq4zG6-BbzOuomzKS2oMOES3GK_EAwsLVU9lvEdK3kDJJT1PI4ygDlzNGx5O9m46uBxighMx8K4XukSFAFLkbkQK1CYCsQgaR7TSGPzyREFk6CUEu39u42Q1bzbSz6a8PruAZE7Sww-vQjt7HK4NGLDwjh_105zzT4_3tYn39SyIohdCL8mUMhbKw_nCC9XDgcJ1Z-v2k5y1z3oiSZeNRU-5ra5OCMYsKRnLSAsTiAoDwurGcEaXMMDz_u4BFif2j0UyGw5KA.jpg" alt="photo" loading="lazy"/></div>
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
