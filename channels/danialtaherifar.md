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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 268 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UC8bY5GrT9Mvs3vPxklC2DiXviEtAsGTFM50kqzyFaaCuvpL5fpvA7pb1lbJPX8A75_VqzERfhxcYPCcLbArrSSmsygdZb59OkCCi8b_2qbMXmJkGKC48jV-l9_vi3GemV5lOpUmBlrgGxMHh1obhB1V0xkMbmij67nKQpOB-i6fDjOVGE26jiyzHa-C0rQeX-DqabB0IB_AycRDcY0048tQ1OPXolOsyl1kmzOvwkWiy6O45iQJEcpnMe5KCCxQmCSSEQw8ZzlOEIvBrH62OyAQyiZpBsHYemZc-lvt83LcaJeX5lRhHta_FTs_KCdQNbO8Li9jMQV67NiQNnYUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UC8bY5GrT9Mvs3vPxklC2DiXviEtAsGTFM50kqzyFaaCuvpL5fpvA7pb1lbJPX8A75_VqzERfhxcYPCcLbArrSSmsygdZb59OkCCi8b_2qbMXmJkGKC48jV-l9_vi3GemV5lOpUmBlrgGxMHh1obhB1V0xkMbmij67nKQpOB-i6fDjOVGE26jiyzHa-C0rQeX-DqabB0IB_AycRDcY0048tQ1OPXolOsyl1kmzOvwkWiy6O45iQJEcpnMe5KCCxQmCSSEQw8ZzlOEIvBrH62OyAQyiZpBsHYemZc-lvt83LcaJeX5lRhHta_FTs_KCdQNbO8Li9jMQV67NiQNnYUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 373 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2PqOn8jpXhdh3-wBzemlZrqIDcIvYX8gwggOaODVR4fMcPvbj81tZHQuRdbg_ACr-1aBeJKmLqdrh24V7_1hjLinDyMUSbdzZ3juJLSt-wriXbbYUYO3jLKrQmArqNyRcY8HXT8NoK0jHMdwg0tSsB9ALbR_yhbPamYEDUEjcFwXEjNyy-Bo00o6dhhfmu86NwafJ1HuzUTfrDAWVnjVKHe3r_b3eOvK-Rd5XBaFuWSG-2_kOzleH7qj7KU1gJd4pZxrw3fPnLp7XGVOevzC9uTqaa4aNY3MT_0J8uIV_9z7DvXF5btNk_82dSlZCPo9P5ZFZ_A1axYJw_HIbwTxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 499 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 729 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4oi1zDp_KsZS-jjJAyXvtGHGBd_vt5QQ4Sau3K_9BjjvXeZKbn8XJ1uwVLnbuzV7oA2weRngvtV9YX1zrDF1LZgX6cV9zpMVrfr-yRUJ_8Ptlh1h31X6ChJj0Ldn7ZzRVfcu0bvdBlQ3M6IIIc8Gwnr3oRwhRtqtkHBkMEgG5xDVHhE-4TkhIcGeweNHX-7r_JDjShABS9bwzZtYjBA0MktVyV2zazu_DKwGu9Y905nHHf8RsCVloTZNiw8xpJvW7sq--S9YqR0GF6plji2eQ940L3yKrFOvGqqW-ovw6IoQqzrUQ13b_FfiegyKUTQDna4wUVVL83tRwUJ11Ek0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 861 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_ER2ZT8WV6tcGFcuZR6KDGF-PR-IXrz9C0N7nCG91HfHTT_BDpiBYj4g2S7dEhh4jY1dbm5p1DkSm6j28TzrksjafWTEwU2J0k9S9nf4l9t4dR0CaMWyhTrlDLxKgvcrPkydUTyir2yuDKcAKX--7ohfGr0LSMCESCxecmVork5bflO6H2otzVENMEC826_pr47liCHjgqzDWTadSlU6W2aFqLS1hb0ZLfSP__PXdTQ6Ncd14T_Qlr9-KyQIb-by9mXEgSyyf-1fK8G-X4_oPMZXcY5Q9tXVCIPBruErOE-I3K9iU9fDEMGYFJexQqg65pS-9eyyRBWJo_RpxshxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJPRk8kEqYnSoAI0wNT6BcoAdS1WGRsSpu4pGfmhVH-LEtDSWh9YYCKo2Zu5gKWqEzliZ5v9AlfH3AjaksK1tLxrafDHVG2TVMpd79sPQQUSUqxTTUS817ka6tHMDm3LN-z_95AN9w3mlIUraOpkmR-SrsjzoGCxZN5ZHPaDvhLnZAU3GBEt3oxMqBWfvuBuSyz5Kh1tHbcEKZGHTjh4p2Q7zDNuiKu1VckNdG1J2_CxzgIhHpb7vdiCpkK9L8EjkbX4M0p7lAmj0VN9T5ZM2_emV__b9X5d3emo8j-y5tkFtAzUgMmC7M57UddrGhSCmFe0foUO4KeNrGK_3dL0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3yOguqT5dOyq-nVInWCLBnhPfUGbWfaxauJ6n17VvzaFIBdw86F4AB6jk5mHXkU9YKgkQB_spH-FTUrbEWzdhgEd3wnLyp48vkJIPByE1Tz5hNgaeNMG76Glc4qivHPgC_ZQ2OyL497N8IN6ijT_XMx1uKTaXIIVV3S-7bb5Gxy_Vcy-UXeJkge0AnB0PO0VNTKJ-dWWnQTfn9T6WGIujrrRyuzQlRO-rGw9-UzdXp_CIH6Oz5b8qEqb4sXcnyWYjqU5ZKHE0tPdyBZj9OYIGRxehjE23-CgoGkySspPHI0zpLwMsI7gaQyydrtwtVNYc8nO5-oiCBf7Rdlm7mhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIYtcp0rbsoCRAlr8tz8p-CCanLp7v4PT5u-J4p9p6BQFuiuImjGHCFrsMkY8RP_l00wfeLfjTI78ZOF8s1c5zySVl1anUuCjUugAkmHOzfvvxB7700RRxjh93USYqSFjpFgLQkoTk_n67QGE-pHcJRtBERkJxTuzXPvGEpOW_S3FeQr_Fo7BbWTeVdiPaK_GACVkW3AVfG66-72vkQaTf3r3qicRtxIQoUSavVy3BqfPAzzk7evpHwtFkh6F7GzaKYyCLMgDy76D5Q6C1xvlM_qE1No_1HYhyBEUA8_77pYUKszw--weNxMi14FHT3Q4fPBknCaaO-ezxvRF8kFNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVZ8wgrmUi8q1Z0MxWVMJjD9GR08_1XTJSU1qiAcQ2AvcL9QHm42eCQfAAwJblkYW6ynGDMioY4tr9DWeIxrb-6Mvu4DAQjNU3-xiYj0lEyiIlWvWhid_Ysj6LNEDE7vWAvyetG1e4wA7mMe0smsswbFv4GohSbiL49jd0CfkmBHOZT-Qg62K_jNUspUq3Yxng0QMGB8zyKq5YYmQlc8SxecD2oHYFkdYQff1Z8azMbdeKiJ1B_bVLw9Q1DV23TLN4sklXWnjH1M3aBdde3z3YeHXXOzTtIRGP4xziHex-seyCINUwb9bRkkJb7MFLjf2FxfztyhrQXwEMw3KziAdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLGpUHUAwXzGxvHQXft2pq6HWh67l_Ptq3exz8SfNpeURLmUdX4GeRNXq9bd6YoTz2djpZUZ3CKzrp9RhEPHHAh8NZsM8ait6L_QZaRlJ5wjkRMjstxrZM3aqYqxwAgfllfiKHjSaW-2MXAkLko_vUq4CSKW1qprgmsZi0XbDEpjCnVt-zRjkUCREfdTUZFylRwlEO0Ea30m8FryGiEKNw91Hd_9TExDP-xqx8nZlqEymX_iTdH2D1BIXqJjxLc_QsKcdt9w3GsblWpMg0Dkx7yeLASe3_uukA6rf5GX4lxijqw8hVnxe5hx9OD2wc8v0NipH7KhGn6SpSGmCscmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snULZPbpFxA4aOBpmZmIyMZtViKcy4mIhlj5l_wWIb2iFxaRMXrUUEE15HcGsRulaEF9PkDlW1iPhRTobj_H5FLDbpq3-1xRuDTpUEwuZy8OS8QAPjkAXGYlogqq3iQ_CagGWaWlwJmZFixZJO2_RPGSFp7g4t7Nppb19bCrZ_PA9uqjgouz3ZJy0OL5KnNi-7PbdBKnbhwE6aUaI1pegK1cWzADZb1PbAXeMSDP9uePid9mkZROvO4fBDGvoA-wn1N4ZZhFuhCMxkaZketqwO-bh9NnP3z2qzzsKtbTid-FE4bfuNglCgIUxzvmwLXy31-N6bx1lB1QuWWLAfYbxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp4Q32Es9WDJT1e0cNwamYZsKUHJVKIw48TadAAajvMMu9RLM1eylrSsr-uP6e9Z_FTKWVg9KDaDZU11bNK5IAi_jOmio-xRw7Jzm06BvrZlsiQzm016ZXquKItRaihO0j4CvHtRRAaerPFayYMpHGUbk-DkwmspWeldugeJ_NEs_8CMS-ynky0bZYcJ2riA1s5ELwO7phM5F2RFSsslmCBDcYPN0Uqnb8OeEG1CjXpsrfBMJABM2pNAUem12sLsq-VYO534Vg86WSovaB7qlXKwlSdEvVeofdrqlK23cNVzStWpvygZehdgXGbaRvQEh09-eeHQWyzRjSoK86czKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjPPJ0nehBuILMJqfTDO3qD1V0EQbVtaRhlX4mLT364TSdgmlu00r4z3R8nLRtPnGLvB5WnGIZtZ9hWswagAnnOcoCCAves7yoXuwqFD1MWqS0RieKEIFLNXQU_53xGrQLqe8B6_wuexHl4gh6sQUvLbnA81DtNzaUjLAiXw8W_YFEqtDXY4Hc-hFrl9FD62TpIH-I7JBlhGU7t5lkN0T6RsFnQeB39kpWFy36ZrzlNH14SrkII2hbk979sMKPpG-n7Deu8zfA-20kPSVkjBrB5bKA6cbHEe_MpHsu-94EJ9lxz90EPJ-q59nbm26zIFy9qKVumSfkx34FfCNqKFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlB_TvTNVRGFzk0jzGH8LE1t-EepdCOYUsQ1-n2XnYnvqKJCgM2gfPAnNlW1Uo9A4aSuqZK7rhuBu0JhfOClp9hmR5gd8RivuolpttdbU3dNTBL9ww53iPEARI9mzNKDZpBXFqFD1GSoMxQd-RTFo_-P4vJD_BUeHGC9MW-RdnTjvSAECtbQRSJdHWCw5sS5mZovDIjkbuEJQAJnL83DZJOBmSy7kBgkO73lDQMlGKWKA5SbOR1MKFH37WNZNJ1D5Em0ILPtCt5AHR0wXMtgMvz634GHWx4i9Q4QXy_ekBbD-aCm8rGbl1NKFA6rLL-huQ7B0ga0YXJNYWcyGJu-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyXBxu1SW0DsymbDvzvYI7KZHNIbHVTmr6N5GAYLjV8HpAhOE7wroxRa14n6acWbDGw1hOEhSzOdlqGD2MUkXRUiavY9LEv66o2KmjNEuJnw-xpX_VNSq6BElbAgdslPk-1k3SMezGkzl_80tFF4czLCeiDLMGUcVRmWrt20dPiuzE2AacgarkT_vlW-IFeFXwNjbLs3q73CCKaRBJjZgTFtmaTXFLfet_ukD3sRaQnzUeCy_2QJyqa7RYbZmBWe-n6Yuzorh_3IkiUbBvIibW3YTuAbuK87GU72UwupXFkArEQ-Z5RbmUbuZpOj2jpf2LRtiqTVYIZyi5caiZPwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrwtO1rT_wBBdBSFzkOOKkyGmBHmCw2AOtwWLQ38zg2Xb3NUtDR7YmIpjYaWBv7U_6xqEk_7_iOz3tJm8weGPZ9n_eDB8vfx5NYGfEPC4S0eXtVwMsFiGgdrCeMW3aUglPoKie3NTtYJPXEiHwfpkozCSn2e1Eea-ztKMreshk9F0kw3zq8Y3t9xGLH3Z6XaEUF_L_c2ux0E8IhTrz6omXorLIDIuMYtj9pqilzQHjA3ashwrQNFNarapfO50wVLk1TzT2WJ9yMcBgC7ucNaFZC80JaFNoUBXOHr-b9ZDnTDFHE6x8IwyW7XdS3V7Qhg5EsJi3vMJ0qxfjUaKIsYyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-6DtzKRQgv45eAUJy-2eecQ9bQ8eQJJxgW7fPzufKgboiFmzwmYP9W151qgvjhWP4LUifii3lzlaXZxgTaIoCmmBmB2fZSDiGC6LYNBKlnnpPKa7aipUjXMYZJAnc0Uvhdmg9Ru8bcGnTPa72VkS2dWR2ap76r6XCyjidjGaRt-N0YbC9aOl-JMf-_mn4CtMdpp5uLFjnkSbk_H9zs6beiJKrZQKWdZqwgOBD0ngnnJsUYBpt80x1uZ9eV5oMXjIdlsq62GF_yW7f8ISFt2TTcJohshKUGNAA1WEquHMGnM_uVoMgZRftWbx_S41Sj4KTdVxtNz0avyBTHktus4iA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=oqbdzQ_V9kS-JtcvZ89554PI8LIV2inCB36DJpkp-LOi3OffLGzJnZ_hauYYfV6asZbTBlobTrl_sm_-KassLa2rsB9my78hmjjGPpArLzxSG4lDex7c8N246ulplHLjlyz3ZpJroOS3Vpb_1T5QxBYwuwZ_V_i0_3_EL5yor66Sb-amoR1fYYo54wjb7ZRDVy0fu7myehdbUAbOoEA5jhrLRUp2xNru9VM5WgdMFlJ4vjh6Q0ir0xNRffGJNQW2huCEnpDwCVwr-cUoS1im7cj1IQuaOzcK-JAuAdz0Mvc2SuLaGuxuLd8SiVjhxNh4XMgXibtMGvKRL1ZmHhU7Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=oqbdzQ_V9kS-JtcvZ89554PI8LIV2inCB36DJpkp-LOi3OffLGzJnZ_hauYYfV6asZbTBlobTrl_sm_-KassLa2rsB9my78hmjjGPpArLzxSG4lDex7c8N246ulplHLjlyz3ZpJroOS3Vpb_1T5QxBYwuwZ_V_i0_3_EL5yor66Sb-amoR1fYYo54wjb7ZRDVy0fu7myehdbUAbOoEA5jhrLRUp2xNru9VM5WgdMFlJ4vjh6Q0ir0xNRffGJNQW2huCEnpDwCVwr-cUoS1im7cj1IQuaOzcK-JAuAdz0Mvc2SuLaGuxuLd8SiVjhxNh4XMgXibtMGvKRL1ZmHhU7Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkBMVMwrONnprTc_i8YZjDAKaqAWmQf6U30RB0mVB2FD_RUBAAOSPVFNW_yvk0xHjjeoCUKwhUU6aWn2ebt5fWIZUe0ldXt0A2nI4wnMXKExKRiabgrR1f0JvDL_HuitDKt1KrqvxKVp3DTQQhWRBUYZI2megas6qUNbVqU5iQmOwJmbQF2yl2RBONOJaWTYX0vx4yisHcUeEJwWpxq2_PmgWVmxPZ3SZ7k5AQuflKbKCD8_ZzCqsl2EBronTJmhlYeEds-bbvD2ghEiargBuBiNa2ah6wlU3XK_NejJlMdvB9xj5bjhb2JyFiXbUc_4qW3Yaq1YjEuaHE1AFfz9eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj_nDLslMj0PYT-PBIrtIqWFyJ-qYW7wqSrxOcJOxF0JDodlg7YTDQrUFFVGXxkiZ0gOJrRUtM1xDmoNZw5K6oRRKRh6OP8BwM0jVUOPzmc8ykp-QHMDtceTlas0u1mSE3dLIEmpQGe8elRvQz-msCZWvKaXv0RS9pL2vhUm_jJj-skaZSvpYqD8_oBNK4Oy8h8MT0GckpYiFWHnmJZvl4CGhXoXhQv3JzTpuBfNscclpCbALXIAHICGwHv-wzq1NH2Hd_ix550kTUa8K-Xz9i_cethbArxfiAaXQOhD-rlVmCwJFYlM0wcqbPA0qOk8n_XQ9Vlq2EUWdCrmNCmcGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfuN4X52Qs4THsxqs5xabxFB4pT36-36N1KpCPQzxmI1gIcXkonUkulHXVFqKmT_RInnO8BDAzUUZw8rmMbd22OiM1oth1Zk5IOcbIzJpOA3ZPFYYRf03MqhUA1jfSeHhN8o9TQwa9y-GtPJXMUqyuAwPBTqzCfXYdggt33o5iFo727P-oC8vn2So8_M1pOt5UmjDQBDB0gGt2Bwr_oImV82tjAyrCKGymaMLMGeV2eidvudRCd_NbHx8Z1NIyGb0yPG-9P37izbvmT3YuoMhA7sL9HC31wi6_d_WbmWdhqx3OGI5SXU-LFAvy9h6l9Ciu3WF-r5iUYMmx8rKMc9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfHWdUwPLbh2pKIbJTmTqVYVxEGF03SqskCTcTWvkznNX5A-ADXPQNlm1yR9o8emIDr_2nFhyGoQLbD1iDqWmhGmxI9mZVhj5lhnOQY-1h8BA3H9qfHkjP3KQz5k9PrQZ0E73C6sCDui38BKmGjPjFMJmSTQAo_bU9yBYtkyxFpjVdj6pz13EjQLTziOSPdCO3FZsAAu5hfv_wLr3wSFfAYybfmABHemArfCnbzngBvI0SdMtLppg2Wr-a3UbxN9pY5Zm9ARF2XCVIKA22rcUsDmhULUV4JMv2JaU7yjalTbqcAGB-TDstfH_34WfmC9lJKF_WkzwAmlNc2PF_tJIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHZEoLAeooj62OJNGL8UvgpRMFFPG0qMPohj9wsVf0ksQaT4TclPR2xKhbamKQfP8Pu3t1J5BcU7m-cusJen7FiU2AVcMD9IlPTy2OI-uqMQFzXHq_Om-gnu13vtyXjMfUziud1lO2doJn5-0RzpuXwtv0z_a79JepdTkX3TpiIzp1kZBHlwSViJjuJifQSi4RFXi7YkcOIZ9QLksUIlaV6eogOVm_GSQNMLBK57YREwXFVN3Srf8Y2IDey1ZfIilLK-qYEI84hQmiWoW9zjoKPE7Hmb94qf4c2eAdNIG8ycAQfhvrpFYdK9MFDJBqHowPbCHtkUymL3SUkL-QQbaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtkP5Bp1gXiAn3NM2hfMe2yilERylTuN5fgZYqGY2mczbN1U1RqopARQCa29Bn7Rivjf1bRmf0J8IgGpgtBZFXvy4VuudvEKRtDQFIITpzqjYvYGnTlf1q_B9QeCgxRxzX1o3l0jbEOrdT3xvvPyEHTeUsaiTI0Olx5Bi5KFxhL3YE1NPEKRC7gbF5XkwBz5YrMnHvHWi6nuK1Q0jXt7HeqMCQgN85I4fbRwjfYPOEJOJ6PHNiXEc4_StyX4OUuWp7YPtqx5MOA0jk4LvMgUx7WOaxsGTuv45XXB0t5zt75ukAzuMn6EdOZSpaTGwAxEIgyRiyBKGJ6SfIoeI0ByVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzLPnDDgw7a64ObEhDc5srIToSPMmtOnyIiA8nXYYqbJf18emZI8CSgVxkbPyXUGGDkHcjwhDp61qU29pAMkKAtAO0WXvuwMSlkGHG3horgsZIiCn6YbB9QNlxzYAX3OIPg0dwm6MvndGRGdWfTIuq8eDBrBNmKrw_I242aqIuX3mL50QgJTiV6rVHv5Kj1YrWScwnslvxTxaINwwJzn0OYEq4L2PVfSDDI4K8RCymfpF57j18YLY8o4VBh_hRzMKUYrxnWQrvNCwCF_JYXcDuFZ8qH_KlfcuFCfFDL0d1hUEMK1iVlgL1F8MCe-ktitT1oW86ckDVsn3JfRfiuY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0OILnNovvPBbOR0ebVtmRIajR98hI14BF991HxPaCPxF1MOmEVr2a1RjzbD0DzK4tM9VBoBntXbyYiZc9zj99Xym1S4Au2xqO6nsnEcAxdk34lwBaDuhifmpmxcnfRlaR4J2kOSNKsbd0ZVVsaK7NKyZCh8RgRYdkUcNUianaPD_YP6gP4-QTOFzzxfQDIOmYa1FM2O29I6OkMHPehlcZhYVRYbN2tkXmqGvd3UMqk6aAbs3nz1-524Sv1LVegq4Xhrj204KVNF8JYhlqvHWw3CsZzXKsSZqcyhvHgTd16ZS3o6uQrqZaAq1qRkSXHzws_zx-0SckBttlHNOFL9Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_G6yDXM2VZso8k0x1pFfjaMHcJTOMHVM777yKaZJLdUgOWU12oLjV7djNYoLNDbk03x4FtdOJ2yelbeBNyX3sank1NdDfvOm_1HmcPkMaW7ZS57mXfuS2iHx-4vrPSByMw3XaYa15sl12vLhbJ3PQfYcukbbZoXddjfoeeNna89XjYUFmAV-spFpclgZ_BtKRhxd1BZMu8Q4VwSmlmldDmK8Qqs17Huu0ixqWioJCG9R_HeMV2_25wcm82gtv1yvjuE69C8rib3Ov1AMk0OWN-RHB23X8ViR0R3xWmjxx_cZaRQbKwRaa6985mVvt_AVDOkhIkSDNy03w2MI2eQMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS9zu8YvTBf-dPBAi75D-mQlIcpTkORzoMhg8NpzjhuOOwT5kpSKdK4F1qV04hHlIFxzyyBoJeft2MPgUI34jE91X9pt9XpC9fjV0LxTKQfjWUaJ-mBAdWryfNUlFzHmAmgy9z3ZpoWPU3HvXeIK6Amm8hOmXvQ0UH67CLj8eFWeRaUgoEqCDmgR96Bg3SobmeqUOuBGM2UmYijo-mdNsCUpLUJTOAhQygRbydynYfg5thGAkJMYwwLkPPipnbT2D22v1x3nF7EEH9KVIRAjsKs2iTgXCFIvbd8F8D-hrUxKymoY0g7LS1mQVN0gT1UVNyAHXYdP2ARcC56C684iJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0tHkVaSosfq18eePxy8A54-LLjklj-oldgAReOtMf24TZU4wRSVQVcBa3xiUAnj69EL2rnRpgw33tMkq-ZwH-fWmAFfWczySc5Cm1-h9XYr5R-9YGiC3VdM3_ItbEl6ejzqcSktVVwt2cwCloV2NUgguDn6sBYmh-57tqSiVS5XZ7wBsCvb0XtDRhaWfnosGqOiCOitzzECzwM4qu4TVdKrd7buvh3igPl9g9Xaw25RKlfvdvwuKkAiS9wMI1WeEhikl3dUWr-NMyoIjTc5mwpDdgZ68X9bkmnbiDcYVmultFx6WXxw8bJA0fcJaqe0Rloj8IRvq_FtmQMdBUPPuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYmnfxqt08iLr_6lk3hSMvMPZT7T5wqzY4uRRAg9KFfAZIeYAysk7BS9mps_IKohfu1miM_UCfldcwW5CNW9KjG8fBpCbj0v-wZ8SfK_KoA4jXy0I6pvJ2BTZmw8xpIHU5q8CmBVpsStU4NVFUfkUwt2uTVVhQtaCU1KIg9QyvKGrOERdGfG3oy6adsgUP1im83Ax7srl6aRAsM9-mPEmK3EOXlVFpSROIbqboxs5uThhsvWJr2h-TNm8EGRJxxbqm5tqH9qA19CGgpW-wxxyBJ1tSy5sZRC3uiXaDdKn2MypCnWzogSbhywStDEHoe3lIU0gqLSIIdIkWA8jvdOlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPBww_QPTCD9TFV_YNJDGJK1nwNT_Gcy-KZswDl2U7NQvGaAHJftoR4CJPNUp-BL2NzLLA0nlu-XDtDHZxdgIG0Mzqvdw3JEy4d_eRtfSxPEUXgpINt5bQxS4Qylrw11LXL793fOoSBwxxzVekmKHLAWsd-YWhe1VZO6FCGK1LS-hR1RU5h8JRpvjXEOLGQF_uxKZTk7AE9uctdzAIQWKaCZPn34JGDDzOcEw1SCGi14lmNzsGhTvCFwWIhBUafb9WZny4Ec-KqFubYOO7GbPEUcYStn5AtitKNLLTw3NBC1QCBUjTUZ1FShDkWBF4ZlyqUpXM6rn_BW7xIOpiw2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_dZGoPSKsMA1g4hXWILia74Rm2A1OV5Q96Bz7EgLxElWUn-upqeENDwRt2FPOmr7_mMZBTnIO5gWsI0dTAJGZX8Wip9Yhbi9-cw96BFtWO0ar2ijYb0-0reQxd5s_q2cQE_reC64tvjhEXfjrFYE1qeEKRgHnwFS6o-YkmWy25q3yseAGDjz71z2uX8rlR23zGmsVDxf5bcSLRyOZrzb2VyGumdIsthfyoE_KEL-rJjiZgpBO8H5R3ESVAhqW3CkLDjzngWbYJuAp_sEa0adt5gPZORq6w2D4IyGpTGYUlbllNLXdiwn37opLeLF4Noo427wdROaTizp5R0JyVRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1VzMta0NPb7fMBshAdwdFGyvjOwb1RzAk-QF6fwDqXcdq1p_2xJGs3G_fKwDEZag6bARHhYUFK7bV2uFKq7ciE05AE6YXJ9ygeunezULgV67tC04-03lJ54DE_wm9XuP20-cZczBf_jBXbCiwIdGW248vuEmDPbC-mHcp7OwSKRipAN4o4XRSNmLwiIKGO3gXNl1eoYSRREvdShbZPkssRjhb3NVZXN2chnMtg31fcu5HB5HUbsoBGc0UEtfMq5LrwZeml47T5onP2vUCiIdPC8N2C96yqYknFvTH8fo_0XsrWpJICRReBxQJqHdJzJyeXIqYhL1jejIu5FkwCimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUDNJ9y7E1JWhWxDC6zytrRNgHsVbEjGtlIoh-zbYKUR9_ElbVlisrUZCn39o8J0YcR0TZi-wopCn5R3dcGj0Gmm2veAbyDwL1FJp3bmzoZ1G0a8aSiwmey8T875WUXtp8XapkvEcOc93l15IUOZ-s6_xUzUrB7cBF8JedsUGsLxcBedSar-pQuIrKrzKbttHJtpwZA5hGhGygj0RJG-nBSu75ap4aJ62esbPc6DZhIfgIoHeUNqwItaa53LgBe-nEWKkHQCQE5F4M7M-YR_mQRiBxYZ8QgjhA_y7SzOGfc_zxl_sI5tENWZOqBpPm3mUdgTWVdf0g0i-Z7Hj0xZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Er4_5tr4IEdzyVU2q0ApiJ1t6fUAImVxOpfcBp7E2J9oXz7vNOWkk-tu-iwABj_Zn7JKBLZoC2QIUOEEQ2a5fBCwbq67EgWdQYFEurQVQzq33219V71Ng540PtiQk_LOCPi97_X5wWC7WzACl4BZukBZaTAvUbM16z5B8SnufnZbcxHgMEFT-KQC7ACIeB2rPUKqEaAEDAIC7FCSiDLlajeJtyKclHDLiKSsagdNMvX2Dcawqw7vJB3RASGp2f3zUtaINUeuQdQ4NL_u-4lrMHRVBICmlxsx7AeJHM9S8N9lE6gk3XMci7Zms1NJn17jMzZetDVqfnPnT65AaImTpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGY6RwnCkjFKiysgV1kbDOiGZ-JSgWc8A9dmaYcu8ePBxNqGvDhvS_Rz1RjZ0jvFRL9PDS4d49XApn1QVdby98o1CIOsL4Z1iXEeeIbvh1KHjVhn51ltd8Sged3h9Y23EYgAfIPcBItU_W0dueeOdjngtUM5hgZM-VHWTrDNwZfJr2owl4QeuQ1QMKyhlm4doCBrcAZEgGjo7EHWteJefBJb1fMvkCI81CFcuNei52P_2n_7bBaaZ7EUAxHJdrc9aH8TYSRl1Zx6hdS-FRa_p_qXoJ6LwT7EGajByvWP_UyerVW9V4oizBLyb3JYm2oPTt_Qd3Z-p5VZJ3y2JBbbGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHw6UfZVWLagp3_HyV2BPb0p-oc5J09CbOy-okl8KstauvQrjEtuBnWlVm4Gzpf_LFrfwhD9GkIlZqkO4MoV3HbiN9PmcwsezSX1MjIdK9879uS27vRXUhO8kuVhsZZU-DGp0kQcOPIxKbeGajhJoMs1Ha9XKSl6uyWzRyrQFCb9tGV_yXD1jhGOM6JTXeYv5u9ckpMlZNAs7-SgwJ7L1lbVfpEUrl2A-ydkXObkNmu7bq-SaIN_ms0Eb0UmHv0O6eZdxYYwl7LMFcRmeYJfxWkOryZgXXkkd8ETZa3cpqv6f2NHLR223KLRbfTONMYlrobu6DX_SNkUSpFysKPeIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqR89ha7dCsn4M_kol63eHdkRd_RklT4JnPwznpytmy3kNv8hPgvZRIXY2rWcUNrrXWjUcEvKyueodAEtu9A96xak5Vg40PVjadRp-54wI43BPccMnz5TmDA6T_aH4S_NcOwuHA1JceLeWrlcwO6xcvUQ-2mcXy6tojWkKRJgukJ2IGWr0W3LC2jf6K3i4iEud2yEdOeKNn63umb7G20YvRpAPwDR100GSi05myCML-4VKJtdNg9-sNjerK9Cw8cnriNAtjQxdrIaLdkaOZXxaq3Wy59ut74W0OWYaMty9d-oD3wqlWn81-9AInd7lnTUhNn3l8fUjhKZqQj7lMTqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-PomYg7Nr-Si45KMteZ8LiYGBk2XJENSE-josI2zjAwl3q51YX8xizRLxAl4t3H0Fa3WDaHn9Kb8ONDDBj8XJ4YitDDr22WE3d27d_YbVE3aPdKzFIP83KIcLG5FxsxKXTKRutjFZItKVzB2dK2-0Mc5va2kxyVmcM1RIK5s6lTNdyFODZ5XZY6yVxotxa9aPbK2FH90rBrgrOKcmxFpOvPkEJkvOEEcb0bPrXmpl8oZN7bkjhz17z1MEpx6g6XSRsb26rU_7NSFyeXbeCt579UgZVpveLLDwO5i7-zzeUBaY1xaxSOd71gnz8L5d74yBDtt3w8gAUF0Elu5zyz4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlxCdBKDe5BTPNFyiaMJ6XmBREMt6rwGB0S9lSNp2P9IUiEsPQc81Sx2dmDPxzyTU6tUO8hQ4XF_eEfxbqWrDo9yMeyfpq45FWukTtNDKNqNnJxrbfb4hUZXDhXz5l9PMi7ZviIMh9smv9t-3ot9BrUf94jhAuuTldlwRSIH6zxlKDnVa-ZVjDweoaCLYFmb0qrUq6pphUaIeAHPQB4fMiKlNLhRKjnPFmbowzy9p8KUpT2DFj_C8CKG0orYOSQSI1tea5FCpO7fbH0g-9J7T_m1P4Hqla17MlONlheP-ufCmRPaP2Yq9FXSMgwAO4xsxkIR15wBJA-oCzglwHk36w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5gl2HLfjNbUJi1OU4420QX2l4zllZ4qpEOFbhy6sp_XKY8NOsREhGYz51TfHbIuOuoAOtWQC5kz9eNkYCIgv4XHsdnKB71VPuNZHYmV6ZXWndOAdkNU4dlybwEDHPNX2ivBxJFgFGMit99Pmby8AJKU-njDhhYBvB3p4WElyQuGC7aFjPEYZuMNjf1j0biTUJgOipqQYcKAOD0KwK9B664JYhcv8Ltaw7U2ENbb9uImrKjg4H4wom6hbc2vjJQVwovl4HBbZh8pDB_Ok7WAYtsNTdOcaOgIfjukrrk87EJzMsRMNvEivbcjyT5TrxuZfcnRhuJx8DfFUmKFz7SV0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJv4FpZRRC1OEAvKjmV1DkvCfCPgvNRpYGOsGjq6SLcSVipr6Kg258Jv5FHJIsJpes_6O_Ta0325KZi2PxV8-0BaQnGYo78w__hz1VmO-fIqcuww2rk7O8zWSPP2k8fKD_gjLHsyKeupIUnrP0MEsJTkeJOQdt7H9XtnNp_hKfaDWbX1WsS1PmpXyyNsLEUKO3L4Yf43ckqq8a4Sou268EfDut78OhnG10afUdQ1RAVIJZMEIolzKhhuBWxEWb91OMo9-emf8lVmBcqin_vqed68Jdqp0F_IquDr5pW2q6fra93o3UeL1EYKraKZwISLLlVSx2L1RFQfRtEFA7ZMxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC6XD8Jtd6yg4zm-5T8t1aQC_tS0_mBs4iFlvwLhjawZc0d6zlh1vo1dARzlIZdyY7eQ1LAZxkqDjEUa4yqmRupOsuRYb_YXu4C_HuPGVmCv3qABdyGG27-4EGg4oDeMcJ42aLOmoUuQqyCcr3medhrFinXv6aUwr7zwURV3eSsU2myGYdkerHb_Rq4fWJAIlSdrIbJbqoY9IcRFC1O5vMCPtBizC8EEHt5SMgSTHrRdezKovqOXh9OVZOLCD9aT0qzkllHzfaEokqAk6M71yx2qM8fKTYUoj-RYQKqxXcPjyYPHCht-_i0OY0TCpoMAf7HwTCgbP4YA85mnik746w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHAZphozcJ2XM9t0v0V8KHs7j1Z4I0atEX8kbeqRBI7QU7ZkIY1my_C3z3A45G6AEGEU-TGSvUVIw4ZQUXdt_rkBD90uEh_R8qA2H4HNBnIfyx91eG3vTN48Gk4ytpTpsxOU30TlwV7Toa3vKQPp4DOjtu-ZwlA603d8DAJkvgDrZHlRXiL60Mxk6mKhiehpP7p7P8dJnbsr5OzR9QWvvb0H7eH8or_YclOa6rG75Pxpy9iAB0Ig_ym3T-ct-ahWIY_gpMHkOeFk-eqHdZpWZx2zvNEMyid2RI1roruvUGl_q0Gur28ck6x8ss87Zh6UU0HFNzqCVvSAgUvIJK5s-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kdjki0Y1WHK1r7PYMWy2xadLbr8ZhoHg_1SZimbxOhWLDsvgRZQHKcXdJfxBa8Kw8xHhJ05220x6trz-LmQZdq6WT7764HHp-hhFfbpo12ajmkMuONaLuy9mBGJW9MAfNWRkKstSbWK2_ustoYbpyntbac9MRSYLAunmuviOXaGFbhKRkmxxVBcPUi9KuTCFaEEREeTkxRXknGSzVZ2_sYeVa7M1sYkQirPcqtp06G5Ek5w1Un6mi363sqcQWQY5ZAdFak0iqIOBNTNjKTfTNDASNl43MUD5wj29vu2myPOGW3yxxSjYZqRbMTUsjgDT2wsLi2IIzmNTL84GKud3lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvjfmqjsFvGUCVcoN3XGMOAJgPh51krfWvDSisrdTVukmuIsKvsvL2V9LgTM-lkT3k1NBU3y_86pbf7AwKFAGj-mBStuw1uyYNBzMmk8i9Pj13vahKbBOBNgkgEn2jonCUiys8Hpdxe_O73PIoU1dzGVVm56DyA0Wbl6RX1eY-oHzoVO-f8_OKd-ya0RYDlovV6vIwig_jW9IojJq4iYGjL45uQbP6zdWUumnQ4q3RJOYORhDvvCmKjP59XDR3MF62WKU8mPXnkmB9_wY_dNIrVK5JHkoyDU4vQBjPCthkTNdwUcpEXnalFFCvWUWXNJTYKz_gZWfFoW9ItXYIKbWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoGYEPK96Ym53jHv2Xcz822o8HO7tje_CbCCfNF0wGvupW6-tTVzSYyA8JSDowfPMp7IdQWKYTZjScSUc8Sy2UoUGz27RHanq3f6lg2bx5-oC3IEo0dY50gDJvoxjwUCCtsp8r1qvr0qG7Uycj2f-h7cCSh5R-D-umgvBut0gIescxXSrkAyxZtvP6Xi3R_AWkodKjE1QE0EI0aycMfzJdKZc6xowDtGZT9zje7tqrPOZlXcLWGGIKOMd7kAEbd2OtVaYxFGvqNwRab8sRu1rrmzF1DrrmO55tYmjfe9Z3ExK57NWaHghTJx0xuI2uJ9ED-dbefG542v4Sk_l3aU5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfolwMdE8S27uFk4feMYIfMBjuHmQqybQQwBjRpHiCe69yh_vlumlo3FG-9SCx_pnDpgNFh6QQ8WcOMtwSx99_37yOcD2h5OaKF7lvnVx2Lr6p8m0OJlQC4EStaxrY93UhgzsYnBBYRX0XjBlW9FxGQYPuUgCIdB10DRgY_0VOVVLDWoElHmdEIN1MU2qVh6-A2USKYxmQWO3-IKoXQNjPtCFiA3DpNiJtGwZuLSAt7HfcYWQ93DfhsDpSZ0G3S0zeU6vzKQafTrkS7RuM_AcK2yKteWw-i47-Dz3Q3jpa1Vuayl1RPLAsJ_pkWzniVaqOcvMMJ1RwFE6kIrBI1f9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOWCkLCzJeucCmQRn_OvqoVCFcjRU0_l5ss-Dyo6OH0xzNvdjYuTDdfUUaampcwOs_EfbrBKdtP8AlCMeQhABF14uerptmbaCP7uo3HlLV1mXQT9Om477t4BkyFkavXR8kPBeBbY4Cn2jg0XfVSiRsDcmEffxmpsY12ZkJ0hgJL4e1qn7UAGpWJ6UuECJWuV7PMbHhSJBGCcYPP6jGWdwzc6eiidlrrGEMJ2c0_ClmJQKOFh23huCmzwS28NWXydO9qCw5DFHIWkYi0H6a-TMmsDOKrSYefw2ycBmD9qOya-tZTLhlmzfb9QObHWSV_3hBqvyRFCMVNOmz7sWY3IuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7zarGybZ4roHCfLQLhSEMI3euwkhqG2V5ChQNKdla0icWIHpelY8XZA4hadmahQxJ4uDaM2j8tUEgMGniFkV4xQqRqPA0jsl6Q29T9QE0B7DYPHsKyoXbLAMtLUzAY-csnU4j26zc_eGEGK2d3dKLcrtBv6DugQxuVfq4wMi5bY5ygG7XCjHAzkHlGcFissBfbf7A3HSbuBfABzpXU_DmizqK2xIrk4JAktT7L4MbgUiV-WTzasKjVXr84rHPCuhaayGcl8vlrBidJicaEbYFerWJi2BbWyZhV6_6DPw7pWcL-iyD4jGhRcsz42UPqu6fTcFsS98TydzDLcv4988A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNz_4Wd7tHK16MQ1jigg5G-IPS0wFrC4rBB5bhhZ0o6tQViJ_DpfKYTT_iiDsZrJO7IQ9RyTGnMgh0eT1ndxn8Nruydgxwp4l6-Ed89WVq5vP-Q7eA9pvYHAagusxCvvkWehG-oSZwQAJNcgouwuz5p_70Xudl3etCmbX5iPY6nc6zo4odUZGn4E7zy2ybtnL3d57Z70KcTF_Qop4G7S8u3-zUOhcuJjw8bbkdFbIqhmBvFgY3Sh7SIfqy3Xi7QRJv9DX_spvT0nkxlHTPg3FIeGtAj7mnZpBKoMtyN1ueheORg-HW9O_V9hq7qb-nVOWImcdtxqo8HJaWWPSMibHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urd_o5Fop_X8ZdMRpW-CHK87oppUcVI5uvuWDYolHv92wrsU-b5nJGV67dTn1WxCSEK5BQ7z0GGultGBXP3wCRA-Iu6_ARton8hCAMZDnAAiaijE65O0B92lU9sFcV0YsOfvJEJkhKpH4fzVKhiNh4DT0S5MHovsWEggV9vF2jvfEYaG2pnnT6D_mziw8-M6rE-2q1ucatybyhjkrY0j1mQ0fSM6LyO7cImND4pjYAbDVEkyHXQNTjZavX2hJ3-vE6WgHX1zQDWcjqjnIQmgIA6KyPNnwutGdv3d-2YM3pUGWhn89cVDJuXZ3KuCBnz-US-VMSJIWJfaCZ0W2vfNDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8JtFPTA8t3Z5U5PFozDJV4fegtYvvbnjuydLeIdYERHZBRlUA8FZN7yZGDj-q1KrBAS3UqqKJ10NEZlh5C4eW_ycZhMcBxwNAisRnfAP9zMoLrIEKty3Doo8JaG-6kR3W3JpMjH9zTQ3hz8piLV7eOMRPAgLHiSFfNOv0oOB_jybSv0SfIQ7uN6DP3HkpanN5YEYdQpj0SPZECoxjxioEAAK9Q57m3Oeoh6R3vl-yftZTUqwPygqHklw1qF794MAGVLx8bN9bfMIDmHw2b2buA-4CVpwt3FNKmi-d6B-JRMKKUayewcKaXBtl18Woy6TRTaOpIDyDPi8CgjQqF2ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jii-Zgr8sD9xEsdG_HXWSha5xdbdKl5KIViOh8raMDFpSHPulHdah-cLB14O8IJnGj8RwpSvg0mWIwTweMwHHLNUhTuok83Ej6-nRRy5rlcAfuU70KVs79chi8eAl3l4t7UXK3vDBr4S763fnWAu4V0zPPWiJTKRwuo9WTRIOteyJhntQ2CEp-QnFf7jc1KKUMyEgs43RKOniREGd3j56BGNvDGrYKczHEGsKR_Da7JCy0PvcVWwE-4GWUIZhcO9Qw2ZBsomrzx3kpqLf7LoQ_qo1myf-Jm_cPOSBUnQHy3hGH6UyTkbCu9RqLxA_oUhnkIo29SyTnDaxM6ZUnnu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCn9dwW77ORvj2Xmv28Nfc4HJzQ-NXUUBh5U1b_8YpYXY_8RopMLEkuiAB4mE_uKCd5b4CpRt7t4-1t8Rw3u6mCseXFCmGlDqUA4WL6Xk8BbxTK8nMYgyVUi6glxnS6MiQhIrJD4iM0Wndg5M7dycpiOEnVlJuGqL0KB3g9D4Y563IsETpZmAILTjQiByW5Bis2j_A_TL58cOLzk_ZT0IOV4zy0vusO1JZYn7DA7WIsSOa8HKKkT01MkYL-bO4ZfldSeVrDe9ls58PuQ4UgDeYm8hebc1JrPM4RerZQZ4dfuGLzjUl6jruky3iBNNqjK7N0UQHWkjjqYuEYNoTAImw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOl8Jtu24_DL6zS2eUWLALA_NiIpWy9o_lyGojIXjk_kRk9IsC-zTw2Zxe9BAHCT_n4l-TzHvxHJhETF0-sUY8EWuhef_kfZ0UpvtBMNNmyT56mHHKoA7NvRtK-Peoq_uWQyAr7NyHlRifz3TeqHrcI85rxu9eBGODrhcqtftU0Jnc3H8POg8hzK4kwQHkQXtHuTy7rHkOcKiOogN1t7AmMqY_H3IDy7TLA-GVkyPQUZD1F05RFD_SKFPLYu3L-DeWoCCw2VO69rXcMNbD0cDvr3MQsyrtSLPGP-X2Y-J0owb3kSKEMJYA9MwI-vayX5wQ8UaC0Ei9gzilztCsV-Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXeJYcHDf4qmpP3nS6Vm-uRrBO2a4r7SCBkIqlrda757SsV55kpYslQo_juNyYcjmFdaKAVcNtEwPUvAEdGx41wNcQ7hqmBbqzOtAlW-svZwxcptQNIt5t8_8xqeu7ID8ylSmbu92yzIPGKBIhXsl4EQ8q1Wezmd4LpUssoNR7FgUNWqGCjWl4jl51f6Omir-0ran3V2-RGo5UgHvr1_IeyHCigw-dAOeoe_W5dOSPFxMxqy_6liEzmX5AW4mci0ldQm7fkBr1hYS0aWl4vgbAG-7oP-I9jLIGINGjPaOzO7NeFgnu3Qh3sh4AMSF0j5LowMcy0hQ6GmtHZzHZK6Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2reyT33sdQxdkuQ8HK3uHsna6HAWkhiHt67a0DL8HokakkFaQfqeYW43i-jL-tMo64eyrKxoeUU7jf-zPKn8pSBaVKPv_QFWYyLc_Yxr2MYWmG6yUW_vnx--216A_4lR0qJFrJRWnGHphrxEOZ40VnfqCDu-dOgRK9gcy-LMnMkKetUuxNThca4EU3DpoGkO69UEelT1re24krb3N6EuLUVTUINhO5hQPKnz9V6_J84eTcE-nqL4YhN6NsWWyCFcA376mkbctchR2jBJWeWTC1oYXc3g0sKGVqm39pYQSIkRYE66mvuyLD2DJMuD7Y_23lFFNmjm1uHebTDJbWkQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tr0jQWCbdqYng7lYGn4DUYZnuxVe1nHZB9YzrmrHwxQEI-HHLiupje118QsJmdPVfTWop1rHsA6NOCs6G9H7UO-5gcOAElAcjOEykEBfuparbnYDwp4EBHAiaaJx6ATNpvdBNEG5x8OD6PWbPYIZ3msJyy_BhHwbyXkXg7d4ZDZnnbcnGTn8iXB5dR99XN0_1ahhawkmeBoFpqrrg7AG3UYw9LUMPths_mLAJrV-PiADdMwWzCkzCgk8Nmb8FtIBOPW71ivq1tK9rhlUmggUbEbrr_dNL3GGHGDS8CC4oh_rSBD6qX70ZF5jx0rpGtDWhYULVF4b1Z72X5u8U_NaKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-czUfy2mDeOHKDjBnsKijxOFRX-3KYkfWfeqTZMO00oxfKrxwANfrFS6viLFbcNdjcbF78J6jZXTqq_bcEE-9YEQsOhqsVUgBsRXxdqoDTaUCSpOIKvV3mFS8hgfiZwE__RuYbDB3iXuNTng4ba0h6-nDZHvvRMPDNcEQafUPauD7pGyITG6Xe-65jAWjFlOTx_VZ5e7AR7MiEExa4nHWYiTBjgx1j_fH-nqCjt7z7ZScOQd2KJIB_RXwAnWKzw0r-CFglvEb1a0DHwpCIZAAHTPSpBBdFGgAScSp6Dj93X-zQIa7ApD-Aj62dnloo4-cI4maCzHoZkYU7yZFd_VQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Cq2iJI3VjN6h9vJ1D19oeO5RkspS395WRLAB6UgVvxwxgLJN8cHdHkaUDO5RjVgVacHUdpnjv44Wku5TZCZB8RVzFTvIQYrVPuuMDSHHwoLx-NeKKsZtTTO2H74E8wb2-6-T1aM4Z--Un7YkWC1URVEHXBM5OJvWkfe6zuHsXfEt2Rvkt6emVfgFYL7VfFcZQAthIfjBqIIEHpYXKn25HjeOwPWUc9_kA-5eybWG9Xj2kI71gOp9rb53vzz1GAUSazYhUfv9WBtXnYZuignyTTJknYay10hA6ITG3M3RpQ0Gygx4YP1Cc_J1H7ZlSQsFfDxjFTi6epzDIfwHZH3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVeCcbjyNQqhFzho206N4Qji5CLmsf_Op5EPtep5YV9j8CaKvvJ_t96NtTxm1I6tFN2W01Gp30z2b82jZxFhZRJzFnvGHJU0IFZTpsV6Rlw4Gl8Y4aiac04tFYrrxBcH2eoFaWMVWpBHuAmkbPQ6TMCjsO2TZ31LIwV99pYy5pyeglbCDXQAxaqQmo2HrvQhURTilM5qMJhDXwg9x0ApiY7FnKX-xSlXhdJvkGsho52oPxfXn-5W0FSC1s7uRLHVFWaobAQqcwxIeznUkzKq_c7wJf14P5L9KXTrA-9I4ifEoT7jQcAUznAt53tVgfG5RtxXeXygsPC7EzbTmvcWQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaKwshgEdMEAZfVT9oUCCURTaD2e370KjmDRUe23ps29gSFmcTAnCBXcHQ1oRTkBWg3RHPBaKFRrKE1BIwx8Gw04WGT2wKH_8lgH4LZmrioYvNtcd-EeQFKbCtlsIa55MZ7wEjKkHrz04_8AH32hRrFQTqEXe4Bq41Q3aIZovDDPstyP4zVcZ3k54AubRxqUHYPn4id3D_FZ0GSerYqOtpibMRZTqE8sgogIyDt1g-CIKZoWpJInqacayGwjC4S9onBdCaE72zLjnT6MGtbfIfohlyB25ZbiD0zYQF9moK5pjRWLZ1H-rpe0YK4_MJIsWosmyll7c4Qputimg4VJng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJCTXP6qkTdipCH8MhRYo3-feVo6J1q97RNH5Y3MJdTOI0slmemLgVU4joRkh2f0krPITzbfZbeprfxpJ1j6C53GFxBRsiy1fzced2IEisYmMybHVe5ur5IHEbr_n85RyBKAt_oTL_y7IjFKcKK6aAnQmG8mAR4qjKXIt06sETDMfyS6BPWVhAK400K8HG3CpGfxBYSRElSL73JmyPwb7SwKR6WLvfUFcBgzMPwIVwXv3ParV-P271H_baDMArf3ec5Gayi_rkIBXLXcatPNKTZIzqLre6VgU1AWgyV1kevYZWBzq6fGVLemnKJQysqTQYnvAiRNL-M4ZhAhKvSJJw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hvQKkOsd6eI_Uoxjw3IU93whrfoLhMV-CNxH0FzKxj-OWa3tTA5DbHN3oYknD_cubDb7KsZhMCASXaFioeeLXzsGoWgOiac3mKrfMk869sXWJrU6jPDBQTxDSEjFLKykltGe80lIBc64nvNCcqM1J_qwnnmHg6OTrs0CxYGmgmW5ETCgSSTfVX92el8BQKvgNel60AK7DCIM3ExkxlixAtJ0RGeF9wRcP4j7ULZxbOcRudmwR2Sw3hdrVNhc7GVl-E9xX_pWaMHHt2eWUCae2pMNm2xYE-GZbXmvGgbNRJXXmv1IZFT-AvwKKofmAgQf55WCSwO7amCEuUiGDSvESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hvQKkOsd6eI_Uoxjw3IU93whrfoLhMV-CNxH0FzKxj-OWa3tTA5DbHN3oYknD_cubDb7KsZhMCASXaFioeeLXzsGoWgOiac3mKrfMk869sXWJrU6jPDBQTxDSEjFLKykltGe80lIBc64nvNCcqM1J_qwnnmHg6OTrs0CxYGmgmW5ETCgSSTfVX92el8BQKvgNel60AK7DCIM3ExkxlixAtJ0RGeF9wRcP4j7ULZxbOcRudmwR2Sw3hdrVNhc7GVl-E9xX_pWaMHHt2eWUCae2pMNm2xYE-GZbXmvGgbNRJXXmv1IZFT-AvwKKofmAgQf55WCSwO7amCEuUiGDSvESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4XVufnQc0xMoKWZJArqHoqS7gbU5FFhhuG48Fm8IzCnIYHGWXlSkwe6IM-uDsM1B6E65OR3aJFriFQS03qkTjzF5rL68vlbhhxhF5wZHm2O3zCOf7XrGBtiBqnNsHmoIVRZEpQ_8dkAP4ubr9wbQxvu0hrRDyr4_1c1p9coRjkGHa-_KvHq9pX4TYV3i2X8wvZnswmeGV9qg-Y5Q2_ttqzRsvZfeX-hEkgOn8-QC1U-GKOTLX_YIqWpoRoVIFRA6gWq-rd5ZGZrMLvzAbD145hTA7jlvQq0V8udGfc8XUOHGhTBoUpJ8aCpeOgG7wWoQ7V_0kmTvS56dV_qFkfYPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0Xt580AYmyVCsnr2Hklg9X0AYpNlfmOZhBe1uWBg93j1Bm0afGKaiZHWiACHRa_atIAf3NSs5LJTRMhAPHx2Hv-BuzqQ5Xz5BHw_BvAqC5k_KOlVv02H10Jy_qTfJXPlQkeizk4d0wRG-PPPXyBUf2iV25CcTsWR-xobhZGh0xKfVXuFRNibbcnB79mN9wr0CIG7uakMHoJWMzA2Hngz73k3E4Ue2_Z977SQ2lCzhB3G_SRTkLSqEGZ-2GbarK37HUVwzFEVHrRJUYGwKFd-Zb_dcLI2MHV-4weFcgyROz7JKTfmA20l-VdYiCOuJl9N-LgXMsv5teECP7m89V1Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLAp2Y4GeioHG1Sx6e2CXXWrWnefYZGHEj7AbiUzsjR9kqqAUHswn2RrVW1ym1bJTXtE_g3hW_Wt1WhaAXcMmvKRaUu4fMm3Cxg-BkiePBsdK9ky5qOldFt3uFmfeh2uIw5tX0H1ZiyN6lvWDF-RuOkPRmSHCNyUbJjQl_QFv-qkSaNEAbXmDZkLsDswpKBQQMfubhbWO_csGehVmRRq32bWCpFgG-k9wCArdm8xPu48Mgzs4aE45s6JqAbOsr6VsDOFBNb8pQWDILYLcCKDzBnD2OuAvi1auzZc1ABYZe_rvI5O5-89VKZqxacNdrz13YNnqQFKvQz5MrOOG5bKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyT1o56GLggiph86QYkefLUJ-yCeGxVbQUElB_mdke76czzKVD2ameGzTmq1rbP3IFkl2uTDQ12UGe2efmNDU0zVcd70W_u5Mtec_wDPEwhyC7yFmjXkUNM-LF26Igrijyaxl9CxBzLwR5Sk7GfrMjNyUh33VgV5_lwbC5_AhK2qPGWeMBi2n8BCEvH0NM73BCkabDitCGcOcHLN8Xk-KJv0Q1OgqUnCpAPE3K_LaIDIB_54U18XZlrcweanWv7sFQr1pOB2JFEoqLMiYSLHSUXzB2U_ln_mCImmAFZDd9ILYaJCXsQD7KbSqggNg7DtxCsekeLWuzxZ2imP6a-8rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pi1QUkt6RdOfaey58N3sH8xUfOdT4jQpDhpzL4jdfYzRmgA1moiAYBfyr9X2WelyYBR5jn0Ruochd3ZyQTtbt3JsiH053vIfBYB5DmGoIX8izj6RxRNIS3j6vfhcfWn_7Ogtzg9qCcgGGU_FzN4Nx507-8uINf_XbpTaYDqrwow0-90PQv50D5zHxpnrr1DcH_3Yjb8T_w08yaYERmDQ69iV7o5oQHkYUxMSDZwla39t4z2q7C5jRLrFafSDuvcZbWMBBOa5_601hUACZ2hnakJxP-u_iTPlud7e7jxtzgHlgR3_ztgu7F6VwmOrMsCNLUk2KKJigYmK5CgG1vK8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEswTKGROrbH0JriTCKNZpPp29-gd6dj4cbZjwQ4W_nKKibyqKeIwDu2UWWwBzwZCY4h9vsxce1vZ5D1VyLnojitkcqQPI4LQJM3yjXXs_O6h_UO2FaH1ecs3N44NC93bNoOkUQFcMOYEVvHoGtykeW3Iy3l0HoabW-VcR-roO99XOm46IMWfgEoMsUuEsOI7l8IjcqytbQwR8_xczz_AvxF3gpzRGbUZErxrXBIf29J-5WUypQ5jiI30SBXA2hmUPxmI2UusQ6Foy77bs3Dm-SvRyTmbmzGAHYCTpsHsgF-U8cE4WCOafVnO8tHdMAx2ErAB32AV-fvpjviA2DG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n92gvZQJaKoBffAFqN1hHZQyH8vb23h9ALIw1AlhuSvm-uaVh_MGdyilEE-B-qXNREj7xxhVWVal8-Wz9hkqZdiB0yg8HjZdkAL_no4GfNbQljLnZ0hoA-nZvd5Fd9eI9YTxOyobicOzBtwWHuePZ19q52qehEFgcilrJw6CgSh364BqL2pn3orkZpbxQFTFaB3jM3A7qOBHvmwy-c6Ye8_HAMOxBQmlUpFG2s6vh9wqUBGATMTbO5Rzdl7vOAuPomrwuojBGLFIbMSz32pGNRsjX9Y-5qb8K3lLiv9wUTTQScfCwCa3mHSuW9J-CQH3bSF8-9e07PN3yBu92CaPVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LFGGZp3JAkMOG7OonXLFBENWdNkp4osIQP-4muhMzFDBIG5unGrYCDCtPzPgI1yQslSZ-0c2pt-x2DCbexHG3XQcHpbNb14pxEdLeu-qMMIkx9xVqlJ65MgtpL9bNAbE-eAVwfcyKj6UZ9QkS1mvZJ1RRct3PLt0s1INCzewFmjX5El1_6olUY_Cg6sgiL6lWkBcmG9AxsRnp9FCziv_1VVqbyOP491RJbnv37sYrXfOHV9i1DAeiL-NGHvxQqVHqggqV5dpooWz9PSHsLVAMhiZh58w5PPMltj4hZ2Y0FV7p1N2dRDq4tW5HJQryiCxfXt5UONi25j7_81XeCchH2zATWAoB4cSXIDmNx0sErYpFdk0N-JUJf1GVoJmF2eSdxA6NBm9jkRuyEKiZNe0NUiN-tRt5Dz3WRUfodIC_9xRosu0n6PSJdCn3K94kAT-3QII_5lJ39zOGVFqafkCCffb_xSHkb4mrWfdm99P1weMGVDCFFj-9dOljCJOj-aMFffAISi5Wu88-_WScIFTj7nxTactZoOBu-ykXBHil4xJ1HMQQJrmQ-TClRMyBUn9FnSKa3RS6kdrtJEJu67Dp0HOMM_9BwrWzQaxu6BsKtU4IUuHaj6HatWhFsxf8LiBQ_X19ms2qpsFin7HZNQnKltj0Udfxw-27gck9-t2maI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=LFGGZp3JAkMOG7OonXLFBENWdNkp4osIQP-4muhMzFDBIG5unGrYCDCtPzPgI1yQslSZ-0c2pt-x2DCbexHG3XQcHpbNb14pxEdLeu-qMMIkx9xVqlJ65MgtpL9bNAbE-eAVwfcyKj6UZ9QkS1mvZJ1RRct3PLt0s1INCzewFmjX5El1_6olUY_Cg6sgiL6lWkBcmG9AxsRnp9FCziv_1VVqbyOP491RJbnv37sYrXfOHV9i1DAeiL-NGHvxQqVHqggqV5dpooWz9PSHsLVAMhiZh58w5PPMltj4hZ2Y0FV7p1N2dRDq4tW5HJQryiCxfXt5UONi25j7_81XeCchH2zATWAoB4cSXIDmNx0sErYpFdk0N-JUJf1GVoJmF2eSdxA6NBm9jkRuyEKiZNe0NUiN-tRt5Dz3WRUfodIC_9xRosu0n6PSJdCn3K94kAT-3QII_5lJ39zOGVFqafkCCffb_xSHkb4mrWfdm99P1weMGVDCFFj-9dOljCJOj-aMFffAISi5Wu88-_WScIFTj7nxTactZoOBu-ykXBHil4xJ1HMQQJrmQ-TClRMyBUn9FnSKa3RS6kdrtJEJu67Dp0HOMM_9BwrWzQaxu6BsKtU4IUuHaj6HatWhFsxf8LiBQ_X19ms2qpsFin7HZNQnKltj0Udfxw-27gck9-t2maI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GiH2Zf_pceCElaUVYgi2Mqu3eOBXW3FU0ZeO2iUyn7KlLLXqk62AjnSHLRg28bKc3RerDc2kzeAw8SmonBsbnURJ3unAsMENXs8ASeAl8UxtqZ1IpxmzX0d2jvV1Jk-ydCkIjmXOZ9gWCnB-54JEAKtmHA-dstRgDJkf79a2zYk4niSonrC6QeuS8miff63UUJk4-AHQtGiOpl0dGErNBvHs5Z1xEGqQpnY7LcSYPhinKjIJmFgyMQ3wGgjHwy9VBst64XPwoYj30_tUiJUZ5M6zKG_bcJ72hbmjmDzVNkt6Hs3c42oKVFX_bVeCnAitsCiR4YCGVEcQMWr-dMl38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mlf7oRF28InssgC82NVIj2YE7tLzhqW1y-f0HkhJbhrnA0MWzfINGTBnICigvgYh5g2fNY2Wdb-fsoiIxVTjJVIqonGSwdkOeKalmOusO-5ZEBfPh-a9DRqUxes1kz_jNecPzVQrwg3Z2fEPNxay_xdk7xz5XVdtt_NE3kuVdfvJPtThvhoS3veLmMUaLCW_D0hLjx7vq3TDTAQlb4I20Sey54U35U9bdTskfNjq-Y9lwXI_BdypmzcUSVpamGj79YSAeGma0evcfKZdlt468pS5lfhi4lXVuH6xj9PQbZpUQH0B5Yc1HdvtNDFrA1Gwv_QoXOz-RatucQT7LwDkkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W58iNW55iknMAAOKnktdUg-51TEBTtyT54g2IATWIUmxGfOuO0iwblRzLj5zWq4FaRFtY-a0KE1vGYp4GpX37nyQnKbk-hLsGNC2MDMF-0PRFrSfcKi24mb6ZSXhMm55aK_gFD54lVk9MTkZtkvDLamdl6R1qAqVh0jTYug_i_jtxjbVMjTBYcpd_uBVgyHDPKyJxt4mCekfGNDvvekJNK5eEMeH3AzjTBlWMUEcnJT3KhtJ3q98lQbYZDytr5IsTV_caVEFD6fw1n-RXWlHHUWQHrtCs_JGiKpysOGvKl2oayBJw7DOeLwsBFdt_Ry-Te62vBrL4TCOgosw8vfPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBokW6nrD-vo_nwg0A0zSkOEcc_oHwNMp1epeulV2ttCRA2gGY3rzmH0JnyAqn-SFE8sJxvxP-AUjNI3MVFjuVQaLCZQGKoVEir2ux3EPoTLLZ9CTIn_MgmVInGRGw1Dj7JtL9sM__1RJnqTf5B4P1hWS33PfutW_JBHtjKmFyKOekP28DukPZIiMtoHpij7v89bkQWki5JYYqNoVL7TjOoJoEiRMPzmdOZcALol9aqE1kte1PQ7vJBY3Mb8Kh1OYOjCdHfPvSLL7d4_NK2hP2UekH2lDuv_pr7QP2Ivrs14_B8Daz1EACjkRm2FSEJW9Pmc9MeFbA2GPWkZQ8Boig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuH1dr9vEEuYyXra3F57UtxqmwVIZD73R6DL7cyy8wQpg0DCCNgt4jtJLMr3MGfUTb8_BoMCFjl-gLE__TFL_14u5tR0_Tra8RFHlAlCmpVNOzOgPQzXE3pfiGP28XbfiM4tfL6cFd5qvIhtkkZe14zRjRLTWnoTx61K3UrdMzg3SKpioo0clgltYjOGRbbmAndiNV49Y63US0PoDHITO4xUGrkoSzg3l1juh-m6VCLRHZnMSeEB_Q9HxYcJ-WD903arz40RqDlUfdToShkz1arsqW9EXl6UDen__G6C1rwgwTCU7gHyT40EaSe5igWW8duB2TlnFRC6BCjQ4m6-mQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WKTWN4yLsDlt7z8E_6Ou2TOYtYjPMr6CaPXPcJ9Ffsmt6lHRZmJNmkFer3KuUeto7dwMatihM5rnoWEvm9jnA3plceWvUjOkZXCaW0Ij-qrNQfS6vKa_X0d9QdBhgyXs5EDAI6-oXZBWBm5h4crhVnbioD5_dNTnmXDeyvAW-wWE89ocepMo2m2ldTQO6IXAnWDsefVrRGb1rsKrxQ-bw_GhI6VfIhpduBlBM0vxuAmMJOr7BLYWifvaA25tDxQRe-ba9rRm-CwhDikLZNQ1PXs7fv7v3_w0sCocee43tRghdEQ9ZjpD0_3PCimIGZKVV1PHMElLercgGBsixNM6nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0WKTWN4yLsDlt7z8E_6Ou2TOYtYjPMr6CaPXPcJ9Ffsmt6lHRZmJNmkFer3KuUeto7dwMatihM5rnoWEvm9jnA3plceWvUjOkZXCaW0Ij-qrNQfS6vKa_X0d9QdBhgyXs5EDAI6-oXZBWBm5h4crhVnbioD5_dNTnmXDeyvAW-wWE89ocepMo2m2ldTQO6IXAnWDsefVrRGb1rsKrxQ-bw_GhI6VfIhpduBlBM0vxuAmMJOr7BLYWifvaA25tDxQRe-ba9rRm-CwhDikLZNQ1PXs7fv7v3_w0sCocee43tRghdEQ9ZjpD0_3PCimIGZKVV1PHMElLercgGBsixNM6nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4LiY5dqvM5RNqgXyGdEiJvoVrm_H-u1QpZQmNPrALvlLGDsPkgFQcRXUfvvhgbUc8jfhCAyJ4h0jqqcDUMtmzP53k87CQNc8QLZ6FL6xsQ7vIJ-ozgk-vA4-wfvOgTqGKXiqvq32Yl2vlf9-32zSAzamOzdpNqGeQICPx5NlLfIjjX-xDT4dTPvpO20d51F22g9aVjRNFUDjzm2l9jcuVFQJ5oLCITh605_aQ9bfKSqyKLLycBUeHtkv_U5sUMCi2LV7LhKw6jE8DUlHQI7__SQ5ww8rVRK015WWmw6nCyuAcI-NxA8riix3fEzCBNoRG03Mq0-XTGJjQLQ9BMRuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrpMc2C3AJTIBFI_Zma56mdDXNTBRT1qslycHxn-8l2tYBYdhmWP3hF-ue4PecmwGQ_Fl1PwIKvcJQ6RjYvNgwC2_tl_tgQlFp8gs61QMzlT9q8_D6NLpVAUPG4jh8a8Tz8kviWlPzw3rI6ZkvPc94_nz6uz7guSdsPvZb0rLDs896fekxF8gkzdvq6Kq51JlZqDAsIQIh5LDmYBixq5abGDVy9wuwdEwWQPBI-vXag58gICsErEPcgBs-bpkexueCZvltgN4t5g7LmH8FhNFAJ3GHvB5SEAxbYCUnnVGHbqdRK3zTFvMgjKu0Mlw5mUrCQ7qHCzCXVCy9lsoySpXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inwyEZMT7r8bhGyv1ah-WyZgDr3a7fCs2dvXVySD3w2oCPIrjpQ2Eejbk1C9iJJgYLJcf6V6DnCNvXHLNef3cLNaEIEXUdWcXLGSFAPkbnW79SBlqOyG3iOVrQBJyyqU1R5sXljC36lrqMOf86eWNxrBLrlKATdZM4fWjJP7KAZmbgUWk9-Oq5EiQSkVfxw__zj7ChB0Lfr9Y7AXIjL0FX85XDchtxarNJnLeAEtGX6h3DFbBBVToArJb8nrxwtnVlzbSxRKO6Fwx2xJjk3LackTORGpXagC_HpGqHx_APDfM7rtqe2_Z7qYRH4cT-Cw9CnvMjbNSOS0BiNP2v6cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1_Ld36dWaEDi064_IAsaDcBmge-j0pVMfIBRFlM1DqGN85FtIdbL2tk8cN_GZfbzj9iylj90vurZGHUVdJAMLcuuBk5bW3TqQLbPOhhq-lItAKEB71kBS5D2PVMfEINUO62NE05i24J1nFIDnzK1vLAviUE5bHqNX3o5GeoaHEJuoZROenIo8PfrsHyrync4KnV9KqEa0oSuo3309ANjt51Pz9kijFAEStWFeis3tVDyGNA2fWCO6peBEXmER3cCiKYZyZm0gxhfuYjYFHc-Ql5bqr7xU7Pl_QxCUxXnjn7JdpETHTVm0tjNryuA-bjXhAQUziKweP_8oLIIbSmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERuT4Ojz0LTkeKsdkgFPHwtm9b9BGP7Mzot362ZGmbbAqguMhB4zxRT1sMstT7MllJm7KYQsPYFjZSWAq6zIlAWiq0jGWAfMjaRKbVkZCkn2N3tLc-j7NOhRIUmW5Dh9d5bW5M4SeDx6KS9BpalezIU5ImI2_jeUV5c1-x9hyESIZBPLMI_tvfN3RSXZGlfxmXqHaDyfSgs3AUpT9y5WcHki8BjNIe7dtkyM6W2_PlZDj8ivQ_5uNSKfHjbi5TWiZAz1Vj6_XfnIAcMui8BNtowpE7iTNCaI818uRk717eZkp_ZAvBuVQNaIvdCyOlpSZ6e1ZhA6vLB5xJUxPVWjBg.jpg" alt="photo" loading="lazy"/></div>
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
