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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltn4OWJZNVlDCMP03buI4RK01sSOper2KZY4zxLBCIP-PpxVGlKMqDsoszc10XYSesqjqzY_H-dy7-NNiWja6XVQJ8o9V4NoOWQON_f0QXMlLhlcVvpWMTeGDueSyxBs5nO45jIuDEjRWjjOtCt45oEdQPrO8mkj1vG-ioStbVRLYxL9FRkGnvt04s1FFJ6z2n1TQ9xwElMjUZ-5XOmuLzA7iVA6RSpI5R7XAErU6YODzVw_nmuKDrIy00pHrc-fXtKzSvNs657xAWry7f7RpBnodbnbGP9XYBe47jx0SqsEk9TE-FwpJFln54OvK_gS-R9XtgZ50TClNTZ4WwIACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 239 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VydtqgoURZecFEyxjc-xZRvsf2YGboJ0U0zNYfMqdofxiBvRomiBcSczZrt1-41OCJtDoNP7nKs8fg2vX_C2kHccfBG7ZPx7aVHsfQqwUSsaNjCdRddjB0NhIAnsowy99gRD8xokamo3STop_ahDMxzLC6pKHotlFkRLkzg7H6FbKnH3xxpXdhny16neE3hoLlVMZy05_MRCZ-r8myLZStn5d3JsGAHRUxIRh4nMrTOCwxALDP8usm3ZFdvj_MykrH6dMkkoQ-FrfRp9rN53VIzcls3ZzbL48Q1O0g8xPydpSDMrlqGexKS5Syyfj-73BzOFU1WxaImy-1wNOWs2Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j47o4vBbI_le7gRN4ILv4GTM5zBBB_bfmT0zOlrwRnLw9tw_cFksd5Zpl66z4OJCNw7gNYJpNqyRPzffkwqBN6HxKfvdcncEL25P-qwEih7UBcHCZLBYiYUjH3s3c8U3wHBVIJj2W2-FkxvSPhsmRtdXNmFnqpAMQg_1fe5mTPOgxlvg1kVqiSHWL_wSDVVFcduw67z2Wr5EiUlp0LHN-mG-M-e5WdUhr6XCjc00P1V-ngwb2BWUjZrka7bWvDp38uNBADnKf23DQYOQpi0YASBv6TnPp7lhc5K19Sel0WRkZ0_V4lZYtdaucLp5QBMsKESTQj7QctmHZOfrytUO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuVU6N4UOTzEwhs6Pba8Lc5Db6NdJMSF7BjgK_V0_W8PrXcDxULKlKMchpeAzEYalb4CdMhz6Xqa-rlvnXd5LkpJSIObgnVSxCrGX35ewKibWjN96fpJARMiW8fk18_VA0BXMw1xX_kgmzPawS5uI_MpvRimSnmtdnCKwEnsp6ORdsNtldtUq8Jwx7JSSd-oGbssm35ggxcTJBLJOFpOqTqHo7W_QB1CrdwLKkseuiU6Wz-4m-Io-jISh2zJ3exWlbl_OAXn8-Z5642Ns5wLmxJ1UNRiWzOfHGpxT06KtzQVhf_9pIYOJRduyWfZkht5yY39Osu9xG6XTkBuD7JIsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7i7FJ3n8sq6E3MmtS1ANpoWcFNkbN7E_ZFcZLvNqPedaKTd1lHznV5zE4_sENcYRA6SidITKmcvoHgkxpL345h0c10aU6Bxw6mbGGc5YikJk_HzeOvO7VMLcrxXaHNjoJ6ohzBQagwjBywO8LEhmkNnS8OrxUziP9kCuUzGphgMCvYOzkuQt2WKkfRQbuDX8itGRhvK-TVuIHzY194XeN-VIfyJz0IXfJnvTMl2FRpuOHBtmtrQ8CNbQxkzk8BodDpcsZx54dwtKAnJpFXZ_zmAATdpAYbBkGwL2k7TWaxmziJHELMG1mHWsuTQaAJ573DIL-dairjKU6czJD33Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9SXnjgtgk_bm1_DKzfIfKfHfWIpwsRmjSDjed_k6KuWvrtixD_4DxvQh5xkYhIDmof9sYvg1PHbhPZZv7HzaN99azQ5eURPAt3BoIRHZWcfm3CWjNzf_msoRbFenuF2ZdS4uLB-xvoH48FcdCN16Xxt99Nt4Z0u_ss4HjuS8PIIcAAFmmZpFHwumGUKhI1c72ELk-kRhyp91dKbdbtncUyqjvFRg6NiOvk2YkDNsvU3E3PclyLAaNJOFLzp1UbTRbqfkp2csCTdTKbQGcuitQeJ3f2gChyKw95CSO1O5eUmsymKqQ6HDooKSwZurFVncdA6b6rtdf8KD3mvu5PZ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdwcAmgMLlbsWa6VSMya2mW6MUrLhYF55bM9atYjCdTLeV0jlta-87tf-CKuhpVU2Y9w_3ifFCsZfOKa7oAQ_-4gPfQOxTxeUPFf8HnqrBq7RvFeys1rQKmGwLfMtTFgoPJuJYIjlnt7HRtHi_jCC2T9fZHS7OhSlrSXgSmtdlBcYh0VTPBNyuH-xxYMzamDneNgwCQdshh_Z9Z4gmx6M1voBXYzKvoMv4Ml3GbcAIeczrVsaO5aZi6YcIg7slZ32otHtdWfzl3kTbeKC1g_1gufWUXZigVcB_k96pzPl3PB6uwhHpBPYTtFaT-2_PAeeUbvb_n2KOhlcnUwjyQoxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2T0ANOQDCfKdfJH9LKVsyDiI_AJ2WSM9vwBaLEobEdhXPpN0lvOC6BtvdCDPPy63qwcqxiRQsd4obluK4zeCc17JRk_lUi0pC3qa5xc9ij6qdgk3l2nGbudyGcumatSwjW4uQ0AnEUH1EK5GkyJJ3YgKXHO6xubifVragiVSxIlj0Bk73JsuopzgpwAQdqvknNscfgTwEhDnkgghqojZpjUBdOhbxYK7FXiczH3UxOqqHO2SqcMDDWZXqKj0Ey3l0VcmyT-Y4t_qh5qfYy4OYE7LKtZY_UreeE74L94m9jySVKpO6OzHhUa2gjkSggH6COfMuaeeE1u2VAYljqmOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqvXEvQ0sFAscYeM6LReUXaZ1xPmDKQulZoDwV0_lBQIaSrg-vzfUm-XVoBGKvQdKLiYclpQIQylHIRwUTcYRNwdeVrYjMPTXSELGbVlNiCVa8E8Y3HwkqRKNFa3eZ3i-Tb152zmr6oNt7VXdjTFmBaQ9Rx9pav8HlHGFXVsy_vTp-O-jfgUAZLz8Am2hrN_AaVauCOCQ5lC8l7slZJHPJV0T4IVmTG8R6QbqplEWx5AnJj7tTs7GKCouir_YYgK1hiq9ILXANJpy4OwpWnPnyce7cpseVVNTV1lb1CaZImd9zrFO64gvAvPiju6KOiBEjmYR3hNMKhV3pVfMvMHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Spzo32z7EjYebT6U5CxHcaaHJrn920La9b3y1g1lTjlBYQTtPPj6g-p0qb5_4yy9dIU5QCNBGEd63smaqKeivgcLTOCa9ELKbnGMVMIQx_WTT9FKQ8M5NO6sFg7qIZ1E9LNWDJ5073D7mBX7piUfz7TXzXY6fYqsE-j_qp0T82ewHMVeL_8tZ2fz39YCMMbriIHqjfenX9autnkeVVzifF5FvveGkVjuBE03sxl6qLhT85uJPU2IMri6l3L-lMzCRv36wXGr5E-OgatunVdfDdTXrl-ywMPmzTcbhztTq3GHuXnkUGYB3Qjy5F4w1t7vUTV6FB9LoyuJeO1Bf1brmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOGADgXHeFNEQ50S4T6Wi57TPPTzW6qksshgjZI68PyhmYp69GCD6Qby31m81SzDSsfLNDXK5bZnJNP-TcF2mRMl67V-nPbzGBIvWIqPTQuQ8MdLIWzI5k86vjhmI7EiPjQJW1jzF44GohaF5za0ufxDKQ0scsbZwxeqRTWmcVhT0t3a74EgsPLekCInzKXeqnL3ZIG3DwbB3E8B-Gr1JWAFa0sOL1Iszq0ktM2uY8vTOV4g7hgHDs2_nTF7WUD_JwAv0wxp5RBcbeN8K2JOi_f-uwg79G61B4LROGCMvjOrJvzY4jCoravBnbhkju93xSKzK9vPk6iwm3qixCbLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4eGbeQW40l_3UkpcJ4sBwuSk8lq7RpkKXJHCyStq8ks8a1Z7KczmTOpjpwqfVfOruGKZRonfaWao-ffctybF4hBV1km3JQ-kAwbppZfSFXRArriwiGCDKlInWbQHjwzBcFkYLuivKt_oEQTH4FdO_aF0davlbtG06sAgTjJN4WzkRsdDiHmk0gjK5-B5xmpZM4vLlQ2YVkodjZqt5kKH7lMGAy64UTD89RJfdfxzGaEWRjjZWqVEv74AgjNkVA_RMGMYA5jECcYDjWSLDk8pCp6pXDmTPmxdlLiutSRxgM17zyI1y9eL0q0C8_vDDUVxExLo49jBR7wf0SS2EJArw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVpkPWE6WdSlLJzYeWuHdbZI0Wu6X2H7wSG5fJbsmDWe5HloB1t2l5CG81FTti0dDIDM_rA3hjqFTLIjgG0H17nGLr75wq5iLLF0e524iC3oOIEN4OfRQnWqURJFXMg4cmGYGiM1uPwQDsJ4ujYNKmJht5362rza56OCwQQ2TLkSp_WbdIcJwbJS4C3dauviGEgpRGx5xwAuGMz_sCzlLoAY50wBbtZ9j1NwWQQZkz4wSuMQwIFGftg2ciF9nCXjWKNK2sq1bTEjTYC0rQLuK_vzzVHh9I3DmS5Ngju1yNvO6u1FRUzj7Uy9ennyV30HqZ25z2Ox6XrsFFEeDFeshg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=mDDlFRFUEEP65sS0Qh_Q05z_AernrjKQL4gA8AMieL7IkWkXd9yqcBqyz5iBEQyrbrxA3P3mA5rDVvz4lj8HujRyttuQrb3TaBAie-qyIKLJTElQv2CYHeW3Sa5y9csIyrIDIKZJatJe5FmR308_PGFKj0DKDzgkp8LXgNsnezAimXIdsdzszHi9rqg52eG9Ud1ZtDCqPoGIgzyBE9UtqMzixEtNAzjK62bRqwL9azbWIvm7C6PajwYydG8yzu5I8KmDvAf9fzMILxqVFPlXBYuYI-rZ8yDr1ix-2Rl_jyT9iP_q7ayNSJyYEdPD_mOdUZwxBPRRJhprCjpX1GRe9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=mDDlFRFUEEP65sS0Qh_Q05z_AernrjKQL4gA8AMieL7IkWkXd9yqcBqyz5iBEQyrbrxA3P3mA5rDVvz4lj8HujRyttuQrb3TaBAie-qyIKLJTElQv2CYHeW3Sa5y9csIyrIDIKZJatJe5FmR308_PGFKj0DKDzgkp8LXgNsnezAimXIdsdzszHi9rqg52eG9Ud1ZtDCqPoGIgzyBE9UtqMzixEtNAzjK62bRqwL9azbWIvm7C6PajwYydG8yzu5I8KmDvAf9fzMILxqVFPlXBYuYI-rZ8yDr1ix-2Rl_jyT9iP_q7ayNSJyYEdPD_mOdUZwxBPRRJhprCjpX1GRe9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY38epu5ab2QzdauWIs7hDNPn7wakZXvDTDwxzl4FUbSxjB0YVQuu0GwHfu-Iy7cOly3bUAVaxfXkFOYbXfZmGtZR-7Xta6fwgxLJGW5xokDvQ9Zt-HMncDAUWN5eG9ZUjZhRj_2HMZhE8XKcarajtjmkTYuk1oZ7mGQZyNk5Ju_xiVl-jKWwSP8XvGyXGtXPyr2c2IMNy1J7tPW45nsoXUdIWHwwJ-ZSSFHMqLGcRq3BSicvryRUN1Pb6ZMiCpkdXJpnd5kqeuG1-SUHZ7pw3dfRvPvB9yj7gkVV5VHsrrl4PhsrZipibAOlUDrtIUBnJlZDk0S9oR46ALCWXdqwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8W-XjFuyF9c1CnpvZcDqTh2joXJR_1u_dioBv5YRQ-9ubOc5nx3_gvETPx-2dizzVvX5mvTQNNUKRg_uAs9T26HmNJgvhHJbhU2uyowBs91r4YyIt9Claf5LGMPnfCv26Yza5PVPSUzlJj-gOP5GYfiitgiTDD4FC7ksNtTfoF_GMltzk0EmCsFzW_8Nsa4TQaTYkuQpJJpXqsPdoZbRKNSxm7bXYav1-T4kAFWGpQfhH5aBqmfjJYIO9XvYBjPvmUMoLMYapiGCelJZiVv9QqyAI6TZMsFS7aksXdyJvjGsfzXgl_gtIdjOwfT9R8A7CLOwlNVZbz6IVm2Z25MWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3lzEhJpaHEezD2unidTKefTZ2cHfiUWbIHrqSIZwivsW1nF8Uk-fpms1ZSHMEFAQhFYIP9cvEMlxnVvb9dRak3xUx9mAL32BP9xqWFB1AFRHfFlLjlFbgT7i4E4MII32DP3KqMaXR4JV3X2zg_daeMgwzO987XbxioK6LZ1IJWuoEgMxYHGsYOmeLNx3OAegK2EPc81gKOdzxVVKBaTGJ9G11DX-g7sc6tTODK4MYS4GK0X8Rj79fUGcl67H4UxZp82-7i8iGw_G6b_ROMZEsrsAN8L_HBqm9oYcVTrqWgvW6o6Qvqs_3XwY0UP6DZrpGjhJQ0TRdSxSkxc3oW2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KH-IB449tKV-xAaNtMAdLR3XixcARpGd1v75fR6cNeiD0XruJo4fWDv76DsTCB5zAK-UHfdcGI2n5RHfxadBni1NjtIT839ZvVG76Wez6VpOeN83VYttChuRO80kJO64WH5VWvR9qQS7JElbXLEvmLzVOUC0NxdY-_GEsxzO8OaZuFnkZgwo2GG87Wi5mHL4msP115S7HQlaI3ayLc78cSBQGKyRfdlU-VHFLQMFZ8gWAs_AD2gS9QDwsFhGlWVE0F3T8ju69iVa4Zdndz10AoW_6-uDHaZYgaIjsAQJigVi5LCB9mvw9B1xGPIpANalZ5pAoA3UqhwqKfQZpheW2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2sPRovmaFARNOqUztMdZNHvL_QfWdn6hq0x6JCWXEcZ0B_p40s_QZCfUJhoaJ-que0p8xa5yhPp3AQGu0X28PfH5iGo1lR4a0lqZsHartbnqWoQT0lgK0V75_KwXmyqCG-urLMy2ImtwVnKlBzQw7_egSu8c-1egCHlPJmifrBPr0VOWrPZY8diwHz5FmcTsSGSS0rY-BK_uPnRPkbk6mEHg4wnhvJF_at2al_zpTkvOlBV6_Lir4s4MjVp7yaxbi04TNhlk_pQkHvohyEcK1pQ0V0d31suX7XtLdzI9JoB5gPMM4pOFEql-2m7909oLS56k5Pcc8AyoGL0nLHxpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQxhHLq5AW-1BRimS1uXw3Rw5PELt44Z0Dqv0_LrPQTOFg_ycsKJTGCKEwM4q8uItIZLEYjguh9kggTNWF1uaW328d7KC1MnBGLvvnQnI3EyeeL2waKVwqynsmpqx4YR33nl_Fz9-oODvJI5RR9ebbvyIjA5KPQHssMMcoR1wYpzLEgi5WRUMjFmBocCx0boYMSRs9ZA4gIDYx_aV9RpSkTK7UDZJUIv0Et-PwBizspiC5J329O6urvUlD1LKS5SBPaiwsQ6NTV_Rub8A-F6kfxvTqZuxtrfXQNZVQyMb1vy1fuje--lUAlhS7jPK5YwWox2BnFBo4-zJ27re7LbUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ed51m86MZKPeLEshzU3Vr60M6pElIb0R7DqPNwOg2tOAf0oUB0yeUrLphzo77pEwhsKPHAZtf12vBNn9askLtCKLYM-FliENJN5EJlqBt3PPnsW3ENv2ogg9e6ECoqRcKcvyt7X1rJoFzvf6vghA_g07QWhM9bgxRQBhUwQTeux4JSsTWgrZ78wvMUuuvJaEz6a3Rp-exlxDcasOmksDSrFFfYFjeFfduonbKKn9ss67BdurC0GwgkEez6cBj8NMUf8tB_gjBh5eTZ4nL7kSDu3w9E19rtsi2i8fwJUHFt5zzEtU3MIS6_XQXtWatoy_0mhp2UXz7vmTzI1FTOpA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijBLnVg5ArVMATd1L9_beNSQPLuaNivxtvj37cCiyabJIgg_TVxveQtc7kjJ5WmVE5Q3UyVoDML62K0kClQZbcx5-KsMpGFsM4sprUTfN1cq8q_k8-93xMshZefVBZZZsbpbHEnyBsSvK86bur2btRh7Q8SlwftoQADOWF9UNSvobfHU82S0Vb4S-77aECCRhjXpMl4qWdrZazXigH8JOBvNoFBDY1K9YemdvJDLk9qsq-WZi4ElQXMovj93dEq-KgikWHFh_-k3XsMCePyiuzXMbBfsWul3rVhXU3cx0QNhGjmiMMjLeYlWZCZ1NETZOcV8GBgmNCtCTiFrGEoUHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovZQJdsaskRJg6rWxX0C2A7wk9XkU4kmz6JGmsQ1VDNt83BdfZFqZM47qODGYkR6c8_tBEz6k1JcyCWav9NdI4k-5ikNCy64J-Eg1WnNJni-fvMR9VEEKY_1up3nbdRP4cRCCxLkBouZ3zDysNvVYjEPm6aD12S4RRNkD7OQ1aY9x9py5yrAyLG7XRs-_6EwajPk6Oa-ryxPIQCL997kTqvs6GD1E4QeWVkOktUkt83GVuywWGj_yKziHh-odn2tga-mripV75byirb69cryJbODHmQrAQlME-yvtBNHX2Bb4qM374FoxHNoqAIutA8KDiCy8JUXdlkeBv7xMa7ARA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMYEXI3gVFupZhFo4G_4C_r9RhPX7o5VrzyEpiCJfWHN9-_stlvHFd0J231GUfRgUvXKk-ejEbC-s5bQlUW12IviZxDdOHPHsXXdwBw1b95CCT0Bu3MVuGrqfCQ5BJ5BHraAeznrUZ9tI693nhEKLeb_q04K7_XqLYpTEvxmnri58O74Q3EZ-oWrHxjDUt19HuDnxJW-Uxq9NHUdr_fI7kmzz_VZz5JJ7tpvw9mk6lSPpLXzlRoltcsvw8bDdGU7fBG8VwmaPMDJwEAdV3izikN9PVQXOt1I_AbdZC-q2aVAFTHvgvL-2-DLrxnlbQUoRPhVRuWpNGV7iet9xdwW-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu34oruR5cz4rHfxwc6AStfLS-tgSoSmAjm_gzWa9Heed8R21cOil41FsaXvx7HMfGmDJVe3WOeSLM41upXXd0JsoptgzZdxW91oLnJxAJeqv2bwGPapgFTkWRuTbJehtzlNPMWmc__dnt40VIjqcU1YyR8qwvcmNcc-bkgXbc443zRUh7MC3qV65B9OiWx3SAl7KzMawzTWbRI5jCT-Kxk4RQJ21qOZBQN3zOSLzr66G__jdCSPyt7aJrC_RIpOvUMvRbS9_qehX6dB-HvCcGxg3Dq34shF22GotDm54C7-2-xRq5vV8BHtA2-jNfcyRkj--8-qV5j1xs_0PMzc-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INoe0B5TolBg5hnvjg6MjnLJiXvXJvD_iNEWGADNFgpoK1UThz4taFOFCSaO68-6Q1NeeJDAIW1bZZtNN8ALu_lpbrH8KlKVbPUc5WAJeqq3S05eAtR-nb9h1cBVuCs_HFKGeJtbmjTO2pnbtoL6H2IS04eQJ732AVrrdmTikYgHrGP7VSZYSxQCTcvYCgNt9Ihusqq4tM9Y39keBEk14nyf7_l_eY8V5X4PexneAUqfmDs5GCNekbEyedXoX-zGxaKLYd26-XZ1fEgUVkyg7BS4wfEGmPTNqZqo0A6Ek5y2TELytbanVNjjweclPPD85XRtDf8g6gbtbwPVf0_xjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcfjlAS6mOTNcTSq7EYn5pbZaNeNBb-OaXT5qltPtRXWgJlhwAHbmZB2TtYGbVKZ672cM3k7Dxx8BoRjkgUcbMt1SGJEPKIYgnf41-iL182aPerdBLDNoa1HqKRH45QUwk2EI8YtwuurzdfiENckBT-kyRoFBmXJah9n9atB1EIEFghLIBuJToqMHZh5qdRArciOIvVeoWefYZONu22s5y1XZ7uiBWVHERJ8sGe-K79qRJZ8SH9x5ptjdKEMoeG-jOeUGCrxwYVEP1jhbA7CVFqfxPIJjrlFJ23CxJeeMZoqka5rX23FWIZpIpmuKkkCjm0KrEpRhdJCfbDb3edAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn-5D1OAGpnMDEGYc9tzgtsIV8vOzG39LNyR1sCj7RABAkbFAJoG-zzn1kyrQihZ32f8IQBKORr9KZVq_X4Rzv-80e_DI2UPzq1Jz1yxXDXWwfwNCiFmIWJgnThgG8eFRSsUNUF3DzTnMfsKPv7hTO0FE29CB4KW38-VE24MqNIASUyn8dpV7WhWFfPifHwgZEcetE7NFLGqnR7G8Y1_Uws_PfLwFXnf9j6PCMIzmtlldn5OaZg1HaO44W5MnsDEFSNSyDZ54SfYu4eMfAii2jO0VGVfXu8vz_seYihy11JwusEV4zEEyMy2KTK0ZA-U39EPPSLhYkRGZfPi0PqKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZ-i15iccwOL4t-LoUoiGdcdpW4lehKza40E-VDuDZItDiJIJoCCWLHb9NIImAmD7Mnr61XrrmmKuSN-6Cbbq6QhYRTSjSDVu74DDtgS6YL9zOJvkKAFth-FRKrQLdY7VPiaJWvaI2OcpCEnHAHcrGGwHFNxRfEAZl7ZBbv6hEZtc9tFv9He79PswYGMAMfiSYlBb8EMmgQrj2FT2hlGunACPdqz-MPoZszpEVV_P8bbTHuowmkIu6kiCmSqvhQSJPW8UxWyZrk0LFt-InpBZ5269WKqwQXmbvSWmPMVO09x8t-KiZmVPNcAby92sMCu_sZ9kthRqkrUP-8j1ORJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFDh0xCJR2aCgpyH4d412SWWWe6bBLo-de-wj7q5GHj3BvUDjSb0Us4qQw9feI3yVJYhXen445HUkIHSNQuX5uXJlcjPmiW-2YP4aJ4fST20HVWa2JQ6ilaZfIVKh3-blckYG6JQ2hHWwwR7AJ9gBO__XxkQeuKEfjNAGqakT3MIk5e4xhId1X7j2WkomN-7s5yyUsELRit6qohyUgQLhJ7fHRKFNzj8upqGtPqgOxJTWfa4QkpTIL4syGuOF8SoDkPUCQlK48kbxLOuqnl8dCIaY8YEZM0PrKCayy3_h4g8cnAN2iUT9GFaq5dQ1X6CMQCbIYfNGRI7GTY36LD6Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKI6lVmCg2JwgQi0bKFJdn2nDgDyWOkuSqoN3MU9rX525bfyjx70fr8p39EchdeYscbNzQbu_oXkYS__d8IgO8Y5Cj120mPGGBLOcLcNXaijz3Aq9fzLE3cZLbMjmu5XaLlD4keb920C5X8xLR_gNBvBMiujfhT7mvp1YhzEYBOY2OQQvj6N9IX7dVHWA3QiVx08vp92i7T5_XBIcek0Sel57ppiSF4FxpYosSz01w0ofndSIn12QwGMgnP62sY47lZ0CosjCDGvFKDgZXr2iTGxLyrmKfMZQszIBaVSu8JtDv4j2Dc3yIM_Cdmpf6RU6WEST_GlUI6Veb32y8Cj1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe2q_LRWNzIDL9ikl-YMsjcXVHiK6_7RacGTQsNzWIkSvpsdD6ISV40UmRmVPZLLBPNL6FNFQ15XSq-cU4yzzO57WhZt6pGzlRNNUO1AESUD82NEHldPInhAYp5WhKe9pGWt0rVNM8yuWnGs1mH9DrBIMo6nq5FGUJa9e-RK3J00ddG8_8SIZ8G0rW4VjcuPYsedGhgu6HD0jSfpJVz5W3yggmR8iceeUD2-2p-11fgPtbeTmhva_ePBj4Dn9dTdW26GxSO7J28NNE8QUYm7ZN4epYm8VqCr9rY5HHrwWK-Z0KrCegpzpfCg81PVDRvha5WuE7AhVLid2s0N-713fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqyAVlgsi32drp9e1vNrF45xgRHlN9iNui3Bsbjmp8T235eUDee5xJrGCPGms0tVQxtDfCwuG37MAIBJPno0H5Jgxih5Zj2IZu1q8VIuxZepGtVvPcYocwvrazDV1rMIN02BNLYdqXdhJJnsK-sgZru9TJFnkqxp41QGAfJ6TdSKPUvL_lrTddUhyX6tunx6yt45ioQofRPedfOg3u7HLl1BSJ2SSNrImnf_i3WJsUVllrdb7QxJsV9UTY_hyyB5bBC1sNpRL6haZfFvqZ_5Yl26USU5WXSLPLM6UOG-0xF4_-0TFNZ8dso3wCBNdwaZ0GYDBuJo6mIAJNa_z9_Now.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGMW1_ApHs9SiqMWIOe549NTEV9iEw_BRIwq6oUUQLr-gzFdf85HMMvVfZTifHdfFscnIOVlsjdEy0GiSDCFUsYm4rSYlrrY4FoPUsFPqeXimpac853Mhmn-PZGymuORWEcAsFlj0Hksvq86PA-ZyN15HaamGjQTqx3F6hiP6PolGgvclUN1I4VS9x3sb_tNKDZJcR3H0HniAeOVcIsACeeAUGE142QW5sYRUovWyeSkOTVoaTLJxd5kjC9Ml45cUljVRbV4NAjUSFQj_ME3WAh2aJVrduJ8KuhCWfT9m39KQICfE9BBT6Ni4mOcJft3cDvRe8F8bMAsObVx-Noy2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA2mQGfEGps86Md_rrZyk6MIBV5eWZdetNIBry3rXs168Ylc_wnvFpDguhEdpxPLFp0oWvkzpiENk9qY9E7ZDUnjx5_3Z2DTEioiKhm4IEQ2Ps2fJ7hlEju1NIvWfXWi3BQu_SAqfLP7LyqDocf218v5ppB0vW5BMcSWdUJhEiNt5dtVZqOgqQIEf4ScYYs2mmC6KRRJETIe_LmTeTR6ASv0DPd28bjd0grrkOPfYXPEj6QtoOlv0pU2XtUsYi1Gz7cxL5pIfcFgiXf7FFge5W3bkvPonBtGSRl9UCK8rxoFXFzLmcUaUa03nfVFuofEmM_0WVg42cgdpQnFe80OuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayB3vxNcUhY1j63P-t3Yh4Xp5x3840g2oUccK1hh5Y5oonHVtJord_iiFcziOQDq-FIjhSpzh4j46vGLEfFTma0Cr8qlvTcvYWYtzmD5bJ7qlnHSugEQqWRQ2FYsEDnDPROc0atIZylZFC1Sc8JqQIMtNsyOiBgH90bQ0isBeS3Oqb6VyCh7O8jZcM7oeTE5kAQBbbccueqi_SgVdy4TPaxzVRLKHw_XGqn6TG1DeRW01_VW_X6xuzm8qXbD8O6taS93x8jnMR2XK6Hb3ogNvnOE24c7MQ4QEvD75Mupuu5KaBRYwvvLUQmeIy-Chd5riOCm-opSF70qcR6HLS66EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxQR05R7x2DiM-5RCBKeqwV22uByfNEfBcUIeePxX7OIH4eGVU91JmwZUwyHrlmwUNGGVE1dHkfUGm11JEfrTxiso3IEGHDcYhIJwFOoZ3mfSe0CKrW47mSi5OsvoMVbPf1rppqQf_Rv-Qy4Zee1k4gP0TnodSn_WFkb28fBt4uYu6ncPLzj_5A3qYa9ahvxk4omsj-mCHo7sM50VCKjMcoAOmjHE5AzvMLzfq-fYBxP4inbupMKV5NgwrQUZ8XKtDLe2phAHJj3L83zgEOE0RWs_AYC5hvw7h7UPFvSEyltjtJCnVkDu-MC7xD7DX3Wu19rPVMyW8Wx_-41Zo4R2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INXk8sUEqv34OhYc9i7GCvIeS6Hzw-XpeG0djaQxqAcc75R3dN3Tgfvkb-WJXbi3vQo2Hr-toindCZyZYYpVUakLn9HucE6Q73T84CARiRTrrBmTqh599UGkAQ7KdE4c-JKJ4o18_6Z936NGcMSSQn1V-utBMZ-MKctHhct5y-FRetN9nnxCt_IbQ7dheTphgZ7PsQ931LcNT181L69aU_3XKpKI_12w1CwQ3hGhY4ItSxg7Kyzm5Hy82JH_IFhe9T7Yjpovw9pZGrDMMvRUzZil-ptc4BO1ozcqI6-yC4yz4oUFGKicyUiVtWIgOwopcS7kBCZYMS1ZMd4xc3aKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbSkheKW-6sihUNQ7Ts3sYWL9zT8tHwvRi0wDzjMDyIIBRmuYXfewgsukXH1SLM07FrEXm1_A1OD2QdRSO5z67ID9LxAqVkedIztggcgDi4vbCp3j5gnOM9WZHdhiM0x8aCZd_m4D6NWtQaiFAxA-RVCae-8bbZpEq5WCvucZDth1NuhwaZpnTOlIZGTvx4-LmNjDQ7hjWz87JQyAHYa_U_bN--kfaTq8H_IaE2Wfpkr4mJNXLHQe35amvxEhi9318l48ccfM91dn8BOE8vkBI7MdsEHaYdgQuHg85flYqyQ5jL-lTCfvX13whSuM6VDwFpF9M5Zp68iVWGnxeHufA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm2-7hlq2OPIBkbhAmLW-yqTRR_zOg80Tj5ivVvP5QHSOGzSyT-u7ilmUYhkMOrzrBceodzsikAGqcfN0a9OM94jz316khVPI1kVdtpJ8mnVrUcKyxhCQ_8n_pANh84-YQq9cdbd84e5ybrUlxEw2hbgzKBAeP54McoGtQvoiGrxSqsl7LbYTyJ_0vXLCQGWE2KOYaDBcL2I8oka4qQfm5LDDgRbmFXYgsizo6-DN16evMr8SAGZpcBudu27DzYrq7Pu2d_P2VQ19N-SpFt-UxXzt-4gsFZ-_bh9uDB2xGimwI7y4sWCXviZVOHRq8r0jcozwkKIbO7UCT0fgIR_tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwpHkGiaO9WP3kmoI6Bz93dfVOX3Q3PVxqAJ_HJpojvwHHrHtT441yRIkHunWOvzrVafjSzTyVZu1AY0iHdJnnDSsEiN9UvrBDGf9QY1PgcgLccv5KTYUdm8m4Nyq6dThBhOXYv_mLEtkYrXGNVQ5ZvOqNJXOXkh4u9QjQut50fLTVFIgspNczOX3EB-RF_z2r-JopgiO5u2H7I3T9-F0Bh2otksbhAsTeB3yeeMN5iMxx9snwsum8KNzT7SW6qaYYkkrie5wZrbX7zCFeUX8QlvPZctJATJmRunqaINZ8s7gwKqDHEMJyD2JY3vWrnA05EFskwlXTixS-dEfxloJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWWjhyJimqF3EgAyHmQiBECPnes8oqUS_1Mph44tW6vCE_wHcSTt2vxJqFFAM2TElbZc-1AX0d_EJ25R0xrd_qL0H4ytuUG0BpjkJY_mrgLI2ZJxYUUfch8uFLPRhix7834Y7JXOrYTodIdfDfFtdrSDxqxQVR2phYcX4D6_suffwD2shaXlfn9MxjQ7UQAY3QSJZaHAF5ygaM0AlhYOdfwxytGjgCAPSjbi4LQfIsWNOPxkl9tm3P79AWhtdF3wYsqIz2as2ovB1SUnTMVfrKUpKaCRH-wcAD14v36UVy8Bz9ukDbIc_Vl7vcfxvxM3nb0ubPWf_IGjMsjN4Q3vYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S94SHmLKh27uv6L9nSJz5b7rbNTFXk29VAlxes-Z6zlhi7nH4X-Or2c4BmSVc-l5S1Qt12sWnvtekiP_Gq9ty3x0G29K0-2DZVdivHm6lwiXg0VJFxX-Nox6b3dQPXPLimjDVo9NnXzlk-dJo6SU3h3hYRVFb3e68we3yK_L7C-EodxnGEyUmucpuBUOQ7jE6COt2z7irTG6sPDVu8oVXinqx5zbuSetJgKlKT232APhd3PvPJWGMYuLgw2_tfq2sENy5DJHflpqYZXTquRKbiwsPVlpLxe1PwbnKAIoZTR9bMyKy444-rjKFzEsNNmE27RpMm8hwY9lekvb0C0xKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilBYvMXUkmVsy0fBSuvbb7FtwAguFr2XdVxfuD3_vI2JmumhUo4TUWXDmwm44n--gPwnh3jeb3smvxgYcxHaTZ4OITdh2B5jNgbkl8uX2DRVvSkUn3p2Xh8bvjJTS8MVJarLLoo6K8pJ6AxvVv9HAFz8xtWNWtNNpRqVzIfi0JtovhWAAzcHA0S2SVXq47loUKpJF7qv3z3kYSmLlXbwbkSKrAvFllJmNpNLDJoq4SktKq_675I6cStx75H9uw3zvbWIGyoptKm4qYDWzdcPKium07lE6RuNcU6UdVwBb_5NEoJCoLw5I3s4xW42atfYxDzJz_R9jVUyBoiyeY9hKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F33bSSn4-refBfHtNXf8_AJJnrSLzKGAGmwUo72D6k3l3dl7d5YI5RvKbZkQrcFQXxhk3pUjCZpTKcq8p7dvFtbcio4j9mQYJH_T-T19ETYqdlKdVbFmrv5wN6C40wtks2m5MpII1e9ZXMuRUqt0r8Zu4nLUha3Fprzc62el1P3mzqubaxjHv5UKmtJGJZHduVPAewWZUzKUA0JHoXAuNQR-PZqL-QuS9-9XHxTsKksUzN6ZwrhzL4it-_2iiQzufm5GKU-tucwQmEKLYXsbq9VIR6wDtqLIe-cfl8sg7sgkXPF53RsJy6uoUjNeualW8p7hdM6DqW_iuUDDlSoe7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPp7CVypIPNiar-v7m1h5bpP_Tk1euKzW-6I2YJctAsDCvI1-41QCe7FykRQcDFAPHpXaDrBX7AXaoEmbBFixsuNxr3jp0VSal2wl2u-y7C3dfGf824-MJIpUikMzMEAdlMBfZrokZ-1kSD9hQ5jcTawm-EBzoE5hg6JtT3W0gmPWWzWTgLLouMfuYBDeYJXJBDmQzyws7Fwv4BsgjiaRSehEF5OObqNkBpZ5Gq095iEDfEbsuDZOOKtKUdnVGJdH4YmuogQY3-ReGs2rd9giP7rcaLD-EkOGGtxE6FZYRVMjd59Ne5x3vYOhpQravqwTu-aNJJ82rsKjEcFtWSC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPBOxP9_6snPCXDpcumTiHZy98nKqoPO503SOukUJy3JQrnTWvIDjRzq596ooPs9CLxgSOe2F-Wdx5xsQVVRFjD_rRpCZbJ_a_iOTkm1jCSpH6BNcLSMEWJHcYnS_pcPgPEXpU7djX7JgwiQPbo6xRLtjZU4w-7uOnSb6OgNlhXhn0PYT_JNXFNyNUuKFJN_Q_1tivqXwsKhU8WQgy84vg0eAVcwjko6kUELVlmXcjnFTdoSlhvyKa6GPE_l7JR5lzObVGiVSo8l4LdNkEahveVhi6ihhm6qJy8CVjqrUa3lJTfmZBDA3ToCY80Xnn9BgGpWMFqkBBYlkTh19eYj6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAoRYmPUBKc-N00h1Q0hBGkT3I72O2xC5MPi0jj3KmYpxgpGKXNFO_9JwXzXe5Yxoxe3JCNlNptnSYSxJFI4-ElnpsA4eAU53j8bsiQRnLQ9Z8ki0TLIOZslnmtDT8HxhsZDbMh3Z9gPq7QV6oObKb72f1Hrstxp1cfSTr0mN9zVdZoJYcnDtcuNCNySQMvOmzx39yZU_3Jd7HBT7EbOqOKS8qpaOVkCbvncdIG_0yO0JORqp_J9XAHimcuEDTwnNHFvT92PD-iZauORDbO8MNMlSK1tvCn5O8z0dE8DV1TbDz8ZpDRSDV5QWAUd2FqYCanHkAJ-IJOKC3uYMlH2Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6IUTaqDWIdr6rekzWct8RNS5j_SSFnBrbNaEDAojWKs0RECPpuLTi2wUJ0tUk1wcCcK0bsPU0H-KYFwgVxViFv2aNztmXwvpwCp7-r8JmfMd88pEGyhxbBtr2M01KJ1KOIveIze9lj09N68iJ3DHFfmTGXonRuR7CFHepwfbQAfkFdsrJrCa42-kVx1P28dFQhULbySYeVQN7SoXRv6PhYCqIWjDShrJCfr1zaT2o2HwmusfuS6KvTWZ-mtfuuXlTlGL2nOTfqdHbIHe6_KXoVfnE9_iBiele745cDT2uwgZPP87gjGGlLXu9mT6Tq4G0Cqy4i5hwSbxC22rDwr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnhZ2ACW4drUtrC7RnqQsygLGKU1GCnnr6cwiRGYEBZ5Im2f-3ufXtHo8PLA_3fkCORyj2f3aifDBmuIcWEKWpseJNwTdJ-zC2GlCaXCunUEK4mdQx4oDyfl0uIeZUTjJ1OGbluBXK3hMd4NwWkR0Zai6c_iAveXxf_ZAEjpzH2znFiCnHx7eUihJb-PxWl-YSzxPUGOy4dTseS4ulz10P-bTlMWCctNRpqV22w_otqRNWrRhR-w68F-yD1oYHHxo3IXYjw9j6Ucy3uQ55W0JH9KOeR1N4Rgn9C1exjBn0UvyoEvc9APkSHknR9t3bl5M1ChsaFFGdWwxh2x_klAOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyo2SlLwjGSJ6icy0zKFXubstLmEF9dZd1WbDO46CJmHWuSjQcRS3W7Xi-hXyQ4KKaUkQcnR1fD484H3MQ1J3gCToApBN_TFpK27hUSEPvq_hh2OhD-EcNu9mDQyVea8V71sB-MKMb4LdRO6xXr2i_QjMXNrRuipRYMkZCH-iqoVEuGigtXWUMbPy1t7Gc7xcyz7V9-dxzd4bPvJ0Bcc1MRvU24KfN9KXGdo3FnU8st4eD8o6HmPvBEczGP6O1kkIw8qHivr63VpLHtXLv6ZmeNcQd1zdFUpXm2yR9nvtGZtQYAw4a5UsyP-7lz4Md2-voiLMYFESysZ3kDKy_0LYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joCsW5nWgPgMx4aibNKXQ0NSiKUC3t_8Ifopd_snLsZYIR32ED_-H3pfN9iSn7wB3CHdV3TrBaOqshsqljbIMdIlQigH-YbW7-SZ6SIPFGxX2LAnta4af7poZ_nSLGY0_17n7MZoY-ryexEmJPst8TL8vSgYlraN7RH_TC6ukESha65Y0f3hPjv56NCZGD88LcbkKqUGhzsCC256i6IWz7rG7O1J6ygGfUxvQsqhQvyYuBLpLB6Lb-0TtewZ5dPdJWhTAE4GSe2wMM-2YHTOJ6FHGW3-w9TNpGaLfJyrArpcwr9ounGg0SJFkTnV54mrebB37bVkKSnk_DKujTMtsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahbRiUhYGk0WsUQDHVUhqmKMm8auZUyhMZbVq_SeKko4PgSr2IJ7eJ9Lo0ts-PhQ78N0Vkl-GMKISWNFPs8kSgh0yKBmggC4qJpOHtmviVGqQutli1z1gILrYSqzKZwFqoIyIbEf4jIT6hRetoFDJFKYXxsqL5dtfaQy92aY8FTLI1ELJ4R5AQhAkZiOcRtMuTQHCSFn7xIyP5ya-oHe48_DJmTb8PYkP2vbVBTKDTpkztaww8v-ayLTNou6RrkWuCRaUeXC1SSfbch1nUTQWNdpSWbOhGtfZXiVKqRJ8dSWsKN9PjCeyOY44-yIt8091KoWXp_u7nWUCZzzIEU7lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xa99J6aaOUfvRYl6Me6mmiOu0DGz4WxuiQLfKzU1O-Oim-JIsYrYFOzfSza-Oy5R6L1PXhhXb0u72b40N5uQgNidx0-374OHJk2_Ld3R16jirQH9f6K5LQ9dnqSwmzEYRMG_xVlp36GqwOk-V0RtIA9X3503lVL6D3aoiL3Qff1kNDV7zkDExQGkvBn75YwJqbkBCGkRHbCw3sKqlNXDQBrx3ezkNhZ5lp4H0EhzLLJHlgIYsB13nWXxQF9dmeCp-OeFAYtXoDfEGMjwDFS_fpAEXH3q-lWBS4uX1cpIG3zGHuL0C4-f_ZHyZ-70nqqUcK_GlTQGutbkUxgSBfWhJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GilYYY5geAB9lKRdXstYS1IBW6F6RW3kMq0Kc4ldLyHM9VHBU4DbOmeliPcUMk9pRFMbCjCBSekCigiYr0wjFahG5GjzVdufkzcTj_gIiHpmf9uO3qt_hfwebOwCD2ySEkCHQv7zdMvJdjcybiByEI-Rz3iLb6zZQy2yVD6SDyebZjXv2I18xkb_Eo3HvWok31lWYmySaonD-J-u0uI7SKtQEBwByQQf0sNGor2EflqvZRbcvj7qccrAzqh2c0XI6xwEWnC3FzRVaDrPksIpMYE6GJS-zSxWuVFsubCgVIyY-g18KmIN3Fk_df9kvQVJJ4dcR7shKK0LoGMek8U1uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWS8JKzQHg1pqSogtWDXCEcXMF28deTsl2l1tOH5tcc2LRqjy99C014wRN_BmE616ztw_iDsVyXbPm5lrItovWyFgjwvJHWIUjfez36lIBf3WRvBcamcJ0mmfT7GmOlLsiRHG8q1r7Gi2sD4TDlXPjZYMdwY6Nrkz5rFCkzW9q4YVgcmPrNRV9QSkUnWq67h8sfGy2WojtLtRsQnNYTutMQy4yPvXW_9gR0C_s2j1QXSahg9uQmwXRFlUnqnh5oSObve8IOYxr7Y5zl_y9dhgZb3u0FreaxjAi7biM2fSwk2pCgZe-UHE2QwGAwzvGagYsYUtbppOznw1smB6Yd9lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd5emdzNI7H_2dxBZvYa1OAc3A5xGKrm0WIg2YelEOmhcQCtB-F91u51uzygxzQSPD6gia8r9MoQUaxbWfHE7eYgw2x2qj6ZRYHTLpWctWqH6wMIiU-BepS5VScBIw35eFrLoyljcaruTZykXONZsx9Y-OwYUcxXefoe24RN1odvjpbx5Bn_gW2YeJEH5z5FkIYzUZ5mr7lJzoK-ov9F0QQw467mCxkO5QuxgaCY16vCYk1Metu_mL6dR3YTBHPEsHmdNZP2k-tGO0gI4gVO0OTzkOpa4jDD17dWJvRCaD-ikuWvth8Ngf0Ht-PFy8RLShhCXFMFtYxFIVW_aDwXgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwI1yBMSzBHcJUX4TcAY4JtU6BS0ltH6rGVwhfXq5aW2V0xM74Xn4EKphkFolIwwBSJ-4YItajRfmZPUnruD2gyWuG6IeWt8Rt1_wCxqw0LZvgamm0ZFiWnBeFmH1IRe4cIQC2eyhaxM7c6lJGDeaFydpA5SovVbgny51_It_G-QyR0CBBbGWb0foVt8fXMUWaQzOrs0PhzuZYmnPyD3NlVuw4_iwwnw_Z2rL5kwHzqq7UsmRI71CrGKlVdasSZ0YZRcRXawgkAkVKe6MgXA1Nw7D6yIubasjFMjdD1kntbkNLakYfbBb8PdQ2Kky0tcqJcOduGPURd9LGh4In2PGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-pZe9Mvvl3dmtezuOXJmc6gK3Lvq-UfYm8Jl6loKiBnBduDv8OKMWHSQYxdvtw_VOQUYmSLdE0A25tMkfK49a8uXuPjWpGdwfWamozPWzd840NE7OinjunA8oumzeUTFfnZ9H6tdWRZFdL5TcQ0mCpFe2A2DXfieFGQZhoAvS2MputB5AxwrE2NTM19tWR3foq_HkJj3DSrr28TJyOamhrnQBonIfesfndAU4sLl7gI3Mt3xANcCFqm-fHz9qhfw_GTK0jTREBzFbnnOeh2W5_U5dq3wbYPOgIpVo5ZdZw7RaZlOgyQ6c2Cb8Sc0qtASBxJBV1ZVDi04DVF4OObQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Y172eRIJDJQnUCY9IIvWC3WBcQmli50D_m3O2DTY5H1YeFdPqAUI8j7YpazMg6WZPBsqOnz888fE2JuSXimNwKRLXglrDubJIz1UWLztR6XzlFU1487txMPY711r37M0_DcZAsghccy9YqAb2vt2uu8h9ggghEwINYIfMll05RZeonMGgLAjRBxXxBXETPRtZRBUkcFhyJRo4vUghQMneQH7Hxp7tM-MDjKfq-L65Buq1BEz7vAnXJBDl16p8eET4qNCwg2T0bNn_z9xr3cVAZZ5ptkTLU6erEiPG9X6S7FVb3GYywvprMWf-S2htJOA3rN97vuQ2RJHUSP2Oz7eNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Y172eRIJDJQnUCY9IIvWC3WBcQmli50D_m3O2DTY5H1YeFdPqAUI8j7YpazMg6WZPBsqOnz888fE2JuSXimNwKRLXglrDubJIz1UWLztR6XzlFU1487txMPY711r37M0_DcZAsghccy9YqAb2vt2uu8h9ggghEwINYIfMll05RZeonMGgLAjRBxXxBXETPRtZRBUkcFhyJRo4vUghQMneQH7Hxp7tM-MDjKfq-L65Buq1BEz7vAnXJBDl16p8eET4qNCwg2T0bNn_z9xr3cVAZZ5ptkTLU6erEiPG9X6S7FVb3GYywvprMWf-S2htJOA3rN97vuQ2RJHUSP2Oz7eNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdZfHajrR3PRLsiissiz0PGnXo33FaG20Q9lXJLzBe9ebMeQBKtzQwJAlrfMYKPDgbfSpoqZIMzCH-uqvBA-9mom10hnNzwLDCkiohTXrNbUP2HW--hIBf9jVqr4Qb8cg1Wcw4Fw045hMtHK7RfLG8NyKXqHXHgFraRHJ6zAyarZG5zOsbZrF0PYMDZ1RCn6VhBTinIJDHPaOQxG1xufD6-hatBoRx3S4IpkQEcam0vh-hdyI_SpYk8rlB3JHwXEDLZL8u3TtboZdqfl7PWAnvpS7TlFySq_AVMqW1jGkoMs51dMdBaW0BhWIFgMwsRdbFvkOv7RN1skRJrxBv9gZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCNIBahDkcC1oNhS6cMpDKJg4HfbbAYnnvK7OSNcm3lHdfuqmU1jvukgUwyaCipfv82ZR1eYQrfOvNMt0Jk9dzLvL6TdM8pnrk5gd-pu7Y1SoQVAkpWpBDHwhbqgCOahZUtibgk7q-istY3hhCiBziNxxmQyFTErrwu4qA7rI1OcqIRFm2FRq2sMGAcPfavBx9mPdj8gkfWH_1qKrmT5K5rgZ5tFdpYngCE1hzGQlsdCxsPNr5juI2iGV1M72ml2uuwlBHkfphsxvIPUlAVveP8Ehuu6LWWiuhC2_AOxRyvKTpNpMGAFzQFFQc6xgNkY9kuLtGW0cEORWqz2qQ90GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-itEm-ah8v4AUIiaC6ZEcKX4uSGvh8SRl2AJbUvBj_rTxw_r5HBt7LJW7FTDc87PdPYnZJkkNxL0vx-nR1gaRf5wCYMDcsuqcbT5EgdmuAt3zWq9tN3rrXzEANBHpL6WKxkg-LaCla_0SNFvZpDFENUKMqn4sfVuXCcIqN_QrPCM-nnYa8Ik5ZxRabRSrLfD23uvBJbfb3vGzJRZFolwdMchVEOf0HLD9slY46LV-9W7E4czc4qdr3idTEqrjKwgUSz-DY1j7Vgu_613U9ejUX63tKU18ZS0N94QhwH3BpuwxbWbQj6Yafc94Yolc4LgNg72fSCkSP0hJHsMTNKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDrWZxW_09s_3uG0F4cPXwPJrN1fyVVX5cIuJmNLs9aOQfor8Uef083U80FogG9hHMj3PxKd6wPTF-RDjeJ26XVeXjG1JOi-MHG4eQFXxW-I3BALlkhZAf4IoRXCZkIrWfs_jfKu3vIrOS9RA7NYmB3w86WgOH4Z1Z1IfTm0NlUke8GpIkyzyi-SIzhBler89Fuxccqx7GjKHH9lDtmKBCiLAspNNPLo2NF5xiRi8Cbtpx0eyQ7SZDrzO9kAvVTaA6fEHbA6eUcqSNL42frOXeJBuvRhehlrpSARJ7d1XCMPwRRATQorOZlcgr0LrEIt68VAfa3J5ydTRNRESAUlQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UE3L_HFofl96x6r3BlXArRxCJB3b0X2p6eSqQetdqtuwubM7xhXWf73gAFntiM7KO0esBShMZmlbCZjffq9lS9wXaN3LDAoHCiQPMzWFrYDRE-q1rLxjOQJ09k1WF9C8IF2nd8odvRzqtsx6UyEMc2QAdvr51gybqqbY1Z2YpZatwOs9thIV16H3MOkZvAUwLbw33-dovGNhdwSSBWW7vAIiqrg752SmvBN6-aGvr6My6eZRGzxLlJrEFS2gdcH11gK3Vw9KBkYXyfE-hLjoCJas2nVPm6AvsV1a-x7qPmQW6lmUvgQi7rwWUvrzZlZrcIgfIKzhGpJGUogZRcIIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWgA66s75HADBXCn-Hy1cEuDRm0JPQm_gd6oQEOHLyW9sEAb934cofkjbI4MKL7Tn20gdUAKQfreeGQ1tnc7_YQFu_Xlt02xn3nin1lEziXIGSn_vy0ogfSPp2Yk6AD8TYpzDxKOQiTXky-Qj6SH_hTpMIWuiJs89qTUX2jfvkIp4xWLGlQHLdKNHhZT4l5rY61s9mdDOAoYpRiXXrcIp3BPcNK3ElFwpInWIqyxnLHuBy196IDuw-sgtKuyV6R0NiYdIazyXz1mCrjOgmJzEsw6iPLJ_8H3SsLurDmL3r8Y8GuGbMMeq0xdpcWq0rPNZO_YuIbJ3SPd5HjkICuNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCN73ZPAQXEcHuMC7I-GVwRNDj-VXOPDxoA1pVxM413BQd2_MPClzZbDfTcXBV5W_d-6HtGyQDbdW7WdbLH1U1dGGO7TCASEYC9Sn_43b6iGtIxfBo9ItbFUzhGLwRBIE22JQp-qH09n0cC9SaWtzFCrgZUEgx9LhXfGuCzQbffyVk8dmDMCQyNd2lpqw0Aw3-L4Ge8xDu9_tTwZ8YjUMh6zWABmNAixM4cdG1OaQJe89i9KkSku6c9Shp5u5oJZIDlF3GjtAYJxIcGhnjAugzYl_bVefEoINt8cJoBbqGeu6xwXEj1MY6uTDrf0e1BGhpuYTe1pqdEISBWwJ1zpHQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Kve8M_o79tV-KU9begXhis6-y2ObE6vLCyaRxyLR8pDNwgpZCDty25YSh07bPogRa_dQ5ktuiQanSTOijECtFN1xbZ_FNLeY2FWWMNF6ZR-NO45eWfkKVL6_CEJC3X9JwhAwpZo7GjULJiKXDBJkuSug8pcM_EnsAilcKJ_K97qxKnm2ZHRJs2_ZO86wdGiZjF7AODCBoXD3F4vtCWcFSQtV8RZn8Xsyn2CbF_Y9dE5qX4bbpMamsiF6f93ZogEl18PefdA2M5p0OAD2Acqwr2bKX2HHggfkFQQl3zANdfWj2AIQ_PBnKGZLHfysl4OnztynT-MZ0k6q3ucuscpPJHLy59Bv8Qx8PNQrD94w0nSY_cgtocGnnaHVUZVHVN4Uj78rjd4INcomZ43yQfo9-o023kXBeJ2zlEzF_CeENSj2CMuyLaQAkieBvGtXANWr4ZsTtQ4TZI-ZDFT7jsSATVdE7AQqZqFnslViclVrQorP39J73tDVbs07AItGPZE4oKM1zKXPj7omzMiTNAxKnWxYBAFB4JpuKLxkWqOFYK4R2o_R-SIUVHDR0HXKcW2wFjw6_S9jXjbcyri98NK8FADFiUTxz8xoKUJtrIv3QAU61o2E-cY39_QZto53f4WU6F5Mys-3FjdQlXtsVI51sNql6FQnj9cXbsHcm-Z7evA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Kve8M_o79tV-KU9begXhis6-y2ObE6vLCyaRxyLR8pDNwgpZCDty25YSh07bPogRa_dQ5ktuiQanSTOijECtFN1xbZ_FNLeY2FWWMNF6ZR-NO45eWfkKVL6_CEJC3X9JwhAwpZo7GjULJiKXDBJkuSug8pcM_EnsAilcKJ_K97qxKnm2ZHRJs2_ZO86wdGiZjF7AODCBoXD3F4vtCWcFSQtV8RZn8Xsyn2CbF_Y9dE5qX4bbpMamsiF6f93ZogEl18PefdA2M5p0OAD2Acqwr2bKX2HHggfkFQQl3zANdfWj2AIQ_PBnKGZLHfysl4OnztynT-MZ0k6q3ucuscpPJHLy59Bv8Qx8PNQrD94w0nSY_cgtocGnnaHVUZVHVN4Uj78rjd4INcomZ43yQfo9-o023kXBeJ2zlEzF_CeENSj2CMuyLaQAkieBvGtXANWr4ZsTtQ4TZI-ZDFT7jsSATVdE7AQqZqFnslViclVrQorP39J73tDVbs07AItGPZE4oKM1zKXPj7omzMiTNAxKnWxYBAFB4JpuKLxkWqOFYK4R2o_R-SIUVHDR0HXKcW2wFjw6_S9jXjbcyri98NK8FADFiUTxz8xoKUJtrIv3QAU61o2E-cY39_QZto53f4WU6F5Mys-3FjdQlXtsVI51sNql6FQnj9cXbsHcm-Z7evA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qzhg0q7OA1RssoTul-b4zNgMB4ofOF98vgGykjPcDV17AWDMgZT7VEKE0wxRTd_mNMbYkNy1cnnWZpdJyuehiDNvdOAJN_LKszdbBfpDqqQpu0zoAjHIWiRuko6A7lim94yEFu9-BjmiBksiccrsH4t6wm0W3TcyMbTAy1flDIUuXdi1qoSXKzHYBJbEL6d7ktLvRQ5QZlcc3e1cfW3kQOVZFmQxMa75yv77CKVadc0AiPGlZdbUEFCDhl76IRsGAzleu07d1Z-gOjoRgJ1OP9sALwdT1PG7Jjw-WbXbuwE2r3wQVEZaAoidHxAPFrIAC9Uh6sVmZ8PDTDbkQzsRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E89gpcgGw195369tnK_Xazxu9Zf617n-SAPbYj6HP-pWsr0QoVq852BcBPvxUFGWhZnAwsxtRX-rBrUMFde4iqXUQv7kX9FtERm8NXcVbkYMRR9GlYSVQRvo1U3hx7IGAIbDEoyvAaqlzErG-AbB-UvFrNXQ7U0ekW0qWSXQTduUzPuITcTC6xcQ2vzGxojwiqyXKXW-niS2ZmipTajecHp3yujpKPsXh1_ZD9aiGQt1uLmH0QIiYJgR-3ghrqoy_zALniyQpi6ZkWkypb0SZl-8kAhPaHFd4doD6ZR1FJeVc_EPUe_zhD8EiTogpYbJFCpx5ySz5WKA-rwHtckQHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEUBCTKJHJ1tdDlx2UvnTprSuOcOKeCDlD9SJo2Tf9a6jFPQkXGZ2eMXGNlPJSdJs-U1zBaqhVOzV2DL8QbEAK99TwLWOFFY0BM0sJiIfc15dnupjJDIjlLIkNaB53FjzbuS4J2GjI68a_MZN6fF0COMg1xUkCN9WYivvGMSLeGxZRhreZoNDWhx5yKZxz3gvYmID6mayWzeXUB2osNwyCGEEwe2XepDmZr8ZD_SqMqufXU3JtkaHdAgkueBG4eFmijNfjiY8ZPuCS9gRI6ceL4brCQI_mNQt4IwsNUENz12yY2iKfAnLSMbk0yBQ1mHkjqy4SzWABP79T5oTfqqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgCb17dBnyjqVAwSMpp8u16PDKi2yENfRHeCdQu7E0LJ41-gfIP_9X6Utm6QQq-TNPPIxUWNEHCW6IiQACSp7145Q7ssyEEK6tMLByQN5rX1i41pl6VFPrNEKDRgFEwM-VnERbANlkDYpmaNWw3gqBIOWS1bhO5vA4Rl4ong7U5BELWNt0Hjp3wOa1FPqB9sLxdZW1g0mn2Wmm6jQMJJg5Xxxu8qPxz7NZfRhqZ3YYrvKzcjF6B7B7sRgrvqzOIUUUNQJBvPss84XmSSJj-tzzmb7qwtYrfnSc14mtVdeJX2QtqdAtYj6FH7zcqY5Cog4xks8gze4lqxWdCCnj596w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGm1RD3Om_YLxVcPBnUNzMuBc3YkZbMa5faNzKqqbkNyF-taiBksSfW0Nl1teM-d4JUNmIhVAAyi2D4NnQPREwWEfL87nz5kK4SJcoL5HP5QOfvHBzpXeF9o_al06nSCXPRnSZTXUr_ETphTF35okM4swyEHd1iM7dvlmfBfXT7vs7eLttRy_fmlVzYKc9GgiUDOAeRi3IkESRHHI6i9vePL84M-vThlL75VrTO1BVwYlx-Iu5Gb84WC-6yNrAaAS2dsE7LbqOIGeCQavO4Ih1tjGfFx98_Gmdf7p9yRS9KCRbj6K-cRShXPljT3RJVKGqXpfh5YmQE26m9BX5wzaw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TgJnfz8Q5k0XcLWuElN1L_oyIhs3ORNnXvdOYN9eZ0H9q5s6w66eCb2H-Fr92Og_l6HkCLp3FmZsJJF6e8EZBXha8jQZM-i7Qyn4jvsgb9jSyAaA9_rmLlz_bvOUQ27Er5-sTxMJ7MAFsm4NK-Blv0jPQVdYargPc-zj94YQvNMlO6CNQUMxrTzgh2zMoBEHZS_q5ZJB-r-z8a55e9eryHztZ7K645pKslxFRJfS6gGuCMBjoQGYllr5i66oRxvTWuyUIc0l903wuHA3C_4DBXO4RTaQN0Fk5AsG6rEe8XAzFVvA-BUBd7y3jqOnxqtQkFIMuTFmBpJROxefzmcQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TgJnfz8Q5k0XcLWuElN1L_oyIhs3ORNnXvdOYN9eZ0H9q5s6w66eCb2H-Fr92Og_l6HkCLp3FmZsJJF6e8EZBXha8jQZM-i7Qyn4jvsgb9jSyAaA9_rmLlz_bvOUQ27Er5-sTxMJ7MAFsm4NK-Blv0jPQVdYargPc-zj94YQvNMlO6CNQUMxrTzgh2zMoBEHZS_q5ZJB-r-z8a55e9eryHztZ7K645pKslxFRJfS6gGuCMBjoQGYllr5i66oRxvTWuyUIc0l903wuHA3C_4DBXO4RTaQN0Fk5AsG6rEe8XAzFVvA-BUBd7y3jqOnxqtQkFIMuTFmBpJROxefzmcQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJuvXETpMdSqhPlo3-d_Q4kCNpeDkoQbzCYK_XlbkMcLCv5X6eiez13JSTpRb45SBQQcW_YKbulP9NBk-LTzCz2ToFtpJP_0BDjVC6rQvzDLnurJ6ZWlP61n5QkjXXn2NH4s7y4kAa6vHdIuNE5DuOt0MYKny0wyvBimeZW5EN_q5syXSbSMFUyyCuRZ9J7Q2F63cmOuWdzxhXMV6pLZWzxIS47UoQ74fLCCTNkDGLl6yN1NUgKCcF_rZeWQ4wDfE2IgGUeV5oa79ogD-Ulo89Y5g2bxm1v5F3MAXsChrIBseLHMnHc50KUm0eHvyppmwwwtRBIelx7qxYHn3b_Fsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biurtegw5ajJnTt9tHri2pnUhvKMFGCH_BZwIc3ElSeEe2W5cHEjip_98sYr7C6DSk6MBkZhNLOUMIC2e0FIq1AmS-GNX67LlXOgayE1ykBIkWaQ7IZ5JuBn-xAkOfpnHliWcmu7RWzvoxkHB3A0-YpS3OjOrfonRfhUVdXogO65IKexTyyrwEuH7uGXa6DI9y-x_ZCCN5nKgiCVFS_-Siu263q2J3g0RR-IDe7a5XXpA1YZtdN7xpRpdsije3ovZ3c7GqutulIcxcYD8JjN5o2Pzut-9p5CJ8TE5myznv1arEXVv6SOpB7pevBBb0WL-xMAlN4TtwiJO_VxEWys0w.jpg" alt="photo" loading="lazy"/></div>
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
