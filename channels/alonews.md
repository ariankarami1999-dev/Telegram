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
<img src="https://cdn4.telesco.pe/file/U3tXZOi1J_sW_ACPha3F830QfLfnxHjX9PquzIYjr3-jMZOvXdxB1qThZhMPe9NYdQewQiyPmu1rVwTtXDZteMMhuSdZSQLSDC2VXRBnTCwblPyCFEhAQ_V-md89IO7xKIjVa5YclXIj0SWbKtIhFxdT8U4Y6GacZ3eE-nthoAL1GJmD_diIQEJwXP4mTwiI_Y2Z80bGvEaCM3MAt2f78q43jwgQkVbCfLZDMVfdrzDClU0iXThRVD2vR0-0dz9W32zpCWh31Aw5lbV_f52UpjaHlsElomEmh5lAoTwnZhZmbuGdzS5j8m9Att4OlSlMzmubWjXmoZT-9lQQrxw0Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 14:08:51</div>
<hr>

<div class="tg-post" id="msg-133212">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شیبلی طلهامی استاد دانشگاه مریلند آمریکا با اشاره به تهدید امروز ترامپ در صورت ترور او: بدیهی است که گزارش اسرائیل درباره وجود یک طرح ایرانی برای ترور ترامپ، او را به‌شدت نگران و آشفته کرده است؛ شاید هم دقیقاً هدف از انتشار آن، همین بوده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/133212" target="_blank">📅 13:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133211">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۲۸ شناور در دریای آزوف حمله کردند، که شامل ۲۱ تانکر، دو کشتی باری، چهار یدک‌کش و یک شناور ویژه بود.
🔴
نیروهای سامانه‌های بدون سرنشین اعلام کردند که یگان‌های آن‌ها در طول شش روز گذشته، مجموعاً به ۷۶ شناور حمله کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/133211" target="_blank">📅 13:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133210">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سی‌بی‌اس: احتمال مذاکره ایران و تیم ونس در مسقط در روز جاری
🔴
عباس عراقچی، وزیر امور خارجه ایران، صبح روز شنبه وارد عمان شد؛ در آستانه مذاکراتی با آمریکا که انتظار می‌رود از طریق میانجی‌ها ادامه یابد.
🔴
انتظار می‌رود تیم مذاکره‌کننده دونالد ترامپ به رهبری جی‌دی ونس، معاون رئیس‌جمهور، جرد کوشنر، مارکو روبیو، وزیر امور خارجه، و استیو ویتکاف، فرستاده ویژه آمریکا، روز شنبه مذاکرات را در عمان ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/133210" target="_blank">📅 13:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133209">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری فارس : تا وقتی که آمریکا از مواضِعِ خودش کوتاه نیاد، مذاکره برگزار نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/133209" target="_blank">📅 13:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133208">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i474BRRY4EgiIkg87hFneWI2RmdyUR_vnAQE1J2_Bt69vRoIGp-PWvFOyEEWK95PmIeBwZLwY4JaHBKQxOLfe1WxBybnu5bFGcW6LvEo1KDEjn4cBFr3AX1PEg5YiDYFv-UX3eYINoPNHTkVwZWVyGz02PGEhaXcxACMrFf_4jNG6GnGAB-Z7m2SlbVfQznnOsqekumez9sVabp07BAXl_D1I0zqSVz2wthH0Sc04YiiSXc-79EhEmQNWHZWA1uL6vmqrSpHTxeT9_Tm6mMOiH9_k8Nw-QYkKxLu0cOwEq8FgnXuW8O_zHv5L48HiJBuN51dfrS-gJaFJPkkVsBPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای منتشر شده که به نظر دو سازه در پایگاه هوایی موفق سلطی اردن طی حمله اخیر نیروهای مسلح ایران مورد اصابت قرار گرفتند‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/133208" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133207">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=dprdLhWNn9NcH1TSjPYtkIY5aX4MqvkaeoiXg-xcXfMPSZmX9kIKkQLj5b7E6OgyaUnkbwGDD7YhMnKYcJ-CHIoDXRFPaEfpuXjec984O-L5FSwIqYKAgBfrH8hGa-nlH96WBFI0g9lucns1zT1a8tQ15bykNglLL-k1CkPdDW1bO4yAt5wUDMUxEzIQUNGr6eLwkhktTWD29o3I00iMvrBeD4BQuA4qNjhCqu4dsd83GoepANaBy6OlWR5WUVwKyj6N5XAUyzGcHpsH6HpJSLoKbY82eqkQ_gv9K9ZN7g3mgaAvuOHeEsjvOGoavyyqdjkXImu7rYYpK_gak9k83Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e0ce0d1c.mp4?token=dprdLhWNn9NcH1TSjPYtkIY5aX4MqvkaeoiXg-xcXfMPSZmX9kIKkQLj5b7E6OgyaUnkbwGDD7YhMnKYcJ-CHIoDXRFPaEfpuXjec984O-L5FSwIqYKAgBfrH8hGa-nlH96WBFI0g9lucns1zT1a8tQ15bykNglLL-k1CkPdDW1bO4yAt5wUDMUxEzIQUNGr6eLwkhktTWD29o3I00iMvrBeD4BQuA4qNjhCqu4dsd83GoepANaBy6OlWR5WUVwKyj6N5XAUyzGcHpsH6HpJSLoKbY82eqkQ_gv9K9ZN7g3mgaAvuOHeEsjvOGoavyyqdjkXImu7rYYpK_gak9k83Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/133207" target="_blank">📅 13:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133206">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
چین صادرات هلیوم را ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/133206" target="_blank">📅 13:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133205">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
به دنبال خبر نیویورک تایمز درباره «تغییر هواپیمای ترامپ در بازگشت از ترکیه از ترس ایران»، دولت آمریکا برای خبرنگاران این روزنامه احضاریه صادر کرد
🔴
نیویورک تایمز اقدام دولت ترامپ علیه خبرنگارانش را «عملی گستاخانه» خواند و محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/133205" target="_blank">📅 13:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133204">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ان‌بی‌سی: یکی از متحدان جمهوری‌خواه ترامپ به او گفته دوباره به ایران حمله کن، این بار ظرف چند روز به اهداف نظامی خود می‌رسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/133204" target="_blank">📅 13:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133203">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
محمدتقی نقدعلی، عضو کمیسیون قضایی مجلس: پس از بازگشایی مجلس، پیگیر قانون حجاب خواهیم بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/133203" target="_blank">📅 13:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133202">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ای بی سی نیوز به نقل از مقامات آمریکایی:  اگر ایران روز شنبه اعلام نکند که تنگه هرمز مانند پیش از جنگ باز شده است، آن روز برایشان روز شادی نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/133202" target="_blank">📅 13:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133201">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مهدی محمدی، مشاور قالیباف:  بیست سال است که کالای اساسی کشور را از دو شرکت‌ آمریکایی می‌ خریم
🔴
الان هم بانک مرکزی می‌خواهد از همان دو شرکتی خرید کند که همیشه می‌ خرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133201" target="_blank">📅 12:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133200">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQoqdWCy1jXjfBSRWX5W71GzdRy0KqKu9vFkFV_DXbb3uknNDOmjRN7RlH0SwdhHS-xzGRw0Tz5jRuWsU6hPP8RtMXEPhzs1FlOIhpQeprSEPdsWHhXRUfYL-99tJH_HmdL3quAyR4P1LXaBpTtRauIakcsyGJL5Qjfhx8f86zcpDvS8wlXrvxaJFDso7dozcoGyjwp0H-DGUzbUTfFIh-3FnYU4PLs7rxw9ItScNoglrjNEMZogIQPltCYMUwymbks54U16n0ZN_uSANsPUfOvOU_2gdw6Qy3Rh51l1d_uhOSTxt62MavVXfc73Fbad3E3YqCDqcaSxDDHdogydUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مبادا غفلت امروز، ‎مدرسه میناب دیگری رقم بزند
🔴
آزاده مختاری: وقتی گفته می‌شود مذاکره هست اما آتش‌بس پایان یافته، یعنی هر لحظه امکان شلیک و اصابت دیگری هست؛ در این شرایط اصرار بر برگزاری ‎امتحانات نهایی از یکشنبه و آنهم حضوری، نیازمند تضمین جدی امنیت دانش آموزان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133200" target="_blank">📅 12:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133199">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پایان چک رمزدار؛ شبکه بانکی به چک تضمین‌شده رسید
🔴
حذف چک‌های رمزدار و جایگزینی آن‌ها با چک‌های تضمین‌شده، یکی از تازه‌ترین اصلاحات نظام پرداخت کشور است؛ اقدامی که به گفته کارشناسان، با افزایش شفافیت، تسهیل استعلام و کاهش ریسک معاملات، اعتماد و امنیت بیشتری را در مبادلات اقتصادی ایجاد خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/133199" target="_blank">📅 12:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133198">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سفارت سعودی در آمریکا: ترامپ و بن‌سلمان درمورد مذاکرات تهران و واشنگتن گفتگو کردند
🔴
محمد بن سلمان ولیعهد، یک تماس تلفنی از دونالد جی. ترامپ، رئیس‌جمهور ایالات متحده آمریکا، دریافت کرد.
🔴
در این گفت‌وگو، دو طرف همکاری میان دو کشور در بخش‌های مختلف و راه‌های تقویت آن را بررسی کردند.
🔴
همچنین دو رهبر درباره تحولات جاری در منطقه، از جمله مذاکرات میان ایالات متحده و جمهوری اسلامی ایران، گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133198" target="_blank">📅 12:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ادعای عجیب ایلان ماسک: ارزش اسپیس ایکس از کل دارایی‌های زمین بیشتر خواهد شد
🔴
ایلان ماسک در واکنش به انتقادها از استراتژی SpaceXAI، اعلام کرد که درصورت دستیابی به اهداف تعیین‌شده، ارزش این شرکت از کل کره زمین بیشتر خواهد شد.
🔴
این اظهارنظر جنجالی که درباره منطق استراتژیک همکاری SpaceXAI با شرکت آنتروپیک مطرح شده، با بازدید میلیونی کاربران در شبکه اجتماعی ایکس همراه شده و توجه تحلیلگران مالی را جلب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/133197" target="_blank">📅 12:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgZ0-LkMms-X75FyFURJHVuJ-k4tq5LHF43k7WjAkw5N3jak1g5OyiGCYq9cc4YLdH7dwcIVXxnK-OTLX3B5O1G4dKNhrQtA9PG1zFAokhXFnriZIP-G8X6MHRRuZPQ3_DV0wgkvudrMaW0ygBJsIjqboHnw5jg2v5ana9xc0IoMTteSsOAo2GZmpoN88yRZQ93rGFGGOXQizhBSXkTTKFyPP4pAgxpwdJ3IfkDIHOgoSFGB4jEXOvLuLGV48cqoE7lhyBYc_j49tajyvnTNxI2dZc1fg8U-vIjZHyC2PJ0qAmADT1TBJU8lY-BkMEAytMZ2TL6y0W35woWoVsCN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گودالی که موشک ایران، تو یکی از پایگاه‌های آمریکا ایجادِ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133196" target="_blank">📅 12:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هواشناسی: هشدار نسبت به وزش باد شدید در تهران
🔴
احتمال سقوط اجسام از ارتفاع
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133195" target="_blank">📅 12:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJeRHaXWezrnAPKsRLO0FuFTjOW5_G8R4rcsWEb8CrId7UBdY55oREocAH49wk8nKXOAajpjMDcrWkVSMq9GdFZOGxi843aRbwy49SQjCdspZ-4TlX-apXhwoSXlxkLr44FjjdD3yGurvhS6W-r3RY9XQDNKtTfZLZoBAzXq4lmzUFMjiLgkLFwhZ588iIQn0pwjQJ_UnQpBETPlllLy7faqMyKBabt_x8zeEwF6MSC3gMnIy4WgK-7Kpl_Q2UcpNrRT_xhNqkaiEwyEgkRTpi2pvEgllKHlMn0H1LC1-0kC5of-N6R1xABjFwPTl_Qvqx6a4OaY-kPc3dgwFOtr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخابرات: افزایش نرخ اینترنت ثابت، کمتر از ۱۰ درصد به درآمد این حوزه می‌افزاید
🔴
شرکت مخابرات ایران در اطلاعیه‌ای در کدال اعلام کرد که تغییرات اخیر در سبد سرویس‌های اینترنت ثابت، تا پایان سال ۱۴۰۵ کمتر از ۱۰ درصد به درآمد خدمات باندپهن این شرکت خواهد افزود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/133194" target="_blank">📅 12:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133192">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
طبق گزارش‌ها برق نقاطی از تهران بدون اطلاع قبلی قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/133192" target="_blank">📅 12:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133191">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slR9NvGD-EzD08HRSLyLqUBiOGkOeGnPDBA1orrufx817RXDeKrrphRLSeiCREKwJvdAbjiUSQVS7fh9nqQBr0Kug3l1OZWfX_R6ckPppB9vbIl82Dfei_JXSpVug07ukxkdHbYGClHVkhJ1TWS2ePpHs_LsRCisBS77965xLR6GnKopjsQxRrtnHtbq6YzYd-VX_rBXXSyJA9YyhXdm0QtfwOeG3Y6gsJDN71IeBXajhJHzzc6scOcLj7iCELrzMlgjEb7BSgz_o0ll-xsq1zT2OgdR-6iNQTOMVFlwXEt2vEGxOti9u_fxCodnuPF0yZvjZuZuQKCHopAttxQSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال اینجاست اگه موساد بیاد و ترامپ رو ترور کنه چی میشه؟ ایران قطعا شخم‌میخوره و اسرائیل هم بیشترین نفع رو میبره
🔴
اما نکته مهم اینه تندروها یا همون زباله‌ها هم دقیقا تو خط اسرائیل دارن جلو میرن و انقدر گفتن کشتن ترامپ کشتن ترامپ که ایران شده مظنون شماره یک
🔴
الی کوهن همین زباله‌ها هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133191" target="_blank">📅 12:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133190">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0a9b96c7.mp4?token=qob_sKA2iSNyFqxSCRraXajT3sGRlNV8aHp7EP3zv8ig3OTygpClrmstfa5l4VwTR9VwwobHDPbHf0AUVUW8Vs60PKM1SsKV7RBfFNgMgIxl4oO4xlE9jFtV7jNAVf8ndEAzGVi3ALrhRqmuTmXb6xPitB-rt-JCWp3Jn3bgjVBgCojDkKfNEDIHkrBTukyopE5x_Szmmu-7-mrjxbE45kvPdM5ue2y-dehiluyfA-Lg7zdgobb_zv7kE8iHwoX3YJs4vdAlQ-iBfUuE_cRAwApUVx6IEY1bboi13U2SYd7ySmWge5cldpIGBAp8AbnCC2kuu5uVMumICT77kTDJlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0a9b96c7.mp4?token=qob_sKA2iSNyFqxSCRraXajT3sGRlNV8aHp7EP3zv8ig3OTygpClrmstfa5l4VwTR9VwwobHDPbHf0AUVUW8Vs60PKM1SsKV7RBfFNgMgIxl4oO4xlE9jFtV7jNAVf8ndEAzGVi3ALrhRqmuTmXb6xPitB-rt-JCWp3Jn3bgjVBgCojDkKfNEDIHkrBTukyopE5x_Szmmu-7-mrjxbE45kvPdM5ue2y-dehiluyfA-Lg7zdgobb_zv7kE8iHwoX3YJs4vdAlQ-iBfUuE_cRAwApUVx6IEY1bboi13U2SYd7ySmWge5cldpIGBAp8AbnCC2kuu5uVMumICT77kTDJlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی مثل امینم، شروع کرد از از مقاماتی که تو جنگ با اسرائیل کشته شدن، رپ خوندن
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/133190" target="_blank">📅 12:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133189">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
استاندار گلستان: پل آسیب‌دیدهٔ آق‌قلا در کمتر از ۲۴ ساعت بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/133189" target="_blank">📅 12:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133188">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اژه ای ، رئیس قوهٔ قضاییه : جِنایتکارای جَنگی باید مجازات بشن و خسارت بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133188" target="_blank">📅 11:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133187">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو کارخانه تولید پهپاد در کی‌یف را هدف قرار دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/133187" target="_blank">📅 11:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133186">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISrVnJ9wnqr6xQpIidwSnlrFtLUoMJPjKxQT3RwQBcQQqSQvTdbUUT681v27tHzdLquNFW-39QFiW0JohQlC44GKmrNp1SmM6iRDHyMN5Oa9Niq6vH8CMeDJ8UQvQxKNarqBgoKyurgKzYjpkApW-aVb8KGb7WezXfAOowRkOJyU8Xw6Gz4GPRh55p2E_EL3QbJXgBD90Owmx6rNCkGLwI1xHSTNrA_P34eBt15ge1nGwbZ23nD-08qQ06R5V1Dad6B5kBvXNTD933aFpXHSMr6dnSxpRBxT6GiMA0fKkAKC5KWvbIz-8tgB_HxygUfKab0SxDJkSkbBrCD4aaCuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : روسیه حمل‌ونقل کالا از کانال دون-آزوف و تنگه کرچ را پس از حمله اوکراین به ۱۳ شناور روسی موقتاً متوقف کرد. ۲۵ درصد صادرات گندم روسیه از این مسیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133186" target="_blank">📅 11:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133185">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
متکی: با اولین شلیک امریکا جنگ زمینی رو شروع کنیم و پایگاه های امریکا رو به عنوان غرامت تصرف کنیم و ازشون اسیر بگیریم!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133185" target="_blank">📅 11:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133184">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKsTytpfJCTLGwAEwRLO9Z7JjZGGI6YEsS7nSIX8q1hGq9f33oKnQld2_XMFRfjc7aXo1ycSGVA_PZhHLvobHDT-0iHKcdvbKkgYffC0a9rYaH99bm2NqVnjNV36Ys9sSUh3vQgBwluHyXVZQmoJZ-YtifUfrlICeC0QB30FP5FNnzWfolmFIzWtELQeWiA3x4NUp8EPJcxykQmcOJf4L-cCYa75HbqRDmAqvCIWn0jCZK72lp7Q2ue7lhGrWTdbpF1eHtrUsdpYmqCzpMIpk79nVg0U-AKQ1ko-y83HOmpJpK1VLQ1WwTLPR9Y-Iwsfpwg5vu-HtxKZN2h8exDsmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت دونالد ترامپ در حال بررسی طرحی برای نصب نرده‌های دائمی جدید در اطراف کاخ سفید با هدف تشدید تدابیر امنیتی است.
🔴
بر اساس گزارش‌ها، این نرده‌ها قرار است در تقاطع خیابان پنسیلوانیا با خیابان‌های ۱۵ و ۱۷ واشنگتن نصب شوند تا دسترسی جمعیت و برگزاری تجمعات در نزدیکی کاخ سفید محدودتر شود. همچنین سرویس مخفی آمریکا و کاخ سفید در صورت بروز تهدیدهای امنیتی، امکان مسدود کردن این مسیرها را خواهند داشت.
🔴
این اقدام بخشی از برنامه‌های امنیتی دولت ترامپ در دوره دوم ریاست‌جمهوری او عنوان شده و شامل دائمی شدن حصارهای اطراف میدان لافایت و اجرای چندین طرح بازسازی امنیتی نیز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133184" target="_blank">📅 11:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133183">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
منابع خبری از شنیده شدن صدای انفجارهایی در منطقه السخنة در حومه حمص سوریه خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133183" target="_blank">📅 11:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133182">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609410a133.mp4?token=RO95Bcd1_ejRQUqlY9T2d1aFW47pWC_9XUd3N_vEq01J2WJAv5ak7BCq8sKUaI6RTDc1oiZPcVF-GnqdM8Xf_Fd2Dro1zKpG-5vS7eIPxN1iBxpl0YE1qMpjesOwQpMxA5J9tKcdSFitJAPRNhDw-JoPKa2K2LZezYEcmBWUPkPSGmg21kSUsVOKJ5X83iYj0phf-XfC4R7lSI2Zo2gxfREBVUzBc3pk5cxd9-quna6WmO6F8jgXfU2PIxY2BCi8XsKNImRM-ZD_rU1pNEXRJ4Lz6ta2Bai1rQsAHw9Qy6XUVLMdrvZFXXidVHAMcJfGw6-a7zLQ_U9mnpexxW251Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609410a133.mp4?token=RO95Bcd1_ejRQUqlY9T2d1aFW47pWC_9XUd3N_vEq01J2WJAv5ak7BCq8sKUaI6RTDc1oiZPcVF-GnqdM8Xf_Fd2Dro1zKpG-5vS7eIPxN1iBxpl0YE1qMpjesOwQpMxA5J9tKcdSFitJAPRNhDw-JoPKa2K2LZezYEcmBWUPkPSGmg21kSUsVOKJ5X83iYj0phf-XfC4R7lSI2Zo2gxfREBVUzBc3pk5cxd9-quna6WmO6F8jgXfU2PIxY2BCi8XsKNImRM-ZD_rU1pNEXRJ4Lz6ta2Bai1rQsAHw9Qy6XUVLMdrvZFXXidVHAMcJfGw6-a7zLQ_U9mnpexxW251Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش شبکه CNN به صورت رسمی از شلیک موشک‌های نیروی دریایی ارتش ایران به ناو آبراهام لینکلن آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133182" target="_blank">📅 11:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133181">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شرکت ردیابی کشتی ویندوارد: ترافیک تجاری در تنگه هرمز برای سومین شب متوالی، کاهش یافته است
🔴
تنها ۶ کشتی در ۱۲ ساعت از این آبراه عبور کرده‌اند، در حالی که چند روز پیش، به طور معمول بین ۱۸ تا ۲۲ فروند تردد می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133181" target="_blank">📅 11:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133180">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df78e521b6.mp4?token=Ksf5tYhhzYouWR7DR3Hia5J1nau84qQ5PdPK-b8iPRp6fV63wj-aCTn28Wp20UM7JzE0_Dt-Ttio5dZlWoaB0dAC_J_Vq4QvCKbbpYkZz5migAIgORT84xBtZxAzCYZAaYFgLsHrQIFZ5v8Nxm2p4IJ1x7b3DQ9n2n_I1tJlEqCVourOodkwqvyPT_O_38u_nlDi_L6JoGeCKxkVRlZ-blIvVvspf05VWWV689K5mIA4xU8hCgi2sU0FKQ3JAfSTl-unZ2CPIDpYk9qD8ryg5LsybqUtEedV1H9WsUSva2WJyELOjh9zzgIUlmdgJVgcGaaMK7v_VMd3P8-u6Xcp8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df78e521b6.mp4?token=Ksf5tYhhzYouWR7DR3Hia5J1nau84qQ5PdPK-b8iPRp6fV63wj-aCTn28Wp20UM7JzE0_Dt-Ttio5dZlWoaB0dAC_J_Vq4QvCKbbpYkZz5migAIgORT84xBtZxAzCYZAaYFgLsHrQIFZ5v8Nxm2p4IJ1x7b3DQ9n2n_I1tJlEqCVourOodkwqvyPT_O_38u_nlDi_L6JoGeCKxkVRlZ-blIvVvspf05VWWV689K5mIA4xU8hCgi2sU0FKQ3JAfSTl-unZ2CPIDpYk9qD8ryg5LsybqUtEedV1H9WsUSva2WJyELOjh9zzgIUlmdgJVgcGaaMK7v_VMd3P8-u6Xcp8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: ادعای ورود ۱۰ فروند هواپیما از عربستان و الحاق  به ناوگان هوایی کشور تکذیب می شود. شرکت‌های خصوصی به‌صورت مستقل برای خرید هواپیما اقدام می‌کنند، اما این خبر صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133180" target="_blank">📅 11:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133179">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سپاه : عملیات امحای مهمات در شرق تهران تا ساعت ۱۵ ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133179" target="_blank">📅 11:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133178">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی دولت: دولت آماده است تا برای عزت کشور و ملت ایران، نه فقط فحاشی و سنگ، بلکه «گلوله» هم بخورد
🔴
در چند روز گذشته در فضای عمومی شاهد برخورد‌هایی بودیم، البته تعداد این افراد بسیار اندک بود، اما صدایشان بلند بود
🔴
می‌دانیم و می‌پذیریم که «باد را با چراغ خاموش کاری نیست»؛ وقتی کار می‌کنیم، آسیب هم می‌بینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133178" target="_blank">📅 11:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133177">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
منابع العربیه: واشنگتن از ایران خواسته است تا به صورت کتبی و علنی تعهد دهد که دیگر به نفتکش‌ها حمله نکند.
🔴
واشنگتن از طریق واسطه‌ها به ایران هشدار داد که در برابر هرگونه تجاوز به آزادی کشتیرانی سکوت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133177" target="_blank">📅 11:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133176">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG0k84t2w6ifr4yg4AJ-4tVvXiLmCfiiTgXyfoehKgK7TEvUx4i5mYmLdkUr4bn38F0sEUXh0-WQrehUpVpt3uYdQIZUGVjg7KmSy0AfSMsfuQu_YyQV8uz-zECaBcf0fnw5-3GsQU5wHvujTvUwq2-fyvNweCSTR3YPiZkBcAaF1Cc5He9gBs7Ski7KXNodJg6z_ylXqmHPREKtu03m45cZOvERHGN7MDM7QAH8nxA4UBvhHyluFGJBwQs1WpPdsfBcsn05kJ9-NU2suxVaV9b5WbSauXe86pmhIvYaVU5BpVBNdRKCR4zEvnSeG35ynBAo06aDGbDdvdcvbByXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش معاون وزیر خارجه به افشای نقش امارات در حمله آمریکا علیه ایران:
غریب آبادی: امارات باید پاسخگو باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133176" target="_blank">📅 11:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FovjKgeALQEOIousgPkUapIXOTYHkdZ11HgkrzQjhQSQnHU0oFMjPiog6aRe059TsASp2nzBkcyEZfDLgbn-S7ZYhW-V1IsIzDW7-yqTCwNbSHQLXX5PHKTvhILdi8zpx-duNIxwwoEIhNSDwDXZSuKkOOgYGaUQGDDRHz_7llvqQ9zM2owE4wLDAq2iMju3cIpB86touPh5KzEmI3RdiIQ2bm1TGxsyKxSp5xj9LTHg_HHZA2P9G21TaqUoYKBvo2_0lvDi1Df9Xzy2NTnbxPNWNJOkd8H7bE8TqjoCc7Vc5tLcEDAEx1M4c_1i5WA2h7uQEJArO3T6vnVmQPHjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqz0OKNR1SHTsHG5ghIxt27iCzGW1LN9n3zcR6oey4wKo6lDOFv0pI_lv3eDl7Ek1CwwkOQyULgWIBro2fynvkH2ft6Ae_LvR1kgFHm-rmSt8bXSjSelnTCtOUTJFWjisktEnk1sl7TtTyn7dU0TmnX9wuZSN9GNn36WyovA0B3n3LnrEG9bjOndiGXxGBTcJF44jlsAZkLwQtOnWnR4Jpw6fqeo1aS-h3zlw2QCsa2qcttLhNtVXOF0vKKC6Vwx73RXU2ZNfhmygzfYh5L9RFhbYk5EktGb4Mxl9Y9trD8-sjUjXCq97wwpekcKWeIB-GjG4wUvSlprr97e__Jbew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ا
ستقبال بدر البوسعیدی از سید عباس عراقچی وزیر امور خارجه کشورمان در بدو ورود به محل وزارت امور خارجه عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133174" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886cfce422.mp4?token=EX6FQyiuMITmXJch9kukClXLSHy-YOFW0Zsq4P9pBI9ocXK-815nBCV4Uiqe9XdkWVGM956jOoNLJwKb4rv4su80IqfMItwF_XUP-xmVIdYrO96X4FxsxBO6ccFYeEyd4L2GwpUXosyUyRi6XtZOUInHgVr-SY_qQuR_eo_eWQxSMGjUutIIdblunHY_TL4Zo1lblExKDhQHMV0d61INgWQJVIjky1KCX4Py9r0XtpCgV5MYHEwSo0LLq0P_4aq819IUX9Xg1fH8Pa3heCh7VjPMlyHtk11tnB4Un9v2yLe80rZgqJBdltX5giX5Q_MUH89j6XU8n-5BZWr6447tXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886cfce422.mp4?token=EX6FQyiuMITmXJch9kukClXLSHy-YOFW0Zsq4P9pBI9ocXK-815nBCV4Uiqe9XdkWVGM956jOoNLJwKb4rv4su80IqfMItwF_XUP-xmVIdYrO96X4FxsxBO6ccFYeEyd4L2GwpUXosyUyRi6XtZOUInHgVr-SY_qQuR_eo_eWQxSMGjUutIIdblunHY_TL4Zo1lblExKDhQHMV0d61INgWQJVIjky1KCX4Py9r0XtpCgV5MYHEwSo0LLq0P_4aq819IUX9Xg1fH8Pa3heCh7VjPMlyHtk11tnB4Un9v2yLe80rZgqJBdltX5giX5Q_MUH89j6XU8n-5BZWr6447tXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پی جاری شدن سیل در یک مزرعۀ پرورش «کبرای قاتل» در چین، حدود ۹۰۰ مار از قفس‌ها گریخته و به ساکنان منطقه حمله کردند. شماری از ساکنان دچار مارگزیدگی شده‌ و به بیمارستان منتقل شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133173" target="_blank">📅 10:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133172">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
روزنامه عبری معاریو: از آن‌جا که اسرائیل برنامه‌های خود را برای بازگشت به جنگ علیه ایران تکمیل کرده، کشور‌های حاشیه خلیج فارس بر ترامپ فشار می‌آورند که تل‌آویو را مهار کند
🔴
محتمل‌ترین گزینه، خارج ماندن از درگیری همراه با اعمال فشار از سوی نتانیاهو بر واشنگتن، جهت تشدید تحریم‌ها علیه ایران و مخالفت با خواسته‌های این کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133172" target="_blank">📅 10:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133171">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قیمت نفت کاهش یافت
🔴
قیمت هر بشکه نفت برنت دریای شمال امروز با ۲۹ سنت معادل ۰.۳۸ درصد کاهش به ۷۶ دلار و یک سنت رسید. نفت وست تگزاس اینترمدیت آمریکا هم با ۶۷ سنت معادل ۰.۹۳ درصد کاهش، ۷۱ دلار و ۴۱ سنت معامله می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133171" target="_blank">📅 10:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133170">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گاردین: اروپا در حال بررسی پیشنهاد‌هایی است که ممکن است امکان وضع عوارض بر تردد در تنگه هرمز را در صورتی که اجباری نباشد و مورد حمایت آژانس سازمان ملل متحد قرار گیرد، فراهم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133170" target="_blank">📅 10:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133169">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی: حکم مراجع بصیر به اراده‌ای برای طوفان انتقام تبدیل شده و هیچ گنبد آهنینی مانع آن نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133169" target="_blank">📅 10:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133168">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت دفاع روسیه : ۱۷۸ پهپادِ اوکراینی رو دیشب رهگیری و منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133168" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133167">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آخر هفته برگزاری آزمون‌کارشناسی ارشد
🔴
آزمون کارشناسی ارشد ۱۴۰۵ صبح و عصر پنجشنبه ۲۵ تیر و صبح جمعه ۲۶ تیر برگزار می‌شود و کارت شرکت در آزمون از روز دوشنبه ۲۲ تیرماه در درگاه سازمان سنجش قرار می‌گیرد.
🔴
داوطلبان باید با دریافت پرینت کارت و همراه داشتن اصل کارت ملی یا شناسنامه عکس‌دار، در حوزه امتحانی درج‌شده روی کارت حاضر شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133167" target="_blank">📅 10:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133166">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXHYZwR3ef3m7yP70gJO4yxAw4HqOt5yhS3J2TSq9d8QjshhjpxFV3m3ZU0iinJOpAPyfdQhMtHZcvp7g7HW6iHfV3J7octkPJAJYlIJUTHHj7C-fkRxtG5fzJs1z-uUvzO-dmaD-j9JxGiLLIXxoQW4Splh6OqHpEKSyGzzDcyqgjQg9umTh8mvT2p2JBI9JKO_rLaKYTWP577EU4tZDwjHdG1BNnIHa1NnQO6BGA-_mzqk08DBA0m-D-JAOGE1Hp6PAGxNCPXCmBLSyhtSlzgyOIj1cyLPXJ-331vEQrbaWtgOww-4jQq4uwBaLCvaUGbVmhhoUp-BnX2f-EMpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی وارد مسقط، پایتخت عمان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133166" target="_blank">📅 10:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133165">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8bcc4a11.mp4?token=vYa6pQYrgy4DDJi6tYHL6Yve0O3FhBppy5Aj7m9t2tdVi9vgStxq9vSlUsxGSI_b5Gatnrhww0WYE4J3-w21OWQYjoaOO1_9fDkCrI3Q68X_9LurIElvCbx7fZy5Z-9eQ6Ti2fJUpS_F9jDMxj_B58UZl7edY9NsUC-bZlHePT7khPo8Jnlek3LKxWlaWtiHuJ0mqI3wjxFjruIZZER4bo5rr2HAMgZvmcD7x5G_f-7M2uxry6je_BfYLHSrWvr5BTRTN1nF2R_cYSnJ9nZFjMgJ34ehWRCtyvuZE59ALWUFSBf1jC1BewyJjEubGph5mEuUmZ_LI5Aq1_Twk2pnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8bcc4a11.mp4?token=vYa6pQYrgy4DDJi6tYHL6Yve0O3FhBppy5Aj7m9t2tdVi9vgStxq9vSlUsxGSI_b5Gatnrhww0WYE4J3-w21OWQYjoaOO1_9fDkCrI3Q68X_9LurIElvCbx7fZy5Z-9eQ6Ti2fJUpS_F9jDMxj_B58UZl7edY9NsUC-bZlHePT7khPo8Jnlek3LKxWlaWtiHuJ0mqI3wjxFjruIZZER4bo5rr2HAMgZvmcD7x5G_f-7M2uxry6je_BfYLHSrWvr5BTRTN1nF2R_cYSnJ9nZFjMgJ34ehWRCtyvuZE59ALWUFSBf1jC1BewyJjEubGph5mEuUmZ_LI5Aq1_Twk2pnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری دانشجو ویدیویی از محل انفجار در پاکدشت منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133165" target="_blank">📅 10:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133164">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqsKy8E74J0cJ-2JLhQxlKgBhk0D-M1iLlxXm_2Ub01H6AqR60Y8ngoQd3zn1EPKAwqmvdxoO597LyOY5gHnphLHRSQSCdn-IqRTEJ59cYqoh9Oc0DIIfj3bk7vLE5lWEzLFpg5E3PGLgOpCloEfjpi60YbJCKt_dKBQ2AhhadApOTC6ZnGxxRt-6N6Nl0Zp0ERQoYdoSKjGl0lvH-TPiky86ZcVZVoDJ1QzvSv0gZmOvBLPuV1WOmUv4VDsaMw9IT_nhRJL4KiuS4xvsS4thJQDRMyGJxLzd9qjgk53w9YB-6-l0M9u4EeVRr29AlKjydhBakNP2cIZ6ekoRKU5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دودی که از پس از امحای بمب کارنکرده ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133164" target="_blank">📅 10:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133163">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcde87d59.mp4?token=ezG38a4UujzKq36FxYjaWKrOYPyTj-wqWb1NllrIp6MH6VYpVZuFCICLkkozA-UoSSENp_29KupM5QeP7SDfMuGdnfIxWgqcxyLZLfazfl0c63earcrT2mfAeB-wPItX9JZOdeoidTzXya_xH7-y3z8IVdZ3lIH44177KNLIU_pKYocgUWCJP2l9ERrPeI3YSzZfxV9fHF0xG8DMUF0ZuOJc3HJqWHYkDjw56d6NoZfRoFl43v1U3Iq-g9J_tb3FG3-xz4dc0FK6AtK5vdGSJszUu8wMdYgzdJb_ZaLu48UM4dQgeEHPJvOIX6IQ1ODmeAjOJOZfmEbuzOTw5MDI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcde87d59.mp4?token=ezG38a4UujzKq36FxYjaWKrOYPyTj-wqWb1NllrIp6MH6VYpVZuFCICLkkozA-UoSSENp_29KupM5QeP7SDfMuGdnfIxWgqcxyLZLfazfl0c63earcrT2mfAeB-wPItX9JZOdeoidTzXya_xH7-y3z8IVdZ3lIH44177KNLIU_pKYocgUWCJP2l9ERrPeI3YSzZfxV9fHF0xG8DMUF0ZuOJc3HJqWHYkDjw56d6NoZfRoFl43v1U3Iq-g9J_tb3FG3-xz4dc0FK6AtK5vdGSJszUu8wMdYgzdJb_ZaLu48UM4dQgeEHPJvOIX6IQ1ODmeAjOJOZfmEbuzOTw5MDI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
10 کشته در سقوط مرگبار هواپیمای مسافربری در باهاما
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133163" target="_blank">📅 10:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133162">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شبکه‌های تلویزیونی اسرائیل:
برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند.
🔴
به دنبال درخواست ایالات متحده، به ارتش اسرائیل دستور داده شده است که تمام عملیات «حساس» خود در جنوب لبنان را متوقف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133162" target="_blank">📅 10:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فرماندار پاکدشت : صدای انفجار مربوط به عملیات کنترل شده مواد منفجره‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133161" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Acj_klh_nt7s8aH12qoqsfa4Lb_1I6gq7pjkE0aCqXmXC9RbmByNBAmmKhm4NUlBugtThaPzs7bs7WaBTw9aQjgNF0ccDXH4JZZBFHLUuUDmBALDqswYg8NZcvtuHE8VCSL34ffdB4GMKe8GAKXtsxCUUJovO53tLxBNgcMVMkascoXKXqzmNA8xAL9OmtUoOQiSn0emFKCFfprFZU22jWHchAxmNgvcXZFOrJrvtdaIVnA23HbOXFITrUyn-QPxZiayoQfOBwzDbttfqMcbGuqjJezoPZJlYVzlMDLdHE2Dt8TVmOrxZNuCKOn9AERmhntdre5Mp02WkYXB9nuBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nm-jOfN8rutZCgO-fstyOmSTwLBncRaUMLi9JZkIy-rBMID1lD7x7LPbsRI3WmrRojynfF_4LIGCY6ILO1gLPB4qOLR9hq9FNG-VhD_TwY4rcpqPdMeIM0IJWwIi7cNobNTB3q2lJiyykzQ1nY1MElXcExwDFxyFGSA6GO4G3AkyR_dfKS4MaNQ6auli6JCb_V9bnyVyEp2sU-GhxdH2Uut4xYswkfNtv6vIxONEWPz0ZsofHt65VPxoZA9WJ2apP0sRIiSz9xGeZYHq5n8huf85dgRBL4Um1WMLw9X9sOtQJIPm-0wL35VclVxzpXI15NDLWU9UWh5sEqyt4iGYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fT-aenZm8n_NEfnxXjO-nRb8aVigfknx_zr7jrL6sUukWI1zZhVg3KGXpr7mF7m2PpJ4xtkjaGg99JV31QbpCCGElKCVheo8mAQUkcI-8FyMcUl4Kaw4i_A2OatgMCh-BZHFwnS8cGO2hF1xbzeRkXNhblYv84SJhw0ijotZzfqZNfFwpJYQ3Jxk4GmBkl79zX08FveiZb_dfmhIlMv9sXtb0_uknOb9U8jOTMSGpBJVsrYp8__qhDU1rG_Zvonxg_--I18Bjv3MMagTa0_TLXE4XMceKSkX4N9JdJb7OMFleRrasGnpYOAdvefFt3PgQBTVw7MFeiBotQov6ZxBqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=N6pDH4EIIYghi_yZQ_5r2dCoiU5OL9UhpyrQntgXWwz18D7un3sJ0cKZAG5CplYa7dg-YlT014qrU80352PaXUH4Z6eeDUarS_VoXTycC1t6G3cW47Frdprg9VLZGtYJUb4_jDxXwKxURPlS_J7KWeYY51E5ks3xf-9IXkeEARMxN_zn1ro7byvpA7YTwKPNRTnOKsxtpge8j1oJWKhr7zEsbxlYjLFXZYXAd9oaVYg-lyHbJPeCHN8I2LjoS6DAilQ9reYOeLh5ocfHEI97Rve5DOT7ibLjnH4MaENlgwepshl1f78XoTVUq-Rnp5aBinCviD4Pj33umrpD1e1S-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=N6pDH4EIIYghi_yZQ_5r2dCoiU5OL9UhpyrQntgXWwz18D7un3sJ0cKZAG5CplYa7dg-YlT014qrU80352PaXUH4Z6eeDUarS_VoXTycC1t6G3cW47Frdprg9VLZGtYJUb4_jDxXwKxURPlS_J7KWeYY51E5ks3xf-9IXkeEARMxN_zn1ro7byvpA7YTwKPNRTnOKsxtpge8j1oJWKhr7zEsbxlYjLFXZYXAd9oaVYg-lyHbJPeCHN8I2LjoS6DAilQ9reYOeLh5ocfHEI97Rve5DOT7ibLjnH4MaENlgwepshl1f78XoTVUq-Rnp5aBinCviD4Pj33umrpD1e1S-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133157" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj9ImzUYUHLd-L9CQRQfOjN6BoDSyOT-ArfL-FJ3TTqvjNk3YyVFgYJAhRmmotEiLXLU82tgbGyy3vd3mNlEqfEu4-fl8EHtO7JidEEwws9rEpswW6NI6_5tsyc4xlTlQTHDWakmbSIKsdxCrqGmq96YQHdvIdT1rTGSIDWB-PR-bVLFmQfmb-caEK9m7RmFsA_3RGQQEFL4d2c02FjU3LP69whXmTRRR9wEqZa8OpN57sf89xFEGp7AsiTehOfa6Iziciw1P0M0r0qosk7Uw-3SJH7fQufECsvwxjKm-UM6SxAgEcCN8RSyL8Z84ILJQyVJWA-EEcIA51bB6M-hcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس هفته جدید را با افت آغاز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133156" target="_blank">📅 09:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از منابع اسرائیلی: ترامپ ممکن است حداکثر محاصره دریایی ایران را بازگرداند و به دنبال ازسرگیری جنگ تمام‌عیار نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133155" target="_blank">📅 09:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
صداسیما: ایران به دلیل پایبند نبودن آمریکا به تفاهم اسلام‌آباد، آماده ادامه مذاکرات نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133154" target="_blank">📅 09:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133153">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCC95OWRApzjFdaFqebCPR_LtdgJRCckzKz1EtQsB6AR1KNuycx2j62vmXaBQ_IHb-EntmT-QWzYLv6g-X03zA6w1W_KoDDuMta2AQx8GFLwx5odwhPFHrsHuMJWMN2NRFrEd1MgH2I0IyDkNlQj88Ua5FsRJF_FaZbiIDs7qeqAGIzvR7ueoRVH3jnHtErqbGg1-icl6TbsHn8Htpd5TUJBbsh7xnslP7o3d3TBJe3PzGHheTwtyqJRLT0ZmRg4B0OGDAUzxdmLwT_u-0Qi9n_m-RVPoexz5Ou4UgVWioqTNzjZndxzFx0uzKTvh6E5RwHolazTQUUAgz7Bk53YGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : ترامپ روز جمعه، با ولهید عربستان، بن سلمان صحبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133153" target="_blank">📅 09:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رویترز:  کاهش فروش نفت ایران به دلیل تغییر رویکرد شرکت‌های چینی که به سمت خرید از بازارهای دیگر در منطقه گرایش پیدا کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133152" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a515cd66d2.mp4?token=M58Y6fovKxV3n1dcyoy0gwRxPtLnwuX9TUILfnVzDFwvRHqTYY5b3G-28Ob0DB9YaGi12x-0TVLTzMjXOeb5Kdt9J9-c0BwK2G2bWzBrjSc70uUWM8AfDlr8Js6s293FDoysnAQ8m4OOgQQeHA-OxevpX3Ak-PYzR4aerUUaXV-qf1KRDhBACeolT4qzEc6tzuRAiHwWBM_Pc2WODcou2DYqr1oNDXs8Ffd5dQ8vYTHccnLfp0pG5r8Q_P13lAjBoRUuXDz6iQZKj8spsE5mZYk2dg7P1GOoB_YF-Hb_Dwemk-709ODXML5tOzzIWpcQFcfFffBeM4h2pxKGzjpBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a515cd66d2.mp4?token=M58Y6fovKxV3n1dcyoy0gwRxPtLnwuX9TUILfnVzDFwvRHqTYY5b3G-28Ob0DB9YaGi12x-0TVLTzMjXOeb5Kdt9J9-c0BwK2G2bWzBrjSc70uUWM8AfDlr8Js6s293FDoysnAQ8m4OOgQQeHA-OxevpX3Ak-PYzR4aerUUaXV-qf1KRDhBACeolT4qzEc6tzuRAiHwWBM_Pc2WODcou2DYqr1oNDXs8Ffd5dQ8vYTHccnLfp0pG5r8Q_P13lAjBoRUuXDz6iQZKj8spsE5mZYk2dg7P1GOoB_YF-Hb_Dwemk-709ODXML5tOzzIWpcQFcfFffBeM4h2pxKGzjpBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
35 کشته و مفقود در آتش‌سوزی جنگل‌های اسپانیا
🔴
در پی آتش‌سوزی گسترده جنگل‌ها در جنوب اسپانیا تاکنون دست‌کم ۱۲ نفر کشته و ۲۳ نفر مفقود شدند.
🔴
شعله‌های آتش بیش از چهار هزار هکتار از جنگل‌ها را نابود کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133151" target="_blank">📅 09:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شرکت هواپیمایی سعودی «فلایناس» اعلام کرد که از اول اوت ۲۰۲۶ پروازهای مستقیم و منظم خود را بین ریاض و حلب سوریه آغاز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133150" target="_blank">📅 09:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0aaW5crnEmGlXdVVyT7Hv64bEZ37Mbis7e9yOTEFFpoAyj8J2Fru-bdafW1wO2xkLdh0DzjY5KizRLzRTg_CLkYvZdVJfVVxmsiCezXtbdPn_knuAC9SePRJU0ry0g5WCWPSzGSRRklC0_Uy6YD4fMvslm_tjX6txqyBp3jkuWJCBnOn8lleYW7ptW-rQB87LFWAhRfCfneGbeATIsUHV5Jd2PbXKbEOD_GAht6TNJIHrr_1gvAtlC32TCLRZ5CG0etCrebjeY-_9VDwZEaZ0z8ofpyvI5LdTmEOoL_X30Jd9h9pgPPKjKlzg9-F1zUo1LKeLcxRUbB9XuCSr659w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ۱۰۰۰ موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا - که در این مورد، خودِ من هستم - عمل کند، شلیک خواهند شد
🔴
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133149" target="_blank">📅 08:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بقائی: نیروهای مسلح با چشمانی بیدار تحرکات دشمن را زیر نظر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133148" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کیهان: «پل ملک فهد» عربستان را با موشک بزنید
🔴
وقتی پل «آق قلا» هدف قرار می‌گیرد، باید بدون هشدار قبلی پل «پل ملک فهد» را هدف قرار داد. اگر به پالایشگاه‌های ما حمله می‌شود، باید به پالایشگاه‌های آنها حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/133147" target="_blank">📅 08:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی:
دولت ترامپ معتقد است که احتمال دستیابی به توافق هسته‌ای با ایران رو به کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133146" target="_blank">📅 08:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سی‌ان‌ان: یک مقام آمریکایی اعلام کرد تا زمانی که ایران اجازه عبور آزادانه نفتکش‌ها از تنگه هرمز رو نده، واشینگتن وارد مذاکرات مربوط به تسلیحات هسته‌ای نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/133145" target="_blank">📅 02:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dU1dhkIgpIERfMFJIAVy5zoVNWjEYwyG1dnr4ayuucTPOuo_LcEMHJnDOHV3PcTdRADxbz7JexI6aCb6mF3d39AbZ5Qfd3vgFItb-Vpipg4Talwddnj-heRwDNbOeBx7Atcwi2DYdhQt2jF1B_K6nvqEDzXI-WalJ7yK6B0sGM_P2rZs4_xrX907_xsLcGPb2zaAcH6XeIq2JeBsWHhcDsfT4lVzYAeVPBXtroi3_ZyAW1CMqr8HUKUs8lMykibjCZ-G5RxXqEPMdUAY-gfZ7RZPpwnzRRwwXiqSxNb2QiG4RjI5TMlBnr5MpcEaf1bOKrQAXVh08jCXVwbrMM-cPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l6ROVyL19MtEa60_oLmE9Du525GXLwL7ymeeUD7MSG_X6aHGU3WbenoaJyKnMc0U3pQ7ZuGgYlDtu6NfWZq54jZfh3Zon7km3tzSuwGCe3KgLW49bVAtkGOqrOZAQKSN5Ud_oyXy7vZujth4Vhsm26VHu-0X8p8LkepEQo9-r9odODz72fqnRfSpBM0K_STrMS836MkO93OnII7PFaeCjL1RwirmDv9n049Mo1TU_ZRo1zEj_HXNVVFV69e1mL6EJPLgHd2IVH0mJSWr4GM0FIBblFdOGDxAGP6WYB2ISSsAij1O7tw_UoAbZMqGiWhrmQ8Nx3o6CsLXWM6D8HTpPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دوستان به شدت دقت کنید این کانال و امثال این فرد کلاهبرداری محض هستند و کوچیک ترین سرمایه ایی وارد نکنید که سرتون کلاه می‌رود
🔴
هر کانالی بهتون گفت برید فلان ارز(لیست نشده تو صرافی‌های معتبر) رو بخرید قطعا کلاهبرداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/133143" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5bb8Mz60eHZkfNWxyHNucpJFriK9s5ch4uoeAgsTl3CvPN2yE62HLWMexB1Tq1NC0gcftHPq4zyT7BJBEyPZYLcFi2vwOHGQ1SarRdn77NMcBekhZZVDPHZ6l5k_BUOoet9QYU8AJxVvgZW0o2DKXBADPAzQHl4nzH4smNnFSMoDKbyFA9lvrA8XK3556j4vf9MxHEeoYQc9fA3eZkl9_c6aCwZQ6-eGboARXkP9JL0uQemie2zX6I5JKCY8NrSTwnKyHgQsTQF1Jaa7TmyG7gr5bdI9LerqqWe4V6S0TEQBXDAzSweZbRx_Y1msSJ4N7lYTmwk2toINFBjsk1cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الناز شاکردوست به دلیل استوری اعتراضی در دی ماه به دادگاه احظار شد!
🔴
جرم: امنیتی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/133142" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس:
به گفته مقام‌های آمریکایی، آمریکا به ایران تا شنبه فرصت داده که رسماً حمله به کشتی‌ها و اتفاقات تنگه هرمز رو محکوم کنه و اعلام کنه که تنگه هرمز برای عبور کشتی‌ها باز و امنه؛ و اگه ایران این درخواست رو قبول نکنه، عواقب سختی درانتظارشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/133141" target="_blank">📅 01:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDWieD_sMG-5h5_inS9pOV8yNvf5EaGge0F2kvcfjZ0qzC0NU6UhrbC6rOP_fHr3ATJFBi0UpYMIMuoGqU-tx2SSEyUG_IvVo-1ELkiSKrLVrCjqLA0YgYgGvk6mRScA_7BLKvvbhxJsuFMNHfUYbDJC2T9_nD73vBYnugcayoLamBFlVjna6g2PHYgQAMp_X3hIuWiINFfed1x7ez6rKsRmdlp6_Qs1aZVITF9_mZFJWUvV0MXyybp0pN4rTCrQ6S0VsY-vNrdcxGqcOx6j8omYWgff_Kt3kvv8F4hLYUtIqssoC75SHLcbP1BManSmchZtI1S_43vUvoJp7kzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
اگه میشد خودم خرخره ترامپ رو میجوییدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/133140" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">تیم ملی ایران هنوز شانس صعود داره
‼️
اگه سر تیم‌های بلژیک، مراکش ،سوئد ، ژاپن، آمریکا، کانادا، پرتغال، پاراگوئه، آلمان، برزیل، مکزیک، مصر، کلمبیا، آفریقای جنوبی، اتریش، کرواسی، بوسنی، سنگال، ساحل عاج، اکوادور، کنگو، الحزایر، استرالیا و غنا، بلایی بیاد یا هواپیماشون سقوط کنه
تیم ملی ایران صعود خواهد کرد
شانس: 0,0000000000000000001%
@AloSport</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/133139" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=i7epyArEC0r__U1taWax5jwqgOCe4FGmAbHdtYZkZ8d2jSHBF73o_YqBIPgmIk3vA3LwkMv75eTdMcebn1ZtIqbYODLGdeuGhRrek8R6ip79yhEtJtcmIIhwcjP_PKDW80pTQYLHLxFndcn23uK3S20c6dr4slcRp_9FNGmKX81bZJDqo41tDFV0rzaRWWR77g8sxntn2M0K38EWiEiDh5-AJN7UzhjyK6_hENcBieV8jj1QgMPHaXNdmFMjKEHs7Y6D5bZg2v0Uwnfty0o2jJGaGfEDZBwflAoDPMB3dlSdrbj-icW3j-OmDJty_NlP1eOOWzH3bhGyHukhYruGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/13ba9b7985.mp4?token=i7epyArEC0r__U1taWax5jwqgOCe4FGmAbHdtYZkZ8d2jSHBF73o_YqBIPgmIk3vA3LwkMv75eTdMcebn1ZtIqbYODLGdeuGhRrek8R6ip79yhEtJtcmIIhwcjP_PKDW80pTQYLHLxFndcn23uK3S20c6dr4slcRp_9FNGmKX81bZJDqo41tDFV0rzaRWWR77g8sxntn2M0K38EWiEiDh5-AJN7UzhjyK6_hENcBieV8jj1QgMPHaXNdmFMjKEHs7Y6D5bZg2v0Uwnfty0o2jJGaGfEDZBwflAoDPMB3dlSdrbj-icW3j-OmDJty_NlP1eOOWzH3bhGyHukhYruGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه دختر دهه هشتادی: من خودم جز جوونای معترض ۱۸ و ۱۹ دی بودم.
اما بعد از شهادت رهبر فهمیدم ایشون چه شخصیت بزرگی بودن، خاک تو سرم که دیر فهمیدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/133138" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آکسیوس:
دولت ترامپ خواستار آن شده است که ایران طی بیانیه‌ای عمومی که قرار است روز شنبه منتشر شود، اعلام کند که تنگه هرمز برای تردد کشتی‌های بین‌المللی باز است و متعهد شود که حملات به کشتی‌های تجاری را متوقف کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/133137" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=kmGmr2a59jKe-nmiRywrVjABJKvMsbOBBkcvBTArwHRJc2hTp1zr0z7jBaXIDHMrhxYCmgXLJeQpdMeslbSI7sRPVTPJCB--oKYUd1AuNi2hNyVuXPi8FbvgS6VFixDQ3HSJFa_kFjJCRyMreNiHGFCRdwXew3nXHU1VagS3wDzrBMwKaZ5SIiJQgX_ZovbQYmX6KUZkXpHiexmHACuaYxRjp8ZVqxSR_AwTkrNJOEgt45A7v_vhZEni8xs2cFKUh_Taomgny8PG3dCXVS8l5csrEfsSbPmzQgoXOapPGQ_ykSgvW3o3KxK62FEBJKp5qyrMINUErK37lWCq-4k3Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875fd4fb2.mp4?token=kmGmr2a59jKe-nmiRywrVjABJKvMsbOBBkcvBTArwHRJc2hTp1zr0z7jBaXIDHMrhxYCmgXLJeQpdMeslbSI7sRPVTPJCB--oKYUd1AuNi2hNyVuXPi8FbvgS6VFixDQ3HSJFa_kFjJCRyMreNiHGFCRdwXew3nXHU1VagS3wDzrBMwKaZ5SIiJQgX_ZovbQYmX6KUZkXpHiexmHACuaYxRjp8ZVqxSR_AwTkrNJOEgt45A7v_vhZEni8xs2cFKUh_Taomgny8PG3dCXVS8l5csrEfsSbPmzQgoXOapPGQ_ykSgvW3o3KxK62FEBJKp5qyrMINUErK37lWCq-4k3Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی وزیر اسبق امور خارجه:
اسلام‌آباد یک پلن فریب بود، اگر تیم مذاکره‌کننده هنوز به این باور نرسیده، جلسه بگذارد تا برایشان توضیح بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/133136" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzKR3RgC7IFdZr9_UuMuht3UpbaJKv5PvvUKXuJjWcCpOrjAUtL0qxHXc91_qknWdVy5KfGn_Gr0q_-hFXObd_zGn9ON1W2wHRfdy8uwXSleXFTqRIUcGowwU0vzrkOgBizLyE7vicYXg7xmAVdoLPpN8ZxIOWzL4aAJXsjyzYElc_gwSLuhgoAbvdJyM-ymH1tHhupqTbo_4SNBGSvETo0vRrF5_pdEs0bW0tzylNS5m9ixlxCSXgyAZOY14EGXfHxW4Qu-Wd8iKrqePQTTE7Rl6LbFq8cKaFc0VTiwb9Jy27KRo2_3F76S5rQ0DIjJJZBFOpgqBs2BiLQ0aIMHSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/133135" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون اطلاع رسانه آموزش و پرورش:
شنبه جلسه‌ای در رابطه با تصمیم نهایی مربوط به امتحانات و تعویق یا عدم تعویق برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/133134" target="_blank">📅 00:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y01GVv2PrG4Rc0K9vIMQWeFTEz5Jrv54O4CjUGEJ9bMkX814k0m-Q1cvfSCYssn3QTF3knKHLDRKtHJWuSGZ62xrJ450D3GPRS3wowZ6jyk94nT-G3GjobbxNjAgUIiOpRV70SOOMEXcZDonpgkxC7tvM4-Oztxvn4PNazejOsOsOOgeKmv64Es9__tOj_YJjSybuHY6Zq7w61iEB2zpCbbP9pu2VGsB-31Fmyq5GFP-V7_nIt2WlcpuJ3tz1Suy7AXqyxzHlpqInxWK62jpWWB5ZYON4LW91S6KhilBZ206tCBX6r-yEHLU-MIyzRvjKiW3KAN8YiHOkshSFf4zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
یه جون دارم اونم برای آقا مجتبی میدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/133133" target="_blank">📅 00:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / العربیه به نقل از یک منبع مطلع:
تیم‌های فنی آمریکایی و ایرانی در تاریخ ۱۲ جولای (۲۱ تیر ماه) در پاکستان با یکدیگر دیدار خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/133132" target="_blank">📅 23:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم؛ اما درخواست یکی از میانجی‌گران منطقه‌ای برای سفر به ایران را رد نکردیم
🔴
این دیدار در مشهد انجام شد و دیدگاه‌هایمان را به طرف قطری اعلام کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/133131" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرنگار الجزیره: احتمال برگزاری دیداری بین ایران و آمریکا وجود دارد که مکان آن ممکن است ژنو، اسلام‌آباد یا دوحه باشد
🔴
برگزاری این دیدار منوط به موفقیت میانجی‌ها و توافق بر سر فعال‌سازی باقی‌ماندهٔ مفاد تفاهم‌نامه است؛ پروندهٔ تنگهٔ هرمز نیز ممکن است به این دیدار موکول شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/133130" target="_blank">📅 23:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIdeQUK7duGqszLw3fk43gz_BTXPLC5IFabhwgIVBLMefR10O4Mg-gBRZKlX1rxWIBsODYTDLGXBmn1VZNx3Bl9EM2l6oDOo8SR2V95oBzOuFE8i94-lFfICgVZyGmQHOFynRm-KOMHAe_Rf_nIswEBgxqZi8Y14CGwEVsz81mvWcwkcyU-e1cUS2GZhwgKJcL5tvgEFGf7oRb9xAChPEzJefoTq5xXlwsVF6u4kR6BcfBprvZgxznyqgqjcdoy4Mx9ZKHta4Y9SKylHIqF81wJ3X9L7wEoSdPd2v7wWRb4-EPvSOBkMdJWg67YRrXwP0TXsot9nr8jz_lNBivEUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمعات شبانه: هرکس مانع قتل و قصاص بشود؛ خودش گزینه قصاص می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/133129" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=GELj1hrh87Msyc5NPimo4NlXQMX1yhm7YqAPcHa7JVDMnzrN2rsaG4nedhiN7iXq2yCcsa6t9GTSbw_0tnj5uUOaufVWjWjkKsEBUkHHXXW1V04d0Z69XBC-CtJ3DaAmmIp_FCVhbcaes00wdPNrhIx_Ngg1x1ZpkqpsGJE82X8b7-kgBhmibvcPIWm-bhwBT5csyzcp2HRBRj-k2WcImc3JmQpVH_J4kL6iukuFgeaDnouwu66J5n8tYCOJP_fSwZJelrv_6jsJJcNqjjRVCdWDsPJTOVU-v7gD6nMb6YF89d1LAQJcQAyHzEhtfQW9yeGdb-qPha1TfmxOjA1x64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b106bf152e.mp4?token=GELj1hrh87Msyc5NPimo4NlXQMX1yhm7YqAPcHa7JVDMnzrN2rsaG4nedhiN7iXq2yCcsa6t9GTSbw_0tnj5uUOaufVWjWjkKsEBUkHHXXW1V04d0Z69XBC-CtJ3DaAmmIp_FCVhbcaes00wdPNrhIx_Ngg1x1ZpkqpsGJE82X8b7-kgBhmibvcPIWm-bhwBT5csyzcp2HRBRj-k2WcImc3JmQpVH_J4kL6iukuFgeaDnouwu66J5n8tYCOJP_fSwZJelrv_6jsJJcNqjjRVCdWDsPJTOVU-v7gD6nMb6YF89d1LAQJcQAyHzEhtfQW9yeGdb-qPha1TfmxOjA1x64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون کرمانشاه آتش سوزی کمربندی نزدیک به میدان شهدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/133128" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مدیریت بحران آذربایجان شرقی: آتش‌سوزی نیروگاه حرارتی تبریز ناشی از نقص فنی در نقطه اتصال به شبکه برق بوده و شایعات درباره حمله به این نیروگاه صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/133127" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایروانی: اگر آمریکا به نقض تعهداتش ادامه دهد، ایران دیگر ملزم به اجرای تعهداتش نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/133126" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ناسا به دنبال ۴ داوطلب برای گذراندن یک سال در یک مأموریت شبیه‌سازی‌شده به ماه/مریخ است.
🔴
شرکت‌کنندگان در زیستگاه‌های منزوی زندگی خواهند کرد، غذا کشت می‌کنند، سلامت خود را پایش می‌کنند، پیاده‌روی‌های فضایی شبیه‌سازی‌شده انجام می‌دهند و خود را با روز مریخی که ۴۰ دقیقه طولانی‌تر است، وفق می‌دهند.
🔴
هدف، مطالعه اثرات فیزیکی و روانی مأموریت‌های فضایی با مدت طولانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/133125" target="_blank">📅 22:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه فردا با یک هیئت دیپلماتیک به عمان سفر خواهد کرد تا در مورد روابط دوجانبه و تحولات منطقه‌ای گفتگوهایی برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/133124" target="_blank">📅 22:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWnVlgqbsEdY0bKbxIjS-vfWlo_GL5ohgauyuJzPWwUh_-gjQLLehIUDg8_xZ7oD7KkG4qpmvzkDBWA661wr3MST2_XIwA-7lI1Hq9ztKidL8Gu2wSnxl3yHq3SHIVsLRLAIX7sZD9lJgP0cJcaWM0Sp15wliK7wvWLvU3xl_CutGqqzhqVyaiROrHbGaTxgH-SpkJM5jIAwBoINzJFPF0hTQtep_It2HU4rhgUDToQupwhg-6MJ528s3hFcj0PyHb3ycktU5puC1LJkK_qk6X8d-dDrI8Me99bw2mIQnXTbw99BYjqa1Sjq7fqkVgZlBNJQ6Ii9kiEAo5EFsaaWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین یه حمله بزرگ با حداقل 270 پهپاد به سمت زیرساخت های غرب روسیه انجام داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/133123" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت بازرگانی آمریکا روز جمعه کنترل‌های واردات کالا به امارات را کاهش داد و صادرات اقلام نظامی، برخی ماهواره‌های تجاری و تراشه‌های هوش مصنوعی را تسهیل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133122" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
العربیه:
وزیر کشور پاکستان احتمالاً به زودی از تهران بازدید خواهد کرد
🔴
العربیه از قول منابع خود از احتمال برگزاری یک تماس تلفنی چهارجانبه بین آمریکا، ایران، قطر و پاکستان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/133121" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/133120" target="_blank">📅 22:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=Zf00Ebkw_OEx9A2rBcAM9WnRrmRBzRnx9Otzhl8YEoCIYIU7zI1syuC7mGTSkQzxxsnl5xxHWs3GQlef4uGe8UdjUelDAVLNR0-W-LAgunk2kYH72otRtOAuN6P5lDb-O--ECDsQrT086zcxIhU94a__LKWG6vxfoj43BjFstVc-Zc6UxnbcLcnwOmdPfhaigFUrGy8m38uIRfRYd2IDMEVkFTz3sO2fbFTzXEIx8-xrrU6Vt7RXplPV0WfbghJcqC5CKnMiSUmHpgPCvpCGvH1jD0BsvAeq5nASlP4m_FsbC0mld4eh-7Q1Is3Ziey7VMJNGyzgBMfiOJt4nSCWEWQK1EbLp6n4Mkqyr5Xy0bvtm2l6njX5hmZt7gtOYnO2OE-DgOU5GUWivMbE2EdMt0XUjz0eCpoQ_uVXrkVMtmjHM3KHTh6WCu9gC0STfEp1MFUhichbxXhlwxOHABJ2c7LIo0_WOMGjNCIlG183WZdVYqF7_mxmsrRPnAKVpZLHTlIeLyecZ-zdJBPDIsR8B_ZTFFMUHo0xSZ0sFBtFHKbXlhl8RNFclaDMdoi5JX58OFt_UJovCkqup_yAAp_30cx-GqwjDV2AfdsofLURHLkh41M4tTW1Ue2_1fQkhY-XuB8tfYrKAe-wBSY9kcIHtIms0he3D5DvB3ZBd8Mj9xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=Zf00Ebkw_OEx9A2rBcAM9WnRrmRBzRnx9Otzhl8YEoCIYIU7zI1syuC7mGTSkQzxxsnl5xxHWs3GQlef4uGe8UdjUelDAVLNR0-W-LAgunk2kYH72otRtOAuN6P5lDb-O--ECDsQrT086zcxIhU94a__LKWG6vxfoj43BjFstVc-Zc6UxnbcLcnwOmdPfhaigFUrGy8m38uIRfRYd2IDMEVkFTz3sO2fbFTzXEIx8-xrrU6Vt7RXplPV0WfbghJcqC5CKnMiSUmHpgPCvpCGvH1jD0BsvAeq5nASlP4m_FsbC0mld4eh-7Q1Is3Ziey7VMJNGyzgBMfiOJt4nSCWEWQK1EbLp6n4Mkqyr5Xy0bvtm2l6njX5hmZt7gtOYnO2OE-DgOU5GUWivMbE2EdMt0XUjz0eCpoQ_uVXrkVMtmjHM3KHTh6WCu9gC0STfEp1MFUhichbxXhlwxOHABJ2c7LIo0_WOMGjNCIlG183WZdVYqF7_mxmsrRPnAKVpZLHTlIeLyecZ-zdJBPDIsR8B_ZTFFMUHo0xSZ0sFBtFHKbXlhl8RNFclaDMdoi5JX58OFt_UJovCkqup_yAAp_30cx-GqwjDV2AfdsofLURHLkh41M4tTW1Ue2_1fQkhY-XuB8tfYrKAe-wBSY9kcIHtIms0he3D5DvB3ZBd8Mj9xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی های هانتر بایدن پسر بایدن به دونالد ترامپ: چطور ترامپ از این کارها جان سالم به در می‌برد؟
🔴
چرا هیچ‌کدام از همکاران سابق شما به او نگفتند: «برو در ماتحت رو بزار، آقای رئیس‌جمهور»؟
🔴
عذر میخواهم... پدرم واقعاً می‌گوید: «توهین نکنی ها، هانتی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/133119" target="_blank">📅 22:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/133118" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا یه هیئت فرستاده بیروت
🔴
تا به حفظ آتش‌بس بین اسرائیل و حزب‌الله کمک کنه و نذاره این آتش‌بس به هم بخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/133117" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام: ما با کاخ سفید بر سر نسخه‌ای از لایحه تحریم‌های روسیه که آن‌ها از آن حمایت خواهند کرد، به توافق رسیده‌ایم. این بدان معناست که این لایحه به قانون تبدیل خواهد شد.
🔴
من همراه با سناتور بلومنتال به نزد رهبران جمهوری‌خواه و دموکرات خواهم رفت تا ببینیم آیا می‌توانیم زمانی را برای پیشبرد این بسته تحریم‌های روسیه پیدا کنیم که ابزارهایی را به رئیس‌جمهور ترامپ بدهد تا به پایان دادن به این جنگ کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/133116" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، اعلام کرد که طرح‌هایی را برای ساخت سه شهرک اسرائیلی در شمال نوار غزه آماده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/133115" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/133114" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۳ شناور در نزدیکی کریمه، از جمله ۱۰ تانکر، یک کشتی باری، یک کشتی مسافربری و یک یدک‌کش، حمله کردند.
🔴
در ۱۲۰ ساعت گذشته، به ۴۸ شناور حمله شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/133113" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl9oNRKeAlJFt-3lsVjHaj4i2e9X0KgYW1E1Yi9Srg5BqcWCwen9KCVO9XnI2rrM3WgaXLJR-qXnU7oy82WBsI6d_VpmNa_Y4Hsh4ufEFCtrQNiEcAgb3UgAj_GvHs_7Tjuw5z3l4qw9F4WcbEnaywA1h_ZI3Az_1GAMZJLyo5SS9l1vImacgNgfo-3DJMrmE0mgFu4fyusJjSOL8kwRxWpGq8W6uXiKvaVBeUnRtPmTQ1W86SQmezjqbZXD0VRuQ8OrFy95kiEAlvoAJiU6POFvxmyyVmMJ1zFnOhOOXZhPjrAfsl_Ey-KA8fVjgenBy-XnixLq9Bua0yr4bGpqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
🔴
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/133112" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شهباز شریف در تماس با پزشکیان: ایران و همه طرف‌ها خویشتن‌داری کنند.
🔴
بر ضرورت پایبندی به مفاد تفاهم تاکید می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/133111" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
منابع خبری اسرائیلی از سقوط یک هواپیمای سبک در فرودگاه این ورد واقع در منطقه شارون خبر دادند.
🔴
بر اساس اعلام این منابع، در جریان این حادثه دو نفر مجروح شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/133110" target="_blank">📅 21:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=PGFovgmo272JPnMAbFJwoCWoKoFx-p6sft1gdvcpBo-6IqvQKc2BtxmpwJrRXIXqPtytEJKsniNCZNybfKwY2ElHXveycgpAw03GsMkx28xr6t_l4aBtccOusrV2uTLKzw-eYPoyateM--luroKPmZKFLCcF4sFD4rQG8i_pR0fi_P7vfDhMvki9tji38ojr7yKjtrQLoNtxFK_kL8cT0l-I9joO-KHWSXHyHE4pYoxPJS9cn1ZeF7FnLW4W3rCtGhNNwtiddKtNz1lVCY06319qB_jEve21CZgq97xH7eaTS_vvdb6HUK2ZrsQa3e6Iirh2P0jzjncQ9Bfus_0_tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=PGFovgmo272JPnMAbFJwoCWoKoFx-p6sft1gdvcpBo-6IqvQKc2BtxmpwJrRXIXqPtytEJKsniNCZNybfKwY2ElHXveycgpAw03GsMkx28xr6t_l4aBtccOusrV2uTLKzw-eYPoyateM--luroKPmZKFLCcF4sFD4rQG8i_pR0fi_P7vfDhMvki9tji38ojr7yKjtrQLoNtxFK_kL8cT0l-I9joO-KHWSXHyHE4pYoxPJS9cn1ZeF7FnLW4W3rCtGhNNwtiddKtNz1lVCY06319qB_jEve21CZgq97xH7eaTS_vvdb6HUK2ZrsQa3e6Iirh2P0jzjncQ9Bfus_0_tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133109" target="_blank">📅 21:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
تسنیم :  انفجار در قائمشهر را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/133108" target="_blank">📅 20:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کان: ایالات متحده از اسرائیل خواسته است که از انجام هرگونه اقدام غیرمعمول در جنوب لبنان خودداری کند. بر این اساس، رده سیاسی به نیروهای دفاعی اسرائیل (IDF) دستور داده است که تمام عملیات حساس در جنوب لبنان را متوقف کنند. این دستورالعمل به IDF تا اطلاع ثانوی و تا زمانی که مشخص نشود تشدید فعلی تنش بین ایالات متحده و ایران و مذاکرات بین اسرائیل و لبنان به کجا منتهی می‌شود، معتبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/133107" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
