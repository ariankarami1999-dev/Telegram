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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 21:23:56</div>
<hr>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_MYiELFmaCuRW4K5t0iXHsssd2nPiMseMwen1dgWTGx0m971qi-AcVBeISstXpS2AyhnVfeeXj43LZfC1a-n6iEhO1pLR5J8AjQeVBRIDzE0hoTO035zhwm40ORszerLXQ3R1EB7bdLoaPRi7z1gEHLYz1yPvQOeylFMUoWTsNdB-Wyj9WO6Lh_cKCtDskntTuSWGzhc64DTBaWW5NU6x0JofnTmwFHfCG8oI5v8NHEnW_23l3seiHCmfb9pwqZPsieW01qN7cWJ0SZVmNsxn58HBGoo7_XYd6Evpn52kw2uv84qYS14b1-kwxyfc2KIq2ogzrCXocJdHYsfBoUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg-Q3oMjNfneqGUWi4Z_1_MstfPfS4pGtLE4XIZUqBTrmlAEex5yamJ31WsLEbXUrJ-nvHulM5RyQayp6mY86zJcCG1upFCSb73SL8oMMmL_gudu__Yp3pqb3B-yyyfSCmrvmyP7wh-qerG7BMWcpRj2OHKl5Bl4g4bsa4IWs-nctM8EAgN2_DzbmkRtxe55kTQHaNeGyFet8H4R_GH-ka5iV0CRe3tuFntWAMvdDR5i1Ye3vByc9Wpgy4pUzgAuQbvLIIIZLZLOLofizDGc1LpDMGi1iOGo4m_gAvYvCBrrG8cOKcwv39kS_9hwyAh1KTughUDl2IpdIsjU-XK8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUBX3Qdqcbnf53lQGgTXV6dCFAb2qOwnIby2Q4oHGqZ7yEML1YV9gNozBzoiax9MY_dmkiPhtsiHevAIvLSWIzYFgZsP6fwjVCvsZ213RFFZWNOkRlrhsU5h6zQ8IQZgtPpD5bgmOHqQWxOlYYLM26WaPV-YJKZKEB22U72w4fa6tFsDLuFsVeZJPSJaRQEMvrkF6lB6CYCsDYaMybIhKyDBBSpegFNMxBtmIOe-H0SRu2FWZxzhdHPCw08tS6sWPf0q2wqTBmHXOhf4HaOC64CqC0-UhbQ66Z-vExq4HjJmkR9EwimULFg2EhzMJis8fyglBX-PPP7KvytCZgilLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-kOBSioRoYtMGTqcY-IBM8rWqdEzKzh872WkLXQ7m2MVmDG0U1JmkJpKriqo8REoTKUNlihb7IYSP6rI_SR3y6fYWu1KI_OUsZEo13y-l2-dqHYueY2p7EkcgXN2KUd6nGlLbRgXnIlXA4XnFxMIJSX9r9qNFadSzzi428XVl2eC8fSGLyesYa-Y5PFzW7nKPxvqKAvUYZzNzR0O_wiuytBcMkUUNOYDkrJTyHHNxIafbXoVldFCQmVDuLrsiSrA2GyyjwFfUnQa-sms6kaPpScnPH15M8Icp2n-zDCvJ1-JC5XECjVMKoSzohZY79RnLASckoa5v3_2jiV4y8XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgINaJIP1ZyAOPM3iTC1tLCFUVXkU_UlrWgn_cZDyZL7_JzY9rS7m-fg5YDxm1gqhfnEGab7we05E5HKJOTVQj-Lopr8P20f2JK8NwhoPLa3F2a9aZ5tCG1ONZNmLSzuIriy0ZK2KaBOJellWmjkKPx3_rldj7d0HM2crhcZxQEiloDan9ws0bFigfGZ8jDGtwJg_PKqvF-tcMuIkXaFbHUEPkiDTsh27Q6AFlJ8AFkNGs7Srm3NIs6CH77cc5VxBVuqWr58DSeI42rac_feM9Qu6IOkF7nUJlTVDYLJ5jIGq7n4kJe9MJMzFBQG0zNaSDPmHlvUnOCmrYXykYs01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm_fHN1nHjyvkaB-7tPOtmZceBjRoGHp3L4iX-tJZ5cMg2Kff5fgtMs1QiL0miXEGA9ycrJI9fFPON0ejXoAQBYMmlAMGA3JkN35ATa9LLfUljVrVdJ0jKI4ktTYju9lIYTzE-VodFMmxet1tBnwKkn7m9r0IE2pqysKnN6kyWjrfmqRhLNeC_7KHKAmQWoFc5CCqnSlPiRgZ2Z6s7YMx5v7eaTR2b6sNVde_oGhI4z5f-w8kpFIe-CCE1-CrsMY8139jkzD5xAbJfWz6_reCBBTdJyeN_oOFHsO_2vF0IvoUhzMWf09AWMlg-Jbw8yF3Pz2tygDA7aU7NRQt9Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMmKCFhB9pYWn_a6jsuz822pq2sb8jcKBrKDGiGghJmReZMhT6FLLr_8jISUrhdI1prpkTvo5aYakNG1yFYeV66GhsQCyYn_3McQC0AY1hP0v-icUhaE71oT_yLpYEnmGfOvOu-xSODoJvmBfSOuBW2U_IncU43uWAlJPTe5s-g6x5ixm9fpPvhpBuOMFmGEKD0Cag6FHpnDd2bO965spJy5MPssoYyXE6CN0vEINXAkSE_-AVgJv3EeMJymo2IejOg5cc4HhyudBc6ikzDaaGFLjJr1lOsLr7ecBS9IKBfl-r_WAi0ZyczU2Y1DeXIvWPvQsmyTqqRJexYhCTyPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss5LsYsSu1bTIb2UxXMd3N9qkH5zx22In_lszP513GGWkQaaaJJZ_Fmym-A_BHX0srIwHm8db2shPuvTVgvLfJCZwxokozeRNnSa3toSS8-2P0Knx5_QnSJPdBdcX2XAiZijT_I6G05RcwAqBuWfSyyExSBX5zzwGWYwguXHVRQndZaDynooC6zlo8PLC_xojC5Nk4Buwdpd-8cw__VSYhmvSXlIFGq5X80iocmT-fA4wsgZdoY2PwTZ9iQGnil0Keu1gPFDiLOWwN4Z_kC4DVkwd4js8Cc1ms85wHe1bFcRm9bnM0UvalOKySJyYhKD7CL2rkFmPNEgwkgaSU5Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW3GqkA_yUw4ZJ97Hniq7n8b7VY8gqwn48WozSD7BqYIdsRSSpphKzfvIFc7S46V3dybYUJcpIP41qqDdMol--i6s0PbeA6c1m1WF97JrpaqYRZq2B4nEgvbhhxkfJwkMQAZc1_fMTK3maKAVsM3fxWV_10g8m-f0gPEGz59tOkAaqa67BCaBu79NNqvrFg1yamaWyZDeKSjpb-s2sveUsE4ASK9ML0jwDN5pvHeXaiMxCviYd652yecRdQdIbEjRjI8J4RallO47rsSageC8jzbBDO2Yerb9JzIVSoRYNIsILxSQpO8Cn9AiM1DUn3d26Ev96Ow8iiPCuu0F0Ylxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=DvywSXMJveFCU0s9HQUY13slKabVbqnGx9Kq8_r5k_h4tAPlPBkDPLjx0pflLGu1UBZafNkWMZAaldxItNRihmfHJmvXklDBznuCUFmKurWZJaa4gVD4hR0JCcM9oP6_VE8I_YSFY4leZFpko4fQt0y5M86IksVCmXtHWX1iOXMI6qqDAvKWhj9nOqDCvxW3hHxR-SmxwjVeG6qNVd1sGzI6ipqkLR8RKhESzYai3iAMIl5HfPSIJ-263aj0b3zY4cQ0_Y2J_bt5-eXrrqnFMQVH6O5pxNSFTjhsuh9P4hghZXAE5_M3CyIw9kqIsAVsZAMrR1fNmg8zWB_PMSSMNQY3IUp11Hidlvb_fYg1XF5yQAW3ggR9ROiq9Clqs60sV6-dgx6rghgqZ0QIoX5tK3bIuu2J0IOL4WbK92RtT5B6tHtcJs6PMDPktlAXIdItvczypfMXsIUyAfMA-mA01U4FOyoql_PojXvy3hhpJufX1SPlHnDgcBoGJBJ6N2NmtqCAOWnzOW7QEYE2elyR5N9dG2K47Psc_8rcNquJ3nbZwmJRCs6FNv6PTsVAJ9919fwoeFlqZZbPAEy2CyiC7r5IQuO3D04gelv0kO2S7S-4djkQ_BXfvQxOp4sWFZfWVdJZ5zUoWt-ZyEg66msH1IGzN62X42l2ur4K100kfUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=DvywSXMJveFCU0s9HQUY13slKabVbqnGx9Kq8_r5k_h4tAPlPBkDPLjx0pflLGu1UBZafNkWMZAaldxItNRihmfHJmvXklDBznuCUFmKurWZJaa4gVD4hR0JCcM9oP6_VE8I_YSFY4leZFpko4fQt0y5M86IksVCmXtHWX1iOXMI6qqDAvKWhj9nOqDCvxW3hHxR-SmxwjVeG6qNVd1sGzI6ipqkLR8RKhESzYai3iAMIl5HfPSIJ-263aj0b3zY4cQ0_Y2J_bt5-eXrrqnFMQVH6O5pxNSFTjhsuh9P4hghZXAE5_M3CyIw9kqIsAVsZAMrR1fNmg8zWB_PMSSMNQY3IUp11Hidlvb_fYg1XF5yQAW3ggR9ROiq9Clqs60sV6-dgx6rghgqZ0QIoX5tK3bIuu2J0IOL4WbK92RtT5B6tHtcJs6PMDPktlAXIdItvczypfMXsIUyAfMA-mA01U4FOyoql_PojXvy3hhpJufX1SPlHnDgcBoGJBJ6N2NmtqCAOWnzOW7QEYE2elyR5N9dG2K47Psc_8rcNquJ3nbZwmJRCs6FNv6PTsVAJ9919fwoeFlqZZbPAEy2CyiC7r5IQuO3D04gelv0kO2S7S-4djkQ_BXfvQxOp4sWFZfWVdJZ5zUoWt-ZyEg66msH1IGzN62X42l2ur4K100kfUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub7H5bICdkFtgUF1Zm997D52JP6VKJeGC9_mPNPi1em-hWyuW5uV27QY0UjSXeCfmpU_4gEF3beztRUVBVTj8uiRDopdLnPmdyJUtUrFf2GB9ZOo51F0iYZ_eqe26wjZ8BywmhedRBvpmDm8Jf39rovjTCwKiKCxM-C3H7UxLsjuuMmDlIIttjvwSZpRuqxg7Ia0pmQfZ48vsNOTj1TzGElFayOGQerw2Ep5hezysotI8pgknoS1iS6HdOZ2C6yP8kiR5vM-xrC9d0rUQ6xYW3es8zVNyJKf8Q1zm2vJyKKHDxeLmurwQYFvFiC5oh_2qHcymUB4QQGiyH6gGJ93dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI52zQ-Hggpt4EztlbYr-RJVZLJaoOub-GCMhYCNy0ECeSNElqRUZSdIRCpa9LHMqiz3IMpSzHvPjd4J3e-HEi1WbYHLauuAUxJZAR6pmZ-lCXVTQop8NM_bUgJOX4UdnsYc8SOr8cmfqpnWUtftpiEFO-Yt5-q7hMDzlBWypFMnF0lQEwob8X-bDdXf_yDLgfS-ygoSi4g1sRQGYCwEfYut0JpuGoOStfQi2GQClXJvkWfTQDtZ9qgw9v5PutXB5O6ipsCy6s9QA2TOIotPIONjddbvK413z2yXvLMYEyV-lpI0_ZIpxNIv2Mc2BmilZpLvbZtfLBuPbHAbwM3KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJoUjNgQ-7CKFEnASY32Ja2LIJzZT5rs576gLmH-ExqwKY1m_n1pZnvDGczyFH2KLc6TE6detZ5XlaJGqueO4PYgim0GqBGVK2BX2gmG0TN4YQxWTL9r7Gqckg1uTS2E-dGYk96VW30Jiu8SJYp4c7AO4q6VNohYaBCGHD97mbkU_vVXwef2Ldfoqj_OXScY2lQUp9utgrkBKJAX9VYNemrVwcMWR1sJPblB2krNiPWg93W6CmLAq84FDnc3vWzuaaQtlRkM8GkguVnmIw156rmzf-2cB49iRPRZQ2FuNjsA3V9Llwx5jfytd1XWg2R-pD0_m-IQZI6bUGIXrREpxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eivk5UzuBcijkPbKizOqlg0Up3z1sjdMlYDihxmwAcebUtFrb0ayRc2qAl02RBYHzxDcmXvlUTcJzIneAzH4oIAKIk3eleDM11m4yFbICBHlV74MWKgpQ70EDDJGVY0r7iTZEI4IPuigrexgHWfZTgoFKXvRerWGP_-p9TjuWSLoDOqWAMu_5YiepaI0Eb3DTRwAQopujdiJJPHQ2P4gU2g9KyQgAX96FadiH964zPaupuaW2Gj4lo-gQ8gdjyWyeFnEO51wtr3_-6sXgXjFr9-9WTLbdHtY4O8kFO2-jU950h_m1K8KMezMVo3z5C4RcgtvO4RaKrf8P0M-cEymaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8jRAKPd303j_rXAgXEekpSidjPB1L3aOOBlsTRt7HKKd7y4QhUSSv4E91JFD6APDWyOhAx7WkcFyP2XPRxluWasBgIizZbwVAdsVQ4l1p7RZ2vcvXCKIrWr5wCJLe-vfS_oewppbM9D1LL7aSCX_-afprKYcYWaERPNkO5QiuM2PHI1_xtCnUBJnC0fPAL70b30yczJY_sWBXd-CTGoJ5l1UQ0MxKDy20l6lktn4HnlTl7-kmH6QLsHDnvbtigsgX4SNaQEsOu1kdXqoF8TBJ1u2M5vWpkvjCo66ourDqGS_ZOxRAqKbfT8nJMq582ziCPI9ORraEobVQJcFTgHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgXaFv0OVML-P_SRu59C-NzXL3Usi8pKn587BvnOk-yAl_11u78_ErivSs4uWIEFwOW6aGPc2wTkM8MmG396hkfGjp8H1ko9WE8S8CrXMBwu6GRDT_UbNL1YL7YGMvCjsuwTt5jzgoJGeGpTGoGzD8HFL9H-qa1qI0yLfA9KELA30cvLaXtWzxYufRs4-iDIeU39U71TO7s1pipA5aMYbrMtVciWHjdNeuNLjJqQWS2CKDTM9PIgpIRx24KY7srhab6gsiCYtSs29MbbrjLUHsWs3XdtiB4XPKWxX4YR-3VyJqfRtNEvvtfJT4tRu23HvIl0CM4LKobqBaO2HXRaNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac42fSOzOAJujsGM637KIATpxXjglDD9spcyZPg2hP1hsW5cxbiI74Uc5Ynpj4zLcYJPYQh2U0Ml22D71deOkiEB9pKYB-0nFX00d_WFKI0x1SLLvsgMBZx1WCdwYT8ZYbwAq_N5Woraxi8SXtyHQ6E0boMXjM6KhsHvEFD52nH_kzjDrD-KIUTXw2ArM7UdfPBit8TbQhKPKNlrkDO11wJpW6RaVpjPFFsSKymWv-a61YXZIk8k6Wayjub28r9MK8CFTJR0qFnHHHXu3-X6_NQMK43QV1nlNpW-0iLpZebdCWP2UMeYaVHmEA6Fu9FpLtzeiKmrqdIwImNiaNGgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Uz26EqDAMf5RiUQHy9JMj2wRsjdX6yBYpo91oXJGcb79DD4jV-P_vXPa7DFT9xg-xlK0zqP2OqpxbXICOdY9_2P_OBYD7caKdrh0rANGEBcimK5dvZ0dt1npgRFBOY5-vqR4ff2iffolJPZ_LbHL3EPv5p_am76sygjAs7nEF0vyvBzJv0dzAjypbE_WQ1Ko3RB1rX6UIhtow-UYF2hH-FEY44Xitik9hu3JP58Y4arA3yZn69kUBw6IY-E0el2m0lREfv7Opt7nk7FYh4Hm16Bflst1Z849FBQCV1cDQuoCfWpKAVXCN-8yDwNUZM_9mD2GP0Bd288jJnp3-TiSyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Uz26EqDAMf5RiUQHy9JMj2wRsjdX6yBYpo91oXJGcb79DD4jV-P_vXPa7DFT9xg-xlK0zqP2OqpxbXICOdY9_2P_OBYD7caKdrh0rANGEBcimK5dvZ0dt1npgRFBOY5-vqR4ff2iffolJPZ_LbHL3EPv5p_am76sygjAs7nEF0vyvBzJv0dzAjypbE_WQ1Ko3RB1rX6UIhtow-UYF2hH-FEY44Xitik9hu3JP58Y4arA3yZn69kUBw6IY-E0el2m0lREfv7Opt7nk7FYh4Hm16Bflst1Z849FBQCV1cDQuoCfWpKAVXCN-8yDwNUZM_9mD2GP0Bd288jJnp3-TiSyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipLB6t2XbEWtNbexuA74Y15sQYj86eDIsuaNp3djZe5c9zfWG4JRKnfpl_auqmng2gQ1_Vlqjqk48dI3duLKZ7ojonQy70N85-w4rewF6J2gmHl9qhXeltnbRiJV9ekQ3JOr-0FL8KXKHxFct0WfMXuFBakmX8Ro98J6m1sSEFcWQWqRCr5FP9Ts_Cjr15SLeCfzXchGllcnIJ3AHIPKf6TUFgjJFIKHiv7bVm0t5Vo2-I2HtoimxYxqej66MivPxO5iCGF5X40bOvU_l8qQfThkWpKCk82TtTHqYN8FFGODHpt4KE7gYKpRKFlEhUZyLzhGdhhWac7FQnl_5BoL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGzoOmX4-7k-ExJnDR-YxwIGQ5E5BMu4dFwI7bW0hALhTirxt4uLgwqtsV0TmhM4Z3UB7_4bkvLX2XhC4v5LR6Uh0hrhBlrOLW_dPsfVWkKhT_5Dcp056XjXlCWAn5tn7K_Ocu1BbKBxn_EKSGqcvlPc7UAYsHyjFan3f1DpIN6pF0SN6pBKcytQHqmKhPP6XOA2TN0pCxfsPvm8e2-fZU66ueCYU_qIG7MlWeLe1jFg_XhLP_O8kFNBMzM5xhIbdvq7I5SBKEUTPC26HFVTnlX4UGWz2Eq6mqM5epb8Y-VqfScdfs5CziKIvjW8Eq9mvDdJugkKAOowsU6T8yGfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=SbJuvMPTMSn5jALb2A4OoOmsPqDzBAnjlmmLuEywJM1L0fsJ7tuuUP5IdG6dOzgLDiox0agPlWA_kwbVEheGWUYXllkMH1NHex3LL1zfO0Ks0AsEeRV2fy0ibrtRbFUYVW60HN5EtufoqD6eLkCzWxqUhNP-eKkrygtCFrFeBLouSWbtvJHNaR5dhG9x7CzFZofFj7mgcAl1Ke79GpcZimXhQNcyILDJG3V_4LEIsGkTd2NqY3QqInRplgx470wtdxuNtvFtIOvjZeu968EYvW7WLU81NDbL7WVZp1vYV_pzgnGsHhKx8Ms7QjCQ1PwB8bse8loOon7kLk9wtaA6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=SbJuvMPTMSn5jALb2A4OoOmsPqDzBAnjlmmLuEywJM1L0fsJ7tuuUP5IdG6dOzgLDiox0agPlWA_kwbVEheGWUYXllkMH1NHex3LL1zfO0Ks0AsEeRV2fy0ibrtRbFUYVW60HN5EtufoqD6eLkCzWxqUhNP-eKkrygtCFrFeBLouSWbtvJHNaR5dhG9x7CzFZofFj7mgcAl1Ke79GpcZimXhQNcyILDJG3V_4LEIsGkTd2NqY3QqInRplgx470wtdxuNtvFtIOvjZeu968EYvW7WLU81NDbL7WVZp1vYV_pzgnGsHhKx8Ms7QjCQ1PwB8bse8loOon7kLk9wtaA6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExSe-BcN4kTV0vHT5toEaO7T4fEXHW5MoqsJOvOw0P5gCJXqEEYGC8Mjd7ngPVrhdWoZktrEHrPF3hurqfwrcfuxS77wVmQ8i4YGopu64WYRHwsSTWqsLCz09ay8-2hMOwr_oajUsabzZwXxe4y475rQghnPkfyxGoYVHdVFWQ6MaML9XRu8ZuG2gB9e7jiH81pc-s7AiOGBoMpJgATt8satSJAssQ9kLxPslI5kGosn0u_wYGTfFjQCRv-K0jChI7zFC0nNpHN9U7XH1f68QAjTYv2rCuXjgl3brCJ6O7L9OGPkaJRZ0XGiZnr_XIMd5c12vmkcaXGZCE-vSS3vKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su45Hvdy29xEAoYjpKEPT52zUA7sl8CdT46pBzrGNhxu6FNm-8BSSufQ2LJVLEhuo8ayPjqyq8CMCoQY2xDEQIlwV4z7h1ZwTJUkKpG3wkCHl1ekd3G0qJtKupoSeOMK4YnLGfVyTxPCF-I2-VC8W8_daEsXQjehrJrBOJ8NObTR9QpB496IzQEu8c3qVrNpJ4t-Wy2YfH7Ln35hsfiqKyDwYIOAs-iFbXTPMVOI1GCO-LZu3BntqvqRmBY2-XeKKsgBsdsMUs3aKuhe4zlzWiVMgqnwYGLGCx4bHOjRF6f3xrKXqnl3yjE5876kbAxz1tgMxoHK-u6RdJ-dIkft9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=cnu6_lGf7-BaLCs_RnUyOsel3Sbl4qnw7dddzbWHRfyAzy7D6ccwO0MXB9UdEYeHVx9y84hJLWNBDzMIbd1zw7YH6UI1YzZ6g66dTFEMsOwfqCrGs9j9IPv5rR0YE3q8mnNcXKE6XbguoNEr3WrH3MyxMkiMvoFc7qYG62HO_RXsB8jYGK10r7fCIR1L19F5C_u-2UBHuPxgNc6fxNKYvqvPjYSTsurTLWroTvvkUMstTFcPo64UVIothJKHfuMjseJQYhabs8Ph56NR5Ymd6471-0qHpcYIByy-QMe_0dzcHVwLoYEXg-sRXPE8yex7K28fd2mqmz3HRfJZgU8JNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=cnu6_lGf7-BaLCs_RnUyOsel3Sbl4qnw7dddzbWHRfyAzy7D6ccwO0MXB9UdEYeHVx9y84hJLWNBDzMIbd1zw7YH6UI1YzZ6g66dTFEMsOwfqCrGs9j9IPv5rR0YE3q8mnNcXKE6XbguoNEr3WrH3MyxMkiMvoFc7qYG62HO_RXsB8jYGK10r7fCIR1L19F5C_u-2UBHuPxgNc6fxNKYvqvPjYSTsurTLWroTvvkUMstTFcPo64UVIothJKHfuMjseJQYhabs8Ph56NR5Ymd6471-0qHpcYIByy-QMe_0dzcHVwLoYEXg-sRXPE8yex7K28fd2mqmz3HRfJZgU8JNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=cnWUmZD0aGgmE84e8byuFJefNubVC2M2ptGhzbztI3GrNF8nLfWTT9nty6IpLCV0kHykajfO-OyQhfs_GxvQHz3yfQ-se841pyaLGXKHqAVu__wx3Odv-_Kc2owi1N15Lo-MtW34RzEwaeDBxvqvZxeAqEmST0sd_c308sQWGmlSXskavP3sONsEgxripVziGNuB9Fk5eqBGUvR05yNDDWTodIKgJtnnFOs0iLZpWTHA3g2F-VD7fiEWKInOGbq-jMoHvL2QmG2UmVocjWY04ksogmWBw6bC9g2ZsqA-LV06k0D3S4x5gF_NbxPq_d2P4o389sW4eHYNd6jT_XPXvamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=cnWUmZD0aGgmE84e8byuFJefNubVC2M2ptGhzbztI3GrNF8nLfWTT9nty6IpLCV0kHykajfO-OyQhfs_GxvQHz3yfQ-se841pyaLGXKHqAVu__wx3Odv-_Kc2owi1N15Lo-MtW34RzEwaeDBxvqvZxeAqEmST0sd_c308sQWGmlSXskavP3sONsEgxripVziGNuB9Fk5eqBGUvR05yNDDWTodIKgJtnnFOs0iLZpWTHA3g2F-VD7fiEWKInOGbq-jMoHvL2QmG2UmVocjWY04ksogmWBw6bC9g2ZsqA-LV06k0D3S4x5gF_NbxPq_d2P4o389sW4eHYNd6jT_XPXvamjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUmAHdwxDHf44ynwFVqMj97S5T0_f_taJmHBHGPSAjZIK1a1X4mu1F3CT13o4_-0kAPEcv4C3TSnuz8EKCFtYbw8mPYsphG_ToVqWb7ar652_o6Q0KxvDTLVDojh8IvtZBV2CQXObamKxuflTZDwCXazRwg2FVOzbgWqC9KiQKeI4QQIXODc-3XkJlo4-hPcfeAEcXgyGB9CE5hQnXCEmNDr2XyYcnSKbgP5QTsAfwSJ-ogsKJfs5JEYOud3dPhf_5QhFb8V36sIUHNaFzINDstOp1mAPlT6DSy4S95hN9pop2oExUlt5BskCkcRPY6Q7-MD8PYFuF10l2aJ-Dclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khtbKxJDqQlAYk9bCXgHLDK8BRYqcUFqBGwmNfXXOoz32gD-2xHxvTNSv8WNfGhOUhUyPReWs_mC3Dyo6gL5TkCdmiQb2CBfLJt5lp6gf-0d96NCi9rBA8rGofW5lmK-SZ1IAqNTcLrqumDnOgo7jKpweUzx7jQgQqfh0X11YgBJ2VSuv6x7BqkVRekYdvyZiWZKIBuExlLedd2-WwVQYBSIBgZ7WWQC86VYPtGh_WGSWV4rXtZ2ILX2GExRuC4SltO-e_SFVwNcp1--PA8y9ew9elL3gb5-pDHBBD8XiE-4LAQK1Wvxp8bk4wRetD-q9TR7KjKnY2UXhKpW0XKHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=iyiePRQU3WjY8tujNIGbq0IA1fDdRbH2-v8vOi-klI6hBPlso-iYlsWbHnkWyqFdkiV7ck8C8tFQEG2Q1A_TwAojHxwgHVNK2ZTUaz5mP7skEGIl6YyTXn4LMq05kY964JC5bm0j5QHeNapXGBEEd2UmilM3HLz0F8f-1WSAywVVtpNwGgmInZpWP2BrGU4QyOjyOES6LS1UWNV4SwzC68u2ZlKz4g_TZk2z53mweKuVzZB2bIx_T-WTIMKL7QsWBJ6l7R56sca9w5XL_SK_IDG3SkqLhlBL5MqekpZThEiozdFufnD0qBtZ6JwlD1VOj4hsdPeHdCn7CFsFkGCMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=iyiePRQU3WjY8tujNIGbq0IA1fDdRbH2-v8vOi-klI6hBPlso-iYlsWbHnkWyqFdkiV7ck8C8tFQEG2Q1A_TwAojHxwgHVNK2ZTUaz5mP7skEGIl6YyTXn4LMq05kY964JC5bm0j5QHeNapXGBEEd2UmilM3HLz0F8f-1WSAywVVtpNwGgmInZpWP2BrGU4QyOjyOES6LS1UWNV4SwzC68u2ZlKz4g_TZk2z53mweKuVzZB2bIx_T-WTIMKL7QsWBJ6l7R56sca9w5XL_SK_IDG3SkqLhlBL5MqekpZThEiozdFufnD0qBtZ6JwlD1VOj4hsdPeHdCn7CFsFkGCMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiiWXRjWIjiSc5JkFpNyxFMitUtIW1-5M-SyY91iCV0oHulHKqCikD5P9OnD-ssALlX3BAN4B8m2Ax56fxu-3z81IV-YWZpbA7bN7HBjMXAAl9ERJ5sfToBCNXz1IJNevXek8NY6e5LODvn8YZUq5nh1FKQvhQPx1zgsn7CDzk0ZqlrUuVahN2AXA2bfLR6iXxZA5U_VL9PWjhoq71x64aoRPGBIV5kre3ZTJkJQ4s4xOLagw0yU6Vxbrn_S-rCyh28AH-RgU4LUQj4VknRFcE_RNuKGVPxhz4WCAcgTXeRtyFU8RNUhSImYgMzjJ0b1c5guknEdPkUxcCO8YiEhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmKZKgIw0tu-ZFxPlEwflDkMga4XMoTPbWpsSRQqICR_O3Y8pR-n33n4pyFvHp66iBWTHajaF2tzaHp-wqj9KaMDjnrzF5cjxxJB7O0SEoVery3EsgcI9tFiM8OZI6A_aZaNobSxg1h6cfQ9uO0j61p62rFnyFpecdETKkPyAyzsL_FqU47jqmdYp44ccNpn-LhYs5bd-6NOIBRWE-74GTxFoCFtFkzHx2IoNOnUiML9eBft-MO9zDuTnMC2mmxUYAWgbOM5uo3v7jPq9MROdnp5yLmWzp9kxV3dlWBOLteAXpVGjJVxDReZCQWDwSdOskuOgZEt7rvET_GzmNNP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4JGAvcdq3drSDO9OE9zoY2B8XMWA6J4pss9A48IaPmwyM2Lyf4dbjm3RGPlOXlqHics2a8_vX31Uah8SSamJaO5lvdLKUaABtZr2K4qSrLgpWY5XW-ZpeyT01xwg1so0_zf9FFF4rN5Tvw5Ff1YGH_xAKoQVkrL1De3efMHi48UiHOyTQt_M_cbvzDqRP2girmag2VtHHu4-bgJ3OiiQNmWovA7KrLOc4Z3o9EYrvtmnt5L_ZrgRocWb6hPMy4xaAdD_gkyxLaGdpN4mHHV1FBuQbJUVy-ZOVb8FTzuGRAsGag8FS9WhZFWReX_iTpEArblNfWqnsQ5ia4HfcoMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZJud6nTNDEoSxrNhPLpQPZJWkB7HFoIrq928kmTaUKOsoTRUBM9kA8nOJcq5jIhGLm4cT2RebET5KP7BJOa4b5FX5iCKMZLOAYKeTvdmc5-mmClzo5ZUImJYZfqKvSfzveKvLrimMu9nIDaTiERdUKDqp9mrelKTIVcnHWGDx2JL9wlBLbh4jtGuGiwJgAifa2Ni8IVLaHJHbZH2RinxeLWrQgaBmC82OOCiUAFM-8Dr4urxU9UtCXpDOl7UgVMd-Y0MLLNnHmV_7LIDl2Ly_sa4qYLfsAVMDIlR70HiaSh0PTVCCeHC7ltg0zeG-vzNELkb0JtRGLte683wTcvHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLZJud6nTNDEoSxrNhPLpQPZJWkB7HFoIrq928kmTaUKOsoTRUBM9kA8nOJcq5jIhGLm4cT2RebET5KP7BJOa4b5FX5iCKMZLOAYKeTvdmc5-mmClzo5ZUImJYZfqKvSfzveKvLrimMu9nIDaTiERdUKDqp9mrelKTIVcnHWGDx2JL9wlBLbh4jtGuGiwJgAifa2Ni8IVLaHJHbZH2RinxeLWrQgaBmC82OOCiUAFM-8Dr4urxU9UtCXpDOl7UgVMd-Y0MLLNnHmV_7LIDl2Ly_sa4qYLfsAVMDIlR70HiaSh0PTVCCeHC7ltg0zeG-vzNELkb0JtRGLte683wTcvHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwYQ28SYHR_VVsUcBufyKAfBPHdOTdJ8k_yLjFna-y6TN9uQridQgsx436ZdAk1h3uJ79H9cB0mRqOJPFrROYLOb1ctjDgsgmOE3-3Qoynp3evnI_q8pwYoL8LWAs1LHaGK2YdU8F7-ATFnmp5KDPkCnazp0_j_bteP3uhbuXgITySAbLplc2tUWWL9UAvLf0knVLhglILZ1jhL0V39TgF99aKc4QrH99_AyqcXFadB-luITU6mKqNSdN1-KqLilb_zLg5hjYveMF33oZ6ADhTBGtwnm8f4-lNkdopRv8m5SzuRqj67DmAzlREs-u3X8VMQzRajJjY4belv8BCy3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFT90zK3r69mP0NgUMxJ8EMbqYjpu4Drs07-5hxryr4gyzFdSKwY0ELygsy3CC7oUu2s5gqCn-4NL4gzAYdJU74ODZvvrSEtxKw0AY3DlC2lRFlW-w_jK89JZvWUuWUSvhzP90eW9AjiaTiHeUqzpaJgApZF3DR4kuLUpl_XSFADLJK84eQRNe9si3eHABXYjFBBYY9JR2kmIvljYjSrwLcOfzxIjA96ougc7RWmvwa3C6gPS-W78z5AFx3k9YYiJiNLA6vH0AfkMlHPA_q8We8sIlU_da1rQNYPbkLoxr2hk-CBWSXwQIvqmOMA0e7oSMhKc2hUFn6nHjbPlJpOnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=kiq1rzrQ9rgWjAAZ4vY5MUSz6IhBD1r8iXYmGgQywcDRPGm2A_PpGt3_wODHGC3IckRtz5MWDe7TOzOHV3P7g1RcFGEqaWl1wgSRZcORHaWGbAHfRkCVbrq0EARWb3pPM-zOqCeKjc-rHYAjV6VYbDFwN7_zm3GSW-8wj6kglMBX-_xuO8z86PLUqQQTNh0O34t5W-PmaoYaE5oSmnD7h2uCTspgCklNcvhVj3F1b_aTXIXPzhgaWrnh61CcxCcwvxEtwUBjbH7n7dyNHu2V_4VSF682Ty7ZG4aevaFy4lUWFVduajJ5PwHJmItAwg8ZZHTueu-wKX_HgSvuIR4wqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=kiq1rzrQ9rgWjAAZ4vY5MUSz6IhBD1r8iXYmGgQywcDRPGm2A_PpGt3_wODHGC3IckRtz5MWDe7TOzOHV3P7g1RcFGEqaWl1wgSRZcORHaWGbAHfRkCVbrq0EARWb3pPM-zOqCeKjc-rHYAjV6VYbDFwN7_zm3GSW-8wj6kglMBX-_xuO8z86PLUqQQTNh0O34t5W-PmaoYaE5oSmnD7h2uCTspgCklNcvhVj3F1b_aTXIXPzhgaWrnh61CcxCcwvxEtwUBjbH7n7dyNHu2V_4VSF682Ty7ZG4aevaFy4lUWFVduajJ5PwHJmItAwg8ZZHTueu-wKX_HgSvuIR4wqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=SlY2WUeDQJu28Hdce4oXR4pJLEB8J6PaGAiRfM75HK4X64QB0eb0R29UNk3MFou03hvcbbT4qH-I7qsqhqNbokK7c2iGeF9mwHPrNWdv3H_dFuRaNMF_dgtOE9swGEsdE0kq1xFSq5OSTbS2p3dPZomJKkgQEfObNzZyN2_TbiWMi3_cqBUHpmOVbIradbSR86hU-Ud2qIwBGN8CSPXjZckcadu0WqJuJz3lTK_0fTUwKXR2N7X32UmtpRM994_X1x_poc5Lx4uc2dhDVW-pp1JJB0n-etjTByAZYAFDwrAh_ANhigpeU8XZxJDZbJPgzFS5zZ9ZdOKR3v-mBEnmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=SlY2WUeDQJu28Hdce4oXR4pJLEB8J6PaGAiRfM75HK4X64QB0eb0R29UNk3MFou03hvcbbT4qH-I7qsqhqNbokK7c2iGeF9mwHPrNWdv3H_dFuRaNMF_dgtOE9swGEsdE0kq1xFSq5OSTbS2p3dPZomJKkgQEfObNzZyN2_TbiWMi3_cqBUHpmOVbIradbSR86hU-Ud2qIwBGN8CSPXjZckcadu0WqJuJz3lTK_0fTUwKXR2N7X32UmtpRM994_X1x_poc5Lx4uc2dhDVW-pp1JJB0n-etjTByAZYAFDwrAh_ANhigpeU8XZxJDZbJPgzFS5zZ9ZdOKR3v-mBEnmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQTG609bpS66zM4If5wRzuSl3kn15tYXjwoWHECZLcXaWspKH5tYz6XOILrkz2OIFJbxhiLqr0Kul2daTZcvK4B1P6TCdv84Cz9gI1HCMtQ0E0AJHz3GTXkQsj1Qq77TD14Ys0zkathZ5BgtUTMHwlkDL8Dj5jmypA1EEliXhPeWV3YkhJqFDg_s2LRD8_iFnPhFdUVckLSiAL2QVtr_Z0NgtrXPg7CIce-A7LynBR0NKiWQccsGluTz23LuBJpYFzCkUwmjMDpKkFlYqUhRqO04Yu_hggim8qNinXxnDg457FyBlcx-s3AWbfJzbhU7z7tolkKej0xlk6IEzPfKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsfdwvNr4sYDbq4mFvvl5XBVLl6PCPGUvlCi70hUDIuhQIlRbZx3D0avvJdnnDt5q6aZOHJsfaaSUENvn1vNkz5DdWXjiB__gfpUqCIBPAskahFQ2du3tNjAH4vQpfJrMmx_OU2xaNCWAomF8W6unB1KsL8Hwmrr-3vFD9hidLYv1A0FSF4sZhoUi7M4iFOlHcbd5_P8HW9LXxhdNjq8Cy8ocqaG-zB3cs0Xq1RoZb6fXJrwWsNdvmcUvGQ_z2ZBner0_4dO1xEImjODmSRaNElgCv0ql7AHs6oDoXgoxE57HUQh63Ygk-LUPdV59cSFOhq7AwYNvKkQqZdlfmfj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=j54ioV8VR6DzuLDEfFSEw6ZPR0KyPyiOyCBoASsZKhf-CaFyAYQXf7smqVFrDFCjh3AklFtIv9E2DuHc_LAsDw7_K3SCky92DO4ADKn8wCWNzmi3UiomuQf0p2XXV2Vj1nLbhqdZiwi9WgrEIyclvZGI0kW0BDDR0yLm8fYx3IaOezRwVBBtYrfEsD_hiJvbDeRZuqEDbFrCwm-A6D83FmDykd4a7eXSL9wS9tuX-VSTQ5gPgZbgFKenIO6l9MZ2a0BQkDP92kLA2OdsfxeD7aon1Q5OIHBqJtgnOxcGcn6kz8LwZXkR5Tha5jN7tE5Av9XBRLRJBEfnh8BUKhMjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=j54ioV8VR6DzuLDEfFSEw6ZPR0KyPyiOyCBoASsZKhf-CaFyAYQXf7smqVFrDFCjh3AklFtIv9E2DuHc_LAsDw7_K3SCky92DO4ADKn8wCWNzmi3UiomuQf0p2XXV2Vj1nLbhqdZiwi9WgrEIyclvZGI0kW0BDDR0yLm8fYx3IaOezRwVBBtYrfEsD_hiJvbDeRZuqEDbFrCwm-A6D83FmDykd4a7eXSL9wS9tuX-VSTQ5gPgZbgFKenIO6l9MZ2a0BQkDP92kLA2OdsfxeD7aon1Q5OIHBqJtgnOxcGcn6kz8LwZXkR5Tha5jN7tE5Av9XBRLRJBEfnh8BUKhMjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=C4iInvnFfABMlhk7qlHaVfwNfESnU5DAyKW0ggwh7qG_1NVLh0mqDTLM_AGZuZp44pypqk2G3r28gwjT9FVPcVjHuGovcE-hHpHuO3U3AugjpbE8S4IQ9WR6CSVySpP8EWzjUnLUQ96aVqfvfY2FOGN9shH_ZBxB0PKX8fcfy8eh-6e1G0AgJJgJKG8WzSAt1UPxk7nmN1_FL0riV0aa_hx_R921v9iDONqPAZ02vAyK0Jl1NHCbqW0aGNalaxSSYAsm9S_oPi9ZBiz7Hd7wdg3l_-VcwAk_QNphkDa1Cm86a6i0zuC741Y_uWXsL3Rkenu5yiGMw__8f_2oWKgjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=C4iInvnFfABMlhk7qlHaVfwNfESnU5DAyKW0ggwh7qG_1NVLh0mqDTLM_AGZuZp44pypqk2G3r28gwjT9FVPcVjHuGovcE-hHpHuO3U3AugjpbE8S4IQ9WR6CSVySpP8EWzjUnLUQ96aVqfvfY2FOGN9shH_ZBxB0PKX8fcfy8eh-6e1G0AgJJgJKG8WzSAt1UPxk7nmN1_FL0riV0aa_hx_R921v9iDONqPAZ02vAyK0Jl1NHCbqW0aGNalaxSSYAsm9S_oPi9ZBiz7Hd7wdg3l_-VcwAk_QNphkDa1Cm86a6i0zuC741Y_uWXsL3Rkenu5yiGMw__8f_2oWKgjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVj8ZOx75Hpp4nP-alwv9WvbhWE2DHWvz9sx6urgezvfiAzy8C_VPCv_F-8CE0Q80cJ3QbMo0xhvwzpyXpNtepmEl3oeAZSbXe0v5oSpUJ8gi1FmcwHw-hoUe_ZXkfDjp7J3pZFwIUFDwWgUrlO3rUeYVP1GslLwFlsomB0rRLkK_xGtha_m1hNZ-GqjqI-PA_sXjsy_GywxDWwDSPvnY4m1_Q1uwH5hK7LAUxTyGEWO0NI6kjreWzi6R7YkwSdfSU99IBWEjmP636yoPphqfrGp3x1K3E1yaGTN2kknsoiBeJp_KhQKBhlZG1ASuFQCvtPkjPgK20eSUjCJQXJyxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTBvozStt4k3_X98CYfwnVCk36NLOB9xXzed_sukZfbUs2GiPIlxw_YrDhyw3nDDfVMPjytUgUzlgbwAFOLabzm61rXenJOfCufG1RpZIsulxNBs2yUD7SzDGyYL1Vvonj-fLNLwDVchFL7emUCwRmqbeBcFPXcJLrltLe81TgFdTiXuzxENDRAQOv4ERP3dher3EgyPyokHOujW1ypXXb-Wj_i9KTMv85GmpfHnjy9zZySwYLRbDRMSgSgiU2pVp41P8Zza2fiwg92GoOoLMdovhx-uoYodPcTi1rS_GX61wKH4JEFb9DRP-OL4L5KDBRUbPrEkt2EE7eeLZFn9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMFBCWv-WBO73Rc3KtIXL9eYV7jqxNZIbXfX_tFzuZM39d0CL43SYaKLfFbDHyAJb7SCZc6jTdAUCJSZS12g-DppS-sWBoop4RyEGqa74jj2cNqA4QoOC--jyMBpr343_rSJO3uJEP6BF5jen7Gts7MIL961KnM5vves-woViXPr3D1KMcTEOgxU_K6QYF5fGUc3CdeF5L8uQ9iyBMBXRu68ab8-RL_v3VPwVOjB0bG7qAaVy2MnPH4wARslt_WvACEwP_e3qsYtIa_sEwDmwq_5yTKZ-tmO-9X7b6OystfPd7QDPdI_l2RDxLoOpxSwZATtgD2pggIJTo-UEG70LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONhB9331DfYS7-Wwmwepv-DW_Y2nPDpHudNOaKa1h8VUsxTaw2JtZ0YRzWUes90iQf0SKSSNhcF0kuVp1QiAfd33WOFEA4wKo8oQBol3s76gxWAXAXF4o8jaMMzjpH31wFeGvtEX-zSRFiF7-qoH7TKG1igODwr4l0ZgcFzVLswrfaJFz02lIQvKsllCMK6eja4jmvhfMwPuhFWCo45FJbicE9ax8Am1eg1T7VQpjwZLcif6zC08srnrsZNBMMMQBuH7EB6V2_3MlAGaN-4q8Nc3-UCnAa83eQBMcHJCzfX3peALKfDRO52aOyuBZohQrrGmNi2Tgth8ZCZOIEhaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFhu3ruw_ATdpTd2jBtXw-1divplcuM7530nnz2tG51dUytfeGzwPV31UDRI9nrfvKMG0dFsmMPFPJ0wFKQhSxaIV9ypgtcOnjsdP_s4gw93SDYqbUboKfSlIUvmkHmDhUZ37OluaTJVXElDf3i_o-cg4RBFZLdNcxulHaCN7GGSt1Ua-FsfrIb-ikyUr9ZC-D_wKZWS5tYlKj1h0_b7o8kDGTzKa2poMbC_-_S9MZGSersQtIsO4p7FUQ7g-KT9-9N4NDeXS8X1EQSeqqO0zjIgLmNy3B0VEompSAVwDTiYM_Ia4E2F1iMWWiX2ea3AntsORW_4iez25XUohoSxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWvbhvukSMk59h5K4RvnoySCWnjbQsuZIc7bNkMBa7Iw1LHjOh0wAVe7iTbY3v3GpbDx0SCNx0_T_SCWFySu1PCGe_HucAqZQt7rzP9SV2bFqH4hbiIdJP5OjKEpwFUezdxisW0IdPLpkEHtcd6tGS8xcFPZLwc9yM3mpMdbdASRKS8amNI6s5sRX73jZ7qZwBDlBZcL_gqOX9O37Szs3F_lVm0Sz1tvGcSKwqr75hWVAkqLKhcc3aWrKl59j0DP02-YL3Jfacik4L3ijrDfK8ccp4u_M3-93Yh6AthgQP3KTcDoTe1nqNowOYw0cffC90N37A61cAM6iz6sprZaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzOQs7GsI3YFGC03-xj5M3VHhRDjOARhdSU8By_3Kb7CT9SYK-03yLUCK_qWeZyG1t70UFzcDLB38AI5AbVEunPiiEB_MzTBMIMDKcW3MEsyZD2pDUyBVTcGPu9y4WS-gRf-UlN5BX9fgHXVoMA3jl5Fg00zbZ9-psaK1t9h7-0flEM3Yc80lwmvm32D6gvpKiM0JuZC3NsxemKl5gK4mpDtX1TQVfBpbL2MAKssJgVJiYxeCTHI72dBIOQ0byo0w5LLHMpq0j0O6nOvR8oRRuqltJ-n6m96T46OVxKFtb4-_nJmdfMhCiANvBBg3FckhqKMwk5GJMxIl2ZEZyqUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1voXkzhXFxA7LD0ffHARmRE0zc6Jq5-XCJ0tRu6eHnsBsBUueg0nCvBJu9y3tbz4dSgFZwAe1rVMJYzPA16DaxAeF7vPJ5_jbE06TdXFReE1ZzbCBTqPDiLzbsaWhQbFxvB2hu51OLAEsypJpT-zTdyyGGtIDC2NlOjy-KzFj7FN8cJhDxUCoQqzBbGQvMEJ7viYWLYBY2NRbEG_jWIW9f9ppED6KPzoiNr9p61uoxeWI6fwbi2yii4cQlXRmwLxiUX3fW3A77myvPtnjk7JaAidyIBhcxDVbV66FvccIsMi3sIPoIbPPkLErAbkhG-IOXi89hjfco83rjex_PY8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiS1LYDtKqyp-UsNZ31WQU5JVvHTRay2MiUM5d44WwpsBUw2lZFDbycdGbAaeGM0iJIm3WEr752ArD97h1cUSb53s8clezYnaQ8QiJseHHL4JxJ0UayyqWcugDA_lqRHnmzjXo7WfChUvHRDJ0W_ALIOKQr7x7NtXqzMsEcjizo4lLwH3HFwQC-6Fm4MWAuK8IqqPRgyEja0A_FK1zSeN08FMxUUcuz3p5dz8JN76RQNbc0iJq4fiisrBRBWZZ5hAv8c125lCRsu0FtNtAZk9t7Z7RJG2s7xD2WnEP50KFmqIjdJEPb-znehrkCVroL_3Rom95aslYSlWQ8cHlFpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0cuyxSvu0WxDoQoQ0SMcW1Ef40zKMUKYPGRmBC8bIQZENg9Nnm0caXXK7vSt7KyW3XhAd6fOj2gRYHj4wGf4E2HgNEk44Z6TdBdu1b35M5ryAPicMW_w5beQVh5WJzch59NBPg_f1ozlZ7pcQmC0_PtHLyd9r5XuaitN_lFSW_G5Dwqx14w6MhAOKFecZ5bTdX5QZ_AEst1Wr2qK57gvvzyM00FcToM6K9PDJzJ0p-COshhCGcecLZh9Qai9GIwCeThC7XJa9q9taD8E91MoNc0Cjw-CNYYvUOWDgEsK-BRrsE4ML9SHl-qIZXC6sfvmBCcP1nQ953eY2wdthVghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=bOxShli2vFNDT0hDK2JD3Pt2cufgeCVuq6rX70Hr3Y2xRplO37SnS2VqD-bu0B28xM_cJ-A-rDkIIHNJGx8GJqsglOdo1q4Ur1UhSDleD-OZKcXhSlAwo3WhhiwAx4VgZRCNX-PA6MRWbmdPIyTtHbCmdCQdc8_IkI-B51lDE3KEyezZCYBRjMoMcXwNoIMy8I_WgX4RmyhQcckVxuJb3vPjqebaUAATS3XTkdk0yVemXkiJFKi7UTyBF5zk668q1IMN3yKQGjFdUQtBm5q4JvhOJ7MAN-IHo43442YTkYElgA4SY3zl4Le_C4xKz7nSJ4CrWk9-oLS92H-x45KLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=bOxShli2vFNDT0hDK2JD3Pt2cufgeCVuq6rX70Hr3Y2xRplO37SnS2VqD-bu0B28xM_cJ-A-rDkIIHNJGx8GJqsglOdo1q4Ur1UhSDleD-OZKcXhSlAwo3WhhiwAx4VgZRCNX-PA6MRWbmdPIyTtHbCmdCQdc8_IkI-B51lDE3KEyezZCYBRjMoMcXwNoIMy8I_WgX4RmyhQcckVxuJb3vPjqebaUAATS3XTkdk0yVemXkiJFKi7UTyBF5zk668q1IMN3yKQGjFdUQtBm5q4JvhOJ7MAN-IHo43442YTkYElgA4SY3zl4Le_C4xKz7nSJ4CrWk9-oLS92H-x45KLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=U0PMku06Ni51nOqBBwMuJBqErIYEEIBR4oXSRn9jmRRQ3T0oiaOihriJ60V_3Yr_WuQNF4FA42taPMmKYS6gAbAN4iocshX6_bayr7BJwqQC7KCb8oKiP-h7hdX0mdSG28BkmjaSSgvaWAjKegp4LpNZPasXZucdpi35yhG_JPBH7CPmLmWjjAwrOpT5u3Zcz1ynzp4wSLgnisdFl8AvvINU5L8qqzh-rE52y8eTSi5TnZz4ZnjxH7NyzrKTo2thTpgw9zweikr9XdJxaIWY1_8fyGcS7fP1yHuO7314Gcltoopn82bSKO5oX9N2nRoX4dp4-eqo8NBAoe5RhHn03A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=U0PMku06Ni51nOqBBwMuJBqErIYEEIBR4oXSRn9jmRRQ3T0oiaOihriJ60V_3Yr_WuQNF4FA42taPMmKYS6gAbAN4iocshX6_bayr7BJwqQC7KCb8oKiP-h7hdX0mdSG28BkmjaSSgvaWAjKegp4LpNZPasXZucdpi35yhG_JPBH7CPmLmWjjAwrOpT5u3Zcz1ynzp4wSLgnisdFl8AvvINU5L8qqzh-rE52y8eTSi5TnZz4ZnjxH7NyzrKTo2thTpgw9zweikr9XdJxaIWY1_8fyGcS7fP1yHuO7314Gcltoopn82bSKO5oX9N2nRoX4dp4-eqo8NBAoe5RhHn03A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=alQw37fmxrCtQwlN8AWXBzG94-x3Wo_vWGUqP7lMykHDq07eU8Cyl9cWsVcTxAESXgpIKgxHM6iD790Bg3DhI90QEinMCXQSzzt6zQmYQofRcMwUaA5qg25MjfDpDcw_KBAAVHudCLK_1YSOwNJIMY1cmi56FWpHYwa_zvW8JwImJQE_9FXrRuR6p7q0WBQK1Bkp0BxGqkv9c4J9M_Cy2c2EfmjmSbAQUdo1C_l0T1BE4hmYwVv2c0rwhZPGhxsJjt9_CqgjbjwAu4CumUAYpObW-888BIe8wKPEUupjy_pf_tQS9mh6Kx6GPOOpCFbz-KlJxFXMdMrA-cj5FcC6wpZ4ImnBhFdOREjXHQGMp8CxAo7-gK5NC5U-j9u_BtolkiC5mabAGAxsq79AizTn45qqgxZaeQRk5KP2cz7qhSRr9YF8-6_PUMcJAknDvdTtsHXwZg1guMEdEZ-9J1uYmREGNt8jK1PMHPaCdYI0JdNeCLN_QeOUXHfaC5VSvY0I709FNEagkidgayZcoASSXNJ3Ov5dwMopzgSrzCP8mUig0zDYldVx2zCQ_vz2h-aElPo-HDi97M7V14w8WAIXnZMZLTV7WP1UHu2vutpiLdNwwz_WOfW8km-QRurQDCvYZKu78EpurTtUghHr0uMHR5PrUKIkq8sk9zRCuPKC8ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=alQw37fmxrCtQwlN8AWXBzG94-x3Wo_vWGUqP7lMykHDq07eU8Cyl9cWsVcTxAESXgpIKgxHM6iD790Bg3DhI90QEinMCXQSzzt6zQmYQofRcMwUaA5qg25MjfDpDcw_KBAAVHudCLK_1YSOwNJIMY1cmi56FWpHYwa_zvW8JwImJQE_9FXrRuR6p7q0WBQK1Bkp0BxGqkv9c4J9M_Cy2c2EfmjmSbAQUdo1C_l0T1BE4hmYwVv2c0rwhZPGhxsJjt9_CqgjbjwAu4CumUAYpObW-888BIe8wKPEUupjy_pf_tQS9mh6Kx6GPOOpCFbz-KlJxFXMdMrA-cj5FcC6wpZ4ImnBhFdOREjXHQGMp8CxAo7-gK5NC5U-j9u_BtolkiC5mabAGAxsq79AizTn45qqgxZaeQRk5KP2cz7qhSRr9YF8-6_PUMcJAknDvdTtsHXwZg1guMEdEZ-9J1uYmREGNt8jK1PMHPaCdYI0JdNeCLN_QeOUXHfaC5VSvY0I709FNEagkidgayZcoASSXNJ3Ov5dwMopzgSrzCP8mUig0zDYldVx2zCQ_vz2h-aElPo-HDi97M7V14w8WAIXnZMZLTV7WP1UHu2vutpiLdNwwz_WOfW8km-QRurQDCvYZKu78EpurTtUghHr0uMHR5PrUKIkq8sk9zRCuPKC8ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ErjXUx5IYgRMOK8gCmf8_72xSTNDFBW69JqqbLq9TvM23vS1rLUeve6utQPWsGU-MgozdHfbvRaBT5aZRyGgt8hZP8iQWfxD33im4J6s3gUdPKvfbrIva3zykWpS2Xw2V9uj-soVd7owWw7LC9ztc5DngI_e8hgl6f3pi1_yF4xm703tvrkD9uI2nzG0Iki3DU7ABjpW0FyK76UDpBSsfvWVo2T8zfPpFq8BT2DpS0dX3FTGW0kB2ZHei2_2oWTy-Uk0QPlIQy5mPfW2Sm4tEnkLLPZOAGRMy-O_hyNTa0MAYVYhKxyaKI_e3RBL347ZHfSNch5Fb_e0iMLm3hWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=vHe8A8IVzm8HpIgDXwfaAB-AjVutTcD7UUiK0wacpAyQbMzBDqGDhcomZtLSrLgDZj6UoEaJHeAWNAPCHSG9CtbBakrY4SXxGBr1N4naCb8qCs6siW0rrBmlpEbehsOC7t9p1OqsSr6FkwuWCIaHppqIASS5uAS1_GQMWG7ES4Tqmy1-sFrl7f3avywbkSM9PMdc4qPOKapYqKC3d-sbnpnwXiipLI-Akjix0dehyUmabPBDIjk20XSIcJLr_WTc3q-uW78FB3v64aKhTyrypX6qp9aPGTGajBF-NYYLcbb1ewme_ZDgJ8u8Pz_L7WfVNbvyfakx12mdzXl0Tvg-Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=vHe8A8IVzm8HpIgDXwfaAB-AjVutTcD7UUiK0wacpAyQbMzBDqGDhcomZtLSrLgDZj6UoEaJHeAWNAPCHSG9CtbBakrY4SXxGBr1N4naCb8qCs6siW0rrBmlpEbehsOC7t9p1OqsSr6FkwuWCIaHppqIASS5uAS1_GQMWG7ES4Tqmy1-sFrl7f3avywbkSM9PMdc4qPOKapYqKC3d-sbnpnwXiipLI-Akjix0dehyUmabPBDIjk20XSIcJLr_WTc3q-uW78FB3v64aKhTyrypX6qp9aPGTGajBF-NYYLcbb1ewme_ZDgJ8u8Pz_L7WfVNbvyfakx12mdzXl0Tvg-Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5bgGy4C4KbCJzyLv3bYPvwePUy8mY0lSKl9Al6O3HvDD4McFgJL_xdKvA0zm0Ji4c9ibDJsYFswZ5V6ibLR5unXX-Mvp2eX26eeAJBHRE7Gvl_pgZnaq72cQx9GKdaPazxFjHWW_JnjBBhy0L217VVlU-RMpS6VQaK7vzH7zaRwlY2wcwGUIexpLOiBCzMsC1KUuTEZ-PDgmZNJ3NQEKw8syzg3o7scg76VxT3RYIXEnFnkzRjeteWWMJutTsHI1bKAXw3y4xN3xtF16EAarhXALnT_ToAZr2hUu_V2uF2_poirT27cL0bf1Wgy6yPvYEV0z6NLeKiXSarv-8SxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuXH51NfBXDDk1lo6fNMFkmAURqU6KUCE-5_rHpOW4CoGxhbSWR_aktU_RDl7YTym7xWEVOCZ2xtXvnHn0YN-lILnHnfrNbLwTcnSyEtUSqNYpVL3GVfh76IeKLUKJFFi2SBOaXSYyVYNlt6ZFmrODTIN0K4hikPGfVnLAcWJASGiSOrAD1-N2QoiVQm0PK08sLwfmmQ8-OQAi439JFkhd2v3fy6sbWUcx4T-LRwYofpfvpDXEgGIE_RtEaHkJ1MKcuxGwoKRaFHwFZWYCZHZf3_7mLcCz8RpnZHZiDWdbeAKUilCpzktcD-_1dQc1c1ZNX9PAx9YMteH9OivueN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E26fBM9vcr6lbHCnC-SCZ5W50gJ_QN4PIuKTZNodwQWYRKPUuMNaUXJf-N7Xp_Xy3InKAN-SoBjlWvbxlhKqn-gKWdSZuWCd1DI0lldyHUkBZeKr4ibSqeBblmGteCpATP5vDycJTqF0oozMKYjJpkcLyNcNr3UfHlkrNozQZ7xxpP-UPuzxYmE93MSGKFc1melM88uK5dXYYfNYHi-SqIr4jM2TKq7PDtAQlRTw4D9QfJiMfdTMMmVTFik_pxKqHSxGWkGSphBvGsOAxXWazKKCooBcThEmPi_hd0zL4sbuy90wRPhnxtU-OG8KgagjPd2PMYunTsxVQrBO3odQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hy-BPygSIWHVEwQOBQcLaBihm96xEB69Fa12aGFPDieFb-YeVaf8kwVW-VOWhiQb2d3uCFgoVcDDKC5DIhGbEkzPyIT2oJP4NDqOh33kz3Cr0IylOwUmsKwxJm-_DAJUrJOwzc8rjhIubVmctCmyJavLwJCgO7-Guf1HuGwnemsGTc1CIf7aJF_BUddpuiqe6_b9mvDlwrP7okqTjPHDY-ICuhnD4iksQBLOZJj7O0FYgY8bjn5ZnbdlrEsejcBJrSZdjD9k5in7UWLDSNaQs1kHG4bK3IGMuDi8FSsGnHQVgXD_nGCJ09f3H-6j-lCDyXOSw7d4r-eX3yEkMe77cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlt0QuAmf9ckPLiJyqIAVS101ZT1ip_D9AiSMbaSrk0Y-E5-HtuG1El1WecDlrBbUh6W_ji6CatwLB4mmIsGMvtYgMX9-qN9CAnrzADXSmHNEVzqpae7LoGsdpmQym3K2Oxmo8M1Tw42Cq3Q2XQWoGHvmR5Dyj8xMhPwHd60EPEfHt2QHmpLp-PMHqakV1J3I8BLFOqSjHifdbMaZ9L6sC6u8sgN2LrU4fAagIcBWvtJmTng4gRvV4c0Ugyv-_YVmnvFtS2udNNEfqQ6tMzpjXkD_Wcid4_mB1_tmgfemRCa9PCEZDuq4q2i1iwuqqFOxX13LZ3thmICllASrvMB9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MExQSh4zmc5SivGZ_CF9NxDrhJkRxTQZYVaiBZIWUlK07_r3Any9mkTuPCkf0DpZiF0_NEY_xGS02FODwQrDJb_UtbUq87WBhHLIeAklfUXyC2ruSbqO6O0qz42qcw085icPtRwnrPhkSAnteqoLl2tnmzmCpPe8WKrsxq9Zv4J1dEvGOFwRE4Wbrej-nDk6QoIL6BV-901hd9FnkQ-it6Wnrb-9kAgyTRHTruV_DU5Fqg8DnnpDmPFyY5E_2-oa9E2uz0F7ObuTS5H1U0GeRxKxWgoj-HqqWtGuqfTbON8e12qJ_PKVr2YErTlj77jgGmKJ0HTDq_q6l8VKiO2yIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHlU8Y3d2xALLejTwt2ScbsyDKHeSZcvIB1MuzYIf0q59HMQaIC84HLjyZjDm6Pw8UKzP8KKlEBLNAORQORJ2xqIVHhIY1kjvIr2RsrQoFhT9YDq3CE_KdNkvBScQqC5KZor__CNimj64U0MMDstiD0YstDxvUhIcvKRPctd0-dw-JEQ71OF0KgZ75f0n6HMgHdD7QSgL4xQYNyv9IC5uj1ETWkqYuS-Hoeayf5Gv4YyH9f0O4Ba5XgtluaKR1_DP3eWyOoOECI1Nqz1ulZxxi5yMxx_AMicI9BAZl2hJjXlVe3Dq92ySmwRi3-LLOLNJkRPs7FDFSwh0pBW3EYESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCMV-rgzcQSMyx8Yq_YJAGAs9YPQcaAT2PXzLd27qMU660oflJMdcu71afBEzSIJ-1C2IElkghizMutXob-8rp7tIWGqmBNqt8kOX-hq3nsWAjmQUlt9DqueQwrHQwkN9GdxCJ4zbz_Q6VjKRkFiFdtDVdKMhZ5zJ3TM5sqbnGBta0P6OqiymT_EntjSp67nxsXDw0GGqALS9Q61R1OVgseHIRKEszdOTp6A-54b0PlRYiLYZn-S-dOx9xaZ66-BOdlbLEdEKVKDBMNiSrox9dNFFtIuXc2cXWlRQFwFlAsCrgob07w-Cl2Nq30dxa0o2p8Mhii_KbY0Nz0CTa8a7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WM9kZggUIF2xRu7WoB4oCgVyzMlG6ih72-QocTy0g3WJBnm3-4wDwruEyWrqm0SzmoSAbDYjxekxqD00D4oIKCtfbwdb2onmMdzrJ2SLjlKOxUQIEJhmW_IfL8eTDZ7765aLc6UNL7l9vsOr6oRwLsepX410uur38yAq-tRud6N_2bhR79bIY1inkFDGdAA_1tMWea5jmBxDm2ciOjmJ9KYs58KXPbxJxMWNc0jVXPogRebcG7HMGS23Gn0kqI15JXl1q-Pq3vUFRJimEALLrd9eIalo83k8Yy-Bc3Exn_O9QV4UMElxJkIZNg5HxvMLTrkUfobPQNseJbbT-Fzp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPWDCr-M2l7mHPuAuRiTJI_14lROQX363qcavtW4zPanoZtzfsqP_jIplO9XCKHTpk6dVzjDBOjSUDTqn4WJFWMgxvvVdLv0wC4tCXIEdePJ1xMyQGVPrjz79wfw1HM4_rWGLr31zBugDHCQECk-eCGFrL76PR-XHBqEKctNrwWcBIzz2H1xMfeEAemOcLIfE3Keqm3Fc0_x9qu8T3BGzA8xpRIEE60EN_sWlBbuxpPoUCbyKWqPI5I9XWr7qkISGBn9Q48vF0gg6EE2DtnP74ARkvnv4Ak4jGG3jbE8O_RB_TFkUuM4lGTjXP9Li_szXR0nvTtEoatUOOutvcLRGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il0aW3tgEzo8RSb878h2lpl1rm9peKbOJP4Rk5U2uCe0Kts6OXJKUsGVFprMeKWTCBB-0ESESPjp2IIvCMble_QYYJy4ymnCxf6Fmf-wiDHuSOcXKXk11mqtDx_Fp_yAgwCnHIUv498R7qTNtOwCb3nBCYk6_utDtNocVOhyQFOOat16aIzY3YjVJqKzC9b87XY4hcmzSgU5aJiupAlaOF6H7frrGj78RmhEjLjhZUhlGiFiFnJQ6R0D4idVIht6k4tTGGhFo0ZUBpHiq0H7njMAStYWUXHcLPhYU49DOrZ7RJpVm2295Lms2-vUy5IPS2r4bqTuXpZSGchwY3_-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdXjwo7UUSUMdUL5IpzAKjGix0EOjpsAnLRsVMzUmD7WAGnbXlvjX61hN8gkONUKPfkfDUrz5PI6McHp1W_m71qYDQE-LIOnRuniw2Il6eEaK1rYTupvKmRrA2cVCyl7OB71iV7PZ-lTgb1X0d_ptm3pci_mtNYhwvduPq-2tf2eRvZBQTmur36pwZj5nPAfbGS2lhp_KWPyeTwA0412zzB1Ur8kEvT4IwCg5MJUfPxh-P4-EPpfMZWPQvTYpsOFEYb_Ki55pD1xplNJ9dkkI_RnBJOuqJ2RRE2UDGNBVk726uJfLjCu9wCLHeywt5bOPm2ZogH4lWTdMTo--V_FlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOHaS84AmXTb8LBq7yarKGZymUCa7TlL2cM7ZSff9e8mZ-1jwA9CIp04U6VBG4JyZYNKGzwNYEy1MDarcS1stR5XfZlxswEakWbxfteu7bt2Pcj8MlKs9y-KgNETPNAi7yh2n_SFWT-Ulm9IJSyAla8UeGBQOXHgMrZCcAyvQDe9DlU1e8_AzTeud_MDQBf_OThs6abXsTq0qsrU0dZOBJ3koM4uJOSgtQhtuguurG4hbPJCsDixDLXTjssg7HilyHqUVxX8hvmmzLCuu8welYvFnTh1nqgMk6nLw96EZu9bewrBJDAx4EJEMzBNDvFNCCTyp18KLmTxeBrmfQhCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZFwwIAJ73gubV2ZI-XD85w8tBnsYjTP5BqVFOylSfUJU254hwGVG_9gqPh1nDBxlPVZf2WcePs32vdQJntAxoZg-L2u4C_Y4Fkh3hmB6O-l1l2jg3gF4ZWmG887XoHGD4tzJoxyPbGATy-uvJY2dvuxSCjntBdhbxlPOZz_NQoYPYuZT5BtD18CFUXffat2Zfz6xL-xii24sjwnAaKuECgQFvVDLCiQhv647VFYwngdUCLiYOdmuqwxdkjbBA34ea7jPuFPFOvzsSlKDMg9U9zmBzCSHJeiC6_b09M_qPxdjkNrcmAKdAMNxKqqMS05C0Ujcgqp5yT-Kk83gM61jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnh4W1CeF1V6J2k-Ala6vYZHEa_1UJwHQPobFUVKGm2wi-_jVgk96-_N8DyS-yraQg9CaFcC4L83HL5d4nEjR7Ahq67zpqXXq8-YyrpdTS_ObJ6TJG9FCANZCHpaO1plDQBf7cs_NLXU8hW1mDbk7meOdOhAyDbNZ6Ce_LV9TmTvErtAC7YS5B-4l98Y5V12Kqi5Ey6GSnrkqzEescVuCs5TbQfUJGZjH0QE7FQ7JzfRinv7xnXQUQneNfWZA51nER1orPVdGpYy2BuQ6iPJ7a7jbCM19mpFXjgXoGuNdqXFbQavqI6ogXUmnnsNvgHZsnob0Wsbb9J2OE8i556QpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOdHpLUCUk4HIe9_jxgvkDcN9K_zqAc2c5y9__ligcqTNqFbwL67H80-mLkwuFcLwCYZWSnudV8IckB1kP3uXAqhBakNGhCwN3-1pcyJ06yRs84sMUPfinB_MmJOYbzuinPHm5DB59RXXlfNnbQOe10k4Di18ijT6PWSKX8i2Ol37-pb3EpGvQYedEaS1fFr8I_N7_CoCnCPlpllwwfugmjpYo0v6aZ3PMQzxLE69gfahRe_hhFotI7vRLRKUKitANIh-46Yh1rkPkrtzWt3hQK7vTiCmMz0GN_1N80L_y5bbYzBZoxvK8lWwhlIJpnKQY6JiKRUyCOOOV5a4w5j1A.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
