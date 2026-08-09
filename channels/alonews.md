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
<img src="https://cdn4.telesco.pe/file/KeFNhqeTxV4U7KRpuCe5uyTrpfgEjEM5hakugEWK2nadMCT2YLemJ3hf9eN2wc9T0G-xCiihO9YvH1cJGhtf_6M8u7rJv3X-ROTMBGJAwVsbGA4wvyv2-hrdi8Vhn9V4uaTbxYze6QwxhWxjobqqmn5hdNl4ZusHCB_QNJNVCjKdUAKj8O0PlnbW17Jiopof-N7Q8ihu0CTbyQZrrBRHPx_mc-x1HYt-0tSCpnWUVlHJnscEynbsYa02qzbf9WxBbSMV3yZFyZzIUrGdG3_P_1av0OxS5-94NjCdr6Rd4dXZ0yfveZC9BAxDqtPfhaiiAyZQqmIAKYRFYQ3FQXwkfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 973K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 18:29:16</div>
<hr>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEfKfbq4p1XuSg_5NrNYVdMl6lGLJ8T8ZrWuTCGfZ0JvS-0DhuQZmCnFTljBSKHVuGT6LeWuxTEN2d_atk0eMLSsu24MYMeiBlD4IlBE13IViyt7RiRmxMbmoopT3rwQXAAs3G9eGre-GHWG9oUZiPccT7Lt6WrPPr11j6X5OsS9rkJBkogxElMgLjHD2o0nGiVaSsPDhsUh9tCSFLkBluhQ_B1xUGd-dqSopiDpIi5tgKjVSS5oHSvFA0Gs5Qm9hz-7IPhqRkojhBiZq-QbPrDRaDixMahUT7dzy4o1l3xtHsJWWTtZCN9ZIIgK_9tPn6pAUlFWDPGCZhsen5riiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره : مارکو روبیو، وزیر خارجه آمریکا، ترامپ را «رئیس‌جمهور صلح» توصیف کرد و از نقش او در پایان دادن به مناقشه میان ارمنستان و جمهوری آذربایجان تمجید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/140776" target="_blank">📅 18:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10edf0d4dc.mp4?token=t_cE1Bf8SLyS_fYGSEvIX72kgLicFK13EjLFsPFzC817BTEwq0iXG-PkZwliDXz5EXrxLqqi6GRrSOzC5WVtNDCUMuqObdy4XIV-B94OiK6SKqUb1SihTbSn_y-AtpQv7FUNlWfNJ3NMbZtg3dOBUkyAoeDNPc0Jas22-8I_Q4gu7zv2qZD6EPFFNVm0wq4tG13X0Qz6qhqPBUOVQtl6yBvAWqMCUMaZMZ7jPCLUaaBqMLTHyU5UNKg778PgMRMLdJCBiatWm3yumioukSOWpYOtRIAOSgNpNgBkvyaaredY6dBsyA69E_Kq7E2mUMz65btNzMLfKAyPENOaL2HAVjfBKhiZGAS1v0vx-xfMLMgrZrVJdl-5FHPGlxUiz_teo8iVtLzXgMUI0V67tHPr9Z_6lzeaYhKk5ZD34ItCLmAEGmQYaljd7AkOV51wRLRsKHGsGCXnQ_EmZi9T3OpGFWFUBFXxcBy1q9Wn4BSH9oYVnm4472STzKGbphWzDHlXOITAdQe09qvcN0TcOJ7jynp_zH6dszToaUiumOQSxwAQOnEbKbX450RiUgVTrM88_7ZKucW1-hj7zJmkEjJKfplOCm9IZJQ87lUq4IgPVrOSjW-EliMbm9G5Q_s5EbucrRbQ8F-V7CgoXVQ21J-KHKmwyxIN6AX0CsogE_y7K8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10edf0d4dc.mp4?token=t_cE1Bf8SLyS_fYGSEvIX72kgLicFK13EjLFsPFzC817BTEwq0iXG-PkZwliDXz5EXrxLqqi6GRrSOzC5WVtNDCUMuqObdy4XIV-B94OiK6SKqUb1SihTbSn_y-AtpQv7FUNlWfNJ3NMbZtg3dOBUkyAoeDNPc0Jas22-8I_Q4gu7zv2qZD6EPFFNVm0wq4tG13X0Qz6qhqPBUOVQtl6yBvAWqMCUMaZMZ7jPCLUaaBqMLTHyU5UNKg778PgMRMLdJCBiatWm3yumioukSOWpYOtRIAOSgNpNgBkvyaaredY6dBsyA69E_Kq7E2mUMz65btNzMLfKAyPENOaL2HAVjfBKhiZGAS1v0vx-xfMLMgrZrVJdl-5FHPGlxUiz_teo8iVtLzXgMUI0V67tHPr9Z_6lzeaYhKk5ZD34ItCLmAEGmQYaljd7AkOV51wRLRsKHGsGCXnQ_EmZi9T3OpGFWFUBFXxcBy1q9Wn4BSH9oYVnm4472STzKGbphWzDHlXOITAdQe09qvcN0TcOJ7jynp_zH6dszToaUiumOQSxwAQOnEbKbX450RiUgVTrM88_7ZKucW1-hj7zJmkEjJKfplOCm9IZJQ87lUq4IgPVrOSjW-EliMbm9G5Q_s5EbucrRbQ8F-V7CgoXVQ21J-KHKmwyxIN6AX0CsogE_y7K8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدل ال‌سیّد در پاسخ به عکس ترامپ در شبکه اجتماعی «تروث» از او و همسرش با این کپشن «دو آمریکا بسیار متفاوت»: بله، او حق دارد. آمریکایی که در آن حاکمان شما دو نفر هستند که از یکدیگر خوششان نمی‌آید اما برای کسب میلیاردها دلار از شما با هم متحد شده‌اند.
🔴
یا دو نفری که واقعاً یکدیگر را دوست دارند، با هم پنکیک خورده‌اند و می‌خواهند برای ساختن آمریکایی که بتوانند در آن خانواده‌ای تشکیل دهند و بدانند که آن خانواده چیزهای خوب را خواهد داشت، با هم متحد شوند.
🔴
من و سارا از یکدیگر خوشمان می‌آید. نمی‌دانم در مورد بانوی اول و رئیس‌جمهور چه باشد، اما از آنچه شنیده‌ام، راهی پرچالش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/140775" target="_blank">📅 18:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دیوان عالی آمریکا با مشکل کاهش اعتماد عمومی مواجه شده و حملات دونالد ترامپ به این نهاد، این وضعیت را تشدید کرده است.
🔴
این گزارش به افزایش نگرانی‌ها درباره جایگاه و اعتبار دیوان عالی در فضای سیاسی آمریکا اشاره می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/140774" target="_blank">📅 18:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnuR6XOnUTArQ0D0zMHqHeOaZN7MvWRdXib_hNoj4sRusO7Q0NGrnI7dk5BWMSYTa6asUheb5Bl04MBB5CEOP10PP3nObSMFzHyX-sp68Jc7YEtGKhakJ24aWjmH4Xo6MzyjkoX4U_D3i0-zAn1JC4tRNV50OgoF4LfB4946GwIw1IDB00IG5OUIhJCUv07JKO2Kmz2sEC85Tq1v1itslE_DEW1yd4vIIw00QoFUjdByVOs-HpvSooTCp6szX8Svz6wK_C2kV5iOQrPJonCOcCYw3ngaYuFx_4SlUAFZE2y9M-KOojHfTGRLWukLJyRZjD3Z8WPEPRKaGcfqrGW_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر خلاف اخبار ضد و نقیض، سعید جلیلی از شورای عالی امنیت ملی کنار گذاشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/140773" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7yPDacwKA0r9GDJnhJqvCy0Hqsijyh_UbPKy6UOfg3yZjzRh7SJYZoOFE_oPjrYjKX06rBf6v-Q80QdoA_rgmlUQHDGxdEam85vIPtomS6NF1mMGNNXmBLMtqyxk8DrBNzJonR3Mn4nKMepYX1eo2XuimowIIM64VUVgV3o6IfCSqMAW3xIPSVz2AKpa5QUtlzbu5XCH8-6EHavxQ39AGS2_OsXZa4vqPDcWzkYYiT89sUh3WIV5wpKaRdnQ6x2wbBqliI3xKAdzXq3VOIn_R_2N_aiPntz-6rl7CgHmngnljnPKOhIfEzjpYr38vx73w2jlxHQE2A3U74PElvN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید
ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/140772" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حماس: به اجرای مرحله دوم توافق آتش‌بس متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/140771" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کمیسیون امنیت ملی با اکثریت آرا لایحه‌ای را در مورد تأمین امنیت تنگه هرمز تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/140770" target="_blank">📅 17:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/140769" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c731bac8ad.mp4?token=JmDganwdirhk5z27a_7sMbqGorXIO0pbJ9njAZTl4QgyBulmP6IApoxNB6PoXoO-rA8EzQc_FnnvEu9z9XvmWNnseq_Px5lRKM2Vo-kiLiOr0TzAUmvTlH5OhYrPzgrhB0ix6KEpT1RGG7lkApNjc9MuGNBXHFTWrYeGuLIuWP7ObNQzG_vCxwwzmzpxwp6e8DhIJM-ocz7DPBifPIY-oXMLWQiuY426ph2mn_Gfv5_IVEAy5Vz8F5Quq_-mGxxsnd2JFmAEW3Xp17AJployeHVd_K2SuZkTX5mjx5-8ozyrPYd3SUkCD8aiZFj94amNnpRz_IEjkYNpZCIQ2XAwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c731bac8ad.mp4?token=JmDganwdirhk5z27a_7sMbqGorXIO0pbJ9njAZTl4QgyBulmP6IApoxNB6PoXoO-rA8EzQc_FnnvEu9z9XvmWNnseq_Px5lRKM2Vo-kiLiOr0TzAUmvTlH5OhYrPzgrhB0ix6KEpT1RGG7lkApNjc9MuGNBXHFTWrYeGuLIuWP7ObNQzG_vCxwwzmzpxwp6e8DhIJM-ocz7DPBifPIY-oXMLWQiuY426ph2mn_Gfv5_IVEAy5Vz8F5Quq_-mGxxsnd2JFmAEW3Xp17AJployeHVd_K2SuZkTX5mjx5-8ozyrPYd3SUkCD8aiZFj94amNnpRz_IEjkYNpZCIQ2XAwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
طوفان سهمگین دلفین به چین رسید
‏
🔴
تلویزیون مرکزی چین از وقوع طوفان سهمگین «دلفین» در استان «چجیانگ» خبر داد.
‏
🔴
حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/140768" target="_blank">📅 17:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c067f64333.mp4?token=JwKM4KImDTx3lNZU6hFYmja-N2N9G3uNs4GCMEgvFoqNaptxQuhd2ED1DuheXNMGwrEoSi9EVXTe8bBSkKzoE39VPpdpRbfh9ZExoT41T2d0Twp5iMy2j7rZ6nLt4KngCq4PSyJR2KPTVTQNg8mWa_7rkCMJYYRXoa8S37SUyK8CMN_LXkzRqYaxDUy3PUKlxVm4iXLCsrUKF3g_rhqA6gKumTMq9HVBQknCsDx_HoO5cnnKI__Nb88aA5dElSIEHBDSTvrbqN2bmgsHRgd6CElU9aXsnPdD5a7CxJjranI1T_nsCcy_t5s038dd3tYpZN3FOrYJ_fylZ7YWOXJ-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c067f64333.mp4?token=JwKM4KImDTx3lNZU6hFYmja-N2N9G3uNs4GCMEgvFoqNaptxQuhd2ED1DuheXNMGwrEoSi9EVXTe8bBSkKzoE39VPpdpRbfh9ZExoT41T2d0Twp5iMy2j7rZ6nLt4KngCq4PSyJR2KPTVTQNg8mWa_7rkCMJYYRXoa8S37SUyK8CMN_LXkzRqYaxDUy3PUKlxVm4iXLCsrUKF3g_rhqA6gKumTMq9HVBQknCsDx_HoO5cnnKI__Nb88aA5dElSIEHBDSTvrbqN2bmgsHRgd6CElU9aXsnPdD5a7CxJjranI1T_nsCcy_t5s038dd3tYpZN3FOrYJ_fylZ7YWOXJ-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی زاده: در جهان پس از ۲۰۰۸ اساسا تحریم اصلا معنایی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/140767" target="_blank">📅 17:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880188eb1c.mp4?token=jvgKO3is08D8Io0JbC7bKTeR310W1obw-5MT1lVYqQr9NWixmIJYvxxplOuTbCi6jR0FcymzBDhJN7E84wmLvLt8LwyHYBsbrNYa-Qb4pxN2kCMFi3ceJI7EWWRoLKlnlkINT3yF_MUOoh7fzQN-9XVEI141CbeO11XKrDEHmIMGIwZ0C8ejismFEMsyyc8CkHvgrb4wlGd-EHc0RR3Swj4jHLgg9cEN0L0_vVY-Vxfyi1j6rfgn5d-VYAqteq3p3PzUnJXiuZDWOdJHCVGTL2swD3WpmBwpCyor7FsMSy-rJ6RVHZPRutUihE8-seNWnplqoNiGSy09TJNMYIHHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880188eb1c.mp4?token=jvgKO3is08D8Io0JbC7bKTeR310W1obw-5MT1lVYqQr9NWixmIJYvxxplOuTbCi6jR0FcymzBDhJN7E84wmLvLt8LwyHYBsbrNYa-Qb4pxN2kCMFi3ceJI7EWWRoLKlnlkINT3yF_MUOoh7fzQN-9XVEI141CbeO11XKrDEHmIMGIwZ0C8ejismFEMsyyc8CkHvgrb4wlGd-EHc0RR3Swj4jHLgg9cEN0L0_vVY-Vxfyi1j6rfgn5d-VYAqteq3p3PzUnJXiuZDWOdJHCVGTL2swD3WpmBwpCyor7FsMSy-rJ6RVHZPRutUihE8-seNWnplqoNiGSy09TJNMYIHHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند پهپاد آمریکایی از نوع MQ-9 که از پایگاه هوایی چابلی در جیبوتی به پرواز درآمده بود، سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/140766" target="_blank">📅 17:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷؛ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140765" target="_blank">📅 17:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7777df6.mp4?token=gglIJ1A2UdYAttWyFW6F0OzJZF8I0ur9yl57o7Qu82KBJLMOpEHuQ1KwSdz_zK62C6Otd52R8AAyC4OIHWMpkO9j5Bq5Q5g8XuBHSPrL3aBggyBjlcRHDgPy7rzlh1NVQC2ZPQrWXA84xbtcm8oG0CmhmbENALmzyrkZuQVtCC4-8u2Aug4q56vTqbk8A_qC85-uImbQw7BBrJjbuWLHqriqsspslSk3Xgow4jjW_9BKvz3so2nWKB2Flieof1JNUhB5XPOPDl4o757XPuLXvvzSYo36wYppCcxHKn2jzLKPKQ-Zl8JmCPbc28-T4KrdDd9cZYXPHNZMVz4XVNW08w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7777df6.mp4?token=gglIJ1A2UdYAttWyFW6F0OzJZF8I0ur9yl57o7Qu82KBJLMOpEHuQ1KwSdz_zK62C6Otd52R8AAyC4OIHWMpkO9j5Bq5Q5g8XuBHSPrL3aBggyBjlcRHDgPy7rzlh1NVQC2ZPQrWXA84xbtcm8oG0CmhmbENALmzyrkZuQVtCC4-8u2Aug4q56vTqbk8A_qC85-uImbQw7BBrJjbuWLHqriqsspslSk3Xgow4jjW_9BKvz3so2nWKB2Flieof1JNUhB5XPOPDl4o757XPuLXvvzSYo36wYppCcxHKn2jzLKPKQ-Zl8JmCPbc28-T4KrdDd9cZYXPHNZMVz4XVNW08w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در جنگل‌های بهشهر؛ هیرکانی دوباره می‌سوزد
!
‌
🔴
شعله‌های آتش بار دیگر بخشی از عرصه‌های جنگلی مازندران را درگیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/140764" target="_blank">📅 17:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPQw6zTgMZSOzFfjONlMlpoShN54Xr625GgTPztNceUUCwhW0y9UkTsZfpZgnYtwcbBM25BYaAWs8mpStbxy1UX05YhNzl8tr0B0hzYXei6IxDoq0KByla81TRLauGuIPJiSBF63ajP0_zj5ZO784e0Sx2yeRFfTDjrzh22Yli3wAnVXe5Ycl4gPj7gIAlpl0aBNicRBoCzeXZ8pxyVdR1Tyqv8boXkVp6Yt9_Gh1kWTBH9OJ1zbDqLvmLgcazID6ZBnkOpXD74Q4npd4ljKjBq4lDCkThvT8CS_OkHXZWxSko8Z36XA5Iil6-FPjRSd0x8MZCKBKgeVtBzeANDuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به وال‌استریت ژورنال:
🔴
به تمام اهداف نظامی خود در ایران دست یافته‌ایم، اما گزینه ازسرگیری جنگ همچنان روی میز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/140763" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4a83f3cc.mp4?token=hj0MktF_2S6Q0nAmmCnxrtJIZo2-a4KVC8o4e1UYMUrkGpL_FFw6GiE50zQNpFQkoqmXgioElLds4VUyntIolKUpUlsQdGH5razq6ehP2OlxRWCXV9HsbZD8b4F7cP-wai5N21lN0UOE1EWSfHiLnBi3hhRI2yuPnKIEH676hO9FNEle06zkbXr2vDyaq98ksZYV8UMtg_nDeVXMCuT84lNwXY98bkSx8zT0MQBM3HRtqgSC_xiztWaMeZ2KH3ttyHFC3b5lxNnScVHxPSlpC7__t_DDLKRN45Xl3e7UDIi7SJDldfwAP3RuwNNt5cEYBy0FR4gIHWrNxGKuysl8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4a83f3cc.mp4?token=hj0MktF_2S6Q0nAmmCnxrtJIZo2-a4KVC8o4e1UYMUrkGpL_FFw6GiE50zQNpFQkoqmXgioElLds4VUyntIolKUpUlsQdGH5razq6ehP2OlxRWCXV9HsbZD8b4F7cP-wai5N21lN0UOE1EWSfHiLnBi3hhRI2yuPnKIEH676hO9FNEle06zkbXr2vDyaq98ksZYV8UMtg_nDeVXMCuT84lNwXY98bkSx8zT0MQBM3HRtqgSC_xiztWaMeZ2KH3ttyHFC3b5lxNnScVHxPSlpC7__t_DDLKRN45Xl3e7UDIi7SJDldfwAP3RuwNNt5cEYBy0FR4gIHWrNxGKuysl8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قرار بود اینترنت دیگه باز‌ نشه و همینطوری بسته بمونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140762" target="_blank">📅 16:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ در پی خاتمه جنگ با ایران است
وال استریت ژوزنال:
‏
🔴
دونالد ترامپ به مشاوران ارشد خود گفته است که ممکن است تمایل داشته باشد بدون آنکه توافق هسته‌ای حاصل شود، به جنگ با ایران پایان دهد.
‏
🔴
این تصمیم مشروط بر این است که تنگه هرمز به طور کامل بازگشایی شود.
‏
🔴
طبق ادعای این رسانه آمریکایی، ترامپ معتقد است که برنامه هسته‌ای ایران به قدری آسیب دیده که نمی‌تواند به شکل قابل‌توجهی بازیابی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140761" target="_blank">📅 16:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03e0d9e77.mp4?token=evun4-8t8n9aoC45iL6oRQs-QuxI8-Ev2EonkvwkeRP-B0ZMPouY7D8s4fEu0qGuKTpuSwScoWJN7hyMJ99ThmvErsX6ekEqcFyL_IDFVg4_4ffqZB3l1rMN7upXjYQ7FJEMgtywno1agK6WAmAfQmzVfGOrFNXix5YwZzv0AHhSTqd8NNI_f9UlYBKY3qKi38XdrRZhl_u-hvAS0zRFS6sMpJOLPv9hPfyhbFqagBDJL1nI-VM46MSBAY64oXaNSVIEGv-5SMxA81Eq0thwSbbK1yvt0mjcCHbYFM_kRAPujQoegKQG0TEsLGZqFx4qjLpSRhwZXa3fWb3J-IWoC6cTXqd9KqhpK54uHDoRh_6_8ksbSGgw8_cy01Ag9A8DvCrXHIetKLR0E9LJexT6RBq3rOqU-sV9tK0xStaEOiOkysoljYD4yrtmp_HbINTfPFuH9kXdAZx8Z9Ty6GFy_yOkehIHuybPFW6iyepbD6LktnJzrpnP2D8H7JOqx38RmWv025QvQQ7VGlw8daCHYtgUzcYYOfb2D_xKCIZXDjxuwIzYckBzjCCwTuaolfbyUj5rvlDn53yu1rEGY2xOEDL7gq1pzKrCZj7iifMlGvcz1x5c7vB4PQ_jU5xx6wIdNBkEnSCf9IlBAzrprnvLm-8oiVP3rTq73nqVnTqXoe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03e0d9e77.mp4?token=evun4-8t8n9aoC45iL6oRQs-QuxI8-Ev2EonkvwkeRP-B0ZMPouY7D8s4fEu0qGuKTpuSwScoWJN7hyMJ99ThmvErsX6ekEqcFyL_IDFVg4_4ffqZB3l1rMN7upXjYQ7FJEMgtywno1agK6WAmAfQmzVfGOrFNXix5YwZzv0AHhSTqd8NNI_f9UlYBKY3qKi38XdrRZhl_u-hvAS0zRFS6sMpJOLPv9hPfyhbFqagBDJL1nI-VM46MSBAY64oXaNSVIEGv-5SMxA81Eq0thwSbbK1yvt0mjcCHbYFM_kRAPujQoegKQG0TEsLGZqFx4qjLpSRhwZXa3fWb3J-IWoC6cTXqd9KqhpK54uHDoRh_6_8ksbSGgw8_cy01Ag9A8DvCrXHIetKLR0E9LJexT6RBq3rOqU-sV9tK0xStaEOiOkysoljYD4yrtmp_HbINTfPFuH9kXdAZx8Z9Ty6GFy_yOkehIHuybPFW6iyepbD6LktnJzrpnP2D8H7JOqx38RmWv025QvQQ7VGlw8daCHYtgUzcYYOfb2D_xKCIZXDjxuwIzYckBzjCCwTuaolfbyUj5rvlDn53yu1rEGY2xOEDL7gq1pzKrCZj7iifMlGvcz1x5c7vB4PQ_jU5xx6wIdNBkEnSCf9IlBAzrprnvLm-8oiVP3rTq73nqVnTqXoe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد جواد لاریجانی: باید به زور هم که شده غرامت بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140760" target="_blank">📅 16:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏
👈
الجزیره به نقل از جی‌دی‌ونس: آمریکا به توافقی درمورد تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود
‏
🔴
نورالدین بوزیان، خبرنگار شبکه الجزیره در واشنگتن، به نقل از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گزارش داد که ایالات متحده به توافقی دربارهٔ تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/140759" target="_blank">📅 16:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی صنعت برق: خاموشی‌ها تا دو هفته آینده به حداقل می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/140758" target="_blank">📅 16:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGEY4mHQ73llDdd7KbhBy0SfAMvK3BceePNYGO9fNWQHPPerC0juBu7OHkg71EqqZ4Dz9alI90x1c285JmedYQDpvGgPnH5I-CbS5aTOPlURLHqCerHZpqMJUYc_MzBmmPVlCE-IzGzex-hhKzsgu_ZrIKlXCjolKbFXLHsSbqxVc6d9KIIsF8zfx6XoXTDibSErmLNv6ftSxEQcjxPCREB46ajyiGCMFFdPKA5S7lp90WJTrLjfKrlbzL0YY0joqOAREf1_UiQfowh2QoKaYEQRA0l4xIWklqdE1WE_lhbwzGHOqSbwLv8QMJzKmcbgzBQ0UYk4ZRYukFDlWHdxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUjHSbyre33sljKjLwXZK_RSLzVpmuAR30KTUuiTSWXA4tObCdom7Ft4NCx_YDMGn14uXLMhUopLRRX4u9DtVVInQG455wQycx1fosxjcUKPTXTLb4sI5subD9LBFveu6CTEZcq4dYcxd_j-Iw3wICaen-4NC08nW3LAaDVrCFSVQvR1XdD7dAoRd7kSjx9uiRIaDB7sdgKlndRhXlezZS40jnfzRzIHcVz267E2OQDOQdfmgL3gtG66TbA0_7P9VEGUp5Su2KyIU0D_xy8T90cY0PYA6muS5jwgTAJ4Vti00Yy0OHQPijAhykuDqZJNOTKWM6ObqjP3gfCXtmKCYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت خارجه اسرائیل نقشه‌ای در ایکس منتشر کرد که ادعا می‌کرد داده‌هایی درباره سوءتغذیه حاد کودکان زیر پنج سال را نشان می‌دهد، اما این نقشه حاوی چندین نادرستی جغرافیایی بود، از جمله نشان دادن بخش بزرگی از جنوب لبنان به عنوان سرزمین اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140756" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAZoKIU_gzt3KPBM15TeQTxXq-N_bVnDpK_XBIOk5VcW87nTZcO7dyEaKQYc0dN3jxeYrnQMIMk-7Ea4dTBBvOPaogIGU5lyU4rA1TVBpzPnTWboICHq-qM6Tp1wqR86YGqJShvKfTp4rU--MtnzlCW3Fpyct3mtjJpWypEIIAC4-UKnyOQ2dafaykK4rdjCmVunfL8V0g7_MGpGX_dasA-rCIrs6ZF-cSEjwx5ODuQTYA8ZQK-GonMSIXGX1BHEhGpnEQ1SyMoziDeQkYLaKlwBzABINgJVlSGsZIhYfEDhnZ7iuio7VUn2MyhUhlCLv8kwXrUp49RLZCWJV7mMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطرناکترین سلاح دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140755" target="_blank">📅 15:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اولین شهید راه دختر
💢
🔴
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.  ‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140754" target="_blank">📅 15:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اولین شهید راه دختر
💢
🔴
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.  ‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140753" target="_blank">📅 15:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pm4bXjFb0MQo38dhP_RoJc-pWKHNswAh6MZPWsLBsILtBl_kUWGSto084AF8Z-znakzeCkdE77a-Jx7pEhqTxO_g0y8PhELNZP8_irRcc5eR5UyvzpmCZ0GMNoA4CMVTW-byFMG8w0PrGZpL55xhJv6m_CTTa6ROVsWHyh3AgdvHjjItggH3f1OBjcluRCFTtP8poCUuFg0zvk3JmPMtSdA5jbeZIr9Z1_ycqvXU3evZYz7A73mbo8kK8-KWbxM5Stvf241ojr2kSb_YnEXJtbH3nZozFt7UgFhue_wJ54-NTeQ7Y3fDaGIsVwjiC6d5lLIsWgG29l9C7pANN1vGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eq5HqFkeUmPLHAtbULovKekc1Av2uV2s5DDEgKnh8SqLgOmj93VuWRa-10KKVbZah0dfKky-GgrVTBRNWicZPPakcnQ2CLb_r0wZOSlrVy_WzGWGnGfplX_Z8r-uFgAPnjbAUVHIDwzJPOBDQS3k4GaNWqc9eXNezq047qxyE8ID34VvcJ2IGl3fgjJaUUrcIUJVf-y1HANdtrHp7IUomWxih3OBZCqLju8ZSSen5voDGdO7Q3sg3HCv95RB0ybHtnRTzfwtVqzlofhyxLTDt8l5Il3CEc9WCa0utRZ1JCVairz3N2L5WvzXR3jjNHlf8opohTEFLLZYfdxoMW8b3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اولین شهید راه دختر
💢
🔴
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.
‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل برسانیم و هم فیلمش را بفرستیم به کانالی که بابت کشتن بسیجی‌ها پول میدهد!
🔴
رفته دیت و کشته شده
#دویست_پنجاه_گرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140751" target="_blank">📅 15:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرگزاری تاس: روسیه از کشته‌شدن ۳ غیرنظامی در حمله پهپادی و پیشروی در خارکف خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140750" target="_blank">📅 15:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روس اتم اعلام کرد: ۵ متخصص روسی به نیروگاه هسته‌ای بوشهر بازگشته‌اند و تعداد متخصصان روس در این نیروگاه به ۲۵ نفر رسیده که قرار است تا پاییز به ۱۰۰ نفر افزایش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140749" target="_blank">📅 15:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c10e4230.mp4?token=vz00tL3k-KfiiZ6SzCztebLtwrJScS85e02H59Ss2wwCnXlPoT-sH5CdHnzaHN32npihof9BhCPmluN0RMLscqI2zCLnQBS8odx7xi8eZG0k1_RJ4PSj4CtdOoOekkGS2qvAVFCMWxfCUXyOE7T6hc20FY2ojXc0EB83vWrTzRzH_TwPLVQ6eoU9s1cmP5-CC6qatWqmf8ELCw6pJ8-38AqjWMVFn0u0LOhdT53bOZEXFhQ1ZYbc6eEir6trmvscPRIhLpdQWWMB-bu8FCtswiDi_qn6KOo_M_kVDlKr0AVTZyU6-gSxTHiEw3vBoqdGXIkCabofvdSNXlZSY2gBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c10e4230.mp4?token=vz00tL3k-KfiiZ6SzCztebLtwrJScS85e02H59Ss2wwCnXlPoT-sH5CdHnzaHN32npihof9BhCPmluN0RMLscqI2zCLnQBS8odx7xi8eZG0k1_RJ4PSj4CtdOoOekkGS2qvAVFCMWxfCUXyOE7T6hc20FY2ojXc0EB83vWrTzRzH_TwPLVQ6eoU9s1cmP5-CC6qatWqmf8ELCw6pJ8-38AqjWMVFn0u0LOhdT53bOZEXFhQ1ZYbc6eEir6trmvscPRIhLpdQWWMB-bu8FCtswiDi_qn6KOo_M_kVDlKr0AVTZyU6-gSxTHiEw3vBoqdGXIkCabofvdSNXlZSY2gBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140748" target="_blank">📅 15:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وال‌استریت ژورنال گزارش داده ترامپ در صورت بازگشایی تنگه هرمز از سوی ایران، مقدمات اعلام پیروزی در جنگ را فراهم کرده است
🔴
به گفته مقام‌های آمریکایی، ترامپ حتی ایده پایان‌دادن به درگیری بدون دستیابی به توافق هسته‌ای را مطرح کرده؛ یک مقام کاخ سفید نیز مدعی شده آمریکا «به تمام اهداف نظامی خود در ایران رسیده است»
🔴
اگر این روایت عملی شود، بازگشایی هرمز می‌تواند برای واشنگتن به نقطه خروج از جنگ تبدیل شود؛ حتی با باقی‌ماندن پرونده هسته‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140747" target="_blank">📅 15:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مایک هابی، سفیر آمریکا در اسرائیل: توانایی ایران برای تولید سلاح هسته‌ای به‌شدت عقب رانده شده است، اما متأسفانه ظرفیت موشکی‌شان افزایش یافته و تنها طی یک سال، برد موشک‌های بالستیک آنها از حدود ۲ هزار کیلومتر به بیش از ۴ هزار و ۱۰۰ کیلومتر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140746" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بیت کوین امروز با کاهش ۰/۱ درصدی به ۶۴/۹۶۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140745" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو طرح ترامپ را رد کرد
🔴
نتانیاهو:اسرائیل طرح ۱۵ ماده‌ای غزه که توسط شورای صلح ارائه شده را رد می‌کند و تا زمانی که حماس واقعاً خلع سلاح نشود، هیچ گونه عقب‌نشینی انجام نخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/140744" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b249a4d6.mp4?token=o3RCFsPlSk_PKScjLxHL0adLukFHykWZT-SrFzxqlvZtXG4BDGTUBdf6tJSt-AWY_GP3RFqkc6dzHWFddn4WoWODqpQgrhYuG57pvjy_VE2LPPs7EF4bO93OLaNRU643veFBKJl6zQKKFOXoeM7G1vxNoOA_eaDixYO4WNrqP0Vrz9ZZz-B6__AHRdp-U-VnLCFI-U7FzkmuGFAuqkaesdkvFgepPBQ5_CaNlPUlY7k2uy1QX1-bxLb4EhkfVl_MzHxdgF5dsbnApl4ZMRLDCZeIHqjhmf_xPFxQzpz0zRpVDt7W3XCtPaOG7SCbyuFToKw3dXHCj5-3FptbrcTfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b249a4d6.mp4?token=o3RCFsPlSk_PKScjLxHL0adLukFHykWZT-SrFzxqlvZtXG4BDGTUBdf6tJSt-AWY_GP3RFqkc6dzHWFddn4WoWODqpQgrhYuG57pvjy_VE2LPPs7EF4bO93OLaNRU643veFBKJl6zQKKFOXoeM7G1vxNoOA_eaDixYO4WNrqP0Vrz9ZZz-B6__AHRdp-U-VnLCFI-U7FzkmuGFAuqkaesdkvFgepPBQ5_CaNlPUlY7k2uy1QX1-bxLb4EhkfVl_MzHxdgF5dsbnApl4ZMRLDCZeIHqjhmf_xPFxQzpz0zRpVDt7W3XCtPaOG7SCbyuFToKw3dXHCj5-3FptbrcTfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که امروز گرفته شده‌اند، نشان می‌دهند که خساراتی به یک پایگاه نظامی که توسط نیروهای وفادار به عربستان سعودی در منطقه مرزی الودعیه مورد استفاده قرار می‌گیرد، وارد شده است. این اتفاق پس از حمله‌ای موشکی و با استفاده از پهپادها توسط نیروهای یمنی در روز جمعه رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140743" target="_blank">📅 14:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نتانیاهو طرح ترامپ را رد کرد
🔴
نتانیاهو:اسرائیل طرح ۱۵ ماده‌ای غزه که توسط شورای صلح ارائه شده را رد می‌کند و تا زمانی که حماس واقعاً خلع سلاح نشود، هیچ گونه عقب‌نشینی انجام نخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140742" target="_blank">📅 14:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تسنیم: محسن رضایی به‌عنوان نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی ایران منصوب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140741" target="_blank">📅 14:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
فارس: پزشکیان امروز با رهبر دیدار و گفت و گو کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140740" target="_blank">📅 14:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
تسنیم: محسن رضایی به‌عنوان نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی ایران منصوب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140739" target="_blank">📅 14:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رئیس پلیس فتا تهران بزرگ: مجرم اینترنتی که با وعده فروش لوازم خانگی اقدام به کلاهبرداری می کرد شناسایی و دستگیر شد.
‏
🔴
متهم حدود صد میلیارد ریال کلاهبرداری کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140738" target="_blank">📅 14:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=q82jrtdIJPcN1_h1-X6A6S1gW46BJto-rXcvVXhEn1SRiLMBntH4xusUi18ExasBtM72vclLqD2P7aGjGffUbeytndT2TezEpsM2OP9DQ47eyt2xt6AqUEw2wyoESOR8PEXZR47Bo6m7yUVyVDSgiF3NOwLbyYjXzKHywu7NmtwOIt9LwU1ZMLF9IPteRa95JzJlecA_5O2C503OGEmJe_811b9z256tDcuxghMwlV3s3NFQ-QChThWpaezAhUAArJzgjPTYHnjMHJDsKgm3jNbfTsGa3PbeYrw54sOBJ0R5hbyT0tVsU66AlqGJl-q1fBKnhBlhMkn83B8akO1F_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcb47fdfd.mp4?token=q82jrtdIJPcN1_h1-X6A6S1gW46BJto-rXcvVXhEn1SRiLMBntH4xusUi18ExasBtM72vclLqD2P7aGjGffUbeytndT2TezEpsM2OP9DQ47eyt2xt6AqUEw2wyoESOR8PEXZR47Bo6m7yUVyVDSgiF3NOwLbyYjXzKHywu7NmtwOIt9LwU1ZMLF9IPteRa95JzJlecA_5O2C503OGEmJe_811b9z256tDcuxghMwlV3s3NFQ-QChThWpaezAhUAArJzgjPTYHnjMHJDsKgm3jNbfTsGa3PbeYrw54sOBJ0R5hbyT0tVsU66AlqGJl-q1fBKnhBlhMkn83B8akO1F_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده نیروی زمینی ارتش: پای نظامی آمریکایی به ایران باز شود آن را قطع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140737" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خبرنگار العربیه: بیش از 15 حمله پهپادی توسط حوثی‌ها به بندر المخا صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140736" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
به گزارش تلگراف، بر اساس طرح جدیدی برای روابط پسابرگزیت، بریتانیا می‌تواند بار دیگر به بازار واحد اتحادیه اروپا و منطقه تجارت آزاد این بلوک دسترسی پیدا کند.
🔴
در مقابل، انتظار می‌رود نخست‌وزیر بریتانیا متعهد شود چتر حمایتی نیروهای مسلح و بازدارندگی هسته‌ای این کشور را در سراسر اروپا گسترش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140735" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
توقف موثر صادرات نفت ایران، چین که بزرگترین خریدار نفت ایران است، در حال حاضر تنها محموله‌های باقیمانده‌ای را که از قبل در دریا هستند، دریافت می‌کند و پیش‌بینی می‌شود حجم این محموله‌ها در هفته‌های آینده به شدت کاهش یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140734" target="_blank">📅 13:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به نظر می‌رسد اهداف مورد نظر در بندر المخا، انبارهای سلاح و مهمات هستند. نیروهای یمنی در حال حاضر، با همکاری نیروهای وفادار به خود، هرگونه عملیات احتمالی عربستان سعودی را با هدف قرار دادن خطوط تدارکات و انبارهای تسلیحاتی، خنثی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140733" target="_blank">📅 13:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عراقچی: تنگه بسته می ماند تا زمانی که آمریکا همه شروط ما را قبول کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140732" target="_blank">📅 13:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت دفاع روسیه :  نیروهای ما کنترل روستای واسیووتینسکه تو شرق اوکراین رو به دست گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140731" target="_blank">📅 13:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IByeDhIT6DVFTNOziyK8lVVM0bHU8oj1l6234kn4Qar0GLzARD5HiAEQMwbZ0NS3dIigfdXvhUJJqLTcQpCe7LehLtPIqhF_FYXYqwwQJIPn6SvZT7VoE5jxIqANYtp5AbkcZN2lVrFpzQBYVycEOioG8t3Hb57lqgG-R4GSaBY-8wYzVmSHUyWcflzdVoPPFObLt1zElhjoa_F4jaQILJ_oO5uYsVRvnUx6n3HcVVDUU-l_O3WZJkBQcXhuodcHT52NmITioRwwRU94OlpHt3AoErFPYE8HLtgatKltDweS3Jt7pGkLuYIMoPBGh-JNApPSxbxZtYmBbRZPPZdvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقدعلی، نماینده مجلس: بهتر است آقای قالیباف از ریاست تیم مذاکره کننده و مسئولیتش در مسائل هماهنگی با چین استعفا دهد تا به کار اصلی خودش که اداره امور مجلس است برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140730" target="_blank">📅 13:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8qEuaoSL0suyYYOsO-JOmIu8hDsjvfNoaCP8hftnaPv_EXPWKDghW-2gHhHvj7NmyWKi5ydJ8LTbrocW30l_yCWSHudGGG0sZIJJdxF-kHvOVOfjjSVpLGow_oGXVVNhjuVyMuurW3Kwu6M-qN4j_tUVFva8a_LEiRryAQAZrRivhBonfTkPYXAs4QesmHSXVeiNL6rISskAAAgQmAKXONqnWebcx_obLzFDtVY3zBAviGl293V2t-LX7Kajs43wrnb1BG2ZCXznQVufNhfi9Hb0Gs7HXabEn3jgtgHkQHoGeGMa44FqBagvYJu-gmWix-eF6ZR-8EyDIKT-M7X7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر می‌رسد اهداف مورد نظر در بندر المخا، انبارهای سلاح و مهمات هستند. نیروهای یمنی در حال حاضر، با همکاری نیروهای وفادار به خود، هرگونه عملیات احتمالی عربستان سعودی را با هدف قرار دادن خطوط تدارکات و انبارهای تسلیحاتی، خنثی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140729" target="_blank">📅 13:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d3ed61b8.mp4?token=JPk2lHZ9JM_gbuORmMoIeJtGsGtMP58fFcQI0WYlWa25VGG_AGWScWnmgyNV3Jl64X8FosdqaXnFk9yRp8lUM8KSi4JmroeCtMu-UpfOvEVCp47CEGc05HuvU5muapYKeAeAp8pfd9-j6XxZm83dLakg2ENfSxm5YcfYPOWoRqda09Y-oR5g19-BpSMGGv_qgR4Vy_SYrMqeAg6xvVeK0AI3BQ__EM_Hh3o7vOmkJeo6-fl2alElZbneVj1FBmWHc-tcnkvapGiuYw222IbNWN64EDLdzM_rH6XEcZJ2C80l9wRUrVQSdYaaKGJtqjTBzm8HVA7INdFjGt4mYLjWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d3ed61b8.mp4?token=JPk2lHZ9JM_gbuORmMoIeJtGsGtMP58fFcQI0WYlWa25VGG_AGWScWnmgyNV3Jl64X8FosdqaXnFk9yRp8lUM8KSi4JmroeCtMu-UpfOvEVCp47CEGc05HuvU5muapYKeAeAp8pfd9-j6XxZm83dLakg2ENfSxm5YcfYPOWoRqda09Y-oR5g19-BpSMGGv_qgR4Vy_SYrMqeAg6xvVeK0AI3BQ__EM_Hh3o7vOmkJeo6-fl2alElZbneVj1FBmWHc-tcnkvapGiuYw222IbNWN64EDLdzM_rH6XEcZJ2C80l9wRUrVQSdYaaKGJtqjTBzm8HVA7INdFjGt4mYLjWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویر منتشر شده از سوی وزارت دفاع روسیه از هدف قرار دادن انبارهای پهپادی نیروهای مسلح اوکراین در منطقه خارکف
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140728" target="_blank">📅 12:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDlfvRLkTVCjPWeM4SBGwn6gvZO7aAoXO62wcPCeXgGZho2BPfkhOL_8AluE3T4ibZuXv-imXxA5KRI7PZQTlbdLjj5YALRCixnvcAc968iXjpEnuxVNLO1BuvzG8pjLeVpHV-aWxsFk2j6U-weaC3ol4OEKvfhDL440lo0hFY8yuDXF6TPK1fMsIvmhmBG7XviwNaSyQ7sR71AGR2Aw2J6mL9cGegk6mEKcqg6ZnfddPvhKP25VBCOKcliqfLv1RcwVfoCSnR3Q1tjk2Orjh2NtIy5kPOZMVNXkthjiN5pLYhmzTSuC3I_WzALeMjcbkrebCNI6wXT28wWMImwViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انصارالله (حوثی‌ها )به محض رسیدن تجهیزات نظامی به نیروهای سعودی در بندر المخا، آن‌ها را مورد هدف قرار می‌دهد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140727" target="_blank">📅 12:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b12df0894.mp4?token=By2x329j97785pQSZZ05JLubKrjXPNvNrvIhvIE9ONu4VTXXjL75Hm2r5L-60fdJptBA7FVL3_a4awqgBYNVR4LW7C7n6dtIsr_esXLHgEcPm7k_jj_vIMj1Mkbwub6pu2RU9IYrIbzAtRznezuJSWRvf0w7CZKaGUSUiXGo8TioqiELWr4wTS4L6T8NZmfUHLy76gSycMPcJilOC2HyvZ0NNNdS3vC4nh3dtoV5z9NtlpDmtkBYUpL-dxZQ5iCBOVekyfTTnRl20yilqSRO0VPXQR5cRg48f3RLSkpBF3veezN92KwdybHRaVQrBDK10Px-84ESQfCf_JAB-R0XzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b12df0894.mp4?token=By2x329j97785pQSZZ05JLubKrjXPNvNrvIhvIE9ONu4VTXXjL75Hm2r5L-60fdJptBA7FVL3_a4awqgBYNVR4LW7C7n6dtIsr_esXLHgEcPm7k_jj_vIMj1Mkbwub6pu2RU9IYrIbzAtRznezuJSWRvf0w7CZKaGUSUiXGo8TioqiELWr4wTS4L6T8NZmfUHLy76gSycMPcJilOC2HyvZ0NNNdS3vC4nh3dtoV5z9NtlpDmtkBYUpL-dxZQ5iCBOVekyfTTnRl20yilqSRO0VPXQR5cRg48f3RLSkpBF3veezN92KwdybHRaVQrBDK10Px-84ESQfCf_JAB-R0XzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
4 انفجاری جدید شهر المخا در غرب یمن را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140726" target="_blank">📅 12:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kgcHhD6YYDkbwbQWLd50CHez2niSiTJdmM9yhykunZXFA-5Nfek7HZpW8ozX0-GV71HC3fejLFHnVdBowZYCu7F97vQBbPl-QKqzsIuciS4SvHBkWhn7zk2U7FKCL2kzFnxXmV5GpwuPYFizwg8A3lWzOa0yvcry_bupxonSVb6yMxYXb9PMseASAjzpkjTnYulHS65YmmMi29KSX54IDXLOc9XZlYrTx4sFmx_Lyc6GmbTrxa0VpfUoUYlopwDT5XNa7bQNg4nlJ7JRg2piBV40hRFDvM6CEfuRGNN9XEUaf1quTotNmumO2DpCoPN4UavTftSGiA1E4l955KBaWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kjhR9YPtbzbjOpFoL6QFEO3rXX7b8HqpQ6b6O-9G3mB2a2v69NrUDzKf0EYPeU5RqZtyzGkC_KMp5dUuTxbXASnuQ0WAHHY3q2hu-B8o9cdEo4J1CX31_gy75ORg3P-wj96jj7R0EEyOl66lZjN4vfbFvZmdQD-hskksRw_KP4-xvlhvk942p_OQYuSBbYceT9UHli1-mQLS07SVf-JhjLpwapt29FoCc9vfXxRp6RPkmKbfP12pMayULm5Wk3S0r4xuX7yle6EkenaUUqCGmbnhu1id-n5sHaeG8Oz5ijJfn3DOByWWrdXkbw3ZT7y3HnQXw7Pk2ZnSDl9KyqS_uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زیر دریایی راهبردی هسته‌ای متعلق به نیروی دریایی روسیه در نزدیکی سواحل قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140724" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140723" target="_blank">📅 12:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی پلیس: نفر اصلی دخیل در قتل حمیدرضا رجب‌زاده دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140722" target="_blank">📅 12:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqAmhJjgHvM9eEgweTZJEPLiyrGhn5hzZSHh1Uv4Ilmni6porqyMGtY9VZKNLFyj81aqisnuVVK9jSyEii9CU27WR56q4gxvmRQwPsR7x80X_KhVXx6kX2MByk5oZTZYC7BTaV0ldsW_8Tav3WABMzzAsttdLaOkmvYu2UK871G0Izz1vKM3ZtMC84dy69Ee-UCVczK4gpvNh2FMzOt-JcrYB5Pjq7sZrrHCAxDB2KJuLYQ4x_vmOscW2xaN8neQOcr69Fz28Sv52-9u0Hvkqp4SVPF3dT_aLnYrPvKHE5iZ4dhDTbuSE4GuXiZyyql9VNrJ_mObuGycS6h7XEkGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدف قرار گرفتن بندر المخا یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140721" target="_blank">📅 12:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu0_GUf0jClICxM3GVbhc1fcrJlI3d1PazdH2qfeEh79gwhvS0EmtIzH6hX-0zeKsql2OQ01gTCHXJCOremCOxha0kkrP7tnqaVKjOLPrCcVdy8Nvx2Ixf0mHzDoGOx8uY0NknCfqjePnd5cd0lG_urLOkwAlXg9UdCECEGopRYb36qVlAN4oh9hLDe5tPpE4iGjqIRT88YUNt8a5kxHr1C8eq_TI_pspUQHKBzXGml9ivtDM28_lcZdf-8E_3QW1YhjjEuaKnYVH9HJ7LMsNZDIzJMiNRnmxl36P1UrP0zT2cKkSJzcUpt8J0sgiOXE3YqoG6EIOWDNrMa_kGYYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: دو آمریکای بسیار متفاوت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140720" target="_blank">📅 12:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9866e3c08.mp4?token=iHu2IMJK8fcSW9pxxkDycptKtSNlxoqdCKd5MfyaqHcjq0xYNoCCUUhaCHqHNbGOr6b_9ks426FCtvYUoNatdB55Zbe3uAbrF3yGl1_nq3xIf_zub-7KUW5ubl86sig3kX5iT3F3eaUD_lIGijoXYDE_XGkXRa5AyhX2nqVqchTEHpSEh4v2l1n58h0qmPVJmBFcTj29zM-Pc3A0OOkkFmv35wtRpLx5p4GJjXafFja_DBjm4cstipf2-GXhvDx8f9Y5oXidffjnyrwQrNVD9aOYxTRTLsQ9xwtNnHubZsKGszF66-9kfq-JgL-W34cHrMqu33Lw05A5yytDm9Ph3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9866e3c08.mp4?token=iHu2IMJK8fcSW9pxxkDycptKtSNlxoqdCKd5MfyaqHcjq0xYNoCCUUhaCHqHNbGOr6b_9ks426FCtvYUoNatdB55Zbe3uAbrF3yGl1_nq3xIf_zub-7KUW5ubl86sig3kX5iT3F3eaUD_lIGijoXYDE_XGkXRa5AyhX2nqVqchTEHpSEh4v2l1n58h0qmPVJmBFcTj29zM-Pc3A0OOkkFmv35wtRpLx5p4GJjXafFja_DBjm4cstipf2-GXhvDx8f9Y5oXidffjnyrwQrNVD9aOYxTRTLsQ9xwtNnHubZsKGszF66-9kfq-JgL-W34cHrMqu33Lw05A5yytDm9Ph3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها
:
پالایشگاه آرامکو تو جیزان عربستان رو با یک پهپاد هدف قرار دادیم
🔴
این حمله تو پاسخ به ورود پهپادهای عربستان به حریم هوایی استان‌های صعده و حجه انجام شده
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140717" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
عراقچی: مذاکرات با عمان در خصوص تعیین مسیر دریایی جدید در تنگه هرمز است
🔴
این مذاکرات خوب پیش رفته است؛ می‌توان گفت در مراحل پایانی هستیم
🔴
مسیر‌های قدیم با مسیر‌های جدید جایگزین می‌شود؛ متخصصین روی تقشه در حال کار هستند
🔴
این به معنی باز شدن تنگه هرمز نیست
🔴
ممکن است توافق صورت بگیرد ولی باز شدن تنگه هرمز منوط به یک‌سری شرایط دیگر است که از طریق واسطه‌ها منتقل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140716" target="_blank">📅 11:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هشدار فرهادی، سخنگوی وزارت آموزش و پرورش درباره زنگ خطر کاهش تعداد دانش آموزان: در هفت سال کاهش بیش از ۳ میلیونی داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140715" target="_blank">📅 11:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd19b5ce80.mp4?token=I4EWauJJ6jh1ZzzbV714D_48L95g7DLAs42JGq1C4rAWlPx2HXb_Q3yjwpQpCDUUmaMOM3PxdQc_o3pBUIBXOC2D_JfXStJLi2XEZiMygLEQaYtVhT-3VHeHAgd8Q-xiNHWqu7TfrmPb8apvorSJ-zxoH-ibXDrWv-jz1WbDofghadN0UiO33XnOgMigPsTpvi7K83AAdJLHnbr4cxR9a62VzNPbiHAI2I7yhvD2pkeKo6A0UAlDhYdyIdrPlNuBVYa9yhdlpIwj-LOjMnhuisuOawhUNScYL2u-uqJkjTrLNha5t3AsZowUGE_kCACbH99e6Y9rKVtEqY0h_FKb1w3ygTOtNu2vrUv73qi-7JPysjEhc0DVZCBy-V04OxSC78hahpd9JxZpoGpiSyei9NG3xSM9gwD0JEYenOQLJqTkPldFt3LMbkdux-Ch2mRG_j_yIEIxaLgHOn0EHYIo26HdTl1QgkRPqoe7-bA-L8sxht_7ivtOvxfP-pNe3ZATnmaV0_nYm-JRFkipw88mOV1phG9cFEvsOybuNtp2RqqOWYrOklCXIiv9iY3GgDXSxiK-SfP2_FkvMJri8xVzDl-XvCYRmi9kfb-OsBjJroaCnh5NeQpPXO8D63acXu2_tIlJFNVLgIMEwOGuym57r3-JgZm7k25YrirtGgGxUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd19b5ce80.mp4?token=I4EWauJJ6jh1ZzzbV714D_48L95g7DLAs42JGq1C4rAWlPx2HXb_Q3yjwpQpCDUUmaMOM3PxdQc_o3pBUIBXOC2D_JfXStJLi2XEZiMygLEQaYtVhT-3VHeHAgd8Q-xiNHWqu7TfrmPb8apvorSJ-zxoH-ibXDrWv-jz1WbDofghadN0UiO33XnOgMigPsTpvi7K83AAdJLHnbr4cxR9a62VzNPbiHAI2I7yhvD2pkeKo6A0UAlDhYdyIdrPlNuBVYa9yhdlpIwj-LOjMnhuisuOawhUNScYL2u-uqJkjTrLNha5t3AsZowUGE_kCACbH99e6Y9rKVtEqY0h_FKb1w3ygTOtNu2vrUv73qi-7JPysjEhc0DVZCBy-V04OxSC78hahpd9JxZpoGpiSyei9NG3xSM9gwD0JEYenOQLJqTkPldFt3LMbkdux-Ch2mRG_j_yIEIxaLgHOn0EHYIo26HdTl1QgkRPqoe7-bA-L8sxht_7ivtOvxfP-pNe3ZATnmaV0_nYm-JRFkipw88mOV1phG9cFEvsOybuNtp2RqqOWYrOklCXIiv9iY3GgDXSxiK-SfP2_FkvMJri8xVzDl-XvCYRmi9kfb-OsBjJroaCnh5NeQpPXO8D63acXu2_tIlJFNVLgIMEwOGuym57r3-JgZm7k25YrirtGgGxUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: اکنون هیچ مذاکره‌ای با آمریکا نداریم
🔴
عراقچی : واسطه ها همچنان دارند تلاش می‌کنند تا راه‌های مذاکره را مجدد پیدا کنند.
🔴
تا موارد نقض یادداشت تفاهم از سوی آمریکا به پایان نرسد و آمریکا انچه را که نقض کرده جبران نکند، از نظر ما امکان شروع مجدد مذاکره وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/140713" target="_blank">📅 11:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
روزنامه آی‌پیپر: ونس در یک بن‌بست سیاسی بسیار پیچیده قرار گرفته؛ او خود را میان جنگ با ایران و مذاکرات صلحی که اکنون تقریباً به‌طور کامل مسئولیت آن را بر عهده دارد، گرفتار می‌بیند
🔴
بزرگ‌ترین شکست ونس تاکنون، ناتوانی او در متقاعد کردن ترامپ برای نرفتن به جنگ بوده و دومین شکستش ناتوانی در پایان دادن به آن؛ معضلی که ممکن است پیامد‌های مستقیمی بر راه‌یابی او به کاخ سفید داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140712" target="_blank">📅 11:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=JsPvCtTAWLYEUKxSgmNKPg4QyCR7EAgyNA54dNq3FylxQc687hLcPJNRbCv4CuQ1XiHwyaIDCw7Um5Xz2FOCaxPjeIIOPntNSmwAPBJq6H0pWMhXqSN00ds556f970YJoTBnlLw2Yfkw3u_Q7k5mtsb8PIqBCF5je0KXi0G4U4UftavHRd2CmqH2I13kT4G4j566iKe1-IUlqzQkQ1E9HbwvXQCvhvGsbR9EBucAoU5CdKPRizex1PtWOTIxRINuTv09TnfAycv63Il0nj1bEqcXc6VJyOxOUnCF6VE2qJXyL0CVX1DTFyZgr1Iy8DYcBgygnl9bmqNNPl5RBpWeno62Hyf6ykzoAddkqiw-MvlrBdMGvVZSm2-ogPEQCHBE53sQs9xxozkI8Jm0uoG2faq3a558mY0F5kqtOkYqloGrEuFylKjWn6YryHaNHmO3auum1_t6cHMHw2WscwhU06I9uzl5s5c3fzLqxW9uAfdzO2PzDM4vMO9oYjOhJGiCNkbqZZ6qDN8TFkRL5vnDfBVdPqcFC88mQA_2GZs3JRJwn2iQNXzTH0x61usj4StrmklSvYRa-MTv3oMJbvMZZXA0a6KIiTkBJCM4nDhnZWnEdjVEOJ4GadgsYk09aAOt0G8xs8_xEM89Fnd_pq5DBLgxBNJ1XNAA7XP6O3P3g3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=JsPvCtTAWLYEUKxSgmNKPg4QyCR7EAgyNA54dNq3FylxQc687hLcPJNRbCv4CuQ1XiHwyaIDCw7Um5Xz2FOCaxPjeIIOPntNSmwAPBJq6H0pWMhXqSN00ds556f970YJoTBnlLw2Yfkw3u_Q7k5mtsb8PIqBCF5je0KXi0G4U4UftavHRd2CmqH2I13kT4G4j566iKe1-IUlqzQkQ1E9HbwvXQCvhvGsbR9EBucAoU5CdKPRizex1PtWOTIxRINuTv09TnfAycv63Il0nj1bEqcXc6VJyOxOUnCF6VE2qJXyL0CVX1DTFyZgr1Iy8DYcBgygnl9bmqNNPl5RBpWeno62Hyf6ykzoAddkqiw-MvlrBdMGvVZSm2-ogPEQCHBE53sQs9xxozkI8Jm0uoG2faq3a558mY0F5kqtOkYqloGrEuFylKjWn6YryHaNHmO3auum1_t6cHMHw2WscwhU06I9uzl5s5c3fzLqxW9uAfdzO2PzDM4vMO9oYjOhJGiCNkbqZZ6qDN8TFkRL5vnDfBVdPqcFC88mQA_2GZs3JRJwn2iQNXzTH0x61usj4StrmklSvYRa-MTv3oMJbvMZZXA0a6KIiTkBJCM4nDhnZWnEdjVEOJ4GadgsYk09aAOt0G8xs8_xEM89Fnd_pq5DBLgxBNJ1XNAA7XP6O3P3g3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: میهن پرستی واقعی وفاداری کورکورانه به سرزمین نیست بلکه وفاداری به ارزش‌هایی چون آزادی و عدالت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/140711" target="_blank">📅 11:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دبیر ستاد ملی جمعیت: تعداد ولادت‌های ثبت‌شده در سال ۱۴۰۴ به ۸۹۲ هزار و ۲۸۲ مورد رسیده؛ رقمی که نسبت به سال ۱۴۰۳ حدود ۸.۹ درصد کاهش نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140710" target="_blank">📅 11:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzTbyB7nL_yRs2eM46YKU9nr65DDubWAGhCaKm7lRLUOws40Cgf1FAf8lvlEb7QHh4YilTLBAKSRdpZObRLb7rc4KNT5VKKBSkHrlQi0CxqkazjN53fSX_ao49rSzXGaRbQkzvNnHW69OE2QchzTGJxJ__dMMXGdUSWQ8EC9AGCwJYAudKm10Yy_Xo5rlgEhuzW9wZzFr0tOVzKuFacEU0ZtIqdm6eAytc7Nicwu-GLFSDBuspkT649Xbcrgvj32-sZ4wxRT8PS7_CIRhT1U-D8ZknosoQ3t_7RJi0bbGbcMP--J0xc34mGwfI70MCZ1Q2PYJweDYM9mSQVPeCj0xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز:
آمریکا در ایران در حال سوزاندن سلاح است و روسیه و چین به این موضوع توجه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140709" target="_blank">📅 11:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
طبق برخی گزارشات تایید نشده چند نفر از عوامل قتل حمیدرضا رجب زاده بازداشت شده‌اند
🔴
حمیدرضا رجب زاده مدتی قبل ربوده شده بود و به شکل غیرانسانی به قتل رسیده بود و فیلم این جنایت در سطح مجازی پخش شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140708" target="_blank">📅 11:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTdZcutiTXTBOvOKoUW2o2uHXSSjp8HbZj8N1-TAhDDERXOngMzeWcbtXSxoBx5H6n_kN52InXPW6BgyQ0KNNmD7xI432Ao0HjZJgUe0ozJuGwst4lkQUYW-3JEuwBnp65K9paRbpuSrQc8svV1-MImXZy5CEOEBkZB-hOjUN49y9nUef9yiBNIRgCiCkqrEpP3aAP0zpUDCxDY6LMScdJzw0_XrbJMw2IH_wbUacWB3CYE1drNliNYrXzdFDljESclKOkcxWBnaZYNB5xDkt9fTqVp7xLwiHypaLphx3VWuoqWVWZ1jr31kno6IYscir1f_ID99Or-t7obncMd9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طراحی نهایی آیفون ۱۸ پرو مکس و آیفون فولد لو رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140707" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مسمومیت ناشی از مصرف مشروبات الکلی در نیشابور به بستری شدن ۱۲ نفر انجامید که یک نفر از آنها جان باخت؛ ۷ نفر تحت دیالیز قرار گرفتند و چند بیمار نیز برای ادامه درمان به مشهد اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140706" target="_blank">📅 11:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b625cd4f.mp4?token=ZFT0fRp1tJh-1j_FW_kIDrtz15EYAz_iKnXhkhkSbbvoO9nDy2ga5QU-K9f52-LHps2sD2KqeWERmqbow12olxTS11nZORnZirsWW2pedyiZIfoFWn14saR7RnmOdUNWGOo2vEkkB9hTevYCX2a9-BNuYMAI-JpfJAfPZkZAnZvNDPy2N0VtiDao-2SAM5SAXBjFPsoCYSfVnHbxBj4yASPM_fgClw1gYhicYRtlLdnuP7sMvrZIiWIfmndcPcKzbC7L63xZ0NCSqBjYwfqGTRPAMKh_VKhoSsz5RNEkXFlF-HHV8jbLjYNHhQxU9isuG0AfOolWONZbrmJW6AWB2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b625cd4f.mp4?token=ZFT0fRp1tJh-1j_FW_kIDrtz15EYAz_iKnXhkhkSbbvoO9nDy2ga5QU-K9f52-LHps2sD2KqeWERmqbow12olxTS11nZORnZirsWW2pedyiZIfoFWn14saR7RnmOdUNWGOo2vEkkB9hTevYCX2a9-BNuYMAI-JpfJAfPZkZAnZvNDPy2N0VtiDao-2SAM5SAXBjFPsoCYSfVnHbxBj4yASPM_fgClw1gYhicYRtlLdnuP7sMvrZIiWIfmndcPcKzbC7L63xZ0NCSqBjYwfqGTRPAMKh_VKhoSsz5RNEkXFlF-HHV8jbLjYNHhQxU9isuG0AfOolWONZbrmJW6AWB2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آتش سوزی در شهرک صنعتی نصیرآباد در بهارستان در جنوب غرب استان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140705" target="_blank">📅 10:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMi3Iup477nJ5UTRQrY_7HnQlw1tZ-zL1wVRP1h57Go6aU63bM22ZH3K3TOAXxcK5JyyZKBH02YMGax_Ec7gIq9hY0yLzo5cGlbraTNJpTYtbXJN1dzKeoWquw0VJ7Ilh1gYhCzZxayxsqXfCRDxGzD49V1wJDqpeog81yHXK4S0r28OcA-bpCygw0LLhMcYLBGg3ZAlumPVY9eTxI_zISbeX69PE86AaWyuSzflqrtgbB-JJuJTHRrrR2Anm7ABQpWTQ7AYh1NF8dz0_Oqa_TZnucpilZ76EEzBiRA_-vHIB7oydyvo1CPcOOUJinzhHgeFZ48DqOTQBTEaAlOTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=jn9u-rhjqY_w58GyaVxnTf2V21Kno3MGN8KlTtXCKbmGc1C1xVLjLJYfaxLnNgnSlduC-0SzhUkSjsBk3SJx2jo96UPdg3MIClmzPu79Wf-Ldvw4VPfvAJwmAZsjuRPluFKWv1lKK4Xpgnho0H4677LPDobmU9wo6gudcEUacLilwnb-WQ2O6_NQGYBB1IpmDBKPDYE7RsA-m2Opqv8dr_waO6lYPSdPWWY0Bpxy5rPQART7O4eKpnTVtH0xuHWLBN_H5IqBJqcMJQHKDB3LHPKDWKBOjqEYc8YeUfrlcDdSgWnTMRqEuRla8rPWvUgCRcq6Yeh9oNezlBvc_Cob1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=jn9u-rhjqY_w58GyaVxnTf2V21Kno3MGN8KlTtXCKbmGc1C1xVLjLJYfaxLnNgnSlduC-0SzhUkSjsBk3SJx2jo96UPdg3MIClmzPu79Wf-Ldvw4VPfvAJwmAZsjuRPluFKWv1lKK4Xpgnho0H4677LPDobmU9wo6gudcEUacLilwnb-WQ2O6_NQGYBB1IpmDBKPDYE7RsA-m2Opqv8dr_waO6lYPSdPWWY0Bpxy5rPQART7O4eKpnTVtH0xuHWLBN_H5IqBJqcMJQHKDB3LHPKDWKBOjqEYc8YeUfrlcDdSgWnTMRqEuRla8rPWvUgCRcq6Yeh9oNezlBvc_Cob1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اوکراینی دیشب یک پهپاد بزرگ را علیه شهر بلگورود در روسیه پرتاب کردند.
🔴
در نتیجه این حمله، چندین ساختمان مسکونی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140701" target="_blank">📅 10:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی: جنایت‌ها را نه فراموش می‌کنیم نه می‌بخشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140700" target="_blank">📅 10:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نیروهای مسلح یمن: به لطف خدا، پالایشگاه آرامکو در جیزان را با استفاده از یک پهپاد مورد هدف قرار دادیم، در پاسخ به نقض حریم هوایی استان‌های صعده و حجه توسط پهپادهای دشمن سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140699" target="_blank">📅 10:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرمانده مرزبانی آذربایجان‌غربی:
در عملیات‌های یک هفتهٔ اخیر ۳۳ سلاح جنگی و شکاری، تعدادی خشاب و ۱۲۲۹ تیر مهمات کشف و ۱۷ نفر دستگیر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140698" target="_blank">📅 10:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
واشنگتن پست: ایران می‌گوید توافق با عمان قریب‌الوقوع است، اما خواسته‌هایش احتمال باز شدن تنگه هرمز را نامشخص می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140697" target="_blank">📅 10:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آتش‌سوزی در یک واحد صنعتی در شهرک صنعتی نصیرآباد رباط‌کریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/140696" target="_blank">📅 10:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس مرکز امور زنان و خانواده وزارت کشور: تردد بانوان با موتورسیکلت از نظر اقتصادی به‌صرفه‌تر و کم‌هزینه‌تر است.
🔴
از نظر ما، مطالبه زنان و دختران جهت اخذ گواهینامه موتورسیکلت یک خواست اجتماعی قابل تحقق است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140695" target="_blank">📅 10:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی دولت: هنوز درباره افزایش قیمت بنزین جمع‌بندی نشده؛ هر زمان به جمع‌بندی برسیم، حتماً اعلام خواهیم کرد
🔴
بحث‌هایی مطرح شده بود که قرار است تخصیص سهمیه بنزین به صورت عدالت‌محور انجام شود؛ یعنی بر اساس تعداد خانوار‌ها و مواردی از این دست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140694" target="_blank">📅 10:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هاکان فیدان، وزیر خارجه ترکیه: ترکیه ایران را در جریان ائتلاف مکه قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140693" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بنابر یادداشت وزارت دفاع آمریکا که به دست واشنگتن‌پست رسیده است، پنتاگون از صنایع دفاعی این کشور خواسته تولید و تحویل تسلیحات، از جمله مهماتی که ذخایر آن‌ها در جنگ با ایران به‌شدت‌ کاهش یافت را به‌سرعت افزایش دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140692" target="_blank">📅 09:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b837bb520a.mp4?token=e221lNUdwwG23vp47xl8H5Ii7Z2KhjQGSzchRfOZuffb_WvmXsZ77PL8klqQz6f0ahQyf5GElxY7-7Vf5d1cTrPSmrIR7G5VpJlq45-0sQeU8f6n1dECLLqAjB3_JGtgVjD9QPURlx7xdhll_DK7UpY9vBxddAvBRal-REgFNFHc3W0s6XKEMSjKzX0L5Dz0JFr3tZAE5niivpt4Z0n67PjKufP17ck7MFF8DFfygu8xHdzacjxOFn59X9GfIa4ddK0JgQcb6ca45ex2kFirjjDfIFOZZmYbLxMiwdn4G4M-e1MOqSRKK3S1aH56t7eNI5luVrJjdM_S94OTcImXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b837bb520a.mp4?token=e221lNUdwwG23vp47xl8H5Ii7Z2KhjQGSzchRfOZuffb_WvmXsZ77PL8klqQz6f0ahQyf5GElxY7-7Vf5d1cTrPSmrIR7G5VpJlq45-0sQeU8f6n1dECLLqAjB3_JGtgVjD9QPURlx7xdhll_DK7UpY9vBxddAvBRal-REgFNFHc3W0s6XKEMSjKzX0L5Dz0JFr3tZAE5niivpt4Z0n67PjKufP17ck7MFF8DFfygu8xHdzacjxOFn59X9GfIa4ddK0JgQcb6ca45ex2kFirjjDfIFOZZmYbLxMiwdn4G4M-e1MOqSRKK3S1aH56t7eNI5luVrJjdM_S94OTcImXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یک واحد صنعتی در شهرک صنعتی نصیرآباد رباط‌کریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140691" target="_blank">📅 09:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: مذاکرات ایران و عمان درباره تنگه هرمز در آستانه نهایی‌شدن است
🔴
عمانی‌ها پذیرفته‌اند که به‌طور موقت از مسیر جنوبی استفاده نشود
🔴
در حال حاضر دو کشور بر روی مسیر مشخصی که مورد نظر ایران نیز هست و به عنوان مسیر پیشنهادی مطرح شده، تمرکز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140690" target="_blank">📅 09:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: فرماندهان ارشد نظامی امریکا در جلسات خصوصی خود از محدودیت‌های نیروی هوایی، کاهش ذخایر مهمات و خطرات گسترش جنگ [علیه ایران] سخن می‌گویند
🔴
فرماندهی آمریکا به دنبال راه فراری است که بتواند پیروزی نمادینی برای ترامپ به ارمغان آورد، بدون اینکه در را به روی درگیری گسترده‌تر باز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140689" target="_blank">📅 09:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p561yc557LHrqxnaSEhCw7aOXuvR5-6107xHT5UCGMR5q6Swp4jtMsxppliWXnmPPcyZlWrP64qjlFD9kOPjnJbwXgw2hPXd8SOT6Qnq6FhX8DyWgDw38Mk6oP6UYt6GXoK3wv_ceinat-IjBnx-ngPqx0w2sHjS-3gl5s47UlwmLfVuKm_SbJU2BLhYPLXz-YoGoDe64LBAeoTQ7WaHeJuEgODRvJkpEeHH89oDSk4KJ3XX8ZXAv_QccwoRKDMGm6uBxH8DNJQPSaPhj3t2BXnctwEQQwmWV3RTkSLcjLzHig5GihlMMrOG-5VIr04nNPEkqfh33aj4AiTMYIF_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وکیل سابق ترامپ با رأی شکننده سنا دادستان کل آمریکا شد
🔴
سنای آمریکا با رأی نزدیک ۵۰ به ۴۹، تاد بلانش، وکیل شخصی سابق دونالد ترامپ، را به عنوان دادستان کل آمریکا تأیید کرد.
🔴
بلانش پیش از این نیز به‌صورت موقت ریاست وزارت دادگستری را بر عهده داشت و نامزدی او برای چند هفته در سنا بلاتکلیف مانده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140688" target="_blank">📅 09:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFI-_R4vriZU8GwyiL2nQEqB_FBZFKERyZSr3fQObgM6JxuMOby5mI6GYoEjxKJ4VjEwtGhzEFaXAHYbDKLnRysigoSaEXp0C1WQnOAqvNy964EtpRICkerTorINZ72IcoRyQsV-xmQ3tPtmy3wZP58gRD11Z14Mcb6EW1HDOlG1ODrjNwscDzgZlQVfht28CyxkO6uOtL2V-MNFiTfcep5ThEicL95BhEnJGMJ8XvZEY47QE6p4X2dgHICDBEcZPdItvBQN-NvQVl-RASvcsXmv0Y_aixgCqK-vB7KMfhBJGnIjj3jR2kk_x0fTVcDeKaDUlADw6BjIHcT1NOLL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1VJOaI_ZVVpcstCBHXJqlGEhkKcpM-JzeVGQyod4EJTiEFHWLInOBDIPLz7EsTI47TF2auVTjfQ0WTT2Ib4hJi6lujdqtP24d_91u0bBVHW-bB6VaAqr-nhQG8n-Z8Itp01WDuyTsZgKlyxSTCR8oWyu-Id7_DfikpVHJjhwF5RamvoJEQ5vEvSBCLTE-KTOAqDC0f8xuvzzml-CKx71LllLuP-gP_wP-d3LhwJIMNpy-ee8zCgLMrS3v_gIFQf5r_0zF4poPdgsq8E22kIwg8qlNNQKdGDKX_ZKaNYZCHO_1zSUxsHCu6yQxAQ1DiHj73rYXo3JpmqCmknaqURxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تانکرترکرز: حداقل ۵۶ نفتکش، در حال جابه‌جایی نفت کشورهای عربی از مسیر عمانی هستند تا جریان صادرات نفت از تنگه هرمز را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140686" target="_blank">📅 08:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت انرژی عربستان اعلام کرد:
شرکت آرامکو آتش‌سوزی رخ‌داده در یکی از تأسیسات پالایشگاهی خود در منطقه جازان را مهار کرده است.
🔴
در این حادثه هیچ مصدومی گزارش نشده و مقام‌های مسئول در حال انجام اقدامات و بررسی‌های لازم برای رسیدگی به این حادثه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140685" target="_blank">📅 08:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921bf906d6.mp4?token=Z0ywyS4057YfJbzzt4IJRRaDdf7O-TIEEshto9_a0phnnSTwEFsXOP8tH2jb0VWoVmTdJAWgnc1_7iP9eWW_k810JxLaXh8TXMmL9ygBS2FDFBQaUC2hVVjVM7PuzTXQaezSARHHBvPYsoqlVPVXoIbFNSIDbdFLA1skOzPcSJGsE_ZCwqv3WwWzh1pOulzbHFfebaCX4MTaJIsgEb9tPqdRL5pZHUGkzpH03T7Ai9VVtcigKHTc3o8Ub2NEam_LpLb__a32LpfSZYOXfA-YRloQry7a953MptAL6EvfT99rV2pP22e5cyd2-s5dR_7eMgow5r28J2wHFDZf9R4T_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921bf906d6.mp4?token=Z0ywyS4057YfJbzzt4IJRRaDdf7O-TIEEshto9_a0phnnSTwEFsXOP8tH2jb0VWoVmTdJAWgnc1_7iP9eWW_k810JxLaXh8TXMmL9ygBS2FDFBQaUC2hVVjVM7PuzTXQaezSARHHBvPYsoqlVPVXoIbFNSIDbdFLA1skOzPcSJGsE_ZCwqv3WwWzh1pOulzbHFfebaCX4MTaJIsgEb9tPqdRL5pZHUGkzpH03T7Ai9VVtcigKHTc3o8Ub2NEam_LpLb__a32LpfSZYOXfA-YRloQry7a953MptAL6EvfT99rV2pP22e5cyd2-s5dR_7eMgow5r28J2wHFDZf9R4T_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر عجیب وایرال شده از یکی از پارک‌های تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/140684" target="_blank">📅 08:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc_9qBOsth2uWIwrl-xiYGK9UWffL0BMQ4vlCukD65cnK4nfKX_I-GRj1BqonTZXvQ28Mhrh7W1lmtIpMHMbVfw9Nf5W-z9hKgllxWzGX4xRS-C4eDZXR8CD1W45dB7-GZbQvLwBkRgex4Nqda8A2Y00VVDZ6E4LGaLbW09ppS6p98zEu9D_qxDKj_qeJp7KmzHU90TuMEYdcckM88JD0Z1dI8a7PEZFDgf-VyofFuIqwpz8pr5ao2ibvG-BVIpfP64eCklk1ByaH4CJUZ1Dm403gf8y8_q6pyRNxFftfd_Oj9D7OxkjwUOV507UykpQE6zKmksPCIpMeK3zqDkxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: ایران می‌گوید توافق با عمان قریب‌الوقوع است، اما خواسته‌هایش احتمال باز شدن تنگه هرمز را نامشخص می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140683" target="_blank">📅 08:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3ce61d0b.mp4?token=NcQYe_4zqlZ2vrDxrAKxD7OYgdIa0qBb29QODtRe56d4kcf9IxlJDt27B2bmS9iJUl42aApXY6kAY_dA5335AtjJnyLGtLzbxPcglNe3pxeUixJ2cm7y8zrXn26rYE_3vtkqCH-mFwfC4bYagZNRxqoCWsKE0X8QttUN53rMRpj_8pWP7P0We0GHUozh3ee4In04ht94ojKQYw2h6-1CGDyVZ50B2zvGKalZeVcMJ4e4YkL2oSm8JfQaoXuataHITz2VDe64OJiXBh1aeKaumIZhTpZ3BrsubwLlE2qZ50Yb-TgdsPgbU-tmrhuaSZulqcQInrtT76Q3D5wIUjO7CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3ce61d0b.mp4?token=NcQYe_4zqlZ2vrDxrAKxD7OYgdIa0qBb29QODtRe56d4kcf9IxlJDt27B2bmS9iJUl42aApXY6kAY_dA5335AtjJnyLGtLzbxPcglNe3pxeUixJ2cm7y8zrXn26rYE_3vtkqCH-mFwfC4bYagZNRxqoCWsKE0X8QttUN53rMRpj_8pWP7P0We0GHUozh3ee4In04ht94ojKQYw2h6-1CGDyVZ50B2zvGKalZeVcMJ4e4YkL2oSm8JfQaoXuataHITz2VDe64OJiXBh1aeKaumIZhTpZ3BrsubwLlE2qZ50Yb-TgdsPgbU-tmrhuaSZulqcQInrtT76Q3D5wIUjO7CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این پسر سوت پلاستیکی رو قورت داده، بعد بردنش دکتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/140682" target="_blank">📅 08:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
طبق گفته بعضی رسانه ها یک پسر جوون برای مراسم ختم آیت الله خامنه‌ای از آلمان اومد ایران،ولی موقع برگشتن نذاشتن برگرده،چون کارت پایان خدمت سربازی نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/140681" target="_blank">📅 08:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lWU_uV1mfrApz2ITJCgmtCd2ybpKxpnSrIYLB9z_jwlFn4tCgkwnI0BX6yWbmEno8RsdZvWELTikMPloInPss6tGfpqFOjHT40SAJllSTiBrjzHqpT1GdhC6STjP1wWWk9x4RVdvcEpTHaiuesY84Eb5wNRVeKOKXIuHYxDzKuO3N9TdY3VH-4eSBayGikpCS6ORABjsHfU7g39BpQ2kV7kPqLNZrfRHQBb_nUY7fb4vt2WZ64_1tgeS0YkO-A3O8nqdn9oXonXyKHzik2AcsdcMQ-ixwZYi0GhKXlmb3qJL-l6C50mBR21pq5eczTbnAgzzk2y12buGrFWHwBRDAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lWU_uV1mfrApz2ITJCgmtCd2ybpKxpnSrIYLB9z_jwlFn4tCgkwnI0BX6yWbmEno8RsdZvWELTikMPloInPss6tGfpqFOjHT40SAJllSTiBrjzHqpT1GdhC6STjP1wWWk9x4RVdvcEpTHaiuesY84Eb5wNRVeKOKXIuHYxDzKuO3N9TdY3VH-4eSBayGikpCS6ORABjsHfU7g39BpQ2kV7kPqLNZrfRHQBb_nUY7fb4vt2WZ64_1tgeS0YkO-A3O8nqdn9oXonXyKHzik2AcsdcMQ-ixwZYi0GhKXlmb3qJL-l6C50mBR21pq5eczTbnAgzzk2y12buGrFWHwBRDAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/140680" target="_blank">📅 07:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GB_fBXixQxtYKw-OsfrEzqbxkp7Ad5_Qe__1842zmXX8SHHwECyxqLB5IqlP0R_hIiGmprJEaIpqhupp4rjYdwbv2krbPKF1lBwii_XQnl4aOZfl63jDUsUFeuzDpVwP-Mr5kmYfuyKc7fU03wJTrlXr1H9R3EucV9dSjUjYSKVTIl15MBgi_fGDtL0BYgI3P3k_8V_sK1nbIhOJJot5AKzRTJ3oX4xPFbOIVXfMzcpJ92Lwem5nNJQn6s7UdvPY1SGYNCvfX_ZWmwfCRSF0Sg5e7dKU4Bm65TascD5a2RXuWR9YGegnWdvWrzj9QqghMCCiD8wmenF9Nw9iILF7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T3yQ40a0oHIMiOThljGqnkavyALLji_BV75qE5n-DxWiPtOAaXLKuOFpHAAVf1cs5GBdi52mneCg_tO_gOLGiN-jCd4QmTQt6Sx1c37j46ZZWDR25xPJaD32eVe-OHa9hdZrq2aPsYBEy1QDMlY1Vo5vx7K49-rREe822F6GTi0jlVBRlz8PaakyXX8PVYk9-Bjqgi5ltB30zg9z-Yvd1tDKsZ-ToR4MMkI4-ep6fEuRBko7OTL30-GaXp5_8fgcj08NnwTqbyPg9TLkrOMwu2afHKPwNCGjsRUBmj1zPKdbtANc2---AYo0LDTls61R2m_bscEcB7g3bQHaPwNALA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر عجیب از بندر شهید رجایی  که بزرگترین بندر ایران است اما به دلیل محاصره خالی خالی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/140678" target="_blank">📅 07:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
⭕️
قیمت طلا و دلار هم اکنون !!!   سایت دلار و طلای تهران@nerkhBroz  داره لحظه ای قیمت میزنه
👇
👇
@nerkhBroz  معتبرترین نرخ طلا ابشده
☝️</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/140677" target="_blank">📅 01:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
قیمت طلا و دلار هم اکنون !!!
سایت دلار و طلای تهران
@nerkhBroz
داره لحظه ای قیمت میزنه
👇
👇
@nerkhBroz
معتبرترین نرخ طلا ابشده
☝️</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/140676" target="_blank">📅 01:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
به مناسبت روز خبرنگار برای خبرنگاران  ۲۰۰ گیگ اینترنت رایگان فعال کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/140675" target="_blank">📅 01:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
‏سنتکام: اجازه دادیم حدود ۳۰ کشتی از منطقه تحت تحریم عبور کنند تا کمک‌های بشردوستانه به ايران منتقل بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/140674" target="_blank">📅 01:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf3aa5132.mp4?token=Wo9IiVKdECP_RSjbB1mrzKBakjwFOiL4b9I225fXDuJtNY4FRpunoQAqgqnkNmkiVyT2_lOdRP4uKgfQ6IEIYX_BN_-NhqVX0rKnCkarm7NUgAwR-T0OsvbWBZEZkjN8Y9kLvriIYFby_vM4zFQV_6z4ZTD30eiA8Fen_FHxDO-iw1CbH1a_jxtTn9tR4ia_RVEaXN3KaD68FDGZoj7yxk0Cr-5EmxS-XqvA8tiRlrJbtjDEoya5ZrslTT5U6DqoEM5hY9Ibtn9bqnIti6dsyw2RBMEDu_-yqaasxuTSgUF1cPSCodc_vPSlyr7EVaDDlksDUYWTfjB4PwoM2NupTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf3aa5132.mp4?token=Wo9IiVKdECP_RSjbB1mrzKBakjwFOiL4b9I225fXDuJtNY4FRpunoQAqgqnkNmkiVyT2_lOdRP4uKgfQ6IEIYX_BN_-NhqVX0rKnCkarm7NUgAwR-T0OsvbWBZEZkjN8Y9kLvriIYFby_vM4zFQV_6z4ZTD30eiA8Fen_FHxDO-iw1CbH1a_jxtTn9tR4ia_RVEaXN3KaD68FDGZoj7yxk0Cr-5EmxS-XqvA8tiRlrJbtjDEoya5ZrslTT5U6DqoEM5hY9Ibtn9bqnIti6dsyw2RBMEDu_-yqaasxuTSgUF1cPSCodc_vPSlyr7EVaDDlksDUYWTfjB4PwoM2NupTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریاض برای جشن توافق دفاعی جدید مکه
🔴
خیابون‌ها و ساختمون‌های مهمش رو با پرچم‌های عربستان، پاکستان و ترکیه، نورپردازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/140673" target="_blank">📅 01:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌پست: ترامپ ممکن است حمله به ورودی‌های «کوه کلنگ» (Pickaxe Mountain) را برای جلوگیری از راه‌اندازی مجدد برنامه تسلیحات هسته‌ای ایران بررسی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/140672" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b213e05880.mp4?token=XqZxrwTB-PTeja7af39bfdrham-_ZTOAsjM4HjPXwNqhE2wIqO3SHgLILKX1C6_73Rtt2K8-9OYEMBA_IF3tAsyTdy2Z8QDIvjXgs1lL42LxTa7q8fjw3yILG8Uzbt8keFrp-Vngr_Cw1gf6jEu-ZVdj94_2BXkq-lNOt3EvpxWPVxiedcTBVeCSmCYxIQAGbyPk2kkKNogR1b25jINjwFgStPmfDuWxshpWUUtcO7ji-Cmd8DbOqQBdd0dBZQrO9tsG4TZyDOwCzjqENnZUht6-5mgzhSoxDmNPgYbjclohVVJ1eOY8aJEsJZKe8YD39vaQK7P2L3rdH-BG3diRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b213e05880.mp4?token=XqZxrwTB-PTeja7af39bfdrham-_ZTOAsjM4HjPXwNqhE2wIqO3SHgLILKX1C6_73Rtt2K8-9OYEMBA_IF3tAsyTdy2Z8QDIvjXgs1lL42LxTa7q8fjw3yILG8Uzbt8keFrp-Vngr_Cw1gf6jEu-ZVdj94_2BXkq-lNOt3EvpxWPVxiedcTBVeCSmCYxIQAGbyPk2kkKNogR1b25jINjwFgStPmfDuWxshpWUUtcO7ji-Cmd8DbOqQBdd0dBZQrO9tsG4TZyDOwCzjqENnZUht6-5mgzhSoxDmNPgYbjclohVVJ1eOY8aJEsJZKe8YD39vaQK7P2L3rdH-BG3diRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیوی ناراحت کننده از پدری پایدارچی که موهای دخترشو بخاطر حجاب نداشتن کچل می‌کنه خیلی وایرال شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/140671" target="_blank">📅 00:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / شلیک موشک بالستیک توسط حوثی‌ها به سمت مواضع دولت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/140670" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سی‌ان‌ان: بعید است تردد کشتی‌ها در تنگه هرمز به سطح قبل از جنگ برگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/140669" target="_blank">📅 00:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: یک تیم باید تشکیل می‌شد تا نقض تفاهم‌نامه را بررسی و حل کند نه این که دعوا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/140668" target="_blank">📅 23:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل درباره ایران: از دیدگاه ما، بهتر است که هیچ توافقی وجود نداشته باشد
🔴
به نظر من، از دیدگاه ما، بهتر است که هیچ توافقی وجود نداشته باشد. ما می‌توانیم به اعمال فشار بر ایران ادامه دهیم.
🔴
و من به شما می‌گویم: با کمک خدا، طی دو یا سه سال آینده، رژیم حاکم در ایران سقوط خواهد کرد.
🔴
به یاد داشته باشید که این ماجرا از کجا شروع شد—ما اطمینان حاصل کردیم که تمام بذرهایی را بکاریم که به سقوط این رژیم منجر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/140667" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvis7Q0XkHKy933z_rl9NkAJoIo2LYCWM-zCyV3eczR308Sdjnrn_kPpev8G1Y49OY1zQ-T_cccIsaxy6qzi4-N-ldgYLca6aDwyxpqYytEo9qVqIwV06P-FcFiR9o1bus8Zx_ETyRynEa3ehxqqXjmXE8-fb1Y9JsR3_lxuwci-I7Ay_H6RC7bNIa4eRdnP_G9eYYHtWg0bnZVni7xp_Wm1eTYyhe6V5cMI_YnhGDaAVZCJAJD2Z1c1HxtluHFK6l6SEG5-BR6aV7eVA3vioOoSDW5ngO3mZ9AMS6EG4rhAv1mB4je3S7LYPzUHhWxqTK8MH6iuaMi665trDczEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز مدعی شد همین حالا ۵۶ نفتکش در تاریکی دیجیتال در کریدور عمانی تنگه هرمز فعالیت می‌کنند و جریان نفت کشورهای عربی را زنده نگه داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/140666" target="_blank">📅 23:43 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
