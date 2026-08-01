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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_youzS5n7_e2yDvafFYXXn57f41h6C6J3QbytiXVz-i-GfVZFe_PkCkWyFf9i8pcjqrSycx4XhWkVpAAx-8vBOkalgvrze8XBY1Pb4B-IQiUl-Bk9_2zPRo3dMEPDXcOF9dOZqc0ersHR4D8fXVeqY3_cZfQ1YM6QRL3qs5WMADRbCaH3ibkBAzmAZ28SGQBxEXDGVskaGZaBvO5u5DYteS859gmkxNbu8byLiQYJ_xR3M_6qZ7sJIs734n3ARObd4dZkW9XXFP7-biyErcmqLIRbJu0ZLRrsjLqp6IYBuTseIOs-elYasfqLoPVFRf2u6BevKkwk6Y9xz2ly-zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfZx36Wi5lQqPuJ_gPvT0mMZDEZQF00NlXCK9EKwp0-dG8tAODX__HY_vJX_DCc755jPQfUKDLOkxWLLZFGnwZo2DWamH8MeoMDsyZkeQAuYOI7NGfHkDiN08echvNQQ9SFqNNQ_Wl-zU3jGdfSTjKosq7QYhrf45rJ3VQpjQMxiTIf3erJSTroBo_P2cA80MzmxUn8pI2-bxL3kqYRkHkIc4qX1wkOTHqgyq6OOd60N9jyEQQ_ae8w-z4nfhIGaIrpJe5K57R_afSY1XF2D8YmFx9f_-Az9Hxu6aNCU2JO9jXBYQYy69WBbvW6hQ8AvQwJe7TIDJJAOKbxpiO0a4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=LTHqfxYDFX9FQyRYtj35fZ1uNH_BzHuTEMeWqjC-DVUSIyTBf-6nL48D7ZIy2J6T2qpluIEEqBFPB6HzBz3KZOlKtPkZG_x42VFAIitGx--CAeLc9t7G-0fvRDaGs_sNESBXyaSoX8SeF47KQKdVWaY-v-gB6vU0hW021LW0VN0QgdrCBA-7tb4nZVPmRb1JwETJRZtD3DF2ObfXfZ0pdHc6veIuWMcsDlmCecmWo_xUhG_nA-HJ_t4lw7xsM15ZbwoP-InoCbeKZU2F8w4FQuyr0Xb24g5Hd2hPM4mFdWFwFrnLMdRWTWFCTJPeX-OY62fawYZ6nTgh00nnXaZCeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=LTHqfxYDFX9FQyRYtj35fZ1uNH_BzHuTEMeWqjC-DVUSIyTBf-6nL48D7ZIy2J6T2qpluIEEqBFPB6HzBz3KZOlKtPkZG_x42VFAIitGx--CAeLc9t7G-0fvRDaGs_sNESBXyaSoX8SeF47KQKdVWaY-v-gB6vU0hW021LW0VN0QgdrCBA-7tb4nZVPmRb1JwETJRZtD3DF2ObfXfZ0pdHc6veIuWMcsDlmCecmWo_xUhG_nA-HJ_t4lw7xsM15ZbwoP-InoCbeKZU2F8w4FQuyr0Xb24g5Hd2hPM4mFdWFwFrnLMdRWTWFCTJPeX-OY62fawYZ6nTgh00nnXaZCeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a423WaxV9iMS_ka7A9SjESfZCoV0LFYH8ovV1560eQ7ePsPQgSDO2q4bN-UmcK64OEy-JH-CvJIQgduaMFmAhKWVILLlyciEXWXCjydRh3YI0bBN6QE0zb_f9i4BFeyqsDP1Anetonn6tld_S0-uHWxPiJ7EEyDUN4lRmu8O-QGvRajHj_CUTaWRePPIpq1CNImgjifcJtstKhbmvYkHpga1kyqwjZ1ci6TyBND6mu_cqaJvebxrsgCo0qmJhYTgsptMdI7iF11KRj6LRuEDoI4izl9a7Vuf0StnzIiEmxlwjZo4nXvwm73bOOGXteYjD7XhN1gS1Kqbb15_qYQ8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHrLsKQ28-dHKvWN0jOJxzksWGz_boHoaaLpurDkR68mjACnluOD02neUE8WkslcgfEkMXvIZnDbm_9FibnBO5LsOGH70LkE5jVJ8mSBQ3S-b55G5oAEXDXx-8wgWPy2gTuNSuDpYIUphMlBRmXez1pCp9nH6PghUy-KdXHSJ_B9x-zO3JGgc_ygbNIVq7YDPW0DZ5BISr79sh2wI7ynBIi4UoTwWxYWhQnCtHlVNHwo_IdYMYZfUsSQj7DRYFH8k3p9XMKvp2n6cxTMxbsdPw6kSXBn6m-ZzOnxHql1QhgP6VNR5dQMf2Dy2j872V4QdeXC6mRjtntEIBfWSNnmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7CmWV7KrKxUXGxrSqchqp6TYjYHg-J1xUyMTeiS2A_En1leunBOdbPstk9S3kQiLwgAYH7UZtAR4_i0MZeH_HvdpKoRtccVnxoywOqa-HLdQZ7oTE8c8fRs7a9V6apd1xKVEq_8XgTDWE0kyqCUbWNlT-gSJjgapxfFO6i-GY7pzyBxYOM59SvCVc-sTTivL19nsSXv1ChgkU5MFqWstwcHuWAzV_a4yMVW5Zkk_Cc4Wzg0_88p8uyPTLQjJeHD-JRhM3jpZzbf_jLLq41uaQbx1rqU0ZnjjDB3iGV_ybmDSFqAZ8dgUTMF5bHgk-MMl7BQp7WJTmOGC1TE-S4OaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvIK3h1dqbBCITqk9Hkv0OCnFxwpeW40OqBNLdxj57Xur7nEnKqe7bFQE-SbzKobVt24hnoMtVvkXGLtdIl4DTrLEAi4oIiYNEVjcAp6riwW5wEi_3yzacV0Jby2vd4tI-0IuhpjJGBtE3RLJlFbbKL45fBjQr1h-xAN98TDrHFk04_z_bK7YDXo77o0l2X1zPY0HcPb3n4eEu1gk8uooSPA_faDS7tDKr-JE22DxI0fNfrnD2lAc7Q_zeXpL35zJ9OIAV9EAn1asLlCy6rIzJPCmsp73oqH1o8UEdxRpvl5hFI0QW910X0hfrFspWedBy_Vy0bxyq5CUYfFvgh9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJXRFkxA_zEPn_QuSZil53mTyG5INtIUemeLRP9cELbZRTyYZ4Lrsnkthu-ls46GAUs2Ii9kcsHH5rUxkUFWWq1T9lEvjzAWe5s57CEKd5hDaHl8XpSYNURlecAtS4AbK1P9GGYnSiLDUlGvGc1OSL_ZtzOkwXk1fHTcm-_DDzWBMoWr_u8p6CwwBvFzodOsmlFIFgAdgK-z5F4ca6n_BLf-wW5IpoQ2ina0ex8AJa_R-W4KZ8LTyaTs4N8PGUazRykxjjsDgNIniD6q3_qpFAEvuPhPgHmLnlUWnRY6V_wfdDglp-CNo73kCCNzcAHiRCDLMbNW_Cl8_Npo5z6eP8IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJXRFkxA_zEPn_QuSZil53mTyG5INtIUemeLRP9cELbZRTyYZ4Lrsnkthu-ls46GAUs2Ii9kcsHH5rUxkUFWWq1T9lEvjzAWe5s57CEKd5hDaHl8XpSYNURlecAtS4AbK1P9GGYnSiLDUlGvGc1OSL_ZtzOkwXk1fHTcm-_DDzWBMoWr_u8p6CwwBvFzodOsmlFIFgAdgK-z5F4ca6n_BLf-wW5IpoQ2ina0ex8AJa_R-W4KZ8LTyaTs4N8PGUazRykxjjsDgNIniD6q3_qpFAEvuPhPgHmLnlUWnRY6V_wfdDglp-CNo73kCCNzcAHiRCDLMbNW_Cl8_Npo5z6eP8IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCUgRSBA0pJFspeaJI0W3VggJdCh9p9EBRM6ZCNgWEGoQs3ezaQ5uku4khe_9T0FeCe5kZ8SAJzuze_9OE7ymkob8h6MRuCjkDiaBmk4VcrZI1tLTlYuopVYf0nv8FYmd_pBjjzqKJns7UsUS-ZeoS6UuWnlYAczpqASVTD_yis_BOirgv7iEkUzHNQR2Hk74JXK6WPxEnrXdqR43nx9BjVA8C3buFbisEszjT3AYkvkkxz4Thsw92uf27S-pEB6dtOZ3OlLbpYKEHcb1sDp-AXS6dN-k62PFrN6fjhH_ADqHX8kJU7EiG1dTwbej6XhrxNh3MRWTdufsAtqfZDNeRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCUgRSBA0pJFspeaJI0W3VggJdCh9p9EBRM6ZCNgWEGoQs3ezaQ5uku4khe_9T0FeCe5kZ8SAJzuze_9OE7ymkob8h6MRuCjkDiaBmk4VcrZI1tLTlYuopVYf0nv8FYmd_pBjjzqKJns7UsUS-ZeoS6UuWnlYAczpqASVTD_yis_BOirgv7iEkUzHNQR2Hk74JXK6WPxEnrXdqR43nx9BjVA8C3buFbisEszjT3AYkvkkxz4Thsw92uf27S-pEB6dtOZ3OlLbpYKEHcb1sDp-AXS6dN-k62PFrN6fjhH_ADqHX8kJU7EiG1dTwbej6XhrxNh3MRWTdufsAtqfZDNeRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=cx0tre3ZDXcsdRYBdA5Rn3v8vxNZhxjnspYj5xRfGhN5GiIeC1BBBSijcsio3qaHYwiO3qGwrc9jQRqNkpG8IinhpI3uzLpUUaYR0NbZ_ALTq3iJ3f3Mh9TFU1Gh8GKe8j71gRh6Gy3SUcHZ0el6BRm-k5eVaH4mEpulHAzqOz-VGVcUxmwGY2drYkZHLuaW7n28CwMntgJa8_VblEc3gNUC-tQvQ6W3mGS8msnxCPyW3hhUpLgno9k7TxdeD6wwlNTLmm54Q5nqGEEtHvrRvFWY9dzHB1Eoa432CQIlb7PC-_oonjXgkt7y6BiyTkvJW4zxyut-aBH-meTvSOIscQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=cx0tre3ZDXcsdRYBdA5Rn3v8vxNZhxjnspYj5xRfGhN5GiIeC1BBBSijcsio3qaHYwiO3qGwrc9jQRqNkpG8IinhpI3uzLpUUaYR0NbZ_ALTq3iJ3f3Mh9TFU1Gh8GKe8j71gRh6Gy3SUcHZ0el6BRm-k5eVaH4mEpulHAzqOz-VGVcUxmwGY2drYkZHLuaW7n28CwMntgJa8_VblEc3gNUC-tQvQ6W3mGS8msnxCPyW3hhUpLgno9k7TxdeD6wwlNTLmm54Q5nqGEEtHvrRvFWY9dzHB1Eoa432CQIlb7PC-_oonjXgkt7y6BiyTkvJW4zxyut-aBH-meTvSOIscQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taJx8K_nPQoj9z9nzfMnrbj3LboR5sHV_N2wdo9H-2Hy3-LDN_fYRqAXUiHbRO7GOF7KeWp-SC0RI1mnZGpX9vrqzWivwIwKqHH9J79XNDB00lv0N2abR7H8F9oAC2n2G5Q0Dle8OPNfud9qTVyB8zlK6WlCZ34VbY8Bz8IspCM7LYDMHQ5JGNE5eoc4M4HChGixVWhzUgunwj8uYYvSuKXHm4Enwh6ahcxp3E9mgRAOOSpd8-Y2r6OCd2DlUuuyZohZ4v3hZNvaXmPQvnTZ4vZReHvG21-mGxiMDnYEwyEqT4OK8ZTBRDM1VmGm013n4CYiIG-gt10I5vHfgaYNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv0G-3Mv5iNGQHpz-JqtkvH6u6HcKDGTJfjrXnlzYE5BwUBiQSFKxr_mZDmN6dgwiJlnB5MIcDmXUkgv54wtWMw_Z1OZ3qudv6LYuZ2SYMdFVq3lBQ8O7jHqI9cPEcqpDJxGj2wkOirN5k6Q6ij7dRqiceOezMBufNZjeoXZ9ms9r642gxIQa_1a8RWeORlQvD-1zTsH55j8B91MLYo2YmZODMMNMWgfUdIKdf32fy28UcdOlARqTUczmzuODt2G5tYzZkavfbJphpeQegdEmcQv4VnPHmFePdjfJ3CJJaKHd8HoJwZiOyJDLZPZK1O_i04Z6HA4FXzYfRIiVg-tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=dThNTEgL5hIA5RUH6lpWM9JlHpUyQVVGaWYVroqIUfPvZ9dBLn0McnK0wMj2RmGYSf8bsiDp-0Z3IpiayXhKhwb6kSCZDaYGew7ZBMJm2UG1adx4f08qGK9WhvIDe03jeyrj6OpWt_PR4iHyDefN2x8kvUtbEBAFp-LygQDw20QqdqTwq5ptgPCJI4aOLYxfe7UKrBTEpCRBaPsT_4GTthdMvpjLTX6GnPHv7b1WXSxNcoHUGrDIdtYE8PpweIBT9PBKA8DzktZoz4tJQBhEa-LPz1Xb1jYaxm-xzQyddRUuhg0bGVuxvZjYmX82xF4qaVHzw8CbgQegy3-P0IWGoGdaqvFIwYYAAezWc8xCLfhV1hoSXJ-W3Zg_NB1mtOfqfj2WZQWNIG453Y55zJmAqiiB1UrXFkNIzyEeCkZ5nK1GGtjKkVf1gVWi1NwRy7XC0tMW9a6vFmFTQO8EqBGVpF0VoKi70-6sl42nEIT_mSgsQdk3iFnOJ5y9inH6HJXMby84N5N7mTYpUGoDUeNe4gtmS6QgkAnvQ59ubkcYO_XQKEjqg6wHd4M3JM13Ch2ZUeE_JUF-bTvRGEEY7uECmScpukqqQTkYrtJLEPdwIPb26tQ8QUjKC9_kHZi301iQXng66Yg9FjyG8CdNeZI6DnxNfVMR93nC2Ss7a-yS9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=dThNTEgL5hIA5RUH6lpWM9JlHpUyQVVGaWYVroqIUfPvZ9dBLn0McnK0wMj2RmGYSf8bsiDp-0Z3IpiayXhKhwb6kSCZDaYGew7ZBMJm2UG1adx4f08qGK9WhvIDe03jeyrj6OpWt_PR4iHyDefN2x8kvUtbEBAFp-LygQDw20QqdqTwq5ptgPCJI4aOLYxfe7UKrBTEpCRBaPsT_4GTthdMvpjLTX6GnPHv7b1WXSxNcoHUGrDIdtYE8PpweIBT9PBKA8DzktZoz4tJQBhEa-LPz1Xb1jYaxm-xzQyddRUuhg0bGVuxvZjYmX82xF4qaVHzw8CbgQegy3-P0IWGoGdaqvFIwYYAAezWc8xCLfhV1hoSXJ-W3Zg_NB1mtOfqfj2WZQWNIG453Y55zJmAqiiB1UrXFkNIzyEeCkZ5nK1GGtjKkVf1gVWi1NwRy7XC0tMW9a6vFmFTQO8EqBGVpF0VoKi70-6sl42nEIT_mSgsQdk3iFnOJ5y9inH6HJXMby84N5N7mTYpUGoDUeNe4gtmS6QgkAnvQ59ubkcYO_XQKEjqg6wHd4M3JM13Ch2ZUeE_JUF-bTvRGEEY7uECmScpukqqQTkYrtJLEPdwIPb26tQ8QUjKC9_kHZi301iQXng66Yg9FjyG8CdNeZI6DnxNfVMR93nC2Ss7a-yS9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=g8t7nb7e8VKUf-R2TlJOrAjI0AHW9Kuy7XscMB4v2bCOi_PI3z1LBMADgngogRQMeDd09-m1cKXTEnI9QANlSM_p6C-xuSEOcqJiZQfT8O9QKDJDHE74vpZ-tQJYmZGEwWsF00hzEUTn2W8c4npejmMCIlJisKPIcqw4jTkAYaGLOiDOt2E5GE-iucYf0KccimGIxhQlsEiAQWKdgsI2Kb3I5evX8EvSCWjqdzoNU7x-6A2MuDRiGi5pwjS6txB9ucaRxhVKvrqLXhq8p41stJxlehDXwudIUyKgXocycAzRQf8CYN_M63hmNBGbCSQ_AkuOKWwAP5G4xsHulnZp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=g8t7nb7e8VKUf-R2TlJOrAjI0AHW9Kuy7XscMB4v2bCOi_PI3z1LBMADgngogRQMeDd09-m1cKXTEnI9QANlSM_p6C-xuSEOcqJiZQfT8O9QKDJDHE74vpZ-tQJYmZGEwWsF00hzEUTn2W8c4npejmMCIlJisKPIcqw4jTkAYaGLOiDOt2E5GE-iucYf0KccimGIxhQlsEiAQWKdgsI2Kb3I5evX8EvSCWjqdzoNU7x-6A2MuDRiGi5pwjS6txB9ucaRxhVKvrqLXhq8p41stJxlehDXwudIUyKgXocycAzRQf8CYN_M63hmNBGbCSQ_AkuOKWwAP5G4xsHulnZp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0mLEATWnpCHWPi-wKXoC2yc28EcVY4csMbQ5bPgIF2nogxoYfUqQWIQQNvaXztfVVx9HEzo1ICxMifWQQuogoFxrWeTXf69u_NQwXcXYhNXIgEYqlWaSg3_dFRcN-M5oKVVfy3tdtuMTAR_1AMzz8WHIm3ROVBQIVS9-4Y6INMJC8-z0W9U-Vii00tsUaYrLRTK4V-GKUTHngKVPb25ke5HpOMSR9VVpFWr6-v9EVnt0W2AmmBqCRnEEBen1JpgjNCKMh86RgIAK29Ez4XC4DPfOoAMpyUgzwzWQXF_zlSoJ71_e0ONLTW8xhVzZ6jb02ZOjDxgZRD_Wa57iG3TNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QokRTYr6FfX-A_JxBwXbFyMW5e7VtTKQfU53FSp9dqgDzoRAGaxeupWP1JxCsmX20QrMDqq3TQdNID4JZRJgyj6zGcvM-rEM1qzxfvVtaeJg3TIQQNjse7uG7t_a1_L5p9tmd3Kc_gkx1Ssr6-qmbmwvYKqwYC4W-EmgTFIPgrQhcOKkWCqTo8lXuTj1LhXDf79fKTswLrumesjaEiGLJTh-ClpkYMlb54R8s9dkdMpblAFuFNZ-w-m7nj-dQf_OwChLyfA_oDBRQYgjH82bQr4MZgifIP-RWegmM81iEKp-7_CZVBLJ0mDp7RD6_dHIEO4C9uuoXH60fk4fdOWUYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=j6fRCP6FY9nFnw6Jzgv-AqyWBNBd4Hny8SGf94jISRxVmejdwxqzSF8S7i5HeGJLWlrhfM0ljLix4LdZJseeLaWzD9yXUzD_G5HiDEn5MNSaD6D0YkeSEuQDMksjLG7CzAxnToUJ72xQvxXFvxTIcB67Pf0PrP4kguxr2A7sITiFnyQhmI4H51KL9BKuaakkg3-rsdjQ588XtWYdQckY0_2Fi_vGJohrr_vDoIIlBlgW64mbzV5QxYCNTsKZmi5_VZSUAITnldLM0Qk9NEsOdTYDOTwFwVPRLdO6mmMtZxN5wd54_po1ehHg_Vu3Im0TLE_Du7L09LeOdcC_gD-7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=j6fRCP6FY9nFnw6Jzgv-AqyWBNBd4Hny8SGf94jISRxVmejdwxqzSF8S7i5HeGJLWlrhfM0ljLix4LdZJseeLaWzD9yXUzD_G5HiDEn5MNSaD6D0YkeSEuQDMksjLG7CzAxnToUJ72xQvxXFvxTIcB67Pf0PrP4kguxr2A7sITiFnyQhmI4H51KL9BKuaakkg3-rsdjQ588XtWYdQckY0_2Fi_vGJohrr_vDoIIlBlgW64mbzV5QxYCNTsKZmi5_VZSUAITnldLM0Qk9NEsOdTYDOTwFwVPRLdO6mmMtZxN5wd54_po1ehHg_Vu3Im0TLE_Du7L09LeOdcC_gD-7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=dFoCVb8fn3TpFFxungfVM_ThbIOYqz8WyaS-NGoxXUs7XlfHhEfzKnRBKLwcyy2WzUJCN5QVg657F6OWlY-L6HOA5xyPtnQSEbKDi4UMbkbIN05fUlB15Kx1jh4ndVvoEdk88yEha2qIBzB67DPEeqptd2sdKbnMRqZmnlXJAUr0wObuMlL_QR2d35SfGXyrgfjEpTKE7W-XkrsPfCFdgn7BIForOz2QfGQlg7YCTb74ECWvPASuzqKWE8af2iV_XnnjuF2mVp6DsWT9bl9wVAOnKuSRxbMnr8YnQmO7zQIi0LkHxRze0FLNa9BVJ1TECOt1bhl-t85yu3S4QUHiWzzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=dFoCVb8fn3TpFFxungfVM_ThbIOYqz8WyaS-NGoxXUs7XlfHhEfzKnRBKLwcyy2WzUJCN5QVg657F6OWlY-L6HOA5xyPtnQSEbKDi4UMbkbIN05fUlB15Kx1jh4ndVvoEdk88yEha2qIBzB67DPEeqptd2sdKbnMRqZmnlXJAUr0wObuMlL_QR2d35SfGXyrgfjEpTKE7W-XkrsPfCFdgn7BIForOz2QfGQlg7YCTb74ECWvPASuzqKWE8af2iV_XnnjuF2mVp6DsWT9bl9wVAOnKuSRxbMnr8YnQmO7zQIi0LkHxRze0FLNa9BVJ1TECOt1bhl-t85yu3S4QUHiWzzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeXKs55d9drruDh_5yJU8uIszsElhjaW4klrnVPeXEfyiZ_dn8OO-10YzdgdrWSnrGNyJI26DthvikcqIbR81VqAsQkcWTkL92oY2CNYM4NmqeyuXHOL6dWp--fklN2oDDE-R1ByUMhNmrlC9fywEMFdIr-oyVxjLqYfal19j3tHVZO9yJApZ0S5E5yJ1oILs7ssjCnrjHoSC2hurN3FkPhNqMEB13ezmUKhp_77N3UV7PvYFS6pcEQ-Hg7AMSIOJaRs_wluHUPZZAmnufMTC0x0XaJGccey5qCTaLoL1tztMRXpW_HyoZGP-DmAkL8NqDEpfZ1errin0aSY8I8HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPaqX3kvK4aoByyH4vJqeGX-qfcEd9sns01IPqaT9rseexcHRSJlK8tQ6R2TkWOfxz0qjBQqL_82CK0VRmkWe6gHSQIctqdZ9nRxqstl8oXZq3_aZXG5BYhLZBBSSz6EoS7t0q2P13LcNMyMNsaB2PgZTxzJZuOqff9qvnVadcHmDke1AEunuZ_pmoECXp9r2uNz_ZlH5PvHVluml1G-vswIjY0n7wHKdCp8NEiGov0fUt-aQcz2wxl2fLgXRhgIgZo-K6o2qNvDlgLKo9sk-n0SkJCeRrpgBf_ZdhilMLxR6uSuK1DIKZPsYQbFGNXTTORfHpoVzFA-p4q2HlxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=St_s21qRjKM_J7Dk7riFXjIOIETooJofuDSQmnapJ8fUMvPpEXeGv7wSp6eG1n9mnkMpKQQ_J_EBdLyrYLAE2-Z-6ee1XUjqkoYaFMIiarYQG18QtbhabphxjPHvUhFKcCur8Tr3uu6ydgPWKjo4v6lWh-mMPL_S7TPwxam3aIFb0dinCWD7eeQDBn5P2UVBwmOx5tlQAi1jw517DbT27cFo96UX4kSQTamgZkszJiidJ4c00H7L_vwK7hXb_jEdEDxFOOY1AwvjbtgEeywXfrIJV-GTNLS1bV4LJlJIYQQFoSHXvyYSBRdKLjuZE5RCUF9I70rgTSoiuC71aPj4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=St_s21qRjKM_J7Dk7riFXjIOIETooJofuDSQmnapJ8fUMvPpEXeGv7wSp6eG1n9mnkMpKQQ_J_EBdLyrYLAE2-Z-6ee1XUjqkoYaFMIiarYQG18QtbhabphxjPHvUhFKcCur8Tr3uu6ydgPWKjo4v6lWh-mMPL_S7TPwxam3aIFb0dinCWD7eeQDBn5P2UVBwmOx5tlQAi1jw517DbT27cFo96UX4kSQTamgZkszJiidJ4c00H7L_vwK7hXb_jEdEDxFOOY1AwvjbtgEeywXfrIJV-GTNLS1bV4LJlJIYQQFoSHXvyYSBRdKLjuZE5RCUF9I70rgTSoiuC71aPj4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Rd1jxR0kqaXETCxgn-yRMcYuZ_qCAkcjByjnm6hmr9Z5c3uT1ueyHm-zx1CaqkosOi3P6LJlrb6A0xC5KYqNa5JbXlFwCbI0z1BeOFqAi_n2knhqtOGzr-ZKYkuAZTfx1M5PeLCmM_YYNdfGgYFKhbRS7SJUf2WzZI1Hb5MjDcxKscQ8z2kNIk-mMgcDI6gnl8CbRF3WnguiO76llJPXnVk1Lij6hPfvPi5937-xy5xb3LmiNsT5aOK-G60mMtms4rTWGcC8EnIgjLXHoUAiKTjv4xbK0kAw8qnWRb_0e50u2OtFtxdXcllCAicwI6r1myDBDbQqlEZYiIPi78lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd2AmUSdV-eZmUWMea4Mr-uynTRUAlbP6FrhEogztaKc2WC9tOzhS7DYXSqoSmWClrsxSHtD0McS0LkW5a1dThx1y9roO7ZH77itxazZITz-WqUIbF1hL62vGEsuU8Wj5lf6XX8mjBHHbFAIpwiidmmPOz2GF6IPUuNOUUFt8V1EpCkreAlxXyQMtYiVcze6qem8VthrJf8eEuaF0abyTLZaot_LepvAQcczW6mjeBNjK9fpL_X2PNhxBfK542m0ogx-8V_Zf3EeUVcpdLtbIL6Da4kWocFoDNiG1t7a3tx2HMSJ8wS_wxm1P0msk1cow8iYxUw-OdgQ4Zh_PXiX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftjTdAYKyy60YkzN9LvrZO6mbOuOrpNGDfks8b12FrOAjt_UXOyRIVYVmr-GuruMqmOhQeu0dhuGy13Zw19nqHvjyGUimm3WBDj61e-W5fX4ByDLgK2n_BwCybuw4vQxQ-dbhBYB-Eairab9-LFdTV7auEmmqYnR1XMWxJPmgoddCtQvgP5ZGuO1sFIA6Y-Yh_raj-c3lusXa2peasaqU08gVi2-rdZ266f7lCvMCCjwOmhY9yxebE55sLDTfSUmEZGutg-vOavv2dOaJpgU2bDBZpsKOutq5lJZBx_0kqS9VFoFYwBKGH7ChmURm0o1ZOhse-G30_m9X3cU5BbYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5axcYN0AUD15Z1meaMkCFblgpsqI1ju7vURFB-JVRz85mEEP-PQWZTOIp7Srzng2fou1gvEl3Bi-IKrOwG5cQQ70vD8_SAaCLznRX4N4KMfqbLbOElQNvjGcdKZjk622_bgsEaju9wSw-AJrv9x--P0WjszEKL8sTrQuaeWwb1yiP-f6WwyNYind2Satv3Zlk71dQHHY7mL2jNzst8cO6X8DahD7dCQCMRdHUEeFwXBchEa47oV9k7ywwXpStk7v7hGt1vRSoue349UoZRcHt9Oui3RFy4zW0DtrVIqSvGRd8E9aiIO65iDYe35rU6-URS_eCOcoLENOKo54XJL17I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5axcYN0AUD15Z1meaMkCFblgpsqI1ju7vURFB-JVRz85mEEP-PQWZTOIp7Srzng2fou1gvEl3Bi-IKrOwG5cQQ70vD8_SAaCLznRX4N4KMfqbLbOElQNvjGcdKZjk622_bgsEaju9wSw-AJrv9x--P0WjszEKL8sTrQuaeWwb1yiP-f6WwyNYind2Satv3Zlk71dQHHY7mL2jNzst8cO6X8DahD7dCQCMRdHUEeFwXBchEa47oV9k7ywwXpStk7v7hGt1vRSoue349UoZRcHt9Oui3RFy4zW0DtrVIqSvGRd8E9aiIO65iDYe35rU6-URS_eCOcoLENOKo54XJL17I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLWvn8PPS0y3g7-Qoama54QmPRVz1G1dxhWEyBfSMyQYOKo5ny9KUatWdXU_se_gJk5ZOcc8PPf7WyGx4VNJwy0r_pBf3twxe927H_IV7bXuL76s6TZZ5Xgc5cbW5IaMV-_A02SE4_M44oEudK_Rxiszb3O4AzHhvzih9ecRWOwueTZzN9Wzu5YSieDLmX9Sf30cFj7SUfnRCJdYcfyRuFWlZ_9GXU8kH6GXaQpe3MbT3YTg-fZSFTwEJO7NCmCkn5hDEPXUn6CWFgViSDucuaZloRcmNTiE1lvc1UGQEGJRBMKLyOD3S0GjwPfiD2bI4yLY1gswYsECpGugpaU1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B93eZry6bbTZacdnR92Kz0UEopRuxzZeQGiyPeFQR2dagqrXo86jixMU49rJuQ-2n505uS52SkMpUDvB7djpROIb-4BPqlLhOlZIgmeWKQHpGC1zsSp2KLl1OsRFFI8GSZ3zGoznMXS1R80Vflw1kbo6ncMAdAeN8S3d5j__QGA4pmZEdU7Q6ShrtVgsFEt6vI8RuSKkeQGU5S2UEKLLCfC9SeGBZ7dbcXBR4VeXvcrwY6ntUwk84QNu8UX05YUjVbliHXsh_nClY6OJ9vEzwv51yL1IQhc--m6X7oqVv4LfWHEBy6UTVaHmLR4s2KpJRLzXGfF4I9y2TViBIxCqWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=DwWuruSzo1zobmW-GkyumnAdj7qzS8-PMTk691bQB0bEzrJVYLvhfNZKfsIji9OJ0GTE6h21Oq919mESBf7QC9PvWs9riK7GoaAUgfXk5ZQfH7D7jAgSHUSyVHRyqT4PVKiQBzl57uCQLwzpFbfDBVo6zF6OXX4m_I5MIO6Zry9Hly4_uaQH4TITzUXc7jUFCtLLX_uWdyrXoXjN-PBeYhWiLvB7z06rANTlUbvz8PYasmnVFyqRAyfCnaN9HZmxgWK_G2WP1zmqu-WWwtVj4iMAUblrlXWTyB2lCjHy6dEmC9FC6c4_I6s27glC9JMwcQWoxVLiFHDLiGIAW3gsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=DwWuruSzo1zobmW-GkyumnAdj7qzS8-PMTk691bQB0bEzrJVYLvhfNZKfsIji9OJ0GTE6h21Oq919mESBf7QC9PvWs9riK7GoaAUgfXk5ZQfH7D7jAgSHUSyVHRyqT4PVKiQBzl57uCQLwzpFbfDBVo6zF6OXX4m_I5MIO6Zry9Hly4_uaQH4TITzUXc7jUFCtLLX_uWdyrXoXjN-PBeYhWiLvB7z06rANTlUbvz8PYasmnVFyqRAyfCnaN9HZmxgWK_G2WP1zmqu-WWwtVj4iMAUblrlXWTyB2lCjHy6dEmC9FC6c4_I6s27glC9JMwcQWoxVLiFHDLiGIAW3gsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CH480-ZJMNVMTNF_2y-jH6PiKNyHPMMGnqLCvPJehOjUI1FQ5yl9IoSGv_NctrP3I2DKqyh68uBeDZ8g3RWjj6jUmzihkTDKmnAp9bTQAKoAlFfJR1s8HI02hzgPZL0jmPiHIMWMsi-c2-GBgy7xQE6dRggechsRaKa4n2DkwxSZlTqJS8d-kWo1rEsRnmu-XPIlM1jd1fmBUN32ZHcedViOjd6qaGWsHNYXOLnHBZyduclWaBg5gvrEXTWOSs-gURPn-cw_EOwOq2F17GYPQY80hD9ThkFuDAogyoaz_tFmNJjKFyefVoqanCT8fcqtzL-ErANrxZuhadbCEBt9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CH480-ZJMNVMTNF_2y-jH6PiKNyHPMMGnqLCvPJehOjUI1FQ5yl9IoSGv_NctrP3I2DKqyh68uBeDZ8g3RWjj6jUmzihkTDKmnAp9bTQAKoAlFfJR1s8HI02hzgPZL0jmPiHIMWMsi-c2-GBgy7xQE6dRggechsRaKa4n2DkwxSZlTqJS8d-kWo1rEsRnmu-XPIlM1jd1fmBUN32ZHcedViOjd6qaGWsHNYXOLnHBZyduclWaBg5gvrEXTWOSs-gURPn-cw_EOwOq2F17GYPQY80hD9ThkFuDAogyoaz_tFmNJjKFyefVoqanCT8fcqtzL-ErANrxZuhadbCEBt9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1UsDlGEudwMKN0oM1T6QiMvB3ndo6jToGtAfIJH6ry2Ro0_NwVk_z4RsvyCwKKGl6i6TwaGmNOhGcya_EyL0PuxGCcH4vnUrEJO0knvAbs6IifVKobOSzXQ6WJxZfRxI45P0Ll_vuJttUHG8nBWOS4fE2oWQnoIA7XzBk2bzPMzeErQ7TeILvR2TJQVTa-fQk8PcYAQKYZJ7uhL9ZTeoBSlGuDdxS6fbliqwqAVfo3YcHYts6HDKk7ehh459V2tUqDcTqlCI8zXg8mGnTD5f_abWwIbYf0oGnFkzBD1ThrH9RdzNYW9r8ABDpGXoeA7n6sJbpQYLDw6I0CJBnpDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9xmAjNpsmVz9kSU7eWuvzSICioWO-XdOZYPOKl_nukIedB_lSl5PsjAFGgT86-xqnUp4m_fSu54cfxGQHy7JxjG3_XLtT2uyBybPrBg6WE95fX31mGQnn7PPHCtPT_a5Relu-s2qxWA0rD76oxg5RYdtocCAqNIWkWUy94fgbmzpqLaiACqcmVuMD3PAHSeUvjWOfJ1FvMpAtL-zqnDA9jAMrkdM93hv5uICXc9GIdz84u0zrUM0K9D_WSVDWCO0wNST8l5mG-s10lVCi4mxvZW3Cw2gJOdMWRW7A9OY43fGuxcOaFMnnLZ0mYyvdJhA0LrtuR5OQVuCF6boKiQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=XeeYRbgDedQEqgn_T8Uq8zn64EOiX6PJI4SFBB2bHN2AtOcu4tXdIVJSv8dd0dgLsABk7N8Ds2_57Or_ZBm5sPrdOoJSX-qmRzblqUf1XOGZ1FSJhlAVs2JdLfiORFAR2LKlerHOVlUxdSQTR1-5swXXpsKpYyMvu0F3RdsIqh3BiT-wIdAzxzdn6q1P0Gfw54qn97GWtSObdtZ2ZtcUKuBe7O29XiuLntuL3-RAliwCilJ2j5uWINQ2DInJTiizA4NUM0mrW4N2k1shggMKViwc6x3QguLUzakV6H0M-msMniQU7jK6N7fD2uUoHHUzeS4ijHbneK7aliAtPF83yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=XeeYRbgDedQEqgn_T8Uq8zn64EOiX6PJI4SFBB2bHN2AtOcu4tXdIVJSv8dd0dgLsABk7N8Ds2_57Or_ZBm5sPrdOoJSX-qmRzblqUf1XOGZ1FSJhlAVs2JdLfiORFAR2LKlerHOVlUxdSQTR1-5swXXpsKpYyMvu0F3RdsIqh3BiT-wIdAzxzdn6q1P0Gfw54qn97GWtSObdtZ2ZtcUKuBe7O29XiuLntuL3-RAliwCilJ2j5uWINQ2DInJTiizA4NUM0mrW4N2k1shggMKViwc6x3QguLUzakV6H0M-msMniQU7jK6N7fD2uUoHHUzeS4ijHbneK7aliAtPF83yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CAPUmw8SPcK8hsn3eFMXkE-aAuw3AHMyn5r7y8uvQpnRc8I64qbZt-HG1W5NZ4ULE3hioWEdLc3_t-DIlWcdn7DnF-4UUs_PaDrrSHd7FZnnP4LpQb1pwoGxeKNn6udGmTbR-Rm0-cC8jI9ww7a55PgSYFpa_4Ed5TWqXBQUmlzHhlNFCZeh9C27fV8zVIxiS4nAh5eJJb6_57NhzYBOP1mtGA5Xulyva-3U68lKspN9XXqFksGjH_GN02KFdAu6jisMcdC1JbBBfrgkdK-HqI5kq-gd0Mi_Llm4BWHlB26l0t8WOrrvZQP7gBVSkaAuiaYp4UJWsL48fpvZtEhCJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CAPUmw8SPcK8hsn3eFMXkE-aAuw3AHMyn5r7y8uvQpnRc8I64qbZt-HG1W5NZ4ULE3hioWEdLc3_t-DIlWcdn7DnF-4UUs_PaDrrSHd7FZnnP4LpQb1pwoGxeKNn6udGmTbR-Rm0-cC8jI9ww7a55PgSYFpa_4Ed5TWqXBQUmlzHhlNFCZeh9C27fV8zVIxiS4nAh5eJJb6_57NhzYBOP1mtGA5Xulyva-3U68lKspN9XXqFksGjH_GN02KFdAu6jisMcdC1JbBBfrgkdK-HqI5kq-gd0Mi_Llm4BWHlB26l0t8WOrrvZQP7gBVSkaAuiaYp4UJWsL48fpvZtEhCJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8fJzWMvrlA4qJUed-1fbWVatjYUMql2jbx7YqsqSXleLrLnvGdGcIfpNiJKlfUQ2weK70I2oCnh7ZxpQGObXYbbW4gh7Qj7AwmQGLcdIQxOUk9TRh_GF8Uf5ns364dnnefMvVH6_BVeZbK9v_tV8vWMEVXka9uV04H7XsMq6HuYSz92-g8CZxhmaavkaFtVXe5LClgceUFaMnMSxHgo0-yyz8Ilqc1LoUN-b8mAFrlSIW2smvT18VcJHKPb4VGPVer7LY0WN-ZZsOsqRypoiBeNw_9ZtXtvAabjAt7mT_U9ebXA1uSve123PmOkcBDYDccf2Au_hBjB2OLf2aXTHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWsz7BrlVuQUYbhtfT5wF2s8lOU-MndLwueq2idgdLy_lWc4vpp36f_WuyNtUA7MixluzuXEhput-wHtGcFpbq9RZ1gcMkQ3oisCdNSetGCpWgG5PpEtT9s_bFA0-hXOJigNJRjd154D_-hE3wiumiHCDBAuhE8i6UvhoYgVimRoBIZAMJQrKh-6AOfIU2ZqUiXML7xiFlp9UvJ5AbOLwExLP4JKqMvOTOWjFvnT8kiK-rFiWC0XY6ASIWx52f6PVIahHGobByKs_n1S7CxIjvYdoIB678-ikG0EKEQHWKNem6NNahqYvHdFloe1ExikOigBgd6v4_1wfNRxlpq45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-v13P3xCq5CppQiTGI9FIRxT79RAJKBxZaNxjUvP9gcdSJxOC42YWMewqILZuw7o_TXOcxmRQQDJgzFzkw2nxB_MH-HoItTApgWS2LDUk32O0mdYYymv2xwh8bHlE3bMq3aYLiRQz4Ed_U341cO9PGIbDUrA1YNsn7HQXpXLiCL98UjrR7L7EeR-TA_gaLA7eIFRda1uKUqFRp_eMTgPccroX4T2vKB8RN7rKDVMNTqmqdiDcR4-jOHMkfotg12olzG37JS_B7_yHAgq93ealxQlvcY_sG752xodSryyNKqBFS3Fgwts4MMY8_x_b5uSX-z8yA2m1SRNwpa8UAN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFjudINAxI_K6z1BNRmL8q1_V2Nrcj0aIvyx1jSWvzK28qawVURSgOLEgrdoH0EZTQWSuR183lfZrZXxzQoDUQ5b5gkdmo_N4_hV7sJZureND7J2hs0ageXkeCVAtMgqfB0cBOXmkypnrrYdMb7XzlEuB9Z5up3xVxxe04FD2ObkqpYV9lT1bitqSaOgxrqX6wh6QL-LgihZUMx3FlN1ta4ruVc3OzhSK--4TMAcdkxTsm40J00rc3G9Cgz_zPfSw7vcvxrkq4wB0XsHnTHU7NnQ-h8IlMhsW5ilSx5ERMNXNoulxwT-r3KDyUYxirE_wQko6YtkYRxkVpFrZUlxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBb8P2kE68-x38SOHO5P8JR7XtONZ7ju3_8F4k6PfDLF_LvK4hwrT9Xh4LQBitRz5xXKp1SnQc3ZhvbaYupSbZ8YVJ1cvgnElAjWR1f3QH9aSiGIuEijKprX3fu4-hsO8drTfmvI9IakVd7qHaHFMb4tycZkFEtQPni1AObOubl0vy5onwa3fJghWfygg50_xs92Gxq3VBBkQVEzNDF52VroPwJJEUZrm6vb8Sz_F-r062sIvuynxKt0Ac7uLtveKxEAGQaOUnx4GjiRKJ2tYvjEJJkPLOC4P3Qfz0v05DJmE40ZZl99Kx9dQBAfLyLPIvGi3Vh1yWUONHeJIdxfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doF4vWpzWG-NPXoAsq9ht639TXsBp0icpupqPoT17uPo6l87WYiHWHDPJESRU4OvzuMvahz07VVSW6ipJ9qh6SE4O0zNWI-9FuAClpxIyj4twPDldmV94jtuf5w6U8_VWBeWi_YTa4PFRJqPEuBwbsAz9UxzYRdIdraZnioJn8VtXfVL-XipT98HKFRDIgFksBM3NlAZVBaC9zVlX4N_AuBSW2ov1wUGCo_MHwY7svZuzggNtZ5nyZCNuVliqIxf8HDlmPEW8hirKlSp0oIXyY1r3De5Ki_-Ot_Yz-QC2QRKtKk8FPiLPG6ryieA7GFLVFRF4JvC7oPx-oxWBcaRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpSOQzMU3DGeq5gD1_CFxdbmEeQzXj3J-Gu7KsMbYdyY1FoSpxsLViDF82XSdgYf-YtiKaa38yqZwBmL-cMh3cOMvuwcRhNU19R9kvZgjrjRNXf2ZQXPISTrNjwU0oZi2i_iukMGTNgDPeUcvagTKLhZ83mygAmVGd335e6kwS7aumwLfdVYqlR8gEZAwmyL7fRTQvPuQaNQqbrBo0QZfmwIsC1r2N3wIi5WRsGzKU-RceFzhy52s-vYu8Bhv17F6fxFl3BbYp1cmhbcOEWNCgMpnPnoZQeQ6SHQbTxhmI_tkqP_YnOxu6D6vb9Xa-8V8wzul0rvhlb5VAc11oklbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwPnOrWauSVTLSFxUp8vxdTvtmcwOiAMONPtJ1lfjs4Nol4nTkroA1jACq0n7wKL__Z5r73DrrGybMbYiMYwyp4gH9ocDxu3D3KCmWXAQmVSkORabrOd2GSe8a-ZwbdFxJU74WDNtLdBwypCJkC6sXkG9uPZIeaq3Z2ijaYO_F3pOFuMXuhyDZYM36NXOYNFbLkPN3h6KH-S_22zzdKno4bgcxjNAWSesRYeeisqSVRm4_dqnHME0Kw4lxAwtow1chYniDzcox4ikDWJmBfq6ayufdWNIuvvLoZumsNtO9iMot1YslgOyrVWdEDGj4aACbuBCi7r4bJwd4pvG7ddxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSAlOgdNwMLErdNLzd7M0NTFXmhR3ym4LDir4Ypm8z6oUk1YFWcWNJQXO1TkcQSlkXrO_UtkbZqFhi7n1QwWVHgiLcnCf6eAoxvWF7JejZ2uqWpKIwz9ilgwe6cfKiZumdd0wj2clCwe7vygYrSP8uXKOcbF5P6g-prtoxRHJWkzw7U2fGDI51b94M02i8Rc7TahCgrQTXK3pldpZ1aOrmOBsAQZoMQdlnRSAaVyCyZeaZm-u9SAObwznimhodSIHVeIXvSGtY1BQ6mIjsQKpX4GYIu2b0VYRpV-lABb4XEzJvNltRQuPiOwxD_AwRW5JKTvYcCDIGi6XTvlZU7gnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo5RMi2wfCGuCzltBT9pWNV_1rZ-5kmVmnCuiZQ7DsBVvS8VbAhpLPWzV9htCleS74czUhlx1wzY7zsb5pRpb0viHON-B0rvrRqMYiN_JoqKkRahb4OYGBaE-xroicYzK5xQ-myJisSt-TQZwbrMAq1gV1Ost3bDdYH7y0Ne3MpXy5AbYQ-6tJxQJQADcKshC-EZOaRRDAExYXx2vkuULqlLttSefj3NK9geyS-t7PQN2_NNJw2u1uMS4Kcaj0BzVEp_lh2qHjtS-FhjjXDBiV6n9TJOf5ew1mxSgVpZ2Eh3SmQjnMRL0-rJcYFOO4sUFgeHanZrbj1k7gOG1zjlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=iE2VXdSu6Zjg8qOki9z_-bG9f-yaB8Nvlv-gLqtH_ht1S_qQRY4SA1dArcNRWFvhkbae7C1CA49yrCWXRbTll8e5CZWhwxZzyV3ehCKu52UkfQbpAxmNBT6bXrLpUQ1k94FB4NZRoG2hV6oYb74OBmwvte2u6cs6IzP54HcqQVohUfJE9GAyhne8QkkBypeVQ_XcuVRhVp9PvRpavAE1URRZzblxVMkIVb6KSYzzLX5dij4wZXeArmHWSL4ZUADZ5LkKowyd1Alx8f9XnLj4JXiiH4k1ZytNaIlUNhbIAJvf2idY-QEu1ZXmVUk6Lc0joEWAVOkX8TTkedowmyyqQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=iE2VXdSu6Zjg8qOki9z_-bG9f-yaB8Nvlv-gLqtH_ht1S_qQRY4SA1dArcNRWFvhkbae7C1CA49yrCWXRbTll8e5CZWhwxZzyV3ehCKu52UkfQbpAxmNBT6bXrLpUQ1k94FB4NZRoG2hV6oYb74OBmwvte2u6cs6IzP54HcqQVohUfJE9GAyhne8QkkBypeVQ_XcuVRhVp9PvRpavAE1URRZzblxVMkIVb6KSYzzLX5dij4wZXeArmHWSL4ZUADZ5LkKowyd1Alx8f9XnLj4JXiiH4k1ZytNaIlUNhbIAJvf2idY-QEu1ZXmVUk6Lc0joEWAVOkX8TTkedowmyyqQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=tP_aUDk9Ok7X4wvij9j77en_1oButtKiRFkz0R1kPRo3tX4Stl3Em7CBztgmOzbVinw4Zq6qSxmN1r37MHdwKYxLeZtsnGTDYkKXhPp9NVJamH3BkzrOCckIKpfQht5UpypjTI_h6jlnG0QpGxtpO7yWKFtJSdhReRJdZLIBrFFz-tf7GaEGwgeACQdHg6iznKWFrs83wcNNEFZ0uiAGkzWY9uuh2JEoZFcSbRqIY94XampINT5veC8-ru0jORNN-rqFd2h_algMRm6QTwENduoFe5FgwKVtN-cWCOPhlLUnGsvP8PoBmCkOitW2T57TRoVBoAXtt9eCwXIIxT6ZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=tP_aUDk9Ok7X4wvij9j77en_1oButtKiRFkz0R1kPRo3tX4Stl3Em7CBztgmOzbVinw4Zq6qSxmN1r37MHdwKYxLeZtsnGTDYkKXhPp9NVJamH3BkzrOCckIKpfQht5UpypjTI_h6jlnG0QpGxtpO7yWKFtJSdhReRJdZLIBrFFz-tf7GaEGwgeACQdHg6iznKWFrs83wcNNEFZ0uiAGkzWY9uuh2JEoZFcSbRqIY94XampINT5veC8-ru0jORNN-rqFd2h_algMRm6QTwENduoFe5FgwKVtN-cWCOPhlLUnGsvP8PoBmCkOitW2T57TRoVBoAXtt9eCwXIIxT6ZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=TjXPko3k6Icoe0_fuhSK-Sl_TAB53-IuuGki0nA26e25OH0LGmK5GRCxKfPTWV0nKtFeQEqWZqLudNoAdmVYi6xhcodgJGrzhsJ07Z35smOkvQ5k-jgcnhENzdvV4pGg6NnxpoTj30ZOrHDF2f8WdKpAsip4_zM4EiyqNoWYZga-0OGIC-_0nrKmDSp8II4tsFcorMWff29Vgu2Gc0Dpud28IdqOtY5_drLhTsbmoT5Clhp1Fd-xX-H_GyozDJ-2dV4V9HMCMNn6K-msq8f-KgXgyL9vF50YkJ4A6TXsLxkmQMjg1ioxpu1R-C-IuU3wtcoyOcpMfgSw5hRbUiPv_K0SoyLqdhrXmnlQ5ejc8rpjNRGHu1iyjpCQjGh8UQkUrcdzFPDyw5aZNiVVXBXDX2y17mWBOuUWRgDHSOwZeBZnPtIUdqXgt0vPus85vv2__E11puFc45AHlEGZEU46MdPvSbPuQnggfJYvaJReMKI-Lz-1pyU_tt1BrNxpkINvUwaZPZjsvFpfP7UixMbq3qN3vzezLtvkb514VTbGJp3hYGsKQpjKPy5RB_cULm0QU3W3o8YYVi5gIqRMLKmU87ksgx2SVRCS7zyiyyllde1a8l7GPsqzhEVwmkHcFHZAcWqlSohAIaVLhewdigdAHecE5L-5EwUQ9IIx3myyYxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=TjXPko3k6Icoe0_fuhSK-Sl_TAB53-IuuGki0nA26e25OH0LGmK5GRCxKfPTWV0nKtFeQEqWZqLudNoAdmVYi6xhcodgJGrzhsJ07Z35smOkvQ5k-jgcnhENzdvV4pGg6NnxpoTj30ZOrHDF2f8WdKpAsip4_zM4EiyqNoWYZga-0OGIC-_0nrKmDSp8II4tsFcorMWff29Vgu2Gc0Dpud28IdqOtY5_drLhTsbmoT5Clhp1Fd-xX-H_GyozDJ-2dV4V9HMCMNn6K-msq8f-KgXgyL9vF50YkJ4A6TXsLxkmQMjg1ioxpu1R-C-IuU3wtcoyOcpMfgSw5hRbUiPv_K0SoyLqdhrXmnlQ5ejc8rpjNRGHu1iyjpCQjGh8UQkUrcdzFPDyw5aZNiVVXBXDX2y17mWBOuUWRgDHSOwZeBZnPtIUdqXgt0vPus85vv2__E11puFc45AHlEGZEU46MdPvSbPuQnggfJYvaJReMKI-Lz-1pyU_tt1BrNxpkINvUwaZPZjsvFpfP7UixMbq3qN3vzezLtvkb514VTbGJp3hYGsKQpjKPy5RB_cULm0QU3W3o8YYVi5gIqRMLKmU87ksgx2SVRCS7zyiyyllde1a8l7GPsqzhEVwmkHcFHZAcWqlSohAIaVLhewdigdAHecE5L-5EwUQ9IIx3myyYxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPFhyikKES_gvATWSfwopvS-Zfc7F7c1tlOZdkYtpz_Vzn4Yn_6xlLx4JhLd0fzfO1DBZkBq8C2Ur9_rprm3ybPTQqgH09GBUq6CgWvdOPPYbCypgsSqqvyjiv9appHy2LLnbRMxsTacgTn-zDuxCBl5mWsdExf9d84sXkXKwWcZ3WPzS8WFUAZy3S6zHCRcQnQNIHYKlquTndPvhORSOZD0ARY39jmaKQwn31auTumLNgEbIpVRSRTsEBM3YlCaEjc0M8aXnxMU7zKNoCBXi8h-LNBykZWeUH_9tw_Y5rXz8EQqqPz3J0J1Fi76Je8as8--4QKLxfcnPk1jvJ7itQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bHu9LuUqX4cJQCLPAvd4hj_fdd4cx59X89Q3TrH9wunqT5Jdi6KUCe3bHiYfmVty9arpaRdv-7XoIPliMTvBCc7YAZeGX45c3_shGvhr8FxxgGjHo6dOi8PiJJUOPfNfZqvg_Aj4mh-wwPTXFGXgrHlMKhywoBAWVfV3nsdb2DjPcuhCn0HynZyExq8XOw4D6vjS1s07hMrsQlfvQd5pwDk34t9M1yJJDA1C6B8koyGl-8QSPUVuuw-PkfXH7PF5bhJGkEODlcgE34yEIoJ0hmILXS0WDluQFU_wNa9Y_wV9UDH_ZCMf-ADxL3xsnEPbq39NBVtJaLRu6lBVgl7d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bHu9LuUqX4cJQCLPAvd4hj_fdd4cx59X89Q3TrH9wunqT5Jdi6KUCe3bHiYfmVty9arpaRdv-7XoIPliMTvBCc7YAZeGX45c3_shGvhr8FxxgGjHo6dOi8PiJJUOPfNfZqvg_Aj4mh-wwPTXFGXgrHlMKhywoBAWVfV3nsdb2DjPcuhCn0HynZyExq8XOw4D6vjS1s07hMrsQlfvQd5pwDk34t9M1yJJDA1C6B8koyGl-8QSPUVuuw-PkfXH7PF5bhJGkEODlcgE34yEIoJ0hmILXS0WDluQFU_wNa9Y_wV9UDH_ZCMf-ADxL3xsnEPbq39NBVtJaLRu6lBVgl7d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNuZy5xdxbp0D1dYTuu5tSt0kMVb-PFdBLlphL_vPttLzBITKYd4gF_CkEwL3fNpfJ3zGipS-Y6RPCqT4Q7Y6Iia5MjkHRGOnsnkLsIBZTpZt4nEAX8RO9F-ZvOMJVa8uJz29X2EgumJ5JuH5KZiEvRh8XADXQS7vqYdnylSlLTwYx4cZt5iP6EGKN-zShlol7rFwBL_9R8P4lbO0ykSXrGeCet6e8QaB1ZWc5xKtWvY2qcGwn6wFBln9EilzWA90CpLNvG783hVQA3c1wqIHvylXlpgqsU6_yV3qWL1s7wFpt4-Q2sD1ZGo_h3rLtrA0tysZoCKqjelVn738h1Qfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHekWFKOOz_Vf4HcK_UqTBL8qBD_OhR1bTGW7zikiO68aXYzILhgwEhbeclXUNX9uS-Vju8aKNWUwY-IWJk-lrjWZQtPKWwuix5mXmTqLv60zmsiHZPGkqYZZm9VucpMxPxLR1weyqKZ_2Li0RUrZ2CXqbR1oZLrh78zPuBG76nl4CPkjfSg4scnla_k7Bf_q9lcgqUGFI6VUTncqlBdF1honqsBeiL2EKJIp-1mLXSu6nfnvmOscbsjTu7-UoggE5EkCl6Fh_rtkTKgiD2ocgI_vH_-0TiG6vWfD6pgj7gpO_mHIG9iVwb8ePoUPUtOFqC6av7p_5Zkb4EfUVgWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNdrk1GXOlZpJ4p8N4giM_2Br-ImDFp0v-EJnW-MgpxChI4FojEjr4AgtBJPKc6U0jvp4OVXzGnyMUlTWjV9lEJFw9xcWOlcwBQkcy4nnzyeB_et8i6fJpKNWD1a8kk5xwxy5XC6DWI5W302utwGL9CvIzoas1EaQEGirTYF2NebJ1n_kspCFMGbwkodq0DafOvIEKXJItXIIwzabfKkwKO3UKVIhma57bmllzljfqeG9uKpncCTYwf_eBb57yyJ-GmXeljsTNHEC-Zj3CpjWTo4fdnLP2GnUAakWzkqapV6i2wRlRZY06fTECTlf6g3avhRRZVynqDUsUO8ibngRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhfWnON_7bPLYWbVNEfNcDlxLdb6KzDCMBASs6NeN3sWtmqUYg6UzXpVroezHXQHJh1kCT5qn-sC7Ou7Dw2dvwlmHeULnIJ2Y5_RjnWtCXl2IYSCZs32ZsSwF4vBuAabLnV0JsxSxQHik0vKjWeHB1oNzXz4q2Y8M2Ieae_djT4eqndNomQwCWuTNcI1MRKC6CEwYIEzwGDw8VUAyi7gUbfdzcVPrpX1zGCBZLY76SL9pVswRJ0_pKO-_F2o4K6-Bq4EgV44xhlfSluZd-Asz9yGydvVwKWxCyGOC0jgU73NedEMrhJUQGDiJFKxTmWpLzEUWhT-EuYY3zUOeQZS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwvkO8hgta0pam4c6XfAZrg7bmvdzn8eqt_KFqsfOCZSmfouHUYdZO9NkiFyTL-Dkdpw4XFrkIyw2ZwJcKRMTHTuQSwp6_3OEU8syCkLzrZwtXSBTi1qrBi58bLe6um3V5nxav24DbT3T8DUu-7vMOtYfxbaQbYayeUwqY-Q4vMQFayHObggfSuwBasRpo9cKuSUpXSSeUu-6PL6pjvBoF5CE2B8AyH1KcWJX8jgVDl_7MhaHxqeem-9hmOML7-qWcdX_y1Gi5qXzPZ49GE_50d_BTFKPP9sgWA7TjYYSaTBZT4fJi8n07OPlo9wbeO1styzaEDzf7wDXjnVTqXBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXOcLpx53bQ_KlaN0XIYSNEVos3vSGY9_BJCoBx5xAYO6zXLmMk69dzUJtdwqQUU-Swfsn6ohCEZpRthpOqI-c7TtWjUf-2n0stRnZcbPE9g5-ahR0qAE1OBkesPbe2dKb67eUJFV6sTQ_EC2gAmxbnaRsNk1R7B1OvtSrLkW448AIDIH_YJSmaHv6JW9_oeSu-G26tHyNYbzPJSOGbBirhAdeUh5JcfkS_qzpHWu7_YNfd4tubZZs3IGukUYy-JZEmSeZGSql5p1omF4dBce0oOy-inF7o8i9yGWHO0YunaHTjXlzr_66Cfk434fBASdsWT3BJtzztXx6J1M7zHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cltQYPbiT_DmcddwI-H4dH2N-kpM7lMFltqUR6akbRkEfBfOEREjMey6v1HA91hFwp-_5XeODcknzcf2rIxeYDQ8-TTS6dGLcXIepjLVaV7l_-HR8CcoZ9HMedQdRsECZDwww1h8Iu9qhb7BTn7lS62GJQnBVSTJ0m_-2A6kdA9blDWcbzwhyDnAexkIYL2YKp8P5XM6zx6TiBqKHjXhD7uoUbdZAh3lGz-UBVYEj714CCmhWeGNHdko-oHXNEnXnkfmr1KQ-zDvoqolQNJ8TOz-YL2903cjtNeUgzSEOF_l8G7LvgewjzGcgFBbO5tK0yUE4MsKsUUjwNhZALxE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzP2-U-2DrK73x3couIwvWyanepqP7t-4mUm-gMhSOuOn1IBzVL6UGr3wEyUNWx1DoV2MYiBKUaeAMs9iFH1XKeYswy8xJXeYmISlMe9CP3RVO_3AGEtcI0wZRjJ79PQCmg7fjmuv8UO3op4w_Bu2-6C6P4wMGUwfe3YcENZteyIgADtZzkzfUJWwr6tNn9yb--RX1IcLoTA7wlw6JLjuufgdu6HReONF9-GFBHCnnhbu3vKEosWqA5gaKwmeHjJ7jUf_UK4l2PGYtY2PJQEM2ICmUqQHpoUTclcQknmWUEIa6aJYEuZsvvuAJGh8S1KQNxbjzSdnVc_8-oSR25SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjPxkDc6n6oef7TJB2JGr6wCleg-CeqJ6cZudcZGp5ohMYi-cgZPuIY3P5gRltfTZ5PHOLUkvwdYV9Bn5RBcAiywRrVgbzhIEQoNl9MRebVXgqIWWlGt-ftXaEu4J8wbySbHlA8H5VddsQvuCPaL0yXNohxG1Lvm_otwmDEgyjDzxqvezyZY83xyguCrrnzmq5d8_cyqlLFwcTLHwZALybfIXhhPhsd9PTDZdOKb83WVB_CB3NoE6h9ZN1NKar3Fzrmk-Tp2zy1gP6ODjL5rxBQoC4dJNNhnvGC4eIyGpqJ0NTqRyg_qBHFSYfL1X9pLSnMpAuSGOzFXaoSnWM6oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOwxOPCA-ls9oRrSHGnIHlbGz9lJdT6R_kDK8Q-liXgHy3ONaHMhksoNCyeGcq_f9OVlg0dqLg8vSh4frvZvFc65UM7M_odcGvIVOzh-WPGYBXNh5DkkRmPFKMZJi0mviV_V9hwUIAKgZ-hRp2lpXuV251oi9aa5JqvT0Tr9aYcrmcO4snYBaLkkDbgJsM4HdCe3rJQST2ID3gxvL74IKzXEbVZ70j61lFhkpx7cNJN7wyJR7xH4Yi44IH23TSgsh8KJoc1bhp-vAGVtNwx0D5aOePVcjARGdZfv2YJXjl-Ker7qYmiLdrDcYz18u9HHYXUGYYnhjigvEi-HgLM3dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZYX5jygend9wm0jry9Oe2IEUCxtpizGz3HvCh6rZldro4Hm8I7mkg2L81Z1vJ3AYjnjxxJjvLFV9ZzKhi4xpObEMdGGCBhbqBhzPwOMNVjWBQ1Yf1tBQ4uwzK7Dz8jIpgdcSncS3UzY1Pz2iD95GAB24BU2C1pbHf99iB56YziepJocQhGeLdbHtzOgu31PiyKTUKQkWGOZMVgSQQHFkveZna7MXBUniTFzriBoLIvZfFepczj5ShVb4PoN6P70FApGDPj5KZ_F7127EIMW6t43SNaokwgmqtNGOMMkvN9HvMFTS2nSxF7PkiOy0AACpX9jbVoBOq3LLpQCe3P8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq2bXtcQp4pmXXNuzUIfByhN_9BjkapZ_y2qFNjzCRQaNhRiOeCwK3qlSV1k5f5DVGurf7ygf3daw_ZojcNzNZ8eg58qdVxdy_fanH9BxTf_kqE14bSt11gy1pP4C7Ks57CCmTDbgwoZDYGcAzpl8lsc6hV_CpiIcZ-W7rSK3H3eSgkOgKNlLdaoYwWLmlAMR-FctOjP4j9UpoerXrJ0BstCc1Blwyz9jlKvGYGCj7qfKUcT-l1f79tFGDfYbGZW1mw678XJ8Pp2b18952ze6vGmwF704mbyaS1teh1XYcESI8uqYUa9p629ZhwxpGhTLEx5kLT_-sHrBNvE_g0QeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KP3InbEhUNuqgML7uTZyJlQ4pxuCn134d94uhm53Rj7muuWta5dajtb6k2wYhI0MY7Mcwl7Gvb83Br46yZMLBwdmMSo0ygJa32H7yABrnfMnqmKyeGDf1OvI8ChaK7GPRxYhYmZxtGSwLtD-1OCdM5XhRnOmtHG03G3sJQYc2iuAmkOFgDegXCdt3nuSqCWnZZO8ZNYen_Fde4eiHwD6MOOV8jKgYs9d0Fb9j5rve6oFisVY1YUQtZdVKy7f8HIF3CSeW5xzsfXzMyl1injl0HCmvU266Q4S-sDg_7m6vJJW_pjHjlrKv3wto_-g0MpttS8cRtb1OQdrFxkW3vuTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyNAu1TK0v56WkJBBVtBJDHfWvDPeyU5GVL6aAYXTe7nzs6WUJuE9omldFPmN_qqEXNr7RuUsmbdG7gh6mn6t6Vz5YJxU6qfap5oZ5ngGKfb5tMpZPx3itpCYNePHxbbAhLgDBOuzkWZEZkDZqU9J_FV-mBA2lpiEYDHYariLKOI3J5C2FmqRLAtUR29j8ONyUttGfOwKoVf-a1DO0IYmr_zcPwgbhTpGeYPn5LNFmbvaG-wBCcWwwrK9kjGQyxA6HMGRBy9UOK3NMsXF8oobiAuudOIzNv1dk3OxScts8-0OJBBnz8lZo6Qd5uW8YrKnx8iTgUpMB2SJ3RqHIyFHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8mSogK3AeJ7CyOrTCnZUi5dWcBva2g0uKZurt2oBIyQjQSpNLIGhTP9XWEonOPcjZQbI9lCVZ7If-I1BxFZS7i07n0tDPMk4UiVB4LNUzVsC7IeIkERz0ejt8I95oAHyR_DjBf_GTWb_egzKhQnso4i-9hvxvzLnbPKrxh-oOJL010X89ex_XMU1t2_gz8yF14nyy27v39oznUzK3dz9jT9iBQErCoKTW3w0g_smMo6PS_Xj7fu841CsXzkMJ7i26iM3aWBtPVvLBzAcwbnxYS5YjLYYCDKtgFH_xhXVqjj_-ipGJo6FbeASFM3fqDErhohTlcM3lvgwYx1Ftf8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSHjKhsAOl7W3de7lrI1Gy-oARmDJPmUeNvBwtSWLzaa7pX_gdzVBnLUzZj0ANA2g9ul9jus6bx7CZO2iJuE1XYOyhBLA190rQAIhvNS_G0YYytjPZh_CmQ_nTPk3EsMkkvmY7F_u53Vu1zC6wGPUp-JDKZF-D_3GYkRcAAmoOwNY4R9NaHyhJd_sGZfgDNysMzmC1DWUzOh_bZP33IafAMu2PyZgeMOMEjDfT6L05In581HDSg3QPARgQjpKcmdBTwSUopwbZ96kzQtHE9Nf8fS6IW5BTBCXPYa69jcA78u9T6uCMgpA3SdGpnCr8kFkiPHpxNcAZU7id84ubZj8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUcLu0TUnzOV6bv046D_wmX3R2lkRYzAVK43lg1q98dQJB8Sjs05DtkqdecDO2-SQ5NIXBReQurjOCWNynJIz4K6sYLMFUxTlJz_wTYk9qxw7-3LPNoaTv3pIuT6oKy53etwjlGPeb1zNKHm0pqHI2Wrfl2OV94vswMKpMXcyQGCUpQwRt8hTTDAAsuLVzPN3OWXqlAptYsdqjhCoH9V1g1Jel-e1fJ_xb51Yz7w2NvaJJdqz3Xt8oXecc_A61xBjUgITSleklbQehCaOKg3IaMF3c_Gzr5o-lqJ3Q_U0kdPeIA1ipDfw2E15HLwaIDyqzLXl9wClJ9eaJVRSK_igQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=N-Wkfp6epWL5soLen0FcrHmdLhXz-3uVHB-2CRELuCVVukJLaHEvyNqaXVKUQ7wS51gqDa7t2r01yYGs5khShTxWa4BPB8ZA3GzVqmTYbhFwliiVvFw3EXs-pon0vdL6Cg-UZMBzEHZBEhEDl-tohSZspL3Uwqmb0es2gRxJANSfnSR1dRnUw_Ufy8jLzrK8OV-v6bQ7PJM8-dEl-nse4kXuyFZgJr0LjuVWIsbBsJN5h6_ACsFkH3vM2fNIaZrncnTMiikxjYe52w03ZMzvjLpEe0ptJBbyWJ1ewbuICFFwK8vxnwLRNHlVRvB4PwzchnVIovjLxtsAScqABxklHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=N-Wkfp6epWL5soLen0FcrHmdLhXz-3uVHB-2CRELuCVVukJLaHEvyNqaXVKUQ7wS51gqDa7t2r01yYGs5khShTxWa4BPB8ZA3GzVqmTYbhFwliiVvFw3EXs-pon0vdL6Cg-UZMBzEHZBEhEDl-tohSZspL3Uwqmb0es2gRxJANSfnSR1dRnUw_Ufy8jLzrK8OV-v6bQ7PJM8-dEl-nse4kXuyFZgJr0LjuVWIsbBsJN5h6_ACsFkH3vM2fNIaZrncnTMiikxjYe52w03ZMzvjLpEe0ptJBbyWJ1ewbuICFFwK8vxnwLRNHlVRvB4PwzchnVIovjLxtsAScqABxklHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt4JbARa_KJuSrr0AmM0j5nqA9sv4fcXEG0_ynFn97THyvuMuZJi4ysvTKm7M7NPcddibhfdyRTOcqJ7Vg6EIraP88EN60gEZ_zHnQGpxopo1jXKdZO-0sFEtIQIQ3Mzoiidu2BI3WzoNABrL30F3d583SyMLOfeQzPWczgLa_xW-Be0pFFHyIcwDHQUeV6HGxcoA-M5_Do9VOpCoE52s3r8-W53KrJ6gNyyRmSsUwj7HkDDqvd1eqM24tGEM8Ck0qnzQ0bF_NkdK_YXLtdPnJ3uB8ETrXIWQGZnu_Lk-9gkDxkg9cnW8nJNdj9zN17Oa19T7xm_2_c0Y2QSRn4dNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
