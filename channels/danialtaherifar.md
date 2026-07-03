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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 246 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP9aOn1physZNsINVAVigTg86GlFnPguKG-sgcH317VRxuqlbPUaXks6xXmyAwxB4z649ylwm6ftkSqD0zXGBvqGsKCnCDpGEruWcu81e9khGwPOAqZHUq3Yv7Lke9fthYW_ncaxyXnEU5LgspTmqiULMP8by8BEvqKNL_HKhhh--j53gv9T0bd6W_T1GCH6pFME3isSY2Q2omraW24LZPTQ4J1-vhXK87BoHWuNYTKuD1PL-5ZqJmFpWU6jizUoWwCC3l_qVeYRtyqPLod9QetJ-GV9lbfnn8CNkER_jMQD8G4XDJIj53cx9Tdcnzy3A5voj1-gWjQxDtnwwhoc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 482 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=XR27pa-q5vO-t_8u2Ai7rMSHEeLH5Lok7ZkwRJPJ9-c7NETesxoVCVaP4b7QwzKjQ6UdxB6-rwB2lRisHix3Sx9IUTImLyvUjBjf1QgkHVKMd4sBVE3fmfv3qy9ESZfHoPya25tdOxc7D2JJoUcHuY9x5vsuBqR7B2_-KOFqKw5_t7qch_JHPSeTo3lTydWxH3AAfm23MbsT1SwkGajiL8WGZE44b3lcdmmWdQiD60gAcmvQls6Bf90JcOdhYYZ1VOEzfYuskIv-G9J2ybfTpwk1WeiqQvk4KzR2CLuLEUm-BOhYhIHl-_hY-nkSQpebO8VQdzt3FZ5CIu4aBA5Kuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=XR27pa-q5vO-t_8u2Ai7rMSHEeLH5Lok7ZkwRJPJ9-c7NETesxoVCVaP4b7QwzKjQ6UdxB6-rwB2lRisHix3Sx9IUTImLyvUjBjf1QgkHVKMd4sBVE3fmfv3qy9ESZfHoPya25tdOxc7D2JJoUcHuY9x5vsuBqR7B2_-KOFqKw5_t7qch_JHPSeTo3lTydWxH3AAfm23MbsT1SwkGajiL8WGZE44b3lcdmmWdQiD60gAcmvQls6Bf90JcOdhYYZ1VOEzfYuskIv-G9J2ybfTpwk1WeiqQvk4KzR2CLuLEUm-BOhYhIHl-_hY-nkSQpebO8VQdzt3FZ5CIu4aBA5Kuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIJrMBc5xKW3fDDZbNrxnT51ct2vyf9milualbrbLImqTXrTUv01ZwWXpRf5XAQrvXUmUuGM2fM7Y9TtnRYpm1zaBwqhaDieawGaSoedIKzr0Ser6RJmRwGRPqIfRzYgQ1MkeKdBYiZ3g1-dHW_49w4JOWWkACCWudDnKs5MwzgO3C7QOemsiEgUzv7VqBo9-n6tvDOJm3iPOYR_j0T-y0M-VG9kfSrKE7IgsNQxh8eh_QtbWAwTN1ZaKca12pGKfUV2WD8V1KgIicge9TbH3k_KqW5-IgDzz8SzUBup9gBxVFMMjTSva2Vuw83_rY56FDQWKRClpyUaDBawr7hAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2UgpXqxQr76Fk2JOW03M1q8NktX2hYOKdPKXfK_0BQf3v1mf9VuEeLqoRVyJhlADCOiVxo_RTurT2wvjzZoxT0JhSBI6Lgi1fNFtHPxrSaYg_SqUwgKftgKoKR11bKhRGmeDKdR_2GBy36Tc11GuyKFZwrGELq9Eu_lUqzDtsK9DaeOhyTDG8rfhfU4GQqHybdk7MvXZhPnge6jNUtsBroaqfyHPK8La5TQJHGi1zO6AhkyiwFp88KkBhTaKN8E_VFDRyTUzLJ_19XDVOiJduMCjQOTYcnwXdfD2nMD50MEJ_6PdP_VjCYwXFPOHwYJ7JYLjucyHP5QprFYjAHYmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDLXpJHYj3li55TbsUoZT_0oGjlnNWMS_z_UodCITGjqVrguxy0GzH9iZ6i-UioWhNhhBLEIlJJ6bxGTbfSqQl84h1JDU6xrltfP1h9H53QH2nKjRCZTlyCrMF8SuqbMEuUn6WMf7mOwwfkIYSRtqfZH835vSFxlwNC8XVccE3C6oAKeCZpvK3HKyQUf3KKa1v0sA3d3Pz_oVP6PkivgeRQZggW9stJMMNmNa31d0kk4lTpcQu8vCCCgSjQ1IjOgKRNL1Junm1bPBcJNA-_NhKAuWmR-mNzAF0m7AbNolwxpSgmnGDgMOimeVpHsWXeJ5UhBLyMsNndAcaDQGkWMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EusVmgZX9NSmnFU1OrHJZ7L7CAQgWJ6LBgGpGHkPQXasyTXxLXTFSQ8u-185bYoDE2IWh9d6lovf_0jv8K2Ig57LcxaoITeG8jJmsUOg-Ye1kmU1tEW5BqJi9s7iC_zaPPHckZHjhzMuFnl5IWBrfqal_95WY58UgzYPvNvGZ8XfG9Wz44fK_V6YldEMelV87TD79lnSyqjGLpolnv3fVs-REIWnd968C-ColEveRiMMx3JsyzcXhMUd-K1lEirAgfoI9tXiN-Ym2G007jQoiV-J1R_S0wke3VHbEEwCE4K-CGNsxydIKnapuMYVOyHM9e7S5lS71r0DuvqJ3viM-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWSn9m3sFSJxJREpVObuAp4FOrSfLpv6JxtHFiDOCXT9nVP7hHjNiyh6LY7qgbXNUu_p8ei8MOAsxQLMjz1RQsFVoTuMgrEPR5zmSiQUQFna2u5maRmgxNFGAbmcB0sqL2w01dNYuVlczxjTz5YdzaCZfdwe4on0X6X9xcnfXXlBCoDBvzUzG_1MEEGZAdddAZ70_zWpX42sXdMN8Ei9YLa5NEO4_a0OzgA9Fg72msVawPQG0RtluCIrV72MWnkU5dfMSqcp_D7pAOSuAXQDNCazI7iXAp5IdlFOwTY2fUL4W1n6Ma3A__NNJ_bZLTXIe0xmUvQ_buksqHe1Tn14MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXFPxzueyBFR2qdMmBKt7Z3uRvqYC8SdPKQMKiw7NeG8th7zJ5LpC8yxRiS3dZKonUgSVdwYbnxI8i_RqN0ek-lEFVoj5EjAZMmnN7BD1ovGJ9J_xeCxIReW34x8Xvm968PMtDg8-AZE6C-EwAUSnuNnq-j619iB_TxtbKn2NDyVvy_JCMib66xPizlnyobUbcILm33P0dtRF1jan4TgDJl5mtrbZwRqLSCmkHnuuxdo1YaY6xQ242PYCLxt1IEmleIh7tg1Y23roQMh6Brq2mncqDnbKeqtc6wwm9vdj0yqpYkiF7XIJTlg5QmAHb44tYmVl8IH-goWVk0zqJopVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXq7niyekYak4oQmet20YdswmZEerKKkDDAM-tsa6osTeIfhcrN6bn_JBMtJ50ztRuzKhRJ0FfM1knDnp4WKQIuHuuUUEOW-RZnugv3iqhpfOsXDeLaxxxToUlHw0JITulMWvKAFk5V7EcsZSFxP35sjB1HKcL5yDc8RwsFdfqPvooujc-Zy3FX_YjebEy1poqhXp_pis2JWMgR6sDQmPdzoTiBdzgq7QgawM5OvU7UD-Hf9YRaLyVHCGoTrl8fearsgaeW9je9qtpQjOXmMKDXetyasPAdFK4Fdcn7pn2RhypdoCGM7jJI04dQcDvK10kieODoDrl-hLyxJHTHg8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FodeVCaMzeL8FrVhIhrMz5ip8-te8uRsk7Y0fZX0vbsKy7P4_U4lh68JiFfwHGeaGET21qoqgR77blKximik0sG-M00whn0Z1a8Q6mfdm3UKd2NNFJPAxuUOP4aeUHIRRUud3zSKFeNhobd9oq7vShsBMGkw4YLcSKP5JspTfUQqXFMhYe3sYrgubUU5NwWwb1mTg9z6YBIVcTcUk4PF1bPe6FY3JEI54-s5TXpzJpayRlhocaXFq-sOPLLuaVG3eFm4p7a7UcZF9mCme0kDLnm0dTC6zb5p0s2eSBPu4i_8gesE-zQPILltms8HBkjXRvB4bQWhIMV0IDbm5KkYlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0hamTslAWtAABhGYK-IPFicMG3wf4ms4011gEjbpRjLoX3Pe1OOxrnnsNDd0Pioh5c9CdYf7GGTyuO433-xrYr9CjF5aT1xcqC9lqgbsYBv9tBF07FjTD3B6VahLYcfjOlI16EjiSitNVW65aF46BSXSmKcuxpfhm6GVSZTYNRN0qtN6HqEX6gNwCPTlxUPYpcdVA9fd2whedtrZTeKITLqgNlgaUJkRAWj-C_5wTXG-32MRCxUWhLeg42wljj8KuDGxxzbaSojyoAMjF6GbVbjw8qbdZUn7QtrZtBDMA2WRb5nSCDjWLp3WJYXIrXsggyHmaDsD5xIau49K7JwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7ctl806v_9Od0GLQFRHx3B5VXolf6pLsMoWK-dHWE7H8cq8jazVuJ8zy9UnCfCjz2o069K8FS0NMAxYcBx2UVc__3HRO51vZikU4MGz_SFHyE0tGyMsnXg7iSDolbx29X2yrsZtIkUl5UeOy_DzO--_3-Lsxkx8xmjugxRjgt_sJ4iDImpzqY4fTewUnFz3gzB3nh93hQfeKcTwoXTe0t64bdjFFIGe5LK9x2liC-iTPxf8dkLuAWbtEntBvuQH0jfa4MJ8XBzUs1y7ux-aYSK2S-oFAq593Kq7bpEB2OPF9WDZU6fthqbomB-vCSH70ISNrBk-4yp2pfpPlIOfbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCb0v6RAKYtv265SRXqLhvTbCtoGMq9BHeWLlCFKXAUK9hBNccLUDFc5tfnaZFC7GVGookBsRfYDaWQ9ClQ4N0CRIXvHUcrLvroQn3bV0R1wvGR7YI14eCHcFXI2Ft8JI15ftQSua9M-OuUlN0aTY1CdRsj6e_EcvgRfD3k-jV6vGqyOKzgsUhO5ANjNxTqlOthMvDtS-2XTNAr45APMItP4lAU_iJSF6sAT9RU2dhUW0t-K1MkcP-mbIDFy6pcNQa89QuDbQhkCGH1FPrHaLmQIxFnOhMyqZfhlkgA6ctUwYujSMtJoQmbyYVSGZP_8Lexc8T6TG_UngZGOO0R-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COElGLhRN6cjpp5EFk-tf150__i4IOU1DVs64Tv-21zX0vDgk2FDetli00cca8oLujJNZ0U7IzmCIeciBZ3JZIdjAEaGuLFfUlDKXkcCKJTy5iAFdb8JYXZJihLDehbfv6Eiii-Cd4CW5LyB3Q6t57e5BnTWU-gFUO6WsVAbdmmQLQb1BkWlubWgjwk1kk9y7Dhbu_DdXbr6itep7Ed6ikiKWeGu9bjxUSSpovgx64LvAUa9hhKINtvneZztC3Lfvg2E-CL3Muf0eYi1ZaCFehPBMhl8G0vyCj3GWyHo0BQU3KciVRTi_56g4f7whhe65KUk3g-vtqsnERI7DtVRwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ58iWeu6RcSN9VZJif_otj70WHbTcxDIyjBN-I5eM6ij_Eg_p9n_NsSRpa_cI4WSXjw65uWe6oDbXZcLM01Mf6Cozh0vm1lfKDld2Ydj2RGCYR_aHA4iJ-CFoWdOTOxn3VgdI-w22u33QkdPfifu3gaUhD6-C6hDEE3lkluVGfYhJp44skcdDcC_fvWNA8k631Le5PBA3EFxf2ejRW6gQ7BVZsmo9zaGTVQQyRULKSwcG6o3Xpz3CVQRRwji7PjrlicS8l2cpYBOe8UTBxESCchhtq7Et5vW5FncGzTko-wNLCGJ0v-9SELSn0vm1GXfL_hvTxUKV-uFV7F6UiH5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=sDkPmVSRGDY0e6YGVoAXQWz6nlvkSmWcrSesbHM0CHuKteJk3Ekp_5eaEjReSSgHQjzGiTXDRZSqDevKva2LOkycauhLFvbV4cEbyPwzpgQmouyGj4a8xzIIOQF_wZ6OaKt_0g3mdZw9YTeIU-JohwpNsfJsWBcwigJMVDmO-YfKiCElx0zSmJqLdkjqtx20s1qPzzUBx6QOi2mG-isw3Cq01NIYUXLerbJBr1xSNmkZ2wtOQn7JfwxSmyAQsjhlOk36MPQxdT8oyXob4Lz0_hAoVCcDmYKRb8wixiPdToQUzpKFfhi_GI3z0aBlJRdaFHLUu8u-rf0SPnWj2lvyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=sDkPmVSRGDY0e6YGVoAXQWz6nlvkSmWcrSesbHM0CHuKteJk3Ekp_5eaEjReSSgHQjzGiTXDRZSqDevKva2LOkycauhLFvbV4cEbyPwzpgQmouyGj4a8xzIIOQF_wZ6OaKt_0g3mdZw9YTeIU-JohwpNsfJsWBcwigJMVDmO-YfKiCElx0zSmJqLdkjqtx20s1qPzzUBx6QOi2mG-isw3Cq01NIYUXLerbJBr1xSNmkZ2wtOQn7JfwxSmyAQsjhlOk36MPQxdT8oyXob4Lz0_hAoVCcDmYKRb8wixiPdToQUzpKFfhi_GI3z0aBlJRdaFHLUu8u-rf0SPnWj2lvyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQR5gSxpAAeIYgaksAKI3jvmJFNtK1tgmwgEdrHVOEO3Y3p1hto5N6LlrXZcGPI5NLCi6a12S-nChynTpuXLCsH6C_MUJMBxMseEvjnpOIwtg8YW4mgAFI5criGA8mmC95vsbrWzhAqDKAU8KhppOBGGOeNAed8bdEPeWHELKbapvNazc2pvXRm7cfbUySdeJ7n4prfdeOlq8n1SUsIkc1r9oPbC75wHZRH5hnDo7yPOrgr4jUNUt8DcOKQ1vF-c_KFv7BvBEA7zbzREoCEOU7O38xkoqFphc1Z0-aeSqq6lj4FigAShKKNONqzuxPUu_KXf5Z3EUw91wTb0UtNG9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nItrXRIqxL0SEr2fFN8RVLLcIvG434aRyW5rw-RLkoNvn3HuhTqwB82UNp9ES9IjhZQ--vR_RAEEUOHHv4RaqtZSoE2G7QoTVZ_jmhWcrfyqgNM5rxSQWmmylmB4KaDaA2x1TjWcx0u3du2hUKDL8gjISU8QHcGC_IFX5JvMdjf9kURGAJz4IhjlNrzQxbUmUOl3EQIvdTUm9cSfxDm-U9-By-Offwgq6dQWo1APXsWQ8z5fG-c1twEuCIb0dikgxnmaTEQVni3KwcLP29Pd5V8e4BzHXAc2_bQP-_ZyR4plD3MhxDdX2cbSpw3zHuCgrVu7KhtF-4V5UWAR8KyrRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzhUJKOzrqn14jP7CC3dxGXZ0uZXBn479s-1D9UPY1vXZsawr1tqg8kzk4f_mCuUxqQ1pH58aMcNDos38tZb444IJyyYq3sxV68OrzoK1SVsARSBhWoRRkgTFk0sxZHZNnGim2hgX2G-_NpDGsDXUXw9IoPmY96n1m2UTBU6aFGbmeJoujdjg8MOrN_hQXZoz6tJJOX3mJ95_kJAXvTLCu3aC38vwJw1L9kmN1sBNMdtXvv4-Qsl33XK4kssn5v_5_ACthdmYXWvV6QPJ1iUhtRq2VxjM8qV9KQbIHtXyUUYNTupfxB1b46us6vYFLUFzGOrVa6khwIoTJgvADBm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lywB4SWRP50FkFMOyR4n5Gm0ZFUotjjoh6yJrJVElGli4oefqmwr45xqLR6HEVLeo33bAdDLDB7yW-ZMA3fhqh6hw3exyR3byuHbraSlC7KhTOpjMgdOr1hxgzH9byFNKY_9IhxFqudge8GT3liGgKa7IQkjPkTxQKA6rTzhwBZ99Mev7ijCb64ndIexZvn6EGNKmIGcDjfqV2oIRXlpMxzWf2_4eHJAy5XMBvSSaTmjadRaf4ngvUY4PtZyRxYDhB5-bkd4cN8a1MamAY5hGpwnZWCWdRCbf0GBO5vSglItkS3nLrtvBZJtdP1kP2RwW1qPXvk8CFhW4dBHPdPNaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBrRhToUi_YKOSZ2JxF_UWArZsRsA3voJ_a8hOBu8wIrx6yLRSI9a1YhNisjFhNoDkVajtpvccDY6NBX6xeqbJ_Ec_NH3BvKhCvHLCJHa7HhTGS6fRm5CsSzu6J714ZfEnziO94EAdJNKubjWyShx6VgT6NiS5M_EfARUnUZl_gj8qzJmpCePoAL_McAeiptVPqMV7MseMF_s-5gr2GOTBqV2g1XdSgDL1Eieu8tZQZZIbK8_ykL8PQh6k3ybjMi2IUgUCKadaBCaHijPKyfsWefGSBk55YNu_xlKGlktb8gUYuoI5NBg_uX72Ssu1Km6Nw2LWKlSui3Z6xOqx9DcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwnG0kskyPO1Hb9SyBdoOvnnT7Cmw3vAc7grFsyxObjDaPJd5pJy2-sMTlD91Bu2rNNe3uBuEeoy37FcUh3xf6lZ30maDC0V9ySlsw-7yr5KEn9VDWgH-jgkoLNmyt6tF9Bsz2cxY7a5bVI7a9LGwFVBt6wccJsQqjMHlW1BbT0_VOfg6p4mJqXmyawiFO2SQXZJOHURIQ-PiGNVjlYGmY26t08w1NoRQ8L88q2okLG0q6zfOb0r3S-D295vcm9sDYGOvGxRnbsNvLfjS--zhClGdywelqETsoPxlZXz_sXUSz--TIW05Ot0ihXRzbAgPH9HUs5Z-8v5_qWiqLOWdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TajxpvPQ0u0ioUvQXhTDKvne68ykWhxIvg_y7AcsfDuT90ZTXfDKmlyFCS23ZDS4r4sH9pA5j-I0VXo4OozgXH6K51oaKoEsLdMLoNdRLkJkX2uPW_CPgljLvnPLPuC-kZ_rT3lYV1OTraNr7HLGuZLtj2v54BVXD3TnCfbhzhPolIBuzo-0_Ix78qYjBX_DDlz1yuawyBwrOFBvB7YTcfIhYR04TIzRXUo0TAZ4nlbbNcd56ui_qOOMrBEkIS5OMduC-pzkU0w1xDcW6L5kRePWQF9iW4VmiVEn_FE74xwBihSMQS-vt0xq6lrplbD0bmjVGHXZbK1ExWRW1rLB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTAL-kfskrqXh28zZ94HTBPa8NNUbh_Zs5TO0IxoO1lsLuNelPVB8CViI_qLsu4zgUmA-qPW4FWYq2LGU30sSAqqbQwhWnEUpa9qOv6WVsdCI27SFp4yb-FG6tBSwTHx2EXWvf9N60avxyaPOvw5Z2OVWkKyVNp1ycH-67ZKetYOW_GKpCx1MUAJK_klkdnGhuO4nXJQaDiO9W9cL1pkb0n_Vf9reH22DwWMtMFA8Nseg1pH2GwuFxbXfRLy7LseSC8HZxTNPV5BPrlYxL6ND8ESTII_TxRv6CfA4WCj2irbM-ZP9a8TibJ0e6VguxDU-tQaaoqUnN3IH36IeqB8wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ini4-qWlUM8LWlvnvAkCBv4q-ogJQr2EKPmjkmuevTyCJo_HiEqruVuGFQiJzRTXdnUnIEpIaYdLOVB5YNEozMUyDDiMdRe48MMrN3z7TRzcqFUZTMP2Z4yJv7t8mTxTp5ibGlTCVT0SrCRRpnc0rdqfatLNl3EAjC_nJyXeeeUXjm5OBBxyBVaSFpZQJGmd7bCWfuH-THut9XZYEnzdmpzswYFuZiKlNyuL-bTot1pTcvowMyDOvMB4Y2zpU9lvHQn3Y3VR8HwkzvpJt3s1QaHsWblu26GHooAFVeAQ2Kfqbu1_WHpZZuwOlXLfmWjKbhNS9AHgsJqOpF1co8YPxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhqU24PWfChn6FiY9OBtEZGysYF4k1NScAPRG36mdqkJ7YbnJg0p_0TmYzyOkKTC89Vuu0kAQYnYg10-5UPtPSCGQxiBQsBsYl5PT8jbzIsWIYZxwIvrZizDG_3tCj_d5GUqpd1PNijdbzW22ttod4RdelMtkrKm54pvkGKwCOs3ijxZ_uklbq5Ll25XipGdEeg-vjndFYGvaVtb4ESMOxpnKfKfVhdkCuq7Pg5j4eDyijOAQisQAqYgbQePZ0oeuHMV_zfMpwyU9oxOgpW2TKi1hA3jvUYftUcTcS27BZQ6f8dfHdENIZlqpN2URfJSO0UHJVJR7BETCUNup245og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3bkVp8cj4qJLEl8ZE4v6vmvDOw_-PfnU11rJRCWcCGU2bbLSGbEUPkZ9MKh75XVYJ910D8QRe2yAKD-xU1nPu1TdGFxEOW1sDm1WDzc6ydBB_Sb1-p96nKtdxdwJzkExdwVVWiRJqx1bnNG0DsHnXN_xj8_KSol7J2oYc1lWQDmS3MXsiQDzxGoquMpyPT_d_xr_AGJ_9e3ZCqxBC5Ewb5QsyvYZTVBmm4cnw8HkP7uEjpxmC5N1_mXAmBqutDVmPPMPLvl-DeK1gE9Vk7lqcHKekkBLfz9WBmSMbOWnAHQa7UrA5BjziZylnN-sxRsYjPEBGcUTUfpcvw1ZMirZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIysvf_YnuJs_qA5GTlaFvHXXVtEpOTNOQOdMoZYEwQVTl6yhRrK5Xx3GXZVwDtWLG3Qj3MXKrBSU_Hp4ZTDZRuLLO2CBDkkd1LkBGyyYxkhIrGAD0Sk0-S_5Wsz-QEV_369DOZEoWao0UAFBqQ_Hx2iMrxq81DZoN1UcSZCzf9XEPSHvPKSabGZwnY20PIzj1sjBpk_kN2bHeH38c7AR_quNJgyMsjbHxqJXYgHc7Z1RCqml841QlJfXUd0ueDC6JDKngdHqz3tU85OlYnIT5Gk8vmxvQ8Ihrm0fEJevcNUmd96S3h1VUr6Xxzp3MfrsTuGs8u8e4YT8CJoxf1OWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3A8NepoNbHBKXgsWgstX0WwwsagBuZkCCweDv4DTX18gaFYy4JNM8wPW3C2KExj9u60cEI1yo0JsOGIOMCRT_AZNYVKSa044qvQ-T0JbuKYUOng3E0c-wdshx7nR6R7nOY7XuqFVh0GNuB1ZlkC4LQVIiZo44IE8x-BUtOSuKNazcLWuVveVdKYCSBQiYrevuHbOWn7V4UL4JjO9pgyXZICuqxzkgbeExJ4CkdulzaW6Y_voQoc_PmovDrGuK6LEloLXU_yE-YqtF00hrcrjGb9wMXXuO_elzWsCpB6as3wWFX5mZB53p-6tVXEIY9T8QFasNUqY3nvlayIvKwpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCANk92qnc083ZgTcKjNxTggpqMbg4Ot8F_2Dlu7VEAeQtdWUCwSjNzl2pytbYBvZ3GjYgHSZz8023E98SZTy_3TOXuVB5dK6Ezg_zEvQs4bcp6tO30sksrnJkku-gMgUuEKzkOzr0oqkkSqDJOMioFvgED88jYFmbAbwULuyq81Bo8GRLWrepLwNfuha5mVXgN7lNRKxK9FXtC4gPSsrDRSbOOyLuzJ_IOs23Fs9rvnq4G2mbttN0IdEMngTUVX_skQ5r8vYlUTUcT83gJQaA0l8dwb0JmDx5dEnJw4bZHBkbXoyhn6A6bzlv4K7goKecJBqSTXtvw1-GU6faoHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu7GqR16tgeBjRfF6xrAEmQyQSjygP1NSm7VuyAaO4jS-z5EOw8C5VhjZUNXTq2PzpUygomrqGpnZGGB1Fl3RlmOg4Op7704S3NfyBJvvqcJumuJQBB4NOvpTjtpM8x-7YQ61OUQzv0Q95uAWs-yi524JDXdQ0Yk0po4TETpTUZuL0boTdqo6v--cnB41u1MpKtVOUYLy6WvYvdwGOc0YG4rIMeZ6MbUBMMdOczpYykJtVMrdI0ifusgagYPakm10Z7DTgWgGKGVCwre96lY_1R4wZu8r9G9MA8q66atN18ErlfH6qQazVCLl38dm00qubrLNRrHkvCLUYOJaebXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHxkx3QXyW3RfXXlQKSPCLtH439UAzrbm9ZckFThkSlRWRrOGbCVVv1j3ir02ZKf0wJ936821WL2r50XbL93TZxH50sC5MFrxpLZLJxi_20W264pYpVdjbFEutU0bvM3NqRS0PaYs66_b9sKi9mH-lbCmIY6VosyZFuE3zQRTiK6Deap5w1pQJIMc2efZCy0sP-FKVC9vyhrbWv1hm3AK4Zp2ZZg5vsSoUk3Vtx_r7UBxFqEQwbafHO2Jq6LBKRhApn7CbaBbNBx_2ycLWxCKUQ2BEUCJsvVBfgdLTmYSzXYoKKnnyms_eBDrsbi5XdNflzfAQJRpJEJySVHnbUHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFwf_wLZBacdwulYWb7AmS2dr6-I9pP9i4Kr_KyB6vCR5EbdXBNbYGkN2O-mkFMbOwp2QkD2TxeIHa3B6pw-mfjObv3hKJ1cIuf6_dtI-8b2rowrA_EYnzfYZ86-CmUzXLuqWYsvEATN5aHlYo-X-r5ut8EJ4t_T3Oa6L2UKnvH1b6THidtx6-6sRH7sXiz5xyvkoZNcCEnW7eb2qJhBqWG-EJHRV3tpDlBW-GStg094tVzhEjR2IJzGiecigMp6ygwZP_BpuRa-P5fnV2tNs7p3xs8qFQwspekC6_Bq1tOlyAsDGlmv3iQBGoJFVd0vf6jYg9p_tq7q_Fvn66SNjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOxyR4Dd-DECMj3gIVbbUBzegesChW0XtuDn7zFRPlfOYk_QimjjvNx7jyKd136RNi6o3XpE6Y4ecRnqJ1G5j_9zXyQisbYpAWnezRwYdUvnC0qGykH-twQsiOovMKew5Dj7hd__rrrxWOuBPu-LvonSN8w962G3QDFrPQqjSePe-aPkfQ7dZzT-YMNItrOnJoO6v9bNYrVW602Bvl6Ev9Ow-EhBJDPHzRCzfTHeaQZJdMNpDdQKGzGFaHsQqNnJ-0YqtihtUtqI2A29YOPaJpC149sAQWaFlF6WEDCi6uo1teswBZEtRJ1vSDXf4QnuBCC0f0JL8KbT441rYAvJvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-RA-wfst8H-OXiFBOOCbLQ38rmgzd7YlMlZVllm6bHQ9unjygw8SJ2eaN6PsoTVxid2dvv6JQUsJgTgepTqOdrJxTamhqNI_muuXqRNt4IxiHWCu4tSNmveD1AcT0Z1g7Qi16_PAb_j_JHVQfoi-9NS-ZiMpeQdx1oWZGGcaedt8kpFWQSFJNaaW5DytQPp09BfAP1Gp8uSp8mCUbBKKa8nFy3he74bv9Vcl3Jiq4-hBB_hhWBuh-je2_nwjSmQ37BvTlWwNclBpu_bkqZMZcWl6TWDI-yCP_t-rSgWy0vXa21xpbPmwxKUjF3xjFcNfn9DQrjb_51XrFNbsJJkYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vubm-SzaYHlcR1fL2Qe3vKxQs8lKFuPsUkb65EwdEuGzvDWNMuB8fZY8G-OMqwbEXHHOfno5tRAbDHJ3B7imEGFfLITmi8UJHZl6L1IMOUaxdAWBSqYjEag4DqqpZKQpAi-IZWOgVgE80wbfUcsrVxdiULWa3bWJCLXTZvGJTB4LvnmjNxCAha1sVN-L-HOf_H1ATCAy0QJPjw_UHSWjD0LOPny588mo_1j1d7erWVqILSV5K_HFkp_tSUTv_TjEB_u6U26RDAWUglTeQqiv20rw4zDATrKTTmXyb6Fs4fIPCv5ukoac0MI3Jaksqze0wlRaaskfmIrLQbY_ehuMFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIfZqMvo3m2Q1R_11MkNt2MrQ8yaRvcMiDZ3H-iDEiYB_YlsaUzE8lHLOB42XzOykSZfTsqvHO9H7i4e3PVa8hhTCPFh7Of4r0Ih7BvAQ2mUCCGdgx8VTN_Pyhy2UraBTyprnlJcqUkBB6TTWOv29o5_AQDkRAk4N_Sh5Jce1O33AZqePgw3LN_a_sSSUNU5iwu2jFoR-WK9aUzd78w6qV01_VSdUdVuu4_DbVuSnqCeik0kGc2EDKwjym6Xd2jH5GVogcZ2Tsbk64OY7l6MIUzPFpDySLkQOIiWxcAN4ELRT-p3yrzER4SNev9k16yGTBGJprKZDr8ZRKphcV3n0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6AODYZBPXsQZzgl-5rnregRHITDubv9boyG1tNYTZanbAyupJxHpd4-WXsyDCUHNxn7ftNpF0nkj6cceu78Wy4cb8oOIp46NqzSd-m37XA1S2wg4Bb4XiW5jNQyi2NZvNE0U557_D_mkqvowpcTuBqfjvt3-tzmXWGa2UfkHhuNplvl2BpqzdoxavPzmQXsEhb_2HvUiSRXT3Hl26neVIGe2M8nulclE9o7fxdndSAn-fYJJ5Nm8TyVjAx3FnItF2a7KyKUoWF_0_Tx21hC1FIhVrtZ50-k_nRxC_HuAewv3NyCEWTnKScKs3KdxCQr-GnR7_D9VheEoRfbg83uaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDr3p0aGs6_3QnD1sUFZiPQCOJDt540g7sb2erSf9qIQga7aYurFIezmspNLDhPlNJUOyuQZjAGTKy-RDY2tWB2orkyrAbOL7GlXlwQvk_aaCOlT40hLvPP1fosrAmrlQvqFCgWejRiTPZM25GkqBUQAdLSfCffOu1R8dt1MeaPHwbOcvt7CDhGhIPfeZL_Xsi_B3VIbenX-G62nY6SFUr5xBZF45F4nMvypE6nGKfAV2etKV-cDFhC_q_ldJTzbkgsWYet9L8pT_H808_dTrIjqv8fgpEKPJyI7GHMbaNM0O4kTHLF3def0XiLLiFHBPLyeZsgiqtJ4mwVchxa9jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw2tdkFvl1BwyublEM02qWx3XqQBIwX5Bzw6qixVDDcJQK8XDSp_IjgtyJUr_pdgzoEXJVoVU9bgMPqQD_TJS043pQaM40u9blC8jH-0nEsJpij7yzIhYa1vtCoiYWzjapCYRw3WYmh45ICwDVWHYl9cTOI_InBzRTyeoN6BNGdBVANcCp5IDDx_dVTNM7SvD4Oeuwk_bLBaELjZ90wIoAQBwPHAnAyeQb-iKSdCmqLYjaC7oX4VTrd7shrIszerkWlr9cWV-egotHFxJnxqRDYPb69evGP3lUSnXUdzT9g0KX4TgDtzoM9szKL5aTehk1cX6248stoEZLifWgGVlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CN_IlHIn5xnxoPov9nAgnMj1jthvwJcVzVziS7aKkiUe3XtEk1wXeWTcIpw2J_7y6i-UcySp7sqbtHNipkgxeUF0tOLy-DJrOPSVvMWZiOsORwRKMhl8uWhd0KIjsxpqNUmtU0yOf_va2fmXgaMYa-RyXw_yoRXxOBFx8koCtwzOETWY0ATweMocM3RinlEX4RYLSDh0XL36X3J3ciQkw4-J_5k84aOpaUtd9FeHYc-2ASZ3aESqzwHtQfBNXNNT9X32KP3WQOdg-kvK7ZbO2MBqyUEAv9hvS_e3MdTxOt0xnH9HyDrT7HoUHqYFaojX2qfyfmFfgX7Bc5q6LhmRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMLLCI5a4Eh7mDpx6bLKQQPtV9zvzc6DsxqvaeEFEtiUw8UNv_abr50uXqVe5ZHaWwnvfQyzjdOZDoD2D7Y0eW0dGgKy3ZQ5WPgCqztP6tFbm8fgIz92EyBmy-kSCVubdX2UsOrJfjWPqNtJdXC8-H5r7WYh0hMTzjWtjRLZz49Ev5K-pSvb9Wv58pBwz9QzVGQj6tEhgqqBAz5JhmUXAS0ApmuAyAsVkgvopee1xJT7TaUJ83SiIrzZPwK15Sb5_fnUGoa0fRXgCNyloZFgygqPoRefb0QOB9Ua6XnezealM8tz3WzyCdS-B2dVIc_ldRN9j98tf2Fy6cHWTM8LBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkOR9zX0cJ_3VLxc2fUE4IaA6hvxRNpPGqhVTgB78IiAV6MA-2fVuTHiVIXiFuzM7kHQFkUtOBx3nOf8UuUuN1zKpgYM6z6PLMxdmePe3q_I0PFrrGs8tzl6hg6YM1zTqTQem5vWypddK3NNT_Y4rSKHh1ji6FJ0zqUwhCWCO_8E7HIpggwP0i-8ciWrWNuLqkMGz-hEgH9o01FUGZsD1B_X1HVsm8M9povBMBxxHkWZx1lTApV_OLzZ1q1NfVNiR0tuGqQLnvK_k9HUiwcpU60W2WBGKIvxQQMqJWgM2PuflK7DIzPkoVTbESv33JA9FgBHLVaGxV-Fk3SjyfGYRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzUwlKEsgGgmAxpKk_vGfTe_zhEQ2tghO7U-zhDu1QvAOtDpyyDZuzs9fuk1oI-KBiASdBSasfXDNzdtw8kRxJ5ro9nO5ujBfqMrCFzZ_FT7OoBKXWAfnEGlo-OXvct3cHfU5O4QLQ8DGacAh-7DzGZK7bR8y-Uiyaw66jvXs8U9AEHmMW9gfI13E6oW2SFLrWuMMuer9uybtZq3CeXea89rx-tmRx5w6u69nnBi29Ce4Ka_0FCPYQmsWajf2zGp2gRup4zWEkmn5BDi5-gsV6UW3mRcnYbpTYegiuri86Bsjci9XxnH9l46qkqbYEDqAiRULc-5pGqb9j46ogeMGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksE30e-2ucY0tJqY0HR4bJF2L9z0gHnOuJgy4iICuh5ILMI8Fw2pQfO86Yn5Qy7FxdH0kfqRBlJo0dz7zZZXrbqEX-g3dBQHSceU5e5mQrvo10cXO1kGZjCuiyuzado42CNlhWK5X7PMQJ9ZloRapf1VSclk9KWIGHGCj3tps1WwuRQhUw7y5JIz_6TxYcPOBjR7oswNg3ywgsgbGlpwMit5Lj7QU9DncC4bqSiPbwynai98bQ2FJt-Q61QU16zyQBA6aAA1sDDnQH4sXi52GG03KywdFr9s9iJbSPmiqRU9If7-7eF0dKzvZdAYZADhzs0NW4G3kRaY-xcPr2WbDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVDEmPGIQMG09ZoEjTslkOIU62tir9c4oqTQd11-fUkHxNWZwhujI89vDdvfufaiYfu6Pa3yKVRU04G_VY_UmMHXi71610Y-R5WgQn_7hQv8jL4WlEGDuF2KJE_TDqcqAghfMXvIB3C9DEEpl0-Jhx25auRnPPBd77IQvejZnFUuSuQJ3JQn50Zpb6-kWhQo5bOiwuK9Gl3YDxnrz4jhoBJEpgFh8EkJcLyp46KXQY4XAOyuTqBBy8uqHWKSt2dMOjaCz17MI0z-4y1mfA-lLAABKpqcrOaCQ39CBWuwfKot7WOsSsdHX0l4EYCFbJE2aPQcuX6Xu-nkUhWUl12tng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N00xCzZ-k1wpzs1l4AHo01ltaH21A_1_RO6jRjHH0iLsCjhjWh_OVkF1WjEfTrnLPl50koV2vDyx0nfyyZn0EtZpk4OsqW8olc6EWwui0xSZR4DB75chejx4TavDv1RMCyT5bzbv3M0_zL8Gn33qDm64xF4kEW6YL7plb49exkSKpgHPybTcMAPaBVy6j9e2yYRZEmz_zfdWqMwbOZeAgRcBcrPmrmoUzd268M9etNoWzFf4HVlBm734ix9lGPJsjoNoAeh7TWGqzb8qzSI8Evi_eBLjnNYDglTW8kyQgsSnzSS0P2Lx112fQ8pJsq6pcRmL0RggELJqiD0oqZLyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5gCt_xhijbJt0ohP3ovJOAVAptmMpPi0Lu9RC3Y6KAg3TTigIO3XZGb0msfBFzHdRn7NDMV8w6fULOHgMU2udJnhXjbx-TRVjFGYGU3a5201Upi-xhCdkJqkYCogl60MSfXXtFymCPgv84UPHkxm40_FctecgsovAaKI3H4wjvxzSGLGNoYvKEMOV4x4gAE412cXor4LGSijO_kbp8yN9G1qeyyYmTYBcIl8IDtPHjLugkmtvQuJz3_wO6V2UVTZ2Fuu42N1gZVlAQQtPKxJmco19aOsfKxWXDUTjxCWZKeoPK72BPYbM91iZgnGT596ti9hz21uWqcVmc-gGEAEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2m_a5dITfQKD1sxZtIfk408gksfeQyVEXklkL6EJ5EhKp5oC_qMJAH7s1WT3hUcbQ36CjRb2JA-1UWeICaXI-MkXmV1tmuIyufOIkXl9zOv8HZbtaPbSSmAgdq1Y0xHyQFRdWigOIUyuTZTBYy0XXhoi6m5dOMmBTMCwNgCUFk8j5rsIQlcLaSOmHcXB1CWkNbnm0dqOIvFzvDyidUvrv2iKUFq59VRUAijWCaQvO97zlq4rQI8gKhJ_TBv25VwcOuMzYkEZGc0erAp1LdUe7M-e-qp3gFL6hu9NPDI5OdrEgSSTMt2RRbLlFqHGbFFg5b7CPA-NpQWuIs_vJD16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQ-Mjtgca07Y85VkUMgLwEAevPDWbzJYPzlFk6ZiQamrMRN9WtBvKz9Ha_YfdnIsmPlPn-2u2dlIhb5RTfaH-YxSurTXyFuzp4TTycTTQj7a8hORdw-4z4bkuPiBMV1D5mP2UL5RP6kKpQ-yv9xLwhDprxR6bQE07cjkZ_ITgcb3ezImMgEigVFXzO8GteRZwaIS-GahPFAHF5i0fdvWPljC_m261KhfSgy7kWyV6dm6YhItqlah2B9bOYiu036oAsPmuhHedNGLQREKD2oQM3I3Xlp-ZgSSAl8Ro8LusVNROaz7y_-wxJ5DkoWBIKVNCe3rPHjQO-CoukXU-ymabA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKCb0itJraRnQKfG_YU4XGfPTGBBVJ0-0JPvl19wHLotsYR1fmbWEPjL281tpMEczMVuYVcZFa1xAuQL91oR4tY4WvyviAbSPYB0Tjr3A1sBGc0MV1IOH68jI3vnkOLm_VG_vWgaognYRIlZTImnltCH6BruYPUxUmx4cUXSeKi3N-OiAlqJo3lNshaDGlJC9alQFeBX0JwpVQLsgf8oMSeK9MaYjG17BWy5FraGQ6ZBNymgytUMyPz--NDRGFNwl0V0z5o4n_LRZSWPgRk2vl64hDmu_mz_btrCN1axfHyV8CQsXxhS35iQSgQPQylrfkEYsgPfEGKz8Jxtsy2CyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lH63M0NJmAwfNhcW7M6z5LeYBNpMHiQ9S0mIhWNDswCUh1x69TQjBO8KV6Y9Wa5Tyio7hXMFLZCx2R2d0kLQbmAEFjZQng-SvklY-QVZYBCiDS0nu-kOlkTuA4baboRxJG5heb3LQY6IPmTwYHM_6z5t59gDS5fXf3K7zbA-pCTJIV3d2Tpzs3v2EHJwbhm8i4JEZR22IoBJiSw2ZBvcBPbSIe5l0bNFoPccc8qfhFCssXcMKI_EK_Cgg1g6R2uJOh33VfPzznqNCw1oqtPOIc-ANe3tblloT7Cm4USswslS7oNrQKTBexhMPPkrJBRmMj266dAZDy-Q9NoNpJyYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1bqtJHnb0dA8XdHsOeGkWoksp6SXAQa6NeaIA3AtGKyFn8MQKsQdGWUGkLlUR51YGekxcYSuHKjwz3uBzk8mL8ywTzK1hd_TvFfLH-R2aMrCmkIMUwUyYV6duV9SgSyBLAIKrvFuUh6Wy-hByp8Xo5O_5kYUXJ0HnWB395eszsIxxN__ItUG_4RZ8P5teXwsVwtJLvSEk3UZmMoo9CHqohGmtB3i3R0tkWqIUORUhIDoZG4mpq6sVFPC41hZRxK88AIcN0shcTOdoLoWz7ScQEVopgYY7Jbj57tFtC27FGBnVTBsxaRPhbpsG04ZHw5xA0_P9R4NNwhSmCToZMr4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfgzx98hZRgCOCGFPEoicc5rE87xyjcua34hqieZQ3Ot6kcx-VLMj0ACxFjB5Sn5YyHxPxnR4mX0qAlDugWzmp9x1oia5XJul2gBvcCEVyTcrIpW3WotTjEtoldjc6tzH3Ot_ZWQyju2yAU17NUMeA4v24a8ly5r22b-SuHyfz5wsTQrW9vMvphYKXlm5xyRl_bUhlhtFmQT2W3bPmnpGjHnpRCFn3fJeYvmgqqXS700AcCsHhiBDr642A_-O-g5R-_5BQOmO10HxouhLYhGe5QbmCaMk9i5kraiCgla0FVrB1TwKtOzxLPA2k_XowIrbRMnMizI2CCa-vK3j-rEoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpfq90E_HgQfSS-1OghvoYdhtSH-cdP5tYLOScG7zX-df7AkBw_48R1cjGCEvGRVuJtoIL7TDJZnUqkjQM4Trd4lOHC3HUupEAFzu-oO_soDHmPjkylIn8OlgrC71QTlRfbYUndFTGBzRjPkfsYKlkfN12CKYayMZ8hXenQhX9BiLtVnEsC5hM8MJ4iSdxFtLIJk5akFarcfwlqmSNVILM1hRTGu5V7FrIZ_ClQi4yJYlovXBLTftqdFHomMIzGtKGoFhjQ34USJCJWKa59YI-sy2HxGWh76kvOjCGvAygsq66hK1C4vRwpEiS3WLeLezCF8zDJD-eZnFg8bz-GJ9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlNmTliT1PieWc5UtDKgbAb8tAW37i4rAIWPD-uJVF8-PZ6bNbtRRX_MdFNlXV7M0rHu4Z6cTd1KpVrNhAH0cH2MW9WA9Fv_Lbwqeqr0W5p_OFlVlbcUD6HsFKa-U8zUxdUUjCxkPebuAzeM6nV3i_Ou-suIVqsQFxgEDdOhx9FMz1ZF5pFADsNgpuEHjcsstkZEyzwHsl_1I-jetGkIMx6iPkcv5AGlTdGuR9o16DOV0vfxhYZryXaRNi3yMGoSbFYo3vrnZSmUmMtovnDCJ1cIlMM_JLOnpWF_eo_qkhyL01mxYmwMCsTqCAojEb9CzN8-Jr5bGWsS3XAz_u2axQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ayublr1E00W57s5qgzAZyFzIDiN4nGM-cx0_T08RMWjnkq53YMIU82nBFDkCPCrCkRYEfR3LpZrPrGoVNB4hIYzoTGGSfR7jxrApGSmNi4HpUMH4nlm78aGeuaaPL8sRsNCUHnTdKb4F-VsWIxR07Uwp6dgDHsLmDyW86WrBlTd8liBFvbgA3RdMSB9e3bx0SWRtPxSlxLLaTkIKf8-tT4nXjZcXIBGKy1OtMHlYYTL4boALrpzEPOE4HNy9aNd13NN7IaBdYS9_CESV5XTCvPbHCrTX6iNHg9hoSMv2C97H0DzKQ5CX008-mj3wSybdVAGgqwNrfbGElsVfxDkJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMTaOqfh0yvzASV6CLFeuc5dUhCuEOLXgxyYAVbtjY70fXzBpcOCvP45tLqKd3JmpUVgZ1B1uXyiimCdDwnTJSOUUktG-ghjxk9pWU-Vbh5EsWbVIs_3I69OtWfn4iB301OJFvWQ24A-gmgR4arEV4Ei3ExM00d6LBSgc57giwAPCg3roGLiljkuGD2PF0Y6N4oRtwg1yG0Yp857FRbTFFY7b1WdAmLFILuvQh_NhvCE5M8X2sBtzboSE3617Ro07qSAfJn4jpjMIC9AJFkcVHAvaDpcZAfTBe_pf33xStm47eIvGyP1EZx21fFUZCpXjGCHmApy2B8BXEmCTrfKug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0a1r4HRBwKObazUeJTpi3XR_RwxMxU29JYD3eEolpD5mN_hiMoZMM0jrxG7Fb2Wy4lRHhfXNKKzn6AUVJpL2pakksJjmYyWZxSZt3_p-QkevQSER2kfCtRqFMsqO01IFKARe6n19GHGM4YE0F3C7RIyM4W1NH5Tnf1ReWiD9PFk38WPZWyRUDoxaTEEoTNtPtgnGSd2q7bPWqvPDc6Zv0K6L7WVcP4gI8oNzQexrnAUIlKq6EPJWD1StXCpALgadoNVwYMqLYOdmnpyoiRZGimcFEDh1bF7fqmEGDl7cscLihcgyT5qUEgenvnYhjMorCGV9JaorY-vwaQFVx8Okw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_lwsrtjYj_4tFjZdnwW0H41Zm4LTxXjJtBDjrunMIEZ6OyApxgPWOiPWLRUEWZaSFEBmgKdEnPm7xxKFYdnxf1aspC02Pqr_4IykOx2wsg-QexbxgEkKUbDOJDKIIcdbSGn0MNvGLVmeDShuJvpPhzsvQe54y-EtEOVq4dYyescOCAoo4eN7FDg120Hde_z2PnFdSsmudxksMnzDD_Oolt1folrlzUwIaSeOdnCPn74S7ytmogzd2qC97Ph8y14jdK33J5uNMm6uD1M2BrNagzQOf7Il-5hVa5CnlW7yIIMhccWtBFI0ASkvbMIL28eMT0m2D4yCN6b-0VC5R07YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLkPRyoJ3hJUnq-FgVTK8nraXDoE8yskOOOhcE_v-KrVAIRcG1_iiCDgKCWd826UwQhMaWYOVbXq_57hdNDCy2zeAqT8tcnlaAe0OM0TpLg5xKc1AJFue_FwEb1uCVARx_RR81e9HiUxPpGTz9hW3BsuaIUOBh-B4IB0q5PeS8_X0pMIe9OWxCjFKDsooroIP0_57iJSyYA-faws6EIeaXgtBi_CYW8TE408CmKqxy0b0w6O24WE5CYVltXKcxIBdAkvwDqVE3qCiHgk1uqwUl_2Gr5dLPHQPPuna0-CleZVPzysKL6ZuZzPNYqqlPzQvir65CX5QWCar9g35WA3dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14cQp_jzgLbxgkhOPQoVdmPyNlZDZwwx6Bpe0wOEJCuqiYiHHXv9rilLsssyxvlU6XIjtyTV-wkQGCU_VZgYGRd_DZ4tvDbepmoSTMZMYXzsZ-v5K0tsBT5JDGL9dghoQcQaEYpKjQhwr7SkGvifwBeDDjxVGzBftnvmjUY9nAwXMd_73D3P-gTQQkyLnPhhxOsxdxWRDUYKw2zTJXwRfVf_ELdo8F3cAUWhD8iyfX0gCX_zKjwnfGMXFwnDlZq23sILPRCdunHpqYru8B40-_VYuFjBWlErsUdciHFFezevv58EtG_k844WcrSdBoLXEAbrH1am5DOuX9bVa9o8A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qwlbjwCo7owoeLKwRbUeCHlR2GmaAOlDGrxlTwwg0W8mfe2W1d_bjaWYwepGgBZBkq5knGBHZOHoXPfNKi7nMvgV_nsG4lXRGPs_6bpuUPm5sgHy24NqTz-KvQw62RfgxqbDlOI4zqB5fxmReHdgj14FZjD9AfK-HOZ3utAGTPcqmgmS1XoKdhvOXnJfa7mfNxb8L4-vKtrgoXtn9XRh2KMRCV2f3b228fCkHmO1oAsuXEDiF8c1em2zY19VVHF7z7e6W7vvC8XQ4k8ThRi5WZcYiH3WIQ5aobyomr1POUoUGHcEVAcSbGFR0JcBU3y9kDOvkDujDG8Lp9P5XijIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qwlbjwCo7owoeLKwRbUeCHlR2GmaAOlDGrxlTwwg0W8mfe2W1d_bjaWYwepGgBZBkq5knGBHZOHoXPfNKi7nMvgV_nsG4lXRGPs_6bpuUPm5sgHy24NqTz-KvQw62RfgxqbDlOI4zqB5fxmReHdgj14FZjD9AfK-HOZ3utAGTPcqmgmS1XoKdhvOXnJfa7mfNxb8L4-vKtrgoXtn9XRh2KMRCV2f3b228fCkHmO1oAsuXEDiF8c1em2zY19VVHF7z7e6W7vvC8XQ4k8ThRi5WZcYiH3WIQ5aobyomr1POUoUGHcEVAcSbGFR0JcBU3y9kDOvkDujDG8Lp9P5XijIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRNRSvfFKHDHkuql4_FXec-cZoLXuzgWCKPCGvq1bopKOodkQG5UX2WrcTPv6xqi2Tk_dNcfNG_Jqj22Qb01T3ixBl_491fAnLkGJhnyjyNfWRVcyBukezxTP5sM0BzCNHo3AGg_0dPhgjMSoeDTYdj8fdZQZIRVInzyKfFsAv6i2Pt92jBnVAKMybq1sR2R3s5qpuUoyGHNHI699cb8wi6oGEv7kRP3H7jRhmAtMWcJ00cYoYyLT99l8HW_qgRdLXKJJ7kwHrg6ANsN8qaxnaKldHcAS_ZbvzeLNHcz8FHqm0D_k4Gwz-2Nzvguhh527Re7xG_87RQPpUtUOx60ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD_lJj1VieCMCAwFZYKqOTKGa55oc7J79SGx-Xyeek7Gr2yYNPG7zA_b1XL-wZdfqPQZUDwVan-eYWgsFWIz4Zg69gBGxrJxPF1yWLELzcmELVMXXi0T-52Ds4nufAl4RkE1fik9tPE5ooBCG1llawHbrlgiNp-RH4Bn60AA90NTC_aqleTn2dvNBeHrOVvTsOjwiJcvAcIu4mAhVrRApnQmZdTy6PgAmAHEXzZqxdlgL2g-5BQrCTkgEKNgkJqtdjKoE185D6n_5iAxY5rR4GvVMKixGb8hDB9Bg1gV5aE0iAKJpqpAq14E1om1dHhVcAUHMdgJwO8MWFC4NNjr0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xl7HWvOqTLd9BcQVO914hUGzpB1lXF62LOjiA75B2zqQP3g8GXzesv72gqUmpH4XCXZPRTVsNEtwP50OmT55TqALFikCbRZHt2y6vMqa8ySD6FzE6g03rSXnZJiWxfw4lWKH855PIQqpRea8o-38ZhIDD4J3Gdzv8pag-6E9-MTncUl_05FO3XmTGp3bYTiPEyYYWWQu7PTNPP7Yccf87zxK86X1wUQ2Ecq0aolU_CFgr7TVkGJZAnGfmodEADBeWNZkQGFeDaKx7oN5LM8498S4Ex5uEAvB9XspH2LXZP4ePMWP9kCFPduKAmvDjwlTsmGjQ8lSJx6Vf76btkh4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDlKUk1lHWMX86HLUkiGoQfbajTuPzTzm2j9QJ2SxclJMsm8cpKksI0yHuTr3DLCZADuRE8rm1OEP_54A8SzwlQrwfq96yqCFs8bXbZ6TSoMWM9xArpHtympL65Hzo07D1qdNzzLQCkS0H8eLE4iSm9FtibxivUdy8hXlmQ7YQpXnh819D1tIhZogt2Rkp32vXXqIgtXx8mimSLsQXog9yX59aR36UgVf5TgqaYslMb6nEdHiBskiar9v6u2Yq6TwENZXgGQ2lyIhfvuSOvq5g1oCKanZfvWEshl376PPMy-4zG_AlkgKBQRUbbBEvopSlT80hJR-gRDpq8ORE3N4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPOLTS5TQ_At73UbLLWZOArvsM5o9k7sTZDNGeFuoo6xyMyQyc3jEK5GVZSH9-FZl0jHYCj03Lz19f15Z-nd_qHJJ8i8JMUZhIwyTrUumivnwaIAZL4IdrveUUH2lcv--73ofaUabY2A0310SdMi7qZhePmM9i0XR1Eb9sG66q88X34I9FbSgaNL5wC5LMns9FKSoVWmJtgsXFxmiY5yMyKnbyiPq2CEGe51s4-BLb5j98ETOtRXjHtCPBN8iwVR-Jl0UZXP3yhIsYlXnG4cdpBb490qITXzQcPij5ookZ49h2l1V5IUIHHtDCX021cqpIaSYHzWWf0ep3l4w3ptlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMshuJmdry9GQ6UEAHntNuG2lDAyjp2--fwvbKRkdjXQgHOjbCLdg6CBGVcDfrMXM3EVIYYYT8iHPNCpl3j3SUMNZ4dHM9lWLloixWazrDQnBu-MV99LCSfmY7F4Z25_eaRTJR0prHWedbZ-boR7CKXb5PGZULNwWIAM2dwXmcZBsU5u7gq6zSa1zQqRmEdVhN33LH_ICMEgYl8jmk9vb-OltYAOgr5jIRbbhdIjnVMpLhGlpd17r5AtvrTNrAPibinqDgyxRfA1fDTOt9Y7jJ6y1HygDtcYF2h12mD3avWmHm1KAPynzBQ1GeGLdbQPVcMRtGz15sWw0rPMDVi1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amrFDYKOkgNig5v_l0l4rS-HHX9ueXkEFRpiUpyHMC-LLgAx7G7WdOBYhd3EZN4YFld4ZQeWHvhytyjpXqzdaTEIEqxe4ALX-3hKAfSZ_c8THyhkCmZO8AxlDR-02QRE2w8cDRz6IwCJdiLJGceRO3294u57LYpkGDfVqDaFkGP2QLaFOuiTmMAHqps9fjTeVPW6C6U84eP3YJWJJgASE-pqLE6Oqe1ReKQgJpLhpuVDnZ6SZU0cxrcwWvv1mg7iYgxKNUnaaszpJOPNDLr1CnBTEpiBLBpU1saaMJ37yZlktrqeOMjQr7KutCwHigccmqpTlBhY_sKxHPW0U6nO9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=M2frsLkvAH659p5Es9u6mDRofcmNQeqo1SnAp5zjCAR302qzyzSHMYVrcasA3PP67JprszT-q3j31D8ZXWVfyMJjFtNPvyf2phj6-KjFsNijoUYyKtCyqcHWxO_jO-xlPvJeuPsFq4SdJMftIw_ODtOagv3EL6apHyKwpYxTl5LWiAwzqO_1q5-rvY_8FZt2ZOL3SgLLZ_Zefwx0VgURVguZWx9UhrDF6thhG-DuvsWaYGPU5S5vP5_mQa7Qk7w3bXgAhz5wOtzsoemL32GmX0_kw-dFBTdv4PisI6KSGfpotW9qHVzmdEzw7T_Z0bSLDoaNcrCTXdkS5uTdSShXXn2uSGKbOjSUP4XSCrewt91-I3Z5TiQFy-ZEiNgkdtqmFuvKeayw_EEegPQojsIqeBhPZdB4JjxXsxsRc-GsQaxNpV8NIXsSd6CfoiOj8tTuOIYzgRO6wohfgn8wu0_dWNiLpndxUmCBi0Xuyngjrk0gh9PHsNMfMHA3_hcXmej3RhWhjTiMSpyTq6bpnl75Zczt9ofc58JL7FIoRdGAO5bbtAJ0vVm-6rHEHsk3a57WLjWhqO4kNLPpQcODG94k4QIBf22d_JRdNcLcEWdMgv9Ug26rb2NwDb7aNeI1R9UELA7reKA3HelMw4XsfvppwOxKWzYgYuIMZ4XRT8g2ks0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=M2frsLkvAH659p5Es9u6mDRofcmNQeqo1SnAp5zjCAR302qzyzSHMYVrcasA3PP67JprszT-q3j31D8ZXWVfyMJjFtNPvyf2phj6-KjFsNijoUYyKtCyqcHWxO_jO-xlPvJeuPsFq4SdJMftIw_ODtOagv3EL6apHyKwpYxTl5LWiAwzqO_1q5-rvY_8FZt2ZOL3SgLLZ_Zefwx0VgURVguZWx9UhrDF6thhG-DuvsWaYGPU5S5vP5_mQa7Qk7w3bXgAhz5wOtzsoemL32GmX0_kw-dFBTdv4PisI6KSGfpotW9qHVzmdEzw7T_Z0bSLDoaNcrCTXdkS5uTdSShXXn2uSGKbOjSUP4XSCrewt91-I3Z5TiQFy-ZEiNgkdtqmFuvKeayw_EEegPQojsIqeBhPZdB4JjxXsxsRc-GsQaxNpV8NIXsSd6CfoiOj8tTuOIYzgRO6wohfgn8wu0_dWNiLpndxUmCBi0Xuyngjrk0gh9PHsNMfMHA3_hcXmej3RhWhjTiMSpyTq6bpnl75Zczt9ofc58JL7FIoRdGAO5bbtAJ0vVm-6rHEHsk3a57WLjWhqO4kNLPpQcODG94k4QIBf22d_JRdNcLcEWdMgv9Ug26rb2NwDb7aNeI1R9UELA7reKA3HelMw4XsfvppwOxKWzYgYuIMZ4XRT8g2ks0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o32cJSHZkEnaaff2E99LwZad3m8t7zN3SkctjQ1V1N1Xqv7DTvZgGX21E4RJobEoHtZopjQ9SuAZGhOc4C6CrLfJDN20tJdFGBft4zAgtX-aUqFRYg7K_P1ajRKl0ZkU3RRN18oPoK5E1oR2ngv65lJseEv2eAAM_MiWXaAMGaim7zFQhmboQ0RD2osAH9unD77OL8XYDCO12wDAp1hz_RlawqOfDraTo4oBuCu32pWSsw5EmQUEgcMX0L8wRGmD6B70cJBsmsrufon77HUIGrFUE6rj3-PDXGkxT00FDeQ6qzBQ7EtsspB2d96GoQ1vA8mR-a6AUgMRmhMeEiJUXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaOIUybDl9yEGKXp8XqApdnXT0lDQO37FqTBkw1yDkhcB67nVJktDh5ieW2Tvl0DhUg5sTF1ajDepRuZPCYfS1dA8kFrOVyPceXCOZoCWhMXr-kcXRmKpNN08f5jTLS2mjycDVDRHKNuQSv1MI_2xpE4mIgzjS0-3SZcIWSzlV7G5acrF5-rPMeOJN2aptGlZIu9iBWIjBRCWdwQkK4tMdUNt7JVW904jGsZ2Q58WkvenlEbb8CxWFPy7ixaeA1Hd-9erLUcazGv7BOHzEdo5A26Yq01UOiRY4XngJoNl0UbjSmqkZlnPCA4omrBJuOLFPt8j-TYETZWLNnWt2_-uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMI8d5Q9k7IP2tEnrV_ecb5wCZKOWVpauwh5UKMtmUEtkEpmReg1Bw0kJzSWHhGs2kIt7YM1SVdhnslvVtX6cFhbZ60HR6DweEszKxqh2pIVw9nJL43hNQu74wXh9gY9zMWMhJdM3okrmZs4HD9pZBccaUZ848MY-xk5abY2JwtAwXMTQaTrjtLCDh8it9N_sDwUdtoHV-wI-6AEmIs3MeG4h2ABtEBOesQd3DL-H_aV75jVOwbzGNvnmTUBZaUvnV0yU8CWTDCujwzFUjdvZ4O8n90k7huLK-0nuY2VIQzk3qVK6-KzgkLaZT0uo0Do96vRFS90jc1vNIXJzL43vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmRnqn5vWjAUbBzP1M1bDbftTI1PkGXzVmutWzUuv6h4y1TL1HX7mRC5V9KaZ9hb66DvOaYWCerPCm1qvrGHe10DSkI-yVo9OS6VKvO0g6_30ywhovnr3PWCRJcmHFj6fPWwCJ2fi2wKS1P7QnqmM1kTdvkgnEul6elOLNC4ptxNB4lxPWFfxgvUKoDRd5uktysTtHCrqFWL-QGt_nxYi38KOjcfjBiuuolIAuRWnP-iiDlYXPenHkmvyHt40XAYZv0FiUCf6_judzKletiOZp4t3zPKkqzn_5EKUSIbeR9nZnC_vmvCHrAzIeG8NRmalZx5A8yv_RV6KW2mJ6_fmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKsG0U7tG7EVX-OE6gwkRFqPrpUrUFN97hkCaHSn9i06KJXNoP_7Pwu8ibZyUAW-_MIfI2-5-ogNz7UTIjRzdRcffLw2wBR8irCvoXsiwgC1vWdIEoWI2xm3ShPJN0RZ-9CQDg08UhxdEmolh94jo_PiuHpb51HyCRFYVE6iSeYYNwzhv3L4zhHEPLvFxnCYyWyZOarp5UCbigZb9B3ckleuLe4JG2jZ68VrS8jbkPNHa4WKppb0m13UTPtMVc9WSVMzxkQKh390B3XDq2h5eP_mc2CW2YChv6os7MmSEIqyUiJtyf2dTIK_ur-1v4aXoFnPaQHNE0owOQDlZ2DVTQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0R3N8INjouEkN-l5vJEvDB6wBdLhK7PRKpkjWtskRJKw_lwRH0dENBgcZiTH3FUe4rJDNMdyiXCWoGSbqAsH4NKXKAR0OqanJZkOlyCQC8RIH0izfOFgVCpmStJnWzjmFaveKXsHqkdJJf8b4zNciMGvJpxPjbZUm0mBnrjDlYB_Ji6YOgzoSmq_610_MX7xzD_s7zchLABJ0cxCAnP_gQ7mLptYvlhHhk3GYB0K8HqiiN29uMUMYYigmMvTvgse_C3wARPI5QrVbxbJq_eZR6FgkWDHLdxlkrDCuZbw-zbSEO0hy9VYTk6WVbSkPgVGmEqq5qXJvHCp5fbyjz97zW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0R3N8INjouEkN-l5vJEvDB6wBdLhK7PRKpkjWtskRJKw_lwRH0dENBgcZiTH3FUe4rJDNMdyiXCWoGSbqAsH4NKXKAR0OqanJZkOlyCQC8RIH0izfOFgVCpmStJnWzjmFaveKXsHqkdJJf8b4zNciMGvJpxPjbZUm0mBnrjDlYB_Ji6YOgzoSmq_610_MX7xzD_s7zchLABJ0cxCAnP_gQ7mLptYvlhHhk3GYB0K8HqiiN29uMUMYYigmMvTvgse_C3wARPI5QrVbxbJq_eZR6FgkWDHLdxlkrDCuZbw-zbSEO0hy9VYTk6WVbSkPgVGmEqq5qXJvHCp5fbyjz97zW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixWUE5CGi60yEPRC9Y81stvQXfp8TKa3mDfdtDo7j8FrC6xTpIIibjxu6WglyMGc72VloRGLUwokGeSroQXkb4i_zYpjQEAZKFZGl8PnCytkJ72M9tKb2CppOOdHBd2wxOQ17_x8c8Xqe6WmaP7Ks136_Qr1BLB8UQs2buDMXicr1pSAbY2eqSnm4AJFHJxcj4I3ewJGvQqhwOmZF2wAG6Txhpvlsfdj3RWHLuvlpn1TtZDciVsz59IOhcDr3D4OzGTXdTguQj5YVVe4E_q1RHR2-ngXfS2KS-y-D1fBpEFRANhBZLoMPHz3BnBQkt1pHAFVhCQOY3cicSu0p2Zarw.jpg" alt="photo" loading="lazy"/></div>
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
