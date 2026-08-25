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
<img src="https://cdn4.telesco.pe/file/WoHnS_2hkvIzpsQ6EWu946M0kI-fjQydv79zg3rXWyiB2F_4JiD40MMAfAd-a4LVqDCflHo_j2DuWVN8mgsofemNBjmQ1RI2_Ffg3Y-n_AH3EQdi2F-dCAxmkygErVzdgVModY0Kq1ewvQJ5Xgb6sfxqAjtCjm0soo0Tr-j-BxabQIgOgUf7zAzOLrOycoczjxlsHJ-cHwp-aRdWX0iuJ7LY_f1QQvAwjKWxaeQMCIG6Ac3gA23vFQaA7vBVrlljhhZDIoyRmJSJ8WETaft9nHDL33CaiXrgVwL6OUM1xNQ0Fwr1WAHf_j5pROe_HQ4k0aYp2JVQDp-TfyIFa3BaeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 441K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 22:36:47</div>
<hr>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اکسیوس: زیردریایی‌های بدون سرنشین نیروی دریایی آمریکا، به مدت چند ماه تنگه هرمز را جستجو کردند و بیش از 100 شیء را شناسایی کردند که به عنوان مین دریایی مشکوک بودند.
بر اساس گزارش‌ها، ایالات متحده همچنین از شرکت‌های خصوصی در این عملیات برای شناسایی و خنثی‌سازی مین‌ها کمک گرفت. رئیس‌جمهور ترامپ امروز اعلام کرد که مین‌های موجود در مسیر اصلی کشتیرانی در این تنگه، برداشته یا منفجر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/withyashar/21508" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4cRN45EioUAQE_rZp2Gmox0wjSEZX16uOga59obP9HMVcZxNJPOYFp4Ee9ZI8G9-memXb5K0s-DlAumr_UUeY4ZmqLaWaCX27rI9jTSAsZguAMkUoYmtr2TZ6DrkCdLfB0723sxJPC44Bjo12jdWGtxa-vk7zM7U4Yp7qCwY4dPlceHqeqyuDwcn4K2Accc3toQuXV0Md7DLDb4x8S6DVKkbFWrzQCq5YtRAAz2bnKUF-2BjLJeXY07mHo5BiSl02x5Ef6nwhgBvUTHJa1xxuBmsTVj1L_Rnxq84UUwfA8TBMlkklunIcEJiw9BVprkAc6wBeNxyOgZ9G_AH0jJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوه اردوغان , حالا اسمشو چی گذاشته باشن خوبه؟ گذاشتن «گوزیده»
«گوزیده بایراکتار» (Güzide Bayraktar)
@WarRoom</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/withyashar/21507" target="_blank">📅 21:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زلنسکی: به موشک‌های پاتریوت دست یافتیم اما به تعداد بیشتری نیاز داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/21506" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پاکستان امروز رسماً از وزارت خزانه‌داری آمریکا درخواست یک سازوکار ۱۰ میلیارد دلاری برای تثبیت ارزش پول ملی کرده است؛ بزرگ‌ترین درخواست از این نوع در تاریخ پاکستان. این درخواست پس از افزایش نقش پاکستان در میانجی‌گری میان آمریکا و ایران مطرح شده؛ نقشی که روابط اسلام‌آباد با دولت ترامپ را تقویت کرده است. پاکستان در حال حاضر حدود ۱۲.۳ میلیارد دلار بدهی دوجانبه کوتاه‌مدت دارد که برای بازپرداخت آن به تمدید مداوم بدهی‌ها از سوی عربستان سعودی، چین و کویت نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/21505" target="_blank">📅 20:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB8MbBPPVyPNSzgZlDH6WJ-vKH_h5KqIGy-j3GMUek2EiN1PZJEUusntvouHCw-4NhClzfH4ZPpsp2J7ZKXq4kZ7k2PJ7yqyPSSEY4xoHFLr1IKcqHU79UryZCm_-T_95_xnNhRhN3FCSdnJWi8gIgX3OFbtu9C588LZSCSAaMGppAQp8tL_6HTvd7pPkQkaTWOiWSU--jTUX71QEF__Xs3s-ie2R4JQQxh8VBfpwzxfloDxh3WczgJs7Tpggl10F1_Mo-u7_koByBShnGtsegbl7IxhPqEEj-nD55bopd-uqsRnrjyJGMjVJ_E5ZjsYaL1I7MRe2btDclF0Ax5KHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : نفت داره میاد پایین ، ترامپ داره هی‌کارای مختلف میکنه که نفت رو بیاره پایین و جمهوری اسلامی هی موشک ول میده که بره بالا !!! فعلا تو این لوپ گیر کردیم…
@WarRoom</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/21504" target="_blank">📅 20:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تنگه دعوا شده ، صدای انفجار ‌از ‌تنگه شنیده شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/21503" target="_blank">📅 20:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yde8DiOSiilvK6LLDwgJcgKMC5ZHjxH0lCFJSF9Cp9eclNR7TzNPy5siReh9ADOn5wBGUmADK7sowPMHEryqAUMnGiq2cW64f0mcDtSbH9CvX4IVXmHDNmPxQUnf73RQASImWIobgTY95hcflVyLn4PcfHw5Wp_8pzz0SWvPnolnQSi4cmaFRwL8s-_CdA03vHlD2_rVLOr0g4CI8uSnteYV3qwZmO7BA2I9RL5baQJgXjxfzANYQgVeWmhlUnI1Dsud3PqQaSCKp9B6dn1_yJJLy1zPwWHAjGzRAux_dfvt0h9l9Ng6seT8hQDluN1C7a4YbnvBRTHQOYb6Oo96tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی ، سخنگوی دولت : مردم منتظر بهتر شدن وضع اقتصاد در شش ماه یا یک سال آینده نباشند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/21502" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بدر البوسعیدی وزیر امور خارجه سلطنت عمان دقایقی پیش وارد تهران شد
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/21501" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اردوغان:
اجازه نخواهیم داد سناریوهای خونینی که برخی برای منطقه ما آماده می‌کنند، اجرا شود و از حمایت خود از همسایگانمان دست نخواهیم کشید.
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/21500" target="_blank">📅 20:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ : آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/21499" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صفحه امروز نیویورک پست : آمریکا جهان را تحت فشار می‌گذارد تا آخرین ضربه اقتصادی را به ایران ورشکسته وارد کند و ملاها را کنار بزند. @WarRoom</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/21498" target="_blank">📅 19:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیوز مکس : ترامپ در دور دوم انتخابات جمهوری‌خواهان، رأی‌دهندگان کارولینای جنوبی را به نفع دارلین گراهام بسیج کرد
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/21497" target="_blank">📅 19:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیانیه ایران و عمان : ایران و عمان در حال بررسی یک طرح مرحله‌ای برای
بازگشایی و تأمین امنیت کشتیرانی در تنگه هرمز
هستند که از یک کریدور موقت و مین‌روبی آغاز می‌شود و می‌تواند به ایجاد یک سازوکار دائمی برای عبور و مدیریت تنگه منجر شود
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/21496" target="_blank">📅 19:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو: اگر به ایزنکوت گوش می‌دادیم، حسن نصرالله الان زنده بود.
غادی ایزنکوت یک ژنرال بازنشسته و سیاستمدار اسرائیلی است. او همچنین مدتی عضو کابینه جنگ اسرائیل در دولت نتانیاهو بود و اکنون رهبر حزب «یاشار» است و جدی ترین رقیب بنیامین نتانیاهو در انتخابات پیش‌رو محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/21495" target="_blank">📅 18:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaOnOg10qTOWQzxbzdcVg3BK3_e9qd-1V11QaH8qkUqCiKNtOS6uRBXA8W151iqxkf_g0SXBP6w_2S20jRk-LkRMZ_L7GIO_89KIMy8e0EGEKnuazSdck6rUZbxJI7vudZJL6OWLlDdY39U1K6kHJahhlr96w4DSJUQaxURrwlzqN96_LeZ0muXsIpCrVnO-bSp_eeh_ZLaLxUSVG96W3Vusn30LqOYzwR6Du-lNj4vHmHa9z-cfv9YRu_XkQVIjvEQwM8QRewUfZPIWkmX-gDskS4ZqQp9Aq7oQFKQNzBOkhPj8IAcMCZMdmRMHIQSg661NhyIG-q4s0JiEGtnnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/21494" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA81FnDdLjxDRB7LywFLI0gf6KssM8BIvtTNDz5ZqedZf8wI4PaxGMM2hDTCLXsmeSbKVtTpM4f3OEJ3areyP4pd4q4Ql8fSVNSfbNoG7-BfevxV1q97LTAE279VY7WRtuPbWVFj3ecJxlS32k9DU-9MbTO1NEmlU_YMfmOZH7Abat7dtj2RLowUBA_rapUuKkoD-S0WO4i3vXHMmuzQDbtlEYzu8wa9VoWC4JeMfFbWmYl4k1IEj40eLmnun8KfnFpkog48Uxqot9QRy0BshOpj_SH7QU-3Rj1-rvMMQMnu43bUUSYIarU7CxMiHEffeSGLy68b2zM4RP2Z5Jm23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: نیروی دریایی آمریکا به من اطلاع داده که تمام مین‌های موجود در آب‌های بین‌المللی تنگه هرمز جمع‌آوری یا منفجر شده‌اند. به ایران هشدار داده‌ایم که هر کشتی یا قایقی که اقدام به مین‌گذاری جدید کند، بلافاصله و به‌طور سیستماتیک منهدم خواهد شد. آمریکا با استفاده از نیروی فضایی، تمام نقاط تنگه هرمز را زیر نظر دارد و سیاست «مدارای صفر» در قبال مین‌گذاری به‌طور کامل اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/21492" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مقام کاخ سفید: محاصره دریایی به طور قاطع و مؤثر در حال اجرا است، تنگه هرمز باز است و تمام مین‌های کار گذاشته شده برداشته شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/21491" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlCqBy6OBtmFaqtWfd7zTKS3NDpX_ZCmpq2V8xRqmYgjPTVWrOAdXpPlwTa72qnsn9xaRXtDq9B0Bt3gtNe-GCDUYi0Txifg7H1q0sGucJr71XvOkMuZkzOqlf5EYpwS1UPwquX-5rWvaHDifAutUYxtuXIAoM3Gy1W3kD58FNqHF3nEFBTrXQH5Dk__NAL0Olq_Umicjwmpu8OOJK4YKnQOeqaN1ZyY2WoqJzKzV40Dvdp4oZriz94yic6ahKTzcAoxtwCnUSFidACVsjAOVYlUxa-qDnGPd42zp8t8OmPBKzMsOA7hUXST7NhHmiXJXCYdFIhPjmleryKct13tSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بر اساس رابطه بسیار خوبم با کیم جونگ اون، رهبر کره شمالی، از این واقعیت خشنود نبودم که ایالات متحده مدت‌ها پیش با شرکت در رزمایش‌های مشترک نظامی با کره جنوبی موافقت کرده بود. این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش بزرگی از هزینه‌های آن، طبق معمول، توسط ایالات متحده آمریکا پرداخت می‌شود، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری ارسال می‌کنند که از زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده است، تهدیدی ایجاد نکرده و محترمانه رفتار کرده است. بنابراین، با توجه به اینکه برای لغو این رزمایش‌ها دیگر خیلی دیر شده بود، به پیت هگست، وزیر جنگ، دستور دادم که رزمایش‌های مشترک نظامی را به میزان قابل‌توجهی کاهش دهد! در موضوعی که تا حدودی بی‌ارتباط است (؟)، اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایل هستند در روند خلع سلاح هسته‌ای جمهوری اسلامی ایران به ما بپیوندند و آنها گفتند: «نه، متشکریم!» از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/21490" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صداوسیما در اقدامی ، اطلاعات به ادعای آنها محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد. @WarRoom</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/21489" target="_blank">📅 16:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ناو آبراهام لینکلن پس از ۲۵۰ روز و جنگ با ایران برای استراحت در تایلند پهلو می‌گیرد یکی از مقام‌های تایلندی امروز اعلام کرد ناو هواپیمابر آمریکایی لینکلن قرار است هفته آینده در این کشور آسیایی پهلو بگیرد. @WarRoom</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/21488" target="_blank">📅 16:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbXsxpe9vzmnMIsetaFdobEwotngoYXPfac0cbr0p3eQRMzA3kdwsYGV2cD_fnCQksiMlxuzF7QHNuLPkRj4W6ncS__W-Y4vwyNI1Q5G7V7xlDQs8fC4GOwKnRvGfiaywv8ab1t0TSjlvcyW_L9LF6hsarEzEX1mvu_6xGw441WkUmqRDZfujXah8nBuhg8lVuMfqSaMHJ8P7gaVNCXQ_3IH5BxzHsRBJshPqnTFidDrhARS_uD76kl7DVgodeqK4cit_lqmPH18T5cyjqIyQT0LRmjZmKg3auziho7I_d0Xa6aETm5ukTFngbWJyMvVx7ujaQtO0VZOZeDo-sqRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو آبراهام لینکلن پس از ۲۵۰ روز و جنگ با ایران برای استراحت در تایلند پهلو می‌گیرد
یکی از مقام‌های تایلندی امروز اعلام کرد ناو هواپیمابر آمریکایی لینکلن قرار است هفته آینده در این کشور آسیایی پهلو بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/21487" target="_blank">📅 16:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb6sj64ecuRu9jzrtXRB9ijalaDc368bSzU-x9dTdgvBSuRJ8kFqnDQC7IFj-pJajzECBbd6comCv-mTSn6bsE_yB0DdxQVvU2_yMWznQC6cp6tnaKhmhXXIm5RKRf6lits9NSHJnwgSLGXQ6N45uaBGvB7VbdZ7MwfhXcTsTOHidJUKUA0OUXING5UdQu4vT4eHho2MkjA25-KfQqaQ4mUACOscY-MUezUa2NwqXqY1j3gm_vQJkAcewMHGKK4j5Pn3xe5PlVMjPX5c8QrmA4__e_sHaCICxvTO2lS65AOLNZ3zpDzhqXJs-s1y53N-cmFlQHK6M2zjSokgVPtNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : موتور جستجو و پرینت مخفی پست های
ترامپ
ناتالی هارپ، ۳۵ ساله، یکی از نزدیک‌ترین دستیاران دونالد ترامپ است. او در کالیفرنیا و در خانواده‌ای مسیحی و محافظه‌کار بزرگ شد و پس از تحصیل در دانشگاه، در جوانی به سرطان استخوان مبتلا شد. در سال ۲۰۱۹ در یک برنامه تلویزیونی حاضر شد و با تعریف داستان بیماری‌اش، مدعی شد قانون «حق تلاش برای درمان» که ترامپ در سال ۲۰۱۸ امضا کرده بود، امکان دسترسی او به درمانی را فراهم کرده و او را از مرگ نجات داده است. این حضور تلویزیونی توجه ترامپ را جلب کرد و ترامپ پس از برنامه از او تمجید کرد.
او سپس به کارزار ترامپ پیوست، در همایش جمهوری‌خواهان سخنرانی کرد، مدتی مجری یک شبکه تلویزیونی محافظه‌کار بود و در سال ۲۰۲۲ مستقیماً به تیم ترامپ پیوست. از سال ۲۰۲۵ نیز به عنوان دستیار اجرایی رئیس‌جمهور فعالیت می‌کند. هارپ به دلیل اینکه تقریباً همیشه ترامپ را همراهی می‌کند و با یک چاپگر قابل‌حمل خبرها، نوشته‌ها و تمام مطالب اینترنتی وایرال را بدون واسطه برای او روی کاغذ چاپ می‌کند، به لقب
«چاپگر انسانی»
مشهور شده است. او همچنین در مدیریت شبکه اجتماعی ترامپ نقش بسیار مهمی دارد و خودش پست میزارد و ولی اکثرأ متن‌هایی را که ترامپ برایش دیکته می‌کند، تایپ و منتشر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/21486" target="_blank">📅 15:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/21485" target="_blank">📅 15:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/21484" target="_blank">📅 15:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/21483" target="_blank">📅 15:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzjMpasAt-WN8rk1rCKPTjdoc7V7TD2yoTubnQjHVM7skVD0j7llVai200JO2d0L5F-ovsExdKvwUgwRDOY2epzT9w2WNR0Esdvzxubhx8MURNaRNvhyX94N5dLiKzVBuEqgtvYS9UkuiXxzHGWkZ376Z9RUHDHZ3tOQa7t_RjtRck4F706Nz6V4fdYLY2DpdusAQH6mcV-CFmviUaPooYqU342Sf3kYceKf1X6iu7NJzG6mCHBwQX596ZvvBBdpr8rle33Anvq4xT2DSoPp9oCyMfu5gtWdaGcGLUdy8ujZlxKR_IjeavrJVg0jewjv9sbUz8pd1OhaEmMHsdeWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : جمهوری اسلامی شکست‌خورده ایران به بخش‌های گسترده‌ای از نیروهای مسلح خود حقوق نمی‌پردازد و هم‌زمان معترضان را می‌کشد حتی زمانی که آنها اصلاً در حال اعتراض نیستند در ابعادی که پیش از این دیده نشده است.این یک بحران انسانی در مقیاسی عظیم است و باید همین حالا متوقف شود.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21482" target="_blank">📅 14:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf545tP9v8IExDBBQb-WSTtg_xR7vzWn2bUzTAEbJdtP-5u7qsQsH7WDO4W6WPA9Mq_IQIKB62GDwEo8NAyTLQAJVEN6ls7wqTU-cBL9wVz8qCbZOUjrZEcF0luWrhGkohbOUHiPVIYeYSbbtSlcdWynQz2OsuCUs4DRst1sz_aNlzovKdNQ2MiFJfROQN5RM3BodtYYOeF8VxwABayyqhG_3UG629v5jiACp_fAlDBaYx6mGSTqjbdcExf5cHnOz860Em-wZCfOKF55i1W2hHsg_BceLo62JezRcN8HVbUSt9yl4rVJZE8fbQlhKLcoT3vrH_tdkm4ms0wvwy3wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه امروز نیویورک پست :
آمریکا جهان را تحت فشار می‌گذارد تا آخرین ضربه اقتصادی را به ایران ورشکسته وارد کند و ملاها را کنار بزند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/21481" target="_blank">📅 14:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران؛ فرماندهان ارشد نظامی تحریم شدند!
آمریکا پنج حوزه
دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی
را هدف قرار داد و شبکه‌های مرتبط با برنامه‌های موشکی و هسته‌ای، عملیات سایبری و انتقال درآمدهای نفتی ایران را تحریم کرد. در بخش نظامی،
امیر حاتمی، رضا طلایی‌نیک و محمدباقر ذوالقدر
تحریم شدند و تحریم‌های چند فرمانده ارشد دیگر نیز گسترش یافت. همچنین شبکه‌هایی در
ایران، چین، هنگ‌کنگ و مالزی
و چند فرد مرتبط با حملات سایبری و وزارت اطلاعات هدف قرار گرفتند. آمریکا چند شرکت، فرد و نفتکش مرتبط با
ناوگان سایه و انتقال نفت ایران
را نیز تحریم و پنج معافیت تحریمی را تعلیق کرد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21480" target="_blank">📅 14:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رژیم ایران اعلام کرد که سفر سرلشکر عاصم منیر، فرمانده ارتش پاکستان، به تهران «بسیار پربار» بوده و به دستاوردهای دیپلماتیک چشمگیری منجر شده است که به زودی «آشکار خواهند شد». محسن نقوی، وزیر کشور پاکستان، نیز گفت که مذاکرات شامل احیای تفاهم‌نامه اسلام‌آباد بوده و «پیشرفت قابل توجهی» در این زمینه حاصل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21479" target="_blank">📅 14:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اکسیوس: ۵ نشانه از فروپاشی اقتصاد ایران زیر فشارهای ترامپ
؛
۱.
سقوط ریال:
دلار به حدود ۲.۰۲ میلیون ریال رسیده است. ۲.
تورم شدید:
پیش‌بینی می‌شود تورم ایران در سال ۲۰۲۶ به حدود ۶۸.۹ درصد برسد. ۳.
فشار معیشتی:
گرانی و کاهش ارزش ریال، تأمین نیازهای روزمره را برای مردم دشوارتر کرده است. ۴.
سقوط صادرات نفت:
محاصره آمریکا صادرات نفت ایران را به‌شدت کاهش داده و درآمدهای نفتی را تحت فشار قرار داده است. ۵.
رکود و بیکاری:
افزایش بیکاری و کاهش فعالیت اقتصادی، پیش‌بینی رشد اقتصاد ایران را به انقباض حدود ۵.۴ درصدی در سال ۲۰۲۶ رسانده است. با این حال، اکسیوس می‌گوید هنوز نشانه‌ای از تسلیم تهران دیده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21478" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دیدبان های اتاق جنگ گزارش های زیادی میدن مبنی بر فعالیت های مختلف‌ و حتی ‌در مواردی عجیب رژیم که همه شما هم حتما شاهد هستید در سطح شهر ها ، که مشخص میکنه بدجور ترسیدن و دارن برای مقابله با شروع اعتراضات ( انقلاب ) آماده میشن
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21477" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏وزارت خارجه چین در واکنش به تحریم‌های آمریکا اعلام کرد تعاملات چین با ایران مطابق قوانین بین‌المللی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21476" target="_blank">📅 11:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وال استریت جورنال : چند روز قبل از صدور دستور حمله به ایران، ترامپ هشدارهای صریحی از سوی سازمان‌های اطلاعاتی دریافت کرد که به او هشدار می‌دادند که ترور خامنه‌ای منجر به سرنگونی نظام نخواهد شد، بلکه باعث ظهور رهبری تندروتر و سرسخت‌تر خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21475" target="_blank">📅 11:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB5E3xAc_QdmVpKLVMXmocTu1Ot0CE2U-nId5llbwL4JyTo8q4GtT2FAaOjSwYw-cpYYx7-kvzaz2qUvEZUMnXmo89U3S2X3t8mGjg4qhCP4NMHqn8qi7JiG4KSAHd_D7hLlpmkX1aDR21QWqc2UFMOXwzesOY2Ok2Yj_XgYtKc1yoeplI96xlBGtMJbaGEaeXRRyC060kI1vevhDzvdbh9gK7DVxUJd8p6S7-DeWykf_bqRNBPZx5heGtd2f7CbSFzmWocSdPPm9gfnduAzdS-QAkGh3aQCSsgkPnF7Z7g8Z1DZI-OuEQA1IsEkLoZ9BXocTaaIvT2p-pDDeeXPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون یک F-35 از سمت خلیج فارس به سمت عربستان سعودی سیگنال 7700 روشن کرده ودر حال فرود اضطراری است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21474" target="_blank">📅 04:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏شاهزاده رضا پهلوی با بازنشر تصویری از دیدار خود با زلنسکی، سی‌وپنجمین سالگرد استقلال اوکراین را به مردم این کشور تبریک گفت و نوشت: «در این روز مهم، مردم ایران در مبارزه مردم اوکراین علیه تجاوز و اشغال، شانه‌به‌شانه آنها ایستاده‌اند. همبستگی شما با مردم ایران…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21473" target="_blank">📅 03:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏شاهزاده رضا پهلوی با بازنشر تصویری از دیدار خود با زلنسکی، سی‌وپنجمین سالگرد استقلال اوکراین را به مردم این کشور تبریک گفت و نوشت: «در این روز مهم، مردم ایران در مبارزه مردم اوکراین علیه تجاوز و اشغال، شانه‌به‌شانه آنها ایستاده‌اند. همبستگی شما با مردم ایران در مبارزه آنها برای آزادی هرگز فراموش نخواهد شد. ما همیشه دوستان خود را به یاد خواهیم داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21472" target="_blank">📅 03:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏آسوشیتدپرس گزارش داد که دولت دونالد ترامپ در حال آماده شدن برای لغو روادید تجاری و گردشگری حداکثر ۲۰۰ هزار تبعه خارجی است که برای دریافت پناهندگی در آمریکا درخواست داده‌اند یا در حال حاضر به دنبال دریافت وضعیت پناهندگی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21471" target="_blank">📅 03:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کارلوس آ. خیمنز نماینده فلوریدا در مجلس نمایندگان آمریکا : اردوغان همچنان فعالانه از تروریست‌های خشن حماس که خون آمریکایی‌ها بر دستانشان است، حمایت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21470" target="_blank">📅 03:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کوینتلگراف : گانون کن ون دایک، سرباز آمریکایی، متهم است با استفاده از اطلاعات سری درباره عملیات برکناری نیکلاس مادورو، بیش از
۴۰۰ هزار دلار
از معاملات پولیمارکت سود کرده است. او اتهامات را رد کرده است.
کمیسیون معاملات آتی کالاهای آمریکا
تلاش دارد در پرونده کیفری او دخالت کند و درباره قانونی بودن قراردادهای پولیمارکت نظر بدهد، اما وکلای ون دایک با این اقدام مخالفت کرده‌اند. رسیدگی به پرونده مدنی CFTC نیز تا پایان پرونده کیفری متوقف شده و دادگاه احتمالا اواخر ۲۰۲۶ یا اوایل ۲۰۲۷ برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21469" target="_blank">📅 02:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQo3dAagAUSb6NDgQtEwT0DHCGPNj6GxbZGLBHxqCIuMaNFNANZkJUv5oqSCLjHI9nCnVhRoj4E2IyrFRGQm8HkX8QpY5Emq4qtTTmH5FRrm4QiF3-9mBU0UjOMPGCW17Zmix38dW3EpUO8Cxv2HdNIbPEeNYMFzNErARxXwaDrn8vpDsQlzIQmKk2RzyZKEemcTpA86zfizePUcAlSjqk09_bo546BJ-KrueC0kAH-ZGLOrp6ECQIqVgeWCEse1_-6D92dGJIHlSGLua-Qvt_bVrGgdYnMMWUo4VJ79OzqSrFy3grvOzz7ml8OPsyftwbbxtw_woJmXGcCf5ClNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست : ایوانکا ترامپ در سفر خانوادگی به کاستاریکا، مهارت‌های موج‌سواری خود را به نمایش گذاشت.
ایوانکا ترامپ و جرد کوشنر در سال
۲۰۰۹
ازدواج کردند و سه فرزند دارند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21468" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncKVPwPDHEVIYc0jU1oMMRDRACRveA2QZCsUTX-TcB5fPgeEyiGo2dKH9B-FRU1GVmnmo4PnCnAw-6d6bijT0wenPGrI1rJST7QPdeCc7lTNbiE-Jb06JyWmlm_ErSL291E7PPDpX-Kl2RlKMf2NSduwDo_Xqnk8V60aPS_FxN6AlIk-wJZV_Wrk-MGNcTSLMpgOC9-iS-qKJMyVbbsfBuutkjtVxqSd6RHslX1Bvb5NRVJcZFX9pdVLtnNcOvSlmjSTk4JH5wjMW8KSQMka-iEKKMPFeghKIBkh3ISt0unt7PKiFgxR18l5XADf7_qQuDRx0onn1K0Eq6gy0EC2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : تفنگداران دریایی ایالات متحده در حال انجام تمرینات سنگین آمادگی بر روی ناو جنگی یواس‌اس باکسر (LHD 4) در حین دریانوردی در دریای مکران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21467" target="_blank">📅 02:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21466" target="_blank">📅 01:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVhcM4u57HlgkbZl3d05l4xqufIZ4yMQ7OAAPWeK8BS7uIkSFnubqvuow3OCqTVrP8FCbYLsebep4vuMhyv-yXDlWfbukYoImCDMAD_2w_WfjevZroAImhJjxty-IEhp0kU5pLWesXGTWIjdKQCybP5BDxwQNlGlfwtI2nbL4bhOM9XWYHr9bv40NCGzvKMkLdMLcm1Jv-usW3BKuNhNCjFWrqp4YVswXOdkDQGoxSE469giX_GXARbX-byUDqm1ozj5DW33NQZ1VVSu70sbgEmtMlkhutJWTG8fIVytWwfOjWVdL95A9UTRWsCGnh4AGGOtpFAgsSwZ-0sIEvdgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت بازمانده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21465" target="_blank">📅 01:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مارک لوین : ایران سعی کرد یکی از پسران نخست وزیر نتانیاهو را ترور کند. آنها همچنین برای سر بارون جایزه تعیین کرده‌اند…
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21464" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=jAe8gB_XGAMhnG02p3DRLQKo-FFmyBAIt19KHMGRLWPkJwAGNsBb4Pe9zls3FEJLHuH54JMdhsJsL3wxhZNpxVpt8DGigoDL-xm_9mXP8HFPEKtHqdfg9yliW1ejOcRhW7SWZtA_Qfmhom665RIuFSqUOvwnKUaFgz4PDe182wIR1QlXQD5V6gZki8hmCaySFxX7K6BgzqJTLJovGHn13jOWddOt70jyuiKMb5sJv--jp1Rs6BY0WgWRNfkRxCGDfFhgSieLNaz7ONTk46nLBxKllNgQVzGF5gdCZWcoOIWH3eNYekgrv0DvLCaYsSje3CXshgQ1rsYm4loPDNWvKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=jAe8gB_XGAMhnG02p3DRLQKo-FFmyBAIt19KHMGRLWPkJwAGNsBb4Pe9zls3FEJLHuH54JMdhsJsL3wxhZNpxVpt8DGigoDL-xm_9mXP8HFPEKtHqdfg9yliW1ejOcRhW7SWZtA_Qfmhom665RIuFSqUOvwnKUaFgz4PDe182wIR1QlXQD5V6gZki8hmCaySFxX7K6BgzqJTLJovGHn13jOWddOt70jyuiKMb5sJv--jp1Rs6BY0WgWRNfkRxCGDfFhgSieLNaz7ONTk46nLBxKllNgQVzGF5gdCZWcoOIWH3eNYekgrv0DvLCaYsSje3CXshgQ1rsYm4loPDNWvKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟
پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم باشد انجام خواهیم داد. فشار اقتصادی در حال حاضر بیشترین آسیب را به آنها می‌زند، اما به هیچ‌وجه استفاده از حملات نظامی را، چه در تنگه هرمز و چه در اطراف ایران، منتفی نکرده‌ایم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21463" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=A-p19aeDGksegMkX0bDcxbIZgfQpM3DEcwkUVqwptsLU-fODWo31eb0OatsqpV-fgcZk0prlUb_lPBMw98W_zpW3-rMYSxO-OgT_qRSusMNzR-SidP81TGdsJ14ZYG2arGP4GZsOWbUVat3YMQ-4YS9SRjjibtJdSOu4Ptoq39itmYv0MglQObT_bf4eENFuXSqBF1vsD7MBUKSAv8tVD1LP_jG_6K6WN6qwWVPifuxwkX0DmiFp5fueKEmFPJyQfHxm-6DQ3k2JiPouFeYDgzt5GIV_dk0BNJQENo9uH4ADooMCNbXNVhnHZ5I4Vuld5sh3v16ojPYGiX9WjpKtXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=A-p19aeDGksegMkX0bDcxbIZgfQpM3DEcwkUVqwptsLU-fODWo31eb0OatsqpV-fgcZk0prlUb_lPBMw98W_zpW3-rMYSxO-OgT_qRSusMNzR-SidP81TGdsJ14ZYG2arGP4GZsOWbUVat3YMQ-4YS9SRjjibtJdSOu4Ptoq39itmYv0MglQObT_bf4eENFuXSqBF1vsD7MBUKSAv8tVD1LP_jG_6K6WN6qwWVPifuxwkX0DmiFp5fueKEmFPJyQfHxm-6DQ3k2JiPouFeYDgzt5GIV_dk0BNJQENo9uH4ADooMCNbXNVhnHZ5I4Vuld5sh3v16ojPYGiX9WjpKtXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد تا امروز (۲۴ آگوست)، نیروهای آمریکایی ۷۱ فروند را تغییر مسیر داده، ۳ فروند کشتی را از کار انداخته و ۲ فروند شناور را به عنوان بخشی از محاصره جاری بنادر ایران، توقیف کرده‌اند
ویدئویی از ناو هواپیمابر جورج بوش، مستقر در دریای عرب و پرواز جت‌های جنگنده F/A-۱۸ نیروی دریایی آمریکا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21462" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZkLhGbzFJm8WLx_eSEJQBaHabSyiJLi6k7aJBMUWXp59eeZDZnd-cf9SY465HvMZJwYSXhu1oJlYxn4osvYFvo2AdIJct6v5SuMrw0XL4ZIZpWHQM9lVfzmILsfxLlzw5jG9AKkK1rnCt0W6ttTyjnGjFjuOXTYBGcovlMruG-0MPkxqmJE1NEBVXphoohD0-XY8ypCtL6BB9HoM9t8pNhKbkGvXM9wHAbldoLwpd10OaHx1gonjQvhxPy9o1xdyGanOFjwS1oU8AVc2F8sPmiFiftWaYWYNxONMJCq3bA6KhNvlgiukRrvFqa4UAqgMq8NC-6rFjV7w6tAFBJdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم پاکستانی سیک و زد برگشت… همکنون نزدیک اسلام آباده ، همچنین ۵ سوخترسان آمریکایی همکنون با سیگنال روشن در حال انجام مأموریت در تنگه هرمز  هستند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21461" target="_blank">📅 23:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiSb-dlf-JRPyLJDqGdPvg3VbK7JVfT0kpg1pIsVmBOpTBn87fqM3VwjHjJPdBZpTxmvXVPgcrCamC3UUsahNhPSI7r4eMXwhY_kQO36ZxfMs8YhsHVxlaqZiC-Ksi3ARGcbhrn71EFAaRTPPpjjsKg4yy-Mtn4e8v-76YPT6CYo38NpwPCE5E5u8ZBIYNddt9SWjS8PBgg4VVjN1vNUdxo0P4kh5yw0ItVSQY-mV6Gre0K1lrBvAxoxtm_R82E1Sdd6GAVZ-qj3zbSOLeE4iKryxzQ-x5Fjxn5eSjxLM7Ee4CoRCj6oG3rKfyS9dMMIXTh8FtzK_cW4X9FIRddebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا، اداره امنیت دیپلماتیک، برنامه «پاداش برای عدالت»:
تا ۱۰ میلیون دلار پاداش برای اطلاعات درباره رهبران کلیدی سپاه پاسداران انقلاب اسلامی ایران.
این افراد فرماندهی و هدایت بخش‌های مختلف سپاه پاسداران را بر عهده دارند؛ نهادی که از دیدگاه دولت آمریکا، برنامه‌ریزی، سازمان‌دهی و اجرای اقدامات تروریستی در سراسر جهان را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21460" target="_blank">📅 23:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4O8EX2NsGEYDA0yvO6oDHZO48ax1SZ-cRsRjTvjQlB9mSxsZ_3_1ALwPP-W0PNSbReXnR2yKX5lLbO0ORwz9c76fB0QuI1dBURTJBUOhsxYZOx1WvxPSt6VEGZzRRcKQ8XRP4Is8ytMHDSBBYxJ61Xl4X_TedsDeFR7HsNpLoLIueth9Mh_aOpo5zEer_YEVvnSBUIFd4dgleTYw87FfRszt9h6_hMrccL4gl9bEEV456TV1-gX-SfINlWcEEwZGDUwdlImhTPln9_KY5c7KQj0X25RtKGXmMrtRSUZ2Xd9GDAQQNQYWhR8C5K1g4rBiIC5zm-O42dXwJ3BlkXE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن کج بند رضایی : نتانیاهو و ترامپ یک برنامه برای 6 ماه محاصره دریایی و اقتصادی علیه ایران را دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21459" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو : تبریک به ترامپ و بِسِن بابت آخرین تحریم‌ها علیه رژیم ایران.
شما به حق هزینه گزافی را از آن دیکتاتوری ظالم و از کسانی که به تجاوز مداوم آن کمک می‌کنند، دریافت می‌کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21458" target="_blank">📅 22:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">@WarRoom
Economic Covid</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21457" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پرس تی وی : ایران مستقیماً پیشنهاد مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد  ایران از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21456" target="_blank">📅 22:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=TYOPTKdwaOUGhphLdgFyp4HdCpQw7Pvq3HymfAWHHCBNrm2HGaGyxVgT9eFgtI6pC2uozBuqgtAql9nPpGkLoJMdyV5SgYh6pgDggLe1wjn8RF8mvGRhfjZ6VeC5E68QtoF-rHYl84vuBmrUqp-HszpU_-msFuIFTDjAWXj2BkMBDrFTDutdoOTmJIiuTy3HNFg_p2V3yuzAeWF3FYCw4vycFzwDD53A4O2oeA9u--hU4adUrML001eW-c3goSti6D5ogzC23CacsOn8v1aJYMbzIYk2XqLhph5hHeetO_CV70zp5s_NYoveoLGVQP0RybD3byFVdDNKGDGsh29D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=TYOPTKdwaOUGhphLdgFyp4HdCpQw7Pvq3HymfAWHHCBNrm2HGaGyxVgT9eFgtI6pC2uozBuqgtAql9nPpGkLoJMdyV5SgYh6pgDggLe1wjn8RF8mvGRhfjZ6VeC5E68QtoF-rHYl84vuBmrUqp-HszpU_-msFuIFTDjAWXj2BkMBDrFTDutdoOTmJIiuTy3HNFg_p2V3yuzAeWF3FYCw4vycFzwDD53A4O2oeA9u--hU4adUrML001eW-c3goSti6D5ogzC23CacsOn8v1aJYMbzIYk2XqLhph5hHeetO_CV70zp5s_NYoveoLGVQP0RybD3byFVdDNKGDGsh29D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21455" target="_blank">📅 22:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایالات متحده، سوریه را بعد از ۴۷ سال از اوایل انقلاب اسلامی از فهرست حامیان تروریسم حذف کرد
‏سوریه از سال 1979 تحت تحریم‌های کشورهای حامی تروریسم آمریکا قرار داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21454" target="_blank">📅 21:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c663b3442.mp4?token=UmwnQY2X655ovMu8BsyoPXpBZFp5qqLogmZ1MmH68AYIslVu_-RNBn9rpoNq9pXx47_jCYiIn4dK103mWp2kj6L414UpnrMqYG6MM43wO5Y3crt28FR153Ne0G0ahjUbw5riG_-jGLAD7G3r05I4hMuGYejrCdhCIP06QoPdMoHXMGGx2crI_IGhDwUZSE1pdJdRPdlLTaKsUgNnbKJi2l1uGhf0qY_lukDMlspzmHOoJOSyj333FABpTs5oUb8W3BQPgqVJrDpXM9Nn8ejZSrOkXkLzJJ5iwDNe0wynYvY6RK5VUiFZ9vG3UFx__h9kHGxB306vdBVLHhthr_6yIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c663b3442.mp4?token=UmwnQY2X655ovMu8BsyoPXpBZFp5qqLogmZ1MmH68AYIslVu_-RNBn9rpoNq9pXx47_jCYiIn4dK103mWp2kj6L414UpnrMqYG6MM43wO5Y3crt28FR153Ne0G0ahjUbw5riG_-jGLAD7G3r05I4hMuGYejrCdhCIP06QoPdMoHXMGGx2crI_IGhDwUZSE1pdJdRPdlLTaKsUgNnbKJi2l1uGhf0qY_lukDMlspzmHOoJOSyj333FABpTs5oUb8W3BQPgqVJrDpXM9Nn8ejZSrOkXkLzJJ5iwDNe0wynYvY6RK5VUiFZ9vG3UFx__h9kHGxB306vdBVLHhthr_6yIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: کشورهای خلیج فارس باید از خود بپرسند مدارا با رژیم ایران در سال‌های گذشته چه دستاوردی داشته است؛ در حالی که آمریکا ایران را هدف قرار می‌داد، ایران نیز کشورهای خلیج فارس را بمباران می‌کرد و
مدارا با این رژیم کارساز نیست.
او خطاب به نیروهای عادی حامی حکومت گفت اگر حقوقشان قطع یا عقب افتاد، از خود بپرسند فرماندهانشان کشور را به سمت پیروزی می‌برند یا نابودی؛ همان‌طور که
دیوار برلین زمانی فرو ریخت که سربازان تصمیم گرفتند به مردم خود شلیک نکنند.
بسنت گفت تا پایان همین هفته یک مؤسسه مالی بزرگ دیگر به‌دلیل ارتباط با ایران تحریم می‌شود و
هیچ‌کس از تحریم‌های آمریکا در امان نیست
؛ هرکس در انتقال پول نفت ایران و تبدیل آن به منابع مالی برای سرکوب نقش داشته باشد، هدف قرار خواهد گرفت.
در پاسخ به خبرنگاری که پرسید چرا با وجود توصیف این اقدام به‌عنوان «روز دی» اقتصادی، تحریم‌ها فوراً اعمال نمی‌شوند و یادآور شد که روز دی تهدید به تهاجم نبود و آمریکا نیز جدول زمانی مشخصی به آلمان نداده بود،
بسنت گفت آمریکا به کشورها فرصت می‌دهد رفتار خود را اصلاح کنند و نمی‌خواهد با اقدامات ناگهانی سیستم مالی جهانی را مختل کند؛ اما این مهلت کوتاه است و روند اقدامات بسیار سریع خواهد بود. او تأکید کرد تحریم‌های ثانویه ابزار قدرتمندی هستند و اگر طرف‌ها انتظارات آمریکا را برآورده نکنند، باید انتظار داشته باشند از
سیستم دلار آمریکا
کنار گذاشته شوند. بسنت در پایان گفت:
«ما این را یک شلیک هشدار و شفاف‌سازی انتظارات می‌دانیم؛ اگر افراد نخواهند انتظارات ما را برآورده کنند، باید انتظار داشته باشند که مجبور شوند سیستم دلار را ترک کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21453" target="_blank">📅 21:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرس تی وی : ایران مستقیماً پیشنهاد مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد
ایران از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21452" target="_blank">📅 21:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‎ وزارت امور خارجه اسرائیل: حتی دایناسور هم جلوی دوربین ظاهر شد ولی مشتبا نه
@WarRoom
🦖
🦕</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21451" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9176177aa.mp4?token=orq8J673xe3nIKDAUxhJOn_JIU0ceSgPgORJfoRiJ7jDanXXJdNa9Ob2pIN2ac2ra4lyAOnU5UbAUuU7yLaLJhzjlyc_rHxMnI4NX74oztPWhVGqJ1NHWXa3igSgAsQxlIEqhgO6XY4MPxdwbl9Fz-NsQkrT2fr3VL1h_Q7WPsMPMNRRnGwWHpQT3enQ-E85JBX3BwrPCEXEjJRIfnizXRfMMPkwilvTaIaJi5aF9kozKrMt1J4MIS-mUAwTuSx2KZg2E8KWCVaTUirchJdyet91diW0KX92HW1Fly6E1AXE0GvDa-m2RN_diTRtmSa7GLBB3ewCdePKR0w3wTcHEFGYHHk2VnZWs5vvXlj7CihPmL8B_fUSwZwS5Mv21hC1gMAd4iFxWTEjArAaOEBt5PySzoZlRuiQyY_a2QYAqli8LzTrNp_gtXOKUvIXzQPQvl7PfL82ycZq3BGuATTsCAKgfOYBfJFSxt6apbJmqA5uU6wDwONJCQBUPZ_flCx0PzG7ZwIIlurEZ7--Jv1TU20J_soRdTw5OWu2zObu9VH_DAhtOkM-YWIRZNGL6bGrC1MaKlsEzslb4VgoCP0wgyg_v3j4ERI-MTYLRhM7F4sU8FoBvjpHVDQm6Ht01xCdbtdamsXnxIsu_vha9db4pMCzRkgtbOU36lnjvVC9ekc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9176177aa.mp4?token=orq8J673xe3nIKDAUxhJOn_JIU0ceSgPgORJfoRiJ7jDanXXJdNa9Ob2pIN2ac2ra4lyAOnU5UbAUuU7yLaLJhzjlyc_rHxMnI4NX74oztPWhVGqJ1NHWXa3igSgAsQxlIEqhgO6XY4MPxdwbl9Fz-NsQkrT2fr3VL1h_Q7WPsMPMNRRnGwWHpQT3enQ-E85JBX3BwrPCEXEjJRIfnizXRfMMPkwilvTaIaJi5aF9kozKrMt1J4MIS-mUAwTuSx2KZg2E8KWCVaTUirchJdyet91diW0KX92HW1Fly6E1AXE0GvDa-m2RN_diTRtmSa7GLBB3ewCdePKR0w3wTcHEFGYHHk2VnZWs5vvXlj7CihPmL8B_fUSwZwS5Mv21hC1gMAd4iFxWTEjArAaOEBt5PySzoZlRuiQyY_a2QYAqli8LzTrNp_gtXOKUvIXzQPQvl7PfL82ycZq3BGuATTsCAKgfOYBfJFSxt6apbJmqA5uU6wDwONJCQBUPZ_flCx0PzG7ZwIIlurEZ7--Jv1TU20J_soRdTw5OWu2zObu9VH_DAhtOkM-YWIRZNGL6bGrC1MaKlsEzslb4VgoCP0wgyg_v3j4ERI-MTYLRhM7F4sU8FoBvjpHVDQm6Ht01xCdbtdamsXnxIsu_vha9db4pMCzRkgtbOU36lnjvVC9ekc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : مؤسساتی که انجام معاملات برای ایران را تسهیل می‌کنند. صحبت‌های زیادی درباره هدف قرار گرفتن بانک‌های چینی مطرح شده، اما ما در اینجا هیچ‌کدام از این مؤسسات را هدف قرارگرفته نمی‌بینیم. آیا قرار است چنین اقدامی در ادامه این کارزار انجام شود، یا آتش‌بس تجاری بسیار حساس با چین ممکن است مانع از این شود که تا این حد پیش بروید و چنین گام بسیار بزرگی بردارید؟
بسنت :
ما می‌خواهیم امروز در اینجا کاملاً روشن کنیم که هیچ‌کس از دسترس تحریم‌های آمریکا خارج نیست. اگر مؤسسه‌ای انجام معاملات را تسهیل کند و بخشی از آن اکوسیستمی باشد که نفت ایران را به پول و در نهایت به سرکوب تبدیل می‌کند، آن مؤسسه نیز هدف تحریم قرار خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21450" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال 13 عبری: ایران به کشور های خلیج فارس هشدار داد که پایگاه‌ها و تجهیزات آمریکایی را تخلیه کنید، در غیر این صورت ما به خاک شما حمله خواهیم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21449" target="_blank">📅 20:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529f1c3c67.mp4?token=QSG0TYjJH_MdXcmmzsQL-zbjIqmqrm6nk9kMtZvtHtiemmGzT-bxcxl3-8CX5mM1-H7pw7phrkbebrZOezUV6ixJMmyk8eBWCIPopQD4cZ6LJo1nBAxKikPSGPKe0Igjv-Ibh5QYwLqqtOK-54E4P29FUMM_I2exCKOIVH1h5iMmHpXsiBRiajpP4Vs4NfLgheaxO3FsXRQeA4AUgiOX4PIKLSmHO2jcb61sKQoeM8bWXGhp5K8i9mEaKsBvDidEsz9XLDerEDBq3RLvMKxHLAsBDgVt-CYu1snbjLOG4x0F_gCyH90pRk56cmPa86zA_j-C6eQStvF-eic-X5MVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529f1c3c67.mp4?token=QSG0TYjJH_MdXcmmzsQL-zbjIqmqrm6nk9kMtZvtHtiemmGzT-bxcxl3-8CX5mM1-H7pw7phrkbebrZOezUV6ixJMmyk8eBWCIPopQD4cZ6LJo1nBAxKikPSGPKe0Igjv-Ibh5QYwLqqtOK-54E4P29FUMM_I2exCKOIVH1h5iMmHpXsiBRiajpP4Vs4NfLgheaxO3FsXRQeA4AUgiOX4PIKLSmHO2jcb61sKQoeM8bWXGhp5K8i9mEaKsBvDidEsz9XLDerEDBq3RLvMKxHLAsBDgVt-CYu1snbjLOG4x0F_gCyH90pRk56cmPa86zA_j-C6eQStvF-eic-X5MVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است. ایران اکنون دو راه دارد:
انزوای کامل جهانی و اقتصادی در حد تأمین نیازهای اولیه، یا بازگشت به مسیر عادی و پیوستن دوباره به اقتصاد جهانی.
وزارت خزانه‌داری تمام شبکه‌ها و واسطه‌هایی را که ایران برای قاچاق نفت و دور زدن تحریم‌ها استفاده می‌کند شناسایی کرده و برای قطع منابع درآمدی حکومت و سپاه وارد عمل می‌شود.
رئیس‌جمهور ترامپ با رهبران کشورهای جهان تماس می‌گیرد و از آنها می‌خواهد تعامل خود با حکومت ایران را متوقف کنند؛ کشورهایی که همکاری کنند از شراکت با آمریکا بهره‌مند می‌شوند و کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
کشورها مهلت مشخصی برای توقف فعالیت‌های موردنظر آمریکا دارند و در صورت عدم اقدام، واشنگتن به‌صورت یک‌جانبه وارد عمل خواهد شد؛
تمام شعب بانک ملت باید تعطیل شوند
و هر نهادی که به پول‌شویی برای ایران کمک کند، از نظام دلار آمریکا حذف خواهد شد. تحریم‌های جدید
دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی
را هدف قرار می‌دهد و بیش از
۶۰ فرد، نهاد و شناور
مرتبط با تأمین فناوری هسته‌ای و موشکی، عملیات سایبری و درآمدهای نفتی ایران نیز تحریم می‌شوند.
هیچ ابهامی در موضع آمریکا وجود ندارد؛ هرگونه تعامل اقتصادی با این حکومت، طرف‌های دخیل را در معرض تمام قدرت آمریکا قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21448" target="_blank">📅 20:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21447" target="_blank">📅 20:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتنياهو
:
ایران تلاش کرده است تا یکی از اعضای خانواده من را ترور کند.
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21446" target="_blank">📅 20:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یاشار تروخدا یه گروه بزن چت کنیم خیلی دلمون گرفته یکم دوست پیدا کنیم</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21445" target="_blank">📅 19:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐁𝐫𝐨𝐧𝐢𝐥</strong></div>
<div class="tg-text">یاشار تروخدا یه گروه بزن چت کنیم خیلی دلمون گرفته یکم دوست پیدا کنیم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21444" target="_blank">📅 19:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXlNOOa5yyYvWuL1hZbxKqOb5UGTIIxnAYaSFaZTmZp2uIUmj503Yt9tqtF25yzGcuWv4ApnEGdJlcKUJsHzOnZc0MjpRk_SmEq7fwL4QwbPa5bZNJaiY_ghrr9Jx9cAn18du5CWVNF1BD-hxwl2qv56Bqyd95eNBkv_Rc0V0zw5Pi80z_RtkkEYXUept21inlojnYyvDkVkZ_H5ol_Cke0TjvIXATjFvYvGW509mb-S3dO6Zc-f05PBf684C8mKxfO1ML74Y38lo3ysxlewTpWlCiwYTt_yHkxpF86GQKV998rbiVAVER-3QhHPub15eu0MLVnvzVfO4pcG2R-Ciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دموکرات‌های چپ افراطی با نظرسنجی‌های جعلی دیوانه‌وار عمل می‌کنند و آنها را با حجمی بی‌سابقه منتشر می‌کنند. به این اقدامات «عملیات تضعیف روحیه» می‌گویند؛ یعنی تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آنها پای صندوق‌های رأی نروند. اما نظرسنجی‌های واقعی فوق‌العاده هستند و روحیه در کشور ما هیچ‌گاه به این اندازه بالا نبوده است.
ما در برابر همه پیروز هستیم، از جمله ایران؛ کشوری که در یک مارپیچ مرگ اقتصادی و نظامی قرار گرفته است
. از توجه شما به این موضوع سپاسگزارم!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21443" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ممباقر : با عاصم پاکستانی درباره مواردی که آمریکا به تعهدات خود، طبق یادداشت تفاهم، عمل نکرده است، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21442" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش فاکس نیوز : کاخ سفید تا ساعاتی دیگر در آستانه اعلام سخت‌ترین تحریم‌های تاریخی آمریکا علیه ایران قرار دارد؛ اسکات بسنت این اقدام را یک «حمله اقتصادی» گسترده برای قطع ارتباطات مالی و تجاری ایران توصیف کرده است. هم‌زمان، ریال ایران به پایین‌ترین سطح تاریخی…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21441" target="_blank">📅 19:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: کانادا سال‌هاست از آمریکا سوءاستفاده کرده است؛ آنها خود را مستحق امتیازات ویژه می‌دانند، در حالی که ما به کانادا نیازی نداریم و این کاناداست که به آمریکا نیاز دارد. دیگر با کانادا در تجارت مانند یک ایالت رفتار نخواهد شد و آنها از جمله بدترین کشورها در جهان برای تعامل و تجارت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21440" target="_blank">📅 18:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش فاکس نیوز : کاخ سفید تا ساعاتی دیگر در آستانه اعلام
سخت‌ترین تحریم‌های تاریخی
آمریکا علیه ایران
قرار دارد؛ اسکات بسنت این اقدام را یک «حمله اقتصادی» گسترده برای قطع ارتباطات مالی و تجاری ایران توصیف کرده است.
هم‌زمان، ریال ایران به پایین‌ترین سطح تاریخی خود سقوط کرده
و فشار تورمی افزایش یافته است.  ایران نیز تهدید کرده کشورهایی را که در اجرای تحریم‌های آمریکا همکاری کنند، تلافی خواهد کرد. در همین شرایط،
عاصم منیر، فرمانده ارتش پاکستان، برای میانجیگری و احیای مذاکرات میان تهران و واشنگتن به ایران رفته
و
وزیر خارجه عمان نیز قرار است برای گفت‌وگو درباره تنش‌ها و وضعیت تنگه هرمز به تهران سفر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21439" target="_blank">📅 17:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رویترز: پیش‌بینی می‌شود صادرات هند به ایران، شامل چای، برنج و برخی داروها، به دلیل تحریم‌های ایالات متحده کاهش یابد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21438" target="_blank">📅 16:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیتکوین برای عبور از مقاومت ۸۰،۰۰۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21437" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJxrYqOBzXQoV4Qjq6ybH6FUXIwGY0oRnfLc3Bpn17SpM4l5oaYqub4R36ilu44XTHzq6UzeZ-wI2aolkMtYR-d2GNjWm7zd8eNkbcI5IAdfA7phecv3J6r8sJD6jS4XUvoUBJ2aqVez5r9f0TXoN9vyTfEv219NEY0PqKN8MEngDYI7f0WTHH223y2b5AhrNuE_zHrPkeNPR-imq6EzfZUXMq0nZoiWBGtk-0sRDzyeLhVmGIFHq9VI8fr-sh0dB8tVXosPexDspPgbNi1WbauEq6ctsUM-1ot7Fd6EGxtDUT1zzJX1Rf3Sd4OTzsqzsQcDhk92V9b-1F_JZiE1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کاملاً فروپاشیده !!!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21436" target="_blank">📅 16:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmzyfMgn5g2tWRSfWEaoSAFUKk33AM-k7egu_QvTN_drxrzZcF22oJ4M-pHoB7q-QbANG6X6qKMm_sHVwzI44As0jovESYAGzCwlEr3zldhCS3G8XSqzka2UtIsdZKvdeebmG7OoV3UBQqD03Be78i729Jm1VWUKeYJa38smmXhgSRuRknyZ4YdRZZgGTrf1aD540ztUhjEroguP3998qO6nerWt5E0jnCtC4NNiy3oCcikpIQLT_u0Alrc6cg1icMDpBe3OcGfcpouLbZOZ8drQ6vOn4uGu8q--GetunwAs7pM3JAVfUDN86tYOwA6viW-R06Y5LKWX2cjlCbOjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتی ایران بالاترین رشد اقتصادی جهان رو داشت روزنامه‌ها با دشمنی و حسودی مدام از «ثروتمندترین کودک دنیا که هیچ دوستی هم نداره ، جز سکش » مینوشتند٬ هزار بار با شاه مصاحبه میکردند که توضیح بده چرا و چطور انقدر رشد کرده مملکت...
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21435" target="_blank">📅 15:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ در تروث :از قول ممباقر ،رئیس مجلس ایران: «ما گرسنه‌ایم، نمی‌توانیم زنده بمانیم»نیوزمکس @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21434" target="_blank">📅 15:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اورشلیم پست : همه نشانه‌ها به پایان رژیم در تهران اشاره دارند و شاهزاده رضا پهلوی فرد مناسبی برای به دست گرفتن مسئولیت آینده ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21433" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4oUyAGRb4baHhaoe-F-SZKwzZ681mT9gth__xzZ--2cNreMjjWxaGi3qPKZCYzn7DnKdnoB8BLNL_0zBkhAO1sLeVw1qcfEM3cvEfkjbhE1-Htj2xgOwhiudltE2dskRUMJlFTDIYCg4HnbsWIUCeGQYHc9DkdWlyJ8WKtz0Fo_iFIpVxik3etYSk4jMO6roGOgwHGkV2Ew6qphofZZrHd9KbosxnwY2OFJDS64JOMCMGnZ4sete4OOdTPf5RrGLyS8bNTAZfw_P-Q2zLFVKPSXWDZkzYWMeJ4bqiOA25hjpx_VofoTShRJTOW5tjqPXrvMRcWgU5ZOsrDiHw18og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه اول روزنامه نیویورک پست امروز:
تنگه ترسیده ، رژیم ایران زیر فشار در حال فروپاشی است، زیرا ایالات متحده حلقه محاصره را تنگ‌تر می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21432" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ارتش اسرائیل، دو تروریست از سازمان تروریستی حماس را که در حمله 7 اکتبر وارد خاک اسرائیل شده بودند، به هلاکت رساند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21431" target="_blank">📅 14:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21430" target="_blank">📅 14:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcW6nX1q4njg1WfGc445CKM9tKPiKOXoty_5_cHwxH7rl6FeUND-I98-0h54ckv_QtgYlkBYC3FOyk2eLfoJPxsB7ri2SPXUAnmhu0HGsEslj8qpM09Cekd4cF_h9trH3MwUImvhY2a0YSYAmZtG-HnhMv9whFtcxQkr6B9fkFKDzb9n5GbSXRgObtja7kSIB7P6bNQncWolUQhX8-DsZqhm9Wq2jrUkaTfAQTbr3vDnqv17zlDGMOfFYzH0eIIWZJbQWYw14BA9a4yLswSHNICddvIwCq4x-EB6UxSavLwyYOVKv1bkWAjThCLp3Vrrx1CIeCVEV94x5fWIsijpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب افکن مخوف B1-B از پایگاه فیرفورد انگلستان بلند شده و در حال تمرین است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21429" target="_blank">📅 13:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR_rAW0YqtX7MUTfQyRr5l-qn-98Rwz5Nn6fGkZlk7-GTPPYPcX9op_pN2-mCsHbgk17GfT5YnUg1FEByoHRajCwz8eXLRv3v_oknwTLYQUOl4mwt_nHBjKiQQzm9n2ajcPrT1NLoIvnp8QVOatIs15-XPuCjmE6w0uREIGthBMnua9jzTEd4LsQXm3dboQLSgSW0KfBRyJ92y_b2cBRCCNOhQiSNtXDk7t4PnTNmWfKJ9Af_29r1XuvTGrBG0N208LBsr7U-rtOH8aFawqOtwCOkSLf1_9FA3oh37HJujAd68yf0-rqKEd5F6h_7VH1yxqw62WHf5gYqAMpuZe0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند
E-11A BACN
نیروی هوایی آمریکا پس از چند هفته غیبت دوباره بر فراز عراق مشاهده شده است. این هواپیما یک
گره ارتباطی پرنده
است که شبکه‌ها و سامانه‌های ارتباطی مختلف نیروهای هوایی و زمینی را به هم متصل کرده و امکان تبادل صوت، تصویر و داده را حتی فراتر از خط دید فراهم می‌کند؛ در نتیجه جنگنده‌ها، پهپادها، نیروهای زمینی و مراکز فرماندهی می‌توانند اطلاعات میدان نبرد را سریع‌تر و هماهنگ‌تر به اشتراک بگذارند. بازگشت E-11A به آسمان عراق از نظر نظامی قابل توجه است، زیرا حضور آن می‌تواند به حفظ ارتباطات و شبکه فرماندهی در عملیات‌های گسترده کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21428" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک حمله مسلحانه توسط عناصر در شهر زاهدان، واقع در جنوب شرقی ایران؛ بر اساس گزارش‌های اولیه، یک مأمور کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21427" target="_blank">📅 12:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21426">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)  دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)  بیتکوین ۷۷،۳۷۹ $ انس جهانی طلا ۴.۶۳۶ $ نفت برنت ۹۱.۰۲$ @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21426" target="_blank">📅 12:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSi6W6WhQLbabwyEpU2pjZ-gMXDVJrRpdvmbsrFAMfgVOn71B6i61_tOgkAvFQtnF10A4hEUn1trW02tLSC2p82__fIx60vR8IzfKRQ9AhSeZWniCjAzf3zuTPbBHwMIcz2jpVtvXaxAldRAXmw4cDMFjB2wWZ3bgAjyGSDKfxwiz93h2OI8R7KV80fmCd9Dpjf8ysPXLgzUhK_jjVGHeBZRGOTiMwUlT7Kimtxm7mNZAuR7UhLbKmcw_yCzIIdOukZSV6k_fX6zGIw_l94WhzraggUO5g3sdkCVJnWwyn0bWk4VogyZpdMa4Eo5ESXQg3K38z2jHK-BlaWkMVnE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hy3Q7nciRPMZvluAFKSq1IOe5vv8Qzdzrztu9Cyis6cp-6WbUr7ZdRAd0LcnuC1MpEimoVVD1b6EPP8Bt7mB15mrjR3DAFBDo1k4vs3Y_GghRvrV41IbKjqFW57ligJ93u4Ug04LujSasRWv6290Ot_RmmJM9f7fdRxii853z9Qcal03ayNI4gIslwwRzszT76e3ePYU1-Q4Fv-9e9vWD3HT9dmiprLwE0-OlX98umUOhV3MmwgnBtZIrbInVMKX7KyRfSVDkW9tW6FnpAdrj5_bZcdiu_7qbNFd8rcYZdisffYJI-i-Xt7RDUKqdWiLQMMNeC9yMFmW3vWgPVJf9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش انفجار شدید در ارومیه ، شدت انفجار در خانه را پرتاب کرده
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21424" target="_blank">📅 12:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزیره به نقل از رویترز: فرمانده ارتش پاکستان پیش از سفرش به تهران، با ترامپ تماس تلفنی برقرار کرده بود
@WarRoom
خبر رویترز که سفر کنسل
شده
فیک نیوزه ، خودتون اینترنت دارین چک کنید قبلش نفرستید برام</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21423" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نرخ دلار ۲۰۲،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر ۲۰۱،۵۰۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۱۲۴ $
انس جهانی طلا ۴،۶۳۰ $
نفت برنت ۹۱.۴۲$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21421" target="_blank">📅 12:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTtYkSoUcnRkeg_NriVjTZfGmLPh7QqNlEPRerBZnc0XUHMvQb523C_K-9pjvRX0d67n_PBGuuAW6ecQBSHGG9TovGte_ktiuenEk8q21IEzwLvKOtygLMFMgNCyDD2NUOAp5EXzPAqG67G0ZtBpXUYRoHX97dGHIVjVcy6ozwiN81tiVcq72WxRg__tnGBxhLWXzthbBcYoJ3MCpbZ4ukc3TSEPuyoKi3586U6BclzuPDc4ZnvvmeFc0LZeI9IE4tDN2893exmqQDmy9_9Zcxvp99_7JJ2MxqGpAT-eAVND5GLNeQDo-5W2FDRsgBU_kbGUhgNB4XUmhn2_mLPQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر به تهران رسید
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21420" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut9e27dy-5-HTvoWQVlYx9loNek4WZpXz6aRUJ-83-iJgwWr0DNShN7j3KMklwc2H314QC8qwKEx_Ah_tQLXWIwkuey_MlyKeqOKZW0JRfskSO7PTeYjDbsi21NFs16LcqMzcA6nHv8nAh7tAr0m4p8_qHkjT51LWk9SZ3GC2Hd6O19Th6TZFmuoCNZQg8Vfd5xsfzbE7vAuB0O6odH3L5PXx0R9GWnWn7-RsJXlTY_pKQcsDdgwX-qHw6OT5MKYY7olWbJ0KQyGpn6U2FwsbUYmhqAcHljunyeSvCNKXcCzRtBjSEnG5BhQ24TVZ0B6ShxUzjcx5oadW5vkFkThpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی : ما از قدیم شطرنج باز بودیم، در سالای اخیر پوکر باز هم شدیم، الان هم مدتیه که ترکیبی بازی می‌ کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21419" target="_blank">📅 11:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOV0Os-h2gnBwlUCBvYzrWivpkGIU4TNKVHIRLC5ItiajPTsSMaFGJeLAxw0lkeVEw9OkrDpxKqGlIDKHhKZJ4eBU0WXSD1e2hLjQPKjgjsA1w7gTpRMGsgsNX3I--NOV3mGXCorlJKVRd1oKQfHr61RYrO4ktBkAJck_bnobRGOSp-u-l893juNKjy_XDnCciR53-82Q0_v2uC0is3fJk70lakA-MqESbwB1amov5xxY616zxOJEmX7XxN0rcJ0kHeRUsfaG6l5X_DfoOR3Deso0JxGKnvGC-jF5PNawEbxX3Tu4tfcFrbLsEQvSWyHNTrLXSOYCg7yoGb820KcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا: گزارشی از حادثه‌ای در ۶۳ مایل دریایی غرب ینبع، عربستان سعودی دریافت کرده است.
مسئول امنیتی شرکت گزارش داد که یک تانکر توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته و باعث آتش‌سوزی در عرشه اصلی کشتی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21418" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۳۷۹ $
انس جهانی طلا ۴.۶۳۶ $
نفت برنت ۹۱.۰۲$
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21417" target="_blank">📅 11:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amolpSGMVRY0rXzZCfQNHRxmG-vL3AAAi0saciO9vPPNhpg0jsTImwc0ynrPIHdYNGL9rQUBNnSb6MrDK6Qig1Wfp1DcxEKyi2zacFUkDjF_J_67PD0I3-7T8Se50wiR4QxGQJoqlGlnAqQ93i48fy159bm16P4qPj4CmhEAAD8Vk_UJigvQ6DeoXtFvutXt3lYNFjVkWKKtGe_Gnlx-HKEDvhuezfyaVaZxEvoq35bXkSyoVC5NuejauydjFLhk1qpxhza6us8DgGTxX0ekujyPDewKGtr_azle9vfcb-CQPHPTkaU7p9uFdVCvXmnJtxQc764oCYABAsY9pYvdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21416" target="_blank">📅 09:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فایننشال تایمز: اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشنگتن وارد «مرحله پایانی» علیه ایران شده
و در حال آماده‌سازی گسترده‌ترین تحریم‌ها برای قطع باقی‌مانده ارتباطات مالی و تجاری تهران است. او هشدار داد کشورها و شرکت‌هایی که به حمایت اقتصادی از ایران ادامه دهند نیز ممکن است هدف تحریم‌های آمریکا قرار گیرند؛ اقدامی که هدف آن انزوای کامل اقتصادی و تشدید فشار بر جمهوری اسلامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21415" target="_blank">📅 09:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=ND_3l3tNj47fcgGiqPe6wiHYOTTFZFcGqt-4JevaVqPWw_ehtralMVqw1QXppqcI_hSLruUy2S3NwtuIcUwvGoXm5rXQadCRt4BEhpRDkadkJrzhJUrMxA9n0GjvQdnvfj7owMgKLHSFtvYo9smzL7EnACBZpNQdRY0o_5LHMawqFGPHm8hk1VyAUoL1TtK20GU_XgL6o6gJZUrZ-i3TXkq1O_4DAKCV3HZYNBea-xsYCAE8CQ6u7OLjlXeC_vWJeK43YDRE2Owvu4vo1E75YzVDUUnntJzSRQ7ZxWgo62ZFaYQc_1zWx-ECirN2l839ERYlqlbAIjBGb7wneKXRqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=ND_3l3tNj47fcgGiqPe6wiHYOTTFZFcGqt-4JevaVqPWw_ehtralMVqw1QXppqcI_hSLruUy2S3NwtuIcUwvGoXm5rXQadCRt4BEhpRDkadkJrzhJUrMxA9n0GjvQdnvfj7owMgKLHSFtvYo9smzL7EnACBZpNQdRY0o_5LHMawqFGPHm8hk1VyAUoL1TtK20GU_XgL6o6gJZUrZ-i3TXkq1O_4DAKCV3HZYNBea-xsYCAE8CQ6u7OLjlXeC_vWJeK43YDRE2Owvu4vo1E75YzVDUUnntJzSRQ7ZxWgo62ZFaYQc_1zWx-ECirN2l839ERYlqlbAIjBGb7wneKXRqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند. @WarRoom یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21414" target="_blank">📅 09:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coAM0Qq6mcYpgpkZJiJOZDxVjtosuvzcnGGPDpbVOqUgpUJP-we8hY_uUr1UwrGrw2CN_SlY5fZIUnjKB1WcoYFtpeMS8dyBSx0E_KCcl-1Ir_LzQhlznM8c5qzV4ppSh7n7TxYYYrS9xJ6hUlw7cCqOzd9vUiyek2hSigVjssFWXlK_RI9Nwuy8a3H8gwJ1fYUJDl9nh_otf9fb1T6cAXLF7Uj4vmP9NKYoEovmmBRm2qEnZplD7JJE50z0L21BbRtRoMSUc3S1YGexwwVPJznlAQyIBq8fyVzyC_51zRLDGHhmpi3VAoLc9gO-qGzGJhdMM1WSSEsfdnu5babAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :از قول ممباقر ،رئیس مجلس ایران: «ما گرسنه‌ایم، نمی‌توانیم زنده بمانیم»نیوزمکس
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21413" target="_blank">📅 09:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=HcNTMPVPRVlbbZgue57rI2cNAopYhfS11VmZ8a-Rgp2lnfKb3_mBacB63X54nxiPG5fCfZK5-GWf-ruS2FJILOmuBhgPPv9JZExRLOcfd-GILpoL_Qt6ccEc5AJczxUJwl3X95S3KoA2kSj_OB06nBM5A352fhhmlkuBn6QVqANGG5R2stI3TTtAu1CG1miLOf2bDofcJKHBGBBUfW6yhahG9Oou6vRM_XTGMu1rJk50ys3U2Ud8lL1ddWfMdbSGUQSoII9-ribFLs4M-9XdLS9K6wjtpk9mYSTevxKXP9_hm1miVUpoWmaQ377Tkmbt-pszrFoBAO6k7s2PMslzww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=HcNTMPVPRVlbbZgue57rI2cNAopYhfS11VmZ8a-Rgp2lnfKb3_mBacB63X54nxiPG5fCfZK5-GWf-ruS2FJILOmuBhgPPv9JZExRLOcfd-GILpoL_Qt6ccEc5AJczxUJwl3X95S3KoA2kSj_OB06nBM5A352fhhmlkuBn6QVqANGG5R2stI3TTtAu1CG1miLOf2bDofcJKHBGBBUfW6yhahG9Oou6vRM_XTGMu1rJk50ys3U2Ud8lL1ddWfMdbSGUQSoII9-ribFLs4M-9XdLS9K6wjtpk9mYSTevxKXP9_hm1miVUpoWmaQ377Tkmbt-pszrFoBAO6k7s2PMslzww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران به سلاح هسته‌ای دست پیدا می‌کرد، فکر می‌کنم تمام خاورمیانه از بین می‌رفت و قطعاً اسرائیل نابود می‌شد. آنها به من می‌گویند اگر دونالد ترامپ رئیس‌جمهور نبود، دیگر اسرائیلی وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21412" target="_blank">📅 08:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روزنامه یونانی کاتیمرینی گزارش داده که آتن پس از تهدیدهای تهران علیه پایگاه‌های آمریکا در اروپا یک سامانه پدافند هوایی Patriot را از کارپاتوس به جزیره کرت منتقل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21411" target="_blank">📅 08:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏نیویورک پست با استناد به تصاویر ماهواره‌ای نوشت: فعالیت در قطب صادرات نفت ایران در جزیره خارک تقریبا صفر است.
‏داده‌های کشتیرانی نشان داد که روزهای شنبه و یکشنبه ۱۷ کشتی از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21410" target="_blank">📅 08:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏خبرگزاری مهر: آتش‌سوزی گسترده در چندین سوله یک کارخانه تولید چسب و عایق در فرون‌آباد پاکدشت، بامداد دوشنبه به وقوع پیوست و به‌دلیل وجود مواد قابل اشتعال، عملیات مهار حریق با دشواری همراه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21409" target="_blank">📅 08:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش های‌ زیاد از صدای انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21408" target="_blank">📅 23:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مایک پنس: ترامپ و اسرائیل دوباره برای «تمام کردن کار» وارد عمل می‌شوند
به گزارش سی‌ان‌ان : مایک پنس، معاون سابق رئیس‌جمهور آمریکا مدعی است:
«بسیار زود و پیش از آنکه دیر شود زمانش فرا می‌رسد که رئیس‌جمهور و متحد ما اسرائیل مجبور شوند وارد شوند و کار را تمام کنند.»
آمریکا باید نیروها و تجهیزات نظامی خود را در منطقه حفظ کند تا برای اقدام احتمالی آینده آماده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21407" target="_blank">📅 23:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اناق جنگ با یاشار : این خلاصه از بهترین ویدیوها از ساعتی پیش که مسابقه شروع شد تا همین دقایقی پیش درست کردم که هیچ جا پیدا نمیکنید.
گرندپری «Freedom 250» در قلب واشنگتن و در مسیر اطراف نشنال مال برگزار می‌شود؛ مسابقه‌ای ۲۵۰ مایلی که نماد ۲۵۰ سالگی استقلال آمریکاست. ترامپ که با فرمان اجرایی زمینه برگزاری آن را فراهم کرد، پیش از آغاز مسابقه با خودرو ریاست‌جمهوری یک دور نمادین زد و پرچم سبز شروع را به اهتزاز درآورد. هم‌زمان، نمایش هوایی گسترده‌ای با حضور بمب‌افکن‌های راهبردی B-2، B-1B و B-52 برگزار شد تا قدرت نظامی آمریکا نیز بخشی از این نمایش ملی و میهن‌پرستانه باشد. هم اکنون ترامپ از جایگاه ویژه در حال مشاهده مسابقه می باشد. البته بیشتر در حال صحبت کردن با اطرافیان است تا این لحظه…
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21406" target="_blank">📅 22:53 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
