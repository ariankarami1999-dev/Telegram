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
<img src="https://cdn4.telesco.pe/file/mN4m-epBkGk1PsZzmS34SDKNNbi9aR2MbV2QKpAgaqnMfWOI5-r1ySYkqLhyqGOMF66-C0dSZJLV8TjGaNpjkRVl9RfzycU6kmxK08QXU_J-nme_CSoTAn-rB_uuR9qzy5Q5y_Wo9v5WrPSd2b5bTQ07cRpvJoQJoTPzw09bvba9QB0SxjIwrDJ5VGo_z0Gp4aE3nYsT1CAfRU6j9alWj5gu7RCwxkzpR28fGF-foqCiJv9A4OCdUQqaMrOnBxSadDv5ku6Du6naDCPqgf7lv_tBsTRU3C_6PnM_yVP9r2XC3-kRvD_WTEcR-cBJwqaB3r02YliDaoS7-F8qiPcZxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 275 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=fCVyQEkiqVBpgu6tUTOaTCeRc3PvR8ldnXyYrSZr2ccc2b9mZq78X99OrNwT3YuKcJCqaM48EMzIVmY6xWs6glbYr9ugbnGuaR6V-9vRWhbYKMIJsTo2rLoQIA2EzswOeTJGh4Pw-IPbCLA3K62vWPVneaqKeZqB-oC-nI5bq3Qk9fGWIFdPbhZLe-gEdBC7tTBxi0IsMOo9g3hrCNIbZ4MpS0cOueAGCuPV-Edy-7wm8cECzQ3JzY6PwpRESpI3IsS-eeLvSnsjRvqbTxkBowhW1y0gTdUW4-wdoopTkQPag6vIMIMBGs83sMMFR314S57-V4G5LXJf84NlA2N_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=fCVyQEkiqVBpgu6tUTOaTCeRc3PvR8ldnXyYrSZr2ccc2b9mZq78X99OrNwT3YuKcJCqaM48EMzIVmY6xWs6glbYr9ugbnGuaR6V-9vRWhbYKMIJsTo2rLoQIA2EzswOeTJGh4Pw-IPbCLA3K62vWPVneaqKeZqB-oC-nI5bq3Qk9fGWIFdPbhZLe-gEdBC7tTBxi0IsMOo9g3hrCNIbZ4MpS0cOueAGCuPV-Edy-7wm8cECzQ3JzY6PwpRESpI3IsS-eeLvSnsjRvqbTxkBowhW1y0gTdUW4-wdoopTkQPag6vIMIMBGs83sMMFR314S57-V4G5LXJf84NlA2N_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 378 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbHGMgc9edUfYBx6PWqB5le3mPR-JR3R-ORLwRxKOx2rbapVXT98RzsMSVlVmwyxfMkWke6_qa0lXV6OsPEmMzyemdg8bVTCQhUT3UW4mVyUMMTA3-3lvhIW9x2MMHckyYWENiM2lJOtI0u5JaeOF4HMJB249aJjJr7aTZ8y7Wts9r0gMksRLZHO_zISCLrjkn-UReTxTLN5bgD4BQw22jcBcbOpok7CVON-QpbuNfSZr34-uyq-a4yeQ7Wimgs1jvK66_CfZdVvf1vd8QxT8qYhVep4sd0KwHWvipX-4bBZIay5gRO9G_ibU3u_NA_m7Da8-Efzwr7qMNjPMy73OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 504 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4oi1zDp_KsZS-jjJAyXvtGHGBd_vt5QQ4Sau3K_9BjjvXeZKbn8XJ1uwVLnbuzV7oA2weRngvtV9YX1zrDF1LZgX6cV9zpMVrfr-yRUJ_8Ptlh1h31X6ChJj0Ldn7ZzRVfcu0bvdBlQ3M6IIIc8Gwnr3oRwhRtqtkHBkMEgG5xDVHhE-4TkhIcGeweNHX-7r_JDjShABS9bwzZtYjBA0MktVyV2zazu_DKwGu9Y905nHHf8RsCVloTZNiw8xpJvW7sq--S9YqR0GF6plji2eQ940L3yKrFOvGqqW-ovw6IoQqzrUQ13b_FfiegyKUTQDna4wUVVL83tRwUJ11Ek0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odf8jM3ODMoemGOV6Hfa694zGm_vsIpw3AV5gCSO1hO_LxVZd1-RYTj8HW3DG-uudIRYbMReV2IQTd71VW3P-8bK6AQSg3R1su2MmiPEXOZAB36mncqysllkHgFQ0SF3Bs84sZa35y-sgsMiOt_wKzATBTJXgNZXv-_oDGahVeffbGEihHYQV-SX7spNJFnXihZi1cAKAcv1qTRDxD_WP885zdrZA_2VQ_al1oInk8VFctvpLqKG37C17_Pdzr7P4F-Vnkvf28k4u5IG9e1BGLAeY3QERH_Klnf-qKAlRGo-R0ewRYBX01OXmh-KzAiDHkf5jFI5NOqlzRUOxMJKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEZRItdt1x-SohpSeCBCyiPrumTfztk2hJxSHBOSs-CNC5xI4V0zQrxH34DZGpmYLmDoRgBrfY3hw4HU_GOa1WTvS2iPKiTodenfQ7FICO-PgyFDjHUHSuvNzMj_0IBPt5TouppoN1wTL_zhw53VcdGFI114L5AKcvnFU-kO-VF3ZHQ3CP71DD3ADDFOturGc54MmTL6_MfLMBOkVs9vTcZLx-8IVSRyuzEzThuR1v57PU9uSzWEudI-KiyAjHjEb0AK4oHu6vTkKpedPNgFnAGdQQfzbYNIZOMQHndQm8X5IaLAChUTzDl-0VE6RM8VXw3qMV3wJI_Erk3hYWiuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxVCtei9VdjHskVo_JvCZ_Cx5zrGUJU56NnrWVpTMS78PDQpj8gHQzSmlE7y3oEell0lI3VLRz2CoF4VP0wZ1wzFxAQnlqKBB_4A3GsbjZ30kyvaCQWdmxpWXAJ3AYVMZvWVnz3jqyJ_hEWyMjpmyf7ga8w7CXTv7IEwJvMsUw3IQ96ETRa9oySpPYsA0mgMyiqz2CD_K7eEGHkGYEGREsO0fJ9JF5qw6UYHEYlgHSUAAwQMz64kHrAVt8TG1INBSD-ioCktudLwK3PBrcygfxf-odaWbz5ar7JWfhrMeyIRo3EP7rqOiCqc3f-tUDzTkNwL6HKOSOrcjDJrh65o7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJPRk8kEqYnSoAI0wNT6BcoAdS1WGRsSpu4pGfmhVH-LEtDSWh9YYCKo2Zu5gKWqEzliZ5v9AlfH3AjaksK1tLxrafDHVG2TVMpd79sPQQUSUqxTTUS817ka6tHMDm3LN-z_95AN9w3mlIUraOpkmR-SrsjzoGCxZN5ZHPaDvhLnZAU3GBEt3oxMqBWfvuBuSyz5Kh1tHbcEKZGHTjh4p2Q7zDNuiKu1VckNdG1J2_CxzgIhHpb7vdiCpkK9L8EjkbX4M0p7lAmj0VN9T5ZM2_emV__b9X5d3emo8j-y5tkFtAzUgMmC7M57UddrGhSCmFe0foUO4KeNrGK_3dL0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGvQNu33RehG9CFeYhKWv_koUY9H_vyvYx5SPmiP7wa_dChvXN5nCcAGV5InEbPGGwBbjyT3GCk5P1XwrVzOTiRiuJJ7HUz8-n7QiOCaLHfkQMaICb3hoS6B7X7oPEHt-Oom6hDRWMISHMqcroQA7G17we23Nut_K-J6y7vb0cNG4BluzosRGOkwdWxXjXvZJKxMxXwA5X0Mx9J5vuPE2509rmlfZiOLUmixBjjMCHn_lRJywMiO0YH-xkODPKPGZ5Q4DEt-iZ4xzdTRcgV9KRCim4wDvORtzQr8eT9opsz5-dYsF6dNlA-BMmHgTAVlSPUONVMWLoTlwaw9DBaLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md_7RoXVa9PxZ8PxBjHJFC9r7T6suG_nAS8K90XcbEeN29AXriOMuYn5N1KFll9d3HWzJzdOm_U3eklwCWAwVJgqiNxyvZDEMQcU9FHQ5eIHk3RhHC0oeXuYOABM2IaeBDfKhMhO_aHrdbjp1arbMEY5xzENeQGRU4vZHszSaABdK-U9eDKoE1nV0f0ULPnd3dqY3FM5FnK-8a4QIRCgQzTrDhF0QNT5Q_YXaW37xooaVyLtxSVaYG73pRuYczzTZXrqqqg8LuvB2Pq8GBS3hHc-yFSm2NC8Y3mup3kd9apyLLlohDxln-Ub9XGC81C27myqaROIXNb_SwMHXIicgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NniV-NuDxF_-Q8rjC9m5P_RBZHcTXXkNWXnRLjZCB4eAAShAU778WfogCzODH9sXQwPOKpq-xRGyK-EZQc2Lxe4Fr0o4qo7LsxB3tIQbB7UILTMbeyZ100S_q2InPxasosdSfqsgnp_pZD7scIkJIL8c38XA4v8PqpsvUGwXIj0LcQm1be7ez6E593_XQYnMsONyi1DsFn08yyY6X49-qmdJji1QjoCRwvpm-BelDw1dk9IS-5xiTdcMpBlJ0Cu5j-8L9_OdkKNmPyRvMXjAUrr44lHeLMkrwyjZZ8L6iVJgBHAjFKJmZa5z6v5hCiUQDwq6Bb3gazFOEbgVpwwXng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdprJx-UIVUJY-6HazKqyo0JS7H3lIdVlaPYSSqcCeyBg3LAH1S2JLmxezkFAVZucVJobjb9n1WCW9aInbs1z-Wf9W0v2VJAvKt_Xw0SD0X62S0RP67u4iMm_5QKotaChZ8m8R11NJKqZPWjbkHpC8u3ofhy9QduXyciUfeavcfdkKFDEka9qJQXC9TFyMznwSpGXq8UDbhfZwGaL3H7n-M-G65Th1ZqiBSY_sn-QdO_RCcYVtgXGnPZKVjViluT6LRDglpanwrZvxgawU1UVFoif8e-Pzy7QM9uY_G20o7kHMkl-d_i4ZfPxRqY7AmsgucAEAOz2Q2IxoyHSmxE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol_tkQ5_FcgZcbsZqhWEJAX_gZLuLt5q2cy-8_CUhLjQyLmMhCVFoKLmVEDWlv69OwPDelFsEsl66RBvMB3BGANbkoPU-sOakuBv0K_9iIGeuEN2MTRPPk7iObkEO4tiQbZMgOx2FWX3sMYc_GgFHbo3qM_UHVCSDGD80Rnpc1mwUjexttNc0-NIFNnwZueoIS3zAkq3_asB7ttUJ8KDiTMroVO1j7dbBkXI4lzpa92L1ADyHc19TEqfaJUX4rbs9OMErKHJSKpLKq3I2efYYKLRbXxFwEJZO1Ns6DRi1onxGXCEwuzww2qJrz6eSji71AH6qNF8RadLi_90dlGceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKBELBnQE35QECoro2mw4VRo9pl4qxeIRBbxqsTIdLj0m80jv1iulRnGiwZkswajsugZKqskkPk9oHMeCj656gHcyohIurw5RX1zOmyJ6KPunX3wvmqVbXvM6yXetE53QsvcXJpI9rLA8Nob0Tu7hKoq_Gj6FpGY5M5DJIo4Sf3eZ-qGGNADWdUL4qGrAAeBVh2AKZcEikdmbEUachRXlvAI-J6WMNECcB3t0LxkhpK52PXH0wkv1XQuzt5U9o4NiwopQTQ5shvCrzoD6j18Y6WvYSEmw8tyRMTENhywPQ6JpZHa0fgyX1St9jbpEbiKSvnyXyygWmbs_6fKp37ZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flqDSioQm_GJdVGBm_rAM3Q2BMCNHhbNQygoP9eyi2dVfp1tng6435HObfBaRoIOh3MGAfoZzh00TK9WFuFAwY1gT8vMmnK39yt9_V8L-HTmLUd8OEkA-Zh-cHr96Ev0QE92jEOSUTjIJf27FNJQkQrNTzmbQhYTTyUDLCFuqQ5w7lvDBWDAhmfPgDUJEx6tXhbdhBbkcInXk-z3dRjE5FHP8u9Z4MqO7UzCvQkAOIt41R9w7IIetYqbg8B4c5wPcbX7dLEISTHhUmNPVsRJpwCU9ioxhReXBLmeMBeAtebiX6ZwOBvR_MXSE0rLKdtrfDnfU-571GEIjn_oLjxXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvDxPj0cvS7Uh_u6BM15Xliq8Gd_qmlLEcU7xzGsljSwtjKvwlE42JX9s-Ak4HsD2hdc5zj1XnCryFCa5Ubl8ehsv-cI9R74-s_wpxuHGnQG6ZbYyTfwdOZFth-urqx6mDAVk1QX-efPPB5izAv4uKWH86AyGAEDd8k3TEzwnAdlnxfP9-3H-edL54N3Tbgw0-vzysdr3D5CD5-6iaY4m5T3pM3JGO_yfLDtBy8DMrwmkRBxfkErwPQG6QXSV-W_28Bgmyr8HS3p1jGIREf2HTuDe67JkwNLMFueuy54wrlz8jP831v5dgxgfwU2CajtA55o6rO0xWlMMj7ao7Qwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF9Gv-IPPC2_4Xzi3rxcv4PIqiYl6FaVaoYFUvhaTtIlQgbtGSvQl7MyKdF_P-ivA37iKkgiHBDXTDgkWVS2iQIJKmI6i9H1S2mZXjdC_gZy9fXOtjZqWr3r44skYPbWXnFPCh4cY3YrkWuATIGc5FaVgcp0WoZInLJG_zn_VxMf4yulDCOl13MKoHWrhjXH7_jP-296T4YkbB7oo6jIQvK83G8-JD0wWSv8rvByMrYwkIOYybHOdm_dAF4kKrD6rZKAxr0qHGteYocFGMSk7H0dpTq0EB4kK7TYgCw2MEyBpbC5tUCkZkW7yj1JlxSopWmqRJtfWYnggv2U7dKnOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQxpvzVBtEPZKs6Ye0Lxini4hQg0gHtvkxgQyl0TM1X1kRtka6K5coBrwQSeFuGV2IQMk1bLuSkOGJl_NBn06z65qAUifDExWEI5Cd7sK42dosnhspDouqwc0238cEKUKkeken0w20vEkWTu2u-2Nz-qQaVrUgfDQFKwtdLiIjGJkkfU28eQjaNukiwcHBFBYxdVo42jWPBpRJ6AtzLIz1z_HLtNnZfnbzY7kPIkS52B2ht78GtT-OSWBHCroX2JVlOXQ7TRLYTZVALcOzCii7X1RCrCBTPez2x9-BxGphhCALQKVfVP-FweazXR8rWcmAwQ9FDaCQtgFeV2UgfggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFd3RG_q2uhOrTa23z2XftZLC3AFr36huCaEc92-27IhC_PzGj55znUU-aA0UNLbV67JVUWKKPNBE8R8NhEAxjdWL5fBHFX2sEewRvitEccMPLFf9ntO7K5h1uo6OHNJzNX1e2Ou8muxUC8FLr1hcWxhxtS0TIu4FGu6JnvwYr4YdbNS3CrsSgGBNtqero3v-5xsS2wLpML2EALlJ0JJf59gYQVEmOofoTmkU4IDbotNRsZgvqtMxC_O3WL-Z46GPaeXvuU5DNueNaiJa6yRXyHeDyA_KkTNOui5VFSJHxCF-HGi846tLqkXdaTRC7FHayjZr7PztTeJXt3zeWBbzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re2XogJfJ7HtRbr5SGgSv5cE2mJqCoJhcde7TGDgAqewlyRRvGVkZXGzXM4b68LhL6JVEZNLP_sPnlI8ch0bFMFKjRV659yN84k-Kd2pyofYOixMd1YeAzVfD1hY-n9DXEZfOHSzg0ZXSG3esfonkz_XtXyCtvQsDKp-xAi_ndc7V_wcPLKd2r4fu95C12vYkqD2N84zz6lKoRZPe2RZnvzSRLH8JH38Rz5sDF5nCV58HaZ3TEqWfa1uE_FpKlAOyBrUD9p2xCOOe4HFAbOMzU7pI92dp8VPyPKtMZgFA8PogIJBKL4gplyWnZJfWu8GNx3jv6TGRLxJSPZlsljRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=r60A1JDaP3m2fGuxkRCitZ6cPncHABnWcR_ihqfMADm5Q9b1mFCCiTQGm3BKEI1sGsYvdU4pirtKhzygLysKup2ggUvF9yCdrZdMSxP27nruN_XvApj8bFMZHrXUrcqbKtA2gfERxqyshnTwVfPsIN0f5VuvpvRmmH7wt9QhTjOJ-wDva2tNwvDIqrzjYOrz6T4_ElOryLe-k4Nj1F8osGxOgXK_7gnbRJ8zTWdEXiqLqX2CHwvk9Aelm6GRRkZZ5cGK8hWojAEAm-QXVN2HMEAkrfwNc-hay4jxSDOxgX-mEono2swccxDZqxkxa7x4-cry-6HyAeJSJIX2P1SmGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=r60A1JDaP3m2fGuxkRCitZ6cPncHABnWcR_ihqfMADm5Q9b1mFCCiTQGm3BKEI1sGsYvdU4pirtKhzygLysKup2ggUvF9yCdrZdMSxP27nruN_XvApj8bFMZHrXUrcqbKtA2gfERxqyshnTwVfPsIN0f5VuvpvRmmH7wt9QhTjOJ-wDva2tNwvDIqrzjYOrz6T4_ElOryLe-k4Nj1F8osGxOgXK_7gnbRJ8zTWdEXiqLqX2CHwvk9Aelm6GRRkZZ5cGK8hWojAEAm-QXVN2HMEAkrfwNc-hay4jxSDOxgX-mEono2swccxDZqxkxa7x4-cry-6HyAeJSJIX2P1SmGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-1YbDTguW_o6yoCoVQDrHXQ-gVjD6MCRzzCKOFg4XkTpCTgikfK_bDhXK2sZdsszE6lqvvLMGLuHriKiiPZWfdxI3ryG_6IDZ2B-5n4rOPWT6QKCmYsPwuk-aa90VygWrJZwz6Wn3RVEHV9vOxKP8_-oznD8gab6IfY7UNjT-wXnUTFakyMlO7lyTjB8lNFubRr_gvQP06JJs7UZOd_O-onT2_K6BwsZSg5gzi1S-OUJVzWAlQu5nwtkXRm2lqqiA65R17bB_1e7ORkMCKxiFt09gog3bFWW95aQ_nKpAEZ9u6bStl24f0_6tRzuPjPsgKUQ4Uhds7pb-RkxnlMrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 927 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEYzj53yLUR3tDNgDFax3wifgFx48Nv4Se2BZ4Jiz6lh_TgDbfyPvwDbQKuMEjuvSnfsB258127lSMU7SdOIabD2mMxwHCMJYVBn0Kzp_RW-o8kv773NtnTNVneNmMWTo78rF0veKeZmCX6IuuaCO66ZfSOCuP99qEndW54YxlfSltnQ8VFKqnKxNM-WZxNYPDkvLSF5YHlpkL8_BtAuYXeULUIQnZ244rgAbRW7An_kf07sfIAFoMnrnRSewSV8Bfsr4l0nGJhCeDo7kCz7rq7TUGFvv97kiFnjV0f2vM68-csSdiESLDDJt2uYj6dMqyDXBhLT8LL6e_CSuPynzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qp5k6LAraBTe5tZpQzxXipq012STR9bI0QYrgv7sBm6218HUx8OZFmr4rz2ZKHmBXnWc2LzqdBXw6LgihnVziUEet_mAhur-uxuEF-XZ3J3uuYKMVoWlebeGk0prAXLrdxERYQe6lvUdar7LdcTdmPJiU8mJVp2MRXIP5dWDGpfV7nZv-jHpez7oXgRWk-GSz288wDDLHl3W2zzfsdGcNPNRZKyoAkoMrr5bddravVXo9PXcUrr3Rs40DGkOrHFGVw9O7qzFn_DtUXot5g5VtQee6y84O2q4P6RIlD4rnWfeUUevpskT4rR9mPORO1z03viB_t1B40rt-zHbEp6dPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQLz3Y5eIwo7NP2R5KmH_ThClZL6XZKM5f1kaR4Fd8jzp0tjn_6mrFt1SZ6Y3utToWvDwugMOV51T-EVW3V70uAGa8ue0EKlz3BKiMWU83wZNK2ST-rU4ubr_4oM5gjPkCBDyDgbH-Ami4Nua15yE4j04BPYIzmqWJkxr1AVmGu10EeU5x0hyolrXvBgLz-IbRJ_iWEXE-ju_X0v5BHri2cTbYZTIwyHZOnmHbPRSxDyymjQHLsOLPiT0asco2zAKy8-HdkzRX_EISjcQJB7Tqrr-YrL-bRrpPfWE7OLCPFR2Vfl5KXrnIS7CPOnzwJs6PADYgMs96wOCiF3aO0vPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 797 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsGVBVfW3_ZQjKC0OR16aV6aYuLJloLYQ2XTnVTs8thqHdG16w1eDJx0JNC8KHwVaBupR3-ufAJFz60xkUduxFu9zBq2ZuHIspGmMheIcfEpRcMl5YwQIUZGPfFKIV_7ieojgHpJbPLXGSUATGDknxvgj_sTusRIk2JYsXwu0zcTy0lAT3lWLMRAoWu5C5zdnVX95WKymbP1EJxxlziiwrqeFdwhcycX2UhYS_yq09lNN8Oym6vEY9JnPNmQq5DTY9NIH80zD5B1H2Gi2aG2bsTCbcTAmlel5Zm9MOcdAWtLhZm5Y_RAIxBVXphJ0rygAT8bdHCbFSKhx6EfZW3nFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu316psgxMzPXXHbOjJ_nUZqXldJUjc5rdwk-zIfBdIx_xX1gikN6JqOlvbHpQL39isp0vnMKEA5hG23WlFP0kRj4YoHhTk82jpvnm-gPaSfZG1duHGgj7fsvMh7JkD6mOT5yLkELqi4RsPHHLu8ULIg_Fkdm2T9UJ0gFCWIhdOB7B18sttj6FTyo1DpdugaHDfR6DpCPKSBe1RDzwQ76cLlwtydmh5y5NpefBVplUKlMS48SnOEELVzXbbh3CENDheEe_0BLlc4cZV_lmKhRdJrqXvfisAQGCgWt_dbnf1TiA3BzUfOaGm_3OakoHgfecfNi6oDJTg3qugeHfns9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJBDvHtpJB6RI4uxo2Z1uITn26Nc14-us7ncDiUno-LcqxUqL-Nu8bHPmBD6CuuWCaAp_5WOiWog7cflAW-TLbK99g3BSctCNb8NK1HgBIXcReMqMRevb-IfFhWq3D-45thPgHYxAWRY7qllE2ywAwqsO3UoBCJuRXaE0WxtrpAv7AbS303SEc2lgpp3H2fjfRAXx3U-PaUq-2obwgyQ5Z9qrN7KiNk3icyHAa8K3gxWgwXYdkWyBF-dDqKJLhUEhwrRFyvM8pI-vIva99oiTjE3KhOgkUjeDNsNEZjRiuaVkY7Px32-c_PRpySET81MBnH6YFomTqip49mx3AdLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppl1MGx1egTuU1no_113O5BtHVjYUtlAbncfOq-98yKirziK4CbWchen3MNACWWFaUfjznUMzS_YSfIp0w4P4kN4NaCJqgf9keKgjhDz3c4hnmYf0e8U5XPd6BWWmPD1DX3PjUmadStyFL8IDMku04F7HKp6jsiDREkIOp5qDhysoJThbjzlAzPdTfHm0Gtd_jTXL4IE1GPzBBDLpI_EbZVmvD1pUC1ogjan4J5g_-gxYkmWhDB81pxzMAZSw-h4SukIsSWUkRnPnMSyer7VX6Jrj7eFjF-afz8bEv7MS69ouq2BBD30vN-yZi6Nynsom-G7W0efj2muF7xEn-zVnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giauUN9wCN0rzUw0LWqqC73DUDXUf7IXurLFF5plcu42Gfs-lW198-foQQAvH-M6N59-fzy7Bzytcwy_LDZmS29DqiIuWMLebnykvd8sqlmoBYfdD8UxtuBE8Gizyy-uEKq3YszTHKy_akj8dl7KA1kGLuoVJwI-tVp13TncF4a9WJXsckvhG1YkyuJsBPoLqJ_NZwt4WPRp4I71Fx7Z0u28_acYjAtqcrVmtZ9ruFEKXGwFs4e7uThzdc8NSWwlOVNaOlFDA2g7rukKsiJmpmQ97Ujr3qE-4-hbLl8o0H-7pMn-DbArhDZNwU3xpkwJF92vxnZhbJw2DCmEtA7imw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZRVhwNGKq_gqrix21qTXihc_Q4YOLZTWD3spJFUsW2HfcTaYRA5Vg8QIqzoKOOsV6UYKdhpuIYd-8F3qWnoJCrnbG7aAWVCHtXSgRXocGEodoffHzVazXlB_29HpcgkoV09fr1GfI_xSJU_6gRIeTMGXqCY_4ALt8GPAguzYqXSP4YXEUlyt2iq02DYdTkn_2sLxGHt_UInVlGaUxpPOeILXDkVY07yF6UYXIiKUjn9A4Us9Nj9sPKDdjevjenGBODLlsme9s_QiRH9u87qz8huSa5VLS4sKnaio3T7ircp4jQNKNVHdevykmLoipOqvE0wJkgmBkGx6btvng0IUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjHWN6hvsmN7yTJEsAA2jEHdcH4Dwvgv-c6_22dz3Au2X5NDAUa2_29XKpN74BcOb1OVRPxWwz0gxg4cMFDUYKi2tLl5JhspdraBYJbpG8_jos5iT8FQf7WsK7PAFgVccXAZ-K_3uHchI_VOs8EMqSGIrwlRCMxv2MaqaXeHfXVC2tzOJZD6PohxHR5pRHubWeIDG61qQw_MaUBJ8bgpFmSt8xQSUDxGxuekdsH-lQzMGkw5ni4g9BUfqEgPlHaZZfra75YKcrVeOxOvachWs_anEEYv1OEg78VOay9HzdcuO1q2IK5MKhACeAqV4lcPA-RB7y46qNBwzNrL8VRtpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQP_07PeVXPtgE53JxxjpHdCGPQnaMeqJOcxDn8-stLif7x2AXq_tSuv-cn3X0zEU2Ez9AUw9n8aq6Vyx0B5bogEFZS9n79NcSdfAPUp9A_dfvt8M6tm8Hz1gBgMMI4T6_1WBrqNK69icv_XiFZtl2p_oGlxMVsOa6UigUOjkpl_KgGYbCTZ1z2CVN1G5ioOp8AcslZGUbLDIg0_k8KoooO3FczboaomR6qK9k7T1SgAviIgdD5L_ZCbBHiAnFpFfw7uODzwOm7yhBA2rNWnEYsVMkl1JwK6U0gbdvTqh4rK3TTL8RW-NP5_v1nZWPTcCoXELuEMzUp3ezID5CCMuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COjK5ydbb7Xg-j5r7oBOmrXppR-PCCu-Eel_ZLQHaZsecWJOIVskPu4afcj-VQxbwzZm3W_dRbAILrVNazFtcrzlDHsb2vx6KSiOriY8EmjqIm0PYS24UwobjHr2o1gBg_ZbEjVU3SMRQ3AP_qylqTERmJJ8Cxe5qf6KmixoFoi5OnXeGIXDJ-KYl5Qu1XA6R9pXYBbERlV4i9YC7Bya2HyarGW0jVcAvHuCVZPFiXilRBVuy9xo1jBUYEsSsQezFH1N6Xl2E_1dbVEvSAZZ_XRhKMNCWinrhaQEbA_8231ePcHMnloJEudqHTQueVaJbcDMbv5G226BMhEmQOmfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwaQu28rz7tZBtu3Zn_crlcD_Cp57EGGOMoE0qpQJJQozwe-hbXkm01DnoCt5itIARhLUrck8BxaQaOhUxxsunjPJ4qJIt6YxAtuINIgfZ1KiTZyGhNQscLIljWAgJ8m7-v_qZxRJUwXmFM2ty_bpk2-jyn6o4LSRmFOnZBdjVNUCNX7e6giUMMiME961_sPCeBAkSjxKBFxrkH_J0k7TvQ62ldwxAp-2eSyNTsqCUOSA8EtFSCOIDIm9VHaERwzYbVtBVF2-Lm6p1vUbFZYkxnDY2iThx9c6NkCU-FFBBr50EeN_-vGh5NGJbViB5BiQ5a332uknku5BPR3OQ_gMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KT-rWY3mxHVopEj4KVf4Diicp3LFmXaaIaMFvlMncuKA1EtbGZqEizDUpsWKVRxOgv_F1yy6rtyJbgXlCjfKcXoDukmO0yWnd8IpUnwzcgRF_Y3-hR7vjRxX23Aucs4dtA-CXJPZakbJljjKz0JZMhTyEbncilTuk9hJVOn-Lauwnugz5RBwmUQvP1xSWiIOx5EkkE7ADk6HC8ZPHVEDaw7ELdUEOipmmgAIArbjSiGkIojuepo2AMzuvywRPVhy_0jMvcDIDDZVzOSrsbH8SbI0nragtJp5KVvQ18Xgv5GN1nnZLsM7Qq0LP28xV6lwZZOOF9SiMwj86FgYn0Ml1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9wJakRxRVxyteZOHH-79-a5iY8_e0t0KzJ-ZjGUi6yzNgfvMHwWK0-9YpT3MCNM0TGDq8_Wi6icmYMq04Ayfzl7IjZlbLrO0jUgHQ4PyEg_jRWMV94srlfS6qa2ewDEGsvGtzQXwWtmAJeIMIw3eqXVjC6my58Vn8tGyQ-zNnoFDMloZLj1lBLy-MSEzJjTQnvyICC5k9T-MJroMpiBEhLrcN9nEZEcn1VSmy_axSAahTWaom2D_-NionHWdejz8JCNeREaMGLhjD1aYho26nu5cuRgGe78WmFxBsfEAlw1KtCauQwrKzdrhwXUaZjDuDPnbOSUMJn5Nm0jEi4Mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAGQ0wsNIAjrXd4s7PtPg-rlFypd6ohNAHp8HsVKd6s6GnX5U3vk27gmni47rZg2OIBssStmWvF-nFj9Q8CVPKWKr1geSYbRmzMDESCbIPY4TWM8d-d965JU3ofmPnshmRoaVeSZIbCTx8fAtpYw33rc3AOzsq6rqIOanjMIoggaOMsAuSDvrRFggZ6q5IOxwYpiBmqzrcCCcAdPPY7hPlmHnBo6Zx8hLq4sYumdERmhdHmc222i_0NlprvnUV8E4zHolgrJ7l1F30Arqx_9EVB4xAUZMGmn1Xu8aWajyFoyni5fBThtseMI1km2yZXkkuAYEcWImKyHvf8Xo7pL9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtK3CMSolCMcGA2bwCrLjmcw8wNQ6zuPDmEJvKAZR6fyN24nWKceBWePT7z8Dta0iHhD6qwhqDltKoK1RQOJ9-RDeCdKmEhjojl7zwXaBVSLVsk1mgBnG52ra3TNZLeW_IB4HSnsapyyNcu5L7rMjk1dEmFovYRbkjHFRw92IFbSzlo5L0FmsHS3tTn6IuaLk0Bjt5j1EogGZQu3dc-xe0Zzx2m9QPBcapCLiFdkmnGoFIetV9c43EFdywE9tFlkXIXIcV3qktjNKOClDbkl_EeysBUbTTABUXTCrC9px1xTtY5EbGosQMH4Sp_rETaNkO_00xkGPsGTlUqfbp5xnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb3gXzYdB9pPNp4gKq8ZGn-2NTzZ9mqr9ykktEg8fgxluw-r05v135gKXwdw6cy9YClzlXE06iI8_LcThsXNYrhGmn2FzLVQO7M5tokHzb8I_QlEJdHUEQCxIl8bEtGckNTPkrW4bLv1ZEECTPBvxwUaVs2IxBUA2DjcZ9hUnr6jxTU7TLeO4TCV44A39vDOjS_nDzr9Bf2mexXSxe9AWCEe7DErZahgmQU-mzyPVJeRAaZLRLEKdPKZ_UmCga5I7vrdo-kwaflgt4ly114UJ1JdOHbYGFCdV5qgXwxeZGp9nVYxU2-t-aglz8e6f8xiPq3rNYUy1nB_KnaRe2YHZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 589 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvYVIRAgkIZOcVF2jtWcuU4hOk_JbKFp1mFalbH2Ta0P8g4FNFkumoJgjWpGxGjAs8DBy2FSswlN5HgTr89B_bLwN4JbxjMkC2y07hhnlIC9i4tA1NE27WuStFq_WgZ31gdvfYCkPNcIhncXKsTaXgfBBQsKkNUER5A_5WT_SyqnEE28IQ9sqNcy6af1nmZUzgMoNNUUV3hizaCQj1KQAeoBeWHCBBD-jjgjlZF63zebB6l5dQauWB69b7MPGG0V_0reZG_xGt3wVOU2Yz-bLkzJHJgR-7nurrvjAZJV6cof6WUtw6PkfDe01ZvOA-Uh2wTC2n4LzA6BXEM-k8xKTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmUAJcVD33QeNZBGiN1HAgwGXZvJpHTRqvXDOoaBKC9MAfPX_l_fty43QNeXb-ymYKq2bvl9b6Nxp7YqxMBw8-iEDBpUnXAYYbz3cDsl-8n02HRJsAseoohUDhDrrCIVSA9rJRON90GCwerWb3k3IcDgsZlMgqP90Nfq71NvV19N4Vyl6vY3xRqJvEyQ50BfAstfwYu0fukH66o3JBWthsAAtK2t4mBQexgEyoU2DpzeCJMteG5eeWLRpfRBH8cXWK7t8sfsNLoXNyMH0Jlaf6nBueScrGPz5cTPMRYOQDFANSeTVymJWO3L_9fP5Hj77UrrTVh9fmI7dOGvVnpHZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 644 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hign2KD0qZWuqp41zfF4V_wi23Gsjt-JMyHOGIFnNj8ntAaMkfycdxTp2XjM_0R3zhquXDH-7tqmyXQw5L7UAuXDEvgelMcbADYIq4TeU_uZC008GmH1S3Ct1V3hWZ9aUOVV-yIj1Dswlm1MAhIZSTtij4OC8Z1Squnh4HYFta2XIzIe8iMQGZRz2rlBIAW-lkudVNKZ5ruTEP73nazqGqtY4wOOLmFkxYVJhJu--VKE90kJkYR7NzkxxT0c0ApeGdVmfmkUyG0z3tgYJFUc3f_ItjiK6SzQ8TiibjJvcGpAQZRiB9mYyZvRxoC6NQ_MdwMWFRFt_815Fcc93pCE0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnalsT1QcnsrC0G4TSxWc6gijF_LNcTjMFDtFarl4qk098zE-qS_kDguQ9rX8qgaHI35fgB0EQhaEWmEJPFQNYXB40eU1yrefpiBRiKktMCgKDEhLHJ7IwhLrdvl6y7qDmCnYHAzIuI3v8WefC5nvqXjaiVgBthfcHyZjn2UabLqMwT4xj79mihgRmNPWFeshkbJa8YHD5N3kSq3XPMRU33-kV7BMhw0cBUdvFw6mTOh8B6sqMFW44ba3hHDtgK3oe60S2SQ9FI1mGiVGipyqwPMJq_wuwhw79gULBiKQrZsGDley2v2TwS--_daxshZAfZ1oFC-ZBCNaeh5lTu-YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXejwG2bLweuSDw6ajdzPvBoFXiPb0LpU4hl_cLcpL2cw0TScMxLfePI4F8lqEeAOQl-DnObBgq8BbhNahnXSvUaCPNSZzF5BXML1BQAAblMGjwYVtZ7Tgi61Nt8vF0Ep3hU012bI3aZNLmqgIaJTrcMvSMPMs9uaBWRxGQedNN9sI7NG682HPyN1wrglzJAIOL1PPkSG5xC368oK9t1_cy5oSGUXckFv5fITnvzTrC1ib3t69YlnD4yz4SwDPmotJ3j20CygQjrl8wt4HR6Zf7dlLYU63QpxXPiwMdNCCywGqCZ96E-Qvp3CoZkUTo97d93o3Avwyw4Q90m0iQ8Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muAj1tUC1VEOfcdHmJYAneOykaKmuCDQATJlJk5gGLG53LtGDTZH778IcwxBSdehTT9_xbo-RZNVs5BCuo4sQyW66roFOWZQQctdSp-QtRdqSFCFpSHB-2urdUaoNbC7iaxICZFMUTcOtkdA9iT5OLNEkEtXHC7cFy01N0mYhJpjugL2_DFlYM_Lfz7AAcYCzZHVNIFsG5iTnhUhtwsyxfcy98nBmseWYkoH9g-Z6fbqfEWkcegzRJOdAU_iyqKRCXujkArEAi_6VBJfiRaswp8hpre1E-b4HgwSXPMqDtDjp7TKHlDyPYNRMIESESETWsOJ7R8jj_UHX-jAVXXaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g45Qxtqp9xlo9CnCChGhUIragJavCiHPO8Ko1PjNfXeLRQjhb5JEZWxBS1CYaE06fg6f5OKdp58NY90Pe9A3_XEiHKDUAaZlnhgEPhuwUgU2aPyPaq3Iei3NOTiKNoCPJR930otuTz9oejd54z7AAptezpr5rAl2R1gTcuNpAbUP9JcMyydpmEOBlWciz8hnZIujrCWJRpUhGHUQpWngiGUu8KEIt8VUqlrUUA63IJlr3zXYyK7mg0douOaLQUoC8vnkYM1U7z4reOmiLjywjEEorMLBfI4_KA96s5KOSPbB9Zae366nktOXpocZiSvx6-M1fn_ycAMzpBpv36dVxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjefxbcmr3lVOwyX6U4GST57icjvgEl1KkKI273SThMvEeiIPuNeEMw1V49RLhL3qUiCfJjUJuzkzCtkZVWpC2B6h5nmTZOJWDu7x9prwdwrqLJuDKMeoCvBgMTTzaLALreQfX-if06x59irstCdZP6zh2yn1u2cb6GcVYB98S4M6Os1NUqSLZn5d99KDiTvlbC40CbDRzuFflrZ6bdIHXAtnCwJ0t6RIjvVDYrxhWnmwNux67jinXRPfImMzD6OEypTisABtGppmcsYru5NGDvzr_MGnJu8j4CjO9r2Bb9P8ubWNNjKdtjTtIuK4EFvEbLLjTykWB_-mpsb2s_KPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3kX7chOWRpDSyvUPKyBjtMlqzWRip1ClNghJvjsAoJL5EGkUeQ6diEBxfnw1XvVqnlHlwhGFY2AhcWrWpa05CCH4F6yVOIpDkzbb4AkXrYexoVR29WJCQAn76gUzBP8ubUf9_ov3qKJT3UTwa0b1AUrqeI9sxziE0crV4cykflppkPQD47dtziZIodnxfAk-1yEJKj7yU6dTcR0eNDoePt7iZ0xkNnoYkyKyOukQrw7G47Ib7JszYjbjePbJbHi-YYJ6oPNju8O1bLUP6GZq6KVcrjiXJYI8Yuoa_1lx5Vl1X95-fmg_FpXlAFInnqe3UaWyJUJ_jFu0KN95Q6-KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4AivKxfH8qHX5B6s0xQhELQy7W8EPLLkzfU723GMIBj6ZAKe0bDIX9YtSbGsBInQ1GNAmwZggpDH7i-URxLQdj42dY_8OuqXCVt6yjY4hmlaBdLLN-XtbLtd_oi9x1fkakzQka839hi2KrfMWzhKCmKNxOjJZnsvylx1uShBidhr8bki_oCpXONp4bEmkX72xEbHE7mdaISjJxmPS57ix6lpXdEQu-BudQMje04bNJZ33X4dZ0iopmCf67ZEsk-sACXmTiG9Y7GK19YSpEZIQcSIpFPqAGT6J7OAncUzl7AT3U0Hx9DQgKtdb2x0NWsA1lYpQmcTNVZPoRoLRWA1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSUEeq5rV3MPKvjtjyb7qFD8rQK3aY33LyaLd9vlG3DEr0LeG7FIP_Skp4dwBjXiFJKpLdQGoxemtuCSWo4XMA46lQgzcyKtJfXGDiI7t5T44kDEfT5UWcji_818YnkJV422gOszuNIlgSYjEWvFVGSfnqeW7TWIxWpUqN16sVm4kEJwBVTPV2pYMgoPZNUSGE2g5SHpQWrpOTQ0r6mJDGuL5ZyPuQpmz_zaRhKxIKrNGAGZzUnD_rd7Sz-HejwLAcQsnpK_mPY8dUqIVuJ4Mmuj2957C87amLDUeUZXdT8QPfg6PiuL7oTptOcmS5DvZGex0T_BSJC-vuYiitIDlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLhyCqHQPOwO4oCb-t9a47yfeC9quvSx2a6fxdW1_JJdm7zl9zaZgmLAZ_FAcCg95RRo63xOKy3Bm4V6AF-YCQzqBhu44YWxdocfx6PL_cemE6hsRRAG1ufTB5BXCSERebZTlPPLYZi8vMxA1Bb-OMibtZwcDplycKQHFbDYgGFsxbKTs-ZrAXfnY__YUo3Vjml2JhTHpWdDzBmulv8xLcnT_cAhidHKTSqY-l33f2VWvVV3yyA5WRL-H6-KtFBtIc-mPYj0xJ7wvTQaAwCN03I-dtH-AKsdohM5SFnJPULHktRcbByLXy7oiEy234zjtWtygcBkRR_e3Sidqes4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8CcHeNsmFeOc1H_WlM1HYpHvvviBZNBCubMZ5xAdlFYqouHJioqO7vmQkQz2VWlNdtVUhSIYixR0oyv58TLLgEEyf0B-FOPoHQ-NtjZ5YsO3t6RCn6XV_3SJBsn0Ufl1ZvSDynNQ-fRJ6PmwGy5oHE3N1WAFs9NqQH4rwGQasZ3apaN1-jM-dUUCvMLR7prpDLRVJbAUhZBzpqQ2D2rjPmc9hqufzJf99BSaN6Zfudp_Ffk9SSHJQ-mV2jM_FYzfJFPlHEIWVJtIYzfmgf9qsBqoIg9uwBrUJxeqFQesvoMjoSwca8ztvnsgJIDJ7yeSn_9L3EiI5pD-GboK6ppog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5S-tOTOl1Y3_09ohssRbqcxVAlVObOhboiNHMvoBxSNdZfsgwGEPQAaWFBdngDDEkeHbYCz4qZ_zLfO0F-rDC3XC9S1uzwKSnESSfIDaGUluZphJYa3hxQHKfV1FubeOpXdBzbALqlIj_JGLcANi-DSWSfKbpdz_fGNNNzi3E0PduEhvKcZnbNtlUE3-yKxlvXFGDpDVuQf4PvjJ0dHzIFFTWFBDV3BP2JwVrvusPw6-RRdqfiCkumrVh3gx_bMNitodXp_PKerahXbhrCzOeds7sgH0drHix8w5AbUBWbROnPy6zUF9HXmcggLlx4LNJUf4FgWCAOFk-_Jc_b_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIuiBVP4hM6hp2Y8pYqmLYlbGxRNz076ySyAXtKl0VOIcthvJ3QACcA8Zkms0KDthKVkpGRZVtkiUGUTnQsQVSaPCsjV12pePpj1H4LW_VViSwpm24_M-mW-04PB1XbySwc0epqJuxaElAaAyxwj58Rcx6CXGGm6_9_Q2EdNYyWW1lcYcTnwqiQDtfj-xyBSG199kXNUWEwyRelBAA9MNb5QCu1xo7aFdnfxVnUIL-AjSnArwWza2C9j-0OgaKihUcFmr9odmpgy1QebL12aMpbEt0nYtxJHYwdEIHSF3Uz9FD89SEVrQVLM3BmdsbnthrJcVnyn-6FCaoNlunB_GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR_oqm1n8RCYKrroVqtASe-dofvRUCAdaZETJDj5Fo9azgHaW-y2RKQ_grAEaDYUljQcJZukRfuMuo4jqL5V0ittI3K3aZTjy8YQkgTX1LBY03qzz__xfIpYQshYZRr-oKohcFCAIUpvoiX0Tj2n-hx8I_J_YVp00n7G-RfgfZrpPyilAmQPpvJ42KwF7BnSfzg4fBK9UCaUXkB-eOXJUS_qIFLid7EICeim7T6YQ26ZaDB1iR2m-9PejwVwc84JnYz1iK5MiOnm18PGnl0Fy7fzer8UjcWmKx9BJb8DUBM_GepWTeNMWpDXq1PVcFiOE31NEKU_K3cL81vfmhlVBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1V-48UTeWu-KrH8mvdhKoWZ4lrsO6val8aFY60e0fgu_UBdr2W4M3U893iqSoU0xvJfAKHOu-x2DGZfkUpKihJHXt32viHPKqtbeCafGBKP2yN7NDlQQQLmo80JsRmzV7-vrdcv5poaJHDZcCITT27dV3EKrJOvPJbg7yooarl4D9V8eN5SQXTV9p_wM6sM3HSc6627TF_klnc0VjeOIyYKHPfIS4xVZHuPrZNSDd3ZRdSdHYceO5ylkR7aG9M_2mZCMAGzlff9fz32Y6HmmwXmremcmkYWsNpEpFbj0J0YKgiNW_DX9I7dlPK3r3wYgk9j1eocuLGC3AQhEQGTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz2jcu8LepsRi8ATRAGJ49NrtTiRGN667AqaMJi58RT4LcswMcFq3ODrvdpOf6U_aVSZJPFnqE7EargS3Co7RPkTpMgMdvWTvwflo_0U2pf-Rbv-pnBjAmPfbWfg73baLO7JSFhxM5Agw-OQ9s9DjhnU5KS_2yWY5NVIgll0vxzLuRWoISapKRLlTm9QO9Y89agTOragsoqmDMLGj5XtoBfzPzsWNFgEmN0xTKrGnTXNogThcsekksE3dDA-l07TuglZwr9pznjxyzrq9AP40VSpI0cT4MRHla7pi5_78akbrYPxo4RJl3Wktld5MperCBZ6lM44Q-ERZi6h02d8jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOfpj2EU5X52VYdM080LOgbBrtpIjVW_yiQedL9Q7iITSj9k-faH1-7bVev2HYPjP-zWHIxQIE6hCVs75kGWKjJTHzzxuCf9O3_-aLLxpKmZdbMRqfHL-SO_lQAPTYFxwHr8jtFY9hWSz-GZSLbR2iB3qe4XMNy00G6_blDXULIskRVas1i3aPz8oiUxhgBNPCRrdOXSKgHOj7bXPfJUbJopEQ2RImyb8FMVFcuiCjwG-ie-k0iivz0zJEJ0eDdESKCkmCIYdOCfwtY3buJcFLH738YoIJAvFQzNiCxxvbgKzpZxKcNP0vmbypnOHBOof84l4IaFJWsNIKqgVsIW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsJDHsd_mAGuXkblEcFVbnC9_Ia10P7WLFep2BEacIUAsqa807zQgZdm4sx24qmbFBJ8r3z6YrKsGD8K_JdySDuMxd9oaUb6Xr00JX310KyXg7W27vFYXz52WS2kH_ufUFBapPnDZwdNS6ajBdivXQsFzp26_3pHU-aZM--eNAGQGjGa2kMeEdYXBT7lzQmC6iRcMf3HjUgexVYkO6W_MFxhMxRcY8UpOai4n8VmCcKsDGu3achAOhaLwsZBc5zRbRxsav5__BtDIwadwJreCP091x0JrNG6pc881FhW2WfHuaxySN9lPJoy3quypQoFNS_h117IhCdHJkpVCGqCzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8cMrgUQ22VuZta8mB8FkzX3Eiyqqir1rQSxskv10l2WCHiRJT45edA3rAc_o_cgsJt5FpOa_Q5xyteB-Jx3olHa-npK6g-YcR7gSViPOL3RIHS8h4debXHw89x7QAvUpsDm6nbIOdDQOdTDpCPpztR-tr32e_nivrPjW8tz0JJ9c9AHO0oAAqsy_Bq2bs53piZOa5xQ2MzqzHZoaB8BVTg8APyDKF7NxHV5CtWry2ILhqRgDWmkf6RDM09mKyZ3xnqh_kfA-CyrUv-3S3Uomnx8JhPNRvdEQpURY8RHWGbK9yWnqUOHdjyYn7GOmU43NspLQPySU9909fCG-1eRNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoH1IyOCmK-vJjoPJg39SiwIXk7CGQAYvFVktx49vJiWaeKktE1XAKVPvcvdSduowqitxezE-f9wgXsunxzNLqYZBvf0WF7lFY-EFuWC4QXLhf6UYxqzSvlyniX3eY0m1vog39JdszhQHr8mB6UW3Pkc0htFPIrijEBqi6cTD_8W6hu7JX6DKGL4ASjkZmUygQqFg7s7hbcKXH7npHMX8Yhd6STxiEGwfw4Wp0oUt46YU6evJdtVjEHLi_TEN-TBMBNQxpDmxB2euVnxiV5eZ2j-iS04BCHZR_LY1aLj5kKaVIlJQXXwSb3tIOw_WUeNWUESTYHxedK10wzA6kNfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiuMsBGP7s3cOnn0h61cRq0-ms3wCC3UST0AingyoM0fy3bwr_uAgsw2ZOogQF9YZgn6dXBEkuy2gMCOOKFGvHSYNRCYzOOIMIgP25GLLMWz0_CM2oaTBBMsLZbwsolk4TrwGVvs7UNPFl2V0_t31pj0Nn4kl3CqzDJ_oxtFBWxWk3d2_lhX0HpXYZNg6MI1SwJQdrwCJgjQ7UIldXlVCxqmHk2PsTAQ9lYf70uICJvzwArD_NrUBgqehrZFRpaBfwSWLYiaAT8bDfVlpdLZyJViXwDP4Ia6psA5mNPoUnpQ_mrkl60JTQCWTSgdn5kJ9ARIVZCXm772NQZbmj5apQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPh7QEi3KRS12RazQYEUBBrl78FGIvAa1r8B2Nle3h1qVk_T8bD0o3GLUVllrlA_joYcUru4t4NZ3kTYmTtOJiRUoxN9dT3n2aAM_WsCpbzWN_UWtnpj9aYybju1L1yxKnXIRhuJf5k3gDfaQ-likdf_5EP2yU0GsrRyuFD0QkUeBcq9whuG4qbhdRxwjwbfbb1qu2qC5ROKeoWog5BaGPp6JSVRkmSRSyK8cwQsyHCbfBS5_zbVcS8skpNc__CQVay7NaK6kad4atpsQxU6p61lcDkFp3UEPgXuzIl5n-kaETjhTuHjoF56z9K7Pe9uub2ko6F7s6iwr08xKUVjbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQD9uGgp6kF9xl3feYrDTWk3pygSVvk7iSEWmMSEHLFyvY0W81tLeAhxGweP_gv5Jigu1Bwu-ZHdi5BN4SRe31h_PDiBpxlCoDH1t0BNM_8AbOhGUnnbMolrCvZoLJ7Q2Ax7WDSIBCaCYfjS3ncfV4Xy5CAGPd7l3xy6WQfQ4AR9Hdang-pdQrR5dybWxPTpBBh7EJ_dMjrkDg6MKdA0GIwWRH4iFyVNPLB-FpbEHO3756wRMmJs02Mo_bNWSmv86XMg_bPj43GJze_elCVKErGLx4cMiF1vimRKv6JUByLQUwgcpoO41YobB8KDJ7OnnWWa3M5YJjerI9zqJjkP2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyAgQb47-lG0V-FjI8wK2WO4IBZzpQ_3m7yiFVMgsR9GvDrdBlz4bxN5GYKYl6En7ME_pgIVb7shd9J6j8emJ1sO2sPnDMAZQhDd4VsDAmZ9f7TigaedQWJN9T-lJVEZzzT_HsvX5i2SN1VESlAlch7ClgVCh7RIBMC65iNlOECKo9m3cAFkVSmzvM66E4gegNh1Ic5gd7fqxcNW2t0tROrcjBo8CUbSy-nLuPyvkJmfbd6hUFXPcp3NcGvQMrQcIddJsLjor-BfhsyyrqsX21vBbQRBTbLP8nj8OmoKNb4NpDZlGKpOx_XnGN6Dd-6N4A6UdxfCfEGGVBUPrER5DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIpj9pKKt35Rc0B-lGp8GzmurUPnNQJ2fLdBTzf_2xKb-T86A267pz01qNhlv0_lmfAWIzWKZ_XrdmvPhrirt-HnxvrPmCRo6ptk_6wfK8-B5MhvhKR4-nOYhxdsYl14Ym9_2ak01XhepmbqnGfm8HuPiM8A45B2GQrT31rvsQP1ATMXSM6ojISoMBbIHsXsroyC6ezHKPzHUW9GL0lJGAuEQSP7ZTjw0tRps_sqAf-vQhrb7eluwl5sK8X3w414kPFqln0gYLRP0GIxw-JU35Pw7NNMjaCkbgDN0c4bOGikfaxBBq-3UvLUTTfbsuYb5zBOVc_Vqcp9LX-i5MwJ0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=YG-XTVJBpCUKlxgnj021eFPFdzqQe2hyRZqy-sP9yDUTkcVCK-o7Ch62ZocG-IC6YqA1YpIZhLnUZD6RN__UxBpNZM1Q1_e9wzqykd7ZQfEx_HU2faI1u6OjFkN9M_HzsM10G2K_ZFYhaMQDeS-LvXP_6Tse_jb5T7CsleyOKDGDQuyTj-G2vUw9Gd1x3rRP1Jw8BqWqHOJ7fs9o8TV_E6X87gZNIywcJDmVxnTQTYxGxHVSxeVnma_ecYP4_R2vY-069kLegGvo2IpRDGfguB_AQEmAdJg9Xu55UQ7GmW88fYJ_u0gjxFyPA0JpAiASs2bXbY9Wf2ng0B3uf86SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=YG-XTVJBpCUKlxgnj021eFPFdzqQe2hyRZqy-sP9yDUTkcVCK-o7Ch62ZocG-IC6YqA1YpIZhLnUZD6RN__UxBpNZM1Q1_e9wzqykd7ZQfEx_HU2faI1u6OjFkN9M_HzsM10G2K_ZFYhaMQDeS-LvXP_6Tse_jb5T7CsleyOKDGDQuyTj-G2vUw9Gd1x3rRP1Jw8BqWqHOJ7fs9o8TV_E6X87gZNIywcJDmVxnTQTYxGxHVSxeVnma_ecYP4_R2vY-069kLegGvo2IpRDGfguB_AQEmAdJg9Xu55UQ7GmW88fYJ_u0gjxFyPA0JpAiASs2bXbY9Wf2ng0B3uf86SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0NFFuFsR7fN33lPvzl3V5-M6Q-WIJNKXE_P0rHsJjZpbOmWDwwHX8U0Feo9TAFJ9cqN10nQjOn5meNQSXoAgwdoAG8A6C0k0IHFWliWbNgL8EkiWKtKXYI0vfVPFeCZ5nw4NA28lxustTukBndhP1LNTWf94Lp1WTx_hyxDI85BGpZo8eQAiMHGthXnFW-G6wn5ni7DkRX9L4ZcqyPklZlJIn1VAuE5Cu5p_DvNCM9CeXyXjVBhM6lsZerxhg5O7S8tikF7lb3bf986I4CJcqU68XiSKh5x7j--rHf15zDBDG4j9IYLGeAJCl0seIFDJYvih036P-XSbWuhW3mWOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/are1uMjnwMBfcTJaTLgJGGK9aDPleuveG4upmnN0AUW24fs1CFTKgu51vck5l5F-DE_T5Km15Dbhd95fC1kYltJUhTaNkHSMOySV03vt-ZFOozdASxIbS2j69Gn2dehcPSuySVbSeOUdcy_rbLSqnwIvQDVFwyfs7UwIrqrhR5p6ZRbs4IjIHYjRn4BF8BumNJYF4BPNbkAsdkwjyj8Sc29RhI92C5Iwz31ofOozp-LqFF6x8hz9dz_FdhxbRvawBMpphjoR7Vkw0iDy5UMYyRy4OiAGSvCT6Dl1Sl5UTVftYc6gKGcknqbZw9i6pZCZjx18rsW1_zcWhY6GMEXHmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EgEB7K7dZhPqyM4017B757pYtappXEoo60A9uz4K8JfqiDazQlavoGuPjwsZa56FSmxZ8KVXIjJMlduZ4yEDYV70eHtPVo6vGZ_JuaqPBMVkf01S6OjzO7DrZ1j2GOOkvvA7Y6UVDaZ-fb_bfFyp0Kdjt9DLgl78fM0cDeCVGG-TgjmzopBlnqPl1G7BXZ7gTo36RzdTaaM8NTPA4jdWE8nVFXMk5a06uL-vmKIXK1KkbrqP7lXxaojY_WUleBrJEDLfm2xk2cozMNoJv1K0Vn_FnxYOJKWp9lbtpuHXDKPmWStT1VNYrkFiXYMhonzX0ZJapeTc3mOlGA8uZGxGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VL0nZe8EeoIuh9a8WfjU2wN_0Y-0ZCEzgCuVJhD-Ai6YIclm6IsB7ltxaG5EE9UyLeRyE-04dIG6vnaD41xlZawRXYRfq6-1msep5FxFonUPHmpI1K9GGhpGCPihbEQFXT-CosCRbjGEZvT_Qb7jcPjzxljH4RdnJXPWFWMT7mmgP0o6OO7waD9y1WXVF-lilPUtPjRKpeE_teBMymptkBWlsVg2DnIov_YH0VCUfR_OPQn0-zUAOf8yddPAD_PDFdcAuTjDCg3EicBWvTOedVLZfXS0jdPIZG3E764UoUgh3imts9BKxwNYg37fdnLJ6XFvOl9oHUIfWkeJnwxiLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zcnw1kblvomqd-4sLP-ZA-iJE-CxxAAU1gvoJkG1wWbKfi6UrDquyNj-HP7S4ZJujdxWttfAgdZOatsorYfQYlhjjG6ZToAqALDu3MEsiz1Z01jrsFzDmK8yCdPn5Ko9SG5P2rgbvYguyPrFfurVsgJtt0Gd6W7lBL96ow5HNhYqeZjn2xL4Pk59wMibTgV3lvwG4ZVNb_EOuHh-Gyjl2JEheM9wruFYTmKbWaaD9MMupn1w0R8Ow4geN3U1fLyii8V9hBsXkMZNrq_0oEqV9AHvM7ZjHVyNNlRMErbH4oZxTon7plA9AOdFnOLrMu3QccUBcBcBZBfyTQVaeIEKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdOohgjZXdb3LurIF2KrugB3KkPZFOCss9pHeoRasxmGWKIe13iqxPJgHW0EBwydHWvfPG3pYINppZ9Z7fElWyCVpIu8MbkbvxsmBhVPCvughb4rZN2AHceC3khxP8sfkybHqCXCjhXuzQ0vEqUouj4ZWwiEFv1S957mphFuBEC-Pqskq7v_Nqg_v-fRA_QQzv08PZP07FpDRr6OZgPSC0-lHxb7Eel2GmiVxfP4O7Hcu0fFnOT5hT02966CVtVN9ccfMrPH4LD6ahU0TrFISu9i-JikaRJGeQu7nEvK9VGe53ct_SUvNMPc0NpYE_zv7VYDw6tbh_3bDsS6ytzmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3RNMnnIuXfMTvQjqcD7klFcWROtC8BAPxqWGCRW0dGS0p1E7sD03XvGlViUMxlEECp6h-G6ow7OeZP4VIKH-1_IoZX87SyPF3Xvk6QOnyYfAUN-6VUdrWphjtSAZJkuWkZ837soWc_4vPyrY7NZcD-d95RNdMxvI7bV-kV-jlTgqbipGM2uorFfn3V8sfmh-NOUiFLnRm7ctR7sfwrFbGsIdS0s0kIKP3WCh5eizWd-8gmdiW1BXWNihnU_lxNCVms1KIUDihu_QEUPuaBMKnBoEv7L4AVDVk6K0lz60hvx_h2UnQ0-oG04S08HomhKACeNAwK-OZyfd0szhsXFFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=msaidzKBKp8nU5IQZuimSff4-oTQXC37tLgqWIMCKojtI0thrlFcPmH_tUT3PXdnT2Ly1oGOhbqJ6xHGD9gKiCktWP-pJoOi5pysgGwe2dDFj3nA_2vEEDYua0nTydZqwah2wNJugQjkZ9w9X4JuDpeu6K59DuwLBJ9hKwPTA76tu0COjM_24UMO7ajKoU4BwSfQ-orS4-6twGd57K9t8zLE-6xhh9ucf2geB_5bbJsVBDfyRLV76DISxVdrZOhF-qBjc42JeMcj_GPStGANVGzDxFPOUzWoR4R68561xSStWdmwD7TooHMnEIH_SLJscNoVYV1cezYpyes52nIqGmUKtO2nMa18DaB0Fssxx3U5kwl3ALN6tmDyRv1UuohFhxX9cxgqmtcougYonwLRFtmtRGOhX4BVD2q32IIGo2fzdAVIm_1Kn0_7qeT5gGaeEN3FijYRqazyylqKKhXWptckhzN8LOFfYdKmmkUrVp20UyfiycbZzrTPKRRN63nyp4Mw-c_ISnJsiw2-4aEZH-iX45-iGHqkzLMWpLr03VQpruhAgPd-Nn_e1lsMcJAGhODljzlMULUyUH4LsrA8S-3odUvRvOlfpIfImbcmkKEmGvLyaQSBR5U-eXmhwvnmPDp3Nfk3t3_kTu2es_dFpchjP4uIwBTyaZ0LfzCc_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=msaidzKBKp8nU5IQZuimSff4-oTQXC37tLgqWIMCKojtI0thrlFcPmH_tUT3PXdnT2Ly1oGOhbqJ6xHGD9gKiCktWP-pJoOi5pysgGwe2dDFj3nA_2vEEDYua0nTydZqwah2wNJugQjkZ9w9X4JuDpeu6K59DuwLBJ9hKwPTA76tu0COjM_24UMO7ajKoU4BwSfQ-orS4-6twGd57K9t8zLE-6xhh9ucf2geB_5bbJsVBDfyRLV76DISxVdrZOhF-qBjc42JeMcj_GPStGANVGzDxFPOUzWoR4R68561xSStWdmwD7TooHMnEIH_SLJscNoVYV1cezYpyes52nIqGmUKtO2nMa18DaB0Fssxx3U5kwl3ALN6tmDyRv1UuohFhxX9cxgqmtcougYonwLRFtmtRGOhX4BVD2q32IIGo2fzdAVIm_1Kn0_7qeT5gGaeEN3FijYRqazyylqKKhXWptckhzN8LOFfYdKmmkUrVp20UyfiycbZzrTPKRRN63nyp4Mw-c_ISnJsiw2-4aEZH-iX45-iGHqkzLMWpLr03VQpruhAgPd-Nn_e1lsMcJAGhODljzlMULUyUH4LsrA8S-3odUvRvOlfpIfImbcmkKEmGvLyaQSBR5U-eXmhwvnmPDp3Nfk3t3_kTu2es_dFpchjP4uIwBTyaZ0LfzCc_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TselRnv4-c1pmuyWBa3Y1Z5IMI_G9Mdfidj7JzsVGgzfh9vODIgFxZuZDEN8X1st39oIAnq4tOslHFQGcsLlSC0bVkDIos05OJ9YuII4QaQz-S1GGi32-nlz20Uox-sGEWb_km8xBt4LCW_k1HlW7zraptso1WcxRDjZkWzP2rbA20DOS1ThK8lEdq_b8yj75luiutD8yJjGpynDUv0qaktwyib6mZ8PKwx1mQP3WnZLevuGk005xQ96BV-BAlSAji2GSp0_zlveUwqn9cXEesZFRlM5BmSY8LmmOsEol_r3cjoAMAm4ytGu23K2He3lpaQ3bJRJYYAGe_y_4qTP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sxi_JCPrMCcKJ296C_deOnbX_ZMPYuL9Z11wbrYyYjI_sA6DLLPTNGXVhl86gKPhSgF4IQll8R2b6llCkGM5olIdFxKXe8tdT9RC2C4wYmLNGVoyq4zTc4o7rlhR3AinDU0xqGCAOERkadQLhS9yLhqT1m6nYV8bShfgAhKEtRBe1da0XoAEdOP8iSOZFrIrmjRPjGWm-cxywS2c3TAy6ZLFvvsOkPxKdqYdKHaf1QwR4CzUcQyHurJkw2BQEaNNDd52LPGnO_F0dzz6XycDeqgL4pY9XaRvJUKkOVrsllgyKjsP3ON923O19cCnRvkc95l6e_6z5ovFCo0X4QYYng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR8FS-Apbxf0Jxl37dP0mhGDyC1mUGevkgbm8t8f-d1xdjXjbAPSI9kY7-rzSjS9OKelCgS64C9cbbLMqpr4_W_I7ALq0EUX6NJ9PQfkAXY5DfByJsQJ3hnJ2w4nVHE1r5RnwAzSHAih5QaL8GdRPwEtgK6Xu78pjOad_rf60sI2pbwyUFDOfJnOoJxjpD5NuiPzaF7Il7of4RGkXqVqIyeru3xli68uP_Kp0TH025_vKQ37nNSay0AtoZ8iMHwEdzX5HI5SBk3tW_tsSEzXqMyUDTfaF9QHj_eRHJCaRkPEzx9HwpwO6_bBY4WUQlglRhg-pr84syop2-SKm2UOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSYTzlmc-c9LfDmSSHQSP0FzUUKwx9tosRNna6Ku98EHSh_lxoozrJq18bO3M_fl0MoVVHJiz3Gphboj946jQ6nXlR_3JuVnj1UCXuYF9mw4yvSFPIPNK_srkQBmOhi4Ty4DszqeDCXBrKJIefpYek1wL9oh6mTFfD5NZWMmo23nuQIN5OxzftBGe7X5R-7yNaUVtpuvnAMgKAOGOpdyhltKMVNJs21CYjw9JAR1yafwDonlhuXaUHq1vXjsBDAA8PmP_fwgbnHr9P-1aH64xzWTrVCuHHxSPJNAOXi1fLaVk9iAr6pWMAPrx4rrBM8KnxpZ0C6b_92xXTet4O0VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aopQCg1XeBhy8U2iw6SepNq95hbiXxrg2f_ALejmH36J2VugcZy_epwV4m0nHtaQyovWUEx6xHNtM-vS2f0nIAKzPdryVNh7pJnJa1FsAUG9oYV6ERvEgDgIKgWv_IiJuSnZf44vnvVPAupYpQwWYtfeLctM5pOJxvsVwrJ5qC3Creif5xlF8aSHyMxi-n7Sp8Hl1yVZL5a_bA2FVPCnratTuY8nQPEt_GpsApsQDrUIFMKqxeH5DuV8rFhJAq4Jzlk178Eejb6gtdka0JqSjpOOLWT8pvpxlgJu36Zc7NXZk1gqFz8PtnSyvHH3_lXZ9fS2ZfTylDZDPl3xRR5leA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUbsy_R4mMMkSM7jWYKfLBB6UsdM_LrWc_YBEBcnuYtSCJg-wpUAAKw2V5-zjtAHtqTa_ZEPWSQryGrHaKQbo9KIOT26_jWt2nUNtJnUrHBBS6woyOphCSya0DuiNc-n4f4oX4OGj-V8YxopCV7Qn1Q7HnHfaofu6CNOqcXR2ATVrMvfUIFyziTgzeGALknIZzywQBEkf5pIHcHWqr1XOkMT0dCpLJ-E2sxIy0j2WRYpGFdT2y6zVArOJZi8qHoUL5CCMl8PPilBaWb7YeQyUoQi69xs7S1a03lDbgvb7XOsy3K2b9pC5wIXYSbcll0uLOLscabayq1rxBDUe-eUQy8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUbsy_R4mMMkSM7jWYKfLBB6UsdM_LrWc_YBEBcnuYtSCJg-wpUAAKw2V5-zjtAHtqTa_ZEPWSQryGrHaKQbo9KIOT26_jWt2nUNtJnUrHBBS6woyOphCSya0DuiNc-n4f4oX4OGj-V8YxopCV7Qn1Q7HnHfaofu6CNOqcXR2ATVrMvfUIFyziTgzeGALknIZzywQBEkf5pIHcHWqr1XOkMT0dCpLJ-E2sxIy0j2WRYpGFdT2y6zVArOJZi8qHoUL5CCMl8PPilBaWb7YeQyUoQi69xs7S1a03lDbgvb7XOsy3K2b9pC5wIXYSbcll0uLOLscabayq1rxBDUe-eUQy8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-BV0zbxl9yTBY_B2JUAyWGgcv2jvEJDCutKdgt0m6YSR8i6VV1BnUVqtvH416dy6rAwkK0eO44kfnciIoxkP4i6OU8BaiXna-6CyG9qH6UwPQxknGXcbtHBFw4jztKKB5T9tNbQvOFDsLmzmGbrBEoHifC74vyRGaPYxt8eMvtrjtKgG265SWEDFYu9u-2TgZlUeiw-yhtxTpKj1DmnU58JkpPZYm78SJ73tSocZ0w9DOIEyTxoYjCK9nhV5LJlpR9L1n27aZWk1dIcZJPnANB_SEfhfF7g0UDpmkIRSdc31IFjp-Iac44CNjxU84KjPxEewo4r49KmH2z90G0mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV_2ugyHit04CC_S4pBfbgi6ElGevckAAQ5pV2evNPJeqaB6BR0wsh-hhNhvOFIrjdrxUExn7jgzxcuoUPI4QR_upOEWuOKYMmaOteOiW7s6UclCmBD_AcZwYp8KW_8nFD0MrA845e7NlLH6JYNnbv0aCdVBpDF6Sy_EZIbVbXLaLdTr7RLgQYWH34YIrcH_vo3EivgeJ100m1mU467zgDsvowC9cU1-66I3L06DhLIr2m8rVjN16O4-6A0-5ptaUYIMSnPbRmS4PfBx6SxEV6xcbVWH7mvIhZ3kueUTOX7nVWcMwL9jwofByTbTNLhQAMUWYyX6-DwXR8LIFo_f0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYrW25oH5LQojpEW3zxWYI-dTZSpGTdJqwAeAhR_uaEcn8VA2FYIEUWax-TkYmWTrPxFr-neWR0E5HV7AfXRcD58_zRzxOxNvFzAoEHBSqwb71Rg0TW6RSHIsMC901t5HcsP_gp-E6lGr0cbeTg7DpvKvQkoOcwE6PJyw2_VhcFgVIngU-UyEtR5-6aSZZWi_HphFmI1B2ae5Ez4Lp1331fJE-ux502CKkkBFMk5Fni7HaBhdTx9f7xKV78gMiYe4VkU9becfmyS9okxUtaFTFxEanKYRqGJzt_RNkDx3KIFOEJKZ81bVUmoXj1yL584nwNMFZnVKpczd2FeLdtbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CainO57Xs5o89Hd6XGO6kR6VzYwdseo2lx6VZQWVkqwfcEZy5YEuRacq7wVic1Q7COKMraYCZ2z0KevDgK4D_UDTI9aIn0JjRKiOUdkAvDp2NN21bTpRPPABlMzte5xZFLTKiVgL3kwBdBzCiqK-ChfRG_2cEYznNwjQvtma1t7BXC_6DnwWsu4I1TnYG2mvw8EE24Tl0qB26AZwwg_v2hRsyz7FJmcrI60STPn94fkOXSQ6NADkYw9YmJBN6QgytMVQneUEHxxZysSYL6KpW3i2NZ5IT6zJNA8D4BZ3dGKuGqf-RpZkJ5t7uTqEmKBLldiZbNusGTl53sJ8gHESGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcF1BeiMmO_HDqjDf8WjLUQAZvN3u8VPJHurg29gHfHPIiM5tuTOncUHyIblRXIS7PMmi15kk2kHX9AlTOPbMT4Ok_myHOkpm9BNvJqbK_74C9QnzxNctaWvYFRsthP1GnmTzRM7jbgIHs0ZwsimY_I5I8-mM3BqpgmVGPkbtzPL99Y6zUmIleOHd68ZWndCwUAKPTyovxOc3klpP1Z3SD_N9ciKaeGWiqY6nvFogeG69tJRRvNU9NC2RfDzlYRiQIdQe8Yl9m3l0vXqIQtZAZMnahrS2zMs1hRD6sFUyCn_uVF_6x_0lkUsFie8mOGNxSROCWopJozqtb7EsYoChQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
