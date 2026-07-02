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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 226 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8hv7vOaQzEU7R_u_1UDSAvPQ6IlHlY_sIEGXL1aHT8rEDVl1zorxER_XxxUqlO0dFsn5KP7GvqFSovsrdEgapxN4yo8mWKou8VnrjyObEZW8nKsI_NLH1cwm5qtGzNfoypoBTL4cOkUMJBSMtDfsUwzfSELI5QBGkk1qWwUOc-8HdMHqjKFBWrUuoKhlhKqJXKlcw1cZ3QVqfHbnEfjq71Ey-GxgVcnjQT4ZtxnqSMAkZBtXZadVGLmuXJBH41unKREaSQE4MktkKAVp1_1M1QoIU0-mqeKj05I7QigRCqrBvK85cKTSRgL72OWDjNa1suyzbvzGFVJOnhMHGXjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 470 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Nx8cpHgdttHxjICt1w3S0hvTTvVwPWxUB849cFwAWTDKn1zD6qUZANe-5knSwTLjaiJnHhMTY-4p1fbo-qtxcWMkb-iCTL6XZbs9ztUQAKIfDIraiE5cXomQNQ4mVUnyifms4xKB1a2z0de0It760sssb2A7JXnc59zuaMmnGP7YqlIXqyw9NJduO04hpcccQzRwSjAO4ZS5gecVk3eTeC3OiALuH5ywAQ1k2i59R9kW0hbW3juNXevn5mpNqyy0qnn_yBBPHUDoJqRjPTTrrkEihyXq84I92KXjMFzWYR4WwdSwMCFXC6Id6ZSnZ2sf6VuRQ1JG_H96-DqOsogg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzFJg_3SvEu47kzlvIb_yniBjpPIxuEG2qZYR-xWbIjVVpReksz0Vd5jnyoZe-zJibJvelbFsW8_s_TI7QgWpot9tCMQlflbrzCFwyYJdwJRPvXFNx9e3DcfSjsVd13Yf5FwYqfX1bczfUqjfDQk4Y7jWgWb0TTp2fDgNP798DpJnDT0Op6yvPELGSuNxALOgH0uMEs4xxN0L80mC2dyypKIjL0dHnfLMAnFAf7MyosxQruHuZu8AWgJKjBKBPYVebNRZCi6cVY8DmlkK8oiksyGYxj4wIpD2RX7jzy4uC4mdjYiO48fiJJ7eAa76VgCT81Z-KE9uIr1Fod1qvQ5Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnQjL5nR4CpfJ3BLuy6IUzXQmcPcNbf-0lEvmmWcVRTLFhxUkguLFrWA-dLRawJvHD4LdYiCi06Rk1sPz7OkaR9EYeXVnhyqwL-OvvB0oUMIflaYW22KHLK70E2nOtRT5Vt4XRZdx0mqgbnOJhKTPqN22ttkNHhUB3dVhOAF92s0jdh39Kkhc2HjSUODrMvQ5gHKRZBLF50cg7nzA_ereRyE8fghuUDhDv-0snyG46TimbbUK7PbZ6k0szHSBCmjojvgqM7QNoginfUakrP0uGj9x5CKX6VPFJLjqO2Fr7FAysiJTHt7vZ7KJwNjQEkQUgOhWCfrQX1EPCNGNbV2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acDbn4miFfPoS3A77zAaDLyH4YGptZzl1f7_S1gK7UyqpsN2bKk7yJ5mGuwOZ2EDAsqWwYr0uM6Y7VS_kbuwcMzMY6yDH4Dz8broWsqLkM8qQ-cMUpUW-sOSx20o4bmG_3y0WtJusVWnhCY_3wao3es56pH3JhQtfRXuAWUu7mJPoXICj2i7msou01l1T0n8wleUg7jPVRPxbxFBxIi9am00FCwrczDrGkKgfYOO6crTmq3Id1Jbtd4vErM350Yy9ubxZ7jGSXTZLn-fW7DUqyqwAH26QDy2oHDAK0BJmV5UwINSppNwT85CewO63IwL--UpHU8MUEaFDp8DCc11qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwrPCBpYQtnHBqGlkhwKiR9jEQ735_dJLeyFJC1gy1XZZfrPUzhawXs0TvSfpYaz40149n8XEXAY8v__o2NXKvow-4vWBfuHrYRqhX_6O5mZCL3v9mzLInEQBofSX446juc7hF3Fp0VJ7FucoaU3_abWIoRPiuLHNflVZg-XtpeVJlonHmjHqXATxvNe3yI8w4u1uQoH4JFoKSl3xay-ioGRUCe_QGu8QBU1O5Cf4G8E7IvcOZCf9owBYKg4-1Q1Jr5rJ9AWtMwKBPl1VBX1BGIp-WvWKQBuHg7GCQ_5O_lDCr-1ZdIEKOHZhsS33_LbQcZO3kSGIAyxrIt2qr07dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-y3D777LDba6aIm_C4IUY8Qlfb1N006qaGjKBXvO3v7Xq28IFph15sA9mjULQEJPeZrh4OSHcYgzUjqzOEFFjV6KNHEBdj3eJNx9AlZrWMdlAvsKKzJpAPAF5lVKqG31MQZmHzAkg8Zlx5N_u0A8zcF4Q9gatDD1r6_mMUQ5u-CozhvdBDfKrKaVp4L5IOarelLE39ZwKHbHItOgyHjhOHndX9Q-5P0UP9ZrHUA984nK9jEkIgt11pQKGzlM53bR9stzxMuWnP45NQRmeZ2LNfxRBjL9oHhALnYxSUll1BqAx1Q3kQHGgIhp9MBYg4MAkhksfpBOsM9t0lHGRgE_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiXOvsZjeUHvomuf9FSdpK80DxbqPBszwPQab3t7c8niRnuABbzUsfj6CeXnflSSTFNrPDdyYF-rXOBBJkYyarnoHL5fg1wcZ4g8JmQRNSn7hXbpk8XfyZDLJz_RDne7VdKDHM6GreBiGwLPzr4ZAR7i0nXm7IYXY4aV9sKgwZILbGx9TdRZit342HwcaoepM65qoPuRfsWZ9TUpb0K4MxE9qpKV3lt7hU7Ccdm_OGejQtLukPy3Z8wdtKpZQOT-Ydll79mfZbGcgkLdc7e_BRevF8CdyEbGBX-6gJFFackc2R44Qi1sAgpxsSejvduIxU9J5eP1hn78rbnvZfxAMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMErB-it5xkJiPWMCG92D2WVzkbZeGyC9h7lr90-ttcOSarPcMBeQZ26nrdsC7m4V-NqRYW5VH3oTYHEAsqDupcKW56CWW9WNBe07xe7LRTOVmMbdRMirwLJ51Y3Ks6IeEvOj5qW5BIk30KlQ_v7zu_9L8ZCnk_wSZslLGkOiq_ekXD54nwJjM7FX14G3RR7LVzZ7RFXyFXOxtExDiARkGExT799ukKn0XbA1q7CI-lf0pZv99Nl755hJPLWlw3bNw0fyqQVKhlvvr31OXEaSZrcSr8-zcM7g5xw6KGdxokQdWw1eRascnJBfoW8_X8s3EO_8ux_d1FGNcCte9W62w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQv7KE4PeEQtLo78gghENiP5_1t1R5-MHzSom0JHiUjZPfGC_wl0eYX_kib0g42y6KKnqUdOSL8LWWZuoeZih-yKSCq0HRHdAJSl16oI2DsJST8RP0bushB1L5Dxvkw2ZFoaxTg9fPsAHkD13bqh0eqIDfiS2jXJQ201vUCDvlzHZrx8Ta_fIImj_hQRUElBodMZeSYBjsjSwWBaDKVt-NHzmkvtnmw2rZP4Te_QgwNsDb-dLdLjB4Ho3Bf7t9486aInIXubDpUGwVvJzhnh88TGLBOfINNmU3ED__Fjh-QEr59NXWFuxsLYsuWGC_gIB-OH0ZAyUSN_tNhqPZGRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azMBievVcawRGt6takrEsLN5NcMsrGQMlnZ-7mwZUggn_AJVADZoynLFHs2cLIIJ_QuiDJo3BrqDuEOHKVtKisn_4EH3ugLxhXLCVVwp0CzeIkj-5ltA9RuD01_46ZIWaFd-4cn_8If6tcpKcc1WXDuWFXfwIZrJkzIgG7jLzcT87txiBaJb87nRI6-CAwDx_zHfntLc1IL03E-0MM9DX5unYlBit2YY0neYVoLVdRXNgwJbQUtQ_JbecjXLzEcaM41lEeB8JG7kn9t5gp397UkBsI9L2-amVfmYZQJ_8wvnq11EGY80w4X0Cgh7HiFJ73zIoOt2hnUuC_KFS_HCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftYfKHDrt2nMcuDGJjsS8_-KmQlXRu_qvEJShFRyo5WvEFhXt0k2_Q0vevu6DJtzwpUj9ub-siHEkgQRPHw9aeEpfXWWZbRsoozBTiuAKnpOjTDKfnH22RxWhrVVVwn-WxFlV1TiuYgxA36qyfYLuhEj_BOez56Mw9Mrg1ua25ojJ3JHTlTzGSW4QaCn1iO_eRJV8H5dzpoPB8OrPXe2H01vZmMtlRS4Io9_YcwKaLhjrOajz69jFnAOhrSjMgTv1miwTz_r5Dzt0pn5y1nJ_U_8He3GzuynMSiiAu4euVz22Y0MBlfr10UvcZEcxWQdE9wAfPRiX4rXWRXoKiwI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOOd4WslpPmcS4iCw4mTTMmJVrqqmds-wu5sglY5lh5dvs-01E4AhAfjcf9haTQVhBeW9AB8TKV5Cm2Z15mWfJhhH2osEy5OdO0cxXwAS8rRsl9FqXulPMBkMJM1V7QxO8fWKXlQQOfKJC-zD6vIMSG_cVaLsXi5_lG1Tv248tdUwVy315kSaIol1u7R6YksPOp5NvNjG_rIZbRG2TClo2sFvM11q-URStG6R7dgJh4XEnmGaTiP2dzAsINot6WQGKXNZ3_OUzLGKTc2GCMN81xchg85J8Z7EpZWvvdE1bYyCswyqpO-l-9OaJ8wEAUbCAn_eyYB7O6JNijx4B5SDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb2vgzRMjBbGXqV-Fpk7b07yf9td-ZY5EFYmP9IplSv7py_6I27ZQmxGnv_ecma9kaf0_JLl-EAeRCgUYb6lt7rThmkQq0k4uKlPjqSxgipPwqnIsX3cu1zoA5n6CWyOg_EJ_MqRJal-sQOxp1YKf11ih1q_5v4gZoqSfRpsIttDEEWBsBQTmcpzk3F3CXIxEP-ch--PVa53E0-uDkN9c6NRsjY6429VowDca30gKp2iFzsfebseVagwXmzrSugBz5YJYOc9n8G8_qR1FA3Rlrb6Fn5xiPrJMed-42nxEGYyIdN05DKQs70_B-TOTdKX5ogdJ7yw8pP35jkaLRV-Yg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=BnVP05gh8Zev2AYa7w1YsQRrM4Ww3C18dtnJo9b6XQdVN4x6FDzl65VYQqjIXrmBl1WM7MypFW7iMX74xvdfvGYEDMiehGABM3Uoy0nSBTOz663OXvIIh50SPcnLUIQbsefdVqIxRwfbTHFYgVZMgBmR42OrNM2Y-l28aG51F8_K6p0wu2Ptocy0GPGnbgLMRUsu6kg66AOyPn2RMJMgdV-ka6WBpRbl7iuc5jly_z6-dSXaBBOduxDKqI9TENZWdupXgDRBJixZ0fD5KYgn0gd7zlmWftH7sP3vZgRktP8DR7sZOG8NFqYejsGJoTw6NUl6AhAnzzKeV7r40wZwEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=BnVP05gh8Zev2AYa7w1YsQRrM4Ww3C18dtnJo9b6XQdVN4x6FDzl65VYQqjIXrmBl1WM7MypFW7iMX74xvdfvGYEDMiehGABM3Uoy0nSBTOz663OXvIIh50SPcnLUIQbsefdVqIxRwfbTHFYgVZMgBmR42OrNM2Y-l28aG51F8_K6p0wu2Ptocy0GPGnbgLMRUsu6kg66AOyPn2RMJMgdV-ka6WBpRbl7iuc5jly_z6-dSXaBBOduxDKqI9TENZWdupXgDRBJixZ0fD5KYgn0gd7zlmWftH7sP3vZgRktP8DR7sZOG8NFqYejsGJoTw6NUl6AhAnzzKeV7r40wZwEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXR6Ur1ZwCQ1nBiW9mekRqRQhLswksGIiYYdHU22OtE9fOXVTvSJ_aDYAP0nCehgiGkTVMMK2LtWs02_m6jfyl1ee9UsuDszpqGoF1WKakdHgEhZyV6Bek6fEwYg7AslREcRcoFI60GeJOKQXNQo5Gpgh8SRkop8Z8HyCLVSS1QOND7oFQ0GHkPdZpuV2_dC8xHrXYwO_99ey44ssqssnn-HxfOc7CYkyVJ_QpOsOJo93FbOqnkeTBuVasiNMiitIbqEydSdW7Vz5_xHeAsHxbuLPngrb7i6mG-L2899sSocpN6DqNjC-TdNGQv9MzqJtq2_mnKtoC8cZoRPF_q12g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1QR_HjwAZe32JihileFQ_t692GhUUxMRFSRu0gS4wJdrGjN6A4GCJxxbxg1poILTgfQntO063IsTwhghh5SRFf5V_Qt__x91q2qPJShUHxkaTlMBTBSgVVXX2e8Gg2QdLx0PQq6W1qhJkIKhcp8HhCXSH2HemQ5yiv2BZEDZ6OovpZKF9S6DnG5iEMsdtkfyqVHsp6975TcmtjwPiPHsVNtkE2_xWlXJumikxOpcjvf6oWtMWPPlDCyuiV-ik-z71yxMVWKjTm7yHe0hasNzOfofivEH6n5PIfw8AaCr_Uny1HVQjOP_YDG571DhVK4kyW0anEVp-CnQiYRd7kolA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec3eQbrUDWlxxRuk5K3i6_E2ko5OzTiM0CReHzMfyRGFz6E1QPbbbKmeUesqXeXEo-TKAORg-GYAlBDC1M_cbymTaUbYzi8JRZXQ3EkfgrA8CCZ-Ui_GX8Si1hbEh8PiBhRpDMnILuoAJZ9bZhR2NENJbp2A1dmMKmcc6K4mZiLE38nL1WzB4oOfIT7YBICJJOEZolbQbW-6YTi2Z320gqI3S2YCeYn8Oiw55m6nF-GjKHazwiSrPpeTKuJp9qmx84Mi7ocnJPeJw9o3cBZKa991SLxel1mfU44Wr1D4c_ZaKyrQdMk8UQnuFKf2VQwyuMO0xovnVmgUM0AhPTVhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_J3cn-SBzmde2O4mPRYrRsQXxc1bHHzlYVgta-oqh9Q3lkZ-cUp2J4CAMCecDgoqTZSkUKPitGpeD-pOPRfgWlVVNFEpWEq3UdB9AZNORswCPTbk5NZISt2m8icNMYu6_X_oOOG5WQUenPHkqWJwA0BzMf2Yyq_Qyu7ZcyIMq2QxWeJFSKe-0WEPsro_l7GkbtrTbimmsg7NoZeORNAG1oSC9x8JZiTyjq9u6gN11Ina2r7zxpHKO6na54UHSreKaLz0nfH8E9r-ZdntvKDQBKQbRVcdxeyuiEaoCyX_rXSu4YJhgjJK1pOvo0sH5_OWF57lbH1oJuWJ7-jri_skw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAM-frzBj5522ibFt4aPfhfJoU3KeJsRMAPhj_9W9Bd30HT9aDLchJVNFc8xSI2UpfXpjHd3qolCus9K-I1mvgmxD0EhbkB_tbnxEm95sd4p76Ed-oZF-hKVMzGi3dGj698ioq8-ddwV3pQ5IzauDLDTOPYYlnBs8vpl1rIKfKjmlEnSGrAQ3gUkVvZzjvtIRHWEqK-SglqTOmdl9pp3NaX6Bafrdq057fjkImWqDq1H61oSDpbHYfV9YRnrUQhkKhxCGpyrqRcLFhyvF2p_2BAigsWnG7lL8Fwx3eIoHCxXJHvmtTSBpvG7RqMxXw6LVcUkjyzI4KZPMME18UST4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDFVQ2PCuQFDWmAvhhkSNRXehLKkVL76VmCj1EIBoJW9uPw_pibm21j9EforKLj2w0rDZjo4jZnOuMks1pUbPskaHqPha81_esGINxYju3Lhs5t8XnPh-5MQy_vrYAPgkKEoJEDVTOo7uWYZbVkB0T17uo0TDqoEtypfuz7NxLirWduol-oGVcDTV0PpmxeHYXVPmu40nfYvcz3hN2GOjczGwF4FsmbN85lBzgkdWd6_2iakgQnDJZjMKAdvKxCF0dgptbGwH93zBN6ppQnQ_6bENik1lqd7EmX6AAQ9ixPtJD3-CfGfslrTb71hJcIpJl5ay2SQVDAq4ypn3rWvnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aaq3m2_CBsIouuCHJErQ7ufPQpiXDjvupZhwpsw1g1utCqE4YJmWhhJrfXsUIZMOiDZ-LWke_AshZwrfgXjYD23d6BIzNIVz9okQgmY0KXeZ0NWFDbM6jn8nnhSX-S9yvtFv1S2cjEt5k6CV7bsI2AlC1ejENN9Pq2Ai5pKA2JhpyYO4YW9cantHJ-qbUIclFTp3MHqXeBjm9tOmSkiSJt4kqSvYqiohw3gbOLjyMSkwOeh2lSfK1EckP7SjQ9j6lPAWpSM2dbb9pNLQmhyFZkC-ccCcZNwQi7HvAiZghTgcfL3HmLMFkd1NMhWOz9AXb8jCtrkr6Tafsit5Zuf3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOsFTjTFu01zWz8d_uJgQlCmfwFwqgulWtO-hmelaqdFgQ16mGfGfClAPEGIphTQvL25_PZYwtSQEM4KwfvPKQZ6J7SPPqPXjBZz8g4pmFCm3QGYLfIuMdp1DsuLN4WaIKS-V2HmDF94BG_m_pcNZfdbvMoYCRntgWZ1DBJTwT30snnxYKv9HWjAUG7PSveUCfH0NbbuutkWH-9HU-lmZsktemrX1IlsmIi7o6Ivo-r1kyV6bGXJJxUAuMPSOSG44qmuuTD0cXItKi_uyEgGih2KLpF1X1AOlxmuhXE44BRD-EVJcYqkKGrIW1NDj-Pf464WX7u7ImWhIoQOXIHL6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbCPYkq_q7epPsbLQH8rF6UaPmLXt9RTB9pVvF8wynDUkJLa9-dMfbrTKyKm4ypcTPEciKZTyJf9nGuQM_el5JW5GVMsIdJFREGvVlPbD55pkjuTzuoDa5qxcsL8jfZBCqbvJiAY2FVyymNw-nU1trog6bXOzjh6SNp_YjAQIIjNZuO4v-hZW0_LWfxSldtiWWYtyOzaOEc_paUyhG1kkrLuwZNo-qSgrAf5OowR7BR3OEZVWLVtCQvhvX5RF3XrWHD_4C9fa8YucpOtp11arw3t-k1IGyY5gd-M0w_010CPR8VYjIfPvpbvtNN_a_3WHA_aZnfvRkt9u9pvXidF0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-EEXTuLkAE0hlKRSqWIU_ll1ni8GfHpn0pBjEbjOuHHQI3m67E3yqgqrJUjoDVKYLNXyh-ASvgvZQ0RYc-RNwArBCgzoIg6DQj_vdPb2gxLHppWzHkv2kovX7QOTghYVRbNigVoMnYami1GWNx9m3UeaRuYycwO3u__xLg0M9B4dK1Sa5R0zUnv1rAAzK2So5AenBGwp3FqbbsTxCBHwhBN-iP7tuVq64eW1LAhcD5NeUmRHwXMmKASqtwyMWWAapvK-45jlKmLNwNpzWrpDY3k3ZsNK30-_ZhL5zQbGib_M8XbzUwAAjSLAGvB13N_jDrlugor9BerW4smoc0X5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEApcGX1GDIka5QORIx-DOXl5_IMlXvErPbkwHg-KVHGSOnxYqitGKGH7tEfeBWPH8FD7MrDpzx3YKOQ5Bl06U5qw7Pd4dBnaDzZapVWgDQcIxYmG1rt-SQAR1ZdqGiZQo6kdmMdg5NLPPBXPu3cjRtx3wjKABzE-Bnvy7_zJo1svhSX2LPdE0LIErpK-taR2i-RlsRSjGtA_kAK3It8hmawhcjEl6sC_JXDX-r9vARQdPQD6XsRIblecordpYAsM85hGg06kLvFrvDFB8pEr3MmYctQ30N-dtQFl19qGheNsVfgyAomG6cSWdrgwePI8SingmnTbziSv_zu3nStpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q24jWRXSex44UcRmxnd9fMgc2_KtbXPTM2FhZHzCze1P-S4mtQYFJM2MFhtg1CcgQGlnmVpggZDHsC0LshyEP3gxCwOFsv5o575aqELOmGuR8aEj2lAvwVARoFMiYwwRKtknhJuetqDdsZUB3eFrbydTROT62AqaTWuvGiRF0NC1vNpLwqAVap0NRleUju1YJn-hxuuIjC6eIzcDS_jZR45y-IFdwAQ-DSm1XhRj3j2tt19Gpv6LYZ7WdiuIU4MLu_FRPqbCqK8UkGAXeq2MMQguOfdekUMAAN5tFfoiJPN3AwL2shGxMmIPcKt5BexNr8s5Q0MWDFUeNQP3ZVWLJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPSXTw2YiVgPWAt7h7SssS8FwQv-9Ti5AKmavdL5ezxgvbjJno7jwhobBezk-KvrBdP0pAMTOXp1VWjFR01L56hDv1nGXsQf3gAKOZi6xrWayYr3BjZ2F4ZzluLkA_LhZdxKwAIES_aZLDvx0HLoIBCaNC2Ey5YgxnlyM_fuTQt3J_lLCJEXHvhHAVU7k0tzzbWYk33LCh_SLTNj6nZx6vzSsUYZcOlpaasfZrenIN4QABYNX9JqstG3Bm2KbUMPqZXKJUC2MkUYev8L9Uga6E7c0iEsoBMYGCjbQGFfp96p6lDwn-BLcv5ovnnVRcsonCcGbpKLATi9J7NwMRKF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvH0TpubVfV0c8IRDM0NwFl-PoFAaI5IwrmibAEv1v2cuw7OThNMfF-HmDGESPNQ279q_wCqzNG9B6igU8ud5256-2Gs5du10jd6lCJy9K1VY5ZQk8YJUo63mBcX1Fu72irL6YkIdfT8UZ8rJeaTB9jRNB0wUWxzFGNaJ9hfB2Rn7dT4-MTbYX2TVGmUcVAej4n9SVgPLM6uWcIi5WutqWE89EZgckyY49W_tvaX_k7UJTEzhiDRT5GBQI38TQCgsFyGLw7Eek1XMzEo_Gb6-QGZ17qzejMsbdqYTSNTzIOQ4cKAaH_MNwQTMtG-i1YdUMMLkfIj-PAZhU-fwAQfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwZx8HqzVbi944Gj5FGnmOB9FrVfyw543jsaaFMk8PMEeDDC8iDFUBy52xOpsfo2tdAHahtn8Oxfu5bB5mI5m9IAfyy3BjBrEKOymyRyb3SmmzMoTJoDwenStSv8pzmCiVDbkO23nJATJqG6pj6l6bB_x-WKVIwTI-A75nvl4mU7tINt_PTCv3hyuapw557_QAWKKCCY0EClKIa3DKHUmG4P5ATy1LdAVBFtOBZtbw9XQLv6ftKjIjVyHwrr0ZkQ7EM9uGxcmeZkKmDPAb_yjkcHiiODX4_BR36YSfFGtOYcBykijhYT80W_QTva6p7cvMDDcg1hIY81MDj2wC25DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGK1VRkMQZBx0nVwjH20F7Z8yEh747LIqs120hwFFHjSCC69Cwotfqt4o1n7RorzMooHTnjgFkFJC-U1xhP4ZT09-4QzyvhSf6h6U-HSwPlvsbnF-8G6-LUuZC2Arc_QKAajFExVFnTzreRHv_zUaeD8VdnX39dicv2FXrS_Ld6lUxq05bWhrccdEtn6Jqz65n5ctLq8SweOTbt13mKx5iKvqZloKsBMYxHZk1ZIC8Yr0bu8IBpgJeH1GVlH35sblJ4sTJLTXz9V5ceSyOXwa2ZPo06bVYudAGGutOLq8R1-agkJwHGSgDrOV737SgHnI2hRAWkFTT87yQA5cUF2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahIHkFPDdKSl2gpWyQEqitsbySb0LlL1KoF9iEnqB8rO_sogeiWlu5MMlM5ouv4BL3ocNtnAdAYV5nnB3d9dbYQ-OMTcL9XVaEb97-AyA2Wvl-XHomwVuQxkRG3B8ziEiVA4fZKnb1LGpQNmJxQeF8okDxxXPbRGhwZgaYdDgISJzmIu_WOuvQ9HnM3qapMsezjs7KYknTuevy-KNaKN9Ej6RRtIc-pDIcXuqtdnM0fIt66chq-GzQXVohlqvdkWL5TlG79yCp6zspAtUM886QzjXLhLArfAqDxDYIUA44b48QEsKTE8tjb007al8KWoer49TmYWadruegx8YnGe8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-XTBjdadV0gGUY_C8o3YYAtC4elDdGtIJnml05jrjI7_9pRnzJOxxwoEQiMdV05sfTZTSTDXV-7uACMNk0j3ExA53RP_so2-qTjS3kiaEF8NzAB3ri_XAjaheGXlJV8ob08yhpGywpssPsKFObJsewhYzRtcmaWmk8sqbEaEuMGPqqv4FUxf8ts84ORThWyPotwYeZ9LaYv4dxp6bhY2QNwJhKLfRpYbKELmJtey5JU-kjjDsgDeEBWBxoydCVriWTXz6ab2UrmAwhvrDjvIaUazJ6b8bLpeuP2KJcAcBaF8sJzd4Tl25Mm2Uc3Pwgx_BJxinzayotmEH78L7AAsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyZSDekADtsMsywW_EnOLp2xY9c1JPN2MYn_F3c7NmDPCe4UT1UmqB3CLQmbJIaAtBmeIwkPmRMdqB_we6S5jO7JrOKHM-UDqPJ0HhJvBCrsILN0OXJfzhjqn8UkJLyt2fBCc0-j4ne5X8E4ESqeKjtA8A7gA9ujHotUEoHogObTBcc7UwVi7Z-wHWirYEQIeM3adrazZaIZTq5oBZUSelPeZ0nB5kXFcOWMc3Na5aQ3EB7Zg9JFMqmHPXEGoCgUIeYnQNqxIJGxkpa5cc_MrR8gkWp4g8rPAMzUR4b3WDDm3bsq8-9W0qp5kTQOeKThR1jWoZ8Q_-lN8mYeSok9Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5RVQTzvAYxP3P2dJfzXrJ0Fn5fsglZogkTCKBQRwEt9sNxuvlMlW1M4SPSqIEhZ6gU4gvpY0Cxxz88nufCl8Lsvf2Kk28wXm3SnacFbtTtN7_3D7400QkcGI5ILH-6c4kZbJdJjwEqy45t6nbIT56hayWN0ldDLXr4mfV7tuHVC0gqH7th23tMcL2kAWRcdx-h27xQf1q2D3CTPGBqT8Yh9BIgSn2xy8vYKtWjkNS7uRiTmrGmtZ4UatZFI81OavqBuXghpOAB3kupwi1F_CH-hQ8MQEv5Gr40cnBhcccPJ0bWEztKs-jNyyObjH2ppED6U-xeL4F4gs1qP_8sWKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ2LmuU4ho-bP0yICGH4BqurvKr6_dQKWJpfmfrvobKOI1wLaQ_G93Gafbtz_yRgWT7r_TV7dfPIvT4DjAHt5HwVfV8_goV1G4TxQGQFYd3um4hQ5pK__WM54rwGBayiA8UfWERBYMDVJkFAqkf1nr3taD0GV18a93PqtE99lfYj15zfxGJoh4fcJV6LqONbeBJHNEEM6mJK3MS_etdgMaWUJFLjZ6Fq30dOQMdJSvzaVpb5ntQnHiMp2BDRumRYE3LZFpK2RlFF1fRAKgAiNeyFYlhEBvzXRkEQY8RMXu7qiEL-VaCVCt8-RlyyKR5sI8ZCy1Vtesg-UAK26Nn64Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiQ0tkPREYdLbptiSBSxdxO6OKmXRTtBeyRgqNtpAhVmbY97b-i6ihhDcBSEZBaE4uriH2caNaC4rBXndlGBpXrKqOZB2FOXqFSM568QFzQFY0oa8S3MvmmVoHIiWnKZvPOgdGCL6expp5QOrY1aSiVCjWuJhe1vRDbsEiFeo7MTnirzGfM6WkpHPV8TYCSF9vma4EnmrDDgkyI9SxpUtf-Xu1Z9aW_Jnw_nWHP_oissloZ1INJhBVaRBrHcz7m5oOXQBblNWcmBmK0vHInSbEBtR3fauIEN3r4FzAasoYb5l0BbF6KBM5FCEqoj3nbOHVcTryR3QFbYgo4rFtSbxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCTf7gVTBOn3HuDNDAUh_lIbF7XJ4iS8cuYlTdBMlVo27NeqhLv84OawUTP-VAN2CC4bcWuOzA2tvM09dkCdURAI-u8D6halUmwFNYY-WBMN4hvm2K8LfU0aMZUUy14cSYVddiWSfHJhiPPPktaHk27gRkdPDa8j4eRnCZHrmkHW14C5ZHm1jLc7fKoxI-RDctgGn2xr93kgVwPpDzYzoUUFw60ci2W9QQrqMwpzuYTJro2B67aHVr0yX-Vy0JKgNruVxjIPYYfgVGJiqITaIWdNXFUrP0O3-JjakFDfCPpmGX96aG3TOGiiNATI83KdJyl74GSKc9BjYZcPl_qEHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRvHclBV3FRkkZuyGLkVxbQlAPIdQ5QZZnBdflNBL4hjDalvPzWYMUIrgV8NRGjNm0_-qkuZx1W4GZTpTLCXbPsCSmnvQvfyMB--r598qvFXG5Da-6sccIlVZqiDcjZOwbOiu3NfLTHM6cDIAPpNJ-og0KRtP-JFH-WKo_3uQABIpihQz1DsQ4SJ6YF6109T0Zh-QmQZPjVgQmVxupcobQnfvlbQQYGNiY3MYvq20yHhp4FRAHBdsszCnN1aN8aJaJkDCRSJn0r3StOP7BgmpfySn-_jTBZHeeaG69GfNf3iOVzncOZarvZ59Ah_jJLiD_S-LaCKeJk7N1vKrpbxzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCCVaqLIpp7AE0-OlkKVQO3u82INehOovDth-bLhjouJHlSnOOlC2RggQTJziyVq6sJ7xPMQ6E4aYqcjxO5H8vgMhSKC-Uk8E3dGtPjUNPOeeoeQtecDx9wPM1MBqoUyql9uJSRsAvG8ooyKWjI2Tt3f5g-sMCijwbyBA1IlkqZvYYdbp2OJrZdHa3_hU4EJFZXo5nbXnurdzQlGa5M-iNSnBLGE507OEZPr2IbfrXsYw0VjzWOaNwluX8nbIG0QIM8cg-d6l0zKLLMYBOUbE6OYs8bz6oadJ_BmcXSOJrekbG-_yhZ2s9nhM3nCVWKprvcHFvuHNO0_wt7OW_eILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7HwAfvr5Hv0lgQf_RqtR3sne5seuXkfs7GY38N-Z3uQqs9wEsW5Y0_7Ynij80n3p53YpR1kSChAQG4lDX0om7L7FLHqHfTZaqkCcjwO4jzQ3PsTZ7YPJrH-n_GW2RSoxSAJ2vXEe0ssmHl8WfAPtshIv15n0dZfGvVK8_sZOlDrz6PWXkDo-CIw9z9k5oD28oTCbEE7p9OmO4CeLGKO-bDd303qfLf8sBFBE-h8vA4CkUwvY_5QN14Kq5p4bW4BocAyf0ogg8gXpJBjVH9T8jN9yxiBp4lfZi2HiBrtEKSi5Oyg7Eh4kwDFxptXg1YNJrX-KLAFCmadx_Zr4FBhZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGd5ZWqgcbZ07wCxBgtVbdnV21lev34BZX4JiVIx2TAhsa5-PJC0UBqMleLWJcZ-QbJgCQpTvN2SyHs4ItRe3iCwtRUa9Bkh9-eivnPegy8UsVkXNitEZaLfH78pVrmA70mF0wHtC-NpetdMM18YCiQ2aBAGkjg9V2k-CKRM--aqaI9qty-UOuyLrDvkf6t09xhOXaZ0-iuNHt5lWDqPgcfsKth79SC2mAs-d1BDxc0yrj2ojdq3nLsawAMOCYaHSsWMAxQBmcBYTFwVW57PN3HViOmc89nU6AtpYOp5WmWzkDKEmrZ2JBdhn6sScaA4O5f547ZmjrHHcOKpmvoNvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv-8SjPi5MKMi16dx8GU0Tv5yhV6gi63u_NKNJyq8a1O6aSO22xikBzx6lFLW67zuUyt3XiCyxlVI-rWEl5kg5zsQ4y_1Qu6SO7K1hGAjJS9BNoNKGZRH18m_IcKBWtHFfWXpPIhkQqfpK5cvHdBnFBQGhYNE4OGWwb4Xw7TqhrxEcj1dUJf6feWzpnXDj57Nd_043-1L2IKLNUWZFejAluWEkTVtSwdQ0KVuG8CbVrjRK6FeWSXcIZmn07JH4Z_HBKi759DqMwKT-CHqbIxbkxL_AbFkV-czyuCt1zej1UbXQCS6poxlwnoeoTfZfMTwey0hIsU9jij9OVLevrk0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr7GGHIVdSgavoFYq-SEhVtYSdRxD-8rJP4KD5MAxi2xJXvPzlzvQBYfNot619P7HDOrZnvAfEfgNqo0bgXknUvqFKjALfUibQmQ1AAuluYtMEtYXc7NEAoA9bDLyOpoUriBGroi_aGuFji3KY2GyLEN3-zo9UiCITjY1wuue082mNJqaEsj9V6ziGMTfU2BPIXcTF1WFTncru5G_2lXyPCrNAb3WGYWXn5X_KEyJGmzYX4ONBfvgkJlTeoTbF-FwXU191-OFyY3vU-er4n-P71M_rAS4h3NGyIUk8zou2R4bg8M1E9aMeqv6iJQ0BsJKf4Sf9eLei8IOlRdV_ptFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKgLym0IH5PpnQs4Uh-nfjItOz6n1iqiUwpia_mbhi5_cWooFCvIJ44ydK3A8wbxxhtUwKH-hk86NPPONyzMrJ3Gb2vAgfgZAAZxBI9ZW2SmHHv1ukTVknY9BhJQEC4qk5StjVU3xP7Al4gDt276YW5nub5-XIJwk_BvgYkDcp_H7w-n_OLEvbaHim5XBsUd-9pwm6hGLcQn0vbMTEe99tgvrXPSMpl313f8-PEln6bI1Blq8DdhxrAXZUPkhszm-2lncowXVuDkJdaerI3Hj-niYo-e4vMDjjaxmQ9zlc73SXzlMEa6q_niQiVneFDv3Hejq9EHCiXDhGrTSVSZHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdIYA_ywXpku0aLnymAINExGvegNmXALqfvK2viGjIwaKTW8nSG00ZWFNlQqCSvxdI4bKFuPD8L2FXm-ubBOj9q2NflTHChkYuDb6V7TbGH_0_f08fontaqDwLpXPtV7tQqp7IhZHEcImI2PRbvkDYx5YiKR4zeC0SFJWyjlRFgGk7Xgusp5wKg27YqE8_OC-vFA71gS2F_OgH8v0MauwD-6VWhB8LeKo97lmarZoeaXMFVJ1JpXwUfAws7Qpg-qTDReNmh_aCuIArKo2kjvghA0Zl_H6HYtSZIMsR7-gvwnqqDtWRA7QkmcEnGKfgFGdXOjbbWLrjTeqTjUJ4ujxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHopUmU_Z0-iUo3BFj9HS9lQ2IeI-kjtVgdsYlidf9kBWwsp9l3E0_6C71OZddDmxlTh4Kyqel8awxnrw2-iex61mR5KmFmhE_eFi8voJAUJx7CkEixUCSVXPDiC-fTz-VZiMbwkFAX1ibHvq4lcy2aoYnE6kvoLxeZeVCwoW15jAkWtv2kWyLVXovJY01hws073BLerSYlZYPpkWc9xxasBUiO_BNem6JDf13PUEnt2okbaQ33XhcDc_2vgKtJf-jiz95idKro5Jhj_pvJh3w7OwoJhckNKecwzWhLZ8cet3LB2TMb0r7JSUxcWH5IhOHFleepw5lrkYSOoC_SJGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2bzgykBhYYwWBNcu7kOzHFdJ5f9gqt30IENcS7_yV08dZdR0L1S7Y5rEmmr6YiNJlriqvLidVrash7XaUHnD2F86m6dm82_Gpu_ZHydZLqaIu6BcV3dzZ0y38VA4yjtomShvtX6MEX-zAaHQuPR2vk0M2l__Vwzcn_txw90GKMbwuUHyBHhVft2Pa-gXvblKQ9u8TANG85e0yN1KBErfzMzqsEHN2w45uPUFGe9s3Zf9XvQDMnsvVWSFRGtZFI4HylnoO4OOu16x3_z413J-sdeKdT-v6qYhaCEvNjdAbpbu1udO2PZePuWi-ZPNB01sIb8yVdNob1pib93nW5NYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ie28i22W4do6ZfyVnMiuP-9AWixVwjaaywsvOiTvQ4bddJI9N9ZYI300v_yKihO_pjMSqXQ7DPK837oRbttZhPljApLYD1coy8_YZ_upBIjTHkh-Vdwx4LQVVdaMWu_7k-T-v9Qhd0gTKlLqSJb65G-rWE1LM2AseNcuei-uLZgwQs7R7hXYY72I-qEbYj0PzJ6csFIccgdyJ5gK3Ad1a65_4XpdDaQYxP0MmRx8Rp1Ygy_1h3YiPoQ4YRPz-ergb6wv7ZLrTS1a-9ezaIwjI-iI-SdBYqndxRh6NCZDAoJXai9zhPXHFAUlkw_2iOxruwX_s78QR7JEJpQFAy6Wvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnaIypT8B3YRMOeDU2bGdkfTLtxEy0z1YqmB5rOICC56KGz5PbOuBSvDz-y5nJ2v6XZAez3KiFHX-vtZHaDAz6nQS0LCl-cm7krP7cOeoAUF-m85PfI2BFVMG5ULV4Ukp0vuX0OpHNSdCihyhOoM96cywFw7OWLOQmH4XjIeA9IaQe06GN71qJoQ8hCvR7dWOY4OQ8fPsom-R7rmbi0_pNdjxvyYwANTxapCmLocxFPDEop84iSfFqArP8TxGcdBSt3POXJspNz7-kjsgbc0_ZtGoe8ncUKfyNxbMOptPt1QoO1wORWn0rJqtMfhjEDA8P1aFPyW7hGQ9JPaD2dO5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQMEq37ribx1r0mqZVJQSCVcc-7gvXqroWvecrwtI0vl4SwgAVIuKOyFvSy6MMdz_WLl6Nu1BqZ-TbiYahl2oCeyIOJsX9SLsEVPFMUkoNxqiWoJxiQGpEg5tv7S55QibBT3KI-IDBjVxUZCfbdyFJ1Vi6VIOyEcuZkWGSUftk8-wAVXfDXXq-LAzA6pbv5Pg0lGP2vvl32T4KJ3rg6qo-A_aZiMhv23BwjXDmxlYOftRVuNp9xlqsnrA_R7Dmw-TtQM38GpFN7twrs1shhZsnupTMRXQClld2YQz23CEZ2wkGWs8emw9XZU001SeEytww3GQCdSUhGB35lbWJdLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NudM4odx2cXgCVO_UPFxVd1Twc37FzT0l6jDv6Fmi4T1Oy3_dHdWyd0JzMksXHKsYbRgphscxajJRstwipVr1yKxQrKpdnemYQr866JrTJ_jS6eiF49KKOCFsmbJbf2lAI4rN0Td0DTCw80oY0pNZ1XRPalRUhB72zrr2YllVcwCVLmw4lOu-Ed7ecMrnC39IJQXbgRSsZrX_pgixAmsKHiMvijxgGZQiph7XZMeBqdRXibwXmtyseMSnjo9R3ma2DviHx-kqts3xlsI22EB773XtNMwjXa0zm2lxpV4al-l9Y1YH0f6Ak8javzFYPeWxwNxowLVVUlLhqFuFJm3Xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqFSQV1Gdgeskcw8oBfqrtqtii_CXzQoO3B4oF9AWHewhacmvB0qqHjPUQXBNMsVs6AG9vKvsaKrA9YXXC3--QFh_QkdHDTxqrXD8w5xV_Cv7MrP_EMlgqex2wsFqOz_gjo48ZwjPsqPzF7CzqIzR0DhDW9A6KanioEkr95HbLBOO3BVBb-NVxIztfdVpK9OKmBhdyx68z1cKdLiNM-g3c9pWq1CPqN7A9DqUY6Ma2KmrD3jQmJBnGwc4xNcuot7G6BthG7C5fQINuKpXKPzJHBAemNLFqmM_6dERmi5NyuABNBz4iDrVhsiGnsalg3_feCiTEh3Ji1Vo1iNQyZ85Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEPG9jjPjumMl3pKj19SHuIvbQW1CzSyr-fF49h85p815kNuS0eCCkk4YmVSPgf7QTUGB2R1f-e2lqiNKDg2JLxdHy35dpl39XqhFAjNE7T4Bt_QHKhYVldeWjDeU0W9skhuvoVe3x-L44MtqiHa4_0YSQ6vp7yvR5hOXGP8ZnqYwbDrIG7UBIdVmiWFiH7XduyslHOtqb9AB3fKFYoVn5yNMiiAENV-GLQRXVcDRW37U8_ZPaBRG3EI6SKoQj-hSX1yFQVirMVktP4bL4msJlnygxnPj1wIOs-8q_dNkHNdX0avgJ-xKT6hojhUB1gh4UejdS1wiKIX3mwLGsYVew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwqXzo9_fZOlpswd2UbrIS1NyJwVw4M869rxyXYUzcEUD9glAJcLzT5Uv2RSdx_wXLdwuh6BJ_8aF5Goz5MrGwg_yM_sJSIR4ThLHHoJoWY3dKaXWCBNw6RBgI359Wp4Ip3wtDmr-BRJIQXOEK7pOA4-AkgSQF4ac77AAzHiLhLoxmbGqOihJ0SgBTcri5TyDwAcp7-RzsnEbZuYRyatbl7xLoexd-ZZeN_v_fyWO3ZOJP-fF3jurW8EKJW79faMwANjOpo6lXNjTHSlgBATb5fxPK92e3bpN3TTY1qpxWvxJzpmgWgyyxkWY7uX_atoppFu6Qzm-S_ibPnvdxbC-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4m1YuR6cptwTf_sPNEf0A5adCyd8DnX_DCVcsUoDG2oyC24uSO5IGaS01Wg3d5JmzglRG8SIt33U822-Q95TBRiQAULcpwBTuIhUmiy54V_NoSKBHWczhQ5g1b6bEXLWKm7opEevloEKzVAT7B1mepbSDpnjK3slXjYkMaa9b4BrkrxLgAf6_niC1HteuVpOfC6UttdgF4Y-n4x5Px6mEHUcAF8sxBK51gf8ynQNvHZM89zv2uJbsR8pXzUEUPx87B8maxkWrh8cj_8Id65Th5ByJW1Rs2dfP0qaXIelYlbyTbQPu3RxuqCzfO65kB0OTxiPoocQcpg2Jg9dE7HfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh238y51Vfc9730WvVgkSgce5ZYwqvf7vldQ3ZJUpFxNgkdU-a2KqPelV4ZHb4Y4KbhQ14gTRWz3bXtj1W-X4_fD1X9v0sB8hI4QWgZ9jN0oKGEdA0K1V265hC2Ss-4L0WPFJ8IB3vkx7nJXxYtHjWP6YQq5PpLofq88JyXFpWRQ0nDgw7LbT7rutl78OFDS9xUVXbEkZU7S5NT-MW2xCjLFvXRoDzgYqtlBA1UlC7FdSPmq2RQCza5oGFPgJN54FTFfPQW32o0iosLJKU2rmFj-fbC8vzzOvZxegpy4orNrKqZzMwR0vvNnqLxs7FBzJYDRXpbghlU2X5_pxC24ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF6gixYkwr0eog8i1TYKGNB8H5l3JmNrUFtkPYGlbizVhdNKKoRo1P8YundrT0s3bFJCQ188R1Jg6UyNKhkcxCsooLWQrhrJLZ_NdWO58pHCjYQ5nGA2MtK49lR-AUvlsmfTF6-FjJ6UW5VInnQ7C5RS7joT8noAhMi25Fik4seSz9peJSjN1rt_mKll04cyZmv6mPO15RQB62T2RNPTEUDhhcQC9j17GV6Mm2E4xqMIQZcSVMfsEWdlcfh8g01iJIerRDyVe_UmpRZqxyX7bZTwcXxz2vH6WKDJ0Am7W-G6UcJjK9MPWi8LUEufEuan7rjA7ZMMfslcB7EKzrzIhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjyFzP42Fpc_XbCAX1P5w1jhExyMAiBm7wSCicqDlUeOAWgwk8lNMIpfJniHHWGJ4ktayP12StR8qqxX90et8tb37z30QJI8ZESkBqyVAT6FKaKBC0pIVMqG89741-ocxauxsChsdt2wepeJhiMHjkRom2ptYsDlfXwTJOffr_zcojsLx0kNMet1KhLE-rGJKRAZbSCkiBIlt2w5mZegmQb-uJiqhtdrUKN3XApgQgR2THmQw1WzyXFE4HsiV_4N2yIMKGmp8tEiNyuqMvIgmkGrPXDdnuzoNaE5SuLzkOMdvrKD_V0mCFIUQobcw8UhwP0tAbMMPyZqwPYKBOD4FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN4VQb5NeuJav1WQGS1hi5O1jOiPDaAXOx8B7V-bTvOHAHTM1aiaVu_6Sz2h9fyn5M9s7FIki0x43FMBLSmR9oaxjnkT9B2h2T4sg4e8DZZPXE-yzbr8pYZQ9Shd5a--IVc3pkvi6ydGByMXNYDjGXU_dobQHnflPEQwv0CaPb3F9qSvPQvRgrVVDzTa2VV3qwedqZTcwKQXGjFUQdP_ggGpilCT1TDOqGE9v_qA5snEZcFptRZxNWAP3pc5Hj14E-bqIFAV-nV7YPGxFi8SrrmMk4gzg0bkUqwXe9WnE1mDnXWNCBrSpsy-K7EKWLNzRxH3CeacZ7nKzL5nzG2UGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkCGOm0zqFgQoF2y6TzjRjZokRX3bjJHhTq-Sg0dArWaQqgv8l2OskgRWAOCKjAW6Z11Qs_7vAKRJMS2tI_-jZ2fYwM6AomaCnapwJ5t63Vl-7o7IUZlWghdWuEFRuO7OEhBfnaB5VvqXIRjbD7zRSD36DYl3LTBJYwkfAKG7mg6cOXUQEjPoMuZKGnC6z4Zt8Ds4PfXNs4sPCEXU9uHFAfxv-cFGoMznIdYfifdU6GEc4mErzEqJtmU4FhbWIQCpDR6Eilc_iU4aq3_V6WgxZ-V_RRChaYO_XVKzwRCkg3-vDXBZ64ZweW38UO6fKcIF7Y4m3z7BrR43MgaGLTkiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ChIIdmDZIV_yJfeEr2Ko79fL8NLPSJu-toSTAyL1mLAPckQJrtg_r4EtFZSEuga8Lz_2guPL8tZPoLfuL_ECF9iAP4ngw5q9oTghDOODkc9VPt4NWjUaOjOMFL30EIIN47MRfxQ58MsfHf9yDlqwdaWq8REM78kC1lvoQuV8Ka8Mw8v_Mk9umL1caujV7bcsOx-ceLNLUcgTjA1pxBzjuWIOuTHsLPxew76OCFoRU4yFUtV9pzhmN_8IIaqrlVGuuBlaDT0g_jbs3Lw2FjI1YyXMl3EF5AqPEAYhTunDX1gU02u9MsCUzlBplqVta8j1_hSbspPmULIfqpZDBkJWXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ChIIdmDZIV_yJfeEr2Ko79fL8NLPSJu-toSTAyL1mLAPckQJrtg_r4EtFZSEuga8Lz_2guPL8tZPoLfuL_ECF9iAP4ngw5q9oTghDOODkc9VPt4NWjUaOjOMFL30EIIN47MRfxQ58MsfHf9yDlqwdaWq8REM78kC1lvoQuV8Ka8Mw8v_Mk9umL1caujV7bcsOx-ceLNLUcgTjA1pxBzjuWIOuTHsLPxew76OCFoRU4yFUtV9pzhmN_8IIaqrlVGuuBlaDT0g_jbs3Lw2FjI1YyXMl3EF5AqPEAYhTunDX1gU02u9MsCUzlBplqVta8j1_hSbspPmULIfqpZDBkJWXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFADtOwUzJDs3Loo60TXekI8TMNVsx33NtRb_PgaPH1T57bq9ZGPlIP4ASw6SI8pdNy8LiR_aaAORbsZlJjv6icGK3m9MNwieZ3qhhsaGq8W6bIx67o51XVU-0NOlJcXC5lmNvRCXachM-J--jBSedKRoZgySKvKzSKc6bHNYBkZuO1XfW0rL97VWjK5BYW5tfkZSyKHPay41vmc4pQJ2BQOycRGS_TfAGenHBnNvZEXrzkTDECcBucdaMnGnIZjl46PEYP4RzDWLWqBk1NpncKjqTGya7JGTe3DubXZ-CLHPlmcPzodMZ1qMqrVunny-g7nNJUzTu4Ixl7FozT_6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZgDR0JlPUwl_n8z5kUY2WDRPIXkN8gvcYkg6GEb9cGg68vBuodPnJ_UUbCQHltZnsie1luahxT6q79l_BV7XasAD3Igsbt29waG2sQYgdYT0s16pSgKwhPSkeZicmeCDGzgueVcbj-Cd4yn8TXfeoVDUk1HQQJdVbfBD4yqu3V0PquOKTk-S26UUh5mj3wh7Rg_cWPpPkJ0gZ6wUBCIeg07xaxI7UHrB3zSBGUUf6QqeYmbYi00sIpRw3grq5YQdGoax5CO6XhnKDcJovA89HTL6MZEG5COlqHVRFTm0QjjSr8mUoxpMmhQO_E5-UMcvyut0ypKSPVb_pU5tO0XWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0RRhUJ9b1NBPK9Oc71XLvaQaJ4Qj7RP8aRsZ8FsM6UGWeqm8Q2u0ppo3MEafz596bpSM2Nid7Mupd4_DdPVKY_M6J7th3cdiKwUtbyis8W7f9Fo32mA3__oTMKznmiR9jZi4-ZwhAOLApM7vCCxh-612qg61QgXbNdEvg9Fx2-UVURKIz6rWfC_wPSo-bgRVpcd_qVzU9xccPZHpRgH9LaNgNdjCmZeGzI0vD2HODWzL0N7Vl4ykIfPfcYpfXfbf7fluuukAnoxFOCh_RQe4o55uEi7FXWfc5WaAyiK2txc84BUT7fZmR4j8KlyNNr4jdfZKn83uBeRfqXdhUmRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWpZu27evbS3_HkmdJFzg-8_NYbiEBTzqS-u0EfMJ4T47rHdgkkUWKx90Xll662lT4Za4LC4HUUcG0mb6j2BW1pPDKzMySfR1L0K26gHpIMxfQQiBCmcVqj1t1IjEpt403AicuPqnCkW6JTte0fDI2Eti2OggAEF97TVdeUZ1BP91246ki5qZGc2ewlOVTTG6zxtH2kJ-PClsJXHbu4nUZ5nMubFW6AOqZUJuXDZWVeoERjxb8r1w5S46zWqAgjey7luyBpiOikuY0oFttGG3_CtkhbcP0nSqJfZhHU7731GBrBoDtsJcFvR6JhFdvJ8K6KeVP2IX7xUwO8dyv599Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic0nzXYMC0crT37ej1VfVFac2AlWTJqUaOiRLFqbD9ovIPuNefk6xYru-jAfTdVaePLbnArbyNS_b89ELQLOJtaDdAPDP1qK2rFuLiPCqe8Sf5anH02XcxD31Wl7xipjzzs6cRnQHWFoebrvJjRW-OcfAlWfsWP4iMB37D1j2twcE2YZYefVuiEAIYhPM3EaLNE8vkqrnR8TH0JUdFzLaVxVdJbsK_pWFEvTn88IBnPG-tBmwyrH2WN2BtD7Tlnn9K-6Kd6w_DvzYNm4vWoT_XPz5h3SdZjM5xXVOFoibwdnV28EKTYbwweTY_IDjX7HZMtW1Fv_pz3AYIoepgOFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aS-IgvIi5i7gYydD0E7u2PmELXxmjMKF4r8s3xiogzB7R-bMzP8lunWo-TPi5MK8_5jTT10ulsFqBUv_0_D6iI4Nu9kqBLMvRZokb3nnrhcGqedYN-DfEjM4AVYIrQzhlV326u9HRW2et800oXdF-MXMLTKL0C8TcSQwoPKgMSzFW2LbB7EV7rCQvt__VwvUO5ryV5z8GJ1zrIt5MCK7v2kr2rr-2YkQZjmuUcptXCwCtvPCBcTpupQnk_GEmShLR_L-CzOOnfwISbkOnR1XdqlVHqnDLyzGi5zI4riDHzONZtAosIqF-0VeYu6XcysCdbncgvzivyslzHPQL-DaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kS9mnpRIWylK3CXb2usQiq5sZLQtsH5zkjyulapNbpdRhWyjKN6gymqhWs0dk7DngkHPJoK7dXnJeRbmQC3jAC3fk3p6beHCYorgkoBL34zj34NkDeMtyWZMjjTiUhY3Xvr78HqW5eOdnNwtNWAMa_6Fbl5pwOt-Jl15nk1058tl3hoGRTq5ZNWcN9C3ApPdh3J8NegCEQMr3QePZJ_NzdTXqY1eDdWV4HjrMY0dFpjWjvFOiMqirZNIlOC6K5WiOQOdPc2mb0PpXnPt2u1w8gXCbxL7GkCuNgPzrHUiys5k4GB928pzu2gi0GqNQcu-wsQ3OnAiTid6MoNeOV154Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=oVG0Jh6LjUCUixmg3IsXMj8Om9LEFM0XG4GQhsGIXcrHhDrT_2U_S-ES0N4SEsqRSRviJJARad3vtj3WBu_YClYN2mccBe-JdWf6zHCI8YSxLfKaGFISY_UO-xO8vfoDTKdPfEibnargW7Ew_abIs2Z-AZDWId9khbOoj63VI7f5EHbjYtt-mn2pStLMfE8k12Kaw-X6Da8LwkG1BnkmA6NqHbkvJ__I6LHlcanV1H49b5ZE7YbEkQ2WSehpexRWZeXeeQauDLE-ACn6BJlP3IaRJBkG6MifbHWlB2g5BXmy8roVuAv9CZhVRgPEvzJTITjcddg7cAEJf1FPoSUP9oaa_nzkngtceKC59OcuTtk4nKRaI2Hp3n9ZqwPUggmPkz6InNOpWiwMbZu9-Vqt0kBmYqTUK2FW43IoRzV95759g8QhI5nEaB4_HLeDMSKT4UZVxQwYqiYbrLCQmpbQ2MuzK49SGU4K7krNyevUp8iVlcSaYUhkx1SYhXUffdBHC3WANqfa1adDBa_PubUr1fIoqxYWoywtTaA7YwQnzb_SOvYj9CphzLCxONXyI-njJigZyTquN0Nbu1WuqkjbOpGSHCE4DAtmxAQet-5AOphoYFc58c1lOj6JE7qvp-vJXTR3k04iJdTrXccJE0DmbW4wipj6rsSKTV9Ab0b1p8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=oVG0Jh6LjUCUixmg3IsXMj8Om9LEFM0XG4GQhsGIXcrHhDrT_2U_S-ES0N4SEsqRSRviJJARad3vtj3WBu_YClYN2mccBe-JdWf6zHCI8YSxLfKaGFISY_UO-xO8vfoDTKdPfEibnargW7Ew_abIs2Z-AZDWId9khbOoj63VI7f5EHbjYtt-mn2pStLMfE8k12Kaw-X6Da8LwkG1BnkmA6NqHbkvJ__I6LHlcanV1H49b5ZE7YbEkQ2WSehpexRWZeXeeQauDLE-ACn6BJlP3IaRJBkG6MifbHWlB2g5BXmy8roVuAv9CZhVRgPEvzJTITjcddg7cAEJf1FPoSUP9oaa_nzkngtceKC59OcuTtk4nKRaI2Hp3n9ZqwPUggmPkz6InNOpWiwMbZu9-Vqt0kBmYqTUK2FW43IoRzV95759g8QhI5nEaB4_HLeDMSKT4UZVxQwYqiYbrLCQmpbQ2MuzK49SGU4K7krNyevUp8iVlcSaYUhkx1SYhXUffdBHC3WANqfa1adDBa_PubUr1fIoqxYWoywtTaA7YwQnzb_SOvYj9CphzLCxONXyI-njJigZyTquN0Nbu1WuqkjbOpGSHCE4DAtmxAQet-5AOphoYFc58c1lOj6JE7qvp-vJXTR3k04iJdTrXccJE0DmbW4wipj6rsSKTV9Ab0b1p8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLlU7quHpfT_HMVcLfOlNj5Bfp0rDbGPo2aN0_I2-DaVvCqB3iGMTMHpNdPuUn4RQ2uQcbYDCN17YRnqHZ_oirQYC1ZdoOZhTyaZElWnXkD1yXLlQxoiTbSl5lVkzN_SHtbqVrqDR0wsPREmgZkfs9uCk5G5HcBvASVeXzCmOhUWjnzgKEBF5etsO03hd5q6_50cQMyKIcpte5KF3oiwvuGziflerBlm3HWrlsoyZUUL9T58VBmv-4RlPiF-goGyxJc4Q-L0EMJRvRl3McYkX4zTvXA0dscTW4axQUloK00xj6ccxthSbhy0rOkpMogK4ekdyGVPQmfHLV8QDRAB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKuJLl7T6s4Iiudr9s64ThjhdBDiTv3u6GieGDBL32uIZg82wbUT5VuqTt2ulAlqWNYs1--k-ZauPGKjBIGCSPOCer-PQof3YKkIJXcOAEnjTAHkb6yzzxSwb7lfHJodwFiYP39GFvx4PHka4GfpBpbwGi4JbiHXmzg8tTAUw02l15g3pYG7Pj0zRK4z3eBxc3uk3Own2NmUeO5QLGJdEz81wL8rtpa4V-cfHUSN7NxpncDH8dKxUxN0qugZ2qLFD0YI4UgCM_UEdEbGbQHCEywW2uNUFO5h-j2QiWCLwAXtphkeCIwWIKfe3AG_3nTKMdRTMFpZGSkoYgq-XzafmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RIr6xM6uW6R_SBsdr-ZZoQQmW5P5G1rYhblt4spJ5k5O0OIPhP-SgRUFDz1ibsU_bR5gjhMsfzp82fjuS6HKR1Veso10MNAdo_Wj3Xl2X7tg3tED2ICqMqQpxqiwa5NKXGS6SKLdFBhoJLd5O3375sJzNud_v-ordiAHqCl__NRhB5P-A8MnC2R3d-tuZAPCZ-pakoI3i8zBLHDE7m5hkT9YMP07mavDT0XSwNC3btPnK4ovn2ABy3qZScvTb-_Fltf9eLm7QCTW1e3lXwEOqnHNxYsR5nnXX1vBsjZwSqFarSdOx2i5F8Uobj_5m8MW0DlRp2JjxfIsf1OGl3_qJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGTsqeTAvHXEf89VefgFWjjWemr7WyGZEOwFew7WpRxy_4JIvUBTrJVi-A2yPGkVQR5XL003rzJfULjIx3w5VDoj0-38jou2l0Y-Xp75B1fga2FOC0TPXwunkpVaXII_DMga_NtrDnHXuNwyJCrOfNvProB1lvnvKsI-2vsdMa7_3UdawAeVKKckT3FnQVAKO0q1DGWyD3hesAN6xdggYUdonwyBvnOZEx6ZiiDnGGTbm5VgsmMhjXEiMVbrkvtTEUPWQCpJ4nWvql0gn1zOhHxmuMZaUGKpyxnO3SEkDV2zauVSxIv-LiF7Uf3fzpWbmWi1gOCHS5wo5GvdIkVHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvZuIPKPoe_GxIqhepn9UBrF51BaJ5iNydocLxMy5LjkQzpU1SfyQR1O2pIWgLt0fOdmSfZapo18i4RIbZ68TfuyWor24ydReD5lLuPDCAjg3NV-1aBJRqNoK0EWxip1QCfSUWBHZSACXFusmGRsR1suLGHFJXXaIlKM_zyHKYtD4YmghMfj_S84kfKu2nz__BnZSAuAS9JDT8ohVNmwArOeTNMAFf1WQ6viF9altMqA_xm1at8wgz0bHDThTINqZiOhLyh2pQhr2SfLBpZbpPf3V1h5GhfyJge2DQ9X7TWZOpFO2499VxpATXNBcL0D-dD0L5q9mkknWtabYkKf1Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0XxhJmnT5JTeUT0FW0T0-Qjld8jiWDT2fHlJ7-lZ9tDRBfZAUHymhRr7Uog-PMVjLlW701HKIuwbEl5CDYmo37qOrtDa3sQ3ecMWAx-lrApLJhdcW_BAr0xVs0s7DUquvdT0U1lHRz9dRtHYZeInJ0IZz3YWF2MQtcmthwSGuM3h92onrp4HH2naWezIsVjrSTvJwsFBflGwZGHoJ-hU6E19sNiGzolzeoG3rFw7LCynSEzdaCcnffnRCxLHujy9uCdbYKusqGBWqtXMRPTFPpJe8wCGS611O7pelAcbF1rfiF3VnJbf4eWcYjFtqRxdkwDqzEAZO_Cfy_72p9JzP_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0XxhJmnT5JTeUT0FW0T0-Qjld8jiWDT2fHlJ7-lZ9tDRBfZAUHymhRr7Uog-PMVjLlW701HKIuwbEl5CDYmo37qOrtDa3sQ3ecMWAx-lrApLJhdcW_BAr0xVs0s7DUquvdT0U1lHRz9dRtHYZeInJ0IZz3YWF2MQtcmthwSGuM3h92onrp4HH2naWezIsVjrSTvJwsFBflGwZGHoJ-hU6E19sNiGzolzeoG3rFw7LCynSEzdaCcnffnRCxLHujy9uCdbYKusqGBWqtXMRPTFPpJe8wCGS611O7pelAcbF1rfiF3VnJbf4eWcYjFtqRxdkwDqzEAZO_Cfy_72p9JzP_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcZkWRRMfkMoy7FcsRxhlo7ANk7tT-qorVZyxM3Asg3viYbPbvsJaEqOXGLvFzKBd66CAVN36YKPd-t_WhZj3Wz5XRMwP98gRl6mi1bxes0M-Y0nlD2sK_e0qgqZoR3eHiqvtIrebaUVPQtAqDNOBb2bQO4W9KU7yyTWn35qQrgfYsOv2UwbbcGCrEwHvrUXGcGp_3Px4afYCu9ciSu8bqgRUXubOSuZQRuVfMeNdTajdNjfr1qt1zJRKzxFU3vc9Q4eQsppmLTq7LLeQx1C33CnLqcW-15CwXR6_ZBg-UEo01w-Px5H738QvNtkUAQFEN4pm8DtYNwbe2aYl9RkgQ.jpg" alt="photo" loading="lazy"/></div>
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
