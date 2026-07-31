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
<img src="https://cdn4.telesco.pe/file/pTnNNOoQhFAKJ-svZzj24VhS1yuHiUw0oZOZilKHSnJbdtdclPKIn_vnSoUjtCdzlTWUc_iVnQsFUY9e9geBRiUQM8cfXKJBFpgTu7TVQxzpGBPTyvllJgp4ACw35-t0-UIHAop_FyzwURNLVst76ki4oJ_aauZK6pnU3kTHqkEGuH6KWbTpycDesf7gi26hLSLxlpyRaV9c8aB5JiMM_A0rWwhrx10NoYg05FBv7iwItQwXhoCNgOmHCWEC2x15qX-NeLjvSSmaKBxrS9UU71fpzb_6qKmTvKoNE89pdfXDymB4UIEixgaJw1tJIorgiej84MMQOvs_lpHO4X1rYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 02:22:26</div>
<hr>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH8g2WkeR2Y3G9gu7FkdFG8XoveS6sXqKiAQCnZoQbe058dm_7y7IC4PXkWu_0mj5U5WewCgWM5muyIRQWuoWuPjXyzziS9TeazGG1lFiboOOUNq08-xxKyEbVAkkTpSA9XnV74zcv1YnSIpYydZRMbD4x9vUkksgFll38pRNlQH54NpDeIhtfwkK0r_QqZ4f9dzEaF9E7R6fsM9Hk8BDr0s3gVbIOSvMQgDkKNSxHpFxlgylKMMyZsbx8nqndFI17v2Rxttn4bDRXGlmb9eBr7H5PaL_ugajw-UF51qAZuu1tqeL4T2k70kwjJTi9GlSqdmtwSmolenYorn3ALJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjOPiJkM5-EEDM6Bj7OV6FYwa6uuVXOBiL-mXDklkcvICj9qBgt2UZtADLR8kiyyeOHfyQcn0FfLZdo9ahC6WTCE0Gy3eF6J_AGRCc6jpnP73GoufsqCZZNizMdGkZTUO49khBUxM4Y6TBU2vIOrdghJElvyZEl5IEKOaMh7yuWN69SA0jg0l0idBUPSC9aBI8wPpcNuXekSRjEz7Jvd8TkQdToAqfOjoCcsa8Qgze6YuKR176p9Qk2dAQHVGpE4zzljhITcIpBkHsGB0OiIhUdx0VZqTRhxzBzphO0T1rgW6byolugK1p47bRTt68SFGrPMKK28I-AJjm0aM8p2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIQTM80iQK69zWeK1zv2hRR6NfL3wncov7BnLo3ze6n_keZzpyBK1vl5c4KapxAjE3O0y6vVlg8WgIA2uFu9ji5D8zywqX9ho0Kqvr_2fcYIHssdNypK6zYLRgiyV7lmBr5XMuduQIcUo85FnSXHKTF21c5j51idawfac2Bw0DCD44sZJZghFvZwzJqcrlEZlB_LW6QE5nHkDmtkH6fA2YqMQG5HTtD6v8ISDpmyT9QyyxsXk4wN47Lc-AqMHkeTwWzW9uARkCB7smN3iFsM1nEqy4MCf1aMQk7sSZ1R7i_DyDjHRlIHDFXBPsmRuiUmnO9GAaYzkOS1EObA5m8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5SNeWkjycX6gsJJwtvo20Mpl26SZZjX19Gi5my1d3P89yGGHjNGX5Nb7B9HX3xHy1hSjl1LHA2YguAot4MmdK9Iqc2jXoJdEQJuGH_hl_a6SzgMO_5Q2_Q4ueCYlF9SWiYxniCXq7mimIN5jvMhQL8V-LgiZPrRMmFrwC7D8xQOkAVJ_jbDkFDgbJGLV3-I9-I58jLC6-5e9E65UTRvfMOvsufXjtX96ST-BYDKr1xk33PWoaF0-KoIJbmhf3vHtfYb8KpmjX4H60z4_JGadulFYnxuXRxALiwZYDfx2YkROe3M9MjCs44ByzEDodPV_Qn10wxXaVt0y3ID6TVyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dbeuUShWM30A_kcihgPofaUCtPNvenAZqq6Y6HkEQ0PEo-xt4qg281D3PmxKVo0S6c3h5XGhG8roFn54Osm0dfLCMx1fNM_hRpo24dJrmZdIImiAVEEGl2n1Asn5OaWQtL_Rx9fHVJ62o0Ml6hs2t0NcQ9RKKXIvTPQb0bWDzKZrxFtDLuS32HRey8R35BESCXF8ZoIJfE22sRsn0N0te6LMPVJ3KwEZUFjyPtTkcI0P0XQiZwGOt24oXXc8qmz5oRQy2tH3uLEON-I7dvVbMOtYa3HajQA_2JT-widb9tMdfT_g11s9psXz7OkHnf30w6WOZur8mdeCB97sDhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zeHLwcL_94UpOnVwHJeR-SjOVAwRNEQoorPnaFWQ1ohNkbzQK4p3iiQl9uEkdgpLe2LnBgv3grpS7bFiErOV3cDg5J7skPJ1Ki4uwUSIpNXd-N78Xy5XMWlb_a8QerRDqBcjhthQRFwffUFxCic89OYyk1zoGFsIXSMCqWdSsN0Z3LWgw5PWsPkrPTiFta-EksSqP8n5_uEJdZHT4kK57drrgogCbn0DMDAxQDxKE7wC3cItTpLv_N1J_jjecwzBtAtuuv3oxcuQ9rcVjp2y0oUeZUXqr88NGUkO_6atSFzTMtaiZB_ti_i1XeA0NO4YNHIzjrFR4kBNQDHyh7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5P76CyG4bVOYZoppovkF2x3KEB2a0Bm8ajKs3D4u0xTvsXMf4OYFfV8M49NvXT8IRKwANSh1ScxXHMGskLkujk2SYWBPtDpjAl46UvK4S6OGqAkva3ZEpS3CXjeC-0eeRqDuptKGmQMtplBiRMhwiQsMFKcUs2x2HNZDlMo9_W_qMjhKWuJuhLkms754rUBXzBsSDUNadQsSWxxtfC8x9dERl6p_eYSw6Z-mLIfXVrJkUEMp6j2RQzJjf28ojuskHK9vYH9r_WP4hQByAe_OxxpXnf1Se9jyYLQpR4bRv3un-h9NdgIAi28xGbzwzlkITL6IGlMWozSljuzOyEVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbjCfFse6t1YbjGml3SlfdHI1-j75JHeGDhn4CS_Sz-Rd--b5MZznij5rB4fQ4rEKfwImdBEWA-mRXcsH0yGj4aSfxDjXKmsln8BTxFIyRyf27zQwZMl5Phoen1u2BSs-VNlElHQzEHHRLuJqzEbHgJFBpglCiSpdMe3gbomE3CGpb1yXPwMsydJY8PR4jOBjywxPBDamF1tyPmULlV3w2BgKY54m-6EcAgSpIZ2NnxkQHMUws0yY5A-jGdlu1A3uzjBtvABiqALg-v8C9G-MZ_Sn4QaMV6CaiaelQ_J-JpPbTah2xg8Bp7h8loPSGRqbuEO7jK6KHPygUymChN3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHFuGJBOpZbh3Gx_oBKc-tUDoQXsA0ZLSZkxbWGHMhPd87k9SCr3Qrkhi2EjR7FLID9jPenqLFaKUEzyCc9g1UsB6lM4PjyLK901xekNoR5gH7ebIl8RbbdyrkJwMaFJqxQ9E8JxoueAOD9-FFze5ywEBLlV6qvNwgXkf2T2qKw_XVumJFxUKX6_87yiWeWYJLhjYNr_zG7JG6NRmHiqUsZT1tRG7SJzTPPORcTvgkBBVu-u5miosZ8QSrnwq1m2b5tkCKM0eNX1d2GfCHTRhvmaeYQoxX9_ASZsyH3OoN4oUOOwVmPLRgvfEBkeCTYErWs4skyCTLyvoU6uCZa61Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLtZZwZ8HffeJmG4QzAdrWvLgJYEhTAkpH3g_5s6drHJ0PthaJNs7IgHimDPZZRKomv3abA2WU1v2mvceHX4utNCo8mZ6ylI_c4kgYIEXSERUfpFpfpPJnOcsczlBLYL_LwsxYPOKDZESov9ZRzPOnaz0qSyc1ekv-QXCcIc3u7yl06e95SiO0qJqEt5nKFKVkKFPuz33TLOpnBlZ241WVRrZVvkPxnCU8nveErrSpF6ZXVrqGVYI-umeitz76AG_YDG0E_2VEHEs8VsoovjARX7liz6WvP06nTUfjTY2h7BV9ZadEwXiFTI46eGXsUR6UlP6Zk9O3at_b6Seq_YmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WrBkQ3bmdAphb1pWeZCGZTCiXlQcQG3_ru1gWq-paFvBOBo_eeNZ2qwCniEFfoz8jbBP33nSMjbuCNiryCwk-GDTo6U5N6vi7UgLHY0KhgtLQDJrZcPk5fxi7O0cd6mv7kYLS0uiQwJSXOQhcDvsMNvJeg_YWYDRyowPRh95M9XE23l-oxcOF94aR5o2ZJLhHDeCs1OU_wUqLZxCHsWXJNgIISi6A-OcXIoHZBP29BQR6NjzHFgC0JJ73r6xgKZfBbDZZfmix3Se3K6ZnPIdNeTbT3BDRlhLjBCymSx2U9Negie20egBHZqoPFgcbW5anCOh9f5ID-9Aww43QAHAO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WrBkQ3bmdAphb1pWeZCGZTCiXlQcQG3_ru1gWq-paFvBOBo_eeNZ2qwCniEFfoz8jbBP33nSMjbuCNiryCwk-GDTo6U5N6vi7UgLHY0KhgtLQDJrZcPk5fxi7O0cd6mv7kYLS0uiQwJSXOQhcDvsMNvJeg_YWYDRyowPRh95M9XE23l-oxcOF94aR5o2ZJLhHDeCs1OU_wUqLZxCHsWXJNgIISi6A-OcXIoHZBP29BQR6NjzHFgC0JJ73r6xgKZfBbDZZfmix3Se3K6ZnPIdNeTbT3BDRlhLjBCymSx2U9Negie20egBHZqoPFgcbW5anCOh9f5ID-9Aww43QAHAO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGfTNNvyU-H_T9dqwvde_iM0JiYB0ErByd11Kwq1JN0vBxM2wrbROGY57_6Iq3NRo7VfxfoT-3AD2MVoiW9rWFSd6tChNW9V30ahmfdsSWc1GQbNziq-FNc6sKXiDoAYzQ0ksWYK5fnDHlqGkcYmQhVAt94Ox6IimhRZgD7VZSwKtX08SaUeJhJF15Z2Y1bXkYv14IE3KYxhPfLLuj7AU-QZbvL8SqNY3SO4Hkni1sOFzAv-rgdWzS7CHi2x8MKxr75Uan5sHMmzcp0SHBsdEWZwaYZIkaVzY-ujcJqw44L8hQzILS3gmbjg6ZC-ov6PT4VI-s12t9tu2J3-eDyD_ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=RQ3oeNRfg3fO-sVuw7_mcNqYhGprWorwPpv-6NqSCbCUDb_XAEpXcGAGkAzPdrtBJjYkqQa22kTng9WnOef_Vsfz70OEzMYb36SuEZQhrs_jj_ALGNRtTJcOLQTel_NE4JlbpqtsLAp_4G1PwsJVvf1PT7IMpVXI9msNACFRLsc3JDHNFJ59PPfkocnD1niu49J-0JfKrWfAjG29rQAN7eQOe3XnDB7NdGOeTL5fVu0PqtFJrIw_jHIzISWgGeCkDM7Vq8r0LcKnJ5jK5EZo1dLCrZtM11fcmhF3OcGpe26Op9_cnLLnvazhOLbNSAm-WTFbOXq7SfijwxzSXEgFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQb0WwzYjRweE-0S6M9QEPC80olLjT8DTot_w-uWQrw-oUQ0TZPbLjq_UCH6jRhyuoiY-uXc_lIExDn3voLy2Wr2Eh7xLoaRo6TarPm8lHvh5sHGwdC8B3ENyptLU8gPtRFYbnkiN41PaU5cbe5f58jmkE9G14AVqaSRfc-fhjOj6R6QMo1XAvfJUnkLqiXLaqAwEe5kauTfFAk5z4wSDyxuImngvW8p5qR9ty3mguWG2UQGD0c0bpjH82S2pjsZKgV_HpCN7Nq4hfJ2FBSJYpqxPLIrVa-YtV0JKU0LUJOvYevhPrkMIj-XCJRoF5aXQ9GVz66gvvml4yOkZKkejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBw2WkkAo4b42MT0RjvgoKJgGk3GJEGi5GwCwG9gCedBvcCN1VT-5soDxBIqfRyNW4xinSVZUtJGuQZVyx-Q6TjpKRRaTVS62Uc0L3c4DHpggZQjmLdoMHP4q_JhjC5PLSQ2KrdCv8iZ__SC2PquMI7ye3a4BhZz_LU15bY_Y_5zjcqVFRTZniEYylhm-pcwWVbVjnn_74nZgJ1fuL3jEACPYWyhXNvXJDBDyVVNEPsmMKSsZbSREu5KIKPUp4cWmu8WcZQbEqkn8hd131TOkvrJoSu_H8_KtxjFEYEvOjsejOEQEkPcDSQxy1Sd7RENX5uuUrXbUBsDKG9RUOSNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=TCMsRRe5cXvivn5pVeYKX06n6TYliQvUX-E6yc3lsm-p04LkI8MQkAC5VkvAC7bGeVuHEDlx2aYDQqjDRAso5dQVjzDyTgFEOT_3nZJ7KE0Zq3Ty-4pO8DxNxGQip0YYMgmNg7EhG4MwReXlGzuAWjWr5ELXPuSQj_9xkv0YMxnNrx20O5gLrYH8ndUrxEZhvpE7CJ1hyW-2-OXqukSA2WxXtdmUF5nrel7X4QbR3LQ9_EQkhf0FLl2aAUqbcDsfnhgSQq_L2Me8uTKt4DcSLIZMYjFfiA4zuLB0y57c2gbvc7t95C5c0bRORg7I9dCuk2kDw_JUVB9gqGU6ik_hNhMhgaKvpV8-mgJH-_Bd06hSTktVn7EwEZImCQxepYfn3revcI43snyfqWne2M1-A2VOvHYwO00JCCpAahmSLT96cDf3yOP0HL8ijIw9rF-jZZOJ3rzRh3deQY28a8RMEc4gDeBh0nAXOdNYvS-9pw3_PgXOIc8Y67YYaYNzk0FBbBQxHe9mq8nPUd-n7QcO7Ryb9Wl2jcOmzOmxh822pkoIZhXvmx6ZlWXCSfaN_LUaPZHFpjcISlPiqU6Lmh8BHiU4B0s2km1fV1JX_fhtD8yTHoBWWHGq6ko7s19X0mlV0bhWj065J8z7ZSENZ5kool8nOElhbo3K20dtSvU3x4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=HAmrOIJQgcGps75U4nu4rfgZ3d3YqUMcl5cAOhHg9eoLUNLxGIbntHGo_K6OVP-DJgNXmK584lUct5YKmbRNYtSUwOMcdRckreLkCg-5ld-4CWIgPGCyDcMLRuD5RfrVLxlw-ux_crQYYLsVH3eOvF1I38TTq6a-CeBYB5pF62-X7mt4KUVRPEK9gFYPWNzetYdl9h_J2jCrPnSgh-gtSHYv63mRZMcUPWuCNTyA9dgfcGNyoO10Q-a_doN4xI7XVKKnccYjT4J5D0B4FvbL6Py2AcdwSb2qnBony8IX_P-l-9rzbZoM9uv3fApR6HwPYTrph6JhbAYKYzV7PryB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg_HQpB-C2Sqn-N9OPTYTqRlA2fKNMp1zAG5LbIteGMGtuo2-yhCRNqJJrUElO6ieyKnMu1o5R5WeLUQOC8I-hxAx_h-ujs9xgVX6cqsMJtPwTvyXvPLgoA_AAV6JXtYNdjjLH3aPba3V8zNGoWvbyUbUWja5ufFj2KWlr-LZUL33R8HWw8pfKfXR4fS0RifU09ZRj2I65dyd2hjxjC9BvgcG0fscalkGD6BvYUPtaSHe4Iuw9NOcWrOfjb7gEFVrFlVJERNmkIZqlBfXIxApNDb9hiElPdpzKjtXLSpZEUMJTsXnkuPKKJ8XzClc1Guntcn1_YMAWEN8JH3jBf_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYS7918eZSq7mxNZ4OU7P1CIwiUklikXEwgjH_Be7dSaj6hW3fAWVFfy_yXB8CeEXGrkGUGAF6r2zMOqWT0A8PfbW4fLtN1LnqJfxrn6rJbsyOdCE0BXUJzfidGclpr8jcOTrM9Cl9wn9xghzPtgdV6F1SL62srYbaRvVwGiD2jQkAH-7-anyfzJBQ9YZz6z19N2MBNmjSqsnsZKwjXBDBdZFQdHTI1fx7ZzcWa7r0VJmBKKX_jDvwI435qI1I2d6fIYkOS2l5XY_TrwaC-48iPVel8JxLm_efuX-Zk0m15bt-p7KDJqWcEDn2c_5kiusLuDU0Lmn7PGXCk3RJot3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v63i8QpCT5Jxhl8jef3L5SWDTNKt8Vu5xfiWQHKgKbiupDeCNGXIm5rOwDZQqhtVgZ-EYm068pET4dM8SsTwQwwK_CyUTbxHIH8SXs1mC5v2eeZypPXPdLuVeYCzF-jRYSTfVloP2yXapdb43EKKyeXv1QhSZ3gpnR_rXLxTbd3Pcvq8bJKAhpcR004RERn6PJqVYPvTF4zLwxNtZw2slHUQJhSrav_BkKpCUuKXMw0Ozbw6rQdLHbXVy3mUfA980ucOGgs7C1UP1dCm4dZZ_6Okb_mPdl88qQ2aB-7581SQFZ3Sz53tvhR2oHzmm1ELBN6DYFZOXfdICaivLHJ1GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=Q9IxZEvjz4hxdz1A6XEYa8iNAUhJ-19wCbBeIwa4J0THZ1sFN-FMBDD-Lc8bR35zX6JPWFVjsaympSmb5ADzIXKQhxSpA07SBazyqcPaQ24LCZOo5fx5UPcg5Vv6SL_wiF-Uir7xDrxLFWET-qCm19zgpBI_UBE_skfiqlUGvpRXz01tQuefm73XAC2uliC1sjdM9o9S9n4ui8gU8VBINFZVIPphsCJ5TQ5lqqbdb4_f_LsfDXG5Ye6pK28tM8HEIyV4hhwTEISTIjha-CEC3mfzfMFzS1h0WhW4f4dP2CmJ-GbyM2ASU8RIGjPWzlgnZMctJHtxOSPFwf3zVriIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=XPfSSc1Q3EddBzr9BNJ2g6e0DC9JuFTcVaK_QjstvAHxKPBhN6dvHmdJ6sFs8HgbSYVsCxj--wDhGty8HdhQlIDtLrmtKnPEVbtp4fd_mez_J3P3PGtL1nx46SpoPNzNojjZor39KK3ELC3awI3OrNAosxxUG6j8jBeKW3Ba-ofZLlJQq5-znsP37ytmWZgRxpsZy9mJGXnuudoES-3fQKtKbXYbrqF2HaV6Mq-82_G4HQoKdXQa-FtJZXgGrToRXj9vmMtTofugp-0dz8Qc2bZ1Pn-7EhXMXhnq3xBNHP6oHoN97GWucTyot2KVtylJgbUYUj5NbrlMjRVrs5UJj6gYtOE6in4mceHGlvL6af-rTHIwQhrZ51sX9ufGO-MIDT55rV3wtzlANW8gE_wHVWYascG-xY60YnMDgp_PPL2kzt6U5MC_h4hMY7Kfjad-Bdr3hgDNsWrfFPuT5sYRLaTLiD1ohHaQPIiltxKgttKqN99-MMSI2OPoz9phT0Hg7pcT6smYHl3gyfnxWxQgufPqVfi15G6HO7BUqG20Cnb8xuqfMkrKW2bG5UF-qdH3SgtPvwFE1guUbwJbK4OKYbcEVstAqI4Y9W8aRPUid8X-CCo1xdy8ACgeS8B-EpvNRefyTA13xo8yRTMcaK2fP6a5J_fTJRhKHS_YB1ruIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5BCBvEXAtLfs7_zV_DM911OMPvSCASknJy1ZjrsE0POBn_o2a7v13PLKOjULbcQF1t7imqyxfGqg5NxHINoSIyN9ZK2JW-iiNUVTIUl2yk4J6P-XRSR7qJMKvvwhrz7MRvPvoVOaUJ7ch0sQrLUkgDtApvFH9_256l9OSePL7YMOFHlzLRS1lzSJTi7YpV8Tla5Air0zRKfVhvMvQZGn0TkNwGJG9cZKI8v9DEA_41EDtHqc10VhMLhENwmugKpOAmx87VwAwglFlHy8XHPB92gjR8SKR6C6QP1KSf36TgaZIcR5blgGk0cnND0HLBDOoEQbql61hiO0GPMlMWlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quPqalXUpJZCWemVBAk-dP94sF0f49IYOoYFMp31Ejj60SmYGnaU4nffAmyn7naYzsHDNL9aN8oXqPn4kdQnT3uW3C665zxryH1dd7u6cbUZLyM689FZgCenN4rnZGkafZLQIBTkN2ordN6WwBWJW2XxwPbwjm2RIGALE7DwunjEjRWJPepX73VXS7gsjrqTZfTG8HGMEiYnX4kAVAYIatDDvLd7uN7MDCOXNeofJ6aU5fknNO2ucQNR7sxbdPCwSVNyyyyvW5WizeyU78DlBIIOuClh6uZUkJ2JiRvP_9UqGwGnWitf0tn8cR11UbyY5D7BcYO_GqU4rF4hCStp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BAebQLx34JmOJRHgX4_rRozqrOmH8KjiuU_uZu0QorzWO7Tr90stnCpZz1uYkP4B2X67FP9JMTIrti8IEmTqKQMSujA1NpGSARxS4b70UAJ-no2E6l5fEWYOQkv0hAsXfQ6ovHZgLLfRzsOwiBBBvUj1KIpIfXXbine37DEn5UQWxEcyEhk2QWDeBIjwjq1Wrt6DmuM37uA1gpmBU0AvZAftkxQ37QWWL3fzPCBFCG6eSQNh7_dOhXvBzHCaYWiqfmHgLQfszoClQDkNDDAyeStvFQmuB97T4deV7ZrCbFdZjkgoVh-HgImYjY72frs8sG6ogsEtkKMcb1ISSZC0Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=BAebQLx34JmOJRHgX4_rRozqrOmH8KjiuU_uZu0QorzWO7Tr90stnCpZz1uYkP4B2X67FP9JMTIrti8IEmTqKQMSujA1NpGSARxS4b70UAJ-no2E6l5fEWYOQkv0hAsXfQ6ovHZgLLfRzsOwiBBBvUj1KIpIfXXbine37DEn5UQWxEcyEhk2QWDeBIjwjq1Wrt6DmuM37uA1gpmBU0AvZAftkxQ37QWWL3fzPCBFCG6eSQNh7_dOhXvBzHCaYWiqfmHgLQfszoClQDkNDDAyeStvFQmuB97T4deV7ZrCbFdZjkgoVh-HgImYjY72frs8sG6ogsEtkKMcb1ISSZC0Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ouaz1mmy3_hFwQhAG-IEcRs3JwY9KDJd3Tv8JrRS6r6IINXiS7sdcKQMtaCZFXyGYLDDa0Xbaz_eJORSztNVUe4MwkjR61rhQgGd4zoQ5cFxtLleHrkroHwPBXP1-4DTvurjQS9Uc8kHRfTDt3v_xdvJTVj8r-YvEfIcZZGB8Pl4_OE5gIBWVeo2Rd0bJpVABOMRJr4AJ9wMZgNDK_y4OccsCuZvrykXVkgH4gNFFKLeuY1EeXpr-5g4tt-ZSbLeKX3M8NP29UvbRdYGK53mk0bLKnw7dfpv4QPK_sPeBmzCy_58uDuRORp1fPJyq2Xy2EB7U1NbJhD01RbNz6NCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2YcvLt25bgAvqSvW0ogfabWzS9wsUPvxd26CtM1IHbjnJN6j9YGY8Ngb5nAfofw-GC3NkkGRPWoSmu1J8h51dk8nchZYoLkDgy30nuDAXAeTPqWmY8KrXe-4fQ1r0h8t1OKNTDQSjCveypxVrSkP7MuXTxlfOtPm_uKocSiedJGuybFKe58lDBLmn3mogLTcWnyYykmVSW5slVutAJc6flGsBPK9-Buyz51LIYCyyVbGxr4sLTMm-i4eUZjmI7qZBXHC3mOka6fKzhQUFGgrIl-2HRNw6q2ZKLUXUNs2HDHADrCWzfmKDXSUOCWTUxNN-uxj3qAKamEhDLYjyKMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ1PJ39t66IgevEH93eOzAd5kfvXqsv3fH5q61IR8auOIySX7VyHV7rEwF525AIchTgucq854Pzmipae1FaZ7pfk0BpjEwJi-uANFtI1DMxHx1FN0kG_kE381F7bBJYgB41cWJWKXtPKOKtOh9mf2gAwWpKsl24RTRXlFZL9CsrBhPnotKcxpLxtiXCGN2cRbs_iQb7RN2tg1AHCtXz0JzeghdgD0Ke9UAvi7_rZTB-2bBfNBRFNv_AIzjE6cW3lW-lzo2YBhfQ38RrC1kq-CYbkqQZBwNDcKpqIsp0uG5tK4laPHmXerMmxqawvOAMU8FAaljKDPw3krf_HW59X_g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxrJHtBdeZxbmnQTLZRnLi9rvWJzCKEi2P2CVX0cU53nOt1FoUowCJ7xSPxMgL14VMDCZW7xmX2pHYRIIMBJxwXhq3CoEcGP7EfBiASCdtkOZGi9SWbTQHcG3Qiffc6CT6_s2G8qgmn0nb6gKyV0BttKe6y7O-gMOrUGvIjMHviy1tFR1xiAB0q0bkM3gm2hv6yYAWP2LE1uCEm13qaJ6-QUCX7blO4WGYRt0nMtkf0GTUXB7k4BZywBA4RSNk120L6vCuTvay0t4T52dBIzwgnNYxPKfKyJfhKdNITzSK6nHGRnW-dR-p-DBhRHLbdrWV6F_kZpolODJEwdqf5ASo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IxrJHtBdeZxbmnQTLZRnLi9rvWJzCKEi2P2CVX0cU53nOt1FoUowCJ7xSPxMgL14VMDCZW7xmX2pHYRIIMBJxwXhq3CoEcGP7EfBiASCdtkOZGi9SWbTQHcG3Qiffc6CT6_s2G8qgmn0nb6gKyV0BttKe6y7O-gMOrUGvIjMHviy1tFR1xiAB0q0bkM3gm2hv6yYAWP2LE1uCEm13qaJ6-QUCX7blO4WGYRt0nMtkf0GTUXB7k4BZywBA4RSNk120L6vCuTvay0t4T52dBIzwgnNYxPKfKyJfhKdNITzSK6nHGRnW-dR-p-DBhRHLbdrWV6F_kZpolODJEwdqf5ASo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0WIvYFd3URsle1CNU1K2NgUG3zq3Y9y8Y9rcymFimbpsoTQzCsnjvqTlLFfZFEeE7oJ3UIsniUh9-Tkpqs0fkBhOT2uUsZs-dZWwXcyqaL1bMqsI477MA-KcxUqsO69ae2SLY10lApSUMYtODzvzKVu6TF_LCniLeZebsEzpYqNM0sBg5ZYrrUCWM6mUXtazCdxI_q-5JnpmbOHtXQIGfre2PvzmHHHBB1WhL-LcxCEdOafxEOCFPC-xdspH-uZbrm3uFIm0m8dUhBwtt3kNIZe_VgMxrXSIY4QzHW02RtBnyO1Q7nNTXoibwbjIZ0tQ0b0KVFgH9IvVTGD5N2dRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYCZB7WKnpzGbYSW74EdTbq2X9xPJKBMFjZ9tvZIQJK92oPmN2MliAPUWOMd29HbJR3Sov7rj9yvRIpcv7hDuNmEFvp-M5w8gBAhGkMYvhuC2bvEYvlaR8YICk_P8edFQCfOwDzaSZS8wUI46__CujLyZ3wWwcnHTCmZjmKubCOwWDPpXOqR4sIWslqs2152ulYwZzDqLIEvQQgyESV-2Io06AAPCRhJW1syxybxqFxG2TOEplzZkv_QQPzlX8VEbbZe6fxZELolSv0W5GeYeg8agnIXZGt8Xd-FDCJUGzDFRkfhIZk5pBX6uEejYgBPTBXFLzJUlo_L7xz0Kp0hIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=gKWQeq-1gX5SDWocuruQMofPiiW99enQKOyp1tqqLdNHPnG8u6u7DaWhYFiIe_DB7jZTJWykENeZAhLWVNdBmsvWw3oaJgGuUqg4f_6QrilWhh5mP22dG23OrDYv9fEwXU-la6xvM9NYoXVHf0Kc5X4MkB-uS-18tnScVOHVcs3vdDzK6t4qp1S3Wdmf05muGe33-Zu3kGQGxalVno_N8-hKUXex8XTuiy3Vj2U0hhMO9Ko0PtsTBkQDDYVxsbARVVE45vtqfbjzDDYi5d7ulCI2yzf-q3MXUfi_MY6QLKvu-ClrjLwM-2SEABo8uU-8l-wuxAKdgHBNjaqqVY13gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=gKWQeq-1gX5SDWocuruQMofPiiW99enQKOyp1tqqLdNHPnG8u6u7DaWhYFiIe_DB7jZTJWykENeZAhLWVNdBmsvWw3oaJgGuUqg4f_6QrilWhh5mP22dG23OrDYv9fEwXU-la6xvM9NYoXVHf0Kc5X4MkB-uS-18tnScVOHVcs3vdDzK6t4qp1S3Wdmf05muGe33-Zu3kGQGxalVno_N8-hKUXex8XTuiy3Vj2U0hhMO9Ko0PtsTBkQDDYVxsbARVVE45vtqfbjzDDYi5d7ulCI2yzf-q3MXUfi_MY6QLKvu-ClrjLwM-2SEABo8uU-8l-wuxAKdgHBNjaqqVY13gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=c8GD7IB2dKYmVuI5vOaZBqr7wrQ69orfUuUBTPbllmo1SpFQ_DIDPCTGKJh4BGZk_vd90zSDd0-90SLYaqFAYHbE9hLANgBmQ5XtiKWWVnG845tQ0SeuhknZlvWMQTwmnsbECPnTAz4eYH0puslxkQK2-QtVGZRI3SGqEqU6nTNyyhKDynryAGF2J7GLaZb_tB2cD9yzcoTsPL9rUtL-uUGrN__IQ_1FVuRfZhv9QrO1vFWj-02suTGLjy-bM232rk7mzd1kTNupUp0VtlmU9l8865wEln_UyjzgGWuptCMCh9-O5Pm27YXXi1idYGSPRDeY9uzHqmSSxCCmvb1qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=c8GD7IB2dKYmVuI5vOaZBqr7wrQ69orfUuUBTPbllmo1SpFQ_DIDPCTGKJh4BGZk_vd90zSDd0-90SLYaqFAYHbE9hLANgBmQ5XtiKWWVnG845tQ0SeuhknZlvWMQTwmnsbECPnTAz4eYH0puslxkQK2-QtVGZRI3SGqEqU6nTNyyhKDynryAGF2J7GLaZb_tB2cD9yzcoTsPL9rUtL-uUGrN__IQ_1FVuRfZhv9QrO1vFWj-02suTGLjy-bM232rk7mzd1kTNupUp0VtlmU9l8865wEln_UyjzgGWuptCMCh9-O5Pm27YXXi1idYGSPRDeY9uzHqmSSxCCmvb1qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMfXVOoL8Tv_XglVlbzRaWXdgIo94zb0ib5t-cK9-MFv30IRaqBkgRR1Llj3qc5pEW8YxBHBmeqA1ZucVNqPu0cHIEwznJ5wnursfQe4p_MHwuFOrIZtzP_2OAN1k9FV7UKhYClzI9nyNGP76UZwYVsaj0RIZgOEVmhrsm8ypnUkeimhZS4TljJr4GY6kIFLyJ6eXz8CvI6dreP4Qtj7sd2Qitv0uQQUCM2B1MmD1WyVVyDmLC4WtkciIRHOXnwqdoYi_13_CcdQuL43NHl7kIDVHd7xMM6rZlv7Nd8LLO1u2DGvGoWSEF3n8dh2VWXUPYEpH2wwtQRo5_-2_TyRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id2MCPglJRVXY2rueI5cmNI6Y9KKXzaPJ5_4PzKJWTHWYXWyKmaExC8rMGDMypRv9Rwptn0PaETPNBjXIFNOOaXQ3Mm0ZIii3tLjcV9hud6gBMwcGgGT1FpAoI_Oulg6Vlo0celF52UujW6hWiJegmjR3wOkNRp1ASAfwXClmNPC_VVvu0IQ3bFZURVOKdLGaUWGeburo6mmaPZfGcWrUWY2Uo9wg8G6KYmQujcASMRL-36bXrHsvRnG3aCh5XI18rubXiMvciUULZsL438i8mZ_QhBkVzvJn0Nkv212YTwEzhcNo39xchv31jqsBj4_fRPGNTVLwnhP0kfXt30qBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=RNQSt_f8ARQCrY474adNjWEDABS2-QABjxHXAFrl5RaHF19TPt-pQB8R3AAZV2dZ4iRJM6TcB9D0KCv4SFyWNaLqv7k8Uxcm0ipWDYMR_HWbcYOX0v1bSttXAF5J4AdEr3KJSddPP1v2rhmVLrZtM0G8mpyDPGMVVLK1fEvTxP0uvTE1nk9oYqowLF9UKpFZT0f-Ph0T8Qar4zs5YMJZrYN_H65397wldjsiNx_i4lzC3b2IYCqM6Z2w4wv2hvC0X8N4yOEfIDDifUigOzLn3XavHk_wOMOaN1R-dsXgYCCLwwILSenD39tYuXq719qHVC4xCnZj-OxZR-sUuwGH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=RNQSt_f8ARQCrY474adNjWEDABS2-QABjxHXAFrl5RaHF19TPt-pQB8R3AAZV2dZ4iRJM6TcB9D0KCv4SFyWNaLqv7k8Uxcm0ipWDYMR_HWbcYOX0v1bSttXAF5J4AdEr3KJSddPP1v2rhmVLrZtM0G8mpyDPGMVVLK1fEvTxP0uvTE1nk9oYqowLF9UKpFZT0f-Ph0T8Qar4zs5YMJZrYN_H65397wldjsiNx_i4lzC3b2IYCqM6Z2w4wv2hvC0X8N4yOEfIDDifUigOzLn3XavHk_wOMOaN1R-dsXgYCCLwwILSenD39tYuXq719qHVC4xCnZj-OxZR-sUuwGH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=R4ebZv_fBbS0GiYxkhbYet7etDsIuMr2YFYc8ulgPZbzkBEtjbv0dQhC0hd-aVuK8BSfBT0860i9sZqy1DZEz5zjQBttPSwPQ4IHbATDirLs3RpEEC1QQKBlRnS6Rh7QUX7gdSFcIuEwcCoA2z_yNVoemA9srHE5XH6ey9nxXsJCHhSHmQcs-1eL0TFEK_Ecg2r3VCiE1HtD1Iv7OBCrWwnVAlvyMywpefhkwBO77_BokX8hhTh8ECtDDgJTtXQ8BSUUua7vyaDRxL08-XUBvPSLOEayTd9M8UT_eNqZGQadIVtj3-ekXeg0oHg5zna7-afqHklwHm_IURNv4PsB7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=R4ebZv_fBbS0GiYxkhbYet7etDsIuMr2YFYc8ulgPZbzkBEtjbv0dQhC0hd-aVuK8BSfBT0860i9sZqy1DZEz5zjQBttPSwPQ4IHbATDirLs3RpEEC1QQKBlRnS6Rh7QUX7gdSFcIuEwcCoA2z_yNVoemA9srHE5XH6ey9nxXsJCHhSHmQcs-1eL0TFEK_Ecg2r3VCiE1HtD1Iv7OBCrWwnVAlvyMywpefhkwBO77_BokX8hhTh8ECtDDgJTtXQ8BSUUua7vyaDRxL08-XUBvPSLOEayTd9M8UT_eNqZGQadIVtj3-ekXeg0oHg5zna7-afqHklwHm_IURNv4PsB7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdltlBt9Pb72XoWOn2YgM_SLrD7xRxB-OEcZ3JwIGyPij_-rmyyUGsMf8WOede375NubpMMlNT93yte2ulVriTBFfb_sy1kmhaoE8lTJWtcjvw5YeaF2YygfAbpCLXvQgFbSDwpCA8az6sCYFWJKptgp1GlKrX6RjG3iuV8hlg__djmyMf-cJTYhwnlSBwblfYJqDh6HhiP6l-0Q9eL7OfzEnEeJlH-HAPBWfmZZRdcMnGZ03oaVs5HSDh0D_f89cJ8BPYL2WbK3fe7dJrU87ZDOQsrdMz8YBgFHymDvccUfGc8HjhJKTW8LupcRMn6xOaPFJiXL5uaH2-b1Ev8-6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zeg8xGOkIQ7iSLLtxNxJofG5Y4p9IooFfzBPxTq9KhG5iFfmdvxIbiSig2YNqKMBZwoPKDWqY3n8QSCggS2Jh5gen_BdacEDnLs_j7PBhzFE2h_5GEfTyEyCUbhN01fazT3SwmvtDxD64SHHyOudL98Aiw9dC3J_h4fs-HprKErqXBA6-ZqcLc1yOtIzzxhhnYhf0ODzkJDEUQ8IYgvKES7nzWXAcVJFIXoS5mfjZKzFcZzyFDWxO2CYzYJY-uJB6wgUOWuPsROB9iPPb0rhOJfi03r22GxDf5d6lskCc1Lg_L_LJG7AEFlQ5ezeVkxc4ls26hNBWGHOVyqBkblv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls9yZDNZX6b3226hwuAcTRXHsDa2vEckYi_AUvVdD1zC2NbdYJl212WlgTXHMPoE0GXlBo9PK7rOgApkJQtS_jf5brVKTPCev8OVQsyZEMZU_hsRGCmgyYXYph5aZDC_fSvKvoS84j1wZRtrI846sBURSRqOOTcWbMxbZxWAb_vfTlzaV1dXceu7yS4eGlyVCZpFdLfxuuWe30RIKfpnXJSz3CpT8BF5nUoldOlnoRakIxH_NAFNNuE03rRFnuBgvRuUaHkMcpJ178Ol6TrbVRc_o9C0Y1OUK7ZPsdMKgx856jFSL0ZF1JRY11Gbf-7q8UoJgbWkydbSuiTbR2B6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2f8XKiZmUtgC6f77EuGbC5xjiin0QYL5LeP2B1BCZSyyP_ZNlH7fIXuDmn_Ibv4s8GzcWanQGFqCbIboc2ap63f7VYrrkFAHb8aJT_Kqm1IDZbPVfkqS_FEm-IwA2Ah_rxd3fVQ13qa1B8j1jBiuBwUCV1u5uEenWN3CVLPpAM4hbwYrPQOKG8Pi1YOOlSI45szc3ic9C4M1NqGf-oMwq2zJq6q0ve_Mj_t3EQOLFour9aCjmOzafP2pErGS7CP2sbZ0bKaaiw6xDKnv3hDCK2UMvKYA7jK6Nf71z8JK6wR9wkTZLTB9kM9sLXDP-xYD2ynneo1hnXkweSbejkLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U07alxCCNcZJN9rmoj-rZu5xNSX0ST-N6EA73SOlGC75MNp2lCQF6zGuiwGWgQvOy_8SxgHbywaaB5poZGXO7Wt586Jpqmycd5FBddBuCK9desdTzwTIaNEV_7tamrIwp2Yz8uxH84Iwb8lsmVk4A71sHnBk2TXXVTA0J72x5FqoAX5L6gPMDQFF8lRhZDfHv_G-MtN6lAozHAyQ775vl7CBw1SAaNgWD205INNKLqqrtY5S07u9XXCxYl4-n4F17WSdN2SyNZpYjgFQFeqwwsC5BO-mzs9gGrOApKkp5WUHyW4zm4RLOFxU8MnzA_dyuAi0ghcGUuRf2cVwLsGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGYamTGfeszbL4tNwJ2iS5pORrmYraMdbjzp5KHkNdxd3uGsJ9TdIfsXx9qn2sTzhXYxazFGy4Cv3S4Tl7FK6lV3lV2FzdT93e004n4MRqu_ubvTCf9wlAvi32OId5ZArbOgkhmk_w6M1zlhIPP7WCkPB3x3Gdf2_OaOmD8ovBEzRq8bzGkfIoUJQ_5SKoW-oBRS-nF_YqSZZUEgdEAUkgrOU0y7oUD-gjdosG2oUj02afbL-PcbxZYhQgHe9Obg7Z7Y7i21FBXrpExFZe8fRSlSda1GNWRX5J6QSCMOGB4Mr1wM0hl8KWjVXSJFYRfDd3ty4lPx90ZlWXjc9P-XgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owwjl2tR2l9iAHrshaj0WY_SExtPVkxljNwQBcCVNXbPuVDN09qXtfU0NX0IaAM-EEBazrMTauXWUwUs4uGGbKm99I4t2iU9wOMdGlTVKlNJJf9XWvKmUlwsEGRgK1gz4k-Mid_AJT2T6KifMcdG1fAF0oyfH9nrO4rECgYGB2ZVquIXwhfnoFNM6vMz3BJKbyehlSFCRmbGbBacEYRMzSz_x_fsdy7JIlPvs0lcgOq39IP8-stVWPG4oWzrgI2QOOoYtZbI7826-Sxli1ZF8Kfl3HVl2sPeixJM8IMbIzB6pV1S-ppHh8WMcqXQurqEgyDlCjxJYXQ2DgrJ3H-ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itge3l4jsPpuevW0c_QkruYBuCGXkz1hG8TAkXr0lPnmmuhlu-BLA015iomIeB5hMnd1Rn76zbUbA_k19txC8At2ZyDJKMcSGChjXg57YWGRc1Z6uUQ7wION9kUKkg0H5CHwqvlbhL1Ar4DBZgqIdQ7qBOowOMpcHzAdugPHZQTeYFGGT4dsdNxCy2PXp1nF7lQD6qZTY8Zkfi79qi3cCOU485tSic-Wr1Abpcgz3Jl-p-bcxFjNrw1KR9KvsWez-GyuQ_ngEbcw3DTylxtkpn6RTg0rujJ67OylUBrcHJGrOBxjGnd_QfR_rxM7fkYmPPd8E1rEbic7qg3Mbso-5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjZC--Vsc3_7-gasWPndIRA7qV4fz0Av85tAx_dk2wp3xkowIZtprFclj2yg_en50IcoBC0izRRsXyZ16j9_AOAeR0mS1bEjj92YMN6cKC-dR5vL75mclryrLt8lb6E_s2s3RX7eqbR5S6SHIOaMeYgiaLiFhW2WMePJWCoNcO6ii0FAIFPybP0Uwl4RXADbCjIfk_ATdgoSZy_HjZe7w6Hbn3bK9L4mKYpCHeAtJMbHZlv6GykEtH2mmVizMDWSM9zNAqlqWr4pOyulFnr4hI9mZX2dpuhpNVj3PszfSPjLL0CsfsiE4JNdlDngyB38xVtgYx0cPjbgMOxcr-jB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzC4L8-Yv6mJsgFd2qrbxQlnmmnra2hPROEwtaoiuk7rmMYeqhC5gXpUxAKamdiI4wAVdYa4rz2J6iWFUEBLiRJUv4I9P2tC5OVHmxEBF4iaMzKrXRSObVixjWVV1znLA4UGAB4mVEDccupm1uH0TtmiY_P5oWPfPFnwEFnZSkIUowI21pT7R0e6pOOqkct3Tpput-7y6-_x8yzTSs5YztRPMA7yz3qLGINiJ8VkwLFDqJ0u3dicjdfUsJwOypgkj6JXGe-SnXexBezhLSvTtoL0WI1UYUwv-Uu50p2KojBRY7PWq-D3qG6qhlBtnWcIpqHQDx0vMLPmZpTiUovUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=FzHub7ocrZ3ywWr93vKUb5WPkIEaW2xf2wQUdHeiDZg40jzY76ILFBersok1f5367w13uPmMIabmzt_0Dph6exuT2OKwiE-o-MTx9KiYcPJTA-Iuv9kBFDL33dKwGDdz3pNnS3g5Wsr5JNE0xjzilXLpBmEGu74V77Amrb5lU457iX-1gNLeWEj72LpiINWESREgU7fuzRubwNFogukinUUBZAdOyj6l4ydvR2xDemp6nDB740OYtPsCMvLOnhCpAOzENnIyRccwh9NdvSG9rVmiGqkqX1ayRuU84YzSpA1FKuCJZ1bznSojciVfo_yYihtDz7WE6Rd0Ke7Vd-dGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=FzHub7ocrZ3ywWr93vKUb5WPkIEaW2xf2wQUdHeiDZg40jzY76ILFBersok1f5367w13uPmMIabmzt_0Dph6exuT2OKwiE-o-MTx9KiYcPJTA-Iuv9kBFDL33dKwGDdz3pNnS3g5Wsr5JNE0xjzilXLpBmEGu74V77Amrb5lU457iX-1gNLeWEj72LpiINWESREgU7fuzRubwNFogukinUUBZAdOyj6l4ydvR2xDemp6nDB740OYtPsCMvLOnhCpAOzENnIyRccwh9NdvSG9rVmiGqkqX1ayRuU84YzSpA1FKuCJZ1bznSojciVfo_yYihtDz7WE6Rd0Ke7Vd-dGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=MyhoR9QSEqjHLM0sbGkQs1wjCiHKm78fE1Q4i6Qtc3KGcDR0Fn10XL_LUDpk7DHAZT-AUBWXo6H3EMXZiFAJb-uRo1Y1KkI43RKUcFCmNbnuY5kJNvm8kp68rW283J3RiE-VgKktYTS6aI7sbhPPtCiZgEreiy-fa3F1-FJANkZVncnCy73flYqOxVuBFHdLc0d9A59iwPQIuPfXm1DkHrz1adnPiLQgHX7o7fHXvKN6EKpDPgkySpV9rVI0lqcNTDxbVakY2Zces9exJbPyP2XZRcxzN6-EyrMimC8JnTeuEQoxsFscW4kH74cRjeANNc_9pUcWGsuGTi2g7fX1Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=MyhoR9QSEqjHLM0sbGkQs1wjCiHKm78fE1Q4i6Qtc3KGcDR0Fn10XL_LUDpk7DHAZT-AUBWXo6H3EMXZiFAJb-uRo1Y1KkI43RKUcFCmNbnuY5kJNvm8kp68rW283J3RiE-VgKktYTS6aI7sbhPPtCiZgEreiy-fa3F1-FJANkZVncnCy73flYqOxVuBFHdLc0d9A59iwPQIuPfXm1DkHrz1adnPiLQgHX7o7fHXvKN6EKpDPgkySpV9rVI0lqcNTDxbVakY2Zces9exJbPyP2XZRcxzN6-EyrMimC8JnTeuEQoxsFscW4kH74cRjeANNc_9pUcWGsuGTi2g7fX1Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=ElNo6qiCu97T4jjan5YWYWWfUEp5rcFrnLGttJ5Hy42-FUnTu0X4SK-zjyeubpE8K4p3zt1_kglZdLUJj_5Z2da09V0WjDVrSyKXXl-OOywFYIfbyN61RJevATvddMuek5fKXnbA0KQNujB0sNDb2g6gei36etxQJSnAYOh3_4TMv_vMdVYfC49wpGMdXToyLwLJk5lp0yeXJosJ_jRON6prK2bXNHKf9iuPBRLUkc68SV19lAyHRDPU2wS8jqbuEVp2WphwXUzsYERt2RrQpQ8dr2lnQI4WKV-UziW6LPjg1TG80ql4zwCiblJmnDCzoPvtbabZUOVBtJ4Bivtp8JntP_W_mTG4dKL6Pinp29YQ4ENtCGQvnVj__OGNrWSl6tgPE499qyyyc_HGMSz_WmFpGD4rhi3-4qcsMgu4uUb7QPQp9pBP9Q4o9p3t42L-o0ddyWIVk9br2df6Sc2Fjihpa-9CyB91csYkBrYPAgfoDycDn42l_zmu7xEdUEcuyilez1xwyOjWgdkSZc0SMc-aRBiI_UrApmI-InXcu5NZ6_-WNnCSd1gQfTQihufPo8fcnc7MCoPd85wnFsiVHdaYxstsIcjWmIc4CgrF0D_BFKvkrpzIflksFZlS2fuC-JZvUMCxUp_CjUz8GMjVzuq_Xy_MpC4sBAWV4iCF1oY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=ElNo6qiCu97T4jjan5YWYWWfUEp5rcFrnLGttJ5Hy42-FUnTu0X4SK-zjyeubpE8K4p3zt1_kglZdLUJj_5Z2da09V0WjDVrSyKXXl-OOywFYIfbyN61RJevATvddMuek5fKXnbA0KQNujB0sNDb2g6gei36etxQJSnAYOh3_4TMv_vMdVYfC49wpGMdXToyLwLJk5lp0yeXJosJ_jRON6prK2bXNHKf9iuPBRLUkc68SV19lAyHRDPU2wS8jqbuEVp2WphwXUzsYERt2RrQpQ8dr2lnQI4WKV-UziW6LPjg1TG80ql4zwCiblJmnDCzoPvtbabZUOVBtJ4Bivtp8JntP_W_mTG4dKL6Pinp29YQ4ENtCGQvnVj__OGNrWSl6tgPE499qyyyc_HGMSz_WmFpGD4rhi3-4qcsMgu4uUb7QPQp9pBP9Q4o9p3t42L-o0ddyWIVk9br2df6Sc2Fjihpa-9CyB91csYkBrYPAgfoDycDn42l_zmu7xEdUEcuyilez1xwyOjWgdkSZc0SMc-aRBiI_UrApmI-InXcu5NZ6_-WNnCSd1gQfTQihufPo8fcnc7MCoPd85wnFsiVHdaYxstsIcjWmIc4CgrF0D_BFKvkrpzIflksFZlS2fuC-JZvUMCxUp_CjUz8GMjVzuq_Xy_MpC4sBAWV4iCF1oY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGrHKO8qZzjVKCaiFU2vm1bLqZUrk14X49ksDL87UE1FyZP_aFCfj1PoM949MtTKueFFTroEEU3LNkNZaUnTaGdz-bY1RXG7EupX3-oiE2ELTzPXTML9pcQOqKkFYd211bwyBHZdM-Fbg1BhybF_b6s5sxQ9V0WEm1pPyNh-Ja_1rPdDmcbx0yoCtg7Nk17A9So-6D_gNmUqxoZ6chkSzVUicVn_KNK5rCPWOtwrbkWLc3Yod_Ojex5Ps1QwPx8509H2U-aiknLsVOa0hylDn2iqDiKosGU1KH5UpFdPxHs9iNOsYRyl_vfHfKya0u7v-V9lrpp-gBDSXYCQPkl7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=NorgPA5HSJXbxYZ-vYRykPqG46J_SovNGWGm9FLKON77fHqxU_UXxqNYO7gexvksqh21tabn4WVorOqj0a9HOg5ClNeWQ8HbR7sC2WqC5BofmAd1jN-WqyZEUQicPxKreiP5hzUIfCgcNOo6aAlIgNOnwHRWapBb5sobJUFfZdmEoJGc974qGaG_jTyuc59NqjK360eLFGljT0FlFeyS4_Z968ngxG_we5iStytzb68r6Kl9Dn6d3e1vJj-7G9aYBqVW84RLq7Oy01I_qjm6CjHtgdKD1Y9Vc10b0pKjqskrgq8pHra9ZdzH3qXBtFuMX8hTf6Jp7txpKGcIRtq0gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=NorgPA5HSJXbxYZ-vYRykPqG46J_SovNGWGm9FLKON77fHqxU_UXxqNYO7gexvksqh21tabn4WVorOqj0a9HOg5ClNeWQ8HbR7sC2WqC5BofmAd1jN-WqyZEUQicPxKreiP5hzUIfCgcNOo6aAlIgNOnwHRWapBb5sobJUFfZdmEoJGc974qGaG_jTyuc59NqjK360eLFGljT0FlFeyS4_Z968ngxG_we5iStytzb68r6Kl9Dn6d3e1vJj-7G9aYBqVW84RLq7Oy01I_qjm6CjHtgdKD1Y9Vc10b0pKjqskrgq8pHra9ZdzH3qXBtFuMX8hTf6Jp7txpKGcIRtq0gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ZfUMAbe3ma1XDNSb405nbXmF-RAnaeo6r7s3wooGXCMH3yhbKeMuhwnbpyvm-bv_7DdLGBCD6-t-CXwYE8_0zGVhXJluNYH1mXy7GJWR3LdYR2zteArcMBFRtdUSaUZZP5QSO6LernuFBoeLUpx0LYkYVrK7D8LAjhwjHMjfEMShG8B-iKLB1AeKEFSvGlhpkOtvAACKL9gl4Vj3cKjAw4va0yCjZCWsROqahGYRInBhOb47CZFlFGL1FulZ1jNN3Bgv1tYV2XnMSY5_kbq_zLWCwieUkbzgwA4tSgm_dfudprYJ8w-pRH-REnOAYTsc0ZIAf6L2hjUsRDgXAHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD1daMvZ-rCxin_uLLYDEshvSfvpaBlrnoqDzTeAfQcT5F79aY3zmcQjrc6u2eHXftdU-Pn_5VTcDaIMbJKwZYFYS8kxEM2wUXXuFeACGqc8uWY_iF7JykbTsSTE3fgXuEzEOhlLdi-UdTq1h9tTy-kXNvbtx6QDJ0JvCxyXIT-92oAb9gtRPGryn3bSimDIwya4gGwZE8-RvuYc9DsqldmnR5aj_tKJVVYh-GHlGOy4eWbaDldRdPfyRySeHBAySrE_TjAILkia5Rb99uvMNOZSp4S_HeOTKBy9Pkbx5Cz2HU3ev0m9wmPe6WnLLVg-dri7s7gdVNeHQbKUWYthGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0TzhnVfFg3f0MJ6prAvFv8RdlFAfjC9iwLOOxvfbA8p-vsQMwnMj6WvQl9HxGs0jHJl2LABTcFE-mmhdnI7_uOq39cQ5eqQCIyOFTtmLV0ZLJ3MItNemyWhp6DdQja-ERGuhBpf9D8zHNtGzT2m81tzOqIVfN441VpY9dq79Cy-NLpETXNSYQtNJPbobqkC1gcY5uo7lWx0ZLjjm7P8fQL5PirqWYQB1p-NUraVRtRPCst3zGMcToN2_cUX36vTLEApd1y-w9XuBBr4eqWR9LUwZ9eAH9ZQJSrX8LdHzkwmAtRVCcE67WcKsqE1uADaRLpvzJZR96B9DThQ16F_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3Y1_KF5Q3uVvW_y4kW9D5NSBTCLW8TigsgzECWMPy-nuQzcPRy3YdsRUjND7pGcNA97I7T5D1VnYGy04vbh5LXJqsBFtGGN9GmQNA52JkT3v8M5s3Ud3ZoJpiJ4kI42Ax6ryjdoo7CY4c3WIVsnsC4epME0D3AJ3Vnupg6r_3ZA6q-pnRfABVAmLBlfPFxI0EYg2dn6Rv-NQVS7Ery__Xebb7m6AfWld0AYdWf3ImK7ZBjgTHbFgmWk1H6W7r6UkpaGppCM2VAK5QoByKHxaXQptIeSPwZtRz5UJAACPHW6j7LYL3O3gi-GyAuXKiyshfytHehDX1k7AJ_OODGNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjnUGLM0143pK3_SrVXMaabWKwKtUVaLF1bbBe-qk8JM2mJPRJ6hjaPtEHOnJ06M6-BN9pb46QZkmVa_v-wZUmRZys1n_UG3wJxWDo2h4HFnv3XCq41hzj064uCfO-dVBCt5xIcR46aT9L6l1T3rCc6TlFmh2DW9bVouwNWHxtes_k4LzDl45tIVGYMvmAkdEZxGFrDoWAElYqqHAAn-yCXmjMahX-eyXKMBVCO_RyobnCuCVYw4HiKpN1_1kWTaCrOmOcr7seNgUMN9mXk21dj_iAsR7p0g_KzT3vcIOKXNePzMu3CTVYuEHJ49mLUzUDLjCuqqPuzMMtYZJRsz7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3P6Oj_SsD9NmfW9BSJncL-q9WJlLLsMImYY6g1LKTfb5PRZBd-ciOoQSoBOvkZUOeSs8L7ckbNVYpuCt-sGGLoR66KZB8fsAj1nmgA9UyLbEdQqe8BDQDJrJmSLec8OtAjZsAmOSzITAoEPlBeUmo7MMqcxBWPKKHYfCVYs4QJQVDvOs2ixYIl32tuWNirM7skWYz9rQxEFw25-a_zS_b_27bBRQLsZaQSGOjdW0fEl48hvrcdlRBTQd2Xv_Jqf2810HufQ2Jtsbf63kB1X3-EiVcff1LFvNjC_y73JMLj-d2PAtjFbcRr9pGXyxFueC6Sx80CSriuYGFSS94zkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAI5Cjoj4QHyyyww6TnEal5y2vd_ej3whHgVAUOcKKOYI3-GfCb-qerrKcC-S8hR5XYWF_R9r5JjknGbkkX9KSUNGK0J-SikZrFth0OxrZ_bSMofPGxCfj0hDSaEno_5MHbrrSCDCd9YqIiLXH6OT1gYbKEe1g6XYQ9EXytdbTkf0BMNKt-MuEwrx5xv7HE2--4OZjZo8PdibnhSOAKNdMWwLdTL9pjy_au1yoci2JgBhIGa2kOnZr07dejIWPaN2rW9Q8qngRJ3EGGnIzIXNjof6tBJfBTe_Doy43AffoJ7q2X1pOOsEiSn94g3hlnnrhofM67xHhcXij0KweYFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BinzMcP9YgmZ97M0QtXsrTN4MXJK9oc242iNU_r60bwf6TlyjfgRLxRcLN3Yb-_SPYpyX9I8mVwIapyjBStFSMop_ZLwdAyBa_ehCH4lCJXy_p2ub1IUSIby_3aVM1AgwzQ9ZzrQ2xNaFJYYsOxRKEY4iyw5O_FHJavX9tEGV0D468HtJr6fnmsGjHujTQMlF47Z1lRwFynCvgAIXzzvxZkkh8WVRobL3JEOl8ybF4TB7ge-pNqS7xSv6pkr0MedUuVXBvbnSFQ_kXptHFLVkH_lN9noPdq3mry3ZNc5VbJq0Q3K0DHn0iXa-VeDYfxNa2X2hQMzo1JXcXcbUM0KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DunRyU04zjtEkwq4SeFeNbbpVrTGlsAiuRKkXeF5-PcQSc-NGsDar5PlU1Fw1KHi9C2P-TZsrvXRBANL4Ix6Lfvu9R7rhkqiCYOcJmVpKCF4yf1BYjN4xFz0JrZKrFu2zsVaMyvHjVcizcPRs3x9b-9nUe8pHiVARXpn_lOWMgAsdwdVzurYTk9QKG1mRARdeRc2laVntCe6VPYBk8taXtsn6CnpwFw0146v7suoDDMey7XbHjKz2Ai8jpGb7u3xLbNy5HwhgP8h21tNCDp9lgckjQowRu_ntc1Jj3wH3vaR7aTRZxLMFuXIG3BuzVhemdKDlAlRtrFxTVEDZmk7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BH9HoILMawJegO7GI9O99xj_HNkg6AOn-toZ6jIu3NemC-r7GUELfjkTPvbDhzbHERE-z9BuEy67Np7znli1LLYO2tonLwfo6LdI08-c62316H3B5taf7_4E3Imz6kzQ_Vas-pdnVSkwlmu8pngGP99XyROGkzjb42educF67UPPaYq4tKJKffncMslR7WwJ9xQ1X4c_5i_cF9Ts5Hc3ceGAQ_1C9fhI7DQtqlPCE1m5VwROU6ArbrmkYZ7D7Uh9Qg8qC5tkeeEqmAcsf2AiH8jJOKQNoq0uhCWecULABx_QznbpucSk0tLRc17quidmGSSY-prcYEQwqiSfj3rgnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwUAWDb428CbCzcNFjm0B9Y4e_2HN4_RIRFYBwp6Qq_aEE1OFqZrCq_-QB2HMr5_bJibDs5WR-Y_owcE-jmkC0YZjBw--sutuQPBwCVz1zlzxkO11mD1g9QJpyMRFtl0fIwL7cXCKB910B7mWrXXp5sGVJh504Ka_a1WTFSasiia1ignrhbXvLrm6GLWHmPYXaKFDeI6uU4vNQPDxYNiaLUI1NtUNLGhSWKpDY-DBtcc1U-Y9_70q4A-IQjI8jEW4rlfVILyyF2Kx-e0nVpT6iIO58HLbhcLW9R65h5eSRQ_mY6JxnY92f7pBBzhvelS2MVgubDNc74-wQt-cKsdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZOcSpI9OO7Yc_7a7SaZHqsH3JJya4XyY7okhM-Jh2v5LO8ym6cl7QgZe6ZjumM1MPRG5SnrW2zXeihibsyw2z-Xgt69-1oLLpUBzKgdK9EM0VkHpLuEWjDfaYkZOVHUhXWrktAkvynBjXpwpFBsF4daUja-qWh7dXDXmZxqj6c13zkb-L0fFeso9dyjgwxEC9uqUhF9OneQuAETkCvG9oGoj9Oim03OMfv31uZVZQX_szZSDQbA25pQGIA-0cG7m8n76YLkYLm-l44U_SvI2P29hlToFjhOIB_fgm6mEQR8gyUD82ikEfJvLpU9jnQJi67_f0EPWG8SVHae4m515g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XePsmK0olWn-D9_wXZ_Pl1eLhNphCYN2l_aNKyEnZBttMHeAgX-7ndzX6X1BllwbXJW7d_PlBvb3qxtMZhBS2-9vTWqzjdqIaEFYC4lT3mMgeWNT8nO9uQOpF_-qwhy-64-6G2UTKR02Nka8QiW7RgQuuiAo9Jt3Uw1OeWg-1ML3hXQpGMix0ywA4SMdkDx7VFjtaqrIKzt2mrUBklStlufjaYnMxD8AELhlBhvBRFUF55ina9XpBbdXr5Kb9xVbchrWqN8KU5R50jBewJ81htdNiJ9W578i8ju19QJ_hcDCXUeGTYYbKAJjXeg55oDxPjw2VGRfd5Ze2o38cbQz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQcFoK3VNu6yx7uHHZ-9VO-M6P_Ex3Pgj8Iu7OBgQ2Vu6Vz5Fxuc6ybGE4JsaZe2RABtl_ICMOvpa5VkPFn8kdyNQSuldWGSgf8zLM8TqsDIsTvJ_c96W3-UeenG9uqddMZFyaAHJl5JDmaYx7O308_8WzHYC1Oh-rKoi2Jaf0cfZ1AE_i7rNA5SA1eipOAhg2dEpbIZNrkq6KxYXvyyHA_KOTIgydlA5agkLIagQX6ryw8Opt6bdMAgy9F1hkK8l8fgPkUSP6bUDSnnuf82h-3ifoQyQXq2NfR78rlsKbayGP0gdU8qgnKAvknrKftpwcBhBiI2KLMKJgUIJXv8XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDDuDHFyCy1LffxOZa90h76AXs5GXlt1el-QPaomiaayicwJmaFwtogvuPZ0VQqw9I0_KXHGG7APSjYLo_DsJDY4Awn6bjrQcWcbUBJqyfYajAde3oBtPMtXe-pCXbcjT0cSv1ID3y0Med65tz6WakljsEj0foidgurdcdGCVpy5wrMG1RCPL9N8DmtHfygYVAYwjSPvi_30a8g_q1CAt3e8tkEpuzvH95FOjHSMGfltPtZ56qbogJCvjhlZ18Chef4J9tmr6tS-Tvat0Ct-1M665UbubF7UeJRylXPUpUab89ru1JbEVUwvFkh40jDD7iGBxEClPZOp9hsXaxn5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYPm38CogHW_yBXX2b_ElAxOfJ_6iTEL6WZ-hzyo-Gp6U5xyW0mXgVjMVl8Yx0Eb6iML7nNvf5U4Jf3V8XgayWo4LwEd5cYADCbZbixL2gJgbxiIOQN0vow7OUYTEKGSR3mZr_hZUucC0w4Xzbd5r4iLsfy1TezrPYncLsgn1TRdvZhajSBSSdfwHdC7qmeZI67YgS8BUfuFsXh4NTT3-A3SCP801AX_5a5DvWfDbYx5Ft4gBSXDcDr-BYGdallkg_ci_p4LnFIubyMAyAwFLPfkXZ3dwalqBwzR65ZiGs7VHSAJRSoOv1PpOGOUn70iWUVHPXXgKngszZwAm4fimg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX5HD23Eps3av3h7HLf0yAoMb7gM_b31pbBoCAUSMmnlQ_CiWjvavLdgylDamT6ZXO27wAqxNCHiJuoqKaLO1wwbnAG9muHdgWKJJQ5QFdZASv4MyNIQb1CNoT3o3GMxO5kHvPlMG8EmbZYGBPLv23Jp9mUjDnxDBRh0pxTnk2v6F2a0hPonjrDt7OINoVqOPijGWCQavCOH5y3VNpUxLdQ6VgOtGAcw76DCxagSU4J_gYlU1FpUOgKyTfW7K6Ot4x0RiCgrdsem_l_Sj4N1Y7J0X1ac1Rr1aoYC6TmTO6O_Jto34N6jgeFtUJ-CdQBNOdf6hfH39A05qWi_KnSJyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=gjZzuAouMlBDS38sY3rI2Dj6vJbsJQht8f7O8ykGIceGba2QaFrDN0QQsdZ8r9Imjk-sBevGnkYXt50bAeLroebZWVJwe8Okm_jz80XqtzRLBiwn27k_aK8PPy-4RZPOTkF3j6hSToT_aVO4Ho03UywdKvQ9il7Mb_z4Lxz53SSumruK2yUzReg7wX3RjOLTZmkylsMa3XecIPxipw-4CvTssYr_qdkykIioH6_H_-N0hWzT9ZdLs0bvBVbyOqvmw7jFbTzO95SWiCSwLRkD_u4zklbWdOxAFAfj2UA6yLk5l_3F_6yEDTLxWRY4XYC1uYAuT0K7XH3040CH6O_EiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=gjZzuAouMlBDS38sY3rI2Dj6vJbsJQht8f7O8ykGIceGba2QaFrDN0QQsdZ8r9Imjk-sBevGnkYXt50bAeLroebZWVJwe8Okm_jz80XqtzRLBiwn27k_aK8PPy-4RZPOTkF3j6hSToT_aVO4Ho03UywdKvQ9il7Mb_z4Lxz53SSumruK2yUzReg7wX3RjOLTZmkylsMa3XecIPxipw-4CvTssYr_qdkykIioH6_H_-N0hWzT9ZdLs0bvBVbyOqvmw7jFbTzO95SWiCSwLRkD_u4zklbWdOxAFAfj2UA6yLk5l_3F_6yEDTLxWRY4XYC1uYAuT0K7XH3040CH6O_EiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVPUUgF76D7L9cRZ7yJ7Hs3EZwuPudH1EGtIlt7-SO_3rIAsJPf3BZueXZnmkEmChnPkMqvzZs_iUILV7OvzUFoIAuWQBuSzi5gQG9-rAJsRcRA-3PABYMzugyTp3XEJD37-2UanOl1rOKiZ3ic2yiXAmTWjNNpP1cZpyYy2vW0mNelGxKrpZaVjgaeJokgIke5Bcdag4Jg3nVY1I_oe5XU4y3LMHiYE83LPWoQtCS_42hrVSaXSuM0Wkiuu0gdO7ayFEZSpD34laQ7wxO4NV-K4MUAPebQ2VJMzDpNhh43XbzewdFjPrhblnYmz-8dSVIr82PrPUB5vYgwV5cwY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYzZRrZzIdMnHO0eE0lzwt3kqDACRqkCZIV9qRlZifDG73xomBpaNn1tGHv-AHv4iXpqcm0ZaPZl-rkCZ0PoLEm0UGQSX4i3pPX39qseEBbdKmQSVNRryPxeQGn50bX9uUiYjvvKggzRZSzq7niN9mbzKBfhjpDcd1zm90SQT8f7Ks68lJdn_rYyobiM5vu6f6AA2pzbagmHUCuSaDeDzOGnYihYot2ZxBH51SVbkcHm46oi--5pGzbadKCsNxgI__kMexIGmH4qJcsWOIs3eUndLHsX75YzPk1EjP3a8Rsgd3RYD2PXEVxF8DBj9B9Yokv2SwCj3gLSrAghkkURfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
