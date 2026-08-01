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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLWvRidvF2WGX36rJFyIkgIwMU8tz8LI1R-TjkWtDoaERDn2JcMfma3Q7dP8EIs_jRegQ0dIh3TLudy0PfUgwTUDcJTqdMdrkrk4ng3c08s-aKyfzgOlabmkZYEKrPfJ0fLz7uqIOaX4kiYylFMCzCMZlmED0hTfpoNNlnW0_w5KhXtk6CtgXIE7Yux4q3PNQACmqO-SmVqFStMtIXYbudWQSHcBuwg9KKTG9NgTNq1Ntf5wVpT8lX2mWEEnwUtyE9ul4XcU3Ab1ufnofnPVjn7IPANWiqY8r0C3IbmKPBLZ5FGqWr8-KnmX0-Pv5ufuK_OOhabkqLEbXY50RDJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=epwSbDFccUQ7k0o5tbn8RVo6rNJUHV5KrpNQfy6PqGMnjPhLqBGAHst5B1CVf4A4EKaefDz1-TnVcvyazkzZP_rcTlsJLudy61CIoKrEx7BGt3QL9HliAkuLG9fZZ5niJXG0TtMsAA74MKHv46_8okFsy1D3v8gxfL82x_8akuWzHRjRp5zdNul8sVlgDv5ZtVjOdIN8CPYm0px4wKoDRUrH-R3e-DwE8sINQb8BF8DuwSRYPlMtL3g2LxDQ4CVQcPeh3pywkJS9fevYclGnsHmUwLaNZQHibmYDzZpNVvctzocsNCt4OpAadWcmRBHp3Nt5DAyofyCPR2t-GDfdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEXtfY8-FEUVtVRd5xFjB7FTDSe3H-iwxnqqV4pDaLdkv0y7wbH0AXhiWInvM1lBBqrvzxqKv2iNdnxi0KUn1Ar_hxL1JYTFcgkKNVTDAzSFwNpn4JAq4ySOeEHQ0G2P827Nz3JrOA_hK1_ex3B-i-CB-8rjALMoiXsNCrr55NwigTZEG4TpaGuYWY8FxGPhSh33Rvg49G_ah-EwktzSJjGN0mYDf5sN8LvAcuuG5TRqW_b6ZQCm1IiFiBoABDuYEQub4Gx9WXdbQZMWwV0To61Ic3vgcleuZTBnmShL9terCQdWPlTGWrZBtNBeGNtE3D1XpjQgYNvBYjV_OpIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgtHC_qJ3yPN5gzII6XHeuqTd4-0_vxnG8uyTzXE702JvuuVUTF2siLBGhcnSCP7FM8g8V9G_pGvlZOJncapPROPh6s5NVnJmBKvkUr_juobyxrmNYlUHRdpJo4Chha1Tb5fOJ76rwxVH-i97Nl8FCQAabAunyxf5YYuFaCzMMHONRkTWTwSL7Ygxzkk3ePLj9uRRWQ4wQZsd2vRjWN4oFsEqkflsQ4B-DW5Ol8m-QTk37u8XCZvJQD7ZFDVWgoCU3OqAaBjPHygSWPBeSdlbzfqEn1t71MvAvmHXBbQCmPNR-uoKoHNM5SvX74A6NosDqVM8mXLJjfDCGNKsV7VqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upjymYfx41tMOdc-Q3UFrqkA9pAlHTlIUcHgbULlRvHZBtzj11Zo-vSHTL7J8MBDAWC42ThsvOfoBpWsDZdcAoCbWXJR-yY148TyIdY1Nd_ULQdGXcv98QotRcxX0381Amd0m6wEv0SfE068EfpWSk4AaREE_RiLkEwwls8eOswPPBRokKwgfjbfCYPq8jwkGJxOAylnCoWo675prd-9IzNJ59GbZ1v1iMLnEAd3bUkkbOvSdK3gB8h6gn6JW7tb-fuLLdU4ZA7X5RuGaj71Oh28Px2RbLiujuzTEWmRP6pyGz_18z41MgMrpPLI9OVyQOrGe11Wcx2GUXPQegRoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7J2uektna_ROR7arJuz3sTUxNibt-L5yk6xtiGC-aDTOMVZt7f3BmrjUFNzp9gb1NefAFd2LdD5OIVDF4UlT7hwuPmZDvyTp9V23QYKP7_Hh-7sCzmitD2bxeuH-8fCc_UwVof-FTkPtM1fIhjIGjZXoEjgDorN0iwBlVphf5BWXMbye9bLIbQNnQaFr7Cc1l-cSujr2zAQUypNGEnGgT6Ni4Sn63Jz7QIftEl7ser4pkzvXK1J6fIbm8LdWSiH1t0YW-8wdzR8fiMEvA5Ge7vhD-O8gbi-nctTSH5ZcdvtgGUGcu4AtlSiQXylTUp-U_ZMHkothw5yMB7CLA4POA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhueWcgmxsedV5e8rqwN0tCIB_CqRr13G6qC8OwCj8AwrPXIJZTkMYKAkUTSmRm7QTDjW8Z2Kj6WGj50PFldcpllHCf9UslAYlpqW70G0LeOlekGYUo-g_Gsf8vEswiMeVlzLuu0b9oK71WTPt_yHhqdKY3bT8Yk2L7mMk7_27vu8MxPpRvI7d0_V1Tc-jdI8kGemGz10S7p00E74diD-A2SPVXC5qaysCdPKrZKLHxCstME8geDgLpgNTEurfyXXeZ26yAWvfk5GFQljup4eN-523FZ0ve9t2Ssl4XdJRuhiu3COhULhtaskcnx-GKkrQPXXLdOseWyWxBFGI3Hsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eubL6-8zmHYGJtB7dpKdEy4Y4Z8hmr6ac-nCYgnJkS8HPcM6IZRYNyZVPdChDY-IvoYROmeCbOdx2klouLAbh4xBORvgdHMj6q3BPJ_0jQTsfZfJEtxg_q6FTIMxQYFD51IsCVniarMmjwwGOIhqq8UTPqxa8GiMxVAapu1gmsDKOf3iUZQMl31Z0AGMXMnMuqK48Pd2IoBJN_fzc7TXo_PZ-8knmURg6Y5-lZDaP5xqrbW7sEuhCkB1jj-PgPJnywAEXtBLfJL0uWgbS0-u6WTgHvAJXqti3mvLN0Pnp5sbWQlVQmkUGe5TrUVIsmvm4jfTbwLA7sHVUn6Gv1V3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Z4nYIpW3Z3ulnIS_DXvyW-T79a-Hw50tuKlxLguBGPPgPr8KXhLByFFoRQSwC3is4Uflfr23UxBU5HIIwBKiL6pIWsWOwHADB3T0Ng1e1K4uUUKV8Lx8J-NR4hNm8LYLHz32G10uCSWDp_G8K3GW2cZgGHVbBawL2biMCEQSIZR3o_FbqI0Evi0k_jbiMfYVo3bSLQ3e1F2zwXw3Aa-gFij3Ak6cWS2QskUA7u5QQznem88ehz0sxbmtcmdn6UJIzLf3yfEArN_B6elnhlst2_9WYvpFkHXLL4BE_-W7giuSk9j704O7dIhnP62iFurAjzXA7ISF_lT2UNdv94OqoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5Z4nYIpW3Z3ulnIS_DXvyW-T79a-Hw50tuKlxLguBGPPgPr8KXhLByFFoRQSwC3is4Uflfr23UxBU5HIIwBKiL6pIWsWOwHADB3T0Ng1e1K4uUUKV8Lx8J-NR4hNm8LYLHz32G10uCSWDp_G8K3GW2cZgGHVbBawL2biMCEQSIZR3o_FbqI0Evi0k_jbiMfYVo3bSLQ3e1F2zwXw3Aa-gFij3Ak6cWS2QskUA7u5QQznem88ehz0sxbmtcmdn6UJIzLf3yfEArN_B6elnhlst2_9WYvpFkHXLL4BE_-W7giuSk9j704O7dIhnP62iFurAjzXA7ISF_lT2UNdv94OqoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf1WZestAUYdpeD1cIe0CWp8PuQ4EaIxqBkqM94uGhcg-6XqKtXbYwjvwEclfGI3y5idZmoguum8GhVVcmK2uOa7DvKGLF8E4ou69LLpMphvpIRUmUFsfIKrgxIo_ws58aCLWVm6dSvuPMIfpSK0P0T2age-vKDYtcJYlX2ulsc4FXwrfwb4txIPF2dCKfBJLKR6wu0Ku2JHOgmmHDBpPxCWXJvOt8xZCVAeSf0T4WN6YhnvDG-OGRHYUNcrAK-fdoA5EqXT6dvDexg-onJ2fyHOVGTqT2RTfZRG4A3Cpsx9tAFbs8_XrnX9ilNMIWeyinqPo6v70LgN8IpValI9HG9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf1WZestAUYdpeD1cIe0CWp8PuQ4EaIxqBkqM94uGhcg-6XqKtXbYwjvwEclfGI3y5idZmoguum8GhVVcmK2uOa7DvKGLF8E4ou69LLpMphvpIRUmUFsfIKrgxIo_ws58aCLWVm6dSvuPMIfpSK0P0T2age-vKDYtcJYlX2ulsc4FXwrfwb4txIPF2dCKfBJLKR6wu0Ku2JHOgmmHDBpPxCWXJvOt8xZCVAeSf0T4WN6YhnvDG-OGRHYUNcrAK-fdoA5EqXT6dvDexg-onJ2fyHOVGTqT2RTfZRG4A3Cpsx9tAFbs8_XrnX9ilNMIWeyinqPo6v70LgN8IpValI9HG9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Fq1RrcaglABPLyOmhSy9HWYej9kzmq-0-qNepOz1RXLKC_I9SMVJcoSg83x2oP_2WF_A4EiCdmRXPMhWu5Mw7M2PTSTRDbcAaQ9W3AMtmI2z4E42nHI9TmmerqFH9Yx2Ehv4fIO72SeL02VAER1684NlkxpAVXAsksSMjlG0bLw5EGvbwJ8DMmnVtU3bxnFmcwo6PsfOzJhKKFeL-86vavJajfd4OynSbAoLu975k1sVNy-BNia_MmdtGPHvx65aGn5iYUfqnlAbiABgBkgwbGH-eJU7YqEZYyZ6KRMyOElMgmThk7fVuqTQPwvnJBigy6FjUIcSNphFPO4i4C0BRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=Fq1RrcaglABPLyOmhSy9HWYej9kzmq-0-qNepOz1RXLKC_I9SMVJcoSg83x2oP_2WF_A4EiCdmRXPMhWu5Mw7M2PTSTRDbcAaQ9W3AMtmI2z4E42nHI9TmmerqFH9Yx2Ehv4fIO72SeL02VAER1684NlkxpAVXAsksSMjlG0bLw5EGvbwJ8DMmnVtU3bxnFmcwo6PsfOzJhKKFeL-86vavJajfd4OynSbAoLu975k1sVNy-BNia_MmdtGPHvx65aGn5iYUfqnlAbiABgBkgwbGH-eJU7YqEZYyZ6KRMyOElMgmThk7fVuqTQPwvnJBigy6FjUIcSNphFPO4i4C0BRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxCvJ8AoP9zJjAuGcDkZ-R79JeUBoZKSV-z_udfD8fHWWvDlXFf_9lep24jTyG0MH14E5Fsp-ZbzAlr6ZRwumPDvft7Nv6Pyh3M59s2b14XcsdFOoPuZ7FucIJboC6f5L04QMxTfutwj_-wE2V7eWAYhKahW7PK4_cUV4cs4nsY3zWMGHWVvkuhw7XWjgEm3-x170WFlDdlpiwxLjY-MOm5S0SmhIhQx3Gr7Kd4Qny_xm16yOGjpo2hvRoPqINLFb0C4XyxNKkn4AFRF-JjgWKHlypm2lzi4yffkvv_6dygXhERMHk3MGF4_Bv1_xiMg1U-dPDw7jQmgbggCS6AAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8IlKqcSDFmKcaFLj4kP2mXdQ2NIQ14Yo41BQs7v3JW3miBEW3bACs9bQEeNR7OuRZgZ_V5gTR1opo5OvnAGA6kFo2wjw44DcJaugVOsmNWQqj_ZgIPlJhaZC_l0jAZRiOBNitf3qI_ITN1gzOu-pasw_YNkrmb5f2ZpFQdlX8tkhAG65iRpTjLm0it2BPt7ToiS6kmKRICefrbXhekoc2Qsgdq-BloW8Ez5aH3h750O5xep4ftgWXjrB4i2Is8QOp382oOJzlLHH6XAhqRMrrnVO3sHPxxrrtsXSYuAiAVScN1lnMsQnGbNWsGauvEW7UCbMmTnIWD0sLonrgaK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=kR8tHkSKo2futsrZ2e1NVnYMSvefTKI20OWuNp4tBvv0iZOlMEP5ZEKI44AZFynnMTGkr7_CLjSqko2laH1L4_1fVW-mvl56YBTUjGqrcMBxojk11irrP_-CAOvqOd6GjwV46tHXtJ8DUz2ZC512F0ccYGWpRmqhhnBdbiGevOpeDVzVHpjItK5khRFElcrAigedLwEMtF3vvSgmcdZJtjzTNoJwChyXmXLN4ZOCfJ8YRYd3O_l9gb-c2d_bb-VeW_sx6YPa68HYZVGJM2ZCNbFQjHq63Qvr_YUp7jlI3Yu9yLrczAB89pSxRUsyzZRrzz1u09EUf_qz5lDhvQO4nBWTlxLv-xpp_3u9NyJShClYUGwYqWmzzLKxIhmL5w4ynOM4OdyLYMlIWmVvjs-6DCUkyeAmquARMeB-J0kNlMHQ42wi8CrSg7tHuE-9_MATlg3qs7wZcLOxsaxTz7gKsCNtY2q7KzErvok7oujsZ2fXH6inCWy1I0jtL6UCBh71t3I1pfjQF2e5aOSrOor4i9iIH_z9-Ic6bDzaw_5d7Pr32OpyHO_rJNDOUZaCxJzLTKJFTm4W0xCDJOjGW7AY4hwPWu0FlV5_Jq1DHA7HKKbLlooxyNrm3VJUuce3Ut8FifmBJ4QVJiVk00-GSdKddBnu4psPYhGa5PqLhO3beFI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=kR8tHkSKo2futsrZ2e1NVnYMSvefTKI20OWuNp4tBvv0iZOlMEP5ZEKI44AZFynnMTGkr7_CLjSqko2laH1L4_1fVW-mvl56YBTUjGqrcMBxojk11irrP_-CAOvqOd6GjwV46tHXtJ8DUz2ZC512F0ccYGWpRmqhhnBdbiGevOpeDVzVHpjItK5khRFElcrAigedLwEMtF3vvSgmcdZJtjzTNoJwChyXmXLN4ZOCfJ8YRYd3O_l9gb-c2d_bb-VeW_sx6YPa68HYZVGJM2ZCNbFQjHq63Qvr_YUp7jlI3Yu9yLrczAB89pSxRUsyzZRrzz1u09EUf_qz5lDhvQO4nBWTlxLv-xpp_3u9NyJShClYUGwYqWmzzLKxIhmL5w4ynOM4OdyLYMlIWmVvjs-6DCUkyeAmquARMeB-J0kNlMHQ42wi8CrSg7tHuE-9_MATlg3qs7wZcLOxsaxTz7gKsCNtY2q7KzErvok7oujsZ2fXH6inCWy1I0jtL6UCBh71t3I1pfjQF2e5aOSrOor4i9iIH_z9-Ic6bDzaw_5d7Pr32OpyHO_rJNDOUZaCxJzLTKJFTm4W0xCDJOjGW7AY4hwPWu0FlV5_Jq1DHA7HKKbLlooxyNrm3VJUuce3Ut8FifmBJ4QVJiVk00-GSdKddBnu4psPYhGa5PqLhO3beFI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=RmpI6zMliekDWAIPPFOevzWkvUc736GKkBkMCyECFehyL-TtQzyShMoFaNaRMHToUsDwfhM44GNhxeiNTGzUFTJoLl1lqwOgrLa-oDAdlvXLlj877JjVmrbO2TjPbXDgYNMxJpeiSuVeOTydLCx8cK47VS_W7f2dwgwGQi0qB0zieEYrd4T5CWMbz1Ink_D0e8aVXpSuOY6KZQXM1dPUI2My4IkYfPURXNxMSWIyRzLXhCntYA63-1U53XPgQh-nqhWhRjWjnYUa4KagpDJYiE63N3b9wGzU-MCv479tdCbKuIPn7qy6eGy67OZ4FM3_mgE0g5zLufdPLH9tL-kvvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=RmpI6zMliekDWAIPPFOevzWkvUc736GKkBkMCyECFehyL-TtQzyShMoFaNaRMHToUsDwfhM44GNhxeiNTGzUFTJoLl1lqwOgrLa-oDAdlvXLlj877JjVmrbO2TjPbXDgYNMxJpeiSuVeOTydLCx8cK47VS_W7f2dwgwGQi0qB0zieEYrd4T5CWMbz1Ink_D0e8aVXpSuOY6KZQXM1dPUI2My4IkYfPURXNxMSWIyRzLXhCntYA63-1U53XPgQh-nqhWhRjWjnYUa4KagpDJYiE63N3b9wGzU-MCv479tdCbKuIPn7qy6eGy67OZ4FM3_mgE0g5zLufdPLH9tL-kvvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARni1O6YvUuHvUOE2IOYjTjFUrxiAEarm5eVCUu-DrdXwrTOnn0y3p_72hmTQut_CM7fEmst4jkhIXZD4vmSCfpCCIgQvF5ZRlm-1DvCb9IB8HBDSqizBNuTDcwSnmeJaN0lE9OgeZnchRnNHYnXLqZEFGbyET8MezBcpZ2wAwIJejlTtrEtUdZUBHhkLX3csVhhGMqCPqt21mVRePaM6sRpkBP3ssS36tX3Ttq2Th54liQPDHA1e5w3ekN3B3cvdNdKIim9RrofDV_pAwVoQXeNjeJZo9i7gcJ60BFM9JByuOw60oMhWVS369DU0nbv3VLUpoaAmrJGxYgFiNXRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYS7918eZSq7mxNZ4OU7P1CIwiUklikXEwgjH_Be7dSaj6hW3fAWVFfy_yXB8CeEXGrkGUGAF6r2zMOqWT0A8PfbW4fLtN1LnqJfxrn6rJbsyOdCE0BXUJzfidGclpr8jcOTrM9Cl9wn9xghzPtgdV6F1SL62srYbaRvVwGiD2jQkAH-7-anyfzJBQ9YZz6z19N2MBNmjSqsnsZKwjXBDBdZFQdHTI1fx7ZzcWa7r0VJmBKKX_jDvwI435qI1I2d6fIYkOS2l5XY_TrwaC-48iPVel8JxLm_efuX-Zk0m15bt-p7KDJqWcEDn2c_5kiusLuDU0Lmn7PGXCk3RJot3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4Wr149mwb1ddGJ9rquY3T6vzLrOOyWqEODR16NSHikq5BFia49AVSZeL2iQy-c4L_VedDkyCLap8AVLbJNEwqiYWphdp9J5yp47yP_oyQlUoCYmUqaAGsy6nl3sbDvssF4Sfhd1TgQA-UPvfNUvw4LCX1l7Ek0Ce4zmZyvYnmtzkQWFmyNo-7Ed6KYhf27drCYHxtL2maUhdZGf5FoP2gsJWjLiz8AA0JSN9sIQXB8KsMdUzphlEUVnYX88IraiOXGGlYWJVhsUBEo29g1n8gQZ97q-D9r-WgXX2LNjpriGh8h2EfbDumYYe2Ri94ZzUpKcw5YHMen1BTvBuS-wqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Qi5RgC_oUAxSKGBGewDV4YNvO8BPpsuZ79gHwpAZtMcidxH07q0YGzZRwP4xzGXs3ngAYvrAy2LuxeOQN4m5jOj5TCDLmW87PjorLDWry-YJV4DdkyhZ6rCXDGRGFYhg8I8Z63E9guQtBvAoqcLPwK1t8lL-bUa03MAWcmEQEiHgobl3jOdRgJgi_iUcmPOFOijiCzdyzy80EDNWvMKEPNPiAsrZIemASdifMYt2H9t71WC1Ukp_r_fox7CHPeGPxqbKEVuGUZpQ9qDp-T0eeMaAhYpXuGgBWyhdL4s7zGlzYezg4cblnEJHFbOZyoF4OSZdLplde0sW4ESkHnXYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Qi5RgC_oUAxSKGBGewDV4YNvO8BPpsuZ79gHwpAZtMcidxH07q0YGzZRwP4xzGXs3ngAYvrAy2LuxeOQN4m5jOj5TCDLmW87PjorLDWry-YJV4DdkyhZ6rCXDGRGFYhg8I8Z63E9guQtBvAoqcLPwK1t8lL-bUa03MAWcmEQEiHgobl3jOdRgJgi_iUcmPOFOijiCzdyzy80EDNWvMKEPNPiAsrZIemASdifMYt2H9t71WC1Ukp_r_fox7CHPeGPxqbKEVuGUZpQ9qDp-T0eeMaAhYpXuGgBWyhdL4s7zGlzYezg4cblnEJHFbOZyoF4OSZdLplde0sW4ESkHnXYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=rWD1MEysJph-z5xxLJxuGwbeUA6EdqNORhS99P2-ew0UpjUxL3fAyjVgXsTr68vid4RZIijmtwONcwQm4kzEKOm8QGaQqpHi0StYNT5WjsCQgZfMwc6Zd48o256YS98p3QZ9b31ct6s0RGoN9dYT5Ap4QrXzjwPCzZbM9dHfRcAuQkKvQno7EEhrum936Rg8s3Z1X4GQTmgT_ZJyLLybLw_5T1CG-WatdGS6UqLqj4hE2uJr5CQrQnAfC6EWP-1Ob-mYuVccDU0cGNwQJPhkeS2soQJBxWkNCr1-JbNAmkiIkHBvCI3oCu7kyMEaBWZanzmoS4ELKcHq2OFhcO1Rf1xA1PEU4dBtW3UFN2hrwdUyTbjaVezrZxqxgdN4wKhUVVAPpzgEO3mWLfaLJKrLERmpVDNa4F1LoSplvZv1I2ajIIAKT8QZwOJQD5Izl_s5cSqee6upFF7V5ULRcSyeyWUPgiIYZ8hb3vV9v2-vqBrz4Lp2cWuUGycqK2wPD8bMMTjeWlGZhn-CWxJbmuemDsUaz0sxi6Lm7-HLFPehiBMT7ZClRS_GaQrt9TV6VcMK8b0skBH1lahWGwQrlUVz-Aohfpeh5n8SJb8DGib9Pg5hlMMozByxO0QGm005VTeSbwFjhI_Y2bl1VubiFyBh_JalwhDvnHo3IZsVTh332dk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=rWD1MEysJph-z5xxLJxuGwbeUA6EdqNORhS99P2-ew0UpjUxL3fAyjVgXsTr68vid4RZIijmtwONcwQm4kzEKOm8QGaQqpHi0StYNT5WjsCQgZfMwc6Zd48o256YS98p3QZ9b31ct6s0RGoN9dYT5Ap4QrXzjwPCzZbM9dHfRcAuQkKvQno7EEhrum936Rg8s3Z1X4GQTmgT_ZJyLLybLw_5T1CG-WatdGS6UqLqj4hE2uJr5CQrQnAfC6EWP-1Ob-mYuVccDU0cGNwQJPhkeS2soQJBxWkNCr1-JbNAmkiIkHBvCI3oCu7kyMEaBWZanzmoS4ELKcHq2OFhcO1Rf1xA1PEU4dBtW3UFN2hrwdUyTbjaVezrZxqxgdN4wKhUVVAPpzgEO3mWLfaLJKrLERmpVDNa4F1LoSplvZv1I2ajIIAKT8QZwOJQD5Izl_s5cSqee6upFF7V5ULRcSyeyWUPgiIYZ8hb3vV9v2-vqBrz4Lp2cWuUGycqK2wPD8bMMTjeWlGZhn-CWxJbmuemDsUaz0sxi6Lm7-HLFPehiBMT7ZClRS_GaQrt9TV6VcMK8b0skBH1lahWGwQrlUVz-Aohfpeh5n8SJb8DGib9Pg5hlMMozByxO0QGm005VTeSbwFjhI_Y2bl1VubiFyBh_JalwhDvnHo3IZsVTh332dk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEPNmlG5GmNWfPgDtH9Z3_HatbrPsEB4tYRVEQ05uaLbWPbtKMBTigz6AXXHmG1tsxmoF3AUtjPevvELZh7M0fJL17qpUQeCsKWLbdhyKEUfzJJiIUMLWo_MHp6-jxSZRrgRBPtf24-qk-QkYVFLyEXw8CCS4lolf8ggvfbD4jt9Vb8omtddbm0sSwbHEnuVNl8Hz-YBZkhItYZTeTX2jYfcEWQg9iOj2cfelLf8ybK4vXNGo6xf04dTwf6CVmmEQOMRn6xGWMIt0lx9VwF1t-zIPNsRWbAJWKdfb15dDBRAKX9JjCZXCqmCzQb3U1QQMfJV-s2K15CVmvtDEZT7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoyPUQGXN2jW8SIMn8hTDVTAa8YjdWVervYvn3REaWeWtZUxgTaqaHWBZtnNQh5F15CQqJw2wNJ85Ar5tx2MVn-MdCWxu_lhlGX0bONsoSDBE9dq9PsKjWNk5aIZW98mls6rB5KiVyuyJHcLTzNSJ7MkX290pzFgik3I12dTpN40v16SW6p6RqmUGPjGZ7wE-2BxO7eSq03x9FhkGqxK5epykzfqgy3deiVZ1MDK613sdlFGRW398YKbLQrH-Z6NpJQvPH9rcNKNKcIlFEe65LOVArNe_MWtGpjil2pmn30uK4wcWjOlGJEcIsFvLO42nSY3lnY62Zi6K8CerILQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=XuaiRC1331aVHEe3AkVwArwsx9i7vqyxFxh9NuPGTwWJ0ZSfmwoThSHADa_F5xPOOfW4ywHXef4KdzVxtc0IfIkLgY2tAuHrex8zlZDy429PH_JpdZ0zHisYW-kZN313BymkIH53m0d_37HMboPjx5slmFK5LDyMAOjExKe-jjxZ4nM5cNtyd6xBcuZDSDsDKJDc9mKu-F1vtSVqt-awxccik-ZO-NpZROnShQSwDVl5xkcvB7aDVRIVpsLhZmHMEbN3Rgj47mZZzZkRFWh1e5lRqGgw-qYtyyAK3jbSOvL8Y8fQ5gT_Jka5Ae1mDT_Fp4EAu0D5J7V5s_tBoC1PZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=XuaiRC1331aVHEe3AkVwArwsx9i7vqyxFxh9NuPGTwWJ0ZSfmwoThSHADa_F5xPOOfW4ywHXef4KdzVxtc0IfIkLgY2tAuHrex8zlZDy429PH_JpdZ0zHisYW-kZN313BymkIH53m0d_37HMboPjx5slmFK5LDyMAOjExKe-jjxZ4nM5cNtyd6xBcuZDSDsDKJDc9mKu-F1vtSVqt-awxccik-ZO-NpZROnShQSwDVl5xkcvB7aDVRIVpsLhZmHMEbN3Rgj47mZZzZkRFWh1e5lRqGgw-qYtyyAK3jbSOvL8Y8fQ5gT_Jka5Ae1mDT_Fp4EAu0D5J7V5s_tBoC1PZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWk6C75RYffEzRykFXKRDplzccCL-tLT8iAtEIYVF_xDqMsF0W9MJU8ehem0mP7djnUNk1uuP5C9JBhXKVUFNQMqDxzzqMeFHD-H8ATLYEzEdaCVt5x4UE_Dkcxv7sjy9FXkO7NaKWiq4oaCTPFA40lcchSSb4GKEnhHZxxUwNNDgNzXZcvbmn74d3MqbEzncI1Wju-E4HLUrxPEhsuZtMNurdBwOkriZQuyELXY53s9LeVg772yZ1gZv_RoDVH69biB9nvkxzLJG1k4oahhuBiuIvOy3Atmxgwtgo6tmuODPrtBvaigOZRu8khLh2D2W-XPLo2cJksGx4vog2CuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc2hy2hm0Ez-1V8K62VT9nf1q_eavjN7Lhf13CzN5xC_caI5SVz6DoGb46e3mcRxP-RA0f4gfNBttVNWXn5u0YO7f6SjtDHF1moB6iNyWGxWPPo2p2o3e9_FMWLpYqwWBLeyiaNag5g1q-6H1SW7cQyfxN5ApD53tvDeE9JACIfdoJJJxz6zg6Q6T2YbZHunmgqyq8TST_7G-m-0IzY_LTj56PjuC0SnSUJ1wEzlbsMNC7PZhbcRwZV45_78JEmzEQOMcTHlAQjYacIC23Fv-1ggRvuuYzAP1FlXijJXaYSxOhanDXYO22R578U49ohkbWzk9qTPNyx3Hnbv_FhlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owDiOsFCxfrSHxTLiS2zeF92407ZL2M1q9TBHrK2KRDzyYauMHP4eQGqilu5zEXKQKiJW_qxhJEkyTtChPbC4DmtuG9cz9J6mlCF56btrtgHzeS8zvLN74kZzHBRlHDW-TwzF0lD8F6HdDYSKjTFFYG9LnsU2NPPKXa68VQgEEpo7v9sDdAOLXB28lAsNU-i4yytN9noOC9J7HMKwnP0VTb49Ck6XfGw4-6HAAGWPrP9DvndF4nRjmu-24n5RIkTuG4uK9ROkoTyjcJ9ZGBsNU7NkavuNuy9rKxAt3GGEVgFLnY799Mc3Iyh_hTcqKwijDDl1HBID6BgSHipkH9UYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I4jHcMz1V-EGX8PW3s-1xspKseVfjnvw9-9tOmryaDimkX382sdmui52hub2iwx0xdOjl2XnqID-Ve3YZf6GntgUAEGbrHQ0r7jODoLkTr5o_rMffJ-5vY-5TODiL4jfSS70uYJ7fAKNUGngtW0m2tGGDMU4_b6kZIaJH2jr3cSdvd_708mt3lG1SXvjqgTi3xRx3DIuAPGbUvi5HGcwpT1EMEuwdRsaPYOjJlVrQj0yK34ga8N6RxOf4VMZLpHzC4qTSktNm7glaEsZ8UHElLDm7u1iK3TJQGn_LZ2YpZKXO5ThLbF3h9ent5x7tkFqW6x1skIKNauQaD7lQY7H7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I4jHcMz1V-EGX8PW3s-1xspKseVfjnvw9-9tOmryaDimkX382sdmui52hub2iwx0xdOjl2XnqID-Ve3YZf6GntgUAEGbrHQ0r7jODoLkTr5o_rMffJ-5vY-5TODiL4jfSS70uYJ7fAKNUGngtW0m2tGGDMU4_b6kZIaJH2jr3cSdvd_708mt3lG1SXvjqgTi3xRx3DIuAPGbUvi5HGcwpT1EMEuwdRsaPYOjJlVrQj0yK34ga8N6RxOf4VMZLpHzC4qTSktNm7glaEsZ8UHElLDm7u1iK3TJQGn_LZ2YpZKXO5ThLbF3h9ent5x7tkFqW6x1skIKNauQaD7lQY7H7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJYNkp_LFLV194-1kxxPLu5po7oEYiYeMgXNz1aw_DZD5TmAyTQgMri54amuxKURNq3Qc8OTrtppMW4ZuwIczzqCgmFSv94wVLxJOMiX2fmqZmgLJWjB8bIDTj14zF9nVewQ_70J9pMb1ZlzV-qO5ty_iuoern-bwFaPY-h53ooIXyxpbiekHPjas3dTDKcO7043JVTTON8Lo5idcOYt5rfJrdmvoMYWhwYNflkyYHANIUJhxjjCjomv-gOCsh5TXffOpQo8TiKfM6BCSnI8SSJSpo8fD9sGmg0Oto_4CloexLqrMxjLI01GRIof67E6axGEZ2KizMC2GvmrKq1Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS_EObHuyBE0o8mzP-OXn1YhVEX7BOfs-rxOGLMu7PIBJT4c_PWSgv7k8KTkSCntmGd2M7rwo0z7ESdYYF_e-9Uz7ivbij7C83M0ImZUv8J6gZjbcHZ6ptHRxnbKRto9VE5qN4R5G9nr3M5NR7pPeMKimAniFdRqovsgnCMJQVCD20amn4EU6ehvqxHUpawNjYdT61RDnGCNSJ9V-wihEYobinDUzGc5RjTlyhmJxagUGoBFyPAgw8zhtLAPGmKImo1VQyvxHpTl5xj-6XVcOZw31cSHAdkLPORCn3DkUtat7LUgeM_gXuN8Xvf7cz7qLRt4WTri8QAbkhWhk7bdBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=jYAQKnOVNKrVYrLQ3RFZRdJqoTMA0e4QrWr--IqZUWf_59ekGEmFg-_ILbc-j2_5puPkIsEjuZpV8R7Mw4B45PuSw9eelvF23NDfkheLDAmXw_km4NSqxP06Tnu7NF1Y2MU1dqgvDpJhHXwLQlDWMtcL5GHoKfCN6zCWFH8HDWlCEANofgtV1kC8zAvoHA11lsPQj2V-2b8mGEHGVPNXUNdFlNPEoP9DienAQWBjsS9aT9GExMmBxsueVUJbJ44467BZdpwsl27QwJtE3z5IWUnjAQaMvtV0OlZfcpTO6UtnuBaU5IOC-YEom-LVT_X8bWBvJXnTJFD6LvVKxKjyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=jYAQKnOVNKrVYrLQ3RFZRdJqoTMA0e4QrWr--IqZUWf_59ekGEmFg-_ILbc-j2_5puPkIsEjuZpV8R7Mw4B45PuSw9eelvF23NDfkheLDAmXw_km4NSqxP06Tnu7NF1Y2MU1dqgvDpJhHXwLQlDWMtcL5GHoKfCN6zCWFH8HDWlCEANofgtV1kC8zAvoHA11lsPQj2V-2b8mGEHGVPNXUNdFlNPEoP9DienAQWBjsS9aT9GExMmBxsueVUJbJ44467BZdpwsl27QwJtE3z5IWUnjAQaMvtV0OlZfcpTO6UtnuBaU5IOC-YEom-LVT_X8bWBvJXnTJFD6LvVKxKjyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=gOlSSmqnHgmtjcRQerYCDyf071vgropGCx0KqKf7KYZ4LETSdQDzoazgl3sQ1EYYfQz6HuoOm0XAeiOhWNu7c7jb5KNPJv4Fcjwnwp52th4UAlFl1C4hirCttyUeY3gkInbySo8-v5IYmHNRhPFd6QWeeB5YfYTFke2VernOkxxdlITHRCSiuaelx03SMHpNc1-VRQmx3f_oIBBVY0NeG6ij0f6bqBBXMAZzmbhr1UI4e19yEG7l39cEkAsDvjhlBaEyVl86f-9PzdkrKN722o-Qf3O-yHbDpb01f0BqlxQmnCV3kda3DUhggU-4FNCg4j_DCY5pQMsCZ7fJZ3iYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=gOlSSmqnHgmtjcRQerYCDyf071vgropGCx0KqKf7KYZ4LETSdQDzoazgl3sQ1EYYfQz6HuoOm0XAeiOhWNu7c7jb5KNPJv4Fcjwnwp52th4UAlFl1C4hirCttyUeY3gkInbySo8-v5IYmHNRhPFd6QWeeB5YfYTFke2VernOkxxdlITHRCSiuaelx03SMHpNc1-VRQmx3f_oIBBVY0NeG6ij0f6bqBBXMAZzmbhr1UI4e19yEG7l39cEkAsDvjhlBaEyVl86f-9PzdkrKN722o-Qf3O-yHbDpb01f0BqlxQmnCV3kda3DUhggU-4FNCg4j_DCY5pQMsCZ7fJZ3iYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5q6OmGvQA8hmn0dWXKUEteenzv8xp8prg__iwRuH7xaWvAed_HSrDSI8QH-MbTlb12A7RMR9g3oh45tijbBamX6Eo3M8f8-ZIMeLZgTjhCJMFo6jXT_dTSPS-cNBQJrbpZmPCinmlhcnIP5D3-6iEem6DwmFJE6Hrr9p4fbTk47zO5ecP2m2w8FUjhVq82jPWn7xHyw9mw11wIGBlAfJExO3EwxcpXOXJWLT8ROCMSAXwnsUUkAHImGt0Pgefoo-1oProhp3H4BhDQT5KptxXMwzwT46WhfyT2f6_NnVrN7-EGyN1ObQVgi7cksHd5w7AIJ0udt3UcCx07MXXDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/basY_epWc9lCTSTFcwfLvIj8UIm542Tmis_RenNX_fnKFOrzZ9D1Dpk7JaLP4gk8kG_jc0DTGgiCQFs1YEiEdpNMEi4YeuKcnFI2gSNnGoal1MNgvtTykz7QjpQpPCYkVgDfoHSxOcFKM8ydpmlRibVoC4k_pJQL1M0jH2KvQJs5WK7od7M0K_GyxBASHSZ1HvtBpn9LCMWFPT3i29_ImOSOtOfrCDsQwMDW_Z7KweHVNsYucNnmgJDi1vQFSpSeEhZkttDbKKzGM19VRyHus4f7j7UwKDuMalIcSVGvFYxB4qnvtQGNGZ2aepBOTQ223VdCO6G6AwstKxpe9XDTlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=aLvx38pd-WNSyF9_S5ENI2zrMukKnsPYZBU9jj3Kn9huTjXz7w7r2pTCBJUO7BnDOicCDVj-KRZ0TZh3nYeI4QbkK8D37FprSHn8VHOMCxb4OhEfw1SmaDf17CAeqDKpM7NiGnnLfjdv2SNqB-M8GGiXq97zu-bJJBpzmkRU_jMS7Yd9VtHQelJRVYaCcpY1zzVjm1xZ9ElwMyGUdQf0hge_j5wNTQYTutHlWQQ4PVWjQ7-AeryiOyRWJhGli_DaZ57w4anDnnkquUX7e_kLc6jZGBZvu_Z9_JTrUGf7b24Swfk_dx00SU2kR7r03-rSYavLzopIE5-wdPaGM6Hwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=aLvx38pd-WNSyF9_S5ENI2zrMukKnsPYZBU9jj3Kn9huTjXz7w7r2pTCBJUO7BnDOicCDVj-KRZ0TZh3nYeI4QbkK8D37FprSHn8VHOMCxb4OhEfw1SmaDf17CAeqDKpM7NiGnnLfjdv2SNqB-M8GGiXq97zu-bJJBpzmkRU_jMS7Yd9VtHQelJRVYaCcpY1zzVjm1xZ9ElwMyGUdQf0hge_j5wNTQYTutHlWQQ4PVWjQ7-AeryiOyRWJhGli_DaZ57w4anDnnkquUX7e_kLc6jZGBZvu_Z9_JTrUGf7b24Swfk_dx00SU2kR7r03-rSYavLzopIE5-wdPaGM6Hwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=ZHpXt_Klk1Z5lA9jf6m-zJRlReKUHKTkggQdL3vSBvOSGhUiltjsokwVdWC6B34e50iiDeQ_8M0ytGjp9RuCQAZT8j12FSeI27jBVbDvy41flS-1Vn0oeHGAepdZWclCod-4sGeUoAXw2WjqvgkkzWxMi6EpqQolaGcXDOBb__qACQIw0N2dFpxckvrEWGVa95LhxsUL7XXJf5EVmlGNbPjymtgCOAy7l8926RG-9GENWIL2CgtBVv6oH_H1qw0q_OXs1mQV088aySc53v529b9RXJlOXezW-79x4-G4lr5x4aQO0VUdyVycbvDYIYdMI4mp_i8w6T7q7R92PTmZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=ZHpXt_Klk1Z5lA9jf6m-zJRlReKUHKTkggQdL3vSBvOSGhUiltjsokwVdWC6B34e50iiDeQ_8M0ytGjp9RuCQAZT8j12FSeI27jBVbDvy41flS-1Vn0oeHGAepdZWclCod-4sGeUoAXw2WjqvgkkzWxMi6EpqQolaGcXDOBb__qACQIw0N2dFpxckvrEWGVa95LhxsUL7XXJf5EVmlGNbPjymtgCOAy7l8926RG-9GENWIL2CgtBVv6oH_H1qw0q_OXs1mQV088aySc53v529b9RXJlOXezW-79x4-G4lr5x4aQO0VUdyVycbvDYIYdMI4mp_i8w6T7q7R92PTmZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMlyQ7KgNTCdKznlitWnzAqMaZxa9fyIbBt24-nCFudZRigLQnoampm4Q-fgE-t1lDh2vNy3ocVdtlAVlF8u157W1Xotgub1ZiZLOIMRhxMKHc-E5VBFuUfCXzWiOnzI6NX5QvNtbvW7ESc_7Oq8U6Is7rJocKtf6t1ecp_Gwp5XrJ4br-yxpwZKWHzFWMI3T14d6NftTwSkNGKYtAF_RjQD1nc8EsE2nW4SKVB1yfh43fJapfIjRZU9QeDYF2kM4E8vIWVIv2cTQv8F6ZVFJ1XBQYTMRR0k0GnzqdykIiypSb6kGHDK7TxTROn6hySw_oSpGXrrjhjoOl55ON_P9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7u7gd37Gr7_mQdlozSAJYMy1LiS-Vbw87rNfU_fK5xY1x_m-gI2p2Aqa4wXY4-lM735C-FDHc7iUquhDjlHh-2gYWRZjmymBHU4-Qzyn7W7k3Vx9U4pjGAIgdHH63-lNtiM_z1jTci4NPkxpbjPxxQj5PPGoY4o-zWLN7wsvhBhf5gcEcmUHU_9Z4ToN9ioOxkovB-FlDnHkibemRj0OPjENGB0Q4zyhnapQpqpRvTodCTzAS3HX6Zq7KQGpSE5QYoV1KyXLb6Dy6FGzZGh-kbg2-bcflP8OJW9z0Qf2MZXFmSpxGCYKp7qQmfXk46lO4otkxshp9CfwONXyp5bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U30sZRWhBuntz6_aANhCF7YvPwq-YrBtR53kJvgkblBOd6chbLwohvZQ1M3ssuli3dlJeYsZCBsyMt7IEI9aEDb0lqvSsCcRhe5Lw3P0pxLdQrmjc4w4u9F8LnkS_CNULdldyjJrqk84o-yp4Els1l55UoqQWyUdHTGc5U_7JsfjcYdeIu-a4wPHQrEbwzhKHK45VBJ4I_JevJvDjP_hr6z7jr5UVp4MWilZt01FwMONIbBNeb5Nc8fxGexsY8Pt7umw1a_izkQQy2-tDgzLRbgjO6-O3xLfLSMEHhR0c34lHcP0oszXsnqPf0cKX4GjdNeCAmDSmN21jkzD7Z0AuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp3IZm1dr6BSrLE3Eg0I5a3HHg8yEV11G8RzOqgCCyfU3SuXhEQx8gI9MxyxzKuIEKN9cRex0X_ggowimpuez6jpBlrqoaGrwbXOWCk9Jp59E96ClM-1GSsANuxw0K6K_XZLBG4wflMjF9sxnIHIe_Nsgjib5ZGLxcuTa5BmP74gG_7tDKOnXhHWJ6vMOqnYVOw2n8PzctSxnyT1HEq-n7z8-VcSn8cl_omuoKkHrOGDgf23GgQ5JW7A3N96lIvEVE_hz3jR9Fz2LUoj9gJ9x5tiVad1tl30ZTwVrhUgOtUMdJOE8UdK2NedhZ61DQIGJaRdcf0LBNueIYC1R66Ypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07alxCCNcZJN9rmoj-rZu5xNSX0ST-N6EA73SOlGC75MNp2lCQF6zGuiwGWgQvOy_8SxgHbywaaB5poZGXO7Wt586Jpqmycd5FBddBuCK9desdTzwTIaNEV_7tamrIwp2Yz8uxH84Iwb8lsmVk4A71sHnBk2TXXVTA0J72x5FqoAX5L6gPMDQFF8lRhZDfHv_G-MtN6lAozHAyQ775vl7CBw1SAaNgWD205INNKLqqrtY5S07u9XXCxYl4-n4F17WSdN2SyNZpYjgFQFeqwwsC5BO-mzs9gGrOApKkp5WUHyW4zm4RLOFxU8MnzA_dyuAi0ghcGUuRf2cVwLsGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEZQhiYyWCJ-BZDBLxHmdbx0q0llciqMiVOcBqb8n4wAnnFl5c6vmYyMbYIlVLSU-GVaFszADZbwhlP4pIUIf3uN7QOVrMQ7fvui3pWuIsIeq_A6kbW55YsBvfapaff3xGYptT0JohLXgXqYTLJBtZrxQxtfUoLYXuuZzyjk-W-kZ9q5_mhJ34Nh6ORB3MfR3cW9hsORo4EoM7g80QXckaSPd-diyIQNTseUqAvuIi3ncZHGJso8RSwlYz32qwhGx2sc4V1sp5vt7iamYCbIOmR3TgVxm2KTgEBWrI8E7k_XR33VTw65Uc_WcBGirIa1q7ww6mHZGxBB4VF4yNHY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ha7OS2KlFZroTBZGnX6Sv7J4u63jvOfkbHqeED9w4dUuFARLOk_08bRFF-_hqSbojc0NyeVk0-1ZzcFJvzGIL2zwHjHDeqrYkFJxRGAinB1nXxe_c3TRCgNlythpBEuZTYXWGIhVALRy3ChSbS_3JvOEtgOI5NS7j3atifL0aeu9sqgVP_thgxRJdINA6NhDPsZ3xn96tDGg3siqlw_PKHZDYQe2lAgys5rTZckFxsKCAwO5intYfeG864RJBgqt97yBDzuwKSlcn_V88QmZ9eDsipMeUEUjqd68pR36YKR3tZfJGjcNt_jYb3itrwwgBCTLpf-rpOEQc6R1YtMpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRveGuJAYYIyz7SgHCh_fEUSEi48v7dNhmK5T_8uFFwnH2a8PGkPYSdNwxdlu4DPeSypYfulMlQIMC731JQBbxSRjGTUSHOuAl5oq-b2xUYXbZR3ZxYAcxKmJs1NNXOsNonwvaothmVKmwYSEQWtb87Opl8AyRQJvm7UihrX1IKyU4RZIIkxg1mxAozqXqAEL7k4GHfSjWv0FT6zmgLUKfqVCX0AbIbHckpTzPztOzJk6AxN3lRuVFCZ_8SjwSFVXQElx0g-wBCzri7ymeEFQOKhA3aRUw9oQswuDl7J41TE9yc_Mx-IWlanY0qCqhZCVw71txDaFkWvBxiQQk0BoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tinVGqESZWBJYTp_xngLmsWpWvXSWg9vYTDdbbU8VkPea8zpIDvxWoMJpiwTWTO13Sh2wt03pa38K6QPoRkiyJf4U8ybKfdTj5ACaMDS_cEDU_Wmok9_4jMh08l3r8oBLwaFLsgCK3O1KgkTvvBEIC7NtILafKNg11zvrAu4d_9ACr40efMvkUppRqtQIVGrXl4JSjdDnKxS79DL2Rbb6F6PVgC_l3pLB-XYpJflrAz9BGOXUVZ7VA0dFZidpkpTxxq8WWNshuSbHxcY4cL3u8_rFp_LGyGnZ2lhh-BuQgloXPv18NKATjP97EMt68tWvCl0LfA9Gjw6ycvA8o1P7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asodADQKSuthC6ZOFQIl51my_-YtT0__ObU-f3qm5mTL7M7kMqbGspHJcS9z7m5jaoExT6HJ_5CHBznW1OYPiteZvOdbjyv2iMLpqKmKePbrTmib5Go5s-zmrzmkak9WbV8s4jT7xUUfKW6gVzTw834PXvs8f7SqQsMzEvLCOhdXnLa9nECAdkviGKWWwL4JD4cIm9KkBfGsp6QOtq0HiBgxX4KKOBqEynxhoGmsD2vz_TYUyROjVMCpgwy4_xkWxlDamZDNg-x1KqgIUtXwop_YvfPEbtGO03AuMERCsbf1C8BuWPVGk5IQank3Dxl9XuDkSqbBHIJimOb8ofbkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=vjoERIqz2d6_JrCyla83I7OOf0nP4lzPy4Ywgw-HUok9-_p6v_eS0TgNcPWd_Kin-oHOUcHQN3ZISgTohSyQj6kIpm4udTJZfc01tjYJWdMCNNNuzkeXlh3xBbvIQGXiNE89TWcIpmAPZE1ucRavX8ZUaV-uoEGlrGpdkYy5nD6iqaAL95PMGXU1MB18Lde9kzCHT0sb6aCPn1GF3r0D_JMqBXexVoLihtTPAIOJddPg02-vnkSPBTJ7uTj0VMGAD96PTgbAV4p8F9ZrQTplLaM2QJJdBXrbdWu1GU0s2aV3xgY754lVe9O9ulWrO0OXzLtYvy4Y6NAgHW6u0JxDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=vjoERIqz2d6_JrCyla83I7OOf0nP4lzPy4Ywgw-HUok9-_p6v_eS0TgNcPWd_Kin-oHOUcHQN3ZISgTohSyQj6kIpm4udTJZfc01tjYJWdMCNNNuzkeXlh3xBbvIQGXiNE89TWcIpmAPZE1ucRavX8ZUaV-uoEGlrGpdkYy5nD6iqaAL95PMGXU1MB18Lde9kzCHT0sb6aCPn1GF3r0D_JMqBXexVoLihtTPAIOJddPg02-vnkSPBTJ7uTj0VMGAD96PTgbAV4p8F9ZrQTplLaM2QJJdBXrbdWu1GU0s2aV3xgY754lVe9O9ulWrO0OXzLtYvy4Y6NAgHW6u0JxDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=gPjKyrofpdESb5zwzFqMvbkXd1VBqV7IF0TQv4aq9QSQ1UVnLKgJqF78g_VLYLXVexPDQvbrv4Z-1jYASGYctnJuw8EsolmALI4O0Ss03fMkJESJw4Qq805fBpG_s75499_nKkPEWYZoQRNlt7jqMlXlKp4ehLKeODW4OqQ9q0O1TrYvzBPrN2u0IpffIrZF9e0ObZGCIorrdK_n0xhAHiB88ygnbAkDHBaNj6N7XgtcvnFlvzT2X_W0zesVn-HSISYZMbOSv8ScLuGLnDEuuSoWu5jezBZJFdXjrtMGVjU_HZ1liHqD1mOgbKNb4-xAdIQTWPBdd4_0XQKaKwu5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=gPjKyrofpdESb5zwzFqMvbkXd1VBqV7IF0TQv4aq9QSQ1UVnLKgJqF78g_VLYLXVexPDQvbrv4Z-1jYASGYctnJuw8EsolmALI4O0Ss03fMkJESJw4Qq805fBpG_s75499_nKkPEWYZoQRNlt7jqMlXlKp4ehLKeODW4OqQ9q0O1TrYvzBPrN2u0IpffIrZF9e0ObZGCIorrdK_n0xhAHiB88ygnbAkDHBaNj6N7XgtcvnFlvzT2X_W0zesVn-HSISYZMbOSv8ScLuGLnDEuuSoWu5jezBZJFdXjrtMGVjU_HZ1liHqD1mOgbKNb4-xAdIQTWPBdd4_0XQKaKwu5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=khzpYxA_N5Y_W76vXY2HKDtfqCTGlxNsKCHxpPw0FagZY0Rs7xpHVzFfZtAcMD--HpqO_U-EmJ876_u1WWhA0SwoDTRqzZcZMZ8FnSi2BpVDrmg2XJvcENCYXpyzFMAX3PKgEyvWKr0wZjDdZLotJKkHJXuY9oy7CPhJLLkAnvqbdf9Ma3KCrbEtkLb1l2kjWa1O3Jcz1XNHMnS0JThU93ZzZdAOnW4cSx4FZhgBRDi_cECLeseR24SHnv3mCahMUyQzGFfx67PTdfdzmHRq4UrXf4zHcMAELSpSjoYrB2C_Il3jyIjTLj3AGL91T-Jb8hZ21foQ-hT5gWM1SNcenqZMbiHcKdYJWkwY-XoVUvjr5-qPtnBG7htX0E68ID055zPwzAAv1tbdHkD6Is5rdA357bF9N-Rgo_TMUXk-jno6TwoQwYDuz8IMqy7DUwGzsYAGU6onYjdokL7jZGSo-neFU__PVnKm6tJIycdsdioasQGy4dMLDEMezSfPV4mlp1XtzBvumcqcKb7BYWEe3TBMZH68q0q_rijDt-LTWC7-60MfjBvClaMaYd_NKWmLQztEzC8B0jAyEjPJ14RpmB3Tr98gYUIxNqMsAzKz7up1oq1Ib2fhzpthrWvBWLaCA7LKOQCG2dcjl9LTfp4G1bjMr3Xsm-GyZej980h4gNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=khzpYxA_N5Y_W76vXY2HKDtfqCTGlxNsKCHxpPw0FagZY0Rs7xpHVzFfZtAcMD--HpqO_U-EmJ876_u1WWhA0SwoDTRqzZcZMZ8FnSi2BpVDrmg2XJvcENCYXpyzFMAX3PKgEyvWKr0wZjDdZLotJKkHJXuY9oy7CPhJLLkAnvqbdf9Ma3KCrbEtkLb1l2kjWa1O3Jcz1XNHMnS0JThU93ZzZdAOnW4cSx4FZhgBRDi_cECLeseR24SHnv3mCahMUyQzGFfx67PTdfdzmHRq4UrXf4zHcMAELSpSjoYrB2C_Il3jyIjTLj3AGL91T-Jb8hZ21foQ-hT5gWM1SNcenqZMbiHcKdYJWkwY-XoVUvjr5-qPtnBG7htX0E68ID055zPwzAAv1tbdHkD6Is5rdA357bF9N-Rgo_TMUXk-jno6TwoQwYDuz8IMqy7DUwGzsYAGU6onYjdokL7jZGSo-neFU__PVnKm6tJIycdsdioasQGy4dMLDEMezSfPV4mlp1XtzBvumcqcKb7BYWEe3TBMZH68q0q_rijDt-LTWC7-60MfjBvClaMaYd_NKWmLQztEzC8B0jAyEjPJ14RpmB3Tr98gYUIxNqMsAzKz7up1oq1Ib2fhzpthrWvBWLaCA7LKOQCG2dcjl9LTfp4G1bjMr3Xsm-GyZej980h4gNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV6BWcl3FdAitrnNCNqnH730wGrJdvWNhONZi9BJUytVnWZtOBYlHSj6LlVYRMaf11LBbhvrH3HX502DI55Cad_CknWSoTlC53lamXtHhqB5FsBaCtJv0U9xi1VCy_bJ_n6GaSShw4m89v_27axVt2jH5KXKd0g3ClUjYv-F6INJYtoqwvX4qDFNpkDnIETNcZBHIdKWDdvgrLKz6b4ENbz7Ksr80L6d6RMJH65wp2EnovUCz6QszsCdn7s2kxGAa0ukJZ76Og0dT_GUbWxgCrWtDRy__yBIkP20quOE6vfZqtGhNXF98AbLamf34jOo5CD5pvQhs7LqCQ1zBCnR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=tkqo0DxqZy0L1DUibg3pWonWxzDxFDwKtwOvlYetfn8Byo3ZtUXmwzhxELqNS43A7wVooIYu3O6IjFtdKN_mUN-ShLC-SnH_kW7LObwh8MOva_net4MoG_qiuRi8sApHohS7aqWwqXzf_647U4eHdkvFwKlJLcxwtReDda7gOynZI6oe8QFvSOHLYMU6D43gdqNcCUYjq1yPausR-BwS5Hogtpb7DadJwB7yrV5vxaH2zTEL2VhxlzMvU_talxd0C1TKlibLhL9OYNWyUDZSnW4sthYGlVskIusu-OK3znf8Zl-yhuyCIzWKvlO3LWrm7wkSy6GRpx5-sSmPZ1f4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=tkqo0DxqZy0L1DUibg3pWonWxzDxFDwKtwOvlYetfn8Byo3ZtUXmwzhxELqNS43A7wVooIYu3O6IjFtdKN_mUN-ShLC-SnH_kW7LObwh8MOva_net4MoG_qiuRi8sApHohS7aqWwqXzf_647U4eHdkvFwKlJLcxwtReDda7gOynZI6oe8QFvSOHLYMU6D43gdqNcCUYjq1yPausR-BwS5Hogtpb7DadJwB7yrV5vxaH2zTEL2VhxlzMvU_talxd0C1TKlibLhL9OYNWyUDZSnW4sthYGlVskIusu-OK3znf8Zl-yhuyCIzWKvlO3LWrm7wkSy6GRpx5-sSmPZ1f4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ni7jkDxbhqssnliy7tMsPd9gU1ELZUicVzAlhskqLKmbaxUTeRpf-y6JEGKvU_mt_DrqCLWyRpgtg0CyEp1ySdVnDnvh4lSSyaxhHOVCx4Qpq8fUu7YYfvSfAn0dMBqIno5mPwsP4vWS284K75cUGiw6kdAx6IBjO-08hkOuPtIdm0SyCzQLS_gynFpWnYwuiuR0hTq--7bLlzkF1D5oq_QW2R66_sLH9DOh-ix9NEoVZzz-vpkK5jl-OReVzopv7XueS9aAYZQrGtdj_KBiR8fPpCFmY1nQjYuGe_kdsmn8nIkjwlJxdu-8nxG6EZgNuuP4HG1fXOgLKRqyz1p8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GD-TOoC2eUAQpN2wdbYPl2vWP6GA2deDAWZCKKOdtkqs-lHf02JcmqcTp_Cwzku0qkBb-f0BMN9YPt6kibTuFc7cohrlhO8rFkw_tbWPG6Cy2wVm2ZrMg3mdNWMgZm2fIjNXxt7pCc-TyZ-0bLhc2rTiaesLOEE6bYqiafFLU_Xx5QxbXbHGlgajOrF0ysWJJxOSuTckOOc1jdg9NzB5invR7mOVvfSw1KhABQ9LhxL0MsSBOCQE4joxjcsVRlaIckiPaaoA1WwQDipkXZdXsYEX-S76J4OF4X2mMihWM1j_WqdZKk5hAKfFa4hBpjxJnKiaGMgJpsVTimZ17POQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDPRe1YNB96Y0euDwVWJ2AS7L-EcLZCe-1BbRugpsYECYSoLikBb7tT5LTxz9QKy4r3_Y0VJRqVPcjq6btpkAMG-oA4yLGfS4WzpJBn6Avd73pjGsP6hr7XwJGCNJPjX_N-dc_SHfyJkqRvJJ1zfurtk_hHGAYZaKAvD1uuon3KWifjosNyIgggjK_bKICkSz_akhrcDJwa9vWNDmFEAORQc3sHCGlLT37iHqMTOYQtPGirhkDXKf-f2zOn_GoFRbbMmrNLVyGyEzqn6ljoxPRXBfKgG6615hRE3TYx6wiHGA_Nk36W6a17_PxlWJDxSAfvC1OVFOr5DnlT0HfuywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLCYVodOw0fJQYTDDQoWzKfw7P_PNesa2fzx0jTzORp0D6ggmPo2oiacQgomD-S-LKJz5RzWVyNQoYwtXKAXiq7WFf8mh9I-QvliII-znfrrN_B_-U75Lok3IB9MnRDDIamsxzoKcu7At8ixoM0hhxT4LS6NfWNBCAkC4UFk_PBfxEGNkld1L08MfPPSUoKdj3VrmlymyBmennufDbt3Ce0NweJCa_5gZT57-dXmvzOvBIaIHGBdy3wNXdtKY7nh_J_SV86stIrOHNwlAyV1vuj8-azMYx9F75smV9R68WlYdFh6wTK86VBNwcRafzCsQSUsD2vriSmr4-1lsNoM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ub6KtfYF3x-sa4MhUJW1l3jcqTGIKhvA68K8QascbSU9SCZ4kJ3fADI1HFGxpC-EzLOKd0q1-_KG15TG-Hz2YqEChSv6qNCzH5Cm8qOUpn1CuinipOpbue4gUHZLjEOoQwRHl3S6vcxK0WUtaR9655R4i9LIS-L8q3RB0pxeOidYtb0QODMIxLOwI4RN76t1JjJgp29H3KIZis0Y8xhq8pgT7P40DcZb3MOXUnU5-osn6uhDa62djCDaAKPFb0thtQnzw0kGnF3ADlwpYUIND1ARPQNpKT4DVKSRf6hWs3L9XYIoFDTbxblaO0BgcHbXeBup-lFuOkT6mSxO1qTHOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOFspGXU2KKrrwXop0yaRiWNFM-aw6wwknod7AGac7AMz7KFs4cCNB8hUf3FWcNDDti9YME1OmS5iZHLz5WxyNTR9kZ3k9n-M3b0IKYYxzjPdfVHdbMrZ4gjLdUKOMZbboDsUNkfO91_bqW9yq2fUJIdNQJAu16V1x7Ckkr8P22-wktTzgSZFKLf1b5JA2kes8mNG9uuoUCZ0AJeINAWjxxmdsAJakk4mxh61clMel4lehzl6PdUcXdqyalXjzaT-VfPWSHZyFmJ91mpvPKaF_FKPy1ssLCwL9TMEPh3kvHOb5WzEdAU9CjCsr6hU9_39NMFrOboTCFUyTfXht7F2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4q61Pq4ThP90tKDaEm8Q6f0ye259YW5j-eokeYKWy1Momhxu3VVOOkUqdUVWLR1UFI_eCd_RFfYs5dts7cVQb54dv8OxWizfKcLygaBcsaCD5b_nBEujuifsWKPz3XidNKBZz8GNnvyxJ2nfTGYaRF1ymwwooRiIZq54dp-tTLmylUjK9ac1dPX4cqGveHsQGnMNOTxo5Tm3QkIAsXPxW3EShOpUsqcGmdf4uN8IGxj78T2dKWfqDIpy5sn3hWczi8bORx2VnmBSVmmxn8FE-FiYXbdj-ei1vZO120utYFdx2hE34QGp2bl1u0hzjuIC5hO25ILplOa5i9rm0bykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEAgjMAcUkp-QSRyU4fyHTi89Cghv3jZKLuOEEVJTHS3GqjXgkZhPxgMvi-TfxCmMD5s-gL4vdFOmdthxxLtH3SiOYujPe8S8PW4UmEiDHDlwiK1qwO3hJ3FbKLCGN1F6-8e7D-5hbI3E483d_G6Tr9c-8ucFBZw5DbGsSNRVqO3tVEA_nIPEQ9ABvhIDy-U5w91p7zLt43fBoXoTrr8z7zGCtIppkwcEnf-XBODFxDjvrG9YIjRUKo22Zf03CRop1xpxEcju81xgsZ1MAknxssroeeQjeEOToyQoP1Z_h5FAyuE6-2JZ4nx_Xue8hoajOfAZN356D3oZxLUAsV4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPI51ZeOhOcTotvrp8aQuro-epTt2gjNFM7clX_X7uDQ14lzpRpTcTbmzOG5-5NRvJC6-RDHqeEDf42dfjjMNzHh0hsB6MYP_V2nBTYY0hWVTi4vgThJQyQx6kl7Ob_0Wq4krfP5Pk5ojtXQYLuIc6X3l2adk7gJZyQ1dcwJ-9iumOBvgfuB-meqSJ4siSxuP44qVOhluEDSrU9oZWUwssufGw4m4zkcAMevGHSrxUW54EczfAH3pzqJKx2mjGI0OuvHuK0v9GBEVWJC7sY1xdg0Gvwdk0BXKKSqFmkaEbDSeSLbganrtUaEBlhvVaOGeJOrDFdZC4E4g0HKKLehxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQ-m-W_n-yNoxliXI3m92DVqZwFG59GJBtp0z2IANqgibQBX6CwEABmApFHaMpSK8escBakG6qI9CixXT95h_BntWCI99z9AFUyVeqc25y5du_HojJsu02aD4RvmhHq9cEFGssZuKeD-LTFMye_3JBdoH541vSfx1UH_A1sG_LX__FASA7vtSqT-dkH5qEr5Nw3gziGHw6HFa2BdC8eB9_-P9kp8KwlWtvYCIlTQ5pdofIheMkeGIaeIEwLRIeK5jRZLMa8u6udJO4n90R6Ik2qdZ9twrM0vsN5XvcS-NTD5JVvJm4VzC1oCQ6DcEkmmN1ZtbRZt8zC56aMQeSBOgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m17twMXYPUgsXR58jvwOu-MrtLafZA-BxOF-k2Xxk-sNM-TNwzeuhAqZ3oGPUboQi6-LP6_TxEu5mGYntNPg1cNZSG8Bbee3YP8fr69HBeGEIKAjMfCBfbvx_fwaQVZP8n_k2dIkX0R13PidiK05qSzCUUkWqT1CXEwaTbTmgul0o8d9fyALevhbzl2QNR7wrnEsyAbfe04sol4Ul_pE2qOs-S9mtJbU1QmRl_Cr7Hk4Sp3mt7fbFb24zN994DXd7yiaFnFsObfxoSkOzWijl5ZtK54lajGrmKjO--ysbJcgS96BzdIk5pQtzpvHYOP89UUVwknV_JUL1hXZTi4oVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURKSrRv7Zg4uLWSXFAzZHFvjf7IhYa56BMyFq7tf6DGUVZoJ3qq7PR5fza4csUf4yTzAzkrvhaaH2JG7C0XzWVh7hC4eB0hSC_w-xxDD6SVWzxf_ULhCBE0XypxPezsIKJYdSHufq-y5xQFo9T76cxSMqajGAn_l4G4S7EF0BEhlkwirSnWnn7jjcPNA4RCCg3Cvz886th5y_XfFifJFrmQA0Kju1wkRIrt1XZNTW_jchnX2Dx2B0BpPj3IV_FFsrneF7z4ndSCknlIT7EPVJgSGDCzssrMNR-93SBha5FjfXlDMoyPpyz1VjeZnomTba9khNaGiUTRba6qU9BJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sv1ErF4uZFxzUm6KirQ5suuUZ-mXdr3OrJLb8QQrZdWunLOmu7I2USfzxov3j9MKbK9rGapKnf6Jds_7UNLXZJvrk5Yt8PYb2wRiUpzZp4OUbQIR21ZJxw0VISkbkJUw9pGExEmYjAul65JkhFSQxJsfgffBQp6A6Q9DhZgNfmUBduC-ENhW1yknZvbvIJq_EozZcksbb6rARpCnZcxG4JWYNTvXGqiLuKI2l0QJe43XLbbk8lWSNbEMei3C8tCcYhiuI-mRQhRlsEupFZNxuR5K3o5pNPaWZB1arh_7lTnz-8sQxStSZ8HmywmHYsxlFx26SsJpcW1iRkR2KYAVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9foT-YizNwjxd8SRKKFuRLdcZhwehouchzQRYmH_1yxOhGw_ZVmXlRmQPKfnWP6BFao3nGwyhKzcIVKci1Zn7Z-D7w6SY5Atgqv_Sx6NwPRpuNNma7OGSkKXvwCoozGhrffVE0AM3Ig5VlwHfHEAL5P188IGHmcKn59WbySq1tJeX7cjPXHSTzFeiZOBveAsLrU211wpfHXBrlYeMRMgqZuYHFd3JuNLgNQZHMMXw9QLWOgnkLioWeldOpLM7cjx-VH-86sZJAxMR9RGA1HcUShImzwLQ8xNz9cTOEgPZXUkNOgkoXEEmrcCJEgY_xhV0s8sSIIDv-HSrmS1ELOqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ghue6tHDFS0QEWT6SyPiw7vzvhxIicKOThQAd_34LjZqJ5nRUSk2gcK2EZ4BafGPD01mgKNV0M5P4ORP2cS3kDUB8yJnXWwWF61lOyfk5sftrK-MGIHjpAK0dr0z3X8e1VOpZF1XVPtT8Iu3a2GUAtJcygt2T-4Y_3UUyAkLVewoxnQ4E1cV-pDxsNpBzOrhKKKAVR9Ov2JNg-JmlbXQCNwLPlL5XiklgMtrFCXHVtv_YROlrKh-PjtPYxUR2PWKgpw4nKQWm9AWGj0-wtQtpXh4K7ITsuTtaT4G62bSF67zomOXV4JN3NKJ6EiztztDylkHUncm_NtHwCg_FKVdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttsu6CVZnZBJ4qJ-aEE4FltDSlwKKFiqy1q7akvlKgUBJW5TJGO5_gh71wOpx-x54Zv538Dyq4sCyoXNc6TfSiRTvXpGUguWI59yLh20BSLZdehrtvvPZtmG3IpIQYJjILoYvPKQue32lCKKgUdZilBzOiT6Vb-uwqedR6Z4RZ-yJKxJ9W6F4B8nknfEidwnqyLtZBocuOasVB0P5S_zp0ebpWjPyE6fzbhB7Vq-cfaPpX62OoOx1_IWo--EFdw3wUD4gTBLeboWYyH0_xlaW5uSCinx58dUc7YD88RB4UCXXC05vgvlM5cKfGfDJHAztSQKlBRIll3FnWnbB9rY2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU2HQoxv9SuvGnuhfmKOCTrrHLnj0hzJPI82ON-PMkQ2KxvN_VaE2GLcD_aKwxuTBvkdZnTf2vqmzieNrK-O45MPcqimIo705vXzUjXgxEaBG1fnK3sBqPlovDIpzELFv7FveNRX-shRST0RZ9s5NlXM_wKwrcWJCzIyRwF-7rKm3G6pAXdoYkJMJuM93sO2FfzqSZbRkj9hgqqeImHukI0BNijca14a0Jp4IKPkP0lR0NFL1Vr5ciedpMxWbXzAXX6NXtvJxpaM-Yg6vVbQWy7iGR_0FWO2NZNWPaynQb7Bu645iqZ8tLKHESioLuI80edIsUzlMWQubbF6_XYijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=XXcVqeFoVILnF3xOLw79qHnoh1_H6LwIjRWwNC4lHsFlt3Oh2rI1hDyw_c1wmyPENO8CgNOZgLFps1ErC9c-oDk2x0J4PJKUZjj5zSwcFUgyoGCcVBcz48ENkjV-aOzZJ-5EU6O8RZlVsCQvgrirKozxNTCIuTslx_dRvnWaN3CnKinbYGbuaTEWtAFhnBP-Pzc_4CGMnpDBkjAjp-Lljyd9QUZpLh7mOR0K2t35Kwz9h8ZqYL0jB7e5CHT9PK7VNEsh5HFnJhqN0C7Cy3oJPwLIP4a7KUGo7l6PvT0BpEmPGpVv7B32vnb-dGrD2oxnlj_muN7nJxru9dnGpVAYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=XXcVqeFoVILnF3xOLw79qHnoh1_H6LwIjRWwNC4lHsFlt3Oh2rI1hDyw_c1wmyPENO8CgNOZgLFps1ErC9c-oDk2x0J4PJKUZjj5zSwcFUgyoGCcVBcz48ENkjV-aOzZJ-5EU6O8RZlVsCQvgrirKozxNTCIuTslx_dRvnWaN3CnKinbYGbuaTEWtAFhnBP-Pzc_4CGMnpDBkjAjp-Lljyd9QUZpLh7mOR0K2t35Kwz9h8ZqYL0jB7e5CHT9PK7VNEsh5HFnJhqN0C7Cy3oJPwLIP4a7KUGo7l6PvT0BpEmPGpVv7B32vnb-dGrD2oxnlj_muN7nJxru9dnGpVAYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qx4lRRhG-oIR-0bWdaVvSA_GXJBpIfszcGufIaRnOHvYJdRXdFRxja6ExO6ZAWq7xPJOVweVO3Dn_yKqZg2KE4GhHtjnqCUu_cX0P9_A5L7Pe_eIXw-tD21mFQZIxwS3mDOfiB5xooS3UgIENp0ip8RgtWfIcT5sp1AvhzisS4DMIFa1BWbTllU8p1aBXak1ZS9PajlHDnkzyi4SgRSEcBgAFX4EP4DQOlIE6n79N2MmNt0wLoMJMMvSEN6FfjANwwA7Hirdc4R7twhetNxGFGMxJ3a4Duy7PRRCx--DsVtGySbmdqWTgpI3O42gvGNQSkIMKpbVIDVbLbT1dwjb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqF6udl5F9Lsh_EBbAXaSeH-A3P3kQg2zF1Kznr4L2OFVc8rG9xwQVYEorO5oSroC3p6Iym_JUgcPSfXmMoIUboI5t8WP2jt7wKptz5vvbjQLHo-04xUfY3YCYiEX5gxrA363yiueLUDpzidr_ayT9sOa_W31LkguJkTaYV8LwaKg3dv1yQUrteTgxRk9O_uWU68KI2KSWHk0t8NFvk2UnBSLnH_A8yBWGBfZbRdDf6bS1qKE_38GOxyzMOaddIr2nQc0Gdrcp-p6e9fY0_4qwSPUtMEvzLITM7tRNoYX0QI8YQkzfjUvefzhEar50qRK2iG3Brvt4xSN_wTfTH-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
