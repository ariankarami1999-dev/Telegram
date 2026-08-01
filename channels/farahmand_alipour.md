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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=M7Z3VBxBgMCJ0aFtmOBsCg_C-FtGUtgWUEBTrIJWhpjOablGJj5O4BaAHwPJop3A2_Ne78Ixb1d_fh1zQ7eT-MB9y2vaGk146i4mFEeJKrHnMEhbIlHZJ5m_ak3O2r0vQ5QKSQPTwqZRdwF4g6njfPArL4Jo1E7JK7uOTV48ams6a01zSg2w0NVFvKE40jrhLv6vSb0iBFBBJ-5xxOAPhlXcLWhrFk_Yg_QVcMVbYvbpS6hFveXieq3Zgrixh7JOaLVOjrOzC9bZtHlsjnUhwZU7qjrSu_RE7lvrU3kWnr-SXC7f_o8PCLFdnuXMV26C2DZwEj5yHPBY2sZsfvIJWFseYJdyQrrDJAAUS27VEY1N2SxYYtocYzEGdPxPI8lRGkZiFm7S4D-sZs93S6ASB_UqcODuu-0nNnErTbfZ0hWjeAHHf8_baCZ_zArufHPG2w3yPhWXSX4ZBrWirwUZ1FRqs5o4AK60vpBFhON1yWQ_ldbzmDSwwCCodUuZpJLv-OJX079Tmg-NGNpeyqu-UQWhcz2Rnvso4T-G3tCJGwlvcRHxCMHbq93OExA2SnxGlMX13GSPRT2Ub6fbNO-dmaH6YBQGk6JTr4BET854FGiguhGQhlhwJbWzIuinTKeT2C-1q0He6YAYjzIPx8RSvlR3fCZQVwS6w0RL8Cp33Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=M7Z3VBxBgMCJ0aFtmOBsCg_C-FtGUtgWUEBTrIJWhpjOablGJj5O4BaAHwPJop3A2_Ne78Ixb1d_fh1zQ7eT-MB9y2vaGk146i4mFEeJKrHnMEhbIlHZJ5m_ak3O2r0vQ5QKSQPTwqZRdwF4g6njfPArL4Jo1E7JK7uOTV48ams6a01zSg2w0NVFvKE40jrhLv6vSb0iBFBBJ-5xxOAPhlXcLWhrFk_Yg_QVcMVbYvbpS6hFveXieq3Zgrixh7JOaLVOjrOzC9bZtHlsjnUhwZU7qjrSu_RE7lvrU3kWnr-SXC7f_o8PCLFdnuXMV26C2DZwEj5yHPBY2sZsfvIJWFseYJdyQrrDJAAUS27VEY1N2SxYYtocYzEGdPxPI8lRGkZiFm7S4D-sZs93S6ASB_UqcODuu-0nNnErTbfZ0hWjeAHHf8_baCZ_zArufHPG2w3yPhWXSX4ZBrWirwUZ1FRqs5o4AK60vpBFhON1yWQ_ldbzmDSwwCCodUuZpJLv-OJX079Tmg-NGNpeyqu-UQWhcz2Rnvso4T-G3tCJGwlvcRHxCMHbq93OExA2SnxGlMX13GSPRT2Ub6fbNO-dmaH6YBQGk6JTr4BET854FGiguhGQhlhwJbWzIuinTKeT2C-1q0He6YAYjzIPx8RSvlR3fCZQVwS6w0RL8Cp33Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRkksgrp1K18DPFvxE_enVV_M6w89v66J2iO1XUbD782KxP4SY3XgoVovn0dp4iu32YemnFnzhxAxFuYgKVdQ1tNbSUDtvwL4RQThnpOmPRHg4eJj089nxHq2iNsl78Taef-_E-guT9RMOFveAxJlit2nG0p-aDkzbJr20g_E9nCiZ1UsgYatrMxAeMkPGKM5n_RputmXLCsdf2w-LPL2qD5Ny-sqXGPuoAuiwRXDOdjLYDxADQYXNCOtgFtwhGd90qqanffLXrU0Q-g-xQaREHN90-iyhe-ZH1f8RxH0Oi9mMM3YbYaBbFSGAoBFc-ikfaRSVUAyqpgrd1_7YeBjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0znLHUso5RfzuDl_Gi8Xz-Cdxb6_lhLt5I8ikMD30an-cCjXVYlKvFL_2-kfDj2H5Vj4PYvnxhrdAMC5_Htmd3OX1U3mth5_i1TNrjECnRUuI7vVIAm6S3Oykh9KMXY5Jvh-LS997gFtZr7b8NxfE2wQ1ToaaL3e5-AaeSLuUF-0bDceWCwIIDB8Ss80VcJZ2NkX6gjiHb97GZVIaH3vAPd1GpF72b4H3re0lL1dEYZMg6k1BGVLDQsPnFQikcPP7QGR2xxnWI3HSWJapdl5IXgElnjTnML44uMJ1XCdGQUeBIzcyWdufjtIeIyURR4IKNwyTJA3On_Q1-Msr0otw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHrLsKQ28-dHKvWN0jOJxzksWGz_boHoaaLpurDkR68mjACnluOD02neUE8WkslcgfEkMXvIZnDbm_9FibnBO5LsOGH70LkE5jVJ8mSBQ3S-b55G5oAEXDXx-8wgWPy2gTuNSuDpYIUphMlBRmXez1pCp9nH6PghUy-KdXHSJ_B9x-zO3JGgc_ygbNIVq7YDPW0DZ5BISr79sh2wI7ynBIi4UoTwWxYWhQnCtHlVNHwo_IdYMYZfUsSQj7DRYFH8k3p9XMKvp2n6cxTMxbsdPw6kSXBn6m-ZzOnxHql1QhgP6VNR5dQMf2Dy2j872V4QdeXC6mRjtntEIBfWSNnmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKkZMvYLphdHgHlw-LPbzLsP2fIj2BxOqes_CeLVgS9uKKbOGcbBXm-nX9yK6DCI_JhJOAjhOpMABLu32zC5i7mHTYjHJsD_pbQ_2DCKmUvC3dlvbAK5B7rz2Qwt9gdbhCyyUAFUQetsCCRtmKN6eep7O3qQguh_UF16HZNy-IMFhc1LmojSdmgnFt3KXGLo_139pvObf6Zt-fluf_cysikgbWjmZtfwRsep5NcbPslgak5WBO-ZhtiWg5dY9oAAhVvt4jTY2hj6ahWxOvlNkbUPZbDU8xkGvOE74ucYqFByIDjSNS_WHVTVwOL6L07Acrwq3-R0tD7t7yvDIUsq0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1gdKCO_UFjmyghf-5i9soOVhM1mnrzHdGKSpv0_LUGMPMlQr9kQf8tHPs-sa5w7avnzmpLpp4vEVdvzCecIa9fT6CzkemMVL-R7ij9fqlXZwmtBP3Z3U7s1oxY1M3F92tWMQmXSFOZta_82suriQx_AG6z3LBbZ-zOZSbFvLoR4_cTqaCtDBPEa5d1d-ewAvOK3wOt9Upl30mcSi-2x7GJ24UF89zUoCr6jn2ETLH8mLPiSTRT6jZFG6h-y7T-ZkScsiJD118onla249wJygt5kmXJ3OB2fcuAOf1ieRyAk4PBS9-J1Fmvckk04Q83V6OoyV4Oh49hmnu5zqEte0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5VEgJw4hanN57qhrF9VUNEuwz_KhE-1RqWLhvbkvMS28xj4Qm6ooTMLa-1o1HIgKxdT2Ew3W4Gdtt0hg1jOCYHjMNHTf49pDP-lDrT9WNf5k7sDbUlRIzcdAo5y91-MUWGK8M4yPyZzUMKhHUGdPel1vg50UaWIuc8PVTTnzkLfyXlw1PhlFGzLGuHEBnPiRSqfLOSF3bjjbSje_PqDM0N8wPSjAFjwqnlvgXHZCFyw6V_tMcFBVABvj02bAQQtIFhIpKw9qW-LXKdT_eBJNC0qiyJD0_Bu4-3lhBQLDmAHDtFP0Lu9GLxutJ2pZjLGvLNuWBJ6wG_56rnhi5oC7pIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5VEgJw4hanN57qhrF9VUNEuwz_KhE-1RqWLhvbkvMS28xj4Qm6ooTMLa-1o1HIgKxdT2Ew3W4Gdtt0hg1jOCYHjMNHTf49pDP-lDrT9WNf5k7sDbUlRIzcdAo5y91-MUWGK8M4yPyZzUMKhHUGdPel1vg50UaWIuc8PVTTnzkLfyXlw1PhlFGzLGuHEBnPiRSqfLOSF3bjjbSje_PqDM0N8wPSjAFjwqnlvgXHZCFyw6V_tMcFBVABvj02bAQQtIFhIpKw9qW-LXKdT_eBJNC0qiyJD0_Bu4-3lhBQLDmAHDtFP0Lu9GLxutJ2pZjLGvLNuWBJ6wG_56rnhi5oC7pIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKiCwUuovxj-UV6RvcEDOZBqsLrSThYZ4mZR6qeECtXjL8Lq7HQaPoVdOB7JfKzrXURLsWj_oi4p7f4bDMsnmce2Jd-789gBHMMXuq6Dk5uNNE4GO9iD23V19YNRXfXifAbHya0Y9CxUa_mQguaNmqKR1mQFLrzgHnFjQUIjiSa1cemE5JerO9Oqq2CTucqA1TJqKmYgrGAjwULiFWfC8myctTa4AqpL0CdLTjBeI4ABA45xt-ACD_t5hdoxfxDXQ7BoBk1rzn2R8KX_ZS7ncxGQPQGYXvcg3vZ6TFePRkVjfihWIh9J8MBg2x1ORk4AWex7D0CkbuAhTcrm4H0a4o4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnKiCwUuovxj-UV6RvcEDOZBqsLrSThYZ4mZR6qeECtXjL8Lq7HQaPoVdOB7JfKzrXURLsWj_oi4p7f4bDMsnmce2Jd-789gBHMMXuq6Dk5uNNE4GO9iD23V19YNRXfXifAbHya0Y9CxUa_mQguaNmqKR1mQFLrzgHnFjQUIjiSa1cemE5JerO9Oqq2CTucqA1TJqKmYgrGAjwULiFWfC8myctTa4AqpL0CdLTjBeI4ABA45xt-ACD_t5hdoxfxDXQ7BoBk1rzn2R8KX_ZS7ncxGQPQGYXvcg3vZ6TFePRkVjfihWIh9J8MBg2x1ORk4AWex7D0CkbuAhTcrm4H0a4o4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Q-HZXHBPtxFVt6ATnMNgCkAaarR8BxK2CTZse-VpwmNpwyLSLzVzIM02PskWe0G6MXtevRpFL0J1wAqN8TWr0bUt1gdPVB8_nZq9WN0gqNlNlsoAJ4NBu4MgEO6g3NhMJmwlqShCR2COAkMaTl1ZUqc5bMzUz2rfRgeEuaU7Dtovo5CUBnyT0213cLCN7-A9jIu0wpLqXF0tpeM6og1h2TADq66o4RlzdWCN0Y0eGSsgYgANkZ8ddqdvpttrf6arO3H3gJ85_-reeYowACxaB2D5YLUZhAR3oCF8WCluEG8TVuBBj0cNU4xlbVqWRXwg_BDKl1XtuqcAedZC6_vYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Q-HZXHBPtxFVt6ATnMNgCkAaarR8BxK2CTZse-VpwmNpwyLSLzVzIM02PskWe0G6MXtevRpFL0J1wAqN8TWr0bUt1gdPVB8_nZq9WN0gqNlNlsoAJ4NBu4MgEO6g3NhMJmwlqShCR2COAkMaTl1ZUqc5bMzUz2rfRgeEuaU7Dtovo5CUBnyT0213cLCN7-A9jIu0wpLqXF0tpeM6og1h2TADq66o4RlzdWCN0Y0eGSsgYgANkZ8ddqdvpttrf6arO3H3gJ85_-reeYowACxaB2D5YLUZhAR3oCF8WCluEG8TVuBBj0cNU4xlbVqWRXwg_BDKl1XtuqcAedZC6_vYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRrZYD69zjpN7yK3RUt4r5z2OHJ5ApfevWeAaFvlih3878EbHlJDoalaSQt9APhk7JOADOCT4sQh_lE69ARAmroapnIQFWCK2Uq6zI8jr4mO-WwoaTcGwZxoq-XPLsHy5T5Zp_0wogkHsdWAHtoU4e-IH7KNEJAFQqmolcAjcmGgQBnlRxTQh09SPmXP-Ix_8aC-OUGYzsIfLhf8H8drhq2UctNRzJjRtbIvPwM-mpOKvP8LsPRFfgRHLRf7kF4UgAF0b6Cdoh6js_Agu3ODcVFlHLMTmu3kpRpJCQsf6Kd_DnuoHBcyp0bc34AyitualTJWLHN3DSPLByg4k8hGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn9sstjSKzeIVa9TdIqBaJ8fX8XPLWHWFybvntNO4xeYm5i-d8uy0dW65ucB8Gs8QRJ_HYmzq8-G1aXpvjE1Ij60POtwoRBSPpIv3Zj038AvAQ-iHxEeDKMwuxPNAw98rjz9I3SKA2Aay3PvB9XlgAiSyCNh-vBpl-83gdgu283WXMNUeEMIs8WcgXK8rckhCvWhs4HcfZ1A23deMbjuYOhdbx3d1i7FNrhp7kPwQBT4TqT7kWzSv3tieYbfuqfMeB9k6gAHLB5ve4Cos9wCW23_CacYIIG-hGyEtxf07dYCBRd-wzc7ov02LemM6ZXESarIqvVZTvXS3jI7Fi_qVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=hEUghzu7n1VQK6nR7v7FnV_q-F3tZZk6T3ECwwRFy-RwWKblXmbeOLyyDNUhL7TkMlGNW7OB8Pc-IYSD_oIUnJT8qN02Sh8DoDFqKUK2u9m757Maw3g3xSkmy4xgUfVBasmm6CrrevtGDBcOGJ5ZlQY3g0OvC_9TqanK_66GYkK4c6aqvqnmz-C4Zj1SR49pggiAWQ9Y9bqldRR3YN6XZbHL8Bj5z3Pu0JLrfc53YmFcYfmQiudX7lNlKIaCHtOQhcftCsE8F-A0BtCsqA-qGqjPdW1d-RzqICT7pwmzuuq6hq5sFhUZE1jBddmZzqOgY0ANgglNE_h6TBk7dZHw9RlNFg1b9xEXD-aLpw5UwPPoi9KOypQd0atN4ZDBqcUo-qkghYW4rwqcSzx1hAcHqyNuS7rPnUoFSn6PNmatCrdi0mBYVpnzw3tJEU8zFRr_K959HoF2Ihz2eGsFWjLzLinOHAt_iVfHW0ByipRsftodoSEDGcKqxDbruOCalT6C1btv4FMGvOy6SzjvimWc5PMjvIuYkTpVj0n6rU2M7qQh8kIfpYM20EpyGVhzCXDibLzh207YbmAq5_etalN760e0fxDPf8VcVhXZIT-GuVNHtiNRFubKMfwhhN_7w4wLKWam4ymgKk47lGDL5TvBbFIRDR45NM5prg8NpL-l1ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=hEUghzu7n1VQK6nR7v7FnV_q-F3tZZk6T3ECwwRFy-RwWKblXmbeOLyyDNUhL7TkMlGNW7OB8Pc-IYSD_oIUnJT8qN02Sh8DoDFqKUK2u9m757Maw3g3xSkmy4xgUfVBasmm6CrrevtGDBcOGJ5ZlQY3g0OvC_9TqanK_66GYkK4c6aqvqnmz-C4Zj1SR49pggiAWQ9Y9bqldRR3YN6XZbHL8Bj5z3Pu0JLrfc53YmFcYfmQiudX7lNlKIaCHtOQhcftCsE8F-A0BtCsqA-qGqjPdW1d-RzqICT7pwmzuuq6hq5sFhUZE1jBddmZzqOgY0ANgglNE_h6TBk7dZHw9RlNFg1b9xEXD-aLpw5UwPPoi9KOypQd0atN4ZDBqcUo-qkghYW4rwqcSzx1hAcHqyNuS7rPnUoFSn6PNmatCrdi0mBYVpnzw3tJEU8zFRr_K959HoF2Ihz2eGsFWjLzLinOHAt_iVfHW0ByipRsftodoSEDGcKqxDbruOCalT6C1btv4FMGvOy6SzjvimWc5PMjvIuYkTpVj0n6rU2M7qQh8kIfpYM20EpyGVhzCXDibLzh207YbmAq5_etalN760e0fxDPf8VcVhXZIT-GuVNHtiNRFubKMfwhhN_7w4wLKWam4ymgKk47lGDL5TvBbFIRDR45NM5prg8NpL-l1ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=UQ8PQEwHeZwJMm_GX7u6AIddGQV3c3M4RXeqTCJ0AQZQ9fK6hxnOf9v2CilSdn-X5y6c2aV_Wxap2HdRBcDq7C83F17_O6t5wNyf1yiA9Ilo6n5bMcB6jMpyn6lEYXxuphLz62PCGDWpHQHRXScJv3tSjd9wQDgOms6LqfQpKctMENQPS2YvDP2dNJz_xPne_FNhVDelx3jDIlcWM6eGL0P4PDxkb_RyH_ARPH02IgFT_2oiZvuhkoOozTUk6wh5nXu-Xld45P0asQt5vldlX3Na6I-I1S9ibpuBhVpK-5M-_T5q5d21sc8YH0AQpQCcM_Hc1ySfrbKrsD6dec5O8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=UQ8PQEwHeZwJMm_GX7u6AIddGQV3c3M4RXeqTCJ0AQZQ9fK6hxnOf9v2CilSdn-X5y6c2aV_Wxap2HdRBcDq7C83F17_O6t5wNyf1yiA9Ilo6n5bMcB6jMpyn6lEYXxuphLz62PCGDWpHQHRXScJv3tSjd9wQDgOms6LqfQpKctMENQPS2YvDP2dNJz_xPne_FNhVDelx3jDIlcWM6eGL0P4PDxkb_RyH_ARPH02IgFT_2oiZvuhkoOozTUk6wh5nXu-Xld45P0asQt5vldlX3Na6I-I1S9ibpuBhVpK-5M-_T5q5d21sc8YH0AQpQCcM_Hc1ySfrbKrsD6dec5O8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apTWWgfoguob8t0U7u-WfcjGVNoS9Mc2q-5lleQ859ugnGageeZ0fKsJG7I41px-ZR1t-jDfY4RB2zPZv5MCh-d8NEAp5M1TSw7YtLAZXE8Kj0cNO9fD4HdnHXYXi6lkrS2D_8dO6h9QrkuXDJCjbKmDOHXRmhrVSm4jjMpMUofUUNi7g4GZURZyaNaa9DzDvRmYr9awwNmvrsEhN3oyfE7hLn7nY-kfc32mIzEGK0fvJLZJMFYKrgfMKR6jUiyc08TOBbGclR5k4y241afL-V-hVlU90f1z9WVH8V-rxcRxU629RzdRfGVO8Xtt5QW_fqqj1l0l7jdzbIRyJSTjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snYy30d4wuRPqKGnbZH3B23wRSN_9yw91QIW2V_pOorrJ1bOiV5Wh6foVSvTjkYWwslQKOthBmnTHEVCRjOHpfO9eeypJroz7SqtGiS1FB0MMcDKBoH-MS6UzlxXWKXE_xCtpwS_AOkpDTlYYu7UR8JX6l-rkp5aR2k_OJ1C50TP_BWdcte5JSIlRMbH78ZLpXIranS7Z4seBkKgJUL2_wUTkaMOqPA22Ot_L3alMP6--MpOJ6MawPQDIbLVtLFukIv5VtVei4ddrKzmkwnwQ3uBr-RlBTgwAEk_B9ZG5BBhZW6__dzMlr3xwbp42WjlkFtMKNQSChzAHjN7bUUcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=rgXvaW0ZchhUG7Umfl_pgEGM38bXRQyOdzY0aKTAsoun0ss_LEYuGL-TbuXxafzV18CicYgfR-QesU3U572uYJ5jnecQ_dg6RbVsB5dbG7A2p2thXJyi2bT-H5YOg93LFIjUi0hr0aVdx3h7fMwz_kElQFX5fww9VtSmBu0_GjndVX5WhOQ_0rRxWi-LuaJ_1GrbXlXCiLDS4dY3Qd60fHe4cHf63N7EUENPkESi-4hLtASN-kATaLEaBEcpNxqbyywHo3YiWVReDz2XSBHQ5cGFOYtYyj3H2n_50uQpHospC7_fPCnoMXVRHyXn2uGqeQw38K-pmrLZJK03tWib_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=rgXvaW0ZchhUG7Umfl_pgEGM38bXRQyOdzY0aKTAsoun0ss_LEYuGL-TbuXxafzV18CicYgfR-QesU3U572uYJ5jnecQ_dg6RbVsB5dbG7A2p2thXJyi2bT-H5YOg93LFIjUi0hr0aVdx3h7fMwz_kElQFX5fww9VtSmBu0_GjndVX5WhOQ_0rRxWi-LuaJ_1GrbXlXCiLDS4dY3Qd60fHe4cHf63N7EUENPkESi-4hLtASN-kATaLEaBEcpNxqbyywHo3YiWVReDz2XSBHQ5cGFOYtYyj3H2n_50uQpHospC7_fPCnoMXVRHyXn2uGqeQw38K-pmrLZJK03tWib_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=sebD97NwLtTDcLkWg0PcbSfCoKCnAL3gBXshmBw1-5llkaryG8ss8vJP9_qZmwB17J4OzDLNtp-x262AomgIGTEJqj2SXK3McSf6_tm0mNuwRGTG8B_qWtvoMYVX_knQNhKdND5EmcfIIaXpjkUieY78T-ffJf6tQXJk2AJwzFd_1BptmUGPT9r_PbWaI_mkBCkh5MAz28cVngrbvwB838Uj_KcZJ2cazjJ4mQ7O0n_hPyuQRYyEK1MIS7IdEmYjWq0tFM3cI6kaLpAiNtUkli6pCwUw6CFGqaMr6k9VPCpYGhI8kOG-O4v2wemdGGex7E1cQd725sYc8fKVXZTsaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=sebD97NwLtTDcLkWg0PcbSfCoKCnAL3gBXshmBw1-5llkaryG8ss8vJP9_qZmwB17J4OzDLNtp-x262AomgIGTEJqj2SXK3McSf6_tm0mNuwRGTG8B_qWtvoMYVX_knQNhKdND5EmcfIIaXpjkUieY78T-ffJf6tQXJk2AJwzFd_1BptmUGPT9r_PbWaI_mkBCkh5MAz28cVngrbvwB838Uj_KcZJ2cazjJ4mQ7O0n_hPyuQRYyEK1MIS7IdEmYjWq0tFM3cI6kaLpAiNtUkli6pCwUw6CFGqaMr6k9VPCpYGhI8kOG-O4v2wemdGGex7E1cQd725sYc8fKVXZTsaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQmF0tf_h7yZpVSTMkfJ45YLKpkIY27qfNde1gL15HkfrN84ttct2ssqpBrIAkGfDYzf-evS1qqvt4aMGRDpxkjYqNSCNEt-eZsKDWjc4gZn43pXA3mYn9ft0tEwgc-0DvaxHin0te3_VDD0Q573wJghl5evIjE3d54S1fXqJ2e0eaJ1pxFJR45Jsuva_ByNg5MPiiF8H1G710g166odoSgTB1gooNUqrk8rxdyeMU1cqgTJbZeRaAI4qRl5JPL4WGlxBybdVZZy7zSsi3FoQHNgqWvOI2BmXkHpsRaJmtm49dqT1VKPObAGvuDY2_eRFYB3w31g_57sDeXgbYml1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5sHJr4_mazeQTOmYnjh_5cTGaNO_Yy1wAnoL6DDU_IxS01-_0QMmeBCdOukJLEZA2UCdiK19qHvimZ_A_PT2qhYkbX6N2AqgnIgdr4y95MckxnbKPGZ4Yv-ekI_-hGOiBFcnkQuolEc3HBhVDs9SnEHyPRE49XchuwL5UjI908Py6wrgeOHus-f8z6hjitRqJt1Flonrh4KPCcaUuVIQV1H_WOrnuGIRZUuZjjUS3HxNhdwps2nkHk1TFL5__yvfUv254ugwak8d7c-ZlMNLAzEGGP-7owGwnTbx9SiBxfVhyzbN6dZe6kcm2UrS9xOlD0-1o5HI5Ky_9Csu46Irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BKp9lQUIM7PbFrtiaegrfkBhMzFxuQAOUVYoS9-wWDTMFkV5SpifTl2WN2lk0yPaLDQhURFybPqnbhJyA-fbxxs2bzPZ8kjTuadaFYYM1JeQMIwZWm0UyqWLcTIhgYu0jqw_oYvHOw27fq66m1rbDpVZiqRrZPpU4Cd8D-wzmk_RxYW57Zrfm4Q_bGZmmfoemf7BqtL8NMqSHB0zzr39kuNmhohxJrQ4aFFrW_aDIcel0SEWdsVe3owZm3EJRaZ09xNR4HYEL3DK_pX2CGoqfwguB0wonHfo9ft4F4zXgbR5vaHLnQzBtck32Ct6MachAkUxBIdXHPIt8ktggJLjxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BKp9lQUIM7PbFrtiaegrfkBhMzFxuQAOUVYoS9-wWDTMFkV5SpifTl2WN2lk0yPaLDQhURFybPqnbhJyA-fbxxs2bzPZ8kjTuadaFYYM1JeQMIwZWm0UyqWLcTIhgYu0jqw_oYvHOw27fq66m1rbDpVZiqRrZPpU4Cd8D-wzmk_RxYW57Zrfm4Q_bGZmmfoemf7BqtL8NMqSHB0zzr39kuNmhohxJrQ4aFFrW_aDIcel0SEWdsVe3owZm3EJRaZ09xNR4HYEL3DK_pX2CGoqfwguB0wonHfo9ft4F4zXgbR5vaHLnQzBtck32Ct6MachAkUxBIdXHPIt8ktggJLjxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1q-2wNnUKAuTMaBza1DLBjthg8m424Eu0qvwXk2gMJhAe69oUmKJEC1AyqH15cPnPZl2w6vV7VZObV04fHPdlXiHTXT2jBTvb9PyFy9JWOn3bkUZgTme5RtrpbxaM1GFuCS0jvpoGmywcK1Xb4HysJH-i9tM7pfDWYYrjL9zRacETmgo3kLT1GRn8k2yzbENbaQYeZ_6tLGE458GgLUVAXR9ZArz7u9ce-_PGV4kwDmFGL9VdBkWl8K6KO-ADS649QAONJtKEiMjbDlVIOi48nKBzHUM-kx2alPeIMJ9c1xo1U_5cZjEX-fMGBNuL0_3WEPYCBhRINS0qQRf4Tr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGvmjQBLkyj8RZ1hgr-5hz6skLTjntIZA-GTU7DtO7uqB_sFA-FXOw2M91BbTcCpIeu-xkw7xLao14wf0sBI2JLw1Oc9jtWAvtZbwVv7kUoGatm9ovlMvoMW0RtfCyNcwSPqw_4EgYyhGG9EUCcsaOOz2wqBshayojoBcqF8H4TyKM2RH1ggGeigNMczDsL3IBzyeI-JMZb52uH0h_VqDTiYIhXNbFd4XoK8gKv2NlQpiyIJSlRGLxN91fpXCk0cDYygOTAmG5ec9vhn5vlLIly98bDym_JQjiaKMWIfFDXie7LxZcWACVqdrD2JZ9t97uLiImUaOvhC_nDEegSbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOzhCGjJ9Xt42nDugOBqne28u8IWEy8pEg6_0Utcjk3X-BbcvI1c0opCXEY3wYZf200dLZPAyMCR95cYw3Y61N07LLredmGYr2Irzsr2cXo_qyVVti6TQd9ZnRNuHUA2SdBy3-81IwzoeF0WawM0P07qlXPMmhWN10ilwKaKApKB_VqplSctQ1qca1rSUFtDxELcPI_w_Kiy8vfkGSap-uqcXIapAM7CfggEpXsTCSbxER6bIDnqFKZzzXh0X8Iy_71QZry77C3ajv1Pg6tDanMpdirqlOduH6F74t8AKY54brw0ND_8WtYrG7LJQ_bCYUeTg_v96XDO0wcN3ZtzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLVPYqnAv1lNXupbNoc6WsvTd1yFv7qBF-y-aMdWWj7YWgdFbmgU5jzGpkEnHWaF4HOmm4Vk7iHc2iSeEFIrg4XZLU2FBNloQems_DV6oGhyM-FIhixNLUefMgo44RE1wjBMtWgUvugr6TrRew4MjJ_b5XeFoYmBEToufeXJeYVNU_T55N9g245JpjeLKoMk8kELev1OaQJIFEWk61NLBvxU1esD2SWwuMnnoIQTitb8mqYM9lggCazggibFaXd7-wId3uNBLPSuJmz_c7ByzreH7IJuJ_LGL6vKLOKAJOlXHLSkCuhf58uRz5i9oBYzxJE2n0A_Joo2PSNDs02Txlas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLVPYqnAv1lNXupbNoc6WsvTd1yFv7qBF-y-aMdWWj7YWgdFbmgU5jzGpkEnHWaF4HOmm4Vk7iHc2iSeEFIrg4XZLU2FBNloQems_DV6oGhyM-FIhixNLUefMgo44RE1wjBMtWgUvugr6TrRew4MjJ_b5XeFoYmBEToufeXJeYVNU_T55N9g245JpjeLKoMk8kELev1OaQJIFEWk61NLBvxU1esD2SWwuMnnoIQTitb8mqYM9lggCazggibFaXd7-wId3uNBLPSuJmz_c7ByzreH7IJuJ_LGL6vKLOKAJOlXHLSkCuhf58uRz5i9oBYzxJE2n0A_Joo2PSNDs02Txlas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOUnvAvzms_bi53_68N24CHhsweWPaXtPnF-ExcuP1VeYXK7Sr7EsRROKNTZ_o48_ruGYp6gbTBImjfE0psDqBDSje98nBDChXte97H8QTCkxHJV8qQ2PmIlbkw5ZtcJnYlAyx4XY6QRa82o093koXp7qhvCzkJ-u8OK1rQiiDwE7qyFq6lwbO4_f8MKChaQo6ZBV89D0UQwzJ9zeXoxjIMeJaXYQVmZ_DueNUzXnQRp1rYCdFctItbX5CIHFPiFAT5mVa1u8oSL8F3K77thku04HAHLV0fu5WtgSsVp36P2VfhxBciFrODEY6BfDzn2nCuqknpDQAQ02ejDrPeZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqYGDWrJ5PO3tpzZSBPit05r6V-4KdUDbWwONlulAf0-lOSCVbJMN0vRlc1QqivWBQdR9zwoqDeTr836M3WQv9bhU9xec42lRdhraJfD6kMOhbu-V3ppl_o_igjXDS62Je6cMwidX663d0__zxm08VfJRYvtY_-FVPMyMzztx0iL32HPqlbg3Y-q27akhDcQvtMFCdXKnEoLQZgs-ifzqUsCxrSMhUeA6umoKc5wbJ1BsZ4wJTTrsn-UF8Sew2MIFvGw-hIy73MFaIN_QZkfp8BeZExeI06BmI8yaoXE9xIZlLctvTUfW-px79e-aUjS7FgdoS_9LYUkl11az1zQcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=c6xGN-rdHrGZ3d90aLT4qiq4RJHZANqIaJCZhQplIxLF-NKT1zzCGZu8ukh55LdzDRHCKW2gOv03vlS9Fb266PZomAgaCizocHTcyUlgeL4GQPFpV6pl5yt5SSaqWhNis6I3O5Bm6owgsmcgHFBzLniIeZYuhJWcObOqAAfoU2ebr9QaRQ8aI2Eq9lzHYxNV-iF9fGYvHTeAO1TgHbsbWW2YUhesheZP8zHZ3nUqGGvG1FdM6f4tI8nhF_KJk66c0rXbqLXiZxBAQi3kpW2MxjcnGisplSLEnMnmhv23tjLcY6rJfFMaw_L7WshNLYqmnK8rGD4jaHhqzZuS_9HNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=c6xGN-rdHrGZ3d90aLT4qiq4RJHZANqIaJCZhQplIxLF-NKT1zzCGZu8ukh55LdzDRHCKW2gOv03vlS9Fb266PZomAgaCizocHTcyUlgeL4GQPFpV6pl5yt5SSaqWhNis6I3O5Bm6owgsmcgHFBzLniIeZYuhJWcObOqAAfoU2ebr9QaRQ8aI2Eq9lzHYxNV-iF9fGYvHTeAO1TgHbsbWW2YUhesheZP8zHZ3nUqGGvG1FdM6f4tI8nhF_KJk66c0rXbqLXiZxBAQi3kpW2MxjcnGisplSLEnMnmhv23tjLcY6rJfFMaw_L7WshNLYqmnK8rGD4jaHhqzZuS_9HNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=EFAFEMeOTcx8XH6QIFDQGkwReh5lCUKtMn5dIKc99v-VJBFfbtkaO4l9ePtLK1iTNPc4HSsWPQzQ6wHZcn3lgr95AFx3XNdK7VfQulc9ZJrIgqXXQVreuXKw9ZPxfqteOedcB3oiW-AWPX8tHh_FlWZZH5i7Xx8oKqF2dhDM5IGKoY90hkZ0-HukC-gU-m_gJqeg2r6rWkhqMLkOSFeQ176J7YY8jfqISFmCFuQfd1bMypTTNQwKkQVx1ElPOZLSuUnZYbEk5CZIXBEv2DpB9XguabV_x0rstcMllwHyNoA8pYaUg1UBbG8kIWi0uQzPoUi-Lk1IWjCqYKsfuhKGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=EFAFEMeOTcx8XH6QIFDQGkwReh5lCUKtMn5dIKc99v-VJBFfbtkaO4l9ePtLK1iTNPc4HSsWPQzQ6wHZcn3lgr95AFx3XNdK7VfQulc9ZJrIgqXXQVreuXKw9ZPxfqteOedcB3oiW-AWPX8tHh_FlWZZH5i7Xx8oKqF2dhDM5IGKoY90hkZ0-HukC-gU-m_gJqeg2r6rWkhqMLkOSFeQ176J7YY8jfqISFmCFuQfd1bMypTTNQwKkQVx1ElPOZLSuUnZYbEk5CZIXBEv2DpB9XguabV_x0rstcMllwHyNoA8pYaUg1UBbG8kIWi0uQzPoUi-Lk1IWjCqYKsfuhKGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-xHwLAj8tvW3BqGP6ZU_dQuBn0TjQjSI9lJki9jYZcwl0DnUXuq5yF23h0M9e8mVzpmlsDT6_azuYP9aMTzOD4ZDb2bxS1Nl2bI8c9Gu7f-inv7i2BdqYH4vskOHz-GBym6OIGZSYbh53UZeFFfTv-_mfA7nWVWPKsuzemN6klYDoft4JHZUhhxb3Z5X7JaxyTCu_fd-YxB_AvS1KtySzfwvLXVUmlEHrO7WTAv_wM8z2LN_tPSxnFJ6i970z9CIELSYHH70AarNM_ZoGmqD6x0-zrYxJH0dng8rRSWP6oicLOKTOH8OOrdwITFxxLzbQLoPLdixaJ0YNFEKjpIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI1goeD_GrCabZ14adxUlwDavbWNYw9B-dFDOYKxheFQshZutZ-hp4tcpNhe38n8WiCtB1OJYGGHPxsvbxwCFtmbP3Is_I4xeHmM5h4XBubu_wM4oA1P2ifIF_utmIAlZLLjUaFxI1KTa7beqffD98PTEHkHXFrsebXBcuteHWCdH8P3RHKKuS1t6WmSPElXXhim6EshsU6c2KQDsChguvLQvwguNEDLT7jU4vg_Ahwu_S45LE3glfMAWxTFgEELO-DnlCMOUonac4ZXRAhQKAqSIGz0gkXckERxaMpwel2dMBm76VNdYXYRAUfcop7FQFJj7uTEsJsmrL6jm-UDKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IQjAp7UFP_xdzIvUlEv_FVISCRoY8SMU-fj7v53rYTLmlK0YbA0DcclROY8ueCahxzBxSIH7xpRs1VBMt9ATUiObqjGpGjl4DmmtaPO5P4i7Nv0y5Gvh8kDwQiHnHtYAw8fILiqYauWmlIofk31DTLOTt0oAoMhsNk9DHEEho4Yk_6IGroYnzuqWKGJn9QrWRrX7sY0Psv6a2ywTupBOr8SY3kyluJkuQluJMai8yeuBGRzHgM9I0uAOdnxJwQmUnb-Vb75AwUBr_tHKUIgIhXeCEOA1r45MQCfy5Ce1VZphyZLZ32Z8fmMGApuZ2MCgpw4p5y574y235x91cKsnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IQjAp7UFP_xdzIvUlEv_FVISCRoY8SMU-fj7v53rYTLmlK0YbA0DcclROY8ueCahxzBxSIH7xpRs1VBMt9ATUiObqjGpGjl4DmmtaPO5P4i7Nv0y5Gvh8kDwQiHnHtYAw8fILiqYauWmlIofk31DTLOTt0oAoMhsNk9DHEEho4Yk_6IGroYnzuqWKGJn9QrWRrX7sY0Psv6a2ywTupBOr8SY3kyluJkuQluJMai8yeuBGRzHgM9I0uAOdnxJwQmUnb-Vb75AwUBr_tHKUIgIhXeCEOA1r45MQCfy5Ce1VZphyZLZ32Z8fmMGApuZ2MCgpw4p5y574y235x91cKsnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=NyLZgpxxdhXmhfRueNLYV_xYhKh-rJdtOlqadlwQxeEpsDK454_woHNRxQqTB_5hQ6-4Xda194UuocSa6DhIl-6bb-DNRtnOlrpv8_YFLC-cVIcazQB9ZF9iJ72VJMAyzejByy2WEd0D5lg9tKygUv4DMqqUFtgvYVzKhLjCr9AUPEgm0RrVsEffUdm6zQUw-KzpKi9ACBGtWHbOMOF-X47EXoZpxcmTE5a8KpRwb2NBEXvCFg741KLXvfFBqQWXbI7TfLZlNSufa1NKSbt9Z0DsjblxA4Jq71vso7C73hicCR5lFy36eLsV2e8N2acFHJtug9k2VDRXSOEWNPm3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=NyLZgpxxdhXmhfRueNLYV_xYhKh-rJdtOlqadlwQxeEpsDK454_woHNRxQqTB_5hQ6-4Xda194UuocSa6DhIl-6bb-DNRtnOlrpv8_YFLC-cVIcazQB9ZF9iJ72VJMAyzejByy2WEd0D5lg9tKygUv4DMqqUFtgvYVzKhLjCr9AUPEgm0RrVsEffUdm6zQUw-KzpKi9ACBGtWHbOMOF-X47EXoZpxcmTE5a8KpRwb2NBEXvCFg741KLXvfFBqQWXbI7TfLZlNSufa1NKSbt9Z0DsjblxA4Jq71vso7C73hicCR5lFy36eLsV2e8N2acFHJtug9k2VDRXSOEWNPm3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKRwvE8UqH7rEQlwi8Ci_gHUyPHb3G_IA2d5e5uF3eGjAI2tZQLOkrt7kW_7hVkdZkjSR5pzurLBqfVZJPzgSYpxr-5cMM6eVFZ2OoOqBa9G68sY0iIpucvZYJ2ed-S_4Bo3Q1fcDxgbId6ns8BI42SbDEA79LrjnhZk6DttRsSVGvn6aTtN8EuyxZHeu9Oqcm0LLu1AXBvA6LvTrmLQWVLgGKS9aIWhfWxPTKw16rG-ydazSna18e9kLW8ckg6oWf8KB7YhMra1C11kYiKuI7PruYzXFDN-tDjvkl0kAmXttKPuFYD_uXuQRlr9VvaaH7wAwjlWn_fiwDRjZeZAGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T07wqKSnfMz2VUZw6vIiWRSNqhT0U5QZ7D2KOl-KnDmhBuEOddQaoj75UprWnWphaeKyy-lAQvywW_b4ZfVl9FEJ_LbwIcgfxqxTTH9vZZJCR5hjL1_FMlzRz9NOOzdIUcm1CsOPdzemGA69fvdIgGd0amPSLDoDubTxt7TH6wgHABs9LcK64_Nsfgti4w_EiPZ-kOSm94DL4VvDJYsKlhx974HI7aSz1NAnfqMdBpnWVbDxJoACD7JPTYOeDVDfxos9lmcRhFlqa4WFYqFnR57GXwo_xGxvLlYq0-FRylZdVRIyK6FoYu2qrhE4WoS0JaO8ubxv3IDKmUKKpbddlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8zDWUwxIdLqWuJnhWN2LOKfEVpobTkynNVZXFNqK787-9YYDJHdLHxrNTpC6valN-XKsnBNymH6O9Z6TxW-Ys7G_VZ47IyHPD2aLfsBjGL5MxCqM0TGxzuAuDQGPWOoUIiEyaYBFdVKV4-8pGpT45wUKHzQOuK6EGAJylHTKFqwWtNK5H7c47zeVSjpRvChgsUR6mgaIV-_D--rseU4Gj6cGXxD5DTKzNIYjuLtPmZcOhfT5OrzAKV8mOPXJ3V3Y0jeIjzpqYVRIe6lwp0tn-UeW_c0DQBUXGzcbZlQWLgiBxJw7fsLg6uTrCBzEMjlN_Kc1g0C-fvcYp7rKWiDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVyR_rVEwDyI9jyNayo0tmw4V-W76nEAu710KMYaVaf4zJthpiRdToKDy6VL2JvXzyHIX6-sJWFCZC8bTcRcboakT6JgGCoEhIZjuPGg1lQ8c995hMj_MmXoI8wmAz4sbn2f35a0yZ6ZeOVWkmCk3z85yD2Lo88d0JBO2GBzyKA9xTXOoAhKeKy_6dB_8JCqe0_maaazeMMXXcJsQOSCfgtLPLzYjVdUz2Yi-FW0qjLeOH6ogGv3IascOZVwC1iInMw8wUCN1H-IWySpAV7grtU_K_yi12dMwcL8NWV3PbpsQyTP_kmZF4OlT5j7ceoP7C_vwubX-OXBHUmI1zEZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNcUKpvxlfXD1Q-y5vr_ggNnptmxndNXHP2EfXbCjfZjWzKQ20gEqZt0QYGjwpcJthXTfwAf4IeKhxkon8Nu5xcg70PyGACdiMi7XZQGSrWupo7Vaf4oqDX2PHjKqWzvfvEcWKpQs_yEGROj1NXVBGU6B_II43DNIR9ybYf-ywvWEiYovYXameLW311_F85BelNx12nzootFlB3I8wC7iVItGXPQ0QArjIbb9bII3XbthRC3m6LAgdffvRIYuq3Ei0pbJx7OQ4Yg09DbFW6hgDxTZpcFd8WaxQMT_ukBG-iZ3GYoJSEMQZ3CzcSkG2Q3xgR2bLHLSkvoMwZ5NgC5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUsR_6qpQGdxBZ4mUfZgvSZKlW3LyAnvfW08Z_T5LUS5zPeB3ruaT-vS0LIhhWUHxNoRwvGZ12MlwlPYSqRDRW85txp91--C-LAQmb09G5zBDIMsH0u0dEoBScF-do054yn-o4DdKjkQhUX1tZEI7szUsKlcqD1LvsKuQcEbeB358tk70U2-4dA1bpedlWC61ePS4G0reiES1P21JesJbxNklAN-7u71U1efO0ICPNuEZs16oZoLuiQsHMYCzuP7RK86SKe1wTTmV6SpKgvjcCiJQ_1GP-lHxyXYBXkF5sXf7fRn1aak9zUiXkgXS9DHIDkO79uWrDIRq_X8topd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuy2pvcJmOWfOqU_lLsFnqi1wotDsY8Q2E3GgGgai4zj4NpNjvAuM8_Y5e9xhg39X9y_U3AlYwYy682-OZI-9KlCSjjM19OM5ypFyk0zPoOC3WMHbcMI0_S_vFv7Pt9FDXEw218gwwNGa7uDVlMuTR-VHZlg4Id23WLPcsEo4_oOElc8Sm35s0-4ibNzCz5Ti0cCt0MGB8hQxIiuccNRl7ARzYjc8ElAvqA_ABqhSYfoaFo38PQHnnW7r9V52OW4GO-7r3I0D-zNPwjvogS2q_YWYBH7831BPb8o-Phpq9ZYbJHg0lpnD19hHy8twgiIJqepedpi2_H_luEETj-JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4jyxDxV7ODRBaSsgodQQ7MadP4jazlpfJIO0zZHV2qhO-UthKLDx_JklEoIpN0KJhO2rNgSXCmkse9sh4OBoS1DxjiXMa4dmi3xlCo4BXYEp_YFs1qvG9yhgn30-6VE4PE5gzmJBPFoYXRAjvnl_iffO5X_F_2iTyaR12Xo-9d1beREQDFtXoISmBy2dyWH56Dua3nZ3jeL_uw2tihMQVVG2wAsMChYQf2yc1mwo8l9l1FpNtVwqqBEcKnid3s-OWp3WXsYyI04qV1mvPag91VPkax4wmj2yvISF2ZXttuGLJnCtj0u7hZi36MY5cnlF_Pf9z3QCCR4BS3apxu1lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EplYG-692v58kVqLlD9aC5c-MkSk6bRp1n9JxmoJ5IiJnrUWtRyE-AXM-xpgz04n5vzCNXD5zQbp0RJ6zweIK7I9NuUTeuBh4Jz_9z9GdyCALj2xdWmWA4kzWUoE5Qhjyl4MU9gPhFAvDtw0QADfzJQHEvsb9B7-xE3jtV4st5OFALL88MNcFKgMD1Mt6GwKiTx4FjDGz9sAy6y5yVQIggzaerQ1whyd_CW77jpcb9onnoDdzkS-mIYKw63r-Ps3xjIciBdaGH3WqZaFgmhmHqxaCgCGhTIfNYbkQUQUo_HGv5l2x9ia_eTddA2miDRENlG5iMNSRMVDFnLTc_0hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWeKWr5dku7BfCS9vF88-6qt7NmK70zM_dkeeNcYh6w5mE-4lui8pqkH7b2TnWyrHn10a8QP_vF_easqx0MLBnM6t_CkC1Gy8BejFvudTyeDge5d-KGgw-j8eUdM72jK_YEXr9m0cY92cY7noh-mJPnc6N68kGupYTAjJa6LtVpoliPvzqMsxPt9NVPwGrKDMk55CsMXnKPDerOLDA3Ptofw7vZYnvKRG9_03K3h_kQPbzAEnwJK2HMSKhcFQ6pGm9viD39FkR8_dqHB2i6A92IAu3MCs-Blx2KXLF2gHB4W5tnBnb9NcuzyUkgZWXwJZo9oyi73J5OIWuXlfwwq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=Q5SAPIVgnFmcsXaACZYZwiMTlfOy1sFzpzO1kDOUD0cZCa8SznATVyzjyrqFfCx7hZXvpYU3-ofoEodvik0LjXsPY5YJEAHkdFUoJY40kIoSHRJCrzMx4MikOrvbLeGLhkR7SkyGQzubuSshnIe4RMrVd45T_ljIxjTaDLm3r61ukJQudNi8kDOuxzgf8KlCP_J663W23QN9_wjRbq_k3JYjPa9RXdYIcGqVjo32UpvK_phn1VwSn9wGZysLMv40DOPBRuy4nHncdk8-6X5z3O5KC9RwSO8O9aUYxS7Ev9ovtsdialSMKMZ5sADcUm7cW0jMdPMWNyXb2hptC_VBig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=Q5SAPIVgnFmcsXaACZYZwiMTlfOy1sFzpzO1kDOUD0cZCa8SznATVyzjyrqFfCx7hZXvpYU3-ofoEodvik0LjXsPY5YJEAHkdFUoJY40kIoSHRJCrzMx4MikOrvbLeGLhkR7SkyGQzubuSshnIe4RMrVd45T_ljIxjTaDLm3r61ukJQudNi8kDOuxzgf8KlCP_J663W23QN9_wjRbq_k3JYjPa9RXdYIcGqVjo32UpvK_phn1VwSn9wGZysLMv40DOPBRuy4nHncdk8-6X5z3O5KC9RwSO8O9aUYxS7Ev9ovtsdialSMKMZ5sADcUm7cW0jMdPMWNyXb2hptC_VBig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=BX-wgSf2aTsnqLtdaifG64_JSYYWdvwxHMhy0RdmA3sQHubVuH2tAf6RTWAfi161sXJZmyJ4XP4YdgMMo7-579oJlv0XfPRYvoSMbfzX3zkqaDLim0hF6AuWHuVo_rKrlmBnJymVVE1gjFvDMphtogP1aCGYRzxdM2z1igGMFh9dq0iWf3Q6lPPvaCx8bDrpi7Dgm3qkD4HM_LlVN-qtXXGMEVK6j-fx03TpvdBpZvrLEXqz4GTTkmr54TZtqBfd97kM9UprbxqfNG1IK1mH5OMQRHBbMTd-6JZKsz4fPTaZX5dzE8wiFESmkF99pPKXQ8ildsMXHZQchE8e1ueATQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=BX-wgSf2aTsnqLtdaifG64_JSYYWdvwxHMhy0RdmA3sQHubVuH2tAf6RTWAfi161sXJZmyJ4XP4YdgMMo7-579oJlv0XfPRYvoSMbfzX3zkqaDLim0hF6AuWHuVo_rKrlmBnJymVVE1gjFvDMphtogP1aCGYRzxdM2z1igGMFh9dq0iWf3Q6lPPvaCx8bDrpi7Dgm3qkD4HM_LlVN-qtXXGMEVK6j-fx03TpvdBpZvrLEXqz4GTTkmr54TZtqBfd97kM9UprbxqfNG1IK1mH5OMQRHBbMTd-6JZKsz4fPTaZX5dzE8wiFESmkF99pPKXQ8ildsMXHZQchE8e1ueATQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=KKHTn8-4sAnajPl_WBp45oqaA9PVpMNhToG_eFLnFgg1xfdbuzRbNxgKOq6Ruu8tLj9P1QGDumiPBxiHjfl8TYiaIBwY7a5OKSKaSP0dPRkK_QGfhc3lxtFOAA5ShiaHZ5VJVsC2kDxuNuN4vgdL2bxpH2-YdZYLCY7DTevVD_f1AQ4SnpDIZ1a5vdd3zfZMXno7I9ufzmTeUnaai5SLZDVIt8UB_PfvZKtBLDQOGV6tasS9P6ad9-FhR5JO6_1epLgO4JG_yf_E02G28F1Cl3CgtFLvCMZTZZafyfX8T_KxWTsftR9vALwFbeNfiBtwH5CTtdIgOwyKw4QYZtNwjAiXCdDxYBW1uqIfCnTVX3SaWu5Mo55lnvmiMjEYtJScv0p2kGuwA_kOG9nvsjV6zloYexbN8Q89u6VGRJGalTDS1w28kmFhi18ahz9fJ_-9XUAlNPwkWtUBe19Mi6EcveZxOyTJgQSNhaHNH83R-6dM5Xkb1DGsyOmA__mcOFra1ZuU0HUv7iJ10u_f8IMdAFiy1RjW4CVk7A82AdF7aU7OSwTM6gH7FlJ4crYC_1Y6EWam-8P48hjqoq6HXXwYpEQeZFRkTOBUqtsSbJVMnIuhbFJeUBuCuegHfTeKrvCZl0PKEDBB-RbppHF-NY3I2Jv4QGuEQ3blUJQHRZRhRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=KKHTn8-4sAnajPl_WBp45oqaA9PVpMNhToG_eFLnFgg1xfdbuzRbNxgKOq6Ruu8tLj9P1QGDumiPBxiHjfl8TYiaIBwY7a5OKSKaSP0dPRkK_QGfhc3lxtFOAA5ShiaHZ5VJVsC2kDxuNuN4vgdL2bxpH2-YdZYLCY7DTevVD_f1AQ4SnpDIZ1a5vdd3zfZMXno7I9ufzmTeUnaai5SLZDVIt8UB_PfvZKtBLDQOGV6tasS9P6ad9-FhR5JO6_1epLgO4JG_yf_E02G28F1Cl3CgtFLvCMZTZZafyfX8T_KxWTsftR9vALwFbeNfiBtwH5CTtdIgOwyKw4QYZtNwjAiXCdDxYBW1uqIfCnTVX3SaWu5Mo55lnvmiMjEYtJScv0p2kGuwA_kOG9nvsjV6zloYexbN8Q89u6VGRJGalTDS1w28kmFhi18ahz9fJ_-9XUAlNPwkWtUBe19Mi6EcveZxOyTJgQSNhaHNH83R-6dM5Xkb1DGsyOmA__mcOFra1ZuU0HUv7iJ10u_f8IMdAFiy1RjW4CVk7A82AdF7aU7OSwTM6gH7FlJ4crYC_1Y6EWam-8P48hjqoq6HXXwYpEQeZFRkTOBUqtsSbJVMnIuhbFJeUBuCuegHfTeKrvCZl0PKEDBB-RbppHF-NY3I2Jv4QGuEQ3blUJQHRZRhRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecJOQQcFv_t-keDeGHcoNz5-uoJ_XcEFu0xCNDpdmCVZo2PzlMBse15Lie_6h_aICy7L_1vw2G69M8tilvw26P37Hrba7VgKc3eBzT006GT6KvNESGY6DxktSWhhmwnz2bxwdq-0rI4_oSz3eGPMWxAcnosEtzbVmQ7g63bqBP9Cex7YkTGEPuUG9OM9f_h0hgaT166FuMAe-ywyRKyglznBUe8HLWqmZq97EMuYgGFsoeKryjS4yBHXq-lcO2_GD2NMLHaIZd3XKgE4CipmQZ0pI6HFEXBep82ynXKCyYfFrduBdOSZbRt59962VzVAVCB7uKCJOUB2NO84SOqz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bC43tbsBU3ykOHZxjI3f2HlBL0ElixL_Aki2EEmHxlbbvp1u4YiCCcx58Tv6O44GRwhwx9TM_p3kdSSjEMfrdJEZpZ8vx-x_sO0d1W4702Zxz3ObjJW2Yk57iWhBFnkODJ8Vq5fSSdDYJmOeNtPA9Ld6ZbSi3GgD7t0GB_COMG_JWSQw2QTHGjrEkccV_Ura57JMORjYo9oXNYZ-dTy0HpUONaNRfV6Dmi9zWtqOfXIf7hunAYfFM8wLhLHZCOlJh4k5wMO1XBSWGSaxmrn5vXdzw6WUuYiOmO9-kJyzBgV17otU1soI2aK9IWFIGQiBMRsp1sc9Y8UoskuNVuaxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bC43tbsBU3ykOHZxjI3f2HlBL0ElixL_Aki2EEmHxlbbvp1u4YiCCcx58Tv6O44GRwhwx9TM_p3kdSSjEMfrdJEZpZ8vx-x_sO0d1W4702Zxz3ObjJW2Yk57iWhBFnkODJ8Vq5fSSdDYJmOeNtPA9Ld6ZbSi3GgD7t0GB_COMG_JWSQw2QTHGjrEkccV_Ura57JMORjYo9oXNYZ-dTy0HpUONaNRfV6Dmi9zWtqOfXIf7hunAYfFM8wLhLHZCOlJh4k5wMO1XBSWGSaxmrn5vXdzw6WUuYiOmO9-kJyzBgV17otU1soI2aK9IWFIGQiBMRsp1sc9Y8UoskuNVuaxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8fLH4FIjEYVFwuy_yQL_DTIV0xnpgd2iBvvgFXUDOB7PN7fuLsin5VRcI4I0v6IMHRrxHCfbdROIp76_rEOszwzAuhfnmF-5KW3y-fpQHFELjtfjDG9pYu3bQfXbW5KSqjWTzJTM0m6_7lZBL2DZxQbhXP3XFqoHAmM9r-OuCG-W0HFjkf6d5uYLvYp-rHRTPxwhoa46XXRmHo-4b9_UoCBvqomKk07KE7FX2i5sou8l1ZTYBIVaVdppylmbYgwS1EydTqSbrNyhGwtKg61duf6Yses4Qzknff5DKgnlS4adOoS83-gMR3t6NIVmBpDQUN99dlXXuS3wikuWMMP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USvtGBY8QkGCUZwWHiTuaUDTj8LaF82MSWNuczMIiDiP5Vq7kAzoUZbJqa7WOTDlW_AaCd4oxCD4j0PzY3SY2bUeOrv9kK4LE36dN_laX87E_nTgbM6njtPHI3dF70WMzpIARmgYz1l9GfkWSZNrDJ_fcmvRcMtxLiIlDJxqC0lR1H8J5xLzCZQdYfdBilRfyaBUJtcZer6DM3IBb2V1t5WRNpcHjLJvFgb3kZvlGr8fyD3C211cvA4WqH679hhTPklB37-VlcrRtYNRu6T9zXharuZ5rOlTZJGVsLO1J0mUTn0F7LtHtTmYz6BpgQUmSt5ww7Teuq0kYvoULPUYhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUgn0sjiH6BhV8DsBmT46CL8JFb39ntS9y3mRYdce2YBOqHX2znocTeSWqDp914iQLPpSbmOOye7VvWqe9sU5zm4Hxy1kpwInecUOKpal_TYSZ2T435pUAAtrQS2RoA7AfWY6LW_9tVWOTR5GnuJdVvQb0CdCW1Xo4KJ9XArRlqtWTPL5tGi-P8jIIPzwkBPgtlGSkJLXQ3YGRF72lTzAxvYjnOQL0kmdYVv7UBENKoV0xrFNOAST5_2yqa6sYvhH4LLMUaqNkTB2N53aqOE2K2kEPHM0en-zjwTdCQIpiduyuMt80uk7B4OG_2PXL3rITrccYaABPaJ1M9I6TBUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0aVae3XR5Awor3jtHSIdrwQv9DCPWFoTOOC0j0JKJGUOx2m-JmUIulqOTDB0cXW_BCt8Aiu9wWNmmZ-2hAzjXQ4uFQQt9MzVUruxsY1Ns8zDI4BeU9fAuWAefSGWJQBZGuzbmkMlHX2JVgeByx9VjZdjT66IcziZXvFyAH188bPibpCz5k6ap_x2vmxkmzVxxXLZcWJNCPCAkFLqEg87eD1YZ1I-jwAUdDse-ryEiiguZZAQ7RB62AuhiZZpwhtuje9-1HUtq5EY6Tsy-EBWBIwmfvyUme6mPTrOgwPWJa0vJ-gKxrhGt1Khlf5zFXpK3OthB6jXJaYvioMsA2tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byxjpsFG_IH-kd91qBsU93OkDWkRqD4Tnq8RtLdlaZ5U6KUcjsstk8quqpAV1WbO_Oqe2lDRLABN71icT2Gd_1xpZJf2jya0OzXg1MN9oCvnUMZao-q5ajqz_omOzYg3Cc8FU_5KsPsKDVE79js1ycVXFQrv2gthAS072gCN0O2e0XiMb3DhNsjbyWamm7-_B2Bxqs642ZDBkiTfZnmF1TD6DKG7KN0jf9orFHFBnvzVppdgqlRA2qNlzURvPDqGlCWht5xEm0-atwCuAq-BOFCg9LJwQaM6rLpGs-u122azkwjAQHFHiF9a8NnD2Y2Zl2FKnZwJwh5D-KsBJAmvkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ZXfFR5t78vBEC7NZgM8cz80ri0cSI5eSCwZ_NuxuOcyQZzDdcdlTAdUrPkIo5VwO1pzHNTkKx8CKsfIxLUqurv_6jzAElKN0T02Opd3I9swMqJPpjEHT7fDXOWk1xar95EfSZsdFr-MDb0M8OyF-luKBWdbdFCHiTgS8xeBMQkwMGSADWlYw9AwaKcrUId9DEGSLdW3HYwe6nzY4E-0Zf8eemCMYmKXyEWPLhoCWGzetymK_dvHcyi-oB-iyFqT2eXTVJbkbXeyWyqMDuKEa3KrqeQFXoXi5euYC2x7KVP7Tvt5pFukG_ox5fXs2pDAXAUmpsfve1AZDrAonbS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f26YJcmMMmT6kqSmS0xn1XiOqX3A02jQY9CgBwFSFktHTJfewSTM1pd8OGYLCt3h9IFlF5DfBrW2aIKgqrbU4OETVQkKTTCloQvgSIwtZV5K5wg9g19KmWz89bk4f16W3Il3Yq7l7m76-b2Ou_AHFy0soSNwXsy7GizafohWEX3gG0h4-p9nN5P1s6hWRogGWCp4ZJk3osklhmuvNaQaSw2k2-Zl0Q2snOEuJcJT0y17R83eKZlF6_cbN7nNiuVXGrK8mJaybTNuHR8ioKT8f4-OIsvyCQylqqLdTL8wUve2HWlLg47u3McC7nRb_c-AAF9Cw98VwLbSTDHTWVWacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8A29FeStH6VX3Op6JqpnWKDMW8E9ihhCfcqCzJ0gwtPdfj_m_vvZj745bNSmYFs0eIb-ogKavAWRPqYoev19uZVNP5Wt0VAiex4ECtdsec46efDgNIDgsIBECRPaK6m4A4INpoNf7oqae6NvQaD4rXha0WLjiwkqiSwnYcYmPEBVAXnH1U_gHMxENgtZ8JDqUxMP_TC-h44EKKUR8Sl-C2FSbCM_-SufmzCB0onyHKckJ4PKKvqC0agfBH5m11R8kISmd7m13Rr-5WmwyQaauxZsgIjzQlNC-TbWBLg4MbBIfkaSUDlW46TQk_wM1BarYFnwCNarWQ2WyvtzGTIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvJK0YmWHnZ2ToHhw895MCgflKWlp_Dj7RTVnYCbhHmPQdqeNfK8ibYLdLsw_tjOwXU16YFPLlAcj7qLsM38jgVNGaX4O1r2858X2TWriVnMGsxLurbmJMq9uKRJinAEPOCrC0gmpI6CIw-xb7Dx3_kECWjfDJcVWbjo-3ubUDY1s8YQIlObDMEg4WvclvA3STr_zaFAGCVzbMEFdmJ1XYOhl_MO829jEn9r0Kao7uUXPHKdBssjf9ZRPeAhu-NkOYwjGyNj_9_9hTQyiVrOIkFPDHuGvn_7wpGJKfvGE1IEzgUkLMISNmTmwrNHPOv6RTIhvW-4vY0PdgmZ69gkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueo0XbnXCHaslbc5LQ9EmNJrmga9E4Lhp4vO1lge_303IAgYaELoeDOpWGiuZXOuDuSkSVMkIPNYCSJeUZIHAhg6C0FcVUCNPi_MesvjhNCMiu9wfXvuC7LKZUMFcxe-PIy-xsOVSbB6VQfCT-qrYYhctqGNTHrbCokPQ2HPUotdz7O3Qf2L4n8AkoxX-wfo3BhpYnVKSQom8q6Jt8t3Jz4MiNa15HUo8BK7OwXoIvQU1qOr7T8hkxhuGBR-CAC7ZgGCyfukTcqV41nwVSuQYetzODbfdBiQ-Xv0bodMNI7K1ATRb4cwFtvEI8Zi6oQNpbS4lKRmoKK_I4KqCc3O2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7Pbs2ykCHu8GbJ6RRUdQSSdsvhTjgUDhV4CarEIXC__ApokoXT4MflN0bc-fdTgceKhzHLYs4HeN1eCREmKs2uoEHXWNXWP3HAA3JFect008o5C46OelSor1Ba2ekDyaUGS_WQ9J8qDYtjJ9IkfImBxMQGIb50MlJBkPlBfo2zxRFhnmY3s_LatJB0VO2FVGh6xz6c-q4Fi26Ey1eLdpJG74oFQG3-QYx2tuqLLv21sl8mJI-vujOY5xds4XqRRX8GE6KCL3qrsTdcUTGA8UJF3ci0TlR5PXIS3X6wGYU4d8CuiK7gfVnWbNfcYitbNdlTVJ7ZATWXBUL-ATclkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sptOgkWHph-lWv0JTbyWjJ0h1JrJf-Lm88dbbzSJAwdBmB4T2nggIlkHY1cpdMatBIu4MNxZDPn_WBgOHGEIX7TGBnW9uwY5t2hkaOP7fvfBzAX0KyRbYMLUO5XdIIjEwTlFuW2D60tkXLgwPRZEdPQYeXwNtkKJ_JQMx-U9IJ98m3hi_TylrJEQKEKgqTRPJdG1SaXLuPm3aetJIptQLzNmUlcWiRAQ-W4O2pRQ58OpRyw1er_bD1GWDE5V1wRmodyp8g0w6lV5sEXW58TV8ryN1AG5po3kpvC8bGJ3JvqNw_uyPJyie9KHpbtOddvwZ9DZKvarGwiqcSpqtd3iVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toXdonR3EBe0oSJRX6HmaCZgTAH-KwygaMc6p0u6ZR-sNRwB8MUVTiZCKTSHeIhtnm0ePxX1pkK23_ToQ8tHiDOMTf5Lm3g1PxVijoaprXLLyle4ot9zjpxPmOd3wUdfITJxdWTVOkd-Z4rn0ITgwNwXwtkmOzGwDqeqXCwzP1q68E2vv03Hrr0Hmbm2XDWiWzaMF8M_-IVd62yCg4c8HTUG-g2Nid4FcSU-qPsZLHgkKntn_iKqeHYSOnirCQvU-6tWo2Jqj0eo63rmEckYIQMxsUFbz054aZ3WwFQByEHjB2HnpR2eX82ICy8e82DhcgadhxBOPX4T00d_vU6f2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjmznt6yysdFj3lCypyzlLi8YfxZYPpoCiJnS_z9YZxjaJzgxjJGk53ds5X9oN-glW_DAX--wHw-baMvVjadNp1ZM6aRBFFpOM7zj8eX56JVvMkjSpX5tpW1BxGClLGF8TFc6eiFcRYRQrGYlnV4S_On85D-9zsPowqqW__9S0Nop6OrEWd2xlK-BSxXy5GYws4MJu3DZon4Ke2xjsA7fEl9E3PiUYMqvQg3sazbwrSgwiEatudqlKDtvbcIqUQE3jfaXKQ1neGlFEfWrtfJ47fD3W2B1u1KY3UfkfCmRv0wM_6YfFQGYP-6nu2Ensg74SbZzkMSYPfWJmuGx9z9dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R90brMPqMD9AFJXVrvGUZjTWr-AQEc_7vwEBMRRbDcdfEWfcF-Ri8IhEbh6BNt6nybSGx2HGfA2WOhKy-E29qyhWuqL5U8rRJk1C01DYE7Zw3LnHXKe3Bru00o5Aij36ZM1T7ReHXTjMxbvxdhEzIKvAXMaWXRNlY_7GG-DdDr-wNUX3BRXZuj7EHBhlqvAkPagfDDlogaHujMKbFLW9at01ldQDf56Hf6Po4NKFLvdFlycMpdD70qIy38ssftMeEihuZYUTrGpu9bxRqekkyuuivljVucLqcDCeJsXa6Z2pMCrrZ92BN-RnPdrxUOU5_kEcglTXFahCGiVLs0VE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USfXEcKZNWgxAu-zCPsndypTdjtfC0Lu1gF7thgdqYvum_rFKfi5UH-tqeCIe-TScc7uG16lObrnRzP3etH26iq9NPgSIBK8_IgT0owwtY7hQRPjnKFrbMHVtqy_w50D3wwfcD0hyOjnIqB6ppJYL5gi5oSXKAf130kC9IGVxrRcImPZTlZGPwOqNrCASzI3ozaWz96h0brDzZGVi9tFTHNsTFdYlFM6AaOwuTImuLYevfM4IU5235W1UwYCzLYxJGG_kGMhiqWX4XYMy9e-TdV3_hy9lnYt91zHvnSmG3gCEuGqJzKRw4mtXcID3XcehXYFRruEL0L4tzae3YJTgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxycfc_ozCE-0i3kQJIZYki8ZqcTYLG1gLHLiWq8jbuMrwL7yYSvDt8yP73aSo9CpmSsqilN_FBnAwstJpQcc88Z-LnNcM1-JCooF5SE3oia_U_uDI8TJz2yo3eYigPBFM85hKm4XlJNt4-qzTkVH8sZWL6WanIAqssedBnMozm87jum7Xqg4fB3aPvbuay9UnYJdqiauBcPRZwwdXXoxSduAYZOJkfcZVMa28DXpLPfbpTFdpCwVzkCunEe8RtBbTxyITI93VuypQ8ekgvfVuVKjaHjfl88E807EuFBduow3WbGl2yJATNuRgstc75xeG-GlDPtYHLQA5CecUAj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
