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
<img src="https://cdn4.telesco.pe/file/OFE5oDEnUDY7AjKDgSgdiI62nAypcSxnUGYpltYJsH8f_4zpEte5PSMxJ42R1cS1sHLjaiT9mEb7_Q-SES6WtrOwkif63jmAmw7xpvcdZ4QO39r5S3GJtPo_qerBfbjaRnMu25o-AEolm56o2g69DwVy0uphkwQogBQfTEMrNbWbRsMdVCTF7mVessPMSjB1cl-BM7IfbW4F--3-KRQlTj7eZMp1Q9xR00nsZvd-zXL8jVbTg1YGuh-3M0gy9cgZsOLQfwx-uQRoyk9hdDHr7hkUsK0eDq9tJYC6LVxvNLG2hd4dRS8NszTqzrq89VMlSvH76l6M9zjjOBHOog1ufw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.97M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-653232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a20a0646.mp4?token=MkX6OrMxhdneoOA02YGM83yghwa8Ax02MstLsRznqhI5lvhRbxe4JAmvwhyej4s8JjTsgVHWs8WyDAS1YnS-gaQrcB6-hZipMXoFhk7GbDBlqo9nvKLC_IJoXxGmP-t1H7zuakd-MYg3HLLUvEXTDtEczS7coWwscf26mqnS2nxssLARHrqWFHZYLJEOI-pAXRkzLq0soMEKblHCHJ1ODYYLEOKiY2ox4uka37X7u3ofcumNDT1qwpsdFrseJpDnqmbFKebyhOiEs3o9AU3rTZNJezdsnvBQ7PflawHnpx5Hk2rCr9fmbFlDPF473ZcHRWLR4NIlZmTB_Dy7IGLo-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a20a0646.mp4?token=MkX6OrMxhdneoOA02YGM83yghwa8Ax02MstLsRznqhI5lvhRbxe4JAmvwhyej4s8JjTsgVHWs8WyDAS1YnS-gaQrcB6-hZipMXoFhk7GbDBlqo9nvKLC_IJoXxGmP-t1H7zuakd-MYg3HLLUvEXTDtEczS7coWwscf26mqnS2nxssLARHrqWFHZYLJEOI-pAXRkzLq0soMEKblHCHJ1ODYYLEOKiY2ox4uka37X7u3ofcumNDT1qwpsdFrseJpDnqmbFKebyhOiEs3o9AU3rTZNJezdsnvBQ7PflawHnpx5Hk2rCr9fmbFlDPF473ZcHRWLR4NIlZmTB_Dy7IGLo-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: عجله ندارم
🔹
رئیس‌جمهور آمریکا بعد از آنکه دست‌کم ۶ بار ضرب‌الاجل‌هایش درباره ایران را تغییر داده امروز چهارشنبه گفت که درباره ایران عجله ندارد.
🔹
او گفت: «عجله ندارم. همه می‌گویند می‌گویند انتخابات میان‌دوره‌ای؛ اما من عجله ندارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/akhbarefori/653232" target="_blank">📅 17:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای ترامپ: در جنگ ونزوئلا و ایران تنها ۱۳ نظامی از دست دادیم
🔹
رئیس‌جمهور آمریکا مدعی شد: «ما در جنگ‌های ونزوئلا و ایران تنها ۱۳ سرباز از دست دادیم در حالی‌که در جنگ‌های قبلی صدها هزار کشته داده بودیم.»
🔹
ادعای ترامپ در حالی مطرح شده که پایگاه اینترسپت در گزارشی افشاگرانه چند وقت پیش گزارش داد که ایالات متحده آمریکا در اقدامی عامدانه آمار تلفات و خسارات جنگ را پنهان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/akhbarefori/653231" target="_blank">📅 17:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
خیالبافی ترامپ درباره تصرف ونزوئلا و ایران
🔹
رئيس‌ٰجمهور آمریکا مدعی شد: «ما ونزوئلا را تصرف کردیم. می‌توانیم بگوییم ایران را هم تصرف کردیم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/653230" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMM_3HxzOCeaNJFcYuzHqgya3G8PZIsbtNe0FtnHw7BBzpGumC9NMNBfGRqpFTLO5U3CiZDQHkwDZ9Zz-oe3v7REa7V9T4QxsDb02maKIROwJWCant94UUJUr_ja4l9OdaRWn4Jp5fGP9LDdAhVyZe6Oa7PH7t5jQDs_IUOu_bnmqZxizOFK5BqjuKrpgf3RxnYkRlhqFkzQjFv_vw-HADtIR4-paFFUzVEl25awAfyOVEqifR6OMorPUAKRpNjF92qBDlu9HSLZdI4ro5fxvZ_QlBzTrk-RLTnyxKBT0EDuwJk1aMJlAUCp0IWRXBunXapBlpLbZh40A25saWlOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم را انجام خواهد داد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/akhbarefori/653229" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قالیباف: در شرایط جنگ اقتصادی روش‌های عادی کافی نیستند و وزارتخانه‌های اقتصادی باید با روش‌های خلاقانه دنبال حل مشکلات باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/akhbarefori/653228" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
قالیباف: مردم انتظار دارند همه مسئولان هم‌راستا با بعثت اعجازگونۀ مردم برای حل مشکلات معیشتی به صورت جهادی تلاش کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/akhbarefori/653227" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سومین فایل صوتی دکتر قالیباف خطاب به مردم ایران
🔹
تحرکات آشکار و پنهان دشمن نشان می دهد که به دنبال دور جدید جنگ است
🔹
مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند
🔹
دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد
🔹
از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
همان‌طور که آقای رئیس‌جمهور گفتند ملت ایران هرگز دربرابر زورگویی سر خم نمی‌کند
🔹
یکی از خطاهای محاسباتی دشمن این بود که اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود
🔹
کمیته نظارتی ویژه مجلس برای بررسی مسائل معیشتی و تامین کالاهای اساسی تشکیل می‌شود
🔹
متاسفانه برخی با انگیزه‌های سیاسی و به بهانه گرانی‌ها بدون در نظر گرفتن واقعیت‌ها، انگشت اتهام را فقط به سوی دولت یا رئیس جمهور می‌گیرند
🔹
برخی انتقادها از دولت بگونه‌ای است که گویی جنگی اتفاق نیفتاده است
🔹
من منکر برخی ضعف‌های مدیریتی نیستم اما آدرس غلط دادن، به وحدت ملی لطمه می‌زند
🔹
تأمین پایدار کالاهای اساسی باید اولویت اول همه مسئولان باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/akhbarefori/653226" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قالیباف: از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
دشمن تصور می‌کند اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود اما مردم ثابت کردند که هم‌چنان در میدان مبارزه با دشمن حضور دارند و انتظار دارند که مسئولان مشکلات را حل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/akhbarefori/653225" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
قالیباف: باید با تقویت آمادگی برای پاسخ موثر به حملات احتمالی و همچنین با افزایش تاب‌آوری اقتصادی، دشمن را از خطای محاسباتی بیرون بیاوریم و ناامیدش کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/akhbarefori/653224" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
قالیباف: دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/akhbarefori/653223" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قالیباف: مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/akhbarefori/653222" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قالیباف: تحرکات آشکار و پنهان دشمن نشان می دهد که به‌دنبال دور جدید جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/akhbarefori/653221" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf79aa6c71.mp4?token=jdUqhEblXMNteGe4n7Vms0sKpyVq5oZPOMv6-8ZPRNxnNYPSk138M0QgXs-8lRAKgOE1OpMeHtCrHRVhlZv2iOZ550UdGiaXF9tOYHQJeDLj-onYpfd1R4ky1T1DeY42GRc4ULUhJOUXB67oTdChQv3VGLwzcX4g9uPLQLif5Aol5S54eUuc2U1dvdntP0VnE3RGQd-Wv3JQVvPYQYmUbiw7pokhj_diega4GLJXo7HHtSyZnIiZkazqKcc99yCSd4NlhEv6eJi_xFn0MYo2nyOIgzEH-ARg_3jdH-IWdmEPg6XNZh47n9SEPR0rp4xXdby1yhjxi78fE8fKIImEDbeWhfnZ1MBwkSm1crWZAnZM1HSeXYpj_cm29IQKE-e4OxVrgttwEx0VzjDlb-ltJRcxuhywXm2XKcCuHf-0vn_eXbv2Waub24uxdXuU-nyAOzSTe20w6X1XuB_4mbPYj4P5T7AFQIYfgHvk4pSQu5ZXa1cqdmevGXXIWSodH_GLEw0n1ofzBAAepVFeiWl_C-IVnIriMYnvaIAJ-VGb1aowLaVNpHxAudYPtPIQ7Cnvwhol4gis1Ae5J4IfPwa4QBCVfWIU3kGNBfUzwaqsFC7WTITGQRVBCT1v_1UFwfTe8xzay6RBursnllmb2oShEveamJttGs4xO7oUsjFxTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf79aa6c71.mp4?token=jdUqhEblXMNteGe4n7Vms0sKpyVq5oZPOMv6-8ZPRNxnNYPSk138M0QgXs-8lRAKgOE1OpMeHtCrHRVhlZv2iOZ550UdGiaXF9tOYHQJeDLj-onYpfd1R4ky1T1DeY42GRc4ULUhJOUXB67oTdChQv3VGLwzcX4g9uPLQLif5Aol5S54eUuc2U1dvdntP0VnE3RGQd-Wv3JQVvPYQYmUbiw7pokhj_diega4GLJXo7HHtSyZnIiZkazqKcc99yCSd4NlhEv6eJi_xFn0MYo2nyOIgzEH-ARg_3jdH-IWdmEPg6XNZh47n9SEPR0rp4xXdby1yhjxi78fE8fKIImEDbeWhfnZ1MBwkSm1crWZAnZM1HSeXYpj_cm29IQKE-e4OxVrgttwEx0VzjDlb-ltJRcxuhywXm2XKcCuHf-0vn_eXbv2Waub24uxdXuU-nyAOzSTe20w6X1XuB_4mbPYj4P5T7AFQIYfgHvk4pSQu5ZXa1cqdmevGXXIWSodH_GLEw0n1ofzBAAepVFeiWl_C-IVnIriMYnvaIAJ-VGb1aowLaVNpHxAudYPtPIQ7Cnvwhol4gis1Ae5J4IfPwa4QBCVfWIU3kGNBfUzwaqsFC7WTITGQRVBCT1v_1UFwfTe8xzay6RBursnllmb2oShEveamJttGs4xO7oUsjFxTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هرجا لازم باشد می‌جنگیم و هرجا لازم باشد مذاکره می‌کنیم؛ ما کاملا در خدمت منافع نظام هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/akhbarefori/653220" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij2geZrIuRSv96fuGdFfugKIECv71nICG0lYRN_QWW2P85NMSJMdOJUstmkZJVUvSoVKXNZGMpsAubbYd27hzMFnq-737_E_1IOIFJr0Nr78mU7Ld3TRjH2fH-OQJpQyKTxgsDsxY5w9dvWoAoIH9nDq9mGADoB5l7OihooyWTIZtDPVwb3_-46Yq7balkpFzwp7KdjjHPEjO3TXdYGvw70crBa9WKoxo7Kg22EJkxJXi_LJb3jFX4RAieR9CMj17CqCmddttULe9xiWBxNI8uICJrXQUHRSJL-XxVEm4ZPRtLcEcBfQ6znj_Yf0Enk-IWscyy-ecVka0Zsdvzgh6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
🔹
رئیس مجلس در حساب کاربری خود در شبکهٔ ایکس، عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون اول رئیس جمهوری آمریکا نقل کرد:
🔹
«ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔹
و در ادامه نوشت:
🔹
این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره در حال تکرار شدن است. این بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/653219" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffbb74799.mp4?token=fp3aDzpcIa0ipxCjih-3-QJuRXHWOpfFIsEhIwWPSvEa-vKFd-uqJu9hXlO4Fbu6DOg-HVXADg-Q4GlviLK5fsIqFfwgN6Gqd8cKjFeNyqwI1FM9_WcIL076RYqzxue_EtgeH7hnm_PdSt6_-MGXjs43qhrCVChDGblwErfL86-e7eJkkax8y8txQ8ESs2HU1LFvyhvSHzakX9nfysjAeDKD3DvhJXvBDWDxsQpSYItV_xf-d8nkrBL4dNe47ObU7ogPGjR9CnAC3j54IBb19qeE5pKTAoYlAa6fk3hGMn5vCJLk-86sBMMTeZ6PWV8JEy4SuGqkh754NZ1v2sK_1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffbb74799.mp4?token=fp3aDzpcIa0ipxCjih-3-QJuRXHWOpfFIsEhIwWPSvEa-vKFd-uqJu9hXlO4Fbu6DOg-HVXADg-Q4GlviLK5fsIqFfwgN6Gqd8cKjFeNyqwI1FM9_WcIL076RYqzxue_EtgeH7hnm_PdSt6_-MGXjs43qhrCVChDGblwErfL86-e7eJkkax8y8txQ8ESs2HU1LFvyhvSHzakX9nfysjAeDKD3DvhJXvBDWDxsQpSYItV_xf-d8nkrBL4dNe47ObU7ogPGjR9CnAC3j54IBb19qeE5pKTAoYlAa6fk3hGMn5vCJLk-86sBMMTeZ6PWV8JEy4SuGqkh754NZ1v2sK_1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ضلع چهارم خیابان و مردم به ارکان دیپلماسی و میدان افزوده شد
🔹
وزیر امور خارجه: پیش از این، ارکان اثرگذاری در تحولات شامل سه ضلع «میدان، دیپلماسی و رسانه» بود؛ اما در نبردهای اخیر، ضلع چهارمی تحت عنوان «خیابان و حضور مردمی» به این مجموعه افزوده شد که برانگیختگی حاصل از آن، ارکان قبلی را تکمیل کرد.
🔹
نیروهای مسلح در جبهه دفاع، نهادهای دولتی در بخش معیشت، دستگاه‌های امنیتی به عنوان چشم نظام، و دستگاه دیپلماسی نیز مأموریت دارد تا صدای رسای کشور در خارج و مدافع منافع ملی در عرصه‌های بین‌المللی باشد.
🔹
دستگاه دیپلماسی با همان قوتی که نیروهای مسلح در میدان دفاع حاضر می‌شوند، در میدان گفتگو و مذاکره برای تأمین منافع کشور عمل خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/akhbarefori/653218" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f944b32f.mp4?token=VSe43xL2imxU2PJaXiJmB5IgmSzFuDRA6MSfpXK_EtPH07VBT-wXmb_XRIvvYBHD8GLXGKVTvQqihTDW9d1Nyij2n8_TDVyJGKDaFB6M09zV9ys0GYG6Lqhjc_Ol8g4ylFcw9_trsXM2vd_UHGY4WHV4IvS2mZ4J-t175Lmp4KIXPrZPLIfpM7OeithS7tnztgYDzLXLlY--Fu1jEQfCOH0BENthfi295mDKqm8-tsiaoqSZF0uryxm1k4-N_Ql2hATIR0tpfZ_WYHl4bCMPpSQxlA9_ysSU2hZ1Kobs1W2RRDgomY_kimGs8aZpmzTR4UZWi91lWTA6II6Rufm1wUwqj30oU0J1MH_EVhvWylkw4xJJJUoiSwkKroF9JtgAsT11hkYLzHN2TtJ8jYFGfWAMVJG66zat32nbX6tHREDB5CFSubpgxNKyI6z0C2y7HbZmi1WaMT6C5uVvLrWncT371YTJa-l_HFSOmpWsOFvedzSpP1p1ipC5tSBX3W5aGtZ3xlF6udL_F5pzxU-OBSH6mDOSahyYlFcwLrDwN_23Qu-62Nla2rkODWOfCBhx-m3OsLL0UcXjRyonqVkWrD66cEheot19hoqo1wp5YnfxNTVUVRiUBvaPWWfumdsA-EvIJP6G9V0HC3yUx9X58rdYUPRgSqEy3cbwZQylFgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f944b32f.mp4?token=VSe43xL2imxU2PJaXiJmB5IgmSzFuDRA6MSfpXK_EtPH07VBT-wXmb_XRIvvYBHD8GLXGKVTvQqihTDW9d1Nyij2n8_TDVyJGKDaFB6M09zV9ys0GYG6Lqhjc_Ol8g4ylFcw9_trsXM2vd_UHGY4WHV4IvS2mZ4J-t175Lmp4KIXPrZPLIfpM7OeithS7tnztgYDzLXLlY--Fu1jEQfCOH0BENthfi295mDKqm8-tsiaoqSZF0uryxm1k4-N_Ql2hATIR0tpfZ_WYHl4bCMPpSQxlA9_ysSU2hZ1Kobs1W2RRDgomY_kimGs8aZpmzTR4UZWi91lWTA6II6Rufm1wUwqj30oU0J1MH_EVhvWylkw4xJJJUoiSwkKroF9JtgAsT11hkYLzHN2TtJ8jYFGfWAMVJG66zat32nbX6tHREDB5CFSubpgxNKyI6z0C2y7HbZmi1WaMT6C5uVvLrWncT371YTJa-l_HFSOmpWsOFvedzSpP1p1ipC5tSBX3W5aGtZ3xlF6udL_F5pzxU-OBSH6mDOSahyYlFcwLrDwN_23Qu-62Nla2rkODWOfCBhx-m3OsLL0UcXjRyonqVkWrD66cEheot19hoqo1wp5YnfxNTVUVRiUBvaPWWfumdsA-EvIJP6G9V0HC3yUx9X58rdYUPRgSqEy3cbwZQylFgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظریف در مراسم بزرگداشت وزرای خارجه شهید: ما نیاز به تضمین از سوی قول شکنان نداریم. مردم‌ و نیروهای مسلح‌ بزرگترین تضمین برای ما هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/akhbarefori/653217" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رسانه‌های عبری گزارش دادند، در عملیات زیرگیری با خودرو در ئزدیکی منطقه عیون الحرامیه در شمال رام الله، دست کم یک شهرک نشین صهیونیست زخمی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/akhbarefori/653216" target="_blank">📅 16:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW8-xeX_vZbiPuCHr4Nrad-BOPboNgmyxYA-vZsQTzt7fSlQ_7jToMHbHI7gzNga1Ye-C0SaoQB21jTAqMWnIFlhZyzcq4TbrQfmQZC9XzTgYvJEQZPTcX7GDmg1N4vQhhTA3w0BHMI5BU68ngl5ZZ77oNd0-ydDQRr96XHEk3xxCX8DdhMqAFUW2M2D-ItawEpzH81xSs4PMnISCG-HqV_5ejxsSqN0a2-FwtnbZhdcGnKP3qrGBm4gBS4q9q7Hq0bz4734YqsJMVVAhy5RF3vOts4GZ9nQ4iGztkINKrMI5P8CRZOxaFKl-OTC8oA-q-H39Kewqseh0cobIOnhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افت ۱۲ درصدی رضایت جمهوری‌خواهان از ترامپ
🔹
نظرسنجی رویترز/ایپسوس نشان می‌دهد ۲۱٪ از جمهوری‌خواهان از عملکرد ترامپ ناراضی‌اند؛ در حالی که این رقم در ابتدای ریاست‌جمهوری‌اش در ژانویه ۲۰۲۵ تنها ۵٪ بود.
🔹
همچنین میزان ارزیابی مثبت از عملکرد ترامپ به ۷۹٪ رسیده که نسبت به ۸۲٪ اوایل این ماه و ۹۱٪ ابتدای دوره او کاهش داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/653215" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر واحد دنبال می‌کنند.
🔹
نیروهای مسلح همواره قهرمانان ما هستند. در مسیر تحقق آرمان‌های کشور برخی جان خود را فدا می‌کنند و برخی دیگر از نام و آبروی خویش می‌گذرند.
🔹
ارتباط و هماهنگی مستمر و روزانه میان وزارت خارجه و فرماندهان نیروهای مسلح در سطوح مختلف جریان دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/akhbarefori/653214" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۵ درصد از غذای کشور در داخل تامین می شود
مجید آنجفی، معاون امور زراعت وزارت جهاد کشاورزی در
#گفتگو
با خبرفوری:
🔹
بخش عمده ای از کود اوره مورد نیاز دنیا در کشورهای حاشیه خلیج فارس تولید می شود و می تواند چالشی برای امنیت غذایی دنیا باشد.
🔹
فکر می کنم بالغ بر ۸ میلیون تن  کود اوره در ایران تامین می شده است و از این مقدار حدود ۲ و نیم تا ۳ میلیون تن مصرف داخلی، و مابقی صادراتی بوده است.
🔹
ما متکی به تولید داخلی هستیم و اوره به اندازه کافی تامین می شود و کشور چالشی را نخواهد داشت.
🔹
حدود ۸۵ درصد از غذای کشور در داخل تامین می شود و بنابراین ضریب امنیت غذایی کشور ما ۸۵ درصد است و باقی مانده هم از مبادی ای تامین می شود که برای تامین آن مشکلی نخواهیم داشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/akhbarefori/653212" target="_blank">📅 16:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9NJFO3OYC9t8uZZ5w_AscvSEVn7zAUCC3bo-iq9isEkvaRScMLXa71EKYZkNglPdWy4hgsTr2HPUOzkxlvMv7KIVaXAClGC-XMEREHuzFPYwfkrcyEuEBr25JibHGGp2XnzgQBNLrAks9MmiyMUy9doybJ4YeIGDH1jp-VpkssmQ_siNxBuKOTLMxmXfxsxuEk6c6CHdMxXCzSR40TIqahWnH3NZj1Zboj4aRhqm12Q2sqOrTvk7rYrcCixAFzqZtuot8qr0fioMrw4EUUNzoM5dpYatGEhnHihKpm9sktlq0Z7DsjTy6-gs1IfK_J2EeK2v6FPxG4miGwFZqbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استعفای مقام ارشد اطلاعاتی دولت ترامپ به‌دلیل مخالفت با جنگ ایران
🔹
عروس رابرت اف. کندی جونیور، وزیر بهداشت و خدمات انسانی آمریکا، از سمت‌های خود در دولت ترامپ کناره‌گیری می‌کند.
🔹
گزارش داد «آماریلیس فاکس کندی، یکی از مقامات ارشد اطلاعاتی دولت ترامپ و متحد تولسی گابارد، مدیر اطلاعات ملی، این هفته از دو سمت کلیدی دولتی کناره‌گیری می‌کند».
🔹
طبق گزارش، خروج آماریلیس فاکس کندی هم انگیزه مشابهی دارد و به گفته یک منبع، «دستکم تا حدی به دلیل مخالفت او با اقدام نظامی ترامپ در ایران بوده است».
🔹
در این گزارش آمده که در ایمیلی به تاریخ هشتم این ماه (مه) که به رویت رسید، کندی به همکارانش گفته که قصد دارد به بخش خصوصی بازگردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/akhbarefori/653211" target="_blank">📅 16:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcGzPTK4TTi1xmKwSyRNhEPV5Osi7iNM7h8se7G_dGjZ4qGiYQJ3aKW3v-tvQ40PfNnajccC11llLW3PkiPRqWqrNfpJUrP3pH6QDJRIO2rTwvEl6KAOo8P62c7TG96IckuoX8el2Xr4rvqQm4Lisnr5tzAduo4ZH4j4bvcgM3GnrQb7A8MfH4MsCz4KRMm9lF5Y8TNYjl70ulZLMIIGQxZdsVwOgsYlgcnP67lgA2ntYbnyPDgNPacfAkmpsy3Ch_ofZ6Q5_2HgJCtEFEA7tT3UOlxm-TAB6h14LJJT9YLjvuA6kSZXEvvKkgEqXP80diPepp3ezrlN-dtLLBT03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه غربی: مواضع ایران تا حد زیادی، بدون تغییر مانده است
🔹
وال‌استریت ژورنال در پی ارسال آخرین پیشنهاد اصلاح‌شدهٔ ایران به طرف آمریکایی در روز یکشنبه، تأکید کرده است که تهران همچنان بر بسیاری از مواضع پیشین خود پافشاری می‌کند.
🔹
به گفته این روزنامه، ایران همچنان خواستار پایان درگیری‌ها، لغو تحریم‌ها، دریافت غرامت برای خسارات جنگی و نقش نظارتی بر تنگهٔ هرمز است.
🔹
این روزنامه همچنین افزوده که ایران در برابر خواسته‌های آمریکا برای تعطیلی یا تعلیق طولانی‌مدت برنامهٔ هسته‌ای خود مقاومت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/akhbarefori/653210" target="_blank">📅 15:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1236795a.mp4?token=i4RHSBmmCdDJpGqqL5_CEW0RyB3PUATrj5T_FA5nRL7bO9EXPNaDrPXQHqXmQKOMnpfqG6R4YZeFKqA3Iamkz2hJXQQ_wHSe3mNDptmh9wM1ijxxiy16Qp3l_nZ2wuD49Nk1fvwUrLoLl0OGcvXAi5vcki4IWkp4VEdD7A-hXqmkzQ-pBoKlqno7NyuO4l49fR2rneSBPZip9NBGLGBK_05xuv9hIvX77zmIJm1CwZBO-SV5uHvDb2Qznco5PURFcb1A5DVNkxnEbg7p2CBUZ7X8VMHvmZGl1xQlZK54uXYBs8v5VbyFwpqEntFxIee31mUetORMH0f0t2LhiumXHk5-mqGCA1xAhi3qYJgoTa648Fkns9Ixwt_W_evgzoTiof2YRFvvEJ4EVCiLbOuTJ3ONPYwc5o7CFwAWzLBKar-YbDT8pfGKbxTrEiO9JambM6zyY5ju4W02X1VZlaaGjUE6Jz8rEP_On5N4OmkHpHg_qKNzcacOmKDN8_fFJMdAy-v57_SfajSHVixZD5GJC2EMQSuj8p2H5SmvmbUawK34CrKVkc6l7vH2dvJZxgm4wTzlP02feAGO0IGXChrfd3mplDmwR5rT42UTWKJ2BMJJfUvmxO2oNpE-YJVfZCUTHsNvqGQWK9ITqVtk2CIJSJbaeb77r6FSs4cLwmK3YfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1236795a.mp4?token=i4RHSBmmCdDJpGqqL5_CEW0RyB3PUATrj5T_FA5nRL7bO9EXPNaDrPXQHqXmQKOMnpfqG6R4YZeFKqA3Iamkz2hJXQQ_wHSe3mNDptmh9wM1ijxxiy16Qp3l_nZ2wuD49Nk1fvwUrLoLl0OGcvXAi5vcki4IWkp4VEdD7A-hXqmkzQ-pBoKlqno7NyuO4l49fR2rneSBPZip9NBGLGBK_05xuv9hIvX77zmIJm1CwZBO-SV5uHvDb2Qznco5PURFcb1A5DVNkxnEbg7p2CBUZ7X8VMHvmZGl1xQlZK54uXYBs8v5VbyFwpqEntFxIee31mUetORMH0f0t2LhiumXHk5-mqGCA1xAhi3qYJgoTa648Fkns9Ixwt_W_evgzoTiof2YRFvvEJ4EVCiLbOuTJ3ONPYwc5o7CFwAWzLBKar-YbDT8pfGKbxTrEiO9JambM6zyY5ju4W02X1VZlaaGjUE6Jz8rEP_On5N4OmkHpHg_qKNzcacOmKDN8_fFJMdAy-v57_SfajSHVixZD5GJC2EMQSuj8p2H5SmvmbUawK34CrKVkc6l7vH2dvJZxgm4wTzlP02feAGO0IGXChrfd3mplDmwR5rT42UTWKJ2BMJJfUvmxO2oNpE-YJVfZCUTHsNvqGQWK9ITqVtk2CIJSJbaeb77r6FSs4cLwmK3YfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تامین کالاهای اساسی و صرفه‌جویی دو موضوع مهم نشست استانداران سراسر کشور با حضور رئیس جمهور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/akhbarefori/653209" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ضرب الاجل ۱۰ روزه دستگاه قضائی به شرکت های بیمه
🔹
رئیس کل دادگستری آذربایجان غربی: طی دستوری به شرکت های بیمه ضرب الاجلی ۱۰ روزه برای پرداخت مطالبات آزمایشگاهها، کلینیک های درمانی و مجموعه های مرتبط با بهداشت، درمان و سلامت تعیین شده است.
🔹
بهداشت و سلامت مردم جزء مهمترین شقوق حقوق عامه است که به جهت عدم همکاری موثر و پرداخت مطالبات مجموعه های درمانی با اخلال مواجه شده است.
🔹
به بیمه تاکید شده است، نسبت به پرداخت بدهی های معوق خود در سریعترین زمان ممکن اقدام کنند.
🔹
بیمه ها ابتدا به صورت نقدی حق بیمه را دریافت کرده اند ولی در پرداخت مطالبات مجموعه های بهداشتی، درمانی حدود یکسال تاخیر نموده اند و این امر به هیچ وجه پذیرفته نیست چرا که موجب اختلال در روند درمان مردم شده است.
🔹
در صورت عدم پرداخت طی ۱۰ روز، اقدامات قاطع و فوری قضایی از جمله برداشت از حساب و تعقیب مدیران خاطی از جهت ترک فعل در دستور کار خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/akhbarefori/653208" target="_blank">📅 15:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c381e0e43.mp4?token=e-CZM7_s8HXpzg7dGLvL1RSevt2MLk7rqveKo_eMOOro5EkKWBahGyhXnc5dfz5K6fsBkBC79FgYKVti9veSNL6nEqwTsZjzQbHfz6JzBnWBSBcxbRvhJ_AK1lEg-4F2SgEgZfWBkHXQ0DMQsG9L_72EWxJAKQAAKfXundaZ0pT7gV4lDIp5t0DZzq13W3HRQiecyuYLEOEkp27pXFA7Zoni0bJrzkly80aFINtGNklV5dDd648UTDOXHN658T7U-4OcN9fpcP72bbVGdAmDxz8UyIwmdmW-SMZtDByD16qADMzsy37JeADhlZh0L1XebwJghq0PvH0EyQaK_YSKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c381e0e43.mp4?token=e-CZM7_s8HXpzg7dGLvL1RSevt2MLk7rqveKo_eMOOro5EkKWBahGyhXnc5dfz5K6fsBkBC79FgYKVti9veSNL6nEqwTsZjzQbHfz6JzBnWBSBcxbRvhJ_AK1lEg-4F2SgEgZfWBkHXQ0DMQsG9L_72EWxJAKQAAKfXundaZ0pT7gV4lDIp5t0DZzq13W3HRQiecyuYLEOEkp27pXFA7Zoni0bJrzkly80aFINtGNklV5dDd648UTDOXHN658T7U-4OcN9fpcP72bbVGdAmDxz8UyIwmdmW-SMZtDByD16qADMzsy37JeADhlZh0L1XebwJghq0PvH0EyQaK_YSKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستیار ویژۀ وزیر کشور: اگر مجدداً جنگی شروع شود، در کوتاه‌ترین زمان ممکن محاصرۀ دریایی شکسته خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/akhbarefori/653207" target="_blank">📅 15:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0722b179b7.mp4?token=iXZYBEGa_9f2gb9jhQjbPQ6jj2yIVwHsGI-yWaJS93t8xd9YMi3F3xgHaOU3JNOPngBbatmxvOsgRlNFPUrb4zkueY10AFzXnIqa5waCgFfPnHaZAmWgFDrfwHwdSMKIRPWSIsm3pJkjREaLAT-4hi2PfXFm386yZCg1EgEiKyILAwxQq6tGjWQfyF67x07TTsx2KQLCYBeVX6Ay3ts9LGPOt6ksdYaYOk7w8Irp9c09yBrYlqif_5doscAq--u3avSxTHGlOqP6XOsn4afM7W3oC5T68XsQkQ_yqQk62jjM5odMy9HvSfbXHJIWfyCjYn2GBEUXylznC7A8evcAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0722b179b7.mp4?token=iXZYBEGa_9f2gb9jhQjbPQ6jj2yIVwHsGI-yWaJS93t8xd9YMi3F3xgHaOU3JNOPngBbatmxvOsgRlNFPUrb4zkueY10AFzXnIqa5waCgFfPnHaZAmWgFDrfwHwdSMKIRPWSIsm3pJkjREaLAT-4hi2PfXFm386yZCg1EgEiKyILAwxQq6tGjWQfyF67x07TTsx2KQLCYBeVX6Ay3ts9LGPOt6ksdYaYOk7w8Irp9c09yBrYlqif_5doscAq--u3avSxTHGlOqP6XOsn4afM7W3oC5T68XsQkQ_yqQk62jjM5odMy9HvSfbXHJIWfyCjYn2GBEUXylznC7A8evcAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرب‌الاجل‌های اجرا نشده ترامپ درباره ایران
🔹
روز دوشنبه، یک روز پس از تهدید به از سرگیری بمباران اهداف ایرانی، ترامپ دوباره گفت که چندین متحد خاورمیانه‌ای معتقدند آمریکا «به توافق با ایران بسیار نزدیک شده است». من این کار را برای مدتی به تعویق انداخته‌ام.
🔹
این ویدئو تهدیدها و مهلت‌هایی که ترامپ برای ایرانی‌ها تعیین کرده را نشان می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/akhbarefori/653206" target="_blank">📅 15:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30fd02dbcf.mp4?token=TFbM7wT-PN6m24XQAilBHHqpW8RLs0Mdkg3hXFxIwkL7u0VidPu6EbV9ZBN8ppawL4ZVS8Pwu6cV3jiXjaU1ZqJqVFIqb5p2SV9SD5eULKOS9QRUck-9CK7JnqsRPk6hkKVCegxqX0fZJ_-UOSrDFPCRrsqMDcV3t61llWdgW_31OlfA5QYkugBgdkBtQxGs3g4KSKxgeL3FLCuVDJsvAws8B7ZLmYJWQ1g5PA7bOeBwc-RvGawP1XdKDQfBYB-GAzkgoCVKPbfJ04Buw1jP3UhSen4ace639VhJ1c__Mp2jVstXhY3taEOuZEWIkhEr-RBYwHGcAa3yB9CNdC5gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30fd02dbcf.mp4?token=TFbM7wT-PN6m24XQAilBHHqpW8RLs0Mdkg3hXFxIwkL7u0VidPu6EbV9ZBN8ppawL4ZVS8Pwu6cV3jiXjaU1ZqJqVFIqb5p2SV9SD5eULKOS9QRUck-9CK7JnqsRPk6hkKVCegxqX0fZJ_-UOSrDFPCRrsqMDcV3t61llWdgW_31OlfA5QYkugBgdkBtQxGs3g4KSKxgeL3FLCuVDJsvAws8B7ZLmYJWQ1g5PA7bOeBwc-RvGawP1XdKDQfBYB-GAzkgoCVKPbfJ04Buw1jP3UhSen4ace639VhJ1c__Mp2jVstXhY3taEOuZEWIkhEr-RBYwHGcAa3yB9CNdC5gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر شرم‌آور از آزار و اذیت اعضای کاروان صمود به‌دست بن‌گویر و نظامیان اشغالگر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/akhbarefori/653204" target="_blank">📅 15:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNmaOvBtROdXB-Y5t44-Cp3KCGNEuKWfLd4H3UPwUGl1g-aRzjGzAYQ25fnXiyAtuyaEhnEIpQp5uhsJiJ2TjWJlgkqKtw_zxGb17wiUbYmPib_fmz4kTJSy2oU72XCqyRerzSCcTiY5k7gs7zQNl_V7Tm6uG6wnLWGswIDN9Rp67kTNO-7kfgIhZl5Kppv2zpiDyzs0kwBle9ivJi8Zzmzgkb4XX-u-zO0W8etWOnhmDjuhu-_QF4-3x8FPp2JQsRmk4GLi-Bbr5X2emWV2czAI4bhL2UMUjkK8NxrGVzpYAhFDnoEEOaF5BnEVCToG8zbuDBiu7psIroCjWOiKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ایران خط
قرمز خود را جا‌به‌جا کرده است
نیویورک‌تایمز:
🔹
بزرگ‌ترین غافلگیری دکترین جدید ایران، خروج از انحصار تنگه هرمز و تسری دادن بحران به دریای سرخ و «تنگه باب‌المندب» است.
🔹
بستن هم‌زمان یا مختل کردن ناوبری در این دو شریان حیاتی انرژی و تجارت جهان، عملاً مسیرهای جایگزین امدادرسانی غرب را مسدود کرده و تیر خلاصی به زنجیره تأمین بین‌المللی شلیک می‌کند.
ایران خط قرمز خود را جابه‌جا کرده است.
🔹
هر کشوری که آسمان، خاک یا پایگاه‌های خود را در اختیار جنگنده‌ها و موشک‌های آمریکایی و اسرائیلی قرار دهد، به عنوان «طرف جنگ» تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/653203" target="_blank">📅 15:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33243e624.mp4?token=qLjagTMafMu61I5zAQIsjjy36_ItTRPBmmuDHmI1TiMEi2GXiet2oY5C3U1yxv7qj6eIQXgdRMft22QLZozFRyrieOmgCZB9dpj0pRtGOGhz91wu5YOjAe6kX24mX4Zp1376gxLWFXauCO2lzJcrb3pvGpcHIjbOfofJynE-kUZGJ3meDeknrEf-x-VvmK0nHaEAZrSVODli07ZzcUPWivCvPWa30Bx0diF6O210Ne534iYgvkWqQwKT9Xx1vWe1pR4eH1jNfrwQYO8t_FBJLlG7EQ3711FbsfTyMkmxsg8Tni3unaP89wH2K4RWJBVvlfePn8Y_gsu1-un3XcU72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33243e624.mp4?token=qLjagTMafMu61I5zAQIsjjy36_ItTRPBmmuDHmI1TiMEi2GXiet2oY5C3U1yxv7qj6eIQXgdRMft22QLZozFRyrieOmgCZB9dpj0pRtGOGhz91wu5YOjAe6kX24mX4Zp1376gxLWFXauCO2lzJcrb3pvGpcHIjbOfofJynE-kUZGJ3meDeknrEf-x-VvmK0nHaEAZrSVODli07ZzcUPWivCvPWa30Bx0diF6O210Ne534iYgvkWqQwKT9Xx1vWe1pR4eH1jNfrwQYO8t_FBJLlG7EQ3711FbsfTyMkmxsg8Tni3unaP89wH2K4RWJBVvlfePn8Y_gsu1-un3XcU72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنبیه نفتکش‌های متخلف در تنگه هرمز
🔹
نفتکش‌های متخلف و پنهان‌کار در دروازه تنگه هرمز شناسایی و تنبیه شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/akhbarefori/653202" target="_blank">📅 15:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شما اسم فرزند آینده‌تون که قراره به ایران جان تازه بده چی می‌ذارید؟
خیلی‌ها توی پویش «جان ایران» شرکت کردند از جوان‌هایی که ذوق فرزند دار شدن دارن تا پدر و مادرهایی که اسم بچه آینده شون رو انتخاب کردن.
شما هم می‌تونید نام فرزند عزیزتون که قراره به ایران جان بده رو به شماره ۳۰۰۰۱۴۱۳ پیامک کنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/akhbarefori/653201" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0_bfM5Zo61EHNle_zDqY2XcXOm_HoL4F3zNj_TILBCYZbxwT9m7HCLItRvCVmRt8Y3hLe8kLg8AhWHng5iVPVzpgleRsIG9eV3sJcSlhIhwi5ZM9xHpgMnB32AcfL1aQQi8Qu00llJqMRYKMaQpGE8KM-cTeM8FA9NB6Anz3-VCTs1OBu2HCM5oGAT529VuSwTdoRBlTwY18tdVNUu--RYKzFRiOUOVIpE2SoJhlE-Gpq3U9Hni4GcZyO9mAQQ70glM5GGZIrMNNOYZTZ5UeQyrISiqzPvVJdsjtMwWlKKCKdBPbxbrIOo4Xfyow5fKoa0JgP3mrBrKt5RVmKdCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت بنزین سوپر ایرانی به جایگاه‌ها
🔹
دولت به پالایشگاه‌های کشور دستور داد، تولید بنزین باکیفیت موسوم به بنزین سوپر را از سر بگیرند.
🔹
از سال ۹۸ کمبود تولید بنزین نسبت به مصرف سبب شده بود تا تولید بنزین سوپر متوقف شود.
🔹
بنزین سوپر نوعی بنزین با عدد اکتان بالاتر نسبت به بنزین معمولی است که برای کاهش پدیدهٔ ناک (احتراق زودرس) و بهبود عملکرد موتورهای با نسبت تراکم بالاتر استفاده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/akhbarefori/653200" target="_blank">📅 15:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iohyg6IBVPJlp0G3AKAMzDhlxjgvJ7BGL5hpjedOWKfEDCTOpPmT3gavbEPEyAz9VdJB6drCwjnubw9gYZID7WXiW8-G_9f3AF6kmtFAP9bZXG2Ds-XatPaldoNS98tlDy4FZD1EbrZB2M48QtKAqa6LArxhHi-iJoB_tl42TLr9NqhL04kDYccNEUFgpgSM3T9efOnoOzt3zcC_77cMr1AIZDKRlcP1cHwzkEeli_i4a_aisJNyyie3B5gEygJ89zSzoH0uxnB8w57HiUEUTUON6KPcYZOnI3ybXEI3TqETwPayuiDmUPB4ZeBlT19iMf9oHhxe79MGpiLC-pQfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران؛ پایتخت پول ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/653199" target="_blank">📅 15:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDIfxgrzI_csQfMOxPmPLmc2f3D_OUJIbOyUfyrICSg8TFzj0Hf6SEMjJ2VPIeCnFNeuZXtXOk_c39822l0gNiofc84PaTMXba2kq_b8iEFMsV7fNxCBXk3N_0U4hqdCsJNImEC577G91fiAdBmFxX4-qNasnG1RTqr9RPZTZc-Y3rlz0_1_sRGMta7J7d3UgwpIS2xpoc8NGwOCHiQvCYb4xPl_WZ18zd1DvXi3LJSGcYwlAJhA538WYihkdNvNlNslNHio9Ng6r-l_wPYwUspIZJWMxs7OL6R6b7a2HhO38BsOqrRDsS9bSiiQPc_-rtVNPJ6iVMsyFjhyR1ikAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید گوگل برای تشخیص تصاویر و ویدیوهای هوش مصنوعی
🔹
گوگل به‌زودی قابلیت شناسایی تصاویر و ویدیوهای ساخته‌شده با هوش مصنوعی را به سرویس‌هایی مثل گوگل لنز، سرچ گوگل و مرورگر Chrome اضافه می‌کند.
🔹
قابلیتی که تشخیص محتوای AI را برای کاربران ساده‌تر از همیشه خواهد کرد.
این سیستم با استفاده از واترمارک نامرئی عمل می‌کند.
🔹
فناوری اختصاصی گوگل که روی تمام تصاویر و ویدیوهای تولیدشده توسط Gemini قرار می‌گیرد تا محتوای هوش مصنوعی به‌راحتی قابل شناسایی باشد. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/653198" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9fe0d300.mp4?token=BYn_F--gJ_69tY01j2RR77BCdX9XEcdF4_1kQvJmj9fU2AJu8k83_IOdfNJe_fxzYTDM87KrYBJkUcV8ZgpGVFALGQYeTtNqAsZAcS1EBOmI3iDgOjx9vD3S4BQWOzQE3ZbIR5kjP8N38jrG4udyvXobjuNh3tu9YEiUl0lzufy-RI1iopDOEA9BJzZonn6RB8xbPx6uokGB6cj-amQvygAOa21XI2lIjpfwPGEgiTa5qe37s6dgbfbrScb8xqeimzn0swmJnMtmWrj_aR5TbcBy5uL93koaivVdimPePX2RfhXT3nTAes89BkrjTUvT5iNb0FJoBYm7bEloCezgGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9fe0d300.mp4?token=BYn_F--gJ_69tY01j2RR77BCdX9XEcdF4_1kQvJmj9fU2AJu8k83_IOdfNJe_fxzYTDM87KrYBJkUcV8ZgpGVFALGQYeTtNqAsZAcS1EBOmI3iDgOjx9vD3S4BQWOzQE3ZbIR5kjP8N38jrG4udyvXobjuNh3tu9YEiUl0lzufy-RI1iopDOEA9BJzZonn6RB8xbPx6uokGB6cj-amQvygAOa21XI2lIjpfwPGEgiTa5qe37s6dgbfbrScb8xqeimzn0swmJnMtmWrj_aR5TbcBy5uL93koaivVdimPePX2RfhXT3nTAes89BkrjTUvT5iNb0FJoBYm7bEloCezgGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزار و اذیت فعالان ناوگان صمود توسط ایتمار بن گویر، وزیر امنیت داخلی صهیونیستی و نظامیان اشغالگر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/653197" target="_blank">📅 14:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX85jwDtqsSXvKjnwD1IoySvbIUTodDwHEy4fC4GPtgvwpYWObnLm2nd8qowQzsTOig9DXoEBH5WFU7c-TvWdr1s08-TFjwM7l3yinTZV64ySojIiI3pxjIFrvQ4RvuCToyxIRjgYcA-StKMAbX0QDXPJtSl_KifBGKUM4HUcW-hB6QmEb-NO1-OjokUOa1U0FRWoMejqoerbwzY_OPInjcK_S7bmew_14uIVYMRCTa9PG5hG5lJORko6gH9YaC72dAb-Ngkk6XFXBKN6BnIUHyJOE3uMqhLrZK11Wt-P8FtkHgNnTbjetUUjsGQGdsacrTk4jrYUIe_s7RS9woZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل اجرایی تسهیلات ۵۰۰ میلیون تومانی مسکن روستایی به بانک‌های عامل ابلاغ شد
🔹
تسهیلات بهسازی و نوسازی مسکن روستایی با نرخ سود ۵ درصد به متقاضیان پرداخت می‌شود.
🔹
بانک مرکزی: مابه‌التفاوت سود تسهیلات مسکن روستایی از محل صندوق ملی مسکن تأمین می‌شود.
🔹
تسهیلات مسکن روستایی با تضمین سفته زنجیره‌ای و در قالب قانون جهش تولید مسکن پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/653196" target="_blank">📅 14:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTMAGIJyON2PKnSUeECm6DOR3GZByl105XpUh9xggvagsVgFfHPdsmr52IvJ4j5k_T4d6WrPZ76ZAqlkK4KlURLe6Dn5Q-HlrxFA3uvMoKxuzCeIc7gUp8WxpzVShIpNrMekCwA3wbZpQT4_R3L-vtDeZxsfCKFH9fBG904CMgi60t8d7XT84hI8dEgKHXIjYFj4o-IIOkkrXjHoPzzDL8bHd18qJtxDvknyPsaEZL3Vculrek6_WB5FvztfNbCSmwK0EKGG5Q2dsqMnrSKG3OLfqcc721LCsSjygl_vcaj2hJ3P5-X8HQOTGhzqtD2bhQmh8KrGRmivDOYKmj_4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جان ایران» به شهر آمد؛
همزمان با هفته جمعیت، بیلبوردهای این پویش ملی با پیامی متفاوت رونمایی شد؛ روایتی از تولد، امید و آینده‌ای که با نفس هر کودک برای ایران ساخته می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/653195" target="_blank">📅 14:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پزشکیان: مردم باید بدانند که کشور در حوزه تأمین بنزین و برخی حامل‌های انرژی، با محدودیت‌هایی مواجه است
🔹
در شرایطی با فشار‌های خارجی و آسیب به بخشی از زیرساخت‌های انرژی روبه‌رو هستیم، استمرار مصرف غیر ضروری، اتلاف منابع ملی است.
🔹
دولت نمی‌تواند منابع را صرف واردات سوخت برای مصارف این چنینی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/akhbarefori/653194" target="_blank">📅 14:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
واریز یارانه نقدی به حساب سرپرستان دهک چهارم تا نهم
🔹
یارانه نقدی اردیبهشت ماه ۱۴۰۵ به حساب سرپرستان خانوارهای دهک های چهارم تا نهم واریز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/653193" target="_blank">📅 14:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3876f012bc.mp4?token=B2ZnYBXGZJalX2MBOJrO1oRL4VDJgWoaNnwWrzUuAqpf2vNrPYR22Xo8qhaCLUyiyCNFlHIkxpLRHRQI2xtVXmh8d6YJNigXIYGa1FXBKyebsOUuozfBhF1IOwMbgVy9Ux17-jQtnvu5L6cQoMEjOYGz9KdB8lXzlbNtaD21imk2qtuZk5dNDPEGwrdQEh80S8F6mT2U5EWrFkiVcQO9YgWc-AOauWEppdMgwkSukqxGLnSL8y2eRtKTVSIgptU7nrXIZ-loYlmiGp51xLdxEiIxf2NPzj0lxLEIAt8sIn6OjfdB90omaBywvLiPtdcMOkDblVES6e9woka4kFTfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3876f012bc.mp4?token=B2ZnYBXGZJalX2MBOJrO1oRL4VDJgWoaNnwWrzUuAqpf2vNrPYR22Xo8qhaCLUyiyCNFlHIkxpLRHRQI2xtVXmh8d6YJNigXIYGa1FXBKyebsOUuozfBhF1IOwMbgVy9Ux17-jQtnvu5L6cQoMEjOYGz9KdB8lXzlbNtaD21imk2qtuZk5dNDPEGwrdQEh80S8F6mT2U5EWrFkiVcQO9YgWc-AOauWEppdMgwkSukqxGLnSL8y2eRtKTVSIgptU7nrXIZ-loYlmiGp51xLdxEiIxf2NPzj0lxLEIAt8sIn6OjfdB90omaBywvLiPtdcMOkDblVES6e9woka4kFTfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسهیلات ازدواج و فرزندآوری افزایش جدی یافت و برنامه های حمایتی پس از این ادامه دارد
🔹
وحید دستجردی، دبیر ستاد ملی جمعیت : طرح یسنا و طرح حمایتی سوء تغذیه کودکان به قوت خود باقیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/653192" target="_blank">📅 14:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رشیدی کوچی: ۹۰ درصد مهمانان صداوسیما وابسته به یک جریان خاصند!
جلال رشیدی‌کوچی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
فعالین سیاسی، بین‌المللی و نمایندگان مجلسی که به صداوسیما دعوت می‌شوند، بالای ۹۰ درصد وابسته به یک جریان خاصی سیاسی هستند که در صدا و سیما حضور دارند.
🔹
چند شب صدا و سیما را نگاه کردم و اکثر کسانی که در آن حضور پیدا می‌کنند، وابسته به جریان پایداری هستند و این یک نوع تک صدایی به نظر می‌رسد.
🔹
واقعیت صدا و سیما نتوانست به حفظ اتحاد کمک کند و موفق نشد و حتی در یک جاهایی که حتما ناخواسته‌ بوده، از طرف مجموعه صدا و سیما به این وحدت خدشه وارد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/akhbarefori/653191" target="_blank">📅 14:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
کنست به انحلال خود و برگزاری زودهنگام انتخابات رای داد
🔹
کنست در جلسه مقدماتی خود با اکثریت ۱۱۰ عضو و بدون هیچ مخالفتی، به لایحه انحلال خود و جلو انداختن تاریخ انتخابات رأی داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/653190" target="_blank">📅 14:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
عراقچی برای شرکت در نشست ویژه وزرای خارجه شورای امنیت به نیویورک دعوت شده است. سخنگوی وزارت خارجه اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/653189" target="_blank">📅 14:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N17N17yUn0pzbxD1iTXeuBe0CjVFKrGZBZqzPB0ZQoxbA9TtHDFiC53FCuBKaX-6Lu_dA8dGeo_exDc0BUTcN84Ri7h2M9EHBLzblk7bs4j3J8OWdSkd-7kTG1UBQGXkD4ONVNgNkAvFc8qVqS_meA1XqhD_YBV-JleJwK1GlnSRMDSHK_wmYNlbL2kOl5AHzY8bxNaLvxWYbz94GeNpeI7AuPQFk1pyjxO7pbvckwhdRJ5fiZwq5eM4ea4TxU7tVDrLRDbrwupWU2hS4H2jIBbSjsB0tPPL50N3PfGuolfL9jfG382MwdN1n48FxGbYMNr6-SJ2R70SlXxuEvsZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✉️
پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
✏️
بسم‌الله الرّحمن الرّحیم
🌷
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی و رجائی و باهنر، تا رئیسی و آل‌هاشم و امیرعبداللهیان و لاریجانی، صدها شخصیت برجسته و تربیت‌یافته‌ی مکتب خمینی کبیر و خامنه‌ای عزیز اعلی‌الله مقامهماالشریف که دفتر خدمت خالصانه و مجاهدانه‌ی مسئولان جمهوری اسلامی را با امضاء خونین خود مزیّن کردند.
🔸
از زمره‌ی ویژگیهای بارز شهید رئیسی، مسئولیت‌پذیری، جوانگرائی، توجه به عدالت، دیپلماسی فعال و نافع، و بخصوص مردمی بودن را می‌توان برشمرد. این خصوصیات موجب دلگرم شدن دوستان ایران از جمله مجاهدان جبهه‌ی قدرتمند مقاومت و بسیاری از دلسوزان نظام می‌شد. این همه البته با معنویتی که ریشه در عمق جان او داشت، آمیخته بود. در رابطه‌ی بین مسئولین و مردم، خصوصیات مثبت تأثیرگذار، موجب قدردانی متقابل می‌شود. اینگونه بود که بدرقه‌ی او تا جوار مولا و مخدومش حضرت ابِی‌الحسنِ‌الرّضا صلوات‌الله و سلامه ‌علیه با شکوه کم نظیری صورت گرفت. دوران ناتمام ریاست جمهوری آن شهید، مقیاسی از تلاش و دلسوزی برای ملت و کشور در عین حفظ استقلال آن را فراهم ساخت.
🇮🇷
اینک ما در برابر حماسه‌آفرینی‌های ملت ایران در مقاومت منحصر به فرد تاریخی مقابل دو ارتش تروریست جهانی هستیم. این امر، بار تکلیف مسئولان جمهوری اسلامی ـ از رهبری و رؤسای قوا تا همه‌ی سطوح مدیران ـ را سنگین‌تر از گذشته می‌کند. امروز شکر نعمت انسجام ملت و دولت و تمامی دستگاه‌های جمهوری اسلامی، در تقویت انگیزه و خدمت مضاعف و مجاهدانه‌ی مسئولان، گره‌گشایی از مسائل و دغدغه‌های مردم خصوصاً در عرصه اقتصادی و معیشتی، حضورهای میدانی و مستقیم، و تعریف نقش جدّی برای مردم بعثت‌یافته در مسیر پیشرفت کشور و حرکت امیدوارانه به‌سوی آینده‌ی روشن است.
🤲
رحمت و رضوان الهی بر شهیدان راه خدمت و نصرت الهی و دعای سرورمان عجل‌الله تعالی فرجه‌ الشریف پشتوانه‌ی خدمتگزاران به مردم مسلمان ایران باد.
✍
سیدمجتبی حسینی خامنه‌ای
🗓
۳۰/اردیبهشت/۱۴۰۵
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/653188" target="_blank">📅 14:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW5iJXP_FkT5JfBq_GD0Msjxha1tM1c8qcyYFURvRWN1bqpa9yge2tt4Ts75k42lNO4typF8xiWXVubbkgu6t5_jCOW_tlCklhiXQR2L3zbmXew5IlzPzy7j0c1EwWfx12ACsrbrbYkNvvPS-C2s8kFMIAMxXWxqTcIS7_ACYrAMjS0Vs93-ITARPpSrpZMg037CeV6g5qBbPNYSJXAsymWW0hTPLDIcSpGyXpPgiSkY05hANGHbsYgQbELvsGIGP17TD2UQX9JFyj_0JMt6Mm6ISBjkv13iGJPYNDb8GuLlJr7PBOeqBckZs2QKelyYZBNIMCsG9GxWcCifeX5VJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجه انگلیس: بحران ایران جهان را به‌سوی گرسنگی گسترده می‌برد
ایوت کوپر، وزیر خارجه انگلیس:
🔹
بر اساس برآورد برنامه جهانی غذا، اگر جنگ با ایران تا اواسط سال پایان نیابد، حدود ۴۵ میلیون نفر ممکن است با ناامنی غذایی حاد و خطر گرسنگی روبه‌رو شوند.
🔹
ادامه انسداد تنگه هرمز، انتقال جهانی کودهای شیمیایی را تقریباً متوقف کرده و امنیت غذایی میلیون‌ها نفر را تهدید می‌کند.
🔹
جهان در حال «خواب‌گردی به‌سوی یک بحران جهانی غذا» است. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/akhbarefori/653187" target="_blank">📅 14:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isFkKEfDrOmWtdEzFNNoXTa4tEK1lA6Tn4pbVlDajitXM8lyNh6lcjdmOarpgw7X9TUmlpzpziG9YR1r-scJmXnfvWJYdpnKsuboUldGcxrnN5SQpEJIrm-Q8yQf0lGruMuccmgb-63dobHCO8ABZz9dgikL189co49THRJw2mo86ntBXHodsTgFDU9mAptTIcamZMIVt0nQ---0h3m45R4ya9ZFXDsweIJ0JVDtqr5wdScTZaKk8Lhi34OX0PIAOBdpFheDIyrZBMSO204E6ZsQzWl2jnZ3MeHbBSREgvu5Hz36wv4DsmE3a9ou2mgJQNgXhw7raw2L6_o_javksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صنعت نفت اجازه نداد در شرایط جنگی چرخه تولید و تأمین سوخت کشور دچار وقفه شود
🔹
رئیس‌جمهور ضمن قدردانی از تلاش‌های شبانه‌روزی مدیران، مهندسان و کارکنان صنعت نفت در حفظ پایداری تولید و تأمین انرژی کشور در شرایط حساس اخیر، دو مأموریت راهبردی را برای مدیریت بهینه منابع انرژی و ساماندهی نظام تخصیص گاز به وزارت نفت ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/653186" target="_blank">📅 13:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
انحلال کنست در رأی گیری مرحله اول
🔹
کنست اسرائیل در رای گیری مقدماتی به طرح انحلال خود و برگزاری انتخابات زودهنگام با اکثریت ۱۱۰ عضو و بدون هیچ رأی مخالفی رأی داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/akhbarefori/653185" target="_blank">📅 13:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سومین فایل صوتی قالیباف منتشر می‌شود
🔹
تا لحظاتی دیگر سومین فایل صوتی قالیباف خطاب به مردم با موضوع تبیین تحرکات دشمن برای آغاز دور جدید جنگ، ارتقای آمادگی دفاعی ایران و تشریح مسائل اقتصادی کشور منتشر می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/653184" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653182">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svH5QUHa2ZVJ68mIggUIjDf9oDeyDX0_HVBVLO4TKmbkzU9WJNPlwWip19rbuXTbHbyZ3O8mRLEZMX8jPkXhhfwacVe2V8dtLt2WfM_ZSbpGvqus78ojRaOqn81XtFjjHVkt1zFU0uV64S8GHxwjwiVQu7BPbBYfsm4Ngs4aZzaAabfczQeGkweJeMCor-iJoCXKzj6DawUQ-E4fhaEN8gbjaEYbe5xq0MfRIwV1N8PNEhUH8_wY-gI8XyC3lF0IRYKCC9SHDODTFrR4_YY4OjGs4y73A02VNXHuk3s5MRnGe9WCHeI8ASmjAq_Fx2NOZpxkqL7o267Nz58fLlRC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ساعتی دیگر پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/653182" target="_blank">📅 13:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653181">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77528fd9.mp4?token=Bm2B41Ya9lSRU-o5YNrx7WP-8LvqwbwlAxQkmKkdQl82Ieu7HimHqt6ZKxiCfKwiQ1VNsOLsKMkjMDOq33ZkaJemxX1c1x-1HKGaxw3DFSZb6ZqYm_qo_00pwBsLvMmT9-rf-LYnqxkhLf53qPSib5LmSVhXR1xxWoGYAgXug2q_YNm5GIYM48jNWBqTJVd9pw630B-tCgk-UQb4HCn5d7Tlad750RoaL9imfXuAz4M7HXAnnYH-SrOBxE4cbxhIzEphUqVg-DWdEye87dodmq17mPkj2ynL0Bdo0fkT47EU2sAXMJQ88kAmopuL6UOkz531fmdTQhhE8eKHEojlCo5YLEUAAQR-zP5Cx2d5uYboZGWrg72389-Bnvi_5WC_AxfzzEm-gvPotbdSVE1Vv2cQUJHzyhXuN94UxCYEE2uNzCtRd056rPEDxFb-Z84A_FOjZ2j8rvXzeZ84lweCabRsT656jnM_ssmRhlYOFnprSYZ2_ZVOm3AkWsEyMAgsqjoxXAVDvBnqrAp1q7taf_IK4U1IIAGJWKJP_PnwVW8ZY8YcW7XSykAuj81AzZm11HqwOt4RoFyECTM70TiSsG0DiXw3LF6_IfFxBn9WhmZk0buB5XAWnD-p1NxYSyvP5vO0-B4iAEW71q90ILlChrXt8-u-_5GCUJktmHoFTj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77528fd9.mp4?token=Bm2B41Ya9lSRU-o5YNrx7WP-8LvqwbwlAxQkmKkdQl82Ieu7HimHqt6ZKxiCfKwiQ1VNsOLsKMkjMDOq33ZkaJemxX1c1x-1HKGaxw3DFSZb6ZqYm_qo_00pwBsLvMmT9-rf-LYnqxkhLf53qPSib5LmSVhXR1xxWoGYAgXug2q_YNm5GIYM48jNWBqTJVd9pw630B-tCgk-UQb4HCn5d7Tlad750RoaL9imfXuAz4M7HXAnnYH-SrOBxE4cbxhIzEphUqVg-DWdEye87dodmq17mPkj2ynL0Bdo0fkT47EU2sAXMJQ88kAmopuL6UOkz531fmdTQhhE8eKHEojlCo5YLEUAAQR-zP5Cx2d5uYboZGWrg72389-Bnvi_5WC_AxfzzEm-gvPotbdSVE1Vv2cQUJHzyhXuN94UxCYEE2uNzCtRd056rPEDxFb-Z84A_FOjZ2j8rvXzeZ84lweCabRsT656jnM_ssmRhlYOFnprSYZ2_ZVOm3AkWsEyMAgsqjoxXAVDvBnqrAp1q7taf_IK4U1IIAGJWKJP_PnwVW8ZY8YcW7XSykAuj81AzZm11HqwOt4RoFyECTM70TiSsG0DiXw3LF6_IfFxBn9WhmZk0buB5XAWnD-p1NxYSyvP5vO0-B4iAEW71q90ILlChrXt8-u-_5GCUJktmHoFTj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت آمریکایی‌ها در رابطه با حمله به قایق‌های ماهیگیری از زبان صیادان لارک
🔹
اینجا وطن ماست؛ به خاطر مشکلات و ناامنی نمی‌توانیم مثل قبل کار کنیم اما پای وطن ایستاده‌ایم.
🔹
برشی از قسمت چهارم مستند «ماجرای تنگه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/653181" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653180">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca1668589.mp4?token=Ked0BZA81nLV1Wr2ke_0JY2XL4L5-Rld8qA_J_shL13uUrwov5-DAN3c87Z-4-oYGCrwr4b9YuFGuWB1iXZcVf3ZPAgnt47vAQ2UcFIu5k5EzzIlwnOLqsKFAHCtchPejm4MRbJAUeV3vQZrbwFxR7m_Bp5IyK-fpwg97whzKYk6UBzJUy5cFz9XzSrzngo4XwOfQ6YjPnw1BNJrGDnX4DESlOyHYVQjEqMeCNqMYq-BDTrhvgIMtuv7hdguxE25K-mdayGunQPvckbEwbnGhMru79w2W2n5JZeg0vKyVAaKoLKW-Xn4NGZ2g-RCbbKaemmfI_m1IVU0cHcRYGan3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca1668589.mp4?token=Ked0BZA81nLV1Wr2ke_0JY2XL4L5-Rld8qA_J_shL13uUrwov5-DAN3c87Z-4-oYGCrwr4b9YuFGuWB1iXZcVf3ZPAgnt47vAQ2UcFIu5k5EzzIlwnOLqsKFAHCtchPejm4MRbJAUeV3vQZrbwFxR7m_Bp5IyK-fpwg97whzKYk6UBzJUy5cFz9XzSrzngo4XwOfQ6YjPnw1BNJrGDnX4DESlOyHYVQjEqMeCNqMYq-BDTrhvgIMtuv7hdguxE25K-mdayGunQPvckbEwbnGhMru79w2W2n5JZeg0vKyVAaKoLKW-Xn4NGZ2g-RCbbKaemmfI_m1IVU0cHcRYGan3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون در کانال ۱۳ اسرائیل:
🔹
فکر نمی‌کنم ایالات متحده به اسرائیل بدهکار باشد. فکر نمی‌کنم ایالات متحده باید چیزی به اسرائیل بدهد.
🔹
فکر می‌کنم باید تمام کمک‌ها به اسرائیل و تمام توافق‌های ویژه برای اسرائیل را از فردا متوقف کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/653180" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653179">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
غربالگری آسیب دیدگان دبستان شجره طیبه میناب
🔹
رئیس مرکز بهداشت میناب: معلمان، اولیا و آسیب دیدگان روحی بازمانده از حمله به مدرسه شجره طیبه، امدادگران و مردم شاهد حادثه، از نظر سلامت روان غربالگری می‌شوند.
🔹
این غربالگری از هفته آینده برای بررسی سلامت روان بیش از ۱۴ هزار نفر اجرا می‌شود.
🔹
معلمان، اولیا و آسیب دیدگان روحی بازمانده از حمله به مدرسه شجره طیبه، امدادگران و مردم شاهد حادثه، نیز از نظر سلامت روان غربالگری می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/653179" target="_blank">📅 12:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLDuzI3MTIk49R7Jje_kpgmRjYS8k1hT_J8_5jEZYUNllBmZqjtAqcmEoNGO8fnUFu8JEQXoaed2vaH-GZC33KJD5KCJ8z8Z1SM5ewybXMacKBtfqmPiWLgvpi49GCLJJ0KoKrA2RD2EwI6PHs3cNBQZ9D2zTa73Z_gASCf4y4wZXLpHYxQuJ4E9a7yvalr_2VN2VXIsyqqwqKGYZg6O1HZm_iq8sBI2jxevfpfUIYnTsazGgZVl6If4KH5UNhY19L5rQhgWXxigbfBklzoDTA3ut--sw9aHGP0WR79xv7063li9RlMFfivH0MbvTXY5i9ERIJLeqwxzGxDQrdXHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دومین گفت‌وگوی تلفنی ترامپ و نتانیاهو در چند روز اخیر
🔹
رئیس‌جمهور آمریکا و نخست‌وزیر اسرائیل دیشب تماس تلفنی طولانی داشتند که بسیار مهم توصیف شده است.
🔹
آن‌ها یکشنبه با هم درباره ایران گفت‌وگو کرده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/653178" target="_blank">📅 12:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653177">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih2Y8ZQjLCxbaWxdBLLVTTs8RmAuXyvG-gdRCJfp6A3EnCMvPlpkBHtFWZjV1nBDEp2MbS1j6UFnkRldzveBnfpJU4KQx5p19IHA_m0YZFsS8VDudSbpTUz4vhDMjrmxcOVCA0JeAJRyPg-z1RiZ8aHBI59ZNvKWvzXbk2x5HaYXISXIoFJdgLKKHgtfisJ6N8ChVpEpB-zUELdQQ5tw8eV6KWNswfzel38Q6kh32Tn31S_yxU3QPdqnfDRVIvK8tk3LrdzqSmJzJLILa4dGUXycbD3jWipnNpNrql1TRP-e1t4Vc3ucFZ_m9hdYKSDO8mv2ZN7pnyAfiIL3tT2A_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی فضای مجازی: باید نسبت به پاکسازی زیرساخت‌های کشور از سخت‌افزارهای آمریکا سریعا اقدام شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/653177" target="_blank">📅 12:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
نشنال اینترست: فرمانده سنتکام در جلسه سنا به حقیقت و واقعیت توهین کرد
🔹
نشریه آمریکایی با اشاره به دروغگویی فرمانده سنتکام درباره کشتار غیرنظامیان ایرانی در حملات آمریکا، بی‌توجهی وزارت جنگ این کشور به تلفات غیرنظامیان در جنگ علیه ایران را نشان‌دهنده سیاسی‌کاری گستاخانه رئیس‌جمهور ایالات متحده دانسته که در حال گسترش در میان صفوف ارتش آمریکاست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653176" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653175">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a53595853.mp4?token=h4hUM-CWjhNLrvWwiZLa6fjUKG7JbO8x_WvO3HxXpOXx4zhlkJPtpgXaD6GzGAeQhoy7xCIsTBY1OxAlZFItzvP11P901UMgw2Q-F51REtghwNQAzxRzqy1sAarLiXpdQn5gMz5H26qTKGrh_C6ZnwLHLPsLf2hgdAnTMLYtN0q4eo8lO-__6QLIB7mDOLgWFEvLwE7epdOFNsCSXd3BYfdY4RtQcKEoEdrLpZ_KG_-NDDYR6ll8CkfehpPn7IOHQgT2C0-KQuQYUIbxNfgpdvIBaXSyvl9y6hNyvR_9NJoS0iAcC61BSEQSJDB9JFXjUSew884DwQdHUA71jtZf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a53595853.mp4?token=h4hUM-CWjhNLrvWwiZLa6fjUKG7JbO8x_WvO3HxXpOXx4zhlkJPtpgXaD6GzGAeQhoy7xCIsTBY1OxAlZFItzvP11P901UMgw2Q-F51REtghwNQAzxRzqy1sAarLiXpdQn5gMz5H26qTKGrh_C6ZnwLHLPsLf2hgdAnTMLYtN0q4eo8lO-__6QLIB7mDOLgWFEvLwE7epdOFNsCSXd3BYfdY4RtQcKEoEdrLpZ_KG_-NDDYR6ll8CkfehpPn7IOHQgT2C0-KQuQYUIbxNfgpdvIBaXSyvl9y6hNyvR_9NJoS0iAcC61BSEQSJDB9JFXjUSew884DwQdHUA71jtZf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار فرمانده سنتکام از پاسخگویی درباره جنایت مدرسه میناب
🔹
فرمانده سنتکام را درباره جنایت مدرسه میناب به چالش کشید و از او پرسید، تا کی می‌خواهید «پشت این ادعا که تحقیقات ادامه دارد پنهان شوید؟»
🔹
مارک استون خطاب به کوپر افزود، تیمی از شبکه اسکای نیوز همین الان در میناب هستند. آنچه آنجا رخ داد را دیده‌اند. هیچ مدرکی دال بر وجود پایگاه موشکی در آنجا وجود ندارد.
🔹
درحالیکه کوپر در حال فرار از پاسخگویی بود مارک استون دوباره وی را سوال پیچ کرد و گفت، تا کی میخواهید پشت این ادعا که تحقیقات در جریان است قایم شوید؟ «حداقل بگویید تحقیقات چه زمانی پایان خواهد یافت؟»
🔹
فرمانده سنتکام به جای پاسخگویی مسیر حرکت خود را تغییر داد و تلاش کرد با کمک محافظانش از دست خبرنگار اسکای نیوز فرار کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/akhbarefori/653175" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653174">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdoWrdVs4gMzAPvAf8qprN43deK-2bBtPgsYugOi2k7ZAEBiIWxMVWwpdgA6HbjQhe98aTqrwU_XjMlnLRiVP97DKB6KybDpIcMFztioAFXcZf5os4qbNo78pMZWvJzIldc0HpVsYVYLYituCaZap0hZIQ_Fou78N8qdoHL4Sk7H1SuDTf-csUBPudSaEoZYItAXuyp2ksUrQ5dX18mDvaCqiMwAvUS8BFWVFgkW0KVC8Iz4PjgeQICPBa7T0pRgoy78l-I5CsL3TCTP3XG0kIJLqr3XAoIURyrLiOcF7UlZCdGoBJXn2huKEbamv9N3el2m14EnPLQahtQrIctVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاثیر جهانی فناوری پهپاد شاهد ۱۳۶
🔹
کشورهایی که نسخه‌های خود را با الهام از این پهپاد ایرانی توسعه می‌دهند:
🔹
آمریکا
🔹
روسیه
🔹
چین
🔹
اوکراین
🔹
لهستان
🔹
ترکیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/653174" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653173">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تکذیب ادعاهای بی‌اساس خبرگزاری مهر درباره حقوق کارکنان بانک مرکزی
🔹
در پاسخ به گزارش منتشرشده توسط خبرگزاری مهر تحت عنوان «پرسش‌هایی درباره افزایش مزایای کارکنان بانک مرکزی در شرایط فشار تورمی»، ضمن ردّ اتهامات و ادعاهای بی‌اساس مطرح‌شده، به منظور تنویر افکار عمومی تأکید می‌شود که هرگونه افزایش حقوق و مزایای کارکنان بانک مرکزی کاملاً بر مبنای قانون بودجه سنواتی و مصوبات دولت  بوده و هیچ افزایش خارج از ضوابط یا رقم بی‌سند «۲۰ میلیون تومانی» در کار نیست.
🔹
تمام حقوق و مزایا بر اساس سقف‌های مصوب قانونی کشور پرداخت می‌شود و هیچ نوع مزایا یا تسهیلات ویژه‌ای خارج از ضوابط سازمانی و قانونی به هیچ یک از کارکنان پرداخت نشده است؛ از این رو ادعای مطروحه در خصوص تسهیلات کذب محض بوده و صحت ندارد.
🔹
آن خبرگزاری بدون استعلام و کسب اطلاع قبلی از صحت و سقم مطالب مطرح شده، اتهامات بزرگی را به سیاستگذار پولی کشور وارد کرده است. در شرایطی که کشور درگیر جنگ تمام‌عیار اقتصادی و تحریم‌های ظالمانه است و بانک مرکزی در خط مقدم مدیریت نقدینگی، کنترل تورم و ثبات‌بخشی به بازار ارز قرار دارد، اتهام‌زنی بی‌اساس به سیاستگذار پولی نه تنها غیرحرفه‌ای، بلکه در تضاد با نیاز مبرم کشور به اعتمادسازی نسبت به سیاست‌های پولی برای دستیابی به اهداف اقتصادی است.
🔹
شایسته است خبرگزاری مهر توجه داشته باشد که در دوران جنگ رمضان، با وجود ابلاغ حضور ۲۰ درصدی کارکنان دستگاه‌های اجرایی، بیش از ۶۲ درصد از کارکنان بانک مرکزی در محل کار خود حاضر شدند و اجازه ندادند حتی یک لحظه چرخه نظام پولی و ارزی کشور متوقف شود؛ این فداکاری و مسئولیت‌پذیری سزاوار چنین اتهام‌زنی‌هایی نیست.
🔹
بی‌تردید در شرایط حساس کنونی که دشمنان نظام از هیچ تلاشی برای ضربه زدن به اقتصاد ایران فروگذار نمی‌کنند، باید منشأ چنین اظهاراتی بررسی شود تا مشخص گردد کدام جریان به دنبال تخریب سیاستگذار پولی کشور و ایجاد بدبینی عمومی نسبت به بانک مرکزی است. از خبرگزاری مهر انتظار می‌رود به جای دامن زدن به شایعات، امانت در انتشار اخبار را رعایت کرده و در مسیر حمایت از ثبات اقتصادی کشور گام بردارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/653173" target="_blank">📅 11:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnTWQZwsr-dDF47hlNtzcZhymcIV3xDsWODlEg7tLThbfzeDCF-rds3d7FmSCeTvHI8GJww62YwWhz3fZIhQvPf30kOWFTb1uH_YwY5_AsY19l--LiAdFJry46BAGQ2jBhGmtxjM1IaN9-rL5D32_-LPLfMmBYGXri72siRrKVN9nXEnZJoArm-LZjXKUXH31PXi_cnrPFsxduE7HBdp2QMZr6vX1ivHEBnPiJaW-i9yhl22uGsLtWgkJLoEgkQXOUTMKQq4jHFFcmwlc5QtXmRASWfLRmCnkMbOY9gjreJ6hpwuRvuVDldaM0dM0peNslj7vuND1KWb4ml1-hvlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصوبهٔ جدید قیمت چای اعلام شد
🔹
براساس مصوبهٔ جدید کارگروه تنظیم بازار کالاهای کشاورزی، تشکل‌های مرتبط موظف شدند با هماهنگی سازمان حمایت، قیمت انواع چای را به‌صورت دوره‌ای تعیین و اعلام کنند؛ دولت همچنین بانک مرکزی و وزارتخانه‌های صمت و راه را مکلف به کنترل بازار چای کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/653172" target="_blank">📅 11:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شی و پوتین حملات آمریکا و اسرائیل به ایران را محکوم کردند
🔹
رئیس‌جمهور روسیه و چین امروز در بیانیه‌ای مشترک حملات نظامی آمریکا و اسرائیل به ایران را محکوم کردند.
🔹
در این بیانیه آمده است «طرفین اتفاق نظر دارند که حملات نظامی آمریکا و اسرائیل به ایران، ناقض حقوق بین‌الملل و اصول اساسی روابط بین‌الملل است و به‌طور جدی ثبات در خاورمیانه را تضعیف می‌کنند».
🔹
دو طرف در بیانیه مذکور، بر ضرورت بازگشت هرچه سریع‌تر طرف‌های درگیر به گفت‌وگو و مذاکرات با هدف جلوگیری از گسترش دامنه درگیری، تأکید کردند.
🔹
آنها همچنین از جامعه بین‌المللی خواستند موضعی عینی و بی‌طرفانه اتخاذ کند، به کاهش تنش‌ها در منطقه غرب آسیا کمک کند و به‌طور مشترک از اصول بنیادی روابط بین‌الملل حفاظت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/akhbarefori/653171" target="_blank">📅 11:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGHkrR0JauLnTrQnNNCy2NzOhUcolCXhYCRmglumGDRQ8vMEBKAoLSlKuKkGEYfZexli9e7sOqv7Feg3fr5cyYwJ-arqbKd69tSSqT05kjCH0nmX-0qYsdH6rPr8yZwqjFp4ou859YNQ2VOIuAkhx6fkpfdhlUInl623khtdffTDrldk0jOyXb6sZy04BZ0YztCExG63xVzCvIA6LjbAP-7Fzz4P2FYWKnYzXdPcyzMVQNfCJyHWN4GC6gS-I1P0CiCudLMwtEK-j6AkKB_n8kNIem1B_gZIro1TbfTJ_8RgniySKFXcv4hDK9RKaxROx6afvci3ncw3OvV-cQbnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشت خشخاش ممنوع است
🔹
قوه‌قضائیه: براساس قانون کشت گیاهان مخدر از جمله خشخاش «مطلقاً ممنوع» بوده و مرتکبان با توجه به اهمیت و تکرار جرم، به مجازات‌های قانونی محکوم خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/653170" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653169">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
یک سوم جمعیت کشور تا ۳۰ سال آینده سالمند می‌شود
🔹
وزیر فرهنگ و ارشاد اسلامی در همایش روز ملی جمعیت: اکنون جمعیت سالمند بالای ۶۰ سال ما حدود ۱۲ میلیون است، اما در سه دهه آینده مطابق نرخ باروری ۱.۳۵ که داریم، جمعیت سالمند کشورمان معادل یک سوم جمعیت کل کشور می‌شود.
🔹
ناترازی جمعیت کمتر از ناترازی آب و برق نیست؛ اما چون بحران آب و برق روزمره دیده می‌شود، ما را درگیر می‌کند، در حالی که بحران جمعیت پنهان است و زمانی متوجه عمق فاجعه می‌شویم که شاید برای جبران خیلی دیر شده باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/akhbarefori/653169" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cacafa4c.mp4?token=VFQppqUB461EEZOmMiLXeopWIUpdHlvJtcLxQjLnph8jL1QoMmFAqIWAn5lzoHXb2gfuqGZjirg6HgNoNyNXBmHRewO_wOqf_9j4sLNPmaPRNXbOY6ubQFvZLTIx_yB3yVn1fr_3MR6F_eR7v-KySNFGznB_Vz3ehmSo7W-Yih_c4VlgrwzYBsFM8uTz3wjqxU9khUK8Xn8J-1htx2p8tH59eNDCBLx4Bq32g-09BtD0xIBNqrxbzw_8e5rEQ3riIAzzqigoYdPqVapmgCscWNCx7gubzRolKw3xpk6x3v1lZbkDyn-q-uJKOqaAKgwEax9lnr9toWdWPE5w88jO_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cacafa4c.mp4?token=VFQppqUB461EEZOmMiLXeopWIUpdHlvJtcLxQjLnph8jL1QoMmFAqIWAn5lzoHXb2gfuqGZjirg6HgNoNyNXBmHRewO_wOqf_9j4sLNPmaPRNXbOY6ubQFvZLTIx_yB3yVn1fr_3MR6F_eR7v-KySNFGznB_Vz3ehmSo7W-Yih_c4VlgrwzYBsFM8uTz3wjqxU9khUK8Xn8J-1htx2p8tH59eNDCBLx4Bq32g-09BtD0xIBNqrxbzw_8e5rEQ3riIAzzqigoYdPqVapmgCscWNCx7gubzRolKw3xpk6x3v1lZbkDyn-q-uJKOqaAKgwEax9lnr9toWdWPE5w88jO_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم پناه معاون اجرایی رئیس جمهور: جمهوری اسلامی آماده است در مقابل حوادث طبیعی و  جنگ و یا حمله از تک تک آحاد ملت دفاع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/653168" target="_blank">📅 11:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
جنگ منطقه‌ای که وعده داده شده بود با تکرار تجاوز، به فراتر از منطقه کشیده خواهد شد
🔹
بیانیه سپاه پاسداران انقلاب اسلامی: دشمن آمریکایی صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پر هزینه ترین ارتش های جهان هستند به ما حمله کردند اما ما همه ظرفیت های انقلاب اسلامی را علیه آنان وارد عمل نکردیم.
🔹
اما اینک اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، اینبار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.
🔹
ما مرد جنگیم و قدرت ما را در میدان نبرد خواهید دید و نه در بیانیه های توخالی و صفحات مجازی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/653166" target="_blank">📅 11:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
‌ابلاغ سهمیۀ بانک‌ها برای وام ازدواج و فرزندآوری
🔹
براساس ابلاغیۀ بانک مرکزی به شبکۀ بانکی، در سال جاری ۴۳۵ همت تسهیلات قرض‌الحسنۀ ازدواج و فرزندآوری پرداخت می‌شود که از این میزان ۳۵۰ همت برای ازدواج و ۸۵ همت فرزندآوری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653165" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0686366cf9.mp4?token=lqPfNfSCzV5MHS1DWIYAW60XeG6CPyT8hEq4iLFZWEsciioYsliu40lT8iOZQWHMze96FweP7VSuuEZcjgTd1m211jJSdtDi2mV6WPIy9O2nzrv-7EPKBsfUpy2nxs4n9iRJJ_CGEEcLZdPMx4FQCcgSzFe037Iymcr1UW5Ub_Wr31-I1HNkMz4pJkqZF18WFQqgCsB_OYBRhul0h0_GRGgYNfMwfYyDJny74FZv1SQWL8bjZruoPHGxwb2WSP_ik8fEjBp59fQuTMyYZs3Kofr50M_PMcYsdr2LMebp7IBrmRGMikclrnCxyMp87NDE45cDfnIvAvYt_uBpEJVbQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0686366cf9.mp4?token=lqPfNfSCzV5MHS1DWIYAW60XeG6CPyT8hEq4iLFZWEsciioYsliu40lT8iOZQWHMze96FweP7VSuuEZcjgTd1m211jJSdtDi2mV6WPIy9O2nzrv-7EPKBsfUpy2nxs4n9iRJJ_CGEEcLZdPMx4FQCcgSzFe037Iymcr1UW5Ub_Wr31-I1HNkMz4pJkqZF18WFQqgCsB_OYBRhul0h0_GRGgYNfMwfYyDJny74FZv1SQWL8bjZruoPHGxwb2WSP_ik8fEjBp59fQuTMyYZs3Kofr50M_PMcYsdr2LMebp7IBrmRGMikclrnCxyMp87NDE45cDfnIvAvYt_uBpEJVbQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا سرشار: جنگ فعلی ۸ سال طول نمی‌کشد و حداکثر در همین یکی دو ماه جمع می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/653164" target="_blank">📅 10:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b013a6c4.mp4?token=pO1W8cYPkZcWSUlD55r_Qr79H2xR33QtB9omTt-WH4GmbwlT0PZM7S2KSP_ox43m_szHBcC3_UalvrwNl6E62stGgdLQqobeMGmdEQlakikIKV_e4bYFinscAXyW_AAAe8ZqK-ki76C4LazdTBShv7o4Oy9horK-Eg5gJkeSnTyP1GSeoP8S7sC4KjXIWor5KLS2_9uaZYbbxdjOuJweWwiyxOHHKw2XylUuD7gYX9ziyWEtKb6MdPWytBJlC9MVKaQvuewANqQ3UHYLu3BdNtHkWH02SFHJe0C15pmxmHc1cyNGPD7gHXDzRqGTEqV-uRsbsB-8dwBqdr-n_iSevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b013a6c4.mp4?token=pO1W8cYPkZcWSUlD55r_Qr79H2xR33QtB9omTt-WH4GmbwlT0PZM7S2KSP_ox43m_szHBcC3_UalvrwNl6E62stGgdLQqobeMGmdEQlakikIKV_e4bYFinscAXyW_AAAe8ZqK-ki76C4LazdTBShv7o4Oy9horK-Eg5gJkeSnTyP1GSeoP8S7sC4KjXIWor5KLS2_9uaZYbbxdjOuJweWwiyxOHHKw2XylUuD7gYX9ziyWEtKb6MdPWytBJlC9MVKaQvuewANqQ3UHYLu3BdNtHkWH02SFHJe0C15pmxmHc1cyNGPD7gHXDzRqGTEqV-uRsbsB-8dwBqdr-n_iSevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود بالگرد نظامی رژیم اشغالگر در بیمارستان رمبام که تعدادی از مجروحان ارتش رژیم صهیونیستی را انتقال داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/653163" target="_blank">📅 10:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60095701d8.mp4?token=qtlDREG4xgZedk-IIIj46jO1zXf1RaYV3TiJPB-KSbwH1gMOzVo_TPXIL2GHgma99utQc1MVUnAReKJJJ70YCbYbH1URG39k9gxXS3Gg5I6L5Z-BAMQ1lAOpZN0whItTWU6ReIYDeqXFmHkTUCOxLbvy7HSmsCHu3qPhfmnpRnAOx2oE7hFxzv3Q4OGor1CNQW6zNQWvGNEib1W183t_gii5oZKqk8JNayUhRvXB23betsWSe_YGCYByNh7I-t0xWSJL1zcp8KKgH7_jFJtdI5vyk5qUS9_TNQ8b8PSUHP0obTDJEZNNgY3aZxAIDwa3SRxLG-XsU5-VdGYMa0U_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60095701d8.mp4?token=qtlDREG4xgZedk-IIIj46jO1zXf1RaYV3TiJPB-KSbwH1gMOzVo_TPXIL2GHgma99utQc1MVUnAReKJJJ70YCbYbH1URG39k9gxXS3Gg5I6L5Z-BAMQ1lAOpZN0whItTWU6ReIYDeqXFmHkTUCOxLbvy7HSmsCHu3qPhfmnpRnAOx2oE7hFxzv3Q4OGor1CNQW6zNQWvGNEib1W183t_gii5oZKqk8JNayUhRvXB23betsWSe_YGCYByNh7I-t0xWSJL1zcp8KKgH7_jFJtdI5vyk5qUS9_TNQ8b8PSUHP0obTDJEZNNgY3aZxAIDwa3SRxLG-XsU5-VdGYMa0U_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین و شی بیانیه مشترک تعمیق روابط دو کشور را امضا کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653162" target="_blank">📅 10:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAl8cIZtb0jsGO4AYbFFf10h366xGuo4iKuLsSQdSMXcJDcepVzH6QSL8vcK2BSXMBPui2rR0PxRr8yshIPfvkO0YODuIMZxsrflxqPPsd4mYB4yDXePJSs6r0NaFlOwqZv_FA-EQ_DNmddvCy0uqK8IVAzgA4zDjF9G4WDwDgheDMP5tYjiBl9oV-EgAv5y1aijVQxHIDydgXbZiZoPXxUUhZmruNrH84s-nzL-Mh9wf0MYnZM7C5w4GFFNcrYpsk9ShBNsTvZ6VouBpsP3CEGTUH48cteT1MNG-nxc7KdB_cwXe-JWkKfycnNza86GXuxkeyDs4YMiYp3_8mzTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: اگر برای مدیریت مصرف برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید و راهکارهای خلاقانه برای عبور از مشکلات طراحی شود.
🔹
یا راهی پیدا خواهیم کرد یا راهی تازه خواهیم ساخت؛ اما لازمه این مسیر، رها شدن از قالب‌های ذهنی محدودکننده و نگاه‌های محدود در تصمیم‌گیری است.
🔹
اگر روش‌های پیشین به‌تنهایی قادر به حل مسایل بود، بسیاری از مشکلات تاکنون برطرف شده بود.
🔹
اگر برای مدیریت مصرف آب، برق، گاز و بنزین برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد.
🔹
باید مردم را برای صرفه‌جویی و مدیریت مصرف به همکاری دعوت کنیم تا بتوانیم کشور را با عزت و اقتدار از شرایط فعلی عبور دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/653161" target="_blank">📅 10:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp0ZXp0-K1OwL4fLMJm4P5ClwFeT_L2aRsY1eThxc0tnOOlAy5LYjPjPwvlpLn0yUUetOKQr0TKaxm7EMTyVpfHSBhlKMnzXvPPOUoAqDtunEef-bdHVY0hVdFmkwCDxxu-yWs5FvKjeUG9SXKj3_8T7cql3UqEFG6QTh_g_4dMrQhu_TyGLCZGYiTYd6bc1M7saYyzXNo68Pd-gdLWU5C-Q9UxPqPUwr-XcmyhFZTj6P53YwdeEeJCeLV1xof5llhDm7IPyM5J2d1kTtyGJdAo46vVUlK8KFi4lDxA7-sDHPacYzLkCrvskcTMo94emmPs1whcdD5IFCc3cWuswWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران: در صورت از سرگیری جنگ هیچ آتش‌بسی را نمی‌پذیریم
🔹
سفارت جمهوری اسلامی ایران در وین امروز و در پی ادعاها و تهدیدات دونالد ترامپ رئیس‌جمهور آمریکا درباره حمله به ایران عنوان کرد: چرا رئیس‌جمهور آمریکا (دونالد ترامپ) معتقد است که انجام یک حمله‌ به اصطلاح «کوتاه» به ایران، تهران را به مذاکره بیشتر متمایل می‌کند؟
🔹
در این پیام که در صفحه ایکس این سفارتخانه منتشر شد، آمده است: بر اساس همین فرض اشتباه، که ناشی از برداشت عمیق نادرست از واقعیت ایران است، پیش‌بینی کرد که جنگ کمتر از یک هفته طول خواهد کشید، اما این جنگ ۴۰ روز به طول انجامید.
🔹
سفارت جمهوری اسلامی ایران در اتریش در این پیام خاطرنشان کرده است: اشتباه نکنید: اگر ایران مجدداً مورد حمله قرار بگیرد، این بار تا زمانی که همه اهدافش به طور کامل محقق نشود، با هیچ آتش‌بس یا مذاکره‌ای موافقت نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/653160" target="_blank">📅 10:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4b6ad821.mp4?token=ert23TTPfhIThKcFzLPa4TZVTWFxDvMHRXt78SAP9mzXj0NyhaUbE-HL4CT66Q4l4PNxn6s2HS9Jo4dv57fm0tG888uRNf3sQFUIycPbyRFZS1wUE1JDObqskJOEDT7pZQI0HQ8mLkO6FAqhc1ldPq7DL9Esiz7kidKp-6l3C68RCupFcREA5_4Y79Bf4o5anYjOiMjajhYZliCGKl1gEvOs0USujd8i2AAv4IK_jAa2Hs434CSMs4a6JYIJcqxMChBB9HPB6pj7DF2GxqzdttWihXcK76c1vPKuVHdIbsbl6ViLEG8fJShhstfXGHuEdNjJVf9uE1FozEh4A9g8KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4b6ad821.mp4?token=ert23TTPfhIThKcFzLPa4TZVTWFxDvMHRXt78SAP9mzXj0NyhaUbE-HL4CT66Q4l4PNxn6s2HS9Jo4dv57fm0tG888uRNf3sQFUIycPbyRFZS1wUE1JDObqskJOEDT7pZQI0HQ8mLkO6FAqhc1ldPq7DL9Esiz7kidKp-6l3C68RCupFcREA5_4Y79Bf4o5anYjOiMjajhYZliCGKl1gEvOs0USujd8i2AAv4IK_jAa2Hs434CSMs4a6JYIJcqxMChBB9HPB6pj7DF2GxqzdttWihXcK76c1vPKuVHdIbsbl6ViLEG8fJShhstfXGHuEdNjJVf9uE1FozEh4A9g8KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم پناه معاون اجرایی رئیس جمهور: دشمن رهبر انقلاب را شهید کرد اما ما تسلیم نشدیم و بلافاصله ایستادیم و به ابرقدرت دنیا پاسخ دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/akhbarefori/653159" target="_blank">📅 10:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رئیس‌جمهور کره جنوبی: اسرائیل شهروند ما را ربوده است
🔹
لی جائه میونگ رئیس جمهور کره جنوبی در پی بازداشت یک فعال شهروند کره‌ای توسط نیروهای اسرائیلی در کاروان کمک‌رسانی به غزه (ناوگان صمود)، بیانیه‌ای تند علیه اسرائیل صادر کرد.
🔹
او در این بیانیه اعلام کرد: اسرائیل یکی از شهروندان ما را در شرایطی ناعادلانه و برخلاف قوانین بین‌المللی ربوده است.
🔹
لی همچنین با اشاره به واکنش کشورهای اروپایی افزود: بیشتر کشورهای اروپایی می‌گویند ناچارند بنیامین نتانیاهو را بازداشت کنند؛ ما نیز باید تصمیم خودمان را بگیریم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653158" target="_blank">📅 09:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBlUfddUUE5n8p_6xxUmyRsPMdIDa3mqpn9dTd9LHSEFtb1gYJpMrSwn1pQdi0UrwRB_HZ3WZDxAMSjBX38QKtJQU-nULIx_vwdqfP0ysPsK4B3Iiu98Tk54RpFHHKEJFg08aunLf0TYeEe_cNjUT2xacYjHHz2IqSeCRFWmwNtK_H6l3w9zwfquT50_c73OH4v62XQyMfFQLkUx_yG3m5zGl9r-WUpN3gGsIkrjbGYA1U7JeVqsgTKV6YOYN88XBzLSH8Pp5IZqeLBs710yBNB8jTvYhlTO2gDn4Rb8ZuIESKkYsawClxxFqfPEqU_4X8RlOlebgX5dg9XJT3BT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روند تخلیه و انتقال کالاهای اساسی با جدیت پیگیری شود/ لزوم ساماندهی فوری بازار اجاره مسکن
🔹
رئیس سازمان بازرسی کل کشور در دیدار با وزیر راه و شهرسازی با تأکید بر ضرورت آمادگی مستمر دستگاه‌ها در شرایط جنگی و پساجنگ، خواستار فعال‌سازی ظرفیت بنادر شمالی و تقویت مسیرهای ریلی و زمینی شد و گفت: روند تخلیه و انتقال کالاهای اساسی با جدیت پیگیری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/akhbarefori/653157" target="_blank">📅 09:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
انفجار پهپاد حزب‌الله در ساختمان محل حضور نظامیان صهیونیست در جنوب لبنان
🔹
یک پهپاد انتحاری متعلق به حزب‌الله که با فناوری فیبر نوری عمل می‌کند، در داخل ساختمانی در جنوب لبنان که نیروهای ارتش اشغالگر اسرائیل در آن سنگر گرفته بودند، منفجر شد.
🔹
این انفجار منجر به زخمی شدن فرمانده لشکر ۴۰۱ و تعدادی از نظامیان شد که با هلیکوپتر به بیمارستان‌ها منتقل می‌شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/653156" target="_blank">📅 09:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
زخمی شدن فرمانده تیپ زرهی ارتش اسرائیل در جنوب لبنان
🔹
پایگاه خبری صهیونیستی واللا گزارش داد که فرمانده تیپ زرهی ۴۰۱ و چند نظامی این رژیم در حمله پهپادی حزب‌الله زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/653155" target="_blank">📅 09:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
دبیر ستاد ملی جمعیت: با این فرمان جلو برویم در سال ۲۱۰۰ میلادی ۳۱ میلیون جمعیت خواهیم داشت!
🔹
دستجردی، دبیر ستاد ملی جمعیت: اگر ما با این فرمانی که داریم جلو می‌رویم که نرخ باروری ما پایین ‌ترین حد هست، پیش برویم در ۷۵ سال آینده در سال ۲۱۰۰ میلادی ما ۳۱ میلیون جمعیت خواهیم داشت و دیگر نیازی به جنگ نخواهیم داشت، خود جمعیت آنقدر کم خواهد شد که در حقیقت ما از صحنه جغرافیای دنیا حذف می‌شویم.
🔹
اگر بتوانیم وضعیت خودمان را ارتقا بدهیم نرخ باروری را به ۱.۹ برسانیم ۶۲ میلیون نفر در ۷۵ سال آینده جمعیت خواهیم داشت و اگر بتوانیم بیشتر موفق باشیم و نرخ باروری افزایش بدهیم، بالای ۱۰۰ میلیون جمعیت خواهیم داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/akhbarefori/653154" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed19b408e4.mp4?token=AU088WmLNnNa_JDpHMHJEnKMkQGtGLK9HPVIBfU-eEQHc9VVirvVaTTsRYB_zpnsi31-96bZOZjJA2i_L9oNSX0yVf7ml3hatQrIbCFEaLwkuOkigXbJMbD-FNqN1m_O3z0_yohCwX485jjBUSrbZn3GfJM83bu-AhbVwdvK0vDNwWXUvecNyRY4HjaUoRqf-ziiAgy-uqsQrAYEvGRdA0jEC8W42CEjtDM4dIY0QKXBj52mxo-NG3hDG5eRHuScqvH8b2lTwteafwq-5iDh1O4RB3tQEfcwsXBkW_GkjV2JuokOwzhP9PtKSL-mnelX2OB7QoURPz2v9tuzEoNyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed19b408e4.mp4?token=AU088WmLNnNa_JDpHMHJEnKMkQGtGLK9HPVIBfU-eEQHc9VVirvVaTTsRYB_zpnsi31-96bZOZjJA2i_L9oNSX0yVf7ml3hatQrIbCFEaLwkuOkigXbJMbD-FNqN1m_O3z0_yohCwX485jjBUSrbZn3GfJM83bu-AhbVwdvK0vDNwWXUvecNyRY4HjaUoRqf-ziiAgy-uqsQrAYEvGRdA0jEC8W42CEjtDM4dIY0QKXBj52mxo-NG3hDG5eRHuScqvH8b2lTwteafwq-5iDh1O4RB3tQEfcwsXBkW_GkjV2JuokOwzhP9PtKSL-mnelX2OB7QoURPz2v9tuzEoNyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم نباید خسارت‌های وارد شده به آمریکا و رژیم صهیونیستی را فراموش کنند
🔹
داوودی، کارشناس مسائل بین‌الملل: طبق منابع خودشان، کشته‌های آمریکا در جنگی که ورود زمینی نداشتند: ۸۰۰ تا ۹۰۰ نفر / کشته‌های اسرائیل: بیش از ۱۶۰۰ نفر
🔹
زخمی‌های آمریکا: بالای ۱۰۰۰ نفر / زخمی‌های اسرائیل: بیش از ۸ هزار نفر – در حالی که هر دو طرف آمار را خیلی پایین‌تر اعلام می‌کنند.
🔹
خسارت انسانی فراتر از تصورشان است. حتی منابع آمریکایی می‌پرسند: این همه تلفات برای سربازانی که وارد جنگ نشدند، یعنی چه؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653153" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH6rRfYdLk1v__rCwP1asl8jofLVAUjnt7ykZtx8I0LtqKwyZmO2Y0b0c56IllJZHRK7fkKVvm3F_lp8mfzQ0ArRCriwe5uqZsa1-HQQz0955ZgG8QK_zazcql2W3iRA9iH8z8McRC65unNrZIWp29WLqcWqUZ4jB6j8SkkfskKSd00376YUSOXLUHhn7JRstLS7GJcswwOv_HrJq5pQ0rvc7yUb1Fx6zktMAHml070KsVphJec-e_XDNX6iEPfxyhzD6-9_4h0MJ8Aw8Kqz83hXAWp9SDr4rOf8taxsvjp37DLDfju1FLnvoREI2sm2PI90CogmdMYHYjid2iGHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: هدف اولیه جنگ، انتصاب محمود احمدی نژاد به عنوان رهبر ایران بود
🔹
بنا بر ادعای نیویورک تایمز، درباره این طرح با احمدی نژاد مشورت شده بود اما پس از مجروح شدن وی در حمله اسرائیل به خانه اش در تهران در روز آغازین جنگ، این موضوع آشکار شد. مقامات آمریکایی گفته اند که هدف از این اعتصاب رهایی او از حبس خانگی بوده است.
🔹
نیویوک تایمز مدعی شد: احمدی نژاد جان سالم به در برد اما پس از آن از تلاش برای تغییر، سرخورده شد و از آن زمان تاکنون در انظار عمومی دیده نشده است و محل نگهداری او مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/653152" target="_blank">📅 09:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کرمان امروز تعطیل شد
🔹
استانداری کرمان: به‌دلیل هجوم ریزگردها و آلودگی هوا، اداره‌ها و دستگاه‌های دولتی استان به استثنای مراکز امدای و خدماتی امروز تعطیل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/akhbarefori/653151" target="_blank">📅 08:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شی: جنگ علیه ایران باید متوقف شود
🔹
رئیس جمهور چین در دیدار خود با پوتین گفت مذاکرات بسیار مهم هستند و جنگ علیه ایران باید متوقف شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653150" target="_blank">📅 07:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-QHMAm_5efdK_hw8Dl-4QkIx483jgOM8_V4ujABcy3RxKAv4rsQysAa4LnN1zbVOoQXXWFqIR2lTOGFkeAPDUnl71TzHXauHZ3ioCKdYrtJRF7f5XabrqLd-Aw0OdyKWwph1tTI8NT0e6Xs1aH1j7SSdtzQbulw-BZhV4xyreL-ZzUh2C-yMT_1OCoLbxhCBAYWYCk_3Uw33JoBlTQhUr9iUu0iascob5w-5i9-uxou_pVQ6enXjnyfkUFscyjRDZmzp4WFQOSDE3jlUp3omZVH-vMIdgjIXVppSwzxTwdwElbV3cJlELbLlKpT2K3gqHP4B_eQPoBJT2EEnuSeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳۰ اردیبهشت ماه
۳ ذی‌الحجه ۱۴۴۷
۲۰ می ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653149" target="_blank">📅 07:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حکم قصاص قاتل الهه حسین‌نژاد اجرا شد
🔹
حکم قصاص قاتل الهه حسین‌نژاد، با درخواست اولیای دم و پس از طی تمامی مراحل قانونی و قضایی اجرا شد.
🔹
حکم قصاص قاتل الهه حسین‌نژاد با درخواست اولیای دم و پس از تایید حکم در دیوان عالی کشور به اجرا درآمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653148" target="_blank">📅 06:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzAgaJgmJ2iQHGAwGYAOi6bPFkUInjV8DsgKW8I4v6DFLfP5iq1ssRBdQiwHWPURSi3m7KJZc7IVcgCt9qy8VLmpKC_Vq42lb0UenIK4ALalt4o0-9-4VTiJ8-Rvsl-PQo6ZZhhJdUuaz8dPKs9VFSupr2TeEmygPR_IhWpDP8CnJom906cFbJyDuQBFuFfL2IaK8v1u46C2GIJPcZAitSGRR74vp2UvwCg9DZcVxC5xowgX-g7CZm74ImSIKL6RkvEuEICC6kQXExf5QXZube617FO3ODpdBN-9_hgM2OPYf2iyP4IwDSwUFywI-fMoVFlZxcdkRIZxt1dF37s6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار روسیه درباره انجام آزمایش هسته‌ای توسط دیگر کشورها
🔹
«سرگئی ریابکوف» معاون وزیر خارجه روسیه بامداد چهارشنبه گفت که روسیه به‌طور متناسب به انجام آزمایشات هسته‌ای توسط هر کشوری، واکنش نشان خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653147" target="_blank">📅 06:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWhpSqjgXYXHUXXGZrWVqpNJswpZfctwAIAGRF8gcF9U4zC9ZhGbvA_kJpqWHCe60_JHv5fkVyMeXAR7udD4sTFpJTVZnIi1yjAGCl-YVaEeV_dWWT_WgGA2KLbZtZ15bORaaRoiABQOWGL4mz_BlX55TBu5-smwPmNIfjHQ_bR5VHCmnfv3_gaKQYCi4-lP1-0q80N4VcMSuBvZnlTrhSH2a_d2L3orU4kMC1zaHW63Z5x6IWWouTypuzNAeS28SvnlKUiLtE1fGbt5NFfrAzjGuEkxc240AMi2fxCVMQlfKIW89f5JRQ_HpL9SB6Be32eTdppn0ruMHmC3bCjfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرباس هزینه‌های جانبی خود را به دلیل جنگ آمریکا علیه ایران کاهش می‌دهد
🔹
شرکت بزرگ هواپیمایی ایرباس به دلیل آشفتگی ناشی از جنگ آمریکا و اسرائیل علیه ایران، از نمایندگی های خود خواسته است که «هزینه‌های غیرضروری» را ۱۰ درصد کاهش دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653146" target="_blank">📅 04:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpIrxMgD0il5syVhivwdYE5OjonlusfZ_Dd_5mCCgLQU6y1XgdCUBzuUH009Xye4VqvZsJitIbUNXz50WJ6mBJc8YIrrgH8L1Xvr7amsS4su46Ak9wi3RYDUeGl7V0RlVqMCCeAMR1SLsRq1WMM4cljiO136XlY4Vt-XY3ptlhh7W48h5zLmfP_4lmp7ucIYFmfiPP0u4_s787Zo5da2D7gNZ8zKZVRfvjhKFGWqK9BwOYJUeQQo58KaYctS21k9A9yetObA8ZqRu6HQ_DtKqTircjEuqaW_wrI44kG2cYjKqwbdgnD8mw60Uk5DyFXLmdfnCmvHiTf6xUbdkP9yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام حماس: اسرائیل از ورود دارو به غزه جلوگیری می‌کند
🔹
مرداوی، عضو ارشد حماس: رژیم‌صهیونیستی به مفاد آتش‌بس در غزه پایبند نیست و اجازۀ بازسازی بیمارستان‌ها را نمی‌دهد.
🔹
بیشتر کسانی که توسط اشغالگران در غزه کشته شده‌اند، غیرنظامی هستند. اسرائیل به مفاد توافق پایبند نیست.
🔹
اشغالگران اجازۀ بازسازی بیمارستان‌ها یا ورود دارو و اسکان موقت به نوار غزه را نداده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653145" target="_blank">📅 03:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5SeezokOZngeo_xFfBTcjLwe3LdDkT5H12IywxfBwz7UnpJDr0Ig6mQqfFZ5d8YbR0H-gp9mHX7UU2GfXk_caIlG58abdfq4eq57zXBuIUDp1zLHlI8p0qC8sQ-oQ8R2kEggfUu_FTwC3jfvHtGNiTZNtl9qHTmTH80MRnCGSYoPJ_D7YY4TgHVfDgi41-JtUGxfLalUbbNyBG_hox4dm_6maBBMdO8WP92Gy7QeSl58tbzZDt1neklaiqbUwn-nE2ZxdTDc7quRfl3QPcgyaAq3EytAQ4U-jfK-qJQb0t6twvhwE3B74tw3kcDDvY8zTy60TnePIAttt5j1FRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید بقائی بر محاکمه و پاسخگویی آمران و عاملان جنایت میناب
🔹
سخنگوی وزارت امور خارجه بامداد امروز با بیان اینکه تقلای شرم‌آور آمریکا برای توجیه جنایت میناب نمی‌تواند ماهیت این جنایت را مخفی کند، گفت: فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653144" target="_blank">📅 02:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1yHQqYSoTG114XP_gCYYEVz1wtQte7-twwElrFHwswa3COo-mbRTm_qOVtKlFTp9OCvSFgXyxjW44obpjSBFB7LCAX8U9_I97c2O9FyjlzydtQGPzpGIJjFqesuB9dGA0oIKO5t7hF0xWEsYUcJE6DtlKHNsE0DJ4v7Nhk58dbilJNCvbMGOCsIPocrJKtM391cscxlLISWk1zDGQNY1ub8Av49v8n-i_iHZKLVKDKOGk5WMtA97dyiQ5M_hBsJ-B79JBEXIuuiMP3HzOCByYV0UB0FmNd9rgPbS4ells9dfYgoRy7zzGIG1xaKDQ-toBiWmmhmYCbhK26B9yYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایندگی جمهوری اسلامی ایران در سازمان ملل متحد: ایالات متحده آمریکا از شورای امنیت سازمان ملل برای انتشار دروغ و اتهامات نادرست علیه جمهوری اسلامی ایران و برنامه هسته ای آن سوءاستفاده می کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653143" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دستگیری مزدور موساد در شهر ری
🔹
دادستان شهرستان ری: یکی از عناصر مرتبط با سرویس جاسوسی رژیم صهیونیستی (موساد) در جنوب شهرستان ری، شناسایی و بازداشت شد.
🔹
هم‌اکنون روند رسیدگی به پرونده وی در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653142" target="_blank">📅 02:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQaCo8Cs-qqLIvzSPiPY1w8eEk9R6Ll6GNmCcwTZLUM7NstyjrmqaKzekTuqG093tk2XqHlDafC2JTs9-A87Jy6G2gKZCL6gCsWGLezARguZrzwZqpfg6HLrEPp5R0k_fdi-WMajWZwsVqNfxOuB8Dt7yZEciZ2fZh3S79Qyp9RWDXb28qgWm0RcVs-vuJ_xT7sYbJ0oazPrkhBqWKJnNA0H8MAhql1bPPqpxQ3TeV977khU2BDmi6xHm_UQcJqhYyGHwg2CXpBWMO2omKAOT8l_sG4k_Brc13J6ogxTrz3K2E-zTAt1LQo4ImwnM7biHn2vJ4Qp-3hf4jL2LRwtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران را، بعد از ۷ بار رد شدن، تصویب کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653141" target="_blank">📅 01:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKc9azQ3jRncEG1rFT-_T_yq9WyTqF4j1Ry75509hU3aJo3UdgN8BUXWncCadNNdLzkfJ3HaJEyrn1nISyILhn5X5l05cuUtpNoE5xaGs5HToIsOyPAjykvIetYsSrqn4QuYrpPpLMfv-BBH2KJG5pvOT7qY9nOr5nGltxLRAwo-iFUmZ5kTAz_1dCFxco4cumNsa9y5FAYulA2gp8rpYLX1Hv3HWf-Pv19ATyr3KFA7_t1_tAPSJmWtbtmE724OWL5cl5QwufDRHi7jIuYo_slLI53S-YXLXJ5KzHlWkOTDL1DNbB0q5tUK_c_Y6sbS1-tzUJOYArEuOKUr6IIBOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز از تصمیم ترامپ برای توقف حمایت نظامی آمریکا از اروپا خبر داد
🔹
ترامپ قصد دارد سهم توانمندی‌های نظامی خود را که برای کمک به متحدان اروپایی در زمان بحران‌های بزرگ در نظر گرفته شده، به شدت کاهش دهد.
🔹
پنتاگون تصمیم گرفته است تعهدات خود را در این زمینه به طور قابل توجهی کم کند و انتظار می‌رود این تصمیم روز جمعه طی نشست مقامات ارشد دفاعی ناتو در بروکسل اعلام رسمی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653140" target="_blank">📅 01:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkrLq4IgDMlQwdH2ZjbTEwTfG6la0K1vCDTZ_R_EI2GfJ-PjidyVxkixgzNitoqy4XnTOtGEYKy3J85gZuUgsuHN5DLwEtCMcWdtTpF110EoWMf8fepf-Uz6GP5tGpB8ZWbBjDiQHFcb7QtqTayjVBkHZD43kXUYCGx3aWlRFj4y3L0jk78-Sxv85ZFalp4-5clstZtsZrKSr2pjUWi-i8Su7tBCSiJKuml1uuaK-2qReqbXIlrnvBtddvRByGJXI3UnVMEk5kgWJ-1VErATrSHLDyapfuHfajdAg188FxfPBXUvFnb9LnsLzGKbXexcvpIsxQ0_XE8WVjoVe_YXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، ماهیت این جنایت را مخفی نمی‌کند
🔹
سخنگوی وزارت امور خارجه، در واکنش به ادعای فرماندهی مرکزی ایالات متحده آمریکا درباره دلیل هدف قرار دادن مدرسه شجره طیبه میناب و کشتار بیش از ۱۷۰ دانش‌آموز و معلم، نوشت:
🔹
ادعای فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) مبنی بر اینکه مدرسه ابتدایی شجره طیبه میناب در محدوده یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمانشان شد.
🔹
هدف قرار دادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشردوستانه بین‌المللی و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حمله فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی کاملاً پاسخگو و محاکمه شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653139" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzNKcjve1o5a6vksl3122v-SU_S0fJeSjNyCl_eyWP7u5f6dC0Kh7lRzioyyvQkTaPtOv9Nf-X9lHCYSjO5pXC8_LfCFulDAirUXjwIaCs_Qc3cje0tWfax8-4ckZLDeAsC9CRdDQtLM5CWsMj9h28vK1VjZTRFMyLncw2BaJt1OYPhYKhiw5Il7fD23DJ_x1DeKC0iRzCVtkBU8_flewUDfMm9EYyjeO-P8RwvujTvSmrZmkAy15PrhFzwzKcwXp1CsHTNKxdP_R-_2t3C_qO27YYPFYaFX7hePqVxk8__YE8WQpFuah28gli6Kxn1RkrWx6EF7WcVs2aGEB7t2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های زیادی همراه خواهد بود
🔹
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
🔹
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-۳۵ را سرنگون کردند.
🔹
با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/653138" target="_blank">📅 00:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df5fd590b.mp4?token=bAxdDFHC4eMKE9-tCvfpb_c7rYaODmBXYpfVs2pysbHZm-26p2hfQDIvrd-Wl_7uiTZYdtt3l7GlHA5-2i1e5HBLaUCB2Evwc7OSkUrLu6zJQHD1R9DtGeDp4QKxeo-F8pwXJi9IIt88D6fkn9iu2bGuv5VrLALKGKFozJ7Hdm-rtXyjDdXEBPttvyLCtEzBu25NUf3C9IL0YzQOMZVkXJNm9apgGQztL0ZC3TeXMX6e9DRyYLLo1TFqxjoO9yex00ze0_td-TrGYE_IhqaHmf-cKCF5QaXdPBB_1HgdzpweExlBkee3I_lRkmiOk6Cwhg_qq08SLprjJa9oPSFqwD9MnfMQlO8DB7X6AgWJgyopOCKwCeSn35ePI8ayPk5JnASMaYVou3YIpiGQMKyLctVGDJL8b8Wf4xSmTo8Cg6anlu5EBXZvgnsu5mR3Il22Amt-9H8azvICkt_xaNdfNcyT6froYIxTEyr-rKP0lqemGrgInxeakruX6Ez6YyBOLRn4YF81CM5ztG5yd3lE1Qv6fqUU8giEM_P312W1KuAkbhrlwMMqFZ0hEzGpZwwbKTieZXm6NCq8ZUGfwYt9fENfY3GJ6LOhiQyMHZYWBPyOOGQJah8Y1wDitLiBtNUFhz2WKsGj4p7GQhssyAtG_LRsXtcb4Y5cEkL6ikvov1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده مجلس: تثبیت تنگه هرمز به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، در جنگ اتفاق افتاده
🔹
روح‌الله متفکرآزاد، عضو هیات‌ رئیسه مجلس: تنگه هرمز آب‌های استراتژیک ملی ماست. به همت شهید تنگسیری و رزمندگان عزیز ما، با تدابیر مقام معظم رهبری، تثبیت این تنگه در جنگ اتفاق افتاده.
🔹
ما تنگه را بسته نگه نخواهیم داشت. موضوع، موضوع حکمرانی ماست که باید تثبیت بشود.
🔹
هرکجا نیاز شد برویم به سمت سیاست‌گذاری اجرایی آن هم شعام، هم مجلس با تمام قوا انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/653137" target="_blank">📅 00:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
۱۰ شهید در تجاوز صهیونیست‌ها به شهر صور لبنان
🔹
وزارت بهداشت لبنان: در حمله هوایی رژیم صهیونیستی به دیر قانون النهر در شهرستان صور در جنوب لبنان بر اساس امار اولیه و غیرنهایی، دست کم ۱۰ نفر از جمله سه کودک و سه زن شهید و سه نفر از جمله یک کودک نیز زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/653136" target="_blank">📅 00:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGsX-udoAuOG5IiDVhxgU69OM68b7vEKhoPwMZZu0YLff2kZkhEL9CWFgWEGCBrQiTNCurm7QKivnSDlk4k14p3G84xtbMP1bIeo4yLkCfxPJP9kUU-NWMLT0Z1_xu8Gr1TRMI_NnKPVE4iBpMcQdRiqqwpA9NooXg-D-13bVMyCZ1SQwde1uSuptIc4IJSrc8DRt8usRpAp0XpmDmbEyHfDy9ly06anK1-Hv2rRw545fjYmodYjtAPEC6MYfb3Yg5SkqiC1TxYjem1pYO3Jzuy1EJPFlpWdkuemtW4orZZ-MjZqEDLmdnhboxAWFYDDCZjrP6rtXCZI4FWvkECrgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرسنال بعد از ۲۲ سال قهرمان لیگ برتر انگلیس شد
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3216390</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/653135" target="_blank">📅 00:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccca31dbb4.mp4?token=vlRy4XOPOuZAtsGU3Kvdja12gz1l7-HOBMnNmN_nnZ9lfy1UEyaoXQ8hDmTQ4ek-IvCqMWQPrmsbLA3uw7a1KE2doMnZeNjkiGh8D1PWUp6lAPtXVt21wY52so3yRv1gGf3zKxU0pwfB8Crz242LJmzFSvhgoYzQ9X740TZeSVd1GCMItglA-dV-2emj14zYugycbI3JXmTQdcvtxYZgSGuWvcUna6qOzFby8Rx7CfzD0jjFdfQyBoSXLu8_-HEfz7u-WyyJelljTf7cX4r8izWwxQV8PsNpgEkJ1OKAN7Wn3BdXuCRu1GJelSSygn6Fbd0NpcrIE2cCtlhs7UjToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسویه‌حساب پادشاه جوان ایرانی با امپراتوری عثمانی !
برای ادامه ویدئو
👇
https://youtu.be/rCuQWD1D_es?si=Cxi0mh-CjPIi0Nmk
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/653134" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653133">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
گزارش لحظه به لحظه از تحولات روابط ایران و آمریکا | شبکه ۱۲ اسرائیل: ترامپ تصمیم گرفته حمله کند!
👇
khabarfoori.com/fa/tiny/news-3216088
🔹
حقه کثیف ترامپ در اعلام تعلیق حمله به ایران | این عدد همه چیز را لو می دهد!
👇
khabarfoori.com/fa/tiny/news-3216090
🔹
نقشه پنهان اعراب برای ایران | پیشنهاد محرمانه عرب‌ها به چین | یک اتفاق غیرمنتظره در دو سه روز آتی!
👇
khabarfoori.com/fa/tiny/news-3216309
🔹
خبر محرمانه یک اسرائیلی برای حمله به تاسیسات هسته ای ایران | جنجال لو رفتن یک نقشه شوم | ماجرای حمله به اصفهان برای استخراج اورانیوم چیست؟
👇
khabarfoori.com/fa/tiny/news-3216091
🔹
جنجال رقص منشوری در خاکسپاری | هیاهوی دختر خواننده مشهور در مراسم عزاداری + فیلم
👇
khabarfoori.com/fa/tiny/news-3216016
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/653133" target="_blank">📅 23:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653132">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfcf97015.mp4?token=rfiGRb7rG63uXFT1QjFr6rZ72OFoHNuQzLM7g81rnX1AwNb7ulL1qRizg-Pp7qdFn2tooGmmW3v8ZvVZUKngRMz2iFmvR68QiVw3dzfPfdfBtWnYfoRktcCOdApJoyy3IxOGQ-kHnKIlhyg3WXXKW1X4AAzRRWAu_l_4MNSSv56FCcW4i6dVS2cSk9W2KQkCLyAiBuCMawvaV7WKC4XwQ55HgDbnSfM7azpX5O5S_tAJFYeC3aKzPb0jz31C9lWUqtCIdRPDc3ZbdwHwpBrcs6utRGMngRqTH7YCdGgBNinZKor-pEaevRuHuKqZs0OdI_r1TOEQJNCvX1Scc2Kmcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: وزیر امور خارجه ترکیه حد و حدود خود را بشناسد و بداند اجازه ندارد درباره جمهوری اسلامی ایران از کلمه باید استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653132" target="_blank">📅 23:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653131">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی از ارائه پیشنهاد تعیین سقف افزایش اجاره‌بها در هر استان و تمدید خودکار قرارداد‌ها به سران قوا خبر داد
🔹
رئیس دانشگاه تهران: ۷۰ سهمیه جذب هیأت علمی برای رشته‌های پیشران علم و فناوری مانند حوزه‌های هوش مصنوعی، کوانتوم و فوتونیک اختصاص یافت.
🔹
فرمانده انتظامی استان هرمزگان: هزار و ۸۲۰ تن برنج پاکستانی که در انبار اطراف اسکله شهید رجایی بندرعباس احتکار شده بود شناسایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/653131" target="_blank">📅 23:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
معاون توسعه روستایی رئیس‌جمهور: اینترنت به وضعیت گذشته بازخواهد گشت، زیرا دستور رئیس‌جمهور است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/653130" target="_blank">📅 23:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej01Pu_ZkFFrluyXfSNBfi_ou89I0dLEGFSGRIe30i3bF1iEc-iLmpCjlU3uireNWMWhTlfX1sjbbRhBOo1RGKJH8JdBGBxqTwASYmnKOzQI9L14PplsW8uG_4ZzHJFWtFMsX_CiaHB6Z-YcRZO9bh3vKpzicoohylSGiOvkF0W4-PXujkCSZ-b9rhJm-xMZH2jrVcmhIobDy_sTn9q3T5ATEMnfQSwoq71QQI_ue7QHHVPPxinqvTiBr-TrMnLwnYIP257DWzzgizmxKUj49mkl4wAjj1x91gVCHUl4bUFqu-YIMHaaVmTIKp7pDFf6CSmjcfsj5iyx9gBcGbaxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون بازرسی قرارگاه خاتم الانبیا (ص): در آستانه تحول تاریخی بزرگی هستیم
🔹
سردار اسدی: با تاکید بر اینکه امروز در انتهای یک پیچ بسیار مهم تاریخی قرار داریم، گفت: آنچه از همه چیز واجب‌تر و لازم‌تر است، حفظ وحدت مسلمین است، زیرا دشمن تمام توان خود را به کار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/653129" target="_blank">📅 23:40 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
