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
<img src="https://cdn4.telesco.pe/file/aibW0XWmIedKeK7QSHF5vDgrC57olmi-GKin54nZBnT1VkfmwB56OZYuM5CJcSBwX-YSbtFUFxvayF-TenjiFRiYBZFsibEQh1Kf3cfat9D7nInFNB6Jx4Bl8HXB7xm7ghmv_NPrba_9kdMg88RDWlcVjFItAtsvqInLCNLgJ1TUsq9fIoKYeiDpRNYwfgFMpfSp_Ec_JytvfbZZJSK6ZLHpYfBF0gDmJfmrbPZvuz8J_Wb_LoEhdBFG4Siu2j1039MR6wAgmz-Ls8EXMr3iUHbYGn007fCm2XVGXX0TIIL1TYUgwbv2OaayTQL1JnmgCeLq9eNzxpAVhJol5roM6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 912K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 11:30:51</div>
<hr>

<div class="tg-post" id="msg-123631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کلش ریپورت: روسیه سفیر خود را از ارمنستان فراخواند و خواستار مشورت شد و همسویی روزافزون ایروان با اتحادیه اروپا را دلیل آن اعلام کرد.
🔴
روسیه تهدید کرد که در صورت ادامه حرکت ارمنستان به سمت غرب، عرضه گاز و نفت بدون تعرفه را قطع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/123631" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvur-BL2z1Ome_-JA2huRcS9ZQzS_RGOctZLnJGaXq6F_eQ7K66iGuE9qfFtichht9XAf7oMvR_2KYFNBebHryx_sEeWCwQk7HHUHcpKdVmQTJjcAn7XSLP677UlX0doCsYSxB-x0rVpw8ArHlmTHChck_97kDBSs96S69SqR200VoTBTVsGjvDRv9IK8y8bwwsS_y5bH6yjICaGgAkInZ6FF0mQRpS5PV-9nkZ1N2KQlfCi2UXF2ssLm57bDCeFCc0e4BsbUmDsWy-2u5V7rA1AGwUrKBumKvuTmHHH9tSA7Cv7dpS6VxNIXrBnpyPqFy-Wz2-JOSReAz5pYC0DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۱۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/123630" target="_blank">📅 11:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123628">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ut1ZuRahZTmw6UpveiuJgdUKV1__cJeY90RngHjouyLKxevZt6Dx19xNCLuvYfnrPIpDYDwAYvBanepqz_C9sjDOzh2fq7V_9JS6K4tXh7Hz8DqQLO8IEQREAuqF887a0LfP3_bK3bi5HhQA8XFW8plD6i3y2ea3SjjrIzlUXGrzdK5jmCJGV6ShcO2qlY6OI6FOxjc9t1oNsYbouHK7Ia7N3qQdEDKcnEY7uAJGjHrit0FguNKfOVYqVZg3JWJkjtxyEuxZssm-iz4sxscEK1jubijtkd-7z_A8XwvSIyGAF5_gy1CvWUW4g4H6a4_iKoNUXCBqvIXhwRqddxBY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egE3-_S8I3grCnN6nm_aMvokeXCVgKNl7z_6zwb8HuJZMR5MX_5_oMTJpFXpkAnV4BpSpGDbtjCBbgk3OZJ4S6EWe848I3RA5a-NSGC_k_HAmphweAB1nqPZG9XHYCcBU50ncJ7ft24_eCdGDFw9SgHoy-CDRw9UeUUCCXsob8GD9_Xd11kxQ__wa7HY2FTYIVjxl-6y4Pv_CVj0UhNomhhPt1LIqIgdbdEmM7TzwCJ4Kir5uZKFBx_rK_ia2cnaWs_UQGCRJogaQ4PBXbheH4sGYnOn1XpjCeLkwF4cMjgzZ1AE4Sjm2tq5CJH9ub8QWlhLwdwa1zT8nKi4N74tJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به مواضع حزب‌الله در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/alonews/123628" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB5eYdLoCIPc2ZiVgpZn-Kdhvoh2W8HoH4unSy2nj5V9nzaW1OMsZjwY_RA15hKzlZ2eE1Xs0N5OWFI8j3DG47eYjkoG5LFeKXcNBA4gZqiYEgrLP5LMAA885QxbMZ4RRZSt1GJYQ04hdqiZj8klFuQDjU_C4MxM13jSt4ZQpxuXFGfZfX5PnFLvmmXY4I0PrmEmSOAaQ5_wprl1bJtVop3easOTnr6pwrIfIrCJ6iGg2Le6hq1rchrJRw12ky8KYlwti1ngSKdZL7cPdJVOkjB-ao81B1APiLB4PTMlyi1LH1AOieE2RM4oqLR6fnjKw8cb5NIyXkkZCaEXAERopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا، ماه گذشته با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123627" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123626">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRq9HKBnQYZuLgmaC-s_4I8OUIgV2J--2middLtjBanYubyUXY7Hm89EknJsJGLx4HdZiCXYFKeUETugX-QE2eyJQHoEUR-TFv9ViCcGgTMUE7iLXoHeB_FkROHP-GroI0rlpZOtq5pFXwriiui5SOmqrzsI5nDoUsmZNFGADneT0fErGAXTjF8z7M-miM0zL8xP8d1qDXUGKIpJ68zbYkcQfX8D-Kj85IZPpSfiZZuk7b1m_p4vuKN94Aa7NDoMKFyh0S7-NP4kGFWN8lvgeat4E8HG2EVxFw0Feg7tokhW9QYi-hg3l-5NGrOyWnoCJ2TMsEQwi1S54PQyevZeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید آخرین معاینه پزشکی ترامپ را منتشر کرد و اعلام کرد که رئیس‌جمهور ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار دارد، هم‌چنین قلب او ۱۴ سال از سن او جوان تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/123626" target="_blank">📅 11:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123625">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کنکور سراسری به همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123625" target="_blank">📅 11:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123624">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: هنوز هیچ چیز نهایی نشده است
🔴
او مدعی شد تیم مذاکره‌کننده آمریکا چارچوب حرفه‌ای و اخلاقی مشخصی ندارد و مواضع و خواسته‌های خود را به‌طور مداوم تغییر می‌دهد.
🔴
این اظهارات در حالی مطرح می‌شود که گزارش‌های مختلفی از ادامه مذاکرات، تبادل پیام‌ها و تلاش میانجی‌ها برای کاهش اختلاف‌های باقی‌مانده منتشر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/123624" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123623">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک پست : آزادسازی منابع ایران مشروط به بازگشایی تنگه هرمز و پاکسازی مین ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123623" target="_blank">📅 10:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نفت برنت بیش از ۹ درصد ریخت و طلا با رشد ۰.۸ درصدی به ۴۵۹۳ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/123621" target="_blank">📅 10:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز در جنوب اصفهان، احتمال شنیدن صدای انفجار در این منطقه وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123620" target="_blank">📅 10:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک راکت حزب‌الله به مرکز کیریات شمونا در منطقه گالیل پان هندل، شمال اسرائیل، لحظاتی پیش اصابت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123618" target="_blank">📅 10:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سی‌بی‌اس: انتظار نمی‌رود که ترامپ پیش از تصمیم‌گیری درباره فروش تسلیحات آمریکا به تایوان، با رئیس‌جمهور تایوان، لای چینگ-ته، تماس بگیرد.
🔴
تماس برنامه‌ریزی شده توجه‌ها را جلب کرده بود زیرا هیچ رئیس‌جمهور فعلی آمریکا از سال ۱۹۷۹ به طور مستقیم با رهبر تایوان صحبت نکرده است.
🔴
ترامپ قبلاً گفته بود که قصد دارد پیش از اتخاذ تصمیم درباره بسته تسلیحاتی با لای صحبت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123617" target="_blank">📅 10:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8SkFqQkaaPI81iElY4Trn5IuS_WVuOQYFN6v4GPmx2mkUhgaIgS3oe6bGypP0EMvbKjnsj28E-6gMdpplyfhJKfeU1cOdvkk73z9DxZaeO2XHDSsWLS73GkUppL7TcRve7W5O6bx0Viwfp7B2D5RIXxIuQ2hbO6x-gwg92esNcnWdYTncsq3VxLOBJU7rYhJHJ9Iv3xixerF0SN1oC8NrOJ1S8zcwzZte3fA0Wn-i-JyKMWO9GNGJ8fg9cw1bYQlN5XZX9nisUKt4V1hsJBG5xYCzGBw4nIjiESb9O3MEDz4a7O9FtcdFq_pADbr7fPSux9mzo1TlJU7ZUyIAbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل یک وانت را در بزرگراه حبوش - دیر الزهرانی، جنوب لبنان هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123616" target="_blank">📅 10:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK39WVVjf3A9Wcn04iDHiokdJUk5uHLocNQpwkACS9inDwHom_cn7c6iWtNJtWp3rGlwA58EAuetS_hs9tcv5Szy1-yY7eZ92-KxPsaJlyU5V2FCulNEPW3PlMlg9VVwc7_4lO1DKLIVcK6LK2xERYh089s4JfkwLQeMd4C0_m26Hi5nizAzCkAZo_hABSOMioTC6zqNO-3Sm_ujUHkhlUJ5vRwgHKq5rHW1XmlTDxgkD5lPgzd9UjHYgjK3Y0t8LKFNu-FBwpApQp4lzmZ-0iB-OZNMf7rSmWC-gMf-wtrtZ4-UT9xFywpWEXHnvQhjgiPGE224g-tMDxnZCKIQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: پنج پرسنل نظامی آمریکایی و پیمانکار پس از آنکه آوار ناشی از موشک بالستیک فاتح-۱۱۰ ایران که رهگیری شده بود، پایگاه هوایی علی الصالح کویت را هدف قرار داد، مجروح شدند. یک پهپاد MQ-9A ریپر نابود شد و دیگری آسیب دید. جراحات تهدیدکننده جان نیستند؛ این حادثه پیش‌تر فاش نشده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123615" target="_blank">📅 10:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/123614" target="_blank">📅 10:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbkAwx6y61UBYlSsWN9oksp-UrHLyBe7aqXNQ8GZgmTAmyqF_mn4veQqISqW4k8_72DOTZ9ljjqCpTslW0ChHibzHz5RidBsUXicnoUeFSGI0cxdjWaevu2bf0lJgKKL0R1mLnVWn9zL_NMzOVRfqf6uWUBpsLkQN3UVZgCpLtGFWs763wzyHwm_LFDtUiedhHpFGf1ELTJbv5tPOUPo1GfH2Oi7iXKpggxEFYFjRIB8YkaIb1S4w6T27udJhSvBbJtTZ3qF0DsSA5ZifIRlRaj-r9qzjKCOy_ggV0LmK1SZKadFxljPKNZjrALhiMf6ByCfVgb4SkUtNO0f99nJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای وال استریت ژورنال: موج کوچکی از کشتی‌ها در تاریکی مطلق در حال عبور از تنگه هرمز هستند و بدون چراغ یا سیستم‌های ناوبری خودکار و با کمک ارتش ایالات متحده، از این آبراه خطرناک عبور می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123613" target="_blank">📅 10:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس ایران در گفتگو با ریانووستی: ایران همواره برای شرکای خود احترام ویژه‌ای قائل بوده‎ و خواهد بود.
🔴
روسیه و چین به عنوان شرکای راهبردی ایران در موضوع تردد شناورهایشان در تنگه هرمز مورد اقدام مثبت بوده و خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123612" target="_blank">📅 10:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
🔴
این یک اثر شایع و خوش‌خیم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123611" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqBnTrbowObkldddFrzFrBkqGlwARlD91RtCD9Bus-2RCY38Uzrhe5oE5le3Li0PlcBxf7HF9kAKyI4qbyQAHZQmjONsaFajZt-4R0IhDhGFJ901DzusatiVf8Q38J-pg8d9UAYulss1FT-48GH4paXBMJTuQX1yVCzCjd4bSjLp5oOZsIU1Bij1awZRFdVJ7NkJjRypdi7H9DJxBT2fUgjJHVVYbnKqdEOKF6uOEMO8NjT3wKUvTynK5CZvvyqIPir3lGzKJIX-85tQQyhxenNoC_DldDm38j7Q9xsAzbiUmJJxRYi6Kgn8Qb0tkBfh1EmG9VGEjrM_Cw5SjNVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توجه‌ها به شبه‌جزیره مسندم؛ نزدیک محل عملیات نیروی دریایی آمریکا
🔴
گزارش‌ها و تصاویر منتشرشده توجه‌ها را به منطقه شبه‌جزیره مسندم در عمان جلب کرده‌اند؛ منطقه‌ای که در نزدیکی محل برخی عملیات‌های اخیر نیروی دریایی آمریکا قرار دارد.
شبه‌جزیره مسندم به دلیل موقعیت راهبردی خود در نزدیکی تنگه هرمز، یکی از مهم‌ترین نقاط ژئوپلیتیکی منطقه محسوب میشود و تحرکات نظامی در اطراف آن همواره مورد توجه رسانه‌ها و تحلیلگران قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123610" target="_blank">📅 09:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t71FlFG5CK7W9zcZbHc-dK4i0cBh4opiCpuDwvtxcPck9UbXRimZv-pyNrENX_4mEBzd6A1Fhdki-K5c5CTRgTcxgdQBJoReheZE9rpAO0bNm-8eGbRl5_wkQnhLc9fCL3lK6YIrfMm2gM_B2SqN96RlwRA3bpmZiepBqhpR22A0HC-RQkibKjHKY5bfVTOSY5dx6zfaA1XFBu17T1PiPrXoEKlFr81iZDwekA4AQkpp5g3k9yNg3M4PuWkvlJ3fHR2Kqpcp34j6tpOdukFOB79ouwAXCp50c5aBrCjnDBiqXBgsyryx6iZb6lYfAbxUg1nPRGMOrfV4_JAuEmRw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRMJp48Osaho0LijCQMiSTZZJ40oQAJDo0YlgoHh__RxClNXw_g4Id5VaQZJ6zg5lE-qy-7QgUDLrMfhbkHEWwMV0RL30iT4yfkRlh81VpuUdk4bIYtoO_3k1-5K0fG7HdEdxzDg2l7rCWKgsHfoj4p9QNpPOW90tp-lzjT9t10JgJZv7HB1qdS_n00fGOBQDPWPbiEh_1fx9Bww1KLv6LgBTCDEX0a1ziU5KnxtwcKLj6h2jEPtrZukxZRnPLUjUYKsbIkDONIf2GPpU5XaNoR6O7ekz7qgSoXHXyrdRE08Y3VI1Cs3G9Dgpxlj5fycBzu-j1og6Msxpnlo_wnBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروی دریایی آمریکا: کشتی‌های تجاری از تنگه هرمز دوری کنند
🔴
فرماندهی مرکزی نیروی دریایی ایالات متحده (USNAVCENT) روز گذشته با انتشار یک بیانیه فوری دریایی، به مالکان کشتی، بهره‌برداران و دریانوردان نسبت به آنچه «عملیات نظامی خطرناک در جریان» در تنگه هرمز خوانده شده، هشدار داد.
🔴
در این بیانیه ادعا شده که ایران در تلاش برای «کنترل غیرقانونی» این آبراه استراتژیک از طریق آنچه «مین‌ریزی خطرناک و غیرقانونی» خوانده شده، است؛ اقدامی که به گفته سنتکام، کشتی‌ها و خدمه آن‌ها را در معرض خطر قرار داده است.
🔴
بر اساس این بیانیه، به تمامی دریانوردان توصیه شده است که از «طرح تفکیک تردد» در تنگه هرمز اجتناب کرده و در عوض، عبور خود را با «مرکز همکاری و راهنمایی نیروی دریایی ایالات متحده برای کشتیرانی» هماهنگ کنند.
🔴
در بخش پایانی این بیانیه، هشداری قاطع مطرح شده است مبنی بر اینکه هر شناوری که در حال انجام فعالیت‌های مین‌ریزی یا پشتیبانی از آن مشاهده شود، در چارچوب آنچه «دفاع مشروع» خوانده شده، از سوی نیروهای آمریکایی هدف قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123608" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123607" target="_blank">📅 09:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بلومبرگ
:
چین خبرنگار نیویورک تایمز را به دلیل مصاحبه با رئیس جمهور تایوان اخراج کرد
🔴
چین در حالی که پکن کمپین خود را برای منزوی کردن تایوان در عرصه جهانی تشدید می‌کند، یک روزنامه‌نگار نیویورک تایمز را به دلیل مصاحبه‌ای که این روزنامه آمریکایی با رئیس جمهور تایوان انجام داده بود، از این کشور اخراج کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123606" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123605" target="_blank">📅 09:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیلی‌ها می‌گویند ترامپ در جنگ با ایران، ما را زیر اتوبوس انداخته
🔴
نتانیاهو، کوشنر و ویتکاف را به خاطر هدایت رئیس‌جمهور آمریکا به سمت پایان دادن به درگیری‌ها، سرزنش می‌کند
🔴
اسرائیلی‌ها درک نمی‌کردند که جنگ می‌تواند به تغییر رژیم در واشنگتن منجر شود
🔴
شاید نتیجه این درگیری، روایت سیاسی نتانیاهو را پیش از انتخابات پیش رو، پیچیده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123604" target="_blank">📅 09:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رکوردشکنی گرما در مازندران؛ دمای دشت ناز به ۴۷ درجه رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123603" target="_blank">📅 08:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آسوشیتدپرس: جمهوری خواهان دولت ترامپ از توافق در حال شکل‌گیری به شدت شاکی هستن و هشدار دادن این توافق ممکنه که توان هسته ای جمهوری اسلامی رو به طور کامل نابود نکنه و دستاورد های نظامی جنگ چهل روزه رو از بین ببره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123602" target="_blank">📅 08:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آغاز امتحانات دانش‌آموزان از امروز؛ اکثر امتحانات مجازی است
🔴
رئیس مرکز ارزشیابی آموزش‌وپرورش: سال تحصیلی امسال به‌جای ۲۹ اردیبهشت، تا ۷ خرداد ادامه یافت و از امروز ۹ خرداد، امتحانات پایه‌های اول تا دهم آغاز می‌شود.
🔴
امتحانات دوره ابتدایی غیرحضوری است و بر اساس ارزشیابی تکوینی و تشخیص معلم انجام می‌شود.
🔴
امتحانات پایه‌های هفتم تا دهم به استان‌ها تفویض اختیار شده و اکثر امتحانات مجازی برگزار می‌شود
🔴
امتحانات نهایی پایه‌های یازدهم و دوازدهم از ۲۱ تیر، به‌شرط عادی‌شدن وضعیت با اعلام مراجع ذی‌صلاح، به صورت حضوری آغاز می‌شود و احتمالاً تا چند روز آینده برنامه امتحانی این پایه‌ها نیز اعلام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123601" target="_blank">📅 08:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فارس : متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123600" target="_blank">📅 08:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره: ترامپ هیچ توافقی با ایران امضا نخواهد کرد، مگر اینکه برای آمریکا سودمند باشد و با خطوط قرمز او مطابقت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/123599" target="_blank">📅 08:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از مقامات آمریکایی:
ارتش آمریکا، با وجود انجام عملیات‌های جست‌وجو، تأیید نکرده است که ایران در تنگه هرمز مین کار گذاشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/123598" target="_blank">📅 08:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پیشنهاد کیهان برای دریافت عوارض از فیبرهای نوری در تنگه هرمز
🔴
روزنامه کیهان پیشنهاد داد از فیبرهای نوری مستقر در کف تنگه هرمز که سرمایه‌ای معادل ۱۰ تریلیون دلار را شامل می‌شود، عوارض دریافت شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/123597" target="_blank">📅 08:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIj4N3XHZA_c7NymL67lf_bQWzHM9qEt2EpmCXudfRYniWOX3emIHinm0rBb9s32Atoay0ctAGncNdl9gI7BL7_bKM53aP0s9cw3vy7ked6H2Tk-fgdpEdr84Z_j7LCIkQUaVduL05zOzUk6rBVEvIv_GYss7_lnxwwrw_5ngzrlknwiL2TyMwN4mOj9_cRtj2u-hdpqxlqhs3uxD8jh9uhBEdJc86bTbx7tVIewtht8GhhSVJfQHOqrSzOuX1fWqR5nNo7vdBuj-6X9xQrB3E5diZQ_IFWcPLrN-M9uPJ4zZq5erfSABSWflvZ66OFLWLXfqtUzkqcbhicBn4pSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6996539c8.mp4?token=uQKwlOt2G8jFaYHp9V2ImxEpwWKlayGCe-FzFeR2ls_dCdHFdp8DUDmIVBoDQibLd8lByuGi5ctxBx3sKI77aMjDJHrsf3rdbjkl3Oi-IiLV-v5q8Yota7K5Gz8ukECv_fop4TG9zKApCH2Tku-0oC78HtRxcL-RqmOKfIlumIB-2hYGK0UtrXf5lQnrTaY4E1WZ1hGETF4WPwOoyPXI0-8n2pcmsdDEep062qV3SYzpimDUVCxmKBwZooNSgVi5eBdZ-z4Z4Wssef8UrqMWsYrA83ffXNi8Is7x2vxhpdzUDjx-pbga7b4stUfxbWD6hwRc46kRtx1EEx1QL4Ox3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6996539c8.mp4?token=uQKwlOt2G8jFaYHp9V2ImxEpwWKlayGCe-FzFeR2ls_dCdHFdp8DUDmIVBoDQibLd8lByuGi5ctxBx3sKI77aMjDJHrsf3rdbjkl3Oi-IiLV-v5q8Yota7K5Gz8ukECv_fop4TG9zKApCH2Tku-0oC78HtRxcL-RqmOKfIlumIB-2hYGK0UtrXf5lQnrTaY4E1WZ1hGETF4WPwOoyPXI0-8n2pcmsdDEep062qV3SYzpimDUVCxmKBwZooNSgVi5eBdZ-z4Z4Wssef8UrqMWsYrA83ffXNi8Is7x2vxhpdzUDjx-pbga7b4stUfxbWD6hwRc46kRtx1EEx1QL4Ox3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیل حملات هوایی به ارتفاعات جبل علی الطاهر در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/123595" target="_blank">📅 08:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QumMHWpgjJDXvKz6WkfqOgQxp_8-DOAo1KwxsyeaGChnu_ytpz50BdofO-ocDdkt1BzXIniBTt7fPlWzyrCEy5Ntp26YqiUpgrfA8VE6JWMVVYFNwD5fYVsi71UpJXYImSu0sJSz_dAw_HLViwGqfcrWene1FCx_eVW9KLg0juMfj-S7kCmD3Zd3Fh9kClUm34jwKHwmRFvO4Utx4Df2F1e01wo6lCMSOFoyD-PcGzrl_kFb9gQQ_M9i2xZa89y4TVhYbtx1rLyeeS19XVUYJ3MJvHOazqHQ_OzvqvpqCMizNYIjmbEmZa61GGGQQRMRg38IesHwJDQe-lPfYHKbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه پاکستان: ابداً قرار نیست اسرائیل را به رسمیت بشناسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/123594" target="_blank">📅 07:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SXQV8qPgHDcBcHZA03uVtmVvF_2jjaN9K9Ctv5IF_PgH7qPYBRCAZixvc5h9Iq0SQUDOBYldWHiIgHMPed-3SN6OhfeQLVvABEDBwFXUt6Irg6S2W0gzEm59umJj75NlPaLkU18CelGaU1HM-ah2X033Dz08Dtvw8UaAjQrPWWRrdO1x0GjplwfVj3WEC93SHUbkf6omgfAdWvixTIXBp6ECjzZBG1QZ17HyeakWbjHKIxdr7A6Nw6hSUUxD4jfy86W7jE3ZUP2Xd8mh1bsGh7_p-hbID-3S8nUcau__sDH8VvMLAoHRXsA_4Ec_aHvB35nVIcajd10sCcgrrXFlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q95Yd8yPx4xyeJ3l8Hq7gZ_TYYGzgqQFAfnLH23dkmb1idGf5jq3PaIBGCEYj_Xj9uLbN443hcvDVBxW8zC0NDztSW4Udx4E-W5h9FD0qUlvn0WNJgeo4KTTVJ2nGmMD6JeM7MZb7gsdunfOi-pMMBqmzrgMVGSDirFMYb9M1dCT850Ji9FLZvXLzF4QfATXOqEIlz9y6EFV75Q3RlIL0bC_imAytEmqyVB-UhSCH_D55siItE4IOOHrtDA6LxWATfD8_DLJSbl_wl8W4eeyotR3LCyvWISo6KvEIlMkNSOofU5dGnPEq7K7t1lLBuJgiJtxw8KAAiI7kj9GJeCenQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان و پرسنل نیروی هوایی هشدار داده است که سنتکام در تنگه هرمز، در شمال "شبه جزیره مسندم" عمان که در وسط تنگه واقع شده است، عملیات نظامی انجام خواهد داد.
🔴
فرماندهی مرکزی نیروی دریایی ایالات متحده به دریانوردان توصیه کرده است که هنگام عبور از تنگه هرمز با ایالات متحده همکاری کنند.
فرماندهی مرکزی نیروی دریایی ایالات متحده
همچنین اعلام کرده است که هر شناوری که در حال انجام یا حمایت از فعالیت‌های مین‌گذاری دیده شود، توسط ایالات متحده هدف قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/123592" target="_blank">📅 07:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NncaJ1LvEoaYpEgHE7hdDy9tKBDWsC79EL6THsQx7aCn0V9JYFJeJGWqmZ8SQMeqVn94jopGnN8DRT_lKu0AwXwF5CLWmmELlcKLdo0oz_A7habaTLiQRKr6YgV0QLhgOr09Aqrfg93KIwVlK6Qe41G4PLI18l1m2XmesdjWDLTUekZA42ayNfpdh3nC6DGXSy_W780BSWxRXforuK_BFx0oLIpYAshJMBlXGFdbjaqBejs1Y7VBAppygkgQ6XkW2ZB_cORxkxTwoVlL22do0itY1aTe8P47CxdbkOYxAysZOuEFd8U4wxmUvWvllQV_UD1ZtJNasmqATSMVWdU1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
همراه با ساب + حجم مصرفی
برای استفاده طولانی‌تر و بهینه‌تر
😍
@NetAazaadBot
@NetAazaadBot
⚡️
سرعت واقعی بدون افت
🛡
اتصال پایدار و بدون قطعی
🚀
مناسب گیم، دانلود و استفاده روزانه
@NetAazaadBot
@NetAazaadBot
💎
گیگی فقط 19T
📩
برای خرید استارت بزن و سریع وصل شو
🚀</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/123591" target="_blank">📅 01:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N84jVPdvkwmHXaLcY-vGetTLcYC18vmKpulUtsuCTSl50FEHBKMh0SPRtsJOF7tGD5IUYlWCZEFp2Y8Ho-Zimr_zF1Qg72fJoPPZpEWwKCJrzJ9appyzXmOTWOLBtFLr34X8ROGEQ2y2d4Fz8Qn_q-bi73fEmDSjHRdfg_1KXdr8IMM5z39XUxJ1fyFeEu390OGQU1ctj1UqHiqdmQw9ngEu2ZjyT-2oWNkWzfEhuk1JpxgyWb8y1JL6Lp2EqHv5292a1cfxfzNf_x6hAF6UyOEzxQTIzPMq2bT_-1NC-uL5erh7GImxPrvFDzi0v-7eTWz81UwCBhhOVBYWYusDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای امنیت سازمان ملل متحد در گزارشی تازه از افزایش خشونت‌های جنسی، تجاوز گروهی، شکنجه و رفتارهای تحقیر‌آمیز علیه زنان و دختران در افغانستان پرده برداشت و مقام‌ها و نیروهای وابسته به طالبان را مسئول بخش عمده این موارد دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/123590" target="_blank">📅 01:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN9fngDrhm8MPw-omzRrOH3xe-gl88gPlkRNr3JliMafGonXN1SROjEAdLfB050GUam4L8VtgDU5XudLX9nED_PVJYgEfPP2ZR0DkT6oEXaisDFQ1zzZQsI4s39r70_1uB2fE14BAlSYE7fi4ZHeeaAzsFwxWoKp4I5mPgex4qTOPfZrSMhomqWAd__sKZZ-bTPF8zvpkQf8_kYIzH9hZfbD0AzqdkrFV8OEl91dbhHrVKUP8grmHdn0LqnHUo9PbTcT-3ZCM5iuksYLdqrxVflQK8qrEfwI1q0825jaB3PMNkhtaXn_UpqFY8Q8dvG3-ILBWjBtcMvbd3l1alTIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مردم ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/123589" target="_blank">📅 01:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYXZ_0lktkx_0nSWCoZyWliX2kp0S2Vvnsh4Mw4-yhug91AiryinGG4sjBvf_4vA3KKbc4iLDf9vcN5xvRjNH1WAtZIyQjC5AD32x8tiEG5CQ9kAs1dVd2_LoovlAEJG6KhlgKWKuYtv4IUojnRa7pJWxql-tMomsd9icTgTfgsfXvZx_RdCPy9e6cubpnPZWFL-GAyBJC32UuSJlyYB82hawRbpLtFktkUUfnTP1evu8XMdViuPL4YCptLBtN-MW5-EhkTaIRoGltKePN1XamzuAYKwxSRCss8Unvylb1rlXwuyc_wqSi80RsriIlxx4MkZ2Ej_JSlvVjsaieX19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/123588" target="_blank">📅 01:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezRjtopcbI10z4mmKxvaiIzmmfxXUEOV_HJ8ueRC72CU0GIEyvcNf_nPeloTF70hqWPkdEFaogFUjeMn_8Pm0ZTUI1UwZnOIcDta7KlCvET2pA1ttynhJbQJlEWA_x5LdVRHQLMw7QgJ5GNiQO6n9oHlTlyVc2j8Iw49YHpw_flxTs2GiSGGWGQ0BSx745ufA1BDHk91FHnantiztUED9soR0VshB7fYOpekHp2Q9m9114wserxD0y2n6-BD-FkJuk0WkivR4NMzU25la3ukxogM_XmDJFnIBmJYZTUIoD3-P0N3v0CeweK06COzMXSeG57XMkamBcuJltFSSiI41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
یک منبع رسمی ایرانی همین الان به من گفت: با تیمی که هیچ چارچوب حرفه‌ای یا اخلاقی ثابتی ندارد، دمدمی مزاج است و مدام خواسته‌هایش را تغییر می‌دهد، نمی‌توان گفت که هیچ چیز «نهایی» شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/123587" target="_blank">📅 00:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیرعامل جی‌پی‌مورگان:
داشتن سلاح هسته‌ای توسط ایران، میتواند بزرگ‌ترین تهدیدی باشد که بشریت در طول تاریخ با آن مواجه شده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/123586" target="_blank">📅 00:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123585">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیویورک پست: ۶ میلیارد دلار از وجوه نگهداری شده در قطر از جمله آخرین نکات مبهم در توافق صلح با ایران است
🔴
این وجوه مستقیماً به ایران منتقل نخواهد شد، بلکه برای خرید مواد غذایی و لوازم پزشکی استفاده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/123585" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9Xk2FpO4rdWp-ebRZi44dFQd3i2lkmFlpqwi5iz4wPr2jQHDQ0cPwm3QX9f8FSSvkCAx8esU7HvnecOxFSCP-nBDVUsNjE_H2uAhBTSKozwqIs8OoPH2-_ugmLS7-Fd6zMfiSM6NuJJlqxpp0tC4uZPUZHaVdXvAQt-WZ1W6-B8haBi5xevXDTYc7ryifLNYhOr4bMAZJNe_cAeQoxn1uxTnejJ_G15Zg4ZExjtNn5SM7ptq9V7LRssmfGsONOPea_B0tI9F6DQ_4xkv82EPYBKPQe9DPVduxmOJP4zJGwjt3RwSiz215yGIlHlT79MIahS7hRMt_rmSJcLlu9Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/123584" target="_blank">📅 00:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123583">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0NhTSxTOpXRd8G2Kh_duGsxMBUdLueL6vhaMExmUsp-G2tk9kEyp1y8rchhVIyL2cPxkp-jMghnjGhbIzLSNpWlyRrb8hV7cayc0NkPKbm6q3I1VMSGndQlPjPdCXv6b6uTvXg0sVz20r--AsJ4nsyxDRimSOTpXVB3f0RVDbCftFFD_vsY37gZ5-04Ps1QW21kk8CQFE9tAxIK6YCFWwDvnmi36sF2KkmwAXz5JI_-PfO7TCrvSIyr1g4OAKTrduML9-yPlMFooz02-ODD7-B_inIgsZgpQIgbTtlzbb_tlR1uFMZb5ZXpz_cal33mOt6v1v3_Pq0VtqpjuoNA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: آمریکا تاب‌ مقاومت جلوی قدرت ما رو نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/123583" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123582">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2jLDpotnFwuUZoogU1c_fwxcGdm0IW46IDGzUWt2vVflNG93PjcQsc-ZgmJbQpNnJlz0_GiOOBS6FK4odBS32U9KuPFOJ79tbJbN3FIQcXnmps2mqOnpv76ZG4ny9cq2kibtS3L4rKcHHHqFQ9fFHtiAL1miARsz4aEnxu6kSQFtRBJ4ziCCucvnY3yEch6HEw_r1nZkXeTGwC5E7HHceEHc_64eDasInP9POYlJRGmuDQ77EAU9OTxrUlFTkC3orHM4pRVppjFwgM47qzQF_4VS-Tnr60OUgwv52wlL5o5H8KDRttzWiCCNZ6BWPen5Tl9oUFIlnMy3Iu_vi4BSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردی که در تصویر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/123582" target="_blank">📅 00:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123581">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/123581" target="_blank">📅 23:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123580">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: محاصره اعمال‌شده بر بنادر ایران به‌تدریج برداشته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/123580" target="_blank">📅 23:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8beb1cabba.mp4?token=qBB3aRu_BJej3zi5Vtpk9ovKx63TBAYOsQ1ipnyVHzRE_c7Tuf2EY3WOOXW91BhrYhtXYgxkkUePcOnnY0t_24h3mMxKKjZTILVnmILQSDzIefx-g2WJWbwtJYj_V-QwighaWT_U0Pv-5OfPzIf2SgIxLoz9kbceluMdNY7lp4K5_V4jmU_tlPbQd3N2bYlac5vSZpAhB1yxb2GhHmmxR2CjAedVrWnX2wQvlyMg2Z94oF1VPfL50-5sqho2Qk2GRnNxGQAS1OFN0hdiwITo5Pb4lD5l3C-rcHEW8GpWUzFqhK3Fi1QuHERIP1GY5o84h4kl33NIFeXaU4E1IfSkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین علایی:
سه روز قبل از جنگ ۴۰ روزه به شمخانی گفتم: آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می کنند؛ او گفت: نمی‌توانند! گفتم چرا نمی توانند. گفت نمی توانند پیداش کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/123579" target="_blank">📅 23:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz7brSAkMMurV62sSX6HCS5Hr_GPrKfno9BPcl4Gsv-_Y100bm4nWYQLf01nH3Xq7FHjQ8HMMGwKijEh4bvvYrLUsXAUeZAw5z7-Au0dNFKMyKZfD0Lf7qZn2-GS7L-pQwrwInKR2oFtxWUV2LWuwUog6l0Xrv7tVOkrauiX0y7rZVAHeOJ3ZT6Pr-0AG0UqViTvimSa0kceH8MhGH9t9FASOu0PVZz2vIeeI5vUvOQhIMhexquSbhbpmURPCcdarRjh-3CxGkJeK72q1zhFWM4xQPJaV2ZH3gw3yE71g_sL0EKUCQ02sHuNwPEF6eznXtGZWS-q7h7utrlPpSQ1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/123578" target="_blank">📅 23:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1defb8b924.mp4?token=ejNp-cEY-_Dl4JYe_gyaRDmWExkevnNd9JyGPZxpO6TfIEzyTt0azKbCIChKEBA7h2xXwK90-dgjzE93-J_BJVEufWmjOo6aotx4zssVCeytoYaMhN-7ozg0Vo7Wcz-ZHtjffJIRZU1bxQzhxtEPOnDHWUlmuN9NOi_JQf14jZ4x5OHDscGhGskVBnQz8bwUVL8mgU7AVFlbwbk25PU3SDF2qXHznoZrwACrJk6kSQuvG5gwEfHoFvBSTXkGQiEyreo-2Ec6qJcBEwi58ZKGsTY5kCbWmwq9c--OBddfnD0JeqBmyH6_XMtFWOlzKQMne9D3QF0gkFIC7sBIgiW4l1BoIKmWc1YDJmrdD-AMPBoWMvN08LbGNso8T3WtJdVrwc5fMu7M3gkRgAk7aoES_QsFGtrIuLDF8Y4wcv6iUL_rtY7hDQxWrvR7ZB-ussPbFD2gvAojO4ptDUT8gEbWrHSd9295ogALns_0CRH0zn0iEev9cRhXv395Ob2sHOfiIUNpJk-mMlA8ckjndKIDhsAE9754pZ6ME_LjjQjvzo7jNAbRx8V4BtD_XUn8N4HJoErFj_AoKmqEXb_fq7kqOhgx8OwvVW7Hr4oo6fzcfGo_dznCgzsD-tdHK5ArNzJhGR0myBtGSiESlEPrdst7gWqsTxOxvHmZeQui_yYIQbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین ماشین حاشیه ساز لکسوس Lx700H با قیمت ۱۱۰ میلیارد تومانی پلاک ملی شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/123577" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0acce2b1.mp4?token=fjDnArTVrUcZ1BbU0eR4UTp5sNzL7a4jtbbjRteBbOgY4ooelx_1u7kqrRqNofCpYK1ygXfHv8K9Wnj1iEDtcSGYUjSttdSxD2P7Nm5id6Ett0Sjp8xjzftms18L9wKtZYOWp_HoLblNCWaobfjzhm5XuJdCfSHtxVHFDkNq9284pdtUHCxyQW58v4VyQdRnvu6cDh8eBcLz3FdMaa7QU4JX2oJkXessw7OqezRceAkFnhDEePIXGMz9_BqwAcAxcmr5kei36WSakVqPn5Q5P9iFWDU18F2jL8fDUE8_LSp9fTp1ovfxcVuFcC5YcAPR4iNlq6JtXS8riVdugbatyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی: کشور های جهانی به خاطر چشم‌های زیبای من یا شما این کار را نمی‌کنند، آنها این کار را انجام می‌دهند چون به نفع منافع شان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/123576" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: هرگونه گمانه‌زنی درباره پیوستن پاکستان به طرح سازش [پیمان ابراهیم] با اسرائیل را قویا رد می‌کنیم
🔴
تا زمانی که سرزمین فلسطین مطابق مرزهای قبل از ۱۹۶۷ به پایتختی قدس شریف به رسمیت شناخته نشود، هیچ انعطاف‌پذیری در موضع ما وجود نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/123575" target="_blank">📅 23:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/123574" target="_blank">📅 23:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/وزیر خزانه داری آمریکا درباره رفع تحریم‌های ایران
🔴
به گزارش الجزیره،  وزیر خزانه‌داری آمریکا مدعی شد که تحریم‌های ایران به تدریج لغو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/123573" target="_blank">📅 23:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAonbBqiu0b7h1DcL3PNKmAEcB88qfCf6ZNstPk7BQx7d25uKiyJYGohLIs-YvpaceVBIctnlQsuAJVzsNkaX1uzc1zi51_CYFL5chvpQHDIGq5L5IyBxuCVVeN-5MkEItm8RUJ2eyFVK4WXsyjVq7UzcFoO2xyaef6yO-3FUI7bUGG7wJWguoKYwyLim60iJfmRPGNFjp7Ab9xao5u4Irt8k08sszAos-DfQOhbSRW05E3JBae2f1TsPMcjgrvM0kqGAliy1IQuhhAbjfTGe2tyHGju9G7EXt-Zjkygc2KpHfhjSKkpHdQJFKifIgk0LJ1oL7DKg-cIF0HuZrMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز اعلام کرد: صادرات نفت و فرآورده‌های نفتی ایران تداوم دارد و امروز یک ابرنفتکش دو میلیون بشکه نفت خام ایران را بارگیری کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/123572" target="_blank">📅 23:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: یک میلیارد دلار از دارایی‌های رمزارز ایران را مصادره کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/123571" target="_blank">📅 23:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کان اسرائیل: نتانیاهو خواستار از سرگیری حملات به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/123570" target="_blank">📅 23:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بسنت وزیر خزانه داری آمریکا:  احتمالاً تورم ایران بیش از ۲۰۰٪ است.
🔴
ما فکر می‌کنیم ایران ماهانه ۴۰۰ تا ۵۰۰ میلیون دلار سرقت می‌کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/123569" target="_blank">📅 22:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT9xwaaoDCC0agxBrCdQtGzLHY4YfEpOP00IqhUKw5ODgK-xv8-wKv-X34wpnvNztYDFp_f74MmlZ4-zGTXIOOT2HsrVX8NLFEUxUnYGm1RFxtXxWiqlIpOIWK3fZVi2vzL49ONv7QIawZinCdj14-vm75Q1bL2bP0Dnjm5DSVBvxS_DdNVFHzQRvFQhXECrPzHz5aDFvwZ6Xh0NFQsfYfOaw_lvYGPERq9A_wby0-d6vN8P1OCeXpq3q05uwq0S_BBigei8Sqf0QIDlx8KQteMjU1MhKgsHKugtwfNmyCx1ASN566ay0mWuOyWvJ-b_lJGuqlMIC7ROOBghpyKftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون در حال جذب صدها عضو نیروهای مسلح برای حضور در رویداد UFC برنامه‌ریزی‌شده توسط رئیس‌جمهور ترامپ در کاخ سفید در ۱۴ ژوئن است، گزارش واشنگتن پست.
🔴
بر اساس یادداشت‌های داخلی که واشنگتن پست بررسی کرده است، نیروهای انتخاب‌شده برای حضور به عنوان تماشاگر با یونیفرم باید هزینه‌های سفر و اقامت خود را بپردازند، استانداردهای فعلی آمادگی جسمانی نظامی — از جمله الزامات قد به کمر — را رعایت کنند و یونیفرم رسمی بپوشند.
🔴
مقامات به دنبال جذب پرسنل درجه‌دار جوان و افسران جوان برای حضور هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/123568" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات حدود دو ساعت به طول انجامید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/123567" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A31axNnlkyW34sF1OSSQFpBHsMeTKB_dyDJfuBx-jwvlme3o9szc0_yOD2ed9amya06-bFc8nhlDYQHaeKKmc1MxZGHO4TcmERUiBu9Zd1NIPkMDwPB9skOqmeaKlcsGaWv0X-6yN4jaTmFX5vBdFYNu3GaHfUBKAKVqmKplaR-lLhSScseSoXXRrdhiijY9EN9nS3_UwQrrnjbM_rI0BJ2bMCNLiqCCzPEtbxpzwkFRD2HksjKia07HBjDpiIg6wdAqWchVdOgA7s5j0Sw71TwASATF65aJW0wMyCu73YC46poYEkjarE266s01zae8P8-0-jZVeParx1RdR3wbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/123566" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام دولت ترامپ: ما به دستیابی به توافق نزدیک شده‌ایم، اما برخی از مسائل همچنان مورد بحث هستند.
🔴
نیویورک تایمز به نقل از یک مقام دولت ترامپ: موضوع دارایی‌های مسدود شده ایران همچنان مانعی در مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/123565" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت خارجه پاکستان اعلام کرد که وزیر خارجه این کشور در دیدار با روبیو، وزیر خارجه امریکا ابراز اطمینان کرده است که تلاشهای تحقق صلح منجر به نتایج مثبت خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/123564" target="_blank">📅 22:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خبرنگار الحدث:  نشست ترامپ در اتاق عملیات کاخ سفید درباره تصمیم‌گیری در مورد ایران به پایان رسید.
🔴
باید منتظر تصمیم ترامپ و اعلامش باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/123563" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDRh4clKS32bjzQpsAMkMp8qE3gJY-L3M-IKQtYsgXP29adQRrPxscwtZGERp8n3Ofq_PUJCotQjZTcGN8E4YptoHlnhL8G49xaEIBfD0w_j7XmnID_zVfQk83dPyKtza1xXKPMiUuxYYzef91hNWdqr8IT1l-g22PqGR-k_TDtwDqNKnYFqUrVZuf3md-EN4RE98QjP9rSlpvg1hu3CuwfjozxRXz56FvI597CmSvOrAmXg8zmwJmga9LkA4Itr42Swp841_LjJnLmj6WpenMm2vbniZY8nXJ1DpXOVvbdrHi27MZLWw7GUvayKtzBk9EG_VCPXeWyrGra9Vn75Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای پهپاد در منطقه خط تقابل، شمال اسرائیل فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/123562" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p74E_n0KpMAcgoOo776m8iSn86IieYOOq3-pb8BR2WffCc5IJ2hCv9KngAL-Z890DSF3Ef7scn2I2evBOt4YtrhIgkfECK56Y_xG0M4KAWII_Q6ZofCfXnKkPoAJJ6mdSWtnILVJ_cIkb1c3ehVRozv1PpTevrF0bpcC3qWAYCnj4ofjU0JTHnRcpMTTc2j3n0yKR00rWqZT-AOTL7xf53-9Jrt5eMGplPMINBkP44mumreEpxFGNAwi-palz3z-HtsYKG0VfonSYS2jbQnvUIFnt2XfpXbBJFvNnIDXLFgnyEd9WLiS_GTBqC102BUnPPd4e0wwnuv1nQGUtb9csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شش فروند هواپیمای ترابری نظامی Boeing C-17A Globemaster III نیروی هوایی ایالات متحده در راه خاورمیانه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/123561" target="_blank">📅 22:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: خبرهای مهمی از نشست ترامپ در کاخ سفید بیرون خواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/123560" target="_blank">📅 22:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه تلویزیونی اسرائیل به نقل از یک منبع گزارش داد: هیئت اسرائیلی در مذاکرات پنتاگون پیشنهاد لبنان برای خروج از لبنان را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/123559" target="_blank">📅 22:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ارتش ایران : یه پهپاد دشمن رو سرنگون کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/123558" target="_blank">📅 22:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ترامپ ضرورت خروج آمریکا از اطراف ایران را نادیده گرفته درحالیکه این موضوع مورد تاکید قطعی ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/123556" target="_blank">📅 21:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=iWvAd5mDpD56K7hQotx-U6pVGFSiEQj2w_3DLLEnrD5-yUgMthU0y8mHYWN7QD2c0lBNELSXvfT9eDD_dQqRYAbQwpDkASpn6k5Kmqipl_Er9ioFc5t9j26PHTubu8xkZVKS629l5VMBpL1AukvENa_N-va6wS9jUd8o2xuElBPVScmIt9_N2yjOMNLjObBTa55VhtImCORz5TmVLJf1l5s0ssi95bih8AEq_cSqshMAMPGShPTqHnqIQaIUmYPuyHTAaETau09FVFBQMcQQDXWEVRcWRJEPJvpD-emr3EXkKZy9PGg_fwUQk0iH7RJmRcuINMv18MmFJeg7FjYAAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=iWvAd5mDpD56K7hQotx-U6pVGFSiEQj2w_3DLLEnrD5-yUgMthU0y8mHYWN7QD2c0lBNELSXvfT9eDD_dQqRYAbQwpDkASpn6k5Kmqipl_Er9ioFc5t9j26PHTubu8xkZVKS629l5VMBpL1AukvENa_N-va6wS9jUd8o2xuElBPVScmIt9_N2yjOMNLjObBTa55VhtImCORz5TmVLJf1l5s0ssi95bih8AEq_cSqshMAMPGShPTqHnqIQaIUmYPuyHTAaETau09FVFBQMcQQDXWEVRcWRJEPJvpD-emr3EXkKZy9PGg_fwUQk0iH7RJmRcuINMv18MmFJeg7FjYAAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از جشن برداشتن محاصره دریایی در قشم و شلیک توپ ضد هوایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/123555" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/123554" target="_blank">📅 21:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/123553" target="_blank">📅 21:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqmnX8tRg73HOsdYUaPqj-sa1O1oi7ltuhHF2qIhh-Pj-PCqlNgnwOZuzfOdLbe84drnOCFHVE25tSoF2khj3VEqLjkbzFHO23HqzOpJ6SlWo08W8XIhipxh0ywQ6mqyleSTvueimvPpSHj9_zmyNd_nhgAgbzj4OsKSEa7kcTcIQsugu7ViMF6uD-Ba4Ft29RLui56FV_FNuj8ac3TLTlVgwLraytv3qcDdSF4aUUdBDADzfq4U23kaiyeI5IXuWuxSNIynRQua0XlTdBair0GNbTE-XuJgU_xCRa7BYfyOyqTPwjNhGqIELccTGn_1-1NSPHFZlY8Pb3IFNLWxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/123552" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / گزارش های تایید نشده از فعالیت پدافند در قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/123551" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123550">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
زلنسکی: روسیه در حال آماده‌سازی یک حمله بزرگ‌مقیاس جدید است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/123550" target="_blank">📅 21:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جورج مالبرونو خبرنگار فیگارو: طبق گفته یک منبع عرب در تماس با میانجی پاکستانی، جرد کوشنر، داماد دونالد ترامپ، مانع از نهایی‌شدن توافق بین واشنگتن و تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/123549" target="_blank">📅 21:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گروسی، مدیر کل آژانس بین‌المللی انرژی اتمی : توافق ایران و آمریکا خبرِ خوبیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/123548" target="_blank">📅 21:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اسماعیل بقایی : مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/123547" target="_blank">📅 21:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ایران هنوز متن ۱۴ بندی ادعایی رسانه‌ها را برای آمریکا ارسال نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/123546" target="_blank">📅 21:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
منابع خبری از خاتمه نشست ترامپ با همکارانش در کاخ سفید  در خصوص ایران خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/123545" target="_blank">📅 20:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: با «زبانِ باید»، ۴۷ سال پیش خداحافظی کردیم
🔴
هیچ یک از طرف‌های غربی که وقتی درباره ایران صحبت می کنند، نباید از باید استفاده کنند؛ ما بر اساس منافع ملت ایران تصمیم می گیریم.
🔴
بایدهایی که آمریکایی‌ها مطرح می‌کنند، در واقع خواهش می‌کنیم است؛ تبادل پیام‌ها ادامه دارد و تفاهم هنوز نهایی نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/123544" target="_blank">📅 20:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یک مقام ایرانی به «رویترز»: عملا به تفاهم سیاسی با آمریکا دست‌یافتیم اما نیاز به نهایی‌شدن دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/123543" target="_blank">📅 20:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تاکنون تفاهمی با آمریکا نهایی نشده است
🔴
در این مرحله بر خاتمه جنگ متمرکز هستیم و درمورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم
🔴
بقایی درباره ادعایِ از بین بردن مواد هسته‌ای توسط ترامپ: در این مرحله تمرکز ما بر خاتمه جنگ است و درباره جزئیات غنی‌سازی و اورانیوم غنی‌شده، صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/123542" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رضایی نماینده مجلس: مخالف تعلیق غنی سازی یا اعطای مواد هسته‌ای به اسرائیل و آمریکا هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/123541" target="_blank">📅 20:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وال استریت ژورنال:
امارات متحده عربی ده‌ها حمله را با هماهنگی آمریکا و اسرائیل انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/123540" target="_blank">📅 20:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGws26NNF3nDpp0ZjOV3QC9Dzo_lV-uWNVfi5icOFPAzaI_qoU6gHu7dXTBW9koId4Tfk9x0aQWr0dEbfcRrOnnNrYLvHaYZ3yTWjzvvEURJ1F4Nl0rvKOLR09YWVJ1cDHjz5gFOiyLLQDQv6-RSCyAKF2s9s8KyHAH47gg7SL4pnOPOffxO_hvo_9pMLKah0yO4wsI9dIOOwTjxPDLMEvqQTDSXcjPtrW9zXYj2UnxVlosKKfe5RkgxH2M0rkd8XhVFuuwM5C6kSFvRyLUtX0KErn6JKQd3lQr2dLQgSYNQLJimQ9jxljBiPYfHXcLuFAbuNB9vGk-cpsRDIcUYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: افراد آشنا با این موضوع گفتند که امارات متحده عربی از روزهای اولیه جنگ ده‌ها حمله هوایی علیه ایران انجام داد که تا روز پس از اعلام آتش‌بس ادامه داشت، دخالتی عمیق‌تر از آنچه قبلاً در کمپین هوایی به رهبری ایالات متحده و اسرائیل شناخته شده بود.
🔴
گستردگی این حملات گواه دیگری بر تمایل روزافزون این کشور برای محافظت از آنچه منافع استراتژیک خود می‌داند، است و آن را از برخی از همسایگانش در منطقه خلیج فارس که رویکردی بسیار محتاطانه‌تر نسبت به تهدید ایران اتخاذ کرده‌اند، متمایز می‌کند.
🔴
این افراد گفتند که این حملات با هماهنگی ایالات متحده و اسرائیل انجام شده است که هر دو اطلاعات ارائه داده‌اند. برخی از این افراد گفتند که این حملات شامل اهدافی در جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاوان در خلیج فارس و مجتمع پتروشیمی عسلویه بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/123539" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
🔴
به گفته گروسی، قزاقستان آماده است در صورت حصول توافق بین آمریکا و ایران، ذخایر اورانیوم غنی‌شده ایران را نگه‌داری کند.
🔴
رافائل گروسی، رئیس آژانس بین‌لمللی انرژی اتمی، در گفتگو با فایننشال تایمز گفت که قاسم‑ژومارت توکایف، رئیس‌جمهور قزاقستان، این پیشنهاد را در دیداری که این هفته در آستانه داشتند، به او منتقل کرده است.
🔴
قزاقستان میزبان بانک بین‌المللی اورانیوم با غنای پایین است تا تأمین سوخت نیروگاه‌ها در کشورهای عضو آژانس بین‌المللی انرژی اتمی تضمین شود و از اشاعه هسته‌ای جلوگیری گردد.
🔴
گروسی گفت: «ما محلی داریم که این [اورانیوم غنی‌شده ایران] می‌تواند با خیال راحت در آن ذخیره شود»، پیشنهادی که به اعتقاد او هم ایران و هم آمریکا می‌توانند آن را بپذیرند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123538" target="_blank">📅 20:16 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم به نقل از منابع ایرانی: اصرار ترامپ بر عدم آزادسازی دارایی‌های مسدود شده، تردیدهای تهران را در مورد جدیت واشنگتن افزایش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/123537" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پوتین : اوضاع توی میدون جنگ جوریه که روسیه می‌تونه بگه این درگیری داره کم‌کم به آخرش نزدیک می‌شه
🔴
حرف بعضی سیاستمدارهای اروپایی که می‌گن دارن خودشون رو برای جنگ با روسیه آماده می‌کنن، کاملاً چرته
🔴
روسیه هیچ‌وقت هیچ نیت تهاجمی علیه کشورهای اروپایی نداشته
🔴
روسیه برای مذاکرات درباره اوکراین آماده‌ست و از اون صرف‌نظر نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/123536" target="_blank">📅 20:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b181524b.mp4?token=hc6y-xgNz6IzXJWQXdxCEx35OiGZWKXgf_uEhIijxaRGzvmFvseLuN7B9mcgoH1qxPyg_ZgkvvhwLxZ1wa7cLELy3s2hKbkky-qjE5zu57xxG4qG5OPapO5e8Moh1gCJc2Pb74dVzfmkDkQSBWnQ6FfxXbC_EqQehNmyxMaW0jaB-yr3iMN7rUgfidBJyHlWrxhKzFf-wuKFUOJpdn_I87oTZvT5JWiwyLuOPyjxcuX_YThsLtV5bB0kYg0uYT56WIkAolbbZFSSOx1bzPIGTPezr5WgB07TXIqJmaG2i_zXsGe4oUFgFkbuwiZaD20x-S-RAQ6Xt4vrw0h69YJXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b181524b.mp4?token=hc6y-xgNz6IzXJWQXdxCEx35OiGZWKXgf_uEhIijxaRGzvmFvseLuN7B9mcgoH1qxPyg_ZgkvvhwLxZ1wa7cLELy3s2hKbkky-qjE5zu57xxG4qG5OPapO5e8Moh1gCJc2Pb74dVzfmkDkQSBWnQ6FfxXbC_EqQehNmyxMaW0jaB-yr3iMN7rUgfidBJyHlWrxhKzFf-wuKFUOJpdn_I87oTZvT5JWiwyLuOPyjxcuX_YThsLtV5bB0kYg0uYT56WIkAolbbZFSSOx1bzPIGTPezr5WgB07TXIqJmaG2i_zXsGe4oUFgFkbuwiZaD20x-S-RAQ6Xt4vrw0h69YJXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین، رئیس جمهور روسیه : ما باید سیستم دفاع هوایی رو تقویت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/123535" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL7sjDktGw6S4tp0J1OFNuIaTZDY_dGe8xb0bUnXsLxVwCeQ4bI7jT6Ipjsuh2Oz0MnxDftzFwpi7Aw5B4M-c68Tl4RS8-3eupRT49IHMcMcoJXPcFP74Tnff_f0acEeJfMvidttOPWQjcQSxl0jQUx-TRJS-GMT_qD70H4Xk-dxcuRo6llXtzxf6dRDBrqhOr4pcUlArDcuZido-QTMD2DqQJ1I0Ry8r5BIsVR5gdLgZUNgc0xJH9WFyVqKB209ipv2ltQim-Zru7seujNq9t35CX-HlHus_2ecGbmSMcT4XlgFqcCLpbmO9BEfl1hwnjMaA5ze3AioulqDAszhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/123534" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پوتین درباره حمله پهپادی در رومانی: هیچ‌کس نمی‌تواند منشاء پهپاد را قبل از بررسی لاشه آن ادعا کند.
🔴
به هر حال، ما می‌دانیم که پهپادهای اوکراینی به فنلاند، لهستان و جایی در کشورهای بالتیک پرواز کرده‌اند.
🔴
واکنش اولیه دقیقاً همان بود که اکنون در رومانی است…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/123533" target="_blank">📅 19:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره: یک منبع مطلع به من گفت که پست دونالد ترامپ در شبکه اجتماعی «تروث سوشال» درباره لغو محاصره بنادر ایران، در واقع اولین شرط پیش از برداشتن گام‌های بعدی در مسیر تفاهم بوده است.
🔴
به گفته این منبع، طرف ایرانی بر اعلام رسمی و عمومی این موضوع در وهله نخست پافشاری کرده است. به نظر می‌رسد ترامپ این موضوع را امری فرعی قلمداد کرده، در حالی که تهران آن را گامی کلیدی برای ایجاد اعتماد پیش از ورود به پرونده‌های حساستر می‌بیند.
🔴
تا کنون، هیچ بحث مستقیمی درباره خود پرونده هسته‌ای صورت نگرفته است. انتظار می‌رود این فرآیند به تدریج و از طریق یک یادداشت تفاهم (MOU) پیش برود، به گونه‌ای که هر گامی با یک اقدام متقابل همراه باشد.
🔴
همین منابع می‌گویند انتظار می‌رود اعلام آتش‌بس بین حزب‌الله و اسرائیل نیز به عنوان بخشی از چارچوب گسترده‌تری که در حال شکل‌گیری است، انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/123532" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ناتو: اوایل صبح امروز، یک ساختمان آپارتمانی در رومانی توسط یک پهپاد روسی هدف قرار گرفت
🔴
ما بی‌مبالاتی روسیه را محکوم می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/123531" target="_blank">📅 19:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از مقامات ایرانی: این توافق به نحوی تدوین خواهد شد که در صورت نقض آن توسط آمریکا، امکان اقدامات متقابل فوری فراهم شود.
🔴
توافق نهایی بر اساس خطوط قرمز ایران و بی‌اعتمادی به آمریکا تدوین خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/123530" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / العربیه: «فایننشال تایمز»: قزاقستان پیشنهاد کرد که اورانیوم غنی‌شده ایران به این کشور انتقال داده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/123529" target="_blank">📅 19:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری فارس: مهم‌ترین بخش توافق، پرداخت فوری ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران و آتش‌بس کامل در لبنان است که ترامپ به آن اشاره‌ای نکرد.
🔴
طبق متن توافق، این مبلغ باید فوراً پرداخت شود و تا زمانی که این پرداخت انجام نشود، ایران وارد هیچ مرحله…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/123528" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرگزاری فارس: مهم‌ترین بخش توافق، پرداخت فوری ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران و آتش‌بس کامل در لبنان است که ترامپ به آن اشاره‌ای نکرد.
🔴
طبق متن توافق، این مبلغ باید فوراً پرداخت شود و تا زمانی که این پرداخت انجام نشود، ایران وارد هیچ مرحله مذاکره دیگری نخواهد شد.
🔴
تنها در صورت حل این مسائل، ایران در مرحله بعدی در مورد لغو همه تحریم‌ها و موضوع هسته‌ای، مطابق با خطوط قرمز خود، وارد مذاکره خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/123527" target="_blank">📅 19:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gilkL_M9cCarEJ4GFQwRe4oFlDqUoSl_9mjHzmYfO-6TodxDdFg93Mj1cAc0Lf_l44RVxoz8-swNeaQgW24f75vwaB_eiI6mGnBtrByYt7u9ukDoAdcf0xfKephEUj9jJd9zFde9ZOxXd8ADJlnOKmB40iP1TbG6ptrqvfrtUYRKqNgR09g_7CMOW3IS9DG0piL1Ue5X2HvcFwBt-sflMoswCV7iMYePMSRJMLh6SmaSKUbWq8ixvCmlxENCuKW2MvqR3v5ZgNjzXuFewNmdYywZg8f_QENH_Wv5CuOH-0_ggapteDgY2d9OpIsqYxTVevExgGMkxCAgJYFYb2Amkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«آکسیوس به نقل از مقام‌های آمریکایی: ما از ایران درباره مواد هسته‌ای تعهدات شفاهی گرفته‌ایم و مهم‌ترین موضوع، آن چیزی است که در مذاکرات بر سرش توافق می‌شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/123526" target="_blank">📅 19:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeZICcLzL1ko9tJ8WudTa3-9mJlbcvA-h-8GKiCd9pQgs77Je8uZEz_xJKhNqes45ZQMKTKDpf-2JihZuhORpPeXIdN1LyIr6RRL_Bfj7vR2gXvdDaMauLEdj-3r0RLRlWTnhCwV0-YUIy_xLweJh9fyts73_YO6pJx_4ZByqoPzyJtKKoaqpFkeWGODQdR73i47AhY7_NjzTKeqmnyQAeyi0QLEUAM_lSF-bsksrRopb42gOdYReqC4MIJlxO7Gqw9qlkosBVmBvZ_f01K3Ua5pRnRnVIYRyXRzf4bJvmfwqtJ9-RGsNmogXKoGr83QGHyCndMoa9Qn4EUids0DBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: توافق مقدماتی آمریکا و ایران نزدیک‌تر از همیشه
🔴
مذاکره‌کنندگان آمریکایی بیش از هر زمان دیگری اطمینان دارند که به یک توافق مقدماتی با ایران نزدیک شده‌اند. نگرانی اما بر سر جزئیات ریزِ برنامه هسته‌ای ایران است؛ موضوعی که حل‌وفصل آن به ۶۰ روز گفت‌وگو موکول خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/123525" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
