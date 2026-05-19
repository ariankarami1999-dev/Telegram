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
<img src="https://cdn4.telesco.pe/file/f3VMPlIyDI8GrdF3Rvwk9HGa5EhoFl6HI6QF07wJIC3kj3Af7oHmQDFma6-5L6wXA_a_8FlRSzoARvgz7SVcKJXMFWwQUUUEbvh5cSyLfZW8QVJeRxKMcMEVd0oBxbmOu7zIir0GzofuXfmZdm46B3QHWmOiJV7ZyXOMTp9VYOAmJg6MkH4eqFcm0Q3XqliHbM_FGx0y2OlnlIKSYAV2-L1K3viuWesKc8rB5jKXjz-e4RfbslVlznrjhoeV3doxXJwH-BjX4EbKZH7oPtrbQdS4M-LtDgLar8ysQnvEOZfcoT0rLsrkzrEwRjBGeit8vld_rweloPr488nO6DQbiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 02:27:34</div>
<hr>

<div class="tg-post" id="msg-436757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
هشتادمین حماسۀ مردم شهرکرد با یاد شهید جمهور، آیت‌الله رئیسی رقم خورد
@Farsna</div>
<div class="tg-footer">👁️ 494 · <a href="https://t.me/farsna/436757" target="_blank">📅 02:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/farsna/436756" target="_blank">📅 02:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uADSiX_tDO2nAJMzLTi3z-9o0FWqgfQvhXHZm8u7NXd5thXHJhb3rHUhAvyEcXPkRS6zH76n0zdap8XnW4HjvZSDkMbZEO-aUvYcx25UhqfchSRn455N0v0aETwKJKFvaouqswcn55_qTarrXtdniwhsnFISPq1LxqddDmxQrV9HDNNZoZLNlcPHor7PPCQInjktQpNdcQs38irDJmm9OHgzelYA0cHRqzTuetrS7KDJ5g5kRN0cwQ8ws5D-ru7nQmWX9S_GUwRoL7W-CQ1NMu509QyXV7km0gCj3j2IMfVfPd-_YDoIFyJxQkmERSeadv8HnjsxOfahsG4U1dEjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/436755" target="_blank">📅 01:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436753">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای آبی و صورتی به میان مردم تهران در میدان آزادی آمدند
@Farsna</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/436753" target="_blank">📅 01:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال نماینده کنگره آمریکا از فرمانده سنتکام: گزارش‌های عمومی متعددی وجود دارد مبنی بر اینکه ایران بسیاری از سایت‌های موشکی بمباران‌شدهٔ خود را بازسازی و احیا کرده است. آیا این هم بخشی از برنامهٔ شما بود؟
🔹
فرمانده سنتکام: این گزارش‌ها دقیق نیستند.
🔸
مولتن:…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/436752" target="_blank">📅 01:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKATwcGQTG9c1Vx8ThIP-cLBMn6EsjxPC-2PHv5777nBoHZ_aIb0irFOWSz6EgriQNSXkAMCY7jKIST2U_oDRAZd5xMEoOvS-8tiAeAt7_4Kco9XfqWhWRQkU8D50Vv1CTM_us3H3HEwePHVxB03jR6fLo8unxLkCWUXr3B91gIL_cUQGA3jTYReKPNpC2u2qRYQr1foGKvAGsU4V0ACxx74gWUsYDMtHM90-HFhhIYTPvNqXcIJrEYqwPz_r9xiWaztk59i8DVI85doMYXxW1NQkMK4HF1o_mqbLp_hSEozmCNU4EDhR2q1bkfV15VD5i19nIGCY7-mV5JXTtdtuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان چگونه دسترسی به شبکه‌های اجتماعی را مدیریت می‌کند؟
🔹
در کشورهای مختلف جهان، دسترسی به شبکه‌های اجتماعی خارجی یکسان نیست و هر کشور با توجه به قوانین و شرایط داخلی خود، سطح متفاوتی از تنظیم‌گری را برای این پلتفرم‌ها در نظر گرفته است.
🔹
از استرالیا، فرانسه، دانمارک و اسپانیا که دسترسی به تیک‌تاک، یوتیوب، اینستاگرام و فیسبوک را برای نوجوانان ممنوع اعلام کرده‌اند، تا ژاپن که شبکه‌های اجتماعی را ملزم به ایجاد سیستم‌های شفاف برای حذف محتوای غیرقانونی نموده است.
🔗
ملاحظات امنیتی یا فرهنگی سایر کشورها در مدیریت شبکۀ اجتماعی چیست؟
اینجا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farsna/436751" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436750">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1yKoE3ji_T9UVOX2auc6yvXlKGzBiD_m5dTGw1MjykXfVlHBCIu6oYuiRDvErlMD9G6uofTkh7BaXaP1f6sg1uOC-rbQdXeEJ-F-5WZGoVywIqRfofZHVf7yT2fhRLfT-44eSFClhuVWulnGxuY-FKJlDaHQPCZm97lDWOS_iNBdiFaqGnFjiScu7bJPFsgoS1B_rdUVJIwfUPyLv67KqSzX1BP1DZ4YUN0OKZWXKy9u1dmXpa-DmU0MqU_sqBuyrIV8hqaodoYe7oNdcsQ0D2ejSGIVU255LFzSqb-UbwFPD28cPURGe0DMmBWD7-oKVV3hl9Nka62wCH818_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم یک نظامی صهیونیست خودکشی کرد
🔹
سازمان رادیو و تلویزیون اسرائیل گزارش داد که جسد یک نظامی ارتش این رژیم در سرویس‌بهداشتی موسسۀ امنیتی در منطقۀ کریا واقع در تل‌آویو پیدا شده است.
🔸
رادیو و تلویزیون اسرائیل تصریح کرد که گمانه‌زنی‌های اولیه حاکی از آن است که این نظامی صهیونیست اقدام به خودکشی کرده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/436750" target="_blank">📅 00:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KatHlJQeClFJPOvT7_136Kr-eb1ZnDkvJv_uUzt4KQTaLKyrCbHcN9FJyYmzmDhFSiPCBthqNqSHRD0EDF9xIvhrCWSQtmSFSpOIC-yxYYr-E5j27VGaDwxwrCtSgsY6ouDYijk-k-YNOR2tpAc2Apap1OF2Gd_Wg86byNC9-reiWIHIY75oN_F0XpkV19ugU4HQHAZW-XGZ4B_mbrc9MeLoJE0EMV6u1FPBMabv7W2l0uKYK8rb5EGHq9Jxq2S81F1mzFOvvlmRUQ_2kPEXV7kgpSvqfwctHqXxH7T2qipAEbv72M44hKfcCh71nArMapGu4Jk9Gb_ExsvUG3iTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، نمی‌تواند ماهیت این جنایت را مخفی کند
🔹
ادعای فرمانده سنتکام مبنی‌ بر اینکه مدرسۀ ابتدایی شجرۀ طیبۀ میناب در محدودۀ یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان‌کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمان‌شان شد.
🔹
هدف قراردادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشر و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حملۀ فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی پاسخ‌گو و محاکمه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/436749" target="_blank">📅 00:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1addgFhifL9gbk4lTWS2H79w2YyQ6eQwhFB3V2_vXZpY9BQ14EuWM00hiX6Xlzsi9VAO_n0_nY3hw6tVS50xon1yR0ihHzAIc7Vm7MB1ll-2xzwK-d9ki7k269CXvHtJSGmzvJK2SNr2MUEuLcRFxOSZCyq53Cc5WL8Mvwz3GumrX615CrT1Ix0fFR7TP5EYGc-xdG_lOBLffbkW8N_Htoq_gGWyyrVVQsaK6NLKZrMqAiSwcN82lu_dl6cw_o7GILpMyNrfJVhrR2gak87bY8bFjW_nURnVBgjBkeFL8WBKABs1ksDyFe7T0kTrZMJ4ifnGgzM-T9AjhrfPUHe0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOySjoTBV6RHyhnczYXGfKJZb7hPZEYZr9GDpZUP3oZnCg2lfvW_JBD57TXh8kTefg1-8NjzHQlOjMhNB8e-ALJ5acsdIUs6vU5obe0cPJLJQ-AHTZoK84o7Ppb49d-KJoHODF2Z5uzf1RqvjfS7d_L8uOIXGtYP24NIepAYb7I7K2GsJM7Nfdr4a_joXazU-sKBLztiXGIj2WMv9uLQAPNqZe4fHWJPj97pTNNEq6sg5tOOmsqk8itf77DCmg86y6oLKHnNcKGwC_VxLhTwSIg3mov_H3JVocEY7-ekmavrsMC54mHxbRq-i5GfEWsgCyC9lmrSc8EwaaKz29s4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxPLivhp86SxO6itPDG5pLuVbwM0ffUGZo5Vj3kiga9Wvibxfrol0IzWlWM6wTTkDTS3HF1jDsZ-nm8zdqLa9fTRNItaDbD96KVAoLFsE3NcL8josKYkm_lCbpfE6AxXX4mSmgMu3VhA332ebo1wxjUOCGwB8v2hKt1o9R59FodJ8Bf4hqXpFpNrWtzPl_Jy4nROfww2W2HRfj3gnMUVDnGEtQD4N2y68zgIKsK3xiIbt9Cla3FxGZ2_UBteMCRTcMg0WfMThpI4vDVT6LzBAKran6TTlKZ6frozEyygwwQIsV7DkWNSmOxx3AqPlCOYsOm_OKAYZ1o_74PUoRyA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsJx-rhQRnoaH_NJraEfYEcJp0_czJ7JVpaGCOGj5NHpDDhoV7gqX_VNn770VXd-LNR4AuBALALIVs_Lr0Xm5hCHd3GrfaD6eHKYGTmJuyT-EAiKKJsZ3tEnPCUNnfiQ5DUJJy-azWOVD-C3AB9OJ8tAlcPjEHWE7bz_qdkVsxB_J_f8uIhGrCvkbC166TVeGsa_XpXvOnYmFBnfDohmXuaj7AD-XmWSFS6ehKk16_FXn7b3M24tuihh2Ew2tbEzgdv6qF52aGgOKVks2StbTcF_pe-82A8u2OAyL4j_u3YyhxnLHVEDSaOWBEMKqlsb_X7-F8UxjyUSaU8n0HMmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbV66PDLKtrrRnGwZ9yKgzxGBnBhuQSkp73xL8PTIumiCWSzDiqJveu293R5THLWR7mANdfU5lJosXw62lYtcW-X-4PH85nhg_Sybv5k9CNMVPL3Y6m0tniJRke5mtkg_3RU3ksWwIZp5fip2ZhWAsrrnUZoKtMoY43Gt7QQh7SRRFnET73C0zrx2_VRhiwAVhGNg9VsAEMjqVWgwbSl7wLkuk5AIz62hHcvh3yImk2hFzhf_LZ43IkVdGjvBbqZP037_JqNN2zHOy42-4LIsxy7d8O4uq9etJwHkvxTVczPgSsW74znDsghhxXoeyYIpqBop-6Px2iInQeBrrO5HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۳۰ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/436744" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436734">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idhJGjXSHhepnABW0qK0yJHvJ-SJxyVaHBMeGlufbxOd_96OKNXWStX65vZSpX0Ugd0h_V5B6TvSsscf6csmpYTOhjR-LJvBDB_50MwzAV6HCpMF9y_io4-Msx_7dYiEboHxXjU1Bjg5RA-eykCeqFDqNYajvucV1YobMSyjI1u5RRKJayPhwJke_-Bj2OGmMEpyM1MTbdgpC_sUKEqiDPTac0wx376RWkHhcfBEkUD647cTqsD5QxtIbX7bQWz71eYtVfV9hyBouR-oe1cCXvNR65qauSGotQAh47yue_bmWup0BqofruSmBwDxIiRwdkJN4Mkz9D6UivzXHk2N9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSI9sYh0vmjYI2cRENUjl7M51xkttiEycH9mKBrdJ26tnqHMhJHPLp16BeBcQPbgmvPWOXRgn3QoJAfQJgGiYRl_Eb1PzbPrPH6C64HMdRFsISg543pacbdkA6COZlEXGbR6PaqxaFm2_sZPAnHd36KU1OIn5fks9_n7AUi_bdRQzpM0RqEPjBVt0UnrV2v4JR-TnsOR9RbogHt53vvo33dGJwj9euTqmLWv5W6W5g1rBLAjEqwL08u-ANbpH1Bakqu4lRZ3D6n5x0Od5vCzWdwrWiUtuqkOFWNPKYw912_EVRNFPqbrF0Q2Fyn9tnNOo3MYT3uEmflUtk6v9JaqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHuir0XwGvQ-uajH7W2fY-DB0NFSdwrGEebZhEMDKc0en9FbLQND-eItLyaTs25TQeHgqe9J36vZZeVtxt2XGLh7A3akwwcyAn-dN7pxQfN5JWDW-gJlwExuvGPnTmAKCjrE242YhgcuEPb2PgoGR3Iry3-poxal4zs0DzRgaiaV7XKXPYU9jIEHxrFJz1dHSprRr-CPY6GX-l97Qg6rUYqcsd7C9pR1Htww_cca0azaCHWF7ag3NVKu7dx6BEb95ry-Lkloy8fyU7pprFyk3AydqeK-a4Nvg0TcWqe57X5E-4pQy0mJYEx_6Gq2GsUBoIIT7sI1FzAp7pZdi6gDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sItLSxJOCB8AmO6cF6mb67hfWt88QmD7EsCN1caqjb-uRt-uqV_e_BSGCVZyard51Xyd-Yyv463VG_-v34ggOiy3PYflDQJSs6ev9PngfI3rT6ZGyZG_XQNSIq8WDt82MWDhRmjVKF1Ohim0jnvjtzMbeYpWWcDi5xL9bn3Pg0v0EkgUamMdJVI3ONnjgMRmdqRqEtzVfBRT60xVJakiBReadx51IxeKPIdSjHdxtEmzuZO_RhPqBsXzPp8KBGZlKCg_CKxJBTh-QhtLwesBuKwzNjUJRKTfxszre_z6_zk28npFAke4BQdPh1sCrhNWKZvIVPp3qqtpz8OA9IRvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alrJCZDmlBnw9C8yibqGbyGbA3DHDUNyiZBCS9fDZEvm3tHJVBerOaJgBz_KFUW1FRi3ueLqSYvRNZ5SbpGydm1DGoXF2y_T-l2Q3k_0_7UcW3d7jvWZwy9jVq95nIWbJv7lGWZsGPxhhIE_DhumlnjlwsGjnLxml7l2hzXyRBpjJL2tZEYYhgu9VRgZBabidN4zvXOWXhtU1caf59WAJt1fwUk3h7IjoKxoVRtJiz2obYZgwA_2eVaH9_9vnDgj4OgQib3MKtdUZFnSYkj_RmSiAnuWexNjYOzbP1VdcoH_ivTSku3WC8A7pk1Vb1cuq8wDf0_SwwgFAaWojw4f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm4T6xpn3Lj4KyiDQ1p_gPlUJuo8juhuaIuajQSPo2q6eoy64-inT7MerBjuXenx7OufR3jsiovw8wJAN4aDp5dDRpDf6VG5WEK8RHgi-y-XCxSV_p1lOLYp2vy2QO0sT_wSgb0v2T5gsUstrIZiteZ31FBER2OoLfVUyjRLixzLsYfK6F0bLeoYhsmW-BgYa_EzzPYuCqLksSYT46kOlLE73jdLariewpm3qhEBA8wK3_KRs1J_ABf3Id4LMPQ4k_LwH59MoHVPNbG6ac6hQ6JjzsIHtvFL5M2eBgJBHxC25PZwN7NN4qw2miaC6effQAzDnOgi_gtYt-FEAJHXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNYaLKbVA9Zx5ZtRxP-u_eEACeVegrCZNcODIyGnM1AcFTRZt0HWsZ_M-D5BYvpdaa1LRWX2ugCAHEZtApdc2o0V0B73TJZR84Kl78kwDUT_HTdwo3VdpctAAL63a54CrLdaYS_P1V-TpSqCnG9aCMEuwIcgJqhQ8njzq--P9tybxgUqDM_4MLGzXogaVp1nmy-4vyerXUOr0PumI2hqjJPHdREDuIlSWUgnbDKeDCd6NClNCbr26jFcxTuxWE236A9VSdiOXVbQcPaTIzDuQWylWCdbbBZoIwE5YUPoltfRVxSP5x6G8OUF2AlMSWvOWCQGpesNZJFM17dAvQ2X4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9mfMr7jKxt47WVzVbBi6N8-MU0B9DHZAdN7DUky_fdsR0oSmjai6bRMiCPcAdtgoriAgyhRfRxM6MrmiBjDhnE9dlIbFoOnhDzlWn1Loy72zNCP4uFhrcubCO54LxJYSuGFQq5-qUpMp6JMfEPWGwOaZjW9N3RWMAI2yv3On4XTdqWpBJKZ2rmSGvoHyyWonBbO-OFhnPMwgCSTp4-d26i9U3zBKTdHP6QTDt_LsjVoE8-_LhZqre2FHJEmuRuZBCXLpsd3gG8fPoiS9saSSr0gapBd2bG1Y-f2eP18AkQwY-kYXb52RjpR-giIMjU2EPt5Riibk1KiFc24ESiK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avLlhofhcd8C1cIHVG_-Lwi2m2VWI25nbr7K71yqU7m4F_EIzoEP5G56pjTKPIy4TpMa8uG-ity7WWXM-ajtDtNHlncz13LbkNR3JdUhyOG0lat9BpWo2xCZVoczntwZ0zZwyWtdl53K66nsrWfyux5uovqVIv_5PpAZqkbB07bhlrWEfBx8DtUBOAIKybdvEH8jYo4hnyocoSyp0-zW4cGMru6kE54I-ZcS0YWRQ21NQRog-3koMAmHfV4loalBVT2XdRgMgzOLY7SzIa5irWA5TomR5Ac9XKswhbpYds0JCIdP_TuHCm_z5jn6sbUF2wSnXJMg-rbpVl25z31pgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2hKt91MGT0QLtKw_OpOtDDoN0u77y_T9L5YFn0Q0tJTYxfd-EdAJgGBMbaGQIAHKZ8vSH2PaWgedzWuztNc1mv3o6xoFtQGcAgi4imbXMSGH09JVCGoYLqrtGXjTdJAiPVvtKUv757UHpQe_5LsHE55UtyDoScGiq6KR8uOB2sxJqiCZQ4XCSbSayKjoid3szOoo3I2OE6cN4-Y9PhINjWyQoteOGmtDLFQf0fyCOHKvmj6z7_H43wqgV9wRl14qEZPdMXtJ1n5V7fX9osqkvgTLM3GbRyXuAoQLDFIq4DFRIscytlI0FD-B524axYqwCu9rwF5Fxa3cfM2Ta55Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/436734" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436733">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2eFuQr2X1UJBbMXdlI0mjOCTMkBXQaFx1upQy3ZoCZ6cvbiMLMXqh2M2IW2lSWy_lIsoIrBVR1YY0Gd_5c6HJ2cCvnXQWBrikO_CeJduuuagV-iYYXYEVzfv0VdrARaxnr5--_FMV4-5t1ooIReb8S-r789eepncIMYShMfFEB1L19GZr-2p2hmq_20Ep4Bu7yskgPsWpJ1w1cdfWPZWs8rqLv4w9myV9dujREZ7sD-0cyHqeNmh5LKaCd3asP1AdzQdvAPrFJdYSJbSpVJA6WI7rC4MxDbw8xmBfYlYuwxp0Suyu95T3B_9pyLcJx-XMaz_qYhJ7wPEeXPnbDiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کنگره از هواگردهای اسقاط شده آمریکا در جنگ با ایران
🔹
بر اساس گزارش‌های خبری و اظهارات وزارت جنگ و فرماندهی مرکزی ایالات متحده (سنتکام)، ۴۲ فروند هواپیمای بال ثابت یا بال گردان (شامل هواپیماهای بدون سرنشین) که در عملیات «خشم حماسی» سرنگون، منهدم یا آسیب…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/436733" target="_blank">📅 00:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436732">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
جشن تکلیف دختران بروجردی در میدانِ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/436732" target="_blank">📅 00:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53d3cd232.mp4?token=ikeqy4OWld5B6Zjixr8nWNRi0o4SagXq6KEgcbriZV5Hf5pEjUMlYvQ6A0jh1k9OoTeQnejFmGzHzBwe_Poj8vfdMbEqqiF_4tmL2S4WuHzIuX41TB2vGbZbKPI7n4C1h9_J7ylDgJQknV5yvUAkI04RPpccdB3D7wcpOfGNbPtFfCPrvD58SMJPaNUCsJvgviG3ESFMeRkiiQrREvW7o9YJlBGQsQp70WujDeihdW_gCo7rcJBPQN0kU33OWlQlSJ0qec2L7iCh35GOCB2i8oF2vCK63PSvLFDxWQkygKO-eGWdmf2NtZLqq8DlRY5QY-_KNOzSUN2d9aDVlYq-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53d3cd232.mp4?token=ikeqy4OWld5B6Zjixr8nWNRi0o4SagXq6KEgcbriZV5Hf5pEjUMlYvQ6A0jh1k9OoTeQnejFmGzHzBwe_Poj8vfdMbEqqiF_4tmL2S4WuHzIuX41TB2vGbZbKPI7n4C1h9_J7ylDgJQknV5yvUAkI04RPpccdB3D7wcpOfGNbPtFfCPrvD58SMJPaNUCsJvgviG3ESFMeRkiiQrREvW7o9YJlBGQsQp70WujDeihdW_gCo7rcJBPQN0kU33OWlQlSJ0qec2L7iCh35GOCB2i8oF2vCK63PSvLFDxWQkygKO-eGWdmf2NtZLqq8DlRY5QY-_KNOzSUN2d9aDVlYq-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مولتن، نماینده کنگرهٔ آمریکا خطاب به فرمانده سنتکام: مگر نمی‌گفتید که جنگ با ایران طبق برنامه پیش‌ می‌رود؟ بسته‌شدن تنگهٔ هرمز کجای برنامه بود؟
🔹
فرمانده سنتکام: با کمال میل حاضر به گفت‌گو دربارهٔ ابعاد عملیاتی مشخص هستم.
🔸
مولتن: پس یعنی شما اصلاً این مسئله…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/436730" target="_blank">📅 00:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ISQVjhJJYxqeb9k7eMVDjcWxDyl7eajLVXRJ8jORfzlPKsp6DrT9YoxsE5uf23XRD3q2A4ONs-2JwbdJ_MJAgq_o1w2TOasEz1C70z-_fUmJ9r_uMoS_XU7Z8SJiSK2lFKMMFNPpKEASS9lOP5VGt3RQrx9bmMSYahNViLmInrR1XqSsLFvyeLPXqp8Zrdi0-tvkYWAaR0Yho-peCOktaUpZeb_s-Ms383OUFayNjZyR7aAl7mXETpDs2xuZbFkY8djMg5W8Wm5SpZKrp98977qT-HbtbDdn65JS8WvmGNxRopB_YTjCi5wvp6tDxaWeZlbcuERUbiQkcHZ0GHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: سابقۀ دشمنی آمریکا در قبال ایران، بیش از ۷۳ سال است
🔹
سخنگوی وزارت خارجه در توییتی به‌مناسبت زادروز دکتر مصدق نوشت: مقامات آمریکایی بارها از ۴۷ سال تقابل با ایران سخن می‌گویند. این روایت، تحریف عمدی تاریخ است.
🔹
دشمنی آمریکا با ملت ایران از سال ۱۹۷۹ آغاز نشد، بلکه از سال ۱۹۵۳ شروع شد. مردم ایران طی بیش از ۷۳ سال با فهرستی طولانی از مداخله، تحریم، تهدید و تجاوز نظامی آمریکا روبرو بوده‌اند.
🔹
بازخوانی کودتای انگلیسی-آمریکایی سال ۱۹۵۳، درسی روشن و دائمی را یادآوری می‌کند: تنها راه مطمئن برای حفظ عزت ملی، حاکمیت و منافع ملی و توسعۀ پایدار، پافشاری بر حقوق حاکمیتی و استقلال سیاسی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/436729" target="_blank">📅 00:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436728">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f035ee4734.mp4?token=tUhrv9YI58_4gYqssyf6khFZ0PM-JE87mHSJnBVBX1L_Tx6Q3AsJM5440wugQiebI-aRJ7bi80HdhJM_k9GNLiH11cZb0MgITNCFo_1bkFGzaxowY7X3otP_wAz4yIrc36SOw3eIC5MzAQfosHPPV6u45XwGnTNUAs9TpK77n6e-nMVgsSnDx_4gy7OBjvqY7WihqawaGmlzG6gVppNAked14zAVSFcLc7m86Q6r3h4n2DlVu4m8jcILtBFte6glSyvxdfbDlrSSV6TpJU9r20ROCQaCOsDz_XwsTEE8PlZg34WD0rKQRpiG9A0NbhaCsSAqpoEVsIX1m-zAmZBEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f035ee4734.mp4?token=tUhrv9YI58_4gYqssyf6khFZ0PM-JE87mHSJnBVBX1L_Tx6Q3AsJM5440wugQiebI-aRJ7bi80HdhJM_k9GNLiH11cZb0MgITNCFo_1bkFGzaxowY7X3otP_wAz4yIrc36SOw3eIC5MzAQfosHPPV6u45XwGnTNUAs9TpK77n6e-nMVgsSnDx_4gy7OBjvqY7WihqawaGmlzG6gVppNAked14zAVSFcLc7m86Q6r3h4n2DlVu4m8jcILtBFte6glSyvxdfbDlrSSV6TpJU9r20ROCQaCOsDz_XwsTEE8PlZg34WD0rKQRpiG9A0NbhaCsSAqpoEVsIX1m-zAmZBEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔸
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/436728" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc615f993.mp4?token=giyESIg_zX51QcCjmWTzLdXOKKz2rdGbxvsR3Ut7j1KpfGrcQzdnOuOkFV2V4Oa-4y-DGoItVjIaYab1ukNpX_s1x5gsYoPkQRqgxMBX8_ZPofFZVpyexskETY81DXa8MJ68eeATjE71KOEZAX-WZDlLJk3gdm4Mnbs6xv1dqvd67w-lcBOXGFSmw_ikWAUzAuP2T0tZgEHCzBaKS8NSUbB8AoS-IKPCjndANk4YE3PT1yE8fBm7X7FU49_PmrTfsJMbisYxEIEQBuUaRzhnbwIDg7qtl6hkGX_pywTE9xbJs6lORU2yOSB6tTvXAjNH7IxM3fX_P-XsfCBqtmuPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc615f993.mp4?token=giyESIg_zX51QcCjmWTzLdXOKKz2rdGbxvsR3Ut7j1KpfGrcQzdnOuOkFV2V4Oa-4y-DGoItVjIaYab1ukNpX_s1x5gsYoPkQRqgxMBX8_ZPofFZVpyexskETY81DXa8MJ68eeATjE71KOEZAX-WZDlLJk3gdm4Mnbs6xv1dqvd67w-lcBOXGFSmw_ikWAUzAuP2T0tZgEHCzBaKS8NSUbB8AoS-IKPCjndANk4YE3PT1yE8fBm7X7FU49_PmrTfsJMbisYxEIEQBuUaRzhnbwIDg7qtl6hkGX_pywTE9xbJs6lORU2yOSB6tTvXAjNH7IxM3fX_P-XsfCBqtmuPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر لُر: دشمن ما از وحوش است و ما عاشق شکار وحوشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/436727" target="_blank">📅 00:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTv8KAwsweUKPvYOjhvHjcvWLbJdB3tgFD_SAPAnbi2rkv-MWg10fD4_GkhfjCdaPs4xEgCY7O6weQnXonD4CGzZrCszuvcFF0w96KcJ3L6fpjw2kQUhWSwn3CQo3SvQW92s93SM7u2fnSAkERCgY26RPWWz6LKK3hLVK8ja_xIC9FxUNX2IEjTecIoS_FceTwIY-xWHm9LkweRW9SbbGOg4d_2Q1xBE5jaz3nhpiOEoXmsLFpXIggLHGqwqZyAjVBDF-6XmTd0TW3KCREJ57B2B0rs2k5CiN8WiSAVbrQDAd-9-1wNv_cqiE-V8R7wNLGAV5ykZIvj02QyEHgWRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به هر قیمتی بالا نرو!
🔹
روزی بوقلمونی در مزرعه، در کنار گاوی ایستاده بود و با حسرت به شاخه‌های بلندِ درختی کهن نگریست. بوقلمون آهی کشید و گفت: «دریغ! بسیار آرزو دارم که بر فراز این درخت بنشینم و جهان را از آن بالا بنگرم اما افسوس که بال و پرم را نیروی پریدن نیست.»
🔹
گاو نگاهی به او انداخت و با خونسردی گفت: «چارهٔ کار تو در نزد من است! از فضولات من بخور؛ چراکه سرشار از موادِ مغذی و انرژی است و شاید تو را نیروی کافی ببخشد تا به آن بالا برسی.»
🔹
بوقلمون که تشنهٔ پرواز بود، اندکی از آن فضولات را خورد و با تلاشی بسیار، خود را به بالا رساند و بر بلندترین شاخهٔ درخت تکیه زد و با غرور به دشت‌های دوردست نگریست.
🔹
اما دیری نپایید که کشاورز، بوقلمون را بر فرازِ درخت دید. او بی‌درنگ تفنگش را برداشت، نشانه‌گیری کرد و با یک شلیک، بوقلمون را از آن اوج به زمین انداخت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/436726" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a54ba1cf.mp4?token=uqoNEa_YWMPR9YEq6z7GuyDoB7XGMJKwaK0LbLmDfXBh9bJOL3rVX5g1e5RoKJRdTA2Y6LUtcTi41_7l-igJl8I8aB9R36aLWBA65J1a9Rh_GgW47mo5HBBcxxJBXqOqDhC2rCJQADtmJyNzzbrM2L7oKcv5zPddQIXPHX8mPaCHmMqsVB6f8ERB_Vvkny3wUdQKD2d8vj6Tme7aP99J6ei64BxDs-0cXXmkx3-ZyDMdbcfGaggSh0WEarEw-RCO0Z_l9SpQWm_WR4Kjuel6a0SCoyEC8s9JGPKfOEFocXzBR6p-XGHAszExCjwYfHq6faTv24D6-wFpriRzru3zyzKgFzk6_pZ8qT15X835qVAU9hfwf7A2qL6Aeu-g6FwNL_qXGnIFkaeH-1FOZbxwGbtGClRZmpHEo8H_j2XUMPXVbR7CZat2VgnDl46Iu03UJvzlijn9x4UEizCLkZeaBCfJlnFnabar7M7edTcEiLcoq4CDEz75rfg0GcvXttW5gXKYvkTYl1J5TCXE3jKMKEC8Tg3JqoflOiaVKtrIrnlya4LY-NOVV0GGEaIpmVxxHUwqwFkxzTBYLwRNVwJw2qDKvYlnR-ggsRAMizSvbYngyvODG6jOTPT9HeIxy-LKjKhzqAoMBFc1CupxUFav4kStMQc4YVvNH03TVtydNFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a54ba1cf.mp4?token=uqoNEa_YWMPR9YEq6z7GuyDoB7XGMJKwaK0LbLmDfXBh9bJOL3rVX5g1e5RoKJRdTA2Y6LUtcTi41_7l-igJl8I8aB9R36aLWBA65J1a9Rh_GgW47mo5HBBcxxJBXqOqDhC2rCJQADtmJyNzzbrM2L7oKcv5zPddQIXPHX8mPaCHmMqsVB6f8ERB_Vvkny3wUdQKD2d8vj6Tme7aP99J6ei64BxDs-0cXXmkx3-ZyDMdbcfGaggSh0WEarEw-RCO0Z_l9SpQWm_WR4Kjuel6a0SCoyEC8s9JGPKfOEFocXzBR6p-XGHAszExCjwYfHq6faTv24D6-wFpriRzru3zyzKgFzk6_pZ8qT15X835qVAU9hfwf7A2qL6Aeu-g6FwNL_qXGnIFkaeH-1FOZbxwGbtGClRZmpHEo8H_j2XUMPXVbR7CZat2VgnDl46Iu03UJvzlijn9x4UEizCLkZeaBCfJlnFnabar7M7edTcEiLcoq4CDEz75rfg0GcvXttW5gXKYvkTYl1J5TCXE3jKMKEC8Tg3JqoflOiaVKtrIrnlya4LY-NOVV0GGEaIpmVxxHUwqwFkxzTBYLwRNVwJw2qDKvYlnR-ggsRAMizSvbYngyvODG6jOTPT9HeIxy-LKjKhzqAoMBFc1CupxUFav4kStMQc4YVvNH03TVtydNFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمندگان هوافضا با ۳ پهپاد شاهد مهمان تجمع اسلامشهری‌ها شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/436725" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aud5vu86R8VT-f2D6DVrD7aVLZim1IDa1owrBr1obS5U5F3p1FRjlZ8oyIFPBVPS0QmiagNjZki4pGTOGmzuziFzhOWPBVL7gNkeaSGw4ln77iwP71pHRx4brGXkJ7gnN9MIIL87Xq8hXZYTvy30NRpWqyExc30dViRU1upBgzY2xJrp1z6G_y7XH7An2YSucLp89sPg1tswnllMkNCK6U16SZkvw4JmeP8r8m-sowbKUtOmk5AD_JcQ0I8s3SMY-UbvjSQX8mI0FpUXZx1XRoy0XhAjZJFr5rlioQdnls28euFzBZmruJDrBjoAGjTiYuPnmu6WeAtvsh3BRbp5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع تراکتور به پرسپولیس بازمی‌گردد؟
🔹
با داغ‌شدن بازار شایعات نقل‌وانتقالاتی، گفته می‌شود صادق محرمی تمایل دارد دوباره به پرسپولیس برگردد.
🔹
پیگیری‌ها از باشگاه سرخ‌پوشان تهرانی نشان می‌دهد که اوسمار ویرا هنوز هیچ فهرست برای نقل‌وانتقالات نداده است.
🔹
البته پرسپولیس حتما به دنبال جذب یک مدافع راست در نقل‌وانتقالات تابستانی خواهد بود چرا که ضعف در این پست، صدمات زیادی به این تیم زده اما این‌که این گزینه صادق محرمی باشد یا نه سوالی است که فقط ویرا قادر به پاسخ آن خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/436724" target="_blank">📅 23:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwHnmv9EckI45hQ2uHEST8Jl71ev0mX_TafVykAE2c5aWdCbMdyo15vomFu9LUSo50vqsZahE8FwoDiRYcxoCJ4fBZDhxoPK7ZPvbN0XxtCXOSPwJjGy-27LTBDvVtYuwHcVY6j-PP29ucsq59Uv1U3f3kUSTKlrJOgNLpJv3kqPJSZAOsFqe4ho3Ia2yE8TYycy9_uK22txaaJ7ErMJvhuwpi5CVBferY3qpnU3GX4Nse-o1nhsQmcxyOSvHTHi03ziaP1TN4YCPaznrdssdJgW4hpgA7FYgLRv82pBGl2um_E5R0MtbSQmKlI4AYxh36If7f6O4sZxnj1k6-RTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان‌: آمریکایی‌ها برای کمبود روغن‌موتور آماده می‌شوند
🔹
سی‌ان‌‌ان‌ نوشت: قیمت عمده‌فروشی روغن موتور در آمزیکا به سرعت درحال افزایش است و برخی از مدیران این صنعت درباره کمبود قریب‌الوقوع این محصول به دلیل جنگ با ایران هشدار می‌دهند.
🔹
آسیب‌دیدن تأسیسات کلیدی در غرب‌ آسیا و بسته‌شدن تنگهٔ هرمز دست‌به‌دست هم داده‌اند تا شرایط بحرانی شدیدی را در این بخش حیاتی از بازار نفت ایجاد کنند.
🔹
مدیرعامل انجمن تولیدکنندگان روان‌کنندهٔ آمریکا می‌گوید: شک ندارم که با کمبود مواجه خواهیم شد. اوضاع حسابی به‌هم ریخته است و این مشکل به‌سرعت حل نخواهد شد. شاید یک سال یا بیشتر طول بکشد تا وضعیت به حالت عادی برگردد.
🔹
در یک سال عادی، تولیدکنندگان روغن موتور قیمت‌ها را حدود ۷۰ تا ۸۰ سنت در هر گالن افزایش می‌دهند اما از زمان آغاز جنگ با ایران، تولیدکنندگان قیمت فروش عمده به توزیع‌کنندگان را ۵ دلار یا بیشتر در هر گالن بالا برده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/436723" target="_blank">📅 23:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZJIdhQ8ATfPvnR0O0yh0SKP5NqVXgwuPkhFRTuIwonB40lliIYyqIuGZt7VUIiSucGFZ7jJQV8vpMdD84glJx6Eeu5Z41ClLgx5KdAaCGpVIQQyNHqzTICM3ytdBztBbLO_M0XbBcIfvv6ElWiNY34quF4ctEFSlhQXhF7A1ASqCv2Lwu2xslm1QaeAQHykdKpaOYQ7wiqqd6-3_PqwJxxu5SbykEo7DkiBmhqk-S-cCMxuKd4gPBNlmsC-CmLxxjEdJ9SadNYIW7gE4eIXg96oaiUW9J0ycjng-KLxk2VcqVyakAhmg-zhjVwHhBraP6gH226C6eJOOWtL2EIlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0F_VgnU1O5vfulmVLNoe86xBB3n0yF7jadUQx-HAkGgfjecwdfFrpSjxsiig2U_ZZ4ZFP8Fr1YqBg2P5iWWGS6zcAFMK3LlCGD8MyUsZZtHswe0qb02Dm2UscoUsnmrvhslASVU_rnAWiOtj3a1QWAf3jPvFdu_PZKEl0fHQdU-6bRHkOYCxGvb_wnT1P4MxclQhnIbJEIjC7WEIx7uxfwpwFhQ2i_TBawCPZSI6MgGCL1-Lxt6eaFKzqOQSx9acuWTkwUoRGYZnhMn0f9Q9FMJq5vuo4kSqEzIgqroandL-FEls2aBS6fvj_2jZ2bUruNGCeu03H0i9iDinvPGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvBGNq_1lBkZk-9V9MWg1AZ2nmXdcZE1IILOcbHlwDqfbfif7yUbstG68Dljj9V5zoGZ_3qLd6i3tqhr7R04eoVpYuJ68XUZUvcw8eAT5OnYI_yRgamrEanIvZV3s_5_hCkMq-4sziTSoUxkkgd8rhvmS1ixIQalqCpA-LWTMdNS8s4VjVkrLgoeMNnTA7qUImfNFc8gHlk8dkUmcWEM2W7Q3grvSDC51eTsxX8kR3LYKHgOfYO5FF69eCaQaJSmq_AMwJvl1iPWrnXycsGRrVkybE8FsD70WVyO53ExFbRo1jZpLnRmtNbnZoUbAqaAPXg31h-RBbFxQFHi4UJHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLqBNCIv3doMM7grZDtKf8r9h_vImbpoqZH_5sJjzVDJ7AYHvJ7cegd2CR3nbRdBNvb8M2I7QCo3d7qu8r1Ys5CBCrzLSoPnK_Yd4tTxO5kwBVxk6I-gG1_fx3-mxY-5iAWxPMaynB5SN7CPJllLINZz0D0sKdzVdifGCFNYZlTk1yg1inna4YoCsAsLASsl8K4JyA7xtFw-gENWmwwJl-vhY4vn3SZo1pqSdNtBkMD_ELH_RHd16e3kRJhIgPrbueEnDdpqhg9z7SrXrt5mZT-RK0vWHTlmPYXS4NqmHBcG57tIRpEO-o77oJluAJjtquuexh5sVS8RuD2K6ZPhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9zn9DnnxW7FbBzn14Dqrt5b3INV678X2MMANy6m8o6pA6BSd_ezR_T2WU7nnXpyuAkcJQFxkexknjlwfaHlOlTy52fk3ovdAWxB24zh1c0vkEPjeQeaK4SQa39YDyJObjSN0CkOc3amxVbO4LbqI1lzRV12BOSQJPcTG_6jmIvlkcm8iGtLgjyj950eHc87x0u9jr5ldTwAj-LwooalHCqaO8b4PRZVHE9l_LEnalqsUaupKR2UVj3oz10WyFRB4XI9JZCHQDMd8NO28zoxm5Qbi42VPYkISi7onur2T5Ua9qD5NbZKa-gsOcvebTbuWu40tyLK9d0-lCS6gmrDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GG0R2hT8OYxDPzbMwOATIkPwXcA8X0weejUJ_2myovQARip_uymXZZzFEWwrE13ecfF9C1I_1aOdbEHowjiNPztWFNFOt6PffbgJFZ_llGSHP2qIjVLq5vaaeu2Z0mAGZtZ3K2QjKuIoe4X6EGbMPyWI_ibZtv_jUJA9sELg1DQtSN8VO_VWFJLGLsbA9Nu35NoST8CvTM1RWZygRcnYbbKGm4uxPlVZ_wbt3y19E9CZDVjBVqspgCeDHk0iWMdyQfcRsrsn7KRDlWRd0CajuvkRY-ctkG0AM7XeS7KAhV6VMsV9hnIELOCZDgykIcHN9QDt_BFeaWSm7TYutUs4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kikDM3pDpUca3jH_ccL0hNcUlen2xCwov67ZWtPkC92SD7yaetlQZB8BCteqPNMbCUmGbtPiMbCXZvVc6e5Aw4wxvoFKhyPrCTy47jG-_fTg3-NPKsvSSre8YA5MAQm3IHEE19sG3-u_pJaCw43VLPi3R8xLDX5w0gyU7KE3fWhHpEThMiO8-aqad3OZHZ4xT0tCrNpORagGyBW55XDYrdNZd_9czOnT1Q06syF5OI0dMenKnyUpfuqJCl-VwoMTAUE-WdLf82dUVR_JTOfW45CK7S5A9URMWSiUbVqFnk22UoxK7Mr1sdS_xL5HMjS50J7O7NQ8fI8A7RoIfki5qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت دومین سالگرد شهید آیت‌الله رئیسی در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/436716" target="_blank">📅 23:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af779788b3.mp4?token=B_ZyjC5iD7f6HMdrIJXoPgF2f8PccHDxsr0o2dcN5-gencNBpL3JIq4OMr_AGzcdSuVgtrCTfAi80qJFN6DBCtptvqPHn-FmE02C4MmdFNsFusdWGKKqdqqTh-a8ZbpDf5-N9HJDM2VpxBjsdf5ceMXxL1Rbn4zaWGvpd-hZaxB5I3ctbq_zqmLadkg8xGkSROVATTh1tojIlR2KYymjti94yD8E9N2A5KVwQrnKCxuvfKIjjl2C4QwaMoSSbJ0PEHCPKqpiUUNwCom0OAvHciTsDeIGDG0mRCS-noqgiJzsgVaEnodLNwtaoKQ7SBS9eLg0P9uxDFyeeNOBb0I2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af779788b3.mp4?token=B_ZyjC5iD7f6HMdrIJXoPgF2f8PccHDxsr0o2dcN5-gencNBpL3JIq4OMr_AGzcdSuVgtrCTfAi80qJFN6DBCtptvqPHn-FmE02C4MmdFNsFusdWGKKqdqqTh-a8ZbpDf5-N9HJDM2VpxBjsdf5ceMXxL1Rbn4zaWGvpd-hZaxB5I3ctbq_zqmLadkg8xGkSROVATTh1tojIlR2KYymjti94yD8E9N2A5KVwQrnKCxuvfKIjjl2C4QwaMoSSbJ0PEHCPKqpiUUNwCom0OAvHciTsDeIGDG0mRCS-noqgiJzsgVaEnodLNwtaoKQ7SBS9eLg0P9uxDFyeeNOBb0I2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگره آمریکا فرمانده سنتکام را سوال‌پیچ کرد
🔸
ست مولتن: دریاسالار کوپر، شما در مورد ایران مدام از عبارت «به‌شدت تضعیف‌شده» استفاده می‌کنید؛ تابستان گذشته به ما گفته شد که برنامه تسلیحات هسته‌ای ایران «نابود و محو» شده است. آیا می‌توانید تفاوت میان «نابودشده» و «به شدت تضعیف‌شده» را شفاف‌سازی کنید؟
🔹
فرمانده سنتکام: جناب نماینده، هرچیزی که به برنامه هسته‌ای مربوط شود...
🔸
ست مولتن: نه، نه! من از شما نمی‌خواهم درباره برنامه هسته‌ای ایران صحبت کنید. من از شما می‌خواهم درباره زبان انگلیسی صحبت کنید! تفاوت میان «نابودشده» و «به‌شدت تضعیف‌شده» چیست؟ آیا این دو یکی هستند؟
🔸
ست مولتن: ۵ ماه پیش ترامپ در استراتژی امنیت ملی خود دقیقاً از همین عبارت «به‌شدت تضعیف‌شده» استفاده کرده بود. اگر این ادعا ۵ ماه پیش صحت داشت، پس چرا ما این جنگ را شروع کردیم؟ آیا او آن زمان به ما دروغ می‌گفت؟
🔹
فرمانده سنتکام هیچ پاسخی نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/436715" target="_blank">📅 23:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b57512bb9.mp4?token=Ag_j7crICvqKQZRQ1GPcnwCsWtvcC5eBT-GwXkB2jrnMwQh3czY6K3vZu9M8OxgEf77LxZROh2oJ6VJrGibJXqd9tcfqXZC1YNNQahUeUv_4sW63_7anbls4NsoXjvLk1hiiplDsjFnLKJwGl4KSGyAVVu5kdRYXaZjVeoEyKJGOcdtj2a1N7mz4M5GkB2Q3KuN2Rr2YwNMG0MhTMZfEySvRO_bsRTcS79pvlWXDcVjRbuj_MIVgggOCuZGbs7dkVak5fIxT1V4he6fiVulXq-buX9eHF_fkwL_CrZxJ1s6xI8WWuy63-zIkrBV70YA5I2unsm5TABiDpUyIgr1rFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b57512bb9.mp4?token=Ag_j7crICvqKQZRQ1GPcnwCsWtvcC5eBT-GwXkB2jrnMwQh3czY6K3vZu9M8OxgEf77LxZROh2oJ6VJrGibJXqd9tcfqXZC1YNNQahUeUv_4sW63_7anbls4NsoXjvLk1hiiplDsjFnLKJwGl4KSGyAVVu5kdRYXaZjVeoEyKJGOcdtj2a1N7mz4M5GkB2Q3KuN2Rr2YwNMG0MhTMZfEySvRO_bsRTcS79pvlWXDcVjRbuj_MIVgggOCuZGbs7dkVak5fIxT1V4he6fiVulXq-buX9eHF_fkwL_CrZxJ1s6xI8WWuy63-zIkrBV70YA5I2unsm5TABiDpUyIgr1rFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری فردی که خود را عزرائیل تبریز می‌نامید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/436714" target="_blank">📅 23:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE2xVLb_bcjBFfE-SkxpRAIIz8-WVSDxExoDQVzwFt_oqQVYCSSSfm4aeI1cL1jpZkuv6TIzmi-de88y4SsJDp9QOud0GaSLRv96v_O8K3J27wAG7HwoY6nsJK0NkCBkAjLix1R_LSuUFBxWwtP-d4pGx8o085Pz1lLxlvCMrSAg5gaoW0W5hm835QZ3Zvi40v-QZTg1DJgAFMroJqOQcI2n2Ke8LOkR940oQotfKIcj7lSoUyJpYqW9z2QReOJV3zoMBiBLBH_L_fagbMuTyHiamG0k_33w_0s5v1kMiG6-edOA1fgCr7W6JCzeM32DlTvuWz-QkeRFRNynRR4cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: برخورد ۲ هواپیمای آمریکایی در عراق احتمالا ناشی از آتش گروه‌های مقاومت بود
🔹
در تاریخ ۲۱ اسفند ۲ فروند هواپیمای سوخت‌رسان آمریکا که درحال پرواز در آسمان عراق بودند به یک‌دیگر برخورد کردند؛ یکی از این ۲ هواپیما آسیب سختی دید اما توانست فرود بیاید اما دیگری سقوط کرد و ۶ نفر را به کام مرگ کشاند.
🔹
در همان روز، سنتکام اعلام کرد که این سقوط بر فراز «حریم هوایی دوستانه» رخ داده و ناشی از آتش دشمن نبوده است.
🔹
حالا اما نشریۀ آمریکایی آتلانتیک به نقل از ۲ مقام آمریکایی گزارش داده که اطلاعات محرمانه نشان می‌دهد این حادثه احتمالا بر اثر شلیک ضدهوایی گروه‌های مقاومت عراق بوده.
🔹
مقامات نظامی به آتلانتیک گفتند که انتظار می‌رود تحقیقات نیروی هوایی به این نتیجه برسد که این فاجعه یک «حادثه قابل اجتناب» توسط خلبانان بوده.
🔹
آتلانتیک در پایان نوشته اطلاعات محرمانه دربارۀ این حادثه نشان می‌دهد گروه‌های نزدیک به ایران در عراق همچنان قدرتمند باقی مانده‌اند و تهدیدی جدی برای آمریکا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/436713" target="_blank">📅 23:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef754870b.mp4?token=rXdeSPdv7EnA_IRMBgvk77jHu4pvMotSBsUktZito5vXtP6w2kAzaM3yXwVTE9zGqB84M_rzIWSnez4YgfnQZQ2CeMtsazUs3fuGJyI0cuDX12o_0IYkJp49UltAFhtCo9ooMhMsnxemmH9MzCxp6zmKEnLkzJrWZEAkHlBneEHrZy1IPUuCfD1F7wFABsd1nIN4dex2KLztfmkyqZvhCkpt8wDki_GII6i0_oGifJI3PvqCS-ObZYyUzFm5jPASGTIl8qEtAjYWdY0LM_jctRlINfqHyJA2K8px_rzte4QwbJsH_lQTl9rFQaEoj17qtTynC52Eh4gNsE50j7qgnXGoDbFFDRuDSyOjregXWM2SvYlBk5HLS6gnaLjX7c8xcpD5rNNCiY_yPHF4ho0mSk5rqs6RjZbTX_a5qipJeos_YWqiAGgXNJIVf8nTvUVNOAskqXqm5a6Wfv-fzueyFvwNhJOnt8Wsp8WlAvsJuG5NaugqVvNUDTWZMhlP5jOjSx9eA02o4BJ6l98zlW1CtNeBr1hLeXS61uuNFbbU5iF7CMwtKULuYcLODlFiCMHEKWnVyhTamQ4N1xPEA_m7t_XqX3sFyy61I-BvkzRG7Gj62wNzzsLYOHNZ7aN9aD6vbUfc6x5raqQVu4iUoIasrsQXgkYdmgdesIUBYAl1g-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef754870b.mp4?token=rXdeSPdv7EnA_IRMBgvk77jHu4pvMotSBsUktZito5vXtP6w2kAzaM3yXwVTE9zGqB84M_rzIWSnez4YgfnQZQ2CeMtsazUs3fuGJyI0cuDX12o_0IYkJp49UltAFhtCo9ooMhMsnxemmH9MzCxp6zmKEnLkzJrWZEAkHlBneEHrZy1IPUuCfD1F7wFABsd1nIN4dex2KLztfmkyqZvhCkpt8wDki_GII6i0_oGifJI3PvqCS-ObZYyUzFm5jPASGTIl8qEtAjYWdY0LM_jctRlINfqHyJA2K8px_rzte4QwbJsH_lQTl9rFQaEoj17qtTynC52Eh4gNsE50j7qgnXGoDbFFDRuDSyOjregXWM2SvYlBk5HLS6gnaLjX7c8xcpD5rNNCiY_yPHF4ho0mSk5rqs6RjZbTX_a5qipJeos_YWqiAGgXNJIVf8nTvUVNOAskqXqm5a6Wfv-fzueyFvwNhJOnt8Wsp8WlAvsJuG5NaugqVvNUDTWZMhlP5jOjSx9eA02o4BJ6l98zlW1CtNeBr1hLeXS61uuNFbbU5iF7CMwtKULuYcLODlFiCMHEKWnVyhTamQ4N1xPEA_m7t_XqX3sFyy61I-BvkzRG7Gj62wNzzsLYOHNZ7aN9aD6vbUfc6x5raqQVu4iUoIasrsQXgkYdmgdesIUBYAl1g-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد به‌یاد شهید رئیسی در شب ۸۰ تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/436712" target="_blank">📅 23:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_1cn4rCaFIrPTDeoEYBueIDooijN6QDo-f7peICCT6sI7PW7Ad81n9AoJxw7pJZmCZNxWmqmd1W0VxQKgLtcAabKRVrIsOShQLb-wFXACHrw_Pab5stO_ZXxZdaKa9zIU9KOKfbVAnudBZfFAF_DGPXaCEsVqrAtZl1a8U06mRrfth5Q2RyqF5F_z5NSBv0Ga7iHGRlHXgupP24fMmnaKvd0SUbVEJZbPvltBrRqOWMoE9a0L-f4fQrCb8gbo6dP2CntfyCcYv31AbFIKbboEnCIvcjmUDebT7YAA8queeMcKCHeD59tqz6R4a93nsLMyqLlo2uM3LKBfdsMsWrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیل دزدی دریایی صهیونیست‌ها علیه ناوگان جهانی صمود
🔹
نیروی دریایی رژیم صهیونیستی ساعاتی پیش به کشتی‌ها و قایق‌های باقی‌مانده ناوگان صمود که برای درهم شکستن محاصره به سوی نوار غزه در حال عزیمت بودند در آب‌های بین‌المللی حمله و آن را توقیف کرد.
🔸
نظامیان صهیونیست پیش از این نیز ده‌ها قایق دیگر را توقیف و صدها فعال شرکت‌کننده در این کارزار را دستگیر کرده بود.
🔹
علیرغم حملات نیروی دریایی اسرائیل از سپیده دم دوشنبه علیه شرکت‌کنندگان در این ناوگان، ده قایق ترکیه‌ای امروز سه‌شنبه به سفر خود به سمت ساحل غزه ادامه داده بودند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/436711" target="_blank">📅 23:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c437f0788.mp4?token=WoxgwoLCJdb9bRNxvlhYmADbkfyVzub4TQGvrd66SO2aoAdKSSRqCvkcfn1olgSc-httIOPKl8EhYLd_R-XOZX-Xf6UYI0apNWMgfOFtNlAJ77gf2T1oAk3azM9UM-IXHyryH88o4KzjZsLnTIO9LMN3STV4DHLXIrs3YGvrzH_9VlsciaBeDh9AoHSZoLGY_0vVK7kWD2EBYRBIId3cgY8k2-3Y7TAw8x4ba5pCiYlP7A-zxHCPqs9HvAlv-oztLfHoHPndYjlZYCTh24X-9TJwiso6wPYga8gogTYG1x0fBdPUW05ypRyj0Ip8Qk2oqmMEzT7IbViV-374oJ1ISFKWv7LFNkxx5m1929Y8PJLZl1KejjlGNhMQ81LK8mWkf7rEfy2K4TtFATppg_ispHk6qgTbhp-cuYM_MsqbJjvCuzXwxgNQb-dfrm14p9JaoPkcwauzVMTUjFgIiC0rNJNg7x80GqDps95pKkwzJW0SSSbvQwsICtIVzIvvg91rJuQyZJXB3pbIy8rhbM8Brkk3PEeZlqgaeLXAO2eHSexRZkFVnCgPOsu1W5d8i_DZWHpSkoFLYfHctiIWsM0-nQzjNwOoD_oM1z2dRTzKiYtqdOp16MXqMOZA5tuzSnQ6c74Y11ot7F-2LPwvgs4L9LkzVL4KLdK3uiCkM1Lrbcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c437f0788.mp4?token=WoxgwoLCJdb9bRNxvlhYmADbkfyVzub4TQGvrd66SO2aoAdKSSRqCvkcfn1olgSc-httIOPKl8EhYLd_R-XOZX-Xf6UYI0apNWMgfOFtNlAJ77gf2T1oAk3azM9UM-IXHyryH88o4KzjZsLnTIO9LMN3STV4DHLXIrs3YGvrzH_9VlsciaBeDh9AoHSZoLGY_0vVK7kWD2EBYRBIId3cgY8k2-3Y7TAw8x4ba5pCiYlP7A-zxHCPqs9HvAlv-oztLfHoHPndYjlZYCTh24X-9TJwiso6wPYga8gogTYG1x0fBdPUW05ypRyj0Ip8Qk2oqmMEzT7IbViV-374oJ1ISFKWv7LFNkxx5m1929Y8PJLZl1KejjlGNhMQ81LK8mWkf7rEfy2K4TtFATppg_ispHk6qgTbhp-cuYM_MsqbJjvCuzXwxgNQb-dfrm14p9JaoPkcwauzVMTUjFgIiC0rNJNg7x80GqDps95pKkwzJW0SSSbvQwsICtIVzIvvg91rJuQyZJXB3pbIy8rhbM8Brkk3PEeZlqgaeLXAO2eHSexRZkFVnCgPOsu1W5d8i_DZWHpSkoFLYfHctiIWsM0-nQzjNwOoD_oM1z2dRTzKiYtqdOp16MXqMOZA5tuzSnQ6c74Y11ot7F-2LPwvgs4L9LkzVL4KLdK3uiCkM1Lrbcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش کار با شکارچی F18 به داوطلبان پویش جان‌فدا
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/436710" target="_blank">📅 22:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیویورک‌تایمز: در صورت ازسرگیری جنگ، ایرانی‌ها تاکتیک‌های جدیدی به‌کار می‌گیرند
🔹
نیویورک‌تایمز نوشت: «ایرانی‌ها خود را برای ازسرگیری احتمالی حملات آماده کرده‌اند و سیگنال‌هایی فرستاده‌اند دال بر اینکه در صورت حملهٔ دوبارهٔ آمریکا، درگرفتن انتقام و تحمیل هزینه‌ای سنگین بر منافع آمریکا در همسایگی‌شان و اقتصاد جهانی تردیدی به خود راه نخواهند داد.
🔹
در هرگونه دور جدید از درگیری‌ها، ایران ممکن است روزانه ده‌ها یا صدها موشک شلیک کند تا «به‌طور مؤثر با دشمن مقابله کند و محاسبات طرف مقابل را تغییر دهد.»
🔹
کشورهای عرب حوزهٔ خلیج فارس باید خود را برای حملات شدیدتر به زیرساخت‌های انرژی‌شان آماده کنند.
🔹
هدف‌قراردادن میادین نفتی، پالایشگاه‌ها و بنادر کشورهای خلیج فارس، یکی از کارآمدترین راه‌های ایران برای آسیب رساندن به اقتصاد جهانی و اعمال فشار بر ترامپ است.
🔹
اگر آمریکا به زیرساخت‌های اقتصادی ایران حمله کند، ایران با بستن تردد در باب‌المندب به آن پاسخ خواهد داد. یک‌دهم تجارت جهانی از تنگهٔ باب‌المندب می‌گذرد.»
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436707" target="_blank">📅 22:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf02d7939.mp4?token=s6oIElwOm4JlLvqutSKPbwQlHaA9RKUIOHtpSl6QCnDAtlN85ZdGntM-p0juOtRiovqRaB6b5CbxaZrB_ncOueugzF0aWu9Nl6mWvxT_g768K9hpb5Wm1Vy_R6fxZaMexODXJNs9fiTRFfrfM-qMs23dAi7mpkKz3cnzL3SZR-ATSIk1fvkJFjqFSY5ayJ2g_H2iwCk-LHR-5OaXznDlv9trgsH4H0ol1P9ry_FJuUHsX9OzMmTWZU3YprT4VyHQVvSIM0qPvI6X0oRxirA3tTdAG7ZkEB5r3hqSIp0roWgxIJ6wSX7G8l2tUiN8HKe0BQdkxjkPu9yRULhQI7BGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf02d7939.mp4?token=s6oIElwOm4JlLvqutSKPbwQlHaA9RKUIOHtpSl6QCnDAtlN85ZdGntM-p0juOtRiovqRaB6b5CbxaZrB_ncOueugzF0aWu9Nl6mWvxT_g768K9hpb5Wm1Vy_R6fxZaMexODXJNs9fiTRFfrfM-qMs23dAi7mpkKz3cnzL3SZR-ATSIk1fvkJFjqFSY5ayJ2g_H2iwCk-LHR-5OaXznDlv9trgsH4H0ol1P9ry_FJuUHsX9OzMmTWZU3YprT4VyHQVvSIM0qPvI6X0oRxirA3tTdAG7ZkEB5r3hqSIp0roWgxIJ6wSX7G8l2tUiN8HKe0BQdkxjkPu9yRULhQI7BGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از ماکت مجسمهٔ «مشت‌ گره‌کردهٔ رهبر شهید انقلاب» رونمایی شد
🔹
این مجسمه قرار است در میدان انقلاب نصب شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/436706" target="_blank">📅 22:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7ClOM7FaS0CD_BtZW53HF_2_PG0J83-wT17Q3oxv4GaHegshykLBVoLJmF_sva9NDEnpF0mdfbbq2ntl9HPQ48nrdVGngoEVJu9XwpROOQYb_dN5d4GM5HBAbNjNytWkOA16fxHmZHIJbRYoqVPGm5jtIcSDFqEhGpWLrBKDP3GCTTmXo9gBCYpN04Ae8488x5Nt3HyAlQOzOUfxYTT8pmkpELm5lqdNzuIwh6BMnmgfuKBQnsWAS7MeAe-rSj7srlNHDh6RTLCuh6U3ZjMix6bjHY_Ugu_srW4yVbyM518N9Yf-K6sDEF6T7WdaYxkPnruJv49zHicB-0QVLsXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردوخاک در تهران با منشا نامشخص
🔹
مدیر حفاظت از محیط‌زیست تهران: باوجود افزایش غلظت ذرات معلق هوا برای امروز و فردا در تهران، هنوز شرایط اضطرار گردوغبار در پایتخت حاکم نشده است.
🔹
جمع‌بندی نهایی درباره داخلی یا خارجی بودن منشأ این پدیده هنوز انجام نشده و نیازمند تحلیل قوی‌‌تر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/436705" target="_blank">📅 21:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBk-z_ideA4mUe4zzH3wDhLrG_dRIgqglzw5O10vex3VzU84CXa8dBZ1Hr-l0VZZL_bb1I7YwDPK6gng6R3lz1acwJTd1aUQOlQsNwb9DWkP3U4Fg5WLES9Hrs_pIWP4B0CyddHKzwCN4NvMNwN3owo4fgqU1BjeH5hapdCRARbs8GCMQH91BhWMMOHxkregpVb2GgxboZVaRf1r4VyyZP-TGr_Gdj0QjSaKtmoWgBcqPIQlqSMJVxF17ac1NNjC7wlLQZGsUFLexmlzrmtBmH5mdLoMJXG9TKwOoBQOLpK-e36pcJEmk3gxayDfXoooX3D1cRIymQ5ZIJRxlWW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش کنگره از هواگردهای اسقاط شده آمریکا در جنگ با ایران
🔹
بر اساس گزارش‌های خبری و اظهارات وزارت جنگ و فرماندهی مرکزی ایالات متحده (سنتکام)، ۴۲ فروند هواپیمای بال ثابت یا بال گردان (شامل هواپیماهای بدون سرنشین) که در عملیات «خشم حماسی» سرنگون، منهدم یا آسیب دیده‌اند، فهرست شده‌اند که شامل: «تعداد هواپیماهای آسیب‌دیده یا نابودشده ممکن است به دلیل عواملی مانند محرمانه بودن، ادامه فعالیت‌های جنگی و انتساب مسئولیت، همچنان در معرض تجدیدنظر باشد.»
🔹
چهار فروند جنگنده F-15E استرایک ایگل
🔹
یک فروند جنگنده F-35A لایتنینگ ۲
🔹
یک فروند هواپیمای تهاجمی زمینی A-10 تاندربولت ۲
🔹
هفت فروند سوخت‌رسان KC-135 استراتوتانکر
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد)
🔹
دو فروند هواپیمای عملیات ویژه MC-130J Commando II
🔹
یک فروند بالگرد جستجو و نجات رزمیHH-60W Jolly Green II
🔹
۲۴
فروند پهپاد MQ-9 Reaper  (پایدار با ارتفاع متوسط و برد بلند)
🔹
پک پهپاد MQ-4C Triton (پایدار در ارتفاع بالا و برد بلند)
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/436704" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb0707161.mp4?token=tsixSiie9O1d9bE4_2qE_fuRI8xxH0e773sC4WaKdkYnXmYfBJqouV9gvEYsGj1s5oz0oZ1xiIBpPgrwseCEZ54Lq14SwF1dPRfYpFw4Pnv4fUqUuPLfBKIOZySKn6V80zGgVxve8uSn0s_rVnI92jRJjNDvOB5jlvW-f_u0-26cjD8EgUHlYzX9Zi9GSi3mVMmx4wkOzo0rV06Wk3XOdE5NB0ut51_r2s1ZbDZDi-uCJNDX9Jgvy8dmjGoUhLiVDo5cQ0WsIZDlRkGbR0I_3LCV8vbaIkTu0cftyPK__6Y8VvlXp_nrrDdOzteXDV6y__iVOyomoyvmPfNhLujvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb0707161.mp4?token=tsixSiie9O1d9bE4_2qE_fuRI8xxH0e773sC4WaKdkYnXmYfBJqouV9gvEYsGj1s5oz0oZ1xiIBpPgrwseCEZ54Lq14SwF1dPRfYpFw4Pnv4fUqUuPLfBKIOZySKn6V80zGgVxve8uSn0s_rVnI92jRJjNDvOB5jlvW-f_u0-26cjD8EgUHlYzX9Zi9GSi3mVMmx4wkOzo0rV06Wk3XOdE5NB0ut51_r2s1ZbDZDi-uCJNDX9Jgvy8dmjGoUhLiVDo5cQ0WsIZDlRkGbR0I_3LCV8vbaIkTu0cftyPK__6Y8VvlXp_nrrDdOzteXDV6y__iVOyomoyvmPfNhLujvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتادمین شبِ ایستادگی و همدلی در گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/436703" target="_blank">📅 21:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک خودروی نظامی در شهرک القوزح در حوالی بنت جبیل و تجمع نظامیان رژیم صهیونیستی در شهرهای العدیسه، رامیان و بیت‌ لیف را هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/436702" target="_blank">📅 21:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
توزیع مرغ منجمد با قیمت کیلویی ۲۶۰ هزار تومان آغاز شد
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/436701" target="_blank">📅 21:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thmkBqwvzS4ciNG0teuqHoKdgl7u7GDbYTPzl_IObs6bGSyOBXtTpUPwe32bfYWxE55KyLeSjRZbtDdpGFu-i30qVPyxpn3tiSB0cZYpCH4EciEWVlnXd-bz98Z-Kt2DpuVwd_RPAEtWn5trXFIZp56fVlx2NLZGmPe4oAJlMb3Ga3cV6J4v0Wkf8gcv5suEeDU3Ihn_U-VJLHwlWpmozbKT4xvwDYwW6qmEBg3FB21wY9No4UqpO3hfHJHCdCxbykNoWoDDkxPFi4LfEPrp4oNGSF59vHE1LF5R1rOjbDN48GvZLtwxJtCZ9W-CpYdzepZk5siZNjAoImjJazgNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ۱۹۲ هزار نسخه کتاب تا نیمهٔ نمایشگاه مجازی
🔹
قائم‌مقام نمایشگاه بین‌المللی کتاب: تا چهارمین روز، فروش ۱۹۲ هزار نسخه اثر با ۸۵ هزار سفارش در نمایشگاه مجازی ثبت شده‌است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436700" target="_blank">📅 21:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست تا زمانی که تعیین‌تکلیف طرح پیشنهادشده به شورا مشخص شود.  @Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436699" target="_blank">📅 20:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgKFDGIIglEZ5bCZ3ew0CnpdUAHNws1uTHX6LswU00V6LhMgiMSvnDfGGAUIQtqUB8y09TDY4kDaJDdeG9YVsHkPNlTnNQOZ71Sdpcw3CUzenCDB05QxV8V5ijlUGX6cVQ8M8pnuo7Dacnly6HYiyVT7Ki8XUREj2wmfOSCxY2DkpKk1Bg2Z-Pfx6TXkJ7AMDN0UQeXf8L4PTBx0zUR58hixqVaYSX5jy7AppnVAvzApSNx6o9sOiEGTEVBC3Ew5eqBnlv_266tmtgmCcV53BZGtVhArcujkDBNaXJ_TIpw1Sl4AcxDXtKgEiGPLWCcayXyU1J9jDodJuPGkvQJUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح مشارکت در تولید سایپا با قیمت نامعلوم
🔹
شرکت سایپا با اعلام شرایط مشارکت در تولید محصولات خود، اعلام کرد متقاضیان می‌توانند از ساعت ۱۰ روز سوم خرداد برای ثبت‌نام اقدام کنند.
🔹
موعد تحویل خودروها در این طرح از مرداد تا آبان سال آینده در نظر گرفته شده.
🔹
در این طرح، خودروی شاهین GL با پیش‌پرداخت ۵۹۰ میلیون تومان و خودروی پارس‌نوا با پیش‌پرداخت ۶۶۰ میلیون تومان عرضه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436698" target="_blank">📅 20:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از کشته‌شدن یک سرگرد از یگان ماگلان در نبردهای امروز جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436697" target="_blank">📅 20:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdjgXFasIbyUTFsbT-LM-Hb4-GWW4MtNQx2JoD-4bvIkFJE8cBAk7SKowjW3i5hoEDLgHCfGw3nyKGTUPr3p8T79ffPzNUp-R7IVMTax2o2DnfDGeqvXRThNuId0raDpj56y1eaQLzjXEpFqhGDQm1C_vcn2a4WHGhfk4VVVLpdH87qAT8GgxzTdTNiSTT6YuBj7L34FbEoI5_85Sqk4qcOa_iwkBgAJYj4UjgOHfMy_yD4mTDXy4aNsDPnDoFdMJSxFCvjhmbcFzNRmAfFKk1pJ_MwwvZjlt90qZTrpdRkUb0-55hkeq5r8dHluPyzqTh37479KUTWtEiqkHSXBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای شهر تهران: در حال حاضر ۹۴ درصد هزینه بلیت مترو از طریق یارانه‌ها تأمین می‌شود
🔹
پیرهادی: اگر حذف همین مبلغ ناچیز باعث شود شهروندان بیشتر به استفاده از مترو و اتوبوس روی بیاورند، این نوعی سرمایه‌گذاری برای آیندهٔ شهر خواهد بود.
🔹
افزایش استفاده از…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436696" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrLosvKXTIpOkl1sWyHKrHYpCWedumvJUR0m-ea4kd8eAPMXM85V7eNfhvmm5kxMpY498IH1-HFFHzwTml7JB0sARmNWrYjhyXOrrRz_n0bGGUFKjLZX83b2dez7JvROKIPr2F7FDOuUvIQ157n9tVvxWl-9DRMh4wb4pxcC1oPxug6NjUjGozsKF31oRrlaHxGLrzE6momiaV-66ylpac5gNSA8GA_HMLwlSPIeNy1RcSr6xFSoC9jgae8kIlH0IwQleLsmcEEQUN7px61I7v6GG1ni-PrZZe5mGcl8Js1zct6xjdDrgikc-_JDyti-pQ4LwiP9U-CqOTABFVjt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436695" target="_blank">📅 20:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436693">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCO-Vsu6n7y4VVYpeQ5DX8oCGXM8eCuUP43JiFiwDPGIHmoHWLh1uymMXR8GLLGh00rYzLLg1NKe8BziMxlHHiepSmtZqPm60Jkyiig3egkBnMGlQa6DrOa230RU65YO2Vr1aUjrMGYcwYB0C11mEG1AfpdgCHxjHB7QtVNhzMzNPcvawd5PMm_9W3hUWWpqe30Y5uXlWE3-G2ZeWwo1jj7ILCTPD_ZgD_vsYTiA5Gl9I_0NFVA2Chn5QLrkCFmhejUR0YYJA6vful3zhR34sKEnReoSU412oCfPyL3E7-JpzOwmHUgpJm-xc7KV2R1BGM0b2umqYvO-Gwc7cUsE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزاداری مسلمیه ۳ شب در شهرری برپا می‌شود
🔹
معاون آستان حضرت عبدالعظیم(ع): مراسم ایام مسلمیه و شهادت امام باقر(ع) در روزهای ۲، ۳ و ۴ خرداد برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/436693" target="_blank">📅 20:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436692">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7386ddfe.mp4?token=ptey8GInZIMeXTYTU_m1CqGm-M6BSiwjAOGP3yj93fP9UCuaNaO5W4LPsFAwCeGQqp9bfsORisuIxnLkwHgs2Q9sY97xVqLg-Z8pxzbcnl-zuuLWCl_eqEdHD377DGx5R0sfVtqWPFtEmC6qaZOOA330X4EU_d8lQj_OPosTSMSSczhCCJiZXeIaw1oa6wZq_jHIiF6gqWyEnLroyhTQwWxGLe5LWcARrqoFMNGlf88CZwzPSZlep8IXuHkGd56Z8YThA_kWAqFMjGqZXcAfTHC53XNZYLPtjPOeO0dzgHS5AcELEY5M5AZ57NxCZ9NUE-t_yYPfAaP4CURJ1wGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7386ddfe.mp4?token=ptey8GInZIMeXTYTU_m1CqGm-M6BSiwjAOGP3yj93fP9UCuaNaO5W4LPsFAwCeGQqp9bfsORisuIxnLkwHgs2Q9sY97xVqLg-Z8pxzbcnl-zuuLWCl_eqEdHD377DGx5R0sfVtqWPFtEmC6qaZOOA330X4EU_d8lQj_OPosTSMSSczhCCJiZXeIaw1oa6wZq_jHIiF6gqWyEnLroyhTQwWxGLe5LWcARrqoFMNGlf88CZwzPSZlep8IXuHkGd56Z8YThA_kWAqFMjGqZXcAfTHC53XNZYLPtjPOeO0dzgHS5AcELEY5M5AZ57NxCZ9NUE-t_yYPfAaP4CURJ1wGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی فیفا به پهلوی در جام جهانی
🔹
نشریۀ اتلتیک از منبعی در فیفا اعلام کرد که این نهاد قصد دارد آوردن پرچم‌های دارای شیر و خورشید را در ورزشگاه‌های جام جهانی ممنوع کند.
🔹
در جام جهانی قطر هم برخی از هواداران پهلوی پرچم‌هایی به ورزشگاه‌ها آورده بودند که از…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436692" target="_blank">📅 20:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436691">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
هدف‌گرفتن گنبد آهنین و پایگاه رژیم صهیونی توسط حزب‌الله  حزب‌الله: یک سکوی گنبد آهنی در شهرک مرگلیوت و یک پایگاه تازه‌تاسیس رژیم صهیونی در شهر مارون‌الراس را با پهپادهای انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/436691" target="_blank">📅 19:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436690">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqu4DAOkAAWTOogaNxb248fk9bsZeCktQht5pOrUHXnnEuiVJA-qf7Of3K7m6BO0V1qBtTP-IVHJsVBNygLPGsEV7CuSuhAIlVzO3Q-sCnRtzdFiyUFQMlveQSnj5gUiJ8233X2zOQlac2Syw2zPRH0IyRqHoMuFiIWdBuWW9bJQ8AvUUZA9RDnJwon2CwVZHd75_ta0B1DHNurXxyTeUl6402El8esh1uj0wRhUsB2DqOhgP2HqT4nv_3O3rgn4k-wgrVes1mUR_tN204ZalAzitPdM5aO8BgNzejsEftTBovgSADSlBkuc_sWl7KNqiE3TMYC0lhmvVwF4tqTlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولد ۱۰ نوزاد خارجی در رویان
🔹
پژوشگاه رویان: از ابتدای سال، ۱۰ نوزاد زوجین نابارور خارجی که از استرالیا، انگلیس، عراق، افغانستان و پاکستان برای درمان به ایران سفر کرده‌اند، به دنیا آمدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/436690" target="_blank">📅 19:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436689">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
واکنش وزیر کشاورزی به بازار سیاه گندم
🔹
روال همیشگی نشان‌داده که کشاورزان مایل هستند گندم و محصولاتشان را به وزارت کشاورزی تحویل بدهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/436689" target="_blank">📅 19:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436688">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ce9cf249.mp4?token=Y56DvHOPZs7Ws5liVMQPLdcu6jPFW8nJ8occuOeW_9EMuPwM1_VKCime0lPDNTqxEgjVPBu5n2kwo-DAXtUt8PBERT9DkAuZYISdyw8ZmiwzvOQNtjuUHWyQicqFAXpVpR50aql6t6HPqy2fbXyBFRhogHgQ7QXgudpKGo34x6-n1fmGG2Mr7bqkREVb60GomD5lueiuNAVax4J9wBn3jieXwmt98ig1PxxYfzohtZxzmX1AarLwIjUI1DumBcaTK3UcQyhiAh8sIwk6Cmdc6MYffB3NWKeJP-v2Hr2-1ucCFRoPh7oed814FtZeZISk9_sgRWdhlsNxTXCTalzZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ce9cf249.mp4?token=Y56DvHOPZs7Ws5liVMQPLdcu6jPFW8nJ8occuOeW_9EMuPwM1_VKCime0lPDNTqxEgjVPBu5n2kwo-DAXtUt8PBERT9DkAuZYISdyw8ZmiwzvOQNtjuUHWyQicqFAXpVpR50aql6t6HPqy2fbXyBFRhogHgQ7QXgudpKGo34x6-n1fmGG2Mr7bqkREVb60GomD5lueiuNAVax4J9wBn3jieXwmt98ig1PxxYfzohtZxzmX1AarLwIjUI1DumBcaTK3UcQyhiAh8sIwk6Cmdc6MYffB3NWKeJP-v2Hr2-1ucCFRoPh7oed814FtZeZISk9_sgRWdhlsNxTXCTalzZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام یک تانک مرکاوای اسرائیل با موشک‌ هدایت‌شوندهٔ مجاهدان حزب‌الله در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/436688" target="_blank">📅 19:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGzKBh9KbTVlJdU1YkikF1bn7-QKQCr09dRIen_D7MmQlp_RL4Wx_1_nWm8YeFceV0hl7nBvX9ehcbrzEOTTuUw70yaF4zFuzLtWV59u1Q7kZGgkvCCVNWvduw6rUGpZrrC9CJp-tI4vKqPjNUUxunefVXf5zfHrnON_4WM81XTbIamzqEpYgTMsg-368_i8o75eqRaktJIEwmBuHR-imObHMs16HBozIVPZ9c8zXLV0tITI-MdNXXA80Zuw1SCrMscmwzEXXz6Jd570WkxYeUhY7yr63w-hvQX1gQCEa7y6oHr6kWeIfrsCdi6sBH15RcUh88yYKzY7_hysaFC83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات چای مجاز شد
🔹
صادرات چای به‌صورت مجاز مشروط از سوی دفتر مقررات صادرات سازمان توسعهٔ تجارت به گمرک ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436687" target="_blank">📅 19:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436686">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
بیعت عشایر بختیاری با رهبر انقلاب در خیابان کشوردوست
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/436686" target="_blank">📅 19:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436685">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b981437517.mp4?token=Tnor5xP2RIWkd9I11ql7WhUul1Wh84t_mYKQdP3LhmIcDI7mw_wjTpzMbMaHgZ-xgPi3T3as8bO1k0XyiCixq0mpZ_mYlojhaxNaYC2DRJ1z-wj1VM8M3CpZB7WLtqBFryUcjc3TN_5ivGK4pEuDN3Kg1dEKhasUe5tPGO3qlySC2yi2RbEQ7hc5kmInAQKnXNhgXDI7R5A72LeX_P-QTiJjWBP9GFwGJVZbETkD2oycV2mVsImOALZ5-jyOpfrcgvaimtmddaacGyDGYUnAH9El6uU2uNuZ3VBzH2hsGJf8VORZCGeewxjwAbND8QSSkmRGVbB9GMWk5ibGa-Qd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b981437517.mp4?token=Tnor5xP2RIWkd9I11ql7WhUul1Wh84t_mYKQdP3LhmIcDI7mw_wjTpzMbMaHgZ-xgPi3T3as8bO1k0XyiCixq0mpZ_mYlojhaxNaYC2DRJ1z-wj1VM8M3CpZB7WLtqBFryUcjc3TN_5ivGK4pEuDN3Kg1dEKhasUe5tPGO3qlySC2yi2RbEQ7hc5kmInAQKnXNhgXDI7R5A72LeX_P-QTiJjWBP9GFwGJVZbETkD2oycV2mVsImOALZ5-jyOpfrcgvaimtmddaacGyDGYUnAH9El6uU2uNuZ3VBzH2hsGJf8VORZCGeewxjwAbND8QSSkmRGVbB9GMWk5ibGa-Qd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز تمرینات بدنی شاگردان قلعه‌نویی
@Sportfars</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/436685" target="_blank">📅 19:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436684">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6077f0e9.mp4?token=gwuyW5vNbZTJL9FMSNcdHXm4IMNv5zv0AEwYNGDYDS5V0f6x6Ap4OBV6jBoaCVdqTaYORSOEQOlpUFZ2h0T-yWYbOlO6LRVqPElps9LJ3nqnuJ8bpZftMqvkFefwQBX6uFRLV7po10xPPuWGMxOIFSqtuKxnzfZH46yzZ6UycLU0IACmxTktwcqnuqEjiCkcXUXPveCmoc2OLxw7_lOHX5HfAsXj-Kf5w6a_ZI_v0ewXj3BE0t0DpVadUrep9gXwEAgjTXT7w-WOumgOxARO5cFkTulNIEM2ZleZfa17crSAovjWQjIAaiyUk3dlynUdQaeLYnZOydls-2yITx-AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6077f0e9.mp4?token=gwuyW5vNbZTJL9FMSNcdHXm4IMNv5zv0AEwYNGDYDS5V0f6x6Ap4OBV6jBoaCVdqTaYORSOEQOlpUFZ2h0T-yWYbOlO6LRVqPElps9LJ3nqnuJ8bpZftMqvkFefwQBX6uFRLV7po10xPPuWGMxOIFSqtuKxnzfZH46yzZ6UycLU0IACmxTktwcqnuqEjiCkcXUXPveCmoc2OLxw7_lOHX5HfAsXj-Kf5w6a_ZI_v0ewXj3BE0t0DpVadUrep9gXwEAgjTXT7w-WOumgOxARO5cFkTulNIEM2ZleZfa17crSAovjWQjIAaiyUk3dlynUdQaeLYnZOydls-2yITx-AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین وارد پکن شد
🔹
رئیس‌جمهور روسیه فردا با همتای چینی دیدار می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436684" target="_blank">📅 19:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436683">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Hx-lbABA-BpucTWJg6YlGwLH_KBoah_M4FpHrjyWR77hQ-KptAzyrpVKbe31spm-0mogPwO8Yjxpi7lzBYTxpbaRVLDhyh3ePmMHVna6yxiDS5ZRtSljotxUGb5keOYlWGCFUzm8nPLyNTUJDUNqJNN1uGWlZe6yHz0OfaI1H9EXcPCi3km7vAWZZReJ2SCKdOl74-mT7RwlJEaQU7ltx5hYMAvGmokOPYLV1g-rqLyzNUWA4NeTPfOIdpQWFRazuY4Xms8g-y_gNR-yG95oKiX0Jz4AGep9JkM9S9KOOGMXcIm2Nb0iTK-QMlVD_haLtl09RDwkVm_u2NZ4YvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ رهبر انقلاب اسلامی به نامهٔ جمعی از فعالان مردمی حوزهٔ جمعیت
بسم‌الله الرّحمن الرّحیم
با سلام و تشکر از ابراز محبت و مسئولیت‌شناسی فعالان دلسوز حوزه‌ی جمعیت؛
🔹
از جمله دستاوردهای ذی‌قیمت دفاع مقدس سوم و نعمت عظیم بعثت بی‌نظیر ملت که بر همگان آشکار شده، برآمدن ایران در مُستَوای قدرتی بزرگ و تأثیرگذار است. بی‌شک استمرار این وضع و وصول به درجه‌ی مطلوب‌تری از آن، نسبت مستقیمی با مسئله‌ی جمعیت می‌یابد. به مسئله‌ی لزوم افزایش جمعیت، گاه از منظر لزوم جبران کاستی‌های ناشی از بعضی سیاستهای گذشته نگریسته میشود؛ ولی افزون بر آن، با پیگیری مجدّانه‌ی سیاست صحیح و حتمی افزایش جمعیت، ملت بزرگ ایران قادر خواهد بود، در آینده نقش‌آفرینی‌های بزرگ و جهش‌هایی راهبردی را تجربه کرده، قدمهای بلندی را در جهت خلق تمدن نوین ایران اسلامی بردارد. از این رو، تلاش روزافزون فعالان مردمی حوزه‌ی جمعیت و ترویج فرهنگ فرزندآوری میتواند تأثیر قابل توجهی در جهت تأمین این
#آینده‌_روشن
داشته باشد.
🔹
از سویی دیگر، این امر یکی از مهمترین دغدغه‌های رهبر عظیم‌الشأن شهیدمان اعلی‌الله مقامه‌الشریف بوده است که در بسیاری از جلسات، مراودات، و دیدارهای عمومی و اختصاصی بر آن تأکید داشتند و همچنان از مهمترین مسائل راهبردی نظام قلمداد میشود. امید است تلاشهای خالصانه‌ی شما عزیزان در پناه دعای خیر سرورمان عجل‌الله تعالی فرجه‌الشریف به نتایج پرباری منتهی شود ان‌شاءالله.
سیدمجتبی حسینی خامنه‌ای
۲۹/اردیبهشت/۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436683" target="_blank">📅 19:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436682">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎥
روایت جانسوز شناسایی یکی از شهدای میناب توسط مادرش
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/436682" target="_blank">📅 19:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436681">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f86e9a08c.mp4?token=bzU74wad5_0jlBTCmpusbDYBpr9LnrS5_EoHxZu373vS5U2vtBgjOoxVECATK8mviZtwVk2fp2LKfA8ubzv128JZasSfH-lpReDGq1n7bENCBqaSIgp9hZXKeXL8iBj_zowA7zVpx9spC4KVjqasdryOGjgrno3Ui2YxBMDqBgEAJAo9L2lhSJycr7QoGmDusP7FDI5o5qPJn4yebWddGoQENEzt_czcWZ6E_g2rjIsvvI3kfKfoSvAH0d1HSDrddB0qUH5X24mccUG5zZUiR7zBBd1A6RlXge61lC7KhHpwVR5_iSI0FWHc61Q1iaeH-jNrE91fGm0DL_SvXEdfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f86e9a08c.mp4?token=bzU74wad5_0jlBTCmpusbDYBpr9LnrS5_EoHxZu373vS5U2vtBgjOoxVECATK8mviZtwVk2fp2LKfA8ubzv128JZasSfH-lpReDGq1n7bENCBqaSIgp9hZXKeXL8iBj_zowA7zVpx9spC4KVjqasdryOGjgrno3Ui2YxBMDqBgEAJAo9L2lhSJycr7QoGmDusP7FDI5o5qPJn4yebWddGoQENEzt_czcWZ6E_g2rjIsvvI3kfKfoSvAH0d1HSDrddB0qUH5X24mccUG5zZUiR7zBBd1A6RlXge61lC7KhHpwVR5_iSI0FWHc61Q1iaeH-jNrE91fGm0DL_SvXEdfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مکالمهٔ تلفنی رئیس‌جمهور شهید ماندگار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436681" target="_blank">📅 19:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b241ac6151.mp4?token=SwvSdJ2CYIzl8JYLMR-LlgoR9P6g7m0-XwKiSLARQYYiudBPr7MRHusamNA5NNGj3QR5ruegC8HpJ9LcPU7_WuxPoMXBk2Bp9nX2qv141-mW6RFBStT9kKPrE0mNVRELv8ZDygOT5mbqyfo6hvcR_4VeInK7Vhmcughm0KBdOsPlvH5RU0iJLzrYg-seIiQvNRuPUiEPCockrvIZ0iSh7c0fmVKWJWdmTEhDUr99-PmlrenN0i5Z6OT7wG5fAG6blibAIY9Ym5i-4iE3W0fgxK6pBdEQIe2H5N6qfOnl2wT8zM5yxgtc1QhYdJMAPcwyPZxNphSX8zGL1jjv0n-07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b241ac6151.mp4?token=SwvSdJ2CYIzl8JYLMR-LlgoR9P6g7m0-XwKiSLARQYYiudBPr7MRHusamNA5NNGj3QR5ruegC8HpJ9LcPU7_WuxPoMXBk2Bp9nX2qv141-mW6RFBStT9kKPrE0mNVRELv8ZDygOT5mbqyfo6hvcR_4VeInK7Vhmcughm0KBdOsPlvH5RU0iJLzrYg-seIiQvNRuPUiEPCockrvIZ0iSh7c0fmVKWJWdmTEhDUr99-PmlrenN0i5Z6OT7wG5fAG6blibAIY9Ym5i-4iE3W0fgxK6pBdEQIe2H5N6qfOnl2wT8zM5yxgtc1QhYdJMAPcwyPZxNphSX8zGL1jjv0n-07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۴ هسته تروریست‌های تکفیری در جنوب‌شرق ایران
🔹
وزارت اطلاعات: سربازان گمنام امام زمان(عج) در سیستان‌وبلوچستان موفق شدند ۱۹ تروریست عضو ۴ هسته تروریست‌های تکفیری را که تحت هدایت مستقیم دشمن آمریکایی-صهیونی بودند را پیش از انجام هرگونه اقدام شناسایی…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/436679" target="_blank">📅 18:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAgNOxvJz19DsD77hE_C2uEpaMqne-kBsmSeKjrzYwlZIBLCgwcZGQ6jLEmtSwUVlMmNAIbV9XLmxv5OejqDR9q6X9jYjVGxf1MGKo62F5cPnt_DGqrcfQ3uR3K_InFtXBrX-LG9cgR1Ixrw5GY_cxdv7EyCDp75qJ_tHmxGCvvKxmryJVX69ORAu7fYx2surMH39Kv05hLeV8Zaieu54MobRghYx7ZMU3aohUXFqdafIXEHO8KeHrQiIjDVqIAfzZtZ1i1Vwul426yCGCkc0Q4dwKO33Pm_zAhLY8wx-2RC1233O_TeKoMJvxE0GduDm8rqcZ3PQCG6oQ8y-4nDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۹ هزار مگاواتی تولید برق ایران
🔹
وزیر نیرو: امسال حدود ۹ هزار مگاوات به ظرفیت تولید برق اضافه شده که این میزان تقریباً معادل ظرفیت برق کشور عراق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/436678" target="_blank">📅 18:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db686a4019.mp4?token=BMSFLKvKUxRicSA_Hj54lyZKvsxeuONt_o0qECdVfwxMJXqAbivjoYkEpZrxFJUtSmUkQYfcgrEIXWOp2kP-IwlZhhQnreHgXxzBVjCxYcEYfWYdoyAcZ1-Nir8T_sO5iqXr5zrX3xzw13Zg1DGoVRWGTH6XYGSFmYEgZ0SfMNSdbhG1tMYVfcKXruDbEf6YFg-LyOQ8t4zxxxkvgpB15ExxUlNnEUzL0IoneA-wPny8K1BvyIKx27nANgBaQlqTC_4OkPHwwAPNS9swcPYGkqT3jxtk2GWmfe6gZIL3gVNLChrhvVX9zKpRBUSV28W4pfPMqRlKiJY-hPUA9VJ2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db686a4019.mp4?token=BMSFLKvKUxRicSA_Hj54lyZKvsxeuONt_o0qECdVfwxMJXqAbivjoYkEpZrxFJUtSmUkQYfcgrEIXWOp2kP-IwlZhhQnreHgXxzBVjCxYcEYfWYdoyAcZ1-Nir8T_sO5iqXr5zrX3xzw13Zg1DGoVRWGTH6XYGSFmYEgZ0SfMNSdbhG1tMYVfcKXruDbEf6YFg-LyOQ8t4zxxxkvgpB15ExxUlNnEUzL0IoneA-wPny8K1BvyIKx27nANgBaQlqTC_4OkPHwwAPNS9swcPYGkqT3jxtk2GWmfe6gZIL3gVNLChrhvVX9zKpRBUSV28W4pfPMqRlKiJY-hPUA9VJ2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: همه می‌گویند [جنگ با ایران] محبوبیت ندارد، اما به‌نظر من محبوب است
🔹
وقت ندارم موضوع را به مردم توضیح دهم چون درگیر اجرای آن هستم؛ اما وقتی درک کنند که هدف، جلوگیری از نابودی سریع لس‌آنجلس و شهرهای بزرگ با سلاح هسته‌ای است، همراه می‌شوند.
🔹
در هر صورت، چه محبوب باشد و چه نباشد باید انجامش دهم؛ چون اجازه نمی‌دهم در دورهٔ من دنیا نابود شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436675" target="_blank">📅 18:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsqWoqdlvBUmshhbyONuxJB3yKksDYr7A-Ee4aU3X_UAL1Y1h4v9VZDO7z0YHmMZxgmhtH-53IjX6kRznlBU3NAasPZZuqsTYouOcf8eW5TkoAhvSflXJ-ZbumMNk2M4kfxJga6au8HLrXEdZ08zFPG6ANIL8lq-K2w800vhmbblkOSU3Eu3vKmjGZA21CQ0cwKUD5wgkyEqI_2e95CtVIRxYEUzuNB5_D05wZw7wgHPQbMRKxrAt3NEczwKAFnxAKzOQED_cUZALZkbusdO8eYkxG_Z9v_wwiZhDFajORUo9sJl70UKOzlWJd35aN4d5mky9N3ghl3mwoXE5WUnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ترانزیتی ایران و عراق با توسعهٔ بندر فاو
🔹
دبیرکل اتاق مشترک ایران و عراق: براساس دستور فعال‌سازی جریان ترانزیت کالا میان ۲ کشور از تمام گمرکات عراق گمرک‌های این کشور موظف شده‌اند رویهٔ ترانزیت کالا با ایران را فعال کنند و این اقدام در چارچوب اجرای کنوانسیون بین‌المللی تیر (TIR) انجام شده است.
🔹
با مصوبهٔ جدید عراق این ظرفیت توسعه یافته و اکنون تمام مرزهای مشترک ۲ کشور که مجموعاً ۷ مرز است برای ترانزیت کالا در نظر گرفته شده است.
🔹
فعال شدن این مسیر می‌تواند فرصتی برای شرکت‌های حمل‌ونقل بین‌المللی ایرانی و عراقی باشد و حتی امکان ترانزیت کالا از بنادر عراق به سمت کشورهای حوزه CIS و آسیای میانه را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436674" target="_blank">📅 18:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8PDw3z1Wkdel0HeE3f5F4aVfugqyymk-rpo81HowtaCPnKHx2xjlDcfoyleQ-aCTmw_uaZUYbAPcpPIVLwlgelqp8SgHjRZW9MxbSJDqrUZbcrAzXBQXRSA739qojAi2L_EfrZF_Hl_yViLxB2TytPrlfME-lDvtu56VLWc_m8-eD2erXNYI4ETpR8cu6Op0cZOzZj8h615t52shLO0LHDesFoFGXqx0Kvd0Jk2wpG67saZml9xXCFPRiRPBYe4ilE63q9oN7nPznHsHcpWrPRlGZZvR6CK-ILH8J45uSfNgbccOYEiRezDjmWx7e9pROuJ6bZjhaYl-zvJARvsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریتیش‌ایرویز هم لغو پروازهایش به تل آویو را تمدید کرد
🔹
شرکت هواپیمایی بریتیش‌ایرویز بار دیگر توقف پروازهای خود به مقصد اسرائیل را حداقل تا اول اوت (۱۰ مرداد) تمدید کرد؛ علت این تصمیم «نگرانی‌های امنیتی» ناشی از ادامهٔ جنگ و بی‌ثباتی در منطقه اعلام شده است.
🔸
پیش از این چندین شرکت‌ از جمله امریکن‌ایرلاینز، لوفت‌هانزا، دلتاایرلاینز، ایرفرانس، کی‌ال‌ام و ایرایندیا پروازهای خود به تل‌آویو را تعلیق کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/436673" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436672">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در اسلامشهر
🔹
فرماندار اسلامشهر: اجرای عملیات تخصصی خنثی‌سازی و انهدام تعدادی از تسلیحات عمل‌نکرده در روز چهارشنبه ۳۰ اردیبهشت‌ماه از ساعت ۷ الی ۱۰ صبح انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/436672" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436671">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db634b8a2d.mp4?token=Z1L3YubFiTLfmnCscCbQ3tfAgCVTycjVsgInjtJ_hUn8mWjeMIP__P6gAnAt3OqCICtpPZWN8pFtW-tJiM-YXgeDlklLakz0G8HDNIfqgqxwj050mdgXIMTdFFgSR6iJlnQVMDyZPqk0y8aW7zKcXyqZ6xlRKCIjag3Gxds-vFQwvkeUWP4_A1dg4EA-1KCsbNSSSMLr0MflEfjs2WNFFTkKAZaoRF288JShjsvDxDO1X94g80VVanBrnvwUzn3AGit7W_IMnzYP25SoOEQRxA5m6t5ev3JdNV6MJJxioC02G09JoAmTVmKUfX9pv53L3KVstyKQAFwI1B2uBFdGYQyBQwzYT743Y1P46a8stLghYRTZEDbKRvFpBs224hzXgnV0KKUZN0Ru_3Sif4Ns0QXMCK9-pYBoN1JHS3kPa2-AcLHRCrZBBCT8q3bL39NxPwJdnDZ2KIEhYn7Z8dmFDFv_01dzIWjC7CfQQdU6JyDp_VNrLcSpIn89AwpmWbJbP52ODAL9GBwnlvxTYR_JVi8sJakoNur4ZfHRUB86Fy1wfK91e7wXvKPo3YGc1EPqT7Rc7mbiw5P-lbSiJzYpDE7yhtxi44Yz8S4m5rnfe8tRw5hPc4C9LfO4PBkZgvawvM7NzBkGBurg2IDUeuVFJAhnuRGJ9Z0k2eK07RE-MUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db634b8a2d.mp4?token=Z1L3YubFiTLfmnCscCbQ3tfAgCVTycjVsgInjtJ_hUn8mWjeMIP__P6gAnAt3OqCICtpPZWN8pFtW-tJiM-YXgeDlklLakz0G8HDNIfqgqxwj050mdgXIMTdFFgSR6iJlnQVMDyZPqk0y8aW7zKcXyqZ6xlRKCIjag3Gxds-vFQwvkeUWP4_A1dg4EA-1KCsbNSSSMLr0MflEfjs2WNFFTkKAZaoRF288JShjsvDxDO1X94g80VVanBrnvwUzn3AGit7W_IMnzYP25SoOEQRxA5m6t5ev3JdNV6MJJxioC02G09JoAmTVmKUfX9pv53L3KVstyKQAFwI1B2uBFdGYQyBQwzYT743Y1P46a8stLghYRTZEDbKRvFpBs224hzXgnV0KKUZN0Ru_3Sif4Ns0QXMCK9-pYBoN1JHS3kPa2-AcLHRCrZBBCT8q3bL39NxPwJdnDZ2KIEhYn7Z8dmFDFv_01dzIWjC7CfQQdU6JyDp_VNrLcSpIn89AwpmWbJbP52ODAL9GBwnlvxTYR_JVi8sJakoNur4ZfHRUB86Fy1wfK91e7wXvKPo3YGc1EPqT7Rc7mbiw5P-lbSiJzYpDE7yhtxi44Yz8S4m5rnfe8tRw5hPc4C9LfO4PBkZgvawvM7NzBkGBurg2IDUeuVFJAhnuRGJ9Z0k2eK07RE-MUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود بازیکنان تیم‌ملی به کمپ تمرین
@Sportfars</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/436671" target="_blank">📅 18:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در  «مسکاف عام» هدف اصابت قطعی قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436670" target="_blank">📅 18:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقام نظامی آمریکایی: جنگ، ایرانی‌ها را مقاوم‌تر و تاب‌آورتر کرده است
🔹
نیویورک‌تایمز به‌‌نقل از یک مقام نظامی آمریکایی نوشت: اگرچه ۵ هفته بمباران سنگین ممکن است باعث شهادت چندین تن از رهبران و فرماندهان ایرانی شده باشد، اما این جنگ حریفی سرسخت‌تر و تاب‌آورتر برجای گذاشته است.
🔹
ایرانی‌ها بسیاری از تسلیحات باقی‌ماندهٔ خود را بازآرایی کرده‌اند و این باور در آن‌ها تقویت شده که می‌توانند با مسدودکردن موثر تنگهٔ هرمز، حمله به [منافع آمریکا] در کشورهای خلیج فارس یا تهدید هواپیماهای آمریکایی، به‌طور موفقیت‌آمیزی در برابر آمریکا مقاومت کنند.»
@Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/436669" target="_blank">📅 18:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuEcCkFf4Td7V5gRN0YtjsL6ObZo9yQ7UJ3DwdhH33lkgppyAXy9lq5gdDxmppQNBAfy2FV9r31kSMzqGdpeGcb5ks5CzbffHnPMh6MT96Sr0efOguv-Pffhrb_3xwEIexB6NFkKSWcb4PG3yQIECaUUxNXxqY2gE-6K7SLqWR0thD8HU4TTWGBCBFUVMQp_QB2TxewnufKsl_bdIQENIibe016GgoDX-3aLLbOdhY-zw7sqOQwvxeg42bHQecJ782xmH2838LoQ6qJPf3P6RTs008TfzDgCCqxkDkYzp0TW3hTDUJNNYcukFi1H6m_VXHjLmwyY2uv2BEqCm5_2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsNTKtNyeyPCmW9hlIw4GAhh2_SpjF2xD3RUCPVnrEGtUEUmlJJwpTUhLY8Wuh9unKrrdtnqWUOcV0O-xYH6yklbOVdRpGyy2MxnuvscmW6SYfJnezVTrqzYjM0ObppSnbuCWxpTg-LU6lAcN1CLQObr0719e901ztlVQTTUjDBJAYQWL6B4MoAHgEYQHJSQ56EM6hV_XZ_jljoeO-mxD97aGSzKUMFYUI4aXhqs-XpLBZoHvye5Ev6-yQpwgBWXY4GM5KfNMBdxZVcKKM2oECZRJqShVNg1SrIyN-71Yn5K6ChoXCPb_hqhS7J4mcTTkR1c097b4EXv07aPiLbcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-nAoxW-yhAlEiz5MrNHqm4Cbjo4ipGFXV6vezIh3zjP_WZWHrv5L8APqJBad1e5NgF4IuPqkNuCkftiR6LW9LDJE2IHNW4dHOubbjvFw9pyggbg3XI6HIIgP90mRIgAinwiZ_eQerRGaN9LGMeJEw1U4hqBq2rSnUVNf5u1-mUIuFA3Sp5B67ooMdoie0BfX6Sa-Q4frU_rbJeQq6ytAygeE92Mj42wvUpRIqcaEm2OBuqzbCGT8PbI0Xl6jTtgX2JL7KSoqhJdKfukxkab9o9JNNVxGRERdw6RPwFlHAcZaIn2unXVWrpaEhD4mwc_QxhQZLKXB9oDPAplhdVLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3E2voU6SylFlVXsVCEue8SPfFqxxhevOnhN4hUnjiADL8s6RL8T65e87ec-bHGS8ecBRL69cdKF43R3ewEeBLGVt0YGSCp1AX-VLsgz_xtzkpTgRPK-HNmerk7mqKpwHZjLi32rWVncqS94c01tPzqi0wqrcZZBGUEceQuD__NJ8s0Y_kDXum9-oBgZmsIT7AoIZV_LNCy8-o_RrtthFW-mSXvtCvwRpRT0zozEC3ojtbSH26_ijZrvSXD9v4rj_Z7gM9NuS9CDVhx65MzsMM1qAOCbpbDCKFHHbhjU2OguyKyeGwXgXuFhnqh9uU5r8hRjVUhGCuh325U-1Jm2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1BAdLNe_OrfLU6JXZjirzmg-1kymiMQKIFPuilBWFzZAnmWo9U4OmY5_8PNyoCOP7RrLAucrvrw4xsw5g02eOmstHU_HetlFWB9vqrVRegCXUFE5g36TtsRcjlRcdY_O8S4QYPTtE5FTSuN6RLfMQkxNBW2EEdxZlBhEh_kD5dED2xN5u5zbezg3rcUxcnmdjFWxM6bF1TxDEVnrRebBGIgs1lwU6KWitgWaKfIrw1hRh-r7AhsJVlwGjv2WMtHNRNR0xiG0zkHrERQuXakNwQiLkLxzyzSGsQu7_FbQbkXWjrLbeI6hII52Bdui-yxYiml-YO1vG2ejLREX1YotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjhcPeiRV_N80ofDIMnTZ59kcOPBsKi8arOBBELA7YnabL4XclzLjaM7QBa3POCVKpZVx5Kz0wsqTQ84mzHWdCBH_WgbeBsxHHdE_YHZkxViC1V1Pmn28swPKGmOnQxxtDWgS6RcZ2SoM-myiIJp9pneFWpoPu6EZTIxDehUMNLvdvqrRAI6vCtpFQfR4P7xVLGGNNVcMpwSgc7f0zQZ1h0UAqLaiPoPucHB6Imzbpb4zr6tBzM380OQ51pR1dU7be6Zsgz0O4Wkr0CeA_rUwavqXPjIAuqoy6hrJFPMyUVZlmzPKGRH1-KGRAasgBg2XaU4f5_XzQN6nFWP2dtKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAHgJWNkkXLf3QihDxDBSdzuRKC4CKxSUz9LuvmQfFFxd1kddADvckpEL-jPQ-oCGEOo6Fc-0eI1LpNtAzj0HV9wHXAG44D9MKgIXse8-Uj8-__A_5u9LWQoKtdQreas1YWUo1hrYu-YXHYxu6d37923R-2CGBhUgrcbXut-PjqpA9bmXTc9IGytO_QlGnYY8chaE8KVk1LBmO8ALuIUi4_mKN2k50-ftUJ1k3tpR28iIp1AyyyiR9Dmn6ZPdQ8efXw_WWns-RSTEJ8TmlLetDyjCCZTeNcBwTHKgDbvjWVwhfXqlCHq38iSZNbsJLxK-7Pd0Une9r8WHCmagtu6eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خرمشهر در محاصرهٔ گرد‌وخاک
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/436661" target="_blank">📅 18:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436659">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر «رشاف» با حمله موشکی هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/436659" target="_blank">📅 18:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436658">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جدال بانک مرکزی و تولیدکنندگان بر سر پرداخت وام جنگی
🔹
پیگیری‌های خبرنگار فارس نشان می‌دهد از ۱۸۰۰ همت تسهیلات در گردش پرداخت شده به بنگاه‌ها از ابتدای دی تا ۱۰ اردیبهشت، ۹۰۰ همت آن جدید بوده است.
🔹
رئیس بانک مرکزی می‌گوید که «این رقم بالاتر از هدف‌گذاری تعیین‌شده در شرایط جنگی بود.»
🔹
به‌تازگی رئیس اتاق بازرگانی گفته است که از ۷۰۰ همتی که قرار بود به بنگاه‌های اقتصادی کمک شود، «هیچ مبلغی پرداخت نشده» و ما هیچ گزارشی از استان‌ها در خصوص پرداخت این وام نداریم.
🔹
افزایش نیاز بنگاه‌ها به سرمایه در گردش بعد از افزایش بی‌سابقه نرخ ارز در دی ماه و حذف ارز ترجیحی اتفاق افتاد. اما تسهیلات بانکی همواره به بنگاه‌هایی تخصیص پیدا می‌کند که ارتباطات ویژه‌تری با بانک‌ها دارند.
🔹
کارشناسان می‌گویند برای کاهش انحراف در تسهیلات و دسترسی عادلانه به وام بانک مرکزی با انتشار ریز اطلاعات تسهیلات، «نظارت عمومی» را فعال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/436658" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436657">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccf5a176a.mp4?token=uNKg6tr5mMlsN54ESapmFR0_9ARSmUNqvma01zzplmyH6RZ2-UrYIo67d6nK6UiCeyMkWkoUjkillkKTUf1BIE1VwNCe8gae7Agn5Mx7_x05pEsfvKa85VpmxUnX1bjgqKKkPB8KuGm2wuMAM6SdtkrGZU3SM-HyvdLR4VmNkqahueBm58yZ9M_iJrYk-LMmpXRGJ85YixfKm5bFINL9aced9Ad0uJtfJTDmnJfmZGIsbwEj4bd16a61N9zFat2h0MRvzS6JxzX5oRNiRI_KWu-mwzB_Tdzosnfp_ef6LR6hW-G1ReP3c3hNm8yo88mYRImp4J462lnZViZZR18S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccf5a176a.mp4?token=uNKg6tr5mMlsN54ESapmFR0_9ARSmUNqvma01zzplmyH6RZ2-UrYIo67d6nK6UiCeyMkWkoUjkillkKTUf1BIE1VwNCe8gae7Agn5Mx7_x05pEsfvKa85VpmxUnX1bjgqKKkPB8KuGm2wuMAM6SdtkrGZU3SM-HyvdLR4VmNkqahueBm58yZ9M_iJrYk-LMmpXRGJ85YixfKm5bFINL9aced9Ad0uJtfJTDmnJfmZGIsbwEj4bd16a61N9zFat2h0MRvzS6JxzX5oRNiRI_KWu-mwzB_Tdzosnfp_ef6LR6hW-G1ReP3c3hNm8yo88mYRImp4J462lnZViZZR18S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هُمای: خاکِ وطن که رفت چه خاکی به سر کنم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/436657" target="_blank">📅 18:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
شبی که تکّه‌ای از قلب ما در ورزقان گم شد
@Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/436656" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کشف نیم‌تن مواد مخدر توسط پلیس بم
🔹
فرمانده انتظامی کرمان: ۴۷۴ کیلوگرم تریاک که در یک دستگاه تریلی جاسازی شده بود، در مسیر بم-کرمان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/436655" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-39.pdf</div>
  <div class="tg-doc-extra">8.3 MB</div>
</div>
<a href="https://t.me/farsna/436653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-38.pdf</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/436653" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436652">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات: امروز یک پهپاد ناشناس به محوطهٔ داخلی نیروگاه هسته‌ای «براکه» در منطقه «الظفره» اصابت کرد.
🔹
تحقیقات برای شناسایی منشأ این حملات در جریان است. @Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/436652" target="_blank">📅 17:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
انهدام سکوی گنبد آهنین با پهپاد FPV حزب‌الله
🔹
حزب‌الله در ادامه ضربات مستمر و جنگ فرسایشی خود علیه نظامیان صهیونیست در جنوب لبنان، از انهدام یک‌ سکوی سامانه گنبد آهنین این رژیم خبر داد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436651" target="_blank">📅 17:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZPq2IX0DChQSZymcO2m2_ply_i5vqaaEvlCWn5ect7g5x5cLNEXpXcOPQMLzxsVCv4Ge9vt3o-8enrlwyDoe1PM-tKYH3_QusLTkEldcwqXvSlJxWTU9a7_exx0KoixS2xALJSBy4QZ7f0Ci5VjV-azfIA-aZGNJDmJXcqJKJq3joZwbSq4qfyJkb4967jGDxRwfips8x0TxPdwVOxV5sCGWb6alMhQPwWn3VM5OJqziWx61F_GDm8k-O-ZJ9U5poK1JWYtePExZdRW5osoPaHIIeb7wCvbnYrLwDA4UOrMPiimyBm3rSfPMSH1G3NgjnxseOLkRp6MwK3DVli8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: ایران یکپارچه و قاطعانه آمادهٔ مقابله با هرگونه تجاوز نظامی است
.
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/436650" target="_blank">📅 17:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d55c2bd.mp4?token=jf1kXzLVQuGZPtYkGedO6MitegKvf61Hdx92w1vGY9eJdt1EdP4QpqHRqi2uecVdkRolUzGiZ4B9P9KRxg1zjb1iCwGShsnyw_qQCKMUls-O4yOA_RN9W5OybZajdVDx-W7U-8PlJI_FSh6PLokSl0uQTzi7_9neNHoVkeuP3q_9_AhRCae6E_Fn1bP90W3pTpnQ-BTExoOa-GE_psTwtachtjz92AQJRkzkmeoXTHmYhiPAYF7pBdoisLeYQ3q3xrUnikT7C16Uhu53iESNsHgwyAv14pUkCmFL8bF9f3stkvQrjTzZXbWWxAr_s_TN7pkTvt8a80QnKEfOwqlkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d55c2bd.mp4?token=jf1kXzLVQuGZPtYkGedO6MitegKvf61Hdx92w1vGY9eJdt1EdP4QpqHRqi2uecVdkRolUzGiZ4B9P9KRxg1zjb1iCwGShsnyw_qQCKMUls-O4yOA_RN9W5OybZajdVDx-W7U-8PlJI_FSh6PLokSl0uQTzi7_9neNHoVkeuP3q_9_AhRCae6E_Fn1bP90W3pTpnQ-BTExoOa-GE_psTwtachtjz92AQJRkzkmeoXTHmYhiPAYF7pBdoisLeYQ3q3xrUnikT7C16Uhu53iESNsHgwyAv14pUkCmFL8bF9f3stkvQrjTzZXbWWxAr_s_TN7pkTvt8a80QnKEfOwqlkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/436649" target="_blank">📅 17:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
ادعای امارات: طی ۴۸ ساعت گذشته با ۶ پهپاد که قصد داشتند مناطق مسکونی و حیاتی را هدف قرار دهند، مقابله کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436647" target="_blank">📅 17:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436645">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436645" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436644">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک‌تایمز: ایرانی‌ها الگوهای پروازی جنگنده‌های آمریکایی را مطالعه کرده‌اند
🔹
نیویورک‌تایمز به‌نقل از یک مقام نظامی آمریکایی نوشت: «فرماندهان ایرانی، الگوهای پروازی جنگنده‌ها و بمب‌افکن‌های آمریکایی را مطالعه کرده‌اند.
🔹
سرنگونی یک فروند جنگنده F-15E در ماه گذشته و آتش پدافند زمینی که به یک فروند F-35 اصابت کرد، نشان داد که تاکتیک‌های پروازی آمریکا بیش از حد قابل‌پیش‌بینی شده است؛ به گونه‌ای که به ایران اجازه داده با کارآمدی بیشتری در برابر آن‌ها دفاع کند.»
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436644" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436643">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e98f32ddb.mp4?token=ffALAa3MeoCi0OzUBNiT0FyyAExSIi20whb9j0U1SKeKIXYVagqpCmbyHRMw8EvhJcRDW97y4KoULQNp9Cya3vOj9y8UA5pk8elHOVcuhV-FQgjlrKawKN_gTahXKlAsnmJAoWMjEHg_cnTqmKBuabkhAl2YDUqMqpdUiwPO-rMHpOmqhqzERQqtbwoFSZX_xqVxgIbMIAen93o8iy4iEVDjdJELgTyXL0yEqa4cNi_SC9lnncn9kW77Q5GJRbzHwHV8laoYBpS46KmsP6TDrLb8-yL-ac7yx1vsUei2_7DoRBi0f0gPDoJmsA6jDF3rdV4dESoQSMXCNNFYiEKrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e98f32ddb.mp4?token=ffALAa3MeoCi0OzUBNiT0FyyAExSIi20whb9j0U1SKeKIXYVagqpCmbyHRMw8EvhJcRDW97y4KoULQNp9Cya3vOj9y8UA5pk8elHOVcuhV-FQgjlrKawKN_gTahXKlAsnmJAoWMjEHg_cnTqmKBuabkhAl2YDUqMqpdUiwPO-rMHpOmqhqzERQqtbwoFSZX_xqVxgIbMIAen93o8iy4iEVDjdJELgTyXL0yEqa4cNi_SC9lnncn9kW77Q5GJRbzHwHV8laoYBpS46KmsP6TDrLb8-yL-ac7yx1vsUei2_7DoRBi0f0gPDoJmsA6jDF3rdV4dESoQSMXCNNFYiEKrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان متفاوت عروس‌ و دامادها در تهران  @Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436643" target="_blank">📅 17:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436642">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okwzwVMjxe7rbuozNctqTuOTKtlmpIRsHxHiv5Jvg6Jp-bV0AlzfLMLZ2qLtYlZc_B0cSk2kczcYph3i3_vHDmKEa_HnxicVQsw-p71XqzlamsPsKlk6WjJCt7GvGDmBSKgKMwt6_jKpi6RslVf8yrlbBo25yiU4KEPKSI_kGYCGs77RF07vrl9SskMI4zFT9pZxrkxBrm5mOguoK1ua5-K-Dq-9le98QDblY5lRfTj4_5jVagSX9dELMhuLVS21Wgembgp3vl3Xnu1NXfcVFbioRsETvpiRZtvdGbWV5hAhX5DeAzEEFuCm-hpRdk20O0_1gHan-uem93FXViI7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پزشکیان! صداقت خوب است اما برای درمان، نسخه لازم است
🔹
رئیس‌جمهور در گردهمایی روز روابط‌عمومی، مشکلات دولت را بی‌پرده پشت تریبون اعلام کرد؛ «نفت فروش نمی‌رود، اقتصاد افتضاح است و کوهی از بدهی روی دست دولت سنگینی می‌کند».
🔹
این صداقت را باید قدر دانست. روراستی با مردم غنیمتی است که می‌تواند پل اعتماد را بازسازی کند؛ اما اگر این صداقت به نقشهٔ راه ختم نشود، به‌جای روشنگری، بن‌بست می‌سازد.
🔹
مردم وقتی می‌شنوند «اقتصاد اقتضاح است» اما بلافاصله نمی‌شنوند که «دولت برای برون‌رفت از بحران برنامه دارد»، ذهن‌شان نه با واقعیت، که با ناامیدی پر می‌شود. فرماندهی که فقط زخم‌های میدان را گزارش کند و راه فتح را نگوید، جنگ را از پیش باخته است.
🔹
خطر دیگر خلأ روایت است. وقتی دولت راهکار داخلی ارائه نمی‌دهد، تنها نسخه‌ای که از بلندگوهای بیرونی پخش می‌شود «مذاکره» است؛ مذاکره‌ای که بهایش تحویل اورانیوم و ازکف‌دادن تنگهٔ هرمز است.
🔹
این درحالی ا‌ست که برای خارج‌شدن از این وضعیت راهکار عملیاتی کم نیست و دست‌کم ۶ مسیر فوری پیش‌روی دولت است:
🔹
مشارکت واقعی مردم
🔹
شفافیت حداکثری
🔹
شوک به بدنه‌ٔ دلالی
🔹
برنامهٔ فوری تهاتر
🔹
جهش دیپلماسی اقتصادی همسایگی
🔹
بازتعریف مسیرهای خنثی‌سازی تحریم
🔗
جزئیات راهکارهای خارج‌شدن از وضعیت فعلی را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/436642" target="_blank">📅 17:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
صحنه‌هایی از هدف قراردادن یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/436640" target="_blank">📅 16:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvzYPEcIf_c3tVhTjcxso9BGoVu6ozka22xGo6tWyemCR4pUknGuveT5Y_JhvuciKEMkCiclHtgambwAT3xeRzPovGB3WJlenpW5aB5m5j7pZleHhZaCij5oanjE0dW0oQhG_ChJUj0PkZ4LcqPRt1xzKhjJ-gKNh6E4DRbXOGAeyPmYpHrYvRK_K2IcwmLHa9X6XN3Zoi0vVOXfttqG9Q6pu8p3Dwvx_YvB9Lapa06B8PXNWxnejeHD60cPpoT1qis_lXl9lDcakBX6lhHf-u6BY51aTNPmmG7jI01kwvSwQtMPNiCuc409JG76cA1u0J7q3qhyfuAoubvoiH9NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیویورک‌تایمز: برخی مقامات آمریکایی می‌گویند شاید حرف‌های ترامپ در مورد حمله‌نکردن به ایران، فریب باشد
🔹
نیویورک‌تایمز نوشت: «برخی از مقامات آمریکایی هشدار دادند که اظهارات علنی ترامپ در مورد حمله‌نکردن به ایران با درخواست قطر، عربستان و امارات می‌تواند…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/436639" target="_blank">📅 16:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCwqKtmTyhl4rq3q6K3X7nYvre_9TTlpcFGHlWgkgVnU1kkwHdn7Lfg9gU9M3Q7CS37YafMDLPVLFopCAk4t967fuQwPgcvVGlF0UNJ-evaurCmbJjlRGI_J5HYK3vwl_1X3vKCNfvR0OJNtYDZrsr7aV71jmONMpO688CDYPXmGoi0KxPS6KiSZxzgisMyUk5TUq2Jx7CwS6-vfW5LMMUXhDZ2ATE3c9AnMzXfBaHFCAw3W24Y-3_-H0vHX1uPMOvSDV_P-ZePUMuNNHQeoB3nxwSvDAqqHnOLbnw25hPIVi6TCq6tg-H_69UleVSEMX0KhiFAxlLkRe_lCu6BtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با زاکانی
🔹
رئیس‌جمهور در دیدار با شهردار تهران، آخرین وضعیت عملکرد شهرداری در مدیریت شرایط جنگی، خدمات‌رسانی شهری، بازسازی مناطق آسیب‌دیده و ساماندهی اسکان خانواده‌های متأثر از حملات اخیر را بررسی کردند.
🔹
همچنین بر ضرورت طراحی سازوکارهای یکپارچه میان مدیریت شهری، نهادهای اجتماعی و دستگاه‌های اجرایی برای ارتقای حکمرانی محلی، تسهیل خدمات‌رسانی به شهروندان و افزایش سرعت واکنش در شرایط بحران تأکید شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436638" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0586d97c1.mp4?token=tAzW5WtEiQKnWx_hsEBycopiz0i2dqXFYtpU_KJIuyxCGjUz4PmQ1-sctq_i-7FOC6oemTvv39FPv1mC5usb9j0_Ec1JDMB1zK7iCWsMLGsg5PpgKPzTJhX5-8GLhVTfphvENjHZFzxsuL8jTpBbHiFX00SRh0fQbxFRonUzP-yELd6qLKX7R1ZUm8rKByyF2Z1s3j3VRfsE1-yhCRXhX1ldHty0VNVJybXk8BnwslZ3cJ6yuaWnEj9WoIgMIjt4KwuF0PoCYz92Umf1iAvf-B96JpknWTpbcRHXSmStnrk6Cuo0d6Jgfqwos62J_HrjSmXOkdH-YV6MysIOkJmxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0586d97c1.mp4?token=tAzW5WtEiQKnWx_hsEBycopiz0i2dqXFYtpU_KJIuyxCGjUz4PmQ1-sctq_i-7FOC6oemTvv39FPv1mC5usb9j0_Ec1JDMB1zK7iCWsMLGsg5PpgKPzTJhX5-8GLhVTfphvENjHZFzxsuL8jTpBbHiFX00SRh0fQbxFRonUzP-yELd6qLKX7R1ZUm8rKByyF2Z1s3j3VRfsE1-yhCRXhX1ldHty0VNVJybXk8BnwslZ3cJ6yuaWnEj9WoIgMIjt4KwuF0PoCYz92Umf1iAvf-B96JpknWTpbcRHXSmStnrk6Cuo0d6Jgfqwos62J_HrjSmXOkdH-YV6MysIOkJmxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آذری جهرمی: اینکه خیال کنند با مداخلهٔ نظامی می توانند تنگه را باز کنند خیالی باطل است
.
@Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/436637" target="_blank">📅 16:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5b66a691.mp4?token=nX-6GGHUEYyOBAnMHDDF51Fm2UYVLJKibzsbmzkcfhchDY6PMdcvh-sBHeZd6fPrI5mno6XIE_4Jr1ZFDB4hOQfTZwEpfy89EVftIOCDNby060Ul6Aiv-_7lf85-vLxfPSor_TpIOTtjahV3I9V6KdprfP5uEGczSKVuSmhgVfH9xU-Ha-4ECe7ue1WLx1egarPM9tmQGPeV9wvCnB8XLcS3RVDUKGFvBmXfbXPTOGgLxAGKKJbTXczfEkcCrFg-yLjRNaAXJ2flgbNQdF2Ux8cFy7gx983UUXSFmgVQI0BcftuwH_5jVO0hM_XT_0khUonRR6W4qObwNgNXMdPTOqyG2Be4i8THQpJI0wtR4MOitPzAk6hWKzJ9uOga0r-4MHFGkSBOlW9Y_MzZmqboMJr7jSirCG5hqEwHQbr2RzAe9nMcvSVIwAx8FNEGLq-M4wT0WRevQ5-EHhaIA6JTUZAKKOgmET6ROSMtr0_wspBTaQEg66y4vDMbv17DFsS4k2PLhsDMdAeryI0CrMSfA1hRwfpuZvd18zCtx3lFep39KqnAQGOw-UhiYlO6tINl01_4izPL97cWJeXWv0N3ABTEfpd-hQOxLdCB5D7u8aHLqKDrRpvthPYlDyGlowcW8iboXCMNZE-xb0bn78SnSle8Gg8eoXQueqnHtacjnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5b66a691.mp4?token=nX-6GGHUEYyOBAnMHDDF51Fm2UYVLJKibzsbmzkcfhchDY6PMdcvh-sBHeZd6fPrI5mno6XIE_4Jr1ZFDB4hOQfTZwEpfy89EVftIOCDNby060Ul6Aiv-_7lf85-vLxfPSor_TpIOTtjahV3I9V6KdprfP5uEGczSKVuSmhgVfH9xU-Ha-4ECe7ue1WLx1egarPM9tmQGPeV9wvCnB8XLcS3RVDUKGFvBmXfbXPTOGgLxAGKKJbTXczfEkcCrFg-yLjRNaAXJ2flgbNQdF2Ux8cFy7gx983UUXSFmgVQI0BcftuwH_5jVO0hM_XT_0khUonRR6W4qObwNgNXMdPTOqyG2Be4i8THQpJI0wtR4MOitPzAk6hWKzJ9uOga0r-4MHFGkSBOlW9Y_MzZmqboMJr7jSirCG5hqEwHQbr2RzAe9nMcvSVIwAx8FNEGLq-M4wT0WRevQ5-EHhaIA6JTUZAKKOgmET6ROSMtr0_wspBTaQEg66y4vDMbv17DFsS4k2PLhsDMdAeryI0CrMSfA1hRwfpuZvd18zCtx3lFep39KqnAQGOw-UhiYlO6tINl01_4izPL97cWJeXWv0N3ABTEfpd-hQOxLdCB5D7u8aHLqKDrRpvthPYlDyGlowcW8iboXCMNZE-xb0bn78SnSle8Gg8eoXQueqnHtacjnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدواج
۱۱۰
زوج‌ جان‌فدا در میدان امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436636" target="_blank">📅 16:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3C2x2tJ5okabFcsUDor3tMGe9BROMAqukrRBoF9D5HMHsrFebmzc5RzJ1s7RTZIjH86rYxuOObLy9hcqd9eYhdo8dVAgI60zgF09sXLRh9fVYGOCusWHoPRI_JVc2ad1M1S4GZMWLL_3Vm0QHwewtqu6a6q5wymN55zDDAkrBBbRI7erUtlCPyFZZWl1Ij7BKlXtcHcT5nArkOBeddX6tIaRPFCjWPtDAbInIBnJWagKsdJNSbOYf5xrs-tCsvanDeYHe6BCm660YfC1zJbRX1X5NiiQLqwa_iUuhOCbHsCfNdFxV8BJ8FVekwZQwJfwyAARq1wivsBmYVzHfcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین نیروگاه خورشیدی تهران در آستانهٔ بهره برداری
🔹
بزرگ‌ترین نیروگاه خورشیدی تهران با ظرفیت ۶۳ مگاوات در مجاورت شهرک صنعتی شمس‌آباد در آستانهٔ بهره‌برداری قرار گرفت.
🔹
این نیروگاه در زمینی حدود ۹۷ هکتاری احداث شده و شامل ۲۱ واحد ۳ مگاواتی است و پیش‌بینی می‌شود بخش قابل‌توجهی از برق شهرک صنعتی شمس‌آباد را تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/436635" target="_blank">📅 16:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
نیویورک‌تایمز: آمریکا نتوانسته شهرهای موشکی ایران را منهدم کند
🔹
نیویورک‌تایمز به‌نقل از یک مقام نظامی آمریکایی نوشت: «بسیاری از موشک‌های بالستیک ایران از غارهای عمیق زیرزمینی و دیگر تاسیسات حفرشده در دل کوه‌های گرانیتی مستقر شده‌اند که انهدام آن‌ها برای هواپیماهای تهاجمی آمریکایی دشوار است.
🔹
در نتیجه، آمریکا عمدتا ورودی‌های این سایت‌ها را بمباران کرد تا با ریزش کوه آن‌ها را دفن کند، اما خود سایت‌ها منهدم نشدند. ایران اکنون تعداد قابل توجهی از آن سایت‌ها را بازگشایی و پاکسازی کرده است.»
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/436634" target="_blank">📅 16:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YouZXB41L6h8a8fK54VZgv2BSKihUYc7TvSVuB6CrZPA3AqtZp3kZP16iZRacaRlcp7WE6jsBlYY8PUekwyu1MQCNn4HOISymCZIHwFlDWdyTNGTfuukpn7hwarMbBSb4U5gaJm43hYa6BwykfPNZ0e_rLC_5rsOQU2gbhg233cYX7zO0YDRTC6F5UNAHtN-LgZO1rxwEyy7tt3ArppR4oFIJVA0UbeT-8nhd1bwT2YV1xsShgL3Pv6C65lwJ5tCe1KfxLRZAgZ8HdurYFxFyhIQITMFwQ8xsOs6t9MhPt3gFUW4kunbQccfgvAa6JMjIMO8gEb7iNex3JTsKO4pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زمین‌لرزۀ ۴.۶ ریشتری در عمق ۸ کیلومتری زمین، حوالی نورآبادِ لرستان را لرزاند.
@Farrsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/436633" target="_blank">📅 16:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO0LFKvcTzpT7BkoJhjANYbh1aOSaQtvRQNBSqS4z-WoBDBq39jqDUbAzR5jMmc_LztMxAzwrl3xYHT9y4G7pk3njkyhsIqzMcN9CFGdzfbjiOjU3bHzz3BN67ODoCOH5eDe9nbGBuFe0fzwPtIy_nuoGOtTkWWSdFCBN0NG6HPRBKTWTIM1Gelua-18yZ2p8R8kOpELAXvwhB5c4NTEVETU_cAhxAV2w-t0R_GopeHXWox_ue6J-SQi3pC6jBUF42iyfw03etn7244ywn_kDv5QaYbGcW8jPBci4_u7hweBL3ciGiSWDg0CwexJZE4YmgEh2X5uVSaU1Fc1dsE5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتکار ۱۴۰۰ تنی مرغ منجمد در شیراز
🔹
تعزیرات حکومتی فارس: در بازرسی از یک کشتارگاه در شیراز، ۱۴۰۰ تن مرغ کشف شد که از ابتدای جنگ تحمیلی در ۹ سردخانه احتکار شده بود.
🔸
یک محمولهٔ مرغ منجمد ۹۰۰ تنی دیگر نیز روز گذشته در شیراز کشف شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436632" target="_blank">📅 15:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر «رشاف» با حمله موشکی هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/436631" target="_blank">📅 15:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz09N2eXNmimwOzzxS-O2qLDys3fNOx2ERxtDjE62dtxNFnDn3nz4_kBaYRQzMMcOsSlDhHA5culj4lA_XlegJzVel-I0-Qrk4uBPEYVCQMcPd8nlLciV-xAE4tH8cEB2RaxJ91oN45lNFY26hq9NB48nNyh0VZTqNrgl5ygdMVwttXh7vgYh0e9WIe-0PfwLc-XrZQ-wNDso6b-WToiofo4AhNit7fgqutMyDDzmsuJLFkGAZJM4lLES6mMh-kipv6xgbQazuVj4Ng9A95GOSGnaUEzqVqhelUhvZ33vZWxg3DDfO8wqSOFP8AST-U-ITe-lUq9jxgQRE7DIsC-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvXcbyXO5jru04HXtV-_gmhullz-fbz4J6qysYgc5ryl_46DH4Qr-A2es-BOY2C1YWvdu_5BEPSXN6YG9HJSGAheusH5dI07Ko24DifQ1-CzIQCXjh5qI7uvyC-PHwx7u75QboGpdgpIFMGyUJ-BPjgWrL66udMyTM8xpkkI0A80P-HgFhkvEPj4bGwKkEqBxIUOPQXAv0qtH6xvROaSIl6AL54a_iiu6SkFcBRWbEftZLGe0bvC5QgGPcOygMIkKwIr64khMOKD7rHl2lw9iR6A_3iLbLdNcHcTrO-y3XSol67Zuc7sz5_4fV7nrfZtj_wtuAe_qyPrjfBq5EMPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUS-voQ3etZwvYlOK77dfDHWJb_IXnfQ0Ac3a8xoRXoaQDD85ePK9UWi6bwQLJa8V9092ppEN8zxL7iVa4VTQ89JoPbodDGc-1hPF9KJxKjABtn7oll9th4FURAy1-aEjSnG-AV_R8lBYBAaRbl9AX8GznlW3hzliM8NtK-GlvSy7ETpIm8UxOZaDVBCcpo-uXkr7dxmBIxpRlvniqxvkNi2SN554F5_jjxNvmUfewQbRbLxtiyN0CTiJAhWSfHHX2r9JUX3kD5ae31a73PsxxmE3MDCNq3v0zFaIOKN09NkUmLJlWz2yGTaeV6qeBUdZT51in6DTJAeIjnwpyqNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1epNCKUY1ir7ruFWghgZpjg44uhk8sGABvR41MqjEMz_hwTLyLbJLDR5VG56dBbLs2pzzdq84onZevs2fYorZGu-gGp6Zno6NRqnw0pzgShTaVBwYmPFkjKRTr9_wUI8ZhDcYEShkhzaLn52IfGLKHOAokocz24iSTifcDRIfMfoflkuBk77yS5YCLEl9F0JAfS6Aqc1mXT4sz1SbzmoUzkJKfjvRMlB8oAUs9Rgfkwbmyk8cfcX2EU6gBo46G5PIGBOqjqGHPaT_1NWUfZR48b9idJPsyIGBi7v_ivLCWARuHcaADBJBU1xfWrTk2myIqME_g18qVplnwNaSZWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6BFmxlAPSf7XNtf2ezW5r_FKW5adgYiPhdXAWAG1xZEBBoRqSSitwzgMCizy3sIOHLOp74ckdJuKiAa4m0rRN-_XqwThyrBw_Tr0FHRAD6GemaSrbut4NZJPcWWah4vkYftQzdVqiP1u5VlvcD-riMstQnsHQktTgzV6yaAmSVulEvJgQCM7GNJiFCCf1U_XeaACOWyV8SvAn5Y6Th3M1vAecoBq4qDmDNxidK12TS-6CgREuViph6pQrsRYRjFSl6gStqtJz2Y39meLL6bCkXFNNCp63WjD8LF21TrysMGX1BKxI_49O3G-vsdlbeWUhxGRdYVYILYqhWDy3l2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUtH1wII4zBik6yH9C1HtKiPVBQNsunURnku2vKVXgtL16Mr-5s46uCr-N9jUu0w4aXLHLC9m-tHUzR12wqT4dkJ0FOiGNe8T3T6c0N3qx1w13ExxHp53PRjUKlv2aUnPYNKhpZFpgovky5wzI4AUOB88g1kfPtxo51OKZHCKTxq_KgqEQXoaTK6czCkFyZQ-9Sl4DyGtHCW5xhJ38jJy86A3M0n5kf3N1dtFCWx21hKLPHASPj4EGNie3_YBbCToAP5FWAhAQ-R_nqo0tMgc9Mq-_yuq3XEae4V0CPcmQz9NMshpb_ly3A2joRIB0bDHQj_ZWf_NBHdd7PZHsay0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تمرین بدنسازی تیم ملی در آنتالیا ترکیه
@Sportfars</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/436625" target="_blank">📅 15:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی: در ایام جنگ روزانه ۱۰۰ حملۀ سایبری به کشور می‌شد
🔹
در جریان جنگ رمضان روزانه بیش از ۱۰۰ حمله حرفه‌ای به زیرساخت‌های کشور از جمله حوزه‌های بانکی و انرژی انجام شد که با تلاش متخصصان امنیت سایبری، بخش عمدۀ آن‌ها با موفقیت دفع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436624" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAuCJ6lJb9j5mFOMJGMQRzo7Sk3YJQ7rrG9kmMGjlFZB_7M89bBTOdxuHQDpyMX1PFe3nxJdktFzcZ5-85t2jQC5fOwsofqOwR6mf6YtJ8b7YryFze5pIsfpU_fDoOgNMp6E_gikrhoygZH2KcEVPiiJTo2rEOU45oQHzp5BnT8urG8fj-OH_6jJ8_Sex_8s9OFN-ALZdz2lMIRCUX8uePTSGZbsG129qDpKNVQA36TLiBxHPZfmUFi25Ya4XLhZas6QBf7hWKh6S4Afj16acDDZoNVGoRE3YQafeLSxnsu2RwX6kZ_80zB-NKuYlg7YMrhw7i139Tp3Ws2y0dbL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقدم‌فر: مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد
🔹
مشاور فرمانده کل سپاه: تحولات دو سال گذشته، به‌ویژه جنایات رژیم صهیونیستی و آمریکا در غزه و همچنین فساد اخلاقی و ساختاری رهبران غربی همچون ترامپ و ماجرای جزیره اپستین، ماهیت پست…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436623" target="_blank">📅 15:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp6UYwoNoEB8dlGv2A0UdKxtgD3F9sF35eYFfmpbF5qWQdtDphisOYxrO9a8q71vR02pM-bpEd8IQQtGr5wSMitEUNc-Kn9unkgR98sgQzS02KOnx5_0Z50FFRZe0yoPK8ZUa1-kaZNBpyZbPsUkXhOc2oiA_QZiZtX0m-I3rJASYj6wrG4R2EshH9wbsTFs3IQFGiHDOP8XW1F7ltbWarViFbmUZFA4R1xINpchoZP6f9g8h_KjKW2wiDGWihFJ3Men8po51mdHRX7jsljaNFF8Us7uvXgqAP53YOqoEgR3nyF1uUobCV96WdtAjIbDY5Oi_b5CwRHwhb8wi9rtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیلی فیفا به پهلوی در جام جهانی
🔹
نشریۀ اتلتیک از منبعی در فیفا اعلام کرد که این نهاد قصد دارد آوردن پرچم‌های دارای شیر و خورشید را در ورزشگاه‌های جام جهانی ممنوع کند.
🔹
در جام جهانی قطر هم برخی از هواداران پهلوی پرچم‌هایی به ورزشگاه‌ها آورده بودند که از سوی ماموران جمع‌آوری شد ولی این‌بار اصلا اجازه ورود به ورزشگاه‌های آمریکا را نخواهد داشت.
🔹
طبق قانون فیفا هواداران حق توهین، سیاسی‌کاری، بی‌احترامی به پرچم و فرهنگ کشورها در ورزشگاه‌های جام جهانی را ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436622" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
منابع خبری از انفجار یک خودروی بمب‌گذاری‌شده در پایتخت سوریه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/436621" target="_blank">📅 15:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrKbY6YyNYoWKQtGNZYL8zVyKdSjG3MsxP3lspLElDwVZt0ItC7SYpVdfKO9aJsRbSEI8hNQOlBQNBa1MGN1G27vSbuOjk31Od98Q9Slv6vshT5f50KoM56bQkAiTfSiHtRXOdI7zeTePmBo-SRTT0NhxY3xRdjQUlSnDiffyWVLEq6guLdTekYZqVsl8d6Hq6EmAuwDXPbKq65uY_0k8eBKg-I0UfY7FFO0q5O82cgsnixXPGbPltI2BPNLzYYrzA02syMSazQpYtK00zepYn4GmqM9PJWkCnwQh6kZAChJh_bxOXMsaWn4_aTOaTM8QivP_1Z2db_JDqZAMZpy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست تا زمانی که تعیین‌تکلیف طرح پیشنهادشده به شورا مشخص شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/436620" target="_blank">📅 15:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌ نیویورک‌تایمز: برخی مقامات آمریکایی می‌گویند شاید حرف‌های ترامپ در مورد حمله‌نکردن به ایران، فریب باشد
🔹
نیویورک‌تایمز نوشت: «برخی از مقامات آمریکایی هشدار دادند که اظهارات علنی ترامپ در مورد حمله‌نکردن به ایران با درخواست قطر، عربستان و امارات می‌تواند…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/436619" target="_blank">📅 15:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBN0hqKgozrmX8ejhVpFBrUBavSDl1QO4Yh3k3SoG0lTNCBCqR6IG6vN1Q9cHDBQB8mPJhggd_hRSQOK9udJ2UBOci2sCTSmiCDUHCn1gP2J9nPZzJyTgecnsDzlkAa9kHWAJAI-QllAnxZdSNaBMQBiQljK0Mzj7RMwuOgJ50xmGK3BQzQW6SIJKjEmhbZOLSBjT4CdTKM4LccNrdV05ci_R03gRt9tkvTAFR8FbzgOkViQ-JE-SVN6KfINHvGIZZBLE-26uRmwzmZ5YV9If4tRIUd10VoWYO_iC36-JCA3cFJQAZ-1H6D4QOweOljt2wEQgAeSq2nBXWfLE1dAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشترکان پرمصرف برق در تهران محدود می‌شوند
🔹
شرکت برق تهران بزرگ: مشترکان بسیار پرمصرف برق از ابتدای خردادماه با اعمال محدودیت در مصرف برق از طریق سامانه‌های هوشمند و پایش‌های میدانی مواجه خواهند شد.
🔹
ادارات نیز در صورت عدم رعایت ابلاغیه هیئت وزیران با قطع برق مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/436618" target="_blank">📅 14:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📷
زوج‌های جان‌فدا
🔹
همزمان با سالگرد ازدواج حضرت علی(ع) و حضرت فاطمه(س) مراسم جشن ازدواج ۵۰۰ زوج‌ جان‌فدا عصر دوشنبه در میادین اصلی شهر تهران برپا شد.
🔹
از این تعداد، آیین ازدواج ۱۱۰ زوج در میدان امام حسین (ع) برگزار شد.  عکس: صادق نیک‌گستر @farsimages</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/436617" target="_blank">📅 14:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">توقیف اموال ۵۲ نفر از خائنین به کشور در زنجان
🔹
با دستور مقام قضایی، اموال ۵۲ نفر از افراد مرتبط با شبکه‌های همکار با دشمن در زنجان شامل دارایی‌های بانکی، منقول و غیرمنقول به نفع مردم توقیف شد.
🔹
از این اموال ۳۳ مورد در شهر زنجان، ۱۵ مورد ابهر، ۳ مورد خرمدره ، یک مورد در تهران و خدابنده شامل وجوه نقد بانکی و ارزی، اموال منقول و غیرمنقول و طلاجات می‌شود که با دستور قضایی توقیف شده و بررسی دقیق‌تر ادامه دارد.
🔹
از این متهمان تعداد ۷ نفر در بازداشت و تعداد دیگری نیز درحال‌حاضر در خارج از کشور به‌سر می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/436616" target="_blank">📅 14:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صدای انفجار در قشم مربوط به خنثی‌سازی مهمات عمل‌نکرده دشمن بود
🔹
معاون سیاسی استاندار هرمزگان: صدای انفجارهای شنیده شده ظهر امروز در جزیره قشم، ناشی از عملیات خنثی‌سازی مهمات عمل‌نکرده متعلق به دشمن بوده است؛ ممکن است طی ساعات آینده نیز  عملیات انهدام مهمات عمل نکرده ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436615" target="_blank">📅 14:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918f9837c.mp4?token=tJo0nMZK9yiext3jbPbIKTF-SXxCK67bkoaJ_xWMkjfZmgT-y-kA1a7EKKcHNpfvCuofn6gWbmbX-zdKukQ63AkfzIS_fzmnqdKYuuvUzCPvy5uEr4IRko6CyAZ0VP8ka-zNblIs9cRtEu_P1rwF4UcOIQsgrcGX5SlDv3cJisNHaRmpOLDUzvXH_pFWpfVa73yj6IqkXC2FHsv0wknZ2My92q10anvSdtqWQYq6u4N_csS7CG96tlqaLwXf7pbPmYia8rSHxEizIw3sTXzCh89SYwuBbFyEf2RTmEo-m4jED6R1j3btOjGI0mNth_ob9db-5MLbdtzg7e6rRmmZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918f9837c.mp4?token=tJo0nMZK9yiext3jbPbIKTF-SXxCK67bkoaJ_xWMkjfZmgT-y-kA1a7EKKcHNpfvCuofn6gWbmbX-zdKukQ63AkfzIS_fzmnqdKYuuvUzCPvy5uEr4IRko6CyAZ0VP8ka-zNblIs9cRtEu_P1rwF4UcOIQsgrcGX5SlDv3cJisNHaRmpOLDUzvXH_pFWpfVa73yj6IqkXC2FHsv0wknZ2My92q10anvSdtqWQYq6u4N_csS7CG96tlqaLwXf7pbPmYia8rSHxEizIw3sTXzCh89SYwuBbFyEf2RTmEo-m4jED6R1j3btOjGI0mNth_ob9db-5MLbdtzg7e6rRmmZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: این ذهنیت مردم که «کارمند ما را سر کار می‌گذارد و کار ما را انجام نمی‌دهد» باید حل شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/436614" target="_blank">📅 14:35 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
