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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.61M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-658161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYY7hpl5D8Tzq-qTnMDA-_AKZQOEj9MfPBdnOaIhmDHev0bF95Lq3GmLmalsxcdLIANb_uJMbDT7RI6iF-zW7CzUXpvbuV_7XnWX6NCSNYJ9Wz09yokWP2xGAM3vuJEu3Q0eJFBs16fnQuoMehbrU_BLpXkd-_xp_0ABTwZcVFYBLGmzu21r_e-E-VqE18kmVaYX-7TH_EyyeU9zDx6Ywp63ENA8BUg_cQAkt0FymOOky_fvHAuluSZSBo33TN5cE1zRJJjj0j6K-NvrWWjvLEnsrbNbAp86RO-BpMl49KAVXhgMwINGZBmWIoYG_StZRyS0G3ope2jEt-3wIZDwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس:
منافع ایالات متحده و اسرائیل همیشه با یکدیگر همسو نیستند؛ رابطه ترامپ با  نتانیاهو بر سر جنگ ایران تحت فشار قرار گرفته است.
گاهی ما [و اسرائیل] در یک مسیر و هم‌نظر هستی</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/658161" target="_blank">📅 23:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ لحنش را تند کرد؛ به ایران حمله می کنیم/ آنها ما را به عنوان یک احمق بازی می‌دهند
👇
khabarfoori.com/fa/tiny/news-3222119
🔹
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم
👇
khabarfoori.com/fa/tiny/news-3222091
🔹
انتشار آهنگ جدید امیر تتلو از داخل زندان/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3221986
🔹
ستون دود در جنوب تهران
👇
khabarfoori.com/fa/tiny/news-3222124
🔹
حمله موشکی سپاه به 4 هدف مهم آمریکایی در اردن و انهدام آشیانه F35ها
👇
khabarfoori.com/fa/tiny/news-3221871
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/658160" target="_blank">📅 23:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4LZSgO5IX0XojvrKKeywD5GeMa_yo3vbshtsaFEqZW-7-CWON_b6snAKMgMYIuTw_RvQcMiPTWD9gkrUt95529A1oj5dGeYSgYetptKAROtqOjHmr_yEEiXAskfFH-wxQoJa1QnJnmeg8rIZcM2vTe0HVkaD-L1iNVToxagV3pxOUeIXvBo9ELaPxDf_pz_0lzedWRDuOBSVldcERLTERbNeOUtuFUNsVWGZFWeH5BZWwNNWk97JIfXsYfs3NIKDHlVHf4WH-a6PSj9XZnytJAQoa6tveA8iw-ZnCRbXBGZsugY0QNqrO4_YUpbmoGWJyYnIIKs-bdCzhGQMBnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرفوری|گروه های سرود،سپر انسانی به دور زیرساخت ها تشکیل می دهند
!
اجرای همزمان گروه های سرود جان فدای ایران در ۱۲۰ نقطه از زیرساخت های سراسر کشور
✊
به صورت همزمان روز جمعه ساعت ۱۷ در ۳۱ استان
🇮🇷</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/658159" target="_blank">📅 23:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی‌ ونس: نتانیاهو در موضوع ایران کارهایی را اشتباه انجام داد
🔹
جی‌دی‌ونس در پاسخ به این سوال CBS که آیا نتانیاهو در نحوه برخورد با رابطه با آمریکا در موضوع ایران، مرتکب اشتباهاتی شده است یا خیر، او پاسخ داد: «او قطعاً کارهایی را اشتباه انجام داده است.»
ونس از ذکر مثال‌های مشخص خودداری کرد و گفت که بهتر است آن بحث‌ها «خصوصی باقی بمانند». /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/658158" target="_blank">📅 23:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مقامات آگاه: ترامپ به شدت از کاهش ذخایر موشکی آمریکا  خمشگین است
ان‌بی‌سی‌ نیوز:
🔹
به گفته منابع آگاه، سران صنایعی تسلیحاتی آمریکا خود را برای دیدار با دونالد ترامپ، رئیس‌جمهور دولت تروریستی آمریکا در کاخ سفید در روزهای آینده آماده می‌کنند.
🔹
انتظار می‌رود این گفت‌وگو با توجه به نگرانی‌های فزاینده درباره ذخایر موشکی آمریکا باشد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/658157" target="_blank">📅 23:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انسیه خزعلی: توافق با طرف آمریکایی ممکن نیست اما چاره‌ای جز مذاکره نداریم
انسیه خزعلی، معاون شهید رییسی در
#گفتگو
با خبرفوری:
🔹
حقیقتا سلطه‌طلبی آمریکا توافق واقعی را غیرممکن کرده است، با وجود این بدعهدی‌ها، حضور در میز مذاکره برای رساندن صدای ملت ایران و اثبات عهدشکنی دشمن ضروری است
🔹
مذاکره‌کنندگان باید با اقتدار کامل حاضر شوند و آزادسازی دارایی‌های ایران را به عنوان تضمینی عملی و غیرقابل‌چشم‌پوشی مطالبه کنند. توافق‌های مبتنی بر وعده،، «خسارت محض» محسوب می‌شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/658156" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش هزینه‌های درمان علت عدم پرداخت بیمه‌های تکمیلی است
جعفری‌آذر، عضو کمیسیون اجتماعی مجلس:
🔹
مشکل اصلی بیمه‌های تکمیلی بازنشستگان و شاغلین، توقف خدمات یا عدم پرداخت نیست، بلکه افزایش شدید هزینه‌های درمان و محدود بودن سقف تعهدات بیمه‌هاست.
🔹
در حال حاضر بخش قابل توجهی از هزینه‌های درمان همچنان بر عهده بازنشستگان و شاغلین است و این مسئله در دوران سالمندی به یکی از دغدغه‌های اصلی خانواده‌ها تبدیل شده است./جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/658155" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منبع بلندپایه ایرانی به المیادین: اگر ترامپ این بار در محاسبات خود اشتباه کند، قیمت‌های نفت با صدایی بلندتر با جهان سخن خواهند گفت
🔹
ایران آماده اجرای نسخه‌ای جدید از جنگ است و غافلگیری‌هایی در انتظار دشمنان خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/658154" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای نورالدین الدغیر خبرنگار الجزیره در تهران: واسطه قطری تهران را ترک کرد
🔹
به گفته ایران، سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
🔹
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است.
🔹
واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/658153" target="_blank">📅 23:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCHaE_i-DNE4c1GIhGmqlO8xWvcTLwObJ7zDo6_bdKiirOaN0A_APAounXkbsECmahdJoWL-HBEDRCr-sTtTxU4R_3GhSLfqfcDCAeav6kaCKf2c_mmdH6K15l_y9WW6ZXBU6ZNoSa1dQDYMgqvXuF_mL1cB7YbE7NQX3tnW4TB2rca0B2Lj7lcqDxoR6N-bHxwjJCghht4a-NKWr8OwbsDxw3oOo8Z9AsPajjdtZIlw3GB_TyWeOR5Uik3IMzWzuBGOktY3MlSC9LULHeIPMVWsGqomRJFLjOUB-LxZHsHXI735YnqmbmDM2sgClG2zszdA-5xayjVoPiTy19KAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جواد خیابانی پس از ۳۵ سال فعالیت مستمر در سازمان صداوسیما بازنشسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/658152" target="_blank">📅 23:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yowk5AVsJtNvNiwOAykqqt_ixYGUkZild8idNtdy4oDra60pH_HUhcsIBa3X-GpoWDItvQb4X433iiGgjZAfaFI3s8wz-BG2IUKb4s5IX_0eM6orDFSpOg-QpMwzaPNlYKAUQ-JGcdkgK5wYdalEqZ1QIeg5g6Mo4PifN_m-N1_qDXVuHNhdGWWvIySLpCOLbP9wxgu10yUyqsXNXKrZHObFT31-ARFgxRfOkjwbOxueFwDiRTXxJlV92MRjXdpXBRCBBpGmIMjPH_UBwEo9iFTwKKdOTpxc9MbzWpZugjLcrHg4dS5H4ws0i-sU-T6cu8XZ8lI-Yk2eo7JmwVmE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: ما از جنگ با بازنده‌ها نمی‌ترسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/658151" target="_blank">📅 23:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قاضی‌زاده‌ هاشمی: وحدت فقط حول رهبری معنا دارد نه چیز دیگری
امیرحسین قاضی‌زاده هاشمی در
#گفتگو
با خبرفوری:
🔹
هر آدم دیگری نمی‌تواند محور وحدت باشد؛ سابقه ما نشان داده همه مسئولان نیاز به مراقبت دارند، نیاز به کنترل دارند.
🔹
این جمهوری، جمهوری اسلامی ایران است. به بهانه‌های واهی نباید به مفهوم جمهوریت صدمه بزنیم. جمهوریتی که به پا خواسته تا هم اسلامیت را حفظ کند و هم ایران را.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/658150" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
هیچ‌گونه فعالیت پدافندی در قم انجام نشده است
‌
معاون سیاسی امنیتی استاندار قم:
🔹
در ساعات گذشته هیچ‌گونه فعالیت مرتبط با پدافند در استان قم انجام نشده و اخبار منتشرشده در این زمینه صحت ندارد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658149" target="_blank">📅 23:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc724dfe0e.mp4?token=fS9p8QWb_KjuIAKefwW03dfU-jAL3dgpwQNVDanUmbsT2OQi_I9CNwYHmLju9YSMF8oA9kPjx9FXaaa6cP5erD018MN6MpGlVFEOD5bW95yDZ0uX-QD_RZE409Ik_axtrsEK_QxSRTsg7JpHwuDn9Xso72OfNLMsrdvfjNDhlCCZ1yuofp8e5pc-VKt8x86iYj8467P4DhN6-Y1n8V70dA0GRHhSwOfaUt7QhKDbD9_azxfwQpf4PWaOZRR1V44KjH9TCuDOm5wmgtPKhkV8THg-ao7rwbgoNMHtRNfvdH7WJSkU6l94ugOhZfUmGwfVxksJVk9ymFmGnSZVfAYXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc724dfe0e.mp4?token=fS9p8QWb_KjuIAKefwW03dfU-jAL3dgpwQNVDanUmbsT2OQi_I9CNwYHmLju9YSMF8oA9kPjx9FXaaa6cP5erD018MN6MpGlVFEOD5bW95yDZ0uX-QD_RZE409Ik_axtrsEK_QxSRTsg7JpHwuDn9Xso72OfNLMsrdvfjNDhlCCZ1yuofp8e5pc-VKt8x86iYj8467P4DhN6-Y1n8V70dA0GRHhSwOfaUt7QhKDbD9_azxfwQpf4PWaOZRR1V44KjH9TCuDOm5wmgtPKhkV8THg-ao7rwbgoNMHtRNfvdH7WJSkU6l94ugOhZfUmGwfVxksJVk9ymFmGnSZVfAYXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو، رئیس فیفا: قولم برای حضور ایران در جام جهانی؟ اگر مجبورم می‌شدم، با اتوبوس به ایران می‌رفتم و تیم ملی را به جام جهانی می‌آوردم؛ البته که کار آسانی نبود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658148" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhjO096ZcIau3fs1-b5pQzwDG5VOsFsVmmwDUKDzwAWNSaNKmOPDocSYxQRKZwf2MSW4Bs1-pNcOtpdvKWM295V47CSJn2ThZI0BH8PZyBsUIxTDtUhSaoT9PVxpKxyjDJkkckoVV0jJmtoCbTQ_SDDg7OHwF2mLoy3lhn2k99ozf9_0WpGqElJfduuSXn_Vmj-iPNLiFWbxJ46bxBQe-rDhNFgkOLkm4Pvtzo0NkzvvvtG8ChxNJYI4ihvu-8Mu70R4M4ydvrPfWHrJbwXHz5hnqB87s0_ICFKZJxxcB8QuYf00GqKaHh98J3xtpYMRBxnqOag9er1Kub0-Gxidhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم مواد غذایی به ۱۲۹/۸ رسید!
‌
🔹
براساس داده‌های مرکز آمار تورم مواد غذایی در ایران در اردیبهشت ماه به رکورد ۱۲۹.۸ درصدی رسیده و قیمت اقلام خوراکی نسبت به ماه مشابه سال قبل بیش از دو برابر شده.
‌
🔹
در جهان، ونزوئلا با تورم اقلام خوراکی ۵۲۴ درصدی رکورددار است و ایران با تورم ۱۲۹ درصدی دوم است./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/658147" target="_blank">📅 22:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
معاون رئیس جمهور آمریکا: به توافق بسیار نزدیکیم
‌
جی‌دی‌ ونس، معاون رئیس جمهور آمریکا در مصاحبه با شبکه خبری سی‌بی‌اس نیوز:
🔹
ما به دستیابی به توافقی که در درازمدت به برنامه هسته‌ای ایران بپردازد، بسیار نزدیک هستیم.
🔹
هدف سیاست ما اطمینان از این است که ایران در آینده به سلاح هسته‌ای دست نیابد.
🔹
هنوز کارهایی برای انجام دادن وجود دارد اما ما همچنان به پیشرفت در جهت دستیابی به توافق ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658146" target="_blank">📅 22:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای باراک راوید خبرنگار اکسیوس: ممکن است مذاکرات ظرف دو تا سه ساعت آینده دچار فروپاشی شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658145" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
توئیت
یک مقام اماراتی: ابوظبی به دنبال کاهش تنش با ایران است
‌
ادعای مشاور پیشین محمد بن زاید رئیس امارات:
🔹
امارات زمینه کاهش تنش با ایران را پس از آن فراهم می کند که بازدارندگی این کشور کارآمدی خود را نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/658144" target="_blank">📅 22:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فلاحت‌پیشه: ترامپ می‌خواهد ایران را عراق ۱۹۹۱ کند
فلاحت‌پیشه، استاد دانشگاه و نماینده پیشین مجلس در
#گفتگو
با خبرفوری:
🔹
در مورد جنگ، علیرغم ادعای ترامپ مبنی بر مخالفت با حملات اسرائیل، نتانیاهو و ترامپ کاملا با هم هماهنگ عمل می‌کنند.
🔹
در واقع ترامپ تلاش دارد جنگ اسرائیل و آمریکا با ایران با شدت تمامی که در جنگ ۴۰ روزه شکل گرفت، توسط اسرائیل ادامه پیدا کند و آمریکا در میز مذاکره امتیازات لازم را از ایران بگیرد. آنچه که در دستور کار ترامپ و نتانیاهو قرار دارد؛ تبدیل ایران به عراق ۱۹۹۱ میلادی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658143" target="_blank">📅 22:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWCpvJJ0paJ0i92lOOH_tuQIfxFkOVSivm6J-F2zdmtFSHgEO6rEq_2UJnbdFVDOE_Q4OFKCEMCgvyZmyixeD88aQvy5rKjjbTmjgfbJzyinnh6dbyzX7VcGONm5FXeFBy1HVTOqHL0bYdqgjefHd-mSR0JbyZcQdJp-YsSdWk30uXFPIVml0UyhFIjOLEe7YaWLIJRMocPF4Y0pRG-ZNQgIo7wHE-SGvKvVIlFSaTNWJ1aFAcHYtO2x_hV2JUhbydirpHYh9pgurvR6eOCIO0Am2Gl98-luzzAxkJw6YgEejbw0Uo8pGt20vZ6JzhwacI5jGqWKwuqZK3Z2stvjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه در این روزها دچار استرس می‌شید و تمرکزتون ضعیف شده این اینفوگرافی مخصوص شماست
🔹
تکنیک‌های فوری برای آرام کردن ذهن در لحظات بحرانی/ اخباراصفهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/658142" target="_blank">📅 22:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d884dfa50.mp4?token=EacmWKLBhjt1gapj3A_cVMNCMquP7mcPhIymnCPnZjBe7jwj_e0Dl0OyvLtBy7J43o1l3upiG3iCM74VkYv8y1CVPdHx8SlGeT4dnLUqmzHqdvN1WUUQfNDwxmyyXcAa6sbngUbuIQK151zYT2owPwMJdOoCKI_6K_AMiHiUJd3ckkXpzr_pKQYCmJWIy0s-65ZS3u4kIKrW-FxUKKdr9jjW0HUVJL7y6rPNqhBb12WjQZ-qqpOnk_fz3LVcrD3RQwGfjy24mSXDMuM2M9cjwm0iInw2zfEWvW-NaiCPd6OMyg59lAzBZjGrleGkxLKp9b0vCTGpNpGpyuWi_Cse7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d884dfa50.mp4?token=EacmWKLBhjt1gapj3A_cVMNCMquP7mcPhIymnCPnZjBe7jwj_e0Dl0OyvLtBy7J43o1l3upiG3iCM74VkYv8y1CVPdHx8SlGeT4dnLUqmzHqdvN1WUUQfNDwxmyyXcAa6sbngUbuIQK151zYT2owPwMJdOoCKI_6K_AMiHiUJd3ckkXpzr_pKQYCmJWIy0s-65ZS3u4kIKrW-FxUKKdr9jjW0HUVJL7y6rPNqhBb12WjQZ-qqpOnk_fz3LVcrD3RQwGfjy24mSXDMuM2M9cjwm0iInw2zfEWvW-NaiCPd6OMyg59lAzBZjGrleGkxLKp9b0vCTGpNpGpyuWi_Cse7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی: ساعت ۱۹:۴۴ امشب، گزارش حریق گسترده در یک انبار فرش واقع در محدوده خیابان ری به مرکز فرماندهی اعلام شد
🔹
محل آتش‌سوزی، یک فضای حدوداً ۲۰۰۰ متر مربعی است که عمدتاً برای انبار کردن فرش استفاده می‌شود.
🔹
عملیات مهار این حریق با مشارکت ۸ ایستگاه…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/658141" target="_blank">📅 22:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای یک دیپلمات لبنانی: نتانیاهو جنگ لبنان را تا انتخابات اسرائیل ادامه می‌دهد
یک منبع دیپلماتیک لبنانی:
🔹
معادلات میدانی، عامل اصلی کشاندن طرفین به میز مذاکرات واشنگتن بوده است.
🔹
هیچ طرفی نمی‌تواند امتیازی فراتر از آنچه در مذاکرات واشنگتن حاصل شده، ارائه دهد.
🔹
نتانیاهو به دنبال تداوم جنگ در لبنان تا زمان برگزاری انتخابات سراسری در (رژیم) اسرائیل است تا موقعیت سیاسی خود را حفظ کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/658140" target="_blank">📅 22:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نقض چندباره حمله هوایی رژیم صهیونیستی به شرق لبنان
‌
🔹
منابع خبری از حمله هوایی رژیم صهیونیستی به منطقه بقاع غربی در شرق لبنان گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/658139" target="_blank">📅 22:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk1DL4Iw9u8DHhbjQ7xbTxFUxomwTsRwXLAL2RRJNWwGdXlkitMrc9XYJPLDoQnnUIwmYEdNUDLjc5nH7xNuYM6B0X5bfFALQY98rbkagz0bpeYoDN4ThJyoXnf39yVXiwtAR4Rm_H5Hb-Lqxl7a1FZg5sywgeKJP15zBR2by5hl3BnwH_E_sYmok0kIe87purhS6MB5dTKe6SesS53O4bzXrsuPxfNi42eARVBUEfEH_9OpSfgYTCzGbxInou9UUeUfdW-rRezDIETFKXkAowaWQB2Cx8f3KaAOiduyIzRDee2j90fvmcJn6vmxOLg6ZAU6aT-Srisld5IY7FJU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی آمریکا و حضور رژیم اسرائیل در فهرست پرهزینه‌ترین برنامه‌های اتمی جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/658138" target="_blank">📅 22:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGNZpRj7EfPYGzAXtQzm6Mk6JtFf6h2mx7jpkiUoHv8kFfKMX89Ul8nIdpEqHhlpV_nX5xF3giWrpage2ypJf-sx2o9qSTcBTKguC3j7OGH2mU958sLAvJ1ZF8nT8sojuoErdhA5fcqF42k4WCrPynTnExUxEr_B8NocN9ZbcWWGoBjUo2FNrNmuH5zTAciALsnDsEXyGTR-ToggSG7vgrl4h5FKJrs7S5mk-WZ5zZnk_yJ3wwkBNOqctQ8HBoNak7n2djeqk2Rbj5AVcXBQ6fKDtcimMIhHhqcJCIFYKzWVaq3RCxdN2_OPWumxW_IQxPiG-YRUbZkzJU32_VA6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سابق CIA: آمریکا و اسرائیل به دنبال «خرابکاری» در مذاکرات با ایران هستند. احتمالاً شاهد درگیری‌های جدیدی خواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658137" target="_blank">📅 22:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتاپ تورز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0SEBFAF1SrugQslolDlwURs6dQ02LA64XqXFQ8zy71n4CuWEqfn1_xDtO7kFS4V7K-8K5M8qRbQOy_fKnKbTqX871p-PgSKqu9pus3vrsJeVBviK5h3cfK_AFC9H3mdtx3xs843Om0zNFM8Dmk4O_87PogtLjF2LXPuFNhJQncp0xLSYTk_9Q9YY00Juh0Rt2vwFw5JMoJYfpVln8uGpj9rnTYnb-1WyyBVN03DMdmusI-vskykNbCceDe6SepD7SlDm2v56Ba7Rd8UB25klDcFw4fk5ZtFM1lt5-O3sK-83oqr9gX19g42dL7tmNScfRr20cTk_C7P1zsF7o_aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
شروع پروازهای هواپیمایی سروش
📍
در مسیر تهران - استانبول - تهران
✈️
ایرباس مدرن310
💺
صندلی بیزینس
⏳
بهترین ساعت پروازی
خرید آنلاین از :
www.Booking.ir
📞
+98 21 8586</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658136" target="_blank">📅 22:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7dff107a.mp4?token=TAtf6Lsdogy72T12zAR1SBKsbc1K6-oUGmbw-h39pFbQ5M6y5FoRsi7HxGZY3E9IkB2ub9Zc4_5z0xCCq8CfuN5Evr1_aS8cMpH4U2psq20DwsBdt0xYh5E2fjott_euWky2xz37DR6CgxY55mCDD1Hv1et_NoG724Fr1Tj_d3pPscVVyCffpVhZcmAf2qfqvS-pw1YVdqb9ogA-trh9ZYlmkGB-4jamA01CzxmvzW9QY8ZUFa3jHs3qwLT8OcRJxDKITYMpbY7nsiuE4KB6M0AX_3GPToPtFqFKIUzNo61bq74NRhBqcL3pAy8sbbf_Cj9OE81lzgI-gGIjttY2c0TKv0papgZM9LHH2h9vJmS_f-gmg2RHrcYo9ww1zE4nnvz1LnEKj63xJjs3u7PfXdPWX6BMylCUwOG7S9mK9rJY6Quh7OrKkHzTy_DpE7WRgX7A4gLkYQoLFTjirFimgoYOmRFUALCCLDNIwjO10aZnOcy7lJw3cSP15AKzFAQ2pUDC5g6L1t6WrdXVbKoDS1EfW1qkMJRahaSl3hbg6FrK3TbTig5Vq1ZIjdYf_YRQGa-DGPaijDVXNh2HE2VM3nx9iTMBLrPrk9vsGT_ENx8MKi3_JANUpe9zVymxEoc2NAe0zLs_1dvtSgOkNc2BOtlB8P8ELkWifQ9pI0acuv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7dff107a.mp4?token=TAtf6Lsdogy72T12zAR1SBKsbc1K6-oUGmbw-h39pFbQ5M6y5FoRsi7HxGZY3E9IkB2ub9Zc4_5z0xCCq8CfuN5Evr1_aS8cMpH4U2psq20DwsBdt0xYh5E2fjott_euWky2xz37DR6CgxY55mCDD1Hv1et_NoG724Fr1Tj_d3pPscVVyCffpVhZcmAf2qfqvS-pw1YVdqb9ogA-trh9ZYlmkGB-4jamA01CzxmvzW9QY8ZUFa3jHs3qwLT8OcRJxDKITYMpbY7nsiuE4KB6M0AX_3GPToPtFqFKIUzNo61bq74NRhBqcL3pAy8sbbf_Cj9OE81lzgI-gGIjttY2c0TKv0papgZM9LHH2h9vJmS_f-gmg2RHrcYo9ww1zE4nnvz1LnEKj63xJjs3u7PfXdPWX6BMylCUwOG7S9mK9rJY6Quh7OrKkHzTy_DpE7WRgX7A4gLkYQoLFTjirFimgoYOmRFUALCCLDNIwjO10aZnOcy7lJw3cSP15AKzFAQ2pUDC5g6L1t6WrdXVbKoDS1EfW1qkMJRahaSl3hbg6FrK3TbTig5Vq1ZIjdYf_YRQGa-DGPaijDVXNh2HE2VM3nx9iTMBLrPrk9vsGT_ENx8MKi3_JANUpe9zVymxEoc2NAe0zLs_1dvtSgOkNc2BOtlB8P8ELkWifQ9pI0acuv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ساقط‌کردن آپاچی به آمریکا برخورد؟
🔹
جزئیات جالب توجهی را در این ویدئو خواهد دید که به شما نشان می‌دهد چرا آمریکا از سرنگونی آپاچی عصبانی شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/658135" target="_blank">📅 21:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
بقائی: حمله آمریکا به منابع آب در جنوب ایران، حمله به نبض زندگی ایرانیان است
سخنگوی وزارت امور خارجه، در پیامی در شبکه ایکس:
🔹
آب نبض زندگی است و آمریکا نبض حیات ایرانیان را هدف قرار داده هست.
🔹
آمریکا در ادامه تجاوزهای خود علیه ایران، شب گذشته زیرساخت‌های حیاتی آب در سریک هرمزگان را هدف قرار داد و تأسیسات تأمین آب مردم را مورد حمله قرار داد؛ تأسیساتی که به بیش از ۲۰ هزار نفر خدمات‌رسانی می‌کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/658134" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC6WlEd0eLgxnbJ1tdsjviDnSj9Q5rxPvS0-iRccj4pYeVP4hdCyCmPBT_UVHCCWON5Z3IDjBBf6LlAqCMN9FyczFyec96lqkMntxzEUkodfH2dkgRWQ07Mg0tOwyb0EDjFoXlKP8vdua4ysUDALVPh68A2BF4O8TR6d1e7JbALOtO6dTxsyXF_aWmjbhvpJdWWvg9juH6CZkqCuU1mdq9qEXUbzA0RBBCP_gANtDRuCgvrP79Np_aJQFcAnbHRl8-oVfDYPjBCgS0EYZ0HgjQRXWf6OGeOeTd8vJPBQgNBYyhjCJUuyXWt35rc86ibLPVpVQcLlY8vy5EfGeTvV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرش ایرانی همچنان محبوب‌ترین صنعت‌دستی
🔸
در این نظرسنجی بیش از ۲۳ هزار نفر شرکت کردند که سهم روبیکا ۶۶، بله حدود ۳۰ و تلگرام حدود ۴ درصد بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان فرش، قالیچه و گلیم و ۱۸٪ هم صنایع چوبی و چرمی را از میان صنایع دستی ایرانی می‌پسندند.
🔸
سلیقه مخاطبان بیشتر به سمت صنایع دستی با هویت فرهنگی قوی و کاربرد روزمره است و شاخه‌هایی مانند چوب و چرم نقش مکمل دارند.
@amarfact</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658133" target="_blank">📅 21:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی: ساعت ۱۹:۴۴ امشب، گزارش حریق گسترده در یک انبار فرش واقع در محدوده خیابان ری به مرکز فرماندهی اعلام شد
🔹
محل آتش‌سوزی، یک فضای حدوداً ۲۰۰۰ متر مربعی است که عمدتاً برای انبار کردن فرش استفاده می‌شود.
🔹
عملیات مهار این حریق با مشارکت ۸ ایستگاه آتش‌نشانی همچنان با شدت بالا در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/658132" target="_blank">📅 21:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
برنامه بازگشت حجاج به کشور؛ امروز ۱۰ پرواز از جده انجام می‌شود
‌
هواپیمایی جمهوری اسلامی ایران اعلام کرد:
🔹
عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور در روز چهارشنبه، ۲۰ خرداد با انجام ۱۰ سورتی پرواز از فرودگاه جده به چهار ایستگاه پروازی کشور ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/658131" target="_blank">📅 21:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای وزیر جنگ اسراییل علیه ایران: نبرد علیه ایران هنوز به پایان نرسیده و اسرائیل آماده است تا به ایران حمله کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658130" target="_blank">📅 21:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای ترامپ: ماه گذشته، به نیروی نظامی آمریکا دستور دادم یک مأموریت مخفی برای پشتیبانی از نفتکش‌ها و دیگر کشتی‌های تجاری از طریق تنگه هرمز اجرا کند
🔹
امروز با خرسندی اعلام می‌کنم که این تلاش منجر به عبور بیش از ۱۰۰ میلیون بشکه نفت از طریق تنگه و ورود آن به بازار آزاد شده است.
🔹
بیش از ۲۰۰ کشتی تجاری با سلامت از این تنگه عبور کرده‌اند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/658129" target="_blank">📅 21:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته یک منبع منطقه‌ای درگیر در میانجی‌گری و یک مقام آمریکایی، عباس عراقچی، وزیر خارجه ایران، به میانجی‌ها و آمریکا گفت برای گرفتن پاسخ به چهار یا پنج روز زمان نیاز دارد
🔹
این زمان به یک بازی انتظار دیپلماتیک تقریباً دو هفته‌ای تبدیل شد،…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658128" target="_blank">📅 21:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت ‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/658127" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت
‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها ارسال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/658126" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5d-zZP3fEQ09rnqNLH2_hATky0Qc2DqwRRRk_NnXg46M96L2PIrHvqd9RyBkLlLt4zqKVj_-j6BgET0iefcfg2ShCwXG23Fj9gvg4n1g-58HZU8YlyK1J4j_4t08DqgwlKGgJqWa7q3w5XazZ5Xacx6vxN21snkHSbt9pEgwCTH1OLNvsUUuPp0wZgPw7pW7dqdpIUqDuTyJvs4YDNnHHNQ-P0UEgudWHzkdKDkVpIV9qx6ih7_ALF4pclfKC5ZlxfEHgQ_fRt-t4S_NA_4joAVQDkjrGsrmP-tGO72wlIUtHGRbdyTDs-c32WPBkCu7K6BFEwTxaebNaLdtRn1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در مسیر جیمی کارتر
فایننشال‌تایمز:
🔹
آمریکا امروز بیش‌از همیشه در مهار نتانیاهو ناتوان به‌نظر می‌رسد، این اتفاق موجب شده تا ایران نیز تمایلی به مذاکره نداشته باشد و آمریکا تعیین‌کننده پایان جنگ نباشد.
🔹
ترامپ برای خروج از این وضعیت، سه راه دارد: تهدید اسرائیل به قطع کمک، جدیت در مذاکرات و ثابت‌قدمی؛ که با توجه به سیاست‌ها و شخصیت ترامپ، محتمل به‌نظر نمی‌رسند و حالا، او که از تکرار تجربه کارتر و افتادن در چرخه تلفات نظامی می‌ترسید، بیش از همیشه گرفتار آن شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658125" target="_blank">📅 21:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNNg_DaPXt3fwfozbEPcc7F-2MFLqrgjY-MMMedgOoMQNPQxprSGr5N7pZpC5rh-dFpcFuBpmZlOCs0Nwz3mb9qlYqIzKRN0rlN3_F419p-iaj5lchq1ED353JHIFxpBHfedW_6e6D2RGyOE98uQDvLV4izT2VofnpiAz7Gu5_RORU4VtIWBENnd9uSI5bAPZyY139t0z5D_Atje5EqLrM5Ob05sqvDF_-DIWF23zybxR2wGV5kup7yW3q7LjDhQfKbATG1NrE-FPD6v25ok8OXvmOrlZwfxsHDhCo4SMMQDrTRFUroSsk_hVNQD_CrGB_BhFYfepDbSxRr2Te_D6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFN--TRcIb4sxFCn5eNbv04tzeAfnt_42n2PFo5_rCKTFMl9v6-eP0nuqA52deGETpocZBoX6UGaXX2Y8Gf0w0Q6kCYnsd5itMqn1plougva6yQwIYWcsmxJVe3ieCQJDs61xSgBY_GoTWU272BMF437QlulH0uvqqW50dpD5XAj24kTZ92LyNWUDb7OuhKKYHgFLOcCXN6iYnkn1StsMoE961q6nfA8cvyJK2LvZkVHh5WpgQEHzh8J1zhBDAtVfODW9Zft9nuYFRmeabPSWjwR9hG0Su0UZiCLpa169ABWT5y1KtHJlLY7tVanCBlrfM5eGBskMPbIde_UOLUKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA9tIkx3swi05VTfAOCemW7K3agS2mNdagus7ej9kFVEwrknq0ZYWTLOwbrN_5wIwQgE2YECaKahIswr1VtNg8qfQfW2r-7D3EowvVVsfAdguYOKqn1egikL2UC2QljhiW1YWUHszabaaWYYpRfqhqKGrLNOfl7wzD4wxuqeAgmRJh88Y7LhLSe4M2kbjMa53DXNRrHUNexBwv5La-P7HiFdcJPYG0wdpIp6K2h3DdeA54jt1Ui63rOhmOUnUuMNZYd8eku566LUgX8LefaxRn9qUdmlI19HTCdib4osBaFk3KbQIN_XA5cOegAaboJ6t47aExz3jGKkssKRiDgUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAp3YBVNgNMX6Oq8U3quYA6C9ussugWSdWhuhh5vPtae7zz2TLquGYhEOwTJ6lVKw0tIrLePjObL-iQhm3z3dFHV2LUwN_YtfLJmInuqlq_OsTu7VzlrETJb6rQTabiMlLLTYueDEYGVurrvrrR-x-XDjv8d8VR80PBzJs_Q8WULDAbrMq3oUoe3DWfdO-VKptV-jmWvebg8U85mzNCaPWLoETQ2TxJ7555tmXnhFNs3FhQ_gJiHXAUPlRQMyonSpU4VG9_TKKiIeOOz-560p6ErFyJCWSX848wAF2mPWApw4YZ8F5FqmELw9h2cqbb9yM4iEKMKRXM0raI-co5UXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اولیه از حریق یک انبار در میدان قیام از زبان سخنگوی آتش نشانی تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658120" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRaL67LHR_H4HBWkHDcvJnIRnSFxfFRYQSW7xZzy0-Cke-Cf8vaCB7xIfBePp4PdrAx8wXbvDnJ4vUZdD97NErrh6ZHB8t9R-nxbOLkcwAwgVRNaSOmGwdelbZRIrn7af1oLh7NDgUBrILI0iQbEaD7pJq6roXpOCA2NFjw3WCyreARUb7-Kl_Vvu58Ah0tywRVcGdXawejFNWeOGNwNngAhXwfPizo6K7yIk18q1s3f6gjYMQDQU73I5qy0VgiuaKwIJva9LFiyR-vy5f4Q1q_CobaYemrPTcnXU3M7w2OLF1mwLXyCVXrCsI6b9HS76nuUebIKsDwAWWXltYVNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشهورترین پیراهن‌های تاریخ جام جهانی
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658119" target="_blank">📅 21:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111fb7a2d5.mp4?token=FZ2wBzrhz9t5ws6wg9HdbL-fiRBX0QXx3nt752Bpz1zpBx_HXUK0jnn_58LjMNKt8kTuLb33k7uoFPLdDgQyWtM8kEw1RclogBHT96F3DsaGYlx9cdj41CcOQnSYtp_8EsuMtcwDCQVBPmEbgUzXVdeNMSM0e7CChyP1z4-2fdNl2nwFYMCQTuR7j5AYWxZV4wvXU9Mux4vW9tgnlzgd4FbjebtiiNL-eElpH9YYDErcfRaA9xOnxqd3PXp-Y3ejPhQ5UnjjdYP63cA0yuZMXXGGKI8bQEBnxfVdPFm2N0liUIY4_qH3QAhj2GoC7fcblcXJio5BTSvHnDEESEpxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111fb7a2d5.mp4?token=FZ2wBzrhz9t5ws6wg9HdbL-fiRBX0QXx3nt752Bpz1zpBx_HXUK0jnn_58LjMNKt8kTuLb33k7uoFPLdDgQyWtM8kEw1RclogBHT96F3DsaGYlx9cdj41CcOQnSYtp_8EsuMtcwDCQVBPmEbgUzXVdeNMSM0e7CChyP1z4-2fdNl2nwFYMCQTuR7j5AYWxZV4wvXU9Mux4vW9tgnlzgd4FbjebtiiNL-eElpH9YYDErcfRaA9xOnxqd3PXp-Y3ejPhQ5UnjjdYP63cA0yuZMXXGGKI8bQEBnxfVdPFm2N0liUIY4_qH3QAhj2GoC7fcblcXJio5BTSvHnDEESEpxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیازی به توافق با ایران نیست، فقط از این جنگ خارج شوید
‌
معاون ستاد انتخاباتی ترامپ در سال ۲۰۲۴:
🔹
من هم خوشحالم که خلبانان ما سالم هستند، اما سوالات زیادی دارم از سرنگونی اولین سوخت‌رسان‌های کی‌سی-۱۳۵ آمریکا در نبرد.
‌
🔹
همچنین درباره خلبانان اف-۱۵ که بالای ایران سقوط کردند و هنوز ندیده‌ایم‌شان. فضانوردان به کاخ سفید آمدند، اما خبری از آن خلبانان نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/658118" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRsVn2P-bEEv4lBDCrSAtceGTwYAsoVzPyEIOc7ow25oTXtsPtoAwS4BqTnCXwVfo7hQJ97AAug9VYtORuqM1hrIJ_0WXL9-8thTq4WH6lRXztWgxnju6P0PBDt9Zq4vG8LSoN_KWrgqpBgMIOQkd8QQ96ceWH1Z7uD7Xdki4-VO5bHXzgc9TXgslgE_YezuGeFcvDZbTmqDl5PS39GJpAHfCoq-9XcOcDcXEIjoCMyghGWKdagn38zQyEaYavRmOCbbKbfVAAP1-FFFDVYKQXmYU8JiYtS0mkpr6V38TskPdEIUzeOTP5Qy82G8nXa6cOpIE-yY4sFp30FF6TLyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاتل‌ِ آپاچی
🔹
از شب گذشته، دونالد ترامپ و برخی مقام‌های آمریکایی مدعی شده‌اند که جمهوری اسلامی ایران یک بالگرد آمریکایی از نوع «آپاچی» را منهدم کرده است و تلاش می‌کنند با برجسته کردن این ادعا فضای تهدید و تنش نظامی علیه ایران را تشدید کنند.
🔹
آپاچی‌کُش‌های باسابقه، حالا ژست عصبانی گرفته اند و با سیاست های رادیکالی که تا به امروز بارها شکست خورده، دوباره در پی آزمودن بخت خود در خلیج فارس هستند.
🔹
فارغ از چگونگی انهدام این بالگرد، ترامپ و تیم آمریکایی نمی‌خواهند از اشتباهات گذشته‌ خود درس بگیرند.
از پاره کردن برجام تا امروز، از حضور در ویتنام تا امروز، از کشتن آپاچی‌های بومی آمریکا تا امروز!
🔹
هفتصدوهفتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/658117" target="_blank">📅 20:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0992445ad.mp4?token=ABN6-V0o9c-PN-WIFU23fh2BYrjzate6kQYO9_pqZ9SP6nmcvBkb9tCPfLaO1nA_yI72-dX6aRbL-GPmPML0dw0wyM4aovNA3so69mGKbhy2XQCr2fhSFMey3kLiRi9LoZirbeAlVsM1LwMxuQNIovvqlMa2ZKmr8HVhdlLnua5cZBZkTQEarAjdVhlgK6w8tfONJcOJ-YNC2eWZz775T04UuOZepJj5M3Efr2qgR9rnwwQrLDd9ecII71Qrek9GpcJ2yaYx4Xn5rRS825aHkl-arv-1JFwdqI5Rt0STnkaMoMANzCiU2P9MIYQr5-xIis9tsBIpiJz2QpCHaq2xtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0992445ad.mp4?token=ABN6-V0o9c-PN-WIFU23fh2BYrjzate6kQYO9_pqZ9SP6nmcvBkb9tCPfLaO1nA_yI72-dX6aRbL-GPmPML0dw0wyM4aovNA3so69mGKbhy2XQCr2fhSFMey3kLiRi9LoZirbeAlVsM1LwMxuQNIovvqlMa2ZKmr8HVhdlLnua5cZBZkTQEarAjdVhlgK6w8tfONJcOJ-YNC2eWZz775T04UuOZepJj5M3Efr2qgR9rnwwQrLDd9ecII71Qrek9GpcJ2yaYx4Xn5rRS825aHkl-arv-1JFwdqI5Rt0STnkaMoMANzCiU2P9MIYQr5-xIis9tsBIpiJz2QpCHaq2xtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/658116" target="_blank">📅 20:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ترامپ: بدون من، اسرائیلی وجود نداشت
🔹
رئیس دولت تروریستی آمریکا در گفت‌وگویی با سازمان رادیو و تلویزیون رژیم صهیونیستی گفته است بدون من، اسرائیل وجود نداشت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/658115" target="_blank">📅 20:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz0YlV4dj473aB36xCGDiyCMz2xeSCEDO_WvaRu-2ODDEAk0kdF2k0hHhdt9qPtfXeX_mzh54n9vvyNEeJhlmSzr5d5z57xQJWfRYWLvx95FoQhGRPgIcpAgnjkHORlsun4KQcSREv4j_YKUk2O_ek717FPI-NjkSSpfZFN-22kFwockBPdbC6D_ZovfBnmpzMNc-_A7FRzrrz7bIsa0m2MLNziS_2F39Sp8pRRdoY5lVLPneti-AEZUAZpUUBQwQ5ugoLqaOHuWcdlpjd8mmIb_etHZLIkpipIph8oK9z8Ehg4Eo1bf3jwIuxe7dEL3fP6b36D7C1-HTIAT9wa3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بانک سینا در جمع ۵ بانک برتر کشور برای دومین سال پیاپی
🔹
بانک سینا در ارزیابی بانک‌ها و مؤسسات اعتباری از سوی بانک مرکزی در چارچوب شاخص CAMELS، برای دومین سال پیاپی در میان ۵ بانک برتر کشور قرار گرفت.
🔹
بر اساس گزارش خبرگزاری وابسته به بانک مرکزی، در ارزیابی انجام‌شده برای شش‌ماهه نخست سال ۱۴۰۴، وضعیت بانک‌ها بر پایه پنج نسبت مالی کلیدی شامل نسبت کفایت سرمایه، نسبت بدهی به حقوق صاحبان سهام، بازده حقوق صاحبان سهام، نسبت کفایت سرمایه لایه یک و نسبت مالکانه مورد بررسی قرار گرفته که بانک سینا در این ارزیابی، برای دومین سال پیاپی در جمع ۵ بانک برتر کشور قرار گرفته است.
این شاخص‌ها از مهم‌ترین معیارهای تحلیل مالی بانک‌ها به شمار می‌روند و در سنجش توان مالی، ساختار سرمایه، سودآوری و میزان ریسک‌پذیری نقش تعیین‌کننده‌ای دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/658114" target="_blank">📅 20:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9195af6679.mp4?token=ee3vn7D2ql98Rrp4EPB4UU694CSGa5XLLUIW-T9IOfAYJke9NCmlUrRkKm9U5j4VZIi_1HAbWKWI6pzmjIStWbUcC2McQYGNIpzNlvg8NiGZ2np8TxpTUp2yy_3EqKWsJO1H-LSF2yBoJNJYbkzCOkxvOJz5NHDM7GlevR7-CD8Yr7FVmQ6Utk4ZYd69Nw0_-j1m0ta7Ar5yyIouO7GOnGKxlFkvEYIXIRg2XksW1WXOt0Tt9MmPFgjD2pr79u5xV3_Tqs8qPLxv3pTFKloChonsBYmvCp2DhmFIIqD0eqnjzSZ-Ck-gqUrGVMBXiViI2RDRltJ384_H2rkJVJlgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9195af6679.mp4?token=ee3vn7D2ql98Rrp4EPB4UU694CSGa5XLLUIW-T9IOfAYJke9NCmlUrRkKm9U5j4VZIi_1HAbWKWI6pzmjIStWbUcC2McQYGNIpzNlvg8NiGZ2np8TxpTUp2yy_3EqKWsJO1H-LSF2yBoJNJYbkzCOkxvOJz5NHDM7GlevR7-CD8Yr7FVmQ6Utk4ZYd69Nw0_-j1m0ta7Ar5yyIouO7GOnGKxlFkvEYIXIRg2XksW1WXOt0Tt9MmPFgjD2pr79u5xV3_Tqs8qPLxv3pTFKloChonsBYmvCp2DhmFIIqD0eqnjzSZ-Ck-gqUrGVMBXiViI2RDRltJ384_H2rkJVJlgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: کشورهای عربی میانجی‌گر بدانند ما زمانی اتمام جنگ را می‌پذیریم که جنگ در تمام جبهه‌ مقاومت به پایان برسد/ صهیونیست‌ها بدانند مسیر اتمام جنگ اینگونه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658113" target="_blank">📅 20:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای عبدالخالق عبدالله مشاور سابق بن زاید: امارات در حال هموار کردن راه برای کاهش تنش با ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658112" target="_blank">📅 20:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎬
#تماشا_کنید
↗️
✅
تحولی در مسیر اعتماد؛ گزارش دستاوردهای بانک تجارت در دوماه ابتدایی سال ۱۴۰۵
‌
🙏
بانک تجارت در ۲ ماه نخست سال جاری، با تکیه بر سرمایه اعتماد مشتریان و اتخاذ رویکردی مدرن، گام‌های بلندی در جهت توسعه و پایداری برداشت.
🌐
گزارش ویژه
👉
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/658111" target="_blank">📅 20:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
از دلیل عدم اجازه ورود به نور تا ماجرای عذاب قهر با پدر و مادر
🔹
00:12:50 تاریکی مطلق و حضور دو موجود وحشتناک
🔹
00:29:50 عدم اجازه ورود به نور
🔹
00:35:50 پیغام پدری برای فرزندانش که ۱۵ سال با یکدیگر قهر بودند
🔹
00:52:30 ماجرای شنیدنی از وابستگی و دلتنگی همسرم به من
🔹
00:58:50 فضای مملو از مه گل‌آلود
🔹
01:01:10 عذابی که در جهت قهر با پدر و مادر متحمل شدم
🔹
01:14:30  رؤیت علت مرگ و جایگاه ۵ نفر از اطرافیانم
🔹
قسمت یازدهم (صدای سخن عشق)، فصل چهارم
🔹
#تجربه‌گر
: مسعود نبی چنانی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658110" target="_blank">📅 20:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/658109" target="_blank">📅 20:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هشدار حنظله به نیروهای آمریکایی‌: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658107" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usYDmbHA77vNArlBxG9o4hkG_xu3dj1eDRxkn5fdYnc37moKH_KnvjoeRoUEB505vg4VUh5QU90I_obqGNCNU0DiE1WkigHovGs3UVM9oxbHBtHz3gWRDglLZFaHW2M-biuiCQKoLh0ELuxwkmD40jBVJKXtZgvPJ3GIjBSXRF1fv0UWWJiqs995Ux5enjCpcolkH1oDgnZSuVTx56zcDFkQxAqFv5D3Cjs5ay9d9Wnwjc40tgPt1yzac2MTcVvODSFubKxw6FBV_oj276EMj8masu5XZ40lQJz_h4ItgWsQlrq9i0oHR6qxcm-QdzqpIc4ar0RkxjUk2q7-3M_COg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: زیرساخت‌های حیاتی، شریان‌های زندگی مردم‌اند
رئیس‌جمهور:
🔹
زیرساخت‌های حیاتی، شریان‌های زندگی مردم‌اند. تهدید به هدف قرار دادن آنها از شبکه‌های حمل و نقل تا صنعت برق و آب نه نمایش قدرت بلکه نشانه استیصال در برابر اراده یک ملت است.
🔹
ایران با تکیه بر دانش و توان متخصصان، وحدت ملی و همبستگی، در برابر هر فشار و تهدیدی استوار خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/658106" target="_blank">📅 20:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52cdfb59be.mp4?token=bY8nyUxTfqy3Wo0iS6sX5R8kkpU8R4CyIuQR76JnnACSRSxJMLRFbuKRImZeztHA8HI8mz1hmz0GDN_OqD8XradVItW4V40_5RNxiZGxnUQWDqfUIplwRlJsuMrEzr7nLlh498DYD6zRJovwYbfYbcftUyB0Sar75ghAyDaPlX5GtB4Ic8173Zk8SVdVzwdn80iALqTyAYIN09gLiLN31NHuXKegM7TZ5tTorI15YPpf8wPHfWJ5bZVBstojxE7qmwY0gsKhf36E7mBWkLjmX3a1TbFs-MijtlBOs6AvxDs08h-8NEdw-wi5Cg9J4ivNgAkvDRTPBdLQ4zXhIkcgQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52cdfb59be.mp4?token=bY8nyUxTfqy3Wo0iS6sX5R8kkpU8R4CyIuQR76JnnACSRSxJMLRFbuKRImZeztHA8HI8mz1hmz0GDN_OqD8XradVItW4V40_5RNxiZGxnUQWDqfUIplwRlJsuMrEzr7nLlh498DYD6zRJovwYbfYbcftUyB0Sar75ghAyDaPlX5GtB4Ic8173Zk8SVdVzwdn80iALqTyAYIN09gLiLN31NHuXKegM7TZ5tTorI15YPpf8wPHfWJ5bZVBstojxE7qmwY0gsKhf36E7mBWkLjmX3a1TbFs-MijtlBOs6AvxDs08h-8NEdw-wi5Cg9J4ivNgAkvDRTPBdLQ4zXhIkcgQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: براساس اطلاعات دقیق و میدانی، تعداد کشته‌های ارتش آمریکا تا به امروز ۵۰۰ نفر بوده است/ آمار منتشر شده از سوی ارتش آمریکا مضحک و خنده‌دار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/658105" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL722eldOba1tZwbpYhKbdg-HiPpFY5bOKXShKu35ZscFL5c_7ZlxlF1u7Emrf0UXUpPqBKmGE543pUrhDAdm8sp1mBhoafdR6KtUzGWki84PP3_AudY-iO5k-Yeg8aLrmNi1tfHlGUg2YWl1KXVV9WKoMikZ5gcPkPwdGWb3ST6wI77J6kt2zO_UYqYhaQhngo_QoeKX8KdwMPoiU1eupgY2msoBZVgjqVfyX5ruxxAbH8G9D76Ja3kGJTuveeLsd_9VC4nOcEW5Dy__qh2WY45rWHkbEAATgZA_AheHzD-7biDF0Y1nN391nplBVQLe_hgY7GAGUHF27FkgPX_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnIYrs9MZfG_OSG_qemAr5IoaTXiDmT30rvbKO0Y6O569YNDbnV0lNK1agkhTY7csnOiOxUAmJCBlNcYBxjeXsUWfxHLurd-b0hxR-VQlTLqrTnNbCrJroMjzbZMOTnk0xWDk-ItuOnszbWVrbocF4c5KpW59i2pX2Kef27zrNK9WIZCcJQ85g3XmboJmC1rMutCrxXqUKUggjSclHGPlrJjU6xoB95Jgjw4-C2qAypOI-oFvFxbTq3VgcGCdt7dj0UXSlKDUkbVhcaAOE5WYWzG7PKT-X6MDUb1tkOej8hoP3v_rAGvV7pcMxq2rCIZqKJ8IpC_Uuv_8Z52vuaahA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: نازنین
🖋
نویسنده: فئودور داستایوفسکی
🔹
«نازنین» داستانی کوتاه اما عمیق درباره عشق، سوءظن، تنهایی و خودفریبی است؛ جایی که راویِ نامطمئن، حقیقت رابطه و فاجعه‌ای پنهان را لایه‌به‌لایه آشکار می‌کند. اثری رازآلود و تأثیرگذار.
🔹
مطالعه این کتاب به کسانی که به واکاوی ذهن انسان و روابط پیچیده انسانی علاقه دارند، توصیه می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/658103" target="_blank">📅 20:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658102" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658101">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: روز سه‌شنبه یک نفتکش را در خلیج عمان پس از آنکه درحال نقض محاصرۀ دریایی ایران بود، از کار انداختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658101" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658100">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYmUM0Zq7J_fVW4AJZkCHXQWVgXcV9h4v6mSoTFHV29j1MuEQSpZEwmwxvWf7dNKuAS_UtBkhb8H6HK_5FCYoPPQc_ZCGNIdF6Ws8D0RcUR7TlCghh2mkkHB_XPNGRVQNEIsWnT4ucYhnBj3FSTdgWTcNEeFdBUT4KrAwxMwiB7rBWOwWZbapYYXkA7TSeKT521aOvjCe8NcswZVSzmsj9-usnGi18eWEM95YUJ8vfImvrzHjVIueCrnU-4wN2c9-UPJRcR3m51gNDhEYomaYnxPoBWTDG57MBV4RX57uGoTKTDPIDtdzJgG1rEzXhRzzozVl83ypXVdOnoPAryTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون سازمان زیباسازی: شهرآرا؛ خانه ای برای رسم نوآورانه در شهر
🔹
حمید عسکری عاون فنی و عمرانی سازمان زیباسازی شهر تهران در آیین گشایش «عمارت شهرآرا؛ خانه طراحی شهری و مرمت بناهای تاریخی تهران» گفت: این مجموعه بستری برای تبادل تجربه، گفت‌وگوهای تخصصی و شکل‌گیری و رسم ایده‌های نو در حوزه طراحی شهری خواهد بود.
🔹
وی افزود: فضای مناسبی برای نمایش دانش، دستاوردها و تولیدات حوزه طراحی، مبلمان و تجهیزات شهری ایجاد شده و محصولاتی همچون پایه‌چراغ‌های هوشمند، نمایشگرهای دیجیتال تبلیغاتی، نیمکت‌های چندمنظوره و دکوراتیو، تجهیزات نورپردازی و سایر عناصر طراحی شهری در آن ارائه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658100" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658099">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: روز سه‌شنبه یک نفتکش را در خلیج عمان پس از آنکه درحال نقض محاصرۀ دریایی ایران بود، از کار انداختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658099" target="_blank">📅 19:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658098">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قطعی آب سیریک پس از حمله آمریکا در ‌‌۱۲ ساعت وصل شد
مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
در پی حملات بامدادی آمریکا، خسارت فراوانی ‌به مخازن ذخیره آب ۵۰۰ و ۲۰۰۰ مترمکعبی شهر کوهستک و بخش بمانی شهرستان سیریک وارد شد.
🔹
از صبح امروز ‌تیم‌های کارشناسی، نیروی عملیاتی، رانندگان ماشین‌آلات و عوامل پشتیبانی با استفاده از اتصالات، لوله‌ها و ماشین‌آلات مورد نیاز عملیات جایگزینی تأسیسات آسیب‌دیده و ایجاد خط انتقال جدید آب را آغاز کردند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658098" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723629509e.mp4?token=kx14xjcFACdNek50YAMC-6R8sIq2pzuZHJBBaY7C0MIbPiX7f5NTc18sLhFbPySCKy6bEUw7hoXQbTqTPltFp9KI2TrhnOwS3fJaln4fjY8tHdnLk5ucSXMDhzj82gFGnHn9ANDvV2L93cLL9rym_83XMqyoIip59wDw7E2pelkxc6JcEQO91SUHiNEMmhhOwCNpWwFxpfqLFIaoXGP6Cpy-lS_ji6Qq5ckkodgQC5Du7Vl9jgxm037jS6Jadhl-h8KFV_jxPY3v0hAgrCu2yp0Irfgzw7KuQAjjc2x2ysSwKd6aWipx_g5tobM1CTX6WrdvlUq1Vh7cDNoGdKLBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723629509e.mp4?token=kx14xjcFACdNek50YAMC-6R8sIq2pzuZHJBBaY7C0MIbPiX7f5NTc18sLhFbPySCKy6bEUw7hoXQbTqTPltFp9KI2TrhnOwS3fJaln4fjY8tHdnLk5ucSXMDhzj82gFGnHn9ANDvV2L93cLL9rym_83XMqyoIip59wDw7E2pelkxc6JcEQO91SUHiNEMmhhOwCNpWwFxpfqLFIaoXGP6Cpy-lS_ji6Qq5ckkodgQC5Du7Vl9jgxm037jS6Jadhl-h8KFV_jxPY3v0hAgrCu2yp0Irfgzw7KuQAjjc2x2ysSwKd6aWipx_g5tobM1CTX6WrdvlUq1Vh7cDNoGdKLBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: وقتی جنگ تمام شود، تورم مثل سنگ [از صخره] پایین خواهد آمد ‌
🔹
میلیون‌ها بشکه نفت را [از تنگه] خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما مدت‌هاست میلیون‌ها بشکه نفت را خارج می‌کردیم. هر شب نفت را خارج می‌کردیم. ‌
🔹
اما حالا به…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658097" target="_blank">📅 19:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ بازهم پایین آمدن نرخ تورم در آمریکا را منوط به پایان جنگ با ایران کرد! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658096" target="_blank">📅 19:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f245a6dbef.mp4?token=ONAz8UDtoUqCNCdTPQ8XA1lUMDKvlncMknhl07EMuy-PiiXgjz5EekObh9TmkZD0xB7xuDt23LqmKv2ALkb5O9yPqiig9XJeGbomzYh1oF2ffEZpk2nvnfDqPdlJVu8_ObdMWz5xIf6uHv4iofUPpvAXsLoND5PAXIzW377Z7ThOb97EoTkfjkYhQcmvzkXEZdphfKfg7Xd_NRpJSfUg0-Q_ZsuUGryqcTD1d6bdNVv4OfGU6oLQK-_S00RCHOAfehhNwnA_LtaUy3MHEvJXCL2Sla86yFXMZgVK17xsXId1EYVCopoDh5NPF8qZ-9Sh6OL-AYyLUBuDBa6WNTDOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f245a6dbef.mp4?token=ONAz8UDtoUqCNCdTPQ8XA1lUMDKvlncMknhl07EMuy-PiiXgjz5EekObh9TmkZD0xB7xuDt23LqmKv2ALkb5O9yPqiig9XJeGbomzYh1oF2ffEZpk2nvnfDqPdlJVu8_ObdMWz5xIf6uHv4iofUPpvAXsLoND5PAXIzW377Z7ThOb97EoTkfjkYhQcmvzkXEZdphfKfg7Xd_NRpJSfUg0-Q_ZsuUGryqcTD1d6bdNVv4OfGU6oLQK-_S00RCHOAfehhNwnA_LtaUy3MHEvJXCL2Sla86yFXMZgVK17xsXId1EYVCopoDh5NPF8qZ-9Sh6OL-AYyLUBuDBa6WNTDOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و ما آنجا قدم زدیم/ تنها کاری که ایران باید انجام دهد این است که امضای سند توافق را آغاز کند؛ این توافق به طور کامل مذاکره شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658095" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658094">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و ما آنجا قدم زدیم/ تنها کاری که ایران باید انجام دهد این است که امضای سند توافق را آغاز کند؛ این توافق به طور کامل مذاکره شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/658094" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ترامپ قمارباز: ما میلیون‌ها بشکه نفت را توقیف کرده‌ایم
🔹
هیچ‌کس از این موضوع خبر ندارد. می‌دانید چه کسی از آن بی‌خبر است؟ ایران؛ تا همین لحظه.
🔹
ما چند شب پیش، در دل شب و بدون روشن کردن چراغ‌ها، ۲۲ کشتی را توقیف کردیم؛ چرا که آن‌ها [کشتی‌ها] رادار ندارند.…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658093" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ترامپ متوهم: ایران مدام ما را احمق جلوه می‌دهد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/658092" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1fed6b11.mp4?token=SOZ0shL5oj9PciFW9uj-rdMb5c5EtrdkzKM05WqhQKB70hKYRa0bYsFTuEWBd5g2ueXW43evSNY4HjOXoqYyjK90Lh2PMCDC3S4HE8Fynm94OzZWcm1zfClOYCHVdmA19OYgzQKeY2gV7E2Kuf82UgMjMAsMN0i2iLvBwz_jBkAB0tiCmFlFZY4Il4_JhFL6HOFH-edWhVqSgKx5vxdMtzFBZpCm2EHTanpjAQ1csSeVbcV_JqdNjEjWCef7hZcaGsUjExlibxLkG9nrZe8l3xmTGKsmRsDZ5pMH-2PA6iEWgslbFfoG4ioyJ8wKbtG6TGS2611Iu0r0QJPoGb1IWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1fed6b11.mp4?token=SOZ0shL5oj9PciFW9uj-rdMb5c5EtrdkzKM05WqhQKB70hKYRa0bYsFTuEWBd5g2ueXW43evSNY4HjOXoqYyjK90Lh2PMCDC3S4HE8Fynm94OzZWcm1zfClOYCHVdmA19OYgzQKeY2gV7E2Kuf82UgMjMAsMN0i2iLvBwz_jBkAB0tiCmFlFZY4Il4_JhFL6HOFH-edWhVqSgKx5vxdMtzFBZpCm2EHTanpjAQ1csSeVbcV_JqdNjEjWCef7hZcaGsUjExlibxLkG9nrZe8l3xmTGKsmRsDZ5pMH-2PA6iEWgslbFfoG4ioyJ8wKbtG6TGS2611Iu0r0QJPoGb1IWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سگ‌زرد: دیشب به آنها حمله کردیم، امروز حمله سنگینی به ایران خواهیم کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/658091" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYx4hvdFPjbnzxnyD1kByWcYIUDNppFUboC0CRie614ElFstZ-4O4htgQZ_VHKXHGrGAdfoJgW_IWXjSsINgcJbyimb9u3FivseCAIm-muf3HLSDx5VqK0SaSCoabE7_FcRWZtCB0JQ10JRt71uHVJjwQjkw6-9OcUR3RPST9RVVRbkqtaJN9vEcLQ-6oWfYRS2wUPM26zX8O4pej9X06qY8hu2ZW3gggY3DpjfYhB69-S8OuiQk-xHlXh7Bq-NCbjtvN9IiIzFr07nEAX2uscWTZQqxowsPFNrCIyAaXnDhVOj1wXD7OslLsmC8psA0es_UnMMJaKkGwXJq6pQG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی فوتبال لباس می‌پوشد | داستان محبوب‌ترین پیراهن‌های تاریخ جام جهانی | سفر به نوستالژی جام جهانی
🔹
برخی می‌گویند زندگی را می‌توان با جام‌های جهانی اندازه گرفت؛ نشانه‌هایی چهار ساله در خط زمان زندگی، از دوران کودکی تا نوجوانی و بزرگسالی. مجموعه‌ای از خاطرات فوتبالی؛ تیم‌هایی که دوست داشتید، قهرمان‌هایی که تحسین می‌کردید و پیراهن‌هایی که به نماد آن دوران تبدیل شدند. موضوع دقیقا همین پیراهن‌هاست؛ لباس‌هایی که داستان تعریف می‌کنند و به آثار ماندگار تبدیل می‌شوند. اما چه چیزی باعث می‌شود میراث یک لباس فوتبالی تا این اندازه پایدار بماند؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221763</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658090" target="_blank">📅 19:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4FOK6ayOlvMNnz-ma62Z4lSCFjcHzh9uR3kBJOamrUSvyZtNjK4RtpleXh7StHsYg1waJZMxqTRdjHgFbJ7qs_FSIihqINyNjKLHAjRazYFvI9FUtIDkkwTPKsMJm4XbMC4fH2m1L5KgwkarO5Sr9XjWunwY6wjdn_qa8aXV2Vdy12ZyTRVC4LhVuxCnk5LtgLZEIfTNxopwiHKA6hFVGu12B-CkX9XfKt494zOKAB5wgd7IlMtiHYhqD2srlk3RhqdJef4YSb3mCm_ERaycq1r9eIGRiiecMKdZgpWrYuRBfmNsGVGxEdI-04WxzZXJA77lqBCTheYmmVhjk6C7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/658089" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: من چندین ماه است که با ایران در حال کار و مذاکره بوده‌ام و آن‌ها باید این توافق را امضا کنند. این توافق، توافق خوبی است
🔹
پاکستان همچنان در تلاش است تا برای دستیابی به یک توافق با ایران کار کند.  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658088" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658087">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
گزافه گویی ترامپ: واشنگتن ممکن است بار دیگر با قدرت و قساوت به ایران حمله کند؛ یا با ایران به راه حلی می‌رسیم یا آن‌ها را نابود می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658087" target="_blank">📅 19:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658086">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6475ac6ebc.mp4?token=WfGutBDpud_cZnq7CDGfSDutQhF-dtFeXv6ZZH6nwuuW5IUb6MQ0rx9H-EkFknaCj8CB72VVLC7NI1FRumWgkhQlGNQLjFfqL15fVE2tudbUteBvKpEGhmrYwBtda9H8zEtjDS2albPLRMx3HAP8eXdGMpr-EUZnfbA7UHCFayM2uJOnV43rf5YWnIIzr0A_EYNJkLWbNzQ9jS-4hshV68MxKypfkMySEIuYYblITvrBpIRcIXINoScgdD2op9nv6ehZe81lZW2KeZd33uAy5yd4FoJVq_qK3z5ajPI5rdNoTxJ_8uhadCVzohRz68fDPuUE3G6O0ek_NIwYVzkBIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6475ac6ebc.mp4?token=WfGutBDpud_cZnq7CDGfSDutQhF-dtFeXv6ZZH6nwuuW5IUb6MQ0rx9H-EkFknaCj8CB72VVLC7NI1FRumWgkhQlGNQLjFfqL15fVE2tudbUteBvKpEGhmrYwBtda9H8zEtjDS2albPLRMx3HAP8eXdGMpr-EUZnfbA7UHCFayM2uJOnV43rf5YWnIIzr0A_EYNJkLWbNzQ9jS-4hshV68MxKypfkMySEIuYYblITvrBpIRcIXINoScgdD2op9nv6ehZe81lZW2KeZd33uAy5yd4FoJVq_qK3z5ajPI5rdNoTxJ_8uhadCVzohRz68fDPuUE3G6O0ek_NIwYVzkBIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی ترامپ: واشنگتن ممکن است بار دیگر با قدرت و قساوت به ایران حمله کند؛ یا با ایران به راه حلی می‌رسیم یا آن‌ها را نابود می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/658086" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaR4yU6ONpmjdejX1k5kw9aS3rgJ1AZAjmTFaSqf5dWffuDfRctt_eyfhLwoGHypH50KaMCaFax7xiPf6Ae6s8_JMhPo6Qbal0IEr11fKOvs7nEuC-7HeciQ5d05Xmqu8EDq1WgpOreTSgfOErykm7NNZZWnPcvTykRyn9r4Pg37bUcyiLRnK98McSC2OkhvQOXi5dtQfgvy_lK-iaofmszMVk8OiDjlMqyxwGb--nqDDX_72ATTMvHGGkNlQHtSqLe393N7O_SETUuBhcr3DbcQ3NamVhMudv6qh-zHc2ieZIJl7mcFVHDDqMMkOr-WK9K3N4Cv6f37IncBqyI2OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت سفارت ایران در ارمنستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658085" target="_blank">📅 19:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش ۴۰ تا ۶۰ درصدی حقوق بازنشستگان تأمین اجتماعی/ زمان واریز حقوق مشخص نیست
جعفری آذر، عضو کمیسیون اجتماعی مجلس شورای اسلامی:
🔹
افزایش حقوق بازنشستگان صندوق‌های کشوری و لشکری بدون تأخیر اجرا شده و بازنشستگان کشوری از ابتدای سال افزایش ۲۰ درصدی حقوق خود را دریافت کرده‌اند.
🔹
احکام افزایش حقوق بازنشستگان تأمین اجتماعی نیز صادر شده است؛ به‌طوری که حداقل‌بگیران حدود ۶۰ درصد و سایر سطوح بیش از ۴۰ درصد به همراه مبالغ ثابت مصوب، افزایش حقوق خواهند داشت.
🔹
هر زمان پرداخت‌ها بر اساس احکام جدید انجام شود، معوقات ماه‌های گذشته نیز به بازنشستگان پرداخت خواهد شد./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658084" target="_blank">📅 19:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc7752550.mp4?token=OgpkF2qUXXHicevAPpb7VtwbqoqApZTgQdw0O-u30a90QRt3ayINgRZoRP2LcN2jEU291FJYmTnJqOkCTfefAQ1pHUjexyV9uVYOSecytjWYLyqH3ioMvSRvBoksvA8oowwJHMIDShERnMwGm2IttK7wiAthYKeb31qbNdbqgA2uaT_4rLqtcTaiflHh7-ucUzDZFqJGgPJhTaLLDa2liYssRjhqN7k9Khm6_futIj5YU4L91bBa-9IfDYua9Ikd28SAh-Fb2eNU2E_umRgvzgk_8AZRMpkGrHaY74uADKtNGML0J930TFbnjRf5LoqiBKYe6GYvU_0LD5K4MIcSbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc7752550.mp4?token=OgpkF2qUXXHicevAPpb7VtwbqoqApZTgQdw0O-u30a90QRt3ayINgRZoRP2LcN2jEU291FJYmTnJqOkCTfefAQ1pHUjexyV9uVYOSecytjWYLyqH3ioMvSRvBoksvA8oowwJHMIDShERnMwGm2IttK7wiAthYKeb31qbNdbqgA2uaT_4rLqtcTaiflHh7-ucUzDZFqJGgPJhTaLLDa2liYssRjhqN7k9Khm6_futIj5YU4L91bBa-9IfDYua9Ikd28SAh-Fb2eNU2E_umRgvzgk_8AZRMpkGrHaY74uADKtNGML0J930TFbnjRf5LoqiBKYe6GYvU_0LD5K4MIcSbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جدید از جنایت آمریکا در مناطق مسکونی تهران
🔹
حاوی تصاویر دلخراش
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658083" target="_blank">📅 19:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658082">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: طرح تنگهٔ هرمز آماده است
کوثری:
🔹
همهٔ اقدامات و بررسی‌های لازم دربارهٔ تنگهٔ هرمز انجام شده و کمیسیون امنیت ملی مجلس نیز کارهای تخصصی مربوط به آن را به سرانجام رسانده است.
🔹
این طرح پس از آغاز به کار مجلس، در دستورکار قرار خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658082" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658081">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قبل از خرید و فروش سکه پارسیان؛ بخوانید
یوسف تقی زادگان، رئیس اتحادیه طلا و جواهر مشهد:
🔹
فروش پلاک طلای پارسیان دارای بسته بندی را برای تولید کننده‌ها ممنوع کردیم که از پک‌ها خارج کرده و به صورت فله در اختیار مردم قرار دهند. هر کسی که پلاک پارسیان را به واحد صنفی می‌برد، باید از پک خارج کرده وزن کنند و چنانچه وزن آن مغایرت داشته باشد مشتری را راهنمایی کنند که به واحد خریداری شده مراجعه کند اگر فروشنده پذیرفت که پول را دریافت می‌کند اگر قبول نکرد به اتحادیه مراجعه و طرح شکایت کند ما پیگیری می‌کنیم./ اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658081" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658080">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGIElUtmRy6qUjuZssjb8BqADZmZ9P2Y_AfdFgb7l_E21B23DiLh_FD6rkOb55X_3vx5Qcy1O6JK6H0fPKM8lYNRcXyFLmP76QZERm_iCED7zNxiyImkATABLzp9gE3h-Q7uF2hJhYOuN7tXUv9b7vGNjaT4nJCz90kmBpwfTEmuvNqpTvj80Z0zgBUwDqcYRmUQLoQdT93CPi9lJeRhqfMYsfY8lMpgF8-1AtQsu_adhxJKscRDQih0XbHCRgGjBg73yE8MWjCrTFVB1Lew7Hu2WUng57atmmnfV9SnH0dBuahVzHfBo4_cmIMv3s2Fzvv_fGqNltKgbMRPPejffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658080" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICOx2V3zXT-1ISsOcxFS4D9x_3mql9dgof2DX8_59WOLR12Ub3HWBeHaqNstjEA-wyXdhVykgjusgDtaSUvXwI72hcoqMuORl-P4UEZqwG4Dyt-sJZi4caJsAnq-QtGXJ8YlRK9uHHAG3cQZFFSjCPMe0jmfWgXzRtY1FF4UPcVIZx1BV7tLozl6XZhHep1-oBirXXTtMB2zo5n3ssEm4bjPBvC-gO1bfHNbVlRVa63pnTQKrmXJPmplgxFg0pAMnZQUv0cuVLWtUyV9uXP4oZ-6DKxuAZBfz2tc37cMDfvlryIHCB4XRmWY1bQ7Hq1Wzo3VWWcB47VaryElJ0-IaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی: سیاست‌ ویزایی آمریکا باعث تنش در جام جهانی است
مهاجم تیم ملی ایران در مصاحبه با ESPN:
🔹
اقدامات دولت آمریکا در رد برخی درخواست‌های ویزا و جلوگیری از ورود یک داور سومالیایی، به وجههٔ این کشور آسیب‌زده و باعث ایجاد «تنش زیادی» در فضای جام جهانی ۲۰۲۶ شده است.
🔹
در ۳ جام جهانی قبلی که حضور داشتم، همیشه وقتی وارد کشور میزبان می‌شدیم، حس صمیمیت و جهانی بودن فوتبال را احساس می‌کردیم. اما متأسفانه اکنون چنین حسی ندارم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/658079" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
احد عظیم زاده، مالک لاکچری‌ترین فرش دنیا را بشناسید!
🔹
روز ملی فرش گرامی باد
#فرزند_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/658078" target="_blank">📅 18:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658077">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یک زخمی و دو مفقودی در پی آتش‌سوزی نفتکش  سازمان تجارت دریایی انگلیس:
🔹
در پی آتش‌سوزی در اتاق موتور یک نفتکش، یک نفر زخمی و دو نفر از خدمه مفقود شده‌اند؛ این نهاد، هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/658077" target="_blank">📅 18:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658076">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jINc4OsV0f-eDPqgWAcuKhBLswKOvx9BNPkhSHKLeSIJZE94idAzyv6wwkqAohPVN0IIB-qXjQ-w_qyhv6jPNlEdm_QaYDcCK0cgzsNBMdsvAVPzOmq_5-qddPeGAoMvS_GHRhq-zdW7pu03B3vkcsy4o8INfAfloeguI1XHU4mXoUnPLPDnEaTMCEflZr6EQJg_A5tYyhH37op7cEaF6jhCeYzqppTiQCcMNJrLF0-ihZaXmCv-jADOEzdvKwGIrApJ3PapSu4qKO45ZiO3OfSdP839WaKf8fmY7WiS92fIZ3JR7dT9qzHS6cNlEnL-mFdr5ICMNpBGsvrSHHzJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابوزید بلخی، نابغه عصر سامانی و نخستین روانشناس
🔹
او از نخستین اندیشمندانی بود که میان بیماری‌های جسم و روان تمایز گذاشت و برای درمان اضطراب، اندوه و وسواس راهکارهایی ارائه کرد. او در جغرافیا نیز پیشگام بود و تصویری دقیق از جهان زمان خود به جا گذاشت. اندیشه‌هایش…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658076" target="_blank">📅 18:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
۵ کشتی حامل ال‌پی‌جی از محاصره دریایی آمریکا عبور کردند
🔹
بر اساس پایش هوش مصنوعی دریایی «ویندوارد»، پنج کشتی حامل ال‌پی‌جی که با ایران تجارت می‌کنند از محاصره دریایی آمریکا عبور کرده‌اند.
🔹
در حالی که ترامپ مدعی شده بود «هیچ چیز» بدون اجازه آمریکا عبور نمی‌کند، داده‌های ماهواره‌ای کپلر نشان می‌دهد چهار کشتی محموله خود را در هند و یک کشتی در پاکستان تخلیه کرده‌اند و صادرات ال‌پی‌جی ایران ادامه دارد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658075" target="_blank">📅 18:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سردار شکارچی: هر تهدید ترامپ را با تودهنی پاسخ داده‌ایم
سخنگوی ارشد نیروهای مسلح:
🔹
به‌هیچ‌عنوان در مقابل نظام سلطهٔ جهانی و شیاطین عالم، به‌ویژه ترامپ و نتانیاهوی خبیث، کوتاه نخواهیم آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658074" target="_blank">📅 18:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658073">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df010c4d4.mp4?token=nQuqdtqyI_giwI1cmL-8g6ffFkKWjN-I-K_QHvATuTGY7ZuvWD90cC5T-IltKEUhFUxTV1WaeaBh0iAmk3Y_0lxlw2qWe3UH7KOPcMrwhYZXgDvIg5VYeg2y9N8Zkilf8HVVNBideVzvhfh-UW_sdeCVrT8EbMW8RDj3plUTx6MDO1NO78y84gZImbg-yrEOSET6F7XDlnT7HDBmrGBkwLF69KcbP8KElbgVSaqiwBw6Phv1SNkFffZKfEJPPCvOmjOwA8YifSn4AWqcgYa2s0CS1mfOH9wBb4f2R4-4RaJY5yjZrNa3WulgreTXbD5WJyjXCP1b8SO0Oc7is_k_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df010c4d4.mp4?token=nQuqdtqyI_giwI1cmL-8g6ffFkKWjN-I-K_QHvATuTGY7ZuvWD90cC5T-IltKEUhFUxTV1WaeaBh0iAmk3Y_0lxlw2qWe3UH7KOPcMrwhYZXgDvIg5VYeg2y9N8Zkilf8HVVNBideVzvhfh-UW_sdeCVrT8EbMW8RDj3plUTx6MDO1NO78y84gZImbg-yrEOSET6F7XDlnT7HDBmrGBkwLF69KcbP8KElbgVSaqiwBw6Phv1SNkFffZKfEJPPCvOmjOwA8YifSn4AWqcgYa2s0CS1mfOH9wBb4f2R4-4RaJY5yjZrNa3WulgreTXbD5WJyjXCP1b8SO0Oc7is_k_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از نجات معجزه‌آسای یک مرد در تصادف زنجیره‌ای ۷ خودرو در آذربایجان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658073" target="_blank">📅 18:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم  نمایندگی ایران در وین:
🔹
شورای حکام آژانس با رأیی ضعیف قطعنامه‌ای سیاسی درباره فعالیت‌های هسته‌ای ایران تصویب کرده است.
🔹
ایران از حقوق مسلم خود کوتاه نخواهد آمد و به این قطعنامه پاسخ خواهد داد.…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658072" target="_blank">📅 18:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658071">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJWAUuDyWrjXggUA2O3qz5UzIPFZqmyojNHiAxFFqx3Vd_7jMBdfDODM32bjxVefEyqBy-Ia_DZiM0tQEcOjPnrucROn01ALaQYCbwK-kQcHTZyCM6VZrjiYqFdrDu5x5llmG2m7XBMZ0bVp4ghyEYPeg1ByjIgJk8bNilYK4nl-0PjCEm0612cDkWz0DPeWQ4pWdJkgl7fG9quAfyYg-lQwzMluQdIGlyfAd-2a38Qfq8A5k1jdBkS2NW_uwtmbSt_cevfExCC2XBZqO4xMfyZ2GXEoeu6S4Y2SHhLMgc_OhnrhycW2EYKAHO-kmizbebT8SY3NETpIU0VvPTLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 در راهه؛ تو آماده‌ای؟
هنوز سوت آغاز مسابقات زده نشده، اما هیجان در «همراه من» به اوج خودش رسیده!
فرصت رو از دست نده و از همین الان، جایگاهت رو در زمینِ بازی «همراه من» محکم کن.
⚽️
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
۳ کمک‌ هزینه سفر به عتبات عالیات در هر بازی تیم ملی
قبل از سوت آغاز، قهرمانِ پیش‌بینی باش!
👇
🔗
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658071" target="_blank">📅 18:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658070">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AINTvgvswRHasVBHL7hHQRglAXaVCw8J_A3yiObhaVt_XBosZJgyMQ6IlTAlhRAPhnDC6_W9uRWRZKi3-1FmM5ESLU3nxELsuS4LwizbhIkFjZPBy0H-jLNASUQyqlM2kehjbhZ3wX1iwgVm8l5z3U67GMXn-uC4qdAPpf3Tg-Vx4LzBkL8mkUJbt61hGqZBakBi30Swx97_lCnR0migQghqS9vSAmvb-vVysPNAt97O-C_lHpLvgQkTE4F1u1hYGT3zMzmOkPd6Gi5J57yzATYfXlBMfPAB5uI-pwUJ1FmjM91SLjc81Ua5eafc-_dPzkUpULEUFItb-9mhe0Cw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم
نمایندگی ایران در وین:
🔹
شورای حکام آژانس با رأیی ضعیف قطعنامه‌ای سیاسی درباره فعالیت‌های هسته‌ای ایران تصویب کرده است.
🔹
ایران از حقوق مسلم خود کوتاه نخواهد آمد و به این قطعنامه پاسخ خواهد داد.
🔹
این قطعنامه که با ۲۱ رأی موافق، ۱۰ رأی ممتنع و ۳ رأی مخالف به تصویب رسید، از ایران می‌خواهد سرنوشت تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده‌ای را که در این تأسیسات نگهداری می‌شد، به آژانس اطلاع دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/658070" target="_blank">📅 18:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ امشب سخنرانی اضطراری برگزار می‌کند
دونالد ترامپ:
🔹
امروز ساعت ۵:۳۰ عصر به وقت ساحل شرقی آمریکا یک سخنرانی اضطراری ارائه خواهم کرد./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/658069" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658068">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1RLa3dMZwhfg5Wkvr4IW7gj4aryyi_v_Un2j21BFUPIXaKEZKluGZhzr3YIWHD87D3J_LJmajE8-Dax4Sz8lwDselceO4Fq8Wigoq8_pK0YBvjkjAJtP584cWR0irHMGIAE6C-W-qJ3I6bvRDeoK85f1nW4pXbpk-8EbRZvi2ovG3gLx5Qfpzx_S0r0JIWaHQrPIBlqHRV1sw6l2NvNivOd5z3R1viiBxU-qfBhBa-rkBVmDnAtGQu84F6mjc3Gy9CLcaqVCdJS-z9GjRwutTfCQ0TJlQ9J7aUE_FLoG1DuLJ8zH0BX3sjzrC_8ObtLAyvGnpQm5WfZaK0m-Ipn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتان لوینز، روزنامه‌نگار آمریکایی: ایران در تمام طول جنگ یک دانش آموز را هم نکشت
🔹
ایالات متحده ۱۵۰ دانش آموز ایرانی را در ۱۰ دقیقه کشت. ایران در تمام طول جنگ یک دانش آموز را هم نکشت. چرا ایران به‌عنوان «طرف شرور» تصویر می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/658068" target="_blank">📅 17:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658067">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حمله تند کارشناس شبکه افق به صادق زیباکلام: زیباکلام لعنتی بیشترین نفع را از ساختار جمهوری اسلامی برده است ولی به رهبر شهید توهین می‌کند/ رهبر شهید ما هنوز دفن نشده است ولی زیباکلام به ایشان اهانت می‌کند و می‌گوید آن که مزاحم همه بود دیگر نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/658067" target="_blank">📅 17:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-text">🔸
روایت مخاطبان خبرفوری از بازار مسکن
🔹
ارسالی از البرز:
سلام وقتتون بخیر توروخدا صدای ما مستأجران روبه گوش مسئولین برسونید واقعا کم آوردیم هرساله چقدر اجاره بها افزایش پیدا می‌کنه مگه مامستاجرا آدم نیستیم که ی زندگی خیلی ساده برامون بشه آرزو.
🔹
ارسالی از مشهد:
با سلام از مشهد هستم شمارو به امام رضا به داد ما برسید اجازه خانه‌ها و رهن خیلی بالایی مگه چقدر حقوق میگیریم خرج خونه.پول برق گاز آب تخلیه چاه به خدا موندیم با دوتا بچه چکار کنیم تورو خدا یه فکری برای صاحبان خانه بکنین لاقل اجارهارو بیارند پایین که شرمنده بچه هامون نشیم
🔹
ارسالی از کرمان:
سلام تشکر می‌کنم بابت این کانال اطلاع رسانی فقط خواستم بگم به داد ما مستاجر ها برسید خواهش میکنم متاسفانه صاحب خونه ها خیلی بی انصاف شدن تواین شرایط که خودشون دارن می‌بینند.  آخه این انصاف نیست نمی‌تونیم هیچی بخوریم هر چی داریم باید بدیم صاحب خونه تو رو قرآن به داد ما برسید.
🔹
ارسالی از شیراز:
سلام خدا قوت.اصلا نظارتی روی قیمت اجاره خانه نیست مالک میگه میخاید این قیمت نمیخای خوش آمدید ، یه سامانه ای باید راه اندازی بشه که راه دور زدن املاک یا مالکان گرفته بشه ، مثلا اگر بیشتر از یه مبلغی بخان اجاره بگیرن ۱۰ درصد میاد روی مالیاتشون یه همچین چیزی،  لطفا شما که زبان رسانه رو بلدید این متن منو با یه اصلاحاتی که بلدید به عنوان یه پیشنهاد مطرح کنید . ممنون
🙏🏽
🔹
ارسالی از پرند:
سلام وقتتون بخیر  تو شهر پرند کسی نیست نظارتی کنه هر جور دلشون می خواد خونه رو میدن اجاره کسی هم نیست جلوشون بگیره ما تو چهار جنوب زندگی میکنیم سال پیش ۲۵۰  رهن نشستم الان املاکی به صاحب خونه گفته ۲۵۰ رهن اجاره بها ۱۶ ملیون مگه من کارگر ساختمانی چقدر در آمد دارم که ماهیانه هم کرایه خونه بدم هم خرج خونه خدا از املاکیای بی انصاف نگذره که رحم ندارن فقط به فکر جیب خودشونن  اگه قانونی باشه   درست وحسابی املاکی  حساب دستش بیاد ما مستا جرا اینقدر تو استرس واضط اب نیستیم میگن ۲۵ پر صد اضافه بشه به قرارداد ولی املاکی ۲۵۰ در صد میزاره روخومه ها ما شکایتمو به کی کنیم
🔹
ارسالی از اصفهان:
سلام وقت بخیرمن ازاصفهان هستم واقعاکسی نیست که به دادمامستاجرین برسه شوهرم بازنشسته است مستاجرهستیم مگه چقدره حقوق یه بازنشسته اضافه میکنن که اینقدر هم اجناس راگران میکنن وهم مبلغ رهن واجاره همراه خداکم آوردیم زیربار گرانی ورهن واجاره له شدیم آیاکسی صدای مارامی شنود مادرکشوری هستیم که همیشه ازهمه دنیاجلوتربودیم پس چی شده که حالااین همه بدبخت شدیم ممنون که پاسخگوباشید
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658066" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfvwxfXbTW3wIWwijilcaaLL34GWBY6k7OCRY-V1Sxx337OMdVNkxIj9xSg-LwwVSks46eq-ECh6g4Iy5c5EJ3VC0r1NjTr0-qt2L90sNJU1a9612ntQMzAV3NjpSYn0ouL53mz8YZiqb1j1IVSevIdpBa_i0Og08rh8qpU1CigpIJq9kkuH6MJclTPwOIfuCXodT7DqEdiJrw0p5T4u3SZzEinUjYXMZUMqcOivshTjvy6Bp_vR48t_NKfxwyEFVJ7KkGQcN68FhuEniCl7L2kRIVtp8qHixW9TndOeQya13j7OkEVf80BzBfE1SF_iCEyZ0rqz7uv1EC59s_PncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساحل فیتوپلانکتون، چابهار
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658065" target="_blank">📅 17:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
بقائی: آمریکا با پیام‌های متناقض به روند دیپلماتیک آسیب می‌زند
سخنگوی وزارت خارجه:
🔹
آمریکا با ارسال پیام‌های متناقض، تغییر مکرر مواضع و نقض‌های پی‌درپی آتش‌بس به روند دیپلماتیک آسیب می‌زند؛ ایران هرجا لازم باشد از دیپلماسی و در صورت اقتضا از توان نظامی برای دفاع از کشور استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658064" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تأیید خسارت در پایگاه نظامی «رامات دیوید» در پی حملات اخیر ایران
ارتش رژیم صهیونیستی:
🔹
در جریان حملات اخیر جمهوری اسلامی ایران، پایگاه هوایی «رامات دیوید» مورد اصابت قرار گرفته و دچار خسارت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658063" target="_blank">📅 16:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ارتش عراق: پرونده انحصار سلاح وارد مرحله اجرایی شده است
🔹
ارتش عراق از آغاز مرحله اجرایی الزام‌آور طرح ساماندهی گروه‌های مسلح و انحصار سلاح در دست دولت خبر داد./ ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658062" target="_blank">📅 16:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
«خانه صانعی» جان گرفت
🔹
عمارت شهرآرا، به عنوان خانه طراحی شهری و مرمت بناهای تاریخی شهر تهران، به کانونی برای گفت‌وگوی میان طراحان صنعتی، معماران، مرمت‌گران و شهروندان تبدیل خواهد شد.
این مجموعه علاوه بر اجرای پروژه‌های مرمتی، طراح و مجری پروژه‌های بزرگ در حوزه مرمت، مبلمان شهری، نورپردازی‌های شهری، طراحی فضاهای شهری، پلازاها، فضاهای مکث و همچنین المان‌های شهری در سطح شهر تهران است.
استقرار این مجموعه در خانه تاریخی صانعی، عملاً این عمارت را به یک پایگاه زنده برای تولید تجربه، آموزش و تبادل دانش در حوزه مرمت و طراحی شهری تبدیل کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658061" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
افزایش اعتبار کارتکس گواهینامه از دو به چهار سال
پلیس:
🔹
از ابتدای تیرماه مدت اعتبار کارتکس آموزش و آزمون رانندگی از دو سال به چهار سال افزایش می‌یابد تا متقاضیان فرصت بیشتری برای تکمیل مراحل دریافت گواهینامه داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658060" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJfIC_NI8xtYdLuQn5Gf07blU-_Z7jP97lOkKhQUypDD1h4_n3vVNom1DyVzt5WYr-tvr6BjxIxX8vzAkbY_XWwGu74VtNAFhCjkejcQp0y5GukLhXpuc_N1oJfKKntaxmeKfURXzHAjMqPRHPSA0TCncwRhsHLlnzNgzT3BHeKOQr9vNQNrZDcBYOkDC0KQXBUDqmXwRboFiDeSZ1xX4IwGhcFkY9PYzUxaBhQWpUIJMmIYD9h6le3tL8MwZYYIkQh5q2ZyD-R1hXWAYChU7PBQ_lVaYvdpVaK0G39yRjErplSyJf3y5BrIr62pEdXrR4DWWs05If4QpF9ODZobMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658059" target="_blank">📅 16:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بقائی: جام جهانی نباید بهانه‌ای برای آزار تیم‌ها شود
سخنگوی وزارت خارجه با اشاره به برخوردهای نامناسب با برخی بازیکنان و کادر فنی برخی کشورهای حاضر در تورنمنت در مبادی ورودی آمریکا:
🔹
فوتبال باید زمینه رقابت سالم و نزدیکی ملت‌ها باشد و جام جهانی نباید به فرصتی برای تحقیر و تبعیض تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/658058" target="_blank">📅 16:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سفر هیات قطری به تهران
🔹
هیاتی از قطر برای رایزنی درباره روابط دوجانبه و رویدادهای منطقه‌، وارد تهران شد.
🔹
قرار است در این سفر، افزون بر بررسی روابط دوجانبه و تحولات منطقه، درباره آخرین تحولات مرتبط با روند دیپلماتیک برای خاتمه جنگ تحمیلی آمریکا هم گفتگو و تبادل نظر شود./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658057" target="_blank">📅 16:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQZWJspkyirDvQ6kdiobwP5XUVff-zcLwjKZwncnrHMW5fHeQTEIvUoeqGzgM8jFmwIKBX5j6NSmbAC_mAxoScgsaxdvTXPySxKO49GcOcTmiqUUCGXBajEXTfw53qcH0iAgxEpElv38RMiJzeCP6gdWIImaXgXN5XqdAW2WhE8DbBPfV_nJ9crL4f4rUc2y1eFo7V41Z1h_lghYFyRzoES34LIDoRJc_aaolkpHiYS9ni5JfNmC-ehLasCnupJk2SGyQWf8jwNsLL1XEK1ZALdXFeouVbZv83nJZ_q9-pF_8xYPaQqzB6lBEmGo_sPstDgDo-6OfEmA4FshpBJxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سد منجیل پر از آب شد
🔹
به لطف بارش های گسترده اخیر سد منجیل نسبت به پارسال پر آب شده است.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/658055" target="_blank">📅 16:24 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
