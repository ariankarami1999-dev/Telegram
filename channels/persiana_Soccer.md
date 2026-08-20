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
<img src="https://cdn4.telesco.pe/file/KNK2dGQNjCCP7P6Un-ca7UujtjM4aCAUfUkpa4_BQOx-MLG1jBpQiHqUEOf-qVpbzTb148cK9zK1fgY8aQcFqqqyYpCCgPPI4Esq8uRN6-WgxJspRnktqU1goSa47THEMSNzz50Wt59DERFwO7pkgalrSsbZ47FB2Iw3F_tJFtrUKJfG-BflO7hMpgzdgwhJKBDcbLxVms61RKWpTslv_aPFdZ2ATKWrF7YvGhczPrNInQuxe0f00G8qV7M0-4jTLbV1OR0asFk0bWtMdAzmZRlHnEQ9z_Kbu2n84vGO8H1kGv0HebA9ARey4rGuG0f-OV8UBy0uapSJtdvlLlnMCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 621K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 20:29:52</div>
<hr>

<div class="tg-post" id="msg-28139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=PDY-exZc7My1C9Cgmv6qQ2mfB4-tGMWRuS1NXbuERgf0e4b3ShwyMTumciwcCBgdbgCG2h6HLc9vxuYVPDwun_iwqtTeSQYex-cEPlwk8PV0lsjtRnwXi-eZFcbY9YhHTBAA_6GRHBWywgFodwepkjJgD7ZXKk_R7-F4BoRjasgl5EE-Zc4W-x3hv-CvQfY1OF6bf4aI46BqWQXBc8oKLyzRaA6ZHZdeQo6dZmimrq5JcqvjLMH3gvQsEbXF5VYoeLNh7LHxb5ZPol6Ug8v-sTe6wby2QWhVcuF3i0elotuQMvhoOGM8ndPq3NBLeHsJ8ioPNrSgONrHIdyhB2AZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=PDY-exZc7My1C9Cgmv6qQ2mfB4-tGMWRuS1NXbuERgf0e4b3ShwyMTumciwcCBgdbgCG2h6HLc9vxuYVPDwun_iwqtTeSQYex-cEPlwk8PV0lsjtRnwXi-eZFcbY9YhHTBAA_6GRHBWywgFodwepkjJgD7ZXKk_R7-F4BoRjasgl5EE-Zc4W-x3hv-CvQfY1OF6bf4aI46BqWQXBc8oKLyzRaA6ZHZdeQo6dZmimrq5JcqvjLMH3gvQsEbXF5VYoeLNh7LHxb5ZPol6Ug8v-sTe6wby2QWhVcuF3i0elotuQMvhoOGM8ndPq3NBLeHsJ8ioPNrSgONrHIdyhB2AZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/28139" target="_blank">📅 19:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/28138" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBFMuwV7D1_yGvVevwC5UT8G6GO6nwCUCkgOG2zcMRZGx7IyARr6fGM57beOqY0mE3NmNo3CeU05hgS2UTkazibhbjrc7lOYr0uYYyNNbIs3Qp58ktB11Db5TRuqLJYnLmIPNJ1MUOq707-N3mJHFsL7aM6qSbgz3iL_Uy_POH6OM2J9HF4OjLg5v6rBExOyLURTfopGN4mlUPubu3OAFsDQI6byqJPjqKfRcaBQzteB6vHR1md4mC3dwFbjlu3MEgn3Ztge8gS52yBYue3rmzT_hz-AlNGoMS_YBFSCakYsuPDALfgxoD9iqSMSJ7yLVdxymWIdlJK9jFCr65NmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آلباسته برای منیر الحدادی ستاره مراکشی جدیداین‌تیم؛ کل دستمزدش برای  دو فصل حضور در این تیم 900 هزار دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/28137" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSAtQM3F4a0eBlSEltBlrYs5CKkdpsWCZufZXWssxpbeS9bVb3D35v1tvW2rKGeOZnolk1nJeXKuuAUevddLAoaNwJYoxkLD9N9dfBObXyPckOmYj_oDrq3tAr_Jr12AFFUI1SDLE6K0GmmSWmS1mP5ytrAuhwSBs1VmUu81q7fl4cr3fAGqhg1aPGbdqPmpTz3h6VKlno8-Xn2LFS28owMbsA52Yx5Tp9ZVKX_U6RfCXjCQK_7Gzf56odHLwDCdvW_aTkLr4EiaRtTAv6-AXS7Dhw6SEEb4ElCSy9R9EjOAH_Gqkxx8k7ztG8OuR7BwVm9u7LgtRF5xRT0VC-Q1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ علی نعمتی مدافع‌میانی‌سابق تیم‌های پرسپولیس و فولاد خوزستان با عقد قرار دادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/28136" target="_blank">📅 19:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJRizaq8bXt21RasQOXSZWR1WmO6vCIxNDgzLn3rtsFK_wTr4wj8mcLoiX0gHZQdyIOMGQkl6hKVNjGirrAPs8ty2-63gma-9wrMZl5sU2oRuBv0kcNZwiPghCChxkn4Cl79PQoeXiBSXknY7XNYYVi6x7nXEFy_z78ZfDO4hw5MLmdpH51IJtJmK0W3svKb0M8YHXY_DJ7cscJZvlnzKkExKEkPC5GPkPl4IPT8WQHppJg0t1VOgMgwT1Kroi8Wmdf9wHCy9NHWwxP_xSV8_JxufmgbkQQhLtxe0lvqXtu-WRq60QaHpuL4mTmKWmbpQ0_PTEBSGe5aWhOEWPpSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونالدینیو شاعر فوتبال‌جهان میخواد در سن ۴۶ به‌مستطیل‌سبزبرگرده و برای تیم راوانا در لیگ سوم فوتبال‌ایتالیا که بخشی‌از سهام این باشگاه روخریده بازی کنه. رونالدینیو اعتقاد داره میتونه کمک کنه که این تیم در سال‌های آینده بسری‌آ ایتالیا صعود کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/28135" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqghTluTIo9lufgcrRY4QMGy2Mz0seWQYdtIrrx0BpPuhSlBd-6IiFdsaP6JDugLjvFfCnKNXlrmJVMLbs_NTMHqPbRXunjpX0ODXuQF8vtIgEKdOwBTJ2w1VqBZ_d4at8aSUNnn4qpAMtN8QBBTCy-50eds5WsY3J477QQbAzwSrRE0R7DTtR_uPWgqRKEzQeTr4zuKE_iziug6BUIPjo8kqaBStnY58AvLVyumWavg3x45DdR42iwO_mgqj9q9RzCOKkyQc74pQy-fe728TPHNC8ZH8aGG7kcNcWrEzsKDRYCyb8nYmZgOJRlKB1nQsa-bQ0zg_OFckZL65KQA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/28134" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=n9g17yWcchR9O0qXqkWgrfZaUmfv4wNO6Sg3Co7-SSgzGnpQA2Vx2wafcwhNjFw__x0OghfqW7OrwFl377vZUMM49EmWj7d2cXQmZ23UjAuK-INA2pO0r108ZUJ1yvTm0t64F5box2AYkVTd1EEYW8_F31jO1-hGl5aK_o8hmKUzhyarqjI2ujn-ikboVdZb0jONyzEzwyMENbcUS9DDNSJedDEYeIQ0HxviUgQiTR5sRrnjl7uSmoUXep18u7uuOziqrhhGKNFFW1K-Tb9FahkdfyXdW5YNfv6VtccGA3NTH3mY9reWKDnUUcnO6c1D0Zj1AtYzEqtzObz4dbPWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=n9g17yWcchR9O0qXqkWgrfZaUmfv4wNO6Sg3Co7-SSgzGnpQA2Vx2wafcwhNjFw__x0OghfqW7OrwFl377vZUMM49EmWj7d2cXQmZ23UjAuK-INA2pO0r108ZUJ1yvTm0t64F5box2AYkVTd1EEYW8_F31jO1-hGl5aK_o8hmKUzhyarqjI2ujn-ikboVdZb0jONyzEzwyMENbcUS9DDNSJedDEYeIQ0HxviUgQiTR5sRrnjl7uSmoUXep18u7uuOziqrhhGKNFFW1K-Tb9FahkdfyXdW5YNfv6VtccGA3NTH3mY9reWKDnUUcnO6c1D0Zj1AtYzEqtzObz4dbPWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
تیپ‌واستایل روزگذشته رامین رضاییان روی نیمکت تیم فولاد 11.5 میلیارد تومان ارزشش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/28133" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJpMDXnwM5X6J44exGNGMRqV_YbFA93u259qmq6EhlcPtT8yt9SBvrwLkyJfpatczE340DPvWx10eh3Mq8a9kDhld2bv5q49ZKnqJnY-sTRT8B0sOCQMBo069HT4_l8s4Ci0F1CtD73GnOwEDhYZe8r1t-ybP0Rb3UZMznNfNmJi2-9IsYFcmZGyFCAOX7YitYu7605fi9LjIcr0njL4UDDthgSN3bw5WOXNHE5y3kK6F6YOwMQymBuDyRpmdDxOnJTn-KGqI0yaBYEFc-z1ih1PSt8jqkm5u4ieeqxJ27zvp89f9NLgVcY8titEfEdNHhTtzeOQbmLZ9IP2zGp7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/28132" target="_blank">📅 17:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd5XC3AjmjMlpxHBAsL807zYhxNzhyIn0-5Z07MzaX8_GQQGt4krGMt9fQe5SIbpf0_IVTzJIkAGNsweK7fEzCd51owJxJUvJfWpI1NXMZlV65k-xBGdOHCfXKkGW0yRhrAX7ZiKCKaXnVRsfCReECrmjfuFfE1ugqcHnmcHAVlH-63xOhHh5FXwQHHbx8IDf7GpzD74knku2ssMpOz2mPAnc0FaF2-54Lh-MrQPgimE8nJazZGEAhsuIsa7Nfx_vtIwQ5qXNgdiRBWOPW7vtrUytrp1-NzJwbfABVsu8XfMCeVpi6bQ2lq5hTacA9_Sb9YF934EBc1gKDdsRoeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های پرشیانا؛ باشگاه شباب الاهلی امارات پیشنهادی دوساله سالانه به ارزش 2.5 میلیون دلار به مهدی طارمی داده و به ایجنت او اعلام کرده حاضرند که رضایت المپیاکوس رو هم بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/28131" target="_blank">📅 17:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqkO6n4nKRwZMRYov2ZN48CmuaKVHJqJm1bu9KflZJLikfmTJNT-GfnC26al942zlXBHP5Esl6DXF7LoFbp56zEOuUFqOZaLqoD98l1TQrRLkGXMYier6tfQExnha-s3Q9VgytzFCqnGZaiyJxFDBSjYH5U-76Z9FHD8zoIyaA_yfl-nXAN6NXXzMoU9N1b8BPgPYUvgpszImkE0mrH1spTtvh20SnxLnpSf9ncw3rqB7Ig5rINmhVBmIgnYGOV7XaH12nAFVTxlHFovL2oGBXpK-MKDNtupn32OHhUFDfWkDtg2TJWfZsoPG7-2nRM7NMZdk-96n6aXCcyf0Vh60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ شهاب‌الدین‌عزیزی‌خادم‌رئیس‌سابق فدراسیون فوتبال روز چهار شنبه با مدیران هلدینگ خلیج فارس جلسه مهمی برگزارخواهدکردودرصورتیکه‌طرفین به تفاهم برسند عزیزی خادم مدیرعامل استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/28130" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=sk5NgfR9pjHBids_SooaCeDn5pz3jIS9uw0tFPfcxjdRfduUpvoCmVn0SaO9twnamRsYsjyySsIFelxGevlsRRoBIMNWv_q0Yn2p54MXN13Ygo3bchjGxdqEJEmdjOrBRYp63jYammvu3IPkSpNLeB471avSX81xXTr5eBAzDqNko2JyIZ5o0sV0layBgZaPvzneAJDaXCNAsysRM5Z4M2GbElyIJtsDF4UmRo0eUBlRRA6upim0lTeACiJ-5zw37U_4ulPVaHPA1CIcTRIFcNNOVo0S0PGlTGI7QFHy8V8oHMvi7rW_3X8YLQnKP570nQfHkuQHtzBPPu7XLfWbvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=sk5NgfR9pjHBids_SooaCeDn5pz3jIS9uw0tFPfcxjdRfduUpvoCmVn0SaO9twnamRsYsjyySsIFelxGevlsRRoBIMNWv_q0Yn2p54MXN13Ygo3bchjGxdqEJEmdjOrBRYp63jYammvu3IPkSpNLeB471avSX81xXTr5eBAzDqNko2JyIZ5o0sV0layBgZaPvzneAJDaXCNAsysRM5Z4M2GbElyIJtsDF4UmRo0eUBlRRA6upim0lTeACiJ-5zw37U_4ulPVaHPA1CIcTRIFcNNOVo0S0PGlTGI7QFHy8V8oHMvi7rW_3X8YLQnKP570nQfHkuQHtzBPPu7XLfWbvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزاز بازیگر سینما و تلویزیون به این شکل از خودرو جدید رونمایی کرد؛ رولزرویس کالینان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/28129" target="_blank">📅 17:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-yWfhSxQtDcd1pS1ngEojRwMHI1HWz7_2cP6w94boNf2uKsvZL8CgynUtnE6kHtrNr6eO7fUsJUyOPtD-TrAfTdpmNzR-6wCjc6K_t50jns1XPrxt5hd35b_tprigMUiaJ-SxAnGuZMa4UsDLGsliJKp9qOyNPX-YL9cpUx2NQX1H8dIvWOCGWfYWeg6HSVu2X9Bb9OOIfQ72qFMB1ClABDuJCOqoVtxvcGgiN6QJ882xezTJOxITimjQw10d865oSbqdSRQK7sgFg8cxAc54X6Dk54UHKeeBNFCc_RSzoULRJEUzbNkPXVhvDuhaD15H1D7PAjvmYr_pt69hCbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی؛ کادرپزشکی‌باشگاه استقلال در تلاش است‌که مهران احمدی ستاره آبی‌ها رو به دیدار هفته‌پنجم باتیم پرسپولیس برسونه. غیب احمدی در چهار هفته ابتدایی لیگ برتر قطعی شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28128" target="_blank">📅 16:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG8z3GnGRxw7A1_cC_PmRZWhYgcgOfFcY-GpdKRtXVYBbo33EevJaBvtwQ2QywJAS39oKItthtuQN76y0dv3Ghhk6AUQetYq1Sx_fQqIt4JODsH4iAdMJvnqQCKgM9uGHwTw8nPS97_KeOLM_VqTGOHI8-aGgqH2l-mlJmSvUKpQqJAnFIqKSUVoMFatymMB1pTLs0ic95gHmYpBGm1Dch6L9KMGfJq0voXuYgv7Il3SqbPmFScMJw1OsUipOLa-is7LAYOdadbaKi5Q2kX8jvz2LmEkdfFKT0Joa3lhrWwrkDdqJWsG2G0An_0jEpb071Rc1UMed6r6Lg-dntsW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام رومانو؛ ژائو کانسلو مدافع 32 ساله سابق اینتر میلان با عقد قراردادی آزاد به مدت 2+1 فصل به تیم بارسلونا پیوست‌. کانسلو پرتغالی فصل گذشته قرضی در جمع آبی اناری حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/28127" target="_blank">📅 16:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWueI2J7NggooIFq79XeIXFb49j29duSqrnMSzhqG5xOep0ZhMWeMKxFr-8Dm3bBsMmKwQICdb7RiZBr3G66niq9U9FDLRQImKx-cJph1qY07bVJ_8lcHp7_DomcmyFFDiNrdakuyzA2S53gqXyJjd7NArjGfXgMSGOVz2V8mFE7LkwZg_dvpXlvL2hU9f45N0ijnhEMBOsbs5s0pHwJkQJGOIWqo1MWuTjmclLrq3J1yZoGBnpFanX9OElOr_fjSiNpaylN-Iyzu1Cg4c5sA0eacUsp6R5RWG6unTmSh2wcS2RcdFEul1waSX-FWzT9gtH_2Bfhn9LGWEWQJZrGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛موندو: دستمزدسالانه منیر الحدادی در آلباسته 450 هزار دلاره درحالی در استقلال سال اول 950 هزار دلار و سال دوم 1.2 میلیون‌ دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/28126" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3278Td8rQwRigL2AoknwFuYMjuiXBtZTCjmIqhyuy0p1L61H6Fni7_8pkuXC8J-mHX0ytxZ_M6CICRswbd0GGRH86-5cE5ySkKWMUv6eJVCKlW83ChAVeKs-TT_DmImYuPJ5X_za5JUE9blvFkdX8Rt9nbiOsHMKIEJzgplXvuSB1_-xiJ1bdy34JSOYmLn2FqFfBNdWPLqfcq1Wv1Qf0O-HM7cxtuZhXs_wHJMYdDgm2UMZwE69xk9i7coRU1wtJ_w9F004RI4ZVr2224Jf35kCPnomlSQf9neklkm2JnsWGdHrChKKAeumMDOYwaHU9wG8If_l3m4m0he7FiZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/28125" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28124">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXvCfD6bx-RBV92JewhoNLNJrci-cyeIKCqINkJT2P_lwc8xMXdtVe3ILRPtPbnzgjLRdAKJvIlovP2bbPVGyKJpiRIuXHcjsNo8G9XpV_JG_ITplwi4poKoyhjui_F2v1oImIfCn3C8BpGwK5IBFnXNWcH9AwjcUnTeCXSs_tLYospr82hwuD1r25E6DG8zcsHJsN5cuJdNPMVfAAcVZ1UGxJVRlHaU2e_oBPysYGyRfcq_cOx9mRAZ0DOuYRcpjXVkCiSzSr0zwkSU26Wel2vosN36t-BJoHK2TrwFbapfBh-Rq9vd3gw0RwgbNxQ0q8cR8LgRUYLoecPEVcGkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
هفته دوم لیگ عربستان
🇸🇦
الفیحا
🆚
الهلال
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
💰
۲۰٪ بونوس روی بالاترین واریز روزانه
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28124" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28123">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roBq4-5BlhoKpVHG23omFFK8eBjXINWmeQ6eARw1ibalA3sJrmrEZvu6Z_ZwpIXtQzh3vMBMHzPeL7mdXA-n5DParWrDbtBNE7R1HmkbU_gqnXfPdfBdVcnruvy2PXV-qlY5wni4GLRkEYY1NzzvmFErkZfRHW3W_wuo_ZhXBWGQdlZT0rQ1Qpu3Z0ASmCerOKXJc4osuU_4v8V5Wc5Ch0-u4cWJCQysNznEK7CLlM9ijURR99fYgEu_wT369UMKz809Mk9xsKacni4fcT_eZQuXp0s_gMXGx0j-QU3AiFfUIkm6dKKw0bkwWKmWmee_v6wPjHD8gg2GXozc4hj4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/28123" target="_blank">📅 15:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28122">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEu_SIoe764S0D1ErWc6r9tdoiRh7owRVMMAV2VLKHTbTj_gU1_eJFZhsjK6_rK1oAUWpjQ_bCFOmyXOGcs6W_KYh8w0pN2RwX0zwtc7yt-ZTMLv9ftpv-zoTFFvpAYFGAdcVugdZq3j9MjGGaCcsjK3ZlAndIWOrnmffAACyRhqtzAAg1EsbjBkzmqaVev7zNwzpugqgmaOiLJ5iVeuDO7Sv705FHqwd_eg9lUQ_LXvkhHcn2mA2V2bFmQ7LG6VpRjHC1RzJMcBW6CLsICzzLx_0vlJ3QlE8CEVh-1UgE0z0p1N3OsxF9H2VIOE0HWvnJ5jdWOL2Tf7WJMdnOuPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها سه و چهار روز تا شروع دو دیدار فوق العاده حساس هفته سوم رقابت های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/28122" target="_blank">📅 15:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28121">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=MoAQu6Tb4O81BC1xwbkty-toHAaFBhBd7qcgrRbpYqm_AWaB8wuXIre0m2BzuFDhNa9tXi72xv__kRzSYH0Vr3TSrUzsFkgUBtswo49VRwF1GzfrT0GKXYxSgc4wcUx45uTSaAfyUP9-VjrDOnMrxXxKqnJdV7cZDmX10FAgQU86b1eSI_zvHU179dnT6y9A3iiclGkMUrmct6hoSK2ZMCIP71Ld89NvcEMnpjfs0grP_sqbEuzn54NWkzBQDS23IFsJfZeFKKckFx0SX82Jhk7xRh1vIX9RLgi2y5MPZOfjUNT3No78tpfQu4ThMTbMceNFgCkhVNakSo6uDEG82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=MoAQu6Tb4O81BC1xwbkty-toHAaFBhBd7qcgrRbpYqm_AWaB8wuXIre0m2BzuFDhNa9tXi72xv__kRzSYH0Vr3TSrUzsFkgUBtswo49VRwF1GzfrT0GKXYxSgc4wcUx45uTSaAfyUP9-VjrDOnMrxXxKqnJdV7cZDmX10FAgQU86b1eSI_zvHU179dnT6y9A3iiclGkMUrmct6hoSK2ZMCIP71Ld89NvcEMnpjfs0grP_sqbEuzn54NWkzBQDS23IFsJfZeFKKckFx0SX82Jhk7xRh1vIX9RLgi2y5MPZOfjUNT3No78tpfQu4ThMTbMceNFgCkhVNakSo6uDEG82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌از وقتی‌باباش فوت شده اعصاب نداره بعد درحاشیه‌ دیداربامداد امروز یکی از بازیکن فیلادلفیا هم‌تو یه‌صحنه‌رفت‌رو مخ لیونل‌مسی اونم باپس گردنی خدابوند تو سر بازیکن فیلادلفیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28121" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28120">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M97d_Ux5ZNk5AdUmk2DuWsfYifPrymKA1obKNfRdTAO5Qgk3omIIsUaeF3UVXE5a_kCO-9zRJwHOnQA9U1tDes_wtv99Y9Mjd6rxKP8nUfbDzZktKvespHelfi49cr6Nz0YXWlLsxpaY0FfE8xciNZ26w_305Ez7fUzAT9N3iEjKB1Qq7JcaHUmi4EEjxh8O83Z0DPBgrLaJHAS9SMdauhUjYfcEcXhVLiJUm0naCGgAX5hKnlq_e5dw4cuuH6N8zrO3xbL3wdPDXxSPGfID-PdnSklDMwG9bR_RRovKX5X7ytbft7nREQG72QUMfhl5uTLRC9AQfsS_U3U-DE-O1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حضور الحدادی ستاره مراکشی سابق استقلال در محل تمرین الباسته حاضر در لالیگا دو!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28120" target="_blank">📅 14:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28119">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=qVy35lN2L5Brcamr2H2G3n0C5qOeeg78rgt5YMtPhHaxz6eI--OX_oyjjckBnTuKTzhmNb2nlgUFG5wQtJd0ncTDYRwM_Yn2pDNvi7TR2tL10SN9bC-JfJUx9pJ_sw7U_9bPbBGgA5Wo0PMgWsIPPVC9x1YgulDBurciQTQ8k9KhSovEnNRBwPV9FR1Mg0NX4FT-iKW_kb6EYpFqX7SZLU4gfKUKbipkSKDa7nn4yq3FoWZyLZa0RUE2NaMgY0n-bocEIBN70QD5saHz_e7OfNTXQ2xvW3U4xT_KwuraiaZfZfxWkj4hY0EZkcUm_UwCnwsD1D3yeL6KbWSDy-qrkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=qVy35lN2L5Brcamr2H2G3n0C5qOeeg78rgt5YMtPhHaxz6eI--OX_oyjjckBnTuKTzhmNb2nlgUFG5wQtJd0ncTDYRwM_Yn2pDNvi7TR2tL10SN9bC-JfJUx9pJ_sw7U_9bPbBGgA5Wo0PMgWsIPPVC9x1YgulDBurciQTQ8k9KhSovEnNRBwPV9FR1Mg0NX4FT-iKW_kb6EYpFqX7SZLU4gfKUKbipkSKDa7nn4yq3FoWZyLZa0RUE2NaMgY0n-bocEIBN70QD5saHz_e7OfNTXQ2xvW3U4xT_KwuraiaZfZfxWkj4hY0EZkcUm_UwCnwsD1D3yeL6KbWSDy-qrkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش: بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28119" target="_blank">📅 14:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28118">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbdUOf-nhNaW7NpStb7LbOFyoIa2Iy9MFqfd7ClQ5Jy3GgCmU-L7_tIABvYAwz7kel318FcleiKIBQucjID6aJ-GrjDIJ-qIBdDDfFIHgR4k4V5odDfjqsN1DzDAtAda68vlxA12OZLeov3JhGeaLaBEq_ZFXJOwUbjfEL8lnYzb8FJr4gp1VyCkg2WcIdYB-UJMTfpuqA53nvXKLJRX8XeJQ1DIGdrOWUPa5edr8993dOXGGRtVbP8zZIQaqQz373kYF4qWrsQLGtRWj8fYK8Sa5tHR4u-gS_yWrs5iM54DzXapAqldsUo_BJIAULVDPNqGvji7m3EucE_Km_aGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای دومین هفته پیاپی؛ محمد حسین صادقی وینگرجوان‌سرخپوشان از لیست این تیم خط خورد. ابرقویی هم دیگر بازیکن خط خورده تیم تارتار بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28118" target="_blank">📅 13:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPRbhgKLs_BwvWPbq8uSiV4I-9YlBbdXW8JlVOzrRZVZyHtlMiiXXQL86PPBTot9eDklv1Ao-cCCn546LaaAn-iFZ8ehm0voRxVyrNXyyspDaRLp5e_y1KXcYDNyVR3n7dR9J8Q7H0nP9VWKtU0ojPGLPy5-57RbEC0GQG6AojI1r9g_i3idq01JVNsSweZlXvM5mOriXJAbOR5O-EyeMpBLuNCNiDtFujeNqhs3Q0GXlt5o_soAmeM3KRk2gejEFEI6lWY6gf2AzDGdDGg-DzXwulogY7ltwRYOApqiqecV4vQQfOkLU5TRhgWNJ0rgZFqYDjoXEJ-Nj358ieZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28117" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNoDOz0W6PPMYVAQ8SajoH7YtmXLmExZvNHEvCcjiB-4GqvTw4rMzm7CtMyQN7GuyvJwXyZGjuTus4ksOku9PrzxXkk_jnduHWO29eL8_8pr-wObETyaBTVqrXSRQLFWoPu_kI0ZtsbiAoDd8OrHCRdUhMjeCV4a3kFx2ww53i4GXTW0mG7FvBwpdfNYt_TblqgkTL_U2nQbbyVNcaULwenjs9JA_Ck8EB3X5pqgxwfgFxb3vERoSkSnxpVm6UGpQWj9bnSifsKJ4GvE_Ss22SRFawgYaUYHPKDbjMRvFGvEnyfbhvwzss7ZCFrD4ZjAlO7gsY6KebHr62YC0vwOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جورجینا همسرکریستیانو رونالدو این رو استوری کرده و نوشته تغذیه مورد علاقه‌ من برای صبحونه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28116" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28115">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g01WZOgJ1rIAwgAlNgkfOGvJxqXgfygZG-_k74IYrhFd8UHiVoAox5QC8ScGU9SxOpDsR10wukpffpsZGKiiaOO_xZ4ayXv072AcQ02r_70SpMTQXac2GzhPvDm7o_brR523K5NHCOi-iTLMBzEUUvu4QTgilglYn-0M5Etyyy6d5E1lN3DoaucvmzeJ7jiE6p-Yb1CpnurnoL4b8VlnvCcNjdg9nzYHvQjnk4Zwccb079FcTkdASD0EJA5ksJcmpq7DXMeb-WtcvRoMsPd1aCGeUyyiJHojtC4drNlFxYarAtv-Syhwg-U2nBN6OAx8brayxib0Xahrl29fc8v0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
رونمایی از کیت سوم خوشکل بایرن مونیخ برای فصل جدید در تمامی رقابت‌های بوندسلیگا و UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28115" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28114">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiUrdqfPDIe84qsj4U6fj_HK0q0UPqdBVeK9iWu2maBeYdHXeImC3UdT9Uv0GaSOZK9pUztWSx4Ki5h9J0W-aGUwbdHcq8SNB7Rc80DDEMZBZ2vJjZGEXnoGDJirZeFgIYglKFzvk3S_IakTQ-S2CuSp0vBTE7cc4UZgH_oAVXm7Ryd_n-WEsMV8Fl1j6G7Z3OEfImsnqVdnrnPN6AC6p8V5xfP0M6crtNIgkOqNMkNqb7yDN3dmHsFHm11UnoKKEwW2PL3Jmp2UzdnlJfcS9fBAN5q6daqQxInoQWdFzatjvxWB3ZSdj54kHT1kBM95G4FjA5GEocEIULI95Rmf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به‌دنیای‌پیش‌بینی‌فوتبال و کازینو با LINEBET خوش آمدید
.
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28114" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28113">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyBqobLlAlIdWqYbEmDQZVYdw8Mf8as8MJ0sYLGKetfLaUuz-g1MLXjsGPBAF90WtFTb9CEN4J_LP3cvlXk251IuRZWEOMz7bcbSe5igDUExOhEbySL66M7kpXkn5y2Sv5A1d21SkKIqtC_LiZn_6DNy4rq_12BpUtnwdtodQIIha09ul_PP54ToMBIWQZwbCUNC3jJ-6-s1i_-ARxho7rq3Y9W4MVkzEYbzAHwUR7gUkvmC91HPfpl-ffcySLt_NC4GxWuUJOO0FHnfiWE0H57n4SbKEZ7hTiPh7A9Thk2nyy658hgDzIpvOHPY1-sSq-NRVQR5oNNTfbaKOsBuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی:
پدر رونالدینیو وقتی‌پسرش تازه داشت بزرگ میشد و دوسالش شده بود،تو برزیل با یه باند خلافکاری‌درگیرمیشه اوناهم با یه اتوبوس از روی پدرش رد میشن طوری که جنازش به زمین بچسبه. با تموم این‌مصیبت‌ها رونالدینیو به یکی از بهترین تاریخ فوتبال تبدیل شد و لقب‌شاعرفوتبال‌رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28113" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28112">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKrkyr1dFKg70Wgwy3bx28JH0gD2r33CtFi5yKCc_ZmP0_i2arA7WtLNA648xZFidMVTHl_xM0FvDHU5tJgJkvuojuqQzm84vfdlZA0l0L8PxzgmTa_OQBkKOONElFzVzoB358O34pfwzrzNmNq0cVRRlOxxAmEt_08JS7j08rj6_DR0rpBUuGcy1yVUNYWE-Pv-ONKg7j1tHZtZmPMP7EZcR2uGJdsTIc801ou8Vlvhdc9P820Rc6cxo2CmtNm2OZbQVaHLlEpCsWjNeNswsTQhzb-GYaGa_VAb6evFJJnU8-rgvBNmxEKE6QT25iq-WDp2zZBEIxXXkPjkHfmGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیداسماعیلی بازیکن‌فصل‌گذشته فجر سپاسی شیراز باامضای‌قراردادی رسمی به ذوب آهن پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28112" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28111">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En-UQpOD9x9od4J7EzkRo-zKp9I_EPl5hWrIuqgeR2wH4C_WlF5E385w8PvP1pRCkvTNCbONStE-vBhdwBV5s-Lf18vK_JjI8TAjb7kFdp-As7j2F5P9w6UyBDdFYN4jL0N2dG5S7N3LrGm2l8nT2uo8DidZaajdmt5rQnHIcs0pEUFvsycKneLr0hOPdUO3ytc2MQrs4u79bGvfci2JcNtzYwp9Q7t7lBHsDIUjrt5kJ3VdIlCyDx38UDJtykRhl3t4LYm_u6PxHQTa3FfBlDVwM2SCIrZoMT_RMSuX1D5G3Ea4fN9GfTw4zpMFyBtftdH1m6LYrgzPb6jOjTeQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
نشریه‌موندو: مونیر الحدادی در آستانه فسخ قرارداد بااستقلال تهران و بازگشت به فوتبال اسپانیا است. مقصد مونیر احتمالا تیم آلباسته خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28111" target="_blank">📅 11:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28110">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNIu-TiHZFPbVymscTAfw39AsAXE3lxXhpA0a_8DHzl7HzFGjRUpJWmr_GCRg8Z0sABpSF_ycWXpXHo-KeNNsSl9QSfE1aT0jcyR8kXA_-PfqAI_y-4k9i224J6G8yP3LSkaScMp0asMIf5oRkLam4sH1JCm6_1wUz0PD8jpZE1V6h3Ito9IJ4qSyfRO3kPZenXYjKDRag77pKu7BQbelHDEpMSvo8o3_TxpjCkoLaIEQJNb1ne_fNb84fXtE_-dls44onGrsP_siMgepSq_OIXvvZCzhf44QSa24u9-K99UzZfxzZM4zr5Cx-7J198tsqUzAwbQd-S4swtPhIzoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28110" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28109">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🥅
کارشناسی‌داوری‌دیداراستقلال - نساجی، سپاهان - تراکتور و دیداردوتیم‌پرسپولیس - استقلال خوزستان توسط مارک کلاتنبرگ داور سابق لیگ جزیزه.
‼️
طبق گفته مارک کلاتنبرگ: گل تیم فوتبال استقلال خوزستان به خاطر اینکه مهاجم در آفساید بود و مانع رسیدن مدافع پرسپولیس به توپ میشه آفسایده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28109" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28108">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=miJZ4IOzwUXUeXeMnSVRhXWdwkIAs-AA-8Qk03ypcbsm9EPtIJOwQl6CNVoXibe6P_SY_mqHl1dvoggBf9ECT38m0K_RGUt9BLn2k_rLqcCXaeqwLhTnGAKkbUP44ckw_jbOGFGXepXE4ng_fXOOjdKmTc-Wh24ABR4_D_xlZGHKLBtdAW8SQbi-aijjgYtfAbWQoEwi_CgBB0hGFCMkATQRNQJ2L3XdVAEwrtJQakjP59LnukzfVZNjN8nzZUk8PwWcyNaeVqYfpGutlIIYxFgSEpZ5uDBpAdqYk3IyzsBHakhcmwfyOrfsxfAmJBnqbRol3Qfir3YYdUQkuSGemA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=miJZ4IOzwUXUeXeMnSVRhXWdwkIAs-AA-8Qk03ypcbsm9EPtIJOwQl6CNVoXibe6P_SY_mqHl1dvoggBf9ECT38m0K_RGUt9BLn2k_rLqcCXaeqwLhTnGAKkbUP44ckw_jbOGFGXepXE4ng_fXOOjdKmTc-Wh24ABR4_D_xlZGHKLBtdAW8SQbi-aijjgYtfAbWQoEwi_CgBB0hGFCMkATQRNQJ2L3XdVAEwrtJQakjP59LnukzfVZNjN8nzZUk8PwWcyNaeVqYfpGutlIIYxFgSEpZ5uDBpAdqYk3IyzsBHakhcmwfyOrfsxfAmJBnqbRol3Qfir3YYdUQkuSGemA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
تاکتیک تارتتا دربازی شب‌گذشته پرسپولیس روی گل‌سوم و چهارم سرخ‌ها به استقلال خوزستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28108" target="_blank">📅 10:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28107">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=EKiXlZY4TS6ROp4YeBxDsxkhOpSFaXLE_cVxml-mm6DP4vS3K452b8WuYRI_0DtZcSBJicxjjULBeQWAxAWA5HhOZhLB-n9Y9HJE7SuOC_Y9ah426nnMEQRCPvHmFto0H0ZteOlOHo3tgfW1yzTkZ7gONoBcmqEGxLU2SRWFwJgOlYLBuA6J7jjHYx5EgwLX2dDqcL4WKbYZAytQ-7KIG6rN7j-K87ewh2soQ59HQ8jkw85XlwTM_rxbujkMxIratsEz9txXYgqxkQnS5f2uZ1s78JeZibf7Hyx-5NsyTmwdULU9dZ5N1TgqJhxU63wtGDiR4yHvjpAQf_0BXBhGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=EKiXlZY4TS6ROp4YeBxDsxkhOpSFaXLE_cVxml-mm6DP4vS3K452b8WuYRI_0DtZcSBJicxjjULBeQWAxAWA5HhOZhLB-n9Y9HJE7SuOC_Y9ah426nnMEQRCPvHmFto0H0ZteOlOHo3tgfW1yzTkZ7gONoBcmqEGxLU2SRWFwJgOlYLBuA6J7jjHYx5EgwLX2dDqcL4WKbYZAytQ-7KIG6rN7j-K87ewh2soQ59HQ8jkw85XlwTM_rxbujkMxIratsEz9txXYgqxkQnS5f2uZ1s78JeZibf7Hyx-5NsyTmwdULU9dZ5N1TgqJhxU63wtGDiR4yHvjpAQf_0BXBhGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال جام‌ خوان‌ گامپر؛ قهرمانی آبی اناری‌ها مقابل الاهلی مصر بادرخشش‌ستاره‌های تازه وارد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28107" target="_blank">📅 09:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28106">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d55041935.mp4?token=ATtz7O0kKmNRzMQQ9o--2vc9Fas8H8MMc0pBOLIdc2P5DGFnVqsNGq4lJwOdCo1MxrdAiHGPJYCp4AMFEhR-6_VL9G-ShR6OL18fF4WViouCcQLpgXDdQIBjFU_CfAymbLFKYYyjJBrS32S86vXcWwY8NisAvcEdCPSRr5OnnZShDwpiNq30AohLVIjrqx5z0KklN9owMinrA6-fC10FoqD9TBsFWvHAjNSCTmtHcEDinAmRaYkyXbConKLb6yhE4t6QJQcikwj2EehhklzFmh5zcC1M5kiNhsNRVCBZ4pJJilM1fW68LghzvjGsZl52MSOUPJiDE7A46Lbgs4ApMyd_ikLlFruN6U3WIPdZ6ohTewzJb2zR5EL_kq11txBWriJFr98vEJkyOxTWmJFtOjhxrY19xlwMScH0-z6Y0jsgwg2otZZ7kWfKKY6TBdIoXye5PINMEsBLGnVsFiJJcmpr1ufzJTe7LpBFPq9ebFxwpYLt5-mK7oW1nrsGR1fNHgTDzAao2o0S0anExy85gEjNU7no6Wd13eL_tgB_glbmyYigH0qb02szfv-P_-PiK4SDGT3EH_gTdcJl8MzHuNIyzCyyDEzMnea7Obh-ZzNYjTD7ibqtkJro5Zkstec5wYyHW-IzAyMJ7g-bTCTuPhMiZsVLLbi3l2sQr2hpo0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d55041935.mp4?token=ATtz7O0kKmNRzMQQ9o--2vc9Fas8H8MMc0pBOLIdc2P5DGFnVqsNGq4lJwOdCo1MxrdAiHGPJYCp4AMFEhR-6_VL9G-ShR6OL18fF4WViouCcQLpgXDdQIBjFU_CfAymbLFKYYyjJBrS32S86vXcWwY8NisAvcEdCPSRr5OnnZShDwpiNq30AohLVIjrqx5z0KklN9owMinrA6-fC10FoqD9TBsFWvHAjNSCTmtHcEDinAmRaYkyXbConKLb6yhE4t6QJQcikwj2EehhklzFmh5zcC1M5kiNhsNRVCBZ4pJJilM1fW68LghzvjGsZl52MSOUPJiDE7A46Lbgs4ApMyd_ikLlFruN6U3WIPdZ6ohTewzJb2zR5EL_kq11txBWriJFr98vEJkyOxTWmJFtOjhxrY19xlwMScH0-z6Y0jsgwg2otZZ7kWfKKY6TBdIoXye5PINMEsBLGnVsFiJJcmpr1ufzJTe7LpBFPq9ebFxwpYLt5-mK7oW1nrsGR1fNHgTDzAao2o0S0anExy85gEjNU7no6Wd13eL_tgB_glbmyYigH0qb02szfv-P_-PiK4SDGT3EH_gTdcJl8MzHuNIyzCyyDEzMnea7Obh-ZzNYjTD7ibqtkJro5Zkstec5wYyHW-IzAyMJ7g-bTCTuPhMiZsVLLbi3l2sQr2hpo0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
#تکمیلی؛ لیونل مسی در بازی بامداد امروز اینترمیامی برای سومین بار دراین مدت کوتاه پنالتی خراب کرد. سطح‌گلر اینترمیامی روهم ببینید عالیه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28106" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=J7IM-eDHKK2o7i8udp4AFEatuXXFvdiFvjsF4ryYUTtUVSk80jN5UCiyt-vwdeTv4Mvbr_Sm5EPurEUgoxVvMlFSk2OcAUOMxhcILhvv8xmCik1s4jox7RFcVutf2-MvX-uOnDNcGg-pEGosnzgX2HRLDk44GGUPNVPstazMNbOAT3Y-QhH_bQizOjVh0srQgi1Ip8IaLKVMDUg9cWsDt3gE5XvRABb7-8J5qKNdPXrb0hkT8uBzqdhKZdj72DHgueuaDqto3QYhbQkHbqVc3bvLW63rr73Xn9VhoOp8CDySG6kH4e9kO4T8EV_tmHrhonGbyD53EDQFFMz3xB9ZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=J7IM-eDHKK2o7i8udp4AFEatuXXFvdiFvjsF4ryYUTtUVSk80jN5UCiyt-vwdeTv4Mvbr_Sm5EPurEUgoxVvMlFSk2OcAUOMxhcILhvv8xmCik1s4jox7RFcVutf2-MvX-uOnDNcGg-pEGosnzgX2HRLDk44GGUPNVPstazMNbOAT3Y-QhH_bQizOjVh0srQgi1Ip8IaLKVMDUg9cWsDt3gE5XvRABb7-8J5qKNdPXrb0hkT8uBzqdhKZdj72DHgueuaDqto3QYhbQkHbqVc3bvLW63rr73Xn9VhoOp8CDySG6kH4e9kO4T8EV_tmHrhonGbyD53EDQFFMz3xB9ZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28105" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUEIFeareoJMEs38Fq5jR0vE-n4H3iy1zm1vacTAh-JYqMcirZpwhRmmRuXXWrCOR_I8gytDx9C9k6lGl7Mik65hEG5emNG77JzhrOFR80MEAT9F5LEXH3h_ty0RHae1x_lwJ1GoSVE2rAA7MjizUb5D_1ZE8bhBK9xU42zN4I238oNbAV_giAc8KfJYa0C7IwN-jr4FmcjZdbgsD-teq17ll5wpmGbc57_Q2LQrijqlzpmE2Kfix2UzKUdA15dnJLkYgu6m8RMOEEVeR_2NmlnUW-1GBoq_w7wXCb10TqghKHUYaDtPij8RQf5kYA3TAdGkrUvk0RkLWLLZ5zudVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دیدار پرسپولیس
🆚
اس. خوزستان از نگاه ورزش سه؛ آمار متریکا آخر شب میاد اونم میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28104" target="_blank">📅 09:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAqMuED6mawyiwjTJNVtAevWj5Snmt8zbSsg0NgzhPc9YLf1pXs8E7QHNChP_mOH99ETv3mbJ0D4_CldmYXu5VgnCcFV5dGrVmU0NiwyqyQ9UhlZi3Mn8YznRJF9-8W3Wq7odndCLvdR7U5APLiaY1lm9d0ULs1a-TLcQbNcnsCvxdqFoP6zKTzt15zQT3TlmnvfcqpIdBLzo25ky3J3gFGCriBvu0jA7m-t6s6lRix7Zr97kizEnHEFLA0bJoQyYpXZVmmUu3C8_oPGO7oqs2fnM67Xqr2-n92obuigzo_DD0xWbdYJ64PbFqmrcNvuIXAwQpIB0Aos5zeuTE7OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28103" target="_blank">📅 01:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=ohuzu_mtsiCTfgrGp0UwIZVJ00S5aHKkUx23q0QGRd51Oh2B1KisrRy21ltucav3gAm0X_U4SHYL8u-hY4-rg6ZS1iE9g9ihcbM70uO6q4OdmdMQHdwRZEW4DkBUBHT4HWl9mj6M-t6ZtyGis__8o6GJU1gmnMs0WVi41ENH7KPdg9GW77O_eWcREeipcuvcrVc5flj48DZrUXfI51Fqa0_UGl9p4Xu8TKdqQEnyQLXesMyCiYrzd5cXEgRx2SokoVE_cmCDCII8hTLbj3y_V3vwJciJSgxeXGL1Mn16gS8Y6IILk__oc_NKoRIlK0Be4nw-EXW9u8T7XM5_TuBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=ohuzu_mtsiCTfgrGp0UwIZVJ00S5aHKkUx23q0QGRd51Oh2B1KisrRy21ltucav3gAm0X_U4SHYL8u-hY4-rg6ZS1iE9g9ihcbM70uO6q4OdmdMQHdwRZEW4DkBUBHT4HWl9mj6M-t6ZtyGis__8o6GJU1gmnMs0WVi41ENH7KPdg9GW77O_eWcREeipcuvcrVc5flj48DZrUXfI51Fqa0_UGl9p4Xu8TKdqQEnyQLXesMyCiYrzd5cXEgRx2SokoVE_cmCDCII8hTLbj3y_V3vwJciJSgxeXGL1Mn16gS8Y6IILk__oc_NKoRIlK0Be4nw-EXW9u8T7XM5_TuBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری از لحظه به ثمر رسیدن گل تیم استقلال خوزستان که نشون میده توپ کامل از خط دروازه عبور کرده و گل بدرستی به ثمر رسیده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28102" target="_blank">📅 01:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quM9qGlhsF__RFfoWsUthsc0D6FwmniM6ECJcB5vEwWS-EFaKyT0YU1wqmwiOz8b3QLXZEqI0rw5_d5tVX9B2sYB18prfEHvry2rXSnO6CjhrZTCA8Fmj5DMwnoLnjD1xLjRaZsIxPtIEG8SWyV9cFqKomplob1yf3b7fc0HzrN4j4d1j-UKAXVPZVi2niqfikNJp5BJ9PuxBFQfAkk6HfGLt4-f0P4MKDw92Wa7uE7ansifyuQf_jVnv2RgjqSdk_QxSvGLmj1mO6NoCLMg9EbkeF0dWdx0ErgKTA6YO2DPV1u0LHmqafvmIOGyxfKBFI4hQMYUlcX-L5fYLIdSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف اینترمیامی با تیم قعرجدولی تا بازی‌ اللهیار در دور نهایی پلی‌اف اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28101" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFmfP-pKdvXg5FUT8BadqKYfn4rGm1C4KsDLwkVSPg5xwKaU0lgSHPPRWHgwGLLpXflJ34n04OtepcRObEFa9lbFSXDGyOwSLf0nB44NO_zvV6R23FjnArPwF7YwnzVcUrTyDa5Dcj_f9DvV_W_xGlSKiBHlry8eoxo-rbikDSzPZDiK4Dm2NbsIEnNiAw7Zc9a-iFMekdXpdf00sAZQilrZEBaao051I-H_hVUPKa5N8Qf2cRj3Te99HqUq7pJLJWinakjdym5xulh0siuq-IPr1WtxDiubQEJ_QtgnaWfdU9ttX-V4AHBbXeU5x3ZOMnloY4vt3368Ic33RRKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
برتری چهارگله سرخ ها با درخشش علیپور و قهرمانی بارسا درجام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28100" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28098">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjP0uqHIfvm_k3YZ4jU1QIfxbUWY6Fm8v4NWlNVDKseTAiU99FYqQ7gN-TTcOgfBJTYswBuWAaGMz3yq2XM-03eE_2rZX7rO_2mzAUReUDi_u9JsmKFmyU52CLs69UgyVpjWHJT5tDI3fGpKGGamF0GdbnHoK75liyCMchaDdLz6NX6p5a9oNXTL3dwGnx3akC2SQPAtnG80YivUIOPTwltBg39M_FFum3PfLrDd9UcMcZAp1gqfUGmPyC6BOu8vJepR_PB-hN68uy7H0W_1V-nOM3Ud6k83hk_weEYKX2mdLyRXXF1yWvjl5hfVolUgWgUGeleyI_HnwRIjvOctKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28098" target="_blank">📅 01:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28097">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=VijI1OLXVNBJEsay7WVVCCwQH-cUBAbvxOCbaIS2OTcUZZM0istQo0Lo59liNNi-MoLNs3bG6mX7f4uK042oenv-XKWS8H9t2FD3Xgl3d-BPMtYa5BRl_TqynMmmaAYMuZuriNx9oon8jbY1kq1X-tnjML7h0K6kmRKblwkOtB2jnqxlQUidWmJDfVPFDqnqjFJY47hVoj87zeDIkRxpm2Y1hvXLG41KIIRriCW-fy6E6abK7V0mQGcnuwbLCt0vYw_XaXSw1drItS2MKqOEciUBlp-vURoH0_9N8e8qSE-l6z7pt2_6Mk4s9PSSSUnYJoc3WwGWUWAqGRfWr_2fFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=VijI1OLXVNBJEsay7WVVCCwQH-cUBAbvxOCbaIS2OTcUZZM0istQo0Lo59liNNi-MoLNs3bG6mX7f4uK042oenv-XKWS8H9t2FD3Xgl3d-BPMtYa5BRl_TqynMmmaAYMuZuriNx9oon8jbY1kq1X-tnjML7h0K6kmRKblwkOtB2jnqxlQUidWmJDfVPFDqnqjFJY47hVoj87zeDIkRxpm2Y1hvXLG41KIIRriCW-fy6E6abK7V0mQGcnuwbLCt0vYw_XaXSw1drItS2MKqOEciUBlp-vURoH0_9N8e8qSE-l6z7pt2_6Mk4s9PSSSUnYJoc3WwGWUWAqGRfWr_2fFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی همین دو هفته پیش یک میلیون دلار پاداش از فدراسیون گرفته. جدیدا هم رفته یه رستوران که غذاهاش‌روتبلیغ‌کنه‌که یه مبلغ هنگفت هم گرفته. بعدشم میگه‌خدا با من ناسازگاری داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28097" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28096">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSRZXckm-arp6z8pONvhmeCejdOHMAEkVPURBj0hXeGQN7deW0zHpwuIsPlvrJPa_0Y7B5l5T4zo6jPTE0fD2QE6b-qeXQzWmFKInz0iU4kf_mOEpaSXF1u0tVud3I0CEcOiWZ7V5n6VLAvb7idHfyNB8iPNEj5s4i2zwzJkmtS_wS3Fph_5eImPIGrS3mjJEs9jQP6TW__1_i4dZAnjkskJyBSHalJvNOWNdnm3eT0-j0cUzAySEEAqrgpg0G8PBJ7MWayRKlkpMdZCp4scj9kjVBPq_GFXWVrlEZtigxdNUHg0-xm71204CZ7TuTOzMWN2Dup87mDOaUCT_VhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28096" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28095">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggXebtuFP4R7CCYpNyRdTKFVsQrx8G_FasncFwIFkI3JKMlMNWiLa_7qJCt8MYXN6YOEUiDK_2g4A80WPOBnHyXKYshQjonoLuh1LTQN8ba2L0uRxQeKliLKGqp82-dcrFcwWTZITRmeI86EIKZ_NYgmjfMqE_qHaCseU8MJYxu7c4DZq7nhqRxAL-3QOSHKXkhg7Rt_vyKFfpO8yNq88mG4KVpyZkDt7_twRLk1gjKI5lOwoeUTeb2NzBPOkQqE3DstJKRcny56PWg9PQRi3lpGBAZHYAYs1O0u92XkNaZrfP0D7-5_1FHzwZ8hQiJXeM3YypP6-nwtvsKlM3ljRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛به‌احتمال‌فراوانAFC ورزشگاه السد رو میزبان مسابقات آسیایی استقلال انتخاب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28095" target="_blank">📅 23:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28094">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukXEjKXNlz0LGtmgDB8Xhsv2Zr9t49hBonTWM0I5JSOjlG7ngTAoDfu024Y2ww5KcCrTdrzVVoexQWswSw6ReAqsrtmOaE3yaCyjeyd3QRpBHBGPB1IwdXqFdUFyleZ37ro77sddO-Ydh5DotRIY6eu7o-q2P2oa7k4POmV-p_dGmK_o3GPFl5VBIOpnQRJP1z1a-R6cNSMqu15WtruX-cBngQ2rSrGuknxJsTH4WPAmYgB58HmEsIgfxwaOFV_UBal5N1cg5DHJ05z5wOP-p3sb4BZdzwROVRmzUso1G-YmOy4MdDNiwmNQa7m23IqJ4FlaekzXtlN33tiMZf2zYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28094" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28093">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5ACEDrBs9rM_FC7d3LCJRZDAAlQ7Xlvt7XcDibXRzpzzMiMy6781gQgXTf7er_I3Izsx2B2uxjHBPE0tWbktKEIeSG87oNGByQcuy7W3FkWueV45cplII8pCNEgKFs-jdLOZXT4g29o5oBr8KwRaodPfGEcJYIEJtlMonavrv_3goQDaBEWhghzc8LaHkIIN3zm2JKHbcC8FBlMeCr8JB4we16znRyDKNMOg5bmFvJkikrdWS9NqAShtGuoNGvEMrqroE6V_F8IyDbsqxsr7r739EpqRdiI2gXIw8O-YsalVO73BpPenygJqVCYzWc8MYHlwsmaShE-t8E04qQyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28093" target="_blank">📅 23:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28092">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs0npl76X5TBBXNNYvc3d-f6LzQS5MAz5H_T1YCI_aYSD6GIAqhCblNrCHY3Vc0Nlu6TBpZdMyG_VQFKFy9fuxxVHuwpAHYMuFz_ylklxEtpZyIavWpGnGG1otip2TJ7g1Hrukjf3sFJe8HUEeJ8jm4-QOFow6-29HdjQhMF3A5Jpgy8tkx8GO3Y6bFkLGazbZGvrCA0MrwmqMr2xUxBQZfMzcN-e4MHWptmD3me6lZhZTX5htB27GSZen87znJX74YOzZSrlsVLzrUHb4IJJ14G4zBXpQcQimH6jfg6CEIaRj3zuP2avG3DXGA5nUPSdaE8cI71WhyEo3MxDVpsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28092" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28091">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T46CkT_6Herj_UnNcTZ3OWg3R6TLbZodlDOUQvHSCGQZKrV3hc6QaKetZ5auHnh3OH56ryb89EEaENhFznjmqJVOemrfsTMXwt8YpvetDdZdx0qiu4PR4Hxa_5G8mARZJhNGAsWQJwXYi_1T4LUjiY-flNWwW4zgKFfCUcOxaycKzMj0LAD7zyejMXdZxgJ3HeCUlnCVOykZaz96bG2Ry9CZ2cOl6YZvbknrJ8jlqD-7BOQTGnb6ACaAInuwYd2l5stbmflz_jOHFMoyFx0-FcHIma45t_bSk5TKYNOfwbmm4b5itkF7RSYemACeOJz3ElCBbL-fyYoq03Ts9WWKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌وجدول‌رده‌بندی‌ لیگ‌برتر در پایان هفته دوم؛ هفته سوم تیم‌ها محک جدی میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28091" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cru4fUl2renR2HMrbLTKveL-JVaAH6TzO925N1zoSCDhTBp3Ljirj_1SRbF0iT9l9sPNktjCyqmbEnIxPVjeTaqLDyhU__S1FmYZHfOWh4WGa7K3RE5RzCKmu_GG4ggeYLt9JwwyTMTRL7d-nDyu8GUHFl4c10v30jjjqhyBUqsfBF4K-5URGUfNDnF6P_cKbwmYDMeBF6ssfh4kT7E5of-6QApFiFjS11zadvsTx8tzyhErDwbJKvTd_n-P_e4mASXs_ZZlWjmuN0gYCna0-YI98faq0xZjILTMXzt0qc87pkfrqkvkiNSuVEUwIg5KS6E9r_k0fchGhVkgyYcDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZF3a6OyBXxmT7UKkVOG9ZX0wW72rOPmmi-6luYeDVlTUAW11Qr71nRYH0CJrkQztW4OrBbfveFfNQssN1en5xeg2CbjVTLuRTaoNvn_TYULtsG7jChuXDLecm1LA-v54r2cck7FmsQ51QIQJ2WRxoC5darwqQDN-Bm1JSXnv1tIAMKg7jz-CUKN1_O_96TB5CicgWQrQweIOxY2BKRpOMsiiWtbolIYFnpxWZr7VR29pX47NpLezwa84r9NMfMZTodQKxht8UyxA2Diwp1f1_VXMkFCCfgzR7Z2wtwZeKyGo1BtqdSv_WrJx_nuKdlLaFfdYj-XToz4sRvEKR43gkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28089" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3_Rs_zTr03MkvzAKBjur66eJ-HvtfEQlvrMAKrd57JMM7IZ_hLS1KsBp6VaQUkzRnxM6_BjheMdbs1xDrL0sF5PMQwhDPPO7jLPT81g1HvwZ4KcBf6vlaIZ7vEmJVtdyffIUPZ0B4EooMKRzjr5fcyvzRJ4cRH4laeVagDPHRT30MlBN8wO5ot0yxMA8yTBvrUag1pDj-QDDygGmi3TxTSxGcD3tt9Hwk82qC4OmjpUvDZQWHSLURFmCBrrPj9Xs12srPtMesycwQYq2HCNAwXJGumWgobGuUhoWD2V484ieRku8AIpjEpKuP-cAz1ewaeMVtVg1wGRlKEbvOTNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28088" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo1OKSEuXm0BWlEV3XlyK43jVjRYo8Zo_gRc5Ij579j1oVQJT7Oa5I67X45Q9ZObhhxRyUc7nahYbROLEaETKwmkoy_GH7sSTu4ptFZzpBeIBhP4KERG3-IQ9ckbV61pNnDeRsQZKidaXYT19iFxSQ_QlajLUsSHdevC_oCYuk-PeC3e_IZklDl-_B9rgITnmex_y3i8YbWr6RkKN8YCc_pconY_OSkZ61nnEeKZE4tWjtb2C4xN_sZGNretJF-GzrJmtQ89QXkcwaVMLz48ZZpjPG-n886dhzXaWnw18I4lvTmibjKWHeTEa4Ws8zgcjH8LdcR_DsU5TkFr-3vxF-Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo1OKSEuXm0BWlEV3XlyK43jVjRYo8Zo_gRc5Ij579j1oVQJT7Oa5I67X45Q9ZObhhxRyUc7nahYbROLEaETKwmkoy_GH7sSTu4ptFZzpBeIBhP4KERG3-IQ9ckbV61pNnDeRsQZKidaXYT19iFxSQ_QlajLUsSHdevC_oCYuk-PeC3e_IZklDl-_B9rgITnmex_y3i8YbWr6RkKN8YCc_pconY_OSkZ61nnEeKZE4tWjtb2C4xN_sZGNretJF-GzrJmtQ89QXkcwaVMLz48ZZpjPG-n886dhzXaWnw18I4lvTmibjKWHeTEa4Ws8zgcjH8LdcR_DsU5TkFr-3vxF-Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🟢
گل‌ های دیدار دیدنی دیدار ملوان
🆚
ذوب آهن؛ ملوانِ زارع بازی یک‌هیچ‌باخته‌رو دو بر یک برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28085" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZqAYVw1WOYhiFPoT49JGS_fUCIotOl_jcyf0zMiultYQ3kYS6AwBWp-8OfPgMyY0I1EfIyPTPD1mTRfm7gPZiKGwH-kW4mb6uRwwx0FuEUxmdeIg2xNT5kD-sehNEimuWBGUial5FO2E-G3DQjUOY7mIDqw8-FY3h2Fz-2zfCEv-TqgIR_5RNzkPZh9CEhk4wLVeckmnoonMGRcMlhUQnPpv9pdxbgO2cDyC_vBlViVStOq6nKT1dR-Gaqf0Si33epnpDi68rdw_4nhiXWOHRHu8YhacUqTqRhjyIjbkHR-EDn9RftY9rtlbnqdQ2NX45EW7Bc0x-srq_cbu00BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امید نورافکن ستاره سپاهان بدلیل مصدومیت از ناحیه همسترینگ به احتمال فراوان دیدار هفته سوم مقابل استقلال در تهران رو از دست خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28084" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC5eskZ-B7bTx9iUbxkUOgkGC5i9pY1HdVyCe5JtWrr52WXrTsMLfZqtpyvSPzY4bCX1oE4UC9IzWQ4Be6VCVOTq41g9lva-2RwRKS8Mj112tkzAxx9i71xTPQE5qa-OEU8VP1kbVbVKGFgk3fOhO6LcKS9pnT2WKRN-ubmVlMyyxKfYeYkNfE2KaJL4eXo_ADEsPXYtxIGQwSXEUfuVxIe5WKSrxVkaqYR_PojzreuTwXHEyZwuEwvMBU_KAtfF81g78Jk-FO77BAuJU7WxNfmHxUuOR9JKFNCfiDOcF3vfB0WGi78bST3crwahoNAXsLn0VOjddOqjPvlT2HoZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
🇮🇷
#تکمیلی؛درخصوص محمد قربانی تا این لحظه باشگاه‌الوحده‌راضی‌نشده رقم رضایت نامه این بازیکن رو از 1.2میلیون‌یورو کمتر کنه و همین باعث شد تا سرخ‌پوشان پیگیر جذب دهقان شوند. اگه طی ساعات آینده اتفاق خاصی رخ بده پوشش میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28083" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28082" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRYcZc8XFYX5VX50K4988AbyFT9Kfir-_clzBZrvKE7ozi9AO2cuaUOXQHfrNs-m0Wd-rVLwb38xYpWMnIrTtgBMldOTIpwONE4f8MA32HmyrX_O_7Xf5SpAnddLOoZukPPpCd4BkjbIzlD92KjkfvmyxudvEwOPQy3H73tsek0fTBfVYMiwoh9GGwIeLBwThKAMEJr7Z9lnD80ILRfy6f4LHd2BSgKLEZbt25uxKjBZDUKM9cYncTCs1MPGdHwenF-BkdwvKtNsfOylR-5wwNzUIgAgE_ZadcB3_TPgHgooJccAwWBv5n0suU8l0EW5M70Zi4NqsVyELee0CP_3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28081" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfIff1HNdW2EcMMEhN8tj4ZOgyifq_xYI6lENExOomxFvE_oyMfrHjO-sVWMdLcFF8K51adu_Gc7lRHfdJMa5n5AwIINq8oaRyOH5A-_5RHBXRxgoMwT0IACwHKR8prqlSs525M67AH3buhyMQ81WBY3Cdjp5yn3NHX8amx7i_MXZlzDJ52xbC36Dv5rfaFcXff5LaBBQO6A7czhLRxI2tZYl82EA_OeTe58z_DgXTFJ_0BhlF5aYYj8qaAXArrGBuuX39pyQ4RkYioH2lk2Tebv_ppvh2tEAjXYNQJMyBrs4xHrPv1Iz4BH6jf6QUb89-hNYilvGFBf73BFs72uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28080" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhL6Y9KcnmcTyWe_5ruEIZiuefyyFR_lfcafEavYTJINRjLh4B4Qi8ja1vSU7Yje60o0TzwNsGiyjMvp6_CC8DkJ6U2zLzt4gtAAqV1Ljf6COmCBFl5IwrKICO6oD1fshpZNpJQ5XzUNzicWmmapqlklm3SBSylqQ79wT_qFSS47dK9SgrDdiXZq-gYjYQANVAdCxFlSpVnzWmau_-5OQNLJ8HTg15-0kC-HhBkQHvjbKzmQNqIRIXEVnwphOh0XrjYFS2Z3uJRzapSWduMlOVvI1juNxNeN-c1he-CnNBApK0gl_Nx_CXRRTIGoJwFv80vq_UtPJi9c5jltDaYe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28079" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28078" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIuUnosxA8-ZYiRE-b-lADhWQqbT-nDJ2HV-YCCeLrQTm1bQtYRo2DGmm2SNVc0eIuGSniZFTMI6pzYelEJi4gnl4URAL0ZHBSbJ1zAK6Q_0RyDa1g3ZMFLSrb6FzBYqyexT0UfH2ZrRpeQhNcoRFLmLeY_jS12vCr7VUi0h_cgdtX7mO4mbIh_MBeEt902ZVngxeNgIxPI96QodHAtCBMHWIMKmUMVqiarITLe9mFB_H0M8N10fU1cpBNIBOUeqqUasXsYKuDEaCJvUQM3ykT2fYoqPUZtJ5bSlwHFcMUSSx-61oOiMJnl1EGauI9LXqc92pVIe8fBhQe8A_7Wksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28077" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف '48 روی پاس هوشمندانه علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28076" target="_blank">📅 21:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28075" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Q2J7sTWGU3n6ooajpnFnzC5Z2Glz1jIaYurrRTrbyYW9F9zaX4F8OHT8l_XKdfkGcWgNYtUseNR0CR94bARmnMBUpVLG08yRP64gAXD-GoS2Ivc_6Aol8c2hDIqdXwZGyxHb9sjDLe8BzQej1oKmp5A5xP0fifjWliWYn_QYkJm-Jya6MgDHQozIL8f9dumCqb52KiphLVB9jJEIF4OdgFIz94A2CFjL8SfNnj6l4i39838xqxXwPqK6fUNTnQCKOTffYUAheFdy1Y6ZyRwADX3SKna2_WlWu2NMH4h5ktGsI0KemPtLHBFbAioCJe4HySF8Zk1R7VxiQJIF7_4nBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Q2J7sTWGU3n6ooajpnFnzC5Z2Glz1jIaYurrRTrbyYW9F9zaX4F8OHT8l_XKdfkGcWgNYtUseNR0CR94bARmnMBUpVLG08yRP64gAXD-GoS2Ivc_6Aol8c2hDIqdXwZGyxHb9sjDLe8BzQej1oKmp5A5xP0fifjWliWYn_QYkJm-Jya6MgDHQozIL8f9dumCqb52KiphLVB9jJEIF4OdgFIz94A2CFjL8SfNnj6l4i39838xqxXwPqK6fUNTnQCKOTffYUAheFdy1Y6ZyRwADX3SKna2_WlWu2NMH4h5ktGsI0KemPtLHBFbAioCJe4HySF8Zk1R7VxiQJIF7_4nBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز منتفی‌شدن حضور مرتضی پور علی گنجی در باشگاه الطلبه عراق؛ رسانه‌های عراقی خبر از آغاز مذاکرات این باشگاه با سیاوش یزدانی مدافع میانی سابق استقلال و سپاهان میدهند. یزدانی از طرفی هم‌پیشنهاد تمدید قرارداد از گل‌گهر دریافت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28074" target="_blank">📅 20:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpx0l_JZMSKfIUj0MrrZsA8hRqd2Vqbnz9XHm1yGM_7m0PNqstQnmeO5zAClF3IQTZ-rv1DT4Jq_5Ln2boFC6nsy2nNUhzpgaDde1sQvFFFuzpuKUkCQ1KIy1WPpybH7Ob_nN2uL_lDXGF8FMgi1Qm7MK_zF-mJ0ezCeYcHLqMyR8YFL0D4tjnONqvyaCcPhw9cowx3KX6omHB6Mes4tanl_MJiw41lSaBm0bmwFmk2ccz9tzjKKfNF3w3PF6-0ieCin8Y2kjxBuGG_ZvYQHVtHm5FMAo7TXm8oIIq9Pj9RQwqGa99LdYjQfDr-j64jRgH_0iVI8CjIWbNyCwwhNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28073" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=ArqDjKgM_bpbstWO-mFygA2o242v4eVfCuPiUSRujG8BUvwXTleBZ-E5L0BMGYjny52DMfMWxzfsIb5Ig6RtUB-vt_fWtgWgL5mnK56FsUw40uWtGb8zZVA8uFKu2MO2M35gs7iIOzUckFaVF-qi7BUfyXhftLcB155NXrGenRPGcAVvJobxqdUXk4w-kPTshyqZKP_5dXdaPO_p5EXyEJ4VCmEjWYMN9MItNjdhfhtIvk5q2_T__n70qJqatbe-ROG25v3tvzfD5PUXTWx7Z-oAaNfwgosepgWwE7wAyMZXmBu1zWDClo1XvRLbGcvuhL9NaywDuocMH7ZxPVXZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=ArqDjKgM_bpbstWO-mFygA2o242v4eVfCuPiUSRujG8BUvwXTleBZ-E5L0BMGYjny52DMfMWxzfsIb5Ig6RtUB-vt_fWtgWgL5mnK56FsUw40uWtGb8zZVA8uFKu2MO2M35gs7iIOzUckFaVF-qi7BUfyXhftLcB155NXrGenRPGcAVvJobxqdUXk4w-kPTshyqZKP_5dXdaPO_p5EXyEJ4VCmEjWYMN9MItNjdhfhtIvk5q2_T__n70qJqatbe-ROG25v3tvzfD5PUXTWx7Z-oAaNfwgosepgWwE7wAyMZXmBu1zWDClo1XvRLbGcvuhL9NaywDuocMH7ZxPVXZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
رامین‌رضاییان ستاره‌فولاد بعداز پیوستن به این‌تیم با استایل بالنسیاگا کنار این تیم حاضر شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28072" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG0Py9Vyfp2NMxtf6KvOeZGVK372pP36CelgbNoP6Mozu-y2EtPu_kFt2Rbl1820TF7SYnpESmZFCZgnP2XBwy-gXYAce8IiAzkkysuYIfIsiPzNf1FcFuSfF6FMdTxMqAN9iJzhyNk7xbumqmw26Nc1nRSobmLUBQbZKTTrcPwcDpx2Nwo6TrzA5ISY2i47NcAwuLHT1XesFw5lxbzkCedyTHpkqCCpNj__4D5HL6sBEp_tppa0w3MvJRJsCCbLq7Vod0Ug2NXWaAsWyiF9kzbXQOveTa0nV6sHeXU89eXcr3txa-r8O09Euopc39R89NEOnD-h9oMcapxuQ51ALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28071" target="_blank">📅 20:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBxTMZqWH5_d4fxq6L4MgLlPlAAq7VtpTPtxmgZsk_XeK1QhSPMXHCgKq-P095Kipp7Of6BnDY_RPRi29TlJRxOXW3h3DEjws70w1Ue-Aqi-N4uFUiS9-0G-zYsXphP0iTdtKASPnYeOtu6XyNruI5jlTk98PfsfiTEYL7O839YAIpBkdJdvC_Nr76DAN_GUaEuHES5CcmdYBNI5HcvNEBx4quVre-E4ybuna0QLBWXSjS1v0E7ExzgusbJ6m2XKeIDJKmz0HOP9O-OP03jXXtAsoqot14bCO5S_JCf5Ip3dacmDk77IljPcTLQNwvfnZfX3LOMhz94sUmQYTUcfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28070" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=br7GIWURiBAN7mJY-7dL9LfXsJLMww7K1XLSVX02lIWYe8E80Hydl7tLbZYrw8A08M0e2rmGrRRTV6vdfJrV34wgvFmZNLp5HqXv7E8Amq418lgvkQvxbhXL5cMcMlsc-gQRVAzsWtv9WCjD5z1i33s2noNylAqJdfL5B2-4j3hUu_MPGntIIJ9d42afHs8a7y2D_AXWvynNmpJU3il6kZQwBwxNcd0QF7OG4JBlnVor29YlzVH0uHpfgdN-i5xRWL2yhcE_RPKdvbdtzY5fcTqH4x_mEuErFF0J8eU9kq4WAjony0b6gp7htE7HBr7cZpKSUDiYuKU9EUGn8o6YyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=br7GIWURiBAN7mJY-7dL9LfXsJLMww7K1XLSVX02lIWYe8E80Hydl7tLbZYrw8A08M0e2rmGrRRTV6vdfJrV34wgvFmZNLp5HqXv7E8Amq418lgvkQvxbhXL5cMcMlsc-gQRVAzsWtv9WCjD5z1i33s2noNylAqJdfL5B2-4j3hUu_MPGntIIJ9d42afHs8a7y2D_AXWvynNmpJU3il6kZQwBwxNcd0QF7OG4JBlnVor29YlzVH0uHpfgdN-i5xRWL2yhcE_RPKdvbdtzY5fcTqH4x_mEuErFF0J8eU9kq4WAjony0b6gp7htE7HBr7cZpKSUDiYuKU9EUGn8o6YyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28069" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=g5T4cchRN6dVlWANYYy87Mg1ffFFFd41bt8kVLnQyyTXwBpGm3WNNM-BWa9ZQul0YQh3yt9zaZxfMJjvzQ2iTft_iNBI58htpXhF1QdRZuBbIiOuonYAxMzQyGbq23uFs9fxZwxl4_J4E2gnO45JD6w1hNaoW2jciYVVpSm7pztWksouooIKgkhIweSU3rJrWwzKXrbfd1E65Ti-42XbExRqYUWZlxFCFJQqtltvmGZf0EjZja7ODiXulGoN9fxrnDiiFA0iPvPChBezmKVTbvNVHHDwIuvg2E7Twqa4Y65_Nps6y1MXxZ7Zx_-69krlfHf-xOfwuVt4x9ffYLJBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=g5T4cchRN6dVlWANYYy87Mg1ffFFFd41bt8kVLnQyyTXwBpGm3WNNM-BWa9ZQul0YQh3yt9zaZxfMJjvzQ2iTft_iNBI58htpXhF1QdRZuBbIiOuonYAxMzQyGbq23uFs9fxZwxl4_J4E2gnO45JD6w1hNaoW2jciYVVpSm7pztWksouooIKgkhIweSU3rJrWwzKXrbfd1E65Ti-42XbExRqYUWZlxFCFJQqtltvmGZf0EjZja7ODiXulGoN9fxrnDiiFA0iPvPChBezmKVTbvNVHHDwIuvg2E7Twqa4Y65_Nps6y1MXxZ7Zx_-69krlfHf-xOfwuVt4x9ffYLJBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب‌پرسپولیس‌برای دیدار امشب با استقلال خوزستان در هفته دوم لیگ برتر؛ تارتار کاری کرده که هرترکیبی از شب قبل منتشر میشه اشتباهه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28068" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=C9lhvBVwTEhghRRZuO2vyap6cG5y6VOHSkL0K7vRmh3dnYI-zyE3p2nAjKSVSuiXZYu92-_qy6LzVcqFDabadnhaIQXoECmyOYj85CawWcoHYZLrFDGSx3uI4we-cub5D1OmYQAtqZO9cG9ryPw_8e8y4LUjpAD_DZgxLys4AR93xsm2gFTMr9BRelTZJif53LtHGgPsHsou4BAb4hKO6C06yoJS8f3DznL7Xw4UTIRdbfoAkLQaSGp8-mDXjFTk5H2oZeLo0uakGhfOObrwmgzZGG3cnff8L9BhKMHll032V_KBKMjlmWkRZyg3NuuVGqe13Za2OFPGE8xbIyG5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=C9lhvBVwTEhghRRZuO2vyap6cG5y6VOHSkL0K7vRmh3dnYI-zyE3p2nAjKSVSuiXZYu92-_qy6LzVcqFDabadnhaIQXoECmyOYj85CawWcoHYZLrFDGSx3uI4we-cub5D1OmYQAtqZO9cG9ryPw_8e8y4LUjpAD_DZgxLys4AR93xsm2gFTMr9BRelTZJif53LtHGgPsHsou4BAb4hKO6C06yoJS8f3DznL7Xw4UTIRdbfoAkLQaSGp8-mDXjFTk5H2oZeLo0uakGhfOObrwmgzZGG3cnff8L9BhKMHll032V_KBKMjlmWkRZyg3NuuVGqe13Za2OFPGE8xbIyG5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28067" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkrhPGmGKEUN9KjqGPh9oxtQVhRRoI3gUejmEVZWAEnv-rNiJMc9WpQ20wEKeb3xiIEQBnoLOVeOFS1p9Ao0JUeb5hvnw9Lv69uPmupPGO7oQ6CwBFGJQYySk0qIuFmZyGuxdTmDy8CYjbL6mBiQhIsU8kRDZvdtC3MLGqeGglbziix7RApNNmjGgOU1ih1EQw9RT8QnbXdFlxphIHW5ziEnIaBrxGulUDYOX7AKD3TugTLesGVIpAcaW6ErMIPOfnbMSdSVu9mwLNmqnqu1DoOqt5J52ye-X6Oqu5Ze3WDlL9rxvTOUikIk6pTQQsfHzPBdKOwW6AME718glAFh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28066" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLVD7ko4fr4XEajbvGpw_IaQ_5X-VLu8aU3Nb2F43DnHh38oYYJeCtsEnvXJR6cx8BNrE1wsP3ylxk7gRuTFmyeCUeYN6uoOKh_QN0xGB7dauKC4_5d_nU1X4e2PTLuCGeu-TCvOcTqK4XB4IDf7w4cHIbVNDc46lUV5OXJ-yOyNfYkZSxkKg26gslSKf7lb3TxR9WG5Z_OBneqPBway4vSuqSv71iVhbQdx2rMM2Fzl3TqTex0ElXAd3-x8sM39CkW0ijsV3MgEbBh7YCHiOQjtrjf1T43RKKK3uYZz-Pk-QFibuK4fcnM_YC2aTnpvByGXDmg4m0AMAdtSJVciSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGecqHRbkMExJ_KspwHZl-ay-E8Y4e7i2dE3UJrMpnZBcnOL_K2IRa1d3kKnJFvp_fRQOiXWRrtwLRpqc7HGSjQ5Hur_ritCOYIh3hsMFCjvTdwa9Nc6YZlJaBP_bTOQeggiBAqb4N4Ke33QoUIzTa92za7h1fizUdWueYRrAcBtKj4wOFbQ5HUe0PB1bp-Jq5nmdBqFhmAZ7G6xS7TbazmT0kqpb8133T84oyvh5lXwcyPqspCMp2t6eE-kShPk59QJaSRf7x61TvxzHGm-K4BhGkNTx7mJ99QdKQ1Lyl4supqsGhDecJNU2Iv_sU6hpW0bb0PfFee5d7CWb3SnNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش:
بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟ آره، ولی شور و شوقمون تموم شد. فوتبال رو چطور بازی می‌کنین؟ فقط چون بازی می‌کنین، یا یه چیزی از درونتونه؟ تو زندگی‌تون، هر کاری که می‌خواین بکنین، با شور و شوق انجامش بدین. من بازیکن خوب نمی‌خوام، بازیکن با شور و شوق می‌خوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28064" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42d22RfTLz1fNs-zb3MdGDmPhwuwz6H3IukDE3XGzqkPKRwHSEKHaHrFEGY4nCCSMmrpIDQ4TWDTfLbbZWT0QseSjZQExoXPHvo0aLtONTWC4pnx3lbvanRc6K-TBjbqDVEbY0ztHXBORXDc3l7BvHqkwczckVkZCj2WaFUGeLk8C1zh8YtA0eNxm0QsmuAV-ryY-IWwoWzPCYJu_qmbXvZqjdHTXa30pyP9HZll5ttHD0hS8jwr6nhPQXc1aJyRmv_dss_u2Io9J-bWAheJtTOC6BjovcSMmC6OYFIvdDHDT8p2y8Qz2EqI62lfgbdixVbserpiSxHYOO1dSWrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزارتومن‌تخفیف‌خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی میتونی از بیشتر از ۴هزار فروشگاه و برند محبوب‌درشبکه‌های‌اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28063" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZRXDWsS-jT-GQpvudYj1jU4x16_E92bAHlIszhirHuUt_qdZL4GX0AHnUGk5kipApoG7A-C83_pLbTmWyZkUvBGPz64fOBL9f0tkgPTHypbngEmPKYt2b2Pb9hDMlyaDIUz1B_N-Y0ZlD0aJT2qxKP9wGx4sgK5gyioQeYm2TrsUyVcrY4t8RLiFNxVlTJUauPta_hadqeiLhxd5eDAoBWkbHM8-wneiv10RzJkfL_Q8yFJ3HQzUOFw7xYTPJpqgG7GGHHlCfaiTMi28I80QEoLawjEizuyzj6vssNI64W4ZX4pZ_IeZgDyMAkgzCRYEH9VzcYcGmmnL1jDvpqx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28062" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoTg6Cbl8s-DilPpiI3ofmfNnzegD38XHNZFHEH7I_Eura_exbF5qmHXwmAfFYUlFRn_CdKRcuZqbuYbtfLywSH0w9V8R9ztsgomItIda57GH4-T8jw-4I9N9ikxqNf7mfUm9AKxlE3LxrfH4PwSjDGpiIZzcZCixLyxcl6TH44YbeZVTF3ORGk6tDCMnlgrdA-OYPMokPMbAOCbd1515pajCaDuYnOUn27esBqgY5eLrXvRgisP1LR0mH2RU0VpnLeVjQUWUhmkj_tuYL8XI3ZZSod-fKmJXuJs9rCBScb5CulTUgEeV8ThCLcFLMnXNantO53mYxda-ZOp5Lq1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب مقابل اس. خوزستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28061" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWo_usSqkGyos6L1QTiP0GK2Aogh8BaAR3X5NdA2I6zxsYP5O2NWhIxYimoQjHc6hiAdHwepm1N7Ps8g38XDqt4uMfS_KysV_LSudott2FQSzAASmSXUXvt-r6nAnKccOg07BFa3m8B_Yh_k0MaipIkQ_SjjIC24n7stag0wW5CJNW6-GmFieKTMjfdLRg0Zy1N8ZBC4Ik_zQF22wO04ewsYqWL7z-75A116HFbabI_OmqNT4T7Q4QS60A1EOpHrP6w9GeAtehTVDkilzK-pfWXMUSaF1nTxyGC5cALKq-e_wNtqpcZulttL3G6fIY9AuArfZoqxJktD37galNko_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28060" target="_blank">📅 18:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPXF3M5a9AOXxQj28Ez7yMOw1kt7V0IO4gii5yUpRoZ1xvP5BkDkqPHM3qVKM57cWJCzlL2DZJAel0u2UV_bd1lu65uCdYR6slZP1Y0wnuRCbTlKUe6lgcG_osBv9L0_z5R8-AX3_VcxIgPN2_aH7GCYULA5ceuXedggh87Gd-VQnck4ueJIxNVNOrvuUj7AC1mW2lrjgz9Nzc7JkWv1PNw1aujesRt2_BJDLzjgV3N-E438Z1RaqBMvA6_yicnzU1xIlTilmPBskXbceigINf4MMp1H52O73qTznkyso_8nAacF0o7G_OBAuzqHBAV9_2CKDqg3ElJoVKJ79ZAFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 5 دیداراخیردوتیم پرسپولیس
🆚
استقلال خوزستان به مناسبت بازی حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28059" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFba3ku-96nAADCGeX9uD67I9gJp85778_CjMEn8OuXXNKePeU1lfoZoQEdPVUO8DvIbOGBCEcSUDcvDwqOrk2OZ2S_t32yRC8T8jzWkbB478Uyt31-Rhbkmg653yL5KoTSbMjz_jHdhSi_tyyY78JFiKVdIQPdTes45foxm-INT1gY0rQAzw4bWD5BcBbkpzqv-xYnTMnIwVNIzrfNN9sllIMGNLwVN1xgPxDVMBbN5KRerFeOa-kEX8l0YqUVL8epRiupdgjtJUrZdced2hdcjxkTMI_cM2QU5dHt-n-afvYOHAdUhGIpIhyzpcI08Zo6AuirOdim6M32uUZrXrMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFba3ku-96nAADCGeX9uD67I9gJp85778_CjMEn8OuXXNKePeU1lfoZoQEdPVUO8DvIbOGBCEcSUDcvDwqOrk2OZ2S_t32yRC8T8jzWkbB478Uyt31-Rhbkmg653yL5KoTSbMjz_jHdhSi_tyyY78JFiKVdIQPdTes45foxm-INT1gY0rQAzw4bWD5BcBbkpzqv-xYnTMnIwVNIzrfNN9sllIMGNLwVN1xgPxDVMBbN5KRerFeOa-kEX8l0YqUVL8epRiupdgjtJUrZdced2hdcjxkTMI_cM2QU5dHt-n-afvYOHAdUhGIpIhyzpcI08Zo6AuirOdim6M32uUZrXrMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سم‌جدیدی‌که ازطریق هوش‌مصنوعی ساخته‌اند با حضور ارلینگ هالند، کیلیان امباپه، مسی، رونالدو و حضور افتخاری رامین رضاییان ستاره فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28058" target="_blank">📅 18:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCxU_ON23MVea2sH9O5GgxwzQmwyMv2O5q6kbOve26MFI9375u10OVO6yKeSprPeigIYgoYY5YyB8-nTVtcRm8rhisnyQ6G6YjJEqNGhnecat8iJUSLj4MdpWpMHxkuOD_Wnn3OjeBBQUO7S1gBURkTVmF8dWcCMwzVaMGlMKIR2sgze4p0XdF1fV82oA3xmvRCQXD5O1Qz5gOk5D1bf0d9ubEbBRVk9jJxNujQGiCsk3LnOmAiGdVpdoZV6ONS55GcV4YGYoZLjEMGv7ygU7igIfmik_20sQzqLh4DybWejp0SPByVOGZbD2RDnMqQ3eH7tpEyiKD40xRj7d4PZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اُما مودریچ دختر خانوم لوکا مودریچ که ستاره خط میانی تیم‌بانوان آث‌میلان بود با عقد قراردادی بلند مدت به اکادمی بانوان رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28057" target="_blank">📅 17:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMo1CakffnQLZIAtyfrrYfqV-daURNowQdXACNclYq4oKcQP6oNfWVwwXrAc0WR1fW4hpYljSTx1M2ZqN0VnaGP8WvLkqK3gT5Jc5jhYTNCzlmWIpnNsFoaYIhSrDUBHCBBg5epEx2U0Rlge1w--2S-kCDr9h1VsB4l0k4jBgSvdcGUU6rJXkK_u9Hr9DLV4O0gER2kgZVagw6mUdY0gy5NpALtbl5cKQ7xLI92vMl8BkgMfnLixa5BN9AFpdpodb6MORI99q7T1XIJy-r01MlSBkzKjt0YTMjZx7-ukVBZpNXP1IB_vHGZuCu40mVd-ezMOUd743QptjLn4qBicFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28056" target="_blank">📅 17:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu1XBiLBb4Y6LF7vAH7O6UiEBMhb4hObfRlt3RjZMlJ4Yi89s0puNqX38s72CcQNVBH3ThG53TzVHWm9AmlhoWUQsCkpUnLcWkXN1uOah6GWv6J_fMwA7So66JDjMd_Tbs7t4c4t2Jyl2TSF5znn2fqD_uXZrHitiurvxxUItmhhxJdeOt19qq9za4-e27KbqGqfzY6qkH0Ip8wQd9R56ZVdPvjbXd_ZjEfDviea3uOz3Z_6eF3FYcGiiIRyhDgthLzN1A3DiNpSjk4EFftYzo7xlAKCt_9l3Xu7HDkpy0tGdmSb8jysfCuf86FLSUHWuTq6DHvSgKr_3NK_7ZDcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28055" target="_blank">📅 17:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28054">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC5_wT3vbdtwmJiW1Vx430DIgO3cXoVISFdoUISBTRXP3wJvRo6lJwbvCP562uUFAeCgEGCt-JSrIEB8zr8DqAZPuqHew9gsBWPL7eQPcMr7z6s23x2NFed61uN0EdDnCgBvYdkmJ-onmh6H07JtQcCBMVqgP_2gyWRM3cuVWWHxOj3DHkuPLoYLWGV6IZWVvqawWzFz0DUz--iDLxn7waE9ttK7Ysu0PHWvI_vzH4a0Sccgu8AQxKqji83dLyGONbfDGtoBq6_oF6sr973XBcARxhxgnPGgJ_INkFYL-HsYjt7FvXK5QMp9RWy9qkfrJBSuYALvlKRqcVS364seZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
عمق اسکواد باشگاه بارسلونا در فصل جدید رقابت ها بعد از نهایی شدن ژائو کانسلو و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28054" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=Iwnx5Jy0hzG0H38xPkVmnbEx5ibhCL7vUAih9amp5PJ1EhgXShdZYRny79S9iEIEoGQqX_AGeIRDFmFxWNYXsMUt1hKwtiMPX7b4eTbGFeRZsnM19v2OzuAHd-5-pSzWhHNUvRCeJU1uhSpuS1_cMqR_9pplXONHTFG6OKwTHf1lxYET8bKnayqV4tpJjUT04z79wMyWyZqrXiIrYWi1pQXXKtYhc26LbrUXXFnnaeC8R4Lsj3NTvJixXKHFG2Nsfk3G48iY_fdiS9wCh4tppXKx2MrOAe9TFUVBCUJZeBeoJEjq1IHe4M49FFay6Fn3X_5UFoIWZiQ1DjgJGiRMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=Iwnx5Jy0hzG0H38xPkVmnbEx5ibhCL7vUAih9amp5PJ1EhgXShdZYRny79S9iEIEoGQqX_AGeIRDFmFxWNYXsMUt1hKwtiMPX7b4eTbGFeRZsnM19v2OzuAHd-5-pSzWhHNUvRCeJU1uhSpuS1_cMqR_9pplXONHTFG6OKwTHf1lxYET8bKnayqV4tpJjUT04z79wMyWyZqrXiIrYWi1pQXXKtYhc26LbrUXXFnnaeC8R4Lsj3NTvJixXKHFG2Nsfk3G48iY_fdiS9wCh4tppXKx2MrOAe9TFUVBCUJZeBeoJEjq1IHe4M49FFay6Fn3X_5UFoIWZiQ1DjgJGiRMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28053" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDXbDEflmn-RwD9YF8E0lNsbxrZ3JP8pdpI2Nz_Uxm6IUpzv0WuREc3gxnzSm9ERvZ-0y-oYmNb3F2gDGqfPRceyMwlkM0O78jOA_fPNPjUNMzCZl5sQH6htllNqa2xAXRoepVAz3MT5RmCz4cz_T5jRJSak6I6CZrNG80_W-qWewvt7B6uNb8Ny239d6r72GqzGJ2_uUlcaRJE1TmfKUwZstn-Hg3O3Vkr3sTyw9KGtIcIIgauxh3gq_JAtXGIEAK583K5pQjjySfOExB-YUOv-0no0T1pKdVhIcp2iMcWNTCado4X4RFiSMfVrW_-JaqCy3nnCwrhhEk2tN5yAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28051" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBVVicpMsxhs89b6SbShWH_w1za8wLRLfgeR7EX3S4NmWcX7DMNyndFRVWkh248BU3zRo_scnbew4QKaTVz7BidFoGiyQirVXaEC1vyDndAQy9ECjKxibsH-Kyrdq-TZA7Sk7i-yEC2BwEQFCMm6bXrRs_mUf8LjabxAQYA_8n6y64vKZvRqHMOd3ci4vnvH4zl-TeewMFxMl5qMyNAFXpzhTG3XBy5AvbobkNRZGpMvM3yx16uPfX_cUl9HDHxL8TipA6__eoDrsUSStYpvUmqRysEy9qotT9kPH59i6tuFI7pr4GEqnW9DQEyt48cH_Zrt50H0o91to7RgnNk5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی مهاجم34ساله تیم‌ملی رسما در لیست خروج‌المپیاکوس‌قرارگرفت و ظرف 72 ساعت آینده قراردادش رو با این تیم فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28050" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nABxczdiv_luiha77Rcim3xCeN-9lX_uFGs3hGn3ZjoM8kpFtL6yI0DDOSmhk_LowUsl_I7G4jYWC_uIvSE3RRn_-CWelfzV-fH67otd93qXmnnbrF92RhmAFQNsePsWjAUmjagtbtmkIhxuhyrnM-rR3Z-WyYIRekPhs-XaKzuVDieoCnft75qB5fgkJt4IP_nS_fayDWzYYqYFI3LbqpKh2VtjIX5DgO-ZOf7h6iOqhEs7kue4L0LDO36mNEI6gC61jfm1zd87qc-UJ7-Ynnqemq3XskX41OhwWkYt3WweoCI8CihndSYX-85fdHs0VLm0PIPWc0U9Aqclvccydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28049" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9ivGkDSOsny4lUuCpoe7q8d27MgB54veXEGy1DphK3zuc-E020x4BXO1tF-LIqYajxuPTDLmerDZpPmTuOHlsXPh0t_28o2QZi9F3KRm1WbrCDEevn05Eqe3EOSY5Oi4f7SI4xmCIqTSe1ORO7sn1AIvl-69imC5X9d6ZdjF1IiqJJG1nfRSN1cPkDqmYtZF5lUK2rh39tudalDIHky9Kgzyc0c-zUvk1eed0Fm7mIelX27Xt6TMkQ643UMRsi4_rW-UNPxlse9_vdNZ_WYLfx0oxx-SW-IT4VNk7lFZCA_JTpGqzdZlH7FJYNEQrIjifT130cfWAhHMKaLJs0zNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داروین نونیس مهاجم فصل گذشته تیم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28048" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwqRqOr2g0wT6xGIQRX0PD8I7dTp-5enuHR5xSOVPjlxXkA2oWnn48GQQgISkmIjA6FvwQsKpM061CPLpbSnP9po0taI8B9DImliqWf9A3aP4PFfdWf-drZ-owFTjJsO2PylQr8Tij5z0nJQhon-rNu3MlBUDBMwd_dJVdRGuQSO8YcOX30F9Icm9nrzs9C4opPHqBfHCkKMNKLtVK33_4W6cuOX6pNRFlwN9R4A140ivv4GIFGkgQxdF0cxIzVqD_AULVMssqOnnAKRdt6BnkE7jqVt-rawv7LWBaXFs4BlhHRNKVSSHCLsAAJxTDI3ceJJd1L3PVFwF0rnS2g4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28047" target="_blank">📅 15:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXkB9kHcMuVF2Jp0d5ff4PAKpcy-I8Z4pylqZpz9slBUI49TBGF1QwR0_otif4y07wUhiN8NKJTYTMj6mTXteLGOxsDOOLpniehwE2fkAPZug0FioWSxUAdtJOIlU2NQO34WV4k13R2WAmjte9tbu943nzab78VrWuPH7Tviu12D7UB3od2Viz1UW7tHSNXnouOIKC_iRULAnbgyaBk_IYJbesk4ifhB3xrQRKv-iX96aaM5WUblTqBtfWDkEiMBQIt8cHUdh49O6t3JCFBIIBwiDX7zzJkaoJUDTuQ_Neygxbx1z5gJbSvgrNjfsN6JP2AjIUL9WY3hSeXmE80YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
جواهرات جورجینا رودریگز جون توی مراسم عروسیش دوتا تیکه لباس ساده‌ی ساتن پوشیده و جواهراتشم از برند chopard بوده که گردنبندش هم ۷۵ میلیون دلار قیمت داشته و انگشتر پروانه‌ایش ۹.۷ قیراطه. ارزش کل جواهراتش تا ۱۰۰ میلیون دلار میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28046" target="_blank">📅 15:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGg_Dpl7XoXt0sFuCLoJ-hYYLSu9RyuAHQxtZpnFCnQ1azp6rgb62uBb5hg9-0P3OQcoMSWQhdmT03D-2e2xpE_P4XVVKDIIR84_G1pj6ckGV9mtaBkFhNNtvQ60qWq0_RbVDHl4zhzGjhxRw_yT3XELSJsUMLVQC0HJv6DjtsSn82EyTHll7Y8mH9WfGirhYt9jHmuFQksXmajyoF_1xZM3O1yM_aVq-DHiW0M1dOg1TVsub43BLxqDSn0OuiLjwiAMYUWf5YI7MSyZr-NQ0M94rPyvZ30fAlUVA0VA3ew90PCMor0KpcZzQg_tmrPT3PRW4_X7lByNaupXCnd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیو باشگاه بارسلونا از رودری ستاره اسپانیایی جدید آبی‌اناری‌ها؛ قرارداد چهار ساله امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28045" target="_blank">📅 14:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKbRPfUtqKYhtzLfo-zMW2u330Yv41Jx254sqO4SEd1nrCLOMJ1PBGN9NhlTkxm9MssBwUdBdolS3CPSgiDNDjiSLdqn4p06kF4ZRMglMkA5wMU82OnE1U6e6flsxhZuyy8Fqgibwg29ehbxVaXkW0vYVVJIDrc_A4kjb2AUOYLXJMNGE9yP6KA2PISNq6_GCmCtD9LizLDJo0y37TwbFjX07nGIr0kTAeH903B4vYkgsYpRlr_XLVXX1kBTB4mxsa-NqqprxOeZDNG07-SlQGK6AcRdV_SalkF_ZTC-iFkZAq_21Tn3tDuZYkJp55gTeMtVhdIEURkMh2O4KwSrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
باشگاه استقلال باارسال نامه‌ای به فدراسیون فوتبال خواسته که بازی رفت شهرآورد که آبی‌پوشان میزبانند درورزشگاه نقش جهان اصفهان برگزار شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28044" target="_blank">📅 13:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=RcMR35XJ96vSFgQ_HZrIXUWz01IGdnB4PFyZqbewUIcWxrTcT61V3x31b97FTqww4C_O9cR2ef80VmmhcvYzO5sfTdLlNceNyhu8J-yHggW73fc3ek8zfX63Xd89WZtNnAOxmjHgBa7r1sD_Em3NEbghdCEJtqMdX0hK9UL6cAi29sperCDZPLFt79JfJ56NibiBcAAdZowc1Vzet3pW-IX9KnAPM4q47vEYvLY591QkSEzHA702j4LiAnlcRvOjZSLzj0tM-WOhLSgzbXk-SIoW90iWdOrhbBnQe6jcDcTIMyMLtX_yB4NDYbxux8W7a5MPWtjq0eshqgg8u0G_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=RcMR35XJ96vSFgQ_HZrIXUWz01IGdnB4PFyZqbewUIcWxrTcT61V3x31b97FTqww4C_O9cR2ef80VmmhcvYzO5sfTdLlNceNyhu8J-yHggW73fc3ek8zfX63Xd89WZtNnAOxmjHgBa7r1sD_Em3NEbghdCEJtqMdX0hK9UL6cAi29sperCDZPLFt79JfJ56NibiBcAAdZowc1Vzet3pW-IX9KnAPM4q47vEYvLY591QkSEzHA702j4LiAnlcRvOjZSLzj0tM-WOhLSgzbXk-SIoW90iWdOrhbBnQe6jcDcTIMyMLtX_yB4NDYbxux8W7a5MPWtjq0eshqgg8u0G_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28043" target="_blank">📅 13:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjtRkoYckfgsyuB_0iOn5dDNqrKZl9mMwL3P3D6th-K8711D9IFL3J1Hg3J6UMquSonkpFx0SrtcWmbfM3BiQF-Zz2y9JgxNzl_VzlzBjDE3mRcIpxv0BGjyGqodVec-il4nYBoFBOEEDAFd7XmdpPxvns1jLk5k-0eftXdR0ayLhs8wS4PV8j60JJT1Nh0JSmJapUAuBuUWiviujfSSV9mUove199vd6vxV8TCUGSeOKAQmrdMGmnjUMjnAGeht3AR4m7mODqvY_lV2LNL7oeyD6hQyDZo_z103hOLH_nT33URGic3ioAPPX22mzjdxIgXdpoZAMyqNrO9Zmz6TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌سوم و چهار رقابت‌های لیگ برتر؛ هفته سوم دو بازی فوق العاده حساس داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28042" target="_blank">📅 13:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXylW44-ut0L3ydw724zrrZ28ZfoqoyGgiTOA2k8rbWwyWvo3yPY9z18ztU-zFLFAwGLPWOAvdDJVmV9rk5i--_stNpoCgUUbAWTf-2W7llIly6kitvVvNPkedpIgU7J-S3JsTX41fmpc2H2lfMBSKJM20YzvWAdT0PN1M1lbAIbIIyDh5y97UF_TBRvZUJO-1Y3WJdIDQYxG2yM7xoUWG4LIJhJRS-Vf7N3BSyJgJhaRGl604ltmnvF29zklGK3E4Iso21Fp745SZqOodGyCtOjkwNMGch0zpVExsuKrqeOZU_nhdd05yI2hsWnWflDHvlQ8GyKEkLXkWspd_ZrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌رومانو
؛کارلوس‌بالپاوینگر22ساله برایتون باعقدقراردادی پنج ساله به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28041" target="_blank">📅 13:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikTbXQNC-w8zs_OoliytosNq44IziUqGUyOyBDZTdTAc2m4Sx5gGRIKAlSgjiVUrZfh3rA5r2P6VHORKLD1-Evvg99BfcAV-a0XJH0pxoe3Ha3u5vVwT3x8uvXzAFJ7azGH328yoHnEQl7TD-5_3oeTYhtnGbbzb18Eq_skXHUHFxLEgKYtFW_-3lgnlOWWPSIn0lenLBfScs4TjLIN68pD1Ot1-6AOQqVAyaFF3tndOeXz-AnygbwZidoEpzNuXPMz2WBQTHOHQ6Z22brkuz5x3hGDGovYWAqBKcl1Cfv6xvPzyMjcJv3uaTAxeFoQcIciePiZD2QXCtKO7XRX8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
پل پوگبا که پارسال بعداز 26 ماه محرومیت با موناکو به میادین بازگشت امروز تو تمرین این تیم بشدت مصدوم‌شده و رباط داخلی داده و طبق شرط تعیین شده موناکو میتونه قراردادش رو فسخ کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28040" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28039">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyDW1U_LADNZW8QkcU3BfCc6fXN2hqrF9TioARuvzCT540PBXwsQ7ry18dn6She8OR-Taphozof5JKWtQ8bAvNdgBVzASBuT4SSvHWYjOgJw-gS1xJ_Hwo38bA1dsSNxzfweCZKMISxKHuLggQj_RgwVB1nCNAvEP-Liv7vsnny3P_Pr0iXjm31Cv0rmZr9QNfa1yXpRzpxVsR22U3Iky6XYKvXnd_3XDDzl_YCefX2rqYSu3WmMNnTO1HDF6LAiKlFQNjiPAAsvbX_U8fPJu3gWImZ9RsIPM7bh0rv2GSZ-VjGru_ZTTCPUh9jnDRzxMGZNtsT-_VM23xZELGnh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
رضا عنایت‌زاده هافبک‌میانی جوان پرسپولیس با عقد قرار دادی قرضی تا پایان فصل به مس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28039" target="_blank">📅 12:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28038">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXzBNbjw9pL7lFsNl6AyoU7UxWBbRBp8-1rTaVSbMtm9G0L3NPvePNnPnfEk_T2zrNYEJ0F_owfwMDclhfR7hZQZFazubZwGHbdpHoXtHSlGFbGoLux9iD_ylYNP2okbf_QbI7NZjlQPvKTvRyIb4zVFRSD6bV7sE73hE67Er2SVDEhvgC40GIL9IqJrZJ3tounsCccPasJh1w7N5s_LOCjGQv85RDI2tv9wQTQ43TCuRYRtiiYaVvlZO54dqYXJGsKwvnYAcj1hCD2yb37LAP43TVf9wz-sWxf44SC2lJPUQVJVdmLPoOFsmu7yP49RBae0e6BD76itbLPWMY_Iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
فدریکو پاستورلو مدیربرنامه مهدی طارمی: جدایی‌مهدی‌طارمی‌از باشگاه المپیاکوس قطعی شده. درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد. مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28038" target="_blank">📅 12:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28037">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axqBU0tyXrKYSEY3uxeUhHP-4QaEf-gAG96QiQQ2SfXGwceylX2UG_NbE3pgSeIG_XeLOx3SyBJ8wBiCkD_JlZt7xUU9PqvLsdncfS0CPMtzc30fZF6RJMXjBdeLpsSScLn_k6bQ9yaPD_vkDne47O7NqUID4EROfsox95w7JDXVQ7M3R3MqYJgqUuKxtFMGh07PFfMbzAElQX0ZDrao9XT2HYHzxXBxIszRLjbebWgSaHFDlvScq_UHJvR688Fe8JTdexr2RQ2Y4rVcpim_08HecaiC-cLLgbb4lzisRvf3jWGUB2WhRhKPIn3MV1PphZF6yVfbBZJp_rk4esE9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
یکی‌ازمسئولان سازمان لیگ: روز شنبه هفته آینده درخصوص‌وضعیت کسری‌طاهری و یاسر آسانی جلسه برگزار خواهیم کرد و رای نهایی خود را درباره قرارداد این دو بازیکن رسما اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28037" target="_blank">📅 11:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28036">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAXRFMHCvwygktQtC58haJOk5Q_teYs09THSm2jhhfRCzVzBxnn1JvhI00fo8LMnb6h8BZQFisK3yU69UO2FGHRTZJMxCgcJnnBRozSrHybNgJdikPz2CuOOTfiVzPSzkxWknP9ryKdj-zXiR-jme8o5aoCEWKhF0RIjderR2UGUv0oU_7MYZCke1jDdmi4MVQWupQBA2AsTU-Vc5lw7l7BaB79fqA6E4XcpG5itNbLZvh6_Mrq3GfalVdcHP3Fhy91JtGLxik51SBsgC1Rr-cjs7fyK3JCZzLNq6Ah1WqbI-E2UYVog1sC_tqJAlmY_dY6rddBBzEl8a7Ie6G6n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
دو باشگاه استقلال و سپاهان امروز تمامی مدارک‌لازم دال برقانونی‌بودن‌قرارداد آسانی و کسری طاهری رو در اختیار فدراسیون فوتبال قرار دادند و بزودی فدراسیون در این باره بیانیه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28036" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28035">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4dSaputAjn6VrOLvAeSLK0X7DummY7USQF65wzqMp4AwnTRoUSoSkFR9lbKaiBkc4had31yM5IqVdes8HFJBfl1hSEVNt-_4O8y4y-UhnMMFR-1aZhQ8Bdn7oY6yP1SHs2sw7rW3jQH9J-g9Bj8617WNcgC4cLZxt4QP9HYkdIjOP625iroZ2QpTDNJmHI4Cb6P4xvwdnRnNruxkBrJErr4H2SmfXIt6C2vdEvB2rM28nsd0FQEhtpodu4WIrnOwiKzz6QEl-V70JiVngGFSwuinXcVwq55Hd0cosIZbz8FvL6WhYqLwEAXo9G1QN0TVc57p5JdtWo0bQ3K0PhU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28035" target="_blank">📅 11:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28034">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZy8t1mi3JNKLPnjCmLdSxVEBpnH6E9obRLusWUxZ4JcFqD2omXLesRNClyNENogtAcBA8BsnHf7cqQPEc0eX6eiW0PsMRZS29qx05pLZh7pCYhVYGvYsCa7HMbZ4fOfkCmfeX_7sOPEDNrFsQbUPFCtwOZYIA4owHFXJWaOi2A72HfiHYzUBfLBZJ-oUWNhEX3_gorJg3ppxDrDNDkw9ndZNbuNfxiChW3ItJxGgDV_fjYc4xh6k8-5sKc-3juRCdVa4IaGGJCeM-wROUjcTywrtKSv1RGHxjk_93pDj2bjrJwAf2x7XoAy67h3t0WZZW_sDdRxgKwLfWeBaD5UWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کسری طاهری: از پیوستن به سپاهان بسیار خوشحال هستم؛ باعث‌افتخارمه که کنار بزرگانی هم چون سید حسینی حسین بازی کنم! واکنش حسینی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28034" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
