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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPj5O8P7_tHYrqZZ6fs0eDIsai6fs_bEE7A4BnAKbuFqyVcfNYaJcDaYrAFPBPQndyrT4CBNx6YBAPHS4qoJ6Y91AylDH-BRkyBh--7aakruKwmW6IPFjZ-D1B9POqnQbayKvuH-VlTu-ooe-p4tFH4SqHgee1R5SA6Igu_YudJuc3AEStI-7wioFeqAM2-zK0A7xt2PgwboP7c3lRV0QIx82WUuJHl4FWdpdDB_eE2n3JGFQuAVUf7Tc-PgaO2K-L5rBfCl2virXBuWd4wSxBap78ybNu56RrdBWnzW8qovZwEksSMB8VxbPR9wSvP7KDKnNHDD64HexZtXhIpkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUBX3Qdqcbnf53lQGgTXV6dCFAb2qOwnIby2Q4oHGqZ7yEML1YV9gNozBzoiax9MY_dmkiPhtsiHevAIvLSWIzYFgZsP6fwjVCvsZ213RFFZWNOkRlrhsU5h6zQ8IQZgtPpD5bgmOHqQWxOlYYLM26WaPV-YJKZKEB22U72w4fa6tFsDLuFsVeZJPSJaRQEMvrkF6lB6CYCsDYaMybIhKyDBBSpegFNMxBtmIOe-H0SRu2FWZxzhdHPCw08tS6sWPf0q2wqTBmHXOhf4HaOC64CqC0-UhbQ66Z-vExq4HjJmkR9EwimULFg2EhzMJis8fyglBX-PPP7KvytCZgilLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtzgI8ZLvFdwG6zvpoh4uaDksqAczQxHK-x0Hf5j-ti4QkPPYlyqTdvNyJRe3fxfTpBBDGC7Im7zjrycBKwu4C66c5wA6lKqAXg-T-uoK3s0dVj1feIot0xL82_a5mQNwXyfa6olMwg8WqZYkyT_pRagL5TBYCunODi8kodCx43ZRXWLnehKQNKFsZVs_WGCjRS5rfnP4sL7fToVc7a-vXmB67ax7AV_3I061SFOuzfD5S72nj1wFXICCcEOqNmwL9dXjMO5SqfD-2fsJMVw_5W4TGN0BY-6a_vjgWVgbJtFoFzokdBQSWpT6V17KBRaqIp3KwEQHLVfszVgOT6ZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgINaJIP1ZyAOPM3iTC1tLCFUVXkU_UlrWgn_cZDyZL7_JzY9rS7m-fg5YDxm1gqhfnEGab7we05E5HKJOTVQj-Lopr8P20f2JK8NwhoPLa3F2a9aZ5tCG1ONZNmLSzuIriy0ZK2KaBOJellWmjkKPx3_rldj7d0HM2crhcZxQEiloDan9ws0bFigfGZ8jDGtwJg_PKqvF-tcMuIkXaFbHUEPkiDTsh27Q6AFlJ8AFkNGs7Srm3NIs6CH77cc5VxBVuqWr58DSeI42rac_feM9Qu6IOkF7nUJlTVDYLJ5jIGq7n4kJe9MJMzFBQG0zNaSDPmHlvUnOCmrYXykYs01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm_fHN1nHjyvkaB-7tPOtmZceBjRoGHp3L4iX-tJZ5cMg2Kff5fgtMs1QiL0miXEGA9ycrJI9fFPON0ejXoAQBYMmlAMGA3JkN35ATa9LLfUljVrVdJ0jKI4ktTYju9lIYTzE-VodFMmxet1tBnwKkn7m9r0IE2pqysKnN6kyWjrfmqRhLNeC_7KHKAmQWoFc5CCqnSlPiRgZ2Z6s7YMx5v7eaTR2b6sNVde_oGhI4z5f-w8kpFIe-CCE1-CrsMY8139jkzD5xAbJfWz6_reCBBTdJyeN_oOFHsO_2vF0IvoUhzMWf09AWMlg-Jbw8yF3Pz2tygDA7aU7NRQt9Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMmKCFhB9pYWn_a6jsuz822pq2sb8jcKBrKDGiGghJmReZMhT6FLLr_8jISUrhdI1prpkTvo5aYakNG1yFYeV66GhsQCyYn_3McQC0AY1hP0v-icUhaE71oT_yLpYEnmGfOvOu-xSODoJvmBfSOuBW2U_IncU43uWAlJPTe5s-g6x5ixm9fpPvhpBuOMFmGEKD0Cag6FHpnDd2bO965spJy5MPssoYyXE6CN0vEINXAkSE_-AVgJv3EeMJymo2IejOg5cc4HhyudBc6ikzDaaGFLjJr1lOsLr7ecBS9IKBfl-r_WAi0ZyczU2Y1DeXIvWPvQsmyTqqRJexYhCTyPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssHwtwbPJB4GLn2liwdodqXW66uVMEIAoifRBwydBYEW4fF-Yh1iogzzSTnNzTM9zeSNIleajRpBM8nkPXddaJ5s7z0PccCEG0WNuyjLQbdcSzGoquXMjViVSPqmVFNaVssvubiTtBE0HZgzhGi0MC0vBcXFGvSMIK2deqaAMRj1xBWjpavNYK0KpQ9UsTGwLhgfmM6ll1oGqkroaYrUXHvSdsiUaEpAVRf9pik4wrGC0ThPPimoRvzKkyUhsHT1UMbDA4IwSR-jrBvIjYPJDpYHc77LHjz8q5EyDangt1oKcJ-snqPZHhbLBfzuX4z2rdt0JH45h7XYMYGLSK37ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HSVpjAaNsLhrE1NdypderPYBjlLoEobaYOYbXQgU8MX9LkEtKO-AE_K8AFY1KvyZ1Sl9onDWY1qtYLimPNLSd5IGmDUzHPvbfNniTaXRN44b-dbZQbMl7UlG12wCyVl0hYGyPH4Ak4FXyWXSQsbR10bNgTvVpbEagjXMP-rwya8XaFwVoHfpicUBO304etJFDCqo0D3XPgVVCnkQydl8UWgDXAWaVeKkz8kY3ib4jwI9sylIOUkrJwfFDXSwoTIySfyWhnNp3_j14AzP_3_ZAJfxurTxgE4PhN6yJ9c06KZkCGcG4f4OKXxriiflRyf24_a0daSn8rmtgi5IhnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=rqIacKuLmHe2ScyplnZviCm95AOb1ZPYomyOjYxNuSYe3yD87XuxRdnMXVZE177zGd330Z36zgWbGIjwB_1ws7I_0oGHi_gmabmF7uICLdYCeTqdNCQ-2OraqV_pJL4iExI3UFQrVfZ8EU8MQurX5t1mTFvCbqtvfgzYpTv6LmvqTe-JIyiTXAPb7n8t9td-s0WOColV7YrkBj9jolrs60hoAYnIke2EAM-t0xQtOrbGiEfLJv82SrdgfEh2IarsV1Yf5SUCRK_qQqZ0CoE6zrt7eUR6LXl7PuZjpMPiJy9hOMhDDBfTTSpa5ptNAzwnKbtQPRmsXaxQ0YIbqhviUbDxkFOwqkT_Wkk77ugvsTCjzQQRCVQrT9VrT4zPTWTUSSSTUo01M7BuPIyWZIvmCH6EOwvBEhHoo02c3Di0CxKrvxG5D_k2HitPNzo1FiBz1PkUwSfvjLduhM7nAVIIGEL88VCu3vbXZ8GDbSGRLq-DXlVO5uDywSmLWpaQ0j0SJ-kyO3_rCqLltBEN9lNkiKCtVoOeGmtwBHT8OdslIJSQ5q_z_x1rtWGekOtxnLr1MU_hBX3xFNF3M0Puu4KJ4t3QuQ2LiKO4qqZ9cDYgdp9DIvnDjvheHjtmINvKDMbak4QfjVjpw7tH2DRm93p9gMGbmlioN__zjZIFF4cLnDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=rqIacKuLmHe2ScyplnZviCm95AOb1ZPYomyOjYxNuSYe3yD87XuxRdnMXVZE177zGd330Z36zgWbGIjwB_1ws7I_0oGHi_gmabmF7uICLdYCeTqdNCQ-2OraqV_pJL4iExI3UFQrVfZ8EU8MQurX5t1mTFvCbqtvfgzYpTv6LmvqTe-JIyiTXAPb7n8t9td-s0WOColV7YrkBj9jolrs60hoAYnIke2EAM-t0xQtOrbGiEfLJv82SrdgfEh2IarsV1Yf5SUCRK_qQqZ0CoE6zrt7eUR6LXl7PuZjpMPiJy9hOMhDDBfTTSpa5ptNAzwnKbtQPRmsXaxQ0YIbqhviUbDxkFOwqkT_Wkk77ugvsTCjzQQRCVQrT9VrT4zPTWTUSSSTUo01M7BuPIyWZIvmCH6EOwvBEhHoo02c3Di0CxKrvxG5D_k2HitPNzo1FiBz1PkUwSfvjLduhM7nAVIIGEL88VCu3vbXZ8GDbSGRLq-DXlVO5uDywSmLWpaQ0j0SJ-kyO3_rCqLltBEN9lNkiKCtVoOeGmtwBHT8OdslIJSQ5q_z_x1rtWGekOtxnLr1MU_hBX3xFNF3M0Puu4KJ4t3QuQ2LiKO4qqZ9cDYgdp9DIvnDjvheHjtmINvKDMbak4QfjVjpw7tH2DRm93p9gMGbmlioN__zjZIFF4cLnDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=X1UupaYY-b9_lFC4pfZyZO8xTyA2-m07gEV7N4rpV0c31GbNH5pw0YzXyoPCu0_M6F0h8qZcLRQngzftCymUx7OrInQ6SZ1G3kEuGGXOwuvcbBofdv7ggwXaSHdAeMDRytO8Wkbb4zqnJl8icKVLf5nAjVAeH633hpb95WR-s9WClJ_7oy6prgEoFnoPAx4yL3hx2f4aajP0gQzfqr5zWsaLYKAcU-vgezMTe5KjynGNAriV51FzeXV9qXSZexUNeOv1p6AWlj9fOGpqAzUi6nrZdYgF0lf_Xr8qvmvQYTMP8H7r4JLyXyvNUtIlmBTQiRU4Rx5R4ZQ4yJ_6hQv8Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=X1UupaYY-b9_lFC4pfZyZO8xTyA2-m07gEV7N4rpV0c31GbNH5pw0YzXyoPCu0_M6F0h8qZcLRQngzftCymUx7OrInQ6SZ1G3kEuGGXOwuvcbBofdv7ggwXaSHdAeMDRytO8Wkbb4zqnJl8icKVLf5nAjVAeH633hpb95WR-s9WClJ_7oy6prgEoFnoPAx4yL3hx2f4aajP0gQzfqr5zWsaLYKAcU-vgezMTe5KjynGNAriV51FzeXV9qXSZexUNeOv1p6AWlj9fOGpqAzUi6nrZdYgF0lf_Xr8qvmvQYTMP8H7r4JLyXyvNUtIlmBTQiRU4Rx5R4ZQ4yJ_6hQv8Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO0QsXDvt9U9FaAgWxXsGmyh20jFY-qkxULilukRgaqJiW_UC-yPR1GJBdpRE2uCdzCkIXAQwaXTJdvBfM91xcao_tGk-yI3vJxuNJuVX2XbiwFAVGNqR0WgaHo4ljypjHsp_U9-aHNNsDMWGfTEwOi8Xv01azinIZIEF4cm7UpNndbocQkaLIhaIMFuTUjhno8A8aG5aewxhLnRrEK2pHa8G1_ANZhFLLtHSYkYFgGejBk2M3qz2hbXOWLoD1iWTxOjKvTV1eXm8vtTn8VxV7mvWVFmw-nxnOISdowz6CpvnYRlPl3tMFFPhJgPS9uTs0TeEX4_hl5CeSyXH33mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ9O1_4oC7DAa5OAKv_4m8G9r_YV3nhv-Dezc7DJzcp3d-irgEH9dr092ObUlpxafriALPR2Npn4k7JVFUVlSLbojP5qXrMDR3eFWWezUPy-a7MeMZS76B1zN5BNBaOCZvat2206ir_ZrkFw8Rl6TdbiSDuajR7Ca5EhSNnwciMlLR87nU09yG6ugBHBDCzKH9yy-xriN2EWoBJInTd8kJhaaGnH3-56n3ZYRrJI_D6v1P-lMAa4lBIML9P-Ynpl9aP63RdK6N1sO5oOHCdy6IFw2UTsvGyJjMrnMCLXkIl_05S2UWhos5bKq_iOqV9aoMw-PmwPjhYIDkcJiC1FaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZWTpRjFr5r7LoRtBY5CHg77iTgfWF13XgWZinUPqZ3BsJ9692ViVyD9zNFHj5Fq023ZoGRiHprMACxufc6yKXEw_YsFZyBZAn9j4kXY5amODUo7OkSVXUb2FGVjSCpm-J5Ihnq9eF9ne52u4YZ3j9pEB_uBlF1ByCax-dFzuQRvL91oQc325EJL09ZWaIlZiNhqwgoYTmrBTE_y5RVuItfNJLJQOoWpnEZVwwtFnjETBOflHhOx_gOyNNEQur-ZHnYWLJqJcgI_DEXnd_2aiFLYvFn--NtJI7vjQ8bTzAworZStX-AQb3hKsIp7y4_cX1RADI9nxez7iw3v6aSOmYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZWTpRjFr5r7LoRtBY5CHg77iTgfWF13XgWZinUPqZ3BsJ9692ViVyD9zNFHj5Fq023ZoGRiHprMACxufc6yKXEw_YsFZyBZAn9j4kXY5amODUo7OkSVXUb2FGVjSCpm-J5Ihnq9eF9ne52u4YZ3j9pEB_uBlF1ByCax-dFzuQRvL91oQc325EJL09ZWaIlZiNhqwgoYTmrBTE_y5RVuItfNJLJQOoWpnEZVwwtFnjETBOflHhOx_gOyNNEQur-ZHnYWLJqJcgI_DEXnd_2aiFLYvFn--NtJI7vjQ8bTzAworZStX-AQb3hKsIp7y4_cX1RADI9nxez7iw3v6aSOmYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VroeyeDAeQR0QN1VtQG-rwXyd8yUbreQJqp6VOoORbJhHjmczhl_LfsiDK6uRL5LbgxRAXdTQxokMZghycl5rPmDVCL8pDhfNjVgsk8KDET4_rD_f27DEb6YWadLuwmNPHzGBTw_grFJ-7joYFwcnl_D9lYcnc_brPm-dOgtHF7RYO2KF3swE1GopMkDy9vRAfcmZ9_l1DLie3J-9oKKa_iVuDDdzGdTXyXNmhUF60eBoHjmuZZ49pgM_PrXZ1UPhWivS08yntYCLN_8tHW58RqnF9r6yAdoIKNUYv5M-zIcZJm6BoGl99YksuKxTCeveTIPfE2yU09l9XXlotqJxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI2Xg88LPVPCFxFPw0G9evx8K8xlESJxrKLcQpiGmcyVV7oAt7QaKLxcAiRHdxL9A_v6VSKjtYKt4dVbdMDhqdSmvttnWEQ13iWMU3JMZra2KHgnOr4TcgOzjyRDvlsv8fcPuyVEb4KJxQTjdZDEwGETT8ZzBOso6VsKLD5mgMYI1qOZcytliEhHLI7IiZcZ9rcxTig633wGwhNyddpCOX33_dM6BzQq3hU4GGSJUo7_CEfDKWTs_uTq95mIgl33jGBtrbrATyxc9RdPSkOf55GbdFBb21OCehduVbHQTmQVXbFqHM1TgnFTjlnhJIHlElTlafUwfCPalb9-VUkVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXcQVbbZTd9x_ilxJTCiIiwSxHmeE91eMvq_Qcb0o1ZC_QHvLzT4hZOfTqr7udIzz1iU3rhQk3AIPNlE-OJU0gPdfUXHmAA0ewtMfdLQGczvs4w14iZPeiZ06ZKFsUJI9ONVrBWwwX2i7FMyv9N-M2kGqZJlYO2wcnjsi_Y_gUUwhcWIlPZEL6S-GfAO3hGicN0JjL84BddFifYXcS40FGh6FEz9Xgk1Jg69ovohWUbHf8R3uqoZyOMbZh-4eX82KWUiUcTy_Aw67jPVhNveScQs60_wvrJ-V11N9seTUbmSTZsO4HxRBb5krDFnP2NhUbXovyCfiOE6VCm0E5Za-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ncwYyyrAinnZJBYEFQjNwA21cXZSwapE55IQwX9hs0CRNxnqdITTN7FLWXKWdxVdtF5Tod1Pm9H2-7sx0YeL8q4e_vDzUnLxFL0D61dewb6UrMMSyenRG3FcvN033fgksPLGPwCvoDoAi18p1VS-K_bJREB729LsrLqLPDNAWhi2M9wROEXDEelManc1ZS0_wtAxC1EHhS5EzvfaEBhpxtP4GBzzOObcY4M7CJjIlCMco41T4jdFOCoCQ084kUPCOGWDkSJ51Sa2l9P7SeZfbi8DFqQkcfESe1kkXtD75J-ELcgS6qr2tjpzMr8MlwRTdWW2mRIWsZ4kg6QblfeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFKEx7x7hiGmluTJ4snzcQzoQ2Z1ORIHDstqreeBzWr4bAHbhY2hm5xg8oOMsUzv--eMeNYS_kDBXOOFiLyfWOjfd6AIywI0KwTyEfHiddDw3KC6eCzkorgJmzvT8-ZocuPdJMTrcfh45noOMB25d4mwXJ0CGey2qiHhzOKljz7VurG-Tv7ijaFaYGxtX3RYV3Vm5zrKhU7CS_ml55GFws8mrOM4a44pyHeTkiBK29GgHqcuBs3UNGB6Bjf2hk7nKNcUhemXPJUcZyBHMrhGQ5pQbc8S2zw2qSIQZyuIp5LFQOR9E5Djde2M-236crkL5vRtkaySKIu5dyUgrBAMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QmZhN_tVHeZGFrVep9sA1Gt2OEyArt5x_yQ2CLXvszAW4QC1yBxdOQfSoSP7GusrT77XAW5e-QEDiK7TO_7HbLwuyymyepR_QDh2hrqLzCHdVTI8a18sudaj9sQmke3eysFjzfgFD4Pndyrx_JxfPj-sghs4jsQfnDd56mDBKJigR4F_n1g9R-r4eCuLygntZhsYG9eyoqcSV752SwAs-9Y_2hiLZZJ5SxZ5pr2-uOKUA87CUCeATGVmrSpjud66JQZd8nDAqHH76RVBQHjugj9JPhxsf6YGu8NTD8AcNnivCUoZbjTjgREi4q7rN_Ya3pGjwPE5WNx-1nsTZl-vYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5QmZhN_tVHeZGFrVep9sA1Gt2OEyArt5x_yQ2CLXvszAW4QC1yBxdOQfSoSP7GusrT77XAW5e-QEDiK7TO_7HbLwuyymyepR_QDh2hrqLzCHdVTI8a18sudaj9sQmke3eysFjzfgFD4Pndyrx_JxfPj-sghs4jsQfnDd56mDBKJigR4F_n1g9R-r4eCuLygntZhsYG9eyoqcSV752SwAs-9Y_2hiLZZJ5SxZ5pr2-uOKUA87CUCeATGVmrSpjud66JQZd8nDAqHH76RVBQHjugj9JPhxsf6YGu8NTD8AcNnivCUoZbjTjgREi4q7rN_Ya3pGjwPE5WNx-1nsTZl-vYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJBFn_POx6R0KYSkQ3hGv0Sh12xrl2gyeS1q1HvkoIkPctBRM8HSUCD9lsjf-B7aXz3unmTpMBNBHtVMHUwTLh-0HVQZAt5TM4UDKt-wwXevigcUhCzBEP4epT8QLEwxstdoitkRhHc5zePwOXs5vB1x5KaRd8J1X3F5Ba8eJKDhjAidIxuWtHGezE-dorkcJKrJmeiPt-p9M89Uo1c4QFVJSI7WAOAsE874fSm14s_uyRiUA6Ng7914SGR-bACSbYZKDVF3CvxLP7DnXDMekoENetFFxlekMGs_rR3SPvvYl4M5q3_2k5am7-7zX2742ynte4JY2Nr_L6NvVXaCSb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnJBFn_POx6R0KYSkQ3hGv0Sh12xrl2gyeS1q1HvkoIkPctBRM8HSUCD9lsjf-B7aXz3unmTpMBNBHtVMHUwTLh-0HVQZAt5TM4UDKt-wwXevigcUhCzBEP4epT8QLEwxstdoitkRhHc5zePwOXs5vB1x5KaRd8J1X3F5Ba8eJKDhjAidIxuWtHGezE-dorkcJKrJmeiPt-p9M89Uo1c4QFVJSI7WAOAsE874fSm14s_uyRiUA6Ng7914SGR-bACSbYZKDVF3CvxLP7DnXDMekoENetFFxlekMGs_rR3SPvvYl4M5q3_2k5am7-7zX2742ynte4JY2Nr_L6NvVXaCSb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=AQbsi1hhetjPJ4ZJVvGSLQcESow-V6t59MU5ymy0VZSl4mDhE4-T9PWr7benj4tjx-9qckM7xd-ROw_JqexEVlB5DPO3A6WLK-1DsADaL1V9qLwF2XbE6GqvnW6cgOsgchebkDbj_B5Ga3BDGewjARbNIBH9dno8qakp-u64g6TE18LM7z3ep4ygHzGXnzqtmG5dfmYy775OlXmEwW8KXguCmaS34BW1byQ9wxDpXNowCFRR9JpPTiDN_6CinM68ILDb5bpkEVhLCLE0kdl4XBd_uuBFAumPWLf5pH95noM1IUeNlwtvOZf3oi8-57MRjldANqYUrziXQwHY2lqvug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=AQbsi1hhetjPJ4ZJVvGSLQcESow-V6t59MU5ymy0VZSl4mDhE4-T9PWr7benj4tjx-9qckM7xd-ROw_JqexEVlB5DPO3A6WLK-1DsADaL1V9qLwF2XbE6GqvnW6cgOsgchebkDbj_B5Ga3BDGewjARbNIBH9dno8qakp-u64g6TE18LM7z3ep4ygHzGXnzqtmG5dfmYy775OlXmEwW8KXguCmaS34BW1byQ9wxDpXNowCFRR9JpPTiDN_6CinM68ILDb5bpkEVhLCLE0kdl4XBd_uuBFAumPWLf5pH95noM1IUeNlwtvOZf3oi8-57MRjldANqYUrziXQwHY2lqvug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjO9dqhbUjcTFl8fnrMKejLDXILlhktnBQChnDIVkjV_QrKVGbV6dnCF3Nd-5-TXgZF8hjifZz3F4LPJZy7Mfd5EBOQzkdovLX0I6R060oHa3Ew3xtiKuuYHxYG6jgDqGCS9Vl6FdOIduktZo49Ajjris8L6qNbAdIcw0Ss7YOA7_T0cCbWG3QLi1tXNOF34tVDCjZ8xGlrH82YQ4zvv6HXV81RqaMvpirRUUuLwfrcL0lR9fqjHSQ3qPKXu22-vueI2JxFJQ7s-RyZMn3FyJsj-IxU0ZrSBAufZEGdQPf1J5StPlCy_1m0OpIWolzFw6ntGaiHI7-edQjLQQ9256Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNPQWgli4R9YIQQhhrOCU8QQudi4LFzWIzEC2RhuOHf_CnN9fEmy7fhRUKaqOO6HfSufv-5bxo8JbKqWpx95Dcyyas9B1PyKJ6qq5mbhkVr-IYJhYHvhIH3ai8UrdrvPjKNP23CfiZrDZc-utXJwQVafeMOUJ1iZhOxuBFWxJFNi8YN8is3NMTyv2phJiFrEnlumq0j9ahE7DMpf9dCKpSf6krPSbeFRu4FU1F6NsY1xvMtoARySg7QYLXuAECT2Hw7ytWnJzBm7uoh4DDqhabxHuyIouACt76lir2QNCz_k9MYXjQmSQiG6Lzl7mJco3Li6aME01HhJZz3Mwhglrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=adePm_3hA1hODFFwPJkB26XipRBAVMZdwfZTqZxkYNpRZB9NSIg1Ym5Trf1apfnvhMzlOOf4oQhlclsvwD3qLfa6Ovd4Sr7yodoUTsY7f5GI-CEulXr8WGRZOQrclCuKiaTC1MzA7oNgdQcX8hXfp-9d-Pyp7eNyU_gX3BKlUqS-KbAFWKm7RqE2_ys_rcl2HxoJf19aLkKtUDiqGK6-LPrST97IT-Erc18ecKsHu2y9TR-6w9U_g8bt3akhgXvofVZDMY1SHjBh67BSrpZnT-QFWmMfYS3bsmHKrEJDQHq9lrBHpURK2IQdgWDWu76k3GQTXOyy0dRG396MUPprSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=adePm_3hA1hODFFwPJkB26XipRBAVMZdwfZTqZxkYNpRZB9NSIg1Ym5Trf1apfnvhMzlOOf4oQhlclsvwD3qLfa6Ovd4Sr7yodoUTsY7f5GI-CEulXr8WGRZOQrclCuKiaTC1MzA7oNgdQcX8hXfp-9d-Pyp7eNyU_gX3BKlUqS-KbAFWKm7RqE2_ys_rcl2HxoJf19aLkKtUDiqGK6-LPrST97IT-Erc18ecKsHu2y9TR-6w9U_g8bt3akhgXvofVZDMY1SHjBh67BSrpZnT-QFWmMfYS3bsmHKrEJDQHq9lrBHpURK2IQdgWDWu76k3GQTXOyy0dRG396MUPprSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCLg3xg8WrGel0wJk6HUyjNWYAoozt0R2go_bFKtAg2KffrsKfeBwM6rZ1iHeUMmDMAFXN0WijZh-PfplPXzAqfb1VM-n73TmSz0nFklKbblPp_I01v77RwWhs2gigij1uu7fnLZczEAccO0IEmhcQ2KXoLyN4yWHurNq-9FJtwp4nMB8hKknB2VwXgoslK9MBE1-dMRTnEnOiyBHhngecEbztoOOBCm2YGJ-pBDAILzBD8Uprjm0Bru29mFnI2mmkizxO6yAnwbBDhj44tkJ2_t8pn5dQ79Okg7vNfk7Y4GkbbmRTbm4Jkk1qSIYyfwJFgrfqrkGvAoRjsQGVwU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4FuLFp7IOyU3WFn9tLk6-TYzg3yoQMHJvXQE2ygz1bfm-NUZv_Kx7FXEljCCpVfu7Ua6L_3aNg-aS2NeR09LpKe1E2JcKSKzWirftwq5fdokgwTrQ5Q5u63T8YxMJupZGdawP6NkrGVOxijVdGjKb1NaYkDJAQBPwIF_9glkHsvKKgK_oBlwQLqcoBi8gOZHVT7EMhcgR4T7RVXRWvO_sdP8br8HrZsMzRy4w-I3ghJHjsX_rNH6xCtKivX3ChNnheSU7UCDrKur8pHS4RHPzq6SYJdTCrwYoV1ainyv2xUogTjYsFpPrE3EJNXwQksbZOvcZAmGVF2mva4YNHvOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aGkF_Ch6Prfg68p50pGwAHIfK-aqpScZi356rFamW0AaSjcYHJPbYzf0t3gBVJQbAdUspvmO4zwrNFF0txrZumtkZoSjRv3CjJcyvn1wHtM6qnFnt44I2hZ6TthxiOeq3mqJ-4WanJC2Wi-03GDeL7Uhzydm3IuVlSgN7fTtk_7E3IyVCFxN8eTqJLkPbhlxL68uFuhHtrAM8lgmcx5HPYD62wcXwXTfIT_ajAJocTBK8BXzxcW0uqwus9FTJ52jELCzIN-kHfSfcTmHLq4Ni--56xl8fOwXi_udEIsfqK4nUoER-GWMOuHtBuGBWCMiKat5o9aYbvhYFDUn3e44Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=aGkF_Ch6Prfg68p50pGwAHIfK-aqpScZi356rFamW0AaSjcYHJPbYzf0t3gBVJQbAdUspvmO4zwrNFF0txrZumtkZoSjRv3CjJcyvn1wHtM6qnFnt44I2hZ6TthxiOeq3mqJ-4WanJC2Wi-03GDeL7Uhzydm3IuVlSgN7fTtk_7E3IyVCFxN8eTqJLkPbhlxL68uFuhHtrAM8lgmcx5HPYD62wcXwXTfIT_ajAJocTBK8BXzxcW0uqwus9FTJ52jELCzIN-kHfSfcTmHLq4Ni--56xl8fOwXi_udEIsfqK4nUoER-GWMOuHtBuGBWCMiKat5o9aYbvhYFDUn3e44Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Mng1NRIPqXzj86FgU2iEseAjpFMXi04G3KgTOGmcfujebiKuuS_hPnapbO_YgLIAmjT_YDEmFXowyG3R6kjzKFkPs1WXIxBcLqVdJNTSXSu3ME42V7cNhnAr9IKxIdVvURBaW1FJaY9dBrBoUeQ3Z8MvoXfROF-gqIJGDLB1fUg2WVNn_0viDGc4nl1uGmK0xvNypOMHdJSOyFi5OfSBW097I3P6wHTvita2wgHBjlEGumRh6cC_aiHNi1VuDuSaxsEY_kScDr_U5UTes69mDbcAlR-QtQcz19IgAEXKen_urxk-cfFFWs8BneLcna7RNoWxq5f979eGuj-e4kaRIGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=Mng1NRIPqXzj86FgU2iEseAjpFMXi04G3KgTOGmcfujebiKuuS_hPnapbO_YgLIAmjT_YDEmFXowyG3R6kjzKFkPs1WXIxBcLqVdJNTSXSu3ME42V7cNhnAr9IKxIdVvURBaW1FJaY9dBrBoUeQ3Z8MvoXfROF-gqIJGDLB1fUg2WVNn_0viDGc4nl1uGmK0xvNypOMHdJSOyFi5OfSBW097I3P6wHTvita2wgHBjlEGumRh6cC_aiHNi1VuDuSaxsEY_kScDr_U5UTes69mDbcAlR-QtQcz19IgAEXKen_urxk-cfFFWs8BneLcna7RNoWxq5f979eGuj-e4kaRIGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxIuNvQB4JTODX90QrNFhWdgelSO-fddRmKGNxEXo062Anvy-mBqjAmXgA5arHctH3MMxtrsFqlMk-HvIwX_NbP5NQ7bm-2WgXShM4Z7fWIhKu0qujgWFPR8LfeTnKVUWYJvZJcrVIkUjr3FfJEFW3325w2jIRYWF5NyCP69YtX-syjDi7m6HWu-cSzf4kChk0WSpiLcYU0p5GMxVQsSty8Wcx-dtxQyj3q6c3A8hcooVXO1MZvx7cDH-92GL_GUinpkldRkbRujHGJskhIXlQ1ZTH0UHt1woknfph4wLAZHTb1hYz46X-Z60GVXe0ZcC_Ev7cP-fpDonCzxWhZ6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6QtLD2Y1MiwXy-BpBWJtVI5BbE6z_ywFqSQyrlRJKoM1mb6nlcLbrVbQFZ_NWVl9Es1D2dTWUFU4egb-onsvWMv5SDVSNzyWYa8YIA3u2-LWHZYKMK9XrQkKrf8GdQYxgMTU0YDGfaBebQxusXeW6MGWo476DYUTjGihPB2Mdd3KUo2jzZgmOpv9vYrq8J4_9mgVY5ijDMvB6obr-lBcX_N8O6yfzrCr-xNtQ79RZshYzvbWRL_SabtPlZzcuqsoKaUjgT3oTiqX-wIwdyVjXGabl5Up3tdaqkyfKwm2rP8sl1JHoWODn1o2p--zJrMyo0dGKKph-QlBxk9sh_d6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=T-D1-0gzp-O_t_NgW-dgrlLnefj0BCVPxs6NUXUo0O4HVCiRiInORcaIO2LVBhrwYcTxwcWXnESQ7l_HTv36cNw3xI8g-AO6hdgxDnUudn8qcg_E_7n3QQel_lpkfHzcq5LhsVk_3V7t6Hh7e9c_K-F2cEl1Z2IKpoTcwikwUKY0MkW1Rd5FJ_Pk2cc64yOwSTXt8JO-AHa7mpLvhtDWm8Wq3AqeK7OunheGw0pOzZ-K6lq4dCQJ0yE_77zqbuAsTqXXHWfPTEB-C3IDCKRn4svodqaocbIAY4aa_BmtRwF7H875EgkQ4crC8gBygONCNX1S6Eso-UstmGXMgHVR7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=T-D1-0gzp-O_t_NgW-dgrlLnefj0BCVPxs6NUXUo0O4HVCiRiInORcaIO2LVBhrwYcTxwcWXnESQ7l_HTv36cNw3xI8g-AO6hdgxDnUudn8qcg_E_7n3QQel_lpkfHzcq5LhsVk_3V7t6Hh7e9c_K-F2cEl1Z2IKpoTcwikwUKY0MkW1Rd5FJ_Pk2cc64yOwSTXt8JO-AHa7mpLvhtDWm8Wq3AqeK7OunheGw0pOzZ-K6lq4dCQJ0yE_77zqbuAsTqXXHWfPTEB-C3IDCKRn4svodqaocbIAY4aa_BmtRwF7H875EgkQ4crC8gBygONCNX1S6Eso-UstmGXMgHVR7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGiMSxyg_ThXmdmt8QBFF__PmpC5mRxUp-bvaxvvFAZWtVPQAGOiDwtxvbszeNjLt3S_mxyaeCHqPXVJrtfZT4HJY6BozgqPaMUwa5_3SqPI0GlEwI_D7yNSnLfiDZJaQ3E_hUZHbWlSUos16OB3wMeigxCotWvd_IhowwOjRmTEL5C4vdKuCj4_2LZeN2DtVg_ceZOvd_7C9UVS8P8qypB6VjlK-c9zY27iTUnWPm2wRNf_ojPHQU9quT0i3OejOGGYmccngzN9lIFm62SckT8zMPW0q620W0mzJ0Xnsl55-t5rbCiJ-wymCtaMZEXf3R0sB5XIjkO3qpCTk8Z8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIsHQs07__o1bDpTjvpetgO0KMUem8yzyzoasaNn9nS9GfBdKmeUf81L3HZEqlzQsMcLQlTUo_13F4P3nBCediP31Q0G_nX5x3dZjzmb1TutV9O-wIMMononmInJ2WCKy5I_RNOQHIfpKnmL8x_nFaajUKriODgrYBMW_WpsSAxZNdOQqlisOUu6Utr3rlbc75u2By-lGsGaawHrL81gl90-BBBFLl6qEz-0WMsnYa8pFVLuN6RwRlkcMDpCJd9vQDYzpy2vtK7pHzYIYpY3EtydFAKY6F-eTnshACNodL4FCsgPW8mPuAukoiNyR8VrfRlgN9bARdtQ2rBXtyhd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apLTGTyPWKBZGRxEK62o5k2wCoLpO6Jnw0eh5D-yMARx4PzJ-NpdCnwQUCXrrMPRHiRyQG9naoRaTHzMfgjQumrQNmgwgxaQiA_X59I5oM-nnJQgpQwxRmrSrrU6H5sfJenGJvR2Uk-dZHqXnkkXX76ebGNE4t8l9oH82xwZltdScIaDZ_mxazN4XkXr-TEK0HmYJWYHtfaw0lTYtq84bqh8xpSQGYhpyqr-PN1UTOtU3ODIv92TgCdshIKOJ1IDwmssG1lv_bNi9409XaENmsRDWJsxesIdNTWxvfGli1Zyb2wt6-AEqUHEzDwHQnXbMs-97qX51aKQbG41R3YFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLQ9_ERswZJaCyRuBc3y2OBjqaJ4B_tEKYt4z07EZYmFdkZ4V3_OqS-0UUfp3vwj5UXs0kYDxICiKFOPqrnNqDk4NAC-e9HthKpS7GFMW7TA-aKPI9NFWjEjcpP-27wv7daTN8k2zBdBxnq5zXgaiv6ov8CuEHhtzBgsZE2gEi9NVIiy0URuSjZZldIsag7LtZAlZCGMXkcFP62UT5VqZgaFP0QwrC5YENfO9mTwXmwfkm331Bd-JfPtJjAuP4__UpunepooDEqAWUoRrJOsMT1aE7PPnny20a620kTCy9S7UNObXCafDFtEy_3Bi1oSbckP1j4HdQUiQ7hL89eq3gbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLQ9_ERswZJaCyRuBc3y2OBjqaJ4B_tEKYt4z07EZYmFdkZ4V3_OqS-0UUfp3vwj5UXs0kYDxICiKFOPqrnNqDk4NAC-e9HthKpS7GFMW7TA-aKPI9NFWjEjcpP-27wv7daTN8k2zBdBxnq5zXgaiv6ov8CuEHhtzBgsZE2gEi9NVIiy0URuSjZZldIsag7LtZAlZCGMXkcFP62UT5VqZgaFP0QwrC5YENfO9mTwXmwfkm331Bd-JfPtJjAuP4__UpunepooDEqAWUoRrJOsMT1aE7PPnny20a620kTCy9S7UNObXCafDFtEy_3Bi1oSbckP1j4HdQUiQ7hL89eq3gbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFTfh_hiFiiw_bpBZFx4Gp4PV8BUv-rgTA_607ZfYv2lCrwZycLrGqV1IyLP5pP-YcXG6AmdjJC0ZtAaroHDA1884OJZoZqA8VMY3wanWjGu0IZqP2SVlfZpbEcEopKFE-D-rxyAamtWtvnlUv6MJtRTm3ipb--R9_Cm1dfoS6bPCllnnQtgBcYIZweLfpsl4zVZvLDJcYFL-ZAxG6Yyatnbe7U-sI5uYu0Ze7KYgjT4K1aJTB1V5dY4-yth9HvnDJY_o07sfhergCnREjELdmhhF20OuGEXf9nl2d68bDU0ZasWIlYdL77nCo7ameVDfB4xsTYSdGiFny833O6naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsEddnK_ZWOgWeowk29l9Xip3Bjosw9H6pKj7in3IB9xhJpEzmVLgQXZNfCjYULM2f99tevrlvdoNzSnGwLOxmd5NoA20-ULHTxmMdSobMietgUq4zkyhFjh3WUcAruriTQ39gK_tw2rKBSmh9yOVBum7gL-GaQ4HYoEeDNF-P-Efqgg1sFlYwg45OTClNxYReh3GN5OdqzY9Ds91omNEo4YrwTtozZF3YsacnZpp0ox8Sc9dOOILN_-RDylnzhDdbrvz8_4ksFGk9dng-_KUhVobYf4kQYi3bd4Z0W83kxeNx5DSS1njC2mgU7vhA5dCAxf6ziToRJaTxmCMApzdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=EzqZphEBvMiY2x6VR1NMU21o5ZICICWaBPx9vPfVGMLJCkpkpylkH9o8r7sodVA9gSvRF4ledbO-maZCqD2W-oH779OSiZpuQCE7h3-xsN3ufMDf_gpYmlakSV481ukJOPTnLPTjyswpnedLnY9jnUVlmM5skI1Sm4nI_rzeWjI3cTx8n4j-ae8B6zRz1uWKyRuZZborLNV6YplJakg7CoBX2VSI_RaE_8FIMnN72TowNBQewgjOkCpYFfqcklXOZqU0vFdKGWAJnzVcRWXNB-hVeKIauYH2gY6tXzne2ME00Sjmvr9uDrtP6VG9L2a8pqmFLpMW5Ha9Ow7FKsY5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=EzqZphEBvMiY2x6VR1NMU21o5ZICICWaBPx9vPfVGMLJCkpkpylkH9o8r7sodVA9gSvRF4ledbO-maZCqD2W-oH779OSiZpuQCE7h3-xsN3ufMDf_gpYmlakSV481ukJOPTnLPTjyswpnedLnY9jnUVlmM5skI1Sm4nI_rzeWjI3cTx8n4j-ae8B6zRz1uWKyRuZZborLNV6YplJakg7CoBX2VSI_RaE_8FIMnN72TowNBQewgjOkCpYFfqcklXOZqU0vFdKGWAJnzVcRWXNB-hVeKIauYH2gY6tXzne2ME00Sjmvr9uDrtP6VG9L2a8pqmFLpMW5Ha9Ow7FKsY5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=KaW4H9ZxMzqNxU8d-klR1CgzVOC3ER6TeqJqXruQB3K9gd8ZIyCHJYSZEyyr0hNOmAV5ey6Tb8L-urdgiCxEbFzmhVOfclX4mgfP_Z-olHj9OyS5i-6JXDlEzpDsoxy1w238pRXqjkGyEvJ2LLdzl9mup4sY2yiYES1_vfaaxm1cEv8I3AAEa8enG89owJaRW5megFSjgZIU57aUoDYMVY1xe8XZ55YXFfvP2ZjO6Z2xWVEAx0LmnErAe77D2jLsu2wkb2AnnECKoksMmvw4sShHx9ziIv-Imx_pyEFN_-G5_XLSgo8ZSsn-HV5XWJy5Ab1uIFrIG76ggCi_dO3K4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=KaW4H9ZxMzqNxU8d-klR1CgzVOC3ER6TeqJqXruQB3K9gd8ZIyCHJYSZEyyr0hNOmAV5ey6Tb8L-urdgiCxEbFzmhVOfclX4mgfP_Z-olHj9OyS5i-6JXDlEzpDsoxy1w238pRXqjkGyEvJ2LLdzl9mup4sY2yiYES1_vfaaxm1cEv8I3AAEa8enG89owJaRW5megFSjgZIU57aUoDYMVY1xe8XZ55YXFfvP2ZjO6Z2xWVEAx0LmnErAe77D2jLsu2wkb2AnnECKoksMmvw4sShHx9ziIv-Imx_pyEFN_-G5_XLSgo8ZSsn-HV5XWJy5Ab1uIFrIG76ggCi_dO3K4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inNVik7Cyfr-RDqs2EmM-kd-kJ5yt-MEdj11_mBuf5f3AJp0MN72OW1HP1iQuVJivtDGeS8Vd3ygp8Oln1qLx1PupmAkev9SDARstGAWRbQfXPdi6S-P5uVrj4kVGVcbPwgoGaz4v0zSeM11FVeYy5cZba_VvnTdd3nQJJM211UgjDy702s6LOFLJUFDqZ2byYXNQUCi_gtkZGhZz6p-wEZwMEi2czjyfP_VGhKL0RulMA8P0j63aE2uUAprQWmR6-ZvbcTQVsulj7YQMXg07y7RALnTxjjjqXb-IcrDOrpAAg93o3IceWEEh1MFw0j95rdEo-Ez3Dttt0qHOanPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPPxxGTaQu66BEGV2hHWOhXtWFLPhO_DomiEC5OjHI_v1UR0EEhr9eXpm7X7SAykaEcvkh4cL-EAopPDxRyTOecLwtlHf8AjhLm7Fvew_ZLtXwxUbzopBiDfehgZ8int34T3ldb-Iar5M0MN_ejgykiBdmeFLN6MFt4_YPHtdYsAJj0NuIgRWo-I-60yKuD7TuoFkqsF_wt7BLPuhP57X8Ff7oP4wrPZQHL6EnA2BYMrnPCSps1Q2Utt3ubFB08bL9eNwQTBq29XhqC0Nv1UNKpA2f66pdpO4KrIqnihmLImufsKQFQQWXAUxES12BQObmbroN7PRRj0iqH2uTEiSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=tCJrbj-Hf10UaCSHN0Y_QuJM7t9umDVZtrdAhMg5N3iDAdYImYtW9MmsQs013pqfqkfFkwQ05iYlFwdWRzMLoUwgU877N_zLYvyRQGZVz0DS4LKG4s_TtQdwNHNL_yTFMyb36Z7xwcx6b8knxu3i7Nxwj8Y7Im_R9xhcO9kZC4Lj6BBDUoU2HOZnvlArvoknlKHC3rPJvwFPI-buu7on-p8bUslwP4hRXtmZ-gft3AlCR4uCk2lbYugzECKFW-ZLbUPR56uFuTIte8-Tr9JqxsbC5y9Ovh5cAPjq1WxNrp76C2V2SMYO4morDR2dfSJMMdZbWbmkGlJxfWNwnXjfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=tCJrbj-Hf10UaCSHN0Y_QuJM7t9umDVZtrdAhMg5N3iDAdYImYtW9MmsQs013pqfqkfFkwQ05iYlFwdWRzMLoUwgU877N_zLYvyRQGZVz0DS4LKG4s_TtQdwNHNL_yTFMyb36Z7xwcx6b8knxu3i7Nxwj8Y7Im_R9xhcO9kZC4Lj6BBDUoU2HOZnvlArvoknlKHC3rPJvwFPI-buu7on-p8bUslwP4hRXtmZ-gft3AlCR4uCk2lbYugzECKFW-ZLbUPR56uFuTIte8-Tr9JqxsbC5y9Ovh5cAPjq1WxNrp76C2V2SMYO4morDR2dfSJMMdZbWbmkGlJxfWNwnXjfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=enrXMiQTkIjOCjaVFKgJrvL6QRXgKPvUNwkobozqkry-9jtAEglbIzZs-m0M1ECH9JR0H3jRMwv1G9WZaulx0ZytmlqeECLp53hJB5uEFexoBcQPUFAXZ6IL6yqMtPltiOBISJu2oUS8tm0F0vhGuviFmLlvs6vx89Q-58fiu8qErFj7zr0jYAUscjpDgDKQ5Tj9G1fdoM9uEgzrk3wzerFfnXNTksAyMhhQNcYGWfq0M3z34uBIcbym15MgtatFzMmhHebG6SHwpzIeIICqF5QMPfIqgz_xFJxY4ezC0ix-ULgd4JZCl0raViuHwOIHWwjDvQ9S4Dn6hW1xLh9iEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=enrXMiQTkIjOCjaVFKgJrvL6QRXgKPvUNwkobozqkry-9jtAEglbIzZs-m0M1ECH9JR0H3jRMwv1G9WZaulx0ZytmlqeECLp53hJB5uEFexoBcQPUFAXZ6IL6yqMtPltiOBISJu2oUS8tm0F0vhGuviFmLlvs6vx89Q-58fiu8qErFj7zr0jYAUscjpDgDKQ5Tj9G1fdoM9uEgzrk3wzerFfnXNTksAyMhhQNcYGWfq0M3z34uBIcbym15MgtatFzMmhHebG6SHwpzIeIICqF5QMPfIqgz_xFJxY4ezC0ix-ULgd4JZCl0raViuHwOIHWwjDvQ9S4Dn6hW1xLh9iEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgO2uRrmTjmaIaWDFt-muofwmzzAM8wKCr5poTGiQ_bahmFtneLZqa7iWgBtNxg1xcJhRpeNw5gcQwori8mL1dwxfBpMQoqQVwlYNdHrkoexzovaRtAWbfAeTJVPFJUwDn5DQKw857dcHSaAgLZttlaSWUTFJEH4lfIej8ilb4YiBBRL0k8YjgqGuhQqvGbF18L1xHNBAq5l-bQiJbiIA2r5r6Ptu0H8VKkTa3aShhkgIv3-ryOuZ2ysJshLYLlOUUkbJ8WiIk-6XmRHKujcCjOKynXZcfV5uH6AM_3EP-2Q32F96ozNBALrF9WA7gAaPn_d8eo1p4Kkx4IGv0eHKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoLh6Q2xfnXQPb7KtSZgILqPI2kJUDN81J2VnLA-uj8SXf-6yId8C57wQE4HlO_laMPjFomPHepvIy_zqBCOW3Ew833kuN_BXP7M-IiO9P8CQvJEf6WzQObGndhiojJWZPhlNLLfd6Qn7SOSaOe7PidEInl2RCQdC1ARZRqNU4youOxWODiCj-Cgt1FGTFCLuSCQo0jvqDPlnUQI9Zl_JdLSIuGhuFG5oiazf-j1gkd-_fmPygHfddO3L2uZsZzI0l4rM5SHYzCltSN5RzibqQz-islHwomGUmlqu6RlcahKMjowQwv9Yv1Vw3gvdppa7a-nqDy13d2Ghh2LhxtMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKAIqK81Adhd7Hb7a3dH1wqLQs_-ZPantbLg-HWfel0SrPPw2pBDROQAZBi6cP5kUmfMEi4UG7G2fgeo9PXJjcbrULa-FGHfM_bsKGh0PjzvyBEc5HcOIa09VQ11a6ZYT23_LZ85BhI26DOm27xULhPCK2a199h3oPilVfk5fbMhEw2q-1PMyc8KABg2qFY4hEYNnClRt5qgiU2f440kxRcGXk2VZA8ema90Zd_LeSgc_3Guc_UyBNeKPLVPN8fAkUvGennYgiNhrCEs-K2xpa_rNm_bOPyrPb3yRhKnrbfwNK4MtoP_dlshfx3Vh-mPtOLwoMAkcZmDC47CiUInNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL7esDQvAMDWz-GkwdPJ71InuVdFQKBv2R1HGK1lqctsP7i6IC4yiB1BG6toKCATtGXtmw8fb_MrPqBt9F3IsB69rZaokRRwaC1j9AP_wmuEX2pPTfvriS6ULyAKIvCrOPvJHMVWbgg1Yh0j0plSHcfn3v6BKtxq2Yol0kTc4z9ftG1Kkj_YpexO5K0f6qjEc83QqhlrHgIJyyp8EPSZfYq7QnBAFx3_3MUGTQnV9Vqe9F0c46tQWq5Ue_14mlisQOdzthzFlc3NDdnrT5Qb_gVAHbn33UZUZn--0W_f8WAVqoM-e85L1JcRcgNAssCmMfNx1vBSvAi4eLda6rPNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L70Lf1iV0Rgfd8lzeJyDwMiTfC0NPXUz-fUTBosSNUR7gahIOrqdtBayejwUcS-RdkjpZ_igSgwk-I9KTaLxIE-ryx6YOkIB3JWudxSdmMXVRmHziwRth2u5tmni4mPHBfWP5NrAHNH_UeVsIkwj_4jL6mmQ73kok5N1u90mSilHd5ye7XCcRzJ_qWPFJqHpU90EISJSwkaXejvr0IxItLgObIcOaZEN1TNe4931GlXpbhaxLxW0oFF4MbuiPcfjlwIdVgOYmH2pgUKfRJaoToPP-c0HlLTKkDVkG1VFpMm0TdRjIBYExBJgPV2tDPtWRoXusXSVxQ92Ndw43BPPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xwwmij06fv7rYHApsgCgnUW2GJV0T_Hqv-mAxKU5ogYgd7subKg7WKaOcSOEY6z1qSXXVwVuEra0AhjbCD-B0bwewTRU_nEZxL5Xu7v7sAQj5vaMRxU-X4h3mVbtwmSTPmSB7jWOaRi7KD3TW8ECwbnpeNrgBcjUXq2OWcbTdPevyBb6jM1O0WnzxgN78uZDR8wSLV0_sNV-5iRtzxolIQWcEPMNaGFn3_wCcTtBxdseQQUTv-2j34UuewMU0dvoP_Ne3h6ZBLG8dK5ItDB7TzaDxiKp95EyVNs7vP0nPT4_LlOxIzxwEcIH376IAauGVSs1pLwei2UdndQuN8zXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LO3_NPjzz6BctJJNM6egjcH2uNA4GTNbv-GYXr-fqnqVb9EflKCn-KjVgxUdhqn-FEce7-ZES8g7IxbKBB-WFuzUDb_u1trQgdfJiyaPJ-lhFyOtKbJTV4QCwtWego-kPHj2dsk_TpWfumrjdJM9xILUxQB-gbOOgcrqE9XF3lgmbtVyCiwElWF4m0BoD5-O5iFO-Ond919dc7_ES-Nyj2cN04gwYRe5nS0T9EMQSj3NBXmscvHDWFwwJkObare75thMf2sQCO1lJe-sVwppiIqOaonQLNEgV90gOKV5fdDPw74mCg1tBlKCaOGZcbdXjYzWPK2gWJsEmNgSsTPWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFCBRv0X3Akq4csLUg8OZcmG5McWEJo7-TYffKJk8NHmx0C4hCDd8Qzsg67rC1bTptmu5Ad8UOCH2kejFL_EVO9ZHsMZAFJbLM3exfyD9HvSQwjQPdxU5H3p3P_hRyghBx0vrUj8JQnMDyW18IjeAZdx5Tz9POaW20_AgekxHUK62bKraxl75PPwt6KHAcbKPx-xVlUlOUeIdaIbHZMm8UUB1UD6m5crTWUwcycErBfti4L2Y3x6P8UeMmYf6a1vvHjHdYbBCxPlyR5ocVVisYxdx6bZ1LP5BPSFDm3jyCruxuSQbjcpprgdY-IVEHHnaRrg2uY_SHhit6q9Xsv8LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS3lQqUycltoAnBZxVnhE_P3jR6co-GHUVJpBAvcOEhr6WUglgBg5EFiQfYZf5DxEpvMAqfMkRudYHN9sUqikyx1uoAMjs2wWsHohsOeG5JqBEWb-6-raZ8qlS_GQc9v02DI_3OseZReARek9pt7E05ux_eOMrh8ES_Aq6fSg6U6cR0jCIAJE78SEtq2C4LpFpVnIIL3jhxDjhwgxocNP9pSPSIjvluMio_VtmmZsCnyj1tnXkU2ronr0pW42hSsM7H5Wfb5TTrMCLp7PGCeY5-3uhat3WLfJ9uPkarQXBthOww5gb4TFvxE3E7dDHtL_9BjjuO6WQCIBpmLPWNXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyfLpLLxJNc0Mi2D58Iug8RRuWntKG-TcZKpWqIN1MtyH24iBwhDUXjAxE1hbv8BCHKnG1DDs8s_RkW-rPQLqvOjDtHVpqbiiim9yThASRkwVlei-0VRjvbHX7f7D6XzpKNjj0BwB1l70L3VBJOztw7ffd0tGO5MM0txcUIxwHaWgkXeqKSE1irO1fvN_9lTyGgTFVLsMrRimnzFef2oJLoQgiPHsQV-MIYzCP64Wwz1LAhLww41R8JNMSz3yCSRx9W76ac83kODW-A4ayrZwIuRWTcoE3x7dB9VTP7Nnz0iiosDEBg9zBOlxFdrrE32RQagWiMZKEKcZF8-7CSowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=pO55nAsZrfEBzvUZmOK9reAxmltV4Z-w7TdZ_16ohci8w-HlhmdHKeB07XXAw5UBB6MnXdPJioFd8aHnf6JGvGLhQ-5vnzHWEa1xL6kWSg37tTWpHgfXKtxidVruTNT45RyoI85y9Ji4HNyq-7QteZptIHlNZcms_VZ9h6VcDgWxaEvHwYHCfiDDGbkujIk2LsD4EJbNY7GhpLsV8oCQ6uy29SeGd3VI3tBo4r6ksb-EXQDVmvzy-wF5IbFGfu83C-x9NnQ1J2goYA7Rk96EqVv0kAZhlSMUyUx-GltNHUCQ_HQHFbvBgGiGsAax_OdFkZ6eHHML91R7mrhYDsSQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=pO55nAsZrfEBzvUZmOK9reAxmltV4Z-w7TdZ_16ohci8w-HlhmdHKeB07XXAw5UBB6MnXdPJioFd8aHnf6JGvGLhQ-5vnzHWEa1xL6kWSg37tTWpHgfXKtxidVruTNT45RyoI85y9Ji4HNyq-7QteZptIHlNZcms_VZ9h6VcDgWxaEvHwYHCfiDDGbkujIk2LsD4EJbNY7GhpLsV8oCQ6uy29SeGd3VI3tBo4r6ksb-EXQDVmvzy-wF5IbFGfu83C-x9NnQ1J2goYA7Rk96EqVv0kAZhlSMUyUx-GltNHUCQ_HQHFbvBgGiGsAax_OdFkZ6eHHML91R7mrhYDsSQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=ZqIWc_bATGNGbyShWss2k7CjgFl_I9tUaz_cx9DQK-cD6Je6ymBpjneewjyO-Djfy3pXhuglcDQWIQstyMuKDFxfN0L4thp6nZdPvM3SsBNnOEWY406PARocLgv99tkwTo3Ijp5LUXQqep9lE6en1vRwW1zoLEdamh_327cP_ba9J-zlkNokShBsaOl9r6W9h3m49yF2sizE-ZzbtXPvXBtjUbqHRaOywP5yWKK117qTfgi6rrwnXZ1vFSf4JeuoYmpNit9tuC82tjP5lkC4L9sb-ju0o9llUyqBJTNcHwQf_LtBOkbSUzAcEE0Fc4ntDxTL-oEH3qLketnyWq3hZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=ZqIWc_bATGNGbyShWss2k7CjgFl_I9tUaz_cx9DQK-cD6Je6ymBpjneewjyO-Djfy3pXhuglcDQWIQstyMuKDFxfN0L4thp6nZdPvM3SsBNnOEWY406PARocLgv99tkwTo3Ijp5LUXQqep9lE6en1vRwW1zoLEdamh_327cP_ba9J-zlkNokShBsaOl9r6W9h3m49yF2sizE-ZzbtXPvXBtjUbqHRaOywP5yWKK117qTfgi6rrwnXZ1vFSf4JeuoYmpNit9tuC82tjP5lkC4L9sb-ju0o9llUyqBJTNcHwQf_LtBOkbSUzAcEE0Fc4ntDxTL-oEH3qLketnyWq3hZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=mJ6TSb6gQ43UArxaBOtnmqHg5UjbsmHD7rfCY9JoeqQHuRFL2JexOPmwviZtKHYcQo4cHiSoZk2OLrzlYkT4QFvRBqERBH2AqiFXV8W_ZfXM2Sz0lWOYxA5UOren9SHMlgMUM9gH84B9pqKgnMQi5wG4bc_4f-efRhrim2eDAgQVI4RJN_SJBOhjTj9THpvt0JnQSphs343z8QQ5IqFoVLlhIRmzv4X_doEnhQ180G5VNhCh8WePqTmDXrHIPDBmlyq4108Dn75cRhDObWW4qzEFG6RWBQn9qcUk4U4AfUIWw78XsNjROwUmB9YfGDtFh2BcSx_yv33UOja0Ppr-_LC0GMyUmngk49LyWh9uxvwI5hHdXVevTd2bqL6rmd3GztlL1om5JbgjGvrpQHfuZr-vHdx5PVezILKSogT7aQOuKJooRXZ6Dm5jc-4Nho5ZRA9P2T8b9OSjnkEmFEznTV8U6MgWQ4eBrJAUAQy6AbVFx5nYXYSZ4HVPH_4yJdP_BTU7PRzP6bdoJGxu9gSKi10wg1UERDpH1OtYtav7iKMVu4QEu4TToANTDR6_wV3_DpcQdILRJMc6r9Okafqe3cfF5Xm-crdMzyvs4R0COqPcoCFwhZyQCNSbmvpS7Td5dEqP22IUEjKzCo38Co0T1tx5f7-hzLS6ueWdZlvI3Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=mJ6TSb6gQ43UArxaBOtnmqHg5UjbsmHD7rfCY9JoeqQHuRFL2JexOPmwviZtKHYcQo4cHiSoZk2OLrzlYkT4QFvRBqERBH2AqiFXV8W_ZfXM2Sz0lWOYxA5UOren9SHMlgMUM9gH84B9pqKgnMQi5wG4bc_4f-efRhrim2eDAgQVI4RJN_SJBOhjTj9THpvt0JnQSphs343z8QQ5IqFoVLlhIRmzv4X_doEnhQ180G5VNhCh8WePqTmDXrHIPDBmlyq4108Dn75cRhDObWW4qzEFG6RWBQn9qcUk4U4AfUIWw78XsNjROwUmB9YfGDtFh2BcSx_yv33UOja0Ppr-_LC0GMyUmngk49LyWh9uxvwI5hHdXVevTd2bqL6rmd3GztlL1om5JbgjGvrpQHfuZr-vHdx5PVezILKSogT7aQOuKJooRXZ6Dm5jc-4Nho5ZRA9P2T8b9OSjnkEmFEznTV8U6MgWQ4eBrJAUAQy6AbVFx5nYXYSZ4HVPH_4yJdP_BTU7PRzP6bdoJGxu9gSKi10wg1UERDpH1OtYtav7iKMVu4QEu4TToANTDR6_wV3_DpcQdILRJMc6r9Okafqe3cfF5Xm-crdMzyvs4R0COqPcoCFwhZyQCNSbmvpS7Td5dEqP22IUEjKzCo38Co0T1tx5f7-hzLS6ueWdZlvI3Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNZycgOLrV3H65Jv8AcxXVkd4kBfze9mHGPE1xJk_kXlE-eJUYHePu4aH3Q7vbzhwKIAef8bQ-tYV7078qJA5mdhTl9h8lyTcy_F_kSvK1gwbAUv2G-RTSHWVmWr5LdQartrvLGnJCISKLXozKqme0B0IQR8nndE4skpY6toUQIFbTGksUvNpVhD1GuWQKy_78sHINGXDg2FiibPq0kJuc9v_LXl8Myhq_PCo0ZkjiEtSPuEo6KSgIMwL_PcAh7V-ksSBNbgU965fEME3gCKYI_P2pcsHvMliTh-gUC6vVn_8XFAQbwdcew1Ejoe7ZWKwzLpbpvmiihuvCYTO7BgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=mExLUUaLbk9KSChwPRlzRUKPEXJ0u4rT4tRQcIlKa5aFrMW7xnDGuuvOZtIbK9A4xmG4fL3rEKq2o3HE0q1KjyalQ0t63LsV9pdL5hGATRdAoSWkWWF3y47-MAktyKS6KqzJAAcKKPgBVpA4Yy1lShUoqZvGFnbm0GmzMFf_0BKBRvA9e0zwRt4vJ_4egS8C0GX4CulDVqfbNtIlxJ-MfSpBZE5tUl-9mBEjy_fXJ2uuBs2JLfoCwbrC-GNTI57rGpRVf4eAuAU81jGypRJovrEwIkf0nQXx2Ypj0AtcjpEM8j7YJm3eE8k28b5JLYRfkVOEdiABamsesU2gIflYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=mExLUUaLbk9KSChwPRlzRUKPEXJ0u4rT4tRQcIlKa5aFrMW7xnDGuuvOZtIbK9A4xmG4fL3rEKq2o3HE0q1KjyalQ0t63LsV9pdL5hGATRdAoSWkWWF3y47-MAktyKS6KqzJAAcKKPgBVpA4Yy1lShUoqZvGFnbm0GmzMFf_0BKBRvA9e0zwRt4vJ_4egS8C0GX4CulDVqfbNtIlxJ-MfSpBZE5tUl-9mBEjy_fXJ2uuBs2JLfoCwbrC-GNTI57rGpRVf4eAuAU81jGypRJovrEwIkf0nQXx2Ypj0AtcjpEM8j7YJm3eE8k28b5JLYRfkVOEdiABamsesU2gIflYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlhuGgUoc_8hSWPXz8ewcQaHqBv36YxScea8M_DiP3LSKcQoOcXQxUS1wHUhU4v_1HnFl3azxYBXuLSXFL8xX31Ct3Qbfl-V2gWELAYB0NnI9AM6FEL6nQB67nBL2qxznqzgyNcSM2NtQHwsg8FEnCyCuWp1LqwL6XuIzjoUxgvZlNL83jg0QbxSnTbGBSOhJy4BAk-p-6QRz8IXQWG6tLK7HEuwmZWD5KOWVRxj0Boy9M4avqvHcId5_aysynhx--9rwBxLk2PG4xO0A0xx8OXHFehDQRftu4p7JRBxxcMwLsdt2YwEFBHMN_3POz0QBFCqov0TEvDn6eugBnyhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD_nmzsXgcJkZp4HJPElgzB-Fm4boIlSMoLr_50l4H_Ethzg3U7CcV3DvUWr3-vppPwMFhbYHrcSxMn7_9aoq35vsLBXa0VsaMGfH9aOJOHAvWr8dNOVwLRwiya22uk_gja3aZ_e1hxBrhnMZ2O-HGhHq22VLNHnJmqseuzBmD1t_pRpDe6fqSsP2GL-eCk9QLAVsw_APMUuZCx5sEtA1zolbQ7-moepGQabx2-3tO70uCUIzM5PKwNwlnYCvdJTfxzQmjgjbHekyjwAjnq7VH1I-BDBZoTIjF3SlfsXmFslMIZg-xLQqYfOPtjd1J89QbYEzAliVbPPYKaNMtcq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmV__3qE_1iGHEcCow7hNbXZJS5e9Ckgn1aGZ9a9kO8fo5s4vNx3qGYNNWO9-RI_W1nmf3b8-B9pW_elb75KNQRx_0c6gCAXT3fr7z78I2GOWl-Ja2xNUgDSJENwnTd9S38KS8VvrQMTIx90G4rqsD6G3m1mMe9jZMx9-8lW0LbGNVnFaIuaVveamAEeFkbN2DDs7uNSY9RaXu8r1IAusGwzg_oQ9bZX63DuZ61qhyAZN2z2eXl4CpZ2EMGqnSJP8W39TmGtwc8Axlrj9Y9CJ_Vg7Yz5hhmlvglqA9nKl0tjlUrvtvzboyAieLWN5XjBrEAPukkwRXN3ttBa7D-4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbjXEfP9uKNfwipjPXQM5j4jmPzMUUTUXBzSbrRAkLbl_DRuApLhVRQPHDocfC5rDkkenqSpKGTWi7EZzNoXDztHPrJTmm7ESIeMi3nAEhvlUU4rioT_eEhXKiglRS8-droellG-MIjs0B5j9fiFjeMwlj0Er3F5ovNnZl8b6n8WvT5e5EHlSl6ExFqmA_9RosoT8Wi1CqvwY2ULzRc0lPIeqO36LgmRs_c_FBABGb3uzhTYRSVH6PZLwqHJmm_MEFvacvj4IDXo-C_vkVJ7PJO9XGE9wH6nJgqhiuy3iOqI_s-fMpKnx0ztDEvc68-sLlEM-GZkkGr54kW-CgoSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7FPZIePBVpcwGZlv__K3wQy7pBMBCiIaQrf7l7_rLtzcKRQu6gcrutHur9PrNkajZVEbqWbfdLW64IGmLcPjqYYJjPW88ZOWAgREIprZHj8S9H4cbgJ-3aoXIcP76KwxMKnT8EYUBCcXfy67HacCRQrWcSwfRZGqYD7cXIeubhmAPlubjMGaHdA4DL17TV_uA6Vw4iMJq_MWM8BudbD4j769JZ8lxX7CCj98pTsOm2FPov9EvgbI38Q6XA2ODvRuzTby5HU36bOtZvcZB5x8hc6tufhBH1CnlyrdyXPScMd70R2uipm0Mk-2j9ydtjy8w7QN3NzaU8BLSY13vXp6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8N-obgGwNCiHw0x3K9nDgv1kEuTq-X4AFHUoEug32j1HXLFBbRCqCEbNPyWEGfGXsefbt0aW4_ELoTIBlEh41McO8yCkUPVVUDpEdi2aBQDQzpr2ayfRNxDZhYB-TxKgDON-KaqeKv3UG-nO7ySo6cFvfDzm3QsWYfgr2wbXvcB19IL_0__TxzX1JIZdPdTmMHMCWJOVYpAfdEhZo7A0qeBPUHjQ65RZoExZ_oFtyNqUDMDpn1b10GS3RKVhBX6LAffOyyu-dflJfhmD-7bcO7MIQDfE0udBa1xsG0vM_LQViDjm1fZcXaT_4A1nCCTlmP2GIrrsRV7YPKR5G-2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irv4jMxgMzY76o_tZXhRhYtS8K4Ew8UbU7tslqVgZgs76UrzY4LBZ4YTJ9lqcpSmm6Co7He3DqX4L_pmCwbm55mWpVy2y1IWwcDFvKmloov0qsOUq44W21NiwRsMIxAHQKZ5rrz46N6ueIxjCqZ42Cx1GoMSUCGxD4YtdDvO3fhD2StQSeuxR7fYjkcf4riw5CpOzcXfbUwSfpzXEbBAvDLlG_exo5d_kVOzvx8XbP-CFK2HXZTy4CBVjaIARJryuzS5FgB25zRAq-cnm6u_8ChHHJI6311jbJMJs5xuCD4thBaQ-pX7zcc1F-vgRNSspp-3G6j46qRTknNQ-nxFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izck-A6cwFyOrAW19XJ9Aev3cn9u-pTHZg2IiN4KVB1H_OG2bjndNBZXDItuthvb8D8mMtoB3f2NVOwtBMKe-unmnoh3P2tLz78EFs2hoQzMr-hEiVYJ-rmVeKtuSQrZoVSFuKy2baXgEF5xgz5uoeWNSurrdfV0rQ7wDec2Sc9-QXR8cI9heUXXl60ipBaWeGq-izq3gCrhqlaxuR5nWSArRNYxy6L12QMn-OdEg5sz98Tkr0A0vIdm0nplbzdmBa2kpj_ZTgTRSdByFMjWNK9jQJMdJjuQFotUaacfRHfP9_ZCwtRcfbVhFJR-5gW_ZEWiBOoHZWt9lqVXVpQZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQxrFfo1EFe5p_xsxZCRQgq66qfkWtP35Y4HsAosNwNAbetBBmLkEjvlPg2jWnBew23Z05cYmxvKESGDpxnFkbF3GkqYld2vpu1Mvn68n4gvDv1Xq1gHPgBju7Kle6S_by1136Q9LkEZhKrW_Up3CJFxApKH9HxQ_purF7yugzX33kHyn4RWj3cM-MlV9dPjLQzmViQ2PCwJQ-JNI2k8MCtu2PpXiJJ1wxA193QZ3MUjwUHoWPxorJ1g6y5OxoiM2zh7PTxmPKgTbPnJmGhMHeDJ_c3UvkepfVeJVE81ktWf0gl47P6zoAsK8Mk770VGoUfTU7Urh7LH-wI9DuOXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DehbeQOpOSXFLxPBclRw0qkFXtmVpHeb7ETdPUEbGs9uS1S8mvpuv1Y-BDZbNtBABy-O9HEMy9cMmJmr7-z3-UAT1Ik3WVNiwnqdL0vWOpH5_-142hXjL2tTOLySstSumUFxSowlwcAuQA-LEcQSUtJzZGTqlwRpzYL4yI9zcrXlgJ3zzOtJ4u2Q54kL69mRoEvf6rZFXfnN_gzH9cU-ZG7iBGwyvZR1yyKjAAJnEgiC9-oK63Iuhgu_Ebg2lZUC-ovdQVWa8qFn18xg7Lf81NQ-zn2CG0jWFuHCfjdn0UdFMYX7yFd0cOMzktr5X26iNQQmgGZskagHGk3htiBMfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1kwPMnGQ6hdF1xruUN7weQvpaZeYJYPglC2pBFyWoNBE1AfA3yz3Rpv___fS6cFazyLtcoM1egJChLly3vmLeoFpUevnNN9gKVpkEFHCS-Kcb04UQfbvYyq-2jUp3dfNBtENDX4Hp5U4xOy0uQDvvBPOILmA9We9WkCDezdzT8KncM_XI8COM4gjNYG4Gsk94Jk2JM-mhYbH8x2eR4nIv2X7gNhVGrszT4xKZG6SOrEZkMr9wMZ_vQm0aLiyb11BsftBadg5N4iPCJjjwSm_jSXeNuBajN3fVrtN3WSSOAq6H1kFEhD1euQubvcJR7FXPxWNj0xV2yOvYnoKfeZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0cHEAVC7ryyu5rGctF01jKgw4bMnXSOsVwzpKTNllYqhU5ioAX8m2r_KoSA23orSydH6LeSlZuQZpJFBgBOnN8ja5vBrEFhW56_Wblevv7J_SOUeaj-V5NikxaaV3EcSdWGO1I4ScLOnMUK0TMSknhARM_xLqokeuSaF2KBUFL47c6Sqn86swJo--oOy5RQ_Ykq8a8gN3Sm9cSGeGywi6hwJve5jw4v-zfWal5tHnoOzxA14X872PzWVT2vimtw6Wihuai2A_XcxjBjRBEe_98C_nJ4ydEC1FLh6CR1y98-QOsndIl1GNzxyMBSI0PfpzAF0OgoZ8wBzIJSF7xm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGB2SrrVPICCaNEWnjAfutUbzeVnqLSEs1fy7RmeMQflZEZ_Zveji4Jsn-0apjOotQDh8jCTxZL0H8dyciIv1fvl6jz1avN2A19py18BWC3nfBlD0Q9fT6Qj_sttS1N69SDYw9ZAbbnAyzbuyrizfgt-zXpl9e9MetBKhBgFXByrNy2PVZ_YvmDTVyO1x5mPBhfhkk2iBOCx4TlsE7AJMERJKP2-I2aTKeMqCZonHEWup9sBmgP7rfEXvhMii99ldHKkA0Oi6US4tnsj1dW_FvKaSyaKDNPLDD0ldVx9SyH0F4yCgAfUQ1pWcW6jTd7jQQ2eKgSRQgPP3g1Y0Vdu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0Mu_uFTiQs52hqzZs8OGMlVOCEycdpXCynzRcgy3njWWUJQDKA1pcVl_kj9MeLizTrvIAQfm6a_Qv0pkF5Qqj2F6pApcHNzE7q0BurlHwxS-18FMKfUy-mf_pfqu4Mq6C0JoiGKTxBgiQZwon-kLRqMwuIHrFpMpHqEBOVvC0oOUwvM7pLzOkKnP3zVmwk3cjn5ZUOKk04NW-Ir5Yy9PEaZV8PqvyGhkvW1KBcGvr_IX_J1D_W9wT0cAJawdEZ3FxXz9ubhi-f6JXTv3YhBD6pq2NR-hwqUhMLZczLwJ8vvcL4CaSkb8zzkbNrXRGaVnkGc1z6fwkN5PlWJQtJTwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvX7DGnR7c6lyM51oJg7mU9t0W6NZ439pqhkYOA0ayVKQzwvgTxgP6-lgqrGLr8LBfzcrEEgmDhRJ9prHrzRn_DDSMPJW6Wm1quTve5YFsRBfCQ8si0Yfcikk46OAoiEEVDR4gytEXjTfFav_vLtP5EIQNyFA7OcePAwS6T91jqvVBqB4_Ipv0EuQIxb5Sm7JuVoGjk6bX9PWWB-P0SLxG8l__rWvYpD0M3Rrx6cTZOaxKTF3J4__tnHb66M6Bz4aSs2kOySc0mZklody8VimEt7bxvjfXhTFWYgKd335SxfbxM_wxzlN4u7CdfqgyJiV0_9zQf1gztxAjf4e87eUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1yuNNyOz9djHoCucHnX2YudAIhibCIk6SKw4H2i1qftI8hx8SzWuUhFueIhLBxROFAjT9sdjOJHMWKXZXEcxQrwUxJyj-nTWbcMFGvne8vjma-og7Gl3yRwc2RrZnC3Vq_IeXTTCrQu8HTe4eVUCuLyuvivuUUvnss0AHUNK0L_0OVLmArFToH9YZzGkT16UmjdzZKsH0WV0vPGpYnZNMntOorgTBHRSg_9M1X40pfih7prAq_Gk7KP5iZyi-ZLpULO0YFWY5nlT_vHZC4kk8BvKGqA_2_3zXLK4dKrNvZ37zCkEQ01nhI5pbb1O_bd-ZV2U8Gq0p-styVYqwNGnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
