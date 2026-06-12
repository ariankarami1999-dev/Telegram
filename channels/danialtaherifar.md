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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 279 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 321 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 382 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 507 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDPyuAD6yAVVG9uwTek5XclXgh-xtOD_PlspGsldOFa5aynas19XXjOq_gjenK30W0J59YhCCAV03fFbn-L0qCYMnxXH4eCOrs8QCwWXLe13YOgUngHJm3W_KGLINz1cL1Sm3n63KMq45eKlBRxYURc_V11IVkASXALe-oJFOw5gPBI2SlyVWyb8WsiYPhw94LuK7hfIdlw-urU2hCB3w090-6WXBlwkhoQcQJcpKeFp53SrAWVhCEg2zSou-vdvudRPJI6gUo0jFAa-wYwvpLfh3r_hlCErup0q9cpYYI7AlmcyOrGqA3UuunAM37H20Pw3ETNZ2m6GU9p4JD8MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 979 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHMcyHOY5e3uIJHpXcFcUnvQv0yfCPg4OG37z9Em9iBWTo9X610mauI8s9WlMsoIDZp_llDGHXjMqfRNP9iVGmmQkRGm_QEOeVuVeA4McKXPnMVVN2n5WJw5CTuyqCw8ra8Gdu5xhEuR3SPanaadObrEwkB7ChYa8gqGR0owz36IYYI5N5O5fT66uF0hrDvLGXPNij1cK3UIAgG29D_SVugKrr0NEc0lykZ9U_6rzBBGFDLE78v5KuYBTRPgO_Se7oUYgYsi4z8YGXBG6gpXLqXKHJyOWUiBt8vTjQDWgiQsKaleEj-tpEe3Px7A-gWBC7MKRtwa0gfxP0R6Ayv67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxdI1A42TXmqmp1wgThncU5DwQ1PW2Op9xufeis08jnyEnI1hF3v2bXo5ZYh2uBGHbM4FfpTe5rxGOJTJ-zVIL2T-ebHlmtD3vcu-O6Devkt-IfGfhen2oX0j8Cng8fTkWIe2Cv90LFVDG8c_AtzbMUy_9i_I_j8X9O3gJpU1wBed7poDDgVJszcnf2eLcBE39fsDBsLplZWkcvJ8xXp7SxPhxW2SheGXpzZhOO_yswI3xZ_JJ5nwBHef5p4C-HtqbeTAgsVTmamcKZMpuF8PSjzsY0rppQC0_znF6aTPSlAHZJ1C8ohEYCTtY6phC7linT-a5fSg4xJDgXWetHziw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL4VW7mW62W5YbpwZXCEdgebJsbMBxNeMA2bVNL0vCJcDdQ9E6Fl_6mfCXkb1SZBUx0NRV3VOpcW8xyWG4gSx7FMu2WzGqdZjK0agoo0mnHrV97Qp5J5t-zbe5fesFSX6sRFk6XcHH2f8CVAQUqoQAarPUJDr1AssQcZjK55w7iEGAaBPQOtIpl7y-gMXCFiRKmsi8YYeOOKkrduR-MqPGOzVa2QdRnDPxy6EoRSCl5Sx4_URb8Kf-K0RtR57ms5KKUBi_dAPlOf3CmwpfM8gHh22oXiimhhdrjoo61bKZbtkwoy6bQHrNqgLuuot1EUquw0OBMoPhpxhvA8-vXV8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJF8Ii8i51UHyTLSoEzUYNunI8f6aEVjg78jo9KESvr7nKOheiWqNBmMrwnq-iZDosSeU02M5za5ZZsy5vMNo3iS5fLtF_4m7VvISgibfv1-697V311_9J4pESh9CmLkPv6kmIQauvSLBxIbJgD0cI9taTe211p3w5SWaG8fgRU1YyOPhGBx8UJ4sGakFsCoshj69K6dCFvkBnrr4k8-_fcuHiu5Mf16u2t8w5GDP3ZtR4rB7QdF-dwoiZZtN5wNu0jzs7uwlkUeVSgmhw6RU90tmokl-dIMK5mcnQDyvE_2Ps7NhPZq_ovdN0axRbPnCoT6x2EDUM-5SmqeFgBFsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/floO0G6-ae4sPLWI74UoEpvNRitZpMY2-gdH0hWiqhvnGuip7XYaDxBS0GYzhgHOyOWi8dj4bOtccX3yiVZx5rZ1_1tM6DAH1q94_n21sD8rzOl5rUG5DLYEfjgUB5oEZRdIhY8JQBPVfTo19SZsmnLfnERFccqMMiRaKNej4OUDeTiaMBnF4eGhF02pq_YwvhIGxWwBWUcrTF28zn_nv6KGCsXEKDSpAB21p3vJRHxtZxLYuNtChAjm_YZd5f5JHr69SjB8roftPWx5LELyUjvPLcPcf8ER26d833NlZzjbFL3QYTyc1QFEAs8NcVsnmDxPCZG1-xCLWR0x_H0vDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKDmtKpuHPRPq6BVWQXA4COOGsgjx_nv5lAr2xDXMVTqLu25NfKGGIl0BbmvTU7xwYo2-wGFpbItKf2rfid290jOJQwyslU2AnvsVuzYU0Iwy_K07RFFm86vCdOS2F0IsDg8VA3qUp99uVJn2I35Cdx60ceS_eTSZQzRE_vVJLGAooaoXt9GJ3zWKyrwYaTbNhDxxMYI4Qpy3XwFinmPoO2eV5K44ofuZadCfqbWs8hhUz4cMkIkBi3KhzpIJcYSfXoHODEphtO801Rum3n6vujK3SGzM-_dwd4VbcgdxByQ_N1Z3nCKqsrTKWjOhANfg40gT-FIDSpY12aHKe2Uag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Fd7IDT3fDF9awM-lyTmtFVzhlmR9681wTic5abJCDx2UmVEsE3V0ulfFrOi2FVHhbrJnrLVsLLhBce_5SUtE2JC9Z3yNRFz8K3O5A_zjD3RAZbZFY6jYfWnP4HRxaXjTESk110NO6RA8pgx9YiV6DFy4OmT7ua18GfRYB91_qW-1cHk3rMrxvA7EZ1HydpREwz0qUevp_8x2nMvxlKc0KesgbS-3ZDsfEj4XWWu4h4HsP58TBjNuou6mZIAPofCKfNnxsFU2ZBkKqiJZlN767CbqqnfYlnwpjzDrI4xIkET2VKSUA8_QRsiuiUmWpHrqrrKPzylS7lShnO8Xd8xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNv4fRakEjpKrPYQRtzM3nuNNo6aJIJRU0hj7HeTRVkHaQdekSupCqfbLV4I34UBEN3tY7jb9aiqK0Aq7ntTqfEmRcZMe3BdnMk3zCZrjg6dzVMNzvdlhSuMkJNX2s51L4Oim6JYztrblE3WcSvqZKpy_dxpisuVgm-qxD7JGGz-V2LZhPYIg0NDgBUht4h2HB_R3RQEM2qJIWRJkB2jit-4h5VtBhOo8Yxthx_dbVsVr7gn6cojTifYq4WkXZEqYsGwrOeHLdWQ8hgvqzxsroICnu4ZIm0kkY1OLPzGxw8qr5_DnJiWNISNeIlWn91G2f20jNpiQmBDOEb8xTxHuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-OXem9GgBpJk11clb46F9_336iTzsbJ8AcGDcoOm1GjeU3AB-BXhZIqO3n0irw9ihUObsFQA3Kv14PVa9h6pvZ7zYrAQD4WhcxnKK559A0z4XvvU2JjbhTqbuPoHT-Z7hzifNmM3P5b6jJ0MugGBcs6KPkB-KU6RYUSJoTfx6aL_2SPqlz3GkcGrNc6Yl05LQ2fduoA1Gd1ENdEgpCUXEwFIUCGP4umU37fqdx9Do1098R02sF9heshgfxpi81MslsHI2m0pMQgceWoorpMT_Xcr-2F0RSckccIyc03osmW32h5PJ-mY1eJwGke_EuPLgVezIjqcfPEWept5cWF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyVLVJ06RufXWYetltdkXziXrk_WLBNWOILtdN_lwDyGMkXyJUi8MseGLMY9E7_bxBTDb_N0GkeF3LJj5064JolU_vqdBKZz5FzLXJMnKDT0-QdagqIHd4rpZj2scuPKgQDpCCE26tbJ5k9HMJWxEghAptVnLFepf1gxnkC8vr_n6lVckvhByJ6dNynCkw91Cev6mD1_6ugCvG4og04BJTM1ig9_pKQ_5DE-SMrwGkdQ5gJ1nP73uhqFEm2pt83ArgPPX6rqTYOBG85pUee8gLNcKfewdnlmxZ00AYo6ivNKiJNMKT0ohuTRZMt8U4oAxbdAA2YsOBft-q8RQe5UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhYCodG3PQKF_KOTo0aaAQgZT4L-td7Nkamx1wj3r2Dgmyzq5jYJWl_6V3rtyHSRlbSokrrl1V06_CZFB-u8shnKfuqsWlV3izmplz7My9-2UNsq-Nc1mvFTF5-LT-pQRZx3KR0yk50TTnMt9_SbEkBsRni73FozsTXpWLvmAVhaNNISApTIU06045BLMnEqFCmo-EAISStucVo7uRh2rim0CuAs_Unf7CHLpg5NwS5_-1RdK1Ph8Wk04WUuTZQdOqcY8ojA53zXiHEAtDivhUpVef6oYoffgBysLyRU_LcDup8Y9bMuXuN1gRgFxt-HU_wUGw8u96Ovp71dyJFytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLebuExlDLMGjbHjR4Ss3jf_329oPts814M2d1GjtwobH8dWKldWddhlBSNXG1aImqUH2lwxb_obPQAXWmoO-F2WHievdhkRt214gD9haA1CKFDyewN0G4m7N8DytbwwFG7fPHkrq066mQjlbiINuaM0ASmP0fNxvtAydkwDHhj5kSVbMJoy4Eirl8P_9KTsMN9Pd-FWZ-LsPuwrZoJHLrl8Zg_xUyro4l8YBhlZlHviLIRtE7O3vhuQZ-7m-DJetGsUjzQ0-aeZaf_0ytLaKKNTqHsyLvW729LsLFP9JZpLVt0hKR68nrxl3EOfqqP1oqmnGicNoZkEywNZck4gsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKlkq_tM2KY_rJGdnz9LYfZNvgnCtBm_rk_rgPpUKQAAtSpXNQnEdJIZOZ-TZZqcqyXEvawgGhrEWNpzIHoS-h24znrEzmn0eecVzKsa-D3ITvlsay-YRipW-qJ617G210nz8Derdw8eBlNtvp9A3NLOoZ7IXfryVP14hIBvOUWpnYd-h5sUyDS4Tx7O3HXEBiiLSZQy3mAJxcB-Cssk5xH05uSOeLTvsiL5sABeABIx-KeNr1xfc0aRyBsGSNzrrIqKXysYSpBWCoDMMPAqZKnpnYBGvD9dt0ZokuGfELEz1ufvMLPD6NVMSC_WGaJdrGTyXkpwHVvAdOmhkHgOkA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=MieGXDy7r5kB7444AihNJCyGP_m5nj9b3EgPzqOHul40Ne8C-h7kvzBYkweQzVrC1YNB-dbqQhod4q2mI_DyvgMthpcTIJTAbjRxrMuynyfrNfCZAc1x2sXILGWsWavf6O654WAEoMeSlWOMMOk7xH56UT0CsCs-OHjlRzH8kS3U72H2K4FZ32yb9geKZGZ50tFUFqbnB948Ji_I_RRx4-H-5EdLQHpoTUMznsUOa5_xbwKKsybO8irYMLEAmYGG5JXo8rRLOxdaOKc_I_LK615XYc9Rcpzy5BFcoLB8B1ZnUDl4wLu7-kMaCWpZANILD_LooOKNcgBAay9GthW12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=MieGXDy7r5kB7444AihNJCyGP_m5nj9b3EgPzqOHul40Ne8C-h7kvzBYkweQzVrC1YNB-dbqQhod4q2mI_DyvgMthpcTIJTAbjRxrMuynyfrNfCZAc1x2sXILGWsWavf6O654WAEoMeSlWOMMOk7xH56UT0CsCs-OHjlRzH8kS3U72H2K4FZ32yb9geKZGZ50tFUFqbnB948Ji_I_RRx4-H-5EdLQHpoTUMznsUOa5_xbwKKsybO8irYMLEAmYGG5JXo8rRLOxdaOKc_I_LK615XYc9Rcpzy5BFcoLB8B1ZnUDl4wLu7-kMaCWpZANILD_LooOKNcgBAay9GthW12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4WcXnnPqM7lhWenUW7eqAc3qSG30zPdZ1_l9b91tKbuUbESQeF6oOPTkYABcT_w9a1dDOFJxjtZYEoEZJoMj9w3kV_mx9wGWGlbmW1x3E6MKpobDCdj3kIyxeeEv2KVHATWFuhOUNNlsjWIeZ2r1zxQAMFSTKxVIIk5YTjXO723-AA5BPstGmpfK_xPfn7klfBpIlk6wQYPMvXDyMH8K4AUWyjgWApxsYJ53eyf_WSkvi4BbFmL3pDrb6UUAriQUWlwHk_KJqNVN9FkzqDTE0pJeBgb9JE9SalGuCpIBNOE1wGHP7vggR0O7YvgZjaeZrbu8m2VmbthDgDW_qVAwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHe2QLBDxsCtvsR0x9RPXXYEEFJq7QL9mZzp2LtS9q3vD1UbsFRJBS_0MmRB73rl2NF6DwCxqZbMhD15xPqeVVtgD0qKDCskRqDUuTc2Hyr7GeesOu3yMqdFGsoSozCtebcnADUcWErzY5_evLO1UV-Rra_A42QPLE1H57S1KDsm3jO6-kIeHMTjHMMPkN4j0t4BVs56XqG0UaY05GGIDGEzHdLOVRLsxZIPLLYIVXN5XbvEChPqtF7cOwike03OjMwIIw2XjFU1cVGsexYAJFO94DlLb8L6EIjTU1mESbYljZeipO8h_QrdDqg9ydFCgMwSTmDhHgC93KdYTj-8Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3RLSQXTJOxxNvyyC6cz233rCEGf_QK1cBANVGKSo__QZCBJlJRz1B24OIj3b3a7WW7NoXPsuLfssChsVexCkZmsvcdmMdCPuD8uY27LdZX5ZUwdlUVAjcHi47DeFZDoCB-gfCIQnxQ14hw7jl1xtRg1cwO9iKibtb8QdS_RliTObHe_LhQSfR5DcKfsb4lRVDM6EbGbfDy4SnfcJ7KkQ5cCIwjOseKfZugz7t5SjiDXwsMbkBtsVHU0q0ZFGWNONCpqwxrhS2ddAbpZ0RVPLbuTMhSrBrf1cRWr6qFbSp1NDwl-D7DrbjiP3XBtSXeA3Z1oc1EsPbrsA4axlcglxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITEShxw6DAgEFowkj42C_Wa2pquW3Php5m6YYe_oYE5HCwK1UnSCocx0DTh7k-8Rw0WCIcE4jHH_v73Mfmo2KGI-aPGoKh_m750D12S3KvhKMLv2uUcXTs91zZVYO1OY-xM_MPba5hrbLJi-7hTjUh6YXcklbR5GEydSlhsZuXbVGRXhilm_hb__O7jD458z_NxbNd3KZRTwhrC7xuZE1ZgyeMoK1HvIVTmr1fd7m7-2asafjiKDJUMEyNwlao2DQunIooBuScZW48_KO0pTbINJxGVm4WmCzOLMeKnHfcxeG19yTcMxwjyEm1kOSlrm194btoW5dt_Z-s0AH1LIhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNvZWTT40vThMwp8qfg3AObknnWDsq4GF9-gymDlUWcKp7dQkPYSkUUUbVqU1Tu8B0qoxhXB38fEa3MP1IS7Zny3-Ogm5U5Dv-gNVRTu4acj5Urb5_7-fc8-svC9Wwc1DNzFOwb3NadEg7Te6dA_kK0XoQ0agLIVt8mCOoZQcqQIyaUziqZOdO8RVbgcemMMnTl5zGER0BvTq70YKS-rMdEQ_xtSRY4xH4WHOyWrFYz_1EEaU5L1XtPgoaqLK-ACqpRfu8k0vsXAn35DRMs4zW8mIHXajhf_ddqmPBmUGgyYmF0zLXxWWdqe6CmC-iy9acp7SNSujjoDJxE2US9hog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkB46j97xs4mT0E2XJi5Sfr6S631_Phi0FVyFCexf3exoWKVJnUkxZrX6J8D-RbceZV5g5SyjZuFP8bvdccC2SRk2jXwTwTnKO0p4eb9Yxexp_Tjksc99SOPkT0eTJW_8cJHnmzNEll7qMs5XBrGtrAMaWO5ueAYaXvrWkwUQqo52JxCBDsQlcaOxvFUkq-_rBj_WpGOvjW9k0oHTB-IpCvr_oHpbhyIRGihGlnHcUDAXdA9I6ZSMEH_IDQayuaLbeqPNOayxacU_BOoVVjWHt-ahSyx8OVA155j58q0332V_9JJXd9XuKcqQqGVWm65SoZfScYZkBLvQmlmQ1SoHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZGwSkV6emKBR1ZwmV2nRetPTkQTC4TH1TlnemW1EgV75Yy5cGdVkwBLSHw1ztOVmX_hm9VsBaNT8ryDscR9uF9NVcnqyGMIVhjsRoDG42tOtNa3assP5OCpiQzzLKBmdQQk8BMCTZTZjR7jhVB6ijZqagdgYuah2xlopA72epROqe_ZkXDKd9GRqPWSQhmghcYOwNTxbjDfo9c8xjEXzMy2a0xPXci1L653rEzTCcSmZPvCEEIstQaHGHhqr1p2nZNMHZ0265-pYjlQAPZIOP4ZJncWJrzBKEmUZriBeMUoBcZuBRfd_Q51ZlmT1FKl68rUKnGcqf5OHL302ukZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfMOY95gLtVYS5z7aKNjTfVroUESojFOnXpcgClZ_v8lFODQPiO0MXIGUV2gkCIpMupJ7wNSat-wVrB3dSppff2w0UWXIF70ALQEIZEQcug6LhS-wJOjXpsWOjug_I4nHvftnHP8-z4ILGpyd-deeq0wnNYeODQU3-Z3ey8twkdijoad4DX4EslYtny5sK19S76i9F-42o9X8tIGRDwzxyMeSrv0J16WMTLauwAUsbrqxsHabEa2XFMOSosjF9CEpUbZU874v69Yj21Xbhuz2c6MXE4jdcFl7n4sJ_x25XzfRwyG1_CQ9o98ryb98YpXjsPySUvI6F6DkxDu1n9FMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tclCCGKDlaXS0kXahiJNM4jPgjzxYUlWuIxV9UANkQETCKeRLF6lX7C-oyS8HmwOUdrZ5f_Qef4Rjs_uzQXedAWa0QwCib3exyqG824OcYTIWUpv-KyfKK0nOvT6nLyKoPgi5OS06R9ahNJTbDNOI4C4TVTjUkVxgEF_o3-IDzDGojRikotxrncA-ytb8IfCQzvifX2t1TGhT9R4bA1fnx7Pt2OESqQRZHDukahO6tZlSuIzudsm34zhHNEr75wTsy_91fjVZ2tm2LPhUP7GHDzAIYbyTtPa4ZGHcvJjZT94xYJ69CLg36ewrKWsT3v6fVY2SizR0DVfzEIvb4VS6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohDgX5EBfHeHBCKc7nHmzqOyOlRO9BB7wSNHy5sal5Sb9BJ21q8d2rH6OCDMM8a9_lqgsiV2T1BLqnYokoOTCHIZimgAfqRyJwfFuxlHN-VuBJ8AwNxmZUVyIvUXdONefOGd5LhQNUggjzd2nHziMnv5T3ekg_jNdpxhw0DEvsK3PDCC6JctFWp2agS2liDoY1kFlazH6chK2siolVD5BRohj6LDTi8pxmZZNJ9SFnHg3BAewkB4S4ezJU4pvJKlhhWMDNsqtPCP6e3e-jQPMM12rpBIXJa9fX8OxrpeEnDGr1NvRES7RIuc7KfM_0kgGStZB8mXV68lpdrPj0sO8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQqacUc4G0-OE7Fu6xRZwxx_Nyj9aANCaFxNjkBsgNjKZf6c0aW7q7dbjGSxA26TgzJ7l7ZkExLujIR5fIpXLFfK3Q_uZbdE-bCUVkeVmvRD9Pv6mnl5fn1rl0-Zx9ortPIHc2letYOliDSgHeFpTgLM9JseAI6IClGd_TGR5C3dSbSWvu7Sje7ByFM4rtuQ2LF8wR6sUoZqIW4kjGywFdEztTey7lJDKodI9y-3hPzc1_ITboSXjcUVgE7todbg9qX_6NAbzbuNNu1FvIZdvOPtmopjZWJ3HOZSz9dvxACSxzc5_59eHSjZ7sy5w11hLSqkuaMGMQn0ZjmrgoYklA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoTSwGGGYlih_pLdQwnKcAVDcQZkhmbg7YsNZ1sDOhkczZuF63UqvA9asKVLl4zBx4pXJx_uO1AGhDC9HM0UaL5oVS2DqbK1xP45YQkgR_kaSynPk_MQGURroo7Y5tg1oSPXFN-t2Q1e1ncAt_ukpqdZvt90wIy1nKlZKrwZu1CT9ed4egPSGTys-MeXEsXzKBOnu2WOfFc09lIrs6BnnFqUzg6aE4d6c1AcjrVcMziODZRO_UYD_mbzzCrzlHjGkc4TNq_Vy20WbCXn_BpZECECPC63egGGRRYRC32uyuNYNj84Z7t16yYWGLvZfM9ZJ9ubVP0APXpMNyRWqD34uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egyGFLPAd35sbN5lJ2pHTGtAA_Iujc2x6iDUnjOBNStuQqsRi_2oMYRqOZXkG5FsxdSBtHae1h04tfRwyo863fGe7yd8S7ymHDdkr4P4UvBMHeBQXLoshzyTcUrycPw4X19TCLlh_ZwLSI0svklK8XzMOnNK7fs0yGlbW2fnzClW31FFSDr_mcjsWOn5S2ez4Z0kLoBI9TxwBH_04yTSZJlCm4KyDVkOE0rx_346co6Bb_yQbPWNoBOKaeNo124HdQaQwo4-B-bI1uhk85HYXXnqVCcj4BGfgzbXjuOACA_nXHQ9oNxSKokjniw3iGzMAxqDxBzCcJwXPGy4au3Jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLTuspbFVVokLjt532SfKKwrbLfgLzS6Sh9PqZDaSBW7G5KLK1EUebDdHohsX-GyHrJHT2BCzOHnUFW3EXJCBXgkDJTlceCkxsPuegAX177OSLxhhTxVlifeg_IpBGFCeqSC68WeAWE4rw7fCE4OOqE_a-TT5mzLtoZtpRFP33sPOgQdalL5uHWBYeZ1FTCpqj-CYPUPzin8Uw321HwJCJXK0okyN2PW0M4L6PKTx3Kg70KhiLKP2Bl734lwkqItjOBhNtwNCvdCY_DOLbg6jPC3AH__jCwHDlHD7MFAKe9w7FSugQ5Oxpdwpk7PxZP2fNnyfv4zyBtwuTIXyulVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHphzU9GMQ0FwVixmMR_7HnRo_fMUDywKUOJPiL_DEetdtLHXMZm4krNBxzhhoiLXyC3TWLuvzQZam3x41ave4fUB4z489ZiBXsHSzEYlZSbW7JGoJ1jibgIAV8sR-SURUI7_J8d8EVp1tbUzvzNG_LWrcn7fwNFmy0X0Vg0UooK-pwTyugLeKmzUuR3oII9VVpYW4ID9Mpwr9qrez507dEsanA1JX2O-zvu_wkyx3Dk5S_OTXhHw5qSHCRviTU_H_kjN-NiKc9GGvr0eTYXy4CoKlF9tVVwmCPK1wsUP_8urapOUz-SsMJKCn7zTIOLIdiLdL5AjZ65hArIZvdX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qb8UqGxyYBY_uz8d5aaOZI9UKZkQTEOlZWug8EYsWqYd9rejTff_3_GbuH8JfAKV8enrcj952_xoEQnyo3DDulJvJGzfPGOBg4GEWEeMKo3V8i5djaPI5iZabD-msGcTffdXsux8t4a9x6WQPhPQewZ81y818Eeezbtlf2q-1YhphlaP7jMZFCTT9u-xzX9BE5NWSYdVl5SEt4etFawVn9uzHncx8RQokUL6LrCJmZh2EFRnAcKKIqFWWL7m1jnKaEO4Vlrd-EB60MjtFTG4Oe3B6GupTiCLIpoq2kr9xUJT92nBhBCAwLq6MFdAeAAG5YT7wnvCnWAzIX1BDSVWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlT0cjXBSIGjtlNESuKnesrqHfOkdPlAGQA9xOmBb9SR-wffSFzsfoDFpvqYy0LZmC6qKsXR3K_Tuc1M6RusxZiIhjzsl2XEzEhb79AsioUiI_dHBo3mI5sX3eoWbsXZmjUlLi0vgOHXYzPtME3_L-PclX516H0R_DrKf30mToO0fyVEpd9jDfhY6bHa2fD-HAPX1632mxMuabJtYQXms-4Pp8pmWM-0SJAlPqIdqNEUBZUaeSWI-76VatReEoOvgdp9AQGKHDNpu0fphxKJfOy1wzvzhTMDHCAZ0NmpxmXUimcnubICGOW4kr8hqdfJQEdAy6B-unyO7mC_TcZSYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8HK8nmV2LhRK-hxCnbEpwwA9u5EbBH62iuC1PChlCHdx--Pwgs88dE6qiSU8ceVxN78tPcl5bZxN4wcpmEcPUcrS2g1jLk-4VFlebYJ2TBPhuMlbKOyazHCwrXk-mo3loprbL1JeK2-BxDf6Ed-hXbcAlCZgzousDe7EDOJ9-ZFEyNpPcEXrbU2R--4g9rSi-G5efBxS_-DSqtYmoSJDEpCu76gTHBabHr7sjd3v7SvQVG7FNv5_GfXgdEtrA58GMVo2DXriCn-xjvyo9MZt91p-6yXwudQFHevHNGIwXQZb5xJXsvFns1N1AH6932WYYE8FAHqWO_dhRtU6ZEhLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBM3bEut2x54am6yvMMu7jCjyL3rJ5-gkgk1FiMrTOL-amx2p2BVIBatc3jJjRCX0QYyhOK2LlVFYAjTwqR7GOc0O9ZqWBh8zlgPsFe_SwHZx0erhicqCqOsSy5TgicEv_b5DKDXOfkpWFWjM6KO-6tguuAOjKW02LfpGnXSc9HI31SbEkzUhtliIaN93Oc_gweVed57ZpPhXNwT4cHrFRFvmZBQJaFvCl6VWvnQIloZAn61GZoz0WUgIj2GRRxpkuKAjQEjI1sWVMRxih5SZBu2nqA4glIz9UGyevlmXgqxzFdRslRNWd6kkmjf0n8wevNJ5_-C8LsOWfV4i1r_DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpM5TZsbwdicD8M2_sfLbDq91QGB28ZplVlvYl5BZpV_DiJBE70hmpapSjLkgZS1JwcPLLnWmRZM-YooX5OKdRNU6ZQos5u15vITst1lMytySxxaIoMcVq-6FQSV0esMKr7TWikad6lxKhIR4KKFcQwVow-gXnTPpBjY-fTU0hVw6BVE4b65-VmMp4GdBcqciv5c6JdErNmI_q-BUdQ4i54hYuxJ0_IqM_4Nm2EqziJmZvOnTDmo8mZ27ekiTDsXuLsxxFU-nPLNWmjQX8OW9fixOLun9hDQ2HMyGW7byWWp-orT29FsOzWTTd3QGy981sQ1rBDqTZhuQr98OTCuhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7g4OW8ogPxOZseKqk6zXWulPzuzHz6EgmL6vMkgsb2ayNB0adH7cBuUXykdWy61QZHadY3myZ3ulJRW_dq-2E7_EsoPRZeqs5E-46c6hckc_lAzi3DAyEU4L-LiDtls4MEBGbHy6nRrkKw-0qr4urQA-vvaVc32uxpWdYAjcuZJv-mo3ZWOzgAH16ByRVxbMPX2wiuK7LRL45he89QIXK1xs5FWItxl2DYCZNofqW0yZEiwwIXcAkZfUQWhgiiT-ucoN9Qi0Unlk3Xis0--bewvVzjsQcYe4Op6OUtgYWZwxKkC_oi98Iq64qJew9g5LjlghtPLEfNCtTXYaYnszg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhurEXweRYdtb5FuE81Mx7xO9dpcFWe8O6-U6_AMB1gdm4y-wgJqhnoXAZGfFhAN0n3fBj4uRAxKiAJRAwqtDGOnAeczSPXA2c1ZxkV78xMKtQOT8M0anFv7kUXR8b3UIfIcDvVyJJt_TrrTMoDE-iSz3ztxgOuk2oxs9YBU_s9Qpblsuu-I7PDnPkYbwxhLhGrC70NHQ1QUQKvPiTUuEzesw0eJoojs2V27fIcVnU_vFRbgnFleqxpnhqPRheKkNcr9Yyk2XvMbZ-htmezB67wbpyEQpdQxxxeGwgXaNvL2k2Wi4kJW2uxKBUHILg18QchUPJekW-zOg7BuPKmztw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7CXK-yb4ReZjTQVfYGgyY_4duaN9Zyz1HXIJzCHKo770ADljSRozvD5xnQhjMeEW7B0DcwbrYiJAvmnoMiuPuKA9EtuFUJJeL9Ypr0PsdMUFlBN6H32-Xobjp__JmAjC_ZbcTp16LqEkBhGQs2fucG_L8FrfNafFt_EGY1TPK4jSFh5ZKD95R55Ke6m1dCNcKIXVcK6qiupMPN81byb6A2Z372I1d8KaEdgEz81zm7OYSvqfSN1bc4lGQDNv76F_htDW2v6EJXS-tmA0fB54EHSUAQD6MBBao6oBKukF6UyXCb4p_aheoivR8HU8-JPGN9h-kAgKBrL97keb8VjDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRjQKCDHMiYeRTb4lfgX-A5Gaye-5WNCYjESnMnOzVxf4N00T4QCCF_cjxD6jepy3yWVRCLfFEyNeD9KrKsS9Lhwiiu-f_bZVbFZqxnlhW9EGiv9eVPMsLgZjSUkI70V8yuclhh89UDjAfFiiGqQZxKa3-tN70cKaYgqQlyOsim5Okk0bvzc7uHEkUlyzJ4iSaHOkNRUCpQ0AtM9Zv5buOHeevWPfpua4HqPxaHsojUFzUXyqcOEoZxaAEoXY5wXfNthRHQLjBGlWr19PuEG88lVDVHuJ9c7Y8vmlJHXLsxNe-JvIp7OdrbLjc_KE0fAE_Wp6OqAFrfTHRQQJBZ5UA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYOWWEnZWUQc6qNhQV04mOHbiyv4r2XnlpMvKF5d5QLAmulGrlS2zYArzGVHe6mZ0hEc7P9VH4556u91E4oHYAzjZaG5wre6mB0mXdIibYwLtnozM1fvug06WPOflQSlWDYAvRq2gWDDVm3Qz39fUQH_SWMp1jM2xrHpEOzK5j4zFBCUWorucBf0lbPyuV8fkv6wlYdrnK3Ti0MzmlI83P84g7lpW9i7iIA5rrP3HdUS8aVWk_XIsUCgBXUoK8_NulBYyps3tJDz-C3EgsMgd9ybPntql2iJDP8HIvdIpd1Ud_weqBMq-ozr34oV7C3CG8yyDVXO1LMhBL0DulEFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtVA63Kx35LIj-p8JXG4SPQh3wvvNf8Kg331xWRDVBcPnjo3S9UnKBaTcw5OGEJgJv1qWYrNKey9voPK-nU4cTe_6ZrGy3tCA52eLL7DZpqiJzdc_lJhv38wkD7mV2w9GAaENns4JehE3mFCn-QY8nZfvDUbT7k_P3DdwP-5DOOfYe9meGzxr-3_ERVZgvgyPg92lQuaiXYJtC78x1X_3yiPeYID0T9rfjUJj3g_Ffk51oCfrCnvJY6vuKSEBpCXG4VtDqs1jLhSr5mPFbWcvI6vsTL7uroIDr8QSon0wPmYOs5wgFUXc8L-7AJcTiE8OjVJvSM27Z270zNknxBciQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_IxxGNIXVRIKBQFj48vdp3GpwDenJeqTusy782Uo4OqIQ2xoMgLVxD5cks1-e0G8LKBI3NgUIlCJJYupOrvCk2j7TzsVUxwGmmk_fg4v02lKHQIE1ejiGhSs7DLnIiTGj8d5h_tXL98mUAV__McX6xo_g2LhJlqcz3djqY490IGEc3DoCj171Wnx4k8-WvhbqgC68fnbHkNYc3hC8umluBO1soN6otWffK27HEy_R4ksZw9lj-nOy70g7w2IvNP2ew0cnjQtxUrFdpl7WjIkqsfh3MylJ2seYSmB9SyPsueowBQV0xDzai1tWawf0u2XsqLESfipfmOoPRbM6UOmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKtBeRUxwFw91NkiVwe9WGuAFEg4cAipGxjZRdh87qyCba5CVW-TSke-X2OolMDXFP0vB0jYjxUoEUIab-vC8E0PzMbklN318vi10yrXpsyU1Wx4ux4wxlpwQ9Mie45sO1a0Kc0wIzqhTEKlnIAEAf51H2q9jfNqKtEcdTx5leYgSaNAc9eSaCNpm-HlLA50vVuRVRW3ggcrYuQHGLktyCPPxsH4O8BgpOJyj7yxFTK_bH_GB6TUooltYdoUKDZZAWSZHx_k0N3aJOLT44o-B2cpnuMLqn6x1FdRarpWp05JyMV37lU2t9HHDTJJd2lrWPYhwZCrGWc8bjKCWNKijg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1Q_M0Xp5uWQ1LePdgYZdMFaV1yMKP2Wr1KFnxPywnN8vOCbwtU0dRlZRyAmYqtrHVyXNUYS8GzKwY3h7ycQvNuKQFM9PNP5yG9c3KP1dHwZyjVWOeygxZqLbyk9GvQx4AZHkHkvWJETFpcSYZ8btxuE7P_VsFpbNziNqJz7Gir_XoXsJTBObSdCC08NVhhold_4PDAsoy3rUbqqyLxh_vqrC2wW9e8tKaIANe3Qkw0J8XjWr3gmSUJ6KCXaLEzXG8MCFjwLbB338J5xRDx321Vy0sRM9RuXhMN6UoK6oibj8N30s50Wg6zUmxN8NeUbEQLmFa_W3uRfUrGxPko_dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOfcuqIwUHbWq5t7OhqpS4viFSAt4Qs2lgy1e88XSmwYFytrbmNWNwxRcRix9m9MmTTaxse0u8dN86xUNFzI80cTSP-XhILqRAaoaycXMjDdTg8H_Kf-nIM81fGeJ3iHsZkKuzBFs4CHyGyTcvKRccuFb4wlKG95VlL00-4hJZNjOWEEK1dWHmTR-do4K17xYAZXlcNX_TfWnwwNnX842Sh4B6lWzoj3IoLES0yGeS0FNQZrYCu8qCFy67Urdb47PbgPu94lnZkih4JrZPRlZB0p-YoUZgDF56DasmRoBSPxZ0cFZxT3lq3ZKbu7HytgHxyCvzeipVG1qcdN91KQxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-qvuaL5oxXnnWMwRQvzsbFlTd2d8SXd3S_SqFsNujpLaAwOEBZaqhYW_XNUd8ieulbSKri_OAcLYEO7FouXsej0hI8srLAah7w2mOgBPwwvEINuPMceYPIi2OgeLKHNzQxxvU0hvBKhxxRfZs3TNuZUPH5vdWXE-RS5OMqXfXq1RfuzB5O4Djch1i49pYqu-oJZD1g-S8Et6QzvXgxRUjRMqIIV0cMrWNOxxo_rkowQoSN3oMjVgISsNbkTpdCO3H9UdY6Z4pQzjz63D79NeU0LshtfCmKdzviTvZpTQhSkOxdt1fSIlgw2OERhAjNcb7kl2gI1fASisKbonxk3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGNcP4VgZMfcoR7vgKxjN46zZgQhk4VdEgElarPdDRR-VCaEHcxkKVaOvFsUmHJp0RC09s2tjCrz21PE2BDT36sE-FFdgChEwYfh7wkxZbQ_L14m43WebJOKP04lswjsBHuKp3YLWI05yST_WyIdBrPoAIac85igkgrN-_PneJb7d8o0wRtIsv0syLc1nqHxevElEaQ9KpK5swAMWlO7ojCKuvO_mc_DaudKnqbEW2y46Mln1j7BedLww7lc48100RF3Abw6tV83OUnqbqZ1PMMg6DWT3EKHxXNMLV9N-UJAAI4vpcj9CC21muZRRhWVRwbTSZZWEZufmEq7yYCJbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZ1r2vwePXIdwjChQzlqYYYbwSJcEehUQOCcMEYY3MZeqH8NC7OSOP3FWdGAoQupUnLfAAyjO6FvHSkoLagfvfd_GFnJdRO6FBqHAuRbA1VG7ErWaDaOvgUozZU3c8P1IedKXdYcOAkGlWJeSm8nzcgzl4i4xY8Uax0A5KQtQOL7R_4wyjM9etYfMwhdk1AzVzHj51GC78mz8Xneyyo6rV2QAqC41hHhUVMxGDuwEjIz02uodFJR3CAeOSXGo5GfyetW2v2jgg9lrweeGCI99GPU1E2kCaiUt3_QkTh0eFUPv-rsJplIrplPCVLhdfuhqwk8MpMX7i8mvE8tnJy1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8iSSy5ITHVOLcabS4sXnpWHnVD898WIo-zumoTlYo2F4w9JkXBIrxmU7uHa2wNVfGbRbatqGCpeoKjzPw0t7cTbueBHeFoLsP3UW1ks2OwY0rAMWuj1CqV78i7K_MjkhgkrQEBxiFeK3oWysl72S8L1NBe4ez9DAARGvqMf7rimFPscuB5XCq08yvqkBoVOoqVNHrn9w0OcVVR8YBdse02_IfMb-rL9d6jHoTG01sUnobUbZH-pw0GE6AQwJxaiuj3g-XOsVnCTCz6oVsl2cDI7k1FteDyZBytDyvQNRPTU0auCYs2jownR44k7miNhVh-QyzTH93qu8PzBN1K3UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBEXPXF564ERxZ5LMqg02HlP52xgkhdiv6ySC4XXA_SB1auwTI-YYF0JFBff7iv4qC8pHFe2EAlZDbNxduoOEwG7lqX53snraVvRu1hpYaHfTxSaGgAeG6RHabNt5_NU8xI6bbvZXWEcZl0XVOMQwAA_rwoG0kw38CxDHmwdTLfq41swrcIcddt7C3fsqdOBgS12vogcnKCel8tzLSObf_uMqNGXzpZA8-kHz5_q2L4GrfwcqKKBo_pcbfoXhqwdUzbrKTmKXxjcBGWqRRRTV3MZIGC0x0UhJuzV4uljO0JOkxl0H7aDQKMB6AFRSY71V1y1VL0BLGTwFkiFAIdKRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7DUCTWMB8Z-O4qn3EziOL8S8C0N-WDV5iMXHC-qoT90o9P_H4LhMBZeE5pCViav3ArzNfv2IN3aXbGxplz3P1u65LDcHfpZ196lQSyd_ykcPaDytVT5-0noWv_hRlV6LWpcPFqJDndGPj3s27Fn3Qes9BDWyJGXK-uTGQIGgGAcEGKrJlQz3RkbteL2lnLHMmjjdsR8opuCtWH6UYrxClyVZtRkhuVNKr29QupG9SIBl9lbLHeNDCBZ6llegflZX7eeUhx1tQ6Ki9x_8Mx6pr8oYsSMCPr9wbjlwv5I_lAvO18-352FEZ111QMiRUdQtLGxblq4JOTTBsrO25LqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktkdBsPPzhX-XYWIlUPb5d1zeBl8Yel7Lohyx68tAyBmqaEoYVcX0SuhJs4grrEEdiAKcc4voL8FAQV4ffEK636GMEM6VmaBcDNJIVcylZTC509CY7e6wkUdgBXJqiKaqI4UaKkdjDaw7YKFTqPyGcq93ER72mTvHZIsZOX3AVtN1emX0nTyMuNPzqjEeyc4_P0FzJ8J3PE7ZIcsfpRTkSGwqlRTrNBqCoFV0iPgUaWTd-HGg-C1ltf_NSsh6sJ1qraNIHhAR9usPHY_K_xTrguVu3exOTba2VSuamUA9s1qq3FBMUE7TdX6um-BO8OrS8u2tS4aIu0LovTjfoIEAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKUJGXQTea_hj0KLTKpmu7GE1KvvFQKTIYVuEKOCk8A_EaUdEeNGeXeeWxpfy4C-BzUD4m1Tp5CzYz373Sc_mL4tBK-33aA-iNXLX_aJ3F0cDzrc-ZtSmo4qDjKNuac8KrL0BOqo6508LXjN0a99HN0RzYEnEadGA5X1Vf3ZNkeuUna5CZfvJutKjMpTR5xFy5u9Q7ZrtdeQu52OZCX5sD1KB4-QJJn24YhqlrLH3Aiz6hlicSWDFZ80CYiscjoGTJAwvn_QKu5JOUAUvL7MJFMYRLfBwYI3cixMEHmApwwnDSivKafc0vRNKFzl-ZbKF0KBL6Dm2ezc2CtLA3aNcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed0NQs-fkZhgjZZCt9FM-WlPXmgh8gAjf2KybcFN-t5w8WeLNbb3v8DQ9_u-ZAS3HnwVygb7bHvOtCOZytBqiqpuwQXj6wdaPsEa0fCtps4T3Zdy7KLFnmhRnbzY748V-n70BnNOxCjGauGqr1zbex6IxEsuhywFk647yuaE4ThNwtEAnw4Ym-65_BWHHcch3PeGeah3fF-V1onRKgu7ztQkMb08XbZ8HBIUPNbb5-kwtclcf2I9dHc2rEOeNMcrRwWIvuNlbTZyd1RalyzhK7jmgyfR17LniDHFtrbUfg8A1DlViqNLmG_VILBKveU3souCj0a7EdBkIl8rZ9eWWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9ccIlLxnOcFpyPCB5mkHrVaPc5CXLP9yV-eVyEm4SKE38TbgXYxXYrzkbUL631sSju9eAT4TybZICb9UPDNIK9C4mBMlj9UILnJM8dVBVqMQ7U4uY45FWpV8W8Fd_FvNmbieGBkLEjZGICIqfqk0e-X4KJukSIeicAI26IAjTvt0WQS-MehNZwUNoM-_k3xLJYXKUjnw25eWOfGIrg7zTLq5x0IYBMV2lHjNKN2t_l8TcTILAugGRtfHUrb3SXNy05HdeddJPviq9ZFpYN67iwDW6XMvLjugd7NbMCbSgBC8Awau83vjGh-WxDaWuPPCZj8Z0pLeVIKNIOWICib1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6-U9CGHU0LHHiQG8wcio7EuUN-PUsFMzw1mNux6-3iU9DNw3FEu_-k0SrnSG9RSPaukWqm2hWhMORx9m0aMeEpPPEE2c61vp1Np4KZsHdHTbHCZPMSPpLlM-3rJ-VOsep-N_RFuvwReJfiqr2ptwqCYMCpaxsM0fkoC-1fVc60HBplYV8vVs4-wI0ZVIORsHyhVbVEeL-FgqiEfJhJzsvpeBi7vsDEgky-WTCwPEjxf2JmQGMHT_0zfztta5scoJqIzMVa-Hwg_aix81vIIvzpAVsfmIF5KBcLz7vnyVKLsCnEwwT7NBKTMyzEvIzOqrCLKfDFrmeGBgnB1Cd_F4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5q7_Ssa_ddesv5WXmiClAGquOzNwEQhAOdp8st-sZMMOf33R-6ShEBgsTSYOMVTdP6eEx5LzJoXoeDYjM-lYsMEKH16mOEzBCy6NNVhtHSrgjjB4kCadrWEK8eHG69jxmW4R_IJ_CWUqelg1uxWTtA3jKdERHzbTj5YMefQOQWqpd9WDllpS78zAgEP_6q8hbZJOcaaNrx2viE3nyviBkteNTMkmxuYN8AT1UxMRNBWdm7vIwz4ins4uWlhjugAW-Tovjfvk5eB9bIR2azOo6-qfxbYBaTaKQU5Iok_ft3cMxQahInBGUibfZSwwdmpH_5J2UQVOqscepKrLXUKEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btpLjztYR6GeJYpep25J5xRJKSnu4j6GVBh8_gi2FnDwagvXetWmGYWw3XO3gZxM8w5Qlo1dawSh43bkL0lY1zyQh2C6-Lo3IIARke2O5WTyleq39xacpiNM9SLTiqpQyCxw9w5BwS0cTqQYcu4xqOQZ58PVSgAHt8JszJl1kgxtRmWuR5P6lxc2vuui3NzRO8XzbLviIVw3QZ0x4f1x2Jv2HQi8hYfYAZ21B2lW2-wIr-CP8Bf6SIKTAfftY_N_79tJZLqp601awyirmqft1B6HzO2Ut57o039NJ2KV7CtTyYRoVIsRuHIU5SAtXu0tZhkEMxcFdr45WIW3_wdZyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3CmfOXsrbumy2NrIBNq9N82GSUEtX93Gq9mcjRJjmGK6bZ33lLzZJxEiZGNbDy-5CTq6DhhcXV_cNUkSCPwjwOe9s00sQoLpKKH0R74ud5OSn02YfpuhlpKnzjeGlaDJCRPaeMIoGimsvhWd1ZHYLsUYGDMOPsHHS_e0n-xdt7O6vFrwjPyimjYlqUcpg8FY4ajts0BuHbyHnTHEcW3zuBc2YaAx942vjnZZJlFI6ADDjvyikK1V12zsnP9pY59WQ94H7cE4w_vguhqr3ATyg49O7m0mHlaT84WmVEDKudlm768Qz4Pto2pVN_N-QXXFcKg742F1I8izxfhd7fx5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhJArQblGRiMLsS2l6HzIk4IwWllCw-MbU2UE4xAsO9FBd9TLEyZVvNAasHxLjYtIyA5gbp-rVPzZg641wc-kc_chpAeBVuqK-IOqXw8nBqF_9pmlqxWXikZ-KIJaPJ_81A2NiDD8JeuSFi3h_LcG8zWE9C43y2RTkASIWCulj99AYHcyvwohmvqAT3QDFGOaWz_cpliBaGadN0MyxXL_df4JliFW8x92NSbpJOY82l34eiGnXz42Rn3O-IM2RkTqMhyZ-29MDO9vL-qriZRnYAXT4Mm0cH5PHgprRY8NB5BY0jhsDxbTfcMdbU4XEevbSkxdTc4NzCUYQzlqNokmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_WOn63E5Jhs0QmzVxoXLzZd4CU1mDNg9gwdlC0L_cDUCKOOGGDV5oks7hAwgdAfYpNQhjFBjAKAzupl_C2KcXUdmVx-8TH21p5PlzIr6kIDryflfv7tWPZi_q2n-pdCnk2hRdfZTwMedVaKz9uzWgeFfxfMXVrK7TbooAsTqbeZK1ovyMxD8XDD-_lXPhI_YZXbxs-cmwMmA0Ao2w7u28lt9BNBK7Tc-pQEei_fguOWtQXNFpm0xpy3fhrfCugpLYm6cVsL7mB1xLObGRi8tjrWHbhmtAoxVzRTIIySNq4EE2Ly51JduNeaoWdFAb-1zcUkxhW9FOgPQLeYYqgYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=XPC-QUJ-uHlszikajfTyn1axMiOPtDHPw2MzkJr5V2F-qFjaZILl9fzToutWaUA0GKqFEwty7D1fbna64ziLWA58wUWD5ErgKT0GQMzr1BatnIWqZQorzxbLVQ1PYUNN9VH06bA6-PKU8UubvHX8uonNz034s3dxq0tBsQ2TEe5_hDXq28K9Y1fDI2L3oVEX5D3ZGduvFOXrBVSAwE09qMOGQ_DDJPOOoYmnMGiPmm8lZ2p2MvhceSa_IbbjHvlfOLRXYb9fB00haS9CYPr4DZhN-RESBrkxj0j2ljyaGteJ05EO02LTP2BwnBTPIY4ubi8nduMJSB0w7hAg7peZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=XPC-QUJ-uHlszikajfTyn1axMiOPtDHPw2MzkJr5V2F-qFjaZILl9fzToutWaUA0GKqFEwty7D1fbna64ziLWA58wUWD5ErgKT0GQMzr1BatnIWqZQorzxbLVQ1PYUNN9VH06bA6-PKU8UubvHX8uonNz034s3dxq0tBsQ2TEe5_hDXq28K9Y1fDI2L3oVEX5D3ZGduvFOXrBVSAwE09qMOGQ_DDJPOOoYmnMGiPmm8lZ2p2MvhceSa_IbbjHvlfOLRXYb9fB00haS9CYPr4DZhN-RESBrkxj0j2ljyaGteJ05EO02LTP2BwnBTPIY4ubi8nduMJSB0w7hAg7peZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4b4nmaqC2VPU8lFJAqfDDY7Bk0eWB03IcxoBZTnrmKesR0OUsN7WMaFtWhNos-inYrdjZ--Tl9JHh-rrtQaTDfOeAV9ut5Uykp6CLDTt9JOXd6am_lAvY71K7bUVoNMLXRNRceWTtvsbJ-3nIBHBH1BiLz436XbOCq1q8X6GBzi-zmIXMqgLSlBJo4Mp6LDUktCfMOrOllH3qzb0b7iaSEzsa99qSh1m0OvIA-K3_rhUbKTBv7148sc6gNfPs-9cO4OzP65I9PUtx1ZMcekHHj7UgsRjL0083uUICel4j3VgPC-E2mOX6XbI1QgEZiYVTz6UlCU-Xw3gDbOsJQYKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMks2oOqc2hA5JpISXCHiuKQpQMWgqdq3NITQib2bdRMPRUU6jTQpMjpoDpVvl8XsgiHHEHZ5JM-RevjsUpOr_j8pgavzWIas9BSJF_DMH3CRwWE-KKbwh5fhhjR5iqeDcBpjNnrSwcuxN491JsTCcNn3VD4gRnS3jJF1msXlyN0syR41lgdkc3NVK-q1G9nagYAkojFT6JWChrSa1G_laNzHvOOUS0ZdzM5AsUwYCd8IWlxE1ImsvacMqG8Fy45Yl_JwoTu7TiX2WgbSywxTO9PCbS68gqkgqRMm0E_EjDm1BgCRQo9oBEb1UbFammVyuIIV53rnRtmsIz6pggMvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqLhzaQQ26SYzto-PUgwQNMo-lDJTp2fpeTmRPRxIgRLSKoMeub2rRLuzQh8N-y6Q84ViRXeMt6J3KNfz6EoQcpprST8Wos3ES_MjFSLhdXEUom3YKGAXJeYaWWhlvZZg7tibydrmUZFI6cDOZKqYHBjrhHg3s6kl52WedJ4LcBRb2_YLWlvKwoy18NfDNj-VSCBaNBeg4b-hUydnosp6Gbb3ZLJ8MCu-9bF2RJN4n0N4Aqhtcw2Xs42S0sCY4dy7pLBJqC7Q7h58dTdJ12o6ntA8u3g7MgO-UhKxEzL96uMORFQBTd_DLaMKubZlXeFhLGTC8hNHSro5bschvYdCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSxp_K9YBk-GJQ2tmCxaqOvT7UEkym01yEhZRZSg3Nf1jbw_ChlErCH9fdp3BHFF1Xd7yAwK8SqnfGmRqYJ4jArv9l52x8_0TGWZRh6re8T3rfI0BzVGqvGx-zjqchCFcfLYZ_7xqZy3JHfZprde6amzboO4JTfjrucc8vxZUgyiXxFSGIFw8cTqMEgtwlhKEMv0NDEDM9-b4Jz7xkJSQ04Rtx1-96PdX3TE6eF96GGtU4RScdbEceXRdT5xVzAH9FI4Vr_C_bdkKbWxpJE-6xn7zPWJtp2E4ZwO4B0jHBdWdra6ht0fDyvzqkxiR4brtDniXIQkfEK4eHshhrW9ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi9PEfoeOwHu3ydpyj63obvfi6Mb_sJItGRcncX4eRymUEMBifPvMz1fqk6NRA6GCacDzxke8eA5yBfXKeqxgXSbtHIay0HioMJWmnIOIGRinc9O__HfRZrghZ5Themov2LBM4erZkOM8suFlm1M4udV0lbBYBapD9GhI3C67HyIjAb--EswOcgMb-cn4I4tRcnsIUd_SqDR2-42WSaTA-_HMhadRh5GepuuaB03lWCfOZKbsGyMb60KaEbF4aYREWKSBG2ZNLhnbBtVk6P8my5ieeN3KyiutaVkKakXsaKmzr1yI7mO7qIme4ClhAFQzEDathgrGxVnTzA2jzrwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBpT-LoY6o3bLVdLfKNqbC1LVSIxh3UPs34tiUfyXFz2iFIZ-hzZZvg5M-ccafaQnW4xQ8nykK1ofSqKVlNBEq8u3VABic2qGbHF9ljOS9SdjR4VYQU5L5c0YAd3PIJ1LhOPGHJ5XW0gYINa8e2x2oB35iF1XFCWlytFEnUZ-7iwCL5nZPQ3A89LlBBAV5EFNj_MHegPjIiuJcPbzkzRXQngYcnFSjAnOn22PNSslS7YD71ZTEDn2-yCBG3Fs3Em9-fw240cbCAXtijhqfyWrW2YdiJIu6E2kLPAoD5jUe51dgP4bECet01AavD-_IQdc12vnOON7qKOt5dxprcS3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2U6ixTfekxGaGA1ovNdy8YJW6RCY0gIe18afapLKhp0MP-JhA8QBEywnfBG1nvwBsMXVbqLjfl_b6umboddgAO9NI7_Ih4402upa3TM3MFItmbJ4ufmppd7nXt6TEOPTaN817gTDW-V7AGoROV93pHNHOWrOlmFQn9ODdl9DnegNEv0b3FNz4aUxn2xDktHJLpGc0HRoO-e8XFNt9Yk6MlQvOs08ljl9a8CzktTNQRC--NM9LEtYlvVY2cUgtJu6KwSBqf9TVQd6e78aMRni1F3-Y7ziNg664d_-77QmFmCUJkJgxHuIwzdr7y6M8RGt6blVr2DLjv_QQO1Ko-7jQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rbegr9PtBsCH_GZCZ33ox4mg0eRCsioGi5CJVl1V7UK_goGidHV_-9dbtxsPaAUOSgulZjjSbDCMeU9SQEuQzRcSbQ3-vEqD9VHG3FHXvZUIICWC6J7hPAWInK67lcW19YWoFiOrdMRnRaVwVgkrR5WJdl9WGNBsqVxdMjuqA1lQNbz20Yn76fnf5gPKhEgi99_jUCvaondsVOVDFcOgXSHHik46oqYGo8_yLKITVj3IsKo-STGJBoxbPLH1rTlOV3eIPnJtzEoee2m3_4CIdeGm2pWwvU6-tURGOzGesnDZ2SmvWleC8n19Grw55B07l7Us7T5s3aZW4jBWHRgz5wSIk3AgYysNyM16B8WGVQ1CIuX0Z7RPZ-eXk1p5y4-GmlNw6buGR1vgewlDpLmL0INCS6ni3bQOJS8khGs6hwauF9pr1ujhAYk8BnE-LYktUtEOrjqt19CgNpj1Cds2bxP62EMDz_OxVGgQdx5zhcIWcFa_Foh_WCjFupN2gVr3kROOHhZt7wvSQyzhCHJKsb0dYV58kxf2DkdPyNMx_QZhg8pGHjj1xkyAOdbEZUhcTNbNhBe7-j630UKAfaFxwNrJp5rJWV_7P6PA3HZHDhAjf1ThLIxTHM0WdQ954HOM7_MRZVCJieHAEHsCQHALz_uY4hb7gucFfRzk5G1fJAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rbegr9PtBsCH_GZCZ33ox4mg0eRCsioGi5CJVl1V7UK_goGidHV_-9dbtxsPaAUOSgulZjjSbDCMeU9SQEuQzRcSbQ3-vEqD9VHG3FHXvZUIICWC6J7hPAWInK67lcW19YWoFiOrdMRnRaVwVgkrR5WJdl9WGNBsqVxdMjuqA1lQNbz20Yn76fnf5gPKhEgi99_jUCvaondsVOVDFcOgXSHHik46oqYGo8_yLKITVj3IsKo-STGJBoxbPLH1rTlOV3eIPnJtzEoee2m3_4CIdeGm2pWwvU6-tURGOzGesnDZ2SmvWleC8n19Grw55B07l7Us7T5s3aZW4jBWHRgz5wSIk3AgYysNyM16B8WGVQ1CIuX0Z7RPZ-eXk1p5y4-GmlNw6buGR1vgewlDpLmL0INCS6ni3bQOJS8khGs6hwauF9pr1ujhAYk8BnE-LYktUtEOrjqt19CgNpj1Cds2bxP62EMDz_OxVGgQdx5zhcIWcFa_Foh_WCjFupN2gVr3kROOHhZt7wvSQyzhCHJKsb0dYV58kxf2DkdPyNMx_QZhg8pGHjj1xkyAOdbEZUhcTNbNhBe7-j630UKAfaFxwNrJp5rJWV_7P6PA3HZHDhAjf1ThLIxTHM0WdQ954HOM7_MRZVCJieHAEHsCQHALz_uY4hb7gucFfRzk5G1fJAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCfGFUSLG2BwP3RMkMB3ZoYlwP-Ce68jMQBvK_08WTqbayKeUgftdveDB2n3n0KAI1kit9n8FPrMcy8KO9eCG6pMBwjP6tF3nt-sjQ5a0-SHn6IsUqCD_NzR7XUxRUUJTcak2StjMh3Gn_5T7nHz6PYcjlST-fWBETd2D2hv31GdbxCCtrlyK4uoOSfU-1XwAHHgJc6XBYUr4wiCSB0e_WAtZTcOfh1A-9CFaDBXeaWB9nnjnkp8XYmfwB7aFC2guBOM5LfF2Y66JsLKoHSSEOwZGxGKLLlPylchTRLMIFmxi8NJPKWg9FyqCQFQX0LepE1MEkaJ2JH9CdSiLYCq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMLAOwfNTgxiKiF-MiJwwALdz4IZhN6Jp6GMpm2Xqn6luhzjgpd-gMDMYkw4jf-ADiRfg2WnWeNHXMTH_OvoO5OK0wuvJq1UgTqQIowgxyOYSx8o9ddS58XPpZJVnMgSmVXlIs71FAkbUuhUICLH1mJ3PkcK1PtPZQ3Kc6B9FALuTQo8HGDb7cg5vewEvZ7ZbqMe3dFiFJ_qxQNW35TsE3Ms0rVtyVxjjNy9Emd6SGxnyCxKz0SSLOTE3WDzBQfYj7Osu71oE__NZ6tIXwmD3mC_VI2W6kgeyImd-6LY3E6nZK9wpAJer1VS5Qt4tE1Xk1R0JT4gvfYBbVXW8VpdwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpGSjgs4bLxZ_hz197WRuHNiJA1QIRazRcDp0qM-YB1jHY3jIMDL9u_Hi_M0P6Z8uPobs9cFrFCcxBe1C2hLOGUIRfUfScrMgx5IewwOZfMTw0yk9_NSf-UAUpQmfIRsNkRuFLaGwx40Gh1nWV5zI6Gxd5v-g4uE2_du33wbg5eIq5R0dsDFDGkI5toZ1YAQP268_stDwC1iPSAB4H-9kIrdmAD6rv-m9MmgCUINsfxUwVRfEWwSkkORRy99q1K6JaIq1o6kmKJqy7PthTttoL40L8UT-kYZhZ6e2XmFS9m9nLR1baiPX4p4X_Eb9flsSbOgJiShmp3vFsOHaRlW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvwhoTyp5ZGL1dRzuzbBfWBbVOQvNvlROEjNPfBYTrifnjKIyYA0I56n8ehTA3RFyUQJXFfE6DZ6m6H40h6M4AZ4mvuLe9TKmBZUlD2xajJOndsjrqjQFTcl8eJCUS1uu1Lwu03Diui5VkMxKvHplhCamd21AOiRhyXPUBgiEbHy-05YlfW2fgLXsj3SMSMF_mDSBlcKQOhP5Mm2-n76xg-048d7GiU4LEoZto7pDsYwe6hmkwy50bac8Bf1dD8JFMJP96s-1C5-Ta7GWe8NxYpmPK1XnVO_vQo8A0MdmL3uDQGWiRaLSGG7pbxPurvt_UpphYMT9ufv9j37_MW_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vU6klg8Dl1J7RWIF2XFgnBVJDrhQ2z5ya-q9-x-EK2gfX9_xVAaN2IUoU0s42d_K66P5hD7r6wvJN4niotV-6A2n2xQuB3S3vdw8BmF_EEXv9YjDW5dXVPtAPME4p4nECHakymIPZfolRpR1QlVAe-_iSx6dtnhUW-aogoVCRD33OoUzbQ_aPsN7gh8uwQc4eNvx83ZeTJwD0s6CX6e2nb8nfMYRQZrlhIyV7PzeT0gyEwsk70syQc2HT9QphRKKJAR55umwtZ4ON2vgHBeARpA5Xn7dCNPADcqX0wj-USyD8olOOIx5v0xiJcw1ord8i6CIlUEddCCp6nP60nmUXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YWiorbFiEGIxmekgA6Chxxxc2zQR4g4agoJsM-Q331uQI0V7Y6igOQ7PQZst9s-bnUwYYXksFQOyu-EjKdk7sv0cvU8hoDA5Nvmi2ugkhMOz-GUQgtekuSnqh520G77zEoJZMEaC9FvIhdhmko_7zgXBPpNurJEQ39TBdc0SC37_J7xjhQcZXkd_eU7vf3fTW3d270CcW_KWDa6FvOE_bonnjF2z1q9BlTwuZTbTXg75PjFwBXaEpqAIGY-HslzKRFLUkG_rERdazka7UxIbxmf26um946UhauE9Dx8yLNd5yh8EsWx_wQigKLLZQwbe6iIz09DCcKSK1F5KjOELJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YWiorbFiEGIxmekgA6Chxxxc2zQR4g4agoJsM-Q331uQI0V7Y6igOQ7PQZst9s-bnUwYYXksFQOyu-EjKdk7sv0cvU8hoDA5Nvmi2ugkhMOz-GUQgtekuSnqh520G77zEoJZMEaC9FvIhdhmko_7zgXBPpNurJEQ39TBdc0SC37_J7xjhQcZXkd_eU7vf3fTW3d270CcW_KWDa6FvOE_bonnjF2z1q9BlTwuZTbTXg75PjFwBXaEpqAIGY-HslzKRFLUkG_rERdazka7UxIbxmf26um946UhauE9Dx8yLNd5yh8EsWx_wQigKLLZQwbe6iIz09DCcKSK1F5KjOELJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6RMax5FZ_Tr66ueN-0JlFibF45hNQ_ESBXga73kyuhm2MQJ7P9ulB-h9VM4OKDTpY_Zihb2vflObXGiHEbaIBoR1-f5_dvmW9KM4nBbmdOKo_nqwNJ-c4B8q6U9XgilJZXVZVqJZ6BhiwnK8XkY_zXbZzknjf-tNBcgpDsp2bsWFoK5rRyeW4nOj4DbLxbQKnSu6KB12u_Gw6Dz1h4naI13_fU0TyElkKj3NdoQaJrNoD_iKV3q1sQimi0LIjchWQZep3F17ExJJnJCCjvyc-547ybBhqSpSS6ALuZUKYbAJQgrpH1HPMvGPNQLdBFPjeL5kCRuecAZNAfzP3BNzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upZu0IJdSo5HErYoJBDPAA7PD5irUkMIT6TIc669aEVW6-vzU6Z-SnLXI4OLbSN8e_x-8fpL1jO1JcliVfPm38SHrljILyjj7u3yqXISeqnxcjj_l-2DMNYMFtPCLsSfalrRREhtqn_wxxYMtobkkxE4cfD0Uqv_U6_I64IW-6hSeWmhvUOIAFK5zCn8frU2IXNSYcmZea6EDvKoAD-vAA54u5NDJgy_X5Q2PJ-mqIh6x6KTlN3ge-UwINJcJ9bIahHvXcH-frP0P5W6Az0xZG46v48v-JA0Ldn8AEdFxpOhs6mRPguW5Ycs3DrB_qqQvWY08M0icyaIL6IXhd2OLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6UWIj38lMLYIhuS5kYPu8iCUhXv-CqS5l_gZcAx2uoVqBcRXKXORDZfgM1C9jKMTp_8ZI778_BbdXYyygJX6C8oFGu8FXd4V5C54siIBuDP0MW805zFDsGQHermVUgD_90xl4JRfK7vfB7WKBXoCSwgQVbqj8h-83Th5W89h3g4ARC68sx_6Msh0GL8yBI04AKXL_LO82qzgfuHurINUkaQJr6cAvq4QWANn9w9DvsEMtFkUFdf1Culs_4gj4tmOK6XRJQtm9Taf4Sj9JJdeDj_R9021bZN8RkxTBiGuwcJfiqPKH5FXzdxOPF5PyUNu2F6M0J02sIozF2_Cp8wEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ViePUAAFF-nNfCZFYDCdkm-94HWsqf0mJBKk__sspnLvauBNeegFPsBcIbUEirZA7p4F7aaJVLFQqoG3DIDDGzeLRTB3Uigia8_SLPaVajNHV-B7cPPTf9TiksR9POeUIjuqXUqFGxJGXl1lr8afYyWILVrMaiij3dtIw38iQomIKZkhA2H_rTQcZxNpPFqKMDwc7EhUmgZchWCia_wysyvebBUd-kHNm0LuHxdIAhGe6C_kpdvva54bliBsxto4hb0guIIL3cYojLHbqy6XGy67rZRaCcSvWvmlAn23NNben5mcmXDikPscLTPJ30WjTOgFN7qtxGcaxbdQlFWs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdtP2IT3SlA_CKUNgrhm6T54sJRtuVf5EwimRTBFrzQPRBg5D9xQFmtMPu2gqDAQZ4PhgpSevUXoGb8DUaCWfjB_DyWr-duwmRBzLlCIkkZJJ7g2i5XRSWNPJCNf2yEruphLRWe6kGJ0Xvh9_UwemX8sSIceOWtuwhF6MAfR_VRERFPhRMFea2Nx6XCxpzmjUn66wwPjard6IkQRAyxnBSm3yoCLJ8Pzub5LkZmsk4Ez1TCd0hS16gEnnDHEBcJyD1vxZjsYq4F_c-KZuuhb7bzwwhCeHgUBF0JF-6BW6VCb-px4VPm6CCSyI4Gee6B-oWTg31-9gz9_lMkDBD2u2Q.jpg" alt="photo" loading="lazy"/></div>
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
