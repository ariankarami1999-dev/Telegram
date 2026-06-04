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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 175K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI5vC0zcRhMAnsxHcqvlrO3_2codGMWwNKMqBSmKomy2ote9pSxxlLHTMDuoW-pQZmiO0saogGu4dU8_O_q9Gincki02rMtoYx4bDpYa9gXPD2ecnlSnZ5QdolNkd7TfPg9uWecvDDANE2K0OpsE5Uyw3-3QhK8bVEN0_UGvwA2cMwBsPjfkcP4qPoKQ5xlCF7w9ZYOmkgeEQcABZ8qybxj8OwDNTTP_cZwMGDFC_ymKh-WlqM6HDP9VLpai66Uz6VG5q7T-1RpUQJXKarvixGhkLcDzMvtA8pWFk0t3Zh8Dnya3Inidb8oS5nKVjnAuKUpxxG3T6nPEn9sPTNcw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etwe8mqwMf5FRXkAeU2N1wIlWHFGfdNE4sJXz69Sn9ubIqo2_h0DA_eCjINIqNuDUL1Eo6L_qhkdDlfBLbisbOA2FQIZvup0-fHSjuFA4H9jJvAK3kmpDwm98pegXohD3U_cVa5J1p7mHfZnbn4guApqPCKxz9keECOAarZ2t3VcO5naksex6K077Js2MZc4jpR8T1ByLuec3WxUjAI7av_BwTZr7OF2OcQUEmhCwODIZtn265DKPidWOnlMZVGkP5Rfa9BUhe6WYp3E0rfPH_L4Kx0CKKPf6fTROkpJTMeLATku0hLbgi4XCgf8FGRXd1d8hl-2nycmM9J3cEV5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq_yUa7D6ejNJxOLsZy1JbpayxQ-amh3xGMJ0-tfsZoc3vzl5YcVZgSu13rpZK6PEt2LJOf7gO2Cp70j6--nH6mD8QTzYJBhOVOynHOeU7bffMIl_seF5rC_obEWfF6rw04CZGyKSVWouXDmoJ3kNR-st9q5Jxl63v6yphsndGlLtoP8RxiQsenVuSxlzHbJQJ_x-EgUHqkF1lpNXlXRyjwCDI543y0hFSdnxrUlytQQ_-dwiiSBHJLUyF6mIyrpCXx4YZLJfkIi71-3OL1s3xbNyQVke7LZd6jpXdMHz2vbPCFRM2i08g0QugEF6gdbTfHwniuFRlA6XsSpanVKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=MMgGB1Yr9QBmfr1siEL4Ep9TYYEVWokNKzT87H0gDt5A617N5wPYbxYUQConXP3pYbQ7O3TKqMUCPZhP3WgRsQEzAN6T9ALALolPKcNGNyurXAuTiEZvMxYZjKzdCZZj6naar9Kr9OJk5hq1UkX_S-dqVItHxuFk6EwfGSinjW6bc5ozJdxRV0_LFmHOxjpz3f0ciKzxYEYI08sxcB4waHq2rleAWhn_lcEJoRlZH2Aw2dUo1uZUuMzQuOoB9VAwgmro0_Ma4FZxoqXi4vEkHsyzLnhm-jPgTyjyEPjFxxYfGfQTfhYT20tyFyxLLudG2-h-s4yTa4G7FT1sZKttTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPmef1jUSRjPyHA_1hV5fMV2h-GPEM3jR9IsqYbpQmsTfehzPh3VSPfQEANLSWaDAU9oa6FnnsaJtnPR4mCPXY-pN4Z6WBDZTF8_zb-DhgsB96WKTSm-KPjiLSlL1pL7RSWXzWsUu8iUdPKQYscCqPOPMu85LV2O5ThfU30DUIRotekUjTC93OWN9PfoLT061mFP4T14n8uSikpBbVLhusiqVUw16x7vskRJQ2ZFdSfd6gA0WSIE_ghhJsNr9QRLj4njCtvftw-hmPxMa_Mn4Q6SPNSOvXY2P-PolWlsWCfxDi4auCTH7BNupwrIyno3SdM5TAZ4jpFiE36N-VROOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEZ2M-IASZew-09f32TUsx0QZlU-HMRLFyx1NuBEQPdtXWyy8zEmVEPCUXq1Zkl3MtpLMidl0ge0Xw77ostbkh6aNNJC5ThjhYx7Dd6li_9BGjHeovNU9xEGHt5yB2DztvMZrfN4nZLTyyRGEK_vOLJR0lQ2qoQ53S2XsuYNKa2K6-hm9I3SehyZnFGBLQ21kGtbQppksYcw7AuzOCiDPnBj3cxH8MTqckcik4e5jABIVlSuz5_186Uxvqm23kLnFEhfJJIHP9R6G-SSI15Oo7GKBS9Xd0h-0hqj0eOk8FQE7Pb_o-p9HD1moj7RHSuihUGvnZhSxxaezvYkdxQvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLVL_SyEPoFNLgH15YZkLkkGYtSIhyVK4LanIYau2qA5k6rIsx2dDTEBYWVteLXifJ398XBGVxtgvBX3GowHcXLeWxpQrp_aleicF5dPdDMoZYFj5h3RVqlXVgtKcW3TXR_vR8NQLVccwAemHkd0KOmpetsnhbIwe8Uuy7RFK1gIgoK_Fj6WhseDG-sm0Ang8yyEE8n7B0tU4KKQskvKdz2rWB5hgu2FkmCDF2kt6w3ufnx-Z6yXpw1aafHNF69bn87fR-ea24G3VyrInEFEbQWMRpGivfNt84NOS6Z_sSesKMGbB6NC1RrdNNKyc3rAnkq9snuScRQT9M5xAnmeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=op4qT547l2shPakDBoHLtRbTn_63ncEfZeAT6E8df1t2DeZbyh5pVQmn0d_IZjn1DzSA0j50ZSopkOcoJV0AtCj9vK7uEjs80yPOrqxclGCQC9-bp-DShExdcS7MI0ohJfQEb0Ku8WcyyMDqg9kHXzPtgvJW5i6bLtO9syxjaydFWF0uneZ_gx6ke9yPelqqrpvikWVgWHEzyWPJsjEcwO6cijnsRit1OJWQL_q5xi502hjzG8-a8-tP3hhtDsgdKZDVK0l2D2xHNBwNupPIO2-qJIPV3go96QAN4QGUvZyjcSiOKJcic1Y_gDoiLAuvxVm91wOFkAoQcMijhLcriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=op4qT547l2shPakDBoHLtRbTn_63ncEfZeAT6E8df1t2DeZbyh5pVQmn0d_IZjn1DzSA0j50ZSopkOcoJV0AtCj9vK7uEjs80yPOrqxclGCQC9-bp-DShExdcS7MI0ohJfQEb0Ku8WcyyMDqg9kHXzPtgvJW5i6bLtO9syxjaydFWF0uneZ_gx6ke9yPelqqrpvikWVgWHEzyWPJsjEcwO6cijnsRit1OJWQL_q5xi502hjzG8-a8-tP3hhtDsgdKZDVK0l2D2xHNBwNupPIO2-qJIPV3go96QAN4QGUvZyjcSiOKJcic1Y_gDoiLAuvxVm91wOFkAoQcMijhLcriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYuO2L-BeZWs2T0lY4eyU49bWopc8zDMdDwL31Uiokyu3-n-XsZyKQxrWebZu7TN-gk4tjSyowElh_uvHz230F82x7xBk3WIS_CjBvX0FXA9RAYDbhvU0toGCkX4YJbxeD1Q1K9wjt7LYpf4OP_DLO9iVnt0_vArQYmg3VDPbqqsj02hznQrVzu9kqd6aJOUw_o4WO-xxL2UISOaVJN4B3A4cY3j5hJKoAgTZaB1yob9CQr_qoy-bOdXgv1ixmMaBan7Qk6kAnBmX9H0LJ433tmJH4S7EiFX5e972Pf7bc9P07RX8ZYdSpU3fcu60G89ulvhqioyw6jRn7pbosAQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF8kNm754rXiNs1QK0quCTA4S1dQPeElj4KxFLtAmuFl2hOFsDPD4w_eFcxqBHUVjw_Wp96iY4vnm2hV4_u5eagDeC_Gi1_SenT5y0Kz_3DKwS4Th9UAWEVed-EDONehg2eUj-5SrUZX8kDkAHE-R69TY0lN3VjzeGUNgAJS_hXeicgtlE1A_-PVK0vxuc-eMAjUgRX3TgtkbT7gYfl2rAVdQEkOwLzK0HnleWNHHPwajlNQWiOA2gcbpDPtm-waO7BCdtOX1AEYRvy9LP9FnoZv8K64W0T0Yg37KZ0NvkjiJeeNQaUPPMxWQ3N2eFvo0CwGpQOalkhinBZa0kSyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcR-Q8MXuC2mAkmqnbb-Ww3Lr9lcvvvw2l9UDOA8MDlk132C15zpvaYRZ2HtCIrkQjznKxkbf6EWJPa5NFe7LZp-vIdGlL2_yNzvPGMUSq9JgSQTwVjZqV3KsdnvW12M6j7ljt8IPODYZHuW_RV_itEPrQLadR0-JYrsrPIaaf4Razg8gNCUGyeEcJtq-WXDnNUMa8zqcckigX0d-Qjv_PCt4igTW7wHWentFgAa9SqruuGQWDg0bg9n3IGuBipJumwO1_K1h3T3qoPXk8oTyLO1eHeUTNXc21P1760NKZ3DR6jqLi18SW9cPodUQ5OUTw36X8ezbAcqZtZOyQOCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR-t5_rs7NOYy0Xh0sYI4xFzEP9E4F57DDWFWNoLFB_go2z8L00lwnuWkVxj0bZbT3QfVZLBG_7bqqd7hSFEwQrpkezZyvmCQNO0sS2XEbyBh9Uce36xdRwAL-FNh_sYsgG21aoUTJl79iRxMbn_d-MvpKahfjaUYH0gWi18nMf_BfKodHg86FACSZrOFia1h0iyU98e-E1tiOqn9_lLZlQl5o1Iu4h99N3vFTX6hv7wlTOcuLEcnZ4eGtFTRzHGjoAs_-qiq-lNVNGHFHQGryaYf7_RsJKk7JQVFcBmRqGGdsQqexUWpfPWqkksfPHvlU-lkho4PxbzPp-6fWXbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQC_U9WD-VIGuFyG5tazb5DElHVIk5a2wZWs4nkbOITxXP2ftvr92jrwyhyzYDTqooiUoXgyOt97dIJFXc5zgAQ1NqJzw2YKfSsMZALVWTYPiZlc6uRLPhWAr2iwu0jVeZ9OcH3s6mT5-TyXDlZecQx0daH9T88zGg_J9jYow8s61zURTrguhJ4zcl-E7HRxXseizS4QVtjVTww2kapRnP0IHIz9ioc6jnokdYfRG5nLsZdpAplZ2hdCKABuGyYufKMOVv4Sg3H30gfIIcOcQzfHpCeEr6eROygxvLYi5GCSqmreTLjqrFKoLlzh2fPATGbH-CZt58UU87_w7SeI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYSzinCQFlYh4886qNz7QwyZMRpfiDVNrLQg-B_cw54od36Bl59sZ9ycNIKoRxJeFDjZk17Kpt45WkaSO3P7oWLz7w2qqT58Np5skL0Zxr5uBxbx0TGmH29OKXElZ52ibXeBQYuskGmmmNgc_bFyHQ_JlubE35LyFHFzeG0ubwX0HcVs93AftaXQ9uMgLzFMTZ7YQXJSI3gWNUHVjUkd72_uZODDde2P4te6X0yNelp6vZbxRMUboe-gFKljGg73MVgZN2wUvjSJqZcfcijaKhVnbhrk4Zwg1ZuRGTeeOODjejFYqoWkrCXdHdKhxb6_hhVfV2-6LcNowIT8MOwi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMG4qBvKc49199hfzY1IbmfMcXqPe3MLCaXeFhODXR-CtyIz_UGcHzJs7uRy8oeUMNW3dwblR-nliamfG6STEHoiyXgdVN7wkUZCPzEqivlM4wfgJXkg1EP93ReR_hURFPAwqnAnmYStFQ7ZBKo-V9p7mokwf_0qIlpiKQuMpn_vcwE383EKeHOcZ-fCSuYHqprWEJPe2pfXw8oywwKD0mkQOnufJPBOocGxV-uIkMaSXDp9dZyyiSDeOYDqb1dhrtfCUIK7lTiZAO1sHy4mqH9O4jubea_gW5SPkFPiE5pQxON19ZQqJJI5yDaQfCPLrB8dSIQe_yc02OBCPth3SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=WDKyhWrHclb0VAkIcOnDEiWMvbsWawnxgeoVvK4SX8pqxkHpqP9UTA3FEVpDq39Mh-_m6kpfRLf1X2sCHniSrULNzQh37CJwmHi3Iz2FxqU0VbeG0qnrLdVHSD_MeBM4CBZ2ZzExuaNeOpSeeFhWtWAHgZWYbFgA2cj-ldeGTNAUsHPjbk8XjTOxQTIGEA1JdRltggX49peVJrXmIxP7RyivCN_yMik5MWH9gE8DCBFKlu4ObF4SysHqV1688LWTo0ET13cZSTlgcwqnz07tTRD0FOissaxBB95k9_ZfgVuvc_ryoSWwMQamrFuc7wq19pQu9IEZEVp1ZYFc6Qqz6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=WDKyhWrHclb0VAkIcOnDEiWMvbsWawnxgeoVvK4SX8pqxkHpqP9UTA3FEVpDq39Mh-_m6kpfRLf1X2sCHniSrULNzQh37CJwmHi3Iz2FxqU0VbeG0qnrLdVHSD_MeBM4CBZ2ZzExuaNeOpSeeFhWtWAHgZWYbFgA2cj-ldeGTNAUsHPjbk8XjTOxQTIGEA1JdRltggX49peVJrXmIxP7RyivCN_yMik5MWH9gE8DCBFKlu4ObF4SysHqV1688LWTo0ET13cZSTlgcwqnz07tTRD0FOissaxBB95k9_ZfgVuvc_ryoSWwMQamrFuc7wq19pQu9IEZEVp1ZYFc6Qqz6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbR7vC-96L4GaFPKD7njr-lHrD7cplek1oNP8qSytfQ-4rLXVp2766vInjuc-xznOAqvO7ehjYzi5eTOJGFe2zaRdgkGke3KdtQsu6z4lPFkc9DOeMcytf6AP5BSqo44wZ9xfvRkiWCLv3F_2zdr0_rHNSPJ4aQAHDQAf6c4GgY2h1LVKa842stlcXCgggoxGScDBY8_zsEjjh9_d8ek113rkUtwzXou94CnhiSjjdzb8njoJ-BMXpXXBvJcXnaLv8-oZWUR6LgF6hqWqOyIH5_79QJjzus3JAHQsX3GAg_sJT7H5oZ1rDR3XvC9iTT7Eo7QBm3Y5_IZ0Q53GR7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoykqZrWzb6lKz8Jnka4ZDglPFtFRzvlqdTzybpwO6mFK82TOry8ZExtwB4Ox6hsN8wDTFy0cX2rnVUVGxTq8VxJS3gaf6eqz8z1IXCGi2UORKcrPpdb2AiusnEdAC1-4Sg3SyzIdy2LFPas6ZaG049HpZELjElsn7s69_4BztQ-EcfSptKyQRSDlFbla75_oNM1Y2gCeTTVgtsdqabPUw2mrHqOezbnEEtrvq07vESTCcGklsByVmedthY7rIMo9z5EBjaTAXvDmE5f_ge37mes5mmwz7ZgiYm7r5CYd7md68josVhmHa1h5Tg-syDOYBQLKVfYI9cJgx8sDlh2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaEr0WJBGKGOo9fknuongQ7uWE7J7L3lknXbWJOFrkzBpfPmPL1xKBgsS-21QcShvEfAq-pZPBZxafn0Lmz6dkNf-6y7_qT3QUA7X_tO_zPIDZFRtA_bUXQF_0zMQGPI8Aj4oOg4nCaJNE9EIIgpMggboLUOp02qnXQ3kINll_DIlu-i9VCZT0oHFVCfrU94xRp-IKkGLw6iioZiDf8MsK-XxwYIcLyx_GQXaLd8qrsmErslDFs-vWvTo_l8tKyoTpRBFRGYqxZ1TLqcwa7gnaqcqHZcGe5qPlFZoj-zVK1K4sEKHDqfs7v0WoeAu-5S4ECmcI3Z8XF7J0PBago0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGUbzYKohhqZ8AI681JtGU30TtODqwDdsY_--OLX5j-QbTPVtXrO0D9PeKWN9KgcbKFLzNteuADd1yomEyCqAWRZ6s0q7fH5VhDnU2DJsc8LbLsxXLVasXHxQNyaF4DmMzIm31NijGXI_kTF679fVglRy_HgEbkfeAreWGU2fwRbU27mDyvTTp0FISHWOpNrDl0tUsXYiiFZGXUy3xZ7LVXHQZLPudVzsE6rquQEMAZx8mwxbB7EOK7cHtS5KJNIixmVY5xsdMDo5zu2SNN1aeTe2mGp9CqRwZ1NCcKtFIFhrIff7osJx8IpvBCFgLnrKFzSpAIcG5j-qis7e2ponQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDgKXmO_XuJ97NWPXvTx0Erg4wlQeEkFqYKGBeoZ6sLinLclAJw4JKuyiVKuxiLDrH92mmaau2zVGmHPYlI_McbkJQthCMov-vA7nTnE-JE1SXrWru1fDz30RhQ5vAlqmYaWWves8o929LJWo1KpDBje7uwJsxHmRzUDiUI_bvHIcYA4ahp-6lHTZ3CfGjQWObjeNNpT7I5tHiDZ4gEZqcdKVj_YPrTEtn47k0_HakuI0eP3BjSdWKBV7gJqXpw1p7CUtl4Xa7Al8vvu427Axf_5r3AT_TpZGtJz6g5v_XzakIrOpG6gXwTkV3HqczJnd9H_GrTQtZkpzm6iIVmxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAt33RujyxzBVJtpp19lhwx-nsDw-XKbKLUeHv2oOEipu0WwC3Avz2r6fy5FaVBPddjs3eNsXK-G0-2fePZy2_rLftd8i6LUd3Hx2gRL27U1tOWW7-vQBoLs-M0siHpi1GV2EJ9L2uzuiyT-oQRMiwvzVPxnq6TMsmx07oP2Kx6mwCCK07PxA2rhQ4rSRFwwrlIxvO2Rte0_TAmWoMo4vgowTjk8pdsXEkYCj1yjJIXy0ecLcONGG7m3Y07G_Yj9V7NbPtiUTCzNsbWU-dKtQqXGplgEcZbgGDqeXslAecxSFvHv48DEuEgR2jvalVwPaIg2g6HcYfO3jucQA46FIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=K0MaG0cOU08AZOGT22Io1OiPiE5imCmfXqCeZ2FXHoa8Ka6Cg9naK--SB2WsNzNLuRlohpR8mPXTfDEqNJZASQCYD-meCx3zGwSbkP-J501USCxQx6V9j2FvUJj3t7y2dktHGIpb5afKscyrZUoNv-p84tb-x4N75_J3va8ilvXvrevfZthprSQgc0-I_yruSqX2qB86E7ZbqS9ebUBTCElt43L8AsOrnbNAKbHxlpJi-mAqV8FhHFtJKYB2ZbzYWujPKGry7HEzMBHC-c0VZotXS5g0ri1I_aVDEMxYqvGhxOFwO8sEEWwoip41ajnnKdCyQWmKNf8iT5Y8cdTHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=K0MaG0cOU08AZOGT22Io1OiPiE5imCmfXqCeZ2FXHoa8Ka6Cg9naK--SB2WsNzNLuRlohpR8mPXTfDEqNJZASQCYD-meCx3zGwSbkP-J501USCxQx6V9j2FvUJj3t7y2dktHGIpb5afKscyrZUoNv-p84tb-x4N75_J3va8ilvXvrevfZthprSQgc0-I_yruSqX2qB86E7ZbqS9ebUBTCElt43L8AsOrnbNAKbHxlpJi-mAqV8FhHFtJKYB2ZbzYWujPKGry7HEzMBHC-c0VZotXS5g0ri1I_aVDEMxYqvGhxOFwO8sEEWwoip41ajnnKdCyQWmKNf8iT5Y8cdTHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=i-32rQ3Cot6QiQ3FXVW86zhcHZ7oCTihgEF08STIinvF8mQer3XK828lE_xWgAddxCX1i3cP1qGKQnZ7M7MpvnbejxYQP-mM6-pErErS39DyNSAZMICNO-6NoJfmrkCulY12kaeKP0xHmpsGh2MaX3j4fdjNUrXe1ufMCweVWdyK7dgHXzVCVFGvZfEiDYVtkZxr7NeAH5Ny9YlLm4QLuDuzLfWkUshFUuCB18VhyG7KIM0ulRhvlj2c1c604b-z8wzF-0MJmMpT8Hd8l0ACpDQjxcqUQxFwdD8t23w0c6ukS5OT_8BAksCLlLSYQNx_1K0t4JuBfxEJndJ9fVdw84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=i-32rQ3Cot6QiQ3FXVW86zhcHZ7oCTihgEF08STIinvF8mQer3XK828lE_xWgAddxCX1i3cP1qGKQnZ7M7MpvnbejxYQP-mM6-pErErS39DyNSAZMICNO-6NoJfmrkCulY12kaeKP0xHmpsGh2MaX3j4fdjNUrXe1ufMCweVWdyK7dgHXzVCVFGvZfEiDYVtkZxr7NeAH5Ny9YlLm4QLuDuzLfWkUshFUuCB18VhyG7KIM0ulRhvlj2c1c604b-z8wzF-0MJmMpT8Hd8l0ACpDQjxcqUQxFwdD8t23w0c6ukS5OT_8BAksCLlLSYQNx_1K0t4JuBfxEJndJ9fVdw84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_04-Hxwnhiqss8LE8ckyQ1wfQcHxqk1PrNkKV6HESMNN87Es-FDZp_FqtcfvKJOPJ5TXzTUFmd-a5oXxitZGucGbODD__PrtQQ9RSqhYyI4WvoAG1Ocf38nMv4MEzBTNdgXUIomrjnopxpfFKsVC1HpnMdaBTi3PBIDv6OiV4z37ziljzEOdl097oL1fSCuAuZFXj3_lZ8TMonLuKWy11K-F25tg-_esTh1HoDLSd3VwiPQc2pIQA21eaD7czJ9PzcoEL2-JQDSSIyzbFdxfxEnf-yYhXPeTECWWmL2FhaU_5uKcQAinJBcG0J2IM7hQ4lISPQXgE4F6eCciVJx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoRTXPiVUtRbjgt8wpWLWJtdF56cXze7SNsRhmmyHf1WELkhQBzInrjbkeUlIUeoCbRUfniPJ1nfqJunwZv_kSXxRP0y-9aXawAaOI3LX8138QagnOK55yzpVZmhisEH18We28Lipd-0xPoJKXQ95jJhqCoCw7JteePyLL9V2Xzat5PdynLan6GA1HHymwYQVPeo3AAJu4g6OYyRhpXve9pn5kOobenXXY4e4vg9Ts5Bpp3G2AeWS4r3J1XHMNmOe5CwJ6FAttph7zjKmdUTDs4a4_0o4KukEfqpSuGRxp5APdohuO2guVKcfEhcyQAFALhtqwUVGRkN_0Z4_u9Jww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0k8rMuwuTMf-47D2cKUCkAdVvlFDJ-qy-BpHW6caJWVYfpg2xfTsum4M7g26FF1-W7wBBaG1W9ce8NAFd8CgSR85nzKWDqkglywS3rdqhv3PcHIK9Pg83nCx6qV1iTwstHlcjjaHtabSbKRKnN4mU5x_IT9Ldcqzq7UKfljjja-wRucTDN4IcBZUKmHBGHqYYYdSxKv7A6lS_oe4NAv28NA7ptN4yOr39-NB_WEeyOwA1hlJRPa8DZo7Qpumd6___7w7m7Rw7iwVCdhhBvnejmJn73RAP07grjT0d1yBqz-fqKHpR5sVS7JmwD4Mh6ieTULGH6588x6sjgZd0PinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=q_-rrlK567rBTcJ79vqtRgySOLPzK_6QvH_RxIYy3zcSckR0XmYpWMRA9kDN0P9TJ08qAudnQj9br6g0ZKYoOurqURBk4m6OUbbt3tfm2KtejaX5bUTmV37MvScZmBd34PMGkcOGnrgXYqxyzm-e43S6g1yVtiG-MuO0JWF9Pev4HptNixg4icZlbQHTzw8ZXtJjNs7ehqrtLWODs7SW4rG4gqBi-KCoaKooBY87-18ApZoeJCJKcPuuKkyOJEIoTMOdOPMa1UVTDBxh-p7nuUAz9hrneoYvgITSipBA-ufUpDKihuv6hJD37R4hvXxsP-kA89xR1IvVRDDGTYJaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=q_-rrlK567rBTcJ79vqtRgySOLPzK_6QvH_RxIYy3zcSckR0XmYpWMRA9kDN0P9TJ08qAudnQj9br6g0ZKYoOurqURBk4m6OUbbt3tfm2KtejaX5bUTmV37MvScZmBd34PMGkcOGnrgXYqxyzm-e43S6g1yVtiG-MuO0JWF9Pev4HptNixg4icZlbQHTzw8ZXtJjNs7ehqrtLWODs7SW4rG4gqBi-KCoaKooBY87-18ApZoeJCJKcPuuKkyOJEIoTMOdOPMa1UVTDBxh-p7nuUAz9hrneoYvgITSipBA-ufUpDKihuv6hJD37R4hvXxsP-kA89xR1IvVRDDGTYJaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV0uVNnTri1Js2y9cIFAqQ9VCwrj2S_WnQyqN4YRyZQuPWKJ0K5sIxwuTsLQBXrv1k-qt-b716MWi6waHAa86zQBYKN7zE7b-sX-VIxZOPxAkMeJyKvwizzL74gMIwmYVVXVuXhDCyxZAJY4MyRielYxX4HBliY5q353aCVu9G6rUH8SA7N1RzK7CVAm7JQ-i-hmfd5qaVWKr5hzow4Wel75ZCCquk67COgue--9tp6iM4iw3RN6cId-87AAd0FMAwYhkQE7D1kWes53jS7C4tLTP5StJLQKb10u8IPusbKI18XINUOddS3b4lasgfhDv0x8hTKs4-MuAKuMCJEiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGdhnZ3mB9AhzFaZ2FwhiUtWPrz7S9I2MURby-qDt15XwIbm23WYgYP45o4OGN7NDVgKITlZaxWbeG0svX5PBoPQGObpDiMJlg68QcCME7_mItWYCw2DoN8rnKCOZy4UPO1VeElKPaLPnWO6_1hRZln9pIbPQj7cB_GUdOr4yWHqcmKFDL3yNQTmmU-ILQEtPOhHMqeaJRjcWIWg1y3DvNyEVRYBngromEx8bv2o3x8Fu263D_vXnpP6g45e8-mDHqB08eJJj3Rg0BF28rhSJ0v4CE_6WOq_feYJ8-fI9fAvPCQWv5fKGc6QprKO7eoX9YjCi8qY5gs5-fYxDJ-bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_2ZGA0gMezvCzHemELG4hBHmJexhT-Z-TOZzlxlSYcsQ6wfXt2kA2XVRkWkpO_70HWpVGifvz6ZgNv4uRBcPiSyDR0KmhLspGGzcufqeCe-ii4Zrh9JawmExdfWc8xrYC5IEzZTEVCVSNqTdymNxaCRfDaCtpZbgSANdfev0G9zS2l2I-upMK2Wbi1zVdbpvCFVaTqHL5Fma59S-tHejFBRegRxQD_a-V0QKz8bz-MBKea1UvehEVNVvvSKk0EuAD7vuCRzhuLER3Ef5FR9i_IuJsfx6m7aqufE6643JHo-EovaBEiJb2U5NjoSwTJI9cIx7h-bjUigp7anNNqb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPm6s06G85kAWxIVvGAj3HMDXLdWasuK0IzAp6OXBiqMu3gkV7qcZIImEhq1mxtfVSfoeAPaZN31F-d5O3uHLMx4wTPhcaEfeZ8W_TWLkYwGpnGNm4FZ4F2zfyJ5PmGrNc1IbyQov9o6ciwKPdYuSk2OzxdKnFm2xpRy_o76o0BS8AhDcDJ73S1fKrfNrLD0SZuV2IQyr2QMnv0z59EGgXZ5vJ_tryZOM8rKUKPfm4IQ0uwd2pLfVGd-Z9W7QWHF16TRnbZjrwdOCKnsj96IMMrjpZLXQTun6BnA6kR8bwTiykrX3BjTA--P8-iST30oRzrky3fc7x13zth3vBUFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt3J2RezzjETL-IJn0291YE-E0cvMFD87K73-hF12YORNCFNUWYks2DuvdZt5cucCI5Q16bUAx9fmZ0YK1loOVlVWLw56tr3wnkRBDDWCRaT8KK01A_XJMq2SVyHqbVcs51sOHpgCsAnAedx3IO0bHxgKl2s3-bixNKoRo27mPJ2nU9tyU0XLxTKrqmeKcJFL9dvmjKUC88bW-4ESg3-aotcDq3Wssjjt2-ZA_c6xUnTaJWnh31i64Q4Y6b84sr4kJQhyDMHogjgh7lOaZG21jONV9GM4VXVWxS1EDAHyRwWwGP_q05sgQ3brUQC0ArhaW2kmrOhXY6NdSh1D1uSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkmjWnhIq7KqCu2ND96N8U0b2c1lRBlwBGamnTwmZHm1zxQJetxFV2J-zzoytj9pnyB9TKhpDMa1QuvQ0l4xJfkZl_-j3esL0cYi7lwwT3F74dBDOb7p-fv2mPDM2iCtIzHu3JDg82F_5K8c-C8xEVbyJk7CxpN2kqr7VatZymnFYVrWLS9oL6PaRyTQX3gX9lTO7Zki85y7tdSLqFJ2NAKomMvdsT6EqdXbmedFvPZ9sGaq2nvA4-hV9VH1qo49NLh0JJbZTXvgK4xSwchAIxzrUJGnBeaur3NT1sP49pHlsQTZSy5Xflc_8dkcdhcCHOmVhdqrCiTV1MaRaiH1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHKvQGIQ7FI53stS8YUDK3Dymjsm7iHc9XQeE6p61DuTmrs2vds_Xf-Ethavh1sv1ztk2b8dwiROhDWS9EOKW1Q3QrK22bkGuOHm18fa0Y7Ebh8lDUcOoig2er3rsyY3SYBKwxihrFbW3t8gwW6sr1HhBj6kHHC7yxoC9xioBWX-6bjUzGV28a9AH1MVe2k-Lkw2WgN2q0aJ0aI9oNhB8YVmNHpT5P3J4ZZpinCZ31q3BXOqOEddQijgk4u67qAKxGFfWVRyN0nV9TUtX-nZnZ7l2oJHamZnOLeHO1PIDhSjpsNNP5D_BjdgKGV8xsZlw_7r56pQCMFe6U0LgzAWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp0NH1imAerHNvA0vA5pSMx4aApXiksuHrVO8erTQN1EMknR7kLsG-ZDWbjJ4Rs6mECqb-GCGZ1d5ll75-mMUS4Ji1QN54GoLdPlPLv3jfqfFmCFVE7ugD-baluJgxbP9gvLq3UEknvxfDye5LfmCh59HKKmfwm3jxau5JG4XT67-PrGUJP3u2wot11BA7YQWt_iSXFOaaBC5nhhAeRjVdIW0g9RBRnlI7Ba8p1MkpjimaQbvfNpUUy_Ntj-ZfXLli_yEsp6i0ziC2hM5fv8Q_7aboMnizitsVSCqgSC-98emmmflkRKIIcVuXfAJTiKJcE0Mx1K-ml3gNcZFWof3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMTdaxN2jzAVK4iOHZXf-__2GYVAHSsq8wm-XeHDNZRTog9kBCYdcDGXMKq9aXGgenrXlDatdGUPsbAgkURQoSq0qxb-wT4JDqAe8W03Gt0BqZWZZ40_EogDqn9kK2ZP_E6pBhzvQitvo3ptrJbUDMwaW7l9mYX7qMreVoT_de018Cm2HIRsRxwiozzB6L_aWFVatR92q4F4ZKTgHQIUiSabMTidzEpY8J1G05SsDaijnWVihbxgmgcIeS6R8tJQj53I9saAcPAkvnrINSzmgZWNrtz6DIaJNXVPCxsUN0FSIPJn2BvWgp5UbDGUhg_IhfiHQM-GpVpF_1VVr7l6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-BvRVwOtWwCvog1IJqcDmRzdKR-SBu_ZMXP2uw5KJEu3elmgEKeJguXi3Y-kV3mdvotW1fl9xl3jaXFI9QWxAbwpMKv9H7cXUKElhGfM3SM_x52XGQajDaVuuwQ_WVoPjIWSrDcOKiD74mkRqzY514Bwig_YJvsy-De-5vEce_g7AOBtWC6VcVm5u_UGRvVVo81cID-YId9S1VRVeFywS4-JyKTp01i8YoU1SuBGD2-POajdCQs48G_DT_H_pm_zx2Ye4iQxanWKKku3015SHMjracEdMyAQilcVpUQdsmyV_skKyYvcAzhHCvMw3ggFPHkV_AUX8uQ-a-TFM7aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECBS2GBVsZ7caYjHCUOXyrGLTWT2qHCizDUfYX-osMOKKv31bT8-ECYqM15SrX6f7tOim9seVzZviPub6ijx1le9au9MioAGQOY912O9Ato_sEMTTTUTDnzax1wlb0NtQLo8qS2Q4Ifsh88x-Ui88X5vSz6vCMY9n89VnVA01xE5-FHbjoe2flDGJgIInL3jweiiZTT50iyAAaV9otsPykUaYYpT4I3Dwm3Nqm80nrvJaycH2Ux47npGOgTFwDer0_14Kva1XF_qx08VBkO86cewoH6NINvxAVdiinOofbWnh8vW4-6LjNObzXqX0a5eLYu_NrtD6PWKT74mLpQBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n89Vj_wKvWyIuxuZnkreLSw0ps-ZCW5YT64c7yS-949hIn0QBQFBmTCFiRQkzMmD1fCgYMNB873zNYw6mrD0v3IL8LoHQgEEMgPuDnUSaf_Jx-DG5v9bfEnM941S0RCTwhnXSroyiZ3FMOnZSPhzEFUdBguQ5l-0Keyj5FOUfEYTEGVXmeUMMjSe5dd6OWRvjBIC_WyjQfox2-8KGc598Zelx0wB9DdVFz6LnnZ30wubosvcBYovthKtLaRklwfpREPD6sNizmeDOYy5mujiZ1kP9AEpcgNRShqXWRedGjJyLbB5wlHVPmeIBiEAhnDlg_DnsDJTvFJLU8STCBhszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5CqSb4lJKz6pRduN2O3qdlcSddFew5-MB_Qil4JB15I_CB1AHVTntIaZhJkn9RrPiVb8Xdf0i4ClnwY90nBdyCz5e0pEx21UzWcDM1SRTuUIrx8Q8IC3tghfYxaVeyQxH5TBKRzUz81MgwboAGLAuKF643ePfGnHyuOvxz-AL0cDB6kVSmKsErKH2yZCYfN4hQQM1Yq-9Z_40VD0CtKw5OsfdKtD3Eco0K4dbmHS0V7Cu4iA2qFYQM2MY4F6xa6IT16zLV51ylYR88BCyubvmQtb1eUEM8ZSMdx8JxWXJl7OER2HisKmXKL8MjQg4WuhqRRlZq94de3GLtZoHtgPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=QmfIMBGY2OJVJ564G-oB03sfOqm7IO8oUnSiLXw6jC-cWk5Sr6tZAm4KmcQv0pkUFSNsIXn7_qh5DgZPtJt-bMjf-X67a1HSXok-AlMayXM8T6nOa2pjLpYicsxbdZJciCUJo7i-Hof_N-6IEY3smebKxjW4yK-_sCz8roWeh5dbMrjsuJA4Ac5TS6VvDdBY2hY3SOauFcG2iq6rMrNVRfZaj967B_NM2rqinY-9CNk77Gh5_Ry40jkYLpmPGW2KEiMf6ZHF1QftvnwwpBzcPEYpAVESHb-OxqxzCS_0FaiwRSrXn87ssIBpKWT44Of0cGm5y87DPtVFpzIIjS-XeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=QmfIMBGY2OJVJ564G-oB03sfOqm7IO8oUnSiLXw6jC-cWk5Sr6tZAm4KmcQv0pkUFSNsIXn7_qh5DgZPtJt-bMjf-X67a1HSXok-AlMayXM8T6nOa2pjLpYicsxbdZJciCUJo7i-Hof_N-6IEY3smebKxjW4yK-_sCz8roWeh5dbMrjsuJA4Ac5TS6VvDdBY2hY3SOauFcG2iq6rMrNVRfZaj967B_NM2rqinY-9CNk77Gh5_Ry40jkYLpmPGW2KEiMf6ZHF1QftvnwwpBzcPEYpAVESHb-OxqxzCS_0FaiwRSrXn87ssIBpKWT44Of0cGm5y87DPtVFpzIIjS-XeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQVF_wP330aEgd3o8_s9ifL1Y_vBCZRKBjv1Xy_AGgwwvzxOKXVWpAp00FrFwL-r30N5EuKQmyMRIGQCDmlN8v3pFbg1XB-bSndIfGG7RDmzO6yODB8RLfHP2q61lDeOpOeQA2RTGkuh0HAbrpkUL_ZMZKE7-GY93pKnf1TmSemeXwIHHRJC0hhy4hUQ-dVW3E7Bl86c_SSLwA-U505ZRJmoGlY0Zm7oTrq1OIVZ--oJdtkm8x5f6YZHz_xWaFvuo6A17NFxbAtQcBG_uNMwkXpdDgT0NJp50pHBQV7p7iYik3gu7_hPLBUCdtDYtPv4xSVNkCyT6xj5bM3wSonh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBveoJ0rOBkxldJ69LZZRMIo3AxPiUkwOlJ_-xFAK7_AjsKWCenPgBUT3nNEczRfcKdeHFQMKZ8f-Xg8v96QqWYUZEfmMKB5OogxPF-nh97F0GtB9FPrjPLVXct-ZOOEESP-Zni3yfP9AuDOAPu1UhAWO3yjWcfZPC2EAXFKtYQkLCrOiBClpVJ8sg_cW8ejTCwoqXBfRw54uiE4DM4UykG0_eySWgXs5z_ibuZh7y_S5DzXNMGlE0kHOF0J1nKJI5x5xK19-1Eo2Vuh4t7RkslW5fyrK2OGO1Ug2EMHG_Gl6vdfyDF7iTExDat398hhDguGJ8XwjWMMCL0OCZhhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=h_5xT8ccdwPSGgNJ5d3UscWu4WYAnYbi4d2TlmhyQf7ZwMHH-XGMc8fFacfEXD5H7cQWXhLyPWTbDUIjp7ARY0XiriE21P-ncHDsrP2YO5Y05NWEg13ulHXy10dMWcO5T9rw3t1OlYxrAGXe989wwJ2jEzpYIbMvGQv2dWXh7zscpnIlO70JJFzkqAG1OWw6H_qeMyQxOxNoLpBHcLI882-wLUfQKV_Wbdog257KC040Ldrh6XK64wD26UmbtROfxwntE5dmIK6mvAPqXr8mxYmb8PkIKUSqlvUpdq0I1RFM0YPU4SjWjj5D63hTEut3M6EdROa7a_zjjw02XRlRSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=h_5xT8ccdwPSGgNJ5d3UscWu4WYAnYbi4d2TlmhyQf7ZwMHH-XGMc8fFacfEXD5H7cQWXhLyPWTbDUIjp7ARY0XiriE21P-ncHDsrP2YO5Y05NWEg13ulHXy10dMWcO5T9rw3t1OlYxrAGXe989wwJ2jEzpYIbMvGQv2dWXh7zscpnIlO70JJFzkqAG1OWw6H_qeMyQxOxNoLpBHcLI882-wLUfQKV_Wbdog257KC040Ldrh6XK64wD26UmbtROfxwntE5dmIK6mvAPqXr8mxYmb8PkIKUSqlvUpdq0I1RFM0YPU4SjWjj5D63hTEut3M6EdROa7a_zjjw02XRlRSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvKsCpKjKb75jCteXWEWbIjqF7JJEHy5rql8YWhnqQeL4ACtUSladvSZtDeF6PWJXF1QFtteSS5fZfH-pSojvjjuUjS58DiA__f9CFMC3NDJnnCAYAphk5zGSZP4O6DicWATagj6SIOGBnVWA8EUKilRP1vHrvNJsWvoF2a0MVR8JAJNsHC9FBKhV9L8lBGJ2EUPLQbz5wssZYpt6A3trSjZjOgOnVXN3s7hSHybYLEYj1bwYLaPHLCdRRPA4HPLTxcDgYhEHTUxFfqqiaAsWw0b5s5KTfrViTZYRfVHdyAWacDjFdAAH1zNyHPxKYcouBNU8TjGnSyTboqGn7v5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6PYpOHkLIQNCB-4CN7eHZ2CJLZgzRsrUilGjm0MZ-nR8GcB07amZNwl34IcqUkBxtfFE1zwz89zPQLiOEbl3qoEMmPXzN7d7d5pXxthvPu0j9b2dTe5l_Txd0Z4BqI-zJrfRihCoMeNDj0DXnvEZAhMOOWBUMp7mgN77fKX5UaRPpZ7f9Hr3KWK1zhUfk2wfsGhYdZc6Pfky7vt8KZhEVTpNAH6lOIed6J_91vtOXYSdGinQpDfULIXKA82qwHs2jxDJgNtkrj5IVztOJmpPWimxEqWlNwGbfhUBs5Ez3v0OlzP8QRNAcFjCmOuqIYmjiqh-69k2sskHwH2RBnF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fns0DGSpY-ZU8qNGyXrQTEiaYCXYodPpQeyoPZME5tMgPyC9tAqaiPVUjYTddkNSeR2PuD6omIhS9HX92YTYt6Q9oBTjecLM99nkED0h5eu1QpMZKYlJU7_BSXd1qJrtY354D8TM6X2nSaA2P_BEw3KtiqC-UfeXu7QGaU0CDZ0gXhXDH5ckRqokxQ_0qL8BsCvvMpiFdR1PVl_x0sL0jXK_QRBaCT4wXqUJlqtY5Soj7YOh8i44I3eXDsyVRNfIsMQE1dKs2z4rIW0LCUDBO2jT3uYZqHh2R1bZBQdc09z4BKiaK7xK7ezJUKgCfbxcxg1OUJ4590y_4kdPp8C8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFVhovQ7tOO8fQXEZPs46FWDPcvoA5P5e2AdNuBf95XCJpFiD2vqAGNdCxDxmlI_z4M3PXXw2UuTs892plcsEjRchzr5BElTOoQhwxoANSN7blbk-ZS_MSDm96Il0STXPOiotQ0qVkqh90oE-bMlUfhEkgRwVNRf9UZKZVnUNIRCe9ejuBJU1abuzGkChKvMHFyNMoSdKwiMo0soI1FqGX7Xpsz4ocGhKQzmBzZYfzl8ONc7Amz-w77g8ZnSMA5VepC-ZSJhLCsgWBUp89gr0XNGvEh_KAqjmYHmqt6k7rnvAzepzpiJqGU1kqol_gluYkH_WBxRb3uPzfkrnkuJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqWVp7AaVrVpy7mU2eytpU9jYV3Wj3yWwASubnihbdLz8_sL3-tiUA39QuSsRfSu_cKzE7FrS-57Vu6ldjeVmRmR5a48dzd6J9sQ2wPgPXZ28xL9uO37NNg7K1lZVFOLyfr9tqPt_a64ggYRMBcC_LepjwMIk5zeDwJKhEw-Vs5R-2qOHvJ8envLXUJrPEw8d4r_gfI0yLsUUwuqxCkRq3nvYLZjsp3aDh5by6DyoMjxZy8Rfmf_CnaTzt76DuVLU3tUwweiGoPABlfWN0H94lpBjwL_E1p2YBlaMmpVWS5sIRsZFq5rJbjUdZ_sqxJvp1etEKKM3_uTfJq714LW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=dsuPEod94gbxDlmHRyC-2YHVTiOFA_SHfMi2UBpua99-ujUbncg31HacCh9xLy3JH3YNTmJ_PerNJL8Rv7wTLx3d74Wi855NelwPvEeUu2M4mTKJVBvMUKEINdS_MUuzbozHtu67kVZdWEy7jLRFXxLViqcV8M_WqzlWV3EWmqvs0Sk0C1CI6wXNEjzrcbqmpJ9Gs6OQXNI56wS2feKcQXeaywbz6z3X0wld9ulLF6feHn2Gyp86f9grADR5akDBsE1zk1kEyW94Ib9CKnD7rkC-ia0RekrLQo4a4Q9e1NG3Rd5T07kCwtCYkC_xUqLxkZHc8sKrduc6PnV_jrHcpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=dsuPEod94gbxDlmHRyC-2YHVTiOFA_SHfMi2UBpua99-ujUbncg31HacCh9xLy3JH3YNTmJ_PerNJL8Rv7wTLx3d74Wi855NelwPvEeUu2M4mTKJVBvMUKEINdS_MUuzbozHtu67kVZdWEy7jLRFXxLViqcV8M_WqzlWV3EWmqvs0Sk0C1CI6wXNEjzrcbqmpJ9Gs6OQXNI56wS2feKcQXeaywbz6z3X0wld9ulLF6feHn2Gyp86f9grADR5akDBsE1zk1kEyW94Ib9CKnD7rkC-ia0RekrLQo4a4Q9e1NG3Rd5T07kCwtCYkC_xUqLxkZHc8sKrduc6PnV_jrHcpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdWOkX3Pz5OpWXkKRqHZJSPSRggJzBo2Pjl0KucJ9a45qFZbYgO-8t8QTaYx5PMTdOB-yMrZAq-6_BLDq51YfpXiAUjz5nmn6UAGTExJ_-kXexVEM9MxGmrDYNNpktQJn5UA2w10qvuGe6Hs9jwvrHn_EGFuqJNUsU9xJQsgmwCpYfJVyuHa3YD9GNs1C3NGyRugTO7oNLqSNugImSnm2MlUBIu2kFW1VhyOcyuX2FaD9g-Wja4VNPmywmS2Fq1i--LseNCT3ukC8WjGjQRLg4R-EDmWmg4OH8tW7r1sts76477sUKEYven57GsDQk60MGDiMhwXB-VewNXMc2rwtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIGpDI5MQ0JF_FObRfdPn4PnVMQ0n5-ldJ9fGrRyjNBC_RnH8jOhV-RQh-xTEqifkXU_Ha8k145KGfKgV49LE07U56RcKvP1Ll-BDWo2GqvackrBeG_N0t03Z2tSHituJfZ1GcIu-uSfyEgVeZV2WBjLBLHgAVOe49bgJLciaQDHw-pC4U5yinNwaJ2skgTiq7w2iS_AcAXoXKnz6UJLIvKWAyPy1SPyKthmARWeVP81qDBQiy83VBWP2-Q-rpSPLloT-_9CljD7-2RxwlExoZOO05NtKX3qGmKJtgMIsci4OeOqVgMwtDtcsD0xFyX4LxBlE_ru1lExeSV8jUmrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzR-JuYJudpKsL01SQd47MkLvqQMMx2Y8Ze1v4PTAzxKW-awtgGH-zW2vgmW8hmKUpWbbokIi6L6BU5dOBKz-0Y1KGXZAHp6u3lBMcQvYB-BsUqaIvSeHkkwKjv8_n-DdjVSApCGBHKKyCmikjOKii7PwbCXjbuaLqMKDupPbvgVhhJ_lGmeFt1xLcGHsfi-9wqwF6mOHWsxDz4ZBAsJmkU2GOggG2kO9wpj7l-yCGtDn2jOOqQ99LaALbG4Kq5y-cfGjGKmgN1X0aNBNLlg-70zr8HCJTE1SGBW-pZP9CopI60dsGLouHSsQxaSH7ZEN6ZdJ1RnMrLiMApf266AuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urfx8nrXzQIYgzBEVmKx0-ltBDWWOMV6KiZzAY_moikNkX9wVJB2w7TDX0SB2y_JrKa0TLL0Kt-PX3dTjXN-xS_C0lWAmKDEAU3RvlRCap-zOnrbwhI3pxYR1K-J3SZytIHhM86Vrc79Fs2zkUsmyrdRXSVsvQgS2c7FbdnqnbQG97ptRXg772jbR7FjlLEh4UA8k70m2XBbnICVjjtvI0UP7so4ypZmerBvq2HNwkjLzNsh2W-gZiDC2kbapXqbLtNOjgk80FMDJ1rxrIq8UY1V238g3caphM3MFRAme3eW6WSPfUywilAG2aePJnlDjc2HoYxabrWQRviAGCxmiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=rV0GyVJvcisopMO6Z3CCwb-pU9GngeNaULc1lhWKAbrdz_DzTkaAI-M36mwVryuboHAvQfslb0ZKjnMKigNYzBm7aDFGJnVfjna4dGWmFl_EJ0C0Wjui6vsEWjgTNJZpKtGk_OsxiDKfeMDrktxS-UYvR_Ja5Ft5XO6-QU27hcdp-KRviorPrnW4mFFgQAxE5w9sEmJilILOJyT7jsm6EKtaVucSD59EQqe3w0GdwoRebuKJw1VAcODVr0UlohJ-5_EkmJyaUb4kM0nSU07P4-MvXUNnxPxtAjvJMNNIKrKEX3l_RjgGl6qMkky8gpi1hwcL-TWU4Feh6t5Ilq6CtYtvDq7bL_O-usgQs16eVll4-RQ8_GCXl2v7s5ZLn6D7wWiBgAi5ByoLdh0ylgI7OTsZBC2sGYvfyNDOSbt8kdzPa602S6V2CVlOYzZv7UT5JXFlbwZxcJ7R0eBNoaEKszoWd_sIl4PX2yBe-EGJA5mXWLad1aN8lfu9bgf0GDoSfP01qexaFvJXs5z5z-MahoJqqWEPcqtzDjn4ZXkkpn9U4OLP5mjJpVAuA46AKnwtZEwC62MQwJoatyzH80l9p6bqM9j8wsZuTI-xE-ntDBfN0dmaeSFrbq-oBeau3CvTcPc90w0ETKEy7_1O_CFPygZSbTg4GVk4v0d30vvQndM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=rV0GyVJvcisopMO6Z3CCwb-pU9GngeNaULc1lhWKAbrdz_DzTkaAI-M36mwVryuboHAvQfslb0ZKjnMKigNYzBm7aDFGJnVfjna4dGWmFl_EJ0C0Wjui6vsEWjgTNJZpKtGk_OsxiDKfeMDrktxS-UYvR_Ja5Ft5XO6-QU27hcdp-KRviorPrnW4mFFgQAxE5w9sEmJilILOJyT7jsm6EKtaVucSD59EQqe3w0GdwoRebuKJw1VAcODVr0UlohJ-5_EkmJyaUb4kM0nSU07P4-MvXUNnxPxtAjvJMNNIKrKEX3l_RjgGl6qMkky8gpi1hwcL-TWU4Feh6t5Ilq6CtYtvDq7bL_O-usgQs16eVll4-RQ8_GCXl2v7s5ZLn6D7wWiBgAi5ByoLdh0ylgI7OTsZBC2sGYvfyNDOSbt8kdzPa602S6V2CVlOYzZv7UT5JXFlbwZxcJ7R0eBNoaEKszoWd_sIl4PX2yBe-EGJA5mXWLad1aN8lfu9bgf0GDoSfP01qexaFvJXs5z5z-MahoJqqWEPcqtzDjn4ZXkkpn9U4OLP5mjJpVAuA46AKnwtZEwC62MQwJoatyzH80l9p6bqM9j8wsZuTI-xE-ntDBfN0dmaeSFrbq-oBeau3CvTcPc90w0ETKEy7_1O_CFPygZSbTg4GVk4v0d30vvQndM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqVZd0cq6RLN9-chovf8S7qJLNFb0KMpI_IyK2XBR0jSI9HZxeze27BY0hMZJZhhR5scOurVrv-WqHn6NpzJeaReWYchVoLcwrYRtaWS_EJ-pXfcwIsf9sZpw80_p3_7Ia78r9sjWWyWjmu5ANWvJE3htsfsRUD2j6S9A3VjPoqZIyE80j1ajy4UXU0ErfTyta8bFwjw-JYJQcLqE-S1Wnj8q87Gl-9vJMfvplWdCuhBeIpfnVqmOWNZSY-Z7s-aEksrqV22f1hKqEN3DlT0_WqzEQ1Dx3qXSUspbbV4n3hbss5D5ZOiZCJcuIM03wrGFnO72ZX74llt38LkhqHhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njXOvjIRWolMe6QeajDAhZgdI64mUbZVriHkh3kzxhmhhDKOhJFwTRP3VMXmFeywLpsEnxBKDu_dyJvlIuDUXQzg93xwDffZ6WkCePcYnnKsIauEXs09nb0y7Ro9U6tUGGwSEzDoupq-2lIEp2oSI4ZhjhH-qvMUIuMkGCVeNfiHzNqnYvCsW_JNT2W_ZgB799nOoJdENKuIWGRftmZ1CX1PR90mP541u8xI32uNQMGBUrn5kGWo9HOPX5KFda1Cho82AZWXbZBuMFHuW5sJSwM4GAXpsHHtKwjquOpavqPFbFznW4hqr90p1RjUPc4GFmt7s-n7WCWp2ZN-GTns0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW0sPVTG_1LaVjHuISmLqJKUi5jG7-ZO_bwQZwpQrnX5UlHhIZd3wC-Oh4Hnmb0ZFDi0PBt2AgkILFqtZvIlLSTQ_oq7dD-5HxQUI0hVgHWcjFGgYS0fjzq-ObDGe43B1q5__OC40zZrwXUTQrvf0hAwtyfbOMfN-OddegNpi3q2yxQGToQqKSxBUVsu1rMaEr1vyKzCuKHdmlkhul6COX2DR4HeBIrFCj5Y_UhHd6kdtiFkgmhymC-K8mXqyhavm3YIal0vKYiWHm0nczXWEto0zOenvipmZ6OL2Xf88M6YXJ_R2844qh8sbYGHX7QCPNw6Up7keJQWrBbO1angsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJZI4BjZ_rl60o2c3uYmwCywYII_9HKKsWfk0y3r36BXkOu-sxOJoPnO5AAWFFYeyd84SZ6MSGZrZnTl_KBUzDl3hc7TJuWbdwNSqgBF8-nqOO47e4TT4HXPgM1PNmincOHJo8ore4F_H3MkLumwfDnOELEP63rX8YVTKRFPsuteutnDzMtwKo639s6O64byoZx6IJoiuVqFkb3lTgzFSoVKhCP6NCxJLRnExCsFHha-wbDZkfAR9PQf-hK9-fuDdgBvWvLEQNiQ7OM03C8YVDuq2SeyRwRMS8IPhweWavMcO9izkT6Tn2ElltljCkVZ68CUE8Dg_j4Xky67giNYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLgsveb7m2FKQyTLx8qhv_xZPEY4XGz9S4BIuOttpsXJ8C2DACdMUaYsolvliu4OwWuDC1l0yk5iQMKFZN9B5izRe1h23X5aWV9MCqffiaOvo2hUEI84cQrtCtm9OVxCUqCntuLJ5lvbuvLYfln_709QdKy1RiqKht69YJN2uSuHK3YqB1b9B5qfW55dwC2XVTC6RylHdL_C0g-4NPT1vSvQG_7Z9MbNgpbRBtk_zc8SARQfmnOJYssjUvZxGwWIl0NeV7NBflHl3AqqE5kIW_mcp8ty4Sr-63SAaU4M3zNNR6kzeODyNpkgmzEg0gTDdm_WDYjN1k6jcTUFPzNRpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdyCVIBlcKjmOYVpryXC1ZG0bg3AvrnXJs0W0TS3UiMdovu9souWis0YU_lew9rybFef6doxCmVSWY6fsuqKEwRKTIxa02hcoIbxXPaSTz251_KqcUHTiacIyax1NkNu83nU081u5NPM7Qwp5JGuWOIaCqmd-n7fTPRFE2QzIUGjNc1llKQzFcSN7mFX7IABWp95ylUVFP0wIKekk1v9RFk7q2dsmPAdJfG4XQfIkP_xcNRDy1XQDjYwZhaOo7bJuTnsUXyBDkYqLE84oPF9yJvOo3oSyr37ygDLyioHc_KZYIW1gr8cQEjih1uCDR6Fi1HvOpwKkRRrTBdSeEkhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr6xCbCUW2yK0cS5xEMJR3m5VuthOpC_UOIq5WE_muAFwkavLQF24zreyk9utYAIoyXCJd7ZkNcTmR712U0M9OFSTIIzhWTixWd_UEVgjxXy3ktLl4XuOKGXFloozSI7Nf3R6F4oK0ExH6LrKDnen7RuRNQeOH0-IwOQNm1GxdhQT1iuojh1ufH2B4IIDGKMiUQtACnOHyX5eTgZ9IPn_QQGz3CeaPLnS15-Sd0K-Wq0sVTq-uefg5UIDHyKmxWtyxSCmLAsSjU2re5aRAze3mYubf91jRsxbdBnhJhUlp_XaLX9SkS35LKok8Vj-LBdWMNYbU8YP2DH4vLLvh0hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=genQgelbafVpvjPfmrpgW5QP7oEwkc9sYCM2Zao0_JU1j1LUn9oiafnMQVRr0QZHXixaOgE1lBLcvHlj_h4VnSOrXWXc34l79ddz7FEaWllobRHuYokL0nP-xoGGEWqnzhyrYzU7huULbNIm3flHdEV9HAPKolx_nZ3PUb0QpHUnj-C4S5pLd9bLkVTEuGoBvE9MqEMEH9cpUsT1BZMZ6koSX2QhUQVpeNx8NVEu5KkgxpAMTyClD7kWYAsXlLtMHNgaMOGqyk1R-JQSDLxq6mXHaRIoI3r8_jTfuNN74juQTZShBZQBDWg_1s0pDTQcmU8LUUE1Egp-PbOJyC-2BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=genQgelbafVpvjPfmrpgW5QP7oEwkc9sYCM2Zao0_JU1j1LUn9oiafnMQVRr0QZHXixaOgE1lBLcvHlj_h4VnSOrXWXc34l79ddz7FEaWllobRHuYokL0nP-xoGGEWqnzhyrYzU7huULbNIm3flHdEV9HAPKolx_nZ3PUb0QpHUnj-C4S5pLd9bLkVTEuGoBvE9MqEMEH9cpUsT1BZMZ6koSX2QhUQVpeNx8NVEu5KkgxpAMTyClD7kWYAsXlLtMHNgaMOGqyk1R-JQSDLxq6mXHaRIoI3r8_jTfuNN74juQTZShBZQBDWg_1s0pDTQcmU8LUUE1Egp-PbOJyC-2BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqHtMc1cjs-Vow0O-WqFvKzJa15vtkrwl7zXXGwzkeZ5ymBktjY88jbCaUpe5_lUBFJJtwIgRiwY233l6DlgHs2ng6jOUTd_9wBTavKRie6Fwp9uSZhdIWGH2nIExOU63xLqRpENSsWuKCWBYWNMK58Mybpa-Wg7xMHgGNgrRV_I1Nu8zfv8yTMijEC_VtDlOX05S2JmMkSUUFrYAdQUgk6NulfT2QnZHe0dd5iI6-uUeH0M8mEglPLh6D3zOsJloxEzWn5t8Z06aGs5hTHo1jg6Rr0jU9PglUoV1JmUXtT9aSG7g5WaBbco71o0Y2wX9ZaWzU2NGWrF8e3M7T8KSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiZbTBjg6f05-kOCsKM3sR7Em7CfkB4mISq0FI18kBR55A4bDZpSJslotAJQkqDLvysBH8pTa2O9KiYMjPhQq2ynEPfi40WOvlncT1lQ-VD_BOcHDMc05uwdUo47jb8wYsOJEfHbZi_Xjn45E4rhj5TvDEQ56xduPCGUtrJGDlfMfUAWKYDHOMc2UfwF9PmxTJH_LFAdhHf5dQ2OYi3NffTtjC3qeqNRewtVWTP_Jas2r2bDR-k0USMDyiuizotxJxyWIo3MEnobySPEMGI7b_NQ3hUO9_-bnZ1XSM1o35jo1LbqKoekOSWtGGl7rbHD0lrtmulhAW49Fh1zCwmpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvIuiM9fbv5qo58FBNIxvt8hurT9bsYIMf9zGgDiMrkAL8J3Li46kza4c2w6DBbEKDrNcEursZDvY2oGRpaURAN6cO43Bpr-Nvg-rhGxHCLZFPqMSv_vAFphKLnJc-566vB1llo-GjMnZhe4DV31dIN4jSRPu1TVN78Xw-VG85aQDQTn-TM-eswe9CKsqvKhC27Ci-PfcAIxJCWknYJYUlvF-ArGmeZS0LVLLTrdUGi5FDf5uYGsu182eHsXHknO07SIhUYDjN94JxQwI0Xv5Qae7dd_XwVBDGEc453xxPGwmGugHii00lIFf7gHUC6sOTKzvF3slpJSVDGFRdq1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=i7qXPfieJymCNsiJ7ve3_cFnezJxGPHX5WM22xTitlTahjaVwboqj8pbCV7iVNeXRbCN9zB35hJlgr0cq1FXSZF-_pNo66lnzcftFH9rLnkMfODHjQpfG38NDn68HyLelTpg9jSQ44Fxtp9ru4TB0htmCDIQBzWFXJzZnbpdYp2S7uH8UbofqpEesKWXLQu1mxPMdvXCtr_ws8o82qij6-psQNFYpaiFUluMAEKJVdejEEOqoS2STphANb4LxM9BLn2IYt90PiHFdZ6b66dWxTA6vJkdOVTxatkyzW_M6Docm2v21ZLKIvO9ZFMTfO4EJidLcC2q3xlO88xvpi_hTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=i7qXPfieJymCNsiJ7ve3_cFnezJxGPHX5WM22xTitlTahjaVwboqj8pbCV7iVNeXRbCN9zB35hJlgr0cq1FXSZF-_pNo66lnzcftFH9rLnkMfODHjQpfG38NDn68HyLelTpg9jSQ44Fxtp9ru4TB0htmCDIQBzWFXJzZnbpdYp2S7uH8UbofqpEesKWXLQu1mxPMdvXCtr_ws8o82qij6-psQNFYpaiFUluMAEKJVdejEEOqoS2STphANb4LxM9BLn2IYt90PiHFdZ6b66dWxTA6vJkdOVTxatkyzW_M6Docm2v21ZLKIvO9ZFMTfO4EJidLcC2q3xlO88xvpi_hTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naSPkkDKhf9imPlTKV8dAzte4W4613rsUKz_6cs5Pk30P9cxdTvYWdVxcM7q2bM2_wy8D83cKcUjKDqJ26Ckyn1DZiKHanSGac3oHmjjuH-7umHW2wkL_fOqQClvCJYGL0IPnuhOOHE5VFHLYh6tS1t9VOT0KAcZrBhRsYMStY2h9Fr_kLgZTOGO0bzw0IuKa4cc-jFUck-pHUHrH9wP8zasIex5jNmNdtEYOpl8TZpTHNYnSkFuDmabo1v-VRCbobUsZ3gpITcBfB6-OYSbAsUaTGlYO4Koxhj1IsXjj_HxbID560epnElDMg4lPkMpAv-1-qxOn03zxlsXvdzfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=kvI9xJMZsXhp5XlSVOjVPR9OpjV6UbHAYr2S2ueKRfukOxNhsXoAqespBj0akgM0pzn3uoveX4PJSWnBq2nmtWPJWh93a8IifBgRkrwpltZG7Tpi4W5mDGRbcK_M-Ak_0gokTA6N2oD3F-cNJYoRWwTViUSww-S54nLcV61cIsZSGw3WIoDTRrh9Z6Mv-JIWvM2syl6vu6LdRV-vIju91aqhkkluALDIn17-4jdw7wg2jEnLxLkpDkykWyC09A38pSWP8QVVXGripxitTasfXtAFbN_ksDWAY80M3l-jra0jig88OOLAo6uAp6PrLNTsTot1FNq1eDH8-Esp4itqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=kvI9xJMZsXhp5XlSVOjVPR9OpjV6UbHAYr2S2ueKRfukOxNhsXoAqespBj0akgM0pzn3uoveX4PJSWnBq2nmtWPJWh93a8IifBgRkrwpltZG7Tpi4W5mDGRbcK_M-Ak_0gokTA6N2oD3F-cNJYoRWwTViUSww-S54nLcV61cIsZSGw3WIoDTRrh9Z6Mv-JIWvM2syl6vu6LdRV-vIju91aqhkkluALDIn17-4jdw7wg2jEnLxLkpDkykWyC09A38pSWP8QVVXGripxitTasfXtAFbN_ksDWAY80M3l-jra0jig88OOLAo6uAp6PrLNTsTot1FNq1eDH8-Esp4itqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX7Szgo2-UXgRlfl31K0mCWBtGWyfvHNPcv31sUxrXpVKGxJmwK2LjKL55N4B8Il9CJn77mwP9X5Ut_4xGgAJR_NTW_iWrMYhiRbwc49fbmaqh-4QPk6Oz8x_XjAZw8PQwC55CrF9Kk9dtCPwDos46hFTDj3eikKJ7PMK5wF8tDmgApaeipUk1GQ_Jjhat2-pWqeHaexx_sTOTUL1G5a4J5mIjwBemjsgxr-jLzIfU8-mEaUzQ9M8oINzovIHugQOjmgpIMz-LThdk_IYNgHRnonZmgY-j3VEcHFslEe7snDpiJyEcNMDbywKb3sUNlTzTeL6yg8qQ4qTh-4D71sAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=GPZlyiQSu0bZYL-ZeGeyBaKLz8_o8f-qRwI-VlLONqbgp_RUG93tjBu3xNvqYGlFtbwf57Ppmkno8oGJQor5omDNHxgtIVFR97qqzNcbcqtf_qcP1bX1gY0P5dc2Td102ad3swwNTb1e_NSg_wuowdlj_MrgHxX9X3Pgg5-tZ1Y0HdO0p1mNlqyTOvYhSQUAPJtNr9Hc-Cy_pQG2uEpubdog-PNdMp6VHMwx5mqLyFtooKGQdaKORdHf78oqsaFedoQfb4i-tFCkusE8GoK_ZOzZ9y5Hp29OOkwjF1aggia96uCOOEtoO_G3X3IBuYCgHbtbNMewPZLUcutiui1rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=GPZlyiQSu0bZYL-ZeGeyBaKLz8_o8f-qRwI-VlLONqbgp_RUG93tjBu3xNvqYGlFtbwf57Ppmkno8oGJQor5omDNHxgtIVFR97qqzNcbcqtf_qcP1bX1gY0P5dc2Td102ad3swwNTb1e_NSg_wuowdlj_MrgHxX9X3Pgg5-tZ1Y0HdO0p1mNlqyTOvYhSQUAPJtNr9Hc-Cy_pQG2uEpubdog-PNdMp6VHMwx5mqLyFtooKGQdaKORdHf78oqsaFedoQfb4i-tFCkusE8GoK_ZOzZ9y5Hp29OOkwjF1aggia96uCOOEtoO_G3X3IBuYCgHbtbNMewPZLUcutiui1rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfjqITu0zQdzXcG7z84c13Cs7XXymtW_NCGAi2vh3il_63acGWzRyLqwt3JtyxkXHK3ro3PnDiNnhzXayNQzjFs9rg6dt5qj7hg6KV7az8gDeQ8cQ18oh6bhCdB9HMpQmlMenIfm3geLS6IMGoQ4IASEQP1SrWn0AGjaABeRGciyjZafdh7C2toQzEBrbZJ7A7ORRw88EuigR3P1XMl7lC-p4dvpypI5_ZGCXhxJ__6kP-A_q-9M2dzpTcrvzc97vIMkrm5kRDo0Ga2zjkW5nd6EajsObvGbqtUOVSGbbI-y6EAo67zJnCcuIEjrSIu8YRyMMtngIqDE-778WM4Ynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7AG_wE8vNUc7Ha5hfqAEynMRH4MJEsRy4Va9b_tOeA7EVUEBeXbynXxKQ8LOjkRhSNMMSxTM7GUF_rmlaMtQvGgyXuuMXn9g1nayium0h0GrbEubHPIEW_sQxzWQI-hj68xwNon8AhD5tBAkPN8TZquG5TmWU20MmFE94ZLg5tOZMdtA78Ok6kpmcWVNehp6whb1O1Qbl3kEgsCMBLLdnkAIOD7zLOJDgvnjhM-F9sXMl-qZU_r39qFEty9YQ9dlqOI1ADuXtulv0lubKHYrSipiLFRelRh0nuKLfk_QRkV2Y2mm7YPBNQBlBEOFXYU4lTG8peEIGN7bs6QqCL3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkvZec2nS1ip1-0AOJ6vNXN7We27jIiy01k6ce3RTKurD0BQvvoM1ib4KkefMRPiWfbaip9hT57V1PVDAPnf-QLWpSd6j0fB79Au1m5Asi335HgxUNpgCijj7lHk9uvA2jYIwxqpmZ_8zSoyKJRpZWAuArfo_bku_RZTEWWU1i-ms1GG6dqRfdJ6NRDVX-erF8altH9ooWU76GstWwbeJ09LRgyP5PU7eneXTa7nKV0QKwcuqqdFftF-Ru_5L4aMrETMwSrUv4bm6WXcmJAo-sIajo3evG7GAzwq8qcNw94vcB0hFeh6mAqOgK87pjNbmaxssPdIzthbp4-UtEZmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfDSuZYSHwjapIkHfScpb1ebvbRCZm4iht9HsEnVoi-MUdJ4rsPrtLkVpcR8E7FK68sAA60ppU4Yu-DZfPNNpgOUTfOajCnzwpdJmWtIuIOvBUSR5M2CdQdOFBPSgYtxJDGYUO54QLnjmF5UUzbaW84KhY9Lemzd6C2K1cocEJ2vAnE_kL8efL3IZFCTwkJgdlbyJ_yhYMrD9WDyeKA2aMtN8oaehpSGNVOFJ0h9J24zqiN_-fxOXUoLMabTa6OADGhCNvLbPIvOklWQPxWTKuxLxFGcG634IBRTVoTx07mf3tegIeQdDU4sT9K4d4V9j2kJQ9WF8Nj2vQi8ZBdIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=MlH6YyJMQby0P1rwtivFt1tR1_oBwL5kpJObEtdBOgIHqZg6eWX76AgeN1nPiVYMe-2zKFvVtoIt99U45q6RznYAPHzxIK4W3UwVbERyVy9_sfznwbR_iitnxk_TEGZkPg23IxRcUUJrREA6rmX_FoIc-RTUScwDpIeUZ8SY7JIEliYOR3Ky9OyDv3nFaICSW39cKJTwNqaTP8KJW5nQvFIwctNeWw6_W_FcONJ0m69pePdYzpraNqghBFq_Df5C6hXKAYqrfTVNeT-xye_vErxX3RGXMWyWEWZ1Jl6coTi4vbEyJqyPHt7aXYghTcn7CJBkoD4Pf3grqtm4Ybd8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=MlH6YyJMQby0P1rwtivFt1tR1_oBwL5kpJObEtdBOgIHqZg6eWX76AgeN1nPiVYMe-2zKFvVtoIt99U45q6RznYAPHzxIK4W3UwVbERyVy9_sfznwbR_iitnxk_TEGZkPg23IxRcUUJrREA6rmX_FoIc-RTUScwDpIeUZ8SY7JIEliYOR3Ky9OyDv3nFaICSW39cKJTwNqaTP8KJW5nQvFIwctNeWw6_W_FcONJ0m69pePdYzpraNqghBFq_Df5C6hXKAYqrfTVNeT-xye_vErxX3RGXMWyWEWZ1Jl6coTi4vbEyJqyPHt7aXYghTcn7CJBkoD4Pf3grqtm4Ybd8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzP5VOIqSMJjKdbxVeiWJCY0y7YEh85xKf9sqywsOV2fcXR9wHgnvapJuCS9PH0gyseG3mYIyE3qT8ICd8sjustX3ClrwjZ_x_o-NqmnKHSHtaZ_MLhl33W83sxmaHq0oj5Y7lTMaX0zxflbNcmEu-6oCF2VpUJeDEG-YTKD7fuf-YX8DcLdnlD5Tph5WZgyJ8h932wTe45-WBXMbui2SFzjUdjNaic0wX7RNthUGaH1DWd7j1UHmDW9nG7zJTy1LioFMZK4Eocq3ek8m25ET7vS6bxzyjjaM8BWCGdf2YerxjBz3yX5tD-eaas82jEVTH0G3cikO7hTAuE9X8YXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqyZnjxagueD1BrjORo3qe4syZz73dUliGf_BtDF-ynnGqMnjHV9ZHPsJt7g3GfSmzWy72RUTNuE79Mhp6-4nehGQYhz5pgCYYLVdagFvxwh_CTPLZNyn0drwqjWy1CGjGQJO87yedCfkss6_mJ-yddLXHEGlT-1Tp-nPl5Tdl58tl6gc3Zk6G7hcPggN_d1yNut0uvwkbkwjGg84mh4A6uVBb7fWrlKizWDPKkUSNkZpSxNp8WNhHlbzrPWwdZ0kglJahymoUJjYILzIvrWmboLtQ0yL3RiPb-XfhWmhMpoSZLwi5lu9OR-MhSWk7UkSKzpqblIH9R9suKfbfylpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlDuQ2-Q0E3uPA51maJb5OKp8OK4P5ULmhbd8NHWIZPCaJ5HTOWx-aFUvbmvGhgtZm5RgqRLVlF3rmSUD5YQcpaVZjZlyZsQNiJrfQJOSVtkV5lpJxw3f8mIQ4mc9Cb0LvbPfIJXDpItJkxSgqUbRNSSKAoqiP-iwsamOIDKzxAP798cXy2Eq6acc2TMKlJgFYg74vus-0PdGL9QjeHILwJvOClqhF3gZBnAEZa9Mgttr0O0ucQ4F4LZPlUTm33gDyQkhPjC_JWVuaV_lKAUVP4rolypupZzFhU_rOn6z0ctoxVkhfU8SeCcJLQM4LdPuGqNb4vBtl8Sk-crKEpv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No7ZAzDCSmrEVzx85RAVnxoHC2RH3s2cHePaTMIr9tFQkYsOcZuiYwPorhNNuefi6SigA_NaFEdcDPVtnaznkngAUAxkLDtkqN0cBJu8uMDUj-Y7WJoFepUXANhn68C9OAoENb3htruB7YiTKg111x3hOKiC-lr4m-wc0sIFTU1EFuKfSVgQnRXwVrcsFoKruOUrxaj6-xF7U5qK0CsWUqGPk7hSn47rJ4BgtueDZQNcrI2QfmP2PtXS-Qk_FGirpx8QdzJzBST-WDmDZG2Fudu4gePvPToFMsFL5VUmWwGTGV7ByuM2JfvQ59KJBJ3FMYAB16rE-w7NJsbE7u2lKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNsUOYkEib4veKPPsE0RNK1F9jhNwPhnt6aNtL1QWY1ohGk3ev8MVvVNnTSqWk4mwbFNcR5Mek4arQAa_PXIkNm98okKaTOzLFu90tcc3IOM6_cyzSYndFEGhEOMCIOInJU4FLIGoG06GEwQtzYRVZFxe7XLp_G6YEI6yOLpbxkhcWxrKSGS7sYc5PG_u2ijlyDp200j3IlcTAh9d1u0tX8XsAdjUw9Fkflxite9-nnauQWsmumN14EpmN_fRNg_UsQ-iJ2Qi45iroZbtD09W8Np0V0nvWUOYPmLM9Q9fqxR_M1oQKfDMxJbyb6GKCTmnkxRG8vbo2_VNGX8LE8iKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBu_37WXNG7n5mBK2gEthhqpAwmEJ-W6qTl9SMdlR9BEQD2zrvrHs5oIJoE7L6XQhSyKv84fkv1u1GQlIVg5QUwuV63iqjRADynpdKTcvqnUjdG-ioGQL3c4_dJLXqRvka688VRAkBb56JoAST1TNyBEeSpqfpuLsEN9pOKc4g8LeSFBNtdehTZ0Jk1rUnm8Ii_TJoWpWxiq87FlQq1_pJEhesiexk9GVAXT6l0LJICHInmvBUMQIrq--Rha3nklGh-Q2PoKQt_1Qtki4altayeg4aPRTZ_dq3gh6Pd8eChbfJNOJhk8B9ORXeAmvH1DzztCsGgZSG3ZJNYfCEtiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNhh0t6GnBM9QNVIjWIceT4X1efNkRSIT0LUJbSDAPqVZbYxg77IdNHlFMLFX6Y3LCfVxhs6_KkOs1BbnbBweRG0uK38DasScCeC9swLvQZNhX9vyiVK26dSGHd7MoKWzZJLR99dgMBZ3XmPVn2syLbzBBAZjab7GWvYKXI1-8WBpLcYunfEXsy5kOIZ11P_yjtLF9-0ZdwxfJ5DoSpqDaOaVgAdvl5CFoXBfEr5LBvgGdr5t1PvycOtDe2rNuytiBcRClJVtl0xnNmThI26ggarqV2_PGUHEiLrkQ5-VvDlrFPrD3_VLotIQCpLLycyLYQ985yLnwNlHGNs_aczbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch_jw917_z91_ET3UwBCeyLDJJPdkq5k_gl2RE2Sy06fIYWvskwurI3edmPRLSJkTn07Sbq5CwpgK1fn2uv80FCTfn1tjtdB59XZLgxmUsfm3TfYLQhcIYSClUSYcmJQySh48cQPwEKeiTwmPtt8_cRCf5fLwNZcZHGXS4t-J0bu4I21SIT5KomJVyhKD8QpQ66Cw1wBAOCCvtBcNiGOeh_WLp8rVlO8Wy9I-S4rAYX-8muCT-fXCapLXKx4C41Y2T_6Gtn29Nh2TjKk5cY-dy3fLAqVBkz85283I7l_Z2L-J6PSnwZqDICBX4P7ecWzE9yuCNPloAaqkXBdx-oQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpl4YuqPyHxJi0JoBSupZYqElCDF_Jq4K8YRUPmytvGV4BUmrblPTWJOcV6rzF-55JfjI4vijw-YKtCtxb2xmRpyMSqmj_RIRaKBEwgN1JoHX5USKQ__s4CD5LpCXhTKJAP1aesQHCa6f5yd4ZqzVgj36YM3UybW48CKBm2BUDM9QMD3PEFoLwBX9nYbsIqWZBXH8SXg00xorsoOrwsWo2O2CHjAk7spEJo1gTwC3RbLUxdOlF3rESW3___qHJkWBg8eNgPBmCBwuG4mzXUQCBCNo9vT9XXW901a8Y280XouWclqONW3yU3u2vYIN-m9XS5j6JakBTupLcSc98dyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2rP0WkdXBZcCPhw_51w44ltoOmUDEAhJcZ3OMChYww2ChIQdZrNcnUX7m7dyOMNXdhLQvKacWd52dUW7CwMuzwPWkQfCAqh5ibjZ2Bc1i6CB8pZm8ZP0c_anRRmSiG1-WSAAso2-rOIQT225paZllWRcwZ05a6J51Lup0Kffh8O5QXXFYu0WQS_9_nqVxmcLyKVHASlcVOusuueG5uhCep8LZjX8Qtc8uYHAx92B8i95OPf56kg-ooaqxSWZvWXzD2uHJvzZGIGEjATl-3T4A3N-reZ0qn1gsdQPDVQiU1rjVh0FsPhxBODV-hug1GXOmoBj3VnMXdueX5hBubkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px6sukhc3mMfINLlXAmcSpqAlFXDNd5ax7xMFBOhDVTOlcLa7wj7IhAXfrDRrwo--AveqEh5T-Y0-d-VhVXhXjhY-nYjglqsqsnbGBJuHUAvdLllhhW_FPnOBs17aWuWyb-rz1PmxcnAdfIf2dxEGRTnlN4Db9upmB4faDlgfAjNvzHoKss0wFeJXARcTNYNEDMQ7kgXiYkrh3Zahp5rzRA3H1KJCfni-pU-0db15H2nfE-pMfTZ_tITwqChSb4kzTg0X1CdLHXRd5t1MOSN-NypmkBe3VjVfBRBUZsMhg03ur33ZPsP3NhEY61Gh5BxOOc_y5oHa933GJ5zraijqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxvH-kDbf5kZJqxz5SdaFjoQ6SnWc8aCdhgA3ufubEiUQ2EisFb5GFG7hGzHXaCKVPEo70DQf2gYT9HDsD24PO8FtUlwfujW3KCcE9O4jWRQrIcpeM4qVRr13tMf5cGQm5jElhA07SJzlcWAHUT99oLCU3hcC3WigL1mBaW6nNwknLgC4oT5YCZb4aPDGHGHGweRTo9aifqyTckAapLVXg9yM5zq3qDR6dzaCAu9Ww5g_qdE_rNy6Ktz-fF3H5ehiROshE8auKyqZ0xpxreYgu8fPVU-pME5xGD8GiZK6Q56VGve_4LD8yQRufSPpmLxC1Cr3aLI0gkcDmqzDSMX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B29k9XsPw0Quv4S2RexfGplhhPnJqpkWAyjeXgL7ip0aaFou_AimVlXN8QC5BXNiDpjAecgME_D1P-Sivk9OFjDRXYZxsvnE8i67oS1Y8omyVCAmubwf12IwtosFI-fPyWmrGkSWABz3BxPYJ5pOG3rwbv0xc58J3iPBZDxtwkDG6WhQoKMidQ3IVsho84C8B-vMU6nKK1c6khGfACUpCbgxqjGnhBWNEaKqP0KgC0306_8ak_Z1E69lBNA9IhtkeosFcGMIkqmHPUkxdaLmV_rKQnV8Myd2qR7umCC03mfppZIxq9s7hKbK1j71kQqII4VBG2QLLrPnvRdOtqJmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=JYiems5rcvI5MV3fbtDvuLGsEEr_3QTZR7FcyUoMYCLMAoSrhcR5nLMbGsq60HRfYr9labIAT01E-4cn7vAAwvVY-eMcwtJMoySkOlQGujr5PyfggD02Yl5wC3YYP6Hq78vjOV3rUQKCFul8IlzvyHJ9RpZJU9ETJCEhrSXtwoHVIVZ0uBYBO6ES2VEobikp3A1OaJrkoEY8phGm8jqip6HWoh9UN9YHCL42JMbt72Ffrn0iAMSxlMAT0DkiRb1jIe1OD3sHKevbwjLVxKNLsjbPefOmrCPpUYrRrECRYZ3Eu3iT-gIliKVBxXbjqu4HSiBLbeAmVLsj4JF5TCRHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=JYiems5rcvI5MV3fbtDvuLGsEEr_3QTZR7FcyUoMYCLMAoSrhcR5nLMbGsq60HRfYr9labIAT01E-4cn7vAAwvVY-eMcwtJMoySkOlQGujr5PyfggD02Yl5wC3YYP6Hq78vjOV3rUQKCFul8IlzvyHJ9RpZJU9ETJCEhrSXtwoHVIVZ0uBYBO6ES2VEobikp3A1OaJrkoEY8phGm8jqip6HWoh9UN9YHCL42JMbt72Ffrn0iAMSxlMAT0DkiRb1jIe1OD3sHKevbwjLVxKNLsjbPefOmrCPpUYrRrECRYZ3Eu3iT-gIliKVBxXbjqu4HSiBLbeAmVLsj4JF5TCRHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1uuYABa5OIuCZYvoNHYoFlwRjquqeWXbVX2qZg6mmLuo-cxNmxwOsvfBqZ0b2V5sJHHbzNYsr9sLnKbEfSxaczWIlaPcXQN_GRDQShUyLmxMB8FdOkIbDRvZxOzuMqjAHjBvKBu71C3AZBGCAkvOM2noeDvESWvusqhz5Xvk71zzW-pn3n8lXqy-ISZh8e3HnW3OuXPDdL3TnrjGRR7HxcEUOY1RsmbofvN1me7_9OcIVhHChcLrhvYKPo8Oq3o4K52sKjSXnpEEQ8bQVCxtZZyxEtVAzlQhl2D8atb8g_0bO9fe_bAMuHXKO48tta2NyKBHOI-oSxXOBOK7N7iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA_MVSL98ZjiBd415qgI7WvhiyDcFaMJZ_4brJZZbg16rSfVHO3A_lRe5VBwgHfc5NwLmSPx_PT5n2TR5lqD8AfE_117ZHY7zY3UKum82Kp0rcTM14KzT64int8x3fqh8CtX0mwAfNtcPlqwQRjNCV0KDnkVYeFYAEnNXNYwZNEUaJHqxCckBWI5l10SojeEJh2HZTHjOC6TqXf83oPBUYBze0393In41EUwul2QlTlU8xU1SnURUuEZk0uU-auxHsHZjrsO2oxIWf3KNPrMf55Rfrj9KHAINOUQYa4YLaDGtBKcnKGaBUj7VyAHbJ2CBDuRMGQOvqpxttiiuImwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=lQBhH6cMUy0yCvWUZrtfcHelJpe26QvhakMBP1sVrfqlEaphsd2sZ7FE3mrRgvnXuAe2HNiMnRukArCJfXnZChzmTYxWH6MDN8IPqdoe_sS2e6NKE0zrLhrKEMKKMS7RCbGt0J5IpMdO-LmEw0TW22biK29eEO_TJfpbekiVmHFiiSN7TWv0ZVY5bzp20zEpcfSl0uCP4r3RTOhqGk2e_Cu85KpSMzVk4TCYd8d21xvemB3ILK-ktl_hsdKlMX6FKMPR0jylIaKldPHhNjl_N_yORpq9KUMDsUrDs-25fxykhwrrFW4YHd8CSsZpijl_Sze0hE2wkHH-PPNBh7UIvXfL_UWF0rEKE9AFfcbz3Nv2zNRskj7EKlfi6hyuqp3EpDLHgayf5NLVg46JwIbKU6gcbCYyjYOzGYSClMbeKLzxKZNui8KxH0GbQo-A3MNCjfd6rHaMBd8bsnPzy2uF6DjxLmpVo8GZYcMEjAyKuW22W5CtzUL5GGDzoKULcaZZ-3qAwnurfoFvTwHYM4sbrWbTcB5E7GCcEZ_iZMMGQLneZsqyT8FUCHqMWmcROgsZx7LJkLeN030dRjhOAJCvsNeYn9K_OhtT83DosC23OaysIiK1-VZK6mBhVrud3cjYGL58Kzkt7Oz6IBtg1s0j1oMs2DUpEl2BJVg2ZM-v4hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=lQBhH6cMUy0yCvWUZrtfcHelJpe26QvhakMBP1sVrfqlEaphsd2sZ7FE3mrRgvnXuAe2HNiMnRukArCJfXnZChzmTYxWH6MDN8IPqdoe_sS2e6NKE0zrLhrKEMKKMS7RCbGt0J5IpMdO-LmEw0TW22biK29eEO_TJfpbekiVmHFiiSN7TWv0ZVY5bzp20zEpcfSl0uCP4r3RTOhqGk2e_Cu85KpSMzVk4TCYd8d21xvemB3ILK-ktl_hsdKlMX6FKMPR0jylIaKldPHhNjl_N_yORpq9KUMDsUrDs-25fxykhwrrFW4YHd8CSsZpijl_Sze0hE2wkHH-PPNBh7UIvXfL_UWF0rEKE9AFfcbz3Nv2zNRskj7EKlfi6hyuqp3EpDLHgayf5NLVg46JwIbKU6gcbCYyjYOzGYSClMbeKLzxKZNui8KxH0GbQo-A3MNCjfd6rHaMBd8bsnPzy2uF6DjxLmpVo8GZYcMEjAyKuW22W5CtzUL5GGDzoKULcaZZ-3qAwnurfoFvTwHYM4sbrWbTcB5E7GCcEZ_iZMMGQLneZsqyT8FUCHqMWmcROgsZx7LJkLeN030dRjhOAJCvsNeYn9K_OhtT83DosC23OaysIiK1-VZK6mBhVrud3cjYGL58Kzkt7Oz6IBtg1s0j1oMs2DUpEl2BJVg2ZM-v4hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0JI-kxEqT7QJSyaoK5DRcs32O5v6usUohCEPyde6nysqHkzxFaXPDuDjLFoG5-4JiEHqT8wyl-FaQjgnn9S92XcSMJqqIe2T0JECcoMp-6J3ORelPBlJaXP1FKXiNdzg_8tQ_ihTzUr6BmNGat8PECj_SVSxe4FITaJW-FUcC7i9rZezp8iUbGjXlpH9KA5iWX8LnnQ2WZHk4zsk1guxXWWLyQkgbOPDCghIF0Y8k1m3jBaUOX1Y37mjoxYYrjFotIsi0nujJgZBpVF9NeROI-icJNQxf9WovhVKKfm_-iQ3JtcU3fBNh632S0tLclpdrMVMFyCwp8INr42Znw5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=ZgUOZfqMdkp9aNnbxQtXFwxT6ikqTd1ddJ3KsGk_8beawXWnkDQ9jvPDQtFPPbgkgCfVBNN4SPquqx9eIKoWACU_x6HhA5egKSC838mYC2gsP1OMEy_7UzBZ8WZqmzQHZVhCndtVKxpkMfYbgVNZgMuv8rhBu9ZgdvUGi_Vgsvpvp-6ZBNIb3sRwrNKIKI2KgWV9toS3FeETFZB2zpXRcuzIDQCLoVyQYntWM8LK20O_93Vm17cbRAY4QmZjnvaHM1ZskQElYwM48uR2C0e1qf63BOInZV_VfzF1qqcOxWfg3LUXgur--mqTd7zAT8bO6bjvO2iyH-3ZAHb68TwHxoxly1lgWf4_1ajmLLSQSVsxeB8VAaGSYyYe9ApGMUp0ah1TkZB7XcT8quokI5XJ9rLof8_B8wwo5oC7V1YOfPfuuOF4s3QCCUNsdnvsOHGDxYxLtSQiAOk0pPHmtJtS4zKPogmwXerG51lgd3kUGH-9G_auwZ64JhlkzCcuh2haZU1eIeWSZ-CazVjU8JQz8eoplLRQLssrCTMKP30xACPxSKMmtVgU5dJA3A0NkQz2W9jwOEQGbkzYkEmW5Mt8GLFtqrKH4GGINkGO7hf4UD1pQUC5Sfw3QQIOl3Fyfg7zDDEOOHSIsfAxbCLTWhiT95WPGvT9gyCf0qD5prnV_Ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=ZgUOZfqMdkp9aNnbxQtXFwxT6ikqTd1ddJ3KsGk_8beawXWnkDQ9jvPDQtFPPbgkgCfVBNN4SPquqx9eIKoWACU_x6HhA5egKSC838mYC2gsP1OMEy_7UzBZ8WZqmzQHZVhCndtVKxpkMfYbgVNZgMuv8rhBu9ZgdvUGi_Vgsvpvp-6ZBNIb3sRwrNKIKI2KgWV9toS3FeETFZB2zpXRcuzIDQCLoVyQYntWM8LK20O_93Vm17cbRAY4QmZjnvaHM1ZskQElYwM48uR2C0e1qf63BOInZV_VfzF1qqcOxWfg3LUXgur--mqTd7zAT8bO6bjvO2iyH-3ZAHb68TwHxoxly1lgWf4_1ajmLLSQSVsxeB8VAaGSYyYe9ApGMUp0ah1TkZB7XcT8quokI5XJ9rLof8_B8wwo5oC7V1YOfPfuuOF4s3QCCUNsdnvsOHGDxYxLtSQiAOk0pPHmtJtS4zKPogmwXerG51lgd3kUGH-9G_auwZ64JhlkzCcuh2haZU1eIeWSZ-CazVjU8JQz8eoplLRQLssrCTMKP30xACPxSKMmtVgU5dJA3A0NkQz2W9jwOEQGbkzYkEmW5Mt8GLFtqrKH4GGINkGO7hf4UD1pQUC5Sfw3QQIOl3Fyfg7zDDEOOHSIsfAxbCLTWhiT95WPGvT9gyCf0qD5prnV_Ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=ssFebNceRUzLtD8OFGPKdCmhTEz63wERGa8050I8uNZkktp7oDuJFh4SxIed_XTuRRqLoVJat-HeYsIgjX2MXGOBCHoilFLB3GGYhx5zKuhIbvaXxSRe2MhVVK7eO_UTkaVjQ5N-HIu34Dj8E6ojG7u3O4Bp_pBQqj51xbOevxVp2NnJUxeDrjelARJrUgk47ccOCLdojG_fIvTSKRTCiQIlErVGqvJECRsyMaJRlir7PcDqOgWG-qsxMxU1BNc71twpTMVA2O_Nj6mq77Ym7wzVBI7NeYtaIWT3tIA_ZMXjg2254dIh1k7qqm1A2T2iwAWmzEGrpg4I791GEnuqhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=ssFebNceRUzLtD8OFGPKdCmhTEz63wERGa8050I8uNZkktp7oDuJFh4SxIed_XTuRRqLoVJat-HeYsIgjX2MXGOBCHoilFLB3GGYhx5zKuhIbvaXxSRe2MhVVK7eO_UTkaVjQ5N-HIu34Dj8E6ojG7u3O4Bp_pBQqj51xbOevxVp2NnJUxeDrjelARJrUgk47ccOCLdojG_fIvTSKRTCiQIlErVGqvJECRsyMaJRlir7PcDqOgWG-qsxMxU1BNc71twpTMVA2O_Nj6mq77Ym7wzVBI7NeYtaIWT3tIA_ZMXjg2254dIh1k7qqm1A2T2iwAWmzEGrpg4I791GEnuqhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEznAW4S-lYh0cDOkUe9FjWtSEwll_x56EXyOX_qsuDgtuSUXKlaVpO_2z2OYV-RCHDnOwCkHauk1WH7h2f5_nOcVm8T6-cBk_eSuRp2GjL6Q-iNPOoWOwORYWPRoLma-dTWTwlH8Gu4eSIB-a1EhBzkWEDa9nSFaZgII34hSGsfO_znOKDPi_FUvmHKo8KFyWaB3YVDkILOUTagDSPLVZEnC1BUEy519W0NJem26rWhix-q-n4XIQjHrX0DlBN9P6zWUbR5QwLDhKk6MTl0nMA5NAucW0UN4vhIqkLEqZ8AZXhNRGdkqV7nu_UAfZ3cz8-ZzMY2L-_CnsabHjwVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qccKNwxt_5q01t_Q-EAhawrXBTKuz1jDFiFJVMp48k6yAhJ-6Cxd6FTVKXCRUDBvsT2mkQiDtUFA0dEtQLaOWcBeGSnsfUn0mRqKuSbSa_0JsvFPmfXlQt5jWNar-gbM9NQnAXfNqYeMpolTOlzEXzwWScQG9IFrLrqX9S54pU5H5-nNetcDmfnHSGLtPBp670_NBD4BvzzVocOO02qknslduBazelyCEKOhpER1Cb8HHj73AnbwQnE6MKhFCGckP7A4274r0gr1BTZHN8miHfEH6SxT22sdpvZGXIiWg3ViAI0ctThqv6aQsNImU3S5rub_e-uLhDukqCSMs69BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
