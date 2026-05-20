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
<img src="https://cdn4.telesco.pe/file/aziROfLZfeX-RoXJqRolqZOoYeYQVUHx5pY0S8g7epBjBJ5WOZC-sFdm435qJvVzjihMOjy3RPWgQ4OBLxvu_PWoM2JM3xb_BIDV0H2XSJXjnlsiFLIc7rMWNd8NUPbO0JoOU1IJXIbirslyyPlehFy5ktCD0hpDbvtTlxHD9k6bWOnSPhfDhDEWbfDGe6Qd7x6_4LtGgGIKIFT19PgCCiVV76gehBs1bKC45ts8FWtxDJdtuLaVtnYmCvhjPiJTu9hw7aPzJusFR1UgDb1rNbiLKm8dBy5S49IsiHWYGoiboexMsnmmuS05UKevH3eAqbGuYUfcCmNB3hr0swiPIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-131962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 162 · <a href="https://t.me/SorkhTimes/131962" target="_blank">📅 22:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
سرخپوشان نمی‌خواهند خسارت بدهند
✅
پرسپولیس به‌دنبال تنظیم دفاعیه برای شکایت اوریه
✅
فرهیختگان: سرژ اوریه یکی از خریدهای عجیب باشگاه پرسپولیس در بازار نقل و انتقالات تابستانی بود. در واقع همان مقطعی که رضا درویش بابت خرید اوریه در رسانه‌ها از بهترین خرید…</div>
<div class="tg-footer">👁️ 222 · <a href="https://t.me/SorkhTimes/131961" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 220 · <a href="https://t.me/SorkhTimes/131960" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 250 · <a href="https://t.me/SorkhTimes/131959" target="_blank">📅 22:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تأیید محکومیت 15 میلیاردی شمس آذر در ماجرای فخریان
🔴
کمیته استیناف فدراسیون فوتبال رأی محکومیت باشگاه شمس آذر قزوین در پرونده انتقال مجتبی فخریان به پرسپولیس را تأیید کرد و به این ترتیب باشگاه قزوینی باید این مبلغ را به پرسپولیس بازگرداند.
🔴
باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 262 · <a href="https://t.me/SorkhTimes/131958" target="_blank">📅 22:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🚨
🚨
#فوری | ترامپ:
🔻
همه چیز تمام شد. تنها سوال این است که آیا ما می رویم و آن را تمام می کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه اتفاقی می افتد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 346 · <a href="https://t.me/SorkhTimes/131957" target="_blank">📅 22:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔴
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 389 · <a href="https://t.me/SorkhTimes/131956" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
باشگاه پرسپولیس با مهدی لیموچی، بازیکن سپاهان وارد مذاکره شده و این بازیکن به همین علت درخواست جدایی از تیم سپاهان را ارائه کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 377 · <a href="https://t.me/SorkhTimes/131954" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00eb689252.mp4?token=qo5ZKGudK-gWtxxJr9abgcZJCjf-w7EP5VgWj1lv6hQR7N9jvGv3WuQXGzu8nZ62e8dcSBrpnjWL4kFbohu0YUb2maxfCKbLMXXF8cl6OWYqOto3_C8dHsCWb6-WnlxVCIYZkTkYFMADKdf_EYEHQOAVvzT-tDkvCjVL55zOgCb0yBF8FsiKOANgPmMrOZT9Us6h9zZzLa6u1JYHLYTQ_tM2GWjxsDxx-A7-iv2DqKWBAS_c0vtUqf6giwMyT1U7kU4gXPiy22PvZyhOGX87NOgSHgkpid5U1OIJf5qwgopMtyCavnZlSuKPKImyTpU4qcvsqoOPsrI9193NiHGTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00eb689252.mp4?token=qo5ZKGudK-gWtxxJr9abgcZJCjf-w7EP5VgWj1lv6hQR7N9jvGv3WuQXGzu8nZ62e8dcSBrpnjWL4kFbohu0YUb2maxfCKbLMXXF8cl6OWYqOto3_C8dHsCWb6-WnlxVCIYZkTkYFMADKdf_EYEHQOAVvzT-tDkvCjVL55zOgCb0yBF8FsiKOANgPmMrOZT9Us6h9zZzLa6u1JYHLYTQ_tM2GWjxsDxx-A7-iv2DqKWBAS_c0vtUqf6giwMyT1U7kU4gXPiy22PvZyhOGX87NOgSHgkpid5U1OIJf5qwgopMtyCavnZlSuKPKImyTpU4qcvsqoOPsrI9193NiHGTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قلعه‌نویی به نورافکن: آقای امیدخان نمیفهمی پای راسته؟ حتی اینم نمیفهمی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 372 · <a href="https://t.me/SorkhTimes/131953" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1098692638.mp4?token=UDgiXzQ2QyW4IUXyH3YIkCu1a2pN5NPNNTsmOitfEor7o53cNZxOkfk2oYYPJqLBxbz87UwlBRGYGOmceJStrDN8J0BResFgmiMAgviUyU0zNtdifbvLC138sNd7Qv0UQ4-wCRT0mJttwo88yK1DkCCkBc6lkddcA57SwpUeh5hMLo-6Umd1duv_Rjx1emRCePr2AeK8KequHrR9kr8GNEYkSOKSGLg4PLJoDPxfe5o8TQzzhFRvKe6MUQMbacAhRL6afzWwENpy-TwYXecHG8l--8oNsuEn1YD1SA61f265rHAaEy6Cbd-YTL4PNs2qQ6eyQsJO-xFae6qUEln19w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1098692638.mp4?token=UDgiXzQ2QyW4IUXyH3YIkCu1a2pN5NPNNTsmOitfEor7o53cNZxOkfk2oYYPJqLBxbz87UwlBRGYGOmceJStrDN8J0BResFgmiMAgviUyU0zNtdifbvLC138sNd7Qv0UQ4-wCRT0mJttwo88yK1DkCCkBc6lkddcA57SwpUeh5hMLo-6Umd1duv_Rjx1emRCePr2AeK8KequHrR9kr8GNEYkSOKSGLg4PLJoDPxfe5o8TQzzhFRvKe6MUQMbacAhRL6afzWwENpy-TwYXecHG8l--8oNsuEn1YD1SA61f265rHAaEy6Cbd-YTL4PNs2qQ6eyQsJO-xFae6qUEln19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ادعای آکسیوس:
🔻
قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 433 · <a href="https://t.me/SorkhTimes/131952" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 533 · <a href="https://t.me/SorkhTimes/131951" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsoiS7AlgWht_WA6KkjgzszLaF7sevmYK-JcleW679gULeis27t3wVkX7VC5ToU-hpSUppSz_sWgcM9E4VWSs8VBUZgn97kMHalK1uEd0B7-cR5zRvqr2uRs_ZizJsUEcqYLUPikoi7pt8z6WFPIQy-wI5hPYVRTJG_pG4CezUdw9m0bCkA5P1wL1ErcV6b42SNfnekSt_R_LNKIlkCCqsG2oJVIYyzYmBik2C-CagfobtG03HJuWX4paToN6uBLP1i7_vPRL3komv72DLEwkGhZagiXOdYvtThzdK2qd6UOfHnVIZieJABFUF5mk-ma3mlFT2epJ_gBgPutOWKHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
Final Europa League
⚫️
Freiburg -
🔵
AstonVilla
‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
براحتی میتونید برای بازی فینال لیگ اروپا وارد سایت بشید و این دیدار رو پیش‌بینی کنید، واریز و برداشت هم بصورت آنی می‌باشد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 535 · <a href="https://t.me/SorkhTimes/131950" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
5 گیگ 800T
10 گیگ 1.5T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 559 · <a href="https://t.me/SorkhTimes/131949" target="_blank">📅 21:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=AV-7kb7qpMla0MOe9Ope8BSyNhq3Gkf-gbza7Ed8EZkQyJsqDpdFsP9Xdh6JxLMugYfeS7-36e-vc3jmLu6JFFw7ZELRqcYn8Kf_OYSH8wQNLn_BCgo4tVV-8jEFZm8VpeveELtcZnj8jii0DZmIhqgCRAt2yJU_bCWlva3fdS0B5MiOLoCPCW43OPB0i-IHh5V3qYjF2ufUenUmUcS2qnoNX-n1pXekl3prkYoTIw9rbUIFB4NGC8n4ns8vMc9PPDQH48kEe4UO-8_P5U_OywritlgdYpbFVP6e17HfFZl3bnN0Z6oTDUbMAwTWbG2JeqPlxzW-2_lNcrzXwRrkKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=AV-7kb7qpMla0MOe9Ope8BSyNhq3Gkf-gbza7Ed8EZkQyJsqDpdFsP9Xdh6JxLMugYfeS7-36e-vc3jmLu6JFFw7ZELRqcYn8Kf_OYSH8wQNLn_BCgo4tVV-8jEFZm8VpeveELtcZnj8jii0DZmIhqgCRAt2yJU_bCWlva3fdS0B5MiOLoCPCW43OPB0i-IHh5V3qYjF2ufUenUmUcS2qnoNX-n1pXekl3prkYoTIw9rbUIFB4NGC8n4ns8vMc9PPDQH48kEe4UO-8_P5U_OywritlgdYpbFVP6e17HfFZl3bnN0Z6oTDUbMAwTWbG2JeqPlxzW-2_lNcrzXwRrkKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 653 · <a href="https://t.me/SorkhTimes/131946" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1XmYDNyE4-Zxymst8hiMoDv5FYPmarL08drxkXsd50I8No5h0Gsiux8d5LtMvd8e9xfjsEKY8s9_sBqSuiAU2nG-1wsk1OY2fUW2Pjftj-PsWnoWQjYaZO4-3jq-HN38-3nupNk0qtOCpIR7vY-8sg1Vg9k6DuNUdigKn8uxPuajuldahf1j6BZkpmKI7N7azz9ykVTEJL2qF8LPvTKLew9bwiTl4JcdHQLOrJcxWzpJX7b0yVTqAqWXFJvr2LrAbgg7pHsnB0ITCEOwHcIXYC6CtfvB4-92kXEzW4DqMPqVviL2cqkdkf6SxDEei1bI3LmKBlirISusFfN6cJHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووووری
شبکه الحدث :
احتمالا طی ساعات آینده، متن توافق ایران و آمریکا نهایی میشه؛ دور بعدی مذاکرات هم باز تو پاکستانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/SorkhTimes/131945" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
۲عدد سرور ۱۰ گیگ اف خورده ۱۹۰۰
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/SorkhTimes/131944" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84765e9843.mp4?token=hzz2cXTIMssQsjElGZqeIBPOdJKSwbjjEd6tNA9uXbGNcxNnK7vkET6x1Z_tKfRSXcFe1dXRTq6o6H7Qs_bBuU7o4CCUV21jX7cvD0PYawg1Pug9QXHsLojVzbYngHW0qRG95D_H3uFHv9pKaMo3nXyhnuu1f9QqAqhQ_5EgJUobipjp1z1VxizF9IOH1UAwzEx3X1T2tIoHUumfnqfRp102VhrxZLNoEyAtbZFlRKedM70hrf2N6coGR8vwU-y9ClM6_-sYZdK7GZSTsNWdTfnfd6Yvt7yc07JprVCKZRi5-RNXJdr_Mek5LkYLhv2GtyNFkvDZmB3j0F-t6Y4OWDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84765e9843.mp4?token=hzz2cXTIMssQsjElGZqeIBPOdJKSwbjjEd6tNA9uXbGNcxNnK7vkET6x1Z_tKfRSXcFe1dXRTq6o6H7Qs_bBuU7o4CCUV21jX7cvD0PYawg1Pug9QXHsLojVzbYngHW0qRG95D_H3uFHv9pKaMo3nXyhnuu1f9QqAqhQ_5EgJUobipjp1z1VxizF9IOH1UAwzEx3X1T2tIoHUumfnqfRp102VhrxZLNoEyAtbZFlRKedM70hrf2N6coGR8vwU-y9ClM6_-sYZdK7GZSTsNWdTfnfd6Yvt7yc07JprVCKZRi5-RNXJdr_Mek5LkYLhv2GtyNFkvDZmB3j0F-t6Y4OWDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سردار دورسون‌ مهاجم سابق پرسپولیس مهمان امروز تمرین تیم ملی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 787 · <a href="https://t.me/SorkhTimes/131943" target="_blank">📅 19:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
#تکمیلی | ترامپ:
🔻
یا با ایران به توافق می‌رسیم یا کارهای سختی انجام خواهیم داد و امیدواریم این اتفاق نیفتد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 771 · <a href="https://t.me/SorkhTimes/131942" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/131941" target="_blank">📅 19:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/SorkhTimes/131940" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/SorkhTimes/131939" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
🇺🇸
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 729 · <a href="https://t.me/SorkhTimes/131936" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ درباره ایران: من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/SorkhTimes/131935" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWMqAVgHhBPUpM7vuFZjW8pTt6zGs_bD-vN80VNURtfWGchz-wwZpLJPInAenIXTcoxCErTKz9tOmBMz0Yymc-5SPA42wWqsSFKpctt1E6AvwPW-4_Zgd6p_czb7y827wTqdLWRouIP2kq0HEQYZlGmVZ9S8_xU5t3ukvvxhD0eDYV5PQZQ1pJN0GsVZksETWZ3yvmZqBGG6ste0932uG-9ozcwp3dNnfEO3VEmexE0s3g0MTdW2bq0sRvBhjh9sn4kkpJklAKg7fP9KngoEIn2TesGNhNn61ubrs1NscBeNlVJgyXHkJGdQEBWM5HzRzKgB_GrwMSwXQorRuqThgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
شکایت یک شرکت تبلیغاتی از باشگاه پرسپولیس در دادگاه تجدید نظر رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 726 · <a href="https://t.me/SorkhTimes/131934" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJq23mlGVFw57Mn_qNkQe-Lg_h_797oNcbJ07j_JSI1GJSMGwd0kvRgAbtsJ-XplqgY083bzOCkaN7AO2HZE0NWAe6S5eNVei7MRGj3gKznMCOkLo0iBOq2nC6tixC6e4mwan5QKF3ZzjSvhg3fXQwiXLaCECK7hqLKtWZs6wKkdmpoGBxTPtt1clbrjYC15uX65AFFG3KyNs7bJ-5nG55hSd-WPZ-5nW8pJVqzLzgzr6bcsyb-UxjkCuVjmVNggWQsC76LRSyjM1G_XxdjGF3QViQ9Fk-6sISqWQWhSsLn9EaEK41WImCEOeefwZ5ETlJcDqZcCkU5mxuXzvMu4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
بازیکنان مطرح تیم ملی سعی میکنند سردار آزمون تو لحظات آخری برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/SorkhTimes/131933" target="_blank">📅 18:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=IkiTGVXRm2w_3LB5lt9slgzPUaAMQcD10zhL0S6L7alS6q8wU0ZkBUNkMxJ2DjH3EBC9w3PSv5bnCk2bflaxWkYrCkHDPouZe-dJdbjpdJKH8qRE-_B4gXmqlY_14wIjtCkX9KOO4rDy7yeWofwDRtgoKIMcZDB7uy94tyj1GIaFdhkYuuGgmrJqCEkpb-MZc9h-sRbxI0x9r3iHBedOqVDJTTglrpW4rUj-qpwBKJslrkeyne63zFpD0IuRCcVkk8gTHbZw9NXgHz934MRi1KSIZXD4c211KGRS2XLVIvAbAyhvTIOyipW9k7L6y3HUM1HauEEUIC5YsNT8mbswnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=IkiTGVXRm2w_3LB5lt9slgzPUaAMQcD10zhL0S6L7alS6q8wU0ZkBUNkMxJ2DjH3EBC9w3PSv5bnCk2bflaxWkYrCkHDPouZe-dJdbjpdJKH8qRE-_B4gXmqlY_14wIjtCkX9KOO4rDy7yeWofwDRtgoKIMcZDB7uy94tyj1GIaFdhkYuuGgmrJqCEkpb-MZc9h-sRbxI0x9r3iHBedOqVDJTTglrpW4rUj-qpwBKJslrkeyne63zFpD0IuRCcVkk8gTHbZw9NXgHz934MRi1KSIZXD4c211KGRS2XLVIvAbAyhvTIOyipW9k7L6y3HUM1HauEEUIC5YsNT8mbswnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ورود کادرفنی تیم ملی به کمپ تمرینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/SorkhTimes/131932" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=Fs79TCo52H6hcQdM9HJqCvHPzOElZd4FP_oXVd804avQMkqTaZjAhPtfqOOeczjGy3LWgu6eBF3DGD3XSYMjmrJhhJWgcPbr2AbOX-pjrM6xsu_yCOJdylMtYvYI8rp4kBcMTnp6lYb-OanR729MlQHnUQ8OHWz2s8cYemvj5_OtHnF6ubgycv2Egqj6sW2ilLk_S4emVWirnGhqEs04t8pvJr1rDPljE5ZDvkq20uAZ22JPqJd5nejs6QlvxSU_Rfq8ArQ0LGcnlstHMFl6hJPcWB9MRAqHbaMMDqXX-Ss2KHpeW-CWvB-xHLG_tRH8maKJJR9ZAfFfb_OSpAdmrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=Fs79TCo52H6hcQdM9HJqCvHPzOElZd4FP_oXVd804avQMkqTaZjAhPtfqOOeczjGy3LWgu6eBF3DGD3XSYMjmrJhhJWgcPbr2AbOX-pjrM6xsu_yCOJdylMtYvYI8rp4kBcMTnp6lYb-OanR729MlQHnUQ8OHWz2s8cYemvj5_OtHnF6ubgycv2Egqj6sW2ilLk_S4emVWirnGhqEs04t8pvJr1rDPljE5ZDvkq20uAZ22JPqJd5nejs6QlvxSU_Rfq8ArQ0LGcnlstHMFl6hJPcWB9MRAqHbaMMDqXX-Ss2KHpeW-CWvB-xHLG_tRH8maKJJR9ZAfFfb_OSpAdmrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زمین تمرینی شماره یک تایتانیک، محل تمرین امروز تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SorkhTimes/131931" target="_blank">📅 18:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
پاکستان متن توافقات اولیه را آماده کرده است و مذاکرات بعد از عید قربان در اسلام آباد انجام خواهد شد و تا ساعات آینده و نهایت تا فردا عاصم مونیر پایان جنگ را اعلام خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 726 · <a href="https://t.me/SorkhTimes/131930" target="_blank">📅 18:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/SorkhTimes/131928" target="_blank">📅 18:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131926">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=BUox-Ia1Jr_zIM2Rr_HwSHbcFf45pl7B9fp8upn1ZFZsnQjCfJ4UpiwgALo7WtUghOBnieE5xoP-qn2inIMPnceX6-a9peDf3rx5Nu972wsX8g81jQXAUHd6QO_3K_HeOCQ92BCLNF1FgxcjWHVqw_i6CPCKmkrYLXtEh3X8_Opc7ysGYFsHltDz_sWOucc0XwN-zTo0ZuzefRW8iisDb-5ZTGunxL9TuqCNjb7snj_QEy9yyDRnCrwaXt1SW-Ra0ialDRe_73X8fTdUCJ5oTlI-2AvVjccLl9yLQ9yLtRBuKBv5lEOzqs2v3b9_7SzdgeaX374Rt1vDn1FNoV16Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=BUox-Ia1Jr_zIM2Rr_HwSHbcFf45pl7B9fp8upn1ZFZsnQjCfJ4UpiwgALo7WtUghOBnieE5xoP-qn2inIMPnceX6-a9peDf3rx5Nu972wsX8g81jQXAUHd6QO_3K_HeOCQ92BCLNF1FgxcjWHVqw_i6CPCKmkrYLXtEh3X8_Opc7ysGYFsHltDz_sWOucc0XwN-zTo0ZuzefRW8iisDb-5ZTGunxL9TuqCNjb7snj_QEy9yyDRnCrwaXt1SW-Ra0ialDRe_73X8fTdUCJ5oTlI-2AvVjccLl9yLQ9yLtRBuKBv5lEOzqs2v3b9_7SzdgeaX374Rt1vDn1FNoV16Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/SorkhTimes/131926" target="_blank">📅 18:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ درباره ایران:
من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/SorkhTimes/131925" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
پژمان جمشیدی به ۹۹ ضربه شلاق محکوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/SorkhTimes/131923" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBXm8jnraK6bOuhGddjyYWu5esb_CxjbSLjrl9ahl4Yz4W_C84Fpwq5a5VYwn_4K3X0xFu0IGP1xowUg9ygGQymzYpz7fYSjLOLR1uc6YVEC0YCZRoUupSC_42uVNqZrMsxRba4uC4fxzV-eqrqyhsDUSpRZ0b7ct-zkbqgD79TggkdD0yDriNFMAS_cfSZxajMzTNdkZz0cNwp1HiwKTlt0l5BRgpQegc43HcpvgXOZi_xu1K7KOJhZ-k2QUOUNarrV05CEHnikhNedMSpGv0jrWsCP9H0rnR8UN8_wQwD1wofFf6F3Awh9pnzYbdxtecddeYl9grOViPcjaMksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
احتمالا بخشی از اینترنت زیر ساخت ها در حال اتصال است!
❗️
بر اساس آماری که چارت های رادار کلادفلیر نمایش می دهند،
❗️
طی ساعات گذشته پهنای باند اینترنت کشور افزایش چشمگیری داشته و احتمالا این بدین معناست که اینترنت دیتا سنتر های ایرانی در حال اتصال است.
❗️
احتمالا تا ساعات آینده شاهد وصل شدن بخشی از فیلترشکن های قدیمی در داخل ایران خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131922" target="_blank">📅 16:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/SorkhTimes/131921" target="_blank">📅 15:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvpbT_TXDKNOhu2g_AV52_wcrrj4K3s4yaldGvxUl3nVQ9YMqzc4jnobjbhjo0JQIQ7-0-zTHJ4OduBgyXApFtRArqhINBDUINbWc1vw1sOKw4QMdsIUdOL2qp3-ELEP7CViH8pS7G0fytIIqHHVQ3mhMotarvTyu_uKH7RO-BAFTvYafPXswsgRRiN_OsU8pAzspM6s6MmWp_gK62F86KdI3OUBjqueLdTICXpK0LzHcuFixT6Q0CtXEx902hp07RLwgLK5Zko2kwJEXKVEHDb19ptGOD_zvjnc21OJugFBiHKSh_4jElECCf0s1Co4rFueAEI4zgMb_JDU4TL0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/SorkhTimes/131920" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
فووری؛ اوستن اورنوف ستاره ازبک پرسپولیس در تمرینات تیم ملی این کشور مصدوم شده و وضعیتش برای جام جهانی نامشخص است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/SorkhTimes/131919" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بعد از ۷ بار تلاش سنای آمریکا، با رای ۵۰ به ۴۷ قطعنامه
اختیارات جنگ در ایران
رو تصویب کردن
این اختیارات ترامپ رو محدود میکنه البته احتمالا خود ترامپ اونو
وتو
کنه. مهم‌ترین تاثیرش اینه که دموکرات ها کم کم دارن قدرت بیشتری پیدا میکنن و برای
انتخابات
بعدی دست بالاتر رو پیدا میکنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/SorkhTimes/131917" target="_blank">📅 15:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICqyx3iIfIdlhkRgjYYQ_5mLDZijHBNsu0SpIXLYrvOhAMSEclG3MqS3HsGwujla2aDudAk85PcHj1n3MpEDb6oAmw3fLaNKVERIVV-PWSFJ02du_RVZyEoqHzIKMOjo_MDFLQ5_GfxDoejRd2oyyOTKjPWuDPOJrygqv29GLjoLKX_WLqFud7UDyibdUVoSl0y9XB0xUPHT2rysQOEnGz0qlAWOLwWwt9ToDgilVQiUxIgcwpunPv1UPPaJPmWcQyOHg89bHmg3vh-tHxXVnmmJrEqDLUkyzHB5iUFRfBImXRQ-mPvIVsIokNdxdXbhL1tqsUKpGp08z1sGaOKSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش مدیر رسانه ای باشگاه
😂
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/131915" target="_blank">📅 12:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDLSTab9dg4xP3IvMIRtFbwUXaD2k1SYwIvAexD8pU58oQK69E1a-MsBcJkn7-g3X9mVt8RUoC6M9mwwW5qEDjQKjjq6lUMG1SzpNmyJpjqf2O4OLuCCSlKqMJ-t4FyXS187N-fy3CbSjReWfZWQ5YTP0hSwihH-JXcBWW-GvVULVWXtsRMEJw9_IFpEC8HCLFmD16qLuTTws1MZcdyNeYc5YYXdXPnQDj1brg4D7UZxaljQ2etWjMJePWKcKZ6-fHszsTjAYA_Wwa8j8Q5ou8z1p1l_MgguUySgimlw1jRGi_dwe6_K7Q_IyMppgvWia_C3cOD2oh9V0I4Xi9eQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از شرط‌بندی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/SorkhTimes/131914" target="_blank">📅 12:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 871 · <a href="https://t.me/SorkhTimes/131913" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:   پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/SorkhTimes/131912" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0T9VlJawS0_akaZOyWhBrLKRpZfV8w34WpSwEKch8OwGGcLNy9J5bBP_Bp8LwVRNsYlZAdmJUpXF5eoypZNI8HVpsWfiGJD1d2Ezj85YXHFqTN5ZJsIPrFJXr7jDyXBdEL_SLZayoSIQ-m4VIDF1DpzFNWACmxP4lNy2_QtEoCwxge2qFuaY5lgnbkXWocbEolmKMwx6qz5FYSCTp69elOX8FYPbUDEh-4jn-n0fbDTgpU1fCQR3NTvm4gwpjbbJTOPh4lNnCpJ6uVvDCqilMoG5w8W161FJgxrubnNO7DSZmu7YyCCOYN6fhvryAVbS5_kETN4DzQAaYJY76uQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/SorkhTimes/131911" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131910" target="_blank">📅 10:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
ونس معاون اول رئیس‌ جمهور در مصاحبه جديد خود اعلام کرد اصلا متوجه نمیشم مقامات رژیم ایران چه میگویند یا چه چیز میخواهند فهمیدن حرف هایشان واقعا سخت است و مدام حرف ها و خواسته هایشان تغییر میکند و نميتوانند به یك تصمیم واحد برسند ، اون 440 کیلو اورانیوم باید…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131909" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
قاتل الهه حسین زاده با اذان صبح فردا اعدام می‌شود.
❗️
استوری خواهر الهه: امشب، قصاص مرهم داغ خواهرم نمی شود... اما شاید کمی از بی عدالتی این دنیا کم کند. الهه جانم...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131908" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">●
بدترین حس وقتیه که میخوای سریع وارد سایت شی، بازی شروع شده، ولی VPN وصل نمیشه یا سایت نصفه لود میشه.
😑
● برای همین
ربات تلگرام وینکوبت
این روزا خیلی کاربردیه چون کل فضای سایتو داخل خود تلگرام میاره و عملاً بدون دردسر میتونی مستقیم وارد بازی‌ها و کازینو شی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131906" target="_blank">📅 00:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
#فارس مدعی شد ؛ مدیرای پرسپولیس اصراری به موندن علیپور ندارن و اگر اوسمار هم بگه نمیخوام قرارداد علیپور تمدید نمیشه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131904" target="_blank">📅 23:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚪️
مهدی تاج: اگر پرچمی به جز پرچم جمهوری اسلامی وارد استادیوم شود به آمریکا نخواهیم رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131903" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
⭕️
🔴
حضور حسین کنعانی زادگان و رضا درویش در منزل خانواده زنده یاد الهه حسین‌نژاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131902" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚖
پژمان جمشیدی تو جلسه دادگاهی امروزش: «من قسم میخورم که هیچکاری نکردم و این اتهام درست نیست. من با این دختر کاری نکردم و اصلا بهش دست هم نزدم. به روح مادرم قسم میخورم که من کاری باهاش نکردم.»
◽️
وکیلش هم گفت ادله و مستنداتی به دادگاه ارائه دادیم که بی‌گناهی…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131901" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131900" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131899" target="_blank">📅 22:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=bDZbKdLQAfXX8pk8eXloC6LuP5DGXhaqf8SuR1p6YC3I_HJB8_q2fyJVH1FHTvLoPDjmZ9U_hvpKIyai9vYsA0pens0_RXNjokEX2j4QvlgVNM_yWa_6sTxinxwZykCkEvpHItqEOF20IRDC9xYqlQ9DNWAHd7DdYzK2MLZnag5pDANpnws1aTvo_Cc5o_rKfzMoTI5Vcp7bM1X_I8mAkFPberO3DpMCa6fiy70mFLPYtXZU0JhQn3QJXwdqNHHNc6pwTfsib2kdmbHprJ-tZcs7Z9nWn2jks-BxNX0nWBOOXbQEa8aMhGSUUm4xepH1qo9831s9c1x6N5awrcprGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=bDZbKdLQAfXX8pk8eXloC6LuP5DGXhaqf8SuR1p6YC3I_HJB8_q2fyJVH1FHTvLoPDjmZ9U_hvpKIyai9vYsA0pens0_RXNjokEX2j4QvlgVNM_yWa_6sTxinxwZykCkEvpHItqEOF20IRDC9xYqlQ9DNWAHd7DdYzK2MLZnag5pDANpnws1aTvo_Cc5o_rKfzMoTI5Vcp7bM1X_I8mAkFPberO3DpMCa6fiy70mFLPYtXZU0JhQn3QJXwdqNHHNc6pwTfsib2kdmbHprJ-tZcs7Z9nWn2jks-BxNX0nWBOOXbQEa8aMhGSUUm4xepH1qo9831s9c1x6N5awrcprGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131898" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
باشگاه پرسپولیس: ما میگیم لیگ برگزار بشه ولی ما رو نادیده میگیرن، اونوقت تیم‌هایی که میگن لیگ کنسل بشه، معرفی میشن واسه آسیا. نمایندگان ایران تو آسیا باید با عدالت و در زمین فوتبال معلوم بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/SorkhTimes/131897" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
💢
بیرانوند از جام جهانی محروم نمی‌شود
💢
رسول باختر، حقوقدان ورزشی در گفت‌وگو با ایسنا: در رای استیناف آمده بود که محرومیت بیرانوند شامل مرحله نهایی مسابقات بین المللی در تیم ملی نیست.
💢
با توجه به این موضوع، حتی در صورت صدور رای CAS پیش از جام جهانی، بیرانوند…</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/SorkhTimes/131896" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/SorkhTimes/131895" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز…</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131894" target="_blank">📅 22:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131893" target="_blank">📅 21:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=T1hkrsjrqKuetON-CHD0StN4uy6dggn9Joe6S-Pi_2W_z9c4T5MjTok5UsHCHc5gT4kN72kX6xbw5EB9lL-3VVR3W6nzY8gl91MyXV3UW0zTL-Fq2R98j8pr6b8bTcM0QkJ2RlPgdIPdUYhdlS_x2GvDsWJboetITCCfJDAk-VHe4kC1z3Fqg0l8l55JJQp7IA7FnJJDd69u-G7PNO32ORDipktS_kh11zoLeTmxKiip88qvOtpIbXcY_wtfN5m9laR8FFAWatSJC7bC5isoC0iFiHWAKAvt5BNfUgj1TAkAGS63gRij7nX4Yq3bLwUAYReJvitfcZqY6MIR1cucEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=T1hkrsjrqKuetON-CHD0StN4uy6dggn9Joe6S-Pi_2W_z9c4T5MjTok5UsHCHc5gT4kN72kX6xbw5EB9lL-3VVR3W6nzY8gl91MyXV3UW0zTL-Fq2R98j8pr6b8bTcM0QkJ2RlPgdIPdUYhdlS_x2GvDsWJboetITCCfJDAk-VHe4kC1z3Fqg0l8l55JJQp7IA7FnJJDd69u-G7PNO32ORDipktS_kh11zoLeTmxKiip88qvOtpIbXcY_wtfN5m9laR8FFAWatSJC7bC5isoC0iFiHWAKAvt5BNfUgj1TAkAGS63gRij7nX4Yq3bLwUAYReJvitfcZqY6MIR1cucEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131892" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
اگر وحید هاشمیان و پرسپولیس توافق نکنند، تکلیف صدور کارت مربیگری اوسمار چه می شود؟ هوشنگ نصیرزاده پاسخ می دهد
‼️
‼️
نصیرزاده: برای فسخ قرارداد یا برکناری سرمربی هیچ محرومیتی تعیین نشده است و فقط باید غرامت پرداخت شود. اگر در قرارداد وحید هاشمیان مبلغی برای…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131891" target="_blank">📅 18:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مسعود پزشکیان خواستار جلوگیری از بی عدالتی در اعلام نمایندگان ایران برای فصل بعد رقابت‌های فوتبال آسیا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131890" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131889" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131887" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚡️
حکم جلب رشید مظاهری گلر سابق کیسه به خاطر بدهی ۴ میلیاردی صادر شد، میگن متواری شده!
⚡️
عجیبه با این قرارداد های میلیاردی که داشتن ۴ میلیارد بدهکار باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131886" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131885" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiXvvqe4ihyTpcFIZ4ly8zqvuDqppiaJMizJordxrB0AKWJGhDBtSmHDimWFnBiO_nHe_6QP05NfArPUbYq40FMIZ4ed_atYtoK8XTAjRObMSSGTuS4Oev_M5c8_SpXu80i-xeI8ysZMbp5unccf7BcFNF2dF1_uKaB-JStPNeY0RA_ZcYb1BxIXeYKZWUHDGxBDYr_pvztMh3XVBpf0iZJgkRNN9Rd4ZHuQ9H54CUrN-MTctgE2a2P-HbU0dPGV9w_EiCf5AroO_nX3ptEXTKqj-LbN7rHQg1qljsVAyI0JMawWNDtn1d987Jm0iGgx3R-k_d87802b3v0SeWR-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131884" target="_blank">📅 15:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131883" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131882" target="_blank">📅 12:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHMeQcNqgPHbJpHB-uPpgHQmd0vUQMRmuwLlppFALTNJ-xp8hcJu8TGfuY98-92NoJqPaduGXHItceS8oRUa5gDbeH5VvTNYbZSWSAms70enbk9lUk-Q6CnG2suybjke38-7rhPRGaofU7U2OQSlH2QFzzczu7cIEEgnWiabrjUsdDkUQGcEjyhhg1lp8ITIQqk24B1X8hWXCj9VXqiubyZs1xI2_79JGYkSCIe4h_qWpLuYQUpNzqR-DLhiEWuXEGeEYvgqhWaAuFaIdqh1FkxRqTOJNi-wPoVwtW5e99SwwmzfKs7VyBOblNJAswwJHAE1218DfsMg8Nd5JsAh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد داشت و از پرسپولیس به عنوان متحمل ترین گزینه وی یاد میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131881" target="_blank">📅 12:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
تغییر بزرگ در نقل‌وانتقالات؛ لیگ برتر ایرانی‌تر می‌شود
❗️
فوتبال باشگاهی ایران در آستانه فصل جدید رقابت‌های لیگ برتر با شرایطی متفاوت نسبت به سال‌های گذشته روبه‌رو شده و به نظر می‌رسد سیاست اکثر باشگاه‌ها در نقل‌وانتقالات تابستانی به سمت کاهش هزینه‌ها و استفاده بیشتر از بازیکنان داخلی تغییر کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131880" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131879" target="_blank">📅 11:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🛜
سرور نامحدود 1 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 4.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131878" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzemK5cU3ykc889bRwoGno4ag-IWe6JeYHjM9EbEq7ZVvYF-lVN3bbzbbJ3FjZUn8WExz7hpYClXr6bwkAU21jGH8WlFyrdqvBMNSue1XEmWQt0hfRQHtxMgTPI4z-fGTxObmVQ_cXvXeNqgT7eDpHUBgFblZeVi_9L3TS6HgBwx4iBXm3efJr_Lday30xB_ps851cAGVq0pfIG8kiyJABcdGim59PoOGSmCsgLro10ngINmr663gYTYkujM7UxaNj-WySBSBomt6P1Kmql1k6dhruzcUmriXmowWDh2NtDIDMqKt4Vd-oXBSo__FVg6iIDWA9N-pOCvN-Ym-oz1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع و مستقیم به
وینکوبت
📌
دیگه لازم نیست بین لینک‌های مختلف بگردی یا وقتت تلف بشه.
📌
فقط با یک ورود ساده به ربات رسمی، مستقیم وارد سایت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
ورود سریع و بدون معطلی
⚡️
بدون لینک‌های اضافی و گیج‌کننده
⚡️
دسترسی مستقیم از داخل تلگرام
😀
همه چیز برای راحتی کاربران داخل ربات فراهم و قرار داده شده.
🔵
برای تحلیل‌ها و اخبار سایت وارد کانال سایت شوید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/131877" target="_blank">📅 02:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=vDk2sQLpQtF7CbDt7hMkQzA4D4T5IOnGz7YrqsXKj1nFkQmF-0AZFlLOUZT693R2fm4NS9ahsPlKL9BFsplCkJZHjDPjoTJQZX-fA_8MpGBJfMYZ6ewT_UCnv0-OAAMR_II7bzJVrd013KctGfR_yAGQdimLSDJpxHQ3e2jPewQGqp4fTE7dowLtFcoIrvBtBKZCAIYFuTOmX4zePdPzbioHzQVbOkf2nMMGD_0D6MOtrLNwJdovqa8xfP1izOgYHf2ylXICilEItIzg0MZi7soEjnXyCpQWrn9Idv2N6fYVoPstv8OCetgswftWL7ximulxAoThsbxInJLMTYje_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=vDk2sQLpQtF7CbDt7hMkQzA4D4T5IOnGz7YrqsXKj1nFkQmF-0AZFlLOUZT693R2fm4NS9ahsPlKL9BFsplCkJZHjDPjoTJQZX-fA_8MpGBJfMYZ6ewT_UCnv0-OAAMR_II7bzJVrd013KctGfR_yAGQdimLSDJpxHQ3e2jPewQGqp4fTE7dowLtFcoIrvBtBKZCAIYFuTOmX4zePdPzbioHzQVbOkf2nMMGD_0D6MOtrLNwJdovqa8xfP1izOgYHf2ylXICilEItIzg0MZi7soEjnXyCpQWrn9Idv2N6fYVoPstv8OCetgswftWL7ximulxAoThsbxInJLMTYje_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131876" target="_blank">📅 01:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131875" target="_blank">📅 01:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131874" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=VVliayT6CS6182u_u18dEgt2b_uzBT0Fwfcw6Gmab18sDf-L-e_yBeMvjPLur5s-I1upKsG41oL_o74g0pW02T-IoFwp42cbS0HgKXsvzmNe6iCQ9d0t9gdlhy7FNfSolVHfeDOC3iGBP7xZzP7qglzdbd8XSzAeOdkyPfjZMRmOJeVTgi0a75FOQN3sfn-7mMvIuitZ5oAa2toijuEsnTDXXAsqnXof2rITW1cBEUrZTN3aYfz-qbJNlqNF5tEG3bsoGCkWcsQP0P-iINzfPliYpGf-oGAi3566-i-vr1yCTByGEnsbAQHeoPRZyaHc-zC2wjf9Grv9ifS0z04Mcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=VVliayT6CS6182u_u18dEgt2b_uzBT0Fwfcw6Gmab18sDf-L-e_yBeMvjPLur5s-I1upKsG41oL_o74g0pW02T-IoFwp42cbS0HgKXsvzmNe6iCQ9d0t9gdlhy7FNfSolVHfeDOC3iGBP7xZzP7qglzdbd8XSzAeOdkyPfjZMRmOJeVTgi0a75FOQN3sfn-7mMvIuitZ5oAa2toijuEsnTDXXAsqnXof2rITW1cBEUrZTN3aYfz-qbJNlqNF5tEG3bsoGCkWcsQP0P-iINzfPliYpGf-oGAi3566-i-vr1yCTByGEnsbAQHeoPRZyaHc-zC2wjf9Grv9ifS0z04Mcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131873" target="_blank">📅 01:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=OnWttOnkfteqSywGsax1e4rCbj694Ne8inCq1Gg8fdH6iXcR_Ef9irma-MPaCKYLa2YoQGcy5iGMPGjvqd_HYGXJYF8-WpHlR28Ih1fkajnmZhlxWqrz6qoBYfJRoWKQl7cVT10ZKEZMnrwQoxAWGOrptTt-io1CrSlnAzKKalvsaDCIJQ0oagUWAI76_6_vngplKQbAvfqy_nMT3L-7zF_ES8-RfMyEIOKeLpLcJB9orvLN9USoYVec4NR8UCbaHFptoDlL-aIyveDB6BSGHxDlX73wo1WXuNW1ugF1tRuoaGIdPtpMgoerPT_kTvXwKLgYKEBBhQrjU-oUUc6Cow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=OnWttOnkfteqSywGsax1e4rCbj694Ne8inCq1Gg8fdH6iXcR_Ef9irma-MPaCKYLa2YoQGcy5iGMPGjvqd_HYGXJYF8-WpHlR28Ih1fkajnmZhlxWqrz6qoBYfJRoWKQl7cVT10ZKEZMnrwQoxAWGOrptTt-io1CrSlnAzKKalvsaDCIJQ0oagUWAI76_6_vngplKQbAvfqy_nMT3L-7zF_ES8-RfMyEIOKeLpLcJB9orvLN9USoYVec4NR8UCbaHFptoDlL-aIyveDB6BSGHxDlX73wo1WXuNW1ugF1tRuoaGIdPtpMgoerPT_kTvXwKLgYKEBBhQrjU-oUUc6Cow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمله عجیب سخنگوی فدارسیون خطاب به تیم‌هایی که هفته اول خرداد تمرینات‌شان شروع می‌شود
◻️
علوی: شاید آنها خبری دارند که ما نداریم؛ ورزش کردن اتفاق خوبی است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131872" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131871">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=tSRDy_PX3Y3v7tRY4R1SOasV1SUp-SzfJoV0C09OgvnCb1fZHJNQ0aR1AWHgtCwJtqix-5nljcFLr4MwOZDMT9g2pxm4RAXNwdHSuvWgtNUjgM816bh7mD1eXrRmJqAJcn3LXeu5fCVRI8oQAtwWxEod_wvzlZnzgI_4iE3tDttLIb2I-pnG9RTMNCOxG-uyVsJHk64cQBDuDBDIomTz9PpMJx63eU6S0CxyXjueYbenfK8GFwhHrnI6JXl2wGKRPPuhK11uHZnjl9QjGV2M543DkP7kUqd-mQizAscOKiSGIz_zPOWrk0ddDrqO1L4OLYRdXldty30L5e-6k2i3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=tSRDy_PX3Y3v7tRY4R1SOasV1SUp-SzfJoV0C09OgvnCb1fZHJNQ0aR1AWHgtCwJtqix-5nljcFLr4MwOZDMT9g2pxm4RAXNwdHSuvWgtNUjgM816bh7mD1eXrRmJqAJcn3LXeu5fCVRI8oQAtwWxEod_wvzlZnzgI_4iE3tDttLIb2I-pnG9RTMNCOxG-uyVsJHk64cQBDuDBDIomTz9PpMJx63eU6S0CxyXjueYbenfK8GFwhHrnI6JXl2wGKRPPuhK11uHZnjl9QjGV2M543DkP7kUqd-mQizAscOKiSGIz_zPOWrk0ddDrqO1L4OLYRdXldty30L5e-6k2i3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131871" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=RvqaWZcTOuGjuL-UA8zMG4X2fbc3YxzEuVULoo-R16J4O5CJzrZCpCyUgj9gxXGjYSGkHw1-OWNIAFszqmQcLC08eMfpAuWE7j-60JvMsa4lPy48kCz2AVrayomsW1Yd-ttfCUGVPFE3dwNjVjFi4zpUa5JCC03NCyOHuDU2dO6OvndCEgDQA7igAGY9jBKsJHeqw-DbWQvZNoDYlePj4ZH8eU0A9fVySwLuRtFIc7rZmQsJdaxSQJhh9-pThpP0ZUaxyJW8Emm7RstB64mBdtDOLibVgCevjn-9zHp9M3pkzABWyZvrUtzDpljTz5eRZ24iiBMjWe_qHLyu01Sq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=RvqaWZcTOuGjuL-UA8zMG4X2fbc3YxzEuVULoo-R16J4O5CJzrZCpCyUgj9gxXGjYSGkHw1-OWNIAFszqmQcLC08eMfpAuWE7j-60JvMsa4lPy48kCz2AVrayomsW1Yd-ttfCUGVPFE3dwNjVjFi4zpUa5JCC03NCyOHuDU2dO6OvndCEgDQA7igAGY9jBKsJHeqw-DbWQvZNoDYlePj4ZH8eU0A9fVySwLuRtFIc7rZmQsJdaxSQJhh9-pThpP0ZUaxyJW8Emm7RstB64mBdtDOLibVgCevjn-9zHp9M3pkzABWyZvrUtzDpljTz5eRZ24iiBMjWe_qHLyu01Sq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
علوی، سخنگوی فدراسیون فوتبال: در حال پیگیری هستیم که باشگاه‌ها از تاریخ 9 اسفند به بعد درپی شرایط اضطراری به خارجی‌هایشان حقوق ندهند؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/SorkhTimes/131870" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SorkhTimes/131869" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131868">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سه ماه تعطیلی؛
🚨
🔴
وظیفه اصلی که هیئت مدیره پرسپولیس فراموش کرده
🔺
هیئت مدیره باشگاه پرسپولیس که طبق قانون موظف است به صورت هفتهگی جلسه برگزار کند (و عادت داشت این جلسات را دوشنبه‌ها برگزار کند)، اما بعد از آتش بس چرا نزدیک به سه ماه است حتی یک جلسه رسمی نداشته؟
🔺
در این مدت، اعضای محترم هیئت مدیره همگی در تهران حضور داشته‌اند. در بازی خیرخواهانه حاضر شدند، مصاحبه کردند، واکنش نشان دادند، ابراز نگرانی و همراهی کردند؛ اما وظیفه اصلی خود را زمین گذاشته‌اند.
🔺
مدیرعامل باشگاه بدون پشت گرمی مصوبات هیئت مدیره، عملاً دست و بال بسته است. هر حرکت اجرایی نیاز به تأیید و چارچوب دارد؛ وقتی جلسه‌ای تشکیل نشود، خبری از مصوبه نیست و مدیریت قادر به گره‌گشایی از کارهای روزمره و بلندمدت نخواهد بود. نتیجه؟ باشگاه لنگ می‌زند. قراردادها روی زمین می‌ماند، برنامه‌ریزی مالی بلاتکلیف است و تیم در آستانه فصل حساس، سردرگم اداره می‌شود.
🔺
هیئت مدیره نباید تنها به حضور نمادین در رویدادهای عمومی و مصاحبه‌های احساسی اکتفا کند.
فریاد هواداران را بشنوید: «هیئت مدیره، به وظیفه قانونی‌ات عمل کن، وگرنه باشگاه را بیشتر از این به زمین نزن.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131868" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131866">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔴
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌جمهور امارات متحده عربی، محمد بن زاید آل نهیان، از من خواستند که حمله نظامی برنامه‌ریزی‌شده‌مان علیه ایران را که برای فردا تعیین شده بود، به تعویق بیندازیم
‼️
…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131866" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131865" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=r_LBJkox5BHtbH6FTTE9Y7cqzLqJRshPrEE6sMWQCrgRCv5txzYxeihTF_A9YqINZXm4VzCcxXcoIM6Vu9JVQGtyKTnKj5fJpaSIJBMbCd_WFwwapKCAvpdor_Ch-xwAGk8Ac5PMcZMEqxNSr3FyhvqpCik9vp0_J92RsRGnY9uYOlcD5aaHjK8dIXNOzaNt4u9qrGeMqjlCZjNXGZh5oGgbSbdoFXfw9ZL7OUvarNJ4NnDURx4BKHkvqKKtqF-7QkLHX1Olk--cdTIMXsJCwjDoUY4RtcRuzVgbUWgPCpH6Fl1djZfZhoc5hHDv7ns27xBDX0WigBBQfdwekQslRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=r_LBJkox5BHtbH6FTTE9Y7cqzLqJRshPrEE6sMWQCrgRCv5txzYxeihTF_A9YqINZXm4VzCcxXcoIM6Vu9JVQGtyKTnKj5fJpaSIJBMbCd_WFwwapKCAvpdor_Ch-xwAGk8Ac5PMcZMEqxNSr3FyhvqpCik9vp0_J92RsRGnY9uYOlcD5aaHjK8dIXNOzaNt4u9qrGeMqjlCZjNXGZh5oGgbSbdoFXfw9ZL7OUvarNJ4NnDURx4BKHkvqKKtqF-7QkLHX1Olk--cdTIMXsJCwjDoUY4RtcRuzVgbUWgPCpH6Fl1djZfZhoc5hHDv7ns27xBDX0WigBBQfdwekQslRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131864" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
ترامپ: ایران می‌داند به زودی چه اتفاقی برایش خواهد افتاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131863" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-jYec8nKFa5Ytk0tURu9W70zlrLLlNGVjmrJ8METXQPN1sADmaDuKPFYv-n9IqBziEBm4S-Hj0I2KLRugvbm0LZoi_Ob4bqN-EcBK-9h-V_V8QOVngcqT-HjvO_Os8DRk_Xqck5LnpTwzOmHxhJZo2rXsAGgMcmA5O6NQnuOf9VXyF5Uh19JS8X9eFV9k3D_l8ZA1zVnkR2TaHpNxbO-HC0gWhz_5QSZlRuHLD3O56O1N__r-et3UgqcvE4ULhnRtVuT5oaflW7RU-YjnODvoAUQiW273VRw4DrqG5JKixPxJt5XKBo4T548BLoFd43AXlgJQSeAr9XRAB9qeXJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یورگن لوکادیا، مهاجم هلندی سابق پرسپولیس، به اردوی تیم ملی کوراسائو برای جام جهانی ۲۰۲۶ دعوت شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131858" target="_blank">📅 21:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/SorkhTimes/131857" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🚨
ممکن است مجوز حرفه ای چند باشگاه مطرح صادر نشود و از شرکت در رقابت های آسیایی حذف شوند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131856" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131855">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
باشگاه تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131855" target="_blank">📅 21:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc7umNyVASxABziZMuxcDWb5UL7e8CQdNvsJXNUjL6nzgvC3hSk-uzFUjRVCLHyN_gEnGFwvsa6J4UOdI7r7pB6NM1kWS3XSNVqkfxA9HwgylqOxBi6MpMqCGvA7FZEq78jMY9Sxm581_yVhhHBZMgNX9MgcS4HGLnRNU67tQjRARskKZ3O1SvVq10bq2KrVcv4HpQhE1xQe8zalwHuMgeMzCgJ9pB8JodIn8vIo9bNlJFvyuXpqBx2BqI-EHBKNGAjDgyG1h_5X8R1vNOFTxuN8W4ZGGIEv2-Se5Qulb3FYdWai60SUfkz2BsqrC-9m3JRGmfjCOXNWvkqwal9PKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🏅
⚽️
واکنش باشگاه پرسپولیس به شایعات در مورد معرفی نمایندگان ایران به AFC
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/SorkhTimes/131854" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
اوسمار گفته اگه دوباره جنگ نشه میام و تمرینات رو اغاز میکنیم ولی اگه جنگ بشه فسخ میکنم ولی خب غرامتی نمیگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131853" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131852" target="_blank">📅 19:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131851" target="_blank">📅 19:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
#فوری |   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131850" target="_blank">📅 19:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=dmq7vGOD9Z3nYvlWuFx3H9JG3Fs0K5o4a6-niSY0lO_FQmODMZo1bMym5PGiFqGFua4faLKIZkhFxL2lqHH8p90Rnv72LQu7cpvAuwNk9DwK0UyOswZov_h1BhZXVHO0fKdT2vmiti3mv6yo1F39yeEktkAaMrhlNUcvxPnP5y48HwzS4d8UruLYTyuZTmns9jRNJnwVGZmzKFacXyRiC5eIFeIJE4IocrdYbfs08wXPlYgiakXE1yqz340bqOUY7Wc4gkTLqJqKLJaXv6UrI87QsfIYKfZMPWHshwL8dc9KfXCMynbsAxABOQXWD2B2EZ7ii5vbn6Wy40jyU30-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=dmq7vGOD9Z3nYvlWuFx3H9JG3Fs0K5o4a6-niSY0lO_FQmODMZo1bMym5PGiFqGFua4faLKIZkhFxL2lqHH8p90Rnv72LQu7cpvAuwNk9DwK0UyOswZov_h1BhZXVHO0fKdT2vmiti3mv6yo1F39yeEktkAaMrhlNUcvxPnP5y48HwzS4d8UruLYTyuZTmns9jRNJnwVGZmzKFacXyRiC5eIFeIJE4IocrdYbfs08wXPlYgiakXE1yqz340bqOUY7Wc4gkTLqJqKLJaXv6UrI87QsfIYKfZMPWHshwL8dc9KfXCMynbsAxABOQXWD2B2EZ7ii5vbn6Wy40jyU30-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
|   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی غرامت با تسهیلات اقتصادی بحث شده است.
🔻
این پیشنهاد بر ضرورت تضمین‌های بین‌المللی، تفکیک مسیر دریایی از پرونده هسته‌ای و نقش‌آفرینی پاکستان و عمان در مدیریت تنش‌های تنگه هرمز نیز تأکید دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131848" target="_blank">📅 18:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131847" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbc9KfU3IFSlpftr3AGNBqn35szAJkrjnVFGcnuAuK6L5FqILtVwQJt4feWkhpu2gfy4PEjDr-afDihxNU9E2SHTuNcOuRklKo2Bo26_tVTiwA6XX8srTm5UP81aENmVoU4uL2SirMF-NF-oFMK5T5Wo6g3heNrLqwNLpFYjC2AXyOg7Gh1sExl1iAB0XnUe-p-9mPqi1hyuuQPd0B_w8rO_0rXh0auvH5WZpa-d_Y1hDb_hiOqPGM6ANs1M-WdvIubtAfJsme3z5OUTX_2osLfcD18dQOCitMFjBXYFp_dEGclyp_Qc4uOy9oowwMj79iv2Ed3HUvbxjfvUKYaFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مدیرعامل پرسپولیس عضو هیات رئیسه فدراسیون هاکی شد
🔺
پیمان حدادی مدیرعامل پرسپولیس با بهرام قدیمی رئیس فدراسیون دیدار و گفت‌وگو کرد. بعد از این دیدار قدیمی با اهداء حکمی، حدادی را به عنوان عضو هیئت رئیسه فدراسیون هاکی منصوب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131845" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89becc508b.mp4?token=OAKz2EWqrtakENMkyAPkEKxxZ02R9LnlNAlw5QNtGyrlfYe_h_t7zu-qzDu8qD8iXgQjfHat5jK2jAkB9da0fCyMgH8GCdIKiGw0tIeTPI9Px9np8Z69BiYNCiqb2momwsUjMjTcx6UBPZrSpMHEdP4sZ5JEK0kbcjdhTw6vlowNch6ZbUjkKPc06IrnY8HYMCh2U609agLSpmWZpqn6hVbcsAn6TTJ7Zz_ofYWTuKQsZmKRsCACux0Qoq2mt8asHZkLC1AQOcMBXLty__IyExOCvL_6GSqo5Hrdpv4Zs7oTF_Lf0w3CIODzk6_QabRuw8CqWsucg80OKxwehtRRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89becc508b.mp4?token=OAKz2EWqrtakENMkyAPkEKxxZ02R9LnlNAlw5QNtGyrlfYe_h_t7zu-qzDu8qD8iXgQjfHat5jK2jAkB9da0fCyMgH8GCdIKiGw0tIeTPI9Px9np8Z69BiYNCiqb2momwsUjMjTcx6UBPZrSpMHEdP4sZ5JEK0kbcjdhTw6vlowNch6ZbUjkKPc06IrnY8HYMCh2U609agLSpmWZpqn6hVbcsAn6TTJ7Zz_ofYWTuKQsZmKRsCACux0Qoq2mt8asHZkLC1AQOcMBXLty__IyExOCvL_6GSqo5Hrdpv4Zs7oTF_Lf0w3CIODzk6_QabRuw8CqWsucg80OKxwehtRRaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند/ ۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم/ شرایط سخت است ولی نباید بهانه بیاوریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131843" target="_blank">📅 17:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=dYKhGbCqX5vA9IE8xGg4Y5Q5kaSPbcKu-3FL-Zx75lsOL0IEsR84oYO6IbWvkw8rjciDKWTCRCcpkHI0ETBVYJV44GiaybiS3y9XndMVGO9XjNe4yPp918lQNAzPBu2DbMt4Xwn3TCMZYqqb9xILzFs8vgxfVuTkGoObWfP8hSUkonBo9Teqk_RaedSF6bo4O0RlzY4CAtJv0UGJZ3EO5jl3BPWHdE210bHI2Oan3otQu8DkE0S67kCc4tWBF3Fs-XIzAJbM2tytTN6p6Dsb8Jo3-htmR26ZG_gNvUy6QwqftlNX60XSGetGRkiqxbsU-S85bhO5OWgQIs5ftLrAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=dYKhGbCqX5vA9IE8xGg4Y5Q5kaSPbcKu-3FL-Zx75lsOL0IEsR84oYO6IbWvkw8rjciDKWTCRCcpkHI0ETBVYJV44GiaybiS3y9XndMVGO9XjNe4yPp918lQNAzPBu2DbMt4Xwn3TCMZYqqb9xILzFs8vgxfVuTkGoObWfP8hSUkonBo9Teqk_RaedSF6bo4O0RlzY4CAtJv0UGJZ3EO5jl3BPWHdE210bHI2Oan3otQu8DkE0S67kCc4tWBF3Fs-XIzAJbM2tytTN6p6Dsb8Jo3-htmR26ZG_gNvUy6QwqftlNX60XSGetGRkiqxbsU-S85bhO5OWgQIs5ftLrAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود کاروان تیم ملی به آنتالیا برای برگزاری اردوی آماده‌سازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131842" target="_blank">📅 17:21 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
