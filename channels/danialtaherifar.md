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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPM1b0rZZ8inoLPTSgi1RLWAkV2ZsMJwyYEqjreS-YGtXkDIOdwXOjI1TOGGWcCVI-9aauI6Ntyi6QFU3iXrTwQeZuaNoQa29YdlGH96Yqb0zG4bbCLK9cm7JbuslSx3YCclGEVe9nZk6ypoV1R-n0CXd9X-cAj84Pljx-vhVSchSI2PWGM5nsYvjCfASAOhRHFSCGy_vH9dPvM7jzHwsApKl_jasbhQPZdnpvfGjvMOA7EDbS3CdrUU1TEXmcq67TFff95KVEgnxL5C72QXO6W0i6IzVR4ddYN3um-VZVaBMcqKhkTKsjAnKLBxsvFTeOVh92mrhrE09hdo66G0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 233 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 471 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 599 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 599 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvTl0AqhkjB53bbBop9p_qoMZ5XH-FKlH9OrL0irDfQevCn6qAxP84D8lTPzcB8GIj5jre-tCnLRyo_xguzkbyP-r5rwDg3UFlrllPxUcXtKXYfZ0p9Ncx1xzjjYj9WeVYm6G4cIh0AIetga028hVacbW4UVM91-xDYBcSGhNJhNAoBfZbZS-uLuNymPPJ5WfSYivy06m5wbi9kRcwwXFhch1OcEZeLaA1sGJQ5JtmwSF_wCflWADZuB7xTu3Bp6OlHeDlRwFSYGhK7Ea-ynG9YJ0CInqmeh4RRerB_I5RM6Pg1Sd_WE4KsRIcuiClJbzoXZYgmSbChsTLSBYovTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPB2SX-uGp5sU1ZN5Zt7sEsBHXuomJyYjwXDP7cKlvVfZeaVJAww5xYBRCk_awC6jwaHg_z4aNicGVLAjDIAewfubbzaHSqcfn_VniFnGB4RWwnXti9xZOOyN6HLILaWSpch03qj5DdJEKgi1eGmeAF8D46fuq30FThg1JVV1VrFVQqSJ-c3DEkoOrvs578ZnYD7vg7Uz8rpTaXBPKbPN8bYrpgqbubrYdYHmFIo7EbQE1677l52qxb3ntknP1paXivkUbY__8wEuKLGa-MKAN39R5t09jChOeyiBVXDprILr7Cinw74TxlGUiGjgtTI5U0O-Au6X8TmZfUdnvqIHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtDuUt1mALK6kg7r9dOe3FjFsp1zYVNuSNqnhkS-qB3wenuPeYqTbNZZ7q5bKaYfFnA9AixvbsZrJOTsplq8Bw_M_kC9V0VbyBtYFLmOmvNNYpdHwj2WQNj79xUN_Ebttx2eqNjuU2x3drLyvcLKqKXPqlgjY7RJuzSA6zqcGJzHSHdlSJrSSvpxYTR_mlbNifhH2_GIq4i5AR-ADblTm2QEpfbP7jn6u5fg_q2kLkGVJ2_kagmwwuR1kgs1_bLN54061uue-WYZGHFIl1hgjGQAdn0wQMJrl0-XOVYKvGUaLDxVG2z0kErEfXdEV0VqFt-nC1LTwZS9L4jph9wAFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaC6KtvvmMmoWJSEFWFCM6vbzNHxL9vuF4iMTl33yENFrAJVzD20_1CwGAbcwE5i6OlS_Yk38g2oMK8q0BDzoNTUTqZnzAjzKC1Lw8OzbqRUpUePI8hRWfzm7-0IwkNxLfEYDYDWUJTEpAQZUgmWvn-XbL49uDndDUtkPrdyWauWIp7DTDbIt7hP9R2itXVhI2jS7O1g5ftAnDK1xlm-SM8I19yzC74K_Fu9D7FSM_7htaNOH1udSjDNwVlyUF111osLz47Z_Awpl3i0enkmTXxWLj8Jgw7pi3ZvYCTIGoSEGAy5I4njzcGENUxPwXfJy43uZ-a3A2CRhYkAb9MawA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syGDy-gg76mx5I5SBy5z4ujUJptpcQKPwGeTeHtE8r44NdFB5Pz9LOYrH8Fllf3mplmR91NE91p3qOm2xgT0CwfUwDccwpGdopAbGv23HrMDttT92smwj6K3MTR0CHEH9gMcXzW2Ii_b5eQWtJBZe3c6FlRZzhDlcG9K2z41NOAh8LM8MsTU_ROnH5sAfQm_YmHNysDJFYib6aK2AElWQ-pw0I7cWCkIhpOS6dKtMwjEGh6lT3w4mZ7IHFXkZ0npUIw9qNcOJp7ZGWLTrMIjZ3XLWufP3UIclmsWnRNeuhxgx-h8y4Gi7UD4q6wIFtywE5VG59WESLfLes25lbj3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBVqAXvxfZ1o5LK35dtNf6sPZGulcSF6-eKKzRAVqWkd27xhLSOjNOP6-fIXVyWpRkar1mXagdjRI10S3N6uBtuaTApv7yFNxEVqAAVAJyUOfTP7uvxJ92LjV7PiaQNRJQptI5ATrS_ZKSEb2JqNpYKc3G0vLDjPBC0qFsOb_7XVHG3j1FJBc26MvJQUvpCUFO1A64ShpcMs37KY-1paR-KH2Z3t5hmXkRh1PfTfooWu39h2QpJ1cVdzWeS28hs1jz938UbsXjXp8hYlw_DDcRboSuTlcxGuYumT417F1M-Su4uAjBcw7NQiDqNPzBk7UmjYI5inAtwjwlnWU3J-6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCAoh8g9o2V1sNiuHT1c7Gzg6_U3amjRiI-xGZpOvwmisp8-DG6SEQgVJYp78Wl2a8mInVR0iAYEBrcw_2K-CpVp8BKxAr_5o6XQajMoAoW97VWxz7vh192JXeN0rSXsoFiEO9CmkWYsEPB4pgHr4ur8BPfswEwgkBqy1D_nC1grpWlPmPkI1IUlMtzTnEkctfQaN9AN9r3JfYu34S75gJfSOdwMOvdDVBLx78hWQGr5h2lN4wQp87dNzmGWSBV0cESjZ1vMuj-gEYp2RLKrPKxt_yMvghdl6nJWc-V3BplHIxUNwmP-yNE-6ACkAlqRI_1gEMQptCO_tN02z8QeyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvgWJDcLnq9XxLaPahzTlX2I5O7mWCJSUD-JJtIbesu6gIc0F3-ijfYneXauxv8AfX9Yt937uN1Yr1a7LdaybJvs5ImbUndtdEgbmsHvF4wMUksBTBvPfdru4un4i2AfOCvDZZtaDTUXZjgg9qrXdE8Nj7xeQ1MQ3q_sZwfapxrcu_RXMv8NMn8ilJKt9uo6KA-2e5ej8tSqeiNom7z-DOdyXhK4w6kdEDbwJKuvz9SDdr9CzVAxLs8ad6mkXJ34LnEZxtPQ7AOK3_AT1tZh140VcYABfGp8j4lJd_dtY5B_r5fCvZqAeW94ok5E6uAKBYSEvlPkF4saHYWWCW2zDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFI1WG0mz71O4OPRLdAK7dFvp6H04bjuZniIbXvDA8VUXa4y_nDFE3FK4IUWcmyzZQvDWPfC36ov_f3rgeFCKyl0o4V-DekscPxaZVrccSa0-OkETIHtDu6c_455vARgd6FZr6wtHGusWsxMG0j6mM_r3yvH9xP0psBIcvXfQaR5o2geg5tAALUOzk3Z-v5GdOvVOgdtSaBBPB9iZVEC-3q6SVWF1cv2-HnAYlRiDyB4nHEiHnGJf3rKixNjegoS_x4y6EqbMwuvSd7dr0zs4mc-9xPUQQe82-EfzpJGa2bDIjVfsASiE8kr2OY4igH4CZewzfotn2WV6RAABfeWmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs7HUIbQgogtE79Gyhgt8rMSrQlUllpIOUKIE4TRqBBqqGueDeASos8o7HkepqBSrU-kH7qjUxCML9ue9n8ULzy4RNdVnO_rzsDK1WpcpFkdYXlyXGlvy9irRhnfuXju5Sf67dwVZEnC7cKV-drrnMurbcJKyhd16LmILgk46riMfB2Xs1AnI0QpmRL4x67kEHz48g9OCfK4ZBHmU0qP9qPquzi0rwDRXzgemmzWzkA6BaUaqH1-NXtU1z3A5kRY1AnZMWRG3GooYVRNk1ta0EQMlUuiU7hqNXWgiPvYkolCwTlgIXhCdTYLSsAfYQXK2IOVdqP0oyTTZ7MCzMWO1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nrl0Zb6r_7f0Bu8uIxaFZrYJVIczSrHDNtZUZq1KblMAfPi1qOGd0uV8BR2LfTWT5IjaACBypZyR6XpsiGW6ip4LMnjUVSGY4bAqDt-QvABBJ2CHhxIVmPZ2LNrAKBfWhIYziv0WvjlSB1sg186cUFn8TlbkRGOw7kVpnWp_7SYfCvtfDzTOEJhxVXNcNssALXZ-9uO1CKC3LxSXTtrH-Ri3VosCJV0O5V2CkVSRM8eYNfTF5Z5fmZxC0RCvHHWBsvqHEgYHWoPNXIDFkGFov1afTTW8fbXwekqjJsdeg6D2ln8T45idCgySARNVXsoWktk4UCw26IZYSK8q_MisPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di0f_pn4P9FASwMDC2l_bWAOjCj79J_ynUR33iKIRVVxldCAZsdob9YopVEidVjmDBDyP46llhIHikOnlG0QMYNXjrNkSRSYaZwfVMi8xaFmQgyKZ9msEvXPE9BxI1KLSZWDI7UEnKhMvf1L3l1rTW8PZBaCP2IsbE4QI2kVrMZdRR3bdWXMHhrCakq0a2Ig2CBw8u69nfKu2j6ieXk5B6WJqH7OBQsBtUHJdPsBB9jDeFNirbggWu9ADsREIgZnGQTRf8EoCNvcgzUeAujgL-N7PfpGgwdViCxqVwoh-oGHG1RZmKuM-QousVDHt1kX_hShsOruXnA0LQeg0glUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY9w7_eyZPgmbbnJl7XOZtLknetqoIQiiYRKiLdFmd25scLd5xuz8lHgjefQ0MdG0oNbRFA2j93kjW2CtPp8sTxFemB68xNlVRIQT5GLhqrJAr6mY0UtnSwrRGHzQybiwhaejsJVSaTF6UTs3qVdn5mmFIdBJsZwtH3-iQ9ZNWZ4-H16HGbXvgWA1S6belpanYjHqm7G1sWWCFV3RvC4Sa2MvJ-hiAV-Mj1AshyGkRN5EGMzGJT_iso4nhZUO81faaPTGhyOnRmeJDENG4Z7PTLerNKWiWDE6icUW64SZQwAKGAJOWzsQ2eg7pzOnj6moVlG208zNx94Q0HCrr_HGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwdAFSEwsfvcmkpxYQql0_rtWe5UvPgmXF6U7KGOR5N0AX0ANiarxhar1pxLzsF9Ps60eb2-gIWFffxreiCh_w3eTS44wvSoCzjT9blGavxv-p_D5h7BbH2zdoldJ89g4nSZTE10APlG6ImQiKpk7UeOCsLSyZkeavDfbua5QkdyUm-OQ46cUXf8lW_PjYVJB5te6WpkAtei5WmF1YSjmr9AVK5YRNMdcEfp5o-VErnmLS4G3-D77H4ay9I27-b1egLArBSTPKTDPUCEtFY2yoACtvIMpIWwPLIaPzxDyOAE-3jIv_LicCYSEwNsAAgWQEoEQgVtoA4CS_CkBx3UaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDA7bejaxHJ15dQ5QVxmQqO-cpwEACMLibVE1Q8gw2s57PUgEn9eczS08mykuWEW4-6NseR9FJ7uayHOC5empf4qrVu6ro_MTjeVf4FU3a8mGZDpENUf5NA1tcKAZ8xjzCtZmofVp0qPVyVAdE5yZjbIBaxVxjroKLSEV1JPVu8qopnqL51PASRE-G0VOxZDlGob7tntUiBTQ1waA2UiMW8YlLU4CuSxfHfewReIv1R9D8vJ01S9RgZT0H6Vt4t720D4nD03StxfDlZsoRbZSIdeLv-DUhquQAlMv3FpZP2IMVH73qL0LLy-vf9cfxyVJuyJ-7RjNW6JnCbpKHuodw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tlQiknZD4jPvpGK4btSP1BccoS4xVxhWgY5gv4jZgUZi1q7B3xqe5v1tcdHqH97I7pTgAOGbbNavN-Hs0YfZGprpOzHOMXeCtHj1qxlJSdNVzOm3vs2yLUKlceK8lYDGIOtxrN26B2VbHBf8EQVNxSOBhCbd7Qm_u9ka_YACAHyogI6mqWTIRscHh0VizV9NMReofSJfpuaDP5Hq456ZlGrZNua1C-AqbiLvG8zDVc7stNpcVJAC1mMwIDg7rukAnaGlbYTqDZNYjLRGBGIh5z7WSJp7b4IA8u_xySY_yzJWIgPm_SY99ESV5-UjNquqg7lbk1iHv_7vQGaL8QGgMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tlQiknZD4jPvpGK4btSP1BccoS4xVxhWgY5gv4jZgUZi1q7B3xqe5v1tcdHqH97I7pTgAOGbbNavN-Hs0YfZGprpOzHOMXeCtHj1qxlJSdNVzOm3vs2yLUKlceK8lYDGIOtxrN26B2VbHBf8EQVNxSOBhCbd7Qm_u9ka_YACAHyogI6mqWTIRscHh0VizV9NMReofSJfpuaDP5Hq456ZlGrZNua1C-AqbiLvG8zDVc7stNpcVJAC1mMwIDg7rukAnaGlbYTqDZNYjLRGBGIh5z7WSJp7b4IA8u_xySY_yzJWIgPm_SY99ESV5-UjNquqg7lbk1iHv_7vQGaL8QGgMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSGppOVVyoKTpxj7-MvMNaFSWBWjUCUL5UoEHHA2HTzeRBEP7qrh91pyvRdrp24dHo2ColEYN2byGHLtfEHJdX9FYdMmJfdDafVW5Qc2hS77tTu1MQ57y8PzS7iZLErGYnYBeJJsYVIM-etrHWEVCaMfrU1oYZRqDABV8xvxH-Flux3ZLAmiZCxzBnn4kuBJePfdMJPLtXp2brQDqkB6-d9iOJFexpwoql5XyF1W_73m1BlZqRqGH77qjholInDfSXzFmecxmFwhW5dPfLJ_KSmWODSEV8zRivFbxF6Z7cp382xOga6tNXWyojEuRTjNnYGY1P3knDeSiuRUPrV3DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2ShdsUVsPBy0zFRxt-Bb4_QLabutmeSjpOYArKEB5hN9-2kQ5H5H_Eg2T7PC5x6ZspsLCaow1vWVeo_mcjHhYqkvWinE1VKOJt-ftFLSNH4Gn4-ZwFqdfwelukCHrnz83eDun4pXIxYOnexUqWQpmL9FmwbdyDMIDzTOKfCoIS2d16nANj8iFqxKkymtiQEW_xoQTry2yAGVdb8es4uhNXBcSf3Tz9uFGK-lAcM7dyKUgRsFUqX408-A2MVQKsPb36V4qqH1L7AlWpG_Y1lvsB98gSDArMqmNTKH62ajjV6fpvfc5pXEB-SLoo-AUjM4HX0msyQizVxdfNMP8xxPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dd5tNl6y1f7v1l3tod2NCEz3zFptvLDQDYhDfTjkgUEepF0dzI4tbHNtoks-q9PNKfnJwSrHGyfIah0m81moEwD7e2CZ7XK733g5RgAbNZX5TZD-txkt4nTCzUR4FeRqTLuagHl5F0sNXAcz7ekc1ag4vtg4ial4x58EoljaMDAOBVTQ9hBm1Z8gZ_2spuA3PFFkDTsaS26crfB_z57M1YoaCXXfidrxLIJqCuYO7NcM8t6w0vZO7wvqvj5Fjh1xVJRlFUsAH9IRK-ZtUk8myEisqlRkygwwIhnidkSyY5K5komBBejRdCGvnxw-LCkp3vhH0wtsAOmstLXuFTUeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfxQrJ-Ih-Xlq8lIIZwVRNQrL-COT1c-bv7SkKRyaqCQAg70XN-6Swh422nincLfFOjlhTlFVVWe8Yf34KyDYEc_IjWv89p-kTWUemHRjIOD0goFzNCxa7F68pg6Xzz3uyABiC6LScp_Z-iZDRk9Y10wMUpPcvhUKBjT2BzNrrx3_lRQipUPEi_Vf1UI0hFgjOz6sXVJ-wTg-eVseBF6H5pdCQxq_DVocVSEbUtrrvck83wRVig8a8GzrMZVNQoROUgprUbOGnw1XSswE0p5no-xGfAUkQILuF_mK2wNaHR40JDwxjJF9G6gpWqIwaMK4NS8xFvnuWwCmg8K-NsnnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMs3obsHdX16ARd4b3rRkrdRWt7hrbvMnBaOFa5-BjtIoDTewuVaTRCZMg0Xuczcr5yecWCNsBFP23VbS2dpBeAIkCMLW_pyRrIeACeX_JAxnJwIIR2TIN9o6Nz1ZCPWzzNNn4fjHyzhh9Ex3oSK5Bz_OzeeThlhKTUQp5AMpgfoi6dDwwZSMwLLbgMDaJ46jlJ86VrmjCPLnQ9x8kANkksUhVUHuXKRrvy2vuLOJ7xsTNhtijjQyjiDB5guje7kS1xD7uR-afNvgc2UYApo0fnQlU3UxpjgOJBKbytECK_eONAkCCTEka5CAlt1DJboKBwejgURjH6fWGr6Jf5dbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0AOWiQNss8bmf4uh7fZHeSGh7JYGrUB4y9BJ0GoMEASlwalK0L3oYkDXjLv6oaAkwqqk_qjKwoGfptqkpE5du140jtj2Z820IsD7vwSiO7-tNcfn9tY_1D61loVFRF9qnvp_jwZrF8Uwc802I7bdub4KPX3qaQDMlDfG3HkK9MBXur62JEpw7e1wsUwiOimlyC_2FwPnblwIcNgZ1OuF0u4Ed8L5Jh7sf4QWwcoldZW1WRdRDG8eGoBgvungbtoZTTSTPRZtgy2LoC305uByzwJSWG13Ppv4sI6BAwynEVsxe3l_JthoXSFK2hihKrDeEScDsPrkJ2fvj53qER9kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzjBfjSw5RVN2xbGrha0ydtbMUhutSvs7R57hpMD10aKW44RIhNKd67p-wYyAOlu1i_dfBjNxMATro_qFNH07lsxHdL_DqeC3Qs04_uqhNurh3p8Obq1r74C66aki-14VqblwYvVbDEHRLisxmSvbHmJRD8_r5ru3OEG3k0J85-URoX0F9V7pryLdkoCPHM1pbHwDEIeemz_JsTy-Rsy-6n0v2n5BjndJQ5iXtgGJXB4T6XEwLPeEySOIjqxSADK6VkTkKP16KSXFIRNi1BoErIuHboJcfm-YMVswKMqY8_qoERugvmsUlHK5khbUKxAmjT5xNFdG2Xrmt_q_aP4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkPwQMzjNXbyjtvUNAM-7rog4IEFKIvsvfccBie3DDDEH1-xr8K1EDYVxd_m8omnMZBSZ18BfXsLaVxhkWkqRbkD99e4WhnVJWmcv67KG4t4BLPp-FSMITCVIPuU4aKlwJmAy1XAgAnWtfcmWhfl1DtFpMKEc2Ow9FrZFpYBk4FWHipuVBnl8CvWvC98jk9d7_7ow_MCExUpNgSWig9p42iHgHS7VO3Sxy8ZsktcH-JEkjpsqcSyDV9PvQusk0ZkxDU8czb8BX4GhMlFwhCZMAtsxFWlbzP2X1Ur9VcPSr1Zd-PVwvEllPCw5f98vtLzOUD4tvvlFNt3RvkDRkz6gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHAJe30xJpeEp6-RJFzSVar4qGSmfMgWIqOHx_1-eqKH7Lg_lwZ2yXlhf5IFL24Ci0IugJKhHyACbhNhG6Y0h5Hf0fN6DTz7-9PHCaFmvnthvLvyJhhxVM-ztq7sFWYcOIwmWUKK65oIW7F7UjsSH5WhYzLJykEPplw7EW3KXjUda5Qg1q86JaHQ9NzqrOhT38AoHlu6uTaGT10zQExJswhSyBFKbSXyO2ENDpLGFab6fQusgZCMZ2uMYrEm7xwU0wPH0o3u-FlMAYWBeJYYwHz5rq8SV1tLVkZRRWLq3f33nrQTkcZg6htutyxc8L5tCJal00hlVNPlPw-aX0mN5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2q3tzt6v8VODMF2T7WQEEdiL99_eefyF4dRI8zd2GAKnY_qgJhdqljXx7qIlESqS_b52gz1Lco8reh1G_kexDkcwmTL4GZILAre6y2MfzuvKp6h2NmuhiUMlO3NseBzpzIbVvjh6ICfyLAJ6xLk8aBctEswFbUjtcIOI2xAbD5KK0__B7CzxBeSXpjOONemRy6MxS-cNK6zrEwvHfS-c1dEN-XlfeOHZDEZUo8XJaNWs9havUBpNE8IwDdUUWD84l0T8Rr3XJeedJUYKqAENWkfCwDG6x_LhkdbS86iZpZbINhF5cPnCaI4o8X7f67zdKmD1Ssu5Yx7IZ53xXTFzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1PbtRP_rpYucQb8BYOpXXPTKdl-7ZCj-COHJFoX0pVwBCF7TMsyZz6FBeJ2lJeCuL9SLAcM-ZZ6gTQM3Ph42rWO2KxhICp4OF9GeidjE60l9-Fdtx-HupAKbHk1Mn9oJ5-fSqCaVdi7BAn2fPZNd55s6tZ-wnebMFtCrYwIhvZCgWub7wi4w3gZxeDpY8UmsrLBSzpyWd5R_RKbTFGrJkFbl9yPv0Dp30lXmiXyz4Qvd-ZdZJTn88dF-w99zx2B5H1NQMOmcAXy3wUIqr3PRgz2KP8_CT-ATl01TlTwNx6cZirJWnVasC40ujiFrOfX052OlgydjQ8qcwbCdym-yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2KNTdnKnJs-yPrZCUczVUB6kFQ96E7eK8c2jBOwgvbzBhj_h4-s0J8Y7CerOY8et5x3pdUp8ipLIggGqHLP4khY816TXFdcQ_WDskl6VMF-m7rAs_pSQ6rhK14pqup3QP__QCFQOvDPuz3ZitfKG6b6nCA-6T8AbNEYQIA-vFZ8hFM1JBv61wuIFeIxZSBL9nbGyUwW6hYEXuHyopBBNh-D-9gDKBVk4bmSSmBauZW3ttDyUpefrtjuiSBUwMX4DyUKapIwEYZE4xUkQgDDAUYbBXUBwWwwFkEg91aI1TkEn5pjPxJMdyqSjSnWFRXWQcLqrvu27GL1efnE0mMsog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbhvvIC1qxjTe2qHI_feAd6zSYEHNLaBprCUsFIVDyCIJTo5sNE_dvusiDfs5aqcPTHktTXdOVmNkm3jk0gdywAe3Gm5hrDQsY2zM62leY0jF4TnoLt-wWRVRplx4w-_yr_F-qJZXEg1uieMUY2vukJpzhB_b4w_6cX4QqA8bQrruDyLQ1KHdrpuqjQepeFYewLN5gZZBIxRNZUgJxoc-bVf58p_qAH_AtzYVXsYr8UFNF_M_0GyF_xnT5ivAXlwEoRYw_AC8zRsAARZ1nnQ89g7FyPap5zsznvQcnQk9OwAVBpMApUdFZf2dqGV3MZNvG1XFktOwxaoiG4gL-UXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaiQ0Re4OpLwNDkhGf6cNVtyGcXfXZ-aoszMyQIpgNAzGkAo3HKwxN-PN8mqzDVjxILGco4RhTlr4wyh1P37hbzdPSmdNP6Y3092Smexl2oktXJKjZqSyUV96pPvKRJz5PGiTaX3Iae9TXKrIWP75GTXR5XjtjTkvy5DiVCD0XFhKtB3D_flp1eKf0qSeXgg2QU19Hv_h27AF0O2waSBFYmcwjV2FKt_GWcYf9NyYypvFZ9sqwAD5JZC8QlMsf8dEW9rUe8a8DpQ1vleW6rWIAkMvYEay1jdOTpil4y2vsCZTtso-LiHPfa1fDhkxKOjsR22opUR6jfV5AQwjaObsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgfQbznRL4W1E09akBCIfyu13Cb5AkhNGVuL487ocJ5MNAqKdduJ3HNqW93PllUJnKwjLHvYSzrO0Bs0rKBApYCoNQEg6kgczZm92tx_4LbUBf8kia_BB62mDW3rkN4fbCK1sXebZMnCfByiV8Vh6bri0wHMH1jBCIxTyxSQitLgOKE-R9fYfAqss_D1m5MYvFyQRWKeweZqrBg4RBBURHx9Whiu14hXR-KenushXGMqU5mSIfonQHxGYNfu4iqSpF3E6a7kutcQoAHH_5GmEnrQX3hEhXBKFV6kIeNvDzvAmdLYMCqRXtFDvobPow_KDHURIRMg92lHGbx5fNFf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBz_JFsovCMR0uD0rMLYrIC5XbkqHG65gQuR1_8RPpHXanFJ2Os4UshMiBSkfTII32ss1SsAAZi2a4R2nC4NSG_wTsWxnTm_z-_KJxWXczHXFIimtRXj47CQ-fyIPVJIlnDW4Iq7g7cnfUsdPd9tapJWAvjfgEKuHZXIq8TBgQE59r2ejuZP4up6ceexxEX6su8Gk7c9HaAYFWcsSayEDmIlvJN2BEgOickjxzRud6wi5h3oC-i5apDKiOIO2aFt7fgELxp7w8hGn8DNDffaLC_j4l3qozCnjtg78pIluefT-E6cQVzyh3Q3jSoxkWrtxa22jcjxZSkWx66bbObeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hT20-gbes1ERFV94AkPqEf3FU0VsGn6PsFfBne6XbvlDwhJNxYI5mQJsf1FXVphdx0xcvmPAaYVT5ZqC2OFpBSWbGTyLGk1P9xhDeu5aaFaDdLILq8y--QdJtNeOGGHyhETe8NyFFaa3ZEgvkSXkOnqV21OaAfFY6K7VqRArRdbDht1Jm6VjkjQQ5FbK2wLNC_dAgV7M4PvyNV_Li9YovkHIKv8TYxcWd8qyS-S6c-Ye_TpvfmzTmE670MKMWSacqq2YYWwxiuWFSUyYCCAzodSFwV9L0qm2E5fb2c1B8zee-lTU-36gFjOX8H5sRHmNq-u2MBxkyXMGRz_t6QB4Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVNPdQ-yHMTXPzk7zRQhOuDoG9Vbdd6JMq2cA4zgDJ2on47NjXazvIlFoCRi-0EY0aQy3OjycPkmYiXK8eUL91bvaFCkFhYjWJxyfYINWdPWf05yifWNuCj4gWK0TppxWG0UBn2-TGWDMaSuBwxMvIMjsSFSJqfgBEoxaUciDL0VGBG_eAl10zJYQC0RENIaQwFAlyqrpLZawobNo8QvFPxnsJK4JV0k0sT1umERFC_JmZlqxh8eJiyE3TgU-lQtx1WERF3UU0TgPjjN6DIaKp-TMoHLzJoUCvsTPqLxk_0f55Htc6YX5hKc0Ad3l1Vyvoi3G_gHVi00Odi0nIoKHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4Krb8uvOtq6997kUNt1Gy-TaZrGXmXn3ThTLs_WkcaZdY9K9w73IsyivANq2Drih-GhlI0GWAiRcs7Tsb7TL6IJ2HfB0hOtZWh54ndPuO2SPWA-M3ZWqCS1C_1bcTyCMw1z4R3v4QzzAWZy64xEEq731jBz9b_i8Ax0FaqJnFumukb7wL_ui5dTMNJulbaRLk6Z1AE5z-aCsNPoy4Nphmoq-WkidB26vW5CiJsWUvXX58EMFEBCOlnGYOgNawlp4iiTKG1RyNZ9zMOUroLqmJZzzNCjreorhWxlem1CPTiC6BT782-S_9q1ycnQugjNbscn4Xp3DD59WBbziobXNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWRRN252ND9cAPalJGxmMhW02CvHghBGznTRH1BxBZIA7BSPgPwQVU8Dgvg59lhpePJV9tVigW_FX7IHw2ZvXohc15cDjVP3Y7i7ayI8WwQQ51sbiap6WvLFjwN-hUQ5br7i2cG71oVE9wFBNcL_1qNgjxP_R3AwH_d39-qLSVV32SdIf5WJ9NwmS1ctVJIoPpGB4mJH0CZQtE4GRsBV24hMgwI7TdMjmcO--J7Io2LyYCbLEOjGeqZVr5SYCJhevIv5nKex0h8xOU05tonhNSa1a8G6NxSRVUu_y0kcVGNWLuBaaRUr4RZe6AswOcsgXuhbTy6ULRsZFgWa-FSQdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1zJdFIa48_7meu9RIvZlKjulRqOdje_8HB8Oo1S2-mw3qouLePA1I3oyTTjPiHwzQemDKvIK-IOT4qs4vKDNHBeZSbFr05QrAy1TotUTEezlgNTZtj-qL3sBU6D0Q3NSEihXzAlh3eTE2oUZT9Bo7gqnu0ssBSCSQoVwKnCLMl-vss6P5AIdAB6ua4q1rC8U-9gy10QvBEIAdltE7u3xYPn-ZevU3QVuPRKPO_7mq7Kx4qlVzUP4gR2QVFf7Lq6YZ-KvX8d2EUMoMTnCXTsnYzilYm7NwCh4FDUi1BtdxrXhMBPSuYDhLVPvEQwjcPAlzg-6tstJj-MQsvbrEu7uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoGeSK05J2zf5DqlPZC3IM02Ytohk2U7cGvkRpG_i1xs_0FuMQqCuMptGRD1eBD2ruHsPeRGBzojGxcxJm1DIc9_0JltLFopyERN2H4c-gWM7HFmU15FyMv5bi0R2tENSmi9gi-AW2J_u27HZkq8U4yFvt-6mISCKW5C-IMhKFFLUfwcunUgLcOC8L105p4NT_Yc0fNKpJzX1vEWDO1MjCs2v3MUlENxpMhfbv2_pwGgeq3vOX49ZF98-uL3N9bE8Vrqsb5FcBOwqyI1vgdPjDRuyk8YKLxRFsoiNDLF1VEUwycwI7SeLbdvjs-57jiFwwdt1zK3rReEXjzIwykqEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJlOCSSXEs2hWedWuxGlH3y0MHOgYiMY7Rym31JJH492xeTa4q4yvKLd7IZQ-wmOCrkvynQatVCS_q6LhTs3SSGkOSOYEJ4L1eURFFMah88uOT4mmHuKZCvjtKAjvjEO3YcVTjHxgYX1fibXSnNBW9sW6ez2L_mBq0GzHmxl1lMoTpjbBjJiWQPHhfHbdaz61x2GfUp-nxaEaerW8lS6m0tlDOjny3sHACUq0UjT1rMbMz56uSmRbE_R6Ul4uXK4yxkH6cdc3K5FJeh6BxbtMWdICdSTonfwFTNkfuasElyjCBqlYwp_OYd3JRdHmIYfJ7pshGOqKdJlB5YWk8GTnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZJgye4IYBXMVywUvwr71h6pF_5_KmzRioEYu49C5Hernlqzs_RPqu9yo8d2gNqau0F0SURjR7oZdaS7KBl9YPkw1bZ6Zu_g4JYY4PrizzC_j-pA93b5iAe_DZz66Sv2e4gjbnK7LGExGGEHf3tkC--gAMEGtOvvehEm8eqghnBiJ-_eWp7x_w816h47WE_Us25HB6hkfkgK5hSu3ahNk6wxLGbBwJJtggyEFJFlxb7eXUxacs8pzfuE_vaf8q-db8CIxbjlBclf-dLin2lWQ_BmRXUWx1k77SXAvOLgUYI8h9U77BDsc9QrQ5jifxc1DZfH-sf4JUS0bVIBS9rBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFH3lcpBd7aWHY3UWpXoqQxnLC2hrZE9pMBqTyhalBR98UPkJdSi9t41e0riUBa3SSCi_Zhm79IvbXPy_yWDVR1CvXeBGGXWDGN0FhejRRbeIzS5DVbiHIgdIPWGLyM-4MI5H-6azgHgGGDLn8fYtyM9BptHZOOlOE6Afa19_F2-HOpCL7Z6gFdcBp3YEsVsn9v-37huc-Wr7sFRC_Flo4Kp46wEWnC9yUPwGPi9FUxCnXvx7rKrgdLUDLhtyAc3BsPI75eYdYXacxQABTcA-IS5W0QqPfPR_cLwkPOBYWXE5G7XIADGqkXvYO2jmQm46ja3qn_MXvWZdCu407OymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogBOLxgiw2dZzuPgrRyu3oc-BEHhUsGw1UcjnPzL9eVEHnvbTMT3MDsriVwv8kx9_GAoFVWGo197cZWped6HNvFRYVRTp8Lk_klpstoGod1qkWSTE_C5QGGjZw5_5F5nIeGVEdHThZwxwVDkn6m9H3MNHVZXqifnzolnJkn3ZFDryez5DHZqGoQk-v_ngIrpPWLQ_nNd-B-Ti1FTgwbGMEW5qWjgc0juLbzJ86-xIFBbeYFlGy2dueFSMY8ctT-MnhocRM_w7wcoEl_JDc5n8uEbdtcTqFdaXROsfqEH5XoBjlHvkLHkjUcHyzlRCmTQC-d7L-p3vqoAoGycHaAzOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNryIeIIO4hZXtExd4ShYIUwpcU0kA0wksg6Gtz6JB_3pBp8rPQvs4OMm2spZy_lLwODHXSeNiRefMNiUuoz68G80jsChKi1QIg5BkCh6JUopMJKW7jmzusC1Ytfq1kIX2evs5_UWE0eBaNK9YH-uu1xONuuEA79OzbQ6d3Muj-Cnl5uE64zQoInIxa6dCNGV_trJ71zuSpJVU_CtyTXuWXv20qjHZ54ttN_L6FrynMGHvYbzRqq58B7-Y1b0U8aFTfEeIk1HzdIFDth2miu-LX3cdPlDwTcj20gx6ADPZIKGuDD7M7cjWFBTL6QWjXeqCHBbaHu1hIe2068UY17GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to-Bv_TF0PAapneEScWd3xQfgu5cIbalEASczWaY_vwD6xPNm75SFzxVjJRQ_xD4tNof0E3hUSrD2LDc5kFIM82hKQREuTpVmX9IKXzqYHCH8Jd9ZRBro-FZ8XbV1zUr5Mjl1QWqVGwmPb4fvrGiHrnQpzkPl21kZ9kKZSnT9G9h34FFuLTkTXF40AUaYPV0PHGPyZlfbkAjNgjUXj48u_4WLun3Nv2l4T0PzQaMfTuVi8-WKR1f1I44vrO4y2BXqI7DSsUvoK-eg7KlLqzsoGSmzbcgcm1Jsu0y6TTHMR9u8mPAQxUR2ESre7mYe5is5ve5ZNx9hrdyQRlwPVF3eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNHHbAMZD22FJYevKiA2bGxsgg0nYvG1JvtDpQKObPndabmT57Ex0SsvU6pvMreC0BuvXgsavayUjxLf8hGvh08BmagDwcr6qWn1jFjRC2KrnEHxLShu6-CiqRGl-GhPf1oYXQrFY-rsl1zP3bazpAo3vn6tsIVswkf2uOzXy94eHPeGJlRUXskAqgLYjctWaBEyaizJlew52U8I9U4ROmdTATifJ5uxLCBIkvn9soL2riPOCN4s-n5sROcwLSUH80dolIQ7NXrHcR1yjL1Oe664xg1cW3YurQMQt3wqeLS12CLCB-u0k_YitytzoWbpe49KgUkY4rmG-xCxqlA0zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFy88J1mzxlaj6QpPM9biu0jJnRzmB36uYxoTXfNmejTyyQXbuXqZ7p_9SFmpAm5TV7MoXqTy7iu7UY5gOePbIOXUH5_uDTp0TmlbvqBMKS540DrYbE4akHYHorgRzn0PwjtfLUantF36EoeoViIx7okW_fHGP8L4fUyrLr9edcSNFvreHx3CtMAkkEAVwK6bG16I53DOxVeXb5su7KNxy0SN4b2I5R6djLcQ36_HBURv3yw4akkeOzLCZB2IUA14zAM-znYz8wXLvhZRerDQ2WkO8Cg2yG2hiQ-_YNUpKMnswblTOzgbg7oZkTKV-9rEqCfGqXFJWoozc2d4w3P5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-1fQ5cxpJSEGVZNknZ0DFACmFz8SVUZWWA6dfsUApYbgkhbbCxRy3aQ0rGfJ2mQ_TLcMZ0m_a8ZmYFJXEElQHzasG3_0fjy9z1fC37cxbPJK-FhIiLA-sDceBgPBNSQ_OPYyri1_VfvzD0Mqth_s8BgqwJU2vQ_FWvQf6KDy_0lfdmPyXnrLzKu31x-Ht80Cjjf-Vnx0bKmNnqylwW90l0gIO2ha9nCvDh-BeuZTvrIC-IAMR4nCOQ6494LoIYqzKfEsmV0_D_iufXke1vbYv88EgggaRdRjwCby-0h5ulKfmEsbJHs8U622JR_dpVg0kFd22_cDJ5BnR9dP9KFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DboffJ7cvtS2N2bD88OhlOYW-7Uu22bI6Aw73VUHn7_Vy1lm1iGoxRtKbcnYKdojRG1VDUPPn5OfYElYvA6VUghdG9JrK37CkZAWSHDsTwCE9jXKj3Q5WMkXHSm17cyO8MznuJyY_g0GkCr0p2RhYariA0Jmh0QkCWs8Ws_NqzrXaI0ELiPwvq0r0Z7w2eg6BQJ4P1RE5jXW-uF4fPqz8pJ5MOexfFda9a4Ieqkx9mEUOS0QhJ7uM6KrpyzvrTDAvUxxWIFb-Zx4aPhBEcz_D9DkZ5z0TWxsfsa7whud5e3n6ojeSwUbcVubNZwvxyxlH1iWffBRQ0-Hskz0WxSo0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mx_wAIs4CSIeoTQ3XW1IXa3YEpQQcBaFYKCuERoFcqWcd9TZ287zqfPUBzca_SmSfVfLtG_WqHCksgl_zwV18RLS2QvAx5qeecpNgvIxSK0eAN4o4KkB5WOkj-Jl2IRkAuD-Fm9EOdj6ieXa2dYCNZwWZ80a9UQNP6tAuDJx9pAVEP39OgHpqE_Ol5wXUW3zWBsUoFW-uS4aN6li5-rknroyNfidWov1fr3riunKxHGnZJKQUQdyzNbLN_50L2jOUXiic51iu_3IxwtSCGpNr5KB9uSIpaoEybzBI6aces9itSer6Al5NA52Mw1ULxdDAThSccNHe-EYg0_L0j9XHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzIoH7Geof4D0I_HUkJSNaKHuqUHoZZhDT9Di5DpFxOQHY_M0ndDrSrTMHHwUV1bTjGC8hBJPp1p6vKKdc3DxAt-mdRHjppehwrp8PuatDcvU3TNNZGQG7RQOKAPVxtocCd-0KSXX2IYmk0h6f0MakMbrxzAkXJMXmxFHKhMtijP90GvVkkrxHt68TGoYXZj_dMK0P34bfUvSPD1KyKSLPORXxwZnXUxJsJn6-ldCsF3VonGlQZY-4GurzKJMme6Hly07kYr7zfueoJAjg3AUHDk7lU-Apkv2jey1YuVikv_aY3YsvwhTfuFcZ0xXbOiHSWs0KkIfvddfKQtPaC50Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg288eIFd60DvGlLzbEEvqZOgDwlwStwDqrHKlZ1CecpoYvWjDtn3ZXiLCEkRGHoadKBTNsYE6JknpV17Dtq-1zaIdU1dffwOk-UCey3rk2_A51JNpryFswhAtXaIXpptof9le8-L4bNWGGdxSP9Z3CdvPvNoKgfo9GqebiqKi2I00QKKI9cEdJapogdI3JXRUgi7RbB_I0wVslruosso6hB6VPh66mOD_tMqLlvyzGEwAKkEyPrvUOZ0pulxOMlz7g9GiYi9a7u0eNup0P40Q18AycQGY1ifaojFYnJlZ1ry8EBzdkDmNrzJH6woffWbr6uSn2Mt7rGilggFJkJgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox-iy8jG8W0nTqTdLnFkDY1VMVPUbH5nh7hHXJHrcIjxxOM2M9m_py0E_6SOIO2nYKutTKOQ9xHIP_fo5sGGZBna9lvlJLTTP9U2xivIq2yBDLMk9PWLAaPcfSX6Nt9RYYmyuEQMrue6waahoJPQhAaFCiSPsqziTKQorYOKOpXux1uOwJ8kCh2P3Vgh5PE4Qx-cM0m2PTo_13nBO-yl5HjPp6abpkDKqzzWWNl5ISu-CqaU73_Hk7PYmx1R01nj92Jan_iuvmGOiYwjlFqOyFVWUybyI3sZs7aF1d7a3hykPxhppEeFIMfA4WVLdKgg0Nach_nL1wK6LTEF3KMhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdljlvXboLIw2wvffGQMJuqXrbes1RNPst-maAqa8DriIjTVMv9pHxmmPkGUxxSHhnzZmsh7rN3p2Nkz_g3iHPamAYzNm_UzpTzcVxnwCx4TyCwoRsjzFIjqrRoQKXCdtROhgabNzR7A1AszwqffwIXmlDFlfCgcPl8wl5gu6fmF9Lx8ewf1ZvD1lybv4x91luA_nc_xdRXwKO6gdK-3Em18saEXwiJy3jfwVe4GrEJ0uJwXeF3OderEKIPu4tLR3X9gcOs_MnnJNALi_fdXRsvdoBqA2RDU3VYZlLZGtU6trFjqceuwwwxPR3tE6KWrZJytuf-HfrPq20-VGvtweA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT3gO7EjjN8WIoZpHCQqN8abb05ou4ChomdWz9bhm0XEYC4t8IZFcAQtXmftdL_zGyNoYL-xJLHMjTUV13WpHIhfV0V1dp4yOL3avUWH_GCk_b03gMKF09FwO4moNqR2noqsnIqDyVY6wk5K1UQsGfY5TYUfFHCwQD5S5UnLnaPjogAMI4omvS6FpxnppK3cCccNbsyc0nM0mLPr5WTpfP1D5kEp_yuNs5C0baEzKkQhPfAdCqRQEc4gJ6x0jIwQSuluQKvxjozJgsxvuiCh80Sr5hslpNQJiJ8Sf75kAac_NW-t8w4BcEVUvFKDLECyqvjCdeszBb1QgbX2z7QxkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvlTP2kPxubaE5dSF-5FTnZxwqmizNnmhPDI_UsaRyeQuvuj_8qFsDFpAU5nFn_qoIhMQvhbnkJCTQ34mZBs9xe0EfjPlOEC3C2doqk1ccpD7DRtEunv57izkBocEtLFnTFk5NFi3lDj02t9yyq_EsBOTARrCg-cDOF7AEPpzhDhabGdZcCdBumtMjvUTYE3MhVSTE6bXi8HFnWeXMdvi71WlGuvbaxZX9FvoVFiUkHyiLhbiWFi61lxknJu-Bp4TWxBK4t_d3z5YoJfyRM61JVeB1KhIym_Lvi8cg-I7oC3yVDAY3TFl71avJNPmdggZlbSbbsrOH-qBGx5wmlGAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAeXfHnM5fq5t0XA9iSitARt8TBRNb83CSoaXq0XpWk5G8hnKxcE_XXWXTw8m289T1QNw0ySm0ibGJmH3h4riA3zpNbuXH1TqSTB6l53LCaUjcc09SibAbKGQ6j6L6Buv7ZhIRr3CzDXshfp6pEzVF_paetGRUb7-1JiJMpH6CkhxtNp1jCFAyjmtHQnSS8VlBROQPoPdA6PJ8p60lpRRqmr7xq9Qp2BlhRLbJ2NurWC2_FTHDENC8rLmxcSaqPOxVC7ympXXc-QfZUdZ0hlCPV1oRE873_n2RvP3mDue05twVwnZEfoSSBNpvNYT1NpYDReflFwfKOpSq00jxR5GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeglS5jYT31_ctSFR6xykl8t86BgtA-5l9gnXI5ekR61U6RWl9qqS4DvM13KLlTv55BrWDVYT_Y9JI8VUAgWVIGV4jpnrFwKPYR1ITH5uZC7WBnTZ_PsMJe8Zfg1YpjLOBZ-gZTrDZOn5FOujZygUp0gYwNnTqBAZ3kPTgbD5rpBVQQcLP7NwFMug0nriJU7Y-ThKB1NNtt-M7twU-Z8gkuFTk2D-wVci29Fo1robc-FSCWIIG5i-X_axfuSwwGmh4662Sy9Tfm95gISsk8C3naT3pkf913uqPh-xOa_4DUZMAF0oF7358JGqO_AaYkjIULVlbCk1g9cHnp4D_OXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zn6PvbU-MfmSbcJMn3r7WyMJwE5U4r5n5JxadTxDvsIib5qRvO6u_3xHFIj5K613vzbaPn1fCxpQnd5VfvM7xOYRoOcao3YoCY3frHeoOuL0zKJx90l48J6U9-OxfukObmktnOv9XRCuUe2wk1-VIzeVqr6OxEmjPwIJJxPJExhyUsidrQWtsNf61V5fLZ7v5mRVkbpCNPLR5y_dLOIby4qWiWOZ7g5dsxmgo5edMKN6S3qWQAgavpEvt4v5UGVlifafDLEzeOtRxc2zV4T2x8lD5KO5HPqzEUIyPWRKE3ecPaI3NZjj3T7U17CfLcM1P62RGVive2Irunt-c4oUWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBNDBgQ_YtsVqfTVkQg-saS0GPnuNIci_h_afuIEHDgEvbTr_zV6Gf8jxfDfua5t6F_P9Nkt0ZILOMuFK0MfLqKWZwi7584VGS7OYQxCQH7qYbLDX7w3E5wXWFAOc7HWr6GuaqQdDmpZELL634FLNGEDdInu2oy5jgA5jMeEfSR4DUYpxtlvKCPf277SBV7R5ZGtsmzmTOfcv5gtuY-5LaXmDCAEb4Vl6Fs4dd7B4NTpGbRNMZPkDl28B7PlvgSlH2aERzDtIegXKc9jrxyOsTwy6pVz5wKDZk79yBhzw_8uYboXZx0wGLFLrp3URvpdXyBIm0s_55QhqHfO9vgj5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9URgzSkSEmpOxwTE_SKP_GszbtXdqTQ81JmKUD58rUzFt6tlBz7kg-ZOdrcNpjo35ul2RN9c0vrgNUAHWnBpyQIQaezb0hLRzp975j9WiZgRzsa7JcoFHMkUk-mkKJFjU1CLBDKME9_kC2KJRJbleX5VaiaI_VeJXFuRSAzPK7ltKwIkujz2W2mnjfIUuwQtK48XOVXuAW48QBBA4glR-_ap_gI5yrGpiJ41WSYuwhXOfOter-I8kteUH1prUCFPTA7VbWmLw-xusYo0enppJiLLEyJ1MeWPyLj5m-66eVCPQai3ua9Yo1YKY4bOl6uMIo2-JE3KhDdSS119hp5Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7N2Ggy3ADycmGp38Ghv7QIGu-jPaTrO7_v7s5x4UCFPgLov1mYfzP3LWzIuCawKpg2MysxEVZEhvsvNb4_pBQ3H8i2joRh0pSi26Hh6RZr53wAWS9DOkF0R3PwY9VZ0A3srDJrkjkm-R-XbpaESvwnRwwNzQOAN0zOMWeW3pYjxdWiXJ8NwcseORECyGrdC0xjC-72oNZeN60jPG3hHewI42Nfqfm-pRKuPegyE3uGH0t3wiyd8DVR-r8_Skd9XGVVfPJerBvuBLugPSFqXvKpH-KUPXpQVqHsQyucrXX93XggKA72siK8qrIxQlRcRGEUQ9VY8qLJLw9LlB5TLbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxkZHeBBzcPXISlKDwNRxxMMys2JHgH8Lykm1YtdtG8D1CViqcz18kiYyU0G_SuRswdTdC1AyZvnd08bAFM9ZPgQ9mlJCsHyPROfP-P77YSW_llBj4XTlfqAxZzxxfGlwuOczOde-FprvUtlBLPCvu0hKrskuuRZDGHAoMEIdKvKBppU4zuGVNTFzHc6skNaWRbZ92RHv0eq59bF0e76kPxOhXztsZcTV-iuHSGitXu8vCtFUt61xmBdjilO1Ww10SjHKLrUHoZO7r52bAOowLLWVLPLQURz_i27BRq67t-3wpKWgDh2QWxCgWEBM7ulqjYl3NuF3Ujqrt1NxVXc4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=SLR8F-uL_dVzhloDSsHqLuwxMu1ct6iz1jmsiDYDthsLqVUY2VLDR-kYvhTFNggUyfYSv5kwP3r5o7fzYHRe7LJ-YzYAvzlZm4cCmYy1asuKsk9_oGUy4kOzd8NB4BrieIaFTNTFdgk9JdNoDrIlLiTbMuoT8PA_2I1byB7FiP5FZ57qkQ3nGISvSDkeEqOSgU9xMJ7NGrX2l_LHoADPwS3oEDE0f7kGMyg2tEmOpZZVpB30S6Ir-PbCyRfRON7T2-E-ldMH5OKbhsxpuPLoxAawCcVDqEefdbJbu1-my59f_UGCwFfO2z3Zp_2X2uqq45tveGjGiLZimhVrp1ZXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=SLR8F-uL_dVzhloDSsHqLuwxMu1ct6iz1jmsiDYDthsLqVUY2VLDR-kYvhTFNggUyfYSv5kwP3r5o7fzYHRe7LJ-YzYAvzlZm4cCmYy1asuKsk9_oGUy4kOzd8NB4BrieIaFTNTFdgk9JdNoDrIlLiTbMuoT8PA_2I1byB7FiP5FZ57qkQ3nGISvSDkeEqOSgU9xMJ7NGrX2l_LHoADPwS3oEDE0f7kGMyg2tEmOpZZVpB30S6Ir-PbCyRfRON7T2-E-ldMH5OKbhsxpuPLoxAawCcVDqEefdbJbu1-my59f_UGCwFfO2z3Zp_2X2uqq45tveGjGiLZimhVrp1ZXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnbc_N17COCYDOZkqwxDRarrjV-3K2lk4_XMLCU8mg3x8Am7y6KlwRIKRt4sffjYFj7XlQa6WUijUCTOUPLT53isipcOBdTOXaaO-JedzOFD156t-gaAEzXaBTU4IY9a3ZlJTWLfhpzfAziIQ3ezqtq8C2mVJjl9A27jNwnZMuK9v9ZwKBnJvNsyO6tpdJCQUN8xb-9pEex6Zd_d-H8mSmVubIlDNceMHmA3nLXpAsZzlgpXzLh4ZxqDExQyR79vLbGG11vn5nxLXT3zscYaRlLtcPp18NegCX_35ufJ45LBX2GduGpyfjruOuJKbJRU2EwHHSLMGDO-mvlHcP12g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWmo18SnYTqyXNgv58hiWT7OAd0eJiakm0MeK56y0NQYELJJ0hLkkGp4N6jDDP0BGWyxAr_9F1RshxjYFpFx-Etst_dS0_k98uva8pE2RGgbxNE8dg_dRooBd-Uuf9KzEfvuKKjY5Pmlv79yk4kGZugk_hCBYOCW6G1t3c8RfEnM17LyOqIn5OBIsad_erGUCORjLdcP6rrOkhwaMou9wTclOCVUbjV5ILwTnCCVcOf1Ks-6q6PJOBlqgj8vxmuyIoAtufbuoCBHDuOV2cdRY4tkJMSUMtXmFEVFOkzV8H0729TixDjItDrSJkJk9pIS1bPHfTsTA06TdVonGWuU1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/By_E2a5cbHjftZxlpqJwGrXyzxTZ23MxpF3iNB_3w2GMGPzcA7G6BM1IxgSHNUFBthj6UwMgMdVvJ6Bm3fBK_Hw0-A8ORSacJl3BVfpVkwy9HKrgwTnxIdJqoMgtbN6vV5gZnuloG-u1okOTFUgiWBCCngrtbLltPOf7-AsWbAysIMHAUkLJRH-8scxX74OrWp5QzaQKO2eYag5mqu4f-wh49TE97qDfs4pyHdqjwHDcxzvpwLaVRH33dsehYqmMddXEfSFB-20PX5CKe59xykaTr3q9wzqCfx3-EBGUHoDyRuo7eURaBbmGG6Xdq4UV_atwJwC7y8Dt1l25_OJrFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF_HFgNC9e6pml1GZSZEZoioiJUmHFcWIjgHBS0eY6mR1BQa9syFOXTu8PASYORGsp8RFPwK0eJYUKVC7WXvP_TZdzWlti6s2NgKB4nAfti1aYAokdDdiliiNtOCDpLQP-3e3rwWEyUtbtKlsIulb-n_7vVBMNeVaBKS0LURLt_LvkF80nfeiLFxtDbyL5s1JbpgUPR__eKKRQKts6SeleiaY5tsiajhPEdSOPUrbea8dDUz3NfwNX09YTeVT7fHJVwbu447f2VJQ0-Ul5AUq0h-xo-RW7KamncPDFjG0PePyi9wRYAu87Zs0JX1bKxrsKXTas7XK2eJ6PK1HGO1tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rn7VEFytHr1hCpm1JdiESJu6lJ6nl97HkSkNJskI_XIe1G8D0CMnUgcdQ4dtBJfTAruF7p73HMLqhCDQWoizqp3F1aFcd56vFeLMFzGlTm4oRSw_nk2iuEtNzlZo6SV2rWBGyPTVGLpYS2n4Hm3Tarv70Q5gxhufvKTCPfrW3JJtWGaFqm7pgOOIhyeAi9j9oHo2MyJJDeR7E4AnNBSQctIjp1v4gLEpNRokbdRwM_hFBqqjUcOGBkECOKPfSmwdXSnFHkDNGyEtqTm36_SU6Jc_7tchbIzSDTe4zT9wZYQed4yo_tv5mOdUrzI0wQbYZpkMXquy7tENCbQzJHzgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9ln3j_uxJYjC9C6Kzk6L2aUmUkayQvcot5ImUna1iKZXyElsvXa-NXRtCh5Oev9gfiGvdv6XPrTfZV1SgYu4sF4Sqm8AAbZAqc1YNlnpKvCQvj2-JE5LpojqoelEinyydKy7NY2Gzk_k0vehgD88pl1hciC8SXiSNxlPjcyIrL3kczDwLFRl5nb1PwVysptqF2JrLrl9i2IdDIlSS1sMpx-h1tA8T1StLfeHkA56UCF_kUgNyn4qD5kr7nlgJhM5ReILDVg3eLrNFP1c9CLhcWdCxCMrhk_xpBwLiyDnuYqoado19S4UCy3gpgZKAdwbN9sXypOYxZSg3JdTH2Lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoDxvXocUYSmshpvGHzrYWnlg3UFUyMaIY1SQcaVo-IKNL8pSTjvOGgD_wPbhICp-PYnPF1rV14k2qZPrMw407-fjVplHp9DB69gpY3POfxpUdPdg13QWB6hMOKnSYxH3xB5jGwfcku0aw1Rr_3y43jlfpU0gQ-yOs7DzYvH2brK1Ia9au3-_mH8B_Y8nxnFallGtS6S3EEdiY0lVNX0lZSo20YNr4cr59j_t4k4HVu7uUdolBQRzuFFkR0_0AxTUZiaKxWsAriyqVFQrr9EguxRUVuEyxfXHUMLa6YpEV8Wr-8TVyDo_b5BT8hAHFHaaW47yu2sbEporNqtOidLHw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=iSA2Kx6ukaAo6mj660_1KzDwUSrcAeeaszyrYQyPF4HIHG-A7Uj5qgyqtyHpbQTTBGKShhC3mP0GfHTrJwxNnY9s46daKJXkGEMs8QAC0Q_BRup5P6AGGvVO2fKx2VsgSr_QCkes0bb1moUHtVVR9KKunGfwHFM2h-iCl_7Q74SPZOoJtai3pR5ibR3VIPuVTuBirBgWnUlide6gfGRwA3DlVjPjvk6Yv9gu747H1PIdNxFeePlaLE05EtlxGJhnWPzccO6XVV9D_n3GsNB92-WMOedYvl1-SoqaPTyQMVvtH7dS4pa_AkmR69MKWhaBHSkqa8A5Z1YrQaZ_sJJ6UZcddCOAiQZMEM7HXA5zANg0QahYNPHdX60P7aMHZibi6OFTEohZ0NMM1xim_Dw1cEFVBbUkB6AOY-DWAKGgqsZTwSlC_1XkI46t-i3kk7GypYnq5li0CozuzEAUrCQA3Uff5g9p82qT_eszru0Ti4uOdNYEBVOUAUASx3RdEvhCzRP6Hy1T_0QLgfkmZo5DhMuYOccf9xIWBBCKj20lraZ7YclXbboTE0ezO0f9q6FRKugai_1MToQlEzVXVgwxKYRcy8BlhltR5pXUwTc_pnvvDX2uBycGtk4kesKWnrhONRkb0TQEIfQODDDR-MWdJEROkfSOjA4GL_R13qB5NgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=iSA2Kx6ukaAo6mj660_1KzDwUSrcAeeaszyrYQyPF4HIHG-A7Uj5qgyqtyHpbQTTBGKShhC3mP0GfHTrJwxNnY9s46daKJXkGEMs8QAC0Q_BRup5P6AGGvVO2fKx2VsgSr_QCkes0bb1moUHtVVR9KKunGfwHFM2h-iCl_7Q74SPZOoJtai3pR5ibR3VIPuVTuBirBgWnUlide6gfGRwA3DlVjPjvk6Yv9gu747H1PIdNxFeePlaLE05EtlxGJhnWPzccO6XVV9D_n3GsNB92-WMOedYvl1-SoqaPTyQMVvtH7dS4pa_AkmR69MKWhaBHSkqa8A5Z1YrQaZ_sJJ6UZcddCOAiQZMEM7HXA5zANg0QahYNPHdX60P7aMHZibi6OFTEohZ0NMM1xim_Dw1cEFVBbUkB6AOY-DWAKGgqsZTwSlC_1XkI46t-i3kk7GypYnq5li0CozuzEAUrCQA3Uff5g9p82qT_eszru0Ti4uOdNYEBVOUAUASx3RdEvhCzRP6Hy1T_0QLgfkmZo5DhMuYOccf9xIWBBCKj20lraZ7YclXbboTE0ezO0f9q6FRKugai_1MToQlEzVXVgwxKYRcy8BlhltR5pXUwTc_pnvvDX2uBycGtk4kesKWnrhONRkb0TQEIfQODDDR-MWdJEROkfSOjA4GL_R13qB5NgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_4arjMC0gzvkx5ziM0BzH9hbnoK1Ow5AYxKnZb67L2yihK2dxsFRk1V77PAWvQpvKirYwnUblBAofc6g_hKNRbQ1KY074-Y-g4-KQciFbS_NAslFA66VEwmJmBVJ8skSqUL3tGepnA4VyxuhQ-y_fgqFeTjSapHwF1qEfIbcsZiAhwA8T2D0X_NAXd7UP7Ud624FP5gdMHQQU6nkjNWZYiNcl-HrvZ8UoWYz4ANgoSvArInUuXmK_kllVnPQR-agXUEHpWomI9Pa3cC6ptS3Pav1EFn87A4ea2OYSMJS8rt69kC9rhsK2S-Udm6-_ml1D7-DBviQS5Ou3bRUfcQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDxyFPdG29QY2O7Jrb4JwuJTf6W0E_1OSTaCpe06goo3C2ovc18zbxlEWNVISQle_QlBHgPEu_UbGQFUS95QubWEWT6kVkJj7eAv7HSUPNj19VCDIxs-v_t9QGi1CIejLxbLWUv0Ay9Fzp2vnAWgwesgrvWjIyAOeeAcEeTVNRyfvEKygnXMX3vCmKXh61tX8bV-LOvDdiBO1DyYi3gmjuBVvSlA1F3q8DfyaYn7NFR2gphC75tjC016R3ZqhdJx4kMJr-BeZtp71gJHkBz44vq2cV8kp1yufHmOdfhVBBeUOVtn6fHUGfVSdXzN2F3Bh38w_LJ-obn-HcUe31aKig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejkOcDAyJVvYQMg1MNl5WdXK-5kio-1fMlBMri0eouyAkQwRffb6V45bWvabfQv16EMDtxP4t_pHN-a8oORgITM_Zw20zutqXsxdHdSoeZMdtVEy_2plppfSgFekIEySfyDNv-GHcaFX9EuyjZlXo5jRlOhY47Afj8bKVIhjgPqGWZ1nf7jRSIIAWzpNPuDKLIiHBN0UbljhQVczb9f7uO47jIj0n7z-zjNBQGQpysAqmD1OfuZV9NhhYp4mNqT_D5HSFgf80gTVP_2AiBHaoHh2JIjyxySds4oudejoCwKr4Yi-qdavdUs3oZfzesgJ498FJKxbedUX7ylkrNqfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHVscROzJieqTaf5RQP7yac6KmTgj2ITLO2fO5uKKXlU1FMxNPOypsUVa_L9B_Fijbac3C9FUFQRjT9gaXnr2QOO9pjqZ6RyU4DFL4QZ4ytmpkFXkJ7xXMuqFIfKGo132q_dhUQKFnrOidnhHaLDaxS4VozeuB7GSYgDm2tpkOmc5q0TrAZAO7p19TueKdhJf27KG5Ks-R8jPaZWVwvRqxi5L7jY9D2UmKZPTUQuKEBji2jk2hzb1rrNy-N2cqferEThnLsOE2Rlq_Dl5ceinxGvsWI6eKHvUtywjhTHBkoPq8VZmMX-KfnM0thNpWDI7fMQ1pcCyzpcGYppp6rkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZVc9vVPPgOvWGb77QcyIjU102EAvZEhdQP5WHH_uxcrndWinyVI48eHAmwASDWrKX-m6jHUngDkSszTzK0jzzLbxsKskmrDmlGXN2ilQMleX5F59c79tQykffnhw5V2fos_PE5zz6plpvvBF7VV8sY3goKzJ7RXwP8Yg6RSTaKWPMfW57WW22fA5q40-2uO4ELLHqS8RIjbo-gJS3aUMqAC-Zyubfq_6wiXoz4DRYjwi-nGE_lAjdEbGdceT09xW4fWlJwu58mDTvHD8efef0IBzU8SWAM2iaysuthIpOEKwi-mwxNbONetuYe9m9qgAg7c0qk6Eu4QOs29ykOg0w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WttigGb0XhuhphzbBUuMa2mZYF5DqKbe8mAXqMYyVUU3fe-Lxx1Td3239bDAT6tqvdJ7NCmQ0nhm13fhtF0YsNN07gPQ4kl1f0ncAFcygu3nQMJzkKJesmINIIBWCl7itPNLqHFn7keq2rkVr_LeM1kwsIcjqXIaQnYgW-mBclfwoYtvmLGLnZ8DCfp1S9dyxS3Q6BibCU4F0rLviogHn1v4SdKsqby8mkIo_GzMddZK0gIkZOBPKUntjuoiHj1gp500NsnDdI2qA00LpH-ZL81RfwQRlWFLnfvFFmDcDOOR9utFz2BP5eeZtegH9UrtH8K108gvvge_JcL88o7pHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WttigGb0XhuhphzbBUuMa2mZYF5DqKbe8mAXqMYyVUU3fe-Lxx1Td3239bDAT6tqvdJ7NCmQ0nhm13fhtF0YsNN07gPQ4kl1f0ncAFcygu3nQMJzkKJesmINIIBWCl7itPNLqHFn7keq2rkVr_LeM1kwsIcjqXIaQnYgW-mBclfwoYtvmLGLnZ8DCfp1S9dyxS3Q6BibCU4F0rLviogHn1v4SdKsqby8mkIo_GzMddZK0gIkZOBPKUntjuoiHj1gp500NsnDdI2qA00LpH-ZL81RfwQRlWFLnfvFFmDcDOOR9utFz2BP5eeZtegH9UrtH8K108gvvge_JcL88o7pHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-WrY2F3n19bkT4ex-65n2n0WqB67h5zzKTVxBWGuUBMPH2qazIWxVUYLC8BkaBB16zSK4sHRrWoUex1rJKp5yVnVoZtmn65tIN-FqaFatn71HWrOTchYc3qnJVPl_3sia9Q-KJaPDz2oZc1Ma9TXDOe1vqpokvEBCLpxVjl5vXzU7yyD3OeupyNN_-1DzONFwgnjh47KPWpHx0Wd9yH32Ifenmk9F_DlN_2yprLUkNoerUqncGoS4y-UMgD-Tr7MxsnpoS9f_MpCNV-MGMccPyG7tMbQhhrnxbWq-h7EGFWD2JjZxHFU8k7ppSBq7whFEqxla9IIMNEya684S3kcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPoBAdPPLx-Taq9jIPJ_bpCikqsjNAshHd2pFBtoVScW-hZBFo8bJLjuqEbHLDn5dkdSq7Sgckzq_35eelpsOzDsL5BKR4ePJT2keuNw7DBIl43WO2LIr3WAG-ReJIiJ9iQMGPoPCOlddIZGqs8iEQAKiX4WeZ_0GIPztFCn0pgxfOasVSkTYbfgg72euqJ4wN4gZ23fhKClZxJmKOxzm3GAwSzpAjgBWU6DKKpIkBRfpeq2y77SCnTPVI_hN_eX5PGAIbftXg595AWEes-OdINPxP7NOYDkv1eBegRM3qnNYUvNR7KX41OnfshWPVOUF1JSFGscMH89BfRIvtXJsQ.jpg" alt="photo" loading="lazy"/></div>
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
