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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 02:04:33</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 244 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP9aOn1physZNsINVAVigTg86GlFnPguKG-sgcH317VRxuqlbPUaXks6xXmyAwxB4z649ylwm6ftkSqD0zXGBvqGsKCnCDpGEruWcu81e9khGwPOAqZHUq3Yv7Lke9fthYW_ncaxyXnEU5LgspTmqiULMP8by8BEvqKNL_HKhhh--j53gv9T0bd6W_T1GCH6pFME3isSY2Q2omraW24LZPTQ4J1-vhXK87BoHWuNYTKuD1PL-5ZqJmFpWU6jizUoWwCC3l_qVeYRtyqPLod9QetJ-GV9lbfnn8CNkER_jMQD8G4XDJIj53cx9Tdcnzy3A5voj1-gWjQxDtnwwhoc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 480 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 643 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 743 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 752 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 852 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrmozK5j7lZ3fVIDNXOH__AdBTpgpdeE5ANGd8OcWZL1JIXyZlCmEKK3kyIf1YVMaQU2Zy7LqtJT7o2zmn5N0_eLDuuebFDQLXx22j5e-3sF_tcPDxhVrJBfueKP2x3FTpnHlIVX1Y_hVDFn1wuI2IfgrTlJsMzbsqGbx4n7JfBXUnKOUJB7ZC4WCNzhooog58jBY_g6sS9pAhkpVAkn-WIgCH4rAy8PHeAtK_LS48k0ScQUnfFAz61GSNacQx3dBwz_V0gPEMDbHLB2-34zyUs6Ewn_M72WrjCW7ukgPsI5QQEvSkK-N7pIdLOrAoEDbERJ7tvYnJaDOimEAA6lkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oM4P8egNinMjquUuOLgavF1ZsbfcBc8tTCXJLw2gO9E-LTpj_q4Q7bQ_ZxratiFxE2jkdWsHHa1cLMNv5QFMI02JDibbWMrM4Os1Uq7j_80_EiZjlsnvIPqGjHdhkQgWF9hisFP6NqkmxNfrpY4JrWljwxZBSo8FtxfJTzBM5MGeuGK2_60-aC3dcLrUjwcIOPnugQyZdCoU7vGjGFTB-dufHrot5YlY3ok-thvElLEb32U4kHrMjComPnX8uRjpaTc2fxiTjaDJEHpRvWE_rsRe2wiVqSdoJW_qmYC7eG5Inq6ngJy4BaY3lJvIAPCPT7in0uVGEnfAGqYYSA1_tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQAM5Iw6efYnrPvop68dTH7Be454Jgs594U3elfyK-fKdEEHKCIoUNnhHeTku5qd-WUu13VVjqWa29jAzzsf6SxKQuX3JJ0cYquXW_dm2cEoGczBaP6sOPNBhkrSNY7XsiuW_D3Ufq3W_TYVLjykgb29XgVOdmrI_AhNTfU4GPGt_BHU-9JB-jlPVO7AsxN3G12q8EDxdRVS-5FcC9Mp3rzLjo5knsRI3DJo8XN8gYglzZEEfzIj6YPacFq94KoFjExTf1diMtMKT5jD-XRGvLZ8XJf_RQeSdKp9kduCPy4igwHv108F6gi0UTEp5P66FpigcyAyOveg7_eAg9y3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heTbHM7bYrThl52WOfN6WiVgxoSYhQelvD-Xg5dZ4TzdMBCP7opKxnpZ8tWhmv_sQYpnnt_zOgobDieJ5DelLtCCVlxsGQh-kr4lMpG8zaTKrIFjRP-IxOx-4U8drRMkD4Kmhe8kZhtUVYiVtJ-KI6HeFvD5pG9U1wNLaY88RsbLx80VT1qljUn3b_lIYBDBFXJblLUEj38hnCbFPcpyHegoQFUdP2WhNczOeyJTmGDZ_GwiKWSmKcdIATgecmd6WJDKfCGpcLHObHs8GFdeVMl6u6ZRlk-82V7V63eSoPwpSmKxKrl4WKOF_cXtVdv-VcbVhO3vm0ATgwr8bNmAoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEWSPdasZgGJGBEGWsLw11qQev05J3MJKHigKhOvdppPd7csnu8SRlusOI14wD5OMircO6wTENo9tZ6d3mbR5hzC_tJaQogzfTGsrVTJAAhx5RqVsIYgo9Hyqe2uvks8fr_gdn2foSrDFEt4-Gkn_8CPby27o__qAdO0JCAdpAO27_yjYBjJUM9hetuiv1Ei7ejenQezSARllhXeDnkmaGyLqVaOyaM5ZcfHtlNONKXTICeXRzJrEh6POQQ_MyEitD4yL6hNH7KdT9A0eMP6FOJfZuGM3Mvm8wekvCMkXHxnJNnKHNjtejKbr4TGnHHU-iyKUsj8PcysbsGz953m4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrNB4sq70xnn_3ssDB_OdEgydspY5VkC93sE5QtQ1fA-3id456RYtbgBNeDVcPZWPGG1VyKhRmbHApW4zmq30s43dizT_j6_bhKnBDTclfvFjaOcwjfQgcwUraOFrV94yMaOcvzjmcQeUYHEjR6OUoHsBZBkhDaPuWnJdmERMB_ssK43Y5ZZbj23XDgT1H1T4GA5EyKSkPGGIhOCTQPl950Y7nUUab4UdrjY7hK74gal_q4DZ-7jAaTe2WSBBYmYdXKOwnHAtXt7EWcwx_3FhsXLOerETsxyshKD41SIjqiYFEFY3ay3eao1JXxd5hBsfgAzibtYrKYukLuWJ-Xx0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v20xQDsfXbSj2Pcd7yQFyP0poPKVjF0shbDIohcYDjbzEKxsnM0yzhapg2eUomiIhL5WJd4T7LT1sozecLS6A5gEclz4zDzLQC9nz7_UB0rMd5rEkfDwwLnl9mMAiuGMQesxhHpD4GST7FZ2JmivilQUAnHzRWc9F3xdMdQYxiao6O8inmxcVQIcxshqcx8bnbsiB-hArfbvd9V75NXhSLS9jws4FoBChb3xuxxwYxhPnMCTZg6L-Xa1dPh8wAgfVt51_CTB5BUz0MLz7q_KQfHf_jt1SCqIP4gkFRKR62pBOEmWYFE9WQKIObGCMOmbbaBzmRyaOcfu4HL3tBk91w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRdMa6V2euP2TZunE6JYsWYKNWhy6wvPIxs73tcoB68VeBGdIC1SAQHlekvdtC82IMEud0tTpH_CYI83RCsQUjaTcO-isp_Xlsui9bh1OdVR_STxXuPcGwb6bypM_5XHbhi_9aUTqn4EIiLQiJdVyy5N3vtWsZ5Mrq-jDLQXIFKZgWSb64qiqwja930JRNMXTOrjDCZ_A8t80vlxpiRF__Xfz6uVO8Ug1QQ-Cc_frP3rgRXmJ6FcIiVl97mBC363itVyL2Cs78LHLr7S7ECy0uKNgWnHiKFtilf5hVjRmBm0EJfJAMFcMqQctNJ8PfwMc1AOp736fPXAg43yzvmFCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYOH-TK0n4RFrB9UcdqjgoLehwyjZqFryJvVs2Wt9FB84Oa5Uv932iuoapkIneoxBQTodV10SZODiusuQ9n1iGrFzKXZJQdJJOX7Zgg0OqEq2Um0mbd3dWtsTFjouY0R8INg8eY2NhkoX2NK3ya60HfrhpuLVLCor8PUM1p4uK0uUJZrsjIMHPGHaLRbdfeJmOOUjOWRVoFQ8B_1A1OBIVPwBVI3L43vx28CZKddRngZGzLk8uVESgdLjcj9z-dJ1ccPAbdRkXf7-z5VSBV-2T__AqQ8saSGupki9GJP8stvedgVkvX2AWbDk_zIYplLyRX0dsw_vNVCsGf3gV9AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXbA-ufz7qEiY0lxEqnoByhn-ZwECnZnlZqtpMrP4WCWOAhIQburBdpRCgEz5BnhDbe-gwHGMPPavRrUsvEgswdy1dflOG3TMJnlN9Lwt8GpxU-kt7N9ABLaNzgs68P5kXVethEoMQKpIVbU6rltq67_guYdUtl_aIKQllIr550W1Y-7KWDcB9lnsym6mxRR4mZeZhzz0vTfbr8MhMEUU6QTDJ4zLOXjXF0CgyJdYihMs37_TzcOjtNj7l0Aor8fW0lNOaYe7pUlNe5QY5rZ1xRiGbcdGRAMu1DSCk6ETV_vhagpD1zg3FgiNHKn_Lpem89ieeT2YKeV68jJpaLTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7MfQCsxTHVL-gy4RWkqH3Z04l3xZnvs8hbhGmfZ8F0uVM0azD0X7H88kGAI612w7zD0mABF9g7oaA61Lxi7yY-48-5Ajxtx7EPeCTysZwuW2G_sz9-PJe8DnQD35sPL0zNSFfKAbVd9aR45TAATEaYlcMiehuA0PkRaypZJK3qIhbi4Sze2sfkzT4kzTCzFwgYBcIC4NAyXboGHfEPlkz1GeD7mjkOJked4r3e3Stm2JIVyEd-EJc1LE39v5Yrl5XyhEvcfSVMInRs0h2WMpVWQgkBFbJlS4oUjV1keZ7-I-qdv6Fd70ZFFgMRXiIKAWpuruN-nM0b_hMVjvYiurw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUM_oNyi-ZzOcGGlDX8cTJFa-sWh1Qzmye3tk2XTLbJ9ARXjsIf7xSwykZeCqV5qQawbKQBt1SNdS0yJsN_eCBNH9GeLGvm2RfclOHhLHIZwUumzfHZSu65G1Oq-3-alj_HhjrafeHUYL4LRGuUfnIdyvJueojrrAzQe6lpubCuLDtWvzjj3jSImQxh_FVHhhcTZ2enDAmGyKfozAIYT7GPBvU1uFjvN-exBI8rEsVdxXPbfztZ7I6jDOHETPB6A39-BRgVMWh3eSdfDCIc1ftqj922aCp-iuzwWonDR9nGdOCpnaQLbWh6QsbJDkccD8MyltIDt22Csz5Hc4SOwug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZA0jFTmKZcb0a999tQo91NFRvLn4TPtkHq4SL4xf4MuMSTRuvL7Q30avcAViT2dL5K0ZtNOldD0l4zv8B_6h3di5Stoc2ABsVXu5JicqFu8oonpvs6Et1GLk_iaaB1N3ZlbP5T4Jqr2B0uG9AD7VD478Id-s5UzACk_fF-tv3iYWLQNaoqkQ4J32PaOE1uqTtzj77Qz_8OcnvGNByzFoJxC5pAK5xPZZrZJgZmzpXWZS-e2acemZTdTJvB0wHhxWVlL4p8OwxGF4a450_Ba_NFbffp5Dk1iHedoVkAw3ivWhZcrVbu7S-xmlSO8JzbkQv3YyoRi80VY50si1Fl3MHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZA0jFTmKZcb0a999tQo91NFRvLn4TPtkHq4SL4xf4MuMSTRuvL7Q30avcAViT2dL5K0ZtNOldD0l4zv8B_6h3di5Stoc2ABsVXu5JicqFu8oonpvs6Et1GLk_iaaB1N3ZlbP5T4Jqr2B0uG9AD7VD478Id-s5UzACk_fF-tv3iYWLQNaoqkQ4J32PaOE1uqTtzj77Qz_8OcnvGNByzFoJxC5pAK5xPZZrZJgZmzpXWZS-e2acemZTdTJvB0wHhxWVlL4p8OwxGF4a450_Ba_NFbffp5Dk1iHedoVkAw3ivWhZcrVbu7S-xmlSO8JzbkQv3YyoRi80VY50si1Fl3MHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWXMAbZWQVvkUz2GOtUAFSjhF7KS2BTkW1fN1W1-sCqjosKdESyyExtBbb4MJOwXAEJCff9jhCw8JU33Re5M2LCuKTB5Ie-BRn_SWuOWiXuiJKpTwoWzn3zkJ-jnKU_EoSPPRNzA1kNLqpPbcq6LA7ElbpPptyyUw9ALuwBjZCwICNP9DRd2kbpHJ5vAL1n50RKt6GKOGjKswqK4uhki2BzZERdEGw9KJzvHkEUFJXOpwQX0p76xrAduIe_21esU82WVJiyqejjqnW6arz-1ySLM0xmIVEd4ayRJaRB0NgOKwpWH9Mn4dFkPN50kAwpxggLiyxvNLdNBRW3rF9ZsXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXk4HPjLo975rnFk8t5KNpZjFeAwdclt6H1g5cQgfqVn-8_YxUwFi5ZKYMEVO1PZfsx56lzbZps6QryjEl-dlOV2WG1osmxu5VlfSDdfLNHxCu244bfxvgQjoSfTkUfYkeIm6RP2a-odZitpoTrgRkPS6kIIA2hnu65GrPF8ssa1Tw3oV6SvuJ6QNIjlPhBf3sDVHOymJsyI161-bH8lJVLP8C5I99H0rggguN2GUhOtszKj9pzXEWdziYlw6rteLqG7Pi0_TIiXEpuhHpxq08764dmv4HfszxOl2YMLepDGmauHETLQsZ60aeesSDTqeE1j1HqKoxsgQbRQ8hXLdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTExeY9HguXmNGWKQ9ppfdW14RqNZPtrIf9NkVx6ILY_EHviELJlHbqP48vKr7i3EHn32o_qWCP6KnU5JAVZVNbsfhG18UuFs-kSTGJklCPjEcMD7QAtDkoNsUW21kxJh8QEOFsyPxRLIi6EuRinjgKgr2c5TZmZzPw_MVFMNdZpxiLn_3dhBKdWh9d5GiJUhQ2ojra_rcQkSE3NyqbKc00z0ukd-HbE07qfkA0MxUnq13Q8xQdQBEWcVRhtGcOpd8dqWDsso3BV7rvo4_H6YBcJwfrvPhOhlpNRSISYWalYP0aQLsrga1PVrS12FTCeb2pLU9RFVL79qeK0qSUM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pR64J29YhdFtHX3dMgHgdKFLw4ejqGREdhxWDwzhplLlK_uUYprSOCnma-Rpjnt8bjFIK_IXyZBV4ZkRG28RjmPqimDFkOVXqLuGnq__79bki646ZsSoa9UTHQtf45DhcDdwbJltXEkRUyYqIzupysdMsZuDzqi0I5OatqoxZMBw_AXYbzGKJMrXhPWiN8uqLBG-mUKcbdqkurd2D1KeWZnVpGXKzG1MGXr6RT6D-olRmwbnPz1IwAiDzM6axVd4CnOURLDQJL93pJoneTrOojbDPRwhv3t2RWkYQHNNjCtZPoQlHhxQy7a9JTTrP7sxbSgBy3cABF9gFwuJ_vR8hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzfvrnfO7_dW2IqBrPAoI4nrd2x9ewNhTTWK8nGxnNmKh8R-TGYdogKzZigwTMNMCoJCkWoH9MF3JbTeidvROJ6NdxpZKBADvFqraZ_fZoxGuy9rA3ysZZsQEh1mw5KawmbvO39-l_EVf-FaY49Fz178Yzvx1bO0_qcxjA74ZP2E62-TAhenFiCdGQ7JJVKt2CBhcuvOjw0XFmLEZcdIcGBZtHZa-bNxMt2EldunrItioZausC4MKHYp5Kpzfi3ekHVdZfqC5Bjv9d9YwBFI_OOO5R6fexXphYJAelPFIeKiSqzYE0d_UC8O6zxW-TTt_a0EyHEG7d_v4tEqhUXBkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgnL64WqXr92rFDLTFSTgQDgrqxMjetOczYEoO8uG-Scbc1AJyvjazyB3fqRNhG8r1lQGiHR08Cp3F-MvU_QjwTaS6s3Qkg4F09neVK5HfbH65e2C5MoLipkCRTil2Hxvk-FZ67yINDmztdYj2WYQmK1UBZeaTZHsTq5sJn3d1CbgJQwGmR7NYGoS6I4r35JoeSdg1Mb7Yq6w749WOiwH21ba06yWGCgIMKNFZ43qxDAsLlgnvaMb2HkTDI0eNrpS2sh9ojpJVFhGb0Mmlkhp34gC8gl2zd3lYMbYKlKeW36e3HytQy7RejN1yYuFdaeKuMP9BXyIXBUFpMTyOx3LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRqnieSU2Z42zo-VYkTfNQJwqe9nbISQXRYsQItMFNkoW4ZqYVIs-QGYksFkP8biEMFPLaasakPdYe8LLqTEWqp2QxozTAwaZI63oI3vc-iuPIuju021n4J4XoAX7rk4syMCiFyLZGH0Hbg_hJ35rBVYCdFXmb6JxNxY3mxlNEMZ8Nk0ygR5qEQPDZuH9u7gv-QQvul5lRJi1Ey2XeI62Ail6rsvEt58QNBWfU79_5A8r7OUnWRCykfpvA_21f6FiBYvcYoQ4XvF3FjElt7IEUhQQbJMWGxTZN56cvehRiFfUbJ3IkXgL28F_LmD_2tGRsv2yAAyXGC_sa-hPSPxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtckTF56Hai1GDz-ycV216H63bnjJRX4oUvvi1qlwNmcGm2p3KcGhSym8R5c9x7LccODvkiPLGCjHcUSpL8u15-XzyPwsGHlcokimJCjy3IlvfZWwro4ptOpebP87iLC3q5LzefZrKv9X3rl9xYNvdbjfDa-TBjnYUHBF2t2w2D613y6yV6Rly108KQcYRLAyjWbNcYsZASJz-yEGums8UJsM0ylHRZq6nIrWKlE4RPOyQfzbbzIxuwc2mqNHDFf97mZhpCS6pB5OhWNNvktoKma-MM1Q4qXxigGRAmJEVkze8zhTymwb6xOd5-Lgt5qeAtzTZqgPNDNQOc9fayXCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHXZC2-8ywz9AkcWiIfRmpZ_DhEaPjYAL30sAnOGm8n7IIq0MieGv5eB2SjMsWYwhCGmCEP39gqF1wlDmCgTXcZu7U6e5rZv0bppFk2mji8-O9Xhb8uN6pI3gO6y4IjGYEZ_Da8Iw6VOffkR1ALoSwG1VMOoIEwaZRsls-Ve9gUiCGOFrvJqAwJHwjHe4tym0kOf72C2OoztmB9f6FfLQtQt15RQGHPIuOnwG_dGgeXM5ydRN1gMuSACL1lh4ThhjCMpI-RppOejNb4ySj9Z2RsSrqEqGOWJdHsudaqx5WLQls-UREh5wmFQRx9MHBE3mGQvewMaPI4EdqVfi2yYwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJPIe6hxNLxvsjoWYNVlAkOkQCRueEp7AcBu-FpIxCZY_eypgqJ3L7CVeD8xkFvE3vD-pUcoOrYPIXf1whic5x1IA9MipkDqVKYsiZwEonDEwgHJrauEX5KwVfDRk4M9zlHJXk9oSWk6umQ7KuYNiw66zdJerVmpyiirnOsyXe8gTrhMGFydG1Lqi8WCodbnZT6ZKhcf5kINuhm_wTEOHmbrwJiQ4maxA-kicbUJl2A0H2BZ4dgagAnxoIdH1M_3JxFupuTXZSmBBNe8AWrJXOAzgLgZmQAm4cRRlkV-ogvPh8fc_U01mBzhV7DXb7QQnMMar7OGmUunYgivJ22PFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdhPryUcuh0MRA__DGC6gf628aSGMD_T8evPVrECVTz2i7ruVtHPH484i4_ASeZ-i7l5i2TSWDc3UhQ2Hb8SHUEi43uVhL8SpXWy-T0awADQKBifK68OhIngeF3IHBC2JV2khKjhUDQ2rCjXDiU2ccfsUHetwLvNb6trDrMrZDfUIaEUWNeLhbP6Ul8OgfC-DlEmRKDbTVMGXgInBFJ2UQ0Is2L0TsulsHz8rJSsTWqdbKX-azTPBrsYQ3XejL0Igx16VDPAYNHcwyVERTELmzcg6djj0jYNiFHl5y58H0HGsaDi_t31vua7ht-jxBMgCR0V7nnTZYmfWSDp2xOeCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2-0p_Xndy6oKLmwxSkyONZxJMw2FuF8zCRABTfOz6gbDB6E_1o1k_6Fr78xNrn8ZKjXSeryIomOiBmndcXQz-HKRWW2IzDTgDDH26zNnOuudhX17FZXRbnZmaezt_NeqEdcvIg9ZjDvlxf0KNDwgnNgJEyz_uXv2VX4-UsmDDFJglThEak_4F0rW_cPjxJx-UMCCOCpzebPJgedslxzXkva6Y5dk--zwDBheh3SZPT1FDFQ02E9l5xYYl0_IFQ3MUTJ2_KRUmyINSTAOaDMa2mSAlPEiwM6M_DF6yykMdKgLU5obCViJRNgnX_bfPdJQ2nlA3_LheGRe9Os6E1Ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUjvOQMgZYEictbMjzYRrowAl0drFOjsgk9b38KKq38eHJ7uyTbsUZzV8FWsn2lnKtpsXhRN-_0lue5_CwPITK1Kxew2zsLafQre40aow27UQge4UG7m7HMaGl-REMNKvzMPEKvFM39_-_BFeu_lKADR8i5eFP9bVx8dOoqmnSi-8MwxQN-kjfRxlDMM0EYCMQQA9w0IXHYS_b0iu63XzOUsvhfeLi1QHXMlYt2nmYF3uYt581kUzLU4L9CRQkumYuQAvWOEd5mEZgLoz8TRp-1uGUzvGQXz8QXHyB6ZS-siytbr3mn1toRNf3YnHwGZ0U0wZFRYCc0P7RDjzgDVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu7GqR16tgeBjRfF6xrAEmQyQSjygP1NSm7VuyAaO4jS-z5EOw8C5VhjZUNXTq2PzpUygomrqGpnZGGB1Fl3RlmOg4Op7704S3NfyBJvvqcJumuJQBB4NOvpTjtpM8x-7YQ61OUQzv0Q95uAWs-yi524JDXdQ0Yk0po4TETpTUZuL0boTdqo6v--cnB41u1MpKtVOUYLy6WvYvdwGOc0YG4rIMeZ6MbUBMMdOczpYykJtVMrdI0ifusgagYPakm10Z7DTgWgGKGVCwre96lY_1R4wZu8r9G9MA8q66atN18ErlfH6qQazVCLl38dm00qubrLNRrHkvCLUYOJaebXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WF_X6xL2l9AEeV976Yeg0ZbWs4Yv5CCuREVZXwFjmeWvFZgtiEVXIxdU0TOtuxS6RpNPxKaZ644Z5XMk5eYtLBDdgbtbVPtlEH6sOXvCZsBEvRlHvySQLRRs0ze5srLXsvdIYztdi0cJ1k8pds17AeuWtA-d7EG-cLvaAnVagAXwpDDoRB3slNgV8fnt5Uq_I5YPT7q7CuAF1ZHVGmYShpJxeExe9V-oOZWdaW0691CYNwikfIklixX7nwd-OJRqSbJUzb-PLvRF8JChdwMQUq6bwhnx1hZuWxj0mWhyoDUPaaJDic-7ESb2kQQGFc4l81Evu56J_5JAHarRT5gy5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTFEH0eAGvRSiM5RIfi1oDMiNGm2ZPGtGWytpJzOQnN1iaWBT5gyDKLdeYzsrbQM48u18bhKScFIp8lzsviX8rc1TPTir9rbGqFAx4vajdhEsfNbGnJBCQOnJZi0SpjTsix64SJKHX2_tDUDE5cqcYJKT0SeIpkpLiwfjqKv7gwPSCXbPSjcwQ4-Sh-OK5H70_bYCeZmmfXfiu44x3lCAZUpAlxzusZ68GY4euW9g1IKfc0REWadzYv-jy4n5DhFOHr_-iZaxlpPgCxbfKu7VQDwPVcUwckeqtf22qf-BbqMkn-YLefmpklA1s5xd2IHCITn9plNGDR3o7BgsNTbNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J96gR3oGJptHsuXodEDLO9B4SyuW65Ky4flYZNWZS6K1sghRCI11_r4bq7zOG5siL84BoYniKmLdSXtnCBAPdIKtwP6_KuipXZmF3LPfDwADL5gwujS_SwaHBKg3-jeTpf4ePGg1BEKEe2gz_XrRvC9_fGO786n22WUVTOw9aE1bE9fZJGzqfnuTpWfzfUG8yN28Glac-wiDTf8pztgl9_OFcRgaWWzZLFhJ3gNbFvasYcTkXj_zGPrtVD4yUYK7eUAyDUHVmFbHiylZ4yjnMlZPLWI_WGcKv8SjPdVs3uf0s6GtQUSoXn1IR5BpEAbfCvJ80fiFyZDVIKM9vYiyBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_NkK2PXeQTe-Og0sx9j3kkNTfRBwUA8l1bYHaVJ2BaJ-PP7uG-75oCtPIEZnBzhIXrts2U7UWHeHZH2XfhmhtS_t2eV2TwsV28-eigLc3E2h74OcnKIijl1RQvXyaCRDZvestrpKiNYcyPw7kSapcBniTug6Jjbqv3vvosd0vhkUQ7R1wsEuPGGbDUj8uSj7rqKtwuqPvdayrSD1UCOi75TH32kggYFq5fT3RGaLZ6h8wzH_xlBE82iCZ4cBwqnIYlGNntwNHj7pL9iI_KgA7PLi813_9iFdqkg5hh8YBGZVvdnTLzCxQtSgBtRw7AL1tJb9v5PrGMYY3fFNEx-Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-fUZGXU0WIRt5oIJ2OlA1UhB0UiGgjAFoMAnhlAs5DbiE5EIhoUDcvvqdAM-J0jzs2AbkZ8ITeYor4OAKtu1hLhh_2T5pvg_u18WG5YAaYaVunOoz90zxiN1NkbUwsklAeIEkDebB5r11bJWsWb0miTz1HHj1MH1H_SFGDxpc4HO2OVuoI9EFQkZaGh-H1F-BFeEQ8iuxwjrfDYVLtprn5LlejtnVObdI4GW0Ev75UbS9UtRvWU-VG9DHbYXaJvUi2Q5-9474v99BE2o0n_w05Bs28iz6aMY-I7ewwN61_0imaOWAk7rEUWSBZP5o7giaC8A1BxOQvbAAWydUOfjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb9y_ocLg92ISBfMsHQc8X7jdirpu4TrmW1VGP4kqFsxbaJGi1vJ1-bMrKkYJGi6vkgp9zr8cFunnYuvN073JW4f9fooj5jG7bnTF73vLJYj2s79OQzGjm5IxLTa8foyqjEBCFsAhJPF6Qy_t5jy7ASIC6VEtbwzRm4KHxEmQbHqzHN7sAYFwvnB_GRGVglgssLHFrWN6BZ6EXKM3KCnEAcHRA6OoeaLarmQJ0yLFYDqwfnbTHrAl_q8HSx8VDvWWit74Xfwd-yCCGzg8ov3wKc5NdpDzOkQOlEPQ3kp7q4xZlSJLCEpbiCY7JWmYQ1IDvRbZMCJ9xs2xf8bbA1EwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZSInjP23kKFIuv_EvHlzqj3KoVxZqfFaPfj8C1n1GU6BFwMubD45SkEVqNoF0_xgGOxn_Ys3BFs-THkhvbIetaXN7pyIELl3M3G8xM_ROKnTucE8Mm8bx5eMdKQbOkqtDTogTVb4bKBuRc1bQQlY9E-mp9yV0-dDuHfnykEx4rCGej2WZNR_J6brif6t0switB_CrT359e1T_rn3bIBBfQ6NlHofQVwbs-ZGouYVVWROEcKFivxHXfm3MLxVnobcyFNo1qDSZZQ7WUo_3KXPTRkY59TalOV0v_w42qR7aeTQc1-FCYt3okaYoh_SDqs77yabtXCoYKy51L5Wk_vBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHSFExCN98wtocukBSskCFjfM86yIPV5tbYDkiqtsIIb5BxZO-sikSsHhBB8aaoVdXywKzknEToX4oVE96AU7KuTEyzGRfUBxBg9nQiakaSmwfke2vjctkGgq9wYByx-b1JbYM_XtCrP1ut68knskVwoToAFR9kWqUWwTmbGeqxZPbocEsqd88wfcBkrlIYnl5OIXFG9hVZV_YMyKbfNcPzYdPrkwcEGdHBDSrXh3TY8uDV9nOF__fQtq-AroVRCUR4bVCKw0Gb745I6OZic6btwtGzFoNyS7HRcG2N2KLKCpUx_lgRjnOrCKXsHYYkeHtRUPC4Q1b6whNlC_DG_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZifS4JLU2U5G3BCmSQzch-cr09aMipxNBN_rhOkCFROXH2ANjlk17giZNnX9rY0OC2x9imjS41_YxMlwkyHryIgaX2-lSPnzakkszivUetr0u8KnfG4CsUuiZVH0ru2RhO88sYrWeyVO7CDiQ8xIHGzQPN0WjBlNsnfoMdeMQsRTzssTABYWqs-gWgenAmk9oI6Al9aNVFyVuD7zuwoDId4OG_0iaEK3ru7cNQqWns0J5BEmxTnMaEKnJ1up0g3CVckK_F1wyGppMnyOEcE-0EoX9CjSLrninGsfELG3IL3X9-II4qrrhvRGIYmmholc_CuFO_oAGxjBIubgL576Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd8ENFVt_78uhWzdINKnzJm41CQClLEUMNq6zXmJ6MNzzL-EZmN4cUhx7XBLYWxdQ1XA1vHFkunyBeBQWCXpyN_rgYt2GTle6CXOBuRB492F6_kSGGI5woR6zm4IxhsXG4S7xAP58G0xtgcfq0XheL49u1cxSNH3CWx_iNdm1XATKue9xRjo8nRIFQulQTyzn1T2QhFTBvkhnnkCqC27d24PmFGT-a5WWw8tUgDUP_LH5u8jUajOMpQ-K5srDTC92ikaK2rQ_hnl5Dj0oQWFAJaMbc8pynRlTq1wga-eZQslAo3duDvCZAbErOLL469qffOhbOQpBa34vVtiljFqEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyBcWiwoSJZtyJYUxM7jXUV0aD8AnLTKbY7zPwxiEr7wgOIcv6GJiw43ULtqNX7g77RDEZ9-Od3jv7tKKcpTSKNkHqcu6oo3KcsDswpOlmm7YtJbNtohW2zhg7skZpfra1HHzt7x35EzKs8I_L_PQRUGdMWOAmRxnaeTV1S15Iii-tnIZmjhA6qqey_d6znxgcLf_cKmY1FEMsRZYZ2VQ7Kx4JqNwU27ajMo7pZ_N_G2Xc97qiWMQh8L3Y98Jp7CRLIz-4RLy6TlZBq4jmgZsyEM3m6iZDvgvvGcNg6VEhOpiLOLF9jocB5z0nDLvEh9EbvMDxkin5FafCHoBM4Ngw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLKTHtvWuwiaPJRcDTpu5T1eKCijuo5lEls6639csKxyL8Z8Ea843DDA3ttsunIieHNkcho027H4bcctM-yuYqu_nAH9H6YGP8_1hWXPvIl9SwCPFQYmBn_lOTrSxEDTiK6eTMvZv7M4PRSzCVgZqXNWBjk3jsfIv8aTRBsnZMlO381GjumXubtvt6L4IG9Nfjdq0VBJS8zb01hLVUbgv-gjS1L1b8LDgWnMnu-vK3QuJnxYCkhMhxvcCedlQhBfkIfTTPGXmaGlU2vJEB1x2QS8IJe6E60phaDSmrJrMkdZFZICZu8-uVl72XlGIqUcbzNvBFgNzV1OrEW4YDtLKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWKsdqedRSZ8_PgmYp5pErpBvhl2vEwIAWsQxqsQzlaYQ4NRKLb9oyNdjVUXBV0GLD4HqZ3mNQ8u7Co3UuBE3fdFTTDu021ezaVFxIYADrYX1WtqEi8dco7aIqTdoEW9jPS25lkzQwOjwNrA27RNx7KSuVP8qVJlStR6-2DiQWyv3f4iZhMAc-G1ZujiEvhuKH2Wq7Wu4pirj5zM4bL7InROQS10Fd9DPE4ewDXj9Mf4Y4jNClfZM19_l9cC1S41d1eGTRfHujorSw5_k6ysKKeKEPhz-JddbM6ELVZ1GsHxOFbPNxgdGy2byvCAyXNMWavNIQmcXC57Hcg0ivweeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdLn2nK1YHLcbxK-IOVZoJARsaAhZCPD5I8_frMH_9myas1b2-J0SmuEUbL4sG0hGzuvQxGYKsS6yn5O-a2TMwuZ_ya3gjd70MFJOvSpdPawDC2kHrwQtLBd4yVqrBporUIdAomsX5UfyiEyz0-NYuUraBx_wGoSyu8ZLiEHFX6-zA7ACaHEi_yBsnn0skvD0DOIJnuojDpwZKZZ_wKvV5naNN1QkUx3Tqg1YRKODbY_NEP05WcApe-9-qnpE00_Y4hs4oYgXi7VzmUViHia1o3jU0gP0XM2FxeBwzaOCUyCNhtt9yulAvqqXVFCIwZ_mZBvn5JLVCDvOZ9s27b8SA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzJ6LTz0lhIJAHm82kic2-DioB-2UeHOGNsa_zhNY8ozyZn152pv7xBMrZELQK1oBRBsLIsZsWjJjszH4mqm2iq1eXPVto8GKmOrjnujNFdLh6wjxHQGw0cFFFLhHofCX8bl6ucU_W0l9ZAuL7Z2DrWE1VhzsyrrUn7E4OvF87DvX-lerbKt3RA8CSfcR28fwUdWKwcQrUEB7mbxJk-3TWJ-xX0zpohYoxAFbPMB843brkpTdCOfuyYWlkitSxSaxlAAFTj8Q8xafq-stKaX3gP42eDRnX7qFapx73TkWxIgIyW0iDiMdmOM-Q07cU_TQrDOvzMdQEI3PqZMqJ31uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jr8id00axbJs6fO1iO-fQedsbWzarIImB8d58pvkzzwfzGU2teFbAjoueDvixbDqHtmehtwubjrs04BpRXigAADyVXU2KGi268ogov-Xlf85N_O279kMUi_h9266FZtI6vXFRxjR1fniIiuNcP7Ms2xpLTFzxgRvojSNrNxyDg5RkB03Pc9enJSeaOFVLjS6-W0APOGYvqZelCdtLMlGy1iGcHR1JoOeBScIrlQigdWySOT0HxpnmMlINwTDuFvHC1CLhf86lYyCBEBw_KQn-qfHiPlwiyn89ltVSYEmVDBOkvEIO-gIj92RIv2GIS3WedsU58NKcDq4J01biOhYDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1e9n9QuH79Sx7fY54mWCnyOZWXO8IyiYDyIRaPawml4v2p4SzmQN8loOtMEI3so-15_PrWV_pO3P_VG-WyxSIeZKf2slesemIhsatEcsT4D5LACpXa3SLA7nKiAsBrRVb4zqu0nb8VYbLvabUpgnF3MbPa_Ml9wHSKqcMrXQf5ThL5rjWpJyRTZLfXl4Bp9U03FMW7nbSUVfjbPynoND2nyJETnvxfwkaoznrkkNP2yod7uEuMfNCh4UQ5Wvef_gwXlS2-woyss2KY0wMSwjVvIuJyhhEy5ph1VklAno83Rzna-rOK5WpxscGq9zbfMsVzIQ3-vUDtJTotX6k5nhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-hmZLCsw2SfIpS5-yFeuoiARQu1Njf657KmXtvBb9bUm-yyuKUqp5jD9pNU2oviBqwxPvLs9KHqDDKdflL4mQHGNJZ_YSEQn-oQTti8h8sroST6CNGG9eq2T-NKOYax4p8DFtSVKEpsyeWgKPTdZwVgYET6tFIDg2IGeiTZd28dE7-Xl1k0R9px75Jj-AouaKPbbswlqnpTlbUFHF72693guzPELucMDWLcKmu6mdbo0LOQYWNzv0zng8uW0cXxC6q__QMdmPFkWnWP3cBigakrv7ElcZFYalEurMV9eL6Lp-ZYdjJTQZ5GX-Za-wyvMaBXnxmxmScKWt3kZC1MnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSM9tRSv5jxDrw_Uk2Uuv59_yAyzICtURZbMUpueROM2uEidymMquEAqonUbhdSnm1X9E6XnTQzLT7EeGpzqunHkutz2WAqQA8RoVOp-sTQ5GxVkimAEccMOQzYeNhBsmjijR5ZgvxVGxQr04K92P9FJI84mTvM0m6V1UNMTFYGOW6V3J7TYSr4RHU_o9BDH94tFEPT-Ed0yJGT-Y3Phom0zAo3U9DgP59xCHpvo4octQ11Zc3tYVWrfnkP3HCAdPYVeA3DBCq1LmPu0-E1KG1cSOhSNxG1b1TiVn-1R4czF-iKsE7ubSMs6-Ustik3Qf-4Eo9mNqCviG9mF7CcwFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgAMfdOsOI9kOKkXeim4wr506clQxxp6iUkOLd3-mDuq13x2LVrJgc7BPuQ8j9LD6DjVKQKVXXXlcQ84QO2yyu0lQUAlZBAyz9YnIOMVAaCD9aMVlChyGI4Wd8EKYFPk_PNivLuM_aiv99zDLTy0aAtM5QiffZZ8dDGyCZAIjcHC3KGKUl4munQ9vXGVJwC7TVJ2vnXlI5dmFVy7nGmU1lIPVRu9kKWRn_tMrS_pgrnsjtwtVFtVZv1mCgBJGojAG6iHOW4WH6KjYpobuGznxDjkbmZ2DNcUgobsQ06zBu_RvVq8IJjMvGD1QMk8TMpsdk9VsD7LqFYoDJ02I7VEdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-tpEy-CDWiihFN21RNNp_Zy9Wh3zpaY_7vN9nfaFL5Ff8GQ7pZRB2-bo77UWqUKgb2mG46LyQZSjZ8AQTV9pPpSUikeMZeW1UDdFD5dbFMEkuDJeh8VOLQD64Kge0AcatqgwPaYWxWffg7b0a_EQ1VTsZGgbphpQtkeO8SrQcEL6GFQ4oJuO8uRRIpfAltw83VhQEgoIYUfEiCZpcgEIn6sJCJDA8uSeo9jlIgOsNiz30Bp6S8w3WAwwd6tlxQXY2FDI8iQjF8xBdStgnFQfX_IpjGLr92ruzGWg3IxBLhegGdkOsTMrU4E8junpaMXkB0AmjV-IMBi3Z8gBQ6fKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfUMDsqAcukn269JfwQg4OeMdSRUqs8h7XrOSWmrSGAeJjKnMjoQES5PM8G3KiIj2JJszTNkoySS7MUw4HsRg6KYj9a1oRmhBPCUZMIQE_b3zfO6AD2_DqwstMEAUMp-NyDILbISBGkdMI39mUUgEaRNtJlWd_BjnVBXqxs8vHl1AJYhDT4QIvoVG2SDD5_q3WTZIlb4mVNuMUFhy_bZF72k8cvTizTq6sb0kHxKbzIGCC6UXI165bj_4K5GLfau9UHmIyiv41jUXntklvsGm2IfMHRD5vNNZkXPRyFu_hcRzVHH9nJFwFThyglP0N53gy6WvxNHfALH7ZE9KR1-OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7lY4knqiOXs_SXz3TkLAI8IieDgpWCFTkE83Y1Xy6vmwzJhj3ZUF-hNQqYg0tzeMb-cjSQ3i4vUvMmvQQ0PAe9SGL9HcHKJt6Zd_TTLP728gA2IodUw3i2AJtHoXUZqLG8kstcZ-SETui424dBGyo_rq07P6opmMVdgMseQI9CSsdGQeaXYM8EFyQUfasLiwxuAwRLN-UzEHwydRmA2WMNZ7wDP3LguEtqQh3REicJzafR8Bzb0C-dev0Nv9NdkSmiIa9jyTtnUkn0XdW4UnWe0vop2PWeGZUq7D94ywClHW-REyIxaSLA6TZLzpOOYzlGTe1ETN_UlYeAbBwZ4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8mWgNuIdvCBw9_F6H2_BO-_52K2KWj4iEAyQ8rVBgapJwUKQHgFTsQ5Rv7t7MeFkmv8AfiF6IV2Lc5_CbU8cT5dINTyPb42B7g0TX02eccPVpJsXkzJvKu4_6XL5MaC3LvbvB7jIDBmrBMs4rARdtTrMADv-24bQj283XhgIcKiYvSAnMW8wF4HJV9JLZk-wwIzOpfZCDcCDwHpzSiRjfpnnuhxj7l490nSH0dJplilWYy7PncKRsPo2C-pnsKNNBv2tGcTdR0aEl5X8TfGvjRAOC9siewuLmeLvtQSLbda7xvl4wtryu7d39xsCjsBG9bf2gsghI5nWvNHZTyxZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMi1ay2sK1iOZoRtnscGe3IkoytcM0i0zG6STN-ufojQZFSSVpLXcgcBOmd6aUxlbPDdUrIZfJ5iHM8qDiX4lbsybYMz4SBJsNPVhpUGFFAMl5GABTbpgMmZ9r_3fzUJMj245E_G8IfykyeIRxVua3XdQ6p1ihEI8u-bl_Dj1U-kBB52gQyyyGgHY_0NQ5UMZ8EdWEuEdgyxjtHyFo8VUkTF01goCbWQGnVM4GzjJPX15POEGpfkgOCh_11RRwQu3eawBIx1v5TH7g7t6m8SGMCc4Frv7T8lIpHl9_T2N4i_qZbS3TMr3oj5kKNn8C8dTuZFuCAk9XIHwSDZyNq1Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH_T6hUpONCtyi0NZJAr_LWBElrH11IC599wwXv4m0bVJYw35y5qvTK1NKiUuFODvgllvaBfJGsAE6l9pfJjx_OdvIOTzS4MHlx5dt8HDsL23ySLMIqEoYctns29X4z9_Ls-82KsyWDB5IABKep328glCA5ZZ3md1uGsgy1xs5_cqCwZkuGyIGJIYmjqOmqk4lGbdaolVz5rMIG60uGlPlFVLxyO8V5na3spC1XwDU8CxZGZ7JS8cK74CJyQVKO9knUit_fO7V1MZF_DR7spAjxLCq4sPPL28wBMyHBZ2N3jRlYdVHueI_uirDO3LCvsoQtEOXpud35EDcSJjefVtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpeRmK3dyc6_L7HSoHbtcBIxkC1AV9vdoZttPODESKvZV2wCOKbq6k4qn4qA4Ilv6dYJOUyl5hafXwDcQAf7dF8W5_5vYrBnuSOQNxwzU8LKmvaRTfMwPEpTj7cz0Fi0nGkN3oUTW-8bU9BrLL9-BVp049owdAFvnNMHZpUilxXBqxv6WunRQtTZa9ILCdSb73gnKBZpihQ2d3rS0Cw0lBs1rcktygXyFE0m15A7IfjKJbd9pltzl7gV55NIIeJ9v7CuuBkua8kWUChyoj6-WUhn2Fnsk4CJYMx5jCSEZfZpjj_QIKhbTJGAoB5N2wTGOqHCcQN0_Rcc_7nlLNaXHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNUc-QHe7xzsQoMcsqwqEoyFKtkJnFVbV1QcMEv-PYx9PUu4MLBMjGEEDIhpngHeBbThJjmMXtrdi2OpruuTDgR1B6k7JEFAgbNiFRXWcJ-AwEdD8OFSZaHiVcQLMN2qoUlPcO91jErcE2y-F3rjXP1tCyTXcOxEgMc80VKq-tCR_6fuCRW9tN-E9wtGPNCR1UWxNfqC53p8R60EH3-_C9RSdjXm-SeMp0NCJ2e--6E_9tBxQEzFSMqnHZbWcv_oaRKZb8OGis8dFEtbqnC5hM8Dy4b1A2y8AJOmFSJDqAzIm1fWeF5Ebx4HXtEviOCOuCzfr4ToJQ9iUjbR3UPsEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=o_h7T4SpFXi8Db5ATHy8391kuyptTl1pPgnQSN4M2NUiqMWa2c306HxKzAVdFJU94Sj3Sy8K77Va0h2fRGNV3GBw1GCv-wmv1IKAXlkFILs0s7isB5xxBe2OZx-EZHgaH4fnAn-Rh5n0bVIyOiBc5INq8NhHdBNojogasb_8Y_i-NyGQlAKAreoawmNfygEX0azmzdP9f5JuiE5sZbbApWwI9eiM7wdNEMPseY-H2fK6BCKr2cisfL8dxFHX1YpibpySBjFIGtqcqT_3lfF2OVwLaQQvxvk3wmuyA0TwGtwZmO_M8H74rekeW0W_sBMBHNLXY4ccps2CKGRI9fzgMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=o_h7T4SpFXi8Db5ATHy8391kuyptTl1pPgnQSN4M2NUiqMWa2c306HxKzAVdFJU94Sj3Sy8K77Va0h2fRGNV3GBw1GCv-wmv1IKAXlkFILs0s7isB5xxBe2OZx-EZHgaH4fnAn-Rh5n0bVIyOiBc5INq8NhHdBNojogasb_8Y_i-NyGQlAKAreoawmNfygEX0azmzdP9f5JuiE5sZbbApWwI9eiM7wdNEMPseY-H2fK6BCKr2cisfL8dxFHX1YpibpySBjFIGtqcqT_3lfF2OVwLaQQvxvk3wmuyA0TwGtwZmO_M8H74rekeW0W_sBMBHNLXY4ccps2CKGRI9fzgMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lttfhy1XAOzzgQ4M0cP9KfAmxnLcUoJOSNQ9yqBmA_gfCFBn1InpF9BBDXUX2mUDgPikQLHPa3w3cA306fqGUlafbLjGtmTX-GBlFel_ps90vu328g2mBZ5gJMmUfGmanEZRk5j-lbu-JiwE0nzoR8HDNxAqZdr2kIOMVZb9-4EiTLMGs8DAe6robUSoIlqi8AOm1qu4QaXuQAljuI9H__50doOVIVq0GqpiO30NcpXqXEoyGGAJto1WnwDK89HSjP90aAmTKe4_cK1YipSZSjMPSnOz4XpBhPDe5skTFL7pCA5cFyaqYPCuyYMjmwZ1MrDxhk0L76AJelabg_wfMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP3rWaoO7PYDZqzuK9_c5fR53dQT1bpqnfae8yfYiAPg3e5miw0Vq0WT8kV8e-Y29UEvXmb3wqvQUydIfo7c2XrtCt_PdTr-uBxQoWF9W5YcwaRb3WBGzSXipGsfRGLwM52sjnY5dD1Y8iyEnYAkz_PpfwIg0yz0Op2hoH04ShvP4Dui8IDUwntcyKne-QWexLqhRF54Fp-SxqUrUtlhRFqwlWn3ZK09OPYUrYou-wJd3JYl8lMfdq9V6eqD1BN-U7rk4_CFUV5n4_2OFLdJM3T3iwhSWOTSd9OhnDlslC5LoQCseeQIJ2V_rTEHGAFXG0mKJcufZeUgbMKK_kkfPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1jv72AAPmiVeucS3892xZ19mEhgErP0WRUdHmskZ2ntP6QFC9s8n5ElaeHzZDORD-6ThsnmNVIsh4fh4HcDy3JgQO1lZK4TicMa1vGCAm092GCfALRHCUSfDjRhFBC9A5eVf-Nnwb-6RtyMOrVX7Bk-G7OrUwo0mQjMUHSrOSmvEF2FihaRD3fjXBzTK1tGldZrS-if-ZcpQHizGgNd1FrIyR9grXCzlZp2drrPcMe4xhXcf9FmeDsTIATkp1gfOILdJPH0YXu0v6j_yMLDtX0h41y6dFd0y6qaXNBTEgF1VLegYUQkXC79zlpd6WDyQMlg625t3LjaXO5onuHexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkyN2IF_U11xKuyUU2OkE0mcc8GezTXNV1Lx_amjPBYj9PPYZhLIaRzWudNjGtb_F2Fcrg3NfT-5EIEQVzTEs0FSZJuTtHF8rz6goPLgexscG-CcJZsMAb6UMleWiMvDMv7RTDYeMIty4HInZaXC-yuTGmJTurbnZ8iD8grzx8oeHOJuHuOPdViTNR4oHR9cw7M0vEiU8aTHPdX0ANwcnMB-ge9VqFzUY1IA9cv2ZLZjc-_op7e1BWKkW8Q7SmuasYAC1YTPcjUoq6aeCr4mM_GHWKI_doaQdQ5X0QR_dk_DMiW-5qq_Cn47jHk46fl15g1ZVvue9KqtvIIwE5X64w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhqEhBrNRsIBXNrJkN-N4UwzzRw-ue321kYkdi8v-0yT9w8p70vE6mnyUChLlyaOgdjkXexFxckQpVaJIdRoo2tXvvtZtaeFjiUCBdJe-zZP-kwAkjVJ9wNLD2RV8oDVaTAiGuNOk-tjIoHL-1PwS42OpfJK4nlfwuTu2as6KGYPxEKfnlzlzbs2oWkyYpZsR0Tq4DUgUtp0-DOBqWdEE0pPXHtOeyaC9lF8N__xQ0V60Bp_gZ-cc-A68AKsvE1gvbYwMLMXoGTNXb8qDwyQPz6YOEBL5mlqT6wEIkTQlKhdHpR57wbp4CUIDghD-00gyNQjldyuY2t3kvwtAKB5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crFzT97iamvXTWWQLadILI9qOaC2HoulfGtp7ZFjnjtorGgtXm5sJSNNi7rKqAjzQRTjacY6Hulcxq4c5Btx1nJRbvKYVLkNOn7VPDtkeKl_fYkZHEYRcaPLuig5qWDWWzmKASB7lujftMqNaS8Y6TAs1AYqaL3HPf6cAvvhiyw83S2q9sIMEBK-VLe3YKl6hkqVlHZq6aXJYIw2nbEk_38RIVTQvWJJYor_sAxHcLX_8byP1gK1XG4glGjnI6BUpw6dlzeW2hcv-mHDbQvihPH5Xu-G7O3fmA5FAlDix9Y2HXYDdRI7I7bvzqoCLn0safHL1wJQDUh9htg6GgwtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm76BnXG0JeG8bjBRgBImWP0XUfTbu5xbKOh75vCj2ij2mNRXmqFME475yBlb65WkKlzKchsKm4zFKoR1WDRo1IFtJ8bxqbfD8lIosMndInPPDyiJFe2vywAw6PRM16gBUsP4kJquG62WCagDE7NJd5o4TNi97xTR2C7BAUv5YwrgZBpmgvSvprnV8TwgtVKB198q6ekId0bKUcQRCVFUyBpYQvTQsGy6hYm-hPh4BBTFaDe9p4BhjXlcHsWhnSKN-TKX6UkedTOlSweWguxM6N3dYTqI24-0TliaClbNBStuu4TYU-Px1cHgWVESXqYHlxwyhVWGn9VrRgCqRrLiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=XkeldlIzp9agckqwQjwZoKAfP-gC8Dr2fg0nJ32wdFzaU_IbOXSUQOFnqBWHBTpCVdeEKhV3mh-IxiAhTY3dYqtp0Z4PjRmJMlJWScAIDAeScDq2I8XW6P0jMTIqaXeCClTlerQ-o8b4MoRLDUzEp7-yC39TKVfVKWdFvlH-LxnEFXt9IYNalt3Y7IWS1JyCphFiVnLu8s0v32vh-J5T5h-i79FxB0rwPOTy0hkEU0Rc414wQxdZrdoR59iufubkXql2nfhgKSO4BPbuQDO3bpy6aXb2tssbuAwtpiNJ40nM7XnrQ2l2Ej9Ux-Rn4xd-jE52DMe4C_zIl3i7xO2ZFk2SHqi756WDQwbSrNINSl07uwEVHLGyGM_yD6eBzJEa2WhO5sk7HNZmXRQVjyDLImLK1MKPbCkdyiO86oZhZy5CktfkMcPKH4n9tSxz-8rg_EgpV4tQja_jLFoV39t-bHiQso3243Trsbpg4C8atSdcxsOodsO6e-XNaHBYvjWc1ZMWS77nLA00KG84dgRQ1X2uqFf82WaGwb3OX6secilkX_JAjbD4i_2hCk96jr2QrYIArsk2Ps9LxUsRiMfulo6CvUh-hdg7Kd9Dbx_Wg8ZmCQbfebRnu_TEtroXbn5mg0ICHopHcIGStXlUKAgSWv4HzHa-4wXsdnRc-WkmoFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=XkeldlIzp9agckqwQjwZoKAfP-gC8Dr2fg0nJ32wdFzaU_IbOXSUQOFnqBWHBTpCVdeEKhV3mh-IxiAhTY3dYqtp0Z4PjRmJMlJWScAIDAeScDq2I8XW6P0jMTIqaXeCClTlerQ-o8b4MoRLDUzEp7-yC39TKVfVKWdFvlH-LxnEFXt9IYNalt3Y7IWS1JyCphFiVnLu8s0v32vh-J5T5h-i79FxB0rwPOTy0hkEU0Rc414wQxdZrdoR59iufubkXql2nfhgKSO4BPbuQDO3bpy6aXb2tssbuAwtpiNJ40nM7XnrQ2l2Ej9Ux-Rn4xd-jE52DMe4C_zIl3i7xO2ZFk2SHqi756WDQwbSrNINSl07uwEVHLGyGM_yD6eBzJEa2WhO5sk7HNZmXRQVjyDLImLK1MKPbCkdyiO86oZhZy5CktfkMcPKH4n9tSxz-8rg_EgpV4tQja_jLFoV39t-bHiQso3243Trsbpg4C8atSdcxsOodsO6e-XNaHBYvjWc1ZMWS77nLA00KG84dgRQ1X2uqFf82WaGwb3OX6secilkX_JAjbD4i_2hCk96jr2QrYIArsk2Ps9LxUsRiMfulo6CvUh-hdg7Kd9Dbx_Wg8ZmCQbfebRnu_TEtroXbn5mg0ICHopHcIGStXlUKAgSWv4HzHa-4wXsdnRc-WkmoFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JErE9ZnH31ARMGNjn9JsjyvMdTWb3xGCzJ_uWFfOTak4mvGcCyeY0OrlaHPU6Lswkunew3ZUbCJ8-FEQuUbv1750Xu1bLa6PQEih21bpf_FrtikpaU9uX1bxn_BbOQ0wp5Emw1fcBHltztpZcN720YAgiEY0B3DClCKPp3BRvgF2F9TQ9dZPWo2vdQv2IJaAhme0MMYIMx2NhqieY4YGgwYMLUTqTVrTQ2GmHYbSBrnyUHIOsuWf3uZjAZNKq0qXgnrKStrgDpYx5Rkfqo7coTI4sgyGmdMxPLyMjrvLNqN0G87URA1bpGjMRFGt-biOkE4jVUwN2nyjDK0DEptxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTip-WfVYYFxq3NnkgbIjy8m3Dvu8tpYGSUUDqouohWt32D5P9QUVlGe1s0HoNwMaKm5HwxB9A81mSLXKS2gcF_eWw3BFP_piE2TL9Zb62Z_sApgCtpwPZRQ_DUfJX9jfukE7DixTz81nSO_uYV1aDfIASYiQu7bCnjHoEHUNBtK0oLjPZP2cB3OWCFcxbqc6HGFiZgihj6o9QtbTLajmm0SRrd2MF05o1GARN1uXHiduR65WNODFMtzvnKaRqn3Caa9rMyQ0CC5R5YLDjF2_hh1Xner68ySbIiksWnlU2FrsuKq2_sr7O9Z2HMi-2FAEgLvjfgSM_FVOAfC4ufctA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3LMWSbI98tkSgTqj_3i4e354Vo1rNt4Id4JadJAvKqnXHXOYAUStcyll1woVTbYKXD3AyBQNasT9RMqK-29oAKAz46JxIiqomlxwOS5pKK39iCUkPPqKng-51aUr6sD43rjZu_JElHaVS5En0c5zyzbfdy455cQGP8y8rSGIvaxf2esOtOtvuDwtGSnWes3RDZFMSqBLH9uKkIt8_j6AUQpyca8DUXCrx8SozO2SpuruF5glUXprvFnCbZv1i54Fn8A_KRGn5-y_FvwTNIWyuSEg1OYl3WUScBxGBbt0pEnBoby4GVmmd9iUqEEBsy7u3Q16_iDtu27MRFXKfpSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-d2r-EZRB4MjtbYZI3115Xh6JNlZygXAYmUXHqhOjVAr4wkIKfxtEquoEAWlwGx9ode2f8sRpKRbN_yFSMyFxBP6YbxjCwyKZQfmTdun5xjO-W6W0hiwSAABrDg2FGTAdPoa6vWeqLmJM6kB-7YXfiUu1a3vNsYtHYE6uaplnp_ZxfqKEBq8pl6LXrDB5Qw-h4xUJQQap1PuExisOywND4P-nWJAjOP4zHvTjIowY0VtowVantO-0NQixja4k44ly7J_Mrs1vPNtrSDIBgLwMSD4sIIXMDJZjRmwv4jOhM8SgVGe3hEDVZTX2KL6cM04NynLwR4c_0rw7xMhk48Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgjzA7IQwri6_bS_DHl5OC1fA_1r-BHzH99DwzBGt3unQslZjumnP4RtprhzFTg3-0tlqNdzbre4llHPK1-HZhwMSsPnNYpkYKjV6n_ZhB38I9h0v7eDF8x2f1YIGzXxdrPA4o0VU2wq5ikBAkT4MqIZNiyJKo2zUGq5Nulo2yC6J6HCnCOcrSFcMnZSyKPzfLJN2sH5P5ZTPFMqtxa1BP13s7ERXdVRezxgrHXtWm-DUVzJtMsFkJoVbAO1l1U9BCBqqjEKzBq2lc_Qw345Mb9WRmYjhf4M_YwBChBui22BMlkMLgWviFX3FloOlkwKnVPo4OnqXA-hbKuGP8XO2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDl0MLC6dQ_mtwyskAuUWj78bJJIEKDeZztiReLL6M_SXYu9CjSDO8EmUIsIROm1azBV_-ZMHz6b-jo_8QxfEdwj9e6FW68LiY5XYpO1c0mcwhqsp6G6SNKV_YvWb55GYID6yRD2EvcdwjvT6I-zMxH17FjkxfxRBmNNnKKxOWxvn2z6WfzhNlbGTzPhcttT0g-9uQzgcAoqRKq6NU72nE6vTdZswvGEri4028HAjaCwwCGCGOYA4enpdX7hRbS__vlYhJiJ4FoNUvD6TW-J1vT6e3KYGLMwI2yHgK5DnYoMvOa0DXEoyUgEFidSGOWD9O79IiXOaB996O1fXb8Qgg.jpg" alt="photo" loading="lazy"/></div>
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
