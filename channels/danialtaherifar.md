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
<img src="https://cdn4.telesco.pe/file/FWyb120xu0n3qmJk7TC8WnAhT7wP-ydb4zE4NDJD-RdyFEs8nrT_gnUnTW_-GFQBNBv96YYQ8V9O9JABCtyw3qYR18ZivGlcG9DLECEmExFdYqpy7VnPciY9z9nNt_Mok8tVb2SxfWqsODYs_jxYujsC99zPL4JcxipaqIBYVRMMza4AuO5PiklkS1l3rUnVU51yPL0DmWbkKUxx-BiJTMJc-GHE_3TRfGr2FY9dCNaG5MjpdChIztxh7NQtXGCltqwg2KDggYYE0D3CDudFHTwvlfuNTm8G2FDi9x5AwgsjoNwroOkpz2oHkXioKZ50k8LaItBZjTWCYcoFIxiQbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 249 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP9aOn1physZNsINVAVigTg86GlFnPguKG-sgcH317VRxuqlbPUaXks6xXmyAwxB4z649ylwm6ftkSqD0zXGBvqGsKCnCDpGEruWcu81e9khGwPOAqZHUq3Yv7Lke9fthYW_ncaxyXnEU5LgspTmqiULMP8by8BEvqKNL_HKhhh--j53gv9T0bd6W_T1GCH6pFME3isSY2Q2omraW24LZPTQ4J1-vhXK87BoHWuNYTKuD1PL-5ZqJmFpWU6jizUoWwCC3l_qVeYRtyqPLod9QetJ-GV9lbfnn8CNkER_jMQD8G4XDJIj53cx9Tdcnzy3A5voj1-gWjQxDtnwwhoc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 745 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dl1ol_AS6PftJbc0s1oqPAS7YH50b4f9wNdF-KqptblylKfdRZx1muz3MZZyvDscJYBe1Te-Rd1ZTk3XrwJCVmLS7ymAUohKVrrmkX1IEqWrYCS9qc_xHUI9QFZTGJdeA8apilR_WySrGIp1Lmq_yaN8RffOtCSmUmC-UDmv04JJFqVODgGbfXDlxiiRQXRGShxoQ6lpWf6L7IWaqtJlS_ulmfXKUyX0c5ibfem4ERvwhXrL0vjGsQ_YB-sMzsCEJUYr8TsDn81Sbef4xo-tK5Q-ulgacLPxiPYq2LYtwVjRL0IX8uwry3h3YTVrhfkjNh3TKREjNigqQTla0dbUDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=dl1ol_AS6PftJbc0s1oqPAS7YH50b4f9wNdF-KqptblylKfdRZx1muz3MZZyvDscJYBe1Te-Rd1ZTk3XrwJCVmLS7ymAUohKVrrmkX1IEqWrYCS9qc_xHUI9QFZTGJdeA8apilR_WySrGIp1Lmq_yaN8RffOtCSmUmC-UDmv04JJFqVODgGbfXDlxiiRQXRGShxoQ6lpWf6L7IWaqtJlS_ulmfXKUyX0c5ibfem4ERvwhXrL0vjGsQ_YB-sMzsCEJUYr8TsDn81Sbef4xo-tK5Q-ulgacLPxiPYq2LYtwVjRL0IX8uwry3h3YTVrhfkjNh3TKREjNigqQTla0dbUDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWFYXWN_111t5ie7Zp5ncZoyPm3jPMSjhaxehVB7K4sSwG7qJAOx5IKTYWrao_PydX3cVyZ53kYrmJKoeR8iLpkfT-vK3H5LJDBoPoVfJ4aa2w6kW6N_G6cVn2O3ymghBwN_V_58USz5L7LZkd4HyG2sXztZmHsPjka2jh69EROTuIgam3Sba3YUw4rG0nMFkdK-l1mecNBDecz2qz3Wn8CcPiMegJDsgLbl1_pcb2efyBP5b8sU6AgdLrv7MWFsiSQRDkr8q7kKRhB7MTzMOqVobzg6yYI1uAF2NCZgDVuLli-ZlY9m0M9qpofHeAl5-BnS_Kg_OUKjMEsFI9Xb5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPMGE-UQLm4ARk9P2-AArSmvC-izFJOz2Ikq9DyV0o28o76RSewu4O9Xf3rWwEq-tfNN6TIYx_v6XFr4GBOH1WhRRCenhUatrJWy1a3SfHaTmSRsQDj1h0U-KpThVqr46NaNJGdaEgtzwJhWTiMGk307MSG1So20eFNVSPrx-8fEncJxl45lyIDBCs0pZpnUFFTRhS5SGDu9fcA2vmS2VfdpwBp7u_tUFeEM7XnobvBbsVsUOE7B_AcKT70tCyfqAYwfqpq7uD6JjSEfTMVIEnI9IpCgHoBFTVXK6Jz9hD4B5dNPYkEWdrGAWn4ZfwQOMip6u-eBUAyM6I_6Q7F1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgk_AYLAWUf7zWtywOl28VcVbpht5J4EwK7RmW8iESM_C8sS4bDW5z2I1lE5YSinS-v9gY3Ns7M-vcPXrvRsH3ThqRFHFhnXQ2Z0UIZO8bsPbS6_3EFjTMmvOjt22pBEBHaFnrM4uXRqczmfeWgXy_j3Z3hdbhguI7sWOH6NYd4IRFsjQ4kC_vSUw-opYQ40lpSm7SvwhBde90oR9Tzi5MBAHbn2Ax-4qseCyrMTAEqC0l-2lLRt4QhOu-niPKACF_wC8ZCHxC4kIKQCjYF_co2IZP-CbiUwdtGfvc-YImD_pS-ddwdI-UnN3P0d2XO_IiI0r8-o8f3TsQXrw_k0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjVIb4yBFs_ilFfD_WOI-ABC1HtL3puWr652GU2qbqkSIPUF-F0KH3W0q62K3eoLwB8S9DYr3RoSvu8102g3vUytX2sLVFHyy1vXjjtk7S-F0k_K-8O8HiNHIKgbgii07hPOt8a8R7ifm2WSAp31537jtaGhLf-2X50tP5-EJVYjUh6ylxB2aulBQ3cZ7hxjRp0KbC8gSYmBl9ocLhLA67_CCMiR1PHFa83pl1-ETKdhqlIJtZw-QuHtSiIwA4LifvcLTKUPpB2d7IEwj0-By8aoVNHerwjDexXbOoCwA8VJKOGe8smG4NmVdwLVLs21zqM8I4-Rj58-fRs414xHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqzdzV52WOcJN51VtGO-qEe_y3_EptiZJkqM_1XV-nlw93evg3Ufyzcx8LRGat24Qp_agS6orRb_JCHoFsVj9y5F19P9WFLwvumzq8rEYNtMTObgS9yBJgzzKX2aOH_jrYpzRjtF6yy0alTvIylZe6JNfkY7nDFZLih5FAiAmDI54MBRK9-P-3LaU0hw0tlHMQlhsQYihzB0JsfXibZFGtbUIyWR4-z6raBoHPqArOBQ4AnQMTomIwKJsWvwoPRYGQb2kjkwpOSotXvsRpWhoT7Rfj0rS3dYlMzNge_INA2wjIvHzf07cusos6f74nFk0HbEUTByjAez7ijS7jM2HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPA4QRMCyTi_VIZYkJMH1fSqf7oW1C7Q0SvJcT16LmucSKsR0_4cr4lQXz9caARzHGcAw81mzYzY_v_VRASxP4GTUoTl-HUix-WX21HLyf8_xEubfc9BIMk-ZeEJd7jXIm9TQvZRFXXdmhq4okmlLvN2tXZG5d6CsqUUZ6vnEIwtXRNBJyk-IS87o1UqV_05jdZzO4U3KiIBjtn3Q9Bx_plLJh8XnXiKw3rIQjl9qYys_PSDTwInzjiuON8w4cBRDTl9PMYKCZW8yI5fLuJukdInR58iv_vJ16NR2yeg_gCG_Dclp5Y5CdWxm13G5kj8NeP-mR1pIybLInvO4p1oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCATqEKAkj3Z1hAK9szAT-Rfkypamwtl6NBGES6KDjStPyWL-CUtwdpYgyaJjSx3qILiVzWhU19n7c-En8pZme_dmFSx0KyOiOaRdWdCqkx4z6AwQo6B16h9N4bBgmDZVlMWvUBMwIasdf9fFs1Z6y-srWyscATd1aqlLetxiYu7qbxJwwEwh7XXASe6jmHmx3QYPzrtuGqVADY-YuutefvsWPyVTldXyjWOOnJouopL_gvianrTMX7Gj1KO3swecdc-xySSlOa360SeqRBS_ygk-kx4Ysu4sxhkTsCCnXcAbwpPoOuj6QnVsPSb8IWUeIkbxBld6eKm8QIQgv2n0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsCZ65Cpc9OdviAmlSD8-onX47zb-eJFhBzOfUlsQuUOzP0CmHqzPINjrzFJw8kvH1frGd6Wrz2xxCXfLz6rHlkLfYkuSdk-qkXbYsPJI0fn0eLZpl1SSKT57-2z9BcSaO4w79t1FYTGsycRC455UGWTyofKTf8iFiLCTJXkTO0xwY1yaEs-U2gHc7nxXMQqh__bDGgHwcbQkf0yCoKdNzvjDdDHgCiXAbapWE3xDvjzyBC3qQTARPIHqkKoKwMEdglb8u-dV24sMTC91QHEv5C5eL8slA8pWKe7Lm12BBJpabunpEnMuNDGFd5c_4LTBvbMcZvqBZ_1KPAs4lN1pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/an1InU_c8gWUimihKf_DsLdP--qUYcbyoqTlXQxehLu_9iIXdvFhGMBo19fudsON-aG-SsDI5_LSKXV_enkEQv69e1_nFstFxYV-XG3zKTRjPJ8iNT1jq4bjFTPQSQdzkmeas0yHe5EKLbQye7KxLhTm1uW6NwDvxI3DB5Dm4-aufIs0O0S87fb6c3zlk_y1He1SncwRLWrBsXGX6ZiDHcF1uKXsGrs60tytjpigYF8NUZ3EUhExULPl62DjQ54RRbxQNhURdW3wIDWiVT7i9KIAZix-gD7ddwChofU8l4ZI3IVGoae4Dv6b9pv5q1R8c6j9DP7H43DPilKX14lDUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWbpwUwx5ZIyexUOm834NeFKHfgo-OixnYjyT6wSveLH09pEgpiWgsj_onG38kT6255g0bROQJHocmbIbgfXjQlHa1oceh89fb4jE-4s4iNybdUA60lF6O_vOarIIZwpAWY22A7ulNtyvFRvlfvIlc-wpFXh5l5sYloEW6S9RMPnwMqiAibmyOEu3A0gGngL6lhZs9cHMu7UeAHrL_LxxlVgOEH9_KyLpW1gIyxxDFm2IMisw8jnaOrBIvsO1A1kpGOgiv2iz9FHIvzU5o49GKstBczKYVVG5qwWFRCUer27B2d9S9Qj0xBxmhuEwZ-VPw9QK9ENJ9syX4bF8YeUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ_UKRCx_hHcGXWUmi00xKktFoPZnj1DnOirXCtQsJYzAs-dNbzfpd209bYHl8yFdkkcWzW2RPPoQU8LG4lxKcoU9Zs4HYNTByQYdiSKWV-ICs0_IeFWXHgdkI03SIz-RMBbOwLAho8pCP97n8zSyvl2IjAXk-Zz1QoXdfTWMAx5d1sGQPQKPxDzb5WRUsmkYn6RAYlzSgJWRHnJHf337hLMjY4sj8glff32iuBCrQ5BfOqmy6mEVNcc0u4yLjDt9QKO9Ld-VZN3JdT3E_uuu9aF3LUD4RVNqnw699OpHcZPjdwTf9dzEj-0UY2HCZidrG-2ThgA6ZKQLVOFi731vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuSwYkpmtyAw1H3LdsJU8qvSbxMDSuCDPHQEqREixnPWwpIvHH-qZAyGAIEz1kEYPrMcF-Mn4XVR1-YrRbSe6sJKf4API171PLY3fvJCkdsf24PZhPfNlRTryHe6rKOMtGYqGrsUZnYd7o5phizwZbvhGIYCKmysGRA-uE5ueCIy7a0ZjTvdlcOAGCS19GYk0l35KPQ1l5C6Nd7UWwbrsLCyLHSxpjcJuM87FD0MCLCe8xGSvR03LkJKvs34jMstXiE42C5r1TeTtl8nGKKF1k8RpIdbxERKJq6w2i_u6Ol8hFagNqXAut40k31zPeu8tVrqo8D6X-ytEevJFntmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoVi9OZ4rkOrZhZVJk8PkEZ5LqS6kADcVb5PCdhmqgp3-_NnozUQ4ZciXP5nCloE7uR8GhQvVTwaJFqbGAOt4V_52Rqp_ohsO_S0mnhc4MXxz_NTQazhiFbvqwlJlcZeT2KoX5wQYRJwBp9xYH8ztzk2R9KYD6FOoDsmjsET6XJvMpuE4dmX996aNozR6zuT7_GnDl10pATzNYuMqHzR5hlLG-Dsg8oHcXlvFYlGzi0KPJpg4s10iOSyO2fEY1yjrybVy9Y4ySYtnT1oOUUFifpn0LaTNEE0l11tKPtFDA44uR3B23XESm2cxCvTUj2f8IZRhM75PlKr8uAU_j9SGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKivB-z6nv6JbYKRstqufA95dlOpNJlnlh_jBMbdO6QygPXzGNxZo8KmWrQSd1nLNPgZBA_gf8rjx_ZJgk7yHzy6vZZBl16aEjavmfSe67z9c-4hKSChwI4AnkZen18w22U71DyLsdX0BYUcOdXIUkFYqwajmfxkP-6c07yaQwU2EGF148orayZXSRP1R_w2wd_DKRpcu37kkFQAy2X1tgZoWu4xYCFQX6CvepQq1v5ScqCcON2Qx7t-pGz1VaLJR-KUMaFy8S0QwGwvLm9Ei7x1sI1SJ30EvH8yAAX7HG7YzB2c1hXe-ga-5gpLmtVOKBa-OEuj7UAK-3Ik-71EfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDVrLDtensZxQ06prPf52sk5JSmxT4sf4qkvYLRctGQ9iddrrobbPAcGDpVKtFIj1mnMPJ65DNo2yiYsVb1oNReJODNVaEbz2KEYpRoQ3aN7RryFUdhgD7yP3aiOKXRnRo1Rv2QSj1L3xE3o45reU81uM34k30w94wAyyw-oPFDvYvmrg9cvfRmSkdFc4EkYRELjvRwJvTpIyxJYFZ_9b2Vl9it81mHwuYR98nZJFBvI-cBndTrXpfXmFZlXf2ajd55zIDLiqfMKE2zG0FgCF3y6jkvY617fLnBRonA4F73v_ey5WM5Nyk2jABXOVOG17hi6FiX4Jm_h79Fsr3GY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzPo3Ev1r8L-XF9G2vPVIIEBehOz8AjOxbUh1CidntpNzLKJ3h_Z_SV-fWjUfFcf6l-D9Jd_2ZlxFhkRNjr6vupYMHWHxBK61Hoy1lqqj1N5UVwCsx42nmWqOOECLOYE-zObuiZ2mFxfPWiiR2UZQaFPnmBN7935Uem4wu4vG8vi63GOK-gPzQbv7-x_aeYZN3xLW1jw09HMXNJKSwrYuIbtk1C_5uZfVBCS5reo94pGIb_H2bwj2KMrl15emALiy0eN_iyrGEHNOLch4SK3pnJHBi2xMwJIdNiL0VK6f3DKLY8CvsjJtBOKEe2XA3OEHR6s_jgXgmdxkPjJVvqleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kh8EeWZ7c94pH5TQDKNzWzGGG1A1QZl5-yWwVH2CxH5tdWhn4JNyN-ZR_pqPP0QS9l8WO9Yg7sNd_rolCS_TIpALcoLMLV1lvOc3WF4cwD9MYSWhLYMw50xEBF_onHA2N7BrSk7ePmBZv6afX0g-vwX4AIXJhfbssm64kjqZwu451UQFsXfOCmnJNH36PgAU-uxWD3ppY23wpxt-J9K3Dt4NMjMfubz_0-ZUfOn1nXll0GXOCy6MtvdHpacbrA6U_bvG1dONOWSRchGSu-rAZdB1YJBRoHUGuaP--L8pBaXohXFHfuivIrQHccPaHGStR-5JFVJf-Q97em2N233JtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAialFlYUCpFiq2aESoaGlJWnG2zClkcnwh2ld-XeDHJwxBW7Ocdck8_iaQkfJGTyuwkpchQzrBn7ZRm3Gdp2ZWKyUo5QdBwTxADEweaWNJKqHdIWh2v6ch9tEkbC3knP4wm56TO-Otu6ftj83DTOf8HPDRd0lauWKrN6ecnGpaXVzohtw9hEeyU3XDeEhW2WtzZ07-UW9eF5rgV8bJPyEIT2g4WYuJNtWZBxupo-EJ3VnOEP8UYPOBU-5VSy_dDrMnPVhqYI_FyMQ1SZtTUysA7B1x47cYdEq7--LMu9afhx_dVa1JI1q7I06UWNLIPvvngZ5YQtgE_K8xvl1zQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=epYuleNFlwFXKdZguVjUin4PujtLYN7XcyRrkWVYBj9I9g5H06MlqsQghixXBZT4QJt7-404KeZTYTMt_s_p0_cwZVB-hUEuu5PIV2Fi6dnXi7tVcyY2dor4dK-ChBGrnvIqwz-0JMyDOs297wd36QOC8OGnUxIw2xO2XX1xV5RbM2VRMOTRfFDFcdWUK-jsTRTqXc9SXp7bbjl1rFgrA2b8S2DLrj1-7w2uUHfV7uh177yTLbPmUVPmilXIvgKlj2hO_AsvJhCaX2SDU1L_f9olqO5umQlBcMOuPxQ02M0g-H4U1AchlFlsTjRyfTc7ct0l7U_ym5bfaeWw11saFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=epYuleNFlwFXKdZguVjUin4PujtLYN7XcyRrkWVYBj9I9g5H06MlqsQghixXBZT4QJt7-404KeZTYTMt_s_p0_cwZVB-hUEuu5PIV2Fi6dnXi7tVcyY2dor4dK-ChBGrnvIqwz-0JMyDOs297wd36QOC8OGnUxIw2xO2XX1xV5RbM2VRMOTRfFDFcdWUK-jsTRTqXc9SXp7bbjl1rFgrA2b8S2DLrj1-7w2uUHfV7uh177yTLbPmUVPmilXIvgKlj2hO_AsvJhCaX2SDU1L_f9olqO5umQlBcMOuPxQ02M0g-H4U1AchlFlsTjRyfTc7ct0l7U_ym5bfaeWw11saFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9lmgSzVPAZ7506qknY-Nhv6IrkhgOM249WuI01ouTGscxQhxIoUhLHZvG253UNSbMQzpo5xWAPqOYBQs93C0Nw698WuAiMXMDQq4AHTuY8I-TIPMaouGq8ggCRb24IcBDDTV8rCPlzahnyiGUKHxC0a6g_lZ4AbGoXIhfdJhU-veyGc88ZAGe4PVhuBat20EKBGUvr1nLeyFBZ3ATQ8aqlGYV6SHq5XIJGTfDkva98tAZAYtOW6_pZGhxvYxgzVYav4p6aV35MXOd_OGJZuXzioXNKqhheyewTjgjzFAZScw2IbOckVP_PHw-tS4HcUFL2dSdBYAZ64ac_3BJpFsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbgiWRrb9r0ZRoI7MMwtzDcQ6Q6fmC5mo12S_fBhq-1BPRBasCXooHEK0er3oKbLgMGgYc-RX1OqpkhStRT_Iw7SnCD12IMBLMkUpUnqPCUSz7pZYh7sUqbtRTUzXUNS7QA6b-81Tjviuh0APHJAchvTVDh5j_t0-1fUYRwQujDHAfpSQQcOOKKfMvruy5KnOSV9_rcR8xj1KygXcNRC__FEIPOtK6F8h1-EABc_zsuj_DNjiHOgoJZFmQvQrF9n2h7Je4BCCmtS4fgBF1RNGh2Wej6gR-TT5xRYmTNLBuCPxvop1o8A7B2Ua_JP0f9kNOAo2fQAiCpnXMSzeG5ZMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjLmnXO68U5U69W54miPArQ5prjC5Z7l8FbrT2h_JVRMj6r3NjA7qjQTtXIhP5h2qhsqXY6Ee3u-ngyAkiMNrV6nETBdUsWoQK3oxMyV8jFnpWpeDm5OFsWfKrYGFWd4R-C4pAQxDEOa2YLwaa9qxDNyJ8goiVTCh-eCnvG0eoqmrDzMLSDXg3vA7PEl6GlPDVnagb-3FTk7GeJ31091GScqDkY0YD-4mTu0yC7cvtjK3BeoHuOQsWPproCN0HU0Q1AZNkLA_LDlteQB3dSVJoukhJFX_C84bAVxo3u4chK6-O_v5zgjKoywbMfNUfNTN6mzMRnxYU-HgUxzUli_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDXwsXldOwUpCtWpfJOQ7xYNzyDn-TcaqukHeE1GzT_JqouB5gg2huUhkSHrHh9adTr0IApL2LrNge9K-hs0Yq8IEQRRY6kahLRvoVngfIPtfdj_RPUPRpBwI2wrFUs2wdO0teSa16rheMpMHLO-z6tkvILW0TYEUyZZYelA_Qqwaw9jT8KBZWZaTZHzspYBMzLkfUvExpz2KsuY2IMoOYFV6TXCpo2s2QI6QTYH9dO99n66EOXtgVfDgoaC_3iDdBtSDD9XmuIsMUMXRj3mdwVdH9tpKW2A_HXQOTbaKTFnLwKQLytftHWs6PTuk5Oz1WY5C9sxLlFTTxiGjVrysw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 803 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_SHgJNP2E-CLK9bH3CHTEBgTGFz2cvezIKsxVUf4ZYmiFF8x_hGNucKNWO-GNySIB6np_OrzdATIxPNXLoNziY4ciXS8CP2j4MGQwGq24LZi67rfxhbrTDzkryCGxIL6LmRVT3Vpb-0gl32_WskP3VTpbFnYddibBuyD-4olTfRRqTG3uxln_tuBt5b4FRtYayL51BTjDMAGBYmDtx8MaVLw82sW83PQ38S_fh1eAUi9a79GaR1c3KPblj5yLcVp3DidLFy5rlTsSJw6rG3UEihQ9_DWnlC3M6XRuWWAykKIhKwoewq2I2n6mAtVCPrvsa40CbAHyH-OMMo6V5XMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX7spAKq4LHqfcLHiZiftjjwmlOySZUeWubK9vT3Y9bLGTA5ladpmCK7c7TnrfqPs5f6TK2qzD3DYNwVEXCd0YK58d-lKTisxo_y2R0_XCWcqlhNtzYBD4Ds4L1kc0Q_oDxVT644x_6sC593u0cQIgGjiAR7JkMiUXm-AxJlyeWqGRFqaFuhMpvyxD4NhavMsCnTGPVAg-PZ_QfpMvaYD3PStwB_UA6xhw_iQRQJRAdm1jBHfK--6rayqXAzia4Es2QIC-FWpGVmRnjcHym8fqp_XjO5k9LaX_XyAb0MkLMwSjyvj8bEr0mhKw3YBn6-eQqx71qaWuM2htM9NLZINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFp5s5JBdfRLu39bihMBacGfuoXiri27_jprA6OFpnRXowDG7LGwNKRyLPUs90tMbwNStrruJJZ0lfTcC8K4wYhzYdJJ5v9G1fFxFhpZha6U9SF28I9To1EkgnfP6mXo3wqv1cckbN27wWjvIJiyWc9aKKVEz10KFBrjdbmuLHdkSTJr22c8PI4P455xUr4_OkX05jE9Nw7v0PEjjqH_9bZ7FGwvQ4SA03n4L9vHdrPlbXqL1PqDnHVKIjZrXrCv8rraAVcDONszku_n8AhSiuyhB0OxzSGR0kwAPZjmyovU_AhrSDQ4rSDovnmISz844P7UpOYWZYJ9mlZQro7h3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBImUF64Em4LUajN_8ur6RvaOwbT-LMYOx6r3V7RXHWjdFbEhh7g6WkD9E1rnv1aTrxmUjkTU5gmHkoTanOD_DVLqf-qdW51X7rWwYgJ2RSMfLKW7eTGWYfrAx3JwHwZzODwJ3mzUfIAuXFftkfidiGA5r2k_3S-4tmrUwQgL9E_y5a3QpZ27FSJKpfZwMsVXmPIGXI-3yGc4eQAYCwQ7mmXgk5bs30Tzd8JMeWtkMX9nByj8CdLneijPGzTpfNDO3PnxtDM4xNw2vOUc3U4np3pujOYLkIBrdAXYPulRJcC6t2FlzyGjFgPfJ2h_VmXq3MPVwSVJ54iqxTQJncX9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU4cWIkohkpV0Dnw2EZCuy8C6oREQUkA8eJByGrrFS8MVEK1xWLFzSZen9DVQ_MvHFF8MbI0T-kb5yuw6dPUdIjqBgIRI8HTa0K-G-rGIpf_BK-8UxVlL5UAjfGBhpzkp_Ldi92UqB10csV45wfJK5w6GwHWm3vKEkEC7qwQbEH5AHJEwFe2payQWVo8U67ZNLntD4dG6ATRW8saB8Ww5AqSdIrypIf24ZJgE606ojtKwU4C9RCMJZlsXLSRqwTw4C80d8BvyVlsh3bDEGFXBIy_LScy0hFs3SOzWAqgVG-r00t4U2MJqmidlyTUy84ir3uB5QbsjeI3g3YKi_v0wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JISg1Gldyj3AMQFzXug-RmXedaJspQVkhKoGAVRUXfH0jMC48s7PXmW4pHFEoaDmCzsC75Bm0pAGzn7dy0d1b56FIhtXg0WCAiOJX26b_1o696w4EAbZsPveuUZRuOi-lMuhnsKxhyDSwj1ZXgG4mno0Wz67iDXBBr3NBH1mINoR8hzkL53xrJ6-4j-eD6FdhOB9jj43ShR59df4xTx_aFnJy9P11qDki1jtVWNTrSj53dsAHK4wmN-RisYt_kb1n9J7zpk2t_SphGcrhfXZd0nQX7r6Csni2GqbwYtEYV_uZDoe4dlzeWrD3-P-rez9KBtMq1hg8jCQjg6Oc6ccAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRuxXx1_cN5qnEZqicH3lbpN4ouEfUGKRpNWd83v-xsm1GymP3Z7asAI0cX-ua7HcMFzYmy5O0-ITsukHixnGR_ewS_QXInW_7Y1SWp7nPt0BWJrWLCiSCRdcicn2GKvjyWNmoTsK8maBxdr2IR-Z2RHlaq7TTOfeSL1m_37RoPlsIKJYfCEJVLFxM_5w9gsmCUMo-Yiy0UcZx67TWQIGnB9LqL48gFkEIdHr9UN4tfcQd8eeNN8Emi2ya3YkvFLDjyPiTYaFwMfs0LNaBb2B1QJrgkPSHPqYUbc5FRJFVS-1xsauxGuO0U4aLJOfBnhb4ReLxzwT4pxKgXtWTraYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnpx89YIoMrjb7uGNNbzyqKI92DpvGXMPto5CJcj4Fi9s6tydxQ5YOcTQ_a3Hql843mvkdAe5y_qufkqOoRSCv2qw8qIzuzgu73mv2nHPLTdGhUHTDilbjf-B_OHGGhuVlOOW8QXC4-SkXHv0rbdkypTsKpRxtwRnJhxAxny1UHXMLj5ubXixkgAfDDv_mG9T1bFajYRMmPBhVSOTX5QS3KVjbSSQpCg2JsLxUmtWa_BzYHXzSur9fkhMxHHKAIu-58AoqK62Rg-OTBBwYHBOaLzIDY0vhHJvWNFtH5Ybhbvqa8ItR_xAmyzAephRv69SmMDqZ6tbvtI3qbgpo2Z3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plxQudy2k2fmzdzTqfFxv9Em-HN8as3QXJT08NT8c30-RRVl2LdjZFwzMRXrRVIc8vAczKnxFi_mdT39_R5t1jj-EfcPbITaa1qg8qQVicH1qdhKM49LstY4yEcckHn1kuSNV3zTGi4h4TitbBCbCR3QhNKiXrocEPxQHMj-vH2iIfNr1VKbdjroUXi3MuSe8uybxOcTR-KXkbc9busDJdaxlK3E0O3GfurqF9o298ImNY-Cymc8TT_fST6i3JSR_cWAxNM8bXJTpiw6aB5fBGvzmd0b8WW-V4yfKhAzIak6PV752MsSIS0Lf4Aand-a8PgtskiZycbWIas0zmCOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuk8mLmL1i4SvGpB2sCd5kSiUuj0ER78Gf93AcxOqs9EswgkQEoyhH4SngHmryhV1eIHh9tB3fD8-r-VWk2K-mMsKEzvyn3BdOM-R1Uvp0XBRArizPTBAsqxXDZoqdIAlc6-VF70iA-QkNq1tBYX4smaJMqKbZW63d8EmL9QEgWUWFkivc8PuGQVUEJ6McY5s0N1qcN-chWl6s7116aN6b6wmAqHn6RXAqQ0EN9YAAOEmsKypG3UiEHCHNhGzLPhZapCvYM6yf-6mANo4NHNjxVDNjkfABvI93dG3-YZgg4Zbh7LH73IR5wup3CZpRuWpe46hUw4Uc031RRfQYLqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5yFiCJ9KzUZCdurX9gwIFLJgeCe4LLI6swholab4mmn9bxHl9qYyYvQOz74rQx5ZrQcf6P0PMbBAvplg468y5k4WSEv2BBHimdl9ArwuGzTTwW5GDXvvPR5xeci3Ni6ipJP48FZwWINmWZw8KM-NtN4NZVg1B6IV0gUHe9zChpy-csJmJqrQshxQ56ZbcfXJkvgWhNBZDV9iAo9a1_3JO6wVhnY-kd2FF55jHmufqoC4Y4qXcpvKjJf2hVCpMkiqTDt7vnPqV7x8VZeI0hDmlZJyWfruyJR3s9qwB_5lGnPVnvBTOoQ7EsWlTRkn4OUPs48GMlb4Z9hAUXqGi2-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URfJnRNFUMKfWLT0nj17jRf30KFydk4T15d6Y_Vo9Bw3qjmHSREwOZUpteNJ2vbdUfJmEF5-8xXkN8PqNlU82lNUmbt-mn2o_wi_lkQpgitoqo4rbbUl_9fl_Gp2nbJj_gAt6GVwNNujF3uMsZFyHOlgSACQyO4YXKXSAMcil73mxrOCk93jUHg_EC2tDZd_8J58XMRtlB7KBM9cQUeQUMttRAyk4r4w5P-C6zZR3LZmOmHOzME2M9Sk1cLTFHlQn5YhjtRbRL404zquFFlZKDSt-fzxCjTbMOITtLij_pnX-TBxXp0xwE10suGWJBzHaOeAvvmty4DkUlVw1eMfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEHMVH12FxsUf1NYvCxxFveUol1lAV8xZgTdrXjYJ-6H76B0QVRCThdO_qzPDaG_NOEYXUh8f83oeJkOqvlRc1uNtgvTfWxMf730qdqEKJzWDHiYgO6ss8vgRtsUKmaOusgH22S7J_wJZQM4lCI_yWlJzTMsRRVu4ia0kfu-DswjHisnrBZTvwn9BETzq06hkJB-D3RnjWPlRmnF0LVHGpJLUDmx2pwUl0aMPJPbxbh7asKT4Kfk5eNDFv_jxAL_fC-qQIyi-VkO7wHmHrypqxJvhwCLgni9biAcqzi-R0bgqwVO896waCDtb4NwEkxWcRl-hstsWBHLzLZdbeaCeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxRkuz1628YhT6u3paxyKJrmLNlLA5XZ5Y2tH3D1jhf08qtXtOdnLnx8jQy-EEfFG3YgoxTdjPUrF1Bzo8VCIYZFIplFedfbQRAts2n_2ZAkiuDN_W0QpcfRRLElVJVHdaYRMVCsDTJ58ujF7PmJ2VCT-FXMdb8zYUlkbKt4VMdBo8o5o4yt4eH0ZnxHRDht2N-M0F4sw7tsxg8YHpAcrQA3-GuU7BLMDfxcvGed_ZkNnb7kdD-8p2HdpBCmZSmsXHOFMUbA3Lbo-LWq1AQxqqw7bD0gRnPZZ1OJi7ilrr4pzs_Vd_6NKhKEgXKmF0_W3vgc1h_3dla8GglVYSWK7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 581 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6CVuoGP1lZmSZUUUEFJwAs72h4nbZGqzfNjqPfLhqg-RV82O7dI0X_m3tnpC4ntOM2qvOM8xfzyaVFsWQFx3TTXNfVUj0dyUnskT0jFIayL6sauR6er-7eEYNcbqFD_Bv-uimgXkDI0AC6G6ZeJjafHzl1mMK8JFIjlGSLjwdkyPIkgHYRJPXRD0Kn43_-WnA-bBqNV0g-hLBkwh6Oe94mln15oLZAWXaz09NVDYr2VO3tlaKx447VqnLPg6SefvkJ9_51SxwWkIsHiOxUowUEZ7Zbme50s1jvej5FqtQ0jwyokI5Rih_goLg2iBw11flXqQfTjI2ltuLJsUSHecQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 593 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnJmdH9ScBr8WaDdAMwx4NWkRL2mFFZlv0D4N3vz0i_gBD2cK0trWd0P_pkZ7SntfG6ZO_-zSrMXkLg10pI3b5VdwA6IXFvv-3uTid6uU0FXfr3n4gYx5Gdh5BQ7DzmsKlr7tNOzKy_sKxgyTit0kbpmh73aOiqHwhrhRlcSUHvh4kGcNXv5rkovxJm77avDBNzBubi0DvvajqcueMJoKViATwbTYOdrH2hO13MGrWc7hh04Xzp-KkJFu86jfnYLAhm0rq1g-QyYqxhHEAc51uOnGGHW5hy4nfzRc6U9AuNgJs3HL20DthdfPhmrNSAGuiLbhHTvWw7Y8QOHhaCgqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9oZHj3wuRYeMVa_2SDyouJF2Yy3kPFLoz1N9B2h3Z9kKvLrO1KRALsxhMeFTEalcjXZfXkRdMYLMrUX3PiOo6KaZPVAlcLCCjqkqsUDS_oNqyOlqe7atbjN80kXNn7NjdgRb8j2AMCCicS8DnB8uFP-Zw_A0RxWoNPCqv1cU6r5vH5zsXSczRQXKPxf3EWt69aWVi5dTDsP9_x5PvQFgp_zeeN1wiBoAGHKA4gC-B8VWiMKfONfMp4DBM6BHjfhqHpoclORD_hrqXmsyJXF4TMewsVRBm5vN72h9P7cKQVFRtAbRmfQJmRyhM9ff6pF6zrh_Ny1kPy-LeBCf2jHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5M_eI_lIedT9vinUoMw9qOMuLvcwiuvRbnfSV2LZQRNxHqzKW6ck5wyg3k4A2_1ykt5794NdkINJNQi2WZEJviHHFDCmky-WphliJXTvQ1ml5JvUWiCVfcsvD8_WUSk545mlHv66kLWssxj9uG-jWyTgCctColIebDnHuq-X4HjzNCdPl6NiF9o68vtmYC5XD7MqbO9w35tJB4REVmsMObl79l2N6xuVdmi_fw-35bTPo4gizo_CZ45wyNMc2f5Ow-Xx4Npdzjm1spjZELgDY0KuGN0z1oc-KUZ0zcAkj0fiPpzVohdgPRiijHhR4H4MJZxRhAa2aZCR4RadrnZfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 714 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccM585CPu-JhroA2lQ3UAQARtyJIGagjpxKO_1eZSc0NmCIWMzbcvh2Fz_FYGFVBPddQkeotNeHj9YGhcaQT18P0UggMLaxA4On2M-oi47aQMt06uFv56RRE9Blh0dgo9YEinsUHzZBhzKaAkTxRFB7F6jfuj3L9VQLOmCberrBE-oKktlZnP3rpaNR7QBbEmgBaPni6vsLSpzwsKNvQrPiiJwnjb4DlqIgVLvBt4CnjFuWdFmOQD4-ZNXR-d84KuJYeejyEGsg61ceZZx4I-_SV0IkI4dh9Ez4sAiDKH2aZu3ypzz3VGf_eemh0lWrV5DjMJ2Y8DuCyqWiijo3Obw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 612 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkA51TsT-QRH1CedWkul4lFPaqtUPVY2qbMVXnOmvfcrCkUNvl5ijc90LYFSNAhAy9Xb9mTlb1JbILdn0W6qGauKWUf6f2AUBKqf2EcxF4YuvWJCSwbVmjEYlk1AlA1edqCb4oA9GRo5cQQGZg1bCJVA5brOT2UvWit1yubXZJzBsl4DXGQKnq-qnOtWNjIr6tP8sGi7zoMOeKT54Vyo6PSbtXjmzfAlF4A4444DUjWXTKnRUSmI8cOEtYhOu8rFyKOITWL2tREhBNsJQtocsaItXPVxfxc6lTlkXnzpKvRswaqpZUkljG-_up4KvOSZhHmb7P9e5Rxw2n9BQBbvVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZWmomymB6ETlaqZji51MDJj7r7SE6lvDRmWnOGzsJ5J0XRYSlzrtlgf7k6n8B0jmvHL4cVOGZiN5wOyzRvMDlOkHdkk3Rmg5RAzf_5--bACEHQjrRehkEIFjGt0Hh2_Sy6nMq0fpbsOvGstZeAfq7uGFhHt6DYHeG_zD_Y4VZTEXWcnWD1pWOCzplo7iQkNr2c404OyW5ivuX2F9Kl0nrggGYV3vIQApiV5dVjX4yLGNklqZIpYjbx3pcW2Gc8MSmuNFAZ-VB5EIZIwSKR3xahJLoEL3oFVMWE8oNQFHTpkG7uBghtChfEEmc3PMt_v4R0yf7DL24H5OkL6q0H2jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOqARGLadPF8BDMMOlugNa6w8RxiRFWrWXQKJUA76XPzfKQR_ZQcunYoDlssvRHXmtQL0Bt-XrQIaPwq0hwG9kiCY8uDcAm-BTuhzAjTHRyYLiVwwLjKwAsUMI08U8uCHrkqCWhfjQVY4X7MlQdQ8zj9uhYuvG8zPHPwWYZzrWyUpy7YdBjgbfMBEkSDxVQl01N0JW9OGqJ4snUkjwWIws5st8gU_9wFVLkG6O-qD3lyneDopC7wVG23tyUOaWaz8DSiuqgfVi1okVPs2KdxXLe_FM6ztBrMWu5Lj-IzO3eAICAuZbtbs32grfXzxok2XqWyEdZ3Z_EQgjrFzJkEag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAnLEnmpL0OSCcTf4jp-oWWnCMK3yINGT2faGS7qmiOsjGiq9Xe4KqN3RDz_y1jr-_dgzvGhEilu_be83PqXFmJXDGd4feE8E1Akh-1s6n1YE1onVXt1aZUDAFEEsRsG-lONO9av2TfEm3h5UVSqhUkCSbHTFPJbHGIgbXC2wotffCALrzzE44rW5-W7uWFeUpFsak9Mm6RANS5hNAeZiNgotERWNsBgyYNYnLifUfq-RMEXUbFL4DDuel7b6Nt-iREtJIhECx-55JCZdbz73rLPJRI-UbYm_a_zzbkn27en58xPCl8MviFYVK4ZbI9_WuC0gTf0kvDHoKK1XxxmuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScxXqRoqv1MHyS1aUN6YYEDh7EnOzply1aUJEoJbTEvyZ7bX51KlB5dUOp92pvJ9O7sPZ4BbK8w3XLBH_Q8mXH3M9St3GtG3TKtQF6HdWSUTZxH0GOtULxY62HyR9aZ7GdO9WvTZwhCC12pE1DM_-Ag6Z6XgIy9lVEzEnFb4c9Ls5ZAYRls1-sup5kJ-8k4wHMxMrZ_KY2psfhfKiqEMoyT_0mpjrhcqD9V7j-JTIcu2gRw00Dq-Pm_IOuNeYID6n0gMa_nbA6-A1HBwWYoymDOfQkA1FBJI0L4y0SaQFkvtdYuhPYgFe2cHwJuDEqitbM3jLZRqMxkQgVryGY2HyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GguWv5DQu_8JdxOY6K7jFOi-wPIbIClvPS9LjRFuMN0cWWHbpgkCEtuY4C4Raar9lfmS2SEJ8VlwrYp5PZhlqtbcFXX0Rh8Ll5VBBWkshPukfvhhhxPLbKGHUe5op1HRquMRya13ZBBFfXRsxNuGsKn2vnVprJnnlckj9Kv0wEGOPd6-LxaZNjWPC05irqRzXanLH4vNx_azz24EvferbUY9xOtgQD2X9puikxZHd4Gxp5IWu6OlDF36OYJORKcRuM1C9Imy-jaTb7r9lqp6J3GzcYccxoPDMbW3FPWEu7UYWbmtqE6INIcmPpLcrDULXQXM8swYqzDcKQqb6sLgXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr4wTgaql71I9IL5wgi5s3iz0lb2X64E2pt9U02TnPkM2-FnU5Uc-lveoVDV5rwFlwLQLHnjUUaPUZymjc_Jzv5Uqg719AOA1Wm8oc97-aS8FitlNYxF5WbfTufP3PtJoK63xcpIxWvz-xa_jG5yOFGzIgryvi_hD2H-vSas402GkZ3_u5NFvKlDTxmCzS2AJUYGGr7osUZM00k3cmjDkZPE94l5FP_dn6ejusRQQjucnAdPtg3oS4QVR6TgqqX1EfJ3CSxEP8eL6e22O5xF-j9WVd_Vv3YLJfhH_mSvBrhu78VMsROPuNkGMJiqCMNBgWPNQ2CBzFxWXb9PS_Syqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Njg83vH5BLLB1go_hFzUPZYAxHpSbDU70rKoR69sFFuZ8LT2l1po7hRGXZXJrN-r312cM5ELGP-ZpwUUwMHCc9mUOzSaV8IupcXzJq1c_oeKz6J0AAADR4aEskkiQufxRoiAfJt33X9K6evRCesb5_uvH8jPHs5g23kFXqmnGmAUDP5WpYom5NH9vJ_hRuQgeSnlwtTDmyJgvzjI_kZUTn8DB5j5B98US685M9PVkCLN3RBJMWgfItQb_5aJxnE1vRuKpXwoofJNMmZyNnWbZ6ZonZsnJiAQWgheKA545Y5c3Tku6PkcQKOOmc8JUckX5Vv-nBAav99qXXPfZHFl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJGvmyogMtPNa1nv2ByQvGbkh5rV1KbVMZCSytNCw38SkirlgXYeHd5oMB4vtvO4yA5ENRg5q6kEoh-igtf8EJnVoIz5PvKID-_JZpuqljkt3GlW0QPdC8nKkUOZilVZM6Jk7cKVIeoCHFSlUqig4BjCFCpw7GTkXDsjp1JeGDuGtv6kGgqM1ItxZr92L0TVh-wRnStkFPCUJP3dDxdQ1RPBJDUjyTEWA6-hyDffGJvan8Hv6p8o8mthVpse_k7c-viiJkuCdbLE_49puWYJi2j-2BO9tf6kpYch2S1moiA1YLbKU_ebDNnQYWdTj0MCDR05KISVJeZDnAarSaN6BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSPGCNMiA_7m2W83nl2X1Ok0gNl5g0ATfrk1OayJz66dZuIAHJutGwjd9idMVZmycP9NzLDeDOOY5-R9OZDYCVJqr9HE01B7F8v8QnOM6d7IaSF9Ml8NTjBNOJWc1UrFcfuXsAGzdVhL2WWcwdsgY0Dr6c6cIfCD_v-wNYgXmcDSi8BEmz9NMQfVZ0RUdioNLq6CFT7D0TW1PfJBuCABczC9ZW26zaJ5pZgbGF5q2Y2rfrlBezMNTY84dLa-btInwDB9iLulO5pDa0ppco8xYvMuQ0MK7_5hoRkM25ZX8sf_XhQbAwqA2n_a-HGrhpYcourujwm36Lq3m9p5lpQTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZsf8Sj9pUAo5IU8mRZSyAfoK3zjY38aSrmDHKlmv-zWnSYBCIR_y4cO3u9Llzhk50SuzffmmGnS_NNRuNP0sijnUIJL57ASCrpvw3SJQmM8srk8QwX1NsTgXtXbkbHaal2nikHCg8awQ-MjV2Jz3byJjjo8kAIuU7POJBe9ki4pmrnb3oQev92IbKXoX9LxLG57oHJo-gpORhBFAJieXndXLYOzLky4cZq8ZcKvrt2aGCZwjQc-BAVfg44PsDG_-uonD7LWTflyPWoZMLyPt4b4Kp571bAxlSsAL0kuhaLOscKnfr4lXlqvfHTsO-ZVVdWwKNM3IKRfdtWLKXvmdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRi94txgDHuD4FIb0mV2gsA7x8AxXUwUZnnWQUlD_iNyhQ55BBBV3lrFw7rBHUEomZV6v-b15uDoeEDm6p5Uo7OCv8L5eE2f-0NNYL0UpaBoncKXeHFIHgGjX_HO-FhHyi9YaOKwIC409FQHfL71-NXLS8Akx-nirdOSGL1XP6G_J5xZTDwve76vtD_qdhWqRR1sJr9-_j5NgZlvfYKUIpGUGWPlbn1HlXQKrunihqWsk9Ws-wT3nRHHEYvgkJzLatFXhHX-1vucYeis-6rmfwjpj_yn538AyFepIQNJ5FiTVYRKSHFGJ2ASt-fu3fdhE3E4G2yJJpIEJDIyZhufsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMfta2rf707BYOUWXpMTXd_1yAznNEtSM52QLdqY15ZAuEqPZoJfMF9lpcjGMcgz2JV8Z1OL7oZTdu42x7hWQyDnrqCyDSsgDHYmqxG52WvCnO81uYtscnRhmJFZSnCEH_ZiOefKOiZ4JR1NIWvi_wNY139uHNBg3QcbhAxlpFi3mIC8zSDO6u7-mZ3FDlLfg3Kr7-N0XTGMXNnjiQKtf7JFxVeskGVXXX5C2SozB5dRXfgGgxY4WL2Hwji9SleK5jxBjdoDiqPYCKJXftBu4ch--PXlXJo3YUtusbZSJnBmu_TQkSd5dJaSMDlpXT9r74wmBosISinSnFZn7bZiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oejTsgjtIEBbDQ9ddQIdH3g4eDdiVJPiywmxeYvZ2Vnx9TOzFDMYjj0nniciIpx8gXqqibb7XpshyqaXfYhfYoKIBiMi9m2h_H4h_w4CAGvnyyL69ch9320xg3LfHaOWaTWlBTlTvwW56Lte2oSzYIsO6fgnT0TUu9d_CK89hY8rytBXnCINfhZG0sJdteF0klqJkRtZel-nF8RoAV92DRwPtIeIqVs3jZyHrXHSmIJPaXOAiU9Mac1Ri_sw_cFR91C0_v7_ldcQSTNbQ79Z4H2Cprr_vxxuNFjtzGi04uFvtSe54LhGftnx8I8PJ2UUVEPqp-aVEZwAt8h4U4c_qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfdDtCczcspgMAgtCHzE54Zk4Gnzigr16sfpyNIOKEsiHNBdoyWfIBud9EdCVrful8fum7H5dDUYi6tfMNdQO5U6f5ou-qn7tnK3bpEljg4i_erRMnuEn5sajpWXoPXHLVzb1nXQAed9jcChR-Oyt3sGNLapSVQ0n1iE12hRTYHrsSAQC-TVCp5UIovmdgrTQsx2YCnGpy40iygEe7qOXWFbbKmLCtK5cmvg-HDCFEBYkbiCvXkfHR7ETfTnmGwF261vrGUe7vsiLkhR3P4V_xZjpXBjMhPnaJKpVhYwgvqN_ue24G4r5hIvSLj0QMYX3Et53pBve0fqCAmNnO2RLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZxI97LvFHFW0AKfTXY-lDXuc9Kb1SdyYb0zVGRlPhgt3p-Jz3EsyWmkqYEmTkcxqbsFrDKggDkub8WgjUIJDKQSX9ffJRRg9F9USQlYzWVPeGPA0UCFXp09przxF_ZF_xZ-5Y2y2G_xm_-O3dVi1j0BQxXyzuKg4dxUbHetDvmUn7-T9qodXFOnOdsvY_MmLNIgUoRtdv-jbKEhFH-a-bGjdFnDJXwFDAarYiEPBTlgHR_-1hgkhH0IfVzaVK1Wc5u7SDNHeOwR3sxc8TYzAhSGhMjDmUBzELddTzVE1yVWk8NvKNJZGr-piMbgfRTWryTNGOX066Kl6ciFUnE9ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKpNcOfBr-HNYP6flcJZAVIVvDlVRq_B7SOXKgS25x5K3pVwbKVbrnzpBX7phmva9iH2O72VdsC7FBh6E35j3fQMwe8TMUVEe6VVzJ8gCQcwEe5GTLegJdUH7LHRXbKqrnGBbPMykOY87PcudRrDl77LzJA8xIy1HPYL63Cq3AhrDMHVDY0s7FCEttKzDpn5V-ZVfK1c08CuYnaPI2hAhihlFZcSd1YfGByUUn6ZHBiK1QEuk8hRfnH4ewZK0LE142uFD30_ZI5vv0BP3sVgADfguyJ83snZr4G5-cdTwBIcsPEiAS3o3pAwospi1wO10N_HLm9QgXOkFfUnmSJ3Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvIdrc1sjx5MRB6aZUC9UDtFVgEGbWob2Cj5vOZ1CCk_NInwDj1qDLmUJdlwVeLAI2TMuhuMN5Yl5lv-xaB630QQsK1_KxhTybb5IFWCOFqRTibE7WgujXeEC2RqxNqdM7s1VC50DSUmVqFNYAhPCQAqFNRdXiPskZErZQv2vEWyzM7ioOS6C73qrCjFuS5fiDvIh0JaCOAF1HvHKWtzJyGaZvflKJgU98NkOL_AWPi6Umex7olu8qaQxg7n0LVYQTrB7S2RuX_RcozxDyaxz8MZ3Y-WqCr6xlzzd7KVT3TAyQJN1N-RcrUbsgxcWOU12USkGLOIW7VqAmUY2mBxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xth0Xr8QAM9mPj24HL0foHhTWlTzZYFO_EznMu1rmbpaou9Cy46Kf8ETqNo9PsrDGoihfJa8cuLa7y9JfPxrtNGgOD3liS8ARMYg3m7ylST_hBXlhv3KLzbn_nxNAIvKT0rCHqdrXSr3DQzhC68wupHG2lp3N0PHYAk_HZaU3KqFd8-u-hVfu-o60Ls_KDW7sT7X6d7zGPzIuquCJIsja7vxWlJb5ll7z-u6E8YCjgPCGo58NUQWZ0Uzp0NtZA3V_dfCCU75-_fulTK41kjAW86yv8j2O1DHNQJ5EKkjCB2HB1v5YD9H2rC_UNMKf5WWRgE9qkLw1Tm8EYtx3PYyuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfZxqAqnpSP31S63ev50sfxEXv02cyhjFGiZmQ2bJ_bsME3ZWuCh1Y_gjPjaLQIObhwTpYP3MKm-FJnGjcL_i96sJISGqOyhHTgpUTF9dYIjZhcbZf4cDd_zfHiCR3Xtd3wa344fW6FVHiD1gaAlr3XAfs8tKEnDyrgNZvfWMTAdsardMKY8eRb-R3GiyvR8V9kEeI2MqyXXfJMHr_UoL-cz5LEp9S3G94Rz_NcjHplOyhlG04ELYaC0ODo4w_YyPHMLAKMD1HjTXIYAIpKUlm5yXnjgBqN_Ba52oXoc5-q2TG0JgnMJfsNpNyGLUlmQppUVlYFmw4zlyP5ELWXhbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trq6POn4zAyGyoeBRb-tDjIhLdAkl9icVNCDztQlUp_lnlV3-qGc24tBM5fdQ7nu1sXW1-H0okKYaBQoJ0cMg95uNHkcHO_XyiJ-YzRPgHkpQbPkWL1gKuryUCnxijbJkAmu9ptg35MAfzLuKaaYERJl1ccZNHHgawD9ZL-xtDS33zbp7HV0LIP5X4k1dHV7fL9i7k1K6zUbzwe9dt3vt0nw9k3O6c-wCuHqlJt_lkb2C2YUkuD05qawkOlQQB0CqiE6WuPdu-_9eNk-GUAjbyIjYBEcft_lAbl8tS4in_zqM1AozjWmX00QpNaj336i9VMV7-8o7avrTrkGakQNww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsF8hgy8odAGtGlE7_Bh3XGjXP-9hR1-H_keu1jvc1dIe_ahFkhi1huZmC11ojDmtXekkwSr6z2L_P94ViVkTGSy-Nx10E7I2OupKu78XBg5NJdulBqsleV80DM_-L9FBpUsjeSB5C8yvghtHXqFQHHc7lg2gf2-HE0pjU3EImf2jcJnVLBonU68nm6JrwSQdQiFpkxAjzs13s86oxwtUyBAMywj6WyRM1rTM8HCwyh08e6PmTuFYDNF2hOSCg8eW3RXyRy9iXZuJ1C4SVFVOdV9_4-zvStWoX3uSFQr1sFBgBcMJ9vLX5GRKAbKfQ-ImyRtI9ObqHbU0q-Ha9vyhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH3rhcA0xEogzmBhOXKrdaj5oCK6za3gZb3ijICH-NQKJhPIrR0FRMAITMPrRR8fK-NI7DxVIQv2ndsyx9OVOGPjBrMDFlBwxNtspwL8MTCr6FIbUijIppT5PP3Q63SUuKNoFY-dgwqjQlmooSvpDR4HLxZ2GJgMellZ9-yrlGmKaVzyV5upBTCpUn2JyQ4UGGIneCwdoYeCQPgTTyujiKYDmOeuy5PQ_0G5oQ7rWzm00vK-tT-t_BZJw1ErtCLEMCsXg73n7heMaJ6ZZzAh1Cd4Jatg20enJI5KCYBW4Z6EtUKCVr9DHGNwbGHAZapqi6LsvWIqsQWS3kPXgy0syg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uSHxttPqXlXGHHJEprv8fSDkcGbXjmlFbAfE-BjyjpDrrWJO23cnyEbF9anvAG_pkYLez1kgcbq3Ji1OHuo1HFLNNZe98_DHysXnndfdfMibZD4CTCCUrrBUdSOSC_r7Fjm6ngXHVT8fQine4cTEPHPzGibWNhFaxgCKj7Q-1_vW32PypsQP0AhhO13glzdpZShmRt-qlyHhS21dhxDoYYEjhJUSGlzTEAKeItyYnjgDIkYLUg9RBYU0l4mUcWaAxz8n_UaLa2b2dXIRmLdBwjyoMtqs2oJNlgliaf5ZpQKFyfrcNGl_M1b2z0tzro4MjBXdmeSCqrjWbsvGZhZ9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uSHxttPqXlXGHHJEprv8fSDkcGbXjmlFbAfE-BjyjpDrrWJO23cnyEbF9anvAG_pkYLez1kgcbq3Ji1OHuo1HFLNNZe98_DHysXnndfdfMibZD4CTCCUrrBUdSOSC_r7Fjm6ngXHVT8fQine4cTEPHPzGibWNhFaxgCKj7Q-1_vW32PypsQP0AhhO13glzdpZShmRt-qlyHhS21dhxDoYYEjhJUSGlzTEAKeItyYnjgDIkYLUg9RBYU0l4mUcWaAxz8n_UaLa2b2dXIRmLdBwjyoMtqs2oJNlgliaf5ZpQKFyfrcNGl_M1b2z0tzro4MjBXdmeSCqrjWbsvGZhZ9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxq1ZZJ6v0WW1Unhg3P_-pxCRj9-EJneZPyKyFuiGt_RC20pfyUBPBHSFNfLjICxMCU8Wrg2H4J3LuCjdydbFO8gJZ8LNwDFmPaykOlGICq3fFm_vP-LnGqUmz2KRTU6ZuzGU4zTHM3zLUPqlUwBCf-F81HdIItCHtjdlJJKbau7HyPcupNbGnbyWkCjS5lvUwkhlmRZ65Jfh6MkP7MvGd6XY8AuJIIyN8OWf4TObQL0_tVU-HsX-PJWDcV7EHeJ-oHBYp8H6JOCP-fAu-3Vv-s0D7mK6hiDx_W4jJHTbOcR9c5XrgB6_TGKF0OYqQkZqtBKJKOye9J1P_UAsBTjkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHZHq18r-VsreGUbHGnfq2o3R95T-oq0lgQtThR3POPoFlRfCucOH9rDHssfZhs6kiUU-tW7mE9MUe6Hct-ny5JEQLS0kydl_68TszpjxyKgCA7uSDt6hQsGMkpHgQ_1PEIjyeHd2ELuCmwYvsduTp-cNWIOKOBXJuizj-oDVjvqeNkg7DVV1yRWLcAJz5uQOGlmzMsGPI1OrWmtG15MesyhvxGzcIv2THJNpvLiNz3InW7cxddfl6IobrTbKSaxVTM_XW7Q8Qhod8TdgF2ZA7B6xijqTc7lJhG9e_bDPYaGqxCAzEoKDXfApcyPnMjGC1FxSIpGRektkCdZcfBq3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LktgCPHZ6m8_joPTitlLP6SDp0PKNCdTfrRV9DJ6WfPGMsEQBhjgv4A3f4ovGbM_WoSjAizIOr4diJnTVT7wqvVQ3dOXHrDt1Dadjp4ch-55fQOH2xAHdE16g2ZZPhWnsAKM9QTnCD2QkrFWZlDfI_zNeDOdI4XhVpEMSmI5x-DN_ww0Mx-ZEUTRotLyPyW7Sk0GKweojoaU-1ioSu2ViUqZKMTulQTO16UYHHrg2WcEuvQykebaV9A9QJr3a4TvKQoklCkggfcZ9Tb2cCp5vXZMgNyLw3lAgjyhcE9Z5rUMTrqSUwNIXwZnsoFPt7VIZ9clkFMDkCWWQYbvZauusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSETdnCRCLKvHTbDsxMtSfv3kgzB8JLFS98QjsMWs9tyDDItvc3jSYJGKYismW4zyBYZnGKtexUvBIdfWKKmG2eBM6JMlRrTKI-7bBqK_2zdXspOBSUElu3_7zjhgxQaLj7VJnDiuQ5DOW_SE9spFeVvI5iuhYivQOlpCUgHFb3RUAnZ5lHAC4G8z8znZn2lBamty9X5xJTFkAOqAt5iexKkIpuqwJnpAVW-cMYuAahjhXGhd-OKrZMMuCGD5qyd4xmGu9o4Wc2cXJ1asalswUhUMMhGplmNJnjoSdXWLJK9x5aEr9fOjzPPTWzhSD3ZVVdtq2hXnI7255LrjuhT3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKBinshzF9Ap-RzICHY7zzOtrejpSw0t9pbHR-dMKacWIWnUteN0AsnLasW-9msAdGAO_7-3R7e6Yd7QCt1gkFPekkz9LounHkWDtQtJwl24xfvaryaI6YTZcGE4glmc7c81Nag_rZP01Ff2VWFk1IFSfeYSaj033HN8UanIBDMUstVAuHtZRYYAI1n4UNYsCTKwYzh7kYxU4P1j9blxpzQeyvfdDYJRDSSDxph18Y_TlxUMFNQIgKf3PAVtUCfj4cBwG8UD-1RVx93ZORMiLW6OTp_NZnE1Z_5FTdrh0D1u6ScLbf9uk9k4fau_KWO9kaP3uYT2eN8I5EP4FMTfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp_w8ZhMQhg19T4wzJ1YF-dtfcG-D1ISg0CpXbgOuSBu_QqoGrHhbohjso5eGcxhEE7VZp5KsD-2xgmOe2odezA262mEGRvWXp0ydPnrZp3EzeDJVu19NSBpxTr6y9xMYAR6HlcMhUqB4ufy-HOYTEw9quWeHlD12G0eYx9VxYDyB2hwf33rFONzUIGArUAjG34n-MpZ8zkPL5mzGreogi3KMTQkjbt71R-SgKdhbVOFtMVam5UbWbJI5XKCul1pwIFvSy7QOys3MXDvF0KEs95J0xjHRPJSWY9LWlyJWfoEpg6cx41YKjaqYmCvNhJSif_XArZXUcM0SET4_XTydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4y_pTXwDaT72WogwgwQDPzL36a9jhGfsgSDg7toh58Sgb8vPv8OUx87A-GahS-JiVYrcxv4X5x8K6Laf4HdSTOfQZF-X86bYdXZ3voATGQMQEbZLEUkUGr6atXOcwb7VXcti8yXyF3D36Qh3jqJsSR-H0OXy_2WubgrjCputE6ydfMfBpcW7MrHem15pK2kagN6ZHMIijnhgfCVkSEXANfYC4_sqIQIcqZ_jfXxXH50gcuQ9XsucRZJD2ViVHDnRfzSW5W_u0855xh2XulgjIrvjuSAz4y6sEkGxoLXRKvgIrVoLX4L9RvU_fp6-r6HgESb9rUsm5gjy3KIUTfCvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NlUUXOXmqpQkZWP_PunenqE8aQtNW1jEsck3tE54V_nAwHSV32FUyjBLDe-l46NozExrhWFHcGju3hMO4vlILFaSO1n2IeMwQvQ0pRXcvN2rtMF4jzyzAIOTJ7B7tu7zxppbj2dqXTv0NC9OAlHmTBFL_Xc-6b1JyJauBFnZCrA5dKgLp_z3sKm9Ojvz--DtpcBav0iNcOUFkpNZcttI_qsq73FjPGwLie-NuULWImCnRI4c5G2Gsed76D_zW6rV4f1oNqALxfszxQPYWRGdUCUGishapHOgPj_qJcOVWwX_LPPQk5CziINV457cVSudrqH-jxP6BDmNgdPr2KwGHrzZKukgKTuctOUgINQzAWT8T71X-nZRYfK_WneJJkbsKiFF_zpsRIXumYh0fbNYzjZiawTeBoQz5TYKrP3xAR1loVGbTE0RmKtIte4CdsjBDvXu17siEeXSHhe8GoqVfs6oW-Yn8hq2tKy9_kRilqmIONFeulVvYrHg2J-9n_3dGfNdWboxQRNIFJzpwC-ChF6GocY-w-TNroYQ7bbEcMj_a9J01Jpf9h_wXPc3M8vgNn4kK1OKUyrNdBW1NnasBACK7K7BkWaAYs4EF8hhmwOUMAihgtKGrVZIdn77uc8ipdC5Ve_wx1uMatl4vU4Cd_99AAPZVkSYTdO_CCy_gU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=NlUUXOXmqpQkZWP_PunenqE8aQtNW1jEsck3tE54V_nAwHSV32FUyjBLDe-l46NozExrhWFHcGju3hMO4vlILFaSO1n2IeMwQvQ0pRXcvN2rtMF4jzyzAIOTJ7B7tu7zxppbj2dqXTv0NC9OAlHmTBFL_Xc-6b1JyJauBFnZCrA5dKgLp_z3sKm9Ojvz--DtpcBav0iNcOUFkpNZcttI_qsq73FjPGwLie-NuULWImCnRI4c5G2Gsed76D_zW6rV4f1oNqALxfszxQPYWRGdUCUGishapHOgPj_qJcOVWwX_LPPQk5CziINV457cVSudrqH-jxP6BDmNgdPr2KwGHrzZKukgKTuctOUgINQzAWT8T71X-nZRYfK_WneJJkbsKiFF_zpsRIXumYh0fbNYzjZiawTeBoQz5TYKrP3xAR1loVGbTE0RmKtIte4CdsjBDvXu17siEeXSHhe8GoqVfs6oW-Yn8hq2tKy9_kRilqmIONFeulVvYrHg2J-9n_3dGfNdWboxQRNIFJzpwC-ChF6GocY-w-TNroYQ7bbEcMj_a9J01Jpf9h_wXPc3M8vgNn4kK1OKUyrNdBW1NnasBACK7K7BkWaAYs4EF8hhmwOUMAihgtKGrVZIdn77uc8ipdC5Ve_wx1uMatl4vU4Cd_99AAPZVkSYTdO_CCy_gU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6iEmlSun_unLEg7ci3lW9dcICI3LRetT0kmn5jJwHm5xLg8llbwioKTIEgC6yEnD1lM4aU8Sw4zQocqf6oTNQKV5Dt9yNRdBd1O_Zu2-iIFMk0E9Rk2A5uIV4jWvFOZ3eW2aShqUtirXXPi28iqssepHV3tFwhmo0MIPqj1x-Cqnkqjed0GNBB8eov3cPlSRhpa7cwZmCEixFgkicXr0E5vU2zWrlMK0Ob0L8L8Wki9ukLvNclqR3j82PdahyEz1P4vxATXaMTEfgc4uMkq_l_iH0z16BQuwM2futZ-mwn1WGgY8gvsErFBTmIzYFKCeUU7kxVzS6_NHdw3pMABVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzZr1NnfAZexJ3sgP6zn2R6kuuiVeX5Y67dx7DwDOX7C2tNlbjkRR5BK7mbXAX40upayWfomlyjjjuOnmA6LVVG-nNoHrOWqNSYiH85VqlZcciV2O3O1ILpsC9VmxKcGg1c1Pg03GDlEUjVPWyjJxMU0MuoPf2HnAd8dYnPg4aJNFmVnvlelMTRmJxXgDH05xteiZxX00Qd2ztGkInZhZy6BLcQA-SUb8mrGIX1Ueo0L8A5IkyUy8_f2M7JD0fvD2LrunnrOV8qKOKh6AgVVQAY5tytTuQKtaAhqD_mNgSqlfvlN0vIWVSlQBiaBW_Whbq6Z55SjtMCbuKLyAH-_hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvObwFTy_YH10RhhO8yae9hkihsggpXenGZzWtZRZi35OdP9Wb2A052I2sw2YPuC_8VdzWuaUXdMcBG3fRv-27qvEYw6uU1XcMzv2kB3Ygilamq0eeEWzLtEpWw4H31t2MbT26VNZw9ViuHYZRul01GU4LdhN1kWjDmDPuWSDiNApOy7bBX868PjV7ZwrUw8cOS5s8wGiCt7-3ZTk6xLjydwXa0pb4J9jXVn7U9PbbWyv4pl8oziehQRsjLK8mmI9kQeV4AjkIRf2t2DDQTkROdVoB8sA9-61szfRWTZuReJ-gM760a8D3IFtT2N9pYD1XmizJpF00-NbzJ4uaBYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpFkfiAoK0ToNapCqpC3SKeqh3KKhZPf0ZC4Y56pwjMjeBMAaBlZ1McgdneRw7wKVTshQjdztUVNsvoV1FbhgX3r_v1bUrQM9Xg7RyghFMVkw5pLRHU52EsXQcoWee2YpYv8bgtr_sov_pOoX5IglccQPtaD-LQYNUSGJDX2hTBFlVAcktEv02EZEwIIPLhvb3tUnJ53h2geedRDiiofv2YIHb5Ry64bPQb3wIw9X7OWmwYowVRWn8e6YhdQGC0C-sq432njDfLH44Ws_3eBP737fAOTND1qMW4Yz8MIAffBsJY8v2nIjV0NuwJRZJp-2h4eG9ag7RrYY8zn0kQBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzVl3N9ABC5vuhr1CoahAOeMTuy6mYFmD3DaRTYMCFWXDLk5j_9QBvidF2md4iwPOoeTArV947AC-AehPWMqz9vgewQ8JUl8abEzX2f64KOkshaLifGv0evRLoQsj3Q7m-1EEtFFcRAczLffnBaJSCtlFc2CgcdbYXT_CzjdkfeAwpRvaH8GcghGkv3AHNfkH-g7lNlkis5L_DomUEw0TGMaSBUo7o56ouMAmvWAKA6VE5s2Sng2aD6teMPcbIuTLfSqcABXfAWCzr7g5yNVodBLLt4yde5UmNnIPINB2cV8jMmYii7wu3nzkwcWyQeOTKWeTJmWu0Ae8v6qyQHHtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0b7iv6npmAbmFx1-BwvjEW7egu3tPel4RwavsGVHA0OHS3mvel1QCfFeN4Ro452n9bY5WCf9cAU2WEj-uPu3cXXLI_HZsVayUo0KgcmOOCexJuGTiaE7g__-iP-cfdUzXn2xXOzjhUOvKMMA0bVXUN_gutKXuUurNSyeRVNIjpMQRH3IXhWlqVPVD1w9X6O9LfNTgyw9IXo5pE-lnw_hMpyBTslKrGVHi9qGCeeKdyCBuK_48arnq2EXJicAczeoGv6zFxyXC68eJ90yam89P5JKWQsVeBFxqp1RMezaIwuCRqulBIB76RINnxVbwVO0KaqCvsIWdYrIjcrkIb1zCh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0b7iv6npmAbmFx1-BwvjEW7egu3tPel4RwavsGVHA0OHS3mvel1QCfFeN4Ro452n9bY5WCf9cAU2WEj-uPu3cXXLI_HZsVayUo0KgcmOOCexJuGTiaE7g__-iP-cfdUzXn2xXOzjhUOvKMMA0bVXUN_gutKXuUurNSyeRVNIjpMQRH3IXhWlqVPVD1w9X6O9LfNTgyw9IXo5pE-lnw_hMpyBTslKrGVHi9qGCeeKdyCBuK_48arnq2EXJicAczeoGv6zFxyXC68eJ90yam89P5JKWQsVeBFxqp1RMezaIwuCRqulBIB76RINnxVbwVO0KaqCvsIWdYrIjcrkIb1zCh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSbdvjY-Zv_hy_zYPnEk_f7NPJNhQziZbmAy4-8Knoc2n5aBDhec6_DTG677HoBJy08Jl9RcyUwt9rRaLghfax6GKECUVsHxpAkslFY3l0G4iqGXauluar-wu7jxP9_3YjWhh8_wwrXZgCMt3AGXNYs1T2OaqpDE3Lote2WM2vLB7wJDnDULYRFSXyHB2WQcsyUPE4bNLhUaZgUOzcUFfcQIgW-fcsTdlwdwl9NhzpDAru7Qgbrcp9tFoXy7rVPWflKx_yxx87mSypnImSjj4lrWnwWU00Gd7KsNw-b7iJKYWj2ZNEqEU-yNvFthoqwbrCiflFeC8Ke1bethURRtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
