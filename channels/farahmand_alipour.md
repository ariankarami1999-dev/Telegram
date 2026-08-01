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
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 17:57:25</div>
<hr>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtzgI8ZLvFdwG6zvpoh4uaDksqAczQxHK-x0Hf5j-ti4QkPPYlyqTdvNyJRe3fxfTpBBDGC7Im7zjrycBKwu4C66c5wA6lKqAXg-T-uoK3s0dVj1feIot0xL82_a5mQNwXyfa6olMwg8WqZYkyT_pRagL5TBYCunODi8kodCx43ZRXWLnehKQNKFsZVs_WGCjRS5rfnP4sL7fToVc7a-vXmB67ax7AV_3I061SFOuzfD5S72nj1wFXICCcEOqNmwL9dXjMO5SqfD-2fsJMVw_5W4TGN0BY-6a_vjgWVgbJtFoFzokdBQSWpT6V17KBRaqIp3KwEQHLVfszVgOT6ZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgINaJIP1ZyAOPM3iTC1tLCFUVXkU_UlrWgn_cZDyZL7_JzY9rS7m-fg5YDxm1gqhfnEGab7we05E5HKJOTVQj-Lopr8P20f2JK8NwhoPLa3F2a9aZ5tCG1ONZNmLSzuIriy0ZK2KaBOJellWmjkKPx3_rldj7d0HM2crhcZxQEiloDan9ws0bFigfGZ8jDGtwJg_PKqvF-tcMuIkXaFbHUEPkiDTsh27Q6AFlJ8AFkNGs7Srm3NIs6CH77cc5VxBVuqWr58DSeI42rac_feM9Qu6IOkF7nUJlTVDYLJ5jIGq7n4kJe9MJMzFBQG0zNaSDPmHlvUnOCmrYXykYs01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm_fHN1nHjyvkaB-7tPOtmZceBjRoGHp3L4iX-tJZ5cMg2Kff5fgtMs1QiL0miXEGA9ycrJI9fFPON0ejXoAQBYMmlAMGA3JkN35ATa9LLfUljVrVdJ0jKI4ktTYju9lIYTzE-VodFMmxet1tBnwKkn7m9r0IE2pqysKnN6kyWjrfmqRhLNeC_7KHKAmQWoFc5CCqnSlPiRgZ2Z6s7YMx5v7eaTR2b6sNVde_oGhI4z5f-w8kpFIe-CCE1-CrsMY8139jkzD5xAbJfWz6_reCBBTdJyeN_oOFHsO_2vF0IvoUhzMWf09AWMlg-Jbw8yF3Pz2tygDA7aU7NRQt9Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMmKCFhB9pYWn_a6jsuz822pq2sb8jcKBrKDGiGghJmReZMhT6FLLr_8jISUrhdI1prpkTvo5aYakNG1yFYeV66GhsQCyYn_3McQC0AY1hP0v-icUhaE71oT_yLpYEnmGfOvOu-xSODoJvmBfSOuBW2U_IncU43uWAlJPTe5s-g6x5ixm9fpPvhpBuOMFmGEKD0Cag6FHpnDd2bO965spJy5MPssoYyXE6CN0vEINXAkSE_-AVgJv3EeMJymo2IejOg5cc4HhyudBc6ikzDaaGFLjJr1lOsLr7ecBS9IKBfl-r_WAi0ZyczU2Y1DeXIvWPvQsmyTqqRJexYhCTyPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssHwtwbPJB4GLn2liwdodqXW66uVMEIAoifRBwydBYEW4fF-Yh1iogzzSTnNzTM9zeSNIleajRpBM8nkPXddaJ5s7z0PccCEG0WNuyjLQbdcSzGoquXMjViVSPqmVFNaVssvubiTtBE0HZgzhGi0MC0vBcXFGvSMIK2deqaAMRj1xBWjpavNYK0KpQ9UsTGwLhgfmM6ll1oGqkroaYrUXHvSdsiUaEpAVRf9pik4wrGC0ThPPimoRvzKkyUhsHT1UMbDA4IwSR-jrBvIjYPJDpYHc77LHjz8q5EyDangt1oKcJ-snqPZHhbLBfzuX4z2rdt0JH45h7XYMYGLSK37ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDxaaIdJ93FbCg24M4H7QVQtJx2BoHEdTf17GJ7a9v58qExiCx4It8PS7VzgMrTqKA-c_cZvawUWwO4qKaOzrkvC3hMyhfXbXblGalRlt3L9f95gaZtSqZlxYyGj2NfCuLfd4h4oUJgIvXib1EIufFXfyT6bspNUAYmlC19Uc0K9hAunbCGcrYP1i19JMqNvZoNRRd-KObLMMtk4AD3-GjZkhVJTw1Ar8RWQ47oOuaNN4KmMW2b_0kIzZ2f_ijLsCbDjJ7oZxudlU6uQ5J9UozKzEshrTXjjEC7T617nq0kbS7IS6IVUAf_zQ2w-6Aw7is6ESJM4rbExSz3QFiZ7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=JeMhylm1gwRJkUJ_xg2v4pj6tL3-VI0SfDCpQvqV71IyPBIdt2pVTWDbf84b1Vm_LR_jKNMb2SiAUJ67ZAH0yvxKg-XJvO9E1qIsjAw3e5AuWdVKCJDXxYAQ63EMsbXa4YiIRMpO16x7MoN7vsy3WKzmoAZksFt6690uCYBcxgU0JdGGCe1S0TdH3S3xHX570vuj0PY7IHXMA7TNJzrGxprrwDva2tbvEitfN2vETyDGPm660TRiV2QuK41u3qSnwQn05LhVKGev2DkuY990Y7yAt7YsQqdaKx35EJ4NWncXQq09vGvBKiAnvjPR-CMAFgajSWZIOBZVwHzbtM4lIl_6Hie9oor2K0Ic6Je6CJObVBPpT-qjDsStf66Uo8siy3NXLXj4iHpAav7qQlEvWHJgn7LcHglczJqYVH1yoqY1xsaFIK2d3YCTRoiSgDsC4WimZ2Jxh02i1UsDJCk735WqA5Yvvz0POE4QWRW_zkkXkT3OszrmYCQxxn471umJBVRiPXzjOdcmyk1B_-keKdKVAMtPib68rtNFvlQO7_hv1SRgscej5s9TafmJR_GFN09JJYPQEoc9uRrsERNEImbjx-5DKfqg6wkVfzb-H5H2Fr5vQxqA5ZI0X33HAzQJGRcucTJWRHvIDoW6vsUAwk8n-EJN5ire8smej3qisiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=JeMhylm1gwRJkUJ_xg2v4pj6tL3-VI0SfDCpQvqV71IyPBIdt2pVTWDbf84b1Vm_LR_jKNMb2SiAUJ67ZAH0yvxKg-XJvO9E1qIsjAw3e5AuWdVKCJDXxYAQ63EMsbXa4YiIRMpO16x7MoN7vsy3WKzmoAZksFt6690uCYBcxgU0JdGGCe1S0TdH3S3xHX570vuj0PY7IHXMA7TNJzrGxprrwDva2tbvEitfN2vETyDGPm660TRiV2QuK41u3qSnwQn05LhVKGev2DkuY990Y7yAt7YsQqdaKx35EJ4NWncXQq09vGvBKiAnvjPR-CMAFgajSWZIOBZVwHzbtM4lIl_6Hie9oor2K0Ic6Je6CJObVBPpT-qjDsStf66Uo8siy3NXLXj4iHpAav7qQlEvWHJgn7LcHglczJqYVH1yoqY1xsaFIK2d3YCTRoiSgDsC4WimZ2Jxh02i1UsDJCk735WqA5Yvvz0POE4QWRW_zkkXkT3OszrmYCQxxn471umJBVRiPXzjOdcmyk1B_-keKdKVAMtPib68rtNFvlQO7_hv1SRgscej5s9TafmJR_GFN09JJYPQEoc9uRrsERNEImbjx-5DKfqg6wkVfzb-H5H2Fr5vQxqA5ZI0X33HAzQJGRcucTJWRHvIDoW6vsUAwk8n-EJN5ire8smej3qisiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=rwkbz0EqkoYlYkFtzBKOCWx8GK5X-UnLfUMi432_xhshwiFtzzPrCmXOJCxmIsweIcc0B7t_0IUQyPG8yg_IEdflPN2n3T0SZRzTmtxTTLFDaX7fBFtJnPWvIiIZRObOfIi3m_itJPVWhjIySEv0B7zJDCmo0NEpOJplu6lGrSAnC5-k1Iqx0G3TjVZOshSxrKnE_CJhvlS9CxJttx8A_zkRyfF1th8V4x4CSjKH4PxpcCg130EC-HYJrotUsieOVoW6yiNS2_Mwx0yDKcRojBXU1kzwgHNfLz1JdENvTv2ygBvcgT6VK_mYqp4Cvk2qSeRQE85KlxxG6xjwtnctBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=rwkbz0EqkoYlYkFtzBKOCWx8GK5X-UnLfUMi432_xhshwiFtzzPrCmXOJCxmIsweIcc0B7t_0IUQyPG8yg_IEdflPN2n3T0SZRzTmtxTTLFDaX7fBFtJnPWvIiIZRObOfIi3m_itJPVWhjIySEv0B7zJDCmo0NEpOJplu6lGrSAnC5-k1Iqx0G3TjVZOshSxrKnE_CJhvlS9CxJttx8A_zkRyfF1th8V4x4CSjKH4PxpcCg130EC-HYJrotUsieOVoW6yiNS2_Mwx0yDKcRojBXU1kzwgHNfLz1JdENvTv2ygBvcgT6VK_mYqp4Cvk2qSeRQE85KlxxG6xjwtnctBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFGFb60vvXuFc7Ei5e9-5_0FLTGyqDc3-VN2Tg9bXgsKEiPFfDHsa5oFqa3cYcU4UodpoEzWtxycpLQea4TaT0D3zVNiW8ZRz4aPDw6uI9HvjpiYifh6uErGEbPCbP1KUDkAROBjWwZP-SlR6D3POuHUHlTum2jFV9uyDGdp7XXpQa_xLf9ZyMLvDqvprVwgolXs2UrJk63wfzA-mNbAV_S7y98N5CLHZRbRjWXuxBF6e0C7M3cRer9soirSDG9Cx4aXLOti6EIIY8thzU5oksKVP8S4UOKq16UM13_cI95dMjc3Ae8sUBiqFSraoo_lg2ZSmxZyn0YI5q1YVjB6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhuS--7FkTHmhBUlWRm9GSslYHHLk_hywHJyVpzKxATESerEXoS-qwKC8Xed-1DdXPKihPD638XmnD3YA6t2nUpbvp1DjspjICNsyxSpuoEsC5g0BrkicS2QDd817W4w35k_Py-hzVUitguVkJC_EMQd0HvHel6UYxKWZm54ImUgTFQ5Uwgiwoau5c-QDN9tMnd_MFjtFnViwmxuXPNx42ihaRALq_OvGjPCzDRGli5iSsU7l-VVsS7XwdxOoS9E7iCqrfoxKJ5PqOyuKtklicehN2op8oKZg6dyqKy-NwmHiVp62x1QDOJ7cdbBJkwF1PQRsRjTC87mmYlSR4A2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=nV0M3R4S7qDA946RTs5zUGOy5NYSJlY_Y1QNYt2ZU5Dn0lblufwMNbjRuCpEBtBXIgp8XKZbtJ_3cSsYg-CiAPwZCGG_oN7kymfTbaRpNqvv15QmAoVNE0qm-IuoSNiQ004sq2eoniD45vsaEL0F9IvwMgqxdSfOejyzpktsQ7cpW8ZUY8vbqPogwvka_FSJtF_fsaGc6Mnxr8I7yfNcI7ENG_WtqvDgHMG0RAuBduC1oTMAGzkAmha6KPBFHZvXRf0cXkJBHSclHg19NyPCnbVTCDrSfI95AKE0x_7vMfMHQHOWXMUhjivm6X6K77K1ZZKARdjVsd21tdNTzVtI-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=nV0M3R4S7qDA946RTs5zUGOy5NYSJlY_Y1QNYt2ZU5Dn0lblufwMNbjRuCpEBtBXIgp8XKZbtJ_3cSsYg-CiAPwZCGG_oN7kymfTbaRpNqvv15QmAoVNE0qm-IuoSNiQ004sq2eoniD45vsaEL0F9IvwMgqxdSfOejyzpktsQ7cpW8ZUY8vbqPogwvka_FSJtF_fsaGc6Mnxr8I7yfNcI7ENG_WtqvDgHMG0RAuBduC1oTMAGzkAmha6KPBFHZvXRf0cXkJBHSclHg19NyPCnbVTCDrSfI95AKE0x_7vMfMHQHOWXMUhjivm6X6K77K1ZZKARdjVsd21tdNTzVtI-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1qX3tiND3glGLVAwI4kpbotGcKRcXWnkgeI6ubnzLvoPkPZYZHU8eLcpD6FVBdjDCC588WpslsrFm2hr3h2JnAKDMlGB-yhKiPQWa21f8A-o00L6hDe4eSIdxiJoU3v-CTSwhjhqn8Yg3sVYAcn9u7E742wxa4hLFshqY9oofgXJGtY2k2pgez2Q_U_CmeX3doGcl6048_YbXEN5nCSSpSHlfk5xWKxyiwbA6Rb0jCAyzFmv5xQ66J0U2T69Bd9-mF7uAuN5_n4FafA2GxssbPKBdt_Ep9BJkexnHV-naduVqh5wzJ83x8eowSmKcgsVg4bZuHPtb0SwXH25XJWSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_HE0ONHAZ4r_9kVXr9jjo9HyZzi03rg-lR8phbELplNi_2xhUE1Naaui-wjXP5pveuTFPw9i_SmaRTafXMPRaImCzrTverU7gv2plvn6ZJALOpt8dJp0mzkWhpp3gTY5WJrSOuDbfNvcIDRi_MGRm3ABmVUVbD3UnoOf2ohBoMi9JhAxZXlmYhz4Q09EwEwf70o2mpDGTN4UYfvCzDEn988UDG52OLh-8ZCxCyNc9MIaP4y-zNfIbCh-r0E7_4mzvplJ9t3NfzMsOaWiAqUZRHioute0v3zDAdLuwEKeGg18vnARaaQ57mLLWisWCEmvkvq_AGvx7oKR2ZlbN-Opw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/netFpsSb6XcGIDsgI6KTZxnBXEKrVloiZeus_j6ZAf74BdZbeiJFd5lcQQH4loFlEy0NtC-L9dzW2W9qQTfz4H_POS-YWga0ULEUrIrhXWDBADu4wuZR3475ef6S_4_mAzL1Y17ZYDLVl7Ff4qrrfqjvhIa4O1bbnCW3ANM7BwRXrHlN6QYiRgnklSrFfZ_QvkgbX4Uwlegedy0I6ctj_suXhITWJ_ayYB8iTrUJQzijdSVs5NTjdh2bh_DM_AYhya3eLOZ4IIJNfA_aT9qRSyxjP1SZUmOTf1mZOJpb9O_iTTBmDezGC8a1ogouiOgOMKdx8yAL_bOMoIiYpN2n3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXocbYrcmWv_kkmX7dieP3zXgeWpcfWNi3hQrI6YbsQ6KCEjyT-nHUHkXso4GCZyGU8w612ezoHEYdp8pepS_53EtnCZRf_tht2ZwLmvcQVTkpr-0komtj-goVP1ZlBZ4zLQCeuNLTONDz4Y2GVegbGtD6HIVegamEA8-QoqwhFkYLSeSrwKz2xB-kMrwiwRa4TZCG1kUbz1VSGNlXA40riwAjN15ffu33XQyxDWgsaLR--J0jxhUUqrSh515qgvSePhsuIqkTxD5uKwQ40zvVNcja2m0FAHoNTUKbi9xlPfBebe2P2eUx2pR3SRkgLWWN3HCxkKxZkOj-cyOCFRVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJJGpZuruy_OZzJQ36_lvkhD0wDjjvkyoeAaEDhkPh-XNXul3YUU_L8ATLIO653lRJhne5dk4Faiq3A-7b9G1EEcqY_62000kzJzH-8AC3uU0XAvjSpTTPH9leISKzDS7XUcXayAkhhMjB5hStitGQCcIvIH04KF8QNFOzTQBqaBAjt31aE-wIennnkFYGSeyg-rXBpDUeNBc1JeHW7Zr8p_729HBf6ch44EZ8QSLADJ-wCDl0V1dy1D48gDgaLR3gSSuBtPHj5OR1xtUuYeAQ6Li9aCVNVNZ2CktTMegs7tXaYqx-qRIvJ0MzNieWuzwHqc7U4J2c-uJFs5FNrntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QjUKv_M1xKx3r-WdaagKW8oqE6_tTgByrj8PdUqrj4rOH2qNTMocqXjOb_TKgr6ZzKpcfME3iYsMECs_SUt5xFyxhw8Q9u-K0TDwsutcio5G42ykRhv5gkZgSB7n6r_uc5gs6Dhyi20pmhBU5u5hL6l40LwJ0bNVDkMZP5ys0huNLRisDe0NCE0E2BZKtBGrj19aoX_jBS449gN763vFbRSzAwIouBZ_kdbZsUjC6Gsp7j7qGy4yb5U81lGpFPTp9JW_Say6PhbJDgeluT9niHHMD6LGtHTTX-iZRw37uVxbZ1TCe0hvgGQDPa0rSKJTZHT6Nwsn6Y4U2DzfS5cZ_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QjUKv_M1xKx3r-WdaagKW8oqE6_tTgByrj8PdUqrj4rOH2qNTMocqXjOb_TKgr6ZzKpcfME3iYsMECs_SUt5xFyxhw8Q9u-K0TDwsutcio5G42ykRhv5gkZgSB7n6r_uc5gs6Dhyi20pmhBU5u5hL6l40LwJ0bNVDkMZP5ys0huNLRisDe0NCE0E2BZKtBGrj19aoX_jBS449gN763vFbRSzAwIouBZ_kdbZsUjC6Gsp7j7qGy4yb5U81lGpFPTp9JW_Say6PhbJDgeluT9niHHMD6LGtHTTX-iZRw37uVxbZ1TCe0hvgGQDPa0rSKJTZHT6Nwsn6Y4U2DzfS5cZ_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBzj22DS5SEHbqwyUI6HVm10U5HoSkVIrms59r-TEmQy5ee9b0hnbhT6T1nnp66NS70q_a3eCWc4K1SQNidj5rbxUcEwfLSMZWn96_cx-UctMxcSjoZAKuyI1K98ILsYAoy18XeI534J71XwVpWHqh6z9TIIYjWZCrTCD3icrbRXKRRRwd8c0FWL2jTiAo26McBo6mEDzZ30NwPYvlJbWoSom7-AZWYNp75IOb9kliABa6O66G0gw6qDHawSq_7ND27-T8MQ88Vh8VOS5Rwn6PbxrypGFsatyEGToONZByxXSgS4XRz3JiIJbHvpFYXXB-wpcqVx5sX5r5gz2yxSMlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnBzj22DS5SEHbqwyUI6HVm10U5HoSkVIrms59r-TEmQy5ee9b0hnbhT6T1nnp66NS70q_a3eCWc4K1SQNidj5rbxUcEwfLSMZWn96_cx-UctMxcSjoZAKuyI1K98ILsYAoy18XeI534J71XwVpWHqh6z9TIIYjWZCrTCD3icrbRXKRRRwd8c0FWL2jTiAo26McBo6mEDzZ30NwPYvlJbWoSom7-AZWYNp75IOb9kliABa6O66G0gw6qDHawSq_7ND27-T8MQ88Vh8VOS5Rwn6PbxrypGFsatyEGToONZByxXSgS4XRz3JiIJbHvpFYXXB-wpcqVx5sX5r5gz2yxSMlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=GC8mDbAFPu8H-9u30yAxckGaqLKTuIXRbkDTfSY0Q2_yPjmWXM4B6l_jGq1fHQABsGTTweW3AlMFga4GXTv_AUKFbFE125U5pQTJARxSUq2sHXi694g71OJ0NYeQTaQap0OLkh6TtlAS6QgoVI1o86W4CelOiB2ltuzShrAKF3qtgXIcj8U4VMYN_kdcu6JQy0RuTMa-iCzrgN-x0adx6QC3veUJ-EtwHtS343hBkDoc_048Eww-0YdbAeZx9gsJnJW1Qo5TEjZjeSlhoDe2y5vlHdhxzd_hC2pLyijae5Ji1EJINUfVgk9jhJeN_7q_KYwdETJMpYb9Ykl330pe5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=GC8mDbAFPu8H-9u30yAxckGaqLKTuIXRbkDTfSY0Q2_yPjmWXM4B6l_jGq1fHQABsGTTweW3AlMFga4GXTv_AUKFbFE125U5pQTJARxSUq2sHXi694g71OJ0NYeQTaQap0OLkh6TtlAS6QgoVI1o86W4CelOiB2ltuzShrAKF3qtgXIcj8U4VMYN_kdcu6JQy0RuTMa-iCzrgN-x0adx6QC3veUJ-EtwHtS343hBkDoc_048Eww-0YdbAeZx9gsJnJW1Qo5TEjZjeSlhoDe2y5vlHdhxzd_hC2pLyijae5Ji1EJINUfVgk9jhJeN_7q_KYwdETJMpYb9Ykl330pe5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/allHITWI623qTOuAoOjSPTpJSnHLeKaw_wjZCdW-JN5pYSfkS1-jUO2023yLIcKYCGjT65Kf1VVGbDOVS0vGAqtg372Red71KIBevpmBmKy6LQUeHlMnpjLLwr_4dyunNYOD_H520A8lguUK1b6ieC-YDGHjLzVdvGFzRL9FoXBNtL83d97rgcX1BnXWWyX6COAaUGjEjh6a8sK39JlptKj1MC077PLTMKb1Ith9lg2HUJsRer_6x-E3Rk93JIH0aUTXD6y8j7vX3yYn0Rk_ydelkg2bgex60oEADNTUMAQwbP1Z22nlAdqr5uXAqYPi-izwc3HrTm0ELJ-hXjFwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw-aclckqI2eZQnPi8-nBICdPUNjHcABsKwoMw152h58jb2tJJrVRCLfb5MNQmmFbaPCv9bGeW11a_83C37pNS4s9pakisLf5kJdicCYZe8KCq49hH4ZbmqOyRIyxjQhAYDyXlTszl_mdoYydQ1BEh4XiY3fDt882tfNcsTt6m-FpHKlpa6GEjEBnFDWWpuAzTs2SS_Y4QBH3g9icOAEDArwI6UM_dhs2_j8HrpAZzfiTZY9ZpnnbWcfWph2TnjyeEms3he0QIOkAF-OxZianUBEGiEm6mu8ufL1L9G6Mi0ivxqRRfF4qZH-HTSsCqCWXL9Qh6BCXDB56cX5jAaA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=gvdnNkiFvhD8MN4FfMtc1eOrvSv95TOH0zXKHFPYEtCd6n826i85ry5eKIrzzXBYoM2BM9pKG2FfGNHX8ghXLEGTJ-JLq0o91KBG6z4U0hSzmvB3tqMOOsA7sv0xWLgxKGQZiWGHkUKUWUSJlywFLg5N5yfXC5KA3S1Rd-Q7BOa0xR7RfY1CtEtHrRDm_owUg45k0nAzjjL3Mo_YK-sRe8iBZFzc1DOHWq8Ts1jPVfK-7868QcKoCMY5P0fU4xM8740XySMrtDTz1GnFAgnSDXCTSj8oHeHq8wsa_Xcn4bthtRDcMF_C8T7nK2ti1zFczECavV0DCto9KjP2lxsZsbUvFd-IiF3OpIPYOGEIS-HeLRQVH7B56uFHA5jgetJ-ywmRJP0Tz3eoyoumqVkHf_M4Ynpw5EzGucMrTieQPc7I7swmoSn0DAMx9t9qtF8uUEH9quzxxkIh6FRIGq1rs_Pdbx5uY8PFwVVrjvsKj90_7vi2jVM_ckbISHrlRxt_ZMpc4FSiSUSP94_LZuEnLtK6Gt2Er_XFwKxS4jKCVSzQc_RvcMTXRSNOt2ey9I5agiXVVQHTcuw0n4tHwakYa_ZeC5KJQqChhUlv0U_6l9sAZIRcjngg2nZrkWrhYTXc22U2h3qo2nJDK6oZf2Z2uLx5gzfuX8cv7P65Mdr4dnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=gvdnNkiFvhD8MN4FfMtc1eOrvSv95TOH0zXKHFPYEtCd6n826i85ry5eKIrzzXBYoM2BM9pKG2FfGNHX8ghXLEGTJ-JLq0o91KBG6z4U0hSzmvB3tqMOOsA7sv0xWLgxKGQZiWGHkUKUWUSJlywFLg5N5yfXC5KA3S1Rd-Q7BOa0xR7RfY1CtEtHrRDm_owUg45k0nAzjjL3Mo_YK-sRe8iBZFzc1DOHWq8Ts1jPVfK-7868QcKoCMY5P0fU4xM8740XySMrtDTz1GnFAgnSDXCTSj8oHeHq8wsa_Xcn4bthtRDcMF_C8T7nK2ti1zFczECavV0DCto9KjP2lxsZsbUvFd-IiF3OpIPYOGEIS-HeLRQVH7B56uFHA5jgetJ-ywmRJP0Tz3eoyoumqVkHf_M4Ynpw5EzGucMrTieQPc7I7swmoSn0DAMx9t9qtF8uUEH9quzxxkIh6FRIGq1rs_Pdbx5uY8PFwVVrjvsKj90_7vi2jVM_ckbISHrlRxt_ZMpc4FSiSUSP94_LZuEnLtK6Gt2Er_XFwKxS4jKCVSzQc_RvcMTXRSNOt2ey9I5agiXVVQHTcuw0n4tHwakYa_ZeC5KJQqChhUlv0U_6l9sAZIRcjngg2nZrkWrhYTXc22U2h3qo2nJDK6oZf2Z2uLx5gzfuX8cv7P65Mdr4dnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snTQg1xEOmMDKP_YGOYc8TSRHd8mfw5yF8G_-XDmnBGqjV0D7DQ2Xa63As__6LHDx5x3ogWsmZyFoikyD1u_gj4ZZlymUBUeOkvQCC70IZ5EXY6Yk4Pc-ZBHLiq32o01PQSEbNindyQiP4jrLSenCtDcNXznVuAPUsrt6ujfy10yJ7dY-bWY0ZpccM_wVoz2VHL0mx0hgI9Oy7kvOlOmX3u836vTHO3-w_FjAUb5E4WSOhoFf8lFSuicy_x3soGCEhlp5hh0oKKvFXHiFKUSYqw6Ifk2eQxzgqaao3B0W1pil4_7bvV7Y7J2iioTPgLeRRwPoIWBP8xf5mbEC4o5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snTQg1xEOmMDKP_YGOYc8TSRHd8mfw5yF8G_-XDmnBGqjV0D7DQ2Xa63As__6LHDx5x3ogWsmZyFoikyD1u_gj4ZZlymUBUeOkvQCC70IZ5EXY6Yk4Pc-ZBHLiq32o01PQSEbNindyQiP4jrLSenCtDcNXznVuAPUsrt6ujfy10yJ7dY-bWY0ZpccM_wVoz2VHL0mx0hgI9Oy7kvOlOmX3u836vTHO3-w_FjAUb5E4WSOhoFf8lFSuicy_x3soGCEhlp5hh0oKKvFXHiFKUSYqw6Ifk2eQxzgqaao3B0W1pil4_7bvV7Y7J2iioTPgLeRRwPoIWBP8xf5mbEC4o5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7pO9C6Vy5wh1RAZZsQ7TkkLiyjmvS6y0LgXqNQDVDDR2lsQ2atwrM38hAWgt3fja7ChwOEZMusFNI2DyAZ29PckoP-HPfPTzC7JClKvduWOFFcq2Ha2FA8K7SkSiJu4ssexA7vqLN1Rw6cSwFGOh4tJKRdLDrvUAwwbIL9W8OBIsQxuUOdY-VShg6qM-4kekDBy1cb9A-RVg5uNIaoy74-V86GOwf9DdJlrR563tHU6KDgWR7L2rF5xI-okIYZ32fYUo8zkU52uIJ4_TPwjcGDYPJ5y5eA0JVhcSnj9YYJEKdFhsz5brYCCPV_wYQrzZW0GYkFoSMgprXGfoY9sWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5yM98r_zQQ-bbLxbzN1HGTu_SObltq-CCkJL6LOl9ekUEKnN51ZdBZehl8fVYtjwtRkV713bxlyuvM1s8AjoD_XJds6MDrqH3fWUL276w-dOGOPphN8XzIee3WdzAsRxaolKKkAr8q4kO2vS49GCUU-hgvysp_Yu2uz-hjHe6VJffaDfvDU49uL6ojYORk8LRvrBriXOgbdm58ErZrUsOMj_z47cPigxKqxM-l6PXzktKTFR27T7VsWJ76tg4RLlIhNfbTn3_bZf16ex0b0KwM7eVwO8d5CJT8tIBxOZXQPnshyUCCL5a0qQyCjhS3u1cR968JBBM1xc_pVfM2jrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aSuTTPo9p6466N4lpfDS8y0ZkbXeFN-NmbqU-99Vje6Dg94N2NOpPxyVJqh5QsbVlyK5LrFcp7MEm4Mtk9HZiVmEPAYBH2G_Wbk1GX4MBGcwnV59ik8Z3030mNFW5PiLgcCewx_i7cXwDPHVJAGtyBlQMsJEaU-wsDrQCCWEAMcMEhDFAXBWSo1NzkXjFDQcDNWMEaBlgG5mTOhhIsmc8z6MI-djxh3ArmiaH6EMjvjcXBT4HOisn0BS8FfczKaszJBoJoirpOpSNPSufnX_SbHoFv1eLnEjha7BdVj8OEdV9YTrfD1j73wthwMP0XNjiHaX8d9GiyOlO5MBbRlqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aSuTTPo9p6466N4lpfDS8y0ZkbXeFN-NmbqU-99Vje6Dg94N2NOpPxyVJqh5QsbVlyK5LrFcp7MEm4Mtk9HZiVmEPAYBH2G_Wbk1GX4MBGcwnV59ik8Z3030mNFW5PiLgcCewx_i7cXwDPHVJAGtyBlQMsJEaU-wsDrQCCWEAMcMEhDFAXBWSo1NzkXjFDQcDNWMEaBlgG5mTOhhIsmc8z6MI-djxh3ArmiaH6EMjvjcXBT4HOisn0BS8FfczKaszJBoJoirpOpSNPSufnX_SbHoFv1eLnEjha7BdVj8OEdV9YTrfD1j73wthwMP0XNjiHaX8d9GiyOlO5MBbRlqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=GA35H1L3O8qRe4EJ2C1Z1gvdG1LN5a7FbyB_Wrzts3jlTbaNGp47kwEmUnjc6sjx6tATdWfdIQpaEfR0xrZz2C8oj-B6gh7kwTkoh7jzhq8xKaOSwP0nsu2rBOj51As87UuNNf6FGzh4hTgylKViX-AlQu6oGVUCOASkBdmgFMduoRdqBssHciYuIMXFbKKMk2lsDCoWejcdavkvQ-rm0UnraywIoGVc83iDUH0VrWDteFEzCCuVXNUvW29pAWHhpNNVomhdJH9XM4_rSJOyiQvGu_JZ0cPpnGuMnWXgU3EtpB4qCH47DeXUFsVGqjcNE2EFD2OvLIMs6gjVBnyPkD-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=GA35H1L3O8qRe4EJ2C1Z1gvdG1LN5a7FbyB_Wrzts3jlTbaNGp47kwEmUnjc6sjx6tATdWfdIQpaEfR0xrZz2C8oj-B6gh7kwTkoh7jzhq8xKaOSwP0nsu2rBOj51As87UuNNf6FGzh4hTgylKViX-AlQu6oGVUCOASkBdmgFMduoRdqBssHciYuIMXFbKKMk2lsDCoWejcdavkvQ-rm0UnraywIoGVc83iDUH0VrWDteFEzCCuVXNUvW29pAWHhpNNVomhdJH9XM4_rSJOyiQvGu_JZ0cPpnGuMnWXgU3EtpB4qCH47DeXUFsVGqjcNE2EFD2OvLIMs6gjVBnyPkD-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpBmsL1AYbN1_zCpit5EPyNHNg0kBftMAn8NRhXCIZYpXh1ka3Ym_q6rjQ6ptgA9ndwQVCUuisLttM8Tl-9mzuxTzsGHfzr6aDlQynsrnJl-GGce-STpiNxfTJ1M9lZwzudNEOceZgKZb-VcLZgdACz7rdP-shsAzCQjCHqFm7pj8giN4K--FVKMTRsCK7fdZZ7YMj0onwxvwis59FA5o8uTzLiyvW5SRdzfi0CNnMqXiMSJsoACRonYKvLLCwnJ3klsXXf2hU1nJiMNd30Yko9Sw_26j6d6vqkoD2hzaW50-3hOQMouzAu2G7Il6rrPiOPHFsyyWEOALqvstGQI_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiNqQw9xOb1iz3_Gis66aJE5ruOWpMVC_3esoguTODuQLZgGE-zfanC3h9GIDaoABCcZk2H6BeV28URDkrBkKMRy6HI4Yhid3n07bj5SUN4lGYYceOPMaT8NH_nYvAqCB7NS4KqvlA_3AK2e93TaRcqVpQTWqfvFJEiDpdhbsMHpe2ZSOvF-21Xidl5vQo95uCeRAZ4i1KBOyjNqtMbXCa1QEXHXTbHwo9naVD-gugg-f6Orw8qI1IUZprgLaC5hsO9ojo2JuNjb9fFtOK5bl_bh9baGck9S0hpiAmjOfB37vne6jWoVsw8E8J6xz2FrkHWliprhLXdSBbNWXltAng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=WBnt1awTpwVBXyZOswvB03XcW9nkMS35ALX3VbavyEwUJCf2TTyFZLjqQHPpg-F370m0h99WF3FDmMh-LcBI2jwOlzTnhKPZp5JfW0msKMoK2B4_QTV5qebIOdogSbTG4JX-eelokQADJRyHx0VzpM_Nj9pQQYpmk0re4saWBwYJ1-NqUC25hR9zF4GoNib_2y-s-t_xAzk2c-Ya4PXDemBemO_iLxqpLQsBdXpJiiUS76fGHxLjZnZP9uvG__baJmEaEh_PMezGCHA3TUYa5MYj0wpf4CKAIHqs9caGSQFDLQDvYEZyMGxTravfFBauMBKG9Y9qFfokESlEbyOCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=WBnt1awTpwVBXyZOswvB03XcW9nkMS35ALX3VbavyEwUJCf2TTyFZLjqQHPpg-F370m0h99WF3FDmMh-LcBI2jwOlzTnhKPZp5JfW0msKMoK2B4_QTV5qebIOdogSbTG4JX-eelokQADJRyHx0VzpM_Nj9pQQYpmk0re4saWBwYJ1-NqUC25hR9zF4GoNib_2y-s-t_xAzk2c-Ya4PXDemBemO_iLxqpLQsBdXpJiiUS76fGHxLjZnZP9uvG__baJmEaEh_PMezGCHA3TUYa5MYj0wpf4CKAIHqs9caGSQFDLQDvYEZyMGxTravfFBauMBKG9Y9qFfokESlEbyOCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd2pUs05RVTwLYZSQC3MqcQYQ4Mz56AyGkS2xsaW8_8ZKzaO-S14d3wVqfne2hyAlQ89ajUX1XAnTL17thfYuU9dOLQQl20POle49kY1hgM018RnyfH8i6vX6SQGs2OolZ1cjWnh2LfDWPh1q40D3h5Im4I8L3lDEjfssOSW0cAx6quoxVshEnCVs4CFVMwB_az95xRQcOlrPxuR18BxLxVE2evjt5Ld9qN7P-d3zC0V_qXCyX6zAqIm1SI1bHb68lW2EE-WNZOE37IokR3welPstIbOLSI-8ZG-JcaCyWOFgKxLLmOaCvNXqaruUSnjHEtXYVc7gDRZctZSx1pOGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZUBeeScfCYp5LckrCt9Vnleftb7AnV_ggYMR-cqQMwQnpqgm3P1LGOPUWifZbug2LqvyYz7K_FYM6dquxlTMCGsFm3T1YKPhpxzauEztCs-AiJO10wr2pFgM4wCDKUHQ6CHk10IcmWHld24MZijCR0N6SMWDR-ovrDgLGoD0Tyy1UNTL25hwXo_uB15q8yJE66_Gz5DO-B4-f4JVjaKRHxigIPC03c0s32EeZ1z3tg_2CETx_yKCZQiKlglpfRhRuHcpSBA1ypV8JRlfSbFlEeAXpd1-ezAzWVbNGE18e9I_IO8sIXt8Pkap5d5FCp0qL-khFGZDiO6gm292bLWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wrn8vVxIOIDIWhbhZYQ9YeJ3ePCkUtiT0FPE6zgbVY4NbaSjSq4gO7D1X1p4oXpk8kmQDoQOobiIOv72kKY9xT48hmUd8tKcGSY3fgyznVrNblNwt0mbHKv-azA3N_dutxZoNN7yWX-16w0oxx0ujLeIBZyIp1e2nE6ibX25YVmpONkD57u2Lt6eryK1OH5YlAg8Wq5kSC0y7Yn64RnbmbHM7TsVINCZTt1-1MaynImehcvvnaGrSGt8rDn61naDHXu0wwr5K05xL1SUwOOQ7HmWXSYzhF_814jCM-y7vQYcP9pKd5vZPT3OndpBnlQmFz117aid04uzRntopmNWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLVMqz1rMtJ4xUunWu0aLGc7RNxZgxOE7TIVl01hBdDd4CRIiSmW8LfjppQvmB-mhewvdftiNLCDk8LJyl4rEtl0DhI5Jx7kR_4zgJcbyVuMsMiAxyUtKGilTq8HYyi8RVWXHTEtbrOnl8jiJAm4Jrndre1B7Z1mjqmV3UdNK0C0I3SF094RdnBQYHFi4tjFUEeAVzT-eidYm3V6QbVGN9AktnNyYSoCBYT3ITusDl7dE3q_SPuwf_QxBoVfJEyArGzEY6vhCsCft4iK-8f4kuqGMjFoE8Bo203k2PL816MVuAuXgMEmKyV65YpJD9rowdShMPlgazbmj_iOUL0ExPqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLVMqz1rMtJ4xUunWu0aLGc7RNxZgxOE7TIVl01hBdDd4CRIiSmW8LfjppQvmB-mhewvdftiNLCDk8LJyl4rEtl0DhI5Jx7kR_4zgJcbyVuMsMiAxyUtKGilTq8HYyi8RVWXHTEtbrOnl8jiJAm4Jrndre1B7Z1mjqmV3UdNK0C0I3SF094RdnBQYHFi4tjFUEeAVzT-eidYm3V6QbVGN9AktnNyYSoCBYT3ITusDl7dE3q_SPuwf_QxBoVfJEyArGzEY6vhCsCft4iK-8f4kuqGMjFoE8Bo203k2PL816MVuAuXgMEmKyV65YpJD9rowdShMPlgazbmj_iOUL0ExPqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHblAJTCg9kKaco68U_8WhfUVQ03yTSGaUbF5d4kH3SWaSSqdN-o70MT9bRsYZk6w8PQPLl4aR8JmE6AyOtBKv_5cdvYatRF7FikxIe4X3MwKXtK16azogYQPWrs0a3U6LATkZvQPQ1EUehbFxBVF0s_mMh4ZoeWIPy9Fkf_oaP6kedpj0MfFRvzvWFYZaUJhMy2AEHmb73Lo2ith8K_vdaNAMsezTIwWAYjXdfXA_geVwSKdbi2xcJIZbsqqCw8izLLw514ZUTZaSR10fQVOWBpBrbuCf0PTBSIAK6bkGUHfLZgQ3ZTRNDz5qkYKXbCOHC_LMQxLOB7U5bqcCPVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BY781gqMA9H2cl6xZgvFVfx5GGsqxp26acILVVRuU7-u0u1OzWYzxzRKuyYC3PT8TeHA_GvQq14fI_EEhjD4ZonJjBH1qsHe5vMfF7AjleG4wP2OYLBevYDeAahgxn26eD2ug3cE0sPL4UquQU_bPoQOop-lvVtF8EjoNgeeZ3AXzqngsO6LnlmsPJ0KWtzbeGcxNbGazKOIK0oUaYl9YblOmCe6218RSsyTH1_AWJVPm51ct0BgMO3BiJEjVAlejBSR_q012_7vY3ATmSVqTfcohro5dBO31XtSYnLLUvtgGqPNBgwCqlXXaLMRfasTyU2YzesxZSdHZEIcO8vRhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=YYJqPElMJ-Lr93RwGpIuN_Td5i4fJqLDv0HIVXnZ9gs2GrWB_TFyeMFJP0sAzPlXjIZdyfzEQFlNF-ZbwiFxqubhOFj1Qu3R3U3Uq5SWZm292Uyqol-5wTHTxdNaO1UgiJUSSBTdhoE7N9EtiScfK74E-v4LgKvDf9lZRYkTqKxSYJSzOqn0Ynd6__YTMxkUqkHf2ZQOlcrI5dkgVPwFkyJkutbSrcFTYmdS6GsN9JcsdSNxll5JL_yypAZ-_r5wiBZNt73iDJk09sV-Jn5ePuOr-7qNhK-XO3Q1Vxv2GqMhVB-01PYv3ZdMHoFTLcKNvqO9ngqdXU5Rx4_Rf3KbuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=YYJqPElMJ-Lr93RwGpIuN_Td5i4fJqLDv0HIVXnZ9gs2GrWB_TFyeMFJP0sAzPlXjIZdyfzEQFlNF-ZbwiFxqubhOFj1Qu3R3U3Uq5SWZm292Uyqol-5wTHTxdNaO1UgiJUSSBTdhoE7N9EtiScfK74E-v4LgKvDf9lZRYkTqKxSYJSzOqn0Ynd6__YTMxkUqkHf2ZQOlcrI5dkgVPwFkyJkutbSrcFTYmdS6GsN9JcsdSNxll5JL_yypAZ-_r5wiBZNt73iDJk09sV-Jn5ePuOr-7qNhK-XO3Q1Vxv2GqMhVB-01PYv3ZdMHoFTLcKNvqO9ngqdXU5Rx4_Rf3KbuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=JldWxYU0iPho9qOnX8A0zEbGrRJFcjbN5XGCXJ4ofMTCHdYS4ZxhlYE7RBjI_pPdln7W9ruob366TTRa-UA-o8lT3B430DuxE4sh1IhptjyxEguvzhPy1Sf077SYL2M-w1fTuFXF18pMjvV3AQGvZmzrBhFBa1tNs96Z5DxFF8Tz9aWTJCfxmeKIgcw9VTmuuX8KGafnTlJIY3qNev4we-wtVzVf2fi1YVR3OvHmHBAE-kc82AdVFOmYFpUX40yTX6mM_y1QizXsPXTnWhJI5ZSHiYD_ibVphegIDeWKpiSsXN-AWJAn-qqjSvm_VknkL2Kmhu26JsH20DijXuaSIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=JldWxYU0iPho9qOnX8A0zEbGrRJFcjbN5XGCXJ4ofMTCHdYS4ZxhlYE7RBjI_pPdln7W9ruob366TTRa-UA-o8lT3B430DuxE4sh1IhptjyxEguvzhPy1Sf077SYL2M-w1fTuFXF18pMjvV3AQGvZmzrBhFBa1tNs96Z5DxFF8Tz9aWTJCfxmeKIgcw9VTmuuX8KGafnTlJIY3qNev4we-wtVzVf2fi1YVR3OvHmHBAE-kc82AdVFOmYFpUX40yTX6mM_y1QizXsPXTnWhJI5ZSHiYD_ibVphegIDeWKpiSsXN-AWJAn-qqjSvm_VknkL2Kmhu26JsH20DijXuaSIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiCK0aqJ9INaUiPpf5PF2d8JpLvfAolIw9Rqn1fBwSCfrAI0d05pGsfJspANgDnM-qK_yDhjC_XCcqOhHmf0P8qMAfCjv7nclFU-LDsZYW95p-BpjfcFcRJaV2l_JMrFAo9gOjidO6kUMcFTtIpc_3mWXVvgJKLB7cR4Ed19l7J_nToTsE0rDE0AzEzlxc56Edr1DO2biJZWPADVvPokqvIDNu9PC8O3fw26-wlwsmaBE4xPraZTL4LzPEjCzNJRPw3cIHfdn1K8bCD9WTHU_cYoqSblzsDx6LbjLAiu0VpZJC-hM2HvA3X3e_Bki3z85EGOuhEMu4uWpz9CCa2qgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR9bYI8JHGcJZvsJ0q2G5CE3bc0mmh_dbe6q2hEjXfsPZMiSboXcxee6t-MwQsPYB6_yauEqc-zu6pAjQgizpXlNkzu-a2-PA8b_m963B1XUnPPsTdFincb6mi2NKFzcvjrfEjcLNO1-MJag71rwSCoFZcymKMdpDB474C1atXu4f0IfgXr-_8cMoiIUv0ZHpXMp6ckFWYCGaFS-gIwDbFqx-YLkKdm3nSu03b3ouuq5YypipF9wlOjLyuii1EeioqalMTG2VZhqaGNOs9TFDMOcbBy-GQ4ZbJIRgx8ctbliDbAvYuXM8KiJYrMvGuV-adQ2iz4uDX6nnccBNqiRSA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ag1bjIcJUW6zBOqbAsbr0375KTzH0d03yo3UgtCY3wAo0vEGGbQ0GW8bYw0cLxLDJ1D6bkinswsqUvGlL084z8oW_8Ok4nV4ikoAOHYGMY6mFEWiiOq7QBUR74B_xz2z3S0TB0SMuYx-ssF3IrxuSuOSDEsqjyLOIzoMzNgQUx5n8NNa1UgKaAazxG61BPMUN7_sSnZ4cdOxw0ESJP4kU8Gh6hDuUOfcXAKU-l_9L0dbyvdrr884OpdCy0fI4pVsx5agpp__SkSqe8TRxdUYAUrytk-ZOCmzRtRIFJwaRqSC1-lmxY1DlXqsPDaEtaMtw4u5kBBqGu4sJqRVWpiKcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=Ag1bjIcJUW6zBOqbAsbr0375KTzH0d03yo3UgtCY3wAo0vEGGbQ0GW8bYw0cLxLDJ1D6bkinswsqUvGlL084z8oW_8Ok4nV4ikoAOHYGMY6mFEWiiOq7QBUR74B_xz2z3S0TB0SMuYx-ssF3IrxuSuOSDEsqjyLOIzoMzNgQUx5n8NNa1UgKaAazxG61BPMUN7_sSnZ4cdOxw0ESJP4kU8Gh6hDuUOfcXAKU-l_9L0dbyvdrr884OpdCy0fI4pVsx5agpp__SkSqe8TRxdUYAUrytk-ZOCmzRtRIFJwaRqSC1-lmxY1DlXqsPDaEtaMtw4u5kBBqGu4sJqRVWpiKcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=HszTdKj5vlZsuCqrM-PI40IdK9qRHc_C3CKCVl3e5SW5bwYHOh0WTUB46i5Sq2nVt78xZdnKe48H33x5qU6r__4hmp955eZZiCy96xRPr0hjLX0I796tStI6C5XPMUg1GTqznieqJ2hP49ClbPRRMWGXMHhAQ3bKNp8dXfUEkuGO7BrwJjtov2k5VdLzhFUnrTLeHsbPoYkLQz6A3g8QlIYMZtl4_yxQNpDzQPree1Y8gemiXzaRwLBgTEzdusNrNz-F-gZv3zpPFu42WH5taaYlJOXz1v8oYgKLrPR2TeyxUvRUBjNoZhXvDiHTZeT4V7rNBAq8S2BSkBynJ_m8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=HszTdKj5vlZsuCqrM-PI40IdK9qRHc_C3CKCVl3e5SW5bwYHOh0WTUB46i5Sq2nVt78xZdnKe48H33x5qU6r__4hmp955eZZiCy96xRPr0hjLX0I796tStI6C5XPMUg1GTqznieqJ2hP49ClbPRRMWGXMHhAQ3bKNp8dXfUEkuGO7BrwJjtov2k5VdLzhFUnrTLeHsbPoYkLQz6A3g8QlIYMZtl4_yxQNpDzQPree1Y8gemiXzaRwLBgTEzdusNrNz-F-gZv3zpPFu42WH5taaYlJOXz1v8oYgKLrPR2TeyxUvRUBjNoZhXvDiHTZeT4V7rNBAq8S2BSkBynJ_m8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdOdHCf5mRUiSFZgr1l7-f9MVKJTZtz4Sq1sUPgoQn9or6OLyREWQjpIp8S-Nl076v4FEzhA29T5LOpPzhr5M0vD-lVsL5URNpThtuk6LaonmSvGxpU_Kw2-zRJ6o2V749MOo6MK96Krr65hAe13ws2Oo72PGVMhs0Ce5-3pcpL0XmTDSyP3oqgnfU9Xi_2Q0JW4gu7W_ZVnCNy_MEvdymi6wG9V32NCNRkbihIBcRpoHnThudcfsMxwMRH198Rzaa0qq3M9bQ0Llio7OzUIrJIjM5EFdLDhJGRPtwwNxzTEM-Kv4Db_kGxttWoASRqQX-afP8a-gh2S8JU04VH9-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etVVHawtiSi4Gm4F2tabXlzfMWcSHbdRJ44bS2J21tXb5SEwPk9SGilKffIpctrkgvsQuGZxnQ6Go15QmhUnq8WevhJbNwiPPhgNs0FzhifSFcf8gH7LrTvSulN8l713djEetnYvJBXGzCHjd4UO9OEUIBhYLFNIU51RJopKaFUw9CKaJ2d3phoS8oqEqovdD9gJHklsucQr1n2_gYEnfnusJ7G-2_QpuZ8Fe4jmj_5nQs5746pBdqSXzPs-rCSub6O7VCS37RI_SlKtr6yjrhVTGY0EFsI6NVTImsDizga-UI-a4G7b6lKZZsAgcnLOWvu6EhDi39n-QzoQFzHG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndN-ryYfRKymyQYSWylDCwv3q9tEi92Dtiu8tQhtZVQrM26FHoHOSFH2cizua_ViAYTX9RM4fMIK8de-WIKQQgZoLNVGF_rhbRRiVf0ZQisNVw7ofD0tQZUobnhTlbMSphmvFGzFbolDk32afayFk6IU0cjvGbTYq0Gc92uyP8UggXIIq51AlFcDv2W4YQtLUNGC4Uu2t20LZUK4-O5AO3kka07Q5xkYWWA8HRNjCM4jM0pdwr9TVLVv-1S6OEzT70Tdqeioy6NF4dEpZN9yxTtqB-RrCQB4iQG78FVyH1YwnRhJHwdu9RdElszNxDf64lRvmBQAMQHNI3S_-WunaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9jQJgklDf5vq3alsvZykXS-gnm6TugG2dST0szmfEsAV_2Bh-b-C9vA1UixGw4mjFNeE_dDvLM-nqTD4RmY7ji49RVlLwDT1xoeykLMyls7lnZqLzuGWpM7fsMXHO19HqzsciiW8KKEATlr9R6Azm5GmUInz0AivIzyBKffCu-7bkiSPfruocXUSQaXh39LH26awF9K8My7B1Sw1zFtxeV6hqUl1ewLekBQHsPI7AAPBsbreOt76WEZvWoE9YcGO7x1Xl4f_13lG9PzPNewj4nC3qgpInFtT01boECiGXD5zMR_T6ZDBLwr7hYrKP_kOVLPJLMGJUpdUvPADNdyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L70Lf1iV0Rgfd8lzeJyDwMiTfC0NPXUz-fUTBosSNUR7gahIOrqdtBayejwUcS-RdkjpZ_igSgwk-I9KTaLxIE-ryx6YOkIB3JWudxSdmMXVRmHziwRth2u5tmni4mPHBfWP5NrAHNH_UeVsIkwj_4jL6mmQ73kok5N1u90mSilHd5ye7XCcRzJ_qWPFJqHpU90EISJSwkaXejvr0IxItLgObIcOaZEN1TNe4931GlXpbhaxLxW0oFF4MbuiPcfjlwIdVgOYmH2pgUKfRJaoToPP-c0HlLTKkDVkG1VFpMm0TdRjIBYExBJgPV2tDPtWRoXusXSVxQ92Ndw43BPPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDnEbaIsYp_jlvKLSuYct-3Pt0sNz8U6kTrwjy4lQdQ8cqQY47mOAotHpH3fTDH2hHQjsW1hOlXN3rU32fUKNV33jivVyaPG_X03HEKPH9RFLJD54oDPnLlQbEputbfIxEjyrYyAVaoTVJ-CvCBNv04hzstbRkomSqeurHah50KR0nNNVAj9MBb9fIheOKVPzUEjbSWDjT4a5lg1HkhHFqoax5v6wP9xzyXybvwe6tpnEWhYaqoGTNjrJDplvhlNPfVKAwuTh96wV95oMQwANTFRQwTZszWWZ79ocZFRuLxosE_sccd5lrKsa4WxmkGelbYKXb5P2uYakjwjRjDhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUdaQfFBB44heKV54dVzyyUFMqMpspDtpfBfATqRPFg6_1mGGu84WKv4lGMrw8Qzqxew3H0CHh1s6V1-9PUlKquRY-YVEno0fLUdKEI91ueG9vAlM099YK_oEGZRFCk1dXA_JTLH7YacesCPAwfBSyYeNJBijElylSzKrgcbo3jLZHU1ejL-nFYOpKE8WQ0A7G9h-VAl5Lq8X98MOTQaVha_nkoRD2d3InpW9trN7krMMojBjN6hYqPPHHUrMkAl9sH5lSjS8Lpy9XUgoBTTyhmGIyl3kKSS49LuVP2Hoex0ruxiaVuP_xFUQ4N_yYy2ERl615JlEwCA8M0870jbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp-QbpnPamauiwP3r3wTwj9v6vkvvJPMFoRFe8wykGSghMtUY3T8tlpW8a1V5v3lhdFan5hpRCIbfjuvHXugVgP7OhULyuWMz9GrRaYYD8zeIIjP2LPGohhUPLXS900r-BswIXfsF8MeQuUOmcdFxqAfCP4X4OIFvAKf1X59vERMaMbUgIS7pMzrhOHBTzcXfgEkWtvEeH9CQBOkvzZdcV7HtPNwb-bnqVZOXpzRL_gEukEOAiteELLpHNBnT0XCeF0mJ3KfmzCz4Su9_Gy885Tgxwdijf7_cmnCpsO9m5-AhfrgSz4BSq9xZDzJMUvut9yYm58NyGn8gv6a0WB3-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJcWYKPqZhlTGsAdXEQxR-vB9BZpH-89UwNiAr0dhuXtCm8NOJmTIf5FvfKTbvKQi56zgLVR0L4bgUXUnCruLv2CNbHdXHO1TLR3a99N1HAK89OE-Dxi91ilBAEfgUGUsGKoEiADIWerhjp3dH4fgel9sV8tTie1qDkrLzIp4jJQqy6CGH8VsJVKEb48Bk0V7l6DawlwxZz9SQ5uqi0j9eq9bhcm1QQ9i15MTuUBLHAW_8p9bS5XHXvk-dTTcCMv27nS95d1U2sYGMjNzK0mpeSIG2gxEYhc9bWmtJzPtxlMj2HnU47Z-WZ50GdZBpET1FpU_QByYY-3LgcFrKAnmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp_mth79imtgJ0xQWCwdiga7aeYQbvgNzUWo4674uoiAH1MxEK5H6eeGjGCu1n52RkyZd33xzjOuKK0cQnJi9x085BiRacIfJdc101mL9X9yBVZhVQZhvV7IdA3Ji3ol8kkJmebFmYdtPpL5uQxmDhtXziwoZlVh-I3F8GEk38_9dKQVTRVwu4XwET_WEM21d5hteClpIIL_MsB_nC46-rEleZLY-qXi5kc0Y1qEZWOhK0iPy00HqNR_te9fYjFlC-8u-CgNdFJzwHG7NXCogSWEEztiV_G5AbkxSNofuuvl342Ri3U0yK4pIKMbibl3uqD7TGQ1ZY_EoePo5T9LAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=LLYM47OLcS6dn4MAD5FmFrqR5ZROqeBXIQuOivsN5ywjEwZ4FIagdvJv1jZOVFLumvairaP0OsSStAEouMcvLDVHXjQx71qRKLRAlsM31HXny1hfPOyOiSUctWGRTfF_W1pk42XAFJyfew2hOGccS7IjNYDH5LXaPNE50Mx8KGMCCLjcAlYeDMuZTszNFtD2_6MvSss0mIQO7gDMgY-XooOBX6dvpcJl5gKJHO0-D4zFItmh14dLhe7bFMs2m0hocGHMqLj2rd4laeHhcO93Y2PXl2TP7CzB469fA4mZ_TbkmoEvGYENfx_XHeYW5tarWHv9CKfBt1nXjre38dlMDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=LLYM47OLcS6dn4MAD5FmFrqR5ZROqeBXIQuOivsN5ywjEwZ4FIagdvJv1jZOVFLumvairaP0OsSStAEouMcvLDVHXjQx71qRKLRAlsM31HXny1hfPOyOiSUctWGRTfF_W1pk42XAFJyfew2hOGccS7IjNYDH5LXaPNE50Mx8KGMCCLjcAlYeDMuZTszNFtD2_6MvSss0mIQO7gDMgY-XooOBX6dvpcJl5gKJHO0-D4zFItmh14dLhe7bFMs2m0hocGHMqLj2rd4laeHhcO93Y2PXl2TP7CzB469fA4mZ_TbkmoEvGYENfx_XHeYW5tarWHv9CKfBt1nXjre38dlMDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=ddI34cbYWnRt-rkfmZOupffFm0bd0JYUKklzliFdxE-py3yG8RV0uKW7YIOhk2-L4pkmN4tHoz-g7i2hWDl5_npp_qA_LGdqrOekKO0VaDmzxntQypEM6MADSM8Px2W2JmB1PCVyKy-XGHFWglMzsRv0ppV65vGrLb7si4Ua5e1Gb9st8wJWmItjZq8hQXWNzO0M6dVak2q08i4UrL3Rh8kjoIYnEWVb4BWmKgUm7aOWaXrekmujSA_irDogCefoP_QdLyJRsLM7OIVSiF_8j-AIaL95y1jnQtkrKgcFuOPHPMQ1zxFTk9MSjTMvV2N0mfNOkLodg78i4KCAF4yIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=ddI34cbYWnRt-rkfmZOupffFm0bd0JYUKklzliFdxE-py3yG8RV0uKW7YIOhk2-L4pkmN4tHoz-g7i2hWDl5_npp_qA_LGdqrOekKO0VaDmzxntQypEM6MADSM8Px2W2JmB1PCVyKy-XGHFWglMzsRv0ppV65vGrLb7si4Ua5e1Gb9st8wJWmItjZq8hQXWNzO0M6dVak2q08i4UrL3Rh8kjoIYnEWVb4BWmKgUm7aOWaXrekmujSA_irDogCefoP_QdLyJRsLM7OIVSiF_8j-AIaL95y1jnQtkrKgcFuOPHPMQ1zxFTk9MSjTMvV2N0mfNOkLodg78i4KCAF4yIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fCgmz5ufWU1a_9EFJqxLJZbEUsOXtfDEfaQqkgUuHQXliuiIzD9KvoIJvqyAiwuXHTPM5mDEdg0Mdpv2dc49Q3EU6XvAGSjeyZNumG0iZuZwdQolK1D1iHRVcSWBr8MZZkW7FtFFDMQz9l8J799PVEpDPJoFtHqpwhfLHLS5lUfNEY9gR8xSI5p7n09qsxvCDCwpeMUNzKru9xPNmW5sIF1kaX7sPr-5jfnaLsYhUTPmwofz2lQK-EYLwGLwb8tlatLqnG4xBpoiLdXF28VmkURNmLnOnD6afpJNEa7qp2G8mD_0stUozsbU9gLfiha_iWWxToHy0H1m-ZvNVzre_qFEafae-lIUBNMTyUCTgqMi7FgTRKgdZlgu4wGnv16lZz8nC2awL8oGbb_5WQfWZv3t5THBTkHj8MZPFnMKFFVcHQPtN3gKO-mlVjsyXU6IQmdkKNMj_cdtHlvfpsPbl_hLi-xeK30ltp_lB_do59WLuNhxvMMePcgBTujlVLQja-EbIQQgoEzFeaJnM0ovo3G9hyUwXsYJz22VYp6lG_Ja2COgGAD_ItnFInGcTqW-q-T4gMH61-fjhyYp-UBmL08SpNscIiU3_ctqWOzJa7AEHGoCF8c-ck-XokIyEnWhI81UDlda6PqFyXG-tG4jnZ_P5x9vIdDfXgJwOiTt_3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fCgmz5ufWU1a_9EFJqxLJZbEUsOXtfDEfaQqkgUuHQXliuiIzD9KvoIJvqyAiwuXHTPM5mDEdg0Mdpv2dc49Q3EU6XvAGSjeyZNumG0iZuZwdQolK1D1iHRVcSWBr8MZZkW7FtFFDMQz9l8J799PVEpDPJoFtHqpwhfLHLS5lUfNEY9gR8xSI5p7n09qsxvCDCwpeMUNzKru9xPNmW5sIF1kaX7sPr-5jfnaLsYhUTPmwofz2lQK-EYLwGLwb8tlatLqnG4xBpoiLdXF28VmkURNmLnOnD6afpJNEa7qp2G8mD_0stUozsbU9gLfiha_iWWxToHy0H1m-ZvNVzre_qFEafae-lIUBNMTyUCTgqMi7FgTRKgdZlgu4wGnv16lZz8nC2awL8oGbb_5WQfWZv3t5THBTkHj8MZPFnMKFFVcHQPtN3gKO-mlVjsyXU6IQmdkKNMj_cdtHlvfpsPbl_hLi-xeK30ltp_lB_do59WLuNhxvMMePcgBTujlVLQja-EbIQQgoEzFeaJnM0ovo3G9hyUwXsYJz22VYp6lG_Ja2COgGAD_ItnFInGcTqW-q-T4gMH61-fjhyYp-UBmL08SpNscIiU3_ctqWOzJa7AEHGoCF8c-ck-XokIyEnWhI81UDlda6PqFyXG-tG4jnZ_P5x9vIdDfXgJwOiTt_3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es2cZ2Azl5gabRwY2m2vW4OfzGA6yIsJq6SbvNlpJ3MdFC_P1eeptqug212YE7HntYx_Q5TtWP-RdwgFtBW54tDbsQInfrPX0GIY8fZ9oAs84T22yWijJgWfDThNKHGa_DpFWi0m68M1QhKAxTg1lQgIlIXJMtn2qCSqY2Sk-MFxIAETmYkbJw_BdFaYNpzEfa56FxxBbBa9Yo-izjkYjbjwp5YijNMcAHyBUGOP4XkWoIlDo-x632oeB8C0XbPb0VhlVFBmmoGu7MAfHO55w86425xVDPHqjdh8alHqxfBZ37U9jg8yxOmAqwRDymFZF2w4gT3fNpglE2H9Bm8wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=gkVCpH12yGGS4NvuBKLH9XnCBH4v6e_YWGbVBqqDbNhlftqmGxA7GaF7Do0UMn2K7KOwn6cIkNsB_6m8Jy_rBTr0PGq--n7Vg1KyqBmpI9b8Go61TzUkWP1idhBl875H2xQZ6t2Rhr4m9bLrUKJXMj2sh_yzuMlUQ9Ue6gZwrXJVtcYlcZ1WnPBHJ5YHv6PgfdVf1KJznqz3XQjvSJGByl8DvQy1XwItDHg3Iadotr2xA7PgBA5QePyqRtnrCCDuyJW_hXbb0tvUq6ZaoQ5eOpJxgq2lmSpXKm7lr9ADBXVfrGHutUtS0sQC7zw3YlaE8zT9okLaMjJzdLYM73SaJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=gkVCpH12yGGS4NvuBKLH9XnCBH4v6e_YWGbVBqqDbNhlftqmGxA7GaF7Do0UMn2K7KOwn6cIkNsB_6m8Jy_rBTr0PGq--n7Vg1KyqBmpI9b8Go61TzUkWP1idhBl875H2xQZ6t2Rhr4m9bLrUKJXMj2sh_yzuMlUQ9Ue6gZwrXJVtcYlcZ1WnPBHJ5YHv6PgfdVf1KJznqz3XQjvSJGByl8DvQy1XwItDHg3Iadotr2xA7PgBA5QePyqRtnrCCDuyJW_hXbb0tvUq6ZaoQ5eOpJxgq2lmSpXKm7lr9ADBXVfrGHutUtS0sQC7zw3YlaE8zT9okLaMjJzdLYM73SaJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlTZJJOn9o-kfp8XwGCj05C3jgEON5xu4kleBUr-a50P8lsUMYyYCuMlKyJDk5CkAMrTHo2MgsLDDl8l0lDMUZ9wlEe1-W3erjOpSmH3C-1L2H1xa-CkdAEi5hxAftd55F6-MPhgS9MJFE9ryxvw3TfkAc6lqxedRA8lLNiCxLhoQr85rngaJVBoquRUl1AzCFcCm3grRpgCCMAN8_z8a3Xm3BC9zffTgYrCpJRbgAya5X3wTyHOclu10I8NovE0qOjh4TuV6PFyRxus9HhavhyfR-NX_8IXtCR1mXYLKVYoAuNerb-QxOWNIJ5NZLUSbitTZ9WKbz2n9yB8ArzjaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBgTQugmf00QHXHOthl4-hKnAfcrCJxwy-E0n0CN9Z43qCglPqB0KxIYXjsHKfoDRD8yqBIkk1XqMlVvHyXOn2TkuewbkZsrfF7CKMRrXB913dZyvJLDuBBcGM2mfNTaVGOv1wEO9D8W9IdtPlwXpeKZ6PtqMetPqJG0CBAa0GpSRskuyOHsKuoA0epk1rj4C9PH4XjMkqL6K4QVyDLS8fWYord39O2YaB3KI5M-mTaWhKeLu4yh3yFFTa53wKtiOkRKsqdI_2YDr9nlB1bRgyNzyf8X0tWXB9QGO89H0sW-C5tlRIi3SCymPt0AsWHjypsNjCiL1y-JBItuKrgGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrI6UVIza0a2t9umy4jHUVaXQw7XS8mFzv-NIKhJybA2a-h2KWE8wuzF001pLZHrFDNGenTNkZURtTFGtbDrWEuTKOkC0-Gn-7zkI9ecto0fuuwNmUKrIGYZdiG6N9qQ1HR0JrNNgMHmSP6BhzUiy6BponmsHIeCeZNuOhg0_eqHvJ7BeCOAiLkZ0nUM8gs33MjBg0_0CMCCa2pCKr77kANtZDwypna6ikoyZFiVYDsJ_0krKWdFPAaf8iHOdPydOv43eWiOs0mG4r-gjihn5-xQkLTgq_kNBJCNASV5N6udH5AtmjxN_04AMoPdkVVGhJ1C22eyTJO7Q5v9uZfsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgl5QWU_X8UDiNPzjm1dlm9RIW1Rl9taI9D0qPca7A6FSMRpjmL9vHmE4XYk1hazZaHzgCCvwWc-rqaJtdTb5YUfQhq2T7fFHu-wD1LyM38kIjOL4bEWJIa-1IV7iVil94ScKspHOw_Zjz7GpcCw9Yn3G5aMibLXMTLBvognmzAKNYkjn6bqxSlzIysIIKs0v8JhRtQ9HbYUe-K2fd5gDPAQZusTSkLY-PfpN3WwzB2zGFojuzJvfjHtbK5EWeYue9PmQ7yYF8fJlUTwMNHv7ubP8BZ6umhysUqQbFqYAeKmAUpv_u2CAC4labUBUo93-DRX8gC7MmuqCyloZ7Sb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkkXWlrgElTaH-3l3KV1SNALyh8jbWudC6zVwx8Rljr_pFqKSMHjQDxWxIWDhLxpR_ZsxZKlWjUFwQ2ABTLITVpUFg9DJIm2gYpWOia0ViVQB3XbN85C5jp8KY4u-hjfe7ukCOpH5Pz7TvDuZqyl8aDtTnsNumVrjfdaGtNjZxkxQkYOpo5SJUhVohrMA7uI2X7nw_aQ-qHt9YaUNkR6afBB9OvN371DlM3CUR7slCIT5l-T1Vrvy2kvPruEJB1zwIex-aiNZo8KZa4iYnDs7SQWAT1ioeWI9oXubsWO4KyOT_h8hTUab5vnhMfXThCXnrLWsOD2CD_rYBqVE00jPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9w2--L8yAM-bdFghGnKsYkmHGDHM0k0PywKG3R344Hw4Nlz7_zH2noQVqZr1mEHY9ydeTUXFRlAm3w6F_FV7MMNeVubOMDHlvZkpRjohA02tmJS9vCIFjOGWrJMWtTfamALHcuEcqDtfjse41Ho05YZ70_OoH36aM9XeNywu5VgPv885h5J7_Z6CHJwZaEY9x1tsAmaTuoH48-rYR9eSc8u1usB9n_avcC-bb6acWM4XbRBmA1Jobhi7nX7mkkFOdNTzy8wh8qVjMfq-jcGxDLQum-fMO5uEleAPcW8I-fbdHw88bLPTgY9sQZPahFX5ltn1IxR1MpJNLthT5mLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImKqhSz0Yu5Ww__UkQzLHjn79i3kqLCrW5qBwQp9uSwJSP5V9QuEvNJ5fBUwT9Tmh_S__GOESBVcDLanV8eXqZ7Z8A7gRMKDtR_xbSiLsgTBnMLdXZEC9IhoUx01bpjCwX8pnnDUygxn3y7ij1NBu3t-UrBEHxiEapYfAts0OcEa8P7IiTgVyz_S89wsPA1te53A72hvzFHWRRlid1XaG86LsEF4P_1SgHuhGB8C4V2wvPRqgo79ZHwb5au24X5IaIxU2fwdQqFcIo6NuE-eIimuDJ0Q-hEv31D5sxAZ5DJPOAqDalD9aZey4L2hgessrrlaoAKbltXM1jrsnXaijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVzEq6nCN-3ET3H81XPBbYQcliCcwRohtNOxYy-oZh0BoFxipBiyJuqOF6crBeslBcn6MbyUD-xW0IVfcWOW-Xu10G794ANoTbqwwgxU1T8jBWiCMFonmQfGsGBqWq-0Ms1FEe7GEKOLFGKLfSNLdwuCOBOZ8w9QQEOwHN878ZAkBJiXZ-C-eniAMwUTMWBL-1ROeFQ0M2-pvw_bHj_sQEISkkt4CSHC8vgOPJz3mlNd5mMw_iEyUydfi7NV4sn-ils8YsHcFvsEjK9unjSWMpfne941b7TKmwBnvuhH3MD02lx8QH-7C7YLrQllwE-CNpNNfYvrBjr-MaCgftKARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkyQcQGimmHkwYefWLPpNaEEdJj-LriLJSQwaGcgsaGjT0iwr7gwwg5BHuuxxWCjaqTGIh72JK7ezBw_AJyJ_t-njW4ALsNpI9OCCDtOBlQc7ycSkRo2RRQu8XH9oV9ofTVMvsV9zZvr0qZi61qbtCzC9e-sjqJD3RTyI-lYHWhC9dbLM6q6SgFsxiewOh3sIhzJb3YacQO8AdRN8Aw71Ya-e92_Qf9ONGTIUY5xbSbbTtXsKJxd_lpwMMOV7Pdk0aePow82TEbG3TFkehlOufXkPv7zrEKn3l2EtIKTNDcnHl2HM6BHqnOCR0SFPYCq1F5CMnOIG9x6TYUHlT3ZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4xTl9XnvXERkZKPF-3USDdoEqmoc1bd-EkEIE7VC-DtYDeo-VPz3BUZGFGOppRes26mxafNDsTk_IrvCnV3pDqlR2KOH8tjHLOPQw4fCBMO90KTIpV08Zms0r81AgtPfLGWinCsAqhYksZPqzJiSH7D_hVY8YJ4AzoZXeXFjmdnmnOxKD55wByFCw6UsUwgpHGrQytQ6-ZZzBKMlbFzqq2Uq11IhgIU9eTa9m3GJe10iKhJu9PuSO2S58GFpFHqCh7-UUzTggVr9Sd4Gd1XZU_ezdYcnMK3OZLeo6Ad7QKN1CROYNTEbhZh9gr_J6HIYileJwJYM0nYpdtqK3Rq1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFxBbc8x62py51Nu4KyXpek0k6aI5uY73OcBDZfSzmMJ4khnpJ6gLiJOzHh-wz50wPFOwJ9YtAfd9zrzpGRhY71VfUw82aclO_QBpruVIdxcOH9VqCbUrOi0TZm-Z4CdN24z1V9P_srAT0rzJYAyQMNIbEnJyrPLDoV6VoQaB0W49dOLTGSsOcUGHHX3ZVCBYf8HGRxWGbF3b7vHzbsMHvibzGW8mIQE8ktCyAwG3dZW--IkldBsFdpEfwlGwX1KdbC-5huKLwmAjOQlZ3uA5bAFOVWRDNd-x7RdEV19rvDnEi5n4i4L81MUEz6wcejJizhShIbte3EOJqFcIIqBPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncqr7grx2LhcgHRYO_BUCtPw2TqJoY2RUw1HQMyp3CBiRMixW3Syg71bNm4NiAT9jaCcJND_Y7Nldd51f-m6bEycNZ3Wp79hbKB6-BXnfkhanUnZ8y5I8ckpVXhIjXdueqG2VUjqRVDz1gYHU1E3FXJ7mHuW2mMTFCTaHjD6g3tGcEnhlX_KY6vbhQMrgfc-uKSRxgIz48pkAKErjqAkITm13gLp42nP23HiR7dMm16l77STq4FJ1P0eNPm_HWd_jIHgm6MNTD1LBTdc9CMQbQD5wlhzOvyGrr0XUldOp0HxWMYMdLelhYYwxdn9s1yS8mJ1AhEKzZrhlSuB9Gy3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSOFt0iZ5r3yiBymQyGzBEc_P-i8zlTy1gm7FeFTmY4svoukXnlnDxC4zTPeY-Jm8Cg6avRxY0oK28ay4UeLsONSlVAlJy052ewpvd5cIo4jhT0d7BE79Pj2iNslkr3BgK4x4VXHRwUaK2ECSL0YbMDhsBxRnCOLtxuznCiBGwMZinnmg9G7MlaJrGGNkwZjBm2Gev2uhcunoQHm_aLvc5JkUZckAK6XKcOEV7qBhec_m57T5TiyL4yEqqx-3CRQRdyGNQ_0C85NQscAOXAsD961RrbAo3ur54YZWs476-9rDoTEiHaspFgKpWXv02DjJSit1zyXIAOokn9XjeEGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJijIpD3VSYQkb1PHYMMqNy9j0ba9kMhGdOgWQMoVjoOIkpT7aA4BhI6AQK0SKrNCvwUWzbh5NK83D2kK85aFlbx8gOmAOX-VRWe-8_Wjz_ijOEZrYBJO-cyAqthj2lIzH9cGweFNHF1PiahOIgfzZc17eDu5LmwVxAkJezKdMBuz2RMS4RRnVNJgel5j0AQrlu9hSHrvDi2en7hM17zc37tyDAJVVWV7ovZ9vVL1TqGgHGUVP0IC1ATVrF9y9OxbnR32Tvo0eMGKC5PJIOarMXEfSIq318TgqEkYBxFUHRWnw6WcpmkQXZRCo71JAWWzGFjkqe2w6Qo5pu9cADWSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkdxgeEk8RFHNI5JfjJNDLgD73GkA_WN88xTiX9c-mht3cvLHgegpMD8gUWv70CmaYyoL6vgRZA2jtpVWXJFw19FcCshcUlKA8VBX0FqnwKoZCV60dOL_Cyy1VL5pDXX6wWpHihPyPjyMZivP59iuAu4scbnQvNvebQrlJOUbCLkc2xkYuyW_Xub3i4LXkDiKnkRa_X8A3WBbMu155DlHJJaZqAN3GT453Un56zpufC2o04UqhzHWsm96xSquMjWv1TvhVKlIDpy8-vG3YtRQC7Us_y4TX9CsbZ03xQ5uzjpCCJ1CTNiustjkI3mQoGP6L5T1hY0ozvgTMYE-ABDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PId8LOCwGuP0oy3_gqACy1J79TD5Fx-ZwYGTC0xXBvikpAEvzqqpNbGIdwA7cRTlrUbr63bxVpYhhwXONmslcpDoRoxJ_g6o6BD5JuDXQDWJmSexFx2KyJIEYOwQVqHZZEQQvyLdw413SJm6aSroYrWh__aep_7RycXC7wwBvMGPFuUMDE7ms42r_Byud6iSA3k2QPeu7G9X2vj67QjbOD2SouymNMJLO1fqqosprTlxPjAlkbnota7T6GB3PCOuLTTKgUqTPRGUOUeuANyDF3qaREdPJ6sOjgU4eQ_PZvT1wuLzg9aRof76QD3AXUHhHgA_ucdz6fIU_05pHP32lw.jpg" alt="photo" loading="lazy"/></div>
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
