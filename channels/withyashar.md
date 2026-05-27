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
<img src="https://cdn4.telesco.pe/file/hWV4OsRIDT73jXn9pV8uRHeN8fLNdlSkujKgBDV0kOz2afg5Fxp3CtQPZnUXMxGEcuQJrSw38TRZ3bkEQRFoXLxLz612hU-bqRnDgzm1-UomoYl3Q_Dys6EwBF1sRErRPpjWj7XPEpioTiXu33ei1aiZTRd7EsH0QmGdOF81O65GTJ9ajWGLunFobda_rcYqAS7YVpEJ_tHCYEPgUA-4iRh4tKARKn6RIgombdQksn-Sgv88CpxdG9FBm4VUtTGdQOcJJJcbWOO9YW-z7efg5_7X-6P1rc7wcDH8orqAmOFwE_f_zw0494aPrGksT_znazmziS_-CEOgaFR2tquHPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 276K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-12661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a0b3327.mp4?token=C7dTtL2-FhoIrk6fuShatApsj0W2hsse39WOThXXdvPjzFQR5FnCg0xgkIdPUxcB-ZZkO9tOMoWYj4P677acfHMm6FBEFsP-XaMm5llVb65LruwIZZqLfSqk4KWfQUSvY8M92Xue1ZvuqwrEOk_J2Ezn1gzTfeBrgVZ4RQqB0CW33PxxjxzIT_WKjnwNpTmLE3tRzwHEZ-MmRfTMKHG3r8DayatlDpJNlNQaEXYnxLj-biHkynVxmrt6T5C-quFczV6ZHWRSY2rumdh5m5mi6DO0ZJZsJimEKpfx97PUhkS-HhrqQNN6QYqTVWpF_mfkYiMLFAkmG5ZhZGrN54845w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a0b3327.mp4?token=C7dTtL2-FhoIrk6fuShatApsj0W2hsse39WOThXXdvPjzFQR5FnCg0xgkIdPUxcB-ZZkO9tOMoWYj4P677acfHMm6FBEFsP-XaMm5llVb65LruwIZZqLfSqk4KWfQUSvY8M92Xue1ZvuqwrEOk_J2Ezn1gzTfeBrgVZ4RQqB0CW33PxxjxzIT_WKjnwNpTmLE3tRzwHEZ-MmRfTMKHG3r8DayatlDpJNlNQaEXYnxLj-biHkynVxmrt6T5C-quFczV6ZHWRSY2rumdh5m5mi6DO0ZJZsJimEKpfx97PUhkS-HhrqQNN6QYqTVWpF_mfkYiMLFAkmG5ZhZGrN54845w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو شورای اطلاع رسانی دولت :
چرا رسانه‌های ضدحکومت دچار سردرگمی و بی‌برنامگی شدند؟
@withyashar
یاشار: چرتو پرتاشو کات کردم ولی اگه ویس های دیشبم رو گوش‌کرده باشید این قسمت حرفش درسته ! ما باید تغییر‌تاکتیکی‌بدیم یا منتظر همون معجزه باشیم که منم گفتم !!! ادب ازکه آموختی از بی ادبان !</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/withyashar/12661" target="_blank">📅 13:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه I24 NEWS: نیروهای دفاعی اسرائیل (IDF) و فرماندهی مرکزی ارتش آمریکا (سنتکام) در حالت آماده‌باش بالا باقی مانده‌اند، در شرایطی که احتمال شکست مذاکرات میان واشنگتن و تهران و صدور دستور اقدام نظامی از سوی رئیس‌جمهور دونالد ترامپ وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/12660" target="_blank">📅 13:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الان نزدیک مجتمع صنایع فولاد مبارکه @withyashar</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/12659" target="_blank">📅 13:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/12658" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fc7b1751.mp4?token=opxEDO92-y1aFfCf_Mp8Q5qWG-G3dww4U94n1JtqhZxIDR7MgvGy8o_n1k3Dv9ykij4LSnFq2ZbFTR9bf6gjWfB881i1BUgb7BvfaU8e0JJb2gV225MPZNyphIKyxvirkymoeu_2mLBrFQ-2kVj5WpRqWNB71hkMQARUYMi5lWYNhRKsJypr9jrYYamR-y2XtjgaYI7EZuXYuHbNeYMiyGPe1ADMz6_WmkLdygIJ03uTxpozxPp1IgnZGoThlceEUUEIncoMX0Dn7fDJk-tHLtJCcY4eA_HM1bz7PXLEv-DIyFBWLHqwix4ZBSmc_5BEbDuyk18qE2FSq0R_bizm2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fc7b1751.mp4?token=opxEDO92-y1aFfCf_Mp8Q5qWG-G3dww4U94n1JtqhZxIDR7MgvGy8o_n1k3Dv9ykij4LSnFq2ZbFTR9bf6gjWfB881i1BUgb7BvfaU8e0JJb2gV225MPZNyphIKyxvirkymoeu_2mLBrFQ-2kVj5WpRqWNB71hkMQARUYMi5lWYNhRKsJypr9jrYYamR-y2XtjgaYI7EZuXYuHbNeYMiyGPe1ADMz6_WmkLdygIJ03uTxpozxPp1IgnZGoThlceEUUEIncoMX0Dn7fDJk-tHLtJCcY4eA_HM1bz7PXLEv-DIyFBWLHqwix4ZBSmc_5BEbDuyk18qE2FSq0R_bizm2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان نزدیک مجتمع صنایع فولاد مبارکه
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/12657" target="_blank">📅 13:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/12656" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079db554c9.mp4?token=WZroYBPdoHLgD96XWnQr49dWVXt5tXoPgDG0IfRal36FEUMlXH0GgTjT91KJWHT0d-DeO5iYJJwD7fCz8PJvo2zMwOBUqQw-AKkzs7D2WGrXEUq4b5RWs60H1Ag6-aL7UAglCFdrm--EEvF8MrYK1nFzmkHbgP5uSVrxB87RLgFWtXLest9obnAwMhGYZnJfRv4gGvddOZ04M8i5AOjgbQlpdqNjp8KjRztU2NODaLQh7EiOqbMdVIn23U01Y5YQR_zeTgM13dHZYn9aTZai6--8tAOFKAnDNvukK7RkpaYywZwwCc-MraOoDVHaq7aA7kCrvNicqB7lQ6SEQGWuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079db554c9.mp4?token=WZroYBPdoHLgD96XWnQr49dWVXt5tXoPgDG0IfRal36FEUMlXH0GgTjT91KJWHT0d-DeO5iYJJwD7fCz8PJvo2zMwOBUqQw-AKkzs7D2WGrXEUq4b5RWs60H1Ag6-aL7UAglCFdrm--EEvF8MrYK1nFzmkHbgP5uSVrxB87RLgFWtXLest9obnAwMhGYZnJfRv4gGvddOZ04M8i5AOjgbQlpdqNjp8KjRztU2NODaLQh7EiOqbMdVIn23U01Y5YQR_zeTgM13dHZYn9aTZai6--8tAOFKAnDNvukK7RkpaYywZwwCc-MraOoDVHaq7aA7kCrvNicqB7lQ6SEQGWuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
مخصوص‌ پیرمردا</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/withyashar/12655" target="_blank">📅 13:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/12654" target="_blank">📅 13:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/12653" target="_blank">📅 13:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Fatehi</strong></div>
<div class="tg-text">یاشار جان
اینترنشنالیا دارن میتوپن به ترامپ که بزدله و به ج ا باج داره میده و عقب نشینی کرده
تقریبا رسانه ها شدن این.
ولی من هنوز یادمه که میگفتی ترامپ فوتبالی بازی میکنه که توپشو نمیشه دید
هنوز این جملات و حرفاتو یادمه
بگو، خواهش میکنم بگو، که این رسانه ها همه دارن اشتباه می‌کنن و هنوز  ما اتاق جنگی های قدیمی دارین درست میریم به سمت قاهره.
مرسی ازت
❤️
#دیکتاتور_مهربون
❤️</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/12652" target="_blank">📅 13:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال‌استریت‌ژورنال: دولت ترامپ در حال کاهش نیروهاییه که در صورت بحران به اروپا اعزام میشن؛ اقدامی تازه در راستای کاهش حمایت نظامی آمریکا از متحدان ناتو.
@withyashar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/12651" target="_blank">📅 12:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEflaeAjNzU1T6V9_89u3GqlwCrqNSLSvNc96MarnSY3Pz1gfexcC4LbUVJF1pHZLc5rm0OBH5x-n__lN4NkhM7bqdpj8fguvx4nQlwwUATt8UZ459euOT9FvJZpyD8kHrqQ2zDtBpDEXyvDMfgksn7hDDJ4hLF_VXEhmcFydF_SNLpB5bM0i7RnIbF3_wzPOv-gh9L8sScRQ_V2OCQgPAmLiFXavExI7Qwe8rPvih9MOc-9k8fopIo2-p2_zNh-jUZGTSL3zg6hYz4sugWx6fWQHHqVggFo4xJ9VGS80V5ZuhfEDfVXEirWdssuHHq9rvN4Hj5bxZXKEJwK-WxyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان ، تهران شوش @withyashar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/12650" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارت اطلاعات ایران: دشمن برای دامن زدن به اختلافات ملی و فرقه‌ای و انجام عملیات تروریستی در کشور تلاش خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/12649" target="_blank">📅 12:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باقری:
ذخایر اورانیوم غنی‌شده ایران در دستورکار مذاکرات نیست
ریانووستی به نقل از معاون دبیر شورای عالی امنیت ملی ایران:
ایران و ایالات متحده هنوز در مورد
رفع انسداد تنگه هرمز
به توافق
نرسیده‌اند
.
ایران و عمان
در حال مذاکره درباره
رویه جدید عبور کشتی‌ها از تنگه هرمز
هستند.
تماس‌های
غیرمستقیم
میان ایران و آمریکا ادامه دارد.
ذخایر اورانیوم غنی‌شده
ایران در دستور کار مذاکرات
نیست
.
@withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/12648" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-NrdQAKZvpl4e34BymmFsoYywbgNN1qpgLTppS1YRypVgjqXDY0Yl1WqqB5wFLdfB-y_JQt2I-q0_wXwuK0ExjiswO6wiJ2dLTM3Er7ANUMnI-s35iWn7Q2V3la9OWfPPgu33Qb55tG3rjSdDLJgr687wjCpYsIuqUp_SzOk1Fd6F-3x-uxldgKzcXJU3yBfvj6WLwwFnijeofUkb_Vad_Gu4KCfOWtXT_hOaLbtGpgzAhtXtzMmyz-WKMo8tV6FGgPGuxfe8QcwU7UIc9qSoSw-GeWZlWfhVZNxRTxJ5t5Vw7yU66Fedr1YablO0dyi72PKIYnKc5_GiZPdChVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان ، تهران شوش
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/12647" target="_blank">📅 12:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : تو نهاد امنیتی، هلاکت محمد عودة تأیید شد @withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/12646" target="_blank">📅 12:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درود یا منظورت حمله اس یا که اب و هوایه سطح کشور مثل تهران اصفهان هوا خوبه یه بررسی بکن ممنون ازت</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12644" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙒𝙕</strong></div>
<div class="tg-text">درود یا منظورت حمله اس یا که اب و هوایه سطح کشور مثل تهران اصفهان هوا خوبه یه بررسی بکن ممنون ازت</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12643" target="_blank">📅 12:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12642" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با یاشار : کمربند ها رو ببندید
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12641" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارزیابی‌های اطلاعاتی حاکی از آن است که برنامه حمله به ایران از دستور کار خارج شده است
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12640" target="_blank">📅 12:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شبکه NBC News به نقل از معاون رئیس‌جمهور آمریکا ، ونس: «من خوش‌بین هستم که ایران در هر توافقی، با عدم توسعه سلاح‌های هسته‌ای موافقت خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/12639" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ics5XyTTV2YNp9LMOX_POYU-vgUZoo1L8p9Qtcrmy30b8sef5UZS-gHu_U_9szaDk8zE82jJgYDGooUJNLDZkAunisRWYK-lByIuuauiDZpceg2zd4XX-nMlYClIJaSQ69bBVXrAKGjEl57QNS1f9satXVEUkqPqV8uzimhK0CVdlqb3x6sjyrww02yglWV9PlPaW-BpSXYU8dIT19uGSr0QhbrjKxasGMpfZjjNmxAgdB_TeLMal62YHWBZMQ4JGWSjEfK93480_XMStmQfnlLXGKoxNC5L6tou26aXQbbKBqwHKH3d9aMExd7HPFOg0vegKRDEFET367YZ-koq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد +۱۰۰کا ویو یک پست رو زدیم اونم در ۱۱ ساعت !!!
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12638" target="_blank">📅 12:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12637">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKL2oHUESfjIM5rl_kRHFuRYTd59FlJFvt0Ih3TA3w1r1Z4UeGLKf_45WkorrDcijLhExqPmuUoI6t4NxF4TFWwOg0y7j877YcrDzuvBTBDIrXjohp7Rr1NC3dAu5o5YO0yXE4TUiK0vs64KsOlZmswlfaTKyVf83JsFYZyCuKKUUc0siPd9IaYfqvglfOMS2zRidRh3Vza1BiTg78_mV3XFyZRbquT5rpl4GoLSvugE0K_-EGqjje6b8lN_ZWrfgp_xq0agiP4V2PM2Wsmd9876nw9v6NyiRSvrM3VrSVq32Dk3C5dgIjSwrW3btD0BDyDytvDoFQbhqnZmJUpKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کاخ سفید، : مامویت سادست؛ صلح از طریق قدرت
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12637" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12636">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با یاشار : پروژه قهرمان سازی زرشکیان رو متوقف کنید !!!
😡
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/12636" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12635">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گروه تروریستی سپاه پاسداران:
احتمال وقوع جنگ کم است، اما نیروهای ما آماده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/12635" target="_blank">📅 11:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12634">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/12634" target="_blank">📅 11:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗠𝗶𝗻𝗮</strong></div>
<div class="tg-text">یاشار برای ماهایی که تازه وصل شدیم اکانت اینستا تو میدی</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/12633" target="_blank">📅 11:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">در حال برسی اینم که امروز‌ خودمو نشون بدم و با یه ویدیو بیام به یوتیوب !
⏳
https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/12632" target="_blank">📅 11:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسرائیل هیوم: پالس‌هایی از احتمال حمله آمریکا به گوش میرسد
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/12631" target="_blank">📅 11:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جلسه کمپ دیوید که قرار بود امروز برگزار شود ترامپ اعلام کرد: جلسه کابینه به دلیل شرایط آب و هوایی در کاخ سفید برگزار خواهد شد، نه در کمپ دیوید!
حالا صحبت‌هایی هست که کمپ دیوید یک تله برای شناسایی فردی بود که اطلاعات را نشت می‌داد ! فرد مورد نظر گیر افتاد !
یاشار : دقیقا مشخص نیست چه کسی بوده است. صحبت ها درمورد تولسی گابارد و ونس هست ، ونس و تولسی از نظر فکری به هم نزدیک دیده می‌شوند؛ هر دو در جناحی قرار می‌گیرند که نسبت به جنگ مستقیم با ایران محتاط‌ترند.
بعد از استعفای جنجالی تولسی، چند روز پیش موجی از تحلیل‌ها راه افتاد که می‌گفت «ونس در حال منزوی شدن در دولت است».
اگه ونس باشه اوضاع خیلی پیچیده میشه
از اونجایی که تنها عضو کابینه هست که رئیس جمهور قدرت عزلش رو نداره و با رأی بالا اومده
تحلیلگران معتقدند درون دولت ترامپ اکنون دو بلوک شکل گرفته:
بلوک hawkish (تندتر علیه ایران)
بلوک restraint/non-intervention (محتاط‌تر)
و چون ونس چهره مهم جناح دوم محسوب می‌شود، هر اتفاق امنیتی فوراً او را وارد شایعات می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/12630" target="_blank">📅 11:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">روزنامه «فایننشال تایمز» گزارش داد صندوق مالی شورای صلح در غزه از زمان تاسیس خود تاکنون هیچ بودجه‌ای دریافت نکرده است.
@withyashar
این همون شورایی است که ترامپ تمام سران رو جمع کرد که پول بزارن</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/12629" target="_blank">📅 10:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجلس سوئد ازدواج فامیلی رو ممنوع کرد؛
طبق این مصوبه، از اول ژوئیه 2026 دیگه ازدواج بین بچه‌های "عمو، دایی، عمه و خاله" تو سوئد ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12628" target="_blank">📅 10:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a45d6ab.mp4?token=W1lLACxwBizc_p56diXK94W5acS313IXIUltM48cE6b_r6OIkTI2gZa8HAX2IRDLXtSXcJAoBRdHmcGetChZMtFcvLPYdpySGwhb7iV_0OppvtMgCI-jf_yhwZ6JFbnhTIYTXf6g6QPnRYJteOC3jiDZPTUAAuswhgkuGwecEi1BWw19RwDeh9E6r1RvT0GuV1W71XFDvvXldsnA37YKO0RCmMYr06q0PItmLECzlL58MY3ScMPSHULoBANp8Ofey5GHjQj_fVGHUCV362h0HTUIBIFJmqFbMS8nv6QqQcUqJCU2KP_j4RdMcuEWmOhmPRLKBiGOM5p6lk6PXxA8EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a45d6ab.mp4?token=W1lLACxwBizc_p56diXK94W5acS313IXIUltM48cE6b_r6OIkTI2gZa8HAX2IRDLXtSXcJAoBRdHmcGetChZMtFcvLPYdpySGwhb7iV_0OppvtMgCI-jf_yhwZ6JFbnhTIYTXf6g6QPnRYJteOC3jiDZPTUAAuswhgkuGwecEi1BWw19RwDeh9E6r1RvT0GuV1W71XFDvvXldsnA37YKO0RCmMYr06q0PItmLECzlL58MY3ScMPSHULoBANp8Ofey5GHjQj_fVGHUCV362h0HTUIBIFJmqFbMS8nv6QqQcUqJCU2KP_j4RdMcuEWmOhmPRLKBiGOM5p6lk6PXxA8EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان:ان‌شاءالله این ظالم به نام نتانیاهو، درسی که شایسته‌اش است را از مسلمانان جهان خواهد گرفت
@withyashar
یاشار : به قول تحلیلگر ترک، ترکیه هیچوقت مثل ایران نمیشه، بلکه بدتر از ایران میشه.</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/12627" target="_blank">📅 10:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارسالی : اینکه شب عید قربان نت وصل کردن، حس گوسفندی رو دارم که قبل ذبح بهش آب میدن.
😂
🤣
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/12626" target="_blank">📅 10:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زنگنه، نماینده مجلس
:
آمریکا حق غنی‌سازی، حاکمیت ایران بر تنگه هرمز و رفع تحریم‌ها را پذیرفت
@withyashar
🤣</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/12625" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گویا موشلی رو جمعه در تهران و شنبه در مشهد تشیع میکنند
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/12624" target="_blank">📅 03:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/12623" target="_blank">📅 03:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12622">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/12622" target="_blank">📅 02:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12621">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/12621" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12620">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/12620" target="_blank">📅 02:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12619">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/12619" target="_blank">📅 01:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12618">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/12618" target="_blank">📅 01:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/12617" target="_blank">📅 01:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/12616" target="_blank">📅 01:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/12615" target="_blank">📅 01:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/12614" target="_blank">📅 01:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12613" target="_blank">📅 01:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : شله داوود @withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/12612" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl0MsYV127XLmO4oZrRE7RX3GXsUqGT-CdwgrTMooRQjBwaQiwvansU_stPpr-FuVA65MycdnFEiv_QSDBmaalifKe2qcVCkG7lgeD6NhJbR-5Ct3nyisRMdihibTf9eKMA5MvsTOK0OyLbxj9JOH9CVSIqxSxjQpU8NBOgYVfQmLZ43EA4khrkL_LbtWpQWuyC3fvk1sQj31PLE22YR-qGHi1e_9x9DNcP0Wqc2Y0ReDtFu6gw2YNsQ_BAU6HcwkIfe-5A3tJwo_n7HO3dzPoDCK_qjQPJqYjapkkOAJzqgORdU53AZQ7WS4PqiUuGgNRZxXyKKWwBIcheRjSp1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تصویر جدیدی از مجتبی خامنه‌ای را منتشر کرد
@withyashar
خوب پس بدل تکمیل شده نتو وصل کردن ولی اصلا شبیهش نیست !
🤣</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/12611" target="_blank">📅 00:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6ZwLJq2WFK27QTOu3McC3sny9MTBo-fM3iYyn7QQUeIs8rcQ914GCqEvqsdJbldYnLunKS0MwEnl2bHqgBwaRNC2E5ultXIby_ec-M_twHxVLSBsjl5loHvw_lAayuKI7dGQyiOtitu4dM_UIhiVer54z1r56O4rkilKb2tN8ZVCBrW-sWXbpW1dXnVjESfn2QJEQE1pHyqxZ5n_FDHfeQGxXquxK5W-1djnFo0KxBzjWOBopqwnDzZoW8zfEvaNVGOyLHUo4txT8mcuRp7qR8iDkVZ9TxHp1m8csgHOhcjEQJGYaDPV-_W6QXpPVf54tgubGnX-D-GY64mN6EzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به شرایط نامساعد جوی احتمالی فردا، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم. از توجه شما به این موضوع سپاسگزاریم! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/12610" target="_blank">📅 00:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/12609" target="_blank">📅 00:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دفتر رسانه‌ای شاهزاده رضا پهلوی با انتشار بیانیه‌ای در واکنش به صدور حکم اعدام برای چهار شهروند ایرانی، نوشت: «صدور دوباره احکام اعدام برای چهار تن از بچه‌های اکباتان، میلاد آرمون، محمدمهدی حسینی، مهدی ایمانی و نوید نجاران، سند دیگری از ماهیت جنایتکار رژیم جمهوری اسلامی است که برای حفظ قدرت، جوانان ایران را به قتل می‌رساند و از خون مردم برای بقای خود تغذیه می‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/12608" target="_blank">📅 23:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو از ترور هدفمند خبر داد :  همین الان محمد عوده، از فرماندهان شاخه نظامی حماس و یکی از طراحان حمله ۷ اکتبر رو در غزه هدف قرار دادیم  به حساب همه‌شون می‌رسیم @withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/12607" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b685af254.mp4?token=tFTNaKql646ueAOjaKwyqWcQNiHDPU9l6YQbe-zp03MS_j_qkExaCiut6UTtI7j71RNqwWHzoD_DU14JGHBQFx9FT-UERYGcx-qBY1lsZN5_WjXXYOcIS8Oal4nOXChu0-a-0GuhBYo_IlDSl2Bnh05NAjUHaMHwut7kdRwdo6eqoe3P3niV2oMxZttR74SnmtsX5aerEQbamBGI6LC8PN7UdlY4CjTTdVta1woHTlsGbgwXn_DrWLcR0rgyKenY6ig_3Ph37swj2EaoJgWO27XE_weDOt-6HI4pMYfxxL8Sr60aFOjh1_bejtPx-EqyOwqrl-UCG7mC6zOWhdKYJq12H4ubJEDkQijZ1hPksUIqGF0jlXYTqPcAcGwducM0ZEZFK8gcDLQudTUQUQlnI2kMKavUvFWT5uhtlFHopcDmlcC0yuiMQsHDjJXpNBmX6Ilb-VSDBn_bwvRYunWhxROFhihqTBLSttagwzENyqWDxok1Y34VpOOmxPExHALn3qymvOQY7bFLn1GdZhIGLr43RaCFmMEK29eb8EdA8FzYmJJPHV4tzCjsN-zJewjT4nIWxAzCmnxKjCfYblMSMdXr6QlY3T3b8151fOf84tS_AD5_t0xbnrVNwvNV52p_yGeePSiZrjCMT1jLAjCSRc44Mn8HTj9-aUUjfkDZGYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b685af254.mp4?token=tFTNaKql646ueAOjaKwyqWcQNiHDPU9l6YQbe-zp03MS_j_qkExaCiut6UTtI7j71RNqwWHzoD_DU14JGHBQFx9FT-UERYGcx-qBY1lsZN5_WjXXYOcIS8Oal4nOXChu0-a-0GuhBYo_IlDSl2Bnh05NAjUHaMHwut7kdRwdo6eqoe3P3niV2oMxZttR74SnmtsX5aerEQbamBGI6LC8PN7UdlY4CjTTdVta1woHTlsGbgwXn_DrWLcR0rgyKenY6ig_3Ph37swj2EaoJgWO27XE_weDOt-6HI4pMYfxxL8Sr60aFOjh1_bejtPx-EqyOwqrl-UCG7mC6zOWhdKYJq12H4ubJEDkQijZ1hPksUIqGF0jlXYTqPcAcGwducM0ZEZFK8gcDLQudTUQUQlnI2kMKavUvFWT5uhtlFHopcDmlcC0yuiMQsHDjJXpNBmX6Ilb-VSDBn_bwvRYunWhxROFhihqTBLSttagwzENyqWDxok1Y34VpOOmxPExHALn3qymvOQY7bFLn1GdZhIGLr43RaCFmMEK29eb8EdA8FzYmJJPHV4tzCjsN-zJewjT4nIWxAzCmnxKjCfYblMSMdXr6QlY3T3b8151fOf84tS_AD5_t0xbnrVNwvNV52p_yGeePSiZrjCMT1jLAjCSRc44Mn8HTj9-aUUjfkDZGYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تری ینگست خبرنگار فاکس‌نیوز از اسرائیل گزارش میکند : رسانه‌های حکومتی ایران ادعا می‌کنند که برای هرگونه توافق با آمریکا، باید ۲۴ میلیارد دلار آزاد شود.
تیم ترامپ می‌گوید چنین چیزی قرار نیست اتفاق بیفتد و “هرگونه کاهش فشار مالی فقط در صورتی انجام می‌شود که ایران به تعهداتش عمل کند.”
ایران باید کاملاً از برنامه هسته‌ای دست بکشد و هیچ‌گونه کنترلی بر تنگه هرمز نداشته باشد، تمام.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/12606" target="_blank">📅 23:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا گرفته‌اند و هرکدام فریاد بزنند «من تسلیم می‌شوم، من…</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/12605" target="_blank">📅 23:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeefxX22Z95R-Mtkq4jRqX3T3OAqMXJVf4wPlWGQH4G4G_kkiD6JnxCa7z9W9qxFuqVY9ABDMKEWBPxuhFpAgjQHdnmoAVZ1MCObgLf1tF7XMOCyPnrg8Xji9sGBNWsKt0QqqixrlNk2Dx3H_lrr-rrDysnaOQN0-mQbXqjt8nN1xoztSNjhWcmToocpq2WMqYYcvZkYqJRPEOpQpwi_xlr_HJ6eeog57bdvKlKicHivpn7nDD4RgKHrfOexWYz_-erfGE8ktShl7V2rGF7i1qWjUkjrroct7_fP_CfHm-v8bRhWnN-sphheFJLt5K6hSBDt69JeYKdxGaTAxDXunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا گرفته‌اند و هرکدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» و همزمان دیوانه‌وار پرچم سفید را تکان دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت بزرگ و نیروی شگفت‌انگیز ایالات متحده آمریکا بپذیرند، در این صورت نیویورک تایمزِ شکست‌خورده، وال‌استریت ژورنال چین (!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و سایر اعضای رسانه‌های «اخبار جعلی»، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورده و اصلاً رقابت نزدیک هم نبوده است. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12604" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عزیمت ترامپ از کاخ سفید به بیمارستان @withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/12603" target="_blank">📅 22:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">منبعی آگاه به «اتاق جنگ با یاشار» گفت که در شروط توافق این مورد تأکیید شده که ترامپ باید ختنه کند.
🤣
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/12602" target="_blank">📅 22:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12601" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تسنیم : فروش نخی سیگار ممنوع شد  اتاق اصناف ایران: فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد. @withyashar
😐</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/12600" target="_blank">📅 22:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تسنیم : فروش نخی سیگار ممنوع شد
اتاق اصناف ایران:
فروش سیگار نخی و فرآورده‌های دخانی بازشده در تمامی واحدهای صنفی ممنوع شد.
@withyashar
😐</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12599" target="_blank">📅 22:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رادیو ارتش اسرائیل گزارش داد که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در حال حاضر در یک تماس تلفنی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/12598" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نت بلاکس : ۸۶٪ اینترنت ایران برگشته @withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/12597" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیروی دریایی ۳پا: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12596" target="_blank">📅 22:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو از ترور هدفمند خبر داد :
همین الان محمد عوده، از فرماندهان شاخه نظامی حماس و یکی از طراحان حمله ۷ اکتبر رو در غزه هدف قرار دادیم
به حساب همه‌شون می‌رسیم
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/12595" target="_blank">📅 21:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGnsv_juExKGTAHduK2I5emDmb6ITX-rUmi6kaGL-gX1nTWwWnJaJcuOH24XjSsDSNKC0Y30Tkj2jtV7IHDQXrhatbtSh8NAToT_uDP55DgSRD7Yq9aklIJJPkpeqFeQ4-zvhRQSg0j0Hm0FNUE-lqCnjzXKE8Qv3kodiZsZH3aHQFdcrtKb1DS4Tltq-Cq9A8VCek2Rz-YbpNnF_N5VcUSpzcTPSsSilxTkUKU4Lnxgw3lhjpHFoTE34TSCTeqebtNaN_sRU_FCnMdv5qVx5VJb5Q1J4pPxnwdQjL5k4bIIjjGv9xisKpNzmhr7VsNtu5hx4RkMvRjA9eoH1MBnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس : ۸۶٪ اینترنت ایران برگشته
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12594" target="_blank">📅 21:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک تایمز: ایران با چندین پهپاد انتحاری به چند ناو آمریکایی که از سمت دریای عمان، قصد ورود به تتگه هرمز را داشتند حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/12593" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/12592" target="_blank">📅 21:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از منابع:
حمله به ایران پس از دریافت «پیام مشخصی» از آمریکا، در این مرحله از دستور کار خارج شده.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/12591" target="_blank">📅 21:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3faocj7v4znazEXIDYGryb3vt1BV4G3X55Uld1e_2ZaefeKSZ-64hnB9If9FkqAbpsQY4qwDlOUWX1c9HdIVKa3YFjmcnGanDtspY2-Iqn7rrBZgQCyDSzI_WvCEsNdBy8W8Lp3eImqR5Z4gw2-cfDlFKS0guhMVAeCopZhGmQ3Br7ury_VwhJiyWvPZdugNS1VDOYGgC4sDdH-2j85E6Jg5DY5QWvDGuJVLYvwD78sc6aFWS2ynhec-gUJuzE1H4E188cAXdYKjEf7Z2Ja9KpqB3HjFtAYiPtcam7AaCDa0ukluyB5p2dyj-fHmPz82rWu0JLpe1lthPlJdn91Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : «بی بی، برو بزن بترکونشون!»
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12590" target="_blank">📅 21:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نت ها اوکی باشه لایو هم شروع میکنم که به امید خدا آخر هفته اگه زد زنده زارتان زورتان رو بگیرم
💥
🌶️
این ۵ روز‌آینده بسیار روز های مهمیه ! ببینیم تکیفمون روشن میشههههههههه</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/12589" target="_blank">📅 20:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12588" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/12587" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو، در بیانیه‌ای اعلام کرد که نیروهای زمینی اسرائیل در حال «گسترش و تعمیق» عملیات این رژیم در لبنان هستند و «در حال تصرف مناطق وسیعی هستند»
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/12586" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۲ عبری:
آمریکا به اسرائیل هشدار داد که به هیچ شکلی به بیروت حمله نکند.
@withyashar
😐</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12585" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qahqBiQboY8_JKBTrnZYyFCURTpUC_0nmrFqOSKVt-R4Np4zGCEbBxkfNXAlaGSTh6GWRiorqjiADDN6BfXAEjiCdh96Msgn-qM1YURDFyug7a4yF2IYb3TRI79AjHHkA_UunsKe60GviFGcFhxj63JZVvwKbghGgi0GnWcelRaRQ5URksV4UdnzNlI-zqsCLM-1IwCL30bn-exMM3VEgqfyB9IOkEdGJmNqiKZBTzdkTjCH7Cx1m63fOdZMnwrvfX14zraPD5pVia1-Ilf2iuMgkBTBZxlZElH0Ve-WQRKow9TIZmbF4SFH5wbN2vAb2tDsq3EmEQZAs8X9jvGdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همین الان معاینات پزشکی شش ماهه‌ام را در مرکز پزشکی نظامی والتر رید تمام کردم. همه چیز عالی بود. از پزشکان و کارکنان عالی متشکرم! به کاخ سفید برمی‌گردم. رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/12584" target="_blank">📅 20:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معاون وزیر ارتباطات: سيستم عامل، مرورگر، آنتی‌ویروس، اپلیکیشن‌های بانکی و ابزارهای امنیتی خود را بروزرسانی کنید
@withyashar
چه دلسوز شدن.
🤣</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/12583" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست کنین ایومجی و استوری اضافه بشه ۵۴۴ بوست لازم داریم
🥲</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/12582" target="_blank">📅 20:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سنتکام: پروژه آزادی از سر گرفته نشده و نیروهای آمریکایی در حال حاضر کشتی‌های تجاری رو از تنگه هرمز همراهی نمی‌کنند.
@withyashar
پروژه قایم موشک گویا شروع شده
😂</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/12581" target="_blank">📅 20:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/12580" target="_blank">📅 19:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf840f209.mp4?token=Z5jGJriF3doNghpB2_rxrsx8OQHvgzHdCk8jbfF7HNjfevHQN2F9UjcZnvVkAeQzYy6pBVVuN8XKYmib4gBuDnEHOdeV22NsU4AbygP8yDjGUQLsq3fCf1bn9e9UOyaPlL_ugSoDpodUs1dooFc7JcSFKRtwvHbaNwG5qyUC_RPMMX_untlM0k46FB6kTw45zuzA0iU3WPMDGq6qiI6JJdXvB0bmz-qVINt4bz4e3yXWoDg6VPYFSpnspQuXIDZOH8-0k2OLA10EcGL5Qmvwxtvtwn2veGtPwNseG7s24qK1Rj5jKR20ShkUlL0ZJbn3gy0sQyJ5vOgJ1OXG6v_THw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf840f209.mp4?token=Z5jGJriF3doNghpB2_rxrsx8OQHvgzHdCk8jbfF7HNjfevHQN2F9UjcZnvVkAeQzYy6pBVVuN8XKYmib4gBuDnEHOdeV22NsU4AbygP8yDjGUQLsq3fCf1bn9e9UOyaPlL_ugSoDpodUs1dooFc7JcSFKRtwvHbaNwG5qyUC_RPMMX_untlM0k46FB6kTw45zuzA0iU3WPMDGq6qiI6JJdXvB0bmz-qVINt4bz4e3yXWoDg6VPYFSpnspQuXIDZOH8-0k2OLA10EcGL5Qmvwxtvtwn2veGtPwNseG7s24qK1Rj5jKR20ShkUlL0ZJbn3gy0sQyJ5vOgJ1OXG6v_THw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیمت ترامپ از کاخ سفید به بیمارستان
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/12579" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1513fcd1a2.mp4?token=ZtkBVJKrKtPj6VoRBoMsrI6mRdYUlxdoWYovb7c-Z5O8wi4nFvXPXLKSWu1Wq1dC2pLY7YXnz_d-nsQp-VU_MpKGsHGSWVb5Cn70JgvWf5eMDuf5bDEPKzSoNOmIGNcCoLU78osMNv1mknbKJofb2WeMGV2tpBf-g5C-I2ZBUC7m63K4jqO0-EiE7bbMcK1NQjDMUVaMlCTQDlNVJcuY6NnANcZ-rrUROCG8dvcbFW6_DxthD1BDJeI59dnTvYD47ZmZZzcW8zvtdomoev6QmobYN8e6xYtv8CFMM_0Wvx6u5GLhPwLaht9Ee1nFM8JfFRamXWlwCSLiNeNmoa4QWlCyYPnGbpbkL5IUKpWJ8F-cGT-cfh06ysLbHRD0nw74IOq7Dy-Bxy7NjxBhI-uJ0-140dLMpjTo-QLLV2Z4yZp6eKS0q9kijnCPY-okq9rAvh6gxWs5H3vI_H_uOIQQfQS_CR2dgSVhlUYRekEgGdjSvbDC64jYC-g6NEsUPmpGVxxjJTeF23GIgofHeUURqcUUmpwYPJG14NfGI6kQg8XwaeNoxXrtUOBQZvI7OAJxVy0-oiszIQlr1wrd9D6r7YcQv8ucb-O0ITO4-5FlX1IM1dv34b-cnrW0bW00SJbhgFwCa7v60q2dOB-tY1-m0Hg9asWQkEfZIPiRVfjYK94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1513fcd1a2.mp4?token=ZtkBVJKrKtPj6VoRBoMsrI6mRdYUlxdoWYovb7c-Z5O8wi4nFvXPXLKSWu1Wq1dC2pLY7YXnz_d-nsQp-VU_MpKGsHGSWVb5Cn70JgvWf5eMDuf5bDEPKzSoNOmIGNcCoLU78osMNv1mknbKJofb2WeMGV2tpBf-g5C-I2ZBUC7m63K4jqO0-EiE7bbMcK1NQjDMUVaMlCTQDlNVJcuY6NnANcZ-rrUROCG8dvcbFW6_DxthD1BDJeI59dnTvYD47ZmZZzcW8zvtdomoev6QmobYN8e6xYtv8CFMM_0Wvx6u5GLhPwLaht9Ee1nFM8JfFRamXWlwCSLiNeNmoa4QWlCyYPnGbpbkL5IUKpWJ8F-cGT-cfh06ysLbHRD0nw74IOq7Dy-Bxy7NjxBhI-uJ0-140dLMpjTo-QLLV2Z4yZp6eKS0q9kijnCPY-okq9rAvh6gxWs5H3vI_H_uOIQQfQS_CR2dgSVhlUYRekEgGdjSvbDC64jYC-g6NEsUPmpGVxxjJTeF23GIgofHeUURqcUUmpwYPJG14NfGI6kQg8XwaeNoxXrtUOBQZvI7OAJxVy0-oiszIQlr1wrd9D6r7YcQv8ucb-O0ITO4-5FlX1IM1dv34b-cnrW0bW00SJbhgFwCa7v60q2dOB-tY1-m0Hg9asWQkEfZIPiRVfjYK94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : شله داوود
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/12578" target="_blank">📅 19:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع عبری: در ساعات اخیر نتانیاهو مشاوره‌ای امنیتی در مورد وضعیت در جبهه های لبنان و ایران با رئیس ستاد ارتش اسرائیل، وزیر دفاع و دیگر سران نظامی ارتش اسرائیل برگزار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/12577" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بچه ها تلگرامتون رو آپدیت کنید سریع تا نظر سنجی‌ها رو ببینید</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/12576" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فک کنم ترامپ با پروژه آزادی پلاس داره کامبک میزنه
😂
💥
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/12575" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک پست: ترامپ برای انجام سفری به کمپ دیوید است در حالی که تنش‌ها با ایران به دلیل حملات آمریکا افزایش یافته است  ترامپ چهارشنبه به طور نادر به کمپ دیوید سفر خواهد کرد تا جلسه کابینه‌ای برگزار کند، زیرا مذاکرات صلح با ایران به زمان حساس خود نزدیک می‌شود،…</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/12574" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/12573" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آمار لحظه‌ای اتصال اینترنت کشور:
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/12572" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که زیرساخت‌هایی به طول 11 کیلومتر را در در شمال غزه منهدم کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/12571" target="_blank">📅 18:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم ترامپ با پروژه آزادی پلاس داره کامبک میزنه
😂
💥
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12570" target="_blank">📅 18:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO ) از وقوع سانحه‌ای در فاصله ۶۰ مایلی دریایی شرق مسقط، پایتخت عمان خبر داده است.
به گزارش این سازمان، ناخدای یک نفتکش گزارش داده که یک انفجار خارجی در اطراف این کشتی رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12569" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادعای وال استریت ژورنال:
به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل عمان، توسط نیروی دریایی آمریکا هدایت شده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/12568" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خوش اومدین ولی‌ لطفا تک تک پیغام ندید که  وصل شدید
🙌🏾</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/12567" target="_blank">📅 18:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/12566" target="_blank">📅 17:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">یاشار گفتی میخوای یه کمپین راه بندازی همه باشن ؟
بیا نتو هم برات وصل کردن
صدات تا کجا میره مرد ... میخوام فکر کنم که پیامتو بالا شنیدن و بهت امیدوارن که نجاتشون بدی</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12565" target="_blank">📅 17:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر: اینکه گفتن قطر 12 میلیارد دلار از پول‌های بلوکه شده ایران رو قراره پرداخت کنه کاملا کذبه و از این خبرا نیست! @withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/12564" target="_blank">📅 17:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تلویزیون ایران:
رئیس مذاکره‌کنندگان ارشد ایرانی قالیباف مذاکرات خود را در دوحه به پایان رساند و به تهران بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/12563" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش اتاق جنگ داره بر‌میگرده
😈
💥</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/12562" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیویورک پست:
ترامپ برای انجام سفری به کمپ دیوید است در حالی که تنش‌ها با ایران به دلیل حملات آمریکا افزایش یافته است
ترامپ چهارشنبه به طور نادر به کمپ دیوید سفر خواهد کرد تا جلسه کابینه‌ای برگزار کند، زیرا مذاکرات صلح با ایران به زمان حساس خود نزدیک می‌شود، روزنامه پست مطلع شده است.
محل برگزاری جلسه ممکن است به دلیل هوای نامساعد تغییر کند.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/12561" target="_blank">📅 17:28 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
