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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 231 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP9aOn1physZNsINVAVigTg86GlFnPguKG-sgcH317VRxuqlbPUaXks6xXmyAwxB4z649ylwm6ftkSqD0zXGBvqGsKCnCDpGEruWcu81e9khGwPOAqZHUq3Yv7Lke9fthYW_ncaxyXnEU5LgspTmqiULMP8by8BEvqKNL_HKhhh--j53gv9T0bd6W_T1GCH6pFME3isSY2Q2omraW24LZPTQ4J1-vhXK87BoHWuNYTKuD1PL-5ZqJmFpWU6jizUoWwCC3l_qVeYRtyqPLod9QetJ-GV9lbfnn8CNkER_jMQD8G4XDJIj53cx9Tdcnzy3A5voj1-gWjQxDtnwwhoc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 472 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 635 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 625 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 851 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrmozK5j7lZ3fVIDNXOH__AdBTpgpdeE5ANGd8OcWZL1JIXyZlCmEKK3kyIf1YVMaQU2Zy7LqtJT7o2zmn5N0_eLDuuebFDQLXx22j5e-3sF_tcPDxhVrJBfueKP2x3FTpnHlIVX1Y_hVDFn1wuI2IfgrTlJsMzbsqGbx4n7JfBXUnKOUJB7ZC4WCNzhooog58jBY_g6sS9pAhkpVAkn-WIgCH4rAy8PHeAtK_LS48k0ScQUnfFAz61GSNacQx3dBwz_V0gPEMDbHLB2-34zyUs6Ewn_M72WrjCW7ukgPsI5QQEvSkK-N7pIdLOrAoEDbERJ7tvYnJaDOimEAA6lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To-Bw_PhBdPoNjYrn3v6Hb2IpWAIeJOefPkAXDANQj-Mrnk07ldK2Pc11acuXQt36UJXUrlddwGJbl-HiWeh0DLgewULSYwfSoseK1X8xxhUeblfK5aGtzb_BIe4YGDany1K6RDKTNT_LobCUAANVW2-eAdYX2M2vZV4VztihNx_pbWd-BJ0Byo74JeLZLKTiwuuLt_oDxcvBSqruYb_Gevlj2I0Wd4uHJKtmhVJPsw6e-3NPJOeHmxUbQU-9mrUHsxtA3V1wwcpBoIHCXwtI4PgtFAKI1F9lMsFF_UDhyLOx_K5CxbxwN5yUMTkHC-6O4FZ4-OPu2eOkffxpemk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzQG7v5rsN_g68vsL42rbgNcV7-aOFDWlSbFchVPwmcfktRag4MzeEmFqBw-6lt2_r2-tq6r02gUEF0esIA6B13CvG4R8IQlSHb5yCmxuJxOdQqDA800YuUf6mgf2-yS8D0YTlrXBCLlCj6IjNC7LZT2Pcri_kvMupTwZeThC3QRLTQX5QXAcKCIHI97F1zY2e9yqIHnWwPyqRi_1X249D-gzwa_6rwAE-s8choUdwSH1AB7H9VNFPrNjAaGJkCbY2e34xcWj53uz_KK0WcA7onFapP9jsNeguaJ1RonSSJ_C6ocnvX0TcrhBic_Fl_7W7NUtrijNCGN8KS4kf5ERg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAhx7Zq7qFYb_b2Z-eea_xwX4If2VU7DwZIY-V_YxIRziiw067E69luR6lfrtW6ahIGZVAMLdRcm56PEZ8qEN-ssOKzzpCGwb8MZKkOUvSkX2u14oaw1vwOJkXU8EnPfGNBCaeuSasvjC6xNNz3rlltIT2hQGV3eVmpXW_UvAerqEA7CXBxaRsAXNcZoPQb3e0YLTc03_JNX9SFyArQjIvpo4graQbEo7klDLQET7vwDfUurz3giWl_J5G1pq_Rfb-P-coU-2VCD3FV5g5I6hvlaBCBbjKqIwL4ujgEFO2UIP_GgtdI0DxdHzHYsbP8eUopUfBAd8nx013yrGwNnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVyj73GP1IRtFuCJDbfYQMAfnR4TuIVoJSVpxfMPLcKclj_AKP5_RenUj61qQ0Lglz7LDtNA90E706D9uRx7ivwOIOEjRxi5vpk_qahFaJHKdpxYYrHbcrT9TUNOzq_NSzMp_cLciyMFrhePwakh07mB3sZNmJEGQ9-LCoprhv0b31GuMQ_N-nzm6LLYQgfweSx-WZRDfGjTeUG2arDysMkv235XcttplHkhexmOpW38FCVBf5l6kQE0H-5b6qy3zR95tOd9LuStRWiJhNc8NEyv2J1mUxpQ_TY-Z2oYWPvv_ME4TypeDbvMo7Brav-R39tOnLtsDd3l-q6ZruWj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-zrNgCjvaXtKinseXUNmdincEvTXzuMYHqhAlSHRoMP-gTm8dMq2zbx0naDPxPjgfcHd6Td9Bl0NMbJUK2AFSRZp0cnKHeIYwB5J9JfFdQFilwyDdexEJk0giJ63est57jCflisb413vu2I0MlzRz206uB6W_vuA4ebsy8BETl0bO3UD_ny2uf9J5qjai1jhx5nRu1Xb2Ao-5yeABjBEpfNNI_of6Gxj7nVJI_5NyGc3N_Rwbt-ryGiaAPWmeBYNs9iNnD8SCA4P-OVqsv1rkhlfDJQsJSRMI2Kl53fnVKugBCORX3FnXuPiDN6RymoikWc3H08mpWIl2l_aw3JVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnIz705rg7_To9yE48niNDfcc4_jZQ2J_R4Pb83J8rdCtuZ9OaJjiAAdgmhKZDalNSmVQSd0_ZZqzUubtdhEqAOx8b6zjyqvysLTs8DDNF8ssqoxQLdK6-y89gkJqQp_3A_Vc7q0GfNDqZIkqWaD62CJnH9dtzE-yLRTOMdC3etEc53RqH-87Rj7uf5F9Y11FtlW44VIN2NUOSmiJHg4pG6woi_Oo1yrhQ6dC-cctoRcHIbv9-m3TYN-s7r12Xx2CCgqnFbv34ppJ3d3x4bnkYnQ1bpxhVcMdjRvcgu4EsnS6jM3QqkgN0xzVjOZUNBgisOi-lSuMYxaCz7Q6rxrmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYFDr1_g25NYmt621pvFGNdqJD0qWcZKtFWVFmcHAJkBu9GbarBU-UcnSolFxx8H19-3POEE8Zm3TyBdBspNjfQQdRKyygFOfPxlFj3jKqiiCe-xCZr9qhXLyCPacYekD_5RBN9yqvPaIcVCbVkDZ4Dp0ojwIt0HHJeteSPHsaD21snOZ0dG2dQLIQf4eHFBUxiaCTpDefI6f4E6HFxB5STilgdpAK8vbAapK-i1ZincuQhVwudCeU2EOG4YkEqgEKrQcPzGAysHi6ETOsM9xiWr_phsQfbtsfZI4TN0hb5bgbnISWh42hu5KvoLtaVS8GwdlePepCPjDmW0t7YWtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gefRcDt5_fYwS2cpiyTZBGC8jGeIec_sOaWlr_8HTZx2_HXHJlGc_CFnDnxGaji14DKTeqSz4Zw-XJJBrJmEv8hgtT3pmO06OAkH_7wbrbn8IrvustkURLfuYhfPYS4YrhZuKg2m-3COUYEyFZ9A-kKGJszlQnNgm0kN6HAxBlFSZSLh9uqmog0mtj7ZACrjaorPY6NwvCGYUxJSNjiHgnGgDTGBtEJ_udHLvsxNyG9OCvaGYs5n_GCkm85JKSSkDu2kXTvEBMhGhbxt3uZxnt0Ir28yLSG8jEQ_sKw4iJlRzNtk66G1T5jf059JeU_sZgzS2PS0cYQ_a1BYKxAvyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZKbxaZcRwCqzeo1RVwYS1abpY-tOqQSOCs74v4RRyD0sY712IfizEkDtDKF_FvjHpbeeTW4sfzkPzdP8gc3M7A3MBsH2ekrEowiXTfu_cbrxU6_WS7UOl6YqDLwL74jTPcLZrIVwwv-8rOJi2pTFBh7zcgEfyNtq2IqdQKAfOknHvf3bUzjCNE9kjiBMuuQ4gjKqCkTWAvyjPJmmjX12zGFWZk-XsxnXbioBaasnBl7jsiiFJ2IumNxrPSuwcy6So2o6_GHqQD9gkp1znLuUPrRbu3eqiB7LVeEMh4PskJpTi5HDGGTlEjqW77-ACdfL0Iim_1-vInru_vRzxOmFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5CCYLXyTgoLfFYrY0U50oan7K3fzAmOpkQut1DhdFywjDbIRfmTYcw2uqEmsLqSqT6XCR6prvPa64DVqvaTjaYX9SP6oJWQJQ3ZhCJ7brxEtaRPRqc7l_0VcFC5Y7O5lfploT8TYE-eWSdHTuVfl_hvBAEzzmW0jMfWm2lDYF6aiMLtxLk6TLCxkNMZI4yLxug8ewndz3dvfgytK-rj3mqAt51UoZlg9XSqFP2jNOcqP1QrH2tSmsKatC1nAkGw1rEZsHa89EinVoobhGTHQo2698-G8bBjMFBUCPJuGKcgwCdHPJG9PU9_7720C4D64U7Zl9BK46BwtYWEDJObwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPNajHDdUrtoc_nQjKHj8zLEYI1NhfflVGTewIsThRSvIN0pOBg3OoVW3ztMMhPpNFMd3GZ-vBr0XnrFo_FhqGgf6qmiSrGWxiubR3m8P5e7yuwmGMlThq3m7P_Bs2mFGt9ZT9d6PoLlMQbrkU2mr7oxKdhcWIbQcfPpsKIZn28mpXzgY8ijDaNoYiNJ_SoTpnyicANAng8-irQHPR5JIABnBd6ciJxdGPzQCyegtvSD5UMiKIvxzi1ahnhczl5KSaBA38gCi1cr0IZENPIXtE6OCRIik7KG6XHzfgl8-C-yASeJxMv8pRU1NOQRlnRpN62iEeFvT_958SUEr4T9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNCPPInK2w0Pxop19c0jwhFwkZ4L-BuSEcLzIh9865jns5QPB2Mli4QemdVcn_P_Mr2fDTE8qA6LBfkaBEzQYsvEdSVkPiRZm7zKBwsbadu-gzlBmqPWomIxpVQfW_rdjuIvAk95f7FeNzbjTCkg6Su8_iG1P38kbLLnvzHJuBlIm77hsk72AfK6YtT-CKjJtOM9e0IFEStX61_d1XG4pz2qXEy-obnnYpgyo5rwsDQK3bMFn6MS5W-092rQRbTnTR7qow9tX1qEzo3OEVc6vZFYNAWytPQNDHmRM8O4rN0AmLcANUxgLjWY266qavaBwUOVLWI--Ft5h-YeBN6qHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tb4pxJGvF3aMrFLQ3grKITQ9g8m2XDi6WLOnDye64EARS2qJpAOefvGYKiHTbgr-w0DM1SUS0Z0nsQ3oG_5kPtVaC6jgXeCTNa_Q5ifAEQ7Kx5YmlsezCDBe-m998fcZ2dtrhowK8YdVMebqysmp97oh-w-efs2tknL4v47Y-7_-wYTDJ4hzHCUyROX9Mf7p71MQcUcFYfuW-D1SWM0wutAQRSJbJIJb0_kTZ5vI72derXcv3sM5u_j1pimCXR2vFmCSVEBoFvZ-Bwf8ELTKwzmwIYidC4pEfLslpGO0T0QsAdKutWrRH3eEmF5PBugqzRjEepesDfP91Ew6w5PY0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWORVH_kYb0R6ry6klC6BHhI4xIlmGJ-hfnPATFQA_7U39-Zey7VdNZdzVoAskyZpsXvGwq2Bw67jLhZT0-YmBEViXfRez3jCGBr2KDzrwJb-esnaZEbh7R-jZxq9GlHx1LO5bZ-6FYuEGEsdESsw6VT4JeeckAyDOOcVuAE2tiGu_sRN1tHPwk1b4ybvxXKLWgDr5gXu675dRp9ewOWBwU6OrOQNiE2QXKeQSvd82g_GbP7ic31TltMoCdxKZfIXPFV2FDLeSNeGrmI3FGqMyJo1ZxpktJFIZ9kLy6UvD9YINQIO6nIVGOAcgFOO0K43iTZnyDXQuGarxuT0db-Tw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=HX2dIEBvY0GfH4cKjKUSb7k3mO1R-RZO4OvMw3EXTE9FxZkdah0YZVvG1O3EhYcWXLz_64ffpP2svhnttqhxest7m57lGBK5qwxGQJaJypdijffHXQaofZzxBHzqPf7fzhOQMWKE70K3DRiXxw0Opx4S__VQkMjeiKy7VZQ36FsGfzWz_3kq7D7W5q2r--fskWHMwne11_6Yt4bp3G0y092XtfLTqqZxw0HTtUcpyqu0C3UnOoTR-VBXubAVfcW6i-TQZyxfAE-2i_Kn80NsMcAPpqKECSk6BNDj7sTffU-aMklEuFwYCUzYCy_GhkgMdLXG1IZ3XBTyTMKrRfg8Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=HX2dIEBvY0GfH4cKjKUSb7k3mO1R-RZO4OvMw3EXTE9FxZkdah0YZVvG1O3EhYcWXLz_64ffpP2svhnttqhxest7m57lGBK5qwxGQJaJypdijffHXQaofZzxBHzqPf7fzhOQMWKE70K3DRiXxw0Opx4S__VQkMjeiKy7VZQ36FsGfzWz_3kq7D7W5q2r--fskWHMwne11_6Yt4bp3G0y092XtfLTqqZxw0HTtUcpyqu0C3UnOoTR-VBXubAVfcW6i-TQZyxfAE-2i_Kn80NsMcAPpqKECSk6BNDj7sTffU-aMklEuFwYCUzYCy_GhkgMdLXG1IZ3XBTyTMKrRfg8Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQMxCOF0zQeXSm-MVzhMhuz3jLoQv0WbubONyM8j1vcj6LD1o6N7Ar5nhXgTlR7CNNRVhNQwC8bbEvOt7Pb63EeQcd9TN_FT7lGe2Hu6DiW_QdVm3ASwuwwE3u6xMX1RZwdZKAP6SYsqNnLbNwYwmQkpPRsjwfXoH3STYC_o7ROUky_QNcPuKjmE4iB9JKeLDVCM989yuYC4p4procVqWPcOpEQ4G8k4qpu24nwGNk-3yqUVcqbs0g0jxxd3inLOWoyX9ipMUNn2_vGFML-4UcdyPF8yp_jgy4BNubnfPgGhw9mFmoDCaG_sunzxYBnittc51OtECfdlph-AXkqJUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx_Yqx5aoaqwJ3SzCPigWZlMzUJTOc8gchJXmpbND6Ykn5QJG4m4jP1KsRxx7Ccua8enZA0DRYhSBDSKt1mVJk_fFFuGCwnI0zHEcQt8Dq7MuILUyzhn8VkLbpaM6aIKtL1-4rvEFMlJbw53ud7GHjGs5Hojs-4KJ_87sSbJY9uZNuduvIb2EHsm02QK4AffHwkPd5K5L6tf14x2Yf6VUx2sgC5JW_eFW0wy_x5i_YoNSjk6klDeueRQTA88_SYuKcZxauOkb4CqH209Ab2IRwA74PTh_dFVEkbRQ92nnJfq6aq6heOflkMk-z5VMKXfwfYq6FXspdw9VsVH2Cvw6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfeiG2xsuXefL0DNlSI4RQplVZ9nWxDz3VPVwhk8FXm01HCp7nuOHvdB58pj2NpVblmDUxSu72nnKLCPABbPchXu6KoJZdgUDkP0S0XJ66pApeqGuJFrGInXHeXTyMs8r7nzQ3ETxSsPRMVHfskUMuYYH4OhcinVn-VYhl9FijMru3WKRxg4butSTf3Qe1ZbqaB7fNWZAU_HdNC9DGErCyHFYHlsEB97GmXbmcTcauXrwnkkgsbExVcFnL81eWBuIiLhzRbF_Bs9rfmd3aWhlee91ODXsb5Ck52fHJNUqBGZ0SRLOTwYHjKs50GGefWcXRhkJW3gRLzwzMzGQdjSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIgj2oJNkde0z2vkxZKLtjRG8wY09lOhMAPEPOHmF5zNz0T6ImftBWA8wUL4cXfbWnpd6K21hlfaifZ_kKfSg1WjPHNP-qykHmZ9KcViSAKKFBR0MYqBzQjRF0_DOJKZ4Lgz2hktxwmjKhazves-Q2g0i70HUN8Ixq_pP5seTU850NpdSuWYXaUYmJyBTB_NKK-Kx1y-HVfsvhD62am-4sRQ2nAoMLWloVam2Hxsh6D59f6dxYGdUor5TDM1ZUZa-yxyxcbSmV2SeO82SC9FtYK-u5sKZHH4EigXavGfeT-fOozQMoZBaDROX2h4UTikQsXov9AlRVp8yuB7ernNqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKef-nN2aGse6TK_fIGzuehAtCJrSqXv0ZN7FpU75tMr8fe-kK1IrX7uUFti_bnbu0rd8Nv1u4aGfvStoNGhV9sPV_RFjUByeqoACg2GghG4pgB3q1JJXSmC41R6vozyuLdvjrXWoeIsCNKbSXeE6DsYsar9cZlMNFZk4XLlG2OHiGmUupw0povg8j-duvuzroLKgoO818jUr95o2ngeyjRLj5yAxN9POx27P2AJbjZRir8HX4KPLRha8quTV9sVwYMPVKF4580SQhcOhrd-Ekm8uC4YV3vl27Pi8imBtX-xfm-j7BdmlTd4kzEDEBXnbqKPjWn-Pb1lj_GxLcVtWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkH-YjmXrbamzCIzl8fdkeMfTh3sngd9pm0kOgyAQegN3OUG6yYsEmzpnbTWQqgOiXBcv9MJTsbj1xRPrOO0mPIjBtC_bnpMackGqzV9XGeRcZ7cZkFPyOLTfvoZ38nuNfAmakvGZ4SzZ-sR1RtTJNy9REwsuh44ZKrilYUHk6IpTOUWpGLqr0X_Y2t-hCzCFH_iRXs2b93cMUmu2z_H1OrP3O2_ayhE-ySrrJuEHHw80mjCBRVzsVr6DOU_QnN3Awo84x0OZ10RyDqfnbtYD3gxE8Kb5toyEu2VSAnq0ui7sw38Qhkaz-pQ02UWvR4BP4YRDdnAODdEasSxqIz8Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_JoFP1s56W7hjoOnmBKYJ_j0mMPX-VzPsOl6sxeAIan-nAy07eTZf9fDjlvVKvW-klzgXUq6Sx-FZI61RXmlcKmQUTvGcVcrvRa525cr8ucaYl3xUnS2frrdIJGw2HilPRQN5Y12eAdPBoOP-PmiOXBKiZpzjZydCiMAbORtseuLGz-3DsiT8Ws-WSD8r81uNRqF4arD8OY-MSgTU_7FZFhh5l5NQ0sFgMoJ-m_X5vtnzo087g4R-DHmmFifm8TZCSXRpnO1EG0K45FygmYCvYFHsB65Dt0hJee4bQLIvxfe6TpIOslryAn5JfoNfhLECq3lobxTvicDvBk3nNmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUyJoVvSYR9jqHjYMbFetgIsuPSGSpcNR7CZc6gXcB0GBL6Wyh9th6srksvecNBma-N8P87ncY0ZqSoMYXzyQDWSHck5bXh9MPgrcSu6bdrDQMuGE9wY8kUMiupXLGEF8d3pFct5GyBwbGTTqvFbWgTOMD06lnnUguEs0TumDXKWMRgbdziLqC30xfPvl0Y8dQbSeew4oI4yFI9_SJX9I4MEI5RKDGkRO_UJQLjBtJJH8DHn08iwjArTMlSLN4ouEugQSwZR1sNUKfksLbMaonSRErLB_hMObisGJ0H8rWaEhTNmgbIibMdGTRKoN1ogwP9wT1CECqI5Re2N_LmfhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKVtvI-KF5Xh5PvTTStvv_2psP4NhHrKmEFH8SYlOx3MBR7JtMz5z5jib0z0-14_Y8djO6Z2Udzo1knECcB6Wpm9VZtLAGvJ3v3a-9xBol9nWsQY3XDN0lF4oDIcCei1WPnPWQdxoRMnCK-F9YDJJlNocqPTvvJFgBmd_hoYPN7yOhFuPdX0Xoce0hUoQGs4zqKB6xesrlZSjOJozt50Y5K7YfwKqhoHCKlzDbdsi7Bp120w32Ts2AoWO6Q9xycfoxuQMm2JPUeEBAdtokQ2aVy6hz6PW7jjOElWj_8G30MaIQik2seL3jxdqjpaAEBQhmRHLUY1dcvkh54kkc14Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbIbRc2LjqJukd2s3j4Mq_FzdZqd03K-Nol50ST1e1KhH8loCLp2Ja89-kKFqzrLmNW-TF6ODS3KVLf-QTQjEteD3BN09tNXq3zxf5wh6X2Bm8P4hxZmeEEII57NKpApsHFMrZyN6GTRicsWRHvACdWTSc2w-ZEdI3wJb7bDgCAvScQz2uRajTnHqy4YdaBwgKYeCZxrgE-IE3tXj8-adGO8ItSdGslQcCik3IH9iKcY01HCiJE7in8Kea0LIYpcKyzvNw2h16vv-5j_Lqm8BzQ3BqDNs01zWBEFfwvW6XIQB8puaN8S-mWsaMV_SYwWLg_JFLRR3aLzNM8EAakcHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usVPKJEaF4C14J8Bsh9j-VNHhh3vb3fm-n7p0-vOnYgpfeJ052Kg8c2kyUyDQTiX7JyKNiv7mVNtlv24ol6yQ04XH_DJ9k2H9pEyoJ8Vve5mmwAIluXFPkweYYdihTSdEloR13766xNJghtzJ27NAGqxzZARt0__bTsjSnu1Al1-uzV79saV-hJBtgAId4tZbJSkBQJ8MVKHAQZNM26LswtT-4NEnVjIHOuDHX5tEf8thHvm_wHafOAvMfZ_DwjoW64kFrb7EyE3-MJiEIvtxzTUgWqwktQhd9o6GVhLhs-IM2WIyFcM3d1z9NnjyChS4dp48a3kD_TinOOnbH_-lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9rhCc5pjfZ4JevNSi3txqTozK0wgFT3-bOIhCIuy8Jxc3MZdKsZI8RTLP4hw3Rod6CsInHEH3ZQlo2Dk5M2swvGk1OkWxKebi_fAfRFPaGWFMVbrp3sW2A0ZQq7eiBaTH1ymrt-NKCuimSE2ey8iubpyKaokPVJ158R2j79K5w-82qGhTOEkv3UwKW6aeBbX-vxwHRVE7EUk9-MKkJQi54h_zFe3ZbhqzZLcBSA-vo6OH0r0r1-s0BS6xjGBQahGhfE9L1lY0i8TxRG5FZDEjGjpfnXAVWQQYDTo3jsnK6JQE8BwzWkJBFuOvsRWx1jhY08BNUTdN4ydnEkCJJGxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBGr-2k1FK1HqzHS6K5h2QLDrr4HOLCgYbfruj5EmITdDbwinv4eSlnds3lT1aAeL2YQETHn87l7qdKHtbGXr0oKGL6hwIkmu0_tGU09DrlYVz9Q7CVdWZK1o7mlxdBYe2D-T6XillNhuyW21vP5VAVKXbaRxem4tlw90EcCBvpShtbLrZkiD948Jls0vE56LPLw0l2PwJSBQdz3twxPy2TUk9z3nLZ7WsYR1RCVQNg-1MMP80r11zZti6bBjdg2IbHRnYQELz16SHCFQjMSpUlZR-ZpA8oQkk4t6jrxdAFubirHHlM4vYcN8kLLHBVWBK2y4er73l45Fc74RrK4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDzKCKR4Ho8dqAyPxID3O2eL9FHf6Spw18l9rJ7s6R7Fd2AFnuF5qndHGGfaJZqHObVzUsd7QqeHD6fTh_wBI3lb2liHMirtchm4yW9RGhUGt84P0d7mP0oIzOReLjOQOhfOtSo-M7MLFIPAbY89sj-OvwDrI-sGRFd-cMMa_npY-JK3M9rfTM8L9233tpUd2_H60wT6e2u6CRJfeNK42tRH40knuA7vhro9xTPaRns8EpBgvPbzb3DDj8vKkvo1ltmp5b9XDIVRYqLpdA2h97Wtmcxc8xCB4UHgOxGnydhdnusHe8sWlL6w6lYef4hArWzDMES89lveMmzVLtq5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOuaxGshVm12AVQbbq04t62AqhjWiolw6hjQYYD7acP5xlXsNvgDNbUJ-hWkWcsxhsEh31yTgNiJp5Opp3YoFp-gQr3gNzZ4EWBWtSvwQHPGVJjWrYpTYJ_Akiz-udRCn19A_bfJ0JLV7ME2H63urrJppdEUK37gmSbdoJuvjf6lHxPu03KFmP9wSVqQomUt4SUqbcW_CEeoLyp_xm1o3zWa2Jy4wRwS5x2J6034tSnnJT2Rc0zTsgLUeWA6MQ3y5TVYIt6Nq8PmIUHnzu-PMyNI5JwZfAoqjL1FNKWfpRaHIWAA9cOK1AYU4Tzrb_PCWS9UsLq7rlchdOVn5Rk0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suOT-b__OacXvtWxtgJExUAkQ-YN8LsQnY1_0XNQod_cWkpwGAdj4kla4gxu5dQFXKLN9SvjNRTFKivlxb2Jst0qg-VTTLxCWu3cvq-7oHC2-mSVJ-XYqA8Yr7LsEhgN3tFis71XgpDtVrSLo1p3fTrcfsFiPBYnMJJHGNyA0c9zytQiFLRizCNyYfCNJYhBRpM5y8GDctW4fwU4u7XojMLOqHdRGOMrpLX-rgstVZKHf3gESZuLMWWvwD7LKqw67nQNSFgloZbfgtCD8FbPDymz4habPb34zSIzpipywdlpxLrvRVl08_vrNK5dM0RD6gGoex6RgyaINtaJ_QmStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZQTH4WrnzF8mzChE7V9gidvjBu3opDpgoHqGHnVFiGrGZb06t7pRxHC5Gqe0bVCqp7Xe7c8I6yr4UhFQaGTeVpIGmp79yCRHxrVVNoCUfkzKLRv-r03vqkH85l7wS4NW4otgVQaYFtCd2qoEVy6dFQbnJOWDzC8venTa2BIE9dB6EZFgfRX2zYSmXcRqclCpdsp1nDIPoH-3zGqGHFKhC9epEsXtz9BxvcOqMW2ciF6IMkUlCww9upU8OxxEcsITs63WL1xOALN5Qu_z7QuRwPHaCHwt4wF5HIs-66euJaspdAa6Dt7MtXv1cYjAWTWHBemAendFFvKIktGBePHLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZFZxDhFLjhaNGGlGW0QsAv7gNIELzexzSFbcTVHG0p4-iQlnela_xm9MpBOHvA6o42CyCnjkpwTartow0QyC8d96_aCrxmpG-wDXFD-U-w0GobWCgWqW-8MV5wmCIImY4Y9aKn-0w4pwpiqK3K1tNUZzcNubMqOZ3ajb9rvUr5eivOpjTWWEjjrefgny1if4CtLRvu5N6nTB9gFu_4vSo0QBQjG1vWsE7uHiL-h_M0OmfLxv9SflJBSt_RFhdYnJ8jpGyut9minWkra4WuuQJqC8bvsP8J6RWoX0jgp02_bgCuHc0UE2KRkaHA-rppo6zmyIluhFYdtmfpz8kFTAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ0s-ajpzY7eMgOcsbZnreEHBQj46DvrggecZtyKZmFmWQt_McjFzUWMKUO2Hk5RKUt4-CPrVuWQkdXpyVN7YN8kZLcYMggdfn6g2TH_VnooxqpSW8OCqSjc-6Odqc-IEizqvx210lLJzmWblfTaht8vSFVZjE1Tw4d6SFMRGmYdlME6F6qXveVlbMCpZKBXSDR-0cjybQfD_W4d0EbmdsSAtdXNKaP5Q4U4m7urgtsJbT0Ue_p71YqIYPQ5Qk2JQl9yYMw130FHmWW3AAh5MdUpgv-s0k3-Hcl9VS8BwWjgmVSagY_EgeVHjwi5-jtBFtbcYvCUS0tlmrs0tjySQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZykB1a76yui8hKj4OAiTzMfVkNC-91IpA72LCuRDg7lGPuCrRF8EitNT4bn-9gqJfc-NOsZvokkIvYDNsb7mPXfu9i9nNlNrCynvjq0FfFTtXuQtcCFMEw7iHIeJjpj5kvox_7Bo1lvptynYcqJO9Q8rvSm4NcOFcGIBqVmNpOKDdIpUhaH8_pRS8v4R0uYBumZgILSi7dPt35RGsPK2vlvcMdLLkdA8e--79Urgtr4k8GuJiyb0RmezO50naAcyBr-STaExWhEfzJtX7l3PDHpY1w7f1eKuZU3bYhpH8HMtoit3Qgu75KGKDPESSu9meS-A319KF2KDTCxetMb-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3NC-q2Ov4ok4bk8k0lSOYw_LlfEgT5AvHNQyeeYv8NHA20beI9b3Fnr83NLKXnCJtNqsB6Zd15YsAKh8kk9SMtVsXZdsc7919u68JK0gr-rwCd7Jx7NMOwRDzSpMGXi-SfXimEzw5zoffbJXNa0f5KQjvupD9Wrp2p-ONKDakNLLOvTy7kZ0Sb51KJxmVpFdeS3LFYz9JckjZDMsEFsNQe6c6FFfKjHalIa9gAGhvagD1yCFubTG2nz4egxUR1bjltsD8QHjJUGPnbHxU623035nhslfe-V59_tJ0DABz505PYrYRIlReLIDuJfDQV2PNFaOIwyPFVplJE1GSbC5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT7unR3SjG2BtU1WHIud_W2a0P4AdRfW3nL3MAHdAnVqO_mW2r5bfWdZIcCIahAlVCBsQU35JkpW9XA12x94Khe6gfrb_wJBNzIUelgUsCk8KpVeG-_LkZOvUs8ySB0R0Tut2w4-Hq_f_0Fat7dGFu2mNVsiqHCcKtuZMUw7sdGExIQY1yUtNcxfwJyRkcaG9TlYgIGieHZp-Ilc5YYBZ-JNzs-Ks0ZAaZRSn9uHzw4XnQKEUbqSYWbwaZIwbnZWr4uMuAZWimA6RSBLgQn4x5PDIPPFtTC4RdP3fYx7m93qlK8Ynv4Q619911f4nzilWDk78uZnV3agweAHMHMDPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxX04eZOe0-HQqkzOqqg3681nKq63iCGqgef0P-NoxCTNFKi__74dfAN9XVKzBR9jEGldqrvNlM54Fyv0HRSq6UdYA6xL6GVLlklMXoA65Qi72rGVY-9gB1o44eVkSvtOa-TynNUt7C8dwuas6FTNoUBX66U2_QStjj5rmnRslocGTaEU4mpqD8_x8xr12c9O659lJIYLldp7N5P_Nj0HrIt-KZ6F6wqqWWFtJkSJyxTMfaomgM4GbIaIYZHWjp3PB1QtIQDxhaEDj5fmF1snFjRNDtCqMmfJctVgd2wM2pRA740BROP91SVT8uGbQ9JSk623ZfNZqOBPkTvOwK2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPb8vgwmHEzYdZR71Yue7MFA7cmmPhlofEBIxD_OynVQDMrR7LI4zMvmiCWRfeoyG0fDx7Kq0zCVcIfvMxuKt-vnmjBhm1S8D9hvI0Nf2KTqx7PUmrZPm32gU4Yz21RmbMdXzR-akuX7_vXqzwo_17bnuIkBecnPikXjCE5ik2kZgISy2D6Zq_QiA9SSyHrE-SZGIe797DS7cJ4wLqVGkqHW9Wq1nlZFyh6VvYCQoNFhlkauZd2Eyd1ecy9L-wX7ImpxF3KiLyLMa5yWHVzFvrPh_UdngxQ14aL1PIszABI499J6c4MBrZ2_HLe4QMfLqfa5D7Bx2o6gHwSqLmpXyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3PBKXP8pfXcTmTmuYn0HQZrdHmG21ml3BDTfaS8Rvgii94fdn4lJuHZKmi_pbaXteN67z3cTQXfiP-Sh8u_IYPrUzSmdWc45WYXyTP0SO7piKuk40OqyVbeUq48L-g2u2Utn9AYczyUfZPJ48LVsH-haIeMNhiTDsoeIOhBKPAccUpeYj41N5m40uXcQY9n5z26exTm9YBdaMipOK896KoEcGCPyyWX0FiHsarDhd4RyirSrSSUun6Lte8ECq899StJk94Yt6iUjYix4V7El_HM2UQUfI7rEZGhmB3tGniW0bvSX4HBhFmMK7Ul2yEoQtAypl4RKRcvAhZDCEDlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcaJ8CWI-r0poEh9R4CV2D6V-jTOhsGOkdMgPEcumBB52p-PUm27CDIWcEh4FXszKvXXXzzlje3_W8LqJuzRBjNuRRMYDZaIuA71PgPAjYhjFPMH9iDfwFst239sYXJoGnSLfpxW1VaAkY-VzXa02N9B6LA-A1Q96AeJUatTnhmjpSiT7SfVTEMshCA0Xc0K6_j5REY39GChbDnOmONfuBWHOoaVv2gNpROmRxLvNh9POXzkns4zF7IsFZW0KKYTLbR_SxC-xkYj9OAOONK2FMyr9pRxkSHwVhPKm_mWWR2rqL3NzHwbC51L8o6CmEaj02lOZrkhMIsuYmXSOqJFnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu3aafhnTNd4u3ng3acqgl7IbxM_-bGZQTbj6WUizTGAFMDT3XYqGGB9ag-4z3DV-58yekPsn28yqLEa9L6kl1E_3P_waPjzDFQh6fUZnLx-icEwfT33eQbSUcAoocMi1gwNeFbDzN5XSE-mBWC4kZb_oR-YBkOTs_2gOJz2-FtZ21j_Pi97yRAH10KI9GL0w1IYP5sS-ZyI7_TjUjOl5wDBdgsF4y0aXQa1fHiu_Qgv9QJdyUiGUEIi_58BP_17PpRMRocalqJcK6oM8xEdSGrq3mi9fFqznCUrEY9vBvyr3hnAIkyrtBXAtWZQOFSizuytKVleuvUe2Khca7kyZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff45QvNV7SxPhgmcML4HRv8uxlOOrXniSI15nuif_QkE9nD4Y-ONz1qwNQK1jU0AnQO7mg8Vf8v6zjM3Ci2h7drmAOCnLGDEXeSi8CQmpyPuzF9dpbLop9QXsYEPUlyOot_vGVRzPiqjlNWUyUxI-nurfhVqR3wm6Djjtf8wli3VU51gea-GP6eexlsbTldgONwBTD0jZLgi4yX9Ln1bwD-kqtsLQ8z6pldlJpZdL79FzbHk3qCBwsqaOF67u0sb-zzAcTH2ZSEBDALKm-Lf2nBD3Ojxxrp_jbi5N21UoUbWOcEfdS2-Y8VWBEMlLN2b-WDYplRQkgDZbO8VBpuuTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciaGOyKpXByRvHqnxuwYxcrDFY5cVlg13wF68FmrmzmIr5TcRi17ZoWAuYs0kQ8VamScnDAv3QfeC7E0df0R1jakrFCoF4cN-0HTVDijneNC3rqn__Ji5ADl3hbYe0zPcJwQFr1blBbJqEIn54VVvwfjiHesX3OkVo5aHQpcycMG_dtuVG8Vm9WR9ds-kv3H3A8tkORH-RQ1qKUDl2sioBPqeC2pObfxY58JMEHM_uakypN90dqcTnLS5l1zjfct6Axk7QXekEfSzMvTnNWBvn8rmwE0NhJ1NturrjXHn-lsgfbIZc6W5fiwibdfiIUxTLnHkAQnw9bNvFKGZdiWgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtYkXW8JkUf_qRs-_tVy0zwYowJ1UzS_iOI03J0OAHNe9HdaeqnJ-VfaT5MFvr2jQjGyWyYnPcA5jQJ_6vQ94bOZBq497ADUhEL-80ds056W-ReWw8Apq40w6BG263YxkM6sNILENNk-s1JUFEMQG739bbJJbQxmgQe5Tyc4R5XinkOAOLlVDGYJ3KhRwosnUtnZhAtNqMK2iPnGDLDZwLvh5DaBnCOItyrrQaADZRhfZeNZ0zDtBlUHGrFtyXhpxZOo1dztVqjhQNZw64HV_u52E2cBknSfiVz44OS5fR4zY3hcIyom3WQNDvd_nzltUMqoha4nO4Mw88izL677-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcms5xXaCrDTTAhchpY-f0wufgBcX9ksvpMoGpEsIIPFPO3hiPiooQ1IrRpFYZ_ZB4l62xzhMGFUsgo53uUHUmH_jZcAhvbRfcMFJXnl0jGRK8oKmKpcAQy1xqgydpNGyGwVqyFDPKqG_VCjGudtJshFkn3YlNEf_YY3WNEjhRD1jNuG91xKP5qNAYi25dgwz0BCa4EC01CMFX3xQEiGFtNrqoloUkU-m481MXDXptnXPbSIbpUCkimcQrGfxl0VNXm2i_jmG-FLj-DOGmLkVCX0oNZD5oyv0pBP5cSv1GfO1aQ146AYB0-cSejhZTdcv0RP-bFUxHURUtMDh8YbxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IciE8VN8a-KIG1cOcIkvCM87brw8eYtIVdbZo_NqFKw0lQqfdBeyhJ143hOofSheufUAqzXdgHFZl4EjZKOMoVTLRwBCDnb09UR183KmP3n7KP9yeT7CqaPp2Xzv-5assrQQp1ZS04Le6m2W-2lvy3JNSTrXUgHsEWcF9qVTrErBqpXtM3uA6tlgXW-y9XhIOmDE3M8OyC6-8cn10xSufWNadcuW1kSkDiB2ys_1SZV080rrtT7mFUJ5B64kUpoMlHhlx5zSU3REUGIWSAz4vuhT5l76wH4QR2P8d5gQPUycB1MMCRsYbJBmEw5jnpsIdcMehK8ezCw000W_X6YH-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FClnJ4mkBv0xt01Cj3FC1jKWQ1da_Nmbh75onc29E9QExyWNEI_vD4nU0CUzRJ871yVdiSla7uY5qh1TOzZQsWVvrWqTmPO4iqDwrlxPG1vBjBq7TCEHavEMbUlpaGuaL_ZMvZIDI6DbCi1WR8qN6vRsCXeu0r-7zabGy2alQ62ts8u0NXfZPpCrf47bWQDBFKHLLmXrvffvMxLdAr7v9bRopEHQc4rbfs_vlb_d8yf-IxaEo6zMgBRnWPNB8tQq4UET9yOQ20kLMM6Lp9slx5kqjkTTjZ8jqXYEnBbZTwZO0nRJMkGwCOeSawEX5e062neYQL9IlH7sI4uyVUtiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sknmGK2wiM8htyP0QLByr9LcsFxGOgRIqeYwlNIGAXlT9pwyMq1pv9bNRjwethE0G8pqu2yPCcoYJQjWG7_SiuI0bdaSVbSdSz6wUMdpItZMhst2bwo40RmgYb-nQ1fIaAlR0RgkpWuyPYQ5lCEvDSI4pDFCr1cMZP52Z4iCq7km5F6h5RdAbT6XNbV5Z4Mze0ufeo-pT4oLqBjwMsKd7RpkPup_10gXXfSeETLRUDorC1XcHPL9ELiqXkBxfRjJoBu02kov4c89Ho7UkejuZZ9-8CIvEc5D0DhlZ4uGKsPOsRzI09-laMLFO11wJoSN1_8R-l1hVt2z7j1eZ5QJrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRTg6BhZTCRLBs70wMYiyNSfUTtvGTPNezUXjVuhGDoMogKJ0JmtDBkr7M5WY51-VOIoKSPXrR_IFdRvbhBvlnJW8vl2gym4DLNXHNMlDCtTspPJMOD2m5KBTZm8qAL6Rx8jNCrj741pLW2CbBRQr1cbxLPUIPV8e_2s9uXuPvvm1QKZ8GPYkiJeYWoMHhpmaxmR7XgjhpmwKWYegehBi8C58xyWHaVZ_mrd-gL2NhWiQRk6Om_kHN2EnE2tcPFlQ_Y-efeNEfZfKgy1jjn-s_W2HaODIfM0gJgk8Q0BgTQE8hjXhQO5_OtNNhDxZt0-oPPjcgHA_kaLSMZy9RXHgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWr2-RttJr9N9V-Hb2D_xh9jNZeHFfJe-VY1tako-9kiDFGbImk7uZ7VEX6D5UJFgXOHRz3brMgF6r7YOwYji83mW4idPD5NYFWRtVPIh2ON32NvrASVIQomGDSIrZPUoExKV2Yl36h92Z7lPJ1Z0REKjPFUy_C56BAyKeZBvbAUevpHEnHvUGM9-3LjX-f9HI8-u85-MYoBckkkB6i3U1o0q9Y39UoHpYLIGnX0_JiZYQJreG6OZHCR5rlvKelt4j5qZsGyHPTyDH2M6ltkv-EI1_7EpoF1_KK_iqECLaolPgz8UNPzexRw-1chuY70YLK9WxYTsAhwuWbOC6fSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txPc1UnpJnIuab9yM3S9TtZQgPJCc7Dq431DpavYNSE6lK2VdAgLqLPNrGlRt53PV64abgfkqtBFypIjjMe1ZusnZ51f9sjQkcxr3QBjTmcgHAQG40LjoCrQ1Hm26Gvh1wWN-AL_0ByEtlJ9CiV8fbgTluACIHgprKG5u1gM8UZLDx87W4D_pd07jYfOE_FIF99g8YVb7mI-y4Uxszv1f2Iok79pVrmec145gH_OzxprbzQCTl3rgqRcJ6b0_LDy548rSVTWyv2f5I1S8l47HW6yUztgrkLyDag2FQfR2qwbnopC8ZTp8gCNls5VQNZfEllhL-f2yxmp72VcGQXlVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9GHfjIg6RUUm0xXThGUh38skWYvIW8z4XggVrelI1JLfExbTyvU0x0jnOVcedvmfZrQA3wpIUew08-r8G01ADwdTHr0KmtQbmZuYJ7YQaxEN1IGyyuFvfEmBar8jP2D504OxFQ-wwYDiTpYu8dgWpSbwryE21kB0V5ILO_CsEFdPwOSiW7xa8Tn1pDfsr-8CToJeOfebiKzf8JWSujupIbT1969e93fBTrdxbPjgI7VHTjo8IEj45ENs1JBOAUB58UorXGtdW5_RqzAlwnTy13wioeUnA5DTHIkjYnvU_1DfTgDbEVF7WgNuYW5_84yhvALYyS4G421B4iKg9qgYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSzy024g-h_fn6huGWXoNE2jRyk2EaiyiPbksTu6m-D5Zi4lp33iN0mNWFFMJRhZtOYUb-3Aq8ElYARsJVXJMYic2ZtT5rdaAB98ALX8WJNlXWBy6QZoBZz4M1DQvEX_EdFp-KTw3cgjjq6WKwHC1pnI5YJWpqYQpRmNw6bT4nO0Xk77o54HexHl3kbuKe8v5nSAIhoEbSR13EXrWqhZsJEVe4YFn3i8yGolEDhQ1N_fCs9TpG_U7x_z03Nl1CltyjlyJTo4Fh1MqcBe2yR_krotZ4-b9BCK-_ygMjhrxTkaxDQnXJRe0gWIKPwjY5O5sRI1OrkjtHuLiEuSzXL8Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxN_nU96VKcHjRDV3GGEsRZ3Zvd6AJ-QK_a88GzAhGhL-VaqYQXI85AWHWBh19OBVfDlqEhOIY_3TbI1gfkbDvHPmHr0q13ZepWOTlQJYvVEGFDADLwN82kyVmYk0RzR2ZkJU4Za1Igi8svV0ZLj5w3gRj9M0uUpA5jtEmy4EF7N-YeMWYpQdKvA-7_VbeXQqD4grLQvvfM6TxoptheNLM_PxGWfl73wppQZ5uuOmIq_W4DqcIB2SGAuuzarYFj2bdD9WzAptIxqGRQLjQSiSiEX_kzMoVopqhvAct8k3-yg7QnsoxDzZO4ox0IqObGeenG6M3SS6NK-mpwbTZEOyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PF6JKCitlDXXGofBbhpejXlwPccIjt6X1k0PcC3fjj1M3tPHs3E9rzXdjMJ6Z_ZrxMuPFyifAJ3urcfToMpLoqweAjXgRdY8mYf6sqDKdVDEKTdY6rqvAotWEwZvklvkh8K-3e6E8c8d6TKgxyfl9teVASZVbp22WEczKPKDt1yCot4BTiuRma6yYrEkOJ9cP1yvuTj0fsaMWpzS4fwe3BmtGb28BLrqZUOMd4O3wKmfsWOQj9cGgto-2blYu-vyI5Nm3HZ0Muh4PfTD7hRWM7O7M1wk3w_RSVe5vIigleJGmKdnVD5t4EnCIkE0sNYg-rrJT_8uXiarmAJOLGdAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHMeV7tG-AHxEfoKZejyfHHec_76jEZRyTTRGxdoR20-dvM12YVs5yIMHOZOoNoufHWyYNf2b-SeNVklnTQUpcRodHkYqSotuDulm8vT0f6s6uHBgB53BKK08MW79nCVtZkaRM8wVtBvGWpminp-vL-EdVt4Q1KtRPgqTGGtvcfDuFdW5xG-hdJo4yMceT1CHDg3bmqYdbaJ4GJPAo8KLTldMTCtA89-a4FGJPo-tgl4GpupCWXOLfc9h98SdbpXWhedANm0Q_mD2ojG0G4CzWO6Acxg171sxfzkZvA9EVqIZbhgNv7hJvf1Lnj8NcelkJ3-9KM_iKsa8kCKmDfqhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt9yP0fOBSPtNTzwNwIXXf_rCmvmAhKJuJRMKDPJurQFobr0xT9pdkYG2Xt0tWBCgZ53yY3iflRrA3rww1EwYM1LEr_w63jeBOoUjeMIXOgOuyoI4oCiKCa37f9sC-A6CB7sgDQDaZNGjbyU2BOkzbWyfGWyagKSHiAKDfs6sjmu02h6kqWAh73ttUF6HnTPx37m7rTgIASWXArqM2nnfG_AnWHSrO_l4E2olfxnhyrZzT7lrATZ5KoM9eJHTO75-vTQplMeTbErU3cM0s_kGnNtDBg7_LhCAStKJjHlHFv_hsPwI4qlb36clBcjKqDLAgGPNsABzqUbQaK82NAQfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAxCxnUvIvZKRz15COzQfAASTU65ieuNe9yCI8QXp1JwRRW-iXZ-O8odgI1BKydxaD6i_uENlkvyMbWwr-HJcwXzhTDvXf7JXpKwRm5nQRsIjV6X_BsbkORgFzhZ7UBlTFmWPt8lz26yzfmfo4Fdpt1nfdRZN3aL2qNnv_RlBSvLEFqAUCvescRH9beginJeQXmILHelCAejBHufLq8cz4WC30NoBponifIW_R5FBp2msQyqg2e1nPFgebdfdMnJAL_01DTLQcdEnLJZ8YwnKpxYczeGz-8bf-s6QCXB_j-yHfqSgNo2ZaLQK70LaPEcFMCHwFx6sH43JO9xlLWYVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azIUA9jyGdMU__if3IfCc0meTzbrPatcVc8eBqToOEb9d9AmzUIy8gVHpVvGiH3K_R6JXTJhFNvc1Vned8r_fgiyZSEixg2d-_IL2_hvx66CY3iUfLitTKBfsC4iur2jFh5qIiorp_7Nticd2mpOLK5w7RjW-kq1snTVWHfYCyyRTgqK9EQaC8mob219-i4szBRcRkpautNwQLnSuCn9W1EHUjlpgBrzaWdIF-QAIGvzmChJ4wyIfEKe1w-0bdQRGNPh5GYG9JTexNyKZmu1mvtOWHdYDZSckor8HAh3uwa_IOQShsuinDgajwsGmqgceMVTRAxntaY9lpdvaHmH8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV0J3IWZNIz9OoZ7ETXxR0rkSKJMWpL8_iBMJZfhGN7y2zAXUL0dLV9X81xGY019sVHrXlGW6t6SGd3J8PB1-W-WWa_2HMR-7l2bnyHI9IkgMiL0rzL1D7qhdJMe6agHBSJdnqhVwbiIvFlZk-FIWh6BpnLAtnXThz65oa4rKIlXYAURzAh3Kh5q5fl7Vnd-i6nR-_dfxOIc1DpKPC646sJ36if5aBygZsEq7G7XwYiMABk2uL-XiF_fXYmqxrC8WhyexRnIohU76ziWSqqZY-lFUoY26E5vMC8WMGxnxyI4vM6RIj79-A8XWtGRRuD7a9m2fhArWWj2hVw6_UfkbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rCTyEDs4E58B8xqNIMMdfZSdnD8XrWsmnoEJ5RyBmKZpSzWL75OoweXHA3JGVnx-lvcZqBkeivPCwD10WukUO3hHWgkMWRVHyXZOqU_Q8np1hGSS_IgshRx0G7eAtiY2Heci5v7j2YmSIzMzV5LsRqfgs31DvgmtM6z6z8k2hkJB_texKv_Zx7J9PpOegW1ZpbbRZr7V5Oxrs-kaB8tQ79KQo-21POBmg49OqfcElWwN5XHCQE-LhJUjtaLIITffLHqoj9a9OhHHejA-mVwccyTU78-eDRXz3_HuAFrUwQGeNDbbdtRB5XXzD6xYswy7xqYFTl2XKcKoLRsIQ5Fctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=rCTyEDs4E58B8xqNIMMdfZSdnD8XrWsmnoEJ5RyBmKZpSzWL75OoweXHA3JGVnx-lvcZqBkeivPCwD10WukUO3hHWgkMWRVHyXZOqU_Q8np1hGSS_IgshRx0G7eAtiY2Heci5v7j2YmSIzMzV5LsRqfgs31DvgmtM6z6z8k2hkJB_texKv_Zx7J9PpOegW1ZpbbRZr7V5Oxrs-kaB8tQ79KQo-21POBmg49OqfcElWwN5XHCQE-LhJUjtaLIITffLHqoj9a9OhHHejA-mVwccyTU78-eDRXz3_HuAFrUwQGeNDbbdtRB5XXzD6xYswy7xqYFTl2XKcKoLRsIQ5Fctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG5URVMGa4cPAtERsro_Hd4-DS-VEhKTSvjzBeSA4KLeUPLHqC9ihAgqhENW_LC_bjefcepkoKhyRDbq96Uazsa60xEXwI_9UCAeYjTtJr0k12JQ139pEhGhYEKIf74J19y6IzmT6ir6xYowHcLEtNJR4A8J0-0WXI2kILYOVEe2pR8dmrNRWbUgo8f5eIg-eREDqotYDpghX46cNsl-vAZyDQaOgJ3GDc2QxlROp3wJgZK6m_yf__TlB-xQY_IpEB5KEfoy3i8peealskNJpTwf5lZ5asldDpMHA3Xgy1JHZBdoge9zCsotOOAFBRAC5Sn4kg19JB0VD0R2O7by8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgRWVTkTJfdJjvCTmTZ5Q5IkVllCI4ULs3w8vidoIrneo9N5X0qoQX8S8jxVPYZHpuxWgA1klNYFLf6oKaKoEr8fyjuWe7ceWsZzQhJC7XWrjLfah_Bhdta1kdWlNasz3PHX9vGO0rWYmCz6SrkT9TtGT_0SAyt_nENp-sySZ__D-tpoNGdXeSyWjLnb0QHBfjLtR9rjpemom6UwmqNpf3BzkpR4iWK0cvbj86bp22diN99vmktTYjMXplxVwhxAYlOqTsCr00XLDwGJSoCkhFTP0qL_8FRG5PAkxl5GlHEGbUiANpy8agxeX-Cz6BeGfb1yIpgafJhgXtrLFog-AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGAQLQ1Hz1owWOj9VE83NUhv9rfqtSV96Ikan2fU-2wYmjr8wmwj7_wxjttJCtSelePmpl4dpUi9zwHvhZEVxXHjtHPBL5lvfS0C1Jqz0PxKs2hbqULVW44gy2-69Diig0BoQFtawzFmSe6yu2PvONSSSwRPdjHRHcIu5Ax4tZ7x1JA2gBI73LL0HO88Sm64QPFal3-xyvPI2vAMFTtiBvXOm2BdasPMYWjqSUvTP55IwRcF4zWCnf5rgFx1GxDsusIOrAxdVPfbtq4emDNgf7NpdFXizGkYtsKOAdNfR9xbqFqKrIzPN-Ekimzu88fVoS8CnxC0GOn8L7zW3u6sOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqmvxdFJ6FbArcqnsrKcEeMbQ6gs8Y9lr31dYt1OTugdqqgPqI7zkwunJZ56q6_i5kSI2f8qLhhMTHfpIP3-5_E67DJaEp3E2_gr0QKE6cNmQfG0al4UdFZX6ksPFfbHnKdrZCWtEGj6IlzcSMhBN0kU5tWicHarq2j01imnT3PPlCaiZyukQVH-WREkcSuv3JrvSBGitkwxqRiWEn3F9_6jTY74oApg7bLyydr5k1W0W36m5cVVvDdZLZv4MVTkg58irih1CO1NQJFAnRZ6xbB-frAg5eqrd3cV2vA1tNJ1bNtoFKZyPU1ukLAbpmiCSyR8Z0Zjn5jHPrO0HZV7gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8DDEuQUTUTNSg6RlvWCuq68ZolDwjpI1txqs2b2BDS_GXdKbv5HG0Z6nvCIcFGocKMxRkbJL9yftxAjKrDfrm4KXSCaYEfNKxRwY_QmEf-WlXNtSxqtcTzyZheM_F5l_qX1RvNZnyhXh4j-94hnEFNonqr7c1kKF0_UXK2KSuv7X9pcDAzG-LFQ5t7zs1HsN1QxBGg6IWFEfzfJ_IQFClOklzmCbQJdoyA5KLZT81SR6x1UzyWtNPMYOZhKenC11t9aT61Xt2vuOXB-VllTBRK170Zj-Qwv1YSkcHKxrgga1mYV142G21jDHA2kh17DNBw5RRYMxY_339JpGENMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Res3RreFXCVuUAwubrkMckn6rs0EcvH59tJepoHfsQ0c3F1SF4124kxWP1Pna35R0MsSzZHcquFhsOXWv8WIMbRqXwWfHKYWCat2VuCaBlzbADPRYFbCGx1dAsJA34zQPgyMeNBbUTow7kC_NWDVv2yDw7MOaU9i33Su2VvWmH6_LkcymLdReUV1Go2HDOGR2DxuQelIczXqQFjaRhr09HrdHUSZE8PdIX9bHwstXhmQCVlL7wVCO2TR6J5GkvrGq1CJiWULtqBO9rzwdvupyd9pEtGGSbgRZCUrTcIs-TOxRA4kpD5glVpSIcYQF_vO1Lnv1VjH94bWjXHW9XTLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHwP9mfwlrksNO2pqCMYUt5y11YgQblL9z6Mwdmhw2hz8yIUOPI2YfoyBuwLnpZCpTALW3AIdTOD7ZnMmYRxv1eZcr6iq4m1ZuuF4rKJMWkqbFoggCNQXz-Os-4jH1DamZy5Cja7pYYB-HA6seYH0wZAikYa-gNiGzVcfWqv0EOSRPpU4hic7Ca473sjMxL4Zstv7uAAmmY-t1lcQvveVmkkBx19vyMCau1DeXygTdeBxnlIkVgh_lZ9za8ftLC0ZOvyxAdlmlFBFCvGH4FLgdlMAiSsFYH61FF8jKFXfNCrR_ZXtgNGjMPGoiyb8Whb_iAGj6Bs1cb8QK_e_QecHg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=mrwKikgCQMaj2U8ki_DvOgXLZ9W7vGD9BUJ99pPd4ivvGEsoS_5VKD05ZokxgO2h8ed51qpbn3eR6aC-pKria9fkuTn-_zxZA4jOsxh0DNtXppMzY1vhlukEzAkfKcRvNPz4-cxSBO1fleWbJNF1mUAlazL-5FACpYH6DPVqiwqJFm71RbnGBJFEjFsXeCwzlXigB-gp_zsnxL-8hFuyKUlK72gBIuKdnI_fBj51sFkSMrz-3F7i7I-B-d3MzmsCjWwhAWU_qSBe9e8lcdC81DAGxehRtHFAu6BStsEfGwTCUqhAuiY0jYWq-aG9pJv6zkspgbnZbjR-cUrG8wF0HRW3tmCw8c0AHOmnr7PbJBWL_ILUM2x4aowwEhPc8eIVZgCEhYfqnMuEVxFY1vwttfoE2sz9648eMQ1Ru58c_EbTA8Kcc-kHchVpimjz0U95x5dG0G43INuR00gwTNGjU4lhCFNxxz8RMvnY-mSrzsC0744inpTReGlHR66bEv9aKKWHJQKPNxk4ITj3QnUWOIya2DstIqfgrP4HFbHQBZU3hu7n0tKI12re5t_k7bOWsnbmTdaNUpxNskaQWSw74dhEZX5HianpzjghTrsb3wOMfls3McfRqGdz4jnt8rTrIKBFUfPhMAf1yxTk1BkqVDRGiEAKAZT0Lm2cL6dEfxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=mrwKikgCQMaj2U8ki_DvOgXLZ9W7vGD9BUJ99pPd4ivvGEsoS_5VKD05ZokxgO2h8ed51qpbn3eR6aC-pKria9fkuTn-_zxZA4jOsxh0DNtXppMzY1vhlukEzAkfKcRvNPz4-cxSBO1fleWbJNF1mUAlazL-5FACpYH6DPVqiwqJFm71RbnGBJFEjFsXeCwzlXigB-gp_zsnxL-8hFuyKUlK72gBIuKdnI_fBj51sFkSMrz-3F7i7I-B-d3MzmsCjWwhAWU_qSBe9e8lcdC81DAGxehRtHFAu6BStsEfGwTCUqhAuiY0jYWq-aG9pJv6zkspgbnZbjR-cUrG8wF0HRW3tmCw8c0AHOmnr7PbJBWL_ILUM2x4aowwEhPc8eIVZgCEhYfqnMuEVxFY1vwttfoE2sz9648eMQ1Ru58c_EbTA8Kcc-kHchVpimjz0U95x5dG0G43INuR00gwTNGjU4lhCFNxxz8RMvnY-mSrzsC0744inpTReGlHR66bEv9aKKWHJQKPNxk4ITj3QnUWOIya2DstIqfgrP4HFbHQBZU3hu7n0tKI12re5t_k7bOWsnbmTdaNUpxNskaQWSw74dhEZX5HianpzjghTrsb3wOMfls3McfRqGdz4jnt8rTrIKBFUfPhMAf1yxTk1BkqVDRGiEAKAZT0Lm2cL6dEfxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NreT_YncFRy42qSP3qipu1xlphR6-2viBmCMeEzBi8y4Ahpt0WBun7Kcf6lQCLK8Xm3SJLK2SRlfnT2r4cFJHvmudLsbrYohQokf6tAX5E6RqUfw4vC-GiLRnbf3AFwshFUsMh3gOkXbHHRY7l72Qy1zD4Ci-_nhO_t7kChzq49LTTiE0Eqcru9szQYvzDkLPHmsKw7vtcSUTVwm2kndc3gtEBC3lJsN6WXA5wYJ-BP7VFaYHo2_uGK-LisfDxPKkPpvfWD7aq-SN8lWx1vwl1utfK9Z2tZFziiXmgavMNabh6BldwbovqFthlnn3PNICMdXFqR3pP9hqxe14TgoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENbV2Exq7jeOyl0tIr_bZvmOu9hdUsxjkv8sjGSVKrccOQpUcXApdkbAOULwDhBBPSMwhFy-MHtvZqGOTtSWOBFrjYrRMNktnFXHNLV35BV-qL7VPFm0u_qgoaGePMfcUdje2JgwP4t5RAVFxyUVc3jjkoUZVV_FdaAT5mpQqecoIytMXTeF4glxFqNH0Y3x9GBFm10bxJ4j678gZuvoWou_be4M_7s_hQGEzHCJrMwyucquHP2XiWcZ9Jz_jKK2XwPrxQzrtUCe4j8U-_3DkmaR4nKLAZ6qNs8jQD6dqnN9avdujCzVxLTM-2ku9rWVlTFNmDt3oTHy1jEkylgnkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlRErIXMsuE6r_vEtE-Nq-voe3MxELmh4DMrqRkvy4ThY8y4AinPk6Mjt70ISaMvyrIOtPTrwZCR10YYMYNz0rP0W0q2_O2i0tKm6Ve6dMUPdOBUWAw-tMOwBrDfrAvfE9mZmGjWDVI49AIsBbBNkdj-ANRTxsrzZFebYeIloNFdgyk-8kjoD8BcTeKKmE_H79vBM4DtEOHFiP5YLBVo5HGV3bzQLPCtY5JFryYJNho05xriK46A7NP8zktIDnbmIRbjPLxjm7syLrM2P5y4xVHn8JRKiv7twOksrBQhA8zgGszDBWm_neDjmRWXoXg6Q78dHACPY4tGPk2BThRe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2RPA0a2GN3kT-z9JLexH1EYtgN1zL2z68yQAOsZ4caZc3qj8GWCPyGJwyn2oPpZ2m8TMY169IJ0wv10NVtMijyvMaspY5HBeGENLMH-JhGFxMqMIuVh0SHQyi7INFS1qvvzAmZqmw8Y9OaPAih5zaQeKqUVO-N_HpKlM2-wU1xovl8tqXl2AN-0bGCO1Qnid3LCi6wkrjwhinKATAJGmZfAL0YlCxQsN3hempqbram0Apyfk87jmr2CxR_rMSW4SAINdZEr4fkmhNVlj26ne1MLm3Zp6zJ1--qnbzCLPyG9n5XVmCQ9eyqII3ueDsTLXYifldoYQ-H3BEC_T7vHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwBd8EyaZcn_ObpXCM9X0Nky7rqm4pUqZY7pERdQHHvAzq_3IxqOXYHbWKL4RT19PyHk_OdCZCDC8G2r5D4leVeNqfV5Lf-KrdLuM5emvZMOH7EqAPgyW5wmnqPmQS8BXUSJN-envJ6i2znDN5EdR9TzLtIwTjykFvyrjnGtcsDiVHkYisUPf-B7GgC0LbNsmy4PVV-yebIvMdxpX6tKlTTBpXvs1uEoGEMmLZOKV5mlo0RSw-Ybwk7NeSn8NLY_tdespeC_kdETnu5vEa7F9Kc-cKQZ8i_uFkt7KqTH-qmJwHKSgtKPpanyzK6RpGuuuzkLuOReu2HXJMXXxfbG3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UxmodbKiEVDYSz-VDlImnXs8UgWM-h95lm-sgQiURgovXpyk05bjXabxCbU_agzfmsR3l4uLUtjyNS8HZUr1M284ycCrrd9YK0KqYzjhbu1H22lGG2itb12yLIWP753ZJRtJNzA1FBzyOiP6KJzggsiWKDlkyMkYUB2vBfGGgqE6PLrrnAw_ZCGnfM6LYYzoAQZ0p-enJa3x8tRWarg05EO1_i6NZYua0eI8ro1fmPHk4n5G20VtIvk1eU-mEyVnFfjRCQ5qRZLU9kUerkiwLrPmHgYufWGC3MXyEE1MMbW_pWr6AEawHMZd9EOwucoEVcfmvDH4ygoFaM9TpWbqTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0UxmodbKiEVDYSz-VDlImnXs8UgWM-h95lm-sgQiURgovXpyk05bjXabxCbU_agzfmsR3l4uLUtjyNS8HZUr1M284ycCrrd9YK0KqYzjhbu1H22lGG2itb12yLIWP753ZJRtJNzA1FBzyOiP6KJzggsiWKDlkyMkYUB2vBfGGgqE6PLrrnAw_ZCGnfM6LYYzoAQZ0p-enJa3x8tRWarg05EO1_i6NZYua0eI8ro1fmPHk4n5G20VtIvk1eU-mEyVnFfjRCQ5qRZLU9kUerkiwLrPmHgYufWGC3MXyEE1MMbW_pWr6AEawHMZd9EOwucoEVcfmvDH4ygoFaM9TpWbqTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSgvBKCsRoKb-3tpBQsribmpLL999wTHhV7f5ucIRHOjlZaz4gTKc-T8-9CPsiUyXZYUJ31BSDM5Ity7WZ31RXvVLRoxvMl6OhPDjZakCaNinr9cnTjDbfyFF9IqJWUIbrFTRXkq-VyyGcS9kWuufZ6T0vknc2hH0lwqfRyrDdKNtKp0nZJVVWKSwHxjSxqQkKwaMle1vX-U-X46cgU1zX_gxEbPkbumyX9MMCMQy4dPvQqQtu4j9mDnbttVQkeXySX78FKy4Mn77B8RduOR76HyIW31it_QhARww6A7Z0KhQQNL30Z5tTiOpNDKhEolFc8P1fqeMIvI0oH_HxWvCA.jpg" alt="photo" loading="lazy"/></div>
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
