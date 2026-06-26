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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltn4OWJZNVlDCMP03buI4RK01sSOper2KZY4zxLBCIP-PpxVGlKMqDsoszc10XYSesqjqzY_H-dy7-NNiWja6XVQJ8o9V4NoOWQON_f0QXMlLhlcVvpWMTeGDueSyxBs5nO45jIuDEjRWjjOtCt45oEdQPrO8mkj1vG-ioStbVRLYxL9FRkGnvt04s1FFJ6z2n1TQ9xwElMjUZ-5XOmuLzA7iVA6RSpI5R7XAErU6YODzVw_nmuKDrIy00pHrc-fXtKzSvNs657xAWry7f7RpBnodbnbGP9XYBe47jx0SqsEk9TE-FwpJFln54OvK_gS-R9XtgZ50TClNTZ4WwIACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 238 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 475 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 601 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=L_xc9xOebF6jkbPUDT6haLgkhkqCd8X0zv3Uyr7K9b8Sh9P6OHjv-5UFlaCCarjQj8IILJjy93lFwkfwvABtfDOQQLBsKR5D7Wfm2oPIm0q6DH2iI9TCL3kjvAHswOuGbil43Z_f-kROU0JJTXmon7-h_itLKDl89ALgk7baIL2GAI_CnCeSzZERpB1P7SjWMdwb0cSU4r44007E8R4npeE-Kig9fIj_y-c4IMUGgaIjJtG2UTh4gik4JXvsgRqyQvwaFKzvL_WkKo-3iiNWUPvsJSUfF8cg-HCi2Ca9OAsfAsxvDwe5ElGyfH5xJBpYEI1b3QzyYDGMrN790lQ5TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=L_xc9xOebF6jkbPUDT6haLgkhkqCd8X0zv3Uyr7K9b8Sh9P6OHjv-5UFlaCCarjQj8IILJjy93lFwkfwvABtfDOQQLBsKR5D7Wfm2oPIm0q6DH2iI9TCL3kjvAHswOuGbil43Z_f-kROU0JJTXmon7-h_itLKDl89ALgk7baIL2GAI_CnCeSzZERpB1P7SjWMdwb0cSU4r44007E8R4npeE-Kig9fIj_y-c4IMUGgaIjJtG2UTh4gik4JXvsgRqyQvwaFKzvL_WkKo-3iiNWUPvsJSUfF8cg-HCi2Ca9OAsfAsxvDwe5ElGyfH5xJBpYEI1b3QzyYDGMrN790lQ5TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 642 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzDHrQNmjpCPgzV4G-HHZcXJUFYn99bY_lBoOtPLVWn96IznYWHJwzbhxnu5wdOS22WpwjI4TpNkNoOPrmNNDzJwwQVLe3iafMUI2eTocQjlmRh2p8S02crwbjuKMh74GR4nTPih1tWv-7wEYF6x_pTR8e5upe-P1YLS8S_uwsMNmeDCtOkeDlS96uqe_bq_n3Od6BBZX5xQvFOvubljKLWJKrcca_DQo1vM7dcMWJ_wWFRy1dXf5vzQRBDHfmwCGlOepgLeWfE_XYmR5FYMWG2wZuUZiE1Z0uOp94N-NFgV7bcdcKH5QdlHqmGB4j_b2nHQ8dadJAM4bkhwZ-4GZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvTl0AqhkjB53bbBop9p_qoMZ5XH-FKlH9OrL0irDfQevCn6qAxP84D8lTPzcB8GIj5jre-tCnLRyo_xguzkbyP-r5rwDg3UFlrllPxUcXtKXYfZ0p9Ncx1xzjjYj9WeVYm6G4cIh0AIetga028hVacbW4UVM91-xDYBcSGhNJhNAoBfZbZS-uLuNymPPJ5WfSYivy06m5wbi9kRcwwXFhch1OcEZeLaA1sGJQ5JtmwSF_wCflWADZuB7xTu3Bp6OlHeDlRwFSYGhK7Ea-ynG9YJ0CInqmeh4RRerB_I5RM6Pg1Sd_WE4KsRIcuiClJbzoXZYgmSbChsTLSBYovTPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9U3YPln8mep7fmaPut-Y1FbKnrfbP717zGMvD6EB1gjZYj4wrDPrUo4mEuoDDGZojD0VrvsK--I4TMdtBt6yHpx3jgvFKdKFtDaDpvFkE7QNGgscEEXcYDesOmsd_NH3mYAKr2oUeXqNA4CtxbCorE-xT7ogIgB8KMQcklPOAuCsPyvF5JYh21-5Lo_IYvVDP1lnCxr7NMUqZhOyemRoXniWKSP8Gp16sJ_RYIVxVoBJ-W7aYrc2SXHioCHIE2H_81KvemIBEWQ7Rp4z_QowdvwFLrdzKMuePigyf6oR7queBVW3v8DkwuLvw-FktJB_1MZCo3Q8ZLBLSRsR3t3GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAlwk-K3UKMuyS_DqmZYUPReNQhmBOx66gELRv2SjXsldwd9wLZoRlmElYrdSTmjeRf1Kz32JsBYcX1TkLTozMAie5bquqmOWGVI1Cmdyz5Iu4WIU9Lk-oyj_VIDHrSGE8a1JB0li07erwA7ET2gEpVvbDvNSrj1Ltaz6lYdHmN6pPJXGe49x9T7vb7JdNzhLGTLC7R8ldkQuwb43K1lKJzBML8VcUcv01OOuR4UT9VAqIDzrwHo80PGGmS3Oxz2QGEkiq_d-t1lgqY1jpgUp8YA6x5qvLaj0ILP6-hDUihAJ8Filzu9HSokPuGzq25otOSNHmeTgZdXhFodesNV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myEvmPjyM4WvuzdXZpXcepvXg0EDv_PF_b1XOfVVIZBT8E-IjUOBZCpMJFqjC0QTiTBMkpmWIDyNATxMLs76DYiPMIFyngYSehZpXTAE1GdF605W0qFIhcprMjrxDFnFYhJR5v4ZuXgzn7FB_k8KptdxE_gRKTkHViIHCRNsFzg_A71tvMWZiW8axfJeJxRcciZ05FTOg9ymKcATG3H59AY98XvueQ47chEJJdPYtVbptFm46CFXsNLyEcSc_PTIinKbPwpk5jZk3gYdidJzWBN8hKOtQvHPTVSsPPHk-wkoKW3WceQd79wvbQGoX0MqvJ-Z0vT4VN6j0up-7WHWXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdAOVKPXgWWCDPQiDWnWlkB67HLotewKB37jCIg2VdmPRJcbPgmbM33DvVzfAjl5VHVSLsHXTa3P6msRB2Cn9NeKXBQtgwXq5Cr3NzogoMyfiZqlCHQjksnY3Km3WIVF-KBNd8a1iFVxbw4ZJqCT_g6wq7Wjie4sZigm-GUfq4IGiiwE_Qo0cmeY-5E00yvqDGCS9a3gkXzHvHRPJ7D76ZdEO7u-QjLSQohde385MUN_M4S2YHgcslofBO_QVFda78wjiY0wliNHOLxzttdkorWdKBy8K_wrhOxqqw7YLXdceNjuN-wMw-LMVdbbb6xFKhACsWX1456ME3TI42810g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saDmGY1Ro-mw7IZOle9o8mMR1tIUB9G0SabSvldVrLfqaHAE7cXAMw8ZM7EPUNUSq7_rtzW5UeSKWWZQVyIvjOwX4olc3PwK5qzNAsCRy8pEHl_jbZMGhjKz8aP3GErPfZ9ji05aRNhCb0l21rPVYMAhIpzwZHlXfiX-gvawXTxc118XkUkd9NOGe6oPJndzx4eJ0CasSkG_Yurvl9CokIR8u-Xk-hVCMWjAHeTUiDwuQdZh_LD3FLNWnDX6R6noqiBhClO86VntICEnkaWPF3QBtldj2BQknf8F31ZDtuoF8OYjc6_9oNd4Et-3ZeKhW5NzB6G6exoVr4Vzu7G5pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6q6dvE-DdTixmaEjtG0r9Vx4btgZEi3-_QuozMUx8brrHXzboG0KLa4gId4M8zc1kr1cCeQ2Rb4XdGRhS_5nh2d2O7spJviKWMOui0nM1nObnjTib9TWLyquu-IyfC5Chln5FhChErnWGHMJqlS1oU1zGct0t5ZR30xFEC2yhnl5Akv0RiIneiYoL4vEue-LVw5hqb_FfDwZJh20GCZDmjUGcLqKtq5NnBKM_BP5_O3_4WsQxjuorHDb86U_XqPGqBeq1b10rdTkv0e6MNugck1M9e4dM3mSFBaqhKO9ExmEX6jMa6oXaN2IkC89LyEhrpCIcuJyDCHFNCxp7lenA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI6DGDVBDM34PXFOTPnE2zuDHAbQ5iHA6svPgJF4DMvN8UX-_BcKA_C5AdvvUu8j72YerZNIYboFfqApNDdRx4SPTbjDYBKlIwEuaT1ANrAAf0rbR56G9bYQpI4NX9b3ygr3VDF3DCxWqcesVnyGxvlPFbbVgMxMPLNksYtrosI_M1ebyGUHddSd7DCeFDYOmHeUi1WwQIqJ5_fodNatnZjWlO-mGvRO1H_wIAVmgjms-Ot26TkAYZHDo8OnvIP7QgzOWKe3rfei_3MWT-xQiagOzggQs3g7U82Ag-oxfUGDzw1NfRSoV1zOchOVUu9blgZj-EfmugO6XG4qi1jKbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbupNPhKfbsNKE4m7d_jF9f9ljoUIt8GSU6fHhdDZcWOZnL_AvxXB6oDnbOXZJD1WlO_e0RgaOh3xvqVFDseF4RxNlQUUYu1kdC5eq94KKrZxon-avzUrngzROUWg6pw1ojKbUi2G5D6uaU5g3qur8ll9H8KndRQ24q_BArmaqRo_rdH-LrpcQFvAmPxwbxuNzoN1Cy7e9e5Lo-sTqRYQrU7HKtN20BKNEc6sCK020q76CU5JR9SLPR6uhE46QTcMnwLjsGKHoFt7odyifitPJH7KR2lc9URgTWWusmaMNEjre33gybWHJbr_2IhqwaN-DexwfecHtGMVR996tEoEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ0brfY1NxHljgBMSOUEh1DDQO9eh8L2eBIkxNl6i8suzNTfcBMUnXFKlmVjQniM92oBauajhebGpRvbsVj9f8_6p1qNJQIBhN26FA2_LVstIVjaUcRbfFmVFiMaPALk87vWuuwIa48Zkk8adxzc9UK1Tbwv9-dBEA6XSrDx4yfrK5pDyxCmkLtJiy6pv0G_mLRlPaSNI6_hpHLBKWol51mG7qoCXzU74oJPmU9GGrfQjTX2_OIuKp0v9B5ij9vGEHD2ECowGNB6re7XUo2U9N4iPENVD_1PyK_p_NZpDVXc2flALpVrImYkmMExd3TSj5W8-05n0aIVnTzyUyz73A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oz09NGZH6TmQJNi2bdzntd6fc1eDf2_TFJK2B5SIzlgbCjVnsMOgoLTAzWrH8unnmjHCbb-a_arkkx-EixOOimWF6pdT6moP59xQhR4-vNow-8kgJYmkjSnG7jRcutJPHpI9S3TMIwL0IsDIGPv5kcGYEf25d5H6GEAVr-avzT9Y1Kvl_8NEPhS_UQs9vWsJa3DhVuh78FxoY8z5_e1gCvDtr6ggYZ9Nmkv_UtFKpeu7t78KBbyH-Mvivcc0YPYXUx9uBszj6hfpt3lMoo8sdlTb70RaHOBFySix24HJF-eNn-tEHTC5nlxPgr0Tu2CKrASYlDsklMDnYsq22NyadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhuuTuH_Fksy2iGq-J_zz87WHxdKQQwg0Re05zwPFNOMVLonyZoqsnbOigR3wozsOmyNaI12Dbw0lSMrKanlCzwPJc_s05H5u-4loIYYfS6mjDpLKjxd6Kp5TAw3ztDRBi1AIeZnpj9QLPS66srSpzRvYqFNiv6XlJP5hxajpT0Z752YDDiozhZkM98xDJ_sjcr43arvalCk-KB_WZdTIelFBnd3zstYJdc09Hrpv7lVDGGAX7GzNVmtXgvnNwcKa3zhnkBHc57eZaxNugIy-i1jX9GKEs4KBYeDqVCT89KU_fWXCE4KUPVKFQl1wcYJfGMY_Xc8NfFji6okD7_zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frVqGi-Sir54umf3qDQ5gVIYeQfopGRr3fwn4Dkj2kXbkfiNyzc4Dh18TxEEZ7ISZ6YOlJwfKAJzsN8uAY8xujEuTwSiY0JsPRyD8QuNL0oDPD4EhwrGWBq6fIEtWj5ETssKBNI6FnAabEMlZNn6iseZEr7f0iLSzDXVXwUlWjT69tz-PAJ7i11GL4x9FB2oHEIfZ5xqKENNDcoxUi90oG5rCvlAlESXI54CF1jzrLXdT8Gxl4LUTC5VF5TG_X8zFoxq_Ims2lq6Bhw3ZqHMsExZA-y54wQQpeIPUk3-VpHo3kpUdNvEp2k_FnrlPakbahyW898tqxfwGcwHZDC1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txilEQmZte5weRf57E3IElEi1vwfiANovxSjGMPPBBDfb5_0KeXBZOOkc74uOZn9Xjs9nNS-ShiJqxfB59pW54FczwyXcdF3Sv_mmMb5uvJPjtlNBlnksG977rMGRlReFlD_p3slDygtOu6yeL_BxmZsViyC7lYq7nbkpKmCgwpS1yUhze1w8mzKDKUpmWheVgyzGfCRG97sOSI5fKbFdqU9x7_4UBhy5XiGDYQkRpnz6fx1zN4D0C6_B2lumAHCFcrLW8-jFEmmV8Qqw3yqNmSlXBy0d_CQ3s6_PvdBvL9JYf9fv1vpu-ATo6SlX6wQeIAKXJAW9S_czNsH1x0CjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvXJVGYLnykpQrasMR0fbvDAs-XNo_QE-XiJdJKb-zShP_TvUWtVg1AFJHdaxP1wrKFyBzj34Uj4ueOEGCV5fI2P80LgRwuvK2UQ7vcT9CDADW9GF1w2GhCbneiNz0-DMasXechyh4fdzL82ml9Hu6VDu2gsVmIyqe3tPKK1uLhmY0Kpvt_8dl0dUlJBW4QlvitqBLimFY0yKcd-msRU1VW9-TYCxWB7vo6afK7YIJUEc-cOpWxhsfxlhsoL4CD0UfTqIOCeAQWZe19axfDC7mll5aw8AFhEeFc4-01luJj_K5vprghXl7jfn3S-FOfF11YyPzaVc_XlM_T52SGgUA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=bcRjNWsunm46pBd1AsFrYewx3FWyxKlXQBPBtBWp3kegZlm6Tby0AiEr_o9P-RJnVLJEx32yW9cB0SRG5ni6wvBB9O6XexBkPIqIpvQ9Llgdq1b6egwC85McYTi3ZLP8620LUfvdjgdWLjTXgEBVno5xByW8P3MqrBT5fQXx26Hunua8xmaTspTmt5XGcRbL3WITrj1C-FcI1ehuQRhyGxp36BpOCiYfdw3Hbg1VT9qsOtRlSiVww2BGDI2ckdCBsjDdmgzc-6kxnZKNqvFezgujsc0ag_dmMdBrzBSs--Ac9w26FRJkZztFKZLbDOg2QIIuUyRp_tnCGz2YnA0Fog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=bcRjNWsunm46pBd1AsFrYewx3FWyxKlXQBPBtBWp3kegZlm6Tby0AiEr_o9P-RJnVLJEx32yW9cB0SRG5ni6wvBB9O6XexBkPIqIpvQ9Llgdq1b6egwC85McYTi3ZLP8620LUfvdjgdWLjTXgEBVno5xByW8P3MqrBT5fQXx26Hunua8xmaTspTmt5XGcRbL3WITrj1C-FcI1ehuQRhyGxp36BpOCiYfdw3Hbg1VT9qsOtRlSiVww2BGDI2ckdCBsjDdmgzc-6kxnZKNqvFezgujsc0ag_dmMdBrzBSs--Ac9w26FRJkZztFKZLbDOg2QIIuUyRp_tnCGz2YnA0Fog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQAhF88t_4aJu6qeUZEN_0wEKAQdotYtc49qspP4C555RW3PJ8rbEQU2PkVxVxVpRPs9QDhPc3dHQn1fsKEMTFhB96d57bj7pu19T4IdnQUsln7hWbmkF8iOiTYVOHnFGNz95uX9zF_Peed90XlAtVBCtuvJyygAfz_2YR-gwGXjXTrcuE-rgOd7_5A4OQa6RZknLb0ovEihuJnCUYLNJgM0qN7bziza6g4AR7gKU_0Z5gE4jhikYJyvdh6KHiZzdj-FsrHOe7K8aFGK1hyyqpSzoHh_43wbsjvw6wjm0JXubdvR04oKkESHCEvABCv_4kek4ii2DjiURG1qZoCrrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6KT12_v6aXnTb0hhreXaVCQ08ySh_gDGFnvyNXenFl4pyGtfnPA0Gn-qsKZBUUxLUkGuId_jd2qNOATkD55ckC6_ohxaz05r4aTj63lHeHgYsT9kVFIAPxbgXEvRorEW0EEKkMNwonyraE0OrfwiChG1GH4QaG7rPTBiELTRcbl2AQ-CArOzGzi8kYN88_nT3JD7M0zDF3HN_ftNeEunsr09GaN1TE2WFq6PFRBwIOqCHd2kiYRQ0scFmcQ6XDjJdEaBJexBJfPAHI_Vfz8ZptTeTpoNgd_2WLYdOa1i-3Eb47J1UDedzfydlDJUxepmNc_rK2EFThL-vVm3dnt_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mq_PwxzwObQMrdecSebtVNSJP4Ag40eC3b0l6i7Svbs0JUfBYFiaLRuMkhChLO0o9sDb9ENTZC90povkXKI6823IjWIiufLxs7HDismuWfuEPurlikKysmNWIldfP0Mey5kFSPfUAxrG4gsCtK2yJ0Z6EtKjO0JBNzczDPMvJ-qwqMFNHhRO5iyhUT2S_0tuBymzyNXy-auyZKcSBoDA-V5ssM3K6AdrV-IGoY3LEL1XeYtJ6BA91FjtMy-0s7l3u7Tp4kw8AFLEeIeGlEzbgwGdrQd5UaoCiRnAiHSWd_rqKEB5EO-FnOprRMlT0DQ8UaL9oeJt85daOuakc6Z4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fppM37uX9QknTgS71Mvjson-GJH3wEy_uru1q1l3l07dL8LxdjynfpGdlnwyVnROk2JF-IWr6JrqpPuLkFdxUi27goy_YIyUaPinlyLfgvGyPa5vaLy2ZpENTpSR1z0Y56psHd1SmJX_z27tHVxyyPgGuXHQBXionf69ao70gcl8afcuHW9lIO6JNuCi176BPa14khERQy6P84u2igQQelaT--kNBHxF54Li2yVkoki1ZpswjAWJYERBJPKQ39RSDHFwOrOxHwBvdijSVjtFp_EQ9RB3NkKIuNeiBwO3KV4eG6EFlc619AJlpiHiY5FhSlUFs4ZuYxrG4wqkvyDeug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuLb_1pfjTUsOEcm9DUYzQ5yVCnIYAKnd566m3f1Q49gQqZqnRvzxV4EmxQImcmZ8MsrooJngsHOnDUudVDF0iJLJdRSpR610_wNRYGT6ueIVf9XGsKNbh9yUdnt-N3RnLI5D-ExCyFvllF-pjRdXZAbYCe_-oNxOg7P-IOKcn7xJLLbv-0etcJC9APP7dWxC_NwhRcy_GyIlNqSRGuphANpnoFe8ytVlaZdlgF5jDMkDIGpqV7VNqefMoUURuygzC8hS_slHchTBCXaqA4bLwe8Yr2HrHJ63c_aRbLWJqrN_FGMH2cOPNwBcBGGAoHELox4oH9xJJkuJ-CoYHs5Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQZbhrCYoVGNkS1nobIKmdOms5SkgGF2547-MGTSpHnJu-yCPrDGeHn5z95MeOgidf_I_0PmhXSnclzTkQ_NOL8SKUf0V5nCOBcftoLECEnfI6uOOev8ano-6ID_urtIAcPz06OMRwKTP-q2krNtQSTUx2NI6jBnhp5Lwnq8grp5AX9V9NFwIdn8MjQIXLH8o7RAE03nfLHPW8NpcgQb22XjFILMW6wBlf0ATdK8z1JUlMj76CVQq-ySxF1puqpX-ziI2o3zroXQ6h_Nugd5L75QxCLNfMUow2iij6Al-LksXhlRrJRcPWeZlgOjfcgJKK43JqNL_UQCdOVi4H0stA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTE9En6UY_M6JtyuQaWQ96TMIbiVvYlpkJQpRN73kWN-KjeuRuX8n_dgzMzQgH4hCGN88Qsmm2-neAOQMF7d2h8mA_3MliP8fULm3wWmr9e3NbseyxNrONNpMRHDp4PqjiY-m3YuMrgFtuQtT2lcCyeJFiSORKmNqtOZsgqu4LdbbOLbViK-9dhhxaL3d0kKwwI_kFJTvbHqs9cfVgKjZj8MAI0oU4YI3RQLoV0xcI10Et5vlnvNRDJm_NQJF9xgN4OpwzAN8PGZ_-OmTlHNiBO4pCdQMKq93iCLEdfAnUVbNwQt5zR25zEPuMq_JhXUEnS46CZSK1ZkN5MFvJDuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/du3UoXcOrDewt1wUVVG7QF6yKhwsWFr0KdsT2KfClAPI8EjQrv5W9R8uuVvVuAxrDhH0Z24-eXV4eRo-jqluxXB9rCPs3y1mmY0PuanaD8hQy5jzWHDC3useNkrfj_HQC5ByFyr9Rwd94MTHJa_Ss2ApfUUGpYlL0moXvwFGTDh9IWZaVieG8wtlv8lugr2127lw1Lge1-PYuymCO_CbTeQXpPYaeudMVdFEI2W0LU3Ia1RMmWJUpgIJQRtZ6TnSmK2OztYctTMCpnkN2D727uk2Mz-htG0JFPLAoLYJ7ApbGQ-vZ6x-pQ4DdudKAX9aFIup4T8RqEHs22Rq8EF7qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlLhqDD163gbfYTFA05EAPqHkcfuuxJXZjgEVyq8Mwvh1EExZ80OzQXTSF0YamaZ0Mt1WyAqhHavaBcuXE97VIpu35UwHqujW_Ror-wAV4ZR45BlO1LMvkMHi2Zxda_bJdYKX1EDOxnJGT9s-FkOcj5u3DW6-izHr8AmdqStGCpCG8JaJRsxDrUP4EXsy9aN6o4HLGNEJdM_LSI8u4x5doagZLwI9_0D7tABLCqWy7IzYfeaXCZzmO8G_hiMYqmpLvJpH2THEvNpljYs-rwlxJvo1ULe1X-OOIrHV45omVfYnObI75XiXITo_s7_BiT-WxpnxzGi14Ej310BWocl7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Weg9_X5wUjnDQWmvQ_3uInQ8tMFyXg4xEfgiSdcESjvg-G28AN9bbWgMheqwbCeJw8PJ9Vv4l6PBFnklzRU7zHrBc_nyZ-n5xLGV8GDpr9mKnjIpuataf2MfSFwGpowwKA472Atm9F0qJbcKyB2tjvuvAlFK5hl8vS-W_7Yz_Cs7gZvZQUB3Z_jaBzBzW2874KEX2hCtRGI_6cDQJX7_bIeRkphsHtKaC9fCcuqE-Tl4JSLl51n7xrtbe7IO53Dia5a5SsUXV5IaQjsPif2BWLA76XgYacosJ6pj7t5MlgxQ3pyxceJAZveZIUpfBM2rgU5HSrf3CZyzG6j61l43Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_xGO-WJELT6I1lRYTJ2nT50qQF0wyEqSgl4a5BlH8pnj94GBdEHa-pGBUthZyGMmKNarSqoMu9obuAz6SGaBw_mUgKrWW7wCiZ22xgiNqlH8byUZaeS-QHuKiw-jc6Nu19HhQvKYxaCwxj4JHl0QiLX6taw5YZGHFedUxtIC2GaX5fP2_WuzCPEl3PwpvvYW48mhb6bSu4jOllUYj0b7laJM-Fj_m1xErV1u3kFFH0NH6oZ7xUDbecSQURRa15vYf_e17XKuOsgGCWNUlSWhXcin4faA2Vb8RJt-nRU8oQhPUDfMsuT0noq7R3g_M3kL3cGz6FqgU9vDR59556_Xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USGPsQdDoyx1uGonIRN6xPzZIJS0Bi8CV8-SN7XnNSXoyZWb0hHydkZ0VVk1uYe83OXRY5Esvurrvt-iJJWWA3iu2IEE0lycCkShLlmLorAUWo0KS5W5vCZKsj0lEBzwice92vybXNHY3n1b5PEWitmWNct34ADkduJ_8Is6wImZtAInGL_zF3FV1oLN7PnnbgOef10bddmQg2--AKjJ7Im9bchHUdZ0TxnWmz3EQmu5U2fvcPGZHcb5ovpgsxaG1HiWL887MPR6dbdSMK7_8Fr2ht0lvFPAvKIPBlPZ9DYfmz3wjmlZRzN38sOHpSwjq8FhQohAtyoqM1mMCzLNhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgCJ7f4iWLC3krCEXyXg2QqY66_eXYQwWA-C33xu-P9MZL54f9_F7w9e4DT4CelUMi2ygSsR3bE50eGCXb_jCy7GVGKKaom3znKNSL1JXa49fLrBcmJRNAuDmooeY24AN9r-eJkzcGknllMe3XJO-JXzM3jwhO97zvZeSjBjXx8zpft_qrl_3wBAy_yGBFiwwG4aWpY9D6IWgqd0uxnUoqFrsYnhFoR0-NvEKLbU7_-xfYbyL3wEDCwZ5Lr22UYOLHgHFTG18O-j1UQk3dIt4Rly2TBkLR9jzIw3ETPbmmAag_pSFMtBsPk5EBBvQuIsqcb4dG0uqWb-zTGfe-Y_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SS62aCTUyU4TDWA-gViHus3ZBLJ7br7qf1bZ7hv0GB838Ca6zWJK9IXG8rxYe0ZLa7pMjyekOXtFbIJMUPSL2kqVN9CZes92LlaMssoNYCmYzIaEMyulz2-LFW4D01g9MrLW67_N1YucjZuo9rv87YqiVPBFS3nPR-AGdSK4pqtOaPosThJIJI9lI-BhwAhwkllobYlNidsyG5HGv5JrksdlJWfXdZQ8aZ6CcSunuE3RFb7DV00OemKDQ6ecVyvrvOcnT6EQviZB_bO6vWxNJr6M6R7_Pb2q-ZALqxSajUHEM2rd-nLpywR1EH61ldjoijqLo66d_naRE_aa_C1UvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OT-RfhL2ktpLXcvLxgEa2Ukpdgp0BKItUssYrphsVguOQkIndMXlkFAR49q40fjVEYHczR_ue1OXgijJHB4bFu4hspQjPJGID1k0w9paHXRnTo5SN_l689sV_SL04FoAKY9TjCJfxnsXs6gY5EiJ6BrztG8-uuJFMgFF4EW8_wRAo_rKTyGOKw3-CGtQT7wG8XlkFaRjBicCxX5a43QNP1H0WFWFQqZ_pYI-O0RmB44tFEpyyplb5RWXulpjs5V5DSw99EtWfMSM2-vuKZ6s0Mj6dNXiUusG9Edrvzp-f2uWJ7Mf0ejB3SMyHRj1057p_P5Skb1t_v_5HgCIDEIDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMfoHRwMgiKgyr-usYXbjJnpGWe6Y2UNqypNeDwDF_IoiVKOPqaghkwLdYmhVXNmbhfcOJFsBcJyOSmMZIkGpy-C9FiDFYQgVOGLp9TA1YgcKbza2n6sp7rq9UrY3TchPqSIFHnOWxOoLUZQYuC_c0VuqwVmA7RAlxYKtcV5-FtKzg0x9g-SWRkdE9GvRvAXopYHd7_dqQzBGjIuR8QC80S2UDuxrVs3MpT2VSCGeguaN--KrcCi93ud7KBLmx7DRaGOTj8QyG3er1CblXJLaZe-w306t4haD3KNsB34eBIeY3zMmEYghykRg6DEZXQB6ZrwpgzZJAKn0SRj9RIhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oE_5TKQhAuXumUSVqY4wvA3ivmYnHCOIzFjUCIw_Um3QAZn4q_I3vhufgJ0kGkkwv_dF-lACYgw-LbeKeCU244A4dC3w6-C2s-B1HT2IYwG-C9MeLuMC4T11fVklGm4InYZyFeV93tSmSBItARuVRWgQj3aoubQMTVkyueym7g3ixLCjIozby_I33dQHDIwVa0OKXFEdgcbMgFuijF-BZJx__s9GCUggZ7X-eREcc8uSxIDls5hOouvw8XwMX-JcXZK0kBacLYPI4Wido2WXcCEZ3-vnN_QZI4YmLTNGKJl9mePxCUVJtmtmOg90p9sq62fhaewNRSkvTrMZ0fl7JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTp2jpgmUXWpqfgpOE7DhKb01EK-FI4ignJ-Hr7FzXFDoTZFNUnKxWVaIiQfhEes6qO9HlZ7GbIC8JDUH9hA7uwHS2QG5hNqrLeVxbXyOi3w5v3r9KiW9Zeo2kxyCAO46i--X1J-4UfTDI2cPUYV29zWX944DkPDv-RyA50fx3MfyrAej_MHisHh4YR_2FSWk4OuQwyR1s-nIXPFJ5E82QyMs5SecesLkLPT2qu392imcVlsbkvUCOPLd6Q-jfyqveHepgLrIZGrLnzqRnVDIqjhum2PpRua8GsoGLYgaMQJ3dltdRG6V3OI2Hdxi1fyk3-h60s28huNRST5RsulWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAG05PVfB-wDMy5zISWQf0T1UjFQ_dUONA4VZWfwAmHNiIV3cfe2KK285v6HW0VwqgYp7JcgZBJEm8JzDp5ONgUQHV80oVlU3uXP5R26HYNgafb8jYwJN9yT9a7zW6dU7yAMs0BkXSo5A7DVGwYxRp0ryLuNVqOM9wyHf1Y-Hmz-P5x7jLSkVT0Bx0M5rUC5n-LVRyPlmFVPwt9ORd2yDdZdIxe0UxYy_M-lRR6FdedKIt7xNczH0iN61MBK8D1I6TrpVtrhVX-4sLyhnzdu8nMv4Nct-oSTO8Jj7NSDWExDRl9pLg3QmDOnMtUuO16IfRLEBxfQsbSBzuDqr68cbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuiHJGXVOIXDFzFdbyKxz6NoK-vY21rg95WrB1s11JeqBa9xGEN5ohNxp10NgJrG6jTzPKF5tOYF7HsMgDGx7doLL0wkK0M6E_q34fLfkkqdavHFO2fc2ggUjLUCpljYIcJXT3_ORy4xXpB3g-HFrIQVjomY3ppzflgk8SEuYt4cyM7Clglqaz4QRYqigMohM1ugv7NWmvfOeU5dmDwEGiZAwm8Mb9jQXjlUXThxuVyMOylUwEr4ML0ESLmjFG7c8SL1TN_09VIG0BY5ZkXmycaiMxQq1dhi2VOoSSENsjcIPqzsungeEDuLsTa3DyrhK7ue7WylGr2So9XxLkYojg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcMPVNmDWw24PUymqFmlR5NFMVBdWphBUhDFXKV4tNBNqrQLrGGLn_gLXZxHl1cn4yhRkaXKzcAlkRa5vyhRCul0C9LaO7FUG9MzM0Xgv3eUQxu8hQOIVM-xQ4iB4IiLR3PrpSr5YL8plQBz0nPSdGoSLw6N4RNUsyNICtsxC_bvrZkpWOpv_jLxh7f51EsJUDrFZPVDFN_QbGTHBnkQprCH8qwGpgsptW3sBJJNXvWhNjog8suvRM9Vced07Oaom9m8bhNXQQJYkSfsDxkGow8SwjAafZAkYkLgH-WtM5Ytu_SfOWXxW4qblZMK6BSL364DQvqd95mMwiKDPqYeKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTTffFnX6DFa6Nmah_fAeJDtVMFPCf3r9s0ZN0hzv3Kc3FweW5haLScr3CdjT-Nc82xIVium7-0OhmHzG0hBcx0goV3epK7-7w9F0q2qqXyZyqjOqbrXYS6Dw892E2a7IcGyu19LgRdi_-TM297xu_7cBipZCEZ7LpLZJgLeKdn0XFhyci8MkFfFz0IN15zOsnM9tG3RwLUMwAUZ3p_o5Td7SijK0eUrLDQ0khqxShk-ulQ-HUeTr3uzIBNm3VrCTFkyaFDPhpdfTPTzxd6cU6T-amz3kXFrK5WyhwJK5dtDtem25ur7c-cX2CktYMERfF7Gw94HB60tM1awivZzTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqsIS_J81zpbDzGWqBKuJNckya-_oh8lODSvvuWomAzNvqTwRPrZnsKVHx9-qVYQej9dLhld9kK8_gQX6iVmRuzcVQUF-e4HJWzMLFaQVCAaabmn_YyvHKkTGdzWQAotD1x6XEwMhR5amdXkmQoDRnqOqllFUFwZwBdrzJsmH_W_P2MmpbRSjzq2g1IsAcntdge757tK0dLpN330lyF-TxTRWTXAs1A1duEcmNk1kuDvtv-K9ZdjBzVKzwou-MPty5UgEyF5P6yVoX6WTbuM603-GPvTEKOG0pT4301o3JWWpfOCLgpQHtVo2frqfQ_U0fPf3RT4yVy6q7nVKwX41g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8CKBWEkkqisHmKLC9cROec2VfF5PUzIyH2hKarluEIjygBl60K1VYxzHucX5WnGlvgw009FDGZ_FkFH_Hv4W8zx3FA82EkKytfIqFmZLiGvWONjWbCIvoDjAR7ob9qd4Vplx4Bh_gGquTlNPCY4j-4OdE6Lm-dPNpV_BHKVgJmCxZwPd4ZpyVavNJZQCTZ56xnb4BuQUVfWXza2EdJ1rPUsvAHuFqWTDVlJa6V0Y52F9xe8L1jNDl09JwyQJVfPVle64HDwnaMsblOy-tWVsNTycP50OlCdEkAkQGFJWEf63peFyb9f-heIJQHJQ_jeql6rS205Cmx4LIuGjvO6xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCrjwg566BmH35TxL11IJm3ua2wdv1Z5MzxDqX097GZ46MxkuFuI4RdC78_ks9yXp0wCDGfL51i5wIBJf4nb-ajcinMPNoWWfWyEKaOw0riUmu9V8WBu4jF9sVE6YnITgzFF2fvs97o_LgnD2PKRrdxHTtS6T9ocFdSSKSapdDoAX3BVm6s-4YlfTVa0NcvsH4s_Kvu3czzG8g0fe5kwepPNRNplfzaCKkgEyATdSHetOcF_Q0KeojNqm3AAMKsOTTJLWPAoezKKhMgMjhtGyTF2IT6kYlnxmxKta4ndCV_x1LZQvlXDefVC_Ha3yJq-rkfUQFxEyQLmRW2t5Hhg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPeFfntMZmdiVAA5u8oNhVyMY6P1F894RlFccL5gPrkZtYFHVmG6xcriv3Z2Gi3j6y6eRbe1fuk-T81jvFXm2lF8E0JcEB5nVPHjIZqINrhnm-JRBjsvnjyZ7FxnFCqSpGWQ6Jt_ymoDGJ8sXJtl1cQHow8juZNXlQhf2eGaEMuWE6qWHZ_7EZJSfXpBHZ6inU0TEWDmRVB7vCElg6VmqdnUkVl3MDcrIB1WAIWBWDNMeAHXx-Ej1kmg0WCtzdtctrlFTaEgGOIeEq3tWKgFU5DprJF5YopENd-hUpIeXelQUJZolEbl7WpU2BEIfeuzrByw6X2uX_H9FVVPrGj69g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJWkjgCtUjgcq_zRVab90xfassMCNQLnY0vxPo5A653dppheePkagGENgWKpBc0xf_mL0oRugZ9YNG7nl5of453oALXZdgh8fTyxwKTepMgIkjdLJ1-SGmRtNV2eI8IDd1ALeobfD3-NaaESdG-YiNmomuNe11nUwZjrfMJKADwTmr1IvLKY8kTmdU_D5_gvIYFKdBnJ9XpjYR8JgxyIFko3btktDElY3QUlV5MrESunVRfNvgRVHejTb3JI8GWynJcELuHhhI7ctwdeAaPiGdID8shOQkBjYsAUgu_sOv_7PmOZTh_QrJA8zpIaZTA6YQJzyFROYVGHSusBEF399g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDQKrpBMgnGF_GoQci4wb2rv2LHJceZzMHDYm_XYcrRXomHahY5VKgGKs_WD1N5g70qGayTdu3htpnqMwz8EHs8uanViV9G1cNAbZPlxYf5lD0z0wqOt7oFYAjbi06V3R93DNgZAHhUx91jVBz2lfHepglIIAf_9HBi-Po8iqCTAVrshKdnJ3a68YprgFwhCAAzAm4CuA_yXId6qPBe-UScWcrUU9prn-bbrjHq4Wn6ksSL3w_-q3HaVoymri_GvEDGRDUUf3uq73PW0cwBX4AJGR9UbcCwaORkdGJDg6ILS8shRJ5GM3bzPMlA-LsED2MXWbYGwbY76pkDGFqsiVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwUPvokfkz5tMdFNwqZyHOHj73SAFZwY6jDLXxGVaVAvCZzE2HiJpPYvDN9KGB02ZvDWbCSExvGdXxYG6SK-U1TKLKFYAIIb1QSqArn9EEKweqGFg4m6WmDpe74z53dsazja5h1Qp9RBLeGHwBiA9CUtT1w1cQqVeW9_JrrLxI11PZIGao3mHgv0zJUhmBM_BNPVkYuK3ZytEq3bjszMan4EY5OEv5CmvvuY0b6XIVVL9_D4Rjb_UVy_KnEOYaVLhPF73IHDFgk1WEFXLxK6vflE_psqZzPuLbKGHvW5G2sp2uhhHFp8Fn1dXL02ArvpOQAs2Ruc2o20cP0JGTfiYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9_CQrwDVv8dkVDw7XYf9e65xWyWsG-0vVigDkaR1gkzKDB0-8blOQfYuLwE-b3JCF8x0fsrBKPawaTqm1sKQ41E3CoEY0-x0F-PlfjwMCewH3tiUeQmqxN112VQ--aeqJGDp4bdXKhj5gN7DA6kjbx7FCNwUufiscXumQn7aO5iicXby_Uw_RLSdTpvwkLFAz5UUF3XgYWbWeV89VLfnlBRq3Bdd8DbjSbLwtANbQinxb0pXAcTOy3R7eJCXSxEaQ4UfeIrf14gdDGj0Mm9ahq3jB2DDelzYY5rHbekYmVoKFjsNnd_KC0j3fjdUcx15lPz4g5ARLFHMzl6D0G1hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csden90D4qhWrk-20Ks4NuoZ5lad6xrj4Wt1mzbQLtny_XhGVqUYJMIc9gkcmMAnag1Yr4fggdxZ5QOW87lqe-x21st7K180GuEDycX4ysw9AkweW7brdXx2EKOCOvbQv6skuGHgjFguOl89uxLrZD5-l4vkWYFxHmAA_Z1LBzWvlJ0yO8IUToPxfyr8QfIjT7W8WcPxQyCauc1ELDDOZN-BTs_dBculXkw-DZJK8l2urLNLSoul955cKHOqW0VfKH6ZSIPc_gu0m6MGHG6beq8qqquP6joGtsUImBXvELqV0ocR8bU_2JN_rv9sfVcCgWFw13hG_sXvq3EcsKzQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuBTvtusW3itS5G1QEe_V_JJnV75uEqhtYB9lpjtU78HmF1KW1hyQeIwIFeyXRD0_FQWkHBRspH6wTwl9DeVftRatDxItfI1hRJjrgGABuhxlzLwma9wlhI1dHB6Ok1Qz-m4e-M3ZeRwDMs2_cz5JZ5pn3i89JTleywAMRNw8nnEU0qXlBaIbDXD-K4H6tdbmQcFoYNBk4dMdh5GfjsxePe2Z9WFVDfuKix3TjHtC3WVcLC70RDdckQzXtqp7QkTRns--k0WDMhKz5Ru47K_TF1dJEyAvTN3jBiMrzvMDi-9QDhrrJ3KthpWocIHB4a6OzO6sUVDdx0VQIsiRUO-zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOI3kbvfDeC8T7oEd0jySIK5tWEcTJbCC_v9ZXQg6GTODNRUeFQH3j5RyxfWkJemadcZgOcD9EJwzajYcqFYBR6ElNmPW2wyNbGHr9o5UGXnGfctJEXSZbhsKLStN6G3E6Aoh3zfU7d36ir7Lib2q-Qk6fNvMZvuXNZBOw5m4MaLvhjf0ZQ0N3mx8r9G-b8J1bfAEVZ2pdlFxoZH_ik31B7hodhs2vhXsYboU77Ub8F0fV6w23Y7ALoDJVyc804CD3el56pExO9w5IeiioN4Yd_hzqQ9g3kP__NlyDMRyhKsEaqht5QG9NLMrONBYJktTQ15FCc_cOuig6buiSIYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnH1KqbuKVQj6v7uquJUEkPcntqfD7eAK2Gqb64TTcnfsmrqhMTr9Bf_g0iBO1O4vXfrniv6LWvZu32waY9wylaxVYkI7E3NsW6iXzxDDD6q8qyq8jRfDhh43446bAY3as1ptfK6U6dJkz-ZVpyNkF3coEP_9uNnLsBq3Ws7pgLwxXNjQw4mLDmu_N3XHUP8aPoa1FP0UnHgXUVYRgF6Y5yqcoxERHH5jjapzSIi3ZSC52SQUCqrsICJNofJw_O7tFbnrfrD4HpUEhvtDK7WAoMy7O-ifYanvaY_I3ji_DLXjYgf2M4aSzrtlk0oNlDcyqAUiKZ8oG-lserNTrJ-Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MguzRrN96fETyV4IGh9dNYoNCnKXAwp88l3wiPKDRAqdvu5FZGIu7cCizCtaXkoFuvyaVsFehHujJwau1_h0NoSzraoBM-5usd1bs30pxZ7cwKay52wm4kXvKvRoTeBXMFdf0PlIv2TpzixhmMWczdimLeavGevEschf9Qcus-731PHG7dyFTqKGMKA2mbWc_uVM2_fRunGfhfSIOmSjwkjgl_aWobZXUBas_tQTyADZTqllROx7dNT4_EyzNYerMbrQKqj-_JJx0c8JVnii6b4NQ-WhAGPi5u0joNB6dJ1bgtNjThbTYmK3YKswbyGyQwrs68rYPYpQUZVWbObrxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jiQ8AQ-QM893IfuxX2Yaqwieb8TaQBRRNK4jxto-rknjaTVlUSTtbaqBfkX62f0CFK3YAIvzIs7t03rAlgWTb6t92LRIsTLhkIRfwk3T8NceDHTFivZTAwcoYMYwGmKhqJCJklkwBb5hRQrivN5EOBCGC0_A4KxX8fh65eZauSVTU_2NDhCTUd3GrPL1FmbGC9vOpHIYvTHrx-M_cP-Dwo0Sen7j9diEJd1F5QlTo4CJXCi-oymeu2l2pwKktB7r8tsvZImp5XZ32FBCnUkEKc-n0meE9t6meRx-CRVpdCxCFe-rsSS52AxpEUxhdYRCtWxH9btfEYXZYdsrHiAadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTUh5p9VUyescN1HVXNNFeuzKX2FSCmGOMHlTX-ekiwOMXPk47ZdieHIhSX2PxMwZQjoet5OWGNTvj54aSJz-ydtfLw0sGyrZ8BtV49ecUDPpS2CGTgM17E8ghlRY05ibb_0QgIFk7lb2NZLMhtOxEBhb9n95sCtbLkfrBbvCVSUu6z0CY5rrhx8JnzUGEeka3sHBZmoZxbLsgmhd6k3Q-DPkSb003K73bdwmGnFG9lAzcvj9oir-BPpx0rycWp3qrJjk2HLjwL_xa3bb4a7nez0TyyaiYCuf8cLunpD2zW8EayW5HnySz-y_rbaOSKOK2ZOLFzNVHSuYR3zMh8FuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odap0iA--lsK9MQ5NkEvoRmLe0HWzTyPGW3mfl67P3oHA6lZQJRap9TpmjSaz-pAxx1jrqH98SvLRTmEN0-PoIJDGXGbk2iNaBPyRd1CzFuO6GKDNuYvGjF8b_lGkhd2e1pEuct47IaCZavnJnXxzlSzomWci_o-hIWl4RkJPf9hj9imnliuRf3kLW7oN120qJVCE7bb3Uk3P__xkdDCBXUdWZ2W6xOt0X0qOjIBkY-x5EGUTxceD5VbVoTF5siDh5IMAwJDhyaNFxHq_lWx66o9bZAHa5JOVKNIkIf3rT7XqsW9TVDbp9tPL8AIcKL74e9JBeDIk_qPh2xRN7IK0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCTQpGybqvCKuWX2gXwUgG4FSAeU8mOMFE0Uy7AMWBmmrdi8pUdeNbnFGsLsxqIANtDx6WxiDLRsP0GXqOScVw2xUskCAeOs_Y2Dxrp51QMLvaYtVfjLxt2BY2rk0MIPuFkqUoVkrMobx27rluW0rUufzf_UtEljn_EU7kIlsGg4cD-fCApffUrVnN6uWMc23tQ1zASThp_483TJ4d3e9aLm9JsexzJ_VxeQwwXkCVo9xN4anMDYXa4TZWKN7dm7Z_GZjpcET_ujuTJNiSVOWBRW0G6atpNWU0uKSjky8wNNUFImzSvLiT20xa3IQufI_bIw5gBVumugwtBgBSAsNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLVPWszebpCf3m0FTHTxtF5IgOxzAZ843e37aPQvPQbj3Qs5sMboTsCP_cL_NTSzqoCBjNJdJ2EVPXgQ4Wf-dJnwmdySgx-_NkQ-OrMEYisv8PfsIz06eHAH9sxEDOXH0PSa0xPSJUmr-5ACGCnS2dRWrtimqXn6DQwEhEX2qd7B-rxUhxnC4L1ZG2yoNuDqhnfi63Hrep2MxSsS-gCxGoKwUvHWcjB7-hCRIjNHuRGQgXa0X44Z-NviU4oj6hZyFij_c-NupBspAI_Jw2JUQj0N0QMvKHvfaPwi9eE-H9hWMfMkAmhqTsJ3L11-Mje6ul_za2RZHRwUQ5ybMkv-rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNSeRIoHcrs3qNJbjAMEYJFEkUaolObtZJyw6_IVxYHwmqpWUYHXTbCwweUFMEfjwbjmTWykbwScvQkSxPU2chX0wVcGkEYEf4oUnz98DlNvXSkkmAKcFhO7sTJ0txg4bxbWdEQnK8evw4_6Fx4IwCrZqGRFcphAAS9ZR-E673JMyg7mhNGK2vJHhZewmsqePJvwBuzwb5WLaKma6zcKQ3-EFuszDvs1wYRPNWGSpNixhFoAiyn174W1IXmBDHEnu20SHelcZn00McxhXUtTwAeANHn-BzXsu2n_0BW4LqkUgu-6Kq9B5XUn7YJmvrv6OLPb73itedi323Iy3CDcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFaIKqdBsVmdWmaZmyfTjgOOhFDmI6591Q73PcXjHi3iVlmhME7S2eQnszM88C7RVwvNAyEFPcr6c1ZhW1MURhyo1m1hnpbxOtExN4umfOVsldLdsB35EY6onk5s4DWgTw_hGpXAH-s9hMhTlCUytHGGFKrAfpaWqNOCUMAuALh5WrbEblUNq2M3pNDzuBfGjS-wUtOCZg9k6cFzXSxe8kgTIca1EVjzp85bMo9EzbGsN7DXVwhZJhNAiwiTW00v637yKjf2IbkQqFbcv1g6nQnEg0g9bolBojpekV3Q9HVvxdjLf-Zbm0RKuc8jsxTWXb5eci4GSIZFXcl5YQlcuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPwyXKNQ2Y8sqmWfzEvgjIgh9wNOBX2jfyQP2waYQsD-z4AZsaRaC0bYvlXeys7qsR-A-J2fMykYsupBOyqbT2Njrta_9SILDEdvdwakx7DxuLzg7cXdB5qZkTytzCAOGvLn2MER3-2stw0Ygan0DoM9rxi54OY5KgxtJVWxkjY7V5g2Vs3MErt00ANV2rPAEIbpA-qL1CVvI9Ol8KeDXT4z1yEJD8WGs17rCN-Ycd9n8sbPWWg_EnYaTBuljiiTwInQksjBEudVzFy5hAIEMo9frxVuSWGjPOVzshkA8tKBafkFvgMWbdKJwIZmPA4RqrrTLA51e7-5AFNWc5jRJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFXoLlqWBjX-4YtV8chQVui7OhOjyhHF-cl1HpxKWKzk3e0uNcheeCVMtQup5wul4q2hEWPXDC47WGTQA4gd1_YVNGrLcerxP7yj8GYGpYrUUMTIx-1hgUgfYIysaaGX1VKTXV5n-xW374OIY0641y4AgYzI0zbMw-qFSonHQZwA-eWV2OTCXDhmLWl8yc-BZcjGt-c_XHAZa4NHdcO2WK_0eOcG8be66KcXCzi7GFyetgmsa3DzgzRNkGSlWXNGw5OCgcxADOjWqieEQE3YFN5zEjoLGMWdNZphzcJEIHV33Fi893TOCQw3Wh_FRd0MrGBBOwRbBVu2OcIT5j22-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcenNanNKGjHm5JNrH6tJlBnPotGuUySfyFvED-WFiVugfOdUCxOu7J6DjeAU1m8i0gGzE-AROJlwn7lpdxMg2l8iDZdqQ2IxjPX6B0zc0uT1A7c6Bjyg1tBf7Bp4k0WwptA34FjjHXVBvDdB9KIF8PhFIUhdFHwAV_p2VLf9H_LVJeB1pWtxN6Ovp88f_Q3oUL7wO8UUcQJ5Kn3tRz0bNvIlZNQf24W2OiAMZjB_Gl8HCBdHNyobLzJ_6FUA_YhC1K3kO9EDQIHqcgY-zzPDtkzL2QbQiBv1Zu1imM_DLpOVnB1CUpsAXqKoKgu-aOQ6lw5ipjvBxAoij9uzPuPVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJYJM0ps2bS65YmBmPgOYjOjTxcvH0N1w_nH8Imk_7AFI0knt7rpIrOanLyDLP7RTtcg1N-HB7Ebf33UuWerGDgKxVrsc-VeyaIumIAXAhPYroNviHSBfVwW5D1cgeqU0tdN7LxEl7lH7JznXzhVL023e_5yMY1EKPLnMXuksk5XOHExc5zMVBRcZ8uQFgKOwCKpqn_JD0LBu_sqCFwywEVmAzcpuCT8KxG9mrbk-lNEaSHxyGF6pGQlQ4VSuoF_JpcJeQ2wcV-5pUjIuxP64r85YYLpEiOxDKQyVUSBrD2xQ8Jv1e80W7dg1aBrm546yFtnLDBc14qTkFxupsFNJA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=q_zP1zjScd_mLzJWM1GdvpLywI6WgX4ul_v7CU5-6XLTaFudgfLbNzKKCxhdzqGVc19KFcVWm2FLcggOHhi_DD_uCHx1KuV76_zgC9SW6HC-bQlcCE_Azb2Ek3eRIqJuNf5Rn0NcD83MvSRDO9MTf78-yfiqAoQSTUt5rZMo6NnBbtDYSLULDV01yEejWNllqt3hpfgGlUnseE7bUss9Pp1xFCxKure2twueoWvXsbe6215nlrRWSGZqRkTwsBZzePjgn_kZuwGl6X6d1mRfCrzWB06Mc-EO4oeSVNWEsLI_Jtwkexi7DYZiqXACsKcRgX7D7eEhcVsZJ5VYAPLdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=q_zP1zjScd_mLzJWM1GdvpLywI6WgX4ul_v7CU5-6XLTaFudgfLbNzKKCxhdzqGVc19KFcVWm2FLcggOHhi_DD_uCHx1KuV76_zgC9SW6HC-bQlcCE_Azb2Ek3eRIqJuNf5Rn0NcD83MvSRDO9MTf78-yfiqAoQSTUt5rZMo6NnBbtDYSLULDV01yEejWNllqt3hpfgGlUnseE7bUss9Pp1xFCxKure2twueoWvXsbe6215nlrRWSGZqRkTwsBZzePjgn_kZuwGl6X6d1mRfCrzWB06Mc-EO4oeSVNWEsLI_Jtwkexi7DYZiqXACsKcRgX7D7eEhcVsZJ5VYAPLdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnoL8WCJ5GBAvbdF-68gmOcj7gwLzE-mCfdWf-p9lkY7XXRlExU4YITa5Hj7yltRMupEP6nS7R5ncn3wrsDVhzYH_2bwuWKj37n1dafB0A3tvxYIQgGw-pM-AhtFHEPzUZ89nMY8w54nNaeJz5wdzkgckvaydG2WNdocNUWXnlnYavZBkuilMFUvASpmmImV5eaIWizCOtBTLrERiKUisNKLWE8rJRW8nqBo_-iZfYVgP41SlVpTvyqC53STr_CWfUbYFchIfgtukAwEO7zCFzCHG5G6wcBONdv8djdGVxavTNhbEPAuCKt7b0dRPfPoctj_BZVfFNKWWieKTm07WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhYpYaxk4Y7KMfyFhD7DUgNqV4ELQ9aFYNy547upxOn5wSiwYsSo2T8uVCWSU08a8cyVRkmzkuDwX2LBNnZ-JsA1yIJCGjS1XBfstErG3LDXQemgxAM304yk3SHIy_SOIBCDg_PVL1g9iw6CNrJCMQeSHli_uCS2wg2fanuCXyry5aVM2-P7loqQdGU7vFlI0MHI9H0rT4791VK3Si0ygqNWesHi34yU98HLHqgwZNEry1LPu5juVv2CptGNkeZJTiUFkkWELiBYSczDiyGEdGM_66Ed9z5f4xWq0eUlfMYypeD2MLIwmdjex9sYbJWtQy2q5cQsKMGliOwcWKKCKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kld4LhKNw9Bpksj72OG2rrTXgIGS_cuLPQ0ovk2r0-KuelZM4Hb0CR7-NIrqtQjM5lE7VMMM8SABm_3o5eubI9HTA4HABK6-T1BFOcjo0qTn6CEKcof_vQLihasrDXZsvPwoFmikPmeYPQrkTKiCk34IS7EwSl0p28HIzEhhzXm8gENRM2UfdO7wQmWFrnxWO9a8JCsFuDAo7_dzmz7nIvZEOeLPqUVTk6lTDTzr5NKAYbkxeYMNkcfIcp04K73ZuHAg5UYur4cqJvj40jAXBpkMR8PcpR3fOoiDSSxO63RKJRZ16cGkhYJmrPJx0HHz-OQTAPhFG7cvSBHm0MUv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwrTvGzMKp5BanJZk0N16IPvftuYoIWSGiDDbCXq6QP1CT7lrWrLhGKJfkHJinKF3ei8AELTO3YBOPrMuRrwOLsfntPxDGZ9DRrlXV5jg4wAXmRWsAWyXw0-tnsHd9TL1wA5R_D4Jzik_uJJ_H36dEe-eF5Q6kBuZ_ykZlFPlXKyncn_ufUZ5l8L_WfIVTPLEIdKGQAkz279jjpk3Z4HY69RMKtjaidtdJCfgDOueSH2bm7pcgtS4ojj3zpbQits_MtuxIURiL0BympZW11nkOJANtPvzw7P76bSxEyooYj-2W4nhd6Of0q_XPdz7wu7NEi5SIHpr0OWoeCvctZmKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUREO3KgEBNQdGtvxI-IRaVkDEcY8HyKzkSH8L8cDuP68aDWvthhgjpSd4Hfn_qWH8aPFPzVenuIo1S8iXHcx4ZIHWst5OXkX3ZAIbY_Jv7kCQcfPJEBhrQ8vep40hshyINOOX33BjAeXXLnEJCH_JgKOrfEa2CKLV_ZmPlMl3Bd6OaNWmB0ByMq8Y7UNXvOM_Udi7A3vKn-bDkK9cRohzDjeKPjkZGJRBpxCeWmy7IeqnDxyql6P2Ef_LgcZEae6G6EIVyzMt1TMnWCJ_TaeW5-ky-1cErvB1PsECdIDebB-D2UatH5g4B4SCHxTQ0fJidzIM5XY0ItVhGtoukLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU3BuhB93-ug67C02Cg3g4cO3tDOovuJFpTarjJyI-29xYwa-IdaLGAPkpGha9KvyHm2SViAnqdRQuPdl3bbURoraLxwOJMqLGIVGqf638AF1Aq-vE6PwvRoIbDDkreTE4DkL2xfZcasYd2-zMQktFRk_h5Frod5Jo8BmREicHKm2dBtPgBxTyfEQStZpkQWJ8SC4JbBiq_3zy8U-NTRNlUdPvsLqYyC7Cr3Z8N8bdwnj2Tafbd5Kn1z6QFf8X4dDKAHoog-vFq7FU9NdCZMfwLsqRgcklTqnyYSLpE-46d-SZRw-FwQ_t3BXvLvX4GGYaLT-h1Ze1CF1IJ9Sye4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHHeXGjavtMtIdMKUKTpElLiytia6bYfD9Zj8wKLSN8ea8lsSj7PiancOr0jfoRvgp1oE2mPsoYm1oz-ONLbIh1N73a843YrAEsr9pi9YWY8wqkAZxi0y0TPVpsmbC65QBIcWmwXkK0Xb0_bdkkxrnJnoHXAsxpCrByXc5M-B0zGQ0NCWTX_c8PEzYx4Zo6XPd82q0XDzOpzOXfICwQkdc3hddF80ZTZaLjJglyPoAI1T26DJ54PcQKqGrybLPakeUvKdECkgwlY_8p4dAW--BAsehITNb3CCpIeQ01miSSMCLVHaVLukKV3rznmODGUabJVarZdDCECBdHOPFhZjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=P1bhRKMjP7eRrKRnIE6gryiiVDkQ-u-s31rP1aZvOvs-OowHEZtowy_rQruwzG-tvkQSfKwdWgtHvRuvVaVGbxUEdelqymvhQsNuBxL9uU-jFE9i-vIu01WFVL-FHqUHb82JKC7y6fISVraMv0PA5sEyrt7yXUktnSmpOgWF4cmdrnNijeBBpMirKu3XKktvXfYNzyrWTPv5cnykqrcg90a65-3iL5_zqyPdjN50wr0qV4tZ5YrHO1C7CH-WY6iIPJsSARQPhTPU4rHToibmSAagqNxPIXbd2U_E2c2ble0Ba2_3ae8_5KdoznZ-j_nbHK1a3y9ybAAG1Ky2daYxk03LfGcEjaI5vASLQXYdltIge8YhlsAnaFfTV330jNyFieajnlYngoNdnKvK6lG8aVPW5ARwpPRH5t2LbqJRxCIDECZvtjiw2zyCJSK-CiQ57eWhfSMui1vkNkAvgUEP-n4OBavnIXnR1csVJDB_hbySgv_2GkWWhpGY8bQx2trwCp1xgK9cmQMQii0L7iUf3cd5d9-JSGlgnecyN89QuK_Ru1aPqKa0vOfOPJx5slcuM0EsPCZ_BYf4o42f8UONtmdm4whmqi4Ihx6wDlVy7Lhruu8KMQ-mKIE-oyE22H3-WSahZK7o9LF8dpAy1B3uQ8MjqmboPIYTngf3-v4UbB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=P1bhRKMjP7eRrKRnIE6gryiiVDkQ-u-s31rP1aZvOvs-OowHEZtowy_rQruwzG-tvkQSfKwdWgtHvRuvVaVGbxUEdelqymvhQsNuBxL9uU-jFE9i-vIu01WFVL-FHqUHb82JKC7y6fISVraMv0PA5sEyrt7yXUktnSmpOgWF4cmdrnNijeBBpMirKu3XKktvXfYNzyrWTPv5cnykqrcg90a65-3iL5_zqyPdjN50wr0qV4tZ5YrHO1C7CH-WY6iIPJsSARQPhTPU4rHToibmSAagqNxPIXbd2U_E2c2ble0Ba2_3ae8_5KdoznZ-j_nbHK1a3y9ybAAG1Ky2daYxk03LfGcEjaI5vASLQXYdltIge8YhlsAnaFfTV330jNyFieajnlYngoNdnKvK6lG8aVPW5ARwpPRH5t2LbqJRxCIDECZvtjiw2zyCJSK-CiQ57eWhfSMui1vkNkAvgUEP-n4OBavnIXnR1csVJDB_hbySgv_2GkWWhpGY8bQx2trwCp1xgK9cmQMQii0L7iUf3cd5d9-JSGlgnecyN89QuK_Ru1aPqKa0vOfOPJx5slcuM0EsPCZ_BYf4o42f8UONtmdm4whmqi4Ihx6wDlVy7Lhruu8KMQ-mKIE-oyE22H3-WSahZK7o9LF8dpAy1B3uQ8MjqmboPIYTngf3-v4UbB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPjY9y4q3BioPi1XXQ8vg9nKBpL4aURP5J_f10SgvzYw6bFXDGJ9BsPxi-4wHrFBaWq7Q6cKVNjGkILTOXLpZOs7jBRy0iIwycbzZolEB4wuHL3Uupe51bvDFqKMObkKHqC5K8SOfbWkT3M77uZPlYoUctwXstpGWT7SICC9uShgmiM3QNWSShbJz1eOMRoBCbVGmdzNh-B0300bUgDw4S1yuXQ_gvwHumJRdDQHQk8DmprRa00QQcRWH5KjcJa_0mvS-Rax9BMItPQWOLNnNfIUbE_NN0ZEL3y4ZxOSaOug9tP4GRTzj3CSLBzDwZiQ0j-rXswIGEdr5Nd9OPguDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzEfSXiz_IFys-fCCQ4n5mv4rbJFaZxydlE32Ex-fxsqVJfFCKtkW8fcwQmy_wVJaYXuliP857tXJQlrDMUBFx4GIQMcoozRKbWd0Iv7Qrip4XKP8biCmQMh4aH4EdKT-pQZSNi0bx7uk4P7vM4KKkQooOWO-uCfVzk1tzb4p_s4HXvRDCfCKS_BM_0b9X_rJu41O4Qj3RERzIOnvok4kd8SEjhsVcolUoZBdZFzJgy-TXSqkcJ9w53es4TIQaC-_3NnOJHQRAnuO2-LuqvWtV1iQ0ZK8EEeyfzItZdjRMbc3LTNk_IMBG4gtykHAZZJK_oNW8qPnTGH9KJNFndjeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npt60f5oRsexEv36NTR71WGV728LDrecJ1jd1d97nbXnLrxbT1bt1kcyndXt2ufvPM-aNKX3COcQEyqNBMtK3_2PXTP4dfES50tBbyQagStLyWvSNDB0C64MZ4Pu8faJSxZBl4qfNNSA7Qq6fy9wzYKJSbjKc6LdMuDJOpZk3-CpRtMqAf9i6lOMSYpRC0HWoqPJmFjj4abytb3itjlEHqFZC7F4w_MZAQnWTGqwKysUOxxlfS8jCp9o1KTFaOrq8TwI5KjLtTJaSOUGo4YdGDdAabkXbhBvifbrmy9TWZwu2tR1G5dHl3aSyJKh7cKEHIkJSFteRM4P4Vaii6DGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcnEuJj_iUbFRvfv_3neFLcGOAPPq7O3LbwGShn1v2YJD_Gm16Hv_ejs6xyM-wD4dDdSwZYboHEF81-2rEyj_X65e5Mv1C6QwUeB0ab4laGpwPOiITIVk460yXFTSYd-mJdmvaxsdc7hW9WFDEDdSdceQS_R2BTxg56eFfrPzYU95HTDimShsd97hV03kwF3JTAsvzJrwfn_7nBLESpMsC0q1WG1dzmNNNxsb1iXsFN-QwTCky97YztZ9Ez_XJCDuUJEwiObKERJurTfMDeEV_O91Msg2xpTQsblfIQA921ZxcVlr9P-9wNBBYz5T46fd8kf43i57Q7rQT9Lj2Sscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRc82lHTkYVtML2AACrJmBdoF4WHHVGYLiTcg1PKOtarBYDn-pqkaOvKTOfE6gPLhdMtFHhV3Y6ueekz5uEfracDPXKjpHid4ct9TO1PfJpWbRB4_1mVszlJa8IK6UFM5lkhmb1T2DtfE9aUY3wtbEbzMRvwFvcGcox38brGGEU_yyfxROWjyUYpayibXr6Fpc_SPysT1qDRLomlbDXtYRsnIK_gTQQ8M5MDiYFW6Ek94fityic5HN6ZHDdzssPS5wjf6VtKtpy2YmCgNbSruXTK1mgxkogIObs5XKQHxpSZ2pkvBntL3nFeFzCKQXQ5mJoE7a-2GsHUJy33YRcrhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZrZg_1JxtR28Vl3TRrP4Vg86tSLMiNyJDjG9w5Nniou3kMDsO7VVKXVkqOPSmP5_2H0CCteCtNI_icy0J1OBOlEeZxPUz2UK9psXEeUDK0uaP7jAbQoeyrNOSoCUFqd52tm3A9r8nP7qqxVWZz3yrrjkgQrpMTwcztlOcNtd5aAWm_yVpnsFtPM1whpNfcyGpKG1K6FPEMP3VtRMMJ9JsSL4JGsw_ss6TRflBTGmOOfqTD8JM7Mre_oRsBUT3S6UKnRrGYjqMFtvGc-SSczwU3etDoiqCaanvsQ09CmbHwfb9drE3lhYEHlFvrHYQF2MEOHm1oPgPGx10Ved2ON4qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZrZg_1JxtR28Vl3TRrP4Vg86tSLMiNyJDjG9w5Nniou3kMDsO7VVKXVkqOPSmP5_2H0CCteCtNI_icy0J1OBOlEeZxPUz2UK9psXEeUDK0uaP7jAbQoeyrNOSoCUFqd52tm3A9r8nP7qqxVWZz3yrrjkgQrpMTwcztlOcNtd5aAWm_yVpnsFtPM1whpNfcyGpKG1K6FPEMP3VtRMMJ9JsSL4JGsw_ss6TRflBTGmOOfqTD8JM7Mre_oRsBUT3S6UKnRrGYjqMFtvGc-SSczwU3etDoiqCaanvsQ09CmbHwfb9drE3lhYEHlFvrHYQF2MEOHm1oPgPGx10Ved2ON4qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTfyTrS6xgxdbAGFAXg6cMiVNMJkKw7CeSLXGwaHpZMf9MkfNBFKrIisA0PsL09tp4QPc7kSx0RoPJtwNqbY2JrU0agTJKa6plHjGPgbz997MK3hanHyrMM52eDDKyPV5Wppk4KkYxiPMJb81a5zUDJThLNJmIXH7JHOXQtwVPu4qcGsDrjvm1mCxDy8I1uTKkHHJKFMEZ6KuPtJwH_4gMOoYX58ltS38lQEyGKW2sNq-7nW01EA88ed6tMmp43Bqu2XOVVB18g83ell9cBvufwsELWPH-B56kUXlzUiaa3QpnxB2U1rfm_R8Scl5qvkZerGHyQsG4BCY3i_EVH0mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9QeP3-Nk3S3Yu-rrFOKfQ3kAQU7REsYpxM6y87_UVJefVODv7CPzXVArKGnYcxyFIXkc310n7iK_oE8eNLyMy3w2lBeLsM2Yc6iLV8eNqdQYx5uAhbpRTeyvKGxKd0vouSMMcojIkzGfTebU5x3CPi8UtxqISotP-k-7mYuPkSXnG252ZceUWQajKPnVKWWri6bdpwslVNnsjVn0ECjiR8YQ818Djx40ofq9iu4cZSFRYTVoCTf9vJ0D4zLCRGJyqAV8PGHAS3NDTBB2lE1LM8AEIh2tclW5p8ng6Ypl4gULzcX_FGN_ZpumgESjD6ewyiaF4smIeQmPsWebCqmow.jpg" alt="photo" loading="lazy"/></div>
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
