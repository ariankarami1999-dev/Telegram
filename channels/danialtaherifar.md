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
<img src="https://cdn4.telesco.pe/file/Jo8ADfoEWCSBUh0dkaaPbIFUwHpQr4MD-hKdOMfm3gAptnJRo8p9Dv_uHyLlnQXKhHym02VWkCXl9OSLgT3t9e1S6SHzAMZsIyFAuq5bd8zjjrDm9VvjKOH3O5N85tLzEtTb_gCCiHXz0W3aMSSU82YB_dYeb_6NC9E2FTQUkNg8B7MdW-XWGQB7bwdW323qQUGKOu2UsmANNrPnOvvtqMfgja8iiWkIqfDJiONizzjDu7OnoHBFkbqAE-W7tCBrW8Nt8emvyRRIgCsjJMjzF0i4Rkpb6ADHqEjK3tKPVM2qqiHTtH6EA5n8d7C_2JtN4RvgyMVc2SkqTPo-7nszWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
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
<div class="tg-footer">👁️ 314 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3cZ_mFfvwWYCJTgVComN9oeI2ONA6G5YP5PDiDgudPHBfQzJg_xXDstb-LABFiSaAXzG5wx69Drbx2DezcJ_OGWe-Vb195Hqv_PRMIFRwZOUwtnyHdU7otJkphoHQm2JSUbMwybWa9S-Qsi42uNgrLIbjX4y7jspJNSElWXgvM8sgzjkf8gsAnrOeypjTNy5OYweJqg1pl4bepa3ndZxgD_TBHvm-mKZlh9lyo6CMU6_dxwkbNAXRc8q80KjU4cALWa6UB-Hkxix_KPI9BD4IU9yRTVADvrzUDtH-Dp2kk94_4pzsFL_qJ0ZUcJqLWkG2Fkg0BhMfLJmWQ_oePjEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZmfpBbHmxzjQiQ2uBh7KX_dThsgFRQJE7XnFqy3uEJsSaqoJCZM3APdaZXzQYAcHiDjXw6ogGpjLIa2g91cwcRNpwr7AwewmDcxmOEQWI5P4JgsJPdGtadHPiHcEn4KTIPmELLDapTPq1EpTt6QHFPJfQSEiAgQRtzYDYfTQBe0NRvgq3GMJxQ_Ng_M4rtqGOkKDHjJaeGhNTtO8LfnlYHEv1ORR6Y-Evd24kCOEKGD8-lCPZYqKQgbe5v1TW649wtXCUjPG3HAcqVfhi6codQ3SHKRSY-C0dzEYuFNAvb3sPuJZSKg5GvCjXN5IMb0qraqFDdDoiUZRAOUUFXioQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja0EY6w5MlXjaUrrjNN9Xz29vsseTHVnoXvvGtl4lZ5rsl3Sti5Q5969apAy5mJ_NdfW5xh8EJQpXHxsUBh7ekzixVBzOB_VXQ7ilaEVUfuK3-0q_RJa6MMVQiu92qT8U3K00yVZe70PJDvrX-1puYl2VEduN8lsL9dbjrM3ljDgRtwy8QitSaIiN_8Gq-4CBsFl9Mh-g7qfwnOYUzrezEkf9aT0YpSedSdDeQpplVnq0uxct7w16KhEkktOduc3nobZucZA2hLWM2nEUV3UDL4Z3TzRBXVYsWV9AUsJuGvg7pcpESRkWL9QRpbriJmkF8SxZd1gCHbxwP7sUMNy1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv9SHTEuWFRV0xdzmkNE2VFXcrQZn3_hjct1b28E841tVvdrbqyRWOf4qksrukCaSNiR_S-lf4t1iG64EUlEZD1wxVGIsb9qWFFhoqdMUt6BIOjr_9iWjUOma35QJhGnBusv2DMVIBJKws6526y2kEtIlBHerSN5NEwJr52N7WMsEkbKz4jjs7G8ZlticqitjUp4K_E3Wl9TvHVZBwNw8RX4GIgL0PWnGUEanhVCntVeBGU4H47ct-H34aYvBttIK5E0iXCjIy7lulDIUqMoz0lW3QFYe0WkDiDvASQPJTw00FzHDgP-98s-hoNWUDnlokegBr5ErAu5RTJ99XgvGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnlL-tRSkDKTYCGzsqllt3cUFFYpB1FpupWgq7nJVvT5mua9FaNTfj0cNLot4QZMuBzPy-Vs-DSX7xpJ07QIHvvuxjdSx9oftpMKW6bT3YJnQzqG8uBGN1mvH5_fIFCZTgiCNHnKVgVAX4cHlzUmt37FguzAYuoZkjM6OOEQJjGzySDN_fVdixq85bn0qsAxdda1f4P9WvLSUTEirjMAVKd_SxhIvuu3vIXKCIHsSxmONXRF5EFNKrUQKEuQHRaJU-TcoY-6U9acB12v5zFhSrU51R4kBNAxhTPRscKqjA3O_r0TAuJMZ20IKmT-X-YdMIYoSm0pl9-vjcaTZk6wgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9MJgiN1A98TqTYoVlsGc1OBdcmoyJcD9WIfrlppOBSEESGrN_LQ_i_ElupXF3XEFbVXN4mt1RuhnNj6Rr7Z3NATTiU9LOMak82o4Qwp0a2rPnpp7ZEKmmmuBUTBSSrbYlDbdYhl66FZaWO7RuUFo1wAfkfSIM0OCwQ5rjiAJlYOEwHO0gjnwg-9c0Wo1NdL4Kagi6H-9FyUbjG_B34gZo3Wv2_rEvurmT68sjU_nXGHDm7l5wWijnTS1U53NoMOqQ689YMhnIbAlIzWJqI2LMQX3v94i37fcu6L6lq32s4LhgtlasXKgKq0FwDux2OoIjVflp3AQ4SBMNfmCyiMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kb1fMx7e56yrDL6MwoX5rSqQaaz8tkQcqt-0CcvoZ5ZoTy8riRROupHJ7fEQWJkyMtl2pmWzJkMKNGK34YjUzwLFJ8el7UvvktcGt8j74vlSzRYPPdlgt7DmSeVPu4Ib4K2ydlSSy19C5mavHArgkZuptB64nNsTDQW7t9-81IVuasOP3ify_cbLFsL4yla_wj18wA6dZTiNGiCeGMclAuC_CNAhSJuE0JD4cgPNxU_WihhjzWPUgXv0Q1_T4oduKAvnB9G-4TE6QziPn0byL5c3qa8orh1l_t00cQmiHmyQVr-6p2CR5nC7kQiRw0Mq_LQqAcYDlvA-TTPiOl4eQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/en3FflTrlNPWSBv5r-sSCtIzM4Ivms1_jd51qi3zry2wYUmsaw2VTK2DbkeBVQorKoV4KYJJcx5PW2XPC5B8UqKcDzdZVJ8DZx9FEwChlw9ibNhyE1r6eQaxIOEhxFiiOL8Mb7YrDMQWxEYMspIAnJ6USsMticQGdrK4ua2pld4RzoamiqvEnJd1suektCaddSehv3XElB49Sl1S0C9tTqISPI0Hh_4Ix8wlU7p-mTtgadNiTJXvR3OgJm79YWexM60Tp3ZrQAFhP6XKhrnSyPs_g-zoBQV0kirEgGtfe3DxN3z5hqOPhC8obV3DjG_S_ei1dVA8FV3eB60Fvmuebg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FysGEM3_HKOOtWxgwAKtCad-IUL_wez9YFB7QLJ0CQPJW8a4btz8fryaKp9XNn3z0Q1SI3eNk46KnOSJ_0fA8bPKcgfBbfXmppqEO3s6RkI9x97sITUv9VsqCe-A2RAMOMvY9HXtJYkEQlzHlaauaoxwNP3yWxT2nGNCwTVa2iJX-z7A3F_fX7fIdE1F7TDsF2GNdCSRgpux2XjugnsRwChnt5eHGdel0rF6zow-sqa46Han7G-n6_pEX2yYyEi9o9M3mjC7BblV_Rq1ip97e6iUIhxL12wqu7Voqn6sPsaihMDACj5AtBTTatjdneI2Hl3vNUK0MxuSwb7zS3SDxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=rkYAQE368H2IOVkV8Vt-apL-5aW4qDs-yyewNKlRChIR6gsNlL8D9KXX4nP4GnbIfGy-2it74APbIeg5feB8BTcb9sir1YOvDFwv6s0skaS-SL7M6zGxzUDr99pMv-ducrf48yBiK9wml2VBKKzppytE4ZV8bRRMKVf7qM0u8-WsEhUuYhdnZrshBshw-HBKYnHItN9T9huKD41djkM16DlsKW3fbzSfTm5dPCwZVbNX-zi98HDK93JIoxxSrCsz1RvUv5Q9sI_3nSzm_b3PxgJcAIXsr8wq6eejrRaRL3VAYKSvoq2fb1lOJy2Tz6VMsSWb64K4URbHjpPmeolSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=rkYAQE368H2IOVkV8Vt-apL-5aW4qDs-yyewNKlRChIR6gsNlL8D9KXX4nP4GnbIfGy-2it74APbIeg5feB8BTcb9sir1YOvDFwv6s0skaS-SL7M6zGxzUDr99pMv-ducrf48yBiK9wml2VBKKzppytE4ZV8bRRMKVf7qM0u8-WsEhUuYhdnZrshBshw-HBKYnHItN9T9huKD41djkM16DlsKW3fbzSfTm5dPCwZVbNX-zi98HDK93JIoxxSrCsz1RvUv5Q9sI_3nSzm_b3PxgJcAIXsr8wq6eejrRaRL3VAYKSvoq2fb1lOJy2Tz6VMsSWb64K4URbHjpPmeolSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKsCHGNP785FwKFaXdAj1qoSe1MhyRNV05tYUwCMTrZ1hL9o5OAjewjnBhEA2pxx5uKcacbS6QjRxGLNrG5ZGxEimgVseFR-sxrynsi6X9aPTmS64eJXlzdqgOHrQ2ih5moQ2WBPG1dsiE1AdKh0CMXNjSYydnx5y6ilnGn2ewdhFEQdPbZQA5hi7Ag_AyMqvPRmfrTKskhGZmMFRjuG2UXs2-eLYRF6kN3ddKVI-yH62AA4LC9w3p7-6ugP3-FWiZG4FagYtCQnn9t5EqVeOk1e_0AMH2sfLODE85u-LbaK_sBkxwb_QS2Y66gCg6Cs7rkLkVLok6UkUm2DykV14g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJzNqGwIowe84BUo_d9CUM7rGUwsh5sNrAxj-deknA8Pp9dTMehzJy0IMGAicFIcO2gy5RSOei7PRPUr5zkhmLiq5cIMDJ7tc_wY7k3Dl7X1mSEpQVzS1-3C7ZUNsiM2oa1McQBNpo_-EofU0S-Z0l3my5s7nrO0etOJVKDeza7EofO3OCwVQ3rdCiZ3BhhLFIblYnwu-sVr6j1PKajiZHlARMgSgzoAHmqzihlxq41kWegSmmmZpik8a5Gtt7uI0tbNp7C8r5pIQFbyXoNTLzpDytzJxeR9EOZSCk39YB1F_hlhDdrgp2pCqNLjrqqZoG4SDxrlt7tPwqTcAlDcNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoanU4jY_Ed-4TRcF0ZATWc0O4tRRYSWZnfmNb4vk2erXJJycBtCWX9N4FicuvqOIjkuNO8X6xaqhBELIc_WOC0Opthzj0GjJk7sKPMPGjD4gElMQZVAV1-xo6u1tHmzr7KXcTthj-rrJEebdTypqUbozXT55G4OLgPpNi7jeB7D1X-SAIvnWKBus65W70tvH8mfwDbTQ-pHb6D0xcduVqk8FbeZ816OKyRKTFS31NJGmM-G1DxPESZprkYgILKFLzs8EvOjZbnX9yN4YE_O5WXSlYZpjHU3-XY2t7t2LK29l4AiHVuoozdMHBeR7Icft4TEzRgXYD3BDeG4Kk0Haw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUNGW9sIaWun_2MbWpneVGO356AaK6uVwJkNR_Pcz9rwHxnyrzIXmtMZU50AGmxUfre81CoHHdqdokc5HPCuwzgWK-NPgxMZcVEdbE_b19xBMvM-or3H0jaXm2ghofKNMWJYoUOlJgAiGn6LxhJj8vY8INWqWtkXNy-1OkQonrHzWffhSKNW7U94_TQqUco2hk-1eyAx4yq02weRBFJVBGkwPpvrJpkbVPUR5Y0nlKVMMU1gxEAXuQz-2x1Ft_c6plrWVXoeySNgGFgEk5W-rj-IJih8kkBWx7SidcxLdRBzuD9rU1P0aSXoLB_vGjegBu4ADdorRO9IBi9RwezwWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRJLYQkAy0mxC6_dr6n2Qnx-A0EEIyzXPxAyNPDMdMCsgAfODLY0YiahPkEkktHRfdXzw8m-JNU9WAAegUM7zFtlc9EPP_1o3maCid2nWvi0FlblMnQNoJdBF5tdAHvnVK5fSyLSxS7CPGCxTD6QAI49DarClZQfhxIbIsIANmRAWz6T4PHM8MzBIvicDGKISt6KB-D8oKOaJEw0XzF2YzP7U--FVaA-nOUlWnZjJudF4gwPEwFUV-1CZDZPRhQIywn33J-12pNwMXHdifkdmBPYcJBzz0xkTpQJoKDBS3LbRkgiky8GXsY5rStMYmRp5FLZqdNs5KuwbWkLvpBEIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP_dCS1ihUFhmLfL9QLwOzowsC8Nr0dGjdrDqyMG-bTsG1TALBqmHSqHzepYQfm6oK67IrB6-ZNOtxboj8yElN_2fq2o3exbEg4Dfp9cuZJkcFd2h2MBeXz8rqoMmg3rGV2ArEG9urVQLoMle7u9L7hBvT7OXaC0abHiPv4mDM3DMhatlAHSB-YVGfmQWNvleTfEQNoYsRylmzZT-ri0eZ9IOeE0It0wdGHeJg5GYw152NTRniEa6FgTu4Zh631EePKiYLHVYxevST94alRUW9g17ownwErQuZsq04ILsdfDelc3fvYx1WVxEvuekwZFo3oQZ4VgtpbPX0iC1oviZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXyiOjiD2F1qBrXVFhhH01DtRMx15JAeDJ_Aw9AsJQbDwB3t8deO5w0mNzIuf9KzG5Kq-Wc86xAYw0QTX5dXhDdh6fALWtc40fAboxBgKI8tY4rN5wowryjLz2OStck5K8zQEK7kyHS-7r4XQCtgwbXINTm8rRIh3GAY7zDmc7sGKKCweP1uWblobcJuWYmkAqXFVZjXOoRZCSXrC-L7mbn_PI4X6m2h7Lkh5paT2KA7ofjRUSZ1w3NCs1iNLPGqPwuy6qOxn0mU2XkWX9uVsGh_TPIhtw9hILk1H-DzQP6-WPlprTghiDbjf5OWbKe6Fm0nal7qbC74hoyMY2TGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qy3kDQZCeKLmMV6LHdc7b6HU7AINVsoBMxvCk8tBm0KIll-2b3TH5RQYGaKoIab0gANMN_nnNmrM2KIOI_jyuH6EMI8PHHQ8WHHwoWAnKti971Qj1dFAvmrIzskOLA5nFHvdCvDEAkNpiH93pIqzCAe-SHdWlLAfhDPMV5jhbbgLhtIqkfqQvwK-XnAH7rD3uUSrFtcuohGJncJs0y_LZbuRXHAxdovtXVeot4Y-cQbE5APGq5rwhPQS49SZ_EX9fg2NmmsbATdll1saT0LlPkVOFNsYeoYb5JoVFK299YxANZXv4a1zk249KiYk2-y5gPdCianD_P9JOi5Qobda7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB2YtGJ9WE5z4vQ29cAYIEVC5Enih6Y7K-D4_YTRcyhI8AamUdwNyJvV1SROk3-yP75-0GVIvEyeyTWfrHed0Tg1Lhi7JJAf1VFGmdj__03Io4V4ptQ6-oJ-OnmGx1fKpKV22AOpQZz3MU6sj5Mh9w6ILZKpGpAqy1AvYs09Wpg3JwUlnRAyxGbJ9Wb4Ry_RTTNR0JrqqcGQsroeGAXpCMA2u-peGgpSubxrMo4MxsfESciSbL-E08fwy2FSz0d6g-yshyui7tz2r8vLUYB1F5CvGT0P16RWY_TON63MSgtg53PfoOhqD9AkqzXTM4HOjOIlDPnxhMosRf20govOBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ2mk4ukcHctjbW_9-sR2DQvNvM0BZqV7U50ujr1WCOYnIkunGR0XikTEWPf7o5Nib7T06Wee6D-lzG_H0dPeGZe7eKLgyDxhJ-C3oU5Dpw2xpxcvesxRcZCQlBdflAKOTzuUvVok_jAxnWDwSHp0Tj0gkHoziIYxMv6vXSl9OdMfuPJo-mihMRGVPsPvUxl8cfcNwFqkAAgaGqkHZwsk-nqF136pVZlXF2tP_UwnjWHh11g5OnUN47nKpUkcdWkZcFycFcjTLp56eizfzouev0LovcT4Wzq5lhkZ6YT-GAXKda42l6JTIBgE8QHsaqQPb_UO_G9gQ919pHRDhisLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDErUD7xShNJSK91SGEo5bgugR4_t-Q5ZN7AJos61vdbtk3pVDnU0bWpMYu9oR_qmV82DKQIcceYaD00qNL2f5BgulOmar3b3SDDF80SL100VQWf6mkKGlEbIpbpS6NouXZ6ssG4ZpeVLl5PeDInBNDt55HBE1r0tABRxr6qICybpoG1OfJT0oGtLlvPg_lWG4MjTI-lcl89uVshEN1vc5UI_phUO5YgctCSLJ8GVM_5m1qxeV-I5L1k83AWIdxZLD89ooJDyzh1rJkzPyUczYmP7MxBvomAry_P7Cqb7s4V3hrO3bcQV26hTZtyvrR9JeEzB74t3z01wqNY9JKgcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOMzJKNVm9cwbqhlsTIVw5zhdhZ1TG3XCmDfZ19PA3TVkF_7EB0ZDQ-r6JL5dxnJa6MfmjEaGAoC47DCraNj22rtZOKzsQ2hXmG1Wl3JaCatuuzLIz9tvBcoyAoVnL7_jAoLFzHI9D3cY8IAqakdKVNUARDg8zotH2Fg_tNOyZh-LIfamMeILMC1kMGJkiLlqshnNwVc1ljXnUFXJVClu_3J9S-lGsZC6sQ0tNVdezTkOYUPjlp2cr7KfCCG1rl-lpc6rB-tIbS9q9odkiDEpilFuSw7YaxAXRXIoVuVs07QK1Bh9euikYIjTbD7MdL64cd5C1gUEA0TK1Xcr-FYVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA3VTXu7dCXrPxDDBNHODUFWUH8bi0uXrasKvdcIb3CSjWNKe1e0UBvc32eaUkXi3UvKrgTBDajm6UYu0-kjcLUFLyIDCJLzSfbLqLuk4WC3Bjzm21U_sph4H9qVRnNe6Iw3D9mAHJWYsFPPNVOdCP9bun_0ZL63qwIq0rIQWfmooSlmxWvtkyNCXfN_XkuwqQzemhYq-8V3pN8zY36Td01hP313IlmJFnt54ngXB_EbpUuVM8L4fsTTWgMO40kzGrrx1pYlnM2yXIszDAMLHXS_e9J3FiIh1KB5mpDa2h5yoFV5X1Zj0Nvpa3jHJT92KM7QPiZpCdjL71kIOa2Szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDe7JMH1bf0gnWm_QdaVPH8zSJ1N4gm8RCeGJmyPSmwE46W71YQ9dnk-V_ZZ8c9hhlxmoCON5cj9bitG3iQ9NVjBtWONFhYT8k4hOD5MbHVgV4b8WNBr-S3swNnYsWuSR6TN-eRPOWefH4u2QVtHL5vOTw4qoK3iY2-ENXY9PmgsJ7ME3AALA-VGqJNbYbSFVJpCZEsX7Yv6wYznzf1kxqOnjILLMKtGY5xQnstL0Wecg0UTcOFGVhxMH5Bh5bUsHisHlmwlyNCCaQMMdf45TI-woNjK4UdqJ_IS1Ma0lP4XNdE9y0cQE91GiWBGisWsNqgk_2opVdMldsSZiSL5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rg4oK7ETYUW9WnG12Nps2Jgn42hLicpL-fAfTZbGarofTi5PPzhmMVquirPNUj0RcKFoeCyxSpAZdJSROHBB5lJ6Wy9f4q8I6yyvlzIUJ7SoxDHoTKpKlEniwtps8MU57Osjk3zriI6nKGSSx5irFLy0pS0I4yUHO17q-ixe6atazx253YnA_WyDtjFe6yuDa9CkcULRBayEWlBPSRvE-Tgd-C8PeVpjIyCrhL7WubAn7XXalBiFb1fNDorwDwAuuUjx5YS-7BDlBjo1Rh24rsEJi2DAZxtW_MoGlr6rcExic1DXbW2dZhCyTzjVmvvR72fBVaxGkNP7BqZjyQ-CPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4iLkPFOPwXwC7GPzzSe2xRcLuFh8B5KI_mq8XFg59qbFFhgmYAU3iMXmiNta7wsB0y3GOva0LaXN3l0dh8Wu5rACRA_Mo4fCD23Ql7Gp50l6lb11avpIJsMdBLYoeZz37wBvEmXkaHJKu8V-xMtf2oEUuD3QDpqIf7ua7gCFHPZNtIoPBhxltnNUGblC8jB-KXLNnbXr4e78OY-TBR3F-b5gGXaod142HHABxrOtNWb1Kv_FRMv0NwyWrDRrxXuk3H7TU0OcQZ8KQWhtgSa2lZ_p76Opk3hTCYZfLgiKZ5Vs4cVGNML3rR2OSHun1S9BRto7JTzUpLkAAs1xUuLLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7YUtEcVZSd6z-ly0xAFeVsUM_MRfFoLgFD6JDIB0hjqM77qd0blF2SQMZgDO2BPQTSKkUdlAs2kVdQDeT2bb1gWbb-Kzl3110D3XLwUbcLGxBoMVvDBGgkrkxgPOJoOCOuAnuB2zTtuddeOuvUsKIKPCXw-cO3slPhszisdYLXe4Ql0AGKBGHcaqwEet46BOO98H9gd-4rMCcNGAbAwhk50U_WAg-K-riPhTUo7MkOLW2NKwHvkFJujtFA_h8gmNM1w_qiebuzH1EZISmkuP0npIIcrsF5UGR2WstNZMYA-6D2uOS25hqhErFmWhwMya63L96_QE7nssmO_ItGOgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwuzRteZdXFQohv44SJwBpR-IC9KT2j2vKZbsos5PRBrnDsIp8GIkQqjXnJzWgwNYoSQyEeXxNB0ZunuUgFZH5VVOI7I5LDYuwjXt7yq6e_r5_XXufmVcCNxz6Ht3XAiQPux2l8xdOxzcHjFSlhRaoNHxbjfxrcBmZSW9ulwygztCdnmlCnMpCEJmUcSlXWYMc7-PN2PODffHBh-yZWflr-XSM0G82EHVJUv5WiWxPS33KDRfSZu5l4moIjCIcF10cMdEaNyRBQ-N8SRY9ts9rSKVroeL504J_ii4sXQAkSZOWTsK_8aO_BmjtCXn-nurgCaGuEZbXmAX4xlQ46-mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfQrL8Z8CwlnbPrLQZoKHg6zpVdqXhiOFDOImy6nL0A5PAxu6qBJTec-xz3llHmU4BDUxFRTbQ8luSKS5T9evdtnFeysxPwmpUTc656sFgNl8cyYKicM2WLLuhouf0X-PXzKVh4NsGiZ2d8qbdnrfrrNffDh510eFvQQT6-riTZ88MoHrUcOuuiBa84CwpR4CPw_wcv9KR7i33PgiMEKc7qqoI4-T3bTBDX0yJGua_G5K5TC9ZzWhV65OQkjHb9jcq-1RZt3VetPkw0cn_nBOwZJ9SaaNWjTECgV25TPZD-a3gmIxVD-gcIIFDmxhXW9vMuwHYmZiUpQSHMjc436mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSkf-DjmJqhtWHmyE06N8UD4Ak5IFYncwGK0wJi1fDbbLTHkO2nwacs8PbUkdSB-lg02nr891TBDcXousmDV6sdJQO4HGHWNX4w4kSZBodu7OgtX3d-jzFvLxX_DA1_EA0RbMLpv_wgGd40lKFtuAqAT2Jguk2D9Z5KJbmon7i_H35Lc03jTzEdPaCsoevqfa2xB7EZvPFb9ZdpHs21mMjg2Dz7R6aQ-kuUrKPM9odITUOniUA9hdpOr7qWhjUAwuEMWYD7Br3WVUhE1xPQiFfAs5kB5xG-y0w5d2kUhVug3XDWAWScNerFH-xTDH6-KysyMqPC1n7TyMcNC1AWs2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8T8l3M1JVtw1XyHLgeBYILgP3hJRmt1ALQbgFaRm5K3q72QLRJX3eBf99gp0YIhdMD-3NB0Na55DlTVnuz3sB1-1BvBewlhMVXabFjQgfrOA9Ov1MRB5iaMYhDTEM4Cpboe_Rmv20SFK5EeFj_9UvFVJxigYsnwYLL09Wf6ZIpHTBa8ubCOLiMTs_udOJU0snO1PLeUWTrjsz25dX7Du5uZ7qm4i6D3DFPPNYq6lNDJPXBPEZUgaGDujMP-1VrYcgPtKry-R3GOV4pwLZuYivUezWnRpUqxolZTu0rtd87OTXFW-OO9Vt6tASQTyN3ry6yQPYul8uDI5FyuAJjVaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQOI5-6A9of2U5G83HMd1T4_TcBqwZkr62922kuezjdwdsc_Wc2-MlMh1AHnLTH0BjafT_m3cvGMQFh7P_j1bZ9EOGm6d0QPKF8svGjit-flccTqb1VorsLhkCGTZq5L4Kq8qrxpR_PB6CKrWeOrqtZ6UN0uKY-pRnEVmVdm4J1hgSbFGX6dN7gDQmh_Q1JxWTslHwtOfBr_Y9tgwq02wh-SLIkhIIrncGCG5u2YV4Qr__Hu1k_UxmoVDlmgaKDZbT15KigH0Jtv8dC6XSN2w4RtlTqvX2ZfhgRTYXBzlkWBC7K4mLletlwEbvDi8_FXnnjNFnLXB3ZPall595tKhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE8rHo645wu5KBOjf7BN7oOEe_4T0sF0SwrGizzrLT9ni1HAB8bBgOp0vKYWDUoo5_UyJ1pCtM3e7jV4Gm-_R2OY4fd5Mcxtg7Tp7A2SZ1vLvGvWU_1qULv60E9a-JzsCvqqAUIfBQKlw1BlqqxLSsIO4DyDg8mQhGtjxt8wslAWTul5Jka6WtHKv2rMB_tenusZYJY47Q7M8Tk8z4Oy9lXFJ5vSBmye2mWA-XVLREnvcxk7TCU0-rBoK8YpvPBSBLvC2b0P4wbu8WN_Ac2E1cKPX_ZLksNSsF85uA6MyrzbeOi_onH4bx1VCvdPo4gVlRdoBvtGlDqwC-xeO-vsMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpkWQuw0Yp3mNOj9LlwcrdjidIk1w6fpI_DkqudwVEWSnhPwnlsA9BniUYfHb1_L9zJGGAN2dxXjU1BxBSH7WkJl2UXXNnaqStLSjGv6UpAwHgCxpw_UYRviic6CLu8DHBTvlvGF3Vw0ofVXhYS-QJGNCHsDxovhhDBqfZocTO3eMxyOoqjI4lcVpMU5cb2VFEZpnQnTI0hhCs7ocYNOOBjcA9-V0i9XHpELKgMp7qw0Kq-WDWqXoO2X3SMTEuMsNiJQ3EIcq7KEMfdhCeN7xKjSpeDzmuSr756Y0OiSFZt8BoMG2WRiS4jLBveq0Tg1RSLtLqOntC1Z6XSZicr2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMFPxAs-HDU0agnqqv9ecc8t7P_3AdNV0WXqRPor3ou6ze7yhg-EZs4h-xA1Tk2YNhA6v8weQIGDphQ6oeVtz7W_cwasEmHSyqGV9fEw0C1Maz3k7CI7XIDBcW4GHYcpc7_eKOI31ssQQDSo3JQ7GRGnpDMXNDXu4fOqGfi5uiXcaxg7DMAltGjf7OcL7J231ZlyBK8uct5-e7q0VEF-FeR3fRX2SITf7aFioBwb_i55sKD5_gvEy0cLerOeH5H7Td_aDJVaM9JuVtNjgzQa2uvgzmRu7Q0-b747IQX0ItZ1YyF7nHFt4yo1PqdrQhLyW0c4AXVK4I2u2r--elPTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL4kw37Yj2uMvn_pc5_o9zPLlAQe_MAlCNZrF8HB-T9EIPdTrLE2l-SmQ7-8liMxPU18Szxo8iNY4Z_jbHUZXKPV0BOUPBpZ4VoufxnTIEkjTqCb3PK6f2ygUKdFb14jqvqanZkMJk2wfUz0ARvs099qXxgPjyWFIsfrbT8Y2HKYQq-VubQZf63a3YDNhI9O_L3ORQS1dY6Ym-9DXnNMb2x6_rRVzGEAKtWMUT-M2YQhP5UABtxUA91sOvsKsNo88k5Zr3VRyN9QEqnH1PKYC5YjxkIl896NAoTQ2nB1nypjnDbpFe0jex__NauBcDh-a6gqa4QQNXXOBH57aYCKLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu2NED_KnPbohhd0fozqvH2IAZCHqP81PEr8M2lVxAnMEMbSgKyy8gGdHcLL3T5nfZF0TcrpeD7X45WyHtGVsOgS9jZiMo0OfwQK1PkWRrgFyvaIYrToh2YkUyPIZPPHN1wy0xmY7SfWSj-O1pLa3BV2784wGaHoROYEJ0nWNxernRAe291dvD2zIZ__KBDqRYajXkocQfy2FJcD9Cy1Tx7Uzx7NLFl5hTFDjchoNiIx2IVJa7QBJGX2hBkN4KD9AgVdlwAo9ZuD4olHcsvY14CBF0ZV-oJR_MonTPwVVaXD9U-YvYnN5c92znxY2ImZn981sLV7DWRQnNuhulWO6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFf1LvuBoIrOxAktkE0iP83eH4vcPBnSbUv_0XhS8Uk9TesrK2uutW82RCCMmz8jeAhtvo9QOmKxoCnuZRxNJcieKI2Rz37E6rGbN_Yn4CvtBeryvyeXu_RBO8q417OHfpZ42tUS5XLBcNxJk04JO9qxT8jcl83LWIgYOtdX6wS8VkEe65gbgO_cfkImdeY6txWZ2wyWZ8oO0U5G5FqEwCozhC8Bs7RnqIf__gwlr7jt-OmBphxwOySfky2pE-k6FcNmVIA6dWPpjkkEBKURStDpo0FICWlDSntvDdVQS8GbIJhyEziCPZn-tIQXnpzEYjNejwLexFQcAvwKOCyujw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDQ2tHxTUBLmezBrqeSU--Yud7ou9IL2ioTQFiOs4ZrA3mDJG-FVWzJOyEXLS7OwHLxHVqlpCsHlHtrW-tOSx4Zl-aGhVjxusAWMhVm4CSPd4hN2uJY5yaoK1IJOw8EvM26IQy_Pd0p7043nJydHewm-ihIjypCowi4gltc24FHJ6VxPkQeowq16CEc3bZNL1BK-rcf58kB_F5j25WeQmD0EgnnHfPw3NAzmFuMZ3dX2IjnKUVFgzp8njFU2Ohbr1NhiQflqoOQpgL2EecDINb0JY-lo0YlMY43UHu11lwnI0Kz1r21qLqul1Zd18Znni5gczRoz9eLuSadL0tBxzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acBiRjuggedJTq7Vso48if87jqwpOO3hS1CKdOl4dN0QO5yi7B7NxuvHfYzAtj8t5LEgXeP1cGxVVQpDNh3chGW7RldzxQamzHVNVHjY0zs3yYE9AHHw8pUlFqzFpP3ccsmYjR-EdpLn9mtUmOi-ypfKOorXGcRgu247VVCY7U13wHmhfnqmlMXwGAMU_Ey9iVgWTEESWywEkTBtQgS-kmCCsxCIiE9oMUysr28She-rfwqP_cJP2BA6afMH2wPjZG8Nhem-qdoZVToP7cmnN4MnRlSTWUY69tUM4Y_vheL8u75mIDYzoFMm0P28woOF23ivi9tuBGe7LgkL08J9cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dowjn3QeWEN87CL9dUh4kp6a8DsKAQwX836wsNpQ49OqQ7FWTj4kWzR7wg4yNvaZb7kgoOYixGlmGD8F74B6Ba4sbmIfkmEfRZaM5QvYrHsRlYRr8ryLlTo7iU1ktk6nsIdW95yqKHUDkRtJArN5MTIb-k0kjb1SYRAa4__vsvMP-eIXdJElmwc6G3NkTN4UoIvaEl9kBE0UiIGLSHSNP2TJb2AJdt-WPFZL2LW4t18ozWw7HMhZ5H9_joXkHDfBMjyKrbwRuM9fuGWXt53UL1onHKJjWR9styvxJbM-HitHt6G90vscrbq03bBuvLGvvgTTxyuphXHUUJS6H8E66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfeyFTxnN528832AVYT9MOQIbg8QJBsJ46fDXh3m2czMeF6a8yuAQsNK0B28q5frFpfAHneE_SeMhL80IuwhHWi7-xZKgEWU2MJNHl9DS_XIK-I8K2u7E2h8nus8nXhRapzGKCAnC8RB0F---RcYFskUvKwibVAf3cpzZywBD08cv9_OKGEUNgCt8VztkHQAOnT4nruZSkBVzWKmnSU7RWvj5LkkwP0G0f6JHc6X6N99lHD10xfKlPQF2YMUK3qPfPcJ-U91h7vMwUT1-TYzC225FN-DjyIsJSWcUOF4on_xGFUuYmCq-9MQMmEdPmnqrhNBaSuSkmnVpBtSGziY9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omvxG5nznfzcyhgNcNsCu6vtpZckOwTltKeAk-F4xYYg_oeTzCLjN6NHVNiDPTampVeg91Hq1g4JeE4Pfz9N7p0eweXcPBxGjqtYd3h-EGvQUbROvrz9MN4kJ4nbJevXc4EuxqY1RfzqsdlWgW4RMFTZb51b2pDmGiuUXZt3PmYA5PeJpTqYqFvOV6TNs_dHYiuMh0lsCzl2QKYW5QqV9y9Emr50d6lQiv79g-VlkGVn-Sy-SCMoOxAKwLXe3p9n0VSnyeop2BLNpWI0fHSzIEqfnV8kroHAwoPv--Ngp3lYdB-s9qWz1AkcsTABnFL94nzWQTNaP84bvLeYwTsvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpdzP3KZsMhCSDW5ujSji4nSllYt2ImAZTCw6QPHtjBayacC8mQVS2-jExD_MBASpkt6whVgeyl7lLEzZRZSEPso4FwCR5hUD5F34e-Qm9GjBbRDpOAtuTFrbQEwU7BNkC6J3jza3m_n0lUC5H8Yk63tgxBZZHz5iSBU9SywErODa5SiJ01gMWzjc0wYfIDbHJFXv8JYuTgQt_uhqpF-2fjDU_hQ5zu_01zgjjlbmPRB73ZHB1bZwKF856KcjGqoRp2409DkA6BZutohBWP5IDFWPNeUoiLgdRRn7kxUvSXH1ccyBwssJd7cCMTcpsInvceqyvxtikEUUqdq9oSM1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUj_KgSy1sMd7_EuWjbh4JcdO9TCbcsxI13o-g1kR3Cn5FKU_hrUJQrZW5ca9ByzwtvOX-G1DGxmo9GZAWUSWAAg6gZSGB49h6hTKUmWL8yL41p75woSZz5kLd6F9okjlmc8-Ya6GSa4n5EUiZf0kIkczmZVJH23WHlkPcVayvY1kCH143wa3WugNCqGdWQSEpWQZtIV8Ipa_ZYVR953QeqQ9Mt4qinGreoGRYCsN6qGsc-x93_Z39iLgDxTjrGWJv0He7JmHmZQHEqbVo9nvpWth3C9pEcKg8Odd8KyS2kizx1AMgpgwMXnziysxuDHJ5yxxZnLNooAFo4Rf8_WUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gY2c25i5Ou6GgOD_HuQDzaR-nBBUkDKOeJo0mHmprYqKf73FaK57H8oeEmTUWumhKx0i07ILSktMfL1PS5LTQUDraMS3YvSkcimMjDqi4VXqs25yaTKnods9foXmWrLNHqudvqEDsiOUBeCh9UnqLpfmdUwv_awsZASz4Tvs6AiyvHj3jgYicoadbir6GFQJftCNZSDBzqSg47jWdyY7utrII-8fvaPoqC1DxfUgM8NAysTNS4Ol5_RwQEBig-rKbtNn2KcFekdHg4ezIutgZmyzRzVc55wRNXxmPIyJNxEQwQlp9h9rauYTRVFrD_YYnJtEgSsGuT4jq4DDQy7oBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIkG_TYpCtP-bKgrmBXIYnrlSui_MJS67KRlubv0xF0LUKWXM1_TGODqAjlJsnsxWrOjjy0Wqq9yM3gtyKZvjJ1uAPUb8UZsIqw1f9MKRMqke9YssVNlQjjtxvbTHliwC8qFim4vya5yBo9aTGwhvioOksr5lEKpeHDFfWaZ4UW_qm67UXLVmAKdu8T4KGK_sRityXRQDEHmCTwPK0aEjHCwVPbpV3w-JtNaKfxzxVvgi8xvdFtbrGg153Y9b3q4nAgk2ttFGmPsE6phn3zszrmF2SMAUiDdN10903g8X0s3bobd1AQhIVGGiKiaCKaaM6N8988CsWm4BnxAzpVD9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqzT_OCp5QsxOewi78Ig-PPpF-TxCLmiitOIW4SRNDV4TBqAikmkzNJGOr5Tx-t1rDGUG0eS1PLrTCOOVEHbZAOuvYu89MDWsPcVlvh3eeSMS4WuWL32KZTdAP8ppeGJzOJbTmwT4EFb_ZRhD9ZXW9J-barTQ-T3cu1nP0hnSD6SYDye7N7vAZbPXrp6_181LeFbzlpIO6DEFtpSmxB6UvTepRev3YXow1dM3gQ3aIAM85nywonz3s1XqxK41pMeGBVMUSgM612lCsLNMLemyKYZ_dxVlXGeqScge1mT2OYR4J5LjSO4PbIQbmb-JbVtEMndHhM0C2sKfSt29NOsOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvVgra57skvr5wEcUfhfE6UUcoXlxzdhU28TUukeIZzKL7OKmoVw7s_WxLuyXZarVnbpq43N4DjDEcAZHwqGGdHMpm-_lNsMviCqaDv1j1G8eXtvm9G2AUDkGUWyXQgc22uXQ5DBH0FIUKM7B5XZWpdrWglqdoB1w-04vijxkNFZ4D7yi6EqnZ-Dy-uzFpFlGIQgc4Cg97dUo5SIMlCWUUThZl2TShSpYHg4iEAbzIwF1IDqAwAsJhTcEiJTgXg3tNdFLGCGRB8dMHKULzrwGFEuwSZLGIrWUaleSgoLTcJphJ4V7qUNCI7lJECvDauzGEnzVCYrNk4lsLKLt1CWvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZCYRfNK1cQW765eBtozZ0PwJ70Asw044uCBI-LWkSliJGrV0UB_N6FdDDamE3AaXxfWUCbIffJ3MeF7IZjNL1q2KI4KvzG6lCH6FyybK9RWyXjoC2Q30knGIz_C6_miHxsyIFCuT1rBc0Yj-CnxxGP3bhGmulE4NRcJACO70Xgc94Wmvh0jypTfKUC9CSUm3W3nnuGaY_KGgGvPc5Llw2YGnrRew3wmPqfPCDUxUjJxIGEwS-SoBtY64R4Rk014NjCJcVSRgamQTd2ctqRVnMbKqzW_A1IRuK9uk9482DHC8xbMs4Jcl6_LD7SGx-D9nUjJrurVAsWdx0Er69Vr_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA-1Zt8CRDwabyAoXgCtsXAZsTJWjWNHCzUIQBP4tqK0ee5I8wtpxwIBcknuPvntufme3bO9S7rx1ofIpguEVxtUVGgjaFVcag_Yw-TT-PKXfk8ukPYWmuCQ5XzfyrCWQ2fkSuOjSxom5WbI0YGHCp9RXuXt2Z9gM2P8WjlelW45t_6ktt3E-2y3RfyH0nFLiPJ4RG-Pnjl4Plg6RAq_VRk0wAdp4RlWp19Us_jOKo4uKO5WOMCBy2LLgLWQKDhA0p9MCtC0bYTvVAG0Yp80mGkOSLiEN_432QiOWGZa7KoQLy9XQax2F_4bq-lHCFnGmP1eK4FYK142TlMl7gwtBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sooYAOK2g7wwH4QDPyUsV6_bskzm00ipTsmhY6Kg5BzCKri6wjMe9XTfq6lRIro2kMp9yevpG3V_f5tCNoVeNNzKu_-eVFT9-XSSDVflikrZ1G-pMCU_mlLUtP6GLWjkdWq6kf8Vjz6BcS56ogtTPlDMVDF7lUOCgQii9vL1cR7M93xLzsFHM9AF8srTmtzs4yNXoKmH9qT0ADtG3cjT-d4wxLuvqu5Q0zoZfI3q14Pj2ARY7Wp0NgKKrn8108looLg5Axn7WGBwJwUObcxOIRZeW2ZLGj3EuyqDMgKV-4po-RenCQdM-w3Hb6_Rr-854T2TRoJQUgp9NVIiWvlpOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bezgnQix8bonFtMuR8l9UmlMpvVc67pjhSIqnpwWv5A6IV-MyiTrh2S4QN8ZVyq8N56JyyZtCQ0RrizDJ996C8OP0aSbzaHBlU7EbkTWggsbYMKfYcZAKS4LZ7iYrF8jFQhU5cCA6Ao5lekUGMPLCGLGxAcP-TiKWEbJXRqMWpyVvJh96miLft5fOb6CtJ_BVYwF2wdoLtFminjlAa_xEpG3fEJ9d50j5NdNZgGz7_xHKzmFYd7T3_9vVe2WJ0pvUIBdf9P-0bdt7ILvubxb1xwAdqep55JLnqizr_JSV8ZsLX0T6JRZl5DhqHLOtSr_xWZU3fW2c0xfJYUYJNFcdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8y46lAVaeghheu8TdsxG_Zn-GI201ENN48iMzI9-6qCHvUmxqc6SRz2dCA-PZFd6GGSTnNksBjux6euc8clGThVlAS8exK0WzvnBU9jcm5xHindTJbuyxs8uqyp2cD0VXXDeurrpQUodLcflPh-LmRExk23JrL-BvZJJx_aKmhZOZ9RDndatHTCOTX32ZFRivtAZ7rsT03oqbc0svLZlSznc9op6aTe736OTClFHXZV8JpnJYK3Kh1i3rheMzlXAQ3IH3DbIeCtfsKRR7TNbTo4pCUhvDzVwGBWEutTsOYhOvUAD6AZG35UNuHbBhWMM1Bki7CrKLxKZ8bSOwVztg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXd5t53Ll66CNTV2AXPDq8GUHo3qfgfXCKWSiCu3FB4HRgeUm9bRvG94PjAFHQsAQHWlfG5Yrcxnw38f_RN7i19lRMfO8cQ6HNV_9FR5j1QtpXGXqUQEI22Wrp9pdVTHVuQiuElNWN3CV2wECaAp8UHRY6qIqyrluXRxkoikAe1lH9Gbn3HUBpcdWpM1posHsZPHFT3w8lB7-B83XQ5NNdB3UZkDl4aGyk7ADDqely0nJRW9KaJCP5_onyX-oOIPx2tE2tKKoWP3AsW7qjvZJm-55YVoMW6zynN7nOai8rNZel7ZEWYMd1Oq_F4GhKiR-YIT01WpoVccqvtBvoMG-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5XjR1yZpRVcMrxp-xpSn1NH_DiwERrOMzsmsYuKTtuwrRCuotz-SP45QVpzLZiEnSlxXSkQoNc5U_GsDSyB3d9bjQIapvCGSZykmZj4lyfzRudLuspuxeX1jD_Dkr4eDdSSkdikLXnkiu4wPFXYqlJDzoSaVcTjSkoTow5RrYYJJ0r9Fr9shn5w8Y1bbyJ58lt4IJXeKMGVkAzbcmJYXNSQyxmsNJHRuzDJgBz1K9s9-0-Nfb2JqZFqpzBNMaRxhATbIXmDl-bUQnQWbpDO4Bzg-_WkH0uo1uaUNoS_9crM5AjycIQnWh_dUtdEPq9Rx7HKlyj8Lt5FdjC165fpwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ug7h4Xmo0sI7mlX7SzIL_pX6d-ON_7gaQ0U8bhDCxXxzOB7sdpY2_VKdmrfEI98bVymf2Dfo9gdaYqKtw6XjrYOePWzF9L6vtfcS9Pe0JY03nXekGar34VhmFEPg1JDoEHqqmwKkn4AuIQuLImU3K1BELxxL0pTndYpLvjBq155Huidpf-x1L4QcBsREgGwydluWIUFivuPAzdTzp3lqIgkZrYgFHlsSKPaypWFi0gRZojBik-8fVGlAglcygAD4HEQDVLqkD3eq2cLX11CujTdesRcvHV6gK3aBE__jOsQQM2l_qDR64Fos_-s2uOrW3jsOK738PJ-aUijy-Cpmzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ug7h4Xmo0sI7mlX7SzIL_pX6d-ON_7gaQ0U8bhDCxXxzOB7sdpY2_VKdmrfEI98bVymf2Dfo9gdaYqKtw6XjrYOePWzF9L6vtfcS9Pe0JY03nXekGar34VhmFEPg1JDoEHqqmwKkn4AuIQuLImU3K1BELxxL0pTndYpLvjBq155Huidpf-x1L4QcBsREgGwydluWIUFivuPAzdTzp3lqIgkZrYgFHlsSKPaypWFi0gRZojBik-8fVGlAglcygAD4HEQDVLqkD3eq2cLX11CujTdesRcvHV6gK3aBE__jOsQQM2l_qDR64Fos_-s2uOrW3jsOK738PJ-aUijy-Cpmzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeZ6YB_DTHBbMpXqB5k2B0DheqQRUv399Ij1UEv6vJEb2b9LSwIvQbIhzSbkTTarMF_mRGSBdYVMwpiVLXXTYKoN_uPZEynJuYNEpkTRy0qh-f23iew-3lL7cy75kBn1dcdVb3PNKabeRwy-QaK8UV6ZAnoVIX5vcMh9GH3zyoX9CaAY16svD4BuJK6qffEGvomJNWuFKvUytqCFDLV1EfnEwvRHhzGTAMK_Szi08oDTHffazyUBtot_mrsZoe4OoqB589BhmkVG6etpSnnL4mb46l-w7OKoL1taPuNF9jcKqyQFysXsGLc1pIXGJCMtXhc-G5WYUj2LgNuQcdL6QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH3056PzDqw92i4KAZ4W0X5qxs6GT1c6QTPZLm97o0Yhbidnj1gQdDybi3XEjrShTu1LMjoUFBaTWIM0inxDyiyqLbLN9EHjsFDm8UPSqBJpbfzVu1uTvY5GRPvEc1ijxccA01Yl_bszeFVWAlfV75XJViwTcid28gws3KsNgMyiWZUw8byuvX6xGRDCS4dozPzXjds5pG4iBCuJWnp5Y5kUlsKHqHT8k66jKxbye02hxyUFinv_TyUfKk4vZ4jj8G99NrLX3edKVxZ91BspoFnEwe1CR3wXzWzZslFXnhSKMKisbo5MKW2BpKBUbbhM0PFTgVzaZtgZlWxncOIIfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWjSJWFg98k01IvQxXLRV9WFCxm0RkF9eJl5vtj-1zM3d4Ikx-8hElj7TRU17bT4sVgQZagFosmsu7P5rHpuvr-ZXTheIeB5W56EXRmDbTjBgbE8jl8CZ-FjM0r9GlOa-YWa6U70rgBq1d3fiB7_Hsgf2qUBmNgUmNst1MqIK6ou08_PDXnWR8dWKirFRkrOcjcRXAbV4l1dGovwNyJ-6Fj4DdApxiU8mQeGTntB2lYQBvWni1bLSMrdJicklwcN0OeoZMCTj7H6H363UrUvjLtMroCtCDJd2wrZKOu2j7ytNiiYfOhcMMH-p-92ujCv0K4BXz1Z-OvQ87P5HgE-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrWfm9kYMI2KakOPMRR75ZiaTC5rcGdkoohZxFHZHsMdfz-VUTmtdCRxNGaj93G-CLF42vvsQfa_fT6zsPQVIeDCHL1bjNt4aPbWYp1OrPW9kgD_tnr4vSaAZGAw5ihBJ6Y_MTKDMrdOdBN8ZwoPR9HnJSW9M9qX8aKDfxwAkzoOMsLWliy2wEHkO3qSoIEIcO9ppBK5_CNoWM2akQHEg6fen9BBZxI4JTv9yjhPFbyxw5GgHtXefYibdabKZlgacJA36ei6cSToGcTd0LuYz2kfBdSx1PvXoL4-1PPPzc6CET-tvNQuCFkCHY-WFcvhsRjlMKFLXjijBpURDOE_sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5iSs2q6EqMkgmbhlXw5vlcly-UEBqlZW_VRQK5_1vdmp52ISurMS3TIzPO8q-FLdLOiGtood7ajdSPmLsTkSt0NDCsurShTfZtCF-Ove6-aMZRjdUrxQT_8JH9M1o3qG5wxgjGEURjvEa1SySVLVs-9i7DgkfXIGEaDYqcx9ZA5J_A3UtFXdjxrXWXJTJX4cvUXVCHdJU781vPxH-ToNuwu5OnOCbyYZgFbEefVNqC4qmQ0-DvQElFyhFEH4QecmAPG4hzv27aXYZBmH_yvUYtHlfegCCCOaiMGpLedcsBPW3OP8exi-epaPw5qgIjwZc9Vz-9FuANnPMZnNnJEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvZDYiuUyDegmi7D-H8XGo-usrCb1OZbatOdtwo6mDfVirM36D52aISUz_pxT7AQ0Y9wE3I-KqxrteroL3JVvpi_gUNr3bmhpo5KhXeDyJXRC9nbVG-yvuPjT3EBtgUJ3xSnLEKRLHGWkWqgH2OopjO9bVXIFDJvX35OvLr-D6oitBiu4RYdolQffB4HdLTmT-TtClBgXP_x934Oo83_znfTqoJ_JzCacmYMI3qZrTPGN0aAfgF-R2n-AncSPa2TGS4t4jdz3-XstXl1F0v8m_c5Ll_QWlGrodXWxBQjBRxoJorWkLZkAWx1zDJFAmscez0ChphEGmeLJ_f-zDZ6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUxnxNqQ8X40qKfbTEdjAqOPv92Ab0AhDk5yawP73fBTCZO66hNjC0Z5TMMltdMGWMRyriX9fZgcMmxIPTmUPb14BDmD9q5tcNkfdZ2wHdkFyTeAGPs53Vay8vAqi8kTPFIJ0MteEM2Vb8v7y9rB_7kA0iQ1MQ87ooaSNcYSe54VL-i3keIDQCCpeDx46EoQDw-EdDCPMg_bFN662RrNkPrBFvKQJIJT0MQ7I2zbesVeFpRSXRyRhellYLDHeEQlw0GPnfCs_EV0bALappu7oGAxyxIw6TCpcJfJoh8_kleHx42-9snt9RQ99cQ21Pzg7OuGpt8sLOVtoq80CGTA_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sFiRy-J-jP-uYVdLMEUigDNK05DF4PFlPgaauZyh9bYv4D8xyVFqUUziQof3KyMU0ovs0s8WNW6u6hda8xWXB9O7_82HbjbnaSZWXIz0OG-3TdI0922e8jLzLRbFM1x9QwaWDXr07y2qz6coGIbbAze-2iDLiyNBjqusB8hwmUWn4-bFwYzGibHOnJxLsXIS_8Rv1_OuP2Knp7HR3L3wqmQY-U-WotqpMWfjTA8xSYKcYYupC6UGF9wLLrlmszJcja70ZYrWQ4YK9cRLI1xy-ZrAF2YoWYU3WjxXEN0XEgqCY8S5Sl5mRDY3D2BTYutCLUaIntchVQFN6e_s8Fb4kTNIMWbmCJ0pJjYGRPj4z6XAlhqJ4FG8SDw34p1yNhkTVld9-Py5SeIEp8WCD3ng-H-zEtiyhhJtlVWndA-XamOCEP1U-nEE1SXA0lm842iLnXOBG80RZPzV3J1cbWvbv26113Axhv9fTvja5DLbWJFGH7BEQenN6o9-OVUfsx7G7PDZ605h2mNEmDiQGdzjJxgtoIlYAhdGGBi43wPXoMOV1vsr2-0y2UP3-OCSLGiaVR1-YYVwUZRI8a6MHsql9mVYkca6iBTHap_dmK-T1mLF5hftUV7MVK8oXqB_acOGwsF7L2-WvUVLawxaA3q6WIVThVK7h9J998aeR7a1OsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sFiRy-J-jP-uYVdLMEUigDNK05DF4PFlPgaauZyh9bYv4D8xyVFqUUziQof3KyMU0ovs0s8WNW6u6hda8xWXB9O7_82HbjbnaSZWXIz0OG-3TdI0922e8jLzLRbFM1x9QwaWDXr07y2qz6coGIbbAze-2iDLiyNBjqusB8hwmUWn4-bFwYzGibHOnJxLsXIS_8Rv1_OuP2Knp7HR3L3wqmQY-U-WotqpMWfjTA8xSYKcYYupC6UGF9wLLrlmszJcja70ZYrWQ4YK9cRLI1xy-ZrAF2YoWYU3WjxXEN0XEgqCY8S5Sl5mRDY3D2BTYutCLUaIntchVQFN6e_s8Fb4kTNIMWbmCJ0pJjYGRPj4z6XAlhqJ4FG8SDw34p1yNhkTVld9-Py5SeIEp8WCD3ng-H-zEtiyhhJtlVWndA-XamOCEP1U-nEE1SXA0lm842iLnXOBG80RZPzV3J1cbWvbv26113Axhv9fTvja5DLbWJFGH7BEQenN6o9-OVUfsx7G7PDZ605h2mNEmDiQGdzjJxgtoIlYAhdGGBi43wPXoMOV1vsr2-0y2UP3-OCSLGiaVR1-YYVwUZRI8a6MHsql9mVYkca6iBTHap_dmK-T1mLF5hftUV7MVK8oXqB_acOGwsF7L2-WvUVLawxaA3q6WIVThVK7h9J998aeR7a1OsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jawlyz-6UZFdWw9hera1J5SqlI2RaFrsLNK-BCFTJGwWOyJs2PDF7_tZS0bgM7xsmI0kYGSxpMV_iCDJ65ob6xoEFPf993nxV-qOMcw7Utj8jX_w2vYCkdMnL-UIvTkEQ3AV2MN9JM9n7fu62HOkD8mvN-7oRRgYFL7FvMIUOTTGy-Y5NyhIVvfB50yCf-5Gpy9Fb1pd44BcnNX3WHYrZ5Rb4NJWrdkXUWwhBKVORZI654Iye1qKXqhD6kw4Gie_HntHmzI6KZwcQ9x3QlwBBFrwa8npxPxNMW1J_0nnTuoJ8Y9uVQPB_Drbxij6tnUziLzbymM4jcfDA9u-b5l5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WARsTxry2W0C3HfNvyfbR91_t6AU9YMs5G37z6GlMLY7aSFcnrpdkSlggBMZx4rNgQ1ei87l-kAUW9GTNYLD1Aa1Gq0LZRc7Zwgxd_KqNPE_n81zqwHGjGTIXsZ3lhTgfAQbB01a0dCy_1knGzWMXdWtvhFFkjxkjJV845AL0Lg8O0kUDY0nqz99ZP7VxW4v9WDF2srZYVFWvVx_2jWKxVo-jv7ax3gZcSWjcjR1Q37NQM9qIbl9JabgorbjJ-rJ2qnXqa_-ZW-t8HpwJYhOWt4kOLYkxR4NTEx-Jy97x2YGssrFozY6lqSpSP7Vi111gUs90awlkHczXXCQaDMGxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9b-igxwAvpjwLn-qAd1kpHMtLobA7Mafv50yRUCEfWbnMNiojH3ALh-RFgOlJuJjw-7-4N0LaindKDSuBMaX_Lz2hJTQyF_r7OCwpKcQ_-nbpqmrz6mAL-b0pSP1IW-lm31oSYgyC3faQ_EBhQGSYnc76iQCzaKFy8U1luAiwZL_3tqz4-Qv_5OFTIuXnyVFYHGlpt3WPPH5WWxQbjmWDHFxwy9UU5W2mIugPxzNrwFLmPPh--C9s3dP09KjWl4Gl3bAli6rB15GlYwD6lmY1fEswvWIpcp5VmkZoGvO_cSy1cfWO2p1RlhYhVweBXvJifKWCv7-NVcNQ0BEVHe8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fopDDR6RZICit5e14j_c0vvy6uFlbbQscKntfdcahyCtZrLlzaK9ur0gD2cCQE2abdbS8JzUy0raNbdmCT37Lf7ADORsP5zc0OQh4gT9QJcr7b4Wy1blF0u3zIeDCX8L4ILqJ4EAjqpXHkpXAKs1f-AcJoYn5wyyO8hoTCwNDzJeYDhXhVQSHo1TwBqgc_SHj-ZffBiG7uXqEhJWmeHqc8Xd9zOGrxwms7Uk27VpALEEDOKXs_NdoEJDNSbtzHDZqda2ZdKehBmiUQ3zkFR_gUlf6o8EXCAQaBGVdzgA7IDDXcykVfPYUhiuis98TUjbM8oFKM7LmoE45tqUBAIcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj90ZGOyq_iIKsm-FkIfREKxvNKbW3gwglHbWuNrEymgqkoVgOh7_szo3RIrOzvTFWz2xA3H2rely6GQN26zFDz1x3_LCs2-DTAT4B3HARdct2jGkuWqR-Ji2iylqKdvfnab5BRuVG-8Ya_GQP98GuQ1P5IOg53Ja9mEfYtTXWgsfvSfLe0Wfr6Yk1Zo2SEJAXQ4y37sCjOG6U7G0TmOp8dudleyVtXSit2azkFUpgsENjnHcbNU7l0HQv9VYY2FwnNWgHvcT30JCK2LWrxb7j4pD3pVBYvKTqveUj8jV_6lKDkekfYtnzLaFTSCLdZBIZm6mezOdkDCmNSuQwJiMA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ty6Jy7EfWN04TMr3tkkext4sBuZlel4ICW8Wo8kIzENuDJxdkn1aQGrmQqtmSVXbvKZkgRIN3XbOYBitun1kdzda_jeIqOEzg3XeO8DSK3kF_9QS5BHUfCquzK5y1wtbwJ5EQjisFJj3J7-1WcXwN6-LkKc6yIBAFPII3RoYa4WBheybAM1cFLnC4N277h1LMmvcL70mc7eO98GVZh93SlDN3Fzf_H3fZBS78-3qZMNi7RIpfHWs3xPeviafkZ4Rg68imXsH4y8_8c8XtIrFEICK8uPWlV1SEWrVkebluwHrf86Sv6h1InjNJT_Fe9aI8boAJ6U0orIIasSU-ElwPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Ty6Jy7EfWN04TMr3tkkext4sBuZlel4ICW8Wo8kIzENuDJxdkn1aQGrmQqtmSVXbvKZkgRIN3XbOYBitun1kdzda_jeIqOEzg3XeO8DSK3kF_9QS5BHUfCquzK5y1wtbwJ5EQjisFJj3J7-1WcXwN6-LkKc6yIBAFPII3RoYa4WBheybAM1cFLnC4N277h1LMmvcL70mc7eO98GVZh93SlDN3Fzf_H3fZBS78-3qZMNi7RIpfHWs3xPeviafkZ4Rg68imXsH4y8_8c8XtIrFEICK8uPWlV1SEWrVkebluwHrf86Sv6h1InjNJT_Fe9aI8boAJ6U0orIIasSU-ElwPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC_RKoNVYP4UTpA4gfmi_ATqoX7iL7YXWxVPZGODuidNMAnj3dtt6cTS9JywvC4Xg9JtUsMxOjPAXgWlHFOGPRsKkigKXlPcBMD4NiNG_SD8ZJh8NFnyQI-fd1BHk5KhrAn6VcduvsO9XKJUnd7pLe6U3BkhfxM42WMUYmQNFgP8nvXc6iweglmGiUACggSOJV96FYXXydvjGRuYBWIPkPKpGJNpwmVmUSqD8DxTgweag6Z4ihtP-RWDsHgDr1jYajnN3CF0r7HrxBh_C9p77mNYb8Pqdd63zffowzRRRVjP5BaNKiXpEodo1L_groyWvwlQn6FHhPwbai7pTjE7bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJrMDFZEbwC7byZeZiXwGiEDF33oJt0JzEh1Ai0ItWK9BCUuZrbqJImQIgfYfLeM6gfF02ejkmWbKoWFHVdAY3kCNO3F5ZUnM_HA3HN_QnpOSRVUzCoXYreswQCRbQj5O3-ClH28nnIdTg_SsEVr8IYjYtjG1czjmkV0gesVqo8fil5kbOtgoVOJG7szFsh96Li1MDsJr51K6XygM9KgORRVL6NBVxhkn4bYCIeE_56o5zqc6C-q6NWRVvP3CPnVTzg2i5wg7gyPCgoVJvC3lwAFi7KMKOCr_tuPKzmgq5UnNkk30wr_dyavUaWKW2LI2Ejaweth9OlUbIpF7JUquQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhT1MpmoQlxSqE-ML5hmLPHfxb1O4FHjCj-WukheAKpRpJdtWpnVkFHG4lZE4-H0AFg4J5TWX-Ezflhn75mCjaC64MrYBS8jo3HFE2a68UA7CksgQfh-q6I3kuGXxP6xB57awBzf30dpd_VtyWcpcsC5NJ4e-TdWaLoRldwm3mvQ9Fq5pTgITKlZld-EvkS-XMgVXXSUYtJmuvRoyoqCiA7AHjI5fxDdO6HCzDRxFVx05GnJ96sosZUOjlb25EMjnw4JuR0QpjIZhfeYKHFM6-mWCD01pMXbMCFB_UGprR_9npuln9zxJ5w115BKAI5gIE0UpczhgX-H7degX0YZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu-GG-AMxhUqk8J0oMHvOQ2d_p5HcAymwhV2HwiS6tQA3ZW3AAen8VO4v7fUNrs4vZEOXhVsRSDq633wn6lNZ_DK7Tfn-g5q-kmb4Q7CZv1b8ek5RVV36MN-Y0H8oxrDZauVlhX8yWkFGYa31GnQx-t6eauJkV0LFainK1dHt_Jkwhma7vKN0_FsGuOxJ4sYCMxYPwlHF0yn3qw8ID-0rcvp5Bt07-m7VQ05D6wvGyvQqpEn78gKF9PWw4aS1Rb-Xf3-KIazktCKP3Yqp1h6I2SPWN5RscvK4gJvRA7yxGr_QdEo640TY3MvP1afd_n1bLvumWLpzyB0gxhUEaJd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAdQ4UHJKTbIEK05h8IUXGvKYmj-9JKEAX9I0157EWu9gkGDF6_CAorjoDtYltA2p2ghNynsJS9PD8AZXq8D5DAd8tBKr7-NTefHSnH6u8TENDjIbICwDmqwKw3AV-2DTzFc1LhcumasWLXW9nDAGbxNMHTjwZWczpOYw-swdHaLA5aFqeWoJKWqWAHmp1Nw-IdxRV_5IUbOuhsBxEIiiPGevRHYiEeEGAyIFNrUxIsJjLckgzMUaWbWu36ZGd4rZ0I1BrP6Ea23nvGaOcRuk8jO6Jr1D74jfyJqVu8JG5GS6sbAcu8914syhjR1_GKqzmQkBNMdU3h9gwFYRM5-Kg.jpg" alt="photo" loading="lazy"/></div>
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
