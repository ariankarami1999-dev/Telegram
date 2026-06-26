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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 02:11:51</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltn4OWJZNVlDCMP03buI4RK01sSOper2KZY4zxLBCIP-PpxVGlKMqDsoszc10XYSesqjqzY_H-dy7-NNiWja6XVQJ8o9V4NoOWQON_f0QXMlLhlcVvpWMTeGDueSyxBs5nO45jIuDEjRWjjOtCt45oEdQPrO8mkj1vG-ioStbVRLYxL9FRkGnvt04s1FFJ6z2n1TQ9xwElMjUZ-5XOmuLzA7iVA6RSpI5R7XAErU6YODzVw_nmuKDrIy00pHrc-fXtKzSvNs657xAWry7f7RpBnodbnbGP9XYBe47jx0SqsEk9TE-FwpJFln54OvK_gS-R9XtgZ50TClNTZ4WwIACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 240 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 476 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7hEt3pcgBT46NR54xHHL-w_71PySVm0VI-keHx4JQWUsztXIB958C4Ls-WCj3XK-eOSRSIuFjTzvg6N_mfjR8DQWoy6HteYVINXYVZ9IHIMCCsqLUFayokjnikA3wZ4SEtTMzR7wdfMvcaGPfGI7YfElyvK6eF6oqhmwlAm7XFXjzIfG1uz3Wk0t_zARohBAl7G8W1vA2jkX9LhgOIXKDqTX_--iotUP-YlEr1ia1kienTdSe-IpXhUUzJaMOhS9qbbBT3NNCToHgGhh-D5kf4LLSuo-NLkoXV6AI7SB_2YGkWt8aowAMq4_lvcUn0tPx29q3wXh98VZRbje6C6eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwpNFIEScj37L1fo6YJavvRJLFJCKTv8-zXrKAus6QbYaZ1wJdRrGDKvDr5lbg_CSs3lEXGybUIWhzEYPfD0iSHDy8JuTs_1u5CA5rIwcbF71vaxmV0R3QGbvpGBLSy3tWk9AO2sV9p8rxGEeey6kg9O6LhIcYt-FkR5OCsBVY5gsLE0wS2vBojQ2g0cXOJkQFbynx0XE80TyqUVYEDgEzRGa8Uk_Inos83tQNs7Ld6Ujsc1rvjv1P58P9EvA1nBt0dhsS9URrU5kC83xBptYEciKuAfbVJ0vgd-xLpigTDQyHqX68tMqf2PSTgF7wsmX791sXEDgHERUBXBdzOO8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ty7YGHKMb1IebDDOECylnKwsfARSiXcYNSb6TVrC_Iq30FteIF8thXI8RiYyzR3VsKbxfLygDNHdDwV6YCXIKQEixVEEg1IqeddBExPDSnFeoaLz-eG0G1gDZQXrhy2jeQBsDpBW03hiOexn3ePrHheLIgSSVT8tqRYUb_OhpqCplEQvLRTSIeZKYRHuUJ4YgHkR6kCVU-kLlDtCK91dbAS9IKjuxMxdUoPXgekdMMaz45upDRhx0F3gPM1r8byi6sCcuSy24BafNB7Ssxykz61wgSQLh9XkNDsVYrxPK_zuDanSVRB1N83K3cUnsWXgdQalHm4zbTqIdSSOIiIYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otaoFM3NN9hXfiAUjBkU-FLXWMlPMNao4GkkG3JBXs53rvoDChKBjeXtq2pQU7_dnv9fVnv7UNJrBd32lBU7TFule3HNf5VrvzE0GN6IXWXuwj-yDptSlDuHA9hKyY2bgh2myh2RQk2RK7OhaNYHIMxrcWkf-5oyL49zYBZI4r7Y0q0KEBtossCFIN8GEJWBaNMCnC2LrSFzo5xiR5fbmhBjEPBQp_dDpXbWbQbpySr0B4s_EwYeln7cqJZ17awDXGdpFBpmUMDKMLLPL5PyAxooEJYG4-t0pWNQND3BWmV9QyFlcEmhXU_DxYRu5OwRk3LSKee_8Tz04gNZdsRtIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx96JrQDDvpD-TXgkDvQQSa3aPs6-wLYy65Wu8zHfDTMgs6_fnhKuvb8QdoXfyF2O9VNyuIgJ2vi_Vs5Y8pJt1WgM2qHvPLjB2PIPYZjLno0YD3p7ETboYonEsyAArPtOQYQSFxkKJcxPNTS5NFk7bOc7V9fpcCL9NVDv_-m5ma8aJHrdDmSTwZkPcHoFS1MwKq4RuzJqtTM-cUE9L1Lv8gUH2kvJ3I1sr9vGuEE3G1KvxbA5MYpTH-9EHHc1BQoTz_LPB2ulsZqBJxfOJQvxea-clRF5oFQxnBmVID7NbUxH84_9znUHVraotnJ6v_6A-jfPkpyPK-ly3s1v8nn7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiKwlH2Rj6WIF2sHDfc40J8tGDamcxwG_DjY8nbgVHqYWjny0osRBcwP3VtKky9mzUY-V-ZipsN_99DsHEmDjObAPZNEkYBA-OsYp6rijlqFm2jfNqwVJNnidtFN4bb9bgvZ3jGGAuBi5RkwTA_KebmXwqXKqaa2UA9nQe-8mWgYQA23N00_48yStXop6mtH833WJyyAZKaDJHokPGyIHb8i9L1KjAeFIRcjPhKTs11f7yOQdoz8nAaBPG7ZzB4Yd4y9LGYRqeURLNkkXqulhxWnlnJYvgtK8aeQmU1oTI9Y3mQryEapGTnoppMZ2hqOGmihyj1yp7txO9HCwu9AiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqB48wkaPbkN6rp8NQUCyO5qmwRYhcFmblBZKdNQ0iF7bVjLEk-6iSh_x7CN8qBWULIWT-86gje7JmiqkDGN1yox4sMO1D3FQ_U5HpKY2A6A-l5_x79HMmswZkMk5gWTub6F3J-Ul9aTf1pUFcJLWhjfsCHIB35M2X_FcEJOdY5U6D_NIrn_cMYpSnP-CT_qZYrsTKdv7Zc0okJP5KopYt5ezd7p6OBYKcNQeOy5SNRLbrmflEVQ1kC8T3lfXhNrSAlb1drtfT9Dh_yyruft5a1t397Xpl3TQUytZBhjWch_SB8b5Ip4jYtnYceVitrJsIOEwzfi7qB2qKYIwHi1ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZt3V_ajHOWe4XwlsNnoSsX_UEvxP1Q_ZBy2k63Mi33DsrhX5Bf-U2OdVqhcRB-PU-lbJRz8KPedCz3hMgiqfWWxBxhkSeAR7bZ8Z8Us6JzZAG7WrWKuYSE72Gy2UvwmwoMSsdGjhXnL-XgtlL2Qt5Uud9CHXbdpxGjv_dIsfh6T8t1udvruHJ366b3rBXfvFS7Qa3kfyMddml-ZN3pHi_Yo7qxpWs7WATwpxE3b-1EqCjFL07TFTxrfZPYEVb8miT-WkVYWzhTVNB4B-8yG6SFcuosxXIOa8Zxsh9Tbf6DbKNN9JxsdI--2MARQ10KKTU2je_dg9FqsSbkIVuBBYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VE_Nf_x0AVl05daTXLcKS1IvZeLV1YJj7TYgE11eXx0rJ7wCwbDJESbHR1VS-ThBHUdVmPN36fLmzjkaWnRUFJ0-Ls7fIhPg18iOsCl6W73cRcapvX5hpbpOoi2Yz7EAWOgMe1NP6uTlF85druGih3dB43g_G2Kt1b7egjn3oqfzfFrB_n9swQUumu40fZtqCRYX9VoxPC0AaSmxQaHFYyOfhjV3ZWhWReXPtr70NUNwrG3bYp4U6U_gZovU8HAGeEAPA0XVGD7YV5tWbbHa8heMGcS9tU6c6XWrfMuCHJNhiPBYisVmU0H-eRQbUrAQJ3Nt9S-HEwdP3d40sdrGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nck8YnJ8L6iMxkZUyND-2pbEZxlIXYwaVQHApdUEJ9s40l_usW5KmvysJVFW_TPF31JO5iNg4OeqsnlQwVwAFD9NP2tcOX-m0TMyt2d70rUAyjId4hbdZz-Vtn6e050MjqWFfQRjMLzRqvnlSEdaCGm4IgHgJKYZPruIEAyZuymCzV2K3p4vs1H6Z2yMd4zEw_dm8hcKpN1a5UeaGk2is5ExNc9pyuMO51cu-2o_pqCqyQMJQKnVgqTt_HAgky-D79xnDyrvSZNPFFDcDLEHnrm8lIzrTeaOwGPYRwV0aQ_FGMeCTzlJ6R5cJ7iObotdS16VVXTs752cSimj3Q_UQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdxEQ-UA4uZkzQDKZdRqs0gCwdsX7GGJ9Cm9L_5qajF9SanAsHrMFKJsiUEmah53yJWGWaoXMwcGDKROLAIu926QRvRDBOB22h-3dRZmPP5HUvHC0xfU3q2kKAPfVDJ_orMxAS-ca9gQcNObkCUxe5pHFaK4xmjJHPGv8YknBzPKo1-SIhjDr_yyXN474txAwVjasNOD_T2IwIvvJtaFVYms-nnAowiuXBbdxjm3ZdlfF-99IqmsBiNTZ1U_iu1eXDsp6I1LoM3fuyslkA8qkRR5c1gJERNIWxzOH0gXv2OvHjgCJ-Yd-9yfmdHKWJlonAyxAG6UZSZ1SdAeXyGRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVmvCxR1s6Tb8toXjStxUAOBHyLa-G-oUnwqei3X-aH7PzPMKWCvYijqTj2e1JNccvwCEENH7z6lwxDFSJh5TvmfsHK63cOMAZiy1OTZ58hIIJyJVUu7VbfS4y_mTPVHUXnneQ-3SwTdqlyHR4DftjWXDn3BUcJdHhsay2-j-1RB5fD2yKl3ML9H8HP3ia2lm48lTET9EG6chT8gJ8ZA-EVsWCu-UnbHT0a0_ZxLdJ7DFR1__ZuKMwXbveV7xgtUeTbekLN2K-PiqYeSIASTqLt6ivu4qiKKagO-5HcV5Ap5BjmpZfbhMR_9S3vf3FMWUKyKdz886KJmJ4IgPtD9Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP8BFC1PEtm7RbLRkJ_idNsDOYscPb7Yzvhq4-SqR-FLQLJY4vwr3tz-5SZ7fvfhbghrOmYCXVyJn9GyMczDK2ryTfF0dvvpdYnk4DxDYvvo1Z8zb7visipa-k6YlZkx1UQhEFaaOSq9rL5UrYx4_dcKzrm17NxJWsxiUerCnyW0MIjDj6YckJgG060mgWJbTUu_fGXxCrbNghWCJITGdoLDL_vdM_YyBTEGCDInGiVuWUnTGZTY-y1IAGZQ1Nl1qc7yXZoBPV12mPMrrtdIa6WTZ0h2DnYznhVUs1ciW0yM4xTjsQcrDssRVGDGt3HR2xuMLYYwHuRu4roo50JbNw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=NCrFmS4s7vR0qDn_gqmUK_0HuUHjCiBSbrYR4Cg0HQbCGJ-iCrlNrFqfRPRI-tuJ4n_ZXNSnlon-006Lrj6OWURlXhflDhsXBp6dvKVYbC9JZ7CvIRtMe5EVo4JvAbCPlmu2hDDrnqfiTkiOfHNhzMGXQ6LUWid8Twk3ljOza762A2PI8oDW4_wl2L461Q4klvTJMxhC81LicQMg-9LVJ_KfWdxAWtfK2mJtV2uSWIUuKyc3TcmW6C3W28l6LMqF8GvfgUJi1WmMdHaA67iPcwoEayNu47FdbRIZr3UZYEEBEBoozxHSMjX2FozKMQbSW3FqDnTqhpmx33mEt_Si3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=NCrFmS4s7vR0qDn_gqmUK_0HuUHjCiBSbrYR4Cg0HQbCGJ-iCrlNrFqfRPRI-tuJ4n_ZXNSnlon-006Lrj6OWURlXhflDhsXBp6dvKVYbC9JZ7CvIRtMe5EVo4JvAbCPlmu2hDDrnqfiTkiOfHNhzMGXQ6LUWid8Twk3ljOza762A2PI8oDW4_wl2L461Q4klvTJMxhC81LicQMg-9LVJ_KfWdxAWtfK2mJtV2uSWIUuKyc3TcmW6C3W28l6LMqF8GvfgUJi1WmMdHaA67iPcwoEayNu47FdbRIZr3UZYEEBEBoozxHSMjX2FozKMQbSW3FqDnTqhpmx33mEt_Si3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tccw2jTn73uXeVzyv5Vt3R7f-sPd8UtECZ0ou_J6xwsesvd7XfwcCt48fDxLepn4zUOyX20etn5azJ-bIpT_rb-B2bJ_L4O1U5M_qivDLZ19dOLLbmEAi3fLUjatvbEEjFSLTDMuT75JxHbPx0j1CLyx_gG8JWJFXQEuhZtczpFjwD561_oOp7zNP2RAXfnP4UJEg-LVQMbrHCc_oHUwmMQyB8G36ZHiItG0y4hpMRWrIml8pmabALuvPL2psdDZP_88M2LF10aoAfnKjbtJxXgRpH0SeYDgBMKhtQeepJbDvKQMKgiLeDoxZ43ulr_qssR0ng2vVz4QzQ-5XZ5PjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfEUo5bc7PxKu1Ma_ITN4fi7ZRvY2M160J8spGbtA44F3pChphK0Wlzt7RrGhLBKYoqWdgQVyGS9K58q9rBOXzoAUfLuNcJHDsNaFztEF0yLg5Wz1a8MyIVRn4Me0K5FX69DtusuYD-W9mSDGErktJgH7Xi4gekqYft9w4YVSO_HMZ8f5zPh0Edfsx3UcBgdb70vkx4WVtC_DkBhgjsYIWknfGUUmviP3QL2Vc7KXdjphwtyTrcc-CIRbXWlQZDyCq-nspHmB9vV4ft2LyvFkwpHN5I8pNLCiyZE1eKh25uqb3qqHpYgEVDgYhBSJTSpwm9HcJWHPsA931kyvXq3mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TL57-MyWJJQMYAlYHaC41cbpgaC4CPzA_VgHViv53HwwA6YpgZ2du5v4wGwvGnVCV6LV_AnZBmIUc9lL69qrBsHNJxdS7l2fUmV1GjNtYSdeWutDCqIjv6DtJeeLTejABYEjQo_Fv93BevRHv25FfbwZgpGSM4XQUIuh5XkYFhHUIQA-WtPLO7WDQVvMfQfYRoYqF-aFcmKSbxTbSo5LewPqxBDt1oFYCJT7w0PscWVn5ppc7J8BsmUNaC4bCd1ollAc7uSD_0_IFoiQlrurDZdaxo1LNDqyIbaTRc5NVcMGqf2kfMBOlLz67IxwgMQ6O_PZ1z-6Sxcntpjn1G0sFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi_js9qC72isrraOLmK-LqRzgsafj7v4PNcpwpcSBmZ0wITgqhcgEMQFk3aBFOcDbAfBkk4BB_w8IWVjwYcozPM4_pXr9l0mmoSlIdR2aF7olUhYJYhuFJMsJzvcej3XgzsoIv6zaqXbR5VxeJbJcwiexdkZK_I_P7wIJI6nooI4PGgFrqWdXOLHLiovM2WEdkLEifBkHPfpjHsIrPAdSddhVJNKRtYUEQzaBEqlMLk4o_SyMMG6IpoNlxeN2hlPFEq4imnKpj0JBJBvNeaZm2k4kMkSl6mGdQdKV-KigjnsPGB9ghkBjU-AKU1xufNar4T43fYZ5TkXD6fM17xewA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtS70nedEYYhOG5o-08aX_F1RXPSsnLX8BxgtlAz4FNl-VqOgSOlzf1xntDXVn4fOPe4lVraZ4hWwMEKrEKbDjM8FXvzJtd9oFDlzUazKgasSHCCHh4ACoxVD-9-e8_z8OEz0NNiQCcY32gAIyVoR-08iv3uC-EXZcX3D5j3BD0UrWYRR9D-stEHBj-p4SeCEzXPlRw4EDwaG0kjp-ufbzuBmpJ0t6-rYHckMqC6ixz68Ty1cIo-nniZgaoT158tVJ93nIvRdv62aimfb8TGd-To9oOqhMuA_3YlxecWk3Zi_T4FQjgFxU37gyxVKi4iy9Sp8vYIjSHNfVavhuIRBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRMvv7qMDnE6R9dz81l-m8u16q6nELhSVKfiNT0Yzf2IP2aQaGT4qck0l1TJoMvlPVMVJ8n6tzPOf0mjT8XuxYSSo1i10mUZLsMMqg0FbIT_0gQkyO14I8TEkc_ikq5OrvvEqVVfb89gXmZ0J8G2WXmuHzh8362_4xKCdXsZBAOOuvqmIWYV7oBtiJkhWz-q5v-OQJDg1qh759zZaYFMVdUMf3lZVY0l88rmT1qiQlLaDG-mUXUhnRpRoucyPE__RpFrj9Q7JCqejvWpiNKVUf-6MCw7mySqvkYxZhHu-0who6WD8yR8fWQuFYBufkmXiGr6tDQwYaKx8TMjXdT8Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9FF-3oU7txmk4v5EpTb9tOC-9UgIOiF4hZqHXkjR9zGqw_km8PgyN6rw-dRKIOP4ofeHVjaUGEaSO89qeMvvChr06KIBiPaZVnHfWBt_Mq-MgE-D7_0Sw1zTi6lXF2-1emVtJeru_d1NO7DL3JF2w9r6kaJMbDfeRlU7Jk7CXI16CVhlq0OhR1AvCfUMeNiJmsrn5eLgubi79j-bs2nWUZFi65MtxHfpNlpm10WaIxx2NBWKQkU-ZoGqstITV7_ifO2CSOTfQHxYbSHTY_921_VISVxyfS2VmKwhNXEE1wsSxSJVKoV7bqL6fp05tnEM8Q97IT-PbJPB5hkh5XnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k96EGVCYGTAKZS2Ju581fEqv8j2O5W_lC8VJcjeMJlmLOYCmdICAlP6XuneR5JI59Tuc5cLyOm1V9galoUUwgwNCa8fK0tzv9E6bgEC3qFHamohqU97EO-9ICz-6p1VC3Yf77VzLsfBq5XLJblvTZA9Ra8eznliw7ZIDTvgPbBV5WGmfwpAePVDuMGQ08uCEgxr3x_GQYb3PdFsgz-u7ISuR0d_UXWXhQ-vp-AOcGxUYRi84xRwW4yFNOv7udAt7t85WbLniDOycDvCkAFehr66zB16BZ4Zj4IdgnmeKE2y6wXuMSjg1UnPdwXcHvmsbdka9uyCWnY03PseckyBlIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADB94c_hAOXYtp5L01Fm9OJBoA0Z1-9XBowEIEEJXioeegXz9NTwbD7_SVBREumpv3X1xpCpsPed7aR0a0nN4fhs8f8zSmqWHkH66Y7_YiOs8nbx7kDG8OqQZ_lBS3-RRHIQW641ExWu6BtL1QNeQqq1it4Fr3-2sIextgHUur6IwKdDEyCAFkcRDsnV4Fj1Dw2-axpVzl7PT6fjH3H7uFaRfpbZuoIwHl89MZDgQaPMJKQ4CFf4FbH4bzSAnOTveEehPdVxbviMch6_CNjtqht6_5z0RLgkIXvgpmvwGl1AYk1szjZisLt3JOXA6VmGUZaKwzSouJa0eAazz5mYdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRXSAOdZj-Ikx_C3H89agZP_CgHmihSy8PLQF4N7b5O0F8gTULb0MJ5czNT8BirOcFbRxx0gtLGSsXRgX1L2yospKEsLs904ZQNaW5abowa_wRATkrjuG61jI6qEgkHa5mSaSelBvWLSrYLw0dG9CkgN2JUuEjJpJ2ggzqHT8g_FfwxJycudz-gpZdjnRcWX07iBN2YPGkjl0EHNdQWQBoN_eGrtU1M36xu2KLpwoUn-dWqBHcDX6wyy9d9xI8fDDT8F0gtCeJQ0rzpeJdTHZLDsFZc97i6MB3je0ahqiKraa6HYgHhP6QnS8_MlQZTqMW3BtE7Nq7eN_0Dc7O12WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J07_4faLf4wkO_XXFpovV25Wqw2MDzImH30XkmDlnoKuMvjQXIjB1vifwC4wrDtW7zANldEoGZGkGi4PFEzhOF24ZX2EzboKgoqLXqBMeWRffrS5ki5-NuJxCHenYLRG0Km8fsFJIAqzMjuaD9R7x0i2ep5jAKVz1IQYhPiDVX6OJGD8sTb6IynQPFKMuDpxv_ud0uT9ZONtCpu2kd29iyTZKIoKCiloK-mHYK47-xf5L49NqzDQM8-npvvcP1LBT1ZbQueF30YCf1R_3WSgfsQPzQDtkpzxK8riKlFXJ2f1-AHr3VrPt5mNRffl5YJ3eqwfjRznmSfCfGRJda6WRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPAvrSo0RCpSFFlWubAR29XYQB7YcNTUMMrUeDtawlg2w60-TT3qvRXEykSXx_NHXevWgGJvVj9eR7MyAxygM4qoyK6YoEqn1fiNaW9WxHluF8wE5BkcTnmljFRMJA-L9G1nppinBTVQ3Y9PL_9zN_XOET0_d4vfF-k4a8mUp64zqEfwSACM2q882AXFWN2zIog-f71Rz7NgKCj3unRjp2oQH2zz2AC-kGqFywCgej2OnzdAMdtRY-tBaxqqHorUT3x1B4cw_FeVD6tB5XtqnRhZ9ENV96n7E3EE0pSN3oOKp-bCJG7Rw8zEd4It8RK06BNQzGr04HWuYG9IEKoP_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaE8KhEiiTrvqiGDS-k5g3qmHQYnulZDKJZJzLDeMKgIyY8j8SkPpkx6DIeFlHiyJ_eWS4t8ACfLWeAb8Y41WeC_o7-LvX2h9abqh8tI2wThbQUDZM-P0s8i2joqZFxqvIKj6oRxg1ucDhBQH-M5wU4CcEUnynC_5bLXVNfN2vBEKoDlNtfE4mDcIrFxO_3ods1eoYt-tpN1iNDiM0ZX-hxAk-y0TMAzvZG5kO273rR4XDzdczNRD0CKRHPzOzHbw5H-Gdli1eeXAOUD6xPr_rPIQHfoqtFJS-vL0JkdzEpDXswI2OrQR6xd6bY2l1uFkQsFEKiK_gRLzfh1edZP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0TQ7xmS-iS-ttgS8x-K8RpQvsdTQY4J8gU8cJCpNCduXIHg3HX76aLw9ESOaRjJyiPGDsSyPYYz-1YRwXNcJkn9wTV-uB7xeNdbQ9kZsKDj86iH-8dIf--AWk5T2VywqtTJ_rELLqu-bjsnaKLiXfvTC4M5eNs6ZRo_n69uJNSMdL1HYRtTuOrc2ouQTZ0p7YjdAa8BSLRBgv3u1nH1VEZTatJpV5BgWkgmm_7c6YFcoTScIYPUdorwZX07NOylmKtDjeIFMtoyNC_6_v4ZB3V_7Am_yVAathcvcB0HOydpt_l779U3-buv2zWI3rJZePvMrXHJS3yM8xoZDB1nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8WDasgKiQSAoa4fyEu5xLVI82639HL_1uiWRHB4uWJH9p-hTWtJ3umz-nsvwRFmMFiG0oVhIM1qPWTEvdctG_xqkpddkE7BV7Op4yoxm6nFsTbmdAlA97TnmFuNLA5vTL4mp1crEO8CAV1L4ORXSapxDrUIBjszEACwwDCEcUPfuz1vw_ggPrcLAWsjupmBxTGMzPV6ErP6s7CzlJQydRDJBURxgrmGr6TjsDfY4zRqRpRsj0Z4S0korEaY2T6wv2quCvqUNuf6GjENmEtif85nzcxJSvnDajqE8Uv4Z75gGHae8cpZ1heu_z982klL0EF4pZEPPKmHO7VRC3GlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSfVr3_ROZ8TULCTSL5imgQYu53NAKGEoE5j1WLpNTQDceN0L9DnLWhWpYx1gVEAiqo6mVlBycz2TdVQL_EfWArEH-Jp5wmnyLK9mVUwpL3Vqi5_qf9WsxQHtmg2FwiWkHAEdAs96CLjvS2SpfhzPd_efmvtBXN_pq7pfYYHH3DF9cfxfMKD7JptLUqsXVZeqtr4cbJOSCK-cNF4CBDlgCUYV2jUGWJJ_kxtcypbMCZ6HnoH9zr_sHoSHNzFDhbAjLFCDZUg2sXC6UaDtcfJ0izBKsDdFDc01kaOO8ubZNSk99fSi3w4L7Lu0yM_CyVLnpyo_qdasmBy_X705anniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvGHprPJytrLSVIjOjYnrqWs_1Jg2txr_ELm6kNHtCQJ2DSX7pfesS10g2jvGmLITDQ2PjNqeHZu1vq-G-dab1OAtxdvnKYShazn9zXUfuBD3bcYEuS241uI8sMNL_zMAs2yYoLYHGNPV3Xq8hg4PzIDlq6jNLGRfhn2hCJgxUixh_cMFq3ZoCcnG-8gXFN4kfkhCIQ3zjjSvTif2RU4CzfUsvWhnvcNtUAxGwKy4T3_LCzK9RMcl88koimDrXOMu96Om1XcaQ6DIDobCONNYXVfb4jeFJazWnQsPLFa5DQ1DibHwjq9R4_mb1myjDtDAoHHZAWi6fYH2BgOOyvZcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSeFxB1pZwsLRovijqmSqlOezWgIcT3LYc2MWZYy8rNRVEdldSO_iEwMq0nODgRKF8AEa-vFXgL5aC1gPWkhipnxjFA1quzy0SBi1pnLDz4b4wxVdZw9FH7ROo7IN-pP9CoEkgtAvhTwHSEXMADX8O11wz5c6_WLnadCvchleR_v9JolCkQZV1zaX15tj-MgJHMFrjHBR3s4k7WE28TWRnlA50nOOTdl8hv4uTa4ByGeU_JGVuzrgMal57FuHhtqorbdA8qeNkOK7aIYGkJ5fkNKjz73ZFhSrEaGqLz1hAAC53zFr72PoruuM9cVZzvEBkZpem1f1kntH5fOFkWcbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhxvGZwisL7585_JB79TCtvR0wC86tVNKG7u-8eh-hNQzIP4wNS4Nzc5-Tgc25cGBiqoLCaKIi9ZKljAIQD5uFluGYPOtOnCOODguMXYougOWoVcoUBik74PtWsQc_8IHkJjSxS9caKX_O-MY-iYFfG2dgw9oAIf5hNmA93mG0Ce_s0Fs08YQtk4z3R9aFiWF-HkuukChwW_ae7RWFfUntaUh6ASUBzU01hdUacOmXvSibnZ2zHl12PHoVZOQrl7OktLbW3VeBBxv1LYuB2q3yrf-e8ypA36vwf3kOxl1rpaHEEEJ3Pkwt-Z-Zf9K0359sEj81xjWx9qsHyyh8_f3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znk5rV5rP8zgPOk7-7pKDC_zGcLNq-WlCVe9ncB7lj_GR3YJ3Bze5eRcszmefwmxXlERTmRiHAGzKS7V5LD6SaN8KXDHDr1ZekOU6ufxjeKiRIfAgZsMeYipe_1wNf9xZtERJOE-p8K5-ibb6xgUaf06QrCViWsWbVGBy_WM_-ehi-xB0NXrHPKbJ3TBK8jJ1oakXPC381ylwQY3YXu5yyo-o1DPvn9o8CcE3VrVVxpRFuezUzgAmZeVjouXf6Yo4_t7Sl0hGhHBTP9qhXrmpyr953CV1F8xA5T69lYQVbFEaeuz5UVSU7ZfgH_9j_IVB0oUfI8Fxa1fxBO9ql7Cpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7OFDB0nhpp9Pi-J4oFS9w1DhGJjQoIWMkMSGnCRP-pOVv_CdI89_HTdwLNQMxwcfkTpiVZDQjMV9Jp44jU9qxnMopdbP2XqhkxokxuzuwR5JmvjLc9-GxwQ7YMcm799OjOYpnxrUgQKch9yuE9LnR8U6e3kMwOI74Jd2tFNBtvEHZ4SodmavgPSg8yUvqlGZXb6hNNPRkXpCejThUItZHqht8xshefKIRzBx6VDeWTp1CcSdxkY4k_kqCTId3N6Asqw-LDsQ8UvxLcqeui6USgltIzof01ZGRpJmPBQl7FT0JAK7oaGdMKERVDPGkGqW8biqKuWhS-y9TooTGt7rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-EAk6W2WTfmRk8Lszeli4y4GIxrmya6DBoIz7UXw-wRDT8Ng5rysDsrQ12x_-H2zK-NlkYOxC8JCH30p5oU3iLmyWiR8wbnxLy0Wp-Ajn_0zT80XH-akdEEgQ-ExqRL6m_-Au1VqnAzhyEOHFYCyTWCj5HO-u_HSfj9pwqotSahPnQto-kGqdGH0LBz1-BD9-ZqOkNm40oN6O75eFd7EZPtRzKCbIESIroqV4pjFdC1LkfBgG3yF6VcFFI9j81olAfk9sG10YGauQpk_3lzEnIl-hrJeYi9NuETuZOMxdxM8q6rnqLY9hPVTEXgn-4NHokIHJLm9YRUpPP_Bf2Psw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZKhDWAim21FJZ_Q7cd5E1jzP10TILZbrFHzG8YpHH_s8blLit4jeElrMCbuoZHgQvSAp_5cZVdKuQ0u6aoBY3X6_wyawUICeXkLhKSuQUtotMY42H5g8UR16Ex-GDSX220sBNv2cpIC5qT0o7DQax_YTS-8vXWdxgt-ckHfliH6u8LGaT0BaHBaGUfRIHbUW0IIl0wL1euzvZeprRrBRs8NOLvcJ5ZH00TCz0hXcQdRA4b6BL18hqnHlqvlzdW52q6XbsjiZIHqt94yGfci-KxupRVrf2Ml8VrS4QTz2a5usPtgJMf_WV7KggtWqNXXo67yy-2PU3UJPXUh5qvpRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJagQHJgTn2byuKOuoJzsBIV5oLteXNn2k_p1R8FXM91K2FsbE1WlalMYe0ij7DkxBibo0BzqvEvBBaR5o6aQG4hdphYgiBlR-0iEN7qKzDOaZsP7ShyO6QtSwjkFsZhaB6V5QbbPycpjY9-8T9bAcSUhOBDXxo8B98kB-GdEUsowUJXkYRLf0RyjjvvWarXgmqWyx5cp4O7d3D_4-fLDpXvDBQUZ1uL_dUISwqNt0rDuY9u5wLkXj6DVyrQjLhWnA7U0yqJutHGRIs7kRQJRwp1SeCNvKYkiDN8PQhBiz-h-o76yPsQrhv-UywwTGCU_gokMldqLexhsLZBlmrMIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deN5RIeDuk4oJGIeKEzcdEX_q09M0jKAxZ2H-IN90ylk0fUTsCqUn-9CtekjcUnhZTTSAJWuSH03poROT5i0M0IxCEwGIOrJeDbx4Azr101dRLOqJradOTcAXAMlhGzb7vEUz9A8aXhoPJ4aNp1E0a2MaZNGlYR8eb4uwDbNgWV-oYkoIOIOWEB12pI1hcow-is5bzjVjGdTZAW_6eAkcHEzgK-DoLW4JaWBc9jhuTWl_9HhsdJDM9FiyQO2PzRHkWJ-Ucpokv03TXkTTgNvmdZRRfJ53M66yYZPXis1CiX1E8yiXEuPecIKqXTUELDX4rCckpBVYjB9IwbxDuW6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHuoRu86dz1duQKkSxz2A1PNfTLE3HRhGGqJZM-oc2xn1KS10xkRFcdrjf4HCbvwLx49u1P4NxhKKofX_uATEA4pq5qaaS0oQmVsP37unHqCvMc9ohz4u0QEJiiq9tSr1RH2aHEVH0i-1cJVIKllICFu8AZhX4RmlsypMGDyn-VPAl9pnyyBno-nOTlfNp1LXwBH64Y3fvxtobp1lioiHaLEnXmsB56CwzteONpdl7Dt8ZMF9Yhla7awkQtMsw5z4ME1whlXlOSO98HNF7JiBLqFqLilojq-tyR84CFS87Zz_dADDwBiKMp1Z3k4dTFLfPXrF2VpgDh5eJgIcC9fmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpN6BXTLxSBG2sgLwrZZEnGtM8StFVZFif_zmlbkdNI6th0hOz1kMCqserSjKz-o7bRCK-O1Nqlxmaim8BWsxGwIZlDDNNEHjVbJJro4ZYkKjGibD4_jjQJoZU-_87vtniRYMK4xVqXyN5B403jXHEKnrZjzNKQzupFbiSBqWPVDohkF8It1hQu2FdMhHR7p9FaRzUz_xslPDpkPcShRoh0te5eonRwYgkKNGaoD4B76JPxemXcTDZhXL6uye-NELt9B9RitWlJgbNz8xZgVLb8leZ5cJKwdPMkFaRg2TJPCxDfMHdG1BFwQw-Ke9pr9mo4nr2lZVvDVXEuSUjQSCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5OQE0gSVH_JQnoURGG1TLYZb5Lj5O40BoXkOYC_0DZ2oK7R6Sn_PUoBnrkiinW7hQu_oOP-yIER4_o7hK07thuCfZhc0ltRz9zg9eEjzAgQI8cm_r9YLvq-vS0il5xgJuIyM_GqXXWk9yuiPJsTLtX7vFMGXJIslI155dZAIZi-aOCXjJx7blbZH5haAzZgMoIWgDHEMiGwMwOZDD7MQs9NQnQNR6JQOtzZJNZh8h38dplmShBPhvtwPuqcTFjACsGtutPAhqA5ohbtkP7IPCDZ287FdpkRhnZwUGwSfc0EWhUUN-5NA0lq-kW8mvQG-qQwBo8Zh71gMjP30g4s5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev3pOosJzwmdwVvAnDh3DW0EYhV2MP_ADfx1BDolukXem7YczoWmQwP-KLA3v6Mn7BR0_T_MqVcJYw0SZ8MN_Cj8-6qZQQ9XRcdOjpNcpcrfdKh5bCQVWZbje-zAz2QrmzDdAAsRs2PyisIGyOTYMNr69BsJYti10Qxb95SJE8ithpmWKcdz97Maf4-taPBQuyKlqVr6W1epY1j9NLIeQnNhyIREaBC7iO9uw2u4vLhS1aZrCVQEO4HD-ZFIjvUUhafJfXrz6sSF9HA1Et47pHZvzLdR0M3ARnASq6IKL747s_heMbje0SL1-dSqgh_c6RWEYthz47KLj6zrHYygmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vroDzLNCHa9Os5pYe3bWT9dq5yaXSCOIVLS7BTJv0iie_Kikxb8M8_pz42pq46sYzT_n9AUFk4B-RmNsAwsS5oTYygpspWQeO0qKvMKnvDgCgJlPm1flHTNOe6nmjgBg7hLXWsKxcEe5_mga2hiRuIbGu-GvrLeSSPoWVZMJI9bRIq4Um2i6Im33EXdnXdYnQENPHXZIk6vneo8HkTNTyFyZRO2f5cnMJiydBEzkANd3QPykYqhB1kf6ttAko3Kcqm_0T3tZ2EVdGeks2IEbnsCMHonORYIt2koSrfpD9bQaOh1Tew8ikgI1GE1rCP7HgPxvkoIggOSESzjRieaZtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnLzU6c0K9UKVF4dKMI2X0JAuuLpjSvc4UaH8OqCW1zjkTMz1d4mWZomGzbVf1B79aM6RwQnv0bGIndxdk6VKg8GT6QopQuc39OpZKeLIC9mLwGoMfhz8rhmfGpk_s_Nkkb64hdzaIPXj1eoPVyxHGLDfDnH-OG309EFwdwGICgKcvHdJLEudHz4XByAbIcrSn7G2eCSM5yoIVrFQZse8b24wE7Q4sAv_nlwJlEKVs--tSDKBCnpCC1fYRfrGIUUyHdNXhY7nhSl778u305qUy5UxV_qqIZ0sp0CsMMUvqaVtuz1w89Ag_K1S_dTyS7E6MZQa0CIY67R3-3xSR6Lhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gzhg0T21wHx8QrPVXvENoYsJBCTwVOifgjhhk6fhmo08H3zHOkZYlwq0xjPKc9uSjCbHoydmFsVmSO2OqMdXve8h0_PPOuWfwgJPHAahJirVCQxFxHI1o_SZRBiod_z-7u0XCM10n4zhrR84hg3xpFikAguu5Lbh0zDtGiDifotYdmMQ-XdsL6kRTTstvjNBx33hQAetocUvd3FUMkcEAhUhYQhvTHMk0P7xn2OCkp67sYjv6UTAaorNr8rCtR9dI-lwfzv-brqNVSaSdR4G8BdvH2oszvccpy_YjHIm_VMbwtiFiMgw46spvZBjVnobTL-fs1MZAvzQjvCizZBElw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r13LJImToICOu9tQM6Mz8ZGn8YIo4UYKt214BmOsR-JoNiowVAFlK9cgVkGoPL7YVbc9aSbYBhIsbOx-7ede2DTrQW7USVTdlVboQz06w9_pLY60L8E667o68PukPEXN0F4SceChsEmH9y2PZOeE5PEk-wmVpl9hpdv7OBg1CIvDd8bamNgh5Lr_jnpFUAipkQU8svoIxZ_YHXoyft4hder8aO_6YgSFhwp0iGM_1Wr0w4LYpYIBikNi24h8GMTFomeEQNMeA0tswpu_9rYps0EOkRDtnfqJTgBV6CXELkHGn77BuvnM5J9Ju9Cd3Lb1WZrqTJwAjLTD3pSKXKXAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EM8Ih2wBospzhwd8z6P2jR4UiJxh22PajlowgwFngCFUs2e73YbGyHdEA-8Y4jMEkUCMH3710hRr1S5sgR4TWTA1YTZwSkZdlQvBHEDaxwd-N6DPBpinMCIZe7LlT4FDAuQ4gDIMl-Ddvc2v9IxJLwkVXFOSKOiKiHVOBFb9p-X9wbPPCYbLX_PxOMTriSwPvxMFbWz6R4tkP_2KKZAPrTgKsvyk8kvTTc6IRwrJCNEpbU4BENQpFe48wTKO0px_zg3SzawGacd8zpv2G57UcGJccpgOL_GAx7HosSeeeP1OMDwRRyw9FGOeGYlbvxb17tlJLn2j0mKOX-olX7kHTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b57ToMksfz_-ptTyX0Rue3Uasoi2knQmvt-uijAqOiPwnZ8Gg9CBOSt9fv6zgWtaaUdtgk1AB65fRqpc7Eb55oZ8_p4Vm3sK7apDryE75iRP7Ttf8gCETyXXMG4TvwNhiESIwQ-rYSvzD-5juf2UiV12NtAItgWyGzhpznGMbLK87CO8r0qu-YEg46XqXFuI7ffXYDikhDKUjf_1GAsj7kWD4937Ks5Qz0NgAnJY21k9gRvgmKXomxe8u_y9RE5oDRpa82fiskTA-7Ek3IdmlQzdyjq_TPHBl3KB3BQiZFoDk8lfDrvtcujevWssPrPtHy66NQ8LLe-Fdu7ogbn7FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjxCqIrmeuVT5BnjrSvcpYc8K8G1HO0UvR6HsAcUfcmhX0y_Bb2fPm-A5OwWZ7Xap0Om47W579MBJlHFjL-wsgYqVYxjyE6ijiM8mTEPpcTKUPEUkXU2CPMvYwwp2EXQ_BFthhxpHqjtGNuIzHBBs4Gga9tdN6XQyR4usjgIFJWnTyCejgC1zpXo3XSYO_B6BhKkxnJIJ4HeM324aRuDuPQUQfz30tcH-F5lOU03gbu09_b_udJ2KROjeBWFWLJR-tOj1D-NKFwijRFebuWdnwPoNbVQIEoJP3y8aug6Ll-F__PucVF8S7zzKOHxjXuo1KROjA7ylg1lwQUT80zLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRmiy6GbVxeGLiK9W773wpjmioEORcyPtwtvOJKrZzjPLzzRj0XUFE6D7Y8n4LuLoNZq74LPIoIvwLk1kJy-Rd7RoJTUfc52u60EMcEWMPER3tTz-VRNPGr0sVRtMxPanhcLAtlSNe2YswpzFwuQk8Z00S8vto1ihwJZ376BUTFYLgS7sh1mHknRu1OBJGXlP3gPWkkoiQaKAIUkcSipX3wbiHazsxSOPlyPqwwssTBh0oXuPOlZMHDooJGYtxety2lHu5JjS9h5el-HLDLyo_cv4JP3MruI3UlMbjNKULjGIxtzxZKgDsaeJ0c46VnbCD0uEh7ca7Ht18lctv_6QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV5JXPFvrWKfAJ1zpa112RE_sUTutj8GCOJOeDNCFyWY3DVo83Q3vkhhG6KDmk7TzHvdP88etVPHcqcDQSuQPH7iaNjTegDB2RhJ6wcB0o261XQw7dQVxB3JZaXH5xt7UNrCgMsnPymakmEn0G81f8ZAYiNXNdXW76ZkmH5IEGNNu9T6FPo5N8a5RC29VzsTTxjQCVyBifSCA87cG_qRk1jB6pbupqZriO_qPJWVxGhl7PE7PO9yZ1RKnLDs2fobc9-fz5i_gflP8YegV-tzvAT_26DcQTs78XrK9LV50Us3Y969pdP7ruVjP387CIMtFXLNsnlwlnaT7arwdEuY-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk9c_CByrgv-byQM4CClQgI5ENSGCuVm0ME3Q8n0q3Sg25gnVdOdl-8UhiZgiVSGdPCn_mteD14_lIvt2Fb8GChEDNkoSVbg5HwORTlC_AcRcZKYjzoK_V0QZCPEyVE3YealRYUaq8e67BiwAg3AbYU0CRwnKhnyHiqihkKb7heHLglHXFzMNinsm-9BR9K8Zhfoo63VLX8NfD5roUAvdI3fjCznSPqWHQvZiX6pCT-S5Ul8d1cy2rVCPjJjzQPW1Gg0bYl-D9IjhcU8rNTRP2pXs5ZGtKVlGXVaUMEDLekAS4OD1XJfSCPW_i6pS_iBJlz-qm-Yj2081NPSwtG02w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzf9n0imlvbN-hy2xRDeiZZqlCHb1X_ieYI_gextSY1SHi1-J6kifz6WZQqYhJkmXX3BEjnobUNQjh-I3J7DUT4QG4T7uOwOhbH8xtK2SVo1n8VUYJrGbhsvh9aPpKYj8v8xQcGMA2wcexkgPOQZH8aHFzHPWdMyk352FAyXPG3gx7OglJpLtFUo2Q3gD3xFbwBC8ZTbmk3XIrMLqZO9q6AspnOviZ8zxh-gXUy1NUs5FagW5qrF7LtEAjTiNmgucspD9rxgC8v1J5733Qfpx5FTbKQIRtJfyMi8ji3I5HochjuZJhY0nPIwUlte0Yau9n9DFZXk-YkXlZkkRAkHzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqGf0pKCFDzLHYfX7wg_W1l4KTswxHlbqY5PAQBCW46tVQC-Sh2EuJ8OUEdsasBFXoFpgjvkYs0IuGvzi8R1B0PScKX-cwkYPR-EcA8lJa6t6WWYQYMou8-PM21VCsHa_HlQF48LOXKVnVGZNOdrlo6yhMdkHtMvekOHBFHIIyk385FkxoWtKa7iKpT3kkY7-XenFSPvP2zxO1KC_ibWsM5zO2FWTnLvD9VBZxp1WBIyXmWOQorzua8FcRMb207O_e2sqZeQTvMd8fCzKqbY0Azh5vy_g34Qr4GWkDLk2TmcVcwD3ufEUGOcfIyRPt3eYdFbBO3sgd7fRSCLRCUOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLcCNIC_Zqjp4ChOwLpVLtaKD7zJ_hlz40j-ITH9i0ZsLPSFSUKIvXa8NlKO-GmeR1V1qTweIHa8I002p8IXB-wC9A2-M1lWHVFsey4E96YyaMJcOBaVSdQHhaEm4FMy7Z1i452fe4NlQWBDwzSstD9O_689wh4n50hx7ZbWcfpuRTqOeMedfE5a0Ku2O7Rg2Yd3HXRTefy41LrReWFp581nDDQYChuZTRkCLP7CjU1AllEkE0Ky2XrwEdgT2Y10WoI6xU1h8akGClGqtZfp71C6Z7w03MmqaDWa1GU1fMG5ffHUBXDB-Wmg7YuMEwyZyktxn8yCBRaFzhvUymhm1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvymoGSr3ys2JEOoEuc6F8hF9eYtbnre_F-1VCfl2U_DgDoW3TG5kk8PJrczJqz8v9Hz-TXxvXvH6Iw5HS0nsHs3koGavAmO2XurS_mPwvISxmYE4mrjqbKdX7MKK1qV-53VpLGti3_vZpAMe1eXZBXO_HjEFfAWg-dU9UNP8U9lURHd-jmMsHRjc6nw45lcOAsQtyvOOdjzRyLy6bgC2oP3GUeF-0d_zUpAMEQgKewEjxa8UhdR_Xs1myKTppC9PgmG1eqdnOT_ovU7FDp-ILCj1bjlgdS606kAzRnK8LrUlZ1gdaj3a2g1ZiGUGjddIyrS_ExCbegho1syUfEGTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKzXv-lO5txswkK-RbpDxL_Szb0oNOcJwfq0kYnnC6EdtLKk4GufGrJ30gq_6rWi2e1CXExOvuv_ohaRtfPIwKDaDF19V23GisGmLAMu3YSDqyRbNRDbzymWPSEn4rMBkOcMJjVu8nsAm8SBHMJA0Sv_Jc1f7MKDC_iGKYg1hp7WYVZD8tB79DsiWnR4SFFWZyVZ_3Jtq9E_UR-xVludMOEe-I3Nn8YEIM-55t2RVgP41cabujeSvaQBoyuGCGrEPkf3obWbzL-MhvrHxsKDJuLLWM0JvhUU6wUzVnan2vJxZBDmEH8_1KpVj7wWnLiqT7HCuHxbHVFxdaUpTIAhdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L54ADEnCEo7lCwufjq84AH35pJP8-NoBwurDfAJSlf9O0Y2_NILixzVnXA0-X85MeTXwtgMTs0J410wRPcv3vtM405Qrh8qt4lRsTTFuajpVtTKWT5E0Qeam_6wyCIduLzDCiSBveIt82rTZzlyMIhPn6fNysNGPgxV0Oh052UWp4eSTddt2_a6MX_Ti0OM6-daC9kNft6CCUuKLWqlNAhcuqUqh3Xg9k6AJxTHPaHGBlCCcxEHHumbNyOTCFgBy71Z10z9CAOtpMdZ2lCacWg0aJrVqBVc-2NVLSJbRhO1VGsLHSFMwtX4JqMe8w6FRlwn7a5YOpH5j-daDZFjuKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNIbnZmEJlZRGt4fOgZTga2r0Enh36AsjWPX5Fnp_Ml4reuGMqUK4BXS7hZpazpLvsXhw21oQAInzs1mlybLP0HNGd-M0wBeIaZ-7kTWy-XtIrDa2J3QNIALA8ssh8cfEY3mSkeivdd8q3wQSxZVKIiTZRqtxRU7y3tewQlMPVFSD1kRz5IsFg4E7xrJuDkVMRYhDUDk6Yo3pxAwrEUYI7lvccq2KbDcZsKeVYJ5qLBI9zWVwaXXNLOD2HCsoYJljp7RQg46zSojaBsX-zqa00mw09tR1QIru_waZU6yVGYOxoHnn91f6weiqBpZ_X3OvMsC0BrWzPgNX7AILQIG9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aFcyBkGht4DreAB8i6Ymk30OeCFK96sq92uHJsDhMea7MeRVhNIDwJoHKCblhxPXwN7vA5r3WvKkKtRAlMzw_R0aREspcPPNL_E71k7n9aMEUbTt-ghU4foEPPvXfzhitCAYKf_McGtTQQn-btqhofRHfel_wFrShdpvDMQTcrH3_qlTuYPSMnECps4RxmYtQvxRlEMB-XUVbsX3wlLOw3zqHLEug2_xGPXomX2UOmdHSqZPAzts-adaoWRPRgYq_tn342vHTnZjyKxKhMUB8hi61QRqDGuZKw8PVhqsXf5emRFdfdvGEBp1osW8ZdSfBmihG4Vwfr9diBlGMXA38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=aFcyBkGht4DreAB8i6Ymk30OeCFK96sq92uHJsDhMea7MeRVhNIDwJoHKCblhxPXwN7vA5r3WvKkKtRAlMzw_R0aREspcPPNL_E71k7n9aMEUbTt-ghU4foEPPvXfzhitCAYKf_McGtTQQn-btqhofRHfel_wFrShdpvDMQTcrH3_qlTuYPSMnECps4RxmYtQvxRlEMB-XUVbsX3wlLOw3zqHLEug2_xGPXomX2UOmdHSqZPAzts-adaoWRPRgYq_tn342vHTnZjyKxKhMUB8hi61QRqDGuZKw8PVhqsXf5emRFdfdvGEBp1osW8ZdSfBmihG4Vwfr9diBlGMXA38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YepS_Q2k_Vk4flp3nGVEZcTi4hOPqUhZeZZKvjqs4wr1w0WLH2jeBgxyiGVRsu28k67bpSdCJsTk900I0kHRlhTktpNNDAa5Fq22k9lLgPckzZv4WgQ8KohS85fVJom7AFrqL3QrH8HHgJxB6vT1CiTn3gEPhNjPfISLaLm6mmqYFxMcuN7xVteVBSYDxDT3SqMdfy-DH2TbCvyFs3QlpPdY-mJznVdTMJ78-jNRvOpKN6-eeuueuVreSMHB0ReBIZK3wWkxwwQeS_y4G35M3sJXNtC54-GmE87I-Mg5uPOS5esoYK_hMuo9EeYHPV0u5TBA0kefun3ZtXNcUnz1LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPqopXU5zV3XuppCjCJeSU4TpvGzuMBL69weTWhxTnSXEhKRCSVE1oeCejlOcrnAgiQpB2L4LOdf-jiWSARMHWtsKl5Eq6lI9m9ArphcFilQQCwwv3GfFmvqRIXTpbZpHi9pyzFvbC2qD58UC5t7pVHJb9FEo33TvQJMZWadPyvch7yLZqgKG9J8IrG3K_Pd_E4BF5qLLscddLCZV_-33Pp1ZqlVU-OAh2KFY7j-7V66sOPdE1yByyBKvbYwpQ1ToOQXRIdXGNClbgRp7ZmCwFKwMYbYkASAZxQqxRBbDNX5qA1B6frFIO0Y-V1YgAp5Te21tyqJmFMfa7XMAmdhEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJkZ2iMosiIWeHA0vA8mIfLoyIKyYR42KArXmFg_dvNIV6hvRdQO6eKybsHBl-oFtSI4hiGGugVk6ejXpkLRD4CM3ypgB6Vzxl_NQttqbIHlqeh2gemU0HvWeWjA0S3KKzE2R_19Lgf-3KICXbiGMB8oE0gHEn0gBFzgdQeRQpIgdkx11yuBHpb0P6x2EEWs78NGIhblorONPIKdiRqJJgB0DqbetHqrNRxF5UX7FVmFjAtWRfd2CTRf_D6cyCMszxzy1tlus__WHC54F00LeBlVoAU-A6BArYtrTOtaPeDZ09ix6UfPz_7hCntQx9AGUwO1KOGKb6pq5i73O4HV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9kGdQ8z9WGcds0X-NQqtlWOJ2wWq67Fp1kaIapU0LuZ_JouWZHF6iUeYGHA0iYWt8aWkQyx2fGkjdEMaSbbBlUpe9FfJL9wEiSXcM2mX_Vvg5_YDCQmI0TYweMUPJtEoluNIvbqjxsesv-i3lcKgg4ir0vwzbZyDuznjbx6TyUX5gE2-n6vnd2nzSPf3F-byGTKq85gnMwyiywBCqpjpUBD3g_fDo62iX12FFnmlU2DcK4m1625zMvwxEJ4OhSXI_as_YhhWh2ejydQX77-1aaV1d3jbMrXLKCv9SazGAViJo4tUKqqpP6c0pswmnBb9OoyapiS4z60tNli6XufHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sgfed0Kg8iWaTSGRvBZf3eP-aTqPJFiTtJlVpLDhbWKqOogTKrbWGcCkDWJuG_9fX-_De0gpmO02w98ikwtlpVUO3eRrTvHY6tpio7CsVejdWSVHD7mvp5-KzDaPfNEfX6HobmiMpBA9nazY2KBNtCYXVpXZD94cdp6bikWn5eY4A-mlvQYFFoEia74QPxQjQvpIt5CowLy_zWFjZOR6GFDOtK_rU0UrtUEXi2atd8cS3Z-2ndK_El7NFJKJpnm2dwZx6E3PQ9tbtL__EZS_FhAgnkGR-YGLh3XBxBjbcOrWVvLXZIY3V8MJaq0T7t-c2OZjgxEg5VkQnwDlYwTddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgUTobiaVVDpjLV_1H4_YI9FMqrNhV2w4Mz9i-8bYCklQ05sRy1qYBUA7ieZhQEi7_fezRIN5ljHF19PEWlEPnzkXt3a2Ps_O2Q5POo1-Un8D1ObL9Mfq48qyHI0fKmITivoLIZ8n2GAN3GF1oX1IbX8BuqDlAnqVj4eACRVqQ9UaVRx7vsJVluuuyIPCwkhkfoA6NENMKfGLnTiY23up7ZtUTCtKX17gqKTrNgXT9gkTSDpaUAkyUD5HOAC86-Y_1adpsUapGw62anIoLm30ccx1HTT17GwVMnenzGP_LGpOvH_L06Rqysd5wprEUaR5ykGc8i8yG3BCEYkbcuZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkhgqLeo08Epf0ZazsKbj0m6Ut8MHjzUDm9V26W-CjIJ05McCgPjZmXPaa_Sd8aIduE-idQBJXJjqcH5xqfqsK6Vws9NURuWk59t68APPMq3_OPDOzHrzBld-WsYbGwSpfx0HPnuEiOhaPj1nqpt3Ih4l9MsTvmaQcvceFruWZN9t_ytbXXq8EilIxhtL8jBhiw2kD-UR9A91MEGRONqWVUhq91JNBvjc35e3e6X8AxKMZ52uBMxgsAaNjQpBqCwNRa90y0Yf52mO1FjvejrC6mEysCgmkPzk1CbiYn1y8xXDhLKnTinp60lcwMpZa4QUGlpiasAJF0U8K-UQyxA_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rfldE6iTKSnj5dQxlpUGRLAZbdb-BzzFlkUt6YMT45mGpHHJX5Axvi-1A7XN4RLcirLxtIocEcVGkoL7dV5nVQ5tPOgEBElGOa-XdCPvIxBBSzSda5am4JboYJTOPu5Q_6Xu65u4RGgU9TQs3iLTheq4tMPHUzTUKnzeYIDOcOvh2PP4umDYVtTnRTbIJ6_deAor8GBsGw59MD_UJHPJHk-l7KQFy4ZxTb2wNwVC7NX0-iQ81TEC2fB_Ng-165ISgR5qZPPQEAAmF-I13cFYnU1D_A5EEv-oA2XU5bf5kut2CI_hW8ZcxGPe8weHT4YYUe0q1ncmZN0ELBgOkfWASS3rsNM3XUWfrLFrJ-09aw6T9PPs9UYA-THfcRLMeDVe6R_pnP8iilwtRRwDzG1o-O8XVf3F-tMfCCto79drjz5yFb26sxD_np7TjdtRmCA4uVBxNE6ECFaLrYGve1UgvN8sVr5UlU0tc8jycqZWHqEJCs9lutwke3LymsujIOSm3jdYD5IFEBs6gipjN2-wENUsZ3CHByqyp6GKFBdwYjEZxv08o7wYPtq9R7p7-PrA0GS-uRjq_Ii091DYvchiBXddNurBsYRHBVTq8MeYq0RXkpOwNy6BmkEDaeMd5u8vsLNYK1NnTbC29HnzfXG03DzAUIjzVo4Tje5nrHslMEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rfldE6iTKSnj5dQxlpUGRLAZbdb-BzzFlkUt6YMT45mGpHHJX5Axvi-1A7XN4RLcirLxtIocEcVGkoL7dV5nVQ5tPOgEBElGOa-XdCPvIxBBSzSda5am4JboYJTOPu5Q_6Xu65u4RGgU9TQs3iLTheq4tMPHUzTUKnzeYIDOcOvh2PP4umDYVtTnRTbIJ6_deAor8GBsGw59MD_UJHPJHk-l7KQFy4ZxTb2wNwVC7NX0-iQ81TEC2fB_Ng-165ISgR5qZPPQEAAmF-I13cFYnU1D_A5EEv-oA2XU5bf5kut2CI_hW8ZcxGPe8weHT4YYUe0q1ncmZN0ELBgOkfWASS3rsNM3XUWfrLFrJ-09aw6T9PPs9UYA-THfcRLMeDVe6R_pnP8iilwtRRwDzG1o-O8XVf3F-tMfCCto79drjz5yFb26sxD_np7TjdtRmCA4uVBxNE6ECFaLrYGve1UgvN8sVr5UlU0tc8jycqZWHqEJCs9lutwke3LymsujIOSm3jdYD5IFEBs6gipjN2-wENUsZ3CHByqyp6GKFBdwYjEZxv08o7wYPtq9R7p7-PrA0GS-uRjq_Ii091DYvchiBXddNurBsYRHBVTq8MeYq0RXkpOwNy6BmkEDaeMd5u8vsLNYK1NnTbC29HnzfXG03DzAUIjzVo4Tje5nrHslMEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fvn_OVdcChRAzbJNx3WqK6FtfWfZofRDl1kfdBRMLC9E9ySbP0hD0yeP3YEd2DrHKddF-ucSqRY0ODNnif8kz112_bOwvQvw_WvgD0k-HMozWDQv8booLaz0wD55S2s5uN3zLjiscUli9NnSMET7iHol3MOP-gtOhO5WWt9Wdwle2rTBeakSVR9JH_RHSAoa9RoSNU1OZLdG9mPXxf1_SHSTiJa59fz1YXgATGhSOvssTpu193Wpk7MgWmh6iDfyM_T4vcE7sNBvEepquoZsDjbu2lD-8Wttq93voCa-JXwwiZRpelfKBgbb1Wtrwaxn3BYlum718_L5ADBJT_sWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-pqTvJa6fy5cxDX2VefRVc77cs8tDybhanY3w_Inx4St7cpH-z-MQ9li-Bl_4HjJPfYZ6qsROiQe1C7xHG3dRRCRfoQeT0EEoP_HJcZni6yOtVc_Y2IfdJWrSJ90g9uCPSYdgX-hhSVDgVUpHiNa9_8c8YyxEArMoSSG6iAFHAjJZ6jF39ahThVRw0ImCzImsBVRvsSLGs3I_I0Pq3VlcYKM5FJu-qZxI-RmocZNEx5KbI2E7vt3Q37-hjeyzz3dbtqmz9ENU4RgGAWpUlr0qu_gE2a0u_BP0J15mY1DnxG0Vl4x-KFiHB4OMHBNHoqJAftVTmIcdjf66s6cVeUvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-ICMMhIJ04sMu0H1-tzSn3C5STnW_Y5LLhA1NscPUDGbzb8AIulJg8mp7ckQCVFgFcfhCj9vY6thX8wzmdOI7I_GcmKUjk-Et8ubEJpMa3vaZg1r7H2EzhIEWHRHSJCbqqA40MbDW7Ni8wuJ902aZAtfCda-ggfufkBgcbP-PJgwVj7D5OEKjWoHJSZ4byMgpw-Mur5V1edZZDMdtv7sqMqd2tfms8lTJVYpyGesIJdehRbhEnWkQKa0gaOC6VaA805rYjmWkaNKWU8wHfZOsRkBc1sec6HRj52OXmStVxCXjwASgIKbFantWzHdQ8dN6a9hLIAjf-IQECllRIe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEyUCDscC4Q3wVycngHOowsKT5TWP8iFQTOxXLujfXyBCjl2_nqXPgnQekewbj6ND9IwLTEVximx-pSeLbyHwJ2zOFDCUEsXM2x7nmRfvhbaECRzzIfqOmd0vj0RYLD9zWKLRc2fr80mk5_YtAWeRfYuby7BPo_W2Pe5U-yDxGGejYmGYUxqhp2cpyrXs8_LmXFfTZuUdIcrLDeOj91Iy27hXc8XGvIdlEEapZLHnTOZmgiJGkIRymvWTt-6DyLazP7zin6yh4q2im3uA_Ul2Sa4oHgXqebsZmlHUaXZUr48z9bq8zQNFecYdzYk7sT4k2nHjINO6p7TcIk_zTxfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfAuDQCKtZHqDRNTOxYTEL0QeKzKY4QfUTZ6DynHXyYMJkCwnR4V0mku-7rkSLOaTj5h_uEIUEkK7tSyQCZrMaweC0CGdQGvMs8E0TaxHeEc-lIVdqWvqHfCvICu2nrSLE0Xa8m29pFPOtKu2PooqsZHYaktfIO4fcErC7TI_yVrd8QGrL5jYPKatR3vcDk9ccY-ZespgftLbi_VWrwir7vG_jPk97-ywFFaM25sI5txvSsWb76vEGhJk7cWJu_qq3Ycgu2ilsjNa-aUhWIrlqKjapvTNEksHKBaYplVz9GAUkNdGwkGzAPArjkY6TkVEMzR4_rUfisa9ro_-FbrNQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SyZ9REX3CAbkDzY9CeKSKtI_aHGEPVx1tQx4oXS4PK8TIz8uvDWnP_RVRTuDXvYuRWC9shr_6IxVa8QdgzcOXh6jRbXu5B5rZJLiiXrSTHNT2vLL3hBUbdsdpEQamz3dNbc2X-9Txgjx1Avn5FtlG46VdGoKH1xcjWNpV1Fro3_HGZx5mPE0_X58c1HqbCIoe9Hy8P4fzfXymx15PyBUS19wgMOMVaE-iM_I1MgL7YecL9wSzcIJkikp4RuKp9gIFWBI49Xw3DcOgpgUCRQBhMFc2_HnBTllD-cADWWfjaGVtJ-nY1t06qB1uzzOYvPQQBrsNAcqXQQlDMy9QvwaBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SyZ9REX3CAbkDzY9CeKSKtI_aHGEPVx1tQx4oXS4PK8TIz8uvDWnP_RVRTuDXvYuRWC9shr_6IxVa8QdgzcOXh6jRbXu5B5rZJLiiXrSTHNT2vLL3hBUbdsdpEQamz3dNbc2X-9Txgjx1Avn5FtlG46VdGoKH1xcjWNpV1Fro3_HGZx5mPE0_X58c1HqbCIoe9Hy8P4fzfXymx15PyBUS19wgMOMVaE-iM_I1MgL7YecL9wSzcIJkikp4RuKp9gIFWBI49Xw3DcOgpgUCRQBhMFc2_HnBTllD-cADWWfjaGVtJ-nY1t06qB1uzzOYvPQQBrsNAcqXQQlDMy9QvwaBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht0KIoQb_ZXKKFvCzX_l4nEVsFxM0v41CjteFCSxmqQM3WU7trhh5ZEtmW3XdPxZFKkhC3Iu296iqMOB4IjKls7I6qTDXMeg5oEWUu9ig49-Ehs5lS99sQtcc5EOOJPHDHIdHpTtsFPJQ991B_2O3KEPJKwMGgkE8LXxTTCLcOHLjiRbXTmVE9t3TYyYCo56irllegTJM8nCfjX_jHaA02wSNMO7At7trGodsY2YJ-B8WQbchKOAqooLHuFMYoLLb5rT9v4ZvZVHSBEWaJAFEOsvyWgWRhqAjVO0T4BFrTzWcgpvPI3a81Pc4_Zl3Qu8LeO6SK7eeSCAQplbPt1tjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyQPRdxWWQ-BTaObzbgU5SHu8TqqYkmTWn71rNrkjxy5GBIuD4jr4_r3YqgYRtr0r8YFAGbB6Tcn6nOTJAeUNsobAnqP3SHtuwht1Gvlo_75hPFMgmJzk9KDrowScbAwi96i5zIsZomuzuGqKNeI8Hy047r4EHp_vj5F72V3qtlMuaEHtHgjxlUzaTPlgb0DMhZjTVxLnctn56Jbzz12VEAsV73zYQuR3OnN6uXHiJv-B_WKwYzNmfyh9My5dRare50HpHyszcbrL6KWZU68olCgaDkhdygwKmHrv-bEpg10RS4atNuLCQOe5DlTtRTKTlghvBzyTPpjj3xN7DYlcA.jpg" alt="photo" loading="lazy"/></div>
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
