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
<img src="https://cdn4.telesco.pe/file/gpgC7JP2ulAj13MLrXj5_iMYk0R6E2sfXqQmrBryg-Moud7_cW5P-adcM1F2PovnVR2fkS9QSNIzK7nNWCJRt1H4vBg4luNd7PxbbfwEmse8AlwHjbOZepFM_Uxw7qK02po_2PCnZcnFu9NDnGtwiXTBV2KRrn7TFnymmrokhtSimxXYwPxeGml6XxbXLPcZM3ouOXjzrlIYIXF-d4gN6C4em_vCwoC81tNBaJ_O3-bDfEY4x9iKkRU8U2J_lvymcr_QL6cbBTPLzoaULpDaMWjQGoueFhYKkSCL0h5X_d5BARCvexvZJU5FoWdXBcyxFdwk91UCL_7sZ5U4fmRxQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 22:33:11</div>
<hr>

<div class="tg-post" id="msg-128314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=bsqkgmS2ql4868xW6Dh-CD2CpGu6Ni_2D32QPeHSqw4_BkkBCoFPsJWq4ltCxVZ5rK7trCssy7a7Jd2-5FkLgnsHdscNERqJAyKoQg3gwO4rWQEKFyp3YBJgw9N_skl-DGPx7bOKM540pXF2JILtpbFdjhg-hFcCrZWw1GkiJG6T_l3akDZzpU0-we7iHj85_GIYGCMvZqS1LuDYwv_sLawuBZSlL_osNGQ4fosRh_IRrpdqkhinqSTOxKXlBkjGVOWKxVc8QNt8_jTku9jsVYPEQgSiz2hqz8ZZJBw0P8_OVTwy1Myv_dnXjUSQj0cTmOVFdUFk1ap3S8UNLC-_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=bsqkgmS2ql4868xW6Dh-CD2CpGu6Ni_2D32QPeHSqw4_BkkBCoFPsJWq4ltCxVZ5rK7trCssy7a7Jd2-5FkLgnsHdscNERqJAyKoQg3gwO4rWQEKFyp3YBJgw9N_skl-DGPx7bOKM540pXF2JILtpbFdjhg-hFcCrZWw1GkiJG6T_l3akDZzpU0-we7iHj85_GIYGCMvZqS1LuDYwv_sLawuBZSlL_osNGQ4fosRh_IRrpdqkhinqSTOxKXlBkjGVOWKxVc8QNt8_jTku9jsVYPEQgSiz2hqz8ZZJBw0P8_OVTwy1Myv_dnXjUSQj0cTmOVFdUFk1ap3S8UNLC-_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده اف/ای-۱۸ هورنت از پایگاه هوایی MCAS میرمار در نزدیکی دریاچه ریمرک، ایالت واشنگتن، در حین تمرینات دیروز سقوط کرد.
🔴
خلبان به‌طور ایمن بیرون پرید و سپس توسط یک معاون شهرستان یاکیما نجات یافت.
🔴
سرویس جنگل‌های ایالات متحده به آتش‌سوزی ناشی از لاشه هواپیما پاسخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/128314" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=e7euEu4Do4Pf8jiqcQ3wM6XfhLQdM89w4PlQBwEx9W5s-LxHuG5wjH_CM_2UAd1FsiOxxON5KD3LA-cSNoDdUJtUnJlr9meTZ7QRow18SvV23pWTPTJ5EK5QruUcbF2JIOHWXYBajWnspXEX8zzJEBr9QDBekV4Y9sG6diqNkFJiBJ5J2cbmosq-8Yz9IxARzhI6vhMjT4HGSZDqsI5mpu5XTqKQQrRRhU2ci5t9PuKcWnblcEs5E8EqIBhzU0t5il8-7qeyte5PBHp8beASg1E5g66mlDOs1gjOCdFoW-NiFrX3jXkbNckZmsioTBeXL5_3DKP9xTVzcy9DO91UOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=e7euEu4Do4Pf8jiqcQ3wM6XfhLQdM89w4PlQBwEx9W5s-LxHuG5wjH_CM_2UAd1FsiOxxON5KD3LA-cSNoDdUJtUnJlr9meTZ7QRow18SvV23pWTPTJ5EK5QruUcbF2JIOHWXYBajWnspXEX8zzJEBr9QDBekV4Y9sG6diqNkFJiBJ5J2cbmosq-8Yz9IxARzhI6vhMjT4HGSZDqsI5mpu5XTqKQQrRRhU2ci5t9PuKcWnblcEs5E8EqIBhzU0t5il8-7qeyte5PBHp8beASg1E5g66mlDOs1gjOCdFoW-NiFrX3jXkbNckZmsioTBeXL5_3DKP9xTVzcy9DO91UOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر صنعت لبنان: درحال پخش شیرینی
🔴
خبرنگار: «مناسبت چیست؟»
🔴
وزیر: «آتش‌بس»
🔴
خبرنگار: «گام‌های بعدی پس از آتش‌بس چیست؟»
🔴
وزیر: «از سفارت ایران بپرسید»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128313" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تسنیم: در صورت جنگ یا ترور در ایران و جبهه مقاومت توافق نهایی انجام نمیشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128312" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری /شبکه ۱۳اسرائیل به نقل از یک منبع: تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128311" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نتانیاهو:  توافق با ایران توسط ترامپ انجام شد، این تصمیم او بود و ما منافع خودمان را داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128310" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو: همانکاری با غزه کردیم با جنوب لبنان نیز خواهیم کرد،همانطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست حزب‌الله نیز در آینده نخواهد بود
🔴
ما در منطقه حائل امنیتی در لبنان باقی خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128309" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو:  من در انتخابات شرکت خواهم کرد و قصد دارم در آن پیروز شوم.
🔴
گاهی اوقات بین من و ترامپ اختلاف نظر وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128308" target="_blank">📅 21:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو: ایران به سمت دستیابی به سلاح هسته ای حرکت می کرد و ما توانستیم برنامه های موشکی و هسته ای آن را نابود کنیم.
🔴
ترامپ رئیس جمهور آمریکاست و من نخست وزیر اسرائیل،من مسئول امنیت کشور خودم هستم.من از منافع اسرائیل نه با غرور و خود‌خواهی بلکه با خرد و عقب دفاع می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128307" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نتانیاهو:  کسانی هستند که می‌خواهند دستاوردهای ما را کم‌اهمیت جلوه دهند، و ما به دستاوردهای بزرگتری هم دست خواهیم یافت.
🔴
ما استقلال خود را در زمینه تسلیحات تضمین خواهیم کرد و نوآوری‌هایی را توسعه خواهیم داد که به خیال‌پردازی نزدیک‌تر هستند.
🔴
من بر منافع امنیتی‌مان در روابطمان با ترامپ و ایالات متحده تأکید کردم
🔴
وضعیت ما امروز بسیار بهتر از هفتم اکتبر است و ما محور ترور را در هم شکسته‌ایم.
🔴
به وضوح می‌گویم تا خلع سلاح حزب‌الله،اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128306" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نتانیاهو:  ما نصرالله را کشتیم و از حمله به جلیله جلوگیری کردیم
🔴
ما کنترل مناطق کلیدی در لبنان را که حزب‌الله از آنجا اسرائیل را تهدید می‌کرد، به دست گرفته‌ایم
🔴
ما دکترین جنگ را تغییر دادیم و سد ترس را شکستیم؛ ما ابتکار عمل و غافلگیری را در دست می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128305" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتانیاهو:ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128304" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نتانیاهو:  ما خطر نابودی اسرائیل و ساکنان آن را دفع کردیم و آن را از ویرانی نجات دادیم. مبارزه ما هنوز تمام نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128303" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
🔴
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128302" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دلار 155000شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128301" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز گفت که خروج از لبنان بخشی از تفاهم‌نامه نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128300" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر اقتصاد: مبلغ کالابرگ دهک‌های پایین به‌زودی افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128299" target="_blank">📅 21:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اردوغان درمورد اسرائیل و ایران:
از ۲۸ فوریه، کاملاً روشن شده است که چه کسی واقعاً خواهان صلح است و چه کسی ادامه جنگ را ترجیح می‌دهد.
🔴
کسانی که تمام امیدهای خود را به ادامه جنگ در منطقه ما بسته‌اند، بدون شک از تقویت فضای صلح ناراحت خواهند شد. همانطور که بارها پیش از این انجام داده‌اند، همه تلاش خود را برای مانع‌تراشی در این روند به کار خواهند بست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128298" target="_blank">📅 21:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
🔴
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
🔴
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128297" target="_blank">📅 21:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e5df9e7a.mp4?token=oPOGEurB24z1PdfOCBP7zLUG87TGWDfRR3KK3DTzpVHlq7B_rF3HXNBrAR67rN5IPutsnckUufIIMpBU_o1a7ulz_zwPiPQ8x3x0lvgIHZB-znMN_RxmGFlt0lWNGQImmQAjIm2TNa-9IACNcjWPzUSDTdunVt6cbb944SUTIvOTDSo1AX27YIELx7XNoWpkfXEwBeUUaH73B8413CCA2C9dQwxb-u8SIdquvTM5BikAieVr_fVmZ2EGxySdm5OJ98mbVqhBXdr3p9xNL9wPKuRKXfub5GfXix2CWqXskUEcl6MxcJQe2AXDKke4Bj2Z-zmzgzzKUSjtl7UXCVdtXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e5df9e7a.mp4?token=oPOGEurB24z1PdfOCBP7zLUG87TGWDfRR3KK3DTzpVHlq7B_rF3HXNBrAR67rN5IPutsnckUufIIMpBU_o1a7ulz_zwPiPQ8x3x0lvgIHZB-znMN_RxmGFlt0lWNGQImmQAjIm2TNa-9IACNcjWPzUSDTdunVt6cbb944SUTIvOTDSo1AX27YIELx7XNoWpkfXEwBeUUaH73B8413CCA2C9dQwxb-u8SIdquvTM5BikAieVr_fVmZ2EGxySdm5OJ98mbVqhBXdr3p9xNL9wPKuRKXfub5GfXix2CWqXskUEcl6MxcJQe2AXDKke4Bj2Z-zmzgzzKUSjtl7UXCVdtXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی کامل در جاده منتهی به شهر حداتا در جنوب لبنان در نتیجه حملات اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/128296" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از منابع:
گفتگوی پرتنشی بین نتانیاهو و معاون رئیس جمهور آمریکا در مورد حضور اسرائیل در لبنان صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128295" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یک مقام آمریکایی به الحدث گفت:
«به زودی خواهیم فهمید که آیا تفاهمات با ایران می‌تواند به توافقی تبدیل شود که مسیر منطقه را تغییر دهد یا خیر.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128294" target="_blank">📅 20:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از مقامات ارشد دولت آمریکا: آماده انجام گام‌هایی برای آغاز کاهش تحریم‌ها علیه ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128293" target="_blank">📅 20:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به i24NEWS گفت: اگر می‌دانستیم که جنگ از نظر «عادت سیاسی» به این شکل تمام می‌شود، مطمئن نیستیم که ارزشش را داشت که وارد آن شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128292" target="_blank">📅 20:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpmb6-yuoT0mYYi9ayKZxfXz9SgNSiQvPEL9VSHGqiQzzCiz768sflZ-Jn3xMf4bSydCyBJ_HgUfHsVFHN8sZ1BZE1aMdePmZyjf6L0dugpmx16fCoTsB4pat8X7z6E4_eYSM_8gTSYu9f84Ah4N8fEm2KM3iCpG4L54D-e0inhaGjxezNJeEVCK4SYbOznRK7CQuDpH-biYkW9AANjOm_hqZ0SSeE56BgoruPBfDTEqohBsUb-ai6hUtU7C4zRPJriHOPCUxt7ou6yvEuLPj_7dY8z0vOxghaVqGiLJGEB0CJ0l_f2_TZtE8d2PgCQUEHF1hIFX45uMlS8k4N7Vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس آمریکا در کمتر از ۲۰ دقیقه ۱ تریلیون دلار به ارزش بازار خود اضافه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128291" target="_blank">📅 20:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiJdeveJq6RtaA-4KuGrOlNUOjoYwO2CW32XLK5usfF1DyrFKJ-whuyUJnTkPnt85ydJeuUIuF_j_Tpz4JLqV5XKZp53KU9PaXoROeInvGUt15VXSuuly8jz68Ult3iMFs9G65hm64uJRxapG2z4jIyiKUvoXss9nfoqKdeumVtA-yy7s9l77B42MTUgEHQoPNDT6OU74GXMnIUWQTfbqtmYsTHZk35DH0n_eHEvUyADYMGaJcjvfvxD-gmoRNU0sBZJCcqMa0d5vKazV8m6lL5YNewQQ1ixRHJVtY3en0nXVOYdWo3psRrAOP__zVQRdwRjLRKpEjOLLESvqmwT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvbnWbhI0ymOd-1TJKg7xiR45qC03JtX6KgyonzmydY4FTmUIr34O50NfcNfNaFiiPK1CfIyRboIuWIHhv1xi8nSIC83yPTztpFIGbtWkZX-O0bV2SgXxtEDqR1PJ0NFS8XvKUbOEU3YtuX8SpBF9ybrRFK_Cp7TCFk0hN5Ow3G7ExDyV_h6GVq0ivHX8ufAIxz7pNw2FOaKJsn0mhF813K_zHMSYOUAhr604wQhnFPwNsX2BAryUEOW0Qabp-TWV5Z3JQHrZJRnMtJslSSzbjZca08y5m9I_QHjKJzHMe-5-44hlglC6k3pe1fYFVLH95bXvf5lf_V5oKVrKtv5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY6M6K_P1PfUUDgZHyZ-vg8iQwp4XSjRPX2TwgBhQvs_TEJ4csT2XSLLS5rDW3w5vAoAgrObtzwuWKwF0hi02U8rL17LUUIhL6CbAKc27bWjAtaGRcuYwEAI5bNn7uiOogl4L7whtOLY9HTWfwgubyAwqYUXK0zRDa7sHJdGf5vS8rQLbwJbjEJ3xVM20FAAuiTUmRuJL_6-Ak_hf6r1YMxzDPgLHmS9NyJ70M_9eMR_HOB0xIZJPo5jZ3FfHcw7MRyOY8fL1Q5fsD7snF-njGw-Rdr0gLdAn-4jEmiB20ZXc9DRZQ1u4DVjrBaOtGXIVDa5fsh_qzuuL6leXZg3ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از سرجنگی عمل نکرده موشک کروز BGM-109 تاماهاوک در نزدیکی ورامین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128288" target="_blank">📅 20:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مکرون: ما از ایالات متحده، ایران و عمان در بازگشایی تنگه هرمز حمایت خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128287" target="_blank">📅 20:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: نتانیاهو هم با توافق موافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128286" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45b122799.mp4?token=Mx_nlKYC7u_7wqDde9FnRJ2T8RXEcupZtfN-OVjMiXl9hpcp9NLazEjq1FqvL3JXnkXkiVsp5aoINcQJ3hxGBshkbuCFo0vuJVcNcKljbhl98y6Lz4FJV4RnEVhJoJ2KB3-3lPY5HiyjS7y0d7INz7snSSlTXWV3y0aJLoTMwbTywt_3L1sRbSz0KiFBucR02_CnMI3gFwAYteLptjXNN65WBKxUEuLdvOJRIBEUUjai0wSb6KKKlbD56QT2FjJubpr5gu3bIFLuYOgI1IuyPUMDPj08Bqv0TfnGmCOR-j7igwy648OuKZqxRtSM1OI7p3CwxRCDD5POh4Ny5nrbGyQBc_TbXoEErwPEN4RKIEZbSbWmlTidaehjvH-_lA7Mepwlwq-wxYFYUgKgLA8_ih8D55PmrwluwJ80e27ZH5sBinofv3_0unSwufDRTHpWiQoz3idZ-flvccO_YggXqVH1fjXjlYbK3SldYg3Oka5Wvz51BecS7lB4XQrnBmaKSFCnDvcm_npbFI5kjdVXXpwuROtq8mJUtXdKg1yi1Dai7UuN0heu_iJrHTp7Ak-oHE2eF6_Eg1dG3hF-ZG6PWIuPSbl8ikik5tiSald25xv0J1VKqfBj--mH7Pq9N9VHov1QZfVADkhpHJrCT0thidYi__Tb0E_QJr9FN17BUcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45b122799.mp4?token=Mx_nlKYC7u_7wqDde9FnRJ2T8RXEcupZtfN-OVjMiXl9hpcp9NLazEjq1FqvL3JXnkXkiVsp5aoINcQJ3hxGBshkbuCFo0vuJVcNcKljbhl98y6Lz4FJV4RnEVhJoJ2KB3-3lPY5HiyjS7y0d7INz7snSSlTXWV3y0aJLoTMwbTywt_3L1sRbSz0KiFBucR02_CnMI3gFwAYteLptjXNN65WBKxUEuLdvOJRIBEUUjai0wSb6KKKlbD56QT2FjJubpr5gu3bIFLuYOgI1IuyPUMDPj08Bqv0TfnGmCOR-j7igwy648OuKZqxRtSM1OI7p3CwxRCDD5POh4Ny5nrbGyQBc_TbXoEErwPEN4RKIEZbSbWmlTidaehjvH-_lA7Mepwlwq-wxYFYUgKgLA8_ih8D55PmrwluwJ80e27ZH5sBinofv3_0unSwufDRTHpWiQoz3idZ-flvccO_YggXqVH1fjXjlYbK3SldYg3Oka5Wvz51BecS7lB4XQrnBmaKSFCnDvcm_npbFI5kjdVXXpwuROtq8mJUtXdKg1yi1Dai7UuN0heu_iJrHTp7Ak-oHE2eF6_Eg1dG3hF-ZG6PWIuPSbl8ikik5tiSald25xv0J1VKqfBj--mH7Pq9N9VHov1QZfVADkhpHJrCT0thidYi__Tb0E_QJr9FN17BUcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به مکرون: شب گذشته بسیار دیر با شما تماس گرفتم تا تبریک بگویم. در دسته‌بندی سنگین‌وزن، یک بوکسور فرانسوی پیروز شد.
🔴
نمی‌دانم — شاید این حتی مهم‌تر از جام جهانی باشد. برای برخی افراد ممکن است این‌طور باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128285" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6h7egtjPhVmYfWw_Xnv_ahlV4DF_caB4oaGSm1MDENYvnHyskPtRrlgBlWo7ecwRy7ySanArpy_qguqrYvTgMW2zXzLYhQQEfNM4YTAkurSdIg4XuZnAMToQE0rN6IdTrBBKNaXwhuJ6KMmrA_hxHX26S0eyj0zP04xGh6ISme1Ijps9vo7Znye7pSVUFE14VBgwgbHP94eF6sKS7FbYAb-M52rULWX8KA_teVV-Od3ubVn5B3LFfVezzJx1p7zJxfHoSSGnoFXiTY431SGH4DjGg9wDzuRAtsLsVSuQcSpbj959_Py0QyrGFX07qsKGlC1r1zuZDJXL-r0nhmF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پارلمان مجارستان اصلاحیه‌ای را تصویب کرده است که محدودیت هشت ساله برای دوره ریاست جمهوری نخست‌وزیران اعمال می‌کند و عملاً بازگشت ویکتور اوربان، نخست‌وزیر سابق، به این سمت را غیرممکن می‌سازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128284" target="_blank">📅 20:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01951dffa5.mp4?token=sKuJsSgwEPc8vmwsU7qPTsrlAsbCMv_7_8-OKrmgXkVw0MV815nvfOu3AtW80FkFihXnFBBFNMGJrkkp4YrONLnL2izeuKLZoHEyE_CEm0vvoiqvSWwNZ1Sd9lgSV13C0kaWufMNlxqe9LqgYrjOEwfsyUOxyEZBl7X0u5iMNMJzfP5AKyd42KL1BeRNYsSBK6SiWsAz1IHWgPV1k26DHiLVWuEdAYpDE6TEmC4FPjTurzHp4kPeZzddY_O2A_y6J_aPPHHSbFp8b22bWm1_JUeYCxYcBT_4WcNWMb9NtPJOEX--cjWqzZ7b1H-F2l7Bdyasx7G1lFiJFxPKf_Du_hIY-1SvaOQweMK383jalNR7wp_CX44uqCiK92uu3u75sSqd-Cq5s2ODRUjNu7R5A5Q4_InvUoijxvUM4g9MpjaiqO-MnAqw04UhOovivbSjr8AfgpuZwXURIwZyeXy2ilPj3irKsnRgB4MWJkYU_LnZPo1SgheP2CBp25WySX-GNtIxo6q4Lb2LbezNyd4Q5_gtR_--BOWVF9e-aRVqby3dHO8lfGAgvzOy_CyX9lmW7s959SyQMg0MBnhr5O_Uu_5GA3GEv2CqqLY-y6XByk_iCTbfyDeDAUaxrTl_5W0ZYpog5dPKjNQRWhOvyMMzUY0cH4-IJvXB8VDnaa677MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01951dffa5.mp4?token=sKuJsSgwEPc8vmwsU7qPTsrlAsbCMv_7_8-OKrmgXkVw0MV815nvfOu3AtW80FkFihXnFBBFNMGJrkkp4YrONLnL2izeuKLZoHEyE_CEm0vvoiqvSWwNZ1Sd9lgSV13C0kaWufMNlxqe9LqgYrjOEwfsyUOxyEZBl7X0u5iMNMJzfP5AKyd42KL1BeRNYsSBK6SiWsAz1IHWgPV1k26DHiLVWuEdAYpDE6TEmC4FPjTurzHp4kPeZzddY_O2A_y6J_aPPHHSbFp8b22bWm1_JUeYCxYcBT_4WcNWMb9NtPJOEX--cjWqzZ7b1H-F2l7Bdyasx7G1lFiJFxPKf_Du_hIY-1SvaOQweMK383jalNR7wp_CX44uqCiK92uu3u75sSqd-Cq5s2ODRUjNu7R5A5Q4_InvUoijxvUM4g9MpjaiqO-MnAqw04UhOovivbSjr8AfgpuZwXURIwZyeXy2ilPj3irKsnRgB4MWJkYU_LnZPo1SgheP2CBp25WySX-GNtIxo6q4Lb2LbezNyd4Q5_gtR_--BOWVF9e-aRVqby3dHO8lfGAgvzOy_CyX9lmW7s959SyQMg0MBnhr5O_Uu_5GA3GEv2CqqLY-y6XByk_iCTbfyDeDAUaxrTl_5W0ZYpog5dPKjNQRWhOvyMMzUY0cH4-IJvXB8VDnaa677MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لبنان
:
ما می‌خواهیم ببینیم آیا می‌توانیم مسئله لبنان را مرتب کنیم، زیرا به نظر می‌رسد هرگز به پایان نمی‌رسد.
🔴
و این نسخه کوچکی از کاری بود که انجام می‌دادیم. اما نباید سخت باشد.
🔴
حزب‌الله. ما باید کمی با آن‌ها صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128283" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرنگار
:
آیا قصد دارید در مراسم امضای روز جمعه شرکت کنید؟
🔴
ترامپ:
خب، بستگی دارد. جی‌دی برای آن می‌آید — در اصل قرار بود او این کار را انجام دهد. احتمالاً تا آن زمان من رفته‌ام.
🔴
ما تا دیر وقت می‌مانیم، بنابراین ممکن است درگیر شوم و ممکن است نشوم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128282" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: احتمال دارد جمعه حضور داشته باشم و با ایرانی ها دیدار کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128281" target="_blank">📅 19:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ در ادامه: از اینکه مجبور شدیم دو شب دیگر به حمله ادامه دهیم، احساس بدی داشتم. و فکر می‌کردم برای بار سوم هم همینطور، اما ما قبل از آن توافق را انجام دادیم.
🔴
فکر می‌کنم اتفاقات خیلی خوبی قرار است در خاورمیانه رخ دهد.
🔴
قیمت نفت در حال سقوط است و بازار سهام مثل موشک در حال افزایش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128280" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ما می‌خواهیم ببینیم چگونه می‌توانیم مناقشه در لبنان را حل کنیم و باید در این مورد با اسرائیل صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128279" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بدون عوارض بازگشایی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128278" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: کاهش تحریم‌های ایران به رفتار این کشور بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128277" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: می‌خواهم یادداشت تفاهم با ایران را منتشر کنم زیرا سندی مهم و قدرتمند است و ما به زودی آن را منتشر خواهیم کرد
🔴
تنگه هرمز پس از جمع‌آوری مین‌ها به‌طور کامل باز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/128276" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: جی دی ونس در مراسم امضای تفاهم‌نامه با ایران شرکت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128275" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: ما خواهان روابط خوب با ایران هستیم و اگر این اتفاق نیفتد، به جنگ باز خواهیم گشت. امیدوارم این اتفاق نیفتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128274" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: ما خواهان روابط خوب با ایران هستیم و اگر این امر محقق نشود، به جنگ باز خواهیم گشت و امیدوارم این اتفاق نیفتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128273" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: توافقی که اوباما با ایران انجام داد، این کشور را قادر به ساخت سلاح هسته‌ای می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128272" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: ایران سلاح هسته‌ای نخواهد داشت و من با این موضوع موافقت کردم. این اصل موضوع مناقشه بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128271" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: توافق با ایران به نفع منطقه خاورمیانه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128270" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: ما با ایران تفاهم‌نامه‌ای امضا کردیم و تنگه هرمز تا حدی بازگشایی شده است
🔴
تنگه هرمز روز جمعه به طور کامل باز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128269" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
معاریو: اسرائیل از توافق میان آمریکا و ایران شوکه شده است و به‌تدریج در حال از دست دادن اعتماد خود به ترامپ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128268" target="_blank">📅 19:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی: جزئیات توافق با ایران ظرف یک یا دو روز منتشر خواهد شد و مذاکرات پیش رو بسیار مهم خواهد بود.
🔴
مذاکرات فنی اواخر این هفته آغاز خواهد شد.
🔴
ما نمی‌توانیم به ایران اجازه دسترسی به دارایی‌هایش را بدهیم یا اگر از آنها برای حمایت از تروریسم…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/128267" target="_blank">📅 19:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9573421eb8.mp4?token=CsJDkPOoBsWdO6ZeOzqgcze605iVCi_V3dcBYki3NJ4fqUUc8vGH8_NtR5XVZeKtPAPqvVUoYguWJjvfjSWRYEq71rWU1N__g2tbqYOjTFarH7WK9hzQREngcIEwIgBzTZEvWut5DOIWJi2EheLKlt8a5OQpm1pCHP5hxZd8i1hC6BSeJ8G1wwaURDceNNcKTwnI4LHlo8nMHqMOS-L3zR-Hh04aw_GsONMBVPbVOBtdkfuydLabhZlNPsbWn66eRv7ABfL8EX72Kq8BkhCHC8A9M-YgnazBZRogrBj0BP64zFXcVX5ViOrGL02ZC_lVf0ljvYb-5H5IEgxjkJeYfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9573421eb8.mp4?token=CsJDkPOoBsWdO6ZeOzqgcze605iVCi_V3dcBYki3NJ4fqUUc8vGH8_NtR5XVZeKtPAPqvVUoYguWJjvfjSWRYEq71rWU1N__g2tbqYOjTFarH7WK9hzQREngcIEwIgBzTZEvWut5DOIWJi2EheLKlt8a5OQpm1pCHP5hxZd8i1hC6BSeJ8G1wwaURDceNNcKTwnI4LHlo8nMHqMOS-L3zR-Hh04aw_GsONMBVPbVOBtdkfuydLabhZlNPsbWn66eRv7ABfL8EX72Kq8BkhCHC8A9M-YgnazBZRogrBj0BP64zFXcVX5ViOrGL02ZC_lVf0ljvYb-5H5IEgxjkJeYfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فکر می‌کنید تفاهم‌نامه ایران و آمریکا طولانی‌مدت و دائمی شود؟
🔴
وزیرخارجه لهستان: ان‌شاءالله!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128266" target="_blank">📅 19:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی: جزئیات توافق با ایران ظرف یک یا دو روز منتشر خواهد شد و مذاکرات پیش رو بسیار مهم خواهد بود.
🔴
مذاکرات فنی اواخر این هفته آغاز خواهد شد.
🔴
ما نمی‌توانیم به ایران اجازه دسترسی به دارایی‌هایش را بدهیم یا اگر از آنها برای حمایت از تروریسم استفاده کند، آنها را آزاد کنیم
🔴
نیروهای ما استقرار فعلی خود در خاورمیانه را حفظ خواهند کرد و هرگونه کاهش نیرو پس از امضای توافق نهایی انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128265" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ارشد آمریکایی:
ترامپ و ونس از طرف امریکا و همچنین قالیباف از طرف ایران این یادداشت تفاهم را امضا کردند.
🔴
این توافق، بازگشایی فوری تنگه هرمز و لغو تحریم‌های آمریکا علیه ایران را تصریح می‌کند.
🔴
ترافیک در تنگه هرمز از همین حالا شاهد افزایش قابل توجهی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128264" target="_blank">📅 19:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4Nzdvn0bhw2w15jLwdi7jsEv4iKp7TEAwG2PKf8q2_-gS2qwJM1350KWxbpqjVL06b_9Cv12T2ue78bDZIaReSJnoPSDAig0sxRHPVUbjmcll3MMiXpOeLD85hCzd5syZpJZTpZmtoK8Odq45TjA3YzK6X2CiSavfmKZaww6ap8f52dGil1BV9OgJ9td1b7xusk2fk6sUO7taRcPPL5yywhZJmSbJ0tfmQkFyC-IIbVeT2jH6DiCPsE33gtYND6ScOTqLHqKa4famWCVDXvyMXPvpw-l9n_DQOdDuGUrRZpFQA6UYPxVlNe7t0zRMJGVnf8C_BScUpES9vTG3EaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف : ایران گامی بلند به سوی پیروزی نهایی برداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128263" target="_blank">📅 19:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحارونوت:
اهدافی که بنیامین نتانیاهو برای توافق با ایران تعیین کرده بود، در یادداشت تفاهم میان آمریکا و ایران جایی ندارند و به نظر می‌رسد در توافق نهایی نیز محقق نخواهند شد.
🔴
این اهداف شامل خروج مواد غنی‌شده از ایران، برچیدن زیرساخت‌های غنی‌سازی، محدودسازی برنامه موشکی و پایان دادن به حمایت ایران از متحدانش در خاورمیانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128262" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عراقچی: روز جمعه احتمالاً در کشور سوئیس دیداری بین روسای هیئت‌های دو طرف انجام و تفاهمنامه بین ایران و امریکا امضا شود، سپس اولین دور مذاکرات بعدی برگزار شو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128261" target="_blank">📅 19:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb39df108.mp4?token=BDsGU_VbkUd23lRyq-pZoXRsu1J-gtbqsp7c9ZaENg8cHHadEk_QOvMVxuF3766nFiXqb3JOYu-Q3sZRZjW7hqsBKqp0JZw3ElXbx98XmfFYjiz-njD0dxSNqCVy514re_u5oDmvHJ2_bXJfvOzNkJO57QRePatRbUXkjVK_Ij7ciMblBcfSgWhLjB3AkxIw8QmyEsaPxBMUyTyr9YlvrZz9kqvokfyL4_4Qz_9LSc6351eJM3OT-lJNa0Tj8l6QJ-2CE537Oi-TEmfnxDTSPDEed9fj7DW47VHxhP_M4pexpgYfEGcpdVsx1Bda4tIJtcflMe6jZB-rC14BSyOfrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb39df108.mp4?token=BDsGU_VbkUd23lRyq-pZoXRsu1J-gtbqsp7c9ZaENg8cHHadEk_QOvMVxuF3766nFiXqb3JOYu-Q3sZRZjW7hqsBKqp0JZw3ElXbx98XmfFYjiz-njD0dxSNqCVy514re_u5oDmvHJ2_bXJfvOzNkJO57QRePatRbUXkjVK_Ij7ciMblBcfSgWhLjB3AkxIw8QmyEsaPxBMUyTyr9YlvrZz9kqvokfyL4_4Qz_9LSc6351eJM3OT-lJNa0Tj8l6QJ-2CE537Oi-TEmfnxDTSPDEed9fj7DW47VHxhP_M4pexpgYfEGcpdVsx1Bda4tIJtcflMe6jZB-rC14BSyOfrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌ پلیس راهور :  صدور گواهینامه موتورسیکلت برای بانوان داره اجرایی میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128260" target="_blank">📅 19:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شرکت مخابرات سوریه به سانا اعلام کرد که یک کابل زیردریایی بین‌المللی که طرطوس را به اسکندریه مصر متصل می‌کند، در نزدیکی ساحل طرطوس خرابکاری شده است.
🔴
این آسیب باعث اختلال در بخش قابل توجهی از ظرفیت اینترنت بین‌المللی سوریه شده و خدمات اینترنتی ضعیف‌تری را در چندین استان به دنبال داشته است.
🔴
شرکت اعلام کرد که تیم‌های تخصصی برای تعمیر کابل اعزام شده‌اند و هشدار داد که بازسازی کامل خدمات ممکن است به دلیل پیچیدگی فنی تعمیرات کابل زیر دریا زمان‌بر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128259" target="_blank">📅 18:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128258">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3f87619.mp4?token=icmo0Fq0czztUB4BXIePajLwhD-4IAXgJagtiKHmWj4AisO_PlHgdim0xG_muh5cPIhmHD8Rej35swR7VaJNrYExABzQzg8dpl0Qs04Zg4UQax3NoPQHCqIH_9T5D4P85677lClNxIcTHKQk_qhithcqMSAU4N-HRmR1Qhl8cIdmFofI2rIY0lupuDQ2fsWkrLesXqtqpwcU5SrSxSIJDR3TcLHBhnz3YrjSk9tLXYEee-_Zl6bK2vKRPVQYKuxNlxvy45aKX_T18COAASQl0KoO9P1SmkvdKth83KutNLZW7BkPtMezYNEN-hiwq3DCCWd8zflwrjAl69sGhoKRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3f87619.mp4?token=icmo0Fq0czztUB4BXIePajLwhD-4IAXgJagtiKHmWj4AisO_PlHgdim0xG_muh5cPIhmHD8Rej35swR7VaJNrYExABzQzg8dpl0Qs04Zg4UQax3NoPQHCqIH_9T5D4P85677lClNxIcTHKQk_qhithcqMSAU4N-HRmR1Qhl8cIdmFofI2rIY0lupuDQ2fsWkrLesXqtqpwcU5SrSxSIJDR3TcLHBhnz3YrjSk9tLXYEee-_Zl6bK2vKRPVQYKuxNlxvy45aKX_T18COAASQl0KoO9P1SmkvdKth83KutNLZW7BkPtMezYNEN-hiwq3DCCWd8zflwrjAl69sGhoKRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، برای شرکت در نشست سران گروه هفت (G7) وارد شهر اویان-له‌بن در فرانسه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128258" target="_blank">📅 18:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128257">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو تا چند ساعت دیگر سخنرانی خواهد کرد و این اولین واکنش رسمی او به اعلام توافق پس از ساعت‌ها سکوت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128257" target="_blank">📅 18:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128254">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6cALD0lTcXQtEDEyUWdJGNnAnirJK5gib9zu98b4KstURIJHdGtxlYrk7KjQE42QW1CMN0DCd85tNncg4hftK_Ou2Qz7Suig1Jrynr0E3PyhEDB2ClIlJCVVxM_fLYvRqLG36t4rulFS2hphIxcnCrVz5Ln9nZeyb7ryZH_jasCzxltpgkGnE6sGNNClVw_zAC6kae9NeQI7r5dZObZyJt4SFF5lgbwd9alYpFbz1hYLMsjRYWrSedoNtD63VyTVLORsP-9BIyKCwNlUd77yFZii8WOvlEP5J6PL76XH9pfQuQgT5BatVvmmoli8jNTEYUCgrpfuvnLp1yInkARLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5_92I2Zj1SLeqrTqeMTEhthoUtK6HZbEZI9eDavEkku29SWR5Hdvuoc9WoFeVIskjcjMZLMMkpRIjWrOlesi7yfdIOIdPDOHLaCCDDKoUj2CLMX19EFnkb_9wlSaXQXwWPAlAN1mYn_XshTiIycHd0cM9FlCltpYzAyDcaAVGR2_RC0S6GCVnplHyoUPAMbDqsn_cWuLDGa6KyGV7LfsN8z5y8XMyMYD__R3-uwbUFPjEOqwo8d7Qf3_QUh2lDPwzQW7CtIc1PkdhjVeixXmw1Iodz-1Ib5QAJO7TA0Mj1_6GI3q6taHoT_wLXjR5kbJuYsmNxfF7iWtWumMUW2bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7b34be62.mp4?token=XMbSDwpbqiNNqW1Yv-Z86vcs_zbjRsb2U8ZyNiXylLz0KNpHN3st_D5f-u4NQyxA39OvnNIqKBnbzuQ6CnhjJuaX7iR3EYPgBt8GNerze5AdGD-JMVFniFAOa2FqR9_M8TXakYYg6d6pSN-_nFvRHbKmNGO6lLs_oZ9OMXNXLW1UrmgBHRgvY6_IvNh3NIkZ90XdubJQVMkH5ldWD4UaGw0zhlZrdyFscqpIbCwCnmAN7ofGHblHhIf2XrQ8K8eZerjA2oRpqJQwe4geY3ws8NJZ1lgpKpzO2Kx0zfFI65144LVjPfkUY21vZfjm2eUeAOzPgtx2nPm2NfwMwl2PlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7b34be62.mp4?token=XMbSDwpbqiNNqW1Yv-Z86vcs_zbjRsb2U8ZyNiXylLz0KNpHN3st_D5f-u4NQyxA39OvnNIqKBnbzuQ6CnhjJuaX7iR3EYPgBt8GNerze5AdGD-JMVFniFAOa2FqR9_M8TXakYYg6d6pSN-_nFvRHbKmNGO6lLs_oZ9OMXNXLW1UrmgBHRgvY6_IvNh3NIkZ90XdubJQVMkH5ldWD4UaGw0zhlZrdyFscqpIbCwCnmAN7ofGHblHhIf2XrQ8K8eZerjA2oRpqJQwe4geY3ws8NJZ1lgpKpzO2Kx0zfFI65144LVjPfkUY21vZfjm2eUeAOzPgtx2nPm2NfwMwl2PlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آتیش سوزی آتش‌سوزی تو میدون تجریش، تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128254" target="_blank">📅 18:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128253">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
براساس گزارش‌های اولیه، یک نفتکش در آب‌های ساحلی یمن هدف قرار گرفته اما تاکنون جزئیات بیشتری منتشر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128253" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128252">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: نگرانی و عصبانیت اسرائیل از توافق،  نشانه‌ای روشن از موفقیت و پیروزی ملت ایران است و به فضل الهی این مسیر با اقتدار ادامه خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128252" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128251">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی مجلس با اشاره به اجرای آزمایشی انتقال سهمیه کارت سوخت به کارت بانکی از تیرماه، گفت:با اجرای این مصوبه، هیچ تغییری درمیزان سهمیه و قیمت سوخت ایجاد نخواهد شد و مردم از این بابت نگرانی نداشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128251" target="_blank">📅 18:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128250">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پزشکیان: تیم مذاکره‌کننده‌ای که برای امضای توافق اعزام خواهد شد، به هیچ عنوان از چارچوب‌ها و سیاست‌های تعیین‌شده از سوی رهبری عالیقدر عدول نخواهد کرد و تمامی اقدامات در چارچوب منافع ملی و خطوط ترسیم‌شده نظام انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128250" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128249">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیویورک‌پست: جمهوری اسلامی باید قدم‌های عملی و مشخصی برای کنار گذاشتن برنامه هسته‌ایش برداره؛ در عوض، آمریکا هم به‌صورت مرحله‌ای تحریم‌ها رو کاهش می‌ده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128249" target="_blank">📅 18:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کمیسیون اروپا: توافق تفاهم نشان می‌دهد دیپلماسی نتیجه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128248" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128247">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بحرین از یادداشت تفاهم میان واشنگتن و تهران استقبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128247" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128246">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
🔴
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
🔴
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128246" target="_blank">📅 18:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128245">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
بدر البوسعیدی، وزیر خارجه عمان، در پستی در شبکه «ایکس» گفت که جامعه جهانی باید از تفاهم حاصل‌شده میان ایالات متحده و ایران استقبال کند و از همه کسانی که در تحقق آن نقش داشتند تشکر کرد.
🔴
او این توافق میان واشنگتن و تهران را پیروزی دیپلماسی و منطق سلیم توصیف کرد و تأکید کرد که در زمان مناسبی به دست آمده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128245" target="_blank">📅 18:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی خودرویی را در کفر تبنیط، جنوب لبنان هدف قرار داد و راننده را کشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128244" target="_blank">📅 18:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128243">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4zlMS7NiEqoLzSqUBomDBnMn6tm_yJwKo5KJN5Zrl_b2oxA20_0wJVH9-McQAfRiTS_SDeKCieul1fXNK3RSWEYEYkUVAknw064WnrObdkdjySURldxWzUgO3SPsi32DR3JG_CB2md1MSCbRGKM58LfTxb35V6ibnUwHabHhxEJwvUDcmYXF1nzB2juoAoZJTwABHPk5qMkKCmxpsTLb5yq7E-_EWBJAPJOo3HpF03Glfbxi0h9w6Uh6BKTHrrgZvtBuN2TDjelO7z8-w5cwkK1pol_DjbIJiy2V-d1uWp2mrahd2HvMiy8uW4bJcHYUT4QEZx2i17sLSU2tG2d5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
🔴
آمریکا را دوباره بزرگ کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128243" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128242">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز به نقل از ارتش آمریکا: محاصره بنادر ایران همچنان ادامه داره و در انتظار تکمیل توافق با ایرانه که قراره روز جمعه انجام بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128242" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128241">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1QIcq_4wlnXkrGBEIWwNW9xkF59nsAvA_D-8xM_9FHhLA-eyRO88i8_CD3nGwFdmuLq0ClEpswJzSOU5DngcviqIBVcD-SrUGlahJ3zZqPq3cxdezlmSXIOWwifPZozTYuaZZ5ngKxtPoG_AoEqLqIeo3CN3SHrRzGb3-fOzN7aOFsKCIrzobtwZXjjaei-nz4_SOpsowiw_1BuSfbU0KtZ4K3vZ2QqlS-ERXmLV_qW7Nd9H7ZJWlG922oO3_bNp8Eb92KpsLwVvyvkIjEoGmYPOeFGHJ-yKc9tCkFyDs3gW3rdHxclUhhmQIm9ojL0ahBmBBrpiUbJOeIL25D9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان هنوز جنگنده‌های میگ-۲۹ باقی‌مانده خود را به اوکراین تحویل نداده است، زیرا مذاکرات در مورد انتقال فناوری پهپاد اوکراین هنوز ناتمام مانده است.
🔴
سزاری تومچیک، معاون وزیر دفاع، گفت که لهستان به عنوان بخشی از توافق، خواهان دسترسی به تخصص پهپادهای میدان نبرد اوکراین است.
🔴
در صورت نهایی شدن انتقال فناوری، ورشو آماده ارسال این هواپیما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128241" target="_blank">📅 18:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128240">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73cb88b33.mp4?token=qk83w7xtMLOhFNUi1TKxKVaY0Ev_mkue8QXwWbTjfHMsfmnN658GjGu7eFFgr_NyhYmv1unaC4uu7qERUeDaUceKSrrmijRx70SUhSQQdDFKr-23HMsWXg9h51adSBwb4AMdtxHoQSctO8Ubg3b8rOdAxddc3RG5ATA6wR_EjhGwD11bCmJrMovSXot42m4mg5inXW5-dSvWRTf5NHzIOPK3WPXsnaKWQQeHy6EKTDbTWwaDBio1o_vBhahobF9S1IlZVDd9izcd-3hKPM-VcdO5V8fY3iAJYHUjDIkqoYe13GOdNOdWS6DGu8ZYHkKfV2hp6lxXr1Wd8hA28rd9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73cb88b33.mp4?token=qk83w7xtMLOhFNUi1TKxKVaY0Ev_mkue8QXwWbTjfHMsfmnN658GjGu7eFFgr_NyhYmv1unaC4uu7qERUeDaUceKSrrmijRx70SUhSQQdDFKr-23HMsWXg9h51adSBwb4AMdtxHoQSctO8Ubg3b8rOdAxddc3RG5ATA6wR_EjhGwD11bCmJrMovSXot42m4mg5inXW5-dSvWRTf5NHzIOPK3WPXsnaKWQQeHy6EKTDbTWwaDBio1o_vBhahobF9S1IlZVDd9izcd-3hKPM-VcdO5V8fY3iAJYHUjDIkqoYe13GOdNOdWS6DGu8ZYHkKfV2hp6lxXr1Wd8hA28rd9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا اورزولا فون در لاین: تا زمانی که لبنان در آتش می‌سوزد، صلح پایدار امکان‌پذیر نیست
🔴
ما خواستار آتش‌بس واقعی و احترام کامل به حاکمیت لبنان هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128240" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128239">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc712a5cb.mp4?token=PmSB3mQUjP9wJsFwgRNuk0RfUOi1224cuQpBqD7L4x3O1v2xC5DdLDgMZIzsYU4K94tzqMpxULxgSIwD1bkF98IoqJw8731TpLgCLSyrRs7AwGG-Rok8L33pwJIf3MwPh1qvSbGF0Gwumkuj9tPvqdQUREdQgGm_arC009oc1jKS35LaAfRjviBNJZvif5MiSHiWRF95IGrUkUQhmBoICX_TQeWfChNnqqQ78HA6f3PdXuQkR2zl4c1mEwYxioxfG9KmlG0M7We8vrpHSd9aJ9EUAnTLZji9t0cNntFBPQJZzie-gyOEpjcxWFXlmXMXQ9pzO6zkkJB0BiLJTSyXLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc712a5cb.mp4?token=PmSB3mQUjP9wJsFwgRNuk0RfUOi1224cuQpBqD7L4x3O1v2xC5DdLDgMZIzsYU4K94tzqMpxULxgSIwD1bkF98IoqJw8731TpLgCLSyrRs7AwGG-Rok8L33pwJIf3MwPh1qvSbGF0Gwumkuj9tPvqdQUREdQgGm_arC009oc1jKS35LaAfRjviBNJZvif5MiSHiWRF95IGrUkUQhmBoICX_TQeWfChNnqqQ78HA6f3PdXuQkR2zl4c1mEwYxioxfG9KmlG0M7We8vrpHSd9aJ9EUAnTLZji9t0cNntFBPQJZzie-gyOEpjcxWFXlmXMXQ9pzO6zkkJB0BiLJTSyXLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره رسانه های ایران: رسانه‌های ایران، به ویژه رسانه‌های تندرو، بدون اینکه درباره آنچه می‌دهند صحبت کنند، درباره آنچه به دست می‌آورند صحبت خواهند کرد.
🔴
برای همه ما مهم است که این سابقه را اصلاح کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128239" target="_blank">📅 18:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
محسنی اژه ای : خداروشکر در جنگ سوم هم مثل دو جنگ قبلی پیروز شدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128238" target="_blank">📅 18:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5a403944.mp4?token=ssLUw6BlawByTo7RST9xZ7qVwpRZsZlJ3AftcE6mSE3NWJffjQjcZlFTG9VtxqWYsukbIX6FucJKvB3xKGnTT4kyJAxiZZTfyj0SD_yWM-mlyGLCdEdYOqufA4PNxIOuX-1d7ywPNyXYsLIxTaOu_Pa30kpU3k3WpFCa6znG-SLLQLazucMfQRnjF72JHxuwXImCsRGujZONJ_u59M7mPs98Ewb0MTtwTp0nH00-pkoJbOgtOjdpXBlYRBmnRPtFdQZLUP_xAtNT_SfN1bPPpbSprZlCgo5yeVPHQXOOJ__D9dpSR2Tw857BUe7j0FwDpkDIo1U_aouHu3zyCIf45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5a403944.mp4?token=ssLUw6BlawByTo7RST9xZ7qVwpRZsZlJ3AftcE6mSE3NWJffjQjcZlFTG9VtxqWYsukbIX6FucJKvB3xKGnTT4kyJAxiZZTfyj0SD_yWM-mlyGLCdEdYOqufA4PNxIOuX-1d7ywPNyXYsLIxTaOu_Pa30kpU3k3WpFCa6znG-SLLQLazucMfQRnjF72JHxuwXImCsRGujZONJ_u59M7mPs98Ewb0MTtwTp0nH00-pkoJbOgtOjdpXBlYRBmnRPtFdQZLUP_xAtNT_SfN1bPPpbSprZlCgo5yeVPHQXOOJ__D9dpSR2Tw857BUe7j0FwDpkDIo1U_aouHu3zyCIf45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر جی‌دی ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128237" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b083f878.mp4?token=TgH7tR_VILfeF6AqFkiowq4pBSEFjoWDe9i0C3cM5hjdpEZ9f3MQkYoOVQHT_nNpMMd0uzYSCOCm_RmwsaTxp0vpRm0wzAWdtRPN8ft1MfftV0l5L54PtUhs76MdeSSHzEl07vNt3ZGr5_LcwU51HfC5-dNZC45hwtlbVCvrr6xrLHiyZE7aTh_oIUyMhxpTncJyWMtKDybxqHUZLlCDeje7iJLxobQ2LWI0npHXaOIlEyNC8oRyEqPyO2v4us-o0e71fZCZZGXoWs7gAFWKmda4P-SXiksmeilORb8DxxyVkIjnBbR8yBvQkrISIfOCjImRhL3yee3TagTe8d8AwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b083f878.mp4?token=TgH7tR_VILfeF6AqFkiowq4pBSEFjoWDe9i0C3cM5hjdpEZ9f3MQkYoOVQHT_nNpMMd0uzYSCOCm_RmwsaTxp0vpRm0wzAWdtRPN8ft1MfftV0l5L54PtUhs76MdeSSHzEl07vNt3ZGr5_LcwU51HfC5-dNZC45hwtlbVCvrr6xrLHiyZE7aTh_oIUyMhxpTncJyWMtKDybxqHUZLlCDeje7iJLxobQ2LWI0npHXaOIlEyNC8oRyEqPyO2v4us-o0e71fZCZZGXoWs7gAFWKmda4P-SXiksmeilORb8DxxyVkIjnBbR8yBvQkrISIfOCjImRhL3yee3TagTe8d8AwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اجلاس
G7
وارد ژنو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128236" target="_blank">📅 17:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128235" target="_blank">📅 17:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار: قبلاً ترامپ گفته بود «هیچ توافقی با ایران جز تسلیم بی‌قید و شرط وجود نخواهد داشت.» چرا مسیر خود را تغییر داد و اکنون با این توافق موافقت کرد؟
🔴
دکتر جی‌دی ونس: فکر نمی‌کنم مسیرش را تغییر داده باشد. اساساً استدلال ترامپ این بود که ما از نیروی نظامی برای فشار آوردن به ایران استفاده خواهیم کرد و چیزی خوب برای مردم آمریکا به دست خواهیم آورد. و اکنون ما آن را داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128234" target="_blank">📅 17:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پرزیدنت پزشکیان:
تفاهم ایران و آمریکا جمعه امضا می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128233" target="_blank">📅 17:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgvOWtNgjlM9f1hi4al2e58zfyP04-c3wjQPO7a4TDCsXZbkdeZywx7F5Z8QmsPJJNY_IoaOUH8qX8tMZM4aVF2imxiiZCu8JDNweTUInrNuliweIrydESSCcH6SKe-xmGQmpjjgif4LrPqqR-AX4cd9QCFw_iUuN-h-hFaug997tX4U4NGJ4yiZCYjbKxbJi3TWAJ5ct6BDKTxqSXcub1v_t1MgrvGno71pd9oROUlnqUY6EbUinUG93Wk2UF4K5X-E3oXwiuJQVGWLiBeUtYBb5R_5-ibFFjll_41L4mBh4x1qSBXm1UX8SjsyWkvdlPXzfJT71DgRjP8GUkLFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت م. پزشکیان: فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود
🔴
پ.ن: جلیلی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128232" target="_blank">📅 17:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzgowz0kH-e917F8EfJZJ93AlABOCiJXlxyp2nOmANWAZwLek4AW0ib3CjYp5qAjXsbobqmj9J2339VLAFP4eeiKdfhMcBrflZ-iuI1KqBCjg_7aElURC_8w6r0Mvi1jdHH0Ie6_TOy9aqwhx7jwd5nkq2_QEFrpk08vaUOMlWL96VMWHcXNTAlEPe_XSBULati5JsfQa00kjgDZowmfgaZk96oaKbp_8CGxaUTbXKfirkvpfHCqR1EnDnXSbLz3xGZC-QhSeCEAbmkV3sb4HlzG-V3XwsgOEI_97Y_m19WT1ZES0DLqTSpkmo3eAJpxmj5Q-vQV-RPRLdD23anr3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله محمد خاتمی:
از تیم مذاکره کننده بابت رشادت‌ها تشکر میکنم
💚
💚
💚
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128231" target="_blank">📅 17:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ونس: رهبران جدید ایران از ۴۷سال مسیر اشتباه برگشته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128230" target="_blank">📅 17:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb6d0af85.mp4?token=UagdBzJDqexHH6TI0wo9PnHqYGDDBfuzpwq-geEuPTN_benwyw7XEFWI1Ku3Ybr2eMBSHSt7ZR8zr82cDkZvbdzAjf4nY3ASBvkbdIT-4Ggeh_nXnfFVvMKTxcVykNtxq-xCf0wo50xdPv90RsyJecjlSQDNPcHJLYY-Sy6ejg3sho86ux8lp18fJo4pZIoFBt-Z4_SyDHe9vjM4ohm8wR5IYWgKylmRzdTdj8yp4o47sUlEYu4JlerEwJ3O4YHL8GZwJDwVFHiqEWdocx1Ptxc43ftPmzH8f8uTWKuWnx8BbNpnJtJgnaG7VgolLhqS785JLF70vZaCpDAc8wDRug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb6d0af85.mp4?token=UagdBzJDqexHH6TI0wo9PnHqYGDDBfuzpwq-geEuPTN_benwyw7XEFWI1Ku3Ybr2eMBSHSt7ZR8zr82cDkZvbdzAjf4nY3ASBvkbdIT-4Ggeh_nXnfFVvMKTxcVykNtxq-xCf0wo50xdPv90RsyJecjlSQDNPcHJLYY-Sy6ejg3sho86ux8lp18fJo4pZIoFBt-Z4_SyDHe9vjM4ohm8wR5IYWgKylmRzdTdj8yp4o47sUlEYu4JlerEwJ3O4YHL8GZwJDwVFHiqEWdocx1Ptxc43ftPmzH8f8uTWKuWnx8BbNpnJtJgnaG7VgolLhqS785JLF70vZaCpDAc8wDRug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
🔴
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128229" target="_blank">📅 17:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کصاخیل درحال جهاد ری اکشنی
😂
میان ری اکت فیک میزنن و اونو جهاد میدونن و میگن ثواب آخرت داره
با همین تفکر هم همیشه.... خوردن</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128228" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b6b743a.mp4?token=DwunIJbaLM2wtHz8h-zGxBv_dqdkLzyLqZtuXJ8dKRb0K-OYRMxPSZE9wK0XU2ZS3S1V2PFvGs5xFigjeAELeOa4m6wjyRAWYlENKawiDhq2Tw8MqFXnfAeofkxXoSUU6WzKBjkGl0nXM4UneXy7BLRhRYuQ9jzdM0VtJvy_KRCrJwDyTJ42X1_N6RZI2FYzR5drdyW_DLwQ68D8V_yyOZUSsjjCWBHDJc6Dg4aLas3PkNAkINonVcSLN11ORi9pms_OZcr51ntxuOafvA9Y4UO5XObSWFmAYIVT3zsF6kQCeIP048HMSZUzYodT48CQbK9iL7KlBImxoTYD1-h-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b6b743a.mp4?token=DwunIJbaLM2wtHz8h-zGxBv_dqdkLzyLqZtuXJ8dKRb0K-OYRMxPSZE9wK0XU2ZS3S1V2PFvGs5xFigjeAELeOa4m6wjyRAWYlENKawiDhq2Tw8MqFXnfAeofkxXoSUU6WzKBjkGl0nXM4UneXy7BLRhRYuQ9jzdM0VtJvy_KRCrJwDyTJ42X1_N6RZI2FYzR5drdyW_DLwQ68D8V_yyOZUSsjjCWBHDJc6Dg4aLas3PkNAkINonVcSLN11ORi9pms_OZcr51ntxuOafvA9Y4UO5XObSWFmAYIVT3zsF6kQCeIP048HMSZUzYodT48CQbK9iL7KlBImxoTYD1-h-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
ما دست دوستی به سوی ایران دراز کرده‌ایم. اگر آن‌ها بخواهند رابطه‌شان با ما را تغییر دهند، ما نیز رابطه‌مان با ایران را تغییر خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128227" target="_blank">📅 17:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87eb24a096.mp4?token=m89_2OeH7sq5BBQlv4Y7Cipps279rPM_icr1svZtc1ymnCInZtzTd1UTPSxom34gua_cjI6RBpygS05cSWhpyiG-b50YPNDCAzXlKrOq1a7ooURuV80OuQhzQTFlTSzFTQnu9_ICJdtuR01rJGl-C7oK4kNUfrfTNsn3LLugHtciLC-ETqvEEvfVghVtHuGS-eRsOl2qW497DpZsfeccCFFWsMp7LUgXFLtd7wHPZ_M4fAzGzxge_HQAqPdBVoU1KhViHslKN17YK5EKoXGfK9GJqS9jS_dfeFzkiOdrE3Z2IMqFvaUE2TKmWaB2sjO8dawiiwv2O6tFZ9b5A-v2NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87eb24a096.mp4?token=m89_2OeH7sq5BBQlv4Y7Cipps279rPM_icr1svZtc1ymnCInZtzTd1UTPSxom34gua_cjI6RBpygS05cSWhpyiG-b50YPNDCAzXlKrOq1a7ooURuV80OuQhzQTFlTSzFTQnu9_ICJdtuR01rJGl-C7oK4kNUfrfTNsn3LLugHtciLC-ETqvEEvfVghVtHuGS-eRsOl2qW497DpZsfeccCFFWsMp7LUgXFLtd7wHPZ_M4fAzGzxge_HQAqPdBVoU1KhViHslKN17YK5EKoXGfK9GJqS9jS_dfeFzkiOdrE3Z2IMqFvaUE2TKmWaB2sjO8dawiiwv2O6tFZ9b5A-v2NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: تعهد دادن که ذخایر مواد بسیار غنی‌شده‌شون رو نابود و جمع‌آوری کنن
🔴
همون اورانیوم بسیار غنی‌شده‌ای که در دوران دولت اوباما و دولت بایدن جمع کرده بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128226" target="_blank">📅 17:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جی‌دی ونس، معاون ترامپ:
ما شاهدیم که هم تندروها و هم رهبران سیاسی ایران میگن: رابطه ما با آمریکا در 47 سال گذشته یک اشتباه بوده، بیایید ورق جدیدی رو برگردونیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128225" target="_blank">📅 17:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a52eea38a.mp4?token=XBNb_w7QMs10CJQlBs4Np3cDjY6yIlvhT9Gn0ehfPytgb6ttDYUWc0XnzlXNeULWsDkVGqDrVgCfs2srx59r6zy4fyX5xvZGoX92Cts1K7eOoo1yjS2cBL8e6ynac-jXxfpbLEr0lJ3on3_HVms5EQJmaRj7QKNOPq-sw2IphisqTtg--7PeAE2lDQU2dF-cQkyJEtWoUJO6ql0CAnu_4sHSLv24WrfYZMM3IzZHzB5TGL2MRjRnJxGzUQilpNKLhqt-1lw_jHI8xNOM3YpwA7hROvjqASGfZZOF6d-cx6jLbe_3Y-eeCS1TkIpDDyzdTFmoE9tKNKu0pg5cT9InqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a52eea38a.mp4?token=XBNb_w7QMs10CJQlBs4Np3cDjY6yIlvhT9Gn0ehfPytgb6ttDYUWc0XnzlXNeULWsDkVGqDrVgCfs2srx59r6zy4fyX5xvZGoX92Cts1K7eOoo1yjS2cBL8e6ynac-jXxfpbLEr0lJ3on3_HVms5EQJmaRj7QKNOPq-sw2IphisqTtg--7PeAE2lDQU2dF-cQkyJEtWoUJO6ql0CAnu_4sHSLv24WrfYZMM3IzZHzB5TGL2MRjRnJxGzUQilpNKLhqt-1lw_jHI8xNOM3YpwA7hROvjqASGfZZOF6d-cx6jLbe_3Y-eeCS1TkIpDDyzdTFmoE9tKNKu0pg5cT9InqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیزر وایرال شده از دکتر قالیباف
#مرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128224" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9226ba657c.mp4?token=NbG8ikzpBrO6BaRKITcYeyP_uJJ2W061v7oWJ0PRLHV_DXlETPEPyOdvDxk9Duc9k7M5a_RZegZHWvMO_t_vM-Gu-NzUoIQ1t7jNqNE0CrKU7YO9T0iGphN7EqpmTO23ljEeA353pNDodu0dq-6JcZhSXHEMwC8pSlXIErcumDVM-9qn19Zg26_uq1iDybP3rf3ZVAifZsjKUDUAuF4dTff14foub0FRZ1yXbLK8JIY8d1e5ljI4W6r_taBOmF74j9R8dyUNBJgJG_vBL2swk5DOkwRJEC26dtKsOwP0oU2EjVV258GedSsOUBvfu315S-SexZmrLEaxTQ2Uxr197GJyU3C5KmgpSav7EQE4w9iCFCVpBQm0Hxi0GID7BvjupYTTmYU0ExmIDVBNUNtcK1nYSALC_hlNuvnjgylDq-F1BIpoZhgmoje35gbnBTBkfDg9EE9v0n_dCjK-qcvujiTbvkkRixgqFP2wxWZpW8AgEarqe1xnqE2TnW17iLv7mfmmTkxOA7HspBpQfCrPVMCWsANanozovi6xK5meFBDcpFIUY1f2kt4bpkrX6kLXj3Fxtp69hOianyMdTy1KtKFChgO4LGOD4FWzhGaf3d6CQ7YI5WD_IGpU0RTs-N0d4XhBY494BkqNBu4oILdY_BDuzB4ZvE5TzRb7829_SEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9226ba657c.mp4?token=NbG8ikzpBrO6BaRKITcYeyP_uJJ2W061v7oWJ0PRLHV_DXlETPEPyOdvDxk9Duc9k7M5a_RZegZHWvMO_t_vM-Gu-NzUoIQ1t7jNqNE0CrKU7YO9T0iGphN7EqpmTO23ljEeA353pNDodu0dq-6JcZhSXHEMwC8pSlXIErcumDVM-9qn19Zg26_uq1iDybP3rf3ZVAifZsjKUDUAuF4dTff14foub0FRZ1yXbLK8JIY8d1e5ljI4W6r_taBOmF74j9R8dyUNBJgJG_vBL2swk5DOkwRJEC26dtKsOwP0oU2EjVV258GedSsOUBvfu315S-SexZmrLEaxTQ2Uxr197GJyU3C5KmgpSav7EQE4w9iCFCVpBQm0Hxi0GID7BvjupYTTmYU0ExmIDVBNUNtcK1nYSALC_hlNuvnjgylDq-F1BIpoZhgmoje35gbnBTBkfDg9EE9v0n_dCjK-qcvujiTbvkkRixgqFP2wxWZpW8AgEarqe1xnqE2TnW17iLv7mfmmTkxOA7HspBpQfCrPVMCWsANanozovi6xK5meFBDcpFIUY1f2kt4bpkrX6kLXj3Fxtp69hOianyMdTy1KtKFChgO4LGOD4FWzhGaf3d6CQ7YI5WD_IGpU0RTs-N0d4XhBY494BkqNBu4oILdY_BDuzB4ZvE5TzRb7829_SEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : می‌تونید دوباره به یه اقتصاد بدون تحریم دسترسی داشته باشید و به اقتصاد جهانی برگردید، اما فقط در صورتی که به تعهداتی که تو این توافق می‌دید پایبند باشید
🔴
پس این هم نقطه فشار ماست و هم‌زمان هم ابزار اجرای توافقیه که تو اختیار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128223" target="_blank">📅 17:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: ایران قبل از لغو تحریم ها باید رفتار خود را تغییر دهد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128222" target="_blank">📅 17:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
جی. دی. ونس درباره ایران:
«تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند.
🔴
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
🔴
ترامپ می‌خواهد ایران کشوری موفق باشد اگر در مورد ورق زدن برگی جدید جدی باشد.
🔴
ما با همه طرف‌های درون رژیم ایران در حال تعامل هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128221" target="_blank">📅 16:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw1O8BIqHIoqg9zXswyP4FE1hcstyBImQSSY74d9MVO_sw2yzSIjmcjGB_40nOHjUorn2viLPSAnKRxXprp3QQuU3OF4rrVNSvVkWJvwotTZHTrXZdtBfCyv_wa4FSoriBX06ST65vYkH_cj_9y4ApEAznGLGnQsiTLPnE0yQKbGkaDAeGFFnP8TmboPdii18v9hoRS797tA8JkLxjucT3yFpZnKXSa7PPyTaXd2u156WNb6q3K4rOxMlh336GRtZnYhhI2yN-ZwF6fLc7XYDQsLM9akk8Hve8aghBhzvqqClX8Z4ANb-tM771p7WZrjojfFdjanQaQcHR1NfvVtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند
🔴
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً امن، مطمئن و بکر است. مناطق دیگری نیز برای سفر وجود دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128220" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ونس: مستقیم با رهبران ایران در ارتباطیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128219" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ونس: برنامه هسته‌ای برچیده خواهد شد و تنها در آن زمان درباره اموال بلوکه شده مذاکره خواهیم کرد.
🔴
با آژانس و ایران درباره چگونگی نابودی اورانیوم غنی‌شده صحبت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128218" target="_blank">📅 16:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بعضیا یجور مردم‌ مردم میکنن انگار مردم اون ۳۰ الی ۴۰هزار نفری هستن که تو میدون‌ها هستن
🔴
مثلا تو تهران ۱۲میلیونی ۴۰هزار نفر عددی نی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128217" target="_blank">📅 16:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8Fqt9vluCNZOyICY4Ravv_QXgrYPVXM9bzpzEqbh4RYcWu9VlEYm4j55zwA7IUHW6c6mH39bJA-uad9lhKdOp8yCXGzc0vCChAqfcqnOWzVOUvTFawA161GWiIy_QEDmHeMwGye99zSiXVEMq7w2YiKtmG4XE-uoXlW1qYns3wGcpll-7ZEFk7k-S4UIdMrdvlYa_O3OsH8hPZOv9x6S5UaYOZNBBM8bSwtUpMb8UfMN3HmSTL_Hb33UX4PbeOde0EWmcqUBSMU9ERDKK2-xy8tX9mQtX6O0okx6VCZP0LEISRCKbkVkRoQfT4KjbzrcCsmLTdh8rFGM5vRFoLMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128216" target="_blank">📅 16:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6aee63ae.mp4?token=jcjjwbkZEYdK_CIySXYa1yiOsfVgL-8yxDCPbQs4fbWtVdVmWYoTv-vKRznDMNJWUyz2AvrAXBZsrE6JD0Xpu4LQaw28iPHaWMHa_7MB0i52vx0gZJsIvDKsRog4JaX4Bu4fYLk1fhfE86ZEXsensxK8AFbhAcLk6ciRGRpbSEogpfrZGs1aQrKjs38fMbMGpLHS_cc7lu0aDuAwuP6Lt-kxakR03IhDiioV4-CjAlw1neRsC0UMH8wkl-aUjkSPEgy6HOW2C3w76L2Q-mFLe9gSV0aH_W6Bk10DqntVCqEdVDXvZCTWcud7kSpAqqQcYWXcr6oJKNAVX0I_-KqVEmP9ILRCYuDj9HsRPnvAMvaUXOAMU6wdu1qlrDJkcrcOBP2IAj4hz5iuAeAl-9NOQIPk2YdWom5O5Y-EkUrwRzw1CD68C49MsLUpe-VO8TRfN3NOvjEMfVmp06yhG7Dgxu5mTxsoyAC8yi3deLrMUJrys0wIUl1r38i-7AhgNHyc3hLgqcdUum_qTzfcU1OSokhZgkxwhT0nU7z-X12PiJHi0e8Pg_kl5VrEeBCriuzh8aEBvF5lcTVHH49AitO5U-jDKZkHKJWVXeJc-i_39pF0AVkRCBaiP4KbiMvZbLgMsFLuYIIOuZlZys7pb8bBFvBYBLMA4hhsF1mXaB4T6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6aee63ae.mp4?token=jcjjwbkZEYdK_CIySXYa1yiOsfVgL-8yxDCPbQs4fbWtVdVmWYoTv-vKRznDMNJWUyz2AvrAXBZsrE6JD0Xpu4LQaw28iPHaWMHa_7MB0i52vx0gZJsIvDKsRog4JaX4Bu4fYLk1fhfE86ZEXsensxK8AFbhAcLk6ciRGRpbSEogpfrZGs1aQrKjs38fMbMGpLHS_cc7lu0aDuAwuP6Lt-kxakR03IhDiioV4-CjAlw1neRsC0UMH8wkl-aUjkSPEgy6HOW2C3w76L2Q-mFLe9gSV0aH_W6Bk10DqntVCqEdVDXvZCTWcud7kSpAqqQcYWXcr6oJKNAVX0I_-KqVEmP9ILRCYuDj9HsRPnvAMvaUXOAMU6wdu1qlrDJkcrcOBP2IAj4hz5iuAeAl-9NOQIPk2YdWom5O5Y-EkUrwRzw1CD68C49MsLUpe-VO8TRfN3NOvjEMfVmp06yhG7Dgxu5mTxsoyAC8yi3deLrMUJrys0wIUl1r38i-7AhgNHyc3hLgqcdUum_qTzfcU1OSokhZgkxwhT0nU7z-X12PiJHi0e8Pg_kl5VrEeBCriuzh8aEBvF5lcTVHH49AitO5U-jDKZkHKJWVXeJc-i_39pF0AVkRCBaiP4KbiMvZbLgMsFLuYIIOuZlZys7pb8bBFvBYBLMA4hhsF1mXaB4T6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل در مینی تجمعات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128215" target="_blank">📅 16:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ونس: امیدواریم متن توافق با ایران این هفته منتشر شود/ خواهیم دید که آیا تهران حاضر به امتیازدهی است یا خیر
جی دی ونس، معاون رئیس جمهور آمریکا در مصاحبه با سی‌ان‌بی‌سی مدعی شد:
🔴
روند راستی‌آزمایی دو مرحله‌ای در مورد ایران وجود خواهد داشت
🔴
ما انتظار داریم تنگه هرمز برای مدت طولانی باز و بدون عوارض باقی بماند.
🔴
هنوز جزئیات زیادی در مورد این توافق وجود دارد که نیاز به توضیح دارد
🔴
فکر می‌کنم کسانی در اسرائیل هستند که این توافق را می‌پذیرند
🔴
ما انتظار داریم که رئیس مجلس، وزیر امور خارجه و دیگران، نمایندگانی از ایران را در مراسم امضای توافق‌نامه حضور داشته باشند.
🔴
تعهد بلندمدتی وجود دارد تا اطمینان حاصل شود که ایران هرگز سلاح هسته‌ای تولید یا به آن دست نمی‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128214" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ ضربه آخرو بزن</div>
  <div class="tg-doc-extra">علیرضا طاهری</div>
</div>
<a href="https://t.me/alonews/128213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128213" target="_blank">📅 16:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127a682588.mp4?token=SiAwQcgaWB1HH6By-RAfhJFQDLh-Sv5tYi-OFekVv-EPhdk83zM8o1fEFHowsFMASeq8YuLerF0xh8DD-3O4msq6WaZm7gUSKCv1V8J1eckM9McsTp8QQ8xzTPJbpohqONk6Pd4xhOz0mmfG5RgAPuEVusiqeXWl-enhMi3xcp1cA4AEXPvcbX7J7Ip4Ov7Aul_Vol_c56eplGf_64zP7q4NSkFHx8DWPxKZh1JSrGDlJkTC21GnXIlUQJf_ksaCKNcHoVkx-rOHa9DvWqYayZG9suT4EkgwsrCVF3g4-NgBP3wLqjuBriJ8UqpEe-s5GcDYjkFRKxXE5ZUgZ7bhaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127a682588.mp4?token=SiAwQcgaWB1HH6By-RAfhJFQDLh-Sv5tYi-OFekVv-EPhdk83zM8o1fEFHowsFMASeq8YuLerF0xh8DD-3O4msq6WaZm7gUSKCv1V8J1eckM9McsTp8QQ8xzTPJbpohqONk6Pd4xhOz0mmfG5RgAPuEVusiqeXWl-enhMi3xcp1cA4AEXPvcbX7J7Ip4Ov7Aul_Vol_c56eplGf_64zP7q4NSkFHx8DWPxKZh1JSrGDlJkTC21GnXIlUQJf_ksaCKNcHoVkx-rOHa9DvWqYayZG9suT4EkgwsrCVF3g4-NgBP3wLqjuBriJ8UqpEe-s5GcDYjkFRKxXE5ZUgZ7bhaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین شاهکار عوستاد خوش چشم ۱۰ثانیه قبل از اعلام توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/128212" target="_blank">📅 16:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ونس: انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128211" target="_blank">📅 16:02 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
