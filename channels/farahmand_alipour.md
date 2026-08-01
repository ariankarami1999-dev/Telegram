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
<img src="https://cdn4.telesco.pe/file/FHrwVQeSyqtCR93YVkuYd7flB8CQRru40Nac91PSieQhX-brh72P50l4SNLu_6OiH0xtwYf0QdPxp-946paGc2OG64HXVlFUxSXkoYF4j2oouTzC2qjkL8ueBfkkHwrRnkYCjPF79QgC1jLYnOBm18zFV-sazVmE7gLK56ozcJARgn4Bmg_P9NhgG7FPj4rPmSYTNPlOknJ4aj5M_vMUwUA3cc51no1FqgUMoSvvHgdWRb2HsoMkbTeEwAyqskNaPqayXNllQnh-XHX5plB-uDqoKf0-gMqIzqEVTWdPv4exJzEYr0edHoOEUUUZTU9DgjQVX2g5ScMMlNc9maLv1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 16:29:12</div>
<hr>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFDpCwGdY9T9XhVIDL27KEEoSl_tY55PTfVKFsEbvxS9xB2Cn2aqly56MTsBvWkd1Nj0_LeCoWjzFOK-rCo8MkxYA75v-FPBpPavzJFTt8F6IGxPzWek2cX66-rJ_YPj2FFBgN0oWejCFbhEF_cMU1yH4qQ3AkiBzZJXNcxISKIFBrExjY1LYAfcvlCx5UoBGMv57kCfuVXQSo8Xo9_fKPSpI0QPsqbyIG3744HKGv9kp6Z-PtJ-1auwc8qAP6KjAKYfKlB1Wd0T9rDDQacL6irn4Kc0nzwteDG9sSm3fN_QXt2nCvLOJQU5bbix4VXhMN0JE_TGZV0wsMPD9_622g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rX3MvzG-BF-wqyw8bOGifbjWwmCqpKTdQRmMIfi8buvYU0sWK207__xLEGE2lJnt7_t_Mq5XoksWCMpr8t20cFSPFfTk6ixgTfnlrwBPV_mmIF09AbB9NZ-De-ZoV9ipPhNoRE5UfJj7oIjAVTvCldijAljXvSafJVUSO2aPb5Xi4XCghwjTTPxQEqZzQZPDEggGD-PqXnnssEL6yJTDGmFG-lXcnuSCcEHPiId0bszvKUqmCpI_GULS_nqBXX2cgHLQ9ONp29MccDA4iCIztSE5vsJuKl_SVooAcGMI3qXOcvukXzRTU-Jew9Sh7LfqYNrBPSbwJI-jDJby_kfXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rX3MvzG-BF-wqyw8bOGifbjWwmCqpKTdQRmMIfi8buvYU0sWK207__xLEGE2lJnt7_t_Mq5XoksWCMpr8t20cFSPFfTk6ixgTfnlrwBPV_mmIF09AbB9NZ-De-ZoV9ipPhNoRE5UfJj7oIjAVTvCldijAljXvSafJVUSO2aPb5Xi4XCghwjTTPxQEqZzQZPDEggGD-PqXnnssEL6yJTDGmFG-lXcnuSCcEHPiId0bszvKUqmCpI_GULS_nqBXX2cgHLQ9ONp29MccDA4iCIztSE5vsJuKl_SVooAcGMI3qXOcvukXzRTU-Jew9Sh7LfqYNrBPSbwJI-jDJby_kfXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=ISbe4Hv1b2dWoPAXyuBsi-BGvahr08GIYhkslohTLdVeInOsYlxar8i1v7ZukaaOmubMdf5cOxJWFT7H_SwZ3RMsVrOwd0rFJ71-U1-VNHqghyQhoTYARxLmy_OZdVFLnji2a1_XEmucgLLugD-NhZMP78QMUfBW352qUTioVqqiuIz9GYU5_J3lmKePf9iJVUizcs9R3G_dr5CxfBYB_XsvQM6VIoaV9rfeCG4Bd-2aWIjdhwwg6pjhXInQSTg0eYZ9N9rin3ZCduYzX-BUO6YkKBqOI7j-o8QycvXNCxM1l0tXVl-ghejilAUW3VUvrbPXprt12EOJQzmEOk-DvGGMH4lV7rcbZwLYGvs4vq7CdLAr9Ig_a_zTqYVSJUh_eeEtZUDsytiuem8ZAI6_fUF3n5A4Hkvq9W36V6O_nchZazboTGUZ9AAhHUlHq7VGnYjZZ7MD0vLxeGpZRUdBFAoAUsdBxyes-oeKVTJ8ZlyMW5mtYBRwkJn3WI7bCTGg5gY3csWT6KbWZREx-lop2sGf-CwVoaXASQdQkBrC-95ZfYxGhhue6Gd38TF3b9gUc3HXQCrbKdSUQEeSl1mrx7osAVsLTMwt9NaEcrsfqbQ1hnsGyaaDtKuoUM-zmK_z7aMn1r9hvK93sjFN4UMiSy3HWCSqw-f8TsRpru0IAvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=ISbe4Hv1b2dWoPAXyuBsi-BGvahr08GIYhkslohTLdVeInOsYlxar8i1v7ZukaaOmubMdf5cOxJWFT7H_SwZ3RMsVrOwd0rFJ71-U1-VNHqghyQhoTYARxLmy_OZdVFLnji2a1_XEmucgLLugD-NhZMP78QMUfBW352qUTioVqqiuIz9GYU5_J3lmKePf9iJVUizcs9R3G_dr5CxfBYB_XsvQM6VIoaV9rfeCG4Bd-2aWIjdhwwg6pjhXInQSTg0eYZ9N9rin3ZCduYzX-BUO6YkKBqOI7j-o8QycvXNCxM1l0tXVl-ghejilAUW3VUvrbPXprt12EOJQzmEOk-DvGGMH4lV7rcbZwLYGvs4vq7CdLAr9Ig_a_zTqYVSJUh_eeEtZUDsytiuem8ZAI6_fUF3n5A4Hkvq9W36V6O_nchZazboTGUZ9AAhHUlHq7VGnYjZZ7MD0vLxeGpZRUdBFAoAUsdBxyes-oeKVTJ8ZlyMW5mtYBRwkJn3WI7bCTGg5gY3csWT6KbWZREx-lop2sGf-CwVoaXASQdQkBrC-95ZfYxGhhue6Gd38TF3b9gUc3HXQCrbKdSUQEeSl1mrx7osAVsLTMwt9NaEcrsfqbQ1hnsGyaaDtKuoUM-zmK_z7aMn1r9hvK93sjFN4UMiSy3HWCSqw-f8TsRpru0IAvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=QpFoXlMjYmQ31pwklzVMY2Spl5qIUCuNU4VSCj951MPOuHxt4chOxvnl4u5MTsuYf8wKvbFAkjZfu0FBZKvzmr1bQozKP2pQHdbkSCEaUURZvj4t7Ii5x0iNF1uLtN6JKRNER1UBxL2-KuOnfgt3YI65SLsYKX-q1bD0y-iacnnVP25bgkk_VAshmUMSjW2Nw0igKbjTP7c_Ua3nqRXw8MNFlb_6efs_ybfQfS-jdhMG_tsv-LGCbTgZeqn-VRWIIjWgZVAHjet2l5rpHp5YBHOXTlBURxHUO-Hl3P8lXCE4Thn8iVd64IiJu3e7UX8qAxJCwIJD-dg3bJSUBqZBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=QpFoXlMjYmQ31pwklzVMY2Spl5qIUCuNU4VSCj951MPOuHxt4chOxvnl4u5MTsuYf8wKvbFAkjZfu0FBZKvzmr1bQozKP2pQHdbkSCEaUURZvj4t7Ii5x0iNF1uLtN6JKRNER1UBxL2-KuOnfgt3YI65SLsYKX-q1bD0y-iacnnVP25bgkk_VAshmUMSjW2Nw0igKbjTP7c_Ua3nqRXw8MNFlb_6efs_ybfQfS-jdhMG_tsv-LGCbTgZeqn-VRWIIjWgZVAHjet2l5rpHp5YBHOXTlBURxHUO-Hl3P8lXCE4Thn8iVd64IiJu3e7UX8qAxJCwIJD-dg3bJSUBqZBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viLmwIkYLotg_1IHyMSyTrS52nW6kAyKtm9pWbBu0f7ZmLGpi1u2kv90OciAH3XdnLMg9QuTwyoRAP0npodHVy1506RvIvuqhQ0fMqHBp7vm_sajbo-7uKBUl-8c5fQ6xg9M5I09QRbnxpKwoR5wFUVyAYfkf9aJ6y91AJd86nmuLywnOy7n_ImWXhVWz5WXMVXgQjzHpS9D-I5FRnPDuiU8yKnvrjzKiDl7jCirDWqce2od3LuACIqU5CnkelQodPAV34WJVAiHrg7FT2Lakom-uXCgDW-xkN8YCrTmEKlEatoM13C4dZnFclHxICQPHfWOx8rJPNUL8M3htgN9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvndpTIEke6t2gzgrxWq__-6MEjmDv79NwSPuGMXNM533bzbaGYwW4YKLQSuaxHDKnHVEmn9pGv74eFDqe10o6XbF8uzacI0bOAdMTiWwOql3HjjvuHsCqo5mfbq8lYZG8pr33sfHJMswsqThCZM5biToBL2s3lMvLSIOqzP2uz4gJPPHi7mSHPgLX3wz4eLb6EluV03aFQeqqcLDcLhsrXWPxI2lVWIV1Jo7EBgxlaRGhStzlXFSeHvPVayLYRDlCbAf0hvIgXIX55pzA1r34ua8GkP1sJPmt38g3nw-roe6UTxcASdd1eFfoHlcuhJNZ74j5Hn2meLGveoFMICWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=X5q4T-9SLG0J0OKOMAe3ODROFf3MABE4LX0bnFXPAn61p2kEopUiQf3VvnLt540j_8EBjBAjn2W9yyXzxGxVYltqR9F8GG2N3nTrR8BHnkPloWFnAPgmVpmPxZKmWdJPAKMOz_-wbK1_o3NYrKsbF_1SnUzvpBz6LjlSCHs6W8pNCfMtkuFyrnbFMDiuTe9mNg1QKLmySv860Zk7mTmRRlRJde1bvlTh0rlMhUkoGRtvrrvjXgO5y68MDvnmyfbNnEY9z7i8WE2sWRj4lM2EFvsdepPcGXSSQaJOyPkTsxOHb6_m7vHi8C2bNhfCJ8XhBDQ8whykQvuTlp6N1I30eTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=X5q4T-9SLG0J0OKOMAe3ODROFf3MABE4LX0bnFXPAn61p2kEopUiQf3VvnLt540j_8EBjBAjn2W9yyXzxGxVYltqR9F8GG2N3nTrR8BHnkPloWFnAPgmVpmPxZKmWdJPAKMOz_-wbK1_o3NYrKsbF_1SnUzvpBz6LjlSCHs6W8pNCfMtkuFyrnbFMDiuTe9mNg1QKLmySv860Zk7mTmRRlRJde1bvlTh0rlMhUkoGRtvrrvjXgO5y68MDvnmyfbNnEY9z7i8WE2sWRj4lM2EFvsdepPcGXSSQaJOyPkTsxOHb6_m7vHi8C2bNhfCJ8XhBDQ8whykQvuTlp6N1I30eTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIPgGiBPcvEpsv3sg17gXYd_8Uj2zCfgKARl_Ra638BKQ1pXyUQ2HUs9p6jFDy2CTvaAYbNe1TOCZZ9ieYfO-7I2DUZBsTMELOy3O11cDieNR1X0NNgYebwnHJvkkHBmnUK91rxcm57MCUCxZc_VsYTbifqa4-GEpQEmUmOQFf1t-GPqgTN7CQLyWNTCTnZd1fNl-MihK2yWmWs64uQEZh5AoLP93RDE44eDKYmPGqm2KU0gx-3i1gbhs6a3KAaugI1tcqmZZKjE1DI3Rf2TbiDtUUbRdKQN43mL8mPEHaCmR9IXOvvDQ8TlrqyB-Jf2tG5CSJQ1fbAoTXbLEd1KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0znLHUso5RfzuDl_Gi8Xz-Cdxb6_lhLt5I8ikMD30an-cCjXVYlKvFL_2-kfDj2H5Vj4PYvnxhrdAMC5_Htmd3OX1U3mth5_i1TNrjECnRUuI7vVIAm6S3Oykh9KMXY5Jvh-LS997gFtZr7b8NxfE2wQ1ToaaL3e5-AaeSLuUF-0bDceWCwIIDB8Ss80VcJZ2NkX6gjiHb97GZVIaH3vAPd1GpF72b4H3re0lL1dEYZMg6k1BGVLDQsPnFQikcPP7QGR2xxnWI3HSWJapdl5IXgElnjTnML44uMJ1XCdGQUeBIzcyWdufjtIeIyURR4IKNwyTJA3On_Q1-Msr0otw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHrLsKQ28-dHKvWN0jOJxzksWGz_boHoaaLpurDkR68mjACnluOD02neUE8WkslcgfEkMXvIZnDbm_9FibnBO5LsOGH70LkE5jVJ8mSBQ3S-b55G5oAEXDXx-8wgWPy2gTuNSuDpYIUphMlBRmXez1pCp9nH6PghUy-KdXHSJ_B9x-zO3JGgc_ygbNIVq7YDPW0DZ5BISr79sh2wI7ynBIi4UoTwWxYWhQnCtHlVNHwo_IdYMYZfUsSQj7DRYFH8k3p9XMKvp2n6cxTMxbsdPw6kSXBn6m-ZzOnxHql1QhgP6VNR5dQMf2Dy2j872V4QdeXC6mRjtntEIBfWSNnmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV70PalbBga7dD4nJChC48W8L6tqK908cMRwQoutFC7wsWSAFCpimUPprq3vh3zaafIJg-WtpIgBCsYu3VPMe__t41pFFMda7Z2wnjh9Ywu1l2K9Btev7F0mSuenPMrMUAOt98dBY9FkWkxDQ_Yb6SkEAM29cP2qemcpv3HkCmmjHUHXrTakNmVqMtRZHvMZ0pNKmcwateNWTHF2Z2xNYG1gmSMs12G-QAF3WbZPLcagRCidzkH5X1Qao-nYuKfTsK8i72Z7oQxxTVDqQPCmmHdthXBxlb6Op1Qx659gGOSqkP1EjK9wgtcwZ-CDKv59Df3MdrF8GUy5OdJ-gh4sTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU1wg_mtEm-nXhV72qY--uxOpFfGHjbJYh9mP9jawwtRHVMjYiI5xL7us33mBvHjFmqUuKaRpX4iXCcrMK9IrIRqnKQppfnlMAE28d_UoSpkA2z9XKK0V7jU_zCDibibJnfsjt5yKnHLaolj1BHRleIILg0GRj5_BLpNEMM_2fEwszgzcas6LBwbfWhuQ44towJYaOYRspuIPI1r6P0OTeaQgr-JPasegO8m43gajYGCFkDP1wmX4ujrDhh5O7vtTK9LsqsWGlmpvOV0GYoByEXlKMVFMemffljiByAjwAdg_v-bLqbTkrQhCD63mILszL2nsLVD0tlmng6hyBbC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=IG81s3RiW0JX8b6zR3vMVluZoVFokz1nDaEERo7NeszxoJvpKOf4ia9LuTFsLIIc2iPmKpfGxu28jaingcnsFqMJmmmkbhgSTgiH8LPTnPtQjNtVEUz5DWdXgdC1Mc9COqGbnXQU0Oq-nK0V-35n-_MOyMTJnqgD1kA2rtgFEu-Ehbjwd_kLf8IGEViFNIujpWmxOyAwFUCmokDHH4JPo5akZzYiF4WWqA4l8mnuR25frIsYjScdblhnJ695l71-tFffpnxigHH4eTE049_hBGgu4Yai-3ZyioIgSylZAxQtXBoZVenoY0j5bvConJD7reXxevybQQFXY2zrvS9dlZwsRLGJ3qJdbcjSCJCNDkvjU-asn_ueIHoVvujuzha6nuAi96ZBS5eZ0GNffRB5-qxaaCe8aXaoSz1m7EdSOMwWOdCwPRyXe_BjJS7UyBQrscRkrgt_hyRPTLnRsTKKeeC3Lp3XTh5yO3TKAAQ5MeGqXD6RjVQW0LViB5SOHQHFv3hq4r_i5GX8M5Tn-oo7n1VVnHBr3SwxwBCOMXXbv4eXqYjUCEu0uY33vEO4V1xj-Jb5jmofqR1cfmcxIs_nZ5r1uMIDPmZmuKFTY5J0uxuJxVFSr9yZcWmvHGsiNJg13W4Ra8kVKomEOysTlGtuxEvpqjsBaehN8oztb0Rh8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=IG81s3RiW0JX8b6zR3vMVluZoVFokz1nDaEERo7NeszxoJvpKOf4ia9LuTFsLIIc2iPmKpfGxu28jaingcnsFqMJmmmkbhgSTgiH8LPTnPtQjNtVEUz5DWdXgdC1Mc9COqGbnXQU0Oq-nK0V-35n-_MOyMTJnqgD1kA2rtgFEu-Ehbjwd_kLf8IGEViFNIujpWmxOyAwFUCmokDHH4JPo5akZzYiF4WWqA4l8mnuR25frIsYjScdblhnJ695l71-tFffpnxigHH4eTE049_hBGgu4Yai-3ZyioIgSylZAxQtXBoZVenoY0j5bvConJD7reXxevybQQFXY2zrvS9dlZwsRLGJ3qJdbcjSCJCNDkvjU-asn_ueIHoVvujuzha6nuAi96ZBS5eZ0GNffRB5-qxaaCe8aXaoSz1m7EdSOMwWOdCwPRyXe_BjJS7UyBQrscRkrgt_hyRPTLnRsTKKeeC3Lp3XTh5yO3TKAAQ5MeGqXD6RjVQW0LViB5SOHQHFv3hq4r_i5GX8M5Tn-oo7n1VVnHBr3SwxwBCOMXXbv4eXqYjUCEu0uY33vEO4V1xj-Jb5jmofqR1cfmcxIs_nZ5r1uMIDPmZmuKFTY5J0uxuJxVFSr9yZcWmvHGsiNJg13W4Ra8kVKomEOysTlGtuxEvpqjsBaehN8oztb0Rh8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKiCwUuovxj-UV6RvcEDOZBqsLrSThYZ4mZR6qeECtXjL8Lq7HQaPoVdOB7JfKzrXURLsWj_oi4p7f4bDMsnmce2Jd-789gBHMMXuq6Dk5uNNE4GO9iD23V19YNRXfXifAbHya0Y9CxUa_mQguaNmqKR1mQFLrzgHnFjQUIjiSa1cemE5JerO9Oqq2CTucqA1TJqKmYgrGAjwULiFWfC8myctTa4AqpL0CdLTjBeI4ABA45xt-ACD_t5hdoxfxDXQ7BoBk1rzn2R8KX_ZS7ncxGQPQGYXvcg3vZ6TFePRkVjfihWIh9J8MBg2x1ORk4AWex7D0CkbuAhTcrm4H0a4o4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKiCwUuovxj-UV6RvcEDOZBqsLrSThYZ4mZR6qeECtXjL8Lq7HQaPoVdOB7JfKzrXURLsWj_oi4p7f4bDMsnmce2Jd-789gBHMMXuq6Dk5uNNE4GO9iD23V19YNRXfXifAbHya0Y9CxUa_mQguaNmqKR1mQFLrzgHnFjQUIjiSa1cemE5JerO9Oqq2CTucqA1TJqKmYgrGAjwULiFWfC8myctTa4AqpL0CdLTjBeI4ABA45xt-ACD_t5hdoxfxDXQ7BoBk1rzn2R8KX_ZS7ncxGQPQGYXvcg3vZ6TFePRkVjfihWIh9J8MBg2x1ORk4AWex7D0CkbuAhTcrm4H0a4o4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Q-HZXHBPtxFVt6ATnMNgCkAaarR8BxK2CTZse-VpwmNpwyLSLzVzIM02PskWe0G6MXtevRpFL0J1wAqN8TWr0bUt1gdPVB8_nZq9WN0gqNlNlsoAJ4NBu4MgEO6g3NhMJmwlqShCR2COAkMaTl1ZUqc5bMzUz2rfRgeEuaU7Dtovo5CUBnyT0213cLCN7-A9jIu0wpLqXF0tpeM6og1h2TADq66o4RlzdWCN0Y0eGSsgYgANkZ8ddqdvpttrf6arO3H3gJ85_-reeYowACxaB2D5YLUZhAR3oCF8WCluEG8TVuBBj0cNU4xlbVqWRXwg_BDKl1XtuqcAedZC6_vYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Q-HZXHBPtxFVt6ATnMNgCkAaarR8BxK2CTZse-VpwmNpwyLSLzVzIM02PskWe0G6MXtevRpFL0J1wAqN8TWr0bUt1gdPVB8_nZq9WN0gqNlNlsoAJ4NBu4MgEO6g3NhMJmwlqShCR2COAkMaTl1ZUqc5bMzUz2rfRgeEuaU7Dtovo5CUBnyT0213cLCN7-A9jIu0wpLqXF0tpeM6og1h2TADq66o4RlzdWCN0Y0eGSsgYgANkZ8ddqdvpttrf6arO3H3gJ85_-reeYowACxaB2D5YLUZhAR3oCF8WCluEG8TVuBBj0cNU4xlbVqWRXwg_BDKl1XtuqcAedZC6_vYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9MGay7ngcw3nFsSNOuIlt6RxcxvLEENIf4uJ3m6NJVGdmbMSSSZJ9gvgPXAgDl8BYLwTzIPrh91qSKq7aOMcxYF9BNQLrzIpSfQVvRtmoKK2QwuJUUwMJvu9mrYJTzlgZytrRyrNmwXxsQY3Ze5M-5kRYj2u498iOlbRZtd5zbCQK_QZMtRwbGFGC_C4lQgzLPVYzqZwpsNKwFoxgosQbO4R-rTjCe0YoHitbpMB_1kBYNNYgRdDdJF3wLvbgwdE3tl4NFsPmyofs6qsM2Mr0OwEnjQ8om_IEKAy1eIAh_KaRQrjcG_TtV6MpTcJJAyLnL5iTO-dfqyg_61FQftZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn9sstjSKzeIVa9TdIqBaJ8fX8XPLWHWFybvntNO4xeYm5i-d8uy0dW65ucB8Gs8QRJ_HYmzq8-G1aXpvjE1Ij60POtwoRBSPpIv3Zj038AvAQ-iHxEeDKMwuxPNAw98rjz9I3SKA2Aay3PvB9XlgAiSyCNh-vBpl-83gdgu283WXMNUeEMIs8WcgXK8rckhCvWhs4HcfZ1A23deMbjuYOhdbx3d1i7FNrhp7kPwQBT4TqT7kWzSv3tieYbfuqfMeB9k6gAHLB5ve4Cos9wCW23_CacYIIG-hGyEtxf07dYCBRd-wzc7ov02LemM6ZXESarIqvVZTvXS3jI7Fi_qVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=hEUghzu7n1VQK6nR7v7FnV_q-F3tZZk6T3ECwwRFy-RwWKblXmbeOLyyDNUhL7TkMlGNW7OB8Pc-IYSD_oIUnJT8qN02Sh8DoDFqKUK2u9m757Maw3g3xSkmy4xgUfVBasmm6CrrevtGDBcOGJ5ZlQY3g0OvC_9TqanK_66GYkK4c6aqvqnmz-C4Zj1SR49pggiAWQ9Y9bqldRR3YN6XZbHL8Bj5z3Pu0JLrfc53YmFcYfmQiudX7lNlKIaCHtOQhcftCsE8F-A0BtCsqA-qGqjPdW1d-RzqICT7pwmzuuq6hq5sFhUZE1jBddmZzqOgY0ANgglNE_h6TBk7dZHw9RlNFg1b9xEXD-aLpw5UwPPoi9KOypQd0atN4ZDBqcUo-qkghYW4rwqcSzx1hAcHqyNuS7rPnUoFSn6PNmatCrdi0mBYVpnzw3tJEU8zFRr_K959HoF2Ihz2eGsFWjLzLinOHAt_iVfHW0ByipRsftodoSEDGcKqxDbruOCalT6C1btv4FMGvOy6SzjvimWc5PMjvIuYkTpVj0n6rU2M7qQh8kIfpYM20EpyGVhzCXDibLzh207YbmAq5_etalN760e0fxDPf8VcVhXZIT-GuVNHtiNRFubKMfwhhN_7w4wLKWam4ymgKk47lGDL5TvBbFIRDR45NM5prg8NpL-l1ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=hEUghzu7n1VQK6nR7v7FnV_q-F3tZZk6T3ECwwRFy-RwWKblXmbeOLyyDNUhL7TkMlGNW7OB8Pc-IYSD_oIUnJT8qN02Sh8DoDFqKUK2u9m757Maw3g3xSkmy4xgUfVBasmm6CrrevtGDBcOGJ5ZlQY3g0OvC_9TqanK_66GYkK4c6aqvqnmz-C4Zj1SR49pggiAWQ9Y9bqldRR3YN6XZbHL8Bj5z3Pu0JLrfc53YmFcYfmQiudX7lNlKIaCHtOQhcftCsE8F-A0BtCsqA-qGqjPdW1d-RzqICT7pwmzuuq6hq5sFhUZE1jBddmZzqOgY0ANgglNE_h6TBk7dZHw9RlNFg1b9xEXD-aLpw5UwPPoi9KOypQd0atN4ZDBqcUo-qkghYW4rwqcSzx1hAcHqyNuS7rPnUoFSn6PNmatCrdi0mBYVpnzw3tJEU8zFRr_K959HoF2Ihz2eGsFWjLzLinOHAt_iVfHW0ByipRsftodoSEDGcKqxDbruOCalT6C1btv4FMGvOy6SzjvimWc5PMjvIuYkTpVj0n6rU2M7qQh8kIfpYM20EpyGVhzCXDibLzh207YbmAq5_etalN760e0fxDPf8VcVhXZIT-GuVNHtiNRFubKMfwhhN_7w4wLKWam4ymgKk47lGDL5TvBbFIRDR45NM5prg8NpL-l1ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=UQ8PQEwHeZwJMm_GX7u6AIddGQV3c3M4RXeqTCJ0AQZQ9fK6hxnOf9v2CilSdn-X5y6c2aV_Wxap2HdRBcDq7C83F17_O6t5wNyf1yiA9Ilo6n5bMcB6jMpyn6lEYXxuphLz62PCGDWpHQHRXScJv3tSjd9wQDgOms6LqfQpKctMENQPS2YvDP2dNJz_xPne_FNhVDelx3jDIlcWM6eGL0P4PDxkb_RyH_ARPH02IgFT_2oiZvuhkoOozTUk6wh5nXu-Xld45P0asQt5vldlX3Na6I-I1S9ibpuBhVpK-5M-_T5q5d21sc8YH0AQpQCcM_Hc1ySfrbKrsD6dec5O8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=UQ8PQEwHeZwJMm_GX7u6AIddGQV3c3M4RXeqTCJ0AQZQ9fK6hxnOf9v2CilSdn-X5y6c2aV_Wxap2HdRBcDq7C83F17_O6t5wNyf1yiA9Ilo6n5bMcB6jMpyn6lEYXxuphLz62PCGDWpHQHRXScJv3tSjd9wQDgOms6LqfQpKctMENQPS2YvDP2dNJz_xPne_FNhVDelx3jDIlcWM6eGL0P4PDxkb_RyH_ARPH02IgFT_2oiZvuhkoOozTUk6wh5nXu-Xld45P0asQt5vldlX3Na6I-I1S9ibpuBhVpK-5M-_T5q5d21sc8YH0AQpQCcM_Hc1ySfrbKrsD6dec5O8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFnBwz2KyG_vWTj3EMsSfIomx95Yv4wXSc5ptCbADOC3Hn5EY4ofnaRnv928H9e_4ZyTAUYi6bIqrqMA9S7ta5y0-_hRJOr5_C5CPAg055rTI7rd8Xfy8Mv1P118Lqs7W0Qp9urpD7j1R7F2MqYw_M-jsIjLRUG16AUcjQqphrGsM2E2aV0Mmc_zLRSpSyMg8Rbwa-GS2J0rA-Nzq6_Hr89xAoUoxqrrxwhv__lff_nHGofOGmTOhFuv9E6sOHcy37DAlnvmpCw2gai7Wd5pAD3-_BIfn3xI5u9_MkGe6suoQgmqMt0_w2UQJK-Wk0kO1JyH0-vXoSg83cy1z1THJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snYy30d4wuRPqKGnbZH3B23wRSN_9yw91QIW2V_pOorrJ1bOiV5Wh6foVSvTjkYWwslQKOthBmnTHEVCRjOHpfO9eeypJroz7SqtGiS1FB0MMcDKBoH-MS6UzlxXWKXE_xCtpwS_AOkpDTlYYu7UR8JX6l-rkp5aR2k_OJ1C50TP_BWdcte5JSIlRMbH78ZLpXIranS7Z4seBkKgJUL2_wUTkaMOqPA22Ot_L3alMP6--MpOJ6MawPQDIbLVtLFukIv5VtVei4ddrKzmkwnwQ3uBr-RlBTgwAEk_B9ZG5BBhZW6__dzMlr3xwbp42WjlkFtMKNQSChzAHjN7bUUcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=uJtGVFlYfnOprApangX0FuBPqi304TsXBsL0zYz7H1Z88wacLqyIwOlK4FJEVEe0z9LTblIXK-FRPzTqY7N02wtox8bePNE4kCecJsz1y1czCArcYnh-KjJSLHAN_4Jela0Hz9oVOJsRJ1vt3b4gKeKQ9EF9D7LMgt3wmNUS-dLnzPC902ZXC48x85v4RDQ1Av5YyZHkMaDXRlr1Zg2u9mmMaUKDdyhkWJo7lwIMSnYeNhsOljPUxZuxzcHO55RGRoR4vczOT8nRhUzSugTXgWW-AcHonrweGEzv7AqP6lU2cF49j_h9mLmBg5mAO7KOctkfUgM-mEKRFr-ouXdbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=uJtGVFlYfnOprApangX0FuBPqi304TsXBsL0zYz7H1Z88wacLqyIwOlK4FJEVEe0z9LTblIXK-FRPzTqY7N02wtox8bePNE4kCecJsz1y1czCArcYnh-KjJSLHAN_4Jela0Hz9oVOJsRJ1vt3b4gKeKQ9EF9D7LMgt3wmNUS-dLnzPC902ZXC48x85v4RDQ1Av5YyZHkMaDXRlr1Zg2u9mmMaUKDdyhkWJo7lwIMSnYeNhsOljPUxZuxzcHO55RGRoR4vczOT8nRhUzSugTXgWW-AcHonrweGEzv7AqP6lU2cF49j_h9mLmBg5mAO7KOctkfUgM-mEKRFr-ouXdbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=sebD97NwLtTDcLkWg0PcbSfCoKCnAL3gBXshmBw1-5llkaryG8ss8vJP9_qZmwB17J4OzDLNtp-x262AomgIGTEJqj2SXK3McSf6_tm0mNuwRGTG8B_qWtvoMYVX_knQNhKdND5EmcfIIaXpjkUieY78T-ffJf6tQXJk2AJwzFd_1BptmUGPT9r_PbWaI_mkBCkh5MAz28cVngrbvwB838Uj_KcZJ2cazjJ4mQ7O0n_hPyuQRYyEK1MIS7IdEmYjWq0tFM3cI6kaLpAiNtUkli6pCwUw6CFGqaMr6k9VPCpYGhI8kOG-O4v2wemdGGex7E1cQd725sYc8fKVXZTsaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=sebD97NwLtTDcLkWg0PcbSfCoKCnAL3gBXshmBw1-5llkaryG8ss8vJP9_qZmwB17J4OzDLNtp-x262AomgIGTEJqj2SXK3McSf6_tm0mNuwRGTG8B_qWtvoMYVX_knQNhKdND5EmcfIIaXpjkUieY78T-ffJf6tQXJk2AJwzFd_1BptmUGPT9r_PbWaI_mkBCkh5MAz28cVngrbvwB838Uj_KcZJ2cazjJ4mQ7O0n_hPyuQRYyEK1MIS7IdEmYjWq0tFM3cI6kaLpAiNtUkli6pCwUw6CFGqaMr6k9VPCpYGhI8kOG-O4v2wemdGGex7E1cQd725sYc8fKVXZTsaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX7pN6gg_yceLcMAIOs1UL3vyRnxu0Hv1S6oyOAefmlE0MucxIXrWpcDBxYxqfiO-y4C9wAgr0MaPJOGm4UWfgcWhknI0JytTFOONFqA4ALhpyczlM1XjLSa0k-522aBTUtVQX2GXbqgdemfcQqLGd7nqBZvQubR7sicfvK2KYC5JHk_qvhs7zWvEhPyRU1wSvmbuNH4AjIEwfmZlKSGU6LfxRf9HRdz5JlcOD3mmdoa6YhyGXr1GP3CTaSXf6K8-HdXo2M_GDJQiXS_KItSLSxydjZYbVXLuOfIwIei2qkRpRsrpCyOFcW2xcZNuI7YcFjkj49iKjQ4-RdQH33RLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5sHJr4_mazeQTOmYnjh_5cTGaNO_Yy1wAnoL6DDU_IxS01-_0QMmeBCdOukJLEZA2UCdiK19qHvimZ_A_PT2qhYkbX6N2AqgnIgdr4y95MckxnbKPGZ4Yv-ekI_-hGOiBFcnkQuolEc3HBhVDs9SnEHyPRE49XchuwL5UjI908Py6wrgeOHus-f8z6hjitRqJt1Flonrh4KPCcaUuVIQV1H_WOrnuGIRZUuZjjUS3HxNhdwps2nkHk1TFL5__yvfUv254ugwak8d7c-ZlMNLAzEGGP-7owGwnTbx9SiBxfVhyzbN6dZe6kcm2UrS9xOlD0-1o5HI5Ky_9Csu46Irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BKp9lQUIM7PbFrtiaegrfkBhMzFxuQAOUVYoS9-wWDTMFkV5SpifTl2WN2lk0yPaLDQhURFybPqnbhJyA-fbxxs2bzPZ8kjTuadaFYYM1JeQMIwZWm0UyqWLcTIhgYu0jqw_oYvHOw27fq66m1rbDpVZiqRrZPpU4Cd8D-wzmk_RxYW57Zrfm4Q_bGZmmfoemf7BqtL8NMqSHB0zzr39kuNmhohxJrQ4aFFrW_aDIcel0SEWdsVe3owZm3EJRaZ09xNR4HYEL3DK_pX2CGoqfwguB0wonHfo9ft4F4zXgbR5vaHLnQzBtck32Ct6MachAkUxBIdXHPIt8ktggJLjxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BKp9lQUIM7PbFrtiaegrfkBhMzFxuQAOUVYoS9-wWDTMFkV5SpifTl2WN2lk0yPaLDQhURFybPqnbhJyA-fbxxs2bzPZ8kjTuadaFYYM1JeQMIwZWm0UyqWLcTIhgYu0jqw_oYvHOw27fq66m1rbDpVZiqRrZPpU4Cd8D-wzmk_RxYW57Zrfm4Q_bGZmmfoemf7BqtL8NMqSHB0zzr39kuNmhohxJrQ4aFFrW_aDIcel0SEWdsVe3owZm3EJRaZ09xNR4HYEL3DK_pX2CGoqfwguB0wonHfo9ft4F4zXgbR5vaHLnQzBtck32Ct6MachAkUxBIdXHPIt8ktggJLjxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKGuwnJ6CNJnzD4U9QkIRHa6TDB7JkjX64hRMnU1m-q-8DzRFbMH-BFM0Lfcd99Wnk-V3JYKdapAs_Y7PGOql9yWJpMT6UaL_k2bG5vXtqYOPq8J0aUiKiX2PVHrrzWPISk47H00WelfHxGXfLozsvUYfDKKMTdz7uEGzwGawFcsC6T7QqSX3FXhNGu1b9ihpuidjKybWu2BFyb3gLGP-mIUqmlZZjGp07sB_S2_Md5nojn_PIREYj_w-GpK6Tkkzk7MPangQIZ8hpLZV8rZOs4lHwDzb7_V-QznZHchBxAIhHHivUbORveVCX6duOL91u8OY6Sa5D4nlXNSlUWn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGvmjQBLkyj8RZ1hgr-5hz6skLTjntIZA-GTU7DtO7uqB_sFA-FXOw2M91BbTcCpIeu-xkw7xLao14wf0sBI2JLw1Oc9jtWAvtZbwVv7kUoGatm9ovlMvoMW0RtfCyNcwSPqw_4EgYyhGG9EUCcsaOOz2wqBshayojoBcqF8H4TyKM2RH1ggGeigNMczDsL3IBzyeI-JMZb52uH0h_VqDTiYIhXNbFd4XoK8gKv2NlQpiyIJSlRGLxN91fpXCk0cDYygOTAmG5ec9vhn5vlLIly98bDym_JQjiaKMWIfFDXie7LxZcWACVqdrD2JZ9t97uLiImUaOvhC_nDEegSbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwwzn1z5KZO_Yaqhf3_Slps3SZEU-aH0UFpTSLa2myeLbIdoLEtO49FGaivAe0vZkYENOLH6pdPG4RYt7AN9o7PO0GKknkJRCX0SFaEvfr7mWY9dj23AhShb2GtfeAXzQojmy5KHNy9WS-gdv5z2Rzq6UsRa130qxYSthYAjltKFfOkofApeVzkrkLFPR14XqSHxp58ECk5GPf9D2cfqJIqjt_vnvO8nFm5xOW4EMXH4lB1Jsvg5sWN7zz6KQ65JxULSQagVMZSE3xdx5nghfJHOukwKvANioCDltb7sxp85XrqH36XFJgCKRtf_8CNQJFEwKVPC5SkyOxuQS6kPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IyN5ZZNoizI8pz2-P_jXjWe18oK66QG4AtlKxt4TW1gAk1XtlF77e1TRvviIN2tzHpJGnRzz8xk1pfZoiSqGDoDREuGC7sLP-IO2NvA1bJeyEazbIKUAnz0ChuSIMFU3Q0xBdwoR405vSCNbcNXL7-dpwpYu1vjn_BIubuHtxLPsqqnUA-N2vr_8ZBPDb6kEkHhSw-zAQBiJN5Fhdw4f1HepWuw0zeZLwQJ27Xva_aEAv4K3nEI6JkqeQ1BrclZOOYr5WoMjx0C7e4IA8rRFZR8QZvWnbzTxCIilDzHT3Ol-y91fiBjA5OAfAMXCbC3KhFx6HzcqvpALKozJFW1C08U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IyN5ZZNoizI8pz2-P_jXjWe18oK66QG4AtlKxt4TW1gAk1XtlF77e1TRvviIN2tzHpJGnRzz8xk1pfZoiSqGDoDREuGC7sLP-IO2NvA1bJeyEazbIKUAnz0ChuSIMFU3Q0xBdwoR405vSCNbcNXL7-dpwpYu1vjn_BIubuHtxLPsqqnUA-N2vr_8ZBPDb6kEkHhSw-zAQBiJN5Fhdw4f1HepWuw0zeZLwQJ27Xva_aEAv4K3nEI6JkqeQ1BrclZOOYr5WoMjx0C7e4IA8rRFZR8QZvWnbzTxCIilDzHT3Ol-y91fiBjA5OAfAMXCbC3KhFx6HzcqvpALKozJFW1C08U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVRhAy0icq7zYtauxMOTGOFUqQ33xiek7Yj54hdRue0ynqLf3_eNn7rA6iauxvn6UcHlq8QuignBapyftKlo25C_21oWdG5a2ekUiaYLymxh7wGtO5SBj7XcxveaMuqQfpGimNkqqF21DSrTdnEbvtI5QtR3YCKbMTzXryZuic6hBSSx3Z2vSnKLWsdOcPlGxCc2j-8IeOOOuguAjJ23lDXHS_v7nlrmr43CEh5FyX8oIGTJr_TIz-SB8iqchphF_n3RN2LPetQzz5xhUwyuI3A4mp5WM402kIhcov-xXoech2MiJ5lsaURIo_8KWnuiLAmZSN6Ps1ODdPfDyPFlgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5FSP3Tk-8QsuHZ6oyMCWYAe2jkoIKkycnzb1VOredte_ywPvV7fbfMbBmJy53uuMX_zl2QlMypwxcWeBv2yZTDqjBbM5X0VI6mp5cy31z9zI02UiLpH4nzzSWqnv5ig3_SMpS1WnMhjl1MB58mq7kMI_zV0WGI2P_VfFCbmiGJIqP2tfCYAdRhNom2VS_bIxOctOoMJISe0fP4LHpgpLQ6SCxPM5jCRwmJ9NaJay4CD5WxpMQfQCekqQnbBB3SrQv-_TOmHrD8vPm7JZnzRm5ytCOiU9zPJCW4xotN59E_tHIq5Fvpity0wTiCHWUCka9WXG6446jFvtTZJ0wiPnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Wrcra94NboJGqkXkS6ySQNumYDUeYFzTw9mlLNMsZ-PqHqyTph-F2grNAjAXH8IqovnFEN1iYvHKyacP32FCMN0hopapyt8xq6g2BNfM24E9TbNbUzPZ8A0OMULrBb0wk3ZnZkYllFY0uO_A4WsnA90fIOLR25iTKGG8pJlevGSf4pNDWop-b0GEak6PTJXBHeCK1UKZ7lQ2No7WQQmrOoew5Td44TwCbaXiWMaTmbTUt8PxSmACol7NLR0n6WLnDSx8gFQ1b5svSSzeo4odCUOae823VmKokSYxJyowhEuvxCWkA_bKbTCLKmcAH5ihA8rUMaykg_enRjaFLHWvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Wrcra94NboJGqkXkS6ySQNumYDUeYFzTw9mlLNMsZ-PqHqyTph-F2grNAjAXH8IqovnFEN1iYvHKyacP32FCMN0hopapyt8xq6g2BNfM24E9TbNbUzPZ8A0OMULrBb0wk3ZnZkYllFY0uO_A4WsnA90fIOLR25iTKGG8pJlevGSf4pNDWop-b0GEak6PTJXBHeCK1UKZ7lQ2No7WQQmrOoew5Td44TwCbaXiWMaTmbTUt8PxSmACol7NLR0n6WLnDSx8gFQ1b5svSSzeo4odCUOae823VmKokSYxJyowhEuvxCWkA_bKbTCLKmcAH5ihA8rUMaykg_enRjaFLHWvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=DEBUQS2u1Dy9BcJq2NzhNoZgS6OATgwFOSEqn3HnVit4OJj2DeRH6b1py1-vgX6A0sCId7iz9eYGHJNP63q4Z7ZX7SI0gyuhPCMexzq_sfVZze5GTuAShHM1fIgOrLuIUEmaoKNb610xES9prlLh8EltJmbBIx-CuhfsdslJyw3q_skP7rXQbXoWUwUgMWLWXIlM69gNNWCNIzG7yzPWVYrrzXNF7_PrnaFGBsTzeZN5JSOM7JUAWGwjteQCNQAc3OS_v3VLLUBo2MQT8ZD5G421blL1fjR2VI1AFqgJ1dtbEWAlJFVdS_VYRj6DczW99PhZsElLuHkBr_q8Cao4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=DEBUQS2u1Dy9BcJq2NzhNoZgS6OATgwFOSEqn3HnVit4OJj2DeRH6b1py1-vgX6A0sCId7iz9eYGHJNP63q4Z7ZX7SI0gyuhPCMexzq_sfVZze5GTuAShHM1fIgOrLuIUEmaoKNb610xES9prlLh8EltJmbBIx-CuhfsdslJyw3q_skP7rXQbXoWUwUgMWLWXIlM69gNNWCNIzG7yzPWVYrrzXNF7_PrnaFGBsTzeZN5JSOM7JUAWGwjteQCNQAc3OS_v3VLLUBo2MQT8ZD5G421blL1fjR2VI1AFqgJ1dtbEWAlJFVdS_VYRj6DczW99PhZsElLuHkBr_q8Cao4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnDeXdUpkjRkpHBym2s_jpdaOHe22SSylaZfpVOMLgghfbayTgAkv76s3uP67qkYK24T3rQjxsgpWvFrAQ9W5jAKl_7qYpXIO2WVPIaVXJu-Yi7tAXfdORFB1cAmuEvBQ-Ry6p8azH2Ye2phuCIKfhgRaw-Tpxbn5HOGjaCysCRzzNdub1oPJjkBKFPhEQCErVsh8MggX5RVmK0NWoFpHU50AX5zd4cPmGq5wieC7y9_8A3TopB9tDzr4sGF6MH9XjrJ6yJPRj_f7fDetuu2m3JMo-A4BIUSU-_Whs4CgcXeODS4deWUuy11Dhqo9ez5Mc7-9sbPyqFt58inqBuQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLWkhvbthQKHVyqFP1wFQJoSZqVJydiXnBWJyzu_v2bTDy7pZe0Mq9JfFi3sTsPpfPkg3Hx0ySXuAoC7l8pjWdJRoZ5ZXgzMhZ7RPT42JnoPN5jpu3BpsAcr4avNSJpic9GZjBza3In78PTswlxphoPb9Yyf5wfapPhPq2UCtJ6V0S7WAaW_Bk86z2QskdMP0NcNv1coJeSE9hECf0b9pII8phFNPlD3lhB3XrGkSwOxOonlam7393Mde5th2BphctCPXCKevNz82-h9Z_KmLXPL1Eu_TgmKKALErf7tZRtAxZ-jSFC2FXHo2PfvaQ_0em0xq4r6z_d3dagjtVvjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=AdbpHlZeFSSr-OTwlXnTW-MSeeCeIvKSf0yHvYSo58Yjlp6jkAXhnxWdQdZOomJcEaQb4MpqnMLYAjnUpFGkTjVKtwwNXzmXZcbnZBTLSRVzQQZvAUbrFanKTFCxJnjx-Cr4M3_fwJukPQk4J0ibAEcBZ8N2-cUcLQhKRzofYYMMWUZ4eVB97SwEEgPLDjDbVzyjUPiOH4djho6acBygINb1iQfLXyYHR41NtgXywi93Q05xMfwCT7vhNVLbNFmoFr5sWMwV2aC2LfwqpPQvGjYdeDQRPuA2cKoqocD6onrL_oods4wpiCXkmhqsGCQb5xEUPDUJm-dD57cs9UFa6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=AdbpHlZeFSSr-OTwlXnTW-MSeeCeIvKSf0yHvYSo58Yjlp6jkAXhnxWdQdZOomJcEaQb4MpqnMLYAjnUpFGkTjVKtwwNXzmXZcbnZBTLSRVzQQZvAUbrFanKTFCxJnjx-Cr4M3_fwJukPQk4J0ibAEcBZ8N2-cUcLQhKRzofYYMMWUZ4eVB97SwEEgPLDjDbVzyjUPiOH4djho6acBygINb1iQfLXyYHR41NtgXywi93Q05xMfwCT7vhNVLbNFmoFr5sWMwV2aC2LfwqpPQvGjYdeDQRPuA2cKoqocD6onrL_oods4wpiCXkmhqsGCQb5xEUPDUJm-dD57cs9UFa6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=NaX750bTqwKAiX3disFAC8npEZLlXvq_AbZnUSpHpgUbag4hlHrWhmWvsL6ZDHVNc6replx9868h8BKWBZRVZSUsgSSjwF9XHQ1JtBqmfsz5H9lAMlXxoM5_AWUBOMxZh7xaLYxFCqWHAnMh_OHjwruDVBpvzWB6MTOocFO6gpXXqLq3AF0RPlScCB-6nDx_Yd54KK4CyQxMSw2L8_cLKv-19MuAzllqO-VTtAxNuALBoeJH3tpzYW2MLWvT-wp6d1_2ORXy2WzKERZwUV70wIlTNXT8Cy5WCzZetA0m4IwEUBs6b4Y59mAKOYtwIOsqy0hIgN5CoU0V4kxu-3DIhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=NaX750bTqwKAiX3disFAC8npEZLlXvq_AbZnUSpHpgUbag4hlHrWhmWvsL6ZDHVNc6replx9868h8BKWBZRVZSUsgSSjwF9XHQ1JtBqmfsz5H9lAMlXxoM5_AWUBOMxZh7xaLYxFCqWHAnMh_OHjwruDVBpvzWB6MTOocFO6gpXXqLq3AF0RPlScCB-6nDx_Yd54KK4CyQxMSw2L8_cLKv-19MuAzllqO-VTtAxNuALBoeJH3tpzYW2MLWvT-wp6d1_2ORXy2WzKERZwUV70wIlTNXT8Cy5WCzZetA0m4IwEUBs6b4Y59mAKOYtwIOsqy0hIgN5CoU0V4kxu-3DIhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvclhIIKA44Q_wwh7pkgXWY9ghOVVyf_sXx399IuUWsLf6Mfv_eYhW15_nPSQMERcfrgz8uaiebFyRuSQeKFQ0AHmZ6kq3WYOTK24JUmyQsQ4addXGgiTWOJT9G-gyT9taFQqaY32AcCiHJI5nMCzlSo_bt2X_kDg0VgY7FJLm8GtCjhsOomrBB9w1Nqa996EiUDuFmA_IE747FG0mfNHe8Zihdbin-yYW_5RtklsQTLTv3KSVhF-F-21cI506CnOzdR6LLOyA6CtedC_kW6G5b_HiKipGBqs5tsmy3a8ba30ywe1LeV_v5tW8FLosCy2bLgKcOTFte0ajx9nc08aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agUHw7_otZ17N1GYSVmt1V8v2IldQeIdyTDBeR7SBkCRgW__p_DM40siT5nTILtckfInpOcs_8mn5itBnlvgn8krsvIvdpovcZIbp5O-HmDd41KTDA2jlGo0Bq-_UQ4lLV37m4yjeM3r_3fi9sWh51Dq9A-ZlO9eKGamIMzyxSSTmLKSucxfo6NvvDJoYpEvy2cJPQt9kaKvXMhqnGO5PMvPkqf0t2ZVI7yxmTQTrmOuEIyKFV-0rpyX-5xzrXujex6SOf6ecB82A1iNyKHAhSyrAI1ALx9iuJzJlmCcp9VlVUGWtdrtD8_B-L2aaEun-67OcsXgcJk9PkOjPExFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJTaiUCfnP6hqPhLNVRCYD__jV-z-EZ1BRB4wjjRaulWrGBLkS_I8yBagi-e_crJPF5i4ettEFYv350OFoOqkca10fGCoFG071tZfBvyMUCzrYYzMAgkV7TnqT1w_5QkQDGzaeTZYnyEYP3oeuJ-QvJOtCRqxFbi5oVB4uckzPd9dx9reHBekXZnanV-Zxv8-OMbDK3acKGu5A5IHiOw6LyE9RjvfhdiBfuSJK8cSH9-nx4Z5RG0o_rhRCw39wmLbsj_8OZRG9WgjtvtzpWGVZVkJ6o7sMhu8KK55DGo97sFXCsCjLXvHNtzB7dGfZEqiEluLur_1g_vhOHVbCq7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLEmMVBG6H0Dyh_EXAnnKPBP5Jp1YYphS4BmPRy-bKRpuTAh_aukuhGcvsiNBpZphZvm5ENXbwdy4P5efRpe-gbGwirDb_sHjammEnWXUxiGHm0ubZp1kaKQG224XjcT_U1qvXKhY02D_WwfPmyZj38wLTIGpozL6dXsiW-1UghHu5kucYsfZjfmr7uD-ErhRTSCHDHqReZ7W_k_Apwmh-zppzuqdVSjkqhgqjDu46S0fE8uJvdpedvgEsB3uPVjBwXkenddFGZkh9htx4AIltDdxtkJ_Toele82Bn2C5F3o9TQRUtB3WfzLW403B_e-eY9lQgmb6R_xtvzRSqi27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNcUKpvxlfXD1Q-y5vr_ggNnptmxndNXHP2EfXbCjfZjWzKQ20gEqZt0QYGjwpcJthXTfwAf4IeKhxkon8Nu5xcg70PyGACdiMi7XZQGSrWupo7Vaf4oqDX2PHjKqWzvfvEcWKpQs_yEGROj1NXVBGU6B_II43DNIR9ybYf-ywvWEiYovYXameLW311_F85BelNx12nzootFlB3I8wC7iVItGXPQ0QArjIbb9bII3XbthRC3m6LAgdffvRIYuq3Ei0pbJx7OQ4Yg09DbFW6hgDxTZpcFd8WaxQMT_ukBG-iZ3GYoJSEMQZ3CzcSkG2Q3xgR2bLHLSkvoMwZ5NgC5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ta2grqtdxuNkth_ui7Cx7AH0vbTZ7jbYt0OrBmsVKrXTDOUFiIjvo80z3uEPz1byyAQx3D-0aGoXP5Tw167yHYU8bDPhalHKGCO_s1x4SyqrCZxUtT0JdFDIeY56OsYnfxN5gUzrKvmvIPmu_6VYRPImkPGtdppE_l9-m78Y_BOFcBQjECDvYYtjzPWBBhSFV2k5qTTsldvPKO7GzDHLLglel6SD6tfnCDWiu-pdY0GYH37w-5V2GkXpZ5wj_MQBjY9otLBbXgkcF9WSK-ChgI8YnUcfK5L_tRxjE_T6PGKXWfeUZOnOxdeltxXoTOr_ksFzc3k6tCHj6auBd1X9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIj90Dy15iLf23fUuQa4ntKXqfE0qbdr71gdf5EXt5NvPy6c4jQFek0ID9RVsAzwe5tZVRaBrZEdKNu4ASUkrawQnQDUe00yM_pabV6sv66tVQOCHkHTu4Ethoxjn3ZZhFHWMvdVZ_IM-EpQal8-VwpXbXo5bICOodVda8HYmGAq47Hy_gDBa6RoMBbqcQ-QoBcSv5Uz4ION3T1Mu7U2dcsN2aPRwmeg2q5hRMKIU3QQb6BUkidJ9E3brNiebKM4oWiVSQF8th3zWv-THNe8NiFcq8UgjlAn8HDJIrittRgK46lb91V4iYAY8U3vajF-kZvYWxcDqcHfutaAcj86-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THH6R3s7yCLQE23ZR-lxE-AsaHSC7ZCP8tYcq9jOmmZpaazn6waNiJgflH7QQai6jzHSDm49JcF9hPTiCUxQZ-iI-vBMfNddOvijMmFsCxURfYE-FWDu7FvtxEgN-v5kkFMktLLnCNgNwc2GomEAvw0JZsMdCxhq5949ehcnmBuOxqtxCxyteOuOSCNHi3bv5Bn_JmofOSx8DiZ69xa_Pggq42Lt1KQd2Uaf-SSLxY_ergkzvNW8LnWPvjxELHubrY-VaTMbj5k-DkW4h5mNeVF2wQkXuSIMbxpM1DVUft_vrK8zGC1iF3zYn6zCa3Im_mEkkiwLGizotK3POhpMiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3o3n4cUhWioTyrGktEsrzrFNSwZho0lDnoW4-K9M_LbHNZxFrOtcdMd887qger4WawisafxM5dbegvHPrLjZj--gy1q_y9NWk9VrIyCu8TBenvr7N7GezYwPxhZJPcESLlO45LRBESROs9IZpITasOc5G9W0y3zLnyPnwpYT02fK9mjs3ReHjJopo13lF_Fjsla-Po-h1sE639UR771ZlrIUECy0WrqW5klovt7AgZtHW-EcuIk5nRu02tjDBJRcs6s2OHSWcIsss5eaDXsUT-Swh6uVbAjSov2E3q06elOF45wsKzOcgRZL4ZROV_mAbat4ASSEJ7ST7HFPyuo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab4VOYhPOOvnbpdm_xf1Jfg-P79FUuDY1s1kchBfRFl5IcJ3Ps5uVpY3DCr-ZSM50GbXpGBiqZod3fjpQ1O5wmZwuvYbmDGGnsWid9ctkTRg6CqB5jX0Ycz1nDqU-BlPDbiPp312AOOQz9vYOFp3pDqEq7pwSpGhWl4CBChs9ocUsOVq56ykQITgYkvuRfvF00keRi25m4fzKBnzV0S41k22YX0LZ7d8eKQ6gTwZ2HHq8m0ijs3MNxz1T4P_t0simA1HBJqF8O6JgzBzwAahnOY8TSPTI9BGli73tdwWrREI_xy9AgZpYbfrS_32YQ6RqKgujET2uzxA0t-XKJCxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=maXuhAPugzFWC3_JeYeu7RATetVHxD6iTQE5u_6OCbWC-G8fVb4lvNzDLbCgff8lvMZeytFk0y_6HWMGp5oam7XkQVGZS5I_uO028o8rRWXTmgdtD37Y89B5jVLcW3iggp3htLumaYl_Vw9qADtzg-W7R_SV0xY67mKi_Y_4P4evoUmx7pDm7Wz2sDQFNLc9Rf2R2o5wFTbiR5jTbARTiZBkc6kYIjld_nZnWJIQtITOuzv6HPhLsvDFUFq3cID3JT7BONeUGUsLRvMktddRk72OprV3cDX8lT4Du7Tmkipeng1NNTCwoquN1XHWCnuID0o1CPaA0VsAZBIAQDcRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=maXuhAPugzFWC3_JeYeu7RATetVHxD6iTQE5u_6OCbWC-G8fVb4lvNzDLbCgff8lvMZeytFk0y_6HWMGp5oam7XkQVGZS5I_uO028o8rRWXTmgdtD37Y89B5jVLcW3iggp3htLumaYl_Vw9qADtzg-W7R_SV0xY67mKi_Y_4P4evoUmx7pDm7Wz2sDQFNLc9Rf2R2o5wFTbiR5jTbARTiZBkc6kYIjld_nZnWJIQtITOuzv6HPhLsvDFUFq3cID3JT7BONeUGUsLRvMktddRk72OprV3cDX8lT4Du7Tmkipeng1NNTCwoquN1XHWCnuID0o1CPaA0VsAZBIAQDcRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=R3-IUowVe-SZ2k7JhVNmg_BXb4ZDpn09VHGczKzlm6LMOLCkcPTFxcp-q31ieYw5iTjYnpg6K-6b7O_o8XS8mNZ0Wdo0_kFoCSl-BqRCF49glZm28s9sXpefb5QHk80eO4Vof4h5Lz5-Tm5h4a3J11D4WxXllOKZPEj_pTDczHyc44Pxm7YiXDynWyW9KIGCp2MgMvBKFPzM8QL7z0esRrT3aNN6klqcc9h6PlY3BYJ3q5SbSuY9FtWRG_tUyWhwY2PBK_0hRqkiDShChjmADprbQtX7AGcrVdGg8bunsZT4XbUY7iLXdAIkUA5xn2Nwl2R_Ls_puOGkRXZJSjx4Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=R3-IUowVe-SZ2k7JhVNmg_BXb4ZDpn09VHGczKzlm6LMOLCkcPTFxcp-q31ieYw5iTjYnpg6K-6b7O_o8XS8mNZ0Wdo0_kFoCSl-BqRCF49glZm28s9sXpefb5QHk80eO4Vof4h5Lz5-Tm5h4a3J11D4WxXllOKZPEj_pTDczHyc44Pxm7YiXDynWyW9KIGCp2MgMvBKFPzM8QL7z0esRrT3aNN6klqcc9h6PlY3BYJ3q5SbSuY9FtWRG_tUyWhwY2PBK_0hRqkiDShChjmADprbQtX7AGcrVdGg8bunsZT4XbUY7iLXdAIkUA5xn2Nwl2R_Ls_puOGkRXZJSjx4Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=FY6D2sv1JkFjlaCVVKEAETsmfv2e-M_N4MC2bb1dqsfcV2L41ZnqAm8Ypa_PgEZ-KbctbkdOeE6BL1_GiEAuGt81xFCjETui2x-vML9iTkF23TOFmtIUAZ0lXDaAE8Fvv5s1fUKAWRxcc36lYiEOpJnXbvI3O7MqFQcVNZGGVcF36KBnh4Xb6Mwm0QzeIOk9WjW4Nqu4hRlVXJbsw6e4UlHsymsRq_DANOD0SE7ko-OW-IEtvKIRkVLKvYXYwLBAVz8meCr4vAptYoflGtOmsGUrUelbmkVN4LaDjmSetJCV1P7GboLWR0NjLbOEWN2txTAuYrxeyGFYK8dAmwcuqzuMzuvIIIjl_Bs5G01qH-7GB8H1Fxe6B_89oBW1mIvIy64zwRBbtSAnF9wFd-Bk4rreEZcp-3PpvfdGYbelmBqq34y_Tl1MZxGfypA7pCGP2ufCftYZjvnHmRaxCJxB9woLOWdzKQlDqlugrgIcDJOMOSnl_TrKLubyrcFyx_hJnE-6B7gqrI0uvjLoWt7HSh3ecE0k3HjtHRtaIcxFLmQc4AvvoiOXbmHzFFimKG-FQsH3hVK6gSSeyuL5_4zBr9idOd6LBf4UNgWpL3J6HgIry715yhSMe0Y3I2ocHhcsbQwQB5YmFa_vdt_70sl1jP5Mofv3XZcA1hwS_1RKCgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=FY6D2sv1JkFjlaCVVKEAETsmfv2e-M_N4MC2bb1dqsfcV2L41ZnqAm8Ypa_PgEZ-KbctbkdOeE6BL1_GiEAuGt81xFCjETui2x-vML9iTkF23TOFmtIUAZ0lXDaAE8Fvv5s1fUKAWRxcc36lYiEOpJnXbvI3O7MqFQcVNZGGVcF36KBnh4Xb6Mwm0QzeIOk9WjW4Nqu4hRlVXJbsw6e4UlHsymsRq_DANOD0SE7ko-OW-IEtvKIRkVLKvYXYwLBAVz8meCr4vAptYoflGtOmsGUrUelbmkVN4LaDjmSetJCV1P7GboLWR0NjLbOEWN2txTAuYrxeyGFYK8dAmwcuqzuMzuvIIIjl_Bs5G01qH-7GB8H1Fxe6B_89oBW1mIvIy64zwRBbtSAnF9wFd-Bk4rreEZcp-3PpvfdGYbelmBqq34y_Tl1MZxGfypA7pCGP2ufCftYZjvnHmRaxCJxB9woLOWdzKQlDqlugrgIcDJOMOSnl_TrKLubyrcFyx_hJnE-6B7gqrI0uvjLoWt7HSh3ecE0k3HjtHRtaIcxFLmQc4AvvoiOXbmHzFFimKG-FQsH3hVK6gSSeyuL5_4zBr9idOd6LBf4UNgWpL3J6HgIry715yhSMe0Y3I2ocHhcsbQwQB5YmFa_vdt_70sl1jP5Mofv3XZcA1hwS_1RKCgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JidLK35lbOM5jvJuzYFeCiJSgJqA9yNCGtMCnQEulAerBtL51UWqTuGEKlaKurxMnE_Wv6Bu6gFiWfINU8jqsGu9L7c8trWrcBZ66ozjC1qMZWBQp-m2afkxVHRd4x1Irgj9do40hsbxjCJpJvsXX3oRIz9rO096K1eBHRY4CKf074CwB30ZgKzk3P4Tp5otXGReY5Q-SKDZNxGHGfwE4tOLfwRRrs3Z_Tsni55KO-Bprt3U0D_0iYcif8zL8e5uqjwMYVs6ju1SW61x41aFLvsqGKtjRySNbe-qPxPtQUt_2U2G02LKtNP191hRIWm3hFsIwenAju6sPnJOz9I17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=fADV7f-wU34uj9v2LN_8jupL5MrObX9OgF_o2xSMa546RyJ8A-QRZ2_jDWKH2iunFB90Yh3dPz5c2fG7-cS0fvQW5iZ3ruSn30B0vCV_hjcnSHhsEvoULL_A43WvC-8I7r5r5VcrYA_-CLflenlwAdxJcj1fP8YoCQ7jvGY0FoUbnz4fNAA-4cQlvmR4Xj7rzI_GZ-RpkxKSk3J2XSTlBEpcqI8pMhqLwrTlEPrNi6NWnkgxs4ctvTcqaRmt8pL_pOEU-oJN6qGtpmv2kk-LJdc18-gARK4oLCjtLC32BMQZZX1UfPK5CPLjuLE4YxlKMpr6gpWqkiPxKICh0DCIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=fADV7f-wU34uj9v2LN_8jupL5MrObX9OgF_o2xSMa546RyJ8A-QRZ2_jDWKH2iunFB90Yh3dPz5c2fG7-cS0fvQW5iZ3ruSn30B0vCV_hjcnSHhsEvoULL_A43WvC-8I7r5r5VcrYA_-CLflenlwAdxJcj1fP8YoCQ7jvGY0FoUbnz4fNAA-4cQlvmR4Xj7rzI_GZ-RpkxKSk3J2XSTlBEpcqI8pMhqLwrTlEPrNi6NWnkgxs4ctvTcqaRmt8pL_pOEU-oJN6qGtpmv2kk-LJdc18-gARK4oLCjtLC32BMQZZX1UfPK5CPLjuLE4YxlKMpr6gpWqkiPxKICh0DCIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKTmGBEmSCo5ORT_by5q39VO-0GFnR3c8nVrR01xF5F2GhfYXNft_wDDbrBZT43eXNqw0UjReyBhdSR2y9TSIej5bGATkvdU3fiWVKEhjRblZ6XNghggTEQO57a5Zwsm9K2rlYRMBT1oj_LTIMOjFg0IC837RY7yjrU6dh6fuST91uqWsjm4eY_NIynr_FjL1gLeEmQpqrwFimXc6L30MKQgzO1rtMhF90ql9xlio4EGPu7Et6L3PCPjoS0Bauo_0VL7bkLHrPNgszp-FfgSVbXzwI_WvfJkcpARn5Xsrd3ELL_RCpey5dmGao9fJ3AwaVTFJ13q8e9VWeiPfwnR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxQCm3WWR4CkZPe7sG4cpj57eZTkvLdi_g_qxv8xJ-LL6PRiMt81V6Y6HI4FtBaALzP-UA5MMBH6Xe8AIdrsqNuLYz2AmEpNO-YfGTpqRB71mFeB-zJiprJmYl7K-XlLZFaSszBwvmJMc3D-UJA6flqlFL8iONnEHQry0SzLYxGO2x5a6lfWPa87tSb0L0qoX2RNAl7LYYDVi0oRSH26v603ug57FpMu4J04IEeutSU60eXsAApuI6vhZwGD0WZvEp-951Bu0DxlT9fvOcqRNRQeeeeVEE_vPrLlwtRf8NAi_zTEQYJi02OmeCsJqsH8hgiKHMsf-Fenw8wImfw7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6Nd_j64Qxyn4gqT3HWVKO8tBWLiY9GxF9bi97kF6iMOi9TPx_iVoo4CgrpLm8tC0FF3A80n0qEeoof0a_4YpyQNHRQ0YIP9wLVZw5nXt4pKVXU2JOMPIZYsVqZrAtEYSS90FeUGJ7EDTGK4fe518bkJUo-I6Sz_O1zODIZDqsnd4xYcUNHpx3vEYw1c3a5HSYde13jiAHhSpRp2Z6vnhfoOKLH95BIk0BK9bvFtm8iTfhBafnwiLRtYZTpmwhLBS-CHwKAhFlBXod6gnEYVD4ZNZrCJV2JihgQEnOeBeRY9eIrwkSiHDmiXJkhXGo8_G0KPgVIEYuHcqpKHdkN9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr3LszjivADRtvmn_VS9N3XSwo3XBpc_oht_DAP3Wdapk75P1UOoEq1WddxjptvcKcXJ5dApi8O23AFHTQPB1-j7SQblUoW8PBhIiDl3ZYLOtD6jXkOFKizOFdpoVVY8c8bVj8_h0hEbYGFBKNAORvRi9DQZ7w8x0yHVWx2byE91Uux8HX8RG9GtKkenyYaqPbZQibwATzE27jbBwKvdx2VZgQJ_7UU9qirYaG2vy9ThXu05-VpLaFu86G0jQPyJaZmAnuv5yaYDP1evjgSGcqVVPD80hfWLTwXLuCIVVnXxB5G0lCbnsdb8fkjnBbzJFTdsL6Bl0hSrk4m1T3TOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGAHRblx207jXTpin4PhNMs9SYKz4wPfj3Aq016aKHAIkE7rLY3JWR-ta76u1c_AQYVCykh1cV4wIn22kv4rIk8LLYbqULzdb6xda7AGt2MArzLP_RGdg-405Uc56dQH16rETocAV5mOrtRjWUxm1v-RnGjbKJbAiEiqYIF_hyOcYHanCOKP9BJEWfpVt7TTUYubqldEsHBzsgld8uSXlVJ4aw0AKw2jYub19mZL9eUiSQ_ThM6dBBD55lWkYmJ8WFjjFNTqooOQLduXuVbH0HCflLbVtI2B1L2USYcKSCEj-gLShM6uK6mpu91LNqtWxvYsh2DmPHW9jNehAhgVtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkDytKjzUIKKfUJNKYYPugxd_tcT0nLTGJnMaZM09zBQgXjb142J6G10ERallsGnvA3cxYe_jVdYvREOId6pdw1JeOG14Z3Q6Oxs0Qx6mGiQO9mEQc4zaII4XJt7W97EGx2Q0HV2dUdkrQ8ahZmBtkYg8FOC0YijCM_7YPb6CNO6UEczEjwGuFOwJ2kPQmVtE_Bi7eoUhE4zw9qm93e7tKs1g73dY_J-2BXuvzl5trdeT5zvqLvoRrEwkW7BqGZflQJ2QHVhqqgDlNxpxxFIG4Il-XH9nu4TzRDsxY3SHc4caRbAtEKoUX0EOHJ33xBfY_t63KazqyaEAYdR1Fq4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEvCcTwDaoWd0WyPsKZak-SlkadidKoVhWvfrSC-tc0yff1SZaX3VI-PHhgP-5wlMisRTzQaRmsfF28pJmWFlkOnfdgbnvgarZmmPpL7bBUY0Allvx__sOyvLEKG7eGznev69yATaCmmn01NUtnadQfGfn2Gu5_UQ6tQQ31HCS95B_A5mY6FoYMFE3iOtN-cWvpi3STzz_XNidmMMXKgnBTS-hj3tuyLnSsA0OsjIT7akYWLev-E1TVuDuhjh3B7NSv-tf_k9xcK_0iJ_-_SAO4po9rH16_tKdASQbyT8y14br93h2EUZkxNbmCUZty_-KjsICd1UFhyGHQ3oD_cVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lt02JjhdJOi88FmLhfFk3E8752ob4JO9MMoAMRA7Hif-puHieRdkS68C9blL2BCa1oWOmLq4Cq8Jhda9xlRcxhHJtezo3_8gN2hHbLHrhtTbjVZ5znm-EVg4EBPLnnZr1483dvkHt2gM4Yd6pP2YNI69kIiksURU0C4rrkz7WapfunXNLbI9ZoQGUMK-kEDMEpGCL1JhbUFyqQIpEOHDIt9Rx7Z5Gk4YBZK6e48BCZS-XyWzSI6HpOm6NBXm1VNS5nxvhyCNbw7MYnjgQqYuVQY0_z0I1VpgXuqMWC6FVUBUS5jfY6tUeleoC4tNkLpH3UcrUv61HJnMYbbVsOe8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vldmr3tybxj5rK6okE8h9ivjLHqoLt-TOhNb10ODlsiZvzvz6qEgFXuCa7UdHGQc0a8SrgH1cJ6NtnVTClsyesg9bGHo1bviFpQR01Fe9YE6wPTGOk71wGqA9yJ6K7Q8JQ46UoKLbYA1n5G1v6MYJeeJNutiO82JLKQoUcIQwpCSIpwr79e7sRDsYaUff-q1sPNxavMQOjL5PKeCMMDbJeMCPWxg0C0_DGHWCu0oW1Nc8VP2hpZ03_YgN5WAAf1oFOPUGbzwywr8f360m1l_YaCmBuOGj-YjQq6NQUFcS7tWrdS0AIOidZMVW9lV-UtYFInOkwlNhJMkEnnDGAsWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8ZmY-KAWTHpQf4XsusJkdBQBmJkNgl4ZfEOomxTgyZoAt-soGnALX8sznYe9fQBOhOdxtQU-oEXu9VyFcg9GyUa9dy3dxipXmLLh0GifQdxgyUHVbKEAfC-Txwzk0CIP05Sb49XZ8KBKtGKuyDrA715mNpPoCCifkSdLUJNviDipE94-IOy2rIjqUz_qcx7pCGQDE97KXtR2Q1pGjmw_fYmjw09jD5ZIB_GfkTFQpeeOk_NotjpTQlo3hKFyXD9c6Dyyh1boJeSW3dn2pu8rZXast0Ztiwv07MmUiCLbFfJiZZLdCZkFylwS_kc4OSGBJdi30gFwOK9N-oc1qFNGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8bPSPqgCXSj1v571TGNe8rnqBrpv2AaYPMkLkUWBrzycLmXEPtlkorGe7_rTH3cpxr3l7j1Qv4c_jJB1ayR_4vTWgSq1MEXszh-2udbin_ljMCzrm-KmY2a9VSTvqYg_p99rLR_OFCKyDWdq6vcu-T6bVDwYCRXOYKUqCEhDBL6jH0t8GGA5NXeWx4P1qYzJjrIc3V6PwLcb_AouGgqjjz_c5pj0TdalrRvtuAp-Pf0EiKFxdWRbBraTeBf-EKBWfZJ95-WAdGan4EXhNrOIZth-ElYPA1MkpdzhAS4dPXp7lLZLMbS8ZEDdjNAM1HgfUFJThpLpX90Jv2DCe5fZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2EP9XsMzIj06kpv8KyBd5v6ktLAqKB0xZpqBTnoHatF1cxQxydQvIE4j44sDZeulYHta-_PNMUVyaUqbq8D1pANf7A_-Bds_h_ZT3sXn7wIQ8v2PW8XN0fg2uLA1jxFhDurp6mqKO2WpEwEazOg1I-IuAsC2V56TNZuiuF2HjZDOBDtvGY4UStasFrdqTZZsA8If3UUFDMnnYiEZjC5Ddud8d5uNbvmQE5s2Oqxh66f7tpIdiAJhpToIQNlt9q6ynZypjKbUan4IexeLlBF5yXKtoT9knFKCGZ8A5EFAGwi0inMJX0PNjoo7OQnbR4ICMNzHYVhAMHmr6ZwFYwJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jItOiPjYsRCna0XK5JSQIoPSLqwOAcMTeRJfuDXGUoS5OoNiK3fZXXFmcw4m7x9Q5sKRsNcIBLE9bQRxwqzFWvIvj5oTpJqzr63gzyVNTWckLuNpVur3-H9-eml66NUmyW7v_3dB0QroUKeJhmQiglWlXAnXvaupHuPv_iUHyAyzNRLL_BGO4D4_0suleQdSUZpQWMmy1NdXJKd7q8juupEjqfW4es-rESes7yh9s_hTcVkgWTUk93N5YFg42DoY8tKQEqT3x9keyimrOK_tplNyfSPpTOWWP5OvMTiFhVKq2wpJFoKFK-roeVG-uHIMqGfWH3slSJ_MHfslatoWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLlEEFuTiROHjuAUhSSDm94IUJSJGKfzThYFHY0s5dA4s6PQJqp_nPGEk9QFL-ZmBUEsOZ7eZUUj5-8epiUYmFsElgeYp0P6ttgvxVUos71UqJYCJuCIlcPVifsyvz73DrJOnz6I7kXFKnqbyiiPBwfeRNG5XZ0VVW1nUKYDZktzzdXiCDXsBIATY8F-6TycRbOLK3QOSRgoKM2saNbB8FcssZdqL_N0SrM4xPB1Nt6u4bh_KQ50-n2AuMbbQ11N8HinVPMv8wIpkWGtQO4dz9Q38P1kOuO-k1hNSrX75a8XQgZUQY4JEjz8IonlDvBOGoHUDI2umIYhy1VvsGqGyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLOENR2OaRRfK76JlTOL0cpwraK_t_TeLh79ilo0CZbS-Uy6RSHqWENu78vA-qUqpiZ6QbnsXxLn8FVsEQGTjbxT2W9Y55l3IC7JskvYOtHYHHQJSiaE4QMi01zkRQA6g1P03gHK-XLLgbcu54hlwRWoLHzB6sbPVceQQG2XO1tPQpfdH4BZqLxnv-rfeXIUTm2z24SlsBIx1PuBn9UuGkeLHl3EX4fxetVOleqBc_40cS7-YP3OPJfxG7R88DRxlcOq0yPb4apw4s9hcAeyR7b7GP7ngXoqHwGMSQluBUSgMDTmmPSnsM5KBg1oQepWmy9XN7LfJVxEmH0fOngiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npQI_d4s4vwb7PO0psNm0Q9Q-uPS1iPAhbcqjBOmUXMuVeYRFhb6fEEUJ238ysYNfv-_FYT8t_n0edzD2bp1Dy5nDzjPRwc3pe5iVLUKcvZcT8OS-EukQaRAg4UDj36zNTwp3IeTp0JEFFPB3I2SA7eEs4PGC0m8iLnw6uHsmJIYu4pDALTH9WQGRvCwjJXWvhrjSZCMo1T8MDu_E6sZ0e1WqrFUoG7Pgn_6WR8QkSKKCrW9Y8ezM4N5hPrNGqinmfFnah6aflXgTL69bQhkSJB29Lwj2oHKgFL6yZfPC5DTzeVCjkGckEoxZKLp6dKOwB8bTt56-An46JyPnVYzCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
