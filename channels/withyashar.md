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
<img src="https://cdn4.telesco.pe/file/BHz2rOn3dNwbhVZO33DX8ri94Fc-n1txl5Va6dOPTB_LGCTp2BMYGuglrR9_R370npXe0YoPVhJ3h7S-Q-ILsymc42LD_o34x6f4HDh4lJkIS2QkS2PWHMvBfshOXvutBiicdb29TVJl87-QR9-11umtpov5LzcZJpfIb-Xp1c7PtXgOVSueLg8qihBlmDDGKEmQaJ0mR970RXyuAAfS9ho7p8b78vN9IJPmNSygaRTDOqH50RhuQbXRGJ8Z7YaqIVg9cyAqFKuj3r6Vc0oxVIijg0G-3_-1Yw0HRpL3UzSUHp6_lF8yzoN4Eha3CaYStRCCrG2-ZN7yVGI3b-elwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 306K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-14096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولچه وله : حزب دمکرات کردستان ایران کمی پیش  امروز سشنبه در شبکه ایکس خبر داد یکی از کمپ‌های این حزب بار دیگر هدف حمله پهپادی جمهوری اسلامی قرار گرفت.
بر اساس این گزارش در این حمله دو فروند پهپاد به سمت "کمپ آزادی" شلیک شده‌اند.
کمپ آزادی محل اسکان خانواده‌های اعضای حزب دمکرات است و از آغاز درگیری‌های اخیر تا کنون بارها هدف حملات جمهوری اسلامی قرار گرفت. این حزب تا کنون گزارشی درباره تلفات جانی یا زخمی‌ها ارائه نکرده است.
بر اساس این گزارش، جمهوری اسلامی ایران از زمان آغاز درگیری‌ها با آمریکا و اسرائیل تا کنون با شلیک بیش از ۱۳۴ فروند موشک و پهپاد، کمپ‌های حزب دمکرات کردستان ایران و همچنین مراکز درمانی و آموزشی این حزب را هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/withyashar/14096" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز همین الان
@withyashar</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/withyashar/14095" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ان‌بی‌سی نیوز : وقتی رئیس جمهور ترامپ در بازی سوم فینال NBA هنگام پخش سرود ملی روی جایگاه تماشاگران در مدیسون اسکوئر گاردن ظاهر شد، توسط جمعیت (BOOE) هو شد.
@withyashar</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/withyashar/14094" target="_blank">📅 09:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14093">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پنتاگون شرکت‌های BYD، Alibaba و Baidu را به فهرست شرکت‌های متهم به همکاری با ارتش چین اضافه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/withyashar/14093" target="_blank">📅 09:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14092">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
هنوز مشخص نیست که آیا این بالگرد توسط آتش‌ ایران سرنگون شده یا دچار نقص فنی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/withyashar/14092" target="_blank">📅 09:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14091">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره لیندزی گراهام:
او برجسته است. مدت‌ها در کنار من بوده است.
ما ابتدا مدت‌ها پیش بر سر موضوع کاندیداتوری با هم مبارزه کردیم. او کاندیدا بود و من هم کاندیدا بودم، و ما مبارزه کردیم، و من شروع کردم به این که بفهمم او فردی بسیار بااستعداد است.
بعد از آن مبارزه، ما بهترین دوستان شدیم و او به من به اندازه هر کسی در سنا کمک کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/14091" target="_blank">📅 02:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14090">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهم کردم!
رئیس جمهور ایالات متحده: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/14090" target="_blank">📅 01:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14089">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کن کلیپنشتاین، روزنامه‌نگار آمریکایی، مدعی شده اسناد محرمانه‌ای را دیده که نشان می‌دهد بخشی از نیروهای لشکر ۸۲ هوابرد آمریکا در آوریل ۲۰۲۶ به‌طور مخفیانه به اسرائیل اعزام شده‌اند. به ادعای او، این نیروها در چارچوب برنامه‌ریزی مشترک آمریکا و اسرائیل برای سناریوهایی از جمله تصرف جزیره خارگ ایران و ایجاد یک منطقه ساحلی در داخل خاک ایران آماده شده بودند. این ادعا تاکنون از سوی پنتاگون یا دولت آمریکا به‌صورت رسمی تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14089" target="_blank">📅 01:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به اسکای نیوز:
من فکر نمی کنم اسرائیل به جنگ با ایران بازگردد. همه چیز خیلی خوب پیش می رود.
ایران کاری را که باید انجام دهد انجام می دهد. من فکر نمی کنم این اتفاق بیفتد، اوکی؟
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14088" target="_blank">📅 01:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلزله شدید بندرعباس الان @withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/14087" target="_blank">📅 01:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک منبع جمهوری اسلامی به الجزیره: آمریکا تغییرات غیرقابل قبولی در پیش‌نویس یادداشت تفاهم ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/14086" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جنگنده غرب تهران
قشنگ دیده میشد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14085" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">زلزله شدید بندرعباس الان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14084" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14083">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صدا جنگنده در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14083" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14082">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حمله پهپادی حزب‌الله به اسرائیل
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14082" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14081">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش صدای انفجار از‌ دروازه دولت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/14081" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14080">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش از وقوع انفجار مهیب در محدوده گیشا تهران؛ لرزش شدید ساختمان‌ها و شیشه‌ها.
هجوم شهروندان به خیابان‌ها در پی شنیده شدن صدای انفجار و ایجاد رعب و وحشت.
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/14080" target="_blank">📅 00:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک پهپاد از لبنان به شمال اسرائیل نفوذ کرد و آژیرها به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14079" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جروزالم پست :  هشدار نفوذ پهپادها گالیلای علیا و جولان (1 مکان). در حال به‌روزرسانی...
وارد اتاق امن شوید و تا اطلاع ثانوی در آن بمانید
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14078" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArad</strong></div>
<div class="tg-text">گیشا یک صدایی شد پنجره لرزید و مردم چند نفر ریختند بیرون</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14077" target="_blank">📅 00:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمکران</strong></div>
<div class="tg-text">صدای انفجار اومد سیریک ولی دور بود</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14076" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">فکر کنم گیشا رو زدن</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14075" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر دادگستری لبنان: حزب‌الله باید سلاح خود را به دولت لبنان تحویل دهد تا موضع مذاکراتی ما تقویت شود. مذاکره جایگزینی جز گرداب جنگ‌ها و ویرانی ندارد. جنگ به اشغال شدن بخش بزرگی از جنوب لبنان منجر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/14074" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فارس:
جنگنده‌های اسرائیلی
در  عملیات‌های شب گذشته
بدون ورود به آسمان ایران
و از خارج از مرزهای کشور اقدام به شلیک تسلیحات دورایستا کرده‌اند.
این تغییر الگو نشانه‌ای از افزایش ریسک ورود مستقیم جنگنده‌های دشمن به حریم هوایی ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14073" target="_blank">📅 00:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مقام ایرانی به الجزیره: توافق فقط به شرط آزادی دارایی‌های ایران حاصل می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/14072" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک مقام آمریکایی به Axios گفت:
بی بی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14071" target="_blank">📅 23:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">@withyashar
جنگ مخفی</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14070" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سامانه های پدافندی آمریکا در اقلیم کردستان، عراق در حال فعالیت می‌باشند.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/14069" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جنگنده های آمریکایی در شمال عراق به پرواز درآمدند.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/14068" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از رهگیری موشک یا پهپاد های جمهوری اسلامی توسط امریکا همکنون در عراق
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/14067" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واقعا یه خبرایی ‌هست
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14066" target="_blank">📅 23:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14065" target="_blank">📅 23:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/14064" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14063">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/14063" target="_blank">📅 23:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14062" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">برم اتاق جنگ رو پست کنم</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14061" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استان یزد فردا تعطیل شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14060" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: جمهوری اسلامی از ما خواست تا اسرائیل حملاتش به ایران را متوقف کند
@withyashar
جمهوری اسلامی هم میگه آمریکا خواست
🤣</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14059" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14058" target="_blank">📅 21:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14057" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14056">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدا های مشکوک به انفجار‌ همکنون تهران
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14056" target="_blank">📅 21:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14055" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14054" target="_blank">📅 21:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐥𝐢 🇺🇸𝐬𝐡𝐚𝐤𝐮𝐫</strong></div>
<div class="tg-text">درود سرباز شاه پیام که برای رضا پهلوی (شاهزاده ) فرستادی پاک کنین ، دشمن دنبال همین پیام ها هستن ، همه میدونیم ادمین کسی دیگس</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14053" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14052" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from:)</strong></div>
<div class="tg-text">یاشار دادا فکر کنم اون گز اجیلی که از چهارماه پیش برای روبیو  و ونس بردن تازه داره دعا جادوش  عمل میکنه جنس ایرانیه  دووم  نداره دیر کار شروع میشه زودم تموم میشه
اینا تموم شدن. اینم مثل جنگ ۱۲ روزه یه تست بود که بییین اینا چقدر داستان دارن که فهمیدن فقط بوق کرناس هیچی ندارن
✌🏻
دمتم گرم خسته نباشید
❤️</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14051" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کنه، اونو تنها خواهم گذاشت.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14050" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14049" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14048" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14047">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14047" target="_blank">📅 20:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14043">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نفتکش
Marivex
با پرچم کشور پالائو را در حالی که از آب‌های بین‌المللی دریای عمان
به سمت ایران در حرکت بود
، هدف قرار داده است.
پس از آنکه خدمه کشتی از اجرای دستورات نیروهای آمریکایی خودداری کردند، یک فروند جنگنده
F/A-18 سوپر هورنت
مستقر بر روی ناو هواپیمابر
آبراهام لینکلن (CVN-72)
یک مهمات هدایت‌شونده دقیق را به بخش موتورخانه و سامانه هدایت کشتی شلیک کرد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14043" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14042">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حریم هوایی ایران در حال باز‌ شدن است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14042" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14041">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14041" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14040">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند. @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14040" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14039" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14038">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نتانیاهو: ایران و حزب‌الله امروز از هر زمان دیگه‌ای ضعیف‌ترن و اسرائیل از همیشه قوی‌تره، اما کارزار ما علیه اون‌ها هنوز تموم نشده. تو 24 ساعت گذشته، ایران و حزب‌الله سعی کردن قواعد جدیدی به ما تحمیل کنن، اما من این موضوع رو نمی‌پذیرم. همون‌طور که سال‌هاست انجام دادم، روی حق اسرائیل برای پاسخ دادن به این حملات پافشاری می‌کنم.
و اگه ایران دوباره اشتباه کنه و حملاتش رو از سر بگیره، با قدرت بهش پاسخ خواهیم داد، اسرائیل حق دفاع از خودش رو داره و این حق رو حفظ خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14038" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14037">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14037" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14036">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: ایران نمیتونه معادلات رو به ما تحمیل کنه. من این موضع رو تأیید میکنم. پس از اینکه حزب‌الله به اسرائیل شلیک کرد، ما به بیروت حمله کردیم. و پس از اینکه ایران به اسرائیل حمله کرد، ما به مناطق دیگری در ایران حمله کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14036" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14035">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو: در حال حاضر آتش در جبهه ایران محصور است، زیرا پس از اینکه رژیم تروریستی در تهران آماده شد، دیگر به ما حمله نکرد. اگر دوباره به ما حمله کند - با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/14035" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14034">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=htTk-KoXhMogVn2QJ42OYL_DKqKiZWHddKtJnAb9MC4ldEfEFKUTNnZ3-fpNXkF-rlVKiMwbX1e1ccOi62v9m1NzQDBQRdMHDSjnYBcshQKwFzH-U2avkngNvlww2GFHZkYUYcGIuZY6dcHe-tEYhLCF-1JDZZvOKdSWd0fMIFEPQYmA0i3bk0-RJgi5mXuqKTQGqZfxbAnlUYk_NlGANep9GtvfFzyrMojAiv-JqvjiXK3QwxZoUL0ijMjC8eNu56f5iak66Bf_KzV-NXvlsyWntU2Lm6vZTQeGWeiEYzwQy_lpEYrPUhaCcBaCwOjfGS2eWmH1T4lWA7kC0aeWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=htTk-KoXhMogVn2QJ42OYL_DKqKiZWHddKtJnAb9MC4ldEfEFKUTNnZ3-fpNXkF-rlVKiMwbX1e1ccOi62v9m1NzQDBQRdMHDSjnYBcshQKwFzH-U2avkngNvlww2GFHZkYUYcGIuZY6dcHe-tEYhLCF-1JDZZvOKdSWd0fMIFEPQYmA0i3bk0-RJgi5mXuqKTQGqZfxbAnlUYk_NlGANep9GtvfFzyrMojAiv-JqvjiXK3QwxZoUL0ijMjC8eNu56f5iak66Bf_KzV-NXvlsyWntU2Lm6vZTQeGWeiEYzwQy_lpEYrPUhaCcBaCwOjfGS2eWmH1T4lWA7kC0aeWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما این حق را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14034" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14033">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس جدید موساد، رومن گوفمن : مردم ایران را مسلح کنید , بازی را تغییر دهید
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14033" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14032">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسرائیل هیوم: درگیری 24 ساعت اخیر نشان داد قدرت نظامی ایران حتی نزدیک به شرایط قبل از جنگ هم نیست.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14032" target="_blank">📅 18:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قالیباف: معادله آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان رو به هم زدیم. تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14031" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه I24News: اسرائیل به پمپی که مواد را در کارخانه بزرگ پتروشیمی در ایران حمل می‌کند حمله کرد. حمله‌ای به یک قطعه حیاتی (و گران‌قیمت) با هدف از کار انداختن کارخانه‌ها.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14030" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14029">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو دقایقی دیگه صحبت میکنه</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14029" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14028">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14028" target="_blank">📅 16:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14027">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=igIOMuRNDe03QX3N9S4MKCeNRNj0Uy8ySXtNKqVSUTt-dfliyyqMy6cxyUY5xVO_mT9bp09-mSbxKNVhEKDnpa--Kymz4iDQXIfx8-dktpcdPDigWYkI47qYiR18z47ZylvjdiNW3fMIumm34f09pR9YpoeFmZ2i97fGuwce27qfWun-stZEDsMAYU_Qh6LQ4So4rg76VHuJ-XSk9uQ3sE0lKOWKgSdhaxMKqMfL7pLZSxMBQ2rd8_wPkQmfysTV_45augymCGXrx7Pb9iRcqpekQ5_VDc_--tuEdP67saSgXBjWzY-FmmJoTruIzlQSMZ1bFmUnSGYpl9CU-gMneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=igIOMuRNDe03QX3N9S4MKCeNRNj0Uy8ySXtNKqVSUTt-dfliyyqMy6cxyUY5xVO_mT9bp09-mSbxKNVhEKDnpa--Kymz4iDQXIfx8-dktpcdPDigWYkI47qYiR18z47ZylvjdiNW3fMIumm34f09pR9YpoeFmZ2i97fGuwce27qfWun-stZEDsMAYU_Qh6LQ4So4rg76VHuJ-XSk9uQ3sE0lKOWKgSdhaxMKqMfL7pLZSxMBQ2rd8_wPkQmfysTV_45augymCGXrx7Pb9iRcqpekQ5_VDc_--tuEdP67saSgXBjWzY-FmmJoTruIzlQSMZ1bFmUnSGYpl9CU-gMneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر
⚠️
اگه ناراحتی قلبی دارید نبینید
🤣
بی اختیاری ادرار میاره
این ویدئو رو صدا و سیما خودشون پخش کرد!
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی برای تنگه هرکز
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14027" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14026">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بریتانیا هشدار تخلیه به شهروندانش از اسراییل رو صادر کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14026" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14025">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul42qx60FNejrqL0tEIFlNP_ZdEDpryoNp8YUb1JAg-2dnKv3WTp9PnFuvmtZX09pyrplFdu_3HlSrw3GgPGCxbjTUFZZ-mXcGQ-MmCaSWzNg6QcGpoVnuoqGcpcbmd9pKrhXB60l6obp-iB8qpqh-Jds_TTkg0lkvDCGI6u8nAmrq8bBzsUU0Cxykd5X_9RQC-sVZL40xs8GUvRQtthEKlxPznu7b_mapP8w0r-vlJ1Wxgbj9XI2OhTEs7z3FNk1004YXxCXkSElIP95huZc2wHK8LelUWLHTzUNADVFbdjfjSyjIk3KbnKWmIZ0N4VKYuoaAokiOmK2Ud28eLWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هم داره جنوب لبنان رو خیلی شیک و مجلسی هوایی میزنه.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14025" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14024">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14024" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14023">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترافیک سنگین در محورهای چالوس و هراز
@withyashar
خوش بگذره به هم وطنام
❤️‍🩹
جای‌منو خالی کنید</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14023" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14022">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14022" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14021">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyaVb65TYZjwOFPrcRN388gDP-RV511MmMaNa2BIAGzi90jH15_N44bjb5Ezm9B4Zs7yRY7XD8O8YB23niU8lomNHGjl1uRmEeRtx5rpCmb7SwfVfhPpkTHZuubeft2Wg8CiyvGzlwEjSUW9ADowRJGzMizg2Es7g29QP5MIjGCDK3RRa8jKC73W5ZCEMqe2c8dyJG0WdADyNhwwozj0vLEE8D3KadN3cGVn731wKXXveHINdciUd-20bbk9FGFoye8bTINVTML0_2xw6RI-Jpc9N9iIDr4K0YFanXf_1nOJ56V5FlizUyIwoB--gKr0sRI-_h2KaxcyEqIA2y3QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14021" target="_blank">📅 16:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14020">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14020" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14019">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حزب‌الله هم حمله موشکی کرد به سمت اسرائیل و آژیرها فعال شد.
اسرائیل : 5 موشک رهگیری شد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14019" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14018">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
تماس تلفنی ترامپ با نتانیاهو «مودبانه» بوده، اما نتانیاهو با درخواست ترامپ برای توقف اقدامات بیشتر مخالفت کرده.
به نتانیاهو صراحتا گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت نکرد و از آنها حمایت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14018" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14017">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراق از بازگشایی حریم هوایی خود خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14017" target="_blank">📅 15:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال 12 اسرائیل: ترامپ و نتانیاهو دقایقی پیش صحبت کردن.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14016" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هم اکنون اسرائیل به لبنان حملهِ کرد
@withyashar
😁</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14015" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدا و سیما:جنگ پس از شکست دشمن به پایان رسید و زندگی به روال عادی بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14014" target="_blank">📅 15:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تحلیل کمی دیگه در‌اینستاگرام پست میشه</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14013" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14012" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=IPm0uoxgXOlY8jfKtcByZyZS0HSC9cnwPvMloLvu8AySmYpLmTiUHROf-2KDQHObfzwyWJmCl_9wz4TKqOWWa1_g1l4_s3NXEh8Ip1-OpW8ygw9m7qLkoBGl9x02MZxcljVv0ZtRG2Z9MCeWUAxFZUXKQL-EcCPDK1ZK5METDLrYQ8x_hMx8SRpp5Pzsq03mDadqatU3WF-3cQdOjGiiH9V05JnHxDB51_ek3HJGEqTZyPUJp8VKTA8MvYPxwGzBeKcTuziAmYGhji_2sdjelQ99Uq_PJMVytkLOpiaNyFCbquUJlbU7jYadbC7tLAw9Wi4PNJ_Y5Jo6O5HxUulxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=IPm0uoxgXOlY8jfKtcByZyZS0HSC9cnwPvMloLvu8AySmYpLmTiUHROf-2KDQHObfzwyWJmCl_9wz4TKqOWWa1_g1l4_s3NXEh8Ip1-OpW8ygw9m7qLkoBGl9x02MZxcljVv0ZtRG2Z9MCeWUAxFZUXKQL-EcCPDK1ZK5METDLrYQ8x_hMx8SRpp5Pzsq03mDadqatU3WF-3cQdOjGiiH9V05JnHxDB51_ek3HJGEqTZyPUJp8VKTA8MvYPxwGzBeKcTuziAmYGhji_2sdjelQ99Uq_PJMVytkLOpiaNyFCbquUJlbU7jYadbC7tLAw9Wi4PNJ_Y5Jo6O5HxUulxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14011" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود @withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14010" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیهش نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14008" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14007">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=dMbZx8SpN3aHtPLs9mGFYJTN9497HFQ-teo4vmAQ824B2JSxLlhlFYR45u15sTAF1PEkqkg72p2V84E29M3lH3ah_XrnK1PjNoO6x6GOr_c2ej8fqBz-jOu_T65ukMCug4Xmdl0c5QwMAnkkOh6AaQQdS1vMTX1K5rOCFvwMKZPOc1SxXxLCtepbjM1YFmLMy4NxhvoMHhK-IpL0QtBKgKXNg6xma4_IfrqSPZeakdhuD3BG88XKF9jJBYhGHAZK6VP4_aWW4mb_sfwxPANxtHgJg7cyEKwEh6WW8vUUCkfZtm43fCiahGTErOkcgBXnsuvf5UWoEYgc_P9Tv03Qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=dMbZx8SpN3aHtPLs9mGFYJTN9497HFQ-teo4vmAQ824B2JSxLlhlFYR45u15sTAF1PEkqkg72p2V84E29M3lH3ah_XrnK1PjNoO6x6GOr_c2ej8fqBz-jOu_T65ukMCug4Xmdl0c5QwMAnkkOh6AaQQdS1vMTX1K5rOCFvwMKZPOc1SxXxLCtepbjM1YFmLMy4NxhvoMHhK-IpL0QtBKgKXNg6xma4_IfrqSPZeakdhuD3BG88XKF9jJBYhGHAZK6VP4_aWW4mb_sfwxPANxtHgJg7cyEKwEh6WW8vUUCkfZtm43fCiahGTErOkcgBXnsuvf5UWoEYgc_P9Tv03Qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل : ما سیستم‌های پدافند هوایی رژیم تروریستی جمهوری اسلامی در غرب و مرکز ایران را نابود کردیم
‏پس از حمله، انفجارهای ثانویه‌ای شناسایی شد که نشان می‌داد موشک‌ها در پرتابگر بوده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14007" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=W1tDZkXnufSAWrQGwzjQvG1nNAqsrqLXrVgCpry2DaJ181igWP7WESInzAts_j3KnubcwZ0itPdT0MEhQMANxp8Ize54UesfqYuwixccJ-aLIJiVi9n5fy88Qfa9UOBcxPI2jpuyfhiN1cUBQTo681R1vIRI2FbI-THd4P_g5N7PnYTcUTyh9XTaYzv2fyTpX_hNTb5YsQX83nOx4PC3B3-tNnNrVAKSoipE8PUFph1k8HseRrq5w29kSy_5J8h-kurV3E2e3tFGL8CfjIEDTZsvjquYeOwjEy5JCL0hlJQeEDbmahnCEEPgH0qmk8RYWNiX-GkpacTpx5Egj-zJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=W1tDZkXnufSAWrQGwzjQvG1nNAqsrqLXrVgCpry2DaJ181igWP7WESInzAts_j3KnubcwZ0itPdT0MEhQMANxp8Ize54UesfqYuwixccJ-aLIJiVi9n5fy88Qfa9UOBcxPI2jpuyfhiN1cUBQTo681R1vIRI2FbI-THd4P_g5N7PnYTcUTyh9XTaYzv2fyTpX_hNTb5YsQX83nOx4PC3B3-tNnNrVAKSoipE8PUFph1k8HseRrq5w29kSy_5J8h-kurV3E2e3tFGL8CfjIEDTZsvjquYeOwjEy5JCL0hlJQeEDbmahnCEEPgH0qmk8RYWNiX-GkpacTpx5Egj-zJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان کرج سمت میدان استاندارد و فردیس
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14006" target="_blank">📅 14:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد @withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14005" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر آموزش و پرورش اسرائیل: تعطیلی مدارس فردا سه‌شنبه نیز ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14004" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14003">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرنگار I24News خطاب به پست رئیس جمهور ترامپ:
من واقعاً نمی‌دانم این مذاکره درباره چیست
این مذاکرات به مدت یک هفته و نیم به دلیل لجاجت ایرانی‌ها متوقف شده است. پیام‌های ترامپ هر روز خجالت‌آورتر می‌شوند
و تا جایی که می‌دانم، اسرائیل خواستار آتش‌بس فوری نیست
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14003" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj0slkkbwPou-2OLsbPEhdphNRlrxaA9LspbEoCPPp-kzXRPZYYjOWrB9gOkbftGTS2jEhOYfNnjVi2KQsObbhlE4Vuhiy4DQo-NTbT6YqTQdwsehIAAlp2wkXSYTLY0xbz1q360KXniTZrdroO6zWaSO3GCuZ8-uzXLoC-sVdisZyF-mmYmj8gp76AUZ21adsa_7D3wZWSXmTwekMDzPo2Ws8Uw8KPfyDAEDz3fi7L0PnBAbdf44bjSQqt9IZOsm3cv2E2CebU2Cd8Uy6lnWA39Km_GBInF4pPQAgsyfWWKYmL8kC4k_3_-OwCMbDWUOYx_aF3obqTHmrkxIxSnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14001" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDyyaipcbzT4j9daQTb7gLxYSYn8r0pifwfsyY3v2CcmvOVEOOkBO-D9MpKZrb9AVNYXUhvIAcqj8GLBsgmc5IFc2Tb2NltPE1DYhaiFexFLqao5m8WlqLgLxj9QDmKWjIAOupyp9GxE5snbvItVoXXI0PexGPhTWD4Y85bwE5aUosmEg_v4-gRpbukFUnO-U7wPuwRgzkgi8mejwTtkhkqhom0KoKbTym8GRa_ke3W_QyVQY340YmZCM2tbQRo3rIed8Et39aJcig4A5CjXxuJJbrDCgqLh6mqNGItBixoV5wDwdQk3iXFLXIEtb9qcT-YKc_wdb61GdM_4CSdzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود از انفجار در شیراز، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14000" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های رژیم : پدافند یزد فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13999" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=cDswgDFVYHWiQXthZwxlzhoszC8IJzslZtQIz5AbNCqDuUr2immKfnMZZx_1RMolyESsMLY2uWBRk-TM2Ky1WGsH33pFvrvFvF5hb9HMi2CTdFrBDDunBl4kYNKRDM8EfNeoWPRdY15CXbzhpAEai9nEPm5K1yHm5DzgXv6ZqoJURVAMtlW4PHKEhR2ZVSbvyyLEW_3BCRheuRgWnyD4JRMYIi_e3dicaZfmNQBHYrJw2QTd6GBYuSrzovNx0liLpBYQruvxX7qvkzlfAw7GriXBl2FmHA_eSBzGEOvpNUwRM0WTua9Xe0eWisQKwGfQQj2WVjDMrJqNuwO7j5QWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=cDswgDFVYHWiQXthZwxlzhoszC8IJzslZtQIz5AbNCqDuUr2immKfnMZZx_1RMolyESsMLY2uWBRk-TM2Ky1WGsH33pFvrvFvF5hb9HMi2CTdFrBDDunBl4kYNKRDM8EfNeoWPRdY15CXbzhpAEai9nEPm5K1yHm5DzgXv6ZqoJURVAMtlW4PHKEhR2ZVSbvyyLEW_3BCRheuRgWnyD4JRMYIi_e3dicaZfmNQBHYrJw2QTd6GBYuSrzovNx0liLpBYQruvxX7qvkzlfAw7GriXBl2FmHA_eSBzGEOvpNUwRM0WTua9Xe0eWisQKwGfQQj2WVjDMrJqNuwO7j5QWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13998" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلیه
@withyashar
🥴</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13997" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب ساعت 9 به وقت اسرائیل تشکیل جلسه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13996" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سرپرست سرکنسولگری ایران در کربلا: هماهنگی‌های لازم با عراق جهت انتقال حجاج انجام شده است
@withyashar
حجاجی که نیومده بودن باید برن عراق زمینی‌ بیان</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13995" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13994" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034343a08d.mp4?token=ViGelL-OjpqJWKlvqHBG_49sp3C3pcVHu0Ajco9ytVwWgbkegzJaYYISFwzBUy8MPMxzDuIE3x-E8kMY6_dfQl3Gx75QlmLDa0K98YlFo23LKv_Nke_Ei3i1k-Y2nOib8dL3BivEQHumVw1jWEXVRlmShHWYt0MEsCYUYK4whQ_hL1z9j9cz4feeQMA6f_abY5-tZk-5v7Z6pmknlIxcld_aH7m9EGp1ZiTbv2aUqdpskQcoK7t8_LVpSaPC9ABcswYcgaF0QsmDCoyJ1bwUYJs-zmyoqCktZXzKuIhU_I25QswUDqc-Lc2GJzCNSJidXcM5RoZ6X7Q3O3x_lTb2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034343a08d.mp4?token=ViGelL-OjpqJWKlvqHBG_49sp3C3pcVHu0Ajco9ytVwWgbkegzJaYYISFwzBUy8MPMxzDuIE3x-E8kMY6_dfQl3Gx75QlmLDa0K98YlFo23LKv_Nke_Ei3i1k-Y2nOib8dL3BivEQHumVw1jWEXVRlmShHWYt0MEsCYUYK4whQ_hL1z9j9cz4feeQMA6f_abY5-tZk-5v7Z6pmknlIxcld_aH7m9EGp1ZiTbv2aUqdpskQcoK7t8_LVpSaPC9ABcswYcgaF0QsmDCoyJ1bwUYJs-zmyoqCktZXzKuIhU_I25QswUDqc-Lc2GJzCNSJidXcM5RoZ6X7Q3O3x_lTb2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش السیسی محموت احمدی‌نژاد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13993" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
